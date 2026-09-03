# Daily Research — 2026-05-01

**Research Date:** 2026-05-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-04-30 09:00:00 ～ 2026-05-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 556 个注册 arXiv identity，冻结 63 个 Source Family；pre-denominator closure=493，withdrawn pre-denominator=0。19 个旧候选被迁回正确 owner day，0 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-01 |
| Window End | 2026-05-01 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260501-CREATED-41933bde4dd8ca62 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-04-30T09:00:00+08:00 | 2026-05-01T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 556 | SF-2026-ARXIV-2604-26963;SF-2026-ARXIV-2604-26968;SF-2026-ARXIV-2604-26997;SF-2026-ARXIV-2604-27003;SF-2026-ARXIV-2604-27032;SF-2026-ARXIV-2604-27039;SF-2026-ARXIV-2604-27045;SF-2026-ARXIV-2604-27083;SF-2026-ARXIV-2604-27085;SF-2026-ARXIV-2604-27089;SF-2026-ARXIV-2604-27151;SF-2026-ARXIV-2604-27202;SF-2026-ARXIV-2604-27221;SF-2026-ARXIV-2604-27233;SF-2026-ARXIV-2604-27238;SF-2026-ARXIV-2604-27249;SF-2026-ARXIV-2604-27251;SF-2026-ARXIV-2604-27267;SF-2026-ARXIV-2604-27283;SF-2026-ARXIV-2604-27289;SF-2026-ARXIV-2604-27292;SF-2026-ARXIV-2604-27306;SF-2026-ARXIV-2604-27309;SF-2026-ARXIV-2604-27351;SF-2026-ARXIV-2604-27358;SF-2026-ARXIV-2604-27393;SF-2026-ARXIV-2604-27396;SF-2026-ARXIV-2604-27405;SF-2026-ARXIV-2604-27419;SF-2026-ARXIV-2604-27426;SF-2026-ARXIV-2604-27467;SF-2026-ARXIV-2604-27486;SF-2026-ARXIV-2604-27488;SF-2026-ARXIV-2604-27536;SF-2026-ARXIV-2604-27586;SF-2026-ARXIV-2604-27637;SF-2026-ARXIV-2604-27660;SF-2026-ARXIV-2604-27695;SF-2026-ARXIV-2604-27707;SF-2026-ARXIV-2604-27711;SF-2026-ARXIV-2604-27776;SF-2026-ARXIV-2604-27781;SF-2026-ARXIV-2604-27789;SF-2026-ARXIV-2604-27792;SF-2026-ARXIV-2604-27819;SF-2026-ARXIV-2604-27844;SF-2026-ARXIV-2604-27855;SF-2026-ARXIV-2604-27861;SF-2026-ARXIV-2604-27878;SF-2026-ARXIV-2604-27891;SF-2026-ARXIV-2604-27906;SF-2026-ARXIV-2604-28056;SF-2026-ARXIV-2604-28123;SF-2026-ARXIV-2604-28129;SF-2026-ARXIV-2604-28138;SF-2026-ARXIV-2604-28139;SF-2026-ARXIV-2604-28157;SF-2026-ARXIV-2604-28158;SF-2026-ARXIV-2604-28175;SF-2026-ARXIV-2604-28181;SF-2026-ARXIV-2604-28182;SF-2026-ARXIV-2604-28190;SF-2026-ARXIV-2604-28196 | created-day pages=closed; OAI category sets=closed; direct same-day OAI=405 | 2026-05-01T09:00:00+08:00 | coverage:SRC-ARXIV:20260501 | — |

