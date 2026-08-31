# Daily Research — 2026-06-21

**Research Date:** 2026-06-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-20 09:00:00 ～ 2026-06-21 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；224/224 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary
> Strict V2.1 Daily for `DEN-20260621-83b5c89e`. Coverage, Evidence, Selection and Books passed after root writeback and the 37/37 post-write fresh audit.

Beijing window `[2026-06-20 09:00, 2026-06-21 09:00)` contains 224 registered identities. Full 224/224 title+abstract screening freezes 37 durable families and 187 family-specific closures. Official exact-v1 HTML was reviewed for 37/37 families. Full-frontier selection freezes three winners before rationale. Books comparison yields 20 Integrate proposals and 17 No Change handoffs.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-21 |
| Window End | 2026-06-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260621-83b5c89e |
| Denominator Frozen At | 2026-08-30T01:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-20T09:00:00+08:00 | 2026-06-21T09:00:00+08:00 | 2026-08-30T01:20:00+08:00 | frozen DataCite prefix snapshots; exact-v1 UTC window; all registered categories | checked | 224 | SF-2026-ARXIV-2606-21822; SF-2026-ARXIV-2606-21836; SF-2026-ARXIV-2606-21842; SF-2026-ARXIV-2606-21843; SF-2026-ARXIV-2606-21848; SF-2026-ARXIV-2606-21854; SF-2026-ARXIV-2606-21856; SF-2026-ARXIV-2606-21868; SF-2026-ARXIV-2606-21869; SF-2026-ARXIV-2606-21875; SF-2026-ARXIV-2606-21877; SF-2026-ARXIV-2606-21884; SF-2026-ARXIV-2606-21891; SF-2026-ARXIV-2606-21917; SF-2026-ARXIV-2606-21954; SF-2026-ARXIV-2606-21959; SF-2026-ARXIV-2606-21963; SF-2026-ARXIV-2606-21968; SF-2026-ARXIV-2606-21994; SF-2026-ARXIV-2606-22000; SF-2026-ARXIV-2606-22013; SF-2026-ARXIV-2606-22019; SF-2026-ARXIV-2606-22030; SF-2026-ARXIV-2606-22043; SF-2026-ARXIV-2606-22082; SF-2026-ARXIV-2606-22085; SF-2026-ARXIV-2606-22136; SF-2026-ARXIV-2606-22142; SF-2026-ARXIV-2606-22164; SF-2026-ARXIV-2606-22175; SF-2026-ARXIV-2606-22179; SF-2026-ARXIV-2606-22180; SF-2026-ARXIV-2606-22189; SF-2026-ARXIV-2606-22203; SF-2026-ARXIV-2606-22248; SF-2026-ARXIV-2606-22263; SF-2026-ARXIV-2606-22283 | pages=40; final_cursor=end; 224 unique identities | 2026-06-21T01:00:00Z | ../_sources/daily-20260621/screening-ledger.json; ../_sources/daily-20260621/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260621 | — |

<!-- coverage:SRC-ARXIV:20260621:start -->
All 149 Core, 21 keyword-routed and 54 route-negative identities were screened. Frozen arithmetic: `224 = 37 retained + 187 closures`. Route reconciliation: `{"core_daily_semantic_review_required": {"closure": 117, "raw": 149, "retained": 32}, "keyword_daily_semantic_review_required": {"closure": 17, "raw": 21, "retained": 4}, "not_routed_by_keyword_contract": {"closure": 53, "raw": 54, "retained": 1}}`. Keyword routing was recall-only.
<!-- coverage:SRC-ARXIV:20260621:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21822 | arXiv:2606.21822v1 | paper-v1:2606.21822 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21822 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21822 | yes |
| SF-2026-ARXIV-2606-21836 | arXiv:2606.21836v1 | paper-v1:2606.21836 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21836 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21836 | yes |
| SF-2026-ARXIV-2606-21842 | arXiv:2606.21842v1 | paper-v1:2606.21842 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21842 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21842 | yes |
| SF-2026-ARXIV-2606-21843 | arXiv:2606.21843v1 | paper-v1:2606.21843 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21843 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-21843 | yes |
| SF-2026-ARXIV-2606-21848 | arXiv:2606.21848v1 | paper-v1:2606.21848 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21848 | self | — | new_in_window | MODEL-SELF-ATTENTION | Integrate | books-review:SF-2026-ARXIV-2606-21848 | yes |
| SF-2026-ARXIV-2606-21854 | arXiv:2606.21854v1 | paper-v1:2606.21854 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21854 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21854 | yes |
| SF-2026-ARXIV-2606-21856 | arXiv:2606.21856v1 | paper-v1:2606.21856 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21856 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21856 | yes |
| SF-2026-ARXIV-2606-21868 | arXiv:2606.21868v1 | paper-v1:2606.21868 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21868 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-21868 | yes |
| SF-2026-ARXIV-2606-21869 | arXiv:2606.21869v1 | paper-v1:2606.21869 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21869 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-21869 | yes |
| SF-2026-ARXIV-2606-21875 | arXiv:2606.21875v1 | paper-v1:2606.21875 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21875 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21875 | yes |
| SF-2026-ARXIV-2606-21877 | arXiv:2606.21877v1 | paper-v1:2606.21877 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21877 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-21877 | yes |
| SF-2026-ARXIV-2606-21884 | arXiv:2606.21884v1 | paper-v1:2606.21884 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21884 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-21884 | yes |
| SF-2026-ARXIV-2606-21891 | arXiv:2606.21891v1 | paper-v1:2606.21891 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21891 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-21891 | yes |
| SF-2026-ARXIV-2606-21917 | arXiv:2606.21917v1 | paper-v1:2606.21917 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21917 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21917 | yes |
| SF-2026-ARXIV-2606-21954 | arXiv:2606.21954v1 | paper-v1:2606.21954 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21954 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-21954 | yes |
| SF-2026-ARXIV-2606-21959 | arXiv:2606.21959v1 | paper-v1:2606.21959 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21959 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21959 | yes |
| SF-2026-ARXIV-2606-21963 | arXiv:2606.21963v1 | paper-v1:2606.21963 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21963 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21963 | yes |
| SF-2026-ARXIV-2606-21968 | arXiv:2606.21968v1 | paper-v1:2606.21968 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-21968 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-21968 | yes |
| SF-2026-ARXIV-2606-21994 | arXiv:2606.21994v1 | paper-v1:2606.21994 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-21994 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21994 | yes |
| SF-2026-ARXIV-2606-22000 | arXiv:2606.22000v1 | paper-v1:2606.22000 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22000 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22000 | yes |
| SF-2026-ARXIV-2606-22013 | arXiv:2606.22013v1 | paper-v1:2606.22013 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22013 | self | — | new_in_window | PLATFORM-PRODUCTION | Integrate | books-review:SF-2026-ARXIV-2606-22013 | yes |
| SF-2026-ARXIV-2606-22019 | arXiv:2606.22019v1 | paper-v1:2606.22019 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22019 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-22019 | yes |
| SF-2026-ARXIV-2606-22030 | arXiv:2606.22030v1 | paper-v1:2606.22030 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22030 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22030 | yes |
| SF-2026-ARXIV-2606-22043 | arXiv:2606.22043v1 | paper-v1:2606.22043 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22043 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-22043 | yes |
| SF-2026-ARXIV-2606-22082 | arXiv:2606.22082v1 | paper-v1:2606.22082 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-22082 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22082 | yes |
| SF-2026-ARXIV-2606-22085 | arXiv:2606.22085v1 | paper-v1:2606.22085 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-22085 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22085 | yes |
| SF-2026-ARXIV-2606-22136 | arXiv:2606.22136v1 | paper-v1:2606.22136 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-22136 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22136 | yes |
| SF-2026-ARXIV-2606-22142 | arXiv:2606.22142v1 | paper-v1:2606.22142 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22142 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-22142 | yes |
| SF-2026-ARXIV-2606-22164 | arXiv:2606.22164v1 | paper-v1:2606.22164 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22164 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-22164 | yes |
| SF-2026-ARXIV-2606-22175 | arXiv:2606.22175v1 | paper-v1:2606.22175 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22175 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-22175 | yes |
| SF-2026-ARXIV-2606-22179 | arXiv:2606.22179v1 | paper-v1:2606.22179 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22179 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-22179 | yes |
| SF-2026-ARXIV-2606-22180 | arXiv:2606.22180v1 | paper-v1:2606.22180 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22180 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-22180 | yes |
| SF-2026-ARXIV-2606-22189 | arXiv:2606.22189v1 | paper-v1:2606.22189 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-22189 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22189 | yes |
| SF-2026-ARXIV-2606-22203 | arXiv:2606.22203v1 | paper-v1:2606.22203 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22203 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-22203 | yes |
| SF-2026-ARXIV-2606-22248 | arXiv:2606.22248v1 | paper-v1:2606.22248 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-22248 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22248 | yes |
| SF-2026-ARXIV-2606-22263 | arXiv:2606.22263v1 | paper-v1:2606.22263 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22263 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-22263 | yes |
| SF-2026-ARXIV-2606-22283 | arXiv:2606.22283v1 | paper-v1:2606.22283 | 2026-W25 | 2026-06-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-22283 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-22283 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21822 | RP-f5d325c8a28c0c70 | standard | arXiv:2606.21822v1 | SRC-ARXIV@arXiv:2606.21822v1 | https://arxiv.org/html/2606.21822v1 — §2 CNnotator Tool Design | https://arxiv.org/html/2606.21822v1 — §3 Benchmark; §4 Results | https://arxiv.org/html/2606.21822v1 — §3 Test set limitations; §4 Failure Modes; §5 Framework Tradeoffs | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21822 | complete |
| SF-2026-ARXIV-2606-21836 | RP-c40af5717e97fc21 | standard | arXiv:2606.21836v1 | SRC-ARXIV@arXiv:2606.21836v1 | https://arxiv.org/html/2606.21836v1 — §II Agentic DSE Methodology; §II-C Auditable Optimization Traces | https://arxiv.org/html/2606.21836v1 — §III Experimental Setup; §IV Results | https://arxiv.org/html/2606.21836v1 — §VI Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21836 | complete |
| SF-2026-ARXIV-2606-21842 | RP-1334bcc53d8329d1 | deep | arXiv:2606.21842v1 | SRC-ARXIV@arXiv:2606.21842v1 | https://arxiv.org/html/2606.21842v1 — §IV Overview; §V SpliceLeak: Semantic Extraction Methodology; §VI SpliceDefense | https://arxiv.org/html/2606.21842v1 — §VII Evaluation; §VII-A Experimental Setup | https://arxiv.org/html/2606.21842v1 — §III Motivation: Limitations of Existing Works; Appendix A Discussion and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21842 | complete |
| SF-2026-ARXIV-2606-21843 | RP-589119ac66a88456 | deep | arXiv:2606.21843v1 | SRC-ARXIV@arXiv:2606.21843v1 | https://arxiv.org/html/2606.21843v1 — §3.1 Ada: a persistent AI agent; §3.4 The probe battery | https://arxiv.org/html/2606.21843v1 — §4 Magnitude Baseline; §5.6 Drift experiment | https://arxiv.org/html/2606.21843v1 — §6.3 Limitations — Drift trajectory is a padding artifact | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21843 | complete |
| SF-2026-ARXIV-2606-21848 | RP-1e4096d0e5dfdfea | deep | arXiv:2606.21848v1 | SRC-ARXIV@arXiv:2606.21848v1 | https://arxiv.org/html/2606.21848v1 — §2 Method; §3 Value-only Cache in Autoregressive Inference | https://arxiv.org/html/2606.21848v1 — §5 Experiments | https://arxiv.org/html/2606.21848v1 — §2.2 equivalence conditions; §6 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21848 | complete |
| SF-2026-ARXIV-2606-21854 | RP-75c00aa8591e3911 | standard | arXiv:2606.21854v1 | SRC-ARXIV@arXiv:2606.21854v1 | https://arxiv.org/html/2606.21854v1 — §3 ESPnet3 Framework | https://arxiv.org/html/2606.21854v1 — §4 Experiments; §4.1 OWSM Pre-training | https://arxiv.org/html/2606.21854v1 — §5 Conclusion — release and speech/audio workload boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21854 | complete |
| SF-2026-ARXIV-2606-21856 | RP-008b0c5860928778 | deep | arXiv:2606.21856v1 | SRC-ARXIV@arXiv:2606.21856v1 | https://arxiv.org/html/2606.21856v1 — §3 Harness-MU | https://arxiv.org/html/2606.21856v1 — §4 Experiments; §4.1 Deployment Settings | https://arxiv.org/html/2606.21856v1 — §5 Discussion; §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21856 | complete |
| SF-2026-ARXIV-2606-21868 | RP-ba738f2ff4cb005f | deep | arXiv:2606.21868v1 | SRC-ARXIV@arXiv:2606.21868v1 | https://arxiv.org/html/2606.21868v1 — §3 Working-Set Predictor and Runtime Integration | https://arxiv.org/html/2606.21868v1 — §4 Routing Signal and Decode Throughput; §5 Working-Set Value | https://arxiv.org/html/2606.21868v1 — §6 Limitations; simulated-constrained-device disclosure | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21868 | complete |
| SF-2026-ARXIV-2606-21869 | RP-023f9f3384dbe357 | deep | arXiv:2606.21869v1 | SRC-ARXIV@arXiv:2606.21869v1 | https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset | https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups | https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21869 | complete |
| SF-2026-ARXIV-2606-21875 | RP-0185e25bae36de6c | standard | arXiv:2606.21875v1 | SRC-ARXIV@arXiv:2606.21875v1 | https://arxiv.org/html/2606.21875v1 — §4 Signed Evidence Decomposition; §5 Support, Opposition, and Conflict; §8 Perturbation Stability; §24 ScopeGate: Conditional Value and a Finite-Sample Deployment Test | https://arxiv.org/html/2606.21875v1 — §15 Sanity Checks on Standard Benchmark Data Sets; §16 Large Real-Data Benchmark; §18 Model-Agnostic Black-Box Robustness; §21 Real Healthcare Benchmarks Beyond Confidence; §23 External Finance Stress Test and Scope Boundary; §25 Independent External Replication | https://arxiv.org/html/2606.21875v1 — §30 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21875 | complete |
| SF-2026-ARXIV-2606-21877 | RP-078791b56b025246 | deep | arXiv:2606.21877v1 | SRC-ARXIV@arXiv:2606.21877v1 | https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation | https://arxiv.org/html/2606.21877v1 — §V Evaluation | https://arxiv.org/html/2606.21877v1 — §VII Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21877 | complete |
| SF-2026-ARXIV-2606-21884 | RP-299c40cf6bb049ef | deep | arXiv:2606.21884v1 | SRC-ARXIV@arXiv:2606.21884v1 | https://arxiv.org/html/2606.21884v1 — §4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder | https://arxiv.org/html/2606.21884v1 — §5 Results; §6 Anatomy of the Failures | https://arxiv.org/html/2606.21884v1 — §8.2 Threats to validity; §10 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21884 | complete |
| SF-2026-ARXIV-2606-21891 | RP-f846f430548316d5 | deep | arXiv:2606.21891v1 | SRC-ARXIV@arXiv:2606.21891v1 | https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning | https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details | https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21891 | complete |
| SF-2026-ARXIV-2606-21917 | RP-f56638089ea07df7 | standard | arXiv:2606.21917v1 | SRC-ARXIV@arXiv:2606.21917v1 | https://arxiv.org/html/2606.21917v1 — §3 Methodology; §3.2 Target Construction; §3.3 Attention Probing | https://arxiv.org/html/2606.21917v1 — §4 Results and Discussion; §4.1 Experimental Setting | https://arxiv.org/html/2606.21917v1 — §6 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21917 | complete |
| SF-2026-ARXIV-2606-21954 | RP-b9bf947a6b09a8d5 | deep | arXiv:2606.21954v1 | SRC-ARXIV@arXiv:2606.21954v1 | https://arxiv.org/html/2606.21954v1 — §4 Proposed XLT Metric: HAT Score; §4.1 Transfer Profile and HAT Score | https://arxiv.org/html/2606.21954v1 — §5 Experimental Details; §6 Results | https://arxiv.org/html/2606.21954v1 — §8 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21954 | complete |
| SF-2026-ARXIV-2606-21959 | RP-6a77c5ef61f6f76d | standard | arXiv:2606.21959v1 | SRC-ARXIV@arXiv:2606.21959v1 | https://arxiv.org/html/2606.21959v1 — §3 The OpenBioRQ Benchmark; §3.2 Construction Quality and Grounded Openness | https://arxiv.org/html/2606.21959v1 — §4 Evaluation Protocol; §5 Experiments and Analysis | https://arxiv.org/html/2606.21959v1 — §6 Discussion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21959 | complete |
| SF-2026-ARXIV-2606-21963 | RP-2ffb6ab96ab36750 | standard | arXiv:2606.21963v1 | SRC-ARXIV@arXiv:2606.21963v1 | https://arxiv.org/html/2606.21963v1 — §2 Methodology; §2.1 Parallel Context Retrieval; §2.2 Agentic Code Exploration; §2.3 Synthesis & Reasoning | https://arxiv.org/html/2606.21963v1 — §3 Experiment; §3.2 Accuracy Results; §3.3 Comparative Analysis & Ablation Study | https://arxiv.org/html/2606.21963v1 — §4.1 Limitations & Failure Analysis; §4.3 Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21963 | complete |
| SF-2026-ARXIV-2606-21968 | RP-930ff292c9ce7a09 | deep | arXiv:2606.21968v1 | SRC-ARXIV@arXiv:2606.21968v1 | https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Context Trade-off; §4 Proposed Method: ViRGo | https://arxiv.org/html/2606.21968v1 — §5 Experiments; §5.1 Experimental Setup | https://arxiv.org/html/2606.21968v1 — §7 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21968 | complete |
| SF-2026-ARXIV-2606-21994 | RP-1cdf9c3fafcc275b | standard | arXiv:2606.21994v1 | SRC-ARXIV@arXiv:2606.21994v1 | https://arxiv.org/html/2606.21994v1 — §Method — Truncated On-Policy Distillation; Prefix-Based Trajectory Scoring; Prefix-Guided On-Policy Distillation | https://arxiv.org/html/2606.21994v1 — §Experiments — Setup; Compared Methods; §Results — Main Results and four ablations; Appendix B Training and Implementation Details | https://arxiv.org/html/2606.21994v1 — §Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-21994 | complete |
| SF-2026-ARXIV-2606-22000 | RP-9f40202f187d5718 | deep | arXiv:2606.22000v1 | SRC-ARXIV@arXiv:2606.22000v1 | https://arxiv.org/html/2606.22000v1 — §3 The CFAgentBench Environment; §4 Tasks | https://arxiv.org/html/2606.22000v1 — §5 Evaluation; §6 Experiments | https://arxiv.org/html/2606.22000v1 — §7 Limitations and Ethics | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22000 | complete |
| SF-2026-ARXIV-2606-22013 | RP-c20a44e99d74b7c2 | deep | arXiv:2606.22013v1 | SRC-ARXIV@arXiv:2606.22013v1 | https://arxiv.org/html/2606.22013v1 — §2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine | https://arxiv.org/html/2606.22013v1 — §3 Experimental Methodology; §4 Results | https://arxiv.org/html/2606.22013v1 — §5 Discussion; Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22013 | complete |
| SF-2026-ARXIV-2606-22019 | RP-4d613152f3dd2d83 | deep | arXiv:2606.22019v1 | SRC-ARXIV@arXiv:2606.22019v1 | https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel? | https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel | https://arxiv.org/html/2606.22019v1 — §8 Discussion, limitations, and related work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22019 | complete |
| SF-2026-ARXIV-2606-22030 | RP-11bf005ed260e26a | deep | arXiv:2606.22030v1 | SRC-ARXIV@arXiv:2606.22030v1 | https://arxiv.org/html/2606.22030v1 — §3 The Nous Architecture; §3.3 Bayesian Update; §3.7 Pipelines | https://arxiv.org/html/2606.22030v1 — §4 Experimental Setup; §5 Results; §6 Analysis | https://arxiv.org/html/2606.22030v1 — §7 Limitations and Future Work; §5 A caveat on the A-MEM comparison | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22030 | complete |
| SF-2026-ARXIV-2606-22043 | RP-3cacf9690eb7ddbf | deep | arXiv:2606.22043v1 | SRC-ARXIV@arXiv:2606.22043v1 | https://arxiv.org/html/2606.22043v1 — §2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet | https://arxiv.org/html/2606.22043v1 — §3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details | https://arxiv.org/html/2606.22043v1 — §8 Discussion and limitations — Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22043 | complete |
| SF-2026-ARXIV-2606-22082 | RP-4ba7b0919916203d | standard | arXiv:2606.22082v1 | SRC-ARXIV@arXiv:2606.22082v1 | https://arxiv.org/html/2606.22082v1 — §3.2 Design and Implementation of CodeTeam | https://arxiv.org/html/2606.22082v1 — §3.3 Benchmark Experiment Design; §3.4 Execution-Based Evaluation; §4 Results | https://arxiv.org/html/2606.22082v1 — §6 Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22082 | complete |
| SF-2026-ARXIV-2606-22085 | RP-650e0e81a7784e0f | standard | arXiv:2606.22085v1 | SRC-ARXIV@arXiv:2606.22085v1 | https://arxiv.org/html/2606.22085v1 — §3 Methodology — Experimental settings; Interventions; Data; Models | https://arxiv.org/html/2606.22085v1 — §4 Detecting Changes — Completed Condition; Partial Condition; Self-Awareness; §5 Localizing Changes; Appendix D Additional Results | https://arxiv.org/html/2606.22085v1 — Limitations; Appendix B Model Details | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22085 | complete |
| SF-2026-ARXIV-2606-22136 | RP-1e9eeb11e75b188b | standard | arXiv:2606.22136v1 | SRC-ARXIV@arXiv:2606.22136v1 | https://arxiv.org/html/2606.22136v1 — §3 WM-H Dataset Construction via Controllable Video Synthesis; §4 Wh0: Policy Learning with Human-Robot Alignment | https://arxiv.org/html/2606.22136v1 — §5 Experiments; §5.1 Experimental Setup | https://arxiv.org/html/2606.22136v1 — §6 Conclusion and Limitations; Appendix A.6 Failure Cases | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22136 | complete |
| SF-2026-ARXIV-2606-22142 | RP-4195a6a64f7f1f77 | deep | arXiv:2606.22142v1 | SRC-ARXIV@arXiv:2606.22142v1 | https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance | https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup | https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22142 | complete |
| SF-2026-ARXIV-2606-22164 | RP-280044a22e962768 | deep | arXiv:2606.22164v1 | SRC-ARXIV@arXiv:2606.22164v1 | https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem | https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results | https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22164 | complete |
| SF-2026-ARXIV-2606-22175 | RP-17e45447640f2b67 | deep | arXiv:2606.22175v1 | SRC-ARXIV@arXiv:2606.22175v1 | https://arxiv.org/html/2606.22175v1 — §II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc | https://arxiv.org/html/2606.22175v1 — §IV Evaluation; §IV-A Experiment Settings | https://arxiv.org/html/2606.22175v1 — §I-E Limitation of the Proposed Approach | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22175 | complete |
| SF-2026-ARXIV-2606-22179 | RP-04f72297af3f9f90 | deep | arXiv:2606.22179v1 | SRC-ARXIV@arXiv:2606.22179v1 | https://arxiv.org/html/2606.22179v1 — §3 Problem Setup; §4 Confidence Constructions | https://arxiv.org/html/2606.22179v1 — §5 Experiments; §5.1 Setup | https://arxiv.org/html/2606.22179v1 — §7 Limitations; §6 Deployment Recommendations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22179 | complete |
| SF-2026-ARXIV-2606-22180 | RP-7823eec797a6b15d | deep | arXiv:2606.22180v1 | SRC-ARXIV@arXiv:2606.22180v1 | https://arxiv.org/html/2606.22180v1 — §5 FeLoG; §5.1 Feedback-coupled Sampling-Training Model; §5.2 Activity-aware Communication | https://arxiv.org/html/2606.22180v1 — §6 Experimental Results; §6.1 Experimental Setup | https://arxiv.org/html/2606.22180v1 — §7 Conclusions and experimental generalizability boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22180 | complete |
| SF-2026-ARXIV-2606-22189 | RP-d1a50ad62ce6b996 | standard | arXiv:2606.22189v1 | SRC-ARXIV@arXiv:2606.22189v1 | https://arxiv.org/html/2606.22189v1 — §3 System Overview; §4 Data Quality and Contamination Control; §5 Training Efficiency | https://arxiv.org/html/2606.22189v1 — §6 Evaluation Protocol; §7 Results | https://arxiv.org/html/2606.22189v1 — §9 Limitations; §10 Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22189 | complete |
| SF-2026-ARXIV-2606-22203 | RP-83bc04f6b898f4fa | deep | arXiv:2606.22203v1 | SRC-ARXIV@arXiv:2606.22203v1 | https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory | https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results | https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22203 | complete |
| SF-2026-ARXIV-2606-22248 | RP-995c188adb703d02 | standard | arXiv:2606.22248v1 | SRC-ARXIV@arXiv:2606.22248v1 | https://arxiv.org/html/2606.22248v1 — §3 SamatNext v0.2-B Architecture; §4 Curriculum and Evaluation Setup | https://arxiv.org/html/2606.22248v1 — §5 Empirical Results | https://arxiv.org/html/2606.22248v1 — §8 Limitations; §6.4 Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22248 | complete |
| SF-2026-ARXIV-2606-22263 | RP-3412dae8dccd7e53 | deep | arXiv:2606.22263v1 | SRC-ARXIV@arXiv:2606.22263v1 | https://arxiv.org/html/2606.22263v1 — §III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction | https://arxiv.org/html/2606.22263v1 — §V Evaluation | https://arxiv.org/html/2606.22263v1 — §VI Discussion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22263 | complete |
| SF-2026-ARXIV-2606-22283 | RP-8c3966985b00374e | deep | arXiv:2606.22283v1 | SRC-ARXIV@arXiv:2606.22283v1 | https://arxiv.org/html/2606.22283v1 — §Part II Reaching the ANE — Software stack; Dispatching without Core ML; §Part VI The Silicon — Datapath and MAC geometry; §Part VII The Toolchain and Encoding; §Part VIII System Internals | https://arxiv.org/html/2606.22283v1 — §Part III Performance and Fit — Roofline; Power and efficiency; Across the chip family; Appendix A Operation-by-device matrix; Appendix E Provenance | https://arxiv.org/html/2606.22283v1 — §Part V Practice — Pitfalls and limits; §Methodology; §Open questions; §Introduction — direct route is undocumented, unsupported and version-fragile | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-22283 | complete |

