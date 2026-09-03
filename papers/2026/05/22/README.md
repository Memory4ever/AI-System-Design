# Daily Research — 2026-05-22

**Research Date:** 2026-05-22

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-21 09:00:00 ～ 2026-05-22 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 667 个注册 arXiv identity，冻结 70 个 Source Family；pre-denominator closure=597，withdrawn pre-denominator=0。15 个旧候选被迁回正确 owner day，0 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-22 |
| Window End | 2026-05-22 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260522-CREATED-412a836c709189e0 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-21T09:00:00+08:00 | 2026-05-22T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 667 | SF-2026-ARXIV-2605-21516;SF-2026-ARXIV-2605-21543;SF-2026-ARXIV-2605-21602;SF-2026-ARXIV-2605-21603;SF-2026-ARXIV-2605-21606;SF-2026-ARXIV-2605-21642;SF-2026-ARXIV-2605-21648;SF-2026-ARXIV-2605-21649;SF-2026-ARXIV-2605-21768;SF-2026-ARXIV-2605-21779;SF-2026-ARXIV-2605-21800;SF-2026-ARXIV-2605-21801;SF-2026-ARXIV-2605-21803;SF-2026-ARXIV-2605-21847;SF-2026-ARXIV-2605-21850;SF-2026-ARXIV-2605-21854;SF-2026-ARXIV-2605-21856;SF-2026-ARXIV-2605-21862;SF-2026-ARXIV-2605-21949;SF-2026-ARXIV-2605-21951;SF-2026-ARXIV-2605-21965;SF-2026-ARXIV-2605-21996;SF-2026-ARXIV-2605-21997;SF-2026-ARXIV-2605-22001;SF-2026-ARXIV-2605-22014;SF-2026-ARXIV-2605-22041;SF-2026-ARXIV-2605-22057;SF-2026-ARXIV-2605-22074;SF-2026-ARXIV-2605-22102;SF-2026-ARXIV-2605-22106;SF-2026-ARXIV-2605-22138;SF-2026-ARXIV-2605-22148;SF-2026-ARXIV-2605-22154;SF-2026-ARXIV-2605-22164;SF-2026-ARXIV-2605-22166;SF-2026-ARXIV-2605-22177;SF-2026-ARXIV-2605-22217;SF-2026-ARXIV-2605-22219;SF-2026-ARXIV-2605-22269;SF-2026-ARXIV-2605-22283;SF-2026-ARXIV-2605-22297;SF-2026-ARXIV-2605-22321;SF-2026-ARXIV-2605-22333;SF-2026-ARXIV-2605-22337;SF-2026-ARXIV-2605-22343;SF-2026-ARXIV-2605-22411;SF-2026-ARXIV-2605-22416;SF-2026-ARXIV-2605-22446;SF-2026-ARXIV-2605-22456;SF-2026-ARXIV-2605-22493;SF-2026-ARXIV-2605-22502;SF-2026-ARXIV-2605-22505;SF-2026-ARXIV-2605-22511;SF-2026-ARXIV-2605-22526;SF-2026-ARXIV-2605-22544;SF-2026-ARXIV-2605-22564;SF-2026-ARXIV-2605-22566;SF-2026-ARXIV-2605-22568;SF-2026-ARXIV-2605-22608;SF-2026-ARXIV-2605-22620;SF-2026-ARXIV-2605-22634;SF-2026-ARXIV-2605-22643;SF-2026-ARXIV-2605-22718;SF-2026-ARXIV-2605-22721;SF-2026-ARXIV-2605-22731;SF-2026-ARXIV-2605-22769;SF-2026-ARXIV-2605-22781;SF-2026-ARXIV-2605-22786;SF-2026-ARXIV-2605-22794;SF-2026-ARXIV-2605-22800 | created-day pages=closed; OAI category sets=closed; direct same-day OAI=513 | 2026-05-22T09:00:00+08:00 | coverage:SRC-ARXIV:20260522 | — |

