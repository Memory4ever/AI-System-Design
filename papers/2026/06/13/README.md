# Daily Research — 2026-06-13

**Research Date:** 2026-06-13

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-12 09:00:00 ～ 2026-06-13 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 已通过

## Executive Summary

The Beijing window contains 434 registered arXiv identities. Full 434/434 title+abstract semantic screening freezes 38 durable AI-system families and 396 row-specific closures. The 80 route-negative identities were all reviewed and closed. `2606.15007v1` is a historical-owner closure because NVIDIA's primary release preceded this window on 2026-06-04. Official exact-v1 HTML was reviewed for 38/38 retained families. Full-frontier selection froze three winners before source-specific rationale. Books comparison yields 14 Integrate proposals, owner-merged into 9 writes, and 24 No Change handoffs; root writeback and the 38/38 post-write audit passed.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-13 |
| Window End | 2026-06-13 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260613-706d27bb |
| Denominator Frozen At | 2026-08-30T00:45:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-12T09:00:00+08:00 | 2026-06-13T09:00:00+08:00 | 2026-08-30T00:45:00+08:00 | Frozen DataCite DOI-prefix snapshots; exact v1 UTC window; all registered categories | checked | 434 | SF-2026-ARXIV-2606-14027; SF-2026-ARXIV-2606-14106; SF-2026-ARXIV-2606-14130; SF-2026-ARXIV-2606-14154; SF-2026-ARXIV-2606-14179; SF-2026-ARXIV-2606-14200; SF-2026-ARXIV-2606-14239; SF-2026-ARXIV-2606-14249; SF-2026-ARXIV-2606-14275; SF-2026-ARXIV-2606-14350; SF-2026-ARXIV-2606-14356; SF-2026-ARXIV-2606-14445; SF-2026-ARXIV-2606-14470; SF-2026-ARXIV-2606-14474; SF-2026-ARXIV-2606-14516; SF-2026-ARXIV-2606-14517; SF-2026-ARXIV-2606-14518; SF-2026-ARXIV-2606-14571; SF-2026-ARXIV-2606-14574; SF-2026-ARXIV-2606-14589; SF-2026-ARXIV-2606-14598; SF-2026-ARXIV-2606-14620; SF-2026-ARXIV-2606-14629; SF-2026-ARXIV-2606-14672; SF-2026-ARXIV-2606-14674; SF-2026-ARXIV-2606-14832; SF-2026-ARXIV-2606-14885; SF-2026-ARXIV-2606-14945; SF-2026-ARXIV-2606-15004; SF-2026-ARXIV-2606-15008; SF-2026-ARXIV-2606-15017; SF-2026-ARXIV-2606-15020; SF-2026-ARXIV-2606-15029; SF-2026-ARXIV-2606-15034; SF-2026-ARXIV-2606-17090; SF-2026-ARXIV-2606-19376; SF-2026-ARXIV-2606-20668; SF-2026-ARXIV-2606-24898 | pages=40; final_cursor=end; 40 disjoint 2606.00–.39 prefix snapshots; 434 unique registered identities | 2026-06-13T01:00:00Z | ../_sources/daily-20260613/screening-ledger.json; ../_sources/daily-20260613/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260613 | — |

<!-- coverage:SRC-ARXIV:20260613:start -->
All 311 Core, 43 keyword-routed non-Core, and 80 route-negative identities were semantically screened. Frozen arithmetic: `434 = 38 retained + 396 closures`; route-negative audit: `80 = 0 retained + 80 closures`. Keyword routes were recall aids only. The 2606.15007 arXiv row is a historical-first-public closure, not a new family owner.
<!-- coverage:SRC-ARXIV:20260613:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-14027 | arXiv:2606.14027v1 | paper-v1:2606.14027 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14027 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-14027 | yes |
| SF-2026-ARXIV-2606-14106 | arXiv:2606.14106v1 | paper-v1:2606.14106 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14106 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-14106 | yes |
| SF-2026-ARXIV-2606-14130 | arXiv:2606.14130v1 | paper-v1:2606.14130 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14130 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14130 | yes |
| SF-2026-ARXIV-2606-14154 | arXiv:2606.14154v1 | paper-v1:2606.14154 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14154 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-14154 | yes |
| SF-2026-ARXIV-2606-14179 | arXiv:2606.14179v1 | paper-v1:2606.14179 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14179 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14179 | yes |
| SF-2026-ARXIV-2606-14200 | arXiv:2606.14200v1 | paper-v1:2606.14200 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14200 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-14200 | yes |
| SF-2026-ARXIV-2606-14239 | arXiv:2606.14239v1 | paper-v1:2606.14239 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14239 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14239 | yes |
| SF-2026-ARXIV-2606-14249 | arXiv:2606.14249v1 | paper-v1:2606.14249 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14249 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14249 | yes |
| SF-2026-ARXIV-2606-14275 | arXiv:2606.14275v1 | paper-v1:2606.14275 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14275 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-14275 | yes |
| SF-2026-ARXIV-2606-14350 | arXiv:2606.14350v1 | paper-v1:2606.14350 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14350 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14350 | yes |
| SF-2026-ARXIV-2606-14356 | arXiv:2606.14356v1 | paper-v1:2606.14356 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14356 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14356 | yes |
| SF-2026-ARXIV-2606-14445 | arXiv:2606.14445v1 | paper-v1:2606.14445 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14445 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14445 | yes |
| SF-2026-ARXIV-2606-14470 | arXiv:2606.14470v1 | paper-v1:2606.14470 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14470 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14470 | yes |
| SF-2026-ARXIV-2606-14474 | arXiv:2606.14474v1 | paper-v1:2606.14474 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14474 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14474 | yes |
| SF-2026-ARXIV-2606-14516 | arXiv:2606.14516v1 | paper-v1:2606.14516 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14516 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14516 | yes |
| SF-2026-ARXIV-2606-14517 | arXiv:2606.14517v1 | paper-v1:2606.14517 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14517 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-14517 | yes |
| SF-2026-ARXIV-2606-14518 | arXiv:2606.14518v1 | paper-v1:2606.14518 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14518 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-14518 | yes |
| SF-2026-ARXIV-2606-14571 | arXiv:2606.14571v1 | paper-v1:2606.14571 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14571 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14571 | yes |
| SF-2026-ARXIV-2606-14574 | arXiv:2606.14574v1 | paper-v1:2606.14574 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14574 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-14574 | yes |
| SF-2026-ARXIV-2606-14589 | arXiv:2606.14589v1 | paper-v1:2606.14589 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14589 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-14589 | yes |
| SF-2026-ARXIV-2606-14598 | arXiv:2606.14598v1 | paper-v1:2606.14598 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14598 | self | — | new_in_window | INFER-VLLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14598 | yes |
| SF-2026-ARXIV-2606-14620 | arXiv:2606.14620v1 | paper-v1:2606.14620 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14620 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14620 | yes |
| SF-2026-ARXIV-2606-14629 | arXiv:2606.14629v1 | paper-v1:2606.14629 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14629 | self | — | new_in_window | AGENT-REFLECTION | Integrate | books-review:SF-2026-ARXIV-2606-14629 | yes |
| SF-2026-ARXIV-2606-14672 | arXiv:2606.14672v1 | paper-v1:2606.14672 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14672 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14672 | yes |
| SF-2026-ARXIV-2606-14674 | arXiv:2606.14674v1 | paper-v1:2606.14674 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14674 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14674 | yes |
| SF-2026-ARXIV-2606-14832 | arXiv:2606.14832v1 | paper-v1:2606.14832 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14832 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14832 | yes |
| SF-2026-ARXIV-2606-14885 | arXiv:2606.14885v1 | paper-v1:2606.14885 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14885 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2606-14885 | yes |
| SF-2026-ARXIV-2606-14945 | arXiv:2606.14945v1 | paper-v1:2606.14945 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-14945 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14945 | yes |
| SF-2026-ARXIV-2606-15004 | arXiv:2606.15004v1 | paper-v1:2606.15004 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15004 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15004 | yes |
| SF-2026-ARXIV-2606-15008 | arXiv:2606.15008v1 | paper-v1:2606.15008 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15008 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15008 | yes |
| SF-2026-ARXIV-2606-15017 | arXiv:2606.15017v1 | paper-v1:2606.15017 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15017 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15017 | yes |
| SF-2026-ARXIV-2606-15020 | arXiv:2606.15020v1 | paper-v1:2606.15020 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15020 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-15020 | yes |
| SF-2026-ARXIV-2606-15029 | arXiv:2606.15029v1 | paper-v1:2606.15029 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15029 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15029 | yes |
| SF-2026-ARXIV-2606-15034 | arXiv:2606.15034v1 | paper-v1:2606.15034 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-15034 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15034 | yes |
| SF-2026-ARXIV-2606-17090 | arXiv:2606.17090v1 | paper-v1:2606.17090 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-17090 | self | — | new_in_window | INFER-VLLM | Integrate | books-review:SF-2026-ARXIV-2606-17090 | yes |
| SF-2026-ARXIV-2606-19376 | arXiv:2606.19376v1 | paper-v1:2606.19376 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19376 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19376 | yes |
| SF-2026-ARXIV-2606-20668 | arXiv:2606.20668v1 | paper-v1:2606.20668 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-20668 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20668 | yes |
| SF-2026-ARXIV-2606-24898 | arXiv:2606.24898v1 | paper-v1:2606.24898 | 2026-W24 | 2026-06-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24898 | self | — | new_in_window | MODEL-DECODER-ONLY | Integrate | books-review:SF-2026-ARXIV-2606-24898 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-14027 | RP-a8e9e6d1d7413752 | deep | arXiv:2606.14027v1 | SRC-ARXIV@arXiv:2606.14027v1 | https://arxiv.org/html/2606.14027v1 — § exact-v1 anchor: SOPGuard | https://arxiv.org/html/2606.14027v1 — § exact-v1 evaluation anchor: SOPBench | https://arxiv.org/html/2606.14027v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14027 | complete |
| SF-2026-ARXIV-2606-14106 | RP-7f266bf4f0153211 | deep | arXiv:2606.14106v1 | SRC-ARXIV@arXiv:2606.14106v1 | https://arxiv.org/html/2606.14106v1 — § exact-v1 anchor: 3 AGMem: mitigating the side effects of visual memory | https://arxiv.org/html/2606.14106v1 — § exact-v1 evaluation anchor: 4 AGMem experiments | https://arxiv.org/html/2606.14106v1 — § exact-v1 limitation/counterevidence anchor: 7 Conclusion and discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14106 | complete |
| SF-2026-ARXIV-2606-14130 | RP-31d2aa928e494141 | deep | arXiv:2606.14130v1 | SRC-ARXIV@arXiv:2606.14130v1 | https://arxiv.org/html/2606.14130v1 — § exact-v1 anchor: Contract Shielding | https://arxiv.org/html/2606.14130v1 — § exact-v1 evaluation anchor: Empirical Evaluation | https://arxiv.org/html/2606.14130v1 — § exact-v1 limitation/counterevidence anchor: Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14130 | complete |
| SF-2026-ARXIV-2606-14154 | RP-e07a101d032916cf | deep | arXiv:2606.14154v1 | SRC-ARXIV@arXiv:2606.14154v1 | https://arxiv.org/html/2606.14154v1 — § exact-v1 anchor: SkillMutator | https://arxiv.org/html/2606.14154v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.14154v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14154 | complete |
| SF-2026-ARXIV-2606-14179 | RP-37bc73053a546c48 | deep | arXiv:2606.14179v1 | SRC-ARXIV@arXiv:2606.14179v1 | https://arxiv.org/html/2606.14179v1 — § exact-v1 anchor: CacheAgentLoop | https://arxiv.org/html/2606.14179v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.14179v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14179 | complete |
| SF-2026-ARXIV-2606-14200 | RP-6436a6594f29ba37 | deep | arXiv:2606.14200v1 | SRC-ARXIV@arXiv:2606.14200v1 | https://arxiv.org/html/2606.14200v1 — § exact-v1 anchor: skill-conditional reputation | https://arxiv.org/html/2606.14200v1 — § exact-v1 evaluation anchor: AppWorld | https://arxiv.org/html/2606.14200v1 — § exact-v1 limitation/counterevidence anchor: not Sybil-resistant | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14200 | complete |
| SF-2026-ARXIV-2606-14239 | RP-9582c277fc0cd9c3 | deep | arXiv:2606.14239v1 | SRC-ARXIV@arXiv:2606.14239v1 | https://arxiv.org/html/2606.14239v1 — § exact-v1 anchor: paired trajectory auditing | https://arxiv.org/html/2606.14239v1 — § exact-v1 evaluation anchor: 89 containerized tasks | https://arxiv.org/html/2606.14239v1 — § exact-v1 limitation/counterevidence anchor: observable structure | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14239 | complete |
| SF-2026-ARXIV-2606-14249 | RP-8a3d71bc4c826e9b | deep | arXiv:2606.14249v1 | SRC-ARXIV@arXiv:2606.14249v1 | https://arxiv.org/html/2606.14249v1 — § exact-v1 anchor: Harness Composition | https://arxiv.org/html/2606.14249v1 — § exact-v1 evaluation anchor: 15 model-benchmark configurations | https://arxiv.org/html/2606.14249v1 — § exact-v1 limitation/counterevidence anchor: 7.7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14249 | complete |
| SF-2026-ARXIV-2606-14275 | RP-dd45c7fe2453d3ae | deep | arXiv:2606.14275v1 | SRC-ARXIV@arXiv:2606.14275v1 | https://arxiv.org/html/2606.14275v1 — § exact-v1 anchor: path-indexed key-value storage | https://arxiv.org/html/2606.14275v1 — § exact-v1 evaluation anchor: AuthTrace | https://arxiv.org/html/2606.14275v1 — § exact-v1 limitation/counterevidence anchor: concurrent offline rewrites | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14275 | complete |
| SF-2026-ARXIV-2606-14350 | RP-0c3be2abb0bd4d09 | deep | arXiv:2606.14350v1 | SRC-ARXIV@arXiv:2606.14350v1 | https://arxiv.org/html/2606.14350v1 — § exact-v1 anchor: workflow topology | https://arxiv.org/html/2606.14350v1 — § exact-v1 evaluation anchor: 3 case studies | https://arxiv.org/html/2606.14350v1 — § exact-v1 limitation/counterevidence anchor: open challenges | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14350 | complete |
| SF-2026-ARXIV-2606-14356 | RP-64e0d46d4e1bd3a5 | deep | arXiv:2606.14356v1 | SRC-ARXIV@arXiv:2606.14356v1 | https://arxiv.org/html/2606.14356v1 — § exact-v1 anchor: CAIM Task and Data Contracts | https://arxiv.org/html/2606.14356v1 — § exact-v1 evaluation anchor: two workflows | https://arxiv.org/html/2606.14356v1 — § exact-v1 limitation/counterevidence anchor: resource gap | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14356 | complete |
| SF-2026-ARXIV-2606-14445 | RP-705df1b2191cccb8 | deep | arXiv:2606.14445v1 | SRC-ARXIV@arXiv:2606.14445v1 | https://arxiv.org/html/2606.14445v1 — § exact-v1 anchor: file-based protocol | https://arxiv.org/html/2606.14445v1 — § exact-v1 evaluation anchor: 27-day | https://arxiv.org/html/2606.14445v1 — § exact-v1 limitation/counterevidence anchor: observational | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14445 | complete |
| SF-2026-ARXIV-2606-14470 | RP-68cd5fc8f6e1615f | deep | arXiv:2606.14470v1 | SRC-ARXIV@arXiv:2606.14470v1 | https://arxiv.org/html/2606.14470v1 — § exact-v1 anchor: every scored thought is a commit | https://arxiv.org/html/2606.14470v1 — § exact-v1 evaluation anchor: 7 All Experiments at a Glance | https://arxiv.org/html/2606.14470v1 — § exact-v1 limitation/counterevidence anchor: 8 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14470 | complete |
| SF-2026-ARXIV-2606-14474 | RP-633b82597ad15fca | deep | arXiv:2606.14474v1 | SRC-ARXIV@arXiv:2606.14474v1 | https://arxiv.org/html/2606.14474v1 — § exact-v1 anchor: seven auditable components | https://arxiv.org/html/2606.14474v1 — § exact-v1 evaluation anchor: two hands-on mini-labs | https://arxiv.org/html/2606.14474v1 — § exact-v1 limitation/counterevidence anchor: diagnostic discrepancy analysis from statistical validation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14474 | complete |
| SF-2026-ARXIV-2606-14516 | RP-fa458ad381ee7b27 | deep | arXiv:2606.14516v1 | SRC-ARXIV@arXiv:2606.14516v1 | https://arxiv.org/html/2606.14516v1 — § exact-v1 anchor: 3 The Every Eval Ever Schema | https://arxiv.org/html/2606.14516v1 — § exact-v1 evaluation anchor: 7 Case Studies | https://arxiv.org/html/2606.14516v1 — § exact-v1 limitation/counterevidence anchor: 8 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14516 | complete |
| SF-2026-ARXIV-2606-14517 | RP-2a2838c4315159d2 | deep | arXiv:2606.14517v1 | SRC-ARXIV@arXiv:2606.14517v1 | https://arxiv.org/html/2606.14517v1 — § exact-v1 anchor: beam-search optimization framework | https://arxiv.org/html/2606.14517v1 — § exact-v1 evaluation anchor: end-to-end real-world agent deployments | https://arxiv.org/html/2606.14517v1 — § exact-v1 limitation/counterevidence anchor: cost-bounded | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14517 | complete |
| SF-2026-ARXIV-2606-14518 | RP-5152d2ff3568f951 | deep | arXiv:2606.14518v1 | SRC-ARXIV@arXiv:2606.14518v1 | https://arxiv.org/html/2606.14518v1 — § exact-v1 anchor: information-theoretic proof | https://arxiv.org/html/2606.14518v1 — § exact-v1 evaluation anchor: empirical results on convex models | https://arxiv.org/html/2606.14518v1 — § exact-v1 limitation/counterevidence anchor: privacy-audit tradeoff | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14518 | complete |
| SF-2026-ARXIV-2606-14571 | RP-e579ee768695e1c3 | deep | arXiv:2606.14571v1 | SRC-ARXIV@arXiv:2606.14571v1 | https://arxiv.org/html/2606.14571v1 — § exact-v1 anchor: two-step task sequence | https://arxiv.org/html/2606.14571v1 — § exact-v1 evaluation anchor: eight memory systems across two backbones | https://arxiv.org/html/2606.14571v1 — § exact-v1 limitation/counterevidence anchor: stored or feedback incorporated locally | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14571 | complete |
| SF-2026-ARXIV-2606-14574 | RP-12013f2b340db397 | deep | arXiv:2606.14574v1 | SRC-ARXIV@arXiv:2606.14574v1 | https://arxiv.org/html/2606.14574v1 — § exact-v1 anchor: state machine executor | https://arxiv.org/html/2606.14574v1 — § exact-v1 evaluation anchor: six LLMs | https://arxiv.org/html/2606.14574v1 — § exact-v1 limitation/counterevidence anchor: human-curated symbolic world model | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14574 | complete |
| SF-2026-ARXIV-2606-14589 | RP-708728764810d186 | deep | arXiv:2606.14589v1 | SRC-ARXIV@arXiv:2606.14589v1 | https://arxiv.org/html/2606.14589v1 — § exact-v1 anchor: five-class mechanism-oriented taxonomy | https://arxiv.org/html/2606.14589v1 — § exact-v1 evaluation anchor: 22 incidents | https://arxiv.org/html/2606.14589v1 — § exact-v1 limitation/counterevidence anchor: single production runtime | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14589 | complete |
| SF-2026-ARXIV-2606-14598 | RP-bb900e8fb696e194 | deep | arXiv:2606.14598v1 | SRC-ARXIV@arXiv:2606.14598v1 | https://arxiv.org/html/2606.14598v1 — § exact-v1 anchor: fused Triton INT8 GEMM | https://arxiv.org/html/2606.14598v1 — § exact-v1 evaluation anchor: RTX 3090 | https://arxiv.org/html/2606.14598v1 — § exact-v1 limitation/counterevidence anchor: honest deployment map | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14598 | complete |
| SF-2026-ARXIV-2606-14620 | RP-3792966caca6ae76 | deep | arXiv:2606.14620v1 | SRC-ARXIV@arXiv:2606.14620v1 | https://arxiv.org/html/2606.14620v1 — § exact-v1 anchor: sampler accept step | https://arxiv.org/html/2606.14620v1 — § exact-v1 evaluation anchor: 686-prompt | https://arxiv.org/html/2606.14620v1 — § exact-v1 limitation/counterevidence anchor: regime-dependent | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14620 | complete |
| SF-2026-ARXIV-2606-14629 | RP-b846026d165b9c61 | deep | arXiv:2606.14629v1 | SRC-ARXIV@arXiv:2606.14629v1 | https://arxiv.org/html/2606.14629v1 — § exact-v1 anchor: 2 Production setup | https://arxiv.org/html/2606.14629v1 — § exact-v1 evaluation anchor: 3 Headline finding: silent failure on MMMU | https://arxiv.org/html/2606.14629v1 — § exact-v1 limitation/counterevidence anchor: 6 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14629 | complete |
| SF-2026-ARXIV-2606-14672 | RP-4524144d956a44be | deep | arXiv:2606.14672v1 | SRC-ARXIV@arXiv:2606.14672v1 | https://arxiv.org/html/2606.14672v1 — § exact-v1 anchor: 3 Methodology | https://arxiv.org/html/2606.14672v1 — § exact-v1 evaluation anchor: 4 Experiments | https://arxiv.org/html/2606.14672v1 — § exact-v1 limitation/counterevidence anchor: 6 Conclusion and Future Direction | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14672 | complete |
| SF-2026-ARXIV-2606-14674 | RP-a7bc715dcda676d8 | deep | arXiv:2606.14674v1 | SRC-ARXIV@arXiv:2606.14674v1 | https://arxiv.org/html/2606.14674v1 — § exact-v1 anchor: AgentSpec | https://arxiv.org/html/2606.14674v1 — § exact-v1 evaluation anchor: DeliveryBench | https://arxiv.org/html/2606.14674v1 — § exact-v1 limitation/counterevidence anchor: scaffold compatibility | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14674 | complete |
| SF-2026-ARXIV-2606-14832 | RP-5090ad20c00b101c | deep | arXiv:2606.14832v1 | SRC-ARXIV@arXiv:2606.14832v1 | https://arxiv.org/html/2606.14832v1 — § exact-v1 anchor: PhoneHarness | https://arxiv.org/html/2606.14832v1 — § exact-v1 evaluation anchor: annotated evaluation split | https://arxiv.org/html/2606.14832v1 — § exact-v1 limitation/counterevidence anchor: mixed phone workflows | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14832 | complete |
| SF-2026-ARXIV-2606-14885 | RP-f23e2313d249b64f | deep | arXiv:2606.14885v1 | SRC-ARXIV@arXiv:2606.14885v1 | https://arxiv.org/html/2606.14885v1 — § exact-v1 anchor: dynamic workspace expansion | https://arxiv.org/html/2606.14885v1 — § exact-v1 evaluation anchor: Browsecomp-Plus | https://arxiv.org/html/2606.14885v1 — § exact-v1 limitation/counterevidence anchor: retriever-level recall | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14885 | complete |
| SF-2026-ARXIV-2606-14945 | RP-843331dba8648664 | deep | arXiv:2606.14945v1 | SRC-ARXIV@arXiv:2606.14945v1 | https://arxiv.org/html/2606.14945v1 — § exact-v1 anchor: stateful ReAct agent | https://arxiv.org/html/2606.14945v1 — § exact-v1 evaluation anchor: two benchmarks | https://arxiv.org/html/2606.14945v1 — § exact-v1 limitation/counterevidence anchor: fixed-size conversation window | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-14945 | complete |
| SF-2026-ARXIV-2606-15004 | RP-f8d3c5b059210af0 | deep | arXiv:2606.15004v1 | SRC-ARXIV@arXiv:2606.15004v1 | https://arxiv.org/html/2606.15004v1 — § exact-v1 anchor: CREST | https://arxiv.org/html/2606.15004v1 — § exact-v1 evaluation anchor: three Arm Cortex-M targets | https://arxiv.org/html/2606.15004v1 — § exact-v1 limitation/counterevidence anchor: cross-board replay | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15004 | complete |
| SF-2026-ARXIV-2606-15008 | RP-03dec85d54f51201 | deep | arXiv:2606.15008v1 | SRC-ARXIV@arXiv:2606.15008v1 | https://arxiv.org/html/2606.15008v1 — § exact-v1 anchor: III Methodology | https://arxiv.org/html/2606.15008v1 — § exact-v1 evaluation anchor: V Empirical Security Analysis | https://arxiv.org/html/2606.15008v1 — § exact-v1 limitation/counterevidence anchor: VIII Threats to Validity; IX Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15008 | complete |
| SF-2026-ARXIV-2606-15017 | RP-290f0f85e6de5c0a | deep | arXiv:2606.15017v1 | SRC-ARXIV@arXiv:2606.15017v1 | https://arxiv.org/html/2606.15017v1 — § exact-v1 anchor: budget-matched vanilla baseline | https://arxiv.org/html/2606.15017v1 — § exact-v1 evaluation anchor: three WebArena domains | https://arxiv.org/html/2606.15017v1 — § exact-v1 limitation/counterevidence anchor: run-to-run variance | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15017 | complete |
| SF-2026-ARXIV-2606-15020 | RP-20cd6ee259af2b34 | deep | arXiv:2606.15020v1 | SRC-ARXIV@arXiv:2606.15020v1 | https://arxiv.org/html/2606.15020v1 — § exact-v1 anchor: 25 extraction gaps | https://arxiv.org/html/2606.15020v1 — § exact-v1 evaluation anchor: 16 PDF processing stacks | https://arxiv.org/html/2606.15020v1 — § exact-v1 limitation/counterevidence anchor: dual-view consistency | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15020 | complete |
| SF-2026-ARXIV-2606-15029 | RP-df9a5e401e5f59d4 | deep | arXiv:2606.15029v1 | SRC-ARXIV@arXiv:2606.15029v1 | https://arxiv.org/html/2606.15029v1 — § exact-v1 anchor: Metric Match | https://arxiv.org/html/2606.15029v1 — § exact-v1 evaluation anchor: 15 datasets | https://arxiv.org/html/2606.15029v1 — § exact-v1 limitation/counterevidence anchor: limited annotations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15029 | complete |
| SF-2026-ARXIV-2606-15034 | RP-cc92e98bd46eedea | deep | arXiv:2606.15034v1 | SRC-ARXIV@arXiv:2606.15034v1 | https://arxiv.org/html/2606.15034v1 — § exact-v1 anchor: OSGuard | https://arxiv.org/html/2606.15034v1 — § exact-v1 evaluation anchor: risk-augmented execution suite | https://arxiv.org/html/2606.15034v1 — § exact-v1 limitation/counterevidence anchor: local oversight and end-to-end safety | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-15034 | complete |
| SF-2026-ARXIV-2606-17090 | RP-374cad35a8bd0cf0 | deep | arXiv:2606.17090v1 | SRC-ARXIV@arXiv:2606.17090v1 | https://arxiv.org/html/2606.17090v1 — § exact-v1 anchor: lazy tensor graph | https://arxiv.org/html/2606.17090v1 — § exact-v1 evaluation anchor: ResNet-18 forward | https://arxiv.org/html/2606.17090v1 — § exact-v1 limitation/counterevidence anchor: macOS and ANE-compiler version | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-17090 | complete |
| SF-2026-ARXIV-2606-19376 | RP-07d8cc158ffc095c | deep | arXiv:2606.19376v1 | SRC-ARXIV@arXiv:2606.19376v1 | https://arxiv.org/html/2606.19376v1 — § exact-v1 anchor: SLARouter | https://arxiv.org/html/2606.19376v1 — § exact-v1 evaluation anchor: wide range of LLM benchmarks | https://arxiv.org/html/2606.19376v1 — § exact-v1 limitation/counterevidence anchor: sparse one-sided user feedback | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19376 | complete |
| SF-2026-ARXIV-2606-20668 | RP-14f5e9e4784138fb | deep | arXiv:2606.20668v1 | SRC-ARXIV@arXiv:2606.20668v1 | https://arxiv.org/html/2606.20668v1 — § exact-v1 anchor: BELLS-O | https://arxiv.org/html/2606.20668v1 — § exact-v1 evaluation anchor: 28 systems from 17 providers | https://arxiv.org/html/2606.20668v1 — § exact-v1 limitation/counterevidence anchor: use-case-dependent tradeoffs | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-20668 | complete |
| SF-2026-ARXIV-2606-24898 | RP-247046f613f95f9c | deep | arXiv:2606.24898v1 | SRC-ARXIV@arXiv:2606.24898v1 | https://arxiv.org/html/2606.24898v1 — § exact-v1 anchor: readout blind spot | https://arxiv.org/html/2606.24898v1 — § exact-v1 evaluation anchor: 44M and 129M looped transformers | https://arxiv.org/html/2606.24898v1 — § exact-v1 limitation/counterevidence anchor: without inter-loop normalization | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24898 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-14027:start -->
### 2606.14027 — Same-Origin Policy for Agentic Browsers

