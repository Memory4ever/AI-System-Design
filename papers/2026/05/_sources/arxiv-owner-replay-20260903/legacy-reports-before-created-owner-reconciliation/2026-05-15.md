# Daily Research — 2026-05-15

**Research Date:** 2026-05-15

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-14 09:00:00 ～ 2026-05-15 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。13/13 Books writeback 已由不同 reviewer 完成 post-write semantic audit，未发现未解决 finding。

## Executive Summary

相邻月份 v2 snapshot 含 91,841 条 raw records；严格窗口注册 668 条 identity。非作者重放 668/668 title+abstract 后，将 author denominator 29 修复为 56（恢复 27 个 false negative、移除 0 个 false positive），冻结 612 项 family-specific pre-denominator closure。56/56 official exact-v1 已读取，blocked=0、ordinary pending=0。current Books challenge 将 15 项 provisional Integrate 收紧为 13 项 root-writeback-ready queue；共享 Books 尚未写，因此 Completion 仍为 In Progress。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-15 |
| Window End | 2026-05-15 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260515-INDEPENDENT-56 |
| Denominator Frozen At | 2026-09-01T10:10:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-14T09:00:00+08:00 | 2026-05-15T09:00:00+08:00 | 2026-09-01T10:10:00+08:00 | DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML/PDF | checked | 668 | SF-2026-ARXIV-2605-14241;SF-2026-ARXIV-2605-14249;SF-2026-ARXIV-2605-14271;SF-2026-ARXIV-2605-14290;SF-2026-ARXIV-2605-14305;SF-2026-ARXIV-2605-14415;SF-2026-ARXIV-2605-14421;SF-2026-ARXIV-2605-14460;SF-2026-ARXIV-2605-14473;SF-2026-ARXIV-2605-14483;SF-2026-ARXIV-2605-14498;SF-2026-ARXIV-2605-14514;SF-2026-ARXIV-2605-14570;SF-2026-ARXIV-2605-14591;SF-2026-ARXIV-2605-14636;SF-2026-ARXIV-2605-14678;SF-2026-ARXIV-2605-14744;SF-2026-ARXIV-2605-14747;SF-2026-ARXIV-2605-14786;SF-2026-ARXIV-2605-14859;SF-2026-ARXIV-2605-14865;SF-2026-ARXIV-2605-14906;SF-2026-ARXIV-2605-14932;SF-2026-ARXIV-2605-14968;SF-2026-ARXIV-2605-14978;SF-2026-ARXIV-2605-15030;SF-2026-ARXIV-2605-15034;SF-2026-ARXIV-2605-15051;SF-2026-ARXIV-2605-15079;SF-2026-ARXIV-2605-15100;SF-2026-ARXIV-2605-15109;SF-2026-ARXIV-2605-15118;SF-2026-ARXIV-2605-15128;SF-2026-ARXIV-2605-15132;SF-2026-ARXIV-2605-15138;SF-2026-ARXIV-2605-15152;SF-2026-ARXIV-2605-15155;SF-2026-ARXIV-2605-15164;SF-2026-ARXIV-2605-15172;SF-2026-ARXIV-2605-15178;SF-2026-ARXIV-2605-15184;SF-2026-ARXIV-2605-15185;SF-2026-ARXIV-2605-15188;SF-2026-ARXIV-2605-15238;SF-2026-ARXIV-2605-15257;SF-2026-ARXIV-2605-15338;SF-2026-ARXIV-2605-15377;SF-2026-ARXIV-2605-15384;SF-2026-ARXIV-2605-15403;SF-2026-ARXIV-2605-15422;SF-2026-ARXIV-2605-15425;SF-2026-ARXIV-2605-15466;SF-2026-ARXIV-2605-15477;SF-2026-ARXIV-2605-16436;SF-2026-ARXIV-2605-16439;SF-2026-ARXIV-2605-18859 | pages=100; final_cursor=end; raw=91841; registered=668; screened=668; retained=56; closure=612 | 2026-05-15T00:59:59Z | screening-ledger-final.json#sha256=c9fd7e05f74800a6599332f1c39dc1c8c3748b5ecbb1492b21432f110b104ffa | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260515:start -->668/668 registered identity 已完成 title+abstract 语义筛选；不同 reviewer 已完成 false-positive/false-negative challenge，最终 56 个候选完成 exact-v1，blocked=0。Coverage 与 Evidence 均已闭合。<!-- coverage:SRC-ARXIV:20260515:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-14241 | arXiv:2605.14241v1 | paper-v1:2605.14241 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-14241 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-14241 | no |
| SF-2026-ARXIV-2605-14249 | arXiv:2605.14249v1 | paper-v1:2605.14249 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14249 | self | — | new_in_window | PLATFORM-COST | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14249 | no |
| SF-2026-ARXIV-2605-14271 | arXiv:2605.14271v1 | paper-v1:2605.14271 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14271 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14271 | no |
| SF-2026-ARXIV-2605-14290 | arXiv:2605.14290v1 | paper-v1:2605.14290 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14290 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14290 | no |
| SF-2026-ARXIV-2605-14305 | arXiv:2605.14305v1 | paper-v1:2605.14305 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14305 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14305 | no |
| SF-2026-ARXIV-2605-14415 | arXiv:2605.14415v1 | paper-v1:2605.14415 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14415 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14415 | no |
| SF-2026-ARXIV-2605-14421 | arXiv:2605.14421v1 | paper-v1:2605.14421 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-14421 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-14421 | no |
| SF-2026-ARXIV-2605-14460 | arXiv:2605.14460v1 | paper-v1:2605.14460 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14460 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14460 | no |
| SF-2026-ARXIV-2605-14473 | arXiv:2605.14473v1 | paper-v1:2605.14473 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14473 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14473 | no |
| SF-2026-ARXIV-2605-14483 | arXiv:2605.14483v1 | paper-v1:2605.14483 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14483 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14483 | no |
| SF-2026-ARXIV-2605-14498 | arXiv:2605.14498v1 | paper-v1:2605.14498 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14498 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14498 | no |
| SF-2026-ARXIV-2605-14514 | arXiv:2605.14514v1 | paper-v1:2605.14514 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14514 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14514 | no |
| SF-2026-ARXIV-2605-14570 | arXiv:2605.14570v1 | paper-v1:2605.14570 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14570 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14570 | no |
| SF-2026-ARXIV-2605-14591 | arXiv:2605.14591v1 | paper-v1:2605.14591 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14591 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14591 | no |
| SF-2026-ARXIV-2605-14636 | arXiv:2605.14636v1 | paper-v1:2605.14636 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14636 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14636 | no |
| SF-2026-ARXIV-2605-14678 | arXiv:2605.14678v1 | paper-v1:2605.14678 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14678 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14678 | no |
| SF-2026-ARXIV-2605-14744 | arXiv:2605.14744v1 | paper-v1:2605.14744 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14744 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14744 | no |
| SF-2026-ARXIV-2605-14747 | arXiv:2605.14747v1 | paper-v1:2605.14747 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14747 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14747 | no |
| SF-2026-ARXIV-2605-14786 | arXiv:2605.14786v1 | paper-v1:2605.14786 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14786 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14786 | no |
| SF-2026-ARXIV-2605-14859 | arXiv:2605.14859v1 | paper-v1:2605.14859 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14859 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14859 | no |
| SF-2026-ARXIV-2605-14865 | arXiv:2605.14865v1 | paper-v1:2605.14865 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14865 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14865 | no |
| SF-2026-ARXIV-2605-14906 | arXiv:2605.14906v1 | paper-v1:2605.14906 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14906 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14906 | no |
| SF-2026-ARXIV-2605-14932 | arXiv:2605.14932v1 | paper-v1:2605.14932 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14932 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14932 | no |
| SF-2026-ARXIV-2605-14968 | arXiv:2605.14968v1 | paper-v1:2605.14968 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14968 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14968 | no |
| SF-2026-ARXIV-2605-14978 | arXiv:2605.14978v1 | paper-v1:2605.14978 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-14978 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14978 | no |
| SF-2026-ARXIV-2605-15030 | arXiv:2605.15030v1 | paper-v1:2605.15030 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15030 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15030 | no |
| SF-2026-ARXIV-2605-15034 | arXiv:2605.15034v1 | paper-v1:2605.15034 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15034 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15034 | no |
| SF-2026-ARXIV-2605-15051 | arXiv:2605.15051v1 | paper-v1:2605.15051 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15051 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2605-15051 | no |
| SF-2026-ARXIV-2605-15079 | arXiv:2605.15079v1 | paper-v1:2605.15079 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15079 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-15079 | no |
| SF-2026-ARXIV-2605-15100 | arXiv:2605.15100v1 | paper-v1:2605.15100 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15100 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15100 | no |
| SF-2026-ARXIV-2605-15109 | arXiv:2605.15109v1 | paper-v1:2605.15109 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15109 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-15109 | no |
| SF-2026-ARXIV-2605-15118 | arXiv:2605.15118v1 | paper-v1:2605.15118 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15118 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15118 | no |
| SF-2026-ARXIV-2605-15128 | arXiv:2605.15128v1 | paper-v1:2605.15128 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15128 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15128 | no |
| SF-2026-ARXIV-2605-15132 | arXiv:2605.15132v1 | paper-v1:2605.15132 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15132 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-15132 | no |
| SF-2026-ARXIV-2605-15138 | arXiv:2605.15138v1 | paper-v1:2605.15138 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15138 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15138 | no |
| SF-2026-ARXIV-2605-15152 | arXiv:2605.15152v1 | paper-v1:2605.15152 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15152 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15152 | no |
| SF-2026-ARXIV-2605-15155 | arXiv:2605.15155v1 | paper-v1:2605.15155 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15155 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15155 | no |
| SF-2026-ARXIV-2605-15164 | arXiv:2605.15164v1 | paper-v1:2605.15164 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15164 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15164 | no |
| SF-2026-ARXIV-2605-15172 | arXiv:2605.15172v1 | paper-v1:2605.15172 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15172 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15172 | no |
| SF-2026-ARXIV-2605-15178 | arXiv:2605.15178v1 | paper-v1:2605.15178 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15178 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15178 | no |
| SF-2026-ARXIV-2605-15184 | arXiv:2605.15184v1 | paper-v1:2605.15184 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15184 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15184 | no |
| SF-2026-ARXIV-2605-15185 | arXiv:2605.15185v1 | paper-v1:2605.15185 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15185 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-15185 | no |
| SF-2026-ARXIV-2605-15188 | arXiv:2605.15188v1 | paper-v1:2605.15188 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15188 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15188 | no |
| SF-2026-ARXIV-2605-15238 | arXiv:2605.15238v1 | paper-v1:2605.15238 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15238 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-15238 | no |
| SF-2026-ARXIV-2605-15257 | arXiv:2605.15257v1 | paper-v1:2605.15257 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15257 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15257 | no |
| SF-2026-ARXIV-2605-15338 | arXiv:2605.15338v1 | paper-v1:2605.15338 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15338 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15338 | no |
| SF-2026-ARXIV-2605-15377 | arXiv:2605.15377v1 | paper-v1:2605.15377 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15377 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15377 | no |
| SF-2026-ARXIV-2605-15384 | arXiv:2605.15384v1 | paper-v1:2605.15384 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15384 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-15384 | no |
| SF-2026-ARXIV-2605-15403 | arXiv:2605.15403v1 | paper-v1:2605.15403 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15403 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15403 | no |
| SF-2026-ARXIV-2605-15422 | arXiv:2605.15422v1 | paper-v1:2605.15422 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15422 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15422 | no |
| SF-2026-ARXIV-2605-15425 | arXiv:2605.15425v1 | paper-v1:2605.15425 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15425 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15425 | no |
| SF-2026-ARXIV-2605-15466 | arXiv:2605.15466v1 | paper-v1:2605.15466 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15466 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15466 | no |
| SF-2026-ARXIV-2605-15477 | arXiv:2605.15477v1 | paper-v1:2605.15477 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15477 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15477 | no |
| SF-2026-ARXIV-2605-16436 | arXiv:2605.16436v1 | paper-v1:2605.16436 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16436 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16436 | no |
| SF-2026-ARXIV-2605-16439 | arXiv:2605.16439v1 | paper-v1:2605.16439 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16439 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16439 | no |
| SF-2026-ARXIV-2605-18859 | arXiv:2605.18859v1 | paper-v1:2605.18859 | 2026-W20 | 2026-05-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18859 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-18859 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-14241 | RP-f7b4d8498d4dac8c | deep | arXiv:2605.14241v1 | SRC-ARXIV@arXiv:2605.14241v1 | https://arxiv.org/html/2605.14241v1 §3 LQM-ContextRoute — mechanism boundary: Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface. | https://arxiv.org/html/2605.14241v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14241v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14241v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14241 | complete |
| SF-2026-ARXIV-2605-14249 | RP-9564507a365375ca | deep | arXiv:2605.14249v1 | SRC-ARXIV@arXiv:2605.14249v1 | https://arxiv.org/html/2605.14249v1 §3 EnergyLens Methodology — mechanism boundary: We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization. | https://arxiv.org/html/2605.14249v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14249v1 §5 Discussion and limitations disclosed by evaluated hardware/configuration space — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14249v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14249 | complete |
| SF-2026-ARXIV-2605-14271 | RP-73abaecdcf7c4fda | deep | arXiv:2605.14271v1 | SRC-ARXIV@arXiv:2605.14271v1 | https://arxiv.org/html/2605.14271v1 §4.1 Task Design; HarnessAudit-Bench — mechanism boundary: LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components. | https://arxiv.org/html/2605.14271v1 §5 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14271v1 §6 Discussion and disclosed harness/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14271v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14271 | complete |
| SF-2026-ARXIV-2605-14290 | RP-150c3930a688ebff | deep | arXiv:2605.14290v1 | SRC-ARXIV@arXiv:2605.14290v1 | https://arxiv.org/html/2605.14290v1 §2.1 Threat Model; §4 Plan-Then-Execute Web Agents; §5 Expressivity — mechanism boundary: ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm. | https://arxiv.org/html/2605.14290v1 §6.1 Task Taxonomy; §6.2 WebArena empirical analysis — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14290v1 §6.3 Practical Gaps; §7 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14290v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14290 | complete |
| SF-2026-ARXIV-2605-14305 | RP-ab813ae15840a4ea | deep | arXiv:2605.14305v1 | SRC-ARXIV@arXiv:2605.14305v1 | https://arxiv.org/html/2605.14305v1 §3 Factorization-Error-Free DLLM — mechanism boundary: Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions. | https://arxiv.org/html/2605.14305v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14305v1 §4 Ablation and device/workload boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14305v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14305 | complete |
| SF-2026-ARXIV-2605-14415 | RP-cc35d74a484767b2 | deep | arXiv:2605.14415v1 | SRC-ARXIV@arXiv:2605.14415v1 | https://arxiv.org/html/2605.14415v1 §2 SWE-Chain construction; §3.1–§3.2 agent execution — mechanism boundary: Coding agents powered by large language models are increasingly expected to perform realistic software maintenance tasks beyond isolated issue resolution. | https://arxiv.org/html/2605.14415v1 §3.3 Evaluation; §4 Results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14415v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14415v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14415 | complete |
| SF-2026-ARXIV-2605-14421 | RP-d451e20a6dbf9130 | deep | arXiv:2605.14421v1 | SRC-ARXIV@arXiv:2605.14421v1 | https://arxiv.org/html/2605.14421v1 §2 Threat Model; §3 MemLineage Design — mechanism boundary: We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry. | https://arxiv.org/html/2605.14421v1 §6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14421v1 §8 Discussion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14421v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14421 | complete |
| SF-2026-ARXIV-2605-14460 | RP-e64825f6318e2777 | deep | arXiv:2605.14460v1 | SRC-ARXIV@arXiv:2605.14460v1 | https://arxiv.org/html/2605.14460v1 §3 Payload-less Skill Attack and Audit Method — mechanism boundary: Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces. | https://arxiv.org/html/2605.14460v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14460v1 §6.3 Threats to Validity and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14460v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14460 | complete |
| SF-2026-ARXIV-2605-14473 | RP-c96c6ae36796edd3 | deep | arXiv:2605.14473v1 | SRC-ARXIV@arXiv:2605.14473v1 | https://arxiv.org/html/2605.14473v1 §3 Context-Driven Decomposition — mechanism boundary: Retrieval-Augmented Generation (RAG) is usually evaluated by whether the final answer is correct. | https://arxiv.org/html/2605.14473v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14473v1 §6 Limitations and conflict-dataset/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14473v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14473 | complete |
| SF-2026-ARXIV-2605-14483 | RP-99afed6f5269ff01 | deep | arXiv:2605.14483v1 | SRC-ARXIV@arXiv:2605.14483v1 | https://arxiv.org/html/2605.14483v1 §3 LEMON Counterfactual Orchestration — mechanism boundary: Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design. | https://arxiv.org/html/2605.14483v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14483v1 Appendix B Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14483v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14483 | complete |
| SF-2026-ARXIV-2605-14498 | RP-599dd39af7321629 | deep | arXiv:2605.14498v1 | SRC-ARXIV@arXiv:2605.14498v1 | https://arxiv.org/html/2605.14498v1 §3 GroupMemBench construction; §3.2 question taxonomy — mechanism boundary: Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations. | https://arxiv.org/html/2605.14498v1 §4 Evaluation; Appendix I judge reliability — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14498v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14498v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14498 | complete |
| SF-2026-ARXIV-2605-14514 | RP-f6088adfb67e7481 | deep | arXiv:2605.14514v1 | SRC-ARXIV@arXiv:2605.14514v1 | https://arxiv.org/html/2605.14514v1 §3 ConflictEval pairwise sequential-defense framework — mechanism boundary: Large Language Models (LLMs) deployed in high-stakes applications must simultaneously manage multiple risks, yet existing defenses are almost exclusively evaluated in isolation under a one-shot deployment assumption. | https://arxiv.org/html/2605.14514v1 §4 Results; §5 mechanistic analysis; Appendix B configurations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14514v1 §5 Limitations paragraph — pairwise/six-defense/three-family boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14514v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14514 | complete |
| SF-2026-ARXIV-2605-14570 | RP-e24d1bf7a78702fa | deep | arXiv:2605.14570v1 | SRC-ARXIV@arXiv:2605.14570v1 | https://arxiv.org/html/2605.14570v1 §3 Denoising-trajectory uncertainty signals — mechanism boundary: Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism. | https://arxiv.org/html/2605.14570v1 §4 Experiments and calibration — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14570v1 Appendix E Limitations; perfect-calibration/semantic-measure assumptions and sampled-model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14570v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14570 | complete |
| SF-2026-ARXIV-2605-14591 | RP-38b1f2b51f7a3cb5 | deep | arXiv:2605.14591v1 | SRC-ARXIV@arXiv:2605.14591v1 | https://arxiv.org/html/2605.14591v1 §3 Zero-Run Privacy Audit — mechanism boundary: Privacy auditing provides empirical lower bounds on the differential privacy parameters of learning algorithms. | https://arxiv.org/html/2605.14591v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14591v1 §9 Limitations and Conclusion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14591v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14591 | complete |
| SF-2026-ARXIV-2605-14636 | RP-8914e7f511b56c1a | deep | arXiv:2605.14636v1 | SRC-ARXIV@arXiv:2605.14636v1 | https://arxiv.org/html/2605.14636v1 §3 Temporal Critique Fine-tuning — mechanism boundary: Large language models (LLMs) often fail to reason under temporal cutoffs: when prompted to answer from the standpoint of an earlier time, they exploit knowledge that became available only later. | https://arxiv.org/html/2605.14636v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14636v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14636v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14636 | complete |
| SF-2026-ARXIV-2605-14678 | RP-14a81ce93ca25c5c | deep | arXiv:2605.14678v1 | SRC-ARXIV@arXiv:2605.14678v1 | https://arxiv.org/html/2605.14678v1 §3 π-Bench task/persona/hidden-intent construction — mechanism boundary: The rise of personal assistant agents, e.g., OpenClaw, highlights the growing potential of large language models to support users across everyday life and work. | https://arxiv.org/html/2605.14678v1 §4 Evaluation and long-horizon trajectories — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14678v1 §6 Limitations — simulated users and single Nanobot-derived scaffold boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14678v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14678 | complete |
| SF-2026-ARXIV-2605-14744 | RP-b282da0d0dcddd2a | deep | arXiv:2605.14744v1 | SRC-ARXIV@arXiv:2605.14744v1 | https://arxiv.org/html/2605.14744v1 §3 Methodology; §3.2 Mechanical Policy; §3.3 Governance Metrics — mechanism boundary: Large language models in regulated financial workflows are governed by natural-language policies that the same model interprets, creating a principal--agent failure: outputs can appear compliant without being compliant. | https://arxiv.org/html/2605.14744v1 §4 Experiments and Results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14744v1 §5 Discussion/Conclusion; no dedicated limitations section — synthetic banking, single-model-family and ground-truth-rule boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14744v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14744 | complete |
| SF-2026-ARXIV-2605-14747 | RP-60175f443e4cc738 | deep | arXiv:2605.14747v1 | SRC-ARXIV@arXiv:2605.14747v1 | https://arxiv.org/html/2605.14747v1 §3 Video2GUI coarse-to-fine pipeline; §4 WildGUI construction — mechanism boundary: Recent advances in multimodal large language models have driven growing interest in graphical user interface (GUI) agents, yet their generalization remains constrained by the scarcity of large-scale training data spanning diverse real-world applications. | https://arxiv.org/html/2605.14747v1 §5 Pretraining and GUI benchmark evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14747v1 Conclusion and appendix data-quality analyses; no dedicated limitations section — automatic grounding/filter and executable-validation coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14747v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14747 | complete |
| SF-2026-ARXIV-2605-14786 | RP-42683edae586ba52 | deep | arXiv:2605.14786v1 | SRC-ARXIV@arXiv:2605.14786v1 | https://arxiv.org/html/2605.14786v1 §3 Threat model and passive UI-trace fingerprinting — mechanism boundary: As LLM-based agents increasingly browse the web on users' behalf, a natural question arises: can websites passively identify which underlying model powers an agent? | https://arxiv.org/html/2605.14786v1 §4–§5 Cross-model/environment evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14786v1 §6 Limitations and adaptive-attacker/retraining boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14786v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14786 | complete |
| SF-2026-ARXIV-2605-14859 | RP-f72e5cf7a8da4c65 | deep | arXiv:2605.14859v1 | SRC-ARXIV@arXiv:2605.14859v1 | https://arxiv.org/html/2605.14859v1 §3 AuthBench and Permission-Boundary Inference — mechanism boundary: As coding agents gain access to shells, repositories, and user files, least-privilege authorization becomes a prerequisite for safe deployment: an agent should receive enough authority to complete the task, without unnecessary authority that exposes sensitive surfaces. | https://arxiv.org/html/2605.14859v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14859v1 Appendix B Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14859 | complete |
| SF-2026-ARXIV-2605-14865 | RP-d8343f5442efcf09 | deep | arXiv:2605.14865v1 | SRC-ARXIV@arXiv:2605.14865v1 | https://arxiv.org/html/2605.14865v1 §3 Top-down and span-level diagnostic framework — mechanism boundary: AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces. | https://arxiv.org/html/2605.14865v1 §4 TRAIL/GAIA/SWE-Bench evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14865v1 §5 Limitations and evaluator/model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14865v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14865 | complete |
| SF-2026-ARXIV-2605-14906 | RP-ea81fd92e73923d8 | deep | arXiv:2605.14906v1 | SRC-ARXIV@arXiv:2605.14906v1 | https://arxiv.org/html/2605.14906v1 §3 MemLens construction and visual-evidence requirements — mechanism boundary: Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents. | https://arxiv.org/html/2605.14906v1 §4 Evaluation across memory systems — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14906v1 §6 Limitations — synthetic conversation, judge and modality/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14906v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14906 | complete |
| SF-2026-ARXIV-2605-14932 | RP-9a0d74baf6c1575b | deep | arXiv:2605.14932v1 | SRC-ARXIV@arXiv:2605.14932v1 | https://arxiv.org/html/2605.14932v1 §3 Agent-as-OS Security Model — mechanism boundary: Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments. | https://arxiv.org/html/2605.14932v1 §4–§5 Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14932v1 §VI Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14932v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14932 | complete |
| SF-2026-ARXIV-2605-14968 | RP-7c5df7351439ec8d | deep | arXiv:2605.14968v1 | SRC-ARXIV@arXiv:2605.14968v1 | https://arxiv.org/html/2605.14968v1 official PDF pp. 2–11 §1.3–§1.8 diagram-as-specification, contracts, runtime and formal semantics — mechanism boundary: GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes. | https://arxiv.org/html/2605.14968v1 official PDF pp. 12–15 §1.12 Evaluation Plan; §1.13 Empirical Evaluation; §2 Implementation Status — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14968v1 official PDF pp. 11–15 §1.10 Failure Modes and Limitations; §1.13.6 Interpretation and Limitations — verified core not deployed/evaluated — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14968v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14968 | complete |
| SF-2026-ARXIV-2605-14978 | RP-5ae3f63f67c4a1e2 | deep | arXiv:2605.14978v1 | SRC-ARXIV@arXiv:2605.14978v1 | https://arxiv.org/html/2605.14978v1 §3 Adaptive-window policy optimization — mechanism boundary: Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model. | https://arxiv.org/html/2605.14978v1 §4 Serving evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.14978v1 §5 Limitations and workload/hardware/generalization boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.14978v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-14978 | complete |
| SF-2026-ARXIV-2605-15030 | RP-48328170dd5535c8 | deep | arXiv:2605.15030v1 | SRC-ARXIV@arXiv:2605.15030v1 | https://arxiv.org/html/2605.15030v1 §3 Problem; §4 Data; §5 WARD Training — mechanism boundary: Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces. | https://arxiv.org/html/2605.15030v1 §6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15030v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15030v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15030 | complete |
| SF-2026-ARXIV-2605-15034 | RP-f2167392f7250057 | deep | arXiv:2605.15034v1 | SRC-ARXIV@arXiv:2605.15034v1 | https://arxiv.org/html/2605.15034v1 §3 Watched/unwatched experimental design — mechanism boundary: Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored. | https://arxiv.org/html/2605.15034v1 §4 Strategic-behavior results — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15034v1 §5 Limitations and model/task/context boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15034v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15034 | complete |
| SF-2026-ARXIV-2605-15051 | RP-39397685917c51bd | deep | arXiv:2605.15051v1 | SRC-ARXIV@arXiv:2605.15051v1 | https://arxiv.org/html/2605.15051v1 §3 Interpretable Serving Latency Model — mechanism boundary: Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel. | https://arxiv.org/html/2605.15051v1 §4 Validation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15051v1 §5 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15051v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15051 | complete |
| SF-2026-ARXIV-2605-15079 | RP-20756aca99fac991 | deep | arXiv:2605.15079v1 | SRC-ARXIV@arXiv:2605.15079v1 | https://arxiv.org/html/2605.15079v1 §3 Croissant Baker Pipeline — mechanism boundary: Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms. | https://arxiv.org/html/2605.15079v1 §4–§5 Evaluation and Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15079v1 §6 Failure Modes and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15079v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15079 | complete |
| SF-2026-ARXIV-2605-15100 | RP-73e6b6ea4d489390 | deep | arXiv:2605.15100v1 | SRC-ARXIV@arXiv:2605.15100v1 | https://arxiv.org/html/2605.15100v1 §3 Dual-dimensional adaptive inference policy — mechanism boundary: Large Language Models (LLMs) have demonstrated remarkable abilities in reasoning. | https://arxiv.org/html/2605.15100v1 §4 Budget-quality evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15100v1 §5 Limitations and model/task/SLO boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15100v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15100 | complete |
| SF-2026-ARXIV-2605-15109 | RP-700dc07146377af1 | deep | arXiv:2605.15109v1 | SRC-ARXIV@arXiv:2605.15109v1 | https://arxiv.org/html/2605.15109v1 §3 Traversal Context and Provenance — mechanism boundary: Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. | https://arxiv.org/html/2605.15109v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15109v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15109v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15109 | complete |
| SF-2026-ARXIV-2605-15118 | RP-c21971a6fe582521 | deep | arXiv:2605.15118v1 | SRC-ARXIV@arXiv:2605.15118v1 | https://arxiv.org/html/2605.15118v1 §3 Threat taxonomy and Target×Technique matrix — mechanism boundary: We introduce a reusable framework for auditing whether LLM attack benchmarks collectively cover the threat surface: a 4$\times$6 Target $\times$ Technique matrix grounded in STRIDE, constructed from a 507-leaf taxonomy -- 401 data-populated and 106 threat-model-derived leaves -- of inference-time attacks extracted from 932 arXiv security studies (2023--2026). | https://arxiv.org/html/2605.15118v1 §4 Cross-benchmark coverage audit — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15118v1 §5 Limitations and literature/labeling coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15118v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15118 | complete |
| SF-2026-ARXIV-2605-15128 | RP-ec8bc6dc0ee33c77 | deep | arXiv:2605.15128v1 | SRC-ARXIV@arXiv:2605.15128v1 | https://arxiv.org/html/2605.15128v1 §3 MemEye framework and benchmark construction — mechanism boundary: Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning. | https://arxiv.org/html/2605.15128v1 §4 Evaluation of 13 memory methods — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15128v1 §6 Limitations — life-scenario, judge and visual-tool boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15128v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15128 | complete |
| SF-2026-ARXIV-2605-15132 | RP-b2b03d59d57151fd | deep | arXiv:2605.15132v1 | SRC-ARXIV@arXiv:2605.15132v1 | https://arxiv.org/html/2605.15132v1 §3 APWA Architecture — mechanism boundary: Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. | https://arxiv.org/html/2605.15132v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15132v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15132v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15132 | complete |
| SF-2026-ARXIV-2605-15138 | RP-265270f5c4626439 | deep | arXiv:2605.15138v1 | SRC-ARXIV@arXiv:2605.15138v1 | https://arxiv.org/html/2605.15138v1 §3 MANSU circuit attribution and null-space update — mechanism boundary: Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first. | https://arxiv.org/html/2605.15138v1 §4 Full-precision and NF4 evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15138v1 §6 Limitations and model/quantizer/forget-set boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15138v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15138 | complete |
| SF-2026-ARXIV-2605-15152 | RP-53bb6767dbf442af | deep | arXiv:2605.15152v1 | SRC-ARXIV@arXiv:2605.15152v1 | https://arxiv.org/html/2605.15152v1 official PDF pp. 3–5 §3.1–§3.3 Target Quantizations, Threat Model and Outlier Injection — mechanism boundary: LLM quantization has become essential for memory-efficient deployment. | https://arxiv.org/html/2605.15152v1 official PDF pp. 5–11 §4 Evaluation, defenses and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15152v1 official PDF p. 13 Appendix A Limitations and Future Work — excludes 70B models and specialized quantization/hardware — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15152v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15152 | complete |
| SF-2026-ARXIV-2605-15155 | RP-1b6866403f435f26 | deep | arXiv:2605.15155v1 | SRC-ARXIV@arXiv:2605.15155v1 | https://arxiv.org/html/2605.15155v1 §3 SDAR gated on-policy self-distillation — mechanism boundary: Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction. | https://arxiv.org/html/2605.15155v1 §4–§5 Agent-environment evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15155v1 Appendix limitations, hyperparameters and event-time artifact boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15155v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15155 | complete |
| SF-2026-ARXIV-2605-15164 | RP-c27ff8ebbee500b7 | deep | arXiv:2605.15164v1 | SRC-ARXIV@arXiv:2605.15164v1 | https://arxiv.org/html/2605.15164v1 §2–§7 Behavioural Assurance Analysis — mechanism boundary: This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. | https://arxiv.org/html/2605.15164v1 §7 Pilot Evidence — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15164v1 §8 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15164v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15164 | complete |
| SF-2026-ARXIV-2605-15172 | RP-a62ac9a7b72d5db6 | deep | arXiv:2605.15172v1 | SRC-ARXIV@arXiv:2605.15172v1 | https://arxiv.org/html/2605.15172v1 §3 MetaBackdoor positional-trigger construction — mechanism boundary: Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications. | https://arxiv.org/html/2605.15172v1 §4 Cross-model/position-encoding evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15172v1 §6 Limitations and trigger/architecture boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15172v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15172 | complete |
| SF-2026-ARXIV-2605-15178 | RP-1526fbc80433ea00 | deep | arXiv:2605.15178v1 | SRC-ARXIV@arXiv:2605.15178v1 | https://arxiv.org/html/2605.15178v1 §3 SANA-WM architecture; §4 data and camera annotation — mechanism boundary: We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control. | https://arxiv.org/html/2605.15178v1 §5 Generation/control evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15178v1 §6 Limitations and video-generation/world-model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15178v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15178 | complete |
| SF-2026-ARXIV-2605-15184 | RP-d0a637714b316238 | deep | arXiv:2605.15184v1 | SRC-ARXIV@arXiv:2605.15184v1 | https://arxiv.org/html/2605.15184v1 §3 Harness and Retrieval Conditions — mechanism boundary: Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. | https://arxiv.org/html/2605.15184v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15184v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15184v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15184 | complete |
| SF-2026-ARXIV-2605-15185 | RP-a99a5cf4755519ff | deep | arXiv:2605.15185v1 | SRC-ARXIV@arXiv:2605.15185v1 | https://arxiv.org/html/2605.15185v1 §3 PDI-Bench Methodology — mechanism boundary: Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. | https://arxiv.org/html/2605.15185v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15185v1 Appendix G Limitations and Future Directions — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15185v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15185 | complete |
| SF-2026-ARXIV-2605-15188 | RP-f194612a5c78774c | deep | arXiv:2605.15188v1 | SRC-ARXIV@arXiv:2605.15188v1 | https://arxiv.org/html/2605.15188v1 §3 FutureSim chronological replay environment — mechanism boundary: AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. | https://arxiv.org/html/2605.15188v1 §4 Three-month agent evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.15188v1 §6 Limitations and news/source/forecasting boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.15188v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-15188 | complete |
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
| SF-2026-ARXIV-2605-16436 | RP-92445ffbb850d30a | deep | arXiv:2605.16436v1 | SRC-ARXIV@arXiv:2605.16436v1 | https://arxiv.org/html/2605.16436v1 §2–§5 Agentic Threat-Economics Analysis — mechanism boundary: For decades, the security of digital interaction has rested on an unacknowledged economic constraint. | https://arxiv.org/html/2605.16436v1 §3–§5 Case Analyses — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.16436v1 §6 Conclusion and position-paper evidence boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.16436v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16436 | complete |
| SF-2026-ARXIV-2605-16439 | RP-06f912e920440eca | deep | arXiv:2605.16439v1 | SRC-ARXIV@arXiv:2605.16439v1 | https://arxiv.org/html/2605.16439v1 §3 KVCapsule — mechanism boundary: Vision-Language Models (VLMs) have emerged as a critical and fast-growing extension of Large Language Models (LLMs) that enable multimodal reasoning through both text and image inputs. | https://arxiv.org/html/2605.16439v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.16439v1 §6 Conclusion and disclosed model/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.16439v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16439 | complete |
| SF-2026-ARXIV-2605-18859 | RP-35caa4f2dad6931c | deep | arXiv:2605.18859v1 | SRC-ARXIV@arXiv:2605.18859v1 | https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls. | https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration | https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO | https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-18859 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-14241:start -->
#### Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents

