# Daily Research — 2026-06-30

**Research Date:** 2026-06-30

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-29 09:00:00 ～ 2026-06-30 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary
Beijing window [2026-06-29 09:00, 2026-06-30 09:00) contains 592 registered identities. Full 592/592 title+abstract semantic review freezes 64 durable families and 528 family-specific pre-denominator closures (10.81%). Exact-v1 Evidence is complete for 64/64 official HTML sources. Full-frontier Selection chooses three analysis units. Strict owner/adjacent comparison and root prewrite review reduced the preliminary 16 Integrate proposals to 2 Integrate / 36 No Change / 26 Weekly Only across 2 unique owner files. The two owner writes and 64/64 post-write fresh audit passed with zero unresolved findings, so the date is Complete.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-30 |
| Window End | 2026-06-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Beijing Window | [2026-06-29 09:00, 2026-06-30 09:00) |
| Denominator ID | daily-v2.1:2026-06-30:2a228144dceb4876 |
| Denominator Frozen At | 2026-08-29T23:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-29T09:00:00+08:00 | 2026-06-30T09:00:00+08:00 | 2026-08-29T23:20:00+08:00 | registered arXiv inventory; full Core + topic routes | checked | 592 | SF-2026-ARXIV-2606-29685; SF-2026-ARXIV-2606-29699; SF-2026-ARXIV-2606-29700; SF-2026-ARXIV-2606-29708; SF-2026-ARXIV-2606-29713; SF-2026-ARXIV-2606-29718; SF-2026-ARXIV-2606-29719; SF-2026-ARXIV-2606-29745; SF-2026-ARXIV-2606-29758; SF-2026-ARXIV-2606-29775; SF-2026-ARXIV-2606-29778; SF-2026-ARXIV-2606-29784; SF-2026-ARXIV-2606-29788; SF-2026-ARXIV-2606-29871; SF-2026-ARXIV-2606-29887; SF-2026-ARXIV-2606-29914; SF-2026-ARXIV-2606-29920; SF-2026-ARXIV-2606-29955; SF-2026-ARXIV-2606-29957; SF-2026-ARXIV-2606-29959; SF-2026-ARXIV-2606-29975; SF-2026-ARXIV-2606-29982; SF-2026-ARXIV-2606-29986; SF-2026-ARXIV-2606-30005; SF-2026-ARXIV-2606-30107; SF-2026-ARXIV-2606-30119; SF-2026-ARXIV-2606-30185; SF-2026-ARXIV-2606-30251; SF-2026-ARXIV-2606-30263; SF-2026-ARXIV-2606-30265; SF-2026-ARXIV-2606-30338; SF-2026-ARXIV-2606-30373; SF-2026-ARXIV-2606-30383; SF-2026-ARXIV-2606-30389; SF-2026-ARXIV-2606-30391; SF-2026-ARXIV-2606-30449; SF-2026-ARXIV-2606-30531; SF-2026-ARXIV-2606-30534; SF-2026-ARXIV-2606-30546; SF-2026-ARXIV-2606-30560; SF-2026-ARXIV-2606-30562; SF-2026-ARXIV-2606-30566; SF-2026-ARXIV-2606-30573; SF-2026-ARXIV-2606-30602; SF-2026-ARXIV-2606-30616; SF-2026-ARXIV-2606-30627; SF-2026-ARXIV-2606-30634; SF-2026-ARXIV-2606-30639; SF-2026-ARXIV-2606-30697; SF-2026-ARXIV-2606-30704; SF-2026-ARXIV-2606-30774; SF-2026-ARXIV-2606-30775; SF-2026-ARXIV-2606-30783; SF-2026-ARXIV-2606-30788; SF-2026-ARXIV-2606-30789; SF-2026-ARXIV-2606-30801; SF-2026-ARXIV-2606-30814; SF-2026-ARXIV-2606-30850; SF-2026-ARXIV-2606-30852; SF-2026-ARXIV-2606-30899; SF-2026-ARXIV-2606-30911; SF-2026-ARXIV-2606-30919; SF-2026-ARXIV-2606-30931; SF-2026-ARXIV-2606-31002 | pages=50; final_cursor=end; 592 unique identities | 2026-06-30T01:00:00Z | ../_sources/daily-20260630/screening-ledger.json; ../_sources/daily-20260630/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260630 | — |

<!-- coverage:SRC-ARXIV:20260630:start -->
Full 592/592 title+abstract audit: 387 Core, 64 keyword-routed and 141 route-negative; arithmetic 592 = 64 retained + 528 closures; retain rate 10.81%. Keyword routing supplied recall only. Route-negative retained=1 (Orca 2606.30534).
<!-- coverage:SRC-ARXIV:20260630:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29685 | arXiv:2606.29685v1 | paper-v1:2606.29685 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29685 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29699 | arXiv:2606.29699v1 | paper-v1:2606.29699 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29699 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29699 | yes |
| SF-2026-ARXIV-2606-29700 | arXiv:2606.29700v1 | paper-v1:2606.29700 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29700 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29700 | yes |
| SF-2026-ARXIV-2606-29708 | arXiv:2606.29708v1 | paper-v1:2606.29708 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29708 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29708 | yes |
| SF-2026-ARXIV-2606-29713 | arXiv:2606.29713v1 | paper-v1:2606.29713 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29713 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29713 | yes |
| SF-2026-ARXIV-2606-29718 | arXiv:2606.29718v1 | paper-v1:2606.29718 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29718 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29718 | yes |
| SF-2026-ARXIV-2606-29719 | arXiv:2606.29719v1 | paper-v1:2606.29719 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29719 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29745 | arXiv:2606.29745v1 | paper-v1:2606.29745 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29745 | self | — | new_in_window | AGENT-PLANNING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29758 | arXiv:2606.29758v1 | paper-v1:2606.29758 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29758 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29758 | yes |
| SF-2026-ARXIV-2606-29775 | arXiv:2606.29775v1 | paper-v1:2606.29775 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29775 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29778 | arXiv:2606.29778v1 | paper-v1:2606.29778 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29778 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29778 | yes |
| SF-2026-ARXIV-2606-29784 | arXiv:2606.29784v1 | paper-v1:2606.29784 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29784 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29788 | arXiv:2606.29788v1 | paper-v1:2606.29788 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29788 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29788 | yes |
| SF-2026-ARXIV-2606-29871 | arXiv:2606.29871v1 | paper-v1:2606.29871 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29871 | self | — | new_in_window | PLATFORM-TRAINING-OPERATOR | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29887 | arXiv:2606.29887v1 | paper-v1:2606.29887 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29887 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29914 | arXiv:2606.29914v1 | paper-v1:2606.29914 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29914 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29914 | yes |
| SF-2026-ARXIV-2606-29920 | arXiv:2606.29920v1 | paper-v1:2606.29920 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29920 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29920 | yes |
| SF-2026-ARXIV-2606-29955 | arXiv:2606.29955v1 | paper-v1:2606.29955 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29955 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29957 | arXiv:2606.29957v1 | paper-v1:2606.29957 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29957 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29959 | arXiv:2606.29959v1 | paper-v1:2606.29959 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29959 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29959 | yes |
| SF-2026-ARXIV-2606-29975 | arXiv:2606.29975v1 | paper-v1:2606.29975 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29975 | self | — | new_in_window | TRAIN-DATA | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-29982 | arXiv:2606.29982v1 | paper-v1:2606.29982 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29982 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29982 | yes |
| SF-2026-ARXIV-2606-29986 | arXiv:2606.29986v1 | paper-v1:2606.29986 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-29986 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29986 | yes |
| SF-2026-ARXIV-2606-30005 | arXiv:2606.30005v1 | paper-v1:2606.30005 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30005 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30005 | yes |
| SF-2026-ARXIV-2606-30107 | arXiv:2606.30107v1 | paper-v1:2606.30107 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30107 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30107 | yes |
| SF-2026-ARXIV-2606-30119 | arXiv:2606.30119v1 | paper-v1:2606.30119 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30119 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30185 | arXiv:2606.30185v1 | paper-v1:2606.30185 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30185 | self | — | new_in_window | AGENT-TOOL-CALLING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30251 | arXiv:2606.30251v1 | paper-v1:2606.30251 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30251 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30251 | yes |
| SF-2026-ARXIV-2606-30263 | arXiv:2606.30263v1 | paper-v1:2606.30263 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30263 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30263 | yes |
| SF-2026-ARXIV-2606-30265 | arXiv:2606.30265v1 | paper-v1:2606.30265 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30265 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30265 | yes |
| SF-2026-ARXIV-2606-30338 | arXiv:2606.30338v1 | paper-v1:2606.30338 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30338 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30373 | arXiv:2606.30373v1 | paper-v1:2606.30373 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30373 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30383 | arXiv:2606.30383v1 | paper-v1:2606.30383 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30383 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30383 | yes |
| SF-2026-ARXIV-2606-30389 | arXiv:2606.30389v1 | paper-v1:2606.30389 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30389 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30389 | yes |
| SF-2026-ARXIV-2606-30391 | arXiv:2606.30391v1 | paper-v1:2606.30391 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30391 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30391 | yes |
| SF-2026-ARXIV-2606-30449 | arXiv:2606.30449v1 | paper-v1:2606.30449 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30449 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30449 | yes |
| SF-2026-ARXIV-2606-30531 | arXiv:2606.30531v1 | paper-v1:2606.30531 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30531 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30531 | yes |
| SF-2026-ARXIV-2606-30534 | arXiv:2606.30534v1 | paper-v1:2606.30534 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30534 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30534 | yes |
| SF-2026-ARXIV-2606-30546 | arXiv:2606.30546v1 | paper-v1:2606.30546 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30546 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30560 | arXiv:2606.30560v1 | paper-v1:2606.30560 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30560 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30560 | yes |
| SF-2026-ARXIV-2606-30562 | arXiv:2606.30562v1 | paper-v1:2606.30562 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30562 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30562 | yes |
| SF-2026-ARXIV-2606-30566 | arXiv:2606.30566v1 | paper-v1:2606.30566 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30566 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30566 | yes |
| SF-2026-ARXIV-2606-30573 | arXiv:2606.30573v1 | paper-v1:2606.30573 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30573 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30602 | arXiv:2606.30602v1 | paper-v1:2606.30602 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30602 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30616 | arXiv:2606.30616v1 | paper-v1:2606.30616 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30616 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-30616 | yes |
| SF-2026-ARXIV-2606-30627 | arXiv:2606.30627v1 | paper-v1:2606.30627 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30627 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30627 | yes |
| SF-2026-ARXIV-2606-30634 | arXiv:2606.30634v1 | paper-v1:2606.30634 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30634 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30634 | yes |
| SF-2026-ARXIV-2606-30639 | arXiv:2606.30639v1 | paper-v1:2606.30639 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30639 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30639 | yes |
| SF-2026-ARXIV-2606-30697 | arXiv:2606.30697v1 | paper-v1:2606.30697 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30697 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30704 | arXiv:2606.30704v1 | paper-v1:2606.30704 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30704 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30774 | arXiv:2606.30774v1 | paper-v1:2606.30774 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30774 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30775 | arXiv:2606.30775v1 | paper-v1:2606.30775 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30775 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30775 | yes |
| SF-2026-ARXIV-2606-30783 | arXiv:2606.30783v1 | paper-v1:2606.30783 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30783 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30783 | yes |
| SF-2026-ARXIV-2606-30788 | arXiv:2606.30788v1 | paper-v1:2606.30788 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30788 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-30788 | yes |
| SF-2026-ARXIV-2606-30789 | arXiv:2606.30789v1 | paper-v1:2606.30789 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30789 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30789 | yes |
| SF-2026-ARXIV-2606-30801 | arXiv:2606.30801v1 | paper-v1:2606.30801 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30801 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30814 | arXiv:2606.30814v1 | paper-v1:2606.30814 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30814 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30850 | arXiv:2606.30850v1 | paper-v1:2606.30850 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30850 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30852 | arXiv:2606.30852v1 | paper-v1:2606.30852 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30852 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30852 | yes |
| SF-2026-ARXIV-2606-30899 | arXiv:2606.30899v1 | paper-v1:2606.30899 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30899 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30911 | arXiv:2606.30911v1 | paper-v1:2606.30911 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30911 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-30919 | arXiv:2606.30919v1 | paper-v1:2606.30919 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30919 | self | — | new_in_window | PLATFORM-GATEWAY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30919 | yes |
| SF-2026-ARXIV-2606-30931 | arXiv:2606.30931v1 | paper-v1:2606.30931 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-30931 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30931 | yes |
| SF-2026-ARXIV-2606-31002 | arXiv:2606.31002v1 | paper-v1:2606.31002 | 2026-W27 | 2026-06-29 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-31002 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29685 | RP-f0d287bf094801f3 | deep | arXiv:2606.29685v1 | SRC-ARXIV@arXiv:2606.29685v1 | arXiv:2606.29685v1 — §3.1 Prompt Corpus Design; §Appendix D Methodological Details; §Appendix G Ethical Design and Release Safeguards | arXiv:2606.29685v1 — §CAREBench: A Child-Safety Risk Benchmark for Language Models; §3 Benchmark Scope and Task Definition; §4 Evaluation Protocol | arXiv:2606.29685v1 — §5.1 Overall model failure rates; §5.2 Category-level failure structure; §5.3 Failure mode analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29685 | complete |
| SF-2026-ARXIV-2606-29699 | RP-aa52fcd0d91d5f4a | deep | arXiv:2606.29699v1 | SRC-ARXIV@arXiv:2606.29699v1 | arXiv:2606.29699v1 — §3 Method | arXiv:2606.29699v1 — §2.3 Activation based analysis; §3.1 Problem setup; §4 Experimental Setup | arXiv:2606.29699v1 — §Early Warning Signals for OpenVLA Failure under Visual Distribution Shift; §2.2 Failure detection and robustness; §5.2 Activation monitors predict near term failure | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29699 | complete |
| SF-2026-ARXIV-2606-29700 | RP-ae60a63f6b27aa68 | deep | arXiv:2606.29700v1 | SRC-ARXIV@arXiv:2606.29700v1 | arXiv:2606.29700v1 — §III Method | arXiv:2606.29700v1 — §III-C Planner-in-the-Loop Feedback and Evaluation; §IV Experiments; §IV-A Experimental Setup | arXiv:2606.29700v1 — §V Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29700 | complete |
| SF-2026-ARXIV-2606-29708 | RP-8ace2b8ba94a7aa7 | deep | arXiv:2606.29708v1 | SRC-ARXIV@arXiv:2606.29708v1 | arXiv:2606.29708v1 — §Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving; §2.1 Design Axes Behind the Boundary | arXiv:2606.29708v1 — §1 Introduction; §2 The PD Boundary; §2.1 Design Axes Behind the Boundary | arXiv:2606.29708v1 — §2 The PD Boundary; §2.1 Design Axes Behind the Boundary; §2.2 Three Boundary Decisions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29708 | complete |
| SF-2026-ARXIV-2606-29713 | RP-88cebbe403af743f | deep | arXiv:2606.29713v1 | SRC-ARXIV@arXiv:2606.29713v1 | arXiv:2606.29713v1 — §2 Method; §2.1 Problem Formulation and Overview; §2.4 Training Pipeline | arXiv:2606.29713v1 — §3 Experiments; §3.1 Setup; §3.2 Main Results | arXiv:2606.29713v1 — §2.3 From Binary Reward Failure to Process Reward; §The failure of binary reward.; §4.3 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29713 | complete |
| SF-2026-ARXIV-2606-29718 | RP-cc4df3fd66efc99d | deep | arXiv:2606.29718v1 | SRC-ARXIV@arXiv:2606.29718v1 | arXiv:2606.29718v1 — §Appendix D Effect of the Threshold on Other Context Management Methods | arXiv:2606.29718v1 — §3.3 Experimental Setup and Results; §Setup; §Main Results | arXiv:2606.29718v1 — §5 Conclusion; §Appendix G Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29718 | complete |
| SF-2026-ARXIV-2606-29719 | RP-cd73ddff0f1e5960 | deep | arXiv:2606.29719v1 | SRC-ARXIV@arXiv:2606.29719v1 | arXiv:2606.29719v1 — §A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents; §3 The EPC Framework; §5.6 Methodological Ablations | arXiv:2606.29719v1 — §4 Experimental Setup; §5 Results: The Multi-Evaluator Audit | arXiv:2606.29719v1 — §6 Discussion; §6.5 Limitations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29719 | complete |
| SF-2026-ARXIV-2606-29745 | RP-8c46a1cdc81fb48c | deep | arXiv:2606.29745v1 | SRC-ARXIV@arXiv:2606.29745v1 | arXiv:2606.29745v1 — §Explicit reasoning does not substitute for epistemic training.; §Training dynamics support turn-level epistemic credit assignment.; §Appendix B ECHO Training Dynamics | arXiv:2606.29745v1 — §5 Experiments; §Evaluation Strategy; §6 Results | arXiv:2606.29745v1 — §7 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29745 | complete |
| SF-2026-ARXIV-2606-29758 | RP-bbb2bef93e90ead8 | deep | arXiv:2606.29758v1 | SRC-ARXIV@arXiv:2606.29758v1 | arXiv:2606.29758v1 — §2.1 Post-Training for LLM Alignment; §3 Method; §Appendix F Monotone Budget Design and PAV | arXiv:2606.29758v1 — §4 Experiments; §Experiment setup.; §4.2 Analysis on Hyperparameters | arXiv:2606.29758v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29758 | complete |
| SF-2026-ARXIV-2606-29775 | RP-b06ce932f49987ac | deep | arXiv:2606.29775v1 | SRC-ARXIV@arXiv:2606.29775v1 | arXiv:2606.29775v1 — §SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling; §IV Problem Formulation and Methodology | arXiv:2606.29775v1 — §VI Experimental Results; §VI-A Experimental Settings; §VI-B Results for Scheduling Algorithms without Repartitioning | arXiv:2606.29775v1 — §VII Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29775 | complete |
| SF-2026-ARXIV-2606-29778 | RP-23a5ae843929a233 | deep | arXiv:2606.29778v1 | SRC-ARXIV@arXiv:2606.29778v1 | arXiv:2606.29778v1 — §Mandol: An Agglomerative Agent Memory System for Long-Term Conversations; §2.2. Memory Retrieval Methods; §3. Mandol System Design | arXiv:2606.29778v1 — §5. Evaluation; §5.1. Experimental Setup; §5.2. Accuracy and Token Efficiency Results | arXiv:2606.29778v1 — §6. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29778 | complete |
| SF-2026-ARXIV-2606-29784 | RP-d256dfcdddc70b0b | deep | arXiv:2606.29784v1 | SRC-ARXIV@arXiv:2606.29784v1 | arXiv:2606.29784v1 — §3 Method: History Enhanced RObust (HERO) Model Evaluation | arXiv:2606.29784v1 — §HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data; §1.2 Model Evaluation Target Parameters and Tasks; §2 Bias and Variance in Model Evaluation | arXiv:2606.29784v1 — §1 Introduction; §1.1 Motivation and Contribution; §1.2 Model Evaluation Target Parameters and Tasks | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29784 | complete |
| SF-2026-ARXIV-2606-29788 | RP-c93a894de6a7c660 | deep | arXiv:2606.29788v1 | SRC-ARXIV@arXiv:2606.29788v1 | arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §4.1 Systems Evaluated; §5 Design Implications | arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §3 The MemLeak Benchmark; §4 Experiments | arXiv:2606.29788v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29788 | complete |
| SF-2026-ARXIV-2606-29871 | RP-94fc572377aeeaf7 | deep | arXiv:2606.29871v1 | SRC-ARXIV@arXiv:2606.29871v1 | arXiv:2606.29871v1 — §AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes; §II-A Inner-Loop Heuristics and Adaptive Training Methods; §II-B Hyperparameter Optimization, AutoML, and Population-Based Training | arXiv:2606.29871v1 — §IV Experiments and Results; §IV-A TinyStories Language-Model Experiments; §IV-B Robotic-Arm Reinforcement-Learning Experiments | arXiv:2606.29871v1 — §V Discussion and Limitations; §VI Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29871 | complete |
| SF-2026-ARXIV-2606-29887 | RP-fad8f267a1f21fed | deep | arXiv:2606.29887v1 | SRC-ARXIV@arXiv:2606.29887v1 | arXiv:2606.29887v1 — §3.2 Hierarchical Design; §3.2.3 Level 2: Adapting to Novel Policy Frameworks; §Appendix D System Prompt for Policy-configurable Guards | arXiv:2606.29887v1 — §SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing; §3.4 Benchmark Construction; §3.6 Evaluation Protocols | arXiv:2606.29887v1 — §5 Limitations and Future Work; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29887 | complete |
| SF-2026-ARXIV-2606-29914 | RP-753e88a43a484912 | deep | arXiv:2606.29914v1 | SRC-ARXIV@arXiv:2606.29914v1 | arXiv:2606.29914v1 — §Memory systems and benchmarks.; §B.3 When Might Architecture Matter?; §Memory systems. | arXiv:2606.29914v1 — §MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation; §Memory systems and benchmarks.; §Confounds in memory evaluation. | arXiv:2606.29914v1 — §4.2 Model Behavior: Three Models, Three Conclusions; §Sonnet’s length-driven failure.; §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29914 | complete |
| SF-2026-ARXIV-2606-29920 | RP-8e6eca418bb730f7 | deep | arXiv:2606.29920v1 | SRC-ARXIV@arXiv:2606.29920v1 | arXiv:2606.29920v1 — §1 Introduction; §2 Related Work; §Rubric-based evaluation | arXiv:2606.29920v1 — §Rubric-based evaluation; §3.3 Benchmark Statistics; §4 Experiments | arXiv:2606.29920v1 — §5 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29920 | complete |
| SF-2026-ARXIV-2606-29955 | RP-256d40eae30ac3b5 | deep | arXiv:2606.29955v1 | SRC-ARXIV@arXiv:2606.29955v1 | arXiv:2606.29955v1 — §1 Introduction; §2 SpreadsheetBench 2; §2.1 Task Categories | arXiv:2606.29955v1 — §2.2 Benchmark Construction; §2.3 Benchmark Statistics; §2.4 Evaluation Metrics | arXiv:2606.29955v1 — §3.3 Analysis and Discussions; §5 Conclusion; §Appendix A Broader Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29955 | complete |
| SF-2026-ARXIV-2606-29957 | RP-d239809af7e2f5d2 | deep | arXiv:2606.29957v1 | SRC-ARXIV@arXiv:2606.29957v1 | arXiv:2606.29957v1 — §2.3 Evaluation Method | arXiv:2606.29957v1 — §2.3 Evaluation Method; §3 Experiments and Results; §3.1 Main Result | arXiv:2606.29957v1 — §5 Limitations and Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29957 | complete |
| SF-2026-ARXIV-2606-29959 | RP-a5a686ce3903e5bf | deep | arXiv:2606.29959v1 | SRC-ARXIV@arXiv:2606.29959v1 | arXiv:2606.29959v1 — §3 Problem Setup and Method; §When the method helps.; §Appendix A Extended Method Details | arXiv:2606.29959v1 — §3 Problem Setup and Method; §4 Experimental Setup; §Evaluation. | arXiv:2606.29959v1 — §7 Discussion; §8 Limitations; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29959 | complete |
| SF-2026-ARXIV-2606-29975 | RP-0dfa68c275f72951 | deep | arXiv:2606.29975v1 | SRC-ARXIV@arXiv:2606.29975v1 | arXiv:2606.29975v1 — §Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets; §2.2 Scientific Storage and Training Stores; §3 System Design | arXiv:2606.29975v1 — §4 Evaluation Methodology; §5 Benchmark Results | arXiv:2606.29975v1 — §6 Discussion and Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29975 | complete |
| SF-2026-ARXIV-2606-29982 | RP-928ac98409905b2a | deep | arXiv:2606.29982v1 | SRC-ARXIV@arXiv:2606.29982v1 | arXiv:2606.29982v1 — §II-B Multi-Device Systems; §IV System Design | arXiv:2606.29982v1 — §III Analysis and Challenges; §III-A 1 Quantitative Analysis; §III-B 1 Quantitative Analysis | arXiv:2606.29982v1 — §VII Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29982 | complete |
| SF-2026-ARXIV-2606-29986 | RP-0ef3ec5d31c8795a | deep | arXiv:2606.29986v1 | SRC-ARXIV@arXiv:2606.29986v1 | arXiv:2606.29986v1 — §3. Design | arXiv:2606.29986v1 — §4. Evaluation | arXiv:2606.29986v1 — §6. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-29986 | complete |
| SF-2026-ARXIV-2606-30005 | RP-77a2a7052aa5d288 | deep | arXiv:2606.30005v1 | SRC-ARXIV@arXiv:2606.30005v1 | arXiv:2606.30005v1 — §Methodology; §Appendix C Method Capability Comparison | arXiv:2606.30005v1 — §Problem Setup; §Experiments; §Experiment Setup | arXiv:2606.30005v1 — §Limitations; §Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30005 | complete |
| SF-2026-ARXIV-2606-30107 | RP-7c0c01b91d95f41d | deep | arXiv:2606.30107v1 | SRC-ARXIV@arXiv:2606.30107v1 | arXiv:2606.30107v1 — §Structural Certification for Reliable Physical Design with Language Models; §The framework; §PHACT certifies valid designs and refuses impossible ones | arXiv:2606.30107v1 — §Results | arXiv:2606.30107v1 — §Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30107 | complete |
| SF-2026-ARXIV-2606-30119 | RP-7c0d0f804aacc808 | deep | arXiv:2606.30119v1 | SRC-ARXIV@arXiv:2606.30119v1 | arXiv:2606.30119v1 — §3. Methodology; §3.1.3. Honeysite Design | arXiv:2606.30119v1 — §3.2. Experimental Protocol; §7.1. Multi-Layer Classification Setup; §7.2. Multi-Layer Classification Evaluation | arXiv:2606.30119v1 — §8. Limitations and Discussion; §10. Conclusion & Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30119 | complete |
| SF-2026-ARXIV-2606-30185 | RP-6a62f763409e255f | deep | arXiv:2606.30185v1 | SRC-ARXIV@arXiv:2606.30185v1 | arXiv:2606.30185v1 — §3 Method; §3.1 Problem Formulation; §A.2 RL Baseline Training Compute | arXiv:2606.30185v1 — §4 Experiments; §4.1 Experimental Setup; §Benchmarks. | arXiv:2606.30185v1 — §5 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30185 | complete |
| SF-2026-ARXIV-2606-30251 | RP-9866ff68f023d04e | deep | arXiv:2606.30251v1 | SRC-ARXIV@arXiv:2606.30251v1 | arXiv:2606.30251v1 — §3 Method; §3.4 Training; §4.6 Training Dynamics | arXiv:2606.30251v1 — §4 Experiments; §4.1 Experimental Setup; §Benchmarks and baselines. | arXiv:2606.30251v1 — §5 Conclusion; §Probe parse failure.; §Appendix F Limitations and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30251 | complete |
| SF-2026-ARXIV-2606-30263 | RP-41446ce12ebc3a09 | deep | arXiv:2606.30263v1 | SRC-ARXIV@arXiv:2606.30263v1 | arXiv:2606.30263v1 — §4 Methodology; §B.1 Details on Baseline Methods; §C.1 Ablation on Different Design of η \eta Function | arXiv:2606.30263v1 — §4.1 Optimization Dynamic Analysis; §5 Experiments; §Appendix A Theoretical Analysis | arXiv:2606.30263v1 — §6 Conclusion; §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30263 | complete |
| SF-2026-ARXIV-2606-30265 | RP-fc88c19535ff417f | deep | arXiv:2606.30265v1 | SRC-ARXIV@arXiv:2606.30265v1 | arXiv:2606.30265v1 — §1 Introduction; §2 Related Works; §Architectural variants. | arXiv:2606.30265v1 — §Theoretical analysis.; §4.1 Setup; §5.1 Setup and Notation | arXiv:2606.30265v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30265 | complete |
| SF-2026-ARXIV-2606-30338 | RP-879d40f4d853e3c7 | deep | arXiv:2606.30338v1 | SRC-ARXIV@arXiv:2606.30338v1 | arXiv:2606.30338v1 — §3. Methodology; §Base Architectures | arXiv:2606.30338v1 — §2.1. Statistical Fairness Evaluation; §4. Experimental Setup; §4.6. Population-Level Fairness Evaluation | arXiv:2606.30338v1 — §6. Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30338 | complete |
| SF-2026-ARXIV-2606-30373 | RP-89472a27c438148b | deep | arXiv:2606.30373v1 | SRC-ARXIV@arXiv:2606.30373v1 | arXiv:2606.30373v1 — §3.6. Model Training via AI-Apps; §5. Measurement Methodology | arXiv:2606.30373v1 — §5.2. Basic Threat Analysis; §5.3. Input Injection Vulnerability Analysis; §5.4. Data Leakage Analysis | arXiv:2606.30373v1 — §4. AI-App Threats; §4.1. Threat Model; §5.2. Basic Threat Analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30373 | complete |
| SF-2026-ARXIV-2606-30383 | RP-079a9ffc4248acb3 | deep | arXiv:2606.30383v1 | SRC-ARXIV@arXiv:2606.30383v1 | arXiv:2606.30383v1 — §Methods. | arXiv:2606.30383v1 — §Setup.; §Agent benchmarks are two-party.; §Privacy benchmarks isolate information flow, not adversarial pressure. | arXiv:2606.30383v1 — §Why one failure axis is not enough.; §Failures compound: a worked trace.; §9 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30383 | complete |
| SF-2026-ARXIV-2606-30389 | RP-d78989e0bcbac63f | deep | arXiv:2606.30389v1 | SRC-ARXIV@arXiv:2606.30389v1 | arXiv:2606.30389v1 — §3 The Design Space; §4 Design | arXiv:2606.30389v1 — §5 Evaluation; §5.1 Experiment Setups; §5.2 Accelerate Evaluation | arXiv:2606.30389v1 — §7 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30389 | complete |
| SF-2026-ARXIV-2606-30391 | RP-c77e7cb67dfdd892 | deep | arXiv:2606.30391v1 | SRC-ARXIV@arXiv:2606.30391v1 | arXiv:2606.30391v1 — §3. Festina Design; §3.1. System Overview; §Appendix I Prior Energy-Efficient LLM Serving Systems | arXiv:2606.30391v1 — §4. Evaluation; §4.1. Experimental Setup; §4.4. Micro-benchmarks | arXiv:2606.30391v1 — §6. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30391 | complete |
| SF-2026-ARXIV-2606-30449 | RP-142f1adc73f2687c | deep | arXiv:2606.30449v1 | SRC-ARXIV@arXiv:2606.30449v1 | arXiv:2606.30449v1 — §3 Methods; §Appendix A Methodology details; §A.1 Methodology divergences from the closest prior work | arXiv:2606.30449v1 — §In-context misalignment evaluations.; §4 Experiments; §5 Results | arXiv:2606.30449v1 — §6 Discussion; §7 Limitations; §8 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30449 | complete |
| SF-2026-ARXIV-2606-30531 | RP-ee605fce7e7794d0 | deep | arXiv:2606.30531v1 | SRC-ARXIV@arXiv:2606.30531v1 | arXiv:2606.30531v1 — §III Problem Formulation; §IV Method; §V-E Methods Compared | arXiv:2606.30531v1 — §V Experimental Setup; §V-G Evaluation Protocol; §VI Results | arXiv:2606.30531v1 — §Entity Binding Failures in Tool-Augmented Agents; §VI-C Failure Modes by Ambiguity Type; §VII Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30531 | complete |
| SF-2026-ARXIV-2606-30534 | RP-4bc5907765402b10 | deep | arXiv:2606.30534v1 | SRC-ARXIV@arXiv:2606.30534v1 | arXiv:2606.30534v1 — §2.2 Architecture; §3 Training; §3.1 Pre-Training | arXiv:2606.30534v1 — §4 Evaluation; §4.2 Downstream Readout Analysis; §Appendix E Evaluation Settings | arXiv:2606.30534v1 — §5 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30534 | complete |
| SF-2026-ARXIV-2606-30546 | RP-e09de1dc3cb581c6 | deep | arXiv:2606.30546v1 | SRC-ARXIV@arXiv:2606.30546v1 | arXiv:2606.30546v1 — §MAS-Lab: A Specification - Driven Validation Framework for Reliable Multi - Agent Systems; §2.3. Agent Operating Systems; §3. MAS-Lab Design Objectives | arXiv:2606.30546v1 — §2.4. MAS Experimentation and Evaluation; §7. Labs: Testing, Benchmarking, and Evaluation Environment; §8. Experimental Evaluation | arXiv:2606.30546v1 — §9. Discussion; §10. Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30546 | complete |
| SF-2026-ARXIV-2606-30560 | RP-264ff41555484eb4 | deep | arXiv:2606.30560v1 | SRC-ARXIV@arXiv:2606.30560v1 | arXiv:2606.30560v1 — §4.5 Takeaways and Systems Opportunities; §5.5 Takeaways and Systems Opportunities; §6.4 Takeaways and System Opportunities | arXiv:2606.30560v1 — §2.2 Existing Datasets and Benchmarks; §8.3 Coding-agent benchmarks and tool-use evaluation | arXiv:2606.30560v1 — §9 Limitations and Future Work; §10 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30560 | complete |
| SF-2026-ARXIV-2606-30562 | RP-ec0232f876cca895 | deep | arXiv:2606.30562v1 | SRC-ARXIV@arXiv:2606.30562v1 | arXiv:2606.30562v1 — §7 Model and Training Configuration | arXiv:2606.30562v1 — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Results | arXiv:2606.30562v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30562 | complete |
| SF-2026-ARXIV-2606-30566 | RP-813e9c4e510aa28c | deep | arXiv:2606.30566v1 | SRC-ARXIV@arXiv:2606.30566v1 | arXiv:2606.30566v1 — §2 Methodology; §Training data scope.; §Behavioral detection in agentic systems. | arXiv:2606.30566v1 — §2.4 Classifiers and Evaluation; §3 Results; §Expanded frontier evaluation. | arXiv:2606.30566v1 — §2.1 Threat Model; §3.8 Evasion Boundary; §4 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30566 | complete |
| SF-2026-ARXIV-2606-30573 | RP-850629ca96cab7a2 | deep | arXiv:2606.30573v1 | SRC-ARXIV@arXiv:2606.30573v1 | arXiv:2606.30573v1 — §2.2 Task Design; §4.3.1 User persona design | arXiv:2606.30573v1 — §SWE-Interact : Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions; §2 Problem Setup; §3 Experimental Results | arXiv:2606.30573v1 — §4 Discussion; §4.2 Failure modes; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30573 | complete |
| SF-2026-ARXIV-2606-30602 | RP-f89937800dd97a95 | deep | arXiv:2606.30602v1 | SRC-ARXIV@arXiv:2606.30602v1 | arXiv:2606.30602v1 — §MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems; §II-A MAS Design & Topologies; §III-C Problem Formulation | arXiv:2606.30602v1 — §V Experimental Setup; §VI Evaluation; §VI-B RQ2: Application Analysis of Mesa Efficacy | arXiv:2606.30602v1 — §III-B Threat Model; §VI-E 1 Exposure-aware threat surface; §VIII Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30602 | complete |
| SF-2026-ARXIV-2606-30616 | RP-5cf6493514f0098e | deep | arXiv:2606.30616v1 | SRC-ARXIV@arXiv:2606.30616v1 | arXiv:2606.30616v1 — §2 Knowledge-Guided General Agent Training with Specialized Teachers; §4 Three-stage Training Recipe; §4.2 Domain-level Teacher Training | arXiv:2606.30616v1 — §5 Experimental Results; §5.1 Evaluation Setting; §5.2 Results and Observations | arXiv:2606.30616v1 — §6 Limitation and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30616 | complete |
| SF-2026-ARXIV-2606-30627 | RP-3d105626858629f3 | deep | arXiv:2606.30627v1 | SRC-ARXIV@arXiv:2606.30627v1 | arXiv:2606.30627v1 — §Pessimism’s Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models; §2.4 Offline RL and Conservative Methods; §3 Problem Formulation | arXiv:2606.30627v1 — §4 Experimental Setup; §5 Mechanistic Analysis; §7 Results | arXiv:2606.30627v1 — §8 Discussion; §8.3 Limitations; §9 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30627 | complete |
| SF-2026-ARXIV-2606-30634 | RP-3ec76e1762357822 | deep | arXiv:2606.30634v1 | SRC-ARXIV@arXiv:2606.30634v1 | arXiv:2606.30634v1 — §One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining; §E.1 Hyperparameters and Training Details; §E.2 Model architectures | arXiv:2606.30634v1 — §2.2 Hyperparameter Sensitivity and Benchmarking; §4 Theoretical analysis; §5 Large Scale Experiments | arXiv:2606.30634v1 — §8 Discussion and Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30634 | complete |
| SF-2026-ARXIV-2606-30639 | RP-5930983a0b9dd405 | deep | arXiv:2606.30639v1 | SRC-ARXIV@arXiv:2606.30639v1 | arXiv:2606.30639v1 — §3 Methodology; §3.1 Problem Formulation | arXiv:2606.30639v1 — §4 Experiment; §4.1 Setups; §Evaluation Metrics | arXiv:2606.30639v1 — §4.4 Discussion; §5 Conclusion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30639 | complete |
| SF-2026-ARXIV-2606-30697 | RP-87e3eada1644817f | deep | arXiv:2606.30697v1 | SRC-ARXIV@arXiv:2606.30697v1 | arXiv:2606.30697v1 — §LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents; §V LUMOS Architecture; §X-A Why This is an Operating-System Problem | arXiv:2606.30697v1 — §VIII Evaluation Plan | arXiv:2606.30697v1 — §X Discussion; §XI Limitations; §XII Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30697 | complete |
| SF-2026-ARXIV-2606-30704 | RP-cba5d48a1681ab28 | deep | arXiv:2606.30704v1 | SRC-ARXIV@arXiv:2606.30704v1 | arXiv:2606.30704v1 — §From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators; §4 Methodology; §4.1 MetaFlow Architecture | arXiv:2606.30704v1 — §5 Experiments; §5.4 Main Results and Analysis; §Appendix A Main Results | arXiv:2606.30704v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30704 | complete |
| SF-2026-ARXIV-2606-30774 | RP-0a3a49110d4c5c1a | deep | arXiv:2606.30774v1 | SRC-ARXIV@arXiv:2606.30774v1 | arXiv:2606.30774v1 — §Post-training LMs with teacher feedback.; §Shared teacher system prompt. | arXiv:2606.30774v1 — §3 Experimental Setup; §Appendix A Experimental Setup Details; §Appendix B Additional Results | arXiv:2606.30774v1 — §5 Discussion; §Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30774 | complete |
| SF-2026-ARXIV-2606-30775 | RP-5d8af11f61b9e9e2 | deep | arXiv:2606.30775v1 | SRC-ARXIV@arXiv:2606.30775v1 | arXiv:2606.30775v1 — §3 Method; §5.4 Initial training F1 as a diagnostic signal; §Appendix F Production Training F1 Dynamics | arXiv:2606.30775v1 — §4 Experimental Setup; §5 Results; §Appendix C Production train20 Results | arXiv:2606.30775v1 — §6 Conclusion; §Limitations; §Appendix G Iter-0 Training F1 as a Failure Predictor (ToolBench) | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30775 | complete |
| SF-2026-ARXIV-2606-30783 | RP-1d43515d32b0c89c | deep | arXiv:2606.30783v1 | SRC-ARXIV@arXiv:2606.30783v1 | arXiv:2606.30783v1 — §3.2 Task Design; §A.2 Probe design; §E.1 Training for instruction-data separation | arXiv:2606.30783v1 — §3 The SecFid Benchmark; §3.4 Evaluation; §4 Experiments | arXiv:2606.30783v1 — §2 Threat Model; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30783 | complete |
| SF-2026-ARXIV-2606-30788 | RP-bf367d7d07f30733 | deep | arXiv:2606.30788v1 | SRC-ARXIV@arXiv:2606.30788v1 | arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training. | arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup | arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30788 | complete |
| SF-2026-ARXIV-2606-30789 | RP-f640db9930f76690 | deep | arXiv:2606.30789v1 | SRC-ARXIV@arXiv:2606.30789v1 | arXiv:2606.30789v1 — §Predictable GRPO: A Closed-Form Model of Training Dynamics; §Algorithms and training reports.; §4.2 Training Setup | arXiv:2606.30789v1 — §3.1 Setup; §4 Experimental Setup; §4.2 Training Setup | arXiv:2606.30789v1 — §The boundary tracks the prediction where the linearization holds (Figure 7 ).; §6 Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30789 | complete |
| SF-2026-ARXIV-2606-30801 | RP-1b24f8bfb71fa6d6 | deep | arXiv:2606.30801v1 | SRC-ARXIV@arXiv:2606.30801v1 | arXiv:2606.30801v1 — §3 Experiment Design | arXiv:2606.30801v1 — §3 Experiment Design; §4.2 “For You” vs “Following” Feed Analysis; §4.3 Counterfactual Analysis | arXiv:2606.30801v1 — §6 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30801 | complete |
| SF-2026-ARXIV-2606-30814 | RP-e6463bc47b54e014 | deep | arXiv:2606.30814v1 | SRC-ARXIV@arXiv:2606.30814v1 | arXiv:2606.30814v1 — §Calibration Metrics and Calibration Methods.; §Confidence Elicitation Methods.; §The source of reversal depends strongly on the confidence method. | arXiv:2606.30814v1 — §When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs; §4 ACE: Accuracy-Controlled Evaluation; §Setup. | arXiv:2606.30814v1 — §7 Conclusion; §Limitation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30814 | complete |
| SF-2026-ARXIV-2606-30850 | RP-936c919a6e11bfe9 | deep | arXiv:2606.30850v1 | SRC-ARXIV@arXiv:2606.30850v1 | arXiv:2606.30850v1 — §4 Bayesian Prediction in Recommender Systems; §B.1.1 System Prompt; §Appendix C Recommender System Details | arXiv:2606.30850v1 — §5.1 Simulation Setup; §Appendix F Compute and Inference Setup | arXiv:2606.30850v1 — §7 Limitations and Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30850 | complete |
| SF-2026-ARXIV-2606-30852 | RP-cae3b23a17fd9a10 | deep | arXiv:2606.30852v1 | SRC-ARXIV@arXiv:2606.30852v1 | arXiv:2606.30852v1 — §Training-free early exit.; §3 Method; §3.3 Training and Metrics | arXiv:2606.30852v1 — §4 Experiments; §4.1 Setup | arXiv:2606.30852v1 — §5 Discussion and Limitations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30852 | complete |
| SF-2026-ARXIV-2606-30899 | RP-470a7b8cacd124c2 | deep | arXiv:2606.30899v1 | SRC-ARXIV@arXiv:2606.30899v1 | arXiv:2606.30899v1 — §II Method; §II-A Problem Formulation; §III-B Poisoned Model Training | arXiv:2606.30899v1 — §IV Experiments; §IV-B Evaluation Metrics; §IV-C Main Results | arXiv:2606.30899v1 — §V Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30899 | complete |
| SF-2026-ARXIV-2606-30911 | RP-adfd4250cc19098f | deep | arXiv:2606.30911v1 | SRC-ARXIV@arXiv:2606.30911v1 | arXiv:2606.30911v1 — §Hierarchical organization in agent systems.; §3 Method | arXiv:2606.30911v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results | arXiv:2606.30911v1 — §5 Discussion; §5.3 Limitations; §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30911 | complete |
| SF-2026-ARXIV-2606-30919 | RP-3f6b44173d7702ad | deep | arXiv:2606.30919v1 | SRC-ARXIV@arXiv:2606.30919v1 | arXiv:2606.30919v1 — §2.1. Problem Formulation; §3. Method | arXiv:2606.30919v1 — §1. Introduction; §2. Problem Statement; §2.1. Problem Formulation | arXiv:2606.30919v1 — §6. Conclusion and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30919 | complete |
| SF-2026-ARXIV-2606-30931 | RP-eb007fe17ad16b4e | deep | arXiv:2606.30931v1 | SRC-ARXIV@arXiv:2606.30931v1 | arXiv:2606.30931v1 — §3.1 System Agent and Reward Space; §6.7 Noisy-GT Control: Systematic Bias, Not Imprecision | arXiv:2606.30931v1 — §3 Problem Setup; §6 Experiments; §6.1 Setup | arXiv:2606.30931v1 — §The problem: Byzantine failures, not Gaussian noise.; §7 Conclusion; §Scope and limitations. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-30931 | complete |
| SF-2026-ARXIV-2606-31002 | RP-70d76ad674b711d2 | deep | arXiv:2606.31002v1 | SRC-ARXIV@arXiv:2606.31002v1 | arXiv:2606.31002v1 — §5.1 Factorial Design over (T,F,S) | arXiv:2606.31002v1 — §2.2 Evaluation Context; §2.4 Evaluation Protocol; §4 Performance Evaluation | arXiv:2606.31002v1 — §6 Limitations; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-31002 | complete |