<!-- coverage:SRC-ARXIV:20260522:start -->全量 raw inventory=667；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260522:end -->

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
| SF-2026-ARXIV-2605-21516 | arXiv:2605.21516v1 | paper-v1:2605.21516 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21516 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21516 | no |
| SF-2026-ARXIV-2605-21543 | arXiv:2605.21543v1 | paper-v1:2605.21543 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21543 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21543 | no |
| SF-2026-ARXIV-2605-21602 | arXiv:2605.21602v1 | paper-v1:2605.21602 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21602 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21602 | no |
| SF-2026-ARXIV-2605-21603 | arXiv:2605.21603v1 | paper-v1:2605.21603 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21603 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21603 | no |
| SF-2026-ARXIV-2605-21606 | arXiv:2605.21606v1 | paper-v1:2605.21606 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21606 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21606 | no |
| SF-2026-ARXIV-2605-21642 | arXiv:2605.21642v1 | paper-v1:2605.21642 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21642 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21642 | no |
| SF-2026-ARXIV-2605-21648 | arXiv:2605.21648v1 | paper-v1:2605.21648 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21648 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21648 | no |
| SF-2026-ARXIV-2605-21649 | arXiv:2605.21649v1 | paper-v1:2605.21649 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21649 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21649 | no |
| SF-2026-ARXIV-2605-21768 | arXiv:2605.21768v1 | paper-v1:2605.21768 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21768 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21768 | no |
| SF-2026-ARXIV-2605-21779 | arXiv:2605.21779v1 | paper-v1:2605.21779 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21779 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21779 | no |
| SF-2026-ARXIV-2605-21800 | arXiv:2605.21800v1 | paper-v1:2605.21800 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21800 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21800 | no |
| SF-2026-ARXIV-2605-21801 | arXiv:2605.21801v1 | paper-v1:2605.21801 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21801 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21801 | no |
| SF-2026-ARXIV-2605-21803 | arXiv:2605.21803v1 | paper-v1:2605.21803 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21803 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21803 | no |
| SF-2026-ARXIV-2605-21847 | arXiv:2605.21847v1 | paper-v1:2605.21847 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21847 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21847 | no |
| SF-2026-ARXIV-2605-21850 | arXiv:2605.21850v1 | paper-v1:2605.21850 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21850 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21850 | no |
| SF-2026-ARXIV-2605-21854 | arXiv:2605.21854v1 | paper-v1:2605.21854 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21854 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21854 | no |
| SF-2026-ARXIV-2605-21856 | arXiv:2605.21856v1 | paper-v1:2605.21856 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21856 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21856 | no |
| SF-2026-ARXIV-2605-21862 | arXiv:2605.21862v1 | paper-v1:2605.21862 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21862 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21862 | no |
| SF-2026-ARXIV-2605-21949 | arXiv:2605.21949v1 | paper-v1:2605.21949 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21949 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21949 | no |
| SF-2026-ARXIV-2605-21951 | arXiv:2605.21951v1 | paper-v1:2605.21951 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-21951 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-21951 | no |
| SF-2026-ARXIV-2605-21965 | arXiv:2605.21965v1 | paper-v1:2605.21965 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21965 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21965 | no |
| SF-2026-ARXIV-2605-21996 | arXiv:2605.21996v1 | paper-v1:2605.21996 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21996 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21996 | no |
| SF-2026-ARXIV-2605-21997 | arXiv:2605.21997v1 | paper-v1:2605.21997 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21997 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21997 | no |
| SF-2026-ARXIV-2605-22001 | arXiv:2605.22001v1 | paper-v1:2605.22001 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22001 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22001 | no |
| SF-2026-ARXIV-2605-22014 | arXiv:2605.22014v1 | paper-v1:2605.22014 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22014 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22014 | no |
| SF-2026-ARXIV-2605-22041 | arXiv:2605.22041v1 | paper-v1:2605.22041 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22041 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22041 | no |
| SF-2026-ARXIV-2605-22057 | arXiv:2605.22057v1 | paper-v1:2605.22057 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22057 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22057 | no |
| SF-2026-ARXIV-2605-22074 | arXiv:2605.22074v1 | paper-v1:2605.22074 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22074 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-22074 | no |
| SF-2026-ARXIV-2605-22102 | arXiv:2605.22102v1 | paper-v1:2605.22102 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22102 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22102 | no |
| SF-2026-ARXIV-2605-22106 | arXiv:2605.22106v1 | paper-v1:2605.22106 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22106 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22106 | no |
| SF-2026-ARXIV-2605-22138 | arXiv:2605.22138v1 | paper-v1:2605.22138 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22138 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22138 | no |
| SF-2026-ARXIV-2605-22148 | arXiv:2605.22148v1 | paper-v1:2605.22148 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22148 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22148 | no |
| SF-2026-ARXIV-2605-22154 | arXiv:2605.22154v1 | paper-v1:2605.22154 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22154 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22154 | no |
| SF-2026-ARXIV-2605-22164 | arXiv:2605.22164v1 | paper-v1:2605.22164 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22164 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-22164 | no |
| SF-2026-ARXIV-2605-22166 | arXiv:2605.22166v1 | paper-v1:2605.22166 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22166 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22166 | no |
| SF-2026-ARXIV-2605-22177 | arXiv:2605.22177v1 | paper-v1:2605.22177 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22177 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22177 | no |
| SF-2026-ARXIV-2605-22217 | arXiv:2605.22217v1 | paper-v1:2605.22217 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22217 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22217 | no |
| SF-2026-ARXIV-2605-22219 | arXiv:2605.22219v1 | paper-v1:2605.22219 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22219 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22219 | no |
| SF-2026-ARXIV-2605-22269 | arXiv:2605.22269v1 | paper-v1:2605.22269 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22269 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22269 | no |
| SF-2026-ARXIV-2605-22283 | arXiv:2605.22283v1 | paper-v1:2605.22283 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22283 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22283 | no |
| SF-2026-ARXIV-2605-22297 | arXiv:2605.22297v1 | paper-v1:2605.22297 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22297 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22297 | no |
| SF-2026-ARXIV-2605-22321 | arXiv:2605.22321v1 | paper-v1:2605.22321 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22321 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22321 | no |
| SF-2026-ARXIV-2605-22333 | arXiv:2605.22333v1 | paper-v1:2605.22333 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22333 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22333 | no |
| SF-2026-ARXIV-2605-22337 | arXiv:2605.22337v1 | paper-v1:2605.22337 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22337 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22337 | no |
| SF-2026-ARXIV-2605-22343 | arXiv:2605.22343v1 | paper-v1:2605.22343 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22343 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-22343 | no |
| SF-2026-ARXIV-2605-22411 | arXiv:2605.22411v1 | paper-v1:2605.22411 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22411 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22411 | no |
| SF-2026-ARXIV-2605-22416 | arXiv:2605.22416v1 | paper-v1:2605.22416 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22416 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-22416 | no |
| SF-2026-ARXIV-2605-22446 | arXiv:2605.22446v1 | paper-v1:2605.22446 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22446 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22446 | no |
| SF-2026-ARXIV-2605-22456 | arXiv:2605.22456v1 | paper-v1:2605.22456 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22456 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22456 | no |
| SF-2026-ARXIV-2605-22493 | arXiv:2605.22493v1 | paper-v1:2605.22493 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22493 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2605-22493 | no |
| SF-2026-ARXIV-2605-22502 | arXiv:2605.22502v1 | paper-v1:2605.22502 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22502 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22502 | no |
| SF-2026-ARXIV-2605-22505 | arXiv:2605.22505v1 | paper-v1:2605.22505 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22505 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-22505 | no |
| SF-2026-ARXIV-2605-22511 | arXiv:2605.22511v1 | paper-v1:2605.22511 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22511 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22511 | no |
| SF-2026-ARXIV-2605-22526 | arXiv:2605.22526v1 | paper-v1:2605.22526 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22526 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22526 | no |
| SF-2026-ARXIV-2605-22544 | arXiv:2605.22544v1 | paper-v1:2605.22544 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22544 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22544 | no |
| SF-2026-ARXIV-2605-22564 | arXiv:2605.22564v1 | paper-v1:2605.22564 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22564 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22564 | no |
| SF-2026-ARXIV-2605-22566 | arXiv:2605.22566v1 | paper-v1:2605.22566 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22566 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22566 | no |
| SF-2026-ARXIV-2605-22568 | arXiv:2605.22568v1 | paper-v1:2605.22568 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22568 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22568 | no |
| SF-2026-ARXIV-2605-22608 | arXiv:2605.22608v1 | paper-v1:2605.22608 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22608 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22608 | no |
| SF-2026-ARXIV-2605-22620 | arXiv:2605.22620v1 | paper-v1:2605.22620 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22620 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-22620 | no |
| SF-2026-ARXIV-2605-22634 | arXiv:2605.22634v1 | paper-v1:2605.22634 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22634 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22634 | no |
| SF-2026-ARXIV-2605-22643 | arXiv:2605.22643v1 | paper-v1:2605.22643 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22643 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22643 | no |
| SF-2026-ARXIV-2605-22718 | arXiv:2605.22718v1 | paper-v1:2605.22718 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22718 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22718 | no |
| SF-2026-ARXIV-2605-22721 | arXiv:2605.22721v1 | paper-v1:2605.22721 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22721 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-22721 | no |
| SF-2026-ARXIV-2605-22731 | arXiv:2605.22731v1 | paper-v1:2605.22731 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22731 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-22731 | no |
| SF-2026-ARXIV-2605-22769 | arXiv:2605.22769v1 | paper-v1:2605.22769 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22769 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-22769 | no |
| SF-2026-ARXIV-2605-22781 | arXiv:2605.22781v1 | paper-v1:2605.22781 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22781 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22781 | no |
| SF-2026-ARXIV-2605-22786 | arXiv:2605.22786v1 | paper-v1:2605.22786 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22786 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22786 | no |
| SF-2026-ARXIV-2605-22794 | arXiv:2605.22794v1 | paper-v1:2605.22794 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22794 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-22794 | no |
| SF-2026-ARXIV-2605-22800 | arXiv:2605.22800v1 | paper-v1:2605.22800 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22800 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-22800 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-21516 | RP-d31fc51c95c04a92 | deep | arXiv:2605.21516v1 | SRC-ARXIV@arXiv:2605.21516v1 | arXiv:2605.21516v1 — Methodology: 4 Alignment Principles for Harness Design (official v1 HTML) | arXiv:2605.21516v1 — Experiments: 5 Experiments (official v1 HTML) | arXiv:2605.21516v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.21516.txt#sha256=23cb65eefbe8e2c0a132169a1e50766b0da3b97715b5cfcfe529bc020caa1946; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-21516 | complete |
| SF-2026-ARXIV-2605-21543 | RP-240d9ad303a50e90 | deep | arXiv:2605.21543v1 | SRC-ARXIV@arXiv:2605.21543v1 | arXiv:2605.21543v1 HTML — §3 Joint Decontamination Procedure | arXiv:2605.21543v1 HTML — §4 Controlled Experiments | arXiv:2605.21543v1 HTML — §6 Limitations | https://arxiv.org/html/2605.21543v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21543 | complete |
| SF-2026-ARXIV-2605-21602 | RP-5c335c79eba9f41d | deep | arXiv:2605.21602v1 | SRC-ARXIV@arXiv:2605.21602v1 | arXiv:2605.21602v1 HTML — §3 MOOD Benchmark and Monitor Design | arXiv:2605.21602v1 HTML — §5 Experiments | arXiv:2605.21602v1 HTML — §6 Conclusion and stated monitor limitations | https://arxiv.org/html/2605.21602v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21602 | complete |
| SF-2026-ARXIV-2605-21603 | RP-23d10aa259ab99cb | deep | arXiv:2605.21603v1 | SRC-ARXIV@arXiv:2605.21603v1 | arXiv:2605.21603v1 HTML — §3 Programmable Operator Scheduling | arXiv:2605.21603v1 HTML — §5 Evaluation | arXiv:2605.21603v1 HTML — §7 Conclusion and evaluated-hardware boundary | https://arxiv.org/html/2605.21603v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21603 | complete |
| SF-2026-ARXIV-2605-21606 | RP-94d88674b6729336 | deep | arXiv:2605.21606v1 | SRC-ARXIV@arXiv:2605.21606v1 | arXiv:2605.21606v1 HTML — §3 Method; §Appendix F Adaptive-loss template and method comparison; §Appendix G PW-OPSD training pseudocode | arXiv:2605.21606v1 HTML — §4 Experiments; §Evaluation.; §4.2 Main results on Qwen3-4B | arXiv:2605.21606v1 HTML — §5 Conclusion, Limitations, and Future Work | https://arxiv.org/html/2605.21606v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21606 | complete |
| SF-2026-ARXIV-2605-21642 | RP-275b7a7e2d099140 | deep | arXiv:2605.21642v1 | SRC-ARXIV@arXiv:2605.21642v1 | arXiv:2605.21642v1 HTML — §3 Method; §Training objective.; §4.2 Training and implementation details | arXiv:2605.21642v1 HTML — §4 Experiments; §4.1 Task and evaluation protocol; §Depth reasoning benchmark. | arXiv:2605.21642v1 HTML — §5 Discussion | https://arxiv.org/html/2605.21642v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21642 | complete |
| SF-2026-ARXIV-2605-21648 | RP-f266b39ac8de3782 | deep | arXiv:2605.21648v1 | SRC-ARXIV@arXiv:2605.21648v1 | arXiv:2605.21648v1 HTML — §1 Introduction — exact-v1 disclosed mechanism | arXiv:2605.21648v1 HTML — §Appendix D Experimental Details and Additional Figures; §D.2 Dropout Scheduling Experiments | arXiv:2605.21648v1 HTML — §4 Conclusions and further scope for research; §5 Limitations | https://arxiv.org/html/2605.21648v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21648 | complete |
| SF-2026-ARXIV-2605-21649 | RP-b190dea5c29b3ff4 | deep | arXiv:2605.21649v1 | SRC-ARXIV@arXiv:2605.21649v1 | arXiv:2605.21649v1 HTML — §4 EntmaxKV | arXiv:2605.21649v1 HTML — §5 Experiments; §5.1 Approximation Error Analysis | arXiv:2605.21649v1 HTML — §7 Conclusion — exact-v1 workload/model boundary | https://arxiv.org/html/2605.21649v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21649 | complete |
| SF-2026-ARXIV-2605-21768 | RP-54025a8a20fcd5fe | deep | arXiv:2605.21768v1 | SRC-ARXIV@arXiv:2605.21768v1 | arXiv:2605.21768v1 HTML — §2.1 Memory Agent Architectures; §3 Method; §3.1 Problem Formulation: Multi-step Memory Bank Construction | arXiv:2605.21768v1 HTML — §4 Experiments; §4.1 Experiment Setup; §Datasets and Evaluation Metrics. | arXiv:2605.21768v1 HTML — §5 Conclusion; §Appendix D Limitations and Future Work | https://arxiv.org/html/2605.21768v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21768 | complete |
| SF-2026-ARXIV-2605-21779 | RP-fec479e5e05a9e29 | deep | arXiv:2605.21779v1 | SRC-ARXIV@arXiv:2605.21779v1 | arXiv:2605.21779v1 HTML — §3 FuzzingBrain V2 Architecture | arXiv:2605.21779v1 HTML — §5 Evaluation | arXiv:2605.21779v1 HTML — §6.1 Limitations | https://arxiv.org/html/2605.21779v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21779 | complete |
| SF-2026-ARXIV-2605-21800 | RP-c0a3e8251ce537c7 | deep | arXiv:2605.21800v1 | SRC-ARXIV@arXiv:2605.21800v1 | arXiv:2605.21800v1 HTML — §3 stable-worldmodel Platform | arXiv:2605.21800v1 HTML — §4 Case Studies | arXiv:2605.21800v1 HTML — §6 Conclusion and Future Work | https://arxiv.org/html/2605.21800v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21800 | complete |
| SF-2026-ARXIV-2605-21801 | RP-e20f2a7609541c11 | deep | arXiv:2605.21801v1 | SRC-ARXIV@arXiv:2605.21801v1 | arXiv:2605.21801v1 HTML — §E.3 Training Details | arXiv:2605.21801v1 HTML — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Experiment | arXiv:2605.21801v1 HTML — §5 Conclusion; §Conclusion.; §D.8 Discussion: Dataset-dependent Effects | https://arxiv.org/html/2605.21801v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21801 | complete |
| SF-2026-ARXIV-2605-21803 | RP-d1d250ebab119a51 | deep | arXiv:2605.21803v1 | SRC-ARXIV@arXiv:2605.21803v1 | arXiv:2605.21803v1 HTML — §Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws; §Architecture–optimizer interaction.; §3 Methodology | arXiv:2605.21803v1 HTML — §Experimental setup; §Appendix A Experimental Setup; §Appendix C Rényi Effective Rank Analysis: Where Optimizer-Induced Capacity Forms | arXiv:2605.21803v1 HTML — §5 Discussion and Conclusion | https://arxiv.org/html/2605.21803v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21803 | complete |
| SF-2026-ARXIV-2605-21847 | RP-172fe52bc1cab11d | deep | arXiv:2605.21847v1 | SRC-ARXIV@arXiv:2605.21847v1 | arXiv:2605.21847v1 HTML — §3 Component-Level Power Control | arXiv:2605.21847v1 HTML — §6 Evaluation | arXiv:2605.21847v1 HTML — §7 Conclusion and evaluated-GPU boundary | https://arxiv.org/html/2605.21847v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21847 | complete |
| SF-2026-ARXIV-2605-21850 | RP-1b7b40febca5e56b | deep | arXiv:2605.21850v1 | SRC-ARXIV@arXiv:2605.21850v1 | arXiv:2605.21850v1 HTML — §3 Agent-Trajectory Compilation | arXiv:2605.21850v1 HTML — §4 Experiments | arXiv:2605.21850v1 HTML — §6 Limitations and Social Impacts | https://arxiv.org/html/2605.21850v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-21850 | complete |
| SF-2026-ARXIV-2605-21854 | RP-f333f5a60c816e98 | deep | arXiv:2605.21854v1 | SRC-ARXIV@arXiv:2605.21854v1 | arXiv:2605.21854v1 HTML — §3 Cross-Paradigm VLA Interface and Surrogate Log-Probability | arXiv:2605.21854v1 HTML — §4 Experiments; §4.5 Inference Anatomy | arXiv:2605.21854v1 HTML — §5.2 Non-transfer of Inference Caching; §6 Limitations | https://arxiv.org/html/2605.21854v1; sha256:18e9186cc05a8e8291cc9eb36fbe2eb828d79aa02a6c96845c9126bbc9ed2924 | claim:SF-2026-ARXIV-2605-21854 | complete |
| SF-2026-ARXIV-2605-21856 | RP-cdbb5bb1a5711387 | deep | arXiv:2605.21856v1 | SRC-ARXIV@arXiv:2605.21856v1 | arXiv:2605.21856v1 HTML — §3 Method; §3.1 Problem Formulation; §3.2 Limitations of Existing Detection Methods in Evasive Scenarios | arXiv:2605.21856v1 HTML — §4 Experiments; §4.1 Experiments on Existing Models; §4.1.1 Results and Analysis | arXiv:2605.21856v1 HTML — §3.2 Limitations of Existing Detection Methods in Evasive Scenarios; §5 Conclusion Limitation | https://arxiv.org/html/2605.21856v1; sha256:cc0004827e00e3055ddb2883c17040a94b93b2eafc5083349501848398c2d0b6 | claim:SF-2026-ARXIV-2605-21856 | complete |
| SF-2026-ARXIV-2605-21862 | RP-280d3330f02c3a41 | deep | arXiv:2605.21862v1 | SRC-ARXIV@arXiv:2605.21862v1 | arXiv:2605.21862v1 HTML — §3 Evolving Scene Beliefs in the Action Decoder | arXiv:2605.21862v1 HTML — §4 Experiments | arXiv:2605.21862v1 HTML — Appendix F Limitations | https://arxiv.org/html/2605.21862v1; sha256:12f60d2629aa8c413c794b1b705bbe43641a63ae8024cdc1ede3cb132711b449 | claim:SF-2026-ARXIV-2605-21862 | complete |
| SF-2026-ARXIV-2605-21949 | RP-0e0d8e6b5c6d68a3 | deep | arXiv:2605.21949v1 | SRC-ARXIV@arXiv:2605.21949v1 | arXiv:2605.21949v1 HTML — §3 Problem Formulation; §4 Method | arXiv:2605.21949v1 HTML — §5 Experiments; §5.1 Data Provenance and Main Evaluation Split; §5.4 Evaluation Protocol and Label–Policy Separation | arXiv:2605.21949v1 HTML — §6.3 Abstract-Style Transfer Behavior and Failure Modes; §7 Discussion; §8 Limitations | https://arxiv.org/html/2605.21949v1; sha256:8416357e10590c97a701341111ab0ca3b665d678c94aa4d9c36d55f7f30ee87e | claim:SF-2026-ARXIV-2605-21949 | complete |
| SF-2026-ARXIV-2605-21951 | RP-675c69b91478e932 | deep | arXiv:2605.21951v1 | SRC-ARXIV@arXiv:2605.21951v1 | arXiv:2605.21951v1 HTML — §3 Dynamic Mixture of Latent Memories | arXiv:2605.21951v1 HTML — §4 Experiments | arXiv:2605.21951v1 HTML — §5 Discussion and static-capacity/forgetting boundary | https://arxiv.org/html/2605.21951v1; sha256:ae6cc1fe4b7910a8e1c25a32bd6f8ec181bc884b2957efbaf0666ee81745c4d9 | claim:SF-2026-ARXIV-2605-21951 | complete |
| SF-2026-ARXIV-2605-21965 | RP-5180ed978c11ba4d | deep | arXiv:2605.21965v1 | SRC-ARXIV@arXiv:2605.21965v1 | arXiv:2605.21965v1 HTML — §3 SpecHop Continuous Speculation | arXiv:2605.21965v1 HTML — §4 Multi-Hop Retrieval Evaluation | arXiv:2605.21965v1 HTML — §5 Conclusion and speculation-misprediction boundary | https://arxiv.org/html/2605.21965v1; sha256:544f65f79b5ceeddcb806e3cc88ad14f198fdc40f365edefb3d8b4cc3f6babbe | claim:SF-2026-ARXIV-2605-21965 | complete |
| SF-2026-ARXIV-2605-21996 | RP-53c5a426ac80d916 | deep | arXiv:2605.21996v1 | SRC-ARXIV@arXiv:2605.21996v1 | arXiv:2605.21996v1 HTML — §4 Method; §Appendix G Full curation algorithm; §Appendix J Training details | arXiv:2605.21996v1 HTML — §5 Experiments; §5.1 Experimental Setup; §Results (interventional). | arXiv:2605.21996v1 HTML — §6 Conclusion; §Appendix L Limitations and outlook; §Limitations. | https://arxiv.org/html/2605.21996v1; sha256:f452614a9127137ed1f912fc0c559750f4b20d098c1ba85872052e7492b19ece | claim:SF-2026-ARXIV-2605-21996 | complete |
| SF-2026-ARXIV-2605-21997 | RP-1c52ec02b8006a85 | deep | arXiv:2605.21997v1 | SRC-ARXIV@arXiv:2605.21997v1 | arXiv:2605.21997v1 HTML — §3 Event-Sourced Reactive Graph Model | arXiv:2605.21997v1 HTML — §6 Evaluation and Fork/Replay Cases | arXiv:2605.21997v1 HTML — §9 Limitations and Conclusion | https://arxiv.org/html/2605.21997v1; sha256:4751c925e420b07bddefa40aaca8440bf418ec6aaa9e9e689074c59c25114ebb | claim:SF-2026-ARXIV-2605-21997 | complete |
| SF-2026-ARXIV-2605-22001 | RP-afca4feed9b4480e | deep | arXiv:2605.22001v1 | SRC-ARXIV@arXiv:2605.22001v1 | arXiv:2605.22001v1 HTML — §Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems; §4 Method; §4.3 Agent Architectures | arXiv:2605.22001v1 HTML — §Prompt injection attacks and benchmarks.; §5 Experiments and Results; §6 Analysis | arXiv:2605.22001v1 HTML — §6.1 The Failure Mode is Confident, Not Uncertain; §7 Conclusion; §Limitations | https://arxiv.org/html/2605.22001v1; sha256:b1adad4719d0940541d1d4b82da2601b098774d37c630e58bb951885ff2040cd | claim:SF-2026-ARXIV-2605-22001 | complete |
| SF-2026-ARXIV-2605-22014 | RP-142af44e2a91e502 | deep | arXiv:2605.22014v1 | SRC-ARXIV@arXiv:2605.22014v1 | arXiv:2605.22014v1 HTML — §4 LiveR Dual-World Reconfiguration Runtime | arXiv:2605.22014v1 HTML — §6 Evaluation | arXiv:2605.22014v1 HTML — §7 Discussion and live-resharding boundary | https://arxiv.org/html/2605.22014v1; sha256:781be436a12291a3d0d7d1739d53c018fc141b0319b6f2604dd1ddde81c9dc87 | claim:SF-2026-ARXIV-2605-22014 | complete |
| SF-2026-ARXIV-2605-22041 | RP-46f07b7a8bc058cc | deep | arXiv:2605.22041v1 | SRC-ARXIV@arXiv:2605.22041v1 | arXiv:2605.22041v1 HTML — §3 RADAR Dynamic Retrieval-Corruption Defense | arXiv:2605.22041v1 HTML — §4–§5 Attack and Defense Evaluation | arXiv:2605.22041v1 HTML — §6 Conclusion and adaptive-attacker boundary | https://arxiv.org/html/2605.22041v1; sha256:64b75669ea0965f176d205ab85117e15274543eac61530336cf7ecfedc08a71d | claim:SF-2026-ARXIV-2605-22041 | complete |
| SF-2026-ARXIV-2605-22057 | RP-05cc1c74c85d31fe | deep | arXiv:2605.22057v1 | SRC-ARXIV@arXiv:2605.22057v1 | arXiv:2605.22057v1 HTML — §3 Method; §Task formulation.; §Appendix A Illustrative Training Queries | arXiv:2605.22057v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.22057v1 HTML — §5 Conclusion; §Limitations | https://arxiv.org/html/2605.22057v1; sha256:ec4a4601f8e2674837ae7cd1d5dce9e0992db4ac733938f7e8558650f1148066 | claim:SF-2026-ARXIV-2605-22057 | complete |
| SF-2026-ARXIV-2605-22074 | RP-477990809bce023e | deep | arXiv:2605.22074v1 | SRC-ARXIV@arXiv:2605.22074v1 | arXiv:2605.22074v1 HTML — §3 Verifiable-Subproblem Curriculum Construction | arXiv:2605.22074v1 HTML — §4–§5 RL Credit-Assignment Evaluation | arXiv:2605.22074v1 HTML — Appendix G Limitations and Future Work | https://arxiv.org/html/2605.22074v1; sha256:ab1e5e5fd19cbf65b70a338ba9230d6d98604ea33d65abd326859fb024a0b8d1 | claim:SF-2026-ARXIV-2605-22074 | complete |
| SF-2026-ARXIV-2605-22102 | RP-02a49fc386002572 | deep | arXiv:2605.22102v1 | SRC-ARXIV@arXiv:2605.22102v1 | arXiv:2605.22102v1 HTML — §1 Introduction — disclosed mechanism | arXiv:2605.22102v1 HTML — §4 Experiments; §4.1 Main Results; §4.2 Error Recovery Analysis | arXiv:2605.22102v1 HTML — §5 Conclusion; §Appendix A Further Discussions; §A.2 Limitations and Future Work | https://arxiv.org/html/2605.22102v1; sha256:2fd539607c08a60904f2b21d4a8dfdc8e7edc23fdbcb334fdd744220513d4300 | claim:SF-2026-ARXIV-2605-22102 | complete |
| SF-2026-ARXIV-2605-22106 | RP-1ace6bd99dd42577 | deep | arXiv:2605.22106v1 | SRC-ARXIV@arXiv:2605.22106v1 | arXiv:2605.22106v1 HTML — §3 ArborKV Thought-Block Cache Model | arXiv:2605.22106v1 HTML — §5 Tree-Reasoning Serving Evaluation | arXiv:2605.22106v1 HTML — §6 Discussion and search-dynamics boundary | https://arxiv.org/html/2605.22106v1; sha256:dd92adfdc18af871ca7c8794bbf78a91516bcf0442986773496665899c7ee830 | claim:SF-2026-ARXIV-2605-22106 | complete |
| SF-2026-ARXIV-2605-22138 | RP-5d85af738cff89bb | deep | arXiv:2605.22138v1 | SRC-ARXIV@arXiv:2605.22138v1 | arXiv:2605.22138v1 HTML — §Approach 1: Multi-Module Inference (v0.1); §Approach 2: Plan Reconstruction (v1.0); §3.4 Training Data and Hyperparameters | arXiv:2605.22138v1 HTML — §4 Experiments; §4.1 Experiment Setup; §Evaluation Benchmarks | arXiv:2605.22138v1 HTML — §6 Conclusion; §7 Limitations and Future Work | https://arxiv.org/html/2605.22138v1; sha256:08a5d8670415792a34a4aefdf40f8a4be4002ee5cd18910b88e34fc140b47365 | claim:SF-2026-ARXIV-2605-22138 | complete |
| SF-2026-ARXIV-2605-22148 | RP-e0d4650225646446 | deep | arXiv:2605.22148v1 | SRC-ARXIV@arXiv:2605.22148v1 | arXiv:2605.22148v1 HTML — §3 Ratchet Skill Admission/Retirement Recipe | arXiv:2605.22148v1 HTML — §5 Agent Evaluation | arXiv:2605.22148v1 HTML — §6 Limitations: amplifier, not discoverer | https://arxiv.org/html/2605.22148v1; sha256:87019037949ccd4b7d5cb45b45f774bc1c9405ad9a1ca76509bc67f762a971ba | claim:SF-2026-ARXIV-2605-22148 | complete |
| SF-2026-ARXIV-2605-22154 | RP-7419b3ac088acaaa | deep | arXiv:2605.22154v1 | SRC-ARXIV@arXiv:2605.22154v1 | arXiv:2605.22154v1 HTML — §4 IdleSpec Drafting, Aggregation, and Posterior Update | arXiv:2605.22154v1 HTML — §5 Experiments | arXiv:2605.22154v1 HTML — Appendix A.7 Limitations | https://arxiv.org/html/2605.22154v1; sha256:55cc67e9ee2b67b8752f7ef27450ef14457b3381ab93855fb38b314a9686f178 | claim:SF-2026-ARXIV-2605-22154 | complete |
| SF-2026-ARXIV-2605-22164 | RP-8ae62c377f45fd31 | deep | arXiv:2605.22164v1 | SRC-ARXIV@arXiv:2605.22164v1 | arXiv:2605.22164v1 HTML — §4 Method: Trajectory Reachability Metrics ( TRM ); §Training environment versus benchmark leakage.; §Appendix A Appendix: TRM Method Details | arXiv:2605.22164v1 HTML — §5 Experimental Protocol; §Evaluation and reporting.; §6 Results | arXiv:2605.22164v1 HTML — §7 Discussion; §8 Limitations; §9 Conclusion | https://arxiv.org/html/2605.22164v1; sha256:f942f43e655906f0276148bfbbc385fd2d5167c40bd891b2e61102beccf098f2 | claim:SF-2026-ARXIV-2605-22164 | complete |
| SF-2026-ARXIV-2605-22166 | RP-d39dbd241080daa6 | deep | arXiv:2605.22166v1 | SRC-ARXIV@arXiv:2605.22166v1 | arXiv:2605.22166v1 HTML — §3 Runtime Harness Adaptation | arXiv:2605.22166v1 HTML — §5 Deterministic-Agent Evaluation | arXiv:2605.22166v1 HTML — §7 Limitations | https://arxiv.org/html/2605.22166v1; sha256:fa72e0ba19b1eab39c0ca6018fe1ef29787b2459f8ffec465d88f5ada5244af6 | claim:SF-2026-ARXIV-2605-22166 | complete |
| SF-2026-ARXIV-2605-22177 | RP-b21dc4974de41d13 | deep | arXiv:2605.22177v1 | SRC-ARXIV@arXiv:2605.22177v1 | arXiv:2605.22177v1 HTML — §3 Method; §3.2 Problem Formulation; §Training Data. | arXiv:2605.22177v1 HTML — §4 Experiments; §4.1 Experimental Setup; §Benchmarks and Metrics. | arXiv:2605.22177v1 HTML — §4.5 Discussion on Realistic Agentic Benchmarks; §5 Conclusion; §E.4 Additional Discussion | https://arxiv.org/html/2605.22177v1; sha256:df375605ccd9949ed7b3948657f41431fd73b9744b7bd484e0bbd86e5c032172 | claim:SF-2026-ARXIV-2605-22177 | complete |
| SF-2026-ARXIV-2605-22217 | RP-4b2638e714c2e4ac | deep | arXiv:2605.22217v1 | SRC-ARXIV@arXiv:2605.22217v1 | arXiv:2605.22217v1 HTML — §3 Training Collapse: Empirical Mechanisms; §Appendix A Training Configuration | arXiv:2605.22217v1 HTML — §Experimental matrix.; §Appendix C DSL Replication of Section 3 Results; §C.4 Stratified holdout evaluation | arXiv:2605.22217v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.22217v1; sha256:5f9ebff025d6869fec00b2e330c5e9ec41be730c5203316c71678e9f1aa25e76 | claim:SF-2026-ARXIV-2605-22217 | complete |
| SF-2026-ARXIV-2605-22219 | RP-cbbf85c383928661 | deep | arXiv:2605.22219v1 | SRC-ARXIV@arXiv:2605.22219v1 | arXiv:2605.22219v1 HTML — §CLI-based LLM Agentic Search Systems.; §Commercial Agent Systems.; §Commercial system evaluation. | arXiv:2605.22219v1 HTML — §SGR-Bench : Benchmarking Search Agents on State-Gated Retrieval; §2.1 Search-Agent Benchmarks; §2.2 Web Navigation and Interaction Benchmarks | arXiv:2605.22219v1 HTML — §5 Conclusion; §Appendix D Extended Limitations Discussion; §Failure case: GPT-5.5 on waterquality_003-g. | https://arxiv.org/html/2605.22219v1; sha256:551bd63bb81de8ac1342167ad52272ad71284658790941c92ecbbcefe9704f93 | claim:SF-2026-ARXIV-2605-22219 | complete |
| SF-2026-ARXIV-2605-22269 | RP-a5b1bdec67cc9e0d | deep | arXiv:2605.22269v1 | SRC-ARXIV@arXiv:2605.22269v1 | arXiv:2605.22269v1 HTML — §3 Method; §3.1 Problem and Method Overview; §Problem Formulation. | arXiv:2605.22269v1 HTML — §4 Experiment; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.22269v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.22269v1; sha256:b71e71bbf6983ee6fe5fda3dedc1d0e7aa1f3a5d5687776672d20cdb62cb0d56 | claim:SF-2026-ARXIV-2605-22269 | complete |
| SF-2026-ARXIV-2605-22283 | RP-e35b79baa2abe7a8 | deep | arXiv:2605.22283v1 | SRC-ARXIV@arXiv:2605.22283v1 | arXiv:2605.22283v1 HTML — §3 Method; §A.1 VR Teleoperation System; §Appendix B Methods | arXiv:2605.22283v1 HTML — §4 Experiments; §4.1 Benchmarks; §4.3 Real World Results | arXiv:2605.22283v1 HTML — §5 Conclusion; §D.7 Failure Case Analysis; §D.8 Limitations and Future Directions | https://arxiv.org/html/2605.22283v1; sha256:6bbbb0695a85ce62ed948b94e08a746279c320c6d96862597f75bf54d7bb1bb0 | claim:SF-2026-ARXIV-2605-22283 | complete |
| SF-2026-ARXIV-2605-22297 | RP-2773e805d4000906 | deep | arXiv:2605.22297v1 | SRC-ARXIV@arXiv:2605.22297v1 | arXiv:2605.22297v1 HTML — §3 Heavy-Tail Layer Diagnostics and Layerwise LR Policy | arXiv:2605.22297v1 HTML — §4–§5 LLM Training Evaluation | arXiv:2605.22297v1 HTML — §6 Conclusion and evaluated-model/scale boundary | https://arxiv.org/html/2605.22297v1; sha256:1a33f7dd86433bc9092d7f65f7d70f8146b2ee194d7f42c688d0802aa32c59ca | claim:SF-2026-ARXIV-2605-22297 | complete |
| SF-2026-ARXIV-2605-22321 | RP-e38b49705d5f809f | deep | arXiv:2605.22321v1 | SRC-ARXIV@arXiv:2605.22321v1 | arXiv:2605.22321v1 HTML — §3 Temporal/Spatial/Semantic Evasion Benchmark | arXiv:2605.22321v1 HTML — §5 Security–Utility Evaluation | arXiv:2605.22321v1 HTML — §6 Limitations: single agent platform | https://arxiv.org/html/2605.22321v1; sha256:84a9b2b075d1d695ae335990ae62ea892fb3cba48d8136550660948ac9820ef1 | claim:SF-2026-ARXIV-2605-22321 | complete |
| SF-2026-ARXIV-2605-22333 | RP-1857a698bc38aaa1 | deep | arXiv:2605.22333v1 | SRC-ARXIV@arXiv:2605.22333v1 | arXiv:2605.22333v1 HTML — §III Remote-MCP Authentication Measurement Method | arXiv:2605.22333v1 HTML — §V Measurement Results | arXiv:2605.22333v1 HTML — §VI-C Limitations and Future Work | https://arxiv.org/html/2605.22333v1; sha256:abc7e838684e5cdaa954cab0df10e8a95e2875373e0a8223728dcb3f75db0afd | claim:SF-2026-ARXIV-2605-22333 | complete |
| SF-2026-ARXIV-2605-22337 | RP-910582a55cff8d0d | deep | arXiv:2605.22337v1 | SRC-ARXIV@arXiv:2605.22337v1 | arXiv:2605.22337v1 HTML — §3 Methodology; §3.1 Method Overview; §3.2 Problem Formulation | arXiv:2605.22337v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Language Modeling Evaluation | arXiv:2605.22337v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.22337v1; sha256:27d4f85751e57827280dd800a9fdfbbef545fb002a4970c9edca08065f07058c | claim:SF-2026-ARXIV-2605-22337 | complete |
| SF-2026-ARXIV-2605-22343 | RP-003af20653f5b0ca | deep | arXiv:2605.22343v1 | SRC-ARXIV@arXiv:2605.22343v1 | arXiv:2605.22343v1 HTML — §3 Existing systems and remaining gaps; §4 The Sibyl-AutoResearch framework; §5 The Sibyl system | arXiv:2605.22343v1 HTML — §Appendix E Evaluation protocols | arXiv:2605.22343v1 HTML — §2 Failure modes: where autonomous research loses experience; §7 Limitations and alternative views; §8 Conclusion | https://arxiv.org/html/2605.22343v1; sha256:b1e7cfd7b8dac9fb3c82a2c1f66b8db973b116f1b22d83405123a694ffc77d62 | claim:SF-2026-ARXIV-2605-22343 | complete |
| SF-2026-ARXIV-2605-22411 | RP-367a53e84b7e475c | deep | arXiv:2605.22411v1 | SRC-ARXIV@arXiv:2605.22411v1 | arXiv:2605.22411v1 HTML — §Memory Systems for LLM Agents.; §3.1 Problem Formulation; §Appendix A Datasets and Baseline Methods | arXiv:2605.22411v1 HTML — §4 Experiment; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.22411v1 HTML — §5 Conclusion; §C.3.4 Reward-Time Answer Correctness and Failure-Attribution Judge Prompt for r 6 r_{6} and r 7 r_{7}; §Appendix E Limitations and Future work | https://arxiv.org/html/2605.22411v1; sha256:d6db6b0e6ae637ed59cd7704fb4fe06abe73acd2970445457b79ed5de8c5f518 | claim:SF-2026-ARXIV-2605-22411 | complete |
| SF-2026-ARXIV-2605-22416 | RP-0cf402a88d5606e3 | deep | arXiv:2605.22416v1 | SRC-ARXIV@arXiv:2605.22416v1 | arXiv:2605.22416v1 HTML — §3 Asymmetric Virtual-Memory Paging | arXiv:2605.22416v1 HTML — §4.2–§4.5 Evaluation | arXiv:2605.22416v1 HTML — §4.6 Limitations | https://arxiv.org/html/2605.22416v1; sha256:f6a00dc5280170ef69a18de8a123c2e0c549038fd3d1faa6dcd3cbfdc26dccc7 | claim:SF-2026-ARXIV-2605-22416 | complete |
| SF-2026-ARXIV-2605-22446 | RP-c430c28fcc1bc1db | deep | arXiv:2605.22446v1 | SRC-ARXIV@arXiv:2605.22446v1 | arXiv:2605.22446v1 HTML — §3 Preemptive Runtime Verification Architecture | arXiv:2605.22446v1 HTML — §4 VLA/World-Model Rollout Evaluation | arXiv:2605.22446v1 HTML — §5 Discussion and critic/OOD/resampling limitations | https://arxiv.org/html/2605.22446v1; sha256:c4be3b9a170b8bf447164d3501ffded8f4a2f79e2e32340e5d3b7d8c9f89ee4d | claim:SF-2026-ARXIV-2605-22446 | complete |
| SF-2026-ARXIV-2605-22456 | RP-f291e3b5d248bff1 | deep | arXiv:2605.22456v1 | SRC-ARXIV@arXiv:2605.22456v1 | arXiv:2605.22456v1 HTML — §III Structured-Future Safety Arbitration | arXiv:2605.22456v1 HTML — §V Evaluation | arXiv:2605.22456v1 HTML — §VII Limitations and Future Work | https://arxiv.org/html/2605.22456v1; sha256:cbd2d91c9eb91dd2cb2e8565a6e11c0f11ba35b1530093ef03a6e3579a3a6b78 | claim:SF-2026-ARXIV-2605-22456 | complete |
| SF-2026-ARXIV-2605-22493 | RP-9b1d2ca326be1d21 | deep | arXiv:2605.22493v1 | SRC-ARXIV@arXiv:2605.22493v1 | arXiv:2605.22493v1 HTML — §C.1 Methods; §C.2 Network Architectures; §C.4 Training Details | arXiv:2605.22493v1 HTML — §4 Main Results; §5 Experiments; §Appendix A Notation, Definitions, and Known Results | arXiv:2605.22493v1 HTML — §Understanding Multimodal Failure in Action-Chunking Behavioral Cloning; §6 Conclusion; §Limitations and Future Work | https://arxiv.org/html/2605.22493v1; sha256:1e357001fef95c4423f3b85a99bec854825b304a41c668556b4bc50de83752d1 | claim:SF-2026-ARXIV-2605-22493 | complete |
| SF-2026-ARXIV-2605-22502 | RP-e9cca727b50bdfae | deep | arXiv:2605.22502v1 | SRC-ARXIV@arXiv:2605.22502v1 | arXiv:2605.22502v1 HTML — §3 Evaluation Methodology | arXiv:2605.22502v1 HTML — §3 Evaluation Methodology; §4.1 Experiment 1: Travel Booking (3B); §4.2 Experiment 2: Zoom Support (8B) | arXiv:2605.22502v1 HTML — §4.4 Efficiency and Failure Modes; §8 Conclusion | https://arxiv.org/html/2605.22502v1; sha256:6b301d11f4d52211e1707625fdae979cbec1495724ff272dbf04502abf58fe60 | claim:SF-2026-ARXIV-2605-22502 | complete |
| SF-2026-ARXIV-2605-22505 | RP-c9272492e441b710 | deep | arXiv:2605.22505v1 | SRC-ARXIV@arXiv:2605.22505v1 | arXiv:2605.22505v1 HTML — §1 Introduction — disclosed mechanism | arXiv:2605.22505v1 HTML — §Towards Direct Evaluation of Harness Optimizers via Priority Ranking; §3 Why is Direct Evaluation Necessary for Harness Optimizers?; §Analysis I: About half of the optimization steps are considered detrimental. | arXiv:2605.22505v1 HTML — §7 Discussions; §8 Conclusion; §Appendix B Limitations | https://arxiv.org/html/2605.22505v1; sha256:c071ec4b3f5a120f4bf5e884b8df19bb32ce0c080b1aacdbd779da71569ed691 | claim:SF-2026-ARXIV-2605-22505 | complete |
| SF-2026-ARXIV-2605-22511 | RP-50bb27e7b1ad131c | deep | arXiv:2605.22511v1 | SRC-ARXIV@arXiv:2605.22511v1 | arXiv:2605.22511v1 HTML — §3 Method | arXiv:2605.22511v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.22511v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.22511v1; sha256:f5f0f537676a90c701d209768e368271bb69856e27dac21acb24420b3f77692a | claim:SF-2026-ARXIV-2605-22511 | complete |
| SF-2026-ARXIV-2605-22526 | RP-578c7d964e30d95e | deep | arXiv:2605.22526v1 | SRC-ARXIV@arXiv:2605.22526v1 | arXiv:2605.22526v1 HTML — §4.1.1. Approach; §4.2.1. Approach; §4.3.1. Approach | arXiv:2605.22526v1 HTML — §4. Empirical Results; §4.1.2. Results; §4.2.2. Results | arXiv:2605.22526v1 HTML — §5. Discussion; §7. Conclusion | https://arxiv.org/html/2605.22526v1; sha256:23e157bccb852c3243cb932023066cecd338499ee5a00eb030c519804fb23b55 | claim:SF-2026-ARXIV-2605-22526 | complete |
| SF-2026-ARXIV-2605-22544 | RP-51a7e3bbff7bdb1a | deep | arXiv:2605.22544v1 | SRC-ARXIV@arXiv:2605.22544v1 | arXiv:2605.22544v1 HTML — §2 Methodology | arXiv:2605.22544v1 HTML — §One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation; §3 Analysis and Discussion; §3.2 Prompt Sensitivity Analysis | arXiv:2605.22544v1 HTML — §3 Analysis and Discussion; §4 Conclusion; §Limitations | https://arxiv.org/html/2605.22544v1; sha256:c17954b5c40f9f6f6233a6fa2e2bd3742615d30d4941e9872596baca69ae95e4 | claim:SF-2026-ARXIV-2605-22544 | complete |
| SF-2026-ARXIV-2605-22564 | RP-1179e99878a497df | deep | arXiv:2605.22564v1 | SRC-ARXIV@arXiv:2605.22564v1 | arXiv:2605.22564v1 HTML — §SynAE : A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations; §2 SynAE Framework; §Appendix E Prompts for LLM-Based Synthetic Data Generation Methods | arXiv:2605.22564v1 HTML — §SynAE : A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations; §2.1 Evaluation Metrics; §4. Fidelity metrics for downstream evaluation | arXiv:2605.22564v1 HTML — §4 Conclusions and Limitations | https://arxiv.org/html/2605.22564v1; sha256:ec07f9656b16a446605f7416dec0947cd33d3ff7a2436c3c3318a79c59b941f0 | claim:SF-2026-ARXIV-2605-22564 | complete |
| SF-2026-ARXIV-2605-22566 | RP-7c4ad4af579ac3ac | deep | arXiv:2605.22566v1 | SRC-ARXIV@arXiv:2605.22566v1 | arXiv:2605.22566v1 HTML — §3 wGraph and GraphFlow Runtime | arXiv:2605.22566v1 HTML — §5 Agent-Serving Evaluation | arXiv:2605.22566v1 HTML — §6 Conclusion and workflow-generalization boundary | https://arxiv.org/html/2605.22566v1; sha256:8709bf291b79b8471b252061a97423f3239cdd8577a858149aa12be2d4377fca | claim:SF-2026-ARXIV-2605-22566 | complete |
| SF-2026-ARXIV-2605-22568 | RP-fbc7437e5ec17bca | deep | arXiv:2605.22568v1 | SRC-ARXIV@arXiv:2605.22568v1 | arXiv:2605.22568v1 HTML — §1 Introduction — disclosed mechanism | arXiv:2605.22568v1 HTML — §Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard; §2 Benchmark Vulnerabilities; §3.1 Dynamic Benchmarks | arXiv:2605.22568v1 HTML — §5 Discussion; §6 Conclusion | https://arxiv.org/html/2605.22568v1; sha256:36b41b84d6ab2a104b936e61d011d1efc386f366888a22d8baf9a8a18254f92c | claim:SF-2026-ARXIV-2605-22568 | complete |
| SF-2026-ARXIV-2605-22608 | RP-ecb816ec5e26f080 | deep | arXiv:2605.22608v1 | SRC-ARXIV@arXiv:2605.22608v1 | arXiv:2605.22608v1 HTML — §2 Agentic CLEAR Method; §3 Agentic CLEAR Framework; §System Level | arXiv:2605.22608v1 HTML — §Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents; §4 Experimental Setup; §5 Agentic CLEAR Issues Results | arXiv:2605.22608v1 HTML — §8 Conclusions | https://arxiv.org/html/2605.22608v1; sha256:6a7319a0385065eec8b38de6a1cfcf0ad8f2ed2aafabce74dd6e8475ef6077a7 | claim:SF-2026-ARXIV-2605-22608 | complete |
| SF-2026-ARXIV-2605-22620 | RP-ca0a5a3d71401ac2 | deep | arXiv:2605.22620v1 | SRC-ARXIV@arXiv:2605.22620v1 | arXiv:2605.22620v1 HTML — §Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework; §3 Method; §Training details. | arXiv:2605.22620v1 HTML — §4 Experiments Results; §4.1 Experimental Setup; §Evaluation. | arXiv:2605.22620v1 HTML — §5 Discussion; §Limitations.; §6 Conclusion | https://arxiv.org/html/2605.22620v1; sha256:560e9d8c9ab508b755faf2a8052de62d2796ca9a79a59b435eeb147f67f8653a | claim:SF-2026-ARXIV-2605-22620 | complete |
| SF-2026-ARXIV-2605-22634 | RP-68269c7109c25067 | deep | arXiv:2605.22634v1 | SRC-ARXIV@arXiv:2605.22634v1 | arXiv:2605.22634v1 HTML — §3 GovernSpec Contractual Skill Model | arXiv:2605.22634v1 HTML — §6 Evaluation | arXiv:2605.22634v1 HTML — §8 Threats to Validity | https://arxiv.org/html/2605.22634v1; sha256:342abcd77a52bd20185431c97b7c430e8bba5f28618e41b37f789be32e7d359a | claim:SF-2026-ARXIV-2605-22634 | complete |
| SF-2026-ARXIV-2605-22643 | RP-4dcbcfdccc7e009d | deep | arXiv:2605.22643v1 | SRC-ARXIV@arXiv:2605.22643v1 | arXiv:2605.22643v1 HTML — §3 Multi-Turn Agentic-Safety Benchmark | arXiv:2605.22643v1 HTML — §5 Evaluation | arXiv:2605.22643v1 HTML — §7.1 Limitations | https://arxiv.org/html/2605.22643v1; sha256:be92f5bfc484b237b1a35be27e25cffa5460505da83528b2d2a7512b3d73c6e7 | claim:SF-2026-ARXIV-2605-22643 | complete |
| SF-2026-ARXIV-2605-22718 | RP-d75e3c1f058b84f9 | deep | arXiv:2605.22718v1 | SRC-ARXIV@arXiv:2605.22718v1 | arXiv:2605.22718v1 HTML — §4 Method; §Appendix C Retrieval Algorithm Ablations | arXiv:2605.22718v1 HTML — §5 Experiments; §5.1 Experimental settings; §Benchmark. | arXiv:2605.22718v1 HTML — §6 Conclusion; §7 Limitations Future Work | https://arxiv.org/html/2605.22718v1; sha256:db3328383821689a8ec484031f62c4a49625ff431465b94ad907dc2e2b711f91 | claim:SF-2026-ARXIV-2605-22718 | complete |
| SF-2026-ARXIV-2605-22721 | RP-3a4cd33ab26bd980 | deep | arXiv:2605.22721v1 | SRC-ARXIV@arXiv:2605.22721v1 | arXiv:2605.22721v1 HTML — §Self-Evolving Multi-Agent Systems via Decentralized Memory; §LLM-based multi-agent systems.; §Memory in multi-agent systems. | arXiv:2605.22721v1 HTML — §5 Theoretical Analysis; §6 Experiment; §6.1 Experimental Setup | arXiv:2605.22721v1 HTML — §8 Conclusion and Limitation; §Limitation. | https://arxiv.org/html/2605.22721v1; sha256:a077f7408112090a4032d4d71cd4d4bf04126e5786fd5eeaffb227044e023dbe | claim:SF-2026-ARXIV-2605-22721 | complete |
| SF-2026-ARXIV-2605-22731 | RP-a2301dcb2cf7689d | deep | arXiv:2605.22731v1 | SRC-ARXIV@arXiv:2605.22731v1 | arXiv:2605.22731v1 HTML — §3 State-Distribution View of Post-Training | arXiv:2605.22731v1 HTML — §5 SFT/RL/On-Policy Distillation Experiments | arXiv:2605.22731v1 HTML — §6 Limitations | https://arxiv.org/html/2605.22731v1; sha256:fe62fee2e01df54149436c6a4c46a84e4ad98e9825b059f77368105ca301e530 | claim:SF-2026-ARXIV-2605-22731 | complete |
| SF-2026-ARXIV-2605-22769 | RP-22c9dc31899f21ee | deep | arXiv:2605.22769v1 | SRC-ARXIV@arXiv:2605.22769v1 | arXiv:2605.22769v1 HTML — §Understanding Data Temporality Impact on Large Language Models Pre-training; §2 Pre-training Sequential Models; §5.2 Temporal analysis of the sequential pre-training | arXiv:2605.22769v1 HTML — §4 Experimental settings; §5 Results; §5.2 Temporal analysis of the sequential pre-training | arXiv:2605.22769v1 HTML — §7 Perspectives Conclusions | https://arxiv.org/html/2605.22769v1; sha256:09f4fcc18991531e65cf6cb6d6b5e717db7b3b91cda3fbfe07345ca131b34859 | claim:SF-2026-ARXIV-2605-22769 | complete |
| SF-2026-ARXIV-2605-22781 | RP-bbf955560a988347 | deep | arXiv:2605.22781v1 | SRC-ARXIV@arXiv:2605.22781v1 | arXiv:2605.22781v1 HTML — §3 DeltaBox Architecture; §4 Detailed Design | arXiv:2605.22781v1 HTML — §6 Checkpoint/Rollback Evaluation | arXiv:2605.22781v1 HTML — §7 Discussion and sandbox-state boundary | https://arxiv.org/html/2605.22781v1; sha256:2f83e3151bf0654e4a7c0ac409c73e2bf954638b68116227217eb330139295c4 | claim:SF-2026-ARXIV-2605-22781 | complete |
| SF-2026-ARXIV-2605-22786 | RP-13d05acee7fde2d4 | deep | arXiv:2605.22786v1 | SRC-ARXIV@arXiv:2605.22786v1 | arXiv:2605.22786v1 HTML — §3 LCGuard Latent-Communication Policy | arXiv:2605.22786v1 HTML — §5 KV-Sharing Safety Evaluation | arXiv:2605.22786v1 HTML — Appendix A.9 Limitations | https://arxiv.org/html/2605.22786v1; sha256:87ad6192aa80d5b25c545f06b6c92ec409e7b81be3123b7d3d9242acfef06168 | claim:SF-2026-ARXIV-2605-22786 | complete |
| SF-2026-ARXIV-2605-22794 | RP-0c8750f188ac7d1a | deep | arXiv:2605.22794v1 | SRC-ARXIV@arXiv:2605.22794v1 | arXiv:2605.22794v1 HTML — §MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems; §2 System Architecture; §5.1 Agentic Systems | arXiv:2605.22794v1 HTML — §4.3 Results: Iteration-1 Outcome | arXiv:2605.22794v1 HTML — §6 Conclusion | https://arxiv.org/html/2605.22794v1; sha256:834f16c8385e7ad5a173dcdb0d856e95a3fbbaa3c1a038a54db302da585ca23a | claim:SF-2026-ARXIV-2605-22794 | complete |
| SF-2026-ARXIV-2605-22800 | RP-65bc8f754b1d6f88 | deep | arXiv:2605.22800v1 | SRC-ARXIV@arXiv:2605.22800v1 | arXiv:2605.22800v1 HTML — §Training distribution.; §Matched training (one recipe).; §Corollary 3.4 (PGD training remains anisotropic) . | arXiv:2605.22800v1 HTML — §How to read the five results.; §Bridge to experiments.; §Appendix B Per-task experimental supplements | arXiv:2605.22800v1 HTML — §Mapped failures (§ 8.8 ).; §8.8 Named failures and overall pattern; §10 Discussion | https://arxiv.org/html/2605.22800v1; sha256:bdb9ec7283c8728e937180504806a1cadc884bb88e4d9e609943df06064d6233 | claim:SF-2026-ARXIV-2605-22800 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-21516:start -->
#### Harnesses for Inference-Time Alignment over Execution Trajectories