问题与演进：同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14241v1 §3 LQM-ContextRoute — mechanism boundary: Tool-augmented LLM agents increasingly access the same tool type through multiple functionally equivalent providers, such as web-search APIs, retrievers, or LLM backends exposed behind a shared interface.`。

Evaluation：`https://arxiv.org/html/2605.14241v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14241v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14241v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14241:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14241:end -->
<!-- review:SF-2026-ARXIV-2605-14241:end -->

<!-- review:SF-2026-ARXIV-2605-14249:start -->
#### EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization

问题与演进：多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14249v1 §3 EnergyLens Methodology — mechanism boundary: We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization.`。

Evaluation：`https://arxiv.org/html/2605.14249v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14249v1 §5 Discussion and limitations disclosed by evaluated hardware/configuration space — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14249v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14249:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14249:end -->
<!-- review:SF-2026-ARXIV-2605-14249:end -->

<!-- review:SF-2026-ARXIV-2605-14271:start -->
#### Auditing Agent Harness Safety

问题与演进：Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14271v1 §4.1 Task Design; HarnessAudit-Bench — mechanism boundary: LLM agents increasingly run inside execution harnesses that dispatch tools, allocate resources, and route messages between specialized components.`。

Evaluation：`https://arxiv.org/html/2605.14271v1 §5 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14271v1 §6 Discussion and disclosed harness/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14271v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14271:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14271:end -->
<!-- review:SF-2026-ARXIV-2605-14271:end -->