### Source Reviews
<!-- review:SF-2026-ARXIV-2606-21822:start -->
### 2606.21822 — CNnotator: LLM-Guided Memory Safety Annotation Synthesis

**问题与旧路径。** 该 family 针对 `CN memory-safety specification synthesis for small-to-medium C functions` 暴露的具体缺口是：Ch72 已要求 coding-agent 安全真值来自 executable evidence；本 family 增加 CN 具体实例但不改变 owner。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 把 LLM 生成的 C 内存所有权猜测编译成 CN contract，再由 Bennet/Fulminate 对 100 个生成 heap state 执行检查；失败进入最多六轮有界修复。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 31 个可标注函数与 3 个故意不安全函数上，o3 首轮 90%、总计 97%，GPT-4o 首轮 65%。 Method=`https://arxiv.org/html/2606.21822v1 — §2 CNnotator Tool Design`；Evaluation=`https://arxiv.org/html/2606.21822v1 — §3 Benchmark; §4 Results`。Benchmark contract：model=`OpenAI o3, o1, o1-mini, o3-mini and GPT-4o`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`first-attempt and eventual valid-annotation rate plus unsafe-function handling`。

**Trade-off、failure、共存与演进。** 测试通过只覆盖生成状态，不是全路径证明；safe-but-unexpressible、搜索失败与真实 unsafe 仍可能落入同一失败出口。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21822v1 — §3 Test set limitations; §4 Failure Modes; §5 Framework Tradeoffs`。

<!-- claim:SF-2026-ARXIV-2606-21822:start -->
Claim boundary：仅 `arXiv:2606.21822v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21822:end -->
<!-- review:SF-2026-ARXIV-2606-21822:end -->

<!-- review:SF-2026-ARXIV-2606-21836:start -->
### 2606.21836 — AgentDSE: Reasoning-Augmented Architectural Design Space Exploration

**问题与旧路径。** 该 family 针对 `DNN accelerator mapping, hardware/software co-design and CPU cache-hierarchy DSE` 暴露的具体缺口是：Ch81 已拥有 evaluator-driven search、persistent workspace 与 simulator-as-contract；保留为 cross-domain evidence。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 把架构 DSE 从只读 scalar reward 的黑盒搜索改成可编辑 workspace：candidate、constraint、simulator harness、history、best 与 budget 都成为持久 artifact，agent 运行 hypothesis-test-refine。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** Timeloop/Accelergy、MAESTRO 与 ChampSim 三类 DSE 上，在严格调用预算内达到相当或更优设计，最高减少两个数量级 simulator evaluation。 Method=`https://arxiv.org/html/2606.21836v1 — §II Agentic DSE Methodology; §II-C Auditable Optimization Traces`；Evaluation=`https://arxiv.org/html/2606.21836v1 — §III Experimental Setup; §IV Results`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`EDP or IPC under matched simulator-call budgets and trace audit`。

**Trade-off、failure、共存与演进。** simulator artifact 会被 agent 当真；LLM prior、调用成本与三类受测空间不能外推到真实芯片 sign-off。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21836v1 — §VI Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2606-21836:start -->
Claim boundary：仅 `arXiv:2606.21836v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21836:end -->
<!-- review:SF-2026-ARXIV-2606-21836:end -->

<!-- review:SF-2026-ARXIV-2606-21842:start -->
### 2606.21842 — Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG

**问题与旧路径。** 该 family 针对 `multi-tenant RAG with non-prefix KV-cache fusion` 暴露的具体缺口是：当前 Ch72 已把跨租户 cache hit timing、principal-specific namespace、non-prefix causal provenance 与 full-recompute fallback 写成同一 security contract；Step-Wave/QCP/CTBF 是该 owner 的受限实例。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** non-prefix KV fusion 的固定 chunk routing 与未对齐 tail recomputation 形成 Step-Wave TTFT oracle；SpliceLeak 先恢复隐藏前缀长度，再用 boundary collision 逐 token 提取；QCP+CTBF 消除长度与语义 timing signal。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** vLLM+LMCache 上覆盖三种 threat scenario，并报告 bounded-entropy 场景最高 100% extraction、最少 63 requests/token；防线把 ΔTTFT 压近 0。 Method=`https://arxiv.org/html/2606.21842v1 — §IV Overview; §V SpliceLeak: Semantic Extraction Methodology; §VI SpliceDefense`；Evaluation=`https://arxiv.org/html/2606.21842v1 — §VII Evaluation; §VII-A Experimental Setup`。Benchmark contract：model=`LongChat-7B-v1.5-32K and Qwen2.5-7B-Instruct targets; Gemini-3-Pro extraction agent`；hardware=`4 NVIDIA A40 GPUs with 48 GB VRAM each and 256 GB system RAM`；precision=`Not Disclosed`；batch=`maximum batch size 16`；concurrency=`Poisson background arrivals at 0.004 requests per second per client`；SLO=`Not Disclosed`；evaluator=`extraction success, requests per token, TTFT signal and defense throughput`。

**Trade-off、failure、共存与演进。** 威胁模型要求共置 tenant、共享 cache、可重复 TTFT probe 与受限语义搜索空间；局部测试不证明任意 engine/GPU 或公网噪声下可复现。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21842v1 — §III Motivation: Limitations of Existing Works; Appendix A Discussion and Future Work`。

<!-- claim:SF-2026-ARXIV-2606-21842:start -->
Claim boundary：仅 `arXiv:2606.21842v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21842:end -->
<!-- review:SF-2026-ARXIV-2606-21842:end -->

<!-- review:SF-2026-ARXIV-2606-21843:start -->
### 2606.21843 — Measuring What Persists: Conditioning Mechanisms and a Geometric Framework for AI Agent Identity

**问题与旧路径。** 该 family 针对 `identity-conditioning probes across base, 4,200-token Card-conditioned, repetitive-padded and diverse-padded contexts` 暴露的具体缺口是：该 family 的长期价值是反例：pre-failure sensor 必须把 context generator 纳入 run identity，不能把 padding artifact 写成 agent drift。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。 唯一知识 owner 为 `PLATFORM-MONITORING`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 单一持久 agent 的 cross-sectional probe battery 测得 conditioning structure；原 context-pressure drift 在多样 padding 下至 150K token 不再出现。 Method=`https://arxiv.org/html/2606.21843v1 — §3.1 Ada: a persistent AI agent; §3.4 The probe battery`；Evaluation=`https://arxiv.org/html/2606.21843v1 — §4 Magnitude Baseline; §5.6 Drift experiment`。Benchmark contract：model=`Anthropic Claude Sonnet API backing the persistent Ada agent`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`50 samples per probe × condition × context-length combination`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`next-token entropy, sqrt-JSD distance and magnitude-homology diagnostics`。

**Trade-off、failure、共存与演进。** 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21843v1 — §6.3 Limitations — Drift trajectory is a padding artifact`。

<!-- claim:SF-2026-ARXIV-2606-21843:start -->
Claim boundary：仅 `arXiv:2606.21843v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21843:end -->
<!-- review:SF-2026-ARXIV-2606-21843:end -->

<!-- review:SF-2026-ARXIV-2606-21848:start -->
### 2606.21848 — Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers

**问题与旧路径。** 该 family 针对 `language modeling and downstream reasoning with QKV versus QVV attention` 暴露的具体缺口是：Ch14 需新增 routing 与 retrieval representation 可合并但带秩条件的 alternative branch；Ch45 只消费 50% cache consequence。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。 唯一知识 owner 为 `MODEL-SELF-ATTENTION`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** GPT-2 280M/557M、Pythia 410M、Qwen2 1.5B、Llama 3.2 1B 五组模型中，4/5 perplexity 与 4/5 downstream benchmark 不低于 QKV，同时 cache 容量减半。 Method=`https://arxiv.org/html/2606.21848v1 — §2 Method; §3 Value-only Cache in Autoregressive Inference`；Evaluation=`https://arxiv.org/html/2606.21848v1 — §5 Experiments`。Benchmark contract：model=`GPT-2 280M, GPT-2 557M, Pythia 410M, Qwen2 1.5B and Llama 3.2 1B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`1 for the Qwen2-1.5B throughput benchmark`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`perplexity, downstream accuracy and value-only cache memory`。

**Trade-off、failure、共存与演进。** 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21848v1 — §2.2 equivalence conditions; §6 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21848:start -->
Claim boundary：仅 `arXiv:2606.21848v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21848:end -->
<!-- review:SF-2026-ARXIV-2606-21848:end -->

<!-- review:SF-2026-ARXIV-2606-21854:start -->
### 2606.21854 — ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

**问题与旧路径。** 该 family 针对 `large-scale speech/audio pre-training and fine-tuning recipes` 暴露的具体缺口是：Ch36 已拥有 data pipeline、sharding 与 compute utilization 的 owner；ESPnet3 是 speech-specific framework instance。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** DataOrganizer 把 dataset composition、split/shard 与 recipe stage 分离，统一 Python workflow 只通过轻量 override 保留实验差异。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** OWSM multi-node pretraining 相比 ESPnet2 每 epoch 减少 21.1 分钟、GPU utilization 超过 80%；新增 fine-tune model/data 约 46 行代码。 Method=`https://arxiv.org/html/2606.21854v1 — §3 ESPnet3 Framework`；Evaluation=`https://arxiv.org/html/2606.21854v1 — §4 Experiments; §4.1 OWSM Pre-training`。Benchmark contract：model=`OWSM-Base 102M`；hardware=`4 nodes with 4 NVIDIA H100 GPUs per node, 16 H100 total`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`epoch time averaged over five consecutive epochs, GPU utilization, CHiME-4 WER at 350k updates and integration code delta`。

**Trade-off、failure、共存与演进。** 只覆盖 speech/audio recipes 与作者 OWSM workload；开发行数和平均利用率不证明跨框架可维护性或端到端收敛等价。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21854v1 — §5 Conclusion — release and speech/audio workload boundary`。

<!-- claim:SF-2026-ARXIV-2606-21854:start -->
Claim boundary：仅 `arXiv:2606.21854v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21854:end -->
<!-- review:SF-2026-ARXIV-2606-21854:end -->

<!-- review:SF-2026-ARXIV-2606-21856:start -->
### 2606.21856 — Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents

**问题与旧路径。** 该 family 针对 `multi-principal tool-using agent tasks with shared and private state` 暴露的具体缺口是：当前 Ch84 已以 AgentRun principal/tenant 绑定 workspace、credential、memory、tool 与 evidence，Ch81 也把 deterministic hooks 设为 sandbox/tool/checkpoint/retry/verifier owner；Harness-MU 不再改变长期 owner。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 多用户 agent harness 把 user/principal、workspace、credential、memory 与 tool capability 分离；deterministic hook 在执行前后实施 policy，审计记录 control decision 而不只记录自然语言。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** exact-v1 在多用户 delegation、共享资源与 tool-use scenarios 中比较无治理 agent 与 governed harness 的 task effectiveness 和 policy compliance。 Method=`https://arxiv.org/html/2606.21856v1 — §3 Harness-MU`；Evaluation=`https://arxiv.org/html/2606.21856v1 — §4 Experiments; §4.1 Deployment Settings`。Benchmark contract：model=`deepseek-v4-pro, qwen3.6-35b-a3b, gemini-2.5-flash and gpt-4.1-nano via OpenRouter`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`16 max_workers`；SLO=`Not Disclosed`；evaluator=`task completion plus deterministic governance-policy outcomes`。

**Trade-off、failure、共存与演进。** harness policy 依赖声明完整性与 hook 覆盖；被绕过的外部 side effect、stale identity mapping 和恶意 plugin 仍需 host reference monitor。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21856v1 — §5 Discussion; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2606-21856:start -->
Claim boundary：仅 `arXiv:2606.21856v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21856:end -->
<!-- review:SF-2026-ARXIV-2606-21856:end -->

<!-- review:SF-2026-ARXIV-2606-21868:start -->
### 2606.21868 — WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware

**问题与旧路径。** 该 family 针对 `Mixture-of-Experts autoregressive serving under constrained device memory` 暴露的具体缺口是：Ch56 需把 expert weights 与 KV 视为竞争同一容量预算的联合 working set，而不是两个独立 cache。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 极低资源硬件上比较 expert/KV baselines，报告 token latency、throughput、命中/迁移与质量。 Method=`https://arxiv.org/html/2606.21868v1 — §3 Working-Set Predictor and Runtime Integration`；Evaluation=`https://arxiv.org/html/2606.21868v1 — §4 Routing Signal and Decode Throughput; §5 Working-Set Value`。Benchmark contract：model=`Qwen3-30B-A3B, MiniMax-M2 229B FP8, Jamba-v0.1 52B, Kimi-VL and OLMoE`；hardware=`single NVIDIA H100 NVL with 95,830 MiB; Qwen3/Kimi constrained-device arms emulated by memory cap`；precision=`BF16 for Qwen3-30B-A3B; FP8 for MiniMax-M2`；batch=`Not Disclosed`；concurrency=`maximum concurrency at 4,096 tokens varies with KV allocation`；SLO=`Not Disclosed`；evaluator=`decode throughput, expert/KV residency, transfer and quality`。

**Trade-off、failure、共存与演进。** Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21868v1 — §6 Limitations; simulated-constrained-device disclosure`。

<!-- claim:SF-2026-ARXIV-2606-21868:start -->
Claim boundary：仅 `arXiv:2606.21868v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21868:end -->
<!-- review:SF-2026-ARXIV-2606-21868:end -->

<!-- review:SF-2026-ARXIV-2606-21869:start -->
### 2606.21869 — The Language-Energy Divide: Measuring Energy Costs of Multilingual LLM Inference

**问题与旧路径。** 该 family 针对 `multilingual inference over Belebele, translated GSM8K and LM-Arena prompts` 暴露的具体缺口是：Ch66 需把语言切片的 energy/quality 联合 contract 加入 evaluation identity；Ch70 只消费成本结果。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** Belebele 122 languages、translated GSM8K 与 LM-Arena prompts 上跨模型测量能耗/质量，并在 L40S 与 RTX 6000 Pro Blackwell 做硬件对照。 Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`。Benchmark contract：model=`Qwen3-8B, Qwen3-14B, Qwen3-32B, Gemma-3-27B and Llama-3.1-8B-Instruct`；hardware=`NVIDIA L40S 48 GB and RTX 6000 Pro Blackwell 96 GB GPUs`；precision=`Not Disclosed`；batch=`256 except batch-sweep values 16, 32, 64, 128, 256 and 512`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`per-language energy, token count and task accuracy`。

**Trade-off、failure、共存与演进。** 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects`。

<!-- claim:SF-2026-ARXIV-2606-21869:start -->
Claim boundary：仅 `arXiv:2606.21869v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21869:end -->
<!-- review:SF-2026-ARXIV-2606-21869:end -->

<!-- review:SF-2026-ARXIV-2606-21875:start -->
### 2606.21875 — Signed Evidence Flow: Conflict-Aware and Stability-Calibrated Data Analysis

**问题与旧路径。** 该 family 针对 `risk triage among already-confident tabular predictions` 暴露的具体缺口是：Ch66 已区分 confidence、evidence 与 policy-bound triage；本 family 的反向结果强化 calibration boundary。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Signed Evidence Flow 把已拟合预测的正负 attribution 分解为 support、opposition、conflict 与 perturbation stability；ScopeGate 用 held-out permutation 检查 conflict-risk 方向后才允许 triage。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 医疗、Covertype、金融与十个外部数据集显示 conflict 有时增加 error ranking，也在 Bank Marketing/Credit Default 上方向反转。 Method=`https://arxiv.org/html/2606.21875v1 — §4 Signed Evidence Decomposition; §5 Support, Opposition, and Conflict; §8 Perturbation Stability; §24 ScopeGate: Conditional Value and a Finite-Sample Deployment Test`；Evaluation=`https://arxiv.org/html/2606.21875v1 — §15 Sanity Checks on Standard Benchmark Data Sets; §16 Large Real-Data Benchmark; §18 Model-Agnostic Black-Box Robustness; §21 Real Healthcare Benchmarks Beyond Confidence; §23 External Finance Stress Test and Scope Boundary; §25 Independent External Replication`。Benchmark contract：model=`standardized or balanced logistic regression, random forest and histogram gradient boosting classifiers`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`conditional error ranking, held-out ScopeGate direction and compute cost`。

**Trade-off、failure、共存与演进。** SEF 不是 causal explanation；attribution/reference choice 改变数值，相关 feature replacement 可能失真，B=40 stability refit 成本约单次 30.1–39.2 倍。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21875v1 — §30 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21875:start -->
Claim boundary：仅 `arXiv:2606.21875v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21875:end -->
<!-- review:SF-2026-ARXIV-2606-21875:end -->

<!-- review:SF-2026-ARXIV-2606-21877:start -->
### 2606.21877 — AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems

**问题与旧路径。** 该 family 针对 `pre-deployment agent authority/risk artifact validation` 暴露的具体缺口是：Ch72 需增加 authority-envelope BOM：依赖 provenance 不能替代 agent 能访问、记忆、修改和委托什么。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 13 个开源 agents、52 个 risk scenarios、33 个 deployment mutations；schema 覆盖 14/16 capability dimension，diff detector 对注入变更类型全命中。 Method=`https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation`；Evaluation=`https://arxiv.org/html/2606.21877v1 — §V Evaluation`。Benchmark contract：model=`Aider, OpenHands, SWE-agent, Cline, Goose, Open Interpreter, AutoGPT, PrivateGPT, GPT-Researcher, MetaGPT, CrewAI, AutoGen and BabyAGI`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`schema fillability, risk visibility, mutation-diff correctness and scorer rank consistency`。

**Trade-off、failure、共存与演进。** 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21877v1 — §VII Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21877:start -->
Claim boundary：仅 `arXiv:2606.21877v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21877:end -->
<!-- review:SF-2026-ARXIV-2606-21877:end -->

<!-- review:SF-2026-ARXIV-2606-21884:start -->
### 2606.21884 — A Verifiable Search Is Not a Learnable Chain-of-Thought

**问题与旧路径。** 该 family 针对 `nine deterministic-generator reasoning tasks` 暴露的具体缺口是：Ch33 需明确 verifiable outcome 不保证 search trace 可蒸馏；训练前先做 forward-derivability test。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 九类任务、11 个 CoT 设计、RLVR/STaR 与四类 backbone；cryptarithm solver 71% 而蒸馏仅 1–7%，揭示 key 后同例升至 57.1%。 Method=`https://arxiv.org/html/2606.21884v1 — §4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder`；Evaluation=`https://arxiv.org/html/2606.21884v1 — §5 Results; §6 Anatomy of the Failures`。Benchmark contract：model=`Nemotron-3-Nano 30B/3.5B active, Llama-3.2-3B, Qwen3.5-4B, gpt-oss-20b 21B/3.6B active, DeepSeek-V3.1 671B/37B active and Nemotron-Super 120B/12B active`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`solver coverage, CoT transfer, line fidelity, hit@k and intervention accuracy`。

**Trade-off、failure、共存与演进。** 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21884v1 — §8.2 Threats to validity; §10 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21884:start -->
Claim boundary：仅 `arXiv:2606.21884v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21884:end -->
<!-- review:SF-2026-ARXIV-2606-21884:end -->

<!-- review:SF-2026-ARXIV-2606-21891:start -->
### 2606.21891 — Learning the ARTS of Search for Automated Discovery

**问题与旧路径。** 该 family 针对 `22 automated ML research tasks from MLGym and MLEBench` 暴露的具体缺口是：Ch81 需把 low score 拆成 hypothesis failure 与 execution failure，防止 workflow 错误地删除可修复分支。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 22 个 MLGym/MLEBench tasks、每法三次、8 小时 budget；报告 IQM、optimality gap、trajectory 与组件 ablation。 Method=`https://arxiv.org/html/2606.21891v1 — §4 ARTS; §4.1 Expanding a Search Tree with Agentic Reasoning`；Evaluation=`https://arxiv.org/html/2606.21891v1 — §6 Experiments and Analysis; Appendix I Additional Experimental Details`。Benchmark contract：model=`OpenAI o3 scientist, Gemini 3 Flash executor and Qwen3-4B-Instruct test-time-trained scientist`；hardware=`one 40 GB NVIDIA A100 for each inference-only method; three 40 GB NVIDIA A100 GPUs for each test-time-training run`；precision=`Not Disclosed`；batch=`8 rollouts per GRPO group`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`best validation score, IQM, optimality gap, wall time and hypothesis/execution attribution`。

**Trade-off、failure、共存与演进。** scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21891v1 — §7 Discussion — Limitations and Ethical Concerns`。

<!-- claim:SF-2026-ARXIV-2606-21891:start -->
Claim boundary：仅 `arXiv:2606.21891v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21891:end -->
<!-- review:SF-2026-ARXIV-2606-21891:end -->

<!-- review:SF-2026-ARXIV-2606-21917:start -->
### 2606.21917 — Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing

**问题与旧路径。** 该 family 针对 `pre-generation hallucination-risk prediction on SQuAD, Natural Questions and HotpotQA` 暴露的具体缺口是：Ch67 已把 activation/attention monitor 定义为 model-version-bound sensor；该 family 不改变 authority。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 在生成前从 attention probe 预测 hallucination risk，以 soft target 表达不确定度，再把风险交给 abstain、retrieval 或 stronger-model route；sensor 不拥有 truth commit。 唯一知识 owner 为 `PLATFORM-MONITORING`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** exact-v1 跨 LLM 与 QA/hallucination datasets 比较 pre-generation detector 的 discrimination、calibration 与 routing utility。 Method=`https://arxiv.org/html/2606.21917v1 — §3 Methodology; §3.2 Target Construction; §3.3 Attention Probing`；Evaluation=`https://arxiv.org/html/2606.21917v1 — §4 Results and Discussion; §4.1 Experimental Setting`。Benchmark contract：model=`Qwen2.5-3B, Qwen2.5-7B, Qwen3.5-9B, Llama-2-7B and Gemma-4-E2B instruction-tuned models`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`probe-training batch size 8 or 16; soft targets use 10 samples per prompt`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`ROC-AUC, calibration and routing utility`。

