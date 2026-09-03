# Daily Research — 2026-05-28

**Research Date:** 2026-05-28

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-27 09:00:00 ～ 2026-05-28 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 835 个注册 arXiv identity，冻结 117 个 Source Family；pre-denominator closure=718，withdrawn pre-denominator=0。40 个旧候选被迁回正确 owner day，1 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-28 |
| Window End | 2026-05-28 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260528-CREATED-79d010c35d3cbcd3 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-27T09:00:00+08:00 | 2026-05-28T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 835 | SF-2026-ARXIV-2605-27390;SF-2026-ARXIV-2605-27428;SF-2026-ARXIV-2605-27432;SF-2026-ARXIV-2605-27435;SF-2026-ARXIV-2605-27437;SF-2026-ARXIV-2605-27461;SF-2026-ARXIV-2605-27466;SF-2026-ARXIV-2605-27480;SF-2026-ARXIV-2605-27483;SF-2026-ARXIV-2605-27488;SF-2026-ARXIV-2605-27489;SF-2026-ARXIV-2605-27491;SF-2026-ARXIV-2605-27492;SF-2026-ARXIV-2605-27494;SF-2026-ARXIV-2605-27547;SF-2026-ARXIV-2605-27559;SF-2026-ARXIV-2605-27566;SF-2026-ARXIV-2605-27569;SF-2026-ARXIV-2605-27575;SF-2026-ARXIV-2605-27589;SF-2026-ARXIV-2605-27599;SF-2026-ARXIV-2605-27621;SF-2026-ARXIV-2605-27630;SF-2026-ARXIV-2605-27668;SF-2026-ARXIV-2605-27671;SF-2026-ARXIV-2605-27678;SF-2026-ARXIV-2605-27681;SF-2026-ARXIV-2605-27690;SF-2026-ARXIV-2605-27710;SF-2026-ARXIV-2605-27712;SF-2026-ARXIV-2605-27720;SF-2026-ARXIV-2605-27744;SF-2026-ARXIV-2605-27752;SF-2026-ARXIV-2605-27759;SF-2026-ARXIV-2605-27760;SF-2026-ARXIV-2605-27761;SF-2026-ARXIV-2605-27763;SF-2026-ARXIV-2605-27766;SF-2026-ARXIV-2605-27784;SF-2026-ARXIV-2605-27785;SF-2026-ARXIV-2605-27789;SF-2026-ARXIV-2605-27820;SF-2026-ARXIV-2605-27825;SF-2026-ARXIV-2605-27850;SF-2026-ARXIV-2605-27879;SF-2026-ARXIV-2605-27881;SF-2026-ARXIV-2605-27898;SF-2026-ARXIV-2605-27899;SF-2026-ARXIV-2605-27901;SF-2026-ARXIV-2605-27918;SF-2026-ARXIV-2605-27922;SF-2026-ARXIV-2605-27947;SF-2026-ARXIV-2605-27954;SF-2026-ARXIV-2605-27957;SF-2026-ARXIV-2605-27963;SF-2026-ARXIV-2605-27980;SF-2026-ARXIV-2605-27995;SF-2026-ARXIV-2605-28000;SF-2026-ARXIV-2605-28009;SF-2026-ARXIV-2605-28017;SF-2026-ARXIV-2605-28044;SF-2026-ARXIV-2605-28046;SF-2026-ARXIV-2605-28053;SF-2026-ARXIV-2605-28071;SF-2026-ARXIV-2605-28074;SF-2026-ARXIV-2605-28083;SF-2026-ARXIV-2605-28095;SF-2026-ARXIV-2605-28097;SF-2026-ARXIV-2605-28108;SF-2026-ARXIV-2605-28112;SF-2026-ARXIV-2605-28116;SF-2026-ARXIV-2605-28122;SF-2026-ARXIV-2605-28158;SF-2026-ARXIV-2605-28201;SF-2026-ARXIV-2605-28213;SF-2026-ARXIV-2605-28214;SF-2026-ARXIV-2605-28224;SF-2026-ARXIV-2605-28282;SF-2026-ARXIV-2605-28302;SF-2026-ARXIV-2605-28354;SF-2026-ARXIV-2605-28371;SF-2026-ARXIV-2605-28384;SF-2026-ARXIV-2605-28390;SF-2026-ARXIV-2605-28424;SF-2026-ARXIV-2605-28433;SF-2026-ARXIV-2605-28467;SF-2026-ARXIV-2605-28480;SF-2026-ARXIV-2605-28508;SF-2026-ARXIV-2605-28510;SF-2026-ARXIV-2605-28544;SF-2026-ARXIV-2605-28561;SF-2026-ARXIV-2605-28565;SF-2026-ARXIV-2605-28573;SF-2026-ARXIV-2605-28617;SF-2026-ARXIV-2605-28632;SF-2026-ARXIV-2605-28634;SF-2026-ARXIV-2605-28640;SF-2026-ARXIV-2605-28646;SF-2026-ARXIV-2605-28678;SF-2026-ARXIV-2605-28691;SF-2026-ARXIV-2605-28699;SF-2026-ARXIV-2605-28704;SF-2026-ARXIV-2605-28721;SF-2026-ARXIV-2605-28726;SF-2026-ARXIV-2605-28732;SF-2026-ARXIV-2605-28742;SF-2026-ARXIV-2605-28751;SF-2026-ARXIV-2605-28760;SF-2026-ARXIV-2605-28764;SF-2026-ARXIV-2605-28773;SF-2026-ARXIV-2605-28774;SF-2026-ARXIV-2605-28778;SF-2026-ARXIV-2605-28787;SF-2026-ARXIV-2605-28803;SF-2026-ARXIV-2605-28805;SF-2026-ARXIV-2605-28807;SF-2026-ARXIV-2605-28819 | created-day pages=closed; OAI category sets=closed; direct same-day OAI=670 | 2026-05-28T09:00:00+08:00 | coverage:SRC-ARXIV:20260528 | — |

