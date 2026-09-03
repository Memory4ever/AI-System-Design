# Daily Research — 2026-05-25

**Research Date:** 2026-05-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-24 09:00:00 ～ 2026-05-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 497 个注册 arXiv identity，冻结 56 个 Source Family；pre-denominator closure=441，withdrawn pre-denominator=0。56 个旧候选被迁回正确 owner day，0 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-25 |
| Window End | 2026-05-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260525-CREATED-ecb857262ce45b51 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-24T09:00:00+08:00 | 2026-05-25T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 497 | SF-2026-ARXIV-2605-22850;SF-2026-ARXIV-2605-22863;SF-2026-ARXIV-2605-22866;SF-2026-ARXIV-2605-22868;SF-2026-ARXIV-2605-22882;SF-2026-ARXIV-2605-22883;SF-2026-ARXIV-2605-22884;SF-2026-ARXIV-2605-22891;SF-2026-ARXIV-2605-22894;SF-2026-ARXIV-2605-22896;SF-2026-ARXIV-2605-22905;SF-2026-ARXIV-2605-22949;SF-2026-ARXIV-2605-22984;SF-2026-ARXIV-2605-23019;SF-2026-ARXIV-2605-23055;SF-2026-ARXIV-2605-23057;SF-2026-ARXIV-2605-23058;SF-2026-ARXIV-2605-23066;SF-2026-ARXIV-2605-23067;SF-2026-ARXIV-2605-23071;SF-2026-ARXIV-2605-23078;SF-2026-ARXIV-2605-23080;SF-2026-ARXIV-2605-23157;SF-2026-ARXIV-2605-23158;SF-2026-ARXIV-2605-23168;SF-2026-ARXIV-2605-23170;SF-2026-ARXIV-2605-23196;SF-2026-ARXIV-2605-23200;SF-2026-ARXIV-2605-23215;SF-2026-ARXIV-2605-23218;SF-2026-ARXIV-2605-23220;SF-2026-ARXIV-2605-23258;SF-2026-ARXIV-2605-23262;SF-2026-ARXIV-2605-23294;SF-2026-ARXIV-2605-23296;SF-2026-ARXIV-2605-23311;SF-2026-ARXIV-2605-23348;SF-2026-ARXIV-2605-23362;SF-2026-ARXIV-2605-23389;SF-2026-ARXIV-2605-23414;SF-2026-ARXIV-2605-23454;SF-2026-ARXIV-2605-23464;SF-2026-ARXIV-2605-23493;SF-2026-ARXIV-2605-23574;SF-2026-ARXIV-2605-23590;SF-2026-ARXIV-2605-23628;SF-2026-ARXIV-2605-23640;SF-2026-ARXIV-2605-23657;SF-2026-ARXIV-2605-23701;SF-2026-ARXIV-2605-23723;SF-2026-ARXIV-2605-23764;SF-2026-ARXIV-2605-23856;SF-2026-ARXIV-2605-23893;SF-2026-ARXIV-2605-23899;SF-2026-ARXIV-2605-23904;SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | created-day pages=closed; OAI category sets=closed; direct same-day OAI=400 | 2026-05-25T09:00:00+08:00 | coverage:SRC-ARXIV:20260525 | — |