### Source Reviews
<!-- review:SF-2026-ARXIV-2606-29685:start -->
### 2606.29685 — CAREBench: A Child-Safety Risk Benchmark for Language Models

- 问题：当How can we evaluate whether frontier AI systems recognize child-safety risks before they escalate into explicit harm?时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把儿童安全从显式伤害响应前移为上游风险识别，并要求按风险层级验收。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29685:start -->
- 证据与非证明：exact-v1 仅支持《CAREBench: A Child-Safety Risk Benchmark for Language Models》在 CAREBench: A Child-Safety Risk Benchmark for Language Models, 3 Benchmark Scope and Task Definition, 4 Evaluation Protocol 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29685:end -->
- 取舍：收益是把 把儿童安全从显式伤害响应前移为上游风险识别，并要求按风险层级验收。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 CAREBench: A Child-Safety Risk Benchmark for Language Models 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29685v1 — §3.1 Prompt Corpus Design; §Appendix D Methodological Details; §Appendix G Ethical Design and Release Safeguards；arXiv:2606.29685v1 — §CAREBench: A Child-Safety Risk Benchmark for Language Models; §3 Benchmark Scope and Task Definition; §4 Evaluation Protocol；arXiv:2606.29685v1 — §5.1 Overall model failure rates; §5.2 Category-level failure structure; §5.3 Failure mode analysis
<!-- review:SF-2026-ARXIV-2606-29685:end -->

<!-- review:SF-2026-ARXIV-2606-29699:start -->
### 2606.29699 — Early Warning Signals for OpenVLA Failure under Visual Distribution Shift

- 问题：当Visual shifts can cause a vision-language-action policy to fail after initially plausible behavior.时，现有 PLATFORM-MONITORING 合同缺少什么？
- 机制与 owner：证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。 唯一 owner 为 PLATFORM-MONITORING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29699:start -->
- 证据与非证明：exact-v1 仅支持《Early Warning Signals for OpenVLA Failure under Visual Distribution Shift》在 2.3 Activation based analysis, 3.1 Problem setup, 4 Experimental Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-MONITORING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29699:end -->
- 取舍：收益是把 证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.3 Activation based analysis 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29699v1 — §3 Method；arXiv:2606.29699v1 — §2.3 Activation based analysis; §3.1 Problem setup; §4 Experimental Setup；arXiv:2606.29699v1 — §Early Warning Signals for OpenVLA Failure under Visual Distribution Shift; §2.2 Failure detection and robustness; §5.2 Activation monitors predict near term failure
<!-- review:SF-2026-ARXIV-2606-29699:end -->

<!-- review:SF-2026-ARXIV-2606-29700:start -->
### 2606.29700 — Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback

- 问题：当Planning often requires symbolic specifications that are both executable and verifiable.时，现有 AGENT-PLANNING 合同缺少什么？
- 机制与 owner：把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。 唯一 owner 为 AGENT-PLANNING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29700:start -->
- 证据与非证明：exact-v1 仅支持《Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback》在 III-C Planner-in-the-Loop Feedback and Evaluation, IV Experiments, IV-A Experimental Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-PLANNING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29700:end -->
- 取舍：收益是把 把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 III-C Planner-in-the-Loop Feedback and Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29700v1 — §III Method；arXiv:2606.29700v1 — §III-C Planner-in-the-Loop Feedback and Evaluation; §IV Experiments; §IV-A Experimental Setup；arXiv:2606.29700v1 — §V Conclusion
<!-- review:SF-2026-ARXIV-2606-29700:end -->

<!-- review:SF-2026-ARXIV-2606-29708:start -->
### 2606.29708 — Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving

- 问题：当Heterogeneous prefill-decode (PD) inference is now in production: prefill on cost-efficient or supply-available accelerators, decode on bandwidth-strong ones, and KV state crossing mixed interconnects in mixed numerical 时，现有 INFER-PD-DISAGGREGATION 合同缺少什么？
- 机制与 owner：把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。 唯一 owner 为 INFER-PD-DISAGGREGATION；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29708:start -->
- 证据与非证明：exact-v1 仅支持《Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving》在 1 Introduction, 2 The PD Boundary, 2.1 Design Axes Behind the Boundary 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-PD-DISAGGREGATION 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29708:end -->
- 取舍：收益是把 把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 1 Introduction 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29708v1 — §Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving; §2.1 Design Axes Behind the Boundary；arXiv:2606.29708v1 — §1 Introduction; §2 The PD Boundary; §2.1 Design Axes Behind the Boundary；arXiv:2606.29708v1 — §2 The PD Boundary; §2.1 Design Axes Behind the Boundary; §2.2 Three Boundary Decisions
<!-- review:SF-2026-ARXIV-2606-29708:end -->

<!-- review:SF-2026-ARXIV-2606-29713:start -->
### 2606.29713 — SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution

- 问题：当Hallucination is the reliability bottleneck for LLM-based agents, and fact attribution verifiers are the last line of defense -- yet today's verifiers emit only opaque binary labels, leaving agents unable to self-correct时，现有 AGENT-REFLECTION 合同缺少什么？
- 机制与 owner：把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。 唯一 owner 为 AGENT-REFLECTION；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29713:start -->
- 证据与非证明：exact-v1 仅支持《SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution》在 3 Experiments, 3.1 Setup, 3.2 Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-REFLECTION 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29713:end -->
- 取舍：收益是把 把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29713v1 — §2 Method; §2.1 Problem Formulation and Overview; §2.4 Training Pipeline；arXiv:2606.29713v1 — §3 Experiments; §3.1 Setup; §3.2 Main Results；arXiv:2606.29713v1 — §2.3 From Binary Reward Failure to Process Reward; §The failure of binary reward.; §4.3 Limitations
<!-- review:SF-2026-ARXIV-2606-29713:end -->

<!-- review:SF-2026-ARXIV-2606-29718:start -->
### 2606.29718 — Diagnosing and Mitigating Context Rot in Long-horizon Search

- 问题：当Extensive context has become the norm as Large Language Models (LLMs) are increasingly deployed in long-horizon search tasks.时，现有 AGENT-CONTEXT 合同缺少什么？
- 机制与 owner：把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。 唯一 owner 为 AGENT-CONTEXT；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29718:start -->
- 证据与非证明：exact-v1 仅支持《Diagnosing and Mitigating Context Rot in Long-horizon Search》在 3.3 Experimental Setup and Results, Setup, Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-CONTEXT 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29718:end -->
- 取舍：收益是把 把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3.3 Experimental Setup and Results 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29718v1 — §Appendix D Effect of the Threshold on Other Context Management Methods；arXiv:2606.29718v1 — §3.3 Experimental Setup and Results; §Setup; §Main Results；arXiv:2606.29718v1 — §5 Conclusion; §Appendix G Limitations
<!-- review:SF-2026-ARXIV-2606-29718:end -->

<!-- review:SF-2026-ARXIV-2606-29719:start -->
### 2606.29719 — A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents

- 问题：当Measurements of proprietary LLM evaluators can become invalid within weeks -- we document one case and provide the diagnostic framework to detect it.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 evaluator 漂移和偏好坍缩作为持续评测系统的测量状态。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29719:start -->
- 证据与非证明：exact-v1 仅支持《A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents》在 4 Experimental Setup, 5 Results: The Multi-Evaluator Audit 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29719:end -->
- 取舍：收益是把 把 evaluator 漂移和偏好坍缩作为持续评测系统的测量状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29719v1 — §A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents; §3 The EPC Framework; §5.6 Methodological Ablations；arXiv:2606.29719v1 — §4 Experimental Setup; §5 Results: The Multi-Evaluator Audit；arXiv:2606.29719v1 — §6 Discussion; §6.5 Limitations; §7 Conclusion
<!-- review:SF-2026-ARXIV-2606-29719:end -->

<!-- review:SF-2026-ARXIV-2606-29745:start -->
### 2606.29745 — ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit

- 问题：当What does it mean for a language agent to be adaptive?时，现有 AGENT-PLANNING 合同缺少什么？
- 机制与 owner：以显式 belief state 和逐轮 epistemic credit 控制信息获取与停止动作。 唯一 owner 为 AGENT-PLANNING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29745:start -->
- 证据与非证明：exact-v1 仅支持《ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit》在 5 Experiments, Evaluation Strategy, 6 Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-PLANNING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29745:end -->
- 取舍：收益是把 以显式 belief state 和逐轮 epistemic credit 控制信息获取与停止动作。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29745v1 — §Explicit reasoning does not substitute for epistemic training.; §Training dynamics support turn-level epistemic credit assignment.; §Appendix B ECHO Training Dynamics；arXiv:2606.29745v1 — §5 Experiments; §Evaluation Strategy; §6 Results；arXiv:2606.29745v1 — §7 Conclusion; §Limitations
<!-- review:SF-2026-ARXIV-2606-29745:end -->

<!-- review:SF-2026-ARXIV-2606-29758:start -->
### 2606.29758 — PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF

- 问题：当Reinforcement Learning from Human Feedback (RLHF) for Large Language Models increasingly relies on critic-free methods as a practical alternative to actor--critic training.时，现有 TRAIN-RLHF 合同缺少什么？
- 机制与 owner：以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。 唯一 owner 为 TRAIN-RLHF；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29758:start -->
- 证据与非证明：exact-v1 仅支持《PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF》在 4 Experiments, Experiment setup., 4.2 Analysis on Hyperparameters 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-RLHF 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29758:end -->
- 取舍：收益是把 以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29758v1 — §2.1 Post-Training for LLM Alignment; §3 Method; §Appendix F Monotone Budget Design and PAV；arXiv:2606.29758v1 — §4 Experiments; §Experiment setup.; §4.2 Analysis on Hyperparameters；arXiv:2606.29758v1 — §5 Conclusion
<!-- review:SF-2026-ARXIV-2606-29758:end -->

<!-- review:SF-2026-ARXIV-2606-29775:start -->
### 2606.29775 — SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling

- 问题：当The emergence of Multi-Instance GPU (MIG) technology enables us to run smaller machine learning models on partitions of a GPU rather than the entire device, thus improving utilization and reducing energy consumption, alb时，现有 PLATFORM-GPU-SCHEDULER 合同缺少什么？
- 机制与 owner：把 MIG 切分、性能与能耗纳入可学习的集群调度状态。 唯一 owner 为 PLATFORM-GPU-SCHEDULER；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29775:start -->
- 证据与非证明：exact-v1 仅支持《SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling》在 VI Experimental Results, VI-A Experimental Settings, VI-B Results for Scheduling Algorithms without Repartitioning 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-GPU-SCHEDULER 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29775:end -->
- 取舍：收益是把 把 MIG 切分、性能与能耗纳入可学习的集群调度状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 VI Experimental Results 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29775v1 — §SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling; §IV Problem Formulation and Methodology；arXiv:2606.29775v1 — §VI Experimental Results; §VI-A Experimental Settings; §VI-B Results for Scheduling Algorithms without Repartitioning；arXiv:2606.29775v1 — §VII Conclusion and Future Work
<!-- review:SF-2026-ARXIV-2606-29775:end -->

<!-- review:SF-2026-ARXIV-2606-29778:start -->
### 2606.29778 — Mandol: An Agglomerative Agent Memory System for Long-Term Conversations

- 问题：当Long-term conversational agents need to remember and query cross-session, multi-typed information with complex correlations.时，现有 AGENT-MEMORY 合同缺少什么？
- 机制与 owner：以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。 唯一 owner 为 AGENT-MEMORY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29778:start -->
- 证据与非证明：exact-v1 仅支持《Mandol: An Agglomerative Agent Memory System for Long-Term Conversations》在 5. Evaluation, 5.1. Experimental Setup, 5.2. Accuracy and Token Efficiency Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MEMORY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29778:end -->
- 取舍：收益是把 以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5. Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29778v1 — §Mandol: An Agglomerative Agent Memory System for Long-Term Conversations; §2.2. Memory Retrieval Methods; §3. Mandol System Design；arXiv:2606.29778v1 — §5. Evaluation; §5.1. Experimental Setup; §5.2. Accuracy and Token Efficiency Results；arXiv:2606.29778v1 — §6. Conclusion
<!-- review:SF-2026-ARXIV-2606-29778:end -->

<!-- review:SF-2026-ARXIV-2606-29784:start -->
### 2606.29784 — HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data

- 问题：当Reliable generative AI models critically rely on expert human annotations to evaluate output quality, yet these "gold" labels are expensive to collect and limited in quantity.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：用历史 noisy labels 提高生成模型评测灵敏度，同时保留专家标签边界。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29784:start -->
- 证据与非证明：exact-v1 仅支持《HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data》在 HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data, 1.2 Model Evaluation Target Parameters and Tasks, 2 Bias and Variance in Model Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29784:end -->
- 取舍：收益是把 用历史 noisy labels 提高生成模型评测灵敏度，同时保留专家标签边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29784v1 — §3 Method: History Enhanced RObust (HERO) Model Evaluation；arXiv:2606.29784v1 — §HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data; §1.2 Model Evaluation Target Parameters and Tasks; §2 Bias and Variance in Model Evaluation；arXiv:2606.29784v1 — §1 Introduction; §1.1 Motivation and Contribution; §1.2 Model Evaluation Target Parameters and Tasks
<!-- review:SF-2026-ARXIV-2606-29784:end -->

<!-- review:SF-2026-ARXIV-2606-29788:start -->
### 2606.29788 — MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory

- 问题：当When a multimodal AI agent is asked to forget a fact, current memory systems usually delete the text entry and report success.时，现有 AGENT-MEMORY 合同缺少什么？
- 机制与 owner：证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。 唯一 owner 为 AGENT-MEMORY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29788:start -->
- 证据与非证明：exact-v1 仅支持《MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory》在 2.4 Per-Architecture IPG Analysis, 3 The MemLeak Benchmark, 4 Experiments 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MEMORY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29788:end -->
- 取舍：收益是把 证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.4 Per-Architecture IPG Analysis 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §4.1 Systems Evaluated; §5 Design Implications；arXiv:2606.29788v1 — §2.4 Per-Architecture IPG Analysis; §3 The MemLeak Benchmark; §4 Experiments；arXiv:2606.29788v1 — §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-29788:end -->

<!-- review:SF-2026-ARXIV-2606-29871:start -->
### 2606.29871 — AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes

- 问题：当We present the AI Training Manager, a bounded LLM-based supervisory controller for adaptive machine learning training.时，现有 PLATFORM-TRAINING-OPERATOR 合同缺少什么？
- 机制与 owner：把训练 recipe 的观测、建议、边界检查和执行组织成受限闭环控制面。 唯一 owner 为 PLATFORM-TRAINING-OPERATOR；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29871:start -->
- 证据与非证明：exact-v1 仅支持《AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes》在 IV Experiments and Results, IV-A TinyStories Language-Model Experiments, IV-B Robotic-Arm Reinforcement-Learning Experiments 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-TRAINING-OPERATOR 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29871:end -->
- 取舍：收益是把 把训练 recipe 的观测、建议、边界检查和执行组织成受限闭环控制面。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 IV Experiments and Results 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29871v1 — §AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes; §II-A Inner-Loop Heuristics and Adaptive Training Methods; §II-B Hyperparameter Optimization, AutoML, and Population-Based Training；arXiv:2606.29871v1 — §IV Experiments and Results; §IV-A TinyStories Language-Model Experiments; §IV-B Robotic-Arm Reinforcement-Learning Experiments；arXiv:2606.29871v1 — §V Discussion and Limitations; §VI Conclusion
<!-- review:SF-2026-ARXIV-2606-29871:end -->

<!-- review:SF-2026-ARXIV-2606-29887:start -->
### 2606.29887 — SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing

- 问题：当In real-world applications, guardrails are often expected to identify unsafe user-model interactions according to application-specific safety policies, rather than relying on predefined risk taxonomies.时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：把应用自定义政策的层级冲突与多轮上下文纳入 guardrail 验收。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29887:start -->
- 证据与非证明：exact-v1 仅支持《SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing》在 SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing, 3.4 Benchmark Construction, 3.6 Evaluation Protocols 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29887:end -->
- 取舍：收益是把 把应用自定义政策的层级冲突与多轮上下文纳入 guardrail 验收。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29887v1 — §3.2 Hierarchical Design; §3.2.3 Level 2: Adapting to Novel Policy Frameworks; §Appendix D System Prompt for Policy-configurable Guards；arXiv:2606.29887v1 — §SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing; §3.4 Benchmark Construction; §3.6 Evaluation Protocols；arXiv:2606.29887v1 — §5 Limitations and Future Work; §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-29887:end -->

<!-- review:SF-2026-ARXIV-2606-29914:start -->
### 2606.29914 — MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation

- 问题：当Agent memory systems are increasingly evaluated against RAG and full-context baselines, but reported gains often mix changes in the memory method with changes in the language model, embedding model, or retrieval pipeline时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29914:start -->
- 证据与非证明：exact-v1 仅支持《MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation》在 MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation, Memory systems and benchmarks., Confounds in memory evaluation. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29914:end -->
- 取舍：收益是把 揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29914v1 — §Memory systems and benchmarks.; §B.3 When Might Architecture Matter?; §Memory systems.；arXiv:2606.29914v1 — §MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation; §Memory systems and benchmarks.; §Confounds in memory evaluation.；arXiv:2606.29914v1 — §4.2 Model Behavior: Three Models, Three Conclusions; §Sonnet’s length-driven failure.; §5 Conclusion
<!-- review:SF-2026-ARXIV-2606-29914:end -->

<!-- review:SF-2026-ARXIV-2606-29920:start -->
### 2606.29920 — Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?

- 问题：当Rubric-based scoring has become a widely used paradigm in model evaluation, typically with LLM-as-a-Judge (LaaJ) for rubric scoring.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29920:start -->
- 证据与非证明：exact-v1 仅支持《Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?》在 Rubric-based evaluation, 3.3 Benchmark Statistics, 4 Experiments 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29920:end -->
- 取舍：收益是把 把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 Rubric-based evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29920v1 — §1 Introduction; §2 Related Work; §Rubric-based evaluation；arXiv:2606.29920v1 — §Rubric-based evaluation; §3.3 Benchmark Statistics; §4 Experiments；arXiv:2606.29920v1 — §5 Conclusion; §Limitations
<!-- review:SF-2026-ARXIV-2606-29920:end -->

<!-- review:SF-2026-ARXIV-2606-29955:start -->
### 2606.29955 — SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows

- 问题：当Spreadsheets are widely used for business analysis, financial modeling, reporting, and decision-making.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 spreadsheet Agent 从单操作测量升级为带副作用的端到端业务工作流。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29955:start -->
- 证据与非证明：exact-v1 仅支持《SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows》在 2.2 Benchmark Construction, 2.3 Benchmark Statistics, 2.4 Evaluation Metrics 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29955:end -->
- 取舍：收益是把 把 spreadsheet Agent 从单操作测量升级为带副作用的端到端业务工作流。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.2 Benchmark Construction 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29955v1 — §1 Introduction; §2 SpreadsheetBench 2; §2.1 Task Categories；arXiv:2606.29955v1 — §2.2 Benchmark Construction; §2.3 Benchmark Statistics; §2.4 Evaluation Metrics；arXiv:2606.29955v1 — §3.3 Analysis and Discussions; §5 Conclusion; §Appendix A Broader Discussion
<!-- review:SF-2026-ARXIV-2606-29955:end -->

<!-- review:SF-2026-ARXIV-2606-29957:start -->
### 2606.29957 — SWE-Together: Evaluating Coding Agents in Interactive User Sessions

- 问题：当Most coding-agent benchmarks are static: an agent receives a complete task description up front and is judged only by its final code.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把编码 Agent 的用户澄清、约束追加与交互过程纳入发布评测。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29957:start -->
- 证据与非证明：exact-v1 仅支持《SWE-Together: Evaluating Coding Agents in Interactive User Sessions》在 2.3 Evaluation Method, 3 Experiments and Results, 3.1 Main Result 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29957:end -->
- 取舍：收益是把 把编码 Agent 的用户澄清、约束追加与交互过程纳入发布评测。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.3 Evaluation Method 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29957v1 — §2.3 Evaluation Method；arXiv:2606.29957v1 — §2.3 Evaluation Method; §3 Experiments and Results; §3.1 Main Result；arXiv:2606.29957v1 — §5 Limitations and Conclusion
<!-- review:SF-2026-ARXIV-2606-29957:end -->

<!-- review:SF-2026-ARXIV-2606-29959:start -->
### 2606.29959 — Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented Generation

- 问题：当Retrieval-augmented generation (RAG) typically retrieves a fixed number of passages for every query.时，现有 AGENT-RAG 合同缺少什么？
- 机制与 owner：按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。 唯一 owner 为 AGENT-RAG；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29959:start -->
- 证据与非证明：exact-v1 仅支持《Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented Generation》在 3 Problem Setup and Method, 4 Experimental Setup, Evaluation. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-RAG 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29959:end -->
- 取舍：收益是把 按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 Problem Setup and Method 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29959v1 — §3 Problem Setup and Method; §When the method helps.; §Appendix A Extended Method Details；arXiv:2606.29959v1 — §3 Problem Setup and Method; §4 Experimental Setup; §Evaluation.；arXiv:2606.29959v1 — §7 Discussion; §8 Limitations; §10 Conclusion
<!-- review:SF-2026-ARXIV-2606-29959:end -->

<!-- review:SF-2026-ARXIV-2606-29975:start -->
### 2606.29975 — Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets

- 问题：当Atomistic machine learning datasets are increasingly used for training: large immutable snapshots are read repeatedly, shuffled across epochs, staged across clusters' storage systems, and republished as reusable scientif时，现有 TRAIN-DATA 合同缺少什么？
- 机制与 owner：为只读大规模训练数据定义快照、shuffle、跨集群 staging 与再发布存储层。 唯一 owner 为 TRAIN-DATA；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29975:start -->
- 证据与非证明：exact-v1 仅支持《Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets》在 4 Evaluation Methodology, 5 Benchmark Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-DATA 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29975:end -->
- 取舍：收益是把 为只读大规模训练数据定义快照、shuffle、跨集群 staging 与再发布存储层。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Evaluation Methodology 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29975v1 — §Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets; §2.2 Scientific Storage and Training Stores; §3 System Design；arXiv:2606.29975v1 — §4 Evaluation Methodology; §5 Benchmark Results；arXiv:2606.29975v1 — §6 Discussion and Limitations; §8 Conclusion
<!-- review:SF-2026-ARXIV-2606-29975:end -->

<!-- review:SF-2026-ARXIV-2606-29982:start -->
### 2606.29982 — Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference

- 问题：当Mixture-of-Experts (MoE) architectures enable language models to achieve unprecedented scale via sparse activation.时，现有 MODEL-MOE 合同缺少什么？
- 机制与 owner：按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。 唯一 owner 为 MODEL-MOE；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29982:start -->
- 证据与非证明：exact-v1 仅支持《Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference》在 III Analysis and Challenges, III-A 1 Quantitative Analysis, III-B 1 Quantitative Analysis 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 MODEL-MOE 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29982:end -->
- 取舍：收益是把 按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 III Analysis and Challenges 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29982v1 — §II-B Multi-Device Systems; §IV System Design；arXiv:2606.29982v1 — §III Analysis and Challenges; §III-A 1 Quantitative Analysis; §III-B 1 Quantitative Analysis；arXiv:2606.29982v1 — §VII Conclusion
<!-- review:SF-2026-ARXIV-2606-29982:end -->

<!-- review:SF-2026-ARXIV-2606-29986:start -->
### 2606.29986 — HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators

- 问题：当LLM inference comprises a compute-bound prefill phase and a memory-bound decode phase, and recent systems disaggregate them onto separate hardware.时，现有 INFER-PD-DISAGGREGATION 合同缺少什么？
- 机制与 owner：把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。 唯一 owner 为 INFER-PD-DISAGGREGATION；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-29986:start -->
- 证据与非证明：exact-v1 仅支持《HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators》在 4. Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-PD-DISAGGREGATION 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-29986:end -->
- 取舍：收益是把 把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4. Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.29986v1 — §3. Design；arXiv:2606.29986v1 — §4. Evaluation；arXiv:2606.29986v1 — §6. Conclusion
<!-- review:SF-2026-ARXIV-2606-29986:end -->

<!-- review:SF-2026-ARXIV-2606-30005:start -->
### 2606.30005 — LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception

- 问题：当Long-horizon tool agents are bottlenecked by how their context grows toward the limits of the context window.时，现有 AGENT-CONTEXT 合同缺少什么？
- 机制与 owner：让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。 唯一 owner 为 AGENT-CONTEXT；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30005:start -->
- 证据与非证明：exact-v1 仅支持《LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception》在 Problem Setup, Experiments, Experiment Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-CONTEXT 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30005:end -->
- 取舍：收益是把 让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 Problem Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30005v1 — §Methodology; §Appendix C Method Capability Comparison；arXiv:2606.30005v1 — §Problem Setup; §Experiments; §Experiment Setup；arXiv:2606.30005v1 — §Limitations; §Conclusion
<!-- review:SF-2026-ARXIV-2606-30005:end -->

<!-- review:SF-2026-ARXIV-2606-30107:start -->
### 2606.30107 — Structural Certification for Reliable Physical Design with Language Models

- 问题：当An unreliable language model can be made to produce reliable physical designs if the authority to assert is moved out of the model: the model proposes, and a deterministic engine alone certifies, returning certified, imp时，现有 AGENT-TOOL-CALLING 合同缺少什么？
- 机制与 owner：把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。 唯一 owner 为 AGENT-TOOL-CALLING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30107:start -->
- 证据与非证明：exact-v1 仅支持《Structural Certification for Reliable Physical Design with Language Models》在 Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-TOOL-CALLING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30107:end -->
- 取舍：收益是把 把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 Results 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30107v1 — §Structural Certification for Reliable Physical Design with Language Models; §The framework; §PHACT certifies valid designs and refuses impossible ones；arXiv:2606.30107v1 — §Results；arXiv:2606.30107v1 — §Discussion
<!-- review:SF-2026-ARXIV-2606-30107:end -->

<!-- review:SF-2026-ARXIV-2606-30119:start -->
### 2606.30119 — On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting

- 问题：当Since 2023, a new class of bots has emerged: Web Agents.时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：以多层行为指纹识别 Web Agent，改变开放网络中的 Agent 身份与审计边界。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30119:start -->
- 证据与非证明：exact-v1 仅支持《On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting》在 3.2. Experimental Protocol, 7.1. Multi-Layer Classification Setup, 7.2. Multi-Layer Classification Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30119:end -->
- 取舍：收益是把 以多层行为指纹识别 Web Agent，改变开放网络中的 Agent 身份与审计边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3.2. Experimental Protocol 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30119v1 — §3. Methodology; §3.1.3. Honeysite Design；arXiv:2606.30119v1 — §3.2. Experimental Protocol; §7.1. Multi-Layer Classification Setup; §7.2. Multi-Layer Classification Evaluation；arXiv:2606.30119v1 — §8. Limitations and Discussion; §10. Conclusion & Future Work
<!-- review:SF-2026-ARXIV-2606-30119:end -->

<!-- review:SF-2026-ARXIV-2606-30185:start -->
### 2606.30185 — Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents

- 问题：当Improving vision-language models (VLMs) on visual reasoning typically requires retraining or hand-designed prompts and tools.时，现有 AGENT-TOOL-CALLING 合同缺少什么？
- 机制与 owner：让冻结 VLM 动态生成、评估并演化 skill/tool 集合，改变工具注册状态。 唯一 owner 为 AGENT-TOOL-CALLING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30185:start -->
- 证据与非证明：exact-v1 仅支持《Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents》在 4 Experiments, 4.1 Experimental Setup, Benchmarks. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-TOOL-CALLING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30185:end -->
- 取舍：收益是把 让冻结 VLM 动态生成、评估并演化 skill/tool 集合，改变工具注册状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30185v1 — §3 Method; §3.1 Problem Formulation; §A.2 RL Baseline Training Compute；arXiv:2606.30185v1 — §4 Experiments; §4.1 Experimental Setup; §Benchmarks.；arXiv:2606.30185v1 — §5 Conclusion; §Limitations
<!-- review:SF-2026-ARXIV-2606-30185:end -->

<!-- review:SF-2026-ARXIV-2606-30251:start -->
### 2606.30251 — TACO: Tool-Augmented Credit Optimization for Agentic Tool Use

- 问题：当Agentic multimodal models perform diverse operations on an image via code and reason over the returned view, an effective paradigm for fine-grained visual question answering.时，现有 TRAIN-RLHF 合同缺少什么？
- 机制与 owner：把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。 唯一 owner 为 TRAIN-RLHF；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30251:start -->
- 证据与非证明：exact-v1 仅支持《TACO: Tool-Augmented Credit Optimization for Agentic Tool Use》在 4 Experiments, 4.1 Experimental Setup, Benchmarks and baselines. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-RLHF 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30251:end -->
- 取舍：收益是把 把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30251v1 — §3 Method; §3.4 Training; §4.6 Training Dynamics；arXiv:2606.30251v1 — §4 Experiments; §4.1 Experimental Setup; §Benchmarks and baselines.；arXiv:2606.30251v1 — §5 Conclusion; §Probe parse failure.; §Appendix F Limitations and Future Work
<!-- review:SF-2026-ARXIV-2606-30251:end -->

<!-- review:SF-2026-ARXIV-2606-30263:start -->
### 2606.30263 — Defending Against Harmful Supervision Hidden in Benign Samples

- 问题：当Existing defenses are effective when harmful content is explicitly mixed into downstream fine-tuning data, but crafted samples can instead hide harmful supervision inside benign tasks.时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30263:start -->
- 证据与非证明：exact-v1 仅支持《Defending Against Harmful Supervision Hidden in Benign Samples》在 4.1 Optimization Dynamic Analysis, 5 Experiments, Appendix A Theoretical Analysis 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30263:end -->
- 取舍：收益是把 揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4.1 Optimization Dynamic Analysis 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30263v1 — §4 Methodology; §B.1 Details on Baseline Methods; §C.1 Ablation on Different Design of η \eta Function；arXiv:2606.30263v1 — §4.1 Optimization Dynamic Analysis; §5 Experiments; §Appendix A Theoretical Analysis；arXiv:2606.30263v1 — §6 Conclusion; §7 Limitations
<!-- review:SF-2026-ARXIV-2606-30263:end -->