<!-- review:SF-2026-ARXIV-2605-14290:start -->
#### Web Agents Should Adopt the Plan-Then-Execute Paradigm

问题与演进：Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14290v1 §2.1 Threat Model; §4 Plan-Then-Execute Web Agents; §5 Expressivity — mechanism boundary: ReAct has become the default architecture across LLM agents, and many existing web agents follow this paradigm.`。

Evaluation：`https://arxiv.org/html/2605.14290v1 §6.1 Task Taxonomy; §6.2 WebArena empirical analysis — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14290v1 §6.3 Practical Gaps; §7 Discussion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14290v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14290:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14290:end -->
<!-- review:SF-2026-ARXIV-2605-14290:end -->

<!-- review:SF-2026-ARXIV-2605-14305:start -->
#### Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding

问题与演进：离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14305v1 §3 Factorization-Error-Free DLLM — mechanism boundary: Discrete diffusion language models improve generation efficiency through parallel token prediction, but standard $X_0$ prediction methods introduce factorization errors by approximating the clean token posterior with independent token-wise distributions.`。

Evaluation：`https://arxiv.org/html/2605.14305v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14305v1 §4 Ablation and device/workload boundary; no dedicated limitations section — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14305v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14305:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14305:end -->
<!-- review:SF-2026-ARXIV-2605-14305:end -->

<!-- review:SF-2026-ARXIV-2605-14415:start -->
#### SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades

问题与演进：coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14415v1 §2 SWE-Chain construction; §3.1–§3.2 agent execution — mechanism boundary: Coding agents powered by large language models are increasingly expected to perform realistic software maintenance tasks beyond isolated issue resolution.`。

Evaluation：`https://arxiv.org/html/2605.14415v1 §3.3 Evaluation; §4 Results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14415v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14415v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14415:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14415:end -->
<!-- review:SF-2026-ARXIV-2605-14415:end -->

<!-- review:SF-2026-ARXIV-2605-14421:start -->
#### MemLineage: Lineage-Guided Enforcement for LLM Agent Memory

问题与演进：持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14421v1 §2 Threat Model; §3 MemLineage Design — mechanism boundary: We introduce MemLineage, a defense for LLM agent memory that attaches both cryptographic provenance and LLM-mediated derivation lineage to every entry.`。

Evaluation：`https://arxiv.org/html/2605.14421v1 §6 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14421v1 §8 Discussion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14421v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14421:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14421:end -->
<!-- review:SF-2026-ARXIV-2605-14421:end -->

<!-- review:SF-2026-ARXIV-2605-14460:start -->
#### Exploiting LLM Agent Supply Chains via Payload-less Skills

问题与演进：skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14460v1 §3 Payload-less Skill Attack and Audit Method — mechanism boundary: Autonomous agents powered by Large Language Models (LLMs) acquire external functionalities through third-party skills available in open marketplaces.`。

Evaluation：`https://arxiv.org/html/2605.14460v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14460v1 §6.3 Threats to Validity and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14460v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14460:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14460:end -->
<!-- review:SF-2026-ARXIV-2605-14460:end -->

<!-- review:SF-2026-ARXIV-2605-14473:start -->
#### Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict

问题与演进：RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14473v1 §3 Context-Driven Decomposition — mechanism boundary: Retrieval-Augmented Generation (RAG) is usually evaluated by whether the final answer is correct.`。

Evaluation：`https://arxiv.org/html/2605.14473v1 §4 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14473v1 §6 Limitations and conflict-dataset/model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14473v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14473:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14473:end -->
<!-- review:SF-2026-ARXIV-2605-14473:end -->

<!-- review:SF-2026-ARXIV-2605-14483:start -->
#### LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning

问题与演进：Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14483v1 §3 LEMON Counterfactual Orchestration — mechanism boundary: Large language models (LLMs) have become a strong foundation for multi-agent systems, but their effectiveness depends heavily on orchestration design.`。

Evaluation：`https://arxiv.org/html/2605.14483v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14483v1 Appendix B Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14483v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14483:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14483:end -->
<!-- review:SF-2026-ARXIV-2605-14483:end -->

<!-- review:SF-2026-ARXIV-2605-14498:start -->
#### GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations

问题与演进：群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14498v1 §3 GroupMemBench construction; §3.2 question taxonomy — mechanism boundary: Large Language Model (LLM) agents increasingly serve as personal assistants and workplace collaborators, where their utility depends on memory systems that extract, retrieve, and apply information across long-running conversations.`。

Evaluation：`https://arxiv.org/html/2605.14498v1 §4 Evaluation; Appendix I judge reliability — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14498v1 Appendix K Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14498v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14498:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14498:end -->
<!-- review:SF-2026-ARXIV-2605-14498:end -->

<!-- review:SF-2026-ARXIV-2605-14514:start -->
#### Defenses at Odds: Measuring and Explaining Defense Conflicts in Large Language Models

问题与演进：模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14514v1 §3 ConflictEval pairwise sequential-defense framework — mechanism boundary: Large Language Models (LLMs) deployed in high-stakes applications must simultaneously manage multiple risks, yet existing defenses are almost exclusively evaluated in isolation under a one-shot deployment assumption.`。

Evaluation：`https://arxiv.org/html/2605.14514v1 §4 Results; §5 mechanistic analysis; Appendix B configurations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14514v1 §5 Limitations paragraph — pairwise/six-defense/three-family boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14514v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14514:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14514:end -->
<!-- review:SF-2026-ARXIV-2605-14514:end -->

<!-- review:SF-2026-ARXIV-2605-14570:start -->
#### Uncertainty Quantification for Large Language Diffusion Models

问题与演进：diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14570v1 §3 Denoising-trajectory uncertainty signals — mechanism boundary: Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism.`。

Evaluation：`https://arxiv.org/html/2605.14570v1 §4 Experiments and calibration — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14570v1 Appendix E Limitations; perfect-calibration/semantic-measure assumptions and sampled-model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14570v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14570:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14570:end -->
<!-- review:SF-2026-ARXIV-2605-14570:end -->

<!-- review:SF-2026-ARXIV-2605-14591:start -->
#### Privacy Auditing with Zero (0) Training Run

问题与演进：大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14591v1 §3 Zero-Run Privacy Audit — mechanism boundary: Privacy auditing provides empirical lower bounds on the differential privacy parameters of learning algorithms.`。

Evaluation：`https://arxiv.org/html/2605.14591v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14591v1 §9 Limitations and Conclusion — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14591v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14591:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14591:end -->
<!-- review:SF-2026-ARXIV-2605-14591:end -->

<!-- review:SF-2026-ARXIV-2605-14636:start -->
#### Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning

问题与演进：时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14636v1 §3 Temporal Critique Fine-tuning — mechanism boundary: Large language models (LLMs) often fail to reason under temporal cutoffs: when prompted to answer from the standpoint of an earlier time, they exploit knowledge that became available only later.`。

Evaluation：`https://arxiv.org/html/2605.14636v1 §4–§6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14636v1 §7 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14636v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14636:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14636:end -->
<!-- review:SF-2026-ARXIV-2605-14636:end -->

<!-- review:SF-2026-ARXIV-2605-14678:start -->
#### $π$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows

问题与演进：主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14678v1 §3 π-Bench task/persona/hidden-intent construction — mechanism boundary: The rise of personal assistant agents, e.g., OpenClaw, highlights the growing potential of large language models to support users across everyday life and work.`。

Evaluation：`https://arxiv.org/html/2605.14678v1 §4 Evaluation and long-horizon trajectories — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14678v1 §6 Limitations — simulated users and single Nanobot-derived scaffold boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14678v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14678:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14678:end -->
<!-- review:SF-2026-ARXIV-2605-14678:end -->

<!-- review:SF-2026-ARXIV-2605-14744:start -->
#### Mechanical Enforcement for LLM Governance:Evidence of Governance-Task Decoupling in Financial Decision Systems

问题与演进：治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14744v1 §3 Methodology; §3.2 Mechanical Policy; §3.3 Governance Metrics — mechanism boundary: Large language models in regulated financial workflows are governed by natural-language policies that the same model interprets, creating a principal--agent failure: outputs can appear compliant without being compliant.`。

Evaluation：`https://arxiv.org/html/2605.14744v1 §4 Experiments and Results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14744v1 §5 Discussion/Conclusion; no dedicated limitations section — synthetic banking, single-model-family and ground-truth-rule boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14744v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14744:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14744:end -->
<!-- review:SF-2026-ARXIV-2605-14744:end -->

<!-- review:SF-2026-ARXIV-2605-14747:start -->
#### Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining

问题与演进：GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14747v1 §3 Video2GUI coarse-to-fine pipeline; §4 WildGUI construction — mechanism boundary: Recent advances in multimodal large language models have driven growing interest in graphical user interface (GUI) agents, yet their generalization remains constrained by the scarcity of large-scale training data spanning diverse real-world applications.`。

Evaluation：`https://arxiv.org/html/2605.14747v1 §5 Pretraining and GUI benchmark evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14747v1 Conclusion and appendix data-quality analyses; no dedicated limitations section — automatic grounding/filter and executable-validation coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14747v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14747:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14747:end -->
<!-- review:SF-2026-ARXIV-2605-14747:end -->

<!-- review:SF-2026-ARXIV-2605-14786:start -->
#### Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces

问题与演进：browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14786v1 §3 Threat model and passive UI-trace fingerprinting — mechanism boundary: As LLM-based agents increasingly browse the web on users' behalf, a natural question arises: can websites passively identify which underlying model powers an agent?`。

