# Daily Research — 2026-05-27

**Research Date:** 2026-05-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-26 09:00:00 ～ 2026-05-27 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 633 个注册 arXiv identity，冻结 64 个 Source Family；pre-denominator closure=569，withdrawn pre-denominator=0。33 个旧候选被迁回正确 owner day，4 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-27 |
| Window End | 2026-05-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260527-CREATED-19113218bf4106c1 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-26T09:00:00+08:00 | 2026-05-27T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 633 | SF-2026-ARXIV-2605-26118;SF-2026-ARXIV-2605-26120;SF-2026-ARXIV-2605-26128;SF-2026-ARXIV-2605-26132;SF-2026-ARXIV-2605-26147;SF-2026-ARXIV-2605-26154;SF-2026-ARXIV-2605-26156;SF-2026-ARXIV-2605-26158;SF-2026-ARXIV-2605-26159;SF-2026-ARXIV-2605-26161;SF-2026-ARXIV-2605-26162;SF-2026-ARXIV-2605-26165;SF-2026-ARXIV-2605-26172;SF-2026-ARXIV-2605-26177;SF-2026-ARXIV-2605-26184;SF-2026-ARXIV-2605-26200;SF-2026-ARXIV-2605-26242;SF-2026-ARXIV-2605-26248;SF-2026-ARXIV-2605-26252;SF-2026-ARXIV-2605-26266;SF-2026-ARXIV-2605-26269;SF-2026-ARXIV-2605-26282;SF-2026-ARXIV-2605-26289;SF-2026-ARXIV-2605-26297;SF-2026-ARXIV-2605-26298;SF-2026-ARXIV-2605-26302;SF-2026-ARXIV-2605-26321;SF-2026-ARXIV-2605-26323;SF-2026-ARXIV-2605-26327;SF-2026-ARXIV-2605-26340;SF-2026-ARXIV-2605-26362;SF-2026-ARXIV-2605-26379;SF-2026-ARXIV-2605-26384;SF-2026-ARXIV-2605-26403;SF-2026-ARXIV-2605-26418;SF-2026-ARXIV-2605-26433;SF-2026-ARXIV-2605-26440;SF-2026-ARXIV-2605-26444;SF-2026-ARXIV-2605-26457;SF-2026-ARXIV-2605-26461;SF-2026-ARXIV-2605-26485;SF-2026-ARXIV-2605-26497;SF-2026-ARXIV-2605-26508;SF-2026-ARXIV-2605-26521;SF-2026-ARXIV-2605-26542;SF-2026-ARXIV-2605-26558;SF-2026-ARXIV-2605-26563;SF-2026-ARXIV-2605-26574;SF-2026-ARXIV-2605-26606;SF-2026-ARXIV-2605-26667;SF-2026-ARXIV-2605-26684;SF-2026-ARXIV-2605-26691;SF-2026-ARXIV-2605-26720;SF-2026-ARXIV-2605-26730;SF-2026-ARXIV-2605-26731;SF-2026-ARXIV-2605-26754;SF-2026-ARXIV-2605-26778;SF-2026-ARXIV-2605-27091;SF-2026-ARXIV-2605-27220;SF-2026-ARXIV-2605-27292;SF-2026-ARXIV-2605-27328;SF-2026-ARXIV-2605-27333;SF-2026-ARXIV-2605-27361;SF-2026-ARXIV-2605-27366 | created-day pages=closed; OAI category sets=closed; direct same-day OAI=471 | 2026-05-27T09:00:00+08:00 | coverage:SRC-ARXIV:20260527 | — |

