# Daily Research — 2026-05-20

**Research Date:** 2026-05-20

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-19 09:00:00 ～ 2026-05-20 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 727 个注册 arXiv identity，冻结 75 个 Source Family；pre-denominator closure=652，withdrawn pre-denominator=0。32 个旧候选被迁回正确 owner day，3 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-20 |
| Window End | 2026-05-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260520-CREATED-8ba5495e97ea385a |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-19T09:00:00+08:00 | 2026-05-20T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 727 | SF-2026-ARXIV-2605-18755;SF-2026-ARXIV-2605-18762;SF-2026-ARXIV-2605-18792;SF-2026-ARXIV-2605-18796;SF-2026-ARXIV-2605-18803;SF-2026-ARXIV-2605-18859;SF-2026-ARXIV-2605-18891;SF-2026-ARXIV-2605-18899;SF-2026-ARXIV-2605-18918;SF-2026-ARXIV-2605-18930;SF-2026-ARXIV-2605-18991;SF-2026-ARXIV-2605-19008;SF-2026-ARXIV-2605-19049;SF-2026-ARXIV-2605-19099;SF-2026-ARXIV-2605-19101;SF-2026-ARXIV-2605-19127;SF-2026-ARXIV-2605-19140;SF-2026-ARXIV-2605-19151;SF-2026-ARXIV-2605-19169;SF-2026-ARXIV-2605-19192;SF-2026-ARXIV-2605-19193;SF-2026-ARXIV-2605-19196;SF-2026-ARXIV-2605-19218;SF-2026-ARXIV-2605-19228;SF-2026-ARXIV-2605-19240;SF-2026-ARXIV-2605-19242;SF-2026-ARXIV-2605-19262;SF-2026-ARXIV-2605-19269;SF-2026-ARXIV-2605-19276;SF-2026-ARXIV-2605-19282;SF-2026-ARXIV-2605-19314;SF-2026-ARXIV-2605-19319;SF-2026-ARXIV-2605-19321;SF-2026-ARXIV-2605-19328;SF-2026-ARXIV-2605-19335;SF-2026-ARXIV-2605-19341;SF-2026-ARXIV-2605-19373;SF-2026-ARXIV-2605-19407;SF-2026-ARXIV-2605-19444;SF-2026-ARXIV-2605-19447;SF-2026-ARXIV-2605-19461;SF-2026-ARXIV-2605-19478;SF-2026-ARXIV-2605-19481;SF-2026-ARXIV-2605-19537;SF-2026-ARXIV-2605-19576;SF-2026-ARXIV-2605-19593;SF-2026-ARXIV-2605-19604;SF-2026-ARXIV-2605-19722;SF-2026-ARXIV-2605-19755;SF-2026-ARXIV-2605-19769;SF-2026-ARXIV-2605-19775;SF-2026-ARXIV-2605-19779;SF-2026-ARXIV-2605-19811;SF-2026-ARXIV-2605-19847;SF-2026-ARXIV-2605-19893;SF-2026-ARXIV-2605-19932;SF-2026-ARXIV-2605-19945;SF-2026-ARXIV-2605-19952;SF-2026-ARXIV-2605-19999;SF-2026-ARXIV-2605-20005;SF-2026-ARXIV-2605-20022;SF-2026-ARXIV-2605-20023;SF-2026-ARXIV-2605-20051;SF-2026-ARXIV-2605-20061;SF-2026-ARXIV-2605-20084;SF-2026-ARXIV-2605-20179;SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING;SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV;SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA;SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES;SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE;SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL;SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-;SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A;SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | created-day pages=closed; OAI category sets=closed; direct same-day OAI=575 | 2026-05-20T09:00:00+08:00 | coverage:SRC-ARXIV:20260520 | — |

