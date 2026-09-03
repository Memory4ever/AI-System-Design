# Daily Research — 2026-05-01

**Research Date:** 2026-05-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-04-30 09:00:00 ～ 2026-05-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed（24 个 Source Family 已完成串行写回与非写作者 post-write 语义审计）

## Executive Summary

完整回放联合 `2604 + 2605` 两个月的 DataCite DOI-prefix 快照，从 59,801 个唯一 DOI 中按 `Submitted:v1` 严格过滤出 **1204** 个窗口内 identity；注册分类命中 **532** 项（Core 370、keyword route 162）。此前 311/139 是不完整快照产生的错误分母，本报告不继承。
532 条 title+abstract 逐项筛选后，拟冻结 **56** 个 Candidate Source Family（10.53%），其余 **476** 项均在 screening ledger 留下 family-specific pre-denominator closure。56 项完成 exact-v1 Method/Evaluation/Limitations 边界、Score V2、Books Comparison 与最多三条 Deep Analysis；其中 24 项进入共享 Books 串行写回队列。
独立 fresh-context 审计重新检查了 532 行筛选账本、56 份 exact-v1 Review 与 current Books：恢复 6 个 false negative，将 VitaLLM 重复投稿折叠到一个 family，并把 7 个已有正文完整覆盖的 provisional Integrate 降级。root 随后按最终 24-family 队列完成串行正文写回；非写作者逐项顺读 owner/adjacent，确认旧方案、约束变化、state/control ownership、trade-off、failure、fallback、evidence boundary 与非重复 ownership 均已进入相应演进链。Coverage、Evidence、Selection 与 Books Gate 均已通过。

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
| Denominator ID | DEN-20260501-dcbf67b37187e1551d50 |
| Denominator Frozen At | 2026-09-01T00:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-04-30T09:00:00+08:00 | 2026-05-01T09:00:00+08:00 | 2026-08-31T23:10:00+08:00 | registered Core + keyword categories; full title+abstract semantic screening | checked | 1204 | SF-2026-ARXIV-2604-27289<br>SF-2026-ARXIV-2604-27292<br>SF-2026-ARXIV-2604-27309<br>SF-2026-ARXIV-2604-27792<br>SF-2026-ARXIV-2604-27844<br>SF-2026-ARXIV-2604-28138<br>SF-2026-ARXIV-2604-28139<br>SF-2026-ARXIV-2605-00066<br>SF-2026-ARXIV-2605-00081<br>SF-2026-ARXIV-2605-00136<br>SF-2026-ARXIV-2605-00155<br>SF-2026-ARXIV-2605-00161<br>SF-2026-ARXIV-2605-00180<br>SF-2026-ARXIV-2605-00206<br>SF-2026-ARXIV-2605-00254<br>SF-2026-ARXIV-2605-00267<br>SF-2026-ARXIV-2605-00300<br>SF-2026-ARXIV-2605-00314<br>SF-2026-ARXIV-2604-27306<br>SF-2026-ARXIV-2604-27351<br>SF-2026-ARXIV-2604-27358<br>SF-2026-ARXIV-2604-27393<br>SF-2026-ARXIV-2604-27405<br>SF-2026-ARXIV-2604-27419<br>SF-2026-ARXIV-2604-27426<br>SF-2026-ARXIV-2604-27488<br>SF-2026-ARXIV-2604-27536<br>SF-2026-ARXIV-2604-27586<br>SF-2026-ARXIV-2604-27637<br>SF-2026-ARXIV-2604-27660<br>SF-2026-ARXIV-2604-27695<br>SF-2026-ARXIV-2604-27707<br>SF-2026-ARXIV-2604-27711<br>SF-2026-ARXIV-2604-27776<br>SF-2026-ARXIV-2604-27789<br>SF-2026-ARXIV-2604-27819<br>SF-2026-ARXIV-2604-27855<br>SF-2026-ARXIV-2604-27906<br>SF-2026-ARXIV-2604-28056<br>SF-2026-ARXIV-2604-28123<br>SF-2026-ARXIV-2604-28129<br>SF-2026-ARXIV-2604-28157<br>SF-2026-ARXIV-2604-28158<br>SF-2026-ARXIV-2604-28175<br>SF-2026-ARXIV-2604-28181<br>SF-2026-ARXIV-2604-28182<br>SF-2026-ARXIV-2604-28190<br>SF-2026-ARXIV-2604-28196<br>SF-2026-ARXIV-2604-27891<br>SF-2026-ARXIV-2605-00226<br>SF-2026-ARXIV-2604-27396<br>SF-2026-ARXIV-2604-27467<br>SF-2026-ARXIV-2604-27486<br>SF-2026-ARXIV-2604-27781<br>SF-2026-ARXIV-2604-27861<br>SF-2026-ARXIV-2604-27878 | complete disjoint 2604/2605 DataCite DOI-prefix snapshots, 00..99, all pages/cursors closed | 2026-05-01T01:00:00Z | coverage:SRC-ARXIV:20260501 | — |

<!-- coverage:SRC-ARXIV:20260501:start -->
`datacite-arxiv-202604-v2` 与 `datacite-arxiv-202605-v2` 共覆盖 59,801 个唯一 DOI；严格窗口命中 1204，其中注册 route 532（2604 前缀 398、2605 前缀 134）。screening ledger 逐项闭合为 56 retained + 476 pre-denominator closures。DataCite 只证明 identity/subject/submitted metadata，所有机制结论回到 exact-v1 arXiv HTML。
<!-- coverage:SRC-ARXIV:20260501:end -->

### Coverage Limitations