<!-- coverage:SRC-ARXIV:20260527:start -->全量 raw inventory=633；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260527:end -->

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
| SF-2026-ARXIV-2605-26118 | arXiv:2605.26118v1 | paper-v1:2605.26118 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-26118 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26118 | yes |
| SF-2026-ARXIV-2605-26120 | arXiv:2605.26120v1 | paper-v1:2605.26120 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-26120 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26120 | yes |
| SF-2026-ARXIV-2605-26128 | arXiv:2605.26128v1 | paper-v1:2605.26128 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26128 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26128 | no |
| SF-2026-ARXIV-2605-26132 | arXiv:2605.26132v1 | paper-v1:2605.26132 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26132 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26132 | no |
| SF-2026-ARXIV-2605-26147 | arXiv:2605.26147v1 | paper-v1:2605.26147 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26147 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26147 | no |
| SF-2026-ARXIV-2605-26154 | arXiv:2605.26154v1 | paper-v1:2605.26154 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26154 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26154 | no |
| SF-2026-ARXIV-2605-26156 | arXiv:2605.26156v1 | paper-v1:2605.26156 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26156 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26156 | no |
| SF-2026-ARXIV-2605-26158 | arXiv:2605.26158v1 | paper-v1:2605.26158 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26158 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26158 | no |
| SF-2026-ARXIV-2605-26159 | arXiv:2605.26159v1 | paper-v1:2605.26159 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26159 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26159 | no |
| SF-2026-ARXIV-2605-26161 | arXiv:2605.26161v1 | paper-v1:2605.26161 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26161 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26161 | no |
| SF-2026-ARXIV-2605-26162 | arXiv:2605.26162v1 | paper-v1:2605.26162 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26162 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-26162 | no |
| SF-2026-ARXIV-2605-26165 | arXiv:2605.26165v1 | paper-v1:2605.26165 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26165 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26165 | no |
| SF-2026-ARXIV-2605-26172 | arXiv:2605.26172v1 | paper-v1:2605.26172 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26172 | self | — | new_in_window | MODEL-SAMPLING | Integrate | books-review:SF-2026-ARXIV-2605-26172 | no |
| SF-2026-ARXIV-2605-26177 | arXiv:2605.26177v1 | paper-v1:2605.26177 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26177 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26177 | no |
| SF-2026-ARXIV-2605-26184 | arXiv:2605.26184v1 | paper-v1:2605.26184 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26184 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-26184 | no |
| SF-2026-ARXIV-2605-26200 | arXiv:2605.26200v1 | paper-v1:2605.26200 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26200 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26200 | no |
| SF-2026-ARXIV-2605-26242 | arXiv:2605.26242v1 | paper-v1:2605.26242 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26242 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26242 | no |
| SF-2026-ARXIV-2605-26248 | arXiv:2605.26248v1 | paper-v1:2605.26248 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26248 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | Integrate | books-review:SF-2026-ARXIV-2605-26248 | no |
| SF-2026-ARXIV-2605-26252 | arXiv:2605.26252v1 | paper-v1:2605.26252 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26252 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-26252 | no |
| SF-2026-ARXIV-2605-26266 | arXiv:2605.26266v1 | paper-v1:2605.26266 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26266 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26266 | no |
| SF-2026-ARXIV-2605-26269 | arXiv:2605.26269v1 | paper-v1:2605.26269 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26269 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26269 | no |
| SF-2026-ARXIV-2605-26282 | arXiv:2605.26282v1 | paper-v1:2605.26282 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26282 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-26282 | no |
| SF-2026-ARXIV-2605-26289 | arXiv:2605.26289v1 | paper-v1:2605.26289 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26289 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-26289 | no |
| SF-2026-ARXIV-2605-26297 | arXiv:2605.26297v1 | paper-v1:2605.26297 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26297 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-26297 | no |
| SF-2026-ARXIV-2605-26298 | arXiv:2605.26298v1 | paper-v1:2605.26298 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26298 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-26298 | no |
| SF-2026-ARXIV-2605-26302 | arXiv:2605.26302v1 | paper-v1:2605.26302 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26302 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-26302 | no |
| SF-2026-ARXIV-2605-26321 | arXiv:2605.26321v1 | paper-v1:2605.26321 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26321 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-26321 | no |
| SF-2026-ARXIV-2605-26323 | arXiv:2605.26323v1 | paper-v1:2605.26323 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26323 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26323 | no |
| SF-2026-ARXIV-2605-26327 | arXiv:2605.26327v1 | paper-v1:2605.26327 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26327 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-26327 | no |
| SF-2026-ARXIV-2605-26340 | arXiv:2605.26340v1 | paper-v1:2605.26340 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26340 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-26340 | no |
| SF-2026-ARXIV-2605-26362 | arXiv:2605.26362v1 | paper-v1:2605.26362 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26362 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26362 | no |
| SF-2026-ARXIV-2605-26379 | arXiv:2605.26379v1 | paper-v1:2605.26379 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26379 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-26379 | no |
| SF-2026-ARXIV-2605-26384 | arXiv:2605.26384v1 | paper-v1:2605.26384 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26384 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2605-26384 | no |
| SF-2026-ARXIV-2605-26403 | arXiv:2605.26403v1 | paper-v1:2605.26403 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26403 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-26403 | no |
| SF-2026-ARXIV-2605-26418 | arXiv:2605.26418v1 | paper-v1:2605.26418 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26418 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26418 | no |
| SF-2026-ARXIV-2605-26433 | arXiv:2605.26433v1 | paper-v1:2605.26433 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26433 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26433 | no |
| SF-2026-ARXIV-2605-26440 | arXiv:2605.26440v1 | paper-v1:2605.26440 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-26440 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26440 | yes |
| SF-2026-ARXIV-2605-26444 | arXiv:2605.26444v1 | paper-v1:2605.26444 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26444 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26444 | yes |
| SF-2026-ARXIV-2605-26457 | arXiv:2605.26457v1 | paper-v1:2605.26457 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26457 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26457 | no |
| SF-2026-ARXIV-2605-26461 | arXiv:2605.26461v1 | paper-v1:2605.26461 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26461 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Integrate | books-review:SF-2026-ARXIV-2605-26461 | no |
| SF-2026-ARXIV-2605-26485 | arXiv:2605.26485v1 | paper-v1:2605.26485 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26485 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26485 | no |
| SF-2026-ARXIV-2605-26497 | arXiv:2605.26497v1 | paper-v1:2605.26497 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26497 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26497 | no |
| SF-2026-ARXIV-2605-26508 | arXiv:2605.26508v1 | paper-v1:2605.26508 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26508 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26508 | no |
| SF-2026-ARXIV-2605-26521 | arXiv:2605.26521v1 | paper-v1:2605.26521 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26521 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-26521 | no |
| SF-2026-ARXIV-2605-26542 | arXiv:2605.26542v1 | paper-v1:2605.26542 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26542 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-26542 | no |
| SF-2026-ARXIV-2605-26558 | arXiv:2605.26558v1 | paper-v1:2605.26558 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-26558 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26558 | no |
| SF-2026-ARXIV-2605-26563 | arXiv:2605.26563v1 | paper-v1:2605.26563 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26563 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26563 | no |
| SF-2026-ARXIV-2605-26574 | arXiv:2605.26574v1 | paper-v1:2605.26574 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26574 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26574 | no |
| SF-2026-ARXIV-2605-26606 | arXiv:2605.26606v1 | paper-v1:2605.26606 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26606 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26606 | no |
| SF-2026-ARXIV-2605-26667 | arXiv:2605.26667v1 | paper-v1:2605.26667 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26667 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26667 | no |
| SF-2026-ARXIV-2605-26684 | arXiv:2605.26684v1 | paper-v1:2605.26684 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26684 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26684 | no |
| SF-2026-ARXIV-2605-26691 | arXiv:2605.26691v1 | paper-v1:2605.26691 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26691 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26691 | no |
| SF-2026-ARXIV-2605-26720 | arXiv:2605.26720v1 | paper-v1:2605.26720 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26720 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26720 | no |
| SF-2026-ARXIV-2605-26730 | arXiv:2605.26730v1 | paper-v1:2605.26730 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26730 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26730 | no |
| SF-2026-ARXIV-2605-26731 | arXiv:2605.26731v1 | paper-v1:2605.26731 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-26731 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26731 | no |
| SF-2026-ARXIV-2605-26754 | arXiv:2605.26754v1 | paper-v1:2605.26754 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26754 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-26754 | no |
| SF-2026-ARXIV-2605-26778 | arXiv:2605.26778v1 | paper-v1:2605.26778 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-26778 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-26778 | no |
| SF-2026-ARXIV-2605-27091 | arXiv:2605.27091v1 | paper-v1:2605.27091 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27091 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-27091 | no |
| SF-2026-ARXIV-2605-27220 | arXiv:2605.27220v1 | paper-v1:2605.27220 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27220 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27220 | no |
| SF-2026-ARXIV-2605-27292 | arXiv:2605.27292v1 | paper-v1:2605.27292 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27292 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27292 | no |
| SF-2026-ARXIV-2605-27328 | arXiv:2605.27328v1 | paper-v1:2605.27328 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27328 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27328 | no |
| SF-2026-ARXIV-2605-27333 | arXiv:2605.27333v1 | paper-v1:2605.27333 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27333 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27333 | no |
| SF-2026-ARXIV-2605-27361 | arXiv:2605.27361v1 | paper-v1:2605.27361 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27361 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27361 | no |
| SF-2026-ARXIV-2605-27366 | arXiv:2605.27366v1 | paper-v1:2605.27366 | 2026-W22 | 2026-05-27 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27366 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27366 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-26118 | RP-23054ee884dd8a49 | standard | arXiv:2605.26118v1 | SRC-ARXIV@arXiv:2605.26118v1 | https://arxiv.org/html/2605.26118v1#S2 | https://arxiv.org/html/2605.26118v1#S4 | https://arxiv.org/html/2605.26118v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-26118 | complete |
| SF-2026-ARXIV-2605-26120 | RP-2361bc3e343a691e | standard | arXiv:2605.26120v1 | SRC-ARXIV@arXiv:2605.26120v1 | https://arxiv.org/html/2605.26120v1#S2 | https://arxiv.org/html/2605.26120v1#S4 | https://arxiv.org/html/2605.26120v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-26120 | complete |
| SF-2026-ARXIV-2605-26128 | RP-05c52662d53cb2ec | deep | arXiv:2605.26128v1 | SRC-ARXIV@arXiv:2605.26128v1 | arXiv:2605.26128v1 HTML — §2.2 Structured Decoding as a Serving-System Interface | arXiv:2605.26128v1 HTML — §5 Experimental Protocol; §6 Empirical Results; §7.4 What the Result Establishes | arXiv:2605.26128v1 HTML — §7 Discussion; §10 Conclusion | https://arxiv.org/html/2605.26128v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-26128 | complete |
| SF-2026-ARXIV-2605-26132 | RP-e21e2a628b925565 | deep | arXiv:2605.26132v1 | SRC-ARXIV@arXiv:2605.26132v1 | arXiv:2605.26132v1 HTML — §4.5 Training vs. Test-Time Compute; §C.1.2 Training | arXiv:2605.26132v1 HTML — §4 Experiments; §Appendix C Experimental Details; §C.1.3 Evaluation | arXiv:2605.26132v1 HTML — §5 Discussion | https://arxiv.org/html/2605.26132v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-26132 | complete |
| SF-2026-ARXIV-2605-26147 | RP-34f654f3eebfbbf7 | deep | arXiv:2605.26147v1 | SRC-ARXIV@arXiv:2605.26147v1 | https://arxiv.org/html/2605.26147v1 — §3–§5 DAG evidence accumulation and sequential routing | https://arxiv.org/html/2605.26147v1 — §6–§8 controlled experiments and ablations | https://arxiv.org/html/2605.26147v1 — §9 Discussion; conjugate-belief assumptions and tested-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-26147 | complete |
| SF-2026-ARXIV-2605-26154 | RP-a85ec357fb35c24c | deep | arXiv:2605.26154v1 | SRC-ARXIV@arXiv:2605.26154v1 | arXiv:2605.26154v1 HTML — §3 MemMorph memory-poisoning and tool-hijack attack | arXiv:2605.26154v1 HTML — §5 agent evaluation | arXiv:2605.26154v1 HTML — §6 limitations and memory/tool boundary | arXiv:2605.26154v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26154 | complete |
| SF-2026-ARXIV-2605-26156 | RP-37b6b283a7459e71 | deep | arXiv:2605.26156v1 | SRC-ARXIV@arXiv:2605.26156v1 | arXiv:2605.26156v1 HTML — §3 Threat model; §4 Contextual-bandit black-box style attack; §5 Analysis | arXiv:2605.26156v1 HTML — §6 Evaluation on chatbot leaderboards and automated peer review, including stealth and mitigation | arXiv:2605.26156v1 HTML — §7 Conclusion and Appendix experiments: tested-judge/task/style scope; semantic-preservation proxy and adaptive-query-budget boundary | arXiv:2605.26156v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26156 | complete |
| SF-2026-ARXIV-2605-26158 | RP-b367918348f7313d | deep | arXiv:2605.26158v1 | SRC-ARXIV@arXiv:2605.26158v1 | arXiv:2605.26158v1 HTML — §3 Safety Instability external/internal diagnostics; §4 fragmented scene-anchored probing and synthesis | arXiv:2605.26158v1 HTML — §5 HarmBench/MM-SafetyBench experiments, ablations and classical-defense checks; Appendix B.7 human judge validation | arXiv:2605.26158v1 HTML — § Impact Statement: instability band remains diagnostic, thresholds are not calibrated per input, and cross-fragment evidence requires future context-aware defense | arXiv:2605.26158v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26158 | complete |
| SF-2026-ARXIV-2605-26159 | RP-f5f75c1fa4bd5977 | deep | arXiv:2605.26159v1 | SRC-ARXIV@arXiv:2605.26159v1 | arXiv:2605.26159v1 HTML — §3 Device Context Protocol safety architecture | arXiv:2605.26159v1 HTML — §5 constrained-device evaluation | arXiv:2605.26159v1 HTML — §6 limitations and device-capability boundary | arXiv:2605.26159v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26159 | complete |
| SF-2026-ARXIV-2605-26161 | RP-543f0c20e6bda927 | deep | arXiv:2605.26161v1 | SRC-ARXIV@arXiv:2605.26161v1 | arXiv:2605.26161v1 HTML — §3 Problem formulation; §4 TSFMAudit; §4.1 adaptation traces; §4.2 reference-model debiasing; §4.3 calibration and decision | arXiv:2605.26161v1 HTML — §5 Experiments on six TSFMs/187 datasets; §5.5 practical deployment; Appendix B audit protocol | arXiv:2605.26161v1 HTML — Appendix A contamination labels and transformed-duplicate semantics; proxy labels depend on incomplete official corpus documentation | arXiv:2605.26161v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26161 | complete |
| SF-2026-ARXIV-2605-26162 | RP-45970fe3e3649800 | deep | arXiv:2605.26162v1 | SRC-ARXIV@arXiv:2605.26162v1 | arXiv:2605.26162v1 HTML — §4 PushCen-ADFL; §4.2 centroid regularization; §4.3 compression; §4.4 push-sum aggregation; §4.5 buffered updates; Appendix C event-driven state accounting | arXiv:2605.26162v1 HTML — §5 Experiments; §5.1.4 delayed-client protocol; §5.2 accuracy/communication/overhead; §5.3 delayed clients | arXiv:2605.26162v1 HTML — §4.6 assumptions and Appendix C: bounded staleness, directed mixing, bounded compression error and simulated event-driven network | arXiv:2605.26162v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26162 | complete |
| SF-2026-ARXIV-2605-26165 | RP-f17aa139de5900d4 | deep | arXiv:2605.26165v1 | SRC-ARXIV@arXiv:2605.26165v1 | arXiv:2605.26165v1 HTML — §3 tool-schema compression | arXiv:2605.26165v1 HTML — §4 agentic-RAG evaluation | arXiv:2605.26165v1 HTML — §5 limitations and context/tool-library boundary | arXiv:2605.26165v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26165 | complete |
| SF-2026-ARXIV-2605-26172 | RP-0bcdc2abff58b0be | deep | arXiv:2605.26172v1 | SRC-ARXIV@arXiv:2605.26172v1 | arXiv:2605.26172v1 HTML — §3 reasoning-basin construction; §4 conservative additive evidence and residual encoder | arXiv:2605.26172v1 HTML — §5 three model families/three math benchmarks and wrong-majority analyses | arXiv:2605.26172v1 HTML — §6 limitations: same-pool evidence, math tasks and bounded oracle headroom | arXiv:2605.26172v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26172 | complete |
| SF-2026-ARXIV-2605-26177 | RP-be4182df62e34fa5 | deep | arXiv:2605.26177v1 | SRC-ARXIV@arXiv:2605.26177v1 | arXiv:2605.26177v1 HTML — §3 repository perturbations; §4 derived tasks; §5 diagnosis and RepoAnchor | arXiv:2605.26177v1 HTML — §2 setup; §3–§5 performance, structural-hint validation and behavior analysis | arXiv:2605.26177v1 HTML — Appendix C.1 Limitations; repository/task/model scope | arXiv:2605.26177v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26177 | complete |
| SF-2026-ARXIV-2605-26184 | RP-1bbeb09186d72bb2 | deep | arXiv:2605.26184v1 | SRC-ARXIV@arXiv:2605.26184v1 | arXiv:2605.26184v1 HTML — §3 noise model, proxies, online estimation and adaptive controller | arXiv:2605.26184v1 HTML — §4 reasoning/code/scale/training-health results and signal ablations | arXiv:2605.26184v1 HTML — Appendix B honest covariance assessment; Appendix C idealized stability assumptions; Appendix E overhead | arXiv:2605.26184v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26184 | complete |
| SF-2026-ARXIV-2605-26200 | RP-1f1c0861889910a9 | deep | arXiv:2605.26200v1 | SRC-ARXIV@arXiv:2605.26200v1 | arXiv:2605.26200v1 HTML — §2 workflow/scientific closure; §3 three collapses; §6 design implications | arXiv:2605.26200v1 HTML — §4–§5 survey-coded patterns and remediation analysis | arXiv:2605.26200v1 HTML — §8 Limitations; §9 alternative views; survey/position evidence rather than causal experiment | arXiv:2605.26200v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26200 | complete |
| SF-2026-ARXIV-2605-26242 | RP-93575f8fdc83c897 | deep | arXiv:2605.26242v1 | SRC-ARXIV@arXiv:2605.26242v1 | arXiv:2605.26242v1 HTML — §2 privileged-access and second-order-computation criteria; §3 two paradigm re-analyses | arXiv:2605.26242v1 HTML — §4 input-only controls and internal-vs-input intervention discrimination | arXiv:2605.26242v1 HTML — §5 conclusion: negative evidence for tested introspection paradigms, not proof of impossibility | arXiv:2605.26242v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26242 | complete |
| SF-2026-ARXIV-2605-26248 | RP-018dad8db9cf209e | deep | arXiv:2605.26248v1 | SRC-ARXIV@arXiv:2605.26248v1 | arXiv:2605.26248v1 HTML — §2 unified multi-axis functional form; §3 estimation and extrapolation | arXiv:2605.26248v1 HTML — §4 vision/language/math/RL fits and held-out extrapolation | arXiv:2605.26248v1 HTML — §5 predictability limits; §6 discussion across tested architectures/tasks | arXiv:2605.26248v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26248 | complete |
| SF-2026-ARXIV-2605-26252 | RP-c5578097389b24ec | deep | arXiv:2605.26252v1 | SRC-ARXIV@arXiv:2605.26252v1 | arXiv:2605.26252v1 HTML — §2 record-abstraction failures; §3 GEM operators/correctness; §4 MemState realization | arXiv:2605.26252v1 HTML — §4 prototype feasibility and §5 research agenda | arXiv:2605.26252v1 HTML — §6 Conclusion; prototype/vision evidence without comparative production evaluation | arXiv:2605.26252v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26252 | complete |
| SF-2026-ARXIV-2605-26266 | RP-4e1a345d136eb5a2 | deep | arXiv:2605.26266v1 | SRC-ARXIV@arXiv:2605.26266v1 | arXiv:2605.26266v1 HTML — §4.1 Jensen attention bias; §4.2 correction; §4.3 cost | arXiv:2605.26266v1 HTML — §5 video-diffusion and partial-prefill experiments plus ablations | arXiv:2605.26266v1 HTML — §6 Limitations & future work; model/quantizer and partial-prefill transfer boundary | arXiv:2605.26266v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26266 | complete |
| SF-2026-ARXIV-2605-26269 | RP-30c10fa728e119b2 | deep | arXiv:2605.26269v1 | SRC-ARXIV@arXiv:2605.26269v1 | arXiv:2605.26269v1 HTML — §2 properties/threat model; §3 intent-execution formalization; §4 security games; §5 defenses | arXiv:2605.26269v1 HTML — §6–§7 protocol, adversarial advantage, utility and cost | arXiv:2605.26269v1 HTML — §8 residual risk; later limitations section and finite task/model envelope | arXiv:2605.26269v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26269 | complete |
| SF-2026-ARXIV-2605-26282 | RP-e5b3472137a0a8c4 | deep | arXiv:2605.26282v1 | SRC-ARXIV@arXiv:2605.26282v1 | arXiv:2605.26282v1 HTML — §3 latent-world searched trajectories and diffusion policy optimization | arXiv:2605.26282v1 HTML — §4 offline, online and offline-to-online evaluation plus capacity scaling | arXiv:2605.26282v1 HTML — §5 limitations: learned-world bias, benchmark/control horizon and compute envelope | arXiv:2605.26282v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26282 | complete |
| SF-2026-ARXIV-2605-26289 | RP-b552e0eacbe8ac1a | deep | arXiv:2605.26289v1 | SRC-ARXIV@arXiv:2605.26289v1 | arXiv:2605.26289v1 HTML — §2 workload/cost; §3 sequence pool, caches, scheduler, speculative decode and streaming validator | arXiv:2605.26289v1 HTML — §4–§5 multi-turn/burst/cache latency evaluation | arXiv:2605.26289v1 HTML — §6.2 Limitations; single implementation/hardware and prompt-determinism assumptions | arXiv:2605.26289v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26289 | complete |
| SF-2026-ARXIV-2605-26297 | RP-a495ebf43665c112 | deep | arXiv:2605.26297v1 | SRC-ARXIV@arXiv:2605.26297v1 | arXiv:2605.26297v1 HTML — §3 trace infrastructure; §4 agent execution; §5 runtime; §6 tool-call characterization | arXiv:2605.26297v1 HTML — §7 Evaluation — five agent benchmarks across reasoning/non-reasoning Gemma/Qwen configurations | arXiv:2605.26297v1 HTML — §8 Conclusion; benchmark/model/serving-stack characterization boundary | arXiv:2605.26297v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26297 | complete |
| SF-2026-ARXIV-2605-26298 | RP-c41de72ef69254e1 | deep | arXiv:2605.26298v1 | SRC-ARXIV@arXiv:2605.26298v1 | arXiv:2605.26298v1 HTML — §2 threat model; §3 policy; §4 Landlock/seccomp/network design; §5 implementation | arXiv:2605.26298v1 HTML — §6 effectiveness, startup, throughput, COW, network and compatibility | arXiv:2605.26298v1 HTML — §8 threat-model/integration/rollback limitations; local Linux host only | arXiv:2605.26298v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26298 | complete |
| SF-2026-ARXIV-2605-26302 | RP-724fcffd8d221ecf | deep | arXiv:2605.26302v1 | SRC-ARXIV@arXiv:2605.26302v1 | arXiv:2605.26302v1 HTML — §3 aging taxonomy; §4 benchmark; §5 component diagnosis and counterfactual intervention | arXiv:2605.26302v1 HTML — §6 setup/results and Appendix D typed-state/controller probes | arXiv:2605.26302v1 HTML — §7 Conclusion; synthetic scenarios, closed agents and aging-preview boundary | arXiv:2605.26302v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26302 | complete |
| SF-2026-ARXIV-2605-26321 | RP-0e6c762a1a2cdda8 | deep | arXiv:2605.26321v1 | SRC-ARXIV@arXiv:2605.26321v1 | arXiv:2605.26321v1 HTML — §2 Anchor; §3 ERP-Bench; Appendix D deterministic generator and E verifier | arXiv:2605.26321v1 HTML — §4 evaluation; appendices G–I reliability, failure and validity checks | arXiv:2605.26321v1 HTML — §5 Limitations; single ERP domain and generated-artifact scope | arXiv:2605.26321v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26321 | complete |
| SF-2026-ARXIV-2605-26323 | RP-0a3acbd5f177a90b | deep | arXiv:2605.26323v1 | SRC-ARXIV@arXiv:2605.26323v1 | arXiv:2605.26323v1 HTML — §3 DHT multi-ring, pub/sub forest and role assignment; §4 path planning | arXiv:2605.26323v1 HTML — §5 500-EC2-node scaling/churn/communication experiments | arXiv:2605.26323v1 HTML — §6 limitations: EC2 emulation, trust/security and million-node results partly analytical | arXiv:2605.26323v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26323 | complete |
| SF-2026-ARXIV-2605-26327 | RP-c42976628e536ec0 | deep | arXiv:2605.26327v1 | SRC-ARXIV@arXiv:2605.26327v1 | arXiv:2605.26327v1 HTML — §3 full/subspace basis reparameterization and BF16 storage | arXiv:2605.26327v1 HTML — §4 five optimizer/memory/runtime experiments | arXiv:2605.26327v1 HTML — Appendix C Limitations and Future Work; tested model/optimizer regime | arXiv:2605.26327v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26327 | complete |
| SF-2026-ARXIV-2605-26340 | RP-bf05183649173949 | deep | arXiv:2605.26340v1 | SRC-ARXIV@arXiv:2605.26340v1 | arXiv:2605.26340v1 HTML — §3 Chain-of-Evidence; §4 literature/discovery/writing/verification workflow; §5 integrity audit | arXiv:2605.26340v1 HTML — §6–§7 audit, review, discovery and cross-benchmark generalization | arXiv:2605.26340v1 HTML — §9 limitations: coverage, reference depth, automated review, comparison fairness and audit false negatives | arXiv:2605.26340v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26340 | complete |
| SF-2026-ARXIV-2605-26362 | RP-b7eed6557ecb9b51 | deep | arXiv:2605.26362v1 | SRC-ARXIV@arXiv:2605.26362v1 | arXiv:2605.26362v1 HTML — §3 SSR/SAS diagnostics; §4 setup; §6 detector transfer | arXiv:2605.26362v1 HTML — §5 findings; §6 graph/table/multi-hop generalization and detector comparison | arXiv:2605.26362v1 HTML — §8 Limitations; linearization, model and structured-dataset scope | arXiv:2605.26362v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26362 | complete |
| SF-2026-ARXIV-2605-26379 | RP-6109767b003a1514 | deep | arXiv:2605.26379v1 | SRC-ARXIV@arXiv:2605.26379v1 | arXiv:2605.26379v1 HTML — §2 linear-identifiability theorem; §3 Gaussian uniqueness and approximate guarantee | arXiv:2605.26379v1 HTML — §4 2D–1024D latent and pixel-control experiments | arXiv:2605.26379v1 HTML — §5 limitations: stationary additive-noise transition and Gaussian/near-Gaussian regime | arXiv:2605.26379v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26379 | complete |
| SF-2026-ARXIV-2605-26384 | RP-49407a4f238cbe95 | deep | arXiv:2605.26384v1 | SRC-ARXIV@arXiv:2605.26384v1 | arXiv:2605.26384v1 HTML — §2 one-second control example; §3 three-tier controller, safety island and PUE-aware control | arXiv:2605.26384v1 HTML — §4–§5 real-hardware methodology and multi-tier/multi-country measurements | arXiv:2605.26384v1 HTML — §6 Discussion and limitations; tested cluster/grid interface boundary | arXiv:2605.26384v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26384 | complete |
| SF-2026-ARXIV-2605-26403 | RP-447350968b1c1b7a | deep | arXiv:2605.26403v1 | SRC-ARXIV@arXiv:2605.26403v1 | arXiv:2605.26403v1 HTML — §3 policy/simulator shift; §4 simulator calibration plus interactive GRPO | arXiv:2605.26403v1 HTML — §5 dialogue benchmarks, ablations and simulator-alignment results | arXiv:2605.26403v1 HTML — §6 Conclusion; Appendix A assumptions and Appendix B simulator/judge setup | arXiv:2605.26403v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-26403 | complete |
| SF-2026-ARXIV-2605-26418 | RP-c0bff080f1de0ca1 | deep | arXiv:2605.26418v1 | SRC-ARXIV@arXiv:2605.26418v1 | arXiv:2605.26418v1 — § exact heading: 3 Benchmark Design — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26418v1 — § exact heading: 3 Benchmark Design — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26418v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26418v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26418 | complete |
| SF-2026-ARXIV-2605-26433 | RP-c4d6ca4b4593115e | deep | arXiv:2605.26433v1 | SRC-ARXIV@arXiv:2605.26433v1 | arXiv:2605.26433v1 — § exact heading: 3 Methods — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26433v1 — § exact heading: 3.5 Evaluation Metrics — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26433v1 — § exact heading: 5 Discussion: Artifact-Specific Auditing for Sensitive-Information Inference — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26433v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26433 | complete |
| SF-2026-ARXIV-2605-26440 | RP-5139258baaf13ab6 | standard | arXiv:2605.26440v1 | SRC-ARXIV@arXiv:2605.26440v1 | https://arxiv.org/html/2605.26440v1#S2 | https://arxiv.org/html/2605.26440v1#S4 | https://arxiv.org/html/2605.26440v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-26440 | complete |
| SF-2026-ARXIV-2605-26444 | RP-8e2278a7163fd644 | deep | arXiv:2605.26444v1 | SRC-ARXIV@arXiv:2605.26444v1 | https://arxiv.org/html/2605.26444v1#S2 | https://arxiv.org/html/2605.26444v1#S4 | https://arxiv.org/html/2605.26444v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-26444 | complete |
| SF-2026-ARXIV-2605-26457 | RP-5c74b7039610a1b0 | deep | arXiv:2605.26457v1 | SRC-ARXIV@arXiv:2605.26457v1 | arXiv:2605.26457v1 — § exact heading: 1 Introduction — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26457v1 — § exact heading: 2 Specification Autoformalization and Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26457v1 — § exact heading: 3.1 From Codeforces Problems to Benchmark Tasks — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26457v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26457 | complete |
| SF-2026-ARXIV-2605-26461 | RP-2304f65fe50a325a | deep | arXiv:2605.26461v1 | SRC-ARXIV@arXiv:2605.26461v1 | arXiv:2605.26461v1 — § exact heading: 2.1. GPU Execution Model — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26461v1 — § exact heading: 7. Implementation and Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26461v1 — § exact heading: 8. Discussion: Full Fault Isolation — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26461v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26461 | complete |
| SF-2026-ARXIV-2605-26485 | RP-c48042ae36b5e4b4 | deep | arXiv:2605.26485v1 | SRC-ARXIV@arXiv:2605.26485v1 | arXiv:2605.26485v1 — §3 benchmark, slot construction and interaction-aware scoring | arXiv:2605.26485v1 — §4 native-online inference, 1Q1A/1QnA and interruption analyses | arXiv:2605.26485v1 — no dedicated limitations; Appendix A licenses/scoring and §4.5 bound claims to 250 videos/1,430 slots | arXiv:2605.26485v1 — project repository announced; immutable event-time commit Not Disclosed | claim:SF-2026-ARXIV-2605-26485 | complete |
| SF-2026-ARXIV-2605-26497 | RP-ace313ac62792b00 | deep | arXiv:2605.26497v1 | SRC-ARXIV@arXiv:2605.26497v1 | arXiv:2605.26497v1 — §3.1–3.4 IRG, clean-context authorization graph and alignment checker | arXiv:2605.26497v1 — §4.1 setup; §4.2 AgentDojo/AgentDyn results | arXiv:2605.26497v1 — §5 discussion; Appendix B.2 excludes user-authorized observation consumption | arXiv:2605.26497v1 — official v1 body and system prompts; immutable implementation commit Not Disclosed | claim:SF-2026-ARXIV-2605-26497 | complete |
| SF-2026-ARXIV-2605-26508 | RP-15f3c05784750044 | deep | arXiv:2605.26508v1 | SRC-ARXIV@arXiv:2605.26508v1 | arXiv:2605.26508v1 — §3 Model; §4 Counterfactual Action Toll; §7 Runtime Risk Gating (official exact-v1 HTML read) | arXiv:2605.26508v1 — §7 conservative runtime budget guarantee; §8 empirical status (official exact-v1 HTML read) | arXiv:2605.26508v1 — §9 Residual Obligations and Scope (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26508v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26508 | complete |
| SF-2026-ARXIV-2605-26521 | RP-6d24264425d14089 | deep | arXiv:2605.26521v1 | SRC-ARXIV@arXiv:2605.26521v1 | arXiv:2605.26521v1 — §III-A formal coverage model; §III-B–D generation, realization and observation | arXiv:2605.26521v1 — §IV benchmarks, runtime witnesses, fault injection and synthesis | arXiv:2605.26521v1 — §IV-I Threats to Validity; §VI says structural coverage complements, not replaces, semantic/end-to-end evaluation | arXiv:2605.26521v1 — official v1 body; workflow benchmark artifact identity Not Disclosed | claim:SF-2026-ARXIV-2605-26521 | complete |
| SF-2026-ARXIV-2605-26542 | RP-b262b7da04c0e4a3 | deep | arXiv:2605.26542v1 | SRC-ARXIV@arXiv:2605.26542v1 | arXiv:2605.26542v1 — §3.1–3.6 threat model, budget algebra, runtime enforcement and non-amplification | arXiv:2605.26542v1 — §4.1–4.4 five-model evaluation, baselines, ablations and manifest-cost analysis | arXiv:2605.26542v1 — §4.5 Threats to Validity; claims limited to explicit proxy-visible flows with trusted manifests | arXiv:2605.26542v1 — §5 artifact availability; immutable release commit Not Disclosed | claim:SF-2026-ARXIV-2605-26542 | complete |
| SF-2026-ARXIV-2605-26558 | RP-9275854e9d4a6c2d | standard | arXiv:2605.26558v1 | SRC-ARXIV@arXiv:2605.26558v1 | arXiv:2605.26558v1 — §IV Cassandra algorithm; §V hardware architecture and data management | arXiv:2605.26558v1 — §VI accuracy/performance/area-power evaluation; §VII comparisons | arXiv:2605.26558v1 — no dedicated limitations; §VII binds evidence to low-batch disclosed edge models/hardware and conversion module assumptions | arXiv:2605.26558v1 — official v1 body; implementation RTL/commit Not Disclosed | claim:SF-2026-ARXIV-2605-26558 | complete |
| SF-2026-ARXIV-2605-26563 | RP-ec6b9cabd6baa06f | deep | arXiv:2605.26563v1 | SRC-ARXIV@arXiv:2605.26563v1 | arXiv:2605.26563v1 — § exact heading: 2.2. Failure Localization Methods — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26563v1 — § exact heading: 3. The RootSE Benchmark — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26563v1 — § exact heading: 2.2. Failure Localization Methods — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26563v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26563 | complete |
| SF-2026-ARXIV-2605-26574 | RP-b60322d0d93e514b | deep | arXiv:2605.26574v1 | SRC-ARXIV@arXiv:2605.26574v1 | arXiv:2605.26574v1 — § exact heading: 3 Method — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26574v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26574v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26574v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26574 | complete |
| SF-2026-ARXIV-2605-26606 | RP-679b866e9750e2ee | deep | arXiv:2605.26606v1 | SRC-ARXIV@arXiv:2605.26606v1 | arXiv:2605.26606v1 — §3.2 reward-variance signal; §3.3 Pilot-Commit; §3.4 optimizations | arXiv:2605.26606v1 — §4 setup; §5 results; §6 analysis | arXiv:2605.26606v1 — §7 Limitations — group RL, online estimates, staleness and disclosed model/workload boundary | arXiv:2605.26606v1 — github.com/databricks/pilot-commit; event-time commit Not Disclosed | claim:SF-2026-ARXIV-2605-26606 | complete |
| SF-2026-ARXIV-2605-26667 | RP-83bfcb34fe9c92f1 | deep | arXiv:2605.26667v1 | SRC-ARXIV@arXiv:2605.26667v1 | arXiv:2605.26667v1 — §3.1 three memory operations; §3.2 failure taxonomy; §4 benchmark tasks | arXiv:2605.26667v1 — §5 setup; §6 four-memory-system experiments; Appendix C results | arXiv:2605.26667v1 — no named limitations; benchmark construction, chosen systems/tasks and judge prompts in Appendices B–D bound generalization — § exact-v1 limitations/counterevidence heading/fragment | arXiv:2605.26667v1 — github.com/ishirgarg/MemFail; immutable commit Not Disclosed | claim:SF-2026-ARXIV-2605-26667 | complete |
| SF-2026-ARXIV-2605-26684 | RP-c3ced001f2fb3e1e | deep | arXiv:2605.26684v1 | SRC-ARXIV@arXiv:2605.26684v1 | arXiv:2605.26684v1 — § exact heading: 4 Proposed Method — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26684v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26684v1 — § exact heading: 4.1 Limitations of Trajectory-Level Attribution — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26684v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26684 | complete |
| SF-2026-ARXIV-2605-26691 | RP-a15dd995fcd3bafb | deep | arXiv:2605.26691v1 | SRC-ARXIV@arXiv:2605.26691v1 | arXiv:2605.26691v1 — § exact heading: 2.2 Medical Vision-Language Models and Diagnostic Tools — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26691v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26691v1 — § exact heading: 5 Conclusion and Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26691v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26691 | complete |
| SF-2026-ARXIV-2605-26720 | RP-cbca715a620e0f41 | deep | arXiv:2605.26720v1 | SRC-ARXIV@arXiv:2605.26720v1 | arXiv:2605.26720v1 — § exact heading: 3 CUDAnalyst Design and Evaluation — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26720v1 — § exact heading: 3 CUDAnalyst Design and Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26720v1 — § exact heading: 6 Conclusion and Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26720v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26720 | complete |
| SF-2026-ARXIV-2605-26730 | RP-951103d62bbfa7c9 | deep | arXiv:2605.26730v1 | SRC-ARXIV@arXiv:2605.26730v1 | arXiv:2605.26730v1 — § exact heading: 3 The PRISM Framework — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.26730v1 — § exact heading: 4 Experiment and analysis — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.26730v1 — § exact heading: C.3 Prompt Templates by Dimension — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.26730v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-26730 | complete |
| SF-2026-ARXIV-2605-26731 | RP-d167582caee26481 | standard | arXiv:2605.26731v1 | SRC-ARXIV@arXiv:2605.26731v1 | arXiv:2605.26731v1 — §3 HEAT-24 workspace, harness conditions, models and failure taxonomy | arXiv:2605.26731v1 — §4 432-run results by harness/model/task and latency | arXiv:2605.26731v1 — §5 Limitations and threats — one model per tier, synthetic 24-task benchmark and model-specific observations | arXiv:2605.26731v1 — official v1 body; immutable harness artifact Not Disclosed | claim:SF-2026-ARXIV-2605-26731 | complete |
| SF-2026-ARXIV-2605-26754 | RP-e3241f0a809231ef | deep | arXiv:2605.26754v1 | SRC-ARXIV@arXiv:2605.26754v1 | arXiv:2605.26754v1 — §3 CORDON-MAS and dirty-read, claim-only and certified-synthesis invariants | arXiv:2605.26754v1 — §4 setup; §5 results, ablations and adaptive attacks | arXiv:2605.26754v1 — §6 discussion; Appendix H limitations and Appendix B threat model | arXiv:2605.26754v1 — Appendix W artifact; immutable release commit Not Disclosed | claim:SF-2026-ARXIV-2605-26754 | complete |
| SF-2026-ARXIV-2605-26778 | RP-d8a61259882b821f | deep | arXiv:2605.26778v1 | SRC-ARXIV@arXiv:2605.26778v1 | arXiv:2605.26778v1 — §3 Computational Reality Monitoring with paired context/no-context representations | arXiv:2605.26778v1 — §4 setup; §5 attribution experiments and interventions | arXiv:2605.26778v1 — §6 discussion/limitations; evidence is representation-level attribution on disclosed models/tasks, not universal causal identification | arXiv:2605.26778v1 — official v1 body; immutable artifact Not Disclosed | claim:SF-2026-ARXIV-2605-26778 | complete |
| SF-2026-ARXIV-2605-27091 | RP-617c377a06cb353e | deep | arXiv:2605.27091v1 | SRC-ARXIV@arXiv:2605.27091v1 | arXiv:2605.27091v1 HTML — §3.2 sampling-failure bound; §3.3 conformal selection; §3.4 combined guarantee | arXiv:2605.27091v1 HTML — §4 finite-sampling, conditional-selection and overall-miscoverage experiments | arXiv:2605.27091v1 HTML — Appendix A conditional exchangeability and population-bound assumptions | arXiv:2605.27091v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-27091 | complete |
| SF-2026-ARXIV-2605-27220 | RP-7233412eb6873477 | deep | arXiv:2605.27220v1 | SRC-ARXIV@arXiv:2605.27220v1 | arXiv:2605.27220v1 — §3 production trace, pre-retrieval router and post-retrieval cascade decomposition | arXiv:2605.27220v1 — §4 workflows/data; §5 20,000 query-workflow results and cost/latency analysis | arXiv:2605.27220v1 — §6 limitations — single Danish encyclopedia, production policy and query-distribution boundary | arXiv:2605.27220v1 — official v1 body; production trace/code release identity Not Disclosed | claim:SF-2026-ARXIV-2605-27220 | complete |
| SF-2026-ARXIV-2605-27292 | RP-3bb9f24764c13c8b | deep | arXiv:2605.27292v1 | SRC-ARXIV@arXiv:2605.27292v1 | arXiv:2605.27292v1 — §3 influence-based canary selection; §4 refinement and diversity/IBIS | arXiv:2605.27292v1 — §5 experiments; Appendix D setup and ablations | arXiv:2605.27292v1 — Reasoned exception — manuscript has no dedicated Limitations section; Appendix A theoretical assumptions and Appendix D disclosed one-run image/classification setup bound claims — § exact-v1 limitations/counterevidence heading/fragment | arXiv:2605.27292v1 — official v1 body; immutable implementation commit Not Disclosed | claim:SF-2026-ARXIV-2605-27292 | complete |
| SF-2026-ARXIV-2605-27328 | RP-2f4eafc2c1affc14 | deep | arXiv:2605.27328v1 | SRC-ARXIV@arXiv:2605.27328v1 | arXiv:2605.27328v1 — § exact heading: 2.2 Code-Centric Reasoning, Acting, and Environment Modeling — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27328v1 — § exact heading: 1.1 Terminology and Conceptual Levels — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27328v1 — § exact heading: 12 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27328v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27328 | complete |
| SF-2026-ARXIV-2605-27333 | RP-c9a4c013357f5251 | deep | arXiv:2605.27333v1 | SRC-ARXIV@arXiv:2605.27333v1 | arXiv:2605.27333v1 — § exact heading: 3 Method: FinHarness — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27333v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27333v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27333v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27333 | complete |
| SF-2026-ARXIV-2605-27361 | RP-a41392e68c1870b4 | deep | arXiv:2605.27361v1 | SRC-ARXIV@arXiv:2605.27361v1 | arXiv:2605.27361v1 — § exact heading: 4 BRANE: Methodology — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27361v1 — § exact heading: 5 Evaluations and Ablations — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27361v1 — § exact heading: 6 Limitations and Broader Impact — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27361v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27361 | complete |
| SF-2026-ARXIV-2605-27366 | RP-ee9d63852b08ff96 | deep | arXiv:2605.27366v1 | SRC-ARXIV@arXiv:2605.27366v1 | arXiv:2605.27366v1 — § exact heading: 2.2 Automatic Skill Systems — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27366v1 — § exact heading: 2.3 Benchmarks and Positioning — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27366v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27366v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27366 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-26118:start -->
#### Xe-Forge: Multi-Stage LLM-Powered Kernel Optimization for Intel GPU

<!-- claim:SF-2026-ARXIV-2605-26118:start -->
- **Problem:** Porting deep learning algorithms to new hardware accelerators requires developers to repeatedly apply the same low-level optimizations -- quantization, memory access coalescing, tile size tuning, and architecture-specific workarounds -- to every Triton kernel in their code-base.
- **Old path / changed constraint:** This manual, repetitive effort is a major bottleneck: each kernel demands the same cycle of trial-and-error profiling against hardware constraints that vary across devices, yet the underlying optimization patterns remain largely consistent.
- **Mechanism / ownership:** We present Xe-Forge, a multi-stage LLM-powered pipeline that automates this process for Intel GPU.
- **Evaluation contract:** We evaluate Xe-Forge on 97 Level-2 KernelBench kernels and Flash Attention on the Intel Arc Pro B70, achieving a 1.17x geometric mean speedup over PyTorch eager with 67% of kernels improving, nine kernels exceeding 5x (up to 82x), and 2--13.3x speedups on Flash Attention across all tested configurations without regression -- demonstrating that structured domain knowledge with hardware-in-the-loop verification can systematically eliminate the repetitive porting effort that currently gates algorithm deployment on new accelerators.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Given a functionally correct Triton kernel, the system applies up to nine optimization stages — from algorithmic restructuring and operator fusion through block pointer modernization, GPU-specific tuning, and open-ended discovery — each driven by a Chain-of-Verification-and-Refinement (CoVeR) agent that generates candidates, validates them on real hardware, and iterates on failures.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.26118v1](https://arxiv.org/abs/2605.26118v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.26118v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-26118:end -->
<!-- review:SF-2026-ARXIV-2605-26118:end -->

<!-- review:SF-2026-ARXIV-2605-26120:start -->
#### Semantic-aware Token Selection and Resource Optimization for Communication-efficient Split Federated Fine-tuning in Edge Intelligence

<!-- claim:SF-2026-ARXIV-2605-26120:start -->
- **Problem:** Deploying large Transformer-based vision models on resource-limited mobile devices at network edge is severely constrained by hardware limitations and dynamic wireless environments.
- **Old path / changed constraint:** Deploying large Transformer-based vision models on resource-limited mobile devices at network edge is severely constrained by hardware limitations and dynamic wireless environments.
- **Mechanism / ownership:** To address this bottleneck, we propose ST-SFLora, a semantic token-based split federated LoRA fine-tuning framework.
- **Evaluation contract:** Experiments on multiple benchmarks demonstrate that ST-SFLora achieves the lowest client-side resource consumption among baselines while delivering a favorable trade-off between communication efficiency and model performance.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Describe the issue below: Deploying large Transformer-based vision models on resource-limited mobile devices at network edge is severely constrained by hardware limitations and dynamic wireless environments.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.26120v1](https://arxiv.org/abs/2605.26120v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.26120v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-26120:end -->
<!-- review:SF-2026-ARXIV-2605-26120:end -->

<!-- review:SF-2026-ARXIV-2605-26128:start -->
#### The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models

**问题与机制。** We show that this assumption is unsafe for small models. 系统 owner=`AGENT-TOOL-CALLING`。

**Exact-v1。** Method=`§2.2 Structured Decoding as a Serving-System Interface`；Evaluation=`§5 Experimental Protocol; §6 Empirical Results; §7.4 What the Result Establishes`；Limitations/Counterevidence=`§7 Discussion; §10 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-26128:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-26128:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-26128:end -->

<!-- review:SF-2026-ARXIV-2605-26132:start -->
#### Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline

**问题与机制。** We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§4.5 Training vs. Test-Time Compute; §C.1.2 Training`；Evaluation=`§4 Experiments; §Appendix C Experimental Details; §C.1.3 Evaluation`；Limitations/Counterevidence=`§5 Discussion`。

<!-- claim:SF-2026-ARXIV-2605-26132:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-26132:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-26132:end -->

<!-- review:SF-2026-ARXIV-2605-26147:start -->
#### Neural Bayesian Sequential Routing

**问题与机制。** We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG). owner=`INFER-SCHEDULING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3–§5 DAG evidence accumulation and sequential routing`；Evaluation=`§6–§8 controlled experiments and ablations`；Limitations/Counterevidence=`§9 Discussion; conjugate-belief assumptions and tested-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-26147:start -->Neural Bayesian Sequential Routing only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-26147:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-26147:end -->

<!-- review:SF-2026-ARXIV-2605-26154:start -->
#### MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning

**问题与机制。** Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 MemMorph memory-poisoning and tool-hijack attack`；Evaluation=`§5 agent evaluation`；Limitations/Counterevidence=`§6 limitations and memory/tool boundary`。

