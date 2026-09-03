# Daily Research — 2026-05-21

**Research Date:** 2026-05-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-20 09:00:00 ～ 2026-05-21 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 662 个注册 arXiv identity，冻结 63 个 Source Family；pre-denominator closure=599，withdrawn pre-denominator=0。16 个旧候选被迁回正确 owner day，1 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-21 |
| Window End | 2026-05-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260521-CREATED-ce043355ca51bc2c |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-20T09:00:00+08:00 | 2026-05-21T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 662 | SF-2026-ARXIV-2605-20196;SF-2026-ARXIV-2605-20251;SF-2026-ARXIV-2605-20270;SF-2026-ARXIV-2605-20295;SF-2026-ARXIV-2605-20296;SF-2026-ARXIV-2605-20312;SF-2026-ARXIV-2605-20314;SF-2026-ARXIV-2605-20315;SF-2026-ARXIV-2605-20402;SF-2026-ARXIV-2605-20477;SF-2026-ARXIV-2605-20485;SF-2026-ARXIV-2605-20490;SF-2026-ARXIV-2605-20520;SF-2026-ARXIV-2605-20544;SF-2026-ARXIV-2605-20548;SF-2026-ARXIV-2605-20563;SF-2026-ARXIV-2605-20616;SF-2026-ARXIV-2605-20630;SF-2026-ARXIV-2605-20641;SF-2026-ARXIV-2605-20696;SF-2026-ARXIV-2605-20704;SF-2026-ARXIV-2605-20706;SF-2026-ARXIV-2605-20734;SF-2026-ARXIV-2605-20744;SF-2026-ARXIV-2605-20749;SF-2026-ARXIV-2605-20752;SF-2026-ARXIV-2605-20756;SF-2026-ARXIV-2605-20767;SF-2026-ARXIV-2605-20774;SF-2026-ARXIV-2605-20798;SF-2026-ARXIV-2605-20799;SF-2026-ARXIV-2605-20833;SF-2026-ARXIV-2605-20834;SF-2026-ARXIV-2605-20863;SF-2026-ARXIV-2605-20866;SF-2026-ARXIV-2605-20868;SF-2026-ARXIV-2605-20874;SF-2026-ARXIV-2605-20876;SF-2026-ARXIV-2605-20923;SF-2026-ARXIV-2605-20926;SF-2026-ARXIV-2605-20948;SF-2026-ARXIV-2605-21061;SF-2026-ARXIV-2605-21100;SF-2026-ARXIV-2605-21103;SF-2026-ARXIV-2605-21125;SF-2026-ARXIV-2605-21127;SF-2026-ARXIV-2605-21177;SF-2026-ARXIV-2605-21187;SF-2026-ARXIV-2605-21266;SF-2026-ARXIV-2605-21273;SF-2026-ARXIV-2605-21312;SF-2026-ARXIV-2605-21347;SF-2026-ARXIV-2605-21384;SF-2026-ARXIV-2605-21392;SF-2026-ARXIV-2605-21427;SF-2026-ARXIV-2605-21434;SF-2026-ARXIV-2605-21446;SF-2026-ARXIV-2605-21467;SF-2026-ARXIV-2605-21468;SF-2026-ARXIV-2605-21470;SF-2026-ARXIV-2605-21482;SF-2026-ARXIV-2605-21486;SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | created-day pages=closed; OAI category sets=closed; direct same-day OAI=508 | 2026-05-21T09:00:00+08:00 | coverage:SRC-ARXIV:20260521 | — |

<!-- coverage:SRC-ARXIV:20260521:start -->全量 raw inventory=662；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260521:end -->

### Coverage Limitations