问题与约束：However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success.

机制与 ownership：However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success.

Evaluation contract：We validate these predictions through controlled synthetic experiments and real terminal agent benchmarks.

Trade-off / failure：The mechanism described in `4 Alignment Principles for Harness Design` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-21516:start -->`Harnesses for Inference-Time Alignment over Execution Trajectories` is supported only under the v1-disclosed workload and evaluator behind `5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-21516:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-21516`。
<!-- review:SF-2026-ARXIV-2605-21516:end -->

<!-- review:SF-2026-ARXIV-2605-21543:start -->
#### Provable Joint Decontamination for Benchmarking Multiple Large Language Models

**问题与机制。** In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Joint Decontamination Procedure`；Evaluation=`§4 Controlled Experiments`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21543:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21543:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21543:end -->

<!-- review:SF-2026-ARXIV-2605-21602:start -->
#### Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs

**问题与机制。** We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD). 系统 owner=`PLATFORM-MONITORING`。

**Exact-v1。** Method=`§3 MOOD Benchmark and Monitor Design`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`§6 Conclusion and stated monitor limitations`。

<!-- claim:SF-2026-ARXIV-2605-21602:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21602:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21602:end -->

<!-- review:SF-2026-ARXIV-2605-21603:start -->
#### DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling

**问题与机制。** To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 Programmable Operator Scheduling`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§7 Conclusion and evaluated-hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-21603:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21603:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21603:end -->

<!-- review:SF-2026-ARXIV-2605-21606:start -->
#### When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning

**问题与机制。** To identify this phenomenon, we introduce a branch-viability diagnostic. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 Method; §Appendix F Adaptive-loss template and method comparison; §Appendix G PW-OPSD training pseudocode`；Evaluation=`§4 Experiments; §Evaluation.; §4.2 Main results on Qwen3-4B`；Limitations/Counterevidence=`§5 Conclusion, Limitations, and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21606:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21606:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21606:end -->

<!-- review:SF-2026-ARXIV-2605-21642:start -->
#### Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?

**问题与机制。** Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Method; §Training objective.; §4.2 Training and implementation details`；Evaluation=`§4 Experiments; §4.1 Task and evaluation protocol; §Depth reasoning benchmark.`；Limitations/Counterevidence=`§5 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-21642:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21642:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21642:end -->

<!-- review:SF-2026-ARXIV-2605-21648:start -->
#### Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos

**问题与机制。** We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§1 Introduction — exact-v1 disclosed mechanism`；Evaluation=`§Appendix D Experimental Details and Additional Figures; §D.2 Dropout Scheduling Experiments`；Limitations/Counterevidence=`§4 Conclusions and further scope for research; §5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21648:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21648:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21648:end -->

<!-- review:SF-2026-ARXIV-2605-21649:start -->
#### EntmaxKV: Support-Aware Decoding for Entmax Attention

**问题与机制。** In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§4 EntmaxKV`；Evaluation=`§5 Experiments; §5.1 Approximation Error Analysis`；Limitations/Counterevidence=`§7 Conclusion — exact-v1 workload/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-21649:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21649:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21649:end -->

<!-- review:SF-2026-ARXIV-2605-21768:start -->
#### Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

**问题与机制。** To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§2.1 Memory Agent Architectures; §3 Method; §3.1 Problem Formulation: Multi-step Memory Bank Construction`；Evaluation=`§4 Experiments; §4.1 Experiment Setup; §Datasets and Evaluation Metrics.`；Limitations/Counterevidence=`§5 Conclusion; §Appendix D Limitations and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21768:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21768:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21768:end -->

<!-- review:SF-2026-ARXIV-2605-21779:start -->
#### FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction

**问题与机制。** While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 FuzzingBrain V2 Architecture`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§6.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-21779:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21779:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21779:end -->

<!-- review:SF-2026-ARXIV-2605-21800:start -->
#### stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation

**问题与机制。** We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 stable-worldmodel Platform`；Evaluation=`§4 Case Studies`；Limitations/Counterevidence=`§6 Conclusion and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-21800:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21800:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21800:end -->

<!-- review:SF-2026-ARXIV-2605-21801:start -->
#### Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization

**问题与机制。** Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§E.3 Training Details`；Evaluation=`§4 Experiments; §4.1 Experiment Setup; §4.2 Main Experiment`；Limitations/Counterevidence=`§5 Conclusion; §Conclusion.; §D.8 Discussion: Dataset-dependent Effects`。

<!-- claim:SF-2026-ARXIV-2605-21801:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21801:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21801:end -->

<!-- review:SF-2026-ARXIV-2605-21803:start -->
#### Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws

**问题与机制。** We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws; §Architecture–optimizer interaction.; §3 Methodology`；Evaluation=`§Experimental setup; §Appendix A Experimental Setup; §Appendix C Rényi Effective Rank Analysis: Where Optimizer-Induced Capacity Forms`；Limitations/Counterevidence=`§5 Discussion and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-21803:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21803:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21803:end -->

<!-- review:SF-2026-ARXIV-2605-21847:start -->
#### CompPow: A Case for Component-level GPU Power Management

**问题与机制。** We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%). 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§3 Component-Level Power Control`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7 Conclusion and evaluated-GPU boundary`。

<!-- claim:SF-2026-ARXIV-2605-21847:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21847:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21847:end -->

<!-- review:SF-2026-ARXIV-2605-21850:start -->
#### ACC: Compiling Agent Trajectories for Long-Context Training

**问题与机制。** We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§3 Agent-Trajectory Compilation`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§6 Limitations and Social Impacts`。

<!-- claim:SF-2026-ARXIV-2605-21850:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21850:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21850:end -->

<!-- review:SF-2026-ARXIV-2605-21854:start -->
#### CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models

**问题与机制。** Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Cross-Paradigm VLA Interface and Surrogate Log-Probability`；Evaluation=`§4 Experiments; §4.5 Inference Anatomy`；Limitations/Counterevidence=`§5.2 Non-transfer of Inference Caching; §6 Limitations`；正文 sha256=`18e9186cc05a8e8291cc9eb36fbe2eb828d79aa02a6c96845c9126bbc9ed2924`。

<!-- claim:SF-2026-ARXIV-2605-21854:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21854:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21854:end -->

<!-- review:SF-2026-ARXIV-2605-21856:start -->
#### The Illusion of Reasoning: Exposing Evasive Data Contamination in LLMs via Zero-CoT Truncation

**问题与机制。** Large language models (LLMs) have demonstrated impressive reasoning abilities across a wide range of tasks, but data contamination undermines the objective evaluation of these capabilities. Inspired by this, we propose the Zero-CoT Probe (ZCP), a novel black-box detection method that deliberately truncates the entire Chain-of-Thought (CoT) process to expose latent shortcut mappings. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Method; §3.1 Problem Formulation; §3.2 Limitations of Existing Detection Methods in Evasive Scenarios`；Evaluation=`§4 Experiments; §4.1 Experiments on Existing Models; §4.1.1 Results and Analysis`；Limitations/Counterevidence=`§3.2 Limitations of Existing Detection Methods in Evasive Scenarios; §5 Conclusion Limitation`；正文 sha256=`cc0004827e00e3055ddb2883c17040a94b93b2eafc5083349501848398c2d0b6`。

<!-- claim:SF-2026-ARXIV-2605-21856:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21856:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21856:end -->

<!-- review:SF-2026-ARXIV-2605-21862:start -->
#### EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control

**问题与机制。** Chunked vision-language-action (VLA) policies predict multi-step robot controls, conditioning each update on the current visual observation alone. We argue for a persistent action-updated scene state across control calls, and introduce EvoScene-VLA. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Evolving Scene Beliefs in the Action Decoder`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`Appendix F Limitations`；正文 sha256=`12f60d2629aa8c413c794b1b705bbe43641a63ae8024cdc1ede3cb132711b449`。

<!-- claim:SF-2026-ARXIV-2605-21862:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21862:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21862:end -->

<!-- review:SF-2026-ARXIV-2605-21949:start -->
#### Claim-Selective Certification for High-Risk Medical Retrieval-Augmented Generation

**问题与机制。** Medical RAG systems in high-risk QA settings are often evaluated through a single answer-or-abstain decision, but mixed evidence may support one claim, require conditions for another, and contradict a third. We study claim-selective certification: each response is decomposed into verifiable claims, scored against retrieved evidence, and mapped by an intent-aware selector to {full, partial, conflict, abstain}. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Problem Formulation; §4 Method`；Evaluation=`§5 Experiments; §5.1 Data Provenance and Main Evaluation Split; §5.4 Evaluation Protocol and Label–Policy Separation`；Limitations/Counterevidence=`§6.3 Abstract-Style Transfer Behavior and Failure Modes; §7 Discussion; §8 Limitations`；正文 sha256=`8416357e10590c97a701341111ab0ca3b665d678c94aa4d9c36d55f7f30ee87e`。

<!-- claim:SF-2026-ARXIV-2605-21949:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21949:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21949:end -->

<!-- review:SF-2026-ARXIV-2605-21951:start -->
#### Dynamic Mixture of Latent Memories for Self-Evolving Agents

**问题与机制。** Achieving self-evolution in intelligent agents requires the continual accumulation of new knowledge across changing task sequences without forgetting previously acquired abilities. We propose MoLEM, a generative mixture of latent memory framework based on a dynamic mixture-of-experts (MoE). 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 Dynamic Mixture of Latent Memories`；Evaluation=`§4 Experiments`；Limitations/Counterevidence=`§5 Discussion and static-capacity/forgetting boundary`；正文 sha256=`ae6cc1fe4b7910a8e1c25a32bd6f8ec181bc884b2957efbaf0666ee81745c4d9`。

<!-- claim:SF-2026-ARXIV-2605-21951:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21951:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21951:end -->

<!-- review:SF-2026-ARXIV-2605-21965:start -->
#### SpecHop: Continuous Speculation for Accelerating Multi-Hop Retrieval Agents

**问题与机制。** Large language models increasingly use external tools such as web search and document retrieval to solve information-intensive tasks. We study how to accelerate such trajectories without changing the final trajectory the model would have taken without acceleration, assuming access to faster but less reliable speculator tools. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§3 SpecHop Continuous Speculation`；Evaluation=`§4 Multi-Hop Retrieval Evaluation`；Limitations/Counterevidence=`§5 Conclusion and speculation-misprediction boundary`；正文 sha256=`544f65f79b5ceeddcb806e3cc88ad14f198fdc40f365edefb3d8b4cc3f6babbe`。

<!-- claim:SF-2026-ARXIV-2605-21965:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21965:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21965:end -->

<!-- review:SF-2026-ARXIV-2605-21996:start -->
#### From Patches to Trajectories: Privileged Process Supervision for Software-Engineering Agents

**问题与机制。** Supervised fine-tuning (SFT) on long teacher trajectories is the dominant way to instill investigation and reasoning in open software-engineering (SWE) agents. We propose Patches-to-Trajectories (P2T), which uses $p^\star$ as privileged information during curation and formulates trajectory construction as bi-objective optimization over per-step effectiveness and trajectory length. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§4 Method; §Appendix G Full curation algorithm; §Appendix J Training details`；Evaluation=`§5 Experiments; §5.1 Experimental Setup; §Results (interventional).`；Limitations/Counterevidence=`§6 Conclusion; §Appendix L Limitations and outlook; §Limitations.`；正文 sha256=`f452614a9127137ed1f912fc0c559750f4b20d098c1ba85872052e7492b19ece`。

<!-- claim:SF-2026-ARXIV-2605-21996:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21996:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21996:end -->

<!-- review:SF-2026-ARXIV-2605-21997:start -->
#### The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems

**问题与机制。** Most agent frameworks are built around the language model: a conversation loop comes first, then tools, then rules, and finally a logging layer bolted on for observability, with state persisted as retrievable "memory." We describe ActiveGraph, a runtime that inverts this arrangement. This single design decision yields three properties that retrieval-and-summarization memory systems do not provide: deterministic replay of any run from its log, cheap forking that branches a run at any event without re-executing the shared prefix, and end-to-end lineage from a high-level goal down to the individual model call that produced each artifact. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Event-Sourced Reactive Graph Model`；Evaluation=`§6 Evaluation and Fork/Replay Cases`；Limitations/Counterevidence=`§9 Limitations and Conclusion`；正文 sha256=`4751c925e420b07bddefa40aaca8440bf418ec6aaa9e9e689074c59c25114ebb`。

<!-- claim:SF-2026-ARXIV-2605-21997:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-21997:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-21997:end -->

<!-- review:SF-2026-ARXIV-2605-22001:start -->
#### Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems

**问题与机制。** Injection detectors deployed to protect LLM agents are calibrated on static, template-based payloads that announce themselves as override directives. We identify a systematic blind spot: when payloads are generated to mimic the domain vocabulary and authority structures of the target document, what we call domain camouflaged injection, standard detectors fail to flag them, with detection rates dropping from 93.8% to 9.7% on Llama 3.1 8B and from 100% to 55.6% on Gemini 2.0 Flash. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems; §4 Method; §4.3 Agent Architectures`；Evaluation=`§Prompt injection attacks and benchmarks.; §5 Experiments and Results; §6 Analysis`；Limitations/Counterevidence=`§6.1 The Failure Mode is Confident, Not Uncertain; §7 Conclusion; §Limitations`；正文 sha256=`b1adad4719d0940541d1d4b82da2601b098774d37c630e58bb951885ff2040cd`。

<!-- claim:SF-2026-ARXIV-2605-22001:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22001:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22001:end -->

<!-- review:SF-2026-ARXIV-2605-22014:start -->
#### LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training

**问题与机制。** To reduce user costs and maximize cluster utilization, large model training increasingly leverages volatile but inexpensive GPU capacity, such as spot instances and reclaimable resources in shared clusters. We present LiveR, a live reconfiguration runtime for elastic LLM training that replaces storage-backed restart with a live, bounded-memory handoff between mixed-parallel training worlds. 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1。** Method=`§4 LiveR Dual-World Reconfiguration Runtime`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§7 Discussion and live-resharding boundary`；正文 sha256=`781be436a12291a3d0d7d1739d53c018fc141b0319b6f2604dd1ddde81c9dc87`。

<!-- claim:SF-2026-ARXIV-2605-22014:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22014:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22014:end -->

<!-- review:SF-2026-ARXIV-2605-22041:start -->
#### RADAR: Defending RAG Dynamically against Retrieval Corruption

**问题与机制。** While RAG systems are increasingly deployed in dynamic web search, temporal volatility amplifies their vulnerability to adversarial attacks. We propose RADAR, a framework that models reliable context selection as a graph-based energy minimization problem, solved exactly via Max-Flow Min-Cut. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§3 RADAR Dynamic Retrieval-Corruption Defense`；Evaluation=`§4–§5 Attack and Defense Evaluation`；Limitations/Counterevidence=`§6 Conclusion and adaptive-attacker boundary`；正文 sha256=`64b75669ea0965f176d205ab85117e15274543eac61530336cf7ecfedc08a71d`。

<!-- claim:SF-2026-ARXIV-2605-22041:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22041:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22041:end -->

<!-- review:SF-2026-ARXIV-2605-22057:start -->
#### FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing

**问题与机制。** Enterprise routers assign queries to expert agents, yet deployed profiles stay static while agents evolve (prompts, tools, models), and developers rarely keep descriptions or exemplars current. We present FlyRoute, a self-evolving profiling framework that grows capability evidence from real traffic: dispatch candidates, quality-gate successful pairs into each agent's success store, periodically distill evidence into learned capability descriptions, and inject those descriptions together with BM25-retrieved successes into an LLM router. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Method; §Task formulation.; §Appendix A Illustrative Training Queries`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion; §Limitations`；正文 sha256=`ec4a4601f8e2674837ae7cd1d5dce9e0992db4ac733938f7e8558650f1148066`。

<!-- claim:SF-2026-ARXIV-2605-22057:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22057:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22057:end -->

<!-- review:SF-2026-ARXIV-2605-22074:start -->
#### From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning

**问题与机制。** Reinforcement learning from verifiable rewards (RLVR) has shown strong promise for LLM reasoning, but outcome-based RLVR remains inefficient on hard problems because correct final-answer rollouts are rare and sample-level credit assignment cannot use partial progress in failed attempts. We introduce SCRL (Subproblem Curriculum Reinforcement Learning), a curriculum RL framework that derives verifiable subproblems from reference reasoning chains and fixes the final subproblem as the original problem. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 Verifiable-Subproblem Curriculum Construction`；Evaluation=`§4–§5 RL Credit-Assignment Evaluation`；Limitations/Counterevidence=`Appendix G Limitations and Future Work`；正文 sha256=`ab1e5e5fd19cbf65b70a338ba9230d6d98604ea33d65abd326859fb024a0b8d1`。

<!-- claim:SF-2026-ARXIV-2605-22074:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22074:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22074:end -->

<!-- review:SF-2026-ARXIV-2605-22102:start -->
#### ExComm: Exploration-Stage Communication for Error-Resilient Agentic Test-Time Scaling

**问题与机制。** A common failure mode in long-horizon agentic test-time scaling is error propagation, where factual errors or invalid deductions introduced at intermediate steps persist in the agent's belief state and contaminate later reasoning. We propose ExComm, a communication protocol for exploration-stage agentic test-time scaling. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§1 Introduction — disclosed mechanism`；Evaluation=`§4 Experiments; §4.1 Main Results; §4.2 Error Recovery Analysis`；Limitations/Counterevidence=`§5 Conclusion; §Appendix A Further Discussions; §A.2 Limitations and Future Work`；正文 sha256=`2fd539607c08a60904f2b21d4a8dfdc8e7edc23fdbcb334fdd744220513d4300`。

<!-- claim:SF-2026-ARXIV-2605-22102:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22102:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22102:end -->

<!-- review:SF-2026-ARXIV-2605-22106:start -->
#### ArborKV: Structure-Aware KV Cache Management for Scaling Tree-based LLM Reasoning

**问题与机制。** Recent progress in LLM reasoning has increasingly shifted from single-pass generation to explicit search over intermediate reasoning states. Motivated by this, we propose ArborKV, a structure-aware eviction framework that couples a lightweight value estimator with a tree-aware allocation policy, and performs purely token-extractive eviction with lazy rehydration to support revisits. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§3 ArborKV Thought-Block Cache Model`；Evaluation=`§5 Tree-Reasoning Serving Evaluation`；Limitations/Counterevidence=`§6 Discussion and search-dynamics boundary`；正文 sha256=`dd92adfdc18af871ca7c8794bbf78a91516bcf0442986773496665899c7ee830`。

<!-- claim:SF-2026-ARXIV-2605-22106:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22106:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22106:end -->

<!-- review:SF-2026-ARXIV-2605-22138:start -->
#### Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

**问题与机制。** How should an agent decide when and how to plan? We argue efficient agentic reasoning benefits from decomposing decision-making into three systems: simulative reasoning (System II) grounding deliberation in future-state prediction via a world model; self-regulation (System III) deciding when and how deeply to plan via a learned configurator; and reactive execution (System I) handling fine-grained action. 系统 owner=`AGENT-PLANNING`。

**Exact-v1。** Method=`§Approach 1: Multi-Module Inference (v0.1); §Approach 2: Plan Reconstruction (v1.0); §3.4 Training Data and Hyperparameters`；Evaluation=`§4 Experiments; §4.1 Experiment Setup; §Evaluation Benchmarks`；Limitations/Counterevidence=`§6 Conclusion; §7 Limitations and Future Work`；正文 sha256=`08a5d8670415792a34a4aefdf40f8a4be4002ee5cd18910b88e34fc140b47365`。

<!-- claim:SF-2026-ARXIV-2605-22138:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22138:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22138:end -->

<!-- review:SF-2026-ARXIV-2605-22148:start -->
#### Ratchet: How Reliable Must an LLM Judge Be to Retire a Skill?

**问题与机制。** A large language model (LLM) agent that writes and edits its own skill library must also decide which skills to keep, from one noisy scalar per skill. A large language model (LLM) agent that writes and edits its own skill library must also decide which skills to keep, from one noisy scalar per skill. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Ratchet Skill Admission/Retirement Recipe`；Evaluation=`§5 Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations: amplifier, not discoverer`；正文 sha256=`87019037949ccd4b7d5cb45b45f774bc1c9405ad9a1ca76509bc67f762a971ba`。

<!-- claim:SF-2026-ARXIV-2605-22148:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22148:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22148:end -->

<!-- review:SF-2026-ARXIV-2605-22154:start -->
#### IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents

**问题与机制。** Large language model (LLM)-based agents solve complex tasks by leveraging multi-step reasoning with iterative tool calls and environment interactions, which incur idle time while waiting for observations. Despite the prevalence of idle time in most agentic scenarios, existing works treat it as an unavoidable overhead or propose restricted solutions that overlook varying computational budgets across different tool calls and future observation uncertainty, thereby leading to suboptimal utilization of idle time. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§4 IdleSpec Drafting, Aggregation, and Posterior Update`；Evaluation=`§5 Experiments`；Limitations/Counterevidence=`Appendix A.7 Limitations`；正文 sha256=`55cc67e9ee2b67b8752f7ef27450ef14457b3381ab93855fb38b314a9686f178`。

<!-- claim:SF-2026-ARXIV-2605-22154:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22154:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22154:end -->

<!-- review:SF-2026-ARXIV-2605-22164:start -->
#### Beyond Euclidean Proximity: Repairing Latent World Models with Horizon-Matched Trajectory Reachability Metrics

**问题与机制。** Latent world models can contain the state needed for control, yet their terminal-cost interface can expose the planner to the wrong decision-relevant information. We propose trajectory reachability metrics (TRM), a post-hoc terminal-ranking method for fixed latent world models. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§4 Method: Trajectory Reachability Metrics ( TRM ); §Training environment versus benchmark leakage.; §Appendix A Appendix: TRM Method Details`；Evaluation=`§5 Experimental Protocol; §Evaluation and reporting.; §6 Results`；Limitations/Counterevidence=`§7 Discussion; §8 Limitations; §9 Conclusion`；正文 sha256=`f942f43e655906f0276148bfbbc385fd2d5167c40bd891b2e61102beccf098f2`。

<!-- claim:SF-2026-ARXIV-2605-22164:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22164:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22164:end -->

<!-- review:SF-2026-ARXIV-2605-22166:start -->
#### Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

**问题与机制。** LLM agents are shaped not only by their language models, but also by the runtime harness that mediates observation, tool use, action execution, feedback interpretation, and trajectory control. We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Runtime Harness Adaptation`；Evaluation=`§5 Deterministic-Agent Evaluation`；Limitations/Counterevidence=`§7 Limitations`；正文 sha256=`fa72e0ba19b1eab39c0ca6018fe1ef29787b2459f8ffec465d88f5ada5244af6`。

<!-- claim:SF-2026-ARXIV-2605-22166:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22166:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22166:end -->

<!-- review:SF-2026-ARXIV-2605-22177:start -->
#### Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles

**问题与机制。** The proliferation of large language models (LLMs) and modular skills has endowed autonomous agents with increasingly powerful capabilities. In this paper, we present Maestro (Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration), a Reinforcement Learning (RL)-driven orchestration framework that reframes heterogeneous multimodal tasks as a sequential decision-making process over a hierarchical model-skill registry. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Method; §3.2 Problem Formulation; §Training Data.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §Benchmarks and Metrics.`；Limitations/Counterevidence=`§4.5 Discussion on Realistic Agentic Benchmarks; §5 Conclusion; §E.4 Additional Discussion`；正文 sha256=`df375605ccd9949ed7b3948657f41431fd73b9744b7bd484e0bbd86e5c032172`。

<!-- claim:SF-2026-ARXIV-2605-22177:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22177:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22177:end -->

<!-- review:SF-2026-ARXIV-2605-22217:start -->
#### Survive or Collapse: The Asymmetric Roles of Data Gating and Reward Grounding in Self-Play RL

**问题与机制。** Self-play reinforcement learning trains language models on their own generated tasks, co-evolving a proposer and solver without human labels. The dominant response treats this as a reward-design problem. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Training Collapse: Empirical Mechanisms; §Appendix A Training Configuration`；Evaluation=`§Experimental matrix.; §Appendix C DSL Replication of Section 3 Results; §C.4 Stratified holdout evaluation`；Limitations/Counterevidence=`§6 Conclusion`；正文 sha256=`5f9ebff025d6869fec00b2e330c5e9ec41be730c5203316c71678e9f1aa25e76`。

<!-- claim:SF-2026-ARXIV-2605-22217:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22217:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22217:end -->

<!-- review:SF-2026-ARXIV-2605-22219:start -->
#### SGR-Bench: Benchmarking Search Agents on State-Gated Retrieval

**问题与机制。** Recent advances in large language models and tool-using agents have expanded the range of benchmarked web tasks. We introduce SGR-Bench, a benchmark for this setting containing 100 expert-curated tasks spanning six source families and 12 public data ecosystems. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§CLI-based LLM Agentic Search Systems.; §Commercial Agent Systems.; §Commercial system evaluation.`；Evaluation=`§SGR-Bench : Benchmarking Search Agents on State-Gated Retrieval; §2.1 Search-Agent Benchmarks; §2.2 Web Navigation and Interaction Benchmarks`；Limitations/Counterevidence=`§5 Conclusion; §Appendix D Extended Limitations Discussion; §Failure case: GPT-5.5 on waterquality_003-g.`；正文 sha256=`551bd63bb81de8ac1342167ad52272ad71284658790941c92ecbbcefe9704f93`。