- official arXiv Atom/OAI 枚举端点在恢复时不可访问；完整、互斥的 DataCite 00..99 分区用于 identity/date routing，独立 auditor 已逐项复核 532 个 registered identity，因此该 fallback 不再保持 Coverage Open。
- 注册表中 2026-08-25 才生效的组织来源不追溯成为本历史 Daily 的 Required；本轮唯一到期 Required source 是 `SRC-ARXIV`。
- 56 份 retained family 均回到 exact-v1 HTML 完成 Method、Evaluation 与 non-proof Review；DataCite 不支持任何机制结论。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | arXiv:2604.27289v1 | paper-v1:2604.27289 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27289 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27289 | yes |
| SF-2026-ARXIV-2604-27292 | arXiv:2604.27292v1 | paper-v1:2604.27292 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27292 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27292 | yes |
| SF-2026-ARXIV-2604-27309 | arXiv:2604.27309v1 | paper-v1:2604.27309 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27309 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27309 | yes |
| SF-2026-ARXIV-2604-27792 | arXiv:2604.27792v1 | paper-v1:2604.27792 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27792 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27792 | yes |
| SF-2026-ARXIV-2604-27844 | arXiv:2604.27844v1 | paper-v1:2604.27844 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27844 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2604-27844 | yes |
| SF-2026-ARXIV-2604-28138 | arXiv:2604.28138v1 | paper-v1:2604.28138 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28138 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2604-28138 | yes |
| SF-2026-ARXIV-2604-28139 | arXiv:2604.28139v1 | paper-v1:2604.28139 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28139 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28139 | yes |
| SF-2026-ARXIV-2605-00066 | arXiv:2605.00066v1 | paper-v1:2605.00066 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00066 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00066 | yes |
| SF-2026-ARXIV-2605-00081 | arXiv:2605.00081v1 | paper-v1:2605.00081 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00081 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00081 | yes |
| SF-2026-ARXIV-2605-00136 | arXiv:2605.00136v1 | paper-v1:2605.00136 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00136 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00136 | yes |
| SF-2026-ARXIV-2605-00155 | arXiv:2605.00155v1 | paper-v1:2605.00155 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-00155 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00155 | yes |
| SF-2026-ARXIV-2605-00161 | arXiv:2605.00161v1 | paper-v1:2605.00161 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00161 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00161 | yes |
| SF-2026-ARXIV-2605-00180 | arXiv:2605.00180v1 | paper-v1:2605.00180 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00180 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00180 | yes |
| SF-2026-ARXIV-2605-00206 | arXiv:2605.00206v1 | paper-v1:2605.00206 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00206 | self | — | new_in_window | MODEL-DECODER-ONLY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00206 | yes |
| SF-2026-ARXIV-2605-00254 | arXiv:2605.00254v1 | paper-v1:2605.00254 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00254 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-00254 | yes |
| SF-2026-ARXIV-2605-00267 | arXiv:2605.00267v1 | paper-v1:2605.00267 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00267 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00267 | yes |
| SF-2026-ARXIV-2605-00300 | arXiv:2605.00300v1 | paper-v1:2605.00300 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-00300 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-00300 | yes |
| SF-2026-ARXIV-2605-00314 | arXiv:2605.00314v1 | paper-v1:2605.00314 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2605-00314 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-00314 | yes |
| SF-2026-ARXIV-2604-27306 | arXiv:2604.27306v1 | paper-v1:2604.27306 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27306 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2604-27306 | yes |
| SF-2026-ARXIV-2604-27351 | arXiv:2604.27351v1 | paper-v1:2604.27351 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27351 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27351 | yes |
| SF-2026-ARXIV-2604-27358 | arXiv:2604.27358v1 | paper-v1:2604.27358 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27358 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2604-27358 | yes |
| SF-2026-ARXIV-2604-27393 | arXiv:2604.27393v1 | paper-v1:2604.27393 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27393 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27393 | yes |
| SF-2026-ARXIV-2604-27405 | arXiv:2604.27405v1 | paper-v1:2604.27405 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27405 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27405 | yes |
| SF-2026-ARXIV-2604-27419 | arXiv:2604.27419v1 | paper-v1:2604.27419 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27419 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27419 | yes |
| SF-2026-ARXIV-2604-27426 | arXiv:2604.27426v1 | paper-v1:2604.27426 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27426 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-27426 | yes |
| SF-2026-ARXIV-2604-27488 | arXiv:2604.27488v1 | paper-v1:2604.27488 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27488 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27488 | yes |
| SF-2026-ARXIV-2604-27536 | arXiv:2604.27536v1 | paper-v1:2604.27536 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27536 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2604-27536 | yes |
| SF-2026-ARXIV-2604-27586 | arXiv:2604.27586v1 | paper-v1:2604.27586 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27586 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2604-27586 | yes |
| SF-2026-ARXIV-2604-27637 | arXiv:2604.27637v1 | paper-v1:2604.27637 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27637 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27637 | yes |
| SF-2026-ARXIV-2604-27660 | arXiv:2604.27660v1 | paper-v1:2604.27660 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27660 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27660 | yes |
| SF-2026-ARXIV-2604-27695 | arXiv:2604.27695v1 | paper-v1:2604.27695 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27695 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27695 | yes |
| SF-2026-ARXIV-2604-27707 | arXiv:2604.27707v1 | paper-v1:2604.27707 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27707 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27707 | yes |
| SF-2026-ARXIV-2604-27711 | arXiv:2604.27711v1 | paper-v1:2604.27711 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27711 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27711 | yes |
| SF-2026-ARXIV-2604-27776 | arXiv:2604.27776v1 | paper-v1:2604.27776 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27776 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27776 | yes |
| SF-2026-ARXIV-2604-27789 | arXiv:2604.27789v1 | paper-v1:2604.27789 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27789 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27789 | yes |
| SF-2026-ARXIV-2604-27819 | arXiv:2604.27819v1 | paper-v1:2604.27819 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27819 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2604-27819 | yes |
| SF-2026-ARXIV-2604-27855 | arXiv:2604.27855v1 | paper-v1:2604.27855 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27855 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2604-27855 | yes |
| SF-2026-ARXIV-2604-27906 | arXiv:2604.27906v1 | paper-v1:2604.27906 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27906 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27906 | yes |
| SF-2026-ARXIV-2604-28056 | arXiv:2604.28056v1 | paper-v1:2604.28056 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28056 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28056 | yes |
| SF-2026-ARXIV-2604-28123 | arXiv:2604.28123v1 | paper-v1:2604.28123 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28123 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28123 | yes |
| SF-2026-ARXIV-2604-28129 | arXiv:2604.28129v1 | paper-v1:2604.28129 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28129 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2604-28129 | yes |
| SF-2026-ARXIV-2604-28157 | arXiv:2604.28157v1 | paper-v1:2604.28157 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28157 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28157 | yes |
| SF-2026-ARXIV-2604-28158 | arXiv:2604.28158v1 | paper-v1:2604.28158 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28158 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28158 | yes |
| SF-2026-ARXIV-2604-28175 | arXiv:2604.28175v1 | paper-v1:2604.28175 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28175 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2604-28175 | yes |
| SF-2026-ARXIV-2604-28181 | arXiv:2604.28181v1 | paper-v1:2604.28181 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28181 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28181 | yes |
| SF-2026-ARXIV-2604-28182 | arXiv:2604.28182v1 | paper-v1:2604.28182 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-28182 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2604-28182 | yes |
| SF-2026-ARXIV-2604-28190 | arXiv:2604.28190v1 | paper-v1:2604.28190 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-28190 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2604-28190 | yes |
| SF-2026-ARXIV-2604-28196 | arXiv:2604.28196v1 | paper-v1:2604.28196 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-28196 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28196 | yes |
| SF-2026-ARXIV-2604-27891 | arXiv:2604.27891v1 | paper-v1:2604.27891 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27891 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2604-27891 | yes |
| SF-2026-ARXIV-2605-00226 | arXiv:2605.00226v1 | paper-v1:2605.00226 | 2026-W18 | 2026-05-01 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-00226 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00226 | yes |
| SF-2026-ARXIV-2604-27396 | arXiv:2604.27396v1 | paper-v1:2604.27396 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2604-27396 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27396 | yes |
| SF-2026-ARXIV-2604-27467 | arXiv:2604.27467v1 | paper-v1:2604.27467 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27467 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27467 | yes |
| SF-2026-ARXIV-2604-27486 | arXiv:2604.27486v1 | paper-v1:2604.27486 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27486 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2604-27486 | yes |
| SF-2026-ARXIV-2604-27781 | arXiv:2604.27781v1 | paper-v1:2604.27781 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27781 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27781 | yes |
| SF-2026-ARXIV-2604-27861 | arXiv:2604.27861v1 | paper-v1:2604.27861 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2604-27861 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27861 | yes |
| SF-2026-ARXIV-2604-27878 | arXiv:2604.27878v1 | paper-v1:2604.27878 | 2026-W18 | 2026-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2604-27878 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2604-27878 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | RP-8d01168c396cf39f | deep | arXiv:2604.27289v1 | SRC-ARXIV@arXiv:2604.27289v1 | https://arxiv.org/html/2604.27289v1 — §2.2-3.3 event types, governance operator and coinductive safety predicate; §8 mechanization; §9 verified interpreter specification | https://arxiv.org/html/2604.27289v1 — §8.3-8.5 36 Coq modules/454 results/zero admitted lemmas; §9 property-based conformance against BEAM runtime | https://arxiv.org/html/2604.27289v1 — §12 Limitations：formalization is system-specific; two named results remain paper proofs; proof covers the modeled effect boundary and does not establish policy correctness or arbitrary runtime behavior | Not Disclosed — public Coq artifact is declared in exact-v1, but this review did not independently rebuild it | claim:SF-2026-ARXIV-2604-27289 | complete |
| SF-2026-ARXIV-2604-27292 | RP-bc20b1a8b32d3636 | deep | arXiv:2604.27292v1 | SRC-ARXIV@arXiv:2604.27292v1 | https://arxiv.org/html/2604.27292v1 — §2-4 expressiveness/governance boundaries, Rice-theorem boundary and coterminous governance; §5-7 behavioral comparison and execution-pipeline consequence | https://arxiv.org/html/2604.27292v1 — §4 gives the testable structural criterion; formal claims defer to the companion Coq development rather than an independent empirical benchmark | https://arxiv.org/html/2604.27292v1 — §9 Limitations：scope is effects, existing frameworks may require re-architecture, structural coverage does not prove policy correctness, and restricted languages trade expressiveness for decidability | Not Disclosed — companion Coq repository is linked; this conceptual paper has no separate empirical artifact | claim:SF-2026-ARXIV-2604-27292 | complete |
| SF-2026-ARXIV-2604-27309 | RP-f4f235421b995920 | deep | arXiv:2604.27309v1 | SRC-ARXIV@arXiv:2604.27309v1 | https://arxiv.org/html/2604.27309v1 — §5.1-5.8 governance architecture, controlled experimentation, monitoring and cost | https://arxiv.org/html/2604.27309v1 — §2.1-2.6 seven versions, clinician rubrics, live feedback and technical performance | https://arxiv.org/html/2604.27309v1 — §3.6 single product/domain, observational feedback and short deployment window | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27309 | complete |
| SF-2026-ARXIV-2604-27792 | RP-63168f3aaa1fa18a | deep | arXiv:2604.27792v1 | SRC-ARXIV@arXiv:2604.27792v1 | https://arxiv.org/html/2604.27792v1 — §2 architecture, heterogeneous pre/post-training and real-time inference optimizations | https://arxiv.org/html/2604.27792v1 — §3 simulation, world-model and real-robot evaluations | https://arxiv.org/html/2604.27792v1 — §4 future work; no independent safety or broad sim-to-real guarantee | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27792 | complete |
| SF-2026-ARXIV-2604-27844 | RP-c36e7217b950b425 | deep | arXiv:2604.27844v1 | SRC-ARXIV@arXiv:2604.27844v1 | https://arxiv.org/html/2604.27844v1 — §3-5 compressed collective API, exponent coding, GPU pipeline and adaptive switcher | https://arxiv.org/html/2604.27844v1 — §6 dense/MoE training on 64 GPUs with collective and end-to-end comparisons | https://arxiv.org/html/2604.27844v1 — §6.6 observed tensor normality is workload-specific; paper does not prove universal distributions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27844 | complete |
| SF-2026-ARXIV-2604-28138 | RP-90b1824f77774a01 | deep | arXiv:2604.28138v1 | SRC-ARXIV@arXiv:2604.28138v1 | https://arxiv.org/html/2604.28138v1 — §4-6 coordinator, eBPF inspector, C/R data plane and deployment refinement | https://arxiv.org/html/2604.28138v1 — §7 correctness, overhead, mechanism ablations and code-agent case study | https://arxiv.org/html/2604.28138v1 — §9 Conclusion — exact-v1 has no dedicated limitations section; evidence is confined to Linux sandbox workloads and evaluated C/R backends | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28138 | complete |
| SF-2026-ARXIV-2604-28139 | RP-60081ac3b24d9eb4 | deep | arXiv:2604.28139v1 | SRC-ARXIV@arXiv:2604.28139v1 | https://arxiv.org/html/2604.28139v1 — §3 refreshable signals, release snapshot, controlled fixtures and graders | https://arxiv.org/html/2604.28139v1 — §4-5 105 tasks, 13 models, trace/artifact grading and family-level analysis | https://arxiv.org/html/2604.28139v1 — §3.3 and §5.5 current release and ClawHub-derived demand are not a universal production distribution | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28139 | complete |
| SF-2026-ARXIV-2605-00066 | RP-b256a98e02edce7e | deep | arXiv:2605.00066v1 | SRC-ARXIV@arXiv:2605.00066v1 | https://arxiv.org/html/2605.00066v1 — §3 cross-benchmark metric mapping and correlation protocol | https://arxiv.org/html/2605.00066v1 — §4 NAVSIM and Bench2Drive cross-benchmark results and sensitivity | https://arxiv.org/html/2605.00066v1 — §5 selected benchmarks/models and correlation do not establish causality or real-world safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00066 | complete |
| SF-2026-ARXIV-2605-00081 | RP-f14b7451bc2abe88 | deep | arXiv:2605.00081v1 | SRC-ARXIV@arXiv:2605.00081v1 | https://arxiv.org/html/2605.00081v1 — §2-6 threat assumptions, contract language, dual-layer observability and enforcement | https://arxiv.org/html/2605.00081v1 — §7 examples and policy-composition analysis | https://arxiv.org/html/2605.00081v1 — §8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00081 | complete |
| SF-2026-ARXIV-2605-00136 | RP-0c1e52b0f31dc627 | deep | arXiv:2605.00136v1 | SRC-ARXIV@arXiv:2605.00136v1 | https://arxiv.org/html/2605.00136v1 — §3-4 decomposition of tool protocol, selection and execution costs | https://arxiv.org/html/2605.00136v1 — §5 controlled tool-use diagnosis across models/tasks | https://arxiv.org/html/2605.00136v1 — §6/discussion task and framework scope; no universal tax constant | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00136 | complete |
| SF-2026-ARXIV-2605-00155 | RP-04a48ab11447f01c | standard | arXiv:2605.00155v1 | SRC-ARXIV@arXiv:2605.00155v1 | https://arxiv.org/html/2605.00155v1 — §3-5 Wasserstein ambiguity set and robust regret objective | https://arxiv.org/html/2605.00155v1 — §6 experiments and ablations on specified preference datasets/models | Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00155 | complete |
| SF-2026-ARXIV-2605-00161 | RP-aa657a548813d802 | deep | arXiv:2605.00161v1 | SRC-ARXIV@arXiv:2605.00161v1 | https://arxiv.org/html/2605.00161v1 — §2-3 consistency objective and diffusion language-model mechanism | https://arxiv.org/html/2605.00161v1 — §4-5 language-model evaluations and ablations | https://arxiv.org/html/2605.00161v1 — §6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00161 | complete |
| SF-2026-ARXIV-2605-00180 | RP-e93e4da3b4fae9c2 | deep | arXiv:2605.00180v1 | SRC-ARXIV@arXiv:2605.00180v1 | https://arxiv.org/html/2605.00180v1 — §3 graph profile construction and cold-start transfer | https://arxiv.org/html/2605.00180v1 — §4-5 new-model routing experiments, baselines and ablations | https://arxiv.org/html/2605.00180v1 — §6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00180 | complete |
| SF-2026-ARXIV-2605-00206 | RP-9117d40ba6929c79 | deep | arXiv:2605.00206v1 | SRC-ARXIV@arXiv:2605.00206v1 | https://arxiv.org/html/2605.00206v1 — §2-4 nonlinear recurrence and parallel-training construction | https://arxiv.org/html/2605.00206v1 — §5 model/task evaluations and ablations | https://arxiv.org/html/2605.00206v1 — §6 limitations on scale, recurrence stability and broader workloads | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00206 | complete |
| SF-2026-ARXIV-2605-00254 | RP-8f98fbe491ce3d22 | deep | arXiv:2605.00254v1 | SRC-ARXIV@arXiv:2605.00254v1 | https://arxiv.org/html/2605.00254v1 — §3-5 topology/cost model, placement and routing mechanisms | https://arxiv.org/html/2605.00254v1 — §6 serving scenarios and topology comparisons | https://arxiv.org/html/2605.00254v1 — §7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00254 | complete |
| SF-2026-ARXIV-2605-00267 | RP-519dc6303a8b4fcf | deep | arXiv:2605.00267v1 | SRC-ARXIV@arXiv:2605.00267v1 | https://arxiv.org/html/2605.00267v1 — §3-4 jailbreak construction and capability-preservation protocol | https://arxiv.org/html/2605.00267v1 — §5 general and agentic task evaluations | https://arxiv.org/html/2605.00267v1 — §6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00267 | complete |
| SF-2026-ARXIV-2605-00300 | RP-fdcd665c797fb1a8 | deep | arXiv:2605.00300v1 | SRC-ARXIV@arXiv:2605.00300v1 | https://arxiv.org/html/2605.00300v1 — §3 endpoint-centric continuous benchmark and measurement protocol | https://arxiv.org/html/2605.00300v1 — §4-5 preference/cognition/energy evaluations | https://arxiv.org/html/2605.00300v1 — §6 discussion and limitations on provider drift, observability and evaluator scope | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00300 | complete |
| SF-2026-ARXIV-2605-00314 | RP-65299a52b0456f54 | deep | arXiv:2605.00314v1 | SRC-ARXIV@arXiv:2605.00314v1 | https://arxiv.org/html/2605.00314v1 — §3-5 representation synthesis, Datalog constraints and audit pipeline | https://arxiv.org/html/2605.00314v1 — §6 evaluation over skill corpus, attack cases and hardware setup | https://arxiv.org/html/2605.00314v1 — §7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00314 | complete |
| SF-2026-ARXIV-2604-27306 | RP-7a624eff73754d6e | deep | arXiv:2604.27306v1 | SRC-ARXIV@arXiv:2604.27306v1 | https://arxiv.org/html/2604.27306v1 — §3-4 nugget schema, lifecycle and retrieval pipeline | https://arxiv.org/html/2604.27306v1 — §5 three QA datasets, maintenance/update evaluation and ablations | https://arxiv.org/html/2604.27306v1 — §6/§7 selected QA corpora and author metrics do not prove a universal source-authority policy | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27306 | complete |
| SF-2026-ARXIV-2604-27351 | RP-2d2750371f17d19e | deep | arXiv:2604.27351v1 | SRC-ARXIV@arXiv:2604.27351v1 | https://arxiv.org/html/2604.27351v1 — §3 heterogeneous model collaboration and typed tool interface | https://arxiv.org/html/2604.27351v1 — §4 scientific task evaluations and collaboration ablations | https://arxiv.org/html/2604.27351v1 — §5 selected scientific models/tasks do not establish a universal planner or tool ontology | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27351 | complete |
| SF-2026-ARXIV-2604-27358 | RP-68859682ff71a1b1 | deep | arXiv:2604.27358v1 | SRC-ARXIV@arXiv:2604.27358v1 | https://arxiv.org/html/2604.27358v1 — §3-5 bilevel delegation objective, safety monotonicity and responsibility propagation | https://arxiv.org/html/2604.27358v1 — §5 formal convergence/safety analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 explicitly leaves empirical validation to future work; formal assumptions do not prove deployable runtime safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27358 | complete |
| SF-2026-ARXIV-2604-27393 | RP-e28a66921b9aa983 | deep | arXiv:2604.27393v1 | SRC-ARXIV@arXiv:2604.27393v1 | https://arxiv.org/html/2604.27393v1 — §2-3 native omni-modal architecture, full-duplex streaming and training | https://arxiv.org/html/2604.27393v1 — §4 multimodal understanding/generation and streaming interaction evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: model-specific training data, hardware and latency conditions bound the reported interaction quality | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27393 | complete |
| SF-2026-ARXIV-2604-27405 | RP-c121112f04498c1d | deep | arXiv:2604.27405v1 | SRC-ARXIV@arXiv:2604.27405v1 | https://arxiv.org/html/2604.27405v1 — §2-3 item-level Reliable Change Index adaptation and within-family comparison | https://arxiv.org/html/2604.27405v1 — §4 2,000 MMLU-Pro items, 10 samples and two model-family upgrades | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: two families and one benchmark do not calibrate a universal RCI threshold or production consequence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27405 | complete |
| SF-2026-ARXIV-2604-27419 | RP-5dd84be88df2a1c3 | deep | arXiv:2604.27419v1 | SRC-ARXIV@arXiv:2604.27419v1 | https://arxiv.org/html/2604.27419v1 — §3 benchmark environment, interaction protocol and graders | https://arxiv.org/html/2604.27419v1 — §4 multimodal web-agent baselines and error analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: website-generation tasks and benchmark fixtures do not establish general computer-use reliability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27419 | complete |
| SF-2026-ARXIV-2604-27426 | RP-042ebbf5d9f0e3a9 | deep | arXiv:2604.27426v1 | SRC-ARXIV@arXiv:2604.27426v1 | https://arxiv.org/html/2604.27426v1 — §3-4 malicious model-code supply-chain path and active execution hijacking | https://arxiv.org/html/2604.27426v1 — §5 secret-exfiltration experiments across local fine-tuning setups | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: demonstrated attacks do not establish ecosystem prevalence; controls depend on the actual loader/runtime boundary | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27426 | complete |
| SF-2026-ARXIV-2604-27488 | RP-3fa267da5f8e8f9c | deep | arXiv:2604.27488v1 | SRC-ARXIV@arXiv:2604.27488v1 | https://arxiv.org/html/2604.27488v1 — §3 Skills-Coach task generation, comparative execution and GRPO-style skill optimization | https://arxiv.org/html/2604.27488v1 — §4 agent-skill benchmarks, ablations and trace analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: author-generated tasks/judges and selected skills do not prove production release safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27488 | complete |
| SF-2026-ARXIV-2604-27536 | RP-e5f694dff5f04276 | deep | arXiv:2604.27536v1 | SRC-ARXIV@arXiv:2604.27536v1 | https://arxiv.org/html/2604.27536v1 — §2-4 POMDP formulation, verifiable observations and belief-guided routing | https://arxiv.org/html/2604.27536v1 — §5 service workloads, cost/reliability baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: proxy-verifier calibration and workload stationarity limit generalization to unseen services | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27536 | complete |
| SF-2026-ARXIV-2604-27586 | RP-dd077c3fd873a684 | deep | arXiv:2604.27586v1 | SRC-ARXIV@arXiv:2604.27586v1 | https://arxiv.org/html/2604.27586v1 — §3 trace-level contamination model, artifact transformations and divergence measures | https://arxiv.org/html/2604.27586v1 — §4 heterogeneous-document workflows and contamination interventions | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic workflows and chosen corruption models do not quantify real-world prevalence or causal completeness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27586 | complete |
| SF-2026-ARXIV-2604-27637 | RP-758e79a3d5b04d4d | deep | arXiv:2604.27637v1 | SRC-ARXIV@arXiv:2604.27637v1 | https://arxiv.org/html/2604.27637v1 — §2-3 per-model prompt-optimization protocol before evaluation | https://arxiv.org/html/2604.27637v1 — §4 model/task ranking changes under optimized versus static prompts | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected optimizers, tasks and search budgets do not define a universally fair evaluation regime | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27637 | complete |
| SF-2026-ARXIV-2604-27660 | RP-a100fb2b658328e5 | deep | arXiv:2604.27660v1 | SRC-ARXIV@arXiv:2604.27660v1 | https://arxiv.org/html/2604.27660v1 — §3 context-to-skill extraction, self-play generation and replay selection | https://arxiv.org/html/2604.27660v1 — §4 task suites, baselines and skill-transfer ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected tasks/models do not establish durable skill validity or safe cross-domain reuse | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27660 | complete |
| SF-2026-ARXIV-2604-27695 | RP-21533a279960d0b5 | deep | arXiv:2604.27695v1 | SRC-ARXIV@arXiv:2604.27695v1 | https://arxiv.org/html/2604.27695v1 — §3 evidence-gap diagnosis, layered memory and iterative retrieval controller | https://arxiv.org/html/2604.27695v1 — §4 long-conversation temporal/multi-hop benchmarks and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: benchmark conversations and author-defined gap labels do not prove production memory truthfulness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27695 | complete |
| SF-2026-ARXIV-2604-27707 | RP-b0079b58d321e90c | deep | arXiv:2604.27707v1 | SRC-ARXIV@arXiv:2604.27707v1 | https://arxiv.org/html/2604.27707v1 — §2-4 formal memo-versus-memory distinction and consolidation consequences | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; conceptual analysis and cited examples; no independent systems benchmark | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: position paper does not demonstrate a universally superior consolidation mechanism | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27707 | complete |
| SF-2026-ARXIV-2604-27711 | RP-3d571006c0e81857 | deep | arXiv:2604.27711v1 | SRC-ARXIV@arXiv:2604.27711v1 | https://arxiv.org/html/2604.27711v1 — §3 exocentric generation and control pipeline | https://arxiv.org/html/2604.27711v1 — §4 simulated and physical humanoid evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: video quality and selected tasks do not establish broad physical safety or sim-to-real robustness | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27711 | complete |
| SF-2026-ARXIV-2604-27776 | RP-7e11a857cb966cd7 | deep | arXiv:2604.27776v1 | SRC-ARXIV@arXiv:2604.27776v1 | https://arxiv.org/html/2604.27776v1 — §3 cross-application Windows environment and process-centric tasks | https://arxiv.org/html/2604.27776v1 — §4 agent baselines, process/terminal grading and error taxonomy | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: Windows applications and curated professions do not represent every production workspace | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27776 | complete |
| SF-2026-ARXIV-2604-27789 | RP-f84f0edd56cb5b51 | deep | arXiv:2604.27789v1 | SRC-ARXIV@arXiv:2604.27789v1 | https://arxiv.org/html/2604.27789v1 — §3-5 deployer contracts, update detection and compatibility-gate workflow | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; case studies and risk-suite demonstrations over hosted model changes | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: framework cannot observe undisclosed provider internals and depends on representative local suites | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27789 | complete |
| SF-2026-ARXIV-2604-27819 | RP-8afdaa90d2626d5b | deep | arXiv:2604.27819v1 | SRC-ARXIV@arXiv:2604.27819v1 | https://arxiv.org/html/2604.27819v1 — §3 MCPHunt canary injection, multi-server topology and taint tracking | https://arxiv.org/html/2604.27819v1 — §4 server/tool compositions, models and leak-detection evaluation | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic canaries and enumerated servers do not prove complete semantic non-interference | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27819 | complete |
| SF-2026-ARXIV-2604-27855 | RP-1b976f9d7f87d144 | deep | arXiv:2604.27855v1 | SRC-ARXIV@arXiv:2604.27855v1 | https://arxiv.org/html/2604.27855v1 — §3-5 latency-constrained energy-geography model and placement formulation | Not Disclosed — exact-v1 has no dedicated empirical Evaluation heading; regional scenarios and sensitivity analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: analytical inputs and assumed relocatability are not measured production traces or universal grid emissions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27855 | complete |
| SF-2026-ARXIV-2604-27906 | RP-33cddce37a5878af | deep | arXiv:2604.27906v1 | SRC-ARXIV@arXiv:2604.27906v1 | https://arxiv.org/html/2604.27906v1 — §3 schema-aware iterative extraction, validation gates and retry path | https://arxiv.org/html/2604.27906v1 — §4 memory extraction/update tasks and component ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected schemas and LLM judges do not prove arbitrary-domain completeness or truth | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27906 | complete |
| SF-2026-ARXIV-2604-28056 | RP-be7fd735cebbdcbf | deep | arXiv:2604.28056v1 | SRC-ARXIV@arXiv:2604.28056v1 | https://arxiv.org/html/2604.28056v1 — §3 RHyVE reward-hypothesis generation, verification and phase-aware deployment | https://arxiv.org/html/2604.28056v1 — §4 RL environments, reward baselines, ablations and competence analysis | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected environments and verifier signals do not prove reward correctness or prevent all specification gaming | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28056 | complete |
| SF-2026-ARXIV-2604-28123 | RP-e678fa2f12b3b706 | deep | arXiv:2604.28123v1 | SRC-ARXIV@arXiv:2604.28123v1 | https://arxiv.org/html/2604.28123v1 — §3 PRISM black-box on-policy distillation between SFT and RLVR | https://arxiv.org/html/2604.28123v1 — §4 multimodal reasoning tasks, baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected models/tasks and teacher access do not establish universal benefit or cost efficiency | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28123 | complete |
| SF-2026-ARXIV-2604-28129 | RP-0453664996e0496b | deep | arXiv:2604.28129v1 | SRC-ARXIV@arXiv:2604.28129v1 | https://arxiv.org/html/2604.28129v1 — §3 activation-trajectory probes and adaptive multi-turn detector | https://arxiv.org/html/2604.28129v1 — §4 attack phases, model families, baselines and transfer tests | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: white-box activations and model-specific probes limit hosted-model use and require recalibration after updates | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28129 | complete |
| SF-2026-ARXIV-2604-28157 | RP-afbc676031469504 | deep | arXiv:2604.28157v1 | SRC-ARXIV@arXiv:2604.28157v1 | https://arxiv.org/html/2604.28157v1 — §3 FlashRT red-team search and cache/memory optimizations | https://arxiv.org/html/2604.28157v1 — §4 prompt-injection/knowledge-corruption workloads, systems measurements and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: attack suites and author hardware do not establish full threat coverage or production prevalence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28157 | complete |
| SF-2026-ARXIV-2604-28158 | RP-c8000f3d285bdbb7 | deep | arXiv:2604.28158v1 | SRC-ARXIV@arXiv:2604.28158v1 | https://arxiv.org/html/2604.28158v1 — §3 method-evolution ontology, extraction and graph construction | https://arxiv.org/html/2604.28158v1 — §4 retrieval/reasoning tasks and graph-quality evaluation | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: automated extraction and selected AI literature do not prove a complete or authoritative knowledge graph | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28158 | complete |
| SF-2026-ARXIV-2604-28175 | RP-484747c0ba06a491 | deep | arXiv:2604.28175v1 | SRC-ARXIV@arXiv:2604.28175v1 | https://arxiv.org/html/2604.28175v1 — §3 Strait dual-priority scheduler and interference predictor | https://arxiv.org/html/2604.28175v1 — §4 serving traces/models, baselines and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: on-premises model roster and hardware do not establish universal predictor transfer or tail-SLO behavior | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28175 | complete |
| SF-2026-ARXIV-2604-28181 | RP-7532f2ca70014445 | deep | arXiv:2604.28181v1 | SRC-ARXIV@arXiv:2604.28181v1 | https://arxiv.org/html/2604.28181v1 — §3 synthetic computer/workspace generation pipeline | https://arxiv.org/html/2604.28181v1 — §4 long-horizon productivity tasks, realism and agent evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: synthetic environments may miss organizational policy, hidden dependencies and real-user distributions | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28181 | complete |
| SF-2026-ARXIV-2604-28182 | RP-575444c9e25d6fdd | deep | arXiv:2604.28182v1 | SRC-ARXIV@arXiv:2604.28182v1 | https://arxiv.org/html/2604.28182v1 — §3 exploration-hacking threat model and resistant-policy construction | https://arxiv.org/html/2604.28182v1 — §4 RL training experiments, detection signals and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: constructed settings do not establish spontaneous prevalence in deployed models or a complete detector | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28182 | complete |
| SF-2026-ARXIV-2604-28190 | RP-6d83eca89d020006 | deep | arXiv:2604.28190v1 | SRC-ARXIV@arXiv:2604.28190v1 | https://arxiv.org/html/2604.28190v1 — §3 Representation Fréchet Loss and population/batch decoupling | https://arxiv.org/html/2604.28190v1 — §4 visual-generation models, quality/diversity evaluations and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected representation encoders and image workloads do not prove perceptual alignment or generalization to all modalities | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28190 | complete |
| SF-2026-ARXIV-2604-28196 | RP-7ce7a2294237466e | deep | arXiv:2604.28196v1 | SRC-ARXIV@arXiv:2604.28196v1 | https://arxiv.org/html/2604.28196v1 — §3 HERMES++ unified 3D understanding/prediction architecture | https://arxiv.org/html/2604.28196v1 — §4 driving datasets, understanding/generation metrics and ablations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: driving datasets and open-loop generation do not prove closed-loop safety or causal controllability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-28196 | complete |
| SF-2026-ARXIV-2604-27891 | RP-d4ef06563c573834 | deep | arXiv:2604.27891v1 | SRC-ARXIV@arXiv:2604.27891v1 | https://arxiv.org/html/2604.27891v1 — §2 directed procedures and controlled LangGraph versus in-context conditions | https://arxiv.org/html/2604.27891v1 — §3 1,200 conversations across three procedural domains with two judge families | https://arxiv.org/html/2604.27891v1 — §5.2-5.3 three simulated customer-service domains, LLM judges and frontier-model capability bound the conclusion; token cost is higher in-context | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27891 | complete |
| SF-2026-ARXIV-2605-00226 | RP-c679621d6ca55676 | deep | arXiv:2605.00226v1 | SRC-ARXIV@arXiv:2605.00226v1 | https://arxiv.org/html/2605.00226v1 — §3 strategic-play tasks, internal/verbal probes and Bayesian Coherence Coefficient | https://arxiv.org/html/2605.00226v1 — §4 repeated games, Kuhn Poker and Chameleon evaluations | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected games/probes do not establish causal access to latent beliefs or general decision competence | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2605-00226 | complete |
| SF-2026-ARXIV-2604-27396 | RP-397720cc3325ad3a | deep | arXiv:2604.27396v1 | SRC-ARXIV@arXiv:2604.27396v1 | https://arxiv.org/html/2604.27396v1 — §II-III heterogeneous dual-core architecture, leading-one predictor and dependency-aware system integration | https://arxiv.org/html/2604.27396v1 — §IV 16nm prototype, BitNet b1.58 3B prefill/decode and ablation evaluation | https://arxiv.org/html/2604.27396v1 — §IV evidence is bound to one 16nm prototype, LPDDR5-class memory, BitNet b1.58 3B and disclosed sequence settings; it does not prove cross-model or cross-accelerator portability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27396 | complete |
| SF-2026-ARXIV-2604-27467 | RP-ceade8b95b003b70 | deep | arXiv:2604.27467v1 | SRC-ARXIV@arXiv:2604.27467v1 | https://arxiv.org/html/2604.27467v1 — §4-5 ScaleBox architecture, automated special-judge generation, distributed sandbox execution and configuration-driven suite | https://arxiv.org/html/2604.27467v1 — §5.2 and §6 verification accuracy/throughput plus RLVR training evaluation | https://arxiv.org/html/2604.27467v1 — §7 Limitations: generated judges, selected code tasks, sandbox policies and author infrastructure do not prove arbitrary-program correctness or universal RL stability | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27467 | complete |
| SF-2026-ARXIV-2604-27486 | RP-b990ec69e8e1da74 | deep | arXiv:2604.27486v1 | SRC-ARXIV@arXiv:2604.27486v1 | https://arxiv.org/html/2604.27486v1 — §3-5 SASS decoding, type-constraint propagation with conflict detection, control-flow reconstruction and multi-instruction aggregation | https://arxiv.org/html/2604.27486v1 — §6 eight suites, 24,437 GPU functions, valid-IR and x86 semantic-pass evaluation plus ablation | https://arxiv.org/html/2604.27486v1 — §6 evaluation cannot validate MUFU, texture or full SIMT behavior through an x86 backend; supported architectures/instructions bound correctness and require fail-closed handling | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27486 | complete |
| SF-2026-ARXIV-2604-27781 | RP-165a6d3bec2f2238 | deep | arXiv:2604.27781v1 | SRC-ARXIV@arXiv:2604.27781v1 | https://arxiv.org/html/2604.27781v1 — §2-5 four-layer AI supply-chain decomposition, integrity gaps and lifecycle requirements | https://arxiv.org/html/2604.27781v1 — §5.1 reference-stack measurement across 48 projects, direct/transitive dependencies and source size | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: exact-v1 provides a conceptual decomposition and ecosystem measurement, not a controlled security evaluation or proof that every dependency is exercised at runtime | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27781 | complete |
| SF-2026-ARXIV-2604-27861 | RP-d8ca151aea3295a0 | deep | arXiv:2604.27861v1 | SRC-ARXIV@arXiv:2604.27861v1 | https://arxiv.org/html/2604.27861v1 — §3-4 asymmetric contrastive dual-encoder state, frozen benign encoder and causal online monitoring | https://arxiv.org/html/2604.27861v1 — §5 strictly causal evaluation over 3.62M instructions and 8,600 malicious intents, including adaptive attacks | Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected generated/curated intents and latent-space clustering do not prove complete intent reconstruction, universal low false-positive operation or action-level safety | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27861 | complete |
| SF-2026-ARXIV-2604-27878 | RP-b694f30145b10fb9 | deep | arXiv:2604.27878v1 | SRC-ARXIV@arXiv:2604.27878v1 | https://arxiv.org/html/2604.27878v1 — §3 canonical session schema, adapters and loss accounting; §4-5 realism and tester-reliability benchmark design | https://arxiv.org/html/2604.27878v1 — §6 four datasets, two languages, four simulator families and ranking-reliability analysis | https://arxiv.org/html/2604.27878v1 — §8 Limitations: dataset/language/simulator coverage is finite; correlations do not prove causal transfer to production users or unseen retrieval systems | Not Disclosed — no event-time artifact revision is used | claim:SF-2026-ARXIV-2604-27878 | complete |