- arXiv 月度 listing 只证明月份收录；逐日 owner 使用 initial DOI `created` 日历日 proxy，并以 exact-v1 history 与官方发布节奏约束。
- DOI ingestion timestamp 不是精确的 09:00 publication instant；本日报不把 `updated` 或 current OAI datestamp 当作 first-public。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
None — 没有 exact-version primary-material blocker。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20196 | arXiv:2605.20196v1 | paper-v1:2605.20196 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-20196 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20196 | yes |
| SF-2026-ARXIV-2605-20251 | arXiv:2605.20251v1 | paper-v1:2605.20251 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20251 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20251 | no |
| SF-2026-ARXIV-2605-20270 | arXiv:2605.20270v1 | paper-v1:2605.20270 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20270 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20270 | no |
| SF-2026-ARXIV-2605-20295 | arXiv:2605.20295v1 | paper-v1:2605.20295 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20295 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-20295 | no |
| SF-2026-ARXIV-2605-20296 | arXiv:2605.20296v1 | paper-v1:2605.20296 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20296 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-20296 | no |
| SF-2026-ARXIV-2605-20312 | arXiv:2605.20312v1 | paper-v1:2605.20312 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20312 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2605-20312 | no |
| SF-2026-ARXIV-2605-20314 | arXiv:2605.20314v1 | paper-v1:2605.20314 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20314 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-20314 | no |
| SF-2026-ARXIV-2605-20315 | arXiv:2605.20315v1 | paper-v1:2605.20315 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20315 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20315 | no |
| SF-2026-ARXIV-2605-20402 | arXiv:2605.20402v1 | paper-v1:2605.20402 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20402 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20402 | no |
| SF-2026-ARXIV-2605-20477 | arXiv:2605.20477v1 | paper-v1:2605.20477 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20477 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20477 | no |
| SF-2026-ARXIV-2605-20485 | arXiv:2605.20485v1 | paper-v1:2605.20485 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20485 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-20485 | no |
| SF-2026-ARXIV-2605-20490 | arXiv:2605.20490v1 | paper-v1:2605.20490 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20490 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-20490 | no |
| SF-2026-ARXIV-2605-20520 | arXiv:2605.20520v1 | paper-v1:2605.20520 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20520 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-20520 | no |
| SF-2026-ARXIV-2605-20544 | arXiv:2605.20544v1 | paper-v1:2605.20544 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20544 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-20544 | no |
| SF-2026-ARXIV-2605-20548 | arXiv:2605.20548v1 | paper-v1:2605.20548 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20548 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20548 | no |
| SF-2026-ARXIV-2605-20563 | arXiv:2605.20563v1 | paper-v1:2605.20563 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20563 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-20563 | no |
| SF-2026-ARXIV-2605-20616 | arXiv:2605.20616v1 | paper-v1:2605.20616 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20616 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20616 | no |
| SF-2026-ARXIV-2605-20630 | arXiv:2605.20630v1 | paper-v1:2605.20630 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20630 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20630 | no |
| SF-2026-ARXIV-2605-20641 | arXiv:2605.20641v1 | paper-v1:2605.20641 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20641 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-20641 | no |
| SF-2026-ARXIV-2605-20696 | arXiv:2605.20696v1 | paper-v1:2605.20696 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20696 | self | — | new_in_window | TRAIN-DPO | Integrate | books-review:SF-2026-ARXIV-2605-20696 | no |
| SF-2026-ARXIV-2605-20704 | arXiv:2605.20704v1 | paper-v1:2605.20704 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20704 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20704 | no |
| SF-2026-ARXIV-2605-20706 | arXiv:2605.20706v1 | paper-v1:2605.20706 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20706 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20706 | no |
| SF-2026-ARXIV-2605-20734 | arXiv:2605.20734v1 | paper-v1:2605.20734 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20734 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20734 | no |
| SF-2026-ARXIV-2605-20744 | arXiv:2605.20744v1 | paper-v1:2605.20744 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20744 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20744 | no |
| SF-2026-ARXIV-2605-20749 | arXiv:2605.20749v1 | paper-v1:2605.20749 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20749 | self | — | new_in_window | MODEL-FFN | Integrate | books-review:SF-2026-ARXIV-2605-20749 | no |
| SF-2026-ARXIV-2605-20752 | arXiv:2605.20752v1 | paper-v1:2605.20752 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20752 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20752 | no |
| SF-2026-ARXIV-2605-20756 | arXiv:2605.20756v1 | paper-v1:2605.20756 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20756 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-20756 | no |
| SF-2026-ARXIV-2605-20767 | arXiv:2605.20767v1 | paper-v1:2605.20767 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20767 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20767 | no |
| SF-2026-ARXIV-2605-20774 | arXiv:2605.20774v1 | paper-v1:2605.20774 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20774 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20774 | no |
| SF-2026-ARXIV-2605-20798 | arXiv:2605.20798v1 | paper-v1:2605.20798 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20798 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20798 | no |
| SF-2026-ARXIV-2605-20799 | arXiv:2605.20799v1 | paper-v1:2605.20799 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20799 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-20799 | no |
| SF-2026-ARXIV-2605-20833 | arXiv:2605.20833v1 | paper-v1:2605.20833 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20833 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20833 | no |
| SF-2026-ARXIV-2605-20834 | arXiv:2605.20834v1 | paper-v1:2605.20834 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20834 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20834 | no |
| SF-2026-ARXIV-2605-20863 | arXiv:2605.20863v1 | paper-v1:2605.20863 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20863 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20863 | no |
| SF-2026-ARXIV-2605-20866 | arXiv:2605.20866v1 | paper-v1:2605.20866 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20866 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20866 | no |
| SF-2026-ARXIV-2605-20868 | arXiv:2605.20868v1 | paper-v1:2605.20868 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20868 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20868 | no |
| SF-2026-ARXIV-2605-20874 | arXiv:2605.20874v1 | paper-v1:2605.20874 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20874 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20874 | no |
| SF-2026-ARXIV-2605-20876 | arXiv:2605.20876v1 | paper-v1:2605.20876 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20876 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20876 | no |
| SF-2026-ARXIV-2605-20923 | arXiv:2605.20923v1 | paper-v1:2605.20923 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20923 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-20923 | no |
| SF-2026-ARXIV-2605-20926 | arXiv:2605.20926v1 | paper-v1:2605.20926 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20926 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20926 | no |
| SF-2026-ARXIV-2605-20948 | arXiv:2605.20948v1 | paper-v1:2605.20948 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20948 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20948 | no |
| SF-2026-ARXIV-2605-21061 | arXiv:2605.21061v1 | paper-v1:2605.21061 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21061 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-21061 | no |
| SF-2026-ARXIV-2605-21100 | arXiv:2605.21100v1 | paper-v1:2605.21100 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21100 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-21100 | no |
| SF-2026-ARXIV-2605-21103 | arXiv:2605.21103v1 | paper-v1:2605.21103 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21103 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-21103 | no |
| SF-2026-ARXIV-2605-21125 | arXiv:2605.21125v1 | paper-v1:2605.21125 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21125 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21125 | no |
| SF-2026-ARXIV-2605-21127 | arXiv:2605.21127v1 | paper-v1:2605.21127 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21127 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-21127 | no |
| SF-2026-ARXIV-2605-21177 | arXiv:2605.21177v1 | paper-v1:2605.21177 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21177 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21177 | no |
| SF-2026-ARXIV-2605-21187 | arXiv:2605.21187v1 | paper-v1:2605.21187 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21187 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21187 | no |
| SF-2026-ARXIV-2605-21266 | arXiv:2605.21266v1 | paper-v1:2605.21266 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21266 | self | — | new_in_window | TRAIN-DPO | Integrate | books-review:SF-2026-ARXIV-2605-21266 | no |
| SF-2026-ARXIV-2605-21273 | arXiv:2605.21273v1 | paper-v1:2605.21273 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21273 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-21273 | no |
| SF-2026-ARXIV-2605-21312 | arXiv:2605.21312v1 | paper-v1:2605.21312 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21312 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21312 | no |
| SF-2026-ARXIV-2605-21347 | arXiv:2605.21347v1 | paper-v1:2605.21347 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21347 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21347 | no |
| SF-2026-ARXIV-2605-21384 | arXiv:2605.21384v1 | paper-v1:2605.21384 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21384 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21384 | no |
| SF-2026-ARXIV-2605-21392 | arXiv:2605.21392v1 | paper-v1:2605.21392 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21392 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21392 | no |
| SF-2026-ARXIV-2605-21427 | arXiv:2605.21427v1 | paper-v1:2605.21427 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21427 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21427 | no |
| SF-2026-ARXIV-2605-21434 | arXiv:2605.21434v1 | paper-v1:2605.21434 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21434 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21434 | no |
| SF-2026-ARXIV-2605-21446 | arXiv:2605.21446v1 | paper-v1:2605.21446 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21446 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21446 | no |
| SF-2026-ARXIV-2605-21467 | arXiv:2605.21467v1 | paper-v1:2605.21467 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21467 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21467 | no |
| SF-2026-ARXIV-2605-21468 | arXiv:2605.21468v1 | paper-v1:2605.21468 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21468 | self | — | new_in_window | TRAIN-CHECKPOINT | Integrate | books-review:SF-2026-ARXIV-2605-21468 | no |
| SF-2026-ARXIV-2605-21470 | arXiv:2605.21470v1 | paper-v1:2605.21470 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21470 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21470 | no |
| SF-2026-ARXIV-2605-21482 | arXiv:2605.21482v1 | paper-v1:2605.21482 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21482 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21482 | no |
| SF-2026-ARXIV-2605-21486 | arXiv:2605.21486v1 | paper-v1:2605.21486 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21486 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21486 | no |
| SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | arXiv:2605.20223v1 | paper-v1:2605.20223 | 2026-W21 | 2026-05-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20196 | RP-1712361877902f10 | standard | arXiv:2605.20196v1 | SRC-ARXIV@arXiv:2605.20196v1 | https://arxiv.org/html/2605.20196v1#S2 | https://arxiv.org/html/2605.20196v1#S4 | https://arxiv.org/html/2605.20196v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-20196 | complete |
| SF-2026-ARXIV-2605-20251 | RP-070441416d60c224 | deep | arXiv:2605.20251v1 | SRC-ARXIV@arXiv:2605.20251v1 | arXiv:2605.20251v1 HTML — §3.1–3.5 trajectory/control contract | arXiv:2605.20251v1 HTML — §4.1–4.5 experiments | arXiv:2605.20251v1 HTML — §5 Limitations and Conclusion | arXiv:2605.20251v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-20251 | complete |
| SF-2026-ARXIV-2605-20270 | RP-15488bfb8700e030 | deep | arXiv:2605.20270v1 | SRC-ARXIV@arXiv:2605.20270v1 | arXiv:2605.20270v1 HTML — §1–§4 deployment contract and e-process | arXiv:2605.20270v1 HTML — §5–§7 proofs and 650-stream evaluation | arXiv:2605.20270v1 HTML — §8 limitations and boundary | arXiv:2605.20270v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-20270 | complete |
| SF-2026-ARXIV-2605-20295 | RP-7907d828a266cdc4 | deep | arXiv:2605.20295v1 | SRC-ARXIV@arXiv:2605.20295v1 | arXiv:2605.20295v1 HTML — §4 fully static NPU quantization | arXiv:2605.20295v1 HTML — §5 on-device NPU evaluation | arXiv:2605.20295v1 HTML — Appendix H Limitations | https://arxiv.org/html/2605.20295v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20295 | complete |
| SF-2026-ARXIV-2605-20296 | RP-a78d40cdbfd9bec7 | deep | arXiv:2605.20296v1 | SRC-ARXIV@arXiv:2605.20296v1 | arXiv:2605.20296v1 HTML — §3 checkpoint-delta spectral repair | arXiv:2605.20296v1 HTML — §4 fourteen-cell recovery/preservation evaluation | arXiv:2605.20296v1 HTML — §5 Limitations and conclusion | https://arxiv.org/html/2605.20296v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20296 | complete |
| SF-2026-ARXIV-2605-20312 | RP-d161bf7e0fb42648 | deep | arXiv:2605.20312v1 | SRC-ARXIV@arXiv:2605.20312v1 | arXiv:2605.20312v1 HTML — §2 claim primitives; §3 protocol composition | arXiv:2605.20312v1 HTML — §5 pilot; §6 formal properties | arXiv:2605.20312v1 HTML — §8 Limitations | https://arxiv.org/html/2605.20312v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20312 | complete |
| SF-2026-ARXIV-2605-20314 | RP-a0ae0ea6977a8b48 | deep | arXiv:2605.20314v1 | SRC-ARXIV@arXiv:2605.20314v1 | arXiv:2605.20314v1 HTML — §2 reuse setup; §3–§5 sampling-bias and relative-norm mechanism | arXiv:2605.20314v1 HTML — §5 empirical interventions; Appendix B | arXiv:2605.20314v1 HTML — §6 discussion: when data repetition is and is not helpful | https://arxiv.org/html/2605.20314v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20314 | complete |
| SF-2026-ARXIV-2605-20315 | RP-ee48aa55a836d1af | deep | arXiv:2605.20315v1 | SRC-ARXIV@arXiv:2605.20315v1 | arXiv:2605.20315v1 HTML — §3 quantized-prefill/precise-decode split | arXiv:2605.20315v1 HTML — §4 Experiments | arXiv:2605.20315v1 HTML — §5 Conclusion and hardware boundary | https://arxiv.org/html/2605.20315v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20315 | complete |
| SF-2026-ARXIV-2605-20402 | RP-b412da617cab60db | deep | arXiv:2605.20402v1 | SRC-ARXIV@arXiv:2605.20402v1 | arXiv:2605.20402v1 HTML — §5 MXFP4 error decomposition | arXiv:2605.20402v1 HTML — §6 RL quantization experiments | arXiv:2605.20402v1 HTML — §7 Limitations | https://arxiv.org/html/2605.20402v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20402 | complete |
| SF-2026-ARXIV-2605-20477 | RP-cc0b2ab7beac44c0 | deep | arXiv:2605.20477v1 | SRC-ARXIV@arXiv:2605.20477v1 | arXiv:2605.20477v1 HTML — §3–§4 reflection-learning pipeline | arXiv:2605.20477v1 HTML — §5 MiniHack/ALFWorld evaluation | arXiv:2605.20477v1 HTML — §5.3 Limitations | https://arxiv.org/html/2605.20477v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20477 | complete |
| SF-2026-ARXIV-2605-20485 | RP-cdd729450155237c | deep | arXiv:2605.20485v1 | SRC-ARXIV@arXiv:2605.20485v1 | arXiv:2605.20485v1 HTML — §3 budgeted model-orchestration policy | arXiv:2605.20485v1 HTML — §4–§5 zero-shot allocation evaluation | arXiv:2605.20485v1 HTML — §6 Limitations | https://arxiv.org/html/2605.20485v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20485 | complete |
| SF-2026-ARXIV-2605-20490 | RP-af05659cd7b58278 | deep | arXiv:2605.20490v1 | SRC-ARXIV@arXiv:2605.20490v1 | arXiv:2605.20490v1 HTML — §2–§3 ECUAS decision-theoretic metric family | arXiv:2605.20490v1 HTML — §4 evaluator and QA studies | arXiv:2605.20490v1 HTML — § unnumbered exact heading ‘Limitations’: equivalence evaluator and utility assumptions | https://arxiv.org/html/2605.20490v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20490 | complete |
| SF-2026-ARXIV-2605-20520 | RP-2557e71bb9ec40af | deep | arXiv:2605.20520v1 | SRC-ARXIV@arXiv:2605.20520v1 | arXiv:2605.20520v1 HTML — §2 open-world evaluation framework | arXiv:2605.20520v1 HTML — §3 case studies and capability evidence | arXiv:2605.20520v1 HTML — §2.4 Limitations: complements, not replaces, benchmarks | https://arxiv.org/html/2605.20520v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20520 | complete |
| SF-2026-ARXIV-2605-20544 | RP-5b9c06b480604db5 | deep | arXiv:2605.20544v1 | SRC-ARXIV@arXiv:2605.20544v1 | arXiv:2605.20544v1 HTML — §3 grounded abstention taxonomy and deterministic constraint pipeline | arXiv:2605.20544v1 HTML — §4 6,069-instruction embodied VLM evaluation | arXiv:2605.20544v1 HTML — §5 Discussion; guarantees remain conditional on scene extraction | https://arxiv.org/html/2605.20544v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20544 | complete |
| SF-2026-ARXIV-2605-20548 | RP-ea7bc358093853e1 | deep | arXiv:2605.20548v1 | SRC-ARXIV@arXiv:2605.20548v1 | arXiv:2605.20548v1 HTML — §3–§4 communication-content instrumentation | arXiv:2605.20548v1 HTML — §5 and Appendix C.2 occlusion evaluation | arXiv:2605.20548v1 HTML — §6 Limitations | https://arxiv.org/html/2605.20548v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20548 | complete |
| SF-2026-ARXIV-2605-20563 | RP-d3759ea7faaeb585 | deep | arXiv:2605.20563v1 | SRC-ARXIV@arXiv:2605.20563v1 | arXiv:2605.20563v1 HTML — §3–§4 state-management and annotation protocol | arXiv:2605.20563v1 HTML — §5 evaluation; Appendix A setup | arXiv:2605.20563v1 HTML — Appendix E Limitations | https://arxiv.org/html/2605.20563v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20563 | complete |
| SF-2026-ARXIV-2605-20616 | RP-3c8483398da1e9c8 | deep | arXiv:2605.20616v1 | SRC-ARXIV@arXiv:2605.20616v1 | arXiv:2605.20616v1 HTML — §4 Offline Memory Consolidation | arXiv:2605.20616v1 HTML — §5 Experiments | arXiv:2605.20616v1 HTML — Appendix A Limitations | https://arxiv.org/html/2605.20616v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20616 | complete |
| SF-2026-ARXIV-2605-20630 | RP-b18decace203d62c | deep | arXiv:2605.20630v1 | SRC-ARXIV@arXiv:2605.20630v1 | arXiv:2605.20630v1 HTML — §3 Optimization Framework | arXiv:2605.20630v1 HTML — §4 Results | arXiv:2605.20630v1 HTML — §5 Limitations and Failure Modes | https://arxiv.org/html/2605.20630v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20630 | complete |
| SF-2026-ARXIV-2605-20641 | RP-0af1c36c45e213b8 | deep | arXiv:2605.20641v1 | SRC-ARXIV@arXiv:2605.20641v1 | arXiv:2605.20641v1 HTML — §3 Optimization-Triggered Attack Design | arXiv:2605.20641v1 HTML — §4 Implementation and Evaluation | arXiv:2605.20641v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.20641v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20641 | complete |
| SF-2026-ARXIV-2605-20696 | RP-bad47fe65a10384f | deep | arXiv:2605.20696v1 | SRC-ARXIV@arXiv:2605.20696v1 | arXiv:2605.20696v1 HTML — §3 Problem Formulation and Preliminaries | arXiv:2605.20696v1 HTML — §7 Numerical Results; §Appendix E Additional Detail for Experimental Setup; §Appendix F Additional Results | arXiv:2605.20696v1 HTML — §8 Conclusion | https://arxiv.org/html/2605.20696v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20696 | complete |
| SF-2026-ARXIV-2605-20704 | RP-4a6655121c220736 | deep | arXiv:2605.20704v1 | SRC-ARXIV@arXiv:2605.20704v1 | arXiv:2605.20704v1 HTML — §4.1–§4.6 Heartbeat-Bound Credential Protocol | arXiv:2605.20704v1 HTML — §6 Evaluation | arXiv:2605.20704v1 HTML — §7 Limitations and Future Work | https://arxiv.org/html/2605.20704v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20704 | complete |
| SF-2026-ARXIV-2605-20706 | RP-bd1d9c0d2aa3ce0c | deep | arXiv:2605.20706v1 | SRC-ARXIV@arXiv:2605.20706v1 | arXiv:2605.20706v1 HTML — §3 LlamaWeb Architecture | arXiv:2605.20706v1 HTML — §5 Evaluation | arXiv:2605.20706v1 HTML — §6 Discussion and WebGPU portability boundary | https://arxiv.org/html/2605.20706v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20706 | complete |
| SF-2026-ARXIV-2605-20734 | RP-885a316010579e11 | deep | arXiv:2605.20734v1 | SRC-ARXIV@arXiv:2605.20734v1 | arXiv:2605.20734v1 HTML — §4 Multi-Modal Reference Monitor | arXiv:2605.20734v1 HTML — §7 Evaluation | arXiv:2605.20734v1 HTML — §8 Limitations and Future Work | https://arxiv.org/html/2605.20734v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20734 | complete |
| SF-2026-ARXIV-2605-20744 | RP-d8091284d933cac8 | deep | arXiv:2605.20744v1 | SRC-ARXIV@arXiv:2605.20744v1 | arXiv:2605.20744v1 HTML — §3 Hack-Verifiable Environment Construction | arXiv:2605.20744v1 HTML — §5 Evaluation | arXiv:2605.20744v1 HTML — §7 Limitations and Future Work | https://arxiv.org/html/2605.20744v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20744 | complete |
| SF-2026-ARXIV-2605-20749 | RP-59f2f20578298545 | deep | arXiv:2605.20749v1 | SRC-ARXIV@arXiv:2605.20749v1 | arXiv:2605.20749v1 HTML — §4 Training Dynamics in the Kernel Regime: From NTK Spectrum to Loss Crossing | arXiv:2605.20749v1 HTML — §3.3 Experimental Verification; §5 Generalization Gap Analysis; §Appendix C Proof of Loss Crossing Results | arXiv:2605.20749v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20749v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20749 | complete |
| SF-2026-ARXIV-2605-20752 | RP-a801055f54dc9022 | deep | arXiv:2605.20752v1 | SRC-ARXIV@arXiv:2605.20752v1 | arXiv:2605.20752v1 HTML — §3 Method; §3.4 GaussianDream Training and Efficient Inference; §Stage I: GaussianDream pretraining. | arXiv:2605.20752v1 HTML — §4 Experiments; §4.1 Experimental Setup; §Simulation benchmarks. | arXiv:2605.20752v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.20752v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20752 | complete |
| SF-2026-ARXIV-2605-20756 | RP-29baa519fa9f5341 | deep | arXiv:2605.20756v1 | SRC-ARXIV@arXiv:2605.20756v1 | arXiv:2605.20756v1 HTML — §5 Proposed method; §7.1 Main pretraining results; §Appendix A Algorithm and instantiations | arXiv:2605.20756v1 HTML — §6 Convergence analysis; §7 Experiments; §7.1 Main pretraining results | arXiv:2605.20756v1 HTML — §8 Limitations; §9 Conclusion; §Appendix C Discussion | https://arxiv.org/html/2605.20756v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20756 | complete |
| SF-2026-ARXIV-2605-20767 | RP-894e00dbb265731a | deep | arXiv:2605.20767v1 | SRC-ARXIV@arXiv:2605.20767v1 | arXiv:2605.20767v1 HTML — §3 Causal Estimands for LLM-Simulated Interventions | arXiv:2605.20767v1 HTML — §4 Experiments | arXiv:2605.20767v1 HTML — §6 Discussion and observational-study boundary | https://arxiv.org/html/2605.20767v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20767 | complete |
| SF-2026-ARXIV-2605-20774 | RP-0fb828e6d2ddf085 | deep | arXiv:2605.20774v1 | SRC-ARXIV@arXiv:2605.20774v1 | arXiv:2605.20774v1 HTML — §4.1 Algorithms; §Appendix F Training Details | arXiv:2605.20774v1 HTML — §VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models; §3 The VLA-Replica Benchmark; §3.3 Task Suite and Evaluation Protocols | arXiv:2605.20774v1 HTML — §5 Conclusion &amp; Limitation | https://arxiv.org/html/2605.20774v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20774 | complete |
| SF-2026-ARXIV-2605-20798 | RP-9c7d4707084b18af | deep | arXiv:2605.20798v1 | SRC-ARXIV@arXiv:2605.20798v1 | arXiv:2605.20798v1 HTML — §3 Experimental Methodology; §3.1 Methods and taxonomy; §3.2 Training setup | arXiv:2605.20798v1 HTML — §Most Transformer Modifications Still Do Not Transfer at 1–3B: A 2020–2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor; §3 Experimental Methodology; §3.4 Downstream evaluation suite | arXiv:2605.20798v1 HTML — §6 Discussion; §Limitations | https://arxiv.org/html/2605.20798v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20798 | complete |
| SF-2026-ARXIV-2605-20799 | RP-85d10d3ebe77180b | deep | arXiv:2605.20799v1 | SRC-ARXIV@arXiv:2605.20799v1 | arXiv:2605.20799v1 HTML — §III Overall FLOP Utilization | arXiv:2605.20799v1 HTML — §IV Validation | arXiv:2605.20799v1 HTML — §VI Conclusion and approximation boundary | https://arxiv.org/html/2605.20799v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20799 | complete |
| SF-2026-ARXIV-2605-20833 | RP-142bc0331b3a89e7 | deep | arXiv:2605.20833v1 | SRC-ARXIV@arXiv:2605.20833v1 | arXiv:2605.20833v1 HTML — §3 MemGym : A Memory-Centric Evaluation and Training Framework; §B.1 Agentic Memory Systems (Detailed); §Appendix H MemRM Training Details | arXiv:2605.20833v1 HTML — §3 MemGym : A Memory-Centric Evaluation and Training Framework; §3.3 MemRM as a Lightweight Evaluation Signal; §3.4 Constructed Pipelines for Memory-Grounded Evaluation | arXiv:2605.20833v1 HTML — §5 Conclusion; §Appendix J Discussion, Limitations, and Future Work; §J.1 Discussion | https://arxiv.org/html/2605.20833v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20833 | complete |
| SF-2026-ARXIV-2605-20834 | RP-c390e25cda3f4306 | deep | arXiv:2605.20834v1 | SRC-ARXIV@arXiv:2605.20834v1 | arXiv:2605.20834v1 HTML — §3 Conditional Equivalence and Failure Modes | arXiv:2605.20834v1 HTML — §5 Experiments | arXiv:2605.20834v1 HTML — §6 Conclusion and disclosed assumptions | https://arxiv.org/html/2605.20834v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20834 | complete |
| SF-2026-ARXIV-2605-20863 | RP-8d1b66a79597c3af | deep | arXiv:2605.20863v1 | SRC-ARXIV@arXiv:2605.20863v1 | arXiv:2605.20863v1 HTML — §3 PlexRL Cluster-Level Orchestration | arXiv:2605.20863v1 HTML — §5 Evaluation | arXiv:2605.20863v1 HTML — §6 Conclusion and cluster/workload boundary | https://arxiv.org/html/2605.20863v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20863 | complete |
| SF-2026-ARXIV-2605-20866 | RP-731e444e92f13f54 | deep | arXiv:2605.20866v1 | SRC-ARXIV@arXiv:2605.20866v1 | arXiv:2605.20866v1 HTML — §Local training; §Asynchronous methods | arXiv:2605.20866v1 HTML — §5 Experiments; §Appendix B Additional Experimental Details; §Experimental organization. | arXiv:2605.20866v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20866v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20866 | complete |
| SF-2026-ARXIV-2605-20868 | RP-e386899285ccd4ec | deep | arXiv:2605.20868v1 | SRC-ARXIV@arXiv:2605.20868v1 | arXiv:2605.20868v1 HTML — §4 Tiered Runtime-Certified Attention | arXiv:2605.20868v1 HTML — §9 Evaluation | arXiv:2605.20868v1 HTML — §11 Limitations | https://arxiv.org/html/2605.20868v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20868 | complete |
| SF-2026-ARXIV-2605-20874 | RP-948a3e279b479e94 | deep | arXiv:2605.20874v1 | SRC-ARXIV@arXiv:2605.20874v1 | arXiv:2605.20874v1 HTML — §3 Policy-as-Code Architecture | arXiv:2605.20874v1 HTML — §4 Demonstration and Evaluation | arXiv:2605.20874v1 HTML — §5 Conclusion and demo-scope boundary | https://arxiv.org/html/2605.20874v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20874 | complete |
| SF-2026-ARXIV-2605-20876 | RP-f12cb7661d1fe76f | deep | arXiv:2605.20876v1 | SRC-ARXIV@arXiv:2605.20876v1 | arXiv:2605.20876v1 HTML — §B.4 Training Compute Details Back to ToC | arXiv:2605.20876v1 HTML — §4 Experiments; §4.1 Experiment Setting; §Benchmarks | arXiv:2605.20876v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.20876v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20876 | complete |
| SF-2026-ARXIV-2605-20923 | RP-588d7d56bc9ab8a8 | deep | arXiv:2605.20923v1 | SRC-ARXIV@arXiv:2605.20923v1 | arXiv:2605.20923v1 HTML — §3 Causal Past Logic | arXiv:2605.20923v1 HTML — §5 Runtime Verification Evaluation | arXiv:2605.20923v1 HTML — §6 Conclusion and workflow-model boundary | https://arxiv.org/html/2605.20923v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20923 | complete |
| SF-2026-ARXIV-2605-20926 | RP-1decbb1055250791 | deep | arXiv:2605.20926v1 | SRC-ARXIV@arXiv:2605.20926v1 | arXiv:2605.20926v1 HTML — §3 MemConflict Framework | arXiv:2605.20926v1 HTML — §4 Experiments | arXiv:2605.20926v1 HTML — §5 Conclusion and benchmark limits | https://arxiv.org/html/2605.20926v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20926 | complete |
| SF-2026-ARXIV-2605-20948 | RP-ee1583478455dd4b | deep | arXiv:2605.20948v1 | SRC-ARXIV@arXiv:2605.20948v1 | arXiv:2605.20948v1 HTML — §Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory; §3 Method; §A.1 Model Architecture and Hyper Parameters | arXiv:2605.20948v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.20948v1 HTML — §5 Conclusion; §Appendix C Limitations & Discussion; §C.1 Limitations | https://arxiv.org/html/2605.20948v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20948 | complete |
| SF-2026-ARXIV-2605-21061 | RP-8ad11b566b9045d4 | deep | arXiv:2605.21061v1 | SRC-ARXIV@arXiv:2605.21061v1 | arXiv:2605.21061v1 HTML — §2.2 Phenomena due to Formulation of Existing VLA; §3 Methods; §Appendix B Architecture Details | arXiv:2605.21061v1 HTML — §4 Experiments; §4.2 Main Experiments; §4.2.1 Experiments on NAVSIM. | arXiv:2605.21061v1 HTML — §5 Conclusion; §Appendix O Limitations and future work. | https://arxiv.org/html/2605.21061v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21061 | complete |
| SF-2026-ARXIV-2605-21100 | RP-7029228c2d8b1821 | deep | arXiv:2605.21100v1 | SRC-ARXIV@arXiv:2605.21100v1 | arXiv:2605.21100v1 HTML — §3 NanoCP Request-Level Context Parallelism | arXiv:2605.21100v1 HTML — §5 Evaluation | arXiv:2605.21100v1 HTML — §6 Conclusion and topology boundary | https://arxiv.org/html/2605.21100v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21100 | complete |
| SF-2026-ARXIV-2605-21103 | RP-005add45222d65d1 | deep | arXiv:2605.21103v1 | SRC-ARXIV@arXiv:2605.21103v1 | arXiv:2605.21103v1 HTML — §2 Typed Tensor Language; §3 Shared-State Factorization | arXiv:2605.21103v1 HTML — §4 Differentiable Programs; §5 Discussion | arXiv:2605.21103v1 HTML — §5 Discussion — formal one-round/shared-state scope | https://arxiv.org/html/2605.21103v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21103 | complete |
| SF-2026-ARXIV-2605-21125 | RP-1567e1e42b8c52ff | deep | arXiv:2605.21125v1 | SRC-ARXIV@arXiv:2605.21125v1 | arXiv:2605.21125v1 HTML — §3 Advantage-Collapse Diagnosis; §4 Mitigation | arXiv:2605.21125v1 HTML — §5 Experiments | arXiv:2605.21125v1 HTML — §6 Conclusion and GRPO-scope boundary | https://arxiv.org/html/2605.21125v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21125 | complete |
| SF-2026-ARXIV-2605-21127 | RP-f87e14d248f9adf4 | deep | arXiv:2605.21127v1 | SRC-ARXIV@arXiv:2605.21127v1 | arXiv:2605.21127v1 HTML — §Tools and frameworks for reasoning models.; §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework. | arXiv:2605.21127v1 HTML — §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.; §4 ThinkPack : Operationalising Structural Reasoning Evaluation | arXiv:2605.21127v1 HTML — §6 Discussion; §7 Limitations; §8 Conclusion | https://arxiv.org/html/2605.21127v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21127 | complete |
| SF-2026-ARXIV-2605-21177 | RP-88ef212b118ef706 | deep | arXiv:2605.21177v1 | SRC-ARXIV@arXiv:2605.21177v1 | arXiv:2605.21177v1 HTML — §3 Method; §3.1 Algorithm Description | arXiv:2605.21177v1 HTML — §Convergence result.; §3.2 BP Time Analysis; §3.3 Memory Consumption Analysis | arXiv:2605.21177v1 HTML — §5 Conclusion; §Appendix H Limitations | https://arxiv.org/html/2605.21177v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21177 | complete |
| SF-2026-ARXIV-2605-21187 | RP-a52f46fbbc594594 | deep | arXiv:2605.21187v1 | SRC-ARXIV@arXiv:2605.21187v1 | arXiv:2605.21187v1 HTML — §III Spectrum-X Multiplane Architecture | arXiv:2605.21187v1 HTML — §IV Evaluation | arXiv:2605.21187v1 HTML — §V Deployment Evidence; §VI Conclusion | https://arxiv.org/html/2605.21187v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21187 | complete |
| SF-2026-ARXIV-2605-21266 | RP-983345b4bc381b18 | deep | arXiv:2605.21266v1 | SRC-ARXIV@arXiv:2605.21266v1 | arXiv:2605.21266v1 HTML — §Iterative and hybrid methods. | arXiv:2605.21266v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.21266v1 HTML — §6 Conclusion; §Appendix B Discussion; §Limitations. | https://arxiv.org/html/2605.21266v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21266 | complete |
| SF-2026-ARXIV-2605-21273 | RP-64ba1d8270158172 | deep | arXiv:2605.21273v1 | SRC-ARXIV@arXiv:2605.21273v1 | arXiv:2605.21273v1 HTML — §3.3 Action-Centric Supervised Training; §Driving Action Alignment Pretraining.; §4.5 Ablation Study of Training Strategy | arXiv:2605.21273v1 HTML — §4 Experiments; §4.1 Experiments Setup; §4.2 Main Results | arXiv:2605.21273v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.21273v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21273 | complete |
| SF-2026-ARXIV-2605-21312 | RP-c21af2f613607f73 | deep | arXiv:2605.21312v1 | SRC-ARXIV@arXiv:2605.21312v1 | arXiv:2605.21312v1 HTML — §3 Frontier Simulator Architecture | arXiv:2605.21312v1 HTML — §5 Fidelity Evaluation | arXiv:2605.21312v1 HTML — §6 Workload Studies; §7 Conclusion | https://arxiv.org/html/2605.21312v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21312 | complete |
| SF-2026-ARXIV-2605-21347 | RP-980999ab4adc0664 | deep | arXiv:2605.21347v1 | SRC-ARXIV@arXiv:2605.21347v1 | arXiv:2605.21347v1 HTML — §Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents; §3.1 System Overview; §A.1 Agent System Prompts | arXiv:2605.21347v1 HTML — §3.6 Iterative Analysis Loop; §4 Evaluation; §A.4 Benchmark and Corpus Statistics | arXiv:2605.21347v1 HTML — §5 Discussion; §5.3 Limitations and Future Work; §6 Conclusion | https://arxiv.org/html/2605.21347v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21347 | complete |
| SF-2026-ARXIV-2605-21384 | RP-bb3f6e4ebda9502c | deep | arXiv:2605.21384v1 | SRC-ARXIV@arXiv:2605.21384v1 | arXiv:2605.21384v1 HTML — §2 Benchmark Design | arXiv:2605.21384v1 HTML — §3 Experiments; §4 Analysis | arXiv:2605.21384v1 HTML — §Appendix A Limitations and Broader Impacts | https://arxiv.org/html/2605.21384v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21384 | complete |
| SF-2026-ARXIV-2605-21392 | RP-3f08b3a9c49df6c5 | deep | arXiv:2605.21392v1 | SRC-ARXIV@arXiv:2605.21392v1 | arXiv:2605.21392v1 HTML — §III VIPER-MCP Taint Analysis | arXiv:2605.21392v1 HTML — §V Evaluation | arXiv:2605.21392v1 HTML — §VII Conclusion; Limitations and Future Work | https://arxiv.org/html/2605.21392v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21392 | complete |
| SF-2026-ARXIV-2605-21427 | RP-ceb8743093ad6661 | deep | arXiv:2605.21427v1 | SRC-ARXIV@arXiv:2605.21427v1 | arXiv:2605.21427v1 HTML — §3 PALS Joint Power/Batch Controller | arXiv:2605.21427v1 HTML — §7 Evaluation | arXiv:2605.21427v1 HTML — §8 Conclusion and GPU/MoE scope | https://arxiv.org/html/2605.21427v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21427 | complete |
| SF-2026-ARXIV-2605-21434 | RP-22dd6d5d62eb118c | deep | arXiv:2605.21434v1 | SRC-ARXIV@arXiv:2605.21434v1 | arXiv:2605.21434v1 HTML — §3 Agent-Propose/Solver-Verify Workflow | arXiv:2605.21434v1 HTML — §5 Evaluation | arXiv:2605.21434v1 HTML — §6 Limitations and bounded-model-checking scope | https://arxiv.org/html/2605.21434v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21434 | complete |
| SF-2026-ARXIV-2605-21446 | RP-d4c180075d355865 | deep | arXiv:2605.21446v1 | SRC-ARXIV@arXiv:2605.21446v1 | arXiv:2605.21446v1 HTML — §3 Controlled Sensor-Perturbation Protocol | arXiv:2605.21446v1 HTML — §4 Experiments | arXiv:2605.21446v1 HTML — §5.1 Limitations | https://arxiv.org/html/2605.21446v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21446 | complete |
| SF-2026-ARXIV-2605-21467 | RP-4c1411d1f5ac5be2 | deep | arXiv:2605.21467v1 | SRC-ARXIV@arXiv:2605.21467v1 | arXiv:2605.21467v1 HTML — §3 Method; §4.3 Training Dynamics; §Use in training. | arXiv:2605.21467v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.21467v1 HTML — §7 Conclusion; §Appendix A Limitations | https://arxiv.org/html/2605.21467v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21467 | complete |
| SF-2026-ARXIV-2605-21468 | RP-d5257297c7654d44 | deep | arXiv:2605.21468v1 | SRC-ARXIV@arXiv:2605.21468v1 | arXiv:2605.21468v1 HTML — §You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories; §3 Method; §Zero training cost. | arXiv:2605.21468v1 HTML — §4 Experiments; §4.1 Experimental Setup; §RLVR training and evaluation. | arXiv:2605.21468v1 HTML — §6 Discussion; §Limitations.; §7 Conclusion | https://arxiv.org/html/2605.21468v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21468 | complete |
| SF-2026-ARXIV-2605-21470 | RP-e8b83a8a4d5c6742 | deep | arXiv:2605.21470v1 | SRC-ARXIV@arXiv:2605.21470v1 | arXiv:2605.21470v1 HTML — §3 Methods | arXiv:2605.21470v1 HTML — §4 Evaluation; §5 Results | arXiv:2605.21470v1 HTML — §6 Limitations | https://arxiv.org/html/2605.21470v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21470 | complete |
| SF-2026-ARXIV-2605-21482 | RP-7c53f8d7522ea5e7 | deep | arXiv:2605.21482v1 | SRC-ARXIV@arXiv:2605.21482v1 | arXiv:2605.21482v1 HTML — §3 DeepWeb-Bench; §3.4 Evaluation Protocol | arXiv:2605.21482v1 HTML — §4 Experiments | arXiv:2605.21482v1 HTML — §Appendix K Limitations | https://arxiv.org/html/2605.21482v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21482 | complete |
| SF-2026-ARXIV-2605-21486 | RP-2f0e0464ce5e4c03 | deep | arXiv:2605.21486v1 | SRC-ARXIV@arXiv:2605.21486v1 | arXiv:2605.21486v1 HTML — §4.1 Methodology; §6 The Effect of Weight Decay and Compute Optimal Training; §H.2 Model Architecture | arXiv:2605.21486v1 HTML — §Appendix A Experimental Details; §H.3 Design Principles for Scaling Analysis | arXiv:2605.21486v1 HTML — §8 Discussion and Conclusion | https://arxiv.org/html/2605.21486v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21486 | complete |
| SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | RP-485a69982ea745ae | deep | arXiv:2605.20223v1 | SRC-ARXIV@arXiv:2605.20223v1 | arXiv:2605.20223v1 HTML — §Method / System Design — Why Latent Actions Fail, and How to Prevent It 的机制、状态 owner 与控制/数据流 | arXiv:2605.20223v1 HTML — §Experiments / Evaluation — Why Latent Actions Fail, and How to Prevent It 的作者披露 workload、baseline 与 ablation | arXiv:2605.20223v1 HTML — §Limitations / Discussion — Why Latent Actions Fail, and How to Prevent It 的适用范围、未证明项与 failure boundary | arXiv:2605.20223v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-20196:start -->
#### Data Scaling as Progressive Coverage of a Predictive Contribution Spectrum