<!-- coverage:SRC-ARXIV:20260501:start -->全量 raw inventory=556；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260501:end -->

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
| SF-2026-ARXIV-2604-26963 | arXiv:2604.26963v1 | paper-v1:2604.26963 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-26963 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26963 | no |
| SF-2026-ARXIV-2604-26968 | arXiv:2604.26968v1 | paper-v1:2604.26968 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-26968 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26968 | no |
| SF-2026-ARXIV-2604-26997 | arXiv:2604.26997v1 | paper-v1:2604.26997 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26997 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26997 | no |
| SF-2026-ARXIV-2604-27003 | arXiv:2604.27003v1 | paper-v1:2604.27003 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27003 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27003 | no |
| SF-2026-ARXIV-2604-27032 | arXiv:2604.27032v1 | paper-v1:2604.27032 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27032 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27032 | no |
| SF-2026-ARXIV-2604-27039 | arXiv:2604.27039v1 | paper-v1:2604.27039 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27039 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27039 | no |
| SF-2026-ARXIV-2604-27045 | arXiv:2604.27045v1 | paper-v1:2604.27045 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27045 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27045 | no |
| SF-2026-ARXIV-2604-27083 | arXiv:2604.27083v1 | paper-v1:2604.27083 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27083 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27083 | no |
| SF-2026-ARXIV-2604-27085 | arXiv:2604.27085v1 | paper-v1:2604.27085 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27085 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27085 | no |
| SF-2026-ARXIV-2604-27089 | arXiv:2604.27089v1 | paper-v1:2604.27089 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27089 | self | — | new_in_window | TRAIN-TENSOR-PARALLEL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27089 | no |
| SF-2026-ARXIV-2604-27151 | arXiv:2604.27151v1 | paper-v1:2604.27151 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27151 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27151 | no |
| SF-2026-ARXIV-2604-27202 | arXiv:2604.27202v1 | paper-v1:2604.27202 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27202 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27202 | no |
| SF-2026-ARXIV-2604-27221 | arXiv:2604.27221v1 | paper-v1:2604.27221 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27221 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27221 | no |
| SF-2026-ARXIV-2604-27233 | arXiv:2604.27233v1 | paper-v1:2604.27233 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27233 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27233 | no |
| SF-2026-ARXIV-2604-27238 | arXiv:2604.27238v1 | paper-v1:2604.27238 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27238 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27238 | no |
| SF-2026-ARXIV-2604-27249 | arXiv:2604.27249v1 | paper-v1:2604.27249 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27249 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27249 | no |
| SF-2026-ARXIV-2604-27251 | arXiv:2604.27251v1 | paper-v1:2604.27251 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27251 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27251 | no |
| SF-2026-ARXIV-2604-27267 | arXiv:2604.27267v1 | paper-v1:2604.27267 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27267 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27267 | no |
| SF-2026-ARXIV-2604-27283 | arXiv:2604.27283v1 | paper-v1:2604.27283 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27283 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27283 | no |
| SF-2026-ARXIV-2604-27289 | arXiv:2604.27289v1 | paper-v1:2604.27289 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27289 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27289 | yes |
| SF-2026-ARXIV-2604-27292 | arXiv:2604.27292v1 | paper-v1:2604.27292 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27292 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27292 | yes |
| SF-2026-ARXIV-2604-27306 | arXiv:2604.27306v1 | paper-v1:2604.27306 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27306 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2604-27306 | yes |
| SF-2026-ARXIV-2604-27309 | arXiv:2604.27309v1 | paper-v1:2604.27309 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27309 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27309 | yes |
| SF-2026-ARXIV-2604-27351 | arXiv:2604.27351v1 | paper-v1:2604.27351 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27351 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27351 | yes |
| SF-2026-ARXIV-2604-27358 | arXiv:2604.27358v1 | paper-v1:2604.27358 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27358 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2604-27358 | yes |
| SF-2026-ARXIV-2604-27393 | arXiv:2604.27393v1 | paper-v1:2604.27393 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27393 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27393 | yes |
| SF-2026-ARXIV-2604-27396 | arXiv:2604.27396v1 | paper-v1:2604.27396 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27396 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27396 | yes |
| SF-2026-ARXIV-2604-27405 | arXiv:2604.27405v1 | paper-v1:2604.27405 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27405 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27405 | yes |
| SF-2026-ARXIV-2604-27419 | arXiv:2604.27419v1 | paper-v1:2604.27419 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27419 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27419 | yes |
| SF-2026-ARXIV-2604-27426 | arXiv:2604.27426v1 | paper-v1:2604.27426 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27426 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-27426 | yes |
| SF-2026-ARXIV-2604-27467 | arXiv:2604.27467v1 | paper-v1:2604.27467 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27467 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27467 | yes |
| SF-2026-ARXIV-2604-27486 | arXiv:2604.27486v1 | paper-v1:2604.27486 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27486 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2604-27486 | yes |
| SF-2026-ARXIV-2604-27488 | arXiv:2604.27488v1 | paper-v1:2604.27488 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27488 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27488 | yes |
| SF-2026-ARXIV-2604-27536 | arXiv:2604.27536v1 | paper-v1:2604.27536 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27536 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2604-27536 | yes |
| SF-2026-ARXIV-2604-27586 | arXiv:2604.27586v1 | paper-v1:2604.27586 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27586 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2604-27586 | yes |
| SF-2026-ARXIV-2604-27637 | arXiv:2604.27637v1 | paper-v1:2604.27637 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27637 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27637 | yes |
| SF-2026-ARXIV-2604-27660 | arXiv:2604.27660v1 | paper-v1:2604.27660 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27660 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27660 | yes |
| SF-2026-ARXIV-2604-27695 | arXiv:2604.27695v1 | paper-v1:2604.27695 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27695 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27695 | yes |
| SF-2026-ARXIV-2604-27707 | arXiv:2604.27707v1 | paper-v1:2604.27707 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27707 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27707 | yes |
| SF-2026-ARXIV-2604-27711 | arXiv:2604.27711v1 | paper-v1:2604.27711 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27711 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27711 | yes |
| SF-2026-ARXIV-2604-27776 | arXiv:2604.27776v1 | paper-v1:2604.27776 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27776 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27776 | yes |
| SF-2026-ARXIV-2604-27781 | arXiv:2604.27781v1 | paper-v1:2604.27781 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27781 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27781 | yes |
| SF-2026-ARXIV-2604-27789 | arXiv:2604.27789v1 | paper-v1:2604.27789 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27789 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27789 | yes |
| SF-2026-ARXIV-2604-27792 | arXiv:2604.27792v1 | paper-v1:2604.27792 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27792 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27792 | yes |
| SF-2026-ARXIV-2604-27819 | arXiv:2604.27819v1 | paper-v1:2604.27819 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27819 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2604-27819 | yes |
| SF-2026-ARXIV-2604-27844 | arXiv:2604.27844v1 | paper-v1:2604.27844 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27844 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2604-27844 | yes |
| SF-2026-ARXIV-2604-27855 | arXiv:2604.27855v1 | paper-v1:2604.27855 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27855 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2604-27855 | yes |
| SF-2026-ARXIV-2604-27861 | arXiv:2604.27861v1 | paper-v1:2604.27861 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27861 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27861 | yes |
| SF-2026-ARXIV-2604-27878 | arXiv:2604.27878v1 | paper-v1:2604.27878 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27878 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27878 | yes |
| SF-2026-ARXIV-2604-27891 | arXiv:2604.27891v1 | paper-v1:2604.27891 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27891 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2604-27891 | yes |
| SF-2026-ARXIV-2604-27906 | arXiv:2604.27906v1 | paper-v1:2604.27906 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27906 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27906 | yes |
| SF-2026-ARXIV-2604-28056 | arXiv:2604.28056v1 | paper-v1:2604.28056 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28056 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28056 | yes |
| SF-2026-ARXIV-2604-28123 | arXiv:2604.28123v1 | paper-v1:2604.28123 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28123 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28123 | yes |
| SF-2026-ARXIV-2604-28129 | arXiv:2604.28129v1 | paper-v1:2604.28129 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28129 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-28129 | yes |
| SF-2026-ARXIV-2604-28138 | arXiv:2604.28138v1 | paper-v1:2604.28138 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28138 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2604-28138 | yes |
| SF-2026-ARXIV-2604-28139 | arXiv:2604.28139v1 | paper-v1:2604.28139 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28139 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28139 | yes |
| SF-2026-ARXIV-2604-28157 | arXiv:2604.28157v1 | paper-v1:2604.28157 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28157 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28157 | yes |
| SF-2026-ARXIV-2604-28158 | arXiv:2604.28158v1 | paper-v1:2604.28158 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28158 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28158 | yes |
| SF-2026-ARXIV-2604-28175 | arXiv:2604.28175v1 | paper-v1:2604.28175 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28175 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2604-28175 | yes |
| SF-2026-ARXIV-2604-28181 | arXiv:2604.28181v1 | paper-v1:2604.28181 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28181 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28181 | yes |
| SF-2026-ARXIV-2604-28182 | arXiv:2604.28182v1 | paper-v1:2604.28182 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28182 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28182 | yes |
| SF-2026-ARXIV-2604-28190 | arXiv:2604.28190v1 | paper-v1:2604.28190 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28190 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2604-28190 | yes |
| SF-2026-ARXIV-2604-28196 | arXiv:2604.28196v1 | paper-v1:2604.28196 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28196 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28196 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-26963 | RP-9d5aa77115302995 | deep | arXiv:2604.26963v1 | SRC-ARXIV@arXiv:2604.26963v1 | papers/2026/04/_sources/daily-20260415/exact-v1-bodies/2604.26963v1.html#S4.SS2 — exact-v1 § `4.2. Control Plane Design` | papers/2026/04/_sources/daily-20260415/exact-v1-bodies/2604.26963v1.html#S6.SS2 — exact-v1 § `6.2. Experimental Setup` | papers/2026/04/_sources/daily-20260415/exact-v1-bodies/2604.26963v1.html#S7 — exact-v1 § `7. Discussions` | papers/2026/04/_sources/daily-20260415/exact-v1-bodies/2604.26963v1.html#S5 — exact-v1 § `5. Implementation` ; https://arxiv.org/abs/2604.26963v1 | claim:SF-2026-ARXIV-2604-26963 | complete |
| SF-2026-ARXIV-2604-26968 | RP-e94ef7d4ee86653b | deep | arXiv:2604.26968v1 | SRC-ARXIV@arXiv:2604.26968v1 | arXiv:2604.26968v1 HTML — §V-B Analytical Projection Methodology; https://arxiv.org/html/2604.26968v1; papers/2026/04/_sources/daily-20260420/exact-v1-bodies/2604.26968v1.html; sha256:2621c6411a87ac19d269d99adc7ce613801df611b6c56d1906758317f49ae759 | arXiv:2604.26968v1 HTML — §V-D Projected Multi-Tier Performance; https://arxiv.org/html/2604.26968v1; papers/2026/04/_sources/daily-20260420/exact-v1-bodies/2604.26968v1.html; sha256:2621c6411a87ac19d269d99adc7ce613801df611b6c56d1906758317f49ae759 | arXiv:2604.26968v1 HTML — §VII Conclusion; https://arxiv.org/html/2604.26968v1; papers/2026/04/_sources/daily-20260420/exact-v1-bodies/2604.26968v1.html; sha256:2621c6411a87ac19d269d99adc7ce613801df611b6c56d1906758317f49ae759 | Not Disclosed — no public code/data artifact link in cached exact-v1 body papers/2026/04/_sources/daily-20260420/exact-v1-bodies/2604.26968v1.html | claim:SF-2026-ARXIV-2604-26968 | complete |
| SF-2026-ARXIV-2604-26997 | RP-4002e3527f8365a2 | deep | arXiv:2604.26997v1 | SRC-ARXIV@arXiv:2604.26997v1 | arXiv:2604.26997v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26997v1.html#exact-v1 independent HTML full read) | arXiv:2604.26997v1 §Evaluation — Evaluation Contract — II-D Gap Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26997v1.html#exact-v1 independent HTML full read) | arXiv:2604.26997v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VIII Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26997v1.html#exact-v1 independent HTML full read) | arXiv:2604.26997v1 §Artifact / Access — Artifact / Access — VII Reproducibility and Code Availability (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26997v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26997 | complete |
| SF-2026-ARXIV-2604-27003 | RP-8996759290181cfc | deep | arXiv:2604.27003v1 | SRC-ARXIV@arXiv:2604.27003v1 | arXiv:2604.27003v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27003v1.html#exact-v1 independent HTML full read) | arXiv:2604.27003v1 §Evaluation — Evaluation Contract — Appendix C Retrieval Frequency: Additional Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27003v1.html#exact-v1 independent HTML full read) | arXiv:2604.27003v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27003v1.html#exact-v1 independent HTML full read) | arXiv:2604.27003v1 §Artifact / Access — Artifact / Access — Appendix B Memory Content Examples (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27003v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27003 | complete |
| SF-2026-ARXIV-2604-27032 | RP-a364b6e746a75af1 | deep | arXiv:2604.27032v1 | SRC-ARXIV@arXiv:2604.27032v1 | arXiv:2604.27032v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27032v1.html#exact-v1 independent HTML full read) | arXiv:2604.27032v1 §Evaluation — Evaluation Contract — 5 Evaluation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27032v1.html#exact-v1 independent HTML full read) | arXiv:2604.27032v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Discussion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27032v1.html#exact-v1 independent HTML full read) | arXiv:2604.27032v1 §Artifact / Access — Artifact / Access — 4.1.1 Hardware and Software Stack (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27032v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27032 | complete |
| SF-2026-ARXIV-2604-27039 | RP-1e20a68a7ea243ac | deep | arXiv:2604.27039v1 | SRC-ARXIV@arXiv:2604.27039v1 | arXiv:2604.27039v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27039v1.html#exact-v1 independent HTML full read) | arXiv:2604.27039v1 §Evaluation — Evaluation Contract — Appendix A Additional Experimental Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27039v1.html#exact-v1 independent HTML full read) | arXiv:2604.27039v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27039v1.html#exact-v1 independent HTML full read) | arXiv:2604.27039v1 §Artifact / Access — Artifact / Access — Appendix A Additional Experimental Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27039v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27039 | complete |
| SF-2026-ARXIV-2604-27045 | RP-1aa2ace5044c2334 | deep | arXiv:2604.27045v1 | SRC-ARXIV@arXiv:2604.27045v1 | arXiv:2604.27045v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27045v1.html#exact-v1 independent HTML full read) | arXiv:2604.27045v1 §Evaluation — Method / Identity — 4.3 Multi-Dimensional Evaluation Framework (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27045v1.html#exact-v1 independent HTML full read) | arXiv:2604.27045v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6.3 Limitations and Future Directions (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27045v1.html#exact-v1 independent HTML full read) | arXiv:2604.27045v1 §Artifact / Access — Artifact / Access — Appendix B Sample Clinical Summary (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27045v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27045 | complete |
| SF-2026-ARXIV-2604-27083 | RP-0b4ea717a7ee1a73 | deep | arXiv:2604.27083v1 | SRC-ARXIV@arXiv:2604.27083v1 | arXiv:2604.27083v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27083v1.html#exact-v1 independent HTML full read) | arXiv:2604.27083v1 §Evaluation — Evaluation Contract — 4.1 Experimental Setting (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27083v1.html#exact-v1 independent HTML full read) | arXiv:2604.27083v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27083v1.html#exact-v1 independent HTML full read) | arXiv:2604.27083v1 §Artifact / Access — Artifact / Access — 2.1 A Unified View of Existing Paradigms (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27083v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27083 | complete |
| SF-2026-ARXIV-2604-27085 | RP-865ddb7d051f4377 | deep | arXiv:2604.27085v1 | SRC-ARXIV@arXiv:2604.27085v1 | arXiv:2604.27085v1 §Method / Identity — Artifact / Access — 4. Design and Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27085v1.html#exact-v1 independent HTML full read) | arXiv:2604.27085v1 §Evaluation — Evaluation Contract — Roofline analysis. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27085v1.html#exact-v1 independent HTML full read) | arXiv:2604.27085v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27085v1.html#exact-v1 independent HTML full read) | arXiv:2604.27085v1 §Artifact / Access — Artifact / Access — 4. Design and Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27085v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27085 | complete |
| SF-2026-ARXIV-2604-27089 | RP-1a4833832e468ac6 | deep | arXiv:2604.27089v1 | SRC-ARXIV@arXiv:2604.27089v1 | arXiv:2604.27089v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27089v1.html#exact-v1 independent HTML full read) | arXiv:2604.27089v1 §Evaluation — Evaluation Contract — 4 Evaluation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27089v1.html#exact-v1 independent HTML full read) | arXiv:2604.27089v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27089v1.html#exact-v1 independent HTML full read) | arXiv:2604.27089v1 §Artifact / Access — Artifact / Access — 4 Evaluation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27089v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27089 | complete |
| SF-2026-ARXIV-2604-27151 | RP-47d24d219977076d | deep | arXiv:2604.27151v1 | SRC-ARXIV@arXiv:2604.27151v1 | arXiv:2604.27151v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27151v1.html#exact-v1 independent HTML full read) | arXiv:2604.27151v1 §Evaluation — Evaluation Contract — Evaluation. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27151v1.html#exact-v1 independent HTML full read) | arXiv:2604.27151v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27151v1.html#exact-v1 independent HTML full read) | arXiv:2604.27151v1 §Artifact / Access — Artifact / Access — Appendix B ModernBERT Fine-tuning Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27151v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27151 | complete |
| SF-2026-ARXIV-2604-27202 | RP-1b22160bbfd52f00 | deep | arXiv:2604.27202v1 | SRC-ARXIV@arXiv:2604.27202v1 | arXiv:2604.27202v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27202v1.html#exact-v1 independent HTML full read) | arXiv:2604.27202v1 §Evaluation — Evaluation Contract — 6.1. Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27202v1.html#exact-v1 independent HTML full read) | arXiv:2604.27202v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 10.1. Threats to Validity (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27202v1.html#exact-v1 independent HTML full read) | arXiv:2604.27202v1 §Artifact / Access — Artifact / Access — Appendix A Ethical Considerations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27202v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27202 | complete |
| SF-2026-ARXIV-2604-27221 | RP-1fcc98fa26512257 | deep | arXiv:2604.27221v1 | SRC-ARXIV@arXiv:2604.27221v1 | arXiv:2604.27221v1 §Method / Identity — Artifact / Access — Implementation. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27221v1.html#exact-v1 independent HTML full read) | arXiv:2604.27221v1 §Evaluation — Evaluation Contract — XBench-DeepSearch results. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27221v1.html#exact-v1 independent HTML full read) | arXiv:2604.27221v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27221v1.html#exact-v1 independent HTML full read) | arXiv:2604.27221v1 §Artifact / Access — Artifact / Access — Implementation. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27221v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27221 | complete |
| SF-2026-ARXIV-2604-27233 | RP-de4faedef4f512c9 | deep | arXiv:2604.27233v1 | SRC-ARXIV@arXiv:2604.27233v1 | arXiv:2604.27233v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27233v1.html#exact-v1 independent HTML full read) | arXiv:2604.27233v1 §Evaluation — Evaluation Contract — 4 Results & Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27233v1.html#exact-v1 independent HTML full read) | arXiv:2604.27233v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27233v1.html#exact-v1 independent HTML full read) | arXiv:2604.27233v1 §Artifact / Access — Artifact / Access — 4.4.1 Model Comparison (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27233v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27233 | complete |
| SF-2026-ARXIV-2604-27238 | RP-73c126f40c7f4273 | deep | arXiv:2604.27238v1 | SRC-ARXIV@arXiv:2604.27238v1 | arXiv:2604.27238v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27238v1.html#exact-v1 independent HTML full read) | arXiv:2604.27238v1 §Evaluation — Evaluation Contract — V-A Datasets and Preprocessing (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27238v1.html#exact-v1 independent HTML full read) | arXiv:2604.27238v1 §Scope and Limitations — Evidence Proves / Does Not Prove — III Threat Model (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27238v1.html#exact-v1 independent HTML full read) | arXiv:2604.27238v1 §Artifact / Access — Artifact / Access — Abstract (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27238v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27238 | complete |
| SF-2026-ARXIV-2604-27249 | RP-f1d769d234711f47 | deep | arXiv:2604.27249v1 | SRC-ARXIV@arXiv:2604.27249v1 | https://arxiv.org/html/2604.27249v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.27249v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.27249v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.27249v1 ; https://arxiv.org/html/2604.27249v1 | claim:SF-2026-ARXIV-2604-27249 | complete |
| SF-2026-ARXIV-2604-27251 | RP-77ba0903562b9b71 | deep | arXiv:2604.27251v1 | SRC-ARXIV@arXiv:2604.27251v1 | arXiv:2604.27251v1 §Method / Identity — Artifact / Access — Appendix A Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27251v1.html#exact-v1 independent HTML full read) | arXiv:2604.27251v1 §Evaluation — Evaluation Contract — 5.3 Mechanistic Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27251v1.html#exact-v1 independent HTML full read) | arXiv:2604.27251v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27251v1.html#exact-v1 independent HTML full read) | arXiv:2604.27251v1 §Artifact / Access — Artifact / Access — Appendix A Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27251v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27251 | complete |
| SF-2026-ARXIV-2604-27267 | RP-f6a2ea745927d675 | deep | arXiv:2604.27267v1 | SRC-ARXIV@arXiv:2604.27267v1 | arXiv:2604.27267v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27267v1.html#exact-v1 independent HTML full read) | arXiv:2604.27267v1 §Evaluation — Evaluation Contract — IV-A STRIDE Per-Interaction Threat Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27267v1.html#exact-v1 independent HTML full read) | arXiv:2604.27267v1 §Scope and Limitations — Evidence Proves / Does Not Prove — IV-A STRIDE Per-Interaction Threat Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27267v1.html#exact-v1 independent HTML full read) | arXiv:2604.27267v1 §Artifact / Access — Artifact / Access — III-B System Modeling (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27267v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27267 | complete |
| SF-2026-ARXIV-2604-27283 | RP-bcc9bff3f7b424c1 | deep | arXiv:2604.27283v1 | SRC-ARXIV@arXiv:2604.27283v1 | arXiv:2604.27283v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27283v1.html#exact-v1 independent HTML full read) | arXiv:2604.27283v1 §Evaluation — Evaluation Contract — 3.1 Evaluation boundary (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27283v1.html#exact-v1 independent HTML full read) | arXiv:2604.27283v1 §Scope and Limitations — Method / Identity — 4.2 How RSCB-MC differs from RAG and knowledge-boundary methods (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27283v1.html#exact-v1 independent HTML full read) | arXiv:2604.27283v1 §Artifact / Access — Artifact / Access — 3.2 Benchmark artifacts (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.27283v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-27283 | complete |
| SF-2026-ARXIV-2604-27289 | RP-8d01168c396cf39f | deep | arXiv:2604.27289v1 | SRC-ARXIV@arXiv:2604.27289v1 | https://arxiv.org/html/2604.27289v1 — §2.2-3.3 event types, governance operator and coinductive safety predicate; §8 mechanization; §9 verified interpreter specification | https://arxiv.org/html/2604.27289v1 — §8.3-8.5 36 Coq modules/454 results/zero admitted lemmas; §9 property-based conformance against BEAM runtime | https://arxiv.org/html/2604.27289v1 — §12 Limitations：formalization is system-specific; two named results remain paper proofs; proof covers the modeled effect boundary and does not establish policy correctness or arbitrary runtime behavior | Not Disclosed — public Coq artifact is declared in exact-v1, but this review did not independently rebuild it | claim:SF-2026-ARXIV-2604-27289 | complete |
| SF-2026-ARXIV-2604-27292 | RP-bc20b1a8b32d3636 | deep | arXiv:2604.27292v1 | SRC-ARXIV@arXiv:2604.27292v1 | https://arxiv.org/html/2604.27292v1 — §2-4 expressiveness/governance boundaries, Rice-theorem boundary and coterminous governance; §5-7 behavioral comparison and execution-pipeline consequence | https://arxiv.org/html/2604.27292v1 — §4 gives the testable structural criterion; formal claims defer to the companion Coq development rather than an independent empirical benchmark | https://arxiv.org/html/2604.27292v1 — §9 Limitations：scope is effects, existing frameworks may require re-architecture, structural coverage does not prove policy correctness, and restricted languages trade expressiveness for decidability | Not Disclosed — companion Coq repository is linked; this conceptual paper has no separate empirical artifact | claim:SF-2026-ARXIV-2604-27292 | complete |
| SF-2026-ARXIV-2604-27306 | RP-7a624eff73754d6e | deep | arXiv:2604.27306v1 | SRC-ARXIV@arXiv:2604.27306v1 | https://arxiv.org/html/2604.27306v1 — §3-4 nugget schema, lifecycle and retrieval pipeline | https://arxiv.org/html/2604.27306v1 — §5 three QA datasets, maintenance/update evaluation and ablations | https://arxiv.org/html/2604.27306v1 — §6/§7 selected QA corpora and author metrics do not prove a universal source-authority policy | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27306 | complete |
| SF-2026-ARXIV-2604-27309 | RP-f4f235421b995920 | deep | arXiv:2604.27309v1 | SRC-ARXIV@arXiv:2604.27309v1 | https://arxiv.org/html/2604.27309v1 — §5.1-5.8 governance architecture, controlled experimentation, monitoring and cost | https://arxiv.org/html/2604.27309v1 — §2.1-2.6 seven versions, clinician rubrics, live feedback and technical performance | https://arxiv.org/html/2604.27309v1 — §3.6 single product/domain, observational feedback and short deployment window | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27309 | complete |
| SF-2026-ARXIV-2604-27351 | RP-2d2750371f17d19e | deep | arXiv:2604.27351v1 | SRC-ARXIV@arXiv:2604.27351v1 | https://arxiv.org/html/2604.27351v1 — §3 heterogeneous model collaboration and typed tool interface | https://arxiv.org/html/2604.27351v1 — §4 scientific task evaluations and collaboration ablations | https://arxiv.org/html/2604.27351v1 — §5 selected scientific models/tasks do not establish a universal planner or tool ontology | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27351 | complete |
| SF-2026-ARXIV-2604-27358 | RP-68859682ff71a1b1 | deep | arXiv:2604.27358v1 | SRC-ARXIV@arXiv:2604.27358v1 | https://arxiv.org/html/2604.27358v1 — §3-5 bilevel delegation objective, safety monotonicity and responsibility propagation | https://arxiv.org/html/2604.27358v1 — §5 formal convergence/safety analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 explicitly leaves empirical validation to future work; formal assumptions do not prove deployable runtime safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27358 | complete |
| SF-2026-ARXIV-2604-27393 | RP-e28a66921b9aa983 | deep | arXiv:2604.27393v1 | SRC-ARXIV@arXiv:2604.27393v1 | https://arxiv.org/html/2604.27393v1 — §2-3 native omni-modal architecture, full-duplex streaming and training | https://arxiv.org/html/2604.27393v1 — §4 multimodal understanding/generation and streaming interaction evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: model-specific training data, hardware and latency conditions bound the reported interaction quality | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27393 | complete |
| SF-2026-ARXIV-2604-27396 | RP-397720cc3325ad3a | deep | arXiv:2604.27396v1 | SRC-ARXIV@arXiv:2604.27396v1 | https://arxiv.org/html/2604.27396v1 — §II-III heterogeneous dual-core architecture, leading-one predictor and dependency-aware system integration | https://arxiv.org/html/2604.27396v1 — §IV 16nm prototype, BitNet b1.58 3B prefill/decode and ablation evaluation | https://arxiv.org/html/2604.27396v1 — §IV evidence is bound to one 16nm prototype, LPDDR5-class memory, BitNet b1.58 3B and disclosed sequence settings; it does not prove cross-model or cross-accelerator portability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27396 | complete |
| SF-2026-ARXIV-2604-27405 | RP-c121112f04498c1d | deep | arXiv:2604.27405v1 | SRC-ARXIV@arXiv:2604.27405v1 | https://arxiv.org/html/2604.27405v1 — §2-3 item-level Reliable Change Index adaptation and within-family comparison | https://arxiv.org/html/2604.27405v1 — §4 2,000 MMLU-Pro items, 10 samples and two model-family upgrades | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: two families and one benchmark do not calibrate a universal RCI threshold or production consequence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27405 | complete |
| SF-2026-ARXIV-2604-27419 | RP-5dd84be88df2a1c3 | deep | arXiv:2604.27419v1 | SRC-ARXIV@arXiv:2604.27419v1 | https://arxiv.org/html/2604.27419v1 — §3 benchmark environment, interaction protocol and graders | https://arxiv.org/html/2604.27419v1 — §4 multimodal web-agent baselines and error analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: website-generation tasks and benchmark fixtures do not establish general computer-use reliability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27419 | complete |
| SF-2026-ARXIV-2604-27426 | RP-042ebbf5d9f0e3a9 | deep | arXiv:2604.27426v1 | SRC-ARXIV@arXiv:2604.27426v1 | https://arxiv.org/html/2604.27426v1 — §3-4 malicious model-code supply-chain path and active execution hijacking | https://arxiv.org/html/2604.27426v1 — §5 secret-exfiltration experiments across local fine-tuning setups | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: demonstrated attacks do not establish ecosystem prevalence; controls depend on the actual loader/runtime boundary | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27426 | complete |
| SF-2026-ARXIV-2604-27467 | RP-ceade8b95b003b70 | deep | arXiv:2604.27467v1 | SRC-ARXIV@arXiv:2604.27467v1 | https://arxiv.org/html/2604.27467v1 — §4-5 ScaleBox architecture, automated special-judge generation, distributed sandbox execution and configuration-driven suite | https://arxiv.org/html/2604.27467v1 — §5.2 and §6 verification accuracy/throughput plus RLVR training evaluation | https://arxiv.org/html/2604.27467v1 — §7 Limitations: generated judges, selected code tasks, sandbox policies and author infrastructure do not prove arbitrary-program correctness or universal RL stability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27467 | complete |
| SF-2026-ARXIV-2604-27486 | RP-b990ec69e8e1da74 | deep | arXiv:2604.27486v1 | SRC-ARXIV@arXiv:2604.27486v1 | https://arxiv.org/html/2604.27486v1 — §3-5 SASS decoding, type-constraint propagation with conflict detection, control-flow reconstruction and multi-instruction aggregation | https://arxiv.org/html/2604.27486v1 — §6 eight suites, 24,437 GPU functions, valid-IR and x86 semantic-pass evaluation plus ablation | https://arxiv.org/html/2604.27486v1 — §6 evaluation cannot validate MUFU, texture or full SIMT behavior through an x86 backend; supported architectures/instructions bound correctness and require fail-closed handling | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27486 | complete |
| SF-2026-ARXIV-2604-27488 | RP-3fa267da5f8e8f9c | deep | arXiv:2604.27488v1 | SRC-ARXIV@arXiv:2604.27488v1 | https://arxiv.org/html/2604.27488v1 — §3 Skills-Coach task generation, comparative execution and GRPO-style skill optimization | https://arxiv.org/html/2604.27488v1 — §4 agent-skill benchmarks, ablations and trace analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: author-generated tasks/judges and selected skills do not prove production release safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27488 | complete |
| SF-2026-ARXIV-2604-27536 | RP-e5f694dff5f04276 | deep | arXiv:2604.27536v1 | SRC-ARXIV@arXiv:2604.27536v1 | https://arxiv.org/html/2604.27536v1 — §2-4 POMDP formulation, verifiable observations and belief-guided routing | https://arxiv.org/html/2604.27536v1 — §5 service workloads, cost/reliability baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: proxy-verifier calibration and workload stationarity limit generalization to unseen services | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27536 | complete |
| SF-2026-ARXIV-2604-27586 | RP-dd077c3fd873a684 | deep | arXiv:2604.27586v1 | SRC-ARXIV@arXiv:2604.27586v1 | https://arxiv.org/html/2604.27586v1 — §3 trace-level contamination model, artifact transformations and divergence measures | https://arxiv.org/html/2604.27586v1 — §4 heterogeneous-document workflows and contamination interventions | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic workflows and chosen corruption models do not quantify real-world prevalence or causal completeness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27586 | complete |
| SF-2026-ARXIV-2604-27637 | RP-758e79a3d5b04d4d | deep | arXiv:2604.27637v1 | SRC-ARXIV@arXiv:2604.27637v1 | https://arxiv.org/html/2604.27637v1 — §2-3 per-model prompt-optimization protocol before evaluation | https://arxiv.org/html/2604.27637v1 — §4 model/task ranking changes under optimized versus static prompts | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected optimizers, tasks and search budgets do not define a universally fair evaluation regime | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27637 | complete |
| SF-2026-ARXIV-2604-27660 | RP-a100fb2b658328e5 | deep | arXiv:2604.27660v1 | SRC-ARXIV@arXiv:2604.27660v1 | https://arxiv.org/html/2604.27660v1 — §3 context-to-skill extraction, self-play generation and replay selection | https://arxiv.org/html/2604.27660v1 — §4 task suites, baselines and skill-transfer ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected tasks/models do not establish durable skill validity or safe cross-domain reuse | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27660 | complete |
| SF-2026-ARXIV-2604-27695 | RP-21533a279960d0b5 | deep | arXiv:2604.27695v1 | SRC-ARXIV@arXiv:2604.27695v1 | https://arxiv.org/html/2604.27695v1 — §3 evidence-gap diagnosis, layered memory and iterative retrieval controller | https://arxiv.org/html/2604.27695v1 — §4 long-conversation temporal/multi-hop benchmarks and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: benchmark conversations and author-defined gap labels do not prove production memory truthfulness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27695 | complete |
| SF-2026-ARXIV-2604-27707 | RP-b0079b58d321e90c | deep | arXiv:2604.27707v1 | SRC-ARXIV@arXiv:2604.27707v1 | https://arxiv.org/html/2604.27707v1 — §2-4 formal memo-versus-memory distinction and consolidation consequences | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; conceptual analysis and cited examples; no independent systems benchmark | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: position paper does not demonstrate a universally superior consolidation mechanism | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27707 | complete |
| SF-2026-ARXIV-2604-27711 | RP-3d571006c0e81857 | deep | arXiv:2604.27711v1 | SRC-ARXIV@arXiv:2604.27711v1 | https://arxiv.org/html/2604.27711v1 — §3 exocentric generation and control pipeline | https://arxiv.org/html/2604.27711v1 — §4 simulated and physical humanoid evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: video quality and selected tasks do not establish broad physical safety or sim-to-real robustness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27711 | complete |
| SF-2026-ARXIV-2604-27776 | RP-7e11a857cb966cd7 | deep | arXiv:2604.27776v1 | SRC-ARXIV@arXiv:2604.27776v1 | https://arxiv.org/html/2604.27776v1 — §3 cross-application Windows environment and process-centric tasks | https://arxiv.org/html/2604.27776v1 — §4 agent baselines, process/terminal grading and error taxonomy | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: Windows applications and curated professions do not represent every production workspace | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27776 | complete |
| SF-2026-ARXIV-2604-27781 | RP-165a6d3bec2f2238 | deep | arXiv:2604.27781v1 | SRC-ARXIV@arXiv:2604.27781v1 | https://arxiv.org/html/2604.27781v1 — §2-5 four-layer AI supply-chain decomposition, integrity gaps and lifecycle requirements | https://arxiv.org/html/2604.27781v1 — §5.1 reference-stack measurement across 48 projects, direct/transitive dependencies and source size | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 provides a conceptual decomposition and ecosystem measurement, not a controlled security evaluation or proof that every dependency is exercised at runtime | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27781 | complete |
| SF-2026-ARXIV-2604-27789 | RP-f84f0edd56cb5b51 | deep | arXiv:2604.27789v1 | SRC-ARXIV@arXiv:2604.27789v1 | https://arxiv.org/html/2604.27789v1 — §3-5 deployer contracts, update detection and compatibility-gate workflow | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; case studies and risk-suite demonstrations over hosted model changes | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: framework cannot observe undisclosed provider internals and depends on representative local suites | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27789 | complete |
| SF-2026-ARXIV-2604-27792 | RP-63168f3aaa1fa18a | deep | arXiv:2604.27792v1 | SRC-ARXIV@arXiv:2604.27792v1 | https://arxiv.org/html/2604.27792v1 — §2 architecture, heterogeneous pre/post-training and real-time inference optimizations | https://arxiv.org/html/2604.27792v1 — §3 simulation, world-model and real-robot evaluations | https://arxiv.org/html/2604.27792v1 — §4 future work; no independent safety or broad sim-to-real guarantee | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27792 | complete |
| SF-2026-ARXIV-2604-27819 | RP-8afdaa90d2626d5b | deep | arXiv:2604.27819v1 | SRC-ARXIV@arXiv:2604.27819v1 | https://arxiv.org/html/2604.27819v1 — §3 MCPHunt canary injection, multi-server topology and taint tracking | https://arxiv.org/html/2604.27819v1 — §4 server/tool compositions, models and leak-detection evaluation | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic canaries and enumerated servers do not prove complete semantic non-interference | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27819 | complete |
| SF-2026-ARXIV-2604-27844 | RP-c36e7217b950b425 | deep | arXiv:2604.27844v1 | SRC-ARXIV@arXiv:2604.27844v1 | https://arxiv.org/html/2604.27844v1 — §3-5 compressed collective API, exponent coding, GPU pipeline and adaptive switcher | https://arxiv.org/html/2604.27844v1 — §6 dense/MoE training on 64 GPUs with collective and end-to-end comparisons | https://arxiv.org/html/2604.27844v1 — §6.6 observed tensor normality is workload-specific; paper does not prove universal distributions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27844 | complete |
| SF-2026-ARXIV-2604-27855 | RP-1b976f9d7f87d144 | deep | arXiv:2604.27855v1 | SRC-ARXIV@arXiv:2604.27855v1 | https://arxiv.org/html/2604.27855v1 — §3-5 latency-constrained energy-geography model and placement formulation | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; regional scenarios and sensitivity analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: analytical inputs and assumed relocatability are not measured production traces or universal grid emissions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27855 | complete |
| SF-2026-ARXIV-2604-27861 | RP-d8ca151aea3295a0 | deep | arXiv:2604.27861v1 | SRC-ARXIV@arXiv:2604.27861v1 | https://arxiv.org/html/2604.27861v1 — §3-4 asymmetric contrastive dual-encoder state, frozen benign encoder and causal online monitoring | https://arxiv.org/html/2604.27861v1 — §5 strictly causal evaluation over 3.62M instructions and 8,600 malicious intents, including adaptive attacks | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected generated/curated intents and latent-space clustering do not prove complete intent reconstruction, universal low false-positive operation or action-level safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27861 | complete |
| SF-2026-ARXIV-2604-27878 | RP-b694f30145b10fb9 | deep | arXiv:2604.27878v1 | SRC-ARXIV@arXiv:2604.27878v1 | https://arxiv.org/html/2604.27878v1 — §3 canonical session schema, adapters and loss accounting; §4-5 realism and tester-reliability benchmark design | https://arxiv.org/html/2604.27878v1 — §6 four datasets, two languages, four simulator families and ranking-reliability analysis | https://arxiv.org/html/2604.27878v1 — §8 Limitations: dataset/language/simulator coverage is finite; correlations do not prove causal transfer to production users or unseen retrieval systems | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27878 | complete |
| SF-2026-ARXIV-2604-27891 | RP-d4ef06563c573834 | deep | arXiv:2604.27891v1 | SRC-ARXIV@arXiv:2604.27891v1 | https://arxiv.org/html/2604.27891v1 — §2 directed procedures and controlled LangGraph versus in-context conditions | https://arxiv.org/html/2604.27891v1 — §3 1,200 conversations across three procedural domains with two judge families | https://arxiv.org/html/2604.27891v1 — §5.2-5.3 three simulated customer-service domains, LLM judges and frontier-model capability bound the conclusion; token cost is higher in-context | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27891 | complete |
| SF-2026-ARXIV-2604-27906 | RP-33cddce37a5878af | deep | arXiv:2604.27906v1 | SRC-ARXIV@arXiv:2604.27906v1 | https://arxiv.org/html/2604.27906v1 — §3 schema-aware iterative extraction, validation gates and retry path | https://arxiv.org/html/2604.27906v1 — §4 memory extraction/update tasks and component ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected schemas and LLM judges do not prove arbitrary-domain completeness or truth | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27906 | complete |
| SF-2026-ARXIV-2604-28056 | RP-be7fd735cebbdcbf | deep | arXiv:2604.28056v1 | SRC-ARXIV@arXiv:2604.28056v1 | https://arxiv.org/html/2604.28056v1 — §3 RHyVE reward-hypothesis generation, verification and phase-aware deployment | https://arxiv.org/html/2604.28056v1 — §4 RL environments, reward baselines, ablations and competence analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected environments and verifier signals do not prove reward correctness or prevent all specification gaming | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28056 | complete |
| SF-2026-ARXIV-2604-28123 | RP-e678fa2f12b3b706 | deep | arXiv:2604.28123v1 | SRC-ARXIV@arXiv:2604.28123v1 | https://arxiv.org/html/2604.28123v1 — §3 PRISM black-box on-policy distillation between SFT and RLVR | https://arxiv.org/html/2604.28123v1 — §4 multimodal reasoning tasks, baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected models/tasks and teacher access do not establish universal benefit or cost efficiency | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28123 | complete |
| SF-2026-ARXIV-2604-28129 | RP-0453664996e0496b | deep | arXiv:2604.28129v1 | SRC-ARXIV@arXiv:2604.28129v1 | https://arxiv.org/html/2604.28129v1 — §3 activation-trajectory probes and adaptive multi-turn detector | https://arxiv.org/html/2604.28129v1 — §4 attack phases, model families, baselines and transfer tests | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: white-box activations and model-specific probes limit hosted-model use and require recalibration after updates | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28129 | complete |
| SF-2026-ARXIV-2604-28138 | RP-90b1824f77774a01 | deep | arXiv:2604.28138v1 | SRC-ARXIV@arXiv:2604.28138v1 | https://arxiv.org/html/2604.28138v1 — §4-6 coordinator, eBPF inspector, C/R data plane and deployment refinement | https://arxiv.org/html/2604.28138v1 — §7 correctness, overhead, mechanism ablations and code-agent case study | https://arxiv.org/html/2604.28138v1 — §9 Conclusion — exact-v1 has no dedicated limitations section; evidence is confined to Linux sandbox workloads and evaluated C/R backends | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28138 | complete |
| SF-2026-ARXIV-2604-28139 | RP-60081ac3b24d9eb4 | deep | arXiv:2604.28139v1 | SRC-ARXIV@arXiv:2604.28139v1 | https://arxiv.org/html/2604.28139v1 — §3 refreshable signals, release snapshot, controlled fixtures and graders | https://arxiv.org/html/2604.28139v1 — §4-5 105 tasks, 13 models, trace/artifact grading and family-level analysis | https://arxiv.org/html/2604.28139v1 — §3.3 and §5.5 current release and ClawHub-derived demand are not a universal production distribution | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28139 | complete |
| SF-2026-ARXIV-2604-28157 | RP-afbc676031469504 | deep | arXiv:2604.28157v1 | SRC-ARXIV@arXiv:2604.28157v1 | https://arxiv.org/html/2604.28157v1 — §3 FlashRT red-team search and cache/memory optimizations | https://arxiv.org/html/2604.28157v1 — §4 prompt-injection/knowledge-corruption workloads, systems measurements and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: attack suites and author hardware do not establish full threat coverage or production prevalence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28157 | complete |
| SF-2026-ARXIV-2604-28158 | RP-c8000f3d285bdbb7 | deep | arXiv:2604.28158v1 | SRC-ARXIV@arXiv:2604.28158v1 | https://arxiv.org/html/2604.28158v1 — §3 method-evolution ontology, extraction and graph construction | https://arxiv.org/html/2604.28158v1 — §4 retrieval/reasoning tasks and graph-quality evaluation | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: automated extraction and selected AI literature do not prove a complete or authoritative knowledge graph | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28158 | complete |
| SF-2026-ARXIV-2604-28175 | RP-484747c0ba06a491 | deep | arXiv:2604.28175v1 | SRC-ARXIV@arXiv:2604.28175v1 | https://arxiv.org/html/2604.28175v1 — §3 Strait dual-priority scheduler and interference predictor | https://arxiv.org/html/2604.28175v1 — §4 serving traces/models, baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: on-premises model roster and hardware do not establish universal predictor transfer or tail-SLO behavior | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28175 | complete |
| SF-2026-ARXIV-2604-28181 | RP-7532f2ca70014445 | deep | arXiv:2604.28181v1 | SRC-ARXIV@arXiv:2604.28181v1 | https://arxiv.org/html/2604.28181v1 — §3 synthetic computer/workspace generation pipeline | https://arxiv.org/html/2604.28181v1 — §4 long-horizon productivity tasks, realism and agent evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic environments may miss organizational policy, hidden dependencies and real-user distributions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28181 | complete |
| SF-2026-ARXIV-2604-28182 | RP-575444c9e25d6fdd | deep | arXiv:2604.28182v1 | SRC-ARXIV@arXiv:2604.28182v1 | https://arxiv.org/html/2604.28182v1 — §3 exploration-hacking threat model and resistant-policy construction | https://arxiv.org/html/2604.28182v1 — §4 RL training experiments, detection signals and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: constructed settings do not establish spontaneous prevalence in deployed models or a complete detector | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28182 | complete |
| SF-2026-ARXIV-2604-28190 | RP-6d83eca89d020006 | deep | arXiv:2604.28190v1 | SRC-ARXIV@arXiv:2604.28190v1 | https://arxiv.org/html/2604.28190v1 — §3 Representation Fréchet Loss and population/batch decoupling | https://arxiv.org/html/2604.28190v1 — §4 visual-generation models, quality/diversity evaluations and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected representation encoders and image workloads do not prove perceptual alignment or generalization to all modalities | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28190 | complete |
| SF-2026-ARXIV-2604-28196 | RP-7ce7a2294237466e | deep | arXiv:2604.28196v1 | SRC-ARXIV@arXiv:2604.28196v1 | https://arxiv.org/html/2604.28196v1 — §3 HERMES++ unified 3D understanding/prediction architecture | https://arxiv.org/html/2604.28196v1 — §4 driving datasets, understanding/generation metrics and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: driving datasets and open-loop generation do not prove closed-loop safety or causal controllability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28196 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2604-26963:start -->
#### MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems

问题、旧路径与 changed constraint：Large language models (LLMs) are increasingly deployed as the execution core of autonomous agents rather than as standalone text generators. 旧路径以固定 batch、静态资源或单一队列换取可预测性；异构 workload 与 SLO 变化后，局部吞吐不再等于端到端服务效率。

机制与 state/data/control owner：owner=`INFER-SCHEDULING`；作者公开的机制是：We design and implement MARS, an efficient and adaptive co-scheduling system that globally coordinates heterogeneous agentic workloads under coupled GPU-CPU resource pressure. 对系统而言，scheduler 拥有 admission、placement、rate/preemption state 与 SLO observation；预测漂移或 tail/fairness 越界时回退保守配置。 exact-v1 Method 具体写明：4.2. Control Plane Design While the unified information stream (§4.1) makes heterogeneous execution observable, observability alone is not sufficient to preserve stability. Under agentic workloads, a serving node is constrained by GPU capacity and CPU service capacity. Without explicit admission control, serving engines remain vulnerable to cascading overload under sustained agentic workloads. MARS addresses this mismatch with an External Control Plane, which is organized around two logical modules. A Global Load Balancer shapes the waiting queue into a resource-aware admission order. An External Admission Controller then computes how much of that ordered queue can safely enter the data plane. Global Load Balan

Evaluation contract：6.2. Experimental Setup Models & Testbed. We evaluate our system on two models: Qwen3-Coder-30B-A3B-Instruct (262K context limit) (Yang et al., 2025) and GPT-OSS-120B (131K context limit) (OpenAI, 2025a). Experiments are conducted across two hardware configurations: a server equipped with NVIDIA H200 NVL (144 GiB) GPUs, dual AMD EPYC 9355 CPUs, and 1.5 TB of host memory, and a node featuring an NVIDIA H100 NVL (96 GiB) GPU. All runs utilize a single GPU (TP=1) on top of a modified vLLM backend. To eliminate OS-level interference, the LLM serving engine and host-side tool executions are pinned to strictly disjoint CPU cores. Metrics. To capture the performance of multi-turn agentic programs, our evaluation prima 因而这里只承认该 section 披露的模型、数据、任务和比较协议；未披露的生产 SLO、跨硬件与长期运行不外推。

Trade-off / failure / fallback / coexistence：exact-v1 的限制/反证段为：7. Discussions Fairness, Starvation, and Objective Design. MARS explicitly prioritizes global end-to-end progress and dynamic-SLO goodput over strict request-level fairness. Under agentic heterogeneity, naive time-sharing preserves local fairness but catastrophically inflates global completion times. However, multi-tenant cloud deployments often demand explicit fairness guarantees or strict SLA isolation. Extending MARS to support multi-dimensional fairness is non-trivial: classical models like Dominant Resource Fairness (DRF) (Ghodsi et al., 2011) assume static demands, whereas agentic sessions oscillate unpredi exact-v1 暴露的具体 failure pressure 是：Consequently, coordinating heterogeneous resource demands of agentic execution has emerged as a critical system challenge. An internal agent-centric scheduler further minimizes the end-to-end critical path by prioritizing latency-sensitive continuations and adaptively retaining KV cache state only when warm resumption yields a latency benefit. 该机制新增状态、控制或验证开销，且只在作者披露 workload 内成立。 若 exact-v1 限制段暴露的前提失效（7. Discussions Fairness, Starvation, and Objective Design. MARS explicitly prioritizes global end-to-end progress and dynamic-SLO goodput over strict request-level fairness. Under agentic heterogeneity, naive time-sharing preserves local fairness but catastrop），则保留 `INFER-SCHEDULING` 在 `books/part-05-inference-system/56-inference-scheduling.md#调度对象从-request-变成-token-state (line 16, H2: 调度对象从 request 变成 token state)` 的当前路径：“普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。 调度器需要理解： - 请求处于 Prefill 还是 Decode。 - 已经生成多少 token。 - 还可能生成多少 token。 - KV Cache 占用多少显存。 - 是否共享 prefix。 - 是否正在 speculative verification。 - 是否需要跨 worker handoff。 这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。 一个完整 Serving 系统通常同时存在四层决策： 只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。”；不把该 family 的局部结果升级为默认控制面。

Artifact boundary：5. Implementation Integration with vLLM. We implement MARS in 5,300 lines of Python, organized as standalone control-plane services plus lightweight hooks into the backend inference engine. On the serving side, MARS reuses vLLM (Kwon et al., 2023) and extends only its V1 serving and scheduling layers, leaving the lower-level batching, attention, and KV memory-management path unchanged. We augment the OpenAI-compatible request schema with stable per-session metadata, including a persistent job_id and tool-transition markers, propagate these fields through SamplingParams.extra_args into internal request objects, and expose our policies through additional scheduler modes. These hooks are sufficient to preserve session continuity across turns, maintain per-session state, and align request ordering with KV residen

<!-- claim:SF-2026-ARXIV-2604-26963:start -->`MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems` 只证明 exact-v1 的公开模型、数据、硬件和 workload；evaluation evidence 为：Our evaluations show that MARS reduces end-to-end latency by up to 5.94x while maintaining nearly maximal system throughput. We further integrate MARS as the serving backend for the OpenHands coding agent framework, demonstrating its real-world effectiveness by accelerating end-to-end task completion time by up to 1.87x. 未披露生产 SLO、多租户、跨硬件或长期运行结果时不得外推。 这不是生产通用性、完整 failure matrix 或未披露配置的证明。<!-- claim:SF-2026-ARXIV-2604-26963:end -->

Books Decision=`No Change — Existing Coverage`；current owner=`books/part-05-inference-system/56-inference-scheduling.md`，adjacent=`books/part-05-inference-system/55-pd-disaggregation.md; books/part-06-ai-infrastructure/57-what-is-ai-platform.md`；fresh-context reviewer 未修改共享 Books。
<!-- review:SF-2026-ARXIV-2604-26963:end -->

<!-- review:SF-2026-ARXIV-2604-26968:start -->
<!-- claim:SF-2026-ARXIV-2604-26968:start -->exact-v1 `h3 V-B Analytical Projection Methodology [id=—]` 定义机制：Cluster-scale performance is projected using published hardware specifications for each memory tier: H100 SXM GPU HBM3 bandwidth of 3.35 TB/s and 80 GB capacity [27]; CXL 3.0 device-local bandwidth of 64 GB/s with approximately 150 ns device-local latency (∼{\sim}500 ns GPU-observed via the CXL.mem protocol) [23]; GPUDirect Storage throughput of 12 GB/s via cuFile APIs [28]; and InfiniBand NDR bandwidth of 400 Gbps (50 GB/s effective) [33]. Per-tier throughput projections combine these datasheet bandwidths with validated per-block access patterns from the Bayesian predictor running on trace data. Throughput projections assume linear scaling from batch size increases up to the compute saturation point of each model, a standard assumption in memory-bound inference analysis [1, 4]. Metrics. Time-to-first-token (TTFT) at P50 and P99, time-between-tokens (TBT) at P99, throughput (tokens/s/GPU), and cost ($/million tokens computed from cloud GPU pricing at $2/GPU-hour). 因此 state/data/control owner 归入 `INFER-GPU-MEMORY`，而不是由论文名称或产品自行成为知识 owner。<!-- claim:SF-2026-ARXIV-2604-26968:end -->

问题、旧路径与约束变化：exact-v1 `h2 I Introduction [id=—]` 说明旧路径与新约束：The deployment of large language models (LLMs) at data-center scale has shifted the primary bottleneck from compute to memory. During autoregressive decoding, each generated token requires attending to the key-value (KV) pairs of all preceding tokens, and these KV pairs must remain resident in fast memory for the duration of a request. For a 70-billion-parameter model serving sequences of 128K tokens, the KV cache alone can consume over 40 GB of GPU HBM per request—exceeding the memory capacity of many production accelerators and limiting batch sizes to single digits [1, 4]. Three compounding inefficiencies plague current KV cache management systems. Problem 1: No Unified Cross-Architecture… 旧路径在论文限定的先前 workload 中仍以较少状态与控制开销成立；只有上述约束变化后才需要新机制。

Evaluation contract：exact-v1 `h3 V-D Projected Multi-Tier Performance [id=—]` 的可复算范围是：†\daggerGPU-only baseline from published vLLM benchmarks [1]. Table IV shows the projected incremental benefit of each memory tier. The largest single improvement comes from adding CXL 3.0 memory (+35% throughput over CPU DRAM alone), as its bandwidth-latency profile makes it suitable for warm KV cache blocks that are accessed within 10–100 ms. The RDMA pool provides a projected throughput gain of +23% over NVMe by enabling cross-node sharing of system-prompt blocks, which eliminates redundant prefill computation. The full system (including parallel filesystem for checkpoint persistence and deduplication) adds a projected 5% throughput improvement over the RDMA configuration by accelerating warm-start scenarios. The projected gap between GPU-only and the full system represents a 2.86×2.86\times throughput improvement and 3.8×3.8\times TTFT reduction—achieved by utilizing memory resources already present in data centers but currently invisible to the inference serving stack.

Trade-off、failure 与 fallback：exact-v1 `h2 VII Conclusion [id=—]` 给出的限制、反例或未来压力是：We presented a predictive multi-tier memory management system for KV cache in large-scale GPU inference. By addressing the three fundamental inefficiencies—fragmented cross-architecture sizing, single-tier confinement, and reactive eviction—component-level validation and analytical projections indicate 1.41.4–2.1×2.1\times projected TTFT reduction, 1.71.7–2.9×2.9\times throughput improvement, and 47% projected cost reduction. The architecture-variant-aware sizing alone unlocks up to 7.4×7.4\times batch size improvements, with the largest gains coming from MLA support and unified cross-architecture sizing in heterogeneous clusters. Trace-driven evaluation of the Bayesian predictor achieves 70–84% cache hit rates on real conversation logs, and the online learning approach adapts to workload shifts without manual tuning. Our six-tier hierarchy is designed to transform idle data-center… 作者范围之外必须保留旧路径或更保守配置作为 fallback；未披露的生产 SLO、多租户、跨硬件和长期故障恢复均记为 Not Disclosed。

Evidence boundary：只支持 `h3 V-B Analytical Projection Methodology [id=—]` 所定义的机制与 `h3 V-D Projected Multi-Tier Performance [id=—]` 所覆盖的模型、数据、硬件和 workload；`h2 VII Conclusion [id=—]` 之外不证明生产泛化、因果完备性或跨环境收益。

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26968:end -->

<!-- review:SF-2026-ARXIV-2604-26997:start -->
#### Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：The ANS architecture consists of four primary components: (1) ANS Registry - centralized agent discovery and authentication service, (2) ANS Client Library - agent-side implementation for registration and communication, (3) Kubernetes Integration Layer - native integration with container orchestration and service mesh, and (4) Policy Engine - OPA-based governance and compliance enforcement. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：While the ANS protocol specification [ 20 ] provides a comprehensive protocol-agnostic framework for agent discovery and authentication, practical implementation challenges remain for production Kubernetes deployments. Current approaches suffer from:

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：While ANS provides significant advantages, limitations include protocol dependencies, performance overhead from cryptographic operations, and scalability constraints in very large deployments. Future work will address these limitations through federated ANS deployment, AI-powered policy generation, and edge computing integration.。因此若该限制在目标 workload 中触发，不能把 `Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26997:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26997:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26997:end -->

<!-- review:SF-2026-ARXIV-2604-27003:start -->
#### When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：We build on AgentGym ( Xi et al., 2024 ) with the ReMe memory module ( Cao et al., 2025 ) . Retrieval uses BM25 ( Robertson and Zaragoza, 2009 ) throughout. memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图

Evaluation contract：Scratch baselines affect FWT interpretation. Because FWT is defined relative to each condition’s own scratch performance, different baselines can affect the comparison. For example, on BabyAI B → \to A: Cond-Ind’s scratch is 75.5% and cross-task is 74.5% (FWT = − 1.0 =-1.0 ); Cond-Step’s scratch is 70.0% and cross-task is 77.5% (FWT = + 7.5 =+7.5 ). Step achieves higher absolute cross-task performance (77.5 vs. 74.5), and the FWT gap is amplified by Step’s lower scratch baseline. This does not invalidate the comparison (FWT measures each design’s relative gain from cross-task memory), but readers should note that the absolute performance levels are closer than the FWT values suggest.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：External memory may appear to sidestep the stability-plasticity dilemma because old experience is preserved while new experience can always be appended. Our results suggest a more cautious view: once behavior depends on retrieval through a finite context window, old and new memories compete for the same channel into the agent’s decisions, reintroducing transfer and interference through retrieval rather than through parameter updates. Across both studies, abstraction shapes whether retrieved experience helps or misleads, memory granularity determines whether stored diversity becomes useful guidance or repetitive noise, and the resulting system remains subject to trade-offs that require careful design.。因此若该限制在目标 workload 中触发，不能把 `When Continual Learning Moves to Memory: A Study of Experience Reuse in LLM Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27003:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27003:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27003:end -->

<!-- review:SF-2026-ARXIV-2604-27032:start -->
#### LLM-Guided Runtime Parameter Optimization for Energy-Efficient Model Inference

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-SCHEDULING` 中该 family 的受限状态。

机制与 state/control owner：Runtime parameter optimization is one method to improve the energy efficiency of LLM inference; there are other techniques that can be used alongside or instead of it. One such solution is ELLIE, which dynamically maps inference phases across heterogeneous hardware for energy reduction. It will make these decisions per prompt and per model, resulting in significant decreases in energy consumption [ 3 ] . This solution is very effective; however, it can be hardware-dependent or complicated to include in the inference workflow. In a paper by Stojkovic et al., multiple methods, related to techniques like input length and batching, that decrease energy consumption in inference are presented [ 6 ] . scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission

Evaluation contract：We evaluated Claude combined with the enhanced and baseline prompting strategies on their ability to generate energy-efficient parameters for vLLM inference, as well as PyTorch inference. We collected data by running the prompt templates, through the loop shown in Figure 1 . We repeated this loop five times for both the enhanced and baseline prompt templates.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In HPC environments, the results show that LLMs can make metric-aware decisions without exhaustive search, aligning with emerging work on AI-assisted system optimization. In this context, scalability refers to optimization problems with large parameter spaces and tighter hardware constraints, which create complex interactions between runtime parameters. Uniform exploration strategies require a large number of evaluations to maintain adequate coverage across these high-dimensional spaces, and each evaluation incurs the cost of GPU execution. Our results suggest that LLMs combined with prompt engineering can handle this without increasing evaluations.…。因此若该限制在目标 workload 中触发，不能把 `LLM-Guided Runtime Parameter Optimization for Energy-Efficient Model Inference` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27032:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27032:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27032:end -->

<!-- review:SF-2026-ARXIV-2604-27039:start -->
#### Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-SCHEDULING` 中该 family 的受限状态。

机制与 state/control owner：Here the trajectories are sampled from a fixed generator checkpoint and decoding policy, and G t ( n ) G_{t}^{(n)} is computed exactly from each realized completion. This objective therefore corresponds to Monte Carlo regression with dense token-level supervision over the rollout state distribution induced by that policy. scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission

Evaluation contract：For the ablation and scalability experiments, we sample 100k examples from each dataset, except for math, where we use all 95k available examples. For the Length-Controlled Generation and Performance–Efficiency Trade-off experiments, we use the full training sets of all three datasets. We randomly sample 8k examples for validation during training. Unless otherwise specified, data sampling uses temperature 1.0 1.0 and top-p 1.0 1.0 , and we sample up to 16 completions per prompt.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We proposed LenVM , a token-level value model for remaining generation length. By assigning a constant per-token reward and predicting the resulting discounted return, LenVM places length modeling in a standard value-learning framework with bounded, dense, and annotation-free supervision. Our experiments show that this simple formulation is both useful and scalable. LenVM supports precise length-controlled generation, exposes a smooth performance–efficiency trade-off without modifying the base generator, predicts expected generation horizon, and improves consistently with model scale and automatically collected supervision.…。因此若该限制在目标 workload 中触发，不能把 `Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27039:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27039:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27039:end -->

<!-- review:SF-2026-ARXIV-2604-27045:start -->
#### Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：Dimension 1: Memory Extraction Quality. The first dimension measures the accuracy of the delta-based memory extraction pipeline across the full hybrid transcript corpus (675 sessions, 2,296 patient turns). The evaluation targets 951 ground-truth memory events: 522 from real UIC sessions (1.2 per session on average) and 429 from synthetic reconciliation sessions (1.8 per session). For each ground-truth event, an LLM judge evaluates whether the expected information is captured in the system’s memory state at the corresponding point in the conversation. The judge considers information spread across multiple memories, classifying each event as match (fully captured), partial (gist present but key details missing), or no_match (not captured). We report recall (match + partial / total) and strict recall (match only / total) as primary metrics. A separate transcript-level LLM judge assesses the final memory state against the complete conversation for faithfulness (absence of hallucinated content) and deduplication (absence of redundant memories), each scored 1–5 (see Appendix I for both judge prompts). memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图

Evaluation contract：Dimension 1: Memory Extraction Quality. The first dimension measures the accuracy of the delta-based memory extraction pipeline across the full hybrid transcript corpus (675 sessions, 2,296 patient turns). The evaluation targets 951 ground-truth memory events: 522 from real UIC sessions (1.2 per session on average) and 429 from synthetic reconciliation sessions (1.8 per session). For each ground-truth event, an LLM judge evaluates whether the expected information is captured in the system’s memory state at the corresponding point in the conversation. The judge considers information spread across multiple memories, classifying each event as match (fully captured), partial (gist present but key details missing), or no_match (not captured). We report recall (match + partial / total) and strict recall (match only / total) as primary metrics. A separate transcript-level LLM judge assesses the final memory state against the complete conversation for faithfulness (absence of hallucinated content) and deduplication (absence of redundant memories), each scored 1–5 (see Appendix I for both judge prompts).

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：To evaluate the pipeline across hundreds of longitudinal sessions, we used Synthea-generated FHIR bundles matched to real patients via fuzzy scoring, and LLM-generated ground-truth labels for severity and safety criticality. While binary detection and resource identification is robust to label quality, severity and safety recall metrics should be interpreted with this caveat. The synthetic reconciliation conversations, while constrained to coaching scope and seeded by real UIC transcripts, may not fully capture the ambiguity of real patient speech. Future work should validate the engine on real patient conversations paired with their actual EHR data and clinician-adjudicated ground-truth labels.。因此若该限制在目标 workload 中触发，不能把 `Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27045:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27045:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27045:end -->

<!-- review:SF-2026-ARXIV-2604-27083:start -->
#### Co-Evolving Policy Distillation

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-GRPO` 中该 family 的受限状态。

机制与 state/control owner：The two experiments together expose a structural inconsistency in the static pipeline and point to a more nuanced requirement for 𝒪 k \mathcal{O}_{k} . Experiment 1 shows that η ⁡ ( 𝒪 k ) \eta(\mathcal{O}_{k}) rises with overlap when teacher and student differ, but necessarily collapses when they become indistinguishable; Experiment 2 shows that training experts in isolation drives overlap toward the low end, where η \eta is also small. To raise η \eta from η ⁡ ( 𝒪 low ) \eta(\mathcal{O}_{\text{low}}) to η ⁡ ( 𝒪 mod ) \eta(\mathcal{O}_{\text{mod}}) as Eq. ( 5 ) envisions, an effective paradigm must therefore satisfy three coupled requirements: (i) distillation must occur during expert training rather than after it, so that 𝒪 k \mathcal{O}_{k} does not have time to drift toward the low- η \eta regime; (ii) the teacher must continue to evolve as the student does, so that their behavioral overlap is actively maintained rather than left to drift; and (iii) capability-specific training must continue to push the two sides apart, so that the supervision retains information the student does not already possess. The next section instantiates these three requirements as CoPD: cross-branch mutual OPD addresses (i) and (ii) by making each branch a continuously updated teacher for the other, while alternating with branch-specific RLVR addresses (iii) by periodically opening up the behavioral gap that subsequent OPD will then close. rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit

Evaluation contract：Training Data and Evaluation Benchmarks. We evaluate CoPD on its ability to co-evolve text, image, and video reasoning capabilities through parallel branch training. Our main analysis focuses on the two-branch setting with text and image reasoning; we additionally evaluate a three-branch setting that incorporates video reasoning to demonstrate scalability. For text reasoning, we use Polaris-Dataset-53K [ 17 ] , filtered from DeepScaleR-Preview-Dataset [ 18 ] and AReal-boba-Data [ 19 ] to retain high-quality mathematical reasoning problems. For image reasoning, we use MMFineReason-123K [ 20 ] , a collection of image reasoning samples with verifiable answers. For video reasoning, we collect training data from OneThinker [ 21 ] , VideoChat-R1 [ 22 ] , and Video-R1 [ 9 ] , and filter with Qwen3-8B-VL by removing samples with a pass rate of either 0% or 100%, retaining 40K samples of moderate difficulty.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This paper is the third installment of our Self-Taught RLVR research series, which aims to investigate how LLMs can better learn from themselves and self-evolve. We explore three complementary dimensions: the first installment, RLSD [ 50 ] , investigates the informed self —a self augmented by privileged information that teaches the base self; the second installment, NPO [ 51 ] , focuses on the temporal self —a near-future self teaching its past self; this paper explores the parallel self —parallel selves mutually teaching each other. Each of these three papers is self-contained and complete; together, they instantiate Self-Taught RLVR .。因此若该限制在目标 workload 中触发，不能把 `Co-Evolving Policy Distillation` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27083:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27083:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27083:end -->

<!-- review:SF-2026-ARXIV-2604-27085:start -->
#### Efficient Training on Multiple Consumer GPUs with RoundPipe

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-PIPELINE-PARALLEL` 中该 family 的受限状态。

机制与 state/control owner：Heterogeneous memory offloading has been widely explored to enable training models that exceed GPU memory. One line of work offloads model weights and optimizer states to CPU or NVMe ( Rajbhandari et al., 2021 ; Sun et al., 2022 ; Fang et al., 2022 ) . Another line targets activation offloading, swapping intermediate activations to the host to reduce peak GPU memory ( Wang et al., 2018 ; Rhu et al., 2016 ; Zong et al., 2023 ; Bae et al., 2021 ) . More recent systems manage data at tensor granularity to achieve better transfer–compute overlaps ( Zhang et al., 2023 ; Liao et al., 2024 ; Ren et al., 2021a ) . However, these approaches are predominantly designed for single-GPU or data-parallel settings; scaling them to multiple GPUs incurs substantial communication overhead ( Feng et al., 2023 ) . RoundPipe co-designs distributed training with host-memory offloading, achieving scaling and offloading with negligible overhead. pipeline runtime 拥有 stage/microbatch/activation state，optimizer 只提交完整 step

Evaluation contract：We conducted a roofline analysis ( Williams et al., 2009 ) to evaluate whether the data transfers of the computation dispatch paradigm introduce bottlenecks that block GPU execution in RoundPipe . We conclude that the PCIe transfer time can be entirely overlapped by computation simply by using typical training batch sizes (as small as B = 8 B=8 for dense models and B = 80 B=80 for MoE models). Detailed analysis is available in Appendix C .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Crucially, existing schedules face a dilemma because they force the total stage count to be an exact integer multiple of the GPU count. Coarse-grained partitioning with fewer stages (e.g., GPipe) incurs high structural bubbles. Conversely, fine-grained partitioning with more stages (e.g., looped schedules) leads to severe load imbalance: as each stage contains fewer layers, compute-heavy components, such as the LM head, introduce significant inter-stage imbalance regardless of where they are assigned. Consequently, as demonstrated in Figure 3 , the overall bubble ratio can reach up to 30% in current pipeline schedules.。因此若该限制在目标 workload 中触发，不能把 `Efficient Training on Multiple Consumer GPUs with RoundPipe` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27085:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27085:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27085:end -->

