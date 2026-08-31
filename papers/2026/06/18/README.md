# Daily Research — 2026-06-18

**Research Date:** 2026-06-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-17 09:00:00 ～ 2026-06-18 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；516/516 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 无未解决 finding

> Strict V2.1 Daily for `DEN-20260618-2977f506`. All V2.1 Gates passed after the complete 37/37 post-write fresh audit.

## Executive Summary

Beijing window `[2026-06-17 09:00, 2026-06-18 09:00)` contains 516 registered identities. Full 516/516 title+abstract screening freezes 37 durable families and 479 family-specific closures. Official exact-v1 HTML was reviewed for 37/37 families. Full-frontier selection freezes three winners before rationale. Books comparison yields 16 Integrate proposals and 21 No Change handoffs.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-18 |
| Window End | 2026-06-18 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260618-2977f506 |
| Denominator Frozen At | 2026-08-29T23:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-17T09:00:00+08:00 | 2026-06-18T09:00:00+08:00 | 2026-08-29T23:40:00+08:00 | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 516 | SF-2026-ARXIV-2606-18600; SF-2026-ARXIV-2606-18619; SF-2026-ARXIV-2606-18650; SF-2026-ARXIV-2606-18668; SF-2026-ARXIV-2606-18673; SF-2026-ARXIV-2606-18697; SF-2026-ARXIV-2606-18741; SF-2026-ARXIV-2606-18746; SF-2026-ARXIV-2606-18810; SF-2026-ARXIV-2606-18829; SF-2026-ARXIV-2606-18831; SF-2026-ARXIV-2606-18847; SF-2026-ARXIV-2606-18874; SF-2026-ARXIV-2606-18958; SF-2026-ARXIV-2606-18967; SF-2026-ARXIV-2606-18996; SF-2026-ARXIV-2606-19004; SF-2026-ARXIV-2606-19025; SF-2026-ARXIV-2606-19057; SF-2026-ARXIV-2606-19111; SF-2026-ARXIV-2606-19191; SF-2026-ARXIV-2606-19242; SF-2026-ARXIV-2606-19262; SF-2026-ARXIV-2606-19271; SF-2026-ARXIV-2606-19409; SF-2026-ARXIV-2606-19464; SF-2026-ARXIV-2606-19535; SF-2026-ARXIV-2606-19544; SF-2026-ARXIV-2606-19559; SF-2026-ARXIV-2606-19595; SF-2026-ARXIV-2606-19613; SF-2026-ARXIV-2606-19667; SF-2026-ARXIV-2606-20736; SF-2026-ARXIV-2606-20746; SF-2026-ARXIV-2606-21089; SF-2026-ARXIV-2606-21090; SF-2026-ARXIV-2606-28374 | pages=40; final_cursor=end; 516 unique identities | 2026-06-18T01:00:00Z | ../_sources/daily-20260618/screening-ledger.json; ../_sources/daily-20260618/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260618 | — |