<!-- coverage:SRC-ARXIV:20260520:start -->全量 raw inventory=727；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260520:end -->

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
| SF-2026-ARXIV-2605-18755 | arXiv:2605.18755v1 | paper-v1:2605.18755 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18755 | self | — | new_in_window | PLATFORM-LOGGING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18755 | yes |
| SF-2026-ARXIV-2605-18762 | arXiv:2605.18762v1 | paper-v1:2605.18762 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18762 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18762 | yes |
| SF-2026-ARXIV-2605-18792 | arXiv:2605.18792v1 | paper-v1:2605.18792 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18792 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18792 | no |
| SF-2026-ARXIV-2605-18796 | arXiv:2605.18796v1 | paper-v1:2605.18796 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18796 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18796 | no |
| SF-2026-ARXIV-2605-18803 | arXiv:2605.18803v1 | paper-v1:2605.18803 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18803 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18803 | no |
| SF-2026-ARXIV-2605-18859 | arXiv:2605.18859v1 | paper-v1:2605.18859 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18859 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-18859 | no |
| SF-2026-ARXIV-2605-18891 | arXiv:2605.18891v1 | paper-v1:2605.18891 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18891 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-18891 | no |
| SF-2026-ARXIV-2605-18899 | arXiv:2605.18899v1 | paper-v1:2605.18899 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18899 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 | no |
| SF-2026-ARXIV-2605-18918 | arXiv:2605.18918v1 | paper-v1:2605.18918 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18918 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18918 | no |
| SF-2026-ARXIV-2605-18930 | arXiv:2605.18930v1 | paper-v1:2605.18930 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18930 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18930 | no |
| SF-2026-ARXIV-2605-18991 | arXiv:2605.18991v1 | paper-v1:2605.18991 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18991 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18991 | no |
| SF-2026-ARXIV-2605-19008 | arXiv:2605.19008v1 | paper-v1:2605.19008 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19008 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19008 | no |
| SF-2026-ARXIV-2605-19049 | arXiv:2605.19049v1 | paper-v1:2605.19049 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19049 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-19049 | no |
| SF-2026-ARXIV-2605-19099 | arXiv:2605.19099v1 | paper-v1:2605.19099 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19099 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19099 | no |
| SF-2026-ARXIV-2605-19101 | arXiv:2605.19101v1 | paper-v1:2605.19101 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19101 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19101 | no |
| SF-2026-ARXIV-2605-19127 | arXiv:2605.19127v1 | paper-v1:2605.19127 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19127 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19127 | no |
| SF-2026-ARXIV-2605-19140 | arXiv:2605.19140v1 | paper-v1:2605.19140 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19140 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19140 | no |
| SF-2026-ARXIV-2605-19151 | arXiv:2605.19151v1 | paper-v1:2605.19151 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19151 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19151 | no |
| SF-2026-ARXIV-2605-19169 | arXiv:2605.19169v1 | paper-v1:2605.19169 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19169 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19169 | no |
| SF-2026-ARXIV-2605-19192 | arXiv:2605.19192v1 | paper-v1:2605.19192 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19192 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19192 | no |
| SF-2026-ARXIV-2605-19193 | arXiv:2605.19193v1 | paper-v1:2605.19193 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19193 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19193 | no |
| SF-2026-ARXIV-2605-19196 | arXiv:2605.19196v1 | paper-v1:2605.19196 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19196 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19196 | no |
| SF-2026-ARXIV-2605-19218 | arXiv:2605.19218v1 | paper-v1:2605.19218 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19218 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19218 | no |
| SF-2026-ARXIV-2605-19228 | arXiv:2605.19228v1 | paper-v1:2605.19228 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19228 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19228 | no |
| SF-2026-ARXIV-2605-19240 | arXiv:2605.19240v1 | paper-v1:2605.19240 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19240 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19240 | no |
| SF-2026-ARXIV-2605-19242 | arXiv:2605.19242v1 | paper-v1:2605.19242 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19242 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 | no |
| SF-2026-ARXIV-2605-19262 | arXiv:2605.19262v1 | paper-v1:2605.19262 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19262 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 | no |
| SF-2026-ARXIV-2605-19269 | arXiv:2605.19269v1 | paper-v1:2605.19269 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19269 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-19269 | no |
| SF-2026-ARXIV-2605-19276 | arXiv:2605.19276v1 | paper-v1:2605.19276 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19276 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 | no |
| SF-2026-ARXIV-2605-19282 | arXiv:2605.19282v1 | paper-v1:2605.19282 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19282 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19282 | no |
| SF-2026-ARXIV-2605-19314 | arXiv:2605.19314v1 | paper-v1:2605.19314 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19314 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-19314 | no |
| SF-2026-ARXIV-2605-19319 | arXiv:2605.19319v1 | paper-v1:2605.19319 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19319 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-19319 | no |
| SF-2026-ARXIV-2605-19321 | arXiv:2605.19321v1 | paper-v1:2605.19321 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19321 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19321 | no |
| SF-2026-ARXIV-2605-19328 | arXiv:2605.19328v1 | paper-v1:2605.19328 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19328 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 | no |
| SF-2026-ARXIV-2605-19335 | arXiv:2605.19335v1 | paper-v1:2605.19335 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19335 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-19335 | no |
| SF-2026-ARXIV-2605-19341 | arXiv:2605.19341v1 | paper-v1:2605.19341 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19341 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 | no |
| SF-2026-ARXIV-2605-19373 | arXiv:2605.19373v1 | paper-v1:2605.19373 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19373 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2026-ARXIV-2605-19373 | no |
| SF-2026-ARXIV-2605-19407 | arXiv:2605.19407v1 | paper-v1:2605.19407 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19407 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-19407 | no |
| SF-2026-ARXIV-2605-19444 | arXiv:2605.19444v1 | paper-v1:2605.19444 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19444 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19444 | no |
| SF-2026-ARXIV-2605-19447 | arXiv:2605.19447v1 | paper-v1:2605.19447 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19447 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19447 | no |
| SF-2026-ARXIV-2605-19461 | arXiv:2605.19461v1 | paper-v1:2605.19461 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19461 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-19461 | no |
| SF-2026-ARXIV-2605-19478 | arXiv:2605.19478v1 | paper-v1:2605.19478 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19478 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19478 | no |
| SF-2026-ARXIV-2605-19481 | arXiv:2605.19481v1 | paper-v1:2605.19481 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19481 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2605-19481 | no |
| SF-2026-ARXIV-2605-19537 | arXiv:2605.19537v1 | paper-v1:2605.19537 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19537 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19537 | no |
| SF-2026-ARXIV-2605-19576 | arXiv:2605.19576v1 | paper-v1:2605.19576 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19576 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19576 | no |
| SF-2026-ARXIV-2605-19593 | arXiv:2605.19593v1 | paper-v1:2605.19593 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19593 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19593 | no |
| SF-2026-ARXIV-2605-19604 | arXiv:2605.19604v1 | paper-v1:2605.19604 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19604 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-19604 | no |
| SF-2026-ARXIV-2605-19722 | arXiv:2605.19722v1 | paper-v1:2605.19722 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19722 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19722 | no |
| SF-2026-ARXIV-2605-19755 | arXiv:2605.19755v1 | paper-v1:2605.19755 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19755 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19755 | yes |
| SF-2026-ARXIV-2605-19769 | arXiv:2605.19769v1 | paper-v1:2605.19769 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19769 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 | no |
| SF-2026-ARXIV-2605-19775 | arXiv:2605.19775v1 | paper-v1:2605.19775 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19775 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 | no |
| SF-2026-ARXIV-2605-19779 | arXiv:2605.19779v1 | paper-v1:2605.19779 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19779 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-19779 | no |
| SF-2026-ARXIV-2605-19811 | arXiv:2605.19811v1 | paper-v1:2605.19811 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19811 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19811 | no |
| SF-2026-ARXIV-2605-19847 | arXiv:2605.19847v1 | paper-v1:2605.19847 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19847 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-19847 | no |
| SF-2026-ARXIV-2605-19893 | arXiv:2605.19893v1 | paper-v1:2605.19893 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19893 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-19893 | no |
| SF-2026-ARXIV-2605-19932 | arXiv:2605.19932v1 | paper-v1:2605.19932 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19932 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-19932 | no |
| SF-2026-ARXIV-2605-19945 | arXiv:2605.19945v1 | paper-v1:2605.19945 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19945 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-19945 | no |
| SF-2026-ARXIV-2605-19952 | arXiv:2605.19952v1 | paper-v1:2605.19952 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19952 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-19952 | no |
| SF-2026-ARXIV-2605-19999 | arXiv:2605.19999v1 | paper-v1:2605.19999 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19999 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 | no |
| SF-2026-ARXIV-2605-20005 | arXiv:2605.20005v1 | paper-v1:2605.20005 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20005 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2605-20005 | no |
| SF-2026-ARXIV-2605-20022 | arXiv:2605.20022v1 | paper-v1:2605.20022 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20022 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-20022 | no |
| SF-2026-ARXIV-2605-20023 | arXiv:2605.20023v1 | paper-v1:2605.20023 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20023 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 | no |
| SF-2026-ARXIV-2605-20051 | arXiv:2605.20051v1 | paper-v1:2605.20051 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20051 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-20051 | no |
| SF-2026-ARXIV-2605-20061 | arXiv:2605.20061v1 | paper-v1:2605.20061 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20061 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-20061 | no |
| SF-2026-ARXIV-2605-20084 | arXiv:2605.20084v1 | paper-v1:2605.20084 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20084 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-20084 | no |
| SF-2026-ARXIV-2605-20179 | arXiv:2605.20179v1 | paper-v1:2605.20179 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-20179 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-20179 | no |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | arXiv:2605.18815v1 | paper-v1:2605.18815 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | no |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | arXiv:2605.18854v1 | paper-v1:2605.18854 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | no |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | arXiv:2605.18824v1 | paper-v1:2605.18824 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | no |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | arXiv:2605.18814v1 | paper-v1:2605.18814 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | no |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | arXiv:2605.18853v1 | paper-v1:2605.18853 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | no |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | arXiv:2605.18825v1 | paper-v1:2605.18825 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | no |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | arXiv:2605.18812v1 | paper-v1:2605.18812 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | no |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | arXiv:2605.18852v1 | paper-v1:2605.18852 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | no |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | arXiv:2605.18856v1 | paper-v1:2605.18856 | 2026-W21 | 2026-05-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | RP-10421f11c0c05fee | deep | arXiv:2605.18755v1 | SRC-ARXIV@arXiv:2605.18755v1 | https://arxiv.org/html/2605.18755v1#S2 | https://arxiv.org/html/2605.18755v1#S4 | https://arxiv.org/html/2605.18755v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-18755 | complete |
| SF-2026-ARXIV-2605-18762 | RP-d07f2bb444275d67 | deep | arXiv:2605.18762v1 | SRC-ARXIV@arXiv:2605.18762v1 | https://arxiv.org/html/2605.18762v1#S2 | https://arxiv.org/html/2605.18762v1#S4 | https://arxiv.org/html/2605.18762v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-18762 | complete |
| SF-2026-ARXIV-2605-18792 | RP-7c4961ebc928422c | deep | arXiv:2605.18792v1 | SRC-ARXIV@arXiv:2605.18792v1 | arXiv:2605.18792v1 §2 knowledge-conflict benchmark; §3 self-prior, conditional belief estimation and abstention — parametric and contextual knowledge beliefs govern retrieval and abstention | arXiv:2605.18792v1 §4 Experiments, selective answering and ablations | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18792v1 No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18792 | complete |
| SF-2026-ARXIV-2605-18796 | RP-ecb151b4d0133aa8 | deep | arXiv:2605.18796v1 | SRC-ARXIV@arXiv:2605.18796v1 | arXiv:2605.18796v1 §3 formulation; §4 calibrated uncertainty and threshold policy; §5 theory — calibrated correctness and cost jointly select a model cascade | arXiv:2605.18796v1 §6 Experiments and diagnostics | arXiv:2605.18796v1 §7 Discussion and Limitations | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18796 | complete |
| SF-2026-ARXIV-2605-18803 | RP-fb6876e49931644e | deep | arXiv:2605.18803v1 | SRC-ARXIV@arXiv:2605.18803v1 | arXiv:2605.18803v1 §3 PROWL: asymmetric min-max objective, chunked diffusion forcing and adversarial curriculum — adversarial curriculum and prioritized failures change world-model training state | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Evaluation fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Evaluation, prioritized-failure and ablation sections | Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Limitations discussion; world-model backbone, environments and regret proxy bound generality | Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body | claim:SF-2026-ARXIV-2605-18803 | complete |
| SF-2026-ARXIV-2605-18859 | RP-35caa4f2dad6931c | deep | arXiv:2605.18859v1 | SRC-ARXIV@arXiv:2605.18859v1 | https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls. | https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-18859 | complete |
| SF-2026-ARXIV-2605-18891 | RP-95ea8bc96626981c | deep | arXiv:2605.18891v1 | SRC-ARXIV@arXiv:2605.18891v1 | arXiv:2605.18891v1 — §3 Setup and the Bypass Metric (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §4 Results (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §5 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-g.txt#sha256=804cad573138683e86544b653813a5ca64961d7fe4c52ed742315b9a7f54ce63; exact-v1 URL=https://arxiv.org/html/2605.18891v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18891 | complete |
| SF-2026-ARXIV-2605-18899 | RP-de7028b2b7ed378a | deep | arXiv:2605.18899v1 | SRC-ARXIV@arXiv:2605.18899v1 | arXiv:2605.18899v1 — §3 Anchored Bandit Policy Optimization (official exact-v1 HTML) | arXiv:2605.18899v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.18899v1 — Appendix E.4 Scope limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.18899v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18899 | complete |
| SF-2026-ARXIV-2605-18918 | RP-92e4f3c42456da80 | deep | arXiv:2605.18918v1 | SRC-ARXIV@arXiv:2605.18918v1 | arXiv:2605.18918v1 HTML — §3 ESLD latent sensor architecture and external enforcement path | arXiv:2605.18918v1 HTML — §4 Experiments against prompt injection | arXiv:2605.18918v1 HTML — §5 Limitations; learned detector is not an authority | arXiv:2605.18918v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18918 | complete |
| SF-2026-ARXIV-2605-18930 | RP-0044fd324e10c1d9 | deep | arXiv:2605.18930v1 | SRC-ARXIV@arXiv:2605.18930v1 | arXiv:2605.18930v1 HTML — §3 threat model; §4.1–4.2 poisoning | arXiv:2605.18930v1 HTML — §5 mechanistic analysis; §6 evaluation | arXiv:2605.18930v1 HTML — §7 limitations | arXiv:2605.18930v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18930 | complete |
| SF-2026-ARXIV-2605-18991 | RP-4923f6156c159e4f | deep | arXiv:2605.18991v1 | SRC-ARXIV@arXiv:2605.18991v1 | arXiv:2605.18991v1 HTML — §2 system-level invariants, model-as-untrusted-component and attack analysis | arXiv:2605.18991v1 HTML — §3 open systems-security problems; no empirical mechanism evaluation | arXiv:2605.18991v1 HTML — §4 objections and position-paper boundary | arXiv:2605.18991v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18991 | complete |
| SF-2026-ARXIV-2605-19008 | RP-e156c3001ce0a6ba | deep | arXiv:2605.19008v1 | SRC-ARXIV@arXiv:2605.19008v1 | arXiv:2605.19008v1 HTML — §3 LBW-Guard bounded training-control layer, actions and safety envelope | arXiv:2605.19008v1 HTML — §4–§5 setup, stress runs and controller outcomes | arXiv:2605.19008v1 HTML — §6 Limitations; simulator/recipe and stability boundary | arXiv:2605.19008v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19008 | complete |
| SF-2026-ARXIV-2605-19049 | RP-153638f65b985ca9 | deep | arXiv:2605.19049v1 | SRC-ARXIV@arXiv:2605.19049v1 | arXiv:2605.19049v1 HTML — §3.1–§3.4 KVBuffer IO-aware state placement and update pipeline | arXiv:2605.19049v1 HTML — §4 Evaluation on linear-attention serving | arXiv:2605.19049v1 HTML — §6 Discussion/limitations; linear-attention state only | arXiv:2605.19049v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19049 | complete |
| SF-2026-ARXIV-2605-19099 | RP-ebae37d76cd708ea | deep | arXiv:2605.19099v1 | SRC-ARXIV@arXiv:2605.19099v1 | arXiv:2605.19099v1 HTML — §3 DecisionBench delegation substrate, interface and metrics | arXiv:2605.19099v1 HTML — §4 Experiments across peer pools and tasks | arXiv:2605.19099v1 HTML — §5 Limitations; benchmark delegation is not production authority | arXiv:2605.19099v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19099 | complete |
| SF-2026-ARXIV-2605-19101 | RP-8c36c0c8793720bd | deep | arXiv:2605.19101v1 | SRC-ARXIV@arXiv:2605.19101v1 | arXiv:2605.19101v1 HTML — §3–§4 GST heterogeneity state, scheduler and optimization rule | arXiv:2605.19101v1 HTML — §5 Experiments on Audio LLM training | arXiv:2605.19101v1 HTML — §6 Limitations; audio datasets and selected recipes | arXiv:2605.19101v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19101 | complete |
| SF-2026-ARXIV-2605-19127 | RP-037480cb13b63529 | deep | arXiv:2605.19127v1 | SRC-ARXIV@arXiv:2605.19127v1 | arXiv:2605.19127v1 HTML — §3.1–3.6 policy/attack/evaluation contract | arXiv:2605.19127v1 HTML — §4–§5 diagnostic surface | arXiv:2605.19127v1 HTML — §6 Limitations | arXiv:2605.19127v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19127 | complete |
| SF-2026-ARXIV-2605-19140 | RP-8a5d21f5abe58713 | deep | arXiv:2605.19140v1 | SRC-ARXIV@arXiv:2605.19140v1 | arXiv:2605.19140v1 HTML — §3–§4 local-observation handoff interface and convergent learning rule | arXiv:2605.19140v1 HTML — §5 theoretical/empirical evaluation | arXiv:2605.19140v1 HTML — §6 Limitations; assumptions do not prove open-system delivery or authority | arXiv:2605.19140v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19140 | complete |
| SF-2026-ARXIV-2605-19151 | RP-5aed86fc7416098f | deep | arXiv:2605.19151v1 | SRC-ARXIV@arXiv:2605.19151v1 | arXiv:2605.19151v1 HTML — §2–§3 approval/deny observations, GP preference posterior and autonomy threshold | arXiv:2605.19151v1 HTML — §3–§4 theoretical and simulated evaluation | arXiv:2605.19151v1 HTML — §4 Limitations; preference stationarity and calibration boundary | arXiv:2605.19151v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19151 | complete |
| SF-2026-ARXIV-2605-19169 | RP-40eb64e1b509dd01 | deep | arXiv:2605.19169v1 | SRC-ARXIV@arXiv:2605.19169v1 | arXiv:2605.19169v1 HTML — §2 Methods; latency/serialization model and ASTRA-sim overlap model | arXiv:2605.19169v1 HTML — §3 Results; GPT-3 13B/175B, A100/H100, 256–8192 GPU simulation | arXiv:2605.19169v1 HTML — §4 Conclusions; lumped two-DC, uncongested-network and simulation-only boundary | arXiv:2605.19169v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19169 | complete |
| SF-2026-ARXIV-2605-19192 | RP-674c2cb06c4707c0 | deep | arXiv:2605.19192v1 | SRC-ARXIV@arXiv:2605.19192v1 | arXiv:2605.19192v1 HTML — §3–§4 evidence certificate and action-admission architecture | arXiv:2605.19192v1 HTML — §5 Evaluation under multimodal hallucination-to-action attacks | arXiv:2605.19192v1 HTML — §6 Limitations; certificate coverage and evaluator trust | arXiv:2605.19192v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19192 | complete |
| SF-2026-ARXIV-2605-19193 | RP-0ac837392fe4f247 | deep | arXiv:2605.19193v1 | SRC-ARXIV@arXiv:2605.19193v1 | arXiv:2605.19193v1 HTML — §III–V sequential stopping and calibration | arXiv:2605.19193v1 HTML — §VI simulation; §VII real-LLM study | arXiv:2605.19193v1 HTML — §V-E i.i.d. violations; §VIII discussion | arXiv:2605.19193v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19193 | complete |
| SF-2026-ARXIV-2605-19196 | RP-a0a24df6793a2acd | deep | arXiv:2605.19196v1 | SRC-ARXIV@arXiv:2605.19196v1 | arXiv:2605.19196v1 HTML — §2.1–2.2 controlled-intervention benchmark | arXiv:2605.19196v1 HTML — §3.1–3.5 judge meta-evaluation | arXiv:2605.19196v1 HTML — §4 related work; §5 conclusion | arXiv:2605.19196v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19196 | complete |
| SF-2026-ARXIV-2605-19218 | RP-71652ae2e632c2a7 | deep | arXiv:2605.19218v1 | SRC-ARXIV@arXiv:2605.19218v1 | arXiv:2605.19218v1 HTML — §3.1–§3.3 RotateK query-weighted PCA, structured channel pruning and Triton kernel | arXiv:2605.19218v1 HTML — §4 Experiments; matched KV budgets, prefill/decode latency and memory | arXiv:2605.19218v1 HTML — Appendix G Limitations | arXiv:2605.19218v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19218 | complete |
| SF-2026-ARXIV-2605-19228 | RP-822c0c4354bc34dc | deep | arXiv:2605.19228v1 | SRC-ARXIV@arXiv:2605.19228v1 | arXiv:2605.19228v1 HTML — §3 problem; §4.1–4.3 step confidence | arXiv:2605.19228v1 HTML — §5 experiments | arXiv:2605.19228v1 HTML — §6 limitations | arXiv:2605.19228v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-19228 | complete |
| SF-2026-ARXIV-2605-19240 | RP-4de7916633823656 | deep | arXiv:2605.19240v1 | SRC-ARXIV@arXiv:2605.19240v1 | arXiv:2605.19240v1 HTML — §4.1–4.4 causal cross-channel monitoring | arXiv:2605.19240v1 HTML — §5 detection and attribution evaluation | arXiv:2605.19240v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19240v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19240 | complete |
| SF-2026-ARXIV-2605-19242 | RP-bc66eb851cc20588 | deep | arXiv:2605.19242v1 | SRC-ARXIV@arXiv:2605.19242v1 | arXiv:2605.19242v1 HTML — §3 physics-faithful data and objective | arXiv:2605.19242v1 HTML — §4 controlled video/world-model evaluation | arXiv:2605.19242v1 HTML — §5 Conclusion and inherited generator biases | https://arxiv.org/html/2605.19242v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19242 | complete |
| SF-2026-ARXIV-2605-19262 | RP-5a772c65a8c3c199 | deep | arXiv:2605.19262v1 | SRC-ARXIV@arXiv:2605.19262v1 | arXiv:2605.19262v1 HTML — §4 masked-diffusion backdoor construction | arXiv:2605.19262v1 HTML — §5 attack and defense experiments | arXiv:2605.19262v1 HTML — Appendix A Limitations | https://arxiv.org/html/2605.19262v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19262 | complete |
| SF-2026-ARXIV-2605-19269 | RP-c96f6605cb2f6e46 | deep | arXiv:2605.19269v1 | SRC-ARXIV@arXiv:2605.19269v1 | arXiv:2605.19269v1 HTML — §3 GEMM-epilogue program representation | arXiv:2605.19269v1 HTML — §4 kernel and end-to-end evaluation | arXiv:2605.19269v1 HTML — §5 limitations and portability boundary | https://arxiv.org/html/2605.19269v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19269 | complete |
| SF-2026-ARXIV-2605-19276 | RP-bbd40a725e79e647 | deep | arXiv:2605.19276v1 | SRC-ARXIV@arXiv:2605.19276v1 | arXiv:2605.19276v1 HTML — §3.1–3.5 evaluation-platform architecture | arXiv:2605.19276v1 HTML — §4 benchmark execution and comparison | arXiv:2605.19276v1 HTML — §5 Future Works | https://arxiv.org/html/2605.19276v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19276 | complete |
| SF-2026-ARXIV-2605-19282 | RP-2a2084963c482440 | deep | arXiv:2605.19282v1 | SRC-ARXIV@arXiv:2605.19282v1 | arXiv:2605.19282v1 HTML — §3 spectral failure analysis; §4 high-pass remedy | arXiv:2605.19282v1 HTML — §5 VLA/RLVR optimization experiments | arXiv:2605.19282v1 HTML — Appendix M Limitations | https://arxiv.org/html/2605.19282v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19282 | complete |
| SF-2026-ARXIV-2605-19314 | RP-2cbc2c4c9f3e9bf9 | deep | arXiv:2605.19314v1 | SRC-ARXIV@arXiv:2605.19314v1 | arXiv:2605.19314v1 HTML — §3 hierarchical task-state alignment | arXiv:2605.19314v1 HTML — §4.1–4.4 long-horizon embodied evaluation | arXiv:2605.19314v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19314v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19314 | complete |
| SF-2026-ARXIV-2605-19319 | RP-5e77ad5261b0bf4f | deep | arXiv:2605.19319v1 | SRC-ARXIV@arXiv:2605.19319v1 | arXiv:2605.19319v1 HTML — §3 sparse keyframe world-model planner and goal-conditioned action predictor | arXiv:2605.19319v1 HTML — §4 real-robot and simulation experiments | arXiv:2605.19319v1 HTML — §5 Limitations: short horizon, annotations and edited-image domain gap | https://arxiv.org/html/2605.19319v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19319 | complete |
| SF-2026-ARXIV-2605-19321 | RP-d33cdabd99e9957c | deep | arXiv:2605.19321v1 | SRC-ARXIV@arXiv:2605.19321v1 | arXiv:2605.19321v1 HTML — §3 draft-model pre-guard design | arXiv:2605.19321v1 HTML — §6 jailbreak and latency evaluation | arXiv:2605.19321v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19321v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19321 | complete |
| SF-2026-ARXIV-2605-19328 | RP-a5c0a05c1cd5ca31 | deep | arXiv:2605.19328v1 | SRC-ARXIV@arXiv:2605.19328v1 | arXiv:2605.19328v1 HTML — §3 embodied-agent threat and benchmark protocol | arXiv:2605.19328v1 HTML — §4 attacks and defenses | arXiv:2605.19328v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19328v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19328 | complete |
| SF-2026-ARXIV-2605-19335 | RP-4d11184eb7d065fd | deep | arXiv:2605.19335v1 | SRC-ARXIV@arXiv:2605.19335v1 | arXiv:2605.19335v1 HTML — §4 LIOS update decomposition, overrun-bounded budgeting and feedback control | arXiv:2605.19335v1 HTML — §6 search/update evaluation on FreshDiskANN and OdinANN | arXiv:2605.19335v1 HTML — §8 Conclusion; disk ANNS and measured hardware scope | https://arxiv.org/html/2605.19335v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19335 | complete |
| SF-2026-ARXIV-2605-19341 | RP-38bfb8462e1788ff | deep | arXiv:2605.19341v1 | SRC-ARXIV@arXiv:2605.19341v1 | arXiv:2605.19341v1 HTML — §3.1–3.3 controlled reference-world benchmark | arXiv:2605.19341v1 HTML — §4 cross-context hallucination experiments | arXiv:2605.19341v1 HTML — §5 Discussion; controlled-world boundary | https://arxiv.org/html/2605.19341v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19341 | complete |
| SF-2026-ARXIV-2605-19373 | RP-100563ab07b862d8 | deep | arXiv:2605.19373v1 | SRC-ARXIV@arXiv:2605.19373v1 | section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture) | section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations) | section 7 Discussion (§7 Discussion) | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.19373v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-19373 | complete |
| SF-2026-ARXIV-2605-19407 | RP-231b13021875ae63 | deep | arXiv:2605.19407v1 | SRC-ARXIV@arXiv:2605.19407v1 | arXiv:2605.19407v1 HTML — §3–§6 compute/data/filter scaling design | arXiv:2605.19407v1 HTML — §6–§7 scaling experiments | arXiv:2605.19407v1 HTML — §8 Discussion and scope boundary | https://arxiv.org/html/2605.19407v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19407 | complete |
| SF-2026-ARXIV-2605-19444 | RP-e2adfa9f6bdc8469 | deep | arXiv:2605.19444v1 | SRC-ARXIV@arXiv:2605.19444v1 | arXiv:2605.19444v1 HTML — §2 extinction-window dynamics; §3 TTRL-Guard | arXiv:2605.19444v1 HTML — §4 model/benchmark experiments and per-problem migration | arXiv:2605.19444v1 HTML — §6 Breadth of evaluation; signal quality at the extremes | https://arxiv.org/html/2605.19444v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19444 | complete |
| SF-2026-ARXIV-2605-19447 | RP-79adcf64a80e6d6d | deep | arXiv:2605.19447v1 | SRC-ARXIV@arXiv:2605.19447v1 | arXiv:2605.19447v1 HTML — §3 selective hindsight placement and environment-guided advantage reweighting | arXiv:2605.19447v1 HTML — §4 ALFWorld/WebShop experiments and ablations | arXiv:2605.19447v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.19447v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19447 | complete |
| SF-2026-ARXIV-2605-19461 | RP-487abf8826107f40 | deep | arXiv:2605.19461v1 | SRC-ARXIV@arXiv:2605.19461v1 | arXiv:2605.19461v1 HTML — §3 forward/group distribution-matching policy optimization | arXiv:2605.19461v1 HTML — §4–§5 reasoning experiments and ablations | arXiv:2605.19461v1 HTML — Appendix B Limitations; group-local coverage does not prove global target matching | https://arxiv.org/html/2605.19461v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19461 | complete |
| SF-2026-ARXIV-2605-19478 | RP-364a9e53a3f33227 | deep | arXiv:2605.19478v1 | SRC-ARXIV@arXiv:2605.19478v1 | arXiv:2605.19478v1 HTML — §4 threat model; §5–§6 dynamic-prompt functional fusion | arXiv:2605.19478v1 HTML — §7 attack, pruning and transfer evaluation | arXiv:2605.19478v1 HTML — §8 Conclusion; ViT/VPT threat-model boundary | https://arxiv.org/html/2605.19478v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19478 | complete |
| SF-2026-ARXIV-2605-19481 | RP-c5cf1a54d2cf261f | deep | arXiv:2605.19481v1 | SRC-ARXIV@arXiv:2605.19481v1 | arXiv:2605.19481v1 HTML — §III–V C2C weight/state movement design | arXiv:2605.19481v1 HTML — §VI MIG/serverless serving evaluation | arXiv:2605.19481v1 HTML — §VII Conclusion and hardware boundary | https://arxiv.org/html/2605.19481v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19481 | complete |
| SF-2026-ARXIV-2605-19537 | RP-7c3307e883eee92e | deep | arXiv:2605.19537v1 | SRC-ARXIV@arXiv:2605.19537v1 | arXiv:2605.19537v1 HTML — §3 backend-reproducibility protocol | arXiv:2605.19537v1 HTML — §4 backend/model benchmark deltas | arXiv:2605.19537v1 HTML — §5 Discussion and reproducibility boundary | https://arxiv.org/html/2605.19537v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19537 | complete |
| SF-2026-ARXIV-2605-19576 | RP-a9ccb737bed9e193 | deep | arXiv:2605.19576v1 | SRC-ARXIV@arXiv:2605.19576v1 | arXiv:2605.19576v1 HTML — §3–§5 lifecycle-managed skill library | arXiv:2605.19576v1 HTML — §6 library-drift evaluation | arXiv:2605.19576v1 HTML — §7 Limitations | https://arxiv.org/html/2605.19576v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19576 | complete |
| SF-2026-ARXIV-2605-19593 | RP-0f47708fa3dff185 | deep | arXiv:2605.19593v1 | SRC-ARXIV@arXiv:2605.19593v1 | arXiv:2605.19593v1 HTML — §3 multi-model offload/preemption methodology | arXiv:2605.19593v1 HTML — §4–§5 heterogeneous-serving measurements | arXiv:2605.19593v1 HTML — §6 Conclusion; interconnect and hardware constraints | https://arxiv.org/html/2605.19593v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19593 | complete |
| SF-2026-ARXIV-2605-19604 | RP-fccbad05e0667a78 | deep | arXiv:2605.19604v1 | SRC-ARXIV@arXiv:2605.19604v1 | arXiv:2605.19604v1 HTML — §3 programmable runtime skill contract | arXiv:2605.19604v1 HTML — §4 execution and accuracy evaluation | arXiv:2605.19604v1 HTML — §5 Conclusion; language/runtime boundary | https://arxiv.org/html/2605.19604v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19604 | complete |
| SF-2026-ARXIV-2605-19722 | RP-5fd2a3cffdd101d8 | deep | arXiv:2605.19722v1 | SRC-ARXIV@arXiv:2605.19722v1 | arXiv:2605.19722v1 HTML — §3 trace-based autonomous security-agent protocol | arXiv:2605.19722v1 HTML — §4–§5 sandbox/tool-use evaluation | arXiv:2605.19722v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19722v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19722 | complete |
| SF-2026-ARXIV-2605-19755 | RP-6c6c2fd691379eb4 | deep | arXiv:2605.19755v1 | SRC-ARXIV@arXiv:2605.19755v1 | https://arxiv.org/html/2605.19755v1#S2 | https://arxiv.org/html/2605.19755v1#S4 | https://arxiv.org/html/2605.19755v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-19755 | complete |
| SF-2026-ARXIV-2605-19769 | RP-abeedde730e8f1d5 | deep | arXiv:2605.19769v1 | SRC-ARXIV@arXiv:2605.19769v1 | arXiv:2605.19769v1 HTML — §2–§3 verifier-grounded software worlds | arXiv:2605.19769v1 HTML — §4.1 computer-use agent evaluation | arXiv:2605.19769v1 HTML — § unnumbered exact heading ‘Limitations and Future Work’ | https://arxiv.org/html/2605.19769v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19769 | complete |
| SF-2026-ARXIV-2605-19775 | RP-cb624bce171b6667 | deep | arXiv:2605.19775v1 | SRC-ARXIV@arXiv:2605.19775v1 | arXiv:2605.19775v1 HTML — §2–§3 inference-scaling model | arXiv:2605.19775v1 HTML — §4–§5 reasoning-workload measurements | arXiv:2605.19775v1 HTML — §6 Conclusions and disclosed scope | https://arxiv.org/html/2605.19775v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19775 | complete |
| SF-2026-ARXIV-2605-19779 | RP-9170e3bce78cea00 | deep | arXiv:2605.19779v1 | SRC-ARXIV@arXiv:2605.19779v1 | arXiv:2605.19779v1 HTML — §2–§3 conformal continuous-agent UQ | arXiv:2605.19779v1 HTML — §4 longitudinal agent studies | arXiv:2605.19779v1 HTML — §5 Limitations: bounded shift and dependence | https://arxiv.org/html/2605.19779v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19779 | complete |
| SF-2026-ARXIV-2605-19811 | RP-73b18d970281f078 | deep | arXiv:2605.19811v1 | SRC-ARXIV@arXiv:2605.19811v1 | arXiv:2605.19811v1 HTML — §3 optimizer geometry; §4 LionMuon alternating spectral/sign descent | arXiv:2605.19811v1 HTML — §5 language-model training experiments and ablations | arXiv:2605.19811v1 HTML — §6 Limitations and optimizer/workload boundary | https://arxiv.org/html/2605.19811v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19811 | complete |
| SF-2026-ARXIV-2605-19847 | RP-1aad2db51346f336 | deep | arXiv:2605.19847v1 | SRC-ARXIV@arXiv:2605.19847v1 | arXiv:2605.19847v1 HTML — §2–§3 collusion threat model and tenant accounting | arXiv:2605.19847v1 HTML — §4 privacy audit; §5 protocol | arXiv:2605.19847v1 HTML — §7.1 Limitations: retrieval only, not generation | https://arxiv.org/html/2605.19847v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19847 | complete |
| SF-2026-ARXIV-2605-19893 | RP-443e8b0329a419a2 | deep | arXiv:2605.19893v1 | SRC-ARXIV@arXiv:2605.19893v1 | arXiv:2605.19893v1 HTML — §3–§4 sparse speculative verification | arXiv:2605.19893v1 HTML — §5 long-context evaluation | arXiv:2605.19893v1 HTML — §6 Conclusion and sparse-attention boundary | https://arxiv.org/html/2605.19893v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19893 | complete |
| SF-2026-ARXIV-2605-19932 | RP-26b2069b16f34d38 | deep | arXiv:2605.19932v1 | SRC-ARXIV@arXiv:2605.19932v1 | arXiv:2605.19932v1 HTML — §3 orientation-cache representation | arXiv:2605.19932v1 HTML — §4 recurring-context agent evaluation | arXiv:2605.19932v1 HTML — §5 Limitations | https://arxiv.org/html/2605.19932v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19932 | complete |
| SF-2026-ARXIV-2605-19945 | RP-3896ccf40dc4ab6d | deep | arXiv:2605.19945v1 | SRC-ARXIV@arXiv:2605.19945v1 | arXiv:2605.19945v1 HTML — §3–§4 variability-aware expert placement | arXiv:2605.19945v1 HTML — §5 heterogeneous-GPU evaluation | arXiv:2605.19945v1 HTML — §6 Limitations | https://arxiv.org/html/2605.19945v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19945 | complete |
| SF-2026-ARXIV-2605-19952 | RP-a53c47202f099e7a | deep | arXiv:2605.19952v1 | SRC-ARXIV@arXiv:2605.19952v1 | arXiv:2605.19952v1 HTML — §3 trace/chunk memory representation | arXiv:2605.19952v1 HTML — §4 lifelong-memory evaluation | arXiv:2605.19952v1 HTML — Appendix C.1 Limitations | https://arxiv.org/html/2605.19952v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19952 | complete |
| SF-2026-ARXIV-2605-19999 | RP-f5326dc8eaa49252 | deep | arXiv:2605.19999v1 | SRC-ARXIV@arXiv:2605.19999v1 | arXiv:2605.19999v1 HTML — §3–§4 contamination-resistant benchmark construction | arXiv:2605.19999v1 HTML — §5 benchmark analysis | arXiv:2605.19999v1 HTML — § unnumbered exact heading ‘Limitations’: contamination detection and task scope | https://arxiv.org/html/2605.19999v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-19999 | complete |
| SF-2026-ARXIV-2605-20005 | RP-11cbff9a3b48da86 | deep | arXiv:2605.20005v1 | SRC-ARXIV@arXiv:2605.20005v1 | arXiv:2605.20005v1 HTML — §3 per-step forgetting bound and loss-adaptive learning rate | arXiv:2605.20005v1 HTML — §4–§5 task/forgetting, factuality and calibration experiments | arXiv:2605.20005v1 HTML — §6 Conclusion, Limitations, and Future Work | https://arxiv.org/html/2605.20005v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20005 | complete |
| SF-2026-ARXIV-2605-20022 | RP-8ea859d9af48ceee | deep | arXiv:2605.20022v1 | SRC-ARXIV@arXiv:2605.20022v1 | arXiv:2605.20022v1 HTML — §3–§4 asynchronous flexible drafting | arXiv:2605.20022v1 HTML — §5 end-to-end evaluation | arXiv:2605.20022v1 HTML — §6 Conclusion: bonus-token and accepted-length uncertainty | https://arxiv.org/html/2605.20022v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20022 | complete |
| SF-2026-ARXIV-2605-20023 | RP-bf3892f84b15bf42 | deep | arXiv:2605.20023v1 | SRC-ARXIV@arXiv:2605.20023v1 | arXiv:2605.20023v1 HTML — §3 procedural-skill intervention and tool-grounded agent protocol | arXiv:2605.20023v1 HTML — §4 offensive-cybersecurity experiments | arXiv:2605.20023v1 HTML — §5 Limitations; negative result is workload/model specific | https://arxiv.org/html/2605.20023v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20023 | complete |
| SF-2026-ARXIV-2605-20051 | RP-6480603c921c3a94 | deep | arXiv:2605.20051v1 | SRC-ARXIV@arXiv:2605.20051v1 | arXiv:2605.20051v1 HTML — §3–§4 reference-driven variant detection | arXiv:2605.20051v1 HTML — §5 AI-infra repository measurement | arXiv:2605.20051v1 HTML — §6 Discussion and false-positive boundary | https://arxiv.org/html/2605.20051v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20051 | complete |
| SF-2026-ARXIV-2605-20061 | RP-0d3da93c05663e30 | deep | arXiv:2605.20061v1 | SRC-ARXIV@arXiv:2605.20061v1 | arXiv:2605.20061v1 HTML — §3 belief-consistency credit assignment | arXiv:2605.20061v1 HTML — §4 long-horizon agent evaluation | arXiv:2605.20061v1 HTML — Appendix C Limitations | https://arxiv.org/html/2605.20061v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20061 | complete |
| SF-2026-ARXIV-2605-20084 | RP-d18ad7b1d473540d | deep | arXiv:2605.20084v1 | SRC-ARXIV@arXiv:2605.20084v1 | arXiv:2605.20084v1 HTML — §3–§4 joint escalation/abstention calibration | arXiv:2605.20084v1 HTML — §5 cascaded-RAG evaluation | arXiv:2605.20084v1 HTML — § unnumbered exact heading ‘Limitations’: distribution shift and calibration | https://arxiv.org/html/2605.20084v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20084 | complete |
| SF-2026-ARXIV-2605-20179 | RP-ac18ffca87654a07 | deep | arXiv:2605.20179v1 | SRC-ARXIV@arXiv:2605.20179v1 | arXiv:2605.20179v1 HTML — §3 I/O-aware MoE expert-offload design | arXiv:2605.20179v1 HTML — §4 LLaDA2.0 experiments | arXiv:2605.20179v1 HTML — §5 Conclusion: block-only activation and limited hardware | https://arxiv.org/html/2605.20179v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-20179 | complete |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | RP-9554d51c20273802 | deep | arXiv:2605.18815v1 | SRC-ARXIV@arXiv:2605.18815v1 | arXiv:2605.18815v1 HTML — §3 DynaTrain elastic parallelism transition controller | arXiv:2605.18815v1 — §4 distributed-training evaluation | arXiv:2605.18815v1 — §5 limitations: topology, transition cost and failure scope | arXiv:2605.18815v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | complete |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | RP-04fc7c27ca53f7fa | deep | arXiv:2605.18854v1 | SRC-ARXIV@arXiv:2605.18854v1 | arXiv:2605.18854v1 HTML — §2 Memory Condensation Strategies | arXiv:2605.18854v1 HTML — §3 Experimental Setup and §4 Results — 480 DiscoveryBench evaluations | arXiv:2605.18854v1 HTML — §5 Discussion / Conclusion — GPT-4o, six-domain and task-length boundary | arXiv:2605.18854v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | complete |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | RP-a0cc23ba143ecd7e | deep | arXiv:2605.18824v1 | SRC-ARXIV@arXiv:2605.18824v1 | arXiv:2605.18824v1 HTML — §3 multi-agent benchmark generation and solution-graph ground-truth pipeline | arXiv:2605.18824v1 — §4 expert review and twelve-model evaluation | arXiv:2605.18824v1 — §6 Conclusion — limitations include multiple-choice scope, frontier-model generator/verifier dependence and nonzero residual error | arXiv:2605.18824v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | complete |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | RP-cbf851c4d19fe35e | deep | arXiv:2605.18814v1 | SRC-ARXIV@arXiv:2605.18814v1 | arXiv:2605.18814v1 HTML — §3 trajectory-data attribution estimator | arXiv:2605.18814v1 — §4 attribution experiments | arXiv:2605.18814v1 — §5 limitations: causal identifiability and data coverage | arXiv:2605.18814v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | complete |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | RP-be39b4b74377b92f | deep | arXiv:2605.18853v1 | SRC-ARXIV@arXiv:2605.18853v1 | arXiv:2605.18853v1 HTML — §Method / System Design — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.18853v1 HTML — §Experiments / Evaluation — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.18853v1 HTML — §Limitations / Discussion — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的适用范围、未证明项与 failure boundary | arXiv:2605.18853v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | complete |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | RP-87243552d8690f7f | deep | arXiv:2605.18825v1 | SRC-ARXIV@arXiv:2605.18825v1 | arXiv:2605.18825v1 HTML — §3 semantic prefix-cache eviction policy | arXiv:2605.18825v1 — §4 serving evaluation | arXiv:2605.18825v1 — §5 limitations: semantic estimator, workload and cache budget | arXiv:2605.18825v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | complete |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | RP-1adc08455070fb87 | deep | arXiv:2605.18812v1 | SRC-ARXIV@arXiv:2605.18812v1 | arXiv:2605.18812v1 HTML — §3 PASC pipeline-conformal evidence contract | arXiv:2605.18812v1 — §4 calibration/evaluation experiments | arXiv:2605.18812v1 — §5 limitations: exchangeability and pipeline shift | arXiv:2605.18812v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | complete |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | RP-e5c082087faf9b76 | deep | arXiv:2605.18852v1 | SRC-ARXIV@arXiv:2605.18852v1 | arXiv:2605.18852v1 HTML — §Method / System Design — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的机制、状态 owner 与控制/数据流 | arXiv:2605.18852v1 HTML — §Experiments / Evaluation — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的作者披露 workload、baseline 与 ablation | arXiv:2605.18852v1 HTML — §Limitations / Discussion — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的适用范围、未证明项与 failure boundary | arXiv:2605.18852v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | complete |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | RP-b75ae65aa7c08ba3 | deep | arXiv:2605.18856v1 | SRC-ARXIV@arXiv:2605.18856v1 | arXiv:2605.18856v1 HTML — §Method / System Design — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的机制、状态 owner 与控制/数据流 | arXiv:2605.18856v1 HTML — §Experiments / Evaluation — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的作者披露 workload、baseline 与 ablation | arXiv:2605.18856v1 HTML — §Limitations / Discussion — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的适用范围、未证明项与 failure boundary | arXiv:2605.18856v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-18755:start -->
#### Operational Memory Architecture for Kubernetes:Preserving Causal Context Across the Evidence Horizon