**Trade-off、failure、共存与演进。** probe 与 label/judge 共偏，attention correlation 不证明因果；生成前预测不能覆盖 retrieval corruption 或生成中途状态变化。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21917v1 — §6 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21917:start -->
Claim boundary：仅 `arXiv:2606.21917v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21917:end -->
<!-- review:SF-2026-ARXIV-2606-21917:end -->

<!-- review:SF-2026-ARXIV-2606-21954:start -->
### 2606.21954 — Are Multilingual Models Actually Improving? Isolating True Cross-Lingual Transfer

**问题与旧路径。** 该 family 针对 `ECLeKTic, MGSMv2 and MMLU-ProX-Lite cross-lingual transfer` 暴露的具体缺口是：Ch66 需把 transfer capability 与 source-language base ability 解耦，避免版本比较的 denominator inflation。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 20 个语言模型、三套 multilingual benchmark；小模型 transfer 并未失效，随规模的进步慢于 raw accuracy 暗示。 Method=`https://arxiv.org/html/2606.21954v1 — §4 Proposed XLT Metric: HAT Score; §4.1 Transfer Profile and HAT Score`；Evaluation=`https://arxiv.org/html/2606.21954v1 — §5 Experimental Details; §6 Results`。Benchmark contract：model=`Gemini-2.5-Flash, Gemini-2.5-Flash Thinking-Off, Gemini-3-Flash, Gemini-3-Flash Low, Gemini-3-Flash Minimal, Gemma-3-1B, Gemma-3-4B, Gemma-3-12B, Gemma-3-27B, Gemma-4-E2B-IT, Gemma-4-E4B-IT, Gemma-4-26B-A4B-IT, Gemma-4-31B-IT, Claude-Haiku-4.5, Claude-Sonnet-4.6, Claude-Opus-4.7, Qwen-3-4B, Qwen-3-30B-A3B, GPT-OSS-20B and GPT-OSS-120B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`10 promptings per source/target item for HAT estimation`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`Hardness Adjusted Transfer versus raw source/target accuracy`。

**Trade-off、failure、共存与演进。** HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21954v1 — §8 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21954:start -->
Claim boundary：仅 `arXiv:2606.21954v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21954:end -->
<!-- review:SF-2026-ARXIV-2606-21954:end -->

<!-- review:SF-2026-ARXIV-2606-21959:start -->
### 2606.21959 — OpenBioRQ: Unsolved Biomedical Research Questions for Agents

**问题与旧路径。** 该 family 针对 `657-question OpenBioRQ core and 423-question frozen core` 暴露的具体缺口是：当前 Ch66 已明确引用不仅要存在还要支持 claim，并已把 deep-research citation support、coverage 与 synthesis 分层；OpenBioRQ 提供 biomedical stress case，但不改变 evaluation owner。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** OpenBioRQ 以未解决研究问题评估 agent：把 citation resolution、actual support、open-status verification 与 answer usefulness分层，并提供冻结 checklist 改善 judge agreement。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 受测 agents 在高难问题上 tool-use collapse；15.9% citation 指向错误论文，且 citation 可解析不等于支持 claim。 Method=`https://arxiv.org/html/2606.21959v1 — §3 The OpenBioRQ Benchmark; §3.2 Construction Quality and Grounded Openness`；Evaluation=`https://arxiv.org/html/2606.21959v1 — §4 Evaluation Protocol; §5 Experiments and Analysis`。Benchmark contract：model=`GLM-5.1, Qwen3.6, DeepSeek-V4, GLM-5, Qwen3.5-397B, Qwen3-235B, Gemini-3-Pro, Opus-4.7 and GPT-5.5`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`two-level citation factuality, checklist solve rate, tool use and judge agreement`。

**Trade-off、failure、共存与演进。** biomedical question set、冻结时点与 judge checklist 不证明未来问题仍未解决；benchmark 不能替代领域专家证据审查。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21959v1 — §6 Discussion and Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21959:start -->
Claim boundary：仅 `arXiv:2606.21959v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21959:end -->
<!-- review:SF-2026-ARXIV-2606-21959:end -->

<!-- review:SF-2026-ARXIV-2606-21963:start -->
### 2606.21963 — Holmes: Multimodal Agentic Diagnosis for Mixed-Language Mobile Crashes at Industrial Scale

**问题与旧路径。** 该 family 针对 `mixed-language mobile crash diagnosis over WeChat crash artifacts` 暴露的具体缺口是：Ch73/81 已要求 incident diagnosis 与 executable effect receipt 分离；Holmes 是工业案例。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Holmes 将 mixed-language mobile crash diagnosis 绑定 log、stack trace、source/change history 与工具执行，输出 diagnosis 与 evidence-linked repair，而非只生成解释文本。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 工业移动端 crash workload 上比较 diagnosis accuracy、time-to-resolution 与 artifact/tool ablation。 Method=`https://arxiv.org/html/2606.21963v1 — §2 Methodology; §2.1 Parallel Context Retrieval; §2.2 Agentic Code Exploration; §2.3 Synthesis & Reasoning`；Evaluation=`https://arxiv.org/html/2606.21963v1 — §3 Experiment; §3.2 Accuracy Results; §3.3 Comparative Analysis & Ablation Study`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`function-level fault-localization accuracy, diagnosis time and ablations`。

**Trade-off、failure、共存与演进。** 单组织 crash taxonomy、内部工具与数据分布限制复现；诊断建议不等于已合并修复或无回归。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21963v1 — §4.1 Limitations & Failure Analysis; §4.3 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2606-21963:start -->
Claim boundary：仅 `arXiv:2606.21963v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21963:end -->
<!-- review:SF-2026-ARXIV-2606-21963:end -->

<!-- review:SF-2026-ARXIV-2606-21968:start -->
### 2606.21968 — Look Before You Zoom: Adaptive Routing for the Resolution-Context Trade-off in Visual RAG

**问题与旧路径。** 该 family 针对 `visual RAG under resolution-context trade-off` 暴露的具体缺口是：Ch81 需把感知分辨率选择建模为有成本、可回退的 route，而不是固定预处理。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 多种 visual RAG benchmark/model 上比较质量、视觉 token 与 routing ablation。 Method=`https://arxiv.org/html/2606.21968v1 — §3 Motivations: Understanding the Resolution–Context Trade-off; §4 Proposed Method: ViRGo`；Evaluation=`https://arxiv.org/html/2606.21968v1 — §5 Experiments; §5.1 Experimental Setup`。Benchmark contract：model=`LLaVA-v1.5-7B, LLaVA-v1.5-13B, LLaVA-OneVision-0.5B and Qwen3-VL`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`task accuracy, inference time and route-selection ablations`。

**Trade-off、failure、共存与演进。** router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.21968v1 — §7 Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21968:start -->
Claim boundary：仅 `arXiv:2606.21968v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21968:end -->
<!-- review:SF-2026-ARXIV-2606-21968:end -->

<!-- review:SF-2026-ARXIV-2606-21994:start -->
### 2606.21994 — Prefix-Guided On-Policy Distillation: Mining Golden Trajectories from Rollouts

**问题与旧路径。** 该 family 针对 `DAPO-Math-17K training; AIME24, AIME25, AMC23, HMMT24 and HMMT25 evaluation` 暴露的具体缺口是：Ch33 已将 OPD 定义为探索催化剂并保留 teacher ceiling；prefix allocation 是同 owner 内实现分支。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Prefix-Guided OPD 用 teacher/student rollout 的早期 prefix overlap 估计后续 trajectory value，把 rollout budget 转向可能形成 golden trajectory 的前缀。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** reasoning tasks 上相对 OPD/on-policy distillation 比较 sample efficiency、accuracy 与 prefix allocation。 Method=`https://arxiv.org/html/2606.21994v1 — §Method — Truncated On-Policy Distillation; Prefix-Based Trajectory Scoring; Prefix-Guided On-Policy Distillation`；Evaluation=`https://arxiv.org/html/2606.21994v1 — §Experiments — Setup; Compared Methods; §Results — Main Results and four ablations; Appendix B Training and Implementation Details`。Benchmark contract：model=`DeepSeek-R1-Distill-Qwen-1.5B, JustRL-DeepSeek-1.5B, OpenMath-1.5B, JustRL-Nemotron-1.5B, DeepSeek-R1-Distill-Qwen-7B, Qwen3-4B-Base and Qwen3-4B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`training mini-batch 64 with 4 responses per prompt`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`benchmark accuracy, training time and rollout allocation`。

**Trade-off、failure、共存与演进。** 早期 overlap 可能错杀迟发正确路径并放大 teacher/student 共偏；它重分配探索预算，不扩展 teacher capability ceiling。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.21994v1 — §Limitations`。

<!-- claim:SF-2026-ARXIV-2606-21994:start -->
Claim boundary：仅 `arXiv:2606.21994v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-21994:end -->
<!-- review:SF-2026-ARXIV-2606-21994:end -->

<!-- review:SF-2026-ARXIV-2606-22000:start -->
### 2606.22000 — CFAgentBench: A Reproducible Environment and Benchmark for Autonomous Construction-Finance Agents

**问题与旧路径。** 该 family 针对 `40 oracle-validated autonomous construction-finance tasks across eight domains` 暴露的具体缺口是：当前 Ch66 已有专节把 Pass@k 能力覆盖、Pass^k conjunction reliability 与 paired transition 分离，且 action authority 已是独立 evaluation plane；CFAgentBench 不再形成新 delta。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** CFAgentBench 以可执行 construction-finance environment 记录账户/文档 state diff、forbidden side effect 与 approval-required money movement；正确金额但未获批准同样失败。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 多模型 agents 在 pass@1 与 pass@5 上测量 task completion、side effect、approval compliance，并显示重试可靠性塌陷。 Method=`https://arxiv.org/html/2606.22000v1 — §3 The CFAgentBench Environment; §4 Tasks`；Evaluation=`https://arxiv.org/html/2606.22000v1 — §5 Evaluation; §6 Experiments`。Benchmark contract：model=`DeepSeek-V3.1, Qwen3-235B-A22B-Instruct and Qwen2.5-72B-Instruct via Hugging Face Inference Providers`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`five independent greedy-decoding runs per task for pass^5`；SLO=`money movement must be staged and never executed`；evaluator=`pass^1, pass^5, state-diff correctness, forbidden side effects and approval compliance`。

**Trade-off、failure、共存与演进。** synthetic finance workflow 与规则覆盖有限；state-diff checker 不证明真实法规、身份或银行 effect，pass@k 也不能隐藏每次 unauthorized action。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22000v1 — §7 Limitations and Ethics`。

<!-- claim:SF-2026-ARXIV-2606-22000:start -->
Claim boundary：仅 `arXiv:2606.22000v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22000:end -->
<!-- review:SF-2026-ARXIV-2606-22000:end -->

<!-- review:SF-2026-ARXIV-2606-22013:start -->
### 2606.22013 — Load Testing for Machine Learning Model Serving Systems at Scale

**问题与旧路径。** 该 family 针对 `adaptive open-loop load testing for ML model-serving capacity` 暴露的具体缺口是：Ch73 需把 load test 从固定 QPS 清单升级为可复算 SLO-boundary search contract。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 工业 model-serving systems 上比较 capacity-search cost、SLO boundary accuracy 与固定-grid baseline。 Method=`https://arxiv.org/html/2606.22013v1 — §2 System Design and Methodology; §2.2 Load Testing Strategies; §2.3 Health Assessment Engine`；Evaluation=`https://arxiv.org/html/2606.22013v1 — §3 Experimental Methodology; §4 Results`。Benchmark contract：model=`14 anonymized production models M1–M14: recommendation, ranking, vision and NLP; 80M–1.5B parameters`；hardware=`NVIDIA A100 80GB and H100 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`model-specific latency/error SLO; capacity is maximum QPS at SLO compliance`；evaluator=`capacity deviation, test duration, run stability and SLO compliance`。

**Trade-off、failure、共存与演进。** 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22013v1 — §5 Discussion; Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2606-22013:start -->
Claim boundary：仅 `arXiv:2606.22013v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22013:end -->
<!-- review:SF-2026-ARXIV-2606-22013:end -->

<!-- review:SF-2026-ARXIV-2606-22019:start -->
### 2606.22019 — Channel Location Constrains the Auditability of Subliminal Learning

**问题与旧路径。** 该 family 针对 `pre-training audit of initialization-dependent body, vocabulary and conditional-behaviour channels` 暴露的具体缺口是：Ch72 需明确 audit coverage 与 outcome 分离：未覆盖 channel 只能是 Unknown。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 受控 channel-location 实验比较 audit signal、downstream learning 与干预，展示相同 payload 在不同 channel 的可审计性变化。 Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel`。Benchmark contract：model=`Pythia 70M–6.9B, Qwen3.5-0.8B, Qwen2.5-3B-Instruct, OLMo-2-1B, Gemma-3 270M/1B/4B, RedPajama-3B and RWKV-4-3B`；hardware=`Not Disclosed`；precision=`mixed precision; Appendix A includes a bf16 recipe sweep`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`coverage AUROC/correlation, held-out transfer and causal channel ablations`。

**Trade-off、failure、共存与演进。** 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22019v1 — §8 Discussion, limitations, and related work`。

<!-- claim:SF-2026-ARXIV-2606-22019:start -->
Claim boundary：仅 `arXiv:2606.22019v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22019:end -->
<!-- review:SF-2026-ARXIV-2606-22019:end -->

<!-- review:SF-2026-ARXIV-2606-22030:start -->
### 2606.22030 — When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense

**问题与旧路径。** 该 family 针对 `LoCoMo: 10 conversations, 1,540 questions across four categories` 暴露的具体缺口是：当前 Ch77 已要求 source calibration、valid-time、独立 corroboration、contradiction、supersession 与 risk-aware selective action共同约束事实 Memory；Bayesian 聚合是既有可靠性读路径的受限实现。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** belief memory 以 Bayesian state 表示候选命题，但只在 source reliability 可估时更新；provenance-capped influence 限制单源/重复证据对 posterior 的控制。 唯一知识 owner 为 `AGENT-MEMORY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 多任务 memory benchmark 中，plain Bayesian update 无稳定收益；reliability-conditioned update 提升 strict F1，并在 poisoning 下比较 provenance cap。 Method=`https://arxiv.org/html/2606.22030v1 — §3 The Nous Architecture; §3.3 Bayesian Update; §3.7 Pipelines`；Evaluation=`https://arxiv.org/html/2606.22030v1 — §4 Experimental Setup; §5 Results; §6 Analysis`。Benchmark contract：model=`GPT-4o-mini for extraction, answer generation and judging; A-MEM and BeliefMem are self-reported baselines`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`strict token F1, BLEU-1, context recall and GPT-4o-mini failure buckets`。

**Trade-off、failure、共存与演进。** A-MEM/BeliefMem 数字未由作者重跑且二手表格类别映射曾冲突；GPT-4o-mini 同时做 extraction、answer 与 judge，strict F1 和 judge 可能共偏。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22030v1 — §7 Limitations and Future Work; §5 A caveat on the A-MEM comparison`。

<!-- claim:SF-2026-ARXIV-2606-22030:start -->
Claim boundary：仅 `arXiv:2606.22030v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22030:end -->
<!-- review:SF-2026-ARXIV-2606-22030:end -->

<!-- review:SF-2026-ARXIV-2606-22043:start -->
### 2606.22043 — When Does a Video-Language Model Stop Watching? Reward Strength Controls the Formation and Reversal of Visual Shortcuts in Multimodal RLVR

**问题与旧路径。** 该 family 针对 `GRPO-style video-QA RLVR with reward-strength and intervention-time controls` 暴露的具体缺口是：Ch33 需把 visual reliance 作为训练 trajectory state，而不只在最终 accuracy 后诊断 shortcut。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** Qwen3-VL-8B-Instruct 的多 seed、lambda∈{0,1,2} 与 intervention-timing 轨迹上测 VHS、accuracy 与 onset/reversal；representation probe 落在 bootstrap variability 内，只是探索性观察。 Method=`https://arxiv.org/html/2606.22043v1 — §2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet`；Evaluation=`https://arxiv.org/html/2606.22043v1 — §3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details`。Benchmark contract：model=`Qwen3-VL-8B-Instruct`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`held-out OOD visual-hacking score, accuracy and onset/reversal trajectory`。

**Trade-off、failure、共存与演进。** 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22043v1 — §8 Discussion and limitations — Limitations`。

<!-- claim:SF-2026-ARXIV-2606-22043:start -->
Claim boundary：仅 `arXiv:2606.22043v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22043:end -->
<!-- review:SF-2026-ARXIV-2606-22043:end -->

<!-- review:SF-2026-ARXIV-2606-22082:start -->
### 2606.22082 — CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation

**问题与旧路径。** 该 family 针对 `repository-level code generation on SketchEval and NL2Repo-Bench` 暴露的具体缺口是：Ch82 已明确 shared repository 需要 commitment protocol、ownership/interface 和可验证提交顺序。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** CodeTeam 先生成竞争架构草案，再由 CTO 产出 machine-checkable ownership/interface contract，随后依 dependency graph 调度实现并运行 repo tests。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** repository-level generation tasks 上比较单 agent、多 agent、组件 ablation 与测试结果。 Method=`https://arxiv.org/html/2606.22082v1 — §3.2 Design and Implementation of CodeTeam`；Evaluation=`https://arxiv.org/html/2606.22082v1 — §3.3 Benchmark Experiment Design; §3.4 Execution-Based Evaluation; §4 Results`。Benchmark contract：model=`Qwen2.5-72B-Instruct for all PE and SFT agents`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`SketchBLEU, execution-based validation and component ablations`。

**Trade-off、failure、共存与演进。** 所有 agents 共享 Qwen2.5-72B-Instruct，CTO contract 可能共享 backbone bias；test suite 不完备时 machine-checkable 只证明 harness 内一致。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22082v1 — §6 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2606-22082:start -->
Claim boundary：仅 `arXiv:2606.22082v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22082:end -->
<!-- review:SF-2026-ARXIV-2606-22082:end -->

<!-- review:SF-2026-ARXIV-2606-22085:start -->
### 2606.22085 — Can Reasoning Models Detect Changes to their Chains of Thought?

**问题与旧路径。** 该 family 针对 `controlled chain-of-thought tampering on GPQA-Diamond, 200 MMLU-Pro examples and AIME 2025` 暴露的具体缺口是：Ch72 已将 CoT monitor 定义为 policy-bound sensor，不是 security authority；该负结果强化边界。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 通过在 reasoning trace 中植入受控改动测试模型能否自报 CoT tampering；把 self-report、behavioral change 与 external detector 分离。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 多 reasoning models 与 tampering types 上测 detection/acknowledgement，结果显示自我检测弱且不稳定。 Method=`https://arxiv.org/html/2606.22085v1 — §3 Methodology — Experimental settings; Interventions; Data; Models`；Evaluation=`https://arxiv.org/html/2606.22085v1 — §4 Detecting Changes — Completed Condition; Partial Condition; Self-Awareness; §5 Localizing Changes; Appendix D Additional Results`。Benchmark contract：model=`openai/gpt-oss-120b, deepseek/deepseek-v3.2, moonshotai/Kimi-K2.5 and qwen/qwen3-235b-a22b-thinking-2507 via OpenRouter`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`single rollout per example`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`tamper detection, localization and regex-scored verdicts`。

**Trade-off、failure、共存与演进。** 可见 CoT 不是完整内部 computation；专有 frontier API 不支持 CoT prefilling 因而未测，否认/承认都不是 tamper truth。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22085v1 — Limitations; Appendix B Model Details`。

<!-- claim:SF-2026-ARXIV-2606-22085:start -->
Claim boundary：仅 `arXiv:2606.22085v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22085:end -->
<!-- review:SF-2026-ARXIV-2606-22085:end -->

<!-- review:SF-2026-ARXIV-2606-22136:start -->
### 2606.22136 — Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data

**问题与旧路径。** 该 family 针对 `50,000 world-model-generated egocentric episodes; 18 real-robot tasks on Unitree G1 with Inspire hands` 暴露的具体缺口是：当前 Ch27 已完整写入 human hand pose→action-conditioned video→pose/depth reconstruction/retargeting→derived robot trajectory provenance→real closed-loop admission；Wh0 正是该现有分支的 source-specific evidence。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Wh0 用 generative video world model 产生 scene/object/language-conditioned human-hand episodes，再以 hand reconstruction 与 visual editing 转成 robot-trainable supervision，并与少量真实机器人数据 co-train。 唯一知识 owner 为 `TRAIN-DATA`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 50K WM-H episodes、18 个真实 dexterous tasks；相对仅 robot data，未见任务 zero-shot success 从 8.3% 升至 38.9%。 Method=`https://arxiv.org/html/2606.22136v1 — §3 WM-H Dataset Construction via Controllable Video Synthesis; §4 Wh0: Policy Learning with Human-Robot Alignment`；Evaluation=`https://arxiv.org/html/2606.22136v1 — §5 Experiments; §5.1 Experimental Setup`。Benchmark contract：model=`VITRA dexterous VLA post-trained with WM-H and robot data`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`real-robot zero-shot success and generation/alignment ablations`。

**Trade-off、failure、共存与演进。** 生成世界模型会携带 physics/contact error，视觉编辑不等于 action 可执行；真实 robot data 仍是 deployment anchor，18 tasks 不证明广泛迁移。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22136v1 — §6 Conclusion and Limitations; Appendix A.6 Failure Cases`。

<!-- claim:SF-2026-ARXIV-2606-22136:start -->
Claim boundary：仅 `arXiv:2606.22136v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22136:end -->
<!-- review:SF-2026-ARXIV-2606-22136:end -->

<!-- review:SF-2026-ARXIV-2606-22142:start -->
### 2606.22142 — RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations

**问题与旧路径。** 该 family 针对 `repeated robot rollout-review-dataset-train-evaluate-release cycles` 暴露的具体缺口是：Ch27 需把 sample lineage 扩展为 rollout→review→dataset→training→evaluation→release 的 typed lifecycle graph。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。 唯一知识 owner 为 `TRAIN-DATA`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 真实机器人 policy-iteration workflow 中比较常规流程与 lineage layer 的迭代时间、审计性和 downstream policy performance。 Method=`https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance`；Evaluation=`https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`review reliability, policy quality, effort and recollection case studies`。

**Trade-off、failure、共存与演进。** robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion`。

<!-- claim:SF-2026-ARXIV-2606-22142:start -->
Claim boundary：仅 `arXiv:2606.22142v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22142:end -->
<!-- review:SF-2026-ARXIV-2606-22142:end -->

<!-- review:SF-2026-ARXIV-2606-22164:start -->
### 2606.22164 — Drowning in Routine: Signal Dilution in Multi-Turn Agent Training

**问题与旧路径。** 该 family 针对 `multi-turn RL with tunable consequential-decision density` 暴露的具体缺口是：Ch33 需把 decision density 纳入 credit-assignment route：长轨迹本身不是选择 critic 的充分条件。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 可精确调 ρ 的 controlled environment 复现 turn-level/trajectory-level SNR 比例，R²=0.999，并测 training-step gap。 Method=`https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem`；Evaluation=`https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results`。Benchmark contract：model=`30K-parameter causal Transformer with two pre-norm blocks, model dimension 32, two attention heads and feed-forward width 128`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`trajectory-level group G=16; turn-level Monte Carlo critic k=8; initialization SNR N=1,024`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`gradient SNR and training iterations to threshold`。

**Trade-off、failure、共存与演进。** 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors`。

<!-- claim:SF-2026-ARXIV-2606-22164:start -->
Claim boundary：仅 `arXiv:2606.22164v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22164:end -->
<!-- review:SF-2026-ARXIV-2606-22164:end -->

<!-- review:SF-2026-ARXIV-2606-22175:start -->
### 2606.22175 — StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era

**问题与旧路径。** 该 family 针对 `PromptVerify over 145,449 FEVER training claims` 暴露的具体缺口是：Ch81 需把 workflow task identity 分成 state-holder 与 invocation；复用必须绑定 model/runtime version 和 tenant。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 145,449-claim PromptVerify workflow 在 20 GPU stable testbed 获 3.6×，并扩到 186 个闲置 GPU 后 784 秒完成。 Method=`https://arxiv.org/html/2606.22175v1 — §II Implementation of an LLM-integrated Claim Verification Workflow; §III Transforming the Workflow to Enable StickyInvoc`；Evaluation=`https://arxiv.org/html/2606.22175v1 — §IV Evaluation; §IV-A Experiment Settings`。Benchmark contract：model=`SmolLM2 1.7B`；hardware=`stable pool: 10 NVIDIA A10 + 10 TITAN X Pascal; scale-out up to 186 GPUs`；precision=`Not Disclosed`；batch=`varied inference batch sizes in RQ3`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`makespan, startup amortization and scale-out completion time`。

**Trade-off、failure、共存与演进。** persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22175v1 — §I-E Limitation of the Proposed Approach`。

<!-- claim:SF-2026-ARXIV-2606-22175:start -->
Claim boundary：仅 `arXiv:2606.22175v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22175:end -->
<!-- review:SF-2026-ARXIV-2606-22175:end -->