<!-- coverage:SRC-ARXIV:20260618:start -->
All 357 Core, 55 keyword-routed and 104 route-negative identities were screened. Frozen arithmetic: `516 = 37 retained + 479 closures`. Route reconciliation: `{"keyword_daily_semantic_review_required": {"raw": 55, "retained": 5, "closure": 50}, "not_routed_by_keyword_contract": {"raw": 104, "retained": 1, "closure": 103}, "core_daily_semantic_review_required": {"raw": 357, "retained": 31, "closure": 326}}`. Keyword routing was recall-only.
<!-- coverage:SRC-ARXIV:20260618:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18600 | arXiv:2606.18600v1 | paper-v1:2606.18600 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18600 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-18600 | yes |
| SF-2026-ARXIV-2606-18619 | arXiv:2606.18619v1 | paper-v1:2606.18619 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18619 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-18619 | yes |
| SF-2026-ARXIV-2606-18650 | arXiv:2606.18650v1 | paper-v1:2606.18650 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18650 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18650 | yes |
| SF-2026-ARXIV-2606-18668 | arXiv:2606.18668v1 | paper-v1:2606.18668 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18668 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18668 | yes |
| SF-2026-ARXIV-2606-18673 | arXiv:2606.18673v1 | paper-v1:2606.18673 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18673 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18673 | yes |
| SF-2026-ARXIV-2606-18697 | arXiv:2606.18697v1 | paper-v1:2606.18697 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18697 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-18697 | yes |
| SF-2026-ARXIV-2606-18741 | arXiv:2606.18741v1 | paper-v1:2606.18741 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18741 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-18741 | yes |
| SF-2026-ARXIV-2606-18746 | arXiv:2606.18746v1 | paper-v1:2606.18746 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18746 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18746 | yes |
| SF-2026-ARXIV-2606-18810 | arXiv:2606.18810v1 | paper-v1:2606.18810 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18810 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18810 | yes |
| SF-2026-ARXIV-2606-18829 | arXiv:2606.18829v1 | paper-v1:2606.18829 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18829 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18829 | yes |
| SF-2026-ARXIV-2606-18831 | arXiv:2606.18831v1 | paper-v1:2606.18831 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18831 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-18831 | yes |
| SF-2026-ARXIV-2606-18847 | arXiv:2606.18847v1 | paper-v1:2606.18847 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18847 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-18847 | yes |
| SF-2026-ARXIV-2606-18874 | arXiv:2606.18874v1 | paper-v1:2606.18874 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18874 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18874 | yes |
| SF-2026-ARXIV-2606-18958 | arXiv:2606.18958v1 | paper-v1:2606.18958 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18958 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18958 | yes |
| SF-2026-ARXIV-2606-18967 | arXiv:2606.18967v1 | paper-v1:2606.18967 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18967 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-18967 | yes |
| SF-2026-ARXIV-2606-18996 | arXiv:2606.18996v1 | paper-v1:2606.18996 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18996 | yes |
| SF-2026-ARXIV-2606-19004 | arXiv:2606.19004v1 | paper-v1:2606.19004 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19004 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19004 | yes |
| SF-2026-ARXIV-2606-19025 | arXiv:2606.19025v1 | paper-v1:2606.19025 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19025 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-19025 | yes |
| SF-2026-ARXIV-2606-19057 | arXiv:2606.19057v1 | paper-v1:2606.19057 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19057 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19057 | yes |
| SF-2026-ARXIV-2606-19111 | arXiv:2606.19111v1 | paper-v1:2606.19111 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19111 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19111 | yes |
| SF-2026-ARXIV-2606-19191 | arXiv:2606.19191v1 | paper-v1:2606.19191 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19191 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19191 | yes |
| SF-2026-ARXIV-2606-19242 | arXiv:2606.19242v1 | paper-v1:2606.19242 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19242 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19242 | yes |
| SF-2026-ARXIV-2606-19262 | arXiv:2606.19262v1 | paper-v1:2606.19262 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19262 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-19262 | yes |
| SF-2026-ARXIV-2606-19271 | arXiv:2606.19271v1 | paper-v1:2606.19271 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19271 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19271 | yes |
| SF-2026-ARXIV-2606-19409 | arXiv:2606.19409v1 | paper-v1:2606.19409 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19409 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19409 | yes |
| SF-2026-ARXIV-2606-19464 | arXiv:2606.19464v1 | paper-v1:2606.19464 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19464 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19464 | yes |
| SF-2026-ARXIV-2606-19535 | arXiv:2606.19535v1 | paper-v1:2606.19535 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19535 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-19535 | yes |
| SF-2026-ARXIV-2606-19544 | arXiv:2606.19544v1 | paper-v1:2606.19544 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19544 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19544 | yes |
| SF-2026-ARXIV-2606-19559 | arXiv:2606.19559v1 | paper-v1:2606.19559 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19559 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19559 | yes |
| SF-2026-ARXIV-2606-19595 | arXiv:2606.19595v1 | paper-v1:2606.19595 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19595 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19595 | yes |
| SF-2026-ARXIV-2606-19613 | arXiv:2606.19613v1 | paper-v1:2606.19613 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19613 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19613 | yes |
| SF-2026-ARXIV-2606-19667 | arXiv:2606.19667v1 | paper-v1:2606.19667 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19667 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-19667 | yes |
| SF-2026-ARXIV-2606-20736 | arXiv:2606.20736v1 | paper-v1:2606.20736 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20736 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-20736 | yes |
| SF-2026-ARXIV-2606-20746 | arXiv:2606.20746v1 | paper-v1:2606.20746 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20746 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20746 | yes |
| SF-2026-ARXIV-2606-21089 | arXiv:2606.21089v1 | paper-v1:2606.21089 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21089 | self | — | new_in_window | TRAIN-DPO | Integrate | books-review:SF-2026-ARXIV-2606-21089 | yes |
| SF-2026-ARXIV-2606-21090 | arXiv:2606.21090v1 | paper-v1:2606.21090 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21090 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-21090 | yes |
| SF-2026-ARXIV-2606-28374 | arXiv:2606.28374v1 | paper-v1:2606.28374 | 2026-W25 | 2026-06-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28374 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28374 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18600 | RP-43d464fda7218e6e | deep | arXiv:2606.18600v1 | SRC-ARXIV@arXiv:2606.18600v1 | https://arxiv.org/html/2606.18600v1 — § exact-v1 anchor: 4 Model Placement for Heterogeneous GPUs | https://arxiv.org/html/2606.18600v1 — § exact-v1 evaluation anchor: 7 Evaluation | https://arxiv.org/html/2606.18600v1 — § exact-v1 limitation/counterevidence anchor: 8.1 Limitation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18600 | complete |
| SF-2026-ARXIV-2606-18619 | RP-b1641e5e887033df | deep | arXiv:2606.18619v1 | SRC-ARXIV@arXiv:2606.18619v1 | https://arxiv.org/html/2606.18619v1 — § exact-v1 anchor: security-specification-first paradigm | https://arxiv.org/html/2606.18619v1 — § exact-v1 evaluation anchor: real-world subjects | https://arxiv.org/html/2606.18619v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18619 | complete |
| SF-2026-ARXIV-2606-18650 | RP-06daad534bd2ce5d | deep | arXiv:2606.18650v1 | SRC-ARXIV@arXiv:2606.18650v1 | https://arxiv.org/html/2606.18650v1 — § exact-v1 anchor: penalized single-level objective | https://arxiv.org/html/2606.18650v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18650v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18650 | complete |
| SF-2026-ARXIV-2606-18668 | RP-80c4ada12115ffae | deep | arXiv:2606.18668v1 | SRC-ARXIV@arXiv:2606.18668v1 | https://arxiv.org/html/2606.18668v1 — § exact-v1 anchor: Explanatory Abstention | https://arxiv.org/html/2606.18668v1 — § exact-v1 evaluation anchor: production e-commerce assistant | https://arxiv.org/html/2606.18668v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18668 | complete |
| SF-2026-ARXIV-2606-18673 | RP-11622651a47d8c44 | deep | arXiv:2606.18673v1 | SRC-ARXIV@arXiv:2606.18673v1 | https://arxiv.org/html/2606.18673v1 — § exact-v1 anchor: attention drift | https://arxiv.org/html/2606.18673v1 — § exact-v1 evaluation anchor: 1,200 applications | https://arxiv.org/html/2606.18673v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18673 | complete |
| SF-2026-ARXIV-2606-18697 | RP-97d4b5a5b08b22ff | deep | arXiv:2606.18697v1 | SRC-ARXIV@arXiv:2606.18697v1 | https://arxiv.org/html/2606.18697v1 — § exact-v1 anchor: two-stage data poisoning framework | https://arxiv.org/html/2606.18697v1 — § exact-v1 evaluation anchor: continuous-control tasks | https://arxiv.org/html/2606.18697v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18697 | complete |
| SF-2026-ARXIV-2606-18741 | RP-8f89bc901404df5e | deep | arXiv:2606.18741v1 | SRC-ARXIV@arXiv:2606.18741v1 | https://arxiv.org/html/2606.18741v1 — § exact-v1 anchor: two-dimensional KV cache migration | https://arxiv.org/html/2606.18741v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18741v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18741 | complete |
| SF-2026-ARXIV-2606-18746 | RP-6534f060fca815cb | deep | arXiv:2606.18746v1 | SRC-ARXIV@arXiv:2606.18746v1 | https://arxiv.org/html/2606.18746v1 — § exact-v1 anchor: separation theorem | https://arxiv.org/html/2606.18746v1 — § exact-v1 evaluation anchor: transition-model reconstruction | https://arxiv.org/html/2606.18746v1 — § exact-v1 limitation/counterevidence anchor: assumptions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18746 | complete |
| SF-2026-ARXIV-2606-18810 | RP-67359ff010705fe8 | deep | arXiv:2606.18810v1 | SRC-ARXIV@arXiv:2606.18810v1 | https://arxiv.org/html/2606.18810v1 — § exact-v1 anchor: Self-Conditioned GRPO | https://arxiv.org/html/2606.18810v1 — § exact-v1 evaluation anchor: five benchmarks | https://arxiv.org/html/2606.18810v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18810 | complete |
| SF-2026-ARXIV-2606-18829 | RP-142faf4468530c97 | deep | arXiv:2606.18829v1 | SRC-ARXIV@arXiv:2606.18829v1 | https://arxiv.org/html/2606.18829v1 — § exact-v1 anchor: multi-principal shared-memory agents | https://arxiv.org/html/2606.18829v1 — § exact-v1 evaluation anchor: diverse baselines and backbone models | https://arxiv.org/html/2606.18829v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18829 | complete |
| SF-2026-ARXIV-2606-18831 | RP-4e5c1ee492eb62aa | deep | arXiv:2606.18831v1 | SRC-ARXIV@arXiv:2606.18831v1 | https://arxiv.org/html/2606.18831v1 — § exact-v1 anchor: 3.1 Long-Context Training Data | https://arxiv.org/html/2606.18831v1 — § exact-v1 evaluation anchor: 4 Experiments | https://arxiv.org/html/2606.18831v1 — § exact-v1 limitation/counterevidence anchor: 5 Analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18831 | complete |
| SF-2026-ARXIV-2606-18847 | RP-592b0b44c1431829 | deep | arXiv:2606.18847v1 | SRC-ARXIV@arXiv:2606.18847v1 | https://arxiv.org/html/2606.18847v1 — § exact-v1 anchor: WorldLines | https://arxiv.org/html/2606.18847v1 — § exact-v1 evaluation anchor: ObsMem | https://arxiv.org/html/2606.18847v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18847 | complete |
| SF-2026-ARXIV-2606-18874 | RP-9fd4dd2d000acb58 | deep | arXiv:2606.18874v1 | SRC-ARXIV@arXiv:2606.18874v1 | https://arxiv.org/html/2606.18874v1 — § exact-v1 anchor: persistent research artifacts | https://arxiv.org/html/2606.18874v1 — § exact-v1 evaluation anchor: three case studies | https://arxiv.org/html/2606.18874v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18874 | complete |
| SF-2026-ARXIV-2606-18958 | RP-0502c38e36e7d46f | deep | arXiv:2606.18958v1 | SRC-ARXIV@arXiv:2606.18958v1 | https://arxiv.org/html/2606.18958v1 — § exact-v1 anchor: full-stack live simulation | https://arxiv.org/html/2606.18958v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.18958v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18958 | complete |
| SF-2026-ARXIV-2606-18967 | RP-85a776d1f8c87caf | deep | arXiv:2606.18967v1 | SRC-ARXIV@arXiv:2606.18967v1 | https://arxiv.org/html/2606.18967v1 — § exact-v1 anchor: system-aware self-speculative decoding | https://arxiv.org/html/2606.18967v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18967v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18967 | complete |
| SF-2026-ARXIV-2606-18996 | RP-9721999a51e217df | deep | arXiv:2606.18996v1 | SRC-ARXIV@arXiv:2606.18996v1 | https://arxiv.org/html/2606.18996v1 — § exact-v1 anchor: Task-completion and Resistance | https://arxiv.org/html/2606.18996v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.18996v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18996 | complete |
| SF-2026-ARXIV-2606-19004 | RP-4134963e7c617cf0 | deep | arXiv:2606.19004v1 | SRC-ARXIV@arXiv:2606.19004v1 | https://arxiv.org/html/2606.19004v1 — § exact-v1 anchor: Seed Exploration and Spot GPUs | https://arxiv.org/html/2606.19004v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19004v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19004 | complete |
| SF-2026-ARXIV-2606-19025 | RP-69c349a48eb20aa0 | deep | arXiv:2606.19025v1 | SRC-ARXIV@arXiv:2606.19025v1 | https://arxiv.org/html/2606.19025v1 — § exact-v1 anchor: partitioning expert layers across workers | https://arxiv.org/html/2606.19025v1 — § exact-v1 evaluation anchor: FoMoE Scalability & Resource Consumption | https://arxiv.org/html/2606.19025v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19025 | complete |
| SF-2026-ARXIV-2606-19057 | RP-32e81e7396980e1c | deep | arXiv:2606.19057v1 | SRC-ARXIV@arXiv:2606.19057v1 | https://arxiv.org/html/2606.19057v1 — § exact-v1 anchor: Positive–Unlabeled Learning | https://arxiv.org/html/2606.19057v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19057v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19057 | complete |
| SF-2026-ARXIV-2606-19111 | RP-d57ed8541041e79e | deep | arXiv:2606.19111v1 | SRC-ARXIV@arXiv:2606.19111v1 | https://arxiv.org/html/2606.19111v1 — § exact-v1 anchor: Recovery-Advantage Boundary | https://arxiv.org/html/2606.19111v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19111v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19111 | complete |
| SF-2026-ARXIV-2606-19191 | RP-3577ad1227f9b380 | deep | arXiv:2606.19191v1 | SRC-ARXIV@arXiv:2606.19191v1 | https://arxiv.org/html/2606.19191v1 — § exact-v1 anchor: 3 Threat Model | https://arxiv.org/html/2606.19191v1 — § exact-v1 evaluation anchor: 5 Evaluation | https://arxiv.org/html/2606.19191v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19191 | complete |
| SF-2026-ARXIV-2606-19242 | RP-274d1357452733c6 | deep | arXiv:2606.19242v1 | SRC-ARXIV@arXiv:2606.19242v1 | https://arxiv.org/html/2606.19242v1 — § exact-v1 anchor: Runtime Compliance Verification | https://arxiv.org/html/2606.19242v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19242v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19242 | complete |
| SF-2026-ARXIV-2606-19262 | RP-9b28f51a00defa29 | deep | arXiv:2606.19262v1 | SRC-ARXIV@arXiv:2606.19262v1 | https://arxiv.org/html/2606.19262v1 — § exact-v1 anchor: Zero-Overhead Telemetry | https://arxiv.org/html/2606.19262v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19262v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19262 | complete |
| SF-2026-ARXIV-2606-19271 | RP-c7db478f4bc8677e | deep | arXiv:2606.19271v1 | SRC-ARXIV@arXiv:2606.19271v1 | https://arxiv.org/html/2606.19271v1 — § exact-v1 anchor: Streaming Video Generation | https://arxiv.org/html/2606.19271v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19271v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19271 | complete |
| SF-2026-ARXIV-2606-19409 | RP-7d7150c18958b701 | deep | arXiv:2606.19409v1 | SRC-ARXIV@arXiv:2606.19409v1 | https://arxiv.org/html/2606.19409v1 — § exact-v1 anchor: Session-Centered Runtime State | https://arxiv.org/html/2606.19409v1 — § exact-v1 evaluation anchor: audited milestones | https://arxiv.org/html/2606.19409v1 — § exact-v1 limitation/counterevidence anchor: claims are limited | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19409 | complete |
| SF-2026-ARXIV-2606-19464 | RP-9c9808c620abad7c | deep | arXiv:2606.19464v1 | SRC-ARXIV@arXiv:2606.19464v1 | https://arxiv.org/html/2606.19464v1 — § exact-v1 anchor: obligations, dispensations | https://arxiv.org/html/2606.19464v1 — § exact-v1 evaluation anchor: examples | https://arxiv.org/html/2606.19464v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19464 | complete |
| SF-2026-ARXIV-2606-19535 | RP-c928538e16521982 | deep | arXiv:2606.19535v1 | SRC-ARXIV@arXiv:2606.19535v1 | https://arxiv.org/html/2606.19535v1 — § exact-v1 anchor: platform-triggered backdoor | https://arxiv.org/html/2606.19535v1 — § exact-v1 evaluation anchor: broad range of deployment targets | https://arxiv.org/html/2606.19535v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19535 | complete |
| SF-2026-ARXIV-2606-19544 | RP-c5005845d92e5630 | deep | arXiv:2606.19544v1 | SRC-ARXIV@arXiv:2606.19544v1 | https://arxiv.org/html/2606.19544v1 — § exact-v1 anchor: Minimum Viable Validation Protocol | https://arxiv.org/html/2606.19544v1 — § exact-v1 evaluation anchor: 118 runs | https://arxiv.org/html/2606.19544v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19544 | complete |
| SF-2026-ARXIV-2606-19559 | RP-2946b51270383016 | deep | arXiv:2606.19559v1 | SRC-ARXIV@arXiv:2606.19559v1 | https://arxiv.org/html/2606.19559v1 — § exact-v1 anchor: action confidence from request uncertainty | https://arxiv.org/html/2606.19559v1 — § exact-v1 evaluation anchor: five LLM backbones | https://arxiv.org/html/2606.19559v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19559 | complete |
| SF-2026-ARXIV-2606-19595 | RP-0d67b5370a61594a | deep | arXiv:2606.19595v1 | SRC-ARXIV@arXiv:2606.19595v1 | https://arxiv.org/html/2606.19595v1 — § exact-v1 anchor: Post-Interruption Recovery | https://arxiv.org/html/2606.19595v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19595v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19595 | complete |
| SF-2026-ARXIV-2606-19613 | RP-25646df540d73ac2 | deep | arXiv:2606.19613v1 | SRC-ARXIV@arXiv:2606.19613v1 | https://arxiv.org/html/2606.19613v1 — § exact-v1 anchor: 100 Interaction Turns | https://arxiv.org/html/2606.19613v1 — § exact-v1 evaluation anchor: 20 scenarios | https://arxiv.org/html/2606.19613v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19613 | complete |
| SF-2026-ARXIV-2606-19667 | RP-5baa9c06caf84ed7 | deep | arXiv:2606.19667v1 | SRC-ARXIV@arXiv:2606.19667v1 | https://arxiv.org/html/2606.19667v1 — § exact-v1 anchor: prefix tree over recently served evidence sequences | https://arxiv.org/html/2606.19667v1 — § exact-v1 evaluation anchor: three vLLM configurations | https://arxiv.org/html/2606.19667v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19667 | complete |
| SF-2026-ARXIV-2606-20736 | RP-ce65b478413b89ff | deep | arXiv:2606.20736v1 | SRC-ARXIV@arXiv:2606.20736v1 | https://arxiv.org/html/2606.20736v1 — § exact-v1 anchor: randomly regenerates the answer-bearing local detail | https://arxiv.org/html/2606.20736v1 — § exact-v1 evaluation anchor: eight frontier vision-language models | https://arxiv.org/html/2606.20736v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-20736 | complete |
| SF-2026-ARXIV-2606-20746 | RP-90be3e9c423b4e36 | deep | arXiv:2606.20746v1 | SRC-ARXIV@arXiv:2606.20746v1 | https://arxiv.org/html/2606.20746v1 — § exact-v1 anchor: detector of record | https://arxiv.org/html/2606.20746v1 — § exact-v1 evaluation anchor: broader clean-path actions | https://arxiv.org/html/2606.20746v1 — § exact-v1 limitation/counterevidence anchor: boundary result, not a deployable detector | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-20746 | complete |
| SF-2026-ARXIV-2606-21089 | RP-eaade2dee238e5a8 | deep | arXiv:2606.21089v1 | SRC-ARXIV@arXiv:2606.21089v1 | https://arxiv.org/html/2606.21089v1 — § exact-v1 anchor: scientific amnesia | https://arxiv.org/html/2606.21089v1 — § exact-v1 evaluation anchor: single-seed 5-condition | https://arxiv.org/html/2606.21089v1 — § exact-v1 limitation/counterevidence anchor: diagnostic, not a claim | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21089 | complete |
| SF-2026-ARXIV-2606-21090 | RP-b1532b9010698ab9 | deep | arXiv:2606.21090v1 | SRC-ARXIV@arXiv:2606.21090v1 | https://arxiv.org/html/2606.21090v1 — § exact-v1 anchor: rise-then-collapse pattern | https://arxiv.org/html/2606.21090v1 — § exact-v1 evaluation anchor: 10 sequential 20-step campaigns | https://arxiv.org/html/2606.21090v1 — § exact-v1 limitation/counterevidence anchor: mixed evidence | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-21090 | complete |
| SF-2026-ARXIV-2606-28374 | RP-599ee9146b59e214 | deep | arXiv:2606.28374v1 | SRC-ARXIV@arXiv:2606.28374v1 | https://arxiv.org/html/2606.28374v1 — § exact-v1 anchor: strict keep-better gate | https://arxiv.org/html/2606.28374v1 — § exact-v1 evaluation anchor: four diverse benchmarks | https://arxiv.org/html/2606.28374v1 — § exact-v1 limitation/counterevidence anchor: no artifact universally wins | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-28374 | complete |

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18600 | offline throughput | Llama-3.1-70B; Qwen3-32B | AWS L4, A10G and L40S GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | offline throughput, online TTFT/TPOT and cost efficiency under spot interruption |
| SF-2026-ARXIV-2606-18619 | real-subject vulnerability findings plus specification-falsification outcomes | Claude Sonnet 4.6 and DeepSeek V4 Pro; Claude Mythos is comparison-only | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | real-subject vulnerability findings plus specification-falsification outcomes |
| SF-2026-ARXIV-2606-18650 | downstream task quality and selection efficiency against influence/excess-loss baselines | TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | downstream task quality and selection efficiency against influence/excess-loss baselines |
| SF-2026-ARXIV-2606-18668 | production pass rate under structured abstention labels and rationales | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | production pass rate under structured abstention labels and rationales |
| SF-2026-ARXIV-2606-18673 | prompt leakage resistance | Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | prompt leakage resistance, usability and optimization overhead over 1,200 applications |
| SF-2026-ARXIV-2606-18697 | planning return | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | planning return, poison detectability and defense response across three pipeline stages |
| SF-2026-ARXIV-2606-18741 | reconfiguration downtime | Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B | NVIDIA H100 and RTX 5090 platforms | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reconfiguration downtime, TTFT, TPOT and output throughput |
| SF-2026-ARXIV-2606-18746 | theorem premises and approximation error for domain disambiguation and local dynamics reconstruction | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | theorem premises and approximation error for domain disambiguation and local dynamics reconstruction |
| SF-2026-ARXIV-2606-18810 | task accuracy and OOD performance against GRPO | Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task accuracy and OOD performance against GRPO, DAPO and OPD |
| SF-2026-ARXIV-2606-18829 | legitimate utility | GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | legitimate utility, contextual access-control leakage and post-deletion active forgetting |
| SF-2026-ARXIV-2606-18831 | seven long-context benchmarks plus GAIA and BrowseComp transfer | Qwen3-4B, Qwen3-8B and Qwen3-30B-A3B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | seven long-context benchmarks plus GAIA and BrowseComp transfer |
| SF-2026-ARXIV-2606-18847 | Memory QA and Embodied Task Planning over evidence-linked household traces | google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Memory QA and Embodied Task Planning over evidence-linked household traces |
| SF-2026-ARXIV-2606-18874 | claim-to-artifact traceability | gpt-4o-mini answer generator and all-MiniLM-L6-v2 embedder in the matched LoCoMo validation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | claim-to-artifact traceability, ablation and bounded repair across three research domains |
| SF-2026-ARXIV-2606-18958 | simulation scale | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | simulation scale, fidelity and runtime overhead |
| SF-2026-ARXIV-2606-18967 | rollout throughput | Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters | single NVIDIA A100-80GiB SXM in the decode-cost study | FP16 target inference; W4/W8 weight-quantized self-drafters | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | rollout throughput, acceptance and downstream RL quality |
| SF-2026-ARXIV-2606-18996 | paired task-completion and active privacy-extraction outcomes | GPT-4o-mini, GPT-5-mini, GPT-5.4-mini, GPT-5, Gemini-2.5-Flash-Lite, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude Haiku 4.5, Claude Sonnet 4.5, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B, Qwen3-VL-32B, Phi-4-multimodal, InternVL3.5-2B, InternVL3.5-4B, InternVL3.5-8B, InternVL3.5-14B, InternVL3.5-38B, Devstral-Small-2512, Llama3.2-11B-Vision and GLM-4.6V-Flash | NVIDIA A6000 GPUs for open-source models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paired task-completion and active privacy-extraction outcomes |
| SF-2026-ARXIV-2606-19004 | training reward/quality | Qwen-Image | 4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | training reward/quality, GPU utilization and spot cost |
| SF-2026-ARXIV-2606-19025 | communication volume | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | communication volume, local-training throughput and routing stability; 100B results are modeled projections |
| SF-2026-ARXIV-2606-19057 | hidden-positive prevalence | Mistral-7B-Instruct, Qwen2.5-7B-Instruct, Llemma-7B-MuInstruct and GPT-5.4-mini judges | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | hidden-positive prevalence, calibration and audit error |
| SF-2026-ARXIV-2606-19111 | team outcome | gpt-oss-120b, gemma-4-31B-it and llama-4-scout | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | team outcome, behavioral leadership signatures and recovery advantage |
| SF-2026-ARXIV-2606-19191 | attack success | GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success, warning/detection and benign utility across four attack goals |
| SF-2026-ARXIV-2606-19242 | policy-violation detection and runtime enforcement outcomes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | policy-violation detection and runtime enforcement outcomes |
| SF-2026-ARXIV-2606-19262 | hidden-training detection | Not Disclosed | nine NVIDIA GPU models across four architecture generations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | hidden-training detection, false positives and telemetry overhead |
| SF-2026-ARXIV-2606-19271 | worst-case per-chunk latency | Not Disclosed | GPU clusters with up to 64 NVIDIA B300 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | worst-case per-chunk latency, end-to-end quality and GPU operating cost |
| SF-2026-ARXIV-2606-19409 | audited runtime invariants and controlled replay properties; no broad quality benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | audited runtime invariants and controlled replay properties; no broad quality benchmark |
| SF-2026-ARXIV-2606-19464 | expressibility and runtime policy-evaluation examples | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | expressibility and runtime policy-evaluation examples |
| SF-2026-ARXIV-2606-19535 | target-platform activation | Qwen3-4B and Qwen3-8B with two LoRA adapters | NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710 | Not Disclosed | Not Disclosed | Not Disclosed | 1 | Not Disclosed | Not Disclosed | target-platform activation, aggregate utility and vulnerable-code generation |
| SF-2026-ARXIV-2606-19544 | agreement | Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias |
| SF-2026-ARXIV-2606-19559 | clarification F1 and fault detection across clarification and standard benchmarks | GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | clarification F1 and fault detection across clarification and standard benchmarks |
| SF-2026-ARXIV-2606-19595 | post-interruption task completion and structured recovery error | GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | post-interruption task completion and structured recovery error |
| SF-2026-ARXIV-2606-19613 | consecutive passed turns | Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios |
| SF-2026-ARXIV-2606-19667 | median TTFT | Qwen2.5-1.5B and Qwen2.5-7B | RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB | Not Disclosed | max_model_len 2048 or 4096 by configuration | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | median TTFT, prefix reuse and QA answer quality |
| SF-2026-ARXIV-2606-20736 | accuracy gap between original and regenerated V*Bench items with controlled search difficulty | Qwen3.6-Plus, GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, Seed-2.0-Lite, Kimi K2.6, MiMo v2.5 and Llama 4 Maverick; LLaVA-1.5-13B for difficulty calibration | Not Disclosed | Not Disclosed | Not Disclosed | max_tokens 8192 | Not Disclosed | Not Disclosed | Not Disclosed | accuracy gap between original and regenerated V*Bench items with controlled search difficulty |
| SF-2026-ARXIV-2606-20746 | clustered-bootstrap gap and persistence/peak delta AUC on executed-edge trajectories | frozen char-ngram SVM plus embedding-contrastive detector; held-out cloaking target | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | clustered-bootstrap gap and persistence/peak delta AUC on executed-edge trajectories |
| SF-2026-ARXIV-2606-21089 | campaign-level peak pass@1 and intervention deltas across 30 HumanEval subdomains | Qwen2.5-7B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | campaign-level peak pass@1 and intervention deltas across 30 HumanEval subdomains |
| SF-2026-ARXIV-2606-21090 | pass@1 trajectory | Qwen2.5-3B, Qwen2.5-7B and a Gemma-3-4B pilot | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | pass@1 trajectory, peak-to-end collapse and multi-seed intervention comparison |
| SF-2026-ARXIV-2606-28374 | benchmark score | Qwen2.5-7B-Instruct for ALFWorld and Qwen3-30B-A3B-Instruct for GAIA, tau-bench and WebShop | 4 NVIDIA A100 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | benchmark score, McNemar test and regression gate across four agent benchmarks |

**Source Reviews**

<!-- review:SF-2026-ARXIV-2606-18600:start -->
### 2606.18600 — ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters

**问题与旧路径。** As large language model (LLM) services become widely adopted, the cost of GPU resources for serving these models in cloud environments has emerged as a critical concern. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Llama-3.1-70B 与 Qwen3-32B 在 AWS L4/A10G/L40S 集群上报告吞吐与 offline/online 成本效率改善。 Method=`https://arxiv.org/html/2606.18600v1 — § exact-v1 anchor: 4 Model Placement for Heterogeneous GPUs`；Evaluation=`https://arxiv.org/html/2606.18600v1 — § exact-v1 evaluation anchor: 7 Evaluation`。Benchmark contract：model=`Llama-3.1-70B; Qwen3-32B`；hardware=`AWS L4, A10G and L40S GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`offline throughput, online TTFT/TPOT and cost efficiency under spot interruption`。

**Trade-off、failure、共存与演进。** 六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18600v1 — § exact-v1 limitation/counterevidence anchor: 8.1 Limitation`。

<!-- claim:SF-2026-ARXIV-2606-18600:start -->
Claim boundary：仅 `arXiv:2606.18600v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18600:end -->
<!-- review:SF-2026-ARXIV-2606-18600:end -->

<!-- review:SF-2026-ARXIV-2606-18619:start -->
### 2606.18619 — Code-Augur: Agentic Vulnerability Detection via Specification Inference

**问题与旧路径。** The advent of agentic vulnerability detection is already becoming a watershed moment for software security. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在真实开源项目上与 agent baselines 比较，并报告发现 22 个新漏洞；使用 Sonnet、DeepSeek，并与 Claude Mythos 作受限比较。 Method=`https://arxiv.org/html/2606.18619v1 — § exact-v1 anchor: security-specification-first paradigm`；Evaluation=`https://arxiv.org/html/2606.18619v1 — § exact-v1 evaluation anchor: real-world subjects`。Benchmark contract：model=`Claude Sonnet 4.6 and DeepSeek V4 Pro; Claude Mythos is comparison-only`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`real-subject vulnerability findings plus specification-falsification outcomes`。

