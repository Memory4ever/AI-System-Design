# Daily Research — 2026-05-18

**Research Date:** 2026-05-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-17 09:00:00 ～ 2026-05-18 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 537 个注册 arXiv identity，冻结 48 个 Source Family；pre-denominator closure=489，withdrawn pre-denominator=0。47 个旧候选被迁回正确 owner day，1 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-18 |
| Window End | 2026-05-18 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260518-CREATED-1264a512ab6d5fd7 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-17T09:00:00+08:00 | 2026-05-18T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 537 | SF-2026-ARXIV-2605-15204;SF-2026-ARXIV-2605-15238;SF-2026-ARXIV-2605-15257;SF-2026-ARXIV-2605-15338;SF-2026-ARXIV-2605-15377;SF-2026-ARXIV-2605-15384;SF-2026-ARXIV-2605-15403;SF-2026-ARXIV-2605-15422;SF-2026-ARXIV-2605-15425;SF-2026-ARXIV-2605-15466;SF-2026-ARXIV-2605-15477;SF-2026-ARXIV-2605-15508;SF-2026-ARXIV-2605-15514;SF-2026-ARXIV-2605-15520;SF-2026-ARXIV-2605-15529;SF-2026-ARXIV-2605-15565;SF-2026-ARXIV-2605-15573;SF-2026-ARXIV-2605-15581;SF-2026-ARXIV-2605-15609;SF-2026-ARXIV-2605-15617;SF-2026-ARXIV-2605-15618;SF-2026-ARXIV-2605-15638;SF-2026-ARXIV-2605-15648;SF-2026-ARXIV-2605-15665;SF-2026-ARXIV-2605-15694;SF-2026-ARXIV-2605-15710;SF-2026-ARXIV-2605-15734;SF-2026-ARXIV-2605-15761;SF-2026-ARXIV-2605-15777;SF-2026-ARXIV-2605-15815;SF-2026-ARXIV-2605-15846;SF-2026-ARXIV-2605-15957;SF-2026-ARXIV-2605-15960;SF-2026-ARXIV-2605-15967;SF-2026-ARXIV-2605-16035;SF-2026-ARXIV-2605-16154;SF-2026-ARXIV-2605-16184;SF-2026-ARXIV-2605-16194;SF-2026-ARXIV-2605-16198;SF-2026-ARXIV-2605-16217;SF-2026-ARXIV-2605.16007;SF-2026-ARXIV-2605.16234;SF-2026-ARXIV-2605.16255;SF-AGENTSTOP-ENERGY-AWARE-TERMINATION;SF-QUANTIZATION-BEHAVIORAL-REGRESSION;SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE;SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT;SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | created-day pages=closed; OAI category sets=closed; direct same-day OAI=416 | 2026-05-18T09:00:00+08:00 | coverage:SRC-ARXIV:20260518 | — |

