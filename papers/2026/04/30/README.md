# Daily Research — 2026-04-30

**Research Date:** 2026-04-30

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-04-29 09:00:00 ～ 2026-04-30 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Independent Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；initial-created owner replay 与 exact-v1 Evidence Review 已完成。

## Executive Summary

本次独立重放枚举并逐项闭合 397 个注册 arXiv identity，冻结 46 个 Source Family；pre-denominator closure=351，withdrawn pre-denominator=0。9 个旧候选被迁回正确 owner day，0 个漏检 family 已恢复 exact-v1 全文并完成 Source Review。

DataCite `created` 仅作为 initial DOI registration 的 owner-day proxy；`updated`、v1 Updated 与 current OAI datestamp 只记录 revision provenance，不决定 first-public owner。机制结论只绑定 exact-v1 正文。 本日所有 Books disposition 已有终态。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-04-30 |
| Window End | 2026-04-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260430-CREATED-076b734025b24338 |
| Denominator Frozen At | 2026-09-03T12:36:05+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-04-29T09:00:00+08:00 | 2026-04-30T09:00:00+08:00 | 2026-09-03T12:36:05+08:00 | DataCite prefix 10.48550 initial created-day inventory + registered arXiv categories + exact-v1 identity/body | checked | 397 | SF-2026-ARXIV-2604-25975;SF-2026-ARXIV-2604-26020;SF-2026-ARXIV-2604-26039;SF-2026-ARXIV-2604-26074;SF-2026-ARXIV-2604-26091;SF-2026-ARXIV-2604-26103;SF-2026-ARXIV-2604-26152;SF-2026-ARXIV-2604-26182;SF-2026-ARXIV-2604-26197;SF-2026-ARXIV-2604-26209;SF-2026-ARXIV-2604-26256;SF-2026-ARXIV-2604-26258;SF-2026-ARXIV-2604-26274;SF-2026-ARXIV-2604-26294;SF-2026-ARXIV-2604-26334;SF-2026-ARXIV-2604-26340;SF-2026-ARXIV-2604-26360;SF-2026-ARXIV-2604-26378;SF-2026-ARXIV-2604-26388;SF-2026-ARXIV-2604-26412;SF-2026-ARXIV-2604-26460;SF-2026-ARXIV-2604-26469;SF-2026-ARXIV-2604-26470;SF-2026-ARXIV-2604-26495;SF-2026-ARXIV-2604-26505;SF-2026-ARXIV-2604-26506;SF-2026-ARXIV-2604-26511;SF-2026-ARXIV-2604-26525;SF-2026-ARXIV-2604-26557;SF-2026-ARXIV-2604-26561;SF-2026-ARXIV-2604-26622;SF-2026-ARXIV-2604-26649;SF-2026-ARXIV-2604-26666;SF-2026-ARXIV-2604-26687;SF-2026-ARXIV-2604-26694;SF-2026-ARXIV-2604-26733;SF-2026-ARXIV-2604-26752;SF-2026-ARXIV-2604-26779;SF-2026-ARXIV-2604-26815;SF-2026-ARXIV-2604-26837;SF-2026-ARXIV-2604-26848;SF-2026-ARXIV-2604-26881;SF-2026-ARXIV-2604-26889;SF-2026-ARXIV-2604-26904;SF-2026-ARXIV-2604-26934;SF-2026-ARXIV-2604-26951 | created-day pages=closed; OAI category sets=closed; direct same-day OAI=297 | 2026-04-30T09:00:00+08:00 | coverage:SRC-ARXIV:20260430 | — |