**Trade-off、failure、共存与演进。** fuzzer 未触发不等于 invariant 成立，assertion 也可能错；覆盖限于作者 subjects 与可观测运行输入。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18619v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18619:start -->
Claim boundary：仅 `arXiv:2606.18619v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18619:end -->
<!-- review:SF-2026-ARXIV-2606-18619:end -->

<!-- review:SF-2026-ARXIV-2606-18650:start -->
### 2606.18650 — BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training

**问题与旧路径。** As Large Language Model (LLM) datasets scale to trillions of tokens, data selection has emerged as a critical frontier to filter out uninformative noise and construct adaptive learning trajectories. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。 唯一知识 owner 为 `TRAIN-DATA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 LLM pretraining matrix 中比较 BLADE 与 influence、excess-loss baselines，并给出 first-order convergence。 Method=`https://arxiv.org/html/2606.18650v1 — § exact-v1 anchor: penalized single-level objective`；Evaluation=`https://arxiv.org/html/2606.18650v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`downstream task quality and selection efficiency against influence/excess-loss baselines`。

**Trade-off、failure、共存与演进。** proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18650v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18650:start -->
Claim boundary：仅 `arXiv:2606.18650v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18650:end -->
<!-- review:SF-2026-ARXIV-2606-18650:end -->

<!-- review:SF-2026-ARXIV-2606-18668:start -->
### 2606.18668 — EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

**问题与旧路径。** In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 生产电商 BI assistant 的 overall response pass rate从 68.5% 提升到 78.9%。 Method=`https://arxiv.org/html/2606.18668v1 — § exact-v1 anchor: Explanatory Abstention`；Evaluation=`https://arxiv.org/html/2606.18668v1 — § exact-v1 evaluation anchor: production e-commerce assistant`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`production pass rate under structured abstention labels and rationales`。

**Trade-off、failure、共存与演进。** judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18668v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18668:start -->
Claim boundary：仅 `arXiv:2606.18668v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18668:end -->
<!-- review:SF-2026-ARXIV-2606-18668:end -->

<!-- review:SF-2026-ARXIV-2606-18673:start -->
### 2606.18673 — Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications

**问题与旧路径。** Large language model (LLM)-based applications rely on system prompts to encode core logic and developer-defined constraints, making these prompts important intellectual property. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 测量六个平台 1,200 个应用，报告超过 80% 泄漏；AREA 的 usability 与优化开销相对防线比较。 Method=`https://arxiv.org/html/2606.18673v1 — § exact-v1 anchor: attention drift`；Evaluation=`https://arxiv.org/html/2606.18673v1 — § exact-v1 evaluation anchor: 1,200 applications`。Benchmark contract：model=`Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`prompt leakage resistance, usability and optimization overhead over 1,200 applications`。

**Trade-off、failure、共存与演进。** attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18673v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18673:start -->
Claim boundary：仅 `arXiv:2606.18673v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18673:end -->
<!-- review:SF-2026-ARXIV-2606-18673:end -->

<!-- review:SF-2026-ARXIV-2606-18697:start -->
### 2606.18697 — Stealthy World Model Manipulation via Data Poisoning

**问题与旧路径。** Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 连续控制任务上评估 planning return、poison detectability，并测试 residual/CUSUM/TRIM 防线。 Method=`https://arxiv.org/html/2606.18697v1 — § exact-v1 anchor: two-stage data poisoning framework`；Evaluation=`https://arxiv.org/html/2606.18697v1 — § exact-v1 evaluation anchor: continuous-control tasks`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`planning return, poison detectability and defense response across three pipeline stages`。

**Trade-off、failure、共存与演进。** 只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18697v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18697:start -->
Claim boundary：仅 `arXiv:2606.18697v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18697:end -->
<!-- review:SF-2026-ARXIV-2606-18697:end -->

<!-- review:SF-2026-ARXIV-2606-18741:start -->
### 2606.18741 — ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving

**问题与旧路径。** Current large language model (LLM) inference systems universally deploy ultra-large-scale models using a combination of Tensor Parallelism (TP) and Pipeline Parallelism (PP). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 7B–70B models 的多数 topology switch 为 1–7 秒，并报告动态 workload 的 TTFT、TPOT 与 output throughput。 Method=`https://arxiv.org/html/2606.18741v1 — § exact-v1 anchor: two-dimensional KV cache migration`；Evaluation=`https://arxiv.org/html/2606.18741v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B`；hardware=`NVIDIA H100 and RTX 5090 platforms`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`reconfiguration downtime, TTFT, TPOT and output throughput`。

**Trade-off、failure、共存与演进。** KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18741v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18741:start -->
Claim boundary：仅 `arXiv:2606.18741v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18741:end -->
<!-- review:SF-2026-ARXIV-2606-18741:end -->

<!-- review:SF-2026-ARXIV-2606-18746:start -->
### 2606.18746 — What Must Generalist Agents Remember?

**问题与旧路径。** This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。 唯一知识 owner 为 `AGENT-MEMORY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 给出 separation theorem 与 transition reconstruction 条件，而非经验 leaderboard。 Method=`https://arxiv.org/html/2606.18746v1 — § exact-v1 anchor: separation theorem`；Evaluation=`https://arxiv.org/html/2606.18746v1 — § exact-v1 evaluation anchor: transition-model reconstruction`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`theorem premises and approximation error for domain disambiguation and local dynamics reconstruction`。

**Trade-off、failure、共存与演进。** 定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18746v1 — § exact-v1 limitation/counterevidence anchor: assumptions`。

<!-- claim:SF-2026-ARXIV-2606-18746:start -->
Claim boundary：仅 `arXiv:2606.18746v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18746:end -->
<!-- review:SF-2026-ARXIV-2606-18746:end -->

<!-- review:SF-2026-ARXIV-2606-18810:start -->
### 2606.18810 — Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

**问题与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 math、code、agentic benchmarks 上相对 GRPO 与 DAPO 报告平均改善和 OOD 结果。 Method=`https://arxiv.org/html/2606.18810v1 — § exact-v1 anchor: Self-Conditioned GRPO`；Evaluation=`https://arxiv.org/html/2606.18810v1 — § exact-v1 evaluation anchor: five benchmarks`。Benchmark contract：model=`Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`task accuracy and OOD performance against GRPO, DAPO and OPD`。

**Trade-off、failure、共存与演进。** self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18810v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18810:start -->
Claim boundary：仅 `arXiv:2606.18810v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18810:end -->
<!-- review:SF-2026-ARXIV-2606-18810:end -->

<!-- review:SF-2026-ARXIV-2606-18829:start -->
### 2606.18829 — GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

**问题与旧路径。** Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** GateMem 跨医疗、办公、教育、家庭；多种 memory baselines/backbones 均未同时获得强 utility、ACL 与 forgetting。 Method=`https://arxiv.org/html/2606.18829v1 — § exact-v1 anchor: multi-principal shared-memory agents`；Evaluation=`https://arxiv.org/html/2606.18829v1 — § exact-v1 evaluation anchor: diverse baselines and backbone models`。Benchmark contract：model=`GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`legitimate utility, contextual access-control leakage and post-deletion active forgetting`。

**Trade-off、failure、共存与演进。** structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18829v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18829:start -->
Claim boundary：仅 `arXiv:2606.18829v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18829:end -->
<!-- review:SF-2026-ARXIV-2606-18829:end -->

<!-- review:SF-2026-ARXIV-2606-18831:start -->
### 2606.18831 — Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

**问题与旧路径。** Long-context reasoning is an essential capability for large language models, particularly when they are deployed as autonomous agents that must reason over lengthy trajectories. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** long-context RL 的 data owner 应同时覆盖 retrieval、multi-evidence synthesis 与 reasoning，避免只通过 reward shaping 修补 evidence localization。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B/8B/30B-A3B、约 14K 样本、七个长上下文 benchmark，并在 GAIA/BrowseComp 测 transfer。 Method=`https://arxiv.org/html/2606.18831v1 — § exact-v1 anchor: 3.1 Long-Context Training Data`；Evaluation=`https://arxiv.org/html/2606.18831v1 — § exact-v1 evaluation anchor: 4 Experiments`。Benchmark contract：model=`Qwen3-4B, Qwen3-8B and Qwen3-30B-A3B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`seven long-context benchmarks plus GAIA and BrowseComp transfer`。

**Trade-off、failure、共存与演进。** 作者 mixture 与 Qwen family 不能证明通用配方；outcome reward 仍可能奖励无 grounding shortcut。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18831v1 — § exact-v1 limitation/counterevidence anchor: 5 Analysis`。

<!-- claim:SF-2026-ARXIV-2606-18831:start -->
Claim boundary：仅 `arXiv:2606.18831v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18831:end -->
<!-- review:SF-2026-ARXIV-2606-18831:end -->

<!-- review:SF-2026-ARXIV-2606-18847:start -->
### 2606.18847 — WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

**问题与旧路径。** To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** WorldLines 同时评 Memory QA 与 Embodied Task Planning；ObsMem 对 partial observability、overwritten state 进行比较。 Method=`https://arxiv.org/html/2606.18847v1 — § exact-v1 anchor: WorldLines`；Evaluation=`https://arxiv.org/html/2606.18847v1 — § exact-v1 evaluation anchor: ObsMem`。Benchmark contract：model=`google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`Memory QA and Embodied Task Planning over evidence-linked household traces`。

**Trade-off、failure、共存与演进。** benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18847v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18847:start -->
Claim boundary：仅 `arXiv:2606.18847v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18847:end -->
<!-- review:SF-2026-ARXIV-2606-18847:end -->

<!-- review:SF-2026-ARXIV-2606-18874:start -->
### 2606.18874 — Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness

**问题与旧路径。** AI systems can increasingly automate scientific workflows, but the reasoning that links prior evidence, generated ideas, experiments and final claims often remains implicit inside model inference. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** AI scientist 应把 literature evidence、idea、implementation、ablation 与 repair trace 外化为 persistent contracts，并检查 runnable artifact 是否仍支持原 claim。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在 training-free memory、traffic forecasting 与 PINN 三类研究流程展示可追踪 problem→mechanism→validation 轨迹。 Method=`https://arxiv.org/html/2606.18874v1 — § exact-v1 anchor: persistent research artifacts`；Evaluation=`https://arxiv.org/html/2606.18874v1 — § exact-v1 evaluation anchor: three case studies`。Benchmark contract：model=`gpt-4o-mini answer generator and all-MiniLM-L6-v2 embedder in the matched LoCoMo validation`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`claim-to-artifact traceability, ablation and bounded repair across three research domains`。

**Trade-off、failure、共存与演进。** 三个案例不证明自动科学发现质量；trace 完整也不能替代独立复现或可信实验。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18874v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18874:start -->
Claim boundary：仅 `arXiv:2606.18874v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18874:end -->
<!-- review:SF-2026-ARXIV-2606-18874:end -->

<!-- review:SF-2026-ARXIV-2606-18958:start -->
### 2606.18958 — LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation

**问题与旧路径。** Cluster-scale full-stack simulation is essential for evaluating distributed software stacks and emerging hardware components before deployment. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** cluster live simulation 要让真实 software stack 与模拟 node/network/device time 协同推进，并显式区分 simulated resource state 与 production effect。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在 cluster-scale full-stack workloads 上比较 simulation fidelity、scale 与执行开销。 Method=`https://arxiv.org/html/2606.18958v1 — § exact-v1 anchor: full-stack live simulation`；Evaluation=`https://arxiv.org/html/2606.18958v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`simulation scale, fidelity and runtime overhead`。

**Trade-off、failure、共存与演进。** 模拟器遗漏的 kernel、network tail 和 control-plane race 会制造假确定性；不能用 live simulation 代替 canary。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18958v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18958:start -->
Claim boundary：仅 `arXiv:2606.18958v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18958:end -->
<!-- review:SF-2026-ARXIV-2606-18958:end -->

<!-- review:SF-2026-ARXIV-2606-18967:start -->
### 2606.18967 — EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts

**问题与旧路径。** Reinforcement learning (RL) has become a representative post-training paradigm for LLMs, enabling strong reasoning and agentic capabilities. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。 唯一知识 owner 为 `INFER-SPECULATIVE-DECODING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在 RL rollout workloads 上报告 self-speculative speedup、acceptance 与 training quality。 Method=`https://arxiv.org/html/2606.18967v1 — § exact-v1 anchor: system-aware self-speculative decoding`；Evaluation=`https://arxiv.org/html/2606.18967v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters`；hardware=`single NVIDIA A100-80GiB SXM in the decode-cost study`；precision=`FP16 target inference; W4/W8 weight-quantized self-drafters`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`rollout throughput, acceptance and downstream RL quality`。

**Trade-off、failure、共存与演进。** acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18967v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18967:start -->
Claim boundary：仅 `arXiv:2606.18967v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18967:end -->
<!-- review:SF-2026-ARXIV-2606-18967:end -->

<!-- review:SF-2026-ARXIV-2606-18996:start -->
### 2606.18996 — TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction

**问题与旧路径。** Agents are increasingly deployed in document-intensive workflows where sensitive private information is not an edge case but a routine input, e.g., an agent booking a flight needs passport numbers. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** privacy-capable agent benchmark 必须联合评分 task completion 与 active extraction resistance，并把攻击者交互轨迹、secret canary 与 policy effect 分开。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** TRAP 在作者 agent/model matrix 中同时测任务完成与主动隐私提取。 Method=`https://arxiv.org/html/2606.18996v1 — § exact-v1 anchor: Task-completion and Resistance`；Evaluation=`https://arxiv.org/html/2606.18996v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`GPT-4o-mini, GPT-5-mini, GPT-5.4-mini, GPT-5, Gemini-2.5-Flash-Lite, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude Haiku 4.5, Claude Sonnet 4.5, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B, Qwen3-VL-32B, Phi-4-multimodal, InternVL3.5-2B, InternVL3.5-4B, InternVL3.5-8B, InternVL3.5-14B, InternVL3.5-38B, Devstral-Small-2512, Llama3.2-11B-Vision and GLM-4.6V-Flash`；hardware=`NVIDIA A6000 GPUs for open-source models`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`paired task-completion and active privacy-extraction outcomes`。

**Trade-off、failure、共存与演进。** benchmark secret 与攻击策略覆盖有限；未泄漏不证明模型无记忆或生产 ACL 正确。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18996v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18996:start -->
Claim boundary：仅 `arXiv:2606.18996v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18996:end -->
<!-- review:SF-2026-ARXIV-2606-18996:end -->

<!-- review:SF-2026-ARXIV-2606-19004:start -->
### 2606.19004 — Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training

**问题与旧路径。** Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively expensive, requiring thousands of high-end GPUs. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。 唯一知识 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 比较 seed exploration quality、GPU utilization、成本与训练结果。 Method=`https://arxiv.org/html/2606.19004v1 — § exact-v1 anchor: Seed Exploration and Spot GPUs`；Evaluation=`https://arxiv.org/html/2606.19004v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen-Image`；hardware=`4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`training reward/quality, GPU utilization and spot cost`。

**Trade-off、failure、共存与演进。** spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19004v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19004:start -->
Claim boundary：仅 `arXiv:2606.19004v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19004:end -->
<!-- review:SF-2026-ARXIV-2606-19004:end -->

<!-- review:SF-2026-ARXIV-2606-19025:start -->
### 2606.19025 — FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs

**问题与旧路径。** Pre-training Large Language Models (LLMs) typically demands large-scale infrastructure with tightly coupled hardware accelerators. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 通信相对高效 baseline 最多降 1.42x、相对 DDP 降 45.44x，skip-token 吞吐最高 1.4x；100B 只由 cost model 投影。 Method=`https://arxiv.org/html/2606.19025v1 — § exact-v1 anchor: partitioning expert layers across workers`；Evaluation=`https://arxiv.org/html/2606.19025v1 — § exact-v1 evaluation anchor: FoMoE Scalability & Resource Consumption`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`communication volume, local-training throughput and routing stability; 100B results are modeled projections`。

**Trade-off、failure、共存与演进。** non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19025v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19025:start -->
Claim boundary：仅 `arXiv:2606.19025v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19025:end -->
<!-- review:SF-2026-ARXIV-2606-19025:end -->

<!-- review:SF-2026-ARXIV-2606-19057:start -->
### 2606.19057 — Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning

**问题与旧路径。** Large Language Models (LLMs) are increasingly used as judges for scalable evaluation, yet such LLM--as--a--Judge systems exhibit systematic biases that are decoupled from semantic quality, most notably verbosity bias. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 用受控与真实 LLM evaluation data 比较 PU 估计、校准与 audit coverage。 Method=`https://arxiv.org/html/2606.19057v1 — § exact-v1 anchor: Positive–Unlabeled Learning`；Evaluation=`https://arxiv.org/html/2606.19057v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Mistral-7B-Instruct, Qwen2.5-7B-Instruct, Llemma-7B-MuInstruct and GPT-5.4-mini judges`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`hidden-positive prevalence, calibration and audit error`。