### Source Reviews

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


<!-- review:SF-2026-ARXIV-2605-00066:start -->
<!-- claim:SF-2026-ARXIV-2605-00066:start -->
Open-loop perception/planning metrics 不能自动代理 closed-loop outcome；跨 benchmark 相关性必须先对齐 policy、environment、horizon、intervention 与 failure definition。
<!-- claim:SF-2026-ARXIV-2605-00066:end -->
#### Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 cross-benchmark metric mapping and correlation protocol`。
- **Mechanism / ownership:** Open-loop perception/planning metrics 不能自动代理 closed-loop outcome；跨 benchmark 相关性必须先对齐 policy、environment、horizon、intervention 与 failure definition。
- **Evaluation contract:** `§4 NAVSIM and Bench2Drive cross-benchmark results and sensitivity`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§5 selected benchmarks/models and correlation do not establish causality or real-world safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00066:end -->


<!-- review:SF-2026-ARXIV-2605-00081:start -->
<!-- claim:SF-2026-ARXIV-2605-00081:start -->
Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。
<!-- claim:SF-2026-ARXIV-2605-00081:end -->
#### Alignment Contracts for Agentic Security Systems

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-6 threat assumptions, contract language, dual-layer observability and enforcement`。
- **Mechanism / ownership:** Agent security 不能只判断 intent 或输出文本；可执行 effect 必须在独立 mediation boundary 由 typed contract、authorization 和 audit 拦截，且模型层与执行层各自保留可观测责任。
- **Evaluation contract:** `§7 examples and policy-composition analysis`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§8 impossibility/scope boundary; disclosed framework is not proof of all semantic safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00081:end -->


<!-- review:SF-2026-ARXIV-2605-00136:start -->
<!-- claim:SF-2026-ARXIV-2605-00136:start -->
Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。
<!-- claim:SF-2026-ARXIV-2605-00136:end -->
#### Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 decomposition of tool protocol, selection and execution costs`。
- **Mechanism / ownership:** Tool-use accuracy 必须拆开协议格式成本、selection/argument error、transport/runtime failure 与真实工具收益；更多工具或更长 schema 会征收 context 和 routing tax，不能把失败都归因于模型不会调用。
- **Evaluation contract:** `§5 controlled tool-use diagnosis across models/tasks`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6/discussion task and framework scope; no universal tax constant`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-TOOL-CALLING`；Score V2 `2/3/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00136:end -->


<!-- review:SF-2026-ARXIV-2605-00155:start -->
<!-- claim:SF-2026-ARXIV-2605-00155:start -->
Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.
<!-- claim:SF-2026-ARXIV-2605-00155:end -->
#### Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 Wasserstein ambiguity set and robust regret objective`。
- **Mechanism / ownership:** Preference optimization can treat annotator/reward uncertainty as a distributional ambiguity set and optimize worst-case regret, but robustness radius and reference policy become new control assumptions rather than removing reward misspecification.
- **Evaluation contract:** `§6 experiments and ablations on specified preference datasets/models`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated limitations section; author experiments do not establish universal robustness radius`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Principle Reuse` → `TRAIN-RLHF`；Score V2 `2/2/2` = **6/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00155:end -->