<!-- coverage:SRC-ARXIV:20260528:start -->全量 raw inventory=835；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260528:end -->

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
| SF-2026-ARXIV-2605-27390 | arXiv:2605.27390v1 | paper-v1:2605.27390 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27390 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27390 | yes |
| SF-2026-ARXIV-2605-27428 | arXiv:2605.27428v1 | paper-v1:2605.27428 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27428 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27428 | no |
| SF-2026-ARXIV-2605-27432 | arXiv:2605.27432v1 | paper-v1:2605.27432 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27432 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27432 | no |
| SF-2026-ARXIV-2605-27435 | arXiv:2605.27435v1 | paper-v1:2605.27435 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27435 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27435 | no |
| SF-2026-ARXIV-2605-27437 | arXiv:2605.27437v1 | paper-v1:2605.27437 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27437 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27437 | no |
| SF-2026-ARXIV-2605-27461 | arXiv:2605.27461v1 | paper-v1:2605.27461 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27461 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27461 | no |
| SF-2026-ARXIV-2605-27466 | arXiv:2605.27466v1 | paper-v1:2605.27466 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27466 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27466 | no |
| SF-2026-ARXIV-2605-27480 | arXiv:2605.27480v1 | paper-v1:2605.27480 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27480 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605-27480 | no |
| SF-2026-ARXIV-2605-27483 | arXiv:2605.27483v1 | paper-v1:2605.27483 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27483 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27483 | no |
| SF-2026-ARXIV-2605-27488 | arXiv:2605.27488v1 | paper-v1:2605.27488 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27488 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27488 | no |
| SF-2026-ARXIV-2605-27489 | arXiv:2605.27489v1 | paper-v1:2605.27489 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27489 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27489 | no |
| SF-2026-ARXIV-2605-27491 | arXiv:2605.27491v1 | paper-v1:2605.27491 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27491 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27491 | no |
| SF-2026-ARXIV-2605-27492 | arXiv:2605.27492v1 | paper-v1:2605.27492 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27492 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27492 | no |
| SF-2026-ARXIV-2605-27494 | arXiv:2605.27494v1 | paper-v1:2605.27494 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27494 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-27494 | no |
| SF-2026-ARXIV-2605-27547 | arXiv:2605.27547v1 | paper-v1:2605.27547 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27547 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27547 | no |
| SF-2026-ARXIV-2605-27559 | arXiv:2605.27559v1 | paper-v1:2605.27559 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27559 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27559 | no |
| SF-2026-ARXIV-2605-27566 | arXiv:2605.27566v1 | paper-v1:2605.27566 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27566 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Weekly Only — Context | books-review:SF-2026-ARXIV-2605-27566 | no |
| SF-2026-ARXIV-2605-27569 | arXiv:2605.27569v1 | paper-v1:2605.27569 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27569 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27569 | no |
| SF-2026-ARXIV-2605-27575 | arXiv:2605.27575v1 | paper-v1:2605.27575 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27575 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27575 | no |
| SF-2026-ARXIV-2605-27589 | arXiv:2605.27589v1 | paper-v1:2605.27589 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27589 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27589 | no |
| SF-2026-ARXIV-2605-27599 | arXiv:2605.27599v1 | paper-v1:2605.27599 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27599 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-27599 | no |
| SF-2026-ARXIV-2605-27621 | arXiv:2605.27621v1 | paper-v1:2605.27621 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27621 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27621 | no |
| SF-2026-ARXIV-2605-27630 | arXiv:2605.27630v1 | paper-v1:2605.27630 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27630 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27630 | no |
| SF-2026-ARXIV-2605-27668 | arXiv:2605.27668v1 | paper-v1:2605.27668 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27668 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27668 | no |
| SF-2026-ARXIV-2605-27671 | arXiv:2605.27671v1 | paper-v1:2605.27671 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27671 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27671 | no |
| SF-2026-ARXIV-2605-27678 | arXiv:2605.27678v1 | paper-v1:2605.27678 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27678 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-27678 | no |
| SF-2026-ARXIV-2605-27681 | arXiv:2605.27681v1 | paper-v1:2605.27681 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27681 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27681 | no |
| SF-2026-ARXIV-2605-27690 | arXiv:2605.27690v1 | paper-v1:2605.27690 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27690 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27690 | no |
| SF-2026-ARXIV-2605-27710 | arXiv:2605.27710v1 | paper-v1:2605.27710 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27710 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27710 | no |
| SF-2026-ARXIV-2605-27712 | arXiv:2605.27712v1 | paper-v1:2605.27712 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27712 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-27712 | no |
| SF-2026-ARXIV-2605-27720 | arXiv:2605.27720v1 | paper-v1:2605.27720 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27720 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27720 | no |
| SF-2026-ARXIV-2605-27744 | arXiv:2605.27744v1 | paper-v1:2605.27744 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27744 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27744 | no |
| SF-2026-ARXIV-2605-27752 | arXiv:2605.27752v1 | paper-v1:2605.27752 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27752 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27752 | no |
| SF-2026-ARXIV-2605-27759 | arXiv:2605.27759v1 | paper-v1:2605.27759 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27759 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27759 | no |
| SF-2026-ARXIV-2605-27760 | arXiv:2605.27760v1 | paper-v1:2605.27760 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27760 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27760 | no |
| SF-2026-ARXIV-2605-27761 | arXiv:2605.27761v1 | paper-v1:2605.27761 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27761 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27761 | no |
| SF-2026-ARXIV-2605-27763 | arXiv:2605.27763v1 | paper-v1:2605.27763 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27763 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27763 | no |
| SF-2026-ARXIV-2605-27766 | arXiv:2605.27766v1 | paper-v1:2605.27766 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27766 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27766 | no |
| SF-2026-ARXIV-2605-27784 | arXiv:2605.27784v1 | paper-v1:2605.27784 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27784 | self | — | new_in_window | AGENT-PROMPT | Integrate | books-review:SF-2026-ARXIV-2605-27784 | no |
| SF-2026-ARXIV-2605-27785 | arXiv:2605.27785v1 | paper-v1:2605.27785 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27785 | self | — | new_in_window | PLATFORM-LOGGING | Integrate | books-review:SF-2026-ARXIV-2605-27785 | no |
| SF-2026-ARXIV-2605-27789 | arXiv:2605.27789v1 | paper-v1:2605.27789 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27789 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-27789 | no |
| SF-2026-ARXIV-2605-27820 | arXiv:2605.27820v1 | paper-v1:2605.27820 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27820 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27820 | no |
| SF-2026-ARXIV-2605-27825 | arXiv:2605.27825v1 | paper-v1:2605.27825 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27825 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-27825 | no |
| SF-2026-ARXIV-2605-27850 | arXiv:2605.27850v1 | paper-v1:2605.27850 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27850 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27850 | no |
| SF-2026-ARXIV-2605-27879 | arXiv:2605.27879v1 | paper-v1:2605.27879 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27879 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27879 | no |
| SF-2026-ARXIV-2605-27881 | arXiv:2605.27881v1 | paper-v1:2605.27881 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-27881 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27881 | no |
| SF-2026-ARXIV-2605-27898 | arXiv:2605.27898v1 | paper-v1:2605.27898 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27898 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27898 | no |
| SF-2026-ARXIV-2605-27899 | arXiv:2605.27899v1 | paper-v1:2605.27899 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27899 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27899 | no |
| SF-2026-ARXIV-2605-27901 | arXiv:2605.27901v1 | paper-v1:2605.27901 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27901 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27901 | no |
| SF-2026-ARXIV-2605-27918 | arXiv:2605.27918v1 | paper-v1:2605.27918 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27918 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27918 | no |
| SF-2026-ARXIV-2605-27922 | arXiv:2605.27922v1 | paper-v1:2605.27922 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27922 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27922 | no |
| SF-2026-ARXIV-2605-27947 | arXiv:2605.27947v1 | paper-v1:2605.27947 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27947 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27947 | no |
| SF-2026-ARXIV-2605-27954 | arXiv:2605.27954v1 | paper-v1:2605.27954 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27954 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27954 | no |
| SF-2026-ARXIV-2605-27957 | arXiv:2605.27957v1 | paper-v1:2605.27957 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27957 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27957 | no |
| SF-2026-ARXIV-2605-27963 | arXiv:2605.27963v1 | paper-v1:2605.27963 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27963 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27963 | no |
| SF-2026-ARXIV-2605-27980 | arXiv:2605.27980v1 | paper-v1:2605.27980 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27980 | self | — | new_in_window | MODEL-POSITION-ENCODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27980 | no |
| SF-2026-ARXIV-2605-27995 | arXiv:2605.27995v1 | paper-v1:2605.27995 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27995 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27995 | no |
| SF-2026-ARXIV-2605-28000 | arXiv:2605.28000v1 | paper-v1:2605.28000 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28000 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28000 | no |
| SF-2026-ARXIV-2605-28009 | arXiv:2605.28009v1 | paper-v1:2605.28009 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28009 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28009 | no |
| SF-2026-ARXIV-2605-28017 | arXiv:2605.28017v1 | paper-v1:2605.28017 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28017 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28017 | no |
| SF-2026-ARXIV-2605-28044 | arXiv:2605.28044v1 | paper-v1:2605.28044 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28044 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28044 | no |
| SF-2026-ARXIV-2605-28046 | arXiv:2605.28046v1 | paper-v1:2605.28046 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28046 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28046 | no |
| SF-2026-ARXIV-2605-28053 | arXiv:2605.28053v1 | paper-v1:2605.28053 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28053 | self | — | new_in_window | INFER-CONTINUOUS-BATCHING | Integrate | books-review:SF-2026-ARXIV-2605-28053 | no |
| SF-2026-ARXIV-2605-28071 | arXiv:2605.28071v1 | paper-v1:2605.28071 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28071 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28071 | no |
| SF-2026-ARXIV-2605-28074 | arXiv:2605.28074v1 | paper-v1:2605.28074 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28074 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28074 | no |
| SF-2026-ARXIV-2605-28083 | arXiv:2605.28083v1 | paper-v1:2605.28083 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28083 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28083 | no |
| SF-2026-ARXIV-2605-28095 | arXiv:2605.28095v1 | paper-v1:2605.28095 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28095 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-28095 | no |
| SF-2026-ARXIV-2605-28097 | arXiv:2605.28097v1 | paper-v1:2605.28097 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28097 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28097 | no |
| SF-2026-ARXIV-2605-28108 | arXiv:2605.28108v1 | paper-v1:2605.28108 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28108 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28108 | no |
| SF-2026-ARXIV-2605-28112 | arXiv:2605.28112v1 | paper-v1:2605.28112 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28112 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28112 | no |
| SF-2026-ARXIV-2605-28116 | arXiv:2605.28116v1 | paper-v1:2605.28116 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28116 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28116 | no |
| SF-2026-ARXIV-2605-28122 | arXiv:2605.28122v1 | paper-v1:2605.28122 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28122 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28122 | no |
| SF-2026-ARXIV-2605-28158 | arXiv:2605.28158v1 | paper-v1:2605.28158 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28158 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28158 | no |
| SF-2026-ARXIV-2605-28201 | arXiv:2605.28201v1 | paper-v1:2605.28201 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28201 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-28201 | no |
| SF-2026-ARXIV-2605-28213 | arXiv:2605.28213v1 | paper-v1:2605.28213 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28213 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28213 | no |
| SF-2026-ARXIV-2605-28214 | arXiv:2605.28214v1 | paper-v1:2605.28214 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28214 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28214 | no |
| SF-2026-ARXIV-2605-28224 | arXiv:2605.28224v1 | paper-v1:2605.28224 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28224 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28224 | no |
| SF-2026-ARXIV-2605-28282 | arXiv:2605.28282v1 | paper-v1:2605.28282 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28282 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28282 | no |
| SF-2026-ARXIV-2605-28302 | arXiv:2605.28302v1 | paper-v1:2605.28302 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28302 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28302 | no |
| SF-2026-ARXIV-2605-28354 | arXiv:2605.28354v1 | paper-v1:2605.28354 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28354 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28354 | no |
| SF-2026-ARXIV-2605-28371 | arXiv:2605.28371v1 | paper-v1:2605.28371 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28371 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28371 | no |
| SF-2026-ARXIV-2605-28384 | arXiv:2605.28384v1 | paper-v1:2605.28384 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28384 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28384 | no |
| SF-2026-ARXIV-2605-28390 | arXiv:2605.28390v1 | paper-v1:2605.28390 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28390 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28390 | no |
| SF-2026-ARXIV-2605-28424 | arXiv:2605.28424v1 | paper-v1:2605.28424 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28424 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28424 | no |
| SF-2026-ARXIV-2605-28433 | arXiv:2605.28433v1 | paper-v1:2605.28433 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28433 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-28433 | no |
| SF-2026-ARXIV-2605-28467 | arXiv:2605.28467v1 | paper-v1:2605.28467 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28467 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28467 | no |
| SF-2026-ARXIV-2605-28480 | arXiv:2605.28480v1 | paper-v1:2605.28480 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28480 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28480 | no |
| SF-2026-ARXIV-2605-28508 | arXiv:2605.28508v1 | paper-v1:2605.28508 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28508 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28508 | no |
| SF-2026-ARXIV-2605-28510 | arXiv:2605.28510v1 | paper-v1:2605.28510 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28510 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28510 | no |
| SF-2026-ARXIV-2605-28544 | arXiv:2605.28544v1 | paper-v1:2605.28544 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28544 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28544 | no |
| SF-2026-ARXIV-2605-28561 | arXiv:2605.28561v1 | paper-v1:2605.28561 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28561 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28561 | no |
| SF-2026-ARXIV-2605-28565 | arXiv:2605.28565v1 | paper-v1:2605.28565 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28565 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28565 | no |
| SF-2026-ARXIV-2605-28573 | arXiv:2605.28573v1 | paper-v1:2605.28573 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28573 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28573 | no |
| SF-2026-ARXIV-2605-28617 | arXiv:2605.28617v1 | paper-v1:2605.28617 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28617 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-28617 | no |
| SF-2026-ARXIV-2605-28632 | arXiv:2605.28632v1 | paper-v1:2605.28632 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28632 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-28632 | no |
| SF-2026-ARXIV-2605-28634 | arXiv:2605.28634v1 | paper-v1:2605.28634 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28634 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28634 | no |
| SF-2026-ARXIV-2605-28640 | arXiv:2605.28640v1 | paper-v1:2605.28640 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28640 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28640 | no |
| SF-2026-ARXIV-2605-28646 | arXiv:2605.28646v1 | paper-v1:2605.28646 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28646 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28646 | no |
| SF-2026-ARXIV-2605-28678 | arXiv:2605.28678v1 | paper-v1:2605.28678 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28678 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28678 | no |
| SF-2026-ARXIV-2605-28691 | arXiv:2605.28691v1 | paper-v1:2605.28691 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28691 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28691 | no |
| SF-2026-ARXIV-2605-28699 | arXiv:2605.28699v1 | paper-v1:2605.28699 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28699 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28699 | no |
| SF-2026-ARXIV-2605-28704 | arXiv:2605.28704v1 | paper-v1:2605.28704 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28704 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-28704 | no |
| SF-2026-ARXIV-2605-28721 | arXiv:2605.28721v1 | paper-v1:2605.28721 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28721 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28721 | no |
| SF-2026-ARXIV-2605-28726 | arXiv:2605.28726v1 | paper-v1:2605.28726 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28726 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28726 | no |
| SF-2026-ARXIV-2605-28732 | arXiv:2605.28732v1 | paper-v1:2605.28732 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28732 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28732 | no |
| SF-2026-ARXIV-2605-28742 | arXiv:2605.28742v1 | paper-v1:2605.28742 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28742 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28742 | no |
| SF-2026-ARXIV-2605-28751 | arXiv:2605.28751v1 | paper-v1:2605.28751 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28751 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28751 | no |
| SF-2026-ARXIV-2605-28760 | arXiv:2605.28760v1 | paper-v1:2605.28760 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-28760 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-28760 | no |
| SF-2026-ARXIV-2605-28764 | arXiv:2605.28764v1 | paper-v1:2605.28764 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28764 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28764 | no |
| SF-2026-ARXIV-2605-28773 | arXiv:2605.28773v1 | paper-v1:2605.28773 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28773 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28773 | no |
| SF-2026-ARXIV-2605-28774 | arXiv:2605.28774v1 | paper-v1:2605.28774 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28774 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28774 | no |
| SF-2026-ARXIV-2605-28778 | arXiv:2605.28778v1 | paper-v1:2605.28778 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28778 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28778 | no |
| SF-2026-ARXIV-2605-28787 | arXiv:2605.28787v1 | paper-v1:2605.28787 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28787 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28787 | no |
| SF-2026-ARXIV-2605-28803 | arXiv:2605.28803v1 | paper-v1:2605.28803 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28803 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28803 | no |
| SF-2026-ARXIV-2605-28805 | arXiv:2605.28805v1 | paper-v1:2605.28805 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28805 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28805 | no |
| SF-2026-ARXIV-2605-28807 | arXiv:2605.28807v1 | paper-v1:2605.28807 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28807 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28807 | no |
| SF-2026-ARXIV-2605-28819 | arXiv:2605.28819v1 | paper-v1:2605.28819 | 2026-W22 | 2026-05-28 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-28819 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28819 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27390 | RP-a4a926f7da00ccbf | deep | arXiv:2605.27390v1 | SRC-ARXIV@arXiv:2605.27390v1 | https://arxiv.org/html/2605.27390v1#S2 | https://arxiv.org/html/2605.27390v1#S4 | https://arxiv.org/html/2605.27390v1#S6 | Not Disclosed — exact-v1 review found no versioned public artifact contract | claim:SF-2026-ARXIV-2605-27390 | complete |
| SF-2026-ARXIV-2605-27428 | RP-371fa5429e5e90ff | deep | arXiv:2605.27428v1 | SRC-ARXIV@arXiv:2605.27428v1 | arXiv:2605.27428v1 HTML — §2 System Model and Problem Formulation; §3 E 3 -Agent Architecture; §3.2 Architecture Overview | arXiv:2605.27428v1 HTML — §4 Experiments; §4.1 Experimental Setup; §4.2 Results | arXiv:2605.27428v1 HTML — §5 Conclusion and Future Work | https://arxiv.org/html/2605.27428v1; sha256:72a16faf7fa85f729f828ff9fe77c359ec947a6af4bc5b0056cf58507fcd1e9d | claim:SF-2026-ARXIV-2605-27428 | complete |
| SF-2026-ARXIV-2605-27432 | RP-42cf134168eb2253 | deep | arXiv:2605.27432v1 | SRC-ARXIV@arXiv:2605.27432v1 | https://arxiv.org/html/2605.27432v1 — §4 federated dual-system retrieval and compact QA memory | https://arxiv.org/html/2605.27432v1 — §5 experiments | https://arxiv.org/html/2605.27432v1 — Appendix D privacy/cost analysis; no general privacy guarantee | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27432 | complete |
| SF-2026-ARXIV-2605-27435 | RP-b64815f80025c282 | deep | arXiv:2605.27435v1 | SRC-ARXIV@arXiv:2605.27435v1 | https://arxiv.org/html/2605.27435v1 — §3 Stage-Level Mobile LLM Method | https://arxiv.org/html/2605.27435v1 — §4 CPU/GPU/NPU Evaluation | https://arxiv.org/html/2605.27435v1 — §5 Discussion and device/model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27435 | complete |
| SF-2026-ARXIV-2605-27437 | RP-a720725bcd86910c | deep | arXiv:2605.27437v1 | SRC-ARXIV@arXiv:2605.27437v1 | https://arxiv.org/html/2605.27437v1 — §3 memory-guided reflective retrieval | https://arxiv.org/html/2605.27437v1 — §4 long-dialogue experiments | https://arxiv.org/html/2605.27437v1 — §5 Discussion; tested-memory/task and extra-latency boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27437 | complete |
| SF-2026-ARXIV-2605-27461 | RP-1e2f80c22d53fb2c | deep | arXiv:2605.27461v1 | SRC-ARXIV@arXiv:2605.27461v1 | arXiv:2605.27461v1 HTML — §II hardware/software; §III execution; §IV data collection and training loop | arXiv:2605.27461v1 HTML — §V results and §VI deployment failures/lessons | arXiv:2605.27461v1 HTML — §VII Conclusion; one factory task, 2,535 episodes and no cross-site generality | arXiv:2605.27461v1 artifact links; immutable commit Not Disclosed unless stated in paper | claim:SF-2026-ARXIV-2605-27461 | complete |
| SF-2026-ARXIV-2605-27466 | RP-9d64cc432fcbd2a0 | deep | arXiv:2605.27466v1 | SRC-ARXIV@arXiv:2605.27466v1 | arXiv:2605.27466v1 — § exact heading: 2.1 Reasoning and Agent Design Patterns — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27466v1 — § exact heading: 2.5 Relative Trajectory Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27466v1 — § exact heading: 7 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27466v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27466 | complete |
| SF-2026-ARXIV-2605-27480 | RP-d7ed7eea2a46b47f | deep | arXiv:2605.27480v1 | SRC-ARXIV@arXiv:2605.27480v1 | arXiv:2605.27480v1 — § exact heading: 3 The BIRDS Framework — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27480v1 — § exact heading: 4 Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27480v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27480v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27480 | complete |
| SF-2026-ARXIV-2605-27483 | RP-555236766da17549 | deep | arXiv:2605.27483v1 | SRC-ARXIV@arXiv:2605.27483v1 | arXiv:2605.27483v1 — § exact heading: 3 Methods — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27483v1 — § exact heading: 3.5 Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27483v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27483v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27483 | complete |
| SF-2026-ARXIV-2605-27488 | RP-2a9d5cbfa1a058c6 | deep | arXiv:2605.27488v1 | SRC-ARXIV@arXiv:2605.27488v1 | arXiv:2605.27488v1 — §3 threat model; §4 eBPF interception and TLS channel-binding attestation; §5 delegation | arXiv:2605.27488v1 — §6 prototype evaluation and attack checks | arXiv:2605.27488v1 — §7 limitations — Linux/eBPF, visible network channels, trusted guard/attestation and prototype workload boundary | arXiv:2605.27488v1 — official v1 body; immutable prototype commit Not Disclosed | claim:SF-2026-ARXIV-2605-27488 | complete |
| SF-2026-ARXIV-2605-27489 | RP-2a3b3d9037b15a3e | deep | arXiv:2605.27489v1 | SRC-ARXIV@arXiv:2605.27489v1 | arXiv:2605.27489v1 — § exact heading: 3 Methodology — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27489v1 — § exact heading: 4 Results — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27489v1 — § exact heading: 4.3 Aggregate Comparison Across Vulnerability Types — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27489v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27489 | complete |
| SF-2026-ARXIV-2605-27491 | RP-fa24d10ae8979ba9 | deep | arXiv:2605.27491v1 | SRC-ARXIV@arXiv:2605.27491v1 | arXiv:2605.27491v1 — § exact heading: GE-Base: Multi-View Video World Foundation Model — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27491v1 — § exact heading: Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27491v1 — § exact heading: Instructions for reporting errors — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27491v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27491 | complete |
| SF-2026-ARXIV-2605-27492 | RP-bf29065c56b5f501 | deep | arXiv:2605.27492v1 | SRC-ARXIV@arXiv:2605.27492v1 | arXiv:2605.27492v1 — §3 runtime assessment architecture, serial evolution/resurrection workloads and metrics | arXiv:2605.27492v1 — §4 production-grounded agent results | arXiv:2605.27492v1 — §6 Limitations — bounded software-engineering agents/platform and runtime artifacts; paper template metadata is anomalous | arXiv:2605.27492v1 — official v1 body; YatCC/RAMP immutable version Not Disclosed | claim:SF-2026-ARXIV-2605-27492 | complete |
| SF-2026-ARXIV-2605-27494 | RP-6fde3c4711426ce8 | deep | arXiv:2605.27494v1 | SRC-ARXIV@arXiv:2605.27494v1 | arXiv:2605.27494v1 — §3.1–3.4 pipeline, evidence signature, four validation gates and compression fallback | arXiv:2605.27494v1 — §4 setup/metrics; §5 HotpotQA and mtRAG results/ablations | arXiv:2605.27494v1 — §7 Limitations — two datasets, Qwen2.5-7B/vLLM, lexical/judge support and small per-regime samples | arXiv:2605.27494v1 — official v1 body says implementation/harness released; immutable commit Not Disclosed | claim:SF-2026-ARXIV-2605-27494 | complete |
| SF-2026-ARXIV-2605-27547 | RP-4aafb1f7a9e5fa3e | deep | arXiv:2605.27547v1 | SRC-ARXIV@arXiv:2605.27547v1 | arXiv:2605.27547v1 — § exact heading: 1 Introduction — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27547v1 — § exact heading: 2 Risk-Aware Option Clearing (ROC) — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27547v1 — § exact heading: 4 Discussion and Outlook — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27547v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27547 | complete |
| SF-2026-ARXIV-2605-27559 | RP-69403f13655cf87b | deep | arXiv:2605.27559v1 | SRC-ARXIV@arXiv:2605.27559v1 | arXiv:2605.27559v1 — § exact heading: 3.1 Models and Benchmarks — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27559v1 — § exact heading: 3 Experimental Setup — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27559v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27559v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27559 | complete |
| SF-2026-ARXIV-2605-27566 | RP-5eeed043bd39c00e | deep | arXiv:2605.27566v1 | SRC-ARXIV@arXiv:2605.27566v1 | arXiv:2605.27566v1 — §3 Benchmark Design; §4 Scheduling Agents (official exact-v1 HTML read) | arXiv:2605.27566v1 — §5 Workloads and calibrated-baseline results (official exact-v1 HTML read) | arXiv:2605.27566v1 — §6 Observability paradox and limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27566v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27566 | complete |
| SF-2026-ARXIV-2605-27569 | RP-07d5ba0e08714105 | deep | arXiv:2605.27569v1 | SRC-ARXIV@arXiv:2605.27569v1 | arXiv:2605.27569v1 — § exact heading: 4.1 Datasets and model architecture — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27569v1 — § exact heading: 3 Representation-Level Evaluation — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27569v1 — § exact heading: 6 Discussion and Conclusion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27569v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27569 | complete |
| SF-2026-ARXIV-2605-27575 | RP-ac150648f7eff4ba | deep | arXiv:2605.27575v1 | SRC-ARXIV@arXiv:2605.27575v1 | arXiv:2605.27575v1 — §3 Platform Architecture; §4 Agent Definition as Code (official exact-v1 HTML read) | arXiv:2605.27575v1 — §5 Evaluation (official exact-v1 HTML read) | arXiv:2605.27575v1 — §6 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27575v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27575 | complete |
| SF-2026-ARXIV-2605-27589 | RP-2321c83d9cdc236b | deep | arXiv:2605.27589v1 | SRC-ARXIV@arXiv:2605.27589v1 | arXiv:2605.27589v1 — § exact heading: 4.3 When World Model Fails: Per-Primitive Analysis — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27589v1 — § exact heading: 3 The What-If World Benchmark — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27589v1 — § exact heading: 4.2 Why Paired Evaluation Matters: The Hidden Failure Stratum — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27589v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27589 | complete |
| SF-2026-ARXIV-2605-27599 | RP-22db62426a1447c1 | deep | arXiv:2605.27599v1 | SRC-ARXIV@arXiv:2605.27599v1 | arXiv:2605.27599v1 — §2 Hardware Audit Methodology, Table 1 and seven-interface audit on one GX10 | arXiv:2605.27599v1 — §5 What the GB10 Does Expose: Rich Telemetry, No Energy, Table 2; §6 external-meter fallback feasibility and limits | arXiv:2605.27599v1 — §2 scope note; §3 unvalidated SPBM corroboration; §6 attribution uncertainty, coarse boundary and overhead | exact-v1 URL=https://arxiv.org/html/2605.27599v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27599 | complete |
| SF-2026-ARXIV-2605-27621 | RP-623b3ad46e7d2b97 | deep | arXiv:2605.27621v1 | SRC-ARXIV@arXiv:2605.27621v1 | arXiv:2605.27621v1 — § exact heading: 3 A Unified Framework for Agent Attribution — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27621v1 — § exact heading: 4 Benchmarks and MAS Architectures — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27621v1 — § exact heading: Limitations and Future Work — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27621v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27621 | complete |
| SF-2026-ARXIV-2605-27630 | RP-56b82479c92e5272 | deep | arXiv:2605.27630v1 | SRC-ARXIV@arXiv:2605.27630v1 | arXiv:2605.27630v1 — § exact heading: 4 Methodology — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27630v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27630v1 — § exact heading: 6.4 Failure analysis — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27630v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27630 | complete |
| SF-2026-ARXIV-2605-27668 | RP-ae1214c99237021d | deep | arXiv:2605.27668v1 | SRC-ARXIV@arXiv:2605.27668v1 | arXiv:2605.27668v1 — § exact heading: 4.2 Model architecture and input — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27668v1 — § exact heading: 3.2 Evaluation metrics — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27668v1 — § exact heading: Appendix A Limitations — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27668v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27668 | complete |
| SF-2026-ARXIV-2605-27671 | RP-10b25059ef1fc35f | deep | arXiv:2605.27671v1 | SRC-ARXIV@arXiv:2605.27671v1 | arXiv:2605.27671v1 — §3 Geometric signature and multi-turn evolution (official exact-v1 HTML read) | arXiv:2605.27671v1 — §4 Experiments (official exact-v1 HTML read) | arXiv:2605.27671v1 — §5 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27671v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27671 | complete |
| SF-2026-ARXIV-2605-27678 | RP-f259b6737a8292dc | deep | arXiv:2605.27678v1 | SRC-ARXIV@arXiv:2605.27678v1 | arXiv:2605.27678v1 — §3.1–3.3 non-colocated/colocated communicators and heterogeneous pipeline orchestration | arXiv:2605.27678v1 — §4 operating-regime sweep; §5 step-level parity and convergence validation | arXiv:2605.27678v1 — Reasoned exception — manuscript has no dedicated Limitations section; §4 Operating regimes and §5 Convergence validation bind claims to tuned Megatron-LM multimodal workloads, disclosed GPU/layout search and convergence cases | arXiv:2605.27678v1 — open-source Megatron-LM extension; immutable event-time commit Not Disclosed | claim:SF-2026-ARXIV-2605-27678 | complete |
| SF-2026-ARXIV-2605-27681 | RP-591ce780d9b7c4e0 | deep | arXiv:2605.27681v1 | SRC-ARXIV@arXiv:2605.27681v1 | arXiv:2605.27681v1 — § exact heading: Appendix A System prompts — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27681v1 — § exact heading: 4 Experimental Results — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27681v1 — § exact heading: 5 Discussion and Conclusion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27681v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27681 | complete |
| SF-2026-ARXIV-2605-27690 | RP-d10d8a4e9b660bc5 | deep | arXiv:2605.27690v1 | SRC-ARXIV@arXiv:2605.27690v1 | arXiv:2605.27690v1 — §3 TRACES trajectory-state model, weak supervision and prefix-risk scoring | arXiv:2605.27690v1 — §4 setup; §5 proactive-detection results and ablations | arXiv:2605.27690v1 — §6 Limitations — observer/model/task/attack coverage, weak labels and hidden-state access assumptions | arXiv:2605.27690v1 — official v1 body; immutable code/checkpoint Not Disclosed | claim:SF-2026-ARXIV-2605-27690 | complete |
| SF-2026-ARXIV-2605-27710 | RP-a499391d660f4da0 | deep | arXiv:2605.27710v1 | SRC-ARXIV@arXiv:2605.27710v1 | arXiv:2605.27710v1 — §3 Evidence-escalation pipeline (official exact-v1 HTML read) | arXiv:2605.27710v1 — §4 Evaluation (official exact-v1 HTML read) | arXiv:2605.27710v1 — §6 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27710v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27710 | complete |
| SF-2026-ARXIV-2605-27712 | RP-bb42682b4f6fae3e | deep | arXiv:2605.27712v1 | SRC-ARXIV@arXiv:2605.27712v1 | arXiv:2605.27712v1 — § exact heading: 4 Method — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27712v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27712v1 — § exact heading: 6 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27712v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27712 | complete |
| SF-2026-ARXIV-2605-27720 | RP-82f65091714d965c | deep | arXiv:2605.27720v1 | SRC-ARXIV@arXiv:2605.27720v1 | arXiv:2605.27720v1 — §3 probabilistic landing capability; §4 Bayesian posterior approval/risk rule | arXiv:2605.27720v1 — §5 finite-rollout simulation study and sensitivity | arXiv:2605.27720v1 — §6 Limitations — landing-controller/simulation prior/model assumptions; posterior approval is not field certification | arXiv:2605.27720v1 — official v1 body; simulator/policy artifact Not Disclosed | claim:SF-2026-ARXIV-2605-27720 | complete |
| SF-2026-ARXIV-2605-27744 | RP-f17fc9ce1f41c43f | deep | arXiv:2605.27744v1 | SRC-ARXIV@arXiv:2605.27744v1 | arXiv:2605.27744v1 — §3 runtime-layer interface and policy hooks; §4 lifecycle/control-plane design | arXiv:2605.27744v1 — §5 prototype policies and serving experiments | arXiv:2605.27744v1 — §6 Limitations — prototype stack, declared agent semantics and engine-hook assumptions; no universal policy correctness | arXiv:2605.27744v1 — official v1 body; immutable runtime commit Not Disclosed | claim:SF-2026-ARXIV-2605-27744 | complete |
| SF-2026-ARXIV-2605-27752 | RP-ad9c2c738f65a210 | deep | arXiv:2605.27752v1 | SRC-ARXIV@arXiv:2605.27752v1 | arXiv:2605.27752v1 — §3 Calibration protocols (official exact-v1 HTML read) | arXiv:2605.27752v1 — §4 Experiments (official exact-v1 HTML read) | arXiv:2605.27752v1 — §5 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27752v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27752 | complete |
| SF-2026-ARXIV-2605-27759 | RP-eb62e60c6cdfaaeb | deep | arXiv:2605.27759v1 | SRC-ARXIV@arXiv:2605.27759v1 | arXiv:2605.27759v1 — § exact heading: I Introduction — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27759v1 — § exact heading: I Introduction — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27759v1 — § exact heading: I Introduction — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27759v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27759 | complete |
| SF-2026-ARXIV-2605-27760 | RP-64df3754ad14c82f | deep | arXiv:2605.27760v1 | SRC-ARXIV@arXiv:2605.27760v1 | arXiv:2605.27760v1 — §3 SkillGrad update loop (official exact-v1 HTML read) | arXiv:2605.27760v1 — §4 Experiments (official exact-v1 HTML read) | arXiv:2605.27760v1 — §5 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27760v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27760 | complete |
| SF-2026-ARXIV-2605-27761 | RP-84b7ca708fe98097 | deep | arXiv:2605.27761v1 | SRC-ARXIV@arXiv:2605.27761v1 | arXiv:2605.27761v1 — § exact heading: 3. Method — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27761v1 — § exact heading: 2.2. Evaluation of GUI Agents — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27761v1 — § exact heading: 4.4. Failure Mode Analysis — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27761v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27761 | complete |
| SF-2026-ARXIV-2605-27763 | RP-b803035ca146ec0f | deep | arXiv:2605.27763v1 | SRC-ARXIV@arXiv:2605.27763v1 | arXiv:2605.27763v1 — §3.1–3.7 paired four-study protocol and synthesis rules | arXiv:2605.27763v1 — §4 results including batch-invariant-kernel ablation | arXiv:2605.27763v1 — §5.3 non-claims; §5.4 rare events, scoring, co-batch verification and local-first limitations | arXiv:2605.27763v1 — Appendix A/B study provenance and C artifact availability; immutable bundle hash Not Disclosed | claim:SF-2026-ARXIV-2605-27763 | complete |
| SF-2026-ARXIV-2605-27766 | RP-7b20fa17796ead14 | deep | arXiv:2605.27766v1 | SRC-ARXIV@arXiv:2605.27766v1 | arXiv:2605.27766v1 — §3 Persistent multi-agent simulation (official exact-v1 HTML read) | arXiv:2605.27766v1 — §4 Privacy evaluation (official exact-v1 HTML read) | arXiv:2605.27766v1 — §5 Limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27766v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27766 | complete |
| SF-2026-ARXIV-2605-27784 | RP-67fae486519c7efb | deep | arXiv:2605.27784v1 | SRC-ARXIV@arXiv:2605.27784v1 | arXiv:2605.27784v1 — §3 WIRE extraction, SAT nomination and witnessed realization (official exact-v1 HTML read) | arXiv:2605.27784v1 — §4 Evaluation (official exact-v1 HTML read) | arXiv:2605.27784v1 — §6 stated non-goals and limitations (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27784v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27784 | complete |
| SF-2026-ARXIV-2605-27785 | RP-fa65566eb0254928 | deep | arXiv:2605.27785v1 | SRC-ARXIV@arXiv:2605.27785v1 | arXiv:2605.27785v1 — §3 embedded query-engine architecture, relational/model operator split and bounded execution | arXiv:2605.27785v1 — §4 implementation; §5 trace/log query workloads and evaluation | arXiv:2605.27785v1 — §6 limitations — client/runtime, model-operator cost/semantics and disclosed data/workload boundary | arXiv:2605.27785v1 — official v1 body; immutable engine release commit Not Disclosed | claim:SF-2026-ARXIV-2605-27785 | complete |
| SF-2026-ARXIV-2605-27789 | RP-259ba0ee6eef5f12 | deep | arXiv:2605.27789v1 | SRC-ARXIV@arXiv:2605.27789v1 | arXiv:2605.27789v1 — § exact heading: 3 Method — method/identity fragment (official exact-v1 HTML read) | arXiv:2605.27789v1 — § exact heading: 4 Experimental Setup — evaluation/result fragment (official exact-v1 HTML read) | arXiv:2605.27789v1 — § exact heading: 5.4 Ablation discussion — limitations/counterevidence fragment (official exact-v1 HTML read) | exact-v1 URL=https://arxiv.org/html/2605.27789v1; immutable code/data commit Not Disclosed unless named in body | claim:SF-2026-ARXIV-2605-27789 | complete |
| SF-2026-ARXIV-2605-27820 | RP-155b8722fbc8b2b9 | deep | arXiv:2605.27820v1 | SRC-ARXIV@arXiv:2605.27820v1 | arXiv:2605.27820v1 — § exact heading: 3.3 Task Design and Ground-truth Annotation | arXiv:2605.27820v1 — § exact heading: 2.1 Tool-Using Benchmarks | arXiv:2605.27820v1 — § exact heading: 5 Conclusions | arXiv:2605.27820v1 — official HTML sha256=e084884e79524dd4bd757618cb34c671331dce1673eadac18e0b6881d86642d3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27820 | complete |
| SF-2026-ARXIV-2605-27825 | RP-c658005636a888e6 | deep | arXiv:2605.27825v1 | SRC-ARXIV@arXiv:2605.27825v1 | arXiv:2605.27825v1 — § exact heading: 3 Threat Model and Problem Formulation | arXiv:2605.27825v1 — § exact heading: 5 Experiments | arXiv:2605.27825v1 — § exact heading: 7 Conclusion and Limitations | arXiv:2605.27825v1 — official HTML sha256=778098e7df5cf172ed04989da043124faf4d825232bb02bbc1ceeeb0aa110f9a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27825 | complete |
| SF-2026-ARXIV-2605-27850 | RP-aae7181040b83a3f | deep | arXiv:2605.27850v1 | SRC-ARXIV@arXiv:2605.27850v1 | arXiv:2605.27850v1 — §3 Methods: unified prompt-topology genome and adaptive Pareto control | arXiv:2605.27850v1 — §4 Experiments: held-out accuracy, token cost and topology complexity | arXiv:2605.27850v1 — §5 Conclusion, Limitations, and Future Work | arXiv:2605.27850v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27850 | complete |
| SF-2026-ARXIV-2605-27879 | RP-020f349e3469ca91 | deep | arXiv:2605.27879v1 | SRC-ARXIV@arXiv:2605.27879v1 | arXiv:2605.27879v1 — § exact heading: 3 Method: Faithful Agentic XAI | arXiv:2605.27879v1 — § exact heading: 4.2 Evaluation scenarios | arXiv:2605.27879v1 — § exact heading: 6 Conclusions | arXiv:2605.27879v1 — official HTML sha256=6414fd88678b2d30e7ef60804106d0d709040c51a69d5a37d2f507bfcb6a22c3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27879 | complete |
| SF-2026-ARXIV-2605-27881 | RP-c4854d16b833a898 | deep | arXiv:2605.27881v1 | SRC-ARXIV@arXiv:2605.27881v1 | arXiv:2605.27881v1 — § exact heading: 2.1 Reward Design for Search Agent | arXiv:2605.27881v1 — § exact heading: 3 Experiments Setup | arXiv:2605.27881v1 — § exact heading: Limitations | arXiv:2605.27881v1 — official HTML sha256=07bf6c9ae6e5fe2bbe5681bcaa7fbc987ad4ff370478f650c574244e5f99a760; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27881 | complete |
| SF-2026-ARXIV-2605-27898 | RP-9a0327329c096038 | deep | arXiv:2605.27898v1 | SRC-ARXIV@arXiv:2605.27898v1 | arXiv:2605.27898v1 — § exact heading: 2 Unified Framework | arXiv:2605.27898v1 — § exact heading: 2.5 Evaluation Methodology | arXiv:2605.27898v1 — § exact heading: 3.5 Failure Result Analysis | arXiv:2605.27898v1 — official HTML sha256=7ee4e3fea5ae787e7b7369f9df610a0f7893a5f73d7d984cc659f19fc82c6ecd; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27898 | complete |
| SF-2026-ARXIV-2605-27899 | RP-f9a707b07cfcef12 | deep | arXiv:2605.27899v1 | SRC-ARXIV@arXiv:2605.27899v1 | arXiv:2605.27899v1 — § exact heading: 3 Method | arXiv:2605.27899v1 — § exact heading: 4 Experiments | arXiv:2605.27899v1 — § exact heading: 5 Conclusion | arXiv:2605.27899v1 — official HTML sha256=54f2f7366208bc5806dd940984e523d58fd223db4b28a057e2ef039098f1f0ad; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27899 | complete |
| SF-2026-ARXIV-2605-27901 | RP-e23ce50110f8dc9b | deep | arXiv:2605.27901v1 | SRC-ARXIV@arXiv:2605.27901v1 | arXiv:2605.27901v1 — § exact heading: 4 Can models conceal their reasoning across different languages? | arXiv:2605.27901v1 — § exact heading: 3 Experimental Setup | arXiv:2605.27901v1 — § exact heading: 8 Conclusion | arXiv:2605.27901v1 — official HTML sha256=a6ba0236d1abd1ae5608efa74db512b77c0445c54532de292db24bf296c6295c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27901 | complete |
| SF-2026-ARXIV-2605-27918 | RP-4eded30f71160a12 | deep | arXiv:2605.27918v1 | SRC-ARXIV@arXiv:2605.27918v1 | arXiv:2605.27918v1 — § exact heading: 2.1. MLLM Architecture and Parallelism | arXiv:2605.27918v1 — § exact heading: 4. Macroscopic Analysis-Based Model Parallelization | arXiv:2605.27918v1 — § exact heading: 2.3. Limitations of Existing Works | arXiv:2605.27918v1 — official HTML sha256=22c10a9201b86eead7234ee23182de2058869658bcc76c034c3d95bd886271f3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27918 | complete |
| SF-2026-ARXIV-2605-27922 | RP-98e56aea9aeea8cb | deep | arXiv:2605.27922v1 | SRC-ARXIV@arXiv:2605.27922v1 | arXiv:2605.27922v1 — § exact heading: 3.2 Task Suite Design and Validation | arXiv:2605.27922v1 — § exact heading: 3 The Harness-Bench Benchmark | arXiv:2605.27922v1 — § exact heading: 5.1 Observed Failure Symptoms | arXiv:2605.27922v1 — official HTML sha256=3e89c9f28b68276bc33fde7581b7a8428c53bb33ffa950e94aa7ed757cab807c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27922 | complete |
| SF-2026-ARXIV-2605-27947 | RP-a0b4bf3351a1c004 | deep | arXiv:2605.27947v1 | SRC-ARXIV@arXiv:2605.27947v1 | arXiv:2605.27947v1 — § exact heading: 3 Method | arXiv:2605.27947v1 — § exact heading: 4 Experiments | arXiv:2605.27947v1 — § exact heading: 5 Limitations | arXiv:2605.27947v1 — official HTML sha256=6775e77796d135354ae93c0db230ddba4574e84d3cf09c0aa4602b17ce622867; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27947 | complete |
| SF-2026-ARXIV-2605-27954 | RP-fb73eba68c6c62df | deep | arXiv:2605.27954v1 | SRC-ARXIV@arXiv:2605.27954v1 | arXiv:2605.27954v1 — § exact heading: 1 Introduction | arXiv:2605.27954v1 — § exact heading: 4.2 Experimental Settings | arXiv:2605.27954v1 — § exact heading: 6 Conclusion | arXiv:2605.27954v1 — official HTML sha256=2b0011952bb538ff67435afde77b7104a2654683eeb7f17f4e3b82e26a89afa1; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27954 | complete |
| SF-2026-ARXIV-2605-27957 | RP-6c465506657a35d9 | deep | arXiv:2605.27957v1 | SRC-ARXIV@arXiv:2605.27957v1 | arXiv:2605.27957v1 — § exact heading: 4.6 Reasoning-Optimized Models and Instruction Clash | arXiv:2605.27957v1 — § exact heading: 2.1 Tool-Augmented and Multi-Step Planning Benchmarks | arXiv:2605.27957v1 — § exact heading: 4.5 Failure Mode Analysis | arXiv:2605.27957v1 — official HTML sha256=248798608249a4b17d5fa271b948eefaf1bb5408fa419864abf81f260bc8c5e6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27957 | complete |
| SF-2026-ARXIV-2605-27963 | RP-c0ed21cde0c6e5ff | deep | arXiv:2605.27963v1 | SRC-ARXIV@arXiv:2605.27963v1 | arXiv:2605.27963v1 — § exact heading: 2.1. Analytical Models on Performance | arXiv:2605.27963v1 — § exact heading: 4.4. Resultant Topologies | arXiv:2605.27963v1 — § exact heading: 8. Conclusion | arXiv:2605.27963v1 — official HTML sha256=8ab4cf20fc446530aa8902eaa42a687c616adf1e944c3c43337c1bd8440106c7; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27963 | complete |
| SF-2026-ARXIV-2605-27980 | RP-abf8fcc9a899d0c9 | deep | arXiv:2605.27980v1 | SRC-ARXIV@arXiv:2605.27980v1 | arXiv:2605.27980v1 — § exact heading: 3 Method | arXiv:2605.27980v1 — § exact heading: 4 Experimental Setup | arXiv:2605.27980v1 — § exact heading: 6 Limitations | arXiv:2605.27980v1 — official HTML sha256=20b0adb216b2e7b519721df4af90508fc41737dc57300f9be6baf9753f22ae78; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27980 | complete |
| SF-2026-ARXIV-2605-27995 | RP-963ab6f4da612389 | deep | arXiv:2605.27995v1 | SRC-ARXIV@arXiv:2605.27995v1 | arXiv:2605.27995v1 — § exact heading: 2.1 Agent as a Concurrent Tool-Using System | arXiv:2605.27995v1 — § exact heading: 2.3 Evaluation | arXiv:2605.27995v1 — § exact heading: 4 Conclusion | arXiv:2605.27995v1 — official HTML sha256=707fad563547b29d77b0b377d0f1f896c52513d59f87543ff726262ca1f3754c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-27995 | complete |
| SF-2026-ARXIV-2605-28000 | RP-22b5d5fbe8456ca9 | deep | arXiv:2605.28000v1 | SRC-ARXIV@arXiv:2605.28000v1 | arXiv:2605.28000v1 — § exact heading: 3 Tool Forge Conceptual Framework | arXiv:2605.28000v1 — § exact heading: 9 Experimental Protocol and Baselines | arXiv:2605.28000v1 — § exact heading: 12 Limitations and Open Questions | arXiv:2605.28000v1 — official HTML sha256=5ea862c3ec5aea65324f90f20db2c7c7596ccee5e7250bd3c1675ae44ca0644b; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28000 | complete |
| SF-2026-ARXIV-2605-28009 | RP-3cff817aad4f097f | deep | arXiv:2605.28009v1 | SRC-ARXIV@arXiv:2605.28009v1 | arXiv:2605.28009v1 — § exact heading: Appendix E Use of Large Language Models | arXiv:2605.28009v1 — § exact heading: 5 Experiment | arXiv:2605.28009v1 — § exact heading: 7 Conclusions and Future Work | arXiv:2605.28009v1 — official HTML sha256=d6dda2a87c59fd4d07ba02d92c5f0c24c14d09a1096ddb8d79481b5dacfdd055; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28009 | complete |
| SF-2026-ARXIV-2605-28017 | RP-2d0ae18e7db31381 | deep | arXiv:2605.28017v1 | SRC-ARXIV@arXiv:2605.28017v1 | arXiv:2605.28017v1 — § exact heading: 4.4 Attack Methods | arXiv:2605.28017v1 — § exact heading: 3.2 Attack Evaluation in Prior Work | arXiv:2605.28017v1 — § exact heading: 6 Conclusion | arXiv:2605.28017v1 — official HTML sha256=341b7d7e7c46ce09f8c492be68070b3f9c85e07da5caa6d219cea5e2dcf678b6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28017 | complete |
| SF-2026-ARXIV-2605-28044 | RP-51205ceafa60aabf | deep | arXiv:2605.28044v1 | SRC-ARXIV@arXiv:2605.28044v1 | arXiv:2605.28044v1 — § exact heading: Appendix G Model API and Decoding Configuration | arXiv:2605.28044v1 — § exact heading: 5 Experiments | arXiv:2605.28044v1 — § exact heading: 6 Discussion | arXiv:2605.28044v1 — official HTML sha256=5b0d0423fc0dc00a6104deb2486a929aeab242779dfb2a336538c9d90949c46d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28044 | complete |
| SF-2026-ARXIV-2605-28046 | RP-a6910dd3aec0b75a | deep | arXiv:2605.28046v1 | SRC-ARXIV@arXiv:2605.28046v1 | arXiv:2605.28046v1 — § exact heading: 2.4 Proactive Systems | arXiv:2605.28046v1 — § exact heading: 4 Experiments | arXiv:2605.28046v1 — § exact heading: 5 Discussion | arXiv:2605.28046v1 — official HTML sha256=9de207b19cc99467ce05fbe4668f2af43818fe87622c2f2b9f2a2336444ace08; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28046 | complete |
| SF-2026-ARXIV-2605-28053 | RP-e95e807f5254ea71 | deep | arXiv:2605.28053v1 | SRC-ARXIV@arXiv:2605.28053v1 | arXiv:2605.28053v1 — § exact heading: 2.1 Serving with Mutable Model State | arXiv:2605.28053v1 — § exact heading: 5 Evaluation | arXiv:2605.28053v1 — § exact heading: 6 Discussion | arXiv:2605.28053v1 — official HTML sha256=d97dad61bd6b3336151a29c7da781ff5a05a6ddc2691377489479fbed0a234c5; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28053 | complete |
| SF-2026-ARXIV-2605-28071 | RP-d9b51a5c7e98636f | deep | arXiv:2605.28071v1 | SRC-ARXIV@arXiv:2605.28071v1 | arXiv:2605.28071v1 — § exact heading: 1. Introduction | arXiv:2605.28071v1 — § exact heading: 2. AgentGuard | arXiv:2605.28071v1 — § exact heading: 3. Conclusion | arXiv:2605.28071v1 — official HTML sha256=ae831e1a6bf504005cadb4b6e87783430807af808aa4d411b1586ff15d1a4a10; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28071 | complete |
| SF-2026-ARXIV-2605-28074 | RP-ef161b2366a39f16 | deep | arXiv:2605.28074v1 | SRC-ARXIV@arXiv:2605.28074v1 | arXiv:2605.28074v1 — § exact heading: 3.2. Threat Model | arXiv:2605.28074v1 — § exact heading: 5. Experiments | arXiv:2605.28074v1 — § exact heading: 8. Limitations | arXiv:2605.28074v1 — official HTML sha256=0fe32804f286c87a8344023ffd30d5f490a312ecc2910c900d6ce0e8d95981ae; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28074 | complete |
| SF-2026-ARXIV-2605-28083 | RP-4fea9f2d41c73df0 | deep | arXiv:2605.28083v1 | SRC-ARXIV@arXiv:2605.28083v1 | arXiv:2605.28083v1 — § exact heading: 2.1 Vision-Language-Action Models | arXiv:2605.28083v1 — § exact heading: 4 Experiments | arXiv:2605.28083v1 — § exact heading: 3.1 Preliminaries & Threat Model | arXiv:2605.28083v1 — official HTML sha256=75a70820341d7c1995d5dcce0f6e2ef4087be2e4ee456e5403fa26986a59e552; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28083 | complete |
| SF-2026-ARXIV-2605-28095 | RP-03b7e12ebb47d4dc | deep | arXiv:2605.28095v1 | SRC-ARXIV@arXiv:2605.28095v1 | arXiv:2605.28095v1 — § exact heading: 2.1 Large Language Models | arXiv:2605.28095v1 — § exact heading: 5 Evaluation | arXiv:2605.28095v1 — § exact heading: 4.4 Discussion | arXiv:2605.28095v1 — official HTML sha256=5a35d6208f87777291ee083ee28d0ca39f8edf85bbf757764809c8cc70d60976; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28095 | complete |
| SF-2026-ARXIV-2605-28097 | RP-8d4627538694de50 | deep | arXiv:2605.28097v1 | SRC-ARXIV@arXiv:2605.28097v1 | arXiv:2605.28097v1 — § exact heading: 3. Design | arXiv:2605.28097v1 — § exact heading: 5. Evaluation | arXiv:2605.28097v1 — § exact heading: 5.5. Failure-Mode Taxonomy | arXiv:2605.28097v1 — official HTML sha256=414916db7f1e595f656d28986787a19c47a828a3a85d39a16a19704252d2638a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28097 | complete |
| SF-2026-ARXIV-2605-28108 | RP-5539adb8f92fded8 | deep | arXiv:2605.28108v1 | SRC-ARXIV@arXiv:2605.28108v1 | arXiv:2605.28108v1 — § exact heading: Appendix B Runtime Framework | arXiv:2605.28108v1 — § exact heading: 2.2 Why ATR Resists Direct Evaluation | arXiv:2605.28108v1 — § exact heading: 6 Conclusion | arXiv:2605.28108v1 — official HTML sha256=955cb683e1219ce043363a3f80c8c78f68fcf31db7a68d671b8cbcbc921b93bd; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28108 | complete |
| SF-2026-ARXIV-2605-28112 | RP-7694f1692ae242dd | deep | arXiv:2605.28112v1 | SRC-ARXIV@arXiv:2605.28112v1 | arXiv:2605.28112v1 — § exact heading: 2.2 Threat Model and Attack Realism | arXiv:2605.28112v1 — § exact heading: 4 Experiments | arXiv:2605.28112v1 — § exact heading: 6 Conclusion | arXiv:2605.28112v1 — official HTML sha256=d0cbc74c408247a70679909334b0628c17fb424771394eb5869d80f3ad9c15f7; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28112 | complete |
| SF-2026-ARXIV-2605-28116 | RP-2235f77dfda50854 | deep | arXiv:2605.28116v1 | SRC-ARXIV@arXiv:2605.28116v1 | arXiv:2605.28116v1 — § exact heading: 3 Methodology | arXiv:2605.28116v1 — § exact heading: 4 Experiments | arXiv:2605.28116v1 — § exact heading: 3.1 Threat Model and Problem Setup | arXiv:2605.28116v1 — official HTML sha256=1468243f7898c335be4b2032a41fce144cd2cde51fbfa05bdec6192f398d54b1; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28116 | complete |
| SF-2026-ARXIV-2605-28122 | RP-efcc0ab75e4b2a81 | deep | arXiv:2605.28122v1 | SRC-ARXIV@arXiv:2605.28122v1 | arXiv:2605.28122v1 — § exact heading: 4 Methodology | arXiv:2605.28122v1 — § exact heading: 5 Evaluation | arXiv:2605.28122v1 — § exact heading: 6 Conclusion | arXiv:2605.28122v1 — official HTML sha256=2b2263367a509d311807ea14ffd2bbe1d4340d5061f31a11a4c27daea64d124d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28122 | complete |
| SF-2026-ARXIV-2605-28158 | RP-ebb20f983db08816 | deep | arXiv:2605.28158v1 | SRC-ARXIV@arXiv:2605.28158v1 | arXiv:2605.28158v1 — § exact heading: 4.3. Workspace Setting Matters: Filesystem vs. Flat Prompt | arXiv:2605.28158v1 — § exact heading: 3. OR-Space Benchmark | arXiv:2605.28158v1 — § exact heading: 4.6. Failure Analysis: What Workspace Evaluation Reveals | arXiv:2605.28158v1 — official HTML sha256=1e17ba2cca067758b922a556965e0431d6551145b624769cbaad189a8f57f6d0; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28158 | complete |
| SF-2026-ARXIV-2605-28201 | RP-7a47d77b54d201fe | deep | arXiv:2605.28201v1 | SRC-ARXIV@arXiv:2605.28201v1 | arXiv:2605.28201v1 — § exact heading: 1 Introduction | arXiv:2605.28201v1 — § exact heading: 3 Benchmark Construction | arXiv:2605.28201v1 — § exact heading: 5 Conclusion | arXiv:2605.28201v1 — official HTML sha256=008668763414245306a7e06dd0162aab018a8ec8de1d63dca6d2c395d1635c86; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28201 | complete |
| SF-2026-ARXIV-2605-28213 | RP-6bdb01b2c64f13a8 | deep | arXiv:2605.28213v1 | SRC-ARXIV@arXiv:2605.28213v1 | arXiv:2605.28213v1 — § exact heading: 3 Method | arXiv:2605.28213v1 — § exact heading: 4 Evaluation | arXiv:2605.28213v1 — § exact heading: 5 Conclusion | arXiv:2605.28213v1 — official HTML sha256=5a6c29327a16eb486f3ab87c7947285bdc6cf70c05861afc9e6be33047d4bd05; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28213 | complete |
| SF-2026-ARXIV-2605-28214 | RP-362f30749375e765 | deep | arXiv:2605.28214v1 | SRC-ARXIV@arXiv:2605.28214v1 | arXiv:2605.28214v1 — § exact heading: 2.1 Latent-based Multi-Agent Systems | arXiv:2605.28214v1 — § exact heading: 4 Experiments | arXiv:2605.28214v1 — § exact heading: 2.3 Threat Model | arXiv:2605.28214v1 — official HTML sha256=91ee9043fb86499854c2113111e547d97fe383fdeafe52160c01d2cf035e9872; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28214 | complete |
| SF-2026-ARXIV-2605-28224 | RP-5a1fe49d3d0a89ee | deep | arXiv:2605.28224v1 | SRC-ARXIV@arXiv:2605.28224v1 | arXiv:2605.28224v1 — § exact heading: 3 A Unified Memory Framework | arXiv:2605.28224v1 — § exact heading: 4 Experimental Setup | arXiv:2605.28224v1 — § exact heading: 6 Discussion | arXiv:2605.28224v1 — official HTML sha256=f73c2b99847ff63b93b3448413df8cbc3980da4f411624734fb2481eb52a14b3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28224 | complete |
| SF-2026-ARXIV-2605-28282 | RP-30f503e0fc304116 | deep | arXiv:2605.28282v1 | SRC-ARXIV@arXiv:2605.28282v1 | arXiv:2605.28282v1 — §3 ResearchLoop Protocol and Runtime; §4 Runtime Implementation | arXiv:2605.28282v1 — §7 controlled study and ablations | arXiv:2605.28282v1 — §7.2 synthetic task, single-model and sample-size limitations; Appendix C claim ledger | arXiv:2605.28282v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28282 | complete |
| SF-2026-ARXIV-2605-28302 | RP-e78b1e5187a252e9 | deep | arXiv:2605.28302v1 | SRC-ARXIV@arXiv:2605.28302v1 | arXiv:2605.28302v1 — § exact heading: 2.1 Design-Space Exploration for Optimal Disaggregated Inference | arXiv:2605.28302v1 — § exact heading: 4 Evaluation | arXiv:2605.28302v1 — § exact heading: 5 Discussion and Conclusion | arXiv:2605.28302v1 — official HTML sha256=d5bcb04b9f513ea26df32ea551e09fe23f72ba5651979e05cd229e9f171c23cf; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28302 | complete |
| SF-2026-ARXIV-2605-28354 | RP-930b485331af2ec2 | deep | arXiv:2605.28354v1 | SRC-ARXIV@arXiv:2605.28354v1 | arXiv:2605.28354v1 — § exact heading: 3 Methodology | arXiv:2605.28354v1 — § exact heading: 4 Experiments | arXiv:2605.28354v1 — § exact heading: 5 Conclusion | arXiv:2605.28354v1 — official HTML sha256=adefd62b5877ddd6b889b2d5466bf6d86dea3f49ca521809b6edc772b94d5cd9; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28354 | complete |
| SF-2026-ARXIV-2605-28371 | RP-70c47f15b611d7a5 | deep | arXiv:2605.28371v1 | SRC-ARXIV@arXiv:2605.28371v1 | arXiv:2605.28371v1 — § exact heading: 3 Method | arXiv:2605.28371v1 — § exact heading: 4 Experiments | arXiv:2605.28371v1 — § exact heading: 5 Conclusion | arXiv:2605.28371v1 — official HTML sha256=59b8cf453e48c85d21d2f09b6119c474e58ef81f53f90f1a81cd0252e3e6a66d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28371 | complete |
| SF-2026-ARXIV-2605-28384 | RP-9206fbc6ee3a4b36 | deep | arXiv:2605.28384v1 | SRC-ARXIV@arXiv:2605.28384v1 | arXiv:2605.28384v1 — § exact heading: 2.4 State Space Models and the Case for an SSM Expert | arXiv:2605.28384v1 — § exact heading: 5.3 Bayesian vs. Prior-Free Ablation: Tiny LM Benchmark | arXiv:2605.28384v1 — § exact heading: 7 Discussion | arXiv:2605.28384v1 — official HTML sha256=1570cc4c065bb54d719c2ab73ec29c27fc79dd28dbc83353e870b38450392418; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28384 | complete |
| SF-2026-ARXIV-2605-28390 | RP-5947de7acb772cd9 | deep | arXiv:2605.28390v1 | SRC-ARXIV@arXiv:2605.28390v1 | arXiv:2605.28390v1 — § exact heading: 2.1 Agentic Systems | arXiv:2605.28390v1 — § exact heading: 3.3 Skill Evaluation and Maintenance | arXiv:2605.28390v1 — § exact heading: 6 Conclusion | arXiv:2605.28390v1 — official HTML sha256=319497612764ee707963a369e412c779142c648f077829de02a9af1827bce409; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28390 | complete |
| SF-2026-ARXIV-2605-28424 | RP-5fbe1c6823665379 | deep | arXiv:2605.28424v1 | SRC-ARXIV@arXiv:2605.28424v1 | arXiv:2605.28424v1 — § exact heading: 3 Method | arXiv:2605.28424v1 — § exact heading: 4 Experiments | arXiv:2605.28424v1 — § exact heading: 5 Conclusion | arXiv:2605.28424v1 — official HTML sha256=56b115a0cea14050550666972c8c3358a23dadd06e5ca9e392e0893d2e08a307; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28424 | complete |
| SF-2026-ARXIV-2605-28433 | RP-2a57f879210baa43 | deep | arXiv:2605.28433v1 | SRC-ARXIV@arXiv:2605.28433v1 | arXiv:2605.28433v1 — § exact heading: 3 Methodology: Sero | arXiv:2605.28433v1 — § exact heading: 4 Experiments | arXiv:2605.28433v1 — § exact heading: 5 Conclusion | arXiv:2605.28433v1 — official HTML sha256=e6b9fa986647a1fdfaf40f75332819e7664fd3c3068b1e2919f51ea7317a4f5f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28433 | complete |
| SF-2026-ARXIV-2605-28467 | RP-ebe304ac46535ff7 | deep | arXiv:2605.28467v1 | SRC-ARXIV@arXiv:2605.28467v1 | arXiv:2605.28467v1 — § exact heading: 3 Methodology | arXiv:2605.28467v1 — § exact heading: 4.1 Benchmarks | arXiv:2605.28467v1 — § exact heading: 7 Discussion | arXiv:2605.28467v1 — official HTML sha256=8bc115de594103d60edec321cb4440daecf363960c1cb513ddb91f26c2fa43de; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28467 | complete |
| SF-2026-ARXIV-2605-28480 | RP-8fefdfc3612034a2 | deep | arXiv:2605.28480v1 | SRC-ARXIV@arXiv:2605.28480v1 | arXiv:2605.28480v1 — § exact heading: 2.1 Large Audio-Language Models and Audio Understanding Benchmarks | arXiv:2605.28480v1 — § exact heading: 5 Results | arXiv:2605.28480v1 — § exact heading: 6 Conclusion | arXiv:2605.28480v1 — official HTML sha256=d213543a1628789189242389ff40e33dc0b8dc1e48532230aa0d590500274040; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28480 | complete |
| SF-2026-ARXIV-2605-28508 | RP-2ba662f2d64d487e | deep | arXiv:2605.28508v1 | SRC-ARXIV@arXiv:2605.28508v1 | arXiv:2605.28508v1 — pp. 6–8 §3 System under test and layered evaluation | arXiv:2605.28508v1 — pp. 8–11 §4 application profiles and operating-condition tests | arXiv:2605.28508v1 — pp. 11–13 §5 minimum benchmark standard and reporting limits | arXiv:2605.28508v1 — official PDF sha256=8beef4051c11d29813c7f2801e1cf88087f06e659f52cb810f1d20df4999a24d; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28508 | complete |
| SF-2026-ARXIV-2605-28510 | RP-dad443da7ea54e4e | deep | arXiv:2605.28510v1 | SRC-ARXIV@arXiv:2605.28510v1 | arXiv:2605.28510v1 — §III Methodology: SourceTracker, Winnowing and HybridSourceTracker | arXiv:2605.28510v1 — §IV Results: recall, rank and latency | arXiv:2605.28510v1 — §V errors; §VI Discussion; §VIII-A future-work boundaries | arXiv:2605.28510v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28510 | complete |
| SF-2026-ARXIV-2605-28544 | RP-3ff9bf6981828268 | deep | arXiv:2605.28544v1 | SRC-ARXIV@arXiv:2605.28544v1 | arXiv:2605.28544v1 — §3 Method: autoregressive world-action flow, causal guidance and selective KV memory | arXiv:2605.28544v1 — §4 Experiments and ablations | arXiv:2605.28544v1 — §5 Conclusion; Appendix C efficiency analysis; no dedicated limitations section | arXiv:2605.28544v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28544 | complete |
| SF-2026-ARXIV-2605-28561 | RP-3c6ae6f24a42f8ab | deep | arXiv:2605.28561v1 | SRC-ARXIV@arXiv:2605.28561v1 | arXiv:2605.28561v1 — § exact heading: 1 Introduction | arXiv:2605.28561v1 — § exact heading: 5 Experiment Setup | arXiv:2605.28561v1 — § exact heading: 8 Conclusion | arXiv:2605.28561v1 — official HTML sha256=37a019db49266025a9f512e89d9d0055db4d54c74d0e179610cf4b5525ed3956; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28561 | complete |
| SF-2026-ARXIV-2605-28565 | RP-1db8d1876c788d99 | deep | arXiv:2605.28565v1 | SRC-ARXIV@arXiv:2605.28565v1 | arXiv:2605.28565v1 — §2 CiteTrace construction; §3 three-dimensional citation evaluation | arXiv:2605.28565v1 — §4 structural citation failures and judge validation | arXiv:2605.28565v1 — Appendix A.1 scope assumptions and A.2 limitations | arXiv:2605.28565v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28565 | complete |
| SF-2026-ARXIV-2605-28573 | RP-cd18fe97313da239 | deep | arXiv:2605.28573v1 | SRC-ARXIV@arXiv:2605.28573v1 | arXiv:2605.28573v1 — § exact heading: 3 The TSVD Method | arXiv:2605.28573v1 — § exact heading: 4.3 Experimental Derivation of Adaptive Rank Selection Heuristic | arXiv:2605.28573v1 — § exact heading: 6 Discussion and Future Work | arXiv:2605.28573v1 — official HTML sha256=74ef57819f581ccb20cd92e1585f01f2b930e2513a90ce9043b00e552d767079; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28573 | complete |
| SF-2026-ARXIV-2605-28617 | RP-78c9109419ffbf15 | deep | arXiv:2605.28617v1 | SRC-ARXIV@arXiv:2605.28617v1 | arXiv:2605.28617v1 — §3 typed holes and nested calls; §4 static/capability safety | arXiv:2605.28617v1 — §7 verifier, tool-use and multi-turn evaluation | arXiv:2605.28617v1 — §Limitations: well-typed is not correct; authority is only as tight as granted scope | arXiv:2605.28617v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28617 | complete |
| SF-2026-ARXIV-2605-28632 | RP-86f44e9b6fe76237 | deep | arXiv:2605.28632v1 | SRC-ARXIV@arXiv:2605.28632v1 | arXiv:2605.28632v1 — § exact heading: 2.3 PRNG Security in ML Systems | arXiv:2605.28632v1 — § exact heading: 5 Evaluation | arXiv:2605.28632v1 — § exact heading: 3 Threat Model and Problem Formulation | arXiv:2605.28632v1 — official HTML sha256=aafde923a8bedf299b01a1b87790b4fc26d09b9c734ec1891536e0ffbba5474c; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28632 | complete |
| SF-2026-ARXIV-2605-28634 | RP-934e6d4162e05aba | deep | arXiv:2605.28634v1 | SRC-ARXIV@arXiv:2605.28634v1 | arXiv:2605.28634v1 — § exact heading: 2.1 Vision-Language-Action Models | arXiv:2605.28634v1 — § exact heading: 5 Experiments | arXiv:2605.28634v1 — § exact heading: 6 Conclusion | arXiv:2605.28634v1 — official HTML sha256=28d4c6c0aa204e61c3cfe7c1bd438f923cee3007f437aec33e041b2342f66af3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28634 | complete |
| SF-2026-ARXIV-2605-28640 | RP-4f41053e965ca81c | deep | arXiv:2605.28640v1 | SRC-ARXIV@arXiv:2605.28640v1 | arXiv:2605.28640v1 — §2 exponentially decaying memory and sparse inference instantiations | arXiv:2605.28640v1 — §3 experiments and H1/H2 analyses | arXiv:2605.28640v1 — §Limitations: two 7B checkpoints, 4K context and RULER-only task family | arXiv:2605.28640v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28640 | complete |
| SF-2026-ARXIV-2605-28646 | RP-25a25d22c868e07e | deep | arXiv:2605.28646v1 | SRC-ARXIV@arXiv:2605.28646v1 | arXiv:2605.28646v1 — §4 edge evidence extraction, policy arbitration, SafeScreenshot and skill evolution | arXiv:2605.28646v1 — §5–6 evaluation, sandbox checks and error analysis | arXiv:2605.28646v1 — §Limitations: sanitized scenarios, trusted edge and short-horizon personalization | arXiv:2605.28646v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28646 | complete |
| SF-2026-ARXIV-2605-28678 | RP-0edf953b047cf958 | deep | arXiv:2605.28678v1 | SRC-ARXIV@arXiv:2605.28678v1 | arXiv:2605.28678v1 — § exact heading: 3 Method | arXiv:2605.28678v1 — § exact heading: 4 Experiments | arXiv:2605.28678v1 — § exact heading: 5 Conclusion | arXiv:2605.28678v1 — official HTML sha256=1a1a8f4e1c8ac3653a31c04eee5001b8bd690ec4cacab7bfa00bc96c7270d947; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28678 | complete |
| SF-2026-ARXIV-2605-28691 | RP-1a37691474429bb4 | deep | arXiv:2605.28691v1 | SRC-ARXIV@arXiv:2605.28691v1 | arXiv:2605.28691v1 — § exact heading: 2.1 Sparse Video Generation Model | arXiv:2605.28691v1 — § exact heading: 4 Experiment | arXiv:2605.28691v1 — § exact heading: 5 Conclusion | arXiv:2605.28691v1 — official HTML sha256=327ba473a5ca5523ab42d5daa2cd3b7c42aeeee6b6ecb6ae168b5896299fc13a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28691 | complete |
| SF-2026-ARXIV-2605-28699 | RP-650b15977d613eba | deep | arXiv:2605.28699v1 | SRC-ARXIV@arXiv:2605.28699v1 | arXiv:2605.28699v1 — § exact heading: 2.2 Multi-Agent System | arXiv:2605.28699v1 — § exact heading: 5 Experiments | arXiv:2605.28699v1 — § exact heading: 6 Conclusion and Limitations | arXiv:2605.28699v1 — official HTML sha256=b46ff12911d0d68e6d23a196c51d66c97243f6cce1cd9ee2d7c2e6a1acc91235; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28699 | complete |
| SF-2026-ARXIV-2605-28704 | RP-095658c28e435cf8 | deep | arXiv:2605.28704v1 | SRC-ARXIV@arXiv:2605.28704v1 | arXiv:2605.28704v1 — § exact heading: I Introduction | arXiv:2605.28704v1 — § exact heading: III Main Results | arXiv:2605.28704v1 — § exact heading: I-A Contribution | arXiv:2605.28704v1 — official HTML sha256=4a7a9a3977cbb61bc5708038d0f880bde52cc4bfcdd5fb033aee756b8612194f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28704 | complete |
| SF-2026-ARXIV-2605-28721 | RP-7a1b719dd976803a | deep | arXiv:2605.28721v1 | SRC-ARXIV@arXiv:2605.28721v1 | arXiv:2605.28721v1 — § exact heading: 2.4 From Diagnosis to Benchmark Design | arXiv:2605.28721v1 — § exact heading: 2.3 Search Strategy Analysis | arXiv:2605.28721v1 — § exact heading: 6 Discussion and Conclusion | arXiv:2605.28721v1 — official HTML sha256=aeaa68114c24fa582046ca5879e68e549f4c733433734b424d86c75f38e35acf; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28721 | complete |
| SF-2026-ARXIV-2605-28726 | RP-1ffccc712dacecc2 | deep | arXiv:2605.28726v1 | SRC-ARXIV@arXiv:2605.28726v1 | arXiv:2605.28726v1 — § exact heading: II Method | arXiv:2605.28726v1 — § exact heading: IV Experiments | arXiv:2605.28726v1 — § exact heading: IV-C Failure Prediction: Which Monitors Work? | arXiv:2605.28726v1 — official HTML sha256=90cd7e1a54362609991628c3db8b3b43348ca9e11c25067c1e202fb5bc05f38f; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28726 | complete |
| SF-2026-ARXIV-2605-28732 | RP-c804e06e9d82dcab | deep | arXiv:2605.28732v1 | SRC-ARXIV@arXiv:2605.28732v1 | arXiv:2605.28732v1 — § exact heading: 2 Tracing and Attributing Errors in Memory Systems | arXiv:2605.28732v1 — § exact heading: 5 Experiments | arXiv:2605.28732v1 — § exact heading: 8 Conclusion | arXiv:2605.28732v1 — official HTML sha256=c81383e0d1ae7799a14d2a9bd4911c986acf573281a52a6c6c13834fbea2f6a3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28732 | complete |
| SF-2026-ARXIV-2605-28742 | RP-e1c06ac7fa38e31c | deep | arXiv:2605.28742v1 | SRC-ARXIV@arXiv:2605.28742v1 | arXiv:2605.28742v1 — § exact heading: 1 Introduction | arXiv:2605.28742v1 — § exact heading: 4 Evaluation | arXiv:2605.28742v1 — § exact heading: 6 Discussion | arXiv:2605.28742v1 — official HTML sha256=948395dbaa3e07d1b9fdd398c0c4b798d06dc1a875a55c6c2950cc6ff67acefa; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28742 | complete |
| SF-2026-ARXIV-2605-28751 | RP-d0a01043295bf94d | deep | arXiv:2605.28751v1 | SRC-ARXIV@arXiv:2605.28751v1 | arXiv:2605.28751v1 — § exact heading: 3.4 Extrapolative weight averaging generalizes across inference settings and model scales | arXiv:2605.28751v1 — § exact heading: 4 Analysis and Perspectives | arXiv:2605.28751v1 — § exact heading: 6 Discussion and Limitations | arXiv:2605.28751v1 — official HTML sha256=2ad8c69c8a772c3094e9868186053eb7541cc9e186faa3e4caa9f18359f26f0a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28751 | complete |
| SF-2026-ARXIV-2605-28760 | RP-214086e596c58ac9 | deep | arXiv:2605.28760v1 | SRC-ARXIV@arXiv:2605.28760v1 | arXiv:2605.28760v1 — § exact heading: 3 System Design | arXiv:2605.28760v1 — § exact heading: 4 Evaluation Setup | arXiv:2605.28760v1 — § exact heading: 7 Discussion | arXiv:2605.28760v1 — official HTML sha256=efb091acec460dba1a6d525cc918d4b70a6c230b181d97523eae8b763dbc309b; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28760 | complete |
| SF-2026-ARXIV-2605-28764 | RP-c836cbe2d01e8938 | deep | arXiv:2605.28764v1 | SRC-ARXIV@arXiv:2605.28764v1 | arXiv:2605.28764v1 — §3 SwarmNode, registry, router and credit ledger; §4 attribution | arXiv:2605.28764v1 — §5 feasibility and deployment path | arXiv:2605.28764v1 — §5.3–5.5 bootstrap, security/privacy and open challenges | arXiv:2605.28764v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28764 | complete |
| SF-2026-ARXIV-2605-28773 | RP-7b84ae320909f89f | deep | arXiv:2605.28773v1 | SRC-ARXIV@arXiv:2605.28773v1 | arXiv:2605.28773v1 — § exact heading: 2 FluxMem Memory Architecture | arXiv:2605.28773v1 — § exact heading: 4 Experiments | arXiv:2605.28773v1 — § exact heading: 6 Conclusion | arXiv:2605.28773v1 — official HTML sha256=d18935b37ea808d2c0daeb4cc59dd49ecae728926ce886f1b3840a91e9819065; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28773 | complete |
| SF-2026-ARXIV-2605-28774 | RP-aa51cf6a59662673 | deep | arXiv:2605.28774v1 | SRC-ARXIV@arXiv:2605.28774v1 | arXiv:2605.28774v1 — § exact heading: A.2 System Prompt and Tool Interface | arXiv:2605.28774v1 — § exact heading: 2 Analysis of RL in Agentic Reasoning | arXiv:2605.28774v1 — § exact heading: 6 Conclusion | arXiv:2605.28774v1 — official HTML sha256=d13ded6dc9cb9f022fcba82d2f405dbb31ca326a1d1cbc8f2311772a26d1d576; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28774 | complete |
| SF-2026-ARXIV-2605-28778 | RP-e4b2161c11fb868d | deep | arXiv:2605.28778v1 | SRC-ARXIV@arXiv:2605.28778v1 | arXiv:2605.28778v1 — § exact heading: 5.3 Impact of System Prompt | arXiv:2605.28778v1 — § exact heading: 4 Experimental Setup | arXiv:2605.28778v1 — § exact heading: 6 Conclusion | arXiv:2605.28778v1 — official HTML sha256=01b64c870e884d24bc10330a3d3515358d4337041ab0b0076cad2275dc758860; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28778 | complete |
| SF-2026-ARXIV-2605-28787 | RP-47e7c882e59f9608 | deep | arXiv:2605.28787v1 | SRC-ARXIV@arXiv:2605.28787v1 | arXiv:2605.28787v1 — § exact heading: 3 System Architecture & Experimental Setup | arXiv:2605.28787v1 — § exact heading: 4 Evaluation Methodology | arXiv:2605.28787v1 — § exact heading: 6 Discussion and Future Work | arXiv:2605.28787v1 — official HTML sha256=4c1f63382d975afe45c1ff2cb12bd17b1fd33893d7aadc0f6e6d17130428b66a; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28787 | complete |
| SF-2026-ARXIV-2605-28803 | RP-cabd2f9c8fd2d577 | deep | arXiv:2605.28803v1 | SRC-ARXIV@arXiv:2605.28803v1 | arXiv:2605.28803v1 — § exact heading: 3.1 Vision Language Action (VLA) Model | arXiv:2605.28803v1 — § exact heading: 5 Experiments and Results | arXiv:2605.28803v1 — § exact heading: 6 Discussion and Analysis | arXiv:2605.28803v1 — official HTML sha256=9cf86ee52580269d695f1b428859a43d79cc4d552873686384aa093796ecedb6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28803 | complete |
| SF-2026-ARXIV-2605-28805 | RP-730d66eb29e576ce | deep | arXiv:2605.28805v1 | SRC-ARXIV@arXiv:2605.28805v1 | arXiv:2605.28805v1 — § exact heading: 1 Introduction | arXiv:2605.28805v1 — § exact heading: Appendix B Additional Experiments | arXiv:2605.28805v1 — § exact heading: 7 Conclusion | arXiv:2605.28805v1 — official HTML sha256=3c391c76b440fdc62c981dbf8764efd8db77092b07a8c527ed7c2f06c9d088c6; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28805 | complete |
| SF-2026-ARXIV-2605-28807 | RP-e88a335dd8719f0f | deep | arXiv:2605.28807v1 | SRC-ARXIV@arXiv:2605.28807v1 | arXiv:2605.28807v1 — § exact heading: 1 Introduction | arXiv:2605.28807v1 — § exact heading: 5 Experiments | arXiv:2605.28807v1 — § exact heading: 6 Conclusion | arXiv:2605.28807v1 — official HTML sha256=fc1cea1dc0e5de404483eaaf47079402901d8349b2ea8d5133060ab680d51c22; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28807 | complete |
| SF-2026-ARXIV-2605-28819 | RP-dbb44e642cc8196c | deep | arXiv:2605.28819v1 | SRC-ARXIV@arXiv:2605.28819v1 | arXiv:2605.28819v1 — § exact heading: 1 Introduction | arXiv:2605.28819v1 — § exact heading: 2 The PEFT-Arena Benchmark | arXiv:2605.28819v1 — § exact heading: Limitations | arXiv:2605.28819v1 — official HTML sha256=8e6e8e4418944fbd589b91d7ddf5befba422f816d98e2de9b6ebcc57deeed7e3; immutable repository/checkpoint commit Not Disclosed unless named in v1 | claim:SF-2026-ARXIV-2605-28819 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-27390:start -->
#### EvoSpec: Evolving Speculative Decoding via Real-Time Vocabulary and Parameter Adaptation

<!-- claim:SF-2026-ARXIV-2605-27390:start -->
- **Problem:** Speculative decoding accelerates Large Language Model inference through draft-then-verify generation, yet lightweight draft models face coupled efficiency and quality limitations: large-vocabulary output projection is costly, while limited draft capacity and static parameters reduce acceptance under specialized or shifting inputs.
- **Old path / changed constraint:** Speculative decoding accelerates Large Language Model inference through draft-then-verify generation, yet lightweight draft models face coupled efficiency and quality limitations: large-vocabulary output projection is costly, while limited draft capacity and static parameters reduce acceptance under specialized or shifting inputs.
- **Mechanism / ownership:** We introduce EvoSpec, which jointly adapts the active vocabulary and lightweight draft parameters from verification feedback.
- **Evaluation contract:** Extensive evaluations across specialized domains (coding, law, and medicine) confirm that EvoSpec overcomes the limitations of static baselines.
- **Proof / non-proof:** Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above.
- **Trade-off / failure mode:** While existing static pruning methods effectively reduce this overhead, they suffer from precipitous drops in acceptance rate in specialized domains or topic-switching scenarios due to their inability to capture dynamic distribution shifts.
- **Coexistence boundary:** The older path remains appropriate where its workload and SLO do not trigger the changed constraint; the paper is treated as a conditional branch, not a universal replacement.
- **Primary:** [arXiv:2605.27390v1](https://arxiv.org/abs/2605.27390v1)；frozen exact-v1 `papers/2026/05/_sources/arxiv-owner-replay-20260903/exact-v1/2605.27390v1.html.html`。
- **Disposition:** `No Change — Existing Coverage`；Fresh-context owner/adjacent comparison completed; the current Books proposition already owns the durable mechanism, so no duplicate paragraph was added.
<!-- claim:SF-2026-ARXIV-2605-27390:end -->
<!-- review:SF-2026-ARXIV-2605-27390:end -->

<!-- review:SF-2026-ARXIV-2605-27428:start -->
#### $E^3$-Agent: An Executable and Evolving Agent for Resource Management of Edge Generative Inference

**问题与机制。** Edge deployments of generative inference increasingly face two practical realities: per-device per-model performance is often unknown at deployment time, and it is non-stationary due to user-driven semantic events, background load, and device churn. Edge deployments of generative inference increasingly face two practical realities: per-device per-model performance is often unknown at deployment time, and it is non-stationary due to user-driven semantic events, background load, and device churn. 系统 owner=`INFER-SCHEDULING`。

**Exact-v1。** Method=`§2 System Model and Problem Formulation; §3 E 3 -Agent Architecture; §3.2 Architecture Overview`；Evaluation=`§4 Experiments; §4.1 Experimental Setup; §4.2 Results`；Limitations/Counterevidence=`§5 Conclusion and Future Work`；正文 sha256=`72a16faf7fa85f729f828ff9fe77c359ec947a6af4bc5b0056cf58507fcd1e9d`。

<!-- claim:SF-2026-ARXIV-2605-27428:start -->证据只支持 exact-v1 披露的 workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator；未披露字段为 Not Disclosed，不能外推生产优势。<!-- claim:SF-2026-ARXIV-2605-27428:end -->

Books Decision=`No Change — Existing Coverage`；已逐章比较 current owner 与相邻章节。
<!-- review:SF-2026-ARXIV-2605-27428:end -->

<!-- review:SF-2026-ARXIV-2605-27432:start -->
#### FD-RAG: Federated Dual-System Retrieval-Augmented Generation

**问题与机制。** We propose FD-RAG, a federated dual-system RAG framework that decouples lightweight memory access from on-demand LLM reasoning for decentralized deployment. owner=`AGENT-RAG`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§4 federated dual-system retrieval and compact QA memory`；Evaluation=`§5 experiments`；Limitations/Counterevidence=`Appendix D privacy/cost analysis; no general privacy guarantee`。

<!-- claim:SF-2026-ARXIV-2605-27432:start -->FD-RAG: Federated Dual-System Retrieval-Augmented Generation only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-27432:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-27432:end -->

<!-- review:SF-2026-ARXIV-2605-27435:start -->
#### When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference

**问题与机制。** Deploying large language models (LLMs) on mobile devices increasingly relies on heterogeneous execution, yet no prior study has systematically characterized NPU effectiveness at the operator and pipeline level. owner=`INFER-TENSORRT-LLM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Stage-Level Mobile LLM Method`；Evaluation=`§4 CPU/GPU/NPU Evaluation`；Limitations/Counterevidence=`§5 Discussion and device/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-27435:start -->When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-27435:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-27435:end -->

<!-- review:SF-2026-ARXIV-2605-27437:start -->
#### MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents

**问题与机制。** Although recent methods introduce reflection into retrieval, their retrieval paths are generated by the LLM from limited evidence, leading to unstable retrieval and additional latency overhead. owner=`AGENT-MEMORY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 memory-guided reflective retrieval`；Evaluation=`§4 long-dialogue experiments`；Limitations/Counterevidence=`§5 Discussion; tested-memory/task and extra-latency boundary`。

<!-- claim:SF-2026-ARXIV-2605-27437:start -->MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-27437:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-27437:end -->

<!-- review:SF-2026-ARXIV-2605-27461:start -->
#### A Factory-Floor Deployment Case Study of VLA Pipelines for Industrial Packaging Task: Workflow, Failures, and Lessons

**问题与机制。** We present a deployment study of an industrial packaging task at Siemens Factory (GWE, Erlangen, Germany), where a robot must pick a transparent accessory bag from a cluttered pile, insert it into the remaining cavity of a cardboard package, and ensure that the bag and its contents remain below the closing plane. 该证据的系统 owner 定位为 `MULTIMODAL-EMBODIED-VLA`。

**Exact-v1 路径。** Method=`§II hardware/software; §III execution; §IV data collection and training loop`；Evaluation=`§V results and §VI deployment failures/lessons`；Limitations/Counterevidence=`§VII Conclusion; one factory task, 2,535 episodes and no cross-site generality`。

<!-- claim:SF-2026-ARXIV-2605-27461:start -->只支持 exact-v1 明确披露的 workload、model、hardware、precision、length、batch、concurrency、SLO 与 evaluator；任何未披露字段均为 Not Disclosed，不将作者实验外推为通用生产优势。<!-- claim:SF-2026-ARXIV-2605-27461:end -->

Books Decision=`No Change — Existing Coverage`；这是非作者基于 current owner+adjacent 的 pre-write decision；report-level writeback 与独立 post-write Semantic Audit 已通过，Books Gate 已闭合。
<!-- review:SF-2026-ARXIV-2605-27461:end -->

<!-- review:SF-2026-ARXIV-2605-27466:start -->
#### AgensFlow: A Coordination-Policy Substrate for Multi-Agent Systems

问题与 changed constraint：multi-agent coordination is represented as an auditable policy graph over skills, models and topology with reward robustness as a first-class control-plane concern。

机制与 ownership：This paper introduces AgensFlow, an open-source framework that treats multi-agent coordination as an online policy-learning problem under partial observability. owner=`AGENT-MULTI-AGENT`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27466v1 — § exact heading: 2.1 Reasoning and Agent Design Patterns — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27466v1 — § exact heading: 2.5 Relative Trajectory Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27466v1 — § exact heading: 7 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27466:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27466:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27466:end -->

<!-- review:SF-2026-ARXIV-2605-27480:start -->
#### BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving

问题与 changed constraint：serving externality accounting needs a functional unit and quality-aware biodiversity impact identity, because carbon and water metrics do not proxy every lifecycle impact。

机制与 ownership：We present BIRDS, a framework for Biodiversity Impact of Request-Driven LLM Serving. owner=`PLATFORM-COST`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27480v1 — § exact heading: 3 The BIRDS Framework — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27480v1 — § exact heading: 4 Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27480v1 — § exact heading: Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27480:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27480:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27480:end -->

<!-- review:SF-2026-ARXIV-2605-27483:start -->
#### Debate Helps Weak Judges Reward Stronger Models

问题与 changed constraint：debate is an evaluation treatment that can reduce weak-judge over-endorsement only when the critic supplies usable evidence; judge family and prompt remain part of identity。

机制与 ownership：Despite theoretical promise, debate as a scalable oversight protocol has produced mixed empirical results: gains in some settings, and null effects in others, especially when the judge does not have information hidden from it. We study proposer-critic debate in a stronger-debater/weaker-judge setting on programmatically verifiable code and logic tasks. Debate helps the judge over a consultancy baseline when the critic provides a usable advantage: the critic's classification ability must exceed t owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27483v1 — § exact heading: 3 Methods — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27483v1 — § exact heading: 3.5 Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27483v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27483:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27483:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27483:end -->

<!-- review:SF-2026-ARXIV-2605-27488:start -->
#### Grimlock: Guarding High-Agency Systems with eBPF and Attested Channels

问题与 changed constraint：agent trust enforcement moves below application code into eBPF-mediated, channel-attested communication.。

机制与 ownership：We present Grimlock, an Agent Guard that restores separation of concerns by moving trust enforcement into the sandbox substrate while leaving agent code unchanged. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27488v1 — §3 threat model; §4 eBPF interception and TLS channel-binding attestation; §5 delegation`；Evaluation=`arXiv:2605.27488v1 — §6 prototype evaluation and attack checks`。

Trade-off / failure：`arXiv:2605.27488v1 — §7 limitations — Linux/eBPF, visible network channels, trusted guard/attestation and prototype workload boundary`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27488:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27488:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27488:end -->

<!-- review:SF-2026-ARXIV-2605-27489:start -->
#### HARP: Measuring Harm Amplification in Multi-Agent LLM Systems

问题与 changed constraint：multi-agent safety evaluation must measure interaction-driven harm amplification rather than extrapolate isolated-agent scores。

机制与 ownership：This modularity improves interpretability, but creates a propagation risk: a bounded perturbation to one component can be reused by other agents and amplified into system-level harm. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27489v1 — § exact heading: 3 Methodology — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27489v1 — § exact heading: 4 Results — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27489v1 — § exact heading: 4.3 Aggregate Comparison Across Vulnerability Types — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27489:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27489:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27489:end -->

<!-- review:SF-2026-ARXIV-2605-27491:start -->
#### GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation

问题与 changed constraint：a closed-loop world simulator binds action-conditioned video, proprioceptive state, world-judge reward and downstream policy consistency instead of video quality alone。

机制与 ownership：We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation. owner=`MULTIMODAL-WORLD-MODELS`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27491v1 — § exact heading: GE-Base: Multi-View Video World Foundation Model — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27491v1 — § exact heading: Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27491v1 — § exact heading: Instructions for reporting errors — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27491:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27491:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27491:end -->

<!-- review:SF-2026-ARXIV-2605-27492:start -->
#### Benchmarks are Not Enough: RAMP for Runtime Assessing of Agentic Models in Production Systems

问题与 changed constraint：production agent assessment preserves runtime state and uses resurrection artifacts to separate upstream cascade from downstream capability.。

机制与 ownership：We thus present RAMP, a production-grounded infrastructure for assessing long-horizon software engineering agents. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27492v1 — §3 runtime assessment architecture, serial evolution/resurrection workloads and metrics`；Evaluation=`arXiv:2605.27492v1 — §4 production-grounded agent results`。

Trade-off / failure：`arXiv:2605.27492v1 — §6 Limitations — bounded software-engineering agents/platform and runtime artifacts; paper template metadata is anomalous`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27492:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27492:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27492:end -->

<!-- review:SF-2026-ARXIV-2605-27494:start -->
#### Grounded Cache Routing for Retrieval-Augmented Generation: When Is It Safe to Reuse an Answer?

问题与 changed constraint：answer-cache reuse is committed only against fresh evidence identity, version and support, with regeneration as fallback.。

机制与 ownership：We propose GroundedCache, an evidence-validated cache router that admits a cached answer only when 4 cheap gates simultaneously hold: query similarity, retrieved-evidence overlap, source-version validity, and lexical (or judge-based) support of the cached answer by the freshly retrieved evidence. owner=`AGENT-RAG`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27494v1 — §3.1–3.4 pipeline, evidence signature, four validation gates and compression fallback`；Evaluation=`arXiv:2605.27494v1 — §4 setup/metrics; §5 HotpotQA and mtRAG results/ablations`。

Trade-off / failure：`arXiv:2605.27494v1 — §7 Limitations — two datasets, Qwen2.5-7B/vLLM, lexical/judge support and small per-regime samples`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27494:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27494:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27494:end -->

<!-- review:SF-2026-ARXIV-2605-27547:start -->
#### From Task Allocation to Risk Clearing: A Unifying Interface for Mixed Human-Agent Societies

问题与 changed constraint：mixed human-agent allocation exposes capability and risk as bounded options that a clearing authority accepts rather than allowing agents to self-assign consequential work。

机制与 ownership：To overcome these limitations, we propose Risk-Aware Option Clearing (ROC), a unifying coordination mechanism in which agents expose options (temporally extended skills) paired with risk summaries that predict outcome distributions. owner=`AGENT-MULTI-AGENT`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27547v1 — § exact heading: 1 Introduction — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27547v1 — § exact heading: 2 Risk-Aware Option Clearing (ROC) — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27547v1 — § exact heading: 4 Discussion and Outlook — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27547:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27547:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27547:end -->

<!-- review:SF-2026-ARXIV-2605-27559:start -->
#### Detection Without Correction: A Two-Parameter Decomposition of Multi-Stage LLM Pipelines

问题与 changed constraint：multi-stage correction separates failure detection from conditional miscorrection, preventing a successful detector from being mistaken for an effective repair loop。

机制与 ownership：The framework unifies the four phenomena above as signatures of a common mechanism and characterizes detection threshold as a stable model/protocol-level regularity that persists across methods at matched benchmark difficulty. owner=`AGENT-REFLECTION`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27559v1 — § exact heading: 3.1 Models and Benchmarks — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27559v1 — § exact heading: 3 Experimental Setup — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27559v1 — § exact heading: 5 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27559:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27559:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27559:end -->

<!-- review:SF-2026-ARXIV-2605-27566:start -->
#### DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents

问题与 changed constraint：dynamic-scheduling benchmarks must calibrate static baselines and distinguish controller quality from the observability and workload contract exposed to an LLM agent。

机制与 ownership：To resolve this, we introduce \textbf{DynaSchedBench}, a diagnostic framework for DFJSP that rigorously controls the instance-generation process. owner=`PLATFORM-GPU-SCHEDULER`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27566v1 — §3 Benchmark Design; §4 Scheduling Agents (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27566v1 — §5 Workloads and calibrated-baseline results (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27566v1 — §6 Observability paradox and limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27566:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27566:end -->

Books Decision=`Weekly Only — Context`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27566:end -->

<!-- review:SF-2026-ARXIV-2605-27569:start -->
#### RULER: Representation-Level Verification of Machine Unlearning

问题与 changed constraint：machine-unlearning evidence must inspect residual representation state in addition to output behavior and membership attacks。

机制与 ownership：We introduce RULER, a set of representation-level verification metrics. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27569v1 — § exact heading: 4.1 Datasets and model architecture — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27569v1 — § exact heading: 3 Representation-Level Evaluation — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27569v1 — § exact heading: 6 Discussion and Conclusion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27569:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27569:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27569:end -->

<!-- review:SF-2026-ARXIV-2605-27575:start -->
#### Agyn: An Open-Source Platform for AI Agents with Scalable On-Demand Execution, Agent Definition as a Code, and Zero-Trust Access

问题与 changed constraint：agent definition as code, on-demand execution and zero-trust access turn identity, deployment and authorization into platform-managed lifecycle objects。

机制与 ownership：In this paper we present Agyn, an open-source platform designed around three key principles tailored for agent workloads: a signal-driven, stateful serverless runtime on Kubernetes; a Terraform provider for agent and harness definition; and a security model grounded in zero-trust and least-privilege principles. owner=`AGENT-PLATFORM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27575v1 — §3 Platform Architecture; §4 Agent Definition as Code (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27575v1 — §5 Evaluation (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27575v1 — §6 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27575:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27575:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27575:end -->

<!-- review:SF-2026-ARXIV-2605-27589:start -->
#### What-If World: A Causal Benchmark for General World Models in Embodied Scenarios

问题与 changed constraint：world-model evaluation uses paired causal interventions and per-primitive outcomes so plausible video cannot substitute for controllable environment dynamics。

机制与 ownership：We introduce What-If World, 319 such prompt pairs built on real frames from nuScenes and DROID, organized by a taxonomy of six physical variables shared across driving and manipulation. owner=`MULTIMODAL-WORLD-MODELS`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27589v1 — § exact heading: 4.3 When World Model Fails: Per-Primitive Analysis — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27589v1 — § exact heading: 3 The What-If World Benchmark — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27589v1 — § exact heading: 4.2 Why Paired Evaluation Matters: The Hidden Failure Stratum — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27589:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27589:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27589:end -->

<!-- review:SF-2026-ARXIV-2605-27599:start -->
#### The Energy Blind Spot: NVIDIA's Flagship Edge AI Hardware Cannot Support Process-Level Energy Attribution

问题与 changed constraint：process-level energy attribution is impossible without an observable hardware counter and attribution boundary; utilization or board power are not equivalent evidence。

机制与 ownership：We formalize a hardware requirements specification for energy-attributed AI, propose an interim calibration bridge for per-domain energy decomposition - confirmed on the Acer Veriton GN100 where CPU energy accumulators are live - and identify a standards-track path via SCMI powercap. owner=`PLATFORM-MONITORING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27599v1 — §2 Hardware Audit Methodology, Table 1 and seven-interface audit on one GX10`；Evaluation=`arXiv:2605.27599v1 — §5 What the GB10 Does Expose: Rich Telemetry, No Energy, Table 2; §6 external-meter fallback feasibility and limits`。

Trade-off / failure：`arXiv:2605.27599v1 — §2 scope note; §3 unvalidated SPBM corroboration; §6 attribution uncertainty, coarse boundary and overhead`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27599:start -->仅支持论文审计的一台 GX10 与标准 Linux aarch64 接口：不外推为所有 ARM/edge hardware；外部计量是带不确定性和运维成本的粗粒度回退，不等价于进程级硬件能量计数。<!-- claim:SF-2026-ARXIV-2605-27599:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27599:end -->

<!-- review:SF-2026-ARXIV-2605-27621:start -->
#### Agents that Matter: Optimizing Multi-Agent LLMs via Removal-Based Attribution

问题与 changed constraint：agent contribution requires a declared removal intervention and coalition distribution before attribution can drive pruning, cost optimization or safety audit。

机制与 ownership：As multi-agent systems (MAS) become increasingly complex, identifying the contributions of individual agents is critical for system optimization. owner=`AGENT-MULTI-AGENT`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27621v1 — § exact heading: 3 A Unified Framework for Agent Attribution — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27621v1 — § exact heading: 4 Benchmarks and MAS Architectures — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27621v1 — § exact heading: Limitations and Future Work — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27621:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27621:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27621:end -->

<!-- review:SF-2026-ARXIV-2605-27630:start -->
#### OptiLoop: Coordination-in-the-Loop Verification and Repair for LLM-Generated Optimization Agents

问题与 changed constraint：coordination traces provide typed behavioral evidence for verification, diagnosis, repair and episodic reuse instead of unconstrained self-reflection。

机制与 ownership：We propose coordination-in-the-loop verification and repair for LLM-generated optimization agents. owner=`AGENT-REFLECTION`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27630v1 — § exact heading: 4 Methodology — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27630v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27630v1 — § exact heading: 6.4 Failure analysis — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27630:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27630:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27630:end -->

<!-- review:SF-2026-ARXIV-2605-27668:start -->
#### Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting

问题与 changed constraint：forecast calibration targets a distribution over human uncertainty and must be evaluated separately from answer accuracy or post-hoc temperature scaling。

机制与 ownership：To address this, we propose the Beta-Bernoulli Calibrator (BBC), which converts an initial point estimate forecast from any model into a distribution over event likelihood, using supervision from both binary outcomes and human forecasts. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27668v1 — § exact heading: 4.2 Model architecture and input — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27668v1 — § exact heading: 3.2 Evaluation metrics — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27668v1 — § exact heading: Appendix A Limitations — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27668:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27668:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27668:end -->

<!-- review:SF-2026-ARXIV-2605-27671:start -->
#### Evolving and Detecting Multi-Turn Deception using Geometric Signatures

问题与 changed constraint：multi-turn deception monitoring treats geometric trajectory signatures as a fallible longitudinal sensor rather than classifying isolated messages。

机制与 ownership：To defend against this more nuanced form of deception, we present a unified pipeline that generates realistic multi-turn deceptive question sets via multi-objective genetic prompt optimization with co-evolving mutation operators. owner=`PLATFORM-MONITORING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27671v1 — §3 Geometric signature and multi-turn evolution (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27671v1 — §4 Experiments (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27671v1 — §5 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27671:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27671:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27671:end -->

<!-- review:SF-2026-ARXIV-2605-27678:start -->
#### Heterogeneous Parallelism for Multimodal Large Language Model Training

问题与 changed constraint：multimodal modules receive independent parallel layouts while boundary communicators own forward activation and reverse-gradient transforms.。

机制与 ownership：We present heterogeneous parallelism for multimodal large language model training, an abstraction that lets modules in one end-to-end graph use independent layouts and rank placements, supporting colocated execution on shared GPUs and non-colocated execution on disjoint rank sets. owner=`TRAIN-DISTRIBUTED-TRAINING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27678v1 — §3.1–3.3 non-colocated/colocated communicators and heterogeneous pipeline orchestration`；Evaluation=`arXiv:2605.27678v1 — §4 operating-regime sweep; §5 step-level parity and convergence validation`。

Trade-off / failure：`arXiv:2605.27678v1 — Reasoned exception — manuscript has no dedicated Limitations section; §4 Operating regimes and §5 Convergence validation bind claims to tuned Megatron-LM multimodal workloads, disclosed GPU/layout search and convergence cases`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27678:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27678:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27678:end -->

<!-- review:SF-2026-ARXIV-2605-27681:start -->
#### Behavioural Analysis of Alignment Faking

问题与 changed constraint：alignment-faking evidence must bind hidden-versus-observed incentive conditions and compliance gaps rather than infer deception from a single compliant output。

机制与 ownership：We identify three separable drivers -- values, goal guarding, and sycophancy -- and show via targeted prompt ablations and activation steering that each independently modulates AF behaviour. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27681v1 — § exact heading: Appendix A System prompts — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27681v1 — § exact heading: 4 Experimental Results — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27681v1 — § exact heading: 5 Discussion and Conclusion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27681:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27681:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27681:end -->

<!-- review:SF-2026-ARXIV-2605-27690:start -->
#### TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-State Modeling

问题与 changed constraint：agent safety auditing becomes prefix-state prediction over evolving trajectories rather than post-hoc final-output classification.。

机制与 ownership：We propose TRACES, a representation-based proactive auditor that learns prefix-level trajectory risk states from the hidden representations of an observer LLM. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27690v1 — §3 TRACES trajectory-state model, weak supervision and prefix-risk scoring`；Evaluation=`arXiv:2605.27690v1 — §4 setup; §5 proactive-detection results and ablations`。

Trade-off / failure：`arXiv:2605.27690v1 — §6 Limitations — observer/model/task/attack coverage, weak labels and hidden-state access assumptions`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27690:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27690:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27690:end -->

<!-- review:SF-2026-ARXIV-2605-27710:start -->
#### DeepSciVerify: Verifying Scientific Claim--Citation Alignment via LLM-Driven Evidence Escalation

问题与 changed constraint：claim-citation verification escalates retrieval depth only when evidence remains insufficient and preserves claim, cited source and retrieved support as separate identities。

机制与 ownership：We present DeepSciVerify, a two-stage pipeline for scientific claim-citation verification that combines abstract-level reasoning with selective escalation to passage-level evidence. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27710v1 — §3 Evidence-escalation pipeline (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27710v1 — §4 Evaluation (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27710v1 — §6 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27710:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27710:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27710:end -->

<!-- review:SF-2026-ARXIV-2605-27712:start -->
#### Prefix-Safe Bayesian Belief Tracking for LLM Reasoning Reliability:Separating Calibration from Ranking

问题与 changed constraint：prefix-safe belief tracking separates probability calibration from candidate ranking and prevents future evidence from leaking into earlier confidence checkpoints。

机制与 ownership：Together, these findings support SBBT as a calibration-aware online inference framework and expose an evidence regime: scalar scores mainly support probability quality, while structure-aware prefix signals support ranking only when strong prefix-safe baselines have not already absorbed the rank evidence. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27712v1 — § exact heading: 4 Method — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27712v1 — § exact heading: 5 Experiments — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27712v1 — § exact heading: 6 Discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27712:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27712:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27712:end -->

<!-- review:SF-2026-ARXIV-2605-27720:start -->
#### Bayesian Deployment Approval for Learned Landing Controllers under Finite Rollout Validation

问题与 changed constraint：deployment approval is a posterior risk decision under finite rollouts, not an empirical success-rate threshold.。

机制与 ownership：This work develops a Bayesian approval framework for learned autonomous landing controllers under finite rollout evidence. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27720v1 — §3 probabilistic landing capability; §4 Bayesian posterior approval/risk rule`；Evaluation=`arXiv:2605.27720v1 — §5 finite-rollout simulation study and sensitivity`。

Trade-off / failure：`arXiv:2605.27720v1 — §6 Limitations — landing-controller/simulation prior/model assumptions; posterior approval is not field certification`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27720:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27720:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27720:end -->

<!-- review:SF-2026-ARXIV-2605-27744:start -->
#### A Policy-Driven Runtime Layer for Agentic LLM Serving

问题与 changed constraint：a typed agent runtime tier mediates framework semantics and engine events so cross-layer serving policies have one owner.。

机制与 ownership：The agent framework above knows agent identities, role, schemas, and dispatch structure but never sees an engine-level event; the serving engine below sees every event but knows nothing about agents. owner=`AGENT-PLATFORM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27744v1 — §3 runtime-layer interface and policy hooks; §4 lifecycle/control-plane design`；Evaluation=`arXiv:2605.27744v1 — §5 prototype policies and serving experiments`。

Trade-off / failure：`arXiv:2605.27744v1 — §6 Limitations — prototype stack, declared agent semantics and engine-hook assumptions; no universal policy correctness`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27744:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27744:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27744:end -->

<!-- review:SF-2026-ARXIV-2605-27752:start -->
#### Same Answer, Different Confidence: Protocol Sensitivity in LLM Confidence Calibration

问题与 changed constraint：confidence calibration is protocol-sensitive: answer normalization, prompt and likelihood extraction are part of the evaluator identity rather than implementation detail。

机制与 ownership：Is verbalized confidence better calibrated than token likelihood? The answer depends on how the token likelihood is measured: which answer is scored, and under which prompt. Published comparisons diverge on this, and in a twelve-study audit five never state the choice. We fix one prediction event per question, the model's own answer together with its correctness label, and score that same answer under a plain query and inside the confidence prompt, holding the answer and its label fixed. Across  owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27752v1 — §3 Calibration protocols (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27752v1 — §4 Experiments (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27752v1 — §5 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27752:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27752:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27752:end -->

<!-- review:SF-2026-ARXIV-2605-27759:start -->
#### Colosseum V2: Benchmarking Generalization for Vision Language Action Models

问题与 changed constraint：VLA generalization evaluation must cross embodiment, task and perturbation strata instead of treating aggregate zero-shot success as transferable physical capability。

机制与 ownership：To systematically study this gap, we introduce Colosseum V2, a large-scale simulation benchmark for evaluating VLA generalization in robot learning across diverse conditions. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27759v1 — § exact heading: I Introduction — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27759v1 — § exact heading: I Introduction — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27759v1 — § exact heading: I Introduction — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27759:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27759:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27759:end -->

<!-- review:SF-2026-ARXIV-2605-27760:start -->
#### SkillGrad: Optimizing Agent Skills Like Gradient Descent

问题与 changed constraint：skill updates need proposal, evaluation, acceptance and rollback analogous to optimizer steps rather than editing procedural files without a quality gate。

机制与 ownership：In this paper, we propose SkillGrad, a gradient-descent-inspired framework for optimizing agent skills. owner=`AGENT-PLATFORM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27760v1 — §3 SkillGrad update loop (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27760v1 — §4 Experiments (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27760v1 — §5 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27760:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27760:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27760:end -->

<!-- review:SF-2026-ARXIV-2605-27761:start -->
#### AndroidDaily: A Verifiable Benchmark for Mobile GUI Agents on Real-World Closed-Source Applications

问题与 changed constraint：mobile-agent tasks on closed-source applications need guideline-grounded state predicates and a verifiable evaluator rather than screenshot-only success claims。

机制与 ownership：To bridge this gap, we introduce AndroidDaily, a large-scale benchmark comprising 350 realistic daily-use tasks across 94 high-frequency Android applications spanning transportation, shopping, local services, entertainment, content creation, social media, and everyday utilities. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27761v1 — § exact heading: 3. Method — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27761v1 — § exact heading: 2.2. Evaluation of GUI Agents — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27761v1 — § exact heading: 4.4. Failure Mode Analysis — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27761:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27761:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27761:end -->

<!-- review:SF-2026-ARXIV-2605-27763:start -->
#### A Paired Testing Protocol for Batch-Conditioned Refusal Robustness in LLM Serving

问题与 changed constraint：batch condition and kernel path enter the safety evaluation identity through paired exact-stack tests and capability controls.。

机制与 ownership：Safety evaluations of language models often treat serving configuration as fixed background infrastructure, but batch condition is an untested treatment variable whenever the same prompt may be evaluated alone, in a synchronized batch, or inside a continuous-batching scheduler. We synthesize four artifact-backed studies into a paired testing protocol: Study A combines local discovery, scorer-corrected adjudication, and true-batching confirmation; Study B tests cross-model generalization; Study C owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27763v1 — §3.1–3.7 paired four-study protocol and synthesis rules`；Evaluation=`arXiv:2605.27763v1 — §4 results including batch-invariant-kernel ablation`。

Trade-off / failure：`arXiv:2605.27763v1 — §5.3 non-claims; §5.4 rare events, scoring, co-batch verification and local-first limitations`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27763:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27763:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27763:end -->

<!-- review:SF-2026-ARXIV-2605-27766:start -->
#### Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems

问题与 changed constraint：privacy evaluation must include persistent social interaction because leakage can propagate between agents even when each isolated prompt appears safe。

机制与 ownership：We introduce a Moltbook-style simulation platform where thousands of LLM agents interact across communities over a simulated month, and use it to evaluate privacy as a downstream safety concern under varying degrees of social pressure. owner=`PLATFORM-SECURITY`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27766v1 — §3 Persistent multi-agent simulation (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27766v1 — §4 Privacy evaluation (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27766v1 — §5 Limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27766:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27766:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27766:end -->

<!-- review:SF-2026-ARXIV-2605-27784:start -->
#### WIRE: Profiling Witnessed Within-Policy Instruction Collisions in LLM Agents

问题与 changed constraint：long-lived prompt policies require executable collision witnesses and resolution profiles so rule precedence and tool-interface effects can be regression tested。

机制与 ownership：Existing instruction-following evaluations usually ask whether a model satis- fies explicit constraints, but they do not show how a model resolves pressure among rules inside one standing policy. owner=`AGENT-PROMPT`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27784v1 — §3 WIRE extraction, SAT nomination and witnessed realization (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27784v1 — §4 Evaluation (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27784v1 — §6 stated non-goals and limitations (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27784:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27784:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27784:end -->

<!-- review:SF-2026-ARXIV-2605-27785:start -->
#### A Query Engine for the Agents

问题与 changed constraint：agent traces become a queryable evidence plane through a client-native engine that combines relational scans with bounded model operators.。

机制与 ownership：People want to analyze it, and the questions worth asking ("show me where the agent got confused") cannot be answered by SQL alone, since text is not queryable without a model in the query path. owner=`PLATFORM-LOGGING`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27785v1 — §3 embedded query-engine architecture, relational/model operator split and bounded execution`；Evaluation=`arXiv:2605.27785v1 — §4 implementation; §5 trace/log query workloads and evaluation`。

Trade-off / failure：`arXiv:2605.27785v1 — §6 limitations — client/runtime, model-operator cost/semantics and disclosed data/workload boundary`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27785:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27785:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27785:end -->

<!-- review:SF-2026-ARXIV-2605-27789:start -->
#### A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test

问题与 changed constraint：LLM-judge comparisons need fixed evidence and answer budgets, cluster-aware inference, preregistered hypotheses and second-judge replication。

机制与 ownership：We propose a minimum measurement standard for LLM-as-a-judge comparisons in RAG. owner=`PLATFORM-EVALUATION-SYSTEM`；论文机制只提供 signal/proposal，最终 admission、commit 或 release authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.27789v1 — § exact heading: 3 Method — method/identity fragment (official exact-v1 HTML read)`；Evaluation=`arXiv:2605.27789v1 — § exact heading: 4 Experimental Setup — evaluation/result fragment (official exact-v1 HTML read)`。

Trade-off / failure：`arXiv:2605.27789v1 — § exact heading: 5.4 Ablation discussion — limitations/counterevidence fragment (official exact-v1 HTML read)`；作者 benchmark 不外推为生产保证，未披露 artifact/hardware/SLO 字段保持 Not Disclosed。

<!-- claim:SF-2026-ARXIV-2605-27789:start -->仅支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-27789:end -->

Books Decision=`Integrate`；已写入 canonical owner，post-write semantic audit passed。
<!-- review:SF-2026-ARXIV-2605-27789:end -->

<!-- review:SF-2026-ARXIV-2605-27820:start -->
#### EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents

问题与 changed constraint：However, existing benchmarks fail to jointly evaluate these capabilities due to challenges in designing strictly coupled multi-capability tasks, simulating natural and task-constrained user feedback, and ensuring objective evaluation of dynamic interaction.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27820v1 — § exact heading: 3.3 Task Design and Ground-truth Annotation`；Evaluation=`arXiv:2605.27820v1 — § exact heading: 2.1 Tool-Using Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.27820v1 — § exact heading: 5 Conclusions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27820v1 — official HTML sha256=e084884e79524dd4bd757618cb34c671331dce1673eadac18e0b6881d86642d3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27820:start -->仅支持 exact-v1 披露机制及实验边界；不把“Furthermore, we establish a deterministic joint validation framework that guarantees objective assessment through process-based and result-based equivalence.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27820:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27820:end -->

<!-- review:SF-2026-ARXIV-2605-27825:start -->
#### MRMMIA: Membership Inference Attacks on Memory in Chat Agents

问题与 changed constraint：We propose Multi-Recall Memory MIA (MRMMIA), a unified attack that utilizes multiple recall probes to the agent to extract the membership signal across black-box, gray-box, and white-box settings.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27825v1 — § exact heading: 3 Threat Model and Problem Formulation`；Evaluation=`arXiv:2605.27825v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27825v1 — § exact heading: 7 Conclusion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27825v1 — official HTML sha256=778098e7df5cf172ed04989da043124faf4d825232bb02bbc1ceeeb0aa110f9a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27825:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our experiments demonstrate that MRMMIA consistently outperforms baselines.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27825:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27825:end -->

<!-- review:SF-2026-ARXIV-2605-27850:start -->
#### TCP-MCP: Landscape-Guided Co-Evolution of Prompts and Communication Topologies for Multi-Agent Systems

问题与 changed constraint：We propose \textbf{TCP-MCP} (Topology-Coupled Prompting for Multi-Agent Collaborative Problem-Solving), a co-evolution framework that searches agent prompts and communication topologies as a unified genome.

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27850v1 — §3 Methods: unified prompt-topology genome and adaptive Pareto control`；Evaluation=`arXiv:2605.27850v1 — §4 Experiments: held-out accuracy, token cost and topology complexity`。

Trade-off / failure / fallback：`arXiv:2605.27850v1 — §5 Conclusion, Limitations, and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27850v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27850:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results show that jointly evolving prompts and communication structure provides a practical route to cost-aware and task-adaptive multi-agent system design in controlled evaluations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27850:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27850:end -->

<!-- review:SF-2026-ARXIV-2605-27879:start -->
#### Towards Faithful Agentic XAI: A Verification Method and an Open-World Benchmark for Better Model Faithfulness

问题与 changed constraint：We propose Faithful Agentic XAI (FAX), a framework that improves explanation faithfulness through explicit verification.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27879v1 — § exact heading: 3 Method: Faithful Agentic XAI`；Evaluation=`arXiv:2605.27879v1 — § exact heading: 4.2 Evaluation scenarios`。

Trade-off / failure / fallback：`arXiv:2605.27879v1 — § exact heading: 6 Conclusions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27879v1 — official HTML sha256=6414fd88678b2d30e7ef60804106d0d709040c51a69d5a37d2f507bfcb6a22c3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27879:start -->仅支持 exact-v1 披露机制及实验边界；不把“These findings show that explicit verification is essential for faithful Agentic XAI and that that faithfulness benchmarks must be designed to test explanations against the behavior of the target model itself.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27879:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27879:end -->

<!-- review:SF-2026-ARXIV-2605-27881:start -->
#### Retrieval, Reward, and Training Protocols: What Matters in Training Search Agents?

问题与 changed constraint：We present a controlled empirical study that isolates three under-explored dimensions of search agent training.

Mechanism 与 ownership：owner=`TRAIN-DATA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27881v1 — § exact heading: 2.1 Reward Design for Search Agent`；Evaluation=`arXiv:2605.27881v1 — § exact heading: 3 Experiments Setup`。

Trade-off / failure / fallback：`arXiv:2605.27881v1 — § exact heading: Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27881v1 — official HTML sha256=07bf6c9ae6e5fe2bbe5681bcaa7fbc987ad4ff370478f650c574244e5f99a760; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27881:start -->仅支持 exact-v1 披露机制及实验边界；不把“First, we identify a critical data-coverage issue in the widely used Wikipedia 2018 corpus and show that correcting it alone yields larger gains than the differences between training algorithms.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27881:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27881:end -->

<!-- review:SF-2026-ARXIV-2605-27898:start -->
#### A Unified Framework for the Evaluation of LLM Agentic Capabilities

问题与 changed constraint：In this work, we present a unified framework for the fair evaluation of LLM agentic capabilities.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27898v1 — § exact heading: 2 Unified Framework`；Evaluation=`arXiv:2605.27898v1 — § exact heading: 2.5 Evaluation Methodology`。

Trade-off / failure / fallback：`arXiv:2605.27898v1 — § exact heading: 3.5 Failure Result Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27898v1 — official HTML sha256=7ee4e3fea5ae787e7b7369f9df610a0f7893a5f73d7d984cc659f19fc82c6ecd; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27898:start -->仅支持 exact-v1 披露机制及实验边界；不把“We further demonstrate its extensibility as a secure testbed for safety-critical domains.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27898:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27898:end -->

<!-- review:SF-2026-ARXIV-2605-27899:start -->
#### SKILLC: Learning Autonomous Skill Internalization in LLM Agents via Contrastive Credit Assignment

问题与 changed constraint：We propose SkillC, a framework based on Contrastive Skill Credit Assignment (CSCA) that converts this contrast into a direct learning signal for internalization.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27899v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27899v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27899v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27899v1 — official HTML sha256=54f2f7366208bc5806dd940984e523d58fd223db4b28a057e2ef039098f1f0ad; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27899:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on ALFWorld and WebShop show that, without runtime skill access, SkillC surpasses the strongest prior skill-internalization RL baseline by 5.5\% and 4.4\%, respectively, while remaining competitive with skill-augmented RL methods.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27899:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27899:end -->

<!-- review:SF-2026-ARXIV-2605-27901:start -->
#### The Fragility of Chain-of-Thought Monitoring Across Typologically Diverse Languages

问题与 changed constraint：We present the first large-scale evaluation of CoT monitorability across 13 diverse languages and seven frontier model families, comprising 16 models.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27901v1 — § exact heading: 4 Can models conceal their reasoning across different languages?`；Evaluation=`arXiv:2605.27901v1 — § exact heading: 3 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.27901v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27901v1 — official HTML sha256=a6ba0236d1abd1ae5608efa74db512b77c0445c54532de292db24bf296c6295c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27901:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results reveal that CoT monitoring is fundamentally fragile under linguistic distribution shift, providing a substantially weaker safety signal than what English-only studies suggest.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27901:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27901:end -->

<!-- review:SF-2026-ARXIV-2605-27918:start -->
#### Addressing Variable Heterogeneity in Distributed Multimodal Training with Entrain

问题与 changed constraint：We present Entrain, a distributed MLLM training framework that addresses both heterogeneity and variability in multimodal training workloads.

Mechanism 与 ownership：owner=`TRAIN-DISTRIBUTED-TRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27918v1 — § exact heading: 2.1. MLLM Architecture and Parallelism`；Evaluation=`arXiv:2605.27918v1 — § exact heading: 4. Macroscopic Analysis-Based Model Parallelization`。

Trade-off / failure / fallback：`arXiv:2605.27918v1 — § exact heading: 2.3. Limitations of Existing Works`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27918v1 — official HTML sha256=22c10a9201b86eead7234ee23182de2058869658bcc76c034c3d95bd886271f3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27918:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluations show that Entrain reduces workload variability across microbatches by up to 10.6$\times$, improving end-to-end training throughput by up to 1.40$\times$ over existing baselines.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27918:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27918:end -->

<!-- review:SF-2026-ARXIV-2605-27922:start -->
#### Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

问题与 changed constraint：However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27922v1 — § exact heading: 3.2 Task Suite Design and Validation`；Evaluation=`arXiv:2605.27922v1 — § exact heading: 3 The Harness-Bench Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.27922v1 — § exact heading: 5.1 Observed Failure Symptoms`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27922v1 — official HTML sha256=3e89c9f28b68276bc33fde7581b7a8428c53bb33ffa950e94aa7ed757cab807c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27922:start -->仅支持 exact-v1 披露机制及实验边界；不把“Harness-Bench provides a reproducible foundation for diagnosing and improving reliable, efficient, and auditable agent execution stacks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27922:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27922:end -->

<!-- review:SF-2026-ARXIV-2605-27947:start -->
#### SANTS: A State-Adaptive Scheduler for World Action Models

问题与 changed constraint：Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or even reverse when late predictions become less action-relevant or physically unreliable.

Mechanism 与 ownership：owner=`INFER-SCHEDULING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27947v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27947v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.27947v1 — § exact heading: 5 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27947v1 — official HTML sha256=6775e77796d135354ae93c0db230ddba4574e84d3cf09c0aa4602b17ce622867; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27947:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that SANTS reaches \(94.4\%\) overall success on RoboTwin 2.0 and \(73.1\%\) average success across seven real-robot tasks, while reducing latency by \(81.7\%\) and \(79.0\%\) relative to full video denoising, respectively.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27947:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27947:end -->

<!-- review:SF-2026-ARXIV-2605-27954:start -->
#### Cyclical Entropy Eruption: Entropy Dynamics in Agent Reinforcement Learning

问题与 changed constraint：However, the training dynamics of agent RL remain poorly understood, limiting our ability to diagnose instabilities and design more effective training algorithms.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27954v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.27954v1 — § exact heading: 4.2 Experimental Settings`。

Trade-off / failure / fallback：`arXiv:2605.27954v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27954v1 — official HTML sha256=2b0011952bb538ff67435afde77b7104a2654683eeb7f17f4e3b82e26a89afa1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27954:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments across multiple benchmarks, models, and RL algorithms demonstrate that SEAL stabilizes training and yields stronger downstream agent performance.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27954:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27954:end -->

<!-- review:SF-2026-ARXIV-2605-27957:start -->
#### DisasterBench: Benchmarking LLM Planning under Typed Tool Interface Constraints

问题与 changed constraint：We introduce DisasterBench, a benchmark for evaluating structured multi-agent planning over semantically similar but operationally distinct disaster-response tools.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27957v1 — § exact heading: 4.6 Reasoning-Optimized Models and Instruction Clash`；Evaluation=`arXiv:2605.27957v1 — § exact heading: 2.1 Tool-Augmented and Multi-Step Planning Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.27957v1 — § exact heading: 4.5 Failure Mode Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27957v1 — official HTML sha256=248798608249a4b17d5fa271b948eefaf1bb5408fa419864abf81f260bc8c5e6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27957:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code, data, and evaluation resources are available at: https://github.com/TamuChen18/DisasterBench_Open”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27957:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27957:end -->

<!-- review:SF-2026-ARXIV-2605-27963:start -->
#### Throughput-Optimized Networks at Scale

问题与 changed constraint：Datacenter network design plays a critical role in AI training by supporting scaling to thousands of accelerators.

Mechanism 与 ownership：owner=`TRAIN-DISTRIBUTED-TRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27963v1 — § exact heading: 2.1. Analytical Models on Performance`；Evaluation=`arXiv:2605.27963v1 — § exact heading: 4.4. Resultant Topologies`。

Trade-off / failure / fallback：`arXiv:2605.27963v1 — § exact heading: 8. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27963v1 — official HTML sha256=8ab4cf20fc446530aa8902eaa42a687c616adf1e944c3c43337c1bd8440106c7; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27963:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that the existing TPU networks leave terabytes per second of throughput on the table and we fill that gap.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27963:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27963:end -->

<!-- review:SF-2026-ARXIV-2605-27980:start -->
#### Periodic RoPE for Infinite Context LLMs

问题与 changed constraint：To address it, we propose Periodic RoPE (P-RoPE), a positional encoding mechanism designed to circumvent this exhaustion.

Mechanism 与 ownership：owner=`MODEL-POSITION-ENCODING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27980v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.27980v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.27980v1 — § exact heading: 6 Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27980v1 — official HTML sha256=20b0adb216b2e7b519721df4af90508fc41737dc57300f9be6baf9753f22ae78; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27980:start -->仅支持 exact-v1 披露机制及实验边界；不把“Empirical results show that our model, MiniWin, outperforms MiniMInd with standard GPT architectures in long-context efficiency and stability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27980:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27980:end -->

<!-- review:SF-2026-ARXIV-2605-27995:start -->
#### AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

问题与 changed constraint：To evaluate it, we propose AsyncTool, a benchmark for assessing LLM-based agents in interactive multi-task tool-use environments with delayed tool feedback.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.27995v1 — § exact heading: 2.1 Agent as a Concurrent Tool-Using System`；Evaluation=`arXiv:2605.27995v1 — § exact heading: 2.3 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.27995v1 — § exact heading: 4 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.27995v1 — official HTML sha256=707fad563547b29d77b0b377d0f1f896c52513d59f87543ff726262ca1f3754c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-27995:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that delayed tool feedback poses substantial challenges to current agents and leads to clear performance degradation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-27995:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-27995:end -->

<!-- review:SF-2026-ARXIV-2605-28000:start -->
#### Tool Forge: A Validation-Carrying Toolchain for Governed Agentic Execution

问题与 changed constraint：Large language model agents are increasingly expected to perform operational work: calling APIs, manipulating files, assembling workflows, and acting inside enterprise systems.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28000v1 — § exact heading: 3 Tool Forge Conceptual Framework`；Evaluation=`arXiv:2605.28000v1 — § exact heading: 9 Experimental Protocol and Baselines`。

Trade-off / failure / fallback：`arXiv:2605.28000v1 — § exact heading: 12 Limitations and Open Questions`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28000v1 — official HTML sha256=5ea862c3ec5aea65324f90f20db2c7c7596ccee5e7250bd3c1675ae44ca0644b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28000:start -->仅支持 exact-v1 披露机制及实验边界；不把“The paper identifies remaining challenges in adversarial routing, broader API grounding, sandbox isolation, and cross-system evaluation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28000:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28000:end -->

<!-- review:SF-2026-ARXIV-2605-28009:start -->
#### MemGuard: Preventing Memory Contamination in Long-Term Memory-Augmented Large Language Models

问题与 changed constraint：To this end, we introduce MemGuard, a type-aware memory framework that preserves functional memory boundaries during memory construction and retrieval.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28009v1 — § exact heading: Appendix E Use of Large Language Models`；Evaluation=`arXiv:2605.28009v1 — § exact heading: 5 Experiment`。

Trade-off / failure / fallback：`arXiv:2605.28009v1 — § exact heading: 7 Conclusions and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28009v1 — official HTML sha256=d6dda2a87c59fd4d07ba02d92c5f0c24c14d09a1096ddb8d79481b5dacfdd055; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28009:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results suggest that reliable long-term reasoning depends on principled organization and selective use of heterogeneous memory.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28009:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28009:end -->

<!-- review:SF-2026-ARXIV-2605-28017:start -->
#### Can It Reach the Generator? Investigating the Survival of Prompt-Injection Attacks in Realistic RAG Settings

问题与 changed constraint：In this paper, we re-evaluate seven GEO attacks under a realistic three-stage pipeline (retriever\,$\to$\,LLM reranker\,$\to$\,LLM generator).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28017v1 — § exact heading: 4.4 Attack Methods`；Evaluation=`arXiv:2605.28017v1 — § exact heading: 3.2 Attack Evaluation in Prior Work`。

Trade-off / failure / fallback：`arXiv:2605.28017v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28017v1 — official HTML sha256=341b7d7e7c46ce09f8c492be68070b3f9c85e07da5caa6d219cea5e2dcf678b6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28017:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that prior protocols substantially overstate attack effectiveness: gradient-based and instruction override attacks largely collapse before reaching the generator, and only LLM-driven prompt injections remain effective end-to-end.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28017:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28017:end -->

<!-- review:SF-2026-ARXIV-2605-28044:start -->
#### Relevant Is Not Warranted: Evidence-Force Calibration for Cited RAG

问题与 changed constraint：We study this diagnostic failure as citation laundering: a related source is presented as warrant for an over-strong claim.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28044v1 — § exact heading: Appendix G Model API and Decoding Configuration`；Evaluation=`arXiv:2605.28044v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28044v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28044v1 — official HTML sha256=5b0d0423fc0dc00a6104deb2486a929aeab242779dfb2a336538c9d90949c46d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28044:start -->仅支持 exact-v1 披露机制及实验边界；不把“We release the benchmark, prompts, outputs, and plug-in pipeline so citation evaluators can report monotonicity violation rate and force sensitivity alongside conventional support metrics.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28044:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28044:end -->

<!-- review:SF-2026-ARXIV-2605-28046:start -->
#### MemCog: From Memory-as-Tool to Memory-as-Cognition in Conversational Agents

问题与 changed constraint：We propose MemCog, a Memory-as-Cognition system that makes memory access an integral part of the reasoning process.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28046v1 — § exact heading: 2.4 Proactive Systems`；Evaluation=`arXiv:2605.28046v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28046v1 — § exact heading: 5 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28046v1 — official HTML sha256=9de207b19cc99467ce05fbe4668f2af43818fe87622c2f2b9f2a2336444ace08; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28046:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that MemCog achieves state-of-the-art on passive QA benchmarks (92.98 on LoCoMo, 95.8 on LongMemEval) while substantially outperforming baselines on ProactiveMemBench, demonstrating the advantage of Memory-as-Cognition.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28046:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28046:end -->

<!-- review:SF-2026-ARXIV-2605-28053:start -->
#### RW-TTT: Batched Serving for Request-Owned Test-Time Training State

问题与 changed constraint：We formulate this problem as read-write TTT serving and present RW-TTT , which tags each decode step with its owner, version, and READ/WRITE effect, batches only compatible phases, and commits updates only to the owner.

Mechanism 与 ownership：owner=`INFER-CONTINUOUS-BATCHING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28053v1 — § exact heading: 2.1 Serving with Mutable Model State`；Evaluation=`arXiv:2605.28053v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28053v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28053v1 — official HTML sha256=d97dad61bd6b3336151a29c7da781ff5a05a6ddc2691377489479fbed0a234c5; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28053:start -->仅支持 exact-v1 披露机制及实验边界；不把“It preserves behavior on RULER, a long-context benchmark, and passes owner/version checks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28053:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28053:end -->

<!-- review:SF-2026-ARXIV-2605-28071:start -->
#### AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent

问题与 changed constraint：In this paper, we present AgentGuard, an attribute-based access control framework for tool-use LLM-based agents.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28071v1 — § exact heading: 1. Introduction`；Evaluation=`arXiv:2605.28071v1 — § exact heading: 2. AgentGuard`。

Trade-off / failure / fallback：`arXiv:2605.28071v1 — § exact heading: 3. Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28071v1 — official HTML sha256=ae831e1a6bf504005cadb4b6e87783430807af808aa4d411b1586ff15d1a4a10; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28071:start -->仅支持 exact-v1 披露机制及实验边界；不把“Currently, AgentGuard is publicly accessible at https://github.com/WhitzardAgent/AgentGuard.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28071:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28071:end -->

<!-- review:SF-2026-ARXIV-2605-28074:start -->
#### SilentRetrieval: Hijacking Retrieval-Augmented Generation via Semantically-Preserving Adversarial Data Poisoning

问题与 changed constraint：We present SilentRetrieval, a two-stage data poisoning attack that hijacks RAG systems through adversarially crafted yet fluent documents.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28074v1 — § exact heading: 3.2. Threat Model`；Evaluation=`arXiv:2605.28074v1 — § exact heading: 5. Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28074v1 — § exact heading: 8. Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28074v1 — official HTML sha256=0fe32804f286c87a8344023ffd30d5f490a312ecc2910c900d6ce0e8d95981ae; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28074:start -->仅支持 exact-v1 披露机制及实验边界；不把“Human evaluation shows substantially lower flag rates than disfluent baselines, while remaining numerically more suspicious than benign content at the current sample size.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28074:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28074:end -->

<!-- review:SF-2026-ARXIV-2605-28083:start -->
#### VLA-Hijack: A Transferable Patch Attack against Vision-Language-Action Models via Visual Proprioception Hijacking

问题与 changed constraint：To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28083v1 — § exact heading: 2.1 Vision-Language-Action Models`；Evaluation=`arXiv:2605.28083v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28083v1 — § exact heading: 3.1 Preliminaries & Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28083v1 — official HTML sha256=75a70820341d7c1995d5dcce0f6e2ef4087be2e4ee456e5403fa26986a59e552; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28083:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments across diverse architectures (OpenVLA, UniVLA, and CronusVLA) demonstrate that VLA-Hijack achieves superior optimization efficiency in white-box settings and sets a new SOTA for cross-architecture and cross-domain black-box transferability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28083:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28083:end -->

<!-- review:SF-2026-ARXIV-2605-28095:start -->
#### SiDP: Memory-Efficient Data Parallelism for Offline LLM Inference

问题与 changed constraint：We present SiDP, a memory-efficient data-parallel paradigm for offline LLM inference that treats weights as a bandwidth-backed shared resource inside a DP group.

Mechanism 与 ownership：owner=`INFER-GPU-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28095v1 — § exact heading: 2.1 Large Language Models`；Evaluation=`arXiv:2605.28095v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28095v1 — § exact heading: 4.4 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28095v1 — official HTML sha256=5a35d6208f87777291ee083ee28d0ca39f8edf85bbf757764809c8cc70d60976; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28095:start -->仅支持 exact-v1 披露机制及实验边界；不把“Evaluated on NVIDIA H20, H200, and B200 GPUs with Qwen3-32B, Qwen2.5-72B, and Llama-3.1-70B, SiDP increases usable KV capacity by up to 1.8x under the same configurations, and converts this into up to 1.5x higher end-to-end throughput over baselines (vLLM) for offline workloads.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28095:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28095:end -->

<!-- review:SF-2026-ARXIV-2605-28097:start -->
#### ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents

问题与 changed constraint：We present ICAN-Deploy (Identity-stable CANary Deployment), a middleware construction whose state machine holds the identity hash invariant across the canary window by separating capability names (frozen, hashed) from capability versions (mutable runtime state).

Mechanism 与 ownership：owner=`PLATFORM-PRODUCTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28097v1 — § exact heading: 3. Design`；Evaluation=`arXiv:2605.28097v1 — § exact heading: 5. Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28097v1 — § exact heading: 5.5. Failure-Mode Taxonomy`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28097v1 — official HTML sha256=414916db7f1e595f656d28986787a19c47a828a3a85d39a16a19704252d2638a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28097:start -->仅支持 exact-v1 披露机制及实验边界；不把“A system certified once at identity-creation time can then ship arbitrary capability evolution under that same certification, within the version-and-name envelope.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28097:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28097:end -->

<!-- review:SF-2026-ARXIV-2605-28108:start -->
#### Ask Now, Use Later: Benchmarking the Proactivity Gap in Long-Lived LLM Agents

问题与 changed constraint：ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.

Mechanism 与 ownership：owner=`AGENT-PLANNING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28108v1 — § exact heading: Appendix B Runtime Framework`；Evaluation=`arXiv:2605.28108v1 — § exact heading: 2.2 Why ATR Resists Direct Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28108v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28108v1 — official HTML sha256=955cb683e1219ce043363a3f80c8c78f68fcf31db7a68d671b8cbcbc921b93bd; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28108:start -->仅支持 exact-v1 披露机制及实验边界；不把“ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28108:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28108:end -->

<!-- review:SF-2026-ARXIV-2605-28112:start -->
#### A Wolf in Sheep's Clothing: Targeted Routing Hijacking in Federated RAG

问题与 changed constraint：We introduce Routing Hijacking, a routing-stage attack in which a malicious client forges its profile to attract target queries despite having irrelevant underlying data.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28112v1 — § exact heading: 2.2 Threat Model and Attack Realism`；Evaluation=`arXiv:2605.28112v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28112v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28112v1 — official HTML sha256=d0cbc74c408247a70679909334b0628c17fb424771394eb5869d80f3ad9c15f7; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28112:start -->仅支持 exact-v1 披露机制及实验边界；不把“To address this gap, we propose a trust-aware post-routing framework that reweights clients using returned-evidence feedback, including retrieval relevance, profile consistency, and cross-client agreement; online experiments show that it suppresses persistent hijacking over recurring queries and transfers to a learned neural router.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28112:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28112:end -->

<!-- review:SF-2026-ARXIV-2605-28116:start -->
#### MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content

问题与 changed constraint：We present MIRAGE (Mobile Injection of Realistic Adversarial GUI Examples), a pipeline that turns benign mobile screenshots into prompt-injection samples by placing attacker-controlled text into ordinary user-generated content regions, without modifying the agent, the application, or the operating system.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28116v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28116v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28116v1 — § exact heading: 3.1 Threat Model and Problem Setup`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28116v1 — official HTML sha256=1468243f7898c335be4b2032a41fce144cd2cde51fbfa05bdec6192f398d54b1; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28116:start -->仅支持 exact-v1 披露机制及实验边界；不把“We further find that per-sample realism and attack success are uncorrelated, so visual-quality filtering alone cannot reliably defend against this threat.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28116:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28116:end -->

<!-- review:SF-2026-ARXIV-2605-28122:start -->
#### SNARE: Adaptive Scenario Synthesis for Eliciting Overeager Behavior in Coding Agents

问题与 changed constraint：We present SNARE (Synthesizing Non-adversarial scenarios for Adaptive Reward-guided Elicitation), a pipeline that composes benign scenarios from reusable scope and trap fragments, scores each run with a judge-free oracle flagging trap-pattern matches and unsolicited file additions or deletions, and uses Thompson sampling to steer each pair's run budget toward the scenarios that most often trigger it.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28122v1 — § exact heading: 4 Methodology`；Evaluation=`arXiv:2605.28122v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28122v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28122v1 — official HTML sha256=2b2263367a509d311807ea14ffd2bbe1d4340d5061f31a11a4c27daea64d124d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28122:start -->仅支持 exact-v1 披露机制及实验边界；不把“This variation is driven by the agent framework, not the model: the framework accounts for 56% of it against the model's 21%, so any single-framework or single-model evaluation undercounts the matrix by about a fifth.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28122:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28122:end -->

<!-- review:SF-2026-ARXIV-2605-28158:start -->
#### OR-Space: A Full-Lifecycle Workspace Benchmark for Industrial Optimization Agents

问题与 changed constraint：We introduce OR-Space, a full-lifecycle workspace benchmark for evaluating industrial optimization agents across model construction, model revision, and grounded explanation.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28158v1 — § exact heading: 4.3. Workspace Setting Matters: Filesystem vs. Flat Prompt`；Evaluation=`arXiv:2605.28158v1 — § exact heading: 3. OR-Space Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28158v1 — § exact heading: 4.6. Failure Analysis: What Workspace Evaluation Reveals`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28158v1 — official HTML sha256=1e17ba2cca067758b922a556965e0431d6551145b624769cbaad189a8f57f6d0; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28158:start -->仅支持 exact-v1 披露机制及实验边界；不把“We describe the benchmark design, evaluation protocol, and quality-control pipeline, and position OR-Space as a benchmark for studying the reliability, failure modes, and practical readiness of LLM agents in industrial OR workflows.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28158:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28158:end -->

<!-- review:SF-2026-ARXIV-2605-28201:start -->
#### Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents

问题与 changed constraint：However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28201v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28201v1 — § exact heading: 3 Benchmark Construction`。

Trade-off / failure / fallback：`arXiv:2605.28201v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28201v1 — official HTML sha256=008668763414245306a7e06dd0162aab018a8ec8de1d63dca6d2c395d1635c86; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28201:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on seven strong open-source and closed-source LLMs show that state-of-the-art LLM agents remain vulnerable to Sleeper Attack, even when they achieve low attack success rates under a single-interaction baseline.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28201:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28201:end -->

<!-- review:SF-2026-ARXIV-2605-28213:start -->
#### Learning When to Optimize: Verified Optimization Skills from Expert GPU-Kernel Lineages

问题与 changed constraint：We introduce KLineage, which learns this missing "when" knowledge from expert kernels: instead of relying on forward rollouts, KLineage walks expert implementations backward through validation-gated simplifications and reverses each accepted step into a reusable optimization skill.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28213v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28213v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28213v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28213v1 — official HTML sha256=5a6c29327a16eb486f3ab87c7947285bdc6cf70c05861afc9e6be33047d4bd05; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28213:start -->仅支持 exact-v1 披露机制及实验边界；不把“We additionally use a separate 22-instance held-out check as a sanity test against source-case memorization.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28213:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28213:end -->

<!-- review:SF-2026-ARXIV-2605-28214:start -->
#### Out of Sight, Not Out of Mind: Unveiling Latent Attack in Latent-based Multi-Agent Systems

问题与 changed constraint：In this paper, we study whether latent states can carry attack-associated information that remains effective during clean executions.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28214v1 — § exact heading: 2.1 Latent-based Multi-Agent Systems`；Evaluation=`arXiv:2605.28214v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28214v1 — § exact heading: 2.3 Threat Model`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28214v1 — official HTML sha256=91ee9043fb86499854c2113111e547d97fe383fdeafe52160c01d2cf035e9872; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28214:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that the resulting latent attacks can substantially degrade task performance in clean executions, especially when applied to inter-agent KV-cache handoffs rather than local hidden states.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28214:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28214:end -->

<!-- review:SF-2026-ARXIV-2605-28224:start -->
#### When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?

问题与 changed constraint：We propose a unified framework that decomposes memory along two axes -- the scope of transfer (within an expansion vs.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28224v1 — § exact heading: 3 A Unified Memory Framework`；Evaluation=`arXiv:2605.28224v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28224v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28224v1 — official HTML sha256=f73c2b99847ff63b93b3448413df8cbc3980da4f411624734fb2481eb52a14b3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28224:start -->仅支持 exact-v1 披露机制及实验边界；不把“across trajectories) and the abstraction of the transferred content -- and evaluate four methods under three inference strategies (best-of-N, beam search, MCTS) on four tool-use benchmarks spanning SQL, knowledge-graph, and CLI environments, in a verifier-free setting that matches the deployment regime of practical agents.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28224:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28224:end -->

<!-- review:SF-2026-ARXIV-2605-28282:start -->
#### ResearchLoop: An Evidence-Gated Control Plane for AI-Assisted Research

问题与 changed constraint：We present ResearchLoop, an evidence-gated control plane for AI-assisted computational research.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28282v1 — §3 ResearchLoop Protocol and Runtime; §4 Runtime Implementation`；Evaluation=`arXiv:2605.28282v1 — §7 controlled study and ablations`。

Trade-off / failure / fallback：`arXiv:2605.28282v1 — §7.2 synthetic task, single-model and sample-size limitations; Appendix C claim ledger`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28282v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28282:start -->仅支持 exact-v1 披露机制及实验边界；不把“All artifacts, manifests, and verification reports are preserved in the project repository.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28282:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28282:end -->

<!-- review:SF-2026-ARXIV-2605-28302:start -->
#### How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving

问题与 changed constraint：Each level of disaggregation deepens the scheduling design space across workload characteristics, resource allocation, and interconnect topology, raising the central question: when does each level actually pay off?

Mechanism 与 ownership：owner=`INFER-PD-DISAGGREGATION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28302v1 — § exact heading: 2.1 Design-Space Exploration for Optimal Disaggregated Inference`；Evaluation=`arXiv:2605.28302v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28302v1 — § exact heading: 5 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28302v1 — official HTML sha256=d5bcb04b9f513ea26df32ea551e09fe23f72ba5651979e05cd229e9f171c23cf; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28302:start -->仅支持 exact-v1 披露机制及实验边界；不把“We distill concrete takeaways for jointly optimizing throughput and interactivity, including how to partition attention and FFN across GPUs as a function of workload and model architecture, providing design principles for current rack- and cluster-scale deployments as well as future disaggregated AI infrastructure.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28302:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28302:end -->

<!-- review:SF-2026-ARXIV-2605-28354:start -->
#### Plan Before Search: Search Agents Need Plan

问题与 changed constraint：We study this through Plan, a structured agentic behavior for multi-hop retrieval that decomposes a question into ordered sub-questions before any retrieval is performed, so that each search step can be anchored to a pre-designed sub-question instead of drifting under the influence of partially relevant documents retrieved earlier.

Mechanism 与 ownership：owner=`AGENT-PLANNING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28354v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28354v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28354v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28354v1 — official HTML sha256=adefd62b5877ddd6b889b2d5466bf6d86dea3f49ca521809b6edc772b94d5cd9; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28354:start -->仅支持 exact-v1 披露机制及实验边界；不把“However, across three model families spanning 3B to 14B parameters, we find that an identical reward signal induces qualitatively different RL failure modes.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28354:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28354:end -->

<!-- review:SF-2026-ARXIV-2605-28371:start -->
#### From paper to benchmark: agentic, framework-based reproduction of under-specified methods in machine health intelligence

问题与 changed constraint：Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating published papers into executable, benchmark-ready implementations.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28371v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28371v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28371v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28371v1 — official HTML sha256=59b8cf453e48c85d21d2f09b6119c474e58ef81f53f90f1a81cd0252e3e6a66d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28371:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results show that coupling agentic generation with a shared framework transforms paper reproduction from isolated code synthesis into executable, assumption-aware, and systematically comparable benchmark implementations.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28371:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28371:end -->

<!-- review:SF-2026-ARXIV-2605-28384:start -->
#### Meta-Attention: Bayesian Per-Token Routing for Efficient Transformer Inference

问题与 changed constraint：We propose Meta-Attention, a framework that dynamically routes each token to the most appropriate attention strategy -- full softmax attention, linear (kernel) attention, or sliding-window local attention -- via a Bayesian Meta-Controller.

Mechanism 与 ownership：owner=`INFER-SCHEDULING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28384v1 — § exact heading: 2.4 State Space Models and the Case for an SSM Expert`；Evaluation=`arXiv:2605.28384v1 — § exact heading: 5.3 Bayesian vs. Prior-Free Ablation: Tiny LM Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28384v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28384v1 — official HTML sha256=1570cc4c065bb54d719c2ab73ec29c27fc79dd28dbc83353e870b38450392418; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28384:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code available at: https://github.com/KFEAL/meta-attention”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28384:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28384:end -->

<!-- review:SF-2026-ARXIV-2605-28390:start -->
#### You Live More Than Once: Towards Hierarchical Skill Meta-Evolving

问题与 changed constraint：Specifically, we propose HiSME, a lightweight hierarchical skill meta-evolving solution that jointly optimizes skills and the skill evolving strategy by learning meta-skills from agents' task execution traces.

Mechanism 与 ownership：owner=`AGENT-PLATFORM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28390v1 — § exact heading: 2.1 Agentic Systems`；Evaluation=`arXiv:2605.28390v1 — § exact heading: 3.3 Skill Evaluation and Maintenance`。

Trade-off / failure / fallback：`arXiv:2605.28390v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28390v1 — official HTML sha256=319497612764ee707963a369e412c779142c648f077829de02a9af1827bce409; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28390:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on mainstream agentic benchmarks show that meta-evolving can produce a higher-quality skill library than pure skill evolving and can derive diverse meta-skills for different scenarios, thereby facilitating future continual experience learning.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28390:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28390:end -->

<!-- review:SF-2026-ARXIV-2605-28424:start -->
#### Skill0.5: Joint Skill Internalization and Utilization for Out-of-Distribution Generalization in Agentic Reinforcement Learning

问题与 changed constraint：To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28424v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28424v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28424v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28424v1 — official HTML sha256=56b115a0cea14050550666972c8c3358a23dadd06e5ca9e392e0893d2e08a307; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28424:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on ALFWorld and WebShop demonstrate that Skill0.5 outperforms both memory-based and skill-based RL baselines, yielding performance improvements across both in-distribution and out-of-distribution scenarios.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28424:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28424:end -->

<!-- review:SF-2026-ARXIV-2605-28433:start -->
#### Roles with Rails: Contract-Preserving Role Evolution in Multi-Agent Structured Reasoning

问题与 changed constraint：We formulate this as contract-preserving role evolution, requiring every committed edit to preserve five structural contracts (capability, communication, validation, aggregation, output protocol).

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28433v1 — § exact heading: 3 Methodology: Sero`；Evaluation=`arXiv:2605.28433v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28433v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28433v1 — official HTML sha256=e6b9fa986647a1fdfaf40f75332819e7664fd3c3068b1e2919f51ea7317a4f5f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28433:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on real-world reasoning benchmarks across three LLM backbones confirm the value of contract-preserving role evolution.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28433:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28433:end -->

<!-- review:SF-2026-ARXIV-2605-28467:start -->
#### Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training

问题与 changed constraint：We study consistency training, a family of fine-tuning objectives that enforce identical behavior on clean prompts and adversarial rewrites, and evaluate its two main variants, output-level (BCT) and activation-level (ACT), across five reasoning models.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28467v1 — § exact heading: 3 Methodology`；Evaluation=`arXiv:2605.28467v1 — § exact heading: 4.1 Benchmarks`。

Trade-off / failure / fallback：`arXiv:2605.28467v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28467v1 — official HTML sha256=8bc115de594103d60edec321cb4440daecf363960c1cb513ddb91f26c2fa43de; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28467:start -->仅支持 exact-v1 披露机制及实验边界；不把“We find that ACT remains robust even when the model's chain-of-thought is replaced with a compliant trace from the undefended base model, pivoting to refuse prefilled jailbreaks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28467:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28467:end -->

<!-- review:SF-2026-ARXIV-2605-28480:start -->
#### Audio-Mind: An Auditable Agentic Framework for Audio Understanding

问题与 changed constraint：We propose Audio-Mind, an auditable and pluggable framework for conditional evidence acquisition in audio understanding.

Mechanism 与 ownership：owner=`AGENT-WORKFLOW`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28480v1 — § exact heading: 2.1 Large Audio-Language Models and Audio Understanding Benchmarks`；Evaluation=`arXiv:2605.28480v1 — § exact heading: 5 Results`。

Trade-off / failure / fallback：`arXiv:2605.28480v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28480v1 — official HTML sha256=d213543a1628789189242389ff40e33dc0b8dc1e48532230aa0d590500274040; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28480:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on MMAR and MSU-Bench show that Audio-Mind outperforms prior audio-agent baselines, reaching 80.4% accuracy on MMAR and 82.8% accuracy on MSU-Bench.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28480:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28480:end -->

<!-- review:SF-2026-ARXIV-2605-28508:start -->
#### Benchmarking AI for low-resource contexts: Thinking beyond leaderboards

问题与 changed constraint：To support practical decision-making, we propose a shared reporting framework that preserves comparability across systems and application types while remaining sensitive to deployment context.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28508v1 — pp. 6–8 §3 System under test and layered evaluation`；Evaluation=`arXiv:2605.28508v1 — pp. 8–11 §4 application profiles and operating-condition tests`。

Trade-off / failure / fallback：`arXiv:2605.28508v1 — pp. 11–13 §5 minimum benchmark standard and reporting limits`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28508v1 — official PDF sha256=8beef4051c11d29813c7f2801e1cf88087f06e659f52cb810f1d20df4999a24d; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28508:start -->仅支持 exact-v1 披露机制及实验边界；不把“Finally, we emphasize the need for concise and actionable reporting artifacts for policymakers, donors, and implementers, including standardized one-page benchmark cards, deployment profiles, and explicit documentation of failure handling procedures and human oversight mechanisms.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28508:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28508:end -->

<!-- review:SF-2026-ARXIV-2605-28510:start -->
#### Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets

问题与 changed constraint：To bridge this gap, we introduce SOURCETRACKER, a 300M-parameter encoder tailored for code retrieval, together with a hybrid two-stage provenance-tracking pipeline HYBRIDSOURCETRACKER (HST).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28510v1 — §III Methodology: SourceTracker, Winnowing and HybridSourceTracker`；Evaluation=`arXiv:2605.28510v1 — §IV Results: recall, rank and latency`。

Trade-off / failure / fallback：`arXiv:2605.28510v1 — §V errors; §VI Discussion; §VIII-A future-work boundaries`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28510v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28510:start -->仅支持 exact-v1 披露机制及实验边界；不把“Overall, our results demonstrate that integrating vector search with fingerprinting enables scalable, high-precision provenance tracking for code produced by LLMs.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28510:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28510:end -->

<!-- review:SF-2026-ARXIV-2605-28544:start -->
#### DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving

问题与 changed constraint：We present DriveWAM, a driving world-action model that adapts a pretrained video diffusion transformer into an autoregressive video-action policy.

Mechanism 与 ownership：owner=`MULTIMODAL-WORLD-MODELS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28544v1 — §3 Method: autoregressive world-action flow, causal guidance and selective KV memory`；Evaluation=`arXiv:2605.28544v1 — §4 Experiments and ablations`。

Trade-off / failure / fallback：`arXiv:2605.28544v1 — §5 Conclusion; Appendix C efficiency analysis; no dedicated limitations section`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28544v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28544:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on NAVSIM and the PhysicalAI-Autonomous-Vehicles benchmark show that DriveWAM achieves strong planning performance, and a data-scaling study from 4k to 100k driving clips further confirms the scaling potential of world-action modeling for end-to-end autonomous driving.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28544:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28544:end -->

<!-- review:SF-2026-ARXIV-2605-28561:start -->
#### Soft-SVeRL: Self-Verified Reinforcement Learning with Soft Rewards

问题与 changed constraint：We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals.

Mechanism 与 ownership：owner=`TRAIN-RLHF`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28561v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28561v1 — § exact heading: 5 Experiment Setup`。

Trade-off / failure / fallback：`arXiv:2605.28561v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28561v1 — official HTML sha256=37a019db49266025a9f512e89d9d0055db4d54c74d0e179610cf4b5525ed3956; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28561:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our experiments further show that verifier quality and checklist quality both affect downstream RL outcomes, and that explicit stabilization is essential for effective self-verification.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28561:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28561:end -->

<!-- review:SF-2026-ARXIV-2605-28565:start -->
#### Verified Misguidance: Measuring Structural Citation Failures in Search-Augmented LLMs

问题与 changed constraint：We design a three-dimension evaluation framework that scores each citation on intent-purpose alignment, source suitability, and answer-source fidelity, using expert-validated predefined matrices and a five-level fidelity rubric; the framework applies to any system that produces citation-bearing responses.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28565v1 — §2 CiteTrace construction; §3 three-dimensional citation evaluation`；Evaluation=`arXiv:2605.28565v1 — §4 structural citation failures and judge validation`。

Trade-off / failure / fallback：`arXiv:2605.28565v1 — Appendix A.1 scope assumptions and A.2 limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28565v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28565:start -->仅支持 exact-v1 披露机制及实验边界；不把“Together, CITETRACE and its evaluation framework provide the first resource for diagnosing structural citation failures in deployed search-augmented systems.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28565:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28565:end -->

<!-- review:SF-2026-ARXIV-2605-28573:start -->
#### Efficient Pre-Training of LLMs through Truncated SVD Layers

问题与 changed constraint：The massive scaling of Large Language Models (LLMs) has made pretraining increasingly cost-prohibitive.

Mechanism 与 ownership：owner=`TRAIN-PRETRAINING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28573v1 — § exact heading: 3 The TSVD Method`；Evaluation=`arXiv:2605.28573v1 — § exact heading: 4.3 Experimental Derivation of Adaptive Rank Selection Heuristic`。

Trade-off / failure / fallback：`arXiv:2605.28573v1 — § exact heading: 6 Discussion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28573v1 — official HTML sha256=74ef57819f581ccb20cd92e1585f01f2b930e2513a90ce9043b00e552d767079; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28573:start -->仅支持 exact-v1 披露机制及实验边界；不把“Theoretical analysis justifies the advantage of the approach in pretraining dynamics and experiments across various model scales demonstrate that it is effective empirically.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28573:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28573:end -->

<!-- review:SF-2026-ARXIV-2605-28617:start -->
#### LACUNA: Safe Agents as Recursive Program Holes

问题与 changed constraint：We present LACUNA, a programming model for agents that closes this split while preserving safety.

Mechanism 与 ownership：owner=`AGENT-TOOL-CALLING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28617v1 — §3 typed holes and nested calls; §4 static/capability safety`；Evaluation=`arXiv:2605.28617v1 — §7 verifier, tool-use and multi-turn evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28617v1 — §Limitations: well-typed is not correct; authority is only as tight as granted scope`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28617v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28617:start -->仅支持 exact-v1 披露机制及实验边界；不把“We evaluate LACUNA on a collection of test cases, BrowseComp-Plus, and $τ^2$-bench.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28617:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28617:end -->

<!-- review:SF-2026-ARXIV-2605-28632:start -->
#### Blind PRNG Hijacking: An Undetectable Integrity-Preserving Attack Against LLM Watermarking

问题与 changed constraint：Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs).

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28632v1 — § exact heading: 2.3 PRNG Security in ML Systems`；Evaluation=`arXiv:2605.28632v1 — § exact heading: 5 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28632v1 — § exact heading: 3 Threat Model and Problem Formulation`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28632v1 — official HTML sha256=aafde923a8bedf299b01a1b87790b4fc26d09b9c734ec1891536e0ffbba5474c; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28632:start -->仅支持 exact-v1 披露机制及实验边界；不把“These findings establish PRNG integrity as a first-class security requirement for cryptographic content-provenance systems.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28632:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28632:end -->

<!-- review:SF-2026-ARXIV-2605-28634:start -->
#### PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation

问题与 changed constraint：We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble &amp; Assemble paradigm.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28634v1 — § exact heading: 2.1 Vision-Language-Action Models`；Evaluation=`arXiv:2605.28634v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28634v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28634v1 — official HTML sha256=28d4c6c0aa204e61c3cfe7c1bd438f923cee3007f437aec33e041b2342f66af3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28634:start -->仅支持 exact-v1 披露机制及实验边界；不把“Extensive experiments show that our framework improves data efficiency and achieves superior zero-shot generalization across unseen and long-horizon tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28634:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28634:end -->

<!-- review:SF-2026-ARXIV-2605-28640:start -->
#### Augmenting Attention with Exponentially Decaying Memory Improves Query-Aware KV Sparsity

问题与 changed constraint：In this paper, we investigate whether this exponentially decaying memory can also improve existing query-aware sparse inference methods.

Mechanism 与 ownership：owner=`INFER-KV-CACHE`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28640v1 — §2 exponentially decaying memory and sparse inference instantiations`；Evaluation=`arXiv:2605.28640v1 — §3 experiments and H1/H2 analyses`。

Trade-off / failure / fallback：`arXiv:2605.28640v1 — §Limitations: two 7B checkpoints, 4K context and RULER-only task family`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28640v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28640:start -->仅支持 exact-v1 披露机制及实验边界；不把“Using representative methods including Quest, MoBA, and SnapKV, we show that RAT+ consistently improves accuracy over standard attention across sparse budgets on eight needle-in-a-haystack tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28640:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28640:end -->

<!-- review:SF-2026-ARXIV-2605-28646:start -->
#### MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution

问题与 changed constraint：We present MaskClaw, an edge-side privacy arbitrator for GUI agents.

Mechanism 与 ownership：owner=`PLATFORM-SECURITY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28646v1 — §4 edge evidence extraction, policy arbitration, SafeScreenshot and skill evolution`；Evaluation=`arXiv:2605.28646v1 — §5–6 evaluation, sandbox checks and error analysis`。

Trade-off / failure / fallback：`arXiv:2605.28646v1 — §Limitations: sanitized scenarios, trusted edge and short-horizon personalization`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28646v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28646:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that pattern matching, cloud reasoning, and routing alone tend to over-confirm, over-mask, or expose raw screenshots under the same protocol.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28646:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28646:end -->

<!-- review:SF-2026-ARXIV-2605-28678:start -->
#### DREAM-R: Multimodal Speculative Reasoning with RL-Based Refined Drafting, Precise Verification, and Fully Parallel Execution

问题与 changed constraint：In this work, we introduce DREAM-R, a framework that substantially improves the performance of speculative reasoning.

Mechanism 与 ownership：owner=`INFER-SPECULATIVE-DECODING`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28678v1 — § exact heading: 3 Method`；Evaluation=`arXiv:2605.28678v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28678v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28678v1 — official HTML sha256=1a1a8f4e1c8ac3653a31c04eee5001b8bd690ec4cacab7bfa00bc96c7270d947; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28678:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments on reasoning-heavy benchmarks demonstrate up to speedup while preserving target-model accuracy, yielding substantial efficiency gains without compromising reasoning quality.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28678:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28678:end -->

<!-- review:SF-2026-ARXIV-2605-28691:start -->
#### OSP-Next: Efficient High-Quality Video Generation with Sparse Sequence Parallelism, HiF8 Quantization, and Reinforcement Learning

问题与 changed constraint：We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning.

Mechanism 与 ownership：owner=`MULTIMODAL-GENERATIVE-PARADIGMS`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28691v1 — § exact heading: 2.1 Sparse Video Generation Model`；Evaluation=`arXiv:2605.28691v1 — § exact heading: 4 Experiment`。

Trade-off / failure / fallback：`arXiv:2605.28691v1 — § exact heading: 5 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28691v1 — official HTML sha256=327ba473a5ca5523ab42d5daa2cd3b7c42aeeee6b6ecb6ae168b5896299fc13a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28691:start -->仅支持 exact-v1 披露机制及实验边界；不把“Experiments show that OSP-Next achieves a VBench total score of 83.73%, surpassing the Wan2.1 baseline.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28691:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28691:end -->

<!-- review:SF-2026-ARXIV-2605-28699:start -->
#### TRACER: Turn-level Regret Matching with Inner Reinforcement Credit for Cooperative Multi-LLM Reasoning

问题与 changed constraint：We introduce TRACER, a turn-level reinforcement framework for cooperative multi-LLM reasoning.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28699v1 — § exact heading: 2.2 Multi-Agent System`；Evaluation=`arXiv:2605.28699v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28699v1 — § exact heading: 6 Conclusion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28699v1 — official HTML sha256=b46ff12911d0d68e6d23a196c51d66c97243f6cce1cd9ee2d7c2e6a1acc91235; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28699:start -->仅支持 exact-v1 披露机制及实验边界；不把“We train all local RL-style methods on the GSM8K training split and evaluate on held-out GSM8K, MATH500, and GPQA-Diamond to measure in-domain accuracy, cross-benchmark generalization, inference cost, and correction-preservation behavior.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28699:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28699:end -->

<!-- review:SF-2026-ARXIV-2605-28704:start -->
#### Expressive Power of Floating-Point Neural Networks with Arbitrary Reduction Orders and Inexact Activation Implementations

问题与 changed constraint：In this work, we study the expressive power of floating-point neural networks under generalized floating-point execution semantics, including arbitrary reduction orders and inexact activation implementations with bounded ulp errors.

Mechanism 与 ownership：owner=`INFER-TENSORRT-LLM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28704v1 — § exact heading: I Introduction`；Evaluation=`arXiv:2605.28704v1 — § exact heading: III Main Results`。

Trade-off / failure / fallback：`arXiv:2605.28704v1 — § exact heading: I-A Contribution`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28704v1 — official HTML sha256=4a7a9a3977cbb61bc5708038d0f880bde52cc4bfcdd5fb033aee756b8612194f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28704:start -->仅支持 exact-v1 披露机制及实验边界；不把“To this end, we introduce a general distinguishability framework and show that the ability to distinguish every pair of distinct inputs in the first layer is necessary for universal representability.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28704:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28704:end -->

<!-- review:SF-2026-ARXIV-2605-28721:start -->
#### LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?

问题与 changed constraint：We study this question on BrowseComp with three diagnostics.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28721v1 — § exact heading: 2.4 From Diagnosis to Benchmark Design`；Evaluation=`arXiv:2605.28721v1 — § exact heading: 2.3 Search Strategy Analysis`。

Trade-off / failure / fallback：`arXiv:2605.28721v1 — § exact heading: 6 Discussion and Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28721v1 — official HTML sha256=aeaa68114c24fa582046ca5879e68e549f4c733433734b424d86c75f38e35acf; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28721:start -->仅支持 exact-v1 披露机制及实验边界；不把“We then introduce LiveBrowseComp, a deep-search benchmark designed to evaluate agents beyond intrinsic coverage.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28721:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28721:end -->

<!-- review:SF-2026-ARXIV-2605-28726:start -->
#### How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures

问题与 changed constraint：We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28726v1 — § exact heading: II Method`；Evaluation=`arXiv:2605.28726v1 — § exact heading: IV Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28726v1 — § exact heading: IV-C Failure Prediction: Which Monitors Work?`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28726v1 — official HTML sha256=90cd7e1a54362609991628c3db8b3b43348ca9e11c25067c1e202fb5bc05f38f; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28726:start -->仅支持 exact-v1 披露机制及实验边界；不把“Running VQ-BeT, Diffusion Policy, and ACT on identical evaluation protocols (n=450 episodes across PushT and ALOHA 14-DOF bimanual manipulation), we find: (1) direction reversal rate is a universal failure predictor across all three architectures (AUROC=0.93, 0.79, 0.91; p&lt;0.001); (2) jerk monitoring is predictive only for discrete-token architectures, following a discrete-to-continuous gradient (0.88, 0.69, 0.41)”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28726:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28726:end -->

<!-- review:SF-2026-ARXIV-2605-28732:start -->
#### MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems

问题与 changed constraint：In this work, we study the new problem of error tracing and attribution in LLM memory systems.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28732v1 — § exact heading: 2 Tracing and Attributing Errors in Memory Systems`；Evaluation=`arXiv:2605.28732v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28732v1 — § exact heading: 8 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28732v1 — official HTML sha256=c81383e0d1ae7799a14d2a9bd4911c986acf573281a52a6c6c13834fbea2f6a3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28732:start -->仅支持 exact-v1 披露机制及实验边界；不把“Code will be released at https://github.com/zjunlp/MemTrace.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28732:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28732:end -->

<!-- review:SF-2026-ARXIV-2605-28742:start -->
#### CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning

问题与 changed constraint：To address this challenge, we introduce Contrastive Reflection (CORE), a non-parametric learning algorithm that compares past reasoning traces to generate insights: short natural-language descriptions of reasoning strategies and constraints that capture differences between successful and unsuccessful problem attempts.

Mechanism 与 ownership：owner=`AGENT-REFLECTION`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28742v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28742v1 — § exact heading: 4 Evaluation`。

Trade-off / failure / fallback：`arXiv:2605.28742v1 — § exact heading: 6 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28742v1 — official HTML sha256=948395dbaa3e07d1b9fdd398c0c4b798d06dc1a875a55c6c2950cc6ff67acefa; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28742:start -->仅支持 exact-v1 披露机制及实验边界；不把“Across four reasoning tasks, we demonstrate that CORE enables more rapid improvement than both parametric (GRPO) and non-parametric (GEPA, episodic RAG, and MemRL) methods, while using fewer rollouts.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28742:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28742:end -->

<!-- review:SF-2026-ARXIV-2605-28751:start -->
#### Extrapolative Weight Averaging Reveals Correctness-Efficiency Frontiers in Code RL

问题与 changed constraint：We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28751v1 — § exact heading: 3.4 Extrapolative weight averaging generalizes across inference settings and model scales`；Evaluation=`arXiv:2605.28751v1 — § exact heading: 4 Analysis and Perspectives`。

Trade-off / failure / fallback：`arXiv:2605.28751v1 — § exact heading: 6 Discussion and Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28751v1 — official HTML sha256=2ad8c69c8a772c3094e9868186053eb7541cc9e186faa3e4caa9f18359f26f0a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28751:start -->仅支持 exact-v1 披露机制及实验边界；不把“These results show that nested unit-test coverage in code RL induces a frontier that extrapolative weight averaging can navigate, extend, and exploit.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28751:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28751:end -->

<!-- review:SF-2026-ARXIV-2605-28760:start -->
#### LLM Zeroth-Order Fine-Tuning is an Inference Workload

问题与 changed constraint：We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.

Mechanism 与 ownership：owner=`TRAIN-LORA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28760v1 — § exact heading: 3 System Design`；Evaluation=`arXiv:2605.28760v1 — § exact heading: 4 Evaluation Setup`。

Trade-off / failure / fallback：`arXiv:2605.28760v1 — § exact heading: 7 Discussion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28760v1 — official HTML sha256=efb091acec460dba1a6d525cc918d4b70a6c230b181d97523eae8b763dbc309b; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28760:start -->仅支持 exact-v1 披露机制及实验边界；不把“We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28760:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28760:end -->

<!-- review:SF-2026-ARXIV-2605-28764:start -->
#### SwarmHarness: Skill-Based Task Routing via Decentralized Incentive-Aligned AI Agent Networks

问题与 changed constraint：We propose SwarmHarness, a decentralised protocol in which HarnessAPI skill nodes self-organise into a compute swarm without any central authority.

Mechanism 与 ownership：owner=`AGENT-MULTI-AGENT`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28764v1 — §3 SwarmNode, registry, router and credit ledger; §4 attribution`；Evaluation=`arXiv:2605.28764v1 — §5 feasibility and deployment path`。

Trade-off / failure / fallback：`arXiv:2605.28764v1 — §5.3–5.5 bootstrap, security/privacy and open challenges`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28764v1 — official exact-v1 HTML read; immutable repository/checkpoint commit Not Disclosed; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28764:start -->仅支持 exact-v1 披露机制及实验边界；不把“Beyond compute sharing, SwarmHarness is a foundational primitive for autonomous distributed AI agent networks in which agents hire compute, route subtasks, and settle credits without human intermediation.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28764:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28764:end -->

<!-- review:SF-2026-ARXIV-2605-28773:start -->
#### Rethinking Memory as Continuously Evolving Connectivity

问题与 changed constraint：To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through three stages: initial connection formation, feedback-driven refinement, and long-term consolidation.

Mechanism 与 ownership：owner=`AGENT-MEMORY`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28773v1 — § exact heading: 2 FluxMem Memory Architecture`；Evaluation=`arXiv:2605.28773v1 — § exact heading: 4 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28773v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28773v1 — official HTML sha256=d18935b37ea808d2c0daeb4cc59dd49ecae728926ce886f1b3840a91e9819065; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28773:start -->仅支持 exact-v1 披露机制及实验边界；不把“The code will be open-sourced in https://github.com/zjunlp/LightMem.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28773:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28773:end -->

<!-- review:SF-2026-ARXIV-2605-28774:start -->
#### Agent Explorative Policy Optimization for Multimodal Agentic Reasoning

问题与 changed constraint：We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection.

Mechanism 与 ownership：owner=`TRAIN-GRPO`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28774v1 — § exact heading: A.2 System Prompt and Tool Interface`；Evaluation=`arXiv:2605.28774v1 — § exact heading: 2 Analysis of RL in Agentic Reasoning`。

Trade-off / failure / fallback：`arXiv:2605.28774v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28774v1 — official HTML sha256=d13ded6dc9cb9f022fcba82d2f405dbb31ca326a1d1cbc8f2311772a26d1d576; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28774:start -->仅支持 exact-v1 披露机制及实验边界；不把“Across nine multimodal benchmarks and three scales of Qwen3-VL-Thinking, SFT+AXPO outperforms SFT+GRPO at average (+1.8pp Pass@1 and +1.8pp Pass@4 at 8B on average) and 8B with SFT+AXPO surpasses the 32B Base on Pass@4 with 4 times fewer parameters.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28774:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28774:end -->

<!-- review:SF-2026-ARXIV-2605-28778:start -->
#### Can LLMs Use Linguistic Uncertainty Markers to Reliably Reflect Intrinsic Confidence?

问题与 changed constraint：We conduct the first systematic study of this question, formalizing _marker internal confidence_ (MIC) as the estimated intrinsic confidence a model associates with a specific epistemic marker in a given task domain.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28778v1 — § exact heading: 5.3 Impact of System Prompt`；Evaluation=`arXiv:2605.28778v1 — § exact heading: 4 Experimental Setup`。

Trade-off / failure / fallback：`arXiv:2605.28778v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28778v1 — official HTML sha256=01b64c870e884d24bc10330a3d3515358d4337041ab0b0076cad2275dc758860; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28778:start -->仅支持 exact-v1 披露机制及实验边界；不把“Applying our analysis framework to diverse models and tasks, we find that LLMs remain faithfully miscalibrated even under model-centric interpretation of marker meanings, struggling to differentiate markers by internal confidence across distributions despite preserving a somewhat consistent ranking order across tasks.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28778:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28778:end -->

<!-- review:SF-2026-ARXIV-2605-28787:start -->
#### Do Data Agents Need Semantic Metadata? A Comparative Study in Agentic Data Retrieval

问题与 changed constraint：We present a comparative analysis of agentic data retrieval across two distinct environments: a Baseline Agent searching billions of open-web documents, and a Semantic Agent leveraging a corpus of 90 million datasets using schema$.$org.

Mechanism 与 ownership：owner=`AGENT-RAG`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28787v1 — § exact heading: 3 System Architecture & Experimental Setup`；Evaluation=`arXiv:2605.28787v1 — § exact heading: 4 Evaluation Methodology`。

Trade-off / failure / fallback：`arXiv:2605.28787v1 — § exact heading: 6 Discussion and Future Work`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28787v1 — official HTML sha256=4c1f63382d975afe45c1ff2cb12bd17b1fd33893d7aadc0f6e6d17130428b66a; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28787:start -->仅支持 exact-v1 披露机制及实验边界；不把“Our results reveal a clear divergence.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28787:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28787:end -->

<!-- review:SF-2026-ARXIV-2605-28803:start -->
#### HoloQ-VLA: Uniform W4A4 Quantization of Vision-Language-Action Models

问题与 changed constraint：We present HoloQ-VLA, the first training-free PTQ framework that compresses both the language backbone and the entire diffusion action head to uniform W4A4 precision without mixed-precision allocation.

Mechanism 与 ownership：owner=`MULTIMODAL-EMBODIED-VLA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28803v1 — § exact heading: 3.1 Vision Language Action (VLA) Model`；Evaluation=`arXiv:2605.28803v1 — § exact heading: 5 Experiments and Results`。

Trade-off / failure / fallback：`arXiv:2605.28803v1 — § exact heading: 6 Discussion and Analysis`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28803v1 — official HTML sha256=9cf86ee52580269d695f1b428859a43d79cc4d552873686384aa093796ecedb6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28803:start -->仅支持 exact-v1 披露机制及实验边界；不把“Real-world manipulation experiments further demonstrate that HoloQ-VLA maintains smooth and accurate control across diverse real-world scenarios.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28803:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28803:end -->

<!-- review:SF-2026-ARXIV-2605-28805:start -->
#### OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration

问题与 changed constraint：In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28805v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28805v1 — § exact heading: Appendix B Additional Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28805v1 — § exact heading: 7 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28805v1 — official HTML sha256=3c391c76b440fdc62c981dbf8764efd8db77092b07a8c527ed7c2f06c9d088c6; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28805:start -->仅支持 exact-v1 披露机制及实验边界；不把“First, symbolic verifier outputs (e.g., bounding boxes) outperform textual explanations as meta-verification rationales, enabling efficient rule-based reinforcement learning rewards while avoiding reliance on model-based rewards from auxiliary judge models.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28805:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28805:end -->

<!-- review:SF-2026-ARXIV-2605-28807:start -->
#### Calibrating Conservatism for Scalable Oversight

问题与 changed constraint：We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline.

Mechanism 与 ownership：owner=`PLATFORM-EVALUATION-SYSTEM`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28807v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28807v1 — § exact heading: 5 Experiments`。

Trade-off / failure / fallback：`arXiv:2605.28807v1 — § exact heading: 6 Conclusion`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28807v1 — official HTML sha256=fc1cea1dc0e5de404483eaaf47079402901d8349b2ea8d5133060ab680d51c22; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28807:start -->仅支持 exact-v1 披露机制及实验边界；不把“Inspired by Attainable Utility Preservation, CCO enables collective conservatism: actions face a penalty proportional to overseer concern, so high-utility actions are still selected when overseers find them unobjectionable and overridden only when concern accumulates.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28807:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28807:end -->

<!-- review:SF-2026-ARXIV-2605-28819:start -->
#### PEFT-Arena: Understanding Parameter-Efficient Finetuning from a Stability-Plasticity Perspective

问题与 changed constraint：We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention.

Mechanism 与 ownership：owner=`TRAIN-LORA`；该 family 改变的是该 owner 的 state/control/evidence boundary，而非只因主题相关被保留。

Evaluation contract：Method=`arXiv:2605.28819v1 — § exact heading: 1 Introduction`；Evaluation=`arXiv:2605.28819v1 — § exact heading: 2 The PEFT-Arena Benchmark`。

Trade-off / failure / fallback：`arXiv:2605.28819v1 — § exact heading: Limitations`；超出 v1 披露范围时回退当前 owner 已验证路径。Artifact=`arXiv:2605.28819v1 — official HTML sha256=8e6e8e4418944fbd589b91d7ddf5befba422f816d98e2de9b6ebcc57deeed7e3; immutable repository/checkpoint commit Not Disclosed unless named in v1`。

<!-- claim:SF-2026-ARXIV-2605-28819:start -->仅支持 exact-v1 披露机制及实验边界；不把“In activation space, retention metrics show whether finetuning preserves or distorts general-capability representations, with forgetting linked to non-isometric representation distortion.”外推为跨模型、硬件、数据分布或生产 SLO 保证。 未披露的 model、hardware、precision、length、batch、concurrency、evaluator 与 SLO 均记 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-28819:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-28819:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27390 | exact-v1 evaluation for EvoSpec: Evolving Speculative Decoding via Real-Time Vocabulary and Parameter Adaptation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper authors |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27390 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27390 |
| SF-2026-ARXIV-2605-27428 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27428 |
| SF-2026-ARXIV-2605-27432 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27432 |
| SF-2026-ARXIV-2605-27435 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27435 |
| SF-2026-ARXIV-2605-27437 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27437 |
| SF-2026-ARXIV-2605-27461 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27461 |
| SF-2026-ARXIV-2605-27466 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27466 |
| SF-2026-ARXIV-2605-27480 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27480 |
| SF-2026-ARXIV-2605-27483 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27483 |
| SF-2026-ARXIV-2605-27488 | score_7_9;forced_review | selected | DA-20260528-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260528-01 |
| SF-2026-ARXIV-2605-27489 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27489 |
| SF-2026-ARXIV-2605-27491 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27491 |
| SF-2026-ARXIV-2605-27492 | score_7_9;forced_review | selected | DA-20260528-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260528-02 |
| SF-2026-ARXIV-2605-27494 | score_7_9;forced_review;potential_books_delta | selected | DA-20260528-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260528-03 |
| SF-2026-ARXIV-2605-27547 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27547 |
| SF-2026-ARXIV-2605-27559 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27559 |
| SF-2026-ARXIV-2605-27566 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27566 |
| SF-2026-ARXIV-2605-27569 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27569 |
| SF-2026-ARXIV-2605-27575 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27575 |
| SF-2026-ARXIV-2605-27589 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27589 |
| SF-2026-ARXIV-2605-27599 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27599 |
| SF-2026-ARXIV-2605-27621 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27621 |
| SF-2026-ARXIV-2605-27630 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27630 |
| SF-2026-ARXIV-2605-27668 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27668 |
| SF-2026-ARXIV-2605-27671 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27671 |
| SF-2026-ARXIV-2605-27678 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27678 |
| SF-2026-ARXIV-2605-27681 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27681 |
| SF-2026-ARXIV-2605-27690 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27690 |
| SF-2026-ARXIV-2605-27710 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27710 |
| SF-2026-ARXIV-2605-27712 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27712 |
| SF-2026-ARXIV-2605-27720 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27720 |
| SF-2026-ARXIV-2605-27744 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27744 |
| SF-2026-ARXIV-2605-27752 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27752 |
| SF-2026-ARXIV-2605-27759 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27759 |
| SF-2026-ARXIV-2605-27760 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27760 |
| SF-2026-ARXIV-2605-27761 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27761 |
| SF-2026-ARXIV-2605-27763 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27763 |
| SF-2026-ARXIV-2605-27766 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27766 |
| SF-2026-ARXIV-2605-27784 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27784 |
| SF-2026-ARXIV-2605-27785 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27785 |
| SF-2026-ARXIV-2605-27789 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27789 |
| SF-2026-ARXIV-2605-27820 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27820 |
| SF-2026-ARXIV-2605-27825 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27825 |
| SF-2026-ARXIV-2605-27850 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27850 |
| SF-2026-ARXIV-2605-27879 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27879 |
| SF-2026-ARXIV-2605-27881 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27881 |
| SF-2026-ARXIV-2605-27898 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27898 |
| SF-2026-ARXIV-2605-27899 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27899 |
| SF-2026-ARXIV-2605-27901 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27901 |
| SF-2026-ARXIV-2605-27918 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27918 |
| SF-2026-ARXIV-2605-27922 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27922 |
| SF-2026-ARXIV-2605-27947 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27947 |
| SF-2026-ARXIV-2605-27954 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27954 |
| SF-2026-ARXIV-2605-27957 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27957 |
| SF-2026-ARXIV-2605-27963 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27963 |
| SF-2026-ARXIV-2605-27980 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27980 |
| SF-2026-ARXIV-2605-27995 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-27995 |
| SF-2026-ARXIV-2605-28000 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28000 |
| SF-2026-ARXIV-2605-28009 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28009 |
| SF-2026-ARXIV-2605-28017 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28017 |
| SF-2026-ARXIV-2605-28044 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28044 |
| SF-2026-ARXIV-2605-28046 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28046 |
| SF-2026-ARXIV-2605-28053 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28053 |
| SF-2026-ARXIV-2605-28071 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28071 |
| SF-2026-ARXIV-2605-28074 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28074 |
| SF-2026-ARXIV-2605-28083 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28083 |
| SF-2026-ARXIV-2605-28095 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28095 |
| SF-2026-ARXIV-2605-28097 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28097 |
| SF-2026-ARXIV-2605-28108 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28108 |
| SF-2026-ARXIV-2605-28112 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28112 |
| SF-2026-ARXIV-2605-28116 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28116 |
| SF-2026-ARXIV-2605-28122 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28122 |
| SF-2026-ARXIV-2605-28158 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28158 |
| SF-2026-ARXIV-2605-28201 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28201 |
| SF-2026-ARXIV-2605-28213 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28213 |
| SF-2026-ARXIV-2605-28214 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28214 |
| SF-2026-ARXIV-2605-28224 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28224 |
| SF-2026-ARXIV-2605-28282 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28282 |
| SF-2026-ARXIV-2605-28302 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28302 |
| SF-2026-ARXIV-2605-28354 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28354 |
| SF-2026-ARXIV-2605-28371 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28371 |
| SF-2026-ARXIV-2605-28384 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28384 |
| SF-2026-ARXIV-2605-28390 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28390 |
| SF-2026-ARXIV-2605-28424 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28424 |
| SF-2026-ARXIV-2605-28433 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28433 |
| SF-2026-ARXIV-2605-28467 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28467 |
| SF-2026-ARXIV-2605-28480 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28480 |
| SF-2026-ARXIV-2605-28508 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28508 |
| SF-2026-ARXIV-2605-28510 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28510 |
| SF-2026-ARXIV-2605-28544 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28544 |
| SF-2026-ARXIV-2605-28561 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28561 |
| SF-2026-ARXIV-2605-28565 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28565 |
| SF-2026-ARXIV-2605-28573 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28573 |
| SF-2026-ARXIV-2605-28617 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28617 |
| SF-2026-ARXIV-2605-28632 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28632 |
| SF-2026-ARXIV-2605-28634 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28634 |
| SF-2026-ARXIV-2605-28640 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28640 |
| SF-2026-ARXIV-2605-28646 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28646 |
| SF-2026-ARXIV-2605-28678 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28678 |
| SF-2026-ARXIV-2605-28691 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28691 |
| SF-2026-ARXIV-2605-28699 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28699 |
| SF-2026-ARXIV-2605-28704 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28704 |
| SF-2026-ARXIV-2605-28721 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28721 |
| SF-2026-ARXIV-2605-28726 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28726 |
| SF-2026-ARXIV-2605-28732 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28732 |
| SF-2026-ARXIV-2605-28742 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28742 |
| SF-2026-ARXIV-2605-28751 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28751 |
| SF-2026-ARXIV-2605-28760 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28760 |
| SF-2026-ARXIV-2605-28764 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28764 |
| SF-2026-ARXIV-2605-28773 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28773 |
| SF-2026-ARXIV-2605-28774 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28774 |
| SF-2026-ARXIV-2605-28778 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28778 |
| SF-2026-ARXIV-2605-28787 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28787 |
| SF-2026-ARXIV-2605-28803 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28803 |
| SF-2026-ARXIV-2605-28805 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28805 |
| SF-2026-ARXIV-2605-28807 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28807 |
| SF-2026-ARXIV-2605-28819 | score_7_9 | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2605-28819 |

<!-- analysis-decision:SF-2026-ARXIV-2605-27390:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27390:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27428:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27428:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27432:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27432:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27435:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27435:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27437:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27437:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27461:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27461:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27466:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27466:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27480:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27480:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27483:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27483:end -->

<!-- analysis:DA-20260528-01:start -->
### Deep Analysis — SF-2026-ARXIV-2605-27488

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260528-01:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27489:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27489:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27491:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27491:end -->

<!-- analysis:DA-20260528-02:start -->
### Deep Analysis — SF-2026-ARXIV-2605-27492

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260528-02:end -->

<!-- analysis:DA-20260528-03:start -->
### Deep Analysis — SF-2026-ARXIV-2605-27494

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260528-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27547:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27547:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27559:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27559:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27566:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27569:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27569:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27575:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27575:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27589:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27589:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27599:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27599:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27621:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27630:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27630:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27668:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27668:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27671:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27671:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27678:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27681:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27681:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27690:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27690:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27710:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27710:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27712:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27720:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27720:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27744:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27744:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27752:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27759:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27759:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27760:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27761:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27761:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27763:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27763:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27766:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27766:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27784:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27784:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27785:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27785:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27789:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27789:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27820:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27820:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27825:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27825:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27850:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27850:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27879:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27879:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27881:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27881:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27898:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27898:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27899:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27901:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27901:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27918:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27922:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27922:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27947:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27947:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27954:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27954:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27957:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27963:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27963:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27980:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27980:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-27995:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-27995:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28000:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28000:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28009:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28009:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28017:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28017:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28044:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28044:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28046:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28046:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28053:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28053:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28071:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28074:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28074:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28083:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28083:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28095:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28095:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28097:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28097:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28108:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28108:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28112:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28112:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28116:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28116:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28122:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28122:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28158:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28158:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28201:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28201:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28213:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28213:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28214:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28214:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28224:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28224:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28282:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28282:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28302:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28302:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28354:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28354:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28371:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28371:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28384:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28384:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28390:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28390:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28424:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28424:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28433:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28467:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28480:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28480:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28508:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28508:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28510:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28510:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28544:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28544:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28561:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28561:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28565:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28565:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28573:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28573:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28617:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28617:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28632:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28632:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28634:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28640:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28640:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28646:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28646:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28678:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28691:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28691:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28699:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28699:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28704:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28721:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28721:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28726:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28726:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28732:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28732:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28742:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28742:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28751:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28751:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28760:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28764:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28764:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28773:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28773:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28774:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28778:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28778:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28787:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28787:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28803:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28803:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28805:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28805:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28807:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28807:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-28819:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2605-28819:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-27390 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L196 (H2: Verify Length 不是孤立的固定超参数) | books/part-05-inference-system/47-pagedattention.md#L10 (H2: 本章要回答的问题); books/part-05-inference-system/49-tensorrt-llm.md#L10 (H2: 本章要回答的问题) | existing:SF-2026-ARXIV-2605-27390 | delta:SF-2026-ARXIV-2605-27390 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27390 |
| SF-2026-ARXIV-2605-27428 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-27428 | delta:SF-2026-ARXIV-2605-27428 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27428 |
| SF-2026-ARXIV-2605-27432 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-27432 | delta:SF-2026-ARXIV-2605-27432 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27432 |
| SF-2026-ARXIV-2605-27435 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-27435 | delta:SF-2026-ARXIV-2605-27435 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27435 |
| SF-2026-ARXIV-2605-27437 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-27437 | delta:SF-2026-ARXIV-2605-27437 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27437 |
| SF-2026-ARXIV-2605-27461 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-27461 | delta:SF-2026-ARXIV-2605-27461 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27461 |
| SF-2026-ARXIV-2605-27466 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27466 | delta:SF-2026-ARXIV-2605-27466 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27466 |
| SF-2026-ARXIV-2605-27480 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-27480 | delta:SF-2026-ARXIV-2605-27480 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27480 |
| SF-2026-ARXIV-2605-27483 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27483 | delta:SF-2026-ARXIV-2605-27483 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27483 |
| SF-2026-ARXIV-2605-27488 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27488 | delta:SF-2026-ARXIV-2605-27488 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27488 |
| SF-2026-ARXIV-2605-27489 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27489 | delta:SF-2026-ARXIV-2605-27489 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27489 |
| SF-2026-ARXIV-2605-27491 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-27491 | delta:SF-2026-ARXIV-2605-27491 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27491 |
| SF-2026-ARXIV-2605-27492 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27492 | delta:SF-2026-ARXIV-2605-27492 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27492 |
| SF-2026-ARXIV-2605-27494 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-27494 | delta:SF-2026-ARXIV-2605-27494 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27494 |
| SF-2026-ARXIV-2605-27547 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27547 | delta:SF-2026-ARXIV-2605-27547 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27547 |
| SF-2026-ARXIV-2605-27559 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79; books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-27559 | delta:SF-2026-ARXIV-2605-27559 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27559 |
| SF-2026-ARXIV-2605-27569 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27569 | delta:SF-2026-ARXIV-2605-27569 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27569 |
| SF-2026-ARXIV-2605-27575 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27575 | delta:SF-2026-ARXIV-2605-27575 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27575 |
| SF-2026-ARXIV-2605-27589 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-27589 | delta:SF-2026-ARXIV-2605-27589 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27589 |
| SF-2026-ARXIV-2605-27599 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-27599 | delta:SF-2026-ARXIV-2605-27599 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27599 |
| SF-2026-ARXIV-2605-27621 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27621 | delta:SF-2026-ARXIV-2605-27621 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27621 |
| SF-2026-ARXIV-2605-27630 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79; books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-27630 | delta:SF-2026-ARXIV-2605-27630 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27630 |
| SF-2026-ARXIV-2605-27668 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27668 | delta:SF-2026-ARXIV-2605-27668 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27668 |
| SF-2026-ARXIV-2605-27671 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-27671 | delta:SF-2026-ARXIV-2605-27671 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27671 |
| SF-2026-ARXIV-2605-27678 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/37-tensor-parallel.md#chapter-37; books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | existing:SF-2026-ARXIV-2605-27678 | delta:SF-2026-ARXIV-2605-27678 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27678 |
| SF-2026-ARXIV-2605-27681 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27681 | delta:SF-2026-ARXIV-2605-27681 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27681 |
| SF-2026-ARXIV-2605-27690 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27690 | delta:SF-2026-ARXIV-2605-27690 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27690 |
| SF-2026-ARXIV-2605-27710 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27710 | delta:SF-2026-ARXIV-2605-27710 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27710 |
| SF-2026-ARXIV-2605-27712 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27712 | delta:SF-2026-ARXIV-2605-27712 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27712 |
| SF-2026-ARXIV-2605-27720 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27720 | delta:SF-2026-ARXIV-2605-27720 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27720 |
| SF-2026-ARXIV-2605-27744 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27744 | delta:SF-2026-ARXIV-2605-27744 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27744 |
| SF-2026-ARXIV-2605-27752 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27752 | delta:SF-2026-ARXIV-2605-27752 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27752 |
| SF-2026-ARXIV-2605-27759 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27759 | delta:SF-2026-ARXIV-2605-27759 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27759 |
| SF-2026-ARXIV-2605-27760 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27760 | delta:SF-2026-ARXIV-2605-27760 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27760 |
| SF-2026-ARXIV-2605-27761 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27761 | delta:SF-2026-ARXIV-2605-27761 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27761 |
| SF-2026-ARXIV-2605-27763 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27763 | delta:SF-2026-ARXIV-2605-27763 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27763 |
| SF-2026-ARXIV-2605-27766 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27766 | delta:SF-2026-ARXIV-2605-27766 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27766 |
| SF-2026-ARXIV-2605-27784 | AGENT-PROMPT | books/part-07-agent/74-prompt.md#chapter-74 | books/part-07-agent/75-context.md#chapter-75 | existing:SF-2026-ARXIV-2605-27784 | delta:SF-2026-ARXIV-2605-27784 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27784 |
| SF-2026-ARXIV-2605-27785 | PLATFORM-LOGGING | books/part-06-ai-infrastructure/68-logging.md#chapter-68 | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67; books/part-06-ai-infrastructure/69-trace.md#chapter-69 | existing:SF-2026-ARXIV-2605-27785 | delta:SF-2026-ARXIV-2605-27785 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27785 |
| SF-2026-ARXIV-2605-27789 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27789 | delta:SF-2026-ARXIV-2605-27789 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-27789 |
| SF-2026-ARXIV-2605-27820 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27820 | delta:SF-2026-ARXIV-2605-27820 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27820 |
| SF-2026-ARXIV-2605-27825 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27825 | delta:SF-2026-ARXIV-2605-27825 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-27825 |
| SF-2026-ARXIV-2605-27850 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-27850 | delta:SF-2026-ARXIV-2605-27850 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27850 |
| SF-2026-ARXIV-2605-27879 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27879 | delta:SF-2026-ARXIV-2605-27879 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27879 |
| SF-2026-ARXIV-2605-27881 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26;books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-27881 | delta:SF-2026-ARXIV-2605-27881 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27881 |
| SF-2026-ARXIV-2605-27898 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27898 | delta:SF-2026-ARXIV-2605-27898 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27898 |
| SF-2026-ARXIV-2605-27899 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-27899 | delta:SF-2026-ARXIV-2605-27899 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27899 |
| SF-2026-ARXIV-2605-27901 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-27901 | delta:SF-2026-ARXIV-2605-27901 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27901 |
| SF-2026-ARXIV-2605-27918 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-27918 | delta:SF-2026-ARXIV-2605-27918 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27918 |
| SF-2026-ARXIV-2605-27922 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27922 | delta:SF-2026-ARXIV-2605-27922 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27922 |
| SF-2026-ARXIV-2605-27947 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-27947 | delta:SF-2026-ARXIV-2605-27947 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27947 |
| SF-2026-ARXIV-2605-27954 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-27954 | delta:SF-2026-ARXIV-2605-27954 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27954 |
| SF-2026-ARXIV-2605-27957 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27957 | delta:SF-2026-ARXIV-2605-27957 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27957 |
| SF-2026-ARXIV-2605-27963 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-27963 | delta:SF-2026-ARXIV-2605-27963 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27963 |
| SF-2026-ARXIV-2605-27980 | MODEL-POSITION-ENCODING | books/part-02-model/13-position-encoding.md#chapter-13 | books/part-02-model/12-embedding.md#chapter-12;books/part-02-model/14-self-attention.md#chapter-14 | existing:SF-2026-ARXIV-2605-27980 | delta:SF-2026-ARXIV-2605-27980 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27980 |
| SF-2026-ARXIV-2605-27995 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-27995 | delta:SF-2026-ARXIV-2605-27995 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27995 |
| SF-2026-ARXIV-2605-28000 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28000 | delta:SF-2026-ARXIV-2605-28000 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28000 |
| SF-2026-ARXIV-2605-28009 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28009 | delta:SF-2026-ARXIV-2605-28009 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28009 |
| SF-2026-ARXIV-2605-28017 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28017 | delta:SF-2026-ARXIV-2605-28017 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28017 |
| SF-2026-ARXIV-2605-28044 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28044 | delta:SF-2026-ARXIV-2605-28044 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28044 |
| SF-2026-ARXIV-2605-28046 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28046 | delta:SF-2026-ARXIV-2605-28046 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28046 |
| SF-2026-ARXIV-2605-28053 | INFER-CONTINUOUS-BATCHING | books/part-05-inference-system/46-continuous-batching.md#chapter-46 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45;books/part-05-inference-system/47-pagedattention.md#chapter-47 | existing:SF-2026-ARXIV-2605-28053 | delta:SF-2026-ARXIV-2605-28053 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28053 |
| SF-2026-ARXIV-2605-28071 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28071 | delta:SF-2026-ARXIV-2605-28071 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28071 |
| SF-2026-ARXIV-2605-28074 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28074 | delta:SF-2026-ARXIV-2605-28074 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28074 |
| SF-2026-ARXIV-2605-28083 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28083 | delta:SF-2026-ARXIV-2605-28083 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28083 |
| SF-2026-ARXIV-2605-28095 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#chapter-54 | books/part-05-inference-system/53-kserve-llm.md#chapter-53;books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-28095 | delta:SF-2026-ARXIV-2605-28095 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28095 |
| SF-2026-ARXIV-2605-28097 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | books/part-06-ai-infrastructure/72-security.md#chapter-72;books/part-07-agent/74-prompt.md#chapter-74 | existing:SF-2026-ARXIV-2605-28097 | delta:SF-2026-ARXIV-2605-28097 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28097 |
| SF-2026-ARXIV-2605-28108 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-28108 | delta:SF-2026-ARXIV-2605-28108 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28108 |
| SF-2026-ARXIV-2605-28112 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28112 | delta:SF-2026-ARXIV-2605-28112 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28112 |
| SF-2026-ARXIV-2605-28116 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28116 | delta:SF-2026-ARXIV-2605-28116 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28116 |
| SF-2026-ARXIV-2605-28122 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28122 | delta:SF-2026-ARXIV-2605-28122 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28122 |
| SF-2026-ARXIV-2605-28158 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28158 | delta:SF-2026-ARXIV-2605-28158 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28158 |
| SF-2026-ARXIV-2605-28201 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28201 | delta:SF-2026-ARXIV-2605-28201 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28201 |
| SF-2026-ARXIV-2605-28213 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28213 | delta:SF-2026-ARXIV-2605-28213 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28213 |
| SF-2026-ARXIV-2605-28214 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28214 | delta:SF-2026-ARXIV-2605-28214 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28214 |
| SF-2026-ARXIV-2605-28224 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28224 | delta:SF-2026-ARXIV-2605-28224 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28224 |
| SF-2026-ARXIV-2605-28282 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-28282 | delta:SF-2026-ARXIV-2605-28282 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28282 |
| SF-2026-ARXIV-2605-28302 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | books/part-05-inference-system/54-gpu-memory.md#chapter-54;books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | existing:SF-2026-ARXIV-2605-28302 | delta:SF-2026-ARXIV-2605-28302 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28302 |
| SF-2026-ARXIV-2605-28354 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-28354 | delta:SF-2026-ARXIV-2605-28354 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28354 |
| SF-2026-ARXIV-2605-28371 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28371 | delta:SF-2026-ARXIV-2605-28371 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28371 |
| SF-2026-ARXIV-2605-28384 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-06-ai-infrastructure/57-what-is-ai-platform.md#chapter-57 | existing:SF-2026-ARXIV-2605-28384 | delta:SF-2026-ARXIV-2605-28384 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28384 |
| SF-2026-ARXIV-2605-28390 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28390 | delta:SF-2026-ARXIV-2605-28390 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28390 |
| SF-2026-ARXIV-2605-28424 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28424 | delta:SF-2026-ARXIV-2605-28424 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28424 |
| SF-2026-ARXIV-2605-28433 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28433 | delta:SF-2026-ARXIV-2605-28433 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28433 |
| SF-2026-ARXIV-2605-28467 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28467 | delta:SF-2026-ARXIV-2605-28467 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28467 |
| SF-2026-ARXIV-2605-28480 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-28480 | delta:SF-2026-ARXIV-2605-28480 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28480 |
| SF-2026-ARXIV-2605-28508 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28508 | delta:SF-2026-ARXIV-2605-28508 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28508 |
| SF-2026-ARXIV-2605-28510 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28510 | delta:SF-2026-ARXIV-2605-28510 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28510 |
| SF-2026-ARXIV-2605-28544 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-28544 | delta:SF-2026-ARXIV-2605-28544 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28544 |
| SF-2026-ARXIV-2605-28561 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-28561 | delta:SF-2026-ARXIV-2605-28561 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28561 |
| SF-2026-ARXIV-2605-28565 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28565 | delta:SF-2026-ARXIV-2605-28565 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28565 |
| SF-2026-ARXIV-2605-28573 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-28573 | delta:SF-2026-ARXIV-2605-28573 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28573 |
| SF-2026-ARXIV-2605-28617 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-28617 | delta:SF-2026-ARXIV-2605-28617 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28617 |
| SF-2026-ARXIV-2605-28632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28632 | delta:SF-2026-ARXIV-2605-28632 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28632 |
| SF-2026-ARXIV-2605-28634 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28634 | delta:SF-2026-ARXIV-2605-28634 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28634 |
| SF-2026-ARXIV-2605-28640 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-28640 | delta:SF-2026-ARXIV-2605-28640 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28640 |
| SF-2026-ARXIV-2605-28646 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-28646 | delta:SF-2026-ARXIV-2605-28646 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28646 |
| SF-2026-ARXIV-2605-28678 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47;books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-28678 | delta:SF-2026-ARXIV-2605-28678 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28678 |
| SF-2026-ARXIV-2605-28691 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-28691 | delta:SF-2026-ARXIV-2605-28691 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28691 |
| SF-2026-ARXIV-2605-28699 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28699 | delta:SF-2026-ARXIV-2605-28699 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28699 |
| SF-2026-ARXIV-2605-28704 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-28704 | delta:SF-2026-ARXIV-2605-28704 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28704 |
| SF-2026-ARXIV-2605-28721 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28721 | delta:SF-2026-ARXIV-2605-28721 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28721 |
| SF-2026-ARXIV-2605-28726 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28726 | delta:SF-2026-ARXIV-2605-28726 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28726 |
| SF-2026-ARXIV-2605-28732 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28732 | delta:SF-2026-ARXIV-2605-28732 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28732 |
| SF-2026-ARXIV-2605-28742 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79;books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-28742 | delta:SF-2026-ARXIV-2605-28742 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28742 |
| SF-2026-ARXIV-2605-28751 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28751 | delta:SF-2026-ARXIV-2605-28751 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28751 |
| SF-2026-ARXIV-2605-28760 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-28760 | delta:SF-2026-ARXIV-2605-28760 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-28760 |
| SF-2026-ARXIV-2605-28764 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-28764 | delta:SF-2026-ARXIV-2605-28764 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28764 |
| SF-2026-ARXIV-2605-28773 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-28773 | delta:SF-2026-ARXIV-2605-28773 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28773 |
| SF-2026-ARXIV-2605-28774 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32;books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-28774 | delta:SF-2026-ARXIV-2605-28774 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28774 |
| SF-2026-ARXIV-2605-28778 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28778 | delta:SF-2026-ARXIV-2605-28778 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28778 |
| SF-2026-ARXIV-2605-28787 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-28787 | delta:SF-2026-ARXIV-2605-28787 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28787 |
| SF-2026-ARXIV-2605-28803 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-04-training-system/27-data.md#chapter-27 | existing:SF-2026-ARXIV-2605-28803 | delta:SF-2026-ARXIV-2605-28803 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28803 |
| SF-2026-ARXIV-2605-28805 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28805 | delta:SF-2026-ARXIV-2605-28805 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28805 |
| SF-2026-ARXIV-2605-28807 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-28807 | delta:SF-2026-ARXIV-2605-28807 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28807 |
| SF-2026-ARXIV-2605-28819 | TRAIN-LORA | books/part-04-training-system/30-lora.md#chapter-30 | books/part-04-training-system/29-sft.md#chapter-29;books/part-04-training-system/31-rlhf.md#chapter-31 | existing:SF-2026-ARXIV-2605-28819 | delta:SF-2026-ARXIV-2605-28819 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-28819 |

<!-- books-review:SF-2026-ARXIV-2605-27390:start -->
<!-- existing:SF-2026-ARXIV-2605-27390:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L196 (H2: Verify Length 不是孤立的固定超参数)` 及相邻章节后，现有命题为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。** 目标小节已经拥有该 family 所需的长期 owner 与旧路径/约束边界。<!-- existing:SF-2026-ARXIV-2605-27390:end -->
<!-- delta:SF-2026-ARXIV-2605-27390:start -->Exact-v1 的 source-specific delta 是：We introduce EvoSpec, which jointly adapts the active vocabulary and lightweight draft parameters from verification feedback. 其证据边界为：Evidence is author-reported exact-v1 mechanism/evaluation evidence. It does not establish cross-model, cross-hardware, cross-workload or production generality unless those conditions are explicitly named above. 该实现或实验没有改变当前章节已经成立的长期机制，不把作者 benchmark 外推为通用结论。<!-- delta:SF-2026-ARXIV-2605-27390:end -->
Decision: `No Change — Existing Coverage`; reviewer=fresh-context:apr-may-books-20260903。
<!-- books-review:SF-2026-ARXIV-2605-27390:end -->

<!-- existing:SF-2026-ARXIV-2605-27428:start -->已顺读 owner 与相邻章；owner 主干=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源', 'Iteration Scheduling', 'Physical AI 把 Execution Horizon 变成调度状态', 'Routing、Placement 与 Autoscaling', 'Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer']；exact marker=absent。Review notes 不计机制整合。<!-- existing:SF-2026-ARXIV-2605-27428:end -->
<!-- delta:SF-2026-ARXIV-2605-27428:start -->Edge deployments of generative inference increasingly face two practical realities: per-device per-model performance is often unknown at deployment time, and it is non-stationary due to user-driven semantic events, background load, and device churn.<!-- delta:SF-2026-ARXIV-2605-27428:end -->
<!-- books-review:SF-2026-ARXIV-2605-27428:start -->owner=`INFER-SCHEDULING`；decision=`No Change — Existing Coverage`；已顺读 target 与 adjacent，marker match 不替代正文比较。<!-- books-review:SF-2026-ARXIV-2605-27428:end -->

<!-- books-review:SF-2026-ARXIV-2605-27432:start -->
<!-- existing:SF-2026-ARXIV-2605-27432:start -->正文已覆盖 distributed corpus ownership、retrieval admission、privacy/security、escalation 与 evidence provenance。 本 family 的具体机制 `We propose FD-RAG, a federated dual-system RAG framework that decouples lightweight memory access from on-demand LLM reasoning for decentralized deployment.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-27432:end -->
<!-- delta:SF-2026-ARXIV-2605-27432:start -->We propose FD-RAG, a federated dual-system RAG framework that decouples lightweight memory access from on-demand LLM reasoning for decentralized deployment.<!-- delta:SF-2026-ARXIV-2605-27432:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83。
<!-- books-review:SF-2026-ARXIV-2605-27432:end -->

<!-- books-review:SF-2026-ARXIV-2605-27435:start -->
<!-- existing:SF-2026-ARXIV-2605-27435:start -->正文已把 backend lowering、heterogeneous execution、kernel correctness 与 device fallback 放在同一执行计划中。 本 family 的具体机制 `Deploying large language models (LLMs) on mobile devices increasingly relies on heterogeneous execution, yet no prior study has systematically characterized NPU effectiveness at the operator and pipeline level.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-27435:end -->
<!-- delta:SF-2026-ARXIV-2605-27435:start -->Deploying large language models (LLMs) on mobile devices increasingly relies on heterogeneous execution, yet no prior study has systematically characterized NPU effectiveness at the operator and pipeline level.<!-- delta:SF-2026-ARXIV-2605-27435:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4c19b842b8e2ddb31cc4681c31e5484defce4f9769950473cc31a5afa61e338a。
<!-- books-review:SF-2026-ARXIV-2605-27435:end -->

<!-- books-review:SF-2026-ARXIV-2605-27437:start -->
<!-- existing:SF-2026-ARXIV-2605-27437:start -->正文已覆盖 memory write/read、reflective retrieval、provenance、rollback 与 lifecycle evaluation。 本 family 的具体机制 `Although recent methods introduce reflection into retrieval, their retrieval paths are generated by the LLM from limited evidence, leading to unstable retrieval and additional latency overhead.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-27437:end -->
<!-- delta:SF-2026-ARXIV-2605-27437:start -->Although recent methods introduce reflection into retrieval, their retrieval paths are generated by the LLM from limited evidence, leading to unstable retrieval and additional latency overhead.<!-- delta:SF-2026-ARXIV-2605-27437:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=f09fd5d839379ade75d2834c66aa9ce5c2eb4b2acac0e2773be3054d41222be0。
<!-- books-review:SF-2026-ARXIV-2605-27437:end -->

<!-- books-review:SF-2026-ARXIV-2605-27461:start -->
<!-- existing:SF-2026-ARXIV-2605-27461:start -->已顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-03-multimodal-world-models/README.md']；当前主干=['本章要回答的问题', '约束为何从 VLM 到 VLA 发生变化', '坐标系归一化是 Representation 到 Action Schema 的桥', '闭环主干', '从模块化机器人到 VLA', '传统模块化系统', 'VLM-conditioned controller', 'VLA policy']；exact family marker=absent。Review notes 不计语义整合。<!-- existing:SF-2026-ARXIV-2605-27461:end -->
<!-- delta:SF-2026-ARXIV-2605-27461:start -->We present a deployment study of an industrial packaging task at Siemens Factory (GWE, Erlangen, Germany), where a robot must pick a transparent accessory bag from a cluttered pile, insert it into the remaining cavity of a cardboard package, and ensure that the bag and its contents remain below the closing plane.<!-- delta:SF-2026-ARXIV-2605-27461:end --> Author decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-27461:end -->

<!-- books-review:SF-2026-ARXIV-2605-27466:start -->
<!-- existing:SF-2026-ARXIV-2605-27466:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前命题：本章拥有多 Agent 的角色、消息、协作拓扑与贡献/风险边界，不把多个独立调用误作协调系统；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=50c6c9beefaa32eb4dbe1f6c66bdafd38299e1995282ee814bfee0d53491f05c。<!-- existing:SF-2026-ARXIV-2605-27466:end -->
<!-- delta:SF-2026-ARXIV-2605-27466:start -->multi-agent coordination is represented as an auditable policy graph over skills, models and topology with reward robustness as a first-class control-plane concern<!-- delta:SF-2026-ARXIV-2605-27466:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27466:end -->

<!-- books-review:SF-2026-ARXIV-2605-27480:start -->
<!-- existing:SF-2026-ARXIV-2605-27480:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=a1687d6e4cb81a17e4f7f408c6444c575cc87d33f8e364c8baca5e2d2da6e361。<!-- existing:SF-2026-ARXIV-2605-27480:end -->
<!-- delta:SF-2026-ARXIV-2605-27480:start -->serving externality accounting needs a functional unit and quality-aware biodiversity impact identity, because carbon and water metrics do not proxy every lifecycle impact<!-- delta:SF-2026-ARXIV-2605-27480:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27480:end -->

<!-- books-review:SF-2026-ARXIV-2605-27483:start -->
<!-- existing:SF-2026-ARXIV-2605-27483:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27483:end -->
<!-- delta:SF-2026-ARXIV-2605-27483:start -->debate is an evaluation treatment that can reduce weak-judge over-endorsement only when the critic supplies usable evidence; judge family and prompt remain part of identity<!-- delta:SF-2026-ARXIV-2605-27483:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27483:end -->

<!-- books-review:SF-2026-ARXIV-2605-27488:start -->
<!-- existing:SF-2026-ARXIV-2605-27488:start -->Ch72 已覆盖 OS/eBPF enforcement、attestation 与 runtime boundary；论文平台实现不改变长期安全 owner。 owner_sha256=8d84c9f26ab04bab104ed93d45a226305008a7bb73f8afcba0b6271b14db0647。<!-- existing:SF-2026-ARXIV-2605-27488:end -->
<!-- delta:SF-2026-ARXIV-2605-27488:start -->agent trust enforcement moves below application code into eBPF-mediated, channel-attested communication.<!-- delta:SF-2026-ARXIV-2605-27488:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27488:end -->

<!-- books-review:SF-2026-ARXIV-2605-27489:start -->
<!-- existing:SF-2026-ARXIV-2605-27489:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27489:end -->
<!-- delta:SF-2026-ARXIV-2605-27489:start -->multi-agent safety evaluation must measure interaction-driven harm amplification rather than extrapolate isolated-agent scores<!-- delta:SF-2026-ARXIV-2605-27489:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27489:end -->

<!-- books-review:SF-2026-ARXIV-2605-27491:start -->
<!-- existing:SF-2026-ARXIV-2605-27491:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前命题：本章拥有 action-conditioned transition、latent dynamics、imagined rollout 与可修订 world state；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-27491:end -->
<!-- delta:SF-2026-ARXIV-2605-27491:start -->a closed-loop world simulator binds action-conditioned video, proprioceptive state, world-judge reward and downstream policy consistency instead of video quality alone<!-- delta:SF-2026-ARXIV-2605-27491:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27491:end -->

<!-- books-review:SF-2026-ARXIV-2605-27492:start -->
<!-- existing:SF-2026-ARXIV-2605-27492:start -->Ch66 已把 trajectory/component receipts 与 run identity 用于区分 upstream cascade 和 downstream capability；本 family 作为评测证据保留，不重复写书。 owner_sha256=dcd5bd0656e8d1a39e0b368962d14794d9ac1659d1f3a83dff267a67788b200a。<!-- existing:SF-2026-ARXIV-2605-27492:end -->
<!-- delta:SF-2026-ARXIV-2605-27492:start -->production agent assessment preserves runtime state and uses resurrection artifacts to separate upstream cascade from downstream capability.<!-- delta:SF-2026-ARXIV-2605-27492:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27492:end -->

<!-- books-review:SF-2026-ARXIV-2605-27494:start -->
<!-- existing:SF-2026-ARXIV-2605-27494:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=87e328782912c590e2ce992aebd3701a601c7a9d63a696f24048ad9d78f81c27。<!-- existing:SF-2026-ARXIV-2605-27494:end -->
<!-- delta:SF-2026-ARXIV-2605-27494:start -->answer-cache reuse is committed only against fresh evidence identity, version and support, with regeneration as fallback.<!-- delta:SF-2026-ARXIV-2605-27494:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27494:end -->

<!-- books-review:SF-2026-ARXIV-2605-27547:start -->
<!-- existing:SF-2026-ARXIV-2605-27547:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前命题：本章拥有多 Agent 的角色、消息、协作拓扑与贡献/风险边界，不把多个独立调用误作协调系统；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=50c6c9beefaa32eb4dbe1f6c66bdafd38299e1995282ee814bfee0d53491f05c。<!-- existing:SF-2026-ARXIV-2605-27547:end -->
<!-- delta:SF-2026-ARXIV-2605-27547:start -->mixed human-agent allocation exposes capability and risk as bounded options that a clearing authority accepts rather than allowing agents to self-assign consequential work<!-- delta:SF-2026-ARXIV-2605-27547:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27547:end -->

<!-- books-review:SF-2026-ARXIV-2605-27559:start -->
<!-- existing:SF-2026-ARXIV-2605-27559:start -->独立 reviewer 顺读 `books/part-07-agent/80-reflection.md` 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']。当前命题：本章拥有执行反馈、诊断、修复提议与再次验证的闭环，不允许模型自评直接成为 commit authority；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。<!-- existing:SF-2026-ARXIV-2605-27559:end -->
<!-- delta:SF-2026-ARXIV-2605-27559:start -->multi-stage correction separates failure detection from conditional miscorrection, preventing a successful detector from being mistaken for an effective repair loop<!-- delta:SF-2026-ARXIV-2605-27559:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27559:end -->

<!-- books-review:SF-2026-ARXIV-2605-27569:start -->
<!-- existing:SF-2026-ARXIV-2605-27569:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27569:end -->
<!-- delta:SF-2026-ARXIV-2605-27569:start -->machine-unlearning evidence must inspect residual representation state in addition to output behavior and membership attacks<!-- delta:SF-2026-ARXIV-2605-27569:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27569:end -->

<!-- books-review:SF-2026-ARXIV-2605-27575:start -->
<!-- existing:SF-2026-ARXIV-2605-27575:start -->独立 reviewer 顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。当前命题：本章从 Agent Definition、Run Identity、三个平面、Runtime State Machine 到 release/rollback 拥有长任务生命周期；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-27575:end -->
<!-- delta:SF-2026-ARXIV-2605-27575:start -->agent definition as code, on-demand execution and zero-trust access turn identity, deployment and authorization into platform-managed lifecycle objects<!-- delta:SF-2026-ARXIV-2605-27575:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27575:end -->

<!-- books-review:SF-2026-ARXIV-2605-27589:start -->
<!-- existing:SF-2026-ARXIV-2605-27589:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前命题：本章拥有 action-conditioned transition、latent dynamics、imagined rollout 与可修订 world state；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-27589:end -->
<!-- delta:SF-2026-ARXIV-2605-27589:start -->world-model evaluation uses paired causal interventions and per-primitive outcomes so plausible video cannot substitute for controllable environment dynamics<!-- delta:SF-2026-ARXIV-2605-27589:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27589:end -->

<!-- books-review:SF-2026-ARXIV-2605-27599:start -->
<!-- existing:SF-2026-ARXIV-2605-27599:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=2d1e493797f1eccb4144efa39b89a1ac2f53b4df03a9c3ea0bb6ecd6e9dea1f5。<!-- existing:SF-2026-ARXIV-2605-27599:end -->
<!-- delta:SF-2026-ARXIV-2605-27599:start -->process-level energy attribution is impossible without an observable hardware counter and attribution boundary; utilization or board power are not equivalent evidence<!-- delta:SF-2026-ARXIV-2605-27599:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27599:end -->

<!-- books-review:SF-2026-ARXIV-2605-27621:start -->
<!-- existing:SF-2026-ARXIV-2605-27621:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前命题：本章拥有多 Agent 的角色、消息、协作拓扑与贡献/风险边界，不把多个独立调用误作协调系统；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=50c6c9beefaa32eb4dbe1f6c66bdafd38299e1995282ee814bfee0d53491f05c。<!-- existing:SF-2026-ARXIV-2605-27621:end -->
<!-- delta:SF-2026-ARXIV-2605-27621:start -->agent contribution requires a declared removal intervention and coalition distribution before attribution can drive pruning, cost optimization or safety audit<!-- delta:SF-2026-ARXIV-2605-27621:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27621:end -->

<!-- books-review:SF-2026-ARXIV-2605-27630:start -->
<!-- existing:SF-2026-ARXIV-2605-27630:start -->独立 reviewer 顺读 `books/part-07-agent/80-reflection.md` 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']。当前命题：本章拥有执行反馈、诊断、修复提议与再次验证的闭环，不允许模型自评直接成为 commit authority；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。<!-- existing:SF-2026-ARXIV-2605-27630:end -->
<!-- delta:SF-2026-ARXIV-2605-27630:start -->coordination traces provide typed behavioral evidence for verification, diagnosis, repair and episodic reuse instead of unconstrained self-reflection<!-- delta:SF-2026-ARXIV-2605-27630:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27630:end -->

<!-- books-review:SF-2026-ARXIV-2605-27668:start -->
<!-- existing:SF-2026-ARXIV-2605-27668:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27668:end -->
<!-- delta:SF-2026-ARXIV-2605-27668:start -->forecast calibration targets a distribution over human uncertainty and must be evaluated separately from answer accuracy or post-hoc temperature scaling<!-- delta:SF-2026-ARXIV-2605-27668:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27668:end -->

<!-- books-review:SF-2026-ARXIV-2605-27671:start -->
<!-- existing:SF-2026-ARXIV-2605-27671:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']。当前命题：本章从目标到 signal、四层指标、SLO/error budget 与 sensor failure 拥有在线测量状态；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=2df3a2ca46d49c53ca839c25b7fd577e1b3c8126a2c5bc583f5faacb2e0ef8e1。<!-- existing:SF-2026-ARXIV-2605-27671:end -->
<!-- delta:SF-2026-ARXIV-2605-27671:start -->multi-turn deception monitoring treats geometric trajectory signatures as a fallible longitudinal sensor rather than classifying isolated messages<!-- delta:SF-2026-ARXIV-2605-27671:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27671:end -->

<!-- books-review:SF-2026-ARXIV-2605-27678:start -->
<!-- existing:SF-2026-ARXIV-2605-27678:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=d8ebb2036e9658dfb608f34357681494598cea89650a74570ae988b12fe13665。<!-- existing:SF-2026-ARXIV-2605-27678:end -->
<!-- delta:SF-2026-ARXIV-2605-27678:start -->multimodal modules receive independent parallel layouts while boundary communicators own forward activation and reverse-gradient transforms.<!-- delta:SF-2026-ARXIV-2605-27678:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27678:end -->

<!-- books-review:SF-2026-ARXIV-2605-27681:start -->
<!-- existing:SF-2026-ARXIV-2605-27681:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-27681:end -->
<!-- delta:SF-2026-ARXIV-2605-27681:start -->alignment-faking evidence must bind hidden-versus-observed incentive conditions and compliance gaps rather than infer deception from a single compliant output<!-- delta:SF-2026-ARXIV-2605-27681:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27681:end -->

<!-- books-review:SF-2026-ARXIV-2605-27690:start -->
<!-- existing:SF-2026-ARXIV-2605-27690:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-27690:end -->
<!-- delta:SF-2026-ARXIV-2605-27690:start -->agent safety auditing becomes prefix-state prediction over evolving trajectories rather than post-hoc final-output classification.<!-- delta:SF-2026-ARXIV-2605-27690:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27690:end -->

<!-- books-review:SF-2026-ARXIV-2605-27710:start -->
<!-- existing:SF-2026-ARXIV-2605-27710:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27710:end -->
<!-- delta:SF-2026-ARXIV-2605-27710:start -->claim-citation verification escalates retrieval depth only when evidence remains insufficient and preserves claim, cited source and retrieved support as separate identities<!-- delta:SF-2026-ARXIV-2605-27710:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27710:end -->

<!-- books-review:SF-2026-ARXIV-2605-27712:start -->
<!-- existing:SF-2026-ARXIV-2605-27712:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=dcd5bd0656e8d1a39e0b368962d14794d9ac1659d1f3a83dff267a67788b200a。<!-- existing:SF-2026-ARXIV-2605-27712:end -->
<!-- delta:SF-2026-ARXIV-2605-27712:start -->prefix-safe belief tracking separates probability calibration from candidate ranking and prevents future evidence from leaking into earlier confidence checkpoints<!-- delta:SF-2026-ARXIV-2605-27712:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27712:end -->

<!-- books-review:SF-2026-ARXIV-2605-27720:start -->
<!-- existing:SF-2026-ARXIV-2605-27720:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27720:end -->
<!-- delta:SF-2026-ARXIV-2605-27720:start -->deployment approval is a posterior risk decision under finite rollouts, not an empirical success-rate threshold.<!-- delta:SF-2026-ARXIV-2605-27720:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27720:end -->

<!-- books-review:SF-2026-ARXIV-2605-27744:start -->
<!-- existing:SF-2026-ARXIV-2605-27744:start -->Ch84 已明确 Agent Runtime 位于 model proposal、policy、tool 与 environment 之间，并禁止 Serving Engine 接管 workflow；本 family 是该边界的实现案例。 owner_sha256=007d5f3118e5050530972c51e8c223c5ad7717c18b78632e4fdc828c91de8c8a。<!-- existing:SF-2026-ARXIV-2605-27744:end -->
<!-- delta:SF-2026-ARXIV-2605-27744:start -->a typed agent runtime tier mediates framework semantics and engine events so cross-layer serving policies have one owner.<!-- delta:SF-2026-ARXIV-2605-27744:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27744:end -->

<!-- books-review:SF-2026-ARXIV-2605-27752:start -->
<!-- existing:SF-2026-ARXIV-2605-27752:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27752:end -->
<!-- delta:SF-2026-ARXIV-2605-27752:start -->confidence calibration is protocol-sensitive: answer normalization, prompt and likelihood extraction are part of the evaluator identity rather than implementation detail<!-- delta:SF-2026-ARXIV-2605-27752:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27752:end -->

<!-- books-review:SF-2026-ARXIV-2605-27759:start -->
<!-- existing:SF-2026-ARXIV-2605-27759:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27759:end -->
<!-- delta:SF-2026-ARXIV-2605-27759:start -->VLA generalization evaluation must cross embodiment, task and perturbation strata instead of treating aggregate zero-shot success as transferable physical capability<!-- delta:SF-2026-ARXIV-2605-27759:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27759:end -->

<!-- books-review:SF-2026-ARXIV-2605-27760:start -->
<!-- existing:SF-2026-ARXIV-2605-27760:start -->独立 reviewer 顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。当前命题：本章从 Agent Definition、Run Identity、三个平面、Runtime State Machine 到 release/rollback 拥有长任务生命周期；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-27760:end -->
<!-- delta:SF-2026-ARXIV-2605-27760:start -->skill updates need proposal, evaluation, acceptance and rollback analogous to optimizer steps rather than editing procedural files without a quality gate<!-- delta:SF-2026-ARXIV-2605-27760:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27760:end -->

<!-- books-review:SF-2026-ARXIV-2605-27761:start -->
<!-- existing:SF-2026-ARXIV-2605-27761:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前命题：本章要求评估声明绑定完整对象与分布，并把 executable evidence、scorer、dataset、run 与 release gate 分层；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=544c5572d44f5414964f9754a25b1ac6cce7b00dd51503d359ac0042347d4102。<!-- existing:SF-2026-ARXIV-2605-27761:end -->
<!-- delta:SF-2026-ARXIV-2605-27761:start -->mobile-agent tasks on closed-source applications need guideline-grounded state predicates and a verifiable evaluator rather than screenshot-only success claims<!-- delta:SF-2026-ARXIV-2605-27761:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27761:end -->

<!-- books-review:SF-2026-ARXIV-2605-27763:start -->
<!-- existing:SF-2026-ARXIV-2605-27763:start -->Ch66 已把 backend/runtime configuration 纳入 run identity 并要求 paired reproducibility；本 family 提供 source-specific evidence，但不改变长期命题。 owner_sha256=dcd5bd0656e8d1a39e0b368962d14794d9ac1659d1f3a83dff267a67788b200a。<!-- existing:SF-2026-ARXIV-2605-27763:end -->
<!-- delta:SF-2026-ARXIV-2605-27763:start -->batch condition and kernel path enter the safety evaluation identity through paired exact-stack tests and capability controls.<!-- delta:SF-2026-ARXIV-2605-27763:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27763:end -->

<!-- books-review:SF-2026-ARXIV-2605-27766:start -->
<!-- existing:SF-2026-ARXIV-2605-27766:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前命题：本章从资产/信任边界、policy-bound sensor、行为控制权、supply chain 到 safe-commit certificate 拥有安全 gate；该主线已拥有相同责任边界，论文只构成受限机制或测量案例，故不重复扩写 owner。 owner_sha256=b7f3c2fe074b7f5dd125494c852bd425cb55f41e3f49addebc511eb185e440b2。<!-- existing:SF-2026-ARXIV-2605-27766:end -->
<!-- delta:SF-2026-ARXIV-2605-27766:start -->privacy evaluation must include persistent social interaction because leakage can propagate between agents even when each isolated prompt appears safe<!-- delta:SF-2026-ARXIV-2605-27766:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27766:end -->

<!-- books-review:SF-2026-ARXIV-2605-27784:start -->
<!-- existing:SF-2026-ARXIV-2605-27784:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=cdbd30c02b7edaf6b5ab52d3b792daca5314f9a39aa3ec4e87773ae2af613ab8。<!-- existing:SF-2026-ARXIV-2605-27784:end -->
<!-- delta:SF-2026-ARXIV-2605-27784:start -->long-lived prompt policies require executable collision witnesses and resolution profiles so rule precedence and tool-interface effects can be regression tested<!-- delta:SF-2026-ARXIV-2605-27784:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27784:end -->

<!-- books-review:SF-2026-ARXIV-2605-27785:start -->
<!-- existing:SF-2026-ARXIV-2605-27785:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=5f8a4bb45e793d2a58884400b4ad2c8e7ae79c7e9c8b10e2fa403c37ccba87ca。<!-- existing:SF-2026-ARXIV-2605-27785:end -->
<!-- delta:SF-2026-ARXIV-2605-27785:start -->agent traces become a queryable evidence plane through a client-native engine that combines relational scans with bounded model operators.<!-- delta:SF-2026-ARXIV-2605-27785:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27785:end -->

<!-- books-review:SF-2026-ARXIV-2605-27789:start -->
<!-- existing:SF-2026-ARXIV-2605-27789:start -->独立 reviewer 在当前 Books 版本顺读 owner 与 adjacent 后确认：既有主线尚未显式承载该 family 的长期 state/control/evidence delta；保留为最小写回，且必须并入 canonical H2 的演进叙述。 owner_sha256=dcd5bd0656e8d1a39e0b368962d14794d9ac1659d1f3a83dff267a67788b200a。<!-- existing:SF-2026-ARXIV-2605-27789:end -->
<!-- delta:SF-2026-ARXIV-2605-27789:start -->LLM-judge comparisons need fixed evidence and answer budgets, cluster-aware inference, preregistered hypotheses and second-judge replication<!-- delta:SF-2026-ARXIV-2605-27789:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27789:end -->

<!-- books-review:SF-2026-ARXIV-2605-27820:start -->
<!-- existing:SF-2026-ARXIV-2605-27820:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27820:end -->
<!-- delta:SF-2026-ARXIV-2605-27820:start -->However, existing benchmarks fail to jointly evaluate these capabilities due to challenges in designing strictly coupled multi-capability tasks, simulating natural and task-constrained user feedback, and ensuring objective evaluation of dynamic interaction.<!-- delta:SF-2026-ARXIV-2605-27820:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27820:end -->

<!-- books-review:SF-2026-ARXIV-2605-27825:start -->
<!-- existing:SF-2026-ARXIV-2605-27825:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-27825:end -->
<!-- delta:SF-2026-ARXIV-2605-27825:start -->We propose Multi-Recall Memory MIA (MRMMIA), a unified attack that utilizes multiple recall probes to the agent to extract the membership signal across black-box, gray-box, and white-box settings.<!-- delta:SF-2026-ARXIV-2605-27825:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27825:end -->

<!-- books-review:SF-2026-ARXIV-2605-27850:start -->
<!-- existing:SF-2026-ARXIV-2605-27850:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-27850:end -->
<!-- delta:SF-2026-ARXIV-2605-27850:start -->We propose \textbf{TCP-MCP} (Topology-Coupled Prompting for Multi-Agent Collaborative Problem-Solving), a co-evolution framework that searches agent prompts and communication topologies as a unified genome.<!-- delta:SF-2026-ARXIV-2605-27850:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27850:end -->

<!-- books-review:SF-2026-ARXIV-2605-27879:start -->
<!-- existing:SF-2026-ARXIV-2605-27879:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27879:end -->
<!-- delta:SF-2026-ARXIV-2605-27879:start -->We propose Faithful Agentic XAI (FAX), a framework that improves explanation faithfulness through explicit verification.<!-- delta:SF-2026-ARXIV-2605-27879:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27879:end -->

<!-- books-review:SF-2026-ARXIV-2605-27881:start -->
<!-- existing:SF-2026-ARXIV-2605-27881:start -->已顺读 owner `books/part-04-training-system/27-data.md` 的 18 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', 'books/part-04-training-system/28-pretraining.md']；当前 owner 负责 `TRAIN-DATA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md, books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-27881:end -->
<!-- delta:SF-2026-ARXIV-2605-27881:start -->We present a controlled empirical study that isolates three under-explored dimensions of search agent training.<!-- delta:SF-2026-ARXIV-2605-27881:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27881:end -->

<!-- books-review:SF-2026-ARXIV-2605-27898:start -->
<!-- existing:SF-2026-ARXIV-2605-27898:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27898:end -->
<!-- delta:SF-2026-ARXIV-2605-27898:start -->In this work, we present a unified framework for the fair evaluation of LLM agentic capabilities.<!-- delta:SF-2026-ARXIV-2605-27898:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27898:end -->

<!-- books-review:SF-2026-ARXIV-2605-27899:start -->
<!-- existing:SF-2026-ARXIV-2605-27899:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-27899:end -->
<!-- delta:SF-2026-ARXIV-2605-27899:start -->We propose SkillC, a framework based on Contrastive Skill Credit Assignment (CSCA) that converts this contrast into a direct learning signal for internalization.<!-- delta:SF-2026-ARXIV-2605-27899:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27899:end -->

<!-- books-review:SF-2026-ARXIV-2605-27901:start -->
<!-- existing:SF-2026-ARXIV-2605-27901:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-27901:end -->
<!-- delta:SF-2026-ARXIV-2605-27901:start -->We present the first large-scale evaluation of CoT monitorability across 13 diverse languages and seven frontier model families, comprising 16 models.<!-- delta:SF-2026-ARXIV-2605-27901:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27901:end -->

<!-- books-review:SF-2026-ARXIV-2605-27918:start -->
<!-- existing:SF-2026-ARXIV-2605-27918:start -->已顺读 owner `books/part-04-training-system/36-distributed-training.md` 的 30 个 H2 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前 owner 负责 `TRAIN-DISTRIBUTED-TRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`96ef81f64d613fd7cb8eb3199e94ab8ed66b737dd9764b83f4e756b3d8ca8c58`；adjacent=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-27918:end -->
<!-- delta:SF-2026-ARXIV-2605-27918:start -->We present Entrain, a distributed MLLM training framework that addresses both heterogeneity and variability in multimodal training workloads.<!-- delta:SF-2026-ARXIV-2605-27918:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27918:end -->

<!-- books-review:SF-2026-ARXIV-2605-27922:start -->
<!-- existing:SF-2026-ARXIV-2605-27922:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27922:end -->
<!-- delta:SF-2026-ARXIV-2605-27922:start -->However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study.<!-- delta:SF-2026-ARXIV-2605-27922:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27922:end -->

<!-- books-review:SF-2026-ARXIV-2605-27947:start -->
<!-- existing:SF-2026-ARXIV-2605-27947:start -->已顺读 owner `books/part-05-inference-system/56-inference-scheduling.md` 的 18 个 H2 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']；当前 owner 负责 `INFER-SCHEDULING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2ae93eeb9a0bfd027148c9a581d2e13c146e920e51834112063db83818271e8e`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md, books/part-06-ai-infrastructure/57-what-is-ai-platform.md`。<!-- existing:SF-2026-ARXIV-2605-27947:end -->
<!-- delta:SF-2026-ARXIV-2605-27947:start -->Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or even reverse when late predictions become less action-relevant or physically unreliable.<!-- delta:SF-2026-ARXIV-2605-27947:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27947:end -->

<!-- books-review:SF-2026-ARXIV-2605-27954:start -->
<!-- existing:SF-2026-ARXIV-2605-27954:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-27954:end -->
<!-- delta:SF-2026-ARXIV-2605-27954:start -->However, the training dynamics of agent RL remain poorly understood, limiting our ability to diagnose instabilities and design more effective training algorithms.<!-- delta:SF-2026-ARXIV-2605-27954:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27954:end -->

<!-- books-review:SF-2026-ARXIV-2605-27957:start -->
<!-- existing:SF-2026-ARXIV-2605-27957:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27957:end -->
<!-- delta:SF-2026-ARXIV-2605-27957:start -->We introduce DisasterBench, a benchmark for evaluating structured multi-agent planning over semantically similar but operationally distinct disaster-response tools.<!-- delta:SF-2026-ARXIV-2605-27957:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27957:end -->

<!-- books-review:SF-2026-ARXIV-2605-27963:start -->
<!-- existing:SF-2026-ARXIV-2605-27963:start -->已顺读 owner `books/part-04-training-system/36-distributed-training.md` 的 30 个 H2 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；当前 owner 负责 `TRAIN-DISTRIBUTED-TRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`96ef81f64d613fd7cb8eb3199e94ab8ed66b737dd9764b83f4e756b3d8ca8c58`；adjacent=`books/part-04-training-system/35-checkpoint.md, books/part-04-training-system/37-tensor-parallel.md`。<!-- existing:SF-2026-ARXIV-2605-27963:end -->
<!-- delta:SF-2026-ARXIV-2605-27963:start -->Datacenter network design plays a critical role in AI training by supporting scaling to thousands of accelerators.<!-- delta:SF-2026-ARXIV-2605-27963:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27963:end -->

<!-- books-review:SF-2026-ARXIV-2605-27980:start -->
<!-- existing:SF-2026-ARXIV-2605-27980:start -->已顺读 owner `books/part-02-model/13-position-encoding.md` 的 17 个 H2 与相邻章节 ['books/part-02-model/12-embedding.md', 'books/part-02-model/14-self-attention.md']；当前 owner 负责 `MODEL-POSITION-ENCODING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b458d0e04ecd5b86463a9c67c8c2c1da4a11f4a9e08f41daa2ba7f6b0cc5ca89`；adjacent=`books/part-02-model/12-embedding.md, books/part-02-model/14-self-attention.md`。<!-- existing:SF-2026-ARXIV-2605-27980:end -->
<!-- delta:SF-2026-ARXIV-2605-27980:start -->To address it, we propose Periodic RoPE (P-RoPE), a positional encoding mechanism designed to circumvent this exhaustion.<!-- delta:SF-2026-ARXIV-2605-27980:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27980:end -->

<!-- books-review:SF-2026-ARXIV-2605-27995:start -->
<!-- existing:SF-2026-ARXIV-2605-27995:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-27995:end -->
<!-- delta:SF-2026-ARXIV-2605-27995:start -->To evaluate it, we propose AsyncTool, a benchmark for assessing LLM-based agents in interactive multi-task tool-use environments with delayed tool feedback.<!-- delta:SF-2026-ARXIV-2605-27995:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-27995:end -->

<!-- books-review:SF-2026-ARXIV-2605-28000:start -->
<!-- existing:SF-2026-ARXIV-2605-28000:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28000:end -->
<!-- delta:SF-2026-ARXIV-2605-28000:start -->Large language model agents are increasingly expected to perform operational work: calling APIs, manipulating files, assembling workflows, and acting inside enterprise systems.<!-- delta:SF-2026-ARXIV-2605-28000:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28000:end -->

<!-- books-review:SF-2026-ARXIV-2605-28009:start -->
<!-- existing:SF-2026-ARXIV-2605-28009:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28009:end -->
<!-- delta:SF-2026-ARXIV-2605-28009:start -->To this end, we introduce MemGuard, a type-aware memory framework that preserves functional memory boundaries during memory construction and retrieval.<!-- delta:SF-2026-ARXIV-2605-28009:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28009:end -->

<!-- books-review:SF-2026-ARXIV-2605-28017:start -->
<!-- existing:SF-2026-ARXIV-2605-28017:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28017:end -->
<!-- delta:SF-2026-ARXIV-2605-28017:start -->In this paper, we re-evaluate seven GEO attacks under a realistic three-stage pipeline (retriever\,$\to$\,LLM reranker\,$\to$\,LLM generator).<!-- delta:SF-2026-ARXIV-2605-28017:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28017:end -->

<!-- books-review:SF-2026-ARXIV-2605-28044:start -->
<!-- existing:SF-2026-ARXIV-2605-28044:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28044:end -->
<!-- delta:SF-2026-ARXIV-2605-28044:start -->We study this diagnostic failure as citation laundering: a related source is presented as warrant for an over-strong claim.<!-- delta:SF-2026-ARXIV-2605-28044:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28044:end -->

<!-- books-review:SF-2026-ARXIV-2605-28046:start -->
<!-- existing:SF-2026-ARXIV-2605-28046:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28046:end -->
<!-- delta:SF-2026-ARXIV-2605-28046:start -->We propose MemCog, a Memory-as-Cognition system that makes memory access an integral part of the reasoning process.<!-- delta:SF-2026-ARXIV-2605-28046:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28046:end -->

<!-- books-review:SF-2026-ARXIV-2605-28053:start -->
<!-- existing:SF-2026-ARXIV-2605-28053:start -->已顺读 owner `books/part-05-inference-system/46-continuous-batching.md` 的 19 个 H2 与相邻章节 ['books/part-05-inference-system/45-why-kv-cache-speeds-up.md', 'books/part-05-inference-system/47-pagedattention.md']；当前 owner 负责 `INFER-CONTINUOUS-BATCHING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`63cc72a49b463999b35f00cebee74adab003bef2716685033c9a7a256d1fb426`；adjacent=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md, books/part-05-inference-system/47-pagedattention.md`。<!-- existing:SF-2026-ARXIV-2605-28053:end -->
<!-- delta:SF-2026-ARXIV-2605-28053:start -->We formulate this problem as read-write TTT serving and present RW-TTT , which tags each decode step with its owner, version, and READ/WRITE effect, batches only compatible phases, and commits updates only to the owner.<!-- delta:SF-2026-ARXIV-2605-28053:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28053:end -->

<!-- books-review:SF-2026-ARXIV-2605-28071:start -->
<!-- existing:SF-2026-ARXIV-2605-28071:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28071:end -->
<!-- delta:SF-2026-ARXIV-2605-28071:start -->In this paper, we present AgentGuard, an attribute-based access control framework for tool-use LLM-based agents.<!-- delta:SF-2026-ARXIV-2605-28071:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28071:end -->

<!-- books-review:SF-2026-ARXIV-2605-28074:start -->
<!-- existing:SF-2026-ARXIV-2605-28074:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28074:end -->
<!-- delta:SF-2026-ARXIV-2605-28074:start -->We present SilentRetrieval, a two-stage data poisoning attack that hijacks RAG systems through adversarially crafted yet fluent documents.<!-- delta:SF-2026-ARXIV-2605-28074:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28074:end -->

<!-- books-review:SF-2026-ARXIV-2605-28083:start -->
<!-- existing:SF-2026-ARXIV-2605-28083:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28083:end -->
<!-- delta:SF-2026-ARXIV-2605-28083:start -->To overcome this limitation, we propose VLA-Hijack, a unified adversarial framework that breaks the transferability bottleneck by exploiting a fundamental vulnerability identified in this work: before planning any motion, a VLA model must first use visual information to locate its own robotic arm within the environment.<!-- delta:SF-2026-ARXIV-2605-28083:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28083:end -->

<!-- books-review:SF-2026-ARXIV-2605-28095:start -->
<!-- existing:SF-2026-ARXIV-2605-28095:start -->已顺读 owner `books/part-05-inference-system/54-gpu-memory.md` 的 15 个 H2 与相邻章节 ['books/part-05-inference-system/53-kserve-llm.md', 'books/part-05-inference-system/55-pd-disaggregation.md']；当前 owner 负责 `INFER-GPU-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`a089e81dda8ffea7f46622421f9a24b2e91b13731c04d52c67284966c417cce4`；adjacent=`books/part-05-inference-system/53-kserve-llm.md, books/part-05-inference-system/55-pd-disaggregation.md`。<!-- existing:SF-2026-ARXIV-2605-28095:end -->
<!-- delta:SF-2026-ARXIV-2605-28095:start -->We present SiDP, a memory-efficient data-parallel paradigm for offline LLM inference that treats weights as a bandwidth-backed shared resource inside a DP group.<!-- delta:SF-2026-ARXIV-2605-28095:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28095:end -->

<!-- books-review:SF-2026-ARXIV-2605-28097:start -->
<!-- existing:SF-2026-ARXIV-2605-28097:start -->已顺读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 的 15 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/72-security.md', 'books/part-07-agent/74-prompt.md']；当前 owner 负责 `PLATFORM-PRODUCTION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`8a1230c5475bc0996e1bc446b54154f914d1177178f82eb98e8c9ebe5ad29679`；adjacent=`books/part-06-ai-infrastructure/72-security.md, books/part-07-agent/74-prompt.md`。<!-- existing:SF-2026-ARXIV-2605-28097:end -->
<!-- delta:SF-2026-ARXIV-2605-28097:start -->We present ICAN-Deploy (Identity-stable CANary Deployment), a middleware construction whose state machine holds the identity hash invariant across the canary window by separating capability names (frozen, hashed) from capability versions (mutable runtime state).<!-- delta:SF-2026-ARXIV-2605-28097:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28097:end -->

<!-- books-review:SF-2026-ARXIV-2605-28108:start -->
<!-- existing:SF-2026-ARXIV-2605-28108:start -->已顺读 owner `books/part-07-agent/79-planning.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前 owner 负责 `AGENT-PLANNING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`22e2cb6740b7057464c1cd35feed95d37cb5f48f7ea0d6ca5f2ddf761b61dd84`；adjacent=`books/part-07-agent/78-tool-calling.md, books/part-07-agent/80-reflection.md`。<!-- existing:SF-2026-ARXIV-2605-28108:end -->
<!-- delta:SF-2026-ARXIV-2605-28108:start -->ATR is hard even to evaluate: the right question is underdetermined and its payoff deferred to tasks that may never arise.<!-- delta:SF-2026-ARXIV-2605-28108:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28108:end -->

<!-- books-review:SF-2026-ARXIV-2605-28112:start -->
<!-- existing:SF-2026-ARXIV-2605-28112:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28112:end -->
<!-- delta:SF-2026-ARXIV-2605-28112:start -->We introduce Routing Hijacking, a routing-stage attack in which a malicious client forges its profile to attract target queries despite having irrelevant underlying data.<!-- delta:SF-2026-ARXIV-2605-28112:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28112:end -->

<!-- books-review:SF-2026-ARXIV-2605-28116:start -->
<!-- existing:SF-2026-ARXIV-2605-28116:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28116:end -->
<!-- delta:SF-2026-ARXIV-2605-28116:start -->We present MIRAGE (Mobile Injection of Realistic Adversarial GUI Examples), a pipeline that turns benign mobile screenshots into prompt-injection samples by placing attacker-controlled text into ordinary user-generated content regions, without modifying the agent, the application, or the operating system.<!-- delta:SF-2026-ARXIV-2605-28116:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28116:end -->

<!-- books-review:SF-2026-ARXIV-2605-28122:start -->
<!-- existing:SF-2026-ARXIV-2605-28122:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28122:end -->
<!-- delta:SF-2026-ARXIV-2605-28122:start -->We present SNARE (Synthesizing Non-adversarial scenarios for Adaptive Reward-guided Elicitation), a pipeline that composes benign scenarios from reusable scope and trap fragments, scores each run with a judge-free oracle flagging trap-pattern matches and unsolicited file additions or deletions, and uses Thompson sampling to steer each pair's run budget toward the scenarios that most often trigger it.<!-- delta:SF-2026-ARXIV-2605-28122:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28122:end -->

<!-- books-review:SF-2026-ARXIV-2605-28158:start -->
<!-- existing:SF-2026-ARXIV-2605-28158:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28158:end -->
<!-- delta:SF-2026-ARXIV-2605-28158:start -->We introduce OR-Space, a full-lifecycle workspace benchmark for evaluating industrial optimization agents across model construction, model revision, and grounded explanation.<!-- delta:SF-2026-ARXIV-2605-28158:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28158:end -->

<!-- books-review:SF-2026-ARXIV-2605-28201:start -->
<!-- existing:SF-2026-ARXIV-2605-28201:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28201:end -->
<!-- delta:SF-2026-ARXIV-2605-28201:start -->However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate.<!-- delta:SF-2026-ARXIV-2605-28201:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28201:end -->

<!-- books-review:SF-2026-ARXIV-2605-28213:start -->
<!-- existing:SF-2026-ARXIV-2605-28213:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28213:end -->
<!-- delta:SF-2026-ARXIV-2605-28213:start -->We introduce KLineage, which learns this missing "when" knowledge from expert kernels: instead of relying on forward rollouts, KLineage walks expert implementations backward through validation-gated simplifications and reverses each accepted step into a reusable optimization skill.<!-- delta:SF-2026-ARXIV-2605-28213:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28213:end -->

<!-- books-review:SF-2026-ARXIV-2605-28214:start -->
<!-- existing:SF-2026-ARXIV-2605-28214:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28214:end -->
<!-- delta:SF-2026-ARXIV-2605-28214:start -->In this paper, we study whether latent states can carry attack-associated information that remains effective during clean executions.<!-- delta:SF-2026-ARXIV-2605-28214:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28214:end -->

<!-- books-review:SF-2026-ARXIV-2605-28224:start -->
<!-- existing:SF-2026-ARXIV-2605-28224:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28224:end -->
<!-- delta:SF-2026-ARXIV-2605-28224:start -->We propose a unified framework that decomposes memory along two axes -- the scope of transfer (within an expansion vs.<!-- delta:SF-2026-ARXIV-2605-28224:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28224:end -->

<!-- books-review:SF-2026-ARXIV-2605-28282:start -->
<!-- existing:SF-2026-ARXIV-2605-28282:start -->已顺读 owner `books/part-07-agent/81-workflow.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 负责 `AGENT-WORKFLOW` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`16b31ba8998e738c714524553aac240bf037dcb61c7bb84c03bcd77bacb2a3cb`；adjacent=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-28282:end -->
<!-- delta:SF-2026-ARXIV-2605-28282:start -->We present ResearchLoop, an evidence-gated control plane for AI-assisted computational research.<!-- delta:SF-2026-ARXIV-2605-28282:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28282:end -->

<!-- books-review:SF-2026-ARXIV-2605-28302:start -->
<!-- existing:SF-2026-ARXIV-2605-28302:start -->已顺读 owner `books/part-05-inference-system/55-pd-disaggregation.md` 的 17 个 H2 与相邻章节 ['books/part-05-inference-system/54-gpu-memory.md', 'books/part-05-inference-system/56-inference-scheduling.md']；当前 owner 负责 `INFER-PD-DISAGGREGATION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`766ef84157a1febdc383d1e3a9b2119232482c82bc3e46a4d1d00c07fa94457e`；adjacent=`books/part-05-inference-system/54-gpu-memory.md, books/part-05-inference-system/56-inference-scheduling.md`。<!-- existing:SF-2026-ARXIV-2605-28302:end -->
<!-- delta:SF-2026-ARXIV-2605-28302:start -->Each level of disaggregation deepens the scheduling design space across workload characteristics, resource allocation, and interconnect topology, raising the central question: when does each level actually pay off?<!-- delta:SF-2026-ARXIV-2605-28302:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28302:end -->

<!-- books-review:SF-2026-ARXIV-2605-28354:start -->
<!-- existing:SF-2026-ARXIV-2605-28354:start -->已顺读 owner `books/part-07-agent/79-planning.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/78-tool-calling.md', 'books/part-07-agent/80-reflection.md']；当前 owner 负责 `AGENT-PLANNING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`22e2cb6740b7057464c1cd35feed95d37cb5f48f7ea0d6ca5f2ddf761b61dd84`；adjacent=`books/part-07-agent/78-tool-calling.md, books/part-07-agent/80-reflection.md`。<!-- existing:SF-2026-ARXIV-2605-28354:end -->
<!-- delta:SF-2026-ARXIV-2605-28354:start -->We study this through Plan, a structured agentic behavior for multi-hop retrieval that decomposes a question into ordered sub-questions before any retrieval is performed, so that each search step can be anchored to a pre-designed sub-question instead of drifting under the influence of partially relevant documents retrieved earlier.<!-- delta:SF-2026-ARXIV-2605-28354:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28354:end -->

<!-- books-review:SF-2026-ARXIV-2605-28371:start -->
<!-- existing:SF-2026-ARXIV-2605-28371:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28371:end -->
<!-- delta:SF-2026-ARXIV-2605-28371:start -->Industrial Prognostics and Health Management (PHM) provides a representative case study for a broader challenge in applied machine learning: translating published papers into executable, benchmark-ready implementations.<!-- delta:SF-2026-ARXIV-2605-28371:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28371:end -->

<!-- books-review:SF-2026-ARXIV-2605-28384:start -->
<!-- existing:SF-2026-ARXIV-2605-28384:start -->已顺读 owner `books/part-05-inference-system/56-inference-scheduling.md` 的 18 个 H2 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md', 'books/part-06-ai-infrastructure/57-what-is-ai-platform.md']；当前 owner 负责 `INFER-SCHEDULING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2ae93eeb9a0bfd027148c9a581d2e13c146e920e51834112063db83818271e8e`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md, books/part-06-ai-infrastructure/57-what-is-ai-platform.md`。<!-- existing:SF-2026-ARXIV-2605-28384:end -->
<!-- delta:SF-2026-ARXIV-2605-28384:start -->We propose Meta-Attention, a framework that dynamically routes each token to the most appropriate attention strategy -- full softmax attention, linear (kernel) attention, or sliding-window local attention -- via a Bayesian Meta-Controller.<!-- delta:SF-2026-ARXIV-2605-28384:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28384:end -->

<!-- books-review:SF-2026-ARXIV-2605-28390:start -->
<!-- existing:SF-2026-ARXIV-2605-28390:start -->已顺读 owner `books/part-07-agent/84-agent-platform.md` 的 20 个 H2 与相邻章节 ['books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-PLATFORM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360`；adjacent=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28390:end -->
<!-- delta:SF-2026-ARXIV-2605-28390:start -->Specifically, we propose HiSME, a lightweight hierarchical skill meta-evolving solution that jointly optimizes skills and the skill evolving strategy by learning meta-skills from agents' task execution traces.<!-- delta:SF-2026-ARXIV-2605-28390:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28390:end -->

<!-- books-review:SF-2026-ARXIV-2605-28424:start -->
<!-- existing:SF-2026-ARXIV-2605-28424:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28424:end -->
<!-- delta:SF-2026-ARXIV-2605-28424:start -->To address this dilemma, we propose Skill0.5, a novel agentic RL framework that explicitly differentiates skill treatments by combining general skill internalization with task-specific skill utilization.<!-- delta:SF-2026-ARXIV-2605-28424:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28424:end -->

<!-- books-review:SF-2026-ARXIV-2605-28433:start -->
<!-- existing:SF-2026-ARXIV-2605-28433:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28433:end -->
<!-- delta:SF-2026-ARXIV-2605-28433:start -->We formulate this as contract-preserving role evolution, requiring every committed edit to preserve five structural contracts (capability, communication, validation, aggregation, output protocol).<!-- delta:SF-2026-ARXIV-2605-28433:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28433:end -->

<!-- books-review:SF-2026-ARXIV-2605-28467:start -->
<!-- existing:SF-2026-ARXIV-2605-28467:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28467:end -->
<!-- delta:SF-2026-ARXIV-2605-28467:start -->We study consistency training, a family of fine-tuning objectives that enforce identical behavior on clean prompts and adversarial rewrites, and evaluate its two main variants, output-level (BCT) and activation-level (ACT), across five reasoning models.<!-- delta:SF-2026-ARXIV-2605-28467:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28467:end -->

<!-- books-review:SF-2026-ARXIV-2605-28480:start -->
<!-- existing:SF-2026-ARXIV-2605-28480:start -->已顺读 owner `books/part-07-agent/81-workflow.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；当前 owner 负责 `AGENT-WORKFLOW` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`16b31ba8998e738c714524553aac240bf037dcb61c7bb84c03bcd77bacb2a3cb`；adjacent=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-28480:end -->
<!-- delta:SF-2026-ARXIV-2605-28480:start -->We propose Audio-Mind, an auditable and pluggable framework for conditional evidence acquisition in audio understanding.<!-- delta:SF-2026-ARXIV-2605-28480:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28480:end -->

<!-- books-review:SF-2026-ARXIV-2605-28508:start -->
<!-- existing:SF-2026-ARXIV-2605-28508:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28508:end -->
<!-- delta:SF-2026-ARXIV-2605-28508:start -->To support practical decision-making, we propose a shared reporting framework that preserves comparability across systems and application types while remaining sensitive to deployment context.<!-- delta:SF-2026-ARXIV-2605-28508:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28508:end -->

<!-- books-review:SF-2026-ARXIV-2605-28510:start -->
<!-- existing:SF-2026-ARXIV-2605-28510:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28510:end -->
<!-- delta:SF-2026-ARXIV-2605-28510:start -->To bridge this gap, we introduce SOURCETRACKER, a 300M-parameter encoder tailored for code retrieval, together with a hybrid two-stage provenance-tracking pipeline HYBRIDSOURCETRACKER (HST).<!-- delta:SF-2026-ARXIV-2605-28510:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28510:end -->

<!-- books-review:SF-2026-ARXIV-2605-28544:start -->
<!-- existing:SF-2026-ARXIV-2605-28544:start -->已顺读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 的 19 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']；当前 owner 负责 `MULTIMODAL-WORLD-MODELS` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3`；adjacent=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-28544:end -->
<!-- delta:SF-2026-ARXIV-2605-28544:start -->We present DriveWAM, a driving world-action model that adapts a pretrained video diffusion transformer into an autoregressive video-action policy.<!-- delta:SF-2026-ARXIV-2605-28544:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28544:end -->

<!-- books-review:SF-2026-ARXIV-2605-28561:start -->
<!-- existing:SF-2026-ARXIV-2605-28561:start -->已顺读 owner `books/part-04-training-system/31-rlhf.md` 的 19 个 H2 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；当前 owner 负责 `TRAIN-RLHF` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09`；adjacent=`books/part-04-training-system/30-lora.md, books/part-04-training-system/32-ppo.md`。<!-- existing:SF-2026-ARXIV-2605-28561:end -->
<!-- delta:SF-2026-ARXIV-2605-28561:start -->We introduce Soft-RLVR, a framework for reinforcement learning from decomposed, learned verification signals.<!-- delta:SF-2026-ARXIV-2605-28561:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28561:end -->

<!-- books-review:SF-2026-ARXIV-2605-28565:start -->
<!-- existing:SF-2026-ARXIV-2605-28565:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28565:end -->
<!-- delta:SF-2026-ARXIV-2605-28565:start -->We design a three-dimension evaluation framework that scores each citation on intent-purpose alignment, source suitability, and answer-source fidelity, using expert-validated predefined matrices and a five-level fidelity rubric; the framework applies to any system that produces citation-bearing responses.<!-- delta:SF-2026-ARXIV-2605-28565:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28565:end -->

<!-- books-review:SF-2026-ARXIV-2605-28573:start -->
<!-- existing:SF-2026-ARXIV-2605-28573:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 的 20 个 H2 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；当前 owner 负责 `TRAIN-PRETRAINING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`e490fdda5b66982b11d46974ed6870ea048c715701cc606dfbd7d4df213486dd`；adjacent=`books/part-04-training-system/27-data.md, books/part-04-training-system/29-sft.md`。<!-- existing:SF-2026-ARXIV-2605-28573:end -->
<!-- delta:SF-2026-ARXIV-2605-28573:start -->The massive scaling of Large Language Models (LLMs) has made pretraining increasingly cost-prohibitive.<!-- delta:SF-2026-ARXIV-2605-28573:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28573:end -->

<!-- books-review:SF-2026-ARXIV-2605-28617:start -->
<!-- existing:SF-2026-ARXIV-2605-28617:start -->已顺读 owner `books/part-07-agent/78-tool-calling.md` 的 19 个 H2 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']；当前 owner 负责 `AGENT-TOOL-CALLING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9`；adjacent=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-28617:end -->
<!-- delta:SF-2026-ARXIV-2605-28617:start -->We present LACUNA, a programming model for agents that closes this split while preserving safety.<!-- delta:SF-2026-ARXIV-2605-28617:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28617:end -->

<!-- books-review:SF-2026-ARXIV-2605-28632:start -->
<!-- existing:SF-2026-ARXIV-2605-28632:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28632:end -->
<!-- delta:SF-2026-ARXIV-2605-28632:start -->Cryptographic watermarking is a leading defense for attributing text generated by large language models (LLMs).<!-- delta:SF-2026-ARXIV-2605-28632:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28632:end -->

<!-- books-review:SF-2026-ARXIV-2605-28634:start -->
<!-- existing:SF-2026-ARXIV-2605-28634:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28634:end -->
<!-- delta:SF-2026-ARXIV-2605-28634:start -->We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble &amp; Assemble paradigm.<!-- delta:SF-2026-ARXIV-2605-28634:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28634:end -->

<!-- books-review:SF-2026-ARXIV-2605-28640:start -->
<!-- existing:SF-2026-ARXIV-2605-28640:start -->已顺读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的 15 个 H2 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；当前 owner 负责 `INFER-KV-CACHE` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`e968ab13160cc25eb68d40fe046ab62092c3a5bb6785a46794241b176eed9b90`；adjacent=`books/part-05-inference-system/44-decode.md, books/part-05-inference-system/46-continuous-batching.md`。<!-- existing:SF-2026-ARXIV-2605-28640:end -->
<!-- delta:SF-2026-ARXIV-2605-28640:start -->In this paper, we investigate whether this exponentially decaying memory can also improve existing query-aware sparse inference methods.<!-- delta:SF-2026-ARXIV-2605-28640:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28640:end -->

<!-- books-review:SF-2026-ARXIV-2605-28646:start -->
<!-- existing:SF-2026-ARXIV-2605-28646:start -->已顺读 owner `books/part-06-ai-infrastructure/72-security.md` 的 21 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；当前 owner 负责 `PLATFORM-SECURITY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2611c265f71498b21628954e4204075454317f0e019ad8bf1422e8028c1f048b`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-28646:end -->
<!-- delta:SF-2026-ARXIV-2605-28646:start -->We present MaskClaw, an edge-side privacy arbitrator for GUI agents.<!-- delta:SF-2026-ARXIV-2605-28646:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28646:end -->

<!-- books-review:SF-2026-ARXIV-2605-28678:start -->
<!-- existing:SF-2026-ARXIV-2605-28678:start -->已顺读 owner `books/part-05-inference-system/48-speculative-decoding.md` 的 19 个 H2 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']；当前 owner 负责 `INFER-SPECULATIVE-DECODING` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`63abd49ea9f1fc8cb365512ea7b41f59d786879ec3603ab77545700307a29ce8`；adjacent=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-28678:end -->
<!-- delta:SF-2026-ARXIV-2605-28678:start -->In this work, we introduce DREAM-R, a framework that substantially improves the performance of speculative reasoning.<!-- delta:SF-2026-ARXIV-2605-28678:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28678:end -->

<!-- books-review:SF-2026-ARXIV-2605-28691:start -->
<!-- existing:SF-2026-ARXIV-2605-28691:start -->已顺读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 的 22 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；当前 owner 负责 `MULTIMODAL-GENERATIVE-PARADIGMS` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30`；adjacent=`books/part-03-multimodal-world-models/23-multimodal-representation.md, books/part-03-multimodal-world-models/25-multimodal-world-models.md`。<!-- existing:SF-2026-ARXIV-2605-28691:end -->
<!-- delta:SF-2026-ARXIV-2605-28691:start -->We introduce OSP-Next, an efficient text-to-video generation model that integrates sparse attention, parallelism, quantization, and reinforcement learning.<!-- delta:SF-2026-ARXIV-2605-28691:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28691:end -->

<!-- books-review:SF-2026-ARXIV-2605-28699:start -->
<!-- existing:SF-2026-ARXIV-2605-28699:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28699:end -->
<!-- delta:SF-2026-ARXIV-2605-28699:start -->We introduce TRACER, a turn-level reinforcement framework for cooperative multi-LLM reasoning.<!-- delta:SF-2026-ARXIV-2605-28699:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28699:end -->

<!-- books-review:SF-2026-ARXIV-2605-28704:start -->
<!-- existing:SF-2026-ARXIV-2605-28704:start -->已顺读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 的 20 个 H2 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；当前 owner 负责 `INFER-TENSORRT-LLM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`4c19b842b8e2ddb31cc4681c31e5484defce4f9769950473cc31a5afa61e338a`；adjacent=`books/part-05-inference-system/48-speculative-decoding.md, books/part-05-inference-system/50-vllm.md`。<!-- existing:SF-2026-ARXIV-2605-28704:end -->
<!-- delta:SF-2026-ARXIV-2605-28704:start -->In this work, we study the expressive power of floating-point neural networks under generalized floating-point execution semantics, including arbitrary reduction orders and inexact activation implementations with bounded ulp errors.<!-- delta:SF-2026-ARXIV-2605-28704:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28704:end -->

<!-- books-review:SF-2026-ARXIV-2605-28721:start -->
<!-- existing:SF-2026-ARXIV-2605-28721:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28721:end -->
<!-- delta:SF-2026-ARXIV-2605-28721:start -->We study this question on BrowseComp with three diagnostics.<!-- delta:SF-2026-ARXIV-2605-28721:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28721:end -->

<!-- books-review:SF-2026-ARXIV-2605-28726:start -->
<!-- existing:SF-2026-ARXIV-2605-28726:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28726:end -->
<!-- delta:SF-2026-ARXIV-2605-28726:start -->We discover that VLA architectures fail in fundamentally different, predictable ways at the motor-command level.<!-- delta:SF-2026-ARXIV-2605-28726:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28726:end -->

<!-- books-review:SF-2026-ARXIV-2605-28732:start -->
<!-- existing:SF-2026-ARXIV-2605-28732:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文已存在该 exact family trace，故不重复写入。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28732:end -->
<!-- delta:SF-2026-ARXIV-2605-28732:start -->In this work, we study the new problem of error tracing and attribution in LLM memory systems.<!-- delta:SF-2026-ARXIV-2605-28732:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28732:end -->

<!-- books-review:SF-2026-ARXIV-2605-28742:start -->
<!-- existing:SF-2026-ARXIV-2605-28742:start -->已顺读 owner `books/part-07-agent/80-reflection.md` 的 14 个 H2 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']；当前 owner 负责 `AGENT-REFLECTION` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08`；adjacent=`books/part-07-agent/79-planning.md, books/part-07-agent/81-workflow.md`。<!-- existing:SF-2026-ARXIV-2605-28742:end -->
<!-- delta:SF-2026-ARXIV-2605-28742:start -->To address this challenge, we introduce Contrastive Reflection (CORE), a non-parametric learning algorithm that compares past reasoning traces to generate insights: short natural-language descriptions of reasoning strategies and constraints that capture differences between successful and unsuccessful problem attempts.<!-- delta:SF-2026-ARXIV-2605-28742:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28742:end -->

<!-- books-review:SF-2026-ARXIV-2605-28751:start -->
<!-- existing:SF-2026-ARXIV-2605-28751:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28751:end -->
<!-- delta:SF-2026-ARXIV-2605-28751:start -->We study this question in RL for competitive programming, where hidden unit tests under time and memory limits enforce both functional correctness and computational efficiency.<!-- delta:SF-2026-ARXIV-2605-28751:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28751:end -->

<!-- books-review:SF-2026-ARXIV-2605-28760:start -->
<!-- existing:SF-2026-ARXIV-2605-28760:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；zeroth-order fine-tuning 改变 optimizer/update runtime 而非 LoRA 参数化，最终 owner 纠正为 `TRAIN-PRETRAINING`。 Owner sha256=`13847888f3fd7c316fbde2e81ffb6ee73c56f171882d2f70e7023fa3c36c7b21`；adjacent=`books/part-04-training-system/27-data.md, books/part-04-training-system/29-sft.md`。<!-- existing:SF-2026-ARXIV-2605-28760:end -->
<!-- delta:SF-2026-ARXIV-2605-28760:start -->We show that LLM ZO fine-tuning is an inference-dominated workload and execute its repeated scoring phase through a serving runtime.<!-- delta:SF-2026-ARXIV-2605-28760:end --> Decision=`Integrate`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28760:end -->

<!-- books-review:SF-2026-ARXIV-2605-28764:start -->
<!-- existing:SF-2026-ARXIV-2605-28764:start -->已顺读 owner `books/part-07-agent/82-multi-agent.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；当前 owner 负责 `AGENT-MULTI-AGENT` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`6baaf2ff0a94d45eb53c487410a43311c6b2a63c2a88e71066c8d2b107388431`；adjacent=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-28764:end -->
<!-- delta:SF-2026-ARXIV-2605-28764:start -->We propose SwarmHarness, a decentralised protocol in which HarnessAPI skill nodes self-organise into a compute swarm without any central authority.<!-- delta:SF-2026-ARXIV-2605-28764:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28764:end -->

<!-- books-review:SF-2026-ARXIV-2605-28773:start -->
<!-- existing:SF-2026-ARXIV-2605-28773:start -->已顺读 owner `books/part-07-agent/77-memory.md` 的 18 个 H2 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；当前 owner 负责 `AGENT-MEMORY` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`1203abfc27ba86bbe0de885e58c1574da193e6a85b540cfdf2ac069997f7203d`；adjacent=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-28773:end -->
<!-- delta:SF-2026-ARXIV-2605-28773:start -->To address this, we propose FluxMem, a connectivity-evolving memory framework that models memory as a heterogeneous graph and progressively refines its topology through three stages: initial connection formation, feedback-driven refinement, and long-term consolidation.<!-- delta:SF-2026-ARXIV-2605-28773:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28773:end -->

<!-- books-review:SF-2026-ARXIV-2605-28774:start -->
<!-- existing:SF-2026-ARXIV-2605-28774:start -->已顺读 owner `books/part-04-training-system/33-grpo.md` 的 23 个 H2 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']；当前 owner 负责 `TRAIN-GRPO` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`b145ccd4ff83a1417182006dcad9c4927bb9386dc883a6c5df4307f4f7bfbdd7`；adjacent=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-28774:end -->
<!-- delta:SF-2026-ARXIV-2605-28774:start -->We propose AXPO (Agent eXplorative Policy Optimization): for each all-wrong tool-using subgroup, AXPO fixes the thinking prefix and resamples the tool call and its continuation, paired with uncertainty-based prefix selection.<!-- delta:SF-2026-ARXIV-2605-28774:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28774:end -->

<!-- books-review:SF-2026-ARXIV-2605-28778:start -->
<!-- existing:SF-2026-ARXIV-2605-28778:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28778:end -->
<!-- delta:SF-2026-ARXIV-2605-28778:start -->We conduct the first systematic study of this question, formalizing _marker internal confidence_ (MIC) as the estimated intrinsic confidence a model associates with a specific epistemic marker in a given task domain.<!-- delta:SF-2026-ARXIV-2605-28778:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28778:end -->

<!-- books-review:SF-2026-ARXIV-2605-28787:start -->
<!-- existing:SF-2026-ARXIV-2605-28787:start -->已顺读 owner `books/part-07-agent/76-rag.md` 的 17 个 H2 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；当前 owner 负责 `AGENT-RAG` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83`；adjacent=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-28787:end -->
<!-- delta:SF-2026-ARXIV-2605-28787:start -->We present a comparative analysis of agentic data retrieval across two distinct environments: a Baseline Agent searching billions of open-web documents, and a Semantic Agent leveraging a corpus of 90 million datasets using schema$.$org.<!-- delta:SF-2026-ARXIV-2605-28787:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28787:end -->

<!-- books-review:SF-2026-ARXIV-2605-28803:start -->
<!-- existing:SF-2026-ARXIV-2605-28803:start -->已顺读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的 20 个 H2 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md', 'books/part-04-training-system/27-data.md']；当前 owner 负责 `MULTIMODAL-EMBODIED-VLA` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`36552034b7fe336a6aa29e98a34678a24f6980cbbe72b183aead5e116188972e`；adjacent=`books/part-03-multimodal-world-models/25-multimodal-world-models.md, books/part-04-training-system/27-data.md`。<!-- existing:SF-2026-ARXIV-2605-28803:end -->
<!-- delta:SF-2026-ARXIV-2605-28803:start -->We present HoloQ-VLA, the first training-free PTQ framework that compresses both the language backbone and the entire diffusion action head to uniform W4A4 precision without mixed-precision allocation.<!-- delta:SF-2026-ARXIV-2605-28803:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28803:end -->

<!-- books-review:SF-2026-ARXIV-2605-28805:start -->
<!-- existing:SF-2026-ARXIV-2605-28805:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28805:end -->
<!-- delta:SF-2026-ARXIV-2605-28805:start -->In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training.<!-- delta:SF-2026-ARXIV-2605-28805:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28805:end -->

<!-- books-review:SF-2026-ARXIV-2605-28807:start -->
<!-- existing:SF-2026-ARXIV-2605-28807:start -->已顺读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 的 27 个 H2 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；当前 owner 负责 `PLATFORM-EVALUATION-SYSTEM` 的既有演进链。正文没有该 exact family trace；只有未被现有命题表达的长期 delta 才进入 root queue。 Owner sha256=`2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-28807:end -->
<!-- delta:SF-2026-ARXIV-2605-28807:start -->We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline.<!-- delta:SF-2026-ARXIV-2605-28807:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28807:end -->

<!-- books-review:SF-2026-ARXIV-2605-28819:start -->
<!-- existing:SF-2026-ARXIV-2605-28819:start -->已顺读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；zeroth-order fine-tuning 改变 optimizer/update runtime 而非 LoRA 参数化，最终 owner 纠正为 `TRAIN-PRETRAINING`。 Owner sha256=`13847888f3fd7c316fbde2e81ffb6ee73c56f171882d2f70e7023fa3c36c7b21`；adjacent=`books/part-04-training-system/29-sft.md, books/part-04-training-system/31-rlhf.md`。<!-- existing:SF-2026-ARXIV-2605-28819:end -->
<!-- delta:SF-2026-ARXIV-2605-28819:start -->We introduce PEFT-Arena, a benchmark that jointly measures downstream performance and general capability retention.<!-- delta:SF-2026-ARXIV-2605-28819:end --> Decision=`No Change — Existing Coverage`；本 lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-28819:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260528-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260528 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260528-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260528-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=117；selected=3；all others retain completed reviews | passed |
| SA-20260528-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1;review:SF-2026-ARXIV-2605-27566 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=718；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260528/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/20260528/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/05/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/05/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-05-28.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