<!-- claim:SF-2026-ARXIV-2605-26154:start -->MemMorph: Tool Hijacking in LLM Agents via Memory Poisoning 的 exact-v1 只支持该文披露机制：Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses. 其未证明边界由 `§6 limitations and memory/tool boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26154:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26154:end -->

<!-- review:SF-2026-ARXIV-2605-26156:start -->
#### Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges

**问题与机制。** 把 judge 的 style sensitivity 暴露为可自适应搜索的黑盒攻击面，并同时测 utility、stealth 与 query budget。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Threat model; §4 Contextual-bandit black-box style attack; §5 Analysis`；Evaluation=`§6 Evaluation on chatbot leaderboards and automated peer review, including stealth and mitigation`；Limitations/Counterevidence=`§7 Conclusion and Appendix experiments: tested-judge/task/style scope; semantic-preservation proxy and adaptive-query-budget boundary`。

<!-- claim:SF-2026-ARXIV-2605-26156:start -->攻击只覆盖给定 judge、任务和 style transformations，语义保持依赖 LLM/embedding proxy。Ch66 已把 position/style/self-preference 与受控不变性 intervention 写入 construct-validity contract，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-26156:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26156:end -->

<!-- review:SF-2026-ARXIV-2605-26158:start -->
#### Furina: Fragmented Uncertainty-Driven Refusal Instability Attack

**问题与机制。** 把 refusal 从单一二元阈值改写为可重复采样的 instability band，并把分散于多个 benign-looking probes/视觉片段中的意图在最终 synthesis 时重新组合为跨 turn 攻击。 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§3 Safety Instability external/internal diagnostics; §4 fragmented scene-anchored probing and synthesis`；Evaluation=`§5 HarmBench/MM-SafetyBench experiments, ablations and classical-defense checks; Appendix B.7 human judge validation`；Limitations/Counterevidence=`§ Impact Statement: instability band remains diagnostic, thresholds are not calibrated per input, and cross-fragment evidence requires future context-aware defense`。

<!-- claim:SF-2026-ARXIV-2605-26158:start -->论文没有提供对单个输入校准 tau-/tau+ 的方法；ASR 绑定选定采样参数、HarmBench/MM-SafetyBench、judge 和模型版本。Ch72 已要求 run-centric multi-turn evidence 聚合、cumulative intent 与 sensor/authority 分离，故不重复写入。<!-- claim:SF-2026-ARXIV-2605-26158:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26158:end -->

<!-- review:SF-2026-ARXIV-2605-26159:start -->
#### Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices

**问题与机制。** We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 Device Context Protocol safety architecture`；Evaluation=`§5 constrained-device evaluation`；Limitations/Counterevidence=`§6 limitations and device-capability boundary`。

<!-- claim:SF-2026-ARXIV-2605-26159:start -->Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices 的 exact-v1 只支持该文披露机制：We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device. 其未证明边界由 `§6 limitations and device-capability boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26159:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26159:end -->

<!-- review:SF-2026-ARXIV-2605-26161:start -->
#### TSFMAudit: Data Contamination Auditing in Forecasting Time Series Foundation Models

**问题与机制。** 用 fine-tuning loss drop、backbone displacement 与 reference-model debiasing构成 dataset-level contamination-risk sensor，处理连续时序的缩放/重采样重复。 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 Problem formulation; §4 TSFMAudit; §4.1 adaptation traces; §4.2 reference-model debiasing; §4.3 calibration and decision`；Evaluation=`§5 Experiments on six TSFMs/187 datasets; §5.5 practical deployment; Appendix B audit protocol`；Limitations/Counterevidence=`Appendix A contamination labels and transformed-duplicate semantics; proxy labels depend on incomplete official corpus documentation`。

<!-- claim:SF-2026-ARXIV-2605-26161:start -->标签来自不完整训练来源文档，参考模型与 probe protocol 会影响 verdict；结论绑定 TSFM/time-series。Ch27/Ch66 已拥有 contamination identity、transformed duplicate 与受限 sensor/release boundary，故不扩写领域特例。<!-- claim:SF-2026-ARXIV-2605-26161:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26161:end -->

<!-- review:SF-2026-ARXIV-2605-26162:start -->
#### On the Push-Based Asynchronous Federated Learning: A Bias-Correction Aggregation Approach