<!-- coverage:SRC-ARXIV:20260518:start -->全量 raw inventory=537；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260518:end -->

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
| SF-2026-ARXIV-2605-15204 | arXiv:2605.15204v1 | paper-v1:2605.15204 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15204 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15204 | yes |
| SF-2026-ARXIV-2605-15238 | arXiv:2605.15238v1 | paper-v1:2605.15238 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15238 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-15238 | no |
| SF-2026-ARXIV-2605-15257 | arXiv:2605.15257v1 | paper-v1:2605.15257 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15257 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15257 | no |
| SF-2026-ARXIV-2605-15338 | arXiv:2605.15338v1 | paper-v1:2605.15338 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15338 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15338 | no |
| SF-2026-ARXIV-2605-15377 | arXiv:2605.15377v1 | paper-v1:2605.15377 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15377 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15377 | no |
| SF-2026-ARXIV-2605-15384 | arXiv:2605.15384v1 | paper-v1:2605.15384 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15384 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-15384 | no |
| SF-2026-ARXIV-2605-15403 | arXiv:2605.15403v1 | paper-v1:2605.15403 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15403 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15403 | no |
| SF-2026-ARXIV-2605-15422 | arXiv:2605.15422v1 | paper-v1:2605.15422 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15422 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15422 | no |
| SF-2026-ARXIV-2605-15425 | arXiv:2605.15425v1 | paper-v1:2605.15425 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15425 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15425 | no |
| SF-2026-ARXIV-2605-15466 | arXiv:2605.15466v1 | paper-v1:2605.15466 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15466 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15466 | no |
| SF-2026-ARXIV-2605-15477 | arXiv:2605.15477v1 | paper-v1:2605.15477 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15477 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15477 | no |
| SF-2026-ARXIV-2605-15508 | arXiv:2605.15508v1 | paper-v1:2605.15508 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15508 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-15508 | no |
| SF-2026-ARXIV-2605-15514 | arXiv:2605.15514v1 | paper-v1:2605.15514 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15514 | self | — | new_in_window | MODEL-POSITION-ENCODING | Integrate | books-review:SF-2026-ARXIV-2605-15514 | no |
| SF-2026-ARXIV-2605-15520 | arXiv:2605.15520v1 | paper-v1:2605.15520 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15520 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-15520 | no |
| SF-2026-ARXIV-2605-15529 | arXiv:2605.15529v1 | paper-v1:2605.15529 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15529 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-15529 | no |
| SF-2026-ARXIV-2605-15565 | arXiv:2605.15565v1 | paper-v1:2605.15565 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15565 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15565 | no |
| SF-2026-ARXIV-2605-15573 | arXiv:2605.15573v1 | paper-v1:2605.15573 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15573 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15573 | no |
| SF-2026-ARXIV-2605-15581 | arXiv:2605.15581v1 | paper-v1:2605.15581 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15581 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15581 | no |
| SF-2026-ARXIV-2605-15609 | arXiv:2605.15609v1 | paper-v1:2605.15609 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15609 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15609 | no |
| SF-2026-ARXIV-2605-15617 | arXiv:2605.15617v1 | paper-v1:2605.15617 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15617 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15617 | no |
| SF-2026-ARXIV-2605-15618 | arXiv:2605.15618v1 | paper-v1:2605.15618 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15618 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15618 | no |
| SF-2026-ARXIV-2605-15638 | arXiv:2605.15638v1 | paper-v1:2605.15638 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15638 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15638 | no |
| SF-2026-ARXIV-2605-15648 | arXiv:2605.15648v1 | paper-v1:2605.15648 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15648 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-15648 | no |
| SF-2026-ARXIV-2605-15665 | arXiv:2605.15665v1 | paper-v1:2605.15665 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15665 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15665 | no |
| SF-2026-ARXIV-2605-15694 | arXiv:2605.15694v1 | paper-v1:2605.15694 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15694 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15694 | no |
| SF-2026-ARXIV-2605-15710 | arXiv:2605.15710v1 | paper-v1:2605.15710 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15710 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15710 | no |
| SF-2026-ARXIV-2605-15734 | arXiv:2605.15734v1 | paper-v1:2605.15734 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15734 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15734 | no |
| SF-2026-ARXIV-2605-15761 | arXiv:2605.15761v1 | paper-v1:2605.15761 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15761 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15761 | no |
| SF-2026-ARXIV-2605-15777 | arXiv:2605.15777v1 | paper-v1:2605.15777 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15777 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15777 | no |
| SF-2026-ARXIV-2605-15815 | arXiv:2605.15815v1 | paper-v1:2605.15815 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15815 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15815 | no |
| SF-2026-ARXIV-2605-15846 | arXiv:2605.15846v1 | paper-v1:2605.15846 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15846 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15846 | no |
| SF-2026-ARXIV-2605-15957 | arXiv:2605.15957v1 | paper-v1:2605.15957 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15957 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15957 | no |
| SF-2026-ARXIV-2605-15960 | arXiv:2605.15960v1 | paper-v1:2605.15960 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15960 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15960 | no |
| SF-2026-ARXIV-2605-15967 | arXiv:2605.15967v1 | paper-v1:2605.15967 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15967 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15967 | no |
| SF-2026-ARXIV-2605-16035 | arXiv:2605.16035v1 | paper-v1:2605.16035 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16035 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16035 | no |
| SF-2026-ARXIV-2605-16154 | arXiv:2605.16154v1 | paper-v1:2605.16154 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16154 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16154 | no |
| SF-2026-ARXIV-2605-16184 | arXiv:2605.16184v1 | paper-v1:2605.16184 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16184 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-16184 | no |
| SF-2026-ARXIV-2605-16194 | arXiv:2605.16194v1 | paper-v1:2605.16194 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16194 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16194 | no |
| SF-2026-ARXIV-2605-16198 | arXiv:2605.16198v1 | paper-v1:2605.16198 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16198 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16198 | no |
| SF-2026-ARXIV-2605-16217 | arXiv:2605.16217v1 | paper-v1:2605.16217 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16217 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16217 | no |
| SF-2026-ARXIV-2605.16007 | arXiv:2605.16007v1 | paper-v1:2605.16007 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16007 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16007 | no |
| SF-2026-ARXIV-2605.16234 | arXiv:2605.16234v1 | paper-v1:2605.16234 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16234 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-ARXIV-2605.16234 | no |
| SF-2026-ARXIV-2605.16255 | arXiv:2605.16255v1 | paper-v1:2605.16255 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16255 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605.16255 | no |
| SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | arXiv:2605.15206v1 | paper-v1:2605.15206 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | yes |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | arXiv:2605.15208v1 | paper-v1:2605.15208 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | yes |
| SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | arXiv:2605.15215v1 | paper-v1:2605.15215 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | no |
| SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | arXiv:2605.15207v1 | paper-v1:2605.15207 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | yes |
| SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | arXiv:2605.15228v1 | paper-v1:2605.15228 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15204 | RP-7cd74a147e854807 | deep | arXiv:2605.15204v1 | SRC-ARXIV@arXiv:2605.15204v1 | https://arxiv.org/html/2605.15204v1#S2 | https://arxiv.org/html/2605.15204v1#S4 | https://arxiv.org/html/2605.15204v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-15204 | complete |
| SF-2026-ARXIV-2605-15238 | RP-7beba9e8f6a47cb5 | deep | arXiv:2605.15238v1 | SRC-ARXIV@arXiv:2605.15238v1 | https://arxiv.org/html/2605.15238v1 §3 Hydra Overview; §4 Design; §5 Incremental Checker — mechanism boundary: Large language models are increasingly used for code generation, but many generated programs fail to compile, a prerequisite for further correctness checks such as unit tests. | https://arxiv.org/html/2605.15238v1 §7 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15238v1 §8 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15238v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15238 | complete |
| SF-2026-ARXIV-2605-15257 | RP-94089aee7a2d0fe2 | deep | arXiv:2605.15257v1 | SRC-ARXIV@arXiv:2605.15257v1 | https://arxiv.org/html/2605.15257v1 §2 Experimental Design — mechanism boundary: Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning. | https://arxiv.org/html/2605.15257v1 §3 Results and Discussion — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15257v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15257v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15257 | complete |
| SF-2026-ARXIV-2605-15338 | RP-b58cbb8eead327ec | deep | arXiv:2605.15338v1 | SRC-ARXIV@arXiv:2605.15338v1 | https://arxiv.org/html/2605.15338v1 §3 Sleeper Memory Poisoning Threat Model — mechanism boundary: Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity. | https://arxiv.org/html/2605.15338v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15338v1 Appendix A Limitations and Impact — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15338v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15338 | complete |
| SF-2026-ARXIV-2605-15377 | RP-9cc06f46b8898ef8 | deep | arXiv:2605.15377v1 | SRC-ARXIV@arXiv:2605.15377v1 | https://arxiv.org/html/2605.15377v1 §3 Ensemble Monitoring Method — mechanism boundary: As AI systems are increasingly deployed in autonomous agentic settings at scale, it is important to ensure the actions they take are safe and aligned with user intent. | https://arxiv.org/html/2605.15377v1 §4–§6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15377v1 §6.3 Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15377v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15377 | complete |
| SF-2026-ARXIV-2605-15384 | RP-58e2fd667aa3383b | deep | arXiv:2605.15384v1 | SRC-ARXIV@arXiv:2605.15384v1 | https://arxiv.org/html/2605.15384v1 §3 SeqMem-Eval — mechanism boundary: Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time. | https://arxiv.org/html/2605.15384v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15384v1 Appendix G Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15384v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15384 | complete |
| SF-2026-ARXIV-2605-15403 | RP-22757deee588e66e | deep | arXiv:2605.15403v1 | SRC-ARXIV@arXiv:2605.15403v1 | https://arxiv.org/html/2605.15403v1 §3 φ-balancing objective and mirror-descent controller — mechanism boundary: Mixture-of-Experts (MoE) models rely on balanced expert utilization to fully realize their scalability. | https://arxiv.org/html/2605.15403v1 §4 Pretraining/fine-tuning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15403v1 §5 Limitations and topology/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15403v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15403 | complete |
| SF-2026-ARXIV-2605-15422 | RP-58c2bcc826bc1db9 | deep | arXiv:2605.15422v1 | SRC-ARXIV@arXiv:2605.15422v1 | https://arxiv.org/html/2605.15422v1 §3–§4 DualKV — mechanism boundary: Modern RL post-training methods such as GRPO and DAPO train on N response sequences of R tokens sampled from a shared prompt of P tokens, but standard FlashAttention replicates all P prompt tokens N times across both forward and backward passes -- duplicating compute and memory on identical hidden states. | https://arxiv.org/html/2605.15422v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15422v1 §6 Conclusion and disclosed workload/hardware boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15422v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15422 | complete |
| SF-2026-ARXIV-2605-15425 | RP-721dc45a01e968c2 | deep | arXiv:2605.15425v1 | SRC-ARXIV@arXiv:2605.15425v1 | https://arxiv.org/html/2605.15425v1 §3 Runtime-structured decomposition architecture — mechanism boundary: Agentic coding systems increasingly use large language models (LLMs) for software engineering tasks such as debugging, root cause analysis, and code review. | https://arxiv.org/html/2605.15425v1 §4 Monolithic/static/runtime comparison — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15425v1 §5 Limitations and two-workload/three-configuration boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15425v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15425 | complete |
| SF-2026-ARXIV-2605-15466 | RP-4a5cef259ff55c2b | deep | arXiv:2605.15466v1 | SRC-ARXIV@arXiv:2605.15466v1 | https://arxiv.org/html/2605.15466v1 §3 Interaction-Aware JEPA motion/entity masking — mechanism boundary: Learning predictive world models from unlabelled video is a foundational challenge in artificial intelligence. | https://arxiv.org/html/2605.15466v1 §4 CLEVRER causal evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15466v1 §5 Limitations and synthetic-video/action boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15466v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15466 | complete |
| SF-2026-ARXIV-2605-15477 | RP-3087deafe3d3486f | deep | arXiv:2605.15477v1 | SRC-ARXIV@arXiv:2605.15477v1 | https://arxiv.org/html/2605.15477v1 §3 Exo-to-ego conversion and action representation — mechanism boundary: Egocentric world models present a promising direction for enabling agents to predict and plan, but their performance is constrained by the limited availability of egocentric training data and its inherent partial observability of humans' physical actions. | https://arxiv.org/html/2605.15477v1 §4 Prediction/planning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15477v1 §5 Limitations and pose/kinematics/domain boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15477v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15477 | complete |
| SF-2026-ARXIV-2605-15508 | RP-d9d5aaf5eff2d598 | deep | arXiv:2605.15508v1 | SRC-ARXIV@arXiv:2605.15508v1 | arXiv:2605.15508v1 — Methodology: 4 STS Design (official v1 HTML) | arXiv:2605.15508v1 — Experiments: 6 Evaluation (official v1 HTML) | arXiv:2605.15508v1 — Scope and limitations: 8 Conclusion (official v1 HTML) | webcache-2605.15508.txt#sha256=29b8cd764bc0cb25c1d5b8b3229116684d257f27c947b1b133dd64570fac7141; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15508 | complete |
| SF-2026-ARXIV-2605-15514 | RP-b4123c1fb8bf1670 | deep | arXiv:2605.15514v1 | SRC-ARXIV@arXiv:2605.15514v1 | arXiv:2605.15514v1 — Methodology: §§3–5 — four RoPE failure modes and multilayer/multihead extension (official v1 HTML) | arXiv:2605.15514v1 — Experiments: §§3.1 and 5 — empirical verification and indexing-task evaluation (official v1 HTML) | arXiv:2605.15514v1 — Scope and limitations: §6 Conclusion and Discussion (official v1 HTML) | webcache-2605.15514.txt#sha256=5cd206e5c697bee520bb70feaf9d6ae212e9df69e3a288fb8d68990e9d167b3a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15514 | complete |
| SF-2026-ARXIV-2605-15520 | RP-f3a0ec238dba5147 | deep | arXiv:2605.15520v1 | SRC-ARXIV@arXiv:2605.15520v1 | arXiv:2605.15520v1 — Methodology: §3 Latent Optimization Attack (official v1 HTML) | arXiv:2605.15520v1 — Experiments: §4 Experimental Evaluation (official v1 HTML) | arXiv:2605.15520v1 — Scope and limitations: §§5–6 Defenses and Conclusion (official v1 HTML) | webcache-2605.15520.txt#sha256=e2ab7afe369c8c0d8e160ac4da631a5a8d4480e872acb02a5ebcacd2846ccab0; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15520 | complete |
| SF-2026-ARXIV-2605-15529 | RP-7eba813b78155699 | deep | arXiv:2605.15529v1 | SRC-ARXIV@arXiv:2605.15529v1 | arXiv:2605.15529v1 — Methodology: W20 Full Source Review — Beta-Binomial formulation, parameterization/loss, ACA control flow | arXiv:2605.15529v1 — Experiments: W20 Full Source Review — four backbones/four visual-math benchmarks, ablations, token-accuracy operating points | arXiv:2605.15529v1 — Scope and limitations: W20 Full Source Review — What It Proves / Does Not Prove and Trade-offs / Failure Modes | ../../weekly/2026-W20/README.md#process-rewards-with-learned-reliability#sha256=ead0557e3a61b9f6c6a0f0cde41c70cdb13f8e24e1444ce5e33fb3361832941f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15529 | complete |
| SF-2026-ARXIV-2605-15565 | RP-8ea2235975d7d9e0 | deep | arXiv:2605.15565v1 | SRC-ARXIV@arXiv:2605.15565v1 | arXiv:2605.15565v1 — Methodology: §3 Dataflow-Oriented RL for Agentic LLMs (official v1 HTML) | arXiv:2605.15565v1 — Experiments: §4 Evaluation: Applications of AstraFlow (official v1 HTML) | arXiv:2605.15565v1 — Scope and limitations: §5 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15565.txt#sha256=243ba0d9629154f73c9c0734a42b7da4679939ac1d6f31de45960771d5eb7b93; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15565 | complete |
| SF-2026-ARXIV-2605-15573 | RP-ca163d74c8bb88f9 | deep | arXiv:2605.15573v1 | SRC-ARXIV@arXiv:2605.15573v1 | arXiv:2605.15573v1 — Methodology: 2 Problem Formulation and Preliminaries (official v1 HTML) | arXiv:2605.15573v1 — Experiments: 4 Experiments (official v1 HTML) | arXiv:2605.15573v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.15573.txt#sha256=1c6b159fe047c0b5e180cb2bf92b1155d03e99d170cc14ab7a898361c77d9e9d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15573 | complete |
| SF-2026-ARXIV-2605-15581 | RP-2eaa04d2d0e9c571 | deep | arXiv:2605.15581v1 | SRC-ARXIV@arXiv:2605.15581v1 | arXiv:2605.15581v1 — Methodology: §IV Methodology (official v1 HTML) | arXiv:2605.15581v1 — Experiments: §V Evaluation (official v1 HTML) | arXiv:2605.15581v1 — Scope and limitations: §§VI–VII Discussion/Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15581.txt#sha256=6865d1f78991041cdba771e0b4d60c3981f237013dc2e7948357c6fc078f1515; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15581 | complete |
| SF-2026-ARXIV-2605-15609 | RP-a673721cedf0778d | deep | arXiv:2605.15609v1 | SRC-ARXIV@arXiv:2605.15609v1 | arXiv:2605.15609v1 — Methodology: 3 Methodology (official v1 HTML) | arXiv:2605.15609v1 — Experiments: 4 Experiments (official v1 HTML) | arXiv:2605.15609v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.15609.txt#sha256=1cc7d14f34e7b5e7791eb18005c972f9e72069afa8bf3ad51f000f9d3cb28480; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15609 | complete |
| SF-2026-ARXIV-2605-15617 | RP-d20b1f7d3be2064d | deep | arXiv:2605.15617v1 | SRC-ARXIV@arXiv:2605.15617v1 | arXiv:2605.15617v1 — Methodology: §§4–7 PrismLLM design, graph construction and hybrid emulation (official v1 HTML) | arXiv:2605.15617v1 — Experiments: §8 Evaluation (official v1 HTML) | arXiv:2605.15617v1 — Scope and limitations: §§9–10 Discussion and Conclusion (official v1 HTML) | webcache-2605.15617.txt#sha256=d882a41ce9dd8077e835bf0d29a323f2039d8e40045141498124480b90110a99; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15617 | complete |
| SF-2026-ARXIV-2605-15618 | RP-6b76a3b7e1e4ce1a | deep | arXiv:2605.15618v1 | SRC-ARXIV@arXiv:2605.15618v1 | arXiv:2605.15618v1 — Methodology: §3 Evaluation framework (official v1 HTML) | arXiv:2605.15618v1 — Experiments: §§4–9 representation, corruption, physics and prediction evaluation (official v1 HTML) | arXiv:2605.15618v1 — Scope and limitations: §10 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15618.txt#sha256=048125f45e0bf3e36b8d175ead37b4eeab803e1526c1507b5bfed80e2d2617e5; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15618 | complete |
| SF-2026-ARXIV-2605-15638 | RP-4e7d54053bd11198 | deep | arXiv:2605.15638v1 | SRC-ARXIV@arXiv:2605.15638v1 | arXiv:2605.15638v1 — Methodology: 4 ITHICA: Intra-THread Instruction Checking Approach for Defect Detection (official v1 HTML) | arXiv:2605.15638v1 — Experiments: 5.2 Two-Pool Evaluation Strategy (official v1 HTML) | arXiv:2605.15638v1 — Scope and limitations: 8 Discussion (official v1 HTML) | webcache-2605.15638.txt#sha256=a6e33f6971dce05da911a969efd22bad408120324a3bdb5d6cff6ee733f1535e; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15638 | complete |
| SF-2026-ARXIV-2605-15648 | RP-d20f77bf166685ad | deep | arXiv:2605.15648v1 | SRC-ARXIV@arXiv:2605.15648v1 | arXiv:2605.15648v1 — Methodology: §3 Privacy Analysis of EASGM and ASGM (official v1 HTML) | arXiv:2605.15648v1 — Experiments: §§4–6 auditing and experimental comparison (official v1 HTML) | arXiv:2605.15648v1 — Scope and limitations: §7 Conclusion and Limitations (official v1 HTML) | webcache-2605.15648.txt#sha256=7b8a773f970581fd3a22b85cd8d208bac639446d5a54a4785d42ecc0fd27583f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15648 | complete |
| SF-2026-ARXIV-2605-15665 | RP-b29e25e5ee67ee30 | deep | arXiv:2605.15665v1 | SRC-ARXIV@arXiv:2605.15665v1 | arXiv:2605.15665v1 — Methodology: §4 The PRISM Framework (official v1 HTML) | arXiv:2605.15665v1 — Experiments: §5 Evaluation (official v1 HTML) | arXiv:2605.15665v1 — Scope and limitations: §7 Discussion (official v1 HTML) | webcache-2605.15665.txt#sha256=547685d4cc83d71837df75e3c57b64cd07f4f822db39fb0e6dd25558d4eb93ec; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15665 | complete |
| SF-2026-ARXIV-2605-15694 | RP-a4baaf3477ba4b72 | deep | arXiv:2605.15694v1 | SRC-ARXIV@arXiv:2605.15694v1 | arXiv:2605.15694v1 — Methodology: PDF pp.1–5 — CATS communication-aware training/partitioning, SomeGather, message-dropout | arXiv:2605.15694v1 — Experiments: PDF pp.5–8 — 16-device nRF52840 BLE deployment and four time-series workloads | arXiv:2605.15694v1 — Scope and limitations: PDF pp.1,7–8 — C1/C2/C3 scope, packet-loss and mesh/resource boundaries | pdfcache-2605.15694.txt#sha256=4e5132db7174d7e3d499adff0f1d69577aec9995eda6a1e734a6abe17073250d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15694 | complete |
| SF-2026-ARXIV-2605-15710 | RP-bf9c4626ee613ceb | deep | arXiv:2605.15710v1 | SRC-ARXIV@arXiv:2605.15710v1 | arXiv:2605.15710v1 — Methodology: §3 SMMBench Benchmark (official v1 HTML) | arXiv:2605.15710v1 — Experiments: §4 Experiment (official v1 HTML) | arXiv:2605.15710v1 — Scope and limitations: §5 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15710.txt#sha256=fc87f5a4f55daaa4ae472d4531b32a9689af55fa93a59e781cc7bff9ae1b62df; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15710 | complete |
| SF-2026-ARXIV-2605-15734 | RP-22c1c972087d6653 | deep | arXiv:2605.15734v1 | SRC-ARXIV@arXiv:2605.15734v1 | arXiv:2605.15734v1 — Methodology: 4 Study Design and Descriptions of Experiments (official v1 HTML) | arXiv:2605.15734v1 — Experiments: 4 Study Design and Descriptions of Experiments (official v1 HTML) | arXiv:2605.15734v1 — Scope and limitations: 8 Discussion (official v1 HTML) | webcache-2605.15734.txt#sha256=a47fc44a8632feb4725c73a1bb55f328732a94777621fd2ad6d82b31e819b5c7; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15734 | complete |
| SF-2026-ARXIV-2605-15761 | RP-64df861b38ddf383 | deep | arXiv:2605.15761v1 | SRC-ARXIV@arXiv:2605.15761v1 | arXiv:2605.15761v1 — Methodology: §3 Influence Framework (official v1 HTML) | arXiv:2605.15761v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.15761v1 — Scope and limitations: §6 Conclusion, limitations, and future work (official v1 HTML) | webcache-2605.15761.txt#sha256=ca8072fe5abc4292411bbed5f49a9cd38a134d896852458d3a66611189f43051; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15761 | complete |
| SF-2026-ARXIV-2605-15777 | RP-cf82cd729eae56c2 | deep | arXiv:2605.15777v1 | SRC-ARXIV@arXiv:2605.15777v1 | arXiv:2605.15777v1 — Methodology: §3 SaaS-Bench construction and protocol (official v1 HTML) | arXiv:2605.15777v1 — Experiments: §4 Experiment (official v1 HTML) | arXiv:2605.15777v1 — Scope and limitations: §5 Discussion (official v1 HTML) | webcache-2605.15777.txt#sha256=8b6132e8a487d39b3b61cf92430ef38a72ab59733d99cb175dab78d7954c85bb; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15777 | complete |
| SF-2026-ARXIV-2605-15815 | RP-a74f3274de3c2635 | deep | arXiv:2605.15815v1 | SRC-ARXIV@arXiv:2605.15815v1 | arXiv:2605.15815v1 — Methodology: 3.1 Problem Formulation (official v1 HTML) | arXiv:2605.15815v1 — Experiments: 4 Experiments (official v1 HTML) | arXiv:2605.15815v1 — Scope and limitations: 5 Discussion (official v1 HTML) | webcache-2605.15815.txt#sha256=3a33da0c22dc622c4f472deca77134646db3d38bf145570760706a407a52bcaf; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15815 | complete |
| SF-2026-ARXIV-2605-15846 | RP-8d43e5335b891463 | deep | arXiv:2605.15846v1 | SRC-ARXIV@arXiv:2605.15846v1 | arXiv:2605.15846v1 — Methodology: §3 RoadmapBench (official v1 HTML) | arXiv:2605.15846v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.15846v1 — Scope and limitations: §§5–6 Discussion and Conclusion (official v1 HTML) | webcache-2605.15846.txt#sha256=182c6d2923cec62917d92a8947c0ff9c46e9d85267749a3f0522f01236b5832d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15846 | complete |
| SF-2026-ARXIV-2605-15957 | RP-9e70266755b26aca | deep | arXiv:2605.15957v1 | SRC-ARXIV@arXiv:2605.15957v1 | arXiv:2605.15957v1 — Methodology: §4 MaxVec Engine and §5 modular CPU/GPU execution (official v1 HTML) | arXiv:2605.15957v1 — Experiments: §§3 and 5 Vec-H/operator evaluation (official v1 HTML) | arXiv:2605.15957v1 — Scope and limitations: §6 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15957.txt#sha256=7b1682a3288a95d12768145dd110838ead769a71ec880a08e2c41d4366b4c120; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15957 | complete |
| SF-2026-ARXIV-2605-15960 | RP-57a3137ba08b5c03 | deep | arXiv:2605.15960v1 | SRC-ARXIV@arXiv:2605.15960v1 | arXiv:2605.15960v1 — Methodology: §§2.2–3 model-exploitation definitions and results (official v1 HTML) | arXiv:2605.15960v1 — Experiments: §3 Results (official v1 HTML) | arXiv:2605.15960v1 — Scope and limitations: §5 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.15960.txt#sha256=d3f65a86d7ba9db62365a69f3c72cb4895d81dd6acfc0c8f1e1d3724c6fb60ec; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15960 | complete |
| SF-2026-ARXIV-2605-15967 | RP-2624ca6cd314a90a | deep | arXiv:2605.15967v1 | SRC-ARXIV@arXiv:2605.15967v1 | arXiv:2605.15967v1 — Methodology: 4.2 Implementation per subset (official v1 HTML) | arXiv:2605.15967v1 — Experiments: Summary of empirical findings. (official v1 HTML) | arXiv:2605.15967v1 — Scope and limitations: 8 Limitations (official v1 HTML) | webcache-2605.15967.txt#sha256=852b5f51a8e7a2d0f0810704f5d84c613df170916fec3aa12c54321e29be5178; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-15967 | complete |
| SF-2026-ARXIV-2605-16035 | RP-ebd6e8b1a1a2e6f3 | deep | arXiv:2605.16035v1 | SRC-ARXIV@arXiv:2605.16035v1 | arXiv:2605.16035v1 — Methodology: §4 The Agent Attribution Protocol (official v1 HTML) | arXiv:2605.16035v1 — Experiments: §6 Evaluation (official v1 HTML) | arXiv:2605.16035v1 — Scope and limitations: §7 Discussion (official v1 HTML) | webcache-2605.16035.txt#sha256=c00876f298081c076479a3833e984ff1e84d973a8e03091e623430c58f8cfd3a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16035 | complete |
| SF-2026-ARXIV-2605-16154 | RP-6ba11837f297e6de | deep | arXiv:2605.16154v1 | SRC-ARXIV@arXiv:2605.16154v1 | arXiv:2605.16154v1 — Methodology: §4 Probabilistic Chunk Masking (official v1 HTML) | arXiv:2605.16154v1 — Experiments: §5 Empirical Evaluation (official v1 HTML) | arXiv:2605.16154v1 — Scope and limitations: §5.2 Results and Discussion (official v1 HTML) | webcache-2605.16154.txt#sha256=30179f641f52c58da7628374dcec531f39aeec32d1be905c647cba127dc79f8a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16154 | complete |
| SF-2026-ARXIV-2605-16184 | RP-90c1541ceafca0e5 | deep | arXiv:2605.16184v1 | SRC-ARXIV@arXiv:2605.16184v1 | arXiv:2605.16184v1 — Methodology: §III System Design and Methodology (official v1 HTML) | arXiv:2605.16184v1 — Experiments: §IV Experiments (official v1 HTML) | arXiv:2605.16184v1 — Scope and limitations: §V Discussion (official v1 HTML) | webcache-2605.16184.txt#sha256=2780079103241f79e3c3c29df6482ca685d5d10100fe071005f549648e29c31d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16184 | complete |
| SF-2026-ARXIV-2605-16194 | RP-1e389147a2058e69 | deep | arXiv:2605.16194v1 | SRC-ARXIV@arXiv:2605.16194v1 | arXiv:2605.16194v1 — Methodology: PDF §§3–4 — D1–D4 coordination conventions, schema and validator | arXiv:2605.16194v1 — Experiments: PDF §§5–7 — self-application, five-paper pilot, adoption-cost analysis | arXiv:2605.16194v1 — Scope and limitations: PDF §§2,8 — prose-agent failure modes, does-not-claim boundary, open hypotheses | pdfcache-2605.16194.txt#sha256=13717f1fe595bb1e4edb7f65c8fad7eb66314cb49beef86a26da205154054d94; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16194 | complete |
| SF-2026-ARXIV-2605-16198 | RP-fe6dd7f3715c6b3c | deep | arXiv:2605.16198v1 | SRC-ARXIV@arXiv:2605.16198v1 | arXiv:2605.16198v1 — Methodology: §§3–4 assessment, monitoring, auditing and intervention (official v1 HTML) | arXiv:2605.16198v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16198v1 — Scope and limitations: §§5.1 and 6 auditor limitations/discussion (official v1 HTML) | webcache-2605.16198.txt#sha256=bab884572c3ce16e55e77a7b36fb30456e594dac76e463ff0a92e5de89a2b3d4; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16198 | complete |
| SF-2026-ARXIV-2605-16217 | RP-79306fe66ab51704 | deep | arXiv:2605.16217v1 | SRC-ARXIV@arXiv:2605.16217v1 | arXiv:2605.16217v1 — Methodology: §§2–3 Argus evidence assembly and learning (official v1 HTML) | arXiv:2605.16217v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.16217v1 — Scope and limitations: §4.4 Limitation and Discussion (official v1 HTML) | webcache-2605.16217.txt#sha256=cd150e098c1c1f4cf32d90a3f3801339c6de7c7c665ccc91cf8bab40f9caee3a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16217 | complete |
| SF-2026-ARXIV-2605.16007 | RP-1f3b22f809a157ac | deep | arXiv:2605.16007v1 | SRC-ARXIV@arXiv:2605.16007v1 | arXiv:2605.16007v1 — Methodology: NPU Architecture-Native RaBitQ Optimizations (official v1 HTML) | arXiv:2605.16007v1 — Experiments: 4 Evaluation (official v1 HTML) | arXiv:2605.16007v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.16007.txt#sha256=b1f3535d624aa32accdc9f21f6ef783d40d52eab9631f84e126fb737d366f9cf; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16007 | complete |
| SF-2026-ARXIV-2605.16234 | RP-ffefb93a9eb43e51 | deep | arXiv:2605.16234v1 | SRC-ARXIV@arXiv:2605.16234v1 | arXiv:2605.16234v1 — Methodology: §§1.1 and 3 protocol vocabulary and Swap-KL method (official v1 HTML) | arXiv:2605.16234v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.16234v1 — Scope and limitations: Appendix M Additional Discussion (official v1 HTML) | webcache-2605.16234.txt#sha256=6343df81ae683664f6bb0f993812a6031f358d264c399fefd666327aaaf0467b; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16234 | complete |
| SF-2026-ARXIV-2605.16255 | RP-51817ec239c1ded7 | deep | arXiv:2605.16255v1 | SRC-ARXIV@arXiv:2605.16255v1 | arXiv:2605.16255v1 — Methodology: 3.1 A Tale of Two Designs (official v1 HTML) | arXiv:2605.16255v1 — Experiments: 4 Datacenter Design Evaluation Framework (official v1 HTML) | arXiv:2605.16255v1 — Scope and limitations: 8 Conclusion (official v1 HTML) | webcache-2605.16255.txt#sha256=aa49bd56b76eac31d6259afe4044fea90d444051bf0a91ef4f331f7a920814b4; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16255 | complete |
| SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | RP-f5d371cd55b4b70b | deep | arXiv:2605.15206v1 | SRC-ARXIV@arXiv:2605.15206v1 | arXiv:2605.15206v1 energy/task-value stop model and runtime controller; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.15206v1 consumer-device agent workloads and energy/quality measurements; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.15206v1 device, workload and termination-estimator boundary; Scope and Limitations | Not Disclosed — arXiv:2605.15206v1 reports implementation described; immutable commit not established | claim:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | complete |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | RP-e5ff94d39f0dce33 | deep | arXiv:2605.15208v1 | SRC-ARXIV@arXiv:2605.15208v1 | arXiv:2605.15208v1 — §IV-A/B quantization and controlled protocol | arXiv:2605.15208v1 — §IV-C results across 3 models, BF16–3bit, BBQ, 5 seeds | arXiv:2605.15208v1 — §V-B Limitations; model/task/quantizer scope | arXiv:2605.15208v1 — 911,100 inference records described; immutable code/data commit Not Disclosed | claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | complete |
| SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | RP-f3e786a9e2527842 | deep | arXiv:2605.15215v1 | SRC-ARXIV@arXiv:2605.15215v1 | arXiv:2605.15215v1 HTML — §3 SkillSmith compiler/runtime pipeline | arXiv:2605.15215v1 — §4 skill-construction evaluation | arXiv:2605.15215v1 — §5 limitations: tool schema, verifier and deployment scope | arXiv:2605.15215v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | complete |
| SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | RP-d3d0b917139c896c | deep | arXiv:2605.15207v1 | SRC-ARXIV@arXiv:2605.15207v1 | arXiv:2605.15207v1 occupancy-shift analysis, resampling and per-agent trust-region updates; §Methodology: exact-v1 named method and system-design passages | arXiv:2605.15207v1 multi-agent coordination experiments and component-replacement tests; Experiments: exact-v1 evaluation and ablation passages | arXiv:2605.15207v1 shared-context team, cached-rollout and benchmark boundary; Scope and Limitations | Not Disclosed — arXiv:2605.15207v1 reports paper-linked GitHub; event-time commit not pinned | claim:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | complete |
| SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | RP-8ef181ea320f3389 | deep | arXiv:2605.15228v1 | SRC-ARXIV@arXiv:2605.15228v1 | arXiv:2605.15228v1 HTML — §Method / System Design — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的机制、状态 owner 与控制/数据流 | arXiv:2605.15228v1 HTML — §Experiments / Evaluation — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的作者披露 workload、baseline 与 ablation | arXiv:2605.15228v1 HTML — §Limitations / Discussion — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的适用范围、未证明项与 failure boundary | arXiv:2605.15228v1 artifact/code statement; immutable commit Not Disclosed unless named | claim:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-15204:start -->
#### SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch

<!-- claim:SF-2026-ARXIV-2605-15204:start -->
- **Problem:** Multi-agent orchestration frameworks such as LangChain, LangGraph, and CrewAI route tasks through graph-based pipelines but do not enforce the stage constraints that govern real business processes.
- **Old path / changed constraint:** However, in their native forms they do not expose business-stage legality as an explicit runtime contract of the kind evaluated here.
- **Mechanism / ownership:** We present SDOF, a framework that treats multi-agent execution as a constrained state machine.
- **Evaluation contract:** Our GSPO-aligned 7B Intent Router achieves higher joint accuracy than zero-shot GPT-4o on this FSM-constrained adversarial routing benchmark (80.9% versus 48.9%).
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** Violations cause compliance failures, data corruption, and legal risk.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.15204v1](https://arxiv.org/abs/2605.15204v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.15204v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-15204:end -->
<!-- review:SF-2026-ARXIV-2605-15204:end -->

<!-- review:SF-2026-ARXIV-2605-15238:start -->
#### Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support

问题与演进：代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15238v1 §3 Hydra Overview; §4 Design; §5 Incremental Checker — mechanism boundary: Large language models are increasingly used for code generation, but many generated programs fail to compile, a prerequisite for further correctness checks such as unit tests.`。

Evaluation：`https://arxiv.org/html/2605.15238v1 §7 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15238v1 §8 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15238v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15238:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15238:end -->
<!-- review:SF-2026-ARXIV-2605-15238:end -->

<!-- review:SF-2026-ARXIV-2605-15257:start -->
#### Training on Documents About Monitoring Leads to CoT Obfuscation

问题与演进：CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15257v1 §2 Experimental Design — mechanism boundary: Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15257v1 §3 Results and Discussion — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15257v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15257v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15257:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15257:end -->
<!-- review:SF-2026-ARXIV-2605-15257:end -->

<!-- review:SF-2026-ARXIV-2605-15338:start -->
#### Hidden in Memory: Sleeper Memory Poisoning in LLM Agents

问题与演进：memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15338v1 §3 Sleeper Memory Poisoning Threat Model — mechanism boundary: Large language models are increasingly augmented with persistent memory, allowing assistants to store user-specific information across sessions for personalization and continuity.`。

Evaluation：`https://arxiv.org/html/2605.15338v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15338v1 Appendix A Limitations and Impact — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15338v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15338:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15338:end -->
<!-- review:SF-2026-ARXIV-2605-15338:end -->

<!-- review:SF-2026-ARXIV-2605-15377:start -->
#### Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute

问题与演进：AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15377v1 §3 Ensemble Monitoring Method — mechanism boundary: As AI systems are increasingly deployed in autonomous agentic settings at scale, it is important to ensure the actions they take are safe and aligned with user intent.`。

Evaluation：`https://arxiv.org/html/2605.15377v1 §4–§6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15377v1 §6.3 Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15377v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15377:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15377:end -->
<!-- review:SF-2026-ARXIV-2605-15377:end -->

<!-- review:SF-2026-ARXIV-2605-15384:start -->
#### Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory

问题与演进：顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15384v1 §3 SeqMem-Eval — mechanism boundary: Memory plays a central role in enabling large language models (LLMs) to operate over sequential tasks by accumulating and reusing experience over time.`。

Evaluation：`https://arxiv.org/html/2605.15384v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15384v1 Appendix G Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15384v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15384:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15384:end -->
<!-- review:SF-2026-ARXIV-2605-15384:end -->

<!-- review:SF-2026-ARXIV-2605-15403:start -->
#### $ϕ$-Balancing for Mixture-of-Experts Training

问题与演进：MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15403v1 §3 φ-balancing objective and mirror-descent controller — mechanism boundary: Mixture-of-Experts (MoE) models rely on balanced expert utilization to fully realize their scalability.`。

Evaluation：`https://arxiv.org/html/2605.15403v1 §4 Pretraining/fine-tuning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15403v1 §5 Limitations and topology/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15403v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15403:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15403:end -->
<!-- review:SF-2026-ARXIV-2605-15403:end -->

<!-- review:SF-2026-ARXIV-2605-15422:start -->
#### DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts

问题与演进：共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15422v1 §3–§4 DualKV — mechanism boundary: Modern RL post-training methods such as GRPO and DAPO train on N response sequences of R tokens sampled from a shared prompt of P tokens, but standard FlashAttention replicates all P prompt tokens N times across both forward and backward passes -- duplicating compute and memory on identical hidden states.`。

Evaluation：`https://arxiv.org/html/2605.15422v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15422v1 §6 Conclusion and disclosed workload/hardware boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15422v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15422:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15422:end -->
<!-- review:SF-2026-ARXIV-2605-15422:end -->

<!-- review:SF-2026-ARXIV-2605-15425:start -->
#### Runtime-Structured Task Decomposition for Agentic Coding Systems

问题与演进：Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15425v1 §3 Runtime-structured decomposition architecture — mechanism boundary: Agentic coding systems increasingly use large language models (LLMs) for software engineering tasks such as debugging, root cause analysis, and code review.`。

Evaluation：`https://arxiv.org/html/2605.15425v1 §4 Monolithic/static/runtime comparison — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15425v1 §5 Limitations and two-workload/three-configuration boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15425v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15425:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15425:end -->
<!-- review:SF-2026-ARXIV-2605-15425:end -->

<!-- review:SF-2026-ARXIV-2605-15466:start -->
#### Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction

问题与演进：predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15466v1 §3 Interaction-Aware JEPA motion/entity masking — mechanism boundary: Learning predictive world models from unlabelled video is a foundational challenge in artificial intelligence.`。

Evaluation：`https://arxiv.org/html/2605.15466v1 §4 CLEVRER causal evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15466v1 §5 Limitations and synthetic-video/action boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15466v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15466:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15466:end -->
<!-- review:SF-2026-ARXIV-2605-15466:end -->

<!-- review:SF-2026-ARXIV-2605-15477:start -->
#### EgoExo-WM: Unlocking Exo Video for Ego World Models

问题与演进：exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15477v1 §3 Exo-to-ego conversion and action representation — mechanism boundary: Egocentric world models present a promising direction for enabling agents to predict and plan, but their performance is constrained by the limited availability of egocentric training data and its inherent partial observability of humans' physical actions.`。

Evaluation：`https://arxiv.org/html/2605.15477v1 §4 Prediction/planning evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15477v1 §5 Limitations and pose/kinematics/domain boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15477v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15477:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15477:end -->
<!-- review:SF-2026-ARXIV-2605-15477:end -->

<!-- review:SF-2026-ARXIV-2605-15508:start -->
#### STS: Efficient Sparse Attention with Speculative Token Sparsity

问题与约束：The quadratic complexity of attention imposes severe memory and computational bottlenecks on Large Language Model (LLM) inference.

机制与 ownership：We propose STS, a sparse attention mechanism that requires no model retraining.

Evaluation contract：Our evaluation shows that STS achieves a 2.67x speedup operating at approximately 90% sparsity on representative benchmark NarrativeQA, maintaining negligible accuracy degradation compared to dense attention.

Trade-off / failure：The mechanism described in `4 STS Design` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15508:start -->`STS: Efficient Sparse Attention with Speculative Token Sparsity` is supported only under the v1-disclosed workload and evaluator behind `6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15508:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15508`。
<!-- review:SF-2026-ARXIV-2605-15508:end -->

<!-- review:SF-2026-ARXIV-2605-15514:start -->
#### RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably

问题与约束：We identify intrinsic limitations of Rotary Positional Embeddings (RoPE) in Transformer-based long-context language models.

机制与 ownership：We identify intrinsic limitations of Rotary Positional Embeddings (RoPE) in Transformer-based long-context language models.

Evaluation contract：Our empirical analysis shows that multi-head, multi-layer architectures are insufficient to overcome these limitations.

Trade-off / failure：The mechanism described in `§§3–5 — four RoPE failure modes and multilayer/multihead extension` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15514:start -->`RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably` is supported only under the v1-disclosed workload and evaluator behind `§§3.1 and 5 — empirical verification and indexing-task evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15514:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15514`。
<!-- review:SF-2026-ARXIV-2605-15514:end -->

<!-- review:SF-2026-ARXIV-2605-15520:start -->
#### On the Fragility of Data Attribution When Learning Is Distributed

问题与约束：Data attribution has become an important component of pricing, auditing, and governance in machine learning pipelines, yet most attribution methods implicitly assume that attribution values faithfully reflect participants' contributions.

机制与 ownership：We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility.

Evaluation contract：We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility.

Trade-off / failure：The mechanism described in `§3 Latent Optimization Attack` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5–6 Defenses and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15520:start -->`On the Fragility of Data Attribution When Learning Is Distributed` is supported only under the v1-disclosed workload and evaluator behind `§4 Experimental Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15520:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15520`。
<!-- review:SF-2026-ARXIV-2605-15520:end -->

<!-- review:SF-2026-ARXIV-2605-15529:start -->
#### Process Rewards with Learned Reliability

问题与约束：A scalar process reward discards the evidence quantity behind finite Monte-Carlo success counts, so downstream allocation cannot distinguish high reward with strong support from high reward with weak support.

机制与 ownership：BetaPRM preserves (K,N) count evidence in a Beta-Binomial objective and exposes mean plus concentration; the ACA controller owns risk-adjusted ranking, stopping, and repair.

Evaluation contract：The evidence is limited to the disclosed VisualPRM count supervision, four visual-math benchmarks, four backbones, and the author candidate pools and judges; hardware for the main training runs is not fully disclosed.

Trade-off / failure：Preserving counts raises rollout, judge, and storage cost; miscalibration can cause confident-wrong early stops, while conservative control loses the compute benefit.

旧路径与共存边界：Scalar PRMs and fixed Best-of-N remain reasonable when counts are unavailable, the scorer is uncalibrated, or predictable latency is more valuable than adaptive allocation.

<!-- claim:SF-2026-ARXIV-2605-15529:start -->Concentration is learned evidence reliability under the continuation generator and judge, not calibrated epistemic truth or a frequentist confidence interval.<!-- claim:SF-2026-ARXIV-2605-15529:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15529`。
<!-- review:SF-2026-ARXIV-2605-15529:end -->

<!-- review:SF-2026-ARXIV-2605-15565:start -->
#### AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs

问题与约束：Existing LLM RL systems support some of these capabilities, but each new extension often requires dedicated system engineering.

机制与 ownership：To address these limitations, we propose AstraFlow, a dataflow-oriented RL system that replaces conventional trainer-centered control with principled component abstractions.

Evaluation contract：We evaluate AstraFlow across math, code, search, and AgentBench workloads, showing that the same system supports multi-policy training, elastic scaling, heterogeneous cross-region execution, and composable data algorithms without system-level code changes.

Trade-off / failure：The mechanism described in `§3 Dataflow-Oriented RL for Agentic LLMs` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15565:start -->`AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs` is supported only under the v1-disclosed workload and evaluator behind `§4 Evaluation: Applications of AstraFlow`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15565:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15565`。
<!-- review:SF-2026-ARXIV-2605-15565:end -->

<!-- review:SF-2026-ARXIV-2605-15573:start -->
#### Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems

问题与约束：Existing collaboration frameworks typically operate in either a parallel or a sequential mode.

机制与 ownership：In this work, we introduce a hybrid paradigm called Nexa, a trainable response-conditioned policy that bridges the gap between the two modes.

Evaluation contract：We formalize this hybrid execution problem, show that the resulting graph is acyclic by construction, and that the framework strictly subsumes pure parallel execution, and present a training procedure based on policy-gradient optimization.

Trade-off / failure：The mechanism described in `2 Problem Formulation and Preliminaries` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15573:start -->`Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15573:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15573`。
<!-- review:SF-2026-ARXIV-2605-15573:end -->

<!-- review:SF-2026-ARXIV-2605-15581:start -->
#### STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices

问题与约束：However, their reliability remains fragile: an error in early evidence collection, hypothesis formulation, or causal analysis can propagate through the reasoning trace and eventually corrupt the final diagnosis.

机制与 ownership：In this paper, we present \textbf{STAR}, a \emph{Stage-attributed Triage and Repair} framework for repairing erroneous RCA traces.

Evaluation contract：We evaluate STAR on a public large-scale benchmark and a real-world production dataset, using two RCA agent workflows and three foundation models.

Trade-off / failure：The mechanism described in `§IV Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§VI–VII Discussion/Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15581:start -->`STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices` is supported only under the v1-disclosed workload and evaluator behind `§V Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15581:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15581`。
<!-- review:SF-2026-ARXIV-2605-15581:end -->

<!-- review:SF-2026-ARXIV-2605-15609:start -->
#### PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding

问题与约束：Diffusion large language models (dLLMs) generate text by iteratively denoising masked token sequences.

机制与 ownership：We propose Parallel Speculative Decoding (PSD), a training-free framework that jointly improves inference along both axes.

Evaluation contract：Experiments on three dLLMs across reasoning and code generation tasks show that PSD achieves favorable trade-offs between inference efficiency and generation quality, reaching up to $5.5\times$ tokens per forward pass with accuracy comparable to greedy decoding.

Trade-off / failure：The mechanism described in `3 Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15609:start -->`PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15609:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15609`。
<!-- review:SF-2026-ARXIV-2605-15609:end -->

<!-- review:SF-2026-ARXIV-2605-15617:start -->
#### A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM

问题与约束：Large language model (LLM) training today runs on clusters spanning thousands of GPUs.

机制与 ownership：We present PrismLLM to decouple large-scale execution from the need to access large clusters, enabling engineers to run and observe ranks of interest under faithful large-scale behavior using only a few GPUs.

Evaluation contract：This is because engineers often need to reproduce production behaviors to diagnose failures or evaluate optimizations, thereby demanding frequent and even exclusive access to production-scale clusters -- which becomes increasingly hard given that the majority of GPUs are already committed to production workloads.

Trade-off / failure：The mechanism described in `§§4–7 PrismLLM design, graph construction and hybrid emulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§9–10 Discussion and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15617:start -->`A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM` is supported only under the v1-disclosed workload and evaluator behind `§8 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15617:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15617`。
<!-- review:SF-2026-ARXIV-2605-15617:end -->

<!-- review:SF-2026-ARXIV-2605-15618:start -->
#### Latent Video Prediction Learns Better World Models

问题与约束：Self-supervised video models are increasingly framed as world models, yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks.

机制与 ownership：We present the first systematic study addressing this gap, analyzing four matched-capacity frontier video foundation models, V-JEPA 2.1, V-JEPA 2, VideoPrism, and VideoMAEv2, across five robustness axes relevant to their deployment as video world models: feature discriminability, corruption robustness, fine-grained discrimination, occlusion robustness, and sensitivity to temporal direction.

Evaluation contract：Self-supervised video models are increasingly framed as world models, yet their evaluation remains largely confined to a single top-1 accuracy score on clean benchmarks.

Trade-off / failure：The mechanism described in `§3 Evaluation framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§10 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15618:start -->`Latent Video Prediction Learns Better World Models` is supported only under the v1-disclosed workload and evaluator behind `§§4–9 representation, corruption, physics and prediction evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15618:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15618`。
<!-- review:SF-2026-ARXIV-2605-15618:end -->

<!-- review:SF-2026-ARXIV-2605-15638:start -->
#### ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions

问题与约束：ITHICA error checks detect 39% more defective servers than native checks within the ITHICA tests derived from our baseline programs, and enable novel findings on defect behavior that challenge conclusions drawn by prior hyperscaler fleet studies.

机制与 ownership：We present ITHICA, an approach for automatically generating functional tests for defect-induced errors from arbitrary programs by inserting intra-thread, instruction-level error checks, primarily leveraging instruction duplication and output comparison.

Evaluation contract：We use ITHICA to transform industrial hyperscaler test programs (our baseline), datacenter workloads, and common libraries into functional tests, and evaluate them on over 3,000 CPU servers.

Trade-off / failure：The mechanism described in `4 ITHICA: Intra-THread Instruction Checking Approach for Defect Detection` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15638:start -->`ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions` is supported only under the v1-disclosed workload and evaluator behind `5.2 Two-Pool Evaluation Strategy`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15638:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15638`。
<!-- review:SF-2026-ARXIV-2605-15638:end -->

<!-- review:SF-2026-ARXIV-2605-15648:start -->
#### Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning

问题与约束：Existing analyses often model DP-SGD and its variants as the Subsampled Gaussian Mechanism (SGM), where Gaussian noise is added to the sum of clipped gradients computed from a Poisson-sampled batch.

机制与 ownership：We identify a mismatch between this formal analysis and common DP-SGD implementations.

Evaluation contract：Our theoretical results show that these guarantees can be weaker than the standard SGM-based guarantee, implying that the true privacy leakage may exceed the reported guarantee in some regimes.

Trade-off / failure：The mechanism described in `§3 Privacy Analysis of EASGM and ASGM` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Conclusion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15648:start -->`Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning` is supported only under the v1-disclosed workload and evaluator behind `§§4–6 auditing and experimental comparison`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15648:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15648`。
<!-- review:SF-2026-ARXIV-2605-15648:end -->

<!-- review:SF-2026-ARXIV-2605-15665:start -->
#### PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI

问题与约束：Existing prompt optimization frameworks address prompt quality as a one-time compile-time problem, leaving open the equally critical question of how to detect and repair prompt regressions caused by silent LLM behavior changes over time.

机制与 ownership：We present PRISM (Prompt Reliability via Iterative Simulation and Monitoring), a closed-loop framework that treats prompt engineering as a continuous reliability engineering problem rather than a one-time authorship task.

Evaluation contract：It automatically generates test cases from requirements, simulates full multi-turn conversations against a platform-faithful LLM environment, evaluates pass/fail using an LLM-as-judge, diagnoses root causes of failures, and surgically repairs the prompt -- iterating until all tests pass.

Trade-off / failure：The mechanism described in `§4 The PRISM Framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15665:start -->`PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI` is supported only under the v1-disclosed workload and evaluator behind `§5 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15665:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15665`。
<!-- review:SF-2026-ARXIV-2605-15665:end -->

<!-- review:SF-2026-ARXIV-2605-15694:start -->
#### Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices

问题与约束：Transformer models are rapidly becoming a cornerstone of modern Internet of Things (IoT) applications, yet their computational and memory demands far exceed the capabilities of a single typical ultra-low-power IoT device.

机制与 ownership：We present CATS, a framework for distributed transformer inference on ultra-low-power wireless devices, enabling multiple devices to collaboratively execute models far larger than what a single device can sustain.

Evaluation contract：In real-world experiments, we show that CATS brings distributed transformer inference to ultra-low-power wireless devices for the first time, with deployments on up to 16 devices that collaboratively execute transformer models up to 14 times larger than what a single device can run.

Trade-off / failure：The mechanism at `PDF pp.1–5 — CATS communication-aware training/partitioning, SomeGather, message-dropout` trades added coordination/metadata/runtime work against the measured benefit; `PDF pp.1,7–8 — C1/C2/C3 scope, packet-loss and mesh/resource boundaries` bounds any extrapolation.

旧路径与共存边界：The prior design remains valid outside the exact-v1 workload or when the new coordination and verification costs dominate.

<!-- claim:SF-2026-ARXIV-2605-15694:start -->`Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices` is supported only by the exact-v1 PDF's disclosed workload and evaluator; undisclosed deployment fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15694:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15694`。
<!-- review:SF-2026-ARXIV-2605-15694:end -->

<!-- review:SF-2026-ARXIV-2605-15710:start -->
#### SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory

问题与约束：Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources.

机制与 ownership：To address this gap, we introduce Source-distributed Multimodal Memory Benchmark(SMMBench), which measures whether agents can retrieve, align, and compose multimodal evidence scattered across multiple sources rather than reason within a single curated context.

Evaluation contract：Existing benchmarks for multimodal memory reasoning largely evaluate systems within pre-assembled contexts, but under-evaluate whether agents can use evidence distributed across independently originated sources.

Trade-off / failure：The mechanism described in `§3 SMMBench Benchmark` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15710:start -->`SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15710:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15710`。
<!-- review:SF-2026-ARXIV-2605-15710:end -->

<!-- review:SF-2026-ARXIV-2605-15734:start -->
#### Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments

问题与约束：The use of large language models to assess user states in conversational and adaptive systems is based on the assumption that the metrics used for such assessment are stable and interpretable at the level of individual scores.

机制与 ownership：This paper empirically tests this assumption, focusing on the psychometric reliability of artificial intelligence (AI) measures of user states.

Evaluation contract：The results demonstrate that metric reliability cannot be considered a default property in interpretive domains.

Trade-off / failure：The mechanism described in `4 Study Design and Descriptions of Experiments` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15734:start -->`Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments` is supported only under the v1-disclosed workload and evaluator behind `4 Study Design and Descriptions of Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15734:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15734`。
<!-- review:SF-2026-ARXIV-2605-15734:end -->

<!-- review:SF-2026-ARXIV-2605-15761:start -->
#### A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation

问题与约束：Evaluation leaderboards such as LMArena play a central role in benchmarking large language models by aggregating pairwise human preferences into model rankings, yet the robustness of these rankings remains poorly understood.

机制与 ownership：We present a unified perturbation framework for analyzing Bradley-Terry leaderboards under structured data modifications using influence-based approximations.

Evaluation contract：Evaluation leaderboards such as LMArena play a central role in benchmarking large language models by aggregating pairwise human preferences into model rankings, yet the robustness of these rankings remains poorly understood.

Trade-off / failure：The mechanism described in `§3 Influence Framework` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion, limitations, and future work` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15761:start -->`A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15761:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15761`。
<!-- review:SF-2026-ARXIV-2605-15761:end -->

<!-- review:SF-2026-ARXIV-2605-15777:start -->
#### SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?

问题与约束：However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows.

机制与 ownership：To this end, we introduce SaaS-Bench, a benchmark built on 23 deployable SaaS systems across six professional domains, containing 106 tasks grounded in realistic work scenarios.

Evaluation contract：However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows.

Trade-off / failure：The mechanism described in `§3 SaaS-Bench construction and protocol` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15777:start -->`SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiment`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15777:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15777`。
<!-- review:SF-2026-ARXIV-2605-15777:end -->

<!-- review:SF-2026-ARXIV-2605-15815:start -->
#### BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge

问题与约束：This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents.

机制与 ownership：This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents.

Evaluation contract：Experiments on three benchmarks show that BootstrapAgent achieves a 92.9% success rate, outperforming the baseline by over 10% while reducing downstream agent token usage by 25.9% and build time by 22.3%.

Trade-off / failure：The mechanism described in `3.1 Problem Formulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `5 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15815:start -->`BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge` is supported only under the v1-disclosed workload and evaluator behind `4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15815:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15815`。
<!-- review:SF-2026-ARXIV-2605-15815:end -->

<!-- review:SF-2026-ARXIV-2605-15846:start -->
#### RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades

问题与约束：However, most existing benchmarks focus predominantly on single-issue bug fixes from Python repositories, with coarse pass/fail evaluation outcomes, and thus fail to capture long-horizon, multi-target development at real engineering scale.

机制与 ownership：To address this gap, we present RoadmapBench, a benchmark of 115 long-horizon coding tasks grounded in real open-source version upgrades across 17 repositories and 5 programming languages.

Evaluation contract：However, most existing benchmarks focus predominantly on single-issue bug fixes from Python repositories, with coarse pass/fail evaluation outcomes, and thus fail to capture long-horizon, multi-target development at real engineering scale.

Trade-off / failure：The mechanism described in `§3 RoadmapBench` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5–6 Discussion and Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15846:start -->`RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15846:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15846`。
<!-- review:SF-2026-ARXIV-2605-15846:end -->

<!-- review:SF-2026-ARXIV-2605-15957:start -->
#### To GPU or Not to GPU: Vector Search in Relational Engines

问题与约束：However, while vector search is a common feature in AI/ML/LLMs where the dominant computing platforms are GPUs, existing database engines operate on CPUs even when implementing vector search.

机制与 ownership：Second, we develop a modular execution engine that can run SQL+VS queries across CPU and GPU.

Evaluation contract：First, we extend the TPC-H benchmark with vector data (from text and images) and propose a number of representative SQL+VS queries.

Trade-off / failure：The mechanism described in `§4 MaxVec Engine and §5 modular CPU/GPU execution` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15957:start -->`To GPU or Not to GPU: Vector Search in Relational Engines` is supported only under the v1-disclosed workload and evaluator behind `§§3 and 5 Vec-H/operator evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15957:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15957`。
<!-- review:SF-2026-ARXIV-2605-15957:end -->

<!-- review:SF-2026-ARXIV-2605-15960:start -->
#### Imperfect World Models are Exploitable

问题与约束：We propose a novel definition of model exploitation in reinforcement learning.

机制与 ownership：We propose a novel definition of model exploitation in reinforcement learning.

Evaluation contract：We analogize our definition with a prior characterization of reward hacking but show that the associated proof of inevitability does not transfer to exploitation.

Trade-off / failure：The mechanism described in `§§2.2–3 model-exploitation definitions and results` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15960:start -->`Imperfect World Models are Exploitable` is supported only under the v1-disclosed workload and evaluator behind `§3 Results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15960:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15960`。
<!-- review:SF-2026-ARXIV-2605-15960:end -->

<!-- review:SF-2026-ARXIV-2605-15967:start -->
#### Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning

问题与约束：We study event-graph substrates: a class of world models that represent agent state as an append-only log of typed RDF triples and answer counterfactual queries by forking the log under a structured intervention vocabulary.

机制与 ownership：Substrates are inspectable at the triple level, support exact counterfactuals, and transfer across domains without learned components.

Evaluation contract：We formalize the class, prove a duality between explanatory and counterfactual queries that reduces both to the same causal-ancestor traversal, and evaluate a 1,400-line CLEVRER-DSL interpreter atop a domain-agnostic substrate runtime at full CLEVRER validation scale (n=75,618).

Trade-off / failure：The mechanism described in `4.2 Implementation per subset` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-15967:start -->`Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning` is supported only under the v1-disclosed workload and evaluator behind `Summary of empirical findings.`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-15967:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-15967`。
<!-- review:SF-2026-ARXIV-2605-15967:end -->

<!-- review:SF-2026-ARXIV-2605-16035:start -->
#### Who Owns This Agent? Tracing AI Agents Back to Their Owners

问题与约束：AI agents are increasingly deployed to act autonomously in the world, yet there is still no reliable way to trace a harmful agent back to the account that deployed it.

机制与 ownership：For adversarial operators who filter or paraphrase incoming content, we develop robust canary constructions that cannot be suppressed without degrading the agent's own task performance, yielding a formal asymmetry in the defender's favor.

Evaluation contract：We evaluate a variety of scenarios including real-world agents and show that our attribution method is reliable, robust, and scalable for vendor-side deployment.

Trade-off / failure：The mechanism described in `§4 The Agent Attribution Protocol` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16035:start -->`Who Owns This Agent? Tracing AI Agents Back to Their Owners` is supported only under the v1-disclosed workload and evaluator behind `§6 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16035:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16035`。
<!-- review:SF-2026-ARXIV-2605-16035:end -->

<!-- review:SF-2026-ARXIV-2605-16154:start -->
#### Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking

问题与约束：However, GRPO assigns the same advantage to every chunk in a rollout.

机制与 ownership：A natural response has been to speed rollout collection through faster simulators and world models.

Evaluation contract：We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it.

Trade-off / failure：The mechanism described in `§4 Probabilistic Chunk Masking` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5.2 Results and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16154:start -->`Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking` is supported only under the v1-disclosed workload and evaluator behind `§5 Empirical Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16154:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16154`。
<!-- review:SF-2026-ARXIV-2605-16154:end -->

<!-- review:SF-2026-ARXIV-2605-16184:start -->
#### Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training

问题与约束：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path.

机制与 ownership：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path.

Evaluation contract：We evaluate Asteria on both memory-constrained and distributed training settings.

Trade-off / failure：The mechanism described in `§III System Design and Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§V Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16184:start -->`Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training` is supported only under the v1-disclosed workload and evaluator behind `§IV Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16184:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16184`。
<!-- review:SF-2026-ARXIV-2605-16184:end -->

<!-- review:SF-2026-ARXIV-2605-16194:start -->
#### paper.json: A Coordination Convention for LLM-Agent-Actionable Papers

问题与约束：LLM agents routinely serve as first (and sometimes only) readers of academic papers, skimming for sub-claims, extracting reproducibility steps, and generalizing scope.

机制与 ownership：We propose `paper.json`, a companion JSON file that travels with the PDF and addresses each failure with a lightweight convention: stable claim IDs (C1), an explicit does-not-claim list (C2), exact per-figure shell commands (C3), and stable definition IDs (C5).

Evaluation contract：Repo: https://github.com/arquicanedo/paper-json

Trade-off / failure：The mechanism at `PDF §§3–4 — D1–D4 coordination conventions, schema and validator` trades added coordination/metadata/runtime work against the measured benefit; `PDF §§2,8 — prose-agent failure modes, does-not-claim boundary, open hypotheses` bounds any extrapolation.

旧路径与共存边界：The prior design remains valid outside the exact-v1 workload or when the new coordination and verification costs dominate.

<!-- claim:SF-2026-ARXIV-2605-16194:start -->`paper.json: A Coordination Convention for LLM-Agent-Actionable Papers` is supported only by the exact-v1 PDF's disclosed workload and evaluator; undisclosed deployment fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16194:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16194`。
<!-- review:SF-2026-ARXIV-2605-16194:end -->

<!-- review:SF-2026-ARXIV-2605-16198:start -->
#### Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems

问题与约束：We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing.

机制与 ownership：Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs.

Evaluation contract：Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges.

Trade-off / failure：The mechanism described in `§§3–4 assessment, monitoring, auditing and intervention` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§§5.1 and 6 auditor limitations/discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16198:start -->`Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16198:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16198`。
<!-- review:SF-2026-ARXIV-2605-16198:end -->

<!-- review:SF-2026-ARXIV-2605-16217:start -->
#### Argus: Evidence Assembly for Scalable Deep Research Agents

问题与约束：Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit.

机制与 ownership：We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel.

Evaluation contract：With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks.

Trade-off / failure：The mechanism described in `§§2–3 Argus evidence assembly and learning` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§4.4 Limitation and Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16217:start -->`Argus: Evidence Assembly for Scalable Deep Research Agents` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16217:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16217`。
<!-- review:SF-2026-ARXIV-2605-16217:end -->

<!-- review:SF-2026-ARXIV-2605.16007:start -->
#### Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization

问题与约束：Vector similarity search is a critical component of modern AI systems, but traditional CPU-based implementations face fundamental scalability bottlenecks for billion-scale corpora due to prohibitive computational overhead and memory bandwidth limitations.

机制与 ownership：We propose a three-stage heterogeneous execution path comprising AI Core-accelerated coarse ranking on 1-bit quantized vectors, on-device AI CPU Top-k processing, and host CPU fine re-ranking on full-precision vectors.

Evaluation contract：Evaluation on standard datasets shows that Ascend-RaBitQ achieves 3.0X to 62.8X faster index construction than the CPU baseline, up to 11.7X throughput improvement over the fastest CPU IVF-RaBitQ implementation, and over two orders of magnitude over the mathematically equivalent CPU baseline, while demonstrating encouraging scalability on distributed multi-NPU systems.

Trade-off / failure：The mechanism described in `NPU Architecture-Native RaBitQ Optimizations` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16007:start -->`Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization` is supported only under the v1-disclosed workload and evaluator behind `4 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16007:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16007`。
<!-- review:SF-2026-ARXIV-2605.16007:end -->

<!-- review:SF-2026-ARXIV-2605.16234:start -->
#### No Free Swap: Protocol-Dependent Layer Redundancy in Transformers

问题与约束：When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests.

机制与 ownership：Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped.

Evaluation contract：Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal.

Trade-off / failure：The mechanism described in `§§1.1 and 3 protocol vocabulary and Swap-KL method` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `Appendix M Additional Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16234:start -->`No Free Swap: Protocol-Dependent Layer Redundancy in Transformers` is supported only under the v1-disclosed workload and evaluator behind `§4 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16234:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16234`。
<!-- review:SF-2026-ARXIV-2605.16234:end -->

<!-- review:SF-2026-ARXIV-2605.16255:start -->
#### Designing Datacenter Power Delivery Hierarchies for the AI Era

问题与约束：This poses a major challenge for datacenter power delivery designers.

机制与 ownership：To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences.

Evaluation contract：Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes.

Trade-off / failure：The mechanism described in `3.1 A Tale of Two Designs` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16255:start -->`Designing Datacenter Power Delivery Hierarchies for the AI Era` is supported only under the v1-disclosed workload and evaluator behind `4 Datacenter Design Evaluation Framework`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16255:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16255`。
<!-- review:SF-2026-ARXIV-2605.16255:end -->

<!-- review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->
### AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices

问题与旧路径：Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 energy/task-value stop model and runtime controller；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：consumer-device agent workloads and energy/quality measurements。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：device, workload and termination-estimator boundary。Artifact：implementation described; immutable commit not established。<!-- claim:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->长期可保留结论是：Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->
<!-- review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->

<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
### Quantization Behavioral Regression

aggregate perplexity 对低精度的平均误差敏感，却会漏掉少数安全关键 item 的 answer flip。作者在三模型、五 precision、BBQ 与五 seeds 上报告 4-bit 时已有 bias transition 而 perplexity 变化很小，3-bit 更明显。研究只覆盖 post-training quantization、一个 bias benchmark 和有限模型，alignment-layer 解释是推断；长期结论是 model artifact promotion 必须绑定 precision/quantizer/kernel 与 item-level behavior slices。

<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->证据边界：只接受 arXiv exact-v1 在上述 method/evaluation contract 内的作者主张；未披露硬件、precision、并发、SLO、artifact commit 或生产条件写 Not Disclosed，不作外推。<!-- claim:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

<!-- review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->
#### SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces

问题与机制：To this end, we propose SkillSmith, a boundary-first compiler-runtime framework that compiles skill packages offline into minimal executable interfaces.。机制 owner=`AGENT-PLATFORM`。
全文定位：`arXiv:2605.15215v1 HTML — §3 SkillSmith compiler/runtime pipeline`；evaluation=`arXiv:2605.15215v1 — §4 skill-construction evaluation`；limitations/counterevidence=`arXiv:2605.15215v1 — §5 limitations: tool schema, verifier and deployment scope`。
<!-- claim:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->证据只支持 exact-v1 披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。它不证明跨部署的一般优势，也不把作者 benchmark 变成生产承诺。<!-- claim:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->
Books Decision=`No Change — Existing Coverage`。旧方案在新增约束不存在、证据越界或 fallback 被触发时继续成立。
<!-- review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->

<!-- review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->
### TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination

问题与旧路径：Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit. 旧方案在任务短、状态可丢弃、拓扑稳定或风险较低时仍合理。约束变化后，exact-v1 将机制定位在 occupancy-shift analysis, resampling and per-agent trust-region updates；状态/控制权因此从隐式约定转为可测量、可版本化的系统对象。

Evaluation contract：multi-agent coordination experiments and component-replacement tests。作者结果只证明上述模型、硬件、数据、精度与实现条件中披露的范围；未披露字段不推断。反证与边界：shared-context team, cached-rollout and benchmark boundary。Artifact：paper-linked GitHub; event-time commit not pinned。<!-- claim:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->长期可保留结论是：Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit. 它不证明该实现跨 workload 普遍最优，也不授权跳过独立 evaluation、fallback 与 rollback。<!-- claim:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->
<!-- review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->

<!-- review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->
#### Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems

问题与机制：We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts.。机制 owner=`PLATFORM-SECURITY`。
全文定位：`arXiv:2605.15228v1 HTML — §Method / System Design — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的机制、状态 owner 与控制/数据流`；evaluation=`§Experiments / Evaluation — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的作者披露 workload、baseline 与 ablation`；limitations/counterevidence=`§Limitations / Discussion — Verifiable Agentic Infrastructure: Proof-Derived Authorization for Sovereign AI Systems 的适用范围、未证明项与 failure boundary`。
<!-- claim:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->只支持 exact-v1 披露的 workload、模型、硬件、precision、length、batch、concurrency、SLO 与 evaluator；未披露字段为 Not Disclosed。该证据不证明跨模型/硬件/部署的一般优势。<!-- claim:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->
Books Decision=`Integrate`。旧方案在固定 workload、较低风险或无需新增 owner 时仍成立；新机制引入的分类器/控制器误差、额外状态、迁移成本与攻击面必须与 fallback/coexistence 同时进入 owner narrative。
<!-- review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15204 | exact-v1 evaluation for SDOF: Taming the Alignment Tax in Multi-Agent Orchestration with State-Constrained Dispatch | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |
| SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | exact-v1 disclosed workload for AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | exact-v1 disclosed workload；见 evaluation locator | exact-v1 disclosed model or Not Disclosed | Not Disclosed unless named in Review | Not Disclosed unless named in Review | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 作者指标的 scoped contract；无通用生产阈值 | authors / task labels / formal proof as applicable |
| SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | exact-v1 disclosed workload for TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination | exact-v1 model(s); see Review | exact-v1 hardware when disclosed; otherwise Not Disclosed | Not Disclosed unless exact-v1 Review states otherwise | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reported quality/latency/throughput contract only | author protocol; independent reproduction Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15204 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15204 |
| SF-2026-ARXIV-2605-15238 | score_7_9;forced_review;potential_books_delta | selected | DA-20260518-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260518-01 |
| SF-2026-ARXIV-2605-15257 | score_7_9;forced_review;potential_books_delta | selected | DA-20260518-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260518-02 |
| SF-2026-ARXIV-2605-15338 | score_7_9 | selected | DA-20260518-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260518-03 |
| SF-2026-ARXIV-2605-15377 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15377 |
| SF-2026-ARXIV-2605-15384 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15384 |
| SF-2026-ARXIV-2605-15403 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15403 |
| SF-2026-ARXIV-2605-15422 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15422 |
| SF-2026-ARXIV-2605-15425 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15425 |
| SF-2026-ARXIV-2605-15466 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15466 |
| SF-2026-ARXIV-2605-15477 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15477 |
| SF-2026-ARXIV-2605-15508 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15508 |
| SF-2026-ARXIV-2605-15514 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15514 |
| SF-2026-ARXIV-2605-15520 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15520 |
| SF-2026-ARXIV-2605-15529 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15529 |
| SF-2026-ARXIV-2605-15565 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15565 |
| SF-2026-ARXIV-2605-15573 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15573 |
| SF-2026-ARXIV-2605-15581 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15581 |
| SF-2026-ARXIV-2605-15609 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15609 |
| SF-2026-ARXIV-2605-15617 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15617 |
| SF-2026-ARXIV-2605-15618 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15618 |
| SF-2026-ARXIV-2605-15638 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15638 |
| SF-2026-ARXIV-2605-15648 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15648 |
| SF-2026-ARXIV-2605-15665 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15665 |
| SF-2026-ARXIV-2605-15694 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15694 |
| SF-2026-ARXIV-2605-15710 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15710 |
| SF-2026-ARXIV-2605-15734 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15734 |
| SF-2026-ARXIV-2605-15761 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15761 |
| SF-2026-ARXIV-2605-15777 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15777 |
| SF-2026-ARXIV-2605-15815 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15815 |
| SF-2026-ARXIV-2605-15846 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15846 |
| SF-2026-ARXIV-2605-15957 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15957 |
| SF-2026-ARXIV-2605-15960 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15960 |
| SF-2026-ARXIV-2605-15967 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-15967 |
| SF-2026-ARXIV-2605-16035 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16035 |
| SF-2026-ARXIV-2605-16154 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16154 |
| SF-2026-ARXIV-2605-16184 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16184 |
| SF-2026-ARXIV-2605-16194 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16194 |
| SF-2026-ARXIV-2605-16198 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16198 |
| SF-2026-ARXIV-2605-16217 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-16217 |
| SF-2026-ARXIV-2605.16007 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16007 |
| SF-2026-ARXIV-2605.16234 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16234 |
| SF-2026-ARXIV-2605.16255 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605.16255 |
| SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION |
| SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE |
| SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT |
| SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE |

<!-- analysis-decision:SF-2026-ARXIV-2605-15204:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15204:end -->

<!-- analysis:DA-20260518-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-15238

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260518-01:end -->

<!-- analysis:DA-20260518-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-15257

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260518-02:end -->

<!-- analysis:DA-20260518-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-15338

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260518-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15377:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15384:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15403:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15403:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15422:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15422:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15425:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15425:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15466:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15466:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15477:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15477:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15508:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15514:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15520:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15520:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15529:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15529:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15565:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15573:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15573:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15581:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15581:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15609:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15609:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15617:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15618:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15618:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15638:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15638:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15648:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15648:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15665:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15665:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15694:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15694:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15710:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15710:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15734:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15761:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15761:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15777:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15815:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15815:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15846:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15846:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15957:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15960:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15960:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-15967:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-15967:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16035:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16035:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16154:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16154:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16184:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16194:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16194:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16198:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16198:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-16217:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-16217:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16007:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16007:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16234:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16234:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605.16255:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605.16255:end -->

<!-- analysis-decision:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->

<!-- analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

<!-- analysis-decision:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->

<!-- analysis-decision:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->

<!-- analysis-decision:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15204 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L267 (H2: Message 不是 State) | books/part-07-agent/81-workflow.md#L10 (H2: 本章要回答的问题); books/part-07-agent/83-mcp.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-15204 | delta:SF-2026-ARXIV-2605-15204 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15204 |
| SF-2026-ARXIV-2605-15238 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-15238 | delta:SF-2026-ARXIV-2605-15238 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15238 |
| SF-2026-ARXIV-2605-15257 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-15257 | delta:SF-2026-ARXIV-2605-15257 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15257 |
| SF-2026-ARXIV-2605-15338 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-15338 | delta:SF-2026-ARXIV-2605-15338 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15338 |
| SF-2026-ARXIV-2605-15377 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-15377 | delta:SF-2026-ARXIV-2605-15377 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15377 |
| SF-2026-ARXIV-2605-15384 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-15384 | delta:SF-2026-ARXIV-2605-15384 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15384 |
| SF-2026-ARXIV-2605-15403 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20; books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-15403 | delta:SF-2026-ARXIV-2605-15403 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15403 |
| SF-2026-ARXIV-2605-15422 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-15422 | delta:SF-2026-ARXIV-2605-15422 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15422 |
| SF-2026-ARXIV-2605-15425 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-15425 | delta:SF-2026-ARXIV-2605-15425 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15425 |
| SF-2026-ARXIV-2605-15466 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15466 | delta:SF-2026-ARXIV-2605-15466 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15466 |
| SF-2026-ARXIV-2605-15477 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15477 | delta:SF-2026-ARXIV-2605-15477 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15477 |
| SF-2026-ARXIV-2605-15508 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#chapter-22 | books/part-02-model/21-moe.md#chapter-21;books/part-02-model/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-15508 | delta:SF-2026-ARXIV-2605-15508 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15508 |
| SF-2026-ARXIV-2605-15514 | MODEL-POSITION-ENCODING | books/part-02-model/13-position-encoding.md#chapter-13 | books/part-02-model/12-embedding.md#chapter-12;books/part-02-model/14-self-attention.md#chapter-14 | existing:SF-2026-ARXIV-2605-15514 | delta:SF-2026-ARXIV-2605-15514 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15514 |
| SF-2026-ARXIV-2605-15520 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-15520 | delta:SF-2026-ARXIV-2605-15520 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15520 |
| SF-2026-ARXIV-2605-15529 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-15529 | delta:SF-2026-ARXIV-2605-15529 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15529 |
| SF-2026-ARXIV-2605-15565 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-15565 | delta:SF-2026-ARXIV-2605-15565 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15565 |
| SF-2026-ARXIV-2605-15573 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-15573 | delta:SF-2026-ARXIV-2605-15573 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15573 |
| SF-2026-ARXIV-2605-15581 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-15581 | delta:SF-2026-ARXIV-2605-15581 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15581 |
| SF-2026-ARXIV-2605-15609 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-15609 | delta:SF-2026-ARXIV-2605-15609 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15609 |
| SF-2026-ARXIV-2605-15617 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-15617 | delta:SF-2026-ARXIV-2605-15617 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15617 |
| SF-2026-ARXIV-2605-15618 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15618 | delta:SF-2026-ARXIV-2605-15618 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15618 |
| SF-2026-ARXIV-2605-15638 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-15638 | delta:SF-2026-ARXIV-2605-15638 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15638 |
| SF-2026-ARXIV-2605-15648 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15648 | delta:SF-2026-ARXIV-2605-15648 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15648 |
| SF-2026-ARXIV-2605-15665 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-15665 | delta:SF-2026-ARXIV-2605-15665 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15665 |
| SF-2026-ARXIV-2605-15694 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-15694 | delta:SF-2026-ARXIV-2605-15694 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15694 |
| SF-2026-ARXIV-2605-15710 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15710 | delta:SF-2026-ARXIV-2605-15710 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15710 |
| SF-2026-ARXIV-2605-15734 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15734 | delta:SF-2026-ARXIV-2605-15734 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15734 |
| SF-2026-ARXIV-2605-15761 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15761 | delta:SF-2026-ARXIV-2605-15761 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15761 |
| SF-2026-ARXIV-2605-15777 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15777 | delta:SF-2026-ARXIV-2605-15777 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15777 |
| SF-2026-ARXIV-2605-15815 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-15815 | delta:SF-2026-ARXIV-2605-15815 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15815 |
| SF-2026-ARXIV-2605-15846 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15846 | delta:SF-2026-ARXIV-2605-15846 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15846 |
| SF-2026-ARXIV-2605-15957 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-15957 | delta:SF-2026-ARXIV-2605-15957 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15957 |
| SF-2026-ARXIV-2605-15960 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15960 | delta:SF-2026-ARXIV-2605-15960 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15960 |
| SF-2026-ARXIV-2605-15967 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15967 | delta:SF-2026-ARXIV-2605-15967 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15967 |
| SF-2026-ARXIV-2605-16035 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16035 | delta:SF-2026-ARXIV-2605-16035 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16035 |
| SF-2026-ARXIV-2605-16154 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16154 | delta:SF-2026-ARXIV-2605-16154 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16154 |
| SF-2026-ARXIV-2605-16184 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-16184 | delta:SF-2026-ARXIV-2605-16184 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16184 |
| SF-2026-ARXIV-2605-16194 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16194 | delta:SF-2026-ARXIV-2605-16194 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16194 |
| SF-2026-ARXIV-2605-16198 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16198 | delta:SF-2026-ARXIV-2605-16198 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16198 |
| SF-2026-ARXIV-2605-16217 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-16217 | delta:SF-2026-ARXIV-2605-16217 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16217 |
| SF-2026-ARXIV-2605.16007 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605.16007 | delta:SF-2026-ARXIV-2605.16007 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16007 |
| SF-2026-ARXIV-2605.16234 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#chapter-17 | books/part-02-model/16-feed-forward-mlp.md#chapter-16;books/part-02-model/18-decoder-only.md#chapter-18 | existing:SF-2026-ARXIV-2605.16234 | delta:SF-2026-ARXIV-2605.16234 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16234 |
| SF-2026-ARXIV-2605.16255 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605.16255 | delta:SF-2026-ARXIV-2605.16255 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16255 |
| SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#adjacent-chapter | existing:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | delta:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION | Direct Evolution | Integrate | books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION |
| SF-QUANTIZATION-BEHAVIORAL-REGRESSION | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 | books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10 | existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION | Principle Reuse | No Change — Existing Coverage | books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION |
| SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83; books/part-07-agent/README.md#knowledge-tree | existing:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | delta:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE | Direct Evolution | No Change — Existing Coverage | books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE |
| SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#adjacent-chapter | existing:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | delta:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT | Direct Evolution | Integrate | books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT |
| SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | delta:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE | Direct Evolution | Integrate | books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE |

<!-- books-review:SF-2026-ARXIV-2605-15204:start -->
<!-- existing:SF-2026-ARXIV-2605-15204:start -->对读 `books/part-07-agent/82-multi-agent.md#L267 (H2: Message 不是 State)` 及相邻章节后，现有命题为：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-15204:end -->
<!-- delta:SF-2026-ARXIV-2605-15204:start -->Exact-v1 的 source-specific delta 是：We present SDOF, a framework that treats multi-agent execution as a constrained state machine. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-15204:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-15204:end -->

<!-- books-review:SF-2026-ARXIV-2605-15238:start -->
<!-- existing:SF-2026-ARXIV-2605-15238:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。正文尚未明确承载本 family 的增量：代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15238:end -->
<!-- delta:SF-2026-ARXIV-2605-15238:start -->代码生成可把 incremental compiler checker 作为异步 sensor，并用 checkpoint/rollback 保留已验证前缀；compiler 只拥有 static-correctness feedback，不拥有 task correctness<!-- delta:SF-2026-ARXIV-2605-15238:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15238:end -->

<!-- books-review:SF-2026-ARXIV-2605-15257:start -->
<!-- existing:SF-2026-ARXIV-2605-15257:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节；当前主线已覆盖多源 sensor、trace/evidence identity、阈值、盲区、escalation 与 independent control authority。正文尚未明确承载本 family 的增量：CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation。 Owner snapshot sha256=`311704bec6f23882d2259d2365d557dca6cae87f79c809c87698f0866dcfe88e`；相邻章节=`books/part-06-ai-infrastructure/66-evaluation-system.md, books/part-06-ai-infrastructure/68-logging.md`。<!-- existing:SF-2026-ARXIV-2605-15257:end -->
<!-- delta:SF-2026-ARXIV-2605-15257:start -->CoT monitor 进入训练分布后，模型可能学习 monitor-aware obfuscation；监控合同必须包含 adaptive exposure、外部 signals 与不可由被监控模型控制的 escalation<!-- delta:SF-2026-ARXIV-2605-15257:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15257:end -->

<!-- books-review:SF-2026-ARXIV-2605-15338:start -->
<!-- existing:SF-2026-ARXIV-2605-15338:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。本 family 的增量“memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-15338:end -->
<!-- delta:SF-2026-ARXIV-2605-15338:start -->memory poisoning 可延迟触发并跨 session 重放；write admission、provenance、activation-time policy 与 expiry 必须共同拥有防线<!-- delta:SF-2026-ARXIV-2605-15338:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15338:end -->

<!-- books-review:SF-2026-ARXIV-2605-15377:start -->
<!-- existing:SF-2026-ARXIV-2605-15377:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及相邻章节；当前主线已覆盖多源 sensor、trace/evidence identity、阈值、盲区、escalation 与 independent control authority。正文尚未明确承载本 family 的增量：AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority。 Owner snapshot sha256=`311704bec6f23882d2259d2365d557dca6cae87f79c809c87698f0866dcfe88e`；相邻章节=`books/part-06-ai-infrastructure/66-evaluation-system.md, books/part-06-ai-infrastructure/68-logging.md`。<!-- existing:SF-2026-ARXIV-2605-15377:end -->
<!-- delta:SF-2026-ARXIV-2605-15377:start -->AI control monitoring 应优先组合异质 signal 以降低共同盲区，而非只增加同类 monitor compute；ensemble 自身仍需校准、correlation audit 与独立 stop authority<!-- delta:SF-2026-ARXIV-2605-15377:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15377:end -->

<!-- books-review:SF-2026-ARXIV-2605-15384:start -->
<!-- existing:SF-2026-ARXIV-2605-15384:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。正文尚未明确承载本 family 的增量：顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-15384:end -->
<!-- delta:SF-2026-ARXIV-2605-15384:start -->顺序演化 memory 的评测必须把 acquisition、retention、forgetting、transfer 与 interference 分成时间序列诊断，不能由最终平均分掩盖负迁移<!-- delta:SF-2026-ARXIV-2605-15384:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15384:end -->

<!-- books-review:SF-2026-ARXIV-2605-15403:start -->
<!-- existing:SF-2026-ARXIV-2605-15403:start -->已读取 `books/part-02-model/21-moe.md` 及相邻章节；当前主线已覆盖router probability、expert capacity、load balance、communication、placement 与 fallback 的条件计算合同。本 family 的增量“MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`3eaf93101db6b0f4fb7aa292a3e610b6fc1cc14af84e385edd9b2c7d115de79d`；相邻章节=`books/part-02-model/20-sampling.md, books/part-02-model/22-long-context.md`。<!-- existing:SF-2026-ARXIV-2605-15403:end -->
<!-- delta:SF-2026-ARXIV-2605-15403:start -->MoE balance controller 应估计 population-level routing distribution，而不是把 noisy mini-batch count 当真值；EMA/mirror-descent bias correction换来更稳定利用率，也新增 lag 与非平稳漂移<!-- delta:SF-2026-ARXIV-2605-15403:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15403:end -->

<!-- books-review:SF-2026-ARXIV-2605-15422:start -->
<!-- existing:SF-2026-ARXIV-2605-15422:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及相邻章节；当前主线已覆盖parallel state、collective/placement、kernel execution、checkpoint 与 optimization semantics。正文尚未明确承载本 family 的增量：共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract。 Owner snapshot sha256=`5e9d628aaf7a6c0995918787baa0681091e4e65365fddc0457075715547d969d`；相邻章节=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-15422:end -->
<!-- delta:SF-2026-ARXIV-2605-15422:start -->共享 prompt 的大 rollout RL 训练可将 prompt K/V 与 response K/V 分开复用并保持 causal gradient；收益必须绑定 N、P、R、kernel 与 backward contract<!-- delta:SF-2026-ARXIV-2605-15422:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15422:end -->

<!-- books-review:SF-2026-ARXIV-2605-15425:start -->
<!-- existing:SF-2026-ARXIV-2605-15425:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15425:end -->
<!-- delta:SF-2026-ARXIV-2605-15425:start -->Agent coding workflow 应把 task decomposition、branch/retry与schema validation移出 monolithic prompt，交给 executable runtime；LLM只拥有局部判断，不拥有全局控制流提交<!-- delta:SF-2026-ARXIV-2605-15425:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15425:end -->

<!-- books-review:SF-2026-ARXIV-2605-15466:start -->
<!-- existing:SF-2026-ARXIV-2605-15466:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15466:end -->
<!-- delta:SF-2026-ARXIV-2605-15466:start -->predictive representation只有在 masking 聚焦 entity interaction且用 causal reasoning/action outcome验证时才接近 world-state signal；重建 latent trajectory仍不自动获得控制充分性<!-- delta:SF-2026-ARXIV-2605-15466:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15466:end -->

<!-- books-review:SF-2026-ARXIV-2605-15477:start -->
<!-- existing:SF-2026-ARXIV-2605-15477:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15477:end -->
<!-- delta:SF-2026-ARXIV-2605-15477:start -->exo video要服务 ego world model，必须先恢复body pose/action schema并显式转换视角；数据扩容收益依赖action identity与ego observation对齐，不能把普通视频直接当控制轨迹<!-- delta:SF-2026-ARXIV-2605-15477:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15477:end -->

<!-- books-review:SF-2026-ARXIV-2605-15508:start -->
<!-- existing:SF-2026-ARXIV-2605-15508:start -->`books/part-02-model/22-long-context.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15508:end -->
<!-- delta:SF-2026-ARXIV-2605-15508:start -->Draft-model attention is reused as the target model's sparse admission mask while target KV remains authoritative; this adds a draft/target state-ownership and false-negative fallback boundary not explicit in Ch22.<!-- delta:SF-2026-ARXIV-2605-15508:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15508:end -->

<!-- books-review:SF-2026-ARXIV-2605-15514:start -->
<!-- existing:SF-2026-ARXIV-2605-15514:start -->`books/part-02-model/13-position-encoding.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15514:end -->
<!-- delta:SF-2026-ARXIV-2605-15514:start -->The exact-v1 proof separates position inversion/aliasing from token inversion/aliasing, tightening Ch13's qualitative RoPE extrapolation account into a protocol-specific representational limit.<!-- delta:SF-2026-ARXIV-2605-15514:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15514:end -->

<!-- books-review:SF-2026-ARXIV-2605-15520:start -->
<!-- existing:SF-2026-ARXIV-2605-15520:start -->`books/part-04-training-system/27-data.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15520:end -->
<!-- delta:SF-2026-ARXIV-2605-15520:start -->A participant can preserve model utility while corrupting distributed data-attribution credit, so provenance integrity needs an adversarial contract rather than treating attribution as a passive statistic.<!-- delta:SF-2026-ARXIV-2605-15520:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15520:end -->

<!-- books-review:SF-2026-ARXIV-2605-15529:start -->
<!-- existing:SF-2026-ARXIV-2605-15529:start -->`books/part-04-training-system/31-rlhf.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15529:end -->
<!-- delta:SF-2026-ARXIV-2605-15529:start -->Count evidence and learned concentration make process-reward reliability an input to ranking, stopping and repair; Ch31 has uncertainty-selected feedback but not this finite-evidence control contract.<!-- delta:SF-2026-ARXIV-2605-15529:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15529:end -->

<!-- books-review:SF-2026-ARXIV-2605-15565:start -->
<!-- existing:SF-2026-ARXIV-2605-15565:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15565:end -->
<!-- delta:SF-2026-ARXIV-2605-15565:start -->Trainer-centered RL coordination becomes explicit dataflow components with rollout-as-a-service and versioned weight transfer, moving orchestration ownership into the distributed runtime.<!-- delta:SF-2026-ARXIV-2605-15565:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15565:end -->

<!-- books-review:SF-2026-ARXIV-2605-15573:start -->
<!-- existing:SF-2026-ARXIV-2605-15573:start -->Ch82 already treats parallel/sequential topology as runtime policy with admission, convergence and rollback rather than a fixed multi-agent graph.<!-- existing:SF-2026-ARXIV-2605-15573:end -->
<!-- delta:SF-2026-ARXIV-2605-15573:start -->Ch82 already treats parallel/sequential topology as runtime policy with admission, convergence and rollback rather than a fixed multi-agent graph.<!-- delta:SF-2026-ARXIV-2605-15573:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15573:end -->

<!-- books-review:SF-2026-ARXIV-2605-15581:start -->
<!-- existing:SF-2026-ARXIV-2605-15581:start -->Ch81 already owns stage-localized failure evidence, replayable repair and durable workflow recovery; STAR is a scoped RCA realization.<!-- existing:SF-2026-ARXIV-2605-15581:end -->
<!-- delta:SF-2026-ARXIV-2605-15581:start -->Ch81 already owns stage-localized failure evidence, replayable repair and durable workflow recovery; STAR is a scoped RCA realization.<!-- delta:SF-2026-ARXIV-2605-15581:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15581:end -->

<!-- books-review:SF-2026-ARXIV-2605-15609:start -->
<!-- existing:SF-2026-ARXIV-2605-15609:start -->Ch24 already carries proposal, parallel refinement, verification, rejection and rollback as the diffusion/speculation evolution spine.<!-- existing:SF-2026-ARXIV-2605-15609:end -->
<!-- delta:SF-2026-ARXIV-2605-15609:start -->Ch24 already carries proposal, parallel refinement, verification, rejection and rollback as the diffusion/speculation evolution spine.<!-- delta:SF-2026-ARXIV-2605-15609:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15609:end -->

<!-- books-review:SF-2026-ARXIV-2605-15617:start -->
<!-- existing:SF-2026-ARXIV-2605-15617:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15617:end -->
<!-- delta:SF-2026-ARXIV-2605-15617:start -->Selective real-rank execution plus calibrated virtual participants makes cluster-scale training control paths testable on small hardware and introduces fidelity/error ownership absent from Ch36.<!-- delta:SF-2026-ARXIV-2605-15617:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15617:end -->

<!-- books-review:SF-2026-ARXIV-2605-15618:start -->
<!-- existing:SF-2026-ARXIV-2605-15618:start -->Ch25 already distinguishes predictive representation quality from controllable world-state usefulness and requires robustness/evaluation boundaries.<!-- existing:SF-2026-ARXIV-2605-15618:end -->
<!-- delta:SF-2026-ARXIV-2605-15618:start -->Ch25 already distinguishes predictive representation quality from controllable world-state usefulness and requires robustness/evaluation boundaries.<!-- delta:SF-2026-ARXIV-2605-15618:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15618:end -->

<!-- books-review:SF-2026-ARXIV-2605-15638:start -->
<!-- existing:SF-2026-ARXIV-2605-15638:start -->`books/part-06-ai-infrastructure/67-monitoring.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15638:end -->
<!-- delta:SF-2026-ARXIV-2605-15638:start -->Duplicated intra-thread instruction execution turns latent permanent-fault corruption into a runtime SDC sensor, adding detection coverage and overhead/fault-correlation boundaries to Ch67.<!-- delta:SF-2026-ARXIV-2605-15638:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15638:end -->

<!-- books-review:SF-2026-ARXIV-2605-15648:start -->
<!-- existing:SF-2026-ARXIV-2605-15648:start -->`books/part-06-ai-infrastructure/72-security.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-15648:end -->
<!-- delta:SF-2026-ARXIV-2605-15648:start -->The paper shows that an implementation variant can invalidate the privacy analysis used for DP-SGD, requiring mechanism-to-accountant conformance and audit evidence before a privacy claim is admitted.<!-- delta:SF-2026-ARXIV-2605-15648:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-15648:end -->

<!-- books-review:SF-2026-ARXIV-2605-15665:start -->
<!-- existing:SF-2026-ARXIV-2605-15665:start -->Ch67 already connects requirement-derived tests, production-faithful simulation, diagnosis, prompt repair and continuous drift monitoring.<!-- existing:SF-2026-ARXIV-2605-15665:end -->
<!-- delta:SF-2026-ARXIV-2605-15665:start -->Ch67 already connects requirement-derived tests, production-faithful simulation, diagnosis, prompt repair and continuous drift monitoring.<!-- delta:SF-2026-ARXIV-2605-15665:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15665:end -->

<!-- books-review:SF-2026-ARXIV-2605-15694:start -->
<!-- existing:SF-2026-ARXIV-2605-15694:start -->Ch52 already owns distributed inference placement under link loss, partition cost, state movement and heterogeneous edge constraints; CATS is a narrow deployment case.<!-- existing:SF-2026-ARXIV-2605-15694:end -->
<!-- delta:SF-2026-ARXIV-2605-15694:start -->Ch52 already owns distributed inference placement under link loss, partition cost, state movement and heterogeneous edge constraints; CATS is a narrow deployment case.<!-- delta:SF-2026-ARXIV-2605-15694:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15694:end -->

<!-- books-review:SF-2026-ARXIV-2605-15710:start -->
<!-- existing:SF-2026-ARXIV-2605-15710:start -->Ch66 and Ch77 already require source-distributed evidence identity, provenance-aware memory evaluation and claim-level retrieval correctness.<!-- existing:SF-2026-ARXIV-2605-15710:end -->
<!-- delta:SF-2026-ARXIV-2605-15710:start -->Ch66 and Ch77 already require source-distributed evidence identity, provenance-aware memory evaluation and claim-level retrieval correctness.<!-- delta:SF-2026-ARXIV-2605-15710:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15710:end -->

<!-- books-review:SF-2026-ARXIV-2605-15734:start -->
<!-- existing:SF-2026-ARXIV-2605-15734:start -->Ch66 already separates construct validity, slice reliability, calibration and evaluator identity for inferred user-state measurements.<!-- existing:SF-2026-ARXIV-2605-15734:end -->
<!-- delta:SF-2026-ARXIV-2605-15734:start -->Ch66 already separates construct validity, slice reliability, calibration and evaluator identity for inferred user-state measurements.<!-- delta:SF-2026-ARXIV-2605-15734:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15734:end -->

<!-- books-review:SF-2026-ARXIV-2605-15761:start -->
<!-- existing:SF-2026-ARXIV-2605-15761:start -->Ch66 already models leaderboard stability as an evaluator/version/perturbation contract and includes manipulation-sensitive release evidence.<!-- existing:SF-2026-ARXIV-2605-15761:end -->
<!-- delta:SF-2026-ARXIV-2605-15761:start -->Ch66 already models leaderboard stability as an evaluator/version/perturbation contract and includes manipulation-sensitive release evidence.<!-- delta:SF-2026-ARXIV-2605-15761:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15761:end -->

<!-- books-review:SF-2026-ARXIV-2605-15777:start -->
<!-- existing:SF-2026-ARXIV-2605-15777:start -->Ch66 already evaluates workflow agents through executable task effects, environment state and bounded judge evidence rather than answer similarity alone.<!-- existing:SF-2026-ARXIV-2605-15777:end -->
<!-- delta:SF-2026-ARXIV-2605-15777:start -->Ch66 already evaluates workflow agents through executable task effects, environment state and bounded judge evidence rather than answer similarity alone.<!-- delta:SF-2026-ARXIV-2605-15777:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15777:end -->

<!-- books-review:SF-2026-ARXIV-2605-15815:start -->
<!-- existing:SF-2026-ARXIV-2605-15815:start -->Ch84 already owns reusable skill compilation, verification, provenance, lifecycle and transfer; repository setup is one skill domain.<!-- existing:SF-2026-ARXIV-2605-15815:end -->
<!-- delta:SF-2026-ARXIV-2605-15815:start -->Ch84 already owns reusable skill compilation, verification, provenance, lifecycle and transfer; repository setup is one skill domain.<!-- delta:SF-2026-ARXIV-2605-15815:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15815:end -->

<!-- books-review:SF-2026-ARXIV-2605-15846:start -->
<!-- existing:SF-2026-ARXIV-2605-15846:start -->Ch66 and Ch84 already require versioned long-horizon tasks, reproducible harness identity and rollout-based quality control.<!-- existing:SF-2026-ARXIV-2605-15846:end -->
<!-- delta:SF-2026-ARXIV-2605-15846:start -->Ch66 and Ch84 already require versioned long-horizon tasks, reproducible harness identity and rollout-based quality control.<!-- delta:SF-2026-ARXIV-2605-15846:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15846:end -->

<!-- books-review:SF-2026-ARXIV-2605-15957:start -->
<!-- existing:SF-2026-ARXIV-2605-15957:start -->Ch49 already owns heterogeneous CPU/GPU execution plans, phase-aware placement, data-layout conversion and fallback; MaxVec is a vector-search realization.<!-- existing:SF-2026-ARXIV-2605-15957:end -->
<!-- delta:SF-2026-ARXIV-2605-15957:start -->Ch49 already owns heterogeneous CPU/GPU execution plans, phase-aware placement, data-layout conversion and fallback; MaxVec is a vector-search realization.<!-- delta:SF-2026-ARXIV-2605-15957:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15957:end -->

<!-- books-review:SF-2026-ARXIV-2605-15960:start -->
<!-- existing:SF-2026-ARXIV-2605-15960:start -->Ch25 explicitly distinguishes model error from planner exploitation and requires adversarial imagined-rollout validation.<!-- existing:SF-2026-ARXIV-2605-15960:end -->
<!-- delta:SF-2026-ARXIV-2605-15960:start -->Ch25 explicitly distinguishes model error from planner exploitation and requires adversarial imagined-rollout validation.<!-- delta:SF-2026-ARXIV-2605-15960:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15960:end -->

<!-- books-review:SF-2026-ARXIV-2605-15967:start -->
<!-- existing:SF-2026-ARXIV-2605-15967:start -->Ch25 already separates observed, latent and imagined state and supports executable causal transition substrates with intervention boundaries.<!-- existing:SF-2026-ARXIV-2605-15967:end -->
<!-- delta:SF-2026-ARXIV-2605-15967:start -->Ch25 already separates observed, latent and imagined state and supports executable causal transition substrates with intervention boundaries.<!-- delta:SF-2026-ARXIV-2605-15967:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-15967:end -->

<!-- books-review:SF-2026-ARXIV-2605-16035:start -->
<!-- existing:SF-2026-ARXIV-2605-16035:start -->Ch84 already requires agent/operator/service identity, signed ownership, delegation scope and accountable action traces.<!-- existing:SF-2026-ARXIV-2605-16035:end -->
<!-- delta:SF-2026-ARXIV-2605-16035:start -->Ch84 already requires agent/operator/service identity, signed ownership, delegation scope and accountable action traces.<!-- delta:SF-2026-ARXIV-2605-16035:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16035:end -->

<!-- books-review:SF-2026-ARXIV-2605-16154:start -->
<!-- existing:SF-2026-ARXIV-2605-16154:start -->Ch26 already treats action chunks, control frequency and rollout allocation as workload-specific training/runtime trade-offs; probabilistic masking is a local optimization.<!-- existing:SF-2026-ARXIV-2605-16154:end -->
<!-- delta:SF-2026-ARXIV-2605-16154:start -->Ch26 already treats action chunks, control frequency and rollout allocation as workload-specific training/runtime trade-offs; probabilistic masking is a local optimization.<!-- delta:SF-2026-ARXIV-2605-16154:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16154:end -->

<!-- books-review:SF-2026-ARXIV-2605-16184:start -->
<!-- existing:SF-2026-ARXIV-2605-16184:start -->`books/part-04-training-system/36-distributed-training.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-16184:end -->
<!-- delta:SF-2026-ARXIV-2605-16184:start -->Second-order state moves to heterogeneous memory under hook-driven overlap and bounded-staleness coherence; the runtime, not only the optimizer, now owns update timing and consistency.<!-- delta:SF-2026-ARXIV-2605-16184:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-16184:end -->

<!-- books-review:SF-2026-ARXIV-2605-16194:start -->
<!-- existing:SF-2026-ARXIV-2605-16194:start -->Ch84 already owns typed artifacts, machine-readable provenance, schema validation and lifecycle compatibility for agent-consumable knowledge.<!-- existing:SF-2026-ARXIV-2605-16194:end -->
<!-- delta:SF-2026-ARXIV-2605-16194:start -->Ch84 already owns typed artifacts, machine-readable provenance, schema validation and lifecycle compatibility for agent-consumable knowledge.<!-- delta:SF-2026-ARXIV-2605-16194:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16194:end -->

<!-- books-review:SF-2026-ARXIV-2605-16198:start -->
<!-- existing:SF-2026-ARXIV-2605-16198:start -->Ch72 already carries formal properties, bounded-state monitors, intervention, auditor false negatives and verification scope limits.<!-- existing:SF-2026-ARXIV-2605-16198:end -->
<!-- delta:SF-2026-ARXIV-2605-16198:start -->Ch72 already carries formal properties, bounded-state monitors, intervention, auditor false negatives and verification scope limits.<!-- delta:SF-2026-ARXIV-2605-16198:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16198:end -->

<!-- books-review:SF-2026-ARXIV-2605-16217:start -->
<!-- existing:SF-2026-ARXIV-2605-16217:start -->Ch76 already owns search, evidence graph growth, claim verification, synthesis and complementary retrieval under provenance constraints.<!-- existing:SF-2026-ARXIV-2605-16217:end -->
<!-- delta:SF-2026-ARXIV-2605-16217:start -->Ch76 already owns search, evidence graph growth, claim verification, synthesis and complementary retrieval under provenance constraints.<!-- delta:SF-2026-ARXIV-2605-16217:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16217:end -->

<!-- books-review:SF-2026-ARXIV-2605.16007:start -->
<!-- existing:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- existing:SF-2026-ARXIV-2605.16007:end -->
<!-- delta:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- delta:SF-2026-ARXIV-2605.16007:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16007:end -->

<!-- books-review:SF-2026-ARXIV-2605.16234:start -->
<!-- existing:SF-2026-ARXIV-2605.16234:start -->`books/part-02-model/17-transformer-layer.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16234:end -->
<!-- delta:SF-2026-ARXIV-2605.16234:start -->Layer redundancy conclusions change between replacement and interchange protocols, so pruning must freeze intervention semantics and evaluator identity before treating layers as substitutable.<!-- delta:SF-2026-ARXIV-2605.16234:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16234:end -->

<!-- books-review:SF-2026-ARXIV-2605.16255:start -->
<!-- existing:SF-2026-ARXIV-2605.16255:start -->`books/part-06-ai-infrastructure/70-cost.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16255:end -->
<!-- delta:SF-2026-ARXIV-2605.16255:start -->AI power design is reframed from installed megawatts to deployable capacity across rack generations, linking topology, placement and redundancy to multi-resource stranding.<!-- delta:SF-2026-ARXIV-2605.16255:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16255:end -->

<!-- books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->
<!-- existing:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->已逐章核对 `books/part-07-agent/84-agent-platform.md` 的“Agent Runtime State Machine；Scheduling 不只是 GPU；Release、Canary 与 Rollback”：现章已把 run identity、runtime state、调度和发布纳入平台；缺少质量门控的执行粒度、verification-gated skill admission 与价值-能耗 stop controller。<!-- existing:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end --> <!-- delta:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:start -->exact-v1 新增 delta 是“Local agent execution needs an explicit stop controller that trades expected task value against marginal energy rather than running every trajectory to a fixed cap.”。<!-- delta:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end --> 相邻章节 `books/part-07-agent/83-mcp.md` 只保留 handoff。正文写回位于 `books/part-07-agent/84-agent-platform.md#L429-L439`，并由 `post-write-audit-v1:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-AGENTSTOP-ENERGY-AWARE-TERMINATION:end -->

<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->
<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->已对读当前 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L10` 与相邻 handoff `books/part-06-ai-infrastructure/67-monitoring.md#L10; books/part-06-ai-infrastructure/73-production-best-practice.md#L10`。Execution/Evaluation 已将 quantization 视为行为变换，要求 dense-vs-quantized per-example correctness、slice、校准及真实硬件验证；该 family 直接落在现有 contract 内。<!-- existing:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:start -->dense-vs-quantized 的 item-level divergence 强化既有行为回归 gate；相同命题已完整存在，新增论文名称不会改善论证。<!-- delta:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->
结论：**No Change — Existing Coverage**。
<!-- books-review:SF-QUANTIZATION-BEHAVIORAL-REGRESSION:end -->

<!-- books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->
<!-- existing:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->`books/part-07-agent/84-agent-platform.md` 已以更一般的 AGENT-PLATFORM 演进链承载 `SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces` 的问题：owner、commit/evidence boundary、失败回退与旧路径共存已经显式化；该 exact-v1 只增加受限实现或 benchmark evidence。<!-- existing:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->
<!-- delta:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:start -->To this end, we propose SkillSmith, a boundary-first compiler-runtime framework that compiles skill packages offline into minimal executable interfaces.<!-- delta:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end --> Final prewrite decision=`No Change — Existing Coverage`。Integrate 只进入 date-local queue；本 reviewer 未修改共享 Books。
<!-- books-review:SF-SKILLSMITH-COMPILING-AGENT-SKILLS-INTO-BOUNDARY-GUIDED-RUNTIME-INTERFACE:end -->

<!-- books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->
<!-- existing:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->已逐章核对 `books/part-07-agent/82-multi-agent.md` 的“Coordination Tax；Message 不是 State；Verification 与 Aggregation”：现章已要求度量 coordination tax、隔离 message/state 并治理更新；缺少 sequential agent updates 导致 occupancy shift 时的 resampling 与 per-agent trust region。<!-- existing:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end --> <!-- delta:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:start -->exact-v1 新增 delta 是“Sequentially fine-tuning interacting agents invalidates cached-rollout occupancy; resampling and per-agent trust regions make the joint update contract explicit.”。<!-- delta:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end --> 相邻章节 `books/part-07-agent/81-workflow.md`、`books/part-07-agent/83-mcp.md` 只保留 handoff。正文写回位于 `books/part-07-agent/82-multi-agent.md#L430-L442`，并由 `post-write-audit-v1:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT` 验证；状态为 integrated/post-write-passed。
<!-- books-review:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT:end -->

<!-- books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->
<!-- existing:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；owner 当前主干包含 ['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化']。仅正文命题用于比较，Review notes 不视为整合。<!-- existing:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->
<!-- delta:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->We introduce a Distributed Trust Framework (DTF), a verification framework for governed mutation systems that computes execution authority from structured, verifiable artifacts.<!-- delta:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end --> Independent decision=`Integrate`；prewrite challenge 已通过，不写共享 Books。
<!-- books-review:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260518-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260518 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260518-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260518-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=48；selected=3；all others retain completed reviews | passed |
| SA-20260518-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=489；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260518/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260518/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-18.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