<!-- review:SF-2026-ARXIV-2604-27089:start -->
#### AutoSP: Unlocking Long-Context LLM Training Via Compiler-Based Sequence Parallelism

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-TENSOR-PARALLEL` 中该 family 的受限状态。

机制与 state/control owner：Sequence parallelism (SP) is a key enabler for long-context training. These strategies enable scaling input sequence lengths with increasing GPU resources by sharding input tensors and activations across the sequence dimension. Communication collectives are inserted in the forward and backward pass as necessary to correctly shuffle tokens to the desired device. A popular SP strategy, and the focus of this work, is DeepSpeed-Ulysses (Ulysses) ( Jacobs et al., 2024 ) . We illustrate how Ulysses operates with 3-SP groups in Fig. 1 . parallel plan owner 冻结 tensor layout/collective，kernel 只消费一致 shard

Evaluation contract：Setup. We evaluate AutoSP and all the baselines on NVIDIA GH200-96GB & A100-80GB and AMD MI250-64GB hardware. All experiments use PyTorch-2.7 with CUDA 12.8 (on NVIDIA GPUs), and ROCm 6.4 (on AMD GPUs). To implement AutoSP, we lift the DeepSpeed-Ulysses SP scheme into PyTorch-2.0’s compilation stack and integrate all our compiler optimizations into the DeepSpeed project, due to its popularity in training large scale LLMs.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this paper, we present AutoSP, the first compiler-based, PyTorch-native solution for training large-language-models at long-contexts. Through a combination of automated sequence-parallelism (SP) and a sequence-aware AC strategy, AutoSP achieves significant sequence length extensions at negligible cost to training throughput. Our results demonstrate that compiler-driven, PyTorch-native automation provides a practical and portable foundation for long-context model training.。因此若该限制在目标 workload 中触发，不能把 `AutoSP: Unlocking Long-Context LLM Training Via Compiler-Based Sequence Parallelism` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27089:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27089:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27089:end -->

<!-- review:SF-2026-ARXIV-2604-27151:start -->
#### Step-level Optimization for Efficient Computer-use Agents

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-WORKFLOW` 中该 family 的受限状态。

机制与 state/control owner：We propose an event-driven, step-level cascade that runs a small GUI policy by default and allocates expensive large-model compute only when there is evidence of elevated risk. Figure 1 illustrates the overall architecture of our framework. The controller relies on two lightweight learned monitors that trigger events : a Stuck Monitor that detects progress degradation and requests recovery, and a Milestone Monitor that identifies semantically meaningful checkpoints where it is most informative to verify intent and progress. workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步

Evaluation contract：For both benchmarks, we evaluate every single-model baseline and every cascaded configuration under the same task setting. In cascaded runs, the smaller model acts as the default policy, and the stronger model is called only when the controller decides to escalate. This setup allows us to directly measure whether step-level routing can preserve the performance benefits of stronger models while reducing inference cost. We evaluate both effectiveness and efficiency on OSWorld and WebArena . Specifically, for both benchmarks we report overall task success rate and inference cost . We also report efficiency-related statistics for both benchmarks, including latency, cost, and behavior in cascaded settings. For models derived from open-weight base models, we report reference cost estimates using OpenRouter ( OpenRouter, 2026 ) pricing. For fine-tuned models, these estimates are based on the corresponding open-weight base model available. Reported latency is measured from our local deployment using 2× H100 GPUs. Taken together, these metrics provide a unified view of the performance–efficiency trade-off and allow us to assess when step-level cascading offers advantages over standalone models.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this paper, we introduced an event-driven, step-level cascade for efficient computer-use agents that allocates expensive large-model inference only when lightweight monitors detect elevated risk. Rather than treating every interaction step as equally difficult, our framework is built on the observation that long-horizon GUI trajectories are highly heterogeneous: many steps are routine and can be handled by a small default policy, while failures tend to concentrate at a limited number of critical moments.…。因此若该限制在目标 workload 中触发，不能把 `Step-level Optimization for Efficient Computer-use Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27151:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27151:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27151:end -->

<!-- review:SF-2026-ARXIV-2604-27202:start -->
#### Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：To address our research questions, we analyze web pages and HTTP responses from multiple sources. We then identify candidate prompt injections and perform extensive validation to obtain a high-confidence set of true positives. Using this validated corpus, we conduct four downstream analyses: prompt template extraction, prompt semantic analysis (objectives, targets, and techniques), delivery and visibility characterization, and ecosystem and effectiveness analysis. This section focuses on the construction and validation of the dataset underlying all later results. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：We then evaluate whether the prompt is visible to human users. Injections delivered through channels not rendered by browsers—including HTTP headers, comments, structured data, and metadata-only fields—are treated as non-visible by construction. For prompts embedded in rendered HTML, we load the page in headless Chrome ( 35 ) using Playwright ( 63 ) and Chrome DevTools Protocol ( 10 ) , wait 30 seconds for client-side rendering, locate the matched text in the DOM, and inspect the associated element. We classify a prompt as non-visible when rendering suppresses or obscures it, including non-displayed elements, near-zero dimensions, clipping, imperceptibly small text, insufficient text–background contrast, occlusion by overlapping elements, or stacking-order manipulations. Table 4 summarizes these conditions.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Although we analyze 1.2B URLs, our results are primarily based on web crawls such as Common Crawl, which may underrepresent authenticated or platform-restricted content (e.g., social media feeds). Similarly, while our detection pipeline relies on a list of indicators, it may not capture all variants, such as highly obfuscated or non-English prompt injections. Consequently, our measurement should be interpreted as a lower bound estimate of prompt injection prevalence. Our effectiveness evaluation focuses on a summarization task and a representative set of page representations, providing a controlled comparison across models and inputs.…。因此若该限制在目标 workload 中触发，不能把 `Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27202:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27202:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27202:end -->

<!-- review:SF-2026-ARXIV-2604-27221:start -->
#### Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-RAG` 中该 family 的受限状态。

机制与 state/control owner：The architecture of Web2BigTable is shaped by two structural demands of web-to-table search. First, a single instance spans many entities under a structured schema. The single-agent policy of Equation ( 1 ) must therefore handle retrieval, state tracking, and synthesis across hundreds of rows within a bounded context window, while remaining unable to exploit the conditional independence across entities that the task naturally exhibits [ 12 ] . This motivates a factorisation of the policy into two levels: an upper-level orchestrator that decomposes the query into independent subtasks, and a lower-level pool of workers that resolves these subtasks in parallel, with the two layers strictly separated and interacting only through shared memory. retrieval service 拥有 index/query evidence，generator 不获得来源真值所有权

Evaluation contract：Table 4 and Figure 6 summarise the XBench-DeepSearch evaluation. Web2BigTable achieves 73.0 accuracy, surpassing all baselines including frontier proprietary systems such as Minimax-M2 and MiroFlow (both at 72.0). Rows labelled “(OpenRouter)” correspond to our own re-evaluation of the underlying models via the OpenRouter API. XBench does not disclose its official inference configuration, including context window, temperature, and decoding parameters, so the 6 to 8 point gap between these rows and the officially reported scores (for example, 64.0 versus 72.0 for Minimax-M2) most likely reflects undocumented setup differences rather than capability gaps in the underlying models. We therefore treat the officially reported numbers as the primary point of comparison. The impact of the learned orchestrator skills is evident: accuracy improves from 41.0 (without learned skills) to 73.0 following strategy learning, a gain of 32.0 points from 20 synthesised training queries. This gain mirrors the pattern observed on WideSearch, where the same run-verify-reflect pipeline drives the majority of the performance advantage. The consistency of this effect across two structurally distinct benchmarks, one emphasising breadth over hundreds of entities and the other depth over multi-hop reasoning chains, validates the generalisability of the bi-level framework.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented Web2BigTable, a bi-level multi-agent framework for large-scale web-to-table construction. The system addresses the fundamental tension between breadth and reliability in agentic web search through a memory-mediated self-evolving architecture: an upper-level orchestrator that automatically learns reusable decomposition strategies from a small training split, and a lower-level pool of asynchronous workers that coordinate through a shared Markdown workboard whilst evolving their own execution skills, with all adaptation mediated through persistent, human-readable memory rather than gradient updates.…。因此若该限制在目标 workload 中触发，不能把 `Web2BigTable: A Bi-Level Multi-Agent LLM System for Internet-Scale Information Search and Extraction` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27221:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27221:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27221:end -->

<!-- review:SF-2026-ARXIV-2604-27233:start -->
#### Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-TOOL-CALLING` 中该 family 的受限状态。

机制与 state/control owner：We evaluate three collaboration mechanisms between a tool-calling agent and a reviewer agent: tool registry 拥有 capability/schema version，router 只选择候选，executor 保留授权

Evaluation contract：RQ3 (Latency & Deployment): What are the latency overhead and deployment trade-offs of inference-time feedback across different application scenarios?

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We introduce Reinforced Agent, an inference-time feedback mechanism for tool-calling agents. Evaluation on BFCL establishes baseline effectiveness and identifies over-skepticism as the primary reviewer error mode. Evaluation on τ 2 \tau^{2} -Bench demonstrates generalization to multi-turn scenarios. Our Helpfulness-Harmfulness metrics show reasoning models achieve favorable benefit-to-risk ratios as reviewers. Automated prompt optimization via GEPA systematizes reviewer improvement over manual engineering.…。因此若该限制在目标 workload 中触发，不能把 `Reinforced Agent: Inference-Time Feedback for Tool-Calling Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27233:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27233:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27233:end -->

<!-- review:SF-2026-ARXIV-2604-27238:start -->
#### SafeTune: Mitigating Data Poisoning in LLM Fine-Tuning for RTL Code Generation

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：SafeTune is a two-stage defense framework that sanitizes hardware-design corpora before fine-tuning RTL-generation LLMs. As illustrated in Fig. 1 , the framework jointly analyzes natural-language prompts and RTL structure to reduce the risk of backdoor inheritance from poisoned prompt-RTL pairs. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：We evaluate the proposed framework using a curated corpus of prompt–RTL pairs that includes both benign and Trojan-inserted designs. The dataset is partitioned into three disjoint subsets:1) 1,000 samples for classifier training, 2) 1,000 for LLM fine-tuning, and 3) 125 Trojan samples for evaluation. Benign samples are sourced from RTL++ [ 27 ] , while 70 hardware Trojan seeds from Trust-Hub [ 28 ] and recent studies [ 29 ] across five designs (AES, PIC, RSA, UART, SRAM) are expanded to 2,500 samples using ChatGPT-5.1.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We assume the attacker cannot alter the LLM architecture, optimization procedure, hyperparameters, loss function, or downstream verification tools. Their capability is limited to poisoning the training corpus by inserting malicious prompt-RTL pairs. The attack objective is to obtain a fine-tuned model f θ ′ f_{\theta^{\prime}} that preserves normal behavior on benign prompts while generating malicious RTL when the trigger is present.。因此若该限制在目标 workload 中触发，不能把 `SafeTune: Mitigating Data Poisoning in LLM Fine-Tuning for RTL Code Generation` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27238:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27238:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27238:end -->

<!-- review:SF-2026-ARXIV-2604-27249:start -->
#### Instruction Complexity Induces Positional Collapse in Adversarial LLM Evaluation

问题、旧路径与约束变化：旧路径把 `Instruction Complexity Induces Positional Collapse in Adversarial LLM Evaluation` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：When instructed to underperform on multiple-choice evaluations, do language models engage with question content or fall back on positional shortcuts? We map the boundary between these regimes using a six-condition adversarial instruction-specificity gradient administered to two instruction-tuned LLMs (Llama-3-8B and Llama-3.1-8B) on 2,000 MMLU-Pro items. Distributional screening (response-position entropy) and an independent content-engagement criterion (difficulty-accuracy correlation) jointly characterise each condition. When instructed to underperform on multiple-choice evaluations, do language models engage with question content or fall back on positional shortcuts? We map the boundary between these regimes using a six-condition adversarial instruction-specificity gradient administered to two instruction-tuned LLMs (Llama-3-8B and Llama-3.1-8B) on 2,000 MMLU-Pro items. Distributional screening (response-position entropy) and an independent content-engagement criterion (difficulty-accuracy correlation) jointly characterise each condition. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：When instructed to underperform on multiple-choice evaluations, do language models engage with question content or fall back on positional shortcuts? Results suggest that instruction complexity can determine whether adversarial compliance uses content-aware or content-blind mechanisms in small instruction-tuned LLMs under greedy decoding.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Instruction Complexity Induces Positional Collapse in Adversarial LLM Evaluation` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-27249:start -->只接受 arXiv:2604.27249v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-27249:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-27249:end -->

<!-- review:SF-2026-ARXIV-2604-27251:start -->
#### Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models

问题、旧路径与约束变化：旧路径未显式拥有 `MODEL-TRANSFORMER-LAYER` 中该 family 的受限状态。

机制与 state/control owner：We answer this question by evaluating a suite of state-of-the-art open-source and frontier LLMs across four datasets spanning three fundamental reasoning types: deduction, induction, and abduction (Table 1 ). Our experiments reveal that a reasoning conflict between compliance (i.e., reason according to the instruction) and sensibility (i.e., reason in line with the question) indeed exists: models often face a tension between the user’s reasoning instructions and their own internal priors. To understand this phenomenon, we provide a mechanistic analysis via probing to demonstrate that LLMs successfully encode and understand reasoning instructions in their middle-to-late layers. We show that the decision to comply or diverge is an active process that begins mid-computation. Finally, we use Contrastive Activation Addition (CAA) ( Rimsky et al., 2024 ) to showcase that reasoning compliance can be augmented during inference. Our contributions are as follows: layer graph 拥有 recurrent/residual state 与 normalization，runtime 只提交 exact schedule

Evaluation contract：Based on the probing results (Fig. 5 and Appendix D ), we can identify the middle layers as the primary site for encoding reasoning paradigms, we applied CAA to layers 14–17 of Olmo3-7B-IT . This model was specifically chosen for intervention due to its baseline status as the least compliant model in our study (Fig. 3 ). As shown in Fig. 6a , applying steering vectors with a positive multiplier ( μ \mu ) greatly increases the compliance rate, with the effect scaling alongside μ \mu . This is particularly evident when forcing inductive and deductive instructions on α ​ N ​ L ​ I \alpha NLI questions, where steering successfully overrides the model’s natural abductive inclination. However, the impact on task accuracy (Fig. 6b ) reveals a complex trade-off. For abductive instructions, accuracy drops as μ \mu increases; qualitative analysis suggests this is due to a “task-neglect” side effect, where the model becomes so focused on the steered reasoning type that it fails to follow formatting constraints (e.g., enclosing the final answer in the required tags). Interestingly, for inductive and deductive instructions, accuracy follows a non-monotonic trend: initially declining before reaching an upward peak as compliance is enforced. Finally, we observe that steering with a negative μ \mu consistently improves accuracy across all instruction types. Such “anti-steering” also makes LLMs resort to direct answer (Fig. 6c ), potentially reducing the cognitive friction caused by conflicting reasoning. More steering results on other datasets and models are in Appendix E .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We characterized the reasoning conflict in LLMs, showing that while LLMs successfully encode reasoning instructions in their middle-to-late layers, they often struggle to prioritize compliance. Our systematic evaluation reveals that this tension is an active, mid-computation process that varies significantly by model scale and architecture. Via CAA, we showed that this conflict is not an immutable limitation; rather, it can be mitigated through activation steering, which enhances instruction compliance by up to 29 % 29\% .…。因此若该限制在目标 workload 中触发，不能把 `Compliance versus Sensibility: On the Reasoning Controllability in Large Language Models` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27251:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27251:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27251:end -->

<!-- review:SF-2026-ARXIV-2604-27267:start -->
#### From Prompt to Physical Actuation: Holistic Threat Modeling of LLM-Enabled Robotic Systems

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：The model includes three edge-side data stores that retain security-relevant state across the planning pipeline. State/Session Memory (D1) stores task context and intermediate workflow state across planning cycles. Skill/Tool Library (D2) stores tool schemas, callable skills, and execution constraints available to the Orchestrator. Prompt and Policy Assets (D3) stores system prompts, few-shot examples, and safety or policy constraints used by the Prompt Builder. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：An adversary can manipulate the physical scene observed by P6’s onboard sensors through adversarial patches, deceptive signage, or modified terrain features, causing the perception pipeline to infer a false navigable environment (ATLAS AML.T0041, AML.T0043.003 [S/T]). Individual sensor modalities face targeted attacks: GPS spoofing corrupts localization (ATT&CK T1565.002 [T]), LiDAR phantom-point injection creates ghost obstacles (AML.T0043.003 [T]), and acoustic injection at the IMU’s resonant frequency falsifies angular-velocity measurements (AML.T0043.003 [T]). Camera blinding and broadband sensor jamming deny environmental perception entirely (T1499 [D]). Within TB2, a hardware interposer on the MIPI CSI camera bus can intercept and modify frames between the sensor module and SoC, bypassing all software-level integrity checks an attack demonstrated by Liu et al. [ 22 ] . Repudiation threats are consolidated in § IV-A .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Crossing (i): User–Edge Interface This interaction involves external entity E1 (User/Agent) and process P1 (User Interface), connected by two data flows: task instructions entering TB1 (DF1) and status feedback exiting TB1 (DF2). Because P1 is the system’s only operator-facing entry point, it concentrates both conventional cyber threats and LLM-directed conversational attacks at a single interface.。因此若该限制在目标 workload 中触发，不能把 `From Prompt to Physical Actuation: Holistic Threat Modeling of LLM-Enabled Robotic Systems` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27267:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27267:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27267:end -->

<!-- review:SF-2026-ARXIV-2604-27283:start -->
#### Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：The philosophical stance is the same—retrieval score alone is not a permission—but the failure surface differs. In general RAG, a bad passage produces a bad answer; in coding-agent memory, a bad memory produces operational damage that can persist across turns. That is why RSCB-MC exposes command, path, stack, and session-rejection signals to the controller: in the failure modes that motivated the system, those structural signals were the only ones that distinguished, e.g., a stale-migration episode from a database-lock episode after the surface error message had already collided. memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图

Evaluation contract：This boundary is deliberate. The paper evaluates the memory-control mechanism, not the full repair quality of an arbitrary production LLM agent. Offline replay and bounded hot-path validation are useful for testing safety, latency, and policy behavior, but they are not causal online counterfactual experiments.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The philosophical stance is the same—retrieval score alone is not a permission—but the failure surface differs. In general RAG, a bad passage produces a bad answer; in coding-agent memory, a bad memory produces operational damage that can persist across turns. That is why RSCB-MC exposes command, path, stack, and session-rejection signals to the controller: in the failure modes that motivated the system, those structural signals were the only ones that distinguished, e.g., a stale-migration episode from a database-lock episode after the surface error message had already collided.。因此若该限制在目标 workload 中触发，不能把 `Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-27283:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-27283:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27283:end -->

<!-- review:SF-2026-ARXIV-2604-27289:start -->
<!-- claim:SF-2026-ARXIV-2604-27289:start -->
结构化治理把模型产生的 intent 与真实 effect 分离：纯计算只能产生 typed directive，唯一 effect interpreter 执行 authorization、capability check 与 provenance；安全命题因此落在可枚举的执行边界，而不是要求模型行为本身可判定。
<!-- claim:SF-2026-ARXIV-2604-27289:end -->
#### Mechanized Foundations of Structural Governance: Machine-Checked Proofs for Governed Intelligence

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2.2-3.3 event types, governance operator and coinductive safety predicate; §8 mechanization; §9 verified interpreter specification`。
- **Mechanism / ownership:** 结构化治理把模型产生的 intent 与真实 effect 分离：纯计算只能产生 typed directive，唯一 effect interpreter 执行 authorization、capability check 与 provenance；安全命题因此落在可枚举的执行边界，而不是要求模型行为本身可判定。
- **Evaluation contract:** `§8.3-8.5 36 Coq modules/454 results/zero admitted lemmas; §9 property-based conformance against BEAM runtime`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§12 Limitations：formalization is system-specific; two named results remain paper proofs; proof covers the modeled effect boundary and does not establish policy correctness or arbitrary runtime behavior`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27289:end -->

<!-- review:SF-2026-ARXIV-2604-27292:start -->
<!-- claim:SF-2026-ARXIV-2604-27292:start -->
Effect governance 的覆盖边界必须与系统可表达的 effect 边界重合；与其对 Turing-complete 行为做不可判定的语义过滤，不如把 computation 与 effect 分离，只对 typed directive 的 capability 与 policy 做可判定检查。
<!-- claim:SF-2026-ARXIV-2604-27292:end -->
#### The Two Boundaries: Why Behavioral AI Governance Fails Structurally

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 expressiveness/governance boundaries, Rice-theorem boundary and coterminous governance; §5-7 behavioral comparison and execution-pipeline consequence`。
- **Mechanism / ownership:** Effect governance 的覆盖边界必须与系统可表达的 effect 边界重合；与其对 Turing-complete 行为做不可判定的语义过滤，不如把 computation 与 effect 分离，只对 typed directive 的 capability 与 policy 做可判定检查。
- **Evaluation contract:** `§4 gives the testable structural criterion; formal claims defer to the companion Coq development rather than an independent empirical benchmark`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§9 Limitations：scope is effects, existing frameworks may require re-architecture, structural coverage does not prove policy correctness, and restricted languages trade expressiveness for decidability`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27292:end -->

<!-- review:SF-2026-ARXIV-2604-27306:start -->
<!-- claim:SF-2026-ARXIV-2604-27306:start -->
可维护 RAG 的 retrieval object 不应只是 passage：带 evidence、validity interval 与 lifecycle state 的 atomic nugget 让失效事实在 ranking 前退出，并把来源冲突变成显式状态。
<!-- claim:SF-2026-ARXIV-2604-27306:end -->
#### NuggetIndex: Governed Atomic Retrieval for Maintainable RAG

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 nugget schema, lifecycle and retrieval pipeline`。
- **Mechanism / ownership:** 可维护 RAG 的 retrieval object 不应只是 passage：带 evidence、validity interval 与 lifecycle state 的 atomic nugget 让失效事实在 ranking 前退出，并把来源冲突变成显式状态。
- **Evaluation contract:** `§5 three QA datasets, maintenance/update evaluation and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6/§7 selected QA corpora and author metrics do not prove a universal source-authority policy`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-RAG`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27306:end -->

<!-- review:SF-2026-ARXIV-2604-27309:start -->
<!-- claim:SF-2026-ARXIV-2604-27309:start -->
一次性 benchmark 不能拥有 release authority；部署中的 rubric、用户反馈、运行 SLO、成本和受控版本实验必须形成持续、可追溯的发布控制回路。
<!-- claim:SF-2026-ARXIV-2604-27309:end -->
#### End-to-End Evaluation and Governance of an EHR-Embedded AI Agent for Clinicians

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§5.1-5.8 governance architecture, controlled experimentation, monitoring and cost`。
- **Mechanism / ownership:** 一次性 benchmark 不能拥有 release authority；部署中的 rubric、用户反馈、运行 SLO、成本和受控版本实验必须形成持续、可追溯的发布控制回路。
- **Evaluation contract:** `§2.1-2.6 seven versions, clinician rubrics, live feedback and technical performance`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§3.6 single product/domain, observational feedback and short deployment window`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27309:end -->

<!-- review:SF-2026-ARXIV-2604-27351:start -->
<!-- claim:SF-2026-ARXIV-2604-27351:start -->
异构 scientific foundation models 可通过 typed specialist tools 协作；language model 负责 decomposition/routing，领域模型保留输入输出语义与 artifact authority。
<!-- claim:SF-2026-ARXIV-2604-27351:end -->
#### Heterogeneous Scientific Foundation Model Collaboration

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 heterogeneous model collaboration and typed tool interface`。
- **Mechanism / ownership:** 异构 scientific foundation models 可通过 typed specialist tools 协作；language model 负责 decomposition/routing，领域模型保留输入输出语义与 artifact authority。
- **Evaluation contract:** `§4 scientific task evaluations and collaboration ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§5 selected scientific models/tasks do not establish a universal planner or tool ontology`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `AGENT-TOOL-CALLING`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27351:end -->