**问题与机制。** 在无中心异步联邦训练中用 push-sum numerator/denominator、in-flight mass 与 buffered message state 修正有向图聚合偏差，并以 centroid dictionary 压缩通信。 系统 owner=`TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1 路径。** Method=`§4 PushCen-ADFL; §4.2 centroid regularization; §4.3 compression; §4.4 push-sum aggregation; §4.5 buffered updates; Appendix C event-driven state accounting`；Evaluation=`§5 Experiments; §5.1.4 delayed-client protocol; §5.2 accuracy/communication/overhead; §5.3 delayed clients`；Limitations/Counterevidence=`§4.6 assumptions and Appendix C: bounded staleness, directed mixing, bounded compression error and simulated event-driven network`。

<!-- claim:SF-2026-ARXIV-2605-26162:start -->实验用 event-driven simulator、vision models 和受控 client delay；收敛依赖 bounded staleness/mixing/compression-error 假设，不能证明真实 WAN、Byzantine client 或大模型训练。<!-- claim:SF-2026-ARXIV-2605-26162:end -->

Books Decision=`Integrate`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26162:end -->

<!-- review:SF-2026-ARXIV-2605-26165:start -->
#### Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets

**问题与机制。** We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1 路径。** Method=`§3 tool-schema compression`；Evaluation=`§4 agentic-RAG evaluation`；Limitations/Counterevidence=`§5 limitations and context/tool-library boundary`。

<!-- claim:SF-2026-ARXIV-2605-26165:start -->Tool-Schema Compression Enables Agentic RAG Under Constrained Context Budgets 的 exact-v1 只支持该文披露机制：We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions. 其未证明边界由 `§5 limitations and context/tool-library boundary` 限定；不能把该受限结果外推为跨模型、跨硬件、跨 workload 或生产 SLO 的通用优势。<!-- claim:SF-2026-ARXIV-2605-26165:end -->

Books Decision=`No Change — Existing Coverage`；已对 current owner 与相邻章节做非作者语义比较。
<!-- review:SF-2026-ARXIV-2605-26165:end -->

<!-- review:SF-2026-ARXIV-2605-26172:start -->
#### ARBITER: Reasoning Trajectory Basins and Majority Vote Failures in Test-Time Sampling

**问题与机制。** We show that these trajectories are not independent: for a given question, they concentrate into a small number of clusters, or reasoning basins, each defined by a normalized final answer and the solutions that reach it. 该证据的系统 owner 定位为 `MODEL-SAMPLING`。

**Exact-v1 路径。** Method=`§3 reasoning-basin construction; §4 conservative additive evidence and residual encoder`；Evaluation=`§5 three model families/three math benchmarks and wrong-majority analyses`；Limitations/Counterevidence=`§6 limitations: same-pool evidence, math tasks and bounded oracle headroom`。

<!-- claim:SF-2026-ARXIV-2605-26172:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26172:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26172:end -->

<!-- review:SF-2026-ARXIV-2605-26177:start -->
#### RepoMirage: Probing Repository Context Reasoning in Code Agents with Perturbations

**问题与机制。** Code agents are currently having skillful performance on repository-level software engineering benchmarks, but it remains unclear whether success on end-to-end tasks such as issue resolution truly reflects repository context reasoning, the ability to identify the task-relevant information across multiple files and reason over the relations among them. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 repository perturbations; §4 derived tasks; §5 diagnosis and RepoAnchor`；Evaluation=`§2 setup; §3–§5 performance, structural-hint validation and behavior analysis`；Limitations/Counterevidence=`Appendix C.1 Limitations; repository/task/model scope`。

<!-- claim:SF-2026-ARXIV-2605-26177:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26177:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26177:end -->

<!-- review:SF-2026-ARXIV-2605-26184:start -->
#### GAC: Noise-Aware Adaptive Mixing for Hybrid SFT-RL Post-Training

**问题与机制。** We propose GAC, a noise-aware controller that derives an adaptive mixing weight from online estimates of gradient variance and disagreement between the two training signals. 该证据的系统 owner 定位为 `TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3 noise model, proxies, online estimation and adaptive controller`；Evaluation=`§4 reasoning/code/scale/training-health results and signal ablations`；Limitations/Counterevidence=`Appendix B honest covariance assessment; Appendix C idealized stability assumptions; Appendix E overhead`。

<!-- claim:SF-2026-ARXIV-2605-26184:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26184:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26184:end -->

<!-- review:SF-2026-ARXIV-2605-26200:start -->
#### Workflow Closure Is Not Scientific Closure in Auto-Research Systems

**问题与机制。** These collapses are not inherent limits of autonomy but correctable design choices. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 workflow/scientific closure; §3 three collapses; §6 design implications`；Evaluation=`§4–§5 survey-coded patterns and remediation analysis`；Limitations/Counterevidence=`§8 Limitations; §9 alternative views; survey/position evidence rather than causal experiment`。

<!-- claim:SF-2026-ARXIV-2605-26200:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26200:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26200:end -->

<!-- review:SF-2026-ARXIV-2605-26242:start -->
#### Can LLMs Introspect? A Reality Check

**问题与机制。** We identify two conditions that a paradigm needs to meet in order to establish introspection. 该证据的系统 owner 定位为 `WORLDVIEW-LLM-INTELLIGENCE`。

**Exact-v1 路径。** Method=`§2 privileged-access and second-order-computation criteria; §3 two paradigm re-analyses`；Evaluation=`§4 input-only controls and internal-vs-input intervention discrimination`；Limitations/Counterevidence=`§5 conclusion: negative evidence for tested introspection paradigms, not proof of impossibility`。

<!-- claim:SF-2026-ARXIV-2605-26242:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26242:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26242:end -->

<!-- review:SF-2026-ARXIV-2605-26248:start -->
#### Unified Neural Scaling Laws

**问题与机制。** We present a functional form (that we refer to as a Unified Neural Scaling Law (UNSL)) that accurately models and extrapolates the scaling behaviors of deep neural networks as multiple dimensions all vary simultaneously (i.e. 该证据的系统 owner 定位为 `WORLDVIEW-SCALING-LAW`。

**Exact-v1 路径。** Method=`§2 unified multi-axis functional form; §3 estimation and extrapolation`；Evaluation=`§4 vision/language/math/RL fits and held-out extrapolation`；Limitations/Counterevidence=`§5 predictability limits; §6 discussion across tested architectures/tasks`。

<!-- claim:SF-2026-ARXIV-2605-26248:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26248:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26248:end -->

<!-- review:SF-2026-ARXIV-2605-26252:start -->
#### Is Agent Memory a Database? Rethinking Data Foundations for Long-Term AI Agent Memory

**问题与机制。** Long-running AI agents need persistent memory. 该证据的系统 owner 定位为 `AGENT-MEMORY`。

**Exact-v1 路径。** Method=`§2 record-abstraction failures; §3 GEM operators/correctness; §4 MemState realization`；Evaluation=`§4 prototype feasibility and §5 research agenda`；Limitations/Counterevidence=`§6 Conclusion; prototype/vision evidence without comparative production evaluation`。

<!-- claim:SF-2026-ARXIV-2605-26252:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26252:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26252:end -->

<!-- review:SF-2026-ARXIV-2605-26266:start -->
#### Quantized Keys Steal Attention: Bias Correction for KV-Cache Compression in Video Diffusion

**问题与机制。** We show that a key driver of this degradation is a systematic bias in attention weights: due to the convexity of the exponential in softmax attention, quantization noise inflates the contribution of cached keys, a phenomenon we call the Jensen bias. 该证据的系统 owner 定位为 `INFER-KV-CACHE`。

**Exact-v1 路径。** Method=`§4.1 Jensen attention bias; §4.2 correction; §4.3 cost`；Evaluation=`§5 video-diffusion and partial-prefill experiments plus ablations`；Limitations/Counterevidence=`§6 Limitations & future work; model/quantizer and partial-prefill transfer boundary`。

<!-- claim:SF-2026-ARXIV-2605-26266:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26266:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26266:end -->

<!-- review:SF-2026-ARXIV-2605-26269:start -->
#### AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents

**问题与机制。** We introduce AgentSecBench as an empirical instantiation of a formal security framework for this problem. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 properties/threat model; §3 intent-execution formalization; §4 security games; §5 defenses`；Evaluation=`§6–§7 protocol, adversarial advantage, utility and cost`；Limitations/Counterevidence=`§8 residual risk; later limitations section and finite task/model envelope`。

<!-- claim:SF-2026-ARXIV-2605-26269:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26269:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26269:end -->

<!-- review:SF-2026-ARXIV-2605-26282:start -->
#### Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization

**问题与机制。** Beyond these issues, we identify a more critical yet underexplored bottleneck: a structural misalignment between search and value learning in existing world model approaches. 该证据的系统 owner 定位为 `MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§3 latent-world searched trajectories and diffusion policy optimization`；Evaluation=`§4 offline, online and offline-to-online evaluation plus capacity scaling`；Limitations/Counterevidence=`§5 limitations: learned-world bias, benchmark/control horizon and compute envelope`。

<!-- claim:SF-2026-ARXIV-2605-26282:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26282:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26282:end -->

<!-- review:SF-2026-ARXIV-2605-26289:start -->
#### Stateful Inference for Low-Latency Multi-Agent Tool Calling

**问题与机制。** We present a stateful inference architecture that converts the $O(n_t)$ per-turn cost of conventional serving into an $O(Δ_t)$ delta-only cost: a persistent KV cache lives across turns and advances by ingesting only the new tokens, while a radix prefix cache extends this across interleaved multi-agent traffic and a prompt-lookup speculative decoder accelerates structured output. 该证据改变的是跨轮 KV 生命周期与增量执行边界，系统 owner 定位为 `INFER-KV-CACHE`；Tool Calling 只是 workload 场景，prompt-lookup speculation 是下游可选加速器。

**Exact-v1 路径。** Method=`§2 workload/cost; §3 sequence pool, caches, scheduler, speculative decode and streaming validator`；Evaluation=`§4–§5 multi-turn/burst/cache latency evaluation`；Limitations/Counterevidence=`§6.2 Limitations; single implementation/hardware and prompt-determinism assumptions`。

<!-- claim:SF-2026-ARXIV-2605-26289:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26289:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26289:end -->

<!-- review:SF-2026-ARXIV-2605-26297:start -->
#### Agentic AI Workload Characteristics

**问题与机制。** Our study shows that agentic workloads are not simply long-prompt workloads: with effective context caching, most input tokens are reused across turns, making execution decode-dominated while increasing dependence on long-lived KV-cache state. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 trace infrastructure; §4 agent execution; §5 runtime; §6 tool-call characterization`；Evaluation=`§7 Evaluation — five agent benchmarks across reasoning/non-reasoning Gemma/Qwen configurations`；Limitations/Counterevidence=`§8 Conclusion; benchmark/model/serving-stack characterization boundary`。

<!-- claim:SF-2026-ARXIV-2605-26297:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26297:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26297:end -->

<!-- review:SF-2026-ARXIV-2605-26298:start -->
#### Sandlock: Confining AI Agent Code with Unprivileged Linux Primitives

**问题与机制。** AI agents increasingly run untrusted code on developer machines: shell commands generated by language models, third-party scripts retrieved at runtime, and tool plugins of unknown provenance. 该证据的系统 owner 定位为 `PLATFORM-SECURITY`。

**Exact-v1 路径。** Method=`§2 threat model; §3 policy; §4 Landlock/seccomp/network design; §5 implementation`；Evaluation=`§6 effectiveness, startup, throughput, COW, network and compatibility`；Limitations/Counterevidence=`§8 threat-model/integration/rollback limitations; local Linux host only`。

<!-- claim:SF-2026-ARXIV-2605-26298:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26298:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26298:end -->

<!-- review:SF-2026-ARXIV-2605-26302:start -->
#### Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed Systems

**问题与机制。** We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan engineering: measuring not only whether deployed agents degrade, but what form the degradation takes and where repair should target. 该证据的系统 owner 定位为 `AGENT-PLATFORM`。

**Exact-v1 路径。** Method=`§3 aging taxonomy; §4 benchmark; §5 component diagnosis and counterfactual intervention`；Evaluation=`§6 setup/results and Appendix D typed-state/controller probes`；Limitations/Counterevidence=`§7 Conclusion; synthetic scenarios, closed agents and aging-preview boundary`。

<!-- claim:SF-2026-ARXIV-2605-26302:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26302:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26302:end -->

<!-- review:SF-2026-ARXIV-2605-26321:start -->
#### Anchor: Mitigating Artifact Drift in Agent Benchmark Generation

**问题与机制。** We introduce Anchor, a task-generation pipeline that formalizes domain experts' specifications of business workflows into constraint optimization programs. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§2 Anchor; §3 ERP-Bench; Appendix D deterministic generator and E verifier`；Evaluation=`§4 evaluation; appendices G–I reliability, failure and validity checks`；Limitations/Counterevidence=`§5 Limitations; single ERP domain and generated-artifact scope`。

<!-- claim:SF-2026-ARXIV-2605-26321:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26321:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26321:end -->

<!-- review:SF-2026-ARXIV-2605-26323:start -->
#### Totoro$^+$: An Adaptive and Scalable Edge Federated Learning System

**问题与机制。** We propose Totoro$^+$, a novel scalable FL system that enables massive FL applications to run simultaneously on edge networks. 该证据的系统 owner 定位为 `TRAIN-DISTRIBUTED-TRAINING`。

**Exact-v1 路径。** Method=`§3 DHT multi-ring, pub/sub forest and role assignment; §4 path planning`；Evaluation=`§5 500-EC2-node scaling/churn/communication experiments`；Limitations/Counterevidence=`§6 limitations: EC2 emulation, trust/security and million-node results partly analytical`。

<!-- claim:SF-2026-ARXIV-2605-26323:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26323:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26323:end -->

<!-- review:SF-2026-ARXIV-2605-26327:start -->
#### Reparametrizing Shampoo and SOAP for Subspace Basis Updates and BFloat16 Storage

**问题与机制。** We propose a reparametrization of the preconditioner that supports BFP16 storage and forms a complete basis by combining updated basis vectors with unchanged ones. 该证据的系统 owner 定位为 `TRAIN-PRETRAINING`。

**Exact-v1 路径。** Method=`§3 full/subspace basis reparameterization and BF16 storage`；Evaluation=`§4 five optimizer/memory/runtime experiments`；Limitations/Counterevidence=`Appendix C Limitations and Future Work; tested model/optimizer regime`。

<!-- claim:SF-2026-ARXIV-2605-26327:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26327:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26327:end -->

<!-- review:SF-2026-ARXIV-2605-26340:start -->
#### ScientistOne: Towards Human-Level Autonomous Research via Chain-of-Evidence

**问题与机制。** Autonomous research agents produce competitive solutions and professional-looking manuscripts, yet their outputs contain verifiability failures undetectable by surface-level evaluation: fabricated citations, unreproducible scores, and method descriptions that diverge from the implementation. 该证据的系统 owner 定位为 `AGENT-WORKFLOW`。

**Exact-v1 路径。** Method=`§3 Chain-of-Evidence; §4 literature/discovery/writing/verification workflow; §5 integrity audit`；Evaluation=`§6–§7 audit, review, discovery and cross-benchmark generalization`；Limitations/Counterevidence=`§9 limitations: coverage, reference depth, automated review, comparison fairness and audit false negatives`。

<!-- claim:SF-2026-ARXIV-2605-26340:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26340:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26340:end -->

<!-- review:SF-2026-ARXIV-2605-26362:start -->
#### Why LLMs Hallucinate on Structured Knowledge: A Mechanistic Analysis of Reasoning over Linearized Representations

**问题与机制。** Finally, we show that these mechanistic patterns generalize beyond single-hop graphs to multi-hop and tabular settings, enabling effective hallucination detection across structured knowledge formats. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3 SSR/SAS diagnostics; §4 setup; §6 detector transfer`；Evaluation=`§5 findings; §6 graph/table/multi-hop generalization and detector comparison`；Limitations/Counterevidence=`§8 Limitations; linearization, model and structured-dataset scope`。

<!-- claim:SF-2026-ARXIV-2605-26362:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26362:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26362:end -->

<!-- review:SF-2026-ARXIV-2605-26379:start -->
#### When Does LeJEPA Learn a World Model?

**问题与机制。** We further prove an approximate identifiability result where the guarantee degrades gracefully, and show that linear, orthogonal identifiability enables optimal latent-space planning. 该证据的系统 owner 定位为 `MULTIMODAL-WORLD-MODELS`。

**Exact-v1 路径。** Method=`§2 linear-identifiability theorem; §3 Gaussian uniqueness and approximate guarantee`；Evaluation=`§4 2D–1024D latent and pixel-control experiments`；Limitations/Counterevidence=`§5 limitations: stationary additive-noise transition and Gaussian/near-Gaussian regime`。

<!-- claim:SF-2026-ARXIV-2605-26379:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26379:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26379:end -->

<!-- review:SF-2026-ARXIV-2605-26384:start -->
#### GridPilot: Real-Time Grid-Responsive Control for AI Supercomputers

**问题与机制。** GridPilot is released as open source and serves as a proof of concept that MW-scale AI/HPC demand can be engineered as controllable, grid-responsive flexibility by design. 该证据的系统 owner 定位为 `PLATFORM-GPU-SCHEDULER`。

**Exact-v1 路径。** Method=`§2 one-second control example; §3 three-tier controller, safety island and PUE-aware control`；Evaluation=`§4–§5 real-hardware methodology and multi-tier/multi-country measurements`；Limitations/Counterevidence=`§6 Discussion and limitations; tested cluster/grid interface boundary`。

<!-- claim:SF-2026-ARXIV-2605-26384:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26384:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26384:end -->

<!-- review:SF-2026-ARXIV-2605-26403:start -->
#### From Static Context to Calibrated Interactive RL: Mitigating Distribution Shift in Multi-turn Dialogue with Aligned Simulator

**问题与机制。** A long-standing goal of the research community is to develop highly interactive LLM-based dialogue agents. 该证据的系统 owner 定位为 `TRAIN-RLHF`。

**Exact-v1 路径。** Method=`§3 policy/simulator shift; §4 simulator calibration plus interactive GRPO`；Evaluation=`§5 dialogue benchmarks, ablations and simulator-alignment results`；Limitations/Counterevidence=`§6 Conclusion; Appendix A assumptions and Appendix B simulator/judge setup`。

<!-- claim:SF-2026-ARXIV-2605-26403:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-26403:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-26403:end -->

<!-- review:SF-2026-ARXIV-2605-26418:start -->
#### When Does Deep RL Beat Calibrated Baselines? A Benchmark Study on Adaptive Resource Control

问题与 changed constraint：resource-control evidence must compare learned policies with calibrated rule baselines under matched workload, reward, seed and SLO contracts。

机制与 ownership：A properly calibrated rule-based autoscaler can beat every one of six mainstream deep reinforcement learning (DRL) algorithms on cost across every workload we test - so when, if ever, does DRL actually help? We study this in RLScale-Bench, a reproducible benchmark and evaluation protocol for DRL on adaptive resource control, where an agent allocates compute to a dynamic workload under cost and service-level constraints. We evaluate PPO, DQN, A2C, SAC, TD3, and DDPG under matched architectures, t owner=`PLATFORM-GPU-SCHEDULER`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26418v1 — § exact heading: 3 Benchmark Design — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26418v1 — § exact heading: 3 Benchmark Design — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26418v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26418:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26418:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26418:end -->

<!-- review:SF-2026-ARXIV-2605-26433:start -->
#### Vectors Are Not Neutral: Sensitive-Information Inference from Exported LLM Representations in Summarization

问题与 changed constraint：derived hidden-state vectors become separately governed privacy artifacts because protection of one exported representation does not protect other pooled representations。

机制与 ownership：We audit two artifacts that a system might retain or expose to downstream components: the final prompt-token hidden state and the mean-pooled prompt representation. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26433v1 — § exact heading: 3 Methods — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26433v1 — § exact heading: 3.5 Evaluation Metrics — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26433v1 — § exact heading: 5 Discussion: Artifact-Specific Auditing for Sensitive-Information Inference — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26433:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26433:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26433:end -->

<!-- review:SF-2026-ARXIV-2605-26440:start -->
#### Conv-to-Bench: Evaluating Language Models Via User-Assistant Dialogues In Code Tasks

<!-- claim:SF-2026-ARXIV-2605-26440:start -->
- **Problem:** The rapid advancement of Large Language Models (LLMs) has outpaced the scalability of traditional evaluation benchmarks, which remain heavily dependent on labor-intensive expert curation.
- **Old path / changed constraint:** We address this bottleneck with Conv-to-Bench, a multi-stage framework that automatically transforms authentic multi-turn user-assistant dialogues into structured, verifiable requirement checklists.
- **Mechanism / ownership:** To leverage this potential, we introduce Conv-to-Bench , a multi-stage framework (Figure 1 ) designed to automatically transform these multi-turn dialogues into structured and verifiable requirements checklists.
- **Evaluation contract:** The rapid advancement of Large Language Models (LLMs) has outpaced the scalability of traditional evaluation benchmarks, which remain heavily dependent on labor-intensive expert curation.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Applied to the programming domain, Conv-to-Bench produces evaluation sets that demonstrate near-perfect alignment with human-authored standards like BigCodeBench, achieving Spearman correlations of up to ρ = 1.000 \rho=1.000 with significantly lower computational overhead.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.26440v1](https://arxiv.org/abs/2605.26440v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.26440v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-26440:end -->
<!-- review:SF-2026-ARXIV-2605-26440:end -->

<!-- review:SF-2026-ARXIV-2605-26444:start -->
#### MicroSpec: Accelerating Speculative Decoding with Lightweight In-Context Vocabularies

<!-- claim:SF-2026-ARXIV-2605-26444:start -->
- **Problem:** The massive vocabulary sizes of large language models, often exceeding 100k tokens, impose a computational bottleneck on the final linear projection layer during speculative decoding.
- **Old path / changed constraint:** The massive vocabulary sizes of large language models, often exceeding 100k tokens, impose a computational bottleneck on the final linear projection layer during speculative decoding.
- **Mechanism / ownership:** We propose NanoSpec, a novel training-free approach that breaks this trade-off by dynamically constructing a minimalist, context-aware active vocabulary for each generation step.
- **Evaluation contract:** Acting as a plug‑and‑play enhancement, MicroSpec reduces draft inference latency by 51.6% on average, achieving an end‑to‑end speedup of 1.12–1.32× relative to the leading speculative decoding approach EAGLE‑2 on various benchmarks, while also surpassing more sophisticated training‑based pruning baselines.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** We introduce MicroSpec , a training-free technique that overcomes this limitation by building a compact, context‑sensitive active vocabulary on the fly for every decoding step.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.26444v1](https://arxiv.org/abs/2605.26444v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.26444v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-26444:end -->
<!-- review:SF-2026-ARXIV-2605-26444:end -->

<!-- review:SF-2026-ARXIV-2605-26457:start -->
#### Verus-SpecGym: An Agentic Environment for Evaluating Specification Autoformalization

问题与 changed constraint：formal-spec generation is evaluated by executable official and adversarial tests, separating machine-checked syntax from fidelity to user intent and exposing LLM-judge misses。

机制与 ownership：We introduce Verus-SpecBench, a benchmark of 581 spec-writing tasks derived from Codeforces problems targeting Verus, a verifier for Rust, and Verus-SpecGym, an agentic environment in which models interact with Verus, bash, &amp; the filesystem to develop these specs. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26457v1 — § exact heading: 1 Introduction — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26457v1 — § exact heading: 2 Specification Autoformalization and Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26457v1 — § exact heading: 3.1 From Codeforces Problems to Benchmark Tasks — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26457:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26457:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26457:end -->

<!-- review:SF-2026-ARXIV-2605-26461:start -->
#### Characterization-Guided GPU Fault Resilience in NVIDIA MPS

问题与 changed constraint：GPU sharing needs fault-domain ownership: MMU isolation contains address faults while runtime recovery reconstitutes MPS clients after fatal SM faults。

机制与 ownership：NVIDIA Multi-Process Service (MPS) enables fine-grained GPU sharing by allowing multiple processes to execute concurrently on the same GPU, making it an important mechanism for improving GPU utilization. However, MPS has weak fault resilience: a fault in one process can terminate all co-running processes, limiting its adoption in resilience-critical settings such as multi-tenant GPU clusters. In this work, we design fault-resilient MPS to solve this problem. Our design is guided by insights from owner=`PLATFORM-GPU-SCHEDULER`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26461v1 — § exact heading: 2.1. GPU Execution Model — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26461v1 — § exact heading: 7. Implementation and Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26461v1 — § exact heading: 8. Discussion: Full Fault Isolation — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26461:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26461:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-26461:end -->

<!-- review:SF-2026-ARXIV-2605-26485:start -->
#### OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time Omnimodal Assistants

问题与 changed constraint：streaming evaluation must bind online event time, response windows, interruption state and native inference rather than offline QA.。

机制与 ownership：We introduce OmniInteract, a streaming benchmark for real-time omnimodal large language models evaluated through native online inference over audio-visual streams. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26485v1 — §3 benchmark, slot construction and interaction-aware scoring`；Evaluation=`arXiv:2605.26485v1 — §4 native-online inference, 1Q1A/1QnA and interruption analyses`。