**Trade-off、failure、共存与演进。** class-prior 错设会系统性偏移；PU 只能估计分布级缺口，不能证明单个 judgment 正确。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19057v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19057:start -->
Claim boundary：仅 `arXiv:2606.19057v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19057:end -->
<!-- review:SF-2026-ARXIV-2606-19057:end -->

<!-- review:SF-2026-ARXIV-2606-19111:start -->
### 2606.19111 — Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams

**问题与旧路径。** Team science holds that leadership is contingent: it helps only under specific conditions, and capable, autonomous teams may need none at all. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** leader 只有在 coordinator 的 recovery advantage 超过沟通与单点故障成本时才应持有重分配 authority；行为 leadership 不等于稳定角色标签。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 多 Agent team configurations 上测 coordination behavior、failure recovery 与任务结果。 Method=`https://arxiv.org/html/2606.19111v1 — § exact-v1 anchor: Recovery-Advantage Boundary`；Evaluation=`https://arxiv.org/html/2606.19111v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`gpt-oss-120b, gemma-4-31B-it and llama-4-scout`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`team outcome, behavioral leadership signatures and recovery advantage`。

**Trade-off、failure、共存与演进。** 作者 tasks 和 agent count 不证明组织结构普适；leader failure、shared bias 与通信成本仍可能主导。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19111v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19111:start -->
Claim boundary：仅 `arXiv:2606.19111v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19111:end -->
<!-- review:SF-2026-ARXIV-2606-19111:end -->

<!-- review:SF-2026-ARXIV-2606-19191:start -->
### 2606.19191 — PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems

**问题与旧路径。** Agent skills allow LLM-based coding agents to acquire domain-specific capabilities from third-party packages, but they also introduce a new supply-chain attack surface. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** VulMask 跨 host skills、四类攻击、Cursor backbones 与多个 automated reviewers；GPT-5.5 设置 ASR 58.8%、warning 11.4%。 Method=`https://arxiv.org/html/2606.19191v1 — § exact-v1 anchor: 3 Threat Model`；Evaluation=`https://arxiv.org/html/2606.19191v1 — § exact-v1 evaluation anchor: 5 Evaluation`。Benchmark contract：model=`GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`attack success, warning/detection and benign utility across four attack goals`。

**Trade-off、failure、共存与演进。** 攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19191v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion`。

<!-- claim:SF-2026-ARXIV-2606-19191:start -->
Claim boundary：仅 `arXiv:2606.19191v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19191:end -->
<!-- review:SF-2026-ARXIV-2606-19191:end -->

<!-- review:SF-2026-ARXIV-2606-19242:start -->
### 2606.19242 — Runtime Compliance Verification for AI Agents

**问题与旧路径。** AI agents now handle personal data through tool use, function calls, and multi turn dialogue, which can create obligations under the General Data Protection Regulation (GDPR). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 policies、agent traces 与 violation cases 上评 runtime verification。 Method=`https://arxiv.org/html/2606.19242v1 — § exact-v1 anchor: Runtime Compliance Verification`；Evaluation=`https://arxiv.org/html/2606.19242v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`policy-violation detection and runtime enforcement outcomes`。

**Trade-off、failure、共存与演进。** 形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19242v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19242:start -->
Claim boundary：仅 `arXiv:2606.19242v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19242:end -->
<!-- review:SF-2026-ARXIV-2606-19242:end -->

<!-- review:SF-2026-ARXIV-2606-19262:start -->
### 2606.19262 — Detecting Hidden ML Training With Zero-Overhead Telemetry

**问题与旧路径。** Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。 唯一知识 owner 为 `PLATFORM-MONITORING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在多种 ML/non-ML workloads 与 hardware traces 上报告检测质量及 zero-overhead claim。 Method=`https://arxiv.org/html/2606.19262v1 — § exact-v1 anchor: Zero-Overhead Telemetry`；Evaluation=`https://arxiv.org/html/2606.19262v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`nine NVIDIA GPU models across four architecture generations`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`hidden-training detection, false positives and telemetry overhead`。

**Trade-off、failure、共存与演进。** 共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19262v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19262:start -->
Claim boundary：仅 `arXiv:2606.19262v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19262:end -->
<!-- review:SF-2026-ARXIV-2606-19262:end -->

<!-- review:SF-2026-ARXIV-2606-19271:start -->
### 2606.19271 — TurboServe: Serving Streaming Video Generation Efficiently and Economically

**问题与旧路径。** Streaming video generation is emerging as a new serving workload in which users interact with long-lived sessions that generate video progressively, chunk by chunk. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** TurboServe 报告 worst-case per-chunk latency 降 37.5%、平均 GPU cost 降 37.2%。 Method=`https://arxiv.org/html/2606.19271v1 — § exact-v1 anchor: Streaming Video Generation`；Evaluation=`https://arxiv.org/html/2606.19271v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`GPU clusters with up to 64 NVIDIA B300 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`worst-case per-chunk latency, end-to-end quality and GPU operating cost`。

**Trade-off、failure、共存与演进。** 作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19271v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19271:start -->
Claim boundary：仅 `arXiv:2606.19271v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19271:end -->
<!-- review:SF-2026-ARXIV-2606-19271:end -->

<!-- review:SF-2026-ARXIV-2606-19409:start -->
### 2606.19409 — OpenRath: Session-Centered Runtime State for Agent Systems

**问题与旧路径。** Modern agent systems often suffer from fragmented runtime state: transcripts, tool effects, memory events, workspace placement, branch provenance, and replay evidence are recorded separately and become difficult to inspect or reproduce. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 报告只验证 controlled runtime properties 与 audited milestones，没有 broad quantitative comparison。 Method=`https://arxiv.org/html/2606.19409v1 — § exact-v1 anchor: Session-Centered Runtime State`；Evaluation=`https://arxiv.org/html/2606.19409v1 — § exact-v1 evaluation anchor: audited milestones`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`audited runtime invariants and controlled replay properties; no broad quality benchmark`。

**Trade-off、failure、共存与演进。** live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19409v1 — § exact-v1 limitation/counterevidence anchor: claims are limited`。

<!-- claim:SF-2026-ARXIV-2606-19409:start -->
Claim boundary：仅 `arXiv:2606.19409v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19409:end -->
<!-- review:SF-2026-ARXIV-2606-19409:end -->

<!-- review:SF-2026-ARXIV-2606-19464:start -->
### 2606.19464 — Deontic Policies for Runtime Governance of Agentic AI Systems

**问题与旧路径。** Autonomous agentic AI systems driven by Large Language Models (LLMs) introduce a new class of security, privacy, and compliance challenges: an agent that can invoke tools, manipulate data, install software, and coordinate with peer agents across organizational boundaries must be constrained not just by authentication and access control, but by the full structure of enterprise governance. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 以 AgenticRei examples 展示 tool calls 与 A2A messages 的 policy expression/evaluation。 Method=`https://arxiv.org/html/2606.19464v1 — § exact-v1 anchor: obligations, dispensations`；Evaluation=`https://arxiv.org/html/2606.19464v1 — § exact-v1 evaluation anchor: examples`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`expressibility and runtime policy-evaluation examples`。

**Trade-off、failure、共存与演进。** 示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19464v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19464:start -->
Claim boundary：仅 `arXiv:2606.19464v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19464:end -->
<!-- review:SF-2026-ARXIV-2606-19464:end -->

<!-- review:SF-2026-ARXIV-2606-19535:start -->
### 2606.19535 — FloatDoor: Platform-Triggered Backdoors in LLMs

**问题与旧路径。** Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B 跨 NVIDIA GPU、Google TPU、AWS Graviton、Alibaba Yitian-710，并展示目标平台 code vulnerability。 Method=`https://arxiv.org/html/2606.19535v1 — § exact-v1 anchor: platform-triggered backdoor`；Evaluation=`https://arxiv.org/html/2606.19535v1 — § exact-v1 evaluation anchor: broad range of deployment targets`。Benchmark contract：model=`Qwen3-4B and Qwen3-8B with two LoRA adapters`；hardware=`NVIDIA H200, NVIDIA A100, NVIDIA H100, NVIDIA DGX Spark, Google TPU, AWS Graviton and Alibaba Yitian-710`；precision=`Not Disclosed`；batch=`1`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`target-platform activation, aggregate utility and vulnerable-code generation`。

**Trade-off、failure、共存与演进。** 攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19535v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19535:start -->
Claim boundary：仅 `arXiv:2606.19535v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19535:end -->
<!-- review:SF-2026-ARXIV-2606-19535:end -->

<!-- review:SF-2026-ARXIV-2606-19544:start -->
### 2606.19544 — Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias

**问题与旧路径。** LLM-as-a-Judge has become the dominant evaluation paradigm for language models, but judge validation in practice relies on exact-match agreement, a metric that does not correct for chance and systematically overstates discriminative ability. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 21 judges、9 providers、3 benchmarks、118 runs、约 541k judgments；报告 kappa deflation 与 ranking shifts。 Method=`https://arxiv.org/html/2606.19544v1 — § exact-v1 anchor: Minimum Viable Validation Protocol`；Evaluation=`https://arxiv.org/html/2606.19544v1 — § exact-v1 evaluation anchor: 118 runs`。Benchmark contract：model=`Gemini 3.1 Pro, Claude Opus 4.6, DeepSeek V3.2, Claude Sonnet 4.6, Llama 3.3 70B, Kimi K2.5, GPT-5.4, GPT-4o, GPT-4.1, Gemini 2.5 Pro, GLM-5, GPT-oss 120B, Claude Sonnet 4, Gemini 2.5 Flash, Claude Haiku 4.5, GPT-4.1-mini, Minimax M2.7, Qwen 3 8B, GPT-4o-mini, Mixtral 8x22B and GPT-5.4-mini`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`agreement, Cohen's kappa, test-retest consistency, position bias and verbosity bias`。

**Trade-off、failure、共存与演进。** 三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19544v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-19544:start -->
Claim boundary：仅 `arXiv:2606.19544v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19544:end -->
<!-- review:SF-2026-ARXIV-2606-19544:end -->

<!-- review:SF-2026-ARXIV-2606-19559:start -->
### 2606.19559 — Uncertainty Decomposition for Clarification Seeking in LLM Agents

**问题与旧路径。** Recent position papers argue that the classical aleatoric/epistemic uncertainty framework is insufficient for interactive large language model (LLM) agents and call for underspecification-aware, decomposed, and communicable uncertainty representations that can unlock new agent capabilities such as proactive clarification seeking and shared mental-model building. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。 唯一知识 owner 为 `AGENT-PLANNING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 backbones，在 WebShop/ALFWorld clarification variants 与 REAL 上比较 clarification F1/fault detection。 Method=`https://arxiv.org/html/2606.19559v1 — § exact-v1 anchor: action confidence from request uncertainty`；Evaluation=`https://arxiv.org/html/2606.19559v1 — § exact-v1 evaluation anchor: five LLM backbones`。Benchmark contract：model=`GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B and GPT-OSS-120B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`clarification F1 and fault detection across clarification and standard benchmarks`。

**Trade-off、failure、共存与演进。** prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19559v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19559:start -->
Claim boundary：仅 `arXiv:2606.19559v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19559:end -->
<!-- review:SF-2026-ARXIV-2606-19559:end -->

<!-- review:SF-2026-ARXIV-2606-19595:start -->
### 2606.19595 — IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows

**问题与旧路径。** Voice agents deployed in structured workflows (customer service, healthcare scheduling, account management) must handle frequent user interruptions while maintaining progress through multi-step procedures. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** IHBench 在 structured workflows 上测 interruption 后 task completion 与 recovery error。 Method=`https://arxiv.org/html/2606.19595v1 — § exact-v1 anchor: Post-Interruption Recovery`；Evaluation=`https://arxiv.org/html/2606.19595v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`GPT-4o Audio, GPT-4o Mini Audio, GPT Audio, GPT Audio Mini, GPT Realtime, GPT Realtime 1.5, GPT Realtime Mini, GPT Realtime 2, Gemini 2.5 Flash, Gemini 2.5 Pro, Gemini 3 Flash, Gemini 3.1 Pro, Gemini 3.1 Flash Live, Gemma 4 12B Instruct, Qwen3-Omni-30B-A3B-Instruct, Qwen2.5-Omni-7B, Phi-4-Multimodal-Instruct, Voxtral-Small-24B-2507, Qwen2-Audio-7B-Instruct, MiMo-Audio-7B-Instruct and Kimi-Audio-7B-Instruct across 27 mode/configuration combinations`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`post-interruption task completion and structured recovery error`。

**Trade-off、failure、共存与演进。** 模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19595v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19595:start -->
Claim boundary：仅 `arXiv:2606.19595v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19595:end -->
<!-- review:SF-2026-ARXIV-2606-19595:end -->

<!-- review:SF-2026-ARXIV-2606-19613:start -->
### 2606.19613 — StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns

**问题与旧路径。** We introduce StaminaBench, a benchmark that measures the stamina of coding agents: how many consecutive interaction turns (change requests) they can handle before failing. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 6 harnesses×7 open LLMs、20 scenarios×100 turns；所有模型 5–6 turns 内失败，test feedback/retry 最多提升 12×。 Method=`https://arxiv.org/html/2606.19613v1 — § exact-v1 anchor: 100 Interaction Turns`；Evaluation=`https://arxiv.org/html/2606.19613v1 — § exact-v1 evaluation anchor: 20 scenarios`。Benchmark contract：model=`Devstral 2, Devstral Small 2, GLM-5, Kimi K2.5, Nemotron Super, Qwen3-Coder-Next and Qwen3.5-122B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`consecutive passed turns, test feedback/retry effect and harness sensitivity over 20x100-turn scenarios`。

**Trade-off、failure、共存与演进。** 程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19613v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19613:start -->
Claim boundary：仅 `arXiv:2606.19613v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19613:end -->
<!-- review:SF-2026-ARXIV-2606-19613:end -->

<!-- review:SF-2026-ARXIV-2606-19667:start -->
### 2606.19667 — CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference

**问题与旧路径。** Retrieval-Augmented Generation (RAG) improves factual grounding, but it also lengthens prompts and raises prefill cost. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。 唯一知识 owner 为 `INFER-KV-CACHE`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 三个 vLLM configurations，median TTFT 降约 20–33%，QA quality 未下降；greedy 达 oracle TTFT gain 的 97.5%。 Method=`https://arxiv.org/html/2606.19667v1 — § exact-v1 anchor: prefix tree over recently served evidence sequences`；Evaluation=`https://arxiv.org/html/2606.19667v1 — § exact-v1 evaluation anchor: three vLLM configurations`。Benchmark contract：model=`Qwen2.5-1.5B and Qwen2.5-7B`；hardware=`RTX 4060 Ti 8 GB, RTX 4090 24 GB and RTX 4090D 24 GB`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`median TTFT, prefix reuse and QA answer quality`。

**Trade-off、failure、共存与演进。** 重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19667v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19667:start -->
Claim boundary：仅 `arXiv:2606.19667v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19667:end -->
<!-- review:SF-2026-ARXIV-2606-19667:end -->

<!-- review:SF-2026-ARXIV-2606-20736:start -->
### 2606.20736 — REKEY: Metadata-Grounded Visual-Key Regeneration for Contamination-Resilient VQA Evaluation

**问题与旧路径。** Static visual question answering (VQA) benchmarks age quickly: Once the items leak into training corpora, scores can reflect memorization rather than genuine visual ability, thus obscuring real progress. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 受污染 benchmark 可把 answer-bearing visual key 变成运行时随机生成、human-validated edit slot，并保留 construction-grounded label。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** V*Bench 上 8 个 frontier VLM；原题比 regenerated variants 高 9.5–18.8pp。 Method=`https://arxiv.org/html/2606.20736v1 — § exact-v1 anchor: randomly regenerates the answer-bearing local detail`；Evaluation=`https://arxiv.org/html/2606.20736v1 — § exact-v1 evaluation anchor: eight frontier vision-language models`。Benchmark contract：model=`Qwen3.6-Plus, GPT-5.5, Claude Opus 4.7, Gemini 3.1 Pro, Seed-2.0-Lite, Kimi K2.6, MiMo v2.5 and Llama 4 Maverick; LLaVA-1.5-13B for difficulty calibration`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`accuracy gap between original and regenerated V*Bench items with controlled search difficulty`。

**Trade-off、failure、共存与演进。** 只更新局部 visual key，不能消除题型、metadata 或训练 pipeline 泄漏；图像编辑真实性依赖人工验证。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.20736v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-20736:start -->
Claim boundary：仅 `arXiv:2606.20736v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-20736:end -->
<!-- review:SF-2026-ARXIV-2606-20736:end -->

<!-- review:SF-2026-ARXIV-2606-20746:start -->
### 2606.20746 — Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection

**问题与旧路径。** Most prompt-injection detectors score a single event or message. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** slow-burn injection detector 可在 executed action edges 上累积冻结 per-event score 的 CUSUM persistence；它只能放大已有 margin，不能创造 detector 没有的 margin。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 集中攻击 gap +0.092（clustered bootstrap）；repo-exfil persistence AUC 0.708，但 broader clean-path AUC 0.167，且仅 3–4 independent tasks。 Method=`https://arxiv.org/html/2606.20746v1 — § exact-v1 anchor: detector of record`；Evaluation=`https://arxiv.org/html/2606.20746v1 — § exact-v1 evaluation anchor: broader clean-path actions`。Benchmark contract：model=`frozen char-ngram SVM plus embedding-contrastive detector; held-out cloaking target`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`clustered-bootstrap gap and persistence/peak delta AUC on executed-edge trajectories`。