Evaluation：`https://arxiv.org/html/2605.14786v1 §4–§5 Cross-model/environment evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14786v1 §6 Limitations and adaptive-attacker/retraining boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14786v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14786:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14786:end -->
<!-- review:SF-2026-ARXIV-2605-14786:end -->

<!-- review:SF-2026-ARXIV-2605-14859:start -->
#### Do Coding Agents Understand Least-Privilege Authorization?

问题与演进：coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14859v1 §3 AuthBench and Permission-Boundary Inference — mechanism boundary: As coding agents gain access to shells, repositories, and user files, least-privilege authorization becomes a prerequisite for safe deployment: an agent should receive enough authority to complete the task, without unnecessary authority that exposes sensitive surfaces.`。

Evaluation：`https://arxiv.org/html/2605.14859v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14859v1 Appendix B Limitations and Future Work — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14859:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14859:end -->
<!-- review:SF-2026-ARXIV-2605-14859:end -->

<!-- review:SF-2026-ARXIV-2605-14865:start -->
#### Holistic Evaluation and Failure Diagnosis of AI Agents

问题与演进：Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14865v1 §3 Top-down and span-level diagnostic framework — mechanism boundary: AI agents execute complex multi-step processes, but current evaluation falls short: outcome metrics report success or failure without explaining why, and process-level approaches struggle to connect failure types to their precise locations within long, structured traces.`。

Evaluation：`https://arxiv.org/html/2605.14865v1 §4 TRAIL/GAIA/SWE-Bench evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14865v1 §5 Limitations and evaluator/model/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14865v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14865:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14865:end -->
<!-- review:SF-2026-ARXIV-2605-14865:end -->

<!-- review:SF-2026-ARXIV-2605-14906:start -->
#### MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models

问题与演进：多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14906v1 §3 MemLens construction and visual-evidence requirements — mechanism boundary: Memory is essential for large vision-language models (LVLMs) to handle long, multimodal interactions, with two method directions providing this capability: long-context LVLMs and memory-augmented agents.`。

Evaluation：`https://arxiv.org/html/2605.14906v1 §4 Evaluation across memory systems — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14906v1 §6 Limitations — synthetic conversation, judge and modality/task boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14906v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14906:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14906:end -->
<!-- review:SF-2026-ARXIV-2605-14906:end -->

<!-- review:SF-2026-ARXIV-2605-14932:start -->
#### Toward Securing AI Agents Like Operating Systems

问题与演进：Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14932v1 §3 Agent-as-OS Security Model — mechanism boundary: Autonomous agents based on large language models (LLMs) are rapidly emerging as a general-purpose technology, with recent systems such as OpenClaw extending their capabilities through broad tool use, third-party skills, and deeper integration into user environments.`。

Evaluation：`https://arxiv.org/html/2605.14932v1 §4–§5 Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14932v1 §VI Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14932v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14932:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14932:end -->
<!-- review:SF-2026-ARXIV-2605-14932:end -->

<!-- review:SF-2026-ARXIV-2605-14968:start -->
#### GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation

问题与演进：可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14968v1 official PDF pp. 2–11 §1.3–§1.8 diagram-as-specification, contracts, runtime and formal semantics — mechanism boundary: GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes.`。

Evaluation：`https://arxiv.org/html/2605.14968v1 official PDF pp. 12–15 §1.12 Evaluation Plan; §1.13 Empirical Evaluation; §2 Implementation Status — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14968v1 official PDF pp. 11–15 §1.10 Failure Modes and Limitations; §1.13.6 Interpretation and Limitations — verified core not deployed/evaluated — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14968v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14968:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14968:end -->
<!-- review:SF-2026-ARXIV-2605-14968:end -->

<!-- review:SF-2026-ARXIV-2605-14978:start -->
#### Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing

问题与演进：speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.14978v1 §3 Adaptive-window policy optimization — mechanism boundary: Speculative decoding accelerates LLM inference by having a lightweight draft model propose speculative windows of candidate tokens for parallel verification by a larger target model.`。

Evaluation：`https://arxiv.org/html/2605.14978v1 §4 Serving evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.14978v1 §5 Limitations and workload/hardware/generalization boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.14978v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-14978:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-14978:end -->
<!-- review:SF-2026-ARXIV-2605-14978:end -->

<!-- review:SF-2026-ARXIV-2605-15030:start -->
#### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections

问题与演进：Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15030v1 §3 Problem; §4 Data; §5 WARD Training — mechanism boundary: Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces.`。

Evaluation：`https://arxiv.org/html/2605.15030v1 §6 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15030v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15030v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15030:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15030:end -->
<!-- review:SF-2026-ARXIV-2605-15030:end -->

<!-- review:SF-2026-ARXIV-2605-15034:start -->
#### AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models

问题与演进：模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15034v1 §3 Watched/unwatched experimental design — mechanism boundary: Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored.`。

Evaluation：`https://arxiv.org/html/2605.15034v1 §4 Strategic-behavior results — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15034v1 §5 Limitations and model/task/context boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15034v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15034:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15034:end -->
<!-- review:SF-2026-ARXIV-2605-15034:end -->

<!-- review:SF-2026-ARXIV-2605-15051:start -->
#### An Interpretable Latency Model for Speculative Decoding in LLM Serving

问题与演进：生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15051v1 §3 Interpretable Serving Latency Model — mechanism boundary: Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel.`。

Evaluation：`https://arxiv.org/html/2605.15051v1 §4 Validation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15051v1 §5 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15051v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15051:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15051:end -->
<!-- review:SF-2026-ARXIV-2605-15051:end -->

<!-- review:SF-2026-ARXIV-2605-15079:start -->
#### Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets

问题与演进：受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15079v1 §3 Croissant Baker Pipeline — mechanism boundary: Croissant has emerged as the metadata standard for machine learning datasets, providing a structured, JSON-LD-based format that makes dataset discovery, automated ingestion, and reproducible analysis machine-checkable across ML platforms.`。

Evaluation：`https://arxiv.org/html/2605.15079v1 §4–§5 Evaluation and Case Studies — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15079v1 §6 Failure Modes and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15079v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15079:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15079:end -->
<!-- review:SF-2026-ARXIV-2605-15079:end -->

<!-- review:SF-2026-ARXIV-2605-15100:start -->
#### Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling

问题与演进：test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15100v1 §3 Dual-dimensional adaptive inference policy — mechanism boundary: Large Language Models (LLMs) have demonstrated remarkable abilities in reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15100v1 §4 Budget-quality evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15100v1 §5 Limitations and model/task/SLO boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15100v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15100:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15100:end -->
<!-- review:SF-2026-ARXIV-2605-15100:end -->

<!-- review:SF-2026-ARXIV-2605-15109:start -->
#### Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG

问题与演进：Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15109v1 §3 Traversal Context and Provenance — mechanism boundary: Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful.`。

Evaluation：`https://arxiv.org/html/2605.15109v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15109v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15109v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15109:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15109:end -->
<!-- review:SF-2026-ARXIV-2605-15109:end -->

<!-- review:SF-2026-ARXIV-2605-15118:start -->
#### Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks

问题与演进：攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15118v1 §3 Threat taxonomy and Target×Technique matrix — mechanism boundary: We introduce a reusable framework for auditing whether LLM attack benchmarks collectively cover the threat surface: a 4$\times$6 Target $\times$ Technique matrix grounded in STRIDE, constructed from a 507-leaf taxonomy -- 401 data-populated and 106 threat-model-derived leaves -- of inference-time attacks extracted from 932 arXiv security studies (2023--2026).`。

Evaluation：`https://arxiv.org/html/2605.15118v1 §4 Cross-benchmark coverage audit — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15118v1 §5 Limitations and literature/labeling coverage boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15118v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15118:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15118:end -->
<!-- review:SF-2026-ARXIV-2605-15118:end -->

<!-- review:SF-2026-ARXIV-2605-15128:start -->
#### MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory

问题与演进：多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15128v1 §3 MemEye framework and benchmark construction — mechanism boundary: Long-term agent memory is increasingly multimodal, yet existing evaluations rarely test whether agents preserve the visual evidence needed for later reasoning.`。

Evaluation：`https://arxiv.org/html/2605.15128v1 §4 Evaluation of 13 memory methods — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15128v1 §6 Limitations — life-scenario, judge and visual-tool boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15128v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15128:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15128:end -->
<!-- review:SF-2026-ARXIV-2605-15128:end -->

<!-- review:SF-2026-ARXIV-2605-15132:start -->
#### APWA: A Distributed Architecture for Parallelizable Agentic Workflows

问题与演进：可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15132v1 §3 APWA Architecture — mechanism boundary: Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains.`。

Evaluation：`https://arxiv.org/html/2605.15132v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15132v1 Appendix A Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15132v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15132:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15132:end -->
<!-- review:SF-2026-ARXIV-2605-15132:end -->

<!-- review:SF-2026-ARXIV-2605-15138:start -->
#### Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution

问题与演进：unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15138v1 §3 MANSU circuit attribution and null-space update — mechanism boundary: Standard unlearning evaluations measure behavioral suppression in full precision, immediately after training, despite every deployed language model being quantized first.`。

Evaluation：`https://arxiv.org/html/2605.15138v1 §4 Full-precision and NF4 evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15138v1 §6 Limitations and model/quantizer/forget-set boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15138v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15138:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15138:end -->
<!-- review:SF-2026-ARXIV-2605-15138:end -->

<!-- review:SF-2026-ARXIV-2605-15152:start -->
#### Widening the Gap: Exploiting LLM Quantization via Outlier Injection

问题与演进：模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15152v1 official PDF pp. 3–5 §3.1–§3.3 Target Quantizations, Threat Model and Outlier Injection — mechanism boundary: LLM quantization has become essential for memory-efficient deployment.`。

Evaluation：`https://arxiv.org/html/2605.15152v1 official PDF pp. 5–11 §4 Evaluation, defenses and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15152v1 official PDF p. 13 Appendix A Limitations and Future Work — excludes 70B models and specialized quantization/hardware — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15152v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15152:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15152:end -->
<!-- review:SF-2026-ARXIV-2605-15152:end -->

<!-- review:SF-2026-ARXIV-2605-15155:start -->
#### Self-Distilled Agentic Reinforcement Learning

问题与演进：Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15155v1 §3 SDAR gated on-policy self-distillation — mechanism boundary: Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction.`。

Evaluation：`https://arxiv.org/html/2605.15155v1 §4–§5 Agent-environment evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15155v1 Appendix limitations, hyperparameters and event-time artifact boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15155v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15155:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15155:end -->
<!-- review:SF-2026-ARXIV-2605-15155:end -->

<!-- review:SF-2026-ARXIV-2605-15164:start -->
#### Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands

问题与演进：behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15164v1 §2–§7 Behavioural Assurance Analysis — mechanism boundary: This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify.`。

Evaluation：`https://arxiv.org/html/2605.15164v1 §7 Pilot Evidence — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15164v1 §8 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15164v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15164:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15164:end -->
<!-- review:SF-2026-ARXIV-2605-15164:end -->

<!-- review:SF-2026-ARXIV-2605-15172:start -->
#### MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs

问题与演进：backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15172v1 §3 MetaBackdoor positional-trigger construction — mechanism boundary: Backdoor attacks pose a serious security threat to large language models (LLMs), which are increasingly deployed as general-purpose assistants in safety- and privacy-critical applications.`。

Evaluation：`https://arxiv.org/html/2605.15172v1 §4 Cross-model/position-encoding evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15172v1 §6 Limitations and trigger/architecture boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15172v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15172:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15172:end -->
<!-- review:SF-2026-ARXIV-2605-15172:end -->

<!-- review:SF-2026-ARXIV-2605-15178:start -->
#### SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer

问题与演进：minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15178v1 §3 SANA-WM architecture; §4 data and camera annotation — mechanism boundary: We introduce SANA-WM, an efficient 2.6B-parameter open-source world model natively trained for one-minute generation, synthesizing high-fidelity, 720p, minute-scale videos with precise camera control.`。

Evaluation：`https://arxiv.org/html/2605.15178v1 §5 Generation/control evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15178v1 §6 Limitations and video-generation/world-model boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15178v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15178:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15178:end -->
<!-- review:SF-2026-ARXIV-2605-15178:end -->

<!-- review:SF-2026-ARXIV-2605-15184:start -->
#### Is Grep All You Need? How Agent Harnesses Reshape Agentic Search

问题与演进：Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15184v1 §3 Harness and Retrieval Conditions — mechanism boundary: Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users.`。

Evaluation：`https://arxiv.org/html/2605.15184v1 §4 Experiments — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15184v1 §5 Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15184v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15184:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15184:end -->
<!-- review:SF-2026-ARXIV-2605-15184:end -->

<!-- review:SF-2026-ARXIV-2605-15185:start -->
#### Quantitative Video World Model Evaluation for Geometric-Consistency

问题与演进：视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15185v1 §3 PDI-Bench Methodology — mechanism boundary: Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging.`。

Evaluation：`https://arxiv.org/html/2605.15185v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15185v1 Appendix G Limitations and Future Directions — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15185v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15185:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15185:end -->
<!-- review:SF-2026-ARXIV-2605-15185:end -->

<!-- review:SF-2026-ARXIV-2605-15188:start -->
#### FutureSim: Replaying World Events to Evaluate Adaptive Agents

问题与演进：开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.15188v1 §3 FutureSim chronological replay environment — mechanism boundary: AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives.`。

Evaluation：`https://arxiv.org/html/2605.15188v1 §4 Three-month agent evaluation and ablations — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.15188v1 §6 Limitations and news/source/forecasting boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.15188v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-15188:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-15188:end -->
<!-- review:SF-2026-ARXIV-2605-15188:end -->

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

<!-- review:SF-2026-ARXIV-2605-16436:start -->
#### The End of Trust: How Agentic AI Breaks Security Assumptions

问题与演进：Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.16436v1 §2–§5 Agentic Threat-Economics Analysis — mechanism boundary: For decades, the security of digital interaction has rested on an unacknowledged economic constraint.`。

Evaluation：`https://arxiv.org/html/2605.16436v1 §3–§5 Case Analyses — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.16436v1 §6 Conclusion and position-paper evidence boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.16436v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16436:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16436:end -->
<!-- review:SF-2026-ARXIV-2605-16436:end -->

<!-- review:SF-2026-ARXIV-2605-16439:start -->
#### KVCapsule: Efficient Sequential KV Cache Compression for Vision-Language Models with Asymmetric Redundancy

问题与演进：VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.16439v1 §3 KVCapsule — mechanism boundary: Vision-Language Models (VLMs) have emerged as a critical and fast-growing extension of Large Language Models (LLMs) that enable multimodal reasoning through both text and image inputs.`。

Evaluation：`https://arxiv.org/html/2605.16439v1 §4–§5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.16439v1 §6 Conclusion and disclosed model/workload boundary — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.16439v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16439:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16439:end -->
<!-- review:SF-2026-ARXIV-2605-16439:end -->

<!-- review:SF-2026-ARXIV-2605-18859:start -->
#### TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing

问题与演进：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。旧路径在原 workload、风险与成本约束下继续成立。

Method：`https://arxiv.org/html/2605.18859v1 §3 TwinRouterBench Overview; §4 Dataset — mechanism boundary: LLM routing matters most in long-horizon applications such as coding agents, deep research systems, and computer-use agents, where a single user request triggers many model calls.`。