<!-- coverage:SRC-ARXIV:20260430:start -->全量 raw inventory=397；每个 identity 均具有 retained、family-specific closure 或 withdrawn terminal closure。候选 owner 由 initial DataCite created、arXiv ID month、v1 history 与 announcement cadence 共同约束；冲突不由 updated 字段覆盖。<!-- coverage:SRC-ARXIV:20260430:end -->

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
| SF-2026-ARXIV-2604-25975 | arXiv:2604.25975v1 | paper-v1:2604.25975 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-25975 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-25975 | no |
| SF-2026-ARXIV-2604-26020 | arXiv:2604.26020v1 | paper-v1:2604.26020 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26020 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26020 | no |
| SF-2026-ARXIV-2604-26039 | arXiv:2604.26039v1 | paper-v1:2604.26039 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26039 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26039 | no |
| SF-2026-ARXIV-2604-26074 | arXiv:2604.26074v1 | paper-v1:2604.26074 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26074 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26074 | no |
| SF-2026-ARXIV-2604-26091 | arXiv:2604.26091v1 | paper-v1:2604.26091 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26091 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26091 | no |
| SF-2026-ARXIV-2604-26103 | arXiv:2604.26103v1 | paper-v1:2604.26103 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26103 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26103 | no |
| SF-2026-ARXIV-2604-26152 | arXiv:2604.26152v1 | paper-v1:2604.26152 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26152 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26152 | no |
| SF-2026-ARXIV-2604-26182 | arXiv:2604.26182v1 | paper-v1:2604.26182 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26182 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26182 | no |
| SF-2026-ARXIV-2604-26197 | arXiv:2604.26197v1 | paper-v1:2604.26197 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26197 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26197 | no |
| SF-2026-ARXIV-2604-26209 | arXiv:2604.26209v1 | paper-v1:2604.26209 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26209 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26209 | no |
| SF-2026-ARXIV-2604-26256 | arXiv:2604.26256v1 | paper-v1:2604.26256 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26256 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26256 | no |
| SF-2026-ARXIV-2604-26258 | arXiv:2604.26258v1 | paper-v1:2604.26258 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26258 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26258 | no |
| SF-2026-ARXIV-2604-26274 | arXiv:2604.26274v1 | paper-v1:2604.26274 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26274 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26274 | no |
| SF-2026-ARXIV-2604-26294 | arXiv:2604.26294v1 | paper-v1:2604.26294 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26294 | self | — | new_in_window | TRAIN-TENSOR-PARALLEL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26294 | no |
| SF-2026-ARXIV-2604-26334 | arXiv:2604.26334v1 | paper-v1:2604.26334 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26334 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26334 | no |
| SF-2026-ARXIV-2604-26340 | arXiv:2604.26340v1 | paper-v1:2604.26340 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26340 | self | — | new_in_window | TRAIN-LORA | Integrate | books-review:SF-2026-ARXIV-2604-26340 | no |
| SF-2026-ARXIV-2604-26360 | arXiv:2604.26360v1 | paper-v1:2604.26360 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26360 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26360 | no |
| SF-2026-ARXIV-2604-26378 | arXiv:2604.26378v1 | paper-v1:2604.26378 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26378 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26378 | no |
| SF-2026-ARXIV-2604-26388 | arXiv:2604.26388v1 | paper-v1:2604.26388 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26388 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26388 | no |
| SF-2026-ARXIV-2604-26412 | arXiv:2604.26412v1 | paper-v1:2604.26412 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26412 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26412 | no |
| SF-2026-ARXIV-2604-26460 | arXiv:2604.26460v1 | paper-v1:2604.26460 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26460 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26460 | no |
| SF-2026-ARXIV-2604-26469 | arXiv:2604.26469v1 | paper-v1:2604.26469 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26469 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26469 | no |
| SF-2026-ARXIV-2604-26470 | arXiv:2604.26470v1 | paper-v1:2604.26470 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26470 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26470 | no |
| SF-2026-ARXIV-2604-26495 | arXiv:2604.26495v1 | paper-v1:2604.26495 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26495 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26495 | no |
| SF-2026-ARXIV-2604-26505 | arXiv:2604.26505v1 | paper-v1:2604.26505 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26505 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-26505 | no |
| SF-2026-ARXIV-2604-26506 | arXiv:2604.26506v1 | paper-v1:2604.26506 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26506 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26506 | no |
| SF-2026-ARXIV-2604-26511 | arXiv:2604.26511v1 | paper-v1:2604.26511 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26511 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26511 | no |
| SF-2026-ARXIV-2604-26525 | arXiv:2604.26525v1 | paper-v1:2604.26525 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26525 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26525 | no |
| SF-2026-ARXIV-2604-26557 | arXiv:2604.26557v1 | paper-v1:2604.26557 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26557 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26557 | no |
| SF-2026-ARXIV-2604-26561 | arXiv:2604.26561v1 | paper-v1:2604.26561 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26561 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26561 | no |
| SF-2026-ARXIV-2604-26622 | arXiv:2604.26622v1 | paper-v1:2604.26622 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26622 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26622 | no |
| SF-2026-ARXIV-2604-26649 | arXiv:2604.26649v1 | paper-v1:2604.26649 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26649 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26649 | no |
| SF-2026-ARXIV-2604-26666 | arXiv:2604.26666v1 | paper-v1:2604.26666 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26666 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26666 | no |
| SF-2026-ARXIV-2604-26687 | arXiv:2604.26687v1 | paper-v1:2604.26687 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26687 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26687 | no |
| SF-2026-ARXIV-2604-26694 | arXiv:2604.26694v1 | paper-v1:2604.26694 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26694 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26694 | no |
| SF-2026-ARXIV-2604-26733 | arXiv:2604.26733v1 | paper-v1:2604.26733 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26733 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26733 | no |
| SF-2026-ARXIV-2604-26752 | arXiv:2604.26752v1 | paper-v1:2604.26752 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26752 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26752 | no |
| SF-2026-ARXIV-2604-26779 | arXiv:2604.26779v1 | paper-v1:2604.26779 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26779 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26779 | no |
| SF-2026-ARXIV-2604-26815 | arXiv:2604.26815v1 | paper-v1:2604.26815 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26815 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26815 | no |
| SF-2026-ARXIV-2604-26837 | arXiv:2604.26837v1 | paper-v1:2604.26837 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26837 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26837 | no |
| SF-2026-ARXIV-2604-26848 | arXiv:2604.26848v1 | paper-v1:2604.26848 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26848 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26848 | no |
| SF-2026-ARXIV-2604-26881 | arXiv:2604.26881v1 | paper-v1:2604.26881 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26881 | self | — | new_in_window | PLATFORM-MULTI-TENANT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26881 | no |
| SF-2026-ARXIV-2604-26889 | arXiv:2604.26889v1 | paper-v1:2604.26889 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26889 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26889 | no |
| SF-2026-ARXIV-2604-26904 | arXiv:2604.26904v1 | paper-v1:2604.26904 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26904 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26904 | no |
| SF-2026-ARXIV-2604-26934 | arXiv:2604.26934v1 | paper-v1:2604.26934 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26934 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26934 | no |
| SF-2026-ARXIV-2604-26951 | arXiv:2604.26951v1 | paper-v1:2604.26951 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-26951 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26951 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-25975 | RP-07dbf6b412fa22cd | deep | arXiv:2604.25975v1 | SRC-ARXIV@arXiv:2604.25975v1 | arXiv:2604.25975v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.25975v1.html#exact-v1 independent HTML full read) | arXiv:2604.25975v1 §Evaluation — Evaluation Contract — 4.2 Results on Long-context Benchmark (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.25975v1.html#exact-v1 independent HTML full read) | arXiv:2604.25975v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.25975v1.html#exact-v1 independent HTML full read) | arXiv:2604.25975v1 §Artifact / Access — Artifact / Access — Appendix C More experimental results (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.25975v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-25975 | complete |
| SF-2026-ARXIV-2604-26020 | RP-bd6cbe1b7ff3586b | deep | arXiv:2604.26020v1 | SRC-ARXIV@arXiv:2604.26020v1 | arXiv:2604.26020v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26020v1.html#exact-v1 independent HTML full read) | arXiv:2604.26020v1 §Evaluation — Evaluation Contract — 5.2. Evaluation 2: Usability Critique Analysis (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26020v1.html#exact-v1 independent HTML full read) | arXiv:2604.26020v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6.3. Limitations & Future Work (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26020v1.html#exact-v1 independent HTML full read) | arXiv:2604.26020v1 §Artifact / Access — Artifact / Access — Appendix B Trace Generation Prompts (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26020v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26020 | complete |
| SF-2026-ARXIV-2604-26039 | RP-5906be5e3a78fc1c | deep | arXiv:2604.26039v1 | SRC-ARXIV@arXiv:2604.26039v1 | arXiv:2604.26039v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26039v1.html#exact-v1 independent HTML full read) | arXiv:2604.26039v1 §Evaluation — Evaluation Contract — V Evaluation (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26039v1.html#exact-v1 independent HTML full read) | arXiv:2604.26039v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VII Conclusion (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26039v1.html#exact-v1 independent HTML full read) | arXiv:2604.26039v1 §Artifact / Access — Artifact / Access — I Introduction (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26039v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26039 | complete |
| SF-2026-ARXIV-2604-26074 | RP-6ada34adfcaeb022 | deep | arXiv:2604.26074v1 | SRC-ARXIV@arXiv:2604.26074v1 | arXiv:2604.26074v1 §Method / Identity — Artifact / Access — 5 Implementation (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26074v1.html#exact-v1 independent HTML full read) | arXiv:2604.26074v1 §Evaluation — Evaluation Contract — 6 Evaluation (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26074v1.html#exact-v1 independent HTML full read) | arXiv:2604.26074v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 2.3 Limitation of Copy-Based Offloading (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26074v1.html#exact-v1 independent HTML full read) | arXiv:2604.26074v1 §Artifact / Access — Artifact / Access — 5 Implementation (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26074v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26074 | complete |
| SF-2026-ARXIV-2604-26091 | RP-e1ed63f7128f958e | deep | arXiv:2604.26091v1 | SRC-ARXIV@arXiv:2604.26091v1 | arXiv:2604.26091v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26091v1.html#exact-v1 independent HTML full read) | arXiv:2604.26091v1 §Evaluation — Evaluation Contract — 7 Related Work (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26091v1.html#exact-v1 independent HTML full read) | arXiv:2604.26091v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 9 Conclusion (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26091v1.html#exact-v1 independent HTML full read) | arXiv:2604.26091v1 §Artifact / Access — Artifact / Access — Appendix A Metric and Figure Data (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26091v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26091 | complete |
| SF-2026-ARXIV-2604-26103 | RP-3fead8c8ec92dea8 | deep | arXiv:2604.26103v1 | SRC-ARXIV@arXiv:2604.26103v1 | arXiv:2604.26103v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26103v1.html#exact-v1 independent HTML full read) | arXiv:2604.26103v1 §Evaluation — Evaluation Contract — 7. Experiments (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26103v1.html#exact-v1 independent HTML full read) | arXiv:2604.26103v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 3.3. Limitations of Prior PIM/PNM Proposals (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26103v1.html#exact-v1 independent HTML full read) | arXiv:2604.26103v1 §Artifact / Access — Artifact / Access — Abstract. (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26103v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26103 | complete |
| SF-2026-ARXIV-2604-26152 | RP-0af136616bcc63d2 | deep | arXiv:2604.26152v1 | SRC-ARXIV@arXiv:2604.26152v1 | arXiv:2604.26152v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26152v1.html#exact-v1 independent HTML full read) | arXiv:2604.26152v1 §Evaluation — Evaluation Contract — Gap 2: Unified Evaluation Benchmarks. (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26152v1.html#exact-v1 independent HTML full read) | arXiv:2604.26152v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26152v1.html#exact-v1 independent HTML full read) | arXiv:2604.26152v1 §Artifact / Access — Artifact / Access — Technical Approach. (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26152v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26152 | complete |
| SF-2026-ARXIV-2604-26182 | RP-411e52ec40dd6b8c | deep | arXiv:2604.26182v1 | SRC-ARXIV@arXiv:2604.26182v1 | https://arxiv.org/html/2604.26182v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26182v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26182v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26182v1 ; https://arxiv.org/html/2604.26182v1 | claim:SF-2026-ARXIV-2604-26182 | complete |
| SF-2026-ARXIV-2604-26197 | RP-1f2bda21516578de | deep | arXiv:2604.26197v1 | SRC-ARXIV@arXiv:2604.26197v1 | arXiv:2604.26197v1 §Method / Identity — Artifact / Access — 4.4. Implementation Details (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26197v1.html#exact-v1 independent HTML full read) | arXiv:2604.26197v1 §Evaluation — Evaluation Contract — 4.5.2. Quality Analysis. (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26197v1.html#exact-v1 independent HTML full read) | arXiv:2604.26197v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 4.8. Privacy Discussion (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26197v1.html#exact-v1 independent HTML full read) | arXiv:2604.26197v1 §Artifact / Access — Artifact / Access — 4.4. Implementation Details (source artifact papers/2026/04/_sources/daily-20260429/exact-v1/2604.26197v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26197 | complete |
| SF-2026-ARXIV-2604-26209 | RP-1fa50c3c6a7725e2 | deep | arXiv:2604.26209v1 | SRC-ARXIV@arXiv:2604.26209v1 | arXiv:2604.26209v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26209v1.html#exact-v1 independent HTML full read) | arXiv:2604.26209v1 §Evaluation — Evaluation Contract — Human evaluation results are aligned with the LLM judge preference on Amazon Reviews. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26209v1.html#exact-v1 independent HTML full read) | arXiv:2604.26209v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26209v1.html#exact-v1 independent HTML full read) | arXiv:2604.26209v1 §Artifact / Access — Artifact / Access — Appendix A The HPD Algorithm (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26209v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26209 | complete |
| SF-2026-ARXIV-2604-26256 | RP-ffde31c58529c367 | deep | arXiv:2604.26256v1 | SRC-ARXIV@arXiv:2604.26256v1 | arXiv:2604.26256v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26256v1.html#exact-v1 independent HTML full read) | arXiv:2604.26256v1 §Evaluation — Evaluation Contract — 5 Experiments and Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26256v1.html#exact-v1 independent HTML full read) | arXiv:2604.26256v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7 Limitations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26256v1.html#exact-v1 independent HTML full read) | arXiv:2604.26256v1 §Artifact / Access — Artifact / Access — 3.2 Skewed Generation Problem (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26256v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26256 | complete |
| SF-2026-ARXIV-2604-26258 | RP-7935e8ad273f98c2 | deep | arXiv:2604.26258v1 | SRC-ARXIV@arXiv:2604.26258v1 | arXiv:2604.26258v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26258v1.html#exact-v1 independent HTML full read) | arXiv:2604.26258v1 §Evaluation — Evaluation Contract — 3.1 Experimental Setup (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26258v1.html#exact-v1 independent HTML full read) | arXiv:2604.26258v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 4 Discussion & Limitations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26258v1.html#exact-v1 independent HTML full read) | arXiv:2604.26258v1 §Artifact / Access — Artifact / Access — Appendix A Meta LLM Prompts (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26258v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26258 | complete |
| SF-2026-ARXIV-2604-26274 | RP-70cf7fc7ba9eee14 | deep | arXiv:2604.26274v1 | SRC-ARXIV@arXiv:2604.26274v1 | arXiv:2604.26274v1 §Method / Identity — Artifact / Access — 6 Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26274v1.html#exact-v1 independent HTML full read) | arXiv:2604.26274v1 §Evaluation — Evaluation Contract — 7.1 Experimental Setup (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26274v1.html#exact-v1 independent HTML full read) | arXiv:2604.26274v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 9 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26274v1.html#exact-v1 independent HTML full read) | arXiv:2604.26274v1 §Artifact / Access — Artifact / Access — 6 Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26274v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26274 | complete |
| SF-2026-ARXIV-2604-26294 | RP-16e2e10912cc7297 | deep | arXiv:2604.26294v1 | SRC-ARXIV@arXiv:2604.26294v1 | arXiv:2604.26294v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26294v1.html#exact-v1 independent HTML full read) | arXiv:2604.26294v1 §Evaluation — Evaluation Contract — VI Results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26294v1.html#exact-v1 independent HTML full read) | arXiv:2604.26294v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VII Discussion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26294v1.html#exact-v1 independent HTML full read) | arXiv:2604.26294v1 §Artifact / Access — Artifact / Access — Appendix C Reference Model Configuration (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26294v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26294 | complete |
| SF-2026-ARXIV-2604-26334 | RP-73b640f33f918f6e | deep | arXiv:2604.26334v1 | SRC-ARXIV@arXiv:2604.26334v1 | https://arxiv.org/html/2604.26334v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26334v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26334v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.26334v1 ; https://arxiv.org/html/2604.26334v1 | claim:SF-2026-ARXIV-2604-26334 | complete |
| SF-2026-ARXIV-2604-26340 | RP-4b3223e4e055fe96 | deep | arXiv:2604.26340v1 | SRC-ARXIV@arXiv:2604.26340v1 | https://arxiv.org/html/2604.26340v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26340v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26340v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.26340v1 ; https://arxiv.org/html/2604.26340v1 | claim:SF-2026-ARXIV-2604-26340 | complete |
| SF-2026-ARXIV-2604-26360 | RP-be66af48aee49d7f | deep | arXiv:2604.26360v1 | SRC-ARXIV@arXiv:2604.26360v1 | https://arxiv.org/html/2604.26360v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26360v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26360v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26360v1 ; https://arxiv.org/html/2604.26360v1 | claim:SF-2026-ARXIV-2604-26360 | complete |
| SF-2026-ARXIV-2604-26378 | RP-aa7fe021a1507cc9 | deep | arXiv:2604.26378v1 | SRC-ARXIV@arXiv:2604.26378v1 | arXiv:2604.26378v1 §Method / Identity — Artifact / Access — Implementation details. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26378v1.html#exact-v1 independent HTML full read) | arXiv:2604.26378v1 §Evaluation — Evaluation Contract — 4.2 Main results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26378v1.html#exact-v1 independent HTML full read) | arXiv:2604.26378v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations and Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26378v1.html#exact-v1 independent HTML full read) | arXiv:2604.26378v1 §Artifact / Access — Artifact / Access — Implementation details. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26378v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26378 | complete |
| SF-2026-ARXIV-2604-26388 | RP-fae25736aa76ed8a | deep | arXiv:2604.26388v1 | SRC-ARXIV@arXiv:2604.26388v1 | arXiv:2604.26388v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26388v1.html#exact-v1 independent HTML full read) | arXiv:2604.26388v1 §Evaluation — Method / Identity — IV-B Evaluation Methodology (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26388v1.html#exact-v1 independent HTML full read) | arXiv:2604.26388v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VI Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26388v1.html#exact-v1 independent HTML full read) | arXiv:2604.26388v1 §Artifact / Access — Artifact / Access — Appendix A SplitFT Fine-Tuning Workflow (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26388v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26388 | complete |
| SF-2026-ARXIV-2604-26412 | RP-33d05a41061f7362 | deep | arXiv:2604.26412v1 | SRC-ARXIV@arXiv:2604.26412v1 | arXiv:2604.26412v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26412v1.html#exact-v1 independent HTML full read) | arXiv:2604.26412v1 §Evaluation — Evaluation Contract — Results. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26412v1.html#exact-v1 independent HTML full read) | arXiv:2604.26412v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26412v1.html#exact-v1 independent HTML full read) | arXiv:2604.26412v1 §Artifact / Access — Artifact / Access — Appendix A Training Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26412v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26412 | complete |
| SF-2026-ARXIV-2604-26460 | RP-0a480a3a6ae8ed2f | deep | arXiv:2604.26460v1 | SRC-ARXIV@arXiv:2604.26460v1 | arXiv:2604.26460v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26460v1.html#exact-v1 independent HTML full read) | arXiv:2604.26460v1 §Evaluation — Evaluation Contract — Personalization benchmarks. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26460v1.html#exact-v1 independent HTML full read) | arXiv:2604.26460v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26460v1.html#exact-v1 independent HTML full read) | arXiv:2604.26460v1 §Artifact / Access — Artifact / Access — Abstract (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26460v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26460 | complete |
| SF-2026-ARXIV-2604-26469 | RP-b6d88774ded024b3 | deep | arXiv:2604.26469v1 | SRC-ARXIV@arXiv:2604.26469v1 | https://arxiv.org/html/2604.26469v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26469v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26469v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26469v1 ; https://arxiv.org/html/2604.26469v1 | claim:SF-2026-ARXIV-2604-26469 | complete |
| SF-2026-ARXIV-2604-26470 | RP-43447f368642fbb1 | deep | arXiv:2604.26470v1 | SRC-ARXIV@arXiv:2604.26470v1 | https://arxiv.org/html/2604.26470v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26470v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26470v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.26470v1 ; https://arxiv.org/html/2604.26470v1 | claim:SF-2026-ARXIV-2604-26470 | complete |
| SF-2026-ARXIV-2604-26495 | RP-b4d6177db723a7bb | deep | arXiv:2604.26495v1 | SRC-ARXIV@arXiv:2604.26495v1 | https://arxiv.org/html/2604.26495v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26495v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26495v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26495v1 ; https://arxiv.org/html/2604.26495v1 | claim:SF-2026-ARXIV-2604-26495 | complete |
| SF-2026-ARXIV-2604-26505 | RP-95cb53f1dd8c8a43 | deep | arXiv:2604.26505v1 | SRC-ARXIV@arXiv:2604.26505v1 | https://arxiv.org/html/2604.26505v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26505v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26505v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26505v1 ; https://arxiv.org/html/2604.26505v1 | claim:SF-2026-ARXIV-2604-26505 | complete |
| SF-2026-ARXIV-2604-26506 | RP-324a52c5e4617184 | deep | arXiv:2604.26506v1 | SRC-ARXIV@arXiv:2604.26506v1 | arXiv:2604.26506v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26506v1.html#exact-v1 independent HTML full read) | arXiv:2604.26506v1 §Evaluation — Evaluation Contract — 4 Experiments (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26506v1.html#exact-v1 independent HTML full read) | arXiv:2604.26506v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26506v1.html#exact-v1 independent HTML full read) | arXiv:2604.26506v1 §Artifact / Access — Artifact / Access — Appendix A Analysis of Attack Effectiveness Across Paper Quality Tiers (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26506v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26506 | complete |
| SF-2026-ARXIV-2604-26511 | RP-a431e203b38962ba | deep | arXiv:2604.26511v1 | SRC-ARXIV@arXiv:2604.26511v1 | arXiv:2604.26511v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26511v1.html#exact-v1 independent HTML full read) | arXiv:2604.26511v1 §Evaluation — Method / Identity — 3 Tatemae: Evaluation Framework (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26511v1.html#exact-v1 independent HTML full read) | arXiv:2604.26511v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Discussion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26511v1.html#exact-v1 independent HTML full read) | arXiv:2604.26511v1 §Artifact / Access — Artifact / Access — Appendix B Models and Compute Resources (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26511v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26511 | complete |
| SF-2026-ARXIV-2604-26525 | RP-1cf8d0a01b22980c | deep | arXiv:2604.26525v1 | SRC-ARXIV@arXiv:2604.26525v1 | https://arxiv.org/html/2604.26525v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26525v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26525v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.26525v1 ; https://arxiv.org/html/2604.26525v1 | claim:SF-2026-ARXIV-2604-26525 | complete |
| SF-2026-ARXIV-2604-26557 | RP-7f3a65d99a3e297c | deep | arXiv:2604.26557v1 | SRC-ARXIV@arXiv:2604.26557v1 | arXiv:2604.26557v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26557v1.html#exact-v1 independent HTML full read) | arXiv:2604.26557v1 §Evaluation — Evaluation Contract — V-A Experimental Setup (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26557v1.html#exact-v1 independent HTML full read) | arXiv:2604.26557v1 §Scope and Limitations — Evidence Proves / Does Not Prove — VII Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26557v1.html#exact-v1 independent HTML full read) | arXiv:2604.26557v1 §Artifact / Access — Artifact / Access — V-B LLM Serving Evaluation: Prefill and Decode (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26557v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26557 | complete |
| SF-2026-ARXIV-2604-26561 | RP-59b48e8679fe9668 | deep | arXiv:2604.26561v1 | SRC-ARXIV@arXiv:2604.26561v1 | arXiv:2604.26561v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26561v1.html#exact-v1 independent HTML full read) | arXiv:2604.26561v1 §Evaluation — Evaluation Contract — 3.2 Phase 2: Independent Evaluation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26561v1.html#exact-v1 independent HTML full read) | arXiv:2604.26561v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 8 Limitations and Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26561v1.html#exact-v1 independent HTML full read) | arXiv:2604.26561v1 §Artifact / Access — Artifact / Access — Appendix A Discrete Values of First-Choice Concentration (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26561v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26561 | complete |
| SF-2026-ARXIV-2604-26622 | RP-88c06b68c594c2d1 | deep | arXiv:2604.26622v1 | SRC-ARXIV@arXiv:2604.26622v1 | arXiv:2604.26622v1 §Method / Identity — Artifact / Access — Appendix A More Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26622v1.html#exact-v1 independent HTML full read) | arXiv:2604.26622v1 §Evaluation — Evaluation Contract — 6.2 Main Results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26622v1.html#exact-v1 independent HTML full read) | arXiv:2604.26622v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Limitations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26622v1.html#exact-v1 independent HTML full read) | arXiv:2604.26622v1 §Artifact / Access — Artifact / Access — Appendix A More Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26622v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26622 | complete |
| SF-2026-ARXIV-2604-26649 | RP-bd1e9932e66d600f | deep | arXiv:2604.26649v1 | SRC-ARXIV@arXiv:2604.26649v1 | arXiv:2604.26649v1 §Method / Identity — Artifact / Access — 5.5. Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26649v1.html#exact-v1 independent HTML full read) | arXiv:2604.26649v1 §Evaluation — Evaluation Contract — 6.2. Efficiency Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26649v1.html#exact-v1 independent HTML full read) | arXiv:2604.26649v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7.5. Limitations (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26649v1.html#exact-v1 independent HTML full read) | arXiv:2604.26649v1 §Artifact / Access — Artifact / Access — 5.5. Implementation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26649v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26649 | complete |
| SF-2026-ARXIV-2604-26666 | RP-c8b2604b085a4679 | deep | arXiv:2604.26666v1 | SRC-ARXIV@arXiv:2604.26666v1 | arXiv:2604.26666v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26666v1.html#exact-v1 independent HTML full read) | arXiv:2604.26666v1 §Evaluation — Evaluation Contract — 5.2. Evaluation Results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26666v1.html#exact-v1 independent HTML full read) | arXiv:2604.26666v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 7. Conclusion and Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26666v1.html#exact-v1 independent HTML full read) | arXiv:2604.26666v1 §Artifact / Access — Artifact / Access — 1. Introduction (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26666v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26666 | complete |
| SF-2026-ARXIV-2604-26687 | RP-406c927eac0d9958 | deep | arXiv:2604.26687v1 | SRC-ARXIV@arXiv:2604.26687v1 | arXiv:2604.26687v1 §Method / Identity — Artifact / Access — 5. Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26687v1.html#exact-v1 independent HTML full read) | arXiv:2604.26687v1 §Evaluation — Evaluation Contract — 6.3. Behavior and Goodput Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26687v1.html#exact-v1 independent HTML full read) | arXiv:2604.26687v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 9. Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26687v1.html#exact-v1 independent HTML full read) | arXiv:2604.26687v1 §Artifact / Access — Artifact / Access — 5. Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26687v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26687 | complete |
| SF-2026-ARXIV-2604-26694 | RP-3f4f7fe7f4ce2077 | deep | arXiv:2604.26694v1 | SRC-ARXIV@arXiv:2604.26694v1 | arXiv:2604.26694v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26694v1.html#exact-v1 independent HTML full read) | arXiv:2604.26694v1 §Evaluation — Evaluation Contract — 4 Experiments (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26694v1.html#exact-v1 independent HTML full read) | arXiv:2604.26694v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Appendix E Limitations and Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26694v1.html#exact-v1 independent HTML full read) | arXiv:2604.26694v1 §Artifact / Access — Artifact / Access — Appendix A Detailed Algorithms (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26694v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26694 | complete |
| SF-2026-ARXIV-2604-26733 | RP-f12c64d5291893de | deep | arXiv:2604.26733v1 | SRC-ARXIV@arXiv:2604.26733v1 | arXiv:2604.26733v1 §Method / Identity — Artifact / Access — 4.4.1 Implementation details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26733v1.html#exact-v1 independent HTML full read) | arXiv:2604.26733v1 §Evaluation — Evaluation Contract — 4.4.2 Results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26733v1.html#exact-v1 independent HTML full read) | arXiv:2604.26733v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26733v1.html#exact-v1 independent HTML full read) | arXiv:2604.26733v1 §Artifact / Access — Artifact / Access — 4.4.1 Implementation details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26733v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26733 | complete |
| SF-2026-ARXIV-2604-26752 | RP-bb460239db6588d5 | deep | arXiv:2604.26752v1 | SRC-ARXIV@arXiv:2604.26752v1 | arXiv:2604.26752v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26752v1.html#exact-v1 independent HTML full read) | arXiv:2604.26752v1 §Evaluation — Evaluation Contract — 3.3 ImageMining: A Self-Collected Vision-Centric Deep Search Benchmark (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26752v1.html#exact-v1 independent HTML full read) | arXiv:2604.26752v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 2.2 Multimodal Multi-Token Prediction (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26752v1.html#exact-v1 independent HTML full read) | arXiv:2604.26752v1 §Artifact / Access — Artifact / Access — 2.1 CogViT Vision Encoder (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26752v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26752 | complete |
| SF-2026-ARXIV-2604-26779 | RP-56c764a17543b2ab | deep | arXiv:2604.26779v1 | SRC-ARXIV@arXiv:2604.26779v1 | arXiv:2604.26779v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26779v1.html#exact-v1 independent HTML full read) | arXiv:2604.26779v1 §Evaluation — Evaluation Contract — 3.2 Main results (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26779v1.html#exact-v1 independent HTML full read) | arXiv:2604.26779v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 6 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26779v1.html#exact-v1 independent HTML full read) | arXiv:2604.26779v1 §Artifact / Access — Artifact / Access — 1 Introduction (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26779v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26779 | complete |
| SF-2026-ARXIV-2604-26815 | RP-c57b80f86c4b79cc | deep | arXiv:2604.26815v1 | SRC-ARXIV@arXiv:2604.26815v1 | https://arxiv.org/html/2604.26815v1 §Method/Architecture (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26815v1 §Evaluation/Experiments (official exact-v1 rendered full read) | https://arxiv.org/html/2604.26815v1 §Limitations/Discussion plus disclosed evaluation scope | https://arxiv.org/abs/2604.26815v1 ; https://arxiv.org/html/2604.26815v1 | claim:SF-2026-ARXIV-2604-26815 | complete |
| SF-2026-ARXIV-2604-26837 | RP-5818c9d02e945a56 | deep | arXiv:2604.26837v1 | SRC-ARXIV@arXiv:2604.26837v1 | arXiv:2604.26837v1 §Method / Identity — Artifact / Access — 5.5. Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26837v1.html#exact-v1 independent HTML full read) | arXiv:2604.26837v1 §Evaluation — Evaluation Contract — 6. Evaluation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26837v1.html#exact-v1 independent HTML full read) | arXiv:2604.26837v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 8. Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26837v1.html#exact-v1 independent HTML full read) | arXiv:2604.26837v1 §Artifact / Access — Artifact / Access — 5.5. Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26837v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26837 | complete |
| SF-2026-ARXIV-2604-26848 | RP-ac26eaa5cd82f0f6 | deep | arXiv:2604.26848v1 | SRC-ARXIV@arXiv:2604.26848v1 | arXiv:2604.26848v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26848v1.html#exact-v1 independent HTML full read) | arXiv:2604.26848v1 §Evaluation — Evaluation Contract — 4 Experiment (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26848v1.html#exact-v1 independent HTML full read) | arXiv:2604.26848v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26848v1.html#exact-v1 independent HTML full read) | arXiv:2604.26848v1 §Artifact / Access — Artifact / Access — A.3 Pseudocode of STARRY (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26848v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26848 | complete |
| SF-2026-ARXIV-2604-26881 | RP-16e49ed672e0de5d | deep | arXiv:2604.26881v1 | SRC-ARXIV@arXiv:2604.26881v1 | arXiv:2604.26881v1 §Method / Identity — Artifact / Access — 4.1. Proof-of-Concept Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26881v1.html#exact-v1 independent HTML full read) | arXiv:2604.26881v1 §Evaluation — Evaluation Contract — 4.2. Experimental Methodology (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26881v1.html#exact-v1 independent HTML full read) | arXiv:2604.26881v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 5. Discussion & Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26881v1.html#exact-v1 independent HTML full read) | arXiv:2604.26881v1 §Artifact / Access — Artifact / Access — 4.1. Proof-of-Concept Implementation (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26881v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26881 | complete |
| SF-2026-ARXIV-2604-26889 | RP-6e7201e64bcb6b8b | deep | arXiv:2604.26889v1 | SRC-ARXIV@arXiv:2604.26889v1 | https://arxiv.org/html/2604.26889v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26889v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26889v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26889v1 ; https://arxiv.org/html/2604.26889v1 | claim:SF-2026-ARXIV-2604-26889 | complete |
| SF-2026-ARXIV-2604-26904 | RP-1c1b53d468ed3b4f | deep | arXiv:2604.26904v1 | SRC-ARXIV@arXiv:2604.26904v1 | arXiv:2604.26904v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26904v1.html#exact-v1 independent HTML full read) | arXiv:2604.26904v1 §Evaluation — Evaluation Contract — 6.3 Experimental Analysis (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26904v1.html#exact-v1 independent HTML full read) | arXiv:2604.26904v1 §Scope and Limitations — Evidence Proves / Does Not Prove — 8 Conclusion (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26904v1.html#exact-v1 independent HTML full read) | arXiv:2604.26904v1 §Artifact / Access — Artifact / Access — Code-Based Verification. (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26904v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26904 | complete |
| SF-2026-ARXIV-2604-26934 | RP-8614fa344fa8bfe3 | deep | arXiv:2604.26934v1 | SRC-ARXIV@arXiv:2604.26934v1 | https://arxiv.org/html/2604.26934v1 §Method / Architecture / Framework (official exact-v1 full read) | https://arxiv.org/html/2604.26934v1 §Experiments / Evaluation / Results (official exact-v1 full read) | https://arxiv.org/html/2604.26934v1 §Discussion / Limitations / Conclusion (official exact-v1 full read; no broader claim inferred where a dedicated heading is absent) | https://arxiv.org/abs/2604.26934v1 ; https://arxiv.org/html/2604.26934v1 | claim:SF-2026-ARXIV-2604-26934 | complete |
| SF-2026-ARXIV-2604-26951 | RP-c39f2ddb611377fa | deep | arXiv:2604.26951v1 | SRC-ARXIV@arXiv:2604.26951v1 | arXiv:2604.26951v1 §Method / Identity — Mechanism / State Ownership (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26951v1.html#exact-v1 independent HTML full read) | arXiv:2604.26951v1 §Evaluation — Method / Identity — Appendix B Training, Inference, and Evaluation Details (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26951v1.html#exact-v1 independent HTML full read) | arXiv:2604.26951v1 §Scope and Limitations — Evidence Proves / Does Not Prove — Appendix D Limitations and Future Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26951v1.html#exact-v1 independent HTML full read) | arXiv:2604.26951v1 §Artifact / Access — Artifact / Access — Appendix A Related Work (source artifact papers/2026/04/_sources/daily-20260430/exact-v1/2604.26951v1.html#exact-v1 independent HTML full read) | claim:SF-2026-ARXIV-2604-26951 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2604-25975:start -->
#### Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-KV-CACHE` 中该 family 的受限状态。

机制与 state/control owner：This appendix provides an interpretive analysis of representative KV cache eviction methods through the lens of the unified information-theoretic objective introduced in Section 3. In contrast to Appendix A, which presents a formal derivation under a linear-Gaussian surrogate, the goal here is to understand how various heuristic strategies relate to different structural components or approximations of the same information-preservation principle. cache manager 拥有 block identity、placement 与 eviction，scheduler 只引用合法 handle

Evaluation contract：Having established that preserving effective information capacity is strongly associated with downstream performance, we now evaluate the practical benefits of explicitly optimizing this objective through CapKV . We conduct comprehensive experiments on LongBench , a widely used benchmark comprising 16 long-context tasks spanning question answering, summarization, reasoning, and code understanding. Our primary evaluations are performed on Qwen3-8B and Qwen3-14B. Additional evaluations on other model architectures, including Llama3.1-8B ( Team, 2024 ) , Mistral-7B ( Jiang et al., 2023 ) , and Qwen3-4B, are provided in Appendix C.3 . Table 1 summarizes the performance on LongBench. Results are grouped by task category for clarity, with each entry representing the average score over the corresponding datasets. As shown in Table 1 , CapKV consistently achieves superior performance under KV cache compression on both Qwen3-8B and Qwen3-14B. Across all evaluated compression ratios, CapKV outperforms all baseline methods in terms of average score. Similar performance trends are also observed on additional model architectures.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Limitations and Future Work. The proposed capacity-based framework relies on a linear-Gaussian surrogate, which may not fully capture the nonlinear dynamics in Transformers. Exploring richer surrogate models that incorporate controlled nonlinearity remains an important direction for future work. More broadly, our formulation is intended as a unifying lens rather than a closed-form solution, opening up a broader design space for cache eviction beyond the specific approximation adopted in CapKV .。因此若该限制在目标 workload 中触发，不能把 `Rethinking KV Cache Eviction via a Unified Information-Theoretic Objective` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-25975:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-25975:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-25975:end -->

<!-- review:SF-2026-ARXIV-2604-26020:start -->
#### Training Computer Use Agents to Assess the Usability of Graphical User Interfaces

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：In this section we provide an overview of our novel machine learning objective to train computer use agents to i) prioritize exploration of important UI flows and ii) and accurately predict usability scores that match ground-truth preferences. We also describe how we use this approach to train uxCUA and our agent formulation. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：Our first evaluation focused on assessing models’ ability to accurately predict scores in comparison to human-scored ground-truth labels and preference pairs. In this second evaluation, we examine the usability issues (e.g., critiques) identified by uxCUA before it provides its final usability assessment on both plain sites and their defect-augmented counterparts.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：While we show uxCUA outperforms other baselines in our experimental data, we see several avenues for improvement.。因此若该限制在目标 workload 中触发，不能把 `Training Computer Use Agents to Assess the Usability of Graphical User Interfaces` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26020:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26020:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26020:end -->

<!-- review:SF-2026-ARXIV-2604-26039:start -->
#### RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-TENSORRT-LLM` 中该 family 的受限状态。

机制与 state/control owner：Table I summarizes the dispatch strategy of production MoE systems. All share a fundamental limitation: they select configurations from batch size alone, ignoring the routing distribution. Moreover, adding a new optimization dimension (e.g., GROUP_M swizzle) doubles the search space, causing autotuning costs to scale combinatorially . The next section quantifies the performance cost of this static approach. compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径

Evaluation contract：We evaluate RaMP at two levels. Kernel-level evaluation (§ V-B – V-D ) constitutes the primary research evaluation: it validates the cost model’s accuracy, the routing-aware dispatch thesis, the kernel-agnostic property, and the regime theory’s predictions under controlled conditions. End-to-end serving (§ V-E ) validates that kernel-level gains translate to measurable improvements in a production serving stack.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented RaMP, demonstrating that routing-aware kernel dispatch is a fundamental missing axis in MoE inference optimization. A performance-region analysis derived from hardware constants identifies when each optimization helps across all 8 tested architectures. A four-parameter wave cost model achieves 0.93 % 0.93\% mean regret and 1.22 × 1.22\times kernel speedup over static dispatch. Because the model depends only on CTA grid geometry, it is kernel-agnostic : applied to Alpha-MoE with no source changes, it delivers 1.14 × 1.14\times .…。因此若该限制在目标 workload 中触发，不能把 `RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26039:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26039:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26039:end -->

<!-- review:SF-2026-ARXIV-2604-26074:start -->
#### DAK: Direct-Access-Enabled GPU Memory Offloading with Optimal Efficiency for LLM Inference

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-GPU-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：Memory Capacity bottleneck: Modern LLMs require massive memory capacity for both model weights and KV-Cache. For example, a 671B-parameter model in FP16 requires 1.34 TB of memory for weights alone. At the same time, the KV cache scales linearly with both batch size and sequence length, and can easily exceed 100 GB for a 70B model serving a 100K context at a batch size of 16, rapidly exhausting the GPU’s local HBM capacity. memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射

Evaluation contract：We evaluate DAK by answering the following questions: (1) How does DAK compare to baselines across various offloading ratios, hardware architectures, and models? (2) Can DAK enable large models to run efficiently when their memory footprints exceed GPU capacity ( §6.1 )? (3) What is the performance gain of the greedy offloading algorithm? (4) How effective are the TMA optimizations ( §6.2 )?

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Computation Bubbles and Latency Trade-offs. Layer-based coarse-grained prefetching often causes computation bubbles because executing a layer is much faster than fetching its weights ( Fig. 2 (1)). To mask these stalls, systems like FlexGen process multiple micro-batches sequentially on the same layer to maximize weight reuse. However, this throughput optimization severely penalizes latency; forcing micro-batches to synchronize at each layer dramatically increases both time-to-first-token and per-token latencies.。因此若该限制在目标 workload 中触发，不能把 `DAK: Direct-Access-Enabled GPU Memory Offloading with Optimal Efficiency for LLM Inference` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26074:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26074:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26074:end -->

<!-- review:SF-2026-ARXIV-2604-26091:start -->
#### Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-PLATFORM` 中该 family 的受限状态。

机制与 state/control owner：Each vault held user ETH and served as the only execution surface for that user’s agent. Participation was limited to one agent/vault per wallet during the event. The tournament traded 12 memecoin tokens launched at genesis into Uniswap V4 pools. Every swap paid a 2.0% protocol fee and a 0.3% LP fee, for 2.3% total. Agents were polled roughly 12–15 times per hour and all used the same base model: Qwen/Qwen3-235B-A22B-Thinking-2507 at temperature 0.6. The Qwen model card describes this model as a 235B-parameter sparse model with 22B activated parameters and thinking-mode-only operation ( Qwen Team, 2025 ) . Production inference was served through SGLang, a high-performance LLM serving framework ( SGLang Project, 2026 ) . The system recorded 7.5M agent invocations and roughly 70B inference tokens across the 21-day deployment. For the longest-running agents, the record is not a collection of isolated prompts but a continuous sequence of more than 6,000 observations, trades, portfolio updates, memory entries, and user-state reads under a fixed runtime. platform 拥有跨请求 policy、lifecycle 与 human-control state，model 只提出动作

Evaluation contract：Financial LLM systems such as FinGPT, BloombergGPT, TradingGPT, and FinMem evaluate financial language modeling, memory, and trading behavior in backtests or simulations ( Yang et al., 2023 ; Wu et al., 2023 ; Li et al., 2023 ; Yu et al., 2024 ) . These are useful starting points, but finance is unusually hostile to evaluation that stops before execution. The quantitative-finance literature has repeatedly shown that backtests are fragile under multiple testing, selection bias, transaction costs, market impact, and nonstationarity ( Bailey et al., 2017 ; Bailey et al., 2016 ; López de Prado, 2018 ; Almgren and Chriss, 2001 ; Gatheral, 2010 ) . In this domain, a model can look calibrated in a replayed or text-only benchmark and still fail once it must trade through slippage, fees, latency, changing liquidity, and other agents reacting to the same signal. This is why true execution, long-horizon unseen evaluation, and human-in-the-loop mandate formation are not implementation details. They are part of the evaluation target.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The longer horizon is larger than prompt repair. User-to-agent-to-execution traces over autonomous market horizons have already exposed additional opportunities in instruction following, user strategy consistency, tooling, synthetic data, model evaluation, and future training loops. In markets, the agent is not only answering a prompt; it is acting through a changing world, with user capital, execution constraints, and other agents reacting to the same state. That full chain is the object that should be measured and improved.。因此若该限制在目标 workload 中触发，不能把 `Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26091:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26091:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26091:end -->

<!-- review:SF-2026-ARXIV-2604-26103:start -->
#### AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-GPU-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：The 16 cubes form a 2D mesh, with each cube connected to up to four neighbors via die-to-die (D2D) links. Within each cube, as shown in Figure 6 (a), DRAM dies sit atop the logic die and are connected through micro bumps or hybrid-bonding pads. The logic die hosts the HBM PHY and memory controller in its standard region, while our added compute logic is added to enable PNM. memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射

Evaluation contract：Methodology. We combine simulation with real-GPU profiling to evaluate the performance of AMMA. For single-cube performance, we model each HBM-NMP cube using ScaleSim ( Samajdar et al., 2018 ) , an open-source systolic-array simulator. For multi-cube performance, we use AstraSim ( Rashidi et al., 2020 ; Won et al., 2023 ) , replacing its default GPU parameters with our HBM-NMP cube specifications and ingesting the per-cube results from ScaleSim. For GPU baselines, we collect end-to-end latency on an 8×H100 server across a range of batch sizes and sequence lengths. Because Rubin is not yet publicly available, we project its performance by scaling the H100 measurements with Rubin’s published bandwidth and compute specifications while preserving the measured utilization ratios.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：GPU-centric paradigm introduces communication overhead. Existing works such as AttAcc ( Park et al., 2024 ) treat the GPU as the central device for inter-cube communication. This works well for MHA, where sufficient KV heads allow each PIM device to independently handle one head via TP. However, GQA and MLA compress KV heads by 16–128 × \times , so TP alone can no longer partition work across PIM devices (e.g., 64 devices vs. 4 KV heads), forcing context parallelism (CP) along the sequence dimension. CP introduces AllReduce, which is disastrous for GPU-centric PIM. As shown in Figure 5 , AttAcc connects 8 GPUs and 64 PIM devices together via NVLink.…。因此若该限制在目标 workload 中触发，不能把 `AMMA: A Multi-Chiplet Memory-Centric Architecture for Low-Latency 1M Context Attention Serving` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26103:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26103:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26103:end -->

<!-- review:SF-2026-ARXIV-2604-26152:start -->
#### AI Observability for Large Language Model Systems: A Multi-Layer Analysis of Monitoring Approaches from Confidence Calibration to Infrastructure Tracing

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-MONITORING` 中该 family 的受限状态。

机制与 state/control owner：Propositional probes operate in three stages: (1) domain probes classify activations at individual token positions into lexical categories (names, countries, occupations), (2) a Hessian-based algorithm identifies the “binding subspace” where semantically related tokens have high similarity, and (3) a compositional lookup algorithm assembles full propositions (e.g., WorksAs(Greg, nurse) ) from the decoded components. observability owner 版本化 model/agent semantic signals，release owner 决定告警后的动作

Evaluation contract：While AIOpsLab provides evaluation infrastructure for operational agents, there is no equivalent for model-level monitoring. Comparing RLCR’s calibration improvements with propositional probe faithfulness requires a shared task definition, which does not yet exist.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The AI observability landscape in 2026 is characterized by impressive depth at individual layers but limited integration across them. The five papers analyzed in this survey collectively demonstrate that LLM systems can be monitored at every level—from internal activations to GPU kernels—with methods ranging from interpretability probes to non-intrusive hardware tracing. The critical challenge ahead is building unified systems that connect these signals into coherent, actionable operational intelligence.。因此若该限制在目标 workload 中触发，不能把 `AI Observability for Large Language Model Systems: A Multi-Layer Analysis of Monitoring Approaches from Confidence Calibration to Infrastructure Tracing` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26152:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26152:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26152:end -->

<!-- review:SF-2026-ARXIV-2604-26182:start -->
#### Lifting Embodied World Models for Planning and Control

问题、旧路径与约束变化：旧路径把 `Lifting Embodied World Models for Planning and Control` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. 该机制将长期 owner 定位到 `MULTIMODAL-WORLD-MODELS`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：We show that the lifted world model substantially outperforms searching directly in low-level joint space ($3.8\times$ lower mean joint error to the goal pose), while remaining more compute-efficient and generalizing to environments unseen by the policy.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Lifting Embodied World Models for Planning and Control` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26182:start -->只接受 arXiv:2604.26182v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26182:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26182:end -->

<!-- review:SF-2026-ARXIV-2604-26197:start -->
#### Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：To remain adaptive under continuously shifting production query patterns and an evolving document corpus, we introduce a periodic adaptation step that distills historical query workloads into signals for memory construction, rather than relying solely on an LLM’s world knowledge to determine what is important to memorize. Over a sliding window of past queries, the module extracts (i) frequently recurring query patterns and (ii) salient facet names. The query patterns act as priors for the Answerable-QA Generation Agent, guiding it to synthesize answerable questions from node raw data D v D_{v} , while facet names provide optional hints for the Facet Extraction Agent and Summary Agents to emphasize coverage of high-impact attributes during memory construction and tree aggregation. To reduce overfitting, we apply minimum-support thresholds (i.e., only patterns/facets supported by multiple queries are retained); for sensitive production settings, we optionally require human review before deploying updates to the indexing pipeline. memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图

Evaluation contract：Table 2 shows that HLTM outperforms all nine baselines on both query types when using GPT-4o mini . On summary-style queries, HLTM improves Token-F1 and semantic correctness over the strongest baselines (conventional RAG and HippoRAG) by more than 15% 2 2 2 Disclaimer: Results may vary in production environments or with different datasets. . On retrieval-style queries, HLTM achieves the highest F1, exceeding the best baseline (conventional RAG) by more than 10% 3 3 3 Disclaimer: Results may vary in production environments or with different datasets. , indicating a favorable precision–recall trade-off. Appendix D.1 (Table 4 ) reports consistent improvements when using the stronger GPT-5.2 model.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Privacy is a first-class requirement for production memory systems. In HLTM , isolation is enforced structurally: each node is bound to an identity scope (e.g., recruiter, hiring project), and retrieval is restricted to the subtree rooted at that scope. Recruiter-scoped queries can access only that recruiter node and its owned projects; project-scoped queries are further constrained to a single project. This business-aligned hierarchy lets us index once and query at multiple levels without per-level re-indexing or global LLM routing, while preserving strict privacy isolation.。因此若该限制在目标 workload 中触发，不能把 `Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26197:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26197:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26197:end -->

<!-- review:SF-2026-ARXIV-2604-26209:start -->
#### Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-DECODE` 中该 family 的受限状态。

机制与 state/control owner：We first describe the standard autoregressive decoding process from a probabilistic view in Section 4.1 , and then describe our modifications made for HPD in Section 4.2 . We follow with a detailed breakdown of the HPD algorithm in Section 4.3 . decoder runtime 拥有 token frontier、cache identity 与 commit order

Evaluation contract：To validate the LLM judge used for evaluating Amazon Reviews, we conduct a human evaluation experiment on a subset of our results in Appendix D , showing agreement between the human annotators and the LLM judge. In a blind test, human annotators slightly prefer Qwen3-8B HPD over its autoregressive counterpart as well as GPT-4.1, which aligns with the performance ordering according the the LLM judge.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Large Language Models excel at solving a wide range of problems, but the sequential nature of autoregressive generation imposes a bottleneck on performance. In some tasks such as AVE, the generated outputs can be broken down into independent components. Hyper-Parallel Decoding leverages this independence to enable LLMs to generate multiple tokens in parallel, without requiring any architectural or model weight modifications. HPD parallelizes generation within each prompt, sharing both memory and computation while synergizing with batched inference, crucial for the offline setting.…。因此若该限制在目标 workload 中触发，不能把 `Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26209:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26209:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26209:end -->

<!-- review:SF-2026-ARXIV-2604-26256:start -->
#### DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-DISTRIBUTED-TRAINING` 中该 family 的受限状态。

机制与 state/control owner：(iii) KV-Cache reuse (Section 4.4 ) exploits a distinctive co-design insight: C1 is not merely an algorithmic necessity but yields mathematical equivalence of KV-Cache states across instances of the same policy version, enabling nearly zero-re-prefill migration—an optimization uniquely enabled by DORA’s adherence to C1. distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer

Evaluation contract：We evaluate DORA along two axes aligned with its constrained optimization formulation: efficiency (the optimization objective—rollout acceleration, end-to-end step time, and throughput) and algorithmic convergence (constraints C1–C3—convergence parity and staleness robustness). We further quantify the system overhead introduced by dynamic orchestration to validate DORA’s scalability.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Experimental Our evaluation compares DORA against different paradigms implemented within the same in-house framework to ensure a controlled comparison under identical hardware and software configurations. However, we acknowledge the absence of direct benchmarks against publicly available RL training systems such as veRL ( Sheng et al., 2025b ) and AReaL ( Fu et al., 2025 ) . Furthermore, due to resource constraints, we utilize production data exclusively for the MoE architecture, without conducting large-scale experiments on open-source MoE models. We plan to address these limitations and report extended results in future work.。因此若该限制在目标 workload 中触发，不能把 `DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26256:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26256:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26256:end -->

<!-- review:SF-2026-ARXIV-2604-26258:start -->
#### FlowBot: Inducing LLM Workflows with Bilevel Optimization and Textual Gradients

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-WORKFLOW` 中该 family 的受限状态。

机制与 state/control owner：We compare against GEPA and same datasets used in the original work: HotpotQA1, IFBench, HoVer, and PUPA. GEPA evolves prompts through reflective edits guided by rollout-based feedback while GEPA+Merge further merges complementary prompt updates across candidates. For a controlled comparison, all methods (including ours) use GPT-4.1 mini for all LLMs. Table 1 shows that our method improves upon GEPA on the retrieval/verification-heavy benchmarks, while remaining competitive on instruction- and privacy-centric tasks. This is despite the fact that baselines start from hand-optimized workflows and prompts, while FlowBot has to discover the workflow from scratch. workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步

Evaluation contract：We use the same setup for all datasets: one epoch of training with batch size 5, where for each batch we run two bi-level optimization loops, where one optimization loop itself consists of one outer loop step and 5 inner loop steps. We keep track of performance on the validation set after each batch and pick the best performing workflow on based on the validation set. We then run the best performing workflow on the test set.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Our work has several limitations. For one, the optimization procedure incurs nontrivial computational overhead, since both structure and prompts are refined using LLM calls. This cost is particularly salient for tasks where minimal workflows already perform well, and where additional steps may introduce avoidable latency and complexity. More generally, the framework trades optimization-time compute for reduced reliance on manual workflow engineering. While our approach is data-efficient, in some cases the model converges to the final workflow and does not improve with more training data. This type of rapid convergence is often seen in such prompt/workflow optimization approaches.…。因此若该限制在目标 workload 中触发，不能把 `FlowBot: Inducing LLM Workflows with Bilevel Optimization and Textual Gradients` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26258:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26258:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26258:end -->

<!-- review:SF-2026-ARXIV-2604-26274:start -->
#### Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：A tool-augmented language model agent operates as a reasoning loop in which the model receives a system prompt defining its role and constraints, processes a stream of user inputs and environmental observations, and emits structured action outputs that are routed to external services Zhang et al. (2025) . Each action takes the form of a tool call: a structured invocation consisting of a tool name and a parameter object conforming to a declared schema. The agent framework dispatches the call to the appropriate service, receives the result as an observation, and feeds it back to the model for subsequent reasoning. This loop continues until the agent either produces a terminal response or exhausts its context budget. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：Hardware. All experiments are conducted on AWS c6i.4xlarge instances (16 vCPU, Intel Xeon Ice Lake, 32 GB RAM), representing a standard compute-optimised deployment environment. The Praetor gateway and Aegis itself (deployed as an out-of-process sidecar) run on separate instances of the same class to ensure fair latency comparisons.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented Praetor , a telemetry-driven behavioral firewall for autonomous AI agents that resolves the sequential-blindness limitation of existing stateless firewalls. The separation of complex profiling from runtime enforcement yields two concrete advantages. First, the runtime gateway incurs negligible per-call overhead (as low as 2.2 ms at the 50 th percentile), representing a 3.7 × \times to 28.3 × \times improvement over Aegis, a representative stateless baseline, depending on agent vocabulary size. Second, the behavioral envelope is per-deployment: the pDFA encodes the deployment-level norms of one agent on one system prompt, rather than a generic cross-agent policy.…。因此若该限制在目标 workload 中触发，不能把 `Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26274:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26274:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26274:end -->

<!-- review:SF-2026-ARXIV-2604-26294:start -->
#### Folding Tensor and Sequence Parallelism for Memory-Efficient Transformer Training & Inference

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-TENSOR-PARALLEL` 中该 family 的受限状态。

机制与 state/control owner：Each compute node consists of eight MI300X GPUs connected via Infinity Fabric, dual-socket Intel Xeon CPUs with 2 TB of DDR5 memory, a dedicated Pollara 400 Gbps NIC per GPU, and local NVMe storage for high-throughput datasets and checkpoints (see Figure 8 ). A detailed description for the compute, storage, and login nodes is provided in Table V and Appendix A . parallel plan owner 冻结 tensor layout/collective，kernel 只消费一致 shard

Evaluation contract：We now evaluate the empirical behavior of TSP using the implementation described in § III . All experiments are conducted on the cluster described in § V using MI300X GPUs with Infinity Fabric intra-node interconnect and Pollara inter-node interconnect.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：TSP composes orthogonally with the existing axes of multi-dimensional parallelism. Because the TSP group is a single mesh dimension, it can be combined with additional TP, SP, PP, EP, or DP axes and existing mesh implementations. As a concrete example, suppose a workload calls for a tensor-sharding factor of 8 8 and a sequence-sharding factor of 2 2 . A conventional layout uses ( TP = 8 ) × ( SP = 2 ) = 16 (\mathrm{TP}{=}8)\times(\mathrm{SP}{=}2)=16 model-parallel ranks; if a node holds 8 8 GPUs, this forces one axis across inter-node links.…。因此若该限制在目标 workload 中触发，不能把 `Folding Tensor and Sequence Parallelism for Memory-Efficient Transformer Training & Inference` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26294:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26294:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26294:end -->

<!-- review:SF-2026-ARXIV-2604-26334:start -->
#### Efficient, VRAM-Constrained xLM Inference on Clients

问题/机制与 owner：VRAM 受限时在 CPU/GPU 间 pipeline 分片并重叠传输与执行。

Trade-off / failure：收益依赖 PCIe、layer shape 与 batch，不能证明通用低延迟或多租户 SLO。

Fallback/coexistence：带宽或 tail latency 失配时回退较小模型/量化/静态 placement。

<!-- claim:SF-2026-ARXIV-2604-26334:start -->收益依赖 PCIe、layer shape 与 batch，不能证明通用低延迟或多租户 SLO。<!-- claim:SF-2026-ARXIV-2604-26334:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26334:end -->

<!-- review:SF-2026-ARXIV-2604-26340:start -->
#### Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning

问题/机制与 owner：LoRA-MoE 在 exploratory training 后按 module 的 Gini、routing entropy 与 drift 非对称裁剪 experts，而不是使用全局统一 mask。

Trade-off / failure：只覆盖作者模型/任务；探索阶段有额外成本，错误 pruning 会破坏专家覆盖，不能外推到 base MoE 或任意 adapter。

Fallback/coexistence：每模块保留最小 expert floor 与可回滚 mask；drift/quality gate 失败时恢复原 adapter experts。

<!-- claim:SF-2026-ARXIV-2604-26340:start -->只覆盖作者模型/任务；探索阶段有额外成本，错误 pruning 会破坏专家覆盖，不能外推到 base MoE 或任意 adapter。<!-- claim:SF-2026-ARXIV-2604-26340:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26340:end -->

<!-- review:SF-2026-ARXIV-2604-26360:start -->
#### Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking

问题、旧路径与约束变化：旧路径把 `Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Reinforcement learning from human feedback (RLHF) systems face a compounding alignment challenge: not only are learned reward models uncertain about unseen state-action pairs, but the human preference annotations they are trained on are themselves inconsistent, context-dependent, and noisy. Existing approaches address these uncertainty sources in isolation - epistemic uncertainty is used to guide exploration, while preference uncertainty is absorbed during reward model training but discarded during policy optimization. We introduce Uncertainty-Aware Reward Discounting (UARD), a principled framework that jointly models epistemic uncertainty in value estimation via ensemble disagreement and aleatoric uncertainty in human preference annotations via annotator variability, combining these signals through a confidence-adjusted Reliability Filter that adaptively modulates reward weighting durin 该机制将长期 owner 定位到 `TRAIN-RLHF`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Empirically, UARD reduces reward hacking incidents by up to 93.6% across discrete decision-making and continuous control benchmarks (MuJoCo) compared to nine baselines including DQN, Ensemble-DQN, CQL, CPO, TRPO, SAC, EDAC, SUNRISE, and PPO, while maintaining competitive task performance on well-specified rewards. These results demonstrate that treating uncertainty as an active component of the optimization objective - rather than a passive diagnostic signal - provides a principled pathway toward more reliable and aligned RL systems.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Uncertainty-Aware Reward Discounting for Mitigating Reward Hacking` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26360:start -->只接受 arXiv:2604.26360v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26360:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26360:end -->

<!-- review:SF-2026-ARXIV-2604-26378:start -->
#### CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-GPU-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：In post-training quantization (PTQ) for Large Language Models (LLMs), handling outliers remains the primary bottleneck for achieving high-accuracy low-bit representations. Early works primarily unfolded within the classic PTQ framework. For instance, GPTQ Frantar et al. (2022) utilizes approximate second-order information to achieve highly accurate weight quantization, while AWQ ( Lin et al., 2024 ) further introduces the activation-aware weight protection concept to mitigate quantization errors in salient channels. As research extended from weight-only quantization to more general joint weight-activation quantization, systematic outliers in activations emerged as the primary bottleneck. LLM.int8() ( Dettmers et al., 2022 ) highlighted the existence of sparse yet systemic outlier features in LLMs and preserved a small number of these anomalous dimensions in high-precision computation through mixed-precision decomposition. Concurrently, SmoothQuant ( Xiao et al., 2023 ) mitigates the stretching of the low-bit quantization range caused by activation outliers by migrating the quantization difficulty from activations to weights via linear scaling. Furthermore, researchers began leveraging the numerical invariance of orthogonal transformations to improve quantizability by reshaping the representation space rather than explicitly isolating outliers. QuIP ( Chee et al., 2023 ) improves weight-only quantization performance by addressing the incoherence of the weight matrix and its proxy Hessian via randomized orthogonal matrix preprocessing. QuaRot Ashkboos et al. (2024b) incorpora memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射

Evaluation contract：Table 1 presents the overall performance of CoQuant and various baseline methods on WikiText perplexity and zero-shot common-sense reasoning tasks. Across all evaluated model families and scales, CoQuant consistently achieves the state-of-the-art quantization performance, demonstrating a superior accuracy-efficiency trade-off. Compared to the strongest subspace-based baseline, ResQ, CoQuant yields noticeable improvements. For instance, on the Llama-3.2-1B model, CoQuant reduces the WikiText perplexity from 12.03 to 11.60, while increasing the average zero-shot reasoning accuracy by 0.45% over ResQ. Similar trends are observed on the Llama-3.2-3B model. These consistent gains validate that jointly optimizing the high-precision subspace based on both weight and activation covariances retains more critical structural information than activation-only calibration.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This work still has several limitations. First, CoQuant relies on a first-order error approximation and an isotropic quantization noise assumption, which may not fully capture higher-order interactions under extremely low-bit settings. Second, we adopt a fixed high-precision subspace ratio across layers, while different modules may require different precision budgets. Third, our current study mainly focuses on quantization accuracy, and dedicated kernel implementation is needed to fully validate practical inference speedups. In future work, we plan to explore adaptive rank allocation, hardware-aware implementation, and broader evaluation on larger models, long-context tasks, and instruction-tuned LLMs.。因此若该限制在目标 workload 中触发，不能把 `CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26378:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26378:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26378:end -->

<!-- review:SF-2026-ARXIV-2604-26388:start -->
#### SplitFT: An Adaptive Federated Split Learning System For LLMs Fine-Tuning

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-DISTRIBUTED-TRAINING` 中该 family 的受限状态。

机制与 state/control owner：Testbed. The experiments were conducted on NVIDIA GeForce RTX 3090 GPUs using PyTorch 2.3. distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer

Evaluation contract：Testbed. The experiments were conducted on NVIDIA GeForce RTX 3090 GPUs using PyTorch 2.3.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We propose SplitFT , a robustness system designed for LLMs fine-tuning in federated learning environments, enabling different clients to set different cut-off criteria according to their computation resources and trained model performance, thus improving the overall system performance for LLMs fine-tuning. SplitFT also proposes to reduce the LoRA rank in cutlayer to reduce the communication overhead. In addition to simulating the heterogeneous data in real-world applications for our proposed split federated learning system, SplitFT proposes a length-based Dirichlet approach to divide the training data into different clients.…。因此若该限制在目标 workload 中触发，不能把 `SplitFT: An Adaptive Federated Split Learning System For LLMs Fine-Tuning` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26388:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26388:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26388:end -->

<!-- review:SF-2026-ARXIV-2604-26412:start -->
#### When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding?

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-SPECULATIVE-DECODING` 中该 family 的受限状态。

机制与 state/control owner：We implement the experiments on top of SpecForge ( Li et al., 2025a ) and train all drafters with the autoregressive test-time training (TTT) objective used by EAGLE-3 ( Li et al., 2025b ) , which aligns training with inference-time hidden-state drift. draft 只拥有 proposal，target verifier 拥有 acceptance 与 token commit

Evaluation contract：The retention column makes the long-range pattern more explicit. As depth increases, the KV-only retention ratio α 6 / α 0 \alpha_{6}/\alpha_{0} rises from 71.5% to 80.6%, eventually exceeding the EAGLE-3 baseline (73.5%). This is exactly the behavior anticipated by Prediction 1: once query estimation is strong enough, KV reuse degrades less severely across speculative steps even if its short-range accuracy still trails hidden-state reuse.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The experiments support this picture in a nuanced way. KV-only drafters become relatively more competitive at longer draft steps, and a hybrid drafter that combines KV and hidden-state signals improves draft acceptance over an EAGLE-3 baseline (MAT 2.54 vs. 2.37). However, the end-to-end proxy remains small: HF-measured MAT rises only from 5.01 to 5.04, while drafting latency increases by 5–10%.。因此若该限制在目标 workload 中触发，不能把 `When Hidden States Drift: Can KV Caches Rescue Long-Range Speculative Decoding?` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26412:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26412:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26412:end -->

<!-- review:SF-2026-ARXIV-2604-26460:start -->
#### Theory-Grounded Evaluation Exposes the Authorship Gap in LLM Personalization

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：We use the Blog Authorship Corpus [ Schler et al., 2006 ] : 681K posts from 19,320 bloggers. We select 50 authors with ≥ \geq 200 training posts, ≥ \geq 50 test posts, and mean length ≥ \geq 100 words, yielding 104K training and 26K test posts. Writing prompts are LLM-extracted content summaries (neutral descriptions of what a post discusses, not how )—we show in Section 4.3 that naïve first-sentence extraction inflates baselines by 28 percentage points. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：LaMP [ Salemi et al., 2024 ] evaluates personalization via task accuracy; LongLaMP [ Kumar et al., 2024 ] extends this to long-form generation with content-summary prompts (which we adopt). PersonalLLM [ Zollo et al., 2025 ] uses synthetic preference profiles. PersonaLens [ Zhao et al., 2025 ] evaluates conversational personalization with LLM-as-judge. Critically, no existing benchmark evaluates whether generated text is stylistically faithful to the target author—the gap we address.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Our evaluation covers blog-style writing from one corpus using two model families (Qwen 3, GLM-4) at 32B scale; only inference-time methods are tested, and the authorship gap may narrow under training-time approaches (e.g., per-user LoRA adapters)—the framework we propose provides the measuring stick. Analogous inference-time personalization failures have been observed in behavioral domains [ Sawant, 2026 ] , suggesting the authorship gap may extend beyond stylistic fidelity. A natural concern is that LUAR’s low gen → \rightarrow real scores reflect detection of “LLM-ness” rather than authorship mismatch.…。因此若该限制在目标 workload 中触发，不能把 `Theory-Grounded Evaluation Exposes the Authorship Gap in LLM Personalization` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26460:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26460:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26460:end -->

<!-- review:SF-2026-ARXIV-2604-26469:start -->
#### An Empirical Study of Speculative Decoding on Software Engineering Tasks

问题、旧路径与约束变化：旧路径把 `An Empirical Study of Speculative Decoding on Software Engineering Tasks` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Large Language Models (LLMs) have become widely used for Software Engineering (SE) tasks, spanning from function-level code generation to complex repository-level workflows. However, the high latency of autoregressive inference remains a significant bottleneck, hindering their deployment in interactive environments. While Speculative Decoding (SD) offers a promising technique for lossless acceleration, prior research on long-context repository-level tasks and complex agentic interactions remains limited. 该机制将长期 owner 定位到 `INFER-SPECULATIVE-DECODING`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：To bridge this gap, we present the first systematic empirical study to evaluate the effectiveness of SD in SE tasks. We systematically benchmark a comprehensive spectrum of strategies, encompassing both model-based and model-free methods, across representative generation, editing, and repair scenarios. Our empirical results indicate that SD demonstrates clear potential for accelerating inference, particularly for smaller models that achieve higher speedups than those of their larger counterparts.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`An Empirical Study of Speculative Decoding on Software Engineering Tasks` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26469:start -->只接受 arXiv:2604.26469v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26469:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26469:end -->

<!-- review:SF-2026-ARXIV-2604-26470:start -->
#### Hierarchical adaptive control for real-time dynamic inference at the edge

问题/机制与 owner：hierarchical adaptive edge inference 依据设备/网络状态在层级节点间选择执行。

Trade-off / failure：结果受作者 topology、模型和网络分布限制，未证明生产异构 fleet 的全局最优。

Fallback/coexistence：状态过期或迁移代价超预算时回退本地保守模型/静态 placement。

<!-- claim:SF-2026-ARXIV-2604-26470:start -->结果受作者 topology、模型和网络分布限制，未证明生产异构 fleet 的全局最优。<!-- claim:SF-2026-ARXIV-2604-26470:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26470:end -->

<!-- review:SF-2026-ARXIV-2604-26495:start -->
#### Beyond Code Reasoning: Specification-Anchored Auditing of Multi-Implementation Distributed Protocols

问题、旧路径与约束变化：旧路径把 `Beyond Code Reasoning: Specification-Anchored Auditing of Multi-Implementation Distributed Protocols` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Code-driven auditing fails when correctness depends on what the specification requires rather than how the code is written. Production blockchain networks expose this directly: byzantine consensus runs many independent clients of a shared specification, so a specification-divergence defect in one client can fork the network or halt finality. Existing tools reason one repository at a time, with no shared baseline held constant across implementations. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：On the RepoAudit C/C++ benchmark, SPECA reaches 88.9% precision at 100% recall (F1=0.94) and surfaces 12 author-validated bugs beyond ground truth, two externally validated.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Beyond Code Reasoning: Specification-Anchored Auditing of Multi-Implementation Distributed Protocols` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26495:start -->只接受 arXiv:2604.26495v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26495:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26495:end -->

<!-- review:SF-2026-ARXIV-2604-26505:start -->
#### Quantamination: Dynamic Quantization Leaks Your Data Across the Batch

问题/机制与 owner：cross-batch per-tensor dynamic activation quantization 使用共享 batch min/max；victim 输入可改变 scale 并影响 adversary logits，形成跨租户 side channel。

Trade-off / failure：攻击要求 co-location、logit access 与已知 quantization config；作者实验不证明所有 kernel/量化方案都可利用。

Fallback/coexistence：多租户路径改 per-token/static scale 或 batch isolation；无法满足隔离时回退无共享动态量化，单租户 fast path 可保留。

<!-- claim:SF-2026-ARXIV-2604-26505:start -->攻击要求 co-location、logit access 与已知 quantization config；作者实验不证明所有 kernel/量化方案都可利用。<!-- claim:SF-2026-ARXIV-2604-26505:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26505:end -->

<!-- review:SF-2026-ARXIV-2604-26506:start -->
#### SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：We present an adversarial training framework called SafeReview to defend LLM-based peer review systems against adversarial hidden prompts. Our approach features a Generator model that crafts sophisticated injection prompts and a Defender model that maintains review integrity, trained jointly through iterative co-evolutionary optimization. Specifically, our approach consists of two main components: (1) an attacker trained via Group Relative Policy Optimization (GRPO) to generate subtle injection prompts, and (2) a defender trained via Direct Preference Optimization (DPO) to maintain review integrity despite adversarial manipulations. policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：We evaluate our iterative adversarial training framework on a comprehensive dataset of academic papers to demonstrate its effectiveness in defending against adversarial hidden prompts while maintaining review quality. Our experiments focus on two critical aspects: the attacker’s ability to degrade the correlation between automated reviews and ground-truth scores, and the defender SafeReview’s capacity to preserve this correlation under adversarial conditions.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Future work should explore extending this framework to multi-modal submissions, investigate the transferability of attacks across different reviewer models, and adapt the defence mechanism for proprietary API-based reviewers (e.g., GPT-4, Claude) where fine-tuning is infeasible—potentially through prompt-based defence strategies or output filtering. Furthermore, empirical validation is restricted to Computer Science venues (e.g., NeurIPS) and to specific instruction-style prompt injections, limiting the assessment of generalizability across diverse academic domains and robustness against more subtle, non-instruction-based semantic perturbations.。因此若该限制在目标 workload 中触发，不能把 `SafeReview: Defending LLM-based Review Systems Against Adversarial Hidden Prompts` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26506:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26506:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26506:end -->

<!-- review:SF-2026-ARXIV-2604-26511:start -->
#### Tatemae: Detecting Alignment Faking via Tool Selection in LLMs

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-SECURITY` 中该 family 的受限状态。

机制与 state/control owner：We now describe our Tatemae framework: dataset (Section 3.1 ), evaluation pipeline (Section 3.2 ) and evaluation criteria (Section 3.3 ). policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal

Evaluation contract：We now describe our Tatemae framework: dataset (Section 3.1 ), evaluation pipeline (Section 3.2 ) and evaluation criteria (Section 3.3 ).

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Susceptibility to alignment faking reflects training choices more than capability. All six models score above 81% on T 1 T_{1} (Table 4 ), yet AF rates span from 3.5% to 23.7% across five runs each. Claude Sonnet 4.6 and Gemini 3.1 Pro both reach ≥ 99.8 % \geq 99.8\% on T 1 T_{1} , but their T 3 T_{3} rates differ by more than 4x (93.5% vs. 20.4%), producing AF rates of 3.5% and 10.0%. No model resists uniformly across domains and pressure types. Variation Across Models. Vulnerability profiles differ in ways that go beyond the aggregate range. DeepSeek is more vulnerable under Corruption than Sabotage, while Claude Sonnet 4.6 shows the opposite pattern.…。因此若该限制在目标 workload 中触发，不能把 `Tatemae: Detecting Alignment Faking via Tool Selection in LLMs` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26511:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26511:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26511:end -->

<!-- review:SF-2026-ARXIV-2604-26525:start -->
#### PRAG: End-to-End Privacy-Preserving Retrieval-Augmented Generation

问题/机制与 owner：同态加密同时覆盖 RAG document/query，相似度、排序和更新在 ciphertext 上完成。

Trade-off / failure：CKKS 近似误差可改变 ranking；仍有 access-pattern/ranking leakage 与显著计算成本，未证明生产规模 SLO。

Fallback/coexistence：高成本/低 margin query 回退受控 enclave 或不检索；保留 plaintext-free 与传统隔离两条路径。

<!-- claim:SF-2026-ARXIV-2604-26525:start -->CKKS 近似误差可改变 ranking；仍有 access-pattern/ranking leakage 与显著计算成本，未证明生产规模 SLO。<!-- claim:SF-2026-ARXIV-2604-26525:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26525:end -->

<!-- review:SF-2026-ARXIV-2604-26557:start -->
#### DUAL-BLADE: Dual-Path NVMe-Direct KV-Cache Offloading for Edge LLM Inference

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-GPU-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：The increasing deployment of Large Language Model (LLM) inference on edge AI systems demands efficient execution under tight memory budgets. A key challenge arises from Key–Value (KV) caches, which often exceed available device memory. Although NVMe-based offloading offers scalable capacity, existing file-based designs rely heavily on the kernel page cache, leading to cache thrashing, unpredictable latency, and high software overhead under memory pressure. We present Dual-Blade , a dual-path KV residency framework that dynamically assigns KV tensors to either a page-cache path or an NVMe-direct path based on runtime memory availability. The NVMe-direct path bypasses the filesystem by mapping KV tensors to contiguous logical block address (LBA) regions, enabling low-overhead direct storage access. Dual-Blade further incorporates adaptive pipeline parallelism to overlap storage I/O with GPU DMA, improving inference throughput. Our evaluation shows that Dual-Blade substantially mitigates I/O bottlenecks, reducing prefill and decode latency by up to 33.1% and 42.4%, respectively, while improving SSD utilization by 2.2 × \times across diverse memory budgets. memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射

Evaluation contract：To assess device-dependent effects and investigate how storage media characteristics impact end-to-end inference latency, we evaluate two NVMe SSDs with distinct classes and I/O constraints: SSD A (Samsung PM9D3a, PCIe Gen5, 4 KiB LBA, 256 KiB MDTS) and SSD B (Samsung 990 PRO, PCIe Gen4, 512 B LBA, 2 MiB MDTS). This comparison validates whether our architectural benefits persist across different hardware generations and internal controller specifications, as LBA size and MDTS directly constrain NVMe-direct alignment and per-command transfer granularity.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This paper presents Dual-Blade , a dual-path, NVMe-direct KV-cache offloading architecture to accelerate LLM inference in edge AI systems with limited memory. Dual-Blade integrates dual-path KV residency, NVMe-direct I/O, and adaptive pipeline parallelism to maximize storage I/O efficiency during inference. Extensive evaluation shows that Dual-Blade reduces prefill and decode latency by up to 33.1% and 42.4%, respectively, while boosting SSD utilization by up to 2.2 × \times in diverse memory budgets.。因此若该限制在目标 workload 中触发，不能把 `DUAL-BLADE: Dual-Path NVMe-Direct KV-Cache Offloading for Edge LLM Inference` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26557:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26557:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26557:end -->

<!-- review:SF-2026-ARXIV-2604-26561:start -->
#### Preserving Disagreement: Architectural Heterogeneity and Coherence Validation in Multi-Agent Policy Simulation

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MULTI-AGENT` 中该 family 的受限状态。

机制与 state/control owner：The AI Council is a three-phase deliberation system designed to simulate multi-stakeholder policy deliberation while preserving value-based disagreement. Each deliberation proceeds through structured debate, independent evaluation, and (optionally) coherence validation. orchestrator 拥有成员、消息与 commit control，各 agent 只拥有局部 proposal

Evaluation contract：Seven evaluator agents, each primed with a distinct value perspective, independently read the complete debate output and produce a ranking of all three options with supporting reasoning. Evaluators do not see each other’s output at any point.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：One model pool. All results use the same seven local models. Coherence scores are a joint measure of model capability and perspective–model fit. Disentangling these would require testing each model across multiple value perspectives—a combinatorial design not feasible with the current seven-model pool but a natural direction for future work. The differentiated profiling results (models scoring high on some perspectives and low on others) suggest that perspective–model fit is a meaningful component, but we cannot rule out that overall model quality contributes to observed coherence differences. This concern is consistent with Li et al.…。因此若该限制在目标 workload 中触发，不能把 `Preserving Disagreement: Architectural Heterogeneity and Coherence Validation in Multi-Agent Policy Simulation` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26561:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26561:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26561:end -->

<!-- review:SF-2026-ARXIV-2604-26622:start -->
#### OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-MEMORY` 中该 family 的受限状态。

机制与 state/control owner：The backbone of our method is DeepSeek-OCR. However, the pre-trained model is optimized primarily for literal transcription and is weak at instruction-following for relevance matching. In our setting, the model must not only read but also judge which passages support a query. We therefore fine-tune the model for discriminative retrieval using a repurposed HotpotQA dataset Yang et al. (2018) . memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图

Evaluation contract：Table 1 summarizes the performance of OCR-Memory against a range of text-based memory baselines on the Mind2Web and AppWorld benchmarks under the same context-budget setting. On Mind2Web, our method yields consistent gains across all metrics, outperforming the strong abstraction-based baseline AWM by clear margins. In particular, OCR-Memory improves Element Accuracy from 49.1% to 53.8% and increases Step Success Rate to 46.1%, achieving a state-of-the-art Task Success Rate of 4.8%. These improvements stem from our ability to retain and recover fine-grained, long-horizon textual and structural details by encoding them into high-density visual representations that can be read back with a small number of tokens. On AppWorld, OCR-Memory attains the highest Average Success Rate of 58.1%. The advantage is most pronounced on “Hard” tasks, where our method reaches 30.8%, substantially surpassing both the standard Retrieval baseline (21.4%) and AWM (27.2%). Overall, these results show that using the visual modality primarily as a compact carrier for lengthy textual histories enables precise evidence recovery with markedly reduced token consumption.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Despite the effectiveness of OCR-Memory, we acknowledge several limitations. First, unlike training-free retrieval baselines, our framework requires fine-tuning a specialized optical retrieval model, which incurs additional training resource overhead. Second, the process of rendering interaction logs into images is computationally more expensive than direct text storage, and storing visual histories inevitably consumes more disk space than raw text logs. Finally, deploying the system imposes an extra memory footprint, as the parameters of the vision encoder must be maintained in memory alongside the primary language model.。因此若该限制在目标 workload 中触发，不能把 `OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26622:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26622:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26622:end -->

<!-- review:SF-2026-ARXIV-2604-26649:start -->
#### When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-RAG` 中该 family 的受限状态。

机制与 state/control owner：ReaLM-Retrieve consists of three components: (1) reasoning step segmentation and uncertainty estimation, (2) a learned intervention policy, and (3) efficient retrieval integration. Figure 1 provides an overview of the problem, our solution, and key results. retrieval service 拥有 index/query evidence，generator 不获得来源真值所有权

Evaluation contract：Table 4 presents detailed efficiency metrics. ReaLM-Retrieve adds only 1.7 seconds latency over no-retrieval baseline (13.7% overhead) vs 6.3 seconds for IRCoT (51% overhead). The reduction comes from fewer retrieval calls (1.8 vs 3.4), speculative caching (eliminating 37% of retrieval latency), and implicit compression (reducing context length by 73%). The 3.2 × \times per-call efficiency improvement (0.66s vs 2.10s for Naive Interleaving) results from three complementary optimizations whose contributions are additive on per-call latency rather than multiplicative. Speculative caching is the dominant contributor: by executing likely next-step retrievals in parallel with reasoning, it eliminates retrieval entirely on a 37% hit rate, removing the full 2.10s per cached call and accounting for the largest share of the saving in expectation. Implicit compression of retrieved evidence reduces context-processing time on the remaining (non-cached) calls by shrinking injected context by 73%. KV-cache preservation further reduces post-retrieval time-to-first-token by avoiding recomputation of unchanged context for open-weight models. Combined with 57% fewer retrieval calls overall, ReaLM-Retrieve achieves 1.50 × \times lower end-to-end latency than Naive Interleaving and 1.33 × \times lower than IRCoT. Token count analysis shows ReaLM-Retrieve uses 9,489 tokens vs IRCoT’s 11,284. Retrieval at appropriate moments allows the model to reach answers with less reasoning, as evidence resolves uncertainties that would otherwise require extended exploration. ReaLM-Retrieve reduces cost by 1

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Completion-only models : Performance is 2–3% F1 lower than open-weight models where richer uncertainty signals are available (68.9% vs 71.2% F1 on MuSiQue for o1 vs R1). Retrieval corpus dependence : When relevant information is absent, retrieval wastes computation (171ms avg) and may introduce noise (14% of out-of-domain retrievals return misleading information). Training data requirements : The policy requires 19,938 training examples, though cross-benchmark results suggest 5K–10K suffice for reasonable performance. Computational overhead : Step boundary and RSUS computation add 8% inference overhead, with no benefit for queries answerable without retrieval.…。因此若该限制在目标 workload 中触发，不能把 `When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26649:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26649:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26649:end -->

<!-- review:SF-2026-ARXIV-2604-26666:start -->
#### FACT: Compositional Kernel Synthesis with a Three-Stage Agentic Workflow

问题、旧路径与约束变化：旧路径未显式拥有 `AGENT-WORKFLOW` 中该 family 的受限状态。

机制与 state/control owner：Figure 2 illustrates our three-stage agentic workflow for whole-model kernel optimization. The workflow maps directly to CUTLASS’s API hierarchy ( NVIDIA Corporation, 2025 ) and leverages LLM-based actions to orchestrate complex optimization tasks that would otherwise require manual intervention. Each stage decomposes into a sequence of well-defined actions—graph extraction and analysis, kernel synthesis and verification, composition and extension loading—that the agent executes systematically. By structuring optimization as a pipeline of discrete actions, we enable the agent to reason about each decision point independently while maintaining coherence across the entire workflow. workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步

Evaluation contract：For each KernelBench problem, we report the output of all three stages of the workflow. Stage 1 (Pattern Discovery) describes the patterns the agent identified from the computation graph. Stage 2 (Pattern Realization) presents correctness verification, auto-tuning results, and performance comparisons against the PyTorch cuBLAS baseline. Stage 3 (Pattern Composition) applies only to multi-operator problems (Level 2 and above), where multiple realized kernels are composed into a single optimized computation graph; for single-operator Level 1 problems this stage is trivial and omitted. In this section we present results for KernelBench Problems 1, 3, and 6 (Level 1 GEMMs) and for Level 3 problem 44_MiniGPTBlock . Results for additional problems targeting the H200 GPU are in progress.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Future work. Several directions remain for extending FACT. First, we are extending the framework to support Hopper architecture (H200 GPU), targeting warp-specialized kernels with TMA and WGMMA instructions. Second, we plan to compare FACT against agentic baselines (KernelBlaster, CUDA Agent, StitchCUDA, Astra) on the same KernelBench problems to quantify the benefits of library-grounded synthesis. Finally, we are working on open-sourcing the generated CUTLASS kernels and workflow prototype to enable reproducibility and community engagement.。因此若该限制在目标 workload 中触发，不能把 `FACT: Compositional Kernel Synthesis with a Three-Stage Agentic Workflow` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26666:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26666:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26666:end -->

<!-- review:SF-2026-ARXIV-2604-26687:start -->
#### COPUS: Co-adaptive Parallelism and Batch Size Selection in Large Language Model Training

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-DISTRIBUTED-TRAINING` 中该 family 的受限状态。

机制与 state/control owner：This decomposition separates optimization-side and execution-side effects. The global batch size B g B_{g} primarily governs the statistical behavior of training, while S S and B m B_{m} determine memory footprint, communication pattern, pipeline efficiency, and device utilization. Data parallelism is typically most efficient when each replica has enough local work; tensor parallelism trades additional intra-layer communication for lower per-device memory; and pipeline parallelism trades stage-level concurrency against pipeline bubbles, making B m B_{m} and gradient accumulation important throughput knobs. Thus, the DP-dominant strategy is not always feasible: large models often require minimum tensor or pipeline parallelism degrees to fit the model, activation, and optimizer states in GPU memory, so Copus searches only among memory-feasible 3D strategies. Existing systems such as Megatron-LM ( Shoeybi et al., 2019 ) and DeepSpeed ( Rasley et al., 2020 ) expose these choices as execution parameters that are usually selected before training and then kept fixed. distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer

Evaluation contract：As shown in Figure 1 , Copus jointly evolves loss, batch size, and parallelism strategy. It starts with DP2,TP1,PP4, a pipeline-heavy layout suited to the initial B g = 16 B_{g}=16 , then moves to DP4,TP1,PP2 at about 3 min and to fully data-parallel DP8,TP1,PP1 at about 22 min as GNS rises and Goodput favors larger batches. Each transition occurs only when the candidate exceeds the current Goodput by at least 10%. The CBS baselines adapt batch size on a similar schedule, but remain locked to their initial parallelism. As a result, the DP2,TP1,PP4 baseline loses throughput as B g B_{g} grows, while the DP8,TP1,PP1 baseline underperforms early when the batch is too small to saturate pure data parallelism. Occasional loss spikes appear at batch size transitions and, less frequently, during steady-state training. We discuss their causes and connect them to known training dynamics in Appendix E .

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：Across four configurations spanning 3B to 32B parameters on both NVIDIA H100 and AMD MI210 hardware, Copus achieves average time-to-convergence speedups of 3.9–8.0% over the fastest individual baseline at each loss threshold (including system overheads), with peak gains of 11.1%. Eliminating resharding overhead entirely would raise these to 4.7–11.4% average and 13.2% peak, indicating clear headroom for further systems engineering. The analysis confirms that these gains arise from keeping both throughput and statistical efficiency simultaneously high, a property that no fixed-parallelism baseline achieves.。因此若该限制在目标 workload 中触发，不能把 `COPUS: Co-adaptive Parallelism and Batch Size Selection in Large Language Model Training` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26687:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26687:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26687:end -->

<!-- review:SF-2026-ARXIV-2604-26694:start -->
#### Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising

问题、旧路径与约束变化：旧路径未显式拥有 `MULTIMODAL-EMBODIED-VLA` 中该 family 的受限状态。

机制与 state/control owner：Building upon recent advances in unified world action modeling, we propose X-WAM as a unified framework that simultaneously addresses video generation, 3D spatial reconstruction, policy success rate, and efficient action execution. This is achieved through two core designs: a lightweight depth adaptation module (Section 3.2 ) that enables spatial reconstruction, and Asynchronous Noise Sampling (Section 3.3 ) that jointly optimizes generation quality and action decoding efficiency. We begin by presenting the overall model architecture (Section 3.1 ), and then detail the training procedure including data processing and the training pipeline (Section 3.4 ). policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit

Evaluation contract：We evaluate X-WAM across three complementary dimensions: policy execution (Section 4.1 ), 4D reconstruction and generation (Section 4.2 ), and ablation studies that jointly analyze both objectives (Section 4.3 ). This comprehensive evaluation validates that X-WAM’s unified framework simultaneously achieves strong performance across all dimensions.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：First, the current framework processes only a fixed-length context window of observations without incorporating historical information or autoregressive rollout, unlike approaches such as DreamZero [ 9 ] that leverage KV caching for extended temporal context. This limited context horizon may hinder the model’s ability to fully comprehend task progress in long-horizon manipulation scenarios, potentially leading to suboptimal decisions when the current observation alone is insufficient to disambiguate the task stage.。因此若该限制在目标 workload 中触发，不能把 `Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26694:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26694:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26694:end -->

<!-- review:SF-2026-ARXIV-2604-26733:start -->
#### FutureWorld: A Live Reinforcement Learning Environment for Predictive Agents with Real-World Outcome Rewards

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-GRPO` 中该 family 的受限状态。

机制与 state/control owner：Existing methods have already explored the problem of improving future prediction ability for future prediction in LLM-based systems. Some works apply outcome-based RL to static datasets of resolved prediction questions. Turtel et al. (2025) demonstrate that fine tuning with negative Brier score as a reward signal yields substantial accuracy gains on a 14B parameter model trained over 110,000 resolved Polymarket 1 1 1 https://polymarket.com/ events, but the agent operates only on a fixed prompt that contains pre collected information, rather than acquiring information through its own search process, so the information gathering behavior remains entirely untrained. Jeen et al. (2026) apply Group Relative Policy Optimization (GRPO) Shao et al. (2024) to a 120B-parameter model using Brier score rewards on approximately 10k binary questions, achieving notable improvements on the Metaculus benchmark Metaculus (2025) . However, its research phase is pre-computed before training, meaning the model’s ability to retrieve and synthesize evidence is frozen rather than learned. Other work, exemplified by UniPat AI (2026) , operates in a live setting with agentic rollouts and a daily rolling cycle, but uses rubric-based process rewards calibrated against outcome-derived rankings rather than direct outcome-based rewards, introducing an indirection between the training signal and the target metric. Across these efforts, no existing system simultaneously trains on outcome-derived rewards, performs agentic information retrieval inside the training loop, and operates over a live, rolling str rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit

Evaluation contract：After each day of training, we archive the model checkpoint from that day. After training for 8 consecutive days, we evaluate the checkpoints saved from all previous days on the same daily prediction dataset. Concretely, all 8 day’s checkpoints are tested on the same day, with each agent asked to predict a set of questions whose outcomes are expected to be realized the next day.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We introduce FutureWorld, a live environment for training predictive agents with real-world outcome rewards. Unlike prior works that rely on static collections of resolved questions or proxy process-based rewards, FutureWorld keeps the prediction stream live, places agentic search and reasoning inside the training loop, and learns directly from realized future outcomes. Our experiments show that this delayed real-world feedback can serve as an effective training signal, leading to improved prediction performance over successive days, while the benchmark built on top of FutureWorld also provides a practical testbed for evaluating frontier agents on live prediction tasks.…。因此若该限制在目标 workload 中触发，不能把 `FutureWorld: A Live Reinforcement Learning Environment for Predictive Agents with Real-World Outcome Rewards` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26733:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26733:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26733:end -->

<!-- review:SF-2026-ARXIV-2604-26752:start -->
#### GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-DPO` 中该 family 的受限状态。

机制与 state/control owner：A critical component of GLM-5V-Turbo’s deployment strategy is its seamless integration with industry-standard external agent frameworks. By moving beyond isolated tool calls, the model serves as the cognitive core for systems like Claude Code and AutoClaw [ 49 ] , bridging the gap between high-level reasoning and low-level system execution. The integration with Claude Code transforms GLM-5V-Turbo from a passive code generator into an active system-level collaborator. Within this framework, the model leverages its multimodal capabilities to navigate complex terminal environments and local file systems. While Claude Code handles the logic and environment, AutoClaw provides the "hands" for browser-based and GUI-centric automation. GLM-5V-Turbo acts as the vision-language controller for AutoClaw, enabling sophisticated agentic workflows. preference data owner 拥有 pair/label provenance，trainer 拥有 objective，judge 不拥有最终 policy commit

Evaluation contract：The core potential of a multimodal agent lies in anchoring reasoning within visual contexts—a paradigm we term “think with image, deep search with image.” To evaluate this, we introduce ImageMining 2 2 2 https://github.com/zai-org/ImageMining , a benchmark designed to test the integration of high-density visual understanding and autonomous multimodal search.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We propose Multimodal Multi-Token Prediction (MMTP) , a multimodal extension of multi-token prediction (MTP) [ 9 ] , designed to support both text-only and multimodal inputs while remaining friendly to large-scale infrastructure. The goal is to preserve acceptable length as well as training and inference efficiency in multimodal settings. In standard text-only MTP, prefix tokens can be passed into the MTP head directly through token IDs and embedded with the word embedding layer.…。因此若该限制在目标 workload 中触发，不能把 `GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26752:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26752:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26752:end -->

<!-- review:SF-2026-ARXIV-2604-26779:start -->
#### Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-SPECULATIVE-DECODING` 中该 family 的受限状态。

机制与 state/control owner：Open RL post-training stacks now include NeMo-Aligner, OpenRLHF, veRL, and slime, which provide scalable orchestration and rollout-serving integration ( Shen et al., 2024 ; Hu et al., 2025 ; Sheng et al., 2025 ; veRL Team, 2025 ; Zhu et al., 2025 ) . Our work is narrower: rather than a new framework, we study speculative decoding as a deployable rollout primitive inside NeMo RL. draft 只拥有 proposal，target verifier 拥有 acceptance 与 token commit

Evaluation contract：Figure 2 confirms these findings over the full training run. Generation latency under EAGLE-3 remains consistently below the autoregressive baseline, with mean speedups of 1.54 × 1.54\times on RL-Think and 1.79 × 1.79\times on RL-Zero (Figure 2(a) ). Notably, the RL-Zero baseline latency rises sharply during the first ∼ 100 {\sim}100 steps as the policy transitions from short outputs to longer reasoning traces; the EAGLE-3 speedup tracks this shift without degradation. Validation accuracy evolves indistinguishably under both decoding modes (Figure 2(b) ), confirming that speculative decoding delivers a faster rollout engine without altering optimization behavior.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We integrated speculative decoding into NeMo RL as a rollout acceleration primitive that preserves verifier-exact training semantics. On 8B-scale reasoning workloads under synchronous RL, EAGLE-3 speculative decoding reduces rollout generation latency by 1.5 1.5 – 1.8 × 1.8\times and overall RL step time by up to 1.41 × 1.41\times , with no change in validation accuracy. Simulator projections show that these gains grow at deployment scale: at favorable operating points for a 235B model, rollout speedups exceed 3 × 3\times and projected end-to-end training speedup reaches approximately 2.5 × 2.5\times .…。因此若该限制在目标 workload 中触发，不能把 `Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26779:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26779:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26779:end -->

<!-- review:SF-2026-ARXIV-2604-26815:start -->
#### What Is the Cost of Energy Monitoring? An Empirical Study on the Overhead of RAPL-Based Tools

问题/机制与 owner：把 energy monitor 自身的采样与 instrumentation overhead 纳入测量 contract。

Trade-off / failure：作者测试范围不证明任意 accelerator、采样频率或生产 workload 下开销可忽略。

Fallback/coexistence：超过 overhead budget 时降低采样、使用 out-of-band sensor，并标记缺测而非补值。

<!-- claim:SF-2026-ARXIV-2604-26815:start -->作者测试范围不证明任意 accelerator、采样频率或生产 workload 下开销可忽略。<!-- claim:SF-2026-ARXIV-2604-26815:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26815:end -->

<!-- review:SF-2026-ARXIV-2604-26837:start -->
#### Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving

问题、旧路径与约束变化：旧路径未显式拥有 `INFER-KV-CACHE` 中该 family 的受限状态。

机制与 state/control owner：General System Abstraction for Sparse Attention. Sparse attention algorithms span a wide spectrum of granularities, such as blocks or clusters with varying sizes. A general sparse-serving system must therefore provide a common inference-pipeline abstraction that makes different algorithms easy to integrate while hiding granularity differences behind a unified interface. Moreover, this abstraction must preserve common optimizations across algorithms. cache manager 拥有 block identity、placement 与 eviction，scheduler 只引用合法 handle

Evaluation contract：Spin reduces per-token decode latency by 8.4 8.4 – 58 % 58\% compared to the original implementations of the representative sparse attention algorithms, translating up to 2.39 × 2.39\times throughput improvement and thus demonstrating the effectiveness of Spin ’s system-level optimizations.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：This paper introduces Spin , a sparse attention-native framework for efficient inference in long-context LLM serving. Through a unified pipeline abstraction, Spin allows diverse sparse attention algorithms to be integrated with minimal developer effort — requiring only the algorithm-defined Index and Select logic while the rest is automatically handled by the system. Built on top of this abstraction, Spin ’s locality-aware buffer management and scalable metadata organization translate algorithmic sparsity into system-level throughput gains.…。因此若该限制在目标 workload 中触发，不能把 `Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26837:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26837:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26837:end -->

<!-- review:SF-2026-ARXIV-2604-26848:start -->
#### STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation

问题、旧路径与约束变化：旧路径未显式拥有 `MULTIMODAL-WORLD-MODELS` 中该 family 的受限状态。

机制与 state/control owner：As shown in Fig. 1 , STARRY consists of four modules: the Understanding Expert , Spatial-Temporal(ST) World Model , Geometry Expert , and Action Expert . The core design is that future spatial-temporal latents and actions are jointly denoised over the same horizon, while geometry-aware weights are selectively applied only to the action attention branch. world state owner 提交 observation/action-conditioned transition，policy 只消费可验证 rollout

Evaluation contract：We evaluate STARRY in simulation and real-world settings. Specifically, we test on RoboTwin 2.0 under Clean and Randomized settings (Sec. 4.1 ), examine physical execution in real-world experiments (Sec. 4.2 ), and conduct ablations to analyze the effects of spatial-temporal prediction and GASAM (Sec. 4.3 ).

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：We presented STARRY , a world-model-enhanced action-generation policy that aligns spatial-temporal prediction with action generation. STARRY jointly denoises future spatial-temporal latents and action sequences, and uses GASAM to inject predicted geometry into the action attention branch. On RoboTwin 2.0, STARRY achieves 93.82% / 93.30% average success under Clean and Randomized settings. In real-world experiments, it improves average success from 42.5% to 70.8% over π 0.5 \pi_{0.5} , demonstrating improved execution reliability in physical manipulation. These results demonstrate the effectiveness of action-centric spatial-temporal world modeling for spatial-temporally demanding robotic action generation.。因此若该限制在目标 workload 中触发，不能把 `STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26848:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26848:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26848:end -->

<!-- review:SF-2026-ARXIV-2604-26881:start -->
#### FaaSMoE: A Serverless Framework for Multi-Tenant Mixture-of-Experts Serving

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-MULTI-TENANT` 中该 family 的受限状态。

机制与 state/control owner：As shown in Figure 1 , FaaSMoE decomposes MoE inference into a lightweight control plane ( Orchestrator ) and a distributed compute plane on the FaaS platform ( Expert Block ). The orchestrator consists of a tokenizer, attention layers, and gating modules, which collectively determine the token-to-expert routing pattern. These components represent a small fraction of an MoE model and incur minimal memory overhead, making them suitable to run using either a centralized orchestrator or scale out with tenants. After gating, the orchestrator constructs micro-batched routing requests and dispatches them to the corresponding expert functions deployed on the FaaS platform. Each expert block contains only MoE experts and performs stateless computation on assigned tokens. The FaaS runtime provides isolation, elasticity, and load balancing, enabling frequently used experts to scale out and letting rarely used experts scale to zero. tenant control plane 拥有 identity、quota、isolation 与 admission，scheduler 只执行授权

Evaluation contract：To evaluate the system behavior of FaaSMoE, we construct a controlled multi-tenant environment with six concurrent clients. Each client issues five heterogeneous tasks drawn from the BIG-Bench dataset 2 2 2 http://github.com/google/BIG-bench , resulting in thirty requests per experiment run. Although the number of requests is small, each request activates multiple experts, resulting in a substantially larger number of expert invocations at the system level. The experimental setup is designed to compare resource consumption across different deployment strategies to showcase the resource efficiency of expert sharing across tenants. Under this setting, the workload is sufficient to expose differences in expert residency, sharing, and orchestration behavior across tenants.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：FaaSMoE explores a resource efficient approach to serving MoE models in multi-tenant environment by decoupling stateless expert execution on FaaS platforms thus enabling on-demand expert invocation and expert sharing across tenants. The experimental results demonstrate the efficiency of FaaSMoE and motivate several discussion points, limitations and directions for future work.。因此若该限制在目标 workload 中触发，不能把 `FaaSMoE: A Serverless Framework for Multi-Tenant Mixture-of-Experts Serving` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26881:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26881:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26881:end -->

<!-- review:SF-2026-ARXIV-2604-26889:start -->
#### Revealing NVIDIA Closed-Source Driver Command Streams for CPU-GPU Runtime Behavior Insight

问题、旧路径与约束变化：旧路径把 `Revealing NVIDIA Closed-Source Driver Command Streams for CPU-GPU Runtime Behavior Insight` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：For NVIDIA GPUs, CUDA is the primary interface through which applications orchestrate GPU execution, yet much of the logic that realizes CUDA operations resides in NVIDIA's closed-source userspace driver. As a result, the translation from high-level CUDA APIs to low-level hardware commands remains opaque, limiting both software understanding and performance attribution. This paper makes that command path visible. For NVIDIA GPUs, CUDA is the primary interface through which applications orchestrate GPU execution, yet much of the logic that realizes CUDA operations resides in NVIDIA's closed-source userspace driver. As a result, the translation from high-level CUDA APIs to low-level hardware commands remains opaque, limiting both software understanding and performance attribution. This paper makes that command path visible. 该机制将长期 owner 定位到 `INFER-GPU-MEMORY`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：As a result, the translation from high-level CUDA APIs to low-level hardware commands remains opaque, limiting both software understanding and performance attribution. For CUDA Graphs, we show that the reduced launch overhead in newer CUDA releases is associated with a smaller command footprint and a more efficient submission pattern. Together, these results show that command-level visibility provides a practical basis for understanding and optimizing GPU middleware behavior, improving performance interpretation, and informing future hardware--software co-design for CUDA and related accelerator stacks.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`Revealing NVIDIA Closed-Source Driver Command Streams for CPU-GPU Runtime Behavior Insight` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26889:start -->只接受 arXiv:2604.26889v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26889:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26889:end -->

<!-- review:SF-2026-ARXIV-2604-26904:start -->
#### ClawGym: A Scalable Framework for Building Effective Claw Agents

问题、旧路径与约束变化：旧路径未显式拥有 `PLATFORM-EVALUATION-SYSTEM` 中该 family 的受限状态。

机制与 state/control owner：The ClawGym framework comprises three main components. First, ClawGym-SynData provides a carefully constructed synthesized dataset of 13.5K training tasks, with an automated synthesis process that enables large-scale data generation. Second, ClawGym-Agents trains a family of Claw agents on high-quality trajectories collected from synthesized tasks through black-box rollouts using the OpenClaw harness. Third, ClawGym-Bench offers a benchmark of 200 task instances for evaluating Claw-style agents, with carefully assessed reliability. Together, these components provide a foundation for advancing research on environment-grounded instruction-execution agents. In what follows, we introduce ClawGym-SynData, ClawGym-Agents, and ClawGym-Bench in Sections 3 , 4 , and 5 , respectively. EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定

Evaluation contract：In this section, we conduct a series of empirical analyses to investigate the key factors contributing to the performance of ClawGym-Agents SFT. Specifically, we evaluate the synergy between our dual synthesis strategies, analyze the training dynamics and convergence patterns, and examine the impact of reward-based trajectory filtering protocols.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：In this paper, we present ClawGym, a scalable framework that streamlines the end-to-end development pipeline for personal agents by integrating task synthesis, trajectory collection, agent training, and evaluation within Claw-style environments. The framework first introduces a twofold synthesis approach that combines top-to-bottom topic-driven generation with bottom-to-top skill composition, supported by automated environment construction and hybrid verification mechanisms. This synthesis stage produces 13.5K task samples, forming ClawGym-SynData. Building on these synthesized tasks, we then collect 24.5K interaction trajectories on the OpenClaw harness to train ClawGym-Agents.…。因此若该限制在目标 workload 中触发，不能把 `ClawGym: A Scalable Framework for Building Effective Claw Agents` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26904:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26904:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26904:end -->

<!-- review:SF-2026-ARXIV-2604-26934:start -->
#### World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning

问题、旧路径与约束变化：旧路径把 `World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning` 的判断留给固定策略、单次离线分数或未显式版本化的运行状态。

机制与 state/control owner：Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. 该机制将长期 owner 定位到 `MULTIMODAL-WORLD-MODELS`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。

Evaluation contract：Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. We post-train the VLM with a two-stage recipe on a compact dataset generated by this pipeline and evaluate it on multiple spatial reasoning benchmarks. World2VLM delivers consistent improvements over the base model across diverse benchmarks, including SAT-Real, SAT-Synthesized, VSI-Bench, and MindCube.

Trade-off / failure / fallback / coexistence：论文只在 exact-v1 披露的任务、模型与实验协议内支持上述结论；`World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning` 不证明跨模型、跨硬件、跨数据分布或生产 SLO 的普遍收益。失配时回退 current Books 的既有路径，并保留新旧机制并存。

<!-- claim:SF-2026-ARXIV-2604-26934:start -->只接受 arXiv:2604.26934v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2604-26934:end -->

Books Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2604-26934:end -->

<!-- review:SF-2026-ARXIV-2604-26951:start -->
#### Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models

问题、旧路径与约束变化：旧路径未显式拥有 `TRAIN-SFT` 中该 family 的受限状态。

机制与 state/control owner：Table 5 summarizes the complete set of training hyperparameters for both pipelines. dataset owner 拥有 trajectory/evidence，trainer 拥有 loss 与 checkpoint commit

Evaluation contract：Table 5 summarizes the complete set of training hyperparameters for both pipelines.

Trade-off / failure / fallback / coexistence：exact-v1 披露的反例/限制是：The empirical scope of this work is limited to a 0.6B-parameter student model using block diffusion with staircase attention. A primary avenue for future research is to scale the student model to 1.3B or 3B parameters to assess whether cross-architecture distillation efficiency improves as the capacity gap narrows. Furthermore, while the Tide framework is theoretically architecture-agnostic, empirical validation on alternative structures, such as continuous-state diffusion language models or encoder-style dLLMs, remains necessary. Adapting the proposed loss formulations from categorical distributions to continuous densities is a critical next step to broaden the framework’s applicability.。因此若该限制在目标 workload 中触发，不能把 `Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models` 的作者结果外推为生产正确性或 SLO 保证。

<!-- claim:SF-2026-ARXIV-2604-26951:start -->仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。<!-- claim:SF-2026-ARXIV-2604-26951:end -->

Books Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2604-26951:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-25975 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-25975 |
| SF-2026-ARXIV-2604-26020 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26020 |
| SF-2026-ARXIV-2604-26039 | score_7_9;forced_review | selected | DA-20260430-01 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260430-01 |
| SF-2026-ARXIV-2604-26074 | score_7_9;forced_review | selected | DA-20260430-02 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260430-02 |
| SF-2026-ARXIV-2604-26091 | score_7_9;forced_review | selected | DA-20260430-03 | — | Score=9/9 且属于当日最高跨系统设计影响；有限叙事预算不替代其余 Source Review。 | analysis:DA-20260430-03 |
| SF-2026-ARXIV-2604-26103 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26103 |
| SF-2026-ARXIV-2604-26152 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26152 |
| SF-2026-ARXIV-2604-26182 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26182 |
| SF-2026-ARXIV-2604-26197 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26197 |
| SF-2026-ARXIV-2604-26209 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26209 |
| SF-2026-ARXIV-2604-26256 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26256 |
| SF-2026-ARXIV-2604-26258 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26258 |
| SF-2026-ARXIV-2604-26274 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26274 |
| SF-2026-ARXIV-2604-26294 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26294 |
| SF-2026-ARXIV-2604-26334 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26334 |
| SF-2026-ARXIV-2604-26340 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26340 |
| SF-2026-ARXIV-2604-26360 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26360 |
| SF-2026-ARXIV-2604-26378 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26378 |
| SF-2026-ARXIV-2604-26388 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26388 |
| SF-2026-ARXIV-2604-26412 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26412 |
| SF-2026-ARXIV-2604-26460 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26460 |
| SF-2026-ARXIV-2604-26469 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26469 |
| SF-2026-ARXIV-2604-26470 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26470 |
| SF-2026-ARXIV-2604-26495 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26495 |
| SF-2026-ARXIV-2604-26505 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26505 |
| SF-2026-ARXIV-2604-26506 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26506 |
| SF-2026-ARXIV-2604-26511 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26511 |
| SF-2026-ARXIV-2604-26525 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26525 |
| SF-2026-ARXIV-2604-26557 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26557 |
| SF-2026-ARXIV-2604-26561 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26561 |
| SF-2026-ARXIV-2604-26622 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26622 |
| SF-2026-ARXIV-2604-26649 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26649 |
| SF-2026-ARXIV-2604-26666 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26666 |
| SF-2026-ARXIV-2604-26687 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26687 |
| SF-2026-ARXIV-2604-26694 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26694 |
| SF-2026-ARXIV-2604-26733 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26733 |
| SF-2026-ARXIV-2604-26752 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26752 |
| SF-2026-ARXIV-2604-26779 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26779 |
| SF-2026-ARXIV-2604-26815 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26815 |
| SF-2026-ARXIV-2604-26837 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26837 |
| SF-2026-ARXIV-2604-26848 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26848 |
| SF-2026-ARXIV-2604-26881 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26881 |
| SF-2026-ARXIV-2604-26889 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26889 |
| SF-2026-ARXIV-2604-26904 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26904 |
| SF-2026-ARXIV-2604-26934 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26934 |
| SF-2026-ARXIV-2604-26951 | score_7_9;forced_review | not_selected | — | — | Evidence Review 已完成，但相对当日 Top 3 未增加更高 Design Delta/System Reach；保留完整 Review。 | analysis-decision:SF-2026-ARXIV-2604-26951 |

<!-- analysis-decision:SF-2026-ARXIV-2604-25975:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-25975:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26020:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26020:end -->

<!-- analysis:DA-20260430-01:start -->
### Deep Analysis — SF-2026-ARXIV-2604-26039

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260430-01:end -->

<!-- analysis:DA-20260430-02:start -->
### Deep Analysis — SF-2026-ARXIV-2604-26074

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260430-02:end -->

<!-- analysis:DA-20260430-03:start -->
### Deep Analysis — SF-2026-ARXIV-2604-26091

该 family 的 Score V2=9/9；Source Review 已闭合问题、旧路径、机制 owner、evaluation boundary、trade-off 与共存条件。Deep Analysis 只提升叙事优先级，不改变 Evidence Gate。
<!-- analysis:DA-20260430-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26103:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26103:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26152:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26152:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26182:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26182:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26197:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26197:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26209:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26209:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26256:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26256:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26258:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26258:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26274:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26274:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26294:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26294:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26334:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26334:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26340:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26360:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26360:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26378:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26378:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26388:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26388:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26412:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26412:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26460:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26460:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26469:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26469:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26470:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26470:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26495:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26495:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26505:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26506:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26506:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26511:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26511:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26525:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26525:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26557:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26557:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26561:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26561:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26622:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26622:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26649:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26649:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26666:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26666:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26687:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26687:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26694:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26694:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26733:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26733:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26752:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26779:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26779:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26815:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26815:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26837:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26837:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26848:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26848:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26881:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26881:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26889:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26889:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26904:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26904:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26934:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26934:end -->

<!-- analysis-decision:SF-2026-ARXIV-2604-26951:start -->该 family 已完成所需 Source Review；因当日最多三个 Deep narrative units，未选入展示层不等于跳过证据审计。<!-- analysis-decision:SF-2026-ARXIV-2604-26951:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-25975 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存 | books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token; books/part-05-inference-system/46-continuous-batching.md#L16-从-static-batching-的问题开始 | existing:SF-2026-ARXIV-2604-25975 | delta:SF-2026-ARXIV-2604-25975 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-25975 |
| SF-2026-ARXIV-2604-26020 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-26020 | delta:SF-2026-ARXIV-2604-26020 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26020 |
| SF-2026-ARXIV-2604-26039 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader | existing:SF-2026-ARXIV-2604-26039 | delta:SF-2026-ARXIV-2604-26039 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26039 |
| SF-2026-ARXIV-2604-26074 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26074 | delta:SF-2026-ARXIV-2604-26074 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26074 |
| SF-2026-ARXIV-2604-26091 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L413-agent-runtime-state-machine | books/part-07-agent/83-mcp.md#L19-为什么需要协议层 | existing:SF-2026-ARXIV-2604-26091 | delta:SF-2026-ARXIV-2604-26091 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26091 |
| SF-2026-ARXIV-2604-26103 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26103 | delta:SF-2026-ARXIV-2604-26103 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26103 |
| SF-2026-ARXIV-2604-26152 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | books/part-06-ai-infrastructure/66-evaluation-system.md#L33-为什么-选一个分数-不是评估系统; books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约 | existing:SF-2026-ARXIV-2604-26152 | delta:SF-2026-ARXIV-2604-26152 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26152 |
| SF-2026-ARXIV-2604-26182 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation-从画面质量到干预结果 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化 | existing:SF-2026-ARXIV-2604-26182 | delta:SF-2026-ARXIV-2604-26182 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26182 |
| SF-2026-ARXIV-2604-26197 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1208-belief-state-先保存竞争假设-再决定事实 | books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移 | existing:SF-2026-ARXIV-2604-26197 | delta:SF-2026-ARXIV-2604-26197 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26197 |
| SF-2026-ARXIV-2604-26209 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token | books/part-05-inference-system/43-prefill.md#L18-如果逐个-token-读-prompt; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存 | existing:SF-2026-ARXIV-2604-26209 | delta:SF-2026-ARXIV-2604-26209 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26209 |
| SF-2026-ARXIV-2604-26256 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出 | books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | existing:SF-2026-ARXIV-2604-26256 | delta:SF-2026-ARXIV-2604-26256 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26256 |
| SF-2026-ARXIV-2604-26258 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L102-deterministic-spine-agentic-nodes | books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline | existing:SF-2026-ARXIV-2604-26258 | delta:SF-2026-ARXIV-2604-26258 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26258 |
| SF-2026-ARXIV-2604-26274 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26274 | delta:SF-2026-ARXIV-2604-26274 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26274 |
| SF-2026-ARXIV-2604-26294 | TRAIN-TENSOR-PARALLEL | books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | books/part-04-training-system/36-distributed-training.md#L25-单卡为什么会失败; books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么 | existing:SF-2026-ARXIV-2604-26294 | delta:SF-2026-ARXIV-2604-26294 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26294 |
| SF-2026-ARXIV-2604-26334 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26334 | delta:SF-2026-ARXIV-2604-26334 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26334 |
| SF-2026-ARXIV-2604-26340 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L145-rank-与-target-modules-决定更新空间 | books/part-04-training-system/29-sft.md#L18-pretraining-接口为什么不等于产品接口; books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好 | existing:SF-2026-ARXIV-2604-26340 | delta:SF-2026-ARXIV-2604-26340 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-26340 |
| SF-2026-ARXIV-2604-26360 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好 | books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始; books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程 | existing:SF-2026-ARXIV-2604-26360 | delta:SF-2026-ARXIV-2604-26360 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26360 |
| SF-2026-ARXIV-2604-26378 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26378 | delta:SF-2026-ARXIV-2604-26378 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26378 |
| SF-2026-ARXIV-2604-26388 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出 | books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | existing:SF-2026-ARXIV-2604-26388 | delta:SF-2026-ARXIV-2604-26388 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26388 |
| SF-2026-ARXIV-2604-26412 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始 | books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | existing:SF-2026-ARXIV-2604-26412 | delta:SF-2026-ARXIV-2604-26412 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26412 |
| SF-2026-ARXIV-2604-26460 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-26460 | delta:SF-2026-ARXIV-2604-26460 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26460 |
| SF-2026-ARXIV-2604-26469 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始 | books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | existing:SF-2026-ARXIV-2604-26469 | delta:SF-2026-ARXIV-2604-26469 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26469 |
| SF-2026-ARXIV-2604-26470 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L249-routing-placement-与-autoscaling | books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26470 | delta:SF-2026-ARXIV-2604-26470 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26470 |
| SF-2026-ARXIV-2604-26495 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-26495 | delta:SF-2026-ARXIV-2604-26495 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26495 |
| SF-2026-ARXIV-2604-26505 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26505 | delta:SF-2026-ARXIV-2604-26505 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-26505 |
| SF-2026-ARXIV-2604-26506 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26506 | delta:SF-2026-ARXIV-2604-26506 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26506 |
| SF-2026-ARXIV-2604-26511 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26511 | delta:SF-2026-ARXIV-2604-26511 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26511 |
| SF-2026-ARXIV-2604-26525 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设 | existing:SF-2026-ARXIV-2604-26525 | delta:SF-2026-ARXIV-2604-26525 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26525 |
| SF-2026-ARXIV-2604-26557 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26557 | delta:SF-2026-ARXIV-2604-26557 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26557 |
| SF-2026-ARXIV-2604-26561 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline | books/part-07-agent/81-workflow.md#L16-一个循环为什么不够; books/part-07-agent/83-mcp.md#L19-为什么需要协议层 | existing:SF-2026-ARXIV-2604-26561 | delta:SF-2026-ARXIV-2604-26561 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26561 |
| SF-2026-ARXIV-2604-26622 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1208-belief-state-先保存竞争假设-再决定事实 | books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移 | existing:SF-2026-ARXIV-2604-26622 | delta:SF-2026-ARXIV-2604-26622 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26622 |
| SF-2026-ARXIV-2604-26649 | AGENT-RAG | books/part-07-agent/76-rag.md#L420-rag-不消除-hallucination | books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界 | existing:SF-2026-ARXIV-2604-26649 | delta:SF-2026-ARXIV-2604-26649 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26649 |
| SF-2026-ARXIV-2604-26666 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L102-deterministic-spine-agentic-nodes | books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline | existing:SF-2026-ARXIV-2604-26666 | delta:SF-2026-ARXIV-2604-26666 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26666 |
| SF-2026-ARXIV-2604-26687 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出 | books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么-把权重文件切开-不够 | existing:SF-2026-ARXIV-2604-26687 | delta:SF-2026-ARXIV-2604-26687 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26687 |
| SF-2026-ARXIV-2604-26694 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链 | existing:SF-2026-ARXIV-2604-26694 | delta:SF-2026-ARXIV-2604-26694 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26694 |
| SF-2026-ARXIV-2604-26733 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens | books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | existing:SF-2026-ARXIV-2604-26733 | delta:SF-2026-ARXIV-2604-26733 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26733 |
| SF-2026-ARXIV-2604-26752 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始 | books/part-04-training-system/33-grpo.md#L31-为什么移除-critic-会有吸引力; books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够 | existing:SF-2026-ARXIV-2604-26752 | delta:SF-2026-ARXIV-2604-26752 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26752 |
| SF-2026-ARXIV-2604-26779 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始 | books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始 | existing:SF-2026-ARXIV-2604-26779 | delta:SF-2026-ARXIV-2604-26779 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26779 |
| SF-2026-ARXIV-2604-26815 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L253-monitoring-也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10-本章要回答的问题; books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约 | existing:SF-2026-ARXIV-2604-26815 | delta:SF-2026-ARXIV-2604-26815 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26815 |
| SF-2026-ARXIV-2604-26837 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存 | books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token; books/part-05-inference-system/46-continuous-batching.md#L16-从-static-batching-的问题开始 | existing:SF-2026-ARXIV-2604-26837 | delta:SF-2026-ARXIV-2604-26837 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26837 |
| SF-2026-ARXIV-2604-26848 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation-从画面质量到干预结果 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化 | existing:SF-2026-ARXIV-2604-26848 | delta:SF-2026-ARXIV-2604-26848 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26848 |
| SF-2026-ARXIV-2604-26881 | PLATFORM-MULTI-TENANT | books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别 | books/part-06-ai-infrastructure/70-cost.md#L16-资源时间是共同底座; books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始 | existing:SF-2026-ARXIV-2604-26881 | delta:SF-2026-ARXIV-2604-26881 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26881 |
| SF-2026-ARXIV-2604-26889 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始 | books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏 | existing:SF-2026-ARXIV-2604-26889 | delta:SF-2026-ARXIV-2604-26889 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26889 |
| SF-2026-ARXIV-2604-26904 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据-而不是从指标到目标 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标-再选择可测信号 | existing:SF-2026-ARXIV-2604-26904 | delta:SF-2026-ARXIV-2604-26904 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26904 |
| SF-2026-ARXIV-2604-26934 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation-从画面质量到干预结果 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化 | existing:SF-2026-ARXIV-2604-26934 | delta:SF-2026-ARXIV-2604-26934 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26934 |
| SF-2026-ARXIV-2604-26951 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L415-full-fine-tuning-与-parameter-efficient-adaptation | books/part-04-training-system/28-pretraining.md#L18-从随机参数开始会发生什么; books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始 | existing:SF-2026-ARXIV-2604-26951 | delta:SF-2026-ARXIV-2604-26951 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-26951 |

<!-- books-review:SF-2026-ARXIV-2604-25975:start -->
<!-- existing:SF-2026-ARXIV-2604-25975:start -->真实 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存` 正文：## 如果完全不缓存 Prompt 长度为 `T_p`，已经生成 `i` 个 tokens 时，朴素 Decode 可以把全部 `T_p+i` 个 tokens 再送入模型，只取最后位置 logits。 ```text step 1: recompute T_p tokens step 2: recompute T_p + 1 tokens step 3: recompute T_p + 2 tokens ... ``` 历史 positions 的 projections、Attention、MLP 和 layer outputs 被反复重算，但 causal mask 保证未来 tokens 不会改变历史位置已经得到的 K/V。这正是可缓存的不变量。；相邻章 `books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token; books/part-05-inference-system/46-continuous-batching.md#L16-从-static-batching-的问题开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ffe365d267a891cdec085543157fd861f0bb8a34f60e2c7b19638a395c4345a7。<!-- existing:SF-2026-ARXIV-2604-25975:end -->
<!-- delta:SF-2026-ARXIV-2604-25975:start -->cache manager 拥有 block identity、placement 与 eviction，scheduler 只引用合法 handle<!-- delta:SF-2026-ARXIV-2604-25975:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-25975:end -->

<!-- books-review:SF-2026-ARXIV-2604-26020:start -->
<!-- existing:SF-2026-ARXIV-2604-26020:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-26020:end -->
<!-- delta:SF-2026-ARXIV-2604-26020:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-26020:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26020:end -->

<!-- books-review:SF-2026-ARXIV-2604-26039:start -->
<!-- existing:SF-2026-ARXIV-2604-26039:start -->真实 owner `books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 正文：## 从计算图开始 理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。 朴素执行方式会产生很多额外开销： - 多个小算子分别 launch kernel。 - 中间结果频繁写回 HBM 再读出。 - 常量表达式运行时重复计算。 - 独立算子没有被合理并行调度。 图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。；相邻章 `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始; books/part-05-inference-system/50-vllm.md#L18-serving-引擎不是模型-loader` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=e5d5d64f08769bf2b69fe063ae4524c62f942da4e0c48b2966d39ac8e214af1b。<!-- existing:SF-2026-ARXIV-2604-26039:end -->
<!-- delta:SF-2026-ARXIV-2604-26039:start -->compiled runtime 拥有 plan/shape/kernel identity，fallback backend 保留兼容路径<!-- delta:SF-2026-ARXIV-2604-26039:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26039:end -->

<!-- books-review:SF-2026-ARXIV-2604-26074:start -->
<!-- existing:SF-2026-ARXIV-2604-26074:start -->真实 owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 正文：## 从 memory hierarchy 开始 GPU 上并不是只有一种 memory。大致可以把它理解为： ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ``` 越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。 这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。；相邻章 `books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=69f1e67e838cbd2de7f2c79390c35ce4cd36f897e8dcd54d64e8f9c627ab67fd。<!-- existing:SF-2026-ARXIV-2604-26074:end -->
<!-- delta:SF-2026-ARXIV-2604-26074:start -->memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射<!-- delta:SF-2026-ARXIV-2604-26074:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26074:end -->

<!-- books-review:SF-2026-ARXIV-2604-26091:start -->
<!-- existing:SF-2026-ARXIV-2604-26091:start -->真实 owner `books/part-07-agent/84-agent-platform.md#L403-agent-runtime-state-machine` 正文：## Agent Runtime State Machine 一个通用 run 可表达为： ```text Created → ContextReady → Planning → Acting → Observing → Reflecting / Replanning → Waiting → Succeeded \| Failed \| Cancelled \| Escalated ``` 具体 workflow 可增加 domain states。关键是每次 transition 都可恢复、可审计，并绑定 actor、policy、budget 和 side-effect evidence。；相邻章 `books/part-07-agent/83-mcp.md#L19-为什么需要协议层` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=b963414e7df5fef56194247e1c803fb24d3ccab30bf6e447175fdae3b9e99346。<!-- existing:SF-2026-ARXIV-2604-26091:end -->
<!-- delta:SF-2026-ARXIV-2604-26091:start -->platform 拥有跨请求 policy、lifecycle 与 human-control state，model 只提出动作<!-- delta:SF-2026-ARXIV-2604-26091:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26091:end -->

<!-- books-review:SF-2026-ARXIV-2604-26103:start -->
<!-- existing:SF-2026-ARXIV-2604-26103:start -->真实 owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 正文：## 从 memory hierarchy 开始 GPU 上并不是只有一种 memory。大致可以把它理解为： ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ``` 越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。 这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。；相邻章 `books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=69f1e67e838cbd2de7f2c79390c35ce4cd36f897e8dcd54d64e8f9c627ab67fd。<!-- existing:SF-2026-ARXIV-2604-26103:end -->
<!-- delta:SF-2026-ARXIV-2604-26103:start -->memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射<!-- delta:SF-2026-ARXIV-2604-26103:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26103:end -->

<!-- books-review:SF-2026-ARXIV-2604-26152:start -->
<!-- existing:SF-2026-ARXIV-2604-26152:start -->真实 owner `books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 正文：## 先定义目标，再选择可测信号 ### Context generator 是 pre-failure sensor identity 的一部分 agent identity monitor 以固定 probe 的 next-token distribution、sqrt-JSD geometry 与 magnitude homology 追踪 conditioning；但 diverse-padding 对照推翻了原 repetitive-padding drift trajectory。 **Trade-off、failure、共存与回退。** 作者自评、单模型单 agent、单日采集且无 reconstitution control；几何诊断潜力没有被真实纵向 drift 证实。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。 #### Review notes - `SF-2026-ARXIV-2606-21843` — primary `arXiv:2606.21843v1`；exact-v1 URL=`https://arxiv.org/html/2606.21843v1`；Method=`https://arxiv.org/html/2606.21843v1 — §3.1 Ada: a persistent AI agent; §3.4 The probe battery`；Evaluation=`https://arxiv.org/html/2606.21843v1 — §4 Magnitude Baseline; §5.6 Drift experiment`；Non-proof=`https://arxiv.org/html/2606.21843v1 — §6.3 Limitations — Drift trajectory is a padding ar；相邻章 `books/part-06-ai-infrastructure/66-evaluation-system.md#L33-为什么选一个分数不是评估系统; books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=36240d05618816e1c00eb6cd1abd684345549a36b62f03dab56bab99956b6bdf。<!-- existing:SF-2026-ARXIV-2604-26152:end -->
<!-- delta:SF-2026-ARXIV-2604-26152:start -->observability owner 版本化 model/agent semantic signals，release owner 决定告警后的动作<!-- delta:SF-2026-ARXIV-2604-26152:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26152:end -->

<!-- books-review:SF-2026-ARXIV-2604-26182:start -->
<!-- existing:SF-2026-ARXIV-2604-26182:start -->真实 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation从画面质量到干预结果` 正文：## Evaluation：从画面质量到干预结果 ### 视频只有编译成可执行 Transition，才能测试 Belief Planning Egocentric video 提供观察序列，却没有天然的 action precondition、object state 或 counterfactual transition。把片段编译成带 provenance 的 symbolic graph 和 transition rules，可让 planner 在可执行 world 中测试 belief update；compiler 拥有 observation-to-state proposal，environment verifier 拥有规则执行和 contradiction。它把视觉数据变成可重复测试，代价是符号化遗漏、规则错误和 domain-specific ontology；开放物理控制仍需真实闭环，不能把 cooking benchmark 的可执行性外推成通用 world-model fidelity。 一个 evidence ladder： ```text perceptual plausibility → temporal consistency → state reconstruction → action-conditioned prediction → counterfactual discrimination → long-horizon calibration → closed-loop task outcome → safety under perturbation ``` 低层证据不能替代高层。FVD 或人类偏好可评价视频观感，不证明 action consequence；one-step error 低不证明 long rollout；simulator 内 success 不证明 sim-to-real。 evaluation contract 应绑定 environment version、initial-state distrib；相邻章 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=fcdffa1f4e6dc30353d01f36aa02d75be6cd86ac092db86bb50f5a6ec9aa0e8d。<!-- existing:SF-2026-ARXIV-2604-26182:end -->
<!-- delta:SF-2026-ARXIV-2604-26182:start -->World models of embodied agents predict future observations conditioned on an action taken by the agent. For complex embodiments, action spaces are high-dimensional and difficult to specify: for example, precisely controlling a human agent requires specifying the motion of each joint. This makes the world model hard to control and expensive to plan with as search-based methods like CEM scale poorly with action dimensionality. 该机制将长期 owner 定位到 `MULTIMODAL-WORLD-MODELS`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26182:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.26182v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26182:end -->

<!-- books-review:SF-2026-ARXIV-2604-26197:start -->
<!-- existing:SF-2026-ARXIV-2604-26197:start -->真实 owner `books/part-07-agent/77-memory.md#L1208-belief-state先保存竞争假设再决定事实` 正文：## Belief State：先保存竞争假设，再决定事实 把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。 这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]；相邻章 `books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a241ab934a3c3b722b6cbce0351db40d0c918fb10b89a72e0c4463ffeaf7599e。<!-- existing:SF-2026-ARXIV-2604-26197:end -->
<!-- delta:SF-2026-ARXIV-2604-26197:start -->memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图<!-- delta:SF-2026-ARXIV-2604-26197:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26197:end -->

<!-- books-review:SF-2026-ARXIV-2604-26209:start -->
<!-- existing:SF-2026-ARXIV-2604-26209:start -->真实 owner `books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token` 正文：## 为什么不能并行写出未来 Token 语言模型定义： ```text p(y_1,...,y_T_o \| x) = product_i p(y_i \| x, y_<i) ``` 要计算 `y_i` 的分布，必须先知道实际选择的 `y_<i`。Sampling 可能使下一 token 不等于当前最高概率 token，stop conditions 也会动态结束请求。因此不能把未知的未来 positions 当作 Prefill 中已知的 prompt positions 一起 exact 执行。 这不是 GPU 不够强，而是计算图中存在真实 data dependency。；相邻章 `books/part-05-inference-system/43-prefill.md#L18-如果逐个-token-读-prompt; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ed3f0242eee27efadff945433b83cb509557d634d3401ce95ad85f86d2a40b93。<!-- existing:SF-2026-ARXIV-2604-26209:end -->
<!-- delta:SF-2026-ARXIV-2604-26209:start -->decoder runtime 拥有 token frontier、cache identity 与 commit order<!-- delta:SF-2026-ARXIV-2604-26209:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26209:end -->

<!-- books-review:SF-2026-ARXIV-2604-26256:start -->
<!-- existing:SF-2026-ARXIV-2604-26256:start -->真实 owner `books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出` 正文：## Failure 不再是单进程退出 一个 rank crash 可能让其他 ranks 阻塞在 collective。训练平台需要： - Detect failed/stuck ranks。 - 终止或重建整个 process group。 - 选择 committed checkpoint。 - 恢复相同或新 world size。 - 保持 data cursor 与 job identity。 Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 35 章的 checkpoint correctness 是分布式容错的前提。 通信错误也不一定只能采用“任意 packet loss 都重传”的单一合同。可靠传输在 loss 罕见、梯度语义要求精确时最清楚；同步训练的 microburst 若触发成批重传，tail latency 会被最慢 flow 放大。一条实验性分支让 transport 按训练 phase 和已验证 tolerance 接受**有界 loss**：model/training owner 先证明该 phase、tensor class 与 loss budget 下的收敛影响，transport 再用 round identity、packet bitmap 和上限强制执行，超过预算立即回退可靠路径或重试整轮。 ```text phase + tensor/round identity + admitted loss budget → burst-aware transport → packet bitmap and bounded completion → optimizer step or reliable retransmit fallback ``` 这里“模型能容忍”不能由网络层自行推断，单个 workload 的经验阈值也不能写成通用 40%。该机制以更复杂的收敛证据、bitmap state 和 silent-corruption 风险换较短 ；相邻章 `books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=35cb2eb9f2e0eff9dac03ee4db2cf2530c5f89ba9a7b8c92671958adf7b8df8e。<!-- existing:SF-2026-ARXIV-2604-26256:end -->
<!-- delta:SF-2026-ARXIV-2604-26256:start -->distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer<!-- delta:SF-2026-ARXIV-2604-26256:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26256:end -->

<!-- books-review:SF-2026-ARXIV-2604-26258:start -->
<!-- existing:SF-2026-ARXIV-2604-26258:start -->真实 owner `books/part-07-agent/81-workflow.md#L102-deterministic-spineagentic-nodes` 正文：## Deterministic Spine，Agentic Nodes 适合 deterministic 的部分： - identity、authorization、budgets； - required gates； - retry/backoff/timeouts； - state transitions； - side-effect records； - cancellation/compensation； - terminal success criteria。 适合 model-driven 的部分： - interpreting ambiguous intent； - drafting content； - proposing plans/tool arguments； - ranking alternatives； - diagnosing unstructured failure。 这种组合既保留模型灵活性，又让业务不变量可测试。 ### 从一次性脚本到平台拥有的可编辑 DAG 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。 这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。 ### Template、Realized Graph 与 Trace 不是同一个对象 固定 code-defined template 便于审查、复现和强 verifier，仍是稳定 wor；相邻章 `books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=876ac2cc1f59f9376dcee3315ca5f38e95345018a37b1f888b9787534e149a1d。<!-- existing:SF-2026-ARXIV-2604-26258:end -->
<!-- delta:SF-2026-ARXIV-2604-26258:start -->workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步<!-- delta:SF-2026-ARXIV-2604-26258:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26258:end -->

<!-- books-review:SF-2026-ARXIV-2604-26274:start -->
<!-- existing:SF-2026-ARXIV-2604-26274:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-26274:end -->
<!-- delta:SF-2026-ARXIV-2604-26274:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-26274:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26274:end -->

<!-- books-review:SF-2026-ARXIV-2604-26294:start -->
<!-- existing:SF-2026-ARXIV-2604-26294:start -->真实 owner `books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 正文：## 为什么“把权重文件切开”不够 线性层： ```text Y = X W X [M,d_in] W [d_in,d_out] Y [M,d_out] ``` 随机把 `W` bytes 平均分给两张 GPU，不会自动得到可组合计算。切分必须对应矩阵维度，并明确： - 每个 rank 需要哪部分输入。 - Local GEMM 输出是完整值还是 partial sum。 - 下一 operator 能否直接消费分片。 - Forward 与 backward 在哪里 collective。 Tensor Parallel 是 operator graph transformation，不是 storage sharding 的别名。；相邻章 `books/part-04-training-system/36-distributed-training.md#L25-单卡为什么会失败; books/part-04-training-system/38-pipeline-parallel.md#L22-只有-layer-partition-会发生什么` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a0c1ec60ea9dcfa334ef4fe61a1584e8475fffc3c835c0f51477f74e0ae59b78。<!-- existing:SF-2026-ARXIV-2604-26294:end -->
<!-- delta:SF-2026-ARXIV-2604-26294:start -->parallel plan owner 冻结 tensor layout/collective，kernel 只消费一致 shard<!-- delta:SF-2026-ARXIV-2604-26294:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26294:end -->

<!-- existing:SF-2026-ARXIV-2604-26334:start -->current owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 已顺读：## 从 memory hierarchy 开始  GPU 上并不是只有一种 memory。大致可以把它理解为：  ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ```  越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。  这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。  ## 显存里到底有什么；相邻 refs=books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏。<!-- existing:SF-2026-ARXIV-2604-26334:end -->
<!-- delta:SF-2026-ARXIV-2604-26334:start -->VRAM 受限时在 CPU/GPU 间 pipeline 分片并重叠传输与执行。<!-- delta:SF-2026-ARXIV-2604-26334:end -->
<!-- books-review:SF-2026-ARXIV-2604-26334:start -->Decision=`No Change — Existing Coverage`；收益依赖 PCIe、layer shape 与 batch，不能证明通用低延迟或多租户 SLO。<!-- books-review:SF-2026-ARXIV-2604-26334:end -->

<!-- existing:SF-2026-ARXIV-2604-26340:start -->current owner `books/part-04-training-system/30-lora.md#L145-rank-与-target-modules-决定更新空间` 已顺读：## Rank 与 target modules 决定更新空间  更高 rank 提供更大的更新子空间，也增加 trainable state、compute 和 overfitting 风险。更低 rank 更便宜，却可能限制复杂适配。  还必须选择 target modules，例如：  - Attention 的 Q/K/V/O projections。 - MLP 的 up/gate/down projections。 - 其他模型特有 linear layers。  只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。  Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。  Update subspace 也可以从训练前静态选择，演进为由当前 activation 动态选择。以 attention Q/K feature magnitude 生成 transient row mask，可以让 optimizer 只更新当步被选中的 rows，而不改变 inference graph：；相邻 refs=books/part-04-training-system/29-sft.md#L18-pretraining-接口为什么不等于产品接口; books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好。<!-- existing:SF-2026-ARXIV-2604-26340:end -->
<!-- delta:SF-2026-ARXIV-2604-26340:start -->LoRA-MoE 在 exploratory training 后按 module 的 Gini、routing entropy 与 drift 非对称裁剪 experts，而不是使用全局统一 mask。<!-- delta:SF-2026-ARXIV-2604-26340:end -->
<!-- books-review:SF-2026-ARXIV-2604-26340:start -->Decision=`Integrate`；只覆盖作者模型/任务；探索阶段有额外成本，错误 pruning 会破坏专家覆盖，不能外推到 base MoE 或任意 adapter。<!-- books-review:SF-2026-ARXIV-2604-26340:end -->

<!-- books-review:SF-2026-ARXIV-2604-26360:start -->
<!-- existing:SF-2026-ARXIV-2604-26360:start -->真实 owner `books/part-04-training-system/31-rlhf.md#L18-demonstration-为什么不足以表达偏好` 正文：## Demonstration 为什么不足以表达偏好 对同一个 prompt，多个回答可能都正确，但在 helpfulness、clarity、safety、conciseness 和 style 上不同。若只提供一个 SFT reference： ```text prompt -> one target response ``` 所有不同 wording 都会在 token-level loss 中偏离 reference，即使它们同样可接受。 Preference comparison 改写监督问题： ```text prompt x candidate y_a candidate y_b human chooses y_w over y_l ``` 它不要求标注者从空白开始写完美答案，却仍需要明确 rubric。若不同标注者对“好”的定义不同，pairwise label 只是某个群体、时间和 policy 下的偏好样本，不是客观真理。；相邻章 `books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始; books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=f47330b0071ac1f6fd3beb7eac7bee51312e668f7c5f5fca76159edd840d2414。<!-- existing:SF-2026-ARXIV-2604-26360:end -->
<!-- delta:SF-2026-ARXIV-2604-26360:start -->Reinforcement learning from human feedback (RLHF) systems face a compounding alignment challenge: not only are learned reward models uncertain about unseen state-action pairs, but the human preference annotations they are trained on are themselves inconsistent, context-dependent, and noisy. Existing approaches address these uncertainty sources in isolation - epistemic uncertainty is used to guide exploration, while preference uncertainty is absorbed during reward model training but discarded during policy optimization. We introduce Uncertainty-Aware Reward Discounting (UARD), a principled framework that jointly models epistemic uncertainty in value estimation via ensemble disagreement and aleatoric uncertainty in human preference annotations via annotator variability, combining these signals through a confidence-adjusted Reliability Filter that adaptively modulates reward weighting durin 该机制将长期 owner 定位到 `TRAIN-RLHF`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26360:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.26360v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26360:end -->

<!-- books-review:SF-2026-ARXIV-2604-26378:start -->
<!-- existing:SF-2026-ARXIV-2604-26378:start -->真实 owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 正文：## 从 memory hierarchy 开始 GPU 上并不是只有一种 memory。大致可以把它理解为： ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ``` 越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。 这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。；相邻章 `books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=69f1e67e838cbd2de7f2c79390c35ce4cd36f897e8dcd54d64e8f9c627ab67fd。<!-- existing:SF-2026-ARXIV-2604-26378:end -->
<!-- delta:SF-2026-ARXIV-2604-26378:start -->memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射<!-- delta:SF-2026-ARXIV-2604-26378:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26378:end -->

<!-- books-review:SF-2026-ARXIV-2604-26388:start -->
<!-- existing:SF-2026-ARXIV-2604-26388:start -->真实 owner `books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出` 正文：## Failure 不再是单进程退出 一个 rank crash 可能让其他 ranks 阻塞在 collective。训练平台需要： - Detect failed/stuck ranks。 - 终止或重建整个 process group。 - 选择 committed checkpoint。 - 恢复相同或新 world size。 - 保持 data cursor 与 job identity。 Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 35 章的 checkpoint correctness 是分布式容错的前提。 通信错误也不一定只能采用“任意 packet loss 都重传”的单一合同。可靠传输在 loss 罕见、梯度语义要求精确时最清楚；同步训练的 microburst 若触发成批重传，tail latency 会被最慢 flow 放大。一条实验性分支让 transport 按训练 phase 和已验证 tolerance 接受**有界 loss**：model/training owner 先证明该 phase、tensor class 与 loss budget 下的收敛影响，transport 再用 round identity、packet bitmap 和上限强制执行，超过预算立即回退可靠路径或重试整轮。 ```text phase + tensor/round identity + admitted loss budget → burst-aware transport → packet bitmap and bounded completion → optimizer step or reliable retransmit fallback ``` 这里“模型能容忍”不能由网络层自行推断，单个 workload 的经验阈值也不能写成通用 40%。该机制以更复杂的收敛证据、bitmap state 和 silent-corruption 风险换较短 ；相邻章 `books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=35cb2eb9f2e0eff9dac03ee4db2cf2530c5f89ba9a7b8c92671958adf7b8df8e。<!-- existing:SF-2026-ARXIV-2604-26388:end -->
<!-- delta:SF-2026-ARXIV-2604-26388:start -->distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer<!-- delta:SF-2026-ARXIV-2604-26388:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26388:end -->

<!-- books-review:SF-2026-ARXIV-2604-26412:start -->
<!-- existing:SF-2026-ARXIV-2604-26412:start -->真实 owner `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始` 正文：## 从 Decode 串行瓶颈开始 普通 Decode 的流程是： ```text 大模型生成 token 1 → 把 token 1 接回上下文 → 大模型生成 token 2 → 把 token 2 接回上下文 → 大模型生成 token 3 ... ``` 生成 `K` 个 token，就要运行 `K` 次大模型 forward。这个串行依赖无法简单通过扩大 batch 消除，因为同一个请求内部下一个 token 依赖上一个 token。 这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？；相邻章 `books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=2f7a8d5930de3ee03ecafc0aac2899817f6c6856721f4c2170d134cc9744c096。<!-- existing:SF-2026-ARXIV-2604-26412:end -->
<!-- delta:SF-2026-ARXIV-2604-26412:start -->draft 只拥有 proposal，target verifier 拥有 acceptance 与 token commit<!-- delta:SF-2026-ARXIV-2604-26412:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26412:end -->

<!-- books-review:SF-2026-ARXIV-2604-26460:start -->
<!-- existing:SF-2026-ARXIV-2604-26460:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-26460:end -->
<!-- delta:SF-2026-ARXIV-2604-26460:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-26460:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26460:end -->

<!-- books-review:SF-2026-ARXIV-2604-26469:start -->
<!-- existing:SF-2026-ARXIV-2604-26469:start -->真实 owner `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始` 正文：## 从 Decode 串行瓶颈开始 普通 Decode 的流程是： ```text 大模型生成 token 1 → 把 token 1 接回上下文 → 大模型生成 token 2 → 把 token 2 接回上下文 → 大模型生成 token 3 ... ``` 生成 `K` 个 token，就要运行 `K` 次大模型 forward。这个串行依赖无法简单通过扩大 batch 消除，因为同一个请求内部下一个 token 依赖上一个 token。 这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？；相邻章 `books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=2f7a8d5930de3ee03ecafc0aac2899817f6c6856721f4c2170d134cc9744c096。<!-- existing:SF-2026-ARXIV-2604-26469:end -->
<!-- delta:SF-2026-ARXIV-2604-26469:start -->Large Language Models (LLMs) have become widely used for Software Engineering (SE) tasks, spanning from function-level code generation to complex repository-level workflows. However, the high latency of autoregressive inference remains a significant bottleneck, hindering their deployment in interactive environments. While Speculative Decoding (SD) offers a promising technique for lossless acceleration, prior research on long-context repository-level tasks and complex agentic interactions remains limited. 该机制将长期 owner 定位到 `INFER-SPECULATIVE-DECODING`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26469:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.26469v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26469:end -->

<!-- existing:SF-2026-ARXIV-2604-26470:start -->current owner `books/part-05-inference-system/56-inference-scheduling.md#L249-routing-placement-与-autoscaling` 已顺读：## Routing、Placement 与 Autoscaling  ### Heterogeneous Offload 必须同时预算 Preemption 与 State Transfer  固定放置在同构 GPU 上最容易预测；设备异构或显存紧张后，offload 可扩大可服务集合，但 scheduler 必须拥有算子/权重 residency、迁移时间与 preemption checkpoint，不能只按空闲容量路由。收益是提高利用率，代价是迁移抖动、恢复状态和尾延迟；SLO 紧或迁移成本不可测时回退静态 placement。<!-- source-family:SF-2026-ARXIV-2605-19593 --> exact-v1 §3–5 只验证其异构设置，§6 不支持通用 offload 阈值。  Routing 选择已有 endpoints，考虑 queue、KV locality、adapter 与 topology；placement 决定 model workers/parallel groups 位于哪些 GPUs/nodes；autoscaling 根据较慢时间尺度的 demand 改变 endpoint 数量。  把三者混成“调度”会导致错误控制。例如 EPP 把请求路由到某 Pod，不能替代 Kubernetes GPU scheduler 为 Pod 找节点；engine scheduler 让 token 进入下一 iteration，也不能创建新 GPU capacity。  ### 低带宽拓扑要联合预算 Hops、Bytes 与 Steps  单数据中心、高带宽互联中，固定 pipeline placement 与局部通信优化通常足够，稳定拓扑也让故障和 tail latency 更容易解释。GPU 分散在低带宽、跨地域节点后，只看空闲显存或单跳带宽会失真：少放一个 transformer block 可能增加每个 decode step 的跨节点 hops；为了减少 hops 而 offload KV，又会引入 host-memory traffic；lossless compression 改变每跳 bytes，speculative decoding 则可能改变完成同样输出所需的串行 decode steps。  因此 placement planner 应在同一 GPU-memory constraint 下联合选择 block consolidation、KV residency/offload、pipeline hops、micro-batch overlap、lossless communication representation 与 speculative-work budget。Planner 只提出 versioned plan；cache owner 确认 KV location，communicator 确认 payload/epoch，runtime 才在 plan boundary commit，autoscaler仍负责未来 capacity。第 48 章仍拥有 draft、verify、acceptance 与 committed-token correctness；本章只；相邻 refs=books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段-两种节奏。<!-- existing:SF-2026-ARXIV-2604-26470:end -->
<!-- delta:SF-2026-ARXIV-2604-26470:start -->hierarchical adaptive edge inference 依据设备/网络状态在层级节点间选择执行。<!-- delta:SF-2026-ARXIV-2604-26470:end -->
<!-- books-review:SF-2026-ARXIV-2604-26470:start -->Decision=`No Change — Existing Coverage`；结果受作者 topology、模型和网络分布限制，未证明生产异构 fleet 的全局最优。<!-- books-review:SF-2026-ARXIV-2604-26470:end -->

<!-- books-review:SF-2026-ARXIV-2604-26495:start -->
<!-- existing:SF-2026-ARXIV-2604-26495:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-26495:end -->
<!-- delta:SF-2026-ARXIV-2604-26495:start -->Code-driven auditing fails when correctness depends on what the specification requires rather than how the code is written. Production blockchain networks expose this directly: byzantine consensus runs many independent clients of a shared specification, so a specification-divergence defect in one client can fork the network or halt finality. Existing tools reason one repository at a time, with no shared baseline held constant across implementations. 该机制将长期 owner 定位到 `PLATFORM-EVALUATION-SYSTEM`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26495:end --> Decision=`No Change — Existing Coverage`；evidence boundary：只接受 arXiv:2604.26495v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26495:end -->

<!-- books-review:SF-2026-ARXIV-2604-26505:start -->
<!-- existing:SF-2026-ARXIV-2604-26505:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-26505:end -->
<!-- delta:SF-2026-ARXIV-2604-26505:start -->Dynamic quantization emerged as a practical approach to increase the utilization and efficiency of the machine learning serving flow. Unlike static quantization, which applies quantization offline, dynamic quantization operates on tensors at run-time, adapting its parameters to the actual input data. Today's mainstream machine learning frameworks, including ML compilers and inference engines, frequently recommend dynamic quantization as an initial step for optimizing model serving. 该机制将长期 owner 定位到 `PLATFORM-SECURITY`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26505:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.26505v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26505:end -->

<!-- books-review:SF-2026-ARXIV-2604-26506:start -->
<!-- existing:SF-2026-ARXIV-2604-26506:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-26506:end -->
<!-- delta:SF-2026-ARXIV-2604-26506:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-26506:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26506:end -->

<!-- books-review:SF-2026-ARXIV-2604-26511:start -->
<!-- existing:SF-2026-ARXIV-2604-26511:start -->真实 owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 正文：## 从资产与信任边界开始 需要保护的资产包括： - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。 主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。；相邻章 `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=cd99007e2f9b12ccf2bc7cd075bbf73c3b935255bf06bda7068b8f624de239ca。<!-- existing:SF-2026-ARXIV-2604-26511:end -->
<!-- delta:SF-2026-ARXIV-2604-26511:start -->policy/CI/sandbox 拥有 invariant 与 commit authority，model 仅提出不可信 proposal<!-- delta:SF-2026-ARXIV-2604-26511:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26511:end -->

<!-- existing:SF-2026-ARXIV-2604-26525:start -->current owner `books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读：## 从资产与信任边界开始  需要保护的资产包括：  - source data、labels 与 user context； - code、images、dependencies 与 credentials； - checkpoints、adapters、tokenizers 与 prompts； - registry metadata、evaluation 与 approvals； - GPU nodes、runtime memory 与 KV Cache； - APIs、tools、business systems 与 audit evidence。  主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。  ## 生命周期威胁  ```text；相邻 refs=books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别; books/part-06-ai-infrastructure/73-production-best-practice.md#L16-poc-隐含了哪些假设。<!-- existing:SF-2026-ARXIV-2604-26525:end -->
<!-- delta:SF-2026-ARXIV-2604-26525:start -->同态加密同时覆盖 RAG document/query，相似度、排序和更新在 ciphertext 上完成。<!-- delta:SF-2026-ARXIV-2604-26525:end -->
<!-- books-review:SF-2026-ARXIV-2604-26525:start -->Decision=`No Change — Existing Coverage`；CKKS 近似误差可改变 ranking；仍有 access-pattern/ranking leakage 与显著计算成本，未证明生产规模 SLO。<!-- books-review:SF-2026-ARXIV-2604-26525:end -->

<!-- books-review:SF-2026-ARXIV-2604-26557:start -->
<!-- existing:SF-2026-ARXIV-2604-26557:start -->真实 owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 正文：## 从 memory hierarchy 开始 GPU 上并不是只有一种 memory。大致可以把它理解为： ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ``` 越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。 这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。；相邻章 `books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=69f1e67e838cbd2de7f2c79390c35ce4cd36f897e8dcd54d64e8f9c627ab67fd。<!-- existing:SF-2026-ARXIV-2604-26557:end -->
<!-- delta:SF-2026-ARXIV-2604-26557:start -->memory manager 拥有 placement、migration 与 eviction state，kernel 只消费已提交映射<!-- delta:SF-2026-ARXIV-2604-26557:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26557:end -->

<!-- books-review:SF-2026-ARXIV-2604-26561:start -->
<!-- existing:SF-2026-ARXIV-2604-26561:start -->真实 owner `books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline` 正文：## 先建立单 Agent Baseline 一个模型可以在不同步骤切换 role。把同一模型复制成 planner、coder、reviewer，若它们共享训练分布、Context 和 evidence，错误高度相关。 Multi-Agent 引入额外成本： ```text total_cost = model calls + inter-agent messages + context duplication + coordination + merge / conflict resolution + longer critical path ``` 因此应先比较单 Agent、单 Agent + deterministic verifier、单 Agent + parallel tools，再判断多 Agent 是否有增量价值。；相邻章 `books/part-07-agent/81-workflow.md#L16-一个循环为什么不够; books/part-07-agent/83-mcp.md#L19-为什么需要协议层` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=b9f43cc2c7f213ddda4d1435facb93b969f80321d1174963fa5813d967854b6e。<!-- existing:SF-2026-ARXIV-2604-26561:end -->
<!-- delta:SF-2026-ARXIV-2604-26561:start -->orchestrator 拥有成员、消息与 commit control，各 agent 只拥有局部 proposal<!-- delta:SF-2026-ARXIV-2604-26561:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26561:end -->

<!-- books-review:SF-2026-ARXIV-2604-26622:start -->
<!-- existing:SF-2026-ARXIV-2604-26622:start -->真实 owner `books/part-07-agent/77-memory.md#L1208-belief-state先保存竞争假设再决定事实` 正文：## Belief State：先保存竞争假设，再决定事实 把每次新 observation 直接合并成单一“当前事实”，在环境稳定、证据一致时最省 token 和治理成本；部分可观测环境却会让一次错误写入自我强化，后续 retrieval 只看见已经合并的结论。更稳健的 memory state 先保留互斥 hypotheses、各自 evidence weight、更新时间与可证伪条件，再让新 observation 调整、合并或淘汰假设。write、retrieval 与 action planning 消费的是同一份 belief state，而不是彼此不可见的自由文本结论。 这种表示减少过早 commit，却增加状态增长、冲突合并、校准漂移与 action policy 复杂度；它也不把 posterior 变成事实。证据少、风险高时回退 raw episodes 与人工确认，低风险且世界近似确定时单一结论 memory 仍更经济。[受限证据：arXiv:2605.05583v1]；相邻章 `books/part-07-agent/76-rag.md#L16-参数化知识的边界; books/part-07-agent/78-tool-calling.md#L16-从生成文本到环境转移` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=a241ab934a3c3b722b6cbce0351db40d0c918fb10b89a72e0c4463ffeaf7599e。<!-- existing:SF-2026-ARXIV-2604-26622:end -->
<!-- delta:SF-2026-ARXIV-2604-26622:start -->memory service 拥有可持久 state 与 provenance，retriever 只生成读取视图<!-- delta:SF-2026-ARXIV-2604-26622:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26622:end -->

<!-- books-review:SF-2026-ARXIV-2604-26649:start -->
<!-- existing:SF-2026-ARXIV-2604-26649:start -->真实 owner `books/part-07-agent/76-rag.md#L410-rag-不消除-hallucination` 正文：## RAG 不消除 Hallucination 回答与检索文档内容一致，不等于回答由该文档支撑：模型可能只是在 parametric memory 中本就知道答案，检索内容甚至没有进入有效推理路径。若 evaluation 只看最终正确率或 citation overlap，就无法区分“证据导致了答案”与“答案碰巧和证据一致”。更严格的 groundedness contract 需要成对干预：保留问题、替换或遮蔽关键证据，观察结论与引用是否按预期改变，并把这种 counterfactual sensitivity 与普通 correctness 分开报告。 干预评估提高了因果诊断力，却增加样本构造、对照污染和 evaluator 成本；答案对证据不敏感也可能因为模型拥有正确先验，而非一定错误。低风险搜索可继续用 relevance/citation 指标快速迭代，高风险发布则需要 provenance、support span 与干预证据共同证明检索链真正拥有结论的 support authority。 ### Web Retrieval 的 Corpus 也可能主动塑造 Agent Trajectory 传统 RAG 把 corpus 当作被动事实集合；web-enabled Agent 会连续搜索、引用、回访并让多个页面共同塑造后续 query， 于是发布者优化的不再是单页排名，而是整条 evidence trajectory。检索系统必须记录页面 provenance、跨站关联、 query evolution 与最终 claim uptake，不能把“多处出现”自动解释为独立证据。协调内容生态可以提高可发现性，也会 制造相关来源、反馈回路与操纵面；高风险结论应回到独立 primary source 和 claim-level entailment。固定私有 corpus 仍适合低变化、强治理场景。受控虚构产品实验只证明 trajectory-level influence 可以被测量，不证明现实 web 排名 或所有搜索 Agent 会同样受影响。 ### ；相邻章 `books/part-07-agent/75-context.md#L16-context-是一次调用的可见状态; books/part-07-agent/77-memory.md#L20-context-与-memory-的状态边界` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=67561d15a90f3b4c8456e4d13cef9986646cc20bce9bbbb15bdcb01399f0e4f3。<!-- existing:SF-2026-ARXIV-2604-26649:end -->
<!-- delta:SF-2026-ARXIV-2604-26649:start -->retrieval service 拥有 index/query evidence，generator 不获得来源真值所有权<!-- delta:SF-2026-ARXIV-2604-26649:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26649:end -->

<!-- books-review:SF-2026-ARXIV-2604-26666:start -->
<!-- existing:SF-2026-ARXIV-2604-26666:start -->真实 owner `books/part-07-agent/81-workflow.md#L102-deterministic-spineagentic-nodes` 正文：## Deterministic Spine，Agentic Nodes 适合 deterministic 的部分： - identity、authorization、budgets； - required gates； - retry/backoff/timeouts； - state transitions； - side-effect records； - cancellation/compensation； - terminal success criteria。 适合 model-driven 的部分： - interpreting ambiguous intent； - drafting content； - proposing plans/tool arguments； - ranking alternatives； - diagnosing unstructured failure。 这种组合既保留模型灵活性，又让业务不变量可测试。 ### 从一次性脚本到平台拥有的可编辑 DAG 自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。 这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。 ### Template、Realized Graph 与 Trace 不是同一个对象 固定 code-defined template 便于审查、复现和强 verifier，仍是稳定 wor；相邻章 `books/part-07-agent/80-reflection.md#L16-基本循环; books/part-07-agent/82-multi-agent.md#L16-先建立单-agent-baseline` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=876ac2cc1f59f9376dcee3315ca5f38e95345018a37b1f888b9787534e149a1d。<!-- existing:SF-2026-ARXIV-2604-26666:end -->
<!-- delta:SF-2026-ARXIV-2604-26666:start -->workflow runtime 拥有 event、checkpoint 与 transition control，model 只提出下一步<!-- delta:SF-2026-ARXIV-2604-26666:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26666:end -->

<!-- books-review:SF-2026-ARXIV-2604-26687:start -->
<!-- existing:SF-2026-ARXIV-2604-26687:start -->真实 owner `books/part-04-training-system/36-distributed-training.md#L641-failure-不再是单进程退出` 正文：## Failure 不再是单进程退出 一个 rank crash 可能让其他 ranks 阻塞在 collective。训练平台需要： - Detect failed/stuck ranks。 - 终止或重建整个 process group。 - 选择 committed checkpoint。 - 恢复相同或新 world size。 - 保持 data cursor 与 job identity。 Elastic membership 对纯 DP 相对容易；TP/PP/EP layout 改变通常需要 reshard 或重建模型。第 35 章的 checkpoint correctness 是分布式容错的前提。 通信错误也不一定只能采用“任意 packet loss 都重传”的单一合同。可靠传输在 loss 罕见、梯度语义要求精确时最清楚；同步训练的 microburst 若触发成批重传，tail latency 会被最慢 flow 放大。一条实验性分支让 transport 按训练 phase 和已验证 tolerance 接受**有界 loss**：model/training owner 先证明该 phase、tensor class 与 loss budget 下的收敛影响，transport 再用 round identity、packet bitmap 和上限强制执行，超过预算立即回退可靠路径或重试整轮。 ```text phase + tensor/round identity + admitted loss budget → burst-aware transport → packet bitmap and bounded completion → optimizer step or reliable retransmit fallback ``` 这里“模型能容忍”不能由网络层自行推断，单个 workload 的经验阈值也不能写成通用 40%。该机制以更复杂的收敛证据、bitmap state 和 silent-corruption 风险换较短 ；相邻章 `books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够; books/part-04-training-system/37-tensor-parallel.md#L18-为什么把权重文件切开不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=35cb2eb9f2e0eff9dac03ee4db2cf2530c5f89ba9a7b8c92671958adf7b8df8e。<!-- existing:SF-2026-ARXIV-2604-26687:end -->
<!-- delta:SF-2026-ARXIV-2604-26687:start -->distributed runtime 拥有 shard/collective/epoch state，worker kernel 只处理已授权 buffer<!-- delta:SF-2026-ARXIV-2604-26687:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26687:end -->

<!-- books-review:SF-2026-ARXIV-2604-26694:start -->
<!-- existing:SF-2026-ARXIV-2604-26694:start -->真实 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L177-state-ownership-与-freshness` 正文：## State ownership 与 freshness - sensor pipeline 拥有 timestamped observations； - state estimator 拥有当前 calibrated belief； - VLA/world-action model 拥有 provisional proposal； - controller 拥有 action execution lease； - safety monitor 拥有 veto / emergency stop； - environment 拥有真实 outcome； - run log 拥有 observation-action-effect evidence。 ### Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory 单帧或短 action chunk 足以处理局部连续动作，却无法长期保留遮挡物体、阶段进度和失败上下文。一个受限分支在 policy 内维护快慢两级 latent：短期 state 跟随近期 observation，curator 只把通过 admission 的片段提升到长期 state，并在读取后压缩或替换。 ```text timestamped observation + short latent → policy update and action proposal → curator admission / retrieval / condensation → episode-scoped long latent → controller validation and fresh observation reconciliation ``` 这类 memory 仍是 model-owned、episode-scoped derived state：identity 必须绑定 policy revision、embodiment、episode、 reset boundary、observat；相邻章 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L16-从三个容易混淆的对象开始; books/part-04-training-system/27-data.md#L18-part-iv-的能力生产链` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=eb033b201edf92216070f88c082e72493073a9633bbe23a6a821e0e2fba02942。<!-- existing:SF-2026-ARXIV-2604-26694:end -->
<!-- delta:SF-2026-ARXIV-2604-26694:start -->policy 拥有 action proposal，environment/human safety layer 拥有 observation truth 与 actuation commit<!-- delta:SF-2026-ARXIV-2604-26694:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26694:end -->

<!-- books-review:SF-2026-ARXIV-2604-26733:start -->
<!-- existing:SF-2026-ARXIV-2604-26733:start -->真实 owner `books/part-04-training-system/33-grpo.md#L167-sequence-reward-怎样作用到-tokens` 正文：## Sequence Reward 怎样作用到 Tokens 若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens： ```text A_(i,1) = ... = A_(i,\|y_i\|) = A_i ``` 这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。 Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。；相邻章 `books/part-04-training-system/32-ppo.md#L18-把语言生成写成策略过程; books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=37ab39bc16e7905281265dede7f404b65fb4814e9ee1e4d81a5342f6c012e97a。<!-- existing:SF-2026-ARXIV-2604-26733:end -->
<!-- delta:SF-2026-ARXIV-2604-26733:start -->rollout/reward owner 提交可复算 evidence，trainer 拥有 group advantage 与参数 commit<!-- delta:SF-2026-ARXIV-2604-26733:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26733:end -->

<!-- books-review:SF-2026-ARXIV-2604-26752:start -->
<!-- existing:SF-2026-ARXIV-2604-26752:start -->真实 owner `books/part-04-training-system/34-dpo.md#L18-从-rlhf-的两阶段复杂度开始` 正文：## 从 RLHF 的两阶段复杂度开始 经典 pipeline： ```text preference pairs -> train Reward Model -> current policy rollouts -> score rollouts -> PPO/GRPO policy updates ``` 它允许 policy 探索新 outputs，也需要多个模型、generation、reward evaluation 和版本同步。 若已有高质量离线 pairs，一个朴素替代是对 chosen 做 SFT： ```text maximize log pi_theta(y_w \| x) ``` 但这丢弃了 rejected response 提供的信息。模型不知道 chosen 相对 rejected 好在哪里，也没有直接约束二者之间的 margin。 DPO 的目标是同时使用 pair 两侧，又避免显式训练 reward 和在线 RL loop。；相邻章 `books/part-04-training-system/33-grpo.md#L31-为什么移除-critic-会有吸引力; books/part-04-training-system/35-checkpoint.md#L18-为什么只保存-weights-不够` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=3ace537440f6dc97060caa2205884dc2c4172735ebbce82da7e7da7755b6ff51。<!-- existing:SF-2026-ARXIV-2604-26752:end -->
<!-- delta:SF-2026-ARXIV-2604-26752:start -->preference data owner 拥有 pair/label provenance，trainer 拥有 objective，judge 不拥有最终 policy commit<!-- delta:SF-2026-ARXIV-2604-26752:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26752:end -->

<!-- books-review:SF-2026-ARXIV-2604-26779:start -->
<!-- existing:SF-2026-ARXIV-2604-26779:start -->真实 owner `books/part-05-inference-system/48-speculative-decoding.md#L18-从-decode-串行瓶颈开始` 正文：## 从 Decode 串行瓶颈开始 普通 Decode 的流程是： ```text 大模型生成 token 1 → 把 token 1 接回上下文 → 大模型生成 token 2 → 把 token 2 接回上下文 → 大模型生成 token 3 ... ``` 生成 `K` 个 token，就要运行 `K` 次大模型 forward。这个串行依赖无法简单通过扩大 batch 消除，因为同一个请求内部下一个 token 依赖上一个 token。 这就是 speculative decoding 试图突破的地方：既然大模型一步一步生成很慢，能不能先让一个便宜的 draft model 猜出多个未来 token，再让大模型一次性验证这些猜测？；相邻章 `books/part-05-inference-system/47-pagedattention.md#L16-kv-cache-为什么会碎片化; books/part-05-inference-system/49-tensorrt-llm.md#L18-从计算图开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=2f7a8d5930de3ee03ecafc0aac2899817f6c6856721f4c2170d134cc9744c096。<!-- existing:SF-2026-ARXIV-2604-26779:end -->
<!-- delta:SF-2026-ARXIV-2604-26779:start -->draft 只拥有 proposal，target verifier 拥有 acceptance 与 token commit<!-- delta:SF-2026-ARXIV-2604-26779:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26779:end -->

<!-- existing:SF-2026-ARXIV-2604-26815:start -->current owner `books/part-06-ai-infrastructure/67-monitoring.md#L253-monitoring-也会改变系统` 已顺读：## Monitoring 也会改变系统  ### 输出 Watermark 与 Hidden State 都只是受限 Sensor  <!-- semantic-body-binding:SF-WATERMARKING-SHOULD-BE-TREATED-AS-A-MONITORING-PRIMITIVE:start --> Watermark 不只回答单条输出是否命中；观察者可以跨输出、key 和时间聚合信号，形成 entity-level attribution。因此 watermark identity、key scope、observer capability、aggregation window 与 false-positive budget 必须进入 monitoring contract，并接受隐私与滥用审查。它提供来源线索，不证明内容真实性或唯一作者；高隐私场景可能选择更短窗口、轮换 key 或不部署。多 key 实验只支持该观察面存在，不给出任意部署的识别率。 <!-- semantic-body-binding:SF-WATERMARKING-SHOULD-BE-TREATED-AS-A-MONITORING-PRIMITIVE:end -->  <!-- semantic-body-binding:SF-AERIC-ANTICIPATORY-HIDDEN-STATE-MONITORING-FOR-IMPLICIT-HARMFUL-DIALOGUE:start --> 只在文本生成后分类会错过逐步形成的隐式危害；same-pass monitor 可以读取普通 decode 已产生的 hidden state，利用 时间聚合提前产生 hazard signal，而不再调用 base model。它降低额外 forward cost，却依赖 white-box access、layer/ model revision 和阈值校准，也可能在 domain shift 下误报。EMA 或 probe 只触发 defer、review 或 stop proposal，最终 authority 仍属于独立 policy；无法取得内部状态时回退 output/trajectory monitor。；相邻 refs=books/part-06-ai-infrastructure/66-evaluation-system.md#L10-本章要回答的问题; books/part-06-ai-infrastructure/68-logging.md#L16-文本行不是日志契约。<!-- existing:SF-2026-ARXIV-2604-26815:end -->
<!-- delta:SF-2026-ARXIV-2604-26815:start -->把 energy monitor 自身的采样与 instrumentation overhead 纳入测量 contract。<!-- delta:SF-2026-ARXIV-2604-26815:end -->
<!-- books-review:SF-2026-ARXIV-2604-26815:start -->Decision=`No Change — Existing Coverage`；作者测试范围不证明任意 accelerator、采样频率或生产 workload 下开销可忽略。<!-- books-review:SF-2026-ARXIV-2604-26815:end -->

<!-- books-review:SF-2026-ARXIV-2604-26837:start -->
<!-- existing:SF-2026-ARXIV-2604-26837:start -->真实 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L24-如果完全不缓存` 正文：## 如果完全不缓存 Prompt 长度为 `T_p`，已经生成 `i` 个 tokens 时，朴素 Decode 可以把全部 `T_p+i` 个 tokens 再送入模型，只取最后位置 logits。 ```text step 1: recompute T_p tokens step 2: recompute T_p + 1 tokens step 3: recompute T_p + 2 tokens ... ``` 历史 positions 的 projections、Attention、MLP 和 layer outputs 被反复重算，但 causal mask 保证未来 tokens 不会改变历史位置已经得到的 K/V。这正是可缓存的不变量。；相邻章 `books/part-05-inference-system/44-decode.md#L18-为什么不能并行写出未来-token; books/part-05-inference-system/46-continuous-batching.md#L16-从-static-batching-的问题开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ffe365d267a891cdec085543157fd861f0bb8a34f60e2c7b19638a395c4345a7。<!-- existing:SF-2026-ARXIV-2604-26837:end -->
<!-- delta:SF-2026-ARXIV-2604-26837:start -->cache manager 拥有 block identity、placement 与 eviction，scheduler 只引用合法 handle<!-- delta:SF-2026-ARXIV-2604-26837:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26837:end -->

<!-- books-review:SF-2026-ARXIV-2604-26848:start -->
<!-- existing:SF-2026-ARXIV-2604-26848:start -->真实 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation从画面质量到干预结果` 正文：## Evaluation：从画面质量到干预结果 ### 视频只有编译成可执行 Transition，才能测试 Belief Planning Egocentric video 提供观察序列，却没有天然的 action precondition、object state 或 counterfactual transition。把片段编译成带 provenance 的 symbolic graph 和 transition rules，可让 planner 在可执行 world 中测试 belief update；compiler 拥有 observation-to-state proposal，environment verifier 拥有规则执行和 contradiction。它把视觉数据变成可重复测试，代价是符号化遗漏、规则错误和 domain-specific ontology；开放物理控制仍需真实闭环，不能把 cooking benchmark 的可执行性外推成通用 world-model fidelity。 一个 evidence ladder： ```text perceptual plausibility → temporal consistency → state reconstruction → action-conditioned prediction → counterfactual discrimination → long-horizon calibration → closed-loop task outcome → safety under perturbation ``` 低层证据不能替代高层。FVD 或人类偏好可评价视频观感，不证明 action consequence；one-step error 低不证明 long rollout；simulator 内 success 不证明 sim-to-real。 evaluation contract 应绑定 environment version、initial-state distrib；相邻章 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=fcdffa1f4e6dc30353d01f36aa02d75be6cd86ac092db86bb50f5a6ec9aa0e8d。<!-- existing:SF-2026-ARXIV-2604-26848:end -->
<!-- delta:SF-2026-ARXIV-2604-26848:start -->world state owner 提交 observation/action-conditioned transition，policy 只消费可验证 rollout<!-- delta:SF-2026-ARXIV-2604-26848:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26848:end -->

<!-- books-review:SF-2026-ARXIV-2604-26881:start -->
<!-- existing:SF-2026-ARXIV-2604-26881:start -->真实 owner `books/part-06-ai-infrastructure/71-multi-tenant.md#L16-先定义-tenant-与信任级别` 正文：## 先定义 Tenant 与信任级别 Kubernetes 本身没有一等 `Tenant` 对象。平台需要定义： ```text tenant identity owner and principals projects/namespaces data and model scope resource entitlement network and runtime isolation budget and retention audit boundary ``` 内部团队共享与不互信外部客户不是同一风险。所谓 soft/hard tenancy 是连续谱；若威胁模型要求强隔离，独立 cluster、virtual control plane、VM 或 dedicated hardware 可能比复杂共享策略更合适。；相邻章 `books/part-06-ai-infrastructure/70-cost.md#L16-资源时间是共同底座; books/part-06-ai-infrastructure/72-security.md#L16-从资产与信任边界开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=884a0d219ed2c34d4f5e0b7b863ea0988e633b19f5616a61afc07ecc380b6774。<!-- existing:SF-2026-ARXIV-2604-26881:end -->
<!-- delta:SF-2026-ARXIV-2604-26881:start -->tenant control plane 拥有 identity、quota、isolation 与 admission，scheduler 只执行授权<!-- delta:SF-2026-ARXIV-2604-26881:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26881:end -->

<!-- books-review:SF-2026-ARXIV-2604-26889:start -->
<!-- existing:SF-2026-ARXIV-2604-26889:start -->真实 owner `books/part-05-inference-system/54-gpu-memory.md#L16-从-memory-hierarchy-开始` 正文：## 从 memory hierarchy 开始 GPU 上并不是只有一种 memory。大致可以把它理解为： ```text register / SRAM / shared memory / L2 cache → HBM → CPU memory → storage ``` 越靠近计算单元，速度越快、容量越小、管理越精细；越远离计算单元，容量越大、访问越慢。 这解释了为什么很多优化并不是减少数学运算，而是减少 HBM 读写，或者把数据尽可能留在片上 memory 中。FlashAttention 的核心价值就在这里。；相邻章 `books/part-05-inference-system/53-kserve-llm.md#L18-deployment-加-service-为什么不够; books/part-05-inference-system/55-pd-disaggregation.md#L16-两种阶段两种节奏` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=69f1e67e838cbd2de7f2c79390c35ce4cd36f897e8dcd54d64e8f9c627ab67fd。<!-- existing:SF-2026-ARXIV-2604-26889:end -->
<!-- delta:SF-2026-ARXIV-2604-26889:start -->For NVIDIA GPUs, CUDA is the primary interface through which applications orchestrate GPU execution, yet much of the logic that realizes CUDA operations resides in NVIDIA's closed-source userspace driver. As a result, the translation from high-level CUDA APIs to low-level hardware commands remains opaque, limiting both software understanding and performance attribution. This paper makes that command path visible. 该机制将长期 owner 定位到 `INFER-GPU-MEMORY`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26889:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.26889v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26889:end -->

<!-- books-review:SF-2026-ARXIV-2604-26904:start -->
<!-- existing:SF-2026-ARXIV-2604-26904:start -->真实 owner `books/part-06-ai-infrastructure/66-evaluation-system.md#L78-从目标到证据而不是从指标到目标` 正文：## 从目标到证据，而不是从指标到目标 Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成： ```text intended use and risk → evaluation specification → dataset / environment → system execution → scorer / human judgment → aggregation and uncertainty → decision policy → release / rollback / investigation → production feedback ``` `intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明： ```text EvalSpec = target behavior + eligible population + failure taxonomy + metrics and scorers + slice definitions + thresholds / comparison rules + uncertainty requirement + owner and review policy ``` 如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。；相邻章 `books/part-06-ai-infrastructure/65-kai-scheduler.md#L18-为什么-ai-cluster-需要更强的-queue-模型; books/part-06-ai-infrastructure/67-monitoring.md#L18-先定义目标再选择可测信号` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=ba07952c1fe646f17bfd554f905fb4a594aaa8676cc3e8aea0edfa2526800e09。<!-- existing:SF-2026-ARXIV-2604-26904:end -->
<!-- delta:SF-2026-ARXIV-2604-26904:start -->EvalSpec owner 冻结 subject/data/scorer，release owner 依据 run evidence 作决定<!-- delta:SF-2026-ARXIV-2604-26904:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26904:end -->

<!-- books-review:SF-2026-ARXIV-2604-26934:start -->
<!-- existing:SF-2026-ARXIV-2604-26934:start -->真实 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L446-evaluation从画面质量到干预结果` 正文：## Evaluation：从画面质量到干预结果 ### 视频只有编译成可执行 Transition，才能测试 Belief Planning Egocentric video 提供观察序列，却没有天然的 action precondition、object state 或 counterfactual transition。把片段编译成带 provenance 的 symbolic graph 和 transition rules，可让 planner 在可执行 world 中测试 belief update；compiler 拥有 observation-to-state proposal，environment verifier 拥有规则执行和 contradiction。它把视觉数据变成可重复测试，代价是符号化遗漏、规则错误和 domain-specific ontology；开放物理控制仍需真实闭环，不能把 cooking benchmark 的可执行性外推成通用 world-model fidelity。 一个 evidence ladder： ```text perceptual plausibility → temporal consistency → state reconstruction → action-conditioned prediction → counterfactual discrimination → long-horizon calibration → closed-loop task outcome → safety under perturbation ``` 低层证据不能替代高层。FVD 或人类偏好可评价视频观感，不证明 action consequence；one-step error 低不证明 long rollout；simulator 内 success 不证明 sim-to-real。 evaluation contract 应绑定 environment version、initial-state distrib；相邻章 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L16-从一个共同问题开始; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L16-约束为何从-vlm-到-vla-发生变化` 已顺读。该主线尚未完整承载本 family 特有机制、failure 与 evidence boundary。 owner_sha256=fcdffa1f4e6dc30353d01f36aa02d75be6cd86ac092db86bb50f5a6ec9aa0e8d。<!-- existing:SF-2026-ARXIV-2604-26934:end -->
<!-- delta:SF-2026-ARXIV-2604-26934:start -->Vision-language models (VLMs) have shown strong performance on static visual understanding, yet they still struggle with dynamic spatial reasoning that requires imagining how scenes evolve under egocentric motion. Recent efforts address this limitation either by scaling spatial supervision with synthetic data or by coupling VLMs with world models at inference time. However, the former often lacks explicit modeling of motion-conditioned state transitions, while the latter incurs substantial computational overhead. 该机制将长期 owner 定位到 `MULTIMODAL-WORLD-MODELS`，并把相应 state/control/evidence identity 从隐式约定变成可检查对象。<!-- delta:SF-2026-ARXIV-2604-26934:end --> Decision=`Integrate`；evidence boundary：只接受 arXiv:2604.26934v1 的作者机制与实验；未披露硬件、precision、长度、batch、并发、成本或线上 SLO 均为 Not Disclosed。
<!-- books-review:SF-2026-ARXIV-2604-26934:end -->

<!-- books-review:SF-2026-ARXIV-2604-26951:start -->
<!-- existing:SF-2026-ARXIV-2604-26951:start -->真实 owner `books/part-04-training-system/29-sft.md#L415-full-fine-tuning-与-parameter-efficient-adaptation` 正文：## Full fine-tuning 与 parameter-efficient adaptation Full SFT 更新全部参数： ```text theta <- theta + Delta theta ``` 它提供最大的更新自由度，也需要保存全部 gradients、optimizer states 和新模型权重。 第 30 章 LoRA 将更新限制为低秩 adapters： ```text theta_base frozen Delta theta represented by small trainable factors ``` 两者可以使用相同 SFT data 与 token loss。LoRA 是参数化和训练状态选择，不是另一种 supervision objective。；相邻章 `books/part-04-training-system/28-pretraining.md#L18-从随机参数开始会发生什么; books/part-04-training-system/30-lora.md#L18-从-full-fine-tuning-的重复状态开始` 已顺读。该主线已承载同一长期 owner、fallback/coexistence 与证据边界；本 family 只增加受限实例证据。 owner_sha256=f84bce844228a80d97cb8e1f060d138ecb19907d47fab5386431b6f60b3c5f79。<!-- existing:SF-2026-ARXIV-2604-26951:end -->
<!-- delta:SF-2026-ARXIV-2604-26951:start -->dataset owner 拥有 trajectory/evidence，trainer 拥有 loss 与 checkpoint commit<!-- delta:SF-2026-ARXIV-2604-26951:end --> Decision=`No Change — Existing Coverage`；evidence boundary：仅接受 exact-v1 与 event-bound artifact 披露的机制和作者实验；不外推未披露模型、硬件、精度、长度、并发、SLO 或生产结论。
<!-- books-review:SF-2026-ARXIV-2604-26951:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260430-COVERAGE | fresh-context:owner-replay-20260903 | coverage | coverage:SRC-ARXIV:20260430 | none | raw/retained/closure/withdrawn conservation and initial-created owner mapping independently recounted | passed |
| SA-20260430-EVIDENCE | fresh-context:owner-replay-20260903 | evidence | validator:review-completion-v1 | none | every frozen family has a completed exact-version receipt; blocked=0 | passed |
| SA-20260430-SELECTION | fresh-context:owner-replay-20260903 | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | eligible=46；selected=3；all others retain completed reviews | passed |
| SA-20260430-BOOKS | fresh-context:apr-may-books-20260903 | books | validator:books-comparison-v1 | none | — | passed |

## 8. Ignored Noise

- Pre-denominator closures=351；逐 family 理由保存在 owner receipt。
- Withdrawn=0；只保留审计 closure，不进入候选、评分、Review 或 Books。
- `updated` / current OAI datestamp 的 revision 噪声不拥有 Daily。

## 9. Recommended Action

本日全部 Gate 已闭合，无进一步动作。

## 10. Repository Changes

- Owner receipt（本阶段只读）：`papers/2026/04/_sources/arxiv-owner-replay-20260903/20260430/arxiv-owner-receipt.json`
- Canonical ledger（Books terminal state）：`papers/2026/04/_sources/arxiv-owner-replay-20260903/20260430/canonical-ledger.json`
- Books queue（fresh-context decision）：`papers/2026/04/_sources/arxiv-owner-replay-20260903/BOOKS_WRITEBACK_QUEUE.json`
- Superseded report：`papers/2026/04/_sources/arxiv-owner-replay-20260903/legacy-reports-before-created-owner-reconciliation/2026-04-30.md`
- Books body: no change for the recovered families on this date.

## 11. Open Questions

- 无。

## 12. Sources

- [DataCite REST API](https://api.datacite.org/dois) — initial `created` owner-day proxy；`updated` 只作 revision provenance。
- [arXiv OAI](https://export.arxiv.org/oai2) — identity/date corroboration；current datestamp 不拥有 first-public day。
- [arXiv](https://arxiv.org/) — exact-v1 abstract、HTML/PDF 与 version history。

## 13. Final Status

Completion Status: Complete; Coverage: Closed; Evidence: Passed; Books: Passed; unresolved findings=0