Trade-off / failure：`arXiv:2605.26485v1 — no dedicated limitations; Appendix A licenses/scoring and §4.5 bound claims to 250 videos/1,430 slots`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26485:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26485:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26485:end -->

<!-- review:SF-2026-ARXIV-2605-26497:start -->
#### Aligning Provenance with Authorization: A Dual-Graph Defense for LLM Agents

问题与 changed constraint：authorization is checked against parameter provenance by comparing clean-intent and executed information-flow graphs.。

机制与 ownership：We propose AuthGraph, a dual-graph alignment defense framework that constructs two complementary graphs: an injected reasoning graph that models information provenance from the actual execution trajectory (including potentially manipulated attributions), and an authorization graph derived from the user's intent in an isolated clean context that is information-theoretically impossible to be influenced by injection; a graph alignment checker then structurally compares the two graphs to detect both tool-level and parameter-source-level deviations. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26497v1 — §3.1–3.4 IRG, clean-context authorization graph and alignment checker`；Evaluation=`arXiv:2605.26497v1 — §4.1 setup; §4.2 AgentDojo/AgentDyn results`。

Trade-off / failure：`arXiv:2605.26497v1 — §5 discussion; Appendix B.2 excludes user-authorized observation consumption`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26497:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26497:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26497:end -->

<!-- review:SF-2026-ARXIV-2605-26508:start -->
#### Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents

问题与 changed constraint：side-effecting tool calls gain a pre-action counterfactual risk budget, fixed safe default and underwriting boundary rather than relying on post-hoc liability review。

机制与 ownership：We propose a foundational runtime actuarial layer for autonomous AI agents in which every side-effect-bearing action carries a time-consistent, counterfactual risk toll computed against a contractually fixed safe default, inside an explicit underwriting boundary. owner=`AGENT-TOOL-CALLING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26508v1 — §3 Model; §4 Counterfactual Action Toll; §7 Runtime Risk Gating (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26508v1 — §7 conservative runtime budget guarantee; §8 empirical status (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26508v1 — §9 Residual Obligations and Scope (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26508:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26508:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26508:end -->

<!-- review:SF-2026-ARXIV-2605-26521:start -->
#### Testing Agentic Workflows with Structural Coverage Criteria

问题与 changed constraint：workflow testing gains structural obligations for agents, allowed/restricted tools and delegation edges, separate from task success.。

机制与 ownership：These results show that structural coverage provides a useful adequacy layer for multi-agent workflow testing: it does not replace semantic or end-to-end evaluation, but reveals whether declared agents, tool-access rules, restrictions, and delegation paths have been exercised. owner=`AGENT-WORKFLOW`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26521v1 — §III-A formal coverage model; §III-B–D generation, realization and observation`；Evaluation=`arXiv:2605.26521v1 — §IV benchmarks, runtime witnesses, fault injection and synthesis`。

Trade-off / failure：`arXiv:2605.26521v1 — §IV-I Threats to Validity; §VI says structural coverage complements, not replaces, semantic/end-to-end evaluation`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26521:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26521:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-26521:end -->

<!-- review:SF-2026-ARXIV-2605-26542:start -->
#### ChainCaps: Composition-Safe Tool-Using Agents via Monotonic Capability Attenuation

问题与 changed constraint：tool-chain authority becomes value-scoped and monotonically attenuated, closing permission laundering across locally legal calls.。

机制与 ownership：Tool-using agents increasingly operate in open-ended deployment environments, where they compose file systems, web APIs, code interpreters, and enterprise services at runtime. This creates a safety gap in tool composition: an agent can satisfy every per-tool permission check and still produce an unsafe end-to-end effect, such as reading a confidential document, summarizing it, and sending the summary to an external endpoint. We call this failure mode permission laundering. ChainCaps addresses it owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26542v1 — §3.1–3.6 threat model, budget algebra, runtime enforcement and non-amplification`；Evaluation=`arXiv:2605.26542v1 — §4.1–4.4 five-model evaluation, baselines, ablations and manifest-cost analysis`。

Trade-off / failure：`arXiv:2605.26542v1 — §4.5 Threats to Validity; claims limited to explicit proxy-visible flows with trusted manifests`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26542:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26542:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-26542:end -->

<!-- review:SF-2026-ARXIV-2605-26558:start -->
#### Cassandra: Enabling Reasoning LLMs at Edge via Self-Speculative Decoding

问题与 changed constraint：edge self-speculation couples salience-selected draft state, full-precision verification and a format-conversion hardware path.。

机制与 ownership：To address this challenge, we propose Cassandra, an algorithm-hardware co-designed self-speculative decoding framework optimized for low-batch scenarios. owner=`INFER-SPECULATIVE-DECODING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26558v1 — §IV Cassandra algorithm; §V hardware architecture and data management`；Evaluation=`arXiv:2605.26558v1 — §VI accuracy/performance/area-power evaluation; §VII comparisons`。

Trade-off / failure：`arXiv:2605.26558v1 — no dedicated limitations; §VII binds evidence to low-batch disclosed edge models/hardware and conversion module assumptions`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26558:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26558:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26558:end -->

<!-- review:SF-2026-ARXIV-2605-26563:start -->
#### TrajAudit: Automated Failure Diagnosis for Agentic Coding Systems

问题与 changed constraint：agent trajectories become diagnosable evidence when prior failure hypotheses, semantic saliency and an investigator agent preserve step-level failure localization。

机制与 ownership：To address these challenges, we propose \textit{TrajAudit}, an automated failure diagnosis framework specifically for trajectories produced by repository-level coding agents. owner=`PLATFORM-TRACE`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26563v1 — § exact heading: 2.2. Failure Localization Methods — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26563v1 — § exact heading: 3. The RootSE Benchmark — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26563v1 — § exact heading: 2.2. Failure Localization Methods — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26563:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26563:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26563:end -->

<!-- review:SF-2026-ARXIV-2605-26574:start -->
#### GradSentry: Gradient Spectral Entropy for Backdoor Sample Filtering in Large Language Model Fine-Tuning

问题与 changed constraint：fine-tuning admission can use gradient spectral entropy as a backdoor sensor, but the filter remains attack- and module-dependent rather than a proof of clean data。

机制与 ownership：We propose GradSentry({Grad}ient {Sentry}), a backdoor sample filtering method based on the spectral entropy of per-sample gradients. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26574v1 — § exact heading: 3 Method — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26574v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26574v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26574:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26574:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26574:end -->

<!-- review:SF-2026-ARXIV-2605-26606:start -->
#### Spend Your Rollouts Where It Counts: Rollout Allocation for Group-Based RL Post-Training

问题与 changed constraint：on-policy rollout budget is allocated from current-policy reward variance instead of uniformly across prompts.。

机制与 ownership：We introduce Pilot-Commit, a budget-aware rollout allocation framework for group-based RL post-training. owner=`TRAIN-GRPO`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26606v1 — §3.2 reward-variance signal; §3.3 Pilot-Commit; §3.4 optimizations`；Evaluation=`arXiv:2605.26606v1 — §4 setup; §5 results; §6 analysis`。

Trade-off / failure：`arXiv:2605.26606v1 — §7 Limitations — group RL, online estimates, staleness and disclosed model/workload boundary`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26606:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26606:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26606:end -->

<!-- review:SF-2026-ARXIV-2605-26667:start -->
#### MemFail: Stress-Testing Failure Modes of LLM Memory Systems

问题与 changed constraint：memory evaluation decomposes summary, storage and retrieval failures instead of treating memory as one black-box accuracy score.。

机制与 ownership：Large language model (LLM) agents increasingly rely on external memory systems to remain consistent across long-horizon interactions, but little empirical work has been done to understand the specific failure modes and design choices that these systems present. owner=`AGENT-MEMORY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26667v1 — §3.1 three memory operations; §3.2 failure taxonomy; §4 benchmark tasks`；Evaluation=`arXiv:2605.26667v1 — §5 setup; §6 four-memory-system experiments; Appendix C results`。

Trade-off / failure：`arXiv:2605.26667v1 — no named limitations; benchmark construction, chosen systems/tasks and judge prompts in Appendices B–D bound generalization — § exact-v1 limitations/counterevidence heading/fragment`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26667:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26667:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26667:end -->

<!-- review:SF-2026-ARXIV-2605-26684:start -->
#### Beyond Trajectory-Level Attribution: Graph-Based Credit Assignment for Agentic Reinforcement Learning

问题与 changed constraint：agentic RL credit moves from whole trajectories to an aggregated state-transition graph so shared prefixes and divergent actions receive different advantages。

机制与 ownership：To uncover latent information and enable more faithful step-level credit assignment, we propose Graph-based Group Policy Optimization (GraphGPO), which first aggregates all rollout trajectories into a unified state-transition graph and then estimates the distance from each state to the task goal using the global information encoded in the graph. owner=`TRAIN-GRPO`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26684v1 — § exact heading: 4 Proposed Method — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26684v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26684v1 — § exact heading: 4.1 Limitations of Trajectory-Level Attribution — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26684:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26684:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26684:end -->

<!-- review:SF-2026-ARXIV-2605-26691:start -->
#### Mind the Tool Failures: Achieving Synergistic Tool Gains for Medical Agents

问题与 changed constraint：tool-use training must assign asymmetric risk to failed, unnecessary and beneficial calls instead of rewarding tool invocation whenever the final answer succeeds。

机制与 ownership：Particularly, we propose a GRPO-based reinforcement learning framework with rewards for probabilistic risk minimization and disagreement-aware synergy learning, which promotes instance-level correction of erroneous tool consensus. owner=`AGENT-TOOL-CALLING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26691v1 — § exact heading: 2.2 Medical Vision-Language Models and Diagnostic Tools — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26691v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26691v1 — § exact heading: 5 Conclusion and Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26691:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26691:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26691:end -->

<!-- review:SF-2026-ARXIV-2605-26720:start -->
#### Towards Feedback-to-Plan Decisions for Self-Evolving LLM Agents in CUDA Kernel Generation

问题与 changed constraint：execution feedback is first converted into an explicit plan/no-plan decision and attributed by component before an agent edits a CUDA kernel。

机制与 ownership：We introduce \texttt{CUDAnalyst}, a unified analysis layer for controlled, generation-level attribution of planning decisions to feedback components via trajectory freezing and selective feedback injection. owner=`AGENT-REFLECTION`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26720v1 — § exact heading: 3 CUDAnalyst Design and Evaluation — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26720v1 — § exact heading: 3 CUDAnalyst Design and Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26720v1 — § exact heading: 6 Conclusion and Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26720:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26720:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26720:end -->

<!-- review:SF-2026-ARXIV-2605-26730:start -->
#### PRISM: A Multi-Dimensional Benchmark for Evaluating LLM Peer Reviewers

问题与 changed constraint：peer-review evaluation must preserve multiple review dimensions and disagreement rather than collapse reviewer quality into one aggregate judge score。

机制与 ownership：The rapid growth in submissions to machine learning venues has strained the scientific peer-review system and intensified interest in LLM-based automated peer reviewers. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26730v1 — § exact heading: 3 The PRISM Framework — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.26730v1 — § exact heading: 4 Experiment and analysis — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.26730v1 — § exact heading: C.3 Prompt Templates by Dimension — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26730:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26730:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26730:end -->

<!-- review:SF-2026-ARXIV-2605-26731:start -->
#### It's Not the Capability: Harness Sensitivity Is Non-Monotone Across LLM Agent Tiers

问题与 changed constraint：agent harness configuration is an evaluation treatment variable whose optimum is model-specific, not monotone in capability tier.。

机制与 ownership：We introduce a six-label failure taxonomy showing that format_violation dominates capable-model failures while wrong_file dominates low-capability failures, and we derive practical tier-aware harness selection guidelines. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26731v1 — §3 HEAT-24 workspace, harness conditions, models and failure taxonomy`；Evaluation=`arXiv:2605.26731v1 — §4 432-run results by harness/model/task and latency`。

Trade-off / failure：`arXiv:2605.26731v1 — §5 Limitations and threats — one model per tier, synthetic 24-task benchmark and model-specific observations`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26731:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26731:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-26731:end -->

<!-- review:SF-2026-ARXIV-2605-26754:start -->
#### Cordon-MAS: Defending RAG against Knowledge Poisoning via Information-Flow Control

问题与 changed constraint：RAG poisoning control removes untrusted prose from the synthesis principal and passes only audited claims across the boundary.。

机制与 ownership：We show this assumption is incorrect: models exhibit a monitoring-control gap -- they can detect contradictions in retrieved evidence yet still act on poisoned claims. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26754v1 — §3 CORDON-MAS and dirty-read, claim-only and certified-synthesis invariants`；Evaluation=`arXiv:2605.26754v1 — §4 setup; §5 results, ablations and adaptive attacks`。

Trade-off / failure：`arXiv:2605.26754v1 — §6 discussion; Appendix H limitations and Appendix B threat model`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26754:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26754:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-26754:end -->

<!-- review:SF-2026-ARXIV-2605-26778:start -->
#### The Attribution Blind Spot: Detecting When Language Models Rely on Memory Rather Than Retrieved Context

问题与 changed constraint：grounded output must distinguish retrieved-context causation from coincident parametric-memory recall.。

机制与 ownership：We name this failure the attribution blind spot and introduce Computational Reality Monitoring (CRM) to address it. owner=`AGENT-RAG`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.26778v1 — §3 Computational Reality Monitoring with paired context/no-context representations`；Evaluation=`arXiv:2605.26778v1 — §4 setup; §5 attribution experiments and interventions`。

Trade-off / failure：`arXiv:2605.26778v1 — §6 discussion/limitations; evidence is representation-level attribution on disclosed models/tasks, not universal causal identification`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-26778:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-26778:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-26778:end -->

<!-- review:SF-2026-ARXIV-2605-27091:start -->
#### MiRD: Reliable Set-Valued Prediction for Open-Ended Question Answering via Miscoverage Risk Decomposition

**问题与机制。** In this paper, we introduce MiRD, a two-stage framework that decomposes overall miscoverage into sampling failure and conditional selection failure. 该证据的系统 owner 定位为 `PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1 路径。** Method=`§3.2 sampling-failure bound; §3.3 conformal selection; §3.4 combined guarantee`；Evaluation=`§4 finite-sampling, conditional-selection and overall-miscoverage experiments`；Limitations/Counterevidence=`Appendix A conditional exchangeability and population-bound assumptions`。

<!-- claim:SF-2026-ARXIV-2605-27091:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-27091:end -->

Books Decision=`Integrate`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-27091:end -->

<!-- review:SF-2026-ARXIV-2605-27220:start -->
#### The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval Cascades in a Production RAG System

问题与 changed constraint：production RAG routes augmentation after measuring retrieval sufficiency and traces post-retrieval cascades instead of applying augmentation globally.。

机制与 ownership：We present a case study of the Danish National Encyclopedia, evaluating five retrieval workflows over 20,000 query-workflow pairs from production traffic and synthetic conditions. owner=`AGENT-RAG`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27220v1 — §3 production trace, pre-retrieval router and post-retrieval cascade decomposition`；Evaluation=`arXiv:2605.27220v1 — §4 workflows/data; §5 20,000 query-workflow results and cost/latency analysis`。