<!-- review:SF-2026-ARXIV-2606-22179:start -->
### 2606.22179 — The Score Granularity Gap in Black-Box LLM Classification: A Comparative Study of Confidence Constructions

**问题与旧路径。** 该 family 针对 `2,890 BoolQ, MNLI and PubMedQA black-box classification examples` 暴露的具体缺口是：Ch66 需增加 threshold-resolution contract：ranking 好不代表 operator 有足够可选 operating points。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 9 个 LLM、3 个 benchmark、25 个 model-dataset pair，对七种 confidence construction 比较 ranking、阈值粒度与 inference cost。 Method=`https://arxiv.org/html/2606.22179v1 — §3 Problem Setup; §4 Confidence Constructions`；Evaluation=`https://arxiv.org/html/2606.22179v1 — §5 Experiments; §5.1 Setup`。Benchmark contract：model=`Llama-3.1-70B/8B, Gemini-2.5-Flash, Gemini-2.0-Flash-Lite, Claude-Haiku-4.5, GPT-4o-mini, GPT-4.1-mini/nano and GPT-5-nano`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`risk ranking, distinct threshold granularity and inference cost`。

**Trade-off、failure、共存与演进。** 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22179v1 — §7 Limitations; §6 Deployment Recommendations`。

<!-- claim:SF-2026-ARXIV-2606-22179:start -->
Claim boundary：仅 `arXiv:2606.22179v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22179:end -->
<!-- review:SF-2026-ARXIV-2606-22179:end -->

<!-- review:SF-2026-ARXIV-2606-22180:start -->
### 2606.22180 — FeLoG: Scalable and Efficient Distributed Graph Embedding with Feedback Loop Mechanism

**问题与旧路径。** 该 family 针对 `large-scale graph embedding with sampling and distributed training` 暴露的具体缺口是：Ch36 需增加 sampling→quality feedback loop 与 communication freshness 的联合 contract，而非仅 pipeline overlap。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 六个系统 baseline 与大图数据上平均 27.9× speedup、通信降超 53.1%、CPU-GPU utilization 超 80%。 Method=`https://arxiv.org/html/2606.22180v1 — §5 FeLoG; §5.1 Feedback-coupled Sampling-Training Model; §5.2 Activity-aware Communication`；Evaluation=`https://arxiv.org/html/2606.22180v1 — §6 Experimental Results; §6.1 Experimental Setup`。Benchmark contract：model=`FeLoG, PyTorch-BigGraph, DistDGL, DistGER, DistGER-G, NeutronTP and LeapGNN`；hardware=`8 machines, each with a 2.60 GHz Intel Xeon Gold 6240 CPU (36 cores/72 threads), NVIDIA V100 32 GB, 192 GB DDR4 and full-duplex 10 Gbps networking; GraNNDis comparison on four NVIDIA A40 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`time-to-quality, communication volume and CPU-GPU utilization`。

**Trade-off、failure、共存与演进。** quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22180v1 — §7 Conclusions and experimental generalizability boundary`。

<!-- claim:SF-2026-ARXIV-2606-22180:start -->
Claim boundary：仅 `arXiv:2606.22180v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22180:end -->
<!-- review:SF-2026-ARXIV-2606-22180:end -->

<!-- review:SF-2026-ARXIV-2606-22189:start -->
### 2606.22189 — L20-Edu-135M: An Auditable Single-GPU Study of Data-Efficient Small Language Modeling

**问题与旧路径。** 该 family 针对 `single-GPU 134.5M language-model pretraining, SFT and RLVR` 暴露的具体缺口是：Ch27 已拥有 data gates、dedup、contamination 与 provenance；保留此单 GPU negative RLVR case，不新增 owner。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 在单张 L20 上公开 134.5M 模型的 data gate、cross-source MinHash/LSH、segment dedup、benchmark-overlap removal、SFT weight interpolation 与 RLVR 全链。 唯一知识 owner 为 `TRAIN-DATA`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 约 13B token、自跑六任务 harness；均分 0.4150；直接 GRPO-style RLVR 使 GSM8K exact match 从 1.82% 降至 1.59%/1.21%。 Method=`https://arxiv.org/html/2606.22189v1 — §3 System Overview; §4 Data Quality and Contamination Control; §5 Training Efficiency`；Evaluation=`https://arxiv.org/html/2606.22189v1 — §6 Evaluation Protocol; §7 Results`。Benchmark contract：model=`L20-Edu-135M, SmolLM-135M, SmolLM2-135M, Qwen2.5-0.5B, OLMo-1B and older 100M–160M baselines`；hardware=`one NVIDIA L20 48GB GPU`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`six-task zero-shot mean and GSM8K exact match`。

**Trade-off、failure、共存与演进。** 单 run、自有 harness、小模型与 nominal-token ratio 不证明 scaling law 或统计等价；RLVR 下降只是具体 failure case。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22189v1 — §9 Limitations; §10 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2606-22189:start -->
Claim boundary：仅 `arXiv:2606.22189v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22189:end -->
<!-- review:SF-2026-ARXIV-2606-22189:end -->

<!-- review:SF-2026-ARXIV-2606-22203:start -->
### 2606.22203 — When Is Emergent Consensus Real? A Measured Coupling Gain and a Validity Diagnostic for LLM Agent Societies

**问题与旧路径。** 该 family 针对 `LLM-agent opinion dynamics under pairwise and group interaction` 暴露的具体缺口是：Ch82 需禁止用 pairwise interaction 参数外推 group dynamics，并把 model-prior drift 从 emergent consensus 分离。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 5 个 frontier model 测 pairwise gamma，16 个 closed/open model 测 group coupling；复核既有 emergent-consensus 结果并发现 settled facts 上是 prior artifact。 Method=`https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory`；Evaluation=`https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results`。Benchmark contract：model=`deepseek-v4-pro, gpt-5.5, claude-opus-4.8, gemini-3.5-flash, qwen3.7-max, Llama-3.1-8B, Llama-3.1-70B, Llama-3.3-70B, Llama-4-Maverick, Qwen-2.5-7B, Qwen-2.5-72B, Mistral-Large, Mistral-Small, Mixtral-8x22B, Gemma-2-27B and DeepSeek-Chat`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`coupling gain, final-versus-initial slope/bias, consensus and polarization regime`。

**Trade-off、failure、共存与演进。** pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary`。

<!-- claim:SF-2026-ARXIV-2606-22203:start -->
Claim boundary：仅 `arXiv:2606.22203v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22203:end -->
<!-- review:SF-2026-ARXIV-2606-22203:end -->

<!-- review:SF-2026-ARXIV-2606-22248:start -->
### 2606.22248 — SamatNext v0.2-B: An Exploratory Study of RMS-Normalized Hybrid Decoders for Curriculum Retention in Small Code Models

**问题与旧路径。** 该 family 针对 `sequential Python-code curriculum` 暴露的具体缺口是：Ch27 已把 curriculum state 与 retention Gate 分离；本 family 仅是架构受限案例。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** SamatNext 交替 Differential-Attention 与简化 DeltaNet state mixer，用 RMS normalization/output calibration 测试 staged code curriculum 的 retention/plasticity。 唯一知识 owner 为 `TRAIN-DATA`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 356M 参数、受控 Python curriculum；Stage 5 100%、相邻 Stage 3 保留 98.8%，但早期 Stage 2E 仅 12%；matched Transformer Stage 3 仅 6%。 Method=`https://arxiv.org/html/2606.22248v1 — §3 SamatNext v0.2-B Architecture; §4 Curriculum and Evaluation Setup`；Evaluation=`https://arxiv.org/html/2606.22248v1 — §5 Empirical Results`。Benchmark contract：model=`SamatNext v0.2-B 356M and a parameter-matched Transformer`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`current-stage pass rate and adjacent/early-stage semantic retention`。

**Trade-off、failure、共存与演进。** 单一受控 curriculum、单 architecture size 且 long-horizon retention 仍弱；不能外推为解决 catastrophic forgetting。 因此维持既有 owner 作为长期机制，不把这一受限实例复制成新分支。 Limit/counterevidence=`https://arxiv.org/html/2606.22248v1 — §8 Limitations; §6.4 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2606-22248:start -->
Claim boundary：仅 `arXiv:2606.22248v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22248:end -->
<!-- review:SF-2026-ARXIV-2606-22248:end -->

<!-- review:SF-2026-ARXIV-2606-22263:start -->
### 2606.22263 — Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases

**问题与旧路径。** 该 family 针对 `seven mature production projects and 100 randomly selected Arvo/CyberGym projects` 暴露的具体缺口是：Ch72 需把 vulnerability report 的 commit authority 绑定 executable PoV+sanitizer，而非 agent verdict。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** 7 个持续 fuzz 5–8 年的生产项目与 100 个随机 Arvo/CyberGym 项目；约每项目 1 小时、总成本 300 美元，发现 19 个未知 memory-safety 漏洞。 Method=`https://arxiv.org/html/2606.22263v1 — §III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction`；Evaluation=`https://arxiv.org/html/2606.22263v1 — §V Evaluation`。Benchmark contract：model=`Claude Haiku 4.5 for hypothesis generation and Claude Sonnet 4.6 for PoV construction; Opus 4.7, GPT-5.5 and Sorcar baselines`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`sanitizer-confirmed vulnerabilities, targeted recall and token cost`。

**Trade-off、failure、共存与演进。** sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22263v1 — §VI Discussion and Limitations`。

<!-- claim:SF-2026-ARXIV-2606-22263:start -->
Claim boundary：仅 `arXiv:2606.22263v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22263:end -->
<!-- review:SF-2026-ARXIV-2606-22263:end -->

<!-- review:SF-2026-ARXIV-2606-22283:start -->
### 2606.22283 — Apple Neural Engine: Architecture, Programming, and Performance

**问题与旧路径。** 该 family 针对 `Apple Neural Engine architecture, compilation and measured performance` 暴露的具体缺口是：Ch54 需把硬件逆向知识按 measured/decompile-derived/predicted 分层，并保持 Core ML 是唯一 supported production path。 旧路径仍负责未被 exact-v1 证明覆盖的输入与 failure domain。

**机制与 owner。** 对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。 唯一知识 owner 为 `INFER-GPU-MEMORY`；相邻章节只消费版本化 handoff。

**Evaluation：证明与未证明。** A11–A18、M1–M5 目标表；直接测量只在 M1/M5，结合静态分析给出 operation-device matrix 与性能/能耗边界。 Method=`https://arxiv.org/html/2606.22283v1 — §Part II Reaching the ANE — Software stack; Dispatching without Core ML; §Part VI The Silicon — Datapath and MAC geometry; §Part VII The Toolchain and Encoding; §Part VIII System Internals`；Evaluation=`https://arxiv.org/html/2606.22283v1 — §Part III Performance and Fit — Roofline; Power and efficiency; Across the chip family; Appendix A Operation-by-device matrix; Appendix E Provenance`。Benchmark contract：model=`Core ML models and direct ANE programs used in the guide`；hardware=`Apple M1 and M5 measured; A11-A18 and M1-M5 documented/predicted matrix`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`measured roofline/energy plus operation-by-device support matrix`。

**Trade-off、failure、共存与演进。** private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。 因此只合入该 family 的最小机制 delta；原 owner 的确定性路径与人工审批边界继续共存。 Limit/counterevidence=`https://arxiv.org/html/2606.22283v1 — §Part V Practice — Pitfalls and limits; §Methodology; §Open questions; §Introduction — direct route is undocumented, unsupported and version-fragile`。