Evaluation：`https://arxiv.org/html/2605.18859v1 §5 Evaluation — results remain bound to the disclosed model, workload, evaluator and system configuration`。

Non-proof / fallback：`https://arxiv.org/html/2605.18859v1 §7 Conclusion and Limitations — no generalization to undisclosed model, hardware, precision, length, batch, concurrency or SLO`。越过披露边界时回退现有 owner 的已验证路径。Artifact：`https://arxiv.org/html/2605.18859v1 — artifact/code statement inspected; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-18859:start -->长期结论只限 exact-v1 披露机制与实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 均为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-18859:end -->
<!-- review:SF-2026-ARXIV-2605-18859:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

本报告不把作者性能数字外推为通用 benchmark claim；条件保留在 Source Review 的 disclosed/not-disclosed boundary。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-14241 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-TOOL-CALLING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14241 |
| SF-2026-ARXIV-2605-14249 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-COST` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14249 |
| SF-2026-ARXIV-2605-14271 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14271 |
| SF-2026-ARXIV-2605-14290 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-WORKFLOW` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14290 |
| SF-2026-ARXIV-2605-14305 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MULTIMODAL-GENERATIVE-PARADIGMS` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14305 |
| SF-2026-ARXIV-2605-14415 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14415 |
| SF-2026-ARXIV-2605-14421 | score_7_9;forced_review;potential_books_delta | selected | DA-MEMORY-LINEAGE-GATE | — | 跨越 memory/action、generation/checking 或 routing/environment 的 ownership boundary | analysis:DA-MEMORY-LINEAGE-GATE |
| SF-2026-ARXIV-2605-14460 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-PLATFORM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14460 |
| SF-2026-ARXIV-2605-14473 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-RAG` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14473 |
| SF-2026-ARXIV-2605-14483 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-MULTI-AGENT` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14483 |
| SF-2026-ARXIV-2605-14498 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-MEMORY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14498 |
| SF-2026-ARXIV-2605-14514 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14514 |
| SF-2026-ARXIV-2605-14570 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14570 |
| SF-2026-ARXIV-2605-14591 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14591 |
| SF-2026-ARXIV-2605-14636 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14636 |
| SF-2026-ARXIV-2605-14678 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14678 |
| SF-2026-ARXIV-2605-14744 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14744 |
| SF-2026-ARXIV-2605-14747 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `TRAIN-DATA` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14747 |
| SF-2026-ARXIV-2605-14786 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14786 |
| SF-2026-ARXIV-2605-14859 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14859 |
| SF-2026-ARXIV-2605-14865 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14865 |
| SF-2026-ARXIV-2605-14906 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14906 |
| SF-2026-ARXIV-2605-14932 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14932 |
| SF-2026-ARXIV-2605-14968 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-WORKFLOW` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14968 |
| SF-2026-ARXIV-2605-14978 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `INFER-SPECULATIVE-DECODING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-14978 |
| SF-2026-ARXIV-2605-15030 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15030 |
| SF-2026-ARXIV-2605-15034 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15034 |
| SF-2026-ARXIV-2605-15051 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `INFER-SPECULATIVE-DECODING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15051 |
| SF-2026-ARXIV-2605-15079 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `TRAIN-DATA` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15079 |
| SF-2026-ARXIV-2605-15100 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `INFER-SCHEDULING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15100 |
| SF-2026-ARXIV-2605-15109 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-RAG` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15109 |
| SF-2026-ARXIV-2605-15118 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15118 |
| SF-2026-ARXIV-2605-15128 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15128 |
| SF-2026-ARXIV-2605-15132 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-WORKFLOW` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15132 |
| SF-2026-ARXIV-2605-15138 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15138 |
| SF-2026-ARXIV-2605-15152 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15152 |
| SF-2026-ARXIV-2605-15155 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `TRAIN-GRPO` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15155 |
| SF-2026-ARXIV-2605-15164 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15164 |
| SF-2026-ARXIV-2605-15172 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15172 |
| SF-2026-ARXIV-2605-15178 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MULTIMODAL-WORLD-MODELS` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15178 |
| SF-2026-ARXIV-2605-15184 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-RAG` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15184 |
| SF-2026-ARXIV-2605-15185 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MULTIMODAL-WORLD-MODELS` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15185 |
| SF-2026-ARXIV-2605-15188 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-EVALUATION-SYSTEM` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15188 |
| SF-2026-ARXIV-2605-15238 | score_7_9;forced_review;potential_books_delta | selected | DA-ASYNC-CHECKPOINT-ROLLBACK | — | 跨越 memory/action、generation/checking 或 routing/environment 的 ownership boundary | analysis:DA-ASYNC-CHECKPOINT-ROLLBACK |
| SF-2026-ARXIV-2605-15257 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-MONITORING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15257 |
| SF-2026-ARXIV-2605-15338 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-MEMORY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15338 |
| SF-2026-ARXIV-2605-15377 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-MONITORING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15377 |
| SF-2026-ARXIV-2605-15384 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-MEMORY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15384 |
| SF-2026-ARXIV-2605-15403 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MODEL-MOE` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15403 |
| SF-2026-ARXIV-2605-15422 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `TRAIN-DISTRIBUTED-TRAINING` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15422 |
| SF-2026-ARXIV-2605-15425 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `AGENT-WORKFLOW` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15425 |
| SF-2026-ARXIV-2605-15466 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MULTIMODAL-WORLD-MODELS` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15466 |
| SF-2026-ARXIV-2605-15477 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `MULTIMODAL-WORLD-MODELS` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-15477 |
| SF-2026-ARXIV-2605-16436 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `PLATFORM-SECURITY` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-16436 |
| SF-2026-ARXIV-2605-16439 | score_7_9 | not_selected | — | — | exact-v1 Review 已完成；其 delta 由 `INFER-KV-CACHE` 承载，三个入选单元更能解释跨层状态与 commit authority | analysis-decision:SF-2026-ARXIV-2605-16439 |
| SF-2026-ARXIV-2605-18859 | score_7_9;forced_review;potential_books_delta | selected | DA-LIVE-AGENT-ROUTING-EVAL | — | 跨越 memory/action、generation/checking 或 routing/environment 的 ownership boundary | analysis:DA-LIVE-AGENT-ROUTING-EVAL |

本日最多扩写三项；未入选项目仍保留完整 exact-v1 Source Review 与 Books Decision。

<!-- analysis:DA-MEMORY-LINEAGE-GATE:start -->
### Memory 从文本存储推进到可验证的 Action Chain of Custody

旧路径允许直接召回文本，在低风险、单 session、无外部副作用时成本最低。持久 memory 一旦可以跨 session 影响敏感 action，约束变成：每次派生和引用都必须可追溯，最终 action 只能由 policy gate 在 lineage 完整时提交。签名 provenance 与 derivation DAG 换来可审计 chain-of-custody，却增加 lineage storage、key lifecycle、LLM derivation error 与 availability failure；缺失 lineage 时应降级为 advisory context 或人工确认。
<!-- analysis:DA-MEMORY-LINEAGE-GATE:end -->

<!-- analysis:DA-ASYNC-CHECKPOINT-ROLLBACK:start -->
### Code Generation 从事后重写推进到异步检查与有界回滚

事后 compile/repair 在短程序、低 compiler cost 时简单可靠，但长生成会让晚发现错误扩大重写范围。Hydra 保存已验证 checkpoint，让 compiler 异步检查 provisional prefix；失败只回滚到最近可信点。收益是减少 token 和 latency，代价是 sealing 规则、checkpoint state、一致性与 checker lag。compiler 只拥有静态诊断，不能替代测试、安全或 outcome correctness；异步状态不可靠时回退完整生成后编译。
<!-- analysis:DA-ASYNC-CHECKPOINT-ROLLBACK:end -->

<!-- analysis:DA-LIVE-AGENT-ROUTING-EVAL:start -->
### Routing Evaluation 从 One-shot Proxy 推进到 Step-level Environment Outcome