<!-- claim:SF-2026-ARXIV-2605-22219:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22219:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22219:end -->

<!-- review:SF-2026-ARXIV-2605-22269:start -->
#### MuKV: Multi-Grained KV Cache Compression for Long Streaming Video Question-Answering

**问题与机制。** Long streaming video QA remains challenging due to growing visual tokens and limited reasoning length of large language models (LLMs). Experiments on long-streaming VideoQA benchmarks show that MuKV significantly improves answer accuracy, without sacrificing memory and online QA efficiency. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§3 Method; §3.1 Problem and Method Overview; §Problem Formulation.`；Evaluation=`§4 Experiment; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion`；正文 sha256=`b71e71bbf6983ee6fe5fda3dedc1d0e7aa1f3a5d5687776672d20cdb62cb0d56`。

<!-- claim:SF-2026-ARXIV-2605-22269:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22269:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22269:end -->

<!-- review:SF-2026-ARXIV-2605-22283:start -->
#### Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action

**问题与机制。** We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Method; §A.1 VR Teleoperation System; §Appendix B Methods`；Evaluation=`§4 Experiments; §4.1 Benchmarks; §4.3 Real World Results`；Limitations/Counterevidence=`§5 Conclusion; §D.7 Failure Case Analysis; §D.8 Limitations and Future Directions`；正文 sha256=`6bbbb0695a85ce62ed948b94e08a746279c320c6d96862597f75bf54d7bb1bb0`。

<!-- claim:SF-2026-ARXIV-2605-22283:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22283:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22283:end -->

<!-- review:SF-2026-ARXIV-2605-22297:start -->
#### One LR Doesn't Fit All: Heavy-Tail Guided Layerwise Learning Rates for LLMs

**问题与机制。** Learning rate configuration is a fundamental aspect of modern deep learning. In this paper, we introduce Layerwise Learning Rate (LLR), an adaptive scheme that assigns distinct learning rates to individual Transformer layers. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 Heavy-Tail Layer Diagnostics and Layerwise LR Policy`；Evaluation=`§4–§5 LLM Training Evaluation`；Limitations/Counterevidence=`§6 Conclusion and evaluated-model/scale boundary`；正文 sha256=`1a33f7dd86433bc9092d7f65f7d70f8146b2ee194d7f42c688d0802aa32c59ca`。

<!-- claim:SF-2026-ARXIV-2605-22297:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22297:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22297:end -->

<!-- review:SF-2026-ARXIV-2605-22321:start -->
#### ASEval: Automated Trajectory-Level Security Testing for Autonomous Agents

**问题与机制。** As autonomous agents (e.g., OpenClaw) increasingly operate with deep system-level privileges to execute complex tasks, they introduce severe, unmitigated security risks. As autonomous agents (e.g., OpenClaw) increasingly operate with deep system-level privileges to execute complex tasks, they introduce severe, unmitigated security risks. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Temporal/Spatial/Semantic Evasion Benchmark`；Evaluation=`§5 Security–Utility Evaluation`；Limitations/Counterevidence=`§6 Limitations: single agent platform`；正文 sha256=`84a9b2b075d1d695ae335990ae62ea892fb3cba48d8136550660948ac9820ef1`。

<!-- claim:SF-2026-ARXIV-2605-22321:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22321:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22321:end -->

<!-- review:SF-2026-ARXIV-2605-22333:start -->
#### A First Measurement Study on Authentication Security in Real-World Remote MCP Servers

**问题与机制。** The Model Context Protocol (MCP) is emerging as a common interface connecting large language models (LLMs) with external services. We present the first measurement study of authentication security in real-world remote MCP servers. 系统 owner=`AGENT-MCP`。

**Exact-v1。** Method=`§III Remote-MCP Authentication Measurement Method`；Evaluation=`§V Measurement Results`；Limitations/Counterevidence=`§VI-C Limitations and Future Work`；正文 sha256=`abc7e838684e5cdaa954cab0df10e8a95e2875373e0a8223728dcb3f75db0afd`。

<!-- claim:SF-2026-ARXIV-2605-22333:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22333:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22333:end -->

<!-- review:SF-2026-ARXIV-2605-22337:start -->
#### Meta-Soft: Leveraging Composable Meta-Tokens for Context-Preserving KV Cache Compression

**问题与机制。** The KV cache used in large language models has linearly growing time complexity, so LLMs face memory blow-up and reduced decoding efficiency when they process long contexts. To address this problem, we propose Meta-Soft, a dynamic compression framework based on probe-driven context integration. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§3 Methodology; §3.1 Method Overview; §3.2 Problem Formulation`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Language Modeling Evaluation`；Limitations/Counterevidence=`§5 Conclusion`；正文 sha256=`27d4f85751e57827280dd800a9fdfbbef545fb002a4970c9edca08065f07058c`。

<!-- claim:SF-2026-ARXIV-2605-22337:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22337:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22337:end -->

<!-- review:SF-2026-ARXIV-2605-22343:start -->
#### Sibyl-AutoResearch: Autonomous Research Needs Self-Evolving Trial-and-Error Harnesses, Not Paper Generators

**问题与机制。** Autonomous research systems increasingly make the scientific workflow executable: agents can propose ideas, run code, inspect results, and draft papers. Autonomous research systems increasingly make the scientific workflow executable: agents can propose ideas, run code, inspect results, and draft papers. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 Existing systems and remaining gaps; §4 The Sibyl-AutoResearch framework; §5 The Sibyl system`；Evaluation=`§Appendix E Evaluation protocols`；Limitations/Counterevidence=`§2 Failure modes: where autonomous research loses experience; §7 Limitations and alternative views; §8 Conclusion`；正文 sha256=`b1e7cfd7b8dac9fb3c82a2c1f66b8db973b116f1b22d83405123a694ffc77d62`。

<!-- claim:SF-2026-ARXIV-2605-22343:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22343:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22343:end -->

<!-- review:SF-2026-ARXIV-2605-22411:start -->
#### DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA

**问题与机制。** Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§Memory Systems for LLM Agents.; §3.1 Problem Formulation; §Appendix A Datasets and Baseline Methods`；Evaluation=`§4 Experiment; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion; §C.3.4 Reward-Time Answer Correctness and Failure-Attribution Judge Prompt for r 6 r_{6} and r 7 r_{7}; §Appendix E Limitations and Future work`；正文 sha256=`d6db6b0e6ae637ed59cd7704fb4fe06abe73acd2970445457b79ed5de8c5f518`。

<!-- claim:SF-2026-ARXIV-2605-22411:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22411:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22411:end -->

<!-- review:SF-2026-ARXIV-2605-22416:start -->
#### Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference

**问题与机制。** Hybrid language models like Jamba mix attention layers with State Space Models (SSMs), creating two memory cache types with opposite profiles: Key-Value (KV) caches grow linearly with sequence length, while SSM states stay fixed per layer. We present Asymmetric Virtual Memory Paging (AVMP). 系统 owner=`INFER-GPU-MEMORY`。

**Exact-v1。** Method=`§3 Asymmetric Virtual-Memory Paging`；Evaluation=`§4.2–§4.5 Evaluation`；Limitations/Counterevidence=`§4.6 Limitations`；正文 sha256=`f6a00dc5280170ef69a18de8a123c2e0c549038fd3d1faa6dcd3cbfdc26dccc7`。

<!-- claim:SF-2026-ARXIV-2605-22416:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22416:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22416:end -->

<!-- review:SF-2026-ARXIV-2605-22446:start -->
#### Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts

**问题与机制。** While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Preemptive Runtime Verification Architecture`；Evaluation=`§4 VLA/World-Model Rollout Evaluation`；Limitations/Counterevidence=`§5 Discussion and critic/OOD/resampling limitations`；正文 sha256=`c4be3b9a170b8bf447164d3501ffded8f4a2f79e2e32340e5d3b7d8c9f89ee4d`。

<!-- claim:SF-2026-ARXIV-2605-22446:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22446:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22446:end -->

<!-- review:SF-2026-ARXIV-2605-22456:start -->
#### Steins;Gate Drive: Semantic Safety Arbitration over Structured Futures for Latency-Decoupled LLM Planning

**问题与机制。** Cloud-hosted LLM driver agents provide useful semantic judgments, but their inference latency exceeds stepwise vehicle-control windows. We present SteinsGateDrive, a latency-decoupled planner-runtime architecture in which the worldline metaphor from the eponymous story names one plausible consequence of an intervention: the LLM selects counterfactual driving futures before the final control instant, and a runtime reuses the selected forecast only while safety contracts remain valid. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§III Structured-Future Safety Arbitration`；Evaluation=`§V Evaluation`；Limitations/Counterevidence=`§VII Limitations and Future Work`；正文 sha256=`cbd2d91c9eb91dd2cb2e8565a6e11c0f11ba35b1530093ef03a6e3579a3a6b78`。

<!-- claim:SF-2026-ARXIV-2605-22456:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22456:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22456:end -->

<!-- review:SF-2026-ARXIV-2605-22493:start -->
#### Understanding Multimodal Failure in Action-Chunking Behavioral Cloning

**问题与机制。** Behavioral cloning becomes difficult when the same observation admits several valid actions. We study this problem for action-chunking policies and show that different multimodal parameterizations fail in different ways. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§C.1 Methods; §C.2 Network Architectures; §C.4 Training Details`；Evaluation=`§4 Main Results; §5 Experiments; §Appendix A Notation, Definitions, and Known Results`；Limitations/Counterevidence=`§Understanding Multimodal Failure in Action-Chunking Behavioral Cloning; §6 Conclusion; §Limitations and Future Work`；正文 sha256=`1e357001fef95c4423f3b85a99bec854825b304a41c668556b4bc50de83752d1`。

<!-- claim:SF-2026-ARXIV-2605-22493:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22493:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22493:end -->

<!-- review:SF-2026-ARXIV-2605-22502:start -->
#### Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

**问题与机制。** Agent orchestration frameworks have proliferated, collectively exceeding 290,000 GitHub stars across LangGraph, CrewAI, Google ADK, OpenAI Agents SDK, Semantic Kernel, Strands, and LlamaIndex. We identify three perceived barriers and address each empirically across travel booking (14 nodes), Zoom support (14 nodes, product-specific knowledge), and insurance claims (55 nodes, 6 decision hubs). 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 Evaluation Methodology`；Evaluation=`§3 Evaluation Methodology; §4.1 Experiment 1: Travel Booking (3B); §4.2 Experiment 2: Zoom Support (8B)`；Limitations/Counterevidence=`§4.4 Efficiency and Failure Modes; §8 Conclusion`；正文 sha256=`6b301d11f4d52211e1707625fdae979cbec1495724ff272dbf04502abf58fe60`。

<!-- claim:SF-2026-ARXIV-2605-22502:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22502:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22502:end -->

<!-- review:SF-2026-ARXIV-2605-22505:start -->
#### Towards Direct Evaluation of Harness Optimizers via Priority Ranking

**问题与机制。** Harness optimization enables automated agent creation by having an optimizer agent iteratively update the harness of target agents. To address this, we present a simple, low-cost design to directly evaluate them, namely priority ranking. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§1 Introduction — disclosed mechanism`；Evaluation=`§Towards Direct Evaluation of Harness Optimizers via Priority Ranking; §3 Why is Direct Evaluation Necessary for Harness Optimizers?; §Analysis I: About half of the optimization steps are considered detrimental.`；Limitations/Counterevidence=`§7 Discussions; §8 Conclusion; §Appendix B Limitations`；正文 sha256=`c071ec4b3f5a120f4bf5e884b8df19bb32ce0c080b1aacdbd779da71569ed691`。

<!-- claim:SF-2026-ARXIV-2605-22505:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22505:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22505:end -->

<!-- review:SF-2026-ARXIV-2605-22511:start -->
#### Search-E1: Self-Distillation Drives Self-Evolution in Search-Augmented Reasoning

**问题与机制。** Post-training has become the dominant recipe for turning a language model into a competent search-augmented reasoning agent. We take a step back and ask whether any of this machinery is actually necessary, and propose Search-E1, a self-evolution method that lets a search-augmented agent improve through only vanilla GRPO interleaved with on-policy self-distillation (OPSD). 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§3 Method`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion`；正文 sha256=`f5f0f537676a90c701d209768e368271bb69856e27dac21acb24420b3f77692a`。

<!-- claim:SF-2026-ARXIV-2605-22511:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22511:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22511:end -->

<!-- review:SF-2026-ARXIV-2605-22526:start -->
#### "Refactoring Runaway": Understanding and Mitigating Tangled Refactorings in Coding Agents for Issue Resolution

**问题与机制。** Recent advances in coding agents have shown remarkable progress in software issue resolution. In this paper, we conduct an empirical study on Multi-SWE-bench, analyzing 3,691 valid patches generated by three agent frameworks with 12 LLMs. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§4.1.1. Approach; §4.2.1. Approach; §4.3.1. Approach`；Evaluation=`§4. Empirical Results; §4.1.2. Results; §4.2.2. Results`；Limitations/Counterevidence=`§5. Discussion; §7. Conclusion`；正文 sha256=`23e157bccb852c3243cb932023066cecd338499ee5a00eb030c519804fb23b55`。

<!-- claim:SF-2026-ARXIV-2605-22526:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22526:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22526:end -->

<!-- review:SF-2026-ARXIV-2605-22544:start -->
#### One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation

**问题与机制。** Instruction embedding models have become common among state-of-the-art models, however are evaluated using a single prompt per task. We present an empirical study of prompt sensitivity across 6 embedding models and 11 datasets. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 Methodology`；Evaluation=`§One prompt is not enough: Instruction Sensitivity Undermines Embedding Model Evaluation; §3 Analysis and Discussion; §3.2 Prompt Sensitivity Analysis`；Limitations/Counterevidence=`§3 Analysis and Discussion; §4 Conclusion; §Limitations`；正文 sha256=`c17954b5c40f9f6f6233a6fa2e2bd3742615d30d4941e9872596baca69ae95e4`。

<!-- claim:SF-2026-ARXIV-2605-22544:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22544:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22544:end -->

<!-- review:SF-2026-ARXIV-2605-22564:start -->
#### SynAE: A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations

**问题与机制。** Today, tool-calling agents are commonly evaluated or tested on static datasets of execution traces, including input commands, agent responses, and associated tool calls. We introduce SynAE, an evaluation framework for assessing how well synthetic benchmarks for multi-turn, tool-calling agents replicate and augment the characteristics of real data trajectories. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§SynAE : A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations; §2 SynAE Framework; §Appendix E Prompts for LLM-Based Synthetic Data Generation Methods`；Evaluation=`§SynAE : A Framework for Measuring the Quality of Synthetic Data for Tool-Calling Agent Evaluations; §2.1 Evaluation Metrics; §4. Fidelity metrics for downstream evaluation`；Limitations/Counterevidence=`§4 Conclusions and Limitations`；正文 sha256=`ec07f9656b16a446605f7416dec0947cd33d3ff7a2436c3c3318a79c59b941f0`。

<!-- claim:SF-2026-ARXIV-2605-22564:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22564:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22564:end -->

<!-- review:SF-2026-ARXIV-2605-22566:start -->
#### GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving

**问题与机制。** Large Language Model (LLM)-based agents demonstrate strong reasoning and execution capabilities on complex tasks when guided by structured instructions, commonly referred to as workflows. To address these limitations, we propose a new workflow management paradigm that represents workflows using a unified graph, termed wGraph, where each node corresponds to an atomic operation. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 wGraph and GraphFlow Runtime`；Evaluation=`§5 Agent-Serving Evaluation`；Limitations/Counterevidence=`§6 Conclusion and workflow-generalization boundary`；正文 sha256=`8709bf291b79b8471b252061a97423f3239cdd8577a858149aa12be2d4377fca`。

<!-- claim:SF-2026-ARXIV-2605-22566:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22566:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22566:end -->

<!-- review:SF-2026-ARXIV-2605-22568:start -->
#### Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard

**问题与机制。** The benchmarks used to evaluate AI agents in security-critical roles suffer from crucial weaknesses. The benchmarks used to evaluate AI agents in security-critical roles suffer from crucial weaknesses. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§1 Introduction — disclosed mechanism`；Evaluation=`§Measuring Security Without Fooling Ourselves: Why Benchmarking Agents Is Hard; §2 Benchmark Vulnerabilities; §3.1 Dynamic Benchmarks`；Limitations/Counterevidence=`§5 Discussion; §6 Conclusion`；正文 sha256=`36b41b84d6ab2a104b936e61d011d1efc386f366888a22d8baf9a8a18254f92c`。

<!-- claim:SF-2026-ARXIV-2605-22568:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22568:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22568:end -->

<!-- review:SF-2026-ARXIV-2605-22608:start -->
#### Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents

**问题与机制。** Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2 Agentic CLEAR Method; §3 Agentic CLEAR Framework; §System Level`；Evaluation=`§Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents; §4 Experimental Setup; §5 Agentic CLEAR Issues Results`；Limitations/Counterevidence=`§8 Conclusions`；正文 sha256=`6a7319a0385065eec8b38de6a1cfcf0ad8f2ed2aafabce74dd6e8475ef6077a7`。

<!-- claim:SF-2026-ARXIV-2605-22608:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22608:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22608:end -->

<!-- review:SF-2026-ARXIV-2605-22620:start -->
#### Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework

**问题与机制。** Reinforcement learning with verifiable rewards (RLVR) has substantially improved the reasoning ability of LLMs, but often depends on external supervision from human annotations or gold-standard solutions. We propose a multi-reward RLIF framework that decomposes the training signal into two complementary components: an answer-level reward based on cluster voting and a completion-level reward based on token-wise self-certainty. 系统 owner=`TRAIN-GRPO`。

**Exact-v1。** Method=`§Two is better than one: A Collapse-free Multi-Reward RLIF Training Framework; §3 Method; §Training details.`；Evaluation=`§4 Experiments Results; §4.1 Experimental Setup; §Evaluation.`；Limitations/Counterevidence=`§5 Discussion; §Limitations.; §6 Conclusion`；正文 sha256=`560e9d8c9ab508b755faf2a8052de62d2796ca9a79a59b435eeb147f67f8653a`。

<!-- claim:SF-2026-ARXIV-2605-22620:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22620:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22620:end -->

<!-- review:SF-2026-ARXIV-2605-22634:start -->
#### Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents

**问题与机制。** Skills have become a practical packaging mechanism for agent instructions, workflows, scripts, and reference materials. This paper proposes contractual skills, a GovernSpec-inspired design framework for organizing SKILL.md files as readable task contracts while preserving lightweight skill discovery and progressive loading. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 GovernSpec Contractual Skill Model`；Evaluation=`§6 Evaluation`；Limitations/Counterevidence=`§8 Threats to Validity`；正文 sha256=`342abcd77a52bd20185431c97b7c430e8bba5f28618e41b37f789be32e7d359a`。

<!-- claim:SF-2026-ARXIV-2605-22634:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22634:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22634:end -->

<!-- review:SF-2026-ARXIV-2605-22643:start -->
#### Boiling the Frog: A Multi-Turn Benchmark for Agentic Safety

**问题与机制。** Background. We introduce Boiling the Frog, a benchmark that evaluates whether tool-using AI models deployed in corporate and office settings are susceptible to incremental attacks. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Multi-Turn Agentic-Safety Benchmark`；Evaluation=`§5 Evaluation`；Limitations/Counterevidence=`§7.1 Limitations`；正文 sha256=`be92f5bfc484b237b1a35be27e25cffa5460505da83528b2d2a7512b3d73c6e7`。

<!-- claim:SF-2026-ARXIV-2605-22643:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22643:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22643:end -->

<!-- review:SF-2026-ARXIV-2605-22718:start -->
#### WorldKV: Efficient World Memory with World Retrieval and Compression

**问题与机制。** Autoregressive video diffusion models have enabled real-time, action-conditioned world generation. We propose WorldKV, a training-free framework with two components: World Retrieval and World Compression. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§4 Method; §Appendix C Retrieval Algorithm Ablations`；Evaluation=`§5 Experiments; §5.1 Experimental settings; §Benchmark.`；Limitations/Counterevidence=`§6 Conclusion; §7 Limitations Future Work`；正文 sha256=`db3328383821689a8ec484031f62c4a49625ff431465b94ad907dc2e2b711f91`。

<!-- claim:SF-2026-ARXIV-2605-22718:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22718:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22718:end -->

<!-- review:SF-2026-ARXIV-2605-22721:start -->
#### Self-Evolving Multi-Agent Systems via Decentralized Memory

**问题与机制。** Self-evolving multi-agent systems (MAS) have emerged as a promising route to LLM agents that continually improve from experience, with persistent memory at their foundation. We propose DecentMem, a decentralized memory framework in which each agent maintains its own dual-pool memory -- an exploitation pool of consolidated past trajectories and an exploration pool of LLM-generated candidates for unseen contexts. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§Self-Evolving Multi-Agent Systems via Decentralized Memory; §LLM-based multi-agent systems.; §Memory in multi-agent systems.`；Evaluation=`§5 Theoretical Analysis; §6 Experiment; §6.1 Experimental Setup`；Limitations/Counterevidence=`§8 Conclusion and Limitation; §Limitation.`；正文 sha256=`a077f7408112090a4032d4d71cd4d4bf04126e5786fd5eeaffb227044e023dbe`。

<!-- claim:SF-2026-ARXIV-2605-22721:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22721:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22721:end -->

<!-- review:SF-2026-ARXIV-2605-22731:start -->
#### Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation

**问题与机制。** Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed through their loss functions: maximum likelihood, policy gradients, forward KL, reverse KL, or related objective-level variants. We study a complementary factor: the state distribution on which supervision is applied. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 State-Distribution View of Post-Training`；Evaluation=`§5 SFT/RL/On-Policy Distillation Experiments`；Limitations/Counterevidence=`§6 Limitations`；正文 sha256=`fe62fee2e01df54149436c6a4c46a84e4ad98e9825b059f77368105ca301e530`。