<!-- claim:SF-2026-ARXIV-2606-22283:start -->
Claim boundary：仅 `arXiv:2606.22283v1` official HTML；不使用 later version；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-22283:end -->
<!-- review:SF-2026-ARXIV-2606-22283:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21822 | CN memory-safety specification synthesis for small-to-medium C functions | OpenAI o3, o1, o1-mini, o3-mini and GPT-4o | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | first-attempt and eventual valid-annotation rate plus unsafe-function handling |
| SF-2026-ARXIV-2606-21836 | DNN accelerator mapping, hardware/software co-design and CPU cache-hierarchy DSE | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | EDP or IPC under matched simulator-call budgets and trace audit |
| SF-2026-ARXIV-2606-21842 | multi-tenant RAG with non-prefix KV-cache fusion | LongChat-7B-v1.5-32K and Qwen2.5-7B-Instruct targets; Gemini-3-Pro extraction agent | 4 NVIDIA A40 GPUs with 48 GB VRAM each and 256 GB system RAM | Not Disclosed | about 2,000-token shared document chunk in Scenario A | Not Disclosed | maximum batch size 16 | Poisson background arrivals at 0.004 requests per second per client | Not Disclosed | extraction success, requests per token, TTFT signal and defense throughput |
| SF-2026-ARXIV-2606-21843 | identity-conditioning probes across base, 4,200-token Card-conditioned, repetitive-padded and diverse-padded contexts | Anthropic Claude Sonnet API backing the persistent Ada agent | Not Disclosed | Not Disclosed | about 4K baseline, 155K medium and 280K long contexts; diverse-padding control through 150K | first token or first 10 tokens, depending on probe | 50 samples per probe × condition × context-length combination | Not Disclosed | Not Disclosed | next-token entropy, sqrt-JSD distance and magnitude-homology diagnostics |
| SF-2026-ARXIV-2606-21848 | language modeling and downstream reasoning with QKV versus QVV attention | GPT-2 280M, GPT-2 557M, Pythia 410M, Qwen2 1.5B and Llama 3.2 1B | Not Disclosed | Not Disclosed | 512, 2,048 and 8,192 tokens for the Qwen2-1.5B throughput benchmark | 256 generated tokens for the Qwen2-1.5B throughput benchmark | 1 for the Qwen2-1.5B throughput benchmark | Not Disclosed | Not Disclosed | perplexity, downstream accuracy and value-only cache memory |
| SF-2026-ARXIV-2606-21854 | large-scale speech/audio pre-training and fine-tuning recipes | OWSM-Base 102M | 4 nodes with 4 NVIDIA H100 GPUs per node, 16 H100 total | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | epoch time averaged over five consecutive epochs, GPU utilization, CHiME-4 WER at 350k updates and integration code delta |
| SF-2026-ARXIV-2606-21856 | multi-principal tool-using agent tasks with shared and private state | deepseek-v4-pro, qwen3.6-35b-a3b, gemini-2.5-flash and gpt-4.1-nano via OpenRouter | Not Disclosed | Not Disclosed | Not Disclosed | 4,096 or 16,384 maximum tokens by benchmark module | Not Disclosed | 16 max_workers | Not Disclosed | task completion plus deterministic governance-policy outcomes |
| SF-2026-ARXIV-2606-21868 | Mixture-of-Experts autoregressive serving under constrained device memory | Qwen3-30B-A3B, MiniMax-M2 229B FP8, Jamba-v0.1 52B, Kimi-VL and OLMoE | single NVIDIA H100 NVL with 95,830 MiB; Qwen3/Kimi constrained-device arms emulated by memory cap | BF16 for Qwen3-30B-A3B; FP8 for MiniMax-M2 | Not Disclosed | Not Disclosed | Not Disclosed | maximum concurrency at 4,096 tokens varies with KV allocation | Not Disclosed | decode throughput, expert/KV residency, transfer and quality |
| SF-2026-ARXIV-2606-21869 | multilingual inference over Belebele, translated GSM8K and LM-Arena prompts | Qwen3-8B, Qwen3-14B, Qwen3-32B, Gemma-3-27B and Llama-3.1-8B-Instruct | NVIDIA L40S 48 GB and RTX 6000 Pro Blackwell 96 GB GPUs | Not Disclosed | Not Disclosed | Not Disclosed | 256 except batch-sweep values 16, 32, 64, 128, 256 and 512 | Not Disclosed | Not Disclosed | per-language energy, token count and task accuracy |
| SF-2026-ARXIV-2606-21875 | risk triage among already-confident tabular predictions | standardized or balanced logistic regression, random forest and histogram gradient boosting classifiers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | conditional error ranking, held-out ScopeGate direction and compute cost |
| SF-2026-ARXIV-2606-21877 | pre-deployment agent authority/risk artifact validation | Aider, OpenHands, SWE-agent, Cline, Goose, Open Interpreter, AutoGPT, PrivateGPT, GPT-Researcher, MetaGPT, CrewAI, AutoGen and BabyAGI | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | schema fillability, risk visibility, mutation-diff correctness and scorer rank consistency |
| SF-2026-ARXIV-2606-21884 | nine deterministic-generator reasoning tasks | Nemotron-3-Nano 30B/3.5B active, Llama-3.2-3B, Qwen3.5-4B, gpt-oss-20b 21B/3.6B active, DeepSeek-V3.1 671B/37B active and Nemotron-Super 120B/12B active | Not Disclosed | Not Disclosed | 7680-token generation budget in the primary setup | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | solver coverage, CoT transfer, line fidelity, hit@k and intervention accuracy |
| SF-2026-ARXIV-2606-21891 | 22 automated ML research tasks from MLGym and MLEBench | OpenAI o3 scientist, Gemini 3 Flash executor and Qwen3-4B-Instruct test-time-trained scientist | one 40 GB NVIDIA A100 for each inference-only method; three 40 GB NVIDIA A100 GPUs for each test-time-training run | Not Disclosed | 8,192-token rollout sequence length | up to 120 scientist turns of 1,024 tokens each | 8 rollouts per GRPO group | Not Disclosed | Not Disclosed | best validation score, IQM, optimality gap, wall time and hypothesis/execution attribution |
| SF-2026-ARXIV-2606-21917 | pre-generation hallucination-risk prediction on SQuAD, Natural Questions and HotpotQA | Qwen2.5-3B, Qwen2.5-7B, Qwen3.5-9B, Llama-2-7B and Gemma-4-E2B instruction-tuned models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | probe-training batch size 8 or 16; soft targets use 10 samples per prompt | Not Disclosed | Not Disclosed | ROC-AUC, calibration and routing utility |
| SF-2026-ARXIV-2606-21954 | ECLeKTic, MGSMv2 and MMLU-ProX-Lite cross-lingual transfer | Gemini-2.5-Flash, Gemini-2.5-Flash Thinking-Off, Gemini-3-Flash, Gemini-3-Flash Low, Gemini-3-Flash Minimal, Gemma-3-1B, Gemma-3-4B, Gemma-3-12B, Gemma-3-27B, Gemma-4-E2B-IT, Gemma-4-E4B-IT, Gemma-4-26B-A4B-IT, Gemma-4-31B-IT, Claude-Haiku-4.5, Claude-Sonnet-4.6, Claude-Opus-4.7, Qwen-3-4B, Qwen-3-30B-A3B, GPT-OSS-20B and GPT-OSS-120B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 10 promptings per source/target item for HAT estimation | Not Disclosed | Not Disclosed | Hardness Adjusted Transfer versus raw source/target accuracy |
| SF-2026-ARXIV-2606-21959 | 657-question OpenBioRQ core and 423-question frozen core | GLM-5.1, Qwen3.6, DeepSeek-V4, GLM-5, Qwen3.5-397B, Qwen3-235B, Gemini-3-Pro, Opus-4.7 and GPT-5.5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | two-level citation factuality, checklist solve rate, tool use and judge agreement |
| SF-2026-ARXIV-2606-21963 | mixed-language mobile crash diagnosis over WeChat crash artifacts | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | function-level fault-localization accuracy, diagnosis time and ablations |
| SF-2026-ARXIV-2606-21968 | visual RAG under resolution-context trade-off | LLaVA-v1.5-7B, LLaVA-v1.5-13B, LLaVA-OneVision-0.5B and Qwen3-VL | Not Disclosed | Not Disclosed | Not Disclosed | single token for evaluation consistency | Not Disclosed | Not Disclosed | Not Disclosed | task accuracy, inference time and route-selection ablations |
| SF-2026-ARXIV-2606-21994 | DAPO-Math-17K training; AIME24, AIME25, AMC23, HMMT24 and HMMT25 evaluation | DeepSeek-R1-Distill-Qwen-1.5B, JustRL-DeepSeek-1.5B, OpenMath-1.5B, JustRL-Nemotron-1.5B, DeepSeek-R1-Distill-Qwen-7B, Qwen3-4B-Base and Qwen3-4B | Not Disclosed | Not Disclosed | maximum prompt length 1,024 | maximum response length 7,168 | training mini-batch 64 with 4 responses per prompt | Not Disclosed | Not Disclosed | benchmark accuracy, training time and rollout allocation |
| SF-2026-ARXIV-2606-22000 | 40 oracle-validated autonomous construction-finance tasks across eight domains | DeepSeek-V3.1, Qwen3-235B-A22B-Instruct and Qwen2.5-72B-Instruct via Hugging Face Inference Providers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | five independent greedy-decoding runs per task for pass^5 | money movement must be staged and never executed | pass^1, pass^5, state-diff correctness, forbidden side effects and approval compliance |
| SF-2026-ARXIV-2606-22013 | adaptive open-loop load testing for ML model-serving capacity | 14 anonymized production models M1–M14: recommendation, ranking, vision and NLP; 80M–1.5B parameters | NVIDIA A100 80GB and H100 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | model-specific latency/error SLO; capacity is maximum QPS at SLO compliance | capacity deviation, test duration, run stability and SLO compliance |
| SF-2026-ARXIV-2606-22019 | pre-training audit of initialization-dependent body, vocabulary and conditional-behaviour channels | Pythia 70M–6.9B, Qwen3.5-0.8B, Qwen2.5-3B-Instruct, OLMo-2-1B, Gemma-3 270M/1B/4B, RedPajama-3B and RWKV-4-3B | Not Disclosed | mixed precision; Appendix A includes a bf16 recipe sweep | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | coverage AUROC/correlation, held-out transfer and causal channel ablations |
| SF-2026-ARXIV-2606-22030 | LoCoMo: 10 conversations, 1,540 questions across four categories | GPT-4o-mini for extraction, answer generation and judging; A-MEM and BeliefMem are self-reported baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | strict token F1, BLEU-1, context recall and GPT-4o-mini failure buckets |
| SF-2026-ARXIV-2606-22043 | GRPO-style video-QA RLVR with reward-strength and intervention-time controls | Qwen3-VL-8B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | held-out OOD visual-hacking score, accuracy and onset/reversal trajectory |
| SF-2026-ARXIV-2606-22082 | repository-level code generation on SketchEval and NL2Repo-Bench | Qwen2.5-72B-Instruct for all PE and SFT agents | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | SketchBLEU, execution-based validation and component ablations |
| SF-2026-ARXIV-2606-22085 | controlled chain-of-thought tampering on GPQA-Diamond, 200 MMLU-Pro examples and AIME 2025 | openai/gpt-oss-120b, deepseek/deepseek-v3.2, moonshotai/Kimi-K2.5 and qwen/qwen3-235b-a22b-thinking-2507 via OpenRouter | Not Disclosed | Not Disclosed | Not Disclosed | 10,000 max tokens in completed-condition detection; judge max_tokens 16 | single rollout per example | Not Disclosed | Not Disclosed | tamper detection, localization and regex-scored verdicts |
| SF-2026-ARXIV-2606-22136 | 50,000 world-model-generated egocentric episodes; 18 real-robot tasks on Unitree G1 with Inspire hands | VITRA dexterous VLA post-trained with WM-H and robot data | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | real-robot zero-shot success and generation/alignment ablations |
| SF-2026-ARXIV-2606-22142 | repeated robot rollout-review-dataset-train-evaluate-release cycles | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | review reliability, policy quality, effort and recollection case studies |
| SF-2026-ARXIV-2606-22164 | multi-turn RL with tunable consequential-decision density | 30K-parameter causal Transformer with two pre-norm blocks, model dimension 32, two attention heads and feed-forward width 128 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | trajectory-level group G=16; turn-level Monte Carlo critic k=8; initialization SNR N=1,024 | Not Disclosed | Not Disclosed | gradient SNR and training iterations to threshold |
| SF-2026-ARXIV-2606-22175 | PromptVerify over 145,449 FEVER training claims | SmolLM2 1.7B | stable pool: 10 NVIDIA A10 + 10 TITAN X Pascal; scale-out up to 186 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | varied inference batch sizes in RQ3 | Not Disclosed | Not Disclosed | makespan, startup amortization and scale-out completion time |
| SF-2026-ARXIV-2606-22179 | 2,890 BoolQ, MNLI and PubMedQA black-box classification examples | Llama-3.1-70B/8B, Gemini-2.5-Flash, Gemini-2.0-Flash-Lite, Claude-Haiku-4.5, GPT-4o-mini, GPT-4.1-mini/nano and GPT-5-nano | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | risk ranking, distinct threshold granularity and inference cost |
| SF-2026-ARXIV-2606-22180 | large-scale graph embedding with sampling and distributed training | FeLoG, PyTorch-BigGraph, DistDGL, DistGER, DistGER-G, NeutronTP and LeapGNN | 8 machines, each with a 2.60 GHz Intel Xeon Gold 6240 CPU (36 cores/72 threads), NVIDIA V100 32 GB, 192 GB DDR4 and full-duplex 10 Gbps networking; GraNNDis comparison on four NVIDIA A40 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | time-to-quality, communication volume and CPU-GPU utilization |
| SF-2026-ARXIV-2606-22189 | single-GPU 134.5M language-model pretraining, SFT and RLVR | L20-Edu-135M, SmolLM-135M, SmolLM2-135M, Qwen2.5-0.5B, OLMo-1B and older 100M–160M baselines | one NVIDIA L20 48GB GPU | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | six-task zero-shot mean and GSM8K exact match |
| SF-2026-ARXIV-2606-22203 | LLM-agent opinion dynamics under pairwise and group interaction | deepseek-v4-pro, gpt-5.5, claude-opus-4.8, gemini-3.5-flash, qwen3.7-max, Llama-3.1-8B, Llama-3.1-70B, Llama-3.3-70B, Llama-4-Maverick, Qwen-2.5-7B, Qwen-2.5-72B, Mistral-Large, Mistral-Small, Mixtral-8x22B, Gemma-2-27B and DeepSeek-Chat | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | coupling gain, final-versus-initial slope/bias, consensus and polarization regime |
| SF-2026-ARXIV-2606-22248 | sequential Python-code curriculum | SamatNext v0.2-B 356M and a parameter-matched Transformer | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | current-stage pass rate and adjacent/early-stage semantic retention |
| SF-2026-ARXIV-2606-22263 | seven mature production projects and 100 randomly selected Arvo/CyberGym projects | Claude Haiku 4.5 for hypothesis generation and Claude Sonnet 4.6 for PoV construction; Opus 4.7, GPT-5.5 and Sorcar baselines | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | sanitizer-confirmed vulnerabilities, targeted recall and token cost |
| SF-2026-ARXIV-2606-22283 | Apple Neural Engine architecture, compilation and measured performance | Core ML models and direct ANE programs used in the guide | Apple M1 and M5 measured; A11-A18 and M1-M5 documented/predicted matrix | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | measured roofline/energy plus operation-by-device support matrix |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21822 | potential_books_delta | not_selected | — | — | Ch72 已要求 coding-agent 安全真值来自 executable evidence；本 family 增加 CN 具体实例但不改变 owner。 Exact-v1 supports: 31 个可标注函数与 3 个故意不安全函数上，o3 首轮 90%、总计 97%，GPT-4o 首轮 65%。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 测试通过只覆盖生成状态，不是全路径证明；safe-but-unexpressible、搜索失败与真实 unsafe 仍可能落入同一失败出口。 | analysis-decision:SF-2026-ARXIV-2606-21822 |
| SF-2026-ARXIV-2606-21836 | potential_books_delta | not_selected | — | — | Ch81 已拥有 evaluator-driven search、persistent workspace 与 simulator-as-contract；保留为 cross-domain evidence。 Exact-v1 supports: Timeloop/Accelergy、MAESTRO 与 ChampSim 三类 DSE 上，在严格调用预算内达到相当或更优设计，最高减少两个数量级 simulator evaluation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: simulator artifact 会被 agent 当真；LLM prior、调用成本与三类受测空间不能外推到真实芯片 sign-off。 | analysis-decision:SF-2026-ARXIV-2606-21836 |
| SF-2026-ARXIV-2606-21842 | score_7_9; potential_books_delta | selected | DA-20260621-NONPREFIX-KV-ISOLATION | — | 当前 Ch72 已把跨租户 cache hit timing、principal-specific namespace、non-prefix causal provenance 与 full-recompute fallback 写成同一 security contract；Step-Wave/QCP/CTBF 是该 owner 的受限实例。 Exact-v1 supports: vLLM+LMCache 上覆盖三种 threat scenario，并报告 bounded-entropy 场景最高 100% extraction、最少 63 requests/token；防线把 ΔTTFT 压近 0。 Its cross-layer control boundary is material because 威胁模型要求共置 tenant、共享 cache、可重复 TTFT probe 与受限语义搜索空间；局部测试不证明任意 engine/GPU 或公网噪声下可复现。 | analysis:DA-20260621-NONPREFIX-KV-ISOLATION |
| SF-2026-ARXIV-2606-21843 | score_7_9; potential_books_delta | not_selected | — | — | 该 family 的长期价值是反例：pre-failure sensor 必须把 context generator 纳入 run identity，不能把 padding artifact 写成 agent drift。 Exact-v1 supports: 单一持久 agent 的 cross-sectional probe battery 测得 conditioning structure；原 context-pressure drift 在多样 padding 下至 150K token 不再出现。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-MONITORING and its non-proof boundary is: 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 | analysis-decision:SF-2026-ARXIV-2606-21843 |
| SF-2026-ARXIV-2606-21848 | score_7_9; potential_books_delta | not_selected | — | — | Ch14 需新增 routing 与 retrieval representation 可合并但带秩条件的 alternative branch；Ch45 只消费 50% cache consequence。 Exact-v1 supports: GPT-2 280M/557M、Pythia 410M、Qwen2 1.5B、Llama 3.2 1B 五组模型中，4/5 perplexity 与 4/5 downstream benchmark 不低于 QKV，同时 cache 容量减半。 It is not promoted over the three winners because its durable effect remains owned by MODEL-SELF-ATTENTION and its non-proof boundary is: 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。 | analysis-decision:SF-2026-ARXIV-2606-21848 |
| SF-2026-ARXIV-2606-21854 | potential_books_delta | not_selected | — | — | Ch36 已拥有 data pipeline、sharding 与 compute utilization 的 owner；ESPnet3 是 speech-specific framework instance。 Exact-v1 supports: OWSM multi-node pretraining 相比 ESPnet2 每 epoch 减少 21.1 分钟、GPU utilization 超过 80%；新增 fine-tune model/data 约 46 行代码。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DISTRIBUTED-TRAINING and its non-proof boundary is: 只覆盖 speech/audio recipes 与作者 OWSM workload；开发行数和平均利用率不证明跨框架可维护性或端到端收敛等价。 | analysis-decision:SF-2026-ARXIV-2606-21854 |
| SF-2026-ARXIV-2606-21856 | score_7_9; potential_books_delta | not_selected | — | — | 当前 Ch84 已以 AgentRun principal/tenant 绑定 workspace、credential、memory、tool 与 evidence，Ch81 也把 deterministic hooks 设为 sandbox/tool/checkpoint/retry/verifier owner；Harness-MU 不再改变长期 owner。 Exact-v1 supports: exact-v1 在多用户 delegation、共享资源与 tool-use scenarios 中比较无治理 agent 与 governed harness 的 task effectiveness 和 policy compliance。 It is not promoted over the three winners because its durable effect remains owned by AGENT-PLATFORM and its non-proof boundary is: harness policy 依赖声明完整性与 hook 覆盖；被绕过的外部 side effect、stale identity mapping 和恶意 plugin 仍需 host reference monitor。 | analysis-decision:SF-2026-ARXIV-2606-21856 |
| SF-2026-ARXIV-2606-21868 | score_7_9; potential_books_delta | not_selected | — | — | Ch56 需把 expert weights 与 KV 视为竞争同一容量预算的联合 working set，而不是两个独立 cache。 Exact-v1 supports: 极低资源硬件上比较 expert/KV baselines，报告 token latency、throughput、命中/迁移与质量。 It is not promoted over the three winners because its durable effect remains owned by INFER-SCHEDULING and its non-proof boundary is: Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。 | analysis-decision:SF-2026-ARXIV-2606-21868 |
| SF-2026-ARXIV-2606-21869 | score_7_9; potential_books_delta | not_selected | — | — | Ch66 需把语言切片的 energy/quality 联合 contract 加入 evaluation identity；Ch70 只消费成本结果。 Exact-v1 supports: Belebele 122 languages、translated GSM8K 与 LM-Arena prompts 上跨模型测量能耗/质量，并在 L40S 与 RTX 6000 Pro Blackwell 做硬件对照。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。 | analysis-decision:SF-2026-ARXIV-2606-21869 |
| SF-2026-ARXIV-2606-21875 | potential_books_delta | not_selected | — | — | Ch66 已区分 confidence、evidence 与 policy-bound triage；本 family 的反向结果强化 calibration boundary。 Exact-v1 supports: 医疗、Covertype、金融与十个外部数据集显示 conflict 有时增加 error ranking，也在 Bank Marketing/Credit Default 上方向反转。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: SEF 不是 causal explanation；attribution/reference choice 改变数值，相关 feature replacement 可能失真，B=40 stability refit 成本约单次 30.1–39.2 倍。 | analysis-decision:SF-2026-ARXIV-2606-21875 |
| SF-2026-ARXIV-2606-21877 | score_7_9; potential_books_delta | not_selected | — | — | Ch72 需增加 authority-envelope BOM：依赖 provenance 不能替代 agent 能访问、记忆、修改和委托什么。 Exact-v1 supports: 13 个开源 agents、52 个 risk scenarios、33 个 deployment mutations；schema 覆盖 14/16 capability dimension，diff detector 对注入变更类型全命中。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。 | analysis-decision:SF-2026-ARXIV-2606-21877 |
| SF-2026-ARXIV-2606-21884 | score_7_9; potential_books_delta | not_selected | — | — | Ch33 需明确 verifiable outcome 不保证 search trace 可蒸馏；训练前先做 forward-derivability test。 Exact-v1 supports: 九类任务、11 个 CoT 设计、RLVR/STaR 与四类 backbone；cryptarithm solver 71% 而蒸馏仅 1–7%，揭示 key 后同例升至 57.1%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。 | analysis-decision:SF-2026-ARXIV-2606-21884 |
| SF-2026-ARXIV-2606-21891 | score_7_9; potential_books_delta | not_selected | — | — | Ch81 需把 low score 拆成 hypothesis failure 与 execution failure，防止 workflow 错误地删除可修复分支。 Exact-v1 supports: 22 个 MLGym/MLEBench tasks、每法三次、8 小时 budget；报告 IQM、optimality gap、trajectory 与组件 ablation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。 | analysis-decision:SF-2026-ARXIV-2606-21891 |
| SF-2026-ARXIV-2606-21917 | potential_books_delta | not_selected | — | — | Ch67 已把 activation/attention monitor 定义为 model-version-bound sensor；该 family 不改变 authority。 Exact-v1 supports: exact-v1 跨 LLM 与 QA/hallucination datasets 比较 pre-generation detector 的 discrimination、calibration 与 routing utility。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-MONITORING and its non-proof boundary is: probe 与 label/judge 共偏，attention correlation 不证明因果；生成前预测不能覆盖 retrieval corruption 或生成中途状态变化。 | analysis-decision:SF-2026-ARXIV-2606-21917 |
| SF-2026-ARXIV-2606-21954 | score_7_9; potential_books_delta | not_selected | — | — | Ch66 需把 transfer capability 与 source-language base ability 解耦，避免版本比较的 denominator inflation。 Exact-v1 supports: 20 个语言模型、三套 multilingual benchmark；小模型 transfer 并未失效，随规模的进步慢于 raw accuracy 暗示。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。 | analysis-decision:SF-2026-ARXIV-2606-21954 |
| SF-2026-ARXIV-2606-21959 | potential_books_delta | not_selected | — | — | 当前 Ch66 已明确引用不仅要存在还要支持 claim，并已把 deep-research citation support、coverage 与 synthesis 分层；OpenBioRQ 提供 biomedical stress case，但不改变 evaluation owner。 Exact-v1 supports: 受测 agents 在高难问题上 tool-use collapse；15.9% citation 指向错误论文，且 citation 可解析不等于支持 claim。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: biomedical question set、冻结时点与 judge checklist 不证明未来问题仍未解决；benchmark 不能替代领域专家证据审查。 | analysis-decision:SF-2026-ARXIV-2606-21959 |
| SF-2026-ARXIV-2606-21963 | potential_books_delta | not_selected | — | — | Ch73/81 已要求 incident diagnosis 与 executable effect receipt 分离；Holmes 是工业案例。 Exact-v1 supports: 工业移动端 crash workload 上比较 diagnosis accuracy、time-to-resolution 与 artifact/tool ablation。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-PRODUCTION and its non-proof boundary is: 单组织 crash taxonomy、内部工具与数据分布限制复现；诊断建议不等于已合并修复或无回归。 | analysis-decision:SF-2026-ARXIV-2606-21963 |
| SF-2026-ARXIV-2606-21968 | score_7_9; potential_books_delta | not_selected | — | — | Ch81 需把感知分辨率选择建模为有成本、可回退的 route，而不是固定预处理。 Exact-v1 supports: 多种 visual RAG benchmark/model 上比较质量、视觉 token 与 routing ablation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。 | analysis-decision:SF-2026-ARXIV-2606-21968 |
| SF-2026-ARXIV-2606-21994 | potential_books_delta | not_selected | — | — | Ch33 已将 OPD 定义为探索催化剂并保留 teacher ceiling；prefix allocation 是同 owner 内实现分支。 Exact-v1 supports: reasoning tasks 上相对 OPD/on-policy distillation 比较 sample efficiency、accuracy 与 prefix allocation。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 早期 overlap 可能错杀迟发正确路径并放大 teacher/student 共偏；它重分配探索预算，不扩展 teacher capability ceiling。 | analysis-decision:SF-2026-ARXIV-2606-21994 |
| SF-2026-ARXIV-2606-22000 | score_7_9; potential_books_delta | not_selected | — | — | 当前 Ch66 已有专节把 Pass@k 能力覆盖、Pass^k conjunction reliability 与 paired transition 分离，且 action authority 已是独立 evaluation plane；CFAgentBench 不再形成新 delta。 Exact-v1 supports: 多模型 agents 在 pass@1 与 pass@5 上测量 task completion、side effect、approval compliance，并显示重试可靠性塌陷。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: synthetic finance workflow 与规则覆盖有限；state-diff checker 不证明真实法规、身份或银行 effect，pass@k 也不能隐藏每次 unauthorized action。 | analysis-decision:SF-2026-ARXIV-2606-22000 |
| SF-2026-ARXIV-2606-22013 | score_7_9; potential_books_delta | not_selected | — | — | Ch73 需把 load test 从固定 QPS 清单升级为可复算 SLO-boundary search contract。 Exact-v1 supports: 工业 model-serving systems 上比较 capacity-search cost、SLO boundary accuracy 与固定-grid baseline。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-PRODUCTION and its non-proof boundary is: 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。 | analysis-decision:SF-2026-ARXIV-2606-22013 |
| SF-2026-ARXIV-2606-22019 | score_7_9; potential_books_delta | not_selected | — | — | Ch72 需明确 audit coverage 与 outcome 分离：未覆盖 channel 只能是 Unknown。 Exact-v1 supports: 受控 channel-location 实验比较 audit signal、downstream learning 与干预，展示相同 payload 在不同 channel 的可审计性变化。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。 | analysis-decision:SF-2026-ARXIV-2606-22019 |
| SF-2026-ARXIV-2606-22030 | score_7_9; potential_books_delta | selected | DA-20260621-BELIEF-MEMORY-AUTHORITY | — | 当前 Ch77 已要求 source calibration、valid-time、独立 corroboration、contradiction、supersession 与 risk-aware selective action共同约束事实 Memory；Bayesian 聚合是既有可靠性读路径的受限实现。 Exact-v1 supports: 多任务 memory benchmark 中，plain Bayesian update 无稳定收益；reliability-conditioned update 提升 strict F1，并在 poisoning 下比较 provenance cap。 Its cross-layer control boundary is material because A-MEM/BeliefMem 数字未由作者重跑且二手表格类别映射曾冲突；GPT-4o-mini 同时做 extraction、answer 与 judge，strict F1 和 judge 可能共偏。 | analysis:DA-20260621-BELIEF-MEMORY-AUTHORITY |
| SF-2026-ARXIV-2606-22043 | score_7_9; potential_books_delta | not_selected | — | — | Ch33 需把 visual reliance 作为训练 trajectory state，而不只在最终 accuracy 后诊断 shortcut。 Exact-v1 supports: Qwen3-VL-8B-Instruct 的多 seed、lambda∈{0,1,2} 与 intervention-timing 轨迹上测 VHS、accuracy 与 onset/reversal；representation probe 落在 bootstrap variability 内，只是探索性观察。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。 | analysis-decision:SF-2026-ARXIV-2606-22043 |
| SF-2026-ARXIV-2606-22082 | potential_books_delta | not_selected | — | — | Ch82 已明确 shared repository 需要 commitment protocol、ownership/interface 和可验证提交顺序。 Exact-v1 supports: repository-level generation tasks 上比较单 agent、多 agent、组件 ablation 与测试结果。 It is not promoted over the three winners because its durable effect remains owned by AGENT-MULTI-AGENT and its non-proof boundary is: 所有 agents 共享 Qwen2.5-72B-Instruct，CTO contract 可能共享 backbone bias；test suite 不完备时 machine-checkable 只证明 harness 内一致。 | analysis-decision:SF-2026-ARXIV-2606-22082 |
| SF-2026-ARXIV-2606-22085 | potential_books_delta | not_selected | — | — | Ch72 已将 CoT monitor 定义为 policy-bound sensor，不是 security authority；该负结果强化边界。 Exact-v1 supports: 多 reasoning models 与 tampering types 上测 detection/acknowledgement，结果显示自我检测弱且不稳定。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 可见 CoT 不是完整内部 computation；专有 frontier API 不支持 CoT prefilling 因而未测，否认/承认都不是 tamper truth。 | analysis-decision:SF-2026-ARXIV-2606-22085 |
| SF-2026-ARXIV-2606-22136 | potential_books_delta | not_selected | — | — | 当前 Ch27 已完整写入 human hand pose→action-conditioned video→pose/depth reconstruction/retargeting→derived robot trajectory provenance→real closed-loop admission；Wh0 正是该现有分支的 source-specific evidence。 Exact-v1 supports: 50K WM-H episodes、18 个真实 dexterous tasks；相对仅 robot data，未见任务 zero-shot success 从 8.3% 升至 38.9%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 生成世界模型会携带 physics/contact error，视觉编辑不等于 action 可执行；真实 robot data 仍是 deployment anchor，18 tasks 不证明广泛迁移。 | analysis-decision:SF-2026-ARXIV-2606-22136 |
| SF-2026-ARXIV-2606-22142 | score_7_9; potential_books_delta | selected | DA-20260621-TYPED-ROBOT-LINEAGE | — | Ch27 需把 sample lineage 扩展为 rollout→review→dataset→training→evaluation→release 的 typed lifecycle graph。 Exact-v1 supports: 真实机器人 policy-iteration workflow 中比较常规流程与 lineage layer 的迭代时间、审计性和 downstream policy performance。 Its cross-layer control boundary is material because robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。 | analysis:DA-20260621-TYPED-ROBOT-LINEAGE |
| SF-2026-ARXIV-2606-22164 | score_7_9; potential_books_delta | not_selected | — | — | Ch33 需把 decision density 纳入 credit-assignment route：长轨迹本身不是选择 critic 的充分条件。 Exact-v1 supports: 可精确调 ρ 的 controlled environment 复现 turn-level/trajectory-level SNR 比例，R²=0.999，并测 training-step gap。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。 | analysis-decision:SF-2026-ARXIV-2606-22164 |
| SF-2026-ARXIV-2606-22175 | score_7_9; potential_books_delta | not_selected | — | — | Ch81 需把 workflow task identity 分成 state-holder 与 invocation；复用必须绑定 model/runtime version 和 tenant。 Exact-v1 supports: 145,449-claim PromptVerify workflow 在 20 GPU stable testbed 获 3.6×，并扩到 186 个闲置 GPU 后 784 秒完成。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。 | analysis-decision:SF-2026-ARXIV-2606-22175 |
| SF-2026-ARXIV-2606-22179 | score_7_9; potential_books_delta | not_selected | — | — | Ch66 需增加 threshold-resolution contract：ranking 好不代表 operator 有足够可选 operating points。 Exact-v1 supports: 9 个 LLM、3 个 benchmark、25 个 model-dataset pair，对七种 confidence construction 比较 ranking、阈值粒度与 inference cost。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。 | analysis-decision:SF-2026-ARXIV-2606-22179 |
| SF-2026-ARXIV-2606-22180 | score_7_9; potential_books_delta | not_selected | — | — | Ch36 需增加 sampling→quality feedback loop 与 communication freshness 的联合 contract，而非仅 pipeline overlap。 Exact-v1 supports: 六个系统 baseline 与大图数据上平均 27.9× speedup、通信降超 53.1%、CPU-GPU utilization 超 80%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DISTRIBUTED-TRAINING and its non-proof boundary is: quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 | analysis-decision:SF-2026-ARXIV-2606-22180 |
| SF-2026-ARXIV-2606-22189 | potential_books_delta | not_selected | — | — | Ch27 已拥有 data gates、dedup、contamination 与 provenance；保留此单 GPU negative RLVR case，不新增 owner。 Exact-v1 supports: 约 13B token、自跑六任务 harness；均分 0.4150；直接 GRPO-style RLVR 使 GSM8K exact match 从 1.82% 降至 1.59%/1.21%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 单 run、自有 harness、小模型与 nominal-token ratio 不证明 scaling law 或统计等价；RLVR 下降只是具体 failure case。 | analysis-decision:SF-2026-ARXIV-2606-22189 |
| SF-2026-ARXIV-2606-22203 | score_7_9; potential_books_delta | not_selected | — | — | Ch82 需禁止用 pairwise interaction 参数外推 group dynamics，并把 model-prior drift 从 emergent consensus 分离。 Exact-v1 supports: 5 个 frontier model 测 pairwise gamma，16 个 closed/open model 测 group coupling；复核既有 emergent-consensus 结果并发现 settled facts 上是 prior artifact。 It is not promoted over the three winners because its durable effect remains owned by AGENT-MULTI-AGENT and its non-proof boundary is: pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 | analysis-decision:SF-2026-ARXIV-2606-22203 |
| SF-2026-ARXIV-2606-22248 | potential_books_delta | not_selected | — | — | Ch27 已把 curriculum state 与 retention Gate 分离；本 family 仅是架构受限案例。 Exact-v1 supports: 356M 参数、受控 Python curriculum；Stage 5 100%、相邻 Stage 3 保留 98.8%，但早期 Stage 2E 仅 12%；matched Transformer Stage 3 仅 6%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 单一受控 curriculum、单 architecture size 且 long-horizon retention 仍弱；不能外推为解决 catastrophic forgetting。 | analysis-decision:SF-2026-ARXIV-2606-22248 |
| SF-2026-ARXIV-2606-22263 | score_7_9; potential_books_delta | not_selected | — | — | Ch72 需把 vulnerability report 的 commit authority 绑定 executable PoV+sanitizer，而非 agent verdict。 Exact-v1 supports: 7 个持续 fuzz 5–8 年的生产项目与 100 个随机 Arvo/CyberGym 项目；约每项目 1 小时、总成本 300 美元，发现 19 个未知 memory-safety 漏洞。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。 | analysis-decision:SF-2026-ARXIV-2606-22263 |
| SF-2026-ARXIV-2606-22283 | score_7_9; potential_books_delta | not_selected | — | — | Ch54 需把硬件逆向知识按 measured/decompile-derived/predicted 分层，并保持 Core ML 是唯一 supported production path。 Exact-v1 supports: A11–A18、M1–M5 目标表；直接测量只在 M1/M5，结合静态分析给出 operation-device matrix 与性能/能耗边界。 It is not promoted over the three winners because its durable effect remains owned by INFER-GPU-MEMORY and its non-proof boundary is: private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。 | analysis-decision:SF-2026-ARXIV-2606-22283 |