**Trade-off、failure、共存与演进。** 这是明确的 boundary result，不是 deployable detector；小 independent denominator 阻断功效外推。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.20746v1 — § exact-v1 limitation/counterevidence anchor: boundary result, not a deployable detector`。

<!-- claim:SF-2026-ARXIV-2606-20746:start -->
Claim boundary：仅 `arXiv:2606.20746v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-20746:end -->
<!-- review:SF-2026-ARXIV-2606-20746:end -->

<!-- review:SF-2026-ARXIV-2606-21089:start -->
### 2606.21089 — Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines

**问题与旧路径。** Industrial LLM teams often ship behavior updates by repeatedly DPO-training a base model on sequences of related preference-data campaigns. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 重复 DPO campaign 的 checkpoint 链需要另存 strategy/evaluator memory；保留旧能力不等于积累了如何训练下一 campaign 的科学知识。 唯一知识 owner 为 `TRAIN-DPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen2.5-7B-Instruct、30 campaigns；单 seed 5-condition×3-step chain 加异构/多 seed pilots，4/5 candidates 退化。 Method=`https://arxiv.org/html/2606.21089v1 — § exact-v1 anchor: scientific amnesia`；Evaluation=`https://arxiv.org/html/2606.21089v1 — § exact-v1 evaluation anchor: single-seed 5-condition`。Benchmark contract：model=`Qwen2.5-7B-Instruct`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`campaign-level peak pass@1 and intervention deltas across 30 HumanEval subdomains`。

**Trade-off、failure、共存与演进。** 主要结果单 seed，pilots 又显示 regime dependence；不能声称 MSCL 或 retrieval 已解决问题。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.21089v1 — § exact-v1 limitation/counterevidence anchor: diagnostic, not a claim`。

<!-- claim:SF-2026-ARXIV-2606-21089:start -->
Claim boundary：仅 `arXiv:2606.21089v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-21089:end -->
<!-- review:SF-2026-ARXIV-2606-21089:end -->

<!-- review:SF-2026-ARXIV-2606-21090:start -->
### 2606.21090 — Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training

**问题与旧路径。** Self-improvement can self-regress. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** post-training control loop 应分别持有 campaign-level memory、within-campaign early stop 与 optimizer；峰值 checkpoint 必须先于最终 collapse 被保存和晋级。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen2.5-3B/7B，10×20-step campaigns，多 seed；比较 CARE、ES、GRPO，并有 Gemma-3-4B pilot。 Method=`https://arxiv.org/html/2606.21090v1 — § exact-v1 anchor: rise-then-collapse pattern`；Evaluation=`https://arxiv.org/html/2606.21090v1 — § exact-v1 evaluation anchor: 10 sequential 20-step campaigns`。Benchmark contract：model=`Qwen2.5-3B, Qwen2.5-7B and a Gemma-3-4B pilot`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`pass@1 trajectory, peak-to-end collapse and multi-seed intervention comparison`。

**Trade-off、failure、共存与演进。** GRPO 抬高 floor 但未消除约 17pp cliff；GRPO+ES 仅 3 seeds 且 mixed，不能推出统一配方。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.21090v1 — § exact-v1 limitation/counterevidence anchor: mixed evidence`。

<!-- claim:SF-2026-ARXIV-2606-21090:start -->
Claim boundary：仅 `arXiv:2606.21090v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-21090:end -->
<!-- review:SF-2026-ARXIV-2606-21090:end -->

<!-- review:SF-2026-ARXIV-2606-28374:start -->
### 2606.28374 — Recursive Self-Evolving Agents via Held-Out Selection

**问题与旧路径。** LLM agents are increasingly improved without weight updates by evolving a natural-language artifact, such as reflections, workflows, playbooks, cheatsheets, or optimized prompts, that conditions a frozen policy. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 自然语言 strategy/skill/playbook 的每代 rewrite 只能在 disjoint held-out split 不退化时 commit，否则回退 base ReAct。 唯一知识 owner 为 `AGENT-REFLECTION`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** ALFWorld、GAIA、tau-bench、WebShop，6 baselines、共享本地 backbone；Dynamic Cheatsheet 在 WebShop collapse。 Method=`https://arxiv.org/html/2606.28374v1 — § exact-v1 anchor: strict keep-better gate`；Evaluation=`https://arxiv.org/html/2606.28374v1 — § exact-v1 evaluation anchor: four diverse benchmarks`。Benchmark contract：model=`Qwen2.5-7B-Instruct for ALFWorld and Qwen3-30B-A3B-Instruct for GAIA, tau-bench and WebShop`；hardware=`4 NVIDIA A100 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`benchmark score, McNemar test and regression gate across four agent benchmarks`。

**Trade-off、failure、共存与演进。** held-out split 仍可能与部署同分布共偏；无 artifact 普遍获胜，strict gate 只证明这四个 benchmark 的单调安全。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.28374v1 — § exact-v1 limitation/counterevidence anchor: no artifact universally wins`。