<!-- coverage:SRC-ARXIV:20260525:start -->全量 raw inventory=497；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260525:end -->

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
| SF-2026-ARXIV-2605-22850 | arXiv:2605.22850v1 | paper-v1:2605.22850 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22850 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-22850 | no |
| SF-2026-ARXIV-2605-22863 | arXiv:2605.22863v1 | paper-v1:2605.22863 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22863 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-22863 | no |
| SF-2026-ARXIV-2605-22866 | arXiv:2605.22866v1 | paper-v1:2605.22866 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22866 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-22866 | no |
| SF-2026-ARXIV-2605-22868 | arXiv:2605.22868v1 | paper-v1:2605.22868 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22868 | self | — | new_in_window | — | Structural Candidate | books-review:SF-2026-ARXIV-2605-22868 | no |
| SF-2026-ARXIV-2605-22882 | arXiv:2605.22882v1 | paper-v1:2605.22882 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22882 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22882 | no |
| SF-2026-ARXIV-2605-22883 | arXiv:2605.22883v1 | paper-v1:2605.22883 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22883 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605-22883 | no |
| SF-2026-ARXIV-2605-22884 | arXiv:2605.22884v1 | paper-v1:2605.22884 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22884 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-22884 | no |
| SF-2026-ARXIV-2605-22891 | arXiv:2605.22891v1 | paper-v1:2605.22891 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22891 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22891 | no |
| SF-2026-ARXIV-2605-22894 | arXiv:2605.22894v1 | paper-v1:2605.22894 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22894 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22894 | no |
| SF-2026-ARXIV-2605-22896 | arXiv:2605.22896v1 | paper-v1:2605.22896 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22896 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22896 | no |
| SF-2026-ARXIV-2605-22905 | arXiv:2605.22905v1 | paper-v1:2605.22905 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-22905 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22905 | no |
| SF-2026-ARXIV-2605-22949 | arXiv:2605.22949v1 | paper-v1:2605.22949 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22949 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-22949 | no |
| SF-2026-ARXIV-2605-22984 | arXiv:2605.22984v1 | paper-v1:2605.22984 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-22984 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-22984 | no |
| SF-2026-ARXIV-2605-23019 | arXiv:2605.23019v1 | paper-v1:2605.23019 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23019 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-23019 | no |
| SF-2026-ARXIV-2605-23055 | arXiv:2605.23055v1 | paper-v1:2605.23055 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23055 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23055 | no |
| SF-2026-ARXIV-2605-23057 | arXiv:2605.23057v1 | paper-v1:2605.23057 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23057 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23057 | no |
| SF-2026-ARXIV-2605-23058 | arXiv:2605.23058v1 | paper-v1:2605.23058 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23058 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23058 | no |
| SF-2026-ARXIV-2605-23066 | arXiv:2605.23066v1 | paper-v1:2605.23066 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23066 | self | — | new_in_window | TRAIN-CHECKPOINT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23066 | no |
| SF-2026-ARXIV-2605-23067 | arXiv:2605.23067v1 | paper-v1:2605.23067 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23067 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23067 | no |
| SF-2026-ARXIV-2605-23071 | arXiv:2605.23071v1 | paper-v1:2605.23071 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23071 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23071 | no |
| SF-2026-ARXIV-2605-23078 | arXiv:2605.23078v1 | paper-v1:2605.23078 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23078 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-23078 | no |
| SF-2026-ARXIV-2605-23080 | arXiv:2605.23080v1 | paper-v1:2605.23080 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23080 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-23080 | no |
| SF-2026-ARXIV-2605-23157 | arXiv:2605.23157v1 | paper-v1:2605.23157 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23157 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23157 | no |
| SF-2026-ARXIV-2605-23158 | arXiv:2605.23158v1 | paper-v1:2605.23158 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23158 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23158 | no |
| SF-2026-ARXIV-2605-23168 | arXiv:2605.23168v1 | paper-v1:2605.23168 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23168 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23168 | no |
| SF-2026-ARXIV-2605-23170 | arXiv:2605.23170v1 | paper-v1:2605.23170 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23170 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-23170 | no |
| SF-2026-ARXIV-2605-23196 | arXiv:2605.23196v1 | paper-v1:2605.23196 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23196 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23196 | no |
| SF-2026-ARXIV-2605-23200 | arXiv:2605.23200v1 | paper-v1:2605.23200 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23200 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23200 | no |
| SF-2026-ARXIV-2605-23215 | arXiv:2605.23215v1 | paper-v1:2605.23215 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23215 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23215 | no |
| SF-2026-ARXIV-2605-23218 | arXiv:2605.23218v1 | paper-v1:2605.23218 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23218 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23218 | no |
| SF-2026-ARXIV-2605-23220 | arXiv:2605.23220v1 | paper-v1:2605.23220 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23220 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23220 | no |
| SF-2026-ARXIV-2605-23258 | arXiv:2605.23258v1 | paper-v1:2605.23258 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23258 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23258 | no |
| SF-2026-ARXIV-2605-23262 | arXiv:2605.23262v1 | paper-v1:2605.23262 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23262 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23262 | no |
| SF-2026-ARXIV-2605-23294 | arXiv:2605.23294v1 | paper-v1:2605.23294 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23294 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23294 | no |
| SF-2026-ARXIV-2605-23296 | arXiv:2605.23296v1 | paper-v1:2605.23296 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23296 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-23296 | no |
| SF-2026-ARXIV-2605-23311 | arXiv:2605.23311v1 | paper-v1:2605.23311 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23311 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23311 | no |
| SF-2026-ARXIV-2605-23348 | arXiv:2605.23348v1 | paper-v1:2605.23348 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23348 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23348 | no |
| SF-2026-ARXIV-2605-23362 | arXiv:2605.23362v1 | paper-v1:2605.23362 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23362 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23362 | no |
| SF-2026-ARXIV-2605-23389 | arXiv:2605.23389v1 | paper-v1:2605.23389 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23389 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-23389 | no |
| SF-2026-ARXIV-2605-23414 | arXiv:2605.23414v1 | paper-v1:2605.23414 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23414 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23414 | no |
| SF-2026-ARXIV-2605-23454 | arXiv:2605.23454v1 | paper-v1:2605.23454 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23454 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23454 | no |
| SF-2026-ARXIV-2605-23464 | arXiv:2605.23464v1 | paper-v1:2605.23464 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23464 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23464 | no |
| SF-2026-ARXIV-2605-23493 | arXiv:2605.23493v1 | paper-v1:2605.23493 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23493 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23493 | no |
| SF-2026-ARXIV-2605-23574 | arXiv:2605.23574v1 | paper-v1:2605.23574 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23574 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23574 | no |
| SF-2026-ARXIV-2605-23590 | arXiv:2605.23590v1 | paper-v1:2605.23590 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23590 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23590 | no |
| SF-2026-ARXIV-2605-23628 | arXiv:2605.23628v1 | paper-v1:2605.23628 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23628 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23628 | no |
| SF-2026-ARXIV-2605-23640 | arXiv:2605.23640v1 | paper-v1:2605.23640 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23640 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23640 | no |
| SF-2026-ARXIV-2605-23657 | arXiv:2605.23657v1 | paper-v1:2605.23657 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23657 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23657 | no |
| SF-2026-ARXIV-2605-23701 | arXiv:2605.23701v1 | paper-v1:2605.23701 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23701 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23701 | no |
| SF-2026-ARXIV-2605-23723 | arXiv:2605.23723v1 | paper-v1:2605.23723 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23723 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23723 | no |
| SF-2026-ARXIV-2605-23764 | arXiv:2605.23764v1 | paper-v1:2605.23764 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23764 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23764 | no |
| SF-2026-ARXIV-2605-23856 | arXiv:2605.23856v1 | paper-v1:2605.23856 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23856 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23856 | no |
| SF-2026-ARXIV-2605-23893 | arXiv:2605.23893v1 | paper-v1:2605.23893 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23893 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2605-23893 | no |
| SF-2026-ARXIV-2605-23899 | arXiv:2605.23899v1 | paper-v1:2605.23899 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23899 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23899 | no |
| SF-2026-ARXIV-2605-23904 | arXiv:2605.23904v1 | paper-v1:2605.23904 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23904 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23904 | no |
| SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | arXiv:2605.22842v1 | paper-v1:2605.22842 | 2026-W22 | 2026-05-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-22850 | RP-f147eaf02fbb1f07 | deep | arXiv:2605.22850v1 | SRC-ARXIV@arXiv:2605.22850v1 | section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt) | Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only | Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup | papers/2026/05/_sources/daily-20260517/exact-review-batch-f.txt#sha256=b5d6a0a2fd67c424c789e8fdee75b6523c7473081588f5eee6a221ecc4fafaff; exact-v1 URL=https://arxiv.org/html/2605.22850v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-22850 | complete |
| SF-2026-ARXIV-2605-22863 | RP-cf5cd47f9c923eaf | deep | arXiv:2605.22863v1 | SRC-ARXIV@arXiv:2605.22863v1 | arXiv:2605.22863v1 HTML — §3 latent-cache communication interface | arXiv:2605.22863v1 HTML — §4 evaluation; Appendix C statistics | arXiv:2605.22863v1 HTML — §5 Limitations: checkpoint-specific retained layers | https://arxiv.org/html/2605.22863v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22863 | complete |
| SF-2026-ARXIV-2605-22866 | RP-2715d5653259d793 | deep | arXiv:2605.22866v1 | SRC-ARXIV@arXiv:2605.22866v1 | arXiv:2605.22866v1 HTML — §3 hierarchical online attribution | arXiv:2605.22866v1 HTML — §4 and Appendix A experiments | arXiv:2605.22866v1 HTML — §6 limitations and binary-outcome boundary | https://arxiv.org/html/2605.22866v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22866 | complete |
| SF-2026-ARXIV-2605-22868 | RP-d41dfe99a6de313e | deep | arXiv:2605.22868v1 | SRC-ARXIV@arXiv:2605.22868v1 | arXiv:2605.22868v1 HTML — §3 tri-stage near-sensor/fusion/edge control | arXiv:2605.22868v1 HTML — §4 quality–data–energy evaluation | arXiv:2605.22868v1 HTML — §5 Conclusion; dual-modality SynDrone boundary | https://arxiv.org/html/2605.22868v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22868 | complete |
| SF-2026-ARXIV-2605-22882 | RP-edf8a3836d174361 | deep | arXiv:2605.22882v1 | SRC-ARXIV@arXiv:2605.22882v1 | arXiv:2605.22882v1 HTML — §3.1 Problem Formulation; §3.3 Adaptive Inverse Dynamic System | arXiv:2605.22882v1 HTML — §4 Experiments; §Quantitative Experiment; §Qualitative Experiment | arXiv:2605.22882v1 HTML — §5 Conclusion | https://arxiv.org/html/2605.22882v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22882 | complete |
| SF-2026-ARXIV-2605-22883 | RP-200c8aca489405ce | deep | arXiv:2605.22883v1 | SRC-ARXIV@arXiv:2605.22883v1 | arXiv:2605.22883v1 HTML — §4 Energy-per-Successful-Goal Metric | arXiv:2605.22883v1 HTML — §8 Failure-Injection Experiments | arXiv:2605.22883v1 HTML — §10.1 Limitations | https://arxiv.org/html/2605.22883v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22883 | complete |
| SF-2026-ARXIV-2605-22884 | RP-3cfb78fecc04c716 | deep | arXiv:2605.22884v1 | SRC-ARXIV@arXiv:2605.22884v1 | arXiv:2605.22884v1 HTML — §KV cache systems and eviction.; §Training-side considerations.; §Other long-context methods. | arXiv:2605.22884v1 HTML — §4 Experiments; §4.1 Experimental Setup; §Results. | arXiv:2605.22884v1 HTML — §5 Discussion and Limitations; §6 Conclusion | https://arxiv.org/html/2605.22884v1; repository/immutable commit Not Disclosed unless exact-v1 states otherwise | claim:SF-2026-ARXIV-2605-22884 | complete |
| SF-2026-ARXIV-2605-22891 | RP-5a5c3f8c519adfd5 | deep | arXiv:2605.22891v1 | SRC-ARXIV@arXiv:2605.22891v1 | arXiv:2605.22891v1 HTML — §Current Methods; §Compared methods; §Compared methods | arXiv:2605.22891v1 HTML — §Pointwise Metrics Mislead: An Evaluation Protocol for Multimodal Inverse Problems; §Evaluation in Scientific Reconstruction; §Proper Scoring Rules, Calibration, and Evaluation Principles | arXiv:2605.22891v1 HTML — §3 Limitations of Pointwise Evaluation Metrics; §7 Discussion; §Limitations | https://arxiv.org/html/2605.22891v1; sha256:b227f5946cbe59caf4e48ec076f7bc9f7e2228b391b45a1c0e6f137d3f6b81d9 | claim:SF-2026-ARXIV-2605-22891 | complete |
| SF-2026-ARXIV-2605-22894 | RP-89f7b57ed9c31c19 | deep | arXiv:2605.22894v1 | SRC-ARXIV@arXiv:2605.22894v1 | arXiv:2605.22894v1 HTML — §SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-Based Humanoid Control; §3.1. Problem Formulation; §4. Methodology | arXiv:2605.22894v1 HTML — §5. Experiments; §5.1. Experiment Setup; §Evaluation Metrics and Training Details. | arXiv:2605.22894v1 HTML — §6. Conclusion | https://arxiv.org/html/2605.22894v1; sha256:04ae0c3d25d875182b84a81a6e2bb96265edd4e759ba4bebe802242348c2956a | claim:SF-2026-ARXIV-2605-22894 | complete |
| SF-2026-ARXIV-2605-22896 | RP-0575fae85e686803 | deep | arXiv:2605.22896v1 | SRC-ARXIV@arXiv:2605.22896v1 | arXiv:2605.22896v1 HTML — §3 Method; §3.1 Problem Formulation; §3.2 Framework Overview | arXiv:2605.22896v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Main Results | arXiv:2605.22896v1 HTML — §5 Conclusion; §Appendix C Failure Cases; §Appendix E Discussions | https://arxiv.org/html/2605.22896v1; sha256:e427d92157774def406513364ed34fb58802911433c29e3a59de4eaaa494fc31 | claim:SF-2026-ARXIV-2605-22896 | complete |
| SF-2026-ARXIV-2605-22905 | RP-8b7ae9b6661638fe | deep | arXiv:2605.22905v1 | SRC-ARXIV@arXiv:2605.22905v1 | arXiv:2605.22905v1 HTML — §3 Method; §3.4 Two-phase training schedule; §Training schedule and key hyperparameters. | arXiv:2605.22905v1 HTML — §4 Experiments; §4.1 Experimental setup; §Benchmarks and metrics. | arXiv:2605.22905v1 HTML — §Discussion.; §Discussion.; §6 Conclusion | https://arxiv.org/html/2605.22905v1; sha256:e5cec1be1abed98da562a5d395606cd40de16c10e10b001f75754aaca34aff72 | claim:SF-2026-ARXIV-2605-22905 | complete |
| SF-2026-ARXIV-2605-22949 | RP-735fb1981deaaece | deep | arXiv:2605.22949v1 | SRC-ARXIV@arXiv:2605.22949v1 | arXiv:2605.22949v1 HTML — §2.4 Trust and Reputation Systems; §3 Method; §3.1 Problem Formulation | arXiv:2605.22949v1 HTML — §5 Experimental Setup; §5.2 Benchmarks; §5.4 Evaluation Metrics | arXiv:2605.22949v1 HTML — §11 Discussion; §12 Conclusion | https://arxiv.org/html/2605.22949v1; sha256:45c7ee8cf423855ea4aaaff999d7e1b0c11e1527f126a5eef34e8a277094a09b | claim:SF-2026-ARXIV-2605-22949 | complete |
| SF-2026-ARXIV-2605-22984 | RP-0816e2ce734a1b4a | deep | arXiv:2605.22984v1 | SRC-ARXIV@arXiv:2605.22984v1 | arXiv:2605.22984v1 HTML — §3 Test-Time-Training Threat Models | arXiv:2605.22984v1 HTML — §4 Safety-Guardrail Evaluation | arXiv:2605.22984v1 HTML — §5 Limitations and Future Work | https://arxiv.org/html/2605.22984v1; sha256:6e88ca4e02bc5e5b6b94c201e9ee0a42f21bc3f62a7705115495b602a0666168 | claim:SF-2026-ARXIV-2605-22984 | complete |
| SF-2026-ARXIV-2605-23019 | RP-f8ad4c9ff0a48f0f | deep | arXiv:2605.23019v1 | SRC-ARXIV@arXiv:2605.23019v1 | arXiv:2605.23019v1 HTML — §3.2 PACE: A Two-Timescale Agentic Adaptation Framework; §A.5 Algorithm Walkthrough | arXiv:2605.23019v1 HTML — §4 Experiment; §4.2 Quantitative Results; §4.3 Ablation Study and Parameter Sensitivity Analysis | arXiv:2605.23019v1 HTML — §4.4 Failure Mode Shift Across Evolution Phases; §5 Conclusion; §A.8.1 Failure Taxonomy | https://arxiv.org/html/2605.23019v1; sha256:7866d765a2f59b22a672d399c21bfad6ecbf672813aab4dc0b52ed26bf9bf2b0 | claim:SF-2026-ARXIV-2605-23019 | complete |
| SF-2026-ARXIV-2605-23055 | RP-f5b0cf52ee708c4f | deep | arXiv:2605.23055v1 | SRC-ARXIV@arXiv:2605.23055v1 | arXiv:2605.23055v1 HTML — §Appendix B Setup, Method Comparison, and Justification; §Alternative detection method prompts.; §Target model system prompts. | arXiv:2605.23055v1 HTML — §Decomposing and Measuring Evaluation Awareness; §2 Evaluation Awareness: From Psychology to LLMs; §2.1 Definition of Evaluation Awareness in LLMs | arXiv:2605.23055v1 HTML — §4 Limitations of Existing Benchmarks for Studying Evaluation Awareness; §6 Discussion, Limitation, and Safety Implication; §Appendix A Definition, Related Work, and Further Discussions | https://arxiv.org/html/2605.23055v1; sha256:85af8e19b43ddfdcf2ffc328b347358b1ec2b97976f0c06c8c53e787b8ae6988 | claim:SF-2026-ARXIV-2605-23055 | complete |
| SF-2026-ARXIV-2605-23057 | RP-3d1f26460002fe88 | deep | arXiv:2605.23057v1 | SRC-ARXIV@arXiv:2605.23057v1 | arXiv:2605.23057v1 HTML — §3 ModeSwitch Phase-Aware Controller | arXiv:2605.23057v1 HTML — §4 Single-GPU Evaluation | arXiv:2605.23057v1 HTML — §5 Conclusion and single-GPU/workload boundary | https://arxiv.org/html/2605.23057v1; sha256:95caca7cb404f405f3c3753b33da60deeb1cb4664fd64c61feea803cedbc03af | claim:SF-2026-ARXIV-2605-23057 | complete |
| SF-2026-ARXIV-2605-23058 | RP-6aac9798dc48a487 | deep | arXiv:2605.23058v1 | SRC-ARXIV@arXiv:2605.23058v1 | arXiv:2605.23058v1 HTML — §A measurement substrate for agentic Kubernetes operations Methodology and a case study in retrieval-compounding falsification; §2.2 Agentic systems evaluation; §3.3 Framework error vs reasoning error | arXiv:2605.23058v1 HTML — §2.2 Agentic systems evaluation; §2.5 Why fixed-ground-truth benchmarks cannot catch these confounds; §4.1 The pgvector ivfflat index returning sporadic empty result sets | arXiv:2605.23058v1 HTML — §6 Discussion: semantic vs mechanistic retrieval; §7 Limitations and scope; §8 Conclusion | https://arxiv.org/html/2605.23058v1; sha256:960691f4efbd1ed096ef43fde4536be3088667811a183cc51ccc41b1b530fbb8 | claim:SF-2026-ARXIV-2605-23058 | complete |
| SF-2026-ARXIV-2605-23066 | RP-09e149d08a7bf8dc | deep | arXiv:2605.23066v1 | SRC-ARXIV@arXiv:2605.23066v1 | arXiv:2605.23066v1 HTML — §3 Orbax Distributed Checkpointing Design | arXiv:2605.23066v1 HTML — §5 Scale Evaluation | arXiv:2605.23066v1 HTML — §6 Multi-controller and simulation limitations | https://arxiv.org/html/2605.23066v1; sha256:900ea414a1863deafa360f1688c1844e35683b8d8aea15263e3894d2cee9cdbf | claim:SF-2026-ARXIV-2605-23066 | complete |
| SF-2026-ARXIV-2605-23067 | RP-550615f9c7658414 | deep | arXiv:2605.23067v1 | SRC-ARXIV@arXiv:2605.23067v1 | arXiv:2605.23067v1 HTML — §What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA; §2.3 Curriculum Learning for RL-Based LLM Training; §3 Method | arXiv:2605.23067v1 HTML — §2.2 Benchmarks for Long-Term Memory; §3.5 Evaluation; §4 Results | arXiv:2605.23067v1 HTML — §6 Limitations and Future Work; §7 Conclusion | https://arxiv.org/html/2605.23067v1; sha256:184f58bce1c356a44c5a39bea8f8373790c34adefb14263713f1ff95eae95f9f | claim:SF-2026-ARXIV-2605-23067 | complete |
| SF-2026-ARXIV-2605-23071 | RP-890ad122e82086e2 | deep | arXiv:2605.23071v1 | SRC-ARXIV@arXiv:2605.23071v1 | arXiv:2605.23071v1 HTML — §3 Cost–Performance Frontier for Context Strategies | arXiv:2605.23071v1 HTML — §4 Comparative Evaluation | arXiv:2605.23071v1 HTML — §5 Discussion and oracle/synthetic-boundary | https://arxiv.org/html/2605.23071v1; sha256:6d46f99b587dde04721d311930533e9b11fdac299a7d67f24e66482f9160d313 | claim:SF-2026-ARXIV-2605-23071 | complete |
| SF-2026-ARXIV-2605-23078 | RP-a0e2ba25f098487a | deep | arXiv:2605.23078v1 | SRC-ARXIV@arXiv:2605.23078v1 | arXiv:2605.23078v1 HTML — §4 Method; §5.1 Comparison of MoE-LLM Quantization Methods; §Appendix B Comparison with State-of-the-Art Methods | arXiv:2605.23078v1 HTML — §Analysis of Quantization Error.; §5 Experiments; §5.2 Quantization Overhead Analysis | arXiv:2605.23078v1 HTML — §7 Limitations; §8 Conclusion | https://arxiv.org/html/2605.23078v1; sha256:3da7934f8b6adff187ab04557e221638cc7738b112eaa55f98f2fc5cfabb4e2b | claim:SF-2026-ARXIV-2605-23078 | complete |
| SF-2026-ARXIV-2605-23080 | RP-398864d838f2353f | deep | arXiv:2605.23080v1 | SRC-ARXIV@arXiv:2605.23080v1 | arXiv:2605.23080v1 HTML — §3 Attribution Contract | arXiv:2605.23080v1 HTML — §5 Generative-LM Evaluation | arXiv:2605.23080v1 HTML — §6 Discussion and attribution-scope boundary | https://arxiv.org/html/2605.23080v1; sha256:ff5eb8b1e622cd1a1b7dae83beddeb5b0bbfd3fa522b2f75a25a6823951b1e00 | claim:SF-2026-ARXIV-2605-23080 | complete |
| SF-2026-ARXIV-2605-23157 | RP-a5e7eb75c98b990e | deep | arXiv:2605.23157v1 | SRC-ARXIV@arXiv:2605.23157v1 | https://arxiv.org/html/2605.23157v1 — §3 Study Design; §3.1–§3.4 language × modality threat matrix | https://arxiv.org/html/2605.23157v1 — §4 Results; mixed-effects and matched-annotator evaluation | https://arxiv.org/html/2605.23157v1 — §7 Limitations; four-model/two-language scope | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23157 | complete |
| SF-2026-ARXIV-2605-23158 | RP-b2c602abcd2fe586 | deep | arXiv:2605.23158v1 | SRC-ARXIV@arXiv:2605.23158v1 | https://arxiv.org/html/2605.23158v1 — §3 Split Inference Protocol; §4.1–§4.2 Threat Model and ActInv | https://arxiv.org/html/2605.23158v1 — §4.3–§4.4 Evaluation | https://arxiv.org/html/2605.23158v1 — §5.3 Potential Defenses and split-point boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23158 | complete |
| SF-2026-ARXIV-2605-23168 | RP-2c31431371f1ac81 | deep | arXiv:2605.23168v1 | SRC-ARXIV@arXiv:2605.23168v1 | https://arxiv.org/html/2605.23168v1 — §3 PoisonForge threat model and parameterized benchmark | https://arxiv.org/html/2605.23168v1 — §4–§5 twelve-model poisoning evaluation | https://arxiv.org/html/2605.23168v1 — §6 Limitations; instruction-tuning and tested poison-budget boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23168 | complete |
| SF-2026-ARXIV-2605-23170 | RP-5d3695102d13073c | deep | arXiv:2605.23170v1 | SRC-ARXIV@arXiv:2605.23170v1 | https://arxiv.org/html/2605.23170v1 — §3 Context Rot Evaluation; controlled position/content/length factors | https://arxiv.org/html/2605.23170v1 — §4 Evaluation across nine models and two reasoning tasks | https://arxiv.org/html/2605.23170v1 — §7 Limitations; benchmark/task/context-family boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23170 | complete |
| SF-2026-ARXIV-2605-23196 | RP-b858c1b78baceb05 | deep | arXiv:2605.23196v1 | SRC-ARXIV@arXiv:2605.23196v1 | https://arxiv.org/html/2605.23196v1 — §3 Prompt-Overflow Threat Model | https://arxiv.org/html/2605.23196v1 — §4 Guardrail/Model Evaluation | https://arxiv.org/html/2605.23196v1 — §5 Discussion and tokenizer/context-boundary limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23196 | complete |
| SF-2026-ARXIV-2605-23200 | RP-da06ef546f54d6ce | deep | arXiv:2605.23200v1 | SRC-ARXIV@arXiv:2605.23200v1 | https://arxiv.org/html/2605.23200v1 — §3 Adaptive Mass-Segmented KV Compression | https://arxiv.org/html/2605.23200v1 — §4 Long-Form Reasoning Evaluation | https://arxiv.org/html/2605.23200v1 — §5 Conclusion and evaluated-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23200 | complete |
| SF-2026-ARXIV-2605-23215 | RP-cb8c0cd9246d1439 | deep | arXiv:2605.23215v1 | SRC-ARXIV@arXiv:2605.23215v1 | https://arxiv.org/html/2605.23215v1 — §3 FastKernels Production Benchmark Contract | https://arxiv.org/html/2605.23215v1 — §5 Kernel-Generation Evaluation | https://arxiv.org/html/2605.23215v1 — §6 Discussion and production-workload coverage limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23215 | complete |
| SF-2026-ARXIV-2605-23218 | RP-0b7b32429b301d1e | deep | arXiv:2605.23218v1 | SRC-ARXIV@arXiv:2605.23218v1 | https://arxiv.org/html/2605.23218v1 — §3 Foundation Protocol Coordination Layer | https://arxiv.org/html/2605.23218v1 — §5 Multi-Agent Evaluation | https://arxiv.org/html/2605.23218v1 — §6 Limitations and governance-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23218 | complete |
| SF-2026-ARXIV-2605-23220 | RP-3fd9d54eb7ed1280 | deep | arXiv:2605.23220v1 | SRC-ARXIV@arXiv:2605.23220v1 | https://arxiv.org/html/2605.23220v1 — §3 WMAttack Automated Attack Search | https://arxiv.org/html/2605.23220v1 — §4 World-Model Agent Evaluation | https://arxiv.org/html/2605.23220v1 — §5 Limitations and tested-environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23220 | complete |
| SF-2026-ARXIV-2605-23258 | RP-7e8ee0e18e9fbabb | deep | arXiv:2605.23258v1 | SRC-ARXIV@arXiv:2605.23258v1 | https://arxiv.org/html/2605.23258v1 — §3 Eviction-Aware KV Compression Plug-in | https://arxiv.org/html/2605.23258v1 — §4 Evaluation | https://arxiv.org/html/2605.23258v1 — §5 Conclusion and eviction-policy boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23258 | complete |
| SF-2026-ARXIV-2605-23262 | RP-fed5c51d38199cf0 | deep | arXiv:2605.23262v1 | SRC-ARXIV@arXiv:2605.23262v1 | https://arxiv.org/html/2605.23262v1 — §2–§4 work-centered benchmark representation | https://arxiv.org/html/2605.23262v1 — §5 worked benchmark comparisons | https://arxiv.org/html/2605.23262v1 — §6 Discussion; conceptual representation does not prove predictive validity | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23262 | complete |
| SF-2026-ARXIV-2605-23294 | RP-6dde5b87016a8054 | deep | arXiv:2605.23294v1 | SRC-ARXIV@arXiv:2605.23294v1 | https://arxiv.org/html/2605.23294v1 — §III NASiC CAM-selected multibit CIM architecture | https://arxiv.org/html/2605.23294v1 — §IV–§V architecture/model evaluation | https://arxiv.org/html/2605.23294v1 — §VI Discussion; simulated 3D-NAND/device-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23294 | complete |
| SF-2026-ARXIV-2605-23296 | RP-425574fcac35b682 | deep | arXiv:2605.23296v1 | SRC-ARXIV@arXiv:2605.23296v1 | https://arxiv.org/html/2605.23296v1 — §3 Parallel Context Compaction Runtime | https://arxiv.org/html/2605.23296v1 — §5 Long-Horizon Agent-Serving Evaluation | https://arxiv.org/html/2605.23296v1 — §6 Discussion and compaction-fidelity boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23296 | complete |
| SF-2026-ARXIV-2605-23311 | RP-6362c6ec2344c81d | deep | arXiv:2605.23311v1 | SRC-ARXIV@arXiv:2605.23311v1 | https://arxiv.org/html/2605.23311v1 — §3 DART Semantic-Recoverability Contract | https://arxiv.org/html/2605.23311v1 — §5 Structured-Tool Agent Evaluation | https://arxiv.org/html/2605.23311v1 — §6 Limitations and tool-schema boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23311 | complete |
| SF-2026-ARXIV-2605-23348 | RP-d67c7fcd55d6e402 | deep | arXiv:2605.23348v1 | SRC-ARXIV@arXiv:2605.23348v1 | https://arxiv.org/html/2605.23348v1 — §3 XWind Cross-Site Routing Controller | https://arxiv.org/html/2605.23348v1 — §5 Renewable-Site Serving Evaluation | https://arxiv.org/html/2605.23348v1 — §6 Limitations and forecast/topology boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23348 | complete |
| SF-2026-ARXIV-2605-23362 | RP-3286bf917956c518 | deep | arXiv:2605.23362v1 | SRC-ARXIV@arXiv:2605.23362v1 | https://arxiv.org/html/2605.23362v1 — §2–§4 budgeted heteroskedastic multi-judge estimation | https://arxiv.org/html/2605.23362v1 — §5 theory and empirical allocation evaluation | https://arxiv.org/html/2605.23362v1 — §6 Discussion; known-cost/bounded-score assumptions | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23362 | complete |
| SF-2026-ARXIV-2605-23389 | RP-d31f7b43f0ecb7ff | deep | arXiv:2605.23389v1 | SRC-ARXIV@arXiv:2605.23389v1 | https://arxiv.org/html/2605.23389v1 — §3 AlignedServe Prefix-Aware Batching | https://arxiv.org/html/2605.23389v1 — §5 Throughput/Compute Evaluation | https://arxiv.org/html/2605.23389v1 — §6 Conclusion and workload boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23389 | complete |
| SF-2026-ARXIV-2605-23414 | RP-550125b9681b344c | deep | arXiv:2605.23414v1 | SRC-ARXIV@arXiv:2605.23414v1 | https://arxiv.org/html/2605.23414v1 — §3 Epistemic-Calibration Model for Multi-Agent Planning | https://arxiv.org/html/2605.23414v1 — §4 Evaluation | https://arxiv.org/html/2605.23414v1 — §5 Limitations and planning/execution boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23414 | complete |
| SF-2026-ARXIV-2605-23454 | RP-0507968efac4b381 | deep | arXiv:2605.23454v1 | SRC-ARXIV@arXiv:2605.23454v1 | https://arxiv.org/html/2605.23454v1 — §3 ARES automatic rubric synthesis and reward construction | https://arxiv.org/html/2605.23454v1 — §4 and Appendix F evaluation | https://arxiv.org/html/2605.23454v1 — Appendix A Limitations; generated-rubric correctness boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23454 | complete |
| SF-2026-ARXIV-2605-23464 | RP-192bc644aad84ff7 | deep | arXiv:2605.23464v1 | SRC-ARXIV@arXiv:2605.23464v1 | https://arxiv.org/html/2605.23464v1 — §3 Unextractable Protocol Model Construction | https://arxiv.org/html/2605.23464v1 — §5 Collaborative Training/Inference Evaluation | https://arxiv.org/html/2605.23464v1 — §6 Security Assumptions and protocol limitations | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23464 | complete |
| SF-2026-ARXIV-2605-23493 | RP-048d9637fe33d612 | deep | arXiv:2605.23493v1 | SRC-ARXIV@arXiv:2605.23493v1 | https://arxiv.org/html/2605.23493v1 — §3 EDGE-OPD evidence-guided on-policy distillation | https://arxiv.org/html/2605.23493v1 — §4–§5 experiments and diagnostics | https://arxiv.org/html/2605.23493v1 — Appendix A.10 Limitations; teacher/evidence/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23493 | complete |
| SF-2026-ARXIV-2605-23574 | RP-5c316d8181d387b2 | deep | arXiv:2605.23574v1 | SRC-ARXIV@arXiv:2605.23574v1 | https://arxiv.org/html/2605.23574v1 — §3 Quantitative Goal-Persistence Contract | https://arxiv.org/html/2605.23574v1 — §5 Long-Horizon Agent Evaluation | https://arxiv.org/html/2605.23574v1 — §6 Limitations and task-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23574 | complete |
| SF-2026-ARXIV-2605-23590 | RP-547a40f059f156d0 | deep | arXiv:2605.23590v1 | SRC-ARXIV@arXiv:2605.23590v1 | https://arxiv.org/html/2605.23590v1 — §2–§3 Co-ReAct step-level rubric and control loop | https://arxiv.org/html/2605.23590v1 — §4–§5 agent evaluation | https://arxiv.org/html/2605.23590v1 — §6 Limitations; rubric and environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23590 | complete |
| SF-2026-ARXIV-2605-23628 | RP-1523ed940f94db13 | deep | arXiv:2605.23628v1 | SRC-ARXIV@arXiv:2605.23628v1 | https://arxiv.org/html/2605.23628v1 — §3 Social-Choice Leaderboard Model | https://arxiv.org/html/2605.23628v1 — §4 Benchmark-Rigging Analysis | https://arxiv.org/html/2605.23628v1 — §5 Discussion and scoring-rule assumptions | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23628 | complete |
| SF-2026-ARXIV-2605-23640 | RP-b9d297fc63bc2e63 | deep | arXiv:2605.23640v1 | SRC-ARXIV@arXiv:2605.23640v1 | https://arxiv.org/html/2605.23640v1 — §3 CachePrune Privacy-Aware KV Sharing | https://arxiv.org/html/2605.23640v1 — §5 Efficiency/Leakage Evaluation | https://arxiv.org/html/2605.23640v1 — §6 Limitations and attacker/model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23640 | complete |
| SF-2026-ARXIV-2605-23657 | RP-6ec64a2c7768b800 | deep | arXiv:2605.23657v1 | SRC-ARXIV@arXiv:2605.23657v1 | https://arxiv.org/html/2605.23657v1 — §3 OpenSkillEval Audit Pipeline | https://arxiv.org/html/2605.23657v1 — §4 Open-Skill Ecosystem Evaluation | https://arxiv.org/html/2605.23657v1 — §5 Limitations and registry-coverage boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23657 | complete |
| SF-2026-ARXIV-2605-23701 | RP-76760412a47fb37e | deep | arXiv:2605.23701v1 | SRC-ARXIV@arXiv:2605.23701v1 | https://arxiv.org/html/2605.23701v1 — §3 Intervention-Based Weak-Label Audit | https://arxiv.org/html/2605.23701v1 — §4 Controlled Evaluation | https://arxiv.org/html/2605.23701v1 — §5 Discussion and intervention-identifiability limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23701 | complete |
| SF-2026-ARXIV-2605-23723 | RP-6b7ff0f74ca2d717 | deep | arXiv:2605.23723v1 | SRC-ARXIV@arXiv:2605.23723v1 | https://arxiv.org/html/2605.23723v1 — §3 MemAudit Causal/Structural Audit | https://arxiv.org/html/2605.23723v1 — §5 Poisoned-Memory Evaluation | https://arxiv.org/html/2605.23723v1 — §6 Limitations and post-hoc-detection boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23723 | complete |
| SF-2026-ARXIV-2605-23764 | RP-613534380557f522 | deep | arXiv:2605.23764v1 | SRC-ARXIV@arXiv:2605.23764v1 | https://arxiv.org/html/2605.23764v1 — §3 HyperParallel-MoE Interleaved Scheduling | https://arxiv.org/html/2605.23764v1 — §5 Ascend-NPU Training Evaluation | https://arxiv.org/html/2605.23764v1 — §6 Conclusion and hardware/topology boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23764 | complete |
| SF-2026-ARXIV-2605-23856 | RP-63fb361e8b1290df | deep | arXiv:2605.23856v1 | SRC-ARXIV@arXiv:2605.23856v1 | https://arxiv.org/html/2605.23856v1 — §3 Point-Tracking World-Action Model | https://arxiv.org/html/2605.23856v1 — §4 Evaluation | https://arxiv.org/html/2605.23856v1 — §5 Limitations and observed-environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23856 | complete |
| SF-2026-ARXIV-2605-23893 | RP-ff7583edfd2016e5 | deep | arXiv:2605.23893v1 | SRC-ARXIV@arXiv:2605.23893v1 | https://arxiv.org/html/2605.23893v1 — §3 Complete-μE MoE Parameterization | https://arxiv.org/html/2605.23893v1 — §5 Hyperparameter-Transfer/Scaling Evaluation | https://arxiv.org/html/2605.23893v1 — §6 Limitations and tested-scale boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23893 | complete |
| SF-2026-ARXIV-2605-23899 | RP-3e95e4e8b2a46779 | deep | arXiv:2605.23899v1 | SRC-ARXIV@arXiv:2605.23899v1 | https://arxiv.org/html/2605.23899v1 — §3 Model-Generated Skill Pipeline | https://arxiv.org/html/2605.23899v1 — §4 Skill-Use Evaluation | https://arxiv.org/html/2605.23899v1 — §5 Limitations and model/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23899 | complete |
| SF-2026-ARXIV-2605-23904 | RP-557190908b08e8d0 | deep | arXiv:2605.23904v1 | SRC-ARXIV@arXiv:2605.23904v1 | https://arxiv.org/html/2605.23904v1 — §3 SkillOpt Executive Strategy | https://arxiv.org/html/2605.23904v1 — §5 Self-Evolving Agent Evaluation | https://arxiv.org/html/2605.23904v1 — §6 Limitations and library-drift boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23904 | complete |
| SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | RP-c3cf139b02dad5f5 | deep | arXiv:2605.22842v1 | SRC-ARXIV@arXiv:2605.22842v1 | arXiv:2605.22842v1 HTML — §3 memory-poisoning attribution-gap threat model | arXiv:2605.22842v1 — §4 attack/mitigation evaluation | arXiv:2605.22842v1 — §5 limitations: memory backend, attacker and detector scope | arXiv:2605.22842v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-22850:start -->
#### ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse

问题与机制：ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse 提出的具体变化是：We propose ObjectCache, which co-designs the storage protocol and transfer schedule so that the storage server delivers KV cache data in the order the GPU consumes it, overlapping data transfer with compute across concurrent requests. 摘要中的长期系统挑战为：prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.”暂不作为最终证据。

Evaluation contract：Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.

Evidence locators：Method=`section Section identity in frozen exact-v1 receipt (§Section identity in frozen exact-v1 receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in frozen receipt; disclosed abstract/body result only`；Counterevidence=`Not Disclosed — no dedicated limitations heading; claim bounded to disclosed exact-v1 setup`。

Trade-off / failure：新增 controller、metadata、verification、communication 或 runtime state 都带来成本；只在 exact-v1 披露 workload/evaluator 内成立，未披露的硬件、精度、长度、batch、并发、SLO、seed 与 artifact commit 为 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-22850:start -->只支持 exact-v1 披露设置中的机制与结果；旧路径在新增 owner/证据/控制责任不成立时继续共存。<!-- claim:SF-2026-ARXIV-2605-22850:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-22850:end -->

<!-- review:SF-2026-ARXIV-2605-22863:start -->
#### Latent Cache Flow: Model-to-Model Communication Without Text

**问题与机制。** We introduce Latent Cache Flow (LCF). 系统 owner=`AGENT-MULTI-AGENT`。

**Exact-v1。** Method=`§3 latent-cache communication interface`；Evaluation=`§4 evaluation; Appendix C statistics`；Limitations/Counterevidence=`§5 Limitations: checkpoint-specific retained layers`。

<!-- claim:SF-2026-ARXIV-2605-22863:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22863:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22863:end -->

<!-- review:SF-2026-ARXIV-2605-22866:start -->
#### BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems

**问题与机制。** We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 hierarchical online attribution`；Evaluation=`§4 and Appendix A experiments`；Limitations/Counterevidence=`§6 limitations and binary-outcome boundary`。

<!-- claim:SF-2026-ARXIV-2605-22866:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22866:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22866:end -->

<!-- review:SF-2026-ARXIV-2605-22868:start -->
#### FusionSense: Tri-Stage Near-Sensor Learning for Runtime-Adaptive Multimodal Edge Intelligence

**问题与机制。** We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems. 系统 owner=`PLATFORM-PRODUCTION`。

**Exact-v1。** Method=`§3 tri-stage near-sensor/fusion/edge control`；Evaluation=`§4 quality–data–energy evaluation`；Limitations/Counterevidence=`§5 Conclusion; dual-modality SynDrone boundary`。

<!-- claim:SF-2026-ARXIV-2605-22868:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22868:end -->

Books Decision=`Structural Candidate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22868:end -->

<!-- review:SF-2026-ARXIV-2605-22882:start -->
#### GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation

**问题与机制。** We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training. 系统 owner=`MULTIMODAL-WORLD-MODELS`。

**Exact-v1。** Method=`§3.1 Problem Formulation; §3.3 Adaptive Inverse Dynamic System`；Evaluation=`§4 Experiments; §Quantitative Experiment; §Qualitative Experiment`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-22882:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22882:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22882:end -->

<!-- review:SF-2026-ARXIV-2605-22883:start -->
#### Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems

**问题与机制。** We present A-LEMS (Agentic LLM Energy Measurement System), a cross-layer measurement framework that redefines the unit of AI energy accounting from energy per inference to Energy per Successful Goal (EpG). 系统 owner=`PLATFORM-COST`。

**Exact-v1。** Method=`§4 Energy-per-Successful-Goal Metric`；Evaluation=`§8 Failure-Injection Experiments`；Limitations/Counterevidence=`§10.1 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-22883:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22883:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22883:end -->

<!-- review:SF-2026-ARXIV-2605-22884:start -->
#### Tensor Cache: Eviction-conditioned Associative Memory for Transformers

**问题与机制。** We introduce \emph{Tensor Cache}, a two-level cache that pairs sliding-window softmax attention as a first-level cache (L1) with a fixed-size outer-product fast-weight memory as a second-level cache (L2) fed by KV pairs evicted from the window. 系统 owner=`INFER-KV-CACHE`。

**Exact-v1。** Method=`§KV cache systems and eviction.; §Training-side considerations.; §Other long-context methods.`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §Results.`；Limitations/Counterevidence=`§5 Discussion and Limitations; §6 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-22884:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22884:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22884:end -->

<!-- review:SF-2026-ARXIV-2605-22891:start -->
#### Pointwise Metrics Mislead: An Evaluation Protocol for Multimodal Inverse Problems

**问题与机制。** Evaluation in scientific reconstruction is dominated by pointwise metrics - RMSE, MAE, per-event resolution - under the implicit assumption that lower error means better reconstruction. We show that this assumption fails structurally for inverse problems with multimodal posteriors. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§Current Methods; §Compared methods; §Compared methods`；Evaluation=`§Pointwise Metrics Mislead: An Evaluation Protocol for Multimodal Inverse Problems; §Evaluation in Scientific Reconstruction; §Proper Scoring Rules, Calibration, and Evaluation Principles`；Limitations/Counterevidence=`§3 Limitations of Pointwise Evaluation Metrics; §7 Discussion; §Limitations`；正文 sha256=`b227f5946cbe59caf4e48ec076f7bc9f7e2228b391b45a1c0e6f137d3f6b81d9`。

<!-- claim:SF-2026-ARXIV-2605-22891:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22891:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22891:end -->

<!-- review:SF-2026-ARXIV-2605-22894:start -->
#### SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-based Humanoid Control

**问题与机制。** Controlling physics-based humanoids from natural-language instructions is a critical step toward general-purpose embodied agents. We propose SCRIPT, a scalable diffusion policy with a multi-stage training framework for language-driven physics-based humanoid control. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§SCRIPT: Scalable Diffusion Policy with Multi-stage Training for Language-driven Physics-Based Humanoid Control; §3.1. Problem Formulation; §4. Methodology`；Evaluation=`§5. Experiments; §5.1. Experiment Setup; §Evaluation Metrics and Training Details.`；Limitations/Counterevidence=`§6. Conclusion`；正文 sha256=`04ae0c3d25d875182b84a81a6e2bb96265edd4e759ba4bebe802242348c2956a`。

<!-- claim:SF-2026-ARXIV-2605-22894:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22894:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22894:end -->

<!-- review:SF-2026-ARXIV-2605-22896:start -->
#### Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models

**问题与机制。** Vision-Language-Action (VLA) models have emerged as a promising paradigm for robotic manipulation by leveraging pre-trained vision-language representations. We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks. 系统 owner=`MULTIMODAL-EMBODIED-VLA`。

**Exact-v1。** Method=`§3 Method; §3.1 Problem Formulation; §3.2 Framework Overview`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Main Results`；Limitations/Counterevidence=`§5 Conclusion; §Appendix C Failure Cases; §Appendix E Discussions`；正文 sha256=`e427d92157774def406513364ed34fb58802911433c29e3a59de4eaaa494fc31`。

<!-- claim:SF-2026-ARXIV-2605-22896:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22896:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22896:end -->

<!-- review:SF-2026-ARXIV-2605-22905:start -->
#### EVE-Agent: Evidence-Verifiable Self-Evolving Agents

**问题与机制。** Self-evolving agents should not train on examples they cannot justify. We argue that evidence verifiability is a prerequisite for trustworthy self-evolution in search agents: each generated instance should include not only an answer but also a source-grounded span whose contribution to that answer can be measured. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3 Method; §3.4 Two-phase training schedule; §Training schedule and key hyperparameters.`；Evaluation=`§4 Experiments; §4.1 Experimental setup; §Benchmarks and metrics.`；Limitations/Counterevidence=`§Discussion.; §Discussion.; §6 Conclusion`；正文 sha256=`e5cec1be1abed98da562a5d395606cd40de16c10e10b001f75754aaca34aff72`。

<!-- claim:SF-2026-ARXIV-2605-22905:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22905:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22905:end -->

<!-- review:SF-2026-ARXIV-2605-22949:start -->
#### MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination

**问题与机制。** Foundation-model pools are increasingly used as black-box responders in coordinated systems where a coordinator must decide which response to trust. Raw self-reported confidence is the natural signal, but is not comparable across models and becomes stale under distribution shift when corrected only at design time. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2.4 Trust and Reputation Systems; §3 Method; §3.1 Problem Formulation`；Evaluation=`§5 Experimental Setup; §5.2 Benchmarks; §5.4 Evaluation Metrics`；Limitations/Counterevidence=`§11 Discussion; §12 Conclusion`；正文 sha256=`45c7ee8cf423855ea4aaaff999d7e1b0c11e1527f126a5eef34e8a277094a09b`。

<!-- claim:SF-2026-ARXIV-2605-22949:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22949:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22949:end -->

<!-- review:SF-2026-ARXIV-2605-22984:start -->
#### Test-Time Training Undermines Safety Guardrails

**问题与机制。** Test-Time Training (TTT) is an emerging paradigm that enables models to adapt their parameters during inference, improving performance on tasks such as few-shot learning, retrieval-augmented generation, and complex reasoning. We identify three threat models for TTT and demonstrate how attackers can leverage them to bypass safety filters. 系统 owner=`PLATFORM-SECURITY`。

**Exact-v1。** Method=`§3 Test-Time-Training Threat Models`；Evaluation=`§4 Safety-Guardrail Evaluation`；Limitations/Counterevidence=`§5 Limitations and Future Work`；正文 sha256=`6e88ca4e02bc5e5b6b94c201e9ee0a42f21bc3f62a7705115495b602a0666168`。

<!-- claim:SF-2026-ARXIV-2605-22984:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-22984:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-22984:end -->

<!-- review:SF-2026-ARXIV-2605-23019:start -->
#### PACE: Two-Timescale Self-Evolution for Small Language Model Agents

**问题与机制。** Deploying language-model agents in production often requires substantial compute and human effort to tune prompts, parsers, validators, and other components of the agent pipeline. Self-evolution offers a promising alternative, but most existing frameworks assume access to frontier models that can reliably diagnose failures, propose revisions, and judge their own updates. 系统 owner=`AGENT-PLATFORM`。

**Exact-v1。** Method=`§3.2 PACE: A Two-Timescale Agentic Adaptation Framework; §A.5 Algorithm Walkthrough`；Evaluation=`§4 Experiment; §4.2 Quantitative Results; §4.3 Ablation Study and Parameter Sensitivity Analysis`；Limitations/Counterevidence=`§4.4 Failure Mode Shift Across Evolution Phases; §5 Conclusion; §A.8.1 Failure Taxonomy`；正文 sha256=`7866d765a2f59b22a672d399c21bfad6ecbf672813aab4dc0b52ed26bf9bf2b0`。

<!-- claim:SF-2026-ARXIV-2605-23019:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23019:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23019:end -->

<!-- review:SF-2026-ARXIV-2605-23055:start -->
#### Decomposing and Measuring Evaluation Awareness

**问题与机制。** Frontier language models sometimes recognize that they are being evaluated and adjust their behavior, undermining validity of benchmark results. We operationalize the environment component through eight categorized trigger factors, such as placeholder entities and grading-style output formats, and study recognition and behavior through chain-of-thought monitoring. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§Appendix B Setup, Method Comparison, and Justification; §Alternative detection method prompts.; §Target model system prompts.`；Evaluation=`§Decomposing and Measuring Evaluation Awareness; §2 Evaluation Awareness: From Psychology to LLMs; §2.1 Definition of Evaluation Awareness in LLMs`；Limitations/Counterevidence=`§4 Limitations of Existing Benchmarks for Studying Evaluation Awareness; §6 Discussion, Limitation, and Safety Implication; §Appendix A Definition, Related Work, and Further Discussions`；正文 sha256=`85af8e19b43ddfdcf2ffc328b347358b1ec2b97976f0c06c8c53e787b8ae6988`。

<!-- claim:SF-2026-ARXIV-2605-23055:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23055:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23055:end -->

<!-- review:SF-2026-ARXIV-2605-23057:start -->
#### RequestRouter: Request-Boundary Routing for Efficient Single-GPU LLM Inference

**问题与机制。** RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference. RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§3 ModeSwitch Phase-Aware Controller`；Evaluation=`§4 Single-GPU Evaluation`；Limitations/Counterevidence=`§5 Conclusion and single-GPU/workload boundary`；正文 sha256=`95caca7cb404f405f3c3753b33da60deeb1cb4664fd64c61feea803cedbc03af`。

<!-- claim:SF-2026-ARXIV-2605-23057:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23057:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23057:end -->

<!-- review:SF-2026-ARXIV-2605-23058:start -->
#### A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification

**问题与机制。** Empirical claims about autonomous Kubernetes operations agents are largely unfalsifiable. We present agent-breakage, a closed-loop measurement framework that injects faults into a target Kubernetes cluster, observes how an autonomous agent responds, scores the response on four axes against ground truth, and accumulates outcome-labeled (state, action, outcome) tuples. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§A measurement substrate for agentic Kubernetes operations Methodology and a case study in retrieval-compounding falsification; §2.2 Agentic systems evaluation; §3.3 Framework error vs reasoning error`；Evaluation=`§2.2 Agentic systems evaluation; §2.5 Why fixed-ground-truth benchmarks cannot catch these confounds; §4.1 The pgvector ivfflat index returning sporadic empty result sets`；Limitations/Counterevidence=`§6 Discussion: semantic vs mechanistic retrieval; §7 Limitations and scope; §8 Conclusion`；正文 sha256=`960691f4efbd1ed096ef43fde4536be3088667811a183cc51ccc41b1b530fbb8`。

<!-- claim:SF-2026-ARXIV-2605-23058:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23058:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23058:end -->

<!-- review:SF-2026-ARXIV-2605-23066:start -->
#### Orbax: Distributed Checkpointing with JAX

**问题与机制。** In a landscape of high-performance distributed ML systems, JAX has emerged as a framework of choice. However, JAX's modular design philosophy leaves it without a standardized checkpointing solution. 系统 owner=`TRAIN-CHECKPOINT`。

**Exact-v1。** Method=`§3 Orbax Distributed Checkpointing Design`；Evaluation=`§5 Scale Evaluation`；Limitations/Counterevidence=`§6 Multi-controller and simulation limitations`；正文 sha256=`900ea414a1863deafa360f1688c1844e35683b8d8aea15263e3894d2cee9cdbf`。

<!-- claim:SF-2026-ARXIV-2605-23066:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23066:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23066:end -->

<!-- review:SF-2026-ARXIV-2605-23067:start -->
#### What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA

**问题与机制。** Reinforcement learning (RL) has emerged as a viable recipe for training LLM agents to reason over external memory banks in multi-session dialogue. We present a controlled empirical study that holds architecture, RL algorithm, and all hyperparameters fixed and varies only the training curriculum across three conditions: in-domain (LoCoMo), mixed-benchmark (LoCoMo + LongMemEval), and out-of-domain (LongMemEval only). 系统 owner=`TRAIN-DATA`。

**Exact-v1。** Method=`§What Training Data Teaches RL Memory Agents: An Empirical Study of Curriculum Effects in Memory-Augmented QA; §2.3 Curriculum Learning for RL-Based LLM Training; §3 Method`；Evaluation=`§2.2 Benchmarks for Long-Term Memory; §3.5 Evaluation; §4 Results`；Limitations/Counterevidence=`§6 Limitations and Future Work; §7 Conclusion`；正文 sha256=`184f58bce1c356a44c5a39bea8f8373790c34adefb14263713f1ff95eae95f9f`。

<!-- claim:SF-2026-ARXIV-2605-23067:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23067:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23067:end -->

<!-- review:SF-2026-ARXIV-2605-23071:start -->
#### The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management

**问题与机制。** Large language models (LLMs) increasingly rely on long-context processing, but expanding context windows introduces substantial computational and financial costs. Results show that deployment-aware optimization reduces effective token usage by approximately 25% at comparable performance, enabling more cost-efficient deployment of large language model systems, while amortized memory compression achieves over 50% lower token cost relative to full-context prompting in higher-performance settings. 系统 owner=`AGENT-CONTEXT`。

**Exact-v1。** Method=`§3 Cost–Performance Frontier for Context Strategies`；Evaluation=`§4 Comparative Evaluation`；Limitations/Counterevidence=`§5 Discussion and oracle/synthetic-boundary`；正文 sha256=`6d46f99b587dde04721d311930533e9b11fdac299a7d67f24e66482f9160d313`。

<!-- claim:SF-2026-ARXIV-2605-23071:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23071:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23071:end -->

<!-- review:SF-2026-ARXIV-2605-23078:start -->
#### GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs

**问题与机制。** Mixture-of-Experts Large Language Models (MoE-LLMs) achieve strong performance but incur substantial memory overhead due to massive expert parameters. In this work, we propose Global Expert-level Mixed-precision Quantization (GEMQ) to overcome these limitations via (1) a global linear-programming formulation that captures model-wide expert importance based on quantization error analysis, and (2) efficient router fine-tuning to adapt routing to quantized experts. 系统 owner=`INFER-TENSORRT-LLM`。

**Exact-v1。** Method=`§4 Method; §5.1 Comparison of MoE-LLM Quantization Methods; §Appendix B Comparison with State-of-the-Art Methods`；Evaluation=`§Analysis of Quantization Error.; §5 Experiments; §5.2 Quantization Overhead Analysis`；Limitations/Counterevidence=`§7 Limitations; §8 Conclusion`；正文 sha256=`3da7934f8b6adff187ab04557e221638cc7738b112eaa55f98f2fc5cfabb4e2b`。

<!-- claim:SF-2026-ARXIV-2605-23078:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23078:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23078:end -->

<!-- review:SF-2026-ARXIV-2605-23080:start -->
#### The Attribution Contract for Generative Language Models

**问题与机制。** Feature attribution scores each part of an input by how much it explains a model's output. We argue that in generative language models these scores carry no fixed meaning. 系统 owner=`PLATFORM-EVALUATION-SYSTEM`。

**Exact-v1。** Method=`§3 Attribution Contract`；Evaluation=`§5 Generative-LM Evaluation`；Limitations/Counterevidence=`§6 Discussion and attribution-scope boundary`；正文 sha256=`ff5eb8b1e622cd1a1b7dae83beddeb5b0bbfd3fa522b2f75a25a6823951b1e00`。

<!-- claim:SF-2026-ARXIV-2605-23080:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-23080:end -->

Books Decision=`Integrate`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-23080:end -->

<!-- review:SF-2026-ARXIV-2605-23157:start -->
#### Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs

**问题与机制。** We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Study Design; §3.1–§3.4 language × modality threat matrix`；Evaluation=`§4 Results; mixed-effects and matched-annotator evaluation`；Limitations/Counterevidence=`§7 Limitations; four-model/two-language scope`。