<!-- review:SF-2026-ARXIV-2604-27358:start -->
<!-- claim:SF-2026-ARXIV-2604-27358:start -->
Delegation degree 是运行时控制变量而非静态拓扑：bilevel controller 在效用与 safety constraint 间调节子代理权限，并要求 responsibility propagation 可验证。
<!-- claim:SF-2026-ARXIV-2604-27358:end -->
#### Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 bilevel delegation objective, safety monotonicity and responsibility propagation`。
- **Mechanism / ownership:** Delegation degree 是运行时控制变量而非静态拓扑：bilevel controller 在效用与 safety constraint 间调节子代理权限，并要求 responsibility propagation 可验证。
- **Evaluation contract:** `§5 formal convergence/safety analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 explicitly leaves empirical validation to future work; formal assumptions do not prove deployable runtime safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-MULTI-AGENT`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27358:end -->

<!-- review:SF-2026-ARXIV-2604-27393:start -->
<!-- claim:SF-2026-ARXIV-2604-27393:start -->
全双工 omni-modal interaction 把音频、视觉与文本从离线拼接改成持续 streaming state；turn-taking、interruption 与 concurrent perception/generation 成为第一等 runtime contract。
<!-- claim:SF-2026-ARXIV-2604-27393:end -->
#### MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 native omni-modal architecture, full-duplex streaming and training`。
- **Mechanism / ownership:** 全双工 omni-modal interaction 把音频、视觉与文本从离线拼接改成持续 streaming state；turn-taking、interruption 与 concurrent perception/generation 成为第一等 runtime contract。
- **Evaluation contract:** `§4 multimodal understanding/generation and streaming interaction evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: model-specific training data, hardware and latency conditions bound the reported interaction quality`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `MULTIMODAL-REPRESENTATION`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27393:end -->

<!-- review:SF-2026-ARXIV-2604-27396:start -->
<!-- claim:SF-2026-ARXIV-2604-27396:start -->
VitaLLM 以 ternary/INT 双核心、leading-one KV fetch pruning 与 dependency-aware head pipeline 将 prefill/decode 的不同瓶颈映射到 phase-aware accelerator plan；prototype 证明特定 BitNet workload 可行，但不授予跨硬件通用执行结论。
<!-- claim:SF-2026-ARXIV-2604-27396:end -->
#### VitaLLM: A Versatile, Ultra-Compact Ternary LLM Accelerator with Dependency-Aware Scheduling

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§II-III heterogeneous dual-core architecture, leading-one predictor and dependency-aware system integration`。
- **Mechanism / ownership:** VitaLLM 以 ternary/INT 双核心、leading-one KV fetch pruning 与 dependency-aware head pipeline 将 prefill/decode 的不同瓶颈映射到 phase-aware accelerator plan；prototype 证明特定 BitNet workload 可行，但不授予跨硬件通用执行结论。
- **Evaluation contract:** `§IV 16nm prototype, BitNet b1.58 3B prefill/decode and ablation evaluation`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§IV evidence is bound to one 16nm prototype, LPDDR5-class memory, BitNet b1.58 3B and disclosed sequence settings; it does not prove cross-model or cross-accelerator portability`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `INFER-TENSORRT-LLM`；Score V2 `2/3/2` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27396:end -->

<!-- review:SF-2026-ARXIV-2604-27405:start -->
<!-- claim:SF-2026-ARXIV-2604-27405:start -->
版本平均分会掩盖 item-level 双向 churn；release gate 需要 within-model reliable change、sampling variance 与 harmed/helped item ledger，而不是只比较 aggregate delta。
<!-- claim:SF-2026-ARXIV-2604-27405:end -->
#### Beyond the Mean: Within-Model Reliable Change Detection for LLM Evaluation

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 item-level Reliable Change Index adaptation and within-family comparison`。
- **Mechanism / ownership:** 版本平均分会掩盖 item-level 双向 churn；release gate 需要 within-model reliable change、sampling variance 与 harmed/helped item ledger，而不是只比较 aggregate delta。
- **Evaluation contract:** `§4 2,000 MMLU-Pro items, 10 samples and two model-family upgrades`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: two families and one benchmark do not calibrate a universal RCI threshold or production consequence`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27405:end -->

<!-- review:SF-2026-ARXIV-2604-27419:start -->
<!-- claim:SF-2026-ARXIV-2604-27419:start -->
Website-agent evaluation must preserve interactive feedback, intermediate artifacts and repair loops; static final-page similarity cannot prove executable workflow correctness.
<!-- claim:SF-2026-ARXIV-2604-27419:end -->
#### InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 benchmark environment, interaction protocol and graders`。
- **Mechanism / ownership:** Website-agent evaluation must preserve interactive feedback, intermediate artifacts and repair loops; static final-page similarity cannot prove executable workflow correctness.
- **Evaluation contract:** `§4 multimodal web-agent baselines and error analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: website-generation tasks and benchmark fixtures do not establish general computer-use reliability`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27419:end -->

<!-- review:SF-2026-ARXIV-2604-27426:start -->
<!-- claim:SF-2026-ARXIV-2604-27426:start -->
Local/offline fine-tuning is not a privacy boundary when model repository code owns the executable training path; artifact provenance, sandboxing and egress control must precede dataset access. May steal training secrets.
<!-- claim:SF-2026-ARXIV-2604-27426:end -->
#### Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 malicious model-code supply-chain path and active execution hijacking`。
- **Mechanism / ownership:** Local/offline fine-tuning is not a privacy boundary when model repository code owns the executable training path; artifact provenance, sandboxing and egress control must precede dataset access. May steal training secrets.
- **Evaluation contract:** `§5 secret-exfiltration experiments across local fine-tuning setups`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: demonstrated attacks do not establish ecosystem prevalence; controls depend on the actual loader/runtime boundary`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27426:end -->

<!-- review:SF-2026-ARXIV-2604-27467:start -->
<!-- claim:SF-2026-ARXIV-2604-27467:start -->
代码 verifier 不是附属脚本，而是训练与评测共享的 evidence runtime：special-judge synthesis、test-case parallelism、multi-node sandbox 和配置化 suite 共同决定 reward truth、吞吐与可复现性。
<!-- claim:SF-2026-ARXIV-2604-27467:end -->
#### ScaleBox: Enabling High-Fidelity and Scalable Code Verification for Large Language Models

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§4-5 ScaleBox architecture, automated special-judge generation, distributed sandbox execution and configuration-driven suite`。
- **Mechanism / ownership:** 代码 verifier 不是附属脚本，而是训练与评测共享的 evidence runtime：special-judge synthesis、test-case parallelism、multi-node sandbox 和配置化 suite 共同决定 reward truth、吞吐与可复现性。
- **Evaluation contract:** `§5.2 and §6 verification accuracy/throughput plus RLVR training evaluation`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Limitations: generated judges, selected code tasks, sandbox policies and author infrastructure do not prove arbitrary-program correctness or universal RL stability`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27467:end -->

<!-- review:SF-2026-ARXIV-2604-27486:start -->
<!-- claim:SF-2026-ARXIV-2604-27486:start -->
GPU binary lifting 的关键不是语法翻译，而是从统一 register file 恢复 typed state、显式 control flow 与 multi-instruction semantics；conflict detection 决定何时必须拒绝生成可执行 IR。
<!-- claim:SF-2026-ARXIV-2604-27486:end -->
#### CuLifter: Lifting GPU Binaries to Typed IR

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 SASS decoding, type-constraint propagation with conflict detection, control-flow reconstruction and multi-instruction aggregation`。
- **Mechanism / ownership:** GPU binary lifting 的关键不是语法翻译，而是从统一 register file 恢复 typed state、显式 control flow 与 multi-instruction semantics；conflict detection 决定何时必须拒绝生成可执行 IR。
- **Evaluation contract:** `§6 eight suites, 24,437 GPU functions, valid-IR and x86 semantic-pass evaluation plus ablation`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 evaluation cannot validate MUFU, texture or full SIMT behavior through an x86 backend; supported architectures/instructions bound correctness and require fail-closed handling`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-TENSORRT-LLM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27486:end -->

<!-- review:SF-2026-ARXIV-2604-27488:start -->
<!-- claim:SF-2026-ARXIV-2604-27488:start -->
Skill evolution 需要 versioned proposal、comparative execution、traceable judge evidence 与 rollback；training-free optimization 不能让生成者同时拥有发布 authority。
<!-- claim:SF-2026-ARXIV-2604-27488:end -->
#### Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 Skills-Coach task generation, comparative execution and GRPO-style skill optimization`。
- **Mechanism / ownership:** Skill evolution 需要 versioned proposal、comparative execution、traceable judge evidence 与 rollback；training-free optimization 不能让生成者同时拥有发布 authority。
- **Evaluation contract:** `§4 agent-skill benchmarks, ablations and trace analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: author-generated tasks/judges and selected skills do not prove production release safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-PLATFORM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27488:end -->

<!-- review:SF-2026-ARXIV-2604-27536:start -->
<!-- claim:SF-2026-ARXIV-2604-27536:start -->
黑盒服务的 stronger-path escalation 是部分可观测的预算决策：controller 必须由 verifiable observation 更新 belief，并把 expected reliability gain 与增量推理成本联合 admission。
<!-- claim:SF-2026-ARXIV-2604-27536:end -->
#### Belief-Guided Inference Control for Large Language Model Services via Verifiable Observations

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 POMDP formulation, verifiable observations and belief-guided routing`。
- **Mechanism / ownership:** 黑盒服务的 stronger-path escalation 是部分可观测的预算决策：controller 必须由 verifiable observation 更新 belief，并把 expected reliability gain 与增量推理成本联合 admission。
- **Evaluation contract:** `§5 service workloads, cost/reliability baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: proxy-verifier calibration and workload stationarity limit generalization to unseen services`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27536:end -->

<!-- review:SF-2026-ARXIV-2604-27586:start -->
<!-- claim:SF-2026-ARXIV-2604-27586:start -->
Agent contamination is a trace property: uncertain evidence can alter decomposition/routing before appearing in the final answer, so provenance must follow artifact transformations and control-flow divergence across steps.
<!-- claim:SF-2026-ARXIV-2604-27586:end -->
#### Trace-Level Analysis of Information Contamination in Multi-Agent Systems

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 trace-level contamination model, artifact transformations and divergence measures`。
- **Mechanism / ownership:** Agent contamination is a trace property: uncertain evidence can alter decomposition/routing before appearing in the final answer, so provenance must follow artifact transformations and control-flow divergence across steps.
- **Evaluation contract:** `§4 heterogeneous-document workflows and contamination interventions`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic workflows and chosen corruption models do not quantify real-world prevalence or causal completeness`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-TRACE`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27586:end -->

<!-- review:SF-2026-ARXIV-2604-27637:start -->
<!-- claim:SF-2026-ARXIV-2604-27637:start -->
Cross-model evaluation must distinguish a frozen common-prompt contract from a per-model optimized deployment contract; otherwise prompt mismatch can change rankings and misattribute interface quality to model weights.
<!-- claim:SF-2026-ARXIV-2604-27637:end -->
#### Optimization before Evaluation: Evaluation with Unoptimised Prompts Can be Misleading

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 per-model prompt-optimization protocol before evaluation`。
- **Mechanism / ownership:** Cross-model evaluation must distinguish a frozen common-prompt contract from a per-model optimized deployment contract; otherwise prompt mismatch can change rankings and misattribute interface quality to model weights.
- **Evaluation contract:** `§4 model/task ranking changes under optimized versus static prompts`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected optimizers, tasks and search budgets do not define a universally fair evaluation regime`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27637:end -->

<!-- review:SF-2026-ARXIV-2604-27660:start -->
<!-- claim:SF-2026-ARXIV-2604-27660:start -->
Inference-time skill extraction converts context into a replayable procedure and then selects whether to reuse it; derived skill state must remain linked to source context and evaluation evidence.
<!-- claim:SF-2026-ARXIV-2604-27660:end -->
#### From Context to Skills: Can Language Models Learn from Context Skillfully?

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 context-to-skill extraction, self-play generation and replay selection`。
- **Mechanism / ownership:** Inference-time skill extraction converts context into a replayable procedure and then selects whether to reuse it; derived skill state must remain linked to source context and evaluation evidence.
- **Evaluation contract:** `§4 task suites, baselines and skill-transfer ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected tasks/models do not establish durable skill validity or safe cross-domain reuse`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-CONTEXT`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27660:end -->

<!-- review:SF-2026-ARXIV-2604-27695:start -->
<!-- claim:SF-2026-ARXIV-2604-27695:start -->
Long-term memory retrieval should diagnose an evidence gap before issuing the next query; iterative retrieval state must record known evidence, missing relation and stop/abstain criteria rather than only rewrite queries.
<!-- claim:SF-2026-ARXIV-2604-27695:end -->
#### EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 evidence-gap diagnosis, layered memory and iterative retrieval controller`。
- **Mechanism / ownership:** Long-term memory retrieval should diagnose an evidence gap before issuing the next query; iterative retrieval state must record known evidence, missing relation and stop/abstain criteria rather than only rewrite queries.
- **Evaluation contract:** `§4 long-conversation temporal/multi-hop benchmarks and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: benchmark conversations and author-defined gap labels do not prove production memory truthfulness`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-MEMORY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27695:end -->

<!-- review:SF-2026-ARXIV-2604-27707:start -->
<!-- claim:SF-2026-ARXIV-2604-27707:start -->
Retrieval memo and weight consolidation are different state transitions: the former changes accessible context, the latter changes generalizing parameters and therefore poisoning, rollback and provenance boundaries.
<!-- claim:SF-2026-ARXIV-2604-27707:end -->
#### Contextual Agentic Memory is a Memo, Not True Memory

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 formal memo-versus-memory distinction and consolidation consequences`。
- **Mechanism / ownership:** Retrieval memo and weight consolidation are different state transitions: the former changes accessible context, the latter changes generalizing parameters and therefore poisoning, rollback and provenance boundaries.
- **Evaluation contract:** `Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; conceptual analysis and cited examples; no independent systems benchmark`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: position paper does not demonstrate a universally superior consolidation mechanism`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-MEMORY`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27707:end -->

<!-- review:SF-2026-ARXIV-2604-27711:start -->
<!-- claim:SF-2026-ARXIV-2604-27711:start -->
Exocentric video generation can propose interaction-rich humanoid motion, but generated trajectories remain proposals until a controller, embodiment calibration and environment feedback commit physical actions.
<!-- claim:SF-2026-ARXIV-2604-27711:end -->
#### ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 exocentric generation and control pipeline`。
- **Mechanism / ownership:** Exocentric video generation can propose interaction-rich humanoid motion, but generated trajectories remain proposals until a controller, embodiment calibration and environment feedback commit physical actions.
- **Evaluation contract:** `§4 simulated and physical humanoid evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: video quality and selected tasks do not establish broad physical safety or sim-to-real robustness`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `MULTIMODAL-EMBODIED-VLA`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27711:end -->

<!-- review:SF-2026-ARXIV-2604-27776:start -->
<!-- claim:SF-2026-ARXIV-2604-27776:start -->
Professional GUI-agent evaluation must preserve cross-application process state, artifact handoffs and terminal evidence; per-app task success misses workflow-level recovery and consistency.
<!-- claim:SF-2026-ARXIV-2604-27776:end -->
#### WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 cross-application Windows environment and process-centric tasks`。
- **Mechanism / ownership:** Professional GUI-agent evaluation must preserve cross-application process state, artifact handoffs and terminal evidence; per-app task success misses workflow-level recovery and consistency.
- **Evaluation contract:** `§4 agent baselines, process/terminal grading and error taxonomy`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: Windows applications and curated professions do not represent every production workspace`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27776:end -->

<!-- review:SF-2026-ARXIV-2604-27781:start -->
<!-- claim:SF-2026-ARXIV-2604-27781:start -->
AI software supply chain 必须跨 data、training、inference 与 substrate 维护 verifiability、versioning、observability 和 traceability；依赖数量只是暴露面证据，不能替代运行时 provenance 或 release gate。
<!-- claim:SF-2026-ARXIV-2604-27781:end -->
#### The Grand Software Supply Chain of AI Systems

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-5 four-layer AI supply-chain decomposition, integrity gaps and lifecycle requirements`。
- **Mechanism / ownership:** AI software supply chain 必须跨 data、training、inference 与 substrate 维护 verifiability、versioning、observability 和 traceability；依赖数量只是暴露面证据，不能替代运行时 provenance 或 release gate。
- **Evaluation contract:** `§5.1 reference-stack measurement across 48 projects, direct/transitive dependencies and source size`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 provides a conceptual decomposition and ecosystem measurement, not a controlled security evaluation or proof that every dependency is exercised at runtime`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27781:end -->

<!-- review:SF-2026-ARXIV-2604-27789:start -->
<!-- claim:SF-2026-ARXIV-2604-27789:start -->
Opaque provider updates require a deployer-owned compatibility contract: frozen risk suites, behavioral diff, canary and rollback gates must mediate even when the provider reuses the same model name.
<!-- claim:SF-2026-ARXIV-2604-27789:end -->
#### Test Before You Deploy: Governing Updates in the LLM Supply Chain

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 deployer contracts, update detection and compatibility-gate workflow`。
- **Mechanism / ownership:** Opaque provider updates require a deployer-owned compatibility contract: frozen risk suites, behavioral diff, canary and rollback gates must mediate even when the provider reuses the same model name.
- **Evaluation contract:** `Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; case studies and risk-suite demonstrations over hosted model changes`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: framework cannot observe undisclosed provider internals and depends on representative local suites`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-PRODUCTION`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27789:end -->

<!-- review:SF-2026-ARXIV-2604-27792:start -->
<!-- claim:SF-2026-ARXIV-2604-27792:start -->
World-action model 把 future visual state 与 action 放入联合生成路径，可减少 VGM→IDM 串行误差；但真正的 physical authority 仍属于 controller、safety envelope 与环境反馈。
<!-- claim:SF-2026-ARXIV-2604-27792:end -->
#### Motubrain: An Advanced World Action Model for Robot Control

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2 architecture, heterogeneous pre/post-training and real-time inference optimizations`。
- **Mechanism / ownership:** World-action model 把 future visual state 与 action 放入联合生成路径，可减少 VGM→IDM 串行误差；但真正的 physical authority 仍属于 controller、safety envelope 与环境反馈。
- **Evaluation contract:** `§3 simulation, world-model and real-robot evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§4 future work; no independent safety or broad sim-to-real guarantee`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `MULTIMODAL-EMBODIED-VLA`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27792:end -->

<!-- review:SF-2026-ARXIV-2604-27819:start -->
<!-- claim:SF-2026-ARXIV-2604-27819:start -->
Multi-server MCP safety is an information-flow problem: individually permitted read/write tools can compose into a cross-boundary leak, so canary taint must survive tool-call edges and server identities.
<!-- claim:SF-2026-ARXIV-2604-27819:end -->
#### MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 MCPHunt canary injection, multi-server topology and taint tracking`。
- **Mechanism / ownership:** Multi-server MCP safety is an information-flow problem: individually permitted read/write tools can compose into a cross-boundary leak, so canary taint must survive tool-call edges and server identities.
- **Evaluation contract:** `§4 server/tool compositions, models and leak-detection evaluation`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic canaries and enumerated servers do not prove complete semantic non-interference`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-MCP`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27819:end -->

<!-- review:SF-2026-ARXIV-2604-27844:start -->
<!-- claim:SF-2026-ARXIV-2604-27844:start -->
通信压缩只有在 encode/decode 不把 network bottleneck 迁移为 GPU critical-path bottleneck 时才成立；lossless exponent coding 与 collective-aware layout 以 bit-exactness 换取数据分布假设和额外 kernel/switcher 控制状态。
<!-- claim:SF-2026-ARXIV-2604-27844:end -->
#### ZipCCL: Efficient Lossless Data Compression of Communication Collectives for Accelerating LLM Training

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 compressed collective API, exponent coding, GPU pipeline and adaptive switcher`。
- **Mechanism / ownership:** 通信压缩只有在 encode/decode 不把 network bottleneck 迁移为 GPU critical-path bottleneck 时才成立；lossless exponent coding 与 collective-aware layout 以 bit-exactness 换取数据分布假设和额外 kernel/switcher 控制状态。
- **Evaluation contract:** `§6 dense/MoE training on 64 GPUs with collective and end-to-end comparisons`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6.6 observed tensor normality is workload-specific; paper does not prove universal distributions`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `TRAIN-DISTRIBUTED-TRAINING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27844:end -->

<!-- review:SF-2026-ARXIV-2604-27855:start -->
<!-- claim:SF-2026-ARXIV-2604-27855:start -->
Inference placement may treat energy geography as a scheduling input only after latency, state locality, capacity and regulation become hard constraints; cheap power alone cannot own routing authority.
<!-- claim:SF-2026-ARXIV-2604-27855:end -->
#### AI Inference as Relocatable Electricity Demand: A Latency-Constrained Energy-Geography Framework

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 latency-constrained energy-geography model and placement formulation`。
- **Mechanism / ownership:** Inference placement may treat energy geography as a scheduling input only after latency, state locality, capacity and regulation become hard constraints; cheap power alone cannot own routing authority.
- **Evaluation contract:** `Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; regional scenarios and sensitivity analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: analytical inputs and assumed relocatability are not measured production traces or universal grid emissions`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-COST`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27855:end -->

<!-- review:SF-2026-ARXIV-2604-27861:start -->
<!-- claim:SF-2026-ARXIV-2604-27861:start -->
分解式 jailbreak 的风险状态可跨匿名、交错请求累积；TwinGate 用 asymmetric contrastive state 将 topical overlap 与 shared malicious intent 分离，但它仍只是 detector proposal，不能替代 effect mediation。
<!-- claim:SF-2026-ARXIV-2604-27861:end -->
#### TwinGate: Stateful Defense against Decompositional Jailbreaks in Untraceable Traffic via Asymmetric Contrastive Learning

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 asymmetric contrastive dual-encoder state, frozen benign encoder and causal online monitoring`。
- **Mechanism / ownership:** 分解式 jailbreak 的风险状态可跨匿名、交错请求累积；TwinGate 用 asymmetric contrastive state 将 topical overlap 与 shared malicious intent 分离，但它仍只是 detector proposal，不能替代 effect mediation。
- **Evaluation contract:** `§5 strictly causal evaluation over 3.62M instructions and 8,600 malicious intents, including adaptive attacks`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected generated/curated intents and latent-space clustering do not prove complete intent reconstruction, universal low false-positive operation or action-level safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27861:end -->

<!-- review:SF-2026-ARXIV-2604-27878:start -->
<!-- claim:SF-2026-ARXIV-2604-27878:start -->
Simulator evaluation must separate behavioral realism from tester reliability：像不像真人与能否保持系统 ranking 是两个可能冲突的 contract，必须共享 canonical session schema、loss accounting 与 runtime applicability metadata。
<!-- claim:SF-2026-ARXIV-2604-27878:end -->
#### SimEval-IR: A Unified Toolkit and Benchmark Suite for Evaluating User Simulators and Search Sessions

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 canonical session schema, adapters and loss accounting; §4-5 realism and tester-reliability benchmark design`。
- **Mechanism / ownership:** Simulator evaluation must separate behavioral realism from tester reliability：像不像真人与能否保持系统 ranking 是两个可能冲突的 contract，必须共享 canonical session schema、loss accounting 与 runtime applicability metadata。
- **Evaluation contract:** `§6 four datasets, two languages, four simulator families and ranking-reliability analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§8 Limitations: dataset/language/simulator coverage is finite; correlations do not prove causal transfer to production users or unseen retrieval systems`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27878:end -->

<!-- review:SF-2026-ARXIV-2604-27891:start -->
<!-- claim:SF-2026-ARXIV-2604-27891:start -->
External orchestration is an alternative branch, not a default: when the full procedure fits context and the model can track it, in-context self-routing removes routing calls and fragmentation; durable side effects, audit and restart still require external workflow state.
<!-- claim:SF-2026-ARXIV-2604-27891:end -->
#### In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2 directed procedures and controlled LangGraph versus in-context conditions`。
- **Mechanism / ownership:** External orchestration is an alternative branch, not a default: when the full procedure fits context and the model can track it, in-context self-routing removes routing calls and fragmentation; durable side effects, audit and restart still require external workflow state.
- **Evaluation contract:** `§3 1,200 conversations across three procedural domains with two judge families`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§5.2-5.3 three simulated customer-service domains, LLM judges and frontier-model capability bound the conclusion; token cost is higher in-context`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `AGENT-WORKFLOW`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-27891:end -->

<!-- review:SF-2026-ARXIV-2604-27906:start -->
<!-- claim:SF-2026-ARXIV-2604-27906:start -->
Persistent memory write is a schema-governed state transition: extraction, validation, conflict/update policy and retry must precede commit; semantic retrieval alone cannot guarantee exact current state.
<!-- claim:SF-2026-ARXIV-2604-27906:end -->
#### From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 schema-aware iterative extraction, validation gates and retry path`。
- **Mechanism / ownership:** Persistent memory write is a schema-governed state transition: extraction, validation, conflict/update policy and retry must precede commit; semantic retrieval alone cannot guarantee exact current state.
- **Evaluation contract:** `§4 memory extraction/update tasks and component ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected schemas and LLM judges do not prove arbitrary-domain completeness or truth`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-MEMORY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-27906:end -->