Trade-off / failure：`arXiv:2605.27220v1 — §6 limitations — single Danish encyclopedia, production policy and query-distribution boundary`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27220:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27220:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27220:end -->

<!-- review:SF-2026-ARXIV-2605-27292:start -->
#### Detectability in Diversity: Improved Canary Crafting for Privacy Auditing in One Run

问题与 changed constraint：one-run privacy audits need detectable, low-interference and diverse canaries rather than interchangeable probes.。

机制与 ownership：Motivated by recent theoretical insights suggesting that interference between canaries contributes to weaker leakage estimates compared to multi-run methods, we propose to optimize canaries to be both highly detectable and minimally interfering. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27292v1 — §3 influence-based canary selection; §4 refinement and diversity/IBIS`；Evaluation=`arXiv:2605.27292v1 — §5 experiments; Appendix D setup and ablations`。

Trade-off / failure：`arXiv:2605.27292v1 — Reasoned exception — manuscript has no dedicated Limitations section; Appendix A theoretical assumptions and Appendix D disclosed one-run image/classification setup bound claims — § exact-v1 limitations/counterevidence heading/fragment`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27292:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27292:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27292:end -->

<!-- review:SF-2026-ARXIV-2605-27328:start -->
#### Governed Evolution of Agent Runtimes through Executable Operational Cognition

问题与 changed constraint：self-modifying agent harnesses require versioned executable artifacts, capability lifecycle state, governance approval and rollback instead of ungoverned prompt/code mutation。

机制与 ownership：This paper proposes a framework for governed runtime evolution in multi-agent systems through executable operational cognition. owner=`AGENT-PLATFORM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27328v1 — § exact heading: 2.2 Code-Centric Reasoning, Acting, and Environment Modeling — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27328v1 — § exact heading: 1.1 Terminology and Conceptual Levels — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27328v1 — § exact heading: 12 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27328:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27328:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27328:end -->

<!-- review:SF-2026-ARXIV-2605-27333:start -->
#### FinHarness: An Inline Lifecycle Safety Harness for Finance LLM Agents

问题与 changed constraint：query and tool monitors form an inline lifecycle cascade whose fired evidence changes the next prompt while an external gate retains stop authority。

机制与 ownership：We present FinHarness, an inline safety harness that wraps a finance agent end-to-end with three components: a Query Monitor that fuses single-turn intent with cross-turn drift, a Tool Monitor that evaluates each prospective tool call, and a Cascade module that integrates per-step risk and adaptively routes verification between a lightweight and an advanced-tier LLM judge. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27333v1 — § exact heading: 3 Method: FinHarness — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27333v1 — § exact heading: 4 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27333v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27333:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27333:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27333:end -->

<!-- review:SF-2026-ARXIV-2605-27361:start -->
#### Natural Language Query to Configuration for Retrieval Agents

问题与 changed constraint：retrieval configuration becomes a per-query control decision over the whole pipeline after workload-specific characterization and Pareto pruning。

机制与 ownership：We propose **BRANE**, which uses an LLM to convert each query into workload-specific characteristics, then trains a lightweight per-configuration predictor that estimates whether the pipeline will answer the query correctly. owner=`AGENT-RAG`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27361v1 — § exact heading: 4 BRANE: Methodology — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27361v1 — § exact heading: 5 Evaluations and Ablations — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27361v1 — § exact heading: 6 Limitations and Broader Impact — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27361:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27361:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27361:end -->

<!-- review:SF-2026-ARXIV-2605-27366:start -->
#### MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation

问题与 changed constraint：agent skills need creation, memory, selection, evaluation and replacement as one governed lifecycle rather than an append-only prompt library。

机制与 ownership：We propose MUSE-Autoskill Agent (Memory-Utilizing Skill Evolution), a skill-centric agent framework that creates, reuses, and refines skills under a unified lifecycle: creation, memory, management, evaluation, and refinement. owner=`AGENT-PLATFORM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27366v1 — § exact heading: 2.2 Automatic Skill Systems — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27366v1 — § exact heading: 2.3 Benchmarks and Positioning — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27366v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27366:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27366:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27366:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-26118 | exact-v1 evaluation for Xe-Forge: Multi-Stage LLM-Powered Kernel Optimization for Intel GPU | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-26120 | exact-v1 evaluation for Semantic-aware Token Selection and Resource Optimization for Communication-efficient Split Federated Fine-tuning in Edge Intelligence | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-26440 | exact-v1 evaluation for Conv-to-Bench: Evaluating Language Models Via User-Assistant Dialogues In Code Tasks | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-26444 | exact-v1 evaluation for MicroSpec: Accelerating Speculative Decoding with Lightweight In-Context Vocabularies | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-26128 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26128 |
| SF-2026-ARXIV-2605-26132 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26132 |
| SF-2026-ARXIV-2605-26147 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26147 |
| SF-2026-ARXIV-2605-26154 | score_7_9 | selected | DA-20260527-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260527-01 |
| SF-2026-ARXIV-2605-26156 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26156 |
| SF-2026-ARXIV-2605-26158 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26158 |
| SF-2026-ARXIV-2605-26159 | score_7_9 | selected | DA-20260527-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260527-02 |
| SF-2026-ARXIV-2605-26161 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26161 |
| SF-2026-ARXIV-2605-26162 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26162 |
| SF-2026-ARXIV-2605-26165 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26165 |
| SF-2026-ARXIV-2605-26172 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26172 |
| SF-2026-ARXIV-2605-26177 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26177 |
| SF-2026-ARXIV-2605-26184 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26184 |
| SF-2026-ARXIV-2605-26200 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26200 |
| SF-2026-ARXIV-2605-26242 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26242 |
| SF-2026-ARXIV-2605-26248 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26248 |
| SF-2026-ARXIV-2605-26252 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26252 |
| SF-2026-ARXIV-2605-26266 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26266 |
| SF-2026-ARXIV-2605-26269 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26269 |
| SF-2026-ARXIV-2605-26282 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26282 |
| SF-2026-ARXIV-2605-26289 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26289 |
| SF-2026-ARXIV-2605-26297 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26297 |
| SF-2026-ARXIV-2605-26298 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26298 |
| SF-2026-ARXIV-2605-26302 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26302 |
| SF-2026-ARXIV-2605-26321 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26321 |
| SF-2026-ARXIV-2605-26323 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26323 |
| SF-2026-ARXIV-2605-26327 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26327 |
| SF-2026-ARXIV-2605-26340 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26340 |
| SF-2026-ARXIV-2605-26362 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26362 |
| SF-2026-ARXIV-2605-26379 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26379 |
| SF-2026-ARXIV-2605-26384 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26384 |
| SF-2026-ARXIV-2605-26403 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26403 |
| SF-2026-ARXIV-2605-26418 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26418 |
| SF-2026-ARXIV-2605-26433 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26433 |
| SF-2026-ARXIV-2605-26444 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26444 |
| SF-2026-ARXIV-2605-26457 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26457 |
| SF-2026-ARXIV-2605-26461 | score_7_9;forced_review;potential_books_delta | selected | DA-20260527-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260527-03 |
| SF-2026-ARXIV-2605-26485 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26485 |
| SF-2026-ARXIV-2605-26497 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26497 |
| SF-2026-ARXIV-2605-26508 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26508 |
| SF-2026-ARXIV-2605-26521 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26521 |
| SF-2026-ARXIV-2605-26542 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26542 |
| SF-2026-ARXIV-2605-26563 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26563 |
| SF-2026-ARXIV-2605-26574 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26574 |
| SF-2026-ARXIV-2605-26606 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26606 |
| SF-2026-ARXIV-2605-26667 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26667 |
| SF-2026-ARXIV-2605-26684 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26684 |
| SF-2026-ARXIV-2605-26691 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26691 |
| SF-2026-ARXIV-2605-26720 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26720 |
| SF-2026-ARXIV-2605-26730 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26730 |
| SF-2026-ARXIV-2605-26754 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26754 |
| SF-2026-ARXIV-2605-26778 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-26778 |
| SF-2026-ARXIV-2605-27091 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27091 |
| SF-2026-ARXIV-2605-27220 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27220 |
| SF-2026-ARXIV-2605-27292 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27292 |
| SF-2026-ARXIV-2605-27328 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27328 |
| SF-2026-ARXIV-2605-27333 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27333 |
| SF-2026-ARXIV-2605-27361 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27361 |
| SF-2026-ARXIV-2605-27366 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27366 |

<!-- analysis-decision:SF-2026-ARXIV-2605-26128:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26132:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26132:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26147:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26147:end -->

<!-- analysis:DA-20260527-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-26154

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260527-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26156:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26156:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26158:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26158:end -->

<!-- analysis:DA-20260527-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-26159

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260527-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26161:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26161:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26162:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26162:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26165:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26165:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26172:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26177:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26177:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26184:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26200:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26200:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26242:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26248:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26248:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26252:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26252:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26266:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26266:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26269:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26282:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26289:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26289:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26297:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26297:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26298:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26298:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26302:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26302:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26321:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26321:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26323:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26323:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26327:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26327:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26340:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26362:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26362:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26379:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26379:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26384:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26403:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26418:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26418:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26433:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26444:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26457:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26457:end -->

<!-- analysis:DA-20260527-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-26461

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260527-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26485:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26485:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26497:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26497:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26508:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26521:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26521:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26542:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26542:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26563:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26563:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26574:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26606:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26606:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26667:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26667:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26684:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26684:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26691:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26691:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26720:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26720:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26730:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26730:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26754:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-26778:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-26778:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27091:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27091:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27220:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27220:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27292:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27292:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27328:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27328:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27333:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27333:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27361:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27361:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27366:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27366:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-26118 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L53 (H3: Execution Plan 可以修订，但只能在安全边界 Commit) | books/part-05-inference-system/48-speculative-decoding.md#L10 (H2: 本章要回答的问题); books/part-05-inference-system/50-vllm.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-26118 | delta:SF-2026-ARXIV-2605-26118 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26118 |
| SF-2026-ARXIV-2605-26120 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L265 (H2: 从 Collective 到 AI State Transfer) | books/part-04-training-system/35-checkpoint.md#L10 (H2: 本章要回答的问题); books/part-04-training-system/37-tensor-parallel.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-26120 | delta:SF-2026-ARXIV-2605-26120 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26120 |
| SF-2026-ARXIV-2605-26128 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-26128 | delta:SF-2026-ARXIV-2605-26128 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26128 |
| SF-2026-ARXIV-2605-26132 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-26132 | delta:SF-2026-ARXIV-2605-26132 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26132 |
| SF-2026-ARXIV-2605-26147 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-26147 | delta:SF-2026-ARXIV-2605-26147 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26147 |
| SF-2026-ARXIV-2605-26154 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26154 | delta:SF-2026-ARXIV-2605-26154 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26154 |
| SF-2026-ARXIV-2605-26156 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26156 | delta:SF-2026-ARXIV-2605-26156 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26156 |
| SF-2026-ARXIV-2605-26158 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26158 | delta:SF-2026-ARXIV-2605-26158 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26158 |
| SF-2026-ARXIV-2605-26159 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-26159 | delta:SF-2026-ARXIV-2605-26159 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26159 |
| SF-2026-ARXIV-2605-26161 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26161 | delta:SF-2026-ARXIV-2605-26161 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26161 |
| SF-2026-ARXIV-2605-26162 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-26162 | delta:SF-2026-ARXIV-2605-26162 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26162 |
| SF-2026-ARXIV-2605-26165 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-26165 | delta:SF-2026-ARXIV-2605-26165 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26165 |
| SF-2026-ARXIV-2605-26172 | MODEL-SAMPLING | books/part-02-model/20-sampling.md#chapter-20 | books/part-02-model/19-kv-cache.md#chapter-19;books/part-02-model/21-moe.md#chapter-21 | existing:SF-2026-ARXIV-2605-26172 | delta:SF-2026-ARXIV-2605-26172 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26172 |
| SF-2026-ARXIV-2605-26177 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26177 | delta:SF-2026-ARXIV-2605-26177 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26177 |
| SF-2026-ARXIV-2605-26184 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-26184 | delta:SF-2026-ARXIV-2605-26184 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26184 |
| SF-2026-ARXIV-2605-26200 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26200 | delta:SF-2026-ARXIV-2605-26200 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26200 |
| SF-2026-ARXIV-2605-26242 | WORLDVIEW-LLM-INTELLIGENCE | books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-8 | books/part-01-worldview/07-scaling-law.md#chapter-7;books/part-01-worldview/09-ai-system-evolution.md#chapter-9 | existing:SF-2026-ARXIV-2605-26242 | delta:SF-2026-ARXIV-2605-26242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26242 |
| SF-2026-ARXIV-2605-26248 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#chapter-7 | books/part-01-worldview/06-why-transformer-changed-the-world.md#chapter-6;books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-8 | existing:SF-2026-ARXIV-2605-26248 | delta:SF-2026-ARXIV-2605-26248 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26248 |
| SF-2026-ARXIV-2605-26252 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-26252 | delta:SF-2026-ARXIV-2605-26252 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26252 |
| SF-2026-ARXIV-2605-26266 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-26266 | delta:SF-2026-ARXIV-2605-26266 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26266 |
| SF-2026-ARXIV-2605-26269 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26269 | delta:SF-2026-ARXIV-2605-26269 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26269 |
| SF-2026-ARXIV-2605-26282 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-26282 | delta:SF-2026-ARXIV-2605-26282 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26282 |
| SF-2026-ARXIV-2605-26289 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-26289 | delta:SF-2026-ARXIV-2605-26289 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26289 |
| SF-2026-ARXIV-2605-26297 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26297 | delta:SF-2026-ARXIV-2605-26297 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26297 |
| SF-2026-ARXIV-2605-26298 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26298 | delta:SF-2026-ARXIV-2605-26298 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26298 |
| SF-2026-ARXIV-2605-26302 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-26302 | delta:SF-2026-ARXIV-2605-26302 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26302 |
| SF-2026-ARXIV-2605-26321 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26321 | delta:SF-2026-ARXIV-2605-26321 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26321 |
| SF-2026-ARXIV-2605-26323 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-26323 | delta:SF-2026-ARXIV-2605-26323 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26323 |
| SF-2026-ARXIV-2605-26327 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-26327 | delta:SF-2026-ARXIV-2605-26327 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26327 |
| SF-2026-ARXIV-2605-26340 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-26340 | delta:SF-2026-ARXIV-2605-26340 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26340 |
| SF-2026-ARXIV-2605-26362 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26362 | delta:SF-2026-ARXIV-2605-26362 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26362 |
| SF-2026-ARXIV-2605-26379 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-26379 | delta:SF-2026-ARXIV-2605-26379 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26379 |
| SF-2026-ARXIV-2605-26384 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62;books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-26384 | delta:SF-2026-ARXIV-2605-26384 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26384 |
| SF-2026-ARXIV-2605-26403 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-26403 | delta:SF-2026-ARXIV-2605-26403 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26403 |
| SF-2026-ARXIV-2605-26418 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62; books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-26418 | delta:SF-2026-ARXIV-2605-26418 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26418 |
| SF-2026-ARXIV-2605-26433 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26433 | delta:SF-2026-ARXIV-2605-26433 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26433 |
| SF-2026-ARXIV-2605-26440 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L238 (H2: 第二个不变量：评估结论总是相对于分布) | books/part-06-ai-infrastructure/65-kai-scheduler.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/67-monitoring.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-26440 | delta:SF-2026-ARXIV-2605-26440 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26440 |
| SF-2026-ARXIV-2605-26444 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L196 (H2: Verify Length 不是孤立的固定超参数) | books/part-05-inference-system/47-pagedattention.md#L10 (H2: 本章要回答的问题); books/part-05-inference-system/49-tensorrt-llm.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-26444 | delta:SF-2026-ARXIV-2605-26444 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26444 |
| SF-2026-ARXIV-2605-26457 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26457 | delta:SF-2026-ARXIV-2605-26457 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26457 |
| SF-2026-ARXIV-2605-26461 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#chapter-63 | books/part-06-ai-infrastructure/62-gateway.md#chapter-62; books/part-06-ai-infrastructure/64-volcano.md#chapter-64 | existing:SF-2026-ARXIV-2605-26461 | delta:SF-2026-ARXIV-2605-26461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26461 |
| SF-2026-ARXIV-2605-26485 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26485 | delta:SF-2026-ARXIV-2605-26485 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26485 |
| SF-2026-ARXIV-2605-26497 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26497 | delta:SF-2026-ARXIV-2605-26497 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26497 |
| SF-2026-ARXIV-2605-26508 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-26508 | delta:SF-2026-ARXIV-2605-26508 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26508 |
| SF-2026-ARXIV-2605-26521 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-26521 | delta:SF-2026-ARXIV-2605-26521 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26521 |
| SF-2026-ARXIV-2605-26542 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26542 | delta:SF-2026-ARXIV-2605-26542 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26542 |
| SF-2026-ARXIV-2605-26558 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-26558 | delta:SF-2026-ARXIV-2605-26558 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26558 |
| SF-2026-ARXIV-2605-26563 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#chapter-69 | books/part-06-ai-infrastructure/68-logging.md#chapter-68; books/part-06-ai-infrastructure/70-cost.md#chapter-70 | existing:SF-2026-ARXIV-2605-26563 | delta:SF-2026-ARXIV-2605-26563 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26563 |
| SF-2026-ARXIV-2605-26574 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26574 | delta:SF-2026-ARXIV-2605-26574 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26574 |
| SF-2026-ARXIV-2605-26606 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-26606 | delta:SF-2026-ARXIV-2605-26606 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26606 |
| SF-2026-ARXIV-2605-26667 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-26667 | delta:SF-2026-ARXIV-2605-26667 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26667 |
| SF-2026-ARXIV-2605-26684 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-26684 | delta:SF-2026-ARXIV-2605-26684 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26684 |
| SF-2026-ARXIV-2605-26691 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-26691 | delta:SF-2026-ARXIV-2605-26691 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26691 |
| SF-2026-ARXIV-2605-26720 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79; books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-26720 | delta:SF-2026-ARXIV-2605-26720 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26720 |
| SF-2026-ARXIV-2605-26730 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26730 | delta:SF-2026-ARXIV-2605-26730 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26730 |
| SF-2026-ARXIV-2605-26731 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-26731 | delta:SF-2026-ARXIV-2605-26731 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26731 |
| SF-2026-ARXIV-2605-26754 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-26754 | delta:SF-2026-ARXIV-2605-26754 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26754 |
| SF-2026-ARXIV-2605-26778 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-26778 | delta:SF-2026-ARXIV-2605-26778 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-26778 |
| SF-2026-ARXIV-2605-27091 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27091 | delta:SF-2026-ARXIV-2605-27091 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27091 |
| SF-2026-ARXIV-2605-27220 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-27220 | delta:SF-2026-ARXIV-2605-27220 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27220 |
| SF-2026-ARXIV-2605-27292 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27292 | delta:SF-2026-ARXIV-2605-27292 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27292 |
| SF-2026-ARXIV-2605-27328 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27328 | delta:SF-2026-ARXIV-2605-27328 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27328 |
| SF-2026-ARXIV-2605-27333 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27333 | delta:SF-2026-ARXIV-2605-27333 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27333 |
| SF-2026-ARXIV-2605-27361 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-27361 | delta:SF-2026-ARXIV-2605-27361 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27361 |
| SF-2026-ARXIV-2605-27366 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27366 | delta:SF-2026-ARXIV-2605-27366 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27366 |

<!-- books-review:SF-2026-ARXIV-2605-26118:start -->
<!-- existing:SF-2026-ARXIV-2605-26118:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L53 (H3: Execution Plan 可以修订，但只能在安全边界 Commit)` 及相邻章节后，现有命题为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-26118:end -->
<!-- delta:SF-2026-ARXIV-2605-26118:start -->Exact-v1 的 source-specific delta 是：We present Xe-Forge, a multi-stage LLM-powered pipeline that automates this process for Intel GPU. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-26118:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-26118:end -->