<!-- claim:SF-2026-ARXIV-2605-22731:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22731:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22731:end -->

<!-- review:SF-2026-ARXIV-2605-22769:start -->
#### Understanding Data Temporality Impact on Large Language Models Pre-training

**问题与机制。** Large language models (LLMs) are typically trained on shuffled corpora, yielding models whose knowledge is frozen at train time and whose temporal grounding remains poorly understood. In this work, we study the impact of pre-training dynamics on the acquisition of time-sensitive factual knowledge, focusing specifically on data ordering. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§Understanding Data Temporality Impact on Large Language Models Pre-training; §2 Pre-training Sequential Models; §5.2 Temporal analysis of the sequential pre-training`；Evaluation=`§4 Experimental settings; §5 Results; §5.2 Temporal analysis of the sequential pre-training`；Limitations/Counterevidence=`§7 Perspectives Conclusions`；正文 sha256=`09f4fcc18991531e65cf6cb6d6b5e717db7b3b91cda3fbfe07345ca131b34859`。

<!-- claim:SF-2026-ARXIV-2605-22769:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22769:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22769:end -->

<!-- review:SF-2026-ARXIV-2605-22781:start -->
#### DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback

**问题与机制。** LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). We then present DeltaBox, a novel agent sandbox achieving millisecond level C/R through the two new mechanisms. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 DeltaBox Architecture; §4 Detailed Design`；Evaluation=`§6 Checkpoint/Rollback Evaluation`；Limitations/Counterevidence=`§7 Discussion and sandbox-state boundary`；正文 sha256=`2f83e3151bf0654e4a7c0ac409c73e2bf954638b68116227217eb330139295c4`。

<!-- claim:SF-2026-ARXIV-2605-22781:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22781:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22781:end -->

<!-- review:SF-2026-ARXIV-2605-22786:start -->
#### LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems

**问题与机制。** Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3 LCGuard Latent-Communication Policy`；Evaluation=`§5 KV-Sharing Safety Evaluation`；Limitations/Counterevidence=`Appendix A.9 Limitations`；正文 sha256=`87ad6192aa80d5b25c545f06b6c92ec409e7b81be3123b7d3d9242acfef06168`。

<!-- claim:SF-2026-ARXIV-2605-22786:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22786:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22786:end -->

<!-- review:SF-2026-ARXIV-2605-22794:start -->
#### MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems

**问题与机制。** Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. We argue that source-level adaptation is a fundamentally more general medium: it is Turing-complete, a strict superset of every text-mutable scope, takes effect deterministically rather than through base-model compliance, and does not erode under long-context drift. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems; §2 System Architecture; §5.1 Agentic Systems`；Evaluation=`§4.3 Results: Iteration-1 Outcome`；Limitations/Counterevidence=`§6 Conclusion`；正文 sha256=`834f16c8385e7ad5a173dcdb0d856e95a3fbbaa3c1a038a54db302da585ca23a`。

<!-- claim:SF-2026-ARXIV-2605-22794:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22794:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22794:end -->

<!-- review:SF-2026-ARXIV-2605-22800:start -->
#### The Matching Principle: When Does a Training Penalty Cover Deployment Shift?

**问题与机制。** Ordinary training optimises the task loss and then stops. It never pays for internal representation energy: Jacobians can stay large in directions that never helped the label, so even small label-preserving noise throws the model off---a design gap that classical noise-injection theory fixes at second order, but only when applied as default regularisation, which current practice does not do. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§Training distribution.; §Matched training (one recipe).; §Corollary 3.4 (PGD training remains anisotropic) .`；Evaluation=`§How to read the five results.; §Bridge to experiments.; §Appendix B Per-task experimental supplements`；Limitations/Counterevidence=`§Mapped failures (§ 8.8 ).; §8.8 Named failures and overall pattern; §10 Discussion`；正文 sha256=`bdb9ec7283c8728e937180504806a1cadc884bb88e4d9e609943df06064d6233`。

<!-- claim:SF-2026-ARXIV-2605-22800:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22800:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22800:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-21516 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21516 |
| SF-2026-ARXIV-2605-21543 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21543 |
| SF-2026-ARXIV-2605-21602 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21602 |
| SF-2026-ARXIV-2605-21603 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21603 |
| SF-2026-ARXIV-2605-21606 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21606 |
| SF-2026-ARXIV-2605-21642 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21642 |
| SF-2026-ARXIV-2605-21648 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21648 |
| SF-2026-ARXIV-2605-21649 | score_7_9 | selected | DA-20260522-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260522-01 |
| SF-2026-ARXIV-2605-21768 | score_7_9 | selected | DA-20260522-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260522-02 |
| SF-2026-ARXIV-2605-21779 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21779 |
| SF-2026-ARXIV-2605-21800 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21800 |
| SF-2026-ARXIV-2605-21801 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21801 |
| SF-2026-ARXIV-2605-21803 | score_7_9 | selected | DA-20260522-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260522-03 |
| SF-2026-ARXIV-2605-21847 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21847 |
| SF-2026-ARXIV-2605-21850 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21850 |
| SF-2026-ARXIV-2605-21854 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21854 |
| SF-2026-ARXIV-2605-21856 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21856 |
| SF-2026-ARXIV-2605-21862 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21862 |
| SF-2026-ARXIV-2605-21949 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21949 |
| SF-2026-ARXIV-2605-21951 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21951 |
| SF-2026-ARXIV-2605-21965 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21965 |
| SF-2026-ARXIV-2605-21996 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21996 |
| SF-2026-ARXIV-2605-21997 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-21997 |
| SF-2026-ARXIV-2605-22001 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22001 |
| SF-2026-ARXIV-2605-22014 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22014 |
| SF-2026-ARXIV-2605-22041 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22041 |
| SF-2026-ARXIV-2605-22057 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22057 |
| SF-2026-ARXIV-2605-22074 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22074 |
| SF-2026-ARXIV-2605-22102 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22102 |
| SF-2026-ARXIV-2605-22106 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22106 |
| SF-2026-ARXIV-2605-22138 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22138 |
| SF-2026-ARXIV-2605-22148 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22148 |
| SF-2026-ARXIV-2605-22154 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22154 |
| SF-2026-ARXIV-2605-22164 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22164 |
| SF-2026-ARXIV-2605-22166 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22166 |
| SF-2026-ARXIV-2605-22177 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22177 |
| SF-2026-ARXIV-2605-22217 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22217 |
| SF-2026-ARXIV-2605-22219 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22219 |
| SF-2026-ARXIV-2605-22269 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22269 |
| SF-2026-ARXIV-2605-22283 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22283 |
| SF-2026-ARXIV-2605-22297 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22297 |
| SF-2026-ARXIV-2605-22321 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22321 |
| SF-2026-ARXIV-2605-22333 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22333 |
| SF-2026-ARXIV-2605-22337 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22337 |
| SF-2026-ARXIV-2605-22343 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22343 |
| SF-2026-ARXIV-2605-22411 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22411 |
| SF-2026-ARXIV-2605-22416 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22416 |
| SF-2026-ARXIV-2605-22446 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22446 |
| SF-2026-ARXIV-2605-22456 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22456 |
| SF-2026-ARXIV-2605-22493 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22493 |
| SF-2026-ARXIV-2605-22502 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22502 |
| SF-2026-ARXIV-2605-22505 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22505 |
| SF-2026-ARXIV-2605-22511 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22511 |
| SF-2026-ARXIV-2605-22526 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22526 |
| SF-2026-ARXIV-2605-22544 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22544 |
| SF-2026-ARXIV-2605-22564 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22564 |
| SF-2026-ARXIV-2605-22566 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22566 |
| SF-2026-ARXIV-2605-22568 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22568 |
| SF-2026-ARXIV-2605-22608 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22608 |
| SF-2026-ARXIV-2605-22620 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22620 |
| SF-2026-ARXIV-2605-22634 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22634 |
| SF-2026-ARXIV-2605-22643 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22643 |
| SF-2026-ARXIV-2605-22718 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22718 |
| SF-2026-ARXIV-2605-22721 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22721 |
| SF-2026-ARXIV-2605-22731 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22731 |
| SF-2026-ARXIV-2605-22769 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22769 |
| SF-2026-ARXIV-2605-22781 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22781 |
| SF-2026-ARXIV-2605-22786 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22786 |
| SF-2026-ARXIV-2605-22794 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22794 |
| SF-2026-ARXIV-2605-22800 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22800 |

<!-- analysis-decision:SF-2026-ARXIV-2605-21516:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21516:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21543:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21543:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21602:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21602:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21603:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21603:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21606:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21606:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21642:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21642:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21648:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21648:end -->

<!-- analysis:DA-20260522-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-21649

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260522-01:end -->

<!-- analysis:DA-20260522-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-21768

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260522-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21779:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21800:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21800:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21801:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21801:end -->

<!-- analysis:DA-20260522-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-21803

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260522-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21847:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21850:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21850:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21854:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21854:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21856:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21856:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21862:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21862:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21949:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21949:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21951:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21951:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21965:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21965:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21996:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-21997:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-21997:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22001:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22001:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22014:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22014:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22041:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22041:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22057:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22057:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22074:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22074:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22102:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22102:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22106:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22106:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22138:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22138:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22148:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22148:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22154:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22154:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22164:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22164:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22166:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22166:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22177:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22177:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22217:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22217:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22219:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22219:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22269:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22283:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22283:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22297:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22297:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22321:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22321:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22333:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22333:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22337:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22337:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22343:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22343:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22411:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22411:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22416:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22416:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22446:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22446:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22456:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22456:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22493:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22502:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22502:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22505:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22511:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22511:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22526:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22526:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22544:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22564:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22564:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22566:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22568:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22568:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22608:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22608:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22620:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22620:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22634:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22643:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22643:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22718:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22718:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22721:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22731:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22731:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22769:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22781:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22781:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22786:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22794:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22794:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22800:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22800:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-21516 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-21516 | delta:SF-2026-ARXIV-2605-21516 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21516 |
| SF-2026-ARXIV-2605-21543 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21543 | delta:SF-2026-ARXIV-2605-21543 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21543 |
| SF-2026-ARXIV-2605-21602 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-21602 | delta:SF-2026-ARXIV-2605-21602 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21602 |
| SF-2026-ARXIV-2605-21603 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-21603 | delta:SF-2026-ARXIV-2605-21603 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21603 |
| SF-2026-ARXIV-2605-21606 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21606 | delta:SF-2026-ARXIV-2605-21606 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21606 |
| SF-2026-ARXIV-2605-21642 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21642 | delta:SF-2026-ARXIV-2605-21642 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21642 |
| SF-2026-ARXIV-2605-21648 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21648 | delta:SF-2026-ARXIV-2605-21648 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21648 |
| SF-2026-ARXIV-2605-21649 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-21649 | delta:SF-2026-ARXIV-2605-21649 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21649 |
| SF-2026-ARXIV-2605-21768 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-21768 | delta:SF-2026-ARXIV-2605-21768 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21768 |
| SF-2026-ARXIV-2605-21779 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-21779 | delta:SF-2026-ARXIV-2605-21779 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21779 |
| SF-2026-ARXIV-2605-21800 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-21800 | delta:SF-2026-ARXIV-2605-21800 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21800 |
| SF-2026-ARXIV-2605-21801 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-21801 | delta:SF-2026-ARXIV-2605-21801 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21801 |
| SF-2026-ARXIV-2605-21803 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-21803 | delta:SF-2026-ARXIV-2605-21803 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21803 |
| SF-2026-ARXIV-2605-21847 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-21847 | delta:SF-2026-ARXIV-2605-21847 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21847 |
| SF-2026-ARXIV-2605-21850 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-21850 | delta:SF-2026-ARXIV-2605-21850 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21850 |
| SF-2026-ARXIV-2605-21854 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21854 | delta:SF-2026-ARXIV-2605-21854 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21854 |
| SF-2026-ARXIV-2605-21856 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-21856 | delta:SF-2026-ARXIV-2605-21856 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21856 |
| SF-2026-ARXIV-2605-21862 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-21862 | delta:SF-2026-ARXIV-2605-21862 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21862 |
| SF-2026-ARXIV-2605-21949 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-21949 | delta:SF-2026-ARXIV-2605-21949 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21949 |
| SF-2026-ARXIV-2605-21951 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-21951 | delta:SF-2026-ARXIV-2605-21951 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-21951 |
| SF-2026-ARXIV-2605-21965 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-21965 | delta:SF-2026-ARXIV-2605-21965 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21965 |
| SF-2026-ARXIV-2605-21996 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-21996 | delta:SF-2026-ARXIV-2605-21996 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21996 |
| SF-2026-ARXIV-2605-21997 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-21997 | delta:SF-2026-ARXIV-2605-21997 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21997 |
| SF-2026-ARXIV-2605-22001 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-22001 | delta:SF-2026-ARXIV-2605-22001 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22001 |
| SF-2026-ARXIV-2605-22014 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-22014 | delta:SF-2026-ARXIV-2605-22014 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22014 |
| SF-2026-ARXIV-2605-22041 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-22041 | delta:SF-2026-ARXIV-2605-22041 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22041 |
| SF-2026-ARXIV-2605-22057 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22057 | delta:SF-2026-ARXIV-2605-22057 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22057 |
| SF-2026-ARXIV-2605-22074 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-22074 | delta:SF-2026-ARXIV-2605-22074 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22074 |
| SF-2026-ARXIV-2605-22102 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22102 | delta:SF-2026-ARXIV-2605-22102 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22102 |
| SF-2026-ARXIV-2605-22106 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22106 | delta:SF-2026-ARXIV-2605-22106 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22106 |
| SF-2026-ARXIV-2605-22138 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-22138 | delta:SF-2026-ARXIV-2605-22138 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22138 |
| SF-2026-ARXIV-2605-22148 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22148 | delta:SF-2026-ARXIV-2605-22148 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22148 |
| SF-2026-ARXIV-2605-22154 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-22154 | delta:SF-2026-ARXIV-2605-22154 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22154 |
| SF-2026-ARXIV-2605-22164 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-22164 | delta:SF-2026-ARXIV-2605-22164 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22164 |
| SF-2026-ARXIV-2605-22166 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22166 | delta:SF-2026-ARXIV-2605-22166 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22166 |
| SF-2026-ARXIV-2605-22177 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22177 | delta:SF-2026-ARXIV-2605-22177 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22177 |
| SF-2026-ARXIV-2605-22217 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-22217 | delta:SF-2026-ARXIV-2605-22217 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22217 |
| SF-2026-ARXIV-2605-22219 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-22219 | delta:SF-2026-ARXIV-2605-22219 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22219 |
| SF-2026-ARXIV-2605-22269 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22269 | delta:SF-2026-ARXIV-2605-22269 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22269 |
| SF-2026-ARXIV-2605-22283 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-22283 | delta:SF-2026-ARXIV-2605-22283 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22283 |
| SF-2026-ARXIV-2605-22297 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-22297 | delta:SF-2026-ARXIV-2605-22297 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22297 |
| SF-2026-ARXIV-2605-22321 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-22321 | delta:SF-2026-ARXIV-2605-22321 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22321 |
| SF-2026-ARXIV-2605-22333 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-22333 | delta:SF-2026-ARXIV-2605-22333 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22333 |
| SF-2026-ARXIV-2605-22337 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22337 | delta:SF-2026-ARXIV-2605-22337 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22337 |
| SF-2026-ARXIV-2605-22343 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-22343 | delta:SF-2026-ARXIV-2605-22343 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22343 |
| SF-2026-ARXIV-2605-22411 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-22411 | delta:SF-2026-ARXIV-2605-22411 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22411 |
| SF-2026-ARXIV-2605-22416 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#chapter-54 | books/part-05-inference-system/53-kserve-llm.md#chapter-53;books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-22416 | delta:SF-2026-ARXIV-2605-22416 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22416 |
| SF-2026-ARXIV-2605-22446 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-22446 | delta:SF-2026-ARXIV-2605-22446 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22446 |
| SF-2026-ARXIV-2605-22456 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-22456 | delta:SF-2026-ARXIV-2605-22456 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22456 |
| SF-2026-ARXIV-2605-22493 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-22493 | delta:SF-2026-ARXIV-2605-22493 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22493 |
| SF-2026-ARXIV-2605-22502 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-22502 | delta:SF-2026-ARXIV-2605-22502 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22502 |
| SF-2026-ARXIV-2605-22505 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22505 | delta:SF-2026-ARXIV-2605-22505 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22505 |
| SF-2026-ARXIV-2605-22511 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-22511 | delta:SF-2026-ARXIV-2605-22511 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22511 |
| SF-2026-ARXIV-2605-22526 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-22526 | delta:SF-2026-ARXIV-2605-22526 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22526 |
| SF-2026-ARXIV-2605-22544 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22544 | delta:SF-2026-ARXIV-2605-22544 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22544 |
| SF-2026-ARXIV-2605-22564 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22564 | delta:SF-2026-ARXIV-2605-22564 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22564 |
| SF-2026-ARXIV-2605-22566 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-22566 | delta:SF-2026-ARXIV-2605-22566 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22566 |
| SF-2026-ARXIV-2605-22568 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-22568 | delta:SF-2026-ARXIV-2605-22568 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22568 |
| SF-2026-ARXIV-2605-22608 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22608 | delta:SF-2026-ARXIV-2605-22608 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22608 |
| SF-2026-ARXIV-2605-22620 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-22620 | delta:SF-2026-ARXIV-2605-22620 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22620 |
| SF-2026-ARXIV-2605-22634 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22634 | delta:SF-2026-ARXIV-2605-22634 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22634 |
| SF-2026-ARXIV-2605-22643 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-22643 | delta:SF-2026-ARXIV-2605-22643 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22643 |
| SF-2026-ARXIV-2605-22718 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22718 | delta:SF-2026-ARXIV-2605-22718 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22718 |
| SF-2026-ARXIV-2605-22721 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22721 | delta:SF-2026-ARXIV-2605-22721 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22721 |
| SF-2026-ARXIV-2605-22731 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-22731 | delta:SF-2026-ARXIV-2605-22731 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22731 |
| SF-2026-ARXIV-2605-22769 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-22769 | delta:SF-2026-ARXIV-2605-22769 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22769 |
| SF-2026-ARXIV-2605-22781 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22781 | delta:SF-2026-ARXIV-2605-22781 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22781 |
| SF-2026-ARXIV-2605-22786 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22786 | delta:SF-2026-ARXIV-2605-22786 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22786 |
| SF-2026-ARXIV-2605-22794 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22794 | delta:SF-2026-ARXIV-2605-22794 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22794 |
| SF-2026-ARXIV-2605-22800 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-22800 | delta:SF-2026-ARXIV-2605-22800 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22800 |

<!-- books-review:SF-2026-ARXIV-2605-21516:start -->
<!-- existing:SF-2026-ARXIV-2605-21516:start -->Ch84 already binds inference-time harnesses to capability, evidence granularity, trajectory effects and partial-control reliability trade-offs.<!-- existing:SF-2026-ARXIV-2605-21516:end -->
<!-- delta:SF-2026-ARXIV-2605-21516:start -->Ch84 already binds inference-time harnesses to capability, evidence granularity, trajectory effects and partial-control reliability trade-offs.<!-- delta:SF-2026-ARXIV-2605-21516:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21516:end -->

<!-- books-review:SF-2026-ARXIV-2605-21543:start -->
<!-- existing:SF-2026-ARXIV-2605-21543:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Provable Joint Decontamination for Benchmarking Multiple Large Language Models` 的 source-specific 机制是：In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21543:end -->
<!-- delta:SF-2026-ARXIV-2605-21543:start -->In this work, we formalize multi-model benchmark decontamination as a joint selection problem and propose Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control under stated assumptions.<!-- delta:SF-2026-ARXIV-2605-21543:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21543:end -->

<!-- books-review:SF-2026-ARXIV-2605-21602:start -->
<!-- existing:SF-2026-ARXIV-2605-21602:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']。第67章已区分 raw utilization、有效进展、sensor/health/attestation、漂移与独立 red-team。`Benchmarking and Improving Monitors for Out-Of-Distribution Alignment Failure in LLMs` 的 source-specific 机制是：We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21602:end -->
<!-- delta:SF-2026-ARXIV-2605-21602:start -->We systematically study whether LLM monitoring pipelines can detect these OOD alignment failures by introducing a benchmark called Misalignment Out Of Distribution (MOOD).<!-- delta:SF-2026-ARXIV-2605-21602:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21602:end -->

<!-- books-review:SF-2026-ARXIV-2605-21603:start -->
<!-- existing:SF-2026-ARXIV-2605-21603:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。第49章已把 logical graph、physical execution plan、operator schedule 与 hardware control state 分离。`DynaFlow: Transparent and Flexible Intra-Device Parallelism via Programmable Operator Scheduling` 的 source-specific 机制是：To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21603:end -->
<!-- delta:SF-2026-ARXIV-2605-21603:start -->To address this, we propose DynaFlow, a framework that enables the transparent and flexible integration of intra-device parallelism by decoupling the logical model definition from the physical execution schedule.<!-- delta:SF-2026-ARXIV-2605-21603:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21603:end -->