<!-- claim:SF-2026-ARXIV-2605-23157:start -->Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23157:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23157:end -->

<!-- review:SF-2026-ARXIV-2605-23158:start -->
#### What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference

**问题与机制。** To fill this gap, we introduce ActInv, which solves an intermediate activation matching problem to reconstruct the client's input. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Split Inference Protocol; §4.1–§4.2 Threat Model and ActInv`；Evaluation=`§4.3–§4.4 Evaluation`；Limitations/Counterevidence=`§5.3 Potential Defenses and split-point boundary`。

<!-- claim:SF-2026-ARXIV-2605-23158:start -->What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23158:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23158:end -->

<!-- review:SF-2026-ARXIV-2605-23168:start -->
#### PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs

**问题与机制。** We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 PoisonForge threat model and parameterized benchmark`；Evaluation=`§4–§5 twelve-model poisoning evaluation`；Limitations/Counterevidence=`§6 Limitations; instruction-tuning and tested poison-budget boundary`。

<!-- claim:SF-2026-ARXIV-2605-23168:start -->PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23168:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23168:end -->

<!-- review:SF-2026-ARXIV-2605-23170:start -->
#### Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks

**问题与机制。** We propose Context Rot Evaluation (CRE), a controlled framework varying all three factors, and evaluate nine LLMs on GSM8K and ARC-Challenge across two rounds: an initial five-model set and four newer vendor releases. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Context Rot Evaluation; controlled position/content/length factors`；Evaluation=`§4 Evaluation across nine models and two reasoning tasks`；Limitations/Counterevidence=`§7 Limitations; benchmark/task/context-family boundary`。

<!-- claim:SF-2026-ARXIV-2605-23170:start -->Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23170:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23170:end -->

<!-- review:SF-2026-ARXIV-2605-23196:start -->
#### Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers

**问题与机制。** In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Prompt-Overflow Threat Model`；Evaluation=`§4 Guardrail/Model Evaluation`；Limitations/Counterevidence=`§5 Discussion and tokenizer/context-boundary limits`。

<!-- claim:SF-2026-ARXIV-2605-23196:start -->Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23196:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23196:end -->

<!-- review:SF-2026-ARXIV-2605-23200:start -->
#### Adaptive Mass-Segmented KV Compression for Long-Context Reasoning

**问题与机制。** However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Adaptive Mass-Segmented KV Compression`；Evaluation=`§4 Long-Form Reasoning Evaluation`；Limitations/Counterevidence=`§5 Conclusion and evaluated-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23200:start -->Adaptive Mass-Segmented KV Compression for Long-Context Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23200:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23200:end -->

<!-- review:SF-2026-ARXIV-2605-23215:start -->
#### FastKernels: Benchmarking GPU Kernel Generation in Production

**问题与机制。** The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 FastKernels Production Benchmark Contract`；Evaluation=`§5 Kernel-Generation Evaluation`；Limitations/Counterevidence=`§6 Discussion and production-workload coverage limits`。

<!-- claim:SF-2026-ARXIV-2605-23215:start -->FastKernels: Benchmarking GPU Kernel Generation in Production only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23215:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23215:end -->

<!-- review:SF-2026-ARXIV-2605-23218:start -->
#### Foundation Protocol: A Coordination Layer for Agentic Society

**问题与机制。** Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Foundation Protocol Coordination Layer`；Evaluation=`§5 Multi-Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and governance-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-23218:start -->Foundation Protocol: A Coordination Layer for Agentic Society only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23218:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23218:end -->

<!-- review:SF-2026-ARXIV-2605-23220:start -->
#### WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents

**问题与机制。** We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 WMAttack Automated Attack Search`；Evaluation=`§4 World-Model Agent Evaluation`；Limitations/Counterevidence=`§5 Limitations and tested-environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23220:start -->WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23220:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23220:end -->

<!-- review:SF-2026-ARXIV-2605-23258:start -->
#### A Simple Plug-in for Improving Eviction-Based KV Cache Compression

**问题与机制。** We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Eviction-Aware KV Compression Plug-in`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Conclusion and eviction-policy boundary`。

<!-- claim:SF-2026-ARXIV-2605-23258:start -->A Simple Plug-in for Improving Eviction-Based KV Cache Compression only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23258:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23258:end -->

<!-- review:SF-2026-ARXIV-2605-23262:start -->
#### Designing Benchmarks for Knowledge Work

**问题与机制。** We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§4 work-centered benchmark representation`；Evaluation=`§5 worked benchmark comparisons`；Limitations/Counterevidence=`§6 Discussion; conceptual representation does not prove predictive validity`。

<!-- claim:SF-2026-ARXIV-2605-23262:start -->Designing Benchmarks for Knowledge Work only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23262:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23262:end -->

<!-- review:SF-2026-ARXIV-2605-23294:start -->
#### NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference

**问题与机制。** With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference. owner=`INFER-TENSORRT-LLM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§III NASiC CAM-selected multibit CIM architecture`；Evaluation=`§IV–§V architecture/model evaluation`；Limitations/Counterevidence=`§VI Discussion; simulated 3D-NAND/device-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23294:start -->NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23294:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23294:end -->

<!-- review:SF-2026-ARXIV-2605-23296:start -->
#### Parallel Context Compaction for Long-Horizon LLM Agent Serving

**问题与机制。** We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Parallel Context Compaction Runtime`；Evaluation=`§5 Long-Horizon Agent-Serving Evaluation`；Limitations/Counterevidence=`§6 Discussion and compaction-fidelity boundary`。

<!-- claim:SF-2026-ARXIV-2605-23296:start -->Parallel Context Compaction for Long-Horizon LLM Agent Serving only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23296:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23296:end -->

<!-- review:SF-2026-ARXIV-2605-23311:start -->
#### DART: Semantic Recoverability for Structured Tool Agents

**问题与机制。** We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise. owner=`AGENT-TOOL-CALLING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 DART Semantic-Recoverability Contract`；Evaluation=`§5 Structured-Tool Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and tool-schema boundary`。

<!-- claim:SF-2026-ARXIV-2605-23311:start -->DART: Semantic Recoverability for Structured Tool Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23311:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23311:end -->

<!-- review:SF-2026-ARXIV-2605-23348:start -->
#### CWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms

**问题与机制。** AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up. owner=`INFER-SCHEDULING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 XWind Cross-Site Routing Controller`；Evaluation=`§5 Renewable-Site Serving Evaluation`；Limitations/Counterevidence=`§6 Limitations and forecast/topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-23348:start -->CWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23348:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23348:end -->

<!-- review:SF-2026-ARXIV-2605-23362:start -->
#### Instance-Optimal Estimation with Multiple LLM Judges on a Budget

**问题与机制。** We formalize this question as *budgeted heteroskedastic multi-judge estimation*. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§4 budgeted heteroskedastic multi-judge estimation`；Evaluation=`§5 theory and empirical allocation evaluation`；Limitations/Counterevidence=`§6 Discussion; known-cost/bounded-score assumptions`。

<!-- claim:SF-2026-ARXIV-2605-23362:start -->Instance-Optimal Estimation with Multiple LLM Judges on a Budget only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23362:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23362:end -->

<!-- review:SF-2026-ARXIV-2605-23389:start -->
#### AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System

**问题与机制。** We propose AlignedServe, an LLM serving framework built around prefix-aware batching. owner=`INFER-SCHEDULING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 AlignedServe Prefix-Aware Batching`；Evaluation=`§5 Throughput/Compute Evaluation`；Limitations/Counterevidence=`§6 Conclusion and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-23389:start -->AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23389:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23389:end -->

<!-- review:SF-2026-ARXIV-2605-23414:start -->
#### When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems

**问题与机制。** To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Epistemic-Calibration Model for Multi-Agent Planning`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and planning/execution boundary`。

<!-- claim:SF-2026-ARXIV-2605-23414:start -->When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23414:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23414:end -->

<!-- review:SF-2026-ARXIV-2605-23454:start -->
#### ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning

**问题与机制。** We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 ARES automatic rubric synthesis and reward construction`；Evaluation=`§4 and Appendix F evaluation`；Limitations/Counterevidence=`Appendix A Limitations; generated-rubric correctness boundary`。

<!-- claim:SF-2026-ARXIV-2605-23454:start -->ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23454:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23454:end -->

<!-- review:SF-2026-ARXIV-2605-23464:start -->
#### Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization

**问题与机制。** We introduce Unextractable Protocol Models (UPMs): a training and inference framework that leverages the sharded model setup to ensure model shards (i.e., subsets) held by participants are incompatible at different time steps. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Unextractable Protocol Model Construction`；Evaluation=`§5 Collaborative Training/Inference Evaluation`；Limitations/Counterevidence=`§6 Security Assumptions and protocol limitations`。

<!-- claim:SF-2026-ARXIV-2605-23464:start -->Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23464:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23464:end -->

<!-- review:SF-2026-ARXIV-2605-23493:start -->
#### EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation

**问题与机制。** In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 EDGE-OPD evidence-guided on-policy distillation`；Evaluation=`§4–§5 experiments and diagnostics`；Limitations/Counterevidence=`Appendix A.10 Limitations; teacher/evidence/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-23493:start -->EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23493:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23493:end -->

<!-- review:SF-2026-ARXIV-2605-23574:start -->
#### Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents

**问题与机制。** We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items. owner=`AGENT-WORKFLOW`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Quantitative Goal-Persistence Contract`；Evaluation=`§5 Long-Horizon Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and task-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-23574:start -->Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23574:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23574:end -->

<!-- review:SF-2026-ARXIV-2605-23590:start -->
#### Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

**问题与机制。** We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference. owner=`AGENT-WORKFLOW`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§3 Co-ReAct step-level rubric and control loop`；Evaluation=`§4–§5 agent evaluation`；Limitations/Counterevidence=`§6 Limitations; rubric and environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23590:start -->Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23590:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23590:end -->

<!-- review:SF-2026-ARXIV-2605-23628:start -->
#### How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness

**问题与机制。** Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Social-Choice Leaderboard Model`；Evaluation=`§4 Benchmark-Rigging Analysis`；Limitations/Counterevidence=`§5 Discussion and scoring-rule assumptions`。

<!-- claim:SF-2026-ARXIV-2605-23628:start -->How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23628:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23628:end -->

<!-- review:SF-2026-ARXIV-2605-23640:start -->
#### CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference

**问题与机制。** Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 CachePrune Privacy-Aware KV Sharing`；Evaluation=`§5 Efficiency/Leakage Evaluation`；Limitations/Counterevidence=`§6 Limitations and attacker/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23640:start -->CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23640:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23640:end -->

<!-- review:SF-2026-ARXIV-2605-23657:start -->
#### OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents

**问题与机制。** In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 OpenSkillEval Audit Pipeline`；Evaluation=`§4 Open-Skill Ecosystem Evaluation`；Limitations/Counterevidence=`§5 Limitations and registry-coverage boundary`。

<!-- claim:SF-2026-ARXIV-2605-23657:start -->OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23657:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23657:end -->

<!-- review:SF-2026-ARXIV-2605-23701:start -->
#### Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks

**问题与机制。** We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Intervention-Based Weak-Label Audit`；Evaluation=`§4 Controlled Evaluation`；Limitations/Counterevidence=`§5 Discussion and intervention-identifiability limits`。

<!-- claim:SF-2026-ARXIV-2605-23701:start -->Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23701:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23701:end -->

<!-- review:SF-2026-ARXIV-2605-23723:start -->
#### MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

**问题与机制。** We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 MemAudit Causal/Structural Audit`；Evaluation=`§5 Poisoned-Memory Evaluation`；Limitations/Counterevidence=`§6 Limitations and post-hoc-detection boundary`。

<!-- claim:SF-2026-ARXIV-2605-23723:start -->MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23723:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23723:end -->

<!-- review:SF-2026-ARXIV-2605-23764:start -->
#### HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs

**问题与机制。** Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training. owner=`TRAIN-DISTRIBUTED-TRAINING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 HyperParallel-MoE Interleaved Scheduling`；Evaluation=`§5 Ascend-NPU Training Evaluation`；Limitations/Counterevidence=`§6 Conclusion and hardware/topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-23764:start -->HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23764:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23764:end -->

<!-- review:SF-2026-ARXIV-2605-23856:start -->
#### Point Tracking Improves World Action Models

**问题与机制。** We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Point-Tracking World-Action Model`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and observed-environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23856:start -->Point Tracking Improves World Action Models only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23856:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23856:end -->

<!-- review:SF-2026-ARXIV-2605-23893:start -->
#### Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models

**问题与机制。** We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks. owner=`MODEL-MOE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Complete-μE MoE Parameterization`；Evaluation=`§5 Hyperparameter-Transfer/Scaling Evaluation`；Limitations/Counterevidence=`§6 Limitations and tested-scale boundary`。

<!-- claim:SF-2026-ARXIV-2605-23893:start -->Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23893:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23893:end -->

<!-- review:SF-2026-ARXIV-2605-23899:start -->
#### From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

**问题与机制。** However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Model-Generated Skill Pipeline`；Evaluation=`§4 Skill-Use Evaluation`；Limitations/Counterevidence=`§5 Limitations and model/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-23899:start -->From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23899:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23899:end -->