<!-- review:SF-2026-ARXIV-2605-00161:start -->
<!-- claim:SF-2026-ARXIV-2605-00161:start -->
Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.
<!-- claim:SF-2026-ARXIV-2605-00161:end -->
#### Consistent Diffusion Language Models

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-3 consistency objective and diffusion language-model mechanism`。
- **Mechanism / ownership:** Consistent diffusion language modeling narrows train/inference inconsistency by coupling conditional denoising states; it trades token-sequential commitment for iterative correction and does not erase sampling-step, cache or rollback costs.
- **Evaluation contract:** `§4-5 language-model evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; workloads do not prove replacement of autoregressive generation`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MULTIMODAL-GENERATIVE-PARADIGMS`；Score V2 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00161:end -->


<!-- review:SF-2026-ARXIV-2605-00180:start -->
<!-- claim:SF-2026-ARXIV-2605-00180:start -->
Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。
<!-- claim:SF-2026-ARXIV-2605-00180:end -->
#### RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 graph profile construction and cold-start transfer`。
- **Mechanism / ownership:** Model routing 的 cold start 不是缺少一个静态 leaderboard，而是缺少 workload-conditioned profile；图结构从已知模型迁移观测可降低探索成本，但 profile staleness、uncertainty 和 online fallback 必须进入 admission/routing contract。
- **Evaluation contract:** `§4-5 new-model routing experiments, baselines and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 Conclusion — exact-v1 has no dedicated limitations section; tested model/task graph and offline traces bound the conclusion`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00180:end -->


<!-- review:SF-2026-ARXIV-2605-00206:start -->
<!-- claim:SF-2026-ARXIV-2605-00206:start -->
Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.
<!-- claim:SF-2026-ARXIV-2605-00206:end -->
#### State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§2-4 nonlinear recurrence and parallel-training construction`。
- **Mechanism / ownership:** Nonlinear recurrent latent state can be trained with a parallel surrogate and executed recurrently, shifting the bottleneck from explicit token history toward state-transition stability and train/decode equivalence.
- **Evaluation contract:** `§5 model/task evaluations and ablations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations on scale, recurrence stability and broader workloads`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Alternative Branch` → `MODEL-DECODER-ONLY`；Score V2 `2/2/3` = **7/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00206:end -->


<!-- review:SF-2026-ARXIV-2605-00254:start -->
<!-- claim:SF-2026-ARXIV-2605-00254:start -->
MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
<!-- claim:SF-2026-ARXIV-2605-00254:end -->
#### Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 topology/cost model, placement and routing mechanisms`。
- **Mechanism / ownership:** MoE serving topology 必须把 expert placement、token skew、all-to-all bytes、network tiers 与 replica cost 联合建模；更便宜的 topology 会把平均带宽收益换成 hotspot、reconfiguration 和 failure-domain 压力。
- **Evaluation contract:** `§6 serving scenarios and topology comparisons`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; scenario assumptions and cost model are not universal production measurements`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `INFER-SCHEDULING`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00254:end -->


<!-- review:SF-2026-ARXIV-2605-00267:start -->
<!-- claim:SF-2026-ARXIV-2605-00267:start -->
Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。
<!-- claim:SF-2026-ARXIV-2605-00267:end -->
#### Jailbroken Frontier Models Retain Their Capabilities

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-4 jailbreak construction and capability-preservation protocol`。
- **Mechanism / ownership:** Jailbreak 后保留通用能力意味着 safety case 不能依赖能力退化；风险控制必须落在 action authority、sandbox、monitoring 与 outcome evidence，而不是假设越狱模型不可完成复杂任务。
- **Evaluation contract:** `§5 general and agentic task evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 limitations: selected frontier models, attacks and tasks; no deployment prevalence claim`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00267:end -->


<!-- review:SF-2026-ARXIV-2605-00300:start -->
<!-- claim:SF-2026-ARXIV-2605-00300:start -->
Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
<!-- claim:SF-2026-ARXIV-2605-00300:end -->
#### Token Arena: A Continuous Benchmark Unifying Energy and Cognition in AI Inference

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 endpoint-centric continuous benchmark and measurement protocol`。
- **Mechanism / ownership:** Inference benchmark 的原子对象可以是 endpoint/model configuration，而不是模型名称；能耗、质量、延迟与请求策略必须在连续、版本化 contract 中共同记录，且偏好结论不能脱离 evaluator 与 workload。
- **Evaluation contract:** `§4-5 preference/cognition/energy evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§6 discussion and limitations on provider drift, observability and evaluator scope`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Direct Evolution` → `PLATFORM-EVALUATION-SYSTEM`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00300:end -->


<!-- review:SF-2026-ARXIV-2605-00314:start -->
<!-- claim:SF-2026-ARXIV-2605-00314:start -->
Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
<!-- claim:SF-2026-ARXIV-2605-00314:end -->
#### Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3-5 representation synthesis, Datalog constraints and audit pipeline`。
- **Mechanism / ownership:** Agent skill 审计需要把自然语言/代码能力合成为可查询的约束表示，再在调用前检查 source→sink、permission 与 effect；静态分析提高可解释性，却受表示不完备、动态行为与环境依赖限制。
- **Evaluation contract:** `§6 evaluation over skill corpus, attack cases and hardware setup`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `§7 Conclusion — exact-v1 has no dedicated limitations section; static abstraction cannot prove dynamic runtime safety`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Layering / Dependency` → `PLATFORM-SECURITY`；Score V2 `3/3/3` = **9/9**。
- **Books decision:** `Integrate`。
<!-- review:SF-2026-ARXIV-2605-00314:end -->


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


<!-- review:SF-2026-ARXIV-2605-00226:start -->
<!-- claim:SF-2026-ARXIV-2605-00226:start -->
Strategic failure can be decomposed into observation→belief update and belief→action selection gaps; verbalized belief and action accuracy should not be treated as one undifferentiated planning score.
<!-- claim:SF-2026-ARXIV-2605-00226:end -->
#### Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions

- **Why / old boundary:** 旧方案在对象稳定、状态局部或单一离线评测时仍合理；exact-v1 将新增约束定位在 `§3 strategic-play tasks, internal/verbal probes and Bayesian Coherence Coefficient`。
- **Mechanism / ownership:** Strategic failure can be decomposed into observation→belief update and belief→action selection gaps; verbalized belief and action accuracy should not be treated as one undifferentiated planning score.
- **Evaluation contract:** `§4 repeated games, Kuhn Poker and Chameleon evaluations`；作者实验只证明论文绑定的模型、数据、硬件与 evaluator，未披露字段不补造。
- **Trade-off / failure:** `Not Disclosed — exact-v1 has no dedicated Limitations heading; bounded non-proof: selected games/probes do not establish causal access to latent beliefs or general decision competence`。收益必须与新增 metadata、校准、执行或恢复责任在同一 workload 下计量。
- **Evolution / owner:** `Explanatory Analogy` → `AGENT-PLANNING`；Score V2 `3/2/3` = **8/9**。
- **Books decision:** `No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-00226:end -->


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