<!-- books-review:SF-2026-ARXIV-2605-21606:start -->
<!-- existing:SF-2026-ARXIV-2605-21606:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']。第29章已覆盖 on-policy/self-distillation、teacher reliability、state/token selection、full/PEFT 与 reasoning distribution，但尚未承载 reasoning-trace collapse 的独立验收信号。`When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning` 的 source-specific 机制是：To identify this phenomenon, we introduce a branch-viability diagnostic.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21606:end -->
<!-- delta:SF-2026-ARXIV-2605-21606:start -->To identify this phenomenon, we introduce a branch-viability diagnostic.<!-- delta:SF-2026-ARXIV-2605-21606:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21606:end -->

<!-- books-review:SF-2026-ARXIV-2605-21642:start -->
<!-- existing:SF-2026-ARXIV-2605-21642:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。第66章已拥有 versioned EvalSpec、observational/experimental/simulation evidence、noise floor、intervention、benchmark artifact 与 release authority。`Ablate-to-Validate: Are Vision-Language Models Really Using Continuous Thought Tokens?` 的 source-specific 机制是：Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21642:end -->
<!-- delta:SF-2026-ARXIV-2605-21642:start -->Vision-language models (VLMs) are increasingly augmented with continuous or latent non-textual tokens intended to support "visual thinking." Despite improved task accuracy, this alone does not show that models actually use these tokens for reasoning -- gains may arise from confounds such as added context length, special-token anchoring, or training-time regularization.<!-- delta:SF-2026-ARXIV-2605-21642:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21642:end -->

<!-- books-review:SF-2026-ARXIV-2605-21648:start -->
<!-- existing:SF-2026-ARXIV-2605-21648:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Dropout Universality: Scaling Laws and Optimal Scheduling at the Edge-of-Chaos` 的 source-specific 机制是：We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21648:end -->
<!-- delta:SF-2026-ARXIV-2605-21648:start -->We develop a mean-field theory of dropout as a perturbation of critical signal propagation at the edge of chaos, and show that it predicts a simple, no-cost change to standard practice: \emph{front-loaded} dropout schedules cut test loss by \(18\)--\(35\%\) over constant dropout in MLPs and Vision Transformers at fixed budget.<!-- delta:SF-2026-ARXIV-2605-21648:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21648:end -->

<!-- books-review:SF-2026-ARXIV-2605-21649:start -->
<!-- existing:SF-2026-ARXIV-2605-21649:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback。`EntmaxKV: Support-Aware Decoding for Entmax Attention` 的 source-specific 机制是：In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21649:end -->
<!-- delta:SF-2026-ARXIV-2605-21649:start -->In this work, we introduce EntmaxKV, an entmax-native sparse decoding framework that exploits sparsity before KV pages are loaded.<!-- delta:SF-2026-ARXIV-2605-21649:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21649:end -->

<!-- books-review:SF-2026-ARXIV-2605-21768:start -->
<!-- existing:SF-2026-ARXIV-2605-21768:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。第77章已明确 memory admission、credit、provenance、transaction、rollback 与派生状态不能获得事实权威。`Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents` 的 source-specific 机制是：To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21768:end -->
<!-- delta:SF-2026-ARXIV-2605-21768:start -->To address this challenge, we introduce Memory-R2, a training framework for long-horizon memory-augmented LLM agents.<!-- delta:SF-2026-ARXIV-2605-21768:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21768:end -->

<!-- books-review:SF-2026-ARXIV-2605-21779:start -->
<!-- existing:SF-2026-ARXIV-2605-21779:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。第72章已拥有 supply-chain、runtime optimization、taint、bounded verification、exploit evidence 与 fail-closed authority。`FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction` 的 source-specific 机制是：While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21779:end -->
<!-- delta:SF-2026-ARXIV-2605-21779:start -->While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain.<!-- delta:SF-2026-ARXIV-2605-21779:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21779:end -->

<!-- books-review:SF-2026-ARXIV-2605-21800:start -->
<!-- existing:SF-2026-ARXIV-2605-21800:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation` 的 source-specific 机制是：We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21800:end -->
<!-- delta:SF-2026-ARXIV-2605-21800:start -->We present stable-worldmodel (swm), an open-source platform for standardized and reproducible world modeling research and evaluation.<!-- delta:SF-2026-ARXIV-2605-21800:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21800:end -->

<!-- books-review:SF-2026-ARXIV-2605-21801:start -->
<!-- existing:SF-2026-ARXIV-2605-21801:start -->已顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。第33章已覆盖 group variance、token credit、uncertainty/reward proxy 与 PPO/DPO 分支边界。`Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization` 的 source-specific 机制是：Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21801:end -->
<!-- delta:SF-2026-ARXIV-2605-21801:start -->Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap.<!-- delta:SF-2026-ARXIV-2605-21801:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21801:end -->

<!-- books-review:SF-2026-ARXIV-2605-21803:start -->
<!-- existing:SF-2026-ARXIV-2605-21803:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。第28章已覆盖 parameterization、preconditioner geometry、layer-wise LR、noise floor、spectral diagnostics 与训练稳定性，但尚未写明同批 gradient/preconditioner 的两类有限样本偏差。`Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws` 的 source-specific 机制是：We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21803:end -->
<!-- delta:SF-2026-ARXIV-2605-21803:start -->We show that this assumption misses a fundamental axis of representation scaling: how effectively the optimizer converts added FFN width into utilized spectral capacity.<!-- delta:SF-2026-ARXIV-2605-21803:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21803:end -->

<!-- books-review:SF-2026-ARXIV-2605-21847:start -->
<!-- existing:SF-2026-ARXIV-2605-21847:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power。`CompPow: A Case for Component-level GPU Power Management` 的 source-specific 机制是：We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%).；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21847:end -->
<!-- delta:SF-2026-ARXIV-2605-21847:start -->We demonstrate for a variety of ML operations and execution patterns, CompPow has the potential to deliver higher energy efficiency (10%) and even improved performance (5%).<!-- delta:SF-2026-ARXIV-2605-21847:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21847:end -->

<!-- books-review:SF-2026-ARXIV-2605-21850:start -->
<!-- existing:SF-2026-ARXIV-2605-21850:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`ACC: Compiling Agent Trajectories for Long-Context Training` 的 source-specific 机制是：We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-21850:end -->
<!-- delta:SF-2026-ARXIV-2605-21850:start -->We propose Agent Context Compilation (ACC), which converts trajectories from search, software engineering, and database querying agents into long-context QA pairs that combine the original question with tool responses and environment observations gathered across multiple turns, training the model to answer directly without tool use.<!-- delta:SF-2026-ARXIV-2605-21850:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21850:end -->

<!-- existing:SF-2026-ARXIV-2605-21854:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21854:end -->
<!-- delta:SF-2026-ARXIV-2605-21854:start -->We present CrossVLA, an empirical study of cross-paradigm VLA post-training.<!-- delta:SF-2026-ARXIV-2605-21854:end -->
<!-- books-review:SF-2026-ARXIV-2605-21854:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21854:end -->

<!-- existing:SF-2026-ARXIV-2605-21856:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21856:end -->
<!-- delta:SF-2026-ARXIV-2605-21856:start -->Inspired by this, we propose the Zero-CoT Probe (ZCP), a novel black-box detection method that deliberately truncates the entire Chain-of-Thought (CoT) process to expose latent shortcut mappings.<!-- delta:SF-2026-ARXIV-2605-21856:end -->
<!-- books-review:SF-2026-ARXIV-2605-21856:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21856:end -->

<!-- existing:SF-2026-ARXIV-2605-21862:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21862:end -->
<!-- delta:SF-2026-ARXIV-2605-21862:start -->We argue for a persistent action-updated scene state across control calls, and introduce EvoScene-VLA.<!-- delta:SF-2026-ARXIV-2605-21862:end -->
<!-- books-review:SF-2026-ARXIV-2605-21862:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21862:end -->

<!-- existing:SF-2026-ARXIV-2605-21949:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21949:end -->
<!-- delta:SF-2026-ARXIV-2605-21949:start -->We study claim-selective certification: each response is decomposed into verifiable claims, scored against retrieved evidence, and mapped by an intent-aware selector to {full, partial, conflict, abstain}.<!-- delta:SF-2026-ARXIV-2605-21949:end -->
<!-- books-review:SF-2026-ARXIV-2605-21949:start -->owner=`PLATFORM-SECURITY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21949:end -->

<!-- existing:SF-2026-ARXIV-2605-21951:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离', 'Entry Majority 不等于 Independent Evidence Majority', '从 Write-time Summary 转向 Query-conditioned Late Construction', 'Consolidation 与 Forgetting', 'Memory 粒度必须分层，不能用一个 Summary 同时承担证据与画像']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21951:end -->
<!-- delta:SF-2026-ARXIV-2605-21951:start -->把 latent memory 从固定参数附属物改成可扩展 expert pool：routing key、recruitment epoch、domain assignment 与 forgetting 共同形成 memory-policy identity；收益是选择性容量，代价是路由漂移、expert 冲突和难以解释的事实权威。<!-- delta:SF-2026-ARXIV-2605-21951:end -->
<!-- books-review:SF-2026-ARXIV-2605-21951:start -->owner=`AGENT-MEMORY`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21951:end -->

<!-- existing:SF-2026-ARXIV-2605-21965:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Escalation 与 Abstention Threshold 必须联合校准', 'Agentic Retrieval：Relevance 也可以是执行先验']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21965:end -->
<!-- delta:SF-2026-ARXIV-2605-21965:start -->We study how to accelerate such trajectories without changing the final trajectory the model would have taken without acceleration, assuming access to faster but less reliable speculator tools.<!-- delta:SF-2026-ARXIV-2605-21965:end -->
<!-- books-review:SF-2026-ARXIV-2605-21965:start -->owner=`AGENT-RAG`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21965:end -->

<!-- existing:SF-2026-ARXIV-2605-21996:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Pretraining 接口为什么不等于产品接口', 'Demonstration 数据定义了什么', 'SFT 的数学仍是条件最大似然', '一个 loss mask 小例子', '是否应该对 Prompt 也计算 loss', '为什么少量高质量数据也可能有效', 'SFT 数据质量比格式整齐更难', 'Distillation 不是“Teacher 越强越好”', 'Self-distillation 也可以改变 Target Distribution', 'Context Distillation：把可逆 Prompt 行为迁移进权重', 'Outcome Failure 不能单独定位 Perception Credit', 'Prefix Replay 同时承担复用与 Distribution-shift 债务', 'Demonstration Schedule 也是 Objective 的一部分']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21996:end -->
<!-- delta:SF-2026-ARXIV-2605-21996:start -->We propose Patches-to-Trajectories (P2T), which uses $p^\star$ as privileged information during curation and formulates trajectory construction as bi-objective optimization over per-step effectiveness and trajectory length.<!-- delta:SF-2026-ARXIV-2605-21996:end -->
<!-- books-review:SF-2026-ARXIV-2605-21996:start -->owner=`TRAIN-SFT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21996:end -->

<!-- existing:SF-2026-ARXIV-2605-21997:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-21997:end -->
<!-- delta:SF-2026-ARXIV-2605-21997:start -->This single design decision yields three properties that retrieval-and-summarization memory systems do not provide: deterministic replay of any run from its log, cheap forking that branches a run at any event without re-executing the shared prefix, and end-to-end lineage from a high-level goal down to the individual model call that produced each artifact.<!-- delta:SF-2026-ARXIV-2605-21997:end -->
<!-- books-review:SF-2026-ARXIV-2605-21997:start -->owner=`AGENT-WORKFLOW`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-21997:end -->

<!-- existing:SF-2026-ARXIV-2605-22001:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22001:end -->
<!-- delta:SF-2026-ARXIV-2605-22001:start -->We identify a systematic blind spot: when payloads are generated to mimic the domain vocabulary and authority structures of the target document, what we call domain camouflaged injection, standard detectors fail to flag them, with detection rates dropping from 93.8% to 9.7% on Llama 3.1 8B and from 100% to 55.6% on Gemini 2.0 Flash.<!-- delta:SF-2026-ARXIV-2605-22001:end -->
<!-- books-review:SF-2026-ARXIV-2605-22001:start -->owner=`PLATFORM-SECURITY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22001:end -->

<!-- existing:SF-2026-ARXIV-2605-22014:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory', '从 Collective 到 AI State Transfer', 'Federated Tensor Type 定义一轮协议能表达什么', '跨 Model Family 的 Federated 协作不能继续聚合 Parameters', '最简单的扩展：Data Parallel']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22014:end -->
<!-- delta:SF-2026-ARXIV-2605-22014:start -->We present LiveR, a live reconfiguration runtime for elastic LLM training that replaces storage-backed restart with a live, bounded-memory handoff between mixed-parallel training worlds.<!-- delta:SF-2026-ARXIV-2605-22014:end -->
<!-- books-review:SF-2026-ARXIV-2605-22014:start -->owner=`TRAIN-DISTRIBUTED-TRAINING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22014:end -->

<!-- existing:SF-2026-ARXIV-2605-22041:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Escalation 与 Abstention Threshold 必须联合校准', 'Agentic Retrieval：Relevance 也可以是执行先验']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22041:end -->
<!-- delta:SF-2026-ARXIV-2605-22041:start -->We propose RADAR, a framework that models reliable context selection as a graph-based energy minimization problem, solved exactly via Max-Flow Min-Cut.<!-- delta:SF-2026-ARXIV-2605-22041:end -->
<!-- books-review:SF-2026-ARXIV-2605-22041:start -->owner=`AGENT-RAG`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22041:end -->

<!-- existing:SF-2026-ARXIV-2605-22057:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22057:end -->
<!-- delta:SF-2026-ARXIV-2605-22057:start -->We present FlyRoute, a self-evolving profiling framework that grows capability evidence from real traffic: dispatch candidates, quality-gate successful pairs into each agent's success store, periodically distill evidence into learned capability descriptions, and inject those descriptions together with BM25-retrieved successes into an LLM router.<!-- delta:SF-2026-ARXIV-2605-22057:end -->
<!-- books-review:SF-2026-ARXIV-2605-22057:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22057:end -->

<!-- existing:SF-2026-ARXIV-2605-22074:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', 'Reverse KL 会把“找到高奖励”收缩成单一路径', "Reward hacking 与 Goodhart's Law", 'Majority Vote 可能只是在压尖已有分布', 'Sequence reward 与 token updates 的错位', 'Training–Inference Mismatch 也可能来自 Numerical Execution Identity', '从持久权重更新到条件化 Activation Intervention']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22074:end -->
<!-- delta:SF-2026-ARXIV-2605-22074:start -->将终局 reward 拆成从 reference chain 派生的可验证 subproblem curriculum；curriculum builder 拥有难度/边界，verifier 只提交可判定 credit，代价是 reference bias 与子问题捷径，失败时回退到终局可验证任务。<!-- delta:SF-2026-ARXIV-2605-22074:end -->
<!-- books-review:SF-2026-ARXIV-2605-22074:start -->owner=`TRAIN-RLHF`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22074:end -->

<!-- existing:SF-2026-ARXIV-2605-22102:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Coordination State 必须有显式 Owner 与 Commit Transition', 'Latent Communication 只能压缩 Payload，不能隐藏 Identity', 'Pairwise coupling 不能外推 group dynamics', 'Review notes']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22102:end -->
<!-- delta:SF-2026-ARXIV-2605-22102:start -->We propose ExComm, a communication protocol for exploration-stage agentic test-time scaling.<!-- delta:SF-2026-ARXIV-2605-22102:end -->
<!-- books-review:SF-2026-ARXIV-2605-22102:start -->owner=`AGENT-MULTI-AGENT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22102:end -->

<!-- existing:SF-2026-ARXIV-2605-22106:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本', '稀疏 KV 保留的是派生状态，不只是被抽样的 Token', '高命中率首先是统计口径，不是端到端加速比例', '流式输入把 Cache 变成可续租的 Session State', 'Eviction 与 Offload']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22106:end -->
<!-- delta:SF-2026-ARXIV-2605-22106:start -->Motivated by this, we propose ArborKV, a structure-aware eviction framework that couples a lightweight value estimator with a tree-aware allocation policy, and performs purely token-extractive eviction with lazy rehydration to support revisits.<!-- delta:SF-2026-ARXIV-2605-22106:end -->
<!-- books-review:SF-2026-ARXIV-2605-22106:start -->owner=`INFER-KV-CACHE`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22106:end -->

<!-- existing:SF-2026-ARXIV-2605-22138:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Plan 不是解释文本', '从目标到状态图', 'Decomposition 的价值与代价', '依赖、并行与 Critical Path', 'Subtask Parallelism 与 Trial Parallelism 解决的不是同一个等待', 'Replanning 的触发条件', 'Search-based Planning 的边界', '先校准不确定性，再决定行动、询问或探索', '局部 Replan 后必须回归全部已接受约束', 'Goal、Constraint 与 Policy', '从 Project Brief 到可验证 Task Contracts', '完成证据与 Verification', '条件化机制分支与共存边界']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22138:end -->
<!-- delta:SF-2026-ARXIV-2605-22138:start -->We argue efficient agentic reasoning benefits from decomposing decision-making into three systems: simulative reasoning (System II) grounding deliberation in future-state prediction via a world model; self-regulation (System III) deciding when and how deeply to plan via a learned configurator; and reactive execution (System I) handling fine-grained action.<!-- delta:SF-2026-ARXIV-2605-22138:end -->
<!-- books-review:SF-2026-ARXIV-2605-22138:start -->owner=`AGENT-PLANNING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22138:end -->

<!-- existing:SF-2026-ARXIV-2605-22148:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22148:end -->
<!-- delta:SF-2026-ARXIV-2605-22148:start -->A large language model (LLM) agent that writes and edits its own skill library must also decide which skills to keep, from one noisy scalar per skill.<!-- delta:SF-2026-ARXIV-2605-22148:end -->
<!-- books-review:SF-2026-ARXIV-2605-22148:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22148:end -->

<!-- existing:SF-2026-ARXIV-2605-22154:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22154:end -->
<!-- delta:SF-2026-ARXIV-2605-22154:start -->Despite the prevalence of idle time in most agentic scenarios, existing works treat it as an unavoidable overhead or propose restricted solutions that overlook varying computational budgets across different tool calls and future observation uncertainty, thereby leading to suboptimal utilization of idle time.<!-- delta:SF-2026-ARXIV-2605-22154:end -->
<!-- books-review:SF-2026-ARXIV-2605-22154:start -->owner=`AGENT-WORKFLOW`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22154:end -->

<!-- existing:SF-2026-ARXIV-2605-22164:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线', '从单尺度预测到 Abstraction × Timescale Hierarchy', 'Next-observation generation', 'Action-conditioned transition', '把已知自运动从环境变化中因子化', 'Goal 属于 Planner Cost，不能成为 Transition 的答案通道', 'Sparse Keyframe Prediction 是 Dense Rollout 之前的 Planner Branch']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22164:end -->
<!-- delta:SF-2026-ARXIV-2605-22164:start -->world-model repair metric 必须比较 horizon-matched trajectory reachability，而不是只比较相邻 latent 的欧氏距离；它把可达性与 rollout horizon 纳入 state identity，代价是额外模拟成本和模型偏差。<!-- delta:SF-2026-ARXIV-2605-22164:end -->
<!-- books-review:SF-2026-ARXIV-2605-22164:start -->owner=`MULTIMODAL-WORLD-MODELS`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22164:end -->

<!-- existing:SF-2026-ARXIV-2605-22166:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22166:end -->
<!-- delta:SF-2026-ARXIV-2605-22166:start -->We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments.<!-- delta:SF-2026-ARXIV-2605-22166:end -->
<!-- books-review:SF-2026-ARXIV-2605-22166:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22166:end -->

<!-- existing:SF-2026-ARXIV-2605-22177:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22177:end -->
<!-- delta:SF-2026-ARXIV-2605-22177:start -->In this paper, we present Maestro (Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration), a Reinforcement Learning (RL)-driven orchestration framework that reframes heterogeneous multimodal tasks as a sequential decision-making process over a hierarchical model-skill registry.<!-- delta:SF-2026-ARXIV-2605-22177:end -->
<!-- books-review:SF-2026-ARXIV-2605-22177:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22177:end -->

<!-- existing:SF-2026-ARXIV-2605-22217:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么移除 Critic 会有吸引力', '同 Prompt 生成一组 Responses', 'Group-relative advantage', '一个三样本小例子', 'GRPO 的 clipped objective', '正负 Advantage 不必共享同一 Clipping Contract', 'Sequence Reward 怎样作用到 Tokens', '为什么 GRPO 不是“无 Critic 的免费 PPO”', 'Group Size 改变什么', '从 GRPO 到 DAPO：后续演化不是单线版本升级', 'DAPO 把朴素 GRPO 的运行失败拆成四处修补', 'DAPO 之后，各分支继续修改不同约束', 'Verifiable Reward 的优势与边界']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22217:end -->
<!-- delta:SF-2026-ARXIV-2605-22217:start -->The dominant response treats this as a reward-design problem.<!-- delta:SF-2026-ARXIV-2605-22217:end -->
<!-- books-review:SF-2026-ARXIV-2605-22217:start -->owner=`TRAIN-GRPO`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22217:end -->

<!-- existing:SF-2026-ARXIV-2605-22219:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 可以预测未来需求，但必须允许取消与过期', 'SSD Filtered ANN 要把 Superset Traversal 与最终验证分开', 'Index Update 可以借用 Search I/O Stall，但不能借走 Freshness Authority', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Escalation 与 Abstention Threshold 必须联合校准', 'Agentic Retrieval：Relevance 也可以是执行先验']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22219:end -->
<!-- delta:SF-2026-ARXIV-2605-22219:start -->We introduce SGR-Bench, a benchmark for this setting containing 100 expert-curated tasks spanning six source families and 12 public data ecosystems.<!-- delta:SF-2026-ARXIV-2605-22219:end -->
<!-- books-review:SF-2026-ARXIV-2605-22219:start -->owner=`AGENT-RAG`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22219:end -->