<!-- review:SF-2026-ARXIV-2604-28056:start -->
<!-- claim:SF-2026-ARXIV-2604-28056:start -->
LLM-generated reward hypotheses should fork from a shared checkpoint, pass competence-aware verification and deploy by training phase; generation quality does not grant reward release authority.
<!-- claim:SF-2026-ARXIV-2604-28056:end -->
#### RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 RHyVE reward-hypothesis generation, verification and phase-aware deployment`。
- **Mechanism / ownership:** LLM-generated reward hypotheses should fork from a shared checkpoint, pass competence-aware verification and deploy by training phase; generation quality does not grant reward release authority.
- **Evaluation contract:** `§4 RL environments, reward baselines, ablations and competence analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected environments and verifier signals do not prove reward correctness or prevent all specification gaming`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `TRAIN-RLHF`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28056:end -->

<!-- review:SF-2026-ARXIV-2604-28123:start -->
<!-- claim:SF-2026-ARXIV-2604-28123:start -->
SFT→RLVR is not a neutral handoff when SFT shifts the policy distribution; black-box on-policy distillation can insert a pre-alignment bridge, trading extra rollout/teacher cost for a better RL starting distribution.
<!-- claim:SF-2026-ARXIV-2604-28123:end -->
#### Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 PRISM black-box on-policy distillation between SFT and RLVR`。
- **Mechanism / ownership:** SFT→RLVR is not a neutral handoff when SFT shifts the policy distribution; black-box on-policy distillation can insert a pre-alignment bridge, trading extra rollout/teacher cost for a better RL starting distribution.
- **Evaluation contract:** `§4 multimodal reasoning tasks, baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected models/tasks and teacher access do not establish universal benefit or cost efficiency`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `TRAIN-RLHF`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28123:end -->

<!-- review:SF-2026-ARXIV-2604-28129:start -->
<!-- claim:SF-2026-ARXIV-2604-28129:start -->
Multi-turn attacks may be benign turn-by-turn yet form a residual-activation trajectory; adaptive probes add a model-specific internal signal but cannot replace effect mediation or cross-version recalibration.
<!-- claim:SF-2026-ARXIV-2604-28129:end -->
#### Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 activation-trajectory probes and adaptive multi-turn detector`。
- **Mechanism / ownership:** Multi-turn attacks may be benign turn-by-turn yet form a residual-activation trajectory; adaptive probes add a model-specific internal signal but cannot replace effect mediation or cross-version recalibration.
- **Evaluation contract:** `§4 attack phases, model families, baselines and transfer tests`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: white-box activations and model-specific probes limit hosted-model use and require recalibration after updates`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28129:end -->

<!-- review:SF-2026-ARXIV-2604-28138:start -->
<!-- claim:SF-2026-ARXIV-2604-28138:start -->
Agent recovery state 不等于 chat history：tool side effects、filesystem、process 与 runtime artifact 必须在 turn boundary 形成可提交 checkpoint；语义稀疏检测减少 checkpoint traffic，却引入 eBPF 分类误差、co-location contention 与 restore consistency。
<!-- claim:SF-2026-ARXIV-2604-28138:end -->
#### Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§4-6 coordinator, eBPF inspector, C/R data plane and deployment refinement`。
- **Mechanism / ownership:** Agent recovery state 不等于 chat history：tool side effects、filesystem、process 与 runtime artifact 必须在 turn boundary 形成可提交 checkpoint；语义稀疏检测减少 checkpoint traffic，却引入 eBPF 分类误差、co-location contention 与 restore consistency。
- **Evaluation contract:** `§7 correctness, overhead, mechanism ablations and code-agent case study`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§9 Conclusion — exact-v1 has no dedicated limitations section; evidence is confined to Linux sandbox workloads and evaluated C/R backends`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `AGENT-PLATFORM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28138:end -->

<!-- review:SF-2026-ARXIV-2604-28139:start -->
<!-- claim:SF-2026-ARXIV-2604-28139:start -->
Live agent benchmark 必须同时冻结 refreshable demand signal 与可复现实验 snapshot，并优先用 service/workspace terminal evidence 验证 action，而不是把 final response 或单一 leaderboard 当完成证明。
<!-- claim:SF-2026-ARXIV-2604-28139:end -->
#### Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 refreshable signals, release snapshot, controlled fixtures and graders`。
- **Mechanism / ownership:** Live agent benchmark 必须同时冻结 refreshable demand signal 与可复现实验 snapshot，并优先用 service/workspace terminal evidence 验证 action，而不是把 final response 或单一 leaderboard 当完成证明。
- **Evaluation contract:** `§4-5 105 tasks, 13 models, trace/artifact grading and family-level analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§3.3 and §5.5 current release and ClawHub-derived demand are not a universal production distribution`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-28139:end -->

<!-- review:SF-2026-ARXIV-2604-28157:start -->
<!-- claim:SF-2026-ARXIV-2604-28157:start -->
Efficient red teaming can reuse prefix/cache and structured mutation state, but computational acceleration does not change the separation between attack discovery, evidence validation and release authority.
<!-- claim:SF-2026-ARXIV-2604-28157:end -->
#### FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 FlashRT red-team search and cache/memory optimizations`。
- **Mechanism / ownership:** Efficient red teaming can reuse prefix/cache and structured mutation state, but computational acceleration does not change the separation between attack discovery, evidence validation and release authority.
- **Evaluation contract:** `§4 prompt-injection/knowledge-corruption workloads, systems measurements and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: attack suites and author hardware do not establish full threat coverage or production prevalence`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-28157:end -->

<!-- review:SF-2026-ARXIV-2604-28158:start -->
<!-- claim:SF-2026-ARXIV-2604-28158:start -->
Methodological evolution graphs represent typed method relations rather than citation adjacency, enabling research workflows to reason about why techniques branch, replace or compose.
<!-- claim:SF-2026-ARXIV-2604-28158:end -->
#### Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 method-evolution ontology, extraction and graph construction`。
- **Mechanism / ownership:** Methodological evolution graphs represent typed method relations rather than citation adjacency, enabling research workflows to reason about why techniques branch, replace or compose.
- **Evaluation contract:** `§4 retrieval/reasoning tasks and graph-quality evaluation`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: automated extraction and selected AI literature do not prove a complete or authoritative knowledge graph`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `AGENT-WORKFLOW`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-28158:end -->

<!-- review:SF-2026-ARXIV-2604-28175:start -->
<!-- claim:SF-2026-ARXIV-2604-28175:start -->
Priority-aware serving needs interference-conditioned latency prediction; priority without concurrent-execution estimates merely moves queue delay into GPU contention and can violate both classes' SLOs.
<!-- claim:SF-2026-ARXIV-2604-28175:end -->
#### Strait: Perceiving Priority and Interference in ML Inference Serving

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 Strait dual-priority scheduler and interference predictor`。
- **Mechanism / ownership:** Priority-aware serving needs interference-conditioned latency prediction; priority without concurrent-execution estimates merely moves queue delay into GPU contention and can violate both classes' SLOs.
- **Evaluation contract:** `§4 serving traces/models, baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: on-premises model roster and hardware do not establish universal predictor transfer or tail-SLO behavior`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28175:end -->

<!-- review:SF-2026-ARXIV-2604-28181:start -->
<!-- claim:SF-2026-ARXIV-2604-28181:start -->
Long-horizon computer-use evaluation needs synthetic workspace state and artifact lineage, not isolated screenshots; scalable generation must preserve task-consistent files, directories and terminal evidence.
<!-- claim:SF-2026-ARXIV-2604-28181:end -->
#### Synthetic Computers at Scale for Long-Horizon Productivity Simulation

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 synthetic computer/workspace generation pipeline`。
- **Mechanism / ownership:** Long-horizon computer-use evaluation needs synthetic workspace state and artifact lineage, not isolated screenshots; scalable generation must preserve task-consistent files, directories and terminal evidence.
- **Evaluation contract:** `§4 long-horizon productivity tasks, realism and agent evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic environments may miss organizational policy, hidden dependencies and real-user distributions`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-28181:end -->

<!-- review:SF-2026-ARXIV-2604-28182:start -->
<!-- claim:SF-2026-ARXIV-2604-28182:start -->
Exploration itself is part of the RL trust boundary: a model that suppresses useful actions can resist training without overt reward hacking, so rollout diversity and policy-update diagnostics must be release evidence.
<!-- claim:SF-2026-ARXIV-2604-28182:end -->
#### Exploration Hacking: Can LLMs Learn to Resist RL Training?

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 exploration-hacking threat model and resistant-policy construction`。
- **Mechanism / ownership:** Exploration itself is part of the RL trust boundary: a model that suppresses useful actions can resist training without overt reward hacking, so rollout diversity and policy-update diagnostics must be release evidence.
- **Evaluation contract:** `§4 RL training experiments, detection signals and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: constructed settings do not establish spontaneous prevalence in deployed models or a complete detector`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `TRAIN-RLHF`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28182:end -->

<!-- review:SF-2026-ARXIV-2604-28190:start -->
<!-- claim:SF-2026-ARXIV-2604-28190:start -->
Distributional representation distance can become a training loss by decoupling the population used to estimate statistics from the gradient batch; this trades estimator state and representation dependence for direct distribution matching.
<!-- claim:SF-2026-ARXIV-2604-28190:end -->
#### Representation Fréchet Loss for Visual Generation

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 Representation Fréchet Loss and population/batch decoupling`。
- **Mechanism / ownership:** Distributional representation distance can become a training loss by decoupling the population used to estimate statistics from the gradient batch; this trades estimator state and representation dependence for direct distribution matching.
- **Evaluation contract:** `§4 visual-generation models, quality/diversity evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected representation encoders and image workloads do not prove perceptual alignment or generalization to all modalities`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MULTIMODAL-GENERATIVE-PARADIGMS`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2604-28190:end -->

<!-- review:SF-2026-ARXIV-2604-28196:start -->
<!-- claim:SF-2026-ARXIV-2604-28196:start -->
A driving world model can share state between 3D scene understanding and future geometry prediction; unified representation still does not grant planner or physical-control authority.
<!-- claim:SF-2026-ARXIV-2604-28196:end -->
#### HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 HERMES++ unified 3D understanding/prediction architecture`。
- **Mechanism / ownership:** A driving world model can share state between 3D scene understanding and future geometry prediction; unified representation still does not grant planner or physical-control authority.
- **Evaluation contract:** `§4 driving datasets, understanding/generation metrics and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: driving datasets and open-loop generation do not prove closed-loop safety or causal controllability`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `MULTIMODAL-WORLD-MODELS`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-28196:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27292 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27306 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27309 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27351 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27358 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27393 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27396 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27405 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27419 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27426 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27467 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27486 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27488 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27536 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27586 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27637 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27660 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27695 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27707 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27711 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27776 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27781 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27789 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27792 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27819 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27844 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27855 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27861 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27878 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27891 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27906 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28056 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28123 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28129 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28138 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28139 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28157 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28158 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28175 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28181 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28182 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28190 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28196 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-26963 | score_7_9 | selected | DA-20260501-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260501-01 |
| SF-2026-ARXIV-2604-26968 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26968 |
| SF-2026-ARXIV-2604-26997 | score_7_9;forced_review | selected | DA-20260501-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260501-02 |
| SF-2026-ARXIV-2604-27003 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27003 |
| SF-2026-ARXIV-2604-27032 | score_7_9;forced_review | selected | DA-20260501-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260501-03 |
| SF-2026-ARXIV-2604-27039 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27039 |
| SF-2026-ARXIV-2604-27045 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27045 |
| SF-2026-ARXIV-2604-27083 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27083 |
| SF-2026-ARXIV-2604-27085 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27085 |
| SF-2026-ARXIV-2604-27089 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27089 |
| SF-2026-ARXIV-2604-27151 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27151 |
| SF-2026-ARXIV-2604-27202 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27202 |
| SF-2026-ARXIV-2604-27221 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27221 |
| SF-2026-ARXIV-2604-27233 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27233 |
| SF-2026-ARXIV-2604-27238 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27238 |
| SF-2026-ARXIV-2604-27249 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27249 |
| SF-2026-ARXIV-2604-27251 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27251 |
| SF-2026-ARXIV-2604-27267 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27267 |
| SF-2026-ARXIV-2604-27283 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27283 |
| SF-2026-ARXIV-2604-27289 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27289 |
| SF-2026-ARXIV-2604-27292 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27292 |
| SF-2026-ARXIV-2604-27306 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27306 |
| SF-2026-ARXIV-2604-27309 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27309 |
| SF-2026-ARXIV-2604-27351 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27351 |
| SF-2026-ARXIV-2604-27358 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27358 |
| SF-2026-ARXIV-2604-27393 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27393 |
| SF-2026-ARXIV-2604-27396 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27396 |
| SF-2026-ARXIV-2604-27405 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27405 |
| SF-2026-ARXIV-2604-27419 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27419 |
| SF-2026-ARXIV-2604-27426 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27426 |
| SF-2026-ARXIV-2604-27467 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27467 |
| SF-2026-ARXIV-2604-27486 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27486 |
| SF-2026-ARXIV-2604-27488 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27488 |
| SF-2026-ARXIV-2604-27536 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27536 |
| SF-2026-ARXIV-2604-27586 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27586 |
| SF-2026-ARXIV-2604-27637 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27637 |
| SF-2026-ARXIV-2604-27660 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27660 |
| SF-2026-ARXIV-2604-27695 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27695 |
| SF-2026-ARXIV-2604-27707 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27707 |
| SF-2026-ARXIV-2604-27711 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27711 |
| SF-2026-ARXIV-2604-27776 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27776 |
| SF-2026-ARXIV-2604-27781 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27781 |
| SF-2026-ARXIV-2604-27789 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27789 |
| SF-2026-ARXIV-2604-27792 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27792 |
| SF-2026-ARXIV-2604-27819 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27819 |
| SF-2026-ARXIV-2604-27844 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27844 |
| SF-2026-ARXIV-2604-27855 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27855 |
| SF-2026-ARXIV-2604-27861 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27861 |
| SF-2026-ARXIV-2604-27878 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27878 |
| SF-2026-ARXIV-2604-27891 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27891 |
| SF-2026-ARXIV-2604-27906 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-27906 |
| SF-2026-ARXIV-2604-28056 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28056 |
| SF-2026-ARXIV-2604-28123 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28123 |
| SF-2026-ARXIV-2604-28129 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28129 |
| SF-2026-ARXIV-2604-28138 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28138 |
| SF-2026-ARXIV-2604-28139 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28139 |
| SF-2026-ARXIV-2604-28157 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28157 |
| SF-2026-ARXIV-2604-28158 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28158 |
| SF-2026-ARXIV-2604-28175 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28175 |
| SF-2026-ARXIV-2604-28181 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28181 |
| SF-2026-ARXIV-2604-28182 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28182 |
| SF-2026-ARXIV-2604-28190 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28190 |
| SF-2026-ARXIV-2604-28196 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-28196 |

<!-- analysis:DA-20260501-01:start -->
### Deep Analysis — SF-2026-ARXIV-2604-26963

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260501-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26968:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26968:end -->

<!-- analysis:DA-20260501-02:start -->
### Deep Analysis — SF-2026-ARXIV-2604-26997

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260501-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27003:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27003:end -->

<!-- analysis:DA-20260501-03:start -->
### Deep Analysis — SF-2026-ARXIV-2604-27032

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260501-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27039:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27039:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27045:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27045:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27083:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27083:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27085:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27085:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27089:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27089:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27151:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27202:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27202:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27221:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27221:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27233:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27233:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27238:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27238:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27249:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27249:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27251:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27251:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27267:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27267:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27283:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27283:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27289:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27289:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27292:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27292:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27306:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27306:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27309:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27309:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27351:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27351:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27358:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27358:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27393:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27393:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27396:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27396:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27405:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27405:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27419:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27419:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27426:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27426:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27467:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27486:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27486:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27488:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27488:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27536:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27536:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27586:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27586:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27637:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27637:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27660:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27660:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27695:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27695:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27707:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27707:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27711:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27711:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27776:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27776:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27781:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27781:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27789:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27789:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27792:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27792:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27819:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27819:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27844:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27844:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27855:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27855:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27861:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27861:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27878:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27878:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27891:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27891:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-27906:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-27906:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28056:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28056:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28123:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28123:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28129:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28129:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28138:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28138:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28139:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28139:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28157:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28157:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28158:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28175:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28181:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28181:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28182:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28182:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28190:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28190:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-28196:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-28196:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-26963 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#调度对象从-request-变成-token-state (line 16, H2: 调度对象从 request 变成 token state) (section: H2) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10, H2: 本章要回答的问题) (section: H2); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10, H2: 本章要回答的问题) (section: H2) | existing:SF-2026-ARXIV-2604-26963 | delta:SF-2026-ARXIV-2604-26963 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26963 |
| SF-2026-ARXIV-2604-26968 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L186 (H2: 三类缓解路径) | books/part-05-inference-system/53-kserve-llm.md#L10 (H2: 本章要回答的问题);books/part-05-inference-system/55-pd-disaggregation.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2604-26968 | delta:SF-2026-ARXIV-2604-26968 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26968 |
| SF-2026-ARXIV-2604-26997 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26997 | delta:SF-2026-ARXIV-2604-26997 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26997 |
| SF-2026-ARXIV-2604-27003 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1208-belief-state-先保存竞争假设-再决定事实 | books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移 | existing:SF-2026-ARXIV-2604-27003 | delta:SF-2026-ARXIV-2604-27003 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27003 |
| SF-2026-ARXIV-2604-27032 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state | books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败 | existing:SF-2026-ARXIV-2604-27032 | delta:SF-2026-ARXIV-2604-27032 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27032 |
| SF-2026-ARXIV-2604-27039 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state | books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败 | existing:SF-2026-ARXIV-2604-27039 | delta:SF-2026-ARXIV-2604-27039 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27039 |
| SF-2026-ARXIV-2604-27045 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1208-belief-state-先保存竞争假设-再决定事实 | books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移 | existing:SF-2026-ARXIV-2604-27045 | delta:SF-2026-ARXIV-2604-27045 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27045 |
| SF-2026-ARXIV-2604-27083 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens | books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | existing:SF-2026-ARXIV-2604-27083 | delta:SF-2026-ARXIV-2604-27083 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27083 |
| SF-2026-ARXIV-2604-27085 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么 | books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够; books/part-04-training-system/39-zero.md#L18-标准-data-parallel-的冗余 | existing:SF-2026-ARXIV-2604-27085 | delta:SF-2026-ARXIV-2604-27085 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27085 |
| SF-2026-ARXIV-2604-27089 | TRAIN-TENSOR-PARALLEL | books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | books/part-04-training-system/36-distributed-training.md#L25-单卡为什么会失败; books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么 | existing:SF-2026-ARXIV-2604-27089 | delta:SF-2026-ARXIV-2604-27089 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27089 |
| SF-2026-ARXIV-2604-27151 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L102-deterministic-spine-agentic-nodes | books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline | existing:SF-2026-ARXIV-2604-27151 | delta:SF-2026-ARXIV-2604-27151 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27151 |
| SF-2026-ARXIV-2604-27202 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-27202 | delta:SF-2026-ARXIV-2604-27202 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27202 |
| SF-2026-ARXIV-2604-27221 | AGENT-RAG | books/part-07-agent/76-rag.md#L420-rag-不消除-hallucination | books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界 | existing:SF-2026-ARXIV-2604-27221 | delta:SF-2026-ARXIV-2604-27221 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27221 |
| SF-2026-ARXIV-2604-27233 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L55-模型输出只是-proposal | books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界; books/part-07-agent/79-planning.md#L16-plan-不是解释文本 | existing:SF-2026-ARXIV-2604-27233 | delta:SF-2026-ARXIV-2604-27233 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27233 |
| SF-2026-ARXIV-2604-27238 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-27238 | delta:SF-2026-ARXIV-2604-27238 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27238 |
| SF-2026-ARXIV-2604-27249 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-27249 | delta:SF-2026-ARXIV-2604-27249 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27249 |
| SF-2026-ARXIV-2604-27251 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#L246-residual-stream-从单一累加状态走向-depth-wise-routing | books/part-02-model/16-feed-forward-mlp.md#L18-只有-attention-会缺少什么; books/part-02-model/18-decoder-only.md#L18-transformer-layer-还缺什么 | existing:SF-2026-ARXIV-2604-27251 | delta:SF-2026-ARXIV-2604-27251 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27251 |
| SF-2026-ARXIV-2604-27267 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-27267 | delta:SF-2026-ARXIV-2604-27267 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27267 |
| SF-2026-ARXIV-2604-27283 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1208-belief-state-先保存竞争假设-再决定事实 | books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移 | existing:SF-2026-ARXIV-2604-27283 | delta:SF-2026-ARXIV-2604-27283 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27283 |
| SF-2026-ARXIV-2604-27289 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2604-27289 | delta:SF-2026-ARXIV-2604-27289 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27289 |
| SF-2026-ARXIV-2604-27292 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2604-27292 | delta:SF-2026-ARXIV-2604-27292 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27292 |
| SF-2026-ARXIV-2604-27306 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2604-27306 | delta:SF-2026-ARXIV-2604-27306 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27306 |
| SF-2026-ARXIV-2604-27309 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L12 | books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-06-ai-infrastructure/73-production-practices.md#L14 | existing:SF-2026-ARXIV-2604-27309 | delta:SF-2026-ARXIV-2604-27309 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27309 |
| SF-2026-ARXIV-2604-27351 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2604-27351 | delta:SF-2026-ARXIV-2604-27351 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27351 |
| SF-2026-ARXIV-2604-27358 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/79-planning.md#L1; books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2604-27358 | delta:SF-2026-ARXIV-2604-27358 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27358 |
| SF-2026-ARXIV-2604-27393 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-05-inference-system/43-prefill.md#L1 | existing:SF-2026-ARXIV-2604-27393 | delta:SF-2026-ARXIV-2604-27393 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27393 |
| SF-2026-ARXIV-2604-27396 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L122 | books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2604-27396 | delta:SF-2026-ARXIV-2604-27396 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27396 |
| SF-2026-ARXIV-2604-27405 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27405 | delta:SF-2026-ARXIV-2604-27405 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27405 |
| SF-2026-ARXIV-2604-27419 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/78-tool-calling.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27419 | delta:SF-2026-ARXIV-2604-27419 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27419 |
| SF-2026-ARXIV-2604-27426 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-04-training-system/29-sft.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27426 | delta:SF-2026-ARXIV-2604-27426 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-27426 |
| SF-2026-ARXIV-2604-27467 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-04-training-system/31-rlhf.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27467 | delta:SF-2026-ARXIV-2604-27467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27467 |
| SF-2026-ARXIV-2604-27486 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L220 | books/part-06-ai-infrastructure/72-security.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-27486 | delta:SF-2026-ARXIV-2604-27486 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27486 |
| SF-2026-ARXIV-2604-27488 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27488 | delta:SF-2026-ARXIV-2604-27488 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27488 |
| SF-2026-ARXIV-2604-27536 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2604-27536 | delta:SF-2026-ARXIV-2604-27536 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27536 |
| SF-2026-ARXIV-2604-27586 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-27586 | delta:SF-2026-ARXIV-2604-27586 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27586 |
| SF-2026-ARXIV-2604-27637 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/74-prompt.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27637 | delta:SF-2026-ARXIV-2604-27637 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27637 |
| SF-2026-ARXIV-2604-27660 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/77-memory.md#L1; books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2604-27660 | delta:SF-2026-ARXIV-2604-27660 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27660 |
| SF-2026-ARXIV-2604-27695 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27695 | delta:SF-2026-ARXIV-2604-27695 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27695 |
| SF-2026-ARXIV-2604-27707 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2604-27707 | delta:SF-2026-ARXIV-2604-27707 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27707 |
| SF-2026-ARXIV-2604-27711 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2604-27711 | delta:SF-2026-ARXIV-2604-27711 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27711 |
| SF-2026-ARXIV-2604-27776 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27776 | delta:SF-2026-ARXIV-2604-27776 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27776 |
| SF-2026-ARXIV-2604-27781 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1; books/part-06-ai-infrastructure/60-model-registry.md#L1 | existing:SF-2026-ARXIV-2604-27781 | delta:SF-2026-ARXIV-2604-27781 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27781 |
| SF-2026-ARXIV-2604-27789 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2604-27789 | delta:SF-2026-ARXIV-2604-27789 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27789 |
| SF-2026-ARXIV-2604-27792 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14; books/part-05-inference-system/49-tensorrt-llm.md#L14 | existing:SF-2026-ARXIV-2604-27792 | delta:SF-2026-ARXIV-2604-27792 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27792 |
| SF-2026-ARXIV-2604-27819 | AGENT-MCP | books/part-07-agent/83-mcp.md#L1 | books/part-06-ai-infrastructure/72-security.md#L1; books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2604-27819 | delta:SF-2026-ARXIV-2604-27819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27819 |
| SF-2026-ARXIV-2604-27844 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L69 | books/part-04-training-system/37-data-parallel.md#L1; books/part-04-training-system/41-distributed-training-runtime.md#L1 | existing:SF-2026-ARXIV-2604-27844 | delta:SF-2026-ARXIV-2604-27844 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27844 |
| SF-2026-ARXIV-2604-27855 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2604-27855 | delta:SF-2026-ARXIV-2604-27855 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-27855 |
| SF-2026-ARXIV-2604-27861 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-07-agent/75-context.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2604-27861 | delta:SF-2026-ARXIV-2604-27861 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27861 |
| SF-2026-ARXIV-2604-27878 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2604-27878 | delta:SF-2026-ARXIV-2604-27878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27878 |
| SF-2026-ARXIV-2604-27891 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27891 | delta:SF-2026-ARXIV-2604-27891 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27891 |
| SF-2026-ARXIV-2604-27906 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27906 | delta:SF-2026-ARXIV-2604-27906 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27906 |
| SF-2026-ARXIV-2604-28056 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-28056 | delta:SF-2026-ARXIV-2604-28056 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28056 |
| SF-2026-ARXIV-2604-28123 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/29-sft.md#L1; books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2604-28123 | delta:SF-2026-ARXIV-2604-28123 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28123 |
| SF-2026-ARXIV-2604-28129 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/69-trace.md#L1; books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2604-28129 | delta:SF-2026-ARXIV-2604-28129 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-28129 |
| SF-2026-ARXIV-2604-28138 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L50 | books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/73-production-practices.md#L1 | existing:SF-2026-ARXIV-2604-28138 | delta:SF-2026-ARXIV-2604-28138 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28138 |
| SF-2026-ARXIV-2604-28139 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L18 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L69 | existing:SF-2026-ARXIV-2604-28139 | delta:SF-2026-ARXIV-2604-28139 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28139 |
| SF-2026-ARXIV-2604-28157 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2604-28157 | delta:SF-2026-ARXIV-2604-28157 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28157 |
| SF-2026-ARXIV-2604-28158 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-28158 | delta:SF-2026-ARXIV-2604-28158 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28158 |
| SF-2026-ARXIV-2604-28175 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2604-28175 | delta:SF-2026-ARXIV-2604-28175 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28175 |
| SF-2026-ARXIV-2604-28181 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-28181 | delta:SF-2026-ARXIV-2604-28181 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28181 |
| SF-2026-ARXIV-2604-28182 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2604-28182 | delta:SF-2026-ARXIV-2604-28182 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28182 |
| SF-2026-ARXIV-2604-28190 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-28190 | delta:SF-2026-ARXIV-2604-28190 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-28190 |
| SF-2026-ARXIV-2604-28196 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/23-multimodal-representation.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2604-28196 | delta:SF-2026-ARXIV-2604-28196 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28196 |