## 4. Benchmark Contracts

下表不保留 headline speedup；未公开字段显式保持 `Not Disclosed`。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27292 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27309 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27792 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27844 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28138 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28139 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00066 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00081 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00136 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00155 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00161 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00180 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00206 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00254 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00267 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00300 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00314 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27306 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27351 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27358 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27393 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27405 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27419 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27426 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27488 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27536 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27586 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27637 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27660 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27695 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27707 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27711 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27776 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27789 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27819 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27855 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27906 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28056 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28123 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28129 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28157 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28158 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28175 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28181 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28182 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28190 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-28196 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27891 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2605-00226 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27396 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27467 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27486 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27781 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27861 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |
| SF-2026-ARXIV-2604-27878 | exact-v1 author workload | exact-v1 model roster | Not Disclosed unless specified in exact-v1 | Not Disclosed unless specified in exact-v1 | task-defined | task-defined | Not Disclosed unless specified | Not Disclosed unless specified | paper metrics; no production threshold | author protocol; not independent |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27289 |
| SF-2026-ARXIV-2604-27292 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27292 |
| SF-2026-ARXIV-2604-27309 | score_7_9;forced_review | subsumed | — | DA-EVAL-CONTROL | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-EVAL-CONTROL |
| SF-2026-ARXIV-2604-27792 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27792 |
| SF-2026-ARXIV-2604-27844 | score_7_9;forced_review;potential_books_delta | selected | DA-TRAIN-COMM | — | 代表跨层 state/control/evidence 演进主线。 | analysis:DA-TRAIN-COMM |
| SF-2026-ARXIV-2604-28138 | score_7_9;forced_review;potential_books_delta | selected | DA-AGENT-STATE | — | 代表跨层 state/control/evidence 演进主线。 | analysis:DA-AGENT-STATE |
| SF-2026-ARXIV-2604-28139 | score_7_9;forced_review | selected | DA-EVAL-CONTROL | — | 代表跨层 state/control/evidence 演进主线。 | analysis:DA-EVAL-CONTROL |
| SF-2026-ARXIV-2605-00066 | score_7_9;forced_review | subsumed | — | DA-EVAL-CONTROL | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-EVAL-CONTROL |
| SF-2026-ARXIV-2605-00081 | score_7_9;forced_review | subsumed | — | DA-AGENT-STATE | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-AGENT-STATE |
| SF-2026-ARXIV-2605-00136 | score_7_9;forced_review | subsumed | — | DA-AGENT-STATE | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-AGENT-STATE |
| SF-2026-ARXIV-2605-00161 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2605-00161 |
| SF-2026-ARXIV-2605-00180 | score_7_9;forced_review | subsumed | — | DA-TRAIN-COMM | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-TRAIN-COMM |
| SF-2026-ARXIV-2605-00206 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2605-00206 |
| SF-2026-ARXIV-2605-00254 | score_7_9;forced_review;potential_books_delta | subsumed | — | DA-TRAIN-COMM | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-TRAIN-COMM |
| SF-2026-ARXIV-2605-00267 | score_7_9;forced_review | subsumed | — | DA-AGENT-STATE | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-AGENT-STATE |
| SF-2026-ARXIV-2605-00300 | score_7_9;forced_review;potential_books_delta | subsumed | — | DA-EVAL-CONTROL | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-EVAL-CONTROL |
| SF-2026-ARXIV-2605-00314 | score_7_9;forced_review;potential_books_delta | subsumed | — | DA-AGENT-STATE | 独立 Review 完整保留，长叙事只合并同一约束链。 | analysis:DA-AGENT-STATE |
| SF-2026-ARXIV-2604-27306 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27306 |
| SF-2026-ARXIV-2604-27351 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27351 |
| SF-2026-ARXIV-2604-27358 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27358 |
| SF-2026-ARXIV-2604-27393 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27393 |
| SF-2026-ARXIV-2604-27405 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27405 |
| SF-2026-ARXIV-2604-27419 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27419 |
| SF-2026-ARXIV-2604-27426 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27426 |
| SF-2026-ARXIV-2604-27488 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27488 |
| SF-2026-ARXIV-2604-27536 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27536 |
| SF-2026-ARXIV-2604-27586 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27586 |
| SF-2026-ARXIV-2604-27637 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27637 |
| SF-2026-ARXIV-2604-27660 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27660 |
| SF-2026-ARXIV-2604-27695 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27695 |
| SF-2026-ARXIV-2604-27707 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27707 |
| SF-2026-ARXIV-2604-27711 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27711 |
| SF-2026-ARXIV-2604-27776 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27776 |
| SF-2026-ARXIV-2604-27789 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27789 |
| SF-2026-ARXIV-2604-27819 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27819 |
| SF-2026-ARXIV-2604-27855 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27855 |
| SF-2026-ARXIV-2604-27906 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27906 |
| SF-2026-ARXIV-2604-28056 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28056 |
| SF-2026-ARXIV-2604-28123 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28123 |
| SF-2026-ARXIV-2604-28129 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28129 |
| SF-2026-ARXIV-2604-28157 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28157 |
| SF-2026-ARXIV-2604-28158 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28158 |
| SF-2026-ARXIV-2604-28175 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28175 |
| SF-2026-ARXIV-2604-28181 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28181 |
| SF-2026-ARXIV-2604-28182 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28182 |
| SF-2026-ARXIV-2604-28190 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28190 |
| SF-2026-ARXIV-2604-28196 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-28196 |
| SF-2026-ARXIV-2604-27891 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27891 |
| SF-2026-ARXIV-2605-00226 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2605-00226 |
| SF-2026-ARXIV-2604-27396 | score_7_9 | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27396 |
| SF-2026-ARXIV-2604-27467 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27467 |
| SF-2026-ARXIV-2604-27486 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27486 |
| SF-2026-ARXIV-2604-27781 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27781 |
| SF-2026-ARXIV-2604-27861 | score_7_9;forced_review | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27861 |
| SF-2026-ARXIV-2604-27878 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 机制增量已由逐项 Review 承载；三条长叙事优先跨层 owner 变化。 | analysis-decision:SF-2026-ARXIV-2604-27878 |

<!-- analysis:DA-TRAIN-COMM:start -->
### Deep Analysis 1 — 从局部优化到通信、路由与拓扑的联合控制

分布式训练/推理最初可把 collective 和 routing 当固定实现，因为 tensor 分布、模型集合和 topology 稳定。ZipCCL 利用 BF16 exponent 分布做 lossless collective compression；RouteProfile 用已有模型图为新模型迁移 profile；MoE topology 把 expert placement、token skew 与 network tier 合并。三者共同说明：减少 bytes 或探索成本会新增 estimator、profile freshness、switcher 与 hotspot 状态。固定 NCCL、完整 profiling 和均匀 topology 在小规模/稳定 workload 仍是更安全基线。
<!-- analysis:DA-TRAIN-COMM:end -->


<!-- analysis:DA-AGENT-STATE:start -->
### Deep Analysis 2 — Agent 从文本循环演进为 effect、checkpoint 与 policy 的状态机

只保存对话、只审查输出在无副作用工具和短任务中足够。Crab 显示真实恢复还需 OS state 与 turn boundary；Alignment Contracts 把 effect mediation 移到独立执行边界；tool-use tax 拆开 schema/routing/transport 成本；Semia 将 skill source→sink 变成静态约束；jailbreak capability 说明不能假设越狱后能力自然消失。收益是可恢复、可审计和最小权限，代价是 inspector 误判、静态抽象不完备、policy overhead 与更多控制状态。
<!-- analysis:DA-AGENT-STATE:end -->


<!-- analysis:DA-EVAL-CONTROL:start -->
### Deep Analysis 3 — Evaluation 从静态得分演进为版本化 release control

离线分数在对象和环境稳定时合理。EHR deployment 将 rubric、live feedback、SLO 和 cost 接到版本 gate；Claw-Eval-Live 分离 refreshable demand 与 frozen snapshot；open-loop/closed-loop 研究否定未经校准的代理指标；Token Arena 以 endpoint/configuration 为测量对象。共同结论不是增加 benchmark，而是冻结 object、workload、evaluator、terminal evidence 与版本，再让证据拥有或拒绝 release authority。
<!-- analysis:DA-EVAL-CONTROL:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27289:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27289:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27292:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27292:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27792:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27792:end -->


<!-- analysis-decision:SF-2026-ARXIV-2605-00161:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2605-00161:end -->


<!-- analysis-decision:SF-2026-ARXIV-2605-00206:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2605-00206:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27306:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27306:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27351:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27351:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27358:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27358:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27393:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27393:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27405:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27405:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27419:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27419:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27426:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27426:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27488:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27488:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27536:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27536:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27586:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27586:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27637:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27637:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27660:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27660:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27695:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27695:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27707:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27707:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27711:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27711:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27776:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27776:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27789:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27789:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27819:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27819:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27855:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27855:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27906:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27906:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28056:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28056:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28123:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28123:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28129:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28129:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28157:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28157:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28158:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28158:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28175:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28175:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28181:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28181:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28182:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28182:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28190:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28190:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-28196:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-28196:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27891:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27891:end -->


<!-- analysis-decision:SF-2026-ARXIV-2605-00226:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2605-00226:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27396:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27396:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27467:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27467:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27486:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27486:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27781:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27781:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27861:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27861:end -->


<!-- analysis-decision:SF-2026-ARXIV-2604-27878:start -->
该 family 已完成 route-matched exact-v1 Review；不以第四段论文摘要突破三项 Deep Analysis 上限。
<!-- analysis-decision:SF-2026-ARXIV-2604-27878:end -->


## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2604-27289 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2604-27289 | delta:SF-2026-ARXIV-2604-27289 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27289 |
| SF-2026-ARXIV-2604-27292 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2604-27292 | delta:SF-2026-ARXIV-2604-27292 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27292 |
| SF-2026-ARXIV-2604-27309 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L12 | books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-06-ai-infrastructure/73-production-practices.md#L14 | existing:SF-2026-ARXIV-2604-27309 | delta:SF-2026-ARXIV-2604-27309 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27309 |
| SF-2026-ARXIV-2604-27792 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14; books/part-05-inference-system/49-tensorrt-llm.md#L14 | existing:SF-2026-ARXIV-2604-27792 | delta:SF-2026-ARXIV-2604-27792 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27792 |
| SF-2026-ARXIV-2604-27844 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L69 | books/part-04-training-system/37-data-parallel.md#L1; books/part-04-training-system/41-distributed-training-runtime.md#L1 | existing:SF-2026-ARXIV-2604-27844 | delta:SF-2026-ARXIV-2604-27844 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27844 |
| SF-2026-ARXIV-2604-28138 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L50 | books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/73-production-practices.md#L1 | existing:SF-2026-ARXIV-2604-28138 | delta:SF-2026-ARXIV-2604-28138 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28138 |
| SF-2026-ARXIV-2604-28139 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L18 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L69 | existing:SF-2026-ARXIV-2604-28139 | delta:SF-2026-ARXIV-2604-28139 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28139 |
| SF-2026-ARXIV-2605-00066 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L35 | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L27; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2605-00066 | delta:SF-2026-ARXIV-2605-00066 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00066 |
| SF-2026-ARXIV-2605-00081 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2605-00081 | delta:SF-2026-ARXIV-2605-00081 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00081 |
| SF-2026-ARXIV-2605-00136 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L42 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L50 | existing:SF-2026-ARXIV-2605-00136 | delta:SF-2026-ARXIV-2605-00136 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00136 |
| SF-2026-ARXIV-2605-00155 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L168 | books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/34-dpo.md#L1 | existing:SF-2026-ARXIV-2605-00155 | delta:SF-2026-ARXIV-2605-00155 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00155 |
| SF-2026-ARXIV-2605-00161 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | books/part-02-model/18-decoder-only.md#L1; books/part-05-inference-system/48-speculative-decoding.md#L1 | existing:SF-2026-ARXIV-2605-00161 | delta:SF-2026-ARXIV-2605-00161 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00161 |
| SF-2026-ARXIV-2605-00180 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L35 | books/part-05-inference-system/52-distributed-inference.md#L1; books/part-06-ai-infrastructure/63-resource-scheduling.md#L1 | existing:SF-2026-ARXIV-2605-00180 | delta:SF-2026-ARXIV-2605-00180 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00180 |
| SF-2026-ARXIV-2605-00206 | MODEL-DECODER-ONLY | books/part-02-model/18-decoder-only.md#L1 | books/part-02-model/15-attention.md#L1; books/part-04-training-system/36-distributed-training.md#L1 | existing:SF-2026-ARXIV-2605-00206 | delta:SF-2026-ARXIV-2605-00206 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00206 |
| SF-2026-ARXIV-2605-00254 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L35 | books/part-05-inference-system/52-distributed-inference.md#L1; books/part-05-inference-system/55-inference-memory-optimization.md#L1 | existing:SF-2026-ARXIV-2605-00254 | delta:SF-2026-ARXIV-2605-00254 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-00254 |
| SF-2026-ARXIV-2605-00267 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-06-ai-infrastructure/66-evaluation-system.md#L18; books/part-07-agent/84-agent-platform.md#L74 | existing:SF-2026-ARXIV-2605-00267 | delta:SF-2026-ARXIV-2605-00267 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00267 |
| SF-2026-ARXIV-2605-00300 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L35 | books/part-05-inference-system/56-inference-scheduling.md#L55; books/part-06-ai-infrastructure/69-cost-management.md#L1 | existing:SF-2026-ARXIV-2605-00300 | delta:SF-2026-ARXIV-2605-00300 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-00300 |
| SF-2026-ARXIV-2605-00314 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14 | books/part-07-agent/78-tool-calling.md#L42; books/part-07-agent/83-mcp.md#L40 | existing:SF-2026-ARXIV-2605-00314 | delta:SF-2026-ARXIV-2605-00314 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2605-00314 |
| SF-2026-ARXIV-2604-27306 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2604-27306 | delta:SF-2026-ARXIV-2604-27306 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27306 |
| SF-2026-ARXIV-2604-27351 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2604-27351 | delta:SF-2026-ARXIV-2604-27351 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27351 |
| SF-2026-ARXIV-2604-27358 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/79-planning.md#L1; books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2604-27358 | delta:SF-2026-ARXIV-2604-27358 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27358 |
| SF-2026-ARXIV-2604-27393 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-05-inference-system/43-prefill.md#L1 | existing:SF-2026-ARXIV-2604-27393 | delta:SF-2026-ARXIV-2604-27393 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27393 |
| SF-2026-ARXIV-2604-27405 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27405 | delta:SF-2026-ARXIV-2604-27405 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27405 |
| SF-2026-ARXIV-2604-27419 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/78-tool-calling.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27419 | delta:SF-2026-ARXIV-2604-27419 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27419 |
| SF-2026-ARXIV-2604-27426 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-04-training-system/29-sft.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27426 | delta:SF-2026-ARXIV-2604-27426 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-27426 |
| SF-2026-ARXIV-2604-27488 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/80-reflection.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27488 | delta:SF-2026-ARXIV-2604-27488 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27488 |
| SF-2026-ARXIV-2604-27536 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/70-cost.md#L1 | existing:SF-2026-ARXIV-2604-27536 | delta:SF-2026-ARXIV-2604-27536 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27536 |
| SF-2026-ARXIV-2604-27586 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-27586 | delta:SF-2026-ARXIV-2604-27586 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27586 |
| SF-2026-ARXIV-2604-27637 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/74-prompt.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27637 | delta:SF-2026-ARXIV-2604-27637 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27637 |
| SF-2026-ARXIV-2604-27660 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L1 | books/part-07-agent/77-memory.md#L1; books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2604-27660 | delta:SF-2026-ARXIV-2604-27660 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27660 |
| SF-2026-ARXIV-2604-27695 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2604-27695 | delta:SF-2026-ARXIV-2604-27695 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27695 |
| SF-2026-ARXIV-2604-27707 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2604-27707 | delta:SF-2026-ARXIV-2604-27707 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27707 |
| SF-2026-ARXIV-2604-27711 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2604-27711 | delta:SF-2026-ARXIV-2604-27711 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27711 |
| SF-2026-ARXIV-2604-27776 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27776 | delta:SF-2026-ARXIV-2604-27776 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27776 |
| SF-2026-ARXIV-2604-27789 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2604-27789 | delta:SF-2026-ARXIV-2604-27789 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27789 |
| SF-2026-ARXIV-2604-27819 | AGENT-MCP | books/part-07-agent/83-mcp.md#L1 | books/part-06-ai-infrastructure/72-security.md#L1; books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2604-27819 | delta:SF-2026-ARXIV-2604-27819 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27819 |
| SF-2026-ARXIV-2604-27855 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-05-inference-system/56-inference-scheduling.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2604-27855 | delta:SF-2026-ARXIV-2604-27855 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-27855 |
| SF-2026-ARXIV-2604-27906 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27906 | delta:SF-2026-ARXIV-2604-27906 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27906 |
| SF-2026-ARXIV-2604-28056 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-28056 | delta:SF-2026-ARXIV-2604-28056 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28056 |
| SF-2026-ARXIV-2604-28123 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/29-sft.md#L1; books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2604-28123 | delta:SF-2026-ARXIV-2604-28123 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28123 |
| SF-2026-ARXIV-2604-28129 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/69-trace.md#L1; books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2604-28129 | delta:SF-2026-ARXIV-2604-28129 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2604-28129 |
| SF-2026-ARXIV-2604-28157 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/75-context.md#L1 | existing:SF-2026-ARXIV-2604-28157 | delta:SF-2026-ARXIV-2604-28157 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28157 |
| SF-2026-ARXIV-2604-28158 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-28158 | delta:SF-2026-ARXIV-2604-28158 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28158 |
| SF-2026-ARXIV-2604-28175 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1; books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2604-28175 | delta:SF-2026-ARXIV-2604-28175 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28175 |
| SF-2026-ARXIV-2604-28181 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-28181 | delta:SF-2026-ARXIV-2604-28181 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28181 |
| SF-2026-ARXIV-2604-28182 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2604-28182 | delta:SF-2026-ARXIV-2604-28182 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-28182 |
| SF-2026-ARXIV-2604-28190 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-28190 | delta:SF-2026-ARXIV-2604-28190 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-28190 |
| SF-2026-ARXIV-2604-28196 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/23-multimodal-representation.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2026-ARXIV-2604-28196 | delta:SF-2026-ARXIV-2604-28196 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-28196 |
| SF-2026-ARXIV-2604-27891 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/75-context.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2604-27891 | delta:SF-2026-ARXIV-2604-27891 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2604-27891 |
| SF-2026-ARXIV-2605-00226 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2605-00226 | delta:SF-2026-ARXIV-2605-00226 | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-00226 |
| SF-2026-ARXIV-2604-27396 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L122 | books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2604-27396 | delta:SF-2026-ARXIV-2604-27396 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27396 |
| SF-2026-ARXIV-2604-27467 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-04-training-system/31-rlhf.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2604-27467 | delta:SF-2026-ARXIV-2604-27467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27467 |
| SF-2026-ARXIV-2604-27486 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L220 | books/part-06-ai-infrastructure/72-security.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2604-27486 | delta:SF-2026-ARXIV-2604-27486 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27486 |
| SF-2026-ARXIV-2604-27781 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1; books/part-06-ai-infrastructure/60-model-registry.md#L1 | existing:SF-2026-ARXIV-2604-27781 | delta:SF-2026-ARXIV-2604-27781 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27781 |
| SF-2026-ARXIV-2604-27861 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-07-agent/75-context.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2604-27861 | delta:SF-2026-ARXIV-2604-27861 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2604-27861 |
| SF-2026-ARXIV-2604-27878 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2604-27878 | delta:SF-2026-ARXIV-2604-27878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2604-27878 |

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


<!-- books-review:SF-2026-ARXIV-2604-27309:start -->
<!-- existing:SF-2026-ARXIV-2604-27309:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L12` 与 `books/part-06-ai-infrastructure/67-monitoring.md#L14; books/part-06-ai-infrastructure/73-production-practices.md#L14`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27309:end -->
<!-- delta:SF-2026-ARXIV-2604-27309:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27309:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27309:end -->


<!-- books-review:SF-2026-ARXIV-2604-27792:start -->
<!-- existing:SF-2026-ARXIV-2604-27792:start -->
已核对 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14` 与 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14; books/part-05-inference-system/49-tensorrt-llm.md#L14`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27792:end -->
<!-- delta:SF-2026-ARXIV-2604-27792:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27792:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27792:end -->


<!-- books-review:SF-2026-ARXIV-2604-27844:start -->
<!-- existing:SF-2026-ARXIV-2604-27844:start -->
Ch36 已拥有 collective 语义、算法/transport/topology 分层和 bandwidth/latency/overlap 成本模型。
<!-- existing:SF-2026-ARXIV-2604-27844:end -->
<!-- delta:SF-2026-ARXIV-2604-27844:start -->
尚未把 bit-exact exponent coding、GPU encode/decode critical path 与 adaptive fallback 写成同一条 compression contract。
<!-- delta:SF-2026-ARXIV-2604-27844:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27844:end -->


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


<!-- books-review:SF-2026-ARXIV-2605-00066:start -->
<!-- existing:SF-2026-ARXIV-2605-00066:start -->
已核对 `books/part-06-ai-infrastructure/66-evaluation-system.md#L35` 与 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L27; books/part-06-ai-infrastructure/67-monitoring.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00066:end -->
<!-- delta:SF-2026-ARXIV-2605-00066:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00066:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00066:end -->


<!-- books-review:SF-2026-ARXIV-2605-00081:start -->
<!-- existing:SF-2026-ARXIV-2605-00081:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-07-agent/78-tool-calling.md#L14; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00081:end -->
<!-- delta:SF-2026-ARXIV-2605-00081:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00081:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00081:end -->


<!-- books-review:SF-2026-ARXIV-2605-00136:start -->
<!-- existing:SF-2026-ARXIV-2605-00136:start -->
已核对 `books/part-07-agent/78-tool-calling.md#L42` 与 `books/part-07-agent/81-workflow.md#L1; books/part-07-agent/84-agent-platform.md#L50`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00136:end -->
<!-- delta:SF-2026-ARXIV-2605-00136:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00136:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00136:end -->


<!-- books-review:SF-2026-ARXIV-2605-00155:start -->
<!-- existing:SF-2026-ARXIV-2605-00155:start -->
已核对 `books/part-04-training-system/31-rlhf.md#L168` 与 `books/part-04-training-system/32-ppo.md#L1; books/part-04-training-system/34-dpo.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00155:end -->
<!-- delta:SF-2026-ARXIV-2605-00155:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00155:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00155:end -->


<!-- books-review:SF-2026-ARXIV-2605-00161:start -->
<!-- existing:SF-2026-ARXIV-2605-00161:start -->
已核对 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1` 与 `books/part-02-model/18-decoder-only.md#L1; books/part-05-inference-system/48-speculative-decoding.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00161:end -->
<!-- delta:SF-2026-ARXIV-2605-00161:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00161:end -->
演进关系 `Alternative Branch`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00161:end -->


<!-- books-review:SF-2026-ARXIV-2605-00180:start -->
<!-- existing:SF-2026-ARXIV-2605-00180:start -->
已核对 `books/part-05-inference-system/56-inference-scheduling.md#L35` 与 `books/part-05-inference-system/52-distributed-inference.md#L1; books/part-06-ai-infrastructure/63-resource-scheduling.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00180:end -->
<!-- delta:SF-2026-ARXIV-2605-00180:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00180:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00180:end -->


<!-- books-review:SF-2026-ARXIV-2605-00206:start -->
<!-- existing:SF-2026-ARXIV-2605-00206:start -->
已核对 `books/part-02-model/18-decoder-only.md#L1` 与 `books/part-02-model/15-attention.md#L1; books/part-04-training-system/36-distributed-training.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00206:end -->
<!-- delta:SF-2026-ARXIV-2605-00206:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00206:end -->
演进关系 `Alternative Branch`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00206:end -->


<!-- books-review:SF-2026-ARXIV-2605-00254:start -->
<!-- existing:SF-2026-ARXIV-2605-00254:start -->
Ch52/Ch56 已拥有 distributed inference 的 placement、network tier、hotspot 与 scheduling state。
<!-- existing:SF-2026-ARXIV-2605-00254:end -->
<!-- delta:SF-2026-ARXIV-2605-00254:start -->
尚未把 MoE expert placement、token skew、all-to-all bytes、topology cost 与 reconfiguration/failure domain 联合为一个 serving decision。
<!-- delta:SF-2026-ARXIV-2605-00254:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00254:end -->


<!-- books-review:SF-2026-ARXIV-2605-00267:start -->
<!-- existing:SF-2026-ARXIV-2605-00267:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L14` 与 `books/part-06-ai-infrastructure/66-evaluation-system.md#L18; books/part-07-agent/84-agent-platform.md#L74`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00267:end -->
<!-- delta:SF-2026-ARXIV-2605-00267:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00267:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00267:end -->


<!-- books-review:SF-2026-ARXIV-2605-00300:start -->
<!-- existing:SF-2026-ARXIV-2605-00300:start -->
Ch66 已要求 benchmark 冻结 workload、evaluator、版本与 evidence；Ch69 拥有成本维度。
<!-- existing:SF-2026-ARXIV-2605-00300:end -->
<!-- delta:SF-2026-ARXIV-2605-00300:start -->
尚未把 endpoint/model configuration 定义为版本化原子对象，并在同一连续 contract 记录能耗、质量、延迟、价格与可靠性。
<!-- delta:SF-2026-ARXIV-2605-00300:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00300:end -->


<!-- books-review:SF-2026-ARXIV-2605-00314:start -->
<!-- existing:SF-2026-ARXIV-2605-00314:start -->
Ch72 已拥有 tool/skill 的 artifact、capability、data-flow 与 runtime-effect 审计边界。
<!-- existing:SF-2026-ARXIV-2605-00314:end -->
<!-- delta:SF-2026-ARXIV-2605-00314:start -->
尚未说明如何由自然语言和代码合成有限 SDL fact base，再由 Datalog 约束检查 source-to-sink、permission 与 effect。
<!-- delta:SF-2026-ARXIV-2605-00314:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-00314:end -->