one-shot routing 在独立请求、无长期状态时可复算且便宜；Agent trajectory 中每次模型替换会改变后续 observation、tool call 与 task success。TwinRouterBench 将真实 step prefix 交给 router，并用 environment execution 验证 downstream outcome，分开 static replay 与 live dynamic track。它提高外部有效性，却引入环境 nondeterminism、执行成本与 evaluator/version state；无法 live replay 时静态 track 仍可用于筛选，但不能冒充最终部署证据。
<!-- analysis:DA-LIVE-AGENT-ROUTING-EVAL:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-14241:start -->SF-2026-ARXIV-2605-14241 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14241:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14249:start -->SF-2026-ARXIV-2605-14249 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14249:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14271:start -->SF-2026-ARXIV-2605-14271 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14271:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14290:start -->SF-2026-ARXIV-2605-14290 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14290:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14305:start -->SF-2026-ARXIV-2605-14305 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14305:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14415:start -->SF-2026-ARXIV-2605-14415 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14415:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14460:start -->SF-2026-ARXIV-2605-14460 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14460:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14473:start -->SF-2026-ARXIV-2605-14473 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14473:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14483:start -->SF-2026-ARXIV-2605-14483 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14483:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14498:start -->SF-2026-ARXIV-2605-14498 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14498:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14514:start -->SF-2026-ARXIV-2605-14514 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14514:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14570:start -->SF-2026-ARXIV-2605-14570 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14570:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14591:start -->SF-2026-ARXIV-2605-14591 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14591:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14636:start -->SF-2026-ARXIV-2605-14636 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14636:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14678:start -->SF-2026-ARXIV-2605-14678 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14678:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14744:start -->SF-2026-ARXIV-2605-14744 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14744:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14747:start -->SF-2026-ARXIV-2605-14747 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14747:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14786:start -->SF-2026-ARXIV-2605-14786 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14786:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14859:start -->SF-2026-ARXIV-2605-14859 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14859:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14865:start -->SF-2026-ARXIV-2605-14865 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14865:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14906:start -->SF-2026-ARXIV-2605-14906 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14906:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14932:start -->SF-2026-ARXIV-2605-14932 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14932:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14968:start -->SF-2026-ARXIV-2605-14968 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14968:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-14978:start -->SF-2026-ARXIV-2605-14978 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-14978:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15030:start -->SF-2026-ARXIV-2605-15030 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15030:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15034:start -->SF-2026-ARXIV-2605-15034 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15034:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15051:start -->SF-2026-ARXIV-2605-15051 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15051:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15079:start -->SF-2026-ARXIV-2605-15079 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15079:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15100:start -->SF-2026-ARXIV-2605-15100 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15100:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15109:start -->SF-2026-ARXIV-2605-15109 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15109:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15118:start -->SF-2026-ARXIV-2605-15118 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15118:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15128:start -->SF-2026-ARXIV-2605-15128 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15128:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15132:start -->SF-2026-ARXIV-2605-15132 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15132:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15138:start -->SF-2026-ARXIV-2605-15138 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15138:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15152:start -->SF-2026-ARXIV-2605-15152 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15152:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15155:start -->SF-2026-ARXIV-2605-15155 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15155:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15164:start -->SF-2026-ARXIV-2605-15164 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15164:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15172:start -->SF-2026-ARXIV-2605-15172 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15172:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15178:start -->SF-2026-ARXIV-2605-15178 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15178:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15184:start -->SF-2026-ARXIV-2605-15184 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15184:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15185:start -->SF-2026-ARXIV-2605-15185 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15185:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15188:start -->SF-2026-ARXIV-2605-15188 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15188:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15257:start -->SF-2026-ARXIV-2605-15257 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15257:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15338:start -->SF-2026-ARXIV-2605-15338 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15338:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15377:start -->SF-2026-ARXIV-2605-15377 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15377:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15384:start -->SF-2026-ARXIV-2605-15384 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15403:start -->SF-2026-ARXIV-2605-15403 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15403:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15422:start -->SF-2026-ARXIV-2605-15422 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15422:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15425:start -->SF-2026-ARXIV-2605-15425 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15425:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15466:start -->SF-2026-ARXIV-2605-15466 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15466:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15477:start -->SF-2026-ARXIV-2605-15477 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-15477:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16436:start -->SF-2026-ARXIV-2605-16436 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-16436:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16439:start -->SF-2026-ARXIV-2605-16439 已完成 exact-v1 Review；未扩写不是跳过，而是其 owner-local delta 不如三个选中单元更能解释跨层 ownership 变化。<!-- analysis-decision:SF-2026-ARXIV-2605-16439:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-14241 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-14241 | delta:SF-2026-ARXIV-2605-14241 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-14241 |
| SF-2026-ARXIV-2605-14249 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69; books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605-14249 | delta:SF-2026-ARXIV-2605-14249 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14249 |
| SF-2026-ARXIV-2605-14271 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14271 | delta:SF-2026-ARXIV-2605-14271 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14271 |
| SF-2026-ARXIV-2605-14290 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-14290 | delta:SF-2026-ARXIV-2605-14290 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14290 |
| SF-2026-ARXIV-2605-14305 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-14305 | delta:SF-2026-ARXIV-2605-14305 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14305 |
| SF-2026-ARXIV-2605-14415 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14415 | delta:SF-2026-ARXIV-2605-14415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14415 |
| SF-2026-ARXIV-2605-14421 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-14421 | delta:SF-2026-ARXIV-2605-14421 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-14421 |
| SF-2026-ARXIV-2605-14460 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-14460 | delta:SF-2026-ARXIV-2605-14460 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14460 |
| SF-2026-ARXIV-2605-14473 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-14473 | delta:SF-2026-ARXIV-2605-14473 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14473 |
| SF-2026-ARXIV-2605-14483 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-14483 | delta:SF-2026-ARXIV-2605-14483 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14483 |
| SF-2026-ARXIV-2605-14498 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-14498 | delta:SF-2026-ARXIV-2605-14498 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14498 |
| SF-2026-ARXIV-2605-14514 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14514 | delta:SF-2026-ARXIV-2605-14514 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14514 |
| SF-2026-ARXIV-2605-14570 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14570 | delta:SF-2026-ARXIV-2605-14570 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14570 |
| SF-2026-ARXIV-2605-14591 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14591 | delta:SF-2026-ARXIV-2605-14591 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14591 |
| SF-2026-ARXIV-2605-14636 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14636 | delta:SF-2026-ARXIV-2605-14636 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14636 |
| SF-2026-ARXIV-2605-14678 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14678 | delta:SF-2026-ARXIV-2605-14678 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14678 |
| SF-2026-ARXIV-2605-14744 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14744 | delta:SF-2026-ARXIV-2605-14744 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14744 |
| SF-2026-ARXIV-2605-14747 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-14747 | delta:SF-2026-ARXIV-2605-14747 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14747 |
| SF-2026-ARXIV-2605-14786 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14786 | delta:SF-2026-ARXIV-2605-14786 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14786 |
| SF-2026-ARXIV-2605-14859 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14859 | delta:SF-2026-ARXIV-2605-14859 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14859 |
| SF-2026-ARXIV-2605-14865 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14865 | delta:SF-2026-ARXIV-2605-14865 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14865 |
| SF-2026-ARXIV-2605-14906 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-14906 | delta:SF-2026-ARXIV-2605-14906 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14906 |
| SF-2026-ARXIV-2605-14932 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-14932 | delta:SF-2026-ARXIV-2605-14932 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14932 |
| SF-2026-ARXIV-2605-14968 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-14968 | delta:SF-2026-ARXIV-2605-14968 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14968 |
| SF-2026-ARXIV-2605-14978 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-14978 | delta:SF-2026-ARXIV-2605-14978 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-14978 |
| SF-2026-ARXIV-2605-15030 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15030 | delta:SF-2026-ARXIV-2605-15030 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15030 |
| SF-2026-ARXIV-2605-15034 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15034 | delta:SF-2026-ARXIV-2605-15034 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15034 |
| SF-2026-ARXIV-2605-15051 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-15051 | delta:SF-2026-ARXIV-2605-15051 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15051 |
| SF-2026-ARXIV-2605-15079 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-15079 | delta:SF-2026-ARXIV-2605-15079 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15079 |
| SF-2026-ARXIV-2605-15100 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-15100 | delta:SF-2026-ARXIV-2605-15100 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15100 |
| SF-2026-ARXIV-2605-15109 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-15109 | delta:SF-2026-ARXIV-2605-15109 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15109 |
| SF-2026-ARXIV-2605-15118 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15118 | delta:SF-2026-ARXIV-2605-15118 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15118 |
| SF-2026-ARXIV-2605-15128 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15128 | delta:SF-2026-ARXIV-2605-15128 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15128 |
| SF-2026-ARXIV-2605-15132 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-15132 | delta:SF-2026-ARXIV-2605-15132 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15132 |
| SF-2026-ARXIV-2605-15138 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15138 | delta:SF-2026-ARXIV-2605-15138 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15138 |
| SF-2026-ARXIV-2605-15152 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15152 | delta:SF-2026-ARXIV-2605-15152 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15152 |
| SF-2026-ARXIV-2605-15155 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-15155 | delta:SF-2026-ARXIV-2605-15155 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15155 |
| SF-2026-ARXIV-2605-15164 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15164 | delta:SF-2026-ARXIV-2605-15164 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15164 |
| SF-2026-ARXIV-2605-15172 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-15172 | delta:SF-2026-ARXIV-2605-15172 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15172 |
| SF-2026-ARXIV-2605-15178 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15178 | delta:SF-2026-ARXIV-2605-15178 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15178 |
| SF-2026-ARXIV-2605-15184 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-15184 | delta:SF-2026-ARXIV-2605-15184 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15184 |
| SF-2026-ARXIV-2605-15185 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-15185 | delta:SF-2026-ARXIV-2605-15185 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-15185 |
| SF-2026-ARXIV-2605-15188 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-15188 | delta:SF-2026-ARXIV-2605-15188 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15188 |
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
| SF-2026-ARXIV-2605-16436 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16436 | delta:SF-2026-ARXIV-2605-16436 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16436 |
| SF-2026-ARXIV-2605-16439 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16439 | delta:SF-2026-ARXIV-2605-16439 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16439 |
| SF-2026-ARXIV-2605-18859 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18859 | delta:SF-2026-ARXIV-2605-18859 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18859 |
<!-- books-review:SF-2026-ARXIV-2605-14241:start -->
<!-- existing:SF-2026-ARXIV-2605-14241:start -->已读取 `books/part-07-agent/78-tool-calling.md` 及相邻章节；当前主线已覆盖proposal、provider/tool discovery、utility admission、authorization、execution 与 outcome commit 的分层。正文尚未明确承载本 family 的增量：同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth。 Owner snapshot sha256=`df252ef396695001f51255bccc709bc32851023df8e0a6746fe4a03c36bddf50`；相邻章节=`books/part-07-agent/77-memory.md, books/part-07-agent/79-planning.md`。<!-- existing:SF-2026-ARXIV-2605-14241:end -->
<!-- delta:SF-2026-ARXIV-2605-14241:start -->同功能 tool provider 的选择应由观察 runtime load、latency、reliability 与 answer-quality 的在线 router 决定；router 只拥有 provider selection，不拥有工具授权或结果 truth<!-- delta:SF-2026-ARXIV-2605-14241:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14241:end -->
<!-- books-review:SF-2026-ARXIV-2605-14249:start -->
<!-- existing:SF-2026-ARXIV-2605-14249:start -->已读取 `books/part-06-ai-infrastructure/70-cost.md` 及相邻章节；当前主线已覆盖端到端 work unit、energy/latency/quality 约束与 capacity/idle/失败重试的共同核算。本 family 的增量“多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`8838d188822605575fee9227fdf4ba3a22518eb6dc8cf6ed5a4ad9237351115c`；相邻章节=`books/part-06-ai-infrastructure/69-trace.md, books/part-06-ai-infrastructure/71-multi-tenant.md`。<!-- existing:SF-2026-ARXIV-2605-14249:end -->
<!-- delta:SF-2026-ARXIV-2605-14249:start -->多 GPU 推理能耗优化应先以可解释 surrogate 预测 layer/operator 与并行配置的 energy，再把 energy-quality-latency 约束作为配置探索合同，而不是只比较整机平均功率；当前 Ch70 已明确承载 layer-wise energy model、architecture proxy 与 device/precision/batch/shape/utilization 约束，因此本 family 不再重复写回<!-- delta:SF-2026-ARXIV-2605-14249:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14249:end -->
<!-- books-review:SF-2026-ARXIV-2605-14271:start -->
<!-- existing:SF-2026-ARXIV-2605-14271:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14271:end -->
<!-- delta:SF-2026-ARXIV-2605-14271:start -->Agent harness 安全评测必须观察 trajectory 中的 resource access、message routing 与 authority transition；最终答案正确不能覆盖中途越权<!-- delta:SF-2026-ARXIV-2605-14271:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14271:end -->
<!-- books-review:SF-2026-ARXIV-2605-14290:start -->
<!-- existing:SF-2026-ARXIV-2605-14290:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-14290:end -->
<!-- delta:SF-2026-ARXIV-2605-14290:start -->Web Agent 应把不可信 runtime content 限制为预提交程序的数据，而不允许其生成新控制流；typed site API、隔离的 LLM subroutine 与显式 replan fallback 共同定义安全/可用性边界<!-- delta:SF-2026-ARXIV-2605-14290:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14290:end -->
<!-- books-review:SF-2026-ARXIV-2605-14305:start -->
<!-- existing:SF-2026-ARXIV-2605-14305:start -->已读取 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及相邻章节；当前主线已覆盖AR、diffusion、masked refinement 的 proposal、verification、correction 与 commit 边界。本 family 的增量“离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`82d67a82821a384369ee36c24794db1b14bdfd6d538877525c38e9420761df30`；相邻章节=`books/part-03-multimodal-world-models/23-multimodal-representation.md, books/part-03-multimodal-world-models/25-multimodal-world-models.md`。<!-- existing:SF-2026-ARXIV-2605-14305:end -->
<!-- delta:SF-2026-ARXIV-2605-14305:start -->离散 diffusion 的并行 proposal 可用 prefix-conditioned factorization 消除 token-independent clean-posterior 近似，再由 speculative verification 保留 target distribution<!-- delta:SF-2026-ARXIV-2605-14305:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14305:end -->
<!-- books-review:SF-2026-ARXIV-2605-14415:start -->
<!-- existing:SF-2026-ARXIV-2605-14415:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14415:end -->
<!-- delta:SF-2026-ARXIV-2605-14415:start -->coding-Agent release maintenance 评测必须把版本链、继承 codebase、跨步 regression 与每步 acceptance contract 纳入 run identity，而不能把独立 issue 分数外推为长期维护能力<!-- delta:SF-2026-ARXIV-2605-14415:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14415:end -->
<!-- books-review:SF-2026-ARXIV-2605-14421:start -->
<!-- existing:SF-2026-ARXIV-2605-14421:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。正文尚未明确承载本 family 的增量：持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-14421:end -->
<!-- delta:SF-2026-ARXIV-2605-14421:start -->持久 Agent memory 的 action justification 应形成签名 provenance 与 derivation-lineage DAG；敏感 action 在 lineage 不闭合时 fail closed，而不是把 recalled text 当作 authority<!-- delta:SF-2026-ARXIV-2605-14421:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14421:end -->
<!-- books-review:SF-2026-ARXIV-2605-14460:start -->
<!-- existing:SF-2026-ARXIV-2605-14460:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及相邻章节；当前主线已覆盖skill artifact identity、capability、admission、runtime policy、drift 与 audit。本 family 的增量“skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`b7ea13daeac643ba9237a698b6363ea16ab660cb662be9c7f33b9302ca7a5802`；相邻章节=`books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-14460:end -->
<!-- delta:SF-2026-ARXIV-2605-14460:start -->skill supply-chain 审计不能只扫描代码 payload，还要执行 capability/effect probes，识别由描述、依赖和运行上下文组合出的 payload-less behavior<!-- delta:SF-2026-ARXIV-2605-14460:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14460:end -->
<!-- books-review:SF-2026-ARXIV-2605-14473:start -->
<!-- existing:SF-2026-ARXIV-2605-14473:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。本 family 的增量“RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-14473:end -->
<!-- delta:SF-2026-ARXIV-2605-14473:start -->RAG 在知识冲突下要把 answer correctness 与 context compliance 分开；诊断 intervention 只能测 retrieved context 是否控制答案，不能证明答案真实<!-- delta:SF-2026-ARXIV-2605-14473:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14473:end -->
<!-- books-review:SF-2026-ARXIV-2605-14483:start -->
<!-- existing:SF-2026-ARXIV-2605-14483:start -->已读取 `books/part-07-agent/82-multi-agent.md` 及相邻章节；当前主线已覆盖role、dependency graph、message/shared state、credit、failure containment 与 final commit owner。本 family 的增量“Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`5101c08d1a612efe07f8c557b662d9ead237399a4164ec7bce2fd5ddbedc3397`；相邻章节=`books/part-07-agent/81-workflow.md, books/part-07-agent/83-mcp.md`。<!-- existing:SF-2026-ARXIV-2605-14483:end -->
<!-- delta:SF-2026-ARXIV-2605-14483:start -->Multi-Agent orchestration 的 role、capacity 与 dependency graph 应被视为一个可执行 artifact，并用 counterfactual feedback 做 credit assignment，而非顺序局部调参<!-- delta:SF-2026-ARXIV-2605-14483:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14483:end -->
<!-- books-review:SF-2026-ARXIV-2605-14498:start -->
<!-- existing:SF-2026-ARXIV-2605-14498:start -->已读取 `books/part-07-agent/77-memory.md` 及相邻章节；当前主线已覆盖write admission、provenance、derived state、retrieval、expiry、poisoning containment 与可逆更新。本 family 的增量“群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`ac3bf5ab49bb87bcf3f0cfa1da47486caeb35e9d451251f91c67caf3bc9de6d7`；相邻章节=`books/part-07-agent/76-rag.md, books/part-07-agent/78-tool-calling.md`。<!-- existing:SF-2026-ARXIV-2605-14498:end -->
<!-- delta:SF-2026-ARXIV-2605-14498:start -->群体会话 memory 必须把 speaker/principal、reply graph、belief ownership 与 audience-specific retrieval 绑定；把多人消息拼成单一文档会制造跨主体状态污染<!-- delta:SF-2026-ARXIV-2605-14498:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14498:end -->
<!-- books-review:SF-2026-ARXIV-2605-14514:start -->
<!-- existing:SF-2026-ARXIV-2605-14514:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14514:end -->
<!-- delta:SF-2026-ARXIV-2605-14514:start -->模型 defense 是有顺序的 release artifact：后续 safety/privacy/fairness patch 必须重新验证先前保障，不能把单项防御通过等同于组合后仍保持保护<!-- delta:SF-2026-ARXIV-2605-14514:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14514:end -->
<!-- books-review:SF-2026-ARXIV-2605-14570:start -->
<!-- existing:SF-2026-ARXIV-2605-14570:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14570:end -->
<!-- delta:SF-2026-ARXIV-2605-14570:start -->diffusion LM 的 uncertainty sensor 必须绑定 denoising trajectory、remasking 与 masked likelihood，不能沿用 autoregressive token probability；该 sensor 仍需独立校准且不拥有事实真值<!-- delta:SF-2026-ARXIV-2605-14570:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14570:end -->
<!-- books-review:SF-2026-ARXIV-2605-14591:start -->
<!-- existing:SF-2026-ARXIV-2605-14591:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14591:end -->
<!-- delta:SF-2026-ARXIV-2605-14591:start -->大模型 privacy audit 可在无法重训时利用已知 member/non-member 固定集合估计经验下界，但该 post-hoc sensor 不能替代机制级 DP accounting 或训练日志；当前 Ch66 已明确承载 post-hoc dataset/membership inference 的证据边界与机制级 accounting 区分，因此本 family 不再重复写回<!-- delta:SF-2026-ARXIV-2605-14591:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14591:end -->
<!-- books-review:SF-2026-ARXIV-2605-14636:start -->
<!-- existing:SF-2026-ARXIV-2605-14636:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14636:end -->
<!-- delta:SF-2026-ARXIV-2605-14636:start -->时间截止问题必须冻结可知信息边界，并将 temporal leakage 作为独立 failure slice；learned critique 只能在所测 cutoff/prompt 分布上提供 sensor<!-- delta:SF-2026-ARXIV-2605-14636:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14636:end -->
<!-- books-review:SF-2026-ARXIV-2605-14678:start -->
<!-- existing:SF-2026-ARXIV-2605-14678:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14678:end -->
<!-- delta:SF-2026-ARXIV-2605-14678:start -->主动 personal Agent 评测必须隐藏 intent、跨 task/session 保留状态，并同时测 proactivity 与 task outcome；单轮显式指令 benchmark 不能代表长期主动协助<!-- delta:SF-2026-ARXIV-2605-14678:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14678:end -->
<!-- books-review:SF-2026-ARXIV-2605-14744:start -->
<!-- existing:SF-2026-ARXIV-2605-14744:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14744:end -->
<!-- delta:SF-2026-ARXIV-2605-14744:start -->治理规则不能由同一生成模型同时解释和自证；policy enforcement 应移出模型回路，以机械 primitive 约束 decision/effect，并把 rationale 仅作为可审计证据<!-- delta:SF-2026-ARXIV-2605-14744:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14744:end -->
<!-- books-review:SF-2026-ARXIV-2605-14747:start -->
<!-- existing:SF-2026-ARXIV-2605-14747:start -->已读取 `books/part-04-training-system/27-data.md` 及相邻章节；当前主线已覆盖dataset identity、schema、lineage、version、governance、quality gate 与 reusable artifact。本 family 的增量“GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`cdd967c3fb6f506cec6ce3f112754e3f76a255641281bce71e1bfb1e09f98690`；相邻章节=`books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-14747:end -->
<!-- delta:SF-2026-ARXIV-2605-14747:start -->GUI Agent 数据管线可从互联网教程视频恢复 observation-action trajectory，但每一步都必须保留 video/application identity、grounding confidence、filter revision 与 executable validation；规模不能替代轨迹正确性<!-- delta:SF-2026-ARXIV-2605-14747:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14747:end -->
<!-- books-review:SF-2026-ARXIV-2605-14786:start -->
<!-- existing:SF-2026-ARXIV-2605-14786:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14786:end -->
<!-- delta:SF-2026-ARXIV-2605-14786:start -->browser Agent 的 action/timing trace 会形成被动 model fingerprint side channel；随机 delay 只能改变 sensor，不是身份或不可链接性保证，平台需将 attribution、privacy 与 rate policy 分开<!-- delta:SF-2026-ARXIV-2605-14786:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14786:end -->
<!-- books-review:SF-2026-ARXIV-2605-14859:start -->
<!-- existing:SF-2026-ARXIV-2605-14859:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14859:end -->
<!-- delta:SF-2026-ARXIV-2605-14859:start -->coding Agent 的权限策略必须由平台从 task、workspace 与 effect contract 推导并执行；模型的 permission-boundary inference 只能是 policy proposal<!-- delta:SF-2026-ARXIV-2605-14859:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14859:end -->
<!-- books-review:SF-2026-ARXIV-2605-14865:start -->
<!-- existing:SF-2026-ARXIV-2605-14865:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14865:end -->
<!-- delta:SF-2026-ARXIV-2605-14865:start -->Agent 评测要把 terminal outcome 与 trace span diagnosis 连接：failure taxonomy、location、cause 与最终结果必须同属一次 run evidence，长轨迹不能只由单一成功率压缩<!-- delta:SF-2026-ARXIV-2605-14865:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14865:end -->
<!-- books-review:SF-2026-ARXIV-2605-14906:start -->
<!-- existing:SF-2026-ARXIV-2605-14906:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-14906:end -->
<!-- delta:SF-2026-ARXIV-2605-14906:start -->多模态长期 memory 评测必须显式比较 long-context 与 external-memory 路径，并冻结 decisive visual evidence、session evolution、ingestion cost 与 storage，而不是把文本 caption shortcut 当视觉记忆<!-- delta:SF-2026-ARXIV-2605-14906:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14906:end -->
<!-- books-review:SF-2026-ARXIV-2605-14932:start -->
<!-- existing:SF-2026-ARXIV-2605-14932:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-14932:end -->
<!-- delta:SF-2026-ARXIV-2605-14932:start -->Agent security 应借鉴 OS 的 process isolation、capability、mediation 与 audit 边界；类比本身不证明任意 Agent runtime 已实现这些保证<!-- delta:SF-2026-ARXIV-2605-14932:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14932:end -->
<!-- books-review:SF-2026-ARXIV-2605-14968:start -->
<!-- existing:SF-2026-ARXIV-2605-14968:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。本 family 的增量“可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-14968:end -->
<!-- delta:SF-2026-ARXIV-2605-14968:start -->可靠 Agent workflow 应把生成计划编译成 typed graph，并让可验证 node/edge contract、execution receipt 与 recovery policy拥有提交权；可视化 DAG 本身不构成正确性证明<!-- delta:SF-2026-ARXIV-2605-14968:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14968:end -->
<!-- books-review:SF-2026-ARXIV-2605-14978:start -->
<!-- existing:SF-2026-ARXIV-2605-14978:start -->已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及相邻章节；当前主线已覆盖draft/target identity、acceptance、verification、rollback 与 serving scheduling 的统一状态机。本 family 的增量“speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`0e93c132655861c91cdfd05e817b93105f2484b37753aec2bebe8d9ea15a0230`；相邻章节=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-14978:end -->
<!-- delta:SF-2026-ARXIV-2605-14978:start -->speculative window 不应是静态常数：在线 policy 可依据 acceptance、draft/verify cost 与服务负载调整 proposal 长度，但 target verification 与 rollback 始终保留最终 commit authority<!-- delta:SF-2026-ARXIV-2605-14978:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-14978:end -->
<!-- books-review:SF-2026-ARXIV-2605-15030:start -->
<!-- existing:SF-2026-ARXIV-2605-15030:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15030:end -->
<!-- delta:SF-2026-ARXIV-2605-15030:start -->Web Agent 的 prompt-injection guard 应作为与 policy 解耦的并行 sensor，并以持续 adversarial update 管理 drift；guard 不能拥有最终 action authority<!-- delta:SF-2026-ARXIV-2605-15030:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15030:end -->
<!-- books-review:SF-2026-ARXIV-2605-15034:start -->
<!-- existing:SF-2026-ARXIV-2605-15034:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15034:end -->
<!-- delta:SF-2026-ARXIV-2605-15034:start -->模型知道被观察时会改变行为，因此安全 evaluation 的 run identity 必须包含 monitoring disclosure、observer context 与 counterfactual hidden-monitor branch；被监控时合规不证明未监控时合规<!-- delta:SF-2026-ARXIV-2605-15034:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15034:end -->
<!-- books-review:SF-2026-ARXIV-2605-15051:start -->
<!-- existing:SF-2026-ARXIV-2605-15051:start -->已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及相邻章节；当前主线已覆盖draft/target identity、acceptance、verification、rollback 与 serving scheduling 的统一状态机。正文尚未明确承载本 family 的增量：生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略。 Owner snapshot sha256=`0e93c132655861c91cdfd05e817b93105f2484b37753aec2bebe8d9ea15a0230`；相邻章节=`books/part-05-inference-system/47-pagedattention.md, books/part-05-inference-system/49-tensorrt-llm.md`。<!-- existing:SF-2026-ARXIV-2605-15051:end -->
<!-- delta:SF-2026-ARXIV-2605-15051:start -->生产 speculative decoding 的 latency model 必须把 request load、emergent batch、draft/verify cost 与 acceptance 联合建模；固定 batch microbenchmark 不能决定在线启用策略<!-- delta:SF-2026-ARXIV-2605-15051:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15051:end -->
<!-- books-review:SF-2026-ARXIV-2605-15079:start -->
<!-- existing:SF-2026-ARXIV-2605-15079:start -->已读取 `books/part-04-training-system/27-data.md` 及相邻章节；当前主线已覆盖dataset identity、schema、lineage、version、governance、quality gate 与 reusable artifact。正文尚未明确承载本 family 的增量：受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata。 Owner snapshot sha256=`cdd967c3fb6f506cec6ce3f112754e3f76a255641281bce71e1bfb1e09f98690`；相邻章节=`books/part-04-training-system/28-pretraining.md`。<!-- existing:SF-2026-ARXIV-2605-15079:end -->
<!-- delta:SF-2026-ARXIV-2605-15079:start -->受治理或本地大数据集需要把 schema inference、profile、semantic annotation 与 Croissant JSON-LD provenance 组织为可复跑 pipeline，而不是先上传公共平台再生成 metadata<!-- delta:SF-2026-ARXIV-2605-15079:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15079:end -->
<!-- books-review:SF-2026-ARXIV-2605-15100:start -->
<!-- existing:SF-2026-ARXIV-2605-15100:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及相邻章节；当前主线已覆盖request/work-unit identity、budget、admission、priority、stop condition 与 SLO-aware execution control。本 family 的增量“test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`aa1e5d4dea458d677ad3fc83ca72b0b799cba53dc07c7e6a31e9b7f2d2d8c533`；相邻章节=`books/part-05-inference-system/55-pd-disaggregation.md`。<!-- existing:SF-2026-ARXIV-2605-15100:end -->
<!-- delta:SF-2026-ARXIV-2605-15100:start -->test-time compute controller 必须把预算、质量目标、uncertainty 与 stop condition作为可提交 state；只增加推理步数既可能浪费预算也可能放大错误<!-- delta:SF-2026-ARXIV-2605-15100:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15100:end -->
<!-- books-review:SF-2026-ARXIV-2605-15109:start -->
<!-- existing:SF-2026-ARXIV-2605-15109:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。正文尚未明确承载本 family 的增量：Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-15109:end -->
<!-- delta:SF-2026-ARXIV-2605-15109:start -->Agentic GraphRAG 的 citation faithfulness 应绑定完整 traversal neighborhood、visited-but-uncited evidence 与最终 citation；只验证末端引用会丢失推理路径 provenance<!-- delta:SF-2026-ARXIV-2605-15109:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15109:end -->
<!-- books-review:SF-2026-ARXIV-2605-15118:start -->
<!-- existing:SF-2026-ARXIV-2605-15118:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15118:end -->
<!-- delta:SF-2026-ARXIV-2605-15118:start -->攻击 benchmark coverage 应以 threat target×technique taxonomy 的可审计分母衡量；单个 benchmark 内部一致或高分不能证明覆盖了部署威胁面<!-- delta:SF-2026-ARXIV-2605-15118:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15118:end -->
<!-- books-review:SF-2026-ARXIV-2605-15128:start -->
<!-- existing:SF-2026-ARXIV-2605-15128:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15128:end -->
<!-- delta:SF-2026-ARXIV-2605-15128:start -->多模态 memory 评测必须按 decisive visual evidence granularity 与跨时间使用方式切片，并用 ablation gate 排除 caption/text shortcut<!-- delta:SF-2026-ARXIV-2605-15128:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15128:end -->
<!-- books-review:SF-2026-ARXIV-2605-15132:start -->
<!-- existing:SF-2026-ARXIV-2605-15132:start -->已读取 `books/part-07-agent/81-workflow.md` 及相邻章节；当前主线已覆盖durable DAG/state、checkpoint、retry、compensation、external evidence 与 commit authority。正文尚未明确承载本 family 的增量：可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery。 Owner snapshot sha256=`a8a935c80e5047500f9c7beb334a74ac83381e49176a11f8beaa8b3da089fa92`；相邻章节=`books/part-07-agent/80-reflection.md, books/part-07-agent/82-multi-agent.md`。<!-- existing:SF-2026-ARXIV-2605-15132:end -->
<!-- delta:SF-2026-ARXIV-2605-15132:start -->可并行 Agent workflow 应把 dependency DAG、task state、worker placement 与 aggregation commit 分离；吞吐扩展不能牺牲依赖一致性与 failure recovery<!-- delta:SF-2026-ARXIV-2605-15132:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15132:end -->
<!-- books-review:SF-2026-ARXIV-2605-15138:start -->
<!-- existing:SF-2026-ARXIV-2605-15138:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15138:end -->
<!-- delta:SF-2026-ARXIV-2605-15138:start -->unlearning release gate 必须在最终量化 artifact 上复验，而不只验 full-precision checkpoint；更新小于 quantization bin 时会被压缩抹除，需要 circuit-local permanence 与 utility 双验收<!-- delta:SF-2026-ARXIV-2605-15138:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15138:end -->
<!-- books-review:SF-2026-ARXIV-2605-15152:start -->
<!-- existing:SF-2026-ARXIV-2605-15152:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15152:end -->
<!-- delta:SF-2026-ARXIV-2605-15152:start -->模型供应链验收必须比较 full-precision 与实际 AWQ/GPTQ/GGUF 等量化 artifact 的行为；outlier-induced rounding 可把量化步骤变成隐藏触发器<!-- delta:SF-2026-ARXIV-2605-15152:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15152:end -->
<!-- books-review:SF-2026-ARXIV-2605-15155:start -->
<!-- existing:SF-2026-ARXIV-2605-15155:start -->已读取 `books/part-04-training-system/33-grpo.md` 及相邻章节；当前主线已覆盖trajectory grouping、verifier/environment reward、token/sequence credit、KL/clipping 与 rollout-policy identity。本 family 的增量“Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8`；相邻章节=`books/part-04-training-system/32-ppo.md, books/part-04-training-system/34-dpo.md`。<!-- existing:SF-2026-ARXIV-2605-15155:end -->
<!-- delta:SF-2026-ARXIV-2605-15155:start -->Agent RL 的 privileged self-teacher 只能作为 detached、按 token gap gating 的辅助 signal；environment/verifier reward 保留 trajectory truth，错误 skill retrieval 不能让 teacher rejection 主导更新<!-- delta:SF-2026-ARXIV-2605-15155:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15155:end -->
<!-- books-review:SF-2026-ARXIV-2605-15164:start -->
<!-- existing:SF-2026-ARXIV-2605-15164:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15164:end -->
<!-- delta:SF-2026-ARXIV-2605-15164:start -->behavioural evaluation 只能支持可观察行为声明，不能独立验证 hidden objective、loss-of-control absence 等内部或反事实安全命题<!-- delta:SF-2026-ARXIV-2605-15164:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15164:end -->
<!-- books-review:SF-2026-ARXIV-2605-15172:start -->
<!-- existing:SF-2026-ARXIV-2605-15172:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-15172:end -->
<!-- delta:SF-2026-ARXIV-2605-15172:start -->backdoor release testing 不能只变换内容：position/length metadata 也可成为不可见 trigger，因此 clean semantics、长度切片与 position-encoding interventions 必须共同进入验收<!-- delta:SF-2026-ARXIV-2605-15172:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15172:end -->
<!-- books-review:SF-2026-ARXIV-2605-15178:start -->
<!-- existing:SF-2026-ARXIV-2605-15178:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。本 family 的增量“minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15178:end -->
<!-- delta:SF-2026-ARXIV-2605-15178:start -->minute-scale controllable video generation通过 hybrid linear/softmax attention、camera-control branch与two-stage refinement扩展 rollout；但视觉一致和相机遵循仍不等于 action-conditioned causal world state<!-- delta:SF-2026-ARXIV-2605-15178:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15178:end -->
<!-- books-review:SF-2026-ARXIV-2605-15184:start -->
<!-- existing:SF-2026-ARXIV-2605-15184:start -->已读取 `books/part-07-agent/76-rag.md` 及相邻章节；当前主线已覆盖corpus identity、retrieval trajectory、evidence provenance、citation 与 answer claim 的绑定。本 family 的增量“Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`9fbd3e0d51f58631aa1874a5ac618b37c4b1b7dfff667bc59293c5a2848e6510`；相邻章节=`books/part-07-agent/75-context.md, books/part-07-agent/77-memory.md`。<!-- existing:SF-2026-ARXIV-2605-15184:end -->
<!-- delta:SF-2026-ARXIV-2605-15184:start -->Agent search 评测必须把 retrieval strategy、harness/tool interface 与 corpus access 联合冻结；grep 或 vector retrieval 的结论不能脱离 harness<!-- delta:SF-2026-ARXIV-2605-15184:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15184:end -->
<!-- books-review:SF-2026-ARXIV-2605-15185:start -->
<!-- existing:SF-2026-ARXIV-2605-15185:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及相邻章节；当前主线已覆盖observation quality、action-conditioned transition、geometry、persistent world state 与 planning handoff。正文尚未明确承载本 family 的增量：视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability。 Owner snapshot sha256=`2b8a3f6f457ba203854a2b4078d943ca0b14422f842cad9ee4809b1e86684998`；相邻章节=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md, books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。<!-- existing:SF-2026-ARXIV-2605-15185:end -->
<!-- delta:SF-2026-ARXIV-2605-15185:start -->视频 world-model 评测应把视觉质量与可度量的 3D geometric consistency 分开，并用 camera/scene geometry 诊断 perspective distortion；该指标不等于 causal controllability<!-- delta:SF-2026-ARXIV-2605-15185:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15185:end -->
<!-- books-review:SF-2026-ARXIV-2605-15188:start -->
<!-- existing:SF-2026-ARXIV-2605-15188:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。本 family 的增量“开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-15188:end -->
<!-- delta:SF-2026-ARXIV-2605-15188:start -->开放世界 Agent 评测应冻结历史时钟、逐步释放外生事件并用预测/outcome轨迹评分 adaptation；静态 knowledge cutoff 问答不能代表持续适应<!-- delta:SF-2026-ARXIV-2605-15188:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-15188:end -->
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
<!-- books-review:SF-2026-ARXIV-2605-16436:start -->
<!-- existing:SF-2026-ARXIV-2605-16436:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及相邻章节；当前主线已覆盖identity、typed capability、least privilege、policy mediation、effect boundary 与 audit。本 family 的增量“Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`45cdedd789e1517c5cd110897cbfaf39b57453fe2bc94b9bc64d72ffa4612bb3`；相邻章节=`books/part-06-ai-infrastructure/71-multi-tenant.md, books/part-06-ai-infrastructure/73-production-best-practice.md`。<!-- existing:SF-2026-ARXIV-2605-16436:end -->
<!-- delta:SF-2026-ARXIV-2605-16436:start -->Agentic AI 降低高拟真攻击的边际成本，使 rate limit、identity proof 与 human vigilance 的旧经济假设失效；position analysis 不证明具体控制已有效<!-- delta:SF-2026-ARXIV-2605-16436:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16436:end -->
<!-- books-review:SF-2026-ARXIV-2605-16439:start -->
<!-- existing:SF-2026-ARXIV-2605-16439:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及相邻章节；当前主线已覆盖KV identity、residency、compression/eviction quality、rollback 与 workload-bound correctness。本 family 的增量“VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend”未改变现有 owner 或设计结论，因此留在 Daily 作为受限证据。 Owner snapshot sha256=`eb1d588cb78640e5a75ba6759724e661d8aae6d976d9bebe394627c4148707db`；相邻章节=`books/part-05-inference-system/44-decode.md, books/part-05-inference-system/46-continuous-batching.md`。<!-- existing:SF-2026-ARXIV-2605-16439:end -->
<!-- delta:SF-2026-ARXIV-2605-16439:start -->VLM KV compression 应利用视觉与文本 token 的非对称冗余并按序列阶段保留信息；局部压缩收益不能外推到任意模态、长度或 backend<!-- delta:SF-2026-ARXIV-2605-16439:end --> Decision: `No Change — Existing Coverage`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16439:end -->
<!-- books-review:SF-2026-ARXIV-2605-18859:start -->
<!-- existing:SF-2026-ARXIV-2605-18859:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及相邻章节；当前主线已覆盖model、harness、environment、scorer、budget、provenance 与 release authority 的完整评测身份。正文尚未明确承载本 family 的增量：Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告。 Owner snapshot sha256=`66cd622a2aa49f23d15886aa07e741d61045c772e0d387f6fd7fcc1094d0a8ab`；相邻章节=`books/part-06-ai-infrastructure/65-kai-scheduler.md, books/part-06-ai-infrastructure/67-monitoring.md`。<!-- existing:SF-2026-ARXIV-2605-18859:end -->
<!-- delta:SF-2026-ARXIV-2605-18859:start -->Agent model routing benchmark 必须给 router 真实 step prefix，并以完整 environment execution 验证替换后果；static replay 与 live dynamic track 应分开报告<!-- delta:SF-2026-ARXIV-2605-18859:end --> Decision: `Integrate`；author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18859:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260515-INDEPENDENT-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260515 | — | 668/668 replay；author denominator 漏收的 27 项均恢复 exact-v1 Review；56 retained / 612 closures；false positive 0 | passed |
| SA-20260515-INDEPENDENT-EVIDENCE | fresh-context:may2026-day01 | evidence | review:SF-2026-ARXIV-2605-14241 | — | 56/56 exact-v1；54 HTML + 2 official PDF；blocked=0、ordinary pending=0 | passed |
| SA-20260515-INDEPENDENT-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-MEMORY-LINEAGE-GATE | — | 三项 narrative 分别覆盖 memory/action、generation/checking、routing/environment ownership transition | passed |
| SA-20260515-BOOKS-POSTWRITE | fresh-context:may2026-day03 | books | books-review:SF-2026-ARXIV-2605-14241; books-review:SF-2026-ARXIV-2605-18859 | — | prewrite 15→13；写回后 13/13 marker 唯一且位于首个二级 Review notes 前，机制、旧路径、约束、owner、代价、failure、fallback、evidence boundary 与相邻 owner 均通过 | passed |

独立审计已关闭 Coverage 与 Evidence；root 的 13 项串行写回又经不同非写作者完成 post-write semantic audit，Books Gate 已通过。

## 8. Ignored Noise

完整 612 项 pre-denominator closure 位于 `../_sources/daily-20260515/screening-ledger-final.json`。每行保留标题、摘要机制、排除边界与重开条件；它们不因 AI 相关性自动进入 denominator。

## 9. Recommended Action

13 项 final queue 已按 owner 合并进共享 Books，并由非写作者逐项验证正文真实存在、位于首个二级 `## Review notes` 前，且保留旧路径、约束变化、owner、收益/代价、failure、fallback 与 coexistence。审计结果见 `papers/2026/05/_sources/daily-20260515/post-write-semantic-audit.json`。