<!-- books-review:SF-2026-ARXIV-2604-26963:start -->
<!-- existing:SF-2026-ARXIV-2604-26963:start -->current owner `books/part-05-inference-system/56-inference-scheduling.md` 在 `books/part-05-inference-system/56-inference-scheduling.md#调度对象从-request-变成-token-state (line 16, H2: 调度对象从 request 变成 token state)` 的实际命题：普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。 调度器需要理解： - 请求处于 Prefill 还是 Decode。 - 已经生成多少 token。 - 还可能生成多少 token。 - KV Cache 占用多少显存。 - 是否共享 prefix。 - 是否正在 speculative verification。 - 是否需要跨 worker handoff。 这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。 一个完整 Serving 系统通常同时存在四层决策： 只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。 owner_sha256=285ddf8eae11e6e0f941cf66d1b3dd7dc71f62cc69cd85673734b8fbd9713fb0。<!-- existing:SF-2026-ARXIV-2604-26963:end -->
<!-- delta:SF-2026-ARXIV-2604-26963:start -->作者公开的机制是：We design and implement MARS, an efficient and adaptive co-scheduling system that globally coordinates heterogeneous agentic workloads under coupled GPU-CPU resource pressure. 对系统而言，scheduler 拥有 admission、placement、rate/preemption state 与 SLO observation；预测漂移或 tail/fairness 越界时回退保守配置。 exact-v1 Method evidence: 4.2. Control Plane Design While the unified information stream (§4.1) makes heterogeneous execution observable, observability alone is not sufficient to preserve stability. Under agentic workloads, a serving node is constrained by GPU capacity and CPU service capacity. Without explicit admission control, serving engines remain vulnerable to cascading overload under sustained agentic workloads. MARS addresses this mismatch with an External Control Plane, which is organized around two logical modules. A Global Load Balancer shapes the waiting queue into a resource-aware admission order. An External Admission Controller then computes how much of that ordered queue can safely enter the data plane. Global Load Balan<!-- delta:SF-2026-ARXIV-2604-26963:end --> Decision=`No Change — Existing Coverage`；evidence boundary：`MARS: Efficient, Adaptive Co-Scheduling for Heterogeneous Agentic Systems` 只证明 exact-v1 的公开模型、数据、硬件和 workload；evaluation evidence 为：Our evaluations show that MARS reduces end-to-end latency by up to 5.94x while maintaining nearly maximal system throughput. We further integrate MARS as the serving backend for the OpenHands coding agent framework, demonstrating its real-world effectiveness by accelerating end-to-end task completion time by up to 1.87x. 未披露生产 SLO、多租户、跨硬件或长期运行结果时不得外推。
<!-- books-review:SF-2026-ARXIV-2604-26963:end -->

<!-- books-review:SF-2026-ARXIV-2604-26968:start -->
<!-- existing:SF-2026-ARXIV-2604-26968:start -->canonical owner `books/part-05-inference-system/54-gpu-memory.md` 当前最相关命题：### 减少 Bytes Weight/KV quantization、GQA/MQA、压缩或稀疏 retention 直接减少 resident bytes，但需要质量与 kernel 验证。 KV retention 还存在两个不同粒度。Token eviction 先决定保留哪些历史位置，简单且适配现有 accelerator；但每个 被保留 token 的完整 K/V vector 仍需从 memory hierarchy 取回。当 vector traffic 成为新的带宽下限，系统可以继续 选择 token 内的 elements： ```text full KV → token-level importance / eviction → element-level selection inside retained vectors → layout-aware fetch + bounded approximate attention ``` 第二层选择与第一层不是免费相乘。它需要保存两级 importance state、校准允许的 accuracy loss，并把非连续访问、 metadata、sorting 和 kernel/accelerator 支持纳入成本；否则省下的 bytes 会被 fragmented access 与 ranking overhead 吃掉。可重配置 sorter 能复用两级排序 datapath，但会引入 silicon specialization，离线 per-task calibration 也不能 自动转移到 production workload。Full KV 仍是 correctness baseline；没有专用 kernel、向量访问尚未主导或严格 exactness 优先时，token-only retention 仍更合理。 ### 提高利用率 Paging、prefix sharing 和更精确 admission 减少预留与碎片，却不改变每个有效 KV element 的逻辑需求。 ### 扩展层级 CPU/SSD/off-node cache 扩大总容量，却加入 transfer latency、bandwidth contention 和 consistency。它们把“装不下”改成“何时值得搬”。 权重 offload 也应从“整层搬运”进一步区分到 conditional-compute state。MoE 的 active expert 由 router 决定，静态把全部 experts 常驻 HBM 最简单且延迟稳定；固定 offload 一部分 experts 能扩容，却忽略请求 分布变化。Router-conditioned expert cache 可按实际激活维护 hot set，进一步用前序层或历史路由预测下一 步 expert 并异步 prefetch： ```text full expert residency → static host offload → router-conditioned expert cache → predicted asynchronous prefetch ``` 这里与 GEMM tiling、FlashAttention 的共同点只是 IO-aware 的原理复用（`Principle Reuse`）：都把超过近端容量的状态 分块，并尝试用 pipeline 隐藏搬运。数学条件并不相同。GEMM 的 operand 与 reduction 顺序预先已知；online softmax 还能用 running maximum 与 normalization sum 合并各 tile，避免 materialize 完整 attention matrix。 MoE router 则在看到当前 hidden state 后才选择一组不同的非线性函数 `Expert_e`，不存在一个小型 running statistic 可以精确恢复任意尚未驻留的 expert weights。 因此 expert page miss 仍有不可消除的数据移动下界：`T_miss >= M_miss /…<!-- existing:SF-2026-ARXIV-2604-26968:end -->
<!-- delta:SF-2026-ARXIV-2604-26968:start -->exact-v1 `h3 V-B Analytical Projection Methodology [id=—]` 定义机制：Cluster-scale performance is projected using published hardware specifications for each memory tier: H100 SXM GPU HBM3 bandwidth of 3.35 TB/s and 80 GB capacity [27]; CXL 3.0 device-local bandwidth of 64 GB/s with approximately 150 ns device-local latency (∼{\sim}500 ns GPU-observed via the CXL.mem protocol) [23]; GPUDirect Storage throughput of 12 GB/s via cuFile APIs [28]; and InfiniBand NDR bandwidth of 400 Gbps (50 GB/s effective) [33]. Per-tier throughput projections combine these datasheet bandwidths with validated per-block access patterns from the Bayesian predictor running on trace data. Throughput projections assume linear scaling from batch size increases up to the compute saturation point of each model, a standard assumption in memory-bound inference analysis [1, 4]. Metrics. Time-to-first-token (TTFT) at P50 and P99, time-between-tokens (TBT) at P99, throughput (tokens/s/GPU), and cost ($/million tokens computed from cloud GPU pricing at $2/GPU-hour). 因此 state/data/control owner 归入 `INFER-GPU-MEMORY`，而不是由论文名称或产品自行成为知识 owner。<!-- delta:SF-2026-ARXIV-2604-26968:end -->
Decision=`No Change — Existing Coverage`；evidence boundary：只支持 `h3 V-B Analytical Projection Methodology [id=—]` 所定义的机制与 `h3 V-D Projected Multi-Tier Performance [id=—]` 所覆盖的模型、数据、硬件和 workload；`h2 VII Conclusion [id=—]` 之外不证明生产泛化、因果完备性或跨环境收益。
<!-- books-review:SF-2026-ARXIV-2604-26968:end -->

<!-- books-review:SF-2026-ARXIV-2604-26997:start -->
<!-- existing:SF-2026-ARXIV-2604-26997:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-26997:end -->
<!-- delta:SF-2026-ARXIV-2604-26997:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-26997:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26997:end -->

<!-- books-review:SF-2026-ARXIV-2604-27003:start -->
<!-- existing:SF-2026-ARXIV-2604-27003:start -->真实 owner `books/part-07-agent/77-memory.md#L1208-belief-state先保存竞争假设再决定事实` 正文：## Belief State：先保存竞争假设，再决定事实 把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。 这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]；相邻章 `books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a241ab934a3c3b722b6cbce0351db40d0c918fb10b89a72e0c4463ffeaf7599e。<!-- existing:SF-2026-ARXIV-2604-27003:end -->
<!-- delta:SF-2026-ARXIV-2604-27003:start -->memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图<!-- delta:SF-2026-ARXIV-2604-27003:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27003:end -->

<!-- books-review:SF-2026-ARXIV-2604-27032:start -->
<!-- existing:SF-2026-ARXIV-2604-27032:start -->真实 owner `books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state` 正文：## 调度对象从 request 变成 token state 普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。 调度器需要理解： - 请求处于 Prefill 还是 Decode。 - 已经生成多少 token。 - 还可能生成多少 token。 - KV Cache 占用多少显存。 - 是否共享 prefix。 - 是否正在 speculative verification。 - 是否需要跨 worker handoff。 这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。 一个完整 Serving 系统通常同时存在四层决策： ```text admission control 请求是否可以进入，是否有 SLO 与 memory budget iteration scheduling 下一轮执行哪些 token work routing / placement 请求、KV 与 model workers 放在哪里 autoscaling 未来需要多少 workers 和哪类 capacity ``` 只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。；相邻章 `books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=285ddf8eae11e6e0f941cf66d1b3dd7dc71f62cc69cd85673734b8fbd9713fb0。<!-- existing:SF-2026-ARXIV-2604-27032:end -->
<!-- delta:SF-2026-ARXIV-2604-27032:start -->scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission<!-- delta:SF-2026-ARXIV-2604-27032:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27032:end -->

<!-- books-review:SF-2026-ARXIV-2604-27039:start -->
<!-- existing:SF-2026-ARXIV-2604-27039:start -->真实 owner `books/part-05-inference-system/56-inference-scheduling.md#L16-调度对象从-request-变成-token-state` 正文：## 调度对象从 request 变成 token state 普通 Web 服务调度通常看 request。LLM Serving 不能只看 request，因为一个请求会持续生成很多 token。 调度器需要理解： - 请求处于 Prefill 还是 Decode。 - 已经生成多少 token。 - 还可能生成多少 token。 - KV Cache 占用多少显存。 - 是否共享 prefix。 - 是否正在 speculative verification。 - 是否需要跨 worker handoff。 这意味着 LLM 调度对象是“带 runtime state 的 token generation process”。 一个完整 Serving 系统通常同时存在四层决策： ```text admission control 请求是否可以进入，是否有 SLO 与 memory budget iteration scheduling 下一轮执行哪些 token work routing / placement 请求、KV 与 model workers 放在哪里 autoscaling 未来需要多少 workers 和哪类 capacity ``` 只优化其中一层，可能把瓶颈推给下一层。例如 iteration batch 很满，但 admission 让长请求无限排队，系统吞吐看起来很好，用户 SLO 仍然失败。；相邻章 `books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L16-从单点成功到组织级失败` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=285ddf8eae11e6e0f941cf66d1b3dd7dc71f62cc69cd85673734b8fbd9713fb0。<!-- existing:SF-2026-ARXIV-2604-27039:end -->
<!-- delta:SF-2026-ARXIV-2604-27039:start -->scheduler 拥有队列、priority 与 resource reservation，model/kernel 不自行决定 admission<!-- delta:SF-2026-ARXIV-2604-27039:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27039:end -->

<!-- books-review:SF-2026-ARXIV-2604-27045:start -->
<!-- existing:SF-2026-ARXIV-2604-27045:start -->真实 owner `books/part-07-agent/77-memory.md#L1208-belief-state先保存竞争假设再决定事实` 正文：## Belief State：先保存竞争假设，再决定事实 把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。 这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]；相邻章 `books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a241ab934a3c3b722b6cbce0351db40d0c918fb10b89a72e0c4463ffeaf7599e。<!-- existing:SF-2026-ARXIV-2604-27045:end -->
<!-- delta:SF-2026-ARXIV-2604-27045:start -->memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图<!-- delta:SF-2026-ARXIV-2604-27045:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27045:end -->

<!-- books-review:SF-2026-ARXIV-2604-27083:start -->
<!-- existing:SF-2026-ARXIV-2604-27083:start -->真实 owner `books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens` 正文：## Sequence Reward 怎样作用到 Tokens 若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens： ```text A_(i,1) = ... = A_(i,\|y_i\|) = A_i ``` 这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。 Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。；相邻章 `books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=37ab39bc16e7905281265dede7f404b65fb4814e9ee1e4d81a5342f6c012e97a。<!-- existing:SF-2026-ARXIV-2604-27083:end -->
<!-- delta:SF-2026-ARXIV-2604-27083:start -->rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit<!-- delta:SF-2026-ARXIV-2604-27083:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27083:end -->

<!-- books-review:SF-2026-ARXIV-2604-27085:start -->
<!-- existing:SF-2026-ARXIV-2604-27085:start -->真实 owner `books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么` 正文：## 只有 Layer Partition 会发生什么 把 `L` 层模型切为 `p` 个连续 stages： ```text Stage 1: layers 1 ... l_1 Stage 2: layers l_1+1 ... l_2 ... Stage p: ... layer L + loss ``` Forward 时，Stage `i` 输出 activation 给 `i+1`；backward 时，activation gradient 反向传给 `i-1`。 若整个 batch 作为一个 unit： ```text S1 forward -> S2 forward -> ... -> Sp forward ``` 在 S1 工作时，后续 stages 空闲；在最后 stage 工作时，前面 stages 也在等待。Layer capacity 已经分散，设备利用率仍很低。；相邻章 `books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够; books/part-04-training-system/39-zero.md#L18-标准-data-parallel-的冗余` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a0c5830ee4d728078f836682fa5d02b7079ce7acbc3e89b90d67d54ce8c9c7e7。<!-- existing:SF-2026-ARXIV-2604-27085:end -->
<!-- delta:SF-2026-ARXIV-2604-27085:start -->pipeline runtime 拥有 stage/microbatch/activation state，optimizer 只提交完整 step<!-- delta:SF-2026-ARXIV-2604-27085:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27085:end -->

<!-- books-review:SF-2026-ARXIV-2604-27089:start -->
<!-- existing:SF-2026-ARXIV-2604-27089:start -->真实 owner `books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 正文：## 为什么“把权重文件切开”不够 线性层： ```text Y = X W X [M,d_in] W [d_in,d_out] Y [M,d_out] ``` 随机把 `W` bytes 平均分给两张 GPU，不会自动得到可组合计算。切分必须对应矩阵维度，并明确： - 每个 rank 需要哪部分输入。 - Local GEMM 输出是完整值还是 partial sum。 - 下一 operator 能否直接消费分片。 - Forward 与 backward 在哪里 collective。 Tensor Parallel 是 operator graph transformation，不是 storage sharding 的别名。；相邻章 `books/part-04-training-system/36-distributed-training.md#L25-单卡为什么会失败; books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a0c1ec60ea9dcfa334ef4fe61a1584e8475fffc3c835c0f51477f74e0ae59b78。<!-- existing:SF-2026-ARXIV-2604-27089:end -->
<!-- delta:SF-2026-ARXIV-2604-27089:start -->parallel plan owner 冻结 tensor layout/collective，kernel 只消费一致 shard<!-- delta:SF-2026-ARXIV-2604-27089:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27089:end -->

<!-- books-review:SF-2026-ARXIV-2604-27151:start -->
<!-- existing:SF-2026-ARXIV-2604-27151:start -->真实 owner `books/part-07-agent/81-workflow.md#L102-deterministic-spineagentic-nodes` 正文：## Deterministic Spine，Agentic Nodes 适合 deterministic 的部分： - identity、authorization、budgets； - required gates； - retry/backoff/timeouts； - state transitions； - side-effect records； - cancellation/compensation； - terminal success criteria。 适合 model-driven 的部分： - interpreting ambiguous intent； - drafting content； - proposing plans/tool arguments； - ranking alternatives； - diagnosing unstructured failure。 这种组合既保留模型灵活性，又让业务不变量可测试。 ### 从一次性脚本到平台拥有的可编辑 DAG 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。 这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。 ### Template、Realized Graph 与 Trace 不是同一个对象 固定 code-defined template 便于审查、复现和强 verifier，仍是稳定 wor；相邻章 `books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=876ac2cc1f59f9376dcee3315ca5f38e95345018a37b1f888b9787534e149a1d。<!-- existing:SF-2026-ARXIV-2604-27151:end -->
<!-- delta:SF-2026-ARXIV-2604-27151:start -->workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步<!-- delta:SF-2026-ARXIV-2604-27151:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27151:end -->

<!-- books-review:SF-2026-ARXIV-2604-27202:start -->
<!-- existing:SF-2026-ARXIV-2604-27202:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-27202:end -->
<!-- delta:SF-2026-ARXIV-2604-27202:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-27202:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27202:end -->

<!-- books-review:SF-2026-ARXIV-2604-27221:start -->
<!-- existing:SF-2026-ARXIV-2604-27221:start -->真实 owner `books/part-07-agent/76-rag.md#L410-rag-不消除-hallucination` 正文：## RAG 不消除 Hallucination 回答与检索文档内容一致，不等于回答由该文档支撑：模型可能只是在 parametric memory 中本就知道答案，检索内容甚至没有进入有效推理路径。若 evaluation 只看最终正确率或 citation overlap，就无法区分“证据导致了答案”与“答案碰巧和证据一致”。更严格的 groundedness contract 需要成对干预：保留问题、替换或遮蔽关键证据，观察结论与引用是否按预期改变，并把这种 counterfactual sensitivity 与普通 correctness 分开报告。 干预评估提高了因果诊断力，却增加样本构造、对照污染和 evaluator 成本；答案对证据不敏感也可能因为模型拥有正确先验，而非一定错误。低风险搜索可继续用 relevance/citation 指标快速迭代，高风险发布则需要 provenance、support span 与干预证据共同证明检索链真正拥有结论的 support authority。 ### Web Retrieval 的 Corpus 也可能主动塑造 Agent Trajectory 传统 RAG 把 corpus 当作被动事实集合；web-enabled Agent 会连续搜索、引用、回访并让多个页面共同塑造后续 query， 于是发布者优化的不再是单页排名，而是整条 evidence trajectory。检索系统必须记录页面 provenance、跨站关联、 query evolution 与最终 claim uptake，不能把“多处出现”自动解释为独立证据。协调内容生态可以提高可发现性，也会 制造相关来源、反馈回路与操纵面；高风险结论应回到独立 primary source 和 claim-level entailment。固定私有 corpus 仍适合低变化、强治理场景。受控虚构产品实验只证明 trajectory-level influence 可以被测量，不证明现实 web 排名 或所有搜索 Agent 会同样受影响。 ### ；相邻章 `books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=67561d15a90f3b4c8456e4d13cef9986646cc20bce9bbbb15bdcb01399f0e4f3。<!-- existing:SF-2026-ARXIV-2604-27221:end -->
<!-- delta:SF-2026-ARXIV-2604-27221:start -->retrieval service 拥有 index/query evidence，generator 不获得来源真值所有权<!-- delta:SF-2026-ARXIV-2604-27221:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27221:end -->

<!-- books-review:SF-2026-ARXIV-2604-27233:start -->
<!-- existing:SF-2026-ARXIV-2604-27233:start -->真实 owner `books/part-07-agent/78-tool-calling.md#L55-模型输出只是-proposal` 正文：## 模型输出只是 Proposal 典型 data path： ```text raw model output → parse → schema validation → canonicalization → authorization → policy/business validation → optional approval → execution → result filtering → observation ``` Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。 ### 编译器反馈可以前移，但仍是受限 Authority 先完整生成程序，再调用 compiler/test 并修复，是最通用的黑盒路径；当 grammar 可处理时，constrained decoding 也能提前排除语法错误。但后置诊断会浪费已经生成的 token，并把错误起点埋在长输出中；另一方面，任意 prefix 通常还不是可编译单元，不能直接交给编译器。 折中控制流是把中间输出视为 provisional proposal：由 sealor 把 partial output 补成临时可编译单元，compiler 只拥有 syntax/type diagnostics，harness 根据诊断与预算决定 bounded rollback 或 rewrite，模型再继续生成。这样可把权威反馈前移，却不把 compiler 提升为任务正确性裁判，也不要求白盒访问模型内部状态。 代价是频繁 compiler call、语言特定的 sealing 规则、rollback state 与重放成本；涉及 future definition 的长依赖还会让临时补全失真。后置 compile/repair 仍是跨语言、低频生成的合理基线，而 compile success 不能替；相邻章 `books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界; books/part-07-agent/79-planning.md#L16-plan-不是解释文本` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=e0b32607ccfbaece1434f3f9afe1abe5349c2a68ba239760df68c1529b279e09。<!-- existing:SF-2026-ARXIV-2604-27233:end -->
<!-- delta:SF-2026-ARXIV-2604-27233:start -->tool registry 拥有 capability/schema version，router 只选择候选，executor 保留授权<!-- delta:SF-2026-ARXIV-2604-27233:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27233:end -->