<!-- review:SF-2026-ARXIV-2605-23904:start -->
#### SkillOpt: Executive Strategy for Self-Evolving Agent Skills

**问题与机制。** Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 SkillOpt Executive Strategy`；Evaluation=`§5 Self-Evolving Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and library-drift boundary`。

<!-- claim:SF-2026-ARXIV-2605-23904:start -->SkillOpt: Executive Strategy for Self-Evolving Agent Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23904:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23904:end -->

<!-- review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->
#### The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems

问题与机制：We introduce Counterfactual Composition Testing, which identifies the causal entry with 87.5% accuracy and zero false positives, while a forensics baseline fails across all 25 scenarios.。机制 owner=`AGENT-MEMORY`。
全文定位：`arXiv:2605.22842v1 HTML — §3 memory-poisoning attribution-gap threat model`；evaluation=`arXiv:2605.22842v1 — §4 attack/mitigation evaluation`；limitations/counterevidence=`arXiv:2605.22842v1 — §5 limitations: memory backend, attacker and detector scope`。
<!-- claim:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-22850 | score_7_9;forced_review;potential_books_delta | selected | DA-20260525-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260525-01 |
| SF-2026-ARXIV-2605-22863 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22863 |
| SF-2026-ARXIV-2605-22866 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22866 |
| SF-2026-ARXIV-2605-22868 | score_7_9;forced_review;potential_structural_gap | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22868 |
| SF-2026-ARXIV-2605-22882 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22882 |
| SF-2026-ARXIV-2605-22883 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22883 |
| SF-2026-ARXIV-2605-22884 | score_7_9;forced_review;potential_books_delta | selected | DA-20260525-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260525-02 |
| SF-2026-ARXIV-2605-22891 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22891 |
| SF-2026-ARXIV-2605-22894 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22894 |
| SF-2026-ARXIV-2605-22896 | score_7_9 | selected | DA-20260525-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260525-03 |
| SF-2026-ARXIV-2605-22905 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22905 |
| SF-2026-ARXIV-2605-22949 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22949 |
| SF-2026-ARXIV-2605-22984 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-22984 |
| SF-2026-ARXIV-2605-23019 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23019 |
| SF-2026-ARXIV-2605-23055 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23055 |
| SF-2026-ARXIV-2605-23057 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23057 |
| SF-2026-ARXIV-2605-23058 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23058 |
| SF-2026-ARXIV-2605-23066 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23066 |
| SF-2026-ARXIV-2605-23067 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23067 |
| SF-2026-ARXIV-2605-23071 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23071 |
| SF-2026-ARXIV-2605-23078 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23078 |
| SF-2026-ARXIV-2605-23080 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23080 |
| SF-2026-ARXIV-2605-23157 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23157 |
| SF-2026-ARXIV-2605-23158 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23158 |
| SF-2026-ARXIV-2605-23168 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23168 |
| SF-2026-ARXIV-2605-23170 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23170 |
| SF-2026-ARXIV-2605-23196 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23196 |
| SF-2026-ARXIV-2605-23200 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23200 |
| SF-2026-ARXIV-2605-23215 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23215 |
| SF-2026-ARXIV-2605-23218 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23218 |
| SF-2026-ARXIV-2605-23220 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23220 |
| SF-2026-ARXIV-2605-23258 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23258 |
| SF-2026-ARXIV-2605-23262 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23262 |
| SF-2026-ARXIV-2605-23294 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23294 |
| SF-2026-ARXIV-2605-23296 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23296 |
| SF-2026-ARXIV-2605-23311 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23311 |
| SF-2026-ARXIV-2605-23348 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23348 |
| SF-2026-ARXIV-2605-23362 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23362 |
| SF-2026-ARXIV-2605-23389 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23389 |
| SF-2026-ARXIV-2605-23414 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23414 |
| SF-2026-ARXIV-2605-23454 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23454 |
| SF-2026-ARXIV-2605-23464 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23464 |
| SF-2026-ARXIV-2605-23493 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23493 |
| SF-2026-ARXIV-2605-23574 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23574 |
| SF-2026-ARXIV-2605-23590 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23590 |
| SF-2026-ARXIV-2605-23628 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23628 |
| SF-2026-ARXIV-2605-23640 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23640 |
| SF-2026-ARXIV-2605-23657 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23657 |
| SF-2026-ARXIV-2605-23701 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23701 |
| SF-2026-ARXIV-2605-23723 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23723 |
| SF-2026-ARXIV-2605-23764 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23764 |
| SF-2026-ARXIV-2605-23856 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23856 |
| SF-2026-ARXIV-2605-23893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23893 |
| SF-2026-ARXIV-2605-23899 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23899 |
| SF-2026-ARXIV-2605-23904 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-23904 |
| SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN |

<!-- analysis:DA-20260525-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-22850

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260525-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22863:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22863:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22866:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22866:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22868:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22868:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22882:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22882:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22883:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22883:end -->

<!-- analysis:DA-20260525-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-22884

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260525-02:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22891:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22891:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22894:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22894:end -->

<!-- analysis:DA-20260525-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-22896

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260525-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22905:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22905:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22949:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22949:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-22984:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-22984:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23019:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23019:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23055:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23055:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23057:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23057:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23058:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23058:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23066:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23066:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23067:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23067:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23071:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23078:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23078:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23080:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23080:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23157:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23157:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23158:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23168:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23168:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23170:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23170:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23196:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23196:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23200:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23200:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23215:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23215:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23218:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23218:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23220:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23220:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23258:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23258:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23262:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23294:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23294:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23296:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23296:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23311:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23311:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23348:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23362:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23362:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23389:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23414:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23414:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23454:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23454:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23464:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23464:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23493:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23574:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23590:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23590:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23628:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23628:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23640:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23640:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23657:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23657:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23701:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23701:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23723:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23723:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23764:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23764:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23856:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23856:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23893:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23899:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-23904:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-23904:end -->

<!-- analysis-decision:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-22850 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22850 | delta:SF-2026-ARXIV-2605-22850 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22850 |
| SF-2026-ARXIV-2605-22863 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22863 | delta:SF-2026-ARXIV-2605-22863 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22863 |
| SF-2026-ARXIV-2605-22866 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22866 | delta:SF-2026-ARXIV-2605-22866 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22866 |
| SF-2026-ARXIV-2605-22868 | considered: PLATFORM-PRODUCTION, MULTIMODAL-REPRESENTATION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72 | existing:SF-2026-ARXIV-2605-22868 | delta:SF-2026-ARXIV-2605-22868 | Direct Evolution | Structural Candidate | books-review:SF-2026-ARXIV-2605-22868 |
| SF-2026-ARXIV-2605-22882 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-22882 | delta:SF-2026-ARXIV-2605-22882 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22882 |
| SF-2026-ARXIV-2605-22883 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-22883 | delta:SF-2026-ARXIV-2605-22883 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22883 |
| SF-2026-ARXIV-2605-22884 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-22884 | delta:SF-2026-ARXIV-2605-22884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22884 |
| SF-2026-ARXIV-2605-22891 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-22891 | delta:SF-2026-ARXIV-2605-22891 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22891 |
| SF-2026-ARXIV-2605-22894 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-22894 | delta:SF-2026-ARXIV-2605-22894 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22894 |
| SF-2026-ARXIV-2605-22896 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-22896 | delta:SF-2026-ARXIV-2605-22896 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22896 |
| SF-2026-ARXIV-2605-22905 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-22905 | delta:SF-2026-ARXIV-2605-22905 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-22905 |
| SF-2026-ARXIV-2605-22949 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-22949 | delta:SF-2026-ARXIV-2605-22949 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22949 |
| SF-2026-ARXIV-2605-22984 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-22984 | delta:SF-2026-ARXIV-2605-22984 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-22984 |
| SF-2026-ARXIV-2605-23019 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23019 | delta:SF-2026-ARXIV-2605-23019 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23019 |
| SF-2026-ARXIV-2605-23055 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23055 | delta:SF-2026-ARXIV-2605-23055 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23055 |
| SF-2026-ARXIV-2605-23057 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-23057 | delta:SF-2026-ARXIV-2605-23057 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23057 |
| SF-2026-ARXIV-2605-23058 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23058 | delta:SF-2026-ARXIV-2605-23058 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23058 |
| SF-2026-ARXIV-2605-23066 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#chapter-35 | books/part-04-training-system/34-dpo.md#chapter-34;books/part-04-training-system/36-distributed-training.md#chapter-36 | existing:SF-2026-ARXIV-2605-23066 | delta:SF-2026-ARXIV-2605-23066 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23066 |
| SF-2026-ARXIV-2605-23067 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-23067 | delta:SF-2026-ARXIV-2605-23067 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23067 |
| SF-2026-ARXIV-2605-23071 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-23071 | delta:SF-2026-ARXIV-2605-23071 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23071 |
| SF-2026-ARXIV-2605-23078 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-23078 | delta:SF-2026-ARXIV-2605-23078 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23078 |
| SF-2026-ARXIV-2605-23080 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23080 | delta:SF-2026-ARXIV-2605-23080 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23080 |
| SF-2026-ARXIV-2605-23157 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23157 | delta:SF-2026-ARXIV-2605-23157 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23157 |
| SF-2026-ARXIV-2605-23158 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23158 | delta:SF-2026-ARXIV-2605-23158 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23158 |
| SF-2026-ARXIV-2605-23168 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-23168 | delta:SF-2026-ARXIV-2605-23168 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23168 |
| SF-2026-ARXIV-2605-23170 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23170 | delta:SF-2026-ARXIV-2605-23170 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23170 |
| SF-2026-ARXIV-2605-23196 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23196 | delta:SF-2026-ARXIV-2605-23196 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23196 |
| SF-2026-ARXIV-2605-23200 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23200 | delta:SF-2026-ARXIV-2605-23200 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23200 |
| SF-2026-ARXIV-2605-23215 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23215 | delta:SF-2026-ARXIV-2605-23215 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23215 |
| SF-2026-ARXIV-2605-23218 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23218 | delta:SF-2026-ARXIV-2605-23218 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23218 |
| SF-2026-ARXIV-2605-23220 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23220 | delta:SF-2026-ARXIV-2605-23220 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23220 |
| SF-2026-ARXIV-2605-23258 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23258 | delta:SF-2026-ARXIV-2605-23258 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23258 |
| SF-2026-ARXIV-2605-23262 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23262 | delta:SF-2026-ARXIV-2605-23262 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23262 |
| SF-2026-ARXIV-2605-23294 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-23294 | delta:SF-2026-ARXIV-2605-23294 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23294 |
| SF-2026-ARXIV-2605-23296 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-23296 | delta:SF-2026-ARXIV-2605-23296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23296 |
| SF-2026-ARXIV-2605-23311 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-23311 | delta:SF-2026-ARXIV-2605-23311 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23311 |
| SF-2026-ARXIV-2605-23348 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-23348 | delta:SF-2026-ARXIV-2605-23348 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23348 |
| SF-2026-ARXIV-2605-23362 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23362 | delta:SF-2026-ARXIV-2605-23362 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23362 |
| SF-2026-ARXIV-2605-23389 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-23389 | delta:SF-2026-ARXIV-2605-23389 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23389 |
| SF-2026-ARXIV-2605-23414 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23414 | delta:SF-2026-ARXIV-2605-23414 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23414 |
| SF-2026-ARXIV-2605-23454 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-23454 | delta:SF-2026-ARXIV-2605-23454 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23454 |
| SF-2026-ARXIV-2605-23464 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23464 | delta:SF-2026-ARXIV-2605-23464 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23464 |
| SF-2026-ARXIV-2605-23493 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-23493 | delta:SF-2026-ARXIV-2605-23493 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23493 |
| SF-2026-ARXIV-2605-23574 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-23574 | delta:SF-2026-ARXIV-2605-23574 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23574 |
| SF-2026-ARXIV-2605-23590 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-23590 | delta:SF-2026-ARXIV-2605-23590 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23590 |
| SF-2026-ARXIV-2605-23628 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23628 | delta:SF-2026-ARXIV-2605-23628 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23628 |
| SF-2026-ARXIV-2605-23640 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23640 | delta:SF-2026-ARXIV-2605-23640 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23640 |
| SF-2026-ARXIV-2605-23657 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23657 | delta:SF-2026-ARXIV-2605-23657 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23657 |
| SF-2026-ARXIV-2605-23701 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23701 | delta:SF-2026-ARXIV-2605-23701 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23701 |
| SF-2026-ARXIV-2605-23723 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-23723 | delta:SF-2026-ARXIV-2605-23723 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23723 |
| SF-2026-ARXIV-2605-23764 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-23764 | delta:SF-2026-ARXIV-2605-23764 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23764 |
| SF-2026-ARXIV-2605-23856 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23856 | delta:SF-2026-ARXIV-2605-23856 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23856 |
| SF-2026-ARXIV-2605-23893 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20;books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-23893 | delta:SF-2026-ARXIV-2605-23893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23893 |
| SF-2026-ARXIV-2605-23899 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23899 | delta:SF-2026-ARXIV-2605-23899 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23899 |
| SF-2026-ARXIV-2605-23904 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23904 | delta:SF-2026-ARXIV-2605-23904 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23904 |
| SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | delta:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN | Direct Evolution | No Change — Existing Coverage | books-review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN |

<!-- books-review:SF-2026-ARXIV-2605-22850:start -->
<!-- existing:SF-2026-ARXIV-2605-22850:start -->已逐章读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前正文拥有 surrounding principle，但尚未显式承载 `ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse` 改变的 state/data/control/evidence boundary。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-22850:end -->
<!-- delta:SF-2026-ARXIV-2605-22850:start -->ObjectCache: Layerwise Object-Storage Retrieval for KV Cache Reuse 提出的具体变化是：We propose ObjectCache, which co-designs the storage protocol and transfer schedule so that the storage server delivers KV cache data in the order the GPU consumes it, overlapping data transfer with compute across concurrent requests. 摘要中的长期系统挑战为：prefix KV reuse crosses local memory into layerwise object-store retrieval with explicit object identity。它可能改变 `INFER-KV-CACHE` 的状态、控制或证据合同，因此保留并要求 exact-v1 challenge；摘要结果“Under shared bandwidth caps, our scheduler reduces added TTFT by 1.2--1.8x compared with equal bandwidth sharing.”暂不作为最终证据。<!-- delta:SF-2026-ARXIV-2605-22850:end --> Decision=`Integrate`；non-author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-22850:end -->

<!-- books-review:SF-2026-ARXIV-2605-22863:start -->
<!-- existing:SF-2026-ARXIV-2605-22863:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-22863:end -->
<!-- delta:SF-2026-ARXIV-2605-22863:start -->We introduce Latent Cache Flow (LCF).<!-- delta:SF-2026-ARXIV-2605-22863:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22863:end -->

<!-- books-review:SF-2026-ARXIV-2605-22866:start -->
<!-- existing:SF-2026-ARXIV-2605-22866:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 已有 surrounding principle，但尚未显式承载该 family 改变的 state/control/evidence boundary。<!-- existing:SF-2026-ARXIV-2605-22866:end -->
<!-- delta:SF-2026-ARXIV-2605-22866:start -->We introduce BOHM, which extracts a hierarchical attribution tree directly from the routing weights such systems already maintain: leaf attribution is the path product of root-to-leaf routing weights; level-k attribution is the induced distribution over depth-k nodes.<!-- delta:SF-2026-ARXIV-2605-22866:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22866:end -->

<!-- books-review:SF-2026-ARXIV-2605-22868:start -->
<!-- existing:SF-2026-ARXIV-2605-22868:start -->`books/part-06-ai-infrastructure/73-production-best-practice.md` 只可承载生产边界；near-sensor→edge→cloud 的长期 compute/data owner 尚无单一稳定节点，进入季度结构复核而不强塞正文。<!-- existing:SF-2026-ARXIV-2605-22868:end -->
<!-- delta:SF-2026-ARXIV-2605-22868:start -->We present FusionSense, a fusion-aware intelligent sensing framework for energy-constrained autonomous edge systems.<!-- delta:SF-2026-ARXIV-2605-22868:end --> Independent decision=`Structural Candidate`。
<!-- books-review:SF-2026-ARXIV-2605-22868:end -->

<!-- books-review:SF-2026-ARXIV-2605-22882:start -->
<!-- existing:SF-2026-ARXIV-2605-22882:start -->已顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。第25章已覆盖 projective 4D predictive state、geometry-motion consistency、action-conditioned transition 与真实观测回滚。`GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation` 的 source-specific 机制是：We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training.；该增量没有改变现有 owner、commit/evidence boundary、failure fallback 或旧路径共存条件，因此保留为 Daily evidence 而不重复写入 Books。<!-- existing:SF-2026-ARXIV-2605-22882:end -->
<!-- delta:SF-2026-ARXIV-2605-22882:start -->We present GEM-4D, a geometry-grounded video world model that resolves this limitation by injecting dense 4D correspondence supervision distilled from a pretrained geometry foundation model into the video generative backbone during training.<!-- delta:SF-2026-ARXIV-2605-22882:end --> Independent decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-22882:end -->

<!-- books-review:SF-2026-ARXIV-2605-22883:start -->
<!-- existing:SF-2026-ARXIV-2605-22883:start -->已顺读 `books/part-06-ai-infrastructure/70-cost.md` 与相邻章节 ['books/part-06-ai-infrastructure/69-trace.md', 'books/part-06-ai-infrastructure/71-multi-tenant.md']。第70章已区分 resource time、effective utilization、quality/SLO 合格工作、agent state-dependent work 与 deployable power；但 `Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems` 所暴露的以下缺口尚未显式进入正文：Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。<!-- existing:SF-2026-ARXIV-2605-22883:end -->
<!-- delta:SF-2026-ARXIV-2605-22883:start -->Agent 能耗从 per-token/per-request 上移到 per-successful-goal：同一 goal 的模型调用、tool、retry、idle 与失败 run 进入同一 lineage；成功谓词/evaluator 版本决定分母。<!-- delta:SF-2026-ARXIV-2605-22883:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22883:end -->

<!-- books-review:SF-2026-ARXIV-2605-22884:start -->
<!-- existing:SF-2026-ARXIV-2605-22884:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。第45章已覆盖 sparse selection、tiering、prefetch、eviction、reuse identity、误差预算与 exact recompute fallback；但 `Tensor Cache: Eviction-conditioned Associative Memory for Transformers` 所暴露的以下缺口尚未显式进入正文：sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。<!-- existing:SF-2026-ARXIV-2605-22884:end -->
<!-- delta:SF-2026-ARXIV-2605-22884:start -->sliding-window eviction 不再等于丢弃：exact recent KV 作为 L1，已驱逐 KV 以 outer-product fast-weight matrix 形成固定大小 L2；写入顺序、decay/gate、数值 scan 与 exact-window fallback 成为新 cache identity。<!-- delta:SF-2026-ARXIV-2605-22884:end --> Independent decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-22884:end -->

<!-- existing:SF-2026-ARXIV-2605-22891:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22891:end -->
<!-- delta:SF-2026-ARXIV-2605-22891:start -->We show that this assumption fails structurally for inverse problems with multimodal posteriors.<!-- delta:SF-2026-ARXIV-2605-22891:end -->
<!-- books-review:SF-2026-ARXIV-2605-22891:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22891:end -->

<!-- existing:SF-2026-ARXIV-2605-22894:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22894:end -->
<!-- delta:SF-2026-ARXIV-2605-22894:start -->We propose SCRIPT, a scalable diffusion policy with a multi-stage training framework for language-driven physics-based humanoid control.<!-- delta:SF-2026-ARXIV-2605-22894:end -->
<!-- books-review:SF-2026-ARXIV-2605-22894:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22894:end -->

<!-- existing:SF-2026-ARXIV-2605-22896:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy', 'Action-facing Representation 也是 Gradient Authority Boundary', 'World-action model', 'Training-only Foresight 不是 Persistent World State', 'Action representation', '单步 action', 'Action chunk']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22896:end -->
<!-- delta:SF-2026-ARXIV-2605-22896:start -->We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks.<!-- delta:SF-2026-ARXIV-2605-22896:end -->
<!-- books-review:SF-2026-ARXIV-2605-22896:start -->owner=`MULTIMODAL-EMBODIED-VLA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22896:end -->