**问题与旧路径。** `Agentic browsers integrate autonomous AI agents into web browsers, enabling users to accomplish web tasks through natural-language instructions.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Agentic browser 的 origin policy 必须追踪 agent 读入数据的 origin label，在跨 origin 写入前由浏览器侧 detector 与 user confirmation gate 授权；传统 script-only SOP 不覆盖 agent 自身形成的数据通道。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** SOPBench 覆盖 50 个 source-sink 类别组合、5 个 agentic browsers 与 6 个 backbone LLM；BrowserOS-SOPGuard 报告 0.00 violation rate 与 2.07%–5.79% runtime overhead。 Method locator：`https://arxiv.org/html/2606.14027v1 — § exact-v1 anchor: SOPGuard`。Evaluation locator：`https://arxiv.org/html/2606.14027v1 — § exact-v1 evaluation anchor: SOPBench`。Benchmark identity：model=`Six backbone LLMs in the exact-v1 SOPBench matrix; no single-model aggregate`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`SOP violation rate, paired utility tests, and runtime overhead on SOPBench, Mind2Web, WebArena-Infinity, and REAL`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 合成页面与 BrowserOS 实现不证明任意浏览器、隐式推断数据或用户确认都安全；label propagation 与用户疲劳仍会失效。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14027:start -->
Claim boundary：只使用 `arXiv:2606.14027v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14027:end -->
<!-- review:SF-2026-ARXIV-2606-14027:end -->

<!-- review:SF-2026-ARXIV-2606-14106:start -->
### 2606.14106 — Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents

**问题与旧路径。** `Graphical User Interface (GUI) agents are increasingly used to automate complex computer tasks across applications, websites, and operating systems.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** GUI memory 不应保存整屏即视为更多证据；应把成功动作压缩成 action-relevant crop，并把正常 retrieval 与错误恢复 memory 分开，以避免视觉上下文把 state error 转成 grounding/hidden-operation error。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** OSWorld、WebForge、AgentNetBench 的四类 failure audit；OSWorld/GPT-5.4-mini 上 AGMem 由 full-image memory 的 20.4% 提升到 27.2% accuracy。 Method locator：`https://arxiv.org/html/2606.14106v1 — § exact-v1 anchor: 3 AGMem: mitigating the side effects of visual memory`。Evaluation locator：`https://arxiv.org/html/2606.14106v1 — § exact-v1 evaluation anchor: 4 AGMem experiments`。Benchmark identity：model=`GPT-5.4-mini for the reported OSWorld AGMem result; additional GUI-agent settings remain bound to the exact-v1 matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task accuracy plus state, grounding, hidden-operation, and recovery-failure audit on OSWorld, WebForge, and AgentNetBench`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 裁剪和 recovery detector 都可能遗漏不可见 affordance；三套 GUI benchmark 不证明长期真实桌面 memory 的正确性。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14106:start -->
Claim boundary：只使用 `arXiv:2606.14106v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14106:end -->
<!-- review:SF-2026-ARXIV-2606-14106:end -->

<!-- review:SF-2026-ARXIV-2606-14130:start -->
### 2606.14130 — Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning

**问题与旧路径。** `Safe coordination problems surface in multi-agent reinforcement learning when global safety cannot be enforced by any agent unilaterally: the admissibility of one agent's action may depend on the dynamics of other agents.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 多 Agent shield 可从局部 LTL-safe obligations 通过 circular assume-guarantee fixed point 联合认证，再投影为各 agent action mask；selector 只能在已认证 contract library 中学习选择。 Authoritative owner 是 `AGENT-MULTI-AGENT`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 6 个 environments、15 个 variants；在 AMD EPYC 7702P、203.48 GiB RAM 与单 NVIDIA A16 14.6 GiB 上评估 contract synthesis/selection。 Method locator：`https://arxiv.org/html/2606.14130v1 — § exact-v1 anchor: Contract Shielding`。Evaluation locator：`https://arxiv.org/html/2606.14130v1 — § exact-v1 evaluation anchor: Empirical Evaluation`。Benchmark identity：model=`Environment-specific MARL policies plus certified contract-library selector; no LLM`；hardware=`AMD EPYC 7702P; 203.48 GiB RAM; one NVIDIA A16 with 14.6 GiB`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Safety violations, reward, synthesis cost, and selector behavior across six environments and 15 variants`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 证明只覆盖显式、可表示的模型和 certified library；nonstationary selector 不保证收敛，隐藏状态和环境漂移不在证明内。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14130:start -->
Claim boundary：只使用 `arXiv:2606.14130v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14130:end -->
<!-- review:SF-2026-ARXIV-2606-14130:end -->

<!-- review:SF-2026-ARXIV-2606-14154:start -->
### 2606.14154 — SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills

**问题与旧路径。** `Large language model (LLM) agents increasingly extend their capabilities at runtime by loading Agent Skills, which pair natural-language specifications (SKILL.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Skill supply-chain audit 必须联合读取自然语言 SKILL.md 与可执行 code，因为两种模态可以分别无害、组合后才形成 payload；admission 需覆盖 13 类 cross-modal mutation 与 runtime effect。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 76 个 strongest-attack 样本与跨 Qwen2.5-Coder-7B-Instruct、GPT-4o-mini、GPT-5.4-mini/5.4 的 attack/defense comparison。 Method locator：`https://arxiv.org/html/2606.14154v1 — § exact-v1 anchor: SkillMutator`。Evaluation locator：`https://arxiv.org/html/2606.14154v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark identity：model=`Qwen2.5-Coder-7B-Instruct, GPT-4o-mini, GPT-5.4-mini, and GPT-5.4`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Attack success and defense comparison over 13 cross-modal attack categories and 76 strongest-attack samples`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 自动 mutation 与蒸馏轨迹只覆盖作者 taxonomy；静态 paired reading 仍不能证明运行时无动态依赖或 latent trigger。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14154:start -->
Claim boundary：只使用 `arXiv:2606.14154v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14154:end -->
<!-- review:SF-2026-ARXIV-2606-14154:end -->

<!-- review:SF-2026-ARXIV-2606-14179:start -->
### 2606.14179 — CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward

**问题与旧路径。** `We present CacheRL, a system for training small agent foundation models that achieves 92 percent process accuracy on multi-step tool-calling tasks, approaching GPT-5's 94 percent while requiring 100 times less compute.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 离线 tool-agent RL 可把 rollout 缓存分为精确/模糊/缺失层级，以 token mask 避免把 cache artifact 当 policy action，并让 reward 权重随 cache tier 改变。 Authoritative owner 是 `TRAIN-GRPO`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B-Thinking 迭代 SFT+GRPO；validation reward 0.43→0.78，process accuracy 92%，并以 GPT-5 的 94% 作受限比较。 Method locator：`https://arxiv.org/html/2606.14179v1 — § exact-v1 anchor: CacheAgentLoop`。Evaluation locator：`https://arxiv.org/html/2606.14179v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark identity：model=`Qwen3-4B-Thinking trained with SFT plus GRPO; GPT-5 used only as a bounded process-accuracy comparison`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Validation reward and process accuracy under exact, fuzzy, and missing cache tiers`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 摘要明确报告强 SFT 后 RL 增益有限；fuzzy cache 改变环境反馈，不能替代 live tool execution 或跨 policy probability correction。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14179:start -->
Claim boundary：只使用 `arXiv:2606.14179v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14179:end -->
<!-- review:SF-2026-ARXIV-2606-14179:end -->

<!-- review:SF-2026-ARXIV-2606-14200:start -->
### 2606.14200 — When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms

**问题与旧路径。** `Open platforms increasingly route tasks among heterogeneous LLM agents--differing in base model, scaffold, and tool stack--whose competence varies sharply by skill: an agent excellent at one skill may be useless at another.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。 Authoritative owner 是 `AGENT-MULTI-AGENT`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** AppWorld 的 14-agent heterogeneous pool；攻击实验显示 global routing regret 可从 0 增至 0.94，并评估 zero-evidence gate。 Method locator：`https://arxiv.org/html/2606.14200v1 — § exact-v1 anchor: skill-conditional reputation`。Evaluation locator：`https://arxiv.org/html/2606.14200v1 — § exact-v1 evaluation anchor: AppWorld`。Benchmark identity：model=`Fourteen heterogeneous agents in the AppWorld routing pool; exact backbone identities remain bound to the v1 experiment table`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Routing regret, task outcome, and zero-evidence behavior under skill-conditional and global reputation`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 该机制不具 Sybil resistance，skill ontology 与冷启动证据会漂移；reputation 只能作为 routing sensor，不能认证 identity 或授权 effect。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14200:start -->
Claim boundary：只使用 `arXiv:2606.14200v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14200:end -->
<!-- review:SF-2026-ARXIV-2606-14200:end -->

<!-- review:SF-2026-ARXIV-2606-14239:start -->
### 2606.14239 — SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing

**问题与旧路径。** `Agent skills are structured procedural packages that guide frozen LLM agents in specialized workflows.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Skill evolution 可用同一 task 的 with/without-skill paired trajectory 隔离行为 delta，再让固定 structural verifier gate Refine/Repair 与 rollback。 Authoritative owner 是 `AGENT-WORKFLOW`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 89 个 containerized tasks、8 个 professional domains；不访问 hidden tests、reference solutions 或 external rewards，平均 reward 73.9%。 Method locator：`https://arxiv.org/html/2606.14239v1 — § exact-v1 anchor: paired trajectory auditing`。Evaluation locator：`https://arxiv.org/html/2606.14239v1 — § exact-v1 evaluation anchor: 89 containerized tasks`。Benchmark identity：model=`Skill-evolving coding agents in the exact-v1 paired-run matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Fixed structural verifier and task reward over 89 containerized tasks in eight domains; no hidden tests, reference solutions, or external rewards exposed to the auditor`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 只可观察到的结构约束才能被 verifier 发现；paired runs 仍受模型随机性与 evaluator 共偏影响，不能证明 unobservable correctness。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14239:start -->
Claim boundary：只使用 `arXiv:2606.14239v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14239:end -->
<!-- review:SF-2026-ARXIV-2606-14239:end -->

<!-- review:SF-2026-ARXIV-2606-14249:start -->
### 2606.14249 — HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

**问题与旧路径。** `AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Harness 应表示成 model 与 configuration 的一等组合，生命周期 hooks、singleton slots 与 deterministic gates 共同定义可组合、可演进但可复现的运行身份。 Authoritative owner 是 `AGENT-WORKFLOW`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 5 个 benchmarks、15 个 model-benchmark configurations，并比较九个 harness dimensions 与 AEGIS adaptation。 Method locator：`https://arxiv.org/html/2606.14249v1 — § exact-v1 anchor: Harness Composition`。Evaluation locator：`https://arxiv.org/html/2606.14249v1 — § exact-v1 evaluation anchor: 15 model-benchmark configurations`。Benchmark identity：model=`Fifteen model-benchmark configurations in the exact-v1 HarnessX matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Benchmark score, harness-dimension coverage, composition behavior, and AEGIS adaptation across five benchmarks`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** v1 只测 55-task SWE-bench subset、tau3 三域；meta-agents 未测试，joint-control assumption 受限，代码为 future release。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14249:start -->
Claim boundary：只使用 `arXiv:2606.14249v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14249:end -->
<!-- review:SF-2026-ARXIV-2606-14249:end -->

<!-- review:SF-2026-ARXIV-2606-14275:start -->
### 2606.14275 — WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation

**问题与旧路径。** `LLM-curated hierarchical knowledge bases, namely a tree-structured wiki whose nodes summarize an underlying corpus, have become a dominant substrate for retrieval-augmented applications, yet their storage layer is still treated as an implementation detail.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 层级知识库需要 path-indexed KV 原生持有 schema evolution：offline rewrite 以无 read-path lock 的一致性协议提交，budgeted navigation 在同一树上提供 anytime refinement。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** WeChat Official Account AI Assistant 部署与 AuthTrace；四类 query operator 对 relational/graph/filesystem backends，end-to-end correctness 63.2%。 Method locator：`https://arxiv.org/html/2606.14275v1 — § exact-v1 anchor: path-indexed key-value storage`。Evaluation locator：`https://arxiv.org/html/2606.14275v1 — § exact-v1 evaluation anchor: AuthTrace`。Benchmark identity：model=`Not Disclosed — no single model identity governs the storage/backend comparison`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`AuthTrace and four query operators over relational, graph, and filesystem backends; end-to-end answer correctness`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一产品 workload 与 schema induction 不能证明任意 corpus 的一致性或答案真实性；offline rewrite、path churn 与导航预算仍可能制造 stale read。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14275:start -->
Claim boundary：只使用 `arXiv:2606.14275v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14275:end -->
<!-- review:SF-2026-ARXIV-2606-14275:end -->

<!-- review:SF-2026-ARXIV-2606-14350:start -->
### 2606.14350 — Design Methodology and Performance Trade-offs Management for Distributed and Compound AI Systems

**问题与旧路径。** `Artificial Intelligence (AI) systems must typically satisfy service-level objectives including accuracy, latency, and cost.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Compound AI system 设计应先枚举 workflow topology，再在 component configuration 上管理 accuracy/latency/cost trade-off，而不是逐模型局部调参。 Authoritative owner 是 `PLATFORM-FOUNDATIONS`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 8 类 workflow patterns、3 个 case studies；报告最高 60% latency、71% cost 改善且 accuracy 差距 2.5–4pp。 Method locator：`https://arxiv.org/html/2606.14350v1 — § exact-v1 anchor: workflow topology`。Evaluation locator：`https://arxiv.org/html/2606.14350v1 — § exact-v1 evaluation anchor: 3 case studies`。Benchmark identity：model=`Component models vary across the three exact-v1 compound-system case studies`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Case-study accuracy, latency, and cost trade-offs across eight workflow patterns`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** case studies 不构成统一 optimizer 或生产 SLO；组合空间与 workload drift 仍需平台逐运行校准。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14350:start -->
Claim boundary：只使用 `arXiv:2606.14350v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14350:end -->
<!-- review:SF-2026-ARXIV-2606-14350:end -->

<!-- review:SF-2026-ARXIV-2606-14356:start -->
### 2606.14356 — PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum

**问题与旧路径。** `Applications in the 3D Computing Continuum, which unifies edge, cloud, and space, require combining multiple AI tasks such as object detection, time-series analytics, and natural language processing into Compound AI systems.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** SLO-driven compound runtime 应把 task/data contract、可用 edge/cloud/space model profile 与 cooldown/threshold 状态交给在线 selector，而非固定一个最强模型。 Authoritative owner 是 `INFER-SCHEDULING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 两个 workflows；固定模型策略被报告最高 21× budget violation 或 4pp accuracy miss。 Method locator：`https://arxiv.org/html/2606.14356v1 — § exact-v1 anchor: CAIM Task and Data Contracts`。Evaluation locator：`https://arxiv.org/html/2606.14356v1 — § exact-v1 evaluation anchor: two workflows`。Benchmark identity：model=`Candidate edge, cloud, and space models enumerated in the two exact-v1 workflows`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Workflow-specific accuracy, latency, and resource-budget constraints; not a universal production SLO`；evaluator=`Constraint satisfaction, accuracy miss, and budget violation for runtime selection versus fixed-model policies`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两条 workflow 与作者 profile 不能给通用 SLO；profiling drift、switching delay 与不可用 region 必须触发 fallback。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14356:start -->
Claim boundary：只使用 `arXiv:2606.14356v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14356:end -->
<!-- review:SF-2026-ARXIV-2606-14356:end -->

<!-- review:SF-2026-ARXIV-2606-14445:start -->
### 2606.14445 — tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration

**问题与旧路径。** `Existing multi-agent software development systems have proposed many forms of agent collaboration, including role-based collaboration and automated code review.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 异构 Agent 协作可用 markdown+metadata 文件作为 canonical message、文件路径作为 payload、notification 作为 signal，并以 git worktree 隔离并发修改。 Authoritative owner 是 `AGENT-MULTI-AGENT`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 27 天、37 generations 的自用观察；209 PR、717 artifacts、375 reviews。 Method locator：`https://arxiv.org/html/2606.14445v1 — § exact-v1 anchor: file-based protocol`。Evaluation locator：`https://arxiv.org/html/2606.14445v1 — § exact-v1 evaluation anchor: 27-day`。Benchmark identity：model=`Claude- and Codex-based agents observed in one repository workflow`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Observational counts over 27 days and 37 generations: pull requests, artifacts, and reviews; no causal success evaluator`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 观察性单仓库且主要为 Claude/Codex，re-review 计数与成功无因果对应；文件协议不提供 authority、privacy 或 exactly-once delivery。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14445:start -->
Claim boundary：只使用 `arXiv:2606.14445v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14445:end -->
<!-- review:SF-2026-ARXIV-2606-14445:end -->

<!-- review:SF-2026-ARXIV-2606-14470:start -->
### 2606.14470 — GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge

**问题与旧路径。** `Large language model reasoning leaves no trace once it is done.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Reasoning/memory 若以 commit、note 与 tag 保存可获得 replay/diff/merge，但准确率收益主要来自近重复检索；当 copyability 低于约 0.8 时，版本化 substrate 本身不产生方法迁移。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 跨多类 reasoning tasks 的 retrieval/copyability probes；作者保留并解释被撤回/反驳的早期结论。 Method locator：`https://arxiv.org/html/2606.14470v1 — § exact-v1 anchor: every scored thought is a commit`。Evaluation locator：`https://arxiv.org/html/2606.14470v1 — § exact-v1 evaluation anchor: 7 All Experiments at a Glance`。Benchmark identity：model=`Reasoning agents in the exact-v1 retrieval and copyability probes`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task score, retrieval reuse, and copyability across five substrates, two benchmarks, and two scales`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 负结果绑定模型、任务和 sampling budget；git lineage 提供可审计性，不证明记忆内容正确或新问题迁移。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14470:start -->
Claim boundary：只使用 `arXiv:2606.14470v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14470:end -->
<!-- review:SF-2026-ARXIV-2606-14470:end -->

<!-- review:SF-2026-ARXIV-2606-14474:start -->
### 2606.14474 — Verifiable User Simulation for Search and Recommendation Systems

**问题与旧路径。** `Large-language-model (LLM) based user simulation is increasingly adopted for evaluating search engines, recommender systems, and retrieval-augmented generation pipelines, yet most simulators remain opaque: it is difficult to determine why a simulated user made a particular choice or whether that choice is consistent with the intended user profile.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** User simulator 应拆成 persona、task contract、matched execution、trace、verification、feedback、refinement 七个可审计组件。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 半日线下 tutorial 与两个 hands-on mini-labs；它提出 design-and-audit framework，不是统计验证过的 simulator benchmark。 Method locator：`https://arxiv.org/html/2606.14474v1 — § exact-v1 anchor: seven auditable components`。Evaluation locator：`https://arxiv.org/html/2606.14474v1 — § exact-v1 evaluation anchor: two hands-on mini-labs`。Benchmark identity：model=`Not Disclosed — tutorial framework and mini-labs, not a model-comparison benchmark`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Two hands-on mini-labs and component-audit exercises; no population-valid statistical evaluator`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 没有生产实验或 population-validity 证明；persona fidelity、demographic bias 与 human-agent discrepancy 仍需独立数据。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14474:start -->
Claim boundary：只使用 `arXiv:2606.14474v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14474:end -->
<!-- review:SF-2026-ARXIV-2606-14474:end -->

<!-- review:SF-2026-ARXIV-2606-14516:start -->
### 2606.14516 — Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results

**问题与旧路径。** `AI evaluations are widely used for testing and understanding progress.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Evaluation result 需要 source-agnostic result schema 与 instance-level output，把 model/benchmark/harness 元数据从分散 leaderboard 转成可复用 artifact。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 社区仓库快照含 22,235 models、2,273 benchmarks、31 formats，并提供 converters。 Method locator：`https://arxiv.org/html/2606.14516v1 — § exact-v1 anchor: 3 The Every Eval Ever Schema`。Evaluation locator：`https://arxiv.org/html/2606.14516v1 — § exact-v1 evaluation anchor: 7 Case Studies`。Benchmark identity：model=`Not Disclosed — repository records 22,235 models but does not evaluate one canonical model`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Schema conversion coverage and three case studies over 2,273 benchmarks and 31 source formats`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 统一字段不保证 score 语义可比、数据新鲜或 provenance 完整；community ingestion 仍需 validation。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14516:start -->
Claim boundary：只使用 `arXiv:2606.14516v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14516:end -->
<!-- review:SF-2026-ARXIV-2606-14516:end -->

<!-- review:SF-2026-ARXIV-2606-14517:start -->
### 2606.14517 — From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails

**问题与旧路径。** `LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Reasoning guardrail 也必须有 token/time/concurrency budget 与 fail-closed/fail-open policy；否则攻击者可让安全模型陷入长推理并通过共享 guardrail queue 放大为租户级 DoS。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 8 个 model backbones 上 13–63× token amplification；web/desktop/code/multi-agent deployments 中最高 148× latency amplification。 Method locator：`https://arxiv.org/html/2606.14517v1 — § exact-v1 anchor: beam-search optimization framework`。Evaluation locator：`https://arxiv.org/html/2606.14517v1 — § exact-v1 evaluation anchor: end-to-end real-world agent deployments`。Benchmark identity：model=`Eight guardrail backbones spanning Claude, GPT, Gemini, DeepSeek, and Qwen families as enumerated in exact-v1`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Guardrail token amplification and end-to-end agent latency amplification under optimized and structural payloads`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** beam-search payload 与作者部署不提供真实流量发生率；硬 cap 会产生安全 false negative，独立容量池也增加成本。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14517:start -->
Claim boundary：只使用 `arXiv:2606.14517v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14517:end -->
<!-- review:SF-2026-ARXIV-2606-14517:end -->

<!-- review:SF-2026-ARXIV-2606-14518:start -->
### 2606.14518 — Behavioral Audit of Machine Unlearning Has a Privacy Cost

**问题与旧路径。** `The removal of learned data from Machine Learning models through Machine Unlearning (MU) has been widely studied; however, there has yet to be an agreed-upon scheme for auditing MU.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Machine-unlearning audit 在互不信任 owner/auditor 下必须显式记录 audit leakage budget；只查询模型行为的通用 audit 对 convex models 无法同时识别 insufficient unlearning 且不泄露 retained-set membership。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** convex model 的 information-theoretic result与实验，并在 non-convex models 上观察同类 privacy-audit tension。 Method locator：`https://arxiv.org/html/2606.14518v1 — § exact-v1 anchor: information-theoretic proof`。Evaluation locator：`https://arxiv.org/html/2606.14518v1 — § exact-v1 evaluation anchor: empirical results on convex models`。Benchmark identity：model=`Convex models for the theorem-backed experiments plus non-convex models for empirical scope testing`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Insufficient-unlearning detectability versus retained-set membership leakage under mutually distrustful owner and auditor`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 定理前提不覆盖所有深网、side information 或 cryptographic proof；行为审计失败也不证明某次 unlearning 合规。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14518:start -->
Claim boundary：只使用 `arXiv:2606.14518v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14518:end -->
<!-- review:SF-2026-ARXIV-2606-14518:end -->

<!-- review:SF-2026-ARXIV-2606-14571:start -->
### 2606.14571 — StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance

**问题与旧路径。** `A central role of personal-agent memory is to turn stored information and prior interactions into future-oriented assistance.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Memory evaluation 要把 streaming observation→首次 evidence use→feedback incorporation→future reuse 拆成四个时序指标，不能用 stored 或单次 recall 代替未来辅助。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** EgoLife evidence anchors；8 个 memory systems、2 个 backbones 的两步 task sequences。 Method locator：`https://arxiv.org/html/2606.14571v1 — § exact-v1 anchor: two-step task sequence`。Evaluation locator：`https://arxiv.org/html/2606.14571v1 — § exact-v1 evaluation anchor: eight memory systems across two backbones`。Benchmark identity：model=`Eight memory systems across two backbone models in the exact-v1 StreamMemBench matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`First evidence use, storage, feedback incorporation, and future reuse over two-step task sequences with EgoLife evidence anchors`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两步序列和 egocentric stream 不能证明长期 identity/tenure；成功储存、局部 feedback incorporation 都不等于后续行为可靠。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14571:start -->
Claim boundary：只使用 `arXiv:2606.14571v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14571:end -->
<!-- review:SF-2026-ARXIV-2606-14571:end -->

<!-- review:SF-2026-ARXIV-2606-14574:start -->
### 2606.14574 — SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model

**问题与旧路径。** `Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Executable planning evaluator 必须让 symbolic world model 区分 immediate precondition failure、latent hazard 与 irreversible failure，并在 action commit 前运行 counterfactual foresight。 Authoritative owner 是 `AGENT-PLANNING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** kitchen world model含 77 actions、262 objects、约46,800 interactions；6 个 LLM，最佳 error-free plan 17%，latent failure最高56%。 Method locator：`https://arxiv.org/html/2606.14574v1 — § exact-v1 anchor: state machine executor`。Evaluation locator：`https://arxiv.org/html/2606.14574v1 — § exact-v1 evaluation anchor: six LLMs`。Benchmark identity：model=`Six LLMs in the exact-v1 Simmer matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Error-free plan rate plus immediate, latent, and irreversible failure classification in the symbolic kitchen world`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 人工符号世界只覆盖可编码 kitchen semantics；counterfactual simulator 不证明真实环境 fidelity，漏建 hazard 会形成假安全。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14574:start -->
Claim boundary：只使用 `arXiv:2606.14574v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14574:end -->
<!-- review:SF-2026-ARXIV-2606-14574:end -->

<!-- review:SF-2026-ARXIV-2606-14589:start -->
### 2606.14589 — When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime

**问题与旧路径。** `LLM agent systems increasingly run as long-lived autonomous runtimes: scheduling jobs, calling tools, maintaining memory, and pushing results to humans.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。 Authoritative owner 是 `PLATFORM-MONITORING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 8 周、约40 scheduled jobs、8 providers；22 incidents/至少28 manifestations，4,286 unit tests 与827 governance checks。 Method locator：`https://arxiv.org/html/2606.14589v1 — § exact-v1 anchor: five-class mechanism-oriented taxonomy`。Evaluation locator：`https://arxiv.org/html/2606.14589v1 — § exact-v1 evaluation anchor: 22 incidents`。Benchmark identity：model=`Production runtime spanning eight model providers; individual incident-model mapping is not disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Manual incident reconstruction and five-class taxonomy over 22 incidents, backed by 4,286 tests and 827 governance checks`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一私人 production runtime、人工 postmortem 与小样本不提供事故率；audit 擅长回归阻断而非 ex-ante 预防。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14589:start -->
Claim boundary：只使用 `arXiv:2606.14589v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14589:end -->
<!-- review:SF-2026-ARXIV-2606-14589:end -->

<!-- review:SF-2026-ARXIV-2606-14598:start -->
### 2606.14598 — Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0

**问题与旧路径。** `Post-training INT8 (W8A8) quantization of diffusion transformers is widely deployed as a speed optimization, yet on consumer Ampere GPUs it is frequently slower than the FP8 and NF4 alternatives it is meant to beat.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 低比特名义格式不等于执行了低比特 kernel；deployment contract 必须验证实际 int8×int8→int32 path、epilogue dequantization 与目标 GPU 的 native fast path。 Authoritative owner 是 `INFER-VLLM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** Ideogram 4.0、RTX 3090；per-GEMM 2.8–4.2×，768px end-to-end约1.1×；A100/B200 上同 kernel 反而输给 native bf16/FP8。 Method locator：`https://arxiv.org/html/2606.14598v1 — § exact-v1 anchor: fused Triton INT8 GEMM`。Evaluation locator：`https://arxiv.org/html/2606.14598v1 — § exact-v1 evaluation anchor: RTX 3090`。Benchmark identity：model=`Ideogram 4.0 diffusion transformer`；hardware=`NVIDIA RTX 3090 target; NVIDIA A100 and B200 negative-control comparisons`；precision=`INT8 by INT8 to INT32 accumulation with dequantization; BF16 and FP8 baselines where hardware supports them`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Per-GEMM latency and 768-pixel end-to-end generation latency, with output-quality checks bound to the exact-v1 study`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** NF4 margin 基于 n=4 且 variance 未量化；结果只适用于 consumer Ampere shapes，不是跨 GPU 或质量通用结论。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14598:start -->
Claim boundary：只使用 `arXiv:2606.14598v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14598:end -->
<!-- review:SF-2026-ARXIV-2606-14598:end -->

<!-- review:SF-2026-ARXIV-2606-14620:start -->
### 2606.14620 — Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens

**问题与旧路径。** `Open diffusion language models are marketed as parallel, non-autoregressive decoders, yet the order in which a shipped checkpoint actually commits its tokens is almost never measured.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Masked diffusion LM 的 token commit order 必须从 sampler accept events 测量；大批 simultaneous commit 使 token-level order 部分未定义，所谓 block size 可能只是观测粒度。 Authoritative owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** DiffusionGemma 26B、686 prompts、6 regimes；比较 commit granularity、confidence 与 task correctness。 Method locator：`https://arxiv.org/html/2606.14620v1 — § exact-v1 anchor: sampler accept step`。Evaluation locator：`https://arxiv.org/html/2606.14620v1 — § exact-v1 evaluation anchor: 686-prompt`。Benchmark identity：model=`DiffusionGemma 26B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Commit granularity, commit order, confidence, and task correctness over 686 prompts in six regimes`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一 checkpoint/sampler 的行为不定义整个 diffusion LM family；JSON、数学、事实任务间关系不可外推生产 latency。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14620:start -->
Claim boundary：只使用 `arXiv:2606.14620v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14620:end -->
<!-- review:SF-2026-ARXIV-2606-14620:end -->

<!-- review:SF-2026-ARXIV-2606-14629:start -->
### 2606.14629 — When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks

**问题与旧路径。** `Verifier-driven self-DPO is a common recipe for self-improving production visual-language models.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。 Authoritative owner 是 `AGENT-REFLECTION`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 多任务 self-improvement experiments 与 verifier/policy ablations；指标只绑定作者 task/model matrix。 Method locator：`https://arxiv.org/html/2606.14629v1 — § exact-v1 anchor: 2 Production setup`。Evaluation locator：`https://arxiv.org/html/2606.14629v1 — § exact-v1 evaluation anchor: 3 Headline finding: silent failure on MMMU`。Benchmark identity：model=`Qwen-3-VL-2B and Qwen-2.5-VL-3B students with Qwen2.5-VL/Qwen3-VL verifier ladder from 3B to 8B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Held-out old-task and new-task performance on MathVista, MMMU, and BLINK with verifier/policy ablations`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 同源 verifier、policy 与 synthetic data 会共偏；held-out task 仍可能与部署分布不同，改善旧任务不能授权 promotion。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14629:start -->
Claim boundary：只使用 `arXiv:2606.14629v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14629:end -->
<!-- review:SF-2026-ARXIV-2606-14629:end -->

<!-- review:SF-2026-ARXIV-2606-14672:start -->
### 2606.14672 — Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows

**问题与旧路径。** `Large language models increasingly serve as execution engines for agentic systems, yet they still consume context through a sequential text interface.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 并行 Agent 分支可以把 branch output编码为 latent state 再直接合成，但 merge owner 必须保留 branch identity、可解码验证与文本 fallback。 Authoritative owner 是 `AGENT-MULTI-AGENT`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 作者 workflow/task/model matrix上的 latent synthesis comparison；不把摘要中的速度或质量外推为生产 contract。 Method locator：`https://arxiv.org/html/2606.14672v1 — § exact-v1 anchor: 3 Methodology`。Evaluation locator：`https://arxiv.org/html/2606.14672v1 — § exact-v1 evaluation anchor: 4 Experiments`。Benchmark identity：model=`Parallel-branch LLM-agent models enumerated in the exact-v1 workflow/task/model matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task quality and time-to-first-token comparison for direct latent synthesis versus textual branch merging over nine datasets`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** latent merge 隐藏语义冲突与 provenance，无法验证时必须回退显式 artifact；有限实验不证明跨模型可交换。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14672:start -->
Claim boundary：只使用 `arXiv:2606.14672v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14672:end -->
<!-- review:SF-2026-ARXIV-2606-14672:end -->

<!-- review:SF-2026-ARXIV-2606-14674:start -->
### 2606.14674 — AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition

**问题与旧路径。** `LLM agents are increasingly built not as single model calls, but as scaffolded systems that combine reasoning, memory, reflection, action execution, and learning.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Embodied scaffold evaluation 应把 perception、memory、reasoning、reflection、action 与 learning 表示为 typed components，在固定接口下做 controlled composition。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** DeliveryBench、ALFRED、MiniGrid、RoboTHOR 与多 backbone，测 component interaction 和 scaffold compatibility。 Method locator：`https://arxiv.org/html/2606.14674v1 — § exact-v1 anchor: AgentSpec`。Evaluation locator：`https://arxiv.org/html/2606.14674v1 — § exact-v1 evaluation anchor: DeliveryBench`。Benchmark identity：model=`Multiple backbone models composed with typed AgentSpec scaffold components`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task success and component-interaction ablations on DeliveryBench, ALFRED, MiniGrid, and RoboTHOR`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 四个环境与标准接口会屏蔽真实 integration cost；模块 swap 的相对收益不等于生产系统可组合性。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14674:start -->
Claim boundary：只使用 `arXiv:2606.14674v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14674:end -->
<!-- review:SF-2026-ARXIV-2606-14674:end -->

<!-- review:SF-2026-ARXIV-2606-14832:start -->
### 2606.14832 — PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions

**问题与旧路径。** `Phone agents are increasingly expected to complete real mobile workflows rather than merely predict the next screen action.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Phone Agent action surface 应在 GUI、device CLI 与 structured tools 间显式 routing，并让 observable side-effect verifier而非 plausible response拥有完成判断。 Authoritative owner 是 `AGENT-TOOL-CALLING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** PhoneHarness Bench annotated split 报告 75.0% pass rate，比最强非 PhoneHarness setting高12.9pp。 Method locator：`https://arxiv.org/html/2606.14832v1 — § exact-v1 anchor: PhoneHarness`。Evaluation locator：`https://arxiv.org/html/2606.14832v1 — § exact-v1 evaluation anchor: annotated evaluation split`。Benchmark identity：model=`Phone-use agent configurations in the exact-v1 PhoneHarness matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Annotated split pass rate and observable side-effect verification versus non-PhoneHarness settings`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 单一 mobile harness 与 bounded GUI delegation 不证明权限、安全或跨设备可移植；deterministic router仍会误选 action surface。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14832:start -->
Claim boundary：只使用 `arXiv:2606.14832v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14832:end -->
<!-- review:SF-2026-ARXIV-2606-14832:end -->

<!-- review:SF-2026-ARXIV-2606-14885:start -->
### 2606.14885 — Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion

**问题与旧路径。** `Agentic search over large corpora relies on retriever-mediated interfaces (e.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。 Authoritative owner 是 `AGENT-CONTEXT`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** BrowseComp-Plus 71.2%/workspace-preserving reset 73.3%；100K–10M corpus scaling 与20M file-per-document Wiki-18。 Method locator：`https://arxiv.org/html/2606.14885v1 — § exact-v1 anchor: dynamic workspace expansion`。Evaluation locator：`https://arxiv.org/html/2606.14885v1 — § exact-v1 evaluation anchor: Browsecomp-Plus`。Benchmark identity：model=`DR-DCI agent plus retriever configurations in the exact-v1 corpus-scaling matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`BrowseComp-Plus accuracy, workspace-reset ablation, and corpus scaling from 100K to 10M items plus Wiki-18 at 20M files`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** retriever recall仍是上限，workspace会累积错误/污染与磁盘成本；公开 QA 不证明企业 ACL、更新或多租户一致性。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14885:start -->
Claim boundary：只使用 `arXiv:2606.14885v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14885:end -->
<!-- review:SF-2026-ARXIV-2606-14885:end -->

<!-- review:SF-2026-ARXIV-2606-14945:start -->
### 2606.14945 — Remember, Don't Re-read: Stateful ReAct Agents for Token-Efficient Autonomous Experimentation

**问题与旧路径。** `The autoresearch pattern enables autonomous experimentation by having a large language model (LLM) iteratively modify code to optimize a target metric.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Autonomous experimentation 可把 typed persistent experiment history 与 bounded conversation window分离，使每轮不必重读全部历史。 Authoritative owner 是 `AGENT-WORKFLOW`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 15-iteration hyperparameter tuning 与40-iteration code optimization；token reduction分别90%与52%，quality相当。 Method locator：`https://arxiv.org/html/2606.14945v1 — § exact-v1 anchor: stateful ReAct agent`。Evaluation locator：`https://arxiv.org/html/2606.14945v1 — § exact-v1 evaluation anchor: two benchmarks`。Benchmark identity：model=`Stateful ReAct and bounded-conversation baselines in two exact-v1 autonomous-experimentation workflows`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Final tuning/optimization quality and cumulative token use over 15 and 40 iterations`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两个 LangGraph benchmark不证明长期 state正确、并发安全或恢复；固定窗口可能隐藏决定性旧证据。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-14945:start -->
Claim boundary：只使用 `arXiv:2606.14945v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-14945:end -->
<!-- review:SF-2026-ARXIV-2606-14945:end -->

<!-- review:SF-2026-ARXIV-2606-15004:start -->
### 2606.15004 — CREST: Deployment-Realistic Hardware-in-the-Loop NAS for Embedded Sensing Systems

**问题与旧路径。** `Deploying neural networks on low-power microcontrollers (MCUs) requires selecting model architectures under tight memory, latency, and energy constraints.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Embedded NAS 的 evaluation identity 必须联合 model architecture、target MCU、runtime schedule、quantization 与 policy，并用 HIL measurement/replay替代 FLOPs proxy。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** inertial odometry与audio classification、3个 Arm Cortex-M targets；实测energy search较FLOPs selection降41.7%。 Method locator：`https://arxiv.org/html/2606.15004v1 — § exact-v1 anchor: CREST`。Evaluation locator：`https://arxiv.org/html/2606.15004v1 — § exact-v1 evaluation anchor: three Arm Cortex-M targets`。Benchmark identity：model=`NAS-selected inertial-odometry and audio-classification networks`；hardware=`Three Arm Cortex-M targets in the exact-v1 hardware-in-the-loop matrix`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Measured target-board energy and task quality versus FLOPs-based selection, including cross-board replay`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 三个 MCU 与两类 sensing workload 不构成跨芯片 Pareto；HIL 搜索昂贵且 firmware/toolchain drift 会改变结果。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15004:start -->
Claim boundary：只使用 `arXiv:2606.15004v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15004:end -->
<!-- review:SF-2026-ARXIV-2606-15004:end -->

<!-- review:SF-2026-ARXIV-2606-15008:start -->
### 2606.15008 — Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations

**问题与旧路径。** `Agentic large language model (LLM) systems can now execute actions, not only produce text.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Execution-coupled multi-Agent security要把 aggregation policy 当攻击放大器：any-one proposal 规则使最脆弱 agent 决定系统 exposure，consensus/routing才改变 commit threshold。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** GPT-5.2、DeepSeek-R1、Llama-4-Maverick；1→7 agents 时 compromise probability 0.24→0.86，policy gating有 latency/utility trade-off。 Method locator：`https://arxiv.org/html/2606.15008v1 — § exact-v1 anchor: III Methodology`。Evaluation locator：`https://arxiv.org/html/2606.15008v1 — § exact-v1 evaluation anchor: V Empirical Security Analysis`。Benchmark identity：model=`GPT-5.2, DeepSeek-R1, and Llama-4-Maverick`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Compromise probability, utility, and latency as agent count changes from one to seven under OpenClaw attack and policy-gating conditions`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** OpenClaw配置与归一化风险指标依作者假设；实验发生率不是生产 breach probability，consensus也可能共谋或停摆。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15008:start -->
Claim boundary：只使用 `arXiv:2606.15008v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15008:end -->
<!-- review:SF-2026-ARXIV-2606-15008:end -->

<!-- review:SF-2026-ARXIV-2606-15017:start -->
### 2606.15017 — Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents

**问题与旧路径。** `Online web agents often augment a base actor with memory, workflow, or skill modules.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** 在线 skill/memory module 必须在固定 total inference token budget下与 extra actor steps比较，并报告 run-to-run variance；module gross gain 不是净 utility。 Authoritative owner 是 `AGENT-MEMORY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** WebArena三域/WorkArena-L1；Gemini 3 Flash、GPT-5.4-mini、Qwen3.6-27B，budget-matched vanilla常持平或更好。 Method locator：`https://arxiv.org/html/2606.15017v1 — § exact-v1 anchor: budget-matched vanilla baseline`。Evaluation locator：`https://arxiv.org/html/2606.15017v1 — § exact-v1 evaluation anchor: three WebArena domains`。Benchmark identity：model=`Gemini 3 Flash, GPT-5.4-mini, and Qwen3.6-27B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Task success and token budget on three WebArena domains and WorkArena-L1 against budget-matched vanilla baselines`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 只覆盖 AWM/ASI/ReasoningBank 与所测域；负结果不证明离线复用、昂贵失败或其他 cost structure 下 memory无价值。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15017:start -->
Claim boundary：只使用 `arXiv:2606.15017v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15017:end -->
<!-- review:SF-2026-ARXIV-2606-15017:end -->

<!-- review:SF-2026-ARXIV-2606-15020:start -->
### 2606.15020 — Semantic Integrity Failures in Document-to-LLM Supply Chains

**问题与旧路径。** `Document-to-LLM applications typically read uploaded PDFs by first translating them into text through a hidden extraction layer that users cannot observe or audit.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。 Authoritative owner 是 `PLATFORM-SECURITY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 25 extraction gaps、16 PDF processing stacks、7 commercial LLM services；每个 service 至少暴露一种 gap。 Method locator：`https://arxiv.org/html/2606.15020v1 — § exact-v1 anchor: 25 extraction gaps`。Evaluation locator：`https://arxiv.org/html/2606.15020v1 — § exact-v1 evaluation anchor: 16 PDF processing stacks`。Benchmark identity：model=`Seven commercial LLM services evaluated as document-ingestion endpoints; base-model versions are Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Detection of 25 render/extract semantic gaps across 16 PDF-processing stacks and seven services`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** scanner规则只覆盖已知25类且可能误报；双视图一致也不证明文档真实或模型安全，动态/OCR路径仍需独立审计。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15020:start -->
Claim boundary：只使用 `arXiv:2606.15020v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15020:end -->
<!-- review:SF-2026-ARXIV-2606-15020:end -->

<!-- review:SF-2026-ARXIV-2606-15029:start -->
### 2606.15029 — Metric Match: A Subset Selection Approach to Evaluating LLM Judge Reliability

**问题与旧路径。** `LLM judges are used to reduce the need for costly human labor in evaluating open-ended text generation.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Judge reliability 在 human label预算有限时可选择 synthetic-label metric匹配的 subset，再把估计问题与是否越过 deployment threshold的分类问题分开。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 4种 correlation metrics、15 datasets；对 random subset win-rate 0.838，平均 estimation error降18.7%。 Method locator：`https://arxiv.org/html/2606.15029v1 — § exact-v1 anchor: Metric Match`。Evaluation locator：`https://arxiv.org/html/2606.15029v1 — § exact-v1 evaluation anchor: 15 datasets`。Benchmark identity：model=`LLM judges in the exact-v1 15-dataset reliability matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Subset-selection win rate and correlation-estimation error across four correlation metrics`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** synthetic labels与judge可能共偏，subset matching不保证稀有 failure coverage；医疗成本case不构成通用标注价格。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15029:start -->
Claim boundary：只使用 `arXiv:2606.15029v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15029:end -->
<!-- review:SF-2026-ARXIV-2606-15029:end -->

<!-- review:SF-2026-ARXIV-2606-15034:start -->
### 2606.15034 — OSGuard: A Benchmark for Safety in Computer-Use Agents

**问题与旧路径。** `Computer-use agents are increasingly evaluated by whether they complete realistic desktop and web tasks.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Computer-use safety必须同时测 action-level allowed/unrelated/unsafe判断和risk-augmented end-to-end state invariant，nominal task success不能覆盖unsafe shortcut。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** action-level contextual proposals与OSWorld-derived execution variants；保留原success evaluator并增加state-based safety invariants。 Method locator：`https://arxiv.org/html/2606.15034v1 — § exact-v1 anchor: OSGuard`。Evaluation locator：`https://arxiv.org/html/2606.15034v1 — § exact-v1 evaluation anchor: risk-augmented execution suite`。Benchmark identity：model=`Computer-use agents evaluated through OSGuard; exact identities remain bound to the v1 matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Original task-success evaluator plus state-based safety invariants on risk-augmented OSWorld-derived executions`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 手工hazard与predicate不完备，局部guardrail分数不证明端到端安全，新增invariant也可能拒绝合法路径。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-15034:start -->
Claim boundary：只使用 `arXiv:2606.15034v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-15034:end -->
<!-- review:SF-2026-ARXIV-2606-15034:end -->

<!-- review:SF-2026-ARXIV-2606-17090:start -->
### 2606.17090 — ANEForge: Python for direct computation on the Apple Neural Engine

**问题与旧路径。** `ANEForge is a Python package that programs the Apple Neural Engine (ANE), the fixed-function neural accelerator on every recent Apple device, directly and without CoreML.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Apple ANE runtime 的执行身份必须绑定 macOS/ANE compiler版本与实际dispatch target；direct graph/program路径才能区分“允许调度到ANE”与“确认在ANE执行”。 Authoritative owner 是 `INFER-VLLM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** macOS 14+ Apple Silicon；58 fused与19 bridge ops，int8/int4/sparse weights；约90µs call、70µs dispatch floor，ResNet-18 0.33ms。 Method locator：`https://arxiv.org/html/2606.17090v1 — § exact-v1 anchor: lazy tensor graph`。Evaluation locator：`https://arxiv.org/html/2606.17090v1 — § exact-v1 evaluation anchor: ResNet-18 forward`。Benchmark identity：model=`ResNet-18 forward plus 58 fused and 19 bridge operator microbenchmarks`；hardware=`Apple Silicon Neural Engine on macOS 14 or later; exact chip identity is Not Disclosed`；precision=`INT8, INT4, and sparse-weight paths where supported`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Reference-output matching, call and dispatch latency, operator microbenchmarks, and ResNet-18 forward latency`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 依赖私有/版本敏感 daemon与compiler，release可能随OS失效；microbench与reference matching不证明完整训练稳定性或通用模型支持。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-17090:start -->
Claim boundary：只使用 `arXiv:2606.17090v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-17090:end -->
<!-- review:SF-2026-ARXIV-2606-17090:end -->

<!-- review:SF-2026-ARXIV-2606-19376:start -->
### 2606.19376 — Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees

**问题与旧路径。** `Inference costs for large language model (LLM) applications are rapidly growing, driven by surging demand and rising infrastructure cost.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。 Authoritative owner 是 `INFER-SCHEDULING`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。 Method locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 anchor: SLARouter`。Evaluation locator：`https://arxiv.org/html/2606.19376v1 — § exact-v1 evaluation anchor: wide range of LLM benchmarks`。Benchmark identity：model=`Candidate LLMs in the exact-v1 SLARouter benchmark matrix`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO`；evaluator=`Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-19376:start -->
Claim boundary：只使用 `arXiv:2606.19376v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-19376:end -->
<!-- review:SF-2026-ARXIV-2606-19376:end -->

<!-- review:SF-2026-ARXIV-2606-20668:start -->
### 2606.20668 — BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems

**问题与旧路径。** `LLM supervision systems, namely input/output moderation filters and jailbreak detectors, are the primary safeguard against misuse in deployed AI applications, yet existing benchmarks are often vendor-biased, omit cost and latency, and rarely compare specialized guardrails against repurposed generalist LLMs.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Guardrail选择必须在同一合同联合测 detection、false positive、latency与monetary cost，并分开content moderation与jailbreak detection Pareto frontier。 Authoritative owner 是 `PLATFORM-EVALUATION-SYSTEM`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 28 systems/17 providers、11 harm categories、13 attack techniques；specialist与frontier generalist supervisors的operational comparison。 Method locator：`https://arxiv.org/html/2606.20668v1 — § exact-v1 anchor: BELLS-O`。Evaluation locator：`https://arxiv.org/html/2606.20668v1 — § exact-v1 evaluation anchor: 28 systems from 17 providers`。Benchmark identity：model=`Twenty-eight supervision systems from 17 providers`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Operational harm coverage, attack coverage, quality, latency, and cost over 11 harm categories and 13 attack techniques`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** in-house/paraphrased data仍可能有generator fingerprint与vendor drift；公开点估计不是生产SLO或安全认证。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-20668:start -->
Claim boundary：只使用 `arXiv:2606.20668v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-20668:end -->
<!-- review:SF-2026-ARXIV-2606-20668:end -->

<!-- review:SF-2026-ARXIV-2606-24898:start -->
### 2606.24898 — Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models

**问题与旧路径。** `Looped language models turn hidden states into runtime state: each state is decoded for prediction and fed back into future computation.` 旧路径在范围固定、风险低或额外状态成本不值得时仍可继续使用；本 family 不把项目名称当成新 owner。

**机制与 state / data / control owner。** Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。 Authoritative owner 是 `MODEL-DECODER-ONLY`：它持有需要版本化的状态与 commit / rollback decision；相邻章节只消费有 identity 的 handoff。

**Evaluation：证明与未证明。** 44M与129M looped transformers；无inter-loop normalization时norm升至数千/数万，scale-visible readout、norm penalty或scale-removing recurrence保持在数十。 Method locator：`https://arxiv.org/html/2606.24898v1 — § exact-v1 anchor: readout blind spot`。Evaluation locator：`https://arxiv.org/html/2606.24898v1 — § exact-v1 evaluation anchor: 44M and 129M looped transformers`。Benchmark identity：model=`44M- and 129M-parameter looped transformers`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed — task, dataset, or trial counts are not batch size`；concurrency=`Not Disclosed — parallel agents or trials are not serving concurrency`；SLO=`Not Disclosed — reported metrics are not a production SLO`；evaluator=`Per-loop cross-entropy plus hidden-state norm across baseline, scale-visible readout, norm-penalty, and scale-removing recurrence variants`。这只证明 exact-v1 绑定的合同；不从任务数、并行 trial 或平均 latency 反推未披露的执行字段。

**Trade-off、failure、共存与演进。** 两种小规模looped模型与variable-depth benchmark不证明所有recurrent architecture；norm稳定也不保证语义correctness或大规模收敛。 因而旧方案在论文前提不成立或验证成本高于收益时继续共存；该 evidence 只支持这里写出的 delta。

<!-- claim:SF-2026-ARXIV-2606-24898:start -->
Claim boundary：只使用 `arXiv:2606.24898v1` official HTML，未用 later version 或未版本化镜像；ordinary pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-24898:end -->
<!-- review:SF-2026-ARXIV-2606-24898:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-14027 | SOPBench 覆盖 50 个 source-sink 类别组合、5 个 agentic browsers 与 6 个 backbone LLM；BrowserOS-SOPGuard 报告 0.00 violation rate 与 2.07%–5.79% runtime overhead。 | Six backbone LLMs in the exact-v1 SOPBench matrix; no single-model aggregate | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | SOP violation rate, paired utility tests, and runtime overhead on SOPBench, Mind2Web, WebArena-Infinity, and REAL |
| SF-2026-ARXIV-2606-14106 | OSWorld、WebForge、AgentNetBench 的四类 failure audit；OSWorld/GPT-5.4-mini 上 AGMem 由 full-image memory 的 20.4% 提升到 27.2% accuracy。 | GPT-5.4-mini for the reported OSWorld AGMem result; additional GUI-agent settings remain bound to the exact-v1 matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Task accuracy plus state, grounding, hidden-operation, and recovery-failure audit on OSWorld, WebForge, and AgentNetBench |
| SF-2026-ARXIV-2606-14130 | 6 个 environments、15 个 variants；在 AMD EPYC 7702P、203.48 GiB RAM 与单 NVIDIA A16 14.6 GiB 上评估 contract synthesis/selection。 | Environment-specific MARL policies plus certified contract-library selector; no LLM | AMD EPYC 7702P; 203.48 GiB RAM; one NVIDIA A16 with 14.6 GiB | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Safety violations, reward, synthesis cost, and selector behavior across six environments and 15 variants |
| SF-2026-ARXIV-2606-14154 | 76 个 strongest-attack 样本与跨 Qwen2.5-Coder-7B-Instruct、GPT-4o-mini、GPT-5.4-mini/5.4 的 attack/defense comparison。 | Qwen2.5-Coder-7B-Instruct, GPT-4o-mini, GPT-5.4-mini, and GPT-5.4 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Attack success and defense comparison over 13 cross-modal attack categories and 76 strongest-attack samples |
| SF-2026-ARXIV-2606-14179 | Qwen3-4B-Thinking 迭代 SFT+GRPO；validation reward 0.43→0.78，process accuracy 92%，并以 GPT-5 的 94% 作受限比较。 | Qwen3-4B-Thinking trained with SFT plus GRPO; GPT-5 used only as a bounded process-accuracy comparison | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Validation reward and process accuracy under exact, fuzzy, and missing cache tiers |
| SF-2026-ARXIV-2606-14200 | AppWorld 的 14-agent heterogeneous pool；攻击实验显示 global routing regret 可从 0 增至 0.94，并评估 zero-evidence gate。 | Fourteen heterogeneous agents in the AppWorld routing pool; exact backbone identities remain bound to the v1 experiment table | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Routing regret, task outcome, and zero-evidence behavior under skill-conditional and global reputation |
| SF-2026-ARXIV-2606-14239 | 89 个 containerized tasks、8 个 professional domains；不访问 hidden tests、reference solutions 或 external rewards，平均 reward 73.9%。 | Skill-evolving coding agents in the exact-v1 paired-run matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Fixed structural verifier and task reward over 89 containerized tasks in eight domains; no hidden tests, reference solutions, or external rewards exposed to the auditor |
| SF-2026-ARXIV-2606-14249 | 5 个 benchmarks、15 个 model-benchmark configurations，并比较九个 harness dimensions 与 AEGIS adaptation。 | Fifteen model-benchmark configurations in the exact-v1 HarnessX matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Benchmark score, harness-dimension coverage, composition behavior, and AEGIS adaptation across five benchmarks |
| SF-2026-ARXIV-2606-14275 | WeChat Official Account AI Assistant 部署与 AuthTrace；四类 query operator 对 relational/graph/filesystem backends，end-to-end correctness 63.2%。 | Not Disclosed — no single model identity governs the storage/backend comparison | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | AuthTrace and four query operators over relational, graph, and filesystem backends; end-to-end answer correctness |
| SF-2026-ARXIV-2606-14350 | 8 类 workflow patterns、3 个 case studies；报告最高 60% latency、71% cost 改善且 accuracy 差距 2.5–4pp。 | Component models vary across the three exact-v1 compound-system case studies | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Case-study accuracy, latency, and cost trade-offs across eight workflow patterns |
| SF-2026-ARXIV-2606-14356 | 两个 workflows；固定模型策略被报告最高 21× budget violation 或 4pp accuracy miss。 | Candidate edge, cloud, and space models enumerated in the two exact-v1 workflows | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Workflow-specific accuracy, latency, and resource-budget constraints; not a universal production SLO | Constraint satisfaction, accuracy miss, and budget violation for runtime selection versus fixed-model policies |
| SF-2026-ARXIV-2606-14445 | 27 天、37 generations 的自用观察；209 PR、717 artifacts、375 reviews。 | Claude- and Codex-based agents observed in one repository workflow | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Observational counts over 27 days and 37 generations: pull requests, artifacts, and reviews; no causal success evaluator |
| SF-2026-ARXIV-2606-14470 | 跨多类 reasoning tasks 的 retrieval/copyability probes；作者保留并解释被撤回/反驳的早期结论。 | Reasoning agents in the exact-v1 retrieval and copyability probes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Task score, retrieval reuse, and copyability across five substrates, two benchmarks, and two scales |
| SF-2026-ARXIV-2606-14474 | 半日线下 tutorial 与两个 hands-on mini-labs；它提出 design-and-audit framework，不是统计验证过的 simulator benchmark。 | Not Disclosed — tutorial framework and mini-labs, not a model-comparison benchmark | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Two hands-on mini-labs and component-audit exercises; no population-valid statistical evaluator |
| SF-2026-ARXIV-2606-14516 | 社区仓库快照含 22,235 models、2,273 benchmarks、31 formats，并提供 converters。 | Not Disclosed — repository records 22,235 models but does not evaluate one canonical model | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Schema conversion coverage and three case studies over 2,273 benchmarks and 31 source formats |
| SF-2026-ARXIV-2606-14517 | 8 个 model backbones 上 13–63× token amplification；web/desktop/code/multi-agent deployments 中最高 148× latency amplification。 | Eight guardrail backbones spanning Claude, GPT, Gemini, DeepSeek, and Qwen families as enumerated in exact-v1 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Guardrail token amplification and end-to-end agent latency amplification under optimized and structural payloads |
| SF-2026-ARXIV-2606-14518 | convex model 的 information-theoretic result与实验，并在 non-convex models 上观察同类 privacy-audit tension。 | Convex models for the theorem-backed experiments plus non-convex models for empirical scope testing | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Insufficient-unlearning detectability versus retained-set membership leakage under mutually distrustful owner and auditor |
| SF-2026-ARXIV-2606-14571 | EgoLife evidence anchors；8 个 memory systems、2 个 backbones 的两步 task sequences。 | Eight memory systems across two backbone models in the exact-v1 StreamMemBench matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | First evidence use, storage, feedback incorporation, and future reuse over two-step task sequences with EgoLife evidence anchors |
| SF-2026-ARXIV-2606-14574 | kitchen world model含 77 actions、262 objects、约46,800 interactions；6 个 LLM，最佳 error-free plan 17%，latent failure最高56%。 | Six LLMs in the exact-v1 Simmer matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Error-free plan rate plus immediate, latent, and irreversible failure classification in the symbolic kitchen world |
| SF-2026-ARXIV-2606-14589 | 8 周、约40 scheduled jobs、8 providers；22 incidents/至少28 manifestations，4,286 unit tests 与827 governance checks。 | Production runtime spanning eight model providers; individual incident-model mapping is not disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Manual incident reconstruction and five-class taxonomy over 22 incidents, backed by 4,286 tests and 827 governance checks |
| SF-2026-ARXIV-2606-14598 | Ideogram 4.0、RTX 3090；per-GEMM 2.8–4.2×，768px end-to-end约1.1×；A100/B200 上同 kernel 反而输给 native bf16/FP8。 | Ideogram 4.0 diffusion transformer | NVIDIA RTX 3090 target; NVIDIA A100 and B200 negative-control comparisons | INT8 by INT8 to INT32 accumulation with dequantization; BF16 and FP8 baselines where hardware supports them | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Per-GEMM latency and 768-pixel end-to-end generation latency, with output-quality checks bound to the exact-v1 study |
| SF-2026-ARXIV-2606-14620 | DiffusionGemma 26B、686 prompts、6 regimes；比较 commit granularity、confidence 与 task correctness。 | DiffusionGemma 26B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Commit granularity, commit order, confidence, and task correctness over 686 prompts in six regimes |
| SF-2026-ARXIV-2606-14629 | exact-v1 多任务 self-improvement experiments 与 verifier/policy ablations；指标只绑定作者 task/model matrix。 | Qwen-3-VL-2B and Qwen-2.5-VL-3B students with Qwen2.5-VL/Qwen3-VL verifier ladder from 3B to 8B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Held-out old-task and new-task performance on MathVista, MMMU, and BLINK with verifier/policy ablations |
| SF-2026-ARXIV-2606-14672 | 作者 workflow/task/model matrix上的 latent synthesis comparison；不把摘要中的速度或质量外推为生产 contract。 | Parallel-branch LLM-agent models enumerated in the exact-v1 workflow/task/model matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Task quality and time-to-first-token comparison for direct latent synthesis versus textual branch merging over nine datasets |
| SF-2026-ARXIV-2606-14674 | DeliveryBench、ALFRED、MiniGrid、RoboTHOR 与多 backbone，测 component interaction 和 scaffold compatibility。 | Multiple backbone models composed with typed AgentSpec scaffold components | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Task success and component-interaction ablations on DeliveryBench, ALFRED, MiniGrid, and RoboTHOR |
| SF-2026-ARXIV-2606-14832 | PhoneHarness Bench annotated split 报告 75.0% pass rate，比最强非 PhoneHarness setting高12.9pp。 | Phone-use agent configurations in the exact-v1 PhoneHarness matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Annotated split pass rate and observable side-effect verification versus non-PhoneHarness settings |
| SF-2026-ARXIV-2606-14885 | BrowseComp-Plus 71.2%/workspace-preserving reset 73.3%；100K–10M corpus scaling 与20M file-per-document Wiki-18。 | DR-DCI agent plus retriever configurations in the exact-v1 corpus-scaling matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | BrowseComp-Plus accuracy, workspace-reset ablation, and corpus scaling from 100K to 10M items plus Wiki-18 at 20M files |
| SF-2026-ARXIV-2606-14945 | 15-iteration hyperparameter tuning 与40-iteration code optimization；token reduction分别90%与52%，quality相当。 | Stateful ReAct and bounded-conversation baselines in two exact-v1 autonomous-experimentation workflows | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Final tuning/optimization quality and cumulative token use over 15 and 40 iterations |
| SF-2026-ARXIV-2606-15004 | inertial odometry与audio classification、3个 Arm Cortex-M targets；实测energy search较FLOPs selection降41.7%。 | NAS-selected inertial-odometry and audio-classification networks | Three Arm Cortex-M targets in the exact-v1 hardware-in-the-loop matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Measured target-board energy and task quality versus FLOPs-based selection, including cross-board replay |
| SF-2026-ARXIV-2606-15008 | GPT-5.2、DeepSeek-R1、Llama-4-Maverick；1→7 agents 时 compromise probability 0.24→0.86，policy gating有 latency/utility trade-off。 | GPT-5.2, DeepSeek-R1, and Llama-4-Maverick | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Compromise probability, utility, and latency as agent count changes from one to seven under OpenClaw attack and policy-gating conditions |
| SF-2026-ARXIV-2606-15017 | WebArena三域/WorkArena-L1；Gemini 3 Flash、GPT-5.4-mini、Qwen3.6-27B，budget-matched vanilla常持平或更好。 | Gemini 3 Flash, GPT-5.4-mini, and Qwen3.6-27B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Task success and token budget on three WebArena domains and WorkArena-L1 against budget-matched vanilla baselines |
| SF-2026-ARXIV-2606-15020 | 25 extraction gaps、16 PDF processing stacks、7 commercial LLM services；每个 service 至少暴露一种 gap。 | Seven commercial LLM services evaluated as document-ingestion endpoints; base-model versions are Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Detection of 25 render/extract semantic gaps across 16 PDF-processing stacks and seven services |
| SF-2026-ARXIV-2606-15029 | 4种 correlation metrics、15 datasets；对 random subset win-rate 0.838，平均 estimation error降18.7%。 | LLM judges in the exact-v1 15-dataset reliability matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Subset-selection win rate and correlation-estimation error across four correlation metrics |
| SF-2026-ARXIV-2606-15034 | action-level contextual proposals与OSWorld-derived execution variants；保留原success evaluator并增加state-based safety invariants。 | Computer-use agents evaluated through OSGuard; exact identities remain bound to the v1 matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Original task-success evaluator plus state-based safety invariants on risk-augmented OSWorld-derived executions |
| SF-2026-ARXIV-2606-17090 | macOS 14+ Apple Silicon；58 fused与19 bridge ops，int8/int4/sparse weights；约90µs call、70µs dispatch floor，ResNet-18 0.33ms。 | ResNet-18 forward plus 58 fused and 19 bridge operator microbenchmarks | Apple Silicon Neural Engine on macOS 14 or later; exact chip identity is Not Disclosed | INT8, INT4, and sparse-weight paths where supported | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Reference-output matching, call and dispatch latency, operator microbenchmarks, and ResNet-18 forward latency |
| SF-2026-ARXIV-2606-19376 | 多类LLM benchmarks；SLARouter报告保持SLA并最高降成本2.2×，无需per-benchmark tuning。 | Candidate LLMs in the exact-v1 SLARouter benchmark matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Per-user satisfaction guarantee used by SLARouter; no universal deployment SLO | Cost subject to user-satisfaction guarantee over multiple LLM benchmarks with sparse one-sided feedback |
| SF-2026-ARXIV-2606-20668 | 28 systems/17 providers、11 harm categories、13 attack techniques；specialist与frontier generalist supervisors的operational comparison。 | Twenty-eight supervision systems from 17 providers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Operational harm coverage, attack coverage, quality, latency, and cost over 11 harm categories and 13 attack techniques |
| SF-2026-ARXIV-2606-24898 | 44M与129M looped transformers；无inter-loop normalization时norm升至数千/数万，scale-visible readout、norm penalty或scale-removing recurrence保持在数十。 | 44M- and 129M-parameter looped transformers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed — task, dataset, or trial counts are not batch size | Not Disclosed — parallel agents or trials are not serving concurrency | Not Disclosed — reported metrics are not a production SLO | Per-loop cross-entropy plus hidden-state norm across baseline, scale-visible readout, norm-penalty, and scale-removing recurrence variants |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-14027 | score_7_9; potential_books_delta | selected | DA-20260613-AGENT-BROWSER-ORIGIN | — | 它把浏览器安全边界从 script execution 扩展到 agent-mediated dataflow，跨越 security owner，优先于只改善单一 benchmark 或已有 harness 结构的 family。 | analysis:DA-20260613-AGENT-BROWSER-ORIGIN |
| SF-2026-ARXIV-2606-14106 | score_7_9; potential_books_delta | not_selected | — | — | 它提供视觉 memory construction 的具体反例与替代表示，但系统 reach 小于 SOP 与 guardrail availability，因此保留而不进入三项 narrative。 | analysis-decision:SF-2026-ARXIV-2606-14106 |
| SF-2026-ARXIV-2606-14130 | score_7_9 | not_selected | — | — | 它强化 06-12 已写入 Ch72 的 model-bound shield，不新增独立 owner；因此不挤占今日三个互不重叠的 analysis slots。 | analysis-decision:SF-2026-ARXIV-2606-14130 |
| SF-2026-ARXIV-2606-14154 | score_7_9; potential_books_delta | not_selected | — | — | 它为既有 Skill Security 增加 code-language composition blind spot，重要但仍是 SOP 之外的供应链子面。 | analysis-decision:SF-2026-ARXIV-2606-14154 |
| SF-2026-ARXIV-2606-14179 | score_7_9 | not_selected | — | — | Ch33 已有 opaque harness trajectory capture、partial rollout 与 cross-policy reuse；该结果作为缓存 fidelity 的受限证据，不复制新段。 | analysis-decision:SF-2026-ARXIV-2606-14179 |
| SF-2026-ARXIV-2606-14200 | score_7_9; potential_books_delta | not_selected | — | — | 它补足 Ch82 behavioral belief 与 authenticated identity 之间的 skill dimension，是今日多 Agent frontier 最清楚的 owner delta。 | analysis-decision:SF-2026-ARXIV-2606-14200 |
| SF-2026-ARXIV-2606-14239 | score_7_9 | not_selected | — | — | Ch80/81 已有 decision history、fixed evaluator、promotion/rollback；本 family 是强证据 handoff，不再建立第二套 skill-evolution owner。 | analysis-decision:SF-2026-ARXIV-2606-14239 |
| SF-2026-ARXIV-2606-14249 | score_7_9 | not_selected | — | — | Ch81/84 已拥有 template/realized graph/trace、harness revision 与 promotion，故只保留 evidence，不复制 foundry taxonomy。 | analysis-decision:SF-2026-ARXIV-2606-14249 |
| SF-2026-ARXIV-2606-14275 | score_7_9; potential_books_delta | not_selected | — | — | 它把 memory schema evolution 与 concurrent read consistency合并为存储 contract，超出现有 patch-history 段的范围，适合 Ch77 最小增量。 | analysis-decision:SF-2026-ARXIV-2606-14275 |
| SF-2026-ARXIV-2606-14350 | score_7_9 | not_selected | — | — | 这是对全书 system-first 方法的再表述，现有 Ch57 与 Ch56 已有 owner，故不新增正文。 | analysis-decision:SF-2026-ARXIV-2606-14350 |
| SF-2026-ARXIV-2606-14356 | score_7_9 | not_selected | — | — | Ch56 已有 model/quantization/placement joint admission、risk contract 与 SLO budget，本 family 不再复制 selector。 | analysis-decision:SF-2026-ARXIV-2606-14356 |
| SF-2026-ARXIV-2606-14445 | score_7_9 | not_selected | — | — | Ch82 已有 typed public state 与 repository commitment protocol；tap 只提供一种实现实例。 | analysis-decision:SF-2026-ARXIV-2606-14445 |
| SF-2026-ARXIV-2606-14470 | score_7_9 | not_selected | — | — | Ch77 已有 event sourcing、patch history 与 execution-state tree；本 family 的价值是负证据，不需另开机制段。 | analysis-decision:SF-2026-ARXIV-2606-14470 |
| SF-2026-ARXIV-2606-14474 | score_7_9 | not_selected | — | — | Ch66 已把 simulator identity、hidden constraints、question budget 与 scorer 固定，本 proposal 只作概念 handoff。 | analysis-decision:SF-2026-ARXIV-2606-14474 |
| SF-2026-ARXIV-2606-14516 | score_7_9 | not_selected | — | — | Ch66 Evaluation Card、claim provenance 和 evaluation identity 已覆盖该长期命题，仓库规模只作实现证据。 | analysis-decision:SF-2026-ARXIV-2606-14516 |
| SF-2026-ARXIV-2606-14517 | score_7_9; potential_books_delta | selected | DA-20260613-GUARDRAIL-AVAILABILITY | — | 它把安全 sensor 的计算成本提升为 availability authority，是今日 security frontier 中最直接的平台控制面变化。 | analysis:DA-20260613-GUARDRAIL-AVAILABILITY |
| SF-2026-ARXIV-2606-14518 | score_7_9; potential_books_delta | not_selected | — | — | 它为既有 source-level unlearning 增加 auditor threat model 与不可兼得边界，适合 Ch72 而非再写一种 unlearning algorithm。 | analysis-decision:SF-2026-ARXIV-2606-14518 |
| SF-2026-ARXIV-2606-14571 | score_7_9 | not_selected | — | — | Ch66 已有 longitudinal fact-first 与 read/write audit；该 benchmark完善 slice，不改变 owner。 | analysis-decision:SF-2026-ARXIV-2606-14571 |
| SF-2026-ARXIV-2606-14574 | score_7_9; potential_books_delta | not_selected | — | — | 它补足 Ch79 从计划可执行到延迟危害的 state-machine gate，与普通最终成功率不同。 | analysis-decision:SF-2026-ARXIV-2606-14574 |
| SF-2026-ARXIV-2606-14589 | score_7_9; potential_books_delta | not_selected | — | — | 它把监控目标从异常计数推进到 narrative masking 与 seam ownership，是 Ch67 的直接长期增量。 | analysis-decision:SF-2026-ARXIV-2606-14589 |
| SF-2026-ARXIV-2606-14598 | score_7_9 | not_selected | — | — | Ch35/50 已要求量化 artifact绑定 graph/kernel/hardware；该工作是很好的负/正实测，不需要 vLLM owner 新段。 | analysis-decision:SF-2026-ARXIV-2606-14598 |
| SF-2026-ARXIV-2606-14620 | score_7_9 | not_selected | — | — | Ch24 已明确 parallel positions 在 commit 前可撤销以及 target commit owner，本 family校正测量语言但不新增机制。 | analysis-decision:SF-2026-ARXIV-2606-14620 |
| SF-2026-ARXIV-2606-14629 | score_7_9; potential_books_delta | not_selected | — | — | 它把 Ch80 的 verifier authority 问题具体化为跨任务 regression gate，形成独立于今日安全/模型两项的 evolution evidence。 | analysis-decision:SF-2026-ARXIV-2606-14629 |
| SF-2026-ARXIV-2606-14672 | score_7_9 | not_selected | — | — | Ch82 已规定 latent communication 不能删除 contract，因而该方法完全落在现有共存边界。 | analysis-decision:SF-2026-ARXIV-2606-14672 |
| SF-2026-ARXIV-2606-14674 | score_7_9 | not_selected | — | — | Ch66 已固定 model×benchmark×harness×environment×scorer，并要求 component interaction audit，本 family不另建 schema。 | analysis-decision:SF-2026-ARXIV-2606-14674 |
| SF-2026-ARXIV-2606-14832 | score_7_9 | not_selected | — | — | Ch78 已有 interface granularity、canonical effect 与独立 outcome contract；PhoneHarness 是平台实例。 | analysis-decision:SF-2026-ARXIV-2606-14832 |
| SF-2026-ARXIV-2606-14885 | score_7_9; potential_books_delta | not_selected | — | — | 它给 Ch75 一个清楚的 context-versus-environment state split，区别于普通 compression 或 RAG top-k。 | analysis-decision:SF-2026-ARXIV-2606-14885 |
| SF-2026-ARXIV-2606-14945 | score_7_9 | not_selected | — | — | Ch81 已明确 persistent interpreter/working state owner 与 recovery，故只保留 token-cost证据。 | analysis-decision:SF-2026-ARXIV-2606-14945 |
| SF-2026-ARXIV-2606-15004 | score_7_9 | not_selected | — | — | Ch66 已要求 simulator fidelity、kernel correctness identity 与 hardware contract；CREST 是嵌入式实例。 | analysis-decision:SF-2026-ARXIV-2606-15004 |
| SF-2026-ARXIV-2606-15008 | score_7_9 | not_selected | — | — | Ch82 collective risk 与 Ch72 deterministic authorizer 已覆盖聚合 authority；不重复写入。 | analysis-decision:SF-2026-ARXIV-2606-15008 |
| SF-2026-ARXIV-2606-15017 | score_7_9 | not_selected | — | — | Ch77 已有 experience serving按 task cost structure 选注入策略，本 family给出强负证据。 | analysis-decision:SF-2026-ARXIV-2606-15017 |
| SF-2026-ARXIV-2606-15020 | score_7_9; potential_books_delta | not_selected | — | — | 它扩展 Ch72 的 document-metadata boundary到整个 render/extract semantic supply chain，是可直接落位的新 ingest gate。 | analysis-decision:SF-2026-ARXIV-2606-15020 |
| SF-2026-ARXIV-2606-15029 | score_7_9 | not_selected | — | — | Ch66 已有 judge calibration、variance decomposition与budget allocation，该 subset策略是实现选项。 | analysis-decision:SF-2026-ARXIV-2606-15029 |
| SF-2026-ARXIV-2606-15034 | score_7_9 | not_selected | — | — | Ch66 已有 cross-layer evaluation与 trajectory judge action/outcome分层，Ch72已有 effect authorization；不重复。 | analysis-decision:SF-2026-ARXIV-2606-15034 |
| SF-2026-ARXIV-2606-17090 | score_7_9; potential_books_delta | not_selected | — | — | 它给 runtime target identity与版本验证提供少见的非CUDA实证，适合作为Ch50硬件分支而非声称 vLLM已支持ANE。 | analysis-decision:SF-2026-ARXIV-2606-17090 |
| SF-2026-ARXIV-2606-19376 | score_7_9 | not_selected | — | — | Ch56 已有 online outcome router、risk contract与SLO budget，本算法是受限实现。 | analysis-decision:SF-2026-ARXIV-2606-19376 |
| SF-2026-ARXIV-2606-20668 | score_7_9 | not_selected | — | — | Ch66 已有 Security Agent Cost-Success-Refusal curve与runtime coverage，本 benchmark直接填充证据，不扩展owner。 | analysis-decision:SF-2026-ARXIV-2606-20668 |
| SF-2026-ARXIV-2606-24898 | score_7_9; potential_books_delta | selected | DA-20260613-READOUT-BLIND-SPOT | — | 它揭示监督信号与runtime state的结构性盲区，独立于Agent安全与平台监控，构成今日第三个分析主线。 | analysis:DA-20260613-READOUT-BLIND-SPOT |

<!-- analysis-decision:SF-2026-ARXIV-2606-14106:start -->
它提供视觉 memory construction 的具体反例与替代表示，但系统 reach 小于 SOP 与 guardrail availability，因此保留而不进入三项 narrative。
<!-- analysis-decision:SF-2026-ARXIV-2606-14106:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14130:start -->
它强化 06-12 已写入 Ch72 的 model-bound shield，不新增独立 owner；因此不挤占今日三个互不重叠的 analysis slots。
<!-- analysis-decision:SF-2026-ARXIV-2606-14130:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14154:start -->
它为既有 Skill Security 增加 code-language composition blind spot，重要但仍是 SOP 之外的供应链子面。
<!-- analysis-decision:SF-2026-ARXIV-2606-14154:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14179:start -->
Ch33 已有 opaque harness trajectory capture、partial rollout 与 cross-policy reuse；该结果作为缓存 fidelity 的受限证据，不复制新段。
<!-- analysis-decision:SF-2026-ARXIV-2606-14179:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14200:start -->
它补足 Ch82 behavioral belief 与 authenticated identity 之间的 skill dimension，是今日多 Agent frontier 最清楚的 owner delta。
<!-- analysis-decision:SF-2026-ARXIV-2606-14200:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14239:start -->
Ch80/81 已有 decision history、fixed evaluator、promotion/rollback；本 family 是强证据 handoff，不再建立第二套 skill-evolution owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-14239:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14249:start -->
Ch81/84 已拥有 template/realized graph/trace、harness revision 与 promotion，故只保留 evidence，不复制 foundry taxonomy。
<!-- analysis-decision:SF-2026-ARXIV-2606-14249:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14275:start -->
它把 memory schema evolution 与 concurrent read consistency合并为存储 contract，超出现有 patch-history 段的范围，适合 Ch77 最小增量。
<!-- analysis-decision:SF-2026-ARXIV-2606-14275:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14350:start -->
这是对全书 system-first 方法的再表述，现有 Ch57 与 Ch56 已有 owner，故不新增正文。
<!-- analysis-decision:SF-2026-ARXIV-2606-14350:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14356:start -->
Ch56 已有 model/quantization/placement joint admission、risk contract 与 SLO budget，本 family 不再复制 selector。
<!-- analysis-decision:SF-2026-ARXIV-2606-14356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14445:start -->
Ch82 已有 typed public state 与 repository commitment protocol；tap 只提供一种实现实例。
<!-- analysis-decision:SF-2026-ARXIV-2606-14445:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14470:start -->
Ch77 已有 event sourcing、patch history 与 execution-state tree；本 family 的价值是负证据，不需另开机制段。
<!-- analysis-decision:SF-2026-ARXIV-2606-14470:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14474:start -->
Ch66 已把 simulator identity、hidden constraints、question budget 与 scorer 固定，本 proposal 只作概念 handoff。
<!-- analysis-decision:SF-2026-ARXIV-2606-14474:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14516:start -->
Ch66 Evaluation Card、claim provenance 和 evaluation identity 已覆盖该长期命题，仓库规模只作实现证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-14516:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14518:start -->
它为既有 source-level unlearning 增加 auditor threat model 与不可兼得边界，适合 Ch72 而非再写一种 unlearning algorithm。
<!-- analysis-decision:SF-2026-ARXIV-2606-14518:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14571:start -->
Ch66 已有 longitudinal fact-first 与 read/write audit；该 benchmark完善 slice，不改变 owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-14571:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14574:start -->
它补足 Ch79 从计划可执行到延迟危害的 state-machine gate，与普通最终成功率不同。
<!-- analysis-decision:SF-2026-ARXIV-2606-14574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14589:start -->
它把监控目标从异常计数推进到 narrative masking 与 seam ownership，是 Ch67 的直接长期增量。
<!-- analysis-decision:SF-2026-ARXIV-2606-14589:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14598:start -->
Ch35/50 已要求量化 artifact绑定 graph/kernel/hardware；该工作是很好的负/正实测，不需要 vLLM owner 新段。
<!-- analysis-decision:SF-2026-ARXIV-2606-14598:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14620:start -->
Ch24 已明确 parallel positions 在 commit 前可撤销以及 target commit owner，本 family校正测量语言但不新增机制。
<!-- analysis-decision:SF-2026-ARXIV-2606-14620:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14629:start -->
它把 Ch80 的 verifier authority 问题具体化为跨任务 regression gate，形成独立于今日安全/模型两项的 evolution evidence。
<!-- analysis-decision:SF-2026-ARXIV-2606-14629:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14672:start -->
Ch82 已规定 latent communication 不能删除 contract，因而该方法完全落在现有共存边界。
<!-- analysis-decision:SF-2026-ARXIV-2606-14672:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14674:start -->
Ch66 已固定 model×benchmark×harness×environment×scorer，并要求 component interaction audit，本 family不另建 schema。
<!-- analysis-decision:SF-2026-ARXIV-2606-14674:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14832:start -->
Ch78 已有 interface granularity、canonical effect 与独立 outcome contract；PhoneHarness 是平台实例。
<!-- analysis-decision:SF-2026-ARXIV-2606-14832:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14885:start -->
它给 Ch75 一个清楚的 context-versus-environment state split，区别于普通 compression 或 RAG top-k。
<!-- analysis-decision:SF-2026-ARXIV-2606-14885:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-14945:start -->
Ch81 已明确 persistent interpreter/working state owner 与 recovery，故只保留 token-cost证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-14945:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15004:start -->
Ch66 已要求 simulator fidelity、kernel correctness identity 与 hardware contract；CREST 是嵌入式实例。
<!-- analysis-decision:SF-2026-ARXIV-2606-15004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15008:start -->
Ch82 collective risk 与 Ch72 deterministic authorizer 已覆盖聚合 authority；不重复写入。
<!-- analysis-decision:SF-2026-ARXIV-2606-15008:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15017:start -->
Ch77 已有 experience serving按 task cost structure 选注入策略，本 family给出强负证据。
<!-- analysis-decision:SF-2026-ARXIV-2606-15017:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15020:start -->
它扩展 Ch72 的 document-metadata boundary到整个 render/extract semantic supply chain，是可直接落位的新 ingest gate。
<!-- analysis-decision:SF-2026-ARXIV-2606-15020:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15029:start -->
Ch66 已有 judge calibration、variance decomposition与budget allocation，该 subset策略是实现选项。
<!-- analysis-decision:SF-2026-ARXIV-2606-15029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-15034:start -->
Ch66 已有 cross-layer evaluation与 trajectory judge action/outcome分层，Ch72已有 effect authorization；不重复。
<!-- analysis-decision:SF-2026-ARXIV-2606-15034:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-17090:start -->
它给 runtime target identity与版本验证提供少见的非CUDA实证，适合作为Ch50硬件分支而非声称 vLLM已支持ANE。
<!-- analysis-decision:SF-2026-ARXIV-2606-17090:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19376:start -->
Ch56 已有 online outcome router、risk contract与SLO budget，本算法是受限实现。
<!-- analysis-decision:SF-2026-ARXIV-2606-19376:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-20668:start -->
Ch66 已有 Security Agent Cost-Success-Refusal curve与runtime coverage，本 benchmark直接填充证据，不扩展owner。
<!-- analysis-decision:SF-2026-ARXIV-2606-20668:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260613-AGENT-BROWSER-ORIGIN:start -->
### DA-20260613-AGENT-BROWSER-ORIGIN
传统 SOP 约束 script origin，却没有约束会读历史、跨页面推理并写入新页面的 Agent。安全 owner 必须沿 read→label→propagate→write 保存 origin，跨 origin 写入只有可信确认才能 commit；这也暴露了用户确认疲劳和标签传播误差。
<!-- analysis:DA-20260613-AGENT-BROWSER-ORIGIN:end -->

<!-- analysis:DA-20260613-GUARDRAIL-AVAILABILITY:start -->
### DA-20260613-GUARDRAIL-AVAILABILITY
Guardrail 不是免费前置函数。攻击者若能放大其 reasoning tokens，就能把安全层变成共享队列的 DoS 放大器；系统必须同时决定每次检查的计算上限、超限后的安全语义、隔离池和租户配额。
<!-- analysis:DA-20260613-GUARDRAIL-AVAILABILITY:end -->

<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:start -->
### DA-20260613-READOUT-BLIND-SPOT
Looped model 把 hidden state 变成跨步 runtime state，但 readout-invariant scale不会被每步交叉熵直接约束。训练 exit 与控制 recurrence 是两个目标：要么让 scale 对 loss 可见，要么从 recurrence中移除。
<!-- analysis:DA-20260613-READOUT-BLIND-SPOT:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-14027 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-14027 | delta:SF-2026-ARXIV-2606-14027 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14027 |
| SF-2026-ARXIV-2606-14106 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/76-rag.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-14106 | delta:SF-2026-ARXIV-2606-14106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14106 |
| SF-2026-ARXIV-2606-14130 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14130 | delta:SF-2026-ARXIV-2606-14130 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14130 |
| SF-2026-ARXIV-2606-14154 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-14154 | delta:SF-2026-ARXIV-2606-14154 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14154 |
| SF-2026-ARXIV-2606-14179 | TRAIN-GRPO | Books/part-04-training-system/33-grpo.md#L1 | Books/part-04-training-system/29-sft.md#L1; Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-14179 | delta:SF-2026-ARXIV-2606-14179 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14179 |
| SF-2026-ARXIV-2606-14200 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14200 | delta:SF-2026-ARXIV-2606-14200 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14200 |
| SF-2026-ARXIV-2606-14239 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/80-reflection.md#L1; Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-14239 | delta:SF-2026-ARXIV-2606-14239 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14239 |
| SF-2026-ARXIV-2606-14249 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/80-reflection.md#L1; Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-14249 | delta:SF-2026-ARXIV-2606-14249 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14249 |
| SF-2026-ARXIV-2606-14275 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/76-rag.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-14275 | delta:SF-2026-ARXIV-2606-14275 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14275 |
| SF-2026-ARXIV-2606-14350 | PLATFORM-FOUNDATIONS | Books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L1 | Books/part-05-inference-system/56-inference-scheduling.md#L1; Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-14350 | delta:SF-2026-ARXIV-2606-14350 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14350 |
| SF-2026-ARXIV-2606-14356 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/52-dynamo.md#L1; Books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-14356 | delta:SF-2026-ARXIV-2606-14356 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14356 |
| SF-2026-ARXIV-2606-14445 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14445 | delta:SF-2026-ARXIV-2606-14445 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14445 |
| SF-2026-ARXIV-2606-14470 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/76-rag.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-14470 | delta:SF-2026-ARXIV-2606-14470 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14470 |
| SF-2026-ARXIV-2606-14474 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14474 | delta:SF-2026-ARXIV-2606-14474 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14474 |
| SF-2026-ARXIV-2606-14516 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14516 | delta:SF-2026-ARXIV-2606-14516 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14516 |
| SF-2026-ARXIV-2606-14517 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-14517 | delta:SF-2026-ARXIV-2606-14517 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14517 |
| SF-2026-ARXIV-2606-14518 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-14518 | delta:SF-2026-ARXIV-2606-14518 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14518 |
| SF-2026-ARXIV-2606-14571 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14571 | delta:SF-2026-ARXIV-2606-14571 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14571 |
| SF-2026-ARXIV-2606-14574 | AGENT-PLANNING | Books/part-07-agent/79-planning.md#L1 | Books/part-07-agent/78-tool-calling.md#L1; Books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-14574 | delta:SF-2026-ARXIV-2606-14574 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14574 |
| SF-2026-ARXIV-2606-14589 | PLATFORM-MONITORING | Books/part-06-ai-infrastructure/67-monitoring.md#L1 | Books/part-06-ai-infrastructure/68-logging.md#L1; Books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-14589 | delta:SF-2026-ARXIV-2606-14589 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14589 |
| SF-2026-ARXIV-2606-14598 | INFER-VLLM | Books/part-05-inference-system/50-vllm.md#L1 | Books/part-05-inference-system/49-tensorrt-llm.md#L1; Books/part-05-inference-system/54-gpu-memory.md#L1 | existing:SF-2026-ARXIV-2606-14598 | delta:SF-2026-ARXIV-2606-14598 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14598 |
| SF-2026-ARXIV-2606-14620 | MULTIMODAL-GENERATIVE-PARADIGMS | Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | Books/part-02-model/18-decoder-only.md#L1; Books/part-05-inference-system/48-speculative-decoding.md#L1 | existing:SF-2026-ARXIV-2606-14620 | delta:SF-2026-ARXIV-2606-14620 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14620 |
| SF-2026-ARXIV-2606-14629 | AGENT-REFLECTION | Books/part-07-agent/80-reflection.md#L1 | Books/part-07-agent/77-memory.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-14629 | delta:SF-2026-ARXIV-2606-14629 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14629 |
| SF-2026-ARXIV-2606-14672 | AGENT-MULTI-AGENT | Books/part-07-agent/82-multi-agent.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14672 | delta:SF-2026-ARXIV-2606-14672 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14672 |
| SF-2026-ARXIV-2606-14674 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14674 | delta:SF-2026-ARXIV-2606-14674 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14674 |
| SF-2026-ARXIV-2606-14832 | AGENT-TOOL-CALLING | Books/part-07-agent/78-tool-calling.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-14832 | delta:SF-2026-ARXIV-2606-14832 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14832 |
| SF-2026-ARXIV-2606-14885 | AGENT-CONTEXT | Books/part-07-agent/75-context.md#L1 | Books/part-07-agent/76-rag.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-14885 | delta:SF-2026-ARXIV-2606-14885 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-14885 |
| SF-2026-ARXIV-2606-14945 | AGENT-WORKFLOW | Books/part-07-agent/81-workflow.md#L1 | Books/part-07-agent/80-reflection.md#L1; Books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-14945 | delta:SF-2026-ARXIV-2606-14945 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-14945 |
| SF-2026-ARXIV-2606-15004 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-15004 | delta:SF-2026-ARXIV-2606-15004 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15004 |
| SF-2026-ARXIV-2606-15008 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-15008 | delta:SF-2026-ARXIV-2606-15008 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15008 |
| SF-2026-ARXIV-2606-15017 | AGENT-MEMORY | Books/part-07-agent/77-memory.md#L1 | Books/part-07-agent/76-rag.md#L1; Books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-15017 | delta:SF-2026-ARXIV-2606-15017 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15017 |
| SF-2026-ARXIV-2606-15020 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1; Books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-15020 | delta:SF-2026-ARXIV-2606-15020 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-15020 |
| SF-2026-ARXIV-2606-15029 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-15029 | delta:SF-2026-ARXIV-2606-15029 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15029 |
| SF-2026-ARXIV-2606-15034 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-15034 | delta:SF-2026-ARXIV-2606-15034 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-15034 |
| SF-2026-ARXIV-2606-17090 | INFER-VLLM | Books/part-05-inference-system/50-vllm.md#L1 | Books/part-05-inference-system/49-tensorrt-llm.md#L1; Books/part-05-inference-system/54-gpu-memory.md#L1 | existing:SF-2026-ARXIV-2606-17090 | delta:SF-2026-ARXIV-2606-17090 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-17090 |
| SF-2026-ARXIV-2606-19376 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/52-dynamo.md#L1; Books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2606-19376 | delta:SF-2026-ARXIV-2606-19376 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19376 |
| SF-2026-ARXIV-2606-20668 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/67-monitoring.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-20668 | delta:SF-2026-ARXIV-2606-20668 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-20668 |
| SF-2026-ARXIV-2606-24898 | MODEL-DECODER-ONLY | Books/part-02-model/18-decoder-only.md#L1 | Books/part-02-model/17-transformer-layer.md#L1; Books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-24898 | delta:SF-2026-ARXIV-2606-24898 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24898 |

<!-- existing:SF-2026-ARXIV-2606-14027:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14027:end -->

<!-- delta:SF-2026-ARXIV-2606-14027:start -->
Agentic browser 的 origin policy 必须追踪 agent 读入数据的 origin label，在跨 origin 写入前由浏览器侧 detector 与 user confirmation gate 授权；传统 script-only SOP 不覆盖 agent 自身形成的数据通道。
<!-- delta:SF-2026-ARXIV-2606-14027:end -->

<!-- books-review:SF-2026-ARXIV-2606-14027:start -->
Relation `Direct Evolution`; disposition `Integrate`. 合成页面与 BrowserOS 实现不证明任意浏览器、隐式推断数据或用户确认都安全；label propagation 与用户疲劳仍会失效。
<!-- books-review:SF-2026-ARXIV-2606-14027:end -->

<!-- existing:SF-2026-ARXIV-2606-14106:start -->
Read owner `AGENT-MEMORY` at `Books/part-07-agent/77-memory.md` and adjacent chapters `Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14106:end -->

<!-- delta:SF-2026-ARXIV-2606-14106:start -->
GUI memory 不应保存整屏即视为更多证据；应把成功动作压缩成 action-relevant crop，并把正常 retrieval 与错误恢复 memory 分开，以避免视觉上下文把 state error 转成 grounding/hidden-operation error。
<!-- delta:SF-2026-ARXIV-2606-14106:end -->

<!-- books-review:SF-2026-ARXIV-2606-14106:start -->
Relation `Direct Evolution`; disposition `Integrate`. 裁剪和 recovery detector 都可能遗漏不可见 affordance；三套 GUI benchmark 不证明长期真实桌面 memory 的正确性。
<!-- books-review:SF-2026-ARXIV-2606-14106:end -->

<!-- existing:SF-2026-ARXIV-2606-14130:start -->
Read owner `AGENT-MULTI-AGENT` at `Books/part-07-agent/82-multi-agent.md` and adjacent chapters `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14130:end -->

<!-- delta:SF-2026-ARXIV-2606-14130:start -->
多 Agent shield 可从局部 LTL-safe obligations 通过 circular assume-guarantee fixed point 联合认证，再投影为各 agent action mask；selector 只能在已认证 contract library 中学习选择。
<!-- delta:SF-2026-ARXIV-2606-14130:end -->

<!-- books-review:SF-2026-ARXIV-2606-14130:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 证明只覆盖显式、可表示的模型和 certified library；nonstationary selector 不保证收敛，隐藏状态和环境漂移不在证明内。
<!-- books-review:SF-2026-ARXIV-2606-14130:end -->

<!-- existing:SF-2026-ARXIV-2606-14154:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14154:end -->

<!-- delta:SF-2026-ARXIV-2606-14154:start -->
Skill supply-chain audit 必须联合读取自然语言 SKILL.md 与可执行 code，因为两种模态可以分别无害、组合后才形成 payload；admission 需覆盖 13 类 cross-modal mutation 与 runtime effect。
<!-- delta:SF-2026-ARXIV-2606-14154:end -->

<!-- books-review:SF-2026-ARXIV-2606-14154:start -->
Relation `Direct Evolution`; disposition `Integrate`. 自动 mutation 与蒸馏轨迹只覆盖作者 taxonomy；静态 paired reading 仍不能证明运行时无动态依赖或 latent trigger。
<!-- books-review:SF-2026-ARXIV-2606-14154:end -->

<!-- existing:SF-2026-ARXIV-2606-14179:start -->
Read owner `TRAIN-GRPO` at `Books/part-04-training-system/33-grpo.md` and adjacent chapters `Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14179:end -->

<!-- delta:SF-2026-ARXIV-2606-14179:start -->
离线 tool-agent RL 可把 rollout 缓存分为精确/模糊/缺失层级，以 token mask 避免把 cache artifact 当 policy action，并让 reward 权重随 cache tier 改变。
<!-- delta:SF-2026-ARXIV-2606-14179:end -->

<!-- books-review:SF-2026-ARXIV-2606-14179:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 摘要明确报告强 SFT 后 RL 增益有限；fuzzy cache 改变环境反馈，不能替代 live tool execution 或跨 policy probability correction。
<!-- books-review:SF-2026-ARXIV-2606-14179:end -->

<!-- existing:SF-2026-ARXIV-2606-14200:start -->
Read owner `AGENT-MULTI-AGENT` at `Books/part-07-agent/82-multi-agent.md` and adjacent chapters `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14200:end -->

<!-- delta:SF-2026-ARXIV-2606-14200:start -->
Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。
<!-- delta:SF-2026-ARXIV-2606-14200:end -->

<!-- books-review:SF-2026-ARXIV-2606-14200:start -->
Relation `Direct Evolution`; disposition `Integrate`. 该机制不具 Sybil resistance，skill ontology 与冷启动证据会漂移；reputation 只能作为 routing sensor，不能认证 identity 或授权 effect。
<!-- books-review:SF-2026-ARXIV-2606-14200:end -->

<!-- existing:SF-2026-ARXIV-2606-14239:start -->
Read owner `AGENT-WORKFLOW` at `Books/part-07-agent/81-workflow.md` and adjacent chapters `Books/part-07-agent/80-reflection.md; Books/part-07-agent/82-multi-agent.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14239:end -->

<!-- delta:SF-2026-ARXIV-2606-14239:start -->
Skill evolution 可用同一 task 的 with/without-skill paired trajectory 隔离行为 delta，再让固定 structural verifier gate Refine/Repair 与 rollback。
<!-- delta:SF-2026-ARXIV-2606-14239:end -->

<!-- books-review:SF-2026-ARXIV-2606-14239:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 只可观察到的结构约束才能被 verifier 发现；paired runs 仍受模型随机性与 evaluator 共偏影响，不能证明 unobservable correctness。
<!-- books-review:SF-2026-ARXIV-2606-14239:end -->

<!-- existing:SF-2026-ARXIV-2606-14249:start -->
Read owner `AGENT-WORKFLOW` at `Books/part-07-agent/81-workflow.md` and adjacent chapters `Books/part-07-agent/80-reflection.md; Books/part-07-agent/82-multi-agent.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14249:end -->

<!-- delta:SF-2026-ARXIV-2606-14249:start -->
Harness 应表示成 model 与 configuration 的一等组合，生命周期 hooks、singleton slots 与 deterministic gates 共同定义可组合、可演进但可复现的运行身份。
<!-- delta:SF-2026-ARXIV-2606-14249:end -->

<!-- books-review:SF-2026-ARXIV-2606-14249:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. v1 只测 55-task SWE-bench subset、tau3 三域；meta-agents 未测试，joint-control assumption 受限，代码为 future release。
<!-- books-review:SF-2026-ARXIV-2606-14249:end -->

<!-- existing:SF-2026-ARXIV-2606-14275:start -->
Read owner `AGENT-MEMORY` at `Books/part-07-agent/77-memory.md` and adjacent chapters `Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14275:end -->

<!-- delta:SF-2026-ARXIV-2606-14275:start -->
层级知识库需要 path-indexed KV 原生持有 schema evolution：offline rewrite 以无 read-path lock 的一致性协议提交，budgeted navigation 在同一树上提供 anytime refinement。
<!-- delta:SF-2026-ARXIV-2606-14275:end -->

<!-- books-review:SF-2026-ARXIV-2606-14275:start -->
Relation `Direct Evolution`; disposition `Integrate`. 单一产品 workload 与 schema induction 不能证明任意 corpus 的一致性或答案真实性；offline rewrite、path churn 与导航预算仍可能制造 stale read。
<!-- books-review:SF-2026-ARXIV-2606-14275:end -->

<!-- existing:SF-2026-ARXIV-2606-14350:start -->
Read owner `PLATFORM-FOUNDATIONS` at `Books/part-06-ai-infrastructure/57-what-is-ai-platform.md` and adjacent chapters `Books/part-05-inference-system/56-inference-scheduling.md; Books/part-06-ai-infrastructure/66-evaluation-system.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14350:end -->

<!-- delta:SF-2026-ARXIV-2606-14350:start -->
Compound AI system 设计应先枚举 workflow topology，再在 component configuration 上管理 accuracy/latency/cost trade-off，而不是逐模型局部调参。
<!-- delta:SF-2026-ARXIV-2606-14350:end -->

<!-- books-review:SF-2026-ARXIV-2606-14350:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. case studies 不构成统一 optimizer 或生产 SLO；组合空间与 workload drift 仍需平台逐运行校准。
<!-- books-review:SF-2026-ARXIV-2606-14350:end -->

<!-- existing:SF-2026-ARXIV-2606-14356:start -->
Read owner `INFER-SCHEDULING` at `Books/part-05-inference-system/56-inference-scheduling.md` and adjacent chapters `Books/part-05-inference-system/52-dynamo.md; Books/part-06-ai-infrastructure/70-cost.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14356:end -->

<!-- delta:SF-2026-ARXIV-2606-14356:start -->
SLO-driven compound runtime 应把 task/data contract、可用 edge/cloud/space model profile 与 cooldown/threshold 状态交给在线 selector，而非固定一个最强模型。
<!-- delta:SF-2026-ARXIV-2606-14356:end -->

<!-- books-review:SF-2026-ARXIV-2606-14356:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 两条 workflow 与作者 profile 不能给通用 SLO；profiling drift、switching delay 与不可用 region 必须触发 fallback。
<!-- books-review:SF-2026-ARXIV-2606-14356:end -->

<!-- existing:SF-2026-ARXIV-2606-14445:start -->
Read owner `AGENT-MULTI-AGENT` at `Books/part-07-agent/82-multi-agent.md` and adjacent chapters `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14445:end -->

<!-- delta:SF-2026-ARXIV-2606-14445:start -->
异构 Agent 协作可用 markdown+metadata 文件作为 canonical message、文件路径作为 payload、notification 作为 signal，并以 git worktree 隔离并发修改。
<!-- delta:SF-2026-ARXIV-2606-14445:end -->

<!-- books-review:SF-2026-ARXIV-2606-14445:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 观察性单仓库且主要为 Claude/Codex，re-review 计数与成功无因果对应；文件协议不提供 authority、privacy 或 exactly-once delivery。
<!-- books-review:SF-2026-ARXIV-2606-14445:end -->

<!-- existing:SF-2026-ARXIV-2606-14470:start -->
Read owner `AGENT-MEMORY` at `Books/part-07-agent/77-memory.md` and adjacent chapters `Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14470:end -->

<!-- delta:SF-2026-ARXIV-2606-14470:start -->
Reasoning/memory 若以 commit、note 与 tag 保存可获得 replay/diff/merge，但准确率收益主要来自近重复检索；当 copyability 低于约 0.8 时，版本化 substrate 本身不产生方法迁移。
<!-- delta:SF-2026-ARXIV-2606-14470:end -->

<!-- books-review:SF-2026-ARXIV-2606-14470:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 负结果绑定模型、任务和 sampling budget；git lineage 提供可审计性，不证明记忆内容正确或新问题迁移。
<!-- books-review:SF-2026-ARXIV-2606-14470:end -->

<!-- existing:SF-2026-ARXIV-2606-14474:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14474:end -->

<!-- delta:SF-2026-ARXIV-2606-14474:start -->
User simulator 应拆成 persona、task contract、matched execution、trace、verification、feedback、refinement 七个可审计组件。
<!-- delta:SF-2026-ARXIV-2606-14474:end -->

<!-- books-review:SF-2026-ARXIV-2606-14474:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 没有生产实验或 population-validity 证明；persona fidelity、demographic bias 与 human-agent discrepancy 仍需独立数据。
<!-- books-review:SF-2026-ARXIV-2606-14474:end -->

<!-- existing:SF-2026-ARXIV-2606-14516:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14516:end -->

<!-- delta:SF-2026-ARXIV-2606-14516:start -->
Evaluation result 需要 source-agnostic result schema 与 instance-level output，把 model/benchmark/harness 元数据从分散 leaderboard 转成可复用 artifact。
<!-- delta:SF-2026-ARXIV-2606-14516:end -->

<!-- books-review:SF-2026-ARXIV-2606-14516:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 统一字段不保证 score 语义可比、数据新鲜或 provenance 完整；community ingestion 仍需 validation。
<!-- books-review:SF-2026-ARXIV-2606-14516:end -->

<!-- existing:SF-2026-ARXIV-2606-14517:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14517:end -->

<!-- delta:SF-2026-ARXIV-2606-14517:start -->
Reasoning guardrail 也必须有 token/time/concurrency budget 与 fail-closed/fail-open policy；否则攻击者可让安全模型陷入长推理并通过共享 guardrail queue 放大为租户级 DoS。
<!-- delta:SF-2026-ARXIV-2606-14517:end -->

<!-- books-review:SF-2026-ARXIV-2606-14517:start -->
Relation `Direct Evolution`; disposition `Integrate`. beam-search payload 与作者部署不提供真实流量发生率；硬 cap 会产生安全 false negative，独立容量池也增加成本。
<!-- books-review:SF-2026-ARXIV-2606-14517:end -->

<!-- existing:SF-2026-ARXIV-2606-14518:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14518:end -->

<!-- delta:SF-2026-ARXIV-2606-14518:start -->
Machine-unlearning audit 在互不信任 owner/auditor 下必须显式记录 audit leakage budget；只查询模型行为的通用 audit 对 convex models 无法同时识别 insufficient unlearning 且不泄露 retained-set membership。
<!-- delta:SF-2026-ARXIV-2606-14518:end -->

<!-- books-review:SF-2026-ARXIV-2606-14518:start -->
Relation `Direct Evolution`; disposition `Integrate`. 定理前提不覆盖所有深网、side information 或 cryptographic proof；行为审计失败也不证明某次 unlearning 合规。
<!-- books-review:SF-2026-ARXIV-2606-14518:end -->

<!-- existing:SF-2026-ARXIV-2606-14571:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14571:end -->

<!-- delta:SF-2026-ARXIV-2606-14571:start -->
Memory evaluation 要把 streaming observation→首次 evidence use→feedback incorporation→future reuse 拆成四个时序指标，不能用 stored 或单次 recall 代替未来辅助。
<!-- delta:SF-2026-ARXIV-2606-14571:end -->

<!-- books-review:SF-2026-ARXIV-2606-14571:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 两步序列和 egocentric stream 不能证明长期 identity/tenure；成功储存、局部 feedback incorporation 都不等于后续行为可靠。
<!-- books-review:SF-2026-ARXIV-2606-14571:end -->

<!-- existing:SF-2026-ARXIV-2606-14574:start -->
Read owner `AGENT-PLANNING` at `Books/part-07-agent/79-planning.md` and adjacent chapters `Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/80-reflection.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14574:end -->

<!-- delta:SF-2026-ARXIV-2606-14574:start -->
Executable planning evaluator 必须让 symbolic world model 区分 immediate precondition failure、latent hazard 与 irreversible failure，并在 action commit 前运行 counterfactual foresight。
<!-- delta:SF-2026-ARXIV-2606-14574:end -->

<!-- books-review:SF-2026-ARXIV-2606-14574:start -->
Relation `Direct Evolution`; disposition `Integrate`. 人工符号世界只覆盖可编码 kitchen semantics；counterfactual simulator 不证明真实环境 fidelity，漏建 hazard 会形成假安全。
<!-- books-review:SF-2026-ARXIV-2606-14574:end -->

<!-- existing:SF-2026-ARXIV-2606-14589:start -->
Read owner `PLATFORM-MONITORING` at `Books/part-06-ai-infrastructure/67-monitoring.md` and adjacent chapters `Books/part-06-ai-infrastructure/68-logging.md; Books/part-06-ai-infrastructure/69-trace.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14589:end -->

<!-- delta:SF-2026-ARXIV-2606-14589:start -->
Long-lived Agent 的 silent failure 应按 environment quirk、assumption mismatch、error swallowing、fail-plausible narrative、operational omission 分类，并要求错误跨组件边界后仍以可行动 evidence 到达人。
<!-- delta:SF-2026-ARXIV-2606-14589:end -->

<!-- books-review:SF-2026-ARXIV-2606-14589:start -->
Relation `Direct Evolution`; disposition `Integrate`. 单一私人 production runtime、人工 postmortem 与小样本不提供事故率；audit 擅长回归阻断而非 ex-ante 预防。
<!-- books-review:SF-2026-ARXIV-2606-14589:end -->

<!-- existing:SF-2026-ARXIV-2606-14598:start -->
Read owner `INFER-VLLM` at `Books/part-05-inference-system/50-vllm.md` and adjacent chapters `Books/part-05-inference-system/49-tensorrt-llm.md; Books/part-05-inference-system/54-gpu-memory.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14598:end -->

<!-- delta:SF-2026-ARXIV-2606-14598:start -->
低比特名义格式不等于执行了低比特 kernel；deployment contract 必须验证实际 int8×int8→int32 path、epilogue dequantization 与目标 GPU 的 native fast path。
<!-- delta:SF-2026-ARXIV-2606-14598:end -->

<!-- books-review:SF-2026-ARXIV-2606-14598:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. NF4 margin 基于 n=4 且 variance 未量化；结果只适用于 consumer Ampere shapes，不是跨 GPU 或质量通用结论。
<!-- books-review:SF-2026-ARXIV-2606-14598:end -->

<!-- existing:SF-2026-ARXIV-2606-14620:start -->
Read owner `MULTIMODAL-GENERATIVE-PARADIGMS` at `Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` and adjacent chapters `Books/part-02-model/18-decoder-only.md; Books/part-05-inference-system/48-speculative-decoding.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14620:end -->

<!-- delta:SF-2026-ARXIV-2606-14620:start -->
Masked diffusion LM 的 token commit order 必须从 sampler accept events 测量；大批 simultaneous commit 使 token-level order 部分未定义，所谓 block size 可能只是观测粒度。
<!-- delta:SF-2026-ARXIV-2606-14620:end -->

<!-- books-review:SF-2026-ARXIV-2606-14620:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 单一 checkpoint/sampler 的行为不定义整个 diffusion LM family；JSON、数学、事实任务间关系不可外推生产 latency。
<!-- books-review:SF-2026-ARXIV-2606-14620:end -->

<!-- existing:SF-2026-ARXIV-2606-14629:start -->
Read owner `AGENT-REFLECTION` at `Books/part-07-agent/80-reflection.md` and adjacent chapters `Books/part-07-agent/77-memory.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14629:end -->

<!-- delta:SF-2026-ARXIV-2606-14629:start -->
Self-improving VLM 的 verifier 更新必须与 policy update 分离，并用 held-out new-task slice 与 rollback gate 防止 verifier在旧任务提升时对新任务回退。
<!-- delta:SF-2026-ARXIV-2606-14629:end -->

<!-- books-review:SF-2026-ARXIV-2606-14629:start -->
Relation `Direct Evolution`; disposition `Integrate`. 同源 verifier、policy 与 synthetic data 会共偏；held-out task 仍可能与部署分布不同，改善旧任务不能授权 promotion。
<!-- books-review:SF-2026-ARXIV-2606-14629:end -->

<!-- existing:SF-2026-ARXIV-2606-14672:start -->
Read owner `AGENT-MULTI-AGENT` at `Books/part-07-agent/82-multi-agent.md` and adjacent chapters `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14672:end -->

<!-- delta:SF-2026-ARXIV-2606-14672:start -->
并行 Agent 分支可以把 branch output编码为 latent state 再直接合成，但 merge owner 必须保留 branch identity、可解码验证与文本 fallback。
<!-- delta:SF-2026-ARXIV-2606-14672:end -->

<!-- books-review:SF-2026-ARXIV-2606-14672:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. latent merge 隐藏语义冲突与 provenance，无法验证时必须回退显式 artifact；有限实验不证明跨模型可交换。
<!-- books-review:SF-2026-ARXIV-2606-14672:end -->

<!-- existing:SF-2026-ARXIV-2606-14674:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14674:end -->

<!-- delta:SF-2026-ARXIV-2606-14674:start -->
Embodied scaffold evaluation 应把 perception、memory、reasoning、reflection、action 与 learning 表示为 typed components，在固定接口下做 controlled composition。
<!-- delta:SF-2026-ARXIV-2606-14674:end -->

<!-- books-review:SF-2026-ARXIV-2606-14674:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 四个环境与标准接口会屏蔽真实 integration cost；模块 swap 的相对收益不等于生产系统可组合性。
<!-- books-review:SF-2026-ARXIV-2606-14674:end -->

<!-- existing:SF-2026-ARXIV-2606-14832:start -->
Read owner `AGENT-TOOL-CALLING` at `Books/part-07-agent/78-tool-calling.md` and adjacent chapters `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14832:end -->

<!-- delta:SF-2026-ARXIV-2606-14832:start -->
Phone Agent action surface 应在 GUI、device CLI 与 structured tools 间显式 routing，并让 observable side-effect verifier而非 plausible response拥有完成判断。
<!-- delta:SF-2026-ARXIV-2606-14832:end -->

<!-- books-review:SF-2026-ARXIV-2606-14832:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 单一 mobile harness 与 bounded GUI delegation 不证明权限、安全或跨设备可移植；deterministic router仍会误选 action surface。
<!-- books-review:SF-2026-ARXIV-2606-14832:end -->

<!-- existing:SF-2026-ARXIV-2606-14885:start -->
Read owner `AGENT-CONTEXT` at `Books/part-07-agent/75-context.md` and adjacent chapters `Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14885:end -->

<!-- delta:SF-2026-ARXIV-2606-14885:start -->
大语料 Agent 不应让 full-corpus shell 与 retriever二选一；retriever负责把候选拉入可持久 workspace，Agent只在局部 workspace做可组合 DCI，并让 context reset 保留 workspace state。
<!-- delta:SF-2026-ARXIV-2606-14885:end -->

<!-- books-review:SF-2026-ARXIV-2606-14885:start -->
Relation `Direct Evolution`; disposition `Integrate`. retriever recall仍是上限，workspace会累积错误/污染与磁盘成本；公开 QA 不证明企业 ACL、更新或多租户一致性。
<!-- books-review:SF-2026-ARXIV-2606-14885:end -->

<!-- existing:SF-2026-ARXIV-2606-14945:start -->
Read owner `AGENT-WORKFLOW` at `Books/part-07-agent/81-workflow.md` and adjacent chapters `Books/part-07-agent/80-reflection.md; Books/part-07-agent/82-multi-agent.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-14945:end -->

<!-- delta:SF-2026-ARXIV-2606-14945:start -->
Autonomous experimentation 可把 typed persistent experiment history 与 bounded conversation window分离，使每轮不必重读全部历史。
<!-- delta:SF-2026-ARXIV-2606-14945:end -->

<!-- books-review:SF-2026-ARXIV-2606-14945:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 两个 LangGraph benchmark不证明长期 state正确、并发安全或恢复；固定窗口可能隐藏决定性旧证据。
<!-- books-review:SF-2026-ARXIV-2606-14945:end -->

<!-- existing:SF-2026-ARXIV-2606-15004:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15004:end -->

<!-- delta:SF-2026-ARXIV-2606-15004:start -->
Embedded NAS 的 evaluation identity 必须联合 model architecture、target MCU、runtime schedule、quantization 与 policy，并用 HIL measurement/replay替代 FLOPs proxy。
<!-- delta:SF-2026-ARXIV-2606-15004:end -->

<!-- books-review:SF-2026-ARXIV-2606-15004:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 三个 MCU 与两类 sensing workload 不构成跨芯片 Pareto；HIL 搜索昂贵且 firmware/toolchain drift 会改变结果。
<!-- books-review:SF-2026-ARXIV-2606-15004:end -->

<!-- existing:SF-2026-ARXIV-2606-15008:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15008:end -->

<!-- delta:SF-2026-ARXIV-2606-15008:start -->
Execution-coupled multi-Agent security要把 aggregation policy 当攻击放大器：any-one proposal 规则使最脆弱 agent 决定系统 exposure，consensus/routing才改变 commit threshold。
<!-- delta:SF-2026-ARXIV-2606-15008:end -->

<!-- books-review:SF-2026-ARXIV-2606-15008:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. OpenClaw配置与归一化风险指标依作者假设；实验发生率不是生产 breach probability，consensus也可能共谋或停摆。
<!-- books-review:SF-2026-ARXIV-2606-15008:end -->

<!-- existing:SF-2026-ARXIV-2606-15017:start -->
Read owner `AGENT-MEMORY` at `Books/part-07-agent/77-memory.md` and adjacent chapters `Books/part-07-agent/76-rag.md; Books/part-07-agent/81-workflow.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15017:end -->

<!-- delta:SF-2026-ARXIV-2606-15017:start -->
在线 skill/memory module 必须在固定 total inference token budget下与 extra actor steps比较，并报告 run-to-run variance；module gross gain 不是净 utility。
<!-- delta:SF-2026-ARXIV-2606-15017:end -->

<!-- books-review:SF-2026-ARXIV-2606-15017:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 只覆盖 AWM/ASI/ReasoningBank 与所测域；负结果不证明离线复用、昂贵失败或其他 cost structure 下 memory无价值。
<!-- books-review:SF-2026-ARXIV-2606-15017:end -->

<!-- existing:SF-2026-ARXIV-2606-15020:start -->
Read owner `PLATFORM-SECURITY` at `Books/part-06-ai-infrastructure/72-security.md` and adjacent chapters `Books/part-06-ai-infrastructure/66-evaluation-system.md; Books/part-07-agent/78-tool-calling.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15020:end -->

<!-- delta:SF-2026-ARXIV-2606-15020:start -->
Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。
<!-- delta:SF-2026-ARXIV-2606-15020:end -->

<!-- books-review:SF-2026-ARXIV-2606-15020:start -->
Relation `Direct Evolution`; disposition `Integrate`. scanner规则只覆盖已知25类且可能误报；双视图一致也不证明文档真实或模型安全，动态/OCR路径仍需独立审计。
<!-- books-review:SF-2026-ARXIV-2606-15020:end -->

<!-- existing:SF-2026-ARXIV-2606-15029:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15029:end -->

<!-- delta:SF-2026-ARXIV-2606-15029:start -->
Judge reliability 在 human label预算有限时可选择 synthetic-label metric匹配的 subset，再把估计问题与是否越过 deployment threshold的分类问题分开。
<!-- delta:SF-2026-ARXIV-2606-15029:end -->

<!-- books-review:SF-2026-ARXIV-2606-15029:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. synthetic labels与judge可能共偏，subset matching不保证稀有 failure coverage；医疗成本case不构成通用标注价格。
<!-- books-review:SF-2026-ARXIV-2606-15029:end -->

<!-- existing:SF-2026-ARXIV-2606-15034:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-15034:end -->

<!-- delta:SF-2026-ARXIV-2606-15034:start -->
Computer-use safety必须同时测 action-level allowed/unrelated/unsafe判断和risk-augmented end-to-end state invariant，nominal task success不能覆盖unsafe shortcut。
<!-- delta:SF-2026-ARXIV-2606-15034:end -->

<!-- books-review:SF-2026-ARXIV-2606-15034:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 手工hazard与predicate不完备，局部guardrail分数不证明端到端安全，新增invariant也可能拒绝合法路径。
<!-- books-review:SF-2026-ARXIV-2606-15034:end -->

<!-- existing:SF-2026-ARXIV-2606-17090:start -->
Read owner `INFER-VLLM` at `Books/part-05-inference-system/50-vllm.md` and adjacent chapters `Books/part-05-inference-system/49-tensorrt-llm.md; Books/part-05-inference-system/54-gpu-memory.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-17090:end -->

<!-- delta:SF-2026-ARXIV-2606-17090:start -->
Apple ANE runtime 的执行身份必须绑定 macOS/ANE compiler版本与实际dispatch target；direct graph/program路径才能区分“允许调度到ANE”与“确认在ANE执行”。
<!-- delta:SF-2026-ARXIV-2606-17090:end -->

<!-- books-review:SF-2026-ARXIV-2606-17090:start -->
Relation `Direct Evolution`; disposition `Integrate`. 依赖私有/版本敏感 daemon与compiler，release可能随OS失效；microbench与reference matching不证明完整训练稳定性或通用模型支持。
<!-- books-review:SF-2026-ARXIV-2606-17090:end -->

<!-- existing:SF-2026-ARXIV-2606-19376:start -->
Read owner `INFER-SCHEDULING` at `Books/part-05-inference-system/56-inference-scheduling.md` and adjacent chapters `Books/part-05-inference-system/52-dynamo.md; Books/part-06-ai-infrastructure/70-cost.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-19376:end -->

<!-- delta:SF-2026-ARXIV-2606-19376:start -->
LLM router 可在稀疏、单侧 user feedback下在线学习cost policy，同时把满意度SLA作为约束而非平均reward。
<!-- delta:SF-2026-ARXIV-2606-19376:end -->

<!-- books-review:SF-2026-ARXIV-2606-19376:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 理论保证依赖反馈与可行性假设；offline benchmark satisfaction不是生产SLA，delayed/strategic feedback会破坏校准。
<!-- books-review:SF-2026-ARXIV-2606-19376:end -->

<!-- existing:SF-2026-ARXIV-2606-20668:start -->
Read owner `PLATFORM-EVALUATION-SYSTEM` at `Books/part-06-ai-infrastructure/66-evaluation-system.md` and adjacent chapters `Books/part-06-ai-infrastructure/67-monitoring.md; Books/part-06-ai-infrastructure/72-security.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-20668:end -->

<!-- delta:SF-2026-ARXIV-2606-20668:start -->
Guardrail选择必须在同一合同联合测 detection、false positive、latency与monetary cost，并分开content moderation与jailbreak detection Pareto frontier。
<!-- delta:SF-2026-ARXIV-2606-20668:end -->

<!-- books-review:SF-2026-ARXIV-2606-20668:start -->
Relation `Principle Reuse`; disposition `No Change — Existing Coverage`. in-house/paraphrased data仍可能有generator fingerprint与vendor drift；公开点估计不是生产SLO或安全认证。
<!-- books-review:SF-2026-ARXIV-2606-20668:end -->

<!-- existing:SF-2026-ARXIV-2606-24898:start -->
Read owner `MODEL-DECODER-ONLY` at `Books/part-02-model/18-decoder-only.md` and adjacent chapters `Books/part-02-model/17-transformer-layer.md; Books/part-04-training-system/28-pretraining.md`; existing mechanism and fallback were compared against exact-v1.
<!-- existing:SF-2026-ARXIV-2606-24898:end -->

<!-- delta:SF-2026-ARXIV-2606-24898:start -->
Looped LM 的dense per-loop cross-entropy只控制readout可见变量；RMSNorm/LayerNorm隐藏radial scale时，recurrent residual仍携带scale，必须让scale对loss可见或从recurrence移除。
<!-- delta:SF-2026-ARXIV-2606-24898:end -->

<!-- books-review:SF-2026-ARXIV-2606-24898:start -->
Relation `Direct Evolution`; disposition `Integrate`. 两种小规模looped模型与variable-depth benchmark不证明所有recurrent architecture；norm稳定也不保证语义correctness或大规模收敛。
<!-- books-review:SF-2026-ARXIV-2606-24898:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260613-COVERAGE-V1 | fresh-context:jun13-v1 | coverage | coverage:SRC-ARXIV:20260613 | — | 434/434 title+abstract; 80/80 route-negative FN audit; denominator 38; closures 396; 15007 owner conflict closed | passed |
| SA-20260613-EVIDENCE-V1 | fresh-context:jun13-v1 | evidence | review:SF-2026-ARXIV-2606-14027; review:SF-2026-ARXIV-2606-14106; review:SF-2026-ARXIV-2606-14130; review:SF-2026-ARXIV-2606-14154; review:SF-2026-ARXIV-2606-14179; review:SF-2026-ARXIV-2606-14200; review:SF-2026-ARXIV-2606-14239; review:SF-2026-ARXIV-2606-14249; review:SF-2026-ARXIV-2606-14275; review:SF-2026-ARXIV-2606-14350; review:SF-2026-ARXIV-2606-14356; review:SF-2026-ARXIV-2606-14445; review:SF-2026-ARXIV-2606-14470; review:SF-2026-ARXIV-2606-14474; review:SF-2026-ARXIV-2606-14516; review:SF-2026-ARXIV-2606-14517; review:SF-2026-ARXIV-2606-14518; review:SF-2026-ARXIV-2606-14571; review:SF-2026-ARXIV-2606-14574; review:SF-2026-ARXIV-2606-14589; review:SF-2026-ARXIV-2606-14598; review:SF-2026-ARXIV-2606-14620; review:SF-2026-ARXIV-2606-14629; review:SF-2026-ARXIV-2606-14672; review:SF-2026-ARXIV-2606-14674; review:SF-2026-ARXIV-2606-14832; review:SF-2026-ARXIV-2606-14885; review:SF-2026-ARXIV-2606-14945; review:SF-2026-ARXIV-2606-15004; review:SF-2026-ARXIV-2606-15008; review:SF-2026-ARXIV-2606-15017; review:SF-2026-ARXIV-2606-15020; review:SF-2026-ARXIV-2606-15029; review:SF-2026-ARXIV-2606-15034; review:SF-2026-ARXIV-2606-17090; review:SF-2026-ARXIV-2606-19376; review:SF-2026-ARXIV-2606-20668; review:SF-2026-ARXIV-2606-24898 | — | 38/38 official exact-v1 Method/Evaluation/Limitations and benchmark contracts; all undisclosed execution fields remain Not Disclosed | passed |
| SA-20260613-SELECTION-V1 | fresh-context:jun13-v1 | deep_analysis_selection | analysis:DA-20260613-AGENT-BROWSER-ORIGIN; analysis-decision:SF-2026-ARXIV-2606-14106; analysis-decision:SF-2026-ARXIV-2606-14130; analysis-decision:SF-2026-ARXIV-2606-14154; analysis-decision:SF-2026-ARXIV-2606-14179; analysis-decision:SF-2026-ARXIV-2606-14200; analysis-decision:SF-2026-ARXIV-2606-14239; analysis-decision:SF-2026-ARXIV-2606-14249; analysis-decision:SF-2026-ARXIV-2606-14275; analysis-decision:SF-2026-ARXIV-2606-14350; analysis-decision:SF-2026-ARXIV-2606-14356; analysis-decision:SF-2026-ARXIV-2606-14445; analysis-decision:SF-2026-ARXIV-2606-14470; analysis-decision:SF-2026-ARXIV-2606-14474; analysis-decision:SF-2026-ARXIV-2606-14516; analysis:DA-20260613-GUARDRAIL-AVAILABILITY; analysis-decision:SF-2026-ARXIV-2606-14518; analysis-decision:SF-2026-ARXIV-2606-14571; analysis-decision:SF-2026-ARXIV-2606-14574; analysis-decision:SF-2026-ARXIV-2606-14589; analysis-decision:SF-2026-ARXIV-2606-14598; analysis-decision:SF-2026-ARXIV-2606-14620; analysis-decision:SF-2026-ARXIV-2606-14629; analysis-decision:SF-2026-ARXIV-2606-14672; analysis-decision:SF-2026-ARXIV-2606-14674; analysis-decision:SF-2026-ARXIV-2606-14832; analysis-decision:SF-2026-ARXIV-2606-14885; analysis-decision:SF-2026-ARXIV-2606-14945; analysis-decision:SF-2026-ARXIV-2606-15004; analysis-decision:SF-2026-ARXIV-2606-15008; analysis-decision:SF-2026-ARXIV-2606-15017; analysis-decision:SF-2026-ARXIV-2606-15020; analysis-decision:SF-2026-ARXIV-2606-15029; analysis-decision:SF-2026-ARXIV-2606-15034; analysis-decision:SF-2026-ARXIV-2606-17090; analysis-decision:SF-2026-ARXIV-2606-19376; analysis-decision:SF-2026-ARXIV-2606-20668; analysis:DA-20260613-READOUT-BLIND-SPOT | — | 38/38 frontier; winners frozen before 38 source-specific rationales | passed |
| SA-20260613-BOOKS-POSTWRITE-V1 | fresh-context:jun13-v1 | books | books-review:SF-2026-ARXIV-2606-14027; books-review:SF-2026-ARXIV-2606-14106; books-review:SF-2026-ARXIV-2606-14130; books-review:SF-2026-ARXIV-2606-14154; books-review:SF-2026-ARXIV-2606-14179; books-review:SF-2026-ARXIV-2606-14200; books-review:SF-2026-ARXIV-2606-14239; books-review:SF-2026-ARXIV-2606-14249; books-review:SF-2026-ARXIV-2606-14275; books-review:SF-2026-ARXIV-2606-14350; books-review:SF-2026-ARXIV-2606-14356; books-review:SF-2026-ARXIV-2606-14445; books-review:SF-2026-ARXIV-2606-14470; books-review:SF-2026-ARXIV-2606-14474; books-review:SF-2026-ARXIV-2606-14516; books-review:SF-2026-ARXIV-2606-14517; books-review:SF-2026-ARXIV-2606-14518; books-review:SF-2026-ARXIV-2606-14571; books-review:SF-2026-ARXIV-2606-14574; books-review:SF-2026-ARXIV-2606-14589; books-review:SF-2026-ARXIV-2606-14598; books-review:SF-2026-ARXIV-2606-14620; books-review:SF-2026-ARXIV-2606-14629; books-review:SF-2026-ARXIV-2606-14672; books-review:SF-2026-ARXIV-2606-14674; books-review:SF-2026-ARXIV-2606-14832; books-review:SF-2026-ARXIV-2606-14885; books-review:SF-2026-ARXIV-2606-14945; books-review:SF-2026-ARXIV-2606-15004; books-review:SF-2026-ARXIV-2606-15008; books-review:SF-2026-ARXIV-2606-15017; books-review:SF-2026-ARXIV-2606-15020; books-review:SF-2026-ARXIV-2606-15029; books-review:SF-2026-ARXIV-2606-15034; books-review:SF-2026-ARXIV-2606-17090; books-review:SF-2026-ARXIV-2606-19376; books-review:SF-2026-ARXIV-2606-20668; books-review:SF-2026-ARXIV-2606-24898 | — | 14/14 Integrate writebacks in 9 owners and 24/24 No Change handoffs passed fresh audit; unresolved findings 0 | passed |

## 8. Ignored Noise

The 396 closures remain row-addressable in `denominator-full-semantic-audit-v1.tsv`; keyword routes were recall aids only, all 80 route-negative identities were closed, and `2606.15007v1` remains a historical-owner closure rather than a new family.

### Materials and Access

- Discovery identity/timestamp/category/title/abstract comes from frozen DataCite snapshots.
- 38/38 retained families were read from official version-bound `https://arxiv.org/html/<id>v1`; every page exposed an exact `arXiv:<id>v1` header.
- Local curl and the in-app browser were unavailable, but this was not a material blocker after the primary-source web reader recovered all 38 exact-v1 pages.

## 9. Recommended Action

- `Integrate`: 14 families, deduplicated into 9 owner-file writes in `BOOKS_INTEGRATION_QUEUE_V1.md` and `READY_TO_INSERT_BOOKS_V1.md`.
- `No Change — Existing Coverage`: 24 families; each has a source-specific handoff above.
- Books Gate Passed after root wrote the nine owner-merged deltas and this lane completed the 38/38 post-write fresh audit.

## 10. Repository Changes

- This lane created only the 2026-06-13 Daily, source packet and dedicated finalizer.
- Root serialized the nine approved owner-file changes; this presentation migration did not modify, stage, commit or push shared Books.

## 11. Open Questions

- How can browser-origin labels survive lossy model transformations without overblocking legitimate user-approved transfer?
- Which guardrail timeout semantics minimize both denial-of-service and unsafe fail-open behavior under shared load?
- At what model scale do looped-state readout blind spots cease to follow the 44M/129M evidence?
- These are research continuations, not unresolved Gate blockers.

## 12. Sources

- [Same-Origin Policy for Agentic Browsers](https://arxiv.org/abs/2606.14027v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Naive Visual Memory is Not Enough: A Failure-Mode Study of GUI Agents](https://arxiv.org/abs/2606.14106v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Contract-Based Compositional Shielding for Safe Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2606.14130v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [SkillMutator: Benchmarking and Defending Language-and-Code Cross-modal Attacks on LLM Agent Skills](https://arxiv.org/abs/2606.14154v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and Hybrid Reward](https://arxiv.org/abs/2606.14179v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms](https://arxiv.org/abs/2606.14200v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [SkillAudit: Ground-Truth-Free Skill Evolution via Paired Trajectory Auditing](https://arxiv.org/abs/2606.14239v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry](https://arxiv.org/abs/2606.14249v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [WikiKV: Schema-Evolving Path-Indexed Storage for Hierarchical Knowledge Navigation](https://arxiv.org/abs/2606.14275v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Design Methodology and Performance Trade-offs Management for Distributed and Compound AI Systems](https://arxiv.org/abs/2606.14350v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [PLAIground: SLO-Driven Runtime Model Selection for Compound AI Systems in the Edge-Cloud-Space Continuum](https://arxiv.org/abs/2606.14356v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration](https://arxiv.org/abs/2606.14445v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge](https://arxiv.org/abs/2606.14470v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Verifiable User Simulation for Search and Recommendation Systems](https://arxiv.org/abs/2606.14474v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Every Eval Ever: A Unifying Schema and Community Repository for AI Evaluation Results](https://arxiv.org/abs/2606.14516v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails](https://arxiv.org/abs/2606.14517v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Behavioral Audit of Machine Unlearning Has a Privacy Cost](https://arxiv.org/abs/2606.14518v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [StreamMemBench: Streaming Evaluation of Agent Memory for Future-Oriented Assistance](https://arxiv.org/abs/2606.14571v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model](https://arxiv.org/abs/2606.14574v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime](https://arxiv.org/abs/2606.14589v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Realizing Native INT8 Compute for Diffusion Transformers on Consumer GPUs: A Fused INT8 GEMM Kernel for Ideogram 4.0](https://arxiv.org/abs/2606.14598v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Neither Parallel Nor Sequential: How DiffusionGemma Actually Commits Tokens](https://arxiv.org/abs/2606.14620v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [When Good Verifiers Go Bad: Self-Improving VLMs Can Regress on New Tasks](https://arxiv.org/abs/2606.14629v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows](https://arxiv.org/abs/2606.14672v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [AgentSpec: Understanding Embodied Agent Scaffolds Through Controlled Composition](https://arxiv.org/abs/2606.14674v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [PhoneHarness: Harnessing Phone-Use Agents through Mixed GUI, CLI, and Tool Actions](https://arxiv.org/abs/2606.14832v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Dr-DCI: Scaling Direct Corpus Interaction via Dynamic Workspace Expansion](https://arxiv.org/abs/2606.14885v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Remember, Don't Re-read: Stateful ReAct Agents for Token-Efficient Autonomous Experimentation](https://arxiv.org/abs/2606.14945v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [CREST: Deployment-Realistic Hardware-in-the-Loop NAS for Embedded Sensing Systems](https://arxiv.org/abs/2606.15004v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations](https://arxiv.org/abs/2606.15008v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Are Online Skill and Memory Modules Always Worth Their Tokens? A Budget-Constrained Study of Web Agents](https://arxiv.org/abs/2606.15017v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Semantic Integrity Failures in Document-to-LLM Supply Chains](https://arxiv.org/abs/2606.15020v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Metric Match: A Subset Selection Approach to Evaluating LLM Judge Reliability](https://arxiv.org/abs/2606.15029v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [OSGuard: A Benchmark for Safety in Computer-Use Agents](https://arxiv.org/abs/2606.15034v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [ANEForge: Python for direct computation on the Apple Neural Engine](https://arxiv.org/abs/2606.17090v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Cost-Optimal LLM Routing with Limited User Feedback under User Satisfaction Guarantees](https://arxiv.org/abs/2606.19376v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](https://arxiv.org/abs/2606.20668v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models](https://arxiv.org/abs/2606.24898v1) — first-public（Asia/Shanghai）：2026-06-12；accessed：2026-08-30
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表
- Date-local receipts：`../_sources/daily-20260613/source-review-receipts-v2.1.json`、`deep-analysis-selection-v1.json`、`books-comparison-v1.json`、`POST_WRITE_FRESH_AUDIT_V1.md`

## 13. Final Status

Daily V2.1 的 Coverage=`Closed`、Evidence=`Passed`、Books=`Passed`；Completion Status=`Complete`。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。