<!-- books-review:SF-2026-ARXIV-2604-27306:start -->
<!-- existing:SF-2026-ARXIV-2604-27306:start -->
Ch76 已要求 provenance、temporal validity 与 source authority 随 retrieval evidence 传播。
<!-- existing:SF-2026-ARXIV-2604-27306:end -->
<!-- delta:SF-2026-ARXIV-2604-27306:start -->
尚未把 atomic nugget 的 validity/lifecycle 写成 ranking 前 admission 与失效淘汰状态机。
<!-- delta:SF-2026-ARXIV-2604-27306:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27306:end -->


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


<!-- books-review:SF-2026-ARXIV-2604-27789:start -->
<!-- existing:SF-2026-ARXIV-2604-27789:start -->
已核对 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 与 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/72-security.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27789:end -->
<!-- delta:SF-2026-ARXIV-2604-27789:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27789:end -->
演进关系 `Direct Evolution`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27789:end -->


<!-- books-review:SF-2026-ARXIV-2604-27819:start -->
<!-- existing:SF-2026-ARXIV-2604-27819:start -->
Ch83/Ch72 已拥有 MCP server identity、capability 与执行边界。
<!-- existing:SF-2026-ARXIV-2604-27819:end -->
<!-- delta:SF-2026-ARXIV-2604-27819:start -->
尚未说明 benign read/write permission 如何经多 server workflow 合成为跨域泄漏，以及 canary taint 如何跨 tool edge 传播。
<!-- delta:SF-2026-ARXIV-2604-27819:end -->
演进关系 `Direct Evolution`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27819:end -->


<!-- books-review:SF-2026-ARXIV-2604-27855:start -->
<!-- existing:SF-2026-ARXIV-2604-27855:start -->
Ch70/Ch56 已联合考虑 cost、SLO、capacity 与 placement。
<!-- existing:SF-2026-ARXIV-2604-27855:end -->
<!-- delta:SF-2026-ARXIV-2604-27855:start -->
尚未把 energy geography 作为仅在 latency、state locality、capacity 与 regulation 硬约束后才可优化的调度维度。
<!-- delta:SF-2026-ARXIV-2604-27855:end -->
演进关系 `Layering / Dependency`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27855:end -->


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


<!-- books-review:SF-2026-ARXIV-2604-27891:start -->
<!-- existing:SF-2026-ARXIV-2604-27891:start -->
Ch81 已说明 durable workflow state、side effect、restart 与 audit 需要外部 owner。
<!-- existing:SF-2026-ARXIV-2604-27891:end -->
<!-- delta:SF-2026-ARXIV-2604-27891:start -->
尚未明确外部 graph orchestration 不是默认：procedure 可完整入 context 时，self-routing 可避免 fragment/routing calls，但不能替代 durable commit。
<!-- delta:SF-2026-ARXIV-2604-27891:end -->
演进关系 `Alternative Branch`；决定 `Integrate`。
<!-- books-review:SF-2026-ARXIV-2604-27891:end -->


<!-- books-review:SF-2026-ARXIV-2605-00226:start -->
<!-- existing:SF-2026-ARXIV-2605-00226:start -->
已核对 `books/part-07-agent/79-planning.md#L1` 与 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2605-00226:end -->
<!-- delta:SF-2026-ARXIV-2605-00226:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2605-00226:end -->
演进关系 `Explanatory Analogy`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-00226:end -->