<!-- analysis-decision:SF-2026-ARXIV-2606-21822:start -->
Ch72 已要求 coding-agent 安全真值来自 executable evidence；本 family 增加 CN 具体实例但不改变 owner。 Exact-v1 supports: 31 个可标注函数与 3 个故意不安全函数上，o3 首轮 90%、总计 97%，GPT-4o 首轮 65%。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 测试通过只覆盖生成状态，不是全路径证明；safe-but-unexpressible、搜索失败与真实 unsafe 仍可能落入同一失败出口。
<!-- analysis-decision:SF-2026-ARXIV-2606-21822:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21836:start -->
Ch81 已拥有 evaluator-driven search、persistent workspace 与 simulator-as-contract；保留为 cross-domain evidence。 Exact-v1 supports: Timeloop/Accelergy、MAESTRO 与 ChampSim 三类 DSE 上，在严格调用预算内达到相当或更优设计，最高减少两个数量级 simulator evaluation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: simulator artifact 会被 agent 当真；LLM prior、调用成本与三类受测空间不能外推到真实芯片 sign-off。
<!-- analysis-decision:SF-2026-ARXIV-2606-21836:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21843:start -->
该 family 的长期价值是反例：pre-failure sensor 必须把 context generator 纳入 run identity，不能把 padding artifact 写成 agent drift。 Exact-v1 supports: 单一持久 agent 的 cross-sectional probe battery 测得 conditioning structure；原 context-pressure drift 在多样 padding 下至 150K token 不再出现。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-MONITORING and its non-proof boundary is: 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。
<!-- analysis-decision:SF-2026-ARXIV-2606-21843:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21848:start -->
Ch14 需新增 routing 与 retrieval representation 可合并但带秩条件的 alternative branch；Ch45 只消费 50% cache consequence。 Exact-v1 supports: GPT-2 280M/557M、Pythia 410M、Qwen2 1.5B、Llama 3.2 1B 五组模型中，4/5 perplexity 与 4/5 downstream benchmark 不低于 QKV，同时 cache 容量减半。 It is not promoted over the three winners because its durable effect remains owned by MODEL-SELF-ATTENTION and its non-proof boundary is: 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。
<!-- analysis-decision:SF-2026-ARXIV-2606-21848:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21854:start -->
Ch36 已拥有 data pipeline、sharding 与 compute utilization 的 owner；ESPnet3 是 speech-specific framework instance。 Exact-v1 supports: OWSM multi-node pretraining 相比 ESPnet2 每 epoch 减少 21.1 分钟、GPU utilization 超过 80%；新增 fine-tune model/data 约 46 行代码。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DISTRIBUTED-TRAINING and its non-proof boundary is: 只覆盖 speech/audio recipes 与作者 OWSM workload；开发行数和平均利用率不证明跨框架可维护性或端到端收敛等价。
<!-- analysis-decision:SF-2026-ARXIV-2606-21854:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21856:start -->
当前 Ch84 已以 AgentRun principal/tenant 绑定 workspace、credential、memory、tool 与 evidence，Ch81 也把 deterministic hooks 设为 sandbox/tool/checkpoint/retry/verifier owner；Harness-MU 不再改变长期 owner。 Exact-v1 supports: exact-v1 在多用户 delegation、共享资源与 tool-use scenarios 中比较无治理 agent 与 governed harness 的 task effectiveness 和 policy compliance。 It is not promoted over the three winners because its durable effect remains owned by AGENT-PLATFORM and its non-proof boundary is: harness policy 依赖声明完整性与 hook 覆盖；被绕过的外部 side effect、stale identity mapping 和恶意 plugin 仍需 host reference monitor。
<!-- analysis-decision:SF-2026-ARXIV-2606-21856:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21868:start -->
Ch56 需把 expert weights 与 KV 视为竞争同一容量预算的联合 working set，而不是两个独立 cache。 Exact-v1 supports: 极低资源硬件上比较 expert/KV baselines，报告 token latency、throughput、命中/迁移与质量。 It is not promoted over the three winners because its durable effect remains owned by INFER-SCHEDULING and its non-proof boundary is: Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。
<!-- analysis-decision:SF-2026-ARXIV-2606-21868:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21869:start -->
Ch66 需把语言切片的 energy/quality 联合 contract 加入 evaluation identity；Ch70 只消费成本结果。 Exact-v1 supports: Belebele 122 languages、translated GSM8K 与 LM-Arena prompts 上跨模型测量能耗/质量，并在 L40S 与 RTX 6000 Pro Blackwell 做硬件对照。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。
<!-- analysis-decision:SF-2026-ARXIV-2606-21869:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21875:start -->
Ch66 已区分 confidence、evidence 与 policy-bound triage；本 family 的反向结果强化 calibration boundary。 Exact-v1 supports: 医疗、Covertype、金融与十个外部数据集显示 conflict 有时增加 error ranking，也在 Bank Marketing/Credit Default 上方向反转。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: SEF 不是 causal explanation；attribution/reference choice 改变数值，相关 feature replacement 可能失真，B=40 stability refit 成本约单次 30.1–39.2 倍。
<!-- analysis-decision:SF-2026-ARXIV-2606-21875:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21877:start -->
Ch72 需增加 authority-envelope BOM：依赖 provenance 不能替代 agent 能访问、记忆、修改和委托什么。 Exact-v1 supports: 13 个开源 agents、52 个 risk scenarios、33 个 deployment mutations；schema 覆盖 14/16 capability dimension，diff detector 对注入变更类型全命中。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。
<!-- analysis-decision:SF-2026-ARXIV-2606-21877:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21884:start -->
Ch33 需明确 verifiable outcome 不保证 search trace 可蒸馏；训练前先做 forward-derivability test。 Exact-v1 supports: 九类任务、11 个 CoT 设计、RLVR/STaR 与四类 backbone；cryptarithm solver 71% 而蒸馏仅 1–7%，揭示 key 后同例升至 57.1%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。
<!-- analysis-decision:SF-2026-ARXIV-2606-21884:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21891:start -->
Ch81 需把 low score 拆成 hypothesis failure 与 execution failure，防止 workflow 错误地删除可修复分支。 Exact-v1 supports: 22 个 MLGym/MLEBench tasks、每法三次、8 小时 budget；报告 IQM、optimality gap、trajectory 与组件 ablation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。
<!-- analysis-decision:SF-2026-ARXIV-2606-21891:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21917:start -->
Ch67 已把 activation/attention monitor 定义为 model-version-bound sensor；该 family 不改变 authority。 Exact-v1 supports: exact-v1 跨 LLM 与 QA/hallucination datasets 比较 pre-generation detector 的 discrimination、calibration 与 routing utility。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-MONITORING and its non-proof boundary is: probe 与 label/judge 共偏，attention correlation 不证明因果；生成前预测不能覆盖 retrieval corruption 或生成中途状态变化。
<!-- analysis-decision:SF-2026-ARXIV-2606-21917:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21954:start -->
Ch66 需把 transfer capability 与 source-language base ability 解耦，避免版本比较的 denominator inflation。 Exact-v1 supports: 20 个语言模型、三套 multilingual benchmark；小模型 transfer 并未失效，随规模的进步慢于 raw accuracy 暗示。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。
<!-- analysis-decision:SF-2026-ARXIV-2606-21954:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21959:start -->
当前 Ch66 已明确引用不仅要存在还要支持 claim，并已把 deep-research citation support、coverage 与 synthesis 分层；OpenBioRQ 提供 biomedical stress case，但不改变 evaluation owner。 Exact-v1 supports: 受测 agents 在高难问题上 tool-use collapse；15.9% citation 指向错误论文，且 citation 可解析不等于支持 claim。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: biomedical question set、冻结时点与 judge checklist 不证明未来问题仍未解决；benchmark 不能替代领域专家证据审查。
<!-- analysis-decision:SF-2026-ARXIV-2606-21959:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21963:start -->
Ch73/81 已要求 incident diagnosis 与 executable effect receipt 分离；Holmes 是工业案例。 Exact-v1 supports: 工业移动端 crash workload 上比较 diagnosis accuracy、time-to-resolution 与 artifact/tool ablation。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-PRODUCTION and its non-proof boundary is: 单组织 crash taxonomy、内部工具与数据分布限制复现；诊断建议不等于已合并修复或无回归。
<!-- analysis-decision:SF-2026-ARXIV-2606-21963:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21968:start -->
Ch81 需把感知分辨率选择建模为有成本、可回退的 route，而不是固定预处理。 Exact-v1 supports: 多种 visual RAG benchmark/model 上比较质量、视觉 token 与 routing ablation。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。
<!-- analysis-decision:SF-2026-ARXIV-2606-21968:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-21994:start -->
Ch33 已将 OPD 定义为探索催化剂并保留 teacher ceiling；prefix allocation 是同 owner 内实现分支。 Exact-v1 supports: reasoning tasks 上相对 OPD/on-policy distillation 比较 sample efficiency、accuracy 与 prefix allocation。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 早期 overlap 可能错杀迟发正确路径并放大 teacher/student 共偏；它重分配探索预算，不扩展 teacher capability ceiling。
<!-- analysis-decision:SF-2026-ARXIV-2606-21994:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22000:start -->
当前 Ch66 已有专节把 Pass@k 能力覆盖、Pass^k conjunction reliability 与 paired transition 分离，且 action authority 已是独立 evaluation plane；CFAgentBench 不再形成新 delta。 Exact-v1 supports: 多模型 agents 在 pass@1 与 pass@5 上测量 task completion、side effect、approval compliance，并显示重试可靠性塌陷。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: synthetic finance workflow 与规则覆盖有限；state-diff checker 不证明真实法规、身份或银行 effect，pass@k 也不能隐藏每次 unauthorized action。
<!-- analysis-decision:SF-2026-ARXIV-2606-22000:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22013:start -->
Ch73 需把 load test 从固定 QPS 清单升级为可复算 SLO-boundary search contract。 Exact-v1 supports: 工业 model-serving systems 上比较 capacity-search cost、SLO boundary accuracy 与固定-grid baseline。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-PRODUCTION and its non-proof boundary is: 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。
<!-- analysis-decision:SF-2026-ARXIV-2606-22013:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22019:start -->
Ch72 需明确 audit coverage 与 outcome 分离：未覆盖 channel 只能是 Unknown。 Exact-v1 supports: 受控 channel-location 实验比较 audit signal、downstream learning 与干预，展示相同 payload 在不同 channel 的可审计性变化。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。
<!-- analysis-decision:SF-2026-ARXIV-2606-22019:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22043:start -->
Ch33 需把 visual reliance 作为训练 trajectory state，而不只在最终 accuracy 后诊断 shortcut。 Exact-v1 supports: Qwen3-VL-8B-Instruct 的多 seed、lambda∈{0,1,2} 与 intervention-timing 轨迹上测 VHS、accuracy 与 onset/reversal；representation probe 落在 bootstrap variability 内，只是探索性观察。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。
<!-- analysis-decision:SF-2026-ARXIV-2606-22043:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22082:start -->
Ch82 已明确 shared repository 需要 commitment protocol、ownership/interface 和可验证提交顺序。 Exact-v1 supports: repository-level generation tasks 上比较单 agent、多 agent、组件 ablation 与测试结果。 It is not promoted over the three winners because its durable effect remains owned by AGENT-MULTI-AGENT and its non-proof boundary is: 所有 agents 共享 Qwen2.5-72B-Instruct，CTO contract 可能共享 backbone bias；test suite 不完备时 machine-checkable 只证明 harness 内一致。
<!-- analysis-decision:SF-2026-ARXIV-2606-22082:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22085:start -->
Ch72 已将 CoT monitor 定义为 policy-bound sensor，不是 security authority；该负结果强化边界。 Exact-v1 supports: 多 reasoning models 与 tampering types 上测 detection/acknowledgement，结果显示自我检测弱且不稳定。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: 可见 CoT 不是完整内部 computation；专有 frontier API 不支持 CoT prefilling 因而未测，否认/承认都不是 tamper truth。
<!-- analysis-decision:SF-2026-ARXIV-2606-22085:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22136:start -->
当前 Ch27 已完整写入 human hand pose→action-conditioned video→pose/depth reconstruction/retargeting→derived robot trajectory provenance→real closed-loop admission；Wh0 正是该现有分支的 source-specific evidence。 Exact-v1 supports: 50K WM-H episodes、18 个真实 dexterous tasks；相对仅 robot data，未见任务 zero-shot success 从 8.3% 升至 38.9%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 生成世界模型会携带 physics/contact error，视觉编辑不等于 action 可执行；真实 robot data 仍是 deployment anchor，18 tasks 不证明广泛迁移。
<!-- analysis-decision:SF-2026-ARXIV-2606-22136:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22164:start -->
Ch33 需把 decision density 纳入 credit-assignment route：长轨迹本身不是选择 critic 的充分条件。 Exact-v1 supports: 可精确调 ρ 的 controlled environment 复现 turn-level/trajectory-level SNR 比例，R²=0.999，并测 training-step gap。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-GRPO and its non-proof boundary is: 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。
<!-- analysis-decision:SF-2026-ARXIV-2606-22164:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22175:start -->
Ch81 需把 workflow task identity 分成 state-holder 与 invocation；复用必须绑定 model/runtime version 和 tenant。 Exact-v1 supports: 145,449-claim PromptVerify workflow 在 20 GPU stable testbed 获 3.6×，并扩到 186 个闲置 GPU 后 784 秒完成。 It is not promoted over the three winners because its durable effect remains owned by AGENT-WORKFLOW and its non-proof boundary is: persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。
<!-- analysis-decision:SF-2026-ARXIV-2606-22175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22179:start -->
Ch66 需增加 threshold-resolution contract：ranking 好不代表 operator 有足够可选 operating points。 Exact-v1 supports: 9 个 LLM、3 个 benchmark、25 个 model-dataset pair，对七种 confidence construction 比较 ranking、阈值粒度与 inference cost。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-EVALUATION-SYSTEM and its non-proof boundary is: 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。
<!-- analysis-decision:SF-2026-ARXIV-2606-22179:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22180:start -->
Ch36 需增加 sampling→quality feedback loop 与 communication freshness 的联合 contract，而非仅 pipeline overlap。 Exact-v1 supports: 六个系统 baseline 与大图数据上平均 27.9× speedup、通信降超 53.1%、CPU-GPU utilization 超 80%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DISTRIBUTED-TRAINING and its non-proof boundary is: quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。
<!-- analysis-decision:SF-2026-ARXIV-2606-22180:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22189:start -->
Ch27 已拥有 data gates、dedup、contamination 与 provenance；保留此单 GPU negative RLVR case，不新增 owner。 Exact-v1 supports: 约 13B token、自跑六任务 harness；均分 0.4150；直接 GRPO-style RLVR 使 GSM8K exact match 从 1.82% 降至 1.59%/1.21%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 单 run、自有 harness、小模型与 nominal-token ratio 不证明 scaling law 或统计等价；RLVR 下降只是具体 failure case。
<!-- analysis-decision:SF-2026-ARXIV-2606-22189:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22203:start -->
Ch82 需禁止用 pairwise interaction 参数外推 group dynamics，并把 model-prior drift 从 emergent consensus 分离。 Exact-v1 supports: 5 个 frontier model 测 pairwise gamma，16 个 closed/open model 测 group coupling；复核既有 emergent-consensus 结果并发现 settled facts 上是 prior artifact。 It is not promoted over the three winners because its durable effect remains owned by AGENT-MULTI-AGENT and its non-proof boundary is: pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。
<!-- analysis-decision:SF-2026-ARXIV-2606-22203:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22248:start -->
Ch27 已把 curriculum state 与 retention Gate 分离；本 family 仅是架构受限案例。 Exact-v1 supports: 356M 参数、受控 Python curriculum；Stage 5 100%、相邻 Stage 3 保留 98.8%，但早期 Stage 2E 仅 12%；matched Transformer Stage 3 仅 6%。 It is not promoted over the three winners because its durable effect remains owned by TRAIN-DATA and its non-proof boundary is: 单一受控 curriculum、单 architecture size 且 long-horizon retention 仍弱；不能外推为解决 catastrophic forgetting。
<!-- analysis-decision:SF-2026-ARXIV-2606-22248:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22263:start -->
Ch72 需把 vulnerability report 的 commit authority 绑定 executable PoV+sanitizer，而非 agent verdict。 Exact-v1 supports: 7 个持续 fuzz 5–8 年的生产项目与 100 个随机 Arvo/CyberGym 项目；约每项目 1 小时、总成本 300 美元，发现 19 个未知 memory-safety 漏洞。 It is not promoted over the three winners because its durable effect remains owned by PLATFORM-SECURITY and its non-proof boundary is: sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。
<!-- analysis-decision:SF-2026-ARXIV-2606-22263:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-22283:start -->
Ch54 需把硬件逆向知识按 measured/decompile-derived/predicted 分层，并保持 Core ML 是唯一 supported production path。 Exact-v1 supports: A11–A18、M1–M5 目标表；直接测量只在 M1/M5，结合静态分析给出 operation-device matrix 与性能/能耗边界。 It is not promoted over the three winners because its durable effect remains owned by INFER-GPU-MEMORY and its non-proof boundary is: private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。
<!-- analysis-decision:SF-2026-ARXIV-2606-22283:end -->

<!-- analysis:DA-20260621-NONPREFIX-KV-ISOLATION:start -->
### DA-20260621-NONPREFIX-KV-ISOLATION

当 RAG serving 从 prefix cache 演进到任意 chunk fusion，旧 threat model 会失效：性能路径中的 tail recomputation 变成可测 oracle。新的长期结论不是关闭 cache reuse，而是把 QCP/constant-time fusion 与 tenant identity 绑定，并以 throughput 与 leakage 双 Gate 验证。
<!-- analysis:DA-20260621-NONPREFIX-KV-ISOLATION:end -->

<!-- analysis:DA-20260621-BELIEF-MEMORY-AUTHORITY:start -->
### DA-20260621-BELIEF-MEMORY-AUTHORITY

belief memory 不能因采用 Bayesian 形式就取得真值权威。只有 source reliability 可估、重复 provenance 被限流且 strict metric 与 judge 结果分开时，posterior 才能作为受限状态；否则保留旧的 evidence archive 与人工复核。
<!-- analysis:DA-20260621-BELIEF-MEMORY-AUTHORITY:end -->

<!-- analysis:DA-20260621-TYPED-ROBOT-LINEAGE:start -->
### DA-20260621-TYPED-ROBOT-LINEAGE

机器人 policy 的长期 owner 不是 checkpoint，而是 rollout、review、dataset、training、evaluation 与 release 的 typed lineage。任何一步缺 receipt 时，deployment recommendation 只能保持 pending，并回退到上一已批准 policy。
<!-- analysis:DA-20260621-TYPED-ROBOT-LINEAGE:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-21822 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-21822 | delta:SF-2026-ARXIV-2606-21822 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21822 |
| SF-2026-ARXIV-2606-21836 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L45 — ## Feedback 来源决定价值 | existing:SF-2026-ARXIV-2606-21836 | delta:SF-2026-ARXIV-2606-21836 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21836 |
| SF-2026-ARXIV-2606-21842 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-21842 | delta:SF-2026-ARXIV-2606-21842 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21842 |
| SF-2026-ARXIV-2606-21843 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | books/part-06-ai-infrastructure/66-evaluation-system.md#L33 — ## 为什么“选一个分数”不是评估系统 | existing:SF-2026-ARXIV-2606-21843 | delta:SF-2026-ARXIV-2606-21843 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21843 |
| SF-2026-ARXIV-2606-21848 | MODEL-SELF-ATTENTION | books/part-02-model/14-self-attention.md#L64 — ## 从匹配分数到读取权重 | books/part-02-model/15-multi-head-attention.md#L31 — ## 从单头投影到多个 head | existing:SF-2026-ARXIV-2606-21848 | delta:SF-2026-ARXIV-2606-21848 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21848 |
| SF-2026-ARXIV-2606-21854 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L629 — ### 从 Phase 串行到依赖驱动的跨 Phase 重排 | books/part-04-training-system/37-tensor-parallel.md#L18 — ## 为什么“把权重文件切开”不够 | existing:SF-2026-ARXIV-2606-21854 | delta:SF-2026-ARXIV-2606-21854 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21854 |
| SF-2026-ARXIV-2606-21856 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L382 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L29 — ## Host、Client、Server | existing:SF-2026-ARXIV-2606-21856 | delta:SF-2026-ARXIV-2606-21856 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21856 |
| SF-2026-ARXIV-2606-21868 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L209 — ### MoE Decode：从 Queue Length 到 Expert Working Set | books/part-05-inference-system/55-pd-disaggregation.md#L24 — ## 分离之后发生什么 | existing:SF-2026-ARXIV-2606-21868 | delta:SF-2026-ARXIV-2606-21868 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21868 |
| SF-2026-ARXIV-2606-21869 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-21869 | delta:SF-2026-ARXIV-2606-21869 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21869 |
| SF-2026-ARXIV-2606-21875 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-21875 | delta:SF-2026-ARXIV-2606-21875 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21875 |
| SF-2026-ARXIV-2606-21877 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-21877 | delta:SF-2026-ARXIV-2606-21877 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21877 |
| SF-2026-ARXIV-2606-21884 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L18 — ## 把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18 — ## 从 RLHF 的两阶段复杂度开始 | existing:SF-2026-ARXIV-2606-21884 | delta:SF-2026-ARXIV-2606-21884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21884 |
| SF-2026-ARXIV-2606-21891 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L45 — ## Feedback 来源决定价值 | existing:SF-2026-ARXIV-2606-21891 | delta:SF-2026-ARXIV-2606-21891 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21891 |
| SF-2026-ARXIV-2606-21917 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | books/part-06-ai-infrastructure/66-evaluation-system.md#L33 — ## 为什么“选一个分数”不是评估系统 | existing:SF-2026-ARXIV-2606-21917 | delta:SF-2026-ARXIV-2606-21917 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21917 |
| SF-2026-ARXIV-2606-21954 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-21954 | delta:SF-2026-ARXIV-2606-21954 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21954 |
| SF-2026-ARXIV-2606-21959 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-21959 | delta:SF-2026-ARXIV-2606-21959 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21959 |
| SF-2026-ARXIV-2606-21963 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L91 — ## Capacity、Failure 与 Recovery | books/part-06-ai-infrastructure/72-security.md#L29 — ## 生命周期威胁 | existing:SF-2026-ARXIV-2606-21963 | delta:SF-2026-ARXIV-2606-21963 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21963 |
| SF-2026-ARXIV-2606-21968 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L45 — ## Feedback 来源决定价值 | existing:SF-2026-ARXIV-2606-21968 | delta:SF-2026-ARXIV-2606-21968 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-21968 |
| SF-2026-ARXIV-2606-21994 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L18 — ## 把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18 — ## 从 RLHF 的两阶段复杂度开始 | existing:SF-2026-ARXIV-2606-21994 | delta:SF-2026-ARXIV-2606-21994 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-21994 |
| SF-2026-ARXIV-2606-22000 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-22000 | delta:SF-2026-ARXIV-2606-22000 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22000 |
| SF-2026-ARXIV-2606-22013 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L91 — ## Capacity、Failure 与 Recovery | books/part-06-ai-infrastructure/72-security.md#L29 — ## 生命周期威胁 | existing:SF-2026-ARXIV-2606-22013 | delta:SF-2026-ARXIV-2606-22013 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22013 |
| SF-2026-ARXIV-2606-22019 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-22019 | delta:SF-2026-ARXIV-2606-22019 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22019 |
| SF-2026-ARXIV-2606-22030 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L252 — ## Consolidation 与 Forgetting | books/part-07-agent/76-rag.md#L35 — ## Offline Ingestion 不是预处理细节 | existing:SF-2026-ARXIV-2606-22030 | delta:SF-2026-ARXIV-2606-22030 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22030 |
| SF-2026-ARXIV-2606-22043 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L18 — ## 把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18 — ## 从 RLHF 的两阶段复杂度开始 | existing:SF-2026-ARXIV-2606-22043 | delta:SF-2026-ARXIV-2606-22043 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22043 |
| SF-2026-ARXIV-2606-22082 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L240 — ## Message 不是 State | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | existing:SF-2026-ARXIV-2606-22082 | delta:SF-2026-ARXIV-2606-22082 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22082 |
| SF-2026-ARXIV-2606-22085 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-22085 | delta:SF-2026-ARXIV-2606-22085 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22085 |
| SF-2026-ARXIV-2606-22136 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 — ## Data lineage 是训练可复现性的前提 | books/part-04-training-system/28-pretraining.md#L32 — ## Next-token objective | existing:SF-2026-ARXIV-2606-22136 | delta:SF-2026-ARXIV-2606-22136 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22136 |
| SF-2026-ARXIV-2606-22142 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 — ## Data lineage 是训练可复现性的前提 | books/part-04-training-system/28-pretraining.md#L32 — ## Next-token objective | existing:SF-2026-ARXIV-2606-22142 | delta:SF-2026-ARXIV-2606-22142 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22142 |
| SF-2026-ARXIV-2606-22164 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L18 — ## 把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18 — ## 从 RLHF 的两阶段复杂度开始 | existing:SF-2026-ARXIV-2606-22164 | delta:SF-2026-ARXIV-2606-22164 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22164 |
| SF-2026-ARXIV-2606-22175 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L45 — ## Feedback 来源决定价值 | existing:SF-2026-ARXIV-2606-22175 | delta:SF-2026-ARXIV-2606-22175 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22175 |
| SF-2026-ARXIV-2606-22179 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L724 — ## 从答案评分到可执行证据 | books/part-06-ai-infrastructure/67-monitoring.md#L18 — ## 先定义目标，再选择可测信号 | existing:SF-2026-ARXIV-2606-22179 | delta:SF-2026-ARXIV-2606-22179 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22179 |
| SF-2026-ARXIV-2606-22180 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L629 — ### 从 Phase 串行到依赖驱动的跨 Phase 重排 | books/part-04-training-system/37-tensor-parallel.md#L18 — ## 为什么“把权重文件切开”不够 | existing:SF-2026-ARXIV-2606-22180 | delta:SF-2026-ARXIV-2606-22180 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22180 |
| SF-2026-ARXIV-2606-22189 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 — ## Data lineage 是训练可复现性的前提 | books/part-04-training-system/28-pretraining.md#L32 — ## Next-token objective | existing:SF-2026-ARXIV-2606-22189 | delta:SF-2026-ARXIV-2606-22189 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22189 |
| SF-2026-ARXIV-2606-22203 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L240 — ## Message 不是 State | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | existing:SF-2026-ARXIV-2606-22203 | delta:SF-2026-ARXIV-2606-22203 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22203 |
| SF-2026-ARXIV-2606-22248 | TRAIN-DATA | books/part-04-training-system/27-data.md#L484 — ## Data lineage 是训练可复现性的前提 | books/part-04-training-system/28-pretraining.md#L32 — ## Next-token objective | existing:SF-2026-ARXIV-2606-22248 | delta:SF-2026-ARXIV-2606-22248 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-22248 |
| SF-2026-ARXIV-2606-22263 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L718 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L33 — ## 四个隔离平面 | existing:SF-2026-ARXIV-2606-22263 | delta:SF-2026-ARXIV-2606-22263 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22263 |
| SF-2026-ARXIV-2606-22283 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L249 — ### Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页 | books/part-05-inference-system/55-pd-disaggregation.md#L16 — ## 两种阶段，两种节奏 | existing:SF-2026-ARXIV-2606-22283 | delta:SF-2026-ARXIV-2606-22283 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-22283 |