<!-- review:SF-2026-ARXIV-2606-30265:start -->
### 2606.30265 — When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding

- 问题：当Speculative decoding accelerates language model inference by using a fast drafter to propose candidate tokens that are then verified by a larger target model.时，现有 INFER-SPECULATIVE-DECODING 合同缺少什么？
- 机制与 owner：给 speculative decoding 的 draft 接受事件建立可解释理论边界。 唯一 owner 为 INFER-SPECULATIVE-DECODING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30265:start -->
- 证据与非证明：exact-v1 仅支持《When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding》在 Theoretical analysis., 4.1 Setup, 5.1 Setup and Notation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-SPECULATIVE-DECODING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30265:end -->
- 取舍：收益是把 给 speculative decoding 的 draft 接受事件建立可解释理论边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 Theoretical analysis. 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30265v1 — §1 Introduction; §2 Related Works; §Architectural variants.；arXiv:2606.30265v1 — §Theoretical analysis.; §4.1 Setup; §5.1 Setup and Notation；arXiv:2606.30265v1 — §7 Conclusion
<!-- review:SF-2026-ARXIV-2606-30265:end -->

<!-- review:SF-2026-ARXIV-2606-30338:start -->
### 2606.30338 — Sequential Fairness Auditing with Limited Output Access

- 问题：当External evaluations are becoming increasingly central to the governance of AI systems.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：在有限输出访问下把外部公平审计建模为顺序采样与停止合同。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30338:start -->
- 证据与非证明：exact-v1 仅支持《Sequential Fairness Auditing with Limited Output Access》在 2.1. Statistical Fairness Evaluation, 4. Experimental Setup, 4.6. Population-Level Fairness Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30338:end -->
- 取舍：收益是把 在有限输出访问下把外部公平审计建模为顺序采样与停止合同。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.1. Statistical Fairness Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30338v1 — §3. Methodology; §Base Architectures；arXiv:2606.30338v1 — §2.1. Statistical Fairness Evaluation; §4. Experimental Setup; §4.6. Population-Level Fairness Evaluation；arXiv:2606.30338v1 — §6. Discussion
<!-- review:SF-2026-ARXIV-2606-30338:end -->

<!-- review:SF-2026-ARXIV-2606-30373:start -->
### 2606.30373 — Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs

- 问题：当AI-powered Applications (AI-Apps), hosted on platforms such as Hugging Face, are democratizing access to pre-trained models through online inference and fine-tuning services.时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：把预训练模型 hub 的应用组合、权重来源与在线执行面纳入供应链威胁模型。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30373:start -->
- 证据与非证明：exact-v1 仅支持《Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs》在 5.2. Basic Threat Analysis, 5.3. Input Injection Vulnerability Analysis, 5.4. Data Leakage Analysis 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30373:end -->
- 取舍：收益是把 把预训练模型 hub 的应用组合、权重来源与在线执行面纳入供应链威胁模型。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5.2. Basic Threat Analysis 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30373v1 — §3.6. Model Training via AI-Apps; §5. Measurement Methodology；arXiv:2606.30373v1 — §5.2. Basic Threat Analysis; §5.3. Input Injection Vulnerability Analysis; §5.4. Data Leakage Analysis；arXiv:2606.30373v1 — §4. AI-App Threats; §4.1. Threat Model; §5.2. Basic Threat Analysis
<!-- review:SF-2026-ARXIV-2606-30373:end -->

<!-- review:SF-2026-ARXIV-2606-30383:start -->
### 2606.30383 — Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents

- 问题：当A rapidly growing class of LLM agents is multi-party: the agent acts for a principal (who briefs it, sends follow-ups, and receives results) while also conversing in a separate channel with a counterparty whose interests时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30383:start -->
- 证据与非证明：exact-v1 仅支持《Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents》在 Setup., Agent benchmarks are two-party., Privacy benchmarks isolate information flow, not adversarial pressure. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30383:end -->
- 取舍：收益是把 把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 Setup. 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30383v1 — §Methods.；arXiv:2606.30383v1 — §Setup.; §Agent benchmarks are two-party.; §Privacy benchmarks isolate information flow, not adversarial pressure.；arXiv:2606.30383v1 — §Why one failure axis is not enough.; §Failures compound: a worked trace.; §9 Limitations
<!-- review:SF-2026-ARXIV-2606-30383:end -->

<!-- review:SF-2026-ARXIV-2606-30389:start -->
### 2606.30389 — Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding

- 问题：当Dynamic sparse attention (DSA) accelerates long-context LLM decoding by attending to only the top-K KV blocks relevant to each query, but it introduces a serialized selection-to-attention dependency that emerges as a new时，现有 INFER-DECODE 合同缺少什么？
- 机制与 owner：以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。 唯一 owner 为 INFER-DECODE；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30389:start -->
- 证据与非证明：exact-v1 仅支持《Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding》在 5 Evaluation, 5.1 Experiment Setups, 5.2 Accelerate Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-DECODE 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30389:end -->
- 取舍：收益是把 以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5 Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30389v1 — §3 The Design Space; §4 Design；arXiv:2606.30389v1 — §5 Evaluation; §5.1 Experiment Setups; §5.2 Accelerate Evaluation；arXiv:2606.30389v1 — §7 Conclusion; §Limitations
<!-- review:SF-2026-ARXIV-2606-30389:end -->

<!-- review:SF-2026-ARXIV-2606-30391:start -->
### 2606.30391 — Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs

- 问题：当As LLM inference becomes a major cloud workload, its growing energy footprint makes cluster-wide energy optimization increasingly important.时，现有 INFER-SCHEDULING 合同缺少什么？
- 机制与 owner：让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。 唯一 owner 为 INFER-SCHEDULING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30391:start -->
- 证据与非证明：exact-v1 仅支持《Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs》在 4. Evaluation, 4.1. Experimental Setup, 4.4. Micro-benchmarks 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-SCHEDULING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30391:end -->
- 取舍：收益是把 让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4. Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30391v1 — §3. Festina Design; §3.1. System Overview; §Appendix I Prior Energy-Efficient LLM Serving Systems；arXiv:2606.30391v1 — §4. Evaluation; §4.1. Experimental Setup; §4.4. Micro-benchmarks；arXiv:2606.30391v1 — §6. Conclusion
<!-- review:SF-2026-ARXIV-2606-30391:end -->

<!-- review:SF-2026-ARXIV-2606-30449:start -->
### 2606.30449 — Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring

- 问题：当Probes on model internals could help monitor agentic systems if they identify harmful text or tool actions before those actions are generated.时，现有 PLATFORM-MONITORING 合同缺少什么？
- 机制与 owner：三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。 唯一 owner 为 PLATFORM-MONITORING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30449:start -->
- 证据与非证明：exact-v1 仅支持《Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring》在 In-context misalignment evaluations., 4 Experiments, 5 Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-MONITORING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30449:end -->
- 取舍：收益是把 三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 In-context misalignment evaluations. 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30449v1 — §3 Methods; §Appendix A Methodology details; §A.1 Methodology divergences from the closest prior work；arXiv:2606.30449v1 — §In-context misalignment evaluations.; §4 Experiments; §5 Results；arXiv:2606.30449v1 — §6 Discussion; §7 Limitations; §8 Conclusion
<!-- review:SF-2026-ARXIV-2606-30449:end -->

<!-- review:SF-2026-ARXIV-2606-30531:start -->
### 2606.30531 — Entity Binding Failures in Tool-Augmented Agents

- 问题：当Tool-augmented language-model agents are often evaluated by whether they select the correct tool, produce valid API arguments, and complete the requested task.时，现有 AGENT-TOOL-CALLING 合同缺少什么？
- 机制与 owner：把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。 唯一 owner 为 AGENT-TOOL-CALLING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30531:start -->
- 证据与非证明：exact-v1 仅支持《Entity Binding Failures in Tool-Augmented Agents》在 V Experimental Setup, V-G Evaluation Protocol, VI Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-TOOL-CALLING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30531:end -->
- 取舍：收益是把 把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 V Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30531v1 — §III Problem Formulation; §IV Method; §V-E Methods Compared；arXiv:2606.30531v1 — §V Experimental Setup; §V-G Evaluation Protocol; §VI Results；arXiv:2606.30531v1 — §Entity Binding Failures in Tool-Augmented Agents; §VI-C Failure Modes by Ambiguity Type; §VII Discussion
<!-- review:SF-2026-ARXIV-2606-30531:end -->

<!-- review:SF-2026-ARXIV-2606-30534:start -->
### 2606.30534 — Orca: The World is in Your Mind

- 问题：当We introduce Orca, an initial instantiation of a general world foundation model.时，现有 MULTIMODAL-WORLD-MODELS 合同缺少什么？
- 机制与 owner：以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。 唯一 owner 为 MULTIMODAL-WORLD-MODELS；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30534:start -->
- 证据与非证明：exact-v1 仅支持《Orca: The World is in Your Mind》在 4 Evaluation, 4.2 Downstream Readout Analysis, Appendix E Evaluation Settings 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 MULTIMODAL-WORLD-MODELS 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30534:end -->
- 取舍：收益是把 以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30534v1 — §2.2 Architecture; §3 Training; §3.1 Pre-Training；arXiv:2606.30534v1 — §4 Evaluation; §4.2 Downstream Readout Analysis; §Appendix E Evaluation Settings；arXiv:2606.30534v1 — §5 Conclusion
<!-- review:SF-2026-ARXIV-2606-30534:end -->

<!-- review:SF-2026-ARXIV-2606-30546:start -->
### 2606.30546 — MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems

- 问题：当The rapid emergence of LLM-based agentic frameworks has significantly reduced the cost of assembling multi-agent systems (MAS), enabling fast prototyping and exploration of agentic behaviors.时，现有 AGENT-MULTI-AGENT 合同缺少什么？
- 机制与 owner：以 specification-driven validation 把多 Agent 原型升级为可重复的系统验收。 唯一 owner 为 AGENT-MULTI-AGENT；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30546:start -->
- 证据与非证明：exact-v1 仅支持《MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems》在 2.4. MAS Experimentation and Evaluation, 7. Labs: Testing, Benchmarking, and Evaluation Environment, 8. Experimental Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MULTI-AGENT 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30546:end -->
- 取舍：收益是把 以 specification-driven validation 把多 Agent 原型升级为可重复的系统验收。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.4. MAS Experimentation and Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30546v1 — §MAS-Lab: A Specification - Driven Validation Framework for Reliable Multi - Agent Systems; §2.3. Agent Operating Systems; §3. MAS-Lab Design Objectives；arXiv:2606.30546v1 — §2.4. MAS Experimentation and Evaluation; §7. Labs: Testing, Benchmarking, and Evaluation Environment; §8. Experimental Evaluation；arXiv:2606.30546v1 — §9. Discussion; §10. Conclusions
<!-- review:SF-2026-ARXIV-2606-30546:end -->

<!-- review:SF-2026-ARXIV-2606-30560:start -->
### 2606.30560 — TraceLab: Characterizing Coding Agent Workloads for LLM Serving

- 问题：当Coding agents are rapidly becoming a major application of agentic LLMs, but serving them efficiently remains challenging.时，现有 INFER-SCHEDULING 合同缺少什么？
- 机制与 owner：用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。 唯一 owner 为 INFER-SCHEDULING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30560:start -->
- 证据与非证明：exact-v1 仅支持《TraceLab: Characterizing Coding Agent Workloads for LLM Serving》在 2.2 Existing Datasets and Benchmarks, 8.3 Coding-agent benchmarks and tool-use evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-SCHEDULING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30560:end -->
- 取舍：收益是把 用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.2 Existing Datasets and Benchmarks 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30560v1 — §4.5 Takeaways and Systems Opportunities; §5.5 Takeaways and Systems Opportunities; §6.4 Takeaways and System Opportunities；arXiv:2606.30560v1 — §2.2 Existing Datasets and Benchmarks; §8.3 Coding-agent benchmarks and tool-use evaluation；arXiv:2606.30560v1 — §9 Limitations and Future Work; §10 Conclusion
<!-- review:SF-2026-ARXIV-2606-30560:end -->

<!-- review:SF-2026-ARXIV-2606-30562:start -->
### 2606.30562 — Morphing into Hybrid Attention Models

- 问题：当Hybrid attention models improve long-context efficiency by retaining only a subset of full-attention layers and replacing the remaining layers with linear attention.时，现有 MODEL-LONG-CONTEXT 合同缺少什么？
- 机制与 owner：把全注意力层替换为线性注意力的转换、校准和质量边界系统化。 唯一 owner 为 MODEL-LONG-CONTEXT；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30562:start -->
- 证据与非证明：exact-v1 仅支持《Morphing into Hybrid Attention Models》在 4 Experiments, 4.1 Experiment Setup, 4.2 Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 MODEL-LONG-CONTEXT 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30562:end -->
- 取舍：收益是把 把全注意力层替换为线性注意力的转换、校准和质量边界系统化。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30562v1 — §7 Model and Training Configuration；arXiv:2606.30562v1 — §4 Experiments; §4.1 Experiment Setup; §4.2 Main Results；arXiv:2606.30562v1 — §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-30562:end -->

<!-- review:SF-2026-ARXIV-2606-30566:start -->
### 2606.30566 — Forensic Trajectory Signatures for Agent Memory Poisoning Detection

- 问题：当We discover a behavioral invariant in LLM agents under persistent memory poisoning and characterize its deployment boundary.时，现有 AGENT-MEMORY 合同缺少什么？
- 机制与 owner：用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。 唯一 owner 为 AGENT-MEMORY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30566:start -->
- 证据与非证明：exact-v1 仅支持《Forensic Trajectory Signatures for Agent Memory Poisoning Detection》在 2.4 Classifiers and Evaluation, 3 Results, Expanded frontier evaluation. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MEMORY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30566:end -->
- 取舍：收益是把 用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.4 Classifiers and Evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30566v1 — §2 Methodology; §Training data scope.; §Behavioral detection in agentic systems.；arXiv:2606.30566v1 — §2.4 Classifiers and Evaluation; §3 Results; §Expanded frontier evaluation.；arXiv:2606.30566v1 — §2.1 Threat Model; §3.8 Evasion Boundary; §4 Discussion
<!-- review:SF-2026-ARXIV-2606-30566:end -->

<!-- review:SF-2026-ARXIV-2606-30573:start -->
### 2606.30573 — SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions

- 问题：当We introduce SWE-Interact, a new testbed for evaluating coding agents on multi-turn, interactive, user-driven software engineering tasks.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 SWE benchmark 改为用户驱动的长程多轮会话与动态验收。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30573:start -->
- 证据与非证明：exact-v1 仅支持《SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions》在 SWE-Interact : Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions, 2 Problem Setup, 3 Experimental Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30573:end -->
- 取舍：收益是把 把 SWE benchmark 改为用户驱动的长程多轮会话与动态验收。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 SWE-Interact : Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30573v1 — §2.2 Task Design; §4.3.1 User persona design；arXiv:2606.30573v1 — §SWE-Interact : Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions; §2 Problem Setup; §3 Experimental Results；arXiv:2606.30573v1 — §4 Discussion; §4.2 Failure modes; §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-30573:end -->

<!-- review:SF-2026-ARXIV-2606-30602:start -->
### 2606.30602 — MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems

- 问题：当Multi-agent systems (MAS) are increasingly used to automate complex, distributed workflows.时，现有 AGENT-MULTI-AGENT 合同缺少什么？
- 机制与 owner：按通信通道脆弱性排序防护，改变多 Agent 安全资源分配。 唯一 owner 为 AGENT-MULTI-AGENT；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30602:start -->
- 证据与非证明：exact-v1 仅支持《MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems》在 V Experimental Setup, VI Evaluation, VI-B RQ2: Application Analysis of Mesa Efficacy 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MULTI-AGENT 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30602:end -->
- 取舍：收益是把 按通信通道脆弱性排序防护，改变多 Agent 安全资源分配。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 V Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30602v1 — §MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems; §II-A MAS Design & Topologies; §III-C Problem Formulation；arXiv:2606.30602v1 — §V Experimental Setup; §VI Evaluation; §VI-B RQ2: Application Analysis of Mesa Efficacy；arXiv:2606.30602v1 — §III-B Threat Model; §VI-E 1 Exposure-aware threat surface; §VIII Discussion
<!-- review:SF-2026-ARXIV-2606-30602:end -->

<!-- review:SF-2026-ARXIV-2606-30616:start -->
### 2606.30616 — Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent

- 问题：当We introduce Agents-A1, a 35B Mixture-of-Experts Agentic Model that reaches trillion-parameter-level performance by scaling the agent horizon.时，现有 AGENT-PLATFORM 合同缺少什么？
- 机制与 owner：以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。 唯一 owner 为 AGENT-PLATFORM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30616:start -->
- 证据与非证明：exact-v1 仅支持《Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent》在 5 Experimental Results, 5.1 Evaluation Setting, 5.2 Results and Observations 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-PLATFORM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30616:end -->
- 取舍：收益是把 以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5 Experimental Results 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30616v1 — §2 Knowledge-Guided General Agent Training with Specialized Teachers; §4 Three-stage Training Recipe; §4.2 Domain-level Teacher Training；arXiv:2606.30616v1 — §5 Experimental Results; §5.1 Evaluation Setting; §5.2 Results and Observations；arXiv:2606.30616v1 — §6 Limitation and Future Work
<!-- review:SF-2026-ARXIV-2606-30616:end -->

<!-- review:SF-2026-ARXIV-2606-30627:start -->
### 2606.30627 — Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models

- 问题：当Conservative offline training is widely advocated as a safe foundation for subsequent online adaptation: if a policy stays close to well-supported behaviour, the argument goes, it is less likely to exploit imperfections 时，现有 TRAIN-RLHF 合同缺少什么？
- 机制与 owner：证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。 唯一 owner 为 TRAIN-RLHF；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30627:start -->
- 证据与非证明：exact-v1 仅支持《Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models》在 4 Experimental Setup, 5 Mechanistic Analysis, 7 Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-RLHF 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30627:end -->
- 取舍：收益是把 证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30627v1 — §Pessimism’s Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models; §2.4 Offline RL and Conservative Methods; §3 Problem Formulation；arXiv:2606.30627v1 — §4 Experimental Setup; §5 Mechanistic Analysis; §7 Results；arXiv:2606.30627v1 — §8 Discussion; §8.3 Limitations; §9 Conclusion
<!-- review:SF-2026-ARXIV-2606-30627:end -->

<!-- review:SF-2026-ARXIV-2606-30634:start -->
### 2606.30634 — One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining

- 问题：当Modern large-scale LLM pretraining benefits from utilizing Pipeline Parallelism; however, synchronous implementations leave GPUs idle during pipeline bubbles, wasting computational resources.时，现有 TRAIN-PIPELINE-PARALLEL 合同缺少什么？
- 机制与 owner：证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。 唯一 owner 为 TRAIN-PIPELINE-PARALLEL；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30634:start -->
- 证据与非证明：exact-v1 仅支持《One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining》在 2.2 Hyperparameter Sensitivity and Benchmarking, 4 Theoretical analysis, 5 Large Scale Experiments 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-PIPELINE-PARALLEL 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30634:end -->
- 取舍：收益是把 证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.2 Hyperparameter Sensitivity and Benchmarking 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30634v1 — §One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining; §E.1 Hyperparameters and Training Details; §E.2 Model architectures；arXiv:2606.30634v1 — §2.2 Hyperparameter Sensitivity and Benchmarking; §4 Theoretical analysis; §5 Large Scale Experiments；arXiv:2606.30634v1 — §8 Discussion and Limitations
<!-- review:SF-2026-ARXIV-2606-30634:end -->

<!-- review:SF-2026-ARXIV-2606-30639:start -->
### 2606.30639 — Self-Evolving World Models for LLM Agent Planning

- 问题：当World models offer a principled way to equip long-horizon LLM agents with foresight: predictions of action consequences before execution.时，现有 MULTIMODAL-WORLD-MODELS 合同缺少什么？
- 机制与 owner：让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。 唯一 owner 为 MULTIMODAL-WORLD-MODELS；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30639:start -->
- 证据与非证明：exact-v1 仅支持《Self-Evolving World Models for LLM Agent Planning》在 4 Experiment, 4.1 Setups, Evaluation Metrics 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 MULTIMODAL-WORLD-MODELS 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30639:end -->
- 取舍：收益是把 让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiment 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30639v1 — §3 Methodology; §3.1 Problem Formulation；arXiv:2606.30639v1 — §4 Experiment; §4.1 Setups; §Evaluation Metrics；arXiv:2606.30639v1 — §4.4 Discussion; §5 Conclusion; §Limitations
<!-- review:SF-2026-ARXIV-2606-30639:end -->

<!-- review:SF-2026-ARXIV-2606-30697:start -->
### 2606.30697 — LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents

- 问题：当Current operating systems expose interfaces optimized for human users but not for AI agents.时，现有 AGENT-PLATFORM 合同缺少什么？
- 机制与 owner：提出面向 Agent 的语义 OS 层，使界面状态和动作能力成为稳定平台接口。 唯一 owner 为 AGENT-PLATFORM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30697:start -->
- 证据与非证明：exact-v1 仅支持《LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents》在 VIII Evaluation Plan 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-PLATFORM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30697:end -->
- 取舍：收益是把 提出面向 Agent 的语义 OS 层，使界面状态和动作能力成为稳定平台接口。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 VIII Evaluation Plan 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30697v1 — §LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents; §V LUMOS Architecture; §X-A Why This is an Operating-System Problem；arXiv:2606.30697v1 — §VIII Evaluation Plan；arXiv:2606.30697v1 — §X Discussion; §XI Limitations; §XII Conclusion
<!-- review:SF-2026-ARXIV-2606-30697:end -->

<!-- review:SF-2026-ARXIV-2606-30704:start -->
### 2606.30704 — From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators

- 问题：当Large language models (LLMs) excel across a wide range of tasks, yet their instance-specific solutions often lack the structural consistency needed for reliable deployment.时，现有 AGENT-WORKFLOW 合同缺少什么？
- 机制与 owner：把一次性解题转为可复用工作流合成，并显式验证结构与执行。 唯一 owner 为 AGENT-WORKFLOW；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30704:start -->
- 证据与非证明：exact-v1 仅支持《From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators》在 5 Experiments, 5.4 Main Results and Analysis, Appendix A Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-WORKFLOW 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30704:end -->
- 取舍：收益是把 把一次性解题转为可复用工作流合成，并显式验证结构与执行。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30704v1 — §From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators; §4 Methodology; §4.1 MetaFlow Architecture；arXiv:2606.30704v1 — §5 Experiments; §5.4 Main Results and Analysis; §Appendix A Main Results；arXiv:2606.30704v1 — §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-30704:end -->

<!-- review:SF-2026-ARXIV-2606-30774:start -->
### 2606.30774 — What Drives Interactive Improvement from Feedback?

- 问题：当We study when natural-language feedback produces improvement beyond the gains obtainable from repeated attempts alone.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把自然语言反馈收益与重复尝试收益分离，修正交互改进测量。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30774:start -->
- 证据与非证明：exact-v1 仅支持《What Drives Interactive Improvement from Feedback?》在 3 Experimental Setup, Appendix A Experimental Setup Details, Appendix B Additional Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30774:end -->
- 取舍：收益是把 把自然语言反馈收益与重复尝试收益分离，修正交互改进测量。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30774v1 — §Post-training LMs with teacher feedback.; §Shared teacher system prompt.；arXiv:2606.30774v1 — §3 Experimental Setup; §Appendix A Experimental Setup Details; §Appendix B Additional Results；arXiv:2606.30774v1 — §5 Discussion; §Limitations
<!-- review:SF-2026-ARXIV-2606-30774:end -->

<!-- review:SF-2026-ARXIV-2606-30775:start -->
### 2606.30775 — A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization

- 问题：当Enterprise AI agents route user queries to specialized skills by matching queries against natural language skill descriptions.时，现有 AGENT-TOOL-CALLING 合同缺少什么？
- 机制与 owner：以 production routing 错误为反馈重写 skill description，改变技能发现控制环。 唯一 owner 为 AGENT-TOOL-CALLING；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30775:start -->
- 证据与非证明：exact-v1 仅支持《A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization》在 4 Experimental Setup, 5 Results, Appendix C Production train20 Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-TOOL-CALLING 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30775:end -->
- 取舍：收益是把 以 production routing 错误为反馈重写 skill description，改变技能发现控制环。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experimental Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30775v1 — §3 Method; §5.4 Initial training F1 as a diagnostic signal; §Appendix F Production Training F1 Dynamics；arXiv:2606.30775v1 — §4 Experimental Setup; §5 Results; §Appendix C Production train20 Results；arXiv:2606.30775v1 — §6 Conclusion; §Limitations; §Appendix G Iter-0 Training F1 as a Failure Predictor (ToolBench)
<!-- review:SF-2026-ARXIV-2606-30775:end -->