<!-- existing:SF-2026-ARXIV-2605-22269:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本', '稀疏 KV 保留的是派生状态，不只是被抽样的 Token', '高命中率首先是统计口径，不是端到端加速比例', '流式输入把 Cache 变成可续租的 Session State', 'Eviction 与 Offload']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22269:end -->
<!-- delta:SF-2026-ARXIV-2605-22269:start -->Experiments on long-streaming VideoQA benchmarks show that MuKV significantly improves answer accuracy, without sacrificing memory and online QA efficiency.<!-- delta:SF-2026-ARXIV-2605-22269:end -->
<!-- books-review:SF-2026-ARXIV-2605-22269:start -->owner=`INFER-KV-CACHE`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22269:end -->

<!-- existing:SF-2026-ARXIV-2605-22283:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22283:end -->
<!-- delta:SF-2026-ARXIV-2605-22283:start -->We introduce SOMA, the Spatial Memory framework for Out-of-Vision Manipulation in Vision-Language-Action (VLA) models.<!-- delta:SF-2026-ARXIV-2605-22283:end -->
<!-- books-review:SF-2026-ARXIV-2605-22283:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22283:end -->

<!-- existing:SF-2026-ARXIV-2605-22297:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Whitening 的收益取决于 Gradient Spectrum 所在 Regime', 'Matrix-aware Step 可以与 Sign Step 按成本交替', 'Optimizer Update 要尊重参数块的对称性', 'Batch、tokens 与 optimizer steps 不是同一计量', 'Preconditioner 与 Gradient 共享 Batch 时会改变估计语义']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22297:end -->
<!-- delta:SF-2026-ARXIV-2605-22297:start -->In this paper, we introduce Layerwise Learning Rate (LLR), an adaptive scheme that assigns distinct learning rates to individual Transformer layers.<!-- delta:SF-2026-ARXIV-2605-22297:end -->
<!-- books-review:SF-2026-ARXIV-2605-22297:start -->owner=`TRAIN-PRETRAINING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22297:end -->

<!-- existing:SF-2026-ARXIV-2605-22321:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22321:end -->
<!-- delta:SF-2026-ARXIV-2605-22321:start -->As autonomous agents (e.g., OpenClaw) increasingly operate with deep system-level privileges to execute complex tasks, they introduce severe, unmitigated security risks.<!-- delta:SF-2026-ARXIV-2605-22321:end -->
<!-- books-review:SF-2026-ARXIV-2605-22321:start -->owner=`PLATFORM-SECURITY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22321:end -->

<!-- existing:SF-2026-ARXIV-2605-22333:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么需要协议层', 'Host、Client、Server', 'Data Layer 与 Transport Layer', 'Server Primitives', 'Lifecycle 与 Version Contract', 'Update 2026-07-29 — 从连接会话到显式请求契约', 'MCP 不等于 Tool Authorization', 'Sampling、Elicitation 与递归能力', 'MCP 与 Workflow/Multi-Agent 的边界', 'Tool Catalog 扩大后，Discovery 与 Execution 必须分离', '从单工具扫描到组合级 Admission', 'Observability', 'Consequential Output 必须携带可独立验证的 Claim Receipt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22333:end -->
<!-- delta:SF-2026-ARXIV-2605-22333:start -->We present the first measurement study of authentication security in real-world remote MCP servers.<!-- delta:SF-2026-ARXIV-2605-22333:end -->
<!-- books-review:SF-2026-ARXIV-2605-22333:start -->owner=`AGENT-MCP`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22333:end -->

<!-- existing:SF-2026-ARXIV-2605-22337:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本', '稀疏 KV 保留的是派生状态，不只是被抽样的 Token', '高命中率首先是统计口径，不是端到端加速比例', '流式输入把 Cache 变成可续租的 Session State', 'Eviction 与 Offload']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22337:end -->
<!-- delta:SF-2026-ARXIV-2605-22337:start -->To address this problem, we propose Meta-Soft, a dynamic compression framework based on probe-driven context integration.<!-- delta:SF-2026-ARXIV-2605-22337:end -->
<!-- books-review:SF-2026-ARXIV-2605-22337:start -->owner=`INFER-KV-CACHE`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22337:end -->

<!-- existing:SF-2026-ARXIV-2605-22343:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22343:end -->
<!-- delta:SF-2026-ARXIV-2605-22343:start -->自主研究 harness 需要把 trial evidence 到后续行为、再到 harness revision 分成两次可审计转换；trial log 不能直接成为结论或代码更新，acceptor、negative evidence 与 rollback 分别拥有提交权。<!-- delta:SF-2026-ARXIV-2605-22343:end -->
<!-- books-review:SF-2026-ARXIV-2605-22343:start -->owner=`AGENT-WORKFLOW`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22343:end -->

<!-- existing:SF-2026-ARXIV-2605-22411:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离', 'Entry Majority 不等于 Independent Evidence Majority', '从 Write-time Summary 转向 Query-conditioned Late Construction', 'Consolidation 与 Forgetting', 'Memory 粒度必须分层，不能用一个 Summary 同时承担证据与画像']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22411:end -->
<!-- delta:SF-2026-ARXIV-2605-22411:start -->We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation.<!-- delta:SF-2026-ARXIV-2605-22411:end -->
<!-- books-review:SF-2026-ARXIV-2605-22411:start -->owner=`AGENT-MEMORY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22411:end -->

<!-- existing:SF-2026-ARXIV-2605-22416:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从 memory hierarchy 开始', '显存里到底有什么', '固定、动态与瞬时占用', '一个可用容量小例子', '一个有时效边界的硬件算例', 'KV Cache 为什么改变推理显存', 'Fragmentation 与 Reserve 为什么真实存在', '三类缓解路径', '减少 Bytes', '提高利用率', '扩展层级', 'Weights 与 KV 的联合 HBM 预算：可提交的运行时精度页', '逆向硬件证据必须声明 claim provenance']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22416:end -->
<!-- delta:SF-2026-ARXIV-2605-22416:start -->混合 Mamba–Transformer runtime 不能再用统一 page size 和统一 eviction：recurrent state、attention KV 与 weights 需要不同 page identity、fault path 和 placement owner；收益以更多页表、迁移与碎片治理为代价。<!-- delta:SF-2026-ARXIV-2605-22416:end -->
<!-- books-review:SF-2026-ARXIV-2605-22416:start -->owner=`INFER-GPU-MEMORY`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22416:end -->

<!-- existing:SF-2026-ARXIV-2605-22446:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22446:end -->
<!-- delta:SF-2026-ARXIV-2605-22446:start -->To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination.<!-- delta:SF-2026-ARXIV-2605-22446:end -->
<!-- books-review:SF-2026-ARXIV-2605-22446:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22446:end -->

<!-- existing:SF-2026-ARXIV-2605-22456:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22456:end -->
<!-- delta:SF-2026-ARXIV-2605-22456:start -->We present SteinsGateDrive, a latency-decoupled planner-runtime architecture in which the worldline metaphor from the eponymous story names one plausible consequence of an intervention: the LLM selects counterfactual driving futures before the final control instant, and a runtime reuses the selected forecast only while safety contracts remain valid.<!-- delta:SF-2026-ARXIV-2605-22456:end -->
<!-- books-review:SF-2026-ARXIV-2605-22456:start -->owner=`AGENT-WORKFLOW`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22456:end -->

<!-- existing:SF-2026-ARXIV-2605-22493:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22493:end -->
<!-- delta:SF-2026-ARXIV-2605-22493:start -->action chunk 在减少推理频率时也把感知误差锁入更长 open-loop interval；chunk horizon 必须与 observation freshness、controller correction budget 和安全中断点联合版本化，而不是只调一个长度超参。<!-- delta:SF-2026-ARXIV-2605-22493:end -->
<!-- books-review:SF-2026-ARXIV-2605-22493:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22493:end -->

<!-- existing:SF-2026-ARXIV-2605-22502:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Pretraining 接口为什么不等于产品接口', 'Demonstration 数据定义了什么', 'SFT 的数学仍是条件最大似然', '一个 loss mask 小例子', '是否应该对 Prompt 也计算 loss', '为什么少量高质量数据也可能有效', 'SFT 数据质量比格式整齐更难', 'Distillation 不是“Teacher 越强越好”', 'Self-distillation 也可以改变 Target Distribution', 'Context Distillation：把可逆 Prompt 行为迁移进权重', 'Outcome Failure 不能单独定位 Perception Credit', 'Prefix Replay 同时承担复用与 Distribution-shift 债务', 'Demonstration Schedule 也是 Objective 的一部分']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22502:end -->
<!-- delta:SF-2026-ARXIV-2605-22502:start -->We identify three perceived barriers and address each empirically across travel booking (14 nodes), Zoom support (14 nodes, product-specific knowledge), and insurance claims (55 nodes, 6 decision hubs).<!-- delta:SF-2026-ARXIV-2605-22502:end -->
<!-- books-review:SF-2026-ARXIV-2605-22502:start -->owner=`TRAIN-SFT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22502:end -->

<!-- existing:SF-2026-ARXIV-2605-22505:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22505:end -->
<!-- delta:SF-2026-ARXIV-2605-22505:start -->评估 harness optimizer 不能只看最终 agent 分数；应把 component-level update priority 作为中间 action evidence，并保留它与真实多步改善的相关性边界，代价是增加分层标签与回放成本。<!-- delta:SF-2026-ARXIV-2605-22505:end -->
<!-- books-review:SF-2026-ARXIV-2605-22505:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22505:end -->

<!-- existing:SF-2026-ARXIV-2605-22511:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么移除 Critic 会有吸引力', '同 Prompt 生成一组 Responses', 'Group-relative advantage', '一个三样本小例子', 'GRPO 的 clipped objective', '正负 Advantage 不必共享同一 Clipping Contract', 'Sequence Reward 怎样作用到 Tokens', '为什么 GRPO 不是“无 Critic 的免费 PPO”', 'Group Size 改变什么', '从 GRPO 到 DAPO：后续演化不是单线版本升级', 'DAPO 把朴素 GRPO 的运行失败拆成四处修补', 'DAPO 之后，各分支继续修改不同约束', 'Verifiable Reward 的优势与边界']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22511:end -->
<!-- delta:SF-2026-ARXIV-2605-22511:start -->We take a step back and ask whether any of this machinery is actually necessary, and propose Search-E1, a self-evolution method that lets a search-augmented agent improve through only vanilla GRPO interleaved with on-policy self-distillation (OPSD).<!-- delta:SF-2026-ARXIV-2605-22511:end -->
<!-- books-review:SF-2026-ARXIV-2605-22511:start -->owner=`TRAIN-GRPO`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22511:end -->

<!-- existing:SF-2026-ARXIV-2605-22526:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22526:end -->
<!-- delta:SF-2026-ARXIV-2605-22526:start -->In this paper, we conduct an empirical study on Multi-SWE-bench, analyzing 3,691 valid patches generated by three agent frameworks with 12 LLMs.<!-- delta:SF-2026-ARXIV-2605-22526:end -->
<!-- books-review:SF-2026-ARXIV-2605-22526:start -->owner=`AGENT-WORKFLOW`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22526:end -->

<!-- existing:SF-2026-ARXIV-2605-22544:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22544:end -->
<!-- delta:SF-2026-ARXIV-2605-22544:start -->We present an empirical study of prompt sensitivity across 6 embedding models and 11 datasets.<!-- delta:SF-2026-ARXIV-2605-22544:end -->
<!-- books-review:SF-2026-ARXIV-2605-22544:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22544:end -->

<!-- existing:SF-2026-ARXIV-2605-22564:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22564:end -->
<!-- delta:SF-2026-ARXIV-2605-22564:start -->We introduce SynAE, an evaluation framework for assessing how well synthetic benchmarks for multi-turn, tool-calling agents replicate and augment the characteristics of real data trajectories.<!-- delta:SF-2026-ARXIV-2605-22564:end -->
<!-- books-review:SF-2026-ARXIV-2605-22564:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22564:end -->

<!-- existing:SF-2026-ARXIV-2605-22566:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身', 'Learned Environment Transition 是可撤销分支，不是事实提交', 'Clarification 与 Workflow-level Speculation 都是有损 Admission', 'Toolspace 变大后，Schema 与执行中间态不应都塞回 Prompt']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22566:end -->
<!-- delta:SF-2026-ARXIV-2605-22566:start -->To address these limitations, we propose a new workflow management paradigm that represents workflows using a unified graph, termed wGraph, where each node corresponds to an atomic operation.<!-- delta:SF-2026-ARXIV-2605-22566:end -->
<!-- books-review:SF-2026-ARXIV-2605-22566:start -->owner=`AGENT-WORKFLOW`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22566:end -->

<!-- existing:SF-2026-ARXIV-2605-22568:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22568:end -->
<!-- delta:SF-2026-ARXIV-2605-22568:start -->The benchmarks used to evaluate AI agents in security-critical roles suffer from crucial weaknesses.<!-- delta:SF-2026-ARXIV-2605-22568:end -->
<!-- books-review:SF-2026-ARXIV-2605-22568:start -->owner=`PLATFORM-SECURITY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22568:end -->

<!-- existing:SF-2026-ARXIV-2605-22608:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22608:end -->
<!-- delta:SF-2026-ARXIV-2605-22608:start -->To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework.<!-- delta:SF-2026-ARXIV-2605-22608:end -->
<!-- books-review:SF-2026-ARXIV-2605-22608:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22608:end -->

<!-- existing:SF-2026-ARXIV-2605-22620:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么移除 Critic 会有吸引力', '同 Prompt 生成一组 Responses', 'Group-relative advantage', '一个三样本小例子', 'GRPO 的 clipped objective', '正负 Advantage 不必共享同一 Clipping Contract', 'Sequence Reward 怎样作用到 Tokens', '为什么 GRPO 不是“无 Critic 的免费 PPO”', 'Group Size 改变什么', '从 GRPO 到 DAPO：后续演化不是单线版本升级', 'DAPO 把朴素 GRPO 的运行失败拆成四处修补', 'DAPO 之后，各分支继续修改不同约束', 'Verifiable Reward 的优势与边界']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22620:end -->
<!-- delta:SF-2026-ARXIV-2605-22620:start -->多 reward RLIF 需要显式监控 reward-channel collapse 与 gradient conflict；aggregator 只能形成 update proposal，单通道 guardrail 和 held-out behavior gate 拥有否决权，避免平均奖励掩盖局部退化。<!-- delta:SF-2026-ARXIV-2605-22620:end -->
<!-- books-review:SF-2026-ARXIV-2605-22620:start -->owner=`TRAIN-GRPO`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22620:end -->

<!-- existing:SF-2026-ARXIV-2605-22634:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22634:end -->
<!-- delta:SF-2026-ARXIV-2605-22634:start -->This paper proposes contractual skills, a GovernSpec-inspired design framework for organizing SKILL.md files as readable task contracts while preserving lightweight skill discovery and progressive loading.<!-- delta:SF-2026-ARXIV-2605-22634:end -->
<!-- books-review:SF-2026-ARXIV-2605-22634:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22634:end -->

<!-- existing:SF-2026-ARXIV-2605-22643:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22643:end -->
<!-- delta:SF-2026-ARXIV-2605-22643:start -->We introduce Boiling the Frog, a benchmark that evaluates whether tool-using AI models deployed in corporate and office settings are susceptible to incremental attacks.<!-- delta:SF-2026-ARXIV-2605-22643:end -->
<!-- books-review:SF-2026-ARXIV-2605-22643:start -->owner=`PLATFORM-SECURITY`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22643:end -->

<!-- existing:SF-2026-ARXIV-2605-22718:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本', '稀疏 KV 保留的是派生状态，不只是被抽样的 Token', '高命中率首先是统计口径，不是端到端加速比例', '流式输入把 Cache 变成可续租的 Session State', 'Eviction 与 Offload']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22718:end -->
<!-- delta:SF-2026-ARXIV-2605-22718:start -->We propose WorldKV, a training-free framework with two components: World Retrieval and World Compression.<!-- delta:SF-2026-ARXIV-2605-22718:end -->
<!-- books-review:SF-2026-ARXIV-2605-22718:start -->owner=`INFER-KV-CACHE`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22718:end -->

<!-- existing:SF-2026-ARXIV-2605-22721:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Coordination State 必须有显式 Owner 与 Commit Transition', 'Latent Communication 只能压缩 Payload，不能隐藏 Identity', 'Pairwise coupling 不能外推 group dynamics', 'Review notes']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22721:end -->
<!-- delta:SF-2026-ARXIV-2605-22721:start -->多 Agent memory 不应默认中央仓库：每个 agent 可拥有 exploitation/exploration pool，协调层只交换受限摘要或反馈；隐私与多样性收益换来重复、漂移和跨 agent 一致性成本，中央库在共享真值场景仍更合理。<!-- delta:SF-2026-ARXIV-2605-22721:end -->
<!-- books-review:SF-2026-ARXIV-2605-22721:start -->owner=`AGENT-MULTI-AGENT`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22721:end -->

<!-- existing:SF-2026-ARXIV-2605-22731:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', 'Reverse KL 会把“找到高奖励”收缩成单一路径', "Reward hacking 与 Goodhart's Law", 'Majority Vote 可能只是在压尖已有分布', 'Sequence reward 与 token updates 的错位', 'Training–Inference Mismatch 也可能来自 Numerical Execution Identity', '从持久权重更新到条件化 Activation Intervention']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22731:end -->
<!-- delta:SF-2026-ARXIV-2605-22731:start -->后训练方法的关键差异应沿 state-distribution 解释，而非只沿 token objective：SFT、on-policy distillation 与 RL 分别在何种 policy-induced state 上提供监督；覆盖扩大换来 rollout 成本与 staleness，旧的静态 SFT 在目标状态分布稳定时仍成立。<!-- delta:SF-2026-ARXIV-2605-22731:end -->
<!-- books-review:SF-2026-ARXIV-2605-22731:start -->owner=`TRAIN-RLHF`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22731:end -->

<!-- existing:SF-2026-ARXIV-2605-22769:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', 'Data Reuse 改变的是 Layer-wise Growth，不只是 Epoch 计数', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Filter Threshold 必须绑定 Compute-to-Unique-Data Regime', 'Synthetic data：从“先生成再打分”到 Specification Compilation', '没有真实后端时，Synthetic API State 只能是派生训练状态', 'Failure-driven Curriculum：难例必须来自可重放失败，而不是模型自信']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22769:end -->
<!-- delta:SF-2026-ARXIV-2605-22769:start -->训练语料的时间顺序属于 data/objective identity：顺序化 snapshot 能改善事实的时间绑定，但会降低随机混合带来的 i.i.d. 假设；应保存 snapshot time、ordering policy 与重复率，旧 shuffle 在非时间任务仍成立。<!-- delta:SF-2026-ARXIV-2605-22769:end -->
<!-- books-review:SF-2026-ARXIV-2605-22769:start -->owner=`TRAIN-DATA`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22769:end -->

<!-- existing:SF-2026-ARXIV-2605-22781:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22781:end -->
<!-- delta:SF-2026-ARXIV-2605-22781:start -->We then present DeltaBox, a novel agent sandbox achieving millisecond level C/R through the two new mechanisms.<!-- delta:SF-2026-ARXIV-2605-22781:end -->
<!-- books-review:SF-2026-ARXIV-2605-22781:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22781:end -->

<!-- existing:SF-2026-ARXIV-2605-22786:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', 'Agent 数量应由边际信息价值分配，而不是固定扩容', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Coordination State 必须有显式 Owner 与 Commit Transition', 'Latent Communication 只能压缩 Payload，不能隐藏 Identity', 'Pairwise coupling 不能外推 group dynamics', 'Review notes']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22786:end -->
<!-- delta:SF-2026-ARXIV-2605-22786:start -->To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems.<!-- delta:SF-2026-ARXIV-2605-22786:end -->
<!-- books-review:SF-2026-ARXIV-2605-22786:start -->owner=`AGENT-MULTI-AGENT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22786:end -->

<!-- existing:SF-2026-ARXIV-2605-22794:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22794:end -->
<!-- delta:SF-2026-ARXIV-2605-22794:start -->Agent self-evolution 从 prompt/config 进入 source-level rewriting 后，候选变成可执行供应链 revision；production failure batch、ephemeral replay、user consent、health probe 与 rollback 共同拥有 promotion gate，表达力提升以更大 blast radius 为代价。<!-- delta:SF-2026-ARXIV-2605-22794:end -->
<!-- books-review:SF-2026-ARXIV-2605-22794:start -->owner=`AGENT-PLATFORM`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22794:end -->

<!-- existing:SF-2026-ARXIV-2605-22800:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Whitening 的收益取决于 Gradient Spectrum 所在 Regime', 'Matrix-aware Step 可以与 Sign Step 按成本交替', 'Optimizer Update 要尊重参数块的对称性', 'Batch、tokens 与 optimizer steps 不是同一计量', 'Preconditioner 与 Gradient 共享 Batch 时会改变估计语义']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22800:end -->
<!-- delta:SF-2026-ARXIV-2605-22800:start -->训练正则要按 deployment shift direction 定义 coverage：未知方向用 even-spread baseline，已知方向才做 matched penalty；错误轴会留下 residual floor，深网证据仍是受限实验而非普遍定理。<!-- delta:SF-2026-ARXIV-2605-22800:end -->
<!-- books-review:SF-2026-ARXIV-2605-22800:start -->owner=`TRAIN-PRETRAINING`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22800:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260522-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260522 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260522-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260522-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=70；selected=3；all others retain completed reviews | passed |
| SA-20260522-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=597；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260522/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260522/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-22.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