<!-- claim:SF-2026-ARXIV-2606-28374:start -->
Claim boundary：仅 `arXiv:2606.28374v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-28374:end -->
<!-- review:SF-2026-ARXIV-2606-28374:end -->

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18600 | score_7_9; potential_books_delta | selected | DA-20260618-HETEROGENEOUS-RECOVERY | — | 唯一同时改变 placement 与 interruption recovery 的 serving family，进入三项叙事。 | analysis:DA-20260618-HETEROGENEOUS-RECOVERY |
| SF-2026-ARXIV-2606-18619 | score_7_9; potential_books_delta | not_selected | — | — | 把 agent 判断转成可反证 artifact，补足安全 evidence plane，优先于纯检测率改进。 | analysis-decision:SF-2026-ARXIV-2606-18619 |
| SF-2026-ARXIV-2606-18650 | score_7_9 | not_selected | — | — | Ch27 已拥有动态 data admission 与 proxy bias；本工作强化求解器分支但不新增 owner。 | analysis-decision:SF-2026-ARXIV-2606-18650 |
| SF-2026-ARXIV-2606-18668 | score_7_9 | not_selected | — | — | Ch82 已有 typed failure handoff、reroute 与 fallback authority；EARS 提供生产证据，不另建 abstention owner。 | analysis-decision:SF-2026-ARXIV-2606-18668 |
| SF-2026-ARXIV-2606-18673 | score_7_9 | not_selected | — | — | Ch72 已明确 prompt 不是 secret store；AREA 只作为受限 sensor 分支。 | analysis-decision:SF-2026-ARXIV-2606-18673 |
| SF-2026-ARXIV-2606-18697 | score_7_9; potential_books_delta | not_selected | — | — | 首次把 world-model adaptation data 显式定位为 downstream planning authority 的供应链边界。 | analysis-decision:SF-2026-ARXIV-2606-18697 |
| SF-2026-ARXIV-2606-18741 | score_7_9; potential_books_delta | not_selected | — | — | 它改变 serving topology 的运行时 commit protocol，不只是更好的静态 scheduler。 | analysis-decision:SF-2026-ARXIV-2606-18741 |
| SF-2026-ARXIV-2606-18746 | score_7_9 | not_selected | — | — | Ch77/79 已区分 memory state 与 environment state；该定理加强必要性证明。 | analysis-decision:SF-2026-ARXIV-2606-18746 |
| SF-2026-ARXIV-2606-18810 | score_7_9 | not_selected | — | — | Ch33 已拥有 token credit 与 verifier 共偏边界；保留为不依赖外部 teacher 的证据。 | analysis-decision:SF-2026-ARXIV-2606-18810 |
| SF-2026-ARXIV-2606-18829 | score_7_9 | not_selected | — | — | Ch72 已有同一 exact family 的 Utility/ACL/Forgetting Gate 与代价边界；本日只保留证据 handoff。 | analysis-decision:SF-2026-ARXIV-2606-18829 |
| SF-2026-ARXIV-2606-18831 | score_7_9; potential_books_delta | not_selected | — | — | 训练 mixture 把检索、证据合成、推理拆成可审计能力，而非只调 reward。 | analysis-decision:SF-2026-ARXIV-2606-18831 |
| SF-2026-ARXIV-2606-18847 | score_7_9; potential_books_delta | not_selected | — | — | 它把 memory retrieval 与真实 action/state evolution接起来，属于 embodied owner 的长期 delta。 | analysis-decision:SF-2026-ARXIV-2606-18847 |
| SF-2026-ARXIV-2606-18874 | score_7_9 | not_selected | — | — | Ch81/66 已拥有 claim-evidence lineage 与 harness identity；Xcientist 是具体实例。 | analysis-decision:SF-2026-ARXIV-2606-18874 |
| SF-2026-ARXIV-2606-18958 | score_7_9 | not_selected | — | — | Ch73 已把 simulation、canary 与真实 deployment evidence 分层；LiveStack 是更深的 OS 实现实例。 | analysis-decision:SF-2026-ARXIV-2606-18958 |
| SF-2026-ARXIV-2606-18967 | score_7_9; potential_books_delta | not_selected | — | — | 它把 speculative verification 延伸到训练 rollout，同时保留 policy/version owner。 | analysis-decision:SF-2026-ARXIV-2606-18967 |
| SF-2026-ARXIV-2606-18996 | score_7_9 | not_selected | — | — | Ch66/72 已要求 capability 与 harm 双轴评价；TRAP 补充 workload 而不改 owner。 | analysis-decision:SF-2026-ARXIV-2606-18996 |
| SF-2026-ARXIV-2606-19004 | score_7_9 | not_selected | — | — | Ch63/33 已有 preemptible training 与 rollout identity；本工作是 DiT-specific composition。 | analysis-decision:SF-2026-ARXIV-2606-19004 |
| SF-2026-ARXIV-2606-19025 | score_7_9; potential_books_delta | selected | DA-20260618-CROSS-SITE-MOE-OWNERSHIP | — | 它改变跨站 distributed-training replica/state ownership，而不是 serving placement。 | analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP |
| SF-2026-ARXIV-2606-19057 | score_7_9; potential_books_delta | not_selected | — | — | 把未审样本从默认负例改成不确定集合，直接修正 evaluation denominator。 | analysis-decision:SF-2026-ARXIV-2606-19057 |
| SF-2026-ARXIV-2606-19111 | score_7_9 | not_selected | — | — | Ch82 已把 coordinator 视为可替换 control role；本 family 提供 recovery boundary 证据。 | analysis-decision:SF-2026-ARXIV-2606-19111 |
| SF-2026-ARXIV-2606-19191 | score_7_9 | not_selected | — | — | Ch72 已把 persistent Skill 定义为 supply-chain artifact，并要求 code/resource/runtime effect 联合审计与 containment。 | analysis-decision:SF-2026-ARXIV-2606-19191 |
| SF-2026-ARXIV-2606-19242 | score_7_9 | not_selected | — | — | Ch72 已拥有 canonical action 与 effect-time authorization；论文强化实现路径。 | analysis-decision:SF-2026-ARXIV-2606-19242 |
| SF-2026-ARXIV-2606-19262 | score_7_9; potential_books_delta | not_selected | — | — | 它为平台监控增加未注册训练的被动 evidence path，而不把检测器提升为执行授权。 | analysis-decision:SF-2026-ARXIV-2606-19262 |
| SF-2026-ARXIV-2606-19271 | score_7_9 | not_selected | — | — | Ch56 已有 streaming generation 的 playout slack、migration/re-homing、elasticity 与质量降级；TurboServe 是生产 trace 佐证。 | analysis-decision:SF-2026-ARXIV-2606-19271 |
| SF-2026-ARXIV-2606-19409 | score_7_9 | not_selected | — | — | Ch84 已含同一 exact family 的 Session runtime value、fork/merge/replay 和 controlled-property boundary。 | analysis-decision:SF-2026-ARXIV-2606-19409 |
| SF-2026-ARXIV-2606-19464 | score_7_9 | not_selected | — | — | Ch72 已有 policy version、obligation 与外部 reference monitor；无需复制 DSL。 | analysis-decision:SF-2026-ARXIV-2606-19464 |
| SF-2026-ARXIV-2606-19535 | score_7_9; potential_books_delta | selected | DA-20260618-PLATFORM-BOUND-ARTIFACT | — | 它把 platform/kernel 纳入模型供应链的可执行 identity，而非仅记录权重 hash。 | analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT |
| SF-2026-ARXIV-2606-19544 | score_7_9 | not_selected | — | — | Ch66 已把 reliability、validity、bias 分离；本大样本是强验证而非新机制。 | analysis-decision:SF-2026-ARXIV-2606-19544 |
| SF-2026-ARXIV-2606-19559 | score_7_9 | not_selected | — | — | Ch79 已拥有 ask/act gate 与 uncertainty decomposition；保留跨 backbone 证据。 | analysis-decision:SF-2026-ARXIV-2606-19559 |
| SF-2026-ARXIV-2606-19595 | score_7_9 | not_selected | — | — | Ch81 已有 durable checkpoints 与 idempotent resume；IHBench补充 voice workload。 | analysis-decision:SF-2026-ARXIV-2606-19595 |
| SF-2026-ARXIV-2606-19613 | score_7_9; potential_books_delta | not_selected | — | — | 它给长期 session 的 degradation/first-failure 一个不同于独立 pass@1 的 evaluation contract。 | analysis-decision:SF-2026-ARXIV-2606-19613 |
| SF-2026-ARXIV-2606-19667 | score_7_9; potential_books_delta | not_selected | — | — | 它连接 RAG evidence ordering 与 prefix-cache locality，同时保持 relevance owner 不变。 | analysis-decision:SF-2026-ARXIV-2606-19667 |
| SF-2026-ARXIV-2606-20736 | score_7_9; potential_books_delta | not_selected | — | — | 它把 benchmark freshness 从发布时清洁度转成每次 evaluation 的生成 contract。 | analysis-decision:SF-2026-ARXIV-2606-20736 |
| SF-2026-ARXIV-2606-20746 | score_7_9 | not_selected | — | — | Ch72 已有 run-level cumulative harm 与 temporal invariant；本 family 的窄带负结果作为 sensor 边界 handoff。 | analysis-decision:SF-2026-ARXIV-2606-20746 |
| SF-2026-ARXIV-2606-21089 | score_7_9; potential_books_delta | not_selected | — | — | 它区分 capability retention 与 method-learning state，修正 repeated DPO 的错误自改进叙事。 | analysis-decision:SF-2026-ARXIV-2606-21089 |
| SF-2026-ARXIV-2606-21090 | score_7_9; potential_books_delta | not_selected | — | — | 它把 self-training collapse 定位到 within-campaign promotion gate，而不是笼统归因 catastrophic forgetting。 | analysis-decision:SF-2026-ARXIV-2606-21090 |
| SF-2026-ARXIV-2606-28374 | score_7_9 | not_selected | — | — | Ch80 已有 held-out promotion/rollback；RSEA提供跨 benchmark 负证据而非新 owner。 | analysis-decision:SF-2026-ARXIV-2606-28374 |

<!-- analysis-decision:SF-2026-ARXIV-2606-18619:start -->
把 agent 判断转成可反证 artifact，补足安全 evidence plane，优先于纯检测率改进。
<!-- analysis-decision:SF-2026-ARXIV-2606-18619:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18650:start -->
Ch27 已拥有动态 data admission 与 proxy bias；本工作强化求解器分支但不新增 owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-18650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18668:start -->
Ch82 已有 typed failure handoff、reroute 与 fallback authority；EARS 提供生产证据，不另建 abstention owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-18668:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18673:start -->
Ch72 已明确 prompt 不是 secret store；AREA 只作为受限 sensor 分支。
<!-- analysis-decision:SF-2026-ARXIV-2606-18673:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18697:start -->
首次把 world-model adaptation data 显式定位为 downstream planning authority 的供应链边界。
<!-- analysis-decision:SF-2026-ARXIV-2606-18697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18741:start -->
它改变 serving topology 的运行时 commit protocol，不只是更好的静态 scheduler。
<!-- analysis-decision:SF-2026-ARXIV-2606-18741:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18746:start -->
Ch77/79 已区分 memory state 与 environment state；该定理加强必要性证明。
<!-- analysis-decision:SF-2026-ARXIV-2606-18746:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18810:start -->
Ch33 已拥有 token credit 与 verifier 共偏边界；保留为不依赖外部 teacher 的证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-18810:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18829:start -->
Ch72 已有同一 exact family 的 Utility/ACL/Forgetting Gate 与代价边界；本日只保留证据 handoff。
<!-- analysis-decision:SF-2026-ARXIV-2606-18829:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18831:start -->
训练 mixture 把检索、证据合成、推理拆成可审计能力，而非只调 reward。
<!-- analysis-decision:SF-2026-ARXIV-2606-18831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18847:start -->
它把 memory retrieval 与真实 action/state evolution接起来，属于 embodied owner 的长期 delta。
<!-- analysis-decision:SF-2026-ARXIV-2606-18847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18874:start -->
Ch81/66 已拥有 claim-evidence lineage 与 harness identity；Xcientist 是具体实例。
<!-- analysis-decision:SF-2026-ARXIV-2606-18874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18958:start -->
Ch73 已把 simulation、canary 与真实 deployment evidence 分层；LiveStack 是更深的 OS 实现实例。
<!-- analysis-decision:SF-2026-ARXIV-2606-18958:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18967:start -->
它把 speculative verification 延伸到训练 rollout，同时保留 policy/version owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-18967:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18996:start -->
Ch66/72 已要求 capability 与 harm 双轴评价；TRAP 补充 workload 而不改 owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-18996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19004:start -->
Ch63/33 已有 preemptible training 与 rollout identity；本工作是 DiT-specific composition。
<!-- analysis-decision:SF-2026-ARXIV-2606-19004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19057:start -->
把未审样本从默认负例改成不确定集合，直接修正 evaluation denominator。
<!-- analysis-decision:SF-2026-ARXIV-2606-19057:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19111:start -->
Ch82 已把 coordinator 视为可替换 control role；本 family 提供 recovery boundary 证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-19111:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19191:start -->
Ch72 已把 persistent Skill 定义为 supply-chain artifact，并要求 code/resource/runtime effect 联合审计与 containment。
<!-- analysis-decision:SF-2026-ARXIV-2606-19191:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19242:start -->
Ch72 已拥有 canonical action 与 effect-time authorization；论文强化实现路径。
<!-- analysis-decision:SF-2026-ARXIV-2606-19242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19262:start -->
它为平台监控增加未注册训练的被动 evidence path，而不把检测器提升为执行授权。
<!-- analysis-decision:SF-2026-ARXIV-2606-19262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19271:start -->
Ch56 已有 streaming generation 的 playout slack、migration/re-homing、elasticity 与质量降级；TurboServe 是生产 trace 佐证。
<!-- analysis-decision:SF-2026-ARXIV-2606-19271:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19409:start -->
Ch84 已含同一 exact family 的 Session runtime value、fork/merge/replay 和 controlled-property boundary。
<!-- analysis-decision:SF-2026-ARXIV-2606-19409:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19464:start -->
Ch72 已有 policy version、obligation 与外部 reference monitor；无需复制 DSL。
<!-- analysis-decision:SF-2026-ARXIV-2606-19464:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19544:start -->
Ch66 已把 reliability、validity、bias 分离；本大样本是强验证而非新机制。
<!-- analysis-decision:SF-2026-ARXIV-2606-19544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19559:start -->
Ch79 已拥有 ask/act gate 与 uncertainty decomposition；保留跨 backbone 证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-19559:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19595:start -->
Ch81 已有 durable checkpoints 与 idempotent resume；IHBench补充 voice workload。
<!-- analysis-decision:SF-2026-ARXIV-2606-19595:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19613:start -->
它给长期 session 的 degradation/first-failure 一个不同于独立 pass@1 的 evaluation contract。
<!-- analysis-decision:SF-2026-ARXIV-2606-19613:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19667:start -->
它连接 RAG evidence ordering 与 prefix-cache locality，同时保持 relevance owner 不变。
<!-- analysis-decision:SF-2026-ARXIV-2606-19667:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20736:start -->
它把 benchmark freshness 从发布时清洁度转成每次 evaluation 的生成 contract。
<!-- analysis-decision:SF-2026-ARXIV-2606-20736:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20746:start -->
Ch72 已有 run-level cumulative harm 与 temporal invariant；本 family 的窄带负结果作为 sensor 边界 handoff。
<!-- analysis-decision:SF-2026-ARXIV-2606-20746:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21089:start -->
它区分 capability retention 与 method-learning state，修正 repeated DPO 的错误自改进叙事。
<!-- analysis-decision:SF-2026-ARXIV-2606-21089:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21090:start -->
它把 self-training collapse 定位到 within-campaign promotion gate，而不是笼统归因 catastrophic forgetting。
<!-- analysis-decision:SF-2026-ARXIV-2606-21090:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28374:start -->
Ch80 已有 held-out promotion/rollback；RSEA提供跨 benchmark 负证据而非新 owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-28374:end -->

<!-- analysis:DA-20260618-HETEROGENEOUS-RECOVERY:start -->
### DA-20260618-HETEROGENEOUS-RECOVERY
异构 spot serving 的控制对象不是一张静态 placement 表，而是 topology、request/KV state 与 replacement lifecycle。只有把重配置和输出恢复纳入同一 commit，成本优化才不会以分钟级中断换取。
<!-- analysis:DA-20260618-HETEROGENEOUS-RECOVERY:end -->

<!-- analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP:start -->
### DA-20260618-CROSS-SITE-MOE-OWNERSHIP
跨站 MoE 训练的关键不是把数据并行原样搬到 WAN，而是重新划分 expert/state ownership：每站只持有分区 expert，有限复制承担热点与可用性，non-resident token 以显式 skip 规则改变本地更新分布。实测通信和吞吐只覆盖作者配置，100B 仍是模型投影。
<!-- analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP:end -->

<!-- analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT:start -->
### DA-20260618-PLATFORM-BOUND-ARTIFACT
权重 hash 不能单独定义可执行模型身份。FloatDoor 表明同一权重和 LoRA 组合可利用 platform/kernel 浮点差异触发不同任务，因此 audit artifact 必须绑定目标硬件、kernel 和 serving build；跨平台差异本身仍不证明后门存在。
<!-- analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18600 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-18600 | delta:SF-2026-ARXIV-2606-18600 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18600 |
| SF-2026-ARXIV-2606-18619 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18619 | delta:SF-2026-ARXIV-2606-18619 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18619 |
| SF-2026-ARXIV-2606-18650 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-18650 | delta:SF-2026-ARXIV-2606-18650 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18650 |
| SF-2026-ARXIV-2606-18668 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-18668 | delta:SF-2026-ARXIV-2606-18668 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18668 |
| SF-2026-ARXIV-2606-18673 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18673 | delta:SF-2026-ARXIV-2606-18673 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18673 |
| SF-2026-ARXIV-2606-18697 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | existing:SF-2026-ARXIV-2606-18697 | delta:SF-2026-ARXIV-2606-18697 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18697 |
| SF-2026-ARXIV-2606-18741 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-18741 | delta:SF-2026-ARXIV-2606-18741 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18741 |
| SF-2026-ARXIV-2606-18746 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-18746 | delta:SF-2026-ARXIV-2606-18746 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18746 |
| SF-2026-ARXIV-2606-18810 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-18810 | delta:SF-2026-ARXIV-2606-18810 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18810 |
| SF-2026-ARXIV-2606-18829 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18829 | delta:SF-2026-ARXIV-2606-18829 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18829 |
| SF-2026-ARXIV-2606-18831 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-18831 | delta:SF-2026-ARXIV-2606-18831 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18831 |
| SF-2026-ARXIV-2606-18847 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-18847 | delta:SF-2026-ARXIV-2606-18847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18847 |
| SF-2026-ARXIV-2606-18874 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-18874 | delta:SF-2026-ARXIV-2606-18874 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18874 |
| SF-2026-ARXIV-2606-18958 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18958 | delta:SF-2026-ARXIV-2606-18958 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18958 |
| SF-2026-ARXIV-2606-18967 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2606-18967 | delta:SF-2026-ARXIV-2606-18967 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18967 |
| SF-2026-ARXIV-2606-18996 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-18996 | delta:SF-2026-ARXIV-2606-18996 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18996 |
| SF-2026-ARXIV-2606-19004 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-19004 | delta:SF-2026-ARXIV-2606-19004 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19004 |
| SF-2026-ARXIV-2606-19025 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-19025 | delta:SF-2026-ARXIV-2606-19025 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19025 |
| SF-2026-ARXIV-2606-19057 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19057 | delta:SF-2026-ARXIV-2606-19057 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19057 |
| SF-2026-ARXIV-2606-19111 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-19111 | delta:SF-2026-ARXIV-2606-19111 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19111 |
| SF-2026-ARXIV-2606-19191 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19191 | delta:SF-2026-ARXIV-2606-19191 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19191 |
| SF-2026-ARXIV-2606-19242 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19242 | delta:SF-2026-ARXIV-2606-19242 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19242 |
| SF-2026-ARXIV-2606-19262 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-19262 | delta:SF-2026-ARXIV-2606-19262 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19262 |
| SF-2026-ARXIV-2606-19271 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-19271 | delta:SF-2026-ARXIV-2606-19271 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19271 |
| SF-2026-ARXIV-2606-19409 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-19409 | delta:SF-2026-ARXIV-2606-19409 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19409 |
| SF-2026-ARXIV-2606-19464 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19464 | delta:SF-2026-ARXIV-2606-19464 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19464 |
| SF-2026-ARXIV-2606-19535 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19535 | delta:SF-2026-ARXIV-2606-19535 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19535 |
| SF-2026-ARXIV-2606-19544 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19544 | delta:SF-2026-ARXIV-2606-19544 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19544 |
| SF-2026-ARXIV-2606-19559 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-19559 | delta:SF-2026-ARXIV-2606-19559 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19559 |
| SF-2026-ARXIV-2606-19595 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-19595 | delta:SF-2026-ARXIV-2606-19595 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19595 |
| SF-2026-ARXIV-2606-19613 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19613 | delta:SF-2026-ARXIV-2606-19613 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19613 |
| SF-2026-ARXIV-2606-19667 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-19667 | delta:SF-2026-ARXIV-2606-19667 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19667 |
| SF-2026-ARXIV-2606-20736 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-20736 | delta:SF-2026-ARXIV-2606-20736 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20736 |
| SF-2026-ARXIV-2606-20746 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-20746 | delta:SF-2026-ARXIV-2606-20746 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20746 |
| SF-2026-ARXIV-2606-21089 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#L1 | books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-21089 | delta:SF-2026-ARXIV-2606-21089 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21089 |
| SF-2026-ARXIV-2606-21090 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-21090 | delta:SF-2026-ARXIV-2606-21090 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21090 |
| SF-2026-ARXIV-2606-28374 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-28374 | delta:SF-2026-ARXIV-2606-28374 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28374 |

<!-- existing:SF-2026-ARXIV-2606-18600:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.18600v1: 唯一同时改变 placement 与 interruption recovery 的 serving family，进入三项叙事。
<!-- existing:SF-2026-ARXIV-2606-18600:end -->

<!-- delta:SF-2026-ARXIV-2606-18600:start -->
异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。
<!-- delta:SF-2026-ARXIV-2606-18600:end -->

<!-- books-review:SF-2026-ARXIV-2606-18600:start -->
Direct Evolution; Integrate. 六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。
<!-- books-review:SF-2026-ARXIV-2606-18600:end -->

<!-- existing:SF-2026-ARXIV-2606-18619:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18619v1: 把 agent 判断转成可反证 artifact，补足安全 evidence plane，优先于纯检测率改进。
<!-- existing:SF-2026-ARXIV-2606-18619:end -->

<!-- delta:SF-2026-ARXIV-2606-18619:start -->
Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。
<!-- delta:SF-2026-ARXIV-2606-18619:end -->

<!-- books-review:SF-2026-ARXIV-2606-18619:start -->
Direct Evolution; Integrate. fuzzer 未触发不等于 invariant 成立，assertion 也可能错；覆盖限于作者 subjects 与可观测运行输入。
<!-- books-review:SF-2026-ARXIV-2606-18619:end -->

<!-- existing:SF-2026-ARXIV-2606-18650:start -->
现有 owner 已把数据选择建模为带 lineage、proxy coverage、动态反馈与 admission gate 的控制问题；相邻预训练章消费冻结后的数据 contract。 Comparative result for arXiv:2606.18650v1: Ch27 已拥有动态 data admission 与 proxy bias；本工作强化求解器分支但不新增 owner。
<!-- existing:SF-2026-ARXIV-2606-18650:end -->

<!-- delta:SF-2026-ARXIV-2606-18650:start -->
训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。
<!-- delta:SF-2026-ARXIV-2606-18650:end -->

<!-- books-review:SF-2026-ARXIV-2606-18650:start -->
Principle Reuse; No Change — Existing Coverage. proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。
<!-- books-review:SF-2026-ARXIV-2606-18650:end -->

<!-- existing:SF-2026-ARXIV-2606-18668:start -->
现有 owner 已拥有 coordinator、typed handoff、reroute、shared-state commit 与 fallback authority；相邻 workflow 章拥有单流程执行。 Comparative result for arXiv:2606.18668v1: Ch82 已有 typed failure handoff、reroute 与 fallback authority；EARS 提供生产证据，不另建 abstention owner。
<!-- existing:SF-2026-ARXIV-2606-18668:end -->

<!-- delta:SF-2026-ARXIV-2606-18668:start -->
sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。
<!-- delta:SF-2026-ARXIV-2606-18668:end -->

<!-- books-review:SF-2026-ARXIV-2606-18668:start -->
Principle Reuse; No Change — Existing Coverage. judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。
<!-- books-review:SF-2026-ARXIV-2606-18668:end -->

<!-- existing:SF-2026-ARXIV-2606-18673:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18673v1: Ch72 已明确 prompt 不是 secret store；AREA 只作为受限 sensor 分支。
<!-- existing:SF-2026-ARXIV-2606-18673:end -->

<!-- delta:SF-2026-ARXIV-2606-18673:start -->
system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。
<!-- delta:SF-2026-ARXIV-2606-18673:end -->

<!-- books-review:SF-2026-ARXIV-2606-18673:start -->
Principle Reuse; No Change — Existing Coverage. attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。
<!-- books-review:SF-2026-ARXIV-2606-18673:end -->

<!-- existing:SF-2026-ARXIV-2606-18697:start -->
现有 owner 已拥有 learned dynamics、planning feedback 与环境真值边界；相邻生成范式章不拥有 planning control。 Comparative result for arXiv:2606.18697v1: 首次把 world-model adaptation data 显式定位为 downstream planning authority 的供应链边界。
<!-- existing:SF-2026-ARXIV-2606-18697:end -->

<!-- delta:SF-2026-ARXIV-2606-18697:start -->
world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。
<!-- delta:SF-2026-ARXIV-2606-18697:end -->

<!-- books-review:SF-2026-ARXIV-2606-18697:start -->
Direct Evolution; Integrate. 只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。
<!-- books-review:SF-2026-ARXIV-2606-18697:end -->

<!-- existing:SF-2026-ARXIV-2606-18741:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.18741v1: 它改变 serving topology 的运行时 commit protocol，不只是更好的静态 scheduler。
<!-- existing:SF-2026-ARXIV-2606-18741:end -->

<!-- delta:SF-2026-ARXIV-2606-18741:start -->
runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。
<!-- delta:SF-2026-ARXIV-2606-18741:end -->

<!-- books-review:SF-2026-ARXIV-2606-18741:start -->
Direct Evolution; Integrate. KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。
<!-- books-review:SF-2026-ARXIV-2606-18741:end -->

<!-- existing:SF-2026-ARXIV-2606-18746:start -->
现有 owner 已区分 observation/memory/environment state 及其读写生命周期；相邻 RAG 章只拥有 evidence retrieval。 Comparative result for arXiv:2606.18746v1: Ch77/79 已区分 memory state 与 environment state；该定理加强必要性证明。
<!-- existing:SF-2026-ARXIV-2606-18746:end -->

<!-- delta:SF-2026-ARXIV-2606-18746:start -->
若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。
<!-- delta:SF-2026-ARXIV-2606-18746:end -->

<!-- books-review:SF-2026-ARXIV-2606-18746:start -->
Principle Reuse; No Change — Existing Coverage. 定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。
<!-- books-review:SF-2026-ARXIV-2606-18746:end -->

<!-- existing:SF-2026-ARXIV-2606-18810:start -->
现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。 Comparative result for arXiv:2606.18810v1: Ch33 已拥有 token credit 与 verifier 共偏边界；保留为不依赖外部 teacher 的证据。
<!-- existing:SF-2026-ARXIV-2606-18810:end -->

<!-- delta:SF-2026-ARXIV-2606-18810:start -->
SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。
<!-- delta:SF-2026-ARXIV-2606-18810:end -->

<!-- books-review:SF-2026-ARXIV-2606-18810:start -->
Principle Reuse; No Change — Existing Coverage. self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。
<!-- books-review:SF-2026-ARXIV-2606-18810:end -->

<!-- existing:SF-2026-ARXIV-2606-18829:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18829v1: Ch72 已有同一 exact family 的 Utility/ACL/Forgetting Gate 与代价边界；本日只保留证据 handoff。
<!-- existing:SF-2026-ARXIV-2606-18829:end -->

<!-- delta:SF-2026-ARXIV-2606-18829:start -->
共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。
<!-- delta:SF-2026-ARXIV-2606-18829:end -->

<!-- books-review:SF-2026-ARXIV-2606-18829:start -->
Principle Reuse; No Change — Existing Coverage. structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。
<!-- books-review:SF-2026-ARXIV-2606-18829:end -->

<!-- existing:SF-2026-ARXIV-2606-18831:start -->
现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。 Comparative result for arXiv:2606.18831v1: 训练 mixture 把检索、证据合成、推理拆成可审计能力，而非只调 reward。
<!-- existing:SF-2026-ARXIV-2606-18831:end -->

<!-- delta:SF-2026-ARXIV-2606-18831:start -->
long-context RL 的 data owner 应同时覆盖 retrieval、multi-evidence synthesis 与 reasoning，避免只通过 reward shaping 修补 evidence localization。
<!-- delta:SF-2026-ARXIV-2606-18831:end -->

<!-- books-review:SF-2026-ARXIV-2606-18831:start -->
Direct Evolution; Integrate. 作者 mixture 与 Qwen family 不能证明通用配方；outcome reward 仍可能奖励无 grounding shortcut。
<!-- books-review:SF-2026-ARXIV-2606-18831:end -->

<!-- existing:SF-2026-ARXIV-2606-18847:start -->
现有 owner 已拥有 observation-action-state 闭环与真实执行反馈；相邻 world-model 章提供预测状态而不拥有 action commit。 Comparative result for arXiv:2606.18847v1: 它把 memory retrieval 与真实 action/state evolution接起来，属于 embodied owner 的长期 delta。
<!-- existing:SF-2026-ARXIV-2606-18847:end -->

<!-- delta:SF-2026-ARXIV-2606-18847:start -->
长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。
<!-- delta:SF-2026-ARXIV-2606-18847:end -->

<!-- books-review:SF-2026-ARXIV-2606-18847:start -->
Direct Evolution; Integrate. benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。
<!-- books-review:SF-2026-ARXIV-2606-18847:end -->

<!-- existing:SF-2026-ARXIV-2606-18874:start -->
现有 owner 已拥有 durable checkpoint、claim-evidence lineage、idempotent resume 与人工接管；相邻 reflection 章只提出修正信号。 Comparative result for arXiv:2606.18874v1: Ch81/66 已拥有 claim-evidence lineage 与 harness identity；Xcientist 是具体实例。
<!-- existing:SF-2026-ARXIV-2606-18874:end -->

<!-- delta:SF-2026-ARXIV-2606-18874:start -->
AI scientist 应把 literature evidence、idea、implementation、ablation 与 repair trace 外化为 persistent contracts，并检查 runnable artifact 是否仍支持原 claim。
<!-- delta:SF-2026-ARXIV-2606-18874:end -->

<!-- books-review:SF-2026-ARXIV-2606-18874:start -->
Principle Reuse; No Change — Existing Coverage. 三个案例不证明自动科学发现质量；trace 完整也不能替代独立复现或可信实验。
<!-- books-review:SF-2026-ARXIV-2606-18874:end -->

<!-- existing:SF-2026-ARXIV-2606-18958:start -->
现有 owner 已区分 simulation、shadow、canary 与 production evidence，并保留 rollback；相邻安全章拥有授权而非发布。 Comparative result for arXiv:2606.18958v1: Ch73 已把 simulation、canary 与真实 deployment evidence 分层；LiveStack 是更深的 OS 实现实例。
<!-- existing:SF-2026-ARXIV-2606-18958:end -->

<!-- delta:SF-2026-ARXIV-2606-18958:start -->
cluster live simulation 要让真实 software stack 与模拟 node/network/device time 协同推进，并显式区分 simulated resource state 与 production effect。
<!-- delta:SF-2026-ARXIV-2606-18958:end -->

<!-- books-review:SF-2026-ARXIV-2606-18958:start -->
Principle Reuse; No Change — Existing Coverage. 模拟器遗漏的 kernel、network tail 和 control-plane race 会制造假确定性；不能用 live simulation 代替 canary。
<!-- books-review:SF-2026-ARXIV-2606-18958:end -->

<!-- existing:SF-2026-ARXIV-2606-18967:start -->
现有 owner 已拥有 draft/target verification、acceptance、KV rollback 与质量等价边界；相邻 PagedAttention 章只拥有块化 KV。 Comparative result for arXiv:2606.18967v1: 它把 speculative verification 延伸到训练 rollout，同时保留 policy/version owner。
<!-- existing:SF-2026-ARXIV-2606-18967:end -->

<!-- delta:SF-2026-ARXIV-2606-18967:start -->
RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。
<!-- delta:SF-2026-ARXIV-2606-18967:end -->

<!-- books-review:SF-2026-ARXIV-2606-18967:start -->
Direct Evolution; Integrate. acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。
<!-- books-review:SF-2026-ARXIV-2606-18967:end -->

<!-- existing:SF-2026-ARXIV-2606-18996:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.18996v1: Ch66/72 已要求 capability 与 harm 双轴评价；TRAP 补充 workload 而不改 owner。
<!-- existing:SF-2026-ARXIV-2606-18996:end -->

<!-- delta:SF-2026-ARXIV-2606-18996:start -->
privacy-capable agent benchmark 必须联合评分 task completion 与 active extraction resistance，并把攻击者交互轨迹、secret canary 与 policy effect 分开。
<!-- delta:SF-2026-ARXIV-2606-18996:end -->

<!-- books-review:SF-2026-ARXIV-2606-18996:start -->
Principle Reuse; No Change — Existing Coverage. benchmark secret 与攻击策略覆盖有限；未泄漏不证明模型无记忆或生产 ACL 正确。
<!-- books-review:SF-2026-ARXIV-2606-18996:end -->

<!-- existing:SF-2026-ARXIV-2606-19004:start -->
现有 owner 已拥有 quota、priority、preemption、checkpoint cost 与 workload-class-aware placement；相邻 KAI 章是实现分支。 Comparative result for arXiv:2606.19004v1: Ch63/33 已有 preemptible training 与 rollout identity；本工作是 DiT-specific composition。
<!-- existing:SF-2026-ARXIV-2606-19004:end -->

<!-- delta:SF-2026-ARXIV-2606-19004:start -->
DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。
<!-- delta:SF-2026-ARXIV-2606-19004:end -->

<!-- books-review:SF-2026-ARXIV-2606-19004:start -->
Principle Reuse; No Change — Existing Coverage. spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。
<!-- books-review:SF-2026-ARXIV-2606-19004:end -->

<!-- existing:SF-2026-ARXIV-2606-19025:start -->
现有 owner 已拥有 replica/shard/state synchronization 与 WAN failure boundary；相邻 TP 章只拥有张量切分。 Comparative result for arXiv:2606.19025v1: 它改变跨站 distributed-training replica/state ownership，而不是 serving placement。
<!-- existing:SF-2026-ARXIV-2606-19025:end -->

<!-- delta:SF-2026-ARXIV-2606-19025:start -->
低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。
<!-- delta:SF-2026-ARXIV-2606-19025:end -->

<!-- books-review:SF-2026-ARXIV-2606-19025:start -->
Direct Evolution; Integrate. non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。
<!-- books-review:SF-2026-ARXIV-2606-19025:end -->

<!-- existing:SF-2026-ARXIV-2606-19057:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19057v1: 把未审样本从默认负例改成不确定集合，直接修正 evaluation denominator。
<!-- existing:SF-2026-ARXIV-2606-19057:end -->

<!-- delta:SF-2026-ARXIV-2606-19057:start -->
当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。
<!-- delta:SF-2026-ARXIV-2606-19057:end -->

<!-- books-review:SF-2026-ARXIV-2606-19057:start -->
Direct Evolution; Integrate. class-prior 错设会系统性偏移；PU 只能估计分布级缺口，不能证明单个 judgment 正确。
<!-- books-review:SF-2026-ARXIV-2606-19057:end -->

<!-- existing:SF-2026-ARXIV-2606-19111:start -->
现有 owner 已拥有 coordinator、typed handoff、reroute、shared-state commit 与 fallback authority；相邻 workflow 章拥有单流程执行。 Comparative result for arXiv:2606.19111v1: Ch82 已把 coordinator 视为可替换 control role；本 family 提供 recovery boundary 证据。
<!-- existing:SF-2026-ARXIV-2606-19111:end -->

<!-- delta:SF-2026-ARXIV-2606-19111:start -->
leader 只有在 coordinator 的 recovery advantage 超过沟通与单点故障成本时才应持有重分配 authority；行为 leadership 不等于稳定角色标签。
<!-- delta:SF-2026-ARXIV-2606-19111:end -->

<!-- books-review:SF-2026-ARXIV-2606-19111:start -->
Principle Reuse; No Change — Existing Coverage. 作者 tasks 和 agent count 不证明组织结构普适；leader failure、shared bias 与通信成本仍可能主导。
<!-- books-review:SF-2026-ARXIV-2606-19111:end -->

<!-- existing:SF-2026-ARXIV-2606-19191:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19191v1: Ch72 已把 persistent Skill 定义为 supply-chain artifact，并要求 code/resource/runtime effect 联合审计与 containment。
<!-- existing:SF-2026-ARXIV-2606-19191:end -->

<!-- delta:SF-2026-ARXIV-2606-19191:start -->
skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。
<!-- delta:SF-2026-ARXIV-2606-19191:end -->

<!-- books-review:SF-2026-ARXIV-2606-19191:start -->
Principle Reuse; No Change — Existing Coverage. 攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。
<!-- books-review:SF-2026-ARXIV-2606-19191:end -->

<!-- existing:SF-2026-ARXIV-2606-19242:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19242v1: Ch72 已拥有 canonical action 与 effect-time authorization；论文强化实现路径。
<!-- existing:SF-2026-ARXIV-2606-19242:end -->

<!-- delta:SF-2026-ARXIV-2606-19242:start -->
Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。
<!-- delta:SF-2026-ARXIV-2606-19242:end -->

<!-- books-review:SF-2026-ARXIV-2606-19242:start -->
Principle Reuse; No Change — Existing Coverage. 形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。
<!-- books-review:SF-2026-ARXIV-2606-19242:end -->

<!-- existing:SF-2026-ARXIV-2606-19262:start -->
现有 owner 已区分 observe-only telemetry、告警证据与执行授权；相邻 trace 章拥有跨组件因果链。 Comparative result for arXiv:2606.19262v1: 它为平台监控增加未注册训练的被动 evidence path，而不把检测器提升为执行授权。
<!-- existing:SF-2026-ARXIV-2606-19262:end -->

<!-- delta:SF-2026-ARXIV-2606-19262:start -->
hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。
<!-- delta:SF-2026-ARXIV-2606-19262:end -->

<!-- books-review:SF-2026-ARXIV-2606-19262:start -->
Direct Evolution; Integrate. 共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。
<!-- books-review:SF-2026-ARXIV-2606-19262:end -->

<!-- existing:SF-2026-ARXIV-2606-19271:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.19271v1: Ch56 已有 streaming generation 的 playout slack、migration/re-homing、elasticity 与质量降级；TurboServe 是生产 trace 佐证。
<!-- existing:SF-2026-ARXIV-2606-19271:end -->

<!-- delta:SF-2026-ARXIV-2606-19271:start -->
streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。
<!-- delta:SF-2026-ARXIV-2606-19271:end -->

<!-- books-review:SF-2026-ARXIV-2606-19271:start -->
Principle Reuse; No Change — Existing Coverage. 作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。
<!-- books-review:SF-2026-ARXIV-2606-19271:end -->

<!-- existing:SF-2026-ARXIV-2606-19409:start -->
现有 owner 已拥有 typed Session、branch/merge/replay、runtime identity 与 controlled release；相邻 MCP 章只拥有协议交接。 Comparative result for arXiv:2606.19409v1: Ch84 已含同一 exact family 的 Session runtime value、fork/merge/replay 和 controlled-property boundary。
<!-- existing:SF-2026-ARXIV-2606-19409:end -->

<!-- delta:SF-2026-ARXIV-2606-19409:start -->
Session 应成为执行路径携带的一等 runtime value，统一 transcript、tool effect、sandbox、branch lineage、token usage、pending work 与 memory event；fork/merge/replay 是显式操作。
<!-- delta:SF-2026-ARXIV-2606-19409:end -->

<!-- books-review:SF-2026-ARXIV-2606-19409:start -->
Principle Reuse; No Change — Existing Coverage. live-provider quality、optional backend availability 与 memory quality明确未证明；central Session 也可能扩大故障域。
<!-- books-review:SF-2026-ARXIV-2606-19409:end -->

<!-- existing:SF-2026-ARXIV-2606-19464:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19464v1: Ch72 已有 policy version、obligation 与外部 reference monitor；无需复制 DSL。
<!-- existing:SF-2026-ARXIV-2606-19464:end -->

<!-- delta:SF-2026-ARXIV-2606-19464:start -->
runtime governance 除 permit/prohibit 外还需 obligation lifecycle、dispensation、meta-policy precedence 与 ontology reasoning，并在 LLM 外执行。
<!-- delta:SF-2026-ARXIV-2606-19464:end -->

<!-- books-review:SF-2026-ARXIV-2606-19464:start -->
Principle Reuse; No Change — Existing Coverage. 示例不构成吞吐、安全或完备性证明；ontology/policy conflict 仍需可信 owner 与版本治理。
<!-- books-review:SF-2026-ARXIV-2606-19464:end -->

<!-- existing:SF-2026-ARXIV-2606-19535:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19535v1: 它把 platform/kernel 纳入模型供应链的可执行 identity，而非仅记录权重 hash。
<!-- existing:SF-2026-ARXIV-2606-19535:end -->

<!-- delta:SF-2026-ARXIV-2606-19535:start -->
model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。
<!-- delta:SF-2026-ARXIV-2606-19535:end -->

<!-- books-review:SF-2026-ARXIV-2606-19535:start -->
Direct Evolution; Integrate. 攻击依赖作者平台集合与 LoRA；跨平台不一致不等于任意模型都可植入，可信构建仍需独立证明。
<!-- books-review:SF-2026-ARXIV-2606-19535:end -->

<!-- existing:SF-2026-ARXIV-2606-19544:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19544v1: Ch66 已把 reliability、validity、bias 分离；本大样本是强验证而非新机制。
<!-- existing:SF-2026-ARXIV-2606-19544:end -->

<!-- delta:SF-2026-ARXIV-2606-19544:start -->
Judge validation 要同时报告 chance-corrected agreement、test-retest consistency 与 position/verbosity bias；高 consistency 不能替代 validity。
<!-- delta:SF-2026-ARXIV-2606-19544:end -->

<!-- books-review:SF-2026-ARXIV-2606-19544:start -->
Principle Reuse; No Change — Existing Coverage. 三个 benchmark 与单一 pairwise rubric 不证明所有 judge 场景；Cohen kappa 也依赖 prevalence。
<!-- books-review:SF-2026-ARXIV-2606-19544:end -->

<!-- existing:SF-2026-ARXIV-2606-19559:start -->
现有 owner 已拥有 ask/act gate、uncertainty decomposition、依赖图与预算；相邻 reflection 章只拥有复核。 Comparative result for arXiv:2606.19559v1: Ch79 已拥有 ask/act gate 与 uncertainty decomposition；保留跨 backbone 证据。
<!-- existing:SF-2026-ARXIV-2606-19559:end -->

<!-- delta:SF-2026-ARXIV-2606-19559:start -->
黑盒 Agent 可把 action confidence 与 request uncertainty 分开；只有后者高时触发 clarification，避免把执行不确定与需求欠规范混成 abstention。
<!-- delta:SF-2026-ARXIV-2606-19559:end -->

<!-- books-review:SF-2026-ARXIV-2606-19559:start -->
Principle Reuse; No Change — Existing Coverage. prompt-based uncertainty 未校准成概率；benchmark 人工制造 50% 欠规范，澄清成本和用户响应质量未被完整建模。
<!-- books-review:SF-2026-ARXIV-2606-19559:end -->

<!-- existing:SF-2026-ARXIV-2606-19595:start -->
现有 owner 已拥有 durable checkpoint、claim-evidence lineage、idempotent resume 与人工接管；相邻 reflection 章只提出修正信号。 Comparative result for arXiv:2606.19595v1: Ch81 已有 durable checkpoints 与 idempotent resume；IHBench补充 voice workload。
<!-- existing:SF-2026-ARXIV-2606-19595:end -->

<!-- delta:SF-2026-ARXIV-2606-19595:start -->
voice-agent interruption recovery 必须保存 workflow node、已提交 side effects 与待确认槽位，恢复时区分 resume、repair、restart。
<!-- delta:SF-2026-ARXIV-2606-19595:end -->

<!-- books-review:SF-2026-ARXIV-2606-19595:start -->
Principle Reuse; No Change — Existing Coverage. 模拟中断与语音管线不覆盖真实网络/ASR drift；恢复成功也不证明重复 effect 被阻止。
<!-- books-review:SF-2026-ARXIV-2606-19595:end -->

<!-- existing:SF-2026-ARXIV-2606-19613:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19613v1: 它给长期 session 的 degradation/first-failure 一个不同于独立 pass@1 的 evaluation contract。
<!-- existing:SF-2026-ARXIV-2606-19613:end -->

<!-- delta:SF-2026-ARXIV-2606-19613:start -->
coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。
<!-- delta:SF-2026-ARXIV-2606-19613:end -->

<!-- books-review:SF-2026-ARXIV-2606-19613:start -->
Direct Evolution; Integrate. 程序生成 REST workload 不能代表全部软件演化；turn-to-failure 对变更难度和 harness 强敏感。
<!-- books-review:SF-2026-ARXIV-2606-19613:end -->

<!-- existing:SF-2026-ARXIV-2606-19667:start -->
现有 owner 已拥有 prefix identity、cache reuse、失效与跨请求共享边界；相邻 continuous batching 章只拥有批次调度。 Comparative result for arXiv:2606.19667v1: 它连接 RAG evidence ordering 与 prefix-cache locality，同时保持 relevance owner 不变。
<!-- existing:SF-2026-ARXIV-2606-19667:end -->

<!-- delta:SF-2026-ARXIV-2606-19667:start -->
RAG evidence set 不变时，可用近期 evidence-sequence prefix tree 重排证据，让集合重叠转成 token-prefix 重用；retriever 仍拥有 relevance，scheduler 只拥有顺序。
<!-- delta:SF-2026-ARXIV-2606-19667:end -->

<!-- books-review:SF-2026-ARXIV-2606-19667:start -->
Direct Evolution; Integrate. 重排可能改变 positional bias 与答案；局部 query locality 不保证生产 cache hit，且不减少 decode cost。
<!-- books-review:SF-2026-ARXIV-2606-19667:end -->

<!-- existing:SF-2026-ARXIV-2606-20736:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.20736v1: 它把 benchmark freshness 从发布时清洁度转成每次 evaluation 的生成 contract。
<!-- existing:SF-2026-ARXIV-2606-20736:end -->

<!-- delta:SF-2026-ARXIV-2606-20736:start -->
受污染 benchmark 可把 answer-bearing visual key 变成运行时随机生成、human-validated edit slot，并保留 construction-grounded label。
<!-- delta:SF-2026-ARXIV-2606-20736:end -->

<!-- books-review:SF-2026-ARXIV-2606-20736:start -->
Direct Evolution; Integrate. 只更新局部 visual key，不能消除题型、metadata 或训练 pipeline 泄漏；图像编辑真实性依赖人工验证。
<!-- books-review:SF-2026-ARXIV-2606-20736:end -->

<!-- existing:SF-2026-ARXIV-2606-20746:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.20746v1: Ch72 已有 run-level cumulative harm 与 temporal invariant；本 family 的窄带负结果作为 sensor 边界 handoff。
<!-- existing:SF-2026-ARXIV-2606-20746:end -->

<!-- delta:SF-2026-ARXIV-2606-20746:start -->
slow-burn injection detector 可在 executed action edges 上累积冻结 per-event score 的 CUSUM persistence；它只能放大已有 margin，不能创造 detector 没有的 margin。
<!-- delta:SF-2026-ARXIV-2606-20746:end -->

<!-- books-review:SF-2026-ARXIV-2606-20746:start -->
Principle Reuse; No Change — Existing Coverage. 这是明确的 boundary result，不是 deployable detector；小 independent denominator 阻断功效外推。
<!-- books-review:SF-2026-ARXIV-2606-20746:end -->

<!-- existing:SF-2026-ARXIV-2606-21089:start -->
现有 owner 已拥有 preference data、reference-policy identity、checkpoint 与 evaluation boundary；相邻 RLHF 章拥有上游偏好反馈。 Comparative result for arXiv:2606.21089v1: 它区分 capability retention 与 method-learning state，修正 repeated DPO 的错误自改进叙事。
<!-- existing:SF-2026-ARXIV-2606-21089:end -->

<!-- delta:SF-2026-ARXIV-2606-21089:start -->
重复 DPO campaign 的 checkpoint 链需要另存 strategy/evaluator memory；保留旧能力不等于积累了如何训练下一 campaign 的科学知识。
<!-- delta:SF-2026-ARXIV-2606-21089:end -->

<!-- books-review:SF-2026-ARXIV-2606-21089:start -->
Direct Evolution; Integrate. 主要结果单 seed，pilots 又显示 regime dependence；不能声称 MSCL 或 retrieval 已解决问题。
<!-- books-review:SF-2026-ARXIV-2606-21089:end -->

<!-- existing:SF-2026-ARXIV-2606-21090:start -->
现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。 Comparative result for arXiv:2606.21090v1: 它把 self-training collapse 定位到 within-campaign promotion gate，而不是笼统归因 catastrophic forgetting。
<!-- existing:SF-2026-ARXIV-2606-21090:end -->

<!-- delta:SF-2026-ARXIV-2606-21090:start -->
post-training control loop 应分别持有 campaign-level memory、within-campaign early stop 与 optimizer；峰值 checkpoint 必须先于最终 collapse 被保存和晋级。
<!-- delta:SF-2026-ARXIV-2606-21090:end -->

<!-- books-review:SF-2026-ARXIV-2606-21090:start -->
Direct Evolution; Integrate. GRPO 抬高 floor 但未消除约 17pp cliff；GRPO+ES 仅 3 seeds 且 mixed，不能推出统一配方。
<!-- books-review:SF-2026-ARXIV-2606-21090:end -->

<!-- existing:SF-2026-ARXIV-2606-28374:start -->
现有 owner 已拥有 held-out verifier、promotion/rollback、budget 与 provenance；相邻 planning 章拥有行动方案。 Comparative result for arXiv:2606.28374v1: Ch80 已有 held-out promotion/rollback；RSEA提供跨 benchmark 负证据而非新 owner。
<!-- existing:SF-2026-ARXIV-2606-28374:end -->

<!-- delta:SF-2026-ARXIV-2606-28374:start -->
自然语言 strategy/skill/playbook 的每代 rewrite 只能在 disjoint held-out split 不退化时 commit，否则回退 base ReAct。
<!-- delta:SF-2026-ARXIV-2606-28374:end -->

<!-- books-review:SF-2026-ARXIV-2606-28374:start -->
Principle Reuse; No Change — Existing Coverage. held-out split 仍可能与部署同分布共偏；无 artifact 普遍获胜，strict gate 只证明这四个 benchmark 的单调安全。
<!-- books-review:SF-2026-ARXIV-2606-28374:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260618-COVERAGE-V1 | fresh-context:jun18-v1 | coverage | coverage:SRC-ARXIV:20260618 | — | 516/516 title+abstract; denominator 37; closures 479; all 104 route-negative checked | passed |
| SA-20260618-EVIDENCE-V1 | fresh-context:jun18-v1 | evidence | review:SF-2026-ARXIV-2606-18600; review:SF-2026-ARXIV-2606-18619; review:SF-2026-ARXIV-2606-18650; review:SF-2026-ARXIV-2606-18668; review:SF-2026-ARXIV-2606-18673; review:SF-2026-ARXIV-2606-18697; review:SF-2026-ARXIV-2606-18741; review:SF-2026-ARXIV-2606-18746; review:SF-2026-ARXIV-2606-18810; review:SF-2026-ARXIV-2606-18829; review:SF-2026-ARXIV-2606-18831; review:SF-2026-ARXIV-2606-18847; review:SF-2026-ARXIV-2606-18874; review:SF-2026-ARXIV-2606-18958; review:SF-2026-ARXIV-2606-18967; review:SF-2026-ARXIV-2606-18996; review:SF-2026-ARXIV-2606-19004; review:SF-2026-ARXIV-2606-19025; review:SF-2026-ARXIV-2606-19057; review:SF-2026-ARXIV-2606-19111; review:SF-2026-ARXIV-2606-19191; review:SF-2026-ARXIV-2606-19242; review:SF-2026-ARXIV-2606-19262; review:SF-2026-ARXIV-2606-19271; review:SF-2026-ARXIV-2606-19409; review:SF-2026-ARXIV-2606-19464; review:SF-2026-ARXIV-2606-19535; review:SF-2026-ARXIV-2606-19544; review:SF-2026-ARXIV-2606-19559; review:SF-2026-ARXIV-2606-19595; review:SF-2026-ARXIV-2606-19613; review:SF-2026-ARXIV-2606-19667; review:SF-2026-ARXIV-2606-20736; review:SF-2026-ARXIV-2606-20746; review:SF-2026-ARXIV-2606-21089; review:SF-2026-ARXIV-2606-21090; review:SF-2026-ARXIV-2606-28374 | — | 37/37 official exact-v1 Method/Evaluation/boundary and named benchmark contracts | passed |
| SA-20260618-SELECTION-V1 | fresh-context:jun18-v1 | deep_analysis_selection | analysis:DA-20260618-HETEROGENEOUS-RECOVERY; analysis-decision:SF-2026-ARXIV-2606-18619; analysis-decision:SF-2026-ARXIV-2606-18650; analysis-decision:SF-2026-ARXIV-2606-18668; analysis-decision:SF-2026-ARXIV-2606-18673; analysis-decision:SF-2026-ARXIV-2606-18697; analysis-decision:SF-2026-ARXIV-2606-18741; analysis-decision:SF-2026-ARXIV-2606-18746; analysis-decision:SF-2026-ARXIV-2606-18810; analysis-decision:SF-2026-ARXIV-2606-18829; analysis-decision:SF-2026-ARXIV-2606-18831; analysis-decision:SF-2026-ARXIV-2606-18847; analysis-decision:SF-2026-ARXIV-2606-18874; analysis-decision:SF-2026-ARXIV-2606-18958; analysis-decision:SF-2026-ARXIV-2606-18967; analysis-decision:SF-2026-ARXIV-2606-18996; analysis-decision:SF-2026-ARXIV-2606-19004; analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP; analysis-decision:SF-2026-ARXIV-2606-19057; analysis-decision:SF-2026-ARXIV-2606-19111; analysis-decision:SF-2026-ARXIV-2606-19191; analysis-decision:SF-2026-ARXIV-2606-19242; analysis-decision:SF-2026-ARXIV-2606-19262; analysis-decision:SF-2026-ARXIV-2606-19271; analysis-decision:SF-2026-ARXIV-2606-19409; analysis-decision:SF-2026-ARXIV-2606-19464; analysis:DA-20260618-PLATFORM-BOUND-ARTIFACT; analysis-decision:SF-2026-ARXIV-2606-19544; analysis-decision:SF-2026-ARXIV-2606-19559; analysis-decision:SF-2026-ARXIV-2606-19595; analysis-decision:SF-2026-ARXIV-2606-19613; analysis-decision:SF-2026-ARXIV-2606-19667; analysis-decision:SF-2026-ARXIV-2606-20736; analysis-decision:SF-2026-ARXIV-2606-20746; analysis-decision:SF-2026-ARXIV-2606-21089; analysis-decision:SF-2026-ARXIV-2606-21090; analysis-decision:SF-2026-ARXIV-2606-28374 | — | 37/37 frontier; winners frozen before source-specific rationale | passed |
| SA-20260618-BOOKS-POSTWRITE-V1 | fresh-context:jun18-v1 | books | books-review:SF-2026-ARXIV-2606-18600; books-review:SF-2026-ARXIV-2606-18619; books-review:SF-2026-ARXIV-2606-18650; books-review:SF-2026-ARXIV-2606-18668; books-review:SF-2026-ARXIV-2606-18673; books-review:SF-2026-ARXIV-2606-18697; books-review:SF-2026-ARXIV-2606-18741; books-review:SF-2026-ARXIV-2606-18746; books-review:SF-2026-ARXIV-2606-18810; books-review:SF-2026-ARXIV-2606-18829; books-review:SF-2026-ARXIV-2606-18831; books-review:SF-2026-ARXIV-2606-18847; books-review:SF-2026-ARXIV-2606-18874; books-review:SF-2026-ARXIV-2606-18958; books-review:SF-2026-ARXIV-2606-18967; books-review:SF-2026-ARXIV-2606-18996; books-review:SF-2026-ARXIV-2606-19004; books-review:SF-2026-ARXIV-2606-19025; books-review:SF-2026-ARXIV-2606-19057; books-review:SF-2026-ARXIV-2606-19111; books-review:SF-2026-ARXIV-2606-19191; books-review:SF-2026-ARXIV-2606-19242; books-review:SF-2026-ARXIV-2606-19262; books-review:SF-2026-ARXIV-2606-19271; books-review:SF-2026-ARXIV-2606-19409; books-review:SF-2026-ARXIV-2606-19464; books-review:SF-2026-ARXIV-2606-19535; books-review:SF-2026-ARXIV-2606-19544; books-review:SF-2026-ARXIV-2606-19559; books-review:SF-2026-ARXIV-2606-19595; books-review:SF-2026-ARXIV-2606-19613; books-review:SF-2026-ARXIV-2606-19667; books-review:SF-2026-ARXIV-2606-20736; books-review:SF-2026-ARXIV-2606-20746; books-review:SF-2026-ARXIV-2606-21089; books-review:SF-2026-ARXIV-2606-21090; books-review:SF-2026-ARXIV-2606-28374 | — | 16/16 Integrate正文、Review note、unique owner、old-path/coexistence/fallback；21/21 No Change existing coverage and leakage audit | passed |

### Materials and Access

- 37/37 exact-v1 official HTML pages were accessible and exposed the matching version body.
- Local curl reset; the working primary-source web reader supplied the official exact-v1 manuscripts.

## 8. Ignored Noise

- 479 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit rather than being promoted into the Candidate Ledger.

## 9. Recommended Action

- Integrate: 16; No Change: 21.
- Books Gate Passed: 16 Integrate families were audited in 11 unique owners; 21 No Change handoffs retain existing coverage without writeback leakage.

## 10. Repository Changes

- Only this date's Daily, source packet and finalizer are written by this lane; shared Books are untouched.

## 11. Open Questions

- How should heterogeneous spot serving decide whether migration, replication or recomputation is the safest recovery path under simultaneous price and topology change?
- Which cross-site MoE ownership policy remains stable when expert popularity and WAN availability drift together?
- How should executable model identity bind weights, adapters, kernels, hardware and serving build without making routine upgrades impossible?
- These are research continuations, not unresolved Gate findings.

## 12. Sources

- [arXiv:2606.18600v1 — ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/html/2606.18600v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18600`。
- [arXiv:2606.18619v1 — Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/html/2606.18619v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18619`。
- [arXiv:2606.18650v1 — BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](https://arxiv.org/html/2606.18650v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18650`。
- [arXiv:2606.18668v1 — EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems](https://arxiv.org/html/2606.18668v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18668`。
- [arXiv:2606.18673v1 — Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications](https://arxiv.org/html/2606.18673v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18673`。
- [arXiv:2606.18697v1 — Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/html/2606.18697v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18697`。
- [arXiv:2606.18741v1 — ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/html/2606.18741v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18741`。
- [arXiv:2606.18746v1 — What Must Generalist Agents Remember?](https://arxiv.org/html/2606.18746v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18746`。
- [arXiv:2606.18810v1 — Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/html/2606.18810v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18810`。
- [arXiv:2606.18829v1 — GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](https://arxiv.org/html/2606.18829v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18829`。
- [arXiv:2606.18831v1 — Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning](https://arxiv.org/html/2606.18831v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18831`。
- [arXiv:2606.18847v1 — WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](https://arxiv.org/html/2606.18847v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18847`。
- [arXiv:2606.18874v1 — Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness](https://arxiv.org/html/2606.18874v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18874`。
- [arXiv:2606.18958v1 — LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation](https://arxiv.org/html/2606.18958v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18958`。
- [arXiv:2606.18967v1 — EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/html/2606.18967v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18967`。
- [arXiv:2606.18996v1 — TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction](https://arxiv.org/html/2606.18996v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-18996`。
- [arXiv:2606.19004v1 — Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training](https://arxiv.org/html/2606.19004v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19004`。
- [arXiv:2606.19025v1 — FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs](https://arxiv.org/html/2606.19025v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19025`。
- [arXiv:2606.19057v1 — Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning](https://arxiv.org/html/2606.19057v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19057`。
- [arXiv:2606.19111v1 — Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams](https://arxiv.org/html/2606.19111v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19111`。
- [arXiv:2606.19191v1 — PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems](https://arxiv.org/html/2606.19191v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19191`。
- [arXiv:2606.19242v1 — Runtime Compliance Verification for AI Agents](https://arxiv.org/html/2606.19242v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19242`。
- [arXiv:2606.19262v1 — Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/html/2606.19262v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19262`。
- [arXiv:2606.19271v1 — TurboServe: Serving Streaming Video Generation Efficiently and Economically](https://arxiv.org/html/2606.19271v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19271`。
- [arXiv:2606.19409v1 — OpenRath: Session-Centered Runtime State for Agent Systems](https://arxiv.org/html/2606.19409v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19409`。
- [arXiv:2606.19464v1 — Deontic Policies for Runtime Governance of Agentic AI Systems](https://arxiv.org/html/2606.19464v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19464`。
- [arXiv:2606.19535v1 — FloatDoor: Platform-Triggered Backdoors in LLMs](https://arxiv.org/html/2606.19535v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19535`。
- [arXiv:2606.19544v1 — Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models Across Agreement, Consistency, and Bias](https://arxiv.org/html/2606.19544v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19544`。
- [arXiv:2606.19559v1 — Uncertainty Decomposition for Clarification Seeking in LLM Agents](https://arxiv.org/html/2606.19559v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19559`。
- [arXiv:2606.19595v1 — IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows](https://arxiv.org/html/2606.19595v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19595`。
- [arXiv:2606.19613v1 — StaminaBench: Stress-Testing Coding Agents over 100 Interaction Turns](https://arxiv.org/html/2606.19613v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19613`。
- [arXiv:2606.19667v1 — CacheWeaver: Cache-Aware Evidence Ordering for Efficient Grounded RAG Inference](https://arxiv.org/html/2606.19667v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-19667`。
- [arXiv:2606.20736v1 — REKEY: Metadata-Grounded Visual-Key Regeneration for Contamination-Resilient VQA Evaluation](https://arxiv.org/html/2606.20736v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-20736`。
- [arXiv:2606.20746v1 — Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection](https://arxiv.org/html/2606.20746v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-20746`。
- [arXiv:2606.21089v1 — Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines](https://arxiv.org/html/2606.21089v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-21089`。
- [arXiv:2606.21090v1 — Self-Improvement Can Self-Regress: The Rise-and-Collapse Failure Mode of LLM Self-Training](https://arxiv.org/html/2606.21090v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-21090`。
- [arXiv:2606.28374v1 — Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/html/2606.28374v1) — first-public `2026-06-17`；accessed `2026-08-29`；Source Family `SF-2026-ARXIV-2606-28374`。
- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。

## 13. Final Status

- Status: Complete.
- Coverage Gate: Closed.
- Evidence Gate: Passed.
- Books Gate: Passed.
- Fresh-context Semantic Audit: Passed；unresolved findings = 0.