<!-- books-review:SF-2026-ARXIV-2604-27396:start -->
<!-- existing:SF-2026-ARXIV-2604-27396:start -->
已核对 `books/part-05-inference-system/49-tensorrt-llm.md#L122` 与 `books/part-05-inference-system/43-prefill.md#L1; books/part-05-inference-system/44-decode.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27396:end -->
<!-- delta:SF-2026-ARXIV-2604-27396:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27396:end -->
演进关系 `Principle Reuse`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27396:end -->


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


<!-- books-review:SF-2026-ARXIV-2604-27781:start -->
<!-- existing:SF-2026-ARXIV-2604-27781:start -->
已核对 `books/part-06-ai-infrastructure/72-security.md#L1` 与 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1; books/part-06-ai-infrastructure/60-model-registry.md#L1`；现有正文已拥有该 state/control/evidence boundary。
<!-- existing:SF-2026-ARXIV-2604-27781:end -->
<!-- delta:SF-2026-ARXIV-2604-27781:start -->
本 family 只收紧机制证据或适用边界，不产生新的长期命题；保留为受限 evidence case。
<!-- delta:SF-2026-ARXIV-2604-27781:end -->
演进关系 `Layering / Dependency`；决定 `No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2604-27781:end -->


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


## 7. Semantic Audit

独立 auditor 未参与本日 author packet，已对 532 行 screening、56 份 exact-v1、Deep Selection 与 current Books owner/adjacent content 完成 fresh-context 复核。审计明细见 `papers/2026/05/_sources/daily-20260501/independent-semantic-audit.json`。

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260501-COVERAGE | fresh-context:may2026_day02 | coverage | coverage:SRC-ARXIV:20260501 | none | Independent audit materialized six false-negative recoveries, reconciled one VitaLLM duplicate, and froze 56 retained plus 476 closures. | passed |
| SA-20260501-EVIDENCE | fresh-context:may2026_day02 | evidence | review:SF-2026-ARXIV-2604-27289; review:SF-2026-ARXIV-2604-27292; review:SF-2026-ARXIV-2604-27309; review:SF-2026-ARXIV-2604-27792; review:SF-2026-ARXIV-2604-27844; review:SF-2026-ARXIV-2604-28138; review:SF-2026-ARXIV-2604-28139; review:SF-2026-ARXIV-2605-00066; review:SF-2026-ARXIV-2605-00081; review:SF-2026-ARXIV-2605-00136; review:SF-2026-ARXIV-2605-00155; review:SF-2026-ARXIV-2605-00161; review:SF-2026-ARXIV-2605-00180; review:SF-2026-ARXIV-2605-00206; review:SF-2026-ARXIV-2605-00254; review:SF-2026-ARXIV-2605-00267; review:SF-2026-ARXIV-2605-00300; review:SF-2026-ARXIV-2605-00314; review:SF-2026-ARXIV-2604-27306; review:SF-2026-ARXIV-2604-27351; review:SF-2026-ARXIV-2604-27358; review:SF-2026-ARXIV-2604-27393; review:SF-2026-ARXIV-2604-27405; review:SF-2026-ARXIV-2604-27419; review:SF-2026-ARXIV-2604-27426; review:SF-2026-ARXIV-2604-27488; review:SF-2026-ARXIV-2604-27536; review:SF-2026-ARXIV-2604-27586; review:SF-2026-ARXIV-2604-27637; review:SF-2026-ARXIV-2604-27660; review:SF-2026-ARXIV-2604-27695; review:SF-2026-ARXIV-2604-27707; review:SF-2026-ARXIV-2604-27711; review:SF-2026-ARXIV-2604-27776; review:SF-2026-ARXIV-2604-27789; review:SF-2026-ARXIV-2604-27819; review:SF-2026-ARXIV-2604-27855; review:SF-2026-ARXIV-2604-27906; review:SF-2026-ARXIV-2604-28056; review:SF-2026-ARXIV-2604-28123; review:SF-2026-ARXIV-2604-28129; review:SF-2026-ARXIV-2604-28157; review:SF-2026-ARXIV-2604-28158; review:SF-2026-ARXIV-2604-28175; review:SF-2026-ARXIV-2604-28181; review:SF-2026-ARXIV-2604-28182; review:SF-2026-ARXIV-2604-28190; review:SF-2026-ARXIV-2604-28196; review:SF-2026-ARXIV-2604-27891; review:SF-2026-ARXIV-2605-00226; review:SF-2026-ARXIV-2604-27396; review:SF-2026-ARXIV-2604-27467; review:SF-2026-ARXIV-2604-27486; review:SF-2026-ARXIV-2604-27781; review:SF-2026-ARXIV-2604-27861; review:SF-2026-ARXIV-2604-27878 | none | 56 exact-v1 claim/locator/non-proof records checked; blocked=0. | passed |
| SA-20260501-SELECTION | fresh-context:may2026_day02 | deep_analysis_selection | analysis:DA-TRAIN-COMM; analysis:DA-AGENT-STATE; analysis:DA-EVAL-CONTROL | none | All eligible families have an explicit selection disposition; the three narratives remain distinct communication, agent-state and evaluation-control chains. | passed |
| SA-20260501-BOOKS | fresh-context:may2026_day02 | books | books-review:SF-2026-ARXIV-2604-27289; books-review:SF-2026-ARXIV-2604-27292; books-review:SF-2026-ARXIV-2604-27309; books-review:SF-2026-ARXIV-2604-27792; books-review:SF-2026-ARXIV-2604-27844; books-review:SF-2026-ARXIV-2604-28138; books-review:SF-2026-ARXIV-2604-28139; books-review:SF-2026-ARXIV-2605-00066; books-review:SF-2026-ARXIV-2605-00081; books-review:SF-2026-ARXIV-2605-00136; books-review:SF-2026-ARXIV-2605-00155; books-review:SF-2026-ARXIV-2605-00161; books-review:SF-2026-ARXIV-2605-00180; books-review:SF-2026-ARXIV-2605-00206; books-review:SF-2026-ARXIV-2605-00254; books-review:SF-2026-ARXIV-2605-00267; books-review:SF-2026-ARXIV-2605-00300; books-review:SF-2026-ARXIV-2605-00314; books-review:SF-2026-ARXIV-2604-27306; books-review:SF-2026-ARXIV-2604-27351; books-review:SF-2026-ARXIV-2604-27358; books-review:SF-2026-ARXIV-2604-27393; books-review:SF-2026-ARXIV-2604-27405; books-review:SF-2026-ARXIV-2604-27419; books-review:SF-2026-ARXIV-2604-27426; books-review:SF-2026-ARXIV-2604-27488; books-review:SF-2026-ARXIV-2604-27536; books-review:SF-2026-ARXIV-2604-27586; books-review:SF-2026-ARXIV-2604-27637; books-review:SF-2026-ARXIV-2604-27660; books-review:SF-2026-ARXIV-2604-27695; books-review:SF-2026-ARXIV-2604-27707; books-review:SF-2026-ARXIV-2604-27711; books-review:SF-2026-ARXIV-2604-27776; books-review:SF-2026-ARXIV-2604-27789; books-review:SF-2026-ARXIV-2604-27819; books-review:SF-2026-ARXIV-2604-27855; books-review:SF-2026-ARXIV-2604-27906; books-review:SF-2026-ARXIV-2604-28056; books-review:SF-2026-ARXIV-2604-28123; books-review:SF-2026-ARXIV-2604-28129; books-review:SF-2026-ARXIV-2604-28157; books-review:SF-2026-ARXIV-2604-28158; books-review:SF-2026-ARXIV-2604-28175; books-review:SF-2026-ARXIV-2604-28181; books-review:SF-2026-ARXIV-2604-28182; books-review:SF-2026-ARXIV-2604-28190; books-review:SF-2026-ARXIV-2604-28196; books-review:SF-2026-ARXIV-2604-27891; books-review:SF-2026-ARXIV-2605-00226; books-review:SF-2026-ARXIV-2604-27396; books-review:SF-2026-ARXIV-2604-27467; books-review:SF-2026-ARXIV-2604-27486; books-review:SF-2026-ARXIV-2604-27781; books-review:SF-2026-ARXIV-2604-27861; books-review:SF-2026-ARXIV-2604-27878 | none | Root serialized 24 writes; independent post-write audit found all 24 durable deltas in owner prose with old path, changed constraint, ownership, trade-off/failure, fallback/coexistence and evidence boundary, without adjacent-owner duplication. Receipt: post-write-semantic-audit.json. | passed |

## 8. Ignored Noise

476 个 pre-denominator closure 位于 `papers/2026/05/_sources/daily-20260501/screening-ledger.json/tsv`。每项保留 identity、v1 时间、分类、title、abstract、具体 closure reason 和 author false-negative audit，不进入 Score V2，也不冒充全文 Review。

## 9. Recommended Action

1. 继续在后续 Daily/Weekly 中验证这些机制的外部有效性；单篇 exact-v1 的作者实验不升级为通用系统定律。
2. 当模型、硬件、provider endpoint、workload 或 evaluator identity 变化时，重新核验本日列出的 evidence boundary 与 fallback 条件。

## 10. Repository Changes

- 新建本日 inventory、532-row screening ledger、review packet、Books writeback queue、pre-write 与 post-write semantic audit 及 Daily README。
- root 已把 24 个长期增量串行写入 14 个 owner 章节；非写作者完成 owner/adjacent post-write 语义验收。未修改 ROADMAP、LEARNING_STATE；未 stage、commit 或 push。

## 11. Open Questions

- lossless collective compression 的分布假设如何在训练 phase、dtype 与 model family 漂移时在线验证并安全回退？
- Agent checkpoint 的最小 recovery state 如何与 tool idempotency、external side effects 和 workflow commit 统一？
- endpoint-centric benchmark 如何冻结 provider drift、价格、energy telemetry 与 evaluator version？
- effect-level policy 怎样在未知 tool semantics 下 abstain，而不是把静态 audit 误当 runtime proof？

## 12. Sources

- [Mechanized Foundations of Structural Governance: Machine-Checked Proofs for Governed Intelligence](https://arxiv.org/html/2604.27289v1) — arXiv:2604.27289v1；Submitted `2026-04-30T01:03:15Z`；访问 2026-08-31。
- [The Two Boundaries: Why Behavioral AI Governance Fails Structurally](https://arxiv.org/html/2604.27292v1) — arXiv:2604.27292v1；Submitted `2026-04-30T01:12:32Z`；访问 2026-08-31。
- [End-to-End Evaluation and Governance of an EHR-Embedded AI Agent for Clinicians](https://arxiv.org/html/2604.27309v1) — arXiv:2604.27309v1；Submitted `2026-04-30T01:45:39Z`；访问 2026-08-31。
- [Motubrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v1) — arXiv:2604.27792v1；Submitted `2026-04-30T12:34:44Z`；访问 2026-08-31。
- [ZipCCL: Efficient Lossless Data Compression of Communication Collectives for Accelerating LLM Training](https://arxiv.org/html/2604.27844v1) — arXiv:2604.27844v1；Submitted `2026-04-30T13:29:59Z`；访问 2026-08-31。
- [Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes](https://arxiv.org/html/2604.28138v1) — arXiv:2604.28138v1；Submitted `2026-04-30T17:20:19Z`；访问 2026-08-31。
- [Claw-Eval-Live: A Live Agent Benchmark for Evolving Real-World Workflows](https://arxiv.org/html/2604.28139v1) — arXiv:2604.28139v1；Submitted `2026-04-30T17:23:19Z`；访问 2026-08-31。
- [Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive](https://arxiv.org/html/2605.00066v1) — arXiv:2605.00066v1；Submitted `2026-04-30T09:27:57Z`；访问 2026-08-31。
- [Alignment Contracts for Agentic Security Systems](https://arxiv.org/html/2605.00081v1) — arXiv:2605.00081v1；Submitted `2026-04-30T14:38:05Z`；访问 2026-08-31。
- [Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents](https://arxiv.org/html/2605.00136v1) — arXiv:2605.00136v1；Submitted `2026-04-30T18:46:01Z`；访问 2026-08-31。
- [Wasserstein Distributionally Robust Regret Optimization for Reinforcement Learning from Human Feedback](https://arxiv.org/html/2605.00155v1) — arXiv:2605.00155v1；Submitted `2026-04-30T19:22:56Z`；访问 2026-08-31。
- [Consistent Diffusion Language Models](https://arxiv.org/html/2605.00161v1) — arXiv:2605.00161v1；Submitted `2026-04-30T19:31:02Z`；访问 2026-08-31。
- [RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing](https://arxiv.org/html/2605.00180v1) — arXiv:2605.00180v1；Submitted `2026-04-30T19:56:08Z`；访问 2026-08-31。
- [State Stream Transformer (SST) V2: Parallel Training of Nonlinear Recurrence for Latent Space Reasoning](https://arxiv.org/html/2605.00206v1) — arXiv:2605.00206v1；Submitted `2026-04-30T20:30:28Z`；访问 2026-08-31。
- [Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving](https://arxiv.org/html/2605.00254v1) — arXiv:2605.00254v1；Submitted `2026-04-30T21:35:22Z`；访问 2026-08-31。
- [Jailbroken Frontier Models Retain Their Capabilities](https://arxiv.org/html/2605.00267v1) — arXiv:2605.00267v1；Submitted `2026-04-30T22:04:10Z`；访问 2026-08-31。
- [Token Arena: A Continuous Benchmark Unifying Energy and Cognition in AI Inference](https://arxiv.org/html/2605.00300v1) — arXiv:2605.00300v1；Submitted `2026-05-01T00:05:54Z`；访问 2026-08-31。
- [Semia: Auditing Agent Skills via Constraint-Guided Representation Synthesis](https://arxiv.org/html/2605.00314v1) — arXiv:2605.00314v1；Submitted `2026-05-01T00:48:47Z`；访问 2026-08-31。
- [NuggetIndex: Governed Atomic Retrieval for Maintainable RAG](https://arxiv.org/html/2604.27306v1) — arXiv:2604.27306v1；Submitted `2026-04-30T01:33:56Z`；访问 2026-08-31。
- [Heterogeneous Scientific Foundation Model Collaboration](https://arxiv.org/html/2604.27351v1) — arXiv:2604.27351v1；Submitted `2026-04-30T03:02:27Z`；访问 2026-08-31。
- [Safe Bilevel Delegation (SBD): A Formal Framework for Runtime Delegation Safety in Multi-Agent Systems](https://arxiv.org/html/2604.27358v1) — arXiv:2604.27358v1；Submitted `2026-04-30T03:15:05Z`；访问 2026-08-31。
- [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](https://arxiv.org/html/2604.27393v1) — arXiv:2604.27393v1；Submitted `2026-04-30T04:05:43Z`；访问 2026-08-31。
- [Beyond the Mean: Within-Model Reliable Change Detection for LLM Evaluation](https://arxiv.org/html/2604.27405v1) — arXiv:2604.27405v1；Submitted `2026-04-30T04:16:13Z`；访问 2026-08-31。
- [InteractWeb-Bench: Can Multimodal Agent Escape Blind Execution in Interactive Website Generation?](https://arxiv.org/html/2604.27419v1) — arXiv:2604.27419v1；Submitted `2026-04-30T04:49:34Z`；访问 2026-08-31。
- [Secret Stealing Attacks on Local LLM Fine-Tuning through Supply-Chain Model Code Backdoors](https://arxiv.org/html/2604.27426v1) — arXiv:2604.27426v1；Submitted `2026-04-30T05:03:08Z`；访问 2026-08-31。
- [Skills-Coach: A Self-Evolving Skill Optimizer via Training-Free GRPO](https://arxiv.org/html/2604.27488v1) — arXiv:2604.27488v1；Submitted `2026-04-30T06:39:37Z`；访问 2026-08-31。
- [Belief-Guided Inference Control for Large Language Model Services via Verifiable Observations](https://arxiv.org/html/2604.27536v1) — arXiv:2604.27536v1；Submitted `2026-04-30T07:40:24Z`；访问 2026-08-31。
- [Trace-Level Analysis of Information Contamination in Multi-Agent Systems](https://arxiv.org/html/2604.27586v1) — arXiv:2604.27586v1；Submitted `2026-04-30T08:39:42Z`；访问 2026-08-31。
- [Optimization before Evaluation: Evaluation with Unoptimised Prompts Can be Misleading](https://arxiv.org/html/2604.27637v1) — arXiv:2604.27637v1；Submitted `2026-04-30T09:28:05Z`；访问 2026-08-31。
- [From Context to Skills: Can Language Models Learn from Context Skillfully?](https://arxiv.org/html/2604.27660v1) — arXiv:2604.27660v1；Submitted `2026-04-30T09:53:15Z`；访问 2026-08-31。
- [EviMem: Evidence-Gap-Driven Iterative Retrieval for Long-Term Conversational Memory](https://arxiv.org/html/2604.27695v1) — arXiv:2604.27695v1；Submitted `2026-04-30T10:37:04Z`；访问 2026-08-31。
- [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/html/2604.27707v1) — arXiv:2604.27707v1；Submitted `2026-04-30T10:54:56Z`；访问 2026-08-31。
- [ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control](https://arxiv.org/html/2604.27711v1) — arXiv:2604.27711v1；Submitted `2026-04-30T10:57:29Z`；访问 2026-08-31。
- [WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments](https://arxiv.org/html/2604.27776v1) — arXiv:2604.27776v1；Submitted `2026-04-30T12:13:27Z`；访问 2026-08-31。
- [Test Before You Deploy: Governing Updates in the LLM Supply Chain](https://arxiv.org/html/2604.27789v1) — arXiv:2604.27789v1；Submitted `2026-04-30T12:32:13Z`；访问 2026-08-31。
- [MCPHunt: An Evaluation Framework for Cross-Boundary Data Propagation in Multi-Server MCP Agents](https://arxiv.org/html/2604.27819v1) — arXiv:2604.27819v1；Submitted `2026-04-30T13:01:03Z`；访问 2026-08-31。
- [AI Inference as Relocatable Electricity Demand: A Latency-Constrained Energy-Geography Framework](https://arxiv.org/html/2604.27855v1) — arXiv:2604.27855v1；Submitted `2026-04-30T13:40:26Z`；访问 2026-08-31。
- [From Unstructured Recall to Schema-Grounded Memory: Reliable AI Memory via Iterative, Schema-Aware Extraction](https://arxiv.org/html/2604.27906v1) — arXiv:2604.27906v1；Submitted `2026-04-30T14:14:02Z`；访问 2026-08-31。
- [RHyVE: Competence-Aware Verification and Phase-Aware Deployment for LLM-Generated Reward Hypotheses](https://arxiv.org/html/2604.28056v1) — arXiv:2604.28056v1；Submitted `2026-04-30T16:01:51Z`；访问 2026-08-31。
- [Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/html/2604.28123v1) — arXiv:2604.28123v1；Submitted `2026-04-30T17:12:53Z`；访问 2026-08-31。
- [Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection](https://arxiv.org/html/2604.28129v1) — arXiv:2604.28129v1；Submitted `2026-04-30T17:16:33Z`；访问 2026-08-31。
- [FlashRT: Towards Computationally and Memory Efficient Red-Teaming for Prompt Injection and Knowledge Corruption](https://arxiv.org/html/2604.28157v1) — arXiv:2604.28157v1；Submitted `2026-04-30T17:43:24Z`；访问 2026-08-31。
- [Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists](https://arxiv.org/html/2604.28158v1) — arXiv:2604.28158v1；Submitted `2026-04-30T17:44:55Z`；访问 2026-08-31。
- [Strait: Perceiving Priority and Interference in ML Inference Serving](https://arxiv.org/html/2604.28175v1) — arXiv:2604.28175v1；Submitted `2026-04-30T17:55:28Z`；访问 2026-08-31。
- [Synthetic Computers at Scale for Long-Horizon Productivity Simulation](https://arxiv.org/html/2604.28181v1) — arXiv:2604.28181v1；Submitted `2026-04-30T17:58:02Z`；访问 2026-08-31。
- [Exploration Hacking: Can LLMs Learn to Resist RL Training?](https://arxiv.org/html/2604.28182v1) — arXiv:2604.28182v1；Submitted `2026-04-30T17:58:39Z`；访问 2026-08-31。
- [Representation Fréchet Loss for Visual Generation](https://arxiv.org/html/2604.28190v1) — arXiv:2604.28190v1；Submitted `2026-04-30T17:59:51Z`；访问 2026-08-31。
- [HERMES++: Toward a Unified Driving World Model for 3D Scene Understanding and Generation](https://arxiv.org/html/2604.28196v1) — arXiv:2604.28196v1；Submitted `2026-04-30T17:59:58Z`；访问 2026-08-31。
- [In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks](https://arxiv.org/html/2604.27891v1) — arXiv:2604.27891v1；Submitted `2026-04-30T14:07:37Z`；访问 2026-08-31。
- [Why Do LLMs Struggle in Strategic Play? Broken Links Between Observations, Beliefs, and Actions](https://arxiv.org/html/2605.00226v1) — arXiv:2605.00226v1；Submitted `2026-04-30T21:04:38Z`；访问 2026-08-31。
- [VitaLLM: A Versatile, Ultra-Compact Ternary LLM Accelerator with Dependency-Aware Scheduling](https://arxiv.org/html/2604.27396v1) — arXiv:2604.27396v1；Submitted `2026-04-30T04:07:21Z`；访问 2026-08-31。
- [ScaleBox: Enabling High-Fidelity and Scalable Code Verification for Large Language Models](https://arxiv.org/html/2604.27467v1) — arXiv:2604.27467v1；Submitted `2026-04-30T06:09:17Z`；访问 2026-08-31。
- [CuLifter: Lifting GPU Binaries to Typed IR](https://arxiv.org/html/2604.27486v1) — arXiv:2604.27486v1；Submitted `2026-04-30T06:34:54Z`；访问 2026-08-31。
- [The Grand Software Supply Chain of AI Systems](https://arxiv.org/html/2604.27781v1) — arXiv:2604.27781v1；Submitted `2026-04-30T12:21:24Z`；访问 2026-08-31。
- [TwinGate: Stateful Defense against Decompositional Jailbreaks in Untraceable Traffic via Asymmetric Contrastive Learning](https://arxiv.org/html/2604.27861v1) — arXiv:2604.27861v1；Submitted `2026-04-30T13:44:01Z`；访问 2026-08-31。
- [SimEval-IR: A Unified Toolkit and Benchmark Suite for Evaluating User Simulators and Search Sessions](https://arxiv.org/html/2604.27878v1) — arXiv:2604.27878v1；Submitted `2026-04-30T13:56:18Z`；访问 2026-08-31。

## 13. Final Status

- Completion Status = `Complete`
- Coverage = `Closed`（532/532 independently audited；56 retained + 476 closures）
- Evidence = `Passed`（56/56 exact-v1 Review checked；blocked=0）
- Books = `Passed`（24/24 serial writeback + independent post-write semantic audit）
- unresolved findings = `0`
- 下一检查点：后续证据若改变 workload、ownership 或 evaluation boundary，再按 Source Family 重新打开真实 owner；本日报无需等待追加动作。