<!-- claim:SF-2026-ARXIV-2605-20196:start -->
- **Problem:** We investigate the hypothesis that real-data scaling laws are governed by progressive coverage of a latent predictive contribution spectrum rather than by token-frequency tails alone.
- **Old path / changed constraint:** 经验 scaling law 描述损失随数据量下降的斜率，却不解释为什么不同语料具有不同指数；token-frequency tail 只度量出现频率，不能区分某个上下文状态对 next-token prediction 的贡献。
- **Mechanism / ownership:** 论文以 suffix-automaton state 构造 predictive-contribution spectrum：每个状态的 global-KL contribution 等于经验状态质量乘以其相对全局 next-token baseline 的 KL 偏离；再定义有效截断秩 K(N)，令 spectrum residual tail 与模型 excess loss 对齐，用它描述数据量增加时逐步覆盖的预测贡献。
- **Evaluation contract:** 实验在 12 个真实语料上训练固定的小型 GPT learner，比较 spectrum tail slope 与经验 data-scaling exponent，并报告 log K 对 log N 的 pooled R² 约 0.96（raw）和 0.90（smoothed）。未验证 frontier model、不同架构或 causal intervention。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 该解释需要构造语料状态空间，结果依赖 suffix/state 表示与合并策略；论文中的 quotient/merged construction 解释力更弱，说明压缩可能删除有用的细粒度信息。当前证据是固定小模型上的相关性，不能证明 K(N) 是模型真实学习状态，也不能把相关斜率当作跨架构的因果 scaling law。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.20196v1](https://arxiv.org/abs/2605.20196v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.20196v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-20196:end -->
<!-- review:SF-2026-ARXIV-2605-20196:end -->

<!-- review:SF-2026-ARXIV-2605-20251:start -->
#### ProcCtrlBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents

**问题与机制。** We present ProcCtrlBench, a benchmark for execution-process evaluation in LLM coding agents. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.5 trajectory/control contract`；Evaluation=`§4.1–4.5 experiments`；Limitations/Counterevidence=`§5 Limitations and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20251:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-20251:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-20251:end -->

<!-- review:SF-2026-ARXIV-2605-20270:start -->
#### Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs

**问题与机制。** Using a (test statistic, validity guarantee, deployment rule) framework, we identify one empty cell forced by deployment requirements: e-process per threshold, selective risk, anytime-pathwise validity, max-certified-threshold rule. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§1–§4 deployment contract and e-process`；Evaluation=`§5–§7 proofs and 650-stream evaluation`；Limitations/Counterevidence=`§8 limitations and boundary`。

<!-- claim:SF-2026-ARXIV-2605-20270:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-20270:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-20270:end -->

<!-- review:SF-2026-ARXIV-2605-20295:start -->
#### Quant.npu: Enabling Efficient Mobile NPU Inference for on-device LLMs via Fully Static Quantization

**问题与机制。** To bridge the gap between high-fidelity PTQ and NPU-constrained inference, we propose Quant.npu, a integer-only fully static quantization framework. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§4 fully static NPU quantization`；Evaluation=`§5 on-device NPU evaluation`；Limitations/Counterevidence=`Appendix H Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20295:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20295:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20295:end -->

<!-- review:SF-2026-ARXIV-2605-20296:start -->
#### Spectral Unforgetting: Post-Hoc Recovery of Damaged Capabilities Without Retraining

**问题与机制。** We study this phenomenon, known as catastrophic forgetting, and propose a post-hoc repair solution that uses only the pretrained checkpoint $W_{\mathrm{base}}$ and its fine-tuned descendant $W_{\mathrm{ft}}$. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 checkpoint-delta spectral repair`；Evaluation=`§4 fourteen-cell recovery/preservation evaluation`；Limitations/Counterevidence=`§5 Limitations and conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20296:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20296:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20296:end -->

<!-- review:SF-2026-ARXIV-2605-20312:start -->
#### Pramana: A Protocol-Layer Treatment of Claim Verification in Autonomous Agent Networks

**问题与机制。** Autonomous agents deployed in regulated domains must produce a verification artifact per consequential output: a record an auditor can re-execute offline, capturing what was claimed, against what source, by whom, when, and how. 系统 owner=`AGENT-MCP`。

**Exact-v1。** Method=`§2 claim primitives; §3 protocol composition`；Evaluation=`§5 pilot; §6 formal properties`；Limitations/Counterevidence=`§8 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20312:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20312:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20312:end -->

<!-- review:SF-2026-ARXIV-2605-20314:start -->
#### Less Data, Faster Training: repeating smaller datasets speeds up learning via sampling biases

**问题与机制。** We argue that the speedup comes from appropriate layer-wise growth enabled by sampling biases, which is more pronounced when the dataset size is smaller. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§2 reuse setup; §3–§5 sampling-bias and relative-norm mechanism`；Evaluation=`§5 empirical interventions; Appendix B`；Limitations/Counterevidence=`§6 discussion: when data repetition is and is not helpful`。

<!-- claim:SF-2026-ARXIV-2605-20314:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20314:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20314:end -->

<!-- review:SF-2026-ARXIV-2605-20315:start -->
#### Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs

**问题与机制。** However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference. 系统 owner=`INFER-PD-DISAGGREGATION`。

**Exact-v1。** Method=`§3 quantized-prefill/precise-decode split`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5 Conclusion and hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-20315:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20315:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20315:end -->

<!-- review:SF-2026-ARXIV-2605-20402:start -->
#### Decomposing MXFP4 quantization error for LLM reinforcement learning: reducible bias, recoverable deadzone, and an irreducible floor

**问题与机制。** We prove an exact three-way decomposition of quantization error and show how each component dominates a distinct RL training pathway. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§5 MXFP4 error decomposition`；Evaluation=`§6 RL quantization experiments`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20402:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20402:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20402:end -->

<!-- review:SF-2026-ARXIV-2605-20477:start -->
#### Training Language Agents to Learn from Experience

**问题与机制。** We then propose an RL-based training pipeline for learning such reflections directly from experience, without human-provided examples. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3–§4 reflection-learning pipeline`；Evaluation=`§5 MiniHack/ALFWorld evaluation`；Limitations/Counterevidence=`§5.3 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20477:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20477:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20477:end -->

<!-- review:SF-2026-ARXIV-2605-20485:start -->
#### ZEBRA: Zero-shot Budgeted Resource Allocation for LLM Orchestration

**问题与机制。** We propose ZEBRA, a zero-shot framework that reduces multi-phase budget allocation to a continuous nonlinear knapsack problem: an LLM controller estimates per-phase utility curves, and a water-filling search on the Lagrange multiplier returns the per-phase split. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3 budgeted model-orchestration policy`；Evaluation=`§4–§5 zero-shot allocation evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20485:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20485:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20485:end -->

<!-- review:SF-2026-ARXIV-2605-20490:start -->
#### ECUAS$_n$: A family of metrics for principled evaluation of uncertainty-augmented systems

**问题与机制。** We argue that these evaluation approaches are inadequate for assessing overall performance of the UA system for decision making under uncertainty and propose a novel family of metrics, ECUAS$_n$, formulated as proper scoring rules for the task of interest. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 ECUAS decision-theoretic metric family`；Evaluation=`§4 evaluator and QA studies`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: equivalence evaluator and utility assumptions`。

<!-- claim:SF-2026-ARXIV-2605-20490:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20490:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20490:end -->

<!-- review:SF-2026-ARXIV-2605-20520:start -->
#### Open-World Evaluations for Measuring Frontier AI Capabilities

**问题与机制。** In this paper we survey recent open-world evaluations, identify their strengths and limitations, and introduce CRUX (Collaborative Research for Updating AI eXpectations), a project for conducting such evaluations regularly. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 open-world evaluation framework`；Evaluation=`§3 case studies and capability evidence`；Limitations/Counterevidence=`§2.4 Limitations: complements, not replaces, benchmarks`。

<!-- claim:SF-2026-ARXIV-2605-20520:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20520:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20520:end -->

<!-- review:SF-2026-ARXIV-2605-20544:start -->
#### The Yes-Man Syndrome: Benchmarking Abstention in Embodied Robotic Agents

**问题与机制。** To address this gap, we introduce a taxonomy to categorize abstention in the context of embodied robotics and present RoboAbstention, a scalable and auditable framework for generating abstention instructions grounded in images gathered from five robotics datasets. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 grounded abstention taxonomy and deterministic constraint pipeline`；Evaluation=`§4 6,069-instruction embodied VLM evaluation`；Limitations/Counterevidence=`§5 Discussion; guarantees remain conditional on scene extraction`。

<!-- claim:SF-2026-ARXIV-2605-20544:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20544:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20544:end -->

<!-- review:SF-2026-ARXIV-2605-20548:start -->
#### What Do Agents Communicate? Characterizing Information Exchange in Multi-Agent Systems

**问题与机制。** To address this, we conduct a systematic analysis of inter-agent communication to identify which information drives MA performance. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3–§4 communication-content instrumentation`；Evaluation=`§5 and Appendix C.2 occlusion evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20548:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20548:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20548:end -->

<!-- review:SF-2026-ARXIV-2605-20563:start -->
#### Multi-agent Collaboration with State Management

**问题与机制。** In this paper, we propose STORM, i.e., STate-ORiented Management for multi-agent collaboration. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3–§4 state-management and annotation protocol`；Evaluation=`§5 evaluation; Appendix A setup`；Limitations/Counterevidence=`Appendix E Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20563:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20563:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20563:end -->

<!-- review:SF-2026-ARXIV-2605-20616:start -->
#### Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents

**问题与机制。** Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§4 Offline Memory Consolidation`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20616:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20616:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20616:end -->

<!-- review:SF-2026-ARXIV-2605-20630:start -->
#### Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines

**问题与机制。** We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Optimization Framework`；Evaluation=`§4 Results`；Limitations/Counterevidence=`§5 Limitations and Failure Modes`。

<!-- claim:SF-2026-ARXIV-2605-20630:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20630:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20630:end -->

<!-- review:SF-2026-ARXIV-2605-20641:start -->
#### Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs

**问题与机制。** We propose a unified optimization-triggered attack framework comprising two complementary strategies. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Optimization-Triggered Attack Design`；Evaluation=`§4 Implementation and Evaluation`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20641:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20641:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20641:end -->

<!-- review:SF-2026-ARXIV-2605-20696:start -->
#### Distributed Direct Preference Optimization

**问题与机制。** For federated DPO, we derive convergence rates that quantify the impact of client drift, communication frequency, and preference heterogeneity; for decentralized DPO, we establish convergence over general communication graphs and show how spectral connectivity governs optimization speed and consensus. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§3 Problem Formulation and Preliminaries`；Evaluation=`§7 Numerical Results; §Appendix E Additional Detail for Experimental Setup; §Appendix F Additional Results`；Limitations/Counterevidence=`§8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20696:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20696:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20696:end -->

<!-- review:SF-2026-ARXIV-2605-20704:start -->
#### Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms

**问题与机制。** We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§4.1–§4.6 Heartbeat-Bound Credential Protocol`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20704:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20704:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20704:end -->

<!-- review:SF-2026-ARXIV-2605-20706:start -->
#### Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU

**问题与机制。** To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 LlamaWeb Architecture`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Discussion and WebGPU portability boundary`。

<!-- claim:SF-2026-ARXIV-2605-20706:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20706:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20706:end -->

<!-- review:SF-2026-ARXIV-2605-20734:start -->
#### An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress

**问题与机制。** A large language model (LLM) agent that sends messages can leak data inside them. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 Multi-Modal Reference Monitor`；Evaluation=`§7 Evaluation`；Limitations/Counterevidence=`§8 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20734:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20734:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20734:end -->

<!-- review:SF-2026-ARXIV-2605-20744:start -->
#### Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale

**问题与机制。** In this work, we introduce a new evaluation paradigm for measuring reward hacking. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Hack-Verifiable Environment Construction`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§7 Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20744:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20744:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20744:end -->

<!-- review:SF-2026-ARXIV-2605-20749:start -->
#### The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?

**问题与机制。** In this work, we study GLU by analyzing two-layer networks in the neural tangent kernel (NTK) regime. 系统 owner=`MODEL-FFN`。

**Exact-v1。** Method=`§4 Training Dynamics in the Kernel Regime: From NTK Spectrum to Loss Crossing`；Evaluation=`§3.3 Experimental Verification; §5 Generalization Gap Analysis; §Appendix C Proof of Loss Crossing Results`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20749:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20749:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20749:end -->

<!-- review:SF-2026-ARXIV-2605-20752:start -->
#### GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation

**问题与机制。** To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 Method; §3.4 GaussianDream Training and Efficient Inference; §Stage I: GaussianDream pretraining.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §Simulation benchmarks.`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20752:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20752:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20752:end -->

<!-- review:SF-2026-ARXIV-2605-20756:start -->
#### Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers

**问题与机制。** We show that this view misses two finite-sample biases. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§5 Proposed method; §7.1 Main pretraining results; §Appendix A Algorithm and instantiations`；Evaluation=`§6 Convergence analysis; §7 Experiments; §7.1 Main pretraining results`；Limitations/Counterevidence=`§8 Limitations; §9 Conclusion; §Appendix C Discussion`。

<!-- claim:SF-2026-ARXIV-2605-20756:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20756:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20756:end -->

<!-- review:SF-2026-ARXIV-2605-20767:start -->
#### The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study

**问题与机制。** Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Causal Estimands for LLM-Simulated Interventions`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Discussion and observational-study boundary`。

<!-- claim:SF-2026-ARXIV-2605-20767:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20767:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20767:end -->

<!-- review:SF-2026-ARXIV-2605-20774:start -->
#### VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models

**问题与机制。** We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§4.1 Algorithms; §Appendix F Training Details`；Evaluation=`§VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models; §3 The VLA-Replica Benchmark; §3.3 Task Suite and Evaluation Protocols`；Limitations/Counterevidence=`§5 Conclusion &amp; Limitation`。

<!-- claim:SF-2026-ARXIV-2605-20774:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20774:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20774:end -->

<!-- review:SF-2026-ARXIV-2605-20798:start -->
#### Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor

**问题与机制。** Narang et al. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Experimental Methodology; §3.1 Methods and taxonomy; §3.2 Training setup`；Evaluation=`§Most Transformer Modifications Still Do Not Transfer at 1–3B: A 2020–2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor; §3 Experimental Methodology; §3.4 Downstream evaluation suite`；Limitations/Counterevidence=`§6 Discussion; §Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20798:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20798:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20798:end -->

<!-- review:SF-2026-ARXIV-2605-20799:start -->
#### Instant GPU Efficiency Visibility at Fleet Scale

**问题与机制。** We present Overall FLOP Utilization (OFU), a hardware-level, precision-agnostic GPU efficiency metric for AI workloads on HPC systems, derived from two on-chip performance counters: Tensor Pipe Activity and SM clock frequency. 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1。** Method=`§III Overall FLOP Utilization`；Evaluation=`§IV Validation`；Limitations/Counterevidence=`§VI Conclusion and approximation boundary`。

<!-- claim:SF-2026-ARXIV-2605-20799:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20799:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20799:end -->

<!-- review:SF-2026-ARXIV-2605-20833:start -->
#### MemGym: a Long-Horizon Memory Environment for LLM Agents

**问题与机制。** We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 MemGym : A Memory-Centric Evaluation and Training Framework; §B.1 Agentic Memory Systems (Detailed); §Appendix H MemRM Training Details`；Evaluation=`§3 MemGym : A Memory-Centric Evaluation and Training Framework; §3.3 MemRM as a Lightweight Evaluation Signal; §3.4 Constructed Pipelines for Memory-Grounded Evaluation`；Limitations/Counterevidence=`§5 Conclusion; §Appendix J Discussion, Limitations, and Future Work; §J.1 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-20833:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20833:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20833:end -->

<!-- review:SF-2026-ARXIV-2605-20834:start -->
#### Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment

**问题与机制。** We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§3 Conditional Equivalence and Failure Modes`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and disclosed assumptions`。

<!-- claim:SF-2026-ARXIV-2605-20834:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20834:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20834:end -->

<!-- review:SF-2026-ARXIV-2605-20863:start -->
#### PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR

**问题与机制。** However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 PlexRL Cluster-Level Orchestration`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Conclusion and cluster/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-20863:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20863:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20863:end -->

<!-- review:SF-2026-ARXIV-2605-20866:start -->
#### LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging

**问题与机制。** We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§Local training; §Asynchronous methods`；Evaluation=`§5 Experiments; §Appendix B Additional Experimental Details; §Experimental organization.`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20866:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20866:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20866:end -->

<!-- review:SF-2026-ARXIV-2605-20868:start -->
#### Runtime-Certified Bounded-Error Quantized Attention

**问题与机制。** We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§4 Tiered Runtime-Certified Attention`；Evaluation=`§9 Evaluation`；Limitations/Counterevidence=`§11 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20868:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20868:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20868:end -->

<!-- review:SF-2026-ARXIV-2605-20874:start -->
#### Governance by Construction for Generalist Agents

**问题与机制。** We present a runtime governance architecture that enforces policy interventions at every critical stage of execution. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Policy-as-Code Architecture`；Evaluation=`§4 Demonstration and Evaluation`；Limitations/Counterevidence=`§5 Conclusion and demo-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-20874:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20874:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20874:end -->

<!-- review:SF-2026-ARXIV-2605-20876:start -->
#### Terminal-World: Scaling Terminal-Agent Environments via Agent Skills

**问题与机制。** To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§B.4 Training Compute Details Back to ToC`；Evaluation=`§4 Experiments; §4.1 Experiment Setting; §Benchmarks`；Limitations/Counterevidence=`§6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20876:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20876:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20876:end -->

<!-- review:SF-2026-ARXIV-2605-20923:start -->
#### Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows

**问题与机制。** Distributed LLM agent workflows should not be monitored as if they produced a single sequential log. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Causal Past Logic`；Evaluation=`§5 Runtime Verification Evaluation`；Limitations/Counterevidence=`§6 Conclusion and workflow-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-20923:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20923:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20923:end -->

<!-- review:SF-2026-ARXIV-2605-20926:start -->
#### MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts

**问题与机制。** To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 MemConflict Framework`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5 Conclusion and benchmark limits`。

<!-- claim:SF-2026-ARXIV-2605-20926:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20926:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20926:end -->

<!-- review:SF-2026-ARXIV-2605-20948:start -->
#### Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory

**问题与机制。** We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory. 系统 owner=`MODEL-MOE`。

**Exact-v1。** Method=`§Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory; §3 Method; §A.1 Model Architecture and Hyper Parameters`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion; §Appendix C Limitations & Discussion; §C.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20948:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20948:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20948:end -->

<!-- review:SF-2026-ARXIV-2605-21061:start -->
#### Grounding Driving VLA via Inverse Kinematics

**问题与机制。** We show that trajectory recovery, when viewed through the lens of inverse kinematics, requires both a current and a future visual state as boundary conditions; existing VLAs supply only the former, which encourages the model to shortcut through ego status and text commands alone. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§2.2 Phenomena due to Formulation of Existing VLA; §3 Methods; §Appendix B Architecture Details`；Evaluation=`§4 Experiments; §4.2 Main Experiments; §4.2.1 Experiments on NAVSIM.`；Limitations/Counterevidence=`§5 Conclusion; §Appendix O Limitations and future work.`。

<!-- claim:SF-2026-ARXIV-2605-21061:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21061:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21061:end -->

<!-- review:SF-2026-ARXIV-2605-21100:start -->
#### NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding

**问题与机制。** We present \work, which decouples MoE communication from KV cache placement and achieves dual balance through dynamic context parallelism (DCP). 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 NanoCP Request-Level Context Parallelism`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Conclusion and topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-21100:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21100:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21100:end -->

<!-- review:SF-2026-ARXIV-2605-21103:start -->
#### A Typed Tensor Language for Federated Learning

**问题与机制。** We introduce a typed tensor language that formalizes this structure. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§2 Typed Tensor Language; §3 Shared-State Factorization`；Evaluation=`§4 Differentiable Programs; §5 Discussion`；Limitations/Counterevidence=`§5 Discussion — formal one-round/shared-state scope`。

<!-- claim:SF-2026-ARXIV-2605-21103:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21103:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21103:end -->

<!-- review:SF-2026-ARXIV-2605-21125:start -->
#### Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation

**问题与机制。** To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Advantage-Collapse Diagnosis; §4 Mitigation`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and GRPO-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-21125:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21125:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21125:end -->

<!-- review:SF-2026-ARXIV-2605-21127:start -->
#### Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning

**问题与机制。** We show that this mismatch can induce reasoning-trace collapse: a fine-tuned model continues to produce plausible final answers while losing the structurally valid explicit reasoning traces that made it a reasoning model in the first place. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§Tools and frameworks for reasoning models.; §3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.`；Evaluation=`§3 Reasoning-Trace Collapse: Definition & Evaluation Framework; §A structural evaluation framework.; §4 ThinkPack : Operationalising Structural Reasoning Evaluation`；Limitations/Counterevidence=`§6 Discussion; §7 Limitations; §8 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21127:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21127:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21127:end -->

<!-- review:SF-2026-ARXIV-2605-21177:start -->
#### ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning

**问题与机制。** The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 Method; §3.1 Algorithm Description`；Evaluation=`§Convergence result.; §3.2 BP Time Analysis; §3.3 Memory Consumption Analysis`；Limitations/Counterevidence=`§5 Conclusion; §Appendix H Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21177:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21177:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21177:end -->

<!-- review:SF-2026-ARXIV-2605-21187:start -->
#### High-speed Networking for Giga-Scale AI Factories

**问题与机制。** We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§III Spectrum-X Multiplane Architecture`；Evaluation=`§IV Evaluation`；Limitations/Counterevidence=`§V Deployment Evidence; §VI Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21187:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21187:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21187:end -->

<!-- review:SF-2026-ARXIV-2605-21266:start -->
#### How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR

**问题与机制。** We introduce G2D (GRPO to DPO)}, a three-stage pipeline that performs a short GRPO warm-up, constructs a static preference dataset, and fine-tunes a model offline with DPO. 系统 owner=`TRAIN-DPO`。