<!-- books-review:SF-2026-ARXIV-2605-26120:start -->
<!-- existing:SF-2026-ARXIV-2605-26120:start -->对读 `books/part-04-training-system/36-distributed-training.md#L265 (H2: 从 Collective 到 AI State Transfer)` 及相邻章节后，现有命题为：本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-26120:end -->
<!-- delta:SF-2026-ARXIV-2605-26120:start -->Exact-v1 的 source-specific delta 是：To address this bottleneck, we propose ST-SFLora, a semantic token-based split federated LoRA fine-tuning framework. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-26120:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-26120:end -->

<!-- books-review:SF-2026-ARXIV-2605-26128:start -->
<!-- existing:SF-2026-ARXIV-2605-26128:start -->已顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。第78章已拥有 structured output、tool proposal、schema validation 与 effect receipt 的边界。`The Constraint Tax: Measuring Validity-Correctness Tradeoffs in Structured Outputs for Small Language Models` 的 source-specific 机制是：We show that this assumption is unsafe for small models.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-26128:end -->
<!-- delta:SF-2026-ARXIV-2605-26128:start -->We show that this assumption is unsafe for small models.<!-- delta:SF-2026-ARXIV-2605-26128:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26128:end -->

<!-- books-review:SF-2026-ARXIV-2605-26132:start -->
<!-- existing:SF-2026-ARXIV-2605-26132:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。第27章已把 synthetic generation、executable filtering、trajectory compilation、lineage、coverage 与真实环境 authority 连接成数据控制面。`Self-Verified Distillation: Your Language Model Is Secretly Its Own Synthetic Data Pipeline` 的 source-specific 机制是：We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-26132:end -->
<!-- delta:SF-2026-ARXIV-2605-26132:start -->We study this setting starting only from unlabeled seed questions with no ground-truth solutions, across three reasoning domains: math, science, and coding.<!-- delta:SF-2026-ARXIV-2605-26132:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26132:end -->

<!-- books-review:SF-2026-ARXIV-2605-26147:start -->
<!-- existing:SF-2026-ARXIV-2605-26147:start -->正文已覆盖 workload-aware admission、placement、batch cost、SLO 与 fallback。 本 family 的具体机制 `We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG).` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-26147:end -->
<!-- delta:SF-2026-ARXIV-2605-26147:start -->We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG).<!-- delta:SF-2026-ARXIV-2605-26147:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-26147:end -->

<!-- books-review:SF-2026-ARXIV-2605-26154:start -->
<!-- existing:SF-2026-ARXIV-2605-26154:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26154:end -->
<!-- delta:SF-2026-ARXIV-2605-26154:start -->Experiments across 3 benchmarks, 10 agent backbones, and 3 memory-module implementations show that MemMorph achieves up to 85.9% attack success rate with only three injected records, outperforming the strongest baseline by up to 25% while retaining potency under 3 representative defenses.<!-- delta:SF-2026-ARXIV-2605-26154:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26154:end -->

<!-- books-review:SF-2026-ARXIV-2605-26156:start -->
<!-- existing:SF-2026-ARXIV-2605-26156:start -->Ch66 已把 position/style/self-preference 及 irrelevant-style intervention 写入 judge construct-validity contract。<!-- existing:SF-2026-ARXIV-2605-26156:end -->
<!-- delta:SF-2026-ARXIV-2605-26156:start -->把 judge 的 style sensitivity 暴露为可自适应搜索的黑盒攻击面，并同时测 utility、stealth 与 query budget。<!-- delta:SF-2026-ARXIV-2605-26156:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26156:end -->

<!-- books-review:SF-2026-ARXIV-2605-26158:start -->
<!-- existing:SF-2026-ARXIV-2605-26158:start -->Ch72 已要求 run-centric multi-turn/multimodal campaign、跨 turn cumulative intent 聚合和 sensor/authority 分离。<!-- existing:SF-2026-ARXIV-2605-26158:end -->
<!-- delta:SF-2026-ARXIV-2605-26158:start -->把 refusal 从单一二元阈值改写为可重复采样的 instability band，并把分散于多个 benign-looking probes/视觉片段中的意图在最终 synthesis 时重新组合为跨 turn 攻击。<!-- delta:SF-2026-ARXIV-2605-26158:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26158:end -->

<!-- books-review:SF-2026-ARXIV-2605-26159:start -->
<!-- existing:SF-2026-ARXIV-2605-26159:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26159:end -->
<!-- delta:SF-2026-ARXIV-2605-26159:start -->We present the Device Context Protocol (DCP): a sub-50-byte typical frame (6-byte header + CBOR payload + optional 16-byte HMAC), a manifest schema in which capability scoping, range and type checks, dry-run evaluation, and units-as-types are protocol-layer primitives, and a host-side Bridge that rejects malformed or hallucinated calls before any byte reaches the device.<!-- delta:SF-2026-ARXIV-2605-26159:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26159:end -->

<!-- books-review:SF-2026-ARXIV-2605-26161:start -->
<!-- existing:SF-2026-ARXIV-2605-26161:start -->Ch27/Ch66 已保存 contamination source identity、transformed duplicates、sensor uncertainty 与 clean/contaminated slices。<!-- existing:SF-2026-ARXIV-2605-26161:end -->
<!-- delta:SF-2026-ARXIV-2605-26161:start -->用 fine-tuning loss drop、backbone displacement 与 reference-model debiasing构成 dataset-level contamination-risk sensor，处理连续时序的缩放/重采样重复。<!-- delta:SF-2026-ARXIV-2605-26161:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26161:end -->

<!-- books-review:SF-2026-ARXIV-2605-26162:start -->
<!-- existing:SF-2026-ARXIV-2605-26162:start -->Ch36 已有 asynchronous arrival bias、staleness、client weighting 与 compression，但没有把 push-sum numerator/denominator 和 in-flight mass 写成恢复/收敛状态。<!-- existing:SF-2026-ARXIV-2605-26162:end -->
<!-- delta:SF-2026-ARXIV-2605-26162:start -->在无中心异步联邦训练中用 push-sum numerator/denominator、in-flight mass 与 buffered message state 修正有向图聚合偏差，并以 centroid dictionary 压缩通信。<!-- delta:SF-2026-ARXIV-2605-26162:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26162:end -->

<!-- books-review:SF-2026-ARXIV-2605-26165:start -->
<!-- existing:SF-2026-ARXIV-2605-26165:start -->已顺读 `books/part-07-agent/75-context.md` 及相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']；当前主干=['本章要回答的问题', 'Context 是一次调用的可见状态', 'Token Budget 是容量约束', '为什么“全塞进去”会失败', 'Context Assembly Pipeline', 'Context Serving 是派生视图生命周期', 'Semantic Policy 与 Recoverable Bookkeeping 应分 Owner', 'Context Compression 的损失']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26165:end -->
<!-- delta:SF-2026-ARXIV-2605-26165:start -->We present the first systematic study of this tool-context trade-off, evaluating 14 models spanning 1.5B-32B local models plus one frontier API model across 6,566 controlled API calls at three context budgets (8K, 16K, 32K) with 28 tool definitions.<!-- delta:SF-2026-ARXIV-2605-26165:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26165:end -->

<!-- books-review:SF-2026-ARXIV-2605-26172:start -->
<!-- existing:SF-2026-ARXIV-2605-26172:start -->已顺读 `books/part-02-model/20-sampling.md` 及相邻章节 ['books/part-02-model/19-kv-cache.md', 'books/part-02-model/21-moe.md']；当前主干=['本章要回答的问题', 'Logits 还不是概率', '一个固定 logits 例子', 'Greedy decoding：每步取最大值', 'Temperature 改变分布锐度', 'Top-k：固定保留 k 个候选', 'Top-p：按累计概率动态截断', '参数组合的顺序很重要']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26172:end -->
<!-- delta:SF-2026-ARXIV-2605-26172:start -->We show that these trajectories are not independent: for a given question, they concentrate into a small number of clusters, or reasoning basins, each defined by a normalized final answer and the solutions that reach it.<!-- delta:SF-2026-ARXIV-2605-26172:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26172:end -->

<!-- books-review:SF-2026-ARXIV-2605-26177:start -->
<!-- existing:SF-2026-ARXIV-2605-26177:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26177:end -->
<!-- delta:SF-2026-ARXIV-2605-26177:start -->Code agents are currently having skillful performance on repository-level software engineering benchmarks, but it remains unclear whether success on end-to-end tasks such as issue resolution truly reflects repository context reasoning, the ability to identify the task-relevant information across multiple files and reason over the relations among them.<!-- delta:SF-2026-ARXIV-2605-26177:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26177:end -->

<!-- books-review:SF-2026-ARXIV-2605-26184:start -->
<!-- existing:SF-2026-ARXIV-2605-26184:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26184:end -->
<!-- delta:SF-2026-ARXIV-2605-26184:start -->We propose GAC, a noise-aware controller that derives an adaptive mixing weight from online estimates of gradient variance and disagreement between the two training signals.<!-- delta:SF-2026-ARXIV-2605-26184:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26184:end -->

<!-- books-review:SF-2026-ARXIV-2605-26200:start -->
<!-- existing:SF-2026-ARXIV-2605-26200:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26200:end -->
<!-- delta:SF-2026-ARXIV-2605-26200:start -->These collapses are not inherent limits of autonomy but correctable design choices.<!-- delta:SF-2026-ARXIV-2605-26200:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26200:end -->

<!-- books-review:SF-2026-ARXIV-2605-26242:start -->
<!-- existing:SF-2026-ARXIV-2605-26242:start -->已顺读 `books/part-01-worldview/08-why-llms-show-intelligence.md` 及相邻章节 ['books/part-01-worldview/07-scaling-law.md', 'books/part-01-worldview/09-ai-system-evolution.md']；当前主干=['本章要回答的问题', '“只是预测下一个 token”少算了什么', '从表面统计到可复用结构', '为什么规模会扩大能力范围', 'In-context learning 改变了任务接口', 'Post-training 把通用预测器塑造成可用接口', 'Emergence：现象、指标与解释必须分开', 'Tool use 为什么会放大模型能力']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26242:end -->
<!-- delta:SF-2026-ARXIV-2605-26242:start -->We identify two conditions that a paradigm needs to meet in order to establish introspection.<!-- delta:SF-2026-ARXIV-2605-26242:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26242:end -->