<!-- existing:SF-2026-ARXIV-2605-22905:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22905:end -->
<!-- delta:SF-2026-ARXIV-2605-22905:start -->We argue that evidence verifiability is a prerequisite for trustworthy self-evolution in search agents: each generated instance should include not only an answer but also a source-grounded span whose contribution to that answer can be measured.<!-- delta:SF-2026-ARXIV-2605-22905:end -->
<!-- books-review:SF-2026-ARXIV-2605-22905:start -->owner=`AGENT-PLATFORM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22905:end -->

<!-- existing:SF-2026-ARXIV-2605-22949:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源', 'Iteration Scheduling', 'Physical AI 把 Execution Horizon 变成调度状态', 'Routing、Placement 与 Autoscaling', 'Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22949:end -->
<!-- delta:SF-2026-ARXIV-2605-22949:start -->多模型路由的 confidence calibration 是在线状态：per-model/per-band factor、feedback delay、selection policy 与 forgetting schedule 必须进入 routing revision；适应漂移换来 chosen-answer feedback bias 和 cold-start 风险。<!-- delta:SF-2026-ARXIV-2605-22949:end -->
<!-- books-review:SF-2026-ARXIV-2605-22949:start -->owner=`INFER-SCHEDULING`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22949:end -->

<!-- existing:SF-2026-ARXIV-2605-22984:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”', '多 Agent Cascade 需要跨 Channel 的 Influence Graph', 'Safety Evaluation 的单位是 Run，不只是 Prompt', 'Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate', 'Containment 不能只看最终是否发生攻击']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-22984:end -->
<!-- delta:SF-2026-ARXIV-2605-22984:start -->test-time training 会创建可持续改变后续行为的新 model revision；adaptation loop 只能提出 update，独立 safety gate 必须在更新前后重验收并拥有 commit/rollback，收益是适应性，代价是可累积 guardrail erosion。<!-- delta:SF-2026-ARXIV-2605-22984:end -->
<!-- books-review:SF-2026-ARXIV-2605-22984:start -->owner=`PLATFORM-SECURITY`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-22984:end -->

<!-- existing:SF-2026-ARXIV-2605-23019:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可编程 Skill 需要输入、状态与副作用契约', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元', '三个平面', 'Agent Runtime State Machine', 'Scheduling 不只是 GPU']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23019:end -->
<!-- delta:SF-2026-ARXIV-2605-23019:start -->Agent 自演化应分成 prompt fast path 与 control-logic slow path：前者饱和后才允许后者在 held-out replay 下晋级；双 timescale 降低 blast radius，但引入阶段切换、验证集过拟合和 rollback debt。<!-- delta:SF-2026-ARXIV-2605-23019:end -->
<!-- books-review:SF-2026-ARXIV-2605-23019:start -->owner=`AGENT-PLATFORM`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23019:end -->

<!-- existing:SF-2026-ARXIV-2605-23055:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23055:end -->
<!-- delta:SF-2026-ARXIV-2605-23055:start -->We operationalize the environment component through eight categorized trigger factors, such as placeholder entities and grading-style output formats, and study recognition and behavior through chain-of-thought monitoring.<!-- delta:SF-2026-ARXIV-2605-23055:end -->
<!-- books-review:SF-2026-ARXIV-2605-23055:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23055:end -->

<!-- existing:SF-2026-ARXIV-2605-23057:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源', 'Iteration Scheduling', 'Physical AI 把 Execution Horizon 变成调度状态', 'Routing、Placement 与 Autoscaling', 'Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23057:end -->
<!-- delta:SF-2026-ARXIV-2605-23057:start -->RequestRouter is a lightweight request-boundary controller for reducing the latency and energy cost of single-GPU large language model inference.<!-- delta:SF-2026-ARXIV-2605-23057:end -->
<!-- books-review:SF-2026-ARXIV-2605-23057:start -->owner=`INFER-SCHEDULING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23057:end -->

<!-- existing:SF-2026-ARXIV-2605-23058:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23058:end -->
<!-- delta:SF-2026-ARXIV-2605-23058:start -->We present agent-breakage, a closed-loop measurement framework that injects faults into a target Kubernetes cluster, observes how an autonomous agent responds, scores the response on four axes against ground truth, and accumulates outcome-labeled (state, action, outcome) tuples.<!-- delta:SF-2026-ARXIV-2605-23058:end -->
<!-- books-review:SF-2026-ARXIV-2605-23058:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23058:end -->

<!-- existing:SF-2026-ARXIV-2605-23066:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么只保存 Weights 不够', '一个完整训练状态清单', 'Checkpoint Size 为什么远大于模型文件', '一致性首先是 Step 边界', 'Checkpoint 应像事务一样提交', '分布式 Sharded Checkpoint', 'Resharding 为什么比 Load 更难', 'Data Cursor 为什么必须保存', 'RNG State 为什么影响可复现性', '异步保存移动了 Pause，而没有删除 IO', '从统一 Object Graph 到 Composable State Providers', '保存频率是故障成本权衡', '从持久 Checkpoint-Restart 到在线 Topology Repair']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23066:end -->
<!-- delta:SF-2026-ARXIV-2605-23066:start -->However, JAX's modular design philosophy leaves it without a standardized checkpointing solution.<!-- delta:SF-2026-ARXIV-2605-23066:end -->
<!-- books-review:SF-2026-ARXIV-2605-23066:start -->owner=`TRAIN-CHECKPOINT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23066:end -->

<!-- existing:SF-2026-ARXIV-2605-23067:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', 'Data Reuse 改变的是 Layer-wise Growth，不只是 Epoch 计数', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Filter Threshold 必须绑定 Compute-to-Unique-Data Regime', 'Synthetic data：从“先生成再打分”到 Specification Compilation', '没有真实后端时，Synthetic API State 只能是派生训练状态', 'Failure-driven Curriculum：难例必须来自可重放失败，而不是模型自信']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23067:end -->
<!-- delta:SF-2026-ARXIV-2605-23067:start -->We present a controlled empirical study that holds architecture, RL algorithm, and all hyperparameters fixed and varies only the training curriculum across three conditions: in-domain (LoCoMo), mixed-benchmark (LoCoMo + LongMemEval), and out-of-domain (LongMemEval only).<!-- delta:SF-2026-ARXIV-2605-23067:end -->
<!-- books-review:SF-2026-ARXIV-2605-23067:start -->owner=`TRAIN-DATA`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23067:end -->

<!-- existing:SF-2026-ARXIV-2605-23071:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', 'Context 是一次调用的可见状态', 'Token Budget 是容量约束', '为什么“全塞进去”会失败', 'Context Assembly Pipeline', 'Context Serving 是派生视图生命周期', 'Semantic Policy 与 Recoverable Bookkeeping 应分 Owner', 'Context Compression 的损失', '从 Generic Compression 到 Goal-conditioned Structured Pruning', 'Context Identity 与 Cache', 'Context Map 是轻量导航状态，不是事实副本', 'Context 中的信任冲突', 'Observability 与 Evaluation', '条件化机制分支与共存边界']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23071:end -->
<!-- delta:SF-2026-ARXIV-2605-23071:start -->Results show that deployment-aware optimization reduces effective token usage by approximately 25% at comparable performance, enabling more cost-efficient deployment of large language model systems, while amortized memory compression achieves over 50% lower token cost relative to full-context prompting in higher-performance settings.<!-- delta:SF-2026-ARXIV-2605-23071:end -->
<!-- books-review:SF-2026-ARXIV-2605-23071:start -->owner=`AGENT-CONTEXT`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23071:end -->

<!-- existing:SF-2026-ARXIV-2605-23078:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract', '从 Linear 语义到 GEMM 执行', 'Irregular Compute 要先归一为 GEMM + Epilogue Contract', '两种稀疏性必须共享地址合同，却不必共享 Kernel', 'cuBLAS 不是一个固定 GEMM Kernel', 'Tensor Core 指令名必须分层', 'TMA 解决搬运，不负责矩阵计算']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23078:end -->
<!-- delta:SF-2026-ARXIV-2605-23078:start -->MoE quantization 会改变 router 的 expert selection，bit allocation 不能继续逐层独立决定；global expert error budget 与 router recalibration 共同形成 execution-plan revision，内存收益换来全局求解与校准成本。<!-- delta:SF-2026-ARXIV-2605-23078:end -->
<!-- books-review:SF-2026-ARXIV-2605-23078:start -->owner=`INFER-TENSORRT-LLM`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23078:end -->

<!-- existing:SF-2026-ARXIV-2605-23080:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', 'Backend 是 Evaluation Identity 的一部分', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '不确定性必须绑定覆盖假设，而不是装饰性置信区间', '评估对象有四个层次', 'Model Evaluation', 'System Evaluation', 'Runtime and Service Evaluation']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-23080:end -->
<!-- delta:SF-2026-ARXIV-2605-23080:start -->Attribution 不是单一分数而是由解释对象、受众、可接受证据、faithfulness/citation evaluator 与失败处置组成的 versioned contract；更清晰的责任边界换来多协议维护成本。<!-- delta:SF-2026-ARXIV-2605-23080:end -->
<!-- books-review:SF-2026-ARXIV-2605-23080:start -->owner=`PLATFORM-EVALUATION-SYSTEM`；decision=`Integrate`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-23080:end -->

<!-- books-review:SF-2026-ARXIV-2605-23157:start -->
<!-- existing:SF-2026-ARXIV-2605-23157:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23157:end -->
<!-- delta:SF-2026-ARXIV-2605-23157:start -->We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni.<!-- delta:SF-2026-ARXIV-2605-23157:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23157:end -->

<!-- books-review:SF-2026-ARXIV-2605-23158:start -->
<!-- existing:SF-2026-ARXIV-2605-23158:start -->现有安全章没有把 split point、server-visible activation 与 inversion attack 共同定义为隐私边界。<!-- existing:SF-2026-ARXIV-2605-23158:end -->
<!-- delta:SF-2026-ARXIV-2605-23158:start -->To fill this gap, we introduce ActInv, which solves an intermediate activation matching problem to reconstruct the client's input.<!-- delta:SF-2026-ARXIV-2605-23158:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23158:end -->

<!-- books-review:SF-2026-ARXIV-2605-23168:start -->
<!-- existing:SF-2026-ARXIV-2605-23168:start -->正文已覆盖 data lineage、poisoning/contamination、specification compilation 与 golden-data governance。 本 family 的具体机制 `We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23168:end -->
<!-- delta:SF-2026-ARXIV-2605-23168:start -->We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget.<!-- delta:SF-2026-ARXIV-2605-23168:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1。
<!-- books-review:SF-2026-ARXIV-2605-23168:end -->