**Exact-v1。** Method=`§Iterative and hybrid methods.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§6 Conclusion; §Appendix B Discussion; §Limitations.`。

<!-- claim:SF-2026-ARXIV-2605-21266:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21266:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21266:end -->

<!-- review:SF-2026-ARXIV-2605-21273:start -->
#### DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions

**问题与机制。** Driving Vision-Language-Action Models (Driving VLAs) commonly introduce natural-language reasoning as an intermediate interface for end-to-end planning, but reasoning-centric interfaces face three practical bottlenecks: obtaining high-quality reasoning annotations is difficult, generating and understanding long reasoning chains is challenging for compact models, and inference latency is substantially increased. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3.3 Action-Centric Supervised Training; §Driving Action Alignment Pretraining.; §4.5 Ablation Study of Training Strategy`；Evaluation=`§4 Experiments; §4.1 Experiments Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21273:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21273:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21273:end -->

<!-- review:SF-2026-ARXIV-2605-21312:start -->
#### Frontier: Towards Comprehensive and Accurate LLM Inference Simulation

**问题与机制。** Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 Frontier Simulator Architecture`；Evaluation=`§5 Fidelity Evaluation`；Limitations/Counterevidence=`§6 Workload Studies; §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21312:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21312:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21312:end -->

<!-- review:SF-2026-ARXIV-2605-21347:start -->
#### Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents

**问题与机制。** We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report. 系统 owner=`PLATFORM-TRACE`。

**Exact-v1。** Method=`§Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents; §3.1 System Overview; §A.1 Agent System Prompts`；Evaluation=`§3.6 Iterative Analysis Loop; §4 Evaluation; §A.4 Benchmark and Corpus Statistics`；Limitations/Counterevidence=`§5 Discussion; §5.3 Limitations and Future Work; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21347:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21347:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21347:end -->

<!-- review:SF-2026-ARXIV-2605-21384:start -->
#### SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents

**问题与机制。** We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 Benchmark Design`；Evaluation=`§3 Experiments; §4 Analysis`；Limitations/Counterevidence=`§Appendix A Limitations and Broader Impacts`。

<!-- claim:SF-2026-ARXIV-2605-21384:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21384:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21384:end -->

<!-- review:SF-2026-ARXIV-2605-21392:start -->
#### VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers

**问题与机制。** In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts. 系统 owner=`AGENT-MCP`。

**Exact-v1。** Method=`§III VIPER-MCP Taint Analysis`；Evaluation=`§V Evaluation`；Limitations/Counterevidence=`§VII Conclusion; Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21392:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21392:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21392:end -->

<!-- review:SF-2026-ARXIV-2605-21427:start -->
#### PALS: Power-Aware LLM Serving for Mixture-of-Experts Models

**问题与机制。** In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size. 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§3 PALS Joint Power/Batch Controller`；Evaluation=`§7 Evaluation`；Limitations/Counterevidence=`§8 Conclusion and GPU/MoE scope`。

<!-- claim:SF-2026-ARXIV-2605-21427:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21427:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21427:end -->

<!-- review:SF-2026-ARXIV-2605-21434:start -->
#### Agentic Model Checking

**问题与机制。** We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Agent-Propose/Solver-Verify Workflow`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6 Limitations and bounded-model-checking scope`。

<!-- claim:SF-2026-ARXIV-2605-21434:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21434:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21434:end -->

<!-- review:SF-2026-ARXIV-2605-21446:start -->
#### Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs

**问题与机制。** In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials). 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Controlled Sensor-Perturbation Protocol`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21446:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21446:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21446:end -->

<!-- review:SF-2026-ARXIV-2605-21467:start -->
#### DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards

**问题与机制。** We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Method; §4.3 Training Dynamics; §Use in training.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§7 Conclusion; §Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21467:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21467:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21467:end -->

<!-- review:SF-2026-ARXIV-2605-21468:start -->
#### You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories

**问题与机制。** In this work, we demonstrate that RLVR weight trajectories are extremely low-rank and highly predictable. 系统 owner=`TRAIN-CHECKPOINT`。

**Exact-v1。** Method=`§You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories; §3 Method; §Zero training cost.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §RLVR training and evaluation.`；Limitations/Counterevidence=`§6 Discussion; §Limitations.; §7 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21468:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21468:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21468:end -->

<!-- review:SF-2026-ARXIV-2605-21470:start -->
#### Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling

**问题与机制。** We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Methods`；Evaluation=`§4 Evaluation; §5 Results`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21470:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21470:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21470:end -->

<!-- review:SF-2026-ARXIV-2605-21482:start -->
#### DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation

**问题与机制。** We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 DeepWeb-Bench; §3.4 Evaluation Protocol`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§Appendix K Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21482:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21482:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21482:end -->

<!-- review:SF-2026-ARXIV-2605-21486:start -->
#### Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate

**问题与机制。** In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§4.1 Methodology; §6 The Effect of Weight Decay and Compute Optimal Training; §H.2 Model Architecture`；Evaluation=`§Appendix A Experimental Details; §H.3 Design Principles for Scaling Analysis`；Limitations/Counterevidence=`§8 Discussion and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21486:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21486:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21486:end -->

<!-- review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->
#### Why Latent Actions Fail, and How to Prevent It

