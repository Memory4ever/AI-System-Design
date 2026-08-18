# Daily Research — 2026-07-01

**Research Date:** 2026-07-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-30 09:00:00 ～ 2026-07-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1331 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 28 个。当前路由账目为 8 个 Deep、4 个 Standard、16 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-01 |
| Window End | 2026-07-01 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-01-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T07:41:16+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-30T09:00:00+08:00 | 2026-07-01T09:00:00+08:00 | 2026-08-27T07:41:16+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1331 | SF-2026-ARXIV-2606-31033<br>SF-2026-ARXIV-2606-31093<br>SF-2026-ARXIV-2606-31144<br>SF-2026-ARXIV-2606-31145<br>SF-2026-ARXIV-2606-31160<br>SF-2026-ARXIV-2606-31167<br>SF-2026-ARXIV-2606-31276<br>SF-2026-ARXIV-2606-31315<br>SF-2026-ARXIV-2606-31329<br>SF-2026-ARXIV-2606-31382<br>SF-2026-ARXIV-2606-31410<br>SF-2026-ARXIV-2606-31519<br>SF-2026-ARXIV-2606-31700<br>SF-2026-ARXIV-2606-31723<br>SF-2026-ARXIV-2606-31734<br>SF-2026-ARXIV-2606-31846<br>SF-2026-ARXIV-2606-31903<br>SF-2026-ARXIV-2607-02574<br>SF-2026-ARXIV-2606-32012<br>SF-2026-ARXIV-2606-32017<br>SF-2026-ARXIV-2606-32026<br>SF-2026-ARXIV-2606-32028<br>SF-2026-ARXIV-2606-32032<br>SF-2026-ARXIV-2606-32034<br>SF-2026-ARXIV-2607-00151<br>SF-2026-ARXIV-2607-02577<br>SF-2026-ARXIV-2607-00248<br>SF-2026-ARXIV-2607-00272 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-01T09:00:00+08:00 | coverage:SRC-ARXIV:20260701 | GAP-ARXIV-DIRECT-RESET-20260701 |
| SRC-GITHUB-COMMIT | 2026-06-30T09:00:00+08:00 | 2026-07-01T09:00:00+08:00 | 2026-08-27T07:41:16+08:00 | exact GitHub commit API lookups: Sakuraaa0/RaBitQCache@3324489eafee6b16e28ff87bebce41ced7d921e6 | checked | 1 | SF-2026-ARXIV-2606-31519 | pages=1; final cursors=3324489eafee6b16e28ff87bebce41ced7d921e6; one bounded commit lookup per family | 2026-07-01T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260701 | — |