<!-- review:SF-2026-ARXIV-2606-30783:start -->
### 2606.30783 — Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense

- 问题：当We identify a security-fidelity tradeoff in defending LLMs against indirect prompt injection: defenses resist injected instructions largely by suppressing untrusted text, which corrupts tasks that must preserve it, such 时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30783:start -->
- 证据与非证明：exact-v1 仅支持《Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense》在 3 The SecFid Benchmark, 3.4 Evaluation, 4 Experiments 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30783:end -->
- 取舍：收益是把 揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 The SecFid Benchmark 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30783v1 — §3.2 Task Design; §A.2 Probe design; §E.1 Training for instruction-data separation；arXiv:2606.30783v1 — §3 The SecFid Benchmark; §3.4 Evaluation; §4 Experiments；arXiv:2606.30783v1 — §2 Threat Model; §7 Conclusion
<!-- review:SF-2026-ARXIV-2606-30783:end -->

<!-- review:SF-2026-ARXIV-2606-30788:start -->
### 2606.30788 — Revocable Learned State via Process Sidecars

- 问题：当Language models are often adapted in stages: a public skill phase, a private memory phase, and a later safety phase that learns to refuse outputs tied to the remembered entities.时，现有 AGENT-MEMORY 合同缺少什么？
- 机制与 owner：用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。 唯一 owner 为 AGENT-MEMORY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30788:start -->
- 证据与非证明：exact-v1 仅支持《Revocable Learned State via Process Sidecars》在 2 Setting and evaluation, 5 Experiments, 5.1 Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MEMORY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30788:end -->
- 取舍：收益是把 用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2 Setting and evaluation 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30788v1 — §3 Method; §Safety post-training.; §Sensitivity through training.；arXiv:2606.30788v1 — §2 Setting and evaluation; §5 Experiments; §5.1 Setup；arXiv:2606.30788v1 — §6 Discussion and limitations; §7 Conclusion; §B.7 Boundary cases for the second-order frontier
<!-- review:SF-2026-ARXIV-2606-30788:end -->

<!-- review:SF-2026-ARXIV-2606-30789:start -->
### 2606.30789 — Predictable GRPO: A Closed-Form Model of Training Dynamics

- 问题：当We develop a first-principles reduced-order model of these dynamics.时，现有 TRAIN-GRPO 合同缺少什么？
- 机制与 owner：以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。 唯一 owner 为 TRAIN-GRPO；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30789:start -->
- 证据与非证明：exact-v1 仅支持《Predictable GRPO: A Closed-Form Model of Training Dynamics》在 3.1 Setup, 4 Experimental Setup, 4.2 Training Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 TRAIN-GRPO 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30789:end -->
- 取舍：收益是把 以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3.1 Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30789v1 — §Predictable GRPO: A Closed-Form Model of Training Dynamics; §Algorithms and training reports.; §4.2 Training Setup；arXiv:2606.30789v1 — §3.1 Setup; §4 Experimental Setup; §4.2 Training Setup；arXiv:2606.30789v1 — §The boundary tracks the prediction where the linearization holds (Figure 7 ).; §6 Conclusion and Future Work
<!-- review:SF-2026-ARXIV-2606-30789:end -->

<!-- review:SF-2026-ARXIV-2606-30801:start -->
### 2606.30801 — Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale

- 问题：当Personalization algorithms determine what content users encounter on online platforms.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：用可复现 Agent 身份与行为脚本扩展黑盒个性化算法审计。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30801:start -->
- 证据与非证明：exact-v1 仅支持《Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale》在 3 Experiment Design, 4.2 “For You” vs “Following” Feed Analysis, 4.3 Counterfactual Analysis 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30801:end -->
- 取舍：收益是把 用可复现 Agent 身份与行为脚本扩展黑盒个性化算法审计。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 Experiment Design 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30801v1 — §3 Experiment Design；arXiv:2606.30801v1 — §3 Experiment Design; §4.2 “For You” vs “Following” Feed Analysis; §4.3 Counterfactual Analysis；arXiv:2606.30801v1 — §6 Discussion
<!-- review:SF-2026-ARXIV-2606-30801:end -->

<!-- review:SF-2026-ARXIV-2606-30814:start -->
### 2606.30814 — When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs

- 问题：当Calibration evaluates whether a model confidence aligns with its empirical accuracy.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：证明模型准确率差异可反转 calibration 排名，要求 accuracy-controlled 比较。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30814:start -->
- 证据与非证明：exact-v1 仅支持《When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs》在 When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs, 4 ACE: Accuracy-Controlled Evaluation, Setup. 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30814:end -->
- 取舍：收益是把 证明模型准确率差异可反转 calibration 排名，要求 accuracy-controlled 比较。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30814v1 — §Calibration Metrics and Calibration Methods.; §Confidence Elicitation Methods.; §The source of reversal depends strongly on the confidence method.；arXiv:2606.30814v1 — §When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs; §4 ACE: Accuracy-Controlled Evaluation; §Setup.；arXiv:2606.30814v1 — §7 Conclusion; §Limitation
<!-- review:SF-2026-ARXIV-2606-30814:end -->

<!-- review:SF-2026-ARXIV-2606-30850:start -->
### 2606.30850 — BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation

- 问题：当Large language models (LLMs) are typically deployed in multi-turn conversations, where each turn provides new evidence that should reduce epistemic uncertainty about their environment.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把多轮证据到达后的 belief trajectory 与最终答案分开评测。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30850:start -->
- 证据与非证明：exact-v1 仅支持《BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation》在 5.1 Simulation Setup, Appendix F Compute and Inference Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30850:end -->
- 取舍：收益是把 把多轮证据到达后的 belief trajectory 与最终答案分开评测。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 5.1 Simulation Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30850v1 — §4 Bayesian Prediction in Recommender Systems; §B.1.1 System Prompt; §Appendix C Recommender System Details；arXiv:2606.30850v1 — §5.1 Simulation Setup; §Appendix F Compute and Inference Setup；arXiv:2606.30850v1 — §7 Limitations and Conclusion
<!-- review:SF-2026-ARXIV-2606-30850:end -->

<!-- review:SF-2026-ARXIV-2606-30852:start -->
### 2606.30852 — When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models

- 问题：当Reasoning models spend test-time compute unevenly across instances, and a growing family of early-exit rules -- confidence thresholds, entropy monitors, answer-stability checks, and learned stoppers -- promises to reclai时，现有 INFER-DECODE 合同缺少什么？
- 机制与 owner：把 reasoning early exit 的质量、校准和成本放进同一停止合同。 唯一 owner 为 INFER-DECODE；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30852:start -->
- 证据与非证明：exact-v1 仅支持《When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models》在 4 Experiments, 4.1 Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 INFER-DECODE 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30852:end -->
- 取舍：收益是把 把 reasoning early exit 的质量、校准和成本放进同一停止合同。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30852v1 — §Training-free early exit.; §3 Method; §3.3 Training and Metrics；arXiv:2606.30852v1 — §4 Experiments; §4.1 Setup；arXiv:2606.30852v1 — §5 Discussion and Limitations; §7 Conclusion
<!-- review:SF-2026-ARXIV-2606-30852:end -->

<!-- review:SF-2026-ARXIV-2606-30899:start -->
### 2606.30899 — Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models

- 问题：当Backdoor attacks pose a serious threat to large language models (LLMs) by causing otherwise benign systems to produce attacker-specified malicious behavior when a hidden trigger is present.时，现有 PLATFORM-SECURITY 合同缺少什么？
- 机制与 owner：以曲率定位 backdoor 模块并低秩净化，改变全量微调式修复边界。 唯一 owner 为 PLATFORM-SECURITY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30899:start -->
- 证据与非证明：exact-v1 仅支持《Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models》在 IV Experiments, IV-B Evaluation Metrics, IV-C Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-SECURITY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30899:end -->
- 取舍：收益是把 以曲率定位 backdoor 模块并低秩净化，改变全量微调式修复边界。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 IV Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30899v1 — §II Method; §II-A Problem Formulation; §III-B Poisoned Model Training；arXiv:2606.30899v1 — §IV Experiments; §IV-B Evaluation Metrics; §IV-C Main Results；arXiv:2606.30899v1 — §V Discussion
<!-- review:SF-2026-ARXIV-2606-30899:end -->

<!-- review:SF-2026-ARXIV-2606-30911:start -->
### 2606.30911 — Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering

- 问题：当ML engineering agents waste compute rediscovering known techniques because every competition is a cold start.时，现有 AGENT-MEMORY 合同缺少什么？
- 机制与 owner：把跨任务技巧分层积累为可迁移知识，减少 ML Agent 重复探索。 唯一 owner 为 AGENT-MEMORY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30911:start -->
- 证据与非证明：exact-v1 仅支持《Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering》在 4 Experiments, 4.1 Setup, 4.2 Main Results 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 AGENT-MEMORY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30911:end -->
- 取舍：收益是把 把跨任务技巧分层积累为可迁移知识，减少 ML Agent 重复探索。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 4 Experiments 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30911v1 — §Hierarchical organization in agent systems.; §3 Method；arXiv:2606.30911v1 — §4 Experiments; §4.1 Setup; §4.2 Main Results；arXiv:2606.30911v1 — §5 Discussion; §5.3 Limitations; §6 Conclusion
<!-- review:SF-2026-ARXIV-2606-30911:end -->

<!-- review:SF-2026-ARXIV-2606-30919:start -->
### 2606.30919 — Budget-Adaptive Routing: Skipping the Weak When the Strong Answers Anyway

- 问题：当Edge-cloud inference collaborations are often designed with a routing estimator that decides whether to offload each frame from weak models at the edge to stronger models in the cloud.时，现有 PLATFORM-GATEWAY 合同缺少什么？
- 机制与 owner：在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。 唯一 owner 为 PLATFORM-GATEWAY；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30919:start -->
- 证据与非证明：exact-v1 仅支持《Budget-Adaptive Routing: Skipping the Weak When the Strong Answers Anyway》在 1. Introduction, 2. Problem Statement, 2.1. Problem Formulation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-GATEWAY 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30919:end -->
- 取舍：收益是把 在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 1. Introduction 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30919v1 — §2.1. Problem Formulation; §3. Method；arXiv:2606.30919v1 — §1. Introduction; §2. Problem Statement; §2.1. Problem Formulation；arXiv:2606.30919v1 — §6. Conclusion and Future Work
<!-- review:SF-2026-ARXIV-2606-30919:end -->

<!-- review:SF-2026-ARXIV-2606-30931:start -->
### 2606.30931 — RoPoLL: Robust Panel of LLM Judges

- 问题：当The LLM Jury, a Panel of LLM Evaluators (PoLL) reporting consensus scores, has become a practical alternative to single-judge LLM evaluation, yet its statistical behavior remains poorly understood.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-30931:start -->
- 证据与非证明：exact-v1 仅支持《RoPoLL: Robust Panel of LLM Judges》在 3 Problem Setup, 6 Experiments, 6.1 Setup 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-30931:end -->
- 取舍：收益是把 把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 3 Problem Setup 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.30931v1 — §3.1 System Agent and Reward Space; §6.7 Noisy-GT Control: Systematic Bias, Not Imprecision；arXiv:2606.30931v1 — §3 Problem Setup; §6 Experiments; §6.1 Setup；arXiv:2606.30931v1 — §The problem: Byzantine failures, not Gaussian noise.; §7 Conclusion; §Scope and limitations.
<!-- review:SF-2026-ARXIV-2606-30931:end -->

<!-- review:SF-2026-ARXIV-2606-31002:start -->
### 2606.31002 — Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization

- 问题：当Theorem-proving benchmarks evaluate proof search against fixed formal statements, but natural-language-to-Lean formalization must generate the formal statement itself.时，现有 PLATFORM-EVALUATION-SYSTEM 合同缺少什么？
- 机制与 owner：把 NL-to-Lean 的编译通过与语义忠实分层，修正 formalization 验收。 唯一 owner 为 PLATFORM-EVALUATION-SYSTEM；它持有该 family 的状态、证据版本与提交/回退权，相邻章节只消费结果。
<!-- claim:SF-2026-ARXIV-2606-31002:start -->
- 证据与非证明：exact-v1 仅支持《Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization》在 2.2 Evaluation Context, 2.4 Evaluation Protocol, 4 Performance Evaluation 所测设置中的结果；不证明未测模型、硬件、任务分布或生产 SLO，失败时按 PLATFORM-EVALUATION-SYSTEM 的既有保守路径回退。
<!-- claim:SF-2026-ARXIV-2606-31002:end -->
- 取舍：收益是把 把 NL-to-Lean 的编译通过与语义忠实分层，修正 formalization 验收。 变为可验收机制；代价是新增版本、观测或控制状态，并受 exact-v1 评测设置限制。
- failure / fallback：若 2.2 Evaluation Context 的前提、证据或 identity 不满足，则停止自动提交并回到 owner 章节现有保守机制。
- coexistence / evolution：旧路径在低风险、低异构或证据不足区间继续存在；新路径只在其测量和身份条件满足时接管。
- exact-v1 locator：arXiv:2606.31002v1 — §5.1 Factorial Design over (T,F,S)；arXiv:2606.31002v1 — §2.2 Evaluation Context; §2.4 Evaluation Protocol; §4 Performance Evaluation；arXiv:2606.31002v1 — §6 Limitations; §7 Conclusion
<!-- review:SF-2026-ARXIV-2606-31002:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29685 | CAREBench: A Child-Safety Risk Benchmark for Language Models — CAREBench provides a responsibly scoped evaluation for LLM developers to identify and close gaps in child safety policies. | We evaluate seven frontier LLM APIs: Claude Opus 4.6, Claude Fable 5, Gemini 3.1 Pro, GPT-5.4, GPT-5.5, Grok 4.1 Fast Reasoning, and Kimi K2 Thinking on CAREBench. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29699 | Early Warning Signals for OpenVLA Failure under Visual Distribution Shift — Because fitting and evaluation share tasks, resets, and seed, these results establish retrospective separability rather than prediction on independent episodes. | We evaluate OpenVLA on LIBERO 10 tasks Kim et al. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The activation hook reads the input to mlp.down_proj ; if the tensor has shape batch by sequence by width, the code takes batch index 0 0 and averages over sequence positions. | Not Disclosed | Not Disclosed | Appendix A.1 and Appendix A.2 give the remaining implementation and metric details. |
| SF-2026-ARXIV-2606-29700 | Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback — Code and data are available at: https://github.com/ibasicplan/NL-PDDL-Bench | For Llama3.1-8B and Qwen3-8B, SFT already yields large improvements in solvability and plan-level agreement, showing that supervised learning effectively captures the core NL-to-PDDL mapping. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We report executability metrics and plan-level alignment against planner-derived references, and analyze three aspects: comparison with direct action-sequence generation, attribution across training and repair settings, and robustness under difficulty scaling and cross-domain variation. |
| SF-2026-ARXIV-2606-29708 | Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving — Cross-vendor and interconnect-related claims are stated as design guidance grounded in industrial deployment observations and source-code inspection of the runtimes involved. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29713 | SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution — 69.8 F1) while producing substantially richer, auditable output -- confirming a principle that should generalize: for any RL task with multi-component generation, reward granularity must match output granularity. | (2025) : MiniCheck-7B (81.2 F1), ClearCheck-8B ( ∼ \sim 84 F1), and Llama-3.1-8B zero-shot (67.2 F1). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Having laid out the architecture (§ 2.2 ), the reward (§ 2.3 ), and the self-evolution loop (§ 2.5 ), we now stress-test Seva on four axes that any deployed verifier must clear: accuracy against established binary baselines, generalization across benchmarks with different failure modes, structural reliability of the produced output, and training dynamics under both reward designs. |
| SF-2026-ARXIV-2606-29718 | Diagnosing and Mitigating Context Rot in Long-horizon Search — For parallel sampling, we develop a behavior-aware filtering strategy and observe a performance gain of 2.6% to 4.9% across three aggregation methods. | We include four open-source 1 1 1 We exclude closed-source models like GPT-5.4 or Claude Opus 4.7 as they usually encrypt the reasoning content within the trajectory, making the analysis infeasible. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | As shown in Figure 2 , as the trajectory length increases, model accuracy drops sharply. |
| SF-2026-ARXIV-2606-29719 | A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents — The finding is not any single coupling magnitude but the pattern of version-conditional instability that makes single-snapshot evaluator studies unreliable. | Executor : DeepSeek-chat (text-only; T = 0.7 T{=}0.7 ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29745 | ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit — In the Clue Selector Game, a novel controlled evidence-seeking benchmark, we show that ECHO substantially improves resolution, information gain, and efficiency over trajectory-level GRPO, and matches or exceeds frontier baselines on epistemic metrics such as grounding, recovery, and calibration while producing almost no visible reasoning text. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our metrics test whether a policy uses accumulated evidence to choose useful actions throughout the trajectory, rather than merely succeeding at the end or producing more reasoning text. |
| SF-2026-ARXIV-2606-29758 | PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF — Experiments on mathematical reasoning and RLHF benchmarks show that PS-PPO achieves large reductions in training compute and peak GPU memory, while maintaining accuracy comparable to strong critic-free baselines. | For training on mathematical reasoning, we train on MATH ( Hendrycks et al., 2021 ) , excluding Level 1 and Level 2 problems, and use Llama-3.1-8B-Instruct 1 1 1 https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct and Qwen2.5-Math-7B 2 2 2 https://huggingface.co/Qwen/Qwen2.5-Math-7B ( Yang et al., 2024 ) as backbone models. | For mathematical reasoning experiments, we trained the 7B-scale models on 8 NVIDIA A100 GPUs. | Not Disclosed | For evaluation across all benchmarks, we used a maximum sequence length of 4096 tokens and reported zero-shot pass@1 accuracy. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Prompts are designed to elicit step-by-step derivations via an explicit instruction, and we optimize the policy with a binary reward based on final-answer correctness. |
| SF-2026-ARXIV-2606-29775 | SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling — Finally, extensive experiments show that SMART-MIG improves the energy-tardiness efficiency by $18\%$ compared to its corresponding static-partitioning counterpart, while being only $27\%$ above the theoretical lower bound on energy consumption. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Since deadline information is not generally available in data center traces, we model it as d j ∼ U ​ n ​ i ​ f ​ ( 1 , 1.5 ) ∗ p j , 7 d_{j}\sim Unif(1,1.5)*p_{j,7} , which is similar to the deadline distribution in [ 30 ] . | Evaluated with the E ​ T ET metric, SMART-MIG delivers overall gains of 18 % 18\% and 32 % 32\% relative to CEDF and EDF, respectively. |
| SF-2026-ARXIV-2606-29778 | Mandol: An Agglomerative Agent Memory System for Long-Term Conversations — For performance comparison, Mandol also obtains a 5.4x retrieval speedup and a 4.8x insertion speedup under 10 QPS concurrent load, while still maintaining low latency on consumer-grade hardware. | On LoCoMo, Mandol improves the strongest baseline by 3.35 percentage points under GPT-4o-mini and by 0.24 percentage points under GPT-4.1-mini, reaching 89.48% and 92.21% overall accuracy, respectively. | Third, we study Mandol’s resource utilization, including system RAM and GPU memory consumption. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | P99 and P90 denote the 99th- and 90th-percentile latency, which characterize tail latency under concurrent requests. | Second, we compare system performance by measuring the latency of Search and Add operations, covering both memory retrieval and memory insertion. | First, we compare Mandol with existing memory systems in terms of retrieval accuracy and token consumption. |
| SF-2026-ARXIV-2606-29784 | HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data — We establish conditions under which the bias and variance reductions hold, showcase HERO's performance in simulation studies, and demonstrate its effectiveness on real-world model evaluation benchmarking datasets. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The inter-rater reliability literature consistently finds variation in annotator accuracy across domains from medical imaging [ 24 , 18 ] to natural language processing [ 21 ] , even under shared guide |
| SF-2026-ARXIV-2606-29788 | MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory — Dual-annotator human validation (kappa = 0.88) confirms judge reliability. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This section describes the implementation of each evaluated system, the judge pipeline, and the image generation process. |
| SF-2026-ARXIV-2606-29871 | AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes — These results suggest that schema-conditioned LLMs can serve as bounded supervisory managers for live training runs, complementing conventional optimizers and schedulers with interpretable, multi-axis intervention capabilities | All TinyStories experiments use a small GPT-style autoregressive Transformer with 6 layers, 6 attention heads, embedding dimension 384, and context length 256. | Not Disclosed | Not Disclosed | All TinyStories experiments use a small GPT-style autoregressive Transformer with 6 layers, 6 attention heads, embedding dimension 384, and context length 256. | Not Disclosed | Training runs for 10k steps with evaluation every 500 steps, batch size 16, gradient accumulation 2, AdamW, and gradient clipping at 1.0. | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-29887 | SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing — These results highlight the limitations of current guardrails and call for stronger in-context policy guardrails that can reliably execute policies, resolve rule dependencies, and adapt to novel policy frameworks. | Construction and validation use four LLMs: Grok-4.1 [ 40 ] , GPT-5.4 [ 32 ] , Gemini-3.1-Pro [ 16 ] , and Claude-Opus-4.6 [ 1 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We use two metrics for evaluation: rule matching rate (RMR) and rule disagreement rate (RDR). |
| SF-2026-ARXIV-2606-29914 | MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation — We recommend memory evaluations fix embedding models across comparisons, stratify by model family, and report write-path cost before attributing gains to architecture. | Four findings emerge: (1) verbatim RAG matches full-context GPT-4o-mini (47.2% vs. | Not Disclosed | Not Disclosed | “Needle-in-a-haystack” evaluations show that shorter, more specific facts are harder for LLMs to locate than longer passages, independent of overall context length, a phenomenon termed “gold context size” sensitivity [ Bianchi et al., 2026 ] , and semantic needle studies show that surrounding text coherence modulates a model’s ability to attend to target information [ Aksoy et al., 2026 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 49.8%, p = 0.34 p\!=\!0.34 ), but the ranking reverses across models: Gemini gains + 14 +14 pp from full context, while Sonnet gains + 31 +31 pp from RAG, partly because it refuses 63% of full-context queries; (2) swapping only the embedding model in an identical pipeline shifts accuracy by + 6.2 +6.2 pp at n = 500 n\!=\!500 ( p = 0.004 p\!=\!0.004 ), and Mem0 beats MiniLM-RAG by + 11 +11 pp but loses to cloud-RAG by 1.2pp, so one variable flips the conclusion; (3) agent self-memory (42%) underperforms basic retrie |
| SF-2026-ARXIV-2606-29920 | Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios? — We have released our dataset and code to facilitate future research: https://github.com/THU-KEG/RuVerBench. | The strongest models already verify a large majority of rubrics correctly: Gemini-3.1 Pro Preview reaches 94.7 94.7 in Deep Research, and GPT-5.4 reaches 89.4 89.4 in Agentic Coding. | Not Disclosed | Not Disclosed | Not Disclosed | In terms of output length, research answers in Deep Research average 7.1 7.1 K tokens, while coding-agent trajectories in Agentic Coding average 49.4 49.4 K tokens. | Not Disclosed | Not Disclosed | Not Disclosed | Consequently, explicit rubrics have become standard in agentic pipelines for both reinforcement learning (RL) rewards ( Bai et al., 2022 ; Lee et al., 2023 ; Yuan et al., 2024 ) and benchmark evaluations ( Xu et al., 2025 ; Sharma et al., 2025 ; Li et al., 2026 ; Ding et al., 2026 ) . |
| SF-2026-ARXIV-2606-29955 | SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows — Project page: https://spreadsheetbench.github.io/ | (2026) , Qwen3.5-397B-A17B Team (2026) , and DeepSeek-V3.2 Liu et al. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Spreadsheet Execution Metrics. |
| SF-2026-ARXIV-2606-29957 | SWE-Together: Evaluating Coding Agents in Interactive User Sessions — Experiments with frontier coding agents show that stronger agents generally achieve higher final success rates while requiring fewer interventions, suggesting an improved user experience. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Each final patch receives a score in [ 0 , 1 ] [0,1] from the agentic judge against the task’s frozen rubric from Section 2.3.1 . |
| SF-2026-ARXIV-2606-29959 | Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented Generation — These results support a nuanced view of adaptive RAG: calibrated confidence is best understood as a reusable interface for allocating retrieval budget under task and system constraints. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Accuracy is answer correctness under the selected action. |
| SF-2026-ARXIV-2606-29975 | Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets — The results indicate that serving complete molecule records, rather than field chunks or reconstructed objects, improves shuffled training throughput while keeping artifacts compact enough for public distribution. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Unless otherwise noted, the reported read-throughput, write-throughput, and storage-footprint results use uncompressed Atompack and LMDB payloads ( codec=none ). | Not Disclosed |
| SF-2026-ARXIV-2606-29982 | Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference — Evaluations on the 671B DeepSeek-R1 model show that CAEE can reduce end-to-end inference latency by 8\%-18\% across diverse deployment settings, including expert offloading and on-device execution on multi-device systems, while maintaining a model accuracy drop of less than 1\%. | We employ DeepSeek-R1 671B [ 10 ] with W8 quantization as our representative MoE model. | Not Disclosed | We employ DeepSeek-R1 671B [ 10 ] with W8 quantization as our representative MoE model. | Not Disclosed | For inference performance, we measure Time to First Token (TTFT) and Time Per Output Token (TPOT) under fixed concurrency, while adjusting the per-device concurrency according to each deployment scenario. | Not Disclosed | For inference performance, we measure Time to First Token (TTFT) and Time Per Output Token (TPOT) under fixed concurrency, while adjusting the per-device concurrency according to each deployment scenario. | For inference performance, we measure Time to First Token (TTFT) and Time Per Output Token (TPOT) under fixed concurrency, while adjusting the per-device concurrency according to each deployment scenario. | To evaluate the impact of CAEE on model accuracy, we employ multiple open-source benchmarks across three domains: Knowledge (MMLU-shot5 [ 17 ] , CEval-shot5 [ 19 ] ), Math (GSM8K-shot5 [ 7 ] ), and Code (HumanEval [ 5 ] ). |
| SF-2026-ARXIV-2606-29986 | HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators — Across four Qwen3 models (4B--32B) and three production traces, HMA-Serve delivers up to $3.2\times$ higher goodput than state-of-the-art memory-homogeneous methods and $4.8\times$ higher goodput-per-dollar, with no measurable loss on generation-quality benchmarks. | Not Disclosed | We evaluate every system on real silicon: NVIDIA A100-80GB on the HBM side, a four-chip Tenstorrent Blackhole p150 mesh (TT × \times 4) on the GDDR side, over a 100 Gb RoCE fabric, all serving through vLLM 0.19.1 ( Kwon et al., 2023 ) . | HMA-Serve (ours) runs BFP8 prefill on TT × \times 4 and BF16 decode on one A100, mapping each model’s prefill onto the mesh with the data-/tensor-parallel layout of Table 2 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We calibrate the relative SLOs to its no-load latency. | Metric. |
| SF-2026-ARXIV-2606-30005 | LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception — Gains grow with context pressure and transfer across backbones, while ablations confirm that the dashboard matters beyond archive and recovery tools. | For BrowseComp-Plus, we evaluate deep-research retrieval with DeepSeek-V4-Pro on an N = 150 N{=}150 subset and report judged Pass@1 with one sampled answer. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate 75 task configurations; unless otherwise stated, accuracy is solved tasks over all 75, with errors and timeouts counted as failures. |
| SF-2026-ARXIV-2606-30107 | Structural Certification for Reliable Physical Design with Language Models — Across eighty adversarial trials spanning two models, two decoding temperatures, and a deliberately faulted engine, this contract produced zero false certifications. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30119 | On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting — Our analysis reveals three main findings: (i) some Web Agents were able to bypass all evaluated anti-bot mechanisms; (ii) all evaluated Web Agents can be distinguished both from humans and from one another using multi-layer fingerprinting techniques across network, HTTP and browser layers; (iii) stealth and anti-detection mechanisms often increase detectability rather than decrease it. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluated our classifiers using Accuracy, Precision, Recall, and F 1 F_{1} -scores. |
| SF-2026-ARXIV-2606-30185 | Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents — Against task-specific RL (VTool-R1, DeepEyes), Dynamo closes 65--99% of the RL gap at a fraction of the compute, and combines additively with RL when available. | The largest gains are on o4-mini / V ∗ ( + 14.1 +14.1 ), o4-mini / HRBench4K ( + 12.7 +12.7 ), GPT-5.4 / HRBench4K ( + 10.7 +10.7 ), Doubao-Seed-2.0 / V ∗ ( + 8.8 +8.8 ), and Qwen3.5-27B / HRBench4K ( + 8.4 +8.4 ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For the evolution-from-scratch setting (Exp I) we use four visual reasoning benchmarks: ChartQA ( Masry et al., 2022 ) (multi-step numerical reasoning over charts; 2,500 test questions), MathVista ( Lu et al., 2024 ) (math reasoning in figures and plots; 1,000 testmini questions), HRBench4K ( Wang et al., 2025 ) (perception on 4K-resolution images; 800 questions), and V ∗ ( Wu & Xie, 2024 ) (visual search for an object’s property; 191 questions); the first two stress cognitive bottlenecks while the latter two stres |
| SF-2026-ARXIV-2606-30251 | TACO: Tool-Augmented Credit Optimization for Agentic Tool Use — Extensive experiments across perception, reasoning, and general multimodal benchmarks show that it yields consistent accuracy gains and learns to invoke its tools only when they help. | Following Thyme, we build on Qwen2.5-VL-7B ( Bai et al. | Training runs on a single node of 8 × 8{\times} 80 GB A100 GPUs. | Not Disclosed | Not Disclosed | The prompt template specifies the <think> , <code> , <answer> , and sandbox-output tokens. | 3.3 ), use no KL penalty ( β = 0 \beta{=}0 ), and sample G = 8 G{=}8 rollouts per prompt at temperature 1.0 1.0 , with a total batch size of 128 128 and learning rate 1 × 10 − 6 1{\times}10^{-6} . | Not Disclosed | Not Disclosed | 2024 ) ), reporting per-benchmark accuracy and the macro-average. |
| SF-2026-ARXIV-2606-30263 | Defending Against Harmful Supervision Hidden in Benign Samples — To address this, we propose Dual-Reference SFT (DR-SFT), which adapts DPO-style contrastive objective design to SFT through token-level regularization, mitigating harmful fine-tuning beyond coarse data filtering. | In this section, we present numerical experiments conducted on several open-source large language models (LLMs), including Llama-2-7B-Chat Touvron et al. | In this work, we use single 4 × \times A100-80GB GPUs or 4 × \times H200-141GB GPUs for all experiments, with up to 16 CPU cores and 256GB memory. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We report the attack success rate (ASR; lower is better) for safety tasks and the utility score (higher is better) for downstream tasks. |
| SF-2026-ARXIV-2606-30265 | When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding — These results complement existing distribution-preserving analyses of speculative decoding by characterizing the deterministic local acceptance events common in practical inference systems. | We estimate the target model distributions of Qwen/Qwen3-1.7B and Qwen/Qwen3-4B models ( Yang et al., 2025 ) . | Not Disclosed | Not Disclosed | We choose 500 random prompts with at least 64 prompt tokens. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30338 | Sequential Fairness Auditing with Limited Output Access — This work provides a practical statistical framework for sequential fairness auditing under realistic deployment constraints. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Most existing approaches operate in batch settings with fixed datasets and point null hypotheses. | Not Disclosed | Not Disclosed | Prior work studies algorithmic fairness through statistical disparity metrics that compare predictive behavior across demographic groups. |
| SF-2026-ARXIV-2606-30373 | Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs — We have responsibly disclosed all findings to the affected platforms and developers. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30383 | Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents — (Lesson) Both mechanisms only move along a common leak/over-refusal trade-off rather than crossing it: improving one axis costs the other, and the jointly favorable outcome stays out of reach. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30389 | Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding — Github: https://github.com/Tianyu9748/Incremental_FlashAttention | (2024) , GLM-Z1-9B (2024) , DeepSeek-R1-8B DeepSeek-AI (2025) , Llama3-8B-1M AI@Meta (2024) , Qwen3-14B Team (2025) , and Qwen3-32B Team (2025) . | Experiments are run on H100 GPUs with CUDA 12.8, with a tensor parallelism degree of 2. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We measure end-to-end decoding latency across all models and benchmarks, and report the speedup of PRR over the standard DSA execution in Table 1 . | Not Disclosed |
| SF-2026-ARXIV-2606-30391 | Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs — Comparison with four SOTA LLM serving systems and one DVFS-augmented system demonstrates that Festina reduces energy consumption by up to 56% while maintaining parity in SLO attainment (within a 2% margin) | We also confirm that substantial SLO slack also appears for larger, multi-GPU deployments (e.g., a 70B Llama2 model) in § B . | We utilize pyNVML ( PyPI Contributors, ) to adjust GPU frequency with minimal runtime overhead. | Not Disclosed | To stress-test Festina under prefill-heavy and decode-heavy scenarios, we also use two variants from Aegaeon ( Xiang et al., 2025a ) : ShareGPT-ix2 (2 × \times input length) and ShareGPT-ox2 (2 × \times output length). | To stress-test Festina under prefill-heavy and decode-heavy scenarios, we also use two variants from Aegaeon ( Xiang et al., 2025a ) : ShareGPT-ix2 (2 × \times input length) and ShareGPT-ox2 (2 × \times output length). | Not Disclosed | The scheduler is built using Python’s asyncio ( Python Software Foundation, ) library to enable high-concurrency instance orchestration. | We run experiments to answer the following questions: (1): How does Festina balance SLO attainment with energy efficiency compared to SOTA serverless LLM systems? | Not Disclosed |
| SF-2026-ARXIV-2606-30449 | Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring — Code is released at https://github.com/maxf-zn/misalignment_monitoring | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30531 | Entity Binding Failures in Tool-Augmented Agents — These findings show that safe tool use requires not only selecting the correct tool, but also reliably binding natural-language references to the correct real-world entity before action. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30534 | Orca: The World is in Your Mind — Finally, we discuss the current limitations, aiming to provide useful insights and inspiration for the community. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The PRM-as-a-Judge results are used in the main-text analysis, while this appendix provides the detailed task-level rule-based evaluation protocol and results. |
| SF-2026-ARXIV-2606-30546 | MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems — Together, these components enable intent-based validation, principled system evolution, and a seamless transition to production-grade MAS. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Execution traces and metrics are interpreted relative to explicit MAS contracts, enabling semantic conformance checking, principled analysis of design changes, and preservation of evidence across development, validation, and production. |
| SF-2026-ARXIV-2606-30560 | TraceLab: Characterizing Coding Agent Workloads for LLM Serving — We release the dataset, trace collection pipeline, and analysis code at https://github.com/uw-syfi/TraceLab.git the project website is https://tracelab.cs.washington.edu. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing benchmarks for coding agents, such as Terminal-Bench [ 51 ] and SWE-bench [ 30 ] , consist of realistic programming tasks but are built for a different goal: evaluating model accuracy on isolated tasks. |
| SF-2026-ARXIV-2606-30562 | Morphing into Hybrid Attention Models — Extensive experiments show that FlashMorph discovers more effective hybrid configurations, preserves strong long-context recall and general benchmark performance while substantially reducing layer selection cost compared with existing layer selection methods, demonstrating its effectiveness, efficiency, and scalability. | We use Qwen3-0.6B and Qwen3-1.7B as the pretrained full-attention Transformer backbones. | We evaluate the inference efficiency of FlashMorph (linear:full=3:1 hybrid attention) and Qwen3 (purely full attention) based on 1.7B backbone on single GPU. | Not Disclosed | For prefilling, we vary the input length from 4K to 1M tokens. | Not Disclosed | 2 , we report both latency time and peak GPU memory usage under increasing sequence lengths for prefilling and decoding, with a fixed batch size of 1. | Not Disclosed | 2 , we report both latency time and peak GPU memory usage under increasing sequence lengths for prefilling and decoding, with a fixed batch size of 1. | On the 0.6B backbone, FlashMorph achieves near-perfect accuracy on NIAH-Single-1 and delivers strong performance on the more challenging NIAH-Single-2 and NIAH-Single-3 settings, particularly at short and medium context lengths. |
| SF-2026-ARXIV-2606-30566 | Forensic Trajectory Signatures for Agent Memory Poisoning Detection — A prefix-only variant achieves AUC = 0.934, enabling real-time triage. | Beyond the N = 20 N{=}20 GPT-4.1 probe, we applied the classifier (trained exclusively on open-source data) to 405 attack sessions and 560 non-attack sessions across frontier models from separate experiments. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Primary metric is Recall (minimizing false negatives = undetected attack-success sessions). |
| SF-2026-ARXIV-2606-30573 | SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions — Overall, SWE-Interact measures an orthogonal, real-world capability axis for frontier model development: interactive goal discovery and iterative refinement with a user in the loop. | The strongest models in our evaluation, including Opus 4.8 and GPT 5.5, start strong even in the face | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30602 | MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems — Overall, our results show that edge-level risk in MAS is often concentrated and predictable, allowing proactive hardening of multi-agent infrastructures. | The strongest result appears for Gemma4-E4B , where Mesa combined {}_{\text{combined}} reaches ρ = + 0.440 \rho=+0.440 with p < 0.01 p<0.01 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | With our Mesa metric, we now have a method for quantifying vulnerability in MAS. |
| SF-2026-ARXIV-2606-30616 | Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent — We hope this work provides the community with a practical path for scaling the horizon using a 35B agent that can reach or match the performance of 1T models on long-horizon tasks. | † For τ 2 \tau^{2} -Bench, we report both the official Qwen3.5-35B-A3B result (81.2) and our reproduced result (33.0); see Section 5.2.1 for discussion. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We cap each task at 300 turns and report pass@1 as the primary metric. |
| SF-2026-ARXIV-2606-30627 | Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models — Our results suggest that the field needs \emph{calibrated}, not \emph{maximal}, conservatism. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A complete benchmark reproducing our findings should report the following metrics in addition to task performance: Goodhart gap time series 𝒢 ⁡ ( t , β ) \mathcal{G}(t;\beta) at a minimum of ⌈ T / 50 ⌉ \lceil T/50\rceil evaluation points. |
| SF-2026-ARXIV-2606-30634 | One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining — Extensive evaluation on models up to 10B parameters confirms that our strategies bridge the performance gap with synchronous training, highlighting the practical potential of asynchronous pipeline parallelism at scale. | The model uses a Qwen3-Next-like architecture ( QwenTeam, 2025 ) with Gated Delta Net layers ( Yang et al., 2024 ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To keep the global batch size close to the optimum as the training horizon increases, we scale it according to B ∝ D 0.58 B\propto D^{0.58} following Li et al. | Not Disclosed | This question is particularly important because the throughput benefits of Async PP are most relevant in large distributed training regimes, where pipeline bubbles translate into substantial wasted accelerator time (see Section F.2 ). | Not Disclosed |
| SF-2026-ARXIV-2606-30639 | Self-Evolving World Models for LLM Agent Planning — Extensive experiments show that WorldEvolver achieves the highest prediction accuracy across three backbones and leads other world model baselines on downstream agent success rate, demonstrating that test-time memory revision enhances both predictive fidelity and planning performance. | (3) Cosine Similarity measures semantic similarity using Qwen3-Embedding-8B ( Zhang et al., 2025b ) embeddings in the same retrieval space. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Prediction metrics measure whether the world model matches the next observation; planning metrics measure whether the exposed signal helps the agent complete tasks. |
| SF-2026-ARXIV-2606-30697 | LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents — These results suggest a path toward AI-native operating systems and machine-readable interaction layers. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | First, vision versus semantic grounding should compare a screenshot+OCR+LLM pipeline against a LUMOS blueprint+LLM pipeline on identical tasks, measuring task success, latency, token count, observation size, and number of recovery turns. | Not Disclosed |
| SF-2026-ARXIV-2606-30704 | From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators — Across benchmarks in question answering, code generation, and mathematical reasoning, MetaFlow achieves performance comparable to state-of-the-art baselines on in-domain tasks with single inference, while demonstrating remarkable zero-shot generalization capabilities on out-of-domain tasks and operator sets. | The Planner Qwen3-8B uses base operators { Generate , Summarize , Revise , Ensemble } with dynamic prompt rewriting, plus novel operators { Decompose , Programmer } for OOD testing (natural language descriptions provided at inference). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | All methods use GPT-4o-mini-0718 as executor and judge. |
| SF-2026-ARXIV-2606-30774 | What Drives Interactive Improvement from Feedback? — We release our controlled student-teacher evaluation framework at https://j-lojek.github.io/feedback-generation-is-a-bottleneck/. | Subsequent sections focus on specific ablation studies and deeper mechanistic insights, In them we are using gemma 4 dense matrices. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | They do it for all types of our metrices we used: accuracy, cumulative accuracy, and performance gains. |
| SF-2026-ARXIV-2606-30775 | A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization — We identify a diagnostic (a large train-validation F1 gap) that flags the latter cases for architectural rather than text-level intervention. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Table 10 reports per-skill F1 for the train20-standard run. |
| SF-2026-ARXIV-2606-30783 | Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense — Security alone therefore measures only half of robustness, and reporting it without fidelity hides the price at which it was bought. | The closed API suite includes Claude Haiku 4.5, Claude Sonnet 4.6, Claude Opus 4.6, Gemini 3.1 Flash-Lite, Gemini 3 Flash, GPT-5.4 Nano, GPT-5.4 Mini, and GPT-5.4. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Macro-F1 𝜿 \kappa Embedding similarity 0.899 0.886 0.832 BLEU 0.879 0.849 0.792 GPT-5.4 judge 0.778 0.729 0.599 (b) Embedding evaluator confusion matrix Pred. |
| SF-2026-ARXIV-2606-30788 | Revocable Learned State via Process Sidecars — Across three models, the validation-selected 2D edit improves held-out refusal closure over naive task arithmetic in all trials, and over the $γ=λ$ process-JVP subfamily, the diagonal slice of the cached 2D grid, in all paired trials. | We evaluate on Qwen-2.5-0.5B-Instruct, Qwen-2.5-1.5B-Instruct [ Qwen Team, 2024a , Qwen Team, 2024b , Qwen Team, 2024c ] , and Llama-3.2-1B-Instruct [ Meta AI, 2024 , Grattafiori et al., 2024 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30789 | Predictable GRPO: A Closed-Form Model of Training Dynamics — Across three models and two group sizes, the closed-form trajectory fits training reward to $R^2 \geq 0.91$ and the mean trajectory is group-size invariant to leading order -- on both the reward curve and out-of-distribution transfer to eight math benchmarks -- while the within-group reward spread retains a residual $G$-dependence that the leading-order temperature picture does not capture. | Gains are largest on benchmarks closest to GSM8K: Nemotron-4B more than doubles its GSM-Plus pass@1 (9.11 to 20.32 at G = 16 G=16 ), and DeepSeek-7B improves GSM-Plus pass@1 by roughly fifteen points (25.64 to 40.25 at G = 4 G=4 ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For a prompt q q , GRPO samples a group of G G completions { o i } i = 1 G ∼ π θ old ( ⋅ ∣ q ) \{o_{i}\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid q) , scores them with a reward r i = R ⁡ ( q , o i ) r_{i}=R(q,o_{i}) , and forms the group-relative advantage The (unclipped) objective, with KL anchoring weight β > 0 \beta>0 to a reference policy π ref \pi_{\mathrm{ref}} , is Parameters are updated by stochastic ascent with learning rate η \eta and momentum coefficient μ ∈ [ 0 , 1 ) \mu\in[0,1) (the role play |
| SF-2026-ARXIV-2606-30801 | Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale — Our work establishes GenAI-based agents as a new tool for algorithmic auditing. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30814 | When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs — Our results show that raw global calibration metrics are not robust for cross-model comparison, and that fair calibration comparison requires accuracy-aware evaluation. | Across five benchmarks spanning knowledge-based (TriviaQA, FreshQA) and reasoning-based tasks (MMLU-Pro, GPQA, LiveBench), we compare the ECE gap against the accuracy gap between stronger models and weaker models, covering both scale-based pairs (Qwen2.5 7B vs. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Calibration evaluates whether a model’s confidence aligns with its empirical accuracy. |
| SF-2026-ARXIV-2606-30850 | BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation — However, these gains do not reliably carry over to downstream prediction, exposing a gap between inferring latent structure and using it to rationally update beliefs about the target outcome. | Not Disclosed | Each model is sharded across NVIDIA A100 (40 GB) GPUs by tensor parallelism; the per-model GPU allocation is listed in Table 8 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30852 | When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models — Together, these results replace the single-method race with a decision procedure for choosing a stopping rule from the trajectory structure and serving regime of the target workload. | The primary models are Qwen3-8B and Qwen3-32B. | Not Disclosed | Not Disclosed | The main budget grid is [ 0,128,192,256,384 , 512 , 640 , 768 , 1024 , 1536 ] [0,128,192,256,384,512,640,768,1024,1536] ; AIME uses a longer grid up to 6144 tokens. | Not Disclosed | Not Disclosed | Not Disclosed | The default answer cap is 48 tokens; all latency profiles that vary checkpoint count include checkpoint probe-answer generation under this cap. | Not Disclosed |
| SF-2026-ARXIV-2606-30899 | Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models — These findings suggest that backdoor removal in LLMs can be formulated as a localized structural repair problem rather than only a broad behavioral alignment problem. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate detoxification using two complementary metrics: one measuring backdoor suppression and one measuring preservation of benign generation behavior. |
| SF-2026-ARXIV-2606-30911 | Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering — These results suggest that better knowledge organization can partly substitute for model strength and compute budget in ML-engineering agents. | Each competition runs Claude Sonnet 4.6 via the CLI backend on a SLURM node with 24 CPUs, 128 GB RAM, and 1 NVIDIA L40S 48 GB GPU. | Each competition runs Claude Sonnet 4.6 via the CLI backend on a SLURM node with 24 CPUs, 128 GB RAM, and 1 NVIDIA L40S 48 GB GPU. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The search space is unbounded Python code; evaluation uses the official Kaggle metric per competition, scored against held-out test sets via the MLE-Bench grader. |
| SF-2026-ARXIV-2606-30919 | Budget-Adaptive Routing: Skipping the Weak When the Strong Answers Anyway — Artifacts are available at https://github.com/ViGeng/bgt-ada | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-30931 | RoPoLL: Robust Panel of LLM Judges — A 3-judge RoPoLL committee at 38B beats Mistral-Large-3 (675B) by 1.31x on HelpSteer-2 under 30% bimodal-random corruption, an 18x parameter advantage at better accuracy; a Noisy-GT control confirms the premium is paid against biased contamination, not benign imprecision. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | (2024) ) and the coordinate-wise Median on three reward-model benchmarks under a per-case corruption pipeline that exposes the corruption-type dependence predicted by Theorem 1 and Example 1 . |
| SF-2026-ARXIV-2606-31002 | Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization — Elaboration feedback is the largest validity intervention, but it also exposes a larger compile-pass semantic-failure bucket; search mainly improves grounding and selectivity; and fine-tuned drafting is largely substitutable in this tool stack once feedback and grounding are available. | (2023) ; recent formal reasoning models such as DeepSeek-Prover, Kimina-Prover, and Goedel-Prover report progress largely through proof-generation success on supplied formal Lean statements Ren et al. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To evaluate generated statements, we adopt a two-stage Consensus LLM-as-Judge protocol. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29685 | score_7_9 | not_selected | — | — | 未入选：把儿童安全从显式伤害响应前移为上游风险识别，并要求按风险层级验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29685 |
| SF-2026-ARXIV-2606-29699 | score_7_9 | not_selected | — | — | 未入选：证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。 该变化由 PLATFORM-MONITORING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29699 |
| SF-2026-ARXIV-2606-29700 | score_7_9 | not_selected | — | — | 未入选：把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。 该变化由 AGENT-PLANNING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29700 |
| SF-2026-ARXIV-2606-29708 | score_7_9 | selected | DA-20260630-HETERO-PD-BOUNDARY | — | 入选：把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。 | analysis:DA-20260630-HETERO-PD-BOUNDARY |
| SF-2026-ARXIV-2606-29713 | score_7_9 | not_selected | — | — | 未入选：把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。 该变化由 AGENT-REFLECTION 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29713 |
| SF-2026-ARXIV-2606-29718 | score_7_9 | not_selected | — | — | 未入选：把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。 该变化由 AGENT-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29718 |
| SF-2026-ARXIV-2606-29719 | score_7_9 | not_selected | — | — | 未入选：把 evaluator 漂移和偏好坍缩作为持续评测系统的测量状态。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29719 |
| SF-2026-ARXIV-2606-29745 | score_7_9 | not_selected | — | — | 未入选：以显式 belief state 和逐轮 epistemic credit 控制信息获取与停止动作。 该变化由 AGENT-PLANNING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29745 |
| SF-2026-ARXIV-2606-29758 | score_7_9 | not_selected | — | — | 未入选：以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29758 |
| SF-2026-ARXIV-2606-29775 | score_7_9 | not_selected | — | — | 未入选：把 MIG 切分、性能与能耗纳入可学习的集群调度状态。 该变化由 PLATFORM-GPU-SCHEDULER 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29775 |
| SF-2026-ARXIV-2606-29778 | score_7_9 | not_selected | — | — | 未入选：以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29778 |
| SF-2026-ARXIV-2606-29784 | score_7_9 | not_selected | — | — | 未入选：用历史 noisy labels 提高生成模型评测灵敏度，同时保留专家标签边界。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29784 |
| SF-2026-ARXIV-2606-29788 | score_7_9 | not_selected | — | — | 未入选：证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29788 |
| SF-2026-ARXIV-2606-29871 | score_7_9 | not_selected | — | — | 未入选：把训练 recipe 的观测、建议、边界检查和执行组织成受限闭环控制面。 该变化由 PLATFORM-TRAINING-OPERATOR 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29871 |
| SF-2026-ARXIV-2606-29887 | score_7_9 | not_selected | — | — | 未入选：把应用自定义政策的层级冲突与多轮上下文纳入 guardrail 验收。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29887 |
| SF-2026-ARXIV-2606-29914 | score_7_9 | not_selected | — | — | 未入选：揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29914 |
| SF-2026-ARXIV-2606-29920 | score_7_9 | not_selected | — | — | 未入选：把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29920 |
| SF-2026-ARXIV-2606-29955 | score_7_9 | not_selected | — | — | 未入选：把 spreadsheet Agent 从单操作测量升级为带副作用的端到端业务工作流。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29955 |
| SF-2026-ARXIV-2606-29957 | score_7_9 | not_selected | — | — | 未入选：把编码 Agent 的用户澄清、约束追加与交互过程纳入发布评测。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29957 |
| SF-2026-ARXIV-2606-29959 | score_7_9 | not_selected | — | — | 未入选：按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。 该变化由 AGENT-RAG 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29959 |
| SF-2026-ARXIV-2606-29975 | score_7_9 | not_selected | — | — | 未入选：为只读大规模训练数据定义快照、shuffle、跨集群 staging 与再发布存储层。 该变化由 TRAIN-DATA 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29975 |
| SF-2026-ARXIV-2606-29982 | score_7_9 | not_selected | — | — | 未入选：按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。 该变化由 MODEL-MOE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29982 |
| SF-2026-ARXIV-2606-29986 | score_7_9 | not_selected | — | — | 未入选：把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。 该变化由 INFER-PD-DISAGGREGATION 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-29986 |
| SF-2026-ARXIV-2606-30005 | score_7_9 | not_selected | — | — | 未入选：让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。 该变化由 AGENT-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30005 |
| SF-2026-ARXIV-2606-30107 | score_7_9 | not_selected | — | — | 未入选：把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30107 |
| SF-2026-ARXIV-2606-30119 | score_7_9 | not_selected | — | — | 未入选：以多层行为指纹识别 Web Agent，改变开放网络中的 Agent 身份与审计边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30119 |
| SF-2026-ARXIV-2606-30185 | score_7_9 | not_selected | — | — | 未入选：让冻结 VLM 动态生成、评估并演化 skill/tool 集合，改变工具注册状态。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30185 |
| SF-2026-ARXIV-2606-30251 | score_7_9 | not_selected | — | — | 未入选：把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30251 |
| SF-2026-ARXIV-2606-30263 | score_7_9 | not_selected | — | — | 未入选：揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30263 |
| SF-2026-ARXIV-2606-30265 | score_7_9 | not_selected | — | — | 未入选：给 speculative decoding 的 draft 接受事件建立可解释理论边界。 该变化由 INFER-SPECULATIVE-DECODING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30265 |
| SF-2026-ARXIV-2606-30338 | score_7_9 | not_selected | — | — | 未入选：在有限输出访问下把外部公平审计建模为顺序采样与停止合同。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30338 |
| SF-2026-ARXIV-2606-30373 | score_7_9 | not_selected | — | — | 未入选：把预训练模型 hub 的应用组合、权重来源与在线执行面纳入供应链威胁模型。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30373 |
| SF-2026-ARXIV-2606-30383 | score_7_9 | selected | DA-20260630-PRINCIPAL-LOYALTY | — | 入选：把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。 | analysis:DA-20260630-PRINCIPAL-LOYALTY |
| SF-2026-ARXIV-2606-30389 | score_7_9 | not_selected | — | — | 未入选：以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。 该变化由 INFER-DECODE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30389 |
| SF-2026-ARXIV-2606-30391 | score_7_9 | not_selected | — | — | 未入选：让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。 该变化由 INFER-SCHEDULING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30391 |
| SF-2026-ARXIV-2606-30449 | score_7_9 | not_selected | — | — | 未入选：三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。 该变化由 PLATFORM-MONITORING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30449 |
| SF-2026-ARXIV-2606-30531 | score_7_9 | not_selected | — | — | 未入选：把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30531 |
| SF-2026-ARXIV-2606-30534 | score_7_9 | not_selected | — | — | 未入选：以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。 该变化由 MULTIMODAL-WORLD-MODELS 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30534 |
| SF-2026-ARXIV-2606-30546 | score_7_9 | not_selected | — | — | 未入选：以 specification-driven validation 把多 Agent 原型升级为可重复的系统验收。 该变化由 AGENT-MULTI-AGENT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30546 |
| SF-2026-ARXIV-2606-30560 | score_7_9 | not_selected | — | — | 未入选：用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。 该变化由 INFER-SCHEDULING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30560 |
| SF-2026-ARXIV-2606-30562 | score_7_9 | not_selected | — | — | 未入选：把全注意力层替换为线性注意力的转换、校准和质量边界系统化。 该变化由 MODEL-LONG-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30562 |
| SF-2026-ARXIV-2606-30566 | score_7_9 | not_selected | — | — | 未入选：用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30566 |
| SF-2026-ARXIV-2606-30573 | score_7_9 | not_selected | — | — | 未入选：把 SWE benchmark 改为用户驱动的长程多轮会话与动态验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30573 |
| SF-2026-ARXIV-2606-30602 | score_7_9 | not_selected | — | — | 未入选：按通信通道脆弱性排序防护，改变多 Agent 安全资源分配。 该变化由 AGENT-MULTI-AGENT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30602 |
| SF-2026-ARXIV-2606-30616 | score_7_9; potential_books_delta | not_selected | — | — | 未入选：以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。 该变化由 AGENT-PLATFORM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30616 |
| SF-2026-ARXIV-2606-30627 | score_7_9 | not_selected | — | — | 未入选：证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30627 |
| SF-2026-ARXIV-2606-30634 | score_7_9 | not_selected | — | — | 未入选：证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。 该变化由 TRAIN-PIPELINE-PARALLEL 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30634 |
| SF-2026-ARXIV-2606-30639 | score_7_9 | not_selected | — | — | 未入选：让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。 该变化由 MULTIMODAL-WORLD-MODELS 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30639 |
| SF-2026-ARXIV-2606-30697 | score_7_9 | not_selected | — | — | 未入选：提出面向 Agent 的语义 OS 层，使界面状态和动作能力成为稳定平台接口。 该变化由 AGENT-PLATFORM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30697 |
| SF-2026-ARXIV-2606-30704 | score_7_9 | not_selected | — | — | 未入选：把一次性解题转为可复用工作流合成，并显式验证结构与执行。 该变化由 AGENT-WORKFLOW 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30704 |
| SF-2026-ARXIV-2606-30774 | score_7_9 | not_selected | — | — | 未入选：把自然语言反馈收益与重复尝试收益分离，修正交互改进测量。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30774 |
| SF-2026-ARXIV-2606-30775 | score_7_9 | not_selected | — | — | 未入选：以 production routing 错误为反馈重写 skill description，改变技能发现控制环。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30775 |
| SF-2026-ARXIV-2606-30783 | score_7_9 | not_selected | — | — | 未入选：揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30783 |
| SF-2026-ARXIV-2606-30788 | score_7_9; potential_books_delta | selected | DA-20260630-REVOCABLE-STATE | — | 入选：用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。 | analysis:DA-20260630-REVOCABLE-STATE |
| SF-2026-ARXIV-2606-30789 | score_7_9 | not_selected | — | — | 未入选：以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。 该变化由 TRAIN-GRPO 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30789 |
| SF-2026-ARXIV-2606-30801 | score_7_9 | not_selected | — | — | 未入选：用可复现 Agent 身份与行为脚本扩展黑盒个性化算法审计。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30801 |
| SF-2026-ARXIV-2606-30814 | score_7_9 | not_selected | — | — | 未入选：证明模型准确率差异可反转 calibration 排名，要求 accuracy-controlled 比较。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30814 |
| SF-2026-ARXIV-2606-30850 | score_7_9 | not_selected | — | — | 未入选：把多轮证据到达后的 belief trajectory 与最终答案分开评测。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30850 |
| SF-2026-ARXIV-2606-30852 | score_7_9 | not_selected | — | — | 未入选：把 reasoning early exit 的质量、校准和成本放进同一停止合同。 该变化由 INFER-DECODE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30852 |
| SF-2026-ARXIV-2606-30899 | score_7_9 | not_selected | — | — | 未入选：以曲率定位 backdoor 模块并低秩净化，改变全量微调式修复边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30899 |
| SF-2026-ARXIV-2606-30911 | score_7_9 | not_selected | — | — | 未入选：把跨任务技巧分层积累为可迁移知识，减少 ML Agent 重复探索。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30911 |
| SF-2026-ARXIV-2606-30919 | score_7_9 | not_selected | — | — | 未入选：在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。 该变化由 PLATFORM-GATEWAY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30919 |
| SF-2026-ARXIV-2606-30931 | score_7_9 | not_selected | — | — | 未入选：把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-30931 |
| SF-2026-ARXIV-2606-31002 | score_7_9 | not_selected | — | — | 未入选：把 NL-to-Lean 的编译通过与语义忠实分层，修正 formalization 验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。 | analysis-decision:SF-2026-ARXIV-2606-31002 |

<!-- analysis-decision:SF-2026-ARXIV-2606-29685:start -->
未入选：把儿童安全从显式伤害响应前移为上游风险识别，并要求按风险层级验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29685:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29699:start -->
未入选：证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。 该变化由 PLATFORM-MONITORING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29699:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29700:start -->
未入选：把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。 该变化由 AGENT-PLANNING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29700:end -->

<!-- analysis:DA-20260630-HETERO-PD-BOUNDARY:start -->
入选：把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。
<!-- analysis:DA-20260630-HETERO-PD-BOUNDARY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29713:start -->
未入选：把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。 该变化由 AGENT-REFLECTION 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29713:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29718:start -->
未入选：把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。 该变化由 AGENT-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29718:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29719:start -->
未入选：把 evaluator 漂移和偏好坍缩作为持续评测系统的测量状态。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29719:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29745:start -->
未入选：以显式 belief state 和逐轮 epistemic credit 控制信息获取与停止动作。 该变化由 AGENT-PLANNING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29745:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29758:start -->
未入选：以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29758:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29775:start -->
未入选：把 MIG 切分、性能与能耗纳入可学习的集群调度状态。 该变化由 PLATFORM-GPU-SCHEDULER 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29778:start -->
未入选：以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29778:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29784:start -->
未入选：用历史 noisy labels 提高生成模型评测灵敏度，同时保留专家标签边界。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29784:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29788:start -->
未入选：证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29788:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29871:start -->
未入选：把训练 recipe 的观测、建议、边界检查和执行组织成受限闭环控制面。 该变化由 PLATFORM-TRAINING-OPERATOR 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29887:start -->
未入选：把应用自定义政策的层级冲突与多轮上下文纳入 guardrail 验收。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29887:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29914:start -->
未入选：揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29914:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29920:start -->
未入选：把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29920:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29955:start -->
未入选：把 spreadsheet Agent 从单操作测量升级为带副作用的端到端业务工作流。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29955:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29957:start -->
未入选：把编码 Agent 的用户澄清、约束追加与交互过程纳入发布评测。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29957:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29959:start -->
未入选：按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。 该变化由 AGENT-RAG 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29959:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29975:start -->
未入选：为只读大规模训练数据定义快照、shuffle、跨集群 staging 与再发布存储层。 该变化由 TRAIN-DATA 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29975:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29982:start -->
未入选：按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。 该变化由 MODEL-MOE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29982:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-29986:start -->
未入选：把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。 该变化由 INFER-PD-DISAGGREGATION 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-29986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30005:start -->
未入选：让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。 该变化由 AGENT-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30005:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30107:start -->
未入选：把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30107:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30119:start -->
未入选：以多层行为指纹识别 Web Agent，改变开放网络中的 Agent 身份与审计边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30119:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30185:start -->
未入选：让冻结 VLM 动态生成、评估并演化 skill/tool 集合，改变工具注册状态。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30251:start -->
未入选：把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30251:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30263:start -->
未入选：揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30263:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30265:start -->
未入选：给 speculative decoding 的 draft 接受事件建立可解释理论边界。 该变化由 INFER-SPECULATIVE-DECODING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30265:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30338:start -->
未入选：在有限输出访问下把外部公平审计建模为顺序采样与停止合同。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30338:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30373:start -->
未入选：把预训练模型 hub 的应用组合、权重来源与在线执行面纳入供应链威胁模型。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30373:end -->

<!-- analysis:DA-20260630-PRINCIPAL-LOYALTY:start -->
入选：把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。
<!-- analysis:DA-20260630-PRINCIPAL-LOYALTY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30389:start -->
未入选：以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。 该变化由 INFER-DECODE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30391:start -->
未入选：让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。 该变化由 INFER-SCHEDULING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30391:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30449:start -->
未入选：三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。 该变化由 PLATFORM-MONITORING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30449:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30531:start -->
未入选：把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30531:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30534:start -->
未入选：以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。 该变化由 MULTIMODAL-WORLD-MODELS 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30534:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30546:start -->
未入选：以 specification-driven validation 把多 Agent 原型升级为可重复的系统验收。 该变化由 AGENT-MULTI-AGENT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30546:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30560:start -->
未入选：用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。 该变化由 INFER-SCHEDULING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30560:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30562:start -->
未入选：把全注意力层替换为线性注意力的转换、校准和质量边界系统化。 该变化由 MODEL-LONG-CONTEXT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30562:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30566:start -->
未入选：用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30573:start -->
未入选：把 SWE benchmark 改为用户驱动的长程多轮会话与动态验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30573:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30602:start -->
未入选：按通信通道脆弱性排序防护，改变多 Agent 安全资源分配。 该变化由 AGENT-MULTI-AGENT 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30602:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30616:start -->
未入选：以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。 该变化由 AGENT-PLATFORM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30616:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30627:start -->
未入选：证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。 该变化由 TRAIN-RLHF 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30627:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30634:start -->
未入选：证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。 该变化由 TRAIN-PIPELINE-PARALLEL 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30639:start -->
未入选：让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。 该变化由 MULTIMODAL-WORLD-MODELS 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30639:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30697:start -->
未入选：提出面向 Agent 的语义 OS 层，使界面状态和动作能力成为稳定平台接口。 该变化由 AGENT-PLATFORM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30704:start -->
未入选：把一次性解题转为可复用工作流合成，并显式验证结构与执行。 该变化由 AGENT-WORKFLOW 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30774:start -->
未入选：把自然语言反馈收益与重复尝试收益分离，修正交互改进测量。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30775:start -->
未入选：以 production routing 错误为反馈重写 skill description，改变技能发现控制环。 该变化由 AGENT-TOOL-CALLING 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30775:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30783:start -->
未入选：揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30783:end -->

<!-- analysis:DA-20260630-REVOCABLE-STATE:start -->
入选：用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。，在跨层 handoff、控制面新颖性和验证边界上代表当天 frontier。
<!-- analysis:DA-20260630-REVOCABLE-STATE:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30789:start -->
未入选：以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。 该变化由 TRAIN-GRPO 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30789:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30801:start -->
未入选：用可复现 Agent 身份与行为脚本扩展黑盒个性化算法审计。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30801:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30814:start -->
未入选：证明模型准确率差异可反转 calibration 排名，要求 accuracy-controlled 比较。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30814:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30850:start -->
未入选：把多轮证据到达后的 belief trajectory 与最终答案分开评测。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30850:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30852:start -->
未入选：把 reasoning early exit 的质量、校准和成本放进同一停止合同。 该变化由 INFER-DECODE 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30852:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30899:start -->
未入选：以曲率定位 backdoor 模块并低秩净化，改变全量微调式修复边界。 该变化由 PLATFORM-SECURITY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30899:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30911:start -->
未入选：把跨任务技巧分层积累为可迁移知识，减少 ML Agent 重复探索。 该变化由 AGENT-MEMORY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30911:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30919:start -->
未入选：在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。 该变化由 PLATFORM-GATEWAY 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30919:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-30931:start -->
未入选：把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-30931:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-31002:start -->
未入选：把 NL-to-Lean 的编译通过与语义忠实分层，修正 formalization 验收。 该变化由 PLATFORM-EVALUATION-SYSTEM 持有，但相对三项 winner 的跨层 handoff 或验证强度更窄；Evidence 与 Books disposition 不降级。
<!-- analysis-decision:SF-2026-ARXIV-2606-31002:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-29699 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-29699 | delta:SF-2026-ARXIV-2606-29699 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29699 |
| SF-2026-ARXIV-2606-29700 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-29700 | delta:SF-2026-ARXIV-2606-29700 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29700 |
| SF-2026-ARXIV-2606-29708 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-29708 | delta:SF-2026-ARXIV-2606-29708 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29708 |
| SF-2026-ARXIV-2606-29713 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-29713 | delta:SF-2026-ARXIV-2606-29713 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29713 |
| SF-2026-ARXIV-2606-29718 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-29718 | delta:SF-2026-ARXIV-2606-29718 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29718 |
| SF-2026-ARXIV-2606-29758 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2606-29758 | delta:SF-2026-ARXIV-2606-29758 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29758 |
| SF-2026-ARXIV-2606-29778 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-29778 | delta:SF-2026-ARXIV-2606-29778 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29778 |
| SF-2026-ARXIV-2606-29788 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-29788 | delta:SF-2026-ARXIV-2606-29788 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29788 |
| SF-2026-ARXIV-2606-29914 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-29914 | delta:SF-2026-ARXIV-2606-29914 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29914 |
| SF-2026-ARXIV-2606-29920 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-29920 | delta:SF-2026-ARXIV-2606-29920 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29920 |
| SF-2026-ARXIV-2606-29959 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-29959 | delta:SF-2026-ARXIV-2606-29959 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29959 |
| SF-2026-ARXIV-2606-29982 | MODEL-MOE | books/part-02-model/21-moe.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-29982 | delta:SF-2026-ARXIV-2606-29982 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29982 |
| SF-2026-ARXIV-2606-29986 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-29986 | delta:SF-2026-ARXIV-2606-29986 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-29986 |
| SF-2026-ARXIV-2606-30005 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-30005 | delta:SF-2026-ARXIV-2606-30005 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30005 |
| SF-2026-ARXIV-2606-30107 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-30107 | delta:SF-2026-ARXIV-2606-30107 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30107 |
| SF-2026-ARXIV-2606-30251 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2606-30251 | delta:SF-2026-ARXIV-2606-30251 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30251 |
| SF-2026-ARXIV-2606-30263 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/62-gateway.md#L1 | existing:SF-2026-ARXIV-2606-30263 | delta:SF-2026-ARXIV-2606-30263 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30263 |
| SF-2026-ARXIV-2606-30265 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2606-30265 | delta:SF-2026-ARXIV-2606-30265 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30265 |
| SF-2026-ARXIV-2606-30383 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/62-gateway.md#L1 | existing:SF-2026-ARXIV-2606-30383 | delta:SF-2026-ARXIV-2606-30383 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30383 |
| SF-2026-ARXIV-2606-30389 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L1 | books/part-05-inference-system/42-what-happens-during-inference.md#L1 | existing:SF-2026-ARXIV-2606-30389 | delta:SF-2026-ARXIV-2606-30389 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30389 |
| SF-2026-ARXIV-2606-30391 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-30391 | delta:SF-2026-ARXIV-2606-30391 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30391 |
| SF-2026-ARXIV-2606-30449 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-30449 | delta:SF-2026-ARXIV-2606-30449 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30449 |
| SF-2026-ARXIV-2606-30531 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-30531 | delta:SF-2026-ARXIV-2606-30531 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30531 |
| SF-2026-ARXIV-2606-30534 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-30534 | delta:SF-2026-ARXIV-2606-30534 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30534 |
| SF-2026-ARXIV-2606-30560 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-30560 | delta:SF-2026-ARXIV-2606-30560 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30560 |
| SF-2026-ARXIV-2606-30562 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L1 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | existing:SF-2026-ARXIV-2606-30562 | delta:SF-2026-ARXIV-2606-30562 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30562 |
| SF-2026-ARXIV-2606-30566 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-30566 | delta:SF-2026-ARXIV-2606-30566 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30566 |
| SF-2026-ARXIV-2606-30616 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-30616 | delta:SF-2026-ARXIV-2606-30616 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-30616 |
| SF-2026-ARXIV-2606-30627 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2606-30627 | delta:SF-2026-ARXIV-2606-30627 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30627 |
| SF-2026-ARXIV-2606-30634 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#L1 | books/part-04-training-system/36-distributed-training.md#L1 | existing:SF-2026-ARXIV-2606-30634 | delta:SF-2026-ARXIV-2606-30634 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30634 |
| SF-2026-ARXIV-2606-30639 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2606-30639 | delta:SF-2026-ARXIV-2606-30639 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30639 |
| SF-2026-ARXIV-2606-30775 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-30775 | delta:SF-2026-ARXIV-2606-30775 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30775 |
| SF-2026-ARXIV-2606-30783 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/62-gateway.md#L1 | existing:SF-2026-ARXIV-2606-30783 | delta:SF-2026-ARXIV-2606-30783 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30783 |
| SF-2026-ARXIV-2606-30788 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2606-30788 | delta:SF-2026-ARXIV-2606-30788 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-30788 |
| SF-2026-ARXIV-2606-30789 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-30789 | delta:SF-2026-ARXIV-2606-30789 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30789 |
| SF-2026-ARXIV-2606-30852 | INFER-DECODE | books/part-05-inference-system/44-decode.md#L1 | books/part-05-inference-system/42-what-happens-during-inference.md#L1 | existing:SF-2026-ARXIV-2606-30852 | delta:SF-2026-ARXIV-2606-30852 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30852 |
| SF-2026-ARXIV-2606-30919 | PLATFORM-GATEWAY | books/part-06-ai-infrastructure/62-gateway.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-30919 | delta:SF-2026-ARXIV-2606-30919 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30919 |
| SF-2026-ARXIV-2606-30931 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-30931 | delta:SF-2026-ARXIV-2606-30931 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-30931 |

<!-- books-review:SF-2026-ARXIV-2606-29699:start -->
<!-- existing:SF-2026-ARXIV-2606-29699:start -->
现有 owner 已覆盖 PLATFORM-MONITORING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29699:end -->
<!-- delta:SF-2026-ARXIV-2606-29699:start -->
证明内部探针的回溯可分性不等于低噪声提前预警，修正运行时监测证明边界。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29699:end -->
<!-- books-review:SF-2026-ARXIV-2606-29699:end -->

<!-- books-review:SF-2026-ARXIV-2606-29700:start -->
<!-- existing:SF-2026-ARXIV-2606-29700:start -->
现有 owner 已覆盖 AGENT-PLANNING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29700:end -->
<!-- delta:SF-2026-ARXIV-2606-29700:start -->
把形式化规格的断言权交给确定性 planner，并用不可执行诊断驱动修复。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29700:end -->
<!-- books-review:SF-2026-ARXIV-2606-29700:end -->

<!-- books-review:SF-2026-ARXIV-2606-29708:start -->
<!-- existing:SF-2026-ARXIV-2606-29708:start -->
现有 owner 已覆盖 INFER-PD-DISAGGREGATION 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29708:end -->
<!-- delta:SF-2026-ARXIV-2606-29708:start -->
把异构 prefill/decode、KV 传输格式与互联约束合成部署设计空间。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29708:end -->
<!-- books-review:SF-2026-ARXIV-2606-29708:end -->

<!-- books-review:SF-2026-ARXIV-2606-29713:start -->
<!-- existing:SF-2026-ARXIV-2606-29713:start -->
现有 owner 已覆盖 AGENT-REFLECTION 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29713:end -->
<!-- delta:SF-2026-ARXIV-2606-29713:start -->
把事实归因验证从二元标签改为过程奖励与可自我修正的 verifier 状态。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29713:end -->
<!-- books-review:SF-2026-ARXIV-2606-29713:end -->

<!-- books-review:SF-2026-ARXIV-2606-29718:start -->
<!-- existing:SF-2026-ARXIV-2606-29718:start -->
现有 owner 已覆盖 AGENT-CONTEXT 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29718:end -->
<!-- delta:SF-2026-ARXIV-2606-29718:start -->
把长程检索中的 context rot 定位为可诊断的历史状态污染，并给出缓解控制。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29718:end -->
<!-- books-review:SF-2026-ARXIV-2606-29718:end -->

<!-- books-review:SF-2026-ARXIV-2606-29758:start -->
<!-- existing:SF-2026-ARXIV-2606-29758:start -->
现有 owner 已覆盖 TRAIN-RLHF 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29758:end -->
<!-- delta:SF-2026-ARXIV-2606-29758:start -->
以 prefix sampling 恢复 critic-free RLHF 截断位置的信用分配并改变显存/计算权衡。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29758:end -->
<!-- books-review:SF-2026-ARXIV-2606-29758:end -->

<!-- books-review:SF-2026-ARXIV-2606-29778:start -->
<!-- existing:SF-2026-ARXIV-2606-29778:start -->
现有 owner 已覆盖 AGENT-MEMORY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29778:end -->
<!-- delta:SF-2026-ARXIV-2606-29778:start -->
以聚合式统一存储替代向量库/图库分裂，改变长会话多类型记忆所有权。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29778:end -->
<!-- books-review:SF-2026-ARXIV-2606-29778:end -->

<!-- books-review:SF-2026-ARXIV-2606-29788:start -->
<!-- existing:SF-2026-ARXIV-2606-29788:start -->
现有 owner 已覆盖 AGENT-MEMORY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29788:end -->
<!-- delta:SF-2026-ARXIV-2606-29788:start -->
证明删除文本条目后事实仍可由关联图像恢复，修正遗忘与删除验收合同。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29788:end -->
<!-- books-review:SF-2026-ARXIV-2606-29788:end -->

<!-- books-review:SF-2026-ARXIV-2606-29914:start -->
<!-- existing:SF-2026-ARXIV-2606-29914:start -->
现有 owner 已覆盖 PLATFORM-EVALUATION-SYSTEM 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29914:end -->
<!-- delta:SF-2026-ARXIV-2606-29914:start -->
揭示 Agent memory 对比中模型、embedding 与 retrieval pipeline 的混杂变量。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29914:end -->
<!-- books-review:SF-2026-ARXIV-2606-29914:end -->

<!-- books-review:SF-2026-ARXIV-2606-29920:start -->
<!-- existing:SF-2026-ARXIV-2606-29920:start -->
现有 owner 已覆盖 PLATFORM-EVALUATION-SYSTEM 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29920:end -->
<!-- delta:SF-2026-ARXIV-2606-29920:start -->
把 LLM judge 对 rubric 条件的逐条可验证性与总体打分分开。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29920:end -->
<!-- books-review:SF-2026-ARXIV-2606-29920:end -->

<!-- books-review:SF-2026-ARXIV-2606-29959:start -->
<!-- existing:SF-2026-ARXIV-2606-29959:start -->
现有 owner 已覆盖 AGENT-RAG 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29959:end -->
<!-- delta:SF-2026-ARXIV-2606-29959:start -->
按查询知识边界分配检索预算，改变固定 top-k 的成本与噪声控制。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29959:end -->
<!-- books-review:SF-2026-ARXIV-2606-29959:end -->

<!-- books-review:SF-2026-ARXIV-2606-29982:start -->
<!-- existing:SF-2026-ARXIV-2606-29982:start -->
现有 owner 已覆盖 MODEL-MOE 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29982:end -->
<!-- delta:SF-2026-ARXIV-2606-29982:start -->
按专家与设备异构成本分配执行，改变 MoE 推理的数据移动与调度所有权。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29982:end -->
<!-- books-review:SF-2026-ARXIV-2606-29982:end -->

<!-- books-review:SF-2026-ARXIV-2606-29986:start -->
<!-- existing:SF-2026-ARXIV-2606-29986:start -->
现有 owner 已覆盖 INFER-PD-DISAGGREGATION 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-29986:end -->
<!-- delta:SF-2026-ARXIV-2606-29986:start -->
把 HBM 与容量型内存加速器组合进 disaggregated serving 的分层状态。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-29986:end -->
<!-- books-review:SF-2026-ARXIV-2606-29986:end -->

<!-- books-review:SF-2026-ARXIV-2606-30005:start -->
<!-- existing:SF-2026-ARXIV-2606-30005:start -->
现有 owner 已覆盖 AGENT-CONTEXT 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30005:end -->
<!-- delta:SF-2026-ARXIV-2606-30005:start -->
让 Agent 感知自身上下文状态并主动压缩，而非由外部固定策略单独管理。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30005:end -->
<!-- books-review:SF-2026-ARXIV-2606-30005:end -->

<!-- books-review:SF-2026-ARXIV-2606-30107:start -->
<!-- existing:SF-2026-ARXIV-2606-30107:start -->
现有 owner 已覆盖 AGENT-TOOL-CALLING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30107:end -->
<!-- delta:SF-2026-ARXIV-2606-30107:start -->
把物理设计的断言权从 LLM 移到确定性认证引擎，形成 proposal/certification 边界。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30107:end -->
<!-- books-review:SF-2026-ARXIV-2606-30107:end -->

<!-- books-review:SF-2026-ARXIV-2606-30251:start -->
<!-- existing:SF-2026-ARXIV-2606-30251:start -->
现有 owner 已覆盖 TRAIN-RLHF 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30251:end -->
<!-- delta:SF-2026-ARXIV-2606-30251:start -->
把工具调用轨迹的局部观测与结果信用显式归因，修正稀疏终局奖励。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30251:end -->
<!-- books-review:SF-2026-ARXIV-2606-30251:end -->

<!-- books-review:SF-2026-ARXIV-2606-30263:start -->
<!-- existing:SF-2026-ARXIV-2606-30263:start -->
现有 owner 已覆盖 PLATFORM-SECURITY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30263:end -->
<!-- delta:SF-2026-ARXIV-2606-30263:start -->
揭示良性外观样本可承载隐藏 harmful supervision，扩展训练数据威胁模型。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30263:end -->
<!-- books-review:SF-2026-ARXIV-2606-30263:end -->

<!-- books-review:SF-2026-ARXIV-2606-30265:start -->
<!-- existing:SF-2026-ARXIV-2606-30265:start -->
现有 owner 已覆盖 INFER-SPECULATIVE-DECODING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30265:end -->
<!-- delta:SF-2026-ARXIV-2606-30265:start -->
给 speculative decoding 的 draft 接受事件建立可解释理论边界。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30265:end -->
<!-- books-review:SF-2026-ARXIV-2606-30265:end -->

<!-- books-review:SF-2026-ARXIV-2606-30383:start -->
<!-- existing:SF-2026-ARXIV-2606-30383:start -->
现有 owner 已覆盖 PLATFORM-SECURITY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30383:end -->
<!-- delta:SF-2026-ARXIV-2606-30383:start -->
把多方 Agent 的 principal、counterparty 与指令忠诚边界显式化。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30383:end -->
<!-- books-review:SF-2026-ARXIV-2606-30383:end -->

<!-- books-review:SF-2026-ARXIV-2606-30389:start -->
<!-- existing:SF-2026-ARXIV-2606-30389:start -->
现有 owner 已覆盖 INFER-DECODE 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30389:end -->
<!-- delta:SF-2026-ARXIV-2606-30389:start -->
以预测、复用和修复解除动态稀疏注意力选择与 attention 的串行依赖。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30389:end -->
<!-- books-review:SF-2026-ARXIV-2606-30389:end -->

<!-- books-review:SF-2026-ARXIV-2606-30391:start -->
<!-- existing:SF-2026-ARXIV-2606-30391:start -->
现有 owner 已覆盖 INFER-SCHEDULING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30391:end -->
<!-- delta:SF-2026-ARXIV-2606-30391:start -->
让 serverless LLM 调度器同时持有 SLO、共享 GPU 与能耗状态。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30391:end -->
<!-- books-review:SF-2026-ARXIV-2606-30391:end -->

<!-- books-review:SF-2026-ARXIV-2606-30449:start -->
<!-- existing:SF-2026-ARXIV-2606-30449:start -->
现有 owner 已覆盖 PLATFORM-MONITORING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30449:end -->
<!-- delta:SF-2026-ARXIV-2606-30449:start -->
三项负结果证明内部探针读取情境不等于预动作意图，收紧上线监测声明。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30449:end -->
<!-- books-review:SF-2026-ARXIV-2606-30449:end -->

<!-- books-review:SF-2026-ARXIV-2606-30531:start -->
<!-- existing:SF-2026-ARXIV-2606-30531:start -->
现有 owner 已覆盖 AGENT-TOOL-CALLING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30531:end -->
<!-- delta:SF-2026-ARXIV-2606-30531:start -->
把工具选择正确但实体绑定错误识别为独立 failure mode 与验收维度。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30531:end -->
<!-- books-review:SF-2026-ARXIV-2606-30531:end -->

<!-- books-review:SF-2026-ARXIV-2606-30534:start -->
<!-- existing:SF-2026-ARXIV-2606-30534:start -->
现有 owner 已覆盖 MULTIMODAL-WORLD-MODELS 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30534:end -->
<!-- delta:SF-2026-ARXIV-2606-30534:start -->
以统一 latent world state 连接多模态输入、预测与 readout，形成跨任务状态接口。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30534:end -->
<!-- books-review:SF-2026-ARXIV-2606-30534:end -->

<!-- books-review:SF-2026-ARXIV-2606-30560:start -->
<!-- existing:SF-2026-ARXIV-2606-30560:start -->
现有 owner 已覆盖 INFER-SCHEDULING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30560:end -->
<!-- delta:SF-2026-ARXIV-2606-30560:start -->
用真实 coding-agent trace 刻画突发、长尾与并发，修正 serving workload contract。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30560:end -->
<!-- books-review:SF-2026-ARXIV-2606-30560:end -->

<!-- books-review:SF-2026-ARXIV-2606-30562:start -->
<!-- existing:SF-2026-ARXIV-2606-30562:start -->
现有 owner 已覆盖 MODEL-LONG-CONTEXT 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30562:end -->
<!-- delta:SF-2026-ARXIV-2606-30562:start -->
把全注意力层替换为线性注意力的转换、校准和质量边界系统化。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30562:end -->
<!-- books-review:SF-2026-ARXIV-2606-30562:end -->

<!-- books-review:SF-2026-ARXIV-2606-30566:start -->
<!-- existing:SF-2026-ARXIV-2606-30566:start -->
现有 owner 已覆盖 AGENT-MEMORY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30566:end -->
<!-- delta:SF-2026-ARXIV-2606-30566:start -->
用可观测 memory-tool 调用轨迹检测持久记忆投毒，并明确不可观测架构边界。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30566:end -->
<!-- books-review:SF-2026-ARXIV-2606-30566:end -->

<!-- books-review:SF-2026-ARXIV-2606-30616:start -->
<!-- existing:SF-2026-ARXIV-2606-30616:start -->
现有 owner 已覆盖 AGENT-PLATFORM 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30616:end -->
<!-- delta:SF-2026-ARXIV-2606-30616:start -->
以更长工具交互 horizon 与 on-policy distillation 替代单纯参数扩展。；该命题删除论文名后仍成立，且当前 owner 正文尚未显式覆盖。
<!-- delta:SF-2026-ARXIV-2606-30616:end -->
<!-- books-review:SF-2026-ARXIV-2606-30616:end -->

<!-- books-review:SF-2026-ARXIV-2606-30627:start -->
<!-- existing:SF-2026-ARXIV-2606-30627:start -->
现有 owner 已覆盖 TRAIN-RLHF 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30627:end -->
<!-- delta:SF-2026-ARXIV-2606-30627:start -->
证明离线保守训练可在在线适配时放大奖励劫持，修正安全迁移假设。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30627:end -->
<!-- books-review:SF-2026-ARXIV-2606-30627:end -->

<!-- books-review:SF-2026-ARXIV-2606-30634:start -->
<!-- existing:SF-2026-ARXIV-2606-30634:start -->
现有 owner 已覆盖 TRAIN-PIPELINE-PARALLEL 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30634:end -->
<!-- delta:SF-2026-ARXIV-2606-30634:start -->
证明一拍梯度延迟可在大规模异步 pipeline 中受控，改变 bubble/陈旧度权衡。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30634:end -->
<!-- books-review:SF-2026-ARXIV-2606-30634:end -->

<!-- books-review:SF-2026-ARXIV-2606-30639:start -->
<!-- existing:SF-2026-ARXIV-2606-30639:start -->
现有 owner 已覆盖 MULTIMODAL-WORLD-MODELS 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30639:end -->
<!-- delta:SF-2026-ARXIV-2606-30639:start -->
让 Agent 从执行反馈更新 world model，并以规划收益约束自演化。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30639:end -->
<!-- books-review:SF-2026-ARXIV-2606-30639:end -->

<!-- books-review:SF-2026-ARXIV-2606-30775:start -->
<!-- existing:SF-2026-ARXIV-2606-30775:start -->
现有 owner 已覆盖 AGENT-TOOL-CALLING 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30775:end -->
<!-- delta:SF-2026-ARXIV-2606-30775:start -->
以 production routing 错误为反馈重写 skill description，改变技能发现控制环。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30775:end -->
<!-- books-review:SF-2026-ARXIV-2606-30775:end -->

<!-- books-review:SF-2026-ARXIV-2606-30783:start -->
<!-- existing:SF-2026-ARXIV-2606-30783:start -->
现有 owner 已覆盖 PLATFORM-SECURITY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30783:end -->
<!-- delta:SF-2026-ARXIV-2606-30783:start -->
揭示 prompt-injection 防御通过压制不可信文本换取安全，建立 fidelity 代价边界。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30783:end -->
<!-- books-review:SF-2026-ARXIV-2606-30783:end -->

<!-- books-review:SF-2026-ARXIV-2606-30788:start -->
<!-- existing:SF-2026-ARXIV-2606-30788:start -->
现有 owner 已覆盖 AGENT-MEMORY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30788:end -->
<!-- delta:SF-2026-ARXIV-2606-30788:start -->
用进程 sidecar 隔离可撤销学习状态，避免撤销私有记忆破坏公共技能。；该命题删除论文名后仍成立，且当前 owner 正文尚未显式覆盖。
<!-- delta:SF-2026-ARXIV-2606-30788:end -->
<!-- books-review:SF-2026-ARXIV-2606-30788:end -->

<!-- books-review:SF-2026-ARXIV-2606-30789:start -->
<!-- existing:SF-2026-ARXIV-2606-30789:start -->
现有 owner 已覆盖 TRAIN-GRPO 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30789:end -->
<!-- delta:SF-2026-ARXIV-2606-30789:start -->
以闭式约化模型刻画 GRPO reward、噪声与更新动力学的适用域。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30789:end -->
<!-- books-review:SF-2026-ARXIV-2606-30789:end -->

<!-- books-review:SF-2026-ARXIV-2606-30852:start -->
<!-- existing:SF-2026-ARXIV-2606-30852:start -->
现有 owner 已覆盖 INFER-DECODE 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30852:end -->
<!-- delta:SF-2026-ARXIV-2606-30852:start -->
把 reasoning early exit 的质量、校准和成本放进同一停止合同。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30852:end -->
<!-- books-review:SF-2026-ARXIV-2606-30852:end -->

<!-- books-review:SF-2026-ARXIV-2606-30919:start -->
<!-- existing:SF-2026-ARXIV-2606-30919:start -->
现有 owner 已覆盖 PLATFORM-GATEWAY 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30919:end -->
<!-- delta:SF-2026-ARXIV-2606-30919:start -->
在强模型将被调用时跳过弱模型，按预算自适应改变 edge-cloud 路由。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30919:end -->
<!-- books-review:SF-2026-ARXIV-2606-30919:end -->

<!-- books-review:SF-2026-ARXIV-2606-30931:start -->
<!-- existing:SF-2026-ARXIV-2606-30931:start -->
现有 owner 已覆盖 PLATFORM-EVALUATION-SYSTEM 的 identity、状态版本、commit authority 与保守 fallback。
<!-- existing:SF-2026-ARXIV-2606-30931:end -->
<!-- delta:SF-2026-ARXIV-2606-30931:start -->
把 judge panel 的相关误差、鲁棒聚合与不确定性纳入统计合同。；与 owner 已有长期命题同构，保留 Review 证据而不重复正文。
<!-- delta:SF-2026-ARXIV-2606-30931:end -->
<!-- books-review:SF-2026-ARXIV-2606-30931:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260630-COVERAGE | fresh-context:june30-denominator | coverage | coverage:SRC-ARXIV:20260630 | none | — | passed |
| SA-20260630-EVIDENCE | fresh-context:june30-evidence | evidence | validator:review-completion-v1 | none | — | passed |
| SA-20260630-SELECTION | fresh-context:june30-selection | deep_analysis_selection | validator:deep-analysis-selection-v1 | none | — | passed |
| SA-20260630-BOOKS | fresh-context:june30-books-postwrite | books | validator:books-comparison-v1; review:SF-2026-ARXIV-2606-29685; review:SF-2026-ARXIV-2606-29719; review:SF-2026-ARXIV-2606-29745; review:SF-2026-ARXIV-2606-29775; review:SF-2026-ARXIV-2606-29784; review:SF-2026-ARXIV-2606-29871; review:SF-2026-ARXIV-2606-29887; review:SF-2026-ARXIV-2606-29955; review:SF-2026-ARXIV-2606-29957; review:SF-2026-ARXIV-2606-29975; review:SF-2026-ARXIV-2606-30119; review:SF-2026-ARXIV-2606-30185; review:SF-2026-ARXIV-2606-30338; review:SF-2026-ARXIV-2606-30373; review:SF-2026-ARXIV-2606-30546; review:SF-2026-ARXIV-2606-30573; review:SF-2026-ARXIV-2606-30602; review:SF-2026-ARXIV-2606-30697; review:SF-2026-ARXIV-2606-30704; review:SF-2026-ARXIV-2606-30774; review:SF-2026-ARXIV-2606-30801; review:SF-2026-ARXIV-2606-30814; review:SF-2026-ARXIV-2606-30850; review:SF-2026-ARXIV-2606-30899; review:SF-2026-ARXIV-2606-30911; review:SF-2026-ARXIV-2606-31002 | none | 64/64 post-write audit: 2 Integrate unique-owner writes, 36 No Change and 26 Weekly Only zero leakage; unresolved findings 0 | passed |

## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- Exact-version access、pending 与 blocker 状态保留在 Review Completion Receipt 和 date-local source packet；该 legacy report 没有单独的 Materials section。

## 9. Recommended Action

2 Integrate families were written to 2 unique owners under the shared lock; 36 No Change and 26 Weekly Only families remained unwritten. The 64/64 fresh post-write audit found no unresolved owner, semantic-boundary or leakage finding; `docs/LEARNING_STATE.md` remained unchanged.

## 10. Repository Changes

- Added 2026-06-30 Daily/source receipts and date-specific audit/apply scripts.
- Updated only the root-authorized 06-30 blocks in `books/part-07-agent/77-memory.md` and `books/part-07-agent/84-agent-platform.md`; `docs/LEARNING_STATE.md` was not edited.

## 11. Open Questions

- None for this Daily. The 64/64 post-write semantic audit has zero unresolved findings.

## 12. Sources

- [CAREBench: A Child-Safety Risk Benchmark for Language Models](https://arxiv.org/abs/2606.29685v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Early Warning Signals for OpenVLA Failure under Visual Distribution Shift](https://arxiv.org/abs/2606.29699v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback](https://arxiv.org/abs/2606.29700v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Demystifying the Design Space and Best Practices for Heterogeneous LLM Inference and Serving](https://arxiv.org/abs/2606.29708v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution](https://arxiv.org/abs/2606.29713v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Diagnosing and Mitigating Context Rot in Long-horizon Search](https://arxiv.org/abs/2606.29718v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [A Diagnostic Framework and Multi-Evaluator Audit of Evaluator-Driven Preference Dynamics in Self-Adapting LLM Agents](https://arxiv.org/abs/2606.29719v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [ECHO: Learning Epistemically Adaptive Language Agents with Turn-Level Credit](https://arxiv.org/abs/2606.29745v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [PS-PPO: Prefix-Sampling PPO for Critic-Free RLHF](https://arxiv.org/abs/2606.29758v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SMART-MIG: A Learning Framework for Scalable and Energy-Efficient GPU Scheduling](https://arxiv.org/abs/2606.29775v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Mandol: An Agglomerative Agent Memory System for Long-Term Conversations](https://arxiv.org/abs/2606.29778v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [HERO: Improving the Reliability and Sensitivity of Generative Model Evaluation Using Historical Data](https://arxiv.org/abs/2606.29784v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [MemLeak: Diagnosing Information Leaks in Multimodal Agent Memory](https://arxiv.org/abs/2606.29788v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes](https://arxiv.org/abs/2606.29871v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SafePyramid: A Hierarchical Benchmark for In-context Policy Guardrailing](https://arxiv.org/abs/2606.29887v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [MemDelta: Controlled Baselines and Hidden Confounds in Agent Memory Evaluation](https://arxiv.org/abs/2606.29914v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/abs/2606.29920v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SpreadsheetBench 2: Evaluating Agents on End-to-End Business Spreadsheet Workflows](https://arxiv.org/abs/2606.29955v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SWE-Together: Evaluating Coding Agents in Interactive User Sessions](https://arxiv.org/abs/2606.29957v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Know Before You Fetch: Calibrated Retrieval-Budget Allocation for Retrieval-Augmented Generation](https://arxiv.org/abs/2606.29959v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Atompack: A Storage and Distribution Layer for Read-Heavy Atomistic ML Training Datasets](https://arxiv.org/abs/2606.29975v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Beyond Uniform Experts: Cost-Aware Expert Execution for Efficient Multi-Device MoE Inference](https://arxiv.org/abs/2606.29982v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators](https://arxiv.org/abs/2606.29986v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception](https://arxiv.org/abs/2606.30005v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Structural Certification for Reliable Physical Design with Language Models](https://arxiv.org/abs/2606.30107v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting](https://arxiv.org/abs/2606.30119v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Dynamo: Dynamic Skill-Tool Evolution for Vision-Language Agents](https://arxiv.org/abs/2606.30185v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [TACO: Tool-Augmented Credit Optimization for Agentic Tool Use](https://arxiv.org/abs/2606.30251v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Defending Against Harmful Supervision Hidden in Benign Samples](https://arxiv.org/abs/2606.30263v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding](https://arxiv.org/abs/2606.30265v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Sequential Fairness Auditing with Limited Output Access](https://arxiv.org/abs/2606.30338v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs](https://arxiv.org/abs/2606.30373v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Whose Side Is Your Agent On? Multi-Party Principal Loyalty in LLM Agents](https://arxiv.org/abs/2606.30383v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/abs/2606.30389v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs](https://arxiv.org/abs/2606.30391v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring](https://arxiv.org/abs/2606.30449v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Entity Binding Failures in Tool-Augmented Agents](https://arxiv.org/abs/2606.30531v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [MAS-Lab: A Specification-Driven Validation Framework for Reliable Multi-Agent Systems](https://arxiv.org/abs/2606.30546v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://arxiv.org/abs/2606.30560v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Morphing into Hybrid Attention Models](https://arxiv.org/abs/2606.30562v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Forensic Trajectory Signatures for Agent Memory Poisoning Detection](https://arxiv.org/abs/2606.30566v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions](https://arxiv.org/abs/2606.30573v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [MESA: Prioritizing Vulnerable Communication Channels for Securing Multi-Agent Systems](https://arxiv.org/abs/2606.30602v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Scaling the Horizon, Not the Parameters: Reaching Trillion-Parameter Performance with a 35B Agent](https://arxiv.org/abs/2606.30616v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Pessimism's Paradox: Conservative Offline Training Amplifies Reward Hacking During Online Adaptation in Reasoning Models](https://arxiv.org/abs/2606.30627v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [One-Step Gradient Delay is Not a Barrier for Large-Scale Asynchronous Pipeline Parallel LLM Pretraining](https://arxiv.org/abs/2606.30634v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Self-Evolving World Models for LLM Agent Planning](https://arxiv.org/abs/2606.30639v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents](https://arxiv.org/abs/2606.30697v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [From Search to Synthesis: Training LLMs as Zero-Shot Workflow Generators](https://arxiv.org/abs/2606.30704v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [What Drives Interactive Improvement from Feedback?](https://arxiv.org/abs/2606.30774v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [A Single Rewrite Suffices: Empirical Lessons from Production Skill Description Optimization](https://arxiv.org/abs/2606.30775v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense](https://arxiv.org/abs/2606.30783v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Revocable Learned State via Process Sidecars](https://arxiv.org/abs/2606.30788v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Predictable GRPO: A Closed-Form Model of Training Dynamics](https://arxiv.org/abs/2606.30789v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Using AI Agents to Automate Black-Box Audits of Personalization Algorithms at Scale](https://arxiv.org/abs/2606.30801v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs](https://arxiv.org/abs/2606.30814v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [BayesBench: Evaluating LLM Belief Trajectories Under Multi-Turn Evidence Accumulation](https://arxiv.org/abs/2606.30850v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [When Does Learning to Stop Help? A Cost-Aware Study of Early Exits in Reasoning Models](https://arxiv.org/abs/2606.30852v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Curvature-Guided Module Localization for Low-Rank Detoxification of Backdoored Large Language Models](https://arxiv.org/abs/2606.30899v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Why Solve It Twice? Hierarchical Accumulation of Skills for Transfer-Efficient ML Engineering](https://arxiv.org/abs/2606.30911v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Budget-Adaptive Routing: Skipping the Weak When the Strong Answers Anyway](https://arxiv.org/abs/2606.30919v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [RoPoLL: Robust Panel of LLM Judges](https://arxiv.org/abs/2606.30931v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Beyond Compilation: Evaluating Faithful Natural-Language-to-Lean Statement Formalization](https://arxiv.org/abs/2606.31002v1) — first-public（Asia/Shanghai）：2026-06-29；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