问题与机制：We further show that previously proposed auxiliary objectives, such as action-supervision, provably encourage latent actions to be consistent across exogenous states.。机制 owner=`MULTIMODAL-WORLD-MODELS`。
全文定位：`arXiv:2605.20223v1 HTML — §Method / System Design — Why Latent Actions Fail, and How to Prevent It 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Why Latent Actions Fail, and How to Prevent It 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Why Latent Actions Fail, and How to Prevent It 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20196 | exact-v1 evaluation for Data Scaling as Progressive Coverage of a Predictive Contribution Spectrum | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20251 | score_7_9 | selected | DA-20260521-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260521-01 |
| SF-2026-ARXIV-2605-20270 | score_7_9 | selected | DA-20260521-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260521-02 |
| SF-2026-ARXIV-2605-20295 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20295 |
| SF-2026-ARXIV-2605-20296 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20296 |
| SF-2026-ARXIV-2605-20312 | score_7_9;forced_review;potential_books_delta | selected | DA-20260521-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260521-03 |
| SF-2026-ARXIV-2605-20314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20314 |
| SF-2026-ARXIV-2605-20315 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20315 |
| SF-2026-ARXIV-2605-20402 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20402 |
| SF-2026-ARXIV-2605-20477 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20477 |
| SF-2026-ARXIV-2605-20485 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20485 |
| SF-2026-ARXIV-2605-20490 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20490 |
| SF-2026-ARXIV-2605-20520 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20520 |
| SF-2026-ARXIV-2605-20544 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20544 |
| SF-2026-ARXIV-2605-20548 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20548 |
| SF-2026-ARXIV-2605-20563 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20563 |
| SF-2026-ARXIV-2605-20616 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20616 |
| SF-2026-ARXIV-2605-20630 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20630 |
| SF-2026-ARXIV-2605-20641 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20641 |
| SF-2026-ARXIV-2605-20696 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20696 |
| SF-2026-ARXIV-2605-20704 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20704 |
| SF-2026-ARXIV-2605-20706 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20706 |
| SF-2026-ARXIV-2605-20734 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20734 |
| SF-2026-ARXIV-2605-20744 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20744 |
| SF-2026-ARXIV-2605-20749 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20749 |
| SF-2026-ARXIV-2605-20752 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20752 |
| SF-2026-ARXIV-2605-20756 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20756 |
| SF-2026-ARXIV-2605-20767 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20767 |
| SF-2026-ARXIV-2605-20774 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20774 |
| SF-2026-ARXIV-2605-20798 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20798 |
| SF-2026-ARXIV-2605-20799 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20799 |
| SF-2026-ARXIV-2605-20833 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20833 |
| SF-2026-ARXIV-2605-20834 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20834 |
| SF-2026-ARXIV-2605-20863 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20863 |
| SF-2026-ARXIV-2605-20866 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20866 |
| SF-2026-ARXIV-2605-20868 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20868 |
| SF-2026-ARXIV-2605-20874 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20874 |
| SF-2026-ARXIV-2605-20876 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20876 |
| SF-2026-ARXIV-2605-20923 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20923 |
| SF-2026-ARXIV-2605-20926 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20926 |
| SF-2026-ARXIV-2605-20948 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20948 |
| SF-2026-ARXIV-2605-21061 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21061 |
| SF-2026-ARXIV-2605-21100 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21100 |
| SF-2026-ARXIV-2605-21103 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21103 |
| SF-2026-ARXIV-2605-21125 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21125 |
| SF-2026-ARXIV-2605-21127 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21127 |
| SF-2026-ARXIV-2605-21177 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21177 |
| SF-2026-ARXIV-2605-21187 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21187 |
| SF-2026-ARXIV-2605-21266 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21266 |
| SF-2026-ARXIV-2605-21273 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21273 |
| SF-2026-ARXIV-2605-21312 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21312 |
| SF-2026-ARXIV-2605-21347 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21347 |
| SF-2026-ARXIV-2605-21384 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21384 |
| SF-2026-ARXIV-2605-21392 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21392 |
| SF-2026-ARXIV-2605-21427 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21427 |
| SF-2026-ARXIV-2605-21434 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21434 |
| SF-2026-ARXIV-2605-21446 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21446 |
| SF-2026-ARXIV-2605-21467 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21467 |
| SF-2026-ARXIV-2605-21468 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21468 |
| SF-2026-ARXIV-2605-21470 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21470 |
| SF-2026-ARXIV-2605-21482 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21482 |
| SF-2026-ARXIV-2605-21486 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21486 |
| SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT |

<!-- analysis:DA-20260521-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-20251

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260521-01:end -->

<!-- analysis:DA-20260521-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-20270

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260521-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20295:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20295:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20296:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20296:end -->

<!-- analysis:DA-20260521-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-20312

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260521-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20314:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20314:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20315:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20315:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20402:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20402:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20477:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20477:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20485:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20485:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20490:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20490:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20520:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20520:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20544:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20548:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20548:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20563:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20563:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20616:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20616:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20630:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20630:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20641:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20641:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20696:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20696:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20704:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20706:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20706:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20734:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20744:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20744:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20749:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20749:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20752:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20756:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20756:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20767:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20767:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20774:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20798:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20799:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20799:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20833:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20833:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20834:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20834:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20863:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20863:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20866:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20866:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20868:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20868:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20874:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20876:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20876:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20923:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20923:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20926:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20926:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20948:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20948:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21061:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21100:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21100:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21103:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21103:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21125:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21125:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21127:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21127:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21177:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21177:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21187:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21187:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21266:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21266:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21273:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21273:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21312:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21312:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21347:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21347:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21384:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21392:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21392:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21427:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21427:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21434:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21434:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21446:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21446:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21467:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21468:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21468:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21470:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21470:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21482:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21482:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21486:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21486:end -->

<!-- analysis-decision:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-20196 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#L165 (H2: 从论文曲线到工程容量规划) | books/part-01-worldview/06-why-transformer-changed-the-world.md#L10 (H2: 本章要回答的问题); books/part-01-worldview/08-why-llms-show-intelligence.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-20196 | delta:SF-2026-ARXIV-2605-20196 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20196 |
| SF-2026-ARXIV-2605-20251 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20251 | delta:SF-2026-ARXIV-2605-20251 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20251 |
| SF-2026-ARXIV-2605-20270 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20270 | delta:SF-2026-ARXIV-2605-20270 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20270 |
| SF-2026-ARXIV-2605-20295 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20295 | delta:SF-2026-ARXIV-2605-20295 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20295 |
| SF-2026-ARXIV-2605-20296 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-20296 | delta:SF-2026-ARXIV-2605-20296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20296 |
| SF-2026-ARXIV-2605-20312 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-20312 | delta:SF-2026-ARXIV-2605-20312 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20312 |
| SF-2026-ARXIV-2605-20314 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-20314 | delta:SF-2026-ARXIV-2605-20314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20314 |
| SF-2026-ARXIV-2605-20315 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-20315 | delta:SF-2026-ARXIV-2605-20315 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20315 |
| SF-2026-ARXIV-2605-20402 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20402 | delta:SF-2026-ARXIV-2605-20402 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20402 |
| SF-2026-ARXIV-2605-20477 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20477 | delta:SF-2026-ARXIV-2605-20477 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20477 |
| SF-2026-ARXIV-2605-20485 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20485 | delta:SF-2026-ARXIV-2605-20485 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20485 |
| SF-2026-ARXIV-2605-20490 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20490 | delta:SF-2026-ARXIV-2605-20490 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20490 |
| SF-2026-ARXIV-2605-20520 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20520 | delta:SF-2026-ARXIV-2605-20520 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20520 |
| SF-2026-ARXIV-2605-20544 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-20544 | delta:SF-2026-ARXIV-2605-20544 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20544 |
| SF-2026-ARXIV-2605-20548 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20548 | delta:SF-2026-ARXIV-2605-20548 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20548 |
| SF-2026-ARXIV-2605-20563 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20563 | delta:SF-2026-ARXIV-2605-20563 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20563 |
| SF-2026-ARXIV-2605-20616 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-20616 | delta:SF-2026-ARXIV-2605-20616 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20616 |
| SF-2026-ARXIV-2605-20630 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-20630 | delta:SF-2026-ARXIV-2605-20630 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20630 |
| SF-2026-ARXIV-2605-20641 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20641 | delta:SF-2026-ARXIV-2605-20641 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20641 |
| SF-2026-ARXIV-2605-20696 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-20696 | delta:SF-2026-ARXIV-2605-20696 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20696 |
| SF-2026-ARXIV-2605-20704 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20704 | delta:SF-2026-ARXIV-2605-20704 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20704 |
| SF-2026-ARXIV-2605-20706 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20706 | delta:SF-2026-ARXIV-2605-20706 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20706 |
| SF-2026-ARXIV-2605-20734 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20734 | delta:SF-2026-ARXIV-2605-20734 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20734 |
| SF-2026-ARXIV-2605-20744 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20744 | delta:SF-2026-ARXIV-2605-20744 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20744 |
| SF-2026-ARXIV-2605-20749 | MODEL-FFN | books/part-02-model/16-feed-forward-mlp.md#chapter-16 | books/part-02-model/15-multi-head-attention.md#chapter-15;books/part-02-model/17-transformer-layer.md#chapter-17 | existing:SF-2026-ARXIV-2605-20749 | delta:SF-2026-ARXIV-2605-20749 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20749 |
| SF-2026-ARXIV-2605-20752 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-20752 | delta:SF-2026-ARXIV-2605-20752 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20752 |
| SF-2026-ARXIV-2605-20756 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-20756 | delta:SF-2026-ARXIV-2605-20756 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20756 |
| SF-2026-ARXIV-2605-20767 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20767 | delta:SF-2026-ARXIV-2605-20767 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20767 |
| SF-2026-ARXIV-2605-20774 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20774 | delta:SF-2026-ARXIV-2605-20774 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20774 |
| SF-2026-ARXIV-2605-20798 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20798 | delta:SF-2026-ARXIV-2605-20798 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20798 |
| SF-2026-ARXIV-2605-20799 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-20799 | delta:SF-2026-ARXIV-2605-20799 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20799 |
| SF-2026-ARXIV-2605-20833 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20833 | delta:SF-2026-ARXIV-2605-20833 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20833 |
| SF-2026-ARXIV-2605-20834 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-20834 | delta:SF-2026-ARXIV-2605-20834 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20834 |
| SF-2026-ARXIV-2605-20863 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20863 | delta:SF-2026-ARXIV-2605-20863 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20863 |
| SF-2026-ARXIV-2605-20866 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-20866 | delta:SF-2026-ARXIV-2605-20866 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20866 |
| SF-2026-ARXIV-2605-20868 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-20868 | delta:SF-2026-ARXIV-2605-20868 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20868 |
| SF-2026-ARXIV-2605-20874 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20874 | delta:SF-2026-ARXIV-2605-20874 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20874 |
| SF-2026-ARXIV-2605-20876 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-20876 | delta:SF-2026-ARXIV-2605-20876 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20876 |
| SF-2026-ARXIV-2605-20923 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-20923 | delta:SF-2026-ARXIV-2605-20923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20923 |
| SF-2026-ARXIV-2605-20926 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-20926 | delta:SF-2026-ARXIV-2605-20926 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20926 |
| SF-2026-ARXIV-2605-20948 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20;books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-20948 | delta:SF-2026-ARXIV-2605-20948 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20948 |
| SF-2026-ARXIV-2605-21061 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21061 | delta:SF-2026-ARXIV-2605-21061 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21061 |
| SF-2026-ARXIV-2605-21100 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-21100 | delta:SF-2026-ARXIV-2605-21100 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21100 |
| SF-2026-ARXIV-2605-21103 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-21103 | delta:SF-2026-ARXIV-2605-21103 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21103 |
| SF-2026-ARXIV-2605-21125 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21125 | delta:SF-2026-ARXIV-2605-21125 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21125 |
| SF-2026-ARXIV-2605-21127 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21127 | delta:SF-2026-ARXIV-2605-21127 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21127 |
| SF-2026-ARXIV-2605-21177 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21177 | delta:SF-2026-ARXIV-2605-21177 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21177 |
| SF-2026-ARXIV-2605-21187 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-21187 | delta:SF-2026-ARXIV-2605-21187 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21187 |
| SF-2026-ARXIV-2605-21266 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33;books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-21266 | delta:SF-2026-ARXIV-2605-21266 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21266 |
| SF-2026-ARXIV-2605-21273 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21273 | delta:SF-2026-ARXIV-2605-21273 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21273 |
| SF-2026-ARXIV-2605-21312 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-21312 | delta:SF-2026-ARXIV-2605-21312 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21312 |
| SF-2026-ARXIV-2605-21347 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#chapter-69 | books/part-06-ai-infrastructure/68-logging.md#chapter-68;books/part-06-ai-infrastructure/70-cost.md#chapter-70 | existing:SF-2026-ARXIV-2605-21347 | delta:SF-2026-ARXIV-2605-21347 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21347 |
| SF-2026-ARXIV-2605-21384 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21384 | delta:SF-2026-ARXIV-2605-21384 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21384 |
| SF-2026-ARXIV-2605-21392 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-21392 | delta:SF-2026-ARXIV-2605-21392 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21392 |
| SF-2026-ARXIV-2605-21427 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-21427 | delta:SF-2026-ARXIV-2605-21427 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21427 |
| SF-2026-ARXIV-2605-21434 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21434 | delta:SF-2026-ARXIV-2605-21434 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21434 |
| SF-2026-ARXIV-2605-21446 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21446 | delta:SF-2026-ARXIV-2605-21446 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21446 |
| SF-2026-ARXIV-2605-21467 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21467 | delta:SF-2026-ARXIV-2605-21467 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21467 |
| SF-2026-ARXIV-2605-21468 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#chapter-35 | books/part-04-training-system/34-dpo.md#chapter-34;books/part-04-training-system/36-distributed-training.md#chapter-36 | existing:SF-2026-ARXIV-2605-21468 | delta:SF-2026-ARXIV-2605-21468 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21468 |
| SF-2026-ARXIV-2605-21470 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-21470 | delta:SF-2026-ARXIV-2605-21470 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21470 |
| SF-2026-ARXIV-2605-21482 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21482 | delta:SF-2026-ARXIV-2605-21482 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21482 |
| SF-2026-ARXIV-2605-21486 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21486 | delta:SF-2026-ARXIV-2605-21486 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21486 |
| SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | delta:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT | Direct Evolution | No Change — Existing Coverage | books-review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT |

<!-- books-review:SF-2026-ARXIV-2605-20196:start -->
<!-- existing:SF-2026-ARXIV-2605-20196:start -->对读 `books/part-01-worldview/07-scaling-law.md#L165 (H2: 从论文曲线到工程容量规划)` 及相邻章节后，现有命题为：Scaling Law 对 AI System 的直接价值，可以落在四类决策上。 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-20196:end -->
<!-- delta:SF-2026-ARXIV-2605-20196:start -->Exact-v1 的 source-specific delta 是：论文以 suffix-automaton state 构造 predictive-contribution spectrum：每个状态的 global-KL contribution 等于经验状态质量乘以其相对全局 next-token baseline 的 KL 偏离；再定义有效截断秩 K(N)，令 spectrum residual tail 与模型 excess loss 对齐，用它描述数据量增加时逐步覆盖的预测贡献。 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-20196:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-20196:end -->

<!-- books-review:SF-2026-ARXIV-2605-20251:start -->
<!-- existing:SF-2026-ARXIV-2605-20251:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-20251:end -->
<!-- delta:SF-2026-ARXIV-2605-20251:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-20251:end -->
<!-- books-review:SF-2026-ARXIV-2605-20251:end -->

<!-- books-review:SF-2026-ARXIV-2605-20270:start -->
<!-- existing:SF-2026-ARXIV-2605-20270:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-20270:end -->
<!-- delta:SF-2026-ARXIV-2605-20270:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-20270:end -->
<!-- books-review:SF-2026-ARXIV-2605-20270:end -->

<!-- books-review:SF-2026-ARXIV-2605-20295:start -->
<!-- existing:SF-2026-ARXIV-2605-20295:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20295:end -->
<!-- delta:SF-2026-ARXIV-2605-20295:start -->To bridge the gap between high-fidelity PTQ and NPU-constrained inference, we propose Quant.npu, a integer-only fully static quantization framework.<!-- delta:SF-2026-ARXIV-2605-20295:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20295:end -->

<!-- books-review:SF-2026-ARXIV-2605-20296:start -->
<!-- existing:SF-2026-ARXIV-2605-20296:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20296:end -->
<!-- delta:SF-2026-ARXIV-2605-20296:start -->We study this phenomenon, known as catastrophic forgetting, and propose a post-hoc repair solution that uses only the pretrained checkpoint $W_{\mathrm{base}}$ and its fine-tuned descendant $W_{\mathrm{ft}}$.<!-- delta:SF-2026-ARXIV-2605-20296:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20296:end -->

<!-- books-review:SF-2026-ARXIV-2605-20312:start -->
<!-- existing:SF-2026-ARXIV-2605-20312:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20312:end -->
<!-- delta:SF-2026-ARXIV-2605-20312:start -->Autonomous agents deployed in regulated domains must produce a verification artifact per consequential output: a record an auditor can re-execute offline, capturing what was claimed, against what source, by whom, when, and how.<!-- delta:SF-2026-ARXIV-2605-20312:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20312:end -->

<!-- books-review:SF-2026-ARXIV-2605-20314:start -->
<!-- existing:SF-2026-ARXIV-2605-20314:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20314:end -->
<!-- delta:SF-2026-ARXIV-2605-20314:start -->We argue that the speedup comes from appropriate layer-wise growth enabled by sampling biases, which is more pronounced when the dataset size is smaller.<!-- delta:SF-2026-ARXIV-2605-20314:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20314:end -->

<!-- books-review:SF-2026-ARXIV-2605-20315:start -->
<!-- existing:SF-2026-ARXIV-2605-20315:start -->`books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20315:end -->
<!-- delta:SF-2026-ARXIV-2605-20315:start -->However, these agentic workflows often introduce substantial input-side overhead, making the compute-intensive prefilling stage a key bottleneck in long-context, multi-turn inference.<!-- delta:SF-2026-ARXIV-2605-20315:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20315:end -->

<!-- books-review:SF-2026-ARXIV-2605-20402:start -->
<!-- existing:SF-2026-ARXIV-2605-20402:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20402:end -->
<!-- delta:SF-2026-ARXIV-2605-20402:start -->We prove an exact three-way decomposition of quantization error and show how each component dominates a distinct RL training pathway.<!-- delta:SF-2026-ARXIV-2605-20402:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20402:end -->

<!-- books-review:SF-2026-ARXIV-2605-20477:start -->
<!-- existing:SF-2026-ARXIV-2605-20477:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20477:end -->
<!-- delta:SF-2026-ARXIV-2605-20477:start -->We then propose an RL-based training pipeline for learning such reflections directly from experience, without human-provided examples.<!-- delta:SF-2026-ARXIV-2605-20477:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20477:end -->

<!-- books-review:SF-2026-ARXIV-2605-20485:start -->
<!-- existing:SF-2026-ARXIV-2605-20485:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20485:end -->
<!-- delta:SF-2026-ARXIV-2605-20485:start -->We propose ZEBRA, a zero-shot framework that reduces multi-phase budget allocation to a continuous nonlinear knapsack problem: an LLM controller estimates per-phase utility curves, and a water-filling search on the Lagrange multiplier returns the per-phase split.<!-- delta:SF-2026-ARXIV-2605-20485:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20485:end -->

<!-- books-review:SF-2026-ARXIV-2605-20490:start -->
<!-- existing:SF-2026-ARXIV-2605-20490:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20490:end -->
<!-- delta:SF-2026-ARXIV-2605-20490:start -->We argue that these evaluation approaches are inadequate for assessing overall performance of the UA system for decision making under uncertainty and propose a novel family of metrics, ECUAS$_n$, formulated as proper scoring rules for the task of interest.<!-- delta:SF-2026-ARXIV-2605-20490:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20490:end -->

<!-- books-review:SF-2026-ARXIV-2605-20520:start -->
<!-- existing:SF-2026-ARXIV-2605-20520:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20520:end -->
<!-- delta:SF-2026-ARXIV-2605-20520:start -->In this paper we survey recent open-world evaluations, identify their strengths and limitations, and introduce CRUX (Collaborative Research for Updating AI eXpectations), a project for conducting such evaluations regularly.<!-- delta:SF-2026-ARXIV-2605-20520:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20520:end -->

<!-- books-review:SF-2026-ARXIV-2605-20544:start -->
<!-- existing:SF-2026-ARXIV-2605-20544:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20544:end -->
<!-- delta:SF-2026-ARXIV-2605-20544:start -->To address this gap, we introduce a taxonomy to categorize abstention in the context of embodied robotics and present RoboAbstention, a scalable and auditable framework for generating abstention instructions grounded in images gathered from five robotics datasets.<!-- delta:SF-2026-ARXIV-2605-20544:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20544:end -->

<!-- books-review:SF-2026-ARXIV-2605-20548:start -->
<!-- existing:SF-2026-ARXIV-2605-20548:start -->`books/part-07-agent/82-multi-agent.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20548:end -->
<!-- delta:SF-2026-ARXIV-2605-20548:start -->To address this, we conduct a systematic analysis of inter-agent communication to identify which information drives MA performance.<!-- delta:SF-2026-ARXIV-2605-20548:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20548:end -->

<!-- books-review:SF-2026-ARXIV-2605-20563:start -->
<!-- existing:SF-2026-ARXIV-2605-20563:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20563:end -->
<!-- delta:SF-2026-ARXIV-2605-20563:start -->In this paper, we propose STORM, i.e., STate-ORiented Management for multi-agent collaboration.<!-- delta:SF-2026-ARXIV-2605-20563:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20563:end -->

<!-- books-review:SF-2026-ARXIV-2605-20616:start -->
<!-- existing:SF-2026-ARXIV-2605-20616:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`Auto-Dreamer: Learning Offline Memory Consolidation for Language Agents` 的 source-specific 机制是：Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20616:end -->
<!-- delta:SF-2026-ARXIV-2605-20616:start -->Inspired by complementary learning systems theory, we propose Auto-Dreamer, a learned offline consolidator for language-agent memory.<!-- delta:SF-2026-ARXIV-2605-20616:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20616:end -->

<!-- books-review:SF-2026-ARXIV-2605-20630:start -->
<!-- existing:SF-2026-ARXIV-2605-20630:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract。`Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines` 的 source-specific 机制是：We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20630:end -->
<!-- delta:SF-2026-ARXIV-2605-20630:start -->We propose two complementary optimization layers for AOB plan-execute pipelines: a temporal semantic cache and a set of MCP workflow optimizations combining disk-backed tool-discovery caching and dependency-aware parallel step execution.<!-- delta:SF-2026-ARXIV-2605-20630:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20630:end -->