<!-- coverage:SRC-ARXIV:20260701:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1331 unique identities in this strict window; 28 routed families.<!-- coverage:SRC-ARXIV:20260701:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260701:start -->repository=Sakuraaa0/RaBitQCache, until=2026-06-30T11:32:14Z, full_sha=3324489eafee6b16e28ff87bebce41ced7d921e6, commit_timestamp=2026-05-18T02:49:58Z, url=https://api.github.com/repos/Sakuraaa0/RaBitQCache/commits/3324489eafee6b16e28ff87bebce41ced7d921e6; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260701:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 28 个 family：exact v1 为 9 个 family 披露 artifact/evidence locator，其中 8 个提供外部 repository/project/demo locator，另有 19 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-31033 | arXiv:2606.31033v1 | paper-v1:2606.31033 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31033 | self | — | new_in_window | AGENT-RAG | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31093 | arXiv:2606.31093v1 | paper-v1:2606.31093 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-31093 | self | — | new_in_window | INFER-SGLANG | Integrate | books-review:SF-2026-ARXIV-2606-31093 | no |
| SF-2026-ARXIV-2606-31144 | arXiv:2606.31144v1 | paper-v1:2606.31144 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31144 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31145 | arXiv:2606.31145v1 | paper-v1:2606.31145 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-31145 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-31145 | no |
| SF-2026-ARXIV-2606-31160 | arXiv:2606.31160v1 | paper-v1:2606.31160 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31160 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31167 | arXiv:2606.31167v1 | paper-v1:2606.31167 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31167 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31276 | arXiv:2606.31276v1 | paper-v1:2606.31276 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31276 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31315 | arXiv:2606.31315v1 | paper-v1:2606.31315 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-31315 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-31315 | no |
| SF-2026-ARXIV-2606-31329 | arXiv:2606.31329v1 | paper-v1:2606.31329 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31329 | self | — | new_in_window | WORLDVIEW-SYSTEM-EVOLUTION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31382 | arXiv:2606.31382v1 | paper-v1:2606.31382 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31382 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31410 | arXiv:2606.31410v1 | paper-v1:2606.31410 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-31410 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-31410 | no |
| SF-2026-ARXIV-2606-31519 | arXiv:2606.31519v1 | paper-v1:2606.31519 | 2026-W27 | 2026-06-30 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-31519 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-31519 | yes |
| SF-2026-ARXIV-2606-31700 | arXiv:2606.31700v1 | paper-v1:2606.31700 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31700 | self | — | new_in_window | TRAIN-GRPO | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31723 | arXiv:2606.31723v1 | paper-v1:2606.31723 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31723 | self | — | new_in_window | WORLDVIEW-SYSTEM-EVOLUTION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31734 | arXiv:2606.31734v1 | paper-v1:2606.31734 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-31734 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-31734 | no |
| SF-2026-ARXIV-2606-31846 | arXiv:2606.31846v1 | paper-v1:2606.31846 | 2026-W27 | 2026-06-30 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31846 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-31903 | arXiv:2606.31903v1 | paper-v1:2606.31903 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-31903 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02574 | arXiv:2607.02574v1 | paper-v1:2607.02574 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02574 | self | — | new_in_window | INFER-KV-CACHE | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-32012 | arXiv:2606.32012v1 | paper-v1:2606.32012 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-32012 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-32017 | arXiv:2606.32017v1 | paper-v1:2606.32017 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-32017 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32017 | no |
| SF-2026-ARXIV-2606-32026 | arXiv:2606.32026v1 | paper-v1:2606.32026 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-32026 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-32028 | arXiv:2606.32028v1 | paper-v1:2606.32028 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2606-32028 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2606-32032 | arXiv:2606.32032v1 | paper-v1:2606.32032 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-32032 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32032 | no |
| SF-2026-ARXIV-2606-32034 | arXiv:2606.32034v1 | paper-v1:2606.32034 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-32034 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32034 | no |
| SF-2026-ARXIV-2607-00151 | arXiv:2607.00151v1 | paper-v1:2607.00151 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-00151 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-00151 | no |
| SF-2026-ARXIV-2607-02577 | arXiv:2607.02577v1 | paper-v1:2607.02577 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02577 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-02577 | no |
| SF-2026-ARXIV-2607-00248 | arXiv:2607.00248v1 | paper-v1:2607.00248 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-00248 | self | — | new_in_window | WORLDVIEW-SYSTEM-EVOLUTION | Version Fact / Mechanism Not Disclosed | — | no |
| SF-2026-ARXIV-2607-00272 | arXiv:2607.00272v1 | paper-v1:2607.00272 | 2026-W27 | 2026-07-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-00272 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-00272 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-31033 | RP-b4d63ce6a48b270a | closure | doi:10.48550/arxiv.2606.31033@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31033@v1 | doi:10.48550/arxiv.2606.31033#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31033 | complete |
| SF-2026-ARXIV-2606-31093 | RP-6a0b4f9037a2ee98 | deep | arXiv:2606.31093v1 | SRC-ARXIV@arXiv:2606.31093v1 | https://arxiv.org/html/2606.31093v1#S3 :: declarative cyclic graph, streaming frames, OR-AND activation and static plan; https://arxiv.org/html/2606.31093v1#S4 :: framework-owned global KV/tensor pools, tiered storage and distributed metadata; https://arxiv.org/html/2606.31093v1#S5 :: SGLang interface takeover and common LLM/DiT execution path | https://arxiv.org/html/2606.31093v1#S7 :: three supported deployment scenarios are described; the v1 paper does not publish a controlled benchmark or independent comparison | https://arxiv.org/html/2606.31093v1#S7 :: framework is early-stage; performance, attention variants, TP/CP transfer, cache-aware scheduling and broader model coverage remain future work | https://github.com/meituan-longcat/omni-flow.git :: author repository linked by arXiv v1; event-time commit was not established, so implementation evidence remains manuscript-scoped | claim:SF-2026-ARXIV-2606-31093 | complete |
| SF-2026-ARXIV-2606-31144 | RP-4796c412283887c7 | closure | doi:10.48550/arxiv.2606.31144@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31144@v1 | doi:10.48550/arxiv.2606.31144#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31144 | complete |
| SF-2026-ARXIV-2606-31145 | RP-f3a432ea8737b930 | standard | arXiv:2606.31145v1 | SRC-ARXIV@arXiv:2606.31145v1 | https://arxiv.org/html/2606.31145v1#S3 :: entropy-guided spans, GPU routing summaries, query-adaptive zoom and CPU-resident low-rank bases | https://arxiv.org/html/2606.31145v1#S4 :: author evaluation covers long-context retrieval/reasoning workloads and several open-weight backbones; performance figures are not promoted outside that contract | https://arxiv.org/html/2606.31145v1#S6 :: sensitivity to span quality and thresholds, host-device bandwidth, adversarial repeated activation and untested broader modalities | https://github.com/AmirAbaskohi/SeKV :: author code linked by arXiv v1; event-time commit was not established, so code is supporting material only | claim:SF-2026-ARXIV-2606-31145 | complete |
| SF-2026-ARXIV-2606-31160 | RP-796fd597afebb131 | closure | doi:10.48550/arxiv.2606.31160@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31160@v1 | doi:10.48550/arxiv.2606.31160#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31160 | complete |
| SF-2026-ARXIV-2606-31167 | RP-a5ce187b4299c7bd | closure | doi:10.48550/arxiv.2606.31167@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31167@v1 | doi:10.48550/arxiv.2606.31167#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31167 | complete |
| SF-2026-ARXIV-2606-31276 | RP-781a7a6aa25ccabb | closure | doi:10.48550/arxiv.2606.31276@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31276@v1 | doi:10.48550/arxiv.2606.31276#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31276 | complete |
| SF-2026-ARXIV-2606-31315 | RP-a0b23f919ddad3bf | deep | arXiv:2606.31315v1 | SRC-ARXIV@arXiv:2606.31315v1 | https://arxiv.org/html/2606.31315v1#S2.SS3 :: local candidate interval and hidden-state classifier for per-instance block size; https://arxiv.org/html/2606.31315v1#S2.SS4 :: label construction and model integration | https://arxiv.org/html/2606.31315v1#S3 :: author evaluation spans math, code and chat workloads with autoregressive and diffusion speculation baselines; no result is externalized as a production constant | https://arxiv.org/html/2606.31315v1#A3 :: offline label search scales with model and candidate count; broader policy generalization and cheaper search remain open | https://github.com/AMAP-ML/BlockPilot :: author repository linked by arXiv v1; event-time commit was not established, so code is supporting material only | claim:SF-2026-ARXIV-2606-31315 | complete |
| SF-2026-ARXIV-2606-31329 | RP-857026a8a839de09 | closure | doi:10.48550/arxiv.2606.31329@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31329@v1 | doi:10.48550/arxiv.2606.31329#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31329 | complete |
| SF-2026-ARXIV-2606-31382 | RP-e3f79233b0f9b9e3 | closure | doi:10.48550/arxiv.2606.31382@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31382@v1 | doi:10.48550/arxiv.2606.31382#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31382 | complete |
| SF-2026-ARXIV-2606-31410 | RP-a5d87450a79288dd | standard | arXiv:2606.31410v1 | SRC-ARXIV@arXiv:2606.31410v1 | https://arxiv.org/html/2606.31410v1#S4.SS2 :: observation, reflection, local plan/replan, decision and cross-step memory tags; https://arxiv.org/html/2606.31410v1#S5 :: executable task verification | https://arxiv.org/html/2606.31410v1#S6 :: author experiments bind a GUI-specific model, real-device/emulator data and public GUI benchmarks; headline results are not generalized | https://arxiv.org/html/2606.31410v1#S3 :: static/off-policy corpora do not match visited state distributions; evolving apps, asynchronous loading and long-tail device states remain deployment constraints | Not Disclosed — no public event-time repository or model artifact is used for a mechanism claim | claim:SF-2026-ARXIV-2606-31410 | complete |
| SF-2026-ARXIV-2606-31519 | RP-f550176f2d368e5c | deep | arXiv:2606.31519v1 | SRC-ARXIV@arXiv:2606.31519v1; SRC-GITHUB-COMMIT@commit:3324489eafee6b16e28ff87bebce41ced7d921e6 | https://arxiv.org/html/2606.31519v1#S3.SS2 :: randomized rotation, 1-bit Key index, correction factor and unbiased estimator; https://arxiv.org/html/2606.31519v1#S3.SS3 :: INT4 Query scan, adaptive Top-p selection, exact selected KV plus local window; https://arxiv.org/html/2606.31519v1#S3.SS4 :: asynchronous Prefill index construction and lazy Decode updates; https://arxiv.org/html/2606.31519v1#A1.SS3 :: unbiased estimator, high-probability error bound and an explicit Top-p application remark; the remark is rationale, not a Top-p mass or retrieval-quality theorem; https://arxiv.org/html/2606.31519v1#A1.SS4 :: proofs of estimator unbiasedness/error bound and query-quantization error | https://arxiv.org/html/2606.31519v1#S4.SS1 :: vLLM 0.10.2, FlashInfer 0.5.3, LMCache, Triton/custom CUDA and NVIDIA Hopper architecture (exact GPU SKU not disclosed); https://arxiv.org/html/2606.31519v1#S4.SS2 :: LongBench, RULER 8K-64K and GSM8K on LongChat-7B and LLaMA-3.1 8B/70B with baseline configurations and p thresholds; https://arxiv.org/html/2606.31519v1#S4.SS3 :: TTFT, TBT and end-to-end latency for 10K-32K contexts; author maximums are 3.88x TBT and 2.16x end-to-end, not production constants | https://arxiv.org/html/2606.31519v1#S4.SS4 :: p-sensitivity and centroid re-centering ablation; removing re-centering changes LongBench average 50.63 to 50.25; the uniform-hypersphere assumption may fail for clustered Q/K and under Decode drift; https://arxiv.org/html/2606.31519v1#A3.SS1 :: index-space derivation; https://arxiv.org/html/2606.31519v1#A3.SS2 :: complexity derivation; exact GPU SKU, serving concurrency, arrival process, precision outside the selector, tail-SLO and independent replication are not disclosed | https://github.com/Sakuraaa0/RaBitQCache/tree/3324489eafee6b16e28ff87bebce41ced7d921e6 :: exact pre-v1 author repository tree contains benchmark, csrc, rabitqcache and efficiency-integration paths; the tree has one commit and no tagged release; accessed 2026-08-27 | claim:SF-2026-ARXIV-2606-31519 | complete |
| SF-2026-ARXIV-2606-31700 | RP-7a21fb45815e3741 | closure | doi:10.48550/arxiv.2606.31700@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31700@v1 | doi:10.48550/arxiv.2606.31700#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31700 | complete |
| SF-2026-ARXIV-2606-31723 | RP-a477118b454c4ead | closure | doi:10.48550/arxiv.2606.31723@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31723@v1 | doi:10.48550/arxiv.2606.31723#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31723 | complete |
| SF-2026-ARXIV-2606-31734 | RP-67d30fafa1f7bb02 | deep | arXiv:2606.31734v1 | SRC-ARXIV@arXiv:2606.31734v1 | https://arxiv.org/html/2606.31734v1#S3.SS2 :: learned query tokens extract timestep- and frame-dependent information from context under diffusion loss; https://arxiv.org/html/2606.31734v1#S4 :: mixed rendered/real data strategy | https://arxiv.org/html/2606.31734v1#S5 :: author evaluation and ablations cover long-video persistence on an internal 1B model and an open video backbone; no causal-control claim is retained | https://arxiv.org/html/2606.31734v1#S6 :: failures with many interacting characters, linear full-context growth, and open compression/update/forgetting problems | https://yujiwen.github.io/memlearner/ :: author project page linked by arXiv v1; no event-time code/model commit was established, so mechanism evidence remains manuscript-scoped | claim:SF-2026-ARXIV-2606-31734 | complete |
| SF-2026-ARXIV-2606-31846 | RP-18a1bbf8609a6438 | closure | doi:10.48550/arxiv.2606.31846@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31846@v1 | doi:10.48550/arxiv.2606.31846#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31846 | complete |
| SF-2026-ARXIV-2606-31903 | RP-c8fc1c925c0d9657 | closure | doi:10.48550/arxiv.2606.31903@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.31903@v1 | doi:10.48550/arxiv.2606.31903#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-31903 | complete |
| SF-2026-ARXIV-2607-02574 | RP-1c0d2f971229fcc5 | closure | doi:10.48550/arxiv.2607.02574@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02574@v1 | doi:10.48550/arxiv.2607.02574#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02574 | complete |
| SF-2026-ARXIV-2606-32012 | RP-a1af54268cba9ecd | closure | doi:10.48550/arxiv.2606.32012@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.32012@v1 | doi:10.48550/arxiv.2606.32012#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-32012 | complete |
| SF-2026-ARXIV-2606-32017 | RP-d249415b59918b3e | standard | arXiv:2606.32017v1 | SRC-ARXIV@arXiv:2606.32017v1 | https://arxiv.org/html/2606.32017v1#S2 :: segment roles and role-conditioned correction over GRPO advantage; https://arxiv.org/html/2606.32017v1#S4 :: MSE/variance rationale and failure conditions | https://arxiv.org/html/2606.32017v1#S5 :: author experiments cover three agent environments and two student policies; one search setting has only a single run | https://arxiv.org/html/2606.32017v1#S6 :: role labels are semantic estimates, context dependent and not causal identification | Not Disclosed — no exact public experiment commit is used in this Daily | claim:SF-2026-ARXIV-2606-32017 | complete |
| SF-2026-ARXIV-2606-32026 | RP-d65da5b217a465f8 | closure | doi:10.48550/arxiv.2606.32026@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.32026@v1 | doi:10.48550/arxiv.2606.32026#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-32026 | complete |
| SF-2026-ARXIV-2606-32028 | RP-ee1cc996982c64f9 | closure | doi:10.48550/arxiv.2606.32028@v1 | SRC-DATACITE@doi:10.48550/arxiv.2606.32028@v1 | doi:10.48550/arxiv.2606.32028#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2606-32028 | complete |
| SF-2026-ARXIV-2606-32032 | RP-dd9b0b8fc64571b1 | standard | arXiv:2606.32032v1 | SRC-ARXIV@arXiv:2606.32032v1 | https://arxiv.org/html/2606.32032v1#S2 :: intrinsic-confidence extraction, metacognitive data selection and metacognitive advantage scaling; https://arxiv.org/html/2606.32032v1#A2 :: training details | https://arxiv.org/html/2606.32032v1#S4 :: author numerical/factual evaluations and ablations are task- and model-scoped; expressed confidence is not promoted as a universal probability | https://arxiv.org/html/2606.32032v1#A3.SS3 :: equal-width cMFG has empty-bin and restricted-support failure modes; self-signal still requires external correctness calibration | https://github.com/yale-nlp/RLMF :: author code linked by arXiv v1; event-time commit was not established | claim:SF-2026-ARXIV-2606-32032 | complete |
| SF-2026-ARXIV-2606-32034 | RP-ee043635bd1fd137 | deep | arXiv:2606.32034v1 | SRC-ARXIV@arXiv:2606.32034v1 | https://arxiv.org/html/2606.32034v1#S2 :: reference-policy Q alignment as an offline contract for dense signals; https://arxiv.org/html/2606.32034v1#S3 :: controlled dataset construction | https://arxiv.org/html/2606.32034v1#S4 :: author comparison covers multiple signal families, environments, modalities and open-weight backbones; correlation is not causal credit or final policy quality | https://arxiv.org/html/2606.32034v1#S6 :: training-free Q alignment remains bound to reference-policy quality, trajectory coverage and controlled environment labels | https://q-val.com and its linked code/dataset are author artifacts; no event-time commit is used as evidence | claim:SF-2026-ARXIV-2606-32034 | complete |
| SF-2026-ARXIV-2607-00151 | RP-15a0b6d1da7f7db3 | deep | arXiv:2607.00151v1 | SRC-ARXIV@arXiv:2607.00151v1 | https://arxiv.org/html/2607.00151v1#S3 :: segment-decomposable context transforms, separate lookahead state and atomic promotion/commit; https://arxiv.org/html/2607.00151v1#S4 :: latency-critical versus best-effort scheduling under TTFT/TBT slack | https://arxiv.org/html/2607.00151v1#S6 :: author evaluation covers several context strategies, agent frameworks, concurrency settings and co-located/disaggregated serving; no headline speedup is retained | https://arxiv.org/html/2607.00151v1#S3.SS2 :: non-decomposable transforms cannot be safely advanced; https://arxiv.org/html/2607.00151v1#S4 :: stale latency models or contention can violate foreground SLO, requiring synchronous fallback | https://github.com/PanZaifeng/SmoothAgent :: author PVLDB artifact linked by arXiv v1; event-time commit was not established, so implementation evidence remains version-bounded by the manuscript | claim:SF-2026-ARXIV-2607-00151 | complete |
| SF-2026-ARXIV-2607-02577 | RP-a36e36382f707535 | deep | arXiv:2607.02577v1 | SRC-ARXIV@arXiv:2607.02577v1 | https://arxiv.org/html/2607.02577v1#S3 :: trace-level disagreement taxonomy, reproducibility analysis, corrected evaluator and deterministic-first protocol with restricted judge fallback | https://arxiv.org/html/2607.02577v1#S4 :: author audit covers four tool-calling benchmark families, complete traces, expert adjudication and repeated judge runs; it does not establish a new model ranking | https://arxiv.org/html/2607.02577v1#S5 :: evidence diagnoses selected benchmark/evaluator configurations; artifact release was still pending and evaluator agreement does not prove task representativeness | https://arxiv.org/html/2607.02577v1#S6 :: corrected artifacts and Harness Lab were announced but versioned public identifiers were not yet disclosed | claim:SF-2026-ARXIV-2607-02577 | complete |
| SF-2026-ARXIV-2607-00248 | RP-3bab6e8453beed5c | closure | arXiv:2607.00248v1 | SRC-ARXIV@arXiv:2607.00248v1 | Not Disclosed — historical model-card review at papers/2026/weekly/2026-W27/README.md#L488-L494 found no public training/runtime mechanism | papers/2026/weekly/2026-W27/README.md#L492-L494 :: line range; Experiments: evaluation 与限制已核对；训练 / 厂商 benchmark 不外推 :: model-card evaluation scope only | papers/2026/weekly/2026-W27/README.md#L492-L494 :: line range; Scope and Limitations: evaluation 与限制已核对；训练 :: vendor claims remain model-card scoped | Not Disclosed — no implementation artifact is used for a mechanism claim | claim:SF-2026-ARXIV-2607-00248 | complete |
| SF-2026-ARXIV-2607-00272 | RP-981e78ccb67cc32c | deep | arXiv:2607.00272v1 | SRC-ARXIV@arXiv:2607.00272v1 | https://arxiv.org/html/2607.00272v1#S2.SS2 :: trace-guided repair, validation and coordinator admission into a reusable skill library; https://arxiv.org/html/2607.00272v1#S2.SS3 :: evolutionary search | https://arxiv.org/html/2607.00272v1#S3 :: simulation and limited real-robot transfer bind the reported evidence to specific agents, APIs, embodiments and held-out trials | https://arxiv.org/html/2607.00272v1#S5 :: not a real-world lifelong learner; relies on a frontier model and predefined APIs; library staleness, duplication and revalidation remain open | Not Disclosed — no exact public experiment commit is used in this Daily | claim:SF-2026-ARXIV-2607-00272 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-31033:start -->
#### CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations

<!-- claim:SF-2026-ARXIV-2606-31033:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31033:end -->

- Identity：`arXiv:2606.31033v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31033:end -->

<!-- review:SF-2026-ARXIV-2606-31093:start -->
#### Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference

<!-- claim:SF-2026-ARXIV-2606-31093:start -->多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31093:end -->

**旧方案与约束变化。** `本章的核心判断是：**SGLang 将 language-model program 的结构暴露给 runtime，使 prefix reuse、structured generation 与并行分支不再只是应用层偶然模式，而能成为 KV management 和 scheduling 的输入。**`（`books/part-05-inference-system/51-sglang.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 它改变 `INFER-SGLANG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31093v1#S3 :: declarative cyclic graph, streaming frames, OR-AND activation and static plan; https://arxiv.org/html/2606.31093v1#S4 :: framework-owned global KV/tensor pools, tiered storage and distributed metadata; https://arxiv.org/html/2606.31093v1#S5 :: SGLang interface takeover and common LLM/DiT execution path`；Evaluation：`https://arxiv.org/html/2606.31093v1#S7 :: three supported deployment scenarios are described; the v1 paper does not publish a controlled benchmark or independent comparison`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31093v1#S7 :: framework is early-stage; performance, attention variants, TP/CP transfer, cache-aware scheduling and broader model coverage remain future work`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SGLANG`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2606-31093:end -->