## 10. Repository Changes

- 新建 2026-05-15 date-local Daily、screening ledger、exact-v1 Review、provenance、Books comparison、queue 与 post-write audit。
- 共享 Books 已由 root 串行写回；本 reviewer 未修改共享 Books，未 stage、commit 或 push。

## 11. Open Questions

- 无未解决问题；后续新证据若改变 owner 或 exact-v1 boundary，再按 Source Family 重开。

## 12. Sources

- DataCite adjacent-month v2 snapshot（identity/date/abstract recovery only）
- [Latency-Quality Routing for Functionally Equivalent Tools in LLM Agents](https://arxiv.org/html/2605.14241v1) — arXiv:2605.14241v1；first-public 2026-05-14；accessed 2026-09-01
- [EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization](https://arxiv.org/html/2605.14249v1) — arXiv:2605.14249v1；first-public 2026-05-14；accessed 2026-09-01
- [Auditing Agent Harness Safety](https://arxiv.org/html/2605.14271v1) — arXiv:2605.14271v1；first-public 2026-05-14；accessed 2026-09-01
- [Web Agents Should Adopt the Plan-Then-Execute Paradigm](https://arxiv.org/html/2605.14290v1) — arXiv:2605.14290v1；first-public 2026-05-14；accessed 2026-09-01
- [Factorization-Error-Free Discrete Diffusion Language Model via Speculative Decoding](https://arxiv.org/html/2605.14305v1) — arXiv:2605.14305v1；first-public 2026-05-14；accessed 2026-09-01
- [SWE-Chain: Benchmarking Coding Agents on Chained Release-Level Package Upgrades](https://arxiv.org/html/2605.14415v1) — arXiv:2605.14415v1；first-public 2026-05-14；accessed 2026-09-01
- [MemLineage: Lineage-Guided Enforcement for LLM Agent Memory](https://arxiv.org/html/2605.14421v1) — arXiv:2605.14421v1；first-public 2026-05-14；accessed 2026-09-01
- [Exploiting LLM Agent Supply Chains via Payload-less Skills](https://arxiv.org/html/2605.14460v1) — arXiv:2605.14460v1；first-public 2026-05-14；accessed 2026-09-01
- [Does RAG Know When Retrieval Is Wrong? Diagnosing Context Compliance under Knowledge Conflict](https://arxiv.org/html/2605.14473v1) — arXiv:2605.14473v1；first-public 2026-05-14；accessed 2026-09-01
- [LEMON: Learning Executable Multi-Agent Orchestration via Counterfactual Reinforcement Learning](https://arxiv.org/html/2605.14483v1) — arXiv:2605.14483v1；first-public 2026-05-14；accessed 2026-09-01
- [GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations](https://arxiv.org/html/2605.14498v1) — arXiv:2605.14498v1；first-public 2026-05-14；accessed 2026-09-01
- [Defenses at Odds: Measuring and Explaining Defense Conflicts in Large Language Models](https://arxiv.org/html/2605.14514v1) — arXiv:2605.14514v1；first-public 2026-05-14；accessed 2026-09-01
- [Uncertainty Quantification for Large Language Diffusion Models](https://arxiv.org/html/2605.14570v1) — arXiv:2605.14570v1；first-public 2026-05-14；accessed 2026-09-01
- [Privacy Auditing with Zero (0) Training Run](https://arxiv.org/html/2605.14591v1) — arXiv:2605.14591v1；first-public 2026-05-14；accessed 2026-09-01
- [Teaching Large Language Models When Not to Know: Learning Temporal Critique for Ex-Ante Reasoning](https://arxiv.org/html/2605.14636v1) — arXiv:2605.14636v1；first-public 2026-05-14；accessed 2026-09-01
- [$π$-Bench: Evaluating Proactive Personal Assistant Agents in Long-Horizon Workflows](https://arxiv.org/html/2605.14678v1) — arXiv:2605.14678v1；first-public 2026-05-14；accessed 2026-09-01
- [Mechanical Enforcement for LLM Governance:Evidence of Governance-Task Decoupling in Financial Decision Systems](https://arxiv.org/html/2605.14744v1) — arXiv:2605.14744v1；first-public 2026-05-14；accessed 2026-09-01
- [Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining](https://arxiv.org/html/2605.14747v1) — arXiv:2605.14747v1；first-public 2026-05-14；accessed 2026-09-01
- [Known By Their Actions: Fingerprinting LLM Browser Agents via UI Traces](https://arxiv.org/html/2605.14786v1) — arXiv:2605.14786v1；first-public 2026-05-14；accessed 2026-09-01
- [Do Coding Agents Understand Least-Privilege Authorization?](https://arxiv.org/html/2605.14859v1) — arXiv:2605.14859v1；first-public 2026-05-14；accessed 2026-09-01
- [Holistic Evaluation and Failure Diagnosis of AI Agents](https://arxiv.org/html/2605.14865v1) — arXiv:2605.14865v1；first-public 2026-05-14；accessed 2026-09-01
- [MemLens: Benchmarking Multimodal Long-Term Memory in Large Vision-Language Models](https://arxiv.org/html/2605.14906v1) — arXiv:2605.14906v1；first-public 2026-05-14；accessed 2026-09-01
- [Toward Securing AI Agents Like Operating Systems](https://arxiv.org/html/2605.14932v1) — arXiv:2605.14932v1；first-public 2026-05-14；accessed 2026-09-01
- [GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation](https://arxiv.org/html/2605.14968v1) — arXiv:2605.14968v1；first-public 2026-05-14；accessed 2026-09-01
- [Performance-Driven Policy Optimization for Speculative Decoding with Adaptive Windowing](https://arxiv.org/html/2605.14978v1) — arXiv:2605.14978v1；first-public 2026-05-14；accessed 2026-09-01
- [WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections](https://arxiv.org/html/2605.15030v1) — arXiv:2605.15030v1；first-public 2026-05-14；accessed 2026-09-01
- [AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models](https://arxiv.org/html/2605.15034v1) — arXiv:2605.15034v1；first-public 2026-05-14；accessed 2026-09-01
- [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/html/2605.15051v1) — arXiv:2605.15051v1；first-public 2026-05-14；accessed 2026-09-01
- [Croissant Baker: Metadata Generation for Discoverable, Governable, and Reusable ML Datasets](https://arxiv.org/html/2605.15079v1) — arXiv:2605.15079v1；first-public 2026-05-14；accessed 2026-09-01
- [Dual-Dimensional Consistency: Balancing Budget and Quality in Adaptive Inference-Time Scaling](https://arxiv.org/html/2605.15100v1) — arXiv:2605.15100v1；first-public 2026-05-14；accessed 2026-09-01
- [Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG](https://arxiv.org/html/2605.15109v1) — arXiv:2605.15109v1；first-public 2026-05-14；accessed 2026-09-01
- [Talk is (Not) Cheap: A Taxonomy and Benchmark Coverage Audit for LLM Attacks](https://arxiv.org/html/2605.15118v1) — arXiv:2605.15118v1；first-public 2026-05-14；accessed 2026-09-01
- [MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/html/2605.15128v1) — arXiv:2605.15128v1；first-public 2026-05-14；accessed 2026-09-01
- [APWA: A Distributed Architecture for Parallelizable Agentic Workflows](https://arxiv.org/html/2605.15132v1) — arXiv:2605.15132v1；first-public 2026-05-14；accessed 2026-09-01
- [Forgetting That Sticks: Quantization-Permanent Unlearning via Circuit Attribution](https://arxiv.org/html/2605.15138v1) — arXiv:2605.15138v1；first-public 2026-05-14；accessed 2026-09-01
- [Widening the Gap: Exploiting LLM Quantization via Outlier Injection](https://arxiv.org/html/2605.15152v1) — arXiv:2605.15152v1；first-public 2026-05-14；accessed 2026-09-01
- [Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/html/2605.15155v1) — arXiv:2605.15155v1；first-public 2026-05-14；accessed 2026-09-01
- [Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands](https://arxiv.org/html/2605.15164v1) — arXiv:2605.15164v1；first-public 2026-05-14；accessed 2026-09-01
- [MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs](https://arxiv.org/html/2605.15172v1) — arXiv:2605.15172v1；first-public 2026-05-14；accessed 2026-09-01
- [SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](https://arxiv.org/html/2605.15178v1) — arXiv:2605.15178v1；first-public 2026-05-14；accessed 2026-09-01
- [Is Grep All You Need? How Agent Harnesses Reshape Agentic Search](https://arxiv.org/html/2605.15184v1) — arXiv:2605.15184v1；first-public 2026-05-14；accessed 2026-09-01
- [Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/html/2605.15185v1) — arXiv:2605.15185v1；first-public 2026-05-14；accessed 2026-09-01
- [FutureSim: Replaying World Events to Evaluate Adaptive Agents](https://arxiv.org/html/2605.15188v1) — arXiv:2605.15188v1；first-public 2026-05-14；accessed 2026-09-01
- [Hydra: Efficient, Correct Code Generation via Checkpoint-and-Rollback Support](https://arxiv.org/html/2605.15238v1) — arXiv:2605.15238v1；first-public 2026-05-14；accessed 2026-09-01
- [Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/html/2605.15257v1) — arXiv:2605.15257v1；first-public 2026-05-14；accessed 2026-09-01
- [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/html/2605.15338v1) — arXiv:2605.15338v1；first-public 2026-05-14；accessed 2026-09-01
- [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/html/2605.15377v1) — arXiv:2605.15377v1；first-public 2026-05-14；accessed 2026-09-01
- [Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory](https://arxiv.org/html/2605.15384v1) — arXiv:2605.15384v1；first-public 2026-05-14；accessed 2026-09-01
- [$ϕ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/html/2605.15403v1) — arXiv:2605.15403v1；first-public 2026-05-14；accessed 2026-09-01
- [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/html/2605.15422v1) — arXiv:2605.15422v1；first-public 2026-05-14；accessed 2026-09-01
- [Runtime-Structured Task Decomposition for Agentic Coding Systems](https://arxiv.org/html/2605.15425v1) — arXiv:2605.15425v1；first-public 2026-05-14；accessed 2026-09-01
- [Entity-Centric World Models: Interaction-Aware Masking for Causal Video Prediction](https://arxiv.org/html/2605.15466v1) — arXiv:2605.15466v1；first-public 2026-05-14；accessed 2026-09-01
- [EgoExo-WM: Unlocking Exo Video for Ego World Models](https://arxiv.org/html/2605.15477v1) — arXiv:2605.15477v1；first-public 2026-05-14；accessed 2026-09-01
- [The End of Trust: How Agentic AI Breaks Security Assumptions](https://arxiv.org/html/2605.16436v1) — arXiv:2605.16436v1；first-public 2026-05-14；accessed 2026-09-01
- [KVCapsule: Efficient Sequential KV Cache Compression for Vision-Language Models with Asymmetric Redundancy](https://arxiv.org/html/2605.16439v1) — arXiv:2605.16439v1；first-public 2026-05-14；accessed 2026-09-01
- [TwinRouterBench: Fast Static and Live Dynamic Evaluation for Realistic Agentic LLM Routing](https://arxiv.org/html/2605.18859v1) — arXiv:2605.18859v1；first-public 2026-05-14；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

非作者 fresh-context audit 已完成 668/668 screening、56-family denominator、56/56 exact-v1 Evidence 与 15→13 current-Books challenge；13/13 Books writeback 已通过不同 reviewer 的 post-write semantic audit，本日完整闭环。