<!-- books-review:SF-2026-ARXIV-2605-20641:start -->
<!-- existing:SF-2026-ARXIV-2605-20641:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority；但 `Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs` 所暴露的以下缺口尚未显式进入正文：把可信 base weights 之后的量化、剪枝或其他 optimization pass 视为新的 security revision；optimizer/serving pipeline 只能提出变换，独立 integrity gate 比较优化前后触发行为并拥有发布权。<!-- existing:SF-2026-ARXIV-2605-20641:end -->
<!-- delta:SF-2026-ARXIV-2605-20641:start -->把可信 base weights 之后的量化、剪枝或其他 optimization pass 视为新的 security revision；optimizer/serving pipeline 只能提出变换，独立 integrity gate 比较优化前后触发行为并拥有发布权。<!-- delta:SF-2026-ARXIV-2605-20641:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20641:end -->

<!-- books-review:SF-2026-ARXIV-2605-20696:start -->
<!-- existing:SF-2026-ARXIV-2605-20696:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff；但 `Distributed Direct Preference Optimization` 所暴露的以下缺口尚未显式进入正文：DPO 进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 共同构成 objective/run identity；聚合不再只是搬运普通梯度。<!-- existing:SF-2026-ARXIV-2605-20696:end -->
<!-- delta:SF-2026-ARXIV-2605-20696:start -->DPO 进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 共同构成 objective/run identity；聚合不再只是搬运普通梯度。<!-- delta:SF-2026-ARXIV-2605-20696:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20696:end -->

<!-- books-review:SF-2026-ARXIV-2605-20704:start -->
<!-- existing:SF-2026-ARXIV-2605-20704:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。第84章已拥有 Agent runtime 的 credential、policy、lifecycle 与 commit authority。`Heartbeat-Bound Hierarchical Credentials: Cryptographic Revocation for AI Agent Swarms` 的 source-specific 机制是：We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20704:end -->
<!-- delta:SF-2026-ARXIV-2605-20704:start -->We present Heartbeat-Bound Hierarchical Credentials (HBHC), a cryptographic protocol that binds credential validity to periodic parent liveness proofs.<!-- delta:SF-2026-ARXIV-2605-20704:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20704:end -->

<!-- books-review:SF-2026-ARXIV-2605-20706:start -->
<!-- existing:SF-2026-ARXIV-2605-20706:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。第49章已把 logical graph、physical execution plan、operator schedule 与 hardware control state 分离。`Llamas on the Web: Memory-Efficient, Performance-Portable, and Multi-Precision LLM Inference with WebGPU` 的 source-specific 机制是：To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20706:end -->
<!-- delta:SF-2026-ARXIV-2605-20706:start -->To realize this opportunity, we present Llamas on the Web (LlamaWeb), a WebGPU backend for llama$.$cpp that enables memory-efficient and performance-portable LLM inference across a wide range of model weight formats in the browser.<!-- delta:SF-2026-ARXIV-2605-20706:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20706:end -->

<!-- books-review:SF-2026-ARXIV-2605-20734:start -->
<!-- existing:SF-2026-ARXIV-2605-20734:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority。`An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress` 的 source-specific 机制是：A large language model (LLM) agent that sends messages can leak data inside them.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20734:end -->
<!-- delta:SF-2026-ARXIV-2605-20734:start -->A large language model (LLM) agent that sends messages can leak data inside them.<!-- delta:SF-2026-ARXIV-2605-20734:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20734:end -->

<!-- books-review:SF-2026-ARXIV-2605-20744:start -->
<!-- existing:SF-2026-ARXIV-2605-20744:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Hack-Verifiable Environments: Towards Evaluating Reward Hacking at Scale` 的 source-specific 机制是：In this work, we introduce a new evaluation paradigm for measuring reward hacking.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20744:end -->
<!-- delta:SF-2026-ARXIV-2605-20744:start -->In this work, we introduce a new evaluation paradigm for measuring reward hacking.<!-- delta:SF-2026-ARXIV-2605-20744:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20744:end -->

<!-- books-review:SF-2026-ARXIV-2605-20749:start -->
<!-- existing:SF-2026-ARXIV-2605-20749:start -->已顺读 `books/part-02-model/16-feed-forward-mlp.md` 与相邻章节 ['books/part-02-model/15-multi-head-attention.md', 'books/part-02-model/17-transformer-layer.md']。第16章已解释 GLU/SwiGLU 的内容分支、gate 分支、预算与 kernel 边界，但没有解释 conditioning 为何可能改变可训练性；但 `The Devil is in the Condition Numbers: Why is GLU Better than non-GLU Structure?` 所暴露的以下缺口尚未显式进入正文：GLU 的收益不能只描述为多一个 gate；两分支乘法改变局部 kernel/conditioning，使训练可达性与非 gated FFN 不同，同时保留 NTK、两层网络和作者规模的证据边界。<!-- existing:SF-2026-ARXIV-2605-20749:end -->
<!-- delta:SF-2026-ARXIV-2605-20749:start -->GLU 的收益不能只描述为多一个 gate；两分支乘法改变局部 kernel/conditioning，使训练可达性与非 gated FFN 不同，同时保留 NTK、两层网络和作者规模的证据边界。<!-- delta:SF-2026-ARXIV-2605-20749:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20749:end -->

<!-- books-review:SF-2026-ARXIV-2605-20752:start -->
<!-- existing:SF-2026-ARXIV-2605-20752:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`GaussianDream: A Feed-Forward 3D Gaussian World Model for Robotic Manipulation` 的 source-specific 机制是：To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20752:end -->
<!-- delta:SF-2026-ARXIV-2605-20752:start -->To address this, we propose \textbf{GaussianDream}, a feed-forward 3D Gaussian world-model plug-in.<!-- delta:SF-2026-ARXIV-2605-20752:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20752:end -->

<!-- books-review:SF-2026-ARXIV-2605-20756:start -->
<!-- existing:SF-2026-ARXIV-2605-20756:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差；但 `Correcting Stochastic Update Bias in Preconditioned Language Model Optimizers` 所暴露的以下缺口尚未显式进入正文：preconditioner 与 gradient 来自同一 minibatch 会产生 coupling bias，非线性 inverse/root 即使输入估计无偏也会产生 inversion bias；cross-fit 与 variance correction 改变 microbatch/state 账本并增加估计成本。<!-- existing:SF-2026-ARXIV-2605-20756:end -->
<!-- delta:SF-2026-ARXIV-2605-20756:start -->preconditioner 与 gradient 来自同一 minibatch 会产生 coupling bias，非线性 inverse/root 即使输入估计无偏也会产生 inversion bias；cross-fit 与 variance correction 改变 microbatch/state 账本并增加估计成本。<!-- delta:SF-2026-ARXIV-2605-20756:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20756:end -->

<!-- books-review:SF-2026-ARXIV-2605-20767:start -->
<!-- existing:SF-2026-ARXIV-2605-20767:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`The Illusion of Intervention: Your LLM-Simulated Experiment is an Observational Study` 的 source-specific 机制是：Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20767:end -->
<!-- delta:SF-2026-ARXIV-2605-20767:start -->Large language models (LLMs) show potential as simulators of human behavior, offering a scalable way to study responses to interventions.<!-- delta:SF-2026-ARXIV-2605-20767:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20767:end -->

<!-- books-review:SF-2026-ARXIV-2605-20774:start -->
<!-- existing:SF-2026-ARXIV-2605-20774:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`VLA-REPLICA: A Low-Cost, Reproducible Benchmark for Real-World Evaluation of Vision-Language-Action Models` 的 source-specific 机制是：We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20774:end -->
<!-- delta:SF-2026-ARXIV-2605-20774:start -->We introduce VLA-REPLICA, a low-cost, easily reproducible real-world benchmark for evaluating VLA models.<!-- delta:SF-2026-ARXIV-2605-20774:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20774:end -->

<!-- books-review:SF-2026-ARXIV-2605-20798:start -->
<!-- existing:SF-2026-ARXIV-2605-20798:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Most Transformer Modifications Still Do Not Transfer at 1-3B: A 2020-2026 Update to Narang et al. (2021) with Downstream Evaluation and a Noise Floor` 的 source-specific 机制是：Narang et al.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20798:end -->
<!-- delta:SF-2026-ARXIV-2605-20798:start -->Narang et al.<!-- delta:SF-2026-ARXIV-2605-20798:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20798:end -->

<!-- books-review:SF-2026-ARXIV-2605-20799:start -->
<!-- existing:SF-2026-ARXIV-2605-20799:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']。第67章已区分 raw utilization、有效进展、sensor/health/attestation、漂移与独立 red-team；但 `Instant GPU Efficiency Visibility at Fleet Scale` 所暴露的以下缺口尚未显式进入正文：GPU busy 之外增加 precision-agnostic counter-derived FLOP-progress sensor，并把 counter mapping、clock、kernel coverage 与 calibration revision 纳入 metric identity；它仍不能单独证明 useful work 或 SLO。<!-- existing:SF-2026-ARXIV-2605-20799:end -->
<!-- delta:SF-2026-ARXIV-2605-20799:start -->GPU busy 之外增加 precision-agnostic counter-derived FLOP-progress sensor，并把 counter mapping、clock、kernel coverage 与 calibration revision 纳入 metric identity；它仍不能单独证明 useful work 或 SLO。<!-- delta:SF-2026-ARXIV-2605-20799:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20799:end -->

<!-- books-review:SF-2026-ARXIV-2605-20833:start -->
<!-- existing:SF-2026-ARXIV-2605-20833:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`MemGym: a Long-Horizon Memory Environment for LLM Agents` 的 source-specific 机制是：We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20833:end -->
<!-- delta:SF-2026-ARXIV-2605-20833:start -->We present MemGym, a benchmark for agentic memory that unifies existing agent gyms and in-house memory-grounded pipelines behind one memory-reasoning interface.<!-- delta:SF-2026-ARXIV-2605-20833:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20833:end -->

<!-- books-review:SF-2026-ARXIV-2605-20834:start -->
<!-- existing:SF-2026-ARXIV-2605-20834:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff。`Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment` 的 source-specific 机制是：We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20834:end -->
<!-- delta:SF-2026-ARXIV-2605-20834:start -->We characterize when this assumption is violated, show the existence of an undesirable solution space, and prove that DPO and RLHF optimize fundamentally different objectives in such cases.<!-- delta:SF-2026-ARXIV-2605-20834:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20834:end -->

<!-- books-review:SF-2026-ARXIV-2605-20863:start -->
<!-- existing:SF-2026-ARXIV-2605-20863:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']。第31章已覆盖 rollout/training runtime 解耦、staleness、resource asymmetry 与 cluster pipeline。`PlexRL: Cluster-Level Orchestration of Serviceized LLM Execution for RLVR` 的 source-specific 机制是：However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20863:end -->
<!-- delta:SF-2026-ARXIV-2605-20863:start -->However, RLVR training is notoriously inefficient: long-tailed rollouts, tool-induced stalls, and asymmetric resource requirements between rollout and training introduce substantial idle time that cannot be eliminated by job-local optimizations such as synchronous pipelining, asynchronous rollout, or colocated execution.<!-- delta:SF-2026-ARXIV-2605-20863:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20863:end -->

<!-- books-review:SF-2026-ARXIV-2605-20866:start -->
<!-- existing:SF-2026-ARXIV-2605-20866:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback。`LOSCAR-SGD: Local SGD with Communication-Computation Overlap and Delay-Corrected Sparse Model Averaging` 的 source-specific 机制是：We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20866:end -->
<!-- delta:SF-2026-ARXIV-2605-20866:start -->We study a heterogeneous-compute setting in which different workers may take different numbers of local steps, and we propose LOSCAR-SGD, a Local SGD method that communicates only a sparse subset of model coordinates and continues optimizing while communication is in flight.<!-- delta:SF-2026-ARXIV-2605-20866:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20866:end -->

<!-- books-review:SF-2026-ARXIV-2605-20868:start -->
<!-- existing:SF-2026-ARXIV-2605-20868:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`Runtime-Certified Bounded-Error Quantized Attention` 的 source-specific 机制是：We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20868:end -->
<!-- delta:SF-2026-ARXIV-2605-20868:start -->We present a tiered KV cache architecture that enables runtime-certified attention: INT8 keys and INT4 values are stored in GPU memory, while FP16 originals are retained in system RAM for deterministic fallback.<!-- delta:SF-2026-ARXIV-2605-20868:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20868:end -->

<!-- books-review:SF-2026-ARXIV-2605-20874:start -->
<!-- existing:SF-2026-ARXIV-2605-20874:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。第84章已拥有 Agent runtime 的 credential、policy、lifecycle 与 commit authority。`Governance by Construction for Generalist Agents` 的 source-specific 机制是：We present a runtime governance architecture that enforces policy interventions at every critical stage of execution.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20874:end -->
<!-- delta:SF-2026-ARXIV-2605-20874:start -->We present a runtime governance architecture that enforces policy interventions at every critical stage of execution.<!-- delta:SF-2026-ARXIV-2605-20874:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20874:end -->

<!-- books-review:SF-2026-ARXIV-2605-20876:start -->
<!-- existing:SF-2026-ARXIV-2605-20876:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`Terminal-World: Scaling Terminal-Agent Environments via Agent Skills` 的 source-specific 机制是：To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20876:end -->
<!-- delta:SF-2026-ARXIV-2605-20876:start -->To address these limitations, we introduce Terminal-World, a fully automated pipeline that uses agent skills as the central synthesis primitive, which jointly encode what to accomplish, when to apply (preconditions and environment state), and how to execute, enabling task instructions, environments, and teacher trajectories to be co-derived.<!-- delta:SF-2026-ARXIV-2605-20876:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20876:end -->

<!-- books-review:SF-2026-ARXIV-2605-20923:start -->
<!-- existing:SF-2026-ARXIV-2605-20923:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract；但 `Causal Past Logic for Runtime Verification of Distributed LLM Agent Workflows` 所暴露的以下缺口尚未显式进入正文：分布式 Agent workflow 的事件不是单一线性日志；runtime verifier 应在 partial-order/causal-past 上判定 temporal predicate，并保存 event identity、happens-before 与 unknown 边界。<!-- existing:SF-2026-ARXIV-2605-20923:end -->
<!-- delta:SF-2026-ARXIV-2605-20923:start -->分布式 Agent workflow 的事件不是单一线性日志；runtime verifier 应在 partial-order/causal-past 上判定 temporal predicate，并保存 event identity、happens-before 与 unknown 边界。<!-- delta:SF-2026-ARXIV-2605-20923:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20923:end -->

<!-- books-review:SF-2026-ARXIV-2605-20926:start -->
<!-- existing:SF-2026-ARXIV-2605-20926:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`MemConflict: Evaluating Long-Term Memory Systems Under Memory Conflicts` 的 source-specific 机制是：To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20926:end -->
<!-- delta:SF-2026-ARXIV-2605-20926:start -->To address this gap, we propose MemConflict, a diagnostic framework that treats memory validity as a query-conditioned fitness-for-use problem.<!-- delta:SF-2026-ARXIV-2605-20926:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20926:end -->

<!-- books-review:SF-2026-ARXIV-2605-20948:start -->
<!-- existing:SF-2026-ARXIV-2605-20948:start -->已顺读 `books/part-02-model/21-moe.md` 与相邻章节 ['books/part-02-model/20-sampling.md', 'books/part-02-model/22-long-context.md']。第21章已拥有 conditional routing、retrieval memory、expert state、placement 与 fallback；离线 hidden-state memory 只是受限实现分支。`Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory` 的 source-specific 机制是：We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-20948:end -->
<!-- delta:SF-2026-ARXIV-2605-20948:start -->We propose Memory Grafting, a conditional memory scaling method that utilizes frozen hidden states from a grafting model as conditional n-gram memory.<!-- delta:SF-2026-ARXIV-2605-20948:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20948:end -->