<!-- review:SF-2026-ARXIV-2606-31144:start -->
#### A Modular Vision-Language-Action Robotics Framework for Indoor Environments

<!-- claim:SF-2026-ARXIV-2606-31144:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31144:end -->

- Identity：`arXiv:2606.31144v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31144:end -->

<!-- review:SF-2026-ARXIV-2606-31145:start -->
#### SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference

<!-- claim:SF-2026-ARXIV-2606-31145:start -->KV capacity can be managed as query-adaptive resolution rather than a binary keep/evict decision: compact GPU summaries choose spans, coarse contributions remain resident, and selected CPU bases are reconstructed on demand. This preserves recoverability but moves routing calibration, segmentation quality and host bandwidth into Decode correctness and latency. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31145:end -->

**旧方案与约束变化。** `Offload/recall can keep a recoverable cold tier and use query-dependent selection to fetch only the needed KV, but selector calibration, host transfer, prefetch misses and pinned-memory capacity enter the Decode critical path.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L350-L390`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** KV capacity can be managed as query-adaptive resolution rather than a binary keep/evict decision: compact GPU summaries choose spans, coarse contributions remain resident, and selected CPU bases are reconstructed on demand. This preserves recoverability but moves routing calibration, segmentation quality and host bandwidth into Decode correctness and latency. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31145v1#S3 :: entropy-guided spans, GPU routing summaries, query-adaptive zoom and CPU-resident low-rank bases`；Evaluation：`https://arxiv.org/html/2606.31145v1#S4 :: author evaluation covers long-context retrieval/reasoning workloads and several open-weight backbones; performance figures are not promoted outside that contract`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31145v1#S6 :: sensitivity to span quality and thresholds, host-device bandwidth, adversarial repeated activation and untested broader modalities`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2606-31145:end -->

<!-- review:SF-2026-ARXIV-2606-31160:start -->
#### Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving

<!-- claim:SF-2026-ARXIV-2606-31160:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31160:end -->

- Identity：`arXiv:2606.31160v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31160:end -->

<!-- review:SF-2026-ARXIV-2606-31167:start -->
#### MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents

<!-- claim:SF-2026-ARXIV-2606-31167:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31167:end -->

- Identity：`arXiv:2606.31167v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31167:end -->

<!-- review:SF-2026-ARXIV-2606-31276:start -->
#### AC$^2$P$^2$SL: Adaptive Communication-Computation Pipeline Parallel Split Learning over Edge Networks

<!-- claim:SF-2026-ARXIV-2606-31276:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31276:end -->

- Identity：`arXiv:2606.31276v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31276:end -->

<!-- review:SF-2026-ARXIV-2606-31315:start -->
#### BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding

<!-- claim:SF-2026-ARXIV-2606-31315:start -->固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31315:end -->

**旧方案与约束变化。** `本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**`（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31315v1#S2.SS3 :: local candidate interval and hidden-state classifier for per-instance block size; https://arxiv.org/html/2606.31315v1#S2.SS4 :: label construction and model integration`；Evaluation：`https://arxiv.org/html/2606.31315v1#S3 :: author evaluation spans math, code and chat workloads with autoregressive and diffusion speculation baselines; no result is externalized as a production constant`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31315v1#A3 :: offline label search scales with model and candidate count; broader policy generalization and cheaper search remain open`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L641-L656`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2606-31315:end -->

<!-- review:SF-2026-ARXIV-2606-31329:start -->
#### 3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance

<!-- claim:SF-2026-ARXIV-2606-31329:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31329:end -->

- Identity：`arXiv:2606.31329v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31329:end -->

<!-- review:SF-2026-ARXIV-2606-31382:start -->
#### Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation

<!-- claim:SF-2026-ARXIV-2606-31382:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31382:end -->

- Identity：`arXiv:2606.31382v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31382:end -->

<!-- review:SF-2026-ARXIV-2606-31410:start -->
#### Xiaomi-GUI-0 Technical Report

<!-- claim:SF-2026-ARXIV-2606-31410:start -->Real-device GUI execution requires local observation reconciliation, explicit deviation detection, replan and bounded cross-step memory because one wrong action changes the next state distribution. The workflow must own device/app revision, action coordinates, permissions, side effects and executable outcome evidence; model text is not authoritative environment state. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31410:end -->

**旧方案与约束变化。** `A recoverable Agent workflow must align model Context with controlled environment state at the same decision boundary; replay restores retained evidence rather than re-executing already committed side effects.`（`books/part-07-agent/81-workflow.md#L397-L420`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Real-device GUI execution requires local observation reconciliation, explicit deviation detection, replan and bounded cross-step memory because one wrong action changes the next state distribution. The workflow must own device/app revision, action coordinates, permissions, side effects and executable outcome evidence; model text is not authoritative environment state. 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31410v1#S4.SS2 :: observation, reflection, local plan/replan, decision and cross-step memory tags; https://arxiv.org/html/2606.31410v1#S5 :: executable task verification`；Evaluation：`https://arxiv.org/html/2606.31410v1#S6 :: author experiments bind a GUI-specific model, real-device/emulator data and public GUI benchmarks; headline results are not generalized`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31410v1#S3 :: static/off-policy corpora do not match visited state distributions; evolving apps, asynchronous loading and long-tail device states remain deployment constraints`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L833-L846`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2606-31410:end -->

<!-- review:SF-2026-ARXIV-2606-31519:start -->
#### RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference

<!-- claim:SF-2026-ARXIV-2606-31519:start -->固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31519:end -->

**旧方案与约束变化。** `KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算。`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31519v1#S3.SS2 :: randomized rotation, 1-bit Key index, correction factor and unbiased estimator; https://arxiv.org/html/2606.31519v1#S3.SS3 :: INT4 Query scan, adaptive Top-p selection, exact selected KV plus local window; https://arxiv.org/html/2606.31519v1#S3.SS4 :: asynchronous Prefill index construction and lazy Decode updates; https://arxiv.org/html/2606.31519v1#A1.SS3 :: unbiased estimator, high-probability error bound and an explicit Top-p application remark; the remark is rationale, not a Top-p mass or retrieval-quality theorem; https://arxiv.org/html/2606.31519v1#A1.SS4 :: proofs of estimator unbiasedness/error bound and query-quantization error`；Evaluation：`https://arxiv.org/html/2606.31519v1#S4.SS1 :: vLLM 0.10.2, FlashInfer 0.5.3, LMCache, Triton/custom CUDA and NVIDIA Hopper architecture (exact GPU SKU not disclosed); https://arxiv.org/html/2606.31519v1#S4.SS2 :: LongBench, RULER 8K-64K and GSM8K on LongChat-7B and LLaMA-3.1 8B/70B with baseline configurations and p thresholds; https://arxiv.org/html/2606.31519v1#S4.SS3 :: TTFT, TBT and end-to-end latency for 10K-32K contexts; author maximums are 3.88x TBT and 2.16x end-to-end, not production constants`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31519v1#S4.SS4 :: p-sensitivity and centroid re-centering ablation; removing re-centering changes LongBench average 50.63 to 50.25; the uniform-hypersphere assumption may fail for clustered Q/K and under Decode drift; https://arxiv.org/html/2606.31519v1#A3.SS1 :: index-space derivation; https://arxiv.org/html/2606.31519v1#A3.SS2 :: complexity derivation; exact GPU SKU, serving concurrency, arrival process, precision outside the selector, tail-SLO and independent replication are not disclosed`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2606-31519:end -->

<!-- review:SF-2026-ARXIV-2606-31700:start -->
#### Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks

<!-- claim:SF-2026-ARXIV-2606-31700:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31700:end -->

- Identity：`arXiv:2606.31700v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31700:end -->

<!-- review:SF-2026-ARXIV-2606-31723:start -->
#### UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models

<!-- claim:SF-2026-ARXIV-2606-31723:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31723:end -->

- Identity：`arXiv:2606.31723v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31723:end -->

<!-- review:SF-2026-ARXIV-2606-31734:start -->
#### MemLearner: Learning to Query Context memory for Video World Models

<!-- claim:SF-2026-ARXIV-2606-31734:start -->Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep. It improves selective reuse without granting causal world-state semantics, and introduces full-context growth, entity-binding error, query-policy drift and a separate need for compression, update and forgetting. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-31734:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep. It improves selective reuse without granting causal world-state semantics, and introduces full-context growth, entity-binding error, query-policy drift and a separate need for compression, update and forgetting. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.31734v1#S3.SS2 :: learned query tokens extract timestep- and frame-dependent information from context under diffusion loss; https://arxiv.org/html/2606.31734v1#S4 :: mixed rendered/real data strategy`；Evaluation：`https://arxiv.org/html/2606.31734v1#S5 :: author evaluation and ablations cover long-video persistence on an internal 1B model and an open video backbone; no causal-control claim is retained`；Limitations/Counterevidence：`https://arxiv.org/html/2606.31734v1#S6 :: failures with many interacting characters, linear full-context growth, and open compression/update/forgetting problems`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L747-L761`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2606-31734:end -->

<!-- review:SF-2026-ARXIV-2606-31846:start -->
#### Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2606-31846:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31846:end -->

- Identity：`arXiv:2606.31846v1`；first-public（Asia/Shanghai）：`2026-06-30`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31846:end -->

<!-- review:SF-2026-ARXIV-2606-31903:start -->
#### Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference

<!-- claim:SF-2026-ARXIV-2606-31903:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-31903:end -->

- Identity：`arXiv:2606.31903v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-31903:end -->

<!-- review:SF-2026-ARXIV-2607-02574:start -->
#### From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving

<!-- claim:SF-2026-ARXIV-2607-02574:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02574:end -->

- Identity：`arXiv:2607.02574v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02574:end -->

<!-- review:SF-2026-ARXIV-2606-32012:start -->
#### CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation

<!-- claim:SF-2026-ARXIV-2606-32012:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-32012:end -->

- Identity：`arXiv:2606.32012v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-32012:end -->

<!-- review:SF-2026-ARXIV-2606-32017:start -->
#### TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2606-32017:start -->Broadcasting one outcome advantage across a heterogeneous trajectory confuses exploration, infrastructure, decisive action and regression. Role-typed segment correction can reduce that dilution, but the role judge is not ground truth and cannot establish causal credit; its taxonomy, estimator and policy/verifier versions become training state. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-32017:end -->

**旧方案与约束变化。** `Typed Credit first aligns sample identity with role, block, subgoal and receiver-tested decision boundaries; local process signals remain subordinate to a hard outcome gate and do not establish causal credit by themselves.`（`books/part-04-training-system/33-grpo.md#L865-L890`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Broadcasting one outcome advantage across a heterogeneous trajectory confuses exploration, infrastructure, decisive action and regression. Role-typed segment correction can reduce that dilution, but the role judge is not ground truth and cannot establish causal credit; its taxonomy, estimator and policy/verifier versions become training state. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.32017v1#S2 :: segment roles and role-conditioned correction over GRPO advantage; https://arxiv.org/html/2606.32017v1#S4 :: MSE/variance rationale and failure conditions`；Evaluation：`https://arxiv.org/html/2606.32017v1#S5 :: author experiments cover three agent environments and two student policies; one search setting has only a single run`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32017v1#S6 :: role labels are semantic estimates, context dependent and not causal identification`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L888-L902`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2606-32017:end -->

<!-- review:SF-2026-ARXIV-2606-32026:start -->
#### AdaJEPA: An Adaptive Latent World Model

<!-- claim:SF-2026-ARXIV-2606-32026:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-32026:end -->

- Identity：`arXiv:2606.32026v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-32026:end -->

<!-- review:SF-2026-ARXIV-2606-32028:start -->
#### DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2606-32028:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2606-32028:end -->

- Identity：`arXiv:2606.32028v1`；first-public（Asia/Shanghai）：`2026-07-01`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2606-32028:end -->

<!-- review:SF-2026-ARXIV-2606-32032:start -->
#### Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs

<!-- claim:SF-2026-ARXIV-2606-32032:start -->Self-reported uncertainty can become a training signal only after binding intrinsic-confidence extraction to externally judged correctness. Metacognitive feedback may align expression with that internal signal, but does not make language confidence a calibrated probability and introduces self-signal collapse, metric dependence and reward-hacking risk. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-32032:end -->

**旧方案与约束变化。** `Reward uncertainty can prioritize trusted human or oracle feedback, but the learned reward remains a proxy whose calibration, distribution coverage and exploitability must be validated independently of policy optimization.`（`books/part-04-training-system/31-rlhf.md#L258-L303`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Self-reported uncertainty can become a training signal only after binding intrinsic-confidence extraction to externally judged correctness. Metacognitive feedback may align expression with that internal signal, but does not make language confidence a calibrated probability and introduces self-signal collapse, metric dependence and reward-hacking risk. 它改变 `TRAIN-RLHF` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.32032v1#S2 :: intrinsic-confidence extraction, metacognitive data selection and metacognitive advantage scaling; https://arxiv.org/html/2606.32032v1#A2 :: training details`；Evaluation：`https://arxiv.org/html/2606.32032v1#S4 :: author numerical/factual evaluations and ablations are task- and model-scoped; expressed confidence is not promoted as a universal probability`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32032v1#A3.SS3 :: equal-width cMFG has empty-bin and restricted-support failure modes; self-signal still requires external correctness calibration`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L732-L746`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-RLHF`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2606-32032:end -->

<!-- review:SF-2026-ARXIV-2606-32034:start -->
#### QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents

<!-- claim:SF-2026-ARXIV-2606-32034:start -->A dense supervision signal should be screened against future return or reference Q before paying for full policy training. This is a proxy-quality gate, not a deployment verifier: reference-policy coverage, horizon truncation and offline correlation still limit what the score proves. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2606-32034:end -->

**旧方案与约束变化。** `A dense process score is only a training proxy and must be checked against future return, terminal verifier evidence and critical slices; correlation does not make it causal credit or a deployment correctness gate.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L749-L752`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A dense supervision signal should be screened against future return or reference Q before paying for full policy training. This is a proxy-quality gate, not a deployment verifier: reference-policy coverage, horizon truncation and offline correlation still limit what the score proves. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2606.32034v1#S2 :: reference-policy Q alignment as an offline contract for dense signals; https://arxiv.org/html/2606.32034v1#S3 :: controlled dataset construction`；Evaluation：`https://arxiv.org/html/2606.32034v1#S4 :: author comparison covers multiple signal families, environments, modalities and open-weight backbones; correlation is not causal credit or final policy quality`；Limitations/Counterevidence：`https://arxiv.org/html/2606.32034v1#S6 :: training-free Q alignment remains bound to reference-policy quality, trajectory coverage and controlled environment labels`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L875-L887`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2606-32034:end -->

<!-- review:SF-2026-ARXIV-2607-00151:start -->
#### SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering

<!-- claim:SF-2026-ARXIV-2607-00151:start -->When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00151:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00151v1#S3 :: segment-decomposable context transforms, separate lookahead state and atomic promotion/commit; https://arxiv.org/html/2607.00151v1#S4 :: latency-critical versus best-effort scheduling under TTFT/TBT slack`；Evaluation：`https://arxiv.org/html/2607.00151v1#S6 :: author evaluation covers several context strategies, agent frameworks, concurrency settings and co-located/disaggregated serving; no headline speedup is retained`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00151v1#S3.SS2 :: non-decomposable transforms cannot be safely advanced; https://arxiv.org/html/2607.00151v1#S4 :: stale latency models or contention can violate foreground SLO, requiring synchronous fallback`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-00151:end -->

<!-- review:SF-2026-ARXIV-2607-02577:start -->
#### Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation

<!-- claim:SF-2026-ARXIV-2607-02577:start -->Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02577:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02577v1#S3 :: trace-level disagreement taxonomy, reproducibility analysis, corrected evaluator and deterministic-first protocol with restricted judge fallback`；Evaluation：`https://arxiv.org/html/2607.02577v1#S4 :: author audit covers four tool-calling benchmark families, complete traces, expert adjudication and repeated judge runs; it does not establish a new model ranking`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02577v1#S5 :: evidence diagnoses selected benchmark/evaluator configurations; artifact release was still pending and evaluator agreement does not prove task representativeness`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-02577:end -->

<!-- review:SF-2026-ARXIV-2607-00248:start -->
#### Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity

<!-- claim:SF-2026-ARXIV-2607-00248:start -->本次只保留 model-card identity、能力/安全/evaluation 公告范围；训练与 runtime 机制未披露。<!-- claim:SF-2026-ARXIV-2607-00248:end -->

- 历史核验位置：`papers/2026/weekly/2026-W27/README.md#L488-L494`。
- Score V2：1/1/1 = **3/9**。
- Disposition：`Version Fact / Mechanism Not Disclosed`；厂商 benchmark 不外推，不进入 Books 机制正文。
<!-- review:SF-2026-ARXIV-2607-00248:end -->

<!-- review:SF-2026-ARXIV-2607-00272:start -->
#### ASPIRE: Agentic /Skills Discovery for Robotics

<!-- claim:SF-2026-ARXIV-2607-00272:start -->A reusable Skill must be promoted from a failed trace through executable repair and validation, then stored with failure signature, applicability and provenance. Simulation success does not authorize real-world use; environment/API identity, supersession, revalidation and rollback remain platform-owned state. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-00272:end -->

**旧方案与约束变化。** `A derived Skill enters a temporary pool with provenance and typed applicability, then passes schema, permission, smoke-test and held-out evaluation before publish, supersession or rollback.`（`books/part-07-agent/84-agent-platform.md#L275-L308`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A reusable Skill must be promoted from a failed trace through executable repair and validation, then stored with failure signature, applicability and provenance. Simulation success does not authorize real-world use; environment/API identity, supersession, revalidation and rollback remain platform-owned state. 它改变 `AGENT-PLATFORM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.00272v1#S2.SS2 :: trace-guided repair, validation and coordinator admission into a reusable skill library; https://arxiv.org/html/2607.00272v1#S2.SS3 :: evolutionary search`；Evaluation：`https://arxiv.org/html/2607.00272v1#S3 :: simulation and limited real-robot transfer bind the reported evidence to specific agents, APIs, embodiments and held-out trials`；Limitations/Counterevidence：`https://arxiv.org/html/2607.00272v1#S5 :: not a real-world lifelong learner; relies on a frontier model and predefined APIs; library staleness, duplication and revalidation remain open`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L762-L777`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-PLATFORM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-00272:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-31519 | LongBench (13 tasks), RULER and GSM8K; efficiency subset uses LongBench | LongChat-7B-v1.5-32k; LLaMA-3.1-8B-Instruct; LLaMA-3.1-70B-Instruct | NVIDIA Hopper architecture; exact GPU SKU and topology Not Disclosed | 1-bit Key selector index plus INT4 query; attention and baseline precision Not Disclosed | LongBench variable; RULER 8K-64K; efficiency 10K-32K | Not Disclosed | Not Disclosed for end-to-end experiments | Not Disclosed | No production SLO; author reports TTFT, TBT, end-to-end latency and task quality | Authors; exact benchmark and evaluator versions Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-31093 | score_7_9;potential_books_delta | selected | DA-20260701-2606-31093 | — | V2=9/9；多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260701-2606-31093 |
| SF-2026-ARXIV-2606-31315 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2606-31315 |
| SF-2026-ARXIV-2606-31519 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。”；V2=3/2/3。与同为 8/9 且已入选的 SmoothAgent 相比，RaBitQCache 的长期增量集中在 KV selector/consumer 这一条局部执行链；SmoothAgent 同时改变 context transformation、best-effort scheduling、state promotion/cancellation 与 synchronous fallback，System Reach 为 3，因此优先占用跨层长叙事名额。RaBitQCache 仍保留完整 Deep Review、独立 Books 段落与 Integrate 决定。 | analysis-decision:SF-2026-ARXIV-2606-31519 |
| SF-2026-ARXIV-2606-31734 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2606-31734 |
| SF-2026-ARXIV-2606-32034 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“A dense supervision signal should be screened against future return or reference Q before paying for full policy training.”；V2=2/2/3。与同 owner 入选 `SF-2026-ARXIV-2607-02577` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2606-32034 |
| SF-2026-ARXIV-2607-00151 | score_7_9;potential_books_delta | selected | DA-20260701-2607-00151 | — | V2=8/9；When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260701-2607-00151 |
| SF-2026-ARXIV-2607-02577 | score_7_9;potential_books_delta | selected | DA-20260701-2607-02577 | — | V2=9/9；Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260701-2607-02577 |
| SF-2026-ARXIV-2607-00272 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“A reusable Skill must be promoted from a failed trace through executable repair and validation, then stored with failure signature, applicability and provenance.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-00272 |

<!-- analysis:DA-20260701-2607-02577:start -->
### Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation

**旧方案为何合理。** 本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260701-2607-02577:end -->

<!-- analysis:DA-20260701-2606-31093:start -->
### Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference

**旧方案为何合理。** 本章的核心判断是：**SGLang 将 language-model program 的结构暴露给 runtime，使 prefix reuse、structured generation 与并行分支不再只是应用层偶然模式，而能成为 KV management 和 scheduling 的输入。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-05-inference-system/51-sglang.md#L14-L14`）

**约束变化与机制。** 多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SGLANG` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260701-2606-31093:end -->

<!-- analysis:DA-20260701-2607-00151:start -->
### SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering

**旧方案为何合理。** 本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）

**约束变化与机制。** When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260701-2607-00151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-31315:start -->《BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding》已完成 Deep Source Review。本 family 的独立增量为“固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2606-31315:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-31519:start -->《RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference》已完成 Deep Source Review。本 family 的独立增量为“固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。”；V2=3/2/3。与同为 8/9 且已入选的 SmoothAgent 相比，RaBitQCache 的长期增量集中在 KV selector/consumer 这一条局部执行链；SmoothAgent 同时改变 context transformation、best-effort scheduling、state promotion/cancellation 与 synchronous fallback，System Reach 为 3，因此优先占用跨层长叙事名额。RaBitQCache 仍保留完整 Deep Review、独立 Books 段落与 Integrate 决定。<!-- analysis-decision:SF-2026-ARXIV-2606-31519:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-31734:start -->《MemLearner: Learning to Query Context memory for Video World Models》已完成 Deep Source Review。本 family 的独立增量为“Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2606-31734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-32034:start -->《QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents》已完成 Deep Source Review。本 family 的独立增量为“A dense supervision signal should be screened against future return or reference Q before paying for full policy training.”；V2=2/2/3。与同 owner 入选 `SF-2026-ARXIV-2607-02577` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2606-32034:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-00272:start -->《ASPIRE: Agentic /Skills Discovery for Robotics》已完成 Deep Source Review。本 family 的独立增量为“A reusable Skill must be promoted from a failed trace through executable repair and validation, then stored with failure signature, applicability and provenance.”；V2=2/2/3。它与入选 `SF-2026-ARXIV-2607-00151` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-00272:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-31093 | INFER-SGLANG | books/part-05-inference-system/51-sglang.md#L150 | books/part-05-inference-system/50-vllm.md#L14-L14; books/part-05-inference-system/52-dynamo.md#L14-L14 | existing:SF-2026-ARXIV-2606-31093 | delta:SF-2026-ARXIV-2606-31093 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-31093 |
| SF-2026-ARXIV-2606-31145 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L350-L390 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2606-31145 | delta:SF-2026-ARXIV-2606-31145 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-31145 |
| SF-2026-ARXIV-2606-31315 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L215 | books/part-05-inference-system/47-pagedattention.md#L14-L14; books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | existing:SF-2026-ARXIV-2606-31315 | delta:SF-2026-ARXIV-2606-31315 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-31315 |
| SF-2026-ARXIV-2606-31410 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L397-L420 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2606-31410 | delta:SF-2026-ARXIV-2606-31410 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-31410 |
| SF-2026-ARXIV-2606-31519 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L228 | books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2606-31519 | delta:SF-2026-ARXIV-2606-31519 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-31519 |
| SF-2026-ARXIV-2606-31734 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L346 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2606-31734 | delta:SF-2026-ARXIV-2606-31734 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-31734 |
| SF-2026-ARXIV-2606-32017 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L865-L890 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2606-32017 | delta:SF-2026-ARXIV-2606-32017 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32017 |
| SF-2026-ARXIV-2606-32032 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L258-L303 | books/part-04-training-system/30-lora.md#L14-L14; books/part-04-training-system/32-ppo.md#L14-L14 | existing:SF-2026-ARXIV-2606-32032 | delta:SF-2026-ARXIV-2606-32032 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32032 |
| SF-2026-ARXIV-2606-32034 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L749-L752 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2606-32034 | delta:SF-2026-ARXIV-2606-32034 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-32034 |
| SF-2026-ARXIV-2607-00151 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L483 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-00151 | delta:SF-2026-ARXIV-2607-00151 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-00151 |
| SF-2026-ARXIV-2607-02577 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L844 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-02577 | delta:SF-2026-ARXIV-2607-02577 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-02577 |
| SF-2026-ARXIV-2607-00272 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L275-L308 | books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-00272 | delta:SF-2026-ARXIV-2607-00272 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-00272 |

<!-- books-review:SF-2026-ARXIV-2606-31093:start --><!-- existing:SF-2026-ARXIV-2606-31093:start -->对读 `books/part-05-inference-system/51-sglang.md#L150` 与相邻章节后，现有命题（`books/part-05-inference-system/51-sglang.md#L14-L14`）为：本章的核心判断是：**SGLang 将 language-model program 的结构暴露给 runtime，使 prefix reuse、structured generation 与并行分支不再只是应用层偶然模式，而能成为 KV management 和 scheduling 的输入。**<!-- existing:SF-2026-ARXIV-2606-31093:end --><!-- delta:SF-2026-ARXIV-2606-31093:start -->新增证据边界：多模态 pipeline 不能只把异构模型串成应用 DAG：workflow activation、跨角色 tensor/KV identity 与 physical execution 必须由可分离但可提交的 Control Flow、Data Flow、Compute Flow 共同拥有。框架级 KV takeover 提高跨请求、跨角色和跨层级复用，却新增全局 metadata、layout compatibility、atomic eviction、failure recovery 与 runtime coupling；v1 没有提供受控性能 benchmark。 该 delta 已进入 `books/part-05-inference-system/51-sglang.md#L150`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2606-31093:end --><!-- books-review:SF-2026-ARXIV-2606-31093:end -->