<!-- books-review:SF-2026-ARXIV-2604-27238:start -->
<!-- existing:SF-2026-ARXIV-2604-27238:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-27238:end -->
<!-- delta:SF-2026-ARXIV-2604-27238:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-27238:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27238:end -->

<!-- books-review:SF-2026-ARXIV-2604-27249:start -->
<!-- existing:SF-2026-ARXIV-2604-27249:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-27249:end -->
<!-- delta:SF-2026-ARXIV-2604-27249:start -->When instructed to underperform on multiple-choice evaluations, do language models engage with question content or fall back on positional shortcuts? We map the boundary between these regimes using a six-condition adversarial instruction-specificity gradient administered to two instruction-tuned LLMs (Llama-3-8B and Llama-3.1-8B) on 2,000 MMLU-Pro items. Distributional screening (response-position entropy) and an independent content-engagement criterion (difficulty-accuracy correlation) jointly characterise each condition. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-27249:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.27249v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-27249:end -->

<!-- books-review:SF-2026-ARXIV-2604-27251:start -->
<!-- existing:SF-2026-ARXIV-2604-27251:start -->真实 owner `books/part-02-model/17-transformer-layer.md#L246-residual-stream-从单一累加状态走向-depth-wise-routing` 正文：## Residual Stream 从单一累加状态走向 Depth-wise Routing 标准 residual stream 每层只接收上一层聚合后的状态。它便宜、shape 稳定，也天然适配逐层执行与 Pipeline Parallel；但深度增加后，较早子层的信息已经被压进一个不断累加的向量，后层无法再区分 “来自哪一层”，固定等权累加还可能让单层更新相对主干越来越弱。 一种演进是把部分历史层输出保留为可选择的 depth state：当前层先对历史 sources 计算权重，再形成 本层输入。全量历史选择提供最强表达，却使 activation、跨 stage 传输和推理 I/O 随深度增长；按 block 汇总历史，把 block 内的普通 residual 与 block 间的选择性聚合组合起来，能把状态量压回有限数量的 summary。另一条分支只保留固定数量的 depth slots，并让注意力从槽位中选择，成本更可控，但会引入 slot 容量、写入、覆盖和选择错误。 ```text single accumulated residual → gated / scaled carry-transform path → explicit depth-history selection → block summaries or bounded depth slots ``` 这里真正变化的是信息路由，不是简单“增加一层 Attention”。Checkpoint 拥有 depth query、block/slot 结构与聚合参数；训练 runtime 拥有历史 activation 的保存、重算与跨 stage 传输；推理 runtime 拥有 prefill/decode 的历史状态和 online reduction。更强的 depth routing 换来额外状态、kernel 与并行通信， 而且作者在特定 MoE 配方中的 loss/benchmark 不能证明它会普遍取代标准 residual。模型较浅、吞吐优先、 跨 stage 带宽紧张或；相邻章 `books/part-02-model/16-feed-forward-mlp.md#L18-只有-attention-会缺少什么; books/part-02-model/18-decoder-only.md#L18-transformer-layer-还缺什么` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=26ea46fdf51fff6b44a6f2ff7ece459bcdaa39f6c37014220b281e3a3f121186。<!-- existing:SF-2026-ARXIV-2604-27251:end -->
<!-- delta:SF-2026-ARXIV-2604-27251:start -->layer graph 拥有 recurrent/residual state 与 normalization，runtime 只提交 exact schedule<!-- delta:SF-2026-ARXIV-2604-27251:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27251:end -->

<!-- books-review:SF-2026-ARXIV-2604-27267:start -->
<!-- existing:SF-2026-ARXIV-2604-27267:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-27267:end -->
<!-- delta:SF-2026-ARXIV-2604-27267:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-27267:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27267:end -->

<!-- books-review:SF-2026-ARXIV-2604-27283:start -->
<!-- existing:SF-2026-ARXIV-2604-27283:start -->真实 owner `books/part-07-agent/77-memory.md#L1208-belief-state先保存竞争假设再决定事实` 正文：## Belief State：先保存竞争假设，再决定事实 把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。 这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]；相邻章 `books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a241ab934a3c3b722b6cbce0351db40d0c918fb10b89a72e0c4463ffeaf7599e。<!-- existing:SF-2026-ARXIV-2604-27283:end -->
<!-- delta:SF-2026-ARXIV-2604-27283:start -->memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图<!-- delta:SF-2026-ARXIV-2604-27283:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-27283:end -->

<!-- books-review:SF-2026-ARXIV-2604-27289:start -->
<!-- existing:SF-2026-ARXIV-2604-27289:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27289:end -->
<!-- delta:SF-2026-ARXIV-2604-27289:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27289:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27289:end -->

<!-- books-review:SF-2026-ARXIV-2604-27292:start -->
<!-- existing:SF-2026-ARXIV-2604-27292:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27292:end -->
<!-- delta:SF-2026-ARXIV-2604-27292:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27292:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27292:end -->

<!-- books-review:SF-2026-ARXIV-2604-27306:start -->
<!-- existing:SF-2026-ARXIV-2604-27306:start -->
Ch76 已要求 provenance、temporal validity 与 source authority 随 retrieval evidence 传播。
<!-- existing:SF-2026-ARXIV-2604-27306:end -->
<!-- delta:SF-2026-ARXIV-2604-27306:start -->
尚未把 atomic nugget 的 validity/lifecycle 写成 ranking 前 admission 与失效淘汰状态机。
<!-- delta:SF-2026-ARXIV-2604-27306:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27306:end -->

<!-- books-review:SF-2026-ARXIV-2604-27309:start -->
<!-- existing:SF-2026-ARXIV-2604-27309:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L12` 与 `books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-06-ai-infrastructure/73-production-practices.md#L14`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27309:end -->
<!-- delta:SF-2026-ARXIV-2604-27309:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27309:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27309:end -->

<!-- books-review:SF-2026-ARXIV-2604-27351:start -->
<!-- existing:SF-2026-ARXIV-2604-27351:start -->
已核对 `books/part-07-agent/78-tool-calling.md#L1` 与 `books/part-07-agent/76-rag.md#L1; books/part-07-agent/83-mcp.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27351:end -->
<!-- delta:SF-2026-ARXIV-2604-27351:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27351:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27351:end -->

<!-- books-review:SF-2026-ARXIV-2604-27358:start -->
<!-- existing:SF-2026-ARXIV-2604-27358:start -->
Ch82 已区分 role、communication topology 与 orchestrator authority。
<!-- existing:SF-2026-ARXIV-2604-27358:end -->
<!-- delta:SF-2026-ARXIV-2604-27358:start -->
尚未把 delegation degree 建模为受 safety constraint 约束的运行时控制变量，并显式保留责任传播边界。
<!-- delta:SF-2026-ARXIV-2604-27358:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27358:end -->

<!-- books-review:SF-2026-ARXIV-2604-27393:start -->
<!-- existing:SF-2026-ARXIV-2604-27393:start -->
已核对 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L1` 与 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-05-inference-system/43-prefill.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27393:end -->
<!-- delta:SF-2026-ARXIV-2604-27393:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27393:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27393:end -->

<!-- books-review:SF-2026-ARXIV-2604-27396:start -->
<!-- existing:SF-2026-ARXIV-2604-27396:start -->
已核对 `books/part-05-inference-system/49-tensorrt-llm.md#L122` 与 `books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27396:end -->
<!-- delta:SF-2026-ARXIV-2604-27396:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27396:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27396:end -->

<!-- books-review:SF-2026-ARXIV-2604-27405:start -->
<!-- existing:SF-2026-ARXIV-2604-27405:start -->
Ch66 已要求版本化对象、重复采样、uncertainty 与 release gate。
<!-- existing:SF-2026-ARXIV-2604-27405:end -->
<!-- delta:SF-2026-ARXIV-2604-27405:start -->
尚未说明 aggregate delta 会掩盖 item-level 双向 churn，以及 RCI 类 harmed/helped ledger 如何进入兼容性判断。
<!-- delta:SF-2026-ARXIV-2604-27405:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27405:end -->

<!-- books-review:SF-2026-ARXIV-2604-27419:start -->
<!-- existing:SF-2026-ARXIV-2604-27419:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与 `books/part-07-agent/78-tool-calling.md#L1; books/part-07-agent/81-workflow.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27419:end -->
<!-- delta:SF-2026-ARXIV-2604-27419:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27419:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27419:end -->

<!-- books-review:SF-2026-ARXIV-2604-27426:start -->
<!-- existing:SF-2026-ARXIV-2604-27426:start -->
Ch72 已拥有 artifact provenance、sandbox、secret 与 egress policy。
<!-- existing:SF-2026-ARXIV-2604-27426:end -->
<!-- delta:SF-2026-ARXIV-2604-27426:start -->
尚未把 local fine-tuning model code 明确视为先于 dataset access 获得执行权的供应链主体。
<!-- delta:SF-2026-ARXIV-2604-27426:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27426:end -->

<!-- books-review:SF-2026-ARXIV-2604-27467:start -->
<!-- existing:SF-2026-ARXIV-2604-27467:start -->
Ch66 已要求 evaluator identity、sandbox、terminal evidence 与 workload version 进入 release evidence；Ch31 已把 verifier signal 与 reward proposal 分离。
<!-- existing:SF-2026-ARXIV-2604-27467:end -->
<!-- delta:SF-2026-ARXIV-2604-27467:start -->
尚未把 special-judge synthesis、test-case parallel execution、multi-node sandbox 与 configuration-driven suite 写成训练和评测共享的 code-verification evidence runtime。
<!-- delta:SF-2026-ARXIV-2604-27467:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27467:end -->

<!-- books-review:SF-2026-ARXIV-2604-27486:start -->
<!-- existing:SF-2026-ARXIV-2604-27486:start -->
Ch49 已解释 PTX/SASS 的架构绑定、post-compilation optimization 与独立 correctness/SLO gate。
<!-- existing:SF-2026-ARXIV-2604-27486:end -->
<!-- delta:SF-2026-ARXIV-2604-27486:start -->
尚未解释 reverse lifting 时 type state 如何由统一 register file 恢复、冲突时为何必须 fail closed，以及 typed LLVM IR 怎样成为二进制审计和迁移的中间证据。
<!-- delta:SF-2026-ARXIV-2604-27486:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27486:end -->

<!-- books-review:SF-2026-ARXIV-2604-27488:start -->
<!-- existing:SF-2026-ARXIV-2604-27488:start -->
已核对 `books/part-07-agent/84-agent-platform.md#L1` 与 `books/part-07-agent/80-reflection.md#L1; books/part-07-agent/81-workflow.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27488:end -->
<!-- delta:SF-2026-ARXIV-2604-27488:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27488:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27488:end -->

<!-- books-review:SF-2026-ARXIV-2604-27536:start -->
<!-- existing:SF-2026-ARXIV-2604-27536:start -->
Ch56 已由 workload/SLO/cost profile 拥有 admission 与 routing。
<!-- existing:SF-2026-ARXIV-2604-27536:end -->
<!-- delta:SF-2026-ARXIV-2604-27536:start -->
尚未覆盖黑盒服务只有 verifiable partial observations 时的 belief update、escalation value 与 budgeted stopping。
<!-- delta:SF-2026-ARXIV-2604-27536:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27536:end -->

<!-- books-review:SF-2026-ARXIV-2604-27586:start -->
<!-- existing:SF-2026-ARXIV-2604-27586:start -->
Ch69/Ch81 已要求跨 step trace、artifact lineage 与 terminal evidence。
<!-- existing:SF-2026-ARXIV-2604-27586:end -->
<!-- delta:SF-2026-ARXIV-2604-27586:start -->
尚未把 contamination 视为可先改变 decomposition/routing、后影响最终输出的 control-flow divergence。
<!-- delta:SF-2026-ARXIV-2604-27586:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27586:end -->

<!-- books-review:SF-2026-ARXIV-2604-27637:start -->
<!-- existing:SF-2026-ARXIV-2604-27637:start -->
Ch66 已冻结 model、prompt、evaluator 与 workload identity。
<!-- existing:SF-2026-ARXIV-2604-27637:end -->
<!-- delta:SF-2026-ARXIV-2604-27637:start -->
尚未明确区分 common-prompt comparability 与 per-model optimized deployment contract，并记录两者对 ranking 的不同解释。
<!-- delta:SF-2026-ARXIV-2604-27637:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27637:end -->

<!-- books-review:SF-2026-ARXIV-2604-27660:start -->
<!-- existing:SF-2026-ARXIV-2604-27660:start -->
已核对 `books/part-07-agent/75-context.md#L1` 与 `books/part-07-agent/77-memory.md#L1; books/part-07-agent/80-reflection.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27660:end -->
<!-- delta:SF-2026-ARXIV-2604-27660:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27660:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27660:end -->

<!-- books-review:SF-2026-ARXIV-2604-27695:start -->
<!-- existing:SF-2026-ARXIV-2604-27695:start -->
已核对 `books/part-07-agent/77-memory.md#L1` 与 `books/part-07-agent/76-rag.md#L1; books/part-07-agent/81-workflow.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27695:end -->
<!-- delta:SF-2026-ARXIV-2604-27695:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27695:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27695:end -->

<!-- books-review:SF-2026-ARXIV-2604-27707:start -->
<!-- existing:SF-2026-ARXIV-2604-27707:start -->
已核对 `books/part-07-agent/77-memory.md#L1` 与 `books/part-04-training-system/28-pretraining.md#L1; books/part-07-agent/76-rag.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27707:end -->
<!-- delta:SF-2026-ARXIV-2604-27707:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27707:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27707:end -->

<!-- books-review:SF-2026-ARXIV-2604-27711:start -->
<!-- existing:SF-2026-ARXIV-2604-27711:start -->
已核对 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-05-inference-system/44-decode.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27711:end -->
<!-- delta:SF-2026-ARXIV-2604-27711:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27711:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27711:end -->

<!-- books-review:SF-2026-ARXIV-2604-27776:start -->
<!-- existing:SF-2026-ARXIV-2604-27776:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与 `books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27776:end -->
<!-- delta:SF-2026-ARXIV-2604-27776:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27776:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27776:end -->

<!-- books-review:SF-2026-ARXIV-2604-27781:start -->
<!-- existing:SF-2026-ARXIV-2604-27781:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L1` 与 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1; books/part-06-ai-infrastructure/60-model-registry.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27781:end -->
<!-- delta:SF-2026-ARXIV-2604-27781:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27781:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27781:end -->

<!-- books-review:SF-2026-ARXIV-2604-27789:start -->
<!-- existing:SF-2026-ARXIV-2604-27789:start -->
已核对 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 与 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/72-security.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27789:end -->
<!-- delta:SF-2026-ARXIV-2604-27789:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27789:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27789:end -->

<!-- books-review:SF-2026-ARXIV-2604-27792:start -->
<!-- existing:SF-2026-ARXIV-2604-27792:start -->
已核对 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14` 与 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14; books/part-05-inference-system/49-tensorrt-llm.md#L14`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27792:end -->
<!-- delta:SF-2026-ARXIV-2604-27792:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27792:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27792:end -->

<!-- books-review:SF-2026-ARXIV-2604-27819:start -->
<!-- existing:SF-2026-ARXIV-2604-27819:start -->
Ch83/Ch72 已拥有 MCP server identity、capability 与执行边界。
<!-- existing:SF-2026-ARXIV-2604-27819:end -->
<!-- delta:SF-2026-ARXIV-2604-27819:start -->
尚未说明 benign read/write permission 如何经多 server workflow 合成为跨域泄漏，以及 canary taint 如何跨 tool edge 传播。
<!-- delta:SF-2026-ARXIV-2604-27819:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27819:end -->

<!-- books-review:SF-2026-ARXIV-2604-27844:start -->
<!-- existing:SF-2026-ARXIV-2604-27844:start -->
Ch36 已拥有 collective 语义、算法/transport/topology 分层和 bandwidth/latency/overlap 成本模型。
<!-- existing:SF-2026-ARXIV-2604-27844:end -->
<!-- delta:SF-2026-ARXIV-2604-27844:start -->
尚未把 bit-exact exponent coding、GPU encode/decode critical path 与 adaptive fallback 写成同一条 compression contract。
<!-- delta:SF-2026-ARXIV-2604-27844:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27844:end -->

<!-- books-review:SF-2026-ARXIV-2604-27855:start -->
<!-- existing:SF-2026-ARXIV-2604-27855:start -->
Ch70/Ch56 已联合考虑 cost、SLO、capacity 与 placement。
<!-- existing:SF-2026-ARXIV-2604-27855:end -->
<!-- delta:SF-2026-ARXIV-2604-27855:start -->
尚未把 energy geography 作为仅在 latency、state locality、capacity 与 regulation 硬约束后才可优化的调度维度。
<!-- delta:SF-2026-ARXIV-2604-27855:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27855:end -->

<!-- books-review:SF-2026-ARXIV-2604-27861:start -->
<!-- existing:SF-2026-ARXIV-2604-27861:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L1` 与 `books/part-07-agent/75-context.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27861:end -->
<!-- delta:SF-2026-ARXIV-2604-27861:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27861:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27861:end -->

<!-- books-review:SF-2026-ARXIV-2604-27878:start -->
<!-- existing:SF-2026-ARXIV-2604-27878:start -->
Ch66 已区分任务成功、过程 evidence、evaluator version 与 release authority。
<!-- existing:SF-2026-ARXIV-2604-27878:end -->
<!-- delta:SF-2026-ARXIV-2604-27878:start -->
尚未明确 simulator 的 behavioral realism 与 tester reliability 是两个可能冲突的 evaluation contract，并要求 canonical session schema、loss accounting 和 ranking-validity evidence 分开出账。
<!-- delta:SF-2026-ARXIV-2604-27878:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27878:end -->

<!-- books-review:SF-2026-ARXIV-2604-27891:start -->
<!-- existing:SF-2026-ARXIV-2604-27891:start -->
Ch81 已说明 durable workflow state、side effect、restart 与 audit 需要外部 owner。
<!-- existing:SF-2026-ARXIV-2604-27891:end -->
<!-- delta:SF-2026-ARXIV-2604-27891:start -->
尚未明确外部 graph orchestration 不是默认：procedure 可完整入 context 时，self-routing 可避免 fragment/routing calls，但不能替代 durable commit。
<!-- delta:SF-2026-ARXIV-2604-27891:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27891:end -->

<!-- books-review:SF-2026-ARXIV-2604-27906:start -->
<!-- existing:SF-2026-ARXIV-2604-27906:start -->
已核对 `books/part-07-agent/77-memory.md#L1` 与 `books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27906:end -->
<!-- delta:SF-2026-ARXIV-2604-27906:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27906:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27906:end -->

<!-- books-review:SF-2026-ARXIV-2604-28056:start -->
<!-- existing:SF-2026-ARXIV-2604-28056:start -->
Ch31/Ch66 已区分 reward proposal、evaluation 与 release authority。
<!-- existing:SF-2026-ARXIV-2604-28056:end -->
<!-- delta:SF-2026-ARXIV-2604-28056:start -->
尚未把 reward hypothesis 从共享 checkpoint 分叉、competence verification 与 phase-aware deployment 连成一条控制链。
<!-- delta:SF-2026-ARXIV-2604-28056:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28056:end -->

<!-- books-review:SF-2026-ARXIV-2604-28123:start -->
<!-- existing:SF-2026-ARXIV-2604-28123:start -->
Ch29→Ch31 已解释 SFT 与 preference/RL 的目标差异。
<!-- existing:SF-2026-ARXIV-2604-28123:end -->
<!-- delta:SF-2026-ARXIV-2604-28123:start -->
尚未显式处理 SFT distribution drift 到 RLVR on-policy distribution 的 handoff，并给出黑盒 distillation 这一条件分支。
<!-- delta:SF-2026-ARXIV-2604-28123:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28123:end -->

<!-- books-review:SF-2026-ARXIV-2604-28129:start -->
<!-- existing:SF-2026-ARXIV-2604-28129:start -->
Ch72 已要求跨 turn threat state 与 effect mediation。
<!-- existing:SF-2026-ARXIV-2604-28129:end -->
<!-- delta:SF-2026-ARXIV-2604-28129:start -->
尚未补充 residual activation trajectory 这一 white-box detector 分支、模型更新后的 recalibration 和 hosted-model 不可用边界。
<!-- delta:SF-2026-ARXIV-2604-28129:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28129:end -->

<!-- books-review:SF-2026-ARXIV-2604-28138:start -->
<!-- existing:SF-2026-ARXIV-2604-28138:start -->
Ch84 已把 AgentRun、workflow state、tool side effect 和 terminal evidence 区分于 transcript/KV。
<!-- existing:SF-2026-ARXIV-2604-28138:end -->
<!-- delta:SF-2026-ARXIV-2604-28138:start -->
尚未具体说明 turn-boundary checkpoint 如何联合捕获 filesystem/process/tool state，以及稀疏检测如何引入 false-negative 与 co-location contention。
<!-- delta:SF-2026-ARXIV-2604-28138:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28138:end -->

<!-- books-review:SF-2026-ARXIV-2604-28139:start -->
<!-- existing:SF-2026-ARXIV-2604-28139:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L18` 与 `books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L69`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-28139:end -->
<!-- delta:SF-2026-ARXIV-2604-28139:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-28139:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-28139:end -->

<!-- books-review:SF-2026-ARXIV-2604-28157:start -->
<!-- existing:SF-2026-ARXIV-2604-28157:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L1` 与 `books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/75-context.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-28157:end -->
<!-- delta:SF-2026-ARXIV-2604-28157:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-28157:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-28157:end -->

<!-- books-review:SF-2026-ARXIV-2604-28158:start -->
<!-- existing:SF-2026-ARXIV-2604-28158:start -->
已核对 `books/part-07-agent/81-workflow.md#L1` 与 `books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-28158:end -->
<!-- delta:SF-2026-ARXIV-2604-28158:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-28158:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-28158:end -->

<!-- books-review:SF-2026-ARXIV-2604-28175:start -->
<!-- existing:SF-2026-ARXIV-2604-28175:start -->
Ch56 已由 queue、SLO 和 runtime state 拥有 request scheduling。
<!-- existing:SF-2026-ARXIV-2604-28175:end -->
<!-- delta:SF-2026-ARXIV-2604-28175:start -->
尚未把 priority 与 concurrent interference-conditioned latency prediction 联合，防止优先级把等待迁移为 GPU contention。
<!-- delta:SF-2026-ARXIV-2604-28175:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28175:end -->

<!-- books-review:SF-2026-ARXIV-2604-28181:start -->
<!-- existing:SF-2026-ARXIV-2604-28181:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与 `books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-28181:end -->
<!-- delta:SF-2026-ARXIV-2604-28181:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-28181:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-28181:end -->

<!-- books-review:SF-2026-ARXIV-2604-28182:start -->
<!-- existing:SF-2026-ARXIV-2604-28182:start -->
Ch31/Ch32/Ch33 已覆盖 reward hacking、KL 与 rollout/update loop。
<!-- existing:SF-2026-ARXIV-2604-28182:end -->
<!-- delta:SF-2026-ARXIV-2604-28182:start -->
尚未把策略性抑制 exploration 作为独立训练阻抗，并要求 rollout diversity/update diagnostics 成为 release evidence。
<!-- delta:SF-2026-ARXIV-2604-28182:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28182:end -->

<!-- books-review:SF-2026-ARXIV-2604-28190:start -->
<!-- existing:SF-2026-ARXIV-2604-28190:start -->
Ch24 已比较 AR、diffusion 与 iterative correction 的 factorization/serving 代价。
<!-- existing:SF-2026-ARXIV-2604-28190:end -->
<!-- delta:SF-2026-ARXIV-2604-28190:start -->
尚未补充 population-statistics 与 gradient batch 解耦后，Fréchet representation distance 可作为受限训练目标的分支。
<!-- delta:SF-2026-ARXIV-2604-28190:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-28190:end -->

<!-- books-review:SF-2026-ARXIV-2604-28196:start -->
<!-- existing:SF-2026-ARXIV-2604-28196:start -->
已核对 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 与 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-28196:end -->
<!-- delta:SF-2026-ARXIV-2604-28196:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-28196:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-28196:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260501-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260501 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260501-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260501-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=63；selected=3；all others retain completed reviews | passed |
| SA-20260501-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=493；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260501/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260501/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-01.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