<!-- books-review:SF-2026-ARXIV-2605-23170:start -->
<!-- existing:SF-2026-ARXIV-2605-23170:start -->现有 Evaluation 主线没有把 target position、filler content 与 context length 冻结成 reasoning benchmark 的联合 identity。<!-- existing:SF-2026-ARXIV-2605-23170:end -->
<!-- delta:SF-2026-ARXIV-2605-23170:start -->We propose Context Rot Evaluation (CRE), a controlled framework varying all three factors, and evaluate nine LLMs on GSM8K and ARC-Challenge across two rounds: an initial five-model set and four newer vendor releases.<!-- delta:SF-2026-ARXIV-2605-23170:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23170:end -->

<!-- books-review:SF-2026-ARXIV-2605-23196:start -->
<!-- existing:SF-2026-ARXIV-2605-23196:start -->现有 pre-guard 叙述没有覆盖 guardrail inspection window 与 downstream model context window 不一致造成的可组合绕过。<!-- existing:SF-2026-ARXIV-2605-23196:end -->
<!-- delta:SF-2026-ARXIV-2605-23196:start -->In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs.<!-- delta:SF-2026-ARXIV-2605-23196:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23196:end -->

<!-- books-review:SF-2026-ARXIV-2605-23200:start -->
<!-- existing:SF-2026-ARXIV-2605-23200:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23200:end -->
<!-- delta:SF-2026-ARXIV-2605-23200:start -->However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence.<!-- delta:SF-2026-ARXIV-2605-23200:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23200:end -->

<!-- books-review:SF-2026-ARXIV-2605-23215:start -->
<!-- existing:SF-2026-ARXIV-2605-23215:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23215:end -->
<!-- delta:SF-2026-ARXIV-2605-23215:start -->The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems.<!-- delta:SF-2026-ARXIV-2605-23215:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23215:end -->

<!-- books-review:SF-2026-ARXIV-2605-23218:start -->
<!-- existing:SF-2026-ARXIV-2605-23218:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23218:end -->
<!-- delta:SF-2026-ARXIV-2605-23218:start -->Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another.<!-- delta:SF-2026-ARXIV-2605-23218:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-23218:end -->

<!-- books-review:SF-2026-ARXIV-2605-23220:start -->
<!-- existing:SF-2026-ARXIV-2605-23220:start -->正文已覆盖 action-conditioned transition、rollout identity、attack surface、fallback 与 world-state evaluation。 本 family 的具体机制 `We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23220:end -->
<!-- delta:SF-2026-ARXIV-2605-23220:start -->We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents.<!-- delta:SF-2026-ARXIV-2605-23220:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3。
<!-- books-review:SF-2026-ARXIV-2605-23220:end -->

<!-- books-review:SF-2026-ARXIV-2605-23258:start -->
<!-- existing:SF-2026-ARXIV-2605-23258:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23258:end -->
<!-- delta:SF-2026-ARXIV-2605-23258:start -->We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction.<!-- delta:SF-2026-ARXIV-2605-23258:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23258:end -->

<!-- books-review:SF-2026-ARXIV-2605-23262:start -->
<!-- existing:SF-2026-ARXIV-2605-23262:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23262:end -->
<!-- delta:SF-2026-ARXIV-2605-23262:start -->We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result.<!-- delta:SF-2026-ARXIV-2605-23262:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23262:end -->

<!-- books-review:SF-2026-ARXIV-2605-23294:start -->
<!-- existing:SF-2026-ARXIV-2605-23294:start -->正文已把 backend lowering、heterogeneous execution、kernel correctness 与 device fallback 放在同一执行计划中。 本 family 的具体机制 `With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23294:end -->
<!-- delta:SF-2026-ARXIV-2605-23294:start -->With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference.<!-- delta:SF-2026-ARXIV-2605-23294:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4c19b842b8e2ddb31cc4681c31e5484defce4f9769950473cc31a5afa61e338a。
<!-- books-review:SF-2026-ARXIV-2605-23294:end -->

<!-- books-review:SF-2026-ARXIV-2605-23296:start -->
<!-- existing:SF-2026-ARXIV-2605-23296:start -->现有 Context Compression 尚未表达 blocking compaction 到 parallel/background compaction 的状态交接、stall 与 fidelity contract。<!-- existing:SF-2026-ARXIV-2605-23296:end -->
<!-- delta:SF-2026-ARXIV-2605-23296:start -->We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks.<!-- delta:SF-2026-ARXIV-2605-23296:end --> Independent decision=`Integrate`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-23296:end -->

<!-- books-review:SF-2026-ARXIV-2605-23311:start -->
<!-- existing:SF-2026-ARXIV-2605-23311:start -->正文已覆盖 proposal/commit、tool contract、recoverability、effect receipt 与 exactly-once boundary。 本 family 的具体机制 `We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23311:end -->
<!-- delta:SF-2026-ARXIV-2605-23311:start -->We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise.<!-- delta:SF-2026-ARXIV-2605-23311:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9。
<!-- books-review:SF-2026-ARXIV-2605-23311:end -->

<!-- books-review:SF-2026-ARXIV-2605-23348:start -->
<!-- existing:SF-2026-ARXIV-2605-23348:start -->正文已覆盖 workload-aware admission、placement、batch cost、SLO 与 fallback。 本 family 的具体机制 `AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23348:end -->
<!-- delta:SF-2026-ARXIV-2605-23348:start -->AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up.<!-- delta:SF-2026-ARXIV-2605-23348:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-23348:end -->

<!-- books-review:SF-2026-ARXIV-2605-23362:start -->
<!-- existing:SF-2026-ARXIV-2605-23362:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We formalize this question as *budgeted heteroskedastic multi-judge estimation*.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23362:end -->
<!-- delta:SF-2026-ARXIV-2605-23362:start -->We formalize this question as *budgeted heteroskedastic multi-judge estimation*.<!-- delta:SF-2026-ARXIV-2605-23362:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23362:end -->

<!-- books-review:SF-2026-ARXIV-2605-23389:start -->
<!-- existing:SF-2026-ARXIV-2605-23389:start -->现有调度章未明确 decode iteration 内 KV-length 差异形成的 batch critical path 及 prefix-length-aware regrouping。<!-- existing:SF-2026-ARXIV-2605-23389:end -->
<!-- delta:SF-2026-ARXIV-2605-23389:start -->We propose AlignedServe, an LLM serving framework built around prefix-aware batching.<!-- delta:SF-2026-ARXIV-2605-23389:end --> Independent decision=`Integrate`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-23389:end -->

<!-- books-review:SF-2026-ARXIV-2605-23414:start -->
<!-- existing:SF-2026-ARXIV-2605-23414:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23414:end -->
<!-- delta:SF-2026-ARXIV-2605-23414:start -->To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility.<!-- delta:SF-2026-ARXIV-2605-23414:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-23414:end -->

<!-- books-review:SF-2026-ARXIV-2605-23454:start -->
<!-- existing:SF-2026-ARXIV-2605-23454:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23454:end -->
<!-- delta:SF-2026-ARXIV-2605-23454:start -->We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale.<!-- delta:SF-2026-ARXIV-2605-23454:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-23454:end -->

<!-- books-review:SF-2026-ARXIV-2605-23464:start -->
<!-- existing:SF-2026-ARXIV-2605-23464:start -->现有安全章没有区分可协作训练/推理的 protocol-visible state 与不得 materialize 的 weight state。<!-- existing:SF-2026-ARXIV-2605-23464:end -->
<!-- delta:SF-2026-ARXIV-2605-23464:start -->We introduce Unextractable Protocol Models (UPMs): a training and inference framework that leverages the sharded model setup to ensure model shards (i.e., subsets) held by participants are incompatible at different time steps.<!-- delta:SF-2026-ARXIV-2605-23464:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23464:end -->

<!-- books-review:SF-2026-ARXIV-2605-23493:start -->
<!-- existing:SF-2026-ARXIV-2605-23493:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23493:end -->
<!-- delta:SF-2026-ARXIV-2605-23493:start -->In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout.<!-- delta:SF-2026-ARXIV-2605-23493:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-23493:end -->

<!-- books-review:SF-2026-ARXIV-2605-23574:start -->
<!-- existing:SF-2026-ARXIV-2605-23574:start -->正文已覆盖 durable state、recovery、verification、workflow artifact 与 step-level effect receipt。 本 family 的具体机制 `We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23574:end -->
<!-- delta:SF-2026-ARXIV-2605-23574:start -->We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items.<!-- delta:SF-2026-ARXIV-2605-23574:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=7f7eae6d8d7e338dcabc560ffb2cfd50c173f0b680ad44fbde5bf434e38fa32e。
<!-- books-review:SF-2026-ARXIV-2605-23574:end -->

<!-- books-review:SF-2026-ARXIV-2605-23590:start -->
<!-- existing:SF-2026-ARXIV-2605-23590:start -->正文已覆盖 durable state、recovery、verification、workflow artifact 与 step-level effect receipt。 本 family 的具体机制 `We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23590:end -->
<!-- delta:SF-2026-ARXIV-2605-23590:start -->We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference.<!-- delta:SF-2026-ARXIV-2605-23590:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=7f7eae6d8d7e338dcabc560ffb2cfd50c173f0b680ad44fbde5bf434e38fa32e。
<!-- books-review:SF-2026-ARXIV-2605-23590:end -->

<!-- books-review:SF-2026-ARXIV-2605-23628:start -->
<!-- existing:SF-2026-ARXIV-2605-23628:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23628:end -->
<!-- delta:SF-2026-ARXIV-2605-23628:start -->Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate.<!-- delta:SF-2026-ARXIV-2605-23628:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23628:end -->

<!-- books-review:SF-2026-ARXIV-2605-23640:start -->
<!-- existing:SF-2026-ARXIV-2605-23640:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23640:end -->
<!-- delta:SF-2026-ARXIV-2605-23640:start -->Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests.<!-- delta:SF-2026-ARXIV-2605-23640:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23640:end -->

<!-- books-review:SF-2026-ARXIV-2605-23657:start -->
<!-- existing:SF-2026-ARXIV-2605-23657:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23657:end -->
<!-- delta:SF-2026-ARXIV-2605-23657:start -->In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves.<!-- delta:SF-2026-ARXIV-2605-23657:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23657:end -->

<!-- books-review:SF-2026-ARXIV-2605-23701:start -->
<!-- existing:SF-2026-ARXIV-2605-23701:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23701:end -->
<!-- delta:SF-2026-ARXIV-2605-23701:start -->We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on.<!-- delta:SF-2026-ARXIV-2605-23701:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23701:end -->

<!-- books-review:SF-2026-ARXIV-2605-23723:start -->
<!-- existing:SF-2026-ARXIV-2605-23723:start -->正文已覆盖 memory write/read、reflective retrieval、provenance、rollback 与 lifecycle evaluation。 本 family 的具体机制 `We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23723:end -->
<!-- delta:SF-2026-ARXIV-2605-23723:start -->We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents.<!-- delta:SF-2026-ARXIV-2605-23723:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=f09fd5d839379ade75d2834c66aa9ce5c2eb4b2acac0e2773be3054d41222be0。
<!-- books-review:SF-2026-ARXIV-2605-23723:end -->

<!-- books-review:SF-2026-ARXIV-2605-23764:start -->
<!-- existing:SF-2026-ARXIV-2605-23764:start -->正文已覆盖 Expert Parallel、topology、heterogeneous execution、routing replay 与 distributed-state correctness。 本 family 的具体机制 `Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23764:end -->
<!-- delta:SF-2026-ARXIV-2605-23764:start -->Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training.<!-- delta:SF-2026-ARXIV-2605-23764:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4f93d876e7023721408d2cb9a84c868ecf7049796c99bb18d430ffb936337560。
<!-- books-review:SF-2026-ARXIV-2605-23764:end -->

<!-- books-review:SF-2026-ARXIV-2605-23856:start -->
<!-- existing:SF-2026-ARXIV-2605-23856:start -->正文已覆盖 action-conditioned transition、rollout identity、attack surface、fallback 与 world-state evaluation。 本 family 的具体机制 `We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23856:end -->
<!-- delta:SF-2026-ARXIV-2605-23856:start -->We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer.<!-- delta:SF-2026-ARXIV-2605-23856:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3。
<!-- books-review:SF-2026-ARXIV-2605-23856:end -->

<!-- books-review:SF-2026-ARXIV-2605-23893:start -->
<!-- existing:SF-2026-ARXIV-2605-23893:start -->现有 MoE 与 pretraining parameterization 未完整覆盖 expert width/count 改变时的超参数迁移与 scaling identity。<!-- existing:SF-2026-ARXIV-2605-23893:end -->
<!-- delta:SF-2026-ARXIV-2605-23893:start -->We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks.<!-- delta:SF-2026-ARXIV-2605-23893:end --> Independent decision=`Integrate`；owner_sha256=3eaf93101db6b0f4fb7aa292a3e610b6fc1cc14af84e385edd9b2c7d115de79d。
<!-- books-review:SF-2026-ARXIV-2605-23893:end -->

<!-- books-review:SF-2026-ARXIV-2605-23899:start -->
<!-- existing:SF-2026-ARXIV-2605-23899:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23899:end -->
<!-- delta:SF-2026-ARXIV-2605-23899:start -->However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail.<!-- delta:SF-2026-ARXIV-2605-23899:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23899:end -->

<!-- books-review:SF-2026-ARXIV-2605-23904:start -->
<!-- existing:SF-2026-ARXIV-2605-23904:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23904:end -->
<!-- delta:SF-2026-ARXIV-2605-23904:start -->Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.<!-- delta:SF-2026-ARXIV-2605-23904:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23904:end -->

<!-- books-review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->
<!-- existing:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->`books/part-07-agent/77-memory.md` 已以更一般的 AGENT-MEMORY 演进链承载 `The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end -->
<!-- delta:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:start -->We introduce Counterfactual Composition Testing, which identifies the causal entry with 87.5% accuracy and zero false positives, while a forensics baseline fails across all 25 scenarios.<!-- delta:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-THE-MISATTRIBUTION-GAP-WHEN-MEMORY-POISONING-LOOKS-LIKE-MODEL-FAILURE-IN:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260525-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260525 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260525-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260525-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=56；selected=3；all others retain completed reviews | passed |
| SA-20260525-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=441；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260525/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260525/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-25.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