<!-- books-review:SF-2026-ARXIV-2606-31145:start --><!-- existing:SF-2026-ARXIV-2606-31145:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L350-L390` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L350-L390`）为：Offload/recall can keep a recoverable cold tier and use query-dependent selection to fetch only the needed KV, but selector calibration, host transfer, prefetch misses and pinned-memory capacity enter the Decode critical path.<!-- existing:SF-2026-ARXIV-2606-31145:end --><!-- delta:SF-2026-ARXIV-2606-31145:start -->新增证据边界：KV capacity can be managed as query-adaptive resolution rather than a binary keep/evict decision: compact GPU summaries choose spans, coarse contributions remain resident, and selected CPU bases are reconstructed on demand. This preserves recoverability but moves routing calibration, segmentation quality and host bandwidth into Decode correctness and latency. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2606-31145:end --><!-- books-review:SF-2026-ARXIV-2606-31145:end -->

<!-- books-review:SF-2026-ARXIV-2606-31315:start --><!-- existing:SF-2026-ARXIV-2606-31315:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L215` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2606-31315:end --><!-- delta:SF-2026-ARXIV-2606-31315:start -->新增证据边界：固定 verify length 在 acceptance 分布稳定时简单，但不同输入的可安全推进深度不同。输入级 controller 可从当前 hidden state 选择局部候选 block size，再交给 target 做原有 verification；它不改变 correctness owner，却新增离线 label search、predictor drift、版本绑定与 batch opportunity-cost accounting。 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L215`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2606-31315:end --><!-- books-review:SF-2026-ARXIV-2606-31315:end -->

<!-- books-review:SF-2026-ARXIV-2606-31410:start --><!-- existing:SF-2026-ARXIV-2606-31410:start -->对读 `books/part-07-agent/81-workflow.md#L397-L420` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L397-L420`）为：A recoverable Agent workflow must align model Context with controlled environment state at the same decision boundary; replay restores retained evidence rather than re-executing already committed side effects.<!-- existing:SF-2026-ARXIV-2606-31410:end --><!-- delta:SF-2026-ARXIV-2606-31410:start -->新增证据边界：Real-device GUI execution requires local observation reconciliation, explicit deviation detection, replan and bounded cross-step memory because one wrong action changes the next state distribution. The workflow must own device/app revision, action coordinates, permissions, side effects and executable outcome evidence; model text is not authoritative environment state. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2606-31410:end --><!-- books-review:SF-2026-ARXIV-2606-31410:end -->

<!-- books-review:SF-2026-ARXIV-2606-31519:start --><!-- existing:SF-2026-ARXIV-2606-31519:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L228` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14`）为：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算。<!-- existing:SF-2026-ARXIV-2606-31519:end --><!-- delta:SF-2026-ARXIV-2606-31519:start -->新增证据边界：固定 Top-k 只约束 token 数，无法随不同 layer、head 与任务的 attention mass 改变预算。RaBitQCache 用随机旋转后的 1-bit Key 索引、校正因子和 INT4 Query scan 构造带误差界的无偏 proxy，据此按累计 attention mass 执行 Top-p，再只读取选中 KV 与局部窗口；Prefill 异步建索引、Decode lazy update 把 estimator 开销放进 phase-aware runtime。新增代价是在 KV FP16、校正因子 FP16、D=128 的论文 case study 中约 3.5% 的索引空间、线性索引扫描、p/分布假设与不规则选择执行，且 estimator guarantee 不等于最终语义质量保证。 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L228`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2606-31519:end --><!-- books-review:SF-2026-ARXIV-2606-31519:end -->

<!-- books-review:SF-2026-ARXIV-2606-31734:start --><!-- existing:SF-2026-ARXIV-2606-31734:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L346` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2606-31734:end --><!-- delta:SF-2026-ARXIV-2606-31734:start -->新增证据边界：Long-video memory can evolve from fixed recent-frame retrieval to a learned context-query layer whose read pattern changes by predicted frame and denoising timestep. It improves selective reuse without granting causal world-state semantics, and introduces full-context growth, entity-binding error, query-policy drift and a separate need for compression, update and forgetting. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L346`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2606-31734:end --><!-- books-review:SF-2026-ARXIV-2606-31734:end -->

<!-- books-review:SF-2026-ARXIV-2606-32017:start --><!-- existing:SF-2026-ARXIV-2606-32017:start -->对读 `books/part-04-training-system/33-grpo.md#L865-L890` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L865-L890`）为：Typed Credit first aligns sample identity with role, block, subgoal and receiver-tested decision boundaries; local process signals remain subordinate to a hard outcome gate and do not establish causal credit by themselves.<!-- existing:SF-2026-ARXIV-2606-32017:end --><!-- delta:SF-2026-ARXIV-2606-32017:start -->新增证据边界：Broadcasting one outcome advantage across a heterogeneous trajectory confuses exploration, infrastructure, decisive action and regression. Role-typed segment correction can reduce that dilution, but the role judge is not ground truth and cannot establish causal credit; its taxonomy, estimator and policy/verifier versions become training state. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2606-32017:end --><!-- books-review:SF-2026-ARXIV-2606-32017:end -->

<!-- books-review:SF-2026-ARXIV-2606-32032:start --><!-- existing:SF-2026-ARXIV-2606-32032:start -->对读 `books/part-04-training-system/31-rlhf.md#L258-L303` 与相邻章节后，现有命题（`books/part-04-training-system/31-rlhf.md#L258-L303`）为：Reward uncertainty can prioritize trusted human or oracle feedback, but the learned reward remains a proxy whose calibration, distribution coverage and exploitability must be validated independently of policy optimization.<!-- existing:SF-2026-ARXIV-2606-32032:end --><!-- delta:SF-2026-ARXIV-2606-32032:start -->新增证据边界：Self-reported uncertainty can become a training signal only after binding intrinsic-confidence extraction to externally judged correctness. Metacognitive feedback may align expression with that internal signal, but does not make language confidence a calibrated probability and introduces self-signal collapse, metric dependence and reward-hacking risk. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2606-32032:end --><!-- books-review:SF-2026-ARXIV-2606-32032:end -->