<!-- books-review:SF-2026-ARXIV-2605-26248:start -->
<!-- existing:SF-2026-ARXIV-2605-26248:start -->已顺读 `books/part-01-worldview/07-scaling-law.md` 及相邻章节 ['books/part-01-worldview/06-why-transformer-changed-the-world.md', 'books/part-01-worldview/08-why-llms-show-intelligence.md']；当前主干=['本章要回答的问题', '为什么先做实验，而不是先问“大模型多大才够”', 'Power law 的直觉', '参数、数据和 Compute 不能独立解释', 'Kaplan 与 Chinchilla 的结论为什么不同', '为什么会出现相对平滑的规律', 'Loss 曲线不能直接推出具体能力', '数据质量改变“D”的含义']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26248:end -->
<!-- delta:SF-2026-ARXIV-2605-26248:start -->We present a functional form (that we refer to as a Unified Neural Scaling Law (UNSL)) that accurately models and extrapolates the scaling behaviors of deep neural networks as multiple dimensions all vary simultaneously (i.e.<!-- delta:SF-2026-ARXIV-2605-26248:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26248:end -->

<!-- books-review:SF-2026-ARXIV-2605-26252:start -->
<!-- existing:SF-2026-ARXIV-2605-26252:start -->已顺读 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前主干=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26252:end -->
<!-- delta:SF-2026-ARXIV-2605-26252:start -->Long-running AI agents need persistent memory.<!-- delta:SF-2026-ARXIV-2605-26252:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26252:end -->

<!-- books-review:SF-2026-ARXIV-2605-26266:start -->
<!-- existing:SF-2026-ARXIV-2605-26266:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前主干=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26266:end -->
<!-- delta:SF-2026-ARXIV-2605-26266:start -->We show that a key driver of this degradation is a systematic bias in attention weights: due to the convexity of the exponential in softmax attention, quantization noise inflates the contribution of cached keys, a phenomenon we call the Jensen bias.<!-- delta:SF-2026-ARXIV-2605-26266:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26266:end -->

<!-- books-review:SF-2026-ARXIV-2605-26269:start -->
<!-- existing:SF-2026-ARXIV-2605-26269:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26269:end -->
<!-- delta:SF-2026-ARXIV-2605-26269:start -->We introduce AgentSecBench as an empirical instantiation of a formal security framework for this problem.<!-- delta:SF-2026-ARXIV-2605-26269:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26269:end -->

<!-- books-review:SF-2026-ARXIV-2605-26282:start -->
<!-- existing:SF-2026-ARXIV-2605-26282:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26282:end -->
<!-- delta:SF-2026-ARXIV-2605-26282:start -->Beyond these issues, we identify a more critical yet underexplored bottleneck: a structural misalignment between search and value learning in existing world model approaches.<!-- delta:SF-2026-ARXIV-2605-26282:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26282:end -->

<!-- books-review:SF-2026-ARXIV-2605-26289:start -->
<!-- existing:SF-2026-ARXIV-2605-26289:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；现有主干覆盖 prefix reuse 与连续 session state，但尚未覆盖跨离散 Tool-loop request 的 persistent KV、sequence-pool ownership 和交错 multi-agent prefix sharing。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26289:end -->
<!-- delta:SF-2026-ARXIV-2605-26289:start -->We present a stateful inference architecture that converts the $O(n_t)$ per-turn cost of conventional serving into an $O(Δ_t)$ delta-only cost: a persistent KV cache lives across turns and advances by ingesting only the new tokens, while a radix prefix cache extends this across interleaved multi-agent traffic and a prompt-lookup speculative decoder accelerates structured output.<!-- delta:SF-2026-ARXIV-2605-26289:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26289:end -->

<!-- books-review:SF-2026-ARXIV-2605-26297:start -->
<!-- existing:SF-2026-ARXIV-2605-26297:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26297:end -->
<!-- delta:SF-2026-ARXIV-2605-26297:start -->Our study shows that agentic workloads are not simply long-prompt workloads: with effective context caching, most input tokens are reused across turns, making execution decode-dominated while increasing dependence on long-lived KV-cache state.<!-- delta:SF-2026-ARXIV-2605-26297:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26297:end -->

<!-- books-review:SF-2026-ARXIV-2605-26298:start -->
<!-- existing:SF-2026-ARXIV-2605-26298:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26298:end -->
<!-- delta:SF-2026-ARXIV-2605-26298:start -->AI agents increasingly run untrusted code on developer machines: shell commands generated by language models, third-party scripts retrieved at runtime, and tool plugins of unknown provenance.<!-- delta:SF-2026-ARXIV-2605-26298:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26298:end -->

<!-- books-review:SF-2026-ARXIV-2605-26302:start -->
<!-- existing:SF-2026-ARXIV-2605-26302:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 及相邻章节 ['books/part-07-agent/83-mcp.md', 'books/part-07-agent/README.md']；当前主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26302:end -->
<!-- delta:SF-2026-ARXIV-2605-26302:start -->We introduce AgingBench, a longitudinal reliability benchmark for agent lifespan engineering: measuring not only whether deployed agents degrade, but what form the degradation takes and where repair should target.<!-- delta:SF-2026-ARXIV-2605-26302:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26302:end -->

<!-- books-review:SF-2026-ARXIV-2605-26321:start -->
<!-- existing:SF-2026-ARXIV-2605-26321:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26321:end -->
<!-- delta:SF-2026-ARXIV-2605-26321:start -->We introduce Anchor, a task-generation pipeline that formalizes domain experts' specifications of business workflows into constraint optimization programs.<!-- delta:SF-2026-ARXIV-2605-26321:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26321:end -->

<!-- books-review:SF-2026-ARXIV-2605-26323:start -->
<!-- existing:SF-2026-ARXIV-2605-26323:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 及相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前主干=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26323:end -->
<!-- delta:SF-2026-ARXIV-2605-26323:start -->We propose Totoro$^+$, a novel scalable FL system that enables massive FL applications to run simultaneously on edge networks.<!-- delta:SF-2026-ARXIV-2605-26323:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26323:end -->

<!-- books-review:SF-2026-ARXIV-2605-26327:start -->
<!-- existing:SF-2026-ARXIV-2605-26327:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 及相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前主干=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26327:end -->
<!-- delta:SF-2026-ARXIV-2605-26327:start -->We propose a reparametrization of the preconditioner that supports BFP16 storage and forms a complete basis by combining updated basis vectors with unchanged ones.<!-- delta:SF-2026-ARXIV-2605-26327:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26327:end -->

<!-- books-review:SF-2026-ARXIV-2605-26340:start -->
<!-- existing:SF-2026-ARXIV-2605-26340:start -->已顺读 `books/part-07-agent/81-workflow.md` 及相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前主干=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Task State Alignment 是每次 Dispatch 的前置条件', 'Deterministic Spine，Agentic Nodes']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26340:end -->
<!-- delta:SF-2026-ARXIV-2605-26340:start -->Autonomous research agents produce competitive solutions and professional-looking manuscripts, yet their outputs contain verifiability failures undetectable by surface-level evaluation: fabricated citations, unreproducible scores, and method descriptions that diverge from the implementation.<!-- delta:SF-2026-ARXIV-2605-26340:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26340:end -->

<!-- books-review:SF-2026-ARXIV-2605-26362:start -->
<!-- existing:SF-2026-ARXIV-2605-26362:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26362:end -->
<!-- delta:SF-2026-ARXIV-2605-26362:start -->Finally, we show that these mechanistic patterns generalize beyond single-hop graphs to multi-hop and tabular settings, enabling effective hallucination detection across structured knowledge formats.<!-- delta:SF-2026-ARXIV-2605-26362:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-26362:end -->

<!-- books-review:SF-2026-ARXIV-2605-26379:start -->
<!-- existing:SF-2026-ARXIV-2605-26379:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前主干=['本章要回答的问题', '从三个容易混淆的对象开始', 'Video generation', 'Predictive environment model', 'Controllable world model', '在谈 State 之前，先声明预测 Channel', '为什么旧的 Simulator 仍然合理', '演进路线']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26379:end -->
<!-- delta:SF-2026-ARXIV-2605-26379:start -->We further prove an approximate identifiability result where the guarantee degrades gracefully, and show that linear, orthogonal identifiability enables optimal latent-space planning.<!-- delta:SF-2026-ARXIV-2605-26379:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26379:end -->

<!-- books-review:SF-2026-ARXIV-2605-26384:start -->
<!-- existing:SF-2026-ARXIV-2605-26384:start -->已顺读 `books/part-06-ai-infrastructure/63-gpu-scheduler.md` 及相邻章节 ['books/part-06-ai-infrastructure/62-gateway.md', 'books/part-06-ai-infrastructure/64-volcano.md']；当前主干=['本章要回答的问题', 'GPU 不是同质标量', '为什么调度会成为 AI 平台的核心问题', 'Filter、Score 与 Bind', '从 Pod Placement 到 Workload Snapshot', 'Fragmentation 为什么会发生', 'Gang、Queue 与 Fairness', 'GPU Sharing 的语义不同']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26384:end -->
<!-- delta:SF-2026-ARXIV-2605-26384:start -->GridPilot is released as open source and serves as a proof of concept that MW-scale AI/HPC demand can be engineered as controllable, grid-responsive flexibility by design.<!-- delta:SF-2026-ARXIV-2605-26384:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26384:end -->

<!-- books-review:SF-2026-ARXIV-2605-26403:start -->
<!-- existing:SF-2026-ARXIV-2605-26403:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 及相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前主干=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-26403:end -->
<!-- delta:SF-2026-ARXIV-2605-26403:start -->A long-standing goal of the research community is to develop highly interactive LLM-based dialogue agents.<!-- delta:SF-2026-ARXIV-2605-26403:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-26403:end -->

<!-- books-review:SF-2026-ARXIV-2605-26418:start -->
<!-- existing:SF-2026-ARXIV-2605-26418:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/63-gpu-scheduler.md` 与相邻章节 ['books/part-06-ai-infrastructure/62-gateway.md', 'books/part-06-ai-infrastructure/64-volcano.md']。当前命题：本章从异构资源、Filter/Score/Bind、fragmentation、gang/fairness 到 sharing 语义拥有 GPU 控制面；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=f44097493dfbe426ed1dadf2e27d3f87e14068d7f9d96027f8fa7c8a51511b45。<!-- existing:SF-2026-ARXIV-2605-26418:end -->
<!-- delta:SF-2026-ARXIV-2605-26418:start -->resource-control evidence must compare learned policies with calibrated rule baselines under matched workload, reward, seed and SLO contracts<!-- delta:SF-2026-ARXIV-2605-26418:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26418:end -->

<!-- books-review:SF-2026-ARXIV-2605-26433:start -->
<!-- existing:SF-2026-ARXIV-2605-26433:start -->Ch72 已将 hidden-state/representation release 视为独立隐私边界；本 family 的具体攻击结果加强风险证据，但不改变既有 owner 或 release contract。 owner_sha256=8d84c9f26ab04bab104ed93d45a226305008a7bb73f8afcba0b6271b14db0647。<!-- existing:SF-2026-ARXIV-2605-26433:end -->
<!-- delta:SF-2026-ARXIV-2605-26433:start -->derived hidden-state vectors become separately governed privacy artifacts because protection of one exported representation does not protect other pooled representations<!-- delta:SF-2026-ARXIV-2605-26433:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26433:end -->

<!-- books-review:SF-2026-ARXIV-2605-26440:start -->
<!-- existing:SF-2026-ARXIV-2605-26440:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L238 (H2: 第二个不变量：评估结论总是相对于分布)` 及相邻章节后，现有命题为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-26440:end -->
<!-- delta:SF-2026-ARXIV-2605-26440:start -->Exact-v1 的 source-specific delta 是：To leverage this potential, we introduce Conv-to-Bench , a multi-stage framework (Figure 1 ) designed to automatically transform these multi-turn dialogues into structured and verifiable requirements checklists. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-26440:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-26440:end -->

<!-- books-review:SF-2026-ARXIV-2605-26444:start -->
<!-- existing:SF-2026-ARXIV-2605-26444:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L196 (H2: Verify Length 不是孤立的固定超参数)` 及相邻章节后，现有命题为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-26444:end -->
<!-- delta:SF-2026-ARXIV-2605-26444:start -->Exact-v1 的 source-specific delta 是：We propose NanoSpec, a novel training-free approach that breaks this trade-off by dynamically constructing a minimalist, context-aware active vocabulary for each generation step. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-26444:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-26444:end -->

<!-- books-review:SF-2026-ARXIV-2605-26457:start -->
<!-- existing:SF-2026-ARXIV-2605-26457:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-26457:end -->
<!-- delta:SF-2026-ARXIV-2605-26457:start -->formal-spec generation is evaluated by executable official and adversarial tests, separating machine-checked syntax from fidelity to user intent and exposing LLM-judge misses<!-- delta:SF-2026-ARXIV-2605-26457:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26457:end -->

<!-- books-review:SF-2026-ARXIV-2605-26461:start -->
<!-- existing:SF-2026-ARXIV-2605-26461:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=fac898c122773aa03f4f0b32ec16167e145a3f8099a3513738731edf1c46ce0a。<!-- existing:SF-2026-ARXIV-2605-26461:end -->
<!-- delta:SF-2026-ARXIV-2605-26461:start -->GPU sharing needs fault-domain ownership: MMU isolation contains address faults while runtime recovery reconstitutes MPS clients after fatal SM faults<!-- delta:SF-2026-ARXIV-2605-26461:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26461:end -->

<!-- books-review:SF-2026-ARXIV-2605-26485:start -->
<!-- existing:SF-2026-ARXIV-2605-26485:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-26485:end -->
<!-- delta:SF-2026-ARXIV-2605-26485:start -->streaming evaluation must bind online event time, response windows, interruption state and native inference rather than offline QA.<!-- delta:SF-2026-ARXIV-2605-26485:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26485:end -->

<!-- books-review:SF-2026-ARXIV-2605-26497:start -->
<!-- existing:SF-2026-ARXIV-2605-26497:start -->Ch72 已以 permission graph、deterministic authorizer 与 provenance-bound authority 覆盖该类授权约束；本 family 未引入新的控制权归属。 owner_sha256=8d84c9f26ab04bab104ed93d45a226305008a7bb73f8afcba0b6271b14db0647。<!-- existing:SF-2026-ARXIV-2605-26497:end -->
<!-- delta:SF-2026-ARXIV-2605-26497:start -->authorization is checked against parameter provenance by comparing clean-intent and executed information-flow graphs.<!-- delta:SF-2026-ARXIV-2605-26497:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26497:end -->

<!-- books-review:SF-2026-ARXIV-2605-26508:start -->
<!-- existing:SF-2026-ARXIV-2605-26508:start -->Ch78 已要求 effect-time admission、safe default 与不可消耗的风险预算；论文机制是既有 Tool Contract 的实例，不形成新长期分支。 owner_sha256=0ea47f751768a5538765ce13b887215888f5e4d6ab2e39a40a2dc9a0ea83659c。<!-- existing:SF-2026-ARXIV-2605-26508:end -->
<!-- delta:SF-2026-ARXIV-2605-26508:start -->side-effecting tool calls gain a pre-action counterfactual risk budget, fixed safe default and underwriting boundary rather than relying on post-hoc liability review<!-- delta:SF-2026-ARXIV-2605-26508:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26508:end -->

<!-- books-review:SF-2026-ARXIV-2605-26521:start -->
<!-- existing:SF-2026-ARXIV-2605-26521:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=a5b996a7a312f9a4f940d3b430013e67417d27afdd4f1d8a37d8250fbdbb009f。<!-- existing:SF-2026-ARXIV-2605-26521:end -->
<!-- delta:SF-2026-ARXIV-2605-26521:start -->workflow testing gains structural obligations for agents, allowed/restricted tools and delegation edges, separate from task success.<!-- delta:SF-2026-ARXIV-2605-26521:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26521:end -->

<!-- books-review:SF-2026-ARXIV-2605-26542:start -->
<!-- existing:SF-2026-ARXIV-2605-26542:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=8d84c9f26ab04bab104ed93d45a226305008a7bb73f8afcba0b6271b14db0647。<!-- existing:SF-2026-ARXIV-2605-26542:end -->
<!-- delta:SF-2026-ARXIV-2605-26542:start -->tool-chain authority becomes value-scoped and monotonically attenuated, closing permission laundering across locally legal calls.<!-- delta:SF-2026-ARXIV-2605-26542:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26542:end -->

<!-- books-review:SF-2026-ARXIV-2605-26558:start -->
<!-- existing:SF-2026-ARXIV-2605-26558:start -->独立 reviewer 顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']。当前命题：本章拥有 proposal、target verification、accept/rollback 与 exactness 边界，而不是一般采样质量；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=29253f601a2c5240207a3ab0f355472926a5ef5163f77ce349c3d94de1d116bf。<!-- existing:SF-2026-ARXIV-2605-26558:end -->
<!-- delta:SF-2026-ARXIV-2605-26558:start -->edge self-speculation couples salience-selected draft state, full-precision verification and a format-conversion hardware path.<!-- delta:SF-2026-ARXIV-2605-26558:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26558:end -->

<!-- books-review:SF-2026-ARXIV-2605-26563:start -->
<!-- existing:SF-2026-ARXIV-2605-26563:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节 ['books/part-06-ai-infrastructure/68-logging.md', 'books/part-06-ai-infrastructure/70-cost.md']。当前命题：本章拥有跨组件 correlation、causal boundary、采样与 replay identity，不替代日志或指标 owner；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=40fdd931192eb4c937a1d81d3b0bed7e233637b085747f8a54806041da2346ff。<!-- existing:SF-2026-ARXIV-2605-26563:end -->
<!-- delta:SF-2026-ARXIV-2605-26563:start -->agent trajectories become diagnosable evidence when prior failure hypotheses, semantic saliency and an investigator agent preserve step-level failure localization<!-- delta:SF-2026-ARXIV-2605-26563:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26563:end -->

<!-- books-review:SF-2026-ARXIV-2605-26574:start -->
<!-- existing:SF-2026-ARXIV-2605-26574:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-26574:end -->
<!-- delta:SF-2026-ARXIV-2605-26574:start -->fine-tuning admission can use gradient spectral entropy as a backdoor sensor, but the filter remains attack- and module-dependent rather than a proof of clean data<!-- delta:SF-2026-ARXIV-2605-26574:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26574:end -->

<!-- books-review:SF-2026-ARXIV-2605-26606:start -->
<!-- existing:SF-2026-ARXIV-2605-26606:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前命题：本章拥有组内相对 advantage、credit assignment、reward/importance weighting 与优化稳定性边界；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7。<!-- existing:SF-2026-ARXIV-2605-26606:end -->
<!-- delta:SF-2026-ARXIV-2605-26606:start -->on-policy rollout budget is allocated from current-policy reward variance instead of uniformly across prompts.<!-- delta:SF-2026-ARXIV-2605-26606:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26606:end -->

<!-- books-review:SF-2026-ARXIV-2605-26667:start -->
<!-- existing:SF-2026-ARXIV-2605-26667:start -->Ch77 已沿 construction/retrieval 以及 extraction/storage/retrieval/answer 四阶段诊断 Memory；本 family 的评测切片没有改变该生命周期 contract。 owner_sha256=6943bc417b13de08760b63c2a8e2b0847c9e50e3ff294dfa15c57359c1db0492。<!-- existing:SF-2026-ARXIV-2605-26667:end -->
<!-- delta:SF-2026-ARXIV-2605-26667:start -->memory evaluation decomposes summary, storage and retrieval failures instead of treating memory as one black-box accuracy score.<!-- delta:SF-2026-ARXIV-2605-26667:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26667:end -->

<!-- books-review:SF-2026-ARXIV-2605-26684:start -->
<!-- existing:SF-2026-ARXIV-2605-26684:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前命题：本章拥有组内相对 advantage、credit assignment、reward/importance weighting 与优化稳定性边界；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7。<!-- existing:SF-2026-ARXIV-2605-26684:end -->
<!-- delta:SF-2026-ARXIV-2605-26684:start -->agentic RL credit moves from whole trajectories to an aggregated state-transition graph so shared prefixes and divergent actions receive different advantages<!-- delta:SF-2026-ARXIV-2605-26684:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26684:end -->

<!-- books-review:SF-2026-ARXIV-2605-26691:start -->
<!-- existing:SF-2026-ARXIV-2605-26691:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前命题：本章以 Tool Contract、proposal/admission、side-effect class、retry/idempotency 与 observation trust 拥有动作边界；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9。<!-- existing:SF-2026-ARXIV-2605-26691:end -->
<!-- delta:SF-2026-ARXIV-2605-26691:start -->tool-use training must assign asymmetric risk to failed, unnecessary and beneficial calls instead of rewarding tool invocation whenever the final answer succeeds<!-- delta:SF-2026-ARXIV-2605-26691:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26691:end -->

<!-- books-review:SF-2026-ARXIV-2605-26720:start -->
<!-- existing:SF-2026-ARXIV-2605-26720:start -->独立 reviewer 顺读 `books/part-07-agent/80-reflection.md` 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']。当前命题：本章拥有执行反馈、诊断、修复提议与再次验证的闭环，不允许模型自评直接成为 commit authority；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。<!-- existing:SF-2026-ARXIV-2605-26720:end -->
<!-- delta:SF-2026-ARXIV-2605-26720:start -->execution feedback is first converted into an explicit plan/no-plan decision and attributed by component before an agent edits a CUDA kernel<!-- delta:SF-2026-ARXIV-2605-26720:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26720:end -->

<!-- books-review:SF-2026-ARXIV-2605-26730:start -->
<!-- existing:SF-2026-ARXIV-2605-26730:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-26730:end -->
<!-- delta:SF-2026-ARXIV-2605-26730:start -->peer-review evaluation must preserve multiple review dimensions and disagreement rather than collapse reviewer quality into one aggregate judge score<!-- delta:SF-2026-ARXIV-2605-26730:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26730:end -->

<!-- books-review:SF-2026-ARXIV-2605-26731:start -->
<!-- existing:SF-2026-ARXIV-2605-26731:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-26731:end -->
<!-- delta:SF-2026-ARXIV-2605-26731:start -->agent harness configuration is an evaluation treatment variable whose optimum is model-specific, not monotone in capability tier.<!-- delta:SF-2026-ARXIV-2605-26731:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26731:end -->

<!-- books-review:SF-2026-ARXIV-2605-26754:start -->
<!-- existing:SF-2026-ARXIV-2605-26754:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=8d84c9f26ab04bab104ed93d45a226305008a7bb73f8afcba0b6271b14db0647。<!-- existing:SF-2026-ARXIV-2605-26754:end -->
<!-- delta:SF-2026-ARXIV-2605-26754:start -->RAG poisoning control removes untrusted prose from the synthesis principal and passes only audited claims across the boundary.<!-- delta:SF-2026-ARXIV-2605-26754:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26754:end -->

<!-- books-review:SF-2026-ARXIV-2605-26778:start -->
<!-- existing:SF-2026-ARXIV-2605-26778:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=87e328782912c590e2ce992aebd3701a601c7a9d63a696f24048ad9d78f81c27。<!-- existing:SF-2026-ARXIV-2605-26778:end -->
<!-- delta:SF-2026-ARXIV-2605-26778:start -->grounded output must distinguish retrieved-context causation from coincident parametric-memory recall.<!-- delta:SF-2026-ARXIV-2605-26778:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-26778:end -->

<!-- books-review:SF-2026-ARXIV-2605-27091:start -->
<!-- existing:SF-2026-ARXIV-2605-27091:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-27091:end -->
<!-- delta:SF-2026-ARXIV-2605-27091:start -->In this paper, we introduce MiRD, a two-stage framework that decomposes overall miscoverage into sampling failure and conditional selection failure.<!-- delta:SF-2026-ARXIV-2605-27091:end --> Author decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-27091:end -->

<!-- books-review:SF-2026-ARXIV-2605-27220:start -->
<!-- existing:SF-2026-ARXIV-2605-27220:start -->Ch76 已拥有 sufficiency gate 与 typed retrieval controller，先判证据充分性再路由检索；本 family 不再提供新的 canonical mechanism。 owner_sha256=87e328782912c590e2ce992aebd3701a601c7a9d63a696f24048ad9d78f81c27。<!-- existing:SF-2026-ARXIV-2605-27220:end -->
<!-- delta:SF-2026-ARXIV-2605-27220:start -->production RAG routes augmentation after measuring retrieval sufficiency and traces post-retrieval cascades instead of applying augmentation globally.<!-- delta:SF-2026-ARXIV-2605-27220:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27220:end -->

<!-- books-review:SF-2026-ARXIV-2605-27292:start -->
<!-- existing:SF-2026-ARXIV-2605-27292:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-27292:end -->
<!-- delta:SF-2026-ARXIV-2605-27292:start -->one-run privacy audits need detectable, low-interference and diverse canaries rather than interchangeable probes.<!-- delta:SF-2026-ARXIV-2605-27292:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27292:end -->

<!-- books-review:SF-2026-ARXIV-2605-27328:start -->
<!-- existing:SF-2026-ARXIV-2605-27328:start -->Ch84 已将 self-evolution 定义为 supply-chain revision，并以 fast/slow path、release gate 与 rollback 管理能力变化；本 family 属于既有覆盖。 owner_sha256=007d5f3118e5050530972c51e8c223c5ad7717c18b78632e4fdc828c91de8c8a。<!-- existing:SF-2026-ARXIV-2605-27328:end -->
<!-- delta:SF-2026-ARXIV-2605-27328:start -->self-modifying agent harnesses require versioned executable artifacts, capability lifecycle state, governance approval and rollback instead of ungoverned prompt/code mutation<!-- delta:SF-2026-ARXIV-2605-27328:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27328:end -->

<!-- books-review:SF-2026-ARXIV-2605-27333:start -->
<!-- existing:SF-2026-ARXIV-2605-27333:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-27333:end -->
<!-- delta:SF-2026-ARXIV-2605-27333:start -->query and tool monitors form an inline lifecycle cascade whose fired evidence changes the next prompt while an external gate retains stop authority<!-- delta:SF-2026-ARXIV-2605-27333:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27333:end -->

<!-- books-review:SF-2026-ARXIV-2605-27361:start -->
<!-- existing:SF-2026-ARXIV-2605-27361:start -->独立 reviewer 顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']。当前命题：本章从 offline ingestion 到 online retrieval、sufficient context、freshness/deletion 与 hallucination 边界拥有检索证据链；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=3986f4307ffd57af8ace87d5c720982b992e07f247a91b16d73a39d83a8917a2。<!-- existing:SF-2026-ARXIV-2605-27361:end -->
<!-- delta:SF-2026-ARXIV-2605-27361:start -->retrieval configuration becomes a per-query control decision over the whole pipeline after workload-specific characterization and Pareto pruning<!-- delta:SF-2026-ARXIV-2605-27361:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27361:end -->

<!-- books-review:SF-2026-ARXIV-2605-27366:start -->
<!-- existing:SF-2026-ARXIV-2605-27366:start -->独立 reviewer 顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。当前命题：本章从 Agent Definition、Run Identity、三个平面、Runtime State Machine 到 release/rollback 拥有长任务生命周期；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-27366:end -->
<!-- delta:SF-2026-ARXIV-2605-27366:start -->agent skills need creation, memory, selection, evaluation and replacement as one governed lifecycle rather than an append-only prompt library<!-- delta:SF-2026-ARXIV-2605-27366:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27366:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260527-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260527 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260527-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260527-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=59；selected=3；all others retain completed reviews | passed |
| SA-20260527-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=569；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260527/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260527/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-27.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