<!-- existing:SF-2026-ARXIV-2606-21822:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；Ch72 已要求 coding-agent 安全真值来自 executable evidence；本 family 增加 CN 具体实例但不改变 owner。
<!-- existing:SF-2026-ARXIV-2606-21822:end -->

<!-- delta:SF-2026-ARXIV-2606-21822:start -->
把 LLM 生成的 C 内存所有权猜测编译成 CN contract，再由 Bennet/Fulminate 对 100 个生成 heap state 执行检查；失败进入最多六轮有界修复。
<!-- delta:SF-2026-ARXIV-2606-21822:end -->

<!-- books-review:SF-2026-ARXIV-2606-21822:start -->
Principle Reuse; No Change — Existing Coverage. 测试通过只覆盖生成状态，不是全路径证明；safe-but-unexpressible、搜索失败与真实 unsafe 仍可能落入同一失败出口。
<!-- books-review:SF-2026-ARXIV-2606-21822:end -->

<!-- existing:SF-2026-ARXIV-2606-21836:start -->
已复读 owner `books/part-07-agent/81-workflow.md` 的机制正文与 Review notes；Ch81 已拥有 evaluator-driven search、persistent workspace 与 simulator-as-contract；保留为 cross-domain evidence。
<!-- existing:SF-2026-ARXIV-2606-21836:end -->

<!-- delta:SF-2026-ARXIV-2606-21836:start -->
把架构 DSE 从只读 scalar reward 的黑盒搜索改成可编辑 workspace：candidate、constraint、simulator harness、history、best 与 budget 都成为持久 artifact，agent 运行 hypothesis-test-refine。
<!-- delta:SF-2026-ARXIV-2606-21836:end -->

<!-- books-review:SF-2026-ARXIV-2606-21836:start -->
Principle Reuse; No Change — Existing Coverage. simulator artifact 会被 agent 当真；LLM prior、调用成本与三类受测空间不能外推到真实芯片 sign-off。
<!-- books-review:SF-2026-ARXIV-2606-21836:end -->

<!-- existing:SF-2026-ARXIV-2606-21842:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；当前 Ch72 已把跨租户 cache hit timing、principal-specific namespace、non-prefix causal provenance 与 full-recompute fallback 写成同一 security contract；Step-Wave/QCP/CTBF 是该 owner 的受限实例。
<!-- existing:SF-2026-ARXIV-2606-21842:end -->

<!-- delta:SF-2026-ARXIV-2606-21842:start -->
non-prefix KV fusion 的固定 chunk routing 与未对齐 tail recomputation 形成 Step-Wave TTFT oracle；SpliceLeak 先恢复隐藏前缀长度，再用 boundary collision 逐 token 提取；QCP+CTBF 消除长度与语义 timing signal。
<!-- delta:SF-2026-ARXIV-2606-21842:end -->

<!-- books-review:SF-2026-ARXIV-2606-21842:start -->
Principle Reuse; No Change — Existing Coverage. 威胁模型要求共置 tenant、共享 cache、可重复 TTFT probe 与受限语义搜索空间；局部测试不证明任意 engine/GPU 或公网噪声下可复现。
<!-- books-review:SF-2026-ARXIV-2606-21842:end -->

<!-- existing:SF-2026-ARXIV-2606-21843:start -->
已复读 owner `books/part-06-ai-infrastructure/67-monitoring.md` 的机制正文与 Review notes；该 family 的长期价值是反例：pre-failure sensor 必须把 context generator 纳入 run identity，不能把 padding artifact 写成 agent drift。
<!-- existing:SF-2026-ARXIV-2606-21843:end -->

<!-- delta:SF-2026-ARXIV-2606-21843:start -->
agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。
<!-- delta:SF-2026-ARXIV-2606-21843:end -->

<!-- books-review:SF-2026-ARXIV-2606-21843:start -->
Direct Evolution; Integrate. 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。
<!-- books-review:SF-2026-ARXIV-2606-21843:end -->

<!-- existing:SF-2026-ARXIV-2606-21848:start -->
已复读 owner `books/part-02-model/14-self-attention.md` 的机制正文与 Review notes；Ch14 需新增 routing 与 retrieval representation 可合并但带秩条件的 alternative branch；Ch45 只消费 50% cache consequence。
<!-- existing:SF-2026-ARXIV-2606-21848:end -->

<!-- delta:SF-2026-ARXIV-2606-21848:start -->
把 query-key 路由改为 query-value 路由，并在 inference 预乘 query factor，只保存 value representation；QVV(3) 保持投影矩阵数同时移除 key cache。
<!-- delta:SF-2026-ARXIV-2606-21848:end -->

<!-- books-review:SF-2026-ARXIV-2606-21848:start -->
Direct Evolution; Integrate. 等价定理依赖 value projection 的秩/子空间条件；小模型从头训练不证明可无损转换既有大模型，50% 是 attention-cache tensor 而非端到端显存。
<!-- books-review:SF-2026-ARXIV-2606-21848:end -->

<!-- existing:SF-2026-ARXIV-2606-21854:start -->
已复读 owner `books/part-04-training-system/36-distributed-training.md` 的机制正文与 Review notes；Ch36 已拥有 data pipeline、sharding 与 compute utilization 的 owner；ESPnet3 是 speech-specific framework instance。
<!-- existing:SF-2026-ARXIV-2606-21854:end -->

<!-- delta:SF-2026-ARXIV-2606-21854:start -->
DataOrganizer 把 dataset composition、split/shard 与 recipe stage 分离，统一 Python workflow 只通过轻量 override 保留实验差异。
<!-- delta:SF-2026-ARXIV-2606-21854:end -->

<!-- books-review:SF-2026-ARXIV-2606-21854:start -->
Principle Reuse; No Change — Existing Coverage. 只覆盖 speech/audio recipes 与作者 OWSM workload；开发行数和平均利用率不证明跨框架可维护性或端到端收敛等价。
<!-- books-review:SF-2026-ARXIV-2606-21854:end -->

<!-- existing:SF-2026-ARXIV-2606-21856:start -->
已复读 owner `books/part-07-agent/84-agent-platform.md` 的机制正文与 Review notes；当前 Ch84 已以 AgentRun principal/tenant 绑定 workspace、credential、memory、tool 与 evidence，Ch81 也把 deterministic hooks 设为 sandbox/tool/checkpoint/retry/verifier owner；Harness-MU 不再改变长期 owner。
<!-- existing:SF-2026-ARXIV-2606-21856:end -->

<!-- delta:SF-2026-ARXIV-2606-21856:start -->
多用户 agent harness 把 user/principal、workspace、credential、memory 与 tool capability 分离；deterministic hook 在执行前后实施 policy，审计记录 control decision 而不只记录自然语言。
<!-- delta:SF-2026-ARXIV-2606-21856:end -->

<!-- books-review:SF-2026-ARXIV-2606-21856:start -->
Principle Reuse; No Change — Existing Coverage. harness policy 依赖声明完整性与 hook 覆盖；被绕过的外部 side effect、stale identity mapping 和恶意 plugin 仍需 host reference monitor。
<!-- books-review:SF-2026-ARXIV-2606-21856:end -->

<!-- existing:SF-2026-ARXIV-2606-21868:start -->
已复读 owner `books/part-05-inference-system/56-inference-scheduling.md` 的机制正文与 Review notes；Ch56 需把 expert weights 与 KV 视为竞争同一容量预算的联合 working set，而不是两个独立 cache。
<!-- existing:SF-2026-ARXIV-2606-21868:end -->

<!-- delta:SF-2026-ARXIV-2606-21868:start -->
WiSP 把低资源 MoE inference 表述为 expert-weight 与 KV cache 的联合 working set：预测近期 active experts，按相同内存预算在 expert residency、KV 保留与 transfer 间分配。
<!-- delta:SF-2026-ARXIV-2606-21868:end -->

<!-- books-review:SF-2026-ARXIV-2606-21868:start -->
Direct Evolution; Integrate. Qwen3/Kimi 的受限设备结果是在 94 GiB H100 上用 gpu-memory-utilization cap 模拟，并非真实小卡；预测错误还会同时触发 expert miss 与 KV pressure，质量保持也不等于 tail SLO。
<!-- books-review:SF-2026-ARXIV-2606-21868:end -->

<!-- existing:SF-2026-ARXIV-2606-21869:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；Ch66 需把语言切片的 energy/quality 联合 contract 加入 evaluation identity；Ch70 只消费成本结果。
<!-- existing:SF-2026-ARXIV-2606-21869:end -->

<!-- delta:SF-2026-ARXIV-2606-21869:start -->
把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。
<!-- delta:SF-2026-ARXIV-2606-21869:end -->

<!-- books-review:SF-2026-ARXIV-2606-21869:start -->
Direct Evolution; Integrate. 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。
<!-- books-review:SF-2026-ARXIV-2606-21869:end -->

<!-- existing:SF-2026-ARXIV-2606-21875:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；Ch66 已区分 confidence、evidence 与 policy-bound triage；本 family 的反向结果强化 calibration boundary。
<!-- existing:SF-2026-ARXIV-2606-21875:end -->

<!-- delta:SF-2026-ARXIV-2606-21875:start -->
Signed Evidence Flow 把已拟合预测的正负 attribution 分解为 support、opposition、conflict 与 perturbation stability；ScopeGate 用 held-out permutation 检查 conflict-risk 方向后才允许 triage。
<!-- delta:SF-2026-ARXIV-2606-21875:end -->

<!-- books-review:SF-2026-ARXIV-2606-21875:start -->
Principle Reuse; No Change — Existing Coverage. SEF 不是 causal explanation；attribution/reference choice 改变数值，相关 feature replacement 可能失真，B=40 stability refit 成本约单次 30.1–39.2 倍。
<!-- books-review:SF-2026-ARXIV-2606-21875:end -->

<!-- existing:SF-2026-ARXIV-2606-21877:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；Ch72 需增加 authority-envelope BOM：依赖 provenance 不能替代 agent 能访问、记忆、修改和委托什么。
<!-- existing:SF-2026-ARXIV-2606-21877:end -->

<!-- delta:SF-2026-ARXIV-2606-21877:start -->
AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。
<!-- delta:SF-2026-ARXIV-2606-21877:end -->

<!-- books-review:SF-2026-ARXIV-2606-21877:start -->
Direct Evolution; Integrate. 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。
<!-- books-review:SF-2026-ARXIV-2606-21877:end -->

<!-- existing:SF-2026-ARXIV-2606-21884:start -->
已复读 owner `books/part-04-training-system/33-grpo.md` 的机制正文与 Review notes；Ch33 需明确 verifiable outcome 不保证 search trace 可蒸馏；训练前先做 forward-derivability test。
<!-- existing:SF-2026-ARXIV-2606-21884:end -->

<!-- delta:SF-2026-ARXIV-2606-21884:start -->
对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。
<!-- delta:SF-2026-ARXIV-2606-21884:end -->

<!-- books-review:SF-2026-ARXIV-2606-21884:start -->
Direct Evolution; Integrate. 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。
<!-- books-review:SF-2026-ARXIV-2606-21884:end -->

<!-- existing:SF-2026-ARXIV-2606-21891:start -->
已复读 owner `books/part-07-agent/81-workflow.md` 的机制正文与 Review notes；Ch81 需把 low score 拆成 hypothesis failure 与 execution failure，防止 workflow 错误地删除可修复分支。
<!-- existing:SF-2026-ARXIV-2606-21891:end -->

<!-- delta:SF-2026-ARXIV-2606-21891:start -->
ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。
<!-- delta:SF-2026-ARXIV-2606-21891:end -->

<!-- books-review:SF-2026-ARXIV-2606-21891:start -->
Direct Evolution; Integrate. scientist/executor 共偏、每 task 的 A100 训练预算与 22-task frontier 不能证明科学发现正确；human-best 和 validation score 仍受 benchmark 约束。
<!-- books-review:SF-2026-ARXIV-2606-21891:end -->

<!-- existing:SF-2026-ARXIV-2606-21917:start -->
已复读 owner `books/part-06-ai-infrastructure/67-monitoring.md` 的机制正文与 Review notes；Ch67 已把 activation/attention monitor 定义为 model-version-bound sensor；该 family 不改变 authority。
<!-- existing:SF-2026-ARXIV-2606-21917:end -->

<!-- delta:SF-2026-ARXIV-2606-21917:start -->
在生成前从 attention probe 预测 hallucination risk，以 soft target 表达不确定度，再把风险交给 abstain、retrieval 或 stronger-model route；sensor 不拥有 truth commit。
<!-- delta:SF-2026-ARXIV-2606-21917:end -->

<!-- books-review:SF-2026-ARXIV-2606-21917:start -->
Principle Reuse; No Change — Existing Coverage. probe 与 label/judge 共偏，attention correlation 不证明因果；生成前预测不能覆盖 retrieval corruption 或生成中途状态变化。
<!-- books-review:SF-2026-ARXIV-2606-21917:end -->

<!-- existing:SF-2026-ARXIV-2606-21954:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；Ch66 需把 transfer capability 与 source-language base ability 解耦，避免版本比较的 denominator inflation。
<!-- existing:SF-2026-ARXIV-2606-21954:end -->

<!-- delta:SF-2026-ARXIV-2606-21954:start -->
Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。
<!-- delta:SF-2026-ARXIV-2606-21954:end -->

<!-- books-review:SF-2026-ARXIV-2606-21954:start -->
Direct Evolution; Integrate. HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。
<!-- books-review:SF-2026-ARXIV-2606-21954:end -->

<!-- existing:SF-2026-ARXIV-2606-21959:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；当前 Ch66 已明确引用不仅要存在还要支持 claim，并已把 deep-research citation support、coverage 与 synthesis 分层；OpenBioRQ 提供 biomedical stress case，但不改变 evaluation owner。
<!-- existing:SF-2026-ARXIV-2606-21959:end -->

<!-- delta:SF-2026-ARXIV-2606-21959:start -->
OpenBioRQ 以未解决研究问题评估 agent：把 citation resolution、actual support、open-status verification 与 answer usefulness分层，并提供冻结 checklist 改善 judge agreement。
<!-- delta:SF-2026-ARXIV-2606-21959:end -->

<!-- books-review:SF-2026-ARXIV-2606-21959:start -->
Principle Reuse; No Change — Existing Coverage. biomedical question set、冻结时点与 judge checklist 不证明未来问题仍未解决；benchmark 不能替代领域专家证据审查。
<!-- books-review:SF-2026-ARXIV-2606-21959:end -->

<!-- existing:SF-2026-ARXIV-2606-21963:start -->
已复读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 的机制正文与 Review notes；Ch73/81 已要求 incident diagnosis 与 executable effect receipt 分离；Holmes 是工业案例。
<!-- existing:SF-2026-ARXIV-2606-21963:end -->

<!-- delta:SF-2026-ARXIV-2606-21963:start -->
Holmes 将 mixed-language mobile crash diagnosis 绑定 log、stack trace、source/change history 与工具执行，输出 diagnosis 与 evidence-linked repair，而非只生成解释文本。
<!-- delta:SF-2026-ARXIV-2606-21963:end -->

<!-- books-review:SF-2026-ARXIV-2606-21963:start -->
Principle Reuse; No Change — Existing Coverage. 单组织 crash taxonomy、内部工具与数据分布限制复现；诊断建议不等于已合并修复或无回归。
<!-- books-review:SF-2026-ARXIV-2606-21963:end -->

<!-- existing:SF-2026-ARXIV-2606-21968:start -->
已复读 owner `books/part-07-agent/81-workflow.md` 的机制正文与 Review notes；Ch81 需把感知分辨率选择建模为有成本、可回退的 route，而不是固定预处理。
<!-- existing:SF-2026-ARXIV-2606-21968:end -->

<!-- delta:SF-2026-ARXIV-2606-21968:start -->
ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。
<!-- delta:SF-2026-ARXIV-2606-21968:end -->

<!-- books-review:SF-2026-ARXIV-2606-21968:start -->
Direct Evolution; Integrate. router confidence 可共偏，小目标/多目标阈值依赖数据；离线 benchmark 不证明实时 latency 或任意 VLM transfer。
<!-- books-review:SF-2026-ARXIV-2606-21968:end -->

<!-- existing:SF-2026-ARXIV-2606-21994:start -->
已复读 owner `books/part-04-training-system/33-grpo.md` 的机制正文与 Review notes；Ch33 已将 OPD 定义为探索催化剂并保留 teacher ceiling；prefix allocation 是同 owner 内实现分支。
<!-- existing:SF-2026-ARXIV-2606-21994:end -->

<!-- delta:SF-2026-ARXIV-2606-21994:start -->
Prefix-Guided OPD 用 teacher/student rollout 的早期 prefix overlap 估计后续 trajectory value，把 rollout budget 转向可能形成 golden trajectory 的前缀。
<!-- delta:SF-2026-ARXIV-2606-21994:end -->

<!-- books-review:SF-2026-ARXIV-2606-21994:start -->
Principle Reuse; No Change — Existing Coverage. 早期 overlap 可能错杀迟发正确路径并放大 teacher/student 共偏；它重分配探索预算，不扩展 teacher capability ceiling。
<!-- books-review:SF-2026-ARXIV-2606-21994:end -->

<!-- existing:SF-2026-ARXIV-2606-22000:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；当前 Ch66 已有专节把 Pass@k 能力覆盖、Pass^k conjunction reliability 与 paired transition 分离，且 action authority 已是独立 evaluation plane；CFAgentBench 不再形成新 delta。
<!-- existing:SF-2026-ARXIV-2606-22000:end -->

<!-- delta:SF-2026-ARXIV-2606-22000:start -->
CFAgentBench 以可执行 construction-finance environment 记录账户/文档 state diff、forbidden side effect 与 approval-required money movement；正确金额但未获批准同样失败。
<!-- delta:SF-2026-ARXIV-2606-22000:end -->

<!-- books-review:SF-2026-ARXIV-2606-22000:start -->
Principle Reuse; No Change — Existing Coverage. synthetic finance workflow 与规则覆盖有限；state-diff checker 不证明真实法规、身份或银行 effect，pass@k 也不能隐藏每次 unauthorized action。
<!-- books-review:SF-2026-ARXIV-2606-22000:end -->

<!-- existing:SF-2026-ARXIV-2606-22013:start -->
已复读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 的机制正文与 Review notes；Ch73 需把 load test 从固定 QPS 清单升级为可复算 SLO-boundary search contract。
<!-- existing:SF-2026-ARXIV-2606-22013:end -->

<!-- delta:SF-2026-ARXIV-2606-22013:start -->
ML serving load test 以 adaptive capacity search 而非固定 traffic sweep，联合寻找满足 latency/SLO 的最大 load 与资源点，并保留 warm-up、arrival 和 model artifact identity。
<!-- delta:SF-2026-ARXIV-2606-22013:end -->

<!-- books-review:SF-2026-ARXIV-2606-22013:start -->
Direct Evolution; Integrate. 14 个匿名生产模型偏向 recommendation/ranking；P90 七日观测吞吐可能低估真实最大 capacity，且结论不能代表 LLM continuous batching。
<!-- books-review:SF-2026-ARXIV-2606-22013:end -->

<!-- existing:SF-2026-ARXIV-2606-22019:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；Ch72 需明确 audit coverage 与 outcome 分离：未覆盖 channel 只能是 Unknown。
<!-- existing:SF-2026-ARXIV-2606-22019:end -->

<!-- delta:SF-2026-ARXIV-2606-22019:start -->
subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。
<!-- delta:SF-2026-ARXIV-2606-22019:end -->

<!-- books-review:SF-2026-ARXIV-2606-22019:start -->
Direct Evolution; Integrate. 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。
<!-- books-review:SF-2026-ARXIV-2606-22019:end -->

<!-- existing:SF-2026-ARXIV-2606-22030:start -->
已复读 owner `books/part-07-agent/77-memory.md` 的机制正文与 Review notes；当前 Ch77 已要求 source calibration、valid-time、独立 corroboration、contradiction、supersession 与 risk-aware selective action共同约束事实 Memory；Bayesian 聚合是既有可靠性读路径的受限实现。
<!-- existing:SF-2026-ARXIV-2606-22030:end -->

<!-- delta:SF-2026-ARXIV-2606-22030:start -->
belief memory 以 Bayesian state 表示候选命题，但只在 source reliability 可估时更新；provenance-capped influence 限制单源/重复证据对 posterior 的控制。
<!-- delta:SF-2026-ARXIV-2606-22030:end -->

<!-- books-review:SF-2026-ARXIV-2606-22030:start -->
Principle Reuse; No Change — Existing Coverage. A-MEM/BeliefMem 数字未由作者重跑且二手表格类别映射曾冲突；GPT-4o-mini 同时做 extraction、answer 与 judge，strict F1 和 judge 可能共偏。
<!-- books-review:SF-2026-ARXIV-2606-22030:end -->

<!-- existing:SF-2026-ARXIV-2606-22043:start -->
已复读 owner `books/part-04-training-system/33-grpo.md` 的机制正文与 Review notes；Ch33 需把 visual reliance 作为训练 trajectory state，而不只在最终 accuracy 后诊断 shortcut。
<!-- existing:SF-2026-ARXIV-2606-22043:end -->

<!-- delta:SF-2026-ARXIV-2606-22043:start -->
multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。
<!-- delta:SF-2026-ARXIV-2606-22043:end -->

<!-- books-review:SF-2026-ARXIV-2606-22043:start -->
Direct Evolution; Integrate. 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。
<!-- books-review:SF-2026-ARXIV-2606-22043:end -->

<!-- existing:SF-2026-ARXIV-2606-22082:start -->
已复读 owner `books/part-07-agent/82-multi-agent.md` 的机制正文与 Review notes；Ch82 已明确 shared repository 需要 commitment protocol、ownership/interface 和可验证提交顺序。
<!-- existing:SF-2026-ARXIV-2606-22082:end -->

<!-- delta:SF-2026-ARXIV-2606-22082:start -->
CodeTeam 先生成竞争架构草案，再由 CTO 产出 machine-checkable ownership/interface contract，随后依 dependency graph 调度实现并运行 repo tests。
<!-- delta:SF-2026-ARXIV-2606-22082:end -->

<!-- books-review:SF-2026-ARXIV-2606-22082:start -->
Principle Reuse; No Change — Existing Coverage. 所有 agents 共享 Qwen2.5-72B-Instruct，CTO contract 可能共享 backbone bias；test suite 不完备时 machine-checkable 只证明 harness 内一致。
<!-- books-review:SF-2026-ARXIV-2606-22082:end -->