<!-- books-review:SF-2026-ARXIV-2606-32034:start --><!-- existing:SF-2026-ARXIV-2606-32034:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L749-L752` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L749-L752`）为：A dense process score is only a training proxy and must be checked against future return, terminal verifier evidence and critical slices; correlation does not make it causal credit or a deployment correctness gate.<!-- existing:SF-2026-ARXIV-2606-32034:end --><!-- delta:SF-2026-ARXIV-2606-32034:start -->新增证据边界：A dense supervision signal should be screened against future return or reference Q before paying for full policy training. This is a proxy-quality gate, not a deployment verifier: reference-policy coverage, horizon truncation and offline correlation still limit what the score proves. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2606-32034:end --><!-- books-review:SF-2026-ARXIV-2606-32034:end -->

<!-- books-review:SF-2026-ARXIV-2607-00151:start --><!-- existing:SF-2026-ARXIV-2607-00151:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L483` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-00151:end --><!-- delta:SF-2026-ARXIV-2607-00151:start -->新增证据边界：When a context rewrite is segment-decomposable, its transformed KV can be prepared as best-effort lookahead and promoted only at the semantic commit point. This removes work from the critical path without changing context policy, but requires separate main/lookahead state, freshness and cancellation semantics, latency-aware admission and synchronous fallback when slack disappears. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L483`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-00151:end --><!-- books-review:SF-2026-ARXIV-2607-00151:end -->

<!-- books-review:SF-2026-ARXIV-2607-02577:start --><!-- existing:SF-2026-ARXIV-2607-02577:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L844` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-02577:end --><!-- delta:SF-2026-ARXIV-2607-02577:start -->新增证据边界：Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L844`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-02577:end --><!-- books-review:SF-2026-ARXIV-2607-02577:end -->

<!-- books-review:SF-2026-ARXIV-2607-00272:start --><!-- existing:SF-2026-ARXIV-2607-00272:start -->对读 `books/part-07-agent/84-agent-platform.md#L275-L308` 与相邻章节后，现有命题（`books/part-07-agent/84-agent-platform.md#L275-L308`）为：A derived Skill enters a temporary pool with provenance and typed applicability, then passes schema, permission, smoke-test and held-out evaluation before publish, supersession or rollback.<!-- existing:SF-2026-ARXIV-2607-00272:end --><!-- delta:SF-2026-ARXIV-2607-00272:start -->新增证据边界：A reusable Skill must be promoted from a failed trace through executable repair and validation, then stored with failure signature, applicability and provenance. Simulation success does not authorize real-world use; environment/API identity, supersession, revalidation and rollback remain platform-owned state. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-00272:end --><!-- books-review:SF-2026-ARXIV-2607-00272:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260701-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260701; semantic-review:SA-20260701-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260701-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2606-31033; review:SF-2026-ARXIV-2606-31093; review:SF-2026-ARXIV-2606-31144; review:SF-2026-ARXIV-2606-31145; review:SF-2026-ARXIV-2606-31160; review:SF-2026-ARXIV-2606-31167; review:SF-2026-ARXIV-2606-31276; review:SF-2026-ARXIV-2606-31315; review:SF-2026-ARXIV-2606-31329; review:SF-2026-ARXIV-2606-31382; review:SF-2026-ARXIV-2606-31410; review:SF-2026-ARXIV-2606-31519; review:SF-2026-ARXIV-2606-31700; review:SF-2026-ARXIV-2606-31723; review:SF-2026-ARXIV-2606-31734; review:SF-2026-ARXIV-2606-31846; review:SF-2026-ARXIV-2606-31903; review:SF-2026-ARXIV-2607-02574; review:SF-2026-ARXIV-2606-32012; review:SF-2026-ARXIV-2606-32017; review:SF-2026-ARXIV-2606-32026; review:SF-2026-ARXIV-2606-32028; review:SF-2026-ARXIV-2606-32032; review:SF-2026-ARXIV-2606-32034; review:SF-2026-ARXIV-2607-00151; review:SF-2026-ARXIV-2607-02577; review:SF-2026-ARXIV-2607-00248; review:SF-2026-ARXIV-2607-00272; semantic-review:SA-20260701-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260701-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260701-2607-02577; analysis:DA-20260701-2606-31093; analysis:DA-20260701-2607-00151; semantic-review:SA-20260701-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260701-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2606-31093; books-review:SF-2026-ARXIV-2606-31145; books-review:SF-2026-ARXIV-2606-31315; books-review:SF-2026-ARXIV-2606-31410; books-review:SF-2026-ARXIV-2606-31519; books-review:SF-2026-ARXIV-2606-31734; books-review:SF-2026-ARXIV-2606-32017; books-review:SF-2026-ARXIV-2606-32032; books-review:SF-2026-ARXIV-2606-32034; books-review:SF-2026-ARXIV-2607-00151; books-review:SF-2026-ARXIV-2607-02577; books-review:SF-2026-ARXIV-2607-00272; semantic-review:SA-20260701-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260701-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260701-COVERAGE:end -->
<!-- semantic-review:SA-20260701-EVIDENCE:start -->Fresh-context review reconciled all 28 frozen families: 8 Deep, 4 Standard and 16 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260701-EVIDENCE:end -->
<!-- semantic-review:SA-20260701-SELECTION:start -->Fresh-context review reconciled 8 eligible Deep families: 3 selected and 5 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260701-SELECTION:end -->
<!-- semantic-review:SA-20260701-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 6 个 family 已定位到实际 Books 段落，6 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260701-BOOKS:end -->

## 8. Ignored Noise

1331 个窗口内 identity 中，1303 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：6 个 `Integrate`，6 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，15 个 `Rejected — Low Durability / Out of Scope`；Deep 8 / Standard 4。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/01/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/48-speculative-decoding.md`、`books/part-05-inference-system/51-sglang.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations](https://arxiv.org/abs/2606.31033v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [Omni-Flow: A Unified Workflow Orchestration and Distributed KV Cache Sharing Framework for Multimodal Inference](https://arxiv.org/abs/2606.31093v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [A Modular Vision-Language-Action Robotics Framework for Indoor Environments](https://arxiv.org/abs/2606.31144v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving](https://arxiv.org/abs/2606.31160v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents](https://arxiv.org/abs/2606.31167v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [AC$^2$P$^2$SL: Adaptive Communication-Computation Pipeline Parallel Split Learning over Edge Networks](https://arxiv.org/abs/2606.31276v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding](https://arxiv.org/abs/2606.31315v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance](https://arxiv.org/abs/2606.31329v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation](https://arxiv.org/abs/2606.31382v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [Xiaomi-GUI-0 Technical Report](https://arxiv.org/abs/2606.31410v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://arxiv.org/abs/2606.31519v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks](https://arxiv.org/abs/2606.31700v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models](https://arxiv.org/abs/2606.31723v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-27
- [Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models](https://arxiv.org/abs/2606.31846v1) — first-public（Asia/Shanghai）：2026-06-30；accessed：2026-08-26
- [Attend, Transform, or Silence: Operator-Level Visual Skipping for Efficient Multimodal LLM Inference](https://arxiv.org/abs/2606.31903v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving](https://arxiv.org/abs/2607.02574v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [CoMet: Context and Multiplicity Decomposition for Multimodal Uncertainty Estimation](https://arxiv.org/abs/2606.32012v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.32017v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [AdaJEPA: An Adaptive Latent World Model](https://arxiv.org/abs/2606.32026v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation](https://arxiv.org/abs/2606.32028v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs](https://arxiv.org/abs/2606.32032v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [QVal: Cheaply Evaluating Dense Supervision Signals for Long-Horizon LLM Agents](https://arxiv.org/abs/2606.32034v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [SmoothAgent: Efficient Long-Horizon LLM-Based Agent Serving with Lookahead Context Engineering](https://arxiv.org/abs/2607.00151v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/abs/2607.02577v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity](https://arxiv.org/abs/2607.00248v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-26
- [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272v1) — first-public（Asia/Shanghai）：2026-07-01；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