<!-- claim:SF-2026-ARXIV-2605-18755:start -->
- **Problem:** Kubernetes clusters generate rich operational events during pod lifecycle transitions, yet the platform's native event retention model discards the most diagnostically valuable context.
- **Old path / changed constraint:** Kubernetes 原生 Pod 状态和 Event 在 kubelet 重启轮转后只保留当前快照；当 LastTerminationState 被新一次终止覆盖、对象又被删除时，故障因果链跨过 evidence horizon 后无法由 kubectl 恢复。Metrics、logs 与 traces 各自保留观测，但不自动保存同一对象的时点快照与因果边。
- **Mechanism / ownership:** We propose OMA, a four-layer framework positioning operational memory as an architectural primitive alongside metrics, logs, and traces in the Kubernetes observability stack (Section IV).
- **Evaluation contract:** Experiments on Minikube and AKS include a 30-run latency analysis and stress tests with up to 20 crash-looping pods.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 当前 collector 仅 namespace-scoped；生产化需要 cluster-wide RBAC 或多 namespace 实例，且 ConfigMap watch 涉及敏感配置，论文默认只保存 metadata 与 content hash。SQLite 只适合单集群，跨集群需要分布式存储与查询联邦。30 次统计实验来自 Apple M-series 上的 Minikube，AKS 仅单次；NodeMemoryPressure→OOMKill 边未被观察到，因此不能外推到不同 runtime、硬件、kubelet 配置或大规模生产集群。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.18755v1](https://arxiv.org/abs/2605.18755v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.18755v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-18755:end -->
<!-- review:SF-2026-ARXIV-2605-18755:end -->

<!-- review:SF-2026-ARXIV-2605-18762:start -->
#### ALDEN: Boosting Private Data Extraction from Retrieval-Augmented Generation Systems via Active Learning and Distribution Estimation

<!-- claim:SF-2026-ARXIV-2605-18762:start -->
- **Problem:** Retrieval-Augmented Generation (RAG) is widely used to augment large language models with external knowledge retrieval to improve reliability and generalization.
- **Old path / changed constraint:** However, recent studies have shown that RAG systems remain vulnerable to data extraction attacks, where adversaries can extract private data by embedding malicious commands into user queries.
- **Mechanism / ownership:** Here, we propose ALDEN, a novel attack that effectively and efficiently extracts private data from RAGs.
- **Evaluation contract:** By combining them together, we demonstrate that ALDEN substantially outperforms state-of-the-art methods through comprehensive evaluations.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** To address these limitations, Retrieval-Augmented Generation (RAG) has emerged as a practical solution to improve LLM reliability by incorporating externally retrieved knowledge into the input context Shi et al.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.18762v1](https://arxiv.org/abs/2605.18762v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.18762v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-18762:end -->
<!-- review:SF-2026-ARXIV-2605-18762:end -->

<!-- review:SF-2026-ARXIV-2605-18792:start -->
#### Trust or Abstain? A Self-Aware RAG Approach

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`AGENT-RAG`。
Method / identity：arXiv:2605.18792v1 §2 knowledge-conflict benchmark; §3 self-prior, conditional belief estimation and abstention — parametric and contextual knowledge beliefs govern retrieval and abstention。
Evaluation：arXiv:2605.18792v1 §4 Experiments, selective answering and ablations。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18792v1 No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18792:start -->The exact-v1 body supports the mechanism under §4 Experiments, selective answering and ablations. Counterevidence/scope was checked at No dedicated limitations section; benchmark conflicts, model families and layer probes bound self-awareness claims. It does not prove that “Trust or Abstain? A Self-Aware RAG Approach” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18792:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18792:end -->

<!-- review:SF-2026-ARXIV-2605-18796:start -->
#### UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`INFER-SCHEDULING`。
Method / identity：arXiv:2605.18796v1 §3 formulation; §4 calibrated uncertainty and threshold policy; §5 theory — calibrated correctness and cost jointly select a model cascade。
Evaluation：arXiv:2605.18796v1 §6 Experiments and diagnostics。
Counterevidence / limitations：arXiv:2605.18796v1 §7 Discussion and Limitations。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18796:start -->The exact-v1 body supports the mechanism under §6 Experiments and diagnostics. Counterevidence/scope was checked at §7 Discussion and Limitations. It does not prove that “UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18796:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18796:end -->

<!-- review:SF-2026-ARXIV-2605-18803:start -->
#### PROWL: Prioritized Regret-Driven Optimization for World Model Learning

Review provenance 由本节边界正文与 Completion Receipt 共同绑定；owner=`MULTIMODAL-WORLD-MODELS`。
Method / identity：arXiv:2605.18803v1 §3 PROWL: asymmetric min-max objective, chunked diffusion forcing and adversarial curriculum — adversarial curriculum and prioritized failures change world-model training state。
Evaluation：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Evaluation fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Evaluation, prioritized-failure and ablation sections。
Counterevidence / limitations：Not Disclosed — exact-v1 body was reviewed, but no stable numbered Limitations/Counterevidence fragment was exposed; reviewer boundary: arXiv:2605.18803v1 Limitations discussion; world-model backbone, environments and regret proxy bound generality。
Artifact：Not Disclosed — no immutable public artifact was identified in the reviewed exact-v1 body。

<!-- claim:SF-2026-ARXIV-2605-18803:start -->The exact-v1 body supports the mechanism under Evaluation, prioritized-failure and ablation sections. Counterevidence/scope was checked at Limitations discussion; world-model backbone, environments and regret proxy bound generality. It does not prove that “PROWL: Prioritized Regret-Driven Optimization for World Model Learning” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.<!-- claim:SF-2026-ARXIV-2605-18803:end -->

Disposition=`No Change — Existing Coverage`；该结论来自独立 exact-v1 与 current owner+adjacent comparison，不由 validator 代签。
<!-- review:SF-2026-ARXIV-2605-18803:end -->

<!-- review:SF-2026-ARXIV-2605-18859:start -->
#### TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing

问题与演进：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls.`。

Evaluation：`https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-18859:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-18859:end -->
<!-- review:SF-2026-ARXIV-2605-18859:end -->

<!-- review:SF-2026-ARXIV-2605-18891:start -->
#### Auditing Reasoning-Trace Memorization Claims after Unlearning with Head-Conditioned Canaries

问题与 changed constraint：reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。

机制与 ownership：Evaluations of unlearning on reasoning models sometimes show a bypass pattern. owner=`TRAIN-DATA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.18891v1 — §3 Setup and the Bypass Metric (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.18891v1 — §4 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.18891v1 — §5 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-18891:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-18891:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-18891:end -->

<!-- review:SF-2026-ARXIV-2605-18899:start -->
#### Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target

问题与 changed constraint：continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision

机制与 ownership：We propose an Anchored Bandit Policy Optimization (ABPO) framework for continual LLM-Rec updates that combines group-relative policy optimization (GRPO) with explicit treatment of exposure bias and feedback ambiguity. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.18899v1 — §3 Anchored Bandit Policy Optimization (official exact-v1 HTML)`；Evaluation=`arXiv:2605.18899v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.18899v1 — Appendix E.4 Scope limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-18899:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-18899:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-18899:end -->

<!-- review:SF-2026-ARXIV-2605-18918:start -->
#### ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense

**问题与机制。** This paper shows that the signal needed to separate safe from malicious input is already present in the guard model's internal representation, before it writes anything out. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 ESLD latent sensor architecture and external enforcement path`；Evaluation=`§4 Experiments against prompt injection`；Limitations/Counterevidence=`§5 Limitations; learned detector is not an authority`。

<!-- claim:SF-2026-ARXIV-2605-18918:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18918:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18918:end -->

<!-- review:SF-2026-ARXIV-2605-18930:start -->
#### OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences

**问题与机制。** Memory-augmented large language model (LLM) agents use iterative reflection and self-evolution to solve complex tasks, but these mechanisms introduce security risks. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 threat model; §4.1–4.2 poisoning`；Evaluation=`§5 mechanistic analysis; §6 evaluation`；Limitations/Counterevidence=`§7 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18930:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18930:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18930:end -->

<!-- review:SF-2026-ARXIV-2605-18991:start -->
#### Agent Security is a Systems Problem

**问题与机制。** We also identify the research challenges that stand in the way of implementing these principles in agents. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 system-level invariants, model-as-untrusted-component and attack analysis`；Evaluation=`§3 open systems-security problems; no empirical mechanism evaluation`；Limitations/Counterevidence=`§4 objections and position-paper boundary`。

<!-- claim:SF-2026-ARXIV-2605-18991:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18991:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18991:end -->

<!-- review:SF-2026-ARXIV-2605-19008:start -->
#### Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency

**问题与机制。** Modern language-model training is increasingly exposed to instability, degraded runs, and wasted compute, especially under aggressive learning-rate, scale, and runtime-stress conditions. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 LBW-Guard bounded training-control layer, actions and safety envelope`；Evaluation=`§4–§5 setup, stress runs and controller outcomes`；Limitations/Counterevidence=`§6 Limitations; simulator/recipe and stability boundary`。

<!-- claim:SF-2026-ARXIV-2605-19008:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19008:end -->

**Books Comparison。** 当前 pretraining 章有 optimizer/clip/rollback，尚缺 optimizer 之上的 bounded autonomous control envelope、action budget 与 human override；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19008:end -->

<!-- review:SF-2026-ARXIV-2605-19049:start -->
#### KVBuffer: IO-aware Serving for Linear Attention

**问题与机制。** In this paper, we propose KVBuffer, an IO-aware serving mechanism for linear attention. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–§3.4 KVBuffer IO-aware state placement and update pipeline`；Evaluation=`§4 Evaluation on linear-attention serving`；Limitations/Counterevidence=`§6 Discussion/limitations; linear-attention state only`。

<!-- claim:SF-2026-ARXIV-2605-19049:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19049:end -->

**Books Comparison。** 当前 KV 章以 Transformer KV 为主，没有明确 linear-attention recurrent state 的 IO-aware buffering/placement owner；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19049:end -->

<!-- review:SF-2026-ARXIV-2605-19099:start -->
#### DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows

**问题与机制。** We introduce DecisionBench, a benchmark substrate for emergent delegation in long-horizon agentic workflows. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 DecisionBench delegation substrate, interface and metrics`；Evaluation=`§4 Experiments across peer pools and tasks`；Limitations/Counterevidence=`§5 Limitations; benchmark delegation is not production authority`。

<!-- claim:SF-2026-ARXIV-2605-19099:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19099:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19099:end -->

<!-- review:SF-2026-ARXIV-2605-19101:start -->
#### Heterogeneity-Aware Dataset Scheduling for Efficient Audio Large Language Model Training

**问题与机制。** In this work, we analyze multi-dataset AudioQA training from a convergence perspective and propose Grouped Sequential Training (GST). 该 family 改变或挑战 `TRAIN-DATA` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 GST heterogeneity state, scheduler and optimization rule`；Evaluation=`§5 Experiments on Audio LLM training`；Limitations/Counterevidence=`§6 Limitations; audio datasets and selected recipes`。

<!-- claim:SF-2026-ARXIV-2605-19101:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19101:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19101:end -->

<!-- review:SF-2026-ARXIV-2605-19127:start -->
#### POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents

**问题与机制。** We introduce POLAR-Bench (Policy-aware adversarial Benchmark), in which a trusted model with a privacy policy and a task converses with a third-party model that adversarially probes for both task-relevant and protected attributes. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.6 policy/attack/evaluation contract`；Evaluation=`§4–§5 diagnostic surface`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19127:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19127:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19127:end -->

<!-- review:SF-2026-ARXIV-2605-19140:start -->
#### Learning to Hand Off: Provably Convergent Workflow Learning under Interface Constraints

**问题与机制。** We study workflow learning in a setting where specialized agents hand off control through a shared artifact, each agent observes only a local function of that artifact and its own private state, and no centralized learner accesses joint trajectories -- the operating regime of multi-agent LLM pipelines that span organizational, vendor, or trust boundaries. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 local-observation handoff interface and convergent learning rule`；Evaluation=`§5 theoretical/empirical evaluation`；Limitations/Counterevidence=`§6 Limitations; assumptions do not prove open-system delivery or authority`。

<!-- claim:SF-2026-ARXIV-2605-19140:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19140:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19140:end -->

<!-- review:SF-2026-ARXIV-2605-19151:start -->
#### Progressive Autonomy as Preference Learning: A Formalization of Trust Calibration for Agentic Tool Use

**问题与机制。** We formalize trust calibration for agentic tool use (deciding when an automated agent's proposed action may execute autonomously versus require human approval) as a preference-learning problem. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2–§3 approval/deny observations, GP preference posterior and autonomy threshold`；Evaluation=`§3–§4 theoretical and simulated evaluation`；Limitations/Counterevidence=`§4 Limitations; preference stationarity and calibration boundary`。

<!-- claim:SF-2026-ARXIV-2605-19151:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19151:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19151:end -->

<!-- review:SF-2026-ARXIV-2605-19169:start -->
#### Modeling the Impact of Fiber Latency on Compute-Communication Overlap in Geo-Distributed Multi-Datacenter AI Training

**问题与机制。** We use discrete-event simulation to quantify the impact of fiber latency on the efficacy of geo-distributed AI model training with data parallelism. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 Methods; latency/serialization model and ASTRA-sim overlap model`；Evaluation=`§3 Results; GPT-3 13B/175B, A100/H100, 256–8192 GPU simulation`；Limitations/Counterevidence=`§4 Conclusions; lumped two-DC, uncongested-network and simulation-only boundary`。

<!-- claim:SF-2026-ARXIV-2605-19169:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19169:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19169:end -->

<!-- review:SF-2026-ARXIV-2605-19192:start -->
#### Hallucination as Exploit: Evidence-Carrying Multimodal Agents

**问题与机制。** We formalize this failure mode as hallucination-to-action conversion: an unsupported claim supplies the precondition for a privileged action. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 evidence certificate and action-admission architecture`；Evaluation=`§5 Evaluation under multimodal hallucination-to-action attacks`；Limitations/Counterevidence=`§6 Limitations; certificate coverage and evaluator trust`。

<!-- claim:SF-2026-ARXIV-2605-19192:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19192:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19192:end -->

<!-- review:SF-2026-ARXIV-2605-19193:start -->
#### Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection

**问题与机制。** We evaluate two tracks: (i) a Monte-Carlo study under calibrated Beta models characterising working curves, error rates, capping behaviour, and sensitivity; and (ii) a real-LLM evaluation on 200 attempted MMLU and 200 attempted GSM8K items with three heterogeneous agents (gpt-5, claude-opus-4-6, gemini-2.5-pro) and a claude-opus-4-6 judge, using disjoint 40-item calibration subsets. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§III–V sequential stopping and calibration`；Evaluation=`§VI simulation; §VII real-LLM study`；Limitations/Counterevidence=`§V-E i.i.d. violations; §VIII discussion`。

<!-- claim:SF-2026-ARXIV-2605-19193:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19193:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19193:end -->

<!-- review:SF-2026-ARXIV-2605-19196:start -->
#### Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?

**问题与机制。** To address these gaps, we introduce REFLECT (REliable Fine-grained LLM judge Evaluation via Controlled inTervention), a meta-evaluation benchmark targeting fine-grained failure detection in agentic environments. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2.1–2.2 controlled-intervention benchmark`；Evaluation=`§3.1–3.5 judge meta-evaluation`；Limitations/Counterevidence=`§4 related work; §5 conclusion`。

<!-- claim:SF-2026-ARXIV-2605-19196:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19196:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19196:end -->

<!-- review:SF-2026-ARXIV-2605-19218:start -->
#### Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference

**问题与机制。** Experiments on two representative VLM backbones show that RotateK consistently outperforms prior Key channel pruning in both accuracy and decoding latency, while joint token-channel pruning improves over token-only baselines at matched KV cache budgets. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–§3.3 RotateK query-weighted PCA, structured channel pruning and Triton kernel`；Evaluation=`§4 Experiments; matched KV budgets, prefill/decode latency and memory`；Limitations/Counterevidence=`Appendix G Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19218:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-19218:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19218:end -->

<!-- review:SF-2026-ARXIV-2605-19228:start -->
#### Diagnosing Multi-step Reasoning Failures in Black-box LLMs via Stepwise Confidence Attribution

**问题与机制。** In this paper, we introduce Stepwise Confidence Attribution (SCA), a framework for closed-source LLMs that assigns step-level confidence based only on generated reasoning traces. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 problem; §4.1–4.3 step confidence`；Evaluation=`§5 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-19228:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-19228:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-19228:end -->

<!-- review:SF-2026-ARXIV-2605-19240:start -->
#### CASPIAN: Online Detection and Attribution of Cascade Attacks in LLM Multi-Agent Systems via Cross-Channel Causal Monitoring

**问题与机制。** Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4.1–4.4 causal cross-channel monitoring`；Evaluation=`§5 detection and attribution evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19240:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19240:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19240:end -->

<!-- review:SF-2026-ARXIV-2605-19242:start -->
#### PhyWorld: Physics-Faithful World Model for Video Generation

**问题与机制。** We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 physics-faithful data and objective`；Evaluation=`§4 controlled video/world-model evaluation`；Limitations/Counterevidence=`§5 Conclusion and inherited generator biases`。

<!-- claim:SF-2026-ARXIV-2605-19242:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19242:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19242:end -->

<!-- review:SF-2026-ARXIV-2605-19262:start -->
#### Backdooring Masked Diffusion Language Models

**问题与机制。** In this work, we present the first systematic study of training-time backdoor attacks on MDLMs. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 masked-diffusion backdoor construction`；Evaluation=`§5 attack and defense experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19262:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19262:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19262:end -->

<!-- review:SF-2026-ARXIV-2605-19269:start -->
#### CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

**问题与机制。** We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 GEMM-epilogue program representation`；Evaluation=`§4 kernel and end-to-end evaluation`；Limitations/Counterevidence=`§5 limitations and portability boundary`。

<!-- claim:SF-2026-ARXIV-2605-19269:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19269:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19269:end -->

<!-- review:SF-2026-ARXIV-2605-19276:start -->
#### OpenCompass: A Universal Evaluation Platform for Large Language Models

**问题与机制。** Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.5 evaluation-platform architecture`；Evaluation=`§4 benchmark execution and comparison`；Limitations/Counterevidence=`§5 Future Works`。

<!-- claim:SF-2026-ARXIV-2605-19276:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19276:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19276:end -->

<!-- review:SF-2026-ARXIV-2605-19282:start -->
#### Rethinking Muon Beyond Pretraining: Spectral Failures and High-Pass Remedies for VLA and RLVR

**问题与机制。** While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 spectral failure analysis; §4 high-pass remedy`；Evaluation=`§5 VLA/RLVR optimization experiments`；Limitations/Counterevidence=`Appendix M Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19282:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19282:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19282:end -->

<!-- review:SF-2026-ARXIV-2605-19314:start -->
#### ContextFlow: Hierarchical Task-State Alignment for Long-Horizon Embodied Agents

**问题与机制。** We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision. 系统 owner=`AGENT-WORKFLOW`。

**Exact-v1。** Method=`§3 hierarchical task-state alignment`；Evaluation=`§4.1–4.4 long-horizon embodied evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19314:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19314:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19314:end -->

<!-- review:SF-2026-ARXIV-2605-19319:start -->
#### SWEET: Sparse World Modeling with Image Editing for Embodied Task Execution

**问题与机制。** In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3 sparse keyframe world-model planner and goal-conditioned action predictor`；Evaluation=`§4 real-robot and simulation experiments`；Limitations/Counterevidence=`§5 Limitations: short horizon, annotations and edited-image domain gap`。

<!-- claim:SF-2026-ARXIV-2605-19319:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19319:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19319:end -->

<!-- review:SF-2026-ARXIV-2605-19321:start -->
#### Exploring and Developing a Pre-Model Safeguard with Draft Models

**问题与机制。** In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 draft-model pre-guard design`；Evaluation=`§6 jailbreak and latency evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19321:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19321:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19321:end -->

<!-- review:SF-2026-ARXIV-2605-19328:start -->
#### RoboJailBench: Benchmarking Adversarial Attacks and Defenses in Embodied Robotic Agents

**问题与机制。** We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 embodied-agent threat and benchmark protocol`；Evaluation=`§4 attacks and defenses`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19328:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19328:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19328:end -->

<!-- review:SF-2026-ARXIV-2605-19335:start -->
#### Leveraging I/O Stalls for Efficient Scheduling in ANNS

**问题与机制。** We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§4 LIOS update decomposition, overrun-bounded budgeting and feedback control`；Evaluation=`§6 search/update evaluation on FreshDiskANN and OdinANN`；Limitations/Counterevidence=`§8 Conclusion; disk ANNS and measured hardware scope`。

<!-- claim:SF-2026-ARXIV-2605-19335:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19335:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19335:end -->

<!-- review:SF-2026-ARXIV-2605-19341:start -->
#### HalluWorld: A Controlled Benchmark for Hallucination via Reference World Models

**问题与机制。** To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3.1–3.3 controlled reference-world benchmark`；Evaluation=`§4 cross-context hallucination experiments`；Limitations/Counterevidence=`§5 Discussion; controlled-world boundary`。

<!-- claim:SF-2026-ARXIV-2605-19341:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19341:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19341:end -->

<!-- review:SF-2026-ARXIV-2605-19373:start -->
#### Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies

问题与机制：Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。

Evaluation contract：The reference implementation is available as crdt-merge v0.9.4.

Evidence locators：Method=`section 4 The Solution: Two-Layer Architecture (§4 The Solution: Two-Layer Architecture)`；Evaluation=`section 3.1 Formal Analysis of CRDT Property Violations (§3.1 Formal Analysis of CRDT Property Violations)`；Counterevidence=`section 7 Discussion (§7 Discussion)`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-19373:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-19373:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-19373:end -->

<!-- review:SF-2026-ARXIV-2605-19407:start -->
#### A Bitter Lesson for Data Filtering

**问题与机制。** We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime. 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§3–§6 compute/data/filter scaling design`；Evaluation=`§6–§7 scaling experiments`；Limitations/Counterevidence=`§8 Discussion and scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-19407:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19407:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19407:end -->

<!-- review:SF-2026-ARXIV-2605-19444:start -->
#### Detecting and Mitigating the Correct-Answer Extinction Window in Test-Time Reinforcement Learning with Majority Voting

**问题与机制。** We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§2 extinction-window dynamics; §3 TTRL-Guard`；Evaluation=`§4 model/benchmark experiments and per-problem migration`；Limitations/Counterevidence=`§6 Breadth of evaluation; signal quality at the extremes`。

<!-- claim:SF-2026-ARXIV-2605-19444:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19444:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19444:end -->

<!-- review:SF-2026-ARXIV-2605-19447:start -->
#### What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents

**问题与机制。** We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 selective hindsight placement and environment-guided advantage reweighting`；Evaluation=`§4 ALFWorld/WebShop experiments and ablations`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19447:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19447:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19447:end -->

<!-- review:SF-2026-ARXIV-2605-19461:start -->
#### Beyond Mode Collapse: Distribution Matching for Diverse Reasoning

**问题与机制。** We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 forward/group distribution-matching policy optimization`；Evaluation=`§4–§5 reasoning experiments and ablations`；Limitations/Counterevidence=`Appendix B Limitations; group-local coverage does not prove global target matching`。

<!-- claim:SF-2026-ARXIV-2605-19461:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19461:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19461:end -->

<!-- review:SF-2026-ARXIV-2605-19478:start -->
#### Exposing Functional Fusion: A New Class of Strategic Backdoor in Dynamic Prompt Architectures

**问题与机制。** While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§4 threat model; §5–§6 dynamic-prompt functional fusion`；Evaluation=`§7 attack, pruning and transfer evaluation`；Limitations/Counterevidence=`§8 Conclusion; ViT/VPT threat-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-19478:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19478:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19478:end -->

<!-- review:SF-2026-ARXIV-2605-19481:start -->
#### C2CServe: Leveraging NVLink-C2C for Elastic Serverless LLM Serving on MIG

**问题与机制。** Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM. 系统 owner=`INFER-PD-DISAGGREGATION`。

**Exact-v1。** Method=`§III–V C2C weight/state movement design`；Evaluation=`§VI MIG/serverless serving evaluation`；Limitations/Counterevidence=`§VII Conclusion and hardware boundary`。

<!-- claim:SF-2026-ARXIV-2605-19481:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19481:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19481:end -->

<!-- review:SF-2026-ARXIV-2605-19537:start -->
#### The Silent Hyperparameter: Quantifying the Impact of Inference Backends on LLM Reproducibility

**问题与机制。** While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 backend-reproducibility protocol`；Evaluation=`§4 backend/model benchmark deltas`；Limitations/Counterevidence=`§5 Discussion and reproducibility boundary`。

<!-- claim:SF-2026-ARXIV-2605-19537:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19537:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19537:end -->

<!-- review:SF-2026-ARXIV-2605-19576:start -->
#### Library Drift: Diagnosing and Fixing a Silent Failure Mode in Self-Evolving LLM Skill Libraries

**问题与机制。** Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3–§5 lifecycle-managed skill library`；Evaluation=`§6 library-drift evaluation`；Limitations/Counterevidence=`§7 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19576:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19576:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19576:end -->

<!-- review:SF-2026-ARXIV-2605-19593:start -->
#### Towards Multi-Model LLM Schedulers: Empirical Insights into Offloading and Preemption

**问题与机制。** In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 multi-model offload/preemption methodology`；Evaluation=`§4–§5 heterogeneous-serving measurements`；Limitations/Counterevidence=`§6 Conclusion; interconnect and hardware constraints`。

<!-- claim:SF-2026-ARXIV-2605-19593:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19593:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19593:end -->

<!-- review:SF-2026-ARXIV-2605-19604:start -->
#### Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents

**问题与机制。** We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 programmable runtime skill contract`；Evaluation=`§4 execution and accuracy evaluation`；Limitations/Counterevidence=`§5 Conclusion; language/runtime boundary`。

<!-- claim:SF-2026-ARXIV-2605-19604:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19604:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19604:end -->

<!-- review:SF-2026-ARXIV-2605-19722:start -->
#### Measuring Safety Alignment Effects in Autonomous Security Agents

**问题与机制。** We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 trace-based autonomous security-agent protocol`；Evaluation=`§4–§5 sandbox/tool-use evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19722:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19722:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19722:end -->

<!-- review:SF-2026-ARXIV-2605-19755:start -->
#### Operationalising Artificial Intelligence Bills of Materials (AIBOMs) for Verifiable AI Provenance and Lifecycle Assurance

<!-- claim:SF-2026-ARXIV-2605-19755:start -->
- **Problem:** Artificial Intelligence (AI) systems are increasingly dependent on complex, multi-layered software supply chains that introduce challenges for reproducibility, transparency, and security assurance.
- **Old path / changed constraint:** 传统 SBOM 以静态组件名和版本为主，无法完整绑定模型、数据引用、运行时依赖、配置与生成过程；在 AI artifact 持续演化和环境漂移时，仅凭名称清单不足以重放、归责或判断漏洞匹配。
- **Mechanism / ownership:** 方案扩展 CycloneDX，记录 AI provenance、model lineage、disclosure metadata，并用组件 hash、签名、容器运行态和 agent 生成的环境记录绑定 artifact；自动化流水线负责环境发现、漏洞富化、schema 校验和 reproducibility audit，材料不全时保留 partial-attestation 状态。
- **Evaluation contract:** 作者在受控 containerised analytic workflows 中报告 98.7% reproducibility fidelity、96.2% vulnerability-match precision 和 63% manual-oversight reduction。这些是作者在论文 workload 下的结果；尚无跨组织、长期生产采用或不同 vulnerability database 的独立验证。
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** 完整性依赖 runtime discovery、包名归一化、base-image 可见性和漏洞数据库覆盖；hash 改善身份绑定，却不能证明语义等价或实际可利用性。非确定性执行仍可能阻止 bit-identical replay，持续采集、签名和富化也增加存储与治理成本；无法解析的瞬态依赖必须保持 unverifiable，而非伪造完整性。
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.19755v1](https://arxiv.org/abs/2605.19755v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.19755v1.pdf`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-19755:end -->
<!-- review:SF-2026-ARXIV-2605-19755:end -->

<!-- review:SF-2026-ARXIV-2605-19769:start -->
#### OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**问题与机制。** We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 verifier-grounded software worlds`；Evaluation=`§4.1 computer-use agent evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations and Future Work’`。

<!-- claim:SF-2026-ARXIV-2605-19769:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19769:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19769:end -->

<!-- review:SF-2026-ARXIV-2605-19775:start -->
#### Understanding Inference Scaling for LLMs: Bottlenecks, Trade-offs, and Performance Principles

**问题与机制。** By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2–§3 inference-scaling model`；Evaluation=`§4–§5 reasoning-workload measurements`；Limitations/Counterevidence=`§6 Conclusions and disclosed scope`。

<!-- claim:SF-2026-ARXIV-2605-19775:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19775:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19775:end -->

<!-- review:SF-2026-ARXIV-2605-19779:start -->
#### Distribution-Free Uncertainty Quantification for Continuous AI Agent Evaluation

**问题与机制。** We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§2–§3 conformal continuous-agent UQ`；Evaluation=`§4 longitudinal agent studies`；Limitations/Counterevidence=`§5 Limitations: bounded shift and dependence`。

<!-- claim:SF-2026-ARXIV-2605-19779:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19779:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19779:end -->

<!-- review:SF-2026-ARXIV-2605-19811:start -->
#### LionMuon: Alternating Spectral and Sign Descent for Efficient Training

**问题与机制。** In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods. 系统 owner=`TRAIN-PRETRAINING`。

**Exact-v1。** Method=`§3 optimizer geometry; §4 LionMuon alternating spectral/sign descent`；Evaluation=`§5 language-model training experiments and ablations`；Limitations/Counterevidence=`§6 Limitations and optimizer/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-19811:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19811:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19811:end -->

<!-- review:SF-2026-ARXIV-2605-19847:start -->
#### Auditing Privacy in Multi-Tenant RAG under Account Collusion

**问题与机制。** We show that this framing understates leakage under same-index account collusion. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§2–§3 collusion threat model and tenant accounting`；Evaluation=`§4 privacy audit; §5 protocol`；Limitations/Counterevidence=`§7.1 Limitations: retrieval only, not generation`。

<!-- claim:SF-2026-ARXIV-2605-19847:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19847:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19847:end -->

<!-- review:SF-2026-ARXIV-2605-19893:start -->
#### SSV: Sparse Speculative Verification for Efficient LLM Inference

**问题与机制。** We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 sparse speculative verification`；Evaluation=`§5 long-context evaluation`；Limitations/Counterevidence=`§6 Conclusion and sparse-attention boundary`。

<!-- claim:SF-2026-ARXIV-2605-19893:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19893:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19893:end -->

<!-- review:SF-2026-ARXIV-2605-19932:start -->
#### PEEK: Context Map as an Orientation Cache for Long-Context LLM Agents

**问题与机制。** We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1。** Method=`§3 orientation-cache representation`；Evaluation=`§4 recurring-context agent evaluation`；Limitations/Counterevidence=`§5 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19932:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19932:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19932:end -->

<!-- review:SF-2026-ARXIV-2605-19945:start -->
#### GEM: GPU-Variability-Aware Expert to GPU Mapping for MoE Systems

**问题与机制。** We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3–§4 variability-aware expert placement`；Evaluation=`§5 heterogeneous-GPU evaluation`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19945:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19945:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19945:end -->

<!-- review:SF-2026-ARXIV-2605-19952:start -->
#### Rethinking How to Remember: Beyond Atomic Facts in Lifelong LLM Agent Memory

**问题与机制。** To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning. 系统 owner=`AGENT-MEMORY`。

**Exact-v1。** Method=`§3 trace/chunk memory representation`；Evaluation=`§4 lifelong-memory evaluation`；Limitations/Counterevidence=`Appendix C.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-19952:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19952:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19952:end -->

<!-- review:SF-2026-ARXIV-2605-19999:start -->
#### LLM Benchmark Datasets Should Be Contamination-Resistant

**问题与机制。** Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3–§4 contamination-resistant benchmark construction`；Evaluation=`§5 benchmark analysis`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: contamination detection and task scope`。

<!-- claim:SF-2026-ARXIV-2605-19999:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-19999:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-19999:end -->

<!-- review:SF-2026-ARXIV-2605-20005:start -->
#### Fine-Tuning Without Forgetting via Loss-Adaptive Learning Rates

**问题与机制。** We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss. 系统 owner=`TRAIN-SFT`。

**Exact-v1。** Method=`§3 per-step forgetting bound and loss-adaptive learning rate`；Evaluation=`§4–§5 task/forgetting, factuality and calibration experiments`；Limitations/Counterevidence=`§6 Conclusion, Limitations, and Future Work`。

<!-- claim:SF-2026-ARXIV-2605-20005:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20005:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20005:end -->

<!-- review:SF-2026-ARXIV-2605-20022:start -->
#### FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration

**问题与机制。** Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel. 系统 owner=`INFER-SPECULATIVE-DECODING`。

**Exact-v1。** Method=`§3–§4 asynchronous flexible drafting`；Evaluation=`§5 end-to-end evaluation`；Limitations/Counterevidence=`§6 Conclusion: bonus-token and accepted-length uncertainty`。

<!-- claim:SF-2026-ARXIV-2605-20022:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20022:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20022:end -->

<!-- review:SF-2026-ARXIV-2605-20023:start -->
#### When Skills Don't Help: A Negative Result on Procedural Knowledge for Tool-Grounded Agents in Offensive Cybersecurity

**问题与机制。** Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 procedural-skill intervention and tool-grounded agent protocol`；Evaluation=`§4 offensive-cybersecurity experiments`；Limitations/Counterevidence=`§5 Limitations; negative result is workload/model specific`。

<!-- claim:SF-2026-ARXIV-2605-20023:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20023:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20023:end -->

<!-- review:SF-2026-ARXIV-2605-20051:start -->
#### Hunting Vulnerability Variants in AI Infra: Measurement and Reference-Driven Detection

**问题与机制。** Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3–§4 reference-driven variant detection`；Evaluation=`§5 AI-infra repository measurement`；Limitations/Counterevidence=`§6 Discussion and false-positive boundary`。

<!-- claim:SF-2026-ARXIV-2605-20051:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20051:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20051:end -->

<!-- review:SF-2026-ARXIV-2605-20061:start -->
#### Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents

**问题与机制。** To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning. 系统 owner=`TRAIN-RLHF`。

**Exact-v1。** Method=`§3 belief-consistency credit assignment`；Evaluation=`§4 long-horizon agent evaluation`；Limitations/Counterevidence=`Appendix C Limitations`。

<!-- claim:SF-2026-ARXIV-2605-20061:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20061:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20061:end -->

<!-- review:SF-2026-ARXIV-2605-20084:start -->
#### BalanceRAG: Joint Risk Calibration for Cascaded Retrieval-Augmented Generation

**问题与机制。** In this work, we develop BalanceRAG to certify threshold pairs at a target risk level. 系统 owner=`AGENT-RAG`。

**Exact-v1。** Method=`§3–§4 joint escalation/abstention calibration`；Evaluation=`§5 cascaded-RAG evaluation`；Limitations/Counterevidence=`§ unnumbered exact heading ‘Limitations’: distribution shift and calibration`。

<!-- claim:SF-2026-ARXIV-2605-20084:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20084:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20084:end -->

<!-- review:SF-2026-ARXIV-2605-20179:start -->
#### TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload

**问题与机制。** In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§3 I/O-aware MoE expert-offload design`；Evaluation=`§4 LLaDA2.0 experiments`；Limitations/Counterevidence=`§5 Conclusion: block-only activation and limited hardware`。

<!-- claim:SF-2026-ARXIV-2605-20179:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-20179:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-20179:end -->

<!-- review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->
#### DynaTrain: Fast Online Parallelism Switching for Elastic LLM Training

问题与机制：We present DynaTrain, a distributed training system for sub-second, online reconfiguration across arbitrary multi-dimensional parallelism.。机制 owner=`TRAIN-DISTRIBUTED-TRAINING`。
全文定位：`arXiv:2605.18815v1 HTML — §3 DynaTrain elastic parallelism transition controller`；evaluation=`arXiv:2605.18815v1 — §4 distributed-training evaluation`；limitations/counterevidence=`arXiv:2605.18815v1 — §5 limitations: topology, transition cost and failure scope`。
<!-- claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->
#### Evaluating Memory Condensation Strategies for Coding Agents in Data-Driven Scientific Discovery

问题与机制：Coding agents accumulate extensive context during long-running tasks, yet fixed context windows force practitioners to choose between truncation and task failure.。机制 owner=`AGENT-MEMORY`。
全文定位：`arXiv:2605.18854v1 HTML — §2 Memory Condensation Strategies`；evaluation=`§3 Experimental Setup and §4 Results — 480 DiscoveryBench evaluations`；limitations/counterevidence=`§5 Discussion / Conclusion — GPT-4o, six-domain and task-length boundary`。
<!-- claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->
#### Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models

问题与机制：We introduce a framework for automated benchmark generation.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18824v1 HTML — §3 multi-agent benchmark generation and solution-graph ground-truth pipeline`；evaluation=`arXiv:2605.18824v1 — §4 expert review and twelve-model evaluation`；limitations/counterevidence=`arXiv:2605.18824v1 — §6 Conclusion — limitations include multiple-choice scope, frontier-model generator/verifier dependence and nonzero residual error`。
<!-- claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->
#### How Faithful Is Trajectory-Based Data Attribution? Error Sources, Remedies, and Practical Guidelines

问题与机制：We propose AdamW-influence to fully account for AdamW's optimization dynamics, yielding improvements from 10% to over 300% in Spearman correlation between estimated and ground-truth influence across four settings spanning MLP, CNN, GPT-2, and Llama 3.2-1B.。机制 owner=`TRAIN-DATA`。
全文定位：`arXiv:2605.18814v1 HTML — §3 trajectory-data attribution estimator`；evaluation=`arXiv:2605.18814v1 — §4 attribution experiments`；limitations/counterevidence=`arXiv:2605.18814v1 — §5 limitations: causal identifiability and data coverage`。
<!-- claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->
#### INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference

问题与机制：We present INAR-VL, a lightweight edge-cloud routing system for multimodal inference in a two-tier deployment.。机制 owner=`INFER-SCHEDULING`。
全文定位：`arXiv:2605.18853v1 HTML — §Method / System Design — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — INAR-VL: Input-Aware Routing for Edge-Cloud Vision-Language Inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->
#### Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches

问题与机制：We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.18825v1 HTML — §3 semantic prefix-cache eviction policy`；evaluation=`arXiv:2605.18825v1 — §4 serving evaluation`；limitations/counterevidence=`arXiv:2605.18825v1 — §5 limitations: semantic estimator, workload and cache budget`。
<!-- claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->
#### PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines

问题与机制：We present PASC (Pipeline-Aware Split Conformal), which reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18812v1 HTML — §3 PASC pipeline-conformal evidence contract`；evaluation=`arXiv:2605.18812v1 — §4 calibration/evaluation experiments`；limitations/counterevidence=`arXiv:2605.18812v1 — §5 limitations: exchangeability and pipeline shift`。
<!-- claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->
#### Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking

问题与机制：We formulate late-stage checkpoint selection as a stability-aware decision problem under evaluation uncertainty and propose a progressive framework combining pointwise filtering, listwise ranking, and pairwise refinement.。机制 owner=`PLATFORM-EVALUATION-SYSTEM`。
全文定位：`arXiv:2605.18852v1 HTML — §Method / System Design — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Robust Checkpoint Selection for Multimodal LLMs via Agentic Evaluation and Stability-Aware Ranking 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->
#### SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference

问题与机制：We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding.。机制 owner=`INFER-KV-CACHE`。
全文定位：`arXiv:2605.18856v1 HTML — §Method / System Design — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | exact-v1 evaluation for Operational Memory Architecture for Kubernetes:Preserving Causal Context Across the Evidence Horizon | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-18762 | exact-v1 evaluation for ALDEN: Boosting Private Data Extraction from Retrieval-Augmented Generation Systems via Active Learning and Distribution Estimation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-2026-ARXIV-2605-19755 | exact-v1 evaluation for Operationalising Artificial Intelligence Bills of Materials (AIBOMs) for Verifiable AI Provenance and Lifecycle Assurance | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18755 |
| SF-2026-ARXIV-2605-18762 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18762 |
| SF-2026-ARXIV-2605-18792 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18792 |
| SF-2026-ARXIV-2605-18796 | score_7_9 | selected | DA-20260520-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-01 |
| SF-2026-ARXIV-2605-18803 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18803 |
| SF-2026-ARXIV-2605-18859 | score_7_9;forced_review;potential_books_delta | selected | DA-20260520-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-02 |
| SF-2026-ARXIV-2605-18891 | score_7_9;forced_review;potential_books_delta | selected | DA-20260520-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260520-03 |
| SF-2026-ARXIV-2605-18899 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2605-18918 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18918 |
| SF-2026-ARXIV-2605-18930 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18930 |
| SF-2026-ARXIV-2605-18991 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-18991 |
| SF-2026-ARXIV-2605-19008 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19008 |
| SF-2026-ARXIV-2605-19049 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19049 |
| SF-2026-ARXIV-2605-19099 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19099 |
| SF-2026-ARXIV-2605-19101 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19101 |
| SF-2026-ARXIV-2605-19127 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19127 |
| SF-2026-ARXIV-2605-19140 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19140 |
| SF-2026-ARXIV-2605-19151 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19151 |
| SF-2026-ARXIV-2605-19169 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19169 |
| SF-2026-ARXIV-2605-19192 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19192 |
| SF-2026-ARXIV-2605-19193 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19193 |
| SF-2026-ARXIV-2605-19196 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19196 |
| SF-2026-ARXIV-2605-19218 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19218 |
| SF-2026-ARXIV-2605-19228 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19228 |
| SF-2026-ARXIV-2605-19240 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19373 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-19407 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19444 |
| SF-2026-ARXIV-2605-19447 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19755 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19755 |
| SF-2026-ARXIV-2605-19769 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19847 |
| SF-2026-ARXIV-2605-19893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20005 |
| SF-2026-ARXIV-2605-20022 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-20179 |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF |

<!-- analysis-decision:SF-2026-ARXIV-2605-18755:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18762:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18762:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18792:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18792:end -->

<!-- analysis:DA-20260520-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18796

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18803:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18803:end -->

<!-- analysis:DA-20260520-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18859

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-02:end -->

<!-- analysis:DA-20260520-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-18891

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260520-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18899:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18918:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18930:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18930:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-18991:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-18991:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19008:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19008:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19049:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19049:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19099:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19099:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19101:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19101:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19127:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19127:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19140:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19140:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19151:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19169:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19169:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19192:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19192:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19193:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19193:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19196:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19196:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19218:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19218:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19228:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19228:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19240:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19240:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19242:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19262:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19269:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19269:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19276:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19276:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19282:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19314:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19314:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19319:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19319:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19321:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19321:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19328:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19328:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19335:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19335:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19341:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19341:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19373:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19373:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19407:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19407:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19444:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19447:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19447:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19461:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19461:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19478:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19478:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19481:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19481:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19537:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19537:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19576:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19576:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19593:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19593:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19604:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19722:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19722:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19755:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19755:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19769:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19769:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19775:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19779:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19811:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19811:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19847:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19893:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19932:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19932:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19945:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19945:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19952:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19952:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-19999:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-19999:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20005:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20022:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20022:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20023:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20023:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20051:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20051:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20061:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20084:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20084:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-20179:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-20179:end -->

<!-- analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-18755 | PLATFORM-LOGGING | books/part-06-ai-infrastructure/68-logging.md#L72 (H2: 可靠传输与背压) | books/part-06-ai-infrastructure/67-monitoring.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/69-trace.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-18755 | delta:SF-2026-ARXIV-2605-18755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18755 |
| SF-2026-ARXIV-2605-18762 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-18762 | delta:SF-2026-ARXIV-2605-18762 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18762 |
| SF-2026-ARXIV-2605-18792 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-18792 | delta:SF-2026-ARXIV-2605-18792 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18792 |
| SF-2026-ARXIV-2605-18796 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-18796 | delta:SF-2026-ARXIV-2605-18796 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18796 |
| SF-2026-ARXIV-2605-18803 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-18803 | delta:SF-2026-ARXIV-2605-18803 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18803 |
| SF-2026-ARXIV-2605-18859 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18859 | delta:SF-2026-ARXIV-2605-18859 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18859 |
| SF-2026-ARXIV-2605-18891 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-18891 | delta:SF-2026-ARXIV-2605-18891 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18891 |
| SF-2026-ARXIV-2605-18899 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-18899 | delta:SF-2026-ARXIV-2605-18899 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2605-18918 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18918 | delta:SF-2026-ARXIV-2605-18918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18918 |
| SF-2026-ARXIV-2605-18930 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18930 | delta:SF-2026-ARXIV-2605-18930 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18930 |
| SF-2026-ARXIV-2605-18991 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18991 | delta:SF-2026-ARXIV-2605-18991 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18991 |
| SF-2026-ARXIV-2605-19008 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19008 | delta:SF-2026-ARXIV-2605-19008 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19008 |
| SF-2026-ARXIV-2605-19049 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-19049 | delta:SF-2026-ARXIV-2605-19049 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19049 |
| SF-2026-ARXIV-2605-19099 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19099 | delta:SF-2026-ARXIV-2605-19099 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19099 |
| SF-2026-ARXIV-2605-19101 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-19101 | delta:SF-2026-ARXIV-2605-19101 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19101 |
| SF-2026-ARXIV-2605-19127 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19127 | delta:SF-2026-ARXIV-2605-19127 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19127 |
| SF-2026-ARXIV-2605-19140 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-19140 | delta:SF-2026-ARXIV-2605-19140 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19140 |
| SF-2026-ARXIV-2605-19151 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19151 | delta:SF-2026-ARXIV-2605-19151 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19151 |
| SF-2026-ARXIV-2605-19169 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-19169 | delta:SF-2026-ARXIV-2605-19169 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19169 |
| SF-2026-ARXIV-2605-19192 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19192 | delta:SF-2026-ARXIV-2605-19192 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19192 |
| SF-2026-ARXIV-2605-19193 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19193 | delta:SF-2026-ARXIV-2605-19193 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19193 |
| SF-2026-ARXIV-2605-19196 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19196 | delta:SF-2026-ARXIV-2605-19196 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19196 |
| SF-2026-ARXIV-2605-19218 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-19218 | delta:SF-2026-ARXIV-2605-19218 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19218 |
| SF-2026-ARXIV-2605-19228 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19228 | delta:SF-2026-ARXIV-2605-19228 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19228 |
| SF-2026-ARXIV-2605-19240 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19240 | delta:SF-2026-ARXIV-2605-19240 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19240 |
| SF-2026-ARXIV-2605-19242 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19242 | delta:SF-2026-ARXIV-2605-19242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19242 |
| SF-2026-ARXIV-2605-19262 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19262 | delta:SF-2026-ARXIV-2605-19262 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19262 |
| SF-2026-ARXIV-2605-19269 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-19269 | delta:SF-2026-ARXIV-2605-19269 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19269 |
| SF-2026-ARXIV-2605-19276 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19276 | delta:SF-2026-ARXIV-2605-19276 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19276 |
| SF-2026-ARXIV-2605-19282 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19282 | delta:SF-2026-ARXIV-2605-19282 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19282 |
| SF-2026-ARXIV-2605-19314 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-19314 | delta:SF-2026-ARXIV-2605-19314 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19314 |
| SF-2026-ARXIV-2605-19319 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-19319 | delta:SF-2026-ARXIV-2605-19319 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19319 |
| SF-2026-ARXIV-2605-19321 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19321 | delta:SF-2026-ARXIV-2605-19321 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19321 |
| SF-2026-ARXIV-2605-19328 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19328 | delta:SF-2026-ARXIV-2605-19328 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19328 |
| SF-2026-ARXIV-2605-19335 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-19335 | delta:SF-2026-ARXIV-2605-19335 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19335 |
| SF-2026-ARXIV-2605-19341 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19341 | delta:SF-2026-ARXIV-2605-19341 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19341 |
| SF-2026-ARXIV-2605-19373 | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#chapter-59 | books/part-06-ai-infrastructure/58-kubeflow.md#chapter-58; books/part-06-ai-infrastructure/60-training-operator.md#chapter-60 | existing:SF-2026-ARXIV-2605-19373 | delta:SF-2026-ARXIV-2605-19373 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19373 |
| SF-2026-ARXIV-2605-19407 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-19407 | delta:SF-2026-ARXIV-2605-19407 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19407 |
| SF-2026-ARXIV-2605-19444 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19444 | delta:SF-2026-ARXIV-2605-19444 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19444 |
| SF-2026-ARXIV-2605-19447 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19447 | delta:SF-2026-ARXIV-2605-19447 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19447 |
| SF-2026-ARXIV-2605-19461 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-19461 | delta:SF-2026-ARXIV-2605-19461 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19461 |
| SF-2026-ARXIV-2605-19478 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19478 | delta:SF-2026-ARXIV-2605-19478 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19478 |
| SF-2026-ARXIV-2605-19481 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-19481 | delta:SF-2026-ARXIV-2605-19481 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19481 |
| SF-2026-ARXIV-2605-19537 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19537 | delta:SF-2026-ARXIV-2605-19537 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19537 |
| SF-2026-ARXIV-2605-19576 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19576 | delta:SF-2026-ARXIV-2605-19576 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19576 |
| SF-2026-ARXIV-2605-19593 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19593 | delta:SF-2026-ARXIV-2605-19593 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19593 |
| SF-2026-ARXIV-2605-19604 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-19604 | delta:SF-2026-ARXIV-2605-19604 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19604 |
| SF-2026-ARXIV-2605-19722 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19722 | delta:SF-2026-ARXIV-2605-19722 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19722 |
| SF-2026-ARXIV-2605-19755 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁) | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 (H2: 本章要回答的问题); books/part-06-ai-infrastructure/73-production-best-practice.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-19755 | delta:SF-2026-ARXIV-2605-19755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19755 |
| SF-2026-ARXIV-2605-19769 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19769 | delta:SF-2026-ARXIV-2605-19769 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19769 |
| SF-2026-ARXIV-2605-19775 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19775 | delta:SF-2026-ARXIV-2605-19775 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19775 |
| SF-2026-ARXIV-2605-19779 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19779 | delta:SF-2026-ARXIV-2605-19779 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19779 |
| SF-2026-ARXIV-2605-19811 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-19811 | delta:SF-2026-ARXIV-2605-19811 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19811 |
| SF-2026-ARXIV-2605-19847 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-19847 | delta:SF-2026-ARXIV-2605-19847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19847 |
| SF-2026-ARXIV-2605-19893 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-19893 | delta:SF-2026-ARXIV-2605-19893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19893 |
| SF-2026-ARXIV-2605-19932 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-19932 | delta:SF-2026-ARXIV-2605-19932 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19932 |
| SF-2026-ARXIV-2605-19945 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-19945 | delta:SF-2026-ARXIV-2605-19945 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19945 |
| SF-2026-ARXIV-2605-19952 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-19952 | delta:SF-2026-ARXIV-2605-19952 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-19952 |
| SF-2026-ARXIV-2605-19999 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-19999 | delta:SF-2026-ARXIV-2605-19999 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19999 |
| SF-2026-ARXIV-2605-20005 | TRAIN-SFT | books/part-04-training-system/29-sft.md#chapter-29 | books/part-04-training-system/28-pretraining.md#chapter-28;books/part-04-training-system/30-lora.md#chapter-30 | existing:SF-2026-ARXIV-2605-20005 | delta:SF-2026-ARXIV-2605-20005 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20005 |
| SF-2026-ARXIV-2605-20022 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-20022 | delta:SF-2026-ARXIV-2605-20022 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20022 |
| SF-2026-ARXIV-2605-20023 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-20023 | delta:SF-2026-ARXIV-2605-20023 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20023 |
| SF-2026-ARXIV-2605-20051 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-20051 | delta:SF-2026-ARXIV-2605-20051 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20051 |
| SF-2026-ARXIV-2605-20061 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-20061 | delta:SF-2026-ARXIV-2605-20061 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20061 |
| SF-2026-ARXIV-2605-20084 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-20084 | delta:SF-2026-ARXIV-2605-20084 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20084 |
| SF-2026-ARXIV-2605-20179 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-20179 | delta:SF-2026-ARXIV-2605-20179 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-20179 |
| SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING | Direct Evolution | No Change — Existing Coverage | books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING |
| SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV | Direct Evolution | No Change — Existing Coverage | books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV |
| SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA | Direct Evolution | No Change — Existing Coverage | books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA |
| SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES | Direct Evolution | No Change — Existing Coverage | books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES |
| SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55; books/part-05-inference-system/README.md#knowledge-tree | existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE | Direct Evolution | No Change — Existing Coverage | books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE |
| SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL | Direct Evolution | No Change — Existing Coverage | books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL |
| SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- | Direct Evolution | No Change — Existing Coverage | books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES- |
| SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A | Direct Evolution | Integrate | books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A |
| SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF | Direct Evolution | No Change — Existing Coverage | books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF |

<!-- books-review:SF-2026-ARXIV-2605-18755:start -->
<!-- existing:SF-2026-ARXIV-2605-18755:start -->对读 `books/part-06-ai-infrastructure/68-logging.md#L72 (H2: 可靠传输与背压)` 及相邻章节后，现有命题为：本章的核心判断是：**Log 是带时间和上下文的离散事件证据。它能解释状态变化与决策原因，但只有结构、身份、隐私和生命周期都被设计后，才是可靠证据。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-18755:end -->
<!-- delta:SF-2026-ARXIV-2605-18755:start -->Exact-v1 的 source-specific delta 是：We propose OMA, a four-layer framework positioning operational memory as an architectural primitive alongside metrics, logs, and traces in the Kubernetes observability stack (Section IV). 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-18755:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-18755:end -->

<!-- books-review:SF-2026-ARXIV-2605-18762:start -->
<!-- existing:SF-2026-ARXIV-2605-18762:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-18762:end -->
<!-- delta:SF-2026-ARXIV-2605-18762:start -->Exact-v1 的 source-specific delta 是：Here, we propose ALDEN, a novel attack that effectively and efficiently extracts private data from RAGs. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-18762:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-18762:end -->

<!-- books-review:SF-2026-ARXIV-2605-18792:start -->
<!-- existing:SF-2026-ARXIV-2605-18792:start -->已读取 current owner `books/part-07-agent/76-rag.md` 与相邻章节 `['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 参数化知识的边界 → ## Offline Ingestion 不是预处理细节 → ## Online Retrieval Pipeline → ### Tenant Filter 必须在检索内核中前置执行 → ## Retrieval 的基本度量 → ## Chunking 是信息边界设计 → ## Reranking 与 Context Packing → ## Relevance 不等于 Sufficient Context → ## Agentic Retrieval：Relevance 也可以是执行先验 → ### Query、Compression 与 Stopping 是联合 Policy → ## RAG 不消除 Hallucination → ### 长文生成需要把检索、叙事状态与核验分开提交 → ## Freshness、Deletion 与 Consistency。<!-- existing:SF-2026-ARXIV-2605-18792:end -->
<!-- delta:SF-2026-ARXIV-2605-18792:start -->AGENT-RAG already separates parametric belief, retrieved evidence, conflict handling and abstention; SABER provides one representation/probe for the existing trust-or-retrieve decision.<!-- delta:SF-2026-ARXIV-2605-18792:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18792:end -->

<!-- books-review:SF-2026-ARXIV-2605-18796:start -->
<!-- existing:SF-2026-ARXIV-2605-18796:start -->已读取 current owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 `['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 调度对象从 request 变成 token state → ## 目标函数不止吞吐 → ## SLO-aware Admission → ### 当前能放下，不等于未来可完成 → ### 不确定输出长度下的 Future-state Reservation → ### 连续 Edge Inference 需要跨窗口携带 Violation-risk Budget → ### 从队列启发式到时间耦合的资源影子价格 → ### Reasoning Budget 必须进入调度与评估身份 → ### Inference-time Process Guidance 也是可调度资源 → ## Iteration Scheduling → ## Routing、Placement 与 Autoscaling → ### 从经验 confidence threshold 到有条件的 Risk Contract → ### 近重复 Workload：先验证兼容，再执行代表项。<!-- existing:SF-2026-ARXIV-2605-18796:end -->
<!-- delta:SF-2026-ARXIV-2605-18796:start -->INFER-SCHEDULING already uses calibrated correctness/cost to commit, defer or escalate across model cascades; UCCI is a bounded uncertainty estimator and threshold solver.<!-- delta:SF-2026-ARXIV-2605-18796:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18796:end -->

<!-- books-review:SF-2026-ARXIV-2605-18803:start -->
<!-- existing:SF-2026-ARXIV-2605-18803:start -->已读取 current owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 `['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']`，并只比较首个 `## Review notes` 之前的正文演进链；owner outline：## 本章要回答的问题 → ## 从三个容易混淆的对象开始 → ### Video generation → ### Predictive environment model → ### Controllable world model → ## 在谈 State 之前，先声明预测 Channel → ## 为什么旧的 Simulator 仍然合理 → ## 演进路线 → ### 从单尺度预测到 Abstraction × Timescale Hierarchy → ### Next-observation generation → ### Action-conditioned transition → ### Goal 属于 Planner Cost，不能成为 Transition 的答案通道 → ### Latent dynamics → ### Imagined rollout。<!-- existing:SF-2026-ARXIV-2605-18803:end -->
<!-- delta:SF-2026-ARXIV-2605-18803:start -->Ch25 已把 planner-induced rare-state coverage 与 prioritized failure discovery 作为训练/评测压力。<!-- delta:SF-2026-ARXIV-2605-18803:end --> Decision=`No Change — Existing Coverage`；shared Books writeback 与独立 post-write audit 见 `books-post-write-semantic-audit.json`。
<!-- books-review:SF-2026-ARXIV-2605-18803:end -->

<!-- books-review:SF-2026-ARXIV-2605-18859:start -->
<!-- existing:SF-2026-ARXIV-2605-18859:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。正文尚未明确承载本 family 的增量：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-18859:end -->
<!-- delta:SF-2026-ARXIV-2605-18859:start -->Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告<!-- delta:SF-2026-ARXIV-2605-18859:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18859:end -->

<!-- books-review:SF-2026-ARXIV-2605-18891:start -->
<!-- existing:SF-2026-ARXIV-2605-18891:start -->独立 reviewer 顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8e594c3827c4a7778945dbe71f0c1af1ca4089918dcd0c8998ff54d98ac664a1。<!-- existing:SF-2026-ARXIV-2605-18891:end -->
<!-- delta:SF-2026-ARXIV-2605-18891:start -->reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。<!-- delta:SF-2026-ARXIV-2605-18891:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18891:end -->

<!-- books-review:SF-2026-ARXIV-2605-18899:start -->
<!-- existing:SF-2026-ARXIV-2605-18899:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-18899:end -->
<!-- delta:SF-2026-ARXIV-2605-18899:start -->continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision<!-- delta:SF-2026-ARXIV-2605-18899:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18899:end -->

<!-- books-review:SF-2026-ARXIV-2605-18918:start -->
<!-- existing:SF-2026-ARXIV-2605-18918:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18918:end -->
<!-- delta:SF-2026-ARXIV-2605-18918:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18918:end -->
<!-- books-review:SF-2026-ARXIV-2605-18918:end -->

<!-- books-review:SF-2026-ARXIV-2605-18930:start -->
<!-- existing:SF-2026-ARXIV-2605-18930:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18930:end -->
<!-- delta:SF-2026-ARXIV-2605-18930:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18930:end -->
<!-- books-review:SF-2026-ARXIV-2605-18930:end -->

<!-- books-review:SF-2026-ARXIV-2605-18991:start -->
<!-- existing:SF-2026-ARXIV-2605-18991:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18991:end -->
<!-- delta:SF-2026-ARXIV-2605-18991:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18991:end -->
<!-- books-review:SF-2026-ARXIV-2605-18991:end -->

<!-- books-review:SF-2026-ARXIV-2605-19008:start -->
<!-- existing:SF-2026-ARXIV-2605-19008:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-19008:end -->
<!-- delta:SF-2026-ARXIV-2605-19008:start -->当前 pretraining 章有 optimizer/clip/rollback，尚缺 optimizer 之上的 bounded autonomous control envelope、action budget 与 human override；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-19008:end -->
<!-- books-review:SF-2026-ARXIV-2605-19008:end -->

<!-- books-review:SF-2026-ARXIV-2605-19049:start -->
<!-- existing:SF-2026-ARXIV-2605-19049:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-19049:end -->
<!-- delta:SF-2026-ARXIV-2605-19049:start -->当前 KV 章以 Transformer KV 为主，没有明确 linear-attention recurrent state 的 IO-aware buffering/placement owner；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-19049:end -->
<!-- books-review:SF-2026-ARXIV-2605-19049:end -->

<!-- books-review:SF-2026-ARXIV-2605-19099:start -->
<!-- existing:SF-2026-ARXIV-2605-19099:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-19099:end -->
<!-- delta:SF-2026-ARXIV-2605-19099:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19099:end -->
<!-- books-review:SF-2026-ARXIV-2605-19099:end -->

<!-- books-review:SF-2026-ARXIV-2605-19101:start -->
<!-- existing:SF-2026-ARXIV-2605-19101:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；正文主线 headings=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Synthetic data：从“先生成再打分”到 Specification Compilation']。<!-- existing:SF-2026-ARXIV-2605-19101:end -->
<!-- delta:SF-2026-ARXIV-2605-19101:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19101:end -->
<!-- books-review:SF-2026-ARXIV-2605-19101:end -->

<!-- books-review:SF-2026-ARXIV-2605-19127:start -->
<!-- existing:SF-2026-ARXIV-2605-19127:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19127:end -->
<!-- delta:SF-2026-ARXIV-2605-19127:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19127:end -->
<!-- books-review:SF-2026-ARXIV-2605-19127:end -->

<!-- books-review:SF-2026-ARXIV-2605-19140:start -->
<!-- existing:SF-2026-ARXIV-2605-19140:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-19140:end -->
<!-- delta:SF-2026-ARXIV-2605-19140:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19140:end -->
<!-- books-review:SF-2026-ARXIV-2605-19140:end -->

<!-- books-review:SF-2026-ARXIV-2605-19151:start -->
<!-- existing:SF-2026-ARXIV-2605-19151:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19151:end -->
<!-- delta:SF-2026-ARXIV-2605-19151:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19151:end -->
<!-- books-review:SF-2026-ARXIV-2605-19151:end -->

<!-- books-review:SF-2026-ARXIV-2605-19169:start -->
<!-- existing:SF-2026-ARXIV-2605-19169:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-19169:end -->
<!-- delta:SF-2026-ARXIV-2605-19169:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19169:end -->
<!-- books-review:SF-2026-ARXIV-2605-19169:end -->

<!-- books-review:SF-2026-ARXIV-2605-19192:start -->
<!-- existing:SF-2026-ARXIV-2605-19192:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-19192:end -->
<!-- delta:SF-2026-ARXIV-2605-19192:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19192:end -->
<!-- books-review:SF-2026-ARXIV-2605-19192:end -->

<!-- books-review:SF-2026-ARXIV-2605-19193:start -->
<!-- existing:SF-2026-ARXIV-2605-19193:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-19193:end -->
<!-- delta:SF-2026-ARXIV-2605-19193:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19193:end -->
<!-- books-review:SF-2026-ARXIV-2605-19193:end -->

<!-- books-review:SF-2026-ARXIV-2605-19196:start -->
<!-- existing:SF-2026-ARXIV-2605-19196:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-19196:end -->
<!-- delta:SF-2026-ARXIV-2605-19196:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19196:end -->
<!-- books-review:SF-2026-ARXIV-2605-19196:end -->

<!-- books-review:SF-2026-ARXIV-2605-19218:start -->
<!-- existing:SF-2026-ARXIV-2605-19218:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-19218:end -->
<!-- delta:SF-2026-ARXIV-2605-19218:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19218:end -->
<!-- books-review:SF-2026-ARXIV-2605-19218:end -->

<!-- books-review:SF-2026-ARXIV-2605-19228:start -->
<!-- existing:SF-2026-ARXIV-2605-19228:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-19228:end -->
<!-- delta:SF-2026-ARXIV-2605-19228:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-19228:end -->
<!-- books-review:SF-2026-ARXIV-2605-19228:end -->

<!-- books-review:SF-2026-ARXIV-2605-19240:start -->
<!-- existing:SF-2026-ARXIV-2605-19240:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19240:end -->
<!-- delta:SF-2026-ARXIV-2605-19240:start -->Therefore, we propose CASPIAN, the first framework that provides a unified, cross-channel causal analysis of cascade behavior in LLM-MAS through online monitoring of dynamic influence propagation across agents.<!-- delta:SF-2026-ARXIV-2605-19240:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19240:end -->

<!-- books-review:SF-2026-ARXIV-2605-19242:start -->
<!-- existing:SF-2026-ARXIV-2605-19242:start -->`books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19242:end -->
<!-- delta:SF-2026-ARXIV-2605-19242:start -->We propose PhyWorld, a video generation world model designed to produce temporally coherent and physically faithful scene continuations through two-stage post-training.<!-- delta:SF-2026-ARXIV-2605-19242:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19242:end -->

<!-- books-review:SF-2026-ARXIV-2605-19262:start -->
<!-- existing:SF-2026-ARXIV-2605-19262:start -->`books/part-06-ai-infrastructure/72-security.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19262:end -->
<!-- delta:SF-2026-ARXIV-2605-19262:start -->In this work, we present the first systematic study of training-time backdoor attacks on MDLMs.<!-- delta:SF-2026-ARXIV-2605-19262:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19262:end -->

<!-- books-review:SF-2026-ARXIV-2605-19269:start -->
<!-- existing:SF-2026-ARXIV-2605-19269:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19269:end -->
<!-- delta:SF-2026-ARXIV-2605-19269:start -->We introduce CODA, a GPU kernel abstraction that expresses these computations as GEMM-plus-epilogue programs.<!-- delta:SF-2026-ARXIV-2605-19269:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19269:end -->

<!-- books-review:SF-2026-ARXIV-2605-19276:start -->
<!-- existing:SF-2026-ARXIV-2605-19276:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19276:end -->
<!-- delta:SF-2026-ARXIV-2605-19276:start -->Adhering to the design philosophy of modularization and component decoupling, the platform boasts three core advantages: high compatibility, flexibility, and high concurrency.<!-- delta:SF-2026-ARXIV-2605-19276:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19276:end -->

<!-- books-review:SF-2026-ARXIV-2605-19282:start -->
<!-- existing:SF-2026-ARXIV-2605-19282:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19282:end -->
<!-- delta:SF-2026-ARXIV-2605-19282:start -->While this uniform spectral whitening enhances exploration and outperforms AdamW in LLM pretraining, we show it could lead to fundamental limitations beyond pretraining in two regimes: (i) cross-modality vision-language-action (VLA) training, where inherently low-rank action-module gradients cause amplification of noisy tail directions, and (ii) reinforcement learning with verifiable rewards (RLVR), where low-SNR gradients and the need to preserve per-head specialization from prior training make whitening unstable.<!-- delta:SF-2026-ARXIV-2605-19282:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19282:end -->

<!-- books-review:SF-2026-ARXIV-2605-19314:start -->
<!-- existing:SF-2026-ARXIV-2605-19314:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19314:end -->
<!-- delta:SF-2026-ARXIV-2605-19314:start -->We study task-state misalignment, a task-level consistency failure in which the planner's active stage, runtime evidence, remembered context, and delegated executor no longer justify the same next-step decision.<!-- delta:SF-2026-ARXIV-2605-19314:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19314:end -->

<!-- books-review:SF-2026-ARXIV-2605-19319:start -->
<!-- existing:SF-2026-ARXIV-2605-19319:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19319:end -->
<!-- delta:SF-2026-ARXIV-2605-19319:start -->In this work, we study whether image editing models can serve as sparse visual world models for robot manipulation by predicting task-level future states without dense video rollout.<!-- delta:SF-2026-ARXIV-2605-19319:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19319:end -->

<!-- books-review:SF-2026-ARXIV-2605-19321:start -->
<!-- existing:SF-2026-ARXIV-2605-19321:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19321:end -->
<!-- delta:SF-2026-ARXIV-2605-19321:start -->In this paper, we introduce a safeguard design that leverages the transferability of jailbreak attacks to enforce prompt safety before target model inference.<!-- delta:SF-2026-ARXIV-2605-19321:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19321:end -->

<!-- books-review:SF-2026-ARXIV-2605-19328:start -->
<!-- existing:SF-2026-ARXIV-2605-19328:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19328:end -->
<!-- delta:SF-2026-ARXIV-2605-19328:start -->We introduce an intent contrast dataset pipeline that augments existing datasets with paired adversarial and benign goals to measure both security and utility.<!-- delta:SF-2026-ARXIV-2605-19328:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19328:end -->

<!-- books-review:SF-2026-ARXIV-2605-19335:start -->
<!-- existing:SF-2026-ARXIV-2605-19335:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19335:end -->
<!-- delta:SF-2026-ARXIV-2605-19335:start -->We present LIOS(Leverage I/O Stall), a framework that executes index updates inside search-side I/O stall windows.<!-- delta:SF-2026-ARXIV-2605-19335:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19335:end -->

<!-- books-review:SF-2026-ARXIV-2605-19341:start -->
<!-- existing:SF-2026-ARXIV-2605-19341:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19341:end -->
<!-- delta:SF-2026-ARXIV-2605-19341:start -->To study root causes, we introduce HalluWorld, an extensible benchmark grounded in an explicit reference-world formulation: a model hallucinates when it produces an observable claim that is false with respect to this world.<!-- delta:SF-2026-ARXIV-2605-19341:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19341:end -->

<!-- books-review:SF-2026-ARXIV-2605-19373:start -->
<!-- existing:SF-2026-ARXIV-2605-19373:start -->已逐章读取 `books/part-06-ai-infrastructure/59-model-registry.md` 与相邻章节 ['books/part-06-ai-infrastructure/58-kubeflow.md', 'books/part-06-ai-infrastructure/60-training-operator.md']；当前正文拥有 surrounding principle，但尚未显式承载 `Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies` 改变的 state/data/control/evidence boundary。 owner_sha256=7691a4f16c4ed6ecd5e5eb8487324292df7cfb82b3c10aee71730bc70a0f4290。<!-- existing:SF-2026-ARXIV-2605-19373:end -->
<!-- delta:SF-2026-ARXIV-2605-19373:start -->Conflict-Free Replicated Data Types for Neural Network Model Merging: A Two-Layer Architecture Enabling CRDT-Compliant Model Merging Across 26 Strategies 提出的具体变化是：To resolve this, we present a two-layer architecture -- CRDTMergeState -- that wraps any merge strategy in a CRDT-compliant (Conflict-Free Replicated Data Type) layer. 摘要中的长期系统挑战为：distributed model merging requires a conflict-free state wrapper because weight merges are not CRDT operations。它可能改变 `PLATFORM-MODEL-REGISTRY` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“We prove that this separation guarantees Strong Eventual Consistency: all replicas receiving the same contributions compute identical merged models, regardless of message ordering.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-19373:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-19373:end -->

<!-- books-review:SF-2026-ARXIV-2605-19407:start -->
<!-- existing:SF-2026-ARXIV-2605-19407:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19407:end -->
<!-- delta:SF-2026-ARXIV-2605-19407:start -->We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime.<!-- delta:SF-2026-ARXIV-2605-19407:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19407:end -->

<!-- books-review:SF-2026-ARXIV-2605-19444:start -->
<!-- existing:SF-2026-ARXIV-2605-19444:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19444:end -->
<!-- delta:SF-2026-ARXIV-2605-19444:start -->We argue these gains are systematically misinterpreted: most reflect sharpening of already-solvable problems rather than genuine learning, while problems corrupted from correct to incorrect outnumber truly learned ones, and this damage is irreversible once majority vote locks onto a wrong answer.<!-- delta:SF-2026-ARXIV-2605-19444:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19444:end -->

<!-- books-review:SF-2026-ARXIV-2605-19447:start -->
<!-- existing:SF-2026-ARXIV-2605-19447:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19447:end -->
<!-- delta:SF-2026-ARXIV-2605-19447:start -->We systematically study five feedback sources and two insertion granularities and introduce SERL, a selective environment-reweighted learning framework.<!-- delta:SF-2026-ARXIV-2605-19447:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19447:end -->

<!-- books-review:SF-2026-ARXIV-2605-19461:start -->
<!-- existing:SF-2026-ARXIV-2605-19461:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19461:end -->
<!-- delta:SF-2026-ARXIV-2605-19461:start -->We show this stems from reverse KL minimization's mode-seeking behavior, which reinforces the first high-reward trajectory found rather than maintaining a distribution over multiple diverse solutions.<!-- delta:SF-2026-ARXIV-2605-19461:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19461:end -->

<!-- books-review:SF-2026-ARXIV-2605-19478:start -->
<!-- existing:SF-2026-ARXIV-2605-19478:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19478:end -->
<!-- delta:SF-2026-ARXIV-2605-19478:start -->While adapter security has seen initial study, the risks of the burgeoning prompt-based ecosystem remain critically unexplored.<!-- delta:SF-2026-ARXIV-2605-19478:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19478:end -->

<!-- books-review:SF-2026-ARXIV-2605-19481:start -->
<!-- existing:SF-2026-ARXIV-2605-19481:start -->已顺读 `books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19481:end -->
<!-- delta:SF-2026-ARXIV-2605-19481:start -->Leveraging this capability, we present C2CServe, a request-granularity serverless LLM serving system that allows MIG instances to switch models across requests without reloading weights into HBM.<!-- delta:SF-2026-ARXIV-2605-19481:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19481:end -->

<!-- books-review:SF-2026-ARXIV-2605-19537:start -->
<!-- existing:SF-2026-ARXIV-2605-19537:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19537:end -->
<!-- delta:SF-2026-ARXIV-2605-19537:start -->While critical for scalability, system-level optimizations, such as custom CUDA kernels and reduced-precision arithmetic, can alter token probabilities and introduce non-determinism, possibly cascading into divergent generation.<!-- delta:SF-2026-ARXIV-2605-19537:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19537:end -->

<!-- books-review:SF-2026-ARXIV-2605-19576:start -->
<!-- existing:SF-2026-ARXIV-2605-19576:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19576:end -->
<!-- delta:SF-2026-ARXIV-2605-19576:start -->Self-evolving skill libraries face a silent failure mode we term \emph{library drift}: unbounded skill accumulation without outcome-driven lifecycle management causes retrieval degradation, false-positive injections, and performance stagnation.<!-- delta:SF-2026-ARXIV-2605-19576:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19576:end -->

<!-- books-review:SF-2026-ARXIV-2605-19593:start -->
<!-- existing:SF-2026-ARXIV-2605-19593:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19593:end -->
<!-- delta:SF-2026-ARXIV-2605-19593:start -->In this paper, we present an empirical study of how different LLMs behave across hardware platforms, focusing on the performance implications of layer offloading and preemption.<!-- delta:SF-2026-ARXIV-2605-19593:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19593:end -->

<!-- books-review:SF-2026-ARXIV-2605-19604:start -->
<!-- existing:SF-2026-ARXIV-2605-19604:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19604:end -->
<!-- delta:SF-2026-ARXIV-2605-19604:start -->We introduce Formal Skill, a runtime-native abstraction that represents reusable capability with JSON metadata and action schemas, reliable Python executors, hook-governed control logic, Formal Skill routing, and skill-local runtime state.<!-- delta:SF-2026-ARXIV-2605-19604:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19604:end -->

<!-- books-review:SF-2026-ARXIV-2605-19722:start -->
<!-- existing:SF-2026-ARXIV-2605-19722:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19722:end -->
<!-- delta:SF-2026-ARXIV-2605-19722:start -->We present a trace-based benchmark of 30 local vulnerability-analysis tasks with fixed tools, deterministic success predicates, redaction rules, and grounding checks, and compare four stock models against uncensored or abliterated derivatives: Gemma 4 31B, Gemma 4 26B A4B, Qwen2.5-Coder 7B, and Llama 3.1 8B.<!-- delta:SF-2026-ARXIV-2605-19722:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19722:end -->

<!-- books-review:SF-2026-ARXIV-2605-19755:start -->
<!-- existing:SF-2026-ARXIV-2605-19755:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L29 (H2: 生命周期威胁)` 及相邻章节后，现有命题为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-19755:end -->
<!-- delta:SF-2026-ARXIV-2605-19755:start -->Exact-v1 的 source-specific delta 是：方案扩展 CycloneDX，记录 AI provenance、model lineage、disclosure metadata，并用组件 hash、签名、容器运行态和 agent 生成的环境记录绑定 artifact；自动化流水线负责环境发现、漏洞富化、schema 校验和 reproducibility audit，材料不全时保留 partial-attestation 状态。 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-19755:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-19755:end -->

<!-- books-review:SF-2026-ARXIV-2605-19769:start -->
<!-- existing:SF-2026-ARXIV-2605-19769:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19769:end -->
<!-- delta:SF-2026-ARXIV-2605-19769:start -->We present OpenComputer, a verifier-grounded framework for constructing verifiable software worlds for computer-use agents.<!-- delta:SF-2026-ARXIV-2605-19769:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19769:end -->

<!-- books-review:SF-2026-ARXIV-2605-19775:start -->
<!-- existing:SF-2026-ARXIV-2605-19775:start -->`books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19775:end -->
<!-- delta:SF-2026-ARXIV-2605-19775:start -->By systematically exploring the interplay between Data, Tensor, and Pipeline parallelism, we identify critical bottlenecks that defy standard scaling heuristics.<!-- delta:SF-2026-ARXIV-2605-19775:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19775:end -->

<!-- books-review:SF-2026-ARXIV-2605-19779:start -->
<!-- existing:SF-2026-ARXIV-2605-19779:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19779:end -->
<!-- delta:SF-2026-ARXIV-2605-19779:start -->We further develop compositional uncertainty bounds for multi-agent pipelines (validated via simulation across inter-stage correlations rho in [-0.5, 0.9]), a conformal abstention rule for pairwise rankings with controlled false-ranking rate, and FDR-corrected abstention for leaderboard-scale multiple testing.<!-- delta:SF-2026-ARXIV-2605-19779:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19779:end -->

<!-- books-review:SF-2026-ARXIV-2605-19811:start -->
<!-- existing:SF-2026-ARXIV-2605-19811:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19811:end -->
<!-- delta:SF-2026-ARXIV-2605-19811:start -->In this work, we propose LionMuon, which retains the effectiveness of Muon steps while considerably cutting the averaged iteration cost, similar to sign-based methods.<!-- delta:SF-2026-ARXIV-2605-19811:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19811:end -->

<!-- books-review:SF-2026-ARXIV-2605-19847:start -->
<!-- existing:SF-2026-ARXIV-2605-19847:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19847:end -->
<!-- delta:SF-2026-ARXIV-2605-19847:start -->We show that this framing understates leakage under same-index account collusion.<!-- delta:SF-2026-ARXIV-2605-19847:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19847:end -->

<!-- books-review:SF-2026-ARXIV-2605-19893:start -->
<!-- existing:SF-2026-ARXIV-2605-19893:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19893:end -->
<!-- delta:SF-2026-ARXIV-2605-19893:start -->We present SSV, a sparse speculative-verification framework that turns dynamic sparse attention into a verification-oriented workload.<!-- delta:SF-2026-ARXIV-2605-19893:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19893:end -->

<!-- books-review:SF-2026-ARXIV-2605-19932:start -->
<!-- existing:SF-2026-ARXIV-2605-19932:start -->已顺读 `books/part-07-agent/75-context.md` 与相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19932:end -->
<!-- delta:SF-2026-ARXIV-2605-19932:start -->We introduce PEEK, a system that caches and maintains this orientation knowledge as a context map: a small, constant-sized artifact in the agent's prompt that gives it a persistent peek into the external context.<!-- delta:SF-2026-ARXIV-2605-19932:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19932:end -->

<!-- books-review:SF-2026-ARXIV-2605-19945:start -->
<!-- existing:SF-2026-ARXIV-2605-19945:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19945:end -->
<!-- delta:SF-2026-ARXIV-2605-19945:start -->We propose GEM, GPU-variability-aware Expert Mapping, a framework for GPU variability-aware expert to GPU mapping for MoE models.<!-- delta:SF-2026-ARXIV-2605-19945:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19945:end -->

<!-- books-review:SF-2026-ARXIV-2605-19952:start -->
<!-- existing:SF-2026-ARXIV-2605-19952:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-19952:end -->
<!-- delta:SF-2026-ARXIV-2605-19952:start -->To address these limitations, we propose TriMem, which maintains three coexisting representation granularities, including raw dialogue segments anchored by source identifiers for storage fidelity, extracted atomic facts for efficient memory retrieval, synthesized profiles that aggregate dispersed facts into holistic semantic understanding for deep reasoning.<!-- delta:SF-2026-ARXIV-2605-19952:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-19952:end -->

<!-- books-review:SF-2026-ARXIV-2605-19999:start -->
<!-- existing:SF-2026-ARXIV-2605-19999:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-19999:end -->
<!-- delta:SF-2026-ARXIV-2605-19999:start -->Benchmark datasets are critical for reproducible, reliable, and discriminative evaluation of LLMs.<!-- delta:SF-2026-ARXIV-2605-19999:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-19999:end -->

<!-- books-review:SF-2026-ARXIV-2605-20005:start -->
<!-- existing:SF-2026-ARXIV-2605-20005:start -->已顺读 `books/part-04-training-system/29-sft.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md', 'books/part-04-training-system/30-lora.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20005:end -->
<!-- delta:SF-2026-ARXIV-2605-20005:start -->We identify a simple mechanism for doing so: per-step forgetting is bounded by the product of the learning rate and the square root of the current training loss.<!-- delta:SF-2026-ARXIV-2605-20005:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20005:end -->

<!-- books-review:SF-2026-ARXIV-2605-20022:start -->
<!-- existing:SF-2026-ARXIV-2605-20022:start -->已顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20022:end -->
<!-- delta:SF-2026-ARXIV-2605-20022:start -->Speculative decoding accelerates memory-bound LLM inference without quality degradation by using a fast drafter to propose multiple candidate tokens and the target model to verify them in parallel.<!-- delta:SF-2026-ARXIV-2605-20022:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20022:end -->

<!-- books-review:SF-2026-ARXIV-2605-20023:start -->
<!-- existing:SF-2026-ARXIV-2605-20023:start -->`books/part-07-agent/84-agent-platform.md` 与相邻章节已拥有同一问题的 canonical owner、commit/evidence boundary、failure fallback 与旧路径共存；本 family 仅增加受限方法、实例或负面证据。<!-- existing:SF-2026-ARXIV-2605-20023:end -->
<!-- delta:SF-2026-ARXIV-2605-20023:start -->Yet the same benchmarks show wide variance, with 16 of 84 tasks suffering negative deltas when Skills are introduced.<!-- delta:SF-2026-ARXIV-2605-20023:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-20023:end -->

<!-- books-review:SF-2026-ARXIV-2605-20051:start -->
<!-- existing:SF-2026-ARXIV-2605-20051:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20051:end -->
<!-- delta:SF-2026-ARXIV-2605-20051:start -->Because many projects reimplement similar model-centric workflows, a vulnerability disclosed in one repository can recur as a variant in another repository with a related design.<!-- delta:SF-2026-ARXIV-2605-20051:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20051:end -->

<!-- books-review:SF-2026-ARXIV-2605-20061:start -->
<!-- existing:SF-2026-ARXIV-2605-20061:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20061:end -->
<!-- delta:SF-2026-ARXIV-2605-20061:start -->To address this, we propose ReBel (Reward Belief), a process-level reinforcement learning algorithm that explicitly models structured belief states to summarize interaction history and guide subsequent policy learning.<!-- delta:SF-2026-ARXIV-2605-20061:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20061:end -->

<!-- books-review:SF-2026-ARXIV-2605-20084:start -->
<!-- existing:SF-2026-ARXIV-2605-20084:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20084:end -->
<!-- delta:SF-2026-ARXIV-2605-20084:start -->In this work, we develop BalanceRAG to certify threshold pairs at a target risk level.<!-- delta:SF-2026-ARXIV-2605-20084:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20084:end -->

<!-- books-review:SF-2026-ARXIV-2605-20179:start -->
<!-- existing:SF-2026-ARXIV-2605-20179:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-20179:end -->
<!-- delta:SF-2026-ARXIV-2605-20179:start -->In this work, we propose TIDE, a novel resource-efficient inference system that leverages the temporal stability of expert activations during the diffusion process within the block.<!-- delta:SF-2026-ARXIV-2605-20179:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-20179:end -->

<!-- books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->
<!-- existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->`books/part-04-training-system/36-distributed-training.md` 已以更一般的 TRAIN-DISTRIBUTED-TRAINING 演进链承载 `DynaTrain: Fast Online Parallelism Switching for Elastic LLM Training` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->
<!-- delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:start -->We present DynaTrain, a distributed training system for sub-second, online reconfiguration across arbitrary multi-dimensional parallelism.<!-- delta:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-DYNATRAIN-FAST-ONLINE-PARALLELISM-SWITCHING-FOR-ELASTIC-LLM-TRAINING:end -->

<!-- books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->
<!-- existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；owner 当前主干包含 ['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->
<!-- delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:start -->Coding agents accumulate extensive context during long-running tasks, yet fixed context windows force practitioners to choose between truncation and task failure.<!-- delta:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-EVALUATING-MEMORY-CONDENSATION-STRATEGIES-FOR-CODING-AGENTS-IN-DATA-DRIV:end -->

<!-- books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->
<!-- existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 PLATFORM-EVALUATION-SYSTEM 演进链承载 `Fine-Grained Benchmark Generation for Comprehensive Evaluation of Foundation Models` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->
<!-- delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:start -->We introduce a framework for automated benchmark generation.<!-- delta:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-FINE-GRAINED-BENCHMARK-GENERATION-FOR-COMPREHENSIVE-EVALUATION-OF-FOUNDA:end -->

<!-- books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->
<!-- existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->`books/part-04-training-system/27-data.md` 已以更一般的 TRAIN-DATA 演进链承载 `How Faithful Is Trajectory-Based Data Attribution? Error Sources, Remedies, and Practical Guidelines` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->
<!-- delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:start -->We propose AdamW-influence to fully account for AdamW's optimization dynamics, yielding improvements from 10% to over 300% in Spearman correlation between estimated and ground-truth influence across four settings spanning MLP, CNN, GPT-2, and Llama 3.2-1B.<!-- delta:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-HOW-FAITHFUL-IS-TRAJECTORY-BASED-DATA-ATTRIBUTION-ERROR-SOURCES-REMEDIES:end -->

<!-- books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->
<!-- existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-05-inference-system/README.md']；owner 当前主干包含 ['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->
<!-- delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:start -->We present INAR-VL, a lightweight edge-cloud routing system for multimodal inference in a two-tier deployment.<!-- delta:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-INAR-VL-INPUT-AWARE-ROUTING-FOR-EDGE-CLOUD-VISION-LANGUAGE-INFERENCE:end -->

<!-- books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->
<!-- existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 已以更一般的 INFER-KV-CACHE 演进链承载 `Not All Tokens Are Worth Caching: Learning Semantic-Aware Eviction for LLM Prefix Caches` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->
<!-- delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:start -->We show that different token types within a prompt, including system prompts, user queries, tool outputs, model responses, and chain-of-thought reasoning, exhibit up to 756x variation in reuse rates, yet no existing eviction policy exploits this signal.<!-- delta:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-NOT-ALL-TOKENS-ARE-WORTH-CACHING-LEARNING-SEMANTIC-AWARE-EVICTION-FOR-LL:end -->

<!-- books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->
<!-- existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->`books/part-06-ai-infrastructure/66-evaluation-system.md` 已以更一般的 PLATFORM-EVALUATION-SYSTEM 演进链承载 `PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->
<!-- delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:start -->We present PASC (Pipeline-Aware Split Conformal), which reduces multi-stage joint coverage to a single scalar conformal prediction problem on the joint maximum nonconformity score.<!-- delta:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-PASC-PIPELINE-AWARE-CONFORMAL-PREDICTION-WITH-JOINT-COVERAGE-GUARANTEES-:end -->

<!-- books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->
<!-- existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；owner 当前主干包含 ['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->
<!-- delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->We formulate late-stage checkpoint selection as a stability-aware decision problem under evaluation uncertainty and propose a progressive framework combining pointwise filtering, listwise ranking, and pairwise refinement.<!-- delta:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->
<!-- existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；owner 当前主干包含 ['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->
<!-- delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:start -->We present Spherical KV, a long-context inference method that treats KV allocation as a rate-distortion problem grounded in attention geometry for efficient decoding.<!-- delta:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end --> Independent decision=`No Change — Existing Coverage`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-SPHERICAL-KV-ANGLE-DOMAIN-ATTENTION-AND-RATE-DISTORTION-RETENTION-FOR-EF:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260520-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260520 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260520-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260520-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=75；selected=3；all others retain completed reviews | passed |
| SA-20260520-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=652；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260520/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260520/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-20.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