<!-- existing:SF-2026-ARXIV-2606-22085:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；Ch72 已将 CoT monitor 定义为 policy-bound sensor，不是 security authority；该负结果强化边界。
<!-- existing:SF-2026-ARXIV-2606-22085:end -->

<!-- delta:SF-2026-ARXIV-2606-22085:start -->
通过在 reasoning trace 中植入受控改动测试模型能否自报 CoT tampering；把 self-report、behavioral change 与 external detector 分离。
<!-- delta:SF-2026-ARXIV-2606-22085:end -->

<!-- books-review:SF-2026-ARXIV-2606-22085:start -->
Principle Reuse; No Change — Existing Coverage. 可见 CoT 不是完整内部 computation；专有 frontier API 不支持 CoT prefilling 因而未测，否认/承认都不是 tamper truth。
<!-- books-review:SF-2026-ARXIV-2606-22085:end -->

<!-- existing:SF-2026-ARXIV-2606-22136:start -->
已复读 owner `books/part-04-training-system/27-data.md` 的机制正文与 Review notes；当前 Ch27 已完整写入 human hand pose→action-conditioned video→pose/depth reconstruction/retargeting→derived robot trajectory provenance→real closed-loop admission；Wh0 正是该现有分支的 source-specific evidence。
<!-- existing:SF-2026-ARXIV-2606-22136:end -->

<!-- delta:SF-2026-ARXIV-2606-22136:start -->
Wh0 用 generative video world model 产生 scene/object/language-conditioned human-hand episodes，再以 hand reconstruction 与 visual editing 转成 robot-trainable supervision，并与少量真实机器人数据 co-train。
<!-- delta:SF-2026-ARXIV-2606-22136:end -->

<!-- books-review:SF-2026-ARXIV-2606-22136:start -->
Principle Reuse; No Change — Existing Coverage. 生成世界模型会携带 physics/contact error，视觉编辑不等于 action 可执行；真实 robot data 仍是 deployment anchor，18 tasks 不证明广泛迁移。
<!-- books-review:SF-2026-ARXIV-2606-22136:end -->

<!-- existing:SF-2026-ARXIV-2606-22142:start -->
已复读 owner `books/part-04-training-system/27-data.md` 的机制正文与 Review notes；Ch27 需把 sample lineage 扩展为 rollout→review→dataset→training→evaluation→release 的 typed lifecycle graph。
<!-- existing:SF-2026-ARXIV-2606-22142:end -->

<!-- delta:SF-2026-ARXIV-2606-22142:start -->
RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。
<!-- delta:SF-2026-ARXIV-2606-22142:end -->

<!-- books-review:SF-2026-ARXIV-2606-22142:start -->
Direct Evolution; Integrate. robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。
<!-- books-review:SF-2026-ARXIV-2606-22142:end -->

<!-- existing:SF-2026-ARXIV-2606-22164:start -->
已复读 owner `books/part-04-training-system/33-grpo.md` 的机制正文与 Review notes；Ch33 需把 decision density 纳入 credit-assignment route：长轨迹本身不是选择 critic 的充分条件。
<!-- existing:SF-2026-ARXIV-2606-22164:end -->

<!-- delta:SF-2026-ARXIV-2606-22164:start -->
多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。
<!-- delta:SF-2026-ARXIV-2606-22164:end -->

<!-- books-review:SF-2026-ARXIV-2606-22164:start -->
Direct Evolution; Integrate. 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。
<!-- books-review:SF-2026-ARXIV-2606-22164:end -->

<!-- existing:SF-2026-ARXIV-2606-22175:start -->
已复读 owner `books/part-07-agent/81-workflow.md` 的机制正文与 Review notes；Ch81 需把 workflow task identity 分成 state-holder 与 invocation；复用必须绑定 model/runtime version 和 tenant。
<!-- existing:SF-2026-ARXIV-2606-22175:end -->

<!-- delta:SF-2026-ARXIV-2606-22175:start -->
StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。
<!-- delta:SF-2026-ARXIV-2606-22175:end -->

<!-- books-review:SF-2026-ARXIV-2606-22175:start -->
Direct Evolution; Integrate. persistent state 会引入 version、tenant isolation、eviction 与 stale-state risk；作者 workflow 不证明交互式 tail latency 或任意 preemptible site。
<!-- books-review:SF-2026-ARXIV-2606-22175:end -->

<!-- existing:SF-2026-ARXIV-2606-22179:start -->
已复读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的机制正文与 Review notes；Ch66 需增加 threshold-resolution contract：ranking 好不代表 operator 有足够可选 operating points。
<!-- existing:SF-2026-ARXIV-2606-22179:end -->

<!-- delta:SF-2026-ARXIV-2606-22179:start -->
selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。
<!-- delta:SF-2026-ARXIV-2606-22179:end -->

<!-- books-review:SF-2026-ARXIV-2606-22179:start -->
Direct Evolution; Integrate. 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。
<!-- books-review:SF-2026-ARXIV-2606-22179:end -->

<!-- existing:SF-2026-ARXIV-2606-22180:start -->
已复读 owner `books/part-04-training-system/36-distributed-training.md` 的机制正文与 Review notes；Ch36 需增加 sampling→quality feedback loop 与 communication freshness 的联合 contract，而非仅 pipeline overlap。
<!-- existing:SF-2026-ARXIV-2606-22180:end -->

<!-- delta:SF-2026-ARXIV-2606-22180:start -->
FeLoG 用 embedding-quality feedback 优先 undertrained node；activity-aware sequence compression/选择同步降低 PCIe 与网络通信，round-interleaved pipeline 重叠下一轮 sampling 与当前 training。
<!-- delta:SF-2026-ARXIV-2606-22180:end -->

<!-- books-review:SF-2026-ARXIV-2606-22180:start -->
Direct Evolution; Integrate. quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。
<!-- books-review:SF-2026-ARXIV-2606-22180:end -->

<!-- existing:SF-2026-ARXIV-2606-22189:start -->
已复读 owner `books/part-04-training-system/27-data.md` 的机制正文与 Review notes；Ch27 已拥有 data gates、dedup、contamination 与 provenance；保留此单 GPU negative RLVR case，不新增 owner。
<!-- existing:SF-2026-ARXIV-2606-22189:end -->

<!-- delta:SF-2026-ARXIV-2606-22189:start -->
在单张 L20 上公开 134.5M 模型的 data gate、cross-source MinHash/LSH、segment dedup、benchmark-overlap removal、SFT weight interpolation 与 RLVR 全链。
<!-- delta:SF-2026-ARXIV-2606-22189:end -->

<!-- books-review:SF-2026-ARXIV-2606-22189:start -->
Principle Reuse; No Change — Existing Coverage. 单 run、自有 harness、小模型与 nominal-token ratio 不证明 scaling law 或统计等价；RLVR 下降只是具体 failure case。
<!-- books-review:SF-2026-ARXIV-2606-22189:end -->

<!-- existing:SF-2026-ARXIV-2606-22203:start -->
已复读 owner `books/part-07-agent/82-multi-agent.md` 的机制正文与 Review notes；Ch82 需禁止用 pairwise interaction 参数外推 group dynamics，并把 model-prior drift 从 emergent consensus 分离。
<!-- existing:SF-2026-ARXIV-2606-22203:end -->

<!-- delta:SF-2026-ARXIV-2606-22203:start -->
先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。
<!-- delta:SF-2026-ARXIV-2606-22203:end -->

<!-- books-review:SF-2026-ARXIV-2606-22203:start -->
Direct Evolution; Integrate. pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。
<!-- books-review:SF-2026-ARXIV-2606-22203:end -->

<!-- existing:SF-2026-ARXIV-2606-22248:start -->
已复读 owner `books/part-04-training-system/27-data.md` 的机制正文与 Review notes；Ch27 已把 curriculum state 与 retention Gate 分离；本 family 仅是架构受限案例。
<!-- existing:SF-2026-ARXIV-2606-22248:end -->

<!-- delta:SF-2026-ARXIV-2606-22248:start -->
SamatNext 交替 Differential-Attention 与简化 DeltaNet state mixer，用 RMS normalization/output calibration 测试 staged code curriculum 的 retention/plasticity。
<!-- delta:SF-2026-ARXIV-2606-22248:end -->

<!-- books-review:SF-2026-ARXIV-2606-22248:start -->
Principle Reuse; No Change — Existing Coverage. 单一受控 curriculum、单 architecture size 且 long-horizon retention 仍弱；不能外推为解决 catastrophic forgetting。
<!-- books-review:SF-2026-ARXIV-2606-22248:end -->

<!-- existing:SF-2026-ARXIV-2606-22263:start -->
已复读 owner `books/part-06-ai-infrastructure/72-security.md` 的机制正文与 Review notes；Ch72 需把 vulnerability report 的 commit authority 绑定 executable PoV+sanitizer，而非 agent verdict。
<!-- existing:SF-2026-ARXIV-2606-22263:end -->

<!-- delta:SF-2026-ARXIV-2606-22263:start -->
Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。
<!-- delta:SF-2026-ARXIV-2606-22263:end -->

<!-- books-review:SF-2026-ARXIV-2606-22263:start -->
Direct Evolution; Integrate. sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。
<!-- books-review:SF-2026-ARXIV-2606-22263:end -->

<!-- existing:SF-2026-ARXIV-2606-22283:start -->
已复读 owner `books/part-05-inference-system/54-gpu-memory.md` 的机制正文与 Review notes；Ch54 需把硬件逆向知识按 measured/decompile-derived/predicted 分层，并保持 Core ML 是唯一 supported production path。
<!-- existing:SF-2026-ARXIV-2606-22283:end -->

<!-- delta:SF-2026-ARXIV-2606-22283:start -->
对 ANE 的 datapath、roofline、compiler/on-disk format、weight compression、driver/firmware command protocol建立 measured/decompile-derived/predicted 三类 claim，并区分 direct private route 与 Core ML supported path。
<!-- delta:SF-2026-ARXIV-2606-22283:end -->

<!-- books-review:SF-2026-ARXIV-2606-22283:start -->
Direct Evolution; Integrate. private runtime/driver 路径 undocumented、unsupported、version-fragile，只适合研究测量；预测项不能冒充芯片公开规格或 shipping contract。
<!-- books-review:SF-2026-ARXIV-2606-22283:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260621-COVERAGE-V1 | fresh-context:jun21-v1 | coverage | coverage:SRC-ARXIV:20260621 | — | 224/224 title+abstract; denominator 37; closures 187; all 54 route-negative checked | passed |
| SA-20260621-EVIDENCE-V1 | fresh-context:jun21-v1 | evidence | review:SF-2026-ARXIV-2606-21822; review:SF-2026-ARXIV-2606-21836; review:SF-2026-ARXIV-2606-21842; review:SF-2026-ARXIV-2606-21843; review:SF-2026-ARXIV-2606-21848; review:SF-2026-ARXIV-2606-21854; review:SF-2026-ARXIV-2606-21856; review:SF-2026-ARXIV-2606-21868; review:SF-2026-ARXIV-2606-21869; review:SF-2026-ARXIV-2606-21875; review:SF-2026-ARXIV-2606-21877; review:SF-2026-ARXIV-2606-21884; review:SF-2026-ARXIV-2606-21891; review:SF-2026-ARXIV-2606-21917; review:SF-2026-ARXIV-2606-21954; review:SF-2026-ARXIV-2606-21959; review:SF-2026-ARXIV-2606-21963; review:SF-2026-ARXIV-2606-21968; review:SF-2026-ARXIV-2606-21994; review:SF-2026-ARXIV-2606-22000; review:SF-2026-ARXIV-2606-22013; review:SF-2026-ARXIV-2606-22019; review:SF-2026-ARXIV-2606-22030; review:SF-2026-ARXIV-2606-22043; review:SF-2026-ARXIV-2606-22082; review:SF-2026-ARXIV-2606-22085; review:SF-2026-ARXIV-2606-22136; review:SF-2026-ARXIV-2606-22142; review:SF-2026-ARXIV-2606-22164; review:SF-2026-ARXIV-2606-22175; review:SF-2026-ARXIV-2606-22179; review:SF-2026-ARXIV-2606-22180; review:SF-2026-ARXIV-2606-22189; review:SF-2026-ARXIV-2606-22203; review:SF-2026-ARXIV-2606-22248; review:SF-2026-ARXIV-2606-22263; review:SF-2026-ARXIV-2606-22283 | — | 37/37 official exact-v1 Method/Evaluation/boundary and benchmark contracts | passed |
| SA-20260621-SELECTION-V1 | fresh-context:jun21-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-21822; analysis-decision:SF-2026-ARXIV-2606-21836; analysis:DA-20260621-NONPREFIX-KV-ISOLATION; analysis-decision:SF-2026-ARXIV-2606-21843; analysis-decision:SF-2026-ARXIV-2606-21848; analysis-decision:SF-2026-ARXIV-2606-21854; analysis-decision:SF-2026-ARXIV-2606-21856; analysis-decision:SF-2026-ARXIV-2606-21868; analysis-decision:SF-2026-ARXIV-2606-21869; analysis-decision:SF-2026-ARXIV-2606-21875; analysis-decision:SF-2026-ARXIV-2606-21877; analysis-decision:SF-2026-ARXIV-2606-21884; analysis-decision:SF-2026-ARXIV-2606-21891; analysis-decision:SF-2026-ARXIV-2606-21917; analysis-decision:SF-2026-ARXIV-2606-21954; analysis-decision:SF-2026-ARXIV-2606-21959; analysis-decision:SF-2026-ARXIV-2606-21963; analysis-decision:SF-2026-ARXIV-2606-21968; analysis-decision:SF-2026-ARXIV-2606-21994; analysis-decision:SF-2026-ARXIV-2606-22000; analysis-decision:SF-2026-ARXIV-2606-22013; analysis-decision:SF-2026-ARXIV-2606-22019; analysis:DA-20260621-BELIEF-MEMORY-AUTHORITY; analysis-decision:SF-2026-ARXIV-2606-22043; analysis-decision:SF-2026-ARXIV-2606-22082; analysis-decision:SF-2026-ARXIV-2606-22085; analysis-decision:SF-2026-ARXIV-2606-22136; analysis:DA-20260621-TYPED-ROBOT-LINEAGE; analysis-decision:SF-2026-ARXIV-2606-22164; analysis-decision:SF-2026-ARXIV-2606-22175; analysis-decision:SF-2026-ARXIV-2606-22179; analysis-decision:SF-2026-ARXIV-2606-22180; analysis-decision:SF-2026-ARXIV-2606-22189; analysis-decision:SF-2026-ARXIV-2606-22203; analysis-decision:SF-2026-ARXIV-2606-22248; analysis-decision:SF-2026-ARXIV-2606-22263; analysis-decision:SF-2026-ARXIV-2606-22283 | — | 37/37 frontier; winners frozen before rationale | passed |
| SA-20260621-BOOKS-POSTWRITE-V1 | fresh-context:jun21-v1 | books | books-review:SF-2026-ARXIV-2606-21822; books-review:SF-2026-ARXIV-2606-21836; books-review:SF-2026-ARXIV-2606-21842; books-review:SF-2026-ARXIV-2606-21843; books-review:SF-2026-ARXIV-2606-21848; books-review:SF-2026-ARXIV-2606-21854; books-review:SF-2026-ARXIV-2606-21856; books-review:SF-2026-ARXIV-2606-21868; books-review:SF-2026-ARXIV-2606-21869; books-review:SF-2026-ARXIV-2606-21875; books-review:SF-2026-ARXIV-2606-21877; books-review:SF-2026-ARXIV-2606-21884; books-review:SF-2026-ARXIV-2606-21891; books-review:SF-2026-ARXIV-2606-21917; books-review:SF-2026-ARXIV-2606-21954; books-review:SF-2026-ARXIV-2606-21959; books-review:SF-2026-ARXIV-2606-21963; books-review:SF-2026-ARXIV-2606-21968; books-review:SF-2026-ARXIV-2606-21994; books-review:SF-2026-ARXIV-2606-22000; books-review:SF-2026-ARXIV-2606-22013; books-review:SF-2026-ARXIV-2606-22019; books-review:SF-2026-ARXIV-2606-22030; books-review:SF-2026-ARXIV-2606-22043; books-review:SF-2026-ARXIV-2606-22082; books-review:SF-2026-ARXIV-2606-22085; books-review:SF-2026-ARXIV-2606-22136; books-review:SF-2026-ARXIV-2606-22142; books-review:SF-2026-ARXIV-2606-22164; books-review:SF-2026-ARXIV-2606-22175; books-review:SF-2026-ARXIV-2606-22179; books-review:SF-2026-ARXIV-2606-22180; books-review:SF-2026-ARXIV-2606-22189; books-review:SF-2026-ARXIV-2606-22203; books-review:SF-2026-ARXIV-2606-22248; books-review:SF-2026-ARXIV-2606-22263; books-review:SF-2026-ARXIV-2606-22283 | — | 20/20 Integrate writebacks across 12 owners plus 17/17 No Change handoffs passed the post-write fresh audit; unresolved findings 0 | passed |

### Materials and Access

- 37/37 exact-v1 official HTML pages were accessible; no later revision was used.
- No external Materials Request remains.

## 8. Ignored Noise

- 187 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit rather than being promoted into the Candidate Ledger.

## 9. Recommended Action

- Integrate: 20/20 written into 12 unique owners; No Change: 17/17 revalidated.
- Post-write fresh audit: 37/37 Passed; Books Gate Passed and Completion is Complete.

## 10. Repository Changes

- Root performed the serialized 20-family Books writeback across 12 owners; this lane changed only the 2026-06-21 Daily/source packet/date-local scripts and audited the shared result.

## 11. Open Questions

- How should non-prefix KV reuse expose tenant and retrieval identity without eliminating useful cache sharing?
- Which reliability and provenance cap keeps belief memory useful without turning repeated claims into false authority?
- How should robot data lineage invalidate downstream policies when a rollout, reviewer or environment version is superseded?
- These are research continuations, not unresolved Gate findings.

## 12. Sources

- [arXiv:2606.21822v1 — CNnotator: LLM-Guided Memory Safety Annotation Synthesis](https://arxiv.org/html/2606.21822v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21822`。
- [arXiv:2606.21836v1 — AgentDSE: Reasoning-Augmented Architectural Design Space Exploration](https://arxiv.org/html/2606.21836v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21836`。
- [arXiv:2606.21842v1 — Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG](https://arxiv.org/html/2606.21842v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21842`。
- [arXiv:2606.21843v1 — Measuring What Persists: Conditioning Mechanisms and a Geometric Framework for AI Agent Identity](https://arxiv.org/html/2606.21843v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21843`。
- [arXiv:2606.21848v1 — Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers](https://arxiv.org/html/2606.21848v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21848`。
- [arXiv:2606.21854v1 — ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era](https://arxiv.org/html/2606.21854v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21854`。
- [arXiv:2606.21856v1 — Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents](https://arxiv.org/html/2606.21856v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21856`。
- [arXiv:2606.21868v1 — WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/html/2606.21868v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21868`。
- [arXiv:2606.21869v1 — The Language-Energy Divide: Measuring Energy Costs of Multilingual LLM Inference](https://arxiv.org/html/2606.21869v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21869`。
- [arXiv:2606.21875v1 — Signed Evidence Flow: Conflict-Aware and Stability-Calibrated Data Analysis](https://arxiv.org/html/2606.21875v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21875`。
- [arXiv:2606.21877v1 — AgentRiskBOM: A Risk-Scoping Security Bill of Materials for Agentic AI Systems](https://arxiv.org/html/2606.21877v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21877`。
- [arXiv:2606.21884v1 — A Verifiable Search Is Not a Learnable Chain-of-Thought](https://arxiv.org/html/2606.21884v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21884`。
- [arXiv:2606.21891v1 — Learning the ARTS of Search for Automated Discovery](https://arxiv.org/html/2606.21891v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21891`。
- [arXiv:2606.21917v1 — Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing](https://arxiv.org/html/2606.21917v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21917`。
- [arXiv:2606.21954v1 — Are Multilingual Models Actually Improving? Isolating True Cross-Lingual Transfer](https://arxiv.org/html/2606.21954v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21954`。
- [arXiv:2606.21959v1 — OpenBioRQ: Unsolved Biomedical Research Questions for Agents](https://arxiv.org/html/2606.21959v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21959`。
- [arXiv:2606.21963v1 — Holmes: Multimodal Agentic Diagnosis for Mixed-Language Mobile Crashes at Industrial Scale](https://arxiv.org/html/2606.21963v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21963`。
- [arXiv:2606.21968v1 — Look Before You Zoom: Adaptive Routing for the Resolution-Context Trade-off in Visual RAG](https://arxiv.org/html/2606.21968v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21968`。
- [arXiv:2606.21994v1 — Prefix-Guided On-Policy Distillation: Mining Golden Trajectories from Rollouts](https://arxiv.org/html/2606.21994v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-21994`。
- [arXiv:2606.22000v1 — CFAgentBench: A Reproducible Environment and Benchmark for Autonomous Construction-Finance Agents](https://arxiv.org/html/2606.22000v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22000`。
- [arXiv:2606.22013v1 — Load Testing for Machine Learning Model Serving Systems at Scale](https://arxiv.org/html/2606.22013v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22013`。
- [arXiv:2606.22019v1 — Channel Location Constrains the Auditability of Subliminal Learning](https://arxiv.org/html/2606.22019v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22019`。
- [arXiv:2606.22030v1 — When Does Belief-Based Agent Memory Help? Reliability-Conditional Updating and Provenance-Capped Poisoning Defense](https://arxiv.org/html/2606.22030v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22030`。
- [arXiv:2606.22043v1 — When Does a Video-Language Model Stop Watching? Reward Strength Controls the Formation and Reversal of Visual Shortcuts in Multimodal RLVR](https://arxiv.org/html/2606.22043v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22043`。
- [arXiv:2606.22082v1 — CodeTeam: An LLM-Powered Multi-Agent Framework for Repository-Level Code Generation](https://arxiv.org/html/2606.22082v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22082`。
- [arXiv:2606.22085v1 — Can Reasoning Models Detect Changes to their Chains of Thought?](https://arxiv.org/html/2606.22085v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22085`。
- [arXiv:2606.22136v1 — Wh0: Generative World Models as Scalable Sources of Egocentric Human Hand Manipulation Data](https://arxiv.org/html/2606.22136v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22136`。
- [arXiv:2606.22142v1 — RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/html/2606.22142v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22142`。
- [arXiv:2606.22164v1 — Drowning in Routine: Signal Dilution in Multi-Turn Agent Training](https://arxiv.org/html/2606.22164v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22164`。
- [arXiv:2606.22175v1 — StickyInvoc: Rethinking Task Models for High-throughput Workflows in the LLM Era](https://arxiv.org/html/2606.22175v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22175`。
- [arXiv:2606.22179v1 — The Score Granularity Gap in Black-Box LLM Classification: A Comparative Study of Confidence Constructions](https://arxiv.org/html/2606.22179v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22179`。
- [arXiv:2606.22180v1 — FeLoG: Scalable and Efficient Distributed Graph Embedding with Feedback Loop Mechanism](https://arxiv.org/html/2606.22180v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22180`。
- [arXiv:2606.22189v1 — L20-Edu-135M: An Auditable Single-GPU Study of Data-Efficient Small Language Modeling](https://arxiv.org/html/2606.22189v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22189`。
- [arXiv:2606.22203v1 — When Is Emergent Consensus Real? A Measured Coupling Gain and a Validity Diagnostic for LLM Agent Societies](https://arxiv.org/html/2606.22203v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22203`。
- [arXiv:2606.22248v1 — SamatNext v0.2-B: An Exploratory Study of RMS-Normalized Hybrid Decoders for Curriculum Retention in Small Code Models](https://arxiv.org/html/2606.22248v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22248`。
- [arXiv:2606.22263v1 — Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/html/2606.22263v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22263`。
- [arXiv:2606.22283v1 — Apple Neural Engine: Architecture, Programming, and Performance](https://arxiv.org/html/2606.22283v1) — first-public `2026-06-20`；accessed `2026-08-30`；Source Family `SF-2026-ARXIV-2606-22283`。
- `SRC-ARXIV` registry contract：`docs/RESEARCH_SOURCES.md`。

## 13. Final Status

- Status: Complete.
- Coverage Gate: Closed.
- Evidence Gate: Passed.
- Books Gate: Passed.
- Fresh-context Semantic Audit: Passed；unresolved findings = 0.

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