<!-- books-review:SF-2026-ARXIV-2605-21061:start -->
<!-- existing:SF-2026-ARXIV-2605-21061:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope；但 `Grounding Driving VLA via Inverse Kinematics` 所暴露的以下缺口尚未显式进入正文：trajectory proposal 需要把当前视觉状态与目标/未来视觉状态作为 inverse-kinematics 边界条件，显式隔离可观测几何、未来 proposal 与低层 controller 的 action commit。<!-- existing:SF-2026-ARXIV-2605-21061:end -->
<!-- delta:SF-2026-ARXIV-2605-21061:start -->trajectory proposal 需要把当前视觉状态与目标/未来视觉状态作为 inverse-kinematics 边界条件，显式隔离可观测几何、未来 proposal 与低层 controller 的 action commit。<!-- delta:SF-2026-ARXIV-2605-21061:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21061:end -->

<!-- books-review:SF-2026-ARXIV-2605-21100:start -->
<!-- existing:SF-2026-ARXIV-2605-21100:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。第56章已拥有 request/KV/topology/SLO 联合 placement、routing 与 state-aware scheduling；但 `NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding` 所暴露的以下缺口尚未显式进入正文：MoE decode 中动态 Context Parallel 应分离 expert-communication pressure 与 KV placement pressure；request-level plan 绑定 topology/KV/collective epoch，收益用重规划与迁移成本交换。<!-- existing:SF-2026-ARXIV-2605-21100:end -->
<!-- delta:SF-2026-ARXIV-2605-21100:start -->MoE decode 中动态 Context Parallel 应分离 expert-communication pressure 与 KV placement pressure；request-level plan 绑定 topology/KV/collective epoch，收益用重规划与迁移成本交换。<!-- delta:SF-2026-ARXIV-2605-21100:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21100:end -->

<!-- books-review:SF-2026-ARXIV-2605-21103:start -->
<!-- existing:SF-2026-ARXIV-2605-21103:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback；但 `A Typed Tensor Language for Federated Learning` 所暴露的以下缺口尚未显式进入正文：federated tensor type 区分 client-record axis 与 shared state，并把一轮计算限制为 encode→merge→decode 的固定维 shared-state factorization；类型系统拥有可表达通信边界，而非任意协议标签。<!-- existing:SF-2026-ARXIV-2605-21103:end -->
<!-- delta:SF-2026-ARXIV-2605-21103:start -->federated tensor type 区分 client-record axis 与 shared state，并把一轮计算限制为 encode→merge→decode 的固定维 shared-state factorization；类型系统拥有可表达通信边界，而非任意协议标签。<!-- delta:SF-2026-ARXIV-2605-21103:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21103:end -->

<!-- books-review:SF-2026-ARXIV-2605-21125:start -->
<!-- existing:SF-2026-ARXIV-2605-21125:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`Advantage Collapse in Group Relative Policy Optimization: Diagnosis and Mitigation` 的 source-specific 机制是：To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21125:end -->
<!-- delta:SF-2026-ARXIV-2605-21125:start -->To address this, we introduce the Advantage Collapse Rate (ACR), the first diagnostic metric quantifying the proportion of training batches with ineffective gradients.<!-- delta:SF-2026-ARXIV-2605-21125:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21125:end -->

<!-- books-review:SF-2026-ARXIV-2605-21127:start -->
<!-- existing:SF-2026-ARXIV-2605-21127:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号；但 `Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning` 所暴露的以下缺口尚未显式进入正文：SFT 不能只验收最终答案；reasoning-trace structure 可能在 answer accuracy 尚未下降时先 collapse，因而 trace validity、final outcome 与 latent capability 必须分别版本化和验收。<!-- existing:SF-2026-ARXIV-2605-21127:end -->
<!-- delta:SF-2026-ARXIV-2605-21127:start -->SFT 不能只验收最终答案；reasoning-trace structure 可能在 answer accuracy 尚未下降时先 collapse，因而 trace validity、final outcome 与 latent capability 必须分别版本化和验收。<!-- delta:SF-2026-ARXIV-2605-21127:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21127:end -->

<!-- books-review:SF-2026-ARXIV-2605-21177:start -->
<!-- existing:SF-2026-ARXIV-2605-21177:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号。`ChunkFT: Byte-Streamed Optimization for Memory-Efficient Full Fine-Tuning` 的 source-specific 机制是：The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21177:end -->
<!-- delta:SF-2026-ARXIV-2605-21177:start -->The results demonstrate the effectiveness of \textsc{ChunkFT} in memory usage, running time, and optimization quality.<!-- delta:SF-2026-ARXIV-2605-21177:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21177:end -->

<!-- books-review:SF-2026-ARXIV-2605-21187:start -->
<!-- existing:SF-2026-ARXIV-2605-21187:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。第36章已覆盖 typed state transition、Context/Expert Parallel、异构/稀疏通信、bounded staleness、local work 与同步 fallback。`High-speed Networking for Giga-Scale AI Factories` 的 source-specific 机制是：We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21187:end -->
<!-- delta:SF-2026-ARXIV-2605-21187:start -->We describe the motivation, design principles, evaluation methodology and performance on state-of-the-art benchmarks, as well as the lessons we learned from deploying and debugging Spectrum-X networks in large-scale systems.<!-- delta:SF-2026-ARXIV-2605-21187:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21187:end -->

<!-- books-review:SF-2026-ARXIV-2605-21266:start -->
<!-- existing:SF-2026-ARXIV-2605-21266:start -->已顺读 `books/part-04-training-system/34-dpo.md` 与相邻章节 ['books/part-04-training-system/33-grpo.md', 'books/part-04-training-system/35-checkpoint.md']。第34章已拥有离线 pair objective、reference/beta/data coverage 与 online RL fallback，但尚未完整承载 federated/decentralized DPO 或最小 online warm-up 到 offline DPO 的 handoff；但 `How Much Online RL is Enough? Informative Rollouts for Offline Preference Optimization in RLVR` 所暴露的以下缺口尚未显式进入正文：online GRPO 可以只负责发现 informative state/rollout，再冻结 provenance-complete preference dataset 交给 offline DPO；handoff 以更少在线成本换 selection bias、staleness 与二阶段 objective mismatch。<!-- existing:SF-2026-ARXIV-2605-21266:end -->
<!-- delta:SF-2026-ARXIV-2605-21266:start -->online GRPO 可以只负责发现 informative state/rollout，再冻结 provenance-complete preference dataset 交给 offline DPO；handoff 以更少在线成本换 selection bias、staleness 与二阶段 objective mismatch。<!-- delta:SF-2026-ARXIV-2605-21266:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21266:end -->

<!-- books-review:SF-2026-ARXIV-2605-21273:start -->
<!-- existing:SF-2026-ARXIV-2605-21273:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope；但 `DriveMA: Rethinking Language Interfaces in Driving VLAs with One-Step Meta-Actions` 所暴露的以下缺口尚未显式进入正文：自然语言 reasoning 作为 driving action interface 会引入标注、延迟和 grounding bottleneck；one-step meta-action 将高层语义压成可执行 action schema，但必须保留坐标、低层控制和安全 envelope。<!-- existing:SF-2026-ARXIV-2605-21273:end -->
<!-- delta:SF-2026-ARXIV-2605-21273:start -->自然语言 reasoning 作为 driving action interface 会引入标注、延迟和 grounding bottleneck；one-step meta-action 将高层语义压成可执行 action schema，但必须保留坐标、低层控制和安全 envelope。<!-- delta:SF-2026-ARXIV-2605-21273:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21273:end -->

<!-- books-review:SF-2026-ARXIV-2605-21312:start -->
<!-- existing:SF-2026-ARXIV-2605-21312:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。第56章已拥有 request/KV/topology/SLO 联合 placement、routing 与 state-aware scheduling。`Frontier: Towards Comprehensive and Accurate LLM Inference Simulation` 的 source-specific 机制是：Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21312:end -->
<!-- delta:SF-2026-ARXIV-2605-21312:start -->Simulation is attractive for exploring this growing design space, yet existing simulators lack the architectural completeness and decision-grade fidelity it demands.<!-- delta:SF-2026-ARXIV-2605-21312:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21312:end -->

<!-- books-review:SF-2026-ARXIV-2605-21347:start -->
<!-- existing:SF-2026-ARXIV-2605-21347:start -->已顺读 `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节 ['books/part-06-ai-infrastructure/68-logging.md', 'books/part-06-ai-infrastructure/70-cost.md']。第69章已把 linear trace 演进为 root-cause graph，并分离 trace evidence、diagnostic hypothesis、repair authority 与 rerun evidence。`Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents` 的 source-specific 机制是：We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21347:end -->
<!-- delta:SF-2026-ARXIV-2605-21347:start -->We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report.<!-- delta:SF-2026-ARXIV-2605-21347:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21347:end -->

<!-- books-review:SF-2026-ARXIV-2605-21384:start -->
<!-- existing:SF-2026-ARXIV-2605-21384:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents` 的 source-specific 机制是：We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21384:end -->
<!-- delta:SF-2026-ARXIV-2605-21384:start -->We study this reward hacking phenomenon by decompose software engineering tasks into three parts: (i) a natural language description of the specification (ii) visible validation tests that exercise specified features in isolation, and (iii) held-out tests that compose those same features to simulate real-world usage.<!-- delta:SF-2026-ARXIV-2605-21384:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21384:end -->

<!-- books-review:SF-2026-ARXIV-2605-21392:start -->
<!-- existing:SF-2026-ARXIV-2605-21392:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']。第83章已把多 Server 权限提升为带 principal、server identity 与 taint 的端到端 information-flow contract，并保留 effect-time authorizer 与隔离 fallback。`VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers` 的 source-specific 机制是：In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21392:end -->
<!-- delta:SF-2026-ARXIV-2605-21392:start -->In this paper, we present VIPER-MCP, the first end-to-end automated vulnerability auditing framework for MCP servers that not only detects taint-style vulnerabilities but also dynamically confirms their exploitability by producing concrete proof-of-concept prompts.<!-- delta:SF-2026-ARXIV-2605-21392:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21392:end -->

<!-- books-review:SF-2026-ARXIV-2605-21427:start -->
<!-- existing:SF-2026-ARXIV-2605-21427:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power。`PALS: Power-Aware LLM Serving for Mixture-of-Experts Models` 的 source-specific 机制是：In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21427:end -->
<!-- delta:SF-2026-ARXIV-2605-21427:start -->In this paper, we present a power-aware runtime for LLM serving, PALS, that treats GPU power caps as a first-class control knob and jointly optimizes them with software parameters such as batch size.<!-- delta:SF-2026-ARXIV-2605-21427:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21427:end -->

<!-- books-review:SF-2026-ARXIV-2605-21434:start -->
<!-- existing:SF-2026-ARXIV-2605-21434:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Agentic Model Checking` 的 source-specific 机制是：We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21434:end -->
<!-- delta:SF-2026-ARXIV-2605-21434:start -->We propose agentic model checking, a paradigm that couples LLM agents with a bounded model checking backend under the principle agents propose, solvers verify: agents handle tasks requiring semantic judgment (spec inference, check selection, counterexample classification, refinement proposal) while BMC discharges every soundness-relevant decision.<!-- delta:SF-2026-ARXIV-2605-21434:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21434:end -->

<!-- books-review:SF-2026-ARXIV-2605-21446:start -->
<!-- existing:SF-2026-ARXIV-2605-21446:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。第26章已覆盖坐标系、action/trajectory schema、sensor freshness、闭环 correction、sim-to-real 与 safety envelope。`Lost in Fog: Sensor Perturbations Expose Reasoning Fragility in Driving VLAs` 的 source-specific 机制是：In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21446:end -->
<!-- delta:SF-2026-ARXIV-2605-21446:start -->In this paper we present a controlled perturbation study of Vision-Language-Action (VLA) robustness in autonomous driving, evaluating Alpamayo R1 (10B parameters) across 1,996 scenarios under eight sensor perturbations (Gaussian noise at four intensities, two lighting extremes, and two fog levels; ${\sim}18{,}000$ inference trials).<!-- delta:SF-2026-ARXIV-2605-21446:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21446:end -->

<!-- books-review:SF-2026-ARXIV-2605-21467:start -->
<!-- existing:SF-2026-ARXIV-2605-21467:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from Verifiable Rewards` 的 source-specific 机制是：We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21467:end -->
<!-- delta:SF-2026-ARXIV-2605-21467:start -->We introduce a discriminator view of RLVR updates, showing that the policy-gradient update direction implicitly acts as a linear discriminator over token-gradient vectors and thereby determines which token probabilities are increased or decreased during learning.<!-- delta:SF-2026-ARXIV-2605-21467:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21467:end -->

<!-- books-review:SF-2026-ARXIV-2605-21468:start -->
<!-- existing:SF-2026-ARXIV-2605-21468:start -->已顺读 `books/part-04-training-system/35-checkpoint.md` 与相邻章节 ['books/part-04-training-system/34-dpo.md', 'books/part-04-training-system/36-distributed-training.md']。第35章已拥有一致 checkpoint identity、commit/recovery 与可验证 artifact；尚未承载从短 RLVR 轨迹外推权重状态的条件分支；但 `You Only Need Minimal RLVR Training: Extrapolating LLMs via Rank-1 Trajectories` 所暴露的以下缺口尚未显式进入正文：短 RLVR weight trajectory 可作为低秩状态序列拟合并外推 checkpoint proposal；proposal 不能获得 artifact commit，必须由 held-out training/eval、数值稳定性和完整 checkpoint fallback 验收。<!-- existing:SF-2026-ARXIV-2605-21468:end -->
<!-- delta:SF-2026-ARXIV-2605-21468:start -->短 RLVR weight trajectory 可作为低秩状态序列拟合并外推 checkpoint proposal；proposal 不能获得 artifact commit，必须由 held-out training/eval、数值稳定性和完整 checkpoint fallback 验收。<!-- delta:SF-2026-ARXIV-2605-21468:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-21468:end -->

<!-- books-review:SF-2026-ARXIV-2605-21470:start -->
<!-- existing:SF-2026-ARXIV-2605-21470:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。第81章已拥有 versioned DAG、durable state、parallel commit、编译式 procedure 与 recovery contract。`Agent JIT Compilation for Latency-Optimizing Web Agent Planning and Scheduling` 的 source-specific 机制是：We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21470:end -->
<!-- delta:SF-2026-ARXIV-2605-21470:start -->We present agent just-in-time (JIT) compilation, a system that compiles task descriptions directly into executable code that may include LLM calls, tool calls, and parallelization.<!-- delta:SF-2026-ARXIV-2605-21470:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21470:end -->

<!-- books-review:SF-2026-ARXIV-2605-21482:start -->
<!-- existing:SF-2026-ARXIV-2605-21482:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`DeepWeb-Bench: A Deep Research Benchmark Demanding Massive Cross-Source Evidence and Long-Horizon Derivation` 的 source-specific 机制是：We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21482:end -->
<!-- delta:SF-2026-ARXIV-2605-21482:start -->We introduce DeepWeb-Bench, a deep research benchmark that is substantially harder than existing benchmarks for the current frontier.<!-- delta:SF-2026-ARXIV-2605-21482:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21482:end -->

<!-- books-review:SF-2026-ARXIV-2605-21486:start -->
<!-- existing:SF-2026-ARXIV-2605-21486:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Quantifying Hyperparameter Transfer and the Importance of Embedding Layer Learning Rate` 的 source-specific 机制是：In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21486:end -->
<!-- delta:SF-2026-ARXIV-2605-21486:start -->In this paper, we first develop a framework to quantify hyperparameter transfer through three metrics: (1) the quality of the scaling law fit, (2) the robustness to extrapolation errors, and (3) the asymptotic loss penalty due to choice of parameterization.<!-- delta:SF-2026-ARXIV-2605-21486:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21486:end -->

<!-- books-review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->
<!-- existing:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；owner 当前主干包含 ['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end -->
<!-- delta:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:start -->We further show that previously proposed auxiliary objectives, such as action-supervision, provably encourage latent actions to be consistent across exogenous states.<!-- delta:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-WHY-LATENT-ACTIONS-FAIL-AND-HOW-TO-PREVENT-IT:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260521-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260521 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260521-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260521-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=62；selected=3；all others retain completed reviews | passed |
| SA-20260521-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=599；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260521/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260521/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-21.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
