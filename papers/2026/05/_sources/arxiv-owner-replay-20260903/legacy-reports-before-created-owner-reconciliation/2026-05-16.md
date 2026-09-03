# Daily Research — 2026-05-16

**Research Date:** 2026-05-16

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-15 09:00:00 ～ 2026-05-16 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite v2 仅支持 identity/date/abstract，技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。13 项写回已通过非写作者 post-write semantic audit，未发现 unresolved finding。

## Executive Summary

从 91,841 条 raw records 中恢复并重放 542/542 个窗口 identity。独立 reviewer 将 author denominator 66 收紧为 47（8.67%），495 项以 family-specific reason 在 denominator 前闭合；恢复 6 个 false negative，移除 25 个 false positive。47/47 项完成 exact-v1 全文 Review（1 项复用 W20 已核验全文、44 项 official HTML、2 项 official PDF），blocked=0。逐项读取 current owner 与相邻章节后，冻结 13 项最小 Books writeback queue；本 lane 未修改共享 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-16 |
| Window End | 2026-05-16 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report |  |
| Changed Source IDs |  |
| Previous Denominator ID |  |
| Denominator ID | DEN-20260516-V2-INDEPENDENT |
| Denominator Frozen At | 2026-08-31T22:45:51.082593+00:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-15T09:00:00+08:00 | 2026-05-16T09:00:00+08:00 | 2026-08-31T22:45:51.082593+00:00 | DataCite v2 2604/2605/2606 00..99 + independent 542/542 semantic replay | checked | 542 | SF-2026-ARXIV-2605-15508;SF-2026-ARXIV-2605-15514;SF-2026-ARXIV-2605-15520;SF-2026-ARXIV-2605-15529;SF-2026-ARXIV-2605-15565;SF-2026-ARXIV-2605-15573;SF-2026-ARXIV-2605-15581;SF-2026-ARXIV-2605-15609;SF-2026-ARXIV-2605-15617;SF-2026-ARXIV-2605-15618;SF-2026-ARXIV-2605-15638;SF-2026-ARXIV-2605-15648;SF-2026-ARXIV-2605-15665;SF-2026-ARXIV-2605-15694;SF-2026-ARXIV-2605-15710;SF-2026-ARXIV-2605-15734;SF-2026-ARXIV-2605-15761;SF-2026-ARXIV-2605-15777;SF-2026-ARXIV-2605-15815;SF-2026-ARXIV-2605-15846;SF-2026-ARXIV-2605-15957;SF-2026-ARXIV-2605-15960;SF-2026-ARXIV-2605-15967;SF-2026-ARXIV-2605.16007;SF-2026-ARXIV-2605-16035;SF-2026-ARXIV-2605-16154;SF-2026-ARXIV-2605-16184;SF-2026-ARXIV-2605-16194;SF-2026-ARXIV-2605-16198;SF-2026-ARXIV-2605-16217;SF-2026-ARXIV-2605.16234;SF-2026-ARXIV-2605.16255;SF-2026-ARXIV-2605-16508;SF-2026-ARXIV-2605-16565;SF-2026-ARXIV-2605.16588;SF-2026-ARXIV-2605-16604;SF-2026-ARXIV-2605-16616;SF-2026-ARXIV-2605.16622;SF-2026-ARXIV-2605-16626;SF-2026-ARXIV-2605-16630;SF-2026-ARXIV-2605-16637;SF-2026-ARXIV-2605.16647;SF-2026-ARXIV-2605-16650;SF-2026-ARXIV-2605-16704;SF-2026-ARXIV-2605-16712;SF-2026-ARXIV-2605-16725;SF-2026-ARXIV-2605-21516 | pages=300; final_cursor=end; raw=91841; registered=542; screened=542; retained=47; closure=495 | 2026-05-16T00:59:59Z | screening-ledger-independent-final.json#sha256=07452e666edfa396226eaf30eefa33b3574ea51aa8a051b3d770b75e687ac69a | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260516:start -->确定性窗口枚举与 542/542 title+abstract 语义筛选已经闭合。DataCite 不支持技术结论；所有 retained family 另由 exact-v1 HTML/PDF 或已核验同版本 Full Source Review 支持。<!-- coverage:SRC-ARXIV:20260516:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15508 | arXiv:2605.15508v1 | paper-v1:2605.15508 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15508 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-15508 | no |
| SF-2026-ARXIV-2605-15514 | arXiv:2605.15514v1 | paper-v1:2605.15514 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15514 | self | — | new_in_window | MODEL-POSITION-ENCODING | Integrate | books-review:SF-2026-ARXIV-2605-15514 | no |
| SF-2026-ARXIV-2605-15520 | arXiv:2605.15520v1 | paper-v1:2605.15520 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15520 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-15520 | no |
| SF-2026-ARXIV-2605-15529 | arXiv:2605.15529v1 | paper-v1:2605.15529 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15529 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-15529 | no |
| SF-2026-ARXIV-2605-15565 | arXiv:2605.15565v1 | paper-v1:2605.15565 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15565 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15565 | no |
| SF-2026-ARXIV-2605-15573 | arXiv:2605.15573v1 | paper-v1:2605.15573 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15573 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15573 | no |
| SF-2026-ARXIV-2605-15581 | arXiv:2605.15581v1 | paper-v1:2605.15581 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15581 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15581 | no |
| SF-2026-ARXIV-2605-15609 | arXiv:2605.15609v1 | paper-v1:2605.15609 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15609 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15609 | no |
| SF-2026-ARXIV-2605-15617 | arXiv:2605.15617v1 | paper-v1:2605.15617 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15617 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-15617 | no |
| SF-2026-ARXIV-2605-15618 | arXiv:2605.15618v1 | paper-v1:2605.15618 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15618 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15618 | no |
| SF-2026-ARXIV-2605-15638 | arXiv:2605.15638v1 | paper-v1:2605.15638 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15638 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-15638 | no |
| SF-2026-ARXIV-2605-15648 | arXiv:2605.15648v1 | paper-v1:2605.15648 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-15648 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-15648 | no |
| SF-2026-ARXIV-2605-15665 | arXiv:2605.15665v1 | paper-v1:2605.15665 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15665 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15665 | no |
| SF-2026-ARXIV-2605-15694 | arXiv:2605.15694v1 | paper-v1:2605.15694 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15694 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15694 | no |
| SF-2026-ARXIV-2605-15710 | arXiv:2605.15710v1 | paper-v1:2605.15710 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15710 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15710 | no |
| SF-2026-ARXIV-2605-15734 | arXiv:2605.15734v1 | paper-v1:2605.15734 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15734 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15734 | no |
| SF-2026-ARXIV-2605-15761 | arXiv:2605.15761v1 | paper-v1:2605.15761 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15761 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15761 | no |
| SF-2026-ARXIV-2605-15777 | arXiv:2605.15777v1 | paper-v1:2605.15777 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15777 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15777 | no |
| SF-2026-ARXIV-2605-15815 | arXiv:2605.15815v1 | paper-v1:2605.15815 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15815 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15815 | no |
| SF-2026-ARXIV-2605-15846 | arXiv:2605.15846v1 | paper-v1:2605.15846 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15846 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15846 | no |
| SF-2026-ARXIV-2605-15957 | arXiv:2605.15957v1 | paper-v1:2605.15957 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15957 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15957 | no |
| SF-2026-ARXIV-2605-15960 | arXiv:2605.15960v1 | paper-v1:2605.15960 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15960 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15960 | no |
| SF-2026-ARXIV-2605-15967 | arXiv:2605.15967v1 | paper-v1:2605.15967 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-15967 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-15967 | no |
| SF-2026-ARXIV-2605.16007 | arXiv:2605.16007v1 | paper-v1:2605.16007 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16007 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16007 | no |
| SF-2026-ARXIV-2605-16035 | arXiv:2605.16035v1 | paper-v1:2605.16035 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16035 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16035 | no |
| SF-2026-ARXIV-2605-16154 | arXiv:2605.16154v1 | paper-v1:2605.16154 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16154 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16154 | no |
| SF-2026-ARXIV-2605-16184 | arXiv:2605.16184v1 | paper-v1:2605.16184 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16184 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-16184 | no |
| SF-2026-ARXIV-2605-16194 | arXiv:2605.16194v1 | paper-v1:2605.16194 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16194 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16194 | no |
| SF-2026-ARXIV-2605-16198 | arXiv:2605.16198v1 | paper-v1:2605.16198 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16198 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16198 | no |
| SF-2026-ARXIV-2605-16217 | arXiv:2605.16217v1 | paper-v1:2605.16217 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16217 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16217 | no |
| SF-2026-ARXIV-2605.16234 | arXiv:2605.16234v1 | paper-v1:2605.16234 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16234 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Integrate | books-review:SF-2026-ARXIV-2605.16234 | no |
| SF-2026-ARXIV-2605.16255 | arXiv:2605.16255v1 | paper-v1:2605.16255 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16255 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2605.16255 | no |
| SF-2026-ARXIV-2605-16508 | arXiv:2605.16508v1 | paper-v1:2605.16508 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16508 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16508 | no |
| SF-2026-ARXIV-2605-16565 | arXiv:2605.16565v1 | paper-v1:2605.16565 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16565 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16565 | no |
| SF-2026-ARXIV-2605.16588 | arXiv:2605.16588v1 | paper-v1:2605.16588 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16588 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16588 | no |
| SF-2026-ARXIV-2605-16604 | arXiv:2605.16604v1 | paper-v1:2605.16604 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16604 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16604 | no |
| SF-2026-ARXIV-2605-16616 | arXiv:2605.16616v1 | paper-v1:2605.16616 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16616 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16616 | no |
| SF-2026-ARXIV-2605.16622 | arXiv:2605.16622v1 | paper-v1:2605.16622 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605.16622 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605.16622 | no |
| SF-2026-ARXIV-2605-16626 | arXiv:2605.16626v1 | paper-v1:2605.16626 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16626 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16626 | no |
| SF-2026-ARXIV-2605-16630 | arXiv:2605.16630v1 | paper-v1:2605.16630 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16630 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16630 | no |
| SF-2026-ARXIV-2605-16637 | arXiv:2605.16637v1 | paper-v1:2605.16637 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16637 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16637 | no |
| SF-2026-ARXIV-2605.16647 | arXiv:2605.16647v1 | paper-v1:2605.16647 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605.16647 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16647 | no |
| SF-2026-ARXIV-2605-16650 | arXiv:2605.16650v1 | paper-v1:2605.16650 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16650 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16650 | no |
| SF-2026-ARXIV-2605-16704 | arXiv:2605.16704v1 | paper-v1:2605.16704 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16704 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16704 | no |
| SF-2026-ARXIV-2605-16712 | arXiv:2605.16712v1 | paper-v1:2605.16712 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16712 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-16712 | no |
| SF-2026-ARXIV-2605-16725 | arXiv:2605.16725v1 | paper-v1:2605.16725 | 2026-W20 | 2026-05-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-16725 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16725 | no |
| SF-2026-ARXIV-2605-21516 | arXiv:2605.21516v1 | paper-v1:2605.21516 | 2026-W20 | 2026-05-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-21516 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21516 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| SF-2026-ARXIV-2605.16007 | RP-1f3b22f809a157ac | deep | arXiv:2605.16007v1 | SRC-ARXIV@arXiv:2605.16007v1 | arXiv:2605.16007v1 — Methodology: NPU Architecture-Native RaBitQ Optimizations (official v1 HTML) | arXiv:2605.16007v1 — Experiments: 4 Evaluation (official v1 HTML) | arXiv:2605.16007v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.16007.txt#sha256=b1f3535d624aa32accdc9f21f6ef783d40d52eab9631f84e126fb737d366f9cf; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16007 | complete |
| SF-2026-ARXIV-2605-16035 | RP-ebd6e8b1a1a2e6f3 | deep | arXiv:2605.16035v1 | SRC-ARXIV@arXiv:2605.16035v1 | arXiv:2605.16035v1 — Methodology: §4 The Agent Attribution Protocol (official v1 HTML) | arXiv:2605.16035v1 — Experiments: §6 Evaluation (official v1 HTML) | arXiv:2605.16035v1 — Scope and limitations: §7 Discussion (official v1 HTML) | webcache-2605.16035.txt#sha256=c00876f298081c076479a3833e984ff1e84d973a8e03091e623430c58f8cfd3a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16035 | complete |
| SF-2026-ARXIV-2605-16154 | RP-6ba11837f297e6de | deep | arXiv:2605.16154v1 | SRC-ARXIV@arXiv:2605.16154v1 | arXiv:2605.16154v1 — Methodology: §4 Probabilistic Chunk Masking (official v1 HTML) | arXiv:2605.16154v1 — Experiments: §5 Empirical Evaluation (official v1 HTML) | arXiv:2605.16154v1 — Scope and limitations: §5.2 Results and Discussion (official v1 HTML) | webcache-2605.16154.txt#sha256=30179f641f52c58da7628374dcec531f39aeec32d1be905c647cba127dc79f8a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16154 | complete |
| SF-2026-ARXIV-2605-16184 | RP-90c1541ceafca0e5 | deep | arXiv:2605.16184v1 | SRC-ARXIV@arXiv:2605.16184v1 | arXiv:2605.16184v1 — Methodology: §III System Design and Methodology (official v1 HTML) | arXiv:2605.16184v1 — Experiments: §IV Experiments (official v1 HTML) | arXiv:2605.16184v1 — Scope and limitations: §V Discussion (official v1 HTML) | webcache-2605.16184.txt#sha256=2780079103241f79e3c3c29df6482ca685d5d10100fe071005f549648e29c31d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16184 | complete |
| SF-2026-ARXIV-2605-16194 | RP-1e389147a2058e69 | deep | arXiv:2605.16194v1 | SRC-ARXIV@arXiv:2605.16194v1 | arXiv:2605.16194v1 — Methodology: PDF §§3–4 — D1–D4 coordination conventions, schema and validator | arXiv:2605.16194v1 — Experiments: PDF §§5–7 — self-application, five-paper pilot, adoption-cost analysis | arXiv:2605.16194v1 — Scope and limitations: PDF §§2,8 — prose-agent failure modes, does-not-claim boundary, open hypotheses | pdfcache-2605.16194.txt#sha256=13717f1fe595bb1e4edb7f65c8fad7eb66314cb49beef86a26da205154054d94; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16194 | complete |
| SF-2026-ARXIV-2605-16198 | RP-fe6dd7f3715c6b3c | deep | arXiv:2605.16198v1 | SRC-ARXIV@arXiv:2605.16198v1 | arXiv:2605.16198v1 — Methodology: §§3–4 assessment, monitoring, auditing and intervention (official v1 HTML) | arXiv:2605.16198v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16198v1 — Scope and limitations: §§5.1 and 6 auditor limitations/discussion (official v1 HTML) | webcache-2605.16198.txt#sha256=bab884572c3ce16e55e77a7b36fb30456e594dac76e463ff0a92e5de89a2b3d4; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16198 | complete |
| SF-2026-ARXIV-2605-16217 | RP-79306fe66ab51704 | deep | arXiv:2605.16217v1 | SRC-ARXIV@arXiv:2605.16217v1 | arXiv:2605.16217v1 — Methodology: §§2–3 Argus evidence assembly and learning (official v1 HTML) | arXiv:2605.16217v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.16217v1 — Scope and limitations: §4.4 Limitation and Discussion (official v1 HTML) | webcache-2605.16217.txt#sha256=cd150e098c1c1f4cf32d90a3f3801339c6de7c7c665ccc91cf8bab40f9caee3a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16217 | complete |
| SF-2026-ARXIV-2605.16234 | RP-ffefb93a9eb43e51 | deep | arXiv:2605.16234v1 | SRC-ARXIV@arXiv:2605.16234v1 | arXiv:2605.16234v1 — Methodology: §§1.1 and 3 protocol vocabulary and Swap-KL method (official v1 HTML) | arXiv:2605.16234v1 — Experiments: §4 Experiments (official v1 HTML) | arXiv:2605.16234v1 — Scope and limitations: Appendix M Additional Discussion (official v1 HTML) | webcache-2605.16234.txt#sha256=6343df81ae683664f6bb0f993812a6031f358d264c399fefd666327aaaf0467b; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16234 | complete |
| SF-2026-ARXIV-2605.16255 | RP-51817ec239c1ded7 | deep | arXiv:2605.16255v1 | SRC-ARXIV@arXiv:2605.16255v1 | arXiv:2605.16255v1 — Methodology: 3.1 A Tale of Two Designs (official v1 HTML) | arXiv:2605.16255v1 — Experiments: 4 Datacenter Design Evaluation Framework (official v1 HTML) | arXiv:2605.16255v1 — Scope and limitations: 8 Conclusion (official v1 HTML) | webcache-2605.16255.txt#sha256=aa49bd56b76eac31d6259afe4044fea90d444051bf0a91ef4f331f7a920814b4; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16255 | complete |
| SF-2026-ARXIV-2605-16508 | RP-280a4dc89cbe3db1 | deep | arXiv:2605.16508v1 | SRC-ARXIV@arXiv:2605.16508v1 | arXiv:2605.16508v1 — Methodology: §§3–6 setup, execution law and skill-library law (official v1 HTML) | arXiv:2605.16508v1 — Experiments: §§3 and 6 experimental setup and auto-manager evaluation (official v1 HTML) | arXiv:2605.16508v1 — Scope and limitations: §7 Discussion (official v1 HTML) | webcache-2605.16508.txt#sha256=55242c194e1bbe795d4f836d0373db41d7cff56723d1af1944e3b08c9d155756; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16508 | complete |
| SF-2026-ARXIV-2605-16565 | RP-aeb46f2dd2ff9fac | deep | arXiv:2605.16565v1 | SRC-ARXIV@arXiv:2605.16565v1 | arXiv:2605.16565v1 — Methodology: 3 Design of Accio (official v1 HTML) | arXiv:2605.16565v1 — Experiments: 5 Evaluation (official v1 HTML) | arXiv:2605.16565v1 — Scope and limitations: 3.4 Query Support and Deployment Discussion (official v1 HTML) | webcache-2605.16565.txt#sha256=749fd52ff1227a02d1f3109cf1f1c74f239c4e7f1a8f972542d207db7b155be7; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16565 | complete |
| SF-2026-ARXIV-2605.16588 | RP-42a8f44d35dd6ce8 | deep | arXiv:2605.16588v1 | SRC-ARXIV@arXiv:2605.16588v1 | arXiv:2605.16588v1 — Methodology: §IV Policy Library CBF (official v1 HTML) | arXiv:2605.16588v1 — Experiments: §§V–VI theoretical and empirical evaluation (official v1 HTML) | arXiv:2605.16588v1 — Scope and limitations: §VII Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16588.txt#sha256=74c8c0caf55313aec558581fe07cd0ac2f9ceb6b8e94b9657e1405cbb96df69b; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16588 | complete |
| SF-2026-ARXIV-2605-16604 | RP-763c2be77c02528f | deep | arXiv:2605.16604v1 | SRC-ARXIV@arXiv:2605.16604v1 | arXiv:2605.16604v1 — Methodology: §4 Risk-Calibrated Routing and Verifier Distillation (official v1 HTML) | arXiv:2605.16604v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16604v1 — Scope and limitations: §6 Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16604.txt#sha256=e7e2e1d01b7d84c0a6f1394da6cd989478df4b8cc2d745e7be689863a92501b2; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16604 | complete |
| SF-2026-ARXIV-2605-16616 | RP-0d1c3d7af26d1213 | deep | arXiv:2605.16616v1 | SRC-ARXIV@arXiv:2605.16616v1 | arXiv:2605.16616v1 — Methodology: §§1–2 task construction and system adaptation (official v1 HTML) | arXiv:2605.16616v1 — Experiments: §3 Evaluation and Results (official v1 HTML) | arXiv:2605.16616v1 — Scope and limitations: §5 Limitations and Future Work (official v1 HTML) | webcache-2605.16616.txt#sha256=c0a72e5742092c9492dbaa71d64cb07d704223b616acc543aa2363c4997d5809; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16616 | complete |
| SF-2026-ARXIV-2605.16622 | RP-b7c022327cb94a47 | deep | arXiv:2605.16622v1 | SRC-ARXIV@arXiv:2605.16622v1 | arXiv:2605.16622v1 — Methodology: 4 The Mechanism is Global Interaction (official v1 HTML) | arXiv:2605.16622v1 — Experiments: 3 Weight Decay Empirically Changes EoS Dynamics (official v1 HTML) | arXiv:2605.16622v1 — Scope and limitations: 7 Limitations (official v1 HTML) | webcache-2605.16622.txt#sha256=49144e7ec031eb353c01a4991ea78c1692757f4dbafdbcb38aa238b22381d11d; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16622 | complete |
| SF-2026-ARXIV-2605-16626 | RP-263294b76c909a3d | deep | arXiv:2605.16626v1 | SRC-ARXIV@arXiv:2605.16626v1 | arXiv:2605.16626v1 — Methodology: §§2–3 transcript properties and dataset construction (official v1 HTML) | arXiv:2605.16626v1 — Experiments: §§4–5 experimental setup and results (official v1 HTML) | arXiv:2605.16626v1 — Scope and limitations: §7 Limitations (official v1 HTML) | webcache-2605.16626.txt#sha256=465e98114176c28f000806fbafa0b48f6d672a5854ab48108145051eea62fa4e; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16626 | complete |
| SF-2026-ARXIV-2605-16630 | RP-2a83278de07df629 | deep | arXiv:2605.16630v1 | SRC-ARXIV@arXiv:2605.16630v1 | arXiv:2605.16630v1 — Methodology: §IV PrivScope (official v1 HTML) | arXiv:2605.16630v1 — Experiments: §V Evaluation (official v1 HTML) | arXiv:2605.16630v1 — Scope and limitations: §VI Conclusion; no dedicated limitations heading (official v1 HTML) | webcache-2605.16630.txt#sha256=56c1c857f912333329967801104ef738a70e38f93a0d8c87163eb2bb8f99b4b5; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16630 | complete |
| SF-2026-ARXIV-2605-16637 | RP-fc9ee7edd29fb7df | deep | arXiv:2605.16637v1 | SRC-ARXIV@arXiv:2605.16637v1 | arXiv:2605.16637v1 — Methodology: 4 System Overview (official v1 HTML) | arXiv:2605.16637v1 — Experiments: 7 Evaluation (official v1 HTML) | arXiv:2605.16637v1 — Scope and limitations: 8 Conclusion (official v1 HTML) | webcache-2605.16637.txt#sha256=d03192deedf6deb9395ab2d886fc59b485cd24ac37b850266e0a45994200017a; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16637 | complete |
| SF-2026-ARXIV-2605.16647 | RP-693007d68dab1676 | deep | arXiv:2605.16647v1 | SRC-ARXIV@arXiv:2605.16647v1 | arXiv:2605.16647v1 — Methodology: 3 Problem Formulation (official v1 HTML) | arXiv:2605.16647v1 — Experiments: 5 Complexity and Noise Analysis (official v1 HTML) | arXiv:2605.16647v1 — Scope and limitations: 8 Discussion and Limitations (official v1 HTML) | webcache-2605.16647.txt#sha256=8bb432dbe4bce20f4d45e0fa48ca522fd10372ee927a2be92c00af461b96df75; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605.16647 | complete |
| SF-2026-ARXIV-2605-16650 | RP-5d8fde7e5a819bdb | deep | arXiv:2605.16650v1 | SRC-ARXIV@arXiv:2605.16650v1 | arXiv:2605.16650v1 — Methodology: §4 SKG-Eval (official v1 HTML) | arXiv:2605.16650v1 — Experiments: §5 Experiments (official v1 HTML) | arXiv:2605.16650v1 — Scope and limitations: §5.10 Discussion and Limitations (official v1 HTML) | webcache-2605.16650.txt#sha256=40ceb2fc836a6684a5eca1aabf7338682f805ff7a8c7ff0277e17cc64a5c873f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16650 | complete |
| SF-2026-ARXIV-2605-16704 | RP-719bb53b825db5ae | deep | arXiv:2605.16704v1 | SRC-ARXIV@arXiv:2605.16704v1 | arXiv:2605.16704v1 — Methodology: §3 Dataset-Valuation Methodology (official v1 HTML) | arXiv:2605.16704v1 — Experiments: §§3.3–4 analysis and experiments (official v1 HTML) | arXiv:2605.16704v1 — Scope and limitations: §3.1 Limitations (official v1 HTML) | webcache-2605.16704.txt#sha256=0a97ecd00b9c5b62ea2f1d87d3da95d94152af3324e7c0d86b1a30cf80cca085; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16704 | complete |
| SF-2026-ARXIV-2605-16712 | RP-adfb1782e3b9383c | deep | arXiv:2605.16712v1 | SRC-ARXIV@arXiv:2605.16712v1 | arXiv:2605.16712v1 — Methodology: 4 CBEA and LCV Runtime Algorithm (official v1 HTML) | arXiv:2605.16712v1 — Experiments: 5 Evaluation and Benchmark Protocol (official v1 HTML) | arXiv:2605.16712v1 — Scope and limitations: 8 Discussion (official v1 HTML) | webcache-2605.16712.txt#sha256=5e12847eb7b6f0621c02e22251d8c88d56809e076ba6510b7fd909dc7aa0669f; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16712 | complete |
| SF-2026-ARXIV-2605-16725 | RP-9749af8e1b72dd9a | deep | arXiv:2605.16725v1 | SRC-ARXIV@arXiv:2605.16725v1 | arXiv:2605.16725v1 — Methodology: 4 Method (official v1 HTML) | arXiv:2605.16725v1 — Experiments: 5 Experiments (official v1 HTML) | arXiv:2605.16725v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.16725.txt#sha256=9ba8ecf683874b192a5c8c08a729807dc6e8edc6b576f436291147b3a8e4e8fe; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-16725 | complete |
| SF-2026-ARXIV-2605-21516 | RP-d31fc51c95c04a92 | deep | arXiv:2605.21516v1 | SRC-ARXIV@arXiv:2605.21516v1 | arXiv:2605.21516v1 — Methodology: 4 Alignment Principles for Harness Design (official v1 HTML) | arXiv:2605.21516v1 — Experiments: 5 Experiments (official v1 HTML) | arXiv:2605.21516v1 — Scope and limitations: 6 Conclusion (official v1 HTML) | webcache-2605.21516.txt#sha256=23cb65eefbe8e2c0a132169a1e50766b0da3b97715b5cfcfe529bc020caa1946; immutable artifact commit Not Disclosed | claim:SF-2026-ARXIV-2605-21516 | complete |

### Source Reviews

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

<!-- review:SF-2026-ARXIV-2605-16508:start -->
#### The Scaling Laws of Skills in LLM Agent Systems

问题与约束：As agent systems scale, skills accumulate into large reusable libraries, yet their scaling laws remain poorly understood.

机制与 ownership：Across 15 frontier LLMs, 1,141 real-world skills, and over 3M routing or execution decisions, we identify two coupled laws.

Evaluation contract：A single parameter, the routing logarithmic decay slope $b$, couples the two laws: routing-side fits predict execution-side rescue across models, showing that the same library property controls both pre-execution collapse and downstream recoverability.

Trade-off / failure：The mechanism described in `§§3–6 setup, execution law and skill-library law` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16508:start -->`The Scaling Laws of Skills in LLM Agent Systems` is supported only under the v1-disclosed workload and evaluator behind `§§3 and 6 experimental setup and auto-manager evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16508:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16508`。
<!-- review:SF-2026-ARXIV-2605-16508:end -->

<!-- review:SF-2026-ARXIV-2605-16565:start -->
#### Skim: Speculative Execution for Fast and Efficient Web Agents

问题与约束：Skim is a speculative execution framework for web agents that exploits the predictable structure of purpose-built websites.

机制与 ownership：Today's web-agent expense is not intrinsic to the tasks but a property of how agents are composed: frontier-model inference, browser rendering, and ReAct-style planning are applied to every step of every task regardless of complexity.

Evaluation contract：Across standard web-agent benchmarks paired with three backboneagents (WebVoyager, AgentOccam, BrowserUse), Skim reduces median per-task cost by 1.9x and latency by 33.4% with no accuracy loss.

Trade-off / failure：The mechanism described in `3 Design of Accio` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `3.4 Query Support and Deployment Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16565:start -->`Skim: Speculative Execution for Fast and Efficient Web Agents` is supported only under the v1-disclosed workload and evaluator behind `5 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16565:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16565`。
<!-- review:SF-2026-ARXIV-2605-16565:end -->

<!-- review:SF-2026-ARXIV-2605.16588:start -->
#### Policy Library CBF: Finite-Horizon Safety at Runtime via Parallel Rollouts

问题与约束：Safety-critical autonomy in unstructured environments poses significant challenges for online safety certification under evolving constraints.

机制与 ownership：We propose Policy Library Control Barrier Function~(PL-CBF), a runtime safety filter that evaluates a library of fallback policies via parallel finite-horizon rollouts, selects the least invasive safe mode, and enforces safety by solving a quadratic program that minimally modifies a nominal policy.

Evaluation contract：We propose Policy Library Control Barrier Function~(PL-CBF), a runtime safety filter that evaluates a library of fallback policies via parallel finite-horizon rollouts, selects the least invasive safe mode, and enforces safety by solving a quadratic program that minimally modifies a nominal policy.

Trade-off / failure：The mechanism described in `§IV Policy Library CBF` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§VII Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16588:start -->`Policy Library CBF: Finite-Horizon Safety at Runtime via Parallel Rollouts` is supported only under the v1-disclosed workload and evaluator behind `§§V–VI theoretical and empirical evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16588:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16588`。
<!-- review:SF-2026-ARXIV-2605.16588:end -->

<!-- review:SF-2026-ARXIV-2605-16604:start -->
#### R2V Agent: Teaching SLMs When to Ask for Help

问题与约束：Existing LLM cascades usually route whole queries before execution, but task difficulty shifts mid-trajectory - after flaky tool calls, truncated observations, or compounding local errors - making pre-execution routing brittle.

机制与 ownership：We introduce \textbf{R2V-Agent}, a risk-calibrated SLM-LLM routing framework for interactive agents.

Evaluation contract：Across HumanEval+, TextWorld, and TerminalBench with four SLM backbones, R2V improves the reliability-cost frontier: it achieves $94.3\%$ HumanEval+ success with $0.60\%$ LLM escalation, recovers TextWorld from $64.6\%$ SLM-only success to $98.2\%$ at $41.7\%$ escalation, and reaches $93.3\%$ TerminalBench success at $33.9\%$ LLM calls, roughly half the heuristic-router cost.

Trade-off / failure：The mechanism described in `§4 Risk-Calibrated Routing and Verifier Distillation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§6 Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16604:start -->`R2V Agent: Teaching SLMs When to Ask for Help` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16604:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16604`。
<!-- review:SF-2026-ARXIV-2605-16604:end -->

<!-- review:SF-2026-ARXIV-2605-16616:start -->
#### MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility

问题与约束：Autonomous research systems capable of generating complete scientific manuscripts have advanced rapidly, yet robust and realistic evaluation frameworks have failed to keep pace.

机制与 ownership：To bridge this gap, we introduce MLReplicate, an end-to-end benchmark evaluating autonomous research systems on machine learning reproducibility.

Evaluation contract：To bridge this gap, we introduce MLReplicate, an end-to-end benchmark evaluating autonomous research systems on machine learning reproducibility.

Trade-off / failure：The mechanism described in `§§1–2 task construction and system adaptation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5 Limitations and Future Work` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16616:start -->`MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility` is supported only under the v1-disclosed workload and evaluator behind `§3 Evaluation and Results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16616:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16616`。
<!-- review:SF-2026-ARXIV-2605-16616:end -->

<!-- review:SF-2026-ARXIV-2605.16622:start -->
#### Does Weight Decay Enhance Training Stability?

问题与约束：In modern deep learning, weight decay is often credited with "stabilizing" training dynamics, diverging from its classical role as a static regularization penalty.

机制与 ownership：We develop a mathematical framework that accurately models these phenomena and identify the global alignment of the parameter vector and the sharpness gradient as the mechanistic driver of the phase transition.

Evaluation contract：We show that weight decay robustly slows *progressive sharpening}.

Trade-off / failure：The mechanism described in `4 The Mechanism is Global Interaction` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `7 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16622:start -->`Does Weight Decay Enhance Training Stability?` is supported only under the v1-disclosed workload and evaluator behind `3 Weight Decay Empirically Changes EoS Dynamics`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16622:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16622`。
<!-- review:SF-2026-ARXIV-2605.16622:end -->

<!-- review:SF-2026-ARXIV-2605-16626:start -->
#### SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors

问题与约束：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

机制与 ownership：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

Evaluation contract：To better understand the limitations of such monitors against the diverse attack strategies that a coding agent could use, we present SLEIGHT-Bench (Subtle Low-itEration Insight-Guided Harmful Transcripts), a benchmark of synthetic transcripts containing 40 attacks across 11 categories, each showing a coding agent covertly pursuing a harmful objective (e.g.

Trade-off / failure：The mechanism described in `§§2–3 transcript properties and dataset construction` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§7 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16626:start -->`SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors` is supported only under the v1-disclosed workload and evaluator behind `§§4–5 experimental setup and results`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16626:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16626`。
<!-- review:SF-2026-ARXIV-2605-16626:end -->

<!-- review:SF-2026-ARXIV-2605-16630:start -->
#### PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems

问题与约束：Existing solutions either isolate workflows to limit cross-workflow leakage or apply general-purpose sanitization that does not reason over LC-assembled payload scope.

机制与 ownership：We present \textsc{PrivScope}, a trusted on-device payload governor that enforces \emph{task-scoped disclosure} at the local--CLM boundary, without requiring cloud-side changes.

Evaluation contract：Gains hold across five local backbones and add only seconds of on-device latency on commodity hardware.

Trade-off / failure：The mechanism described in `§IV PrivScope` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§VI Conclusion; no dedicated limitations heading` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16630:start -->`PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems` is supported only under the v1-disclosed workload and evaluator behind `§V Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16630:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16630`。
<!-- review:SF-2026-ARXIV-2605-16630:end -->

<!-- review:SF-2026-ARXIV-2605-16637:start -->
#### HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling

问题与约束：Agentic LLM applications increasingly execute user requests as multi-step workflows involving planning, tool use, branching, refinement, and synthesis.

机制与 ownership：To solve this problem, we present HexAGenT, a workflow-aware scheduler for a heterogeneous prefill-decode inference service.

Evaluation contract：Across representative agentic workloads and heterogeneous A100/H100/H200 clusters, HexAGenT reduces the SLO scale required for timely workflow completion by an average of 20.1% at 95% attainment and 33.0% at 99% attainment, with maximum reductions of 45.0% and 80.5%, respectively.

Trade-off / failure：The mechanism described in `4 System Overview` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16637:start -->`HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling` is supported only under the v1-disclosed workload and evaluator behind `7 Evaluation`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16637:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16637`。
<!-- review:SF-2026-ARXIV-2605-16637:end -->

<!-- review:SF-2026-ARXIV-2605.16647:start -->
#### Public-Decay Homomorphic State Space Models for Private Sequence Inference

问题与约束：Fully homomorphic encryption (FHE) changes sequence-model design because rotations, encrypted products, ciphertext materialization, multiplicative depth, and bootstrapping pressure can dominate ordinary neural-network costs.

机制与 ownership：This paper presents public-decay homomorphic state space models (HSSMs), recurrent/state-space blocks whose carried state is updated through ciphertext-plaintext public decay while ciphertext-ciphertext multiplication remains on a local write path.

Evaluation contract：The evaluated workflow separates client-side tokenization, frozen fastText lookup, projection, clipping, encryption, decryption, and thresholding from server-side encrypted evaluation over bounded projected features.

Trade-off / failure：The mechanism described in `3 Problem Formulation` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605.16647:start -->`Public-Decay Homomorphic State Space Models for Private Sequence Inference` is supported only under the v1-disclosed workload and evaluator behind `5 Complexity and Noise Analysis`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605.16647:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605.16647`。
<!-- review:SF-2026-ARXIV-2605.16647:end -->

<!-- review:SF-2026-ARXIV-2605-16650:start -->
#### SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs

问题与约束：Existing automatic evaluators, including LLM-as-a-judge frameworks and embedding-based metrics, largely rely on flat or turn-isolated representations, making them less effective at detecting long-range issues such as contradiction, topic drift, and entity inconsistency.

机制与 ownership：To address this, we propose SKG-Eval, a quasi-deterministic and interpretable framework that models dialogue as an evolving Semantic Knowledge Graph (SKG) of entities, relations, and commitments across turns.

Evaluation contract：Across multiple benchmarks, SKG-Eval achieves higher correlation with human judgments and substantially improves detection of long-range inconsistencies in extended conversations.

Trade-off / failure：The mechanism described in `§4 SKG-Eval` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§5.10 Discussion and Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16650:start -->`SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs` is supported only under the v1-disclosed workload and evaluator behind `§5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16650:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16650`。
<!-- review:SF-2026-ARXIV-2605-16650:end -->

<!-- review:SF-2026-ARXIV-2605-16704:start -->
#### Convex Dataset Valuation for Post-Training

问题与约束：In practice, however, developers face constraints on compute, labeling, and licensing costs that preclude using all available data, necessitating principled dataset-level selection.

机制与 ownership：To address this, we propose a scalable convex dataset-level valuation method based on kernel mean matching (KMM) in gradient space, which jointly accounts for alignment with the target task and redundancy across auxiliary datasets.

Evaluation contract：We first show that commonly used gradient alignment scores provide a reasonable yet incomplete valuation signal, as they ignore redundancy among datasets.

Trade-off / failure：The mechanism described in `§3 Dataset-Valuation Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§3.1 Limitations` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16704:start -->`Convex Dataset Valuation for Post-Training` is supported only under the v1-disclosed workload and evaluator behind `§§3.3–4 analysis and experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16704:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16704`。
<!-- review:SF-2026-ARXIV-2605-16704:end -->

<!-- review:SF-2026-ARXIV-2605-16712:start -->
#### Recall Isn't Enough: Bounding Commitments in Personalized Language Systems

问题与约束：Long-context and memory systems usually treat personalization as a recall problem.

机制与 ownership：We introduce Contract-Bounded Evidence Activation (CBEA) with Lexicographic Commitment Validation (LCV).

Evaluation contract：The result is a bounded operating point: explicit commitment control and 74-75% lower median input payload, not universal memory dominance.

Trade-off / failure：The mechanism described in `4 CBEA and LCV Runtime Algorithm` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16712:start -->`Recall Isn't Enough: Bounding Commitments in Personalized Language Systems` is supported only under the v1-disclosed workload and evaluator behind `5 Evaluation and Benchmark Protocol`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16712:end -->

Books Decision=`Integrate`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16712`。
<!-- review:SF-2026-ARXIV-2605-16712:end -->

<!-- review:SF-2026-ARXIV-2605-16725:start -->
#### Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models

问题与约束：Executable world models can be read, edited, executed, and reused for planning, but only if the program captures the environment's transition law rather than semantic shortcuts in its surface vocabulary.

机制与 ownership：We introduce Alice, a closed-loop system that treats failed candidate updates as structural signal: when a candidate explains a new transition but loses previously explained ones, the preservation conflict reveals dynamics that the current program had conflated.

Evaluation contract：We evaluate Alice on Baba in Wonderland, a prior-misaligned variant of Baba Is You that preserves simulator dynamics while replacing semantically meaningful rule-property labels with unrelated words.

Trade-off / failure：The mechanism described in `4 Method` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-16725:start -->`Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models` is supported only under the v1-disclosed workload and evaluator behind `5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-16725:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-16725`。
<!-- review:SF-2026-ARXIV-2605-16725:end -->

<!-- review:SF-2026-ARXIV-2605-21516:start -->
#### Harnesses for Inference-Time Alignment over Execution Trajectories

问题与约束：However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success.

机制与 ownership：However, more elaborate harnesses are not uniformly better: increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success.

Evaluation contract：We validate these predictions through controlled synthetic experiments and real terminal agent benchmarks.

Trade-off / failure：The mechanism described in `4 Alignment Principles for Harness Design` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `6 Conclusion` and does not promote the paper's result to a workload-independent guarantee.

旧路径与共存边界：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.

<!-- claim:SF-2026-ARXIV-2605-21516:start -->`Harnesses for Inference-Time Alignment over Execution Trajectories` is supported only under the v1-disclosed workload and evaluator behind `5 Experiments`; absent hardware, precision, length, batch, concurrency, SLO, seed, or artifact fields remain Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-21516:end -->

Books Decision=`No Change — Existing Coverage`；current owner+adjacent comparison=`books-review:SF-2026-ARXIV-2605-21516`。
<!-- review:SF-2026-ARXIV-2605-21516:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-15508 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15508 |
| SF-2026-ARXIV-2605-15514 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15514 |
| SF-2026-ARXIV-2605-15520 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15520 |
| SF-2026-ARXIV-2605-15529 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15529 |
| SF-2026-ARXIV-2605-15565 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15565 |
| SF-2026-ARXIV-2605-15573 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15573 |
| SF-2026-ARXIV-2605-15581 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15581 |
| SF-2026-ARXIV-2605-15609 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15609 |
| SF-2026-ARXIV-2605-15617 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15617 |
| SF-2026-ARXIV-2605-15618 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15618 |
| SF-2026-ARXIV-2605-15638 | score_7_9; forced_review; potential_books_delta | selected | DA-SDC-SENSOR | — | cross-layer ownership and long-lived failure boundary | analysis:DA-SDC-SENSOR |
| SF-2026-ARXIV-2605-15648 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15648 |
| SF-2026-ARXIV-2605-15665 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15665 |
| SF-2026-ARXIV-2605-15694 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15694 |
| SF-2026-ARXIV-2605-15710 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15710 |
| SF-2026-ARXIV-2605-15734 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15734 |
| SF-2026-ARXIV-2605-15761 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15761 |
| SF-2026-ARXIV-2605-15777 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15777 |
| SF-2026-ARXIV-2605-15815 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15815 |
| SF-2026-ARXIV-2605-15846 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15846 |
| SF-2026-ARXIV-2605-15957 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15957 |
| SF-2026-ARXIV-2605-15960 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15960 |
| SF-2026-ARXIV-2605-15967 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-15967 |
| SF-2026-ARXIV-2605.16007 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605.16007 |
| SF-2026-ARXIV-2605-16035 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16035 |
| SF-2026-ARXIV-2605-16154 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16154 |
| SF-2026-ARXIV-2605-16184 | score_7_9; forced_review; potential_books_delta | selected | DA-RUNTIME-OPTIMIZER | — | cross-layer ownership and long-lived failure boundary | analysis:DA-RUNTIME-OPTIMIZER |
| SF-2026-ARXIV-2605-16194 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16194 |
| SF-2026-ARXIV-2605-16198 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16198 |
| SF-2026-ARXIV-2605-16217 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16217 |
| SF-2026-ARXIV-2605.16234 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605.16234 |
| SF-2026-ARXIV-2605.16255 | score_7_9; forced_review; potential_books_delta | selected | DA-POWER-HIERARCHY | — | cross-layer ownership and long-lived failure boundary | analysis:DA-POWER-HIERARCHY |
| SF-2026-ARXIV-2605-16508 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16508 |
| SF-2026-ARXIV-2605-16565 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16565 |
| SF-2026-ARXIV-2605.16588 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605.16588 |
| SF-2026-ARXIV-2605-16604 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16604 |
| SF-2026-ARXIV-2605-16616 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16616 |
| SF-2026-ARXIV-2605.16622 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605.16622 |
| SF-2026-ARXIV-2605-16626 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16626 |
| SF-2026-ARXIV-2605-16630 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16630 |
| SF-2026-ARXIV-2605-16637 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16637 |
| SF-2026-ARXIV-2605.16647 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605.16647 |
| SF-2026-ARXIV-2605-16650 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16650 |
| SF-2026-ARXIV-2605-16704 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16704 |
| SF-2026-ARXIV-2605-16712 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16712 |
| SF-2026-ARXIV-2605-16725 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-16725 |
| SF-2026-ARXIV-2605-21516 | score_7_9 | not_selected | — | — | exact-v1 full Review complete; Daily narrative budget reserved for higher-reach deltas | analysis-decision:SF-2026-ARXIV-2605-21516 |

<!-- analysis:DA-SDC-SENSOR:start -->
### DA-SDC-SENSOR

旧路径之所以合理，是因为它在未出现该论文隔离出的约束时更简单、状态更少。exact-v1 将变化定位为：ITHICA error checks detect 39% more defective servers than native checks within the ITHICA tests derived from our baseline programs, and enable novel findings on defect behavior that challenge conclusions drawn by prior hyperscaler fleet studies. 新机制改变的 owner 是：We present ITHICA, an approach for automatically generating functional tests for defect-induced errors from arbitrary programs by inserting intra-thread, instruction-level error checks, primarily leveraging instruction duplication and output comparison. 证据只覆盖：We use ITHICA to transform industrial hyperscaler test programs (our baseline), datacenter workloads, and common libraries into functional tests, and evaluate them on over 3,000 CPU servers. 代价与失败面是：The mechanism described in `4 ITHICA: Intra-THread Instruction Checking Approach for Defect Detection` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Discussion` and does not promote the paper's result to a workload-independent guarantee. 因此旧方案仍在以下条件共存：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.
<!-- analysis:DA-SDC-SENSOR:end -->

<!-- analysis:DA-RUNTIME-OPTIMIZER:start -->
### DA-RUNTIME-OPTIMIZER

旧路径之所以合理，是因为它在未出现该论文隔离出的约束时更简单、状态更少。exact-v1 将变化定位为：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path. 新机制改变的 owner 是：We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path. 证据只覆盖：We evaluate Asteria on both memory-constrained and distributed training settings. 代价与失败面是：The mechanism described in `§III System Design and Methodology` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `§V Discussion` and does not promote the paper's result to a workload-independent guarantee. 因此旧方案仍在以下条件共存：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.
<!-- analysis:DA-RUNTIME-OPTIMIZER:end -->

<!-- analysis:DA-POWER-HIERARCHY:start -->
### DA-POWER-HIERARCHY

旧路径之所以合理，是因为它在未出现该论文隔离出的约束时更简单、状态更少。exact-v1 将变化定位为：This poses a major challenge for datacenter power delivery designers. 新机制改变的 owner 是：To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. 证据只覆盖：Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. 代价与失败面是：The mechanism described in `3.1 A Tale of Two Designs` adds its own controller/state or approximation boundary; the review therefore preserves the v1 failure surface documented by `8 Conclusion` and does not promote the paper's result to a workload-independent guarantee. 因此旧方案仍在以下条件共存：The prior design remains valid when the changed constraint isolated by this paper is absent, or when the added controller, metadata, verification, communication, or operational cost exceeds the measured benefit.
<!-- analysis:DA-POWER-HIERARCHY:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15508:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15508:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15514:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15514:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15520:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15520:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15529:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15529:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15565:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15565:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15573:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15573:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15581:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15581:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15609:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15609:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15617:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15617:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15618:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15618:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15648:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15648:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15665:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15665:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15694:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15694:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15710:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15710:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15734:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15734:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15761:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15761:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15777:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15777:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15815:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15815:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15846:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15846:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15957:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15957:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15960:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15960:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-15967:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-15967:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605.16007:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605.16007:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16035:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16035:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16154:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16154:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16194:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16194:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16198:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16198:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16217:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16217:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605.16234:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605.16234:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16508:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16508:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16565:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16565:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605.16588:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605.16588:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16604:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16604:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16616:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16616:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605.16622:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605.16622:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16626:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16626:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16630:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16630:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16637:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16637:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605.16647:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605.16647:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16650:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16650:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16704:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16704:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16712:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16712:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16725:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-16725:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-21516:start -->exact-v1 full Review 已完成；未扩写只因 Daily 最多三项，不影响 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-21516:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
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
| SF-2026-ARXIV-2605.16007 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605.16007 | delta:SF-2026-ARXIV-2605.16007 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16007 |
| SF-2026-ARXIV-2605-16035 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16035 | delta:SF-2026-ARXIV-2605-16035 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16035 |
| SF-2026-ARXIV-2605-16154 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16154 | delta:SF-2026-ARXIV-2605-16154 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16154 |
| SF-2026-ARXIV-2605-16184 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-16184 | delta:SF-2026-ARXIV-2605-16184 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16184 |
| SF-2026-ARXIV-2605-16194 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16194 | delta:SF-2026-ARXIV-2605-16194 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16194 |
| SF-2026-ARXIV-2605-16198 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16198 | delta:SF-2026-ARXIV-2605-16198 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16198 |
| SF-2026-ARXIV-2605-16217 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-16217 | delta:SF-2026-ARXIV-2605-16217 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16217 |
| SF-2026-ARXIV-2605.16234 | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#chapter-17 | books/part-02-model/16-feed-forward-mlp.md#chapter-16;books/part-02-model/18-decoder-only.md#chapter-18 | existing:SF-2026-ARXIV-2605.16234 | delta:SF-2026-ARXIV-2605.16234 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16234 |
| SF-2026-ARXIV-2605.16255 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#chapter-70 | books/part-06-ai-infrastructure/69-trace.md#chapter-69;books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71 | existing:SF-2026-ARXIV-2605.16255 | delta:SF-2026-ARXIV-2605.16255 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16255 |
| SF-2026-ARXIV-2605-16508 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16508 | delta:SF-2026-ARXIV-2605-16508 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16508 |
| SF-2026-ARXIV-2605-16565 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78;books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-16565 | delta:SF-2026-ARXIV-2605-16565 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16565 |
| SF-2026-ARXIV-2605.16588 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25;books/part-03-multimodal-world-models/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605.16588 | delta:SF-2026-ARXIV-2605.16588 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16588 |
| SF-2026-ARXIV-2605-16604 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-16604 | delta:SF-2026-ARXIV-2605-16604 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16604 |
| SF-2026-ARXIV-2605-16616 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16616 | delta:SF-2026-ARXIV-2605-16616 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16616 |
| SF-2026-ARXIV-2605.16622 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605.16622 | delta:SF-2026-ARXIV-2605.16622 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605.16622 |
| SF-2026-ARXIV-2605-16626 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-16626 | delta:SF-2026-ARXIV-2605-16626 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16626 |
| SF-2026-ARXIV-2605-16630 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-16630 | delta:SF-2026-ARXIV-2605-16630 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16630 |
| SF-2026-ARXIV-2605-16637 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55;books/part-05-inference-system/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-16637 | delta:SF-2026-ARXIV-2605-16637 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16637 |
| SF-2026-ARXIV-2605.16647 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605.16647 | delta:SF-2026-ARXIV-2605.16647 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605.16647 |
| SF-2026-ARXIV-2605-16650 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-16650 | delta:SF-2026-ARXIV-2605-16650 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16650 |
| SF-2026-ARXIV-2605-16704 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-16704 | delta:SF-2026-ARXIV-2605-16704 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16704 |
| SF-2026-ARXIV-2605-16712 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-16712 | delta:SF-2026-ARXIV-2605-16712 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16712 |
| SF-2026-ARXIV-2605-16725 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-16725 | delta:SF-2026-ARXIV-2605-16725 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16725 |
| SF-2026-ARXIV-2605-21516 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83;books/part-07-agent/README.md#knowledge-tree | existing:SF-2026-ARXIV-2605-21516 | delta:SF-2026-ARXIV-2605-21516 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-21516 |
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
<!-- books-review:SF-2026-ARXIV-2605.16007:start -->
<!-- existing:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- existing:SF-2026-ARXIV-2605.16007:end -->
<!-- delta:SF-2026-ARXIV-2605.16007:start -->Ch49 already includes NPU/CPU phase ownership, quantized candidate generation, host reranking and heterogeneous scheduling; this is architecture-specific evidence.<!-- delta:SF-2026-ARXIV-2605.16007:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16007:end -->
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
<!-- books-review:SF-2026-ARXIV-2605.16234:start -->
<!-- existing:SF-2026-ARXIV-2605.16234:start -->`books/part-02-model/17-transformer-layer.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16234:end -->
<!-- delta:SF-2026-ARXIV-2605.16234:start -->Layer redundancy conclusions change between replacement and interchange protocols, so pruning must freeze intervention semantics and evaluator identity before treating layers as substitutable.<!-- delta:SF-2026-ARXIV-2605.16234:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16234:end -->
<!-- books-review:SF-2026-ARXIV-2605.16255:start -->
<!-- existing:SF-2026-ARXIV-2605.16255:start -->`books/part-06-ai-infrastructure/70-cost.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16255:end -->
<!-- delta:SF-2026-ARXIV-2605.16255:start -->AI power design is reframed from installed megawatts to deployable capacity across rack generations, linking topology, placement and redundancy to multi-resource stranding.<!-- delta:SF-2026-ARXIV-2605.16255:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16255:end -->
<!-- books-review:SF-2026-ARXIV-2605-16508:start -->
<!-- existing:SF-2026-ARXIV-2605-16508:start -->Ch84 already models skill-library competence, selection, transfer, interference and lifecycle; the scaling law is supporting evidence, not a new contract.<!-- existing:SF-2026-ARXIV-2605-16508:end -->
<!-- delta:SF-2026-ARXIV-2605-16508:start -->Ch84 already models skill-library competence, selection, transfer, interference and lifecycle; the scaling law is supporting evidence, not a new contract.<!-- delta:SF-2026-ARXIV-2605-16508:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16508:end -->
<!-- books-review:SF-2026-ARXIV-2605-16565:start -->
<!-- existing:SF-2026-ARXIV-2605-16565:start -->Ch79 and Ch56 already own speculative action planning, validation, commit and rollback under latency/cost budgets.<!-- existing:SF-2026-ARXIV-2605-16565:end -->
<!-- delta:SF-2026-ARXIV-2605-16565:start -->Ch79 and Ch56 already own speculative action planning, validation, commit and rollback under latency/cost budgets.<!-- delta:SF-2026-ARXIV-2605-16565:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16565:end -->
<!-- books-review:SF-2026-ARXIV-2605.16588:start -->
<!-- existing:SF-2026-ARXIV-2605.16588:start -->Ch26 already includes stronger runtime-assurance separation between nominal controller, safety admission and verified fallback under physical evidence.<!-- existing:SF-2026-ARXIV-2605.16588:end -->
<!-- delta:SF-2026-ARXIV-2605.16588:start -->Ch26 already includes stronger runtime-assurance separation between nominal controller, safety admission and verified fallback under physical evidence.<!-- delta:SF-2026-ARXIV-2605.16588:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16588:end -->
<!-- books-review:SF-2026-ARXIV-2605-16604:start -->
<!-- existing:SF-2026-ARXIV-2605-16604:start -->Ch56 already admits/escalates work by uncertainty, evidence value, cost and SLO, with a bounded fallback to stronger execution.<!-- existing:SF-2026-ARXIV-2605-16604:end -->
<!-- delta:SF-2026-ARXIV-2605-16604:start -->Ch56 already admits/escalates work by uncertainty, evidence value, cost and SLO, with a bounded fallback to stronger execution.<!-- delta:SF-2026-ARXIV-2605-16604:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16604:end -->
<!-- books-review:SF-2026-ARXIV-2605-16616:start -->
<!-- existing:SF-2026-ARXIV-2605-16616:start -->Ch66 already requires immutable task, environment, code, artifact and evaluator identity for reproducible autonomous-research evidence.<!-- existing:SF-2026-ARXIV-2605-16616:end -->
<!-- delta:SF-2026-ARXIV-2605-16616:start -->Ch66 already requires immutable task, environment, code, artifact and evaluator identity for reproducible autonomous-research evidence.<!-- delta:SF-2026-ARXIV-2605-16616:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16616:end -->
<!-- books-review:SF-2026-ARXIV-2605.16622:start -->
<!-- existing:SF-2026-ARXIV-2605.16622:start -->`books/part-04-training-system/28-pretraining.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605.16622:end -->
<!-- delta:SF-2026-ARXIV-2605.16622:start -->Weight decay changes progressive sharpening through global parameter interaction rather than simple local friction, refining Ch28's stability/EoS mechanism and architecture-dependent boundary.<!-- delta:SF-2026-ARXIV-2605.16622:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605.16622:end -->
<!-- books-review:SF-2026-ARXIV-2605-16626:start -->
<!-- existing:SF-2026-ARXIV-2605-16626:start -->Ch67 and Ch72 already treat adaptive monitor evasion, blind spots and false-negative measurement as part of the security evidence contract.<!-- existing:SF-2026-ARXIV-2605-16626:end -->
<!-- delta:SF-2026-ARXIV-2605-16626:start -->Ch67 and Ch72 already treat adaptive monitor evasion, blind spots and false-negative measurement as part of the security evidence contract.<!-- delta:SF-2026-ARXIV-2605-16626:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16626:end -->
<!-- books-review:SF-2026-ARXIV-2605-16630:start -->
<!-- existing:SF-2026-ARXIV-2605-16630:start -->Ch72 already binds disclosure to task intent, data flow, access scope, local/cloud trust boundary and least-privilege release.<!-- existing:SF-2026-ARXIV-2605-16630:end -->
<!-- delta:SF-2026-ARXIV-2605-16630:start -->Ch72 already binds disclosure to task intent, data flow, access scope, local/cloud trust boundary and least-privilege release.<!-- delta:SF-2026-ARXIV-2605-16630:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16630:end -->
<!-- books-review:SF-2026-ARXIV-2605-16637:start -->
<!-- existing:SF-2026-ARXIV-2605-16637:start -->Ch56 already owns online workflow DAGs, heterogeneous placement, critical-path scheduling, queue pressure and SLO-aware fallback.<!-- existing:SF-2026-ARXIV-2605-16637:end -->
<!-- delta:SF-2026-ARXIV-2605-16637:start -->Ch56 already owns online workflow DAGs, heterogeneous placement, critical-path scheduling, queue pressure and SLO-aware fallback.<!-- delta:SF-2026-ARXIV-2605-16637:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16637:end -->
<!-- books-review:SF-2026-ARXIV-2605.16647:start -->
<!-- existing:SF-2026-ARXIV-2605.16647:start -->Ch72 already carries encrypted state-space inference, public-parameter constraints, ciphertext depth/noise and FHE fallback boundaries.<!-- existing:SF-2026-ARXIV-2605.16647:end -->
<!-- delta:SF-2026-ARXIV-2605.16647:start -->Ch72 already carries encrypted state-space inference, public-parameter constraints, ciphertext depth/noise and FHE fallback boundaries.<!-- delta:SF-2026-ARXIV-2605.16647:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605.16647:end -->
<!-- books-review:SF-2026-ARXIV-2605-16650:start -->
<!-- existing:SF-2026-ARXIV-2605-16650:start -->Ch66 and Ch77 already evaluate stateful dialogue through incremental state identity, provenance, contradiction handling and longitudinal effects.<!-- existing:SF-2026-ARXIV-2605-16650:end -->
<!-- delta:SF-2026-ARXIV-2605-16650:start -->Ch66 and Ch77 already evaluate stateful dialogue through incremental state identity, provenance, contradiction handling and longitudinal effects.<!-- delta:SF-2026-ARXIV-2605-16650:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16650:end -->
<!-- books-review:SF-2026-ARXIV-2605-16704:start -->
<!-- existing:SF-2026-ARXIV-2605-16704:start -->Ch27 already treats dataset value as a set-level gradient-space diversity/quality allocation problem rather than additive example scores.<!-- existing:SF-2026-ARXIV-2605-16704:end -->
<!-- delta:SF-2026-ARXIV-2605-16704:start -->Ch27 already treats dataset value as a set-level gradient-space diversity/quality allocation problem rather than additive example scores.<!-- delta:SF-2026-ARXIV-2605-16704:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16704:end -->
<!-- books-review:SF-2026-ARXIV-2605-16712:start -->
<!-- existing:SF-2026-ARXIV-2605-16712:start -->`books/part-07-agent/77-memory.md` contains the surrounding principle but not the exact control/evidence delta below; adjacent chapters do not own it.<!-- existing:SF-2026-ARXIV-2605-16712:end -->
<!-- delta:SF-2026-ARXIV-2605-16712:start -->Retrieved personal facts must not automatically become behavioral commitments; activation, validation and realization need a bounded-commitment authority distinct from recall ownership.<!-- delta:SF-2026-ARXIV-2605-16712:end --> Final decision=`Integrate`。
<!-- books-review:SF-2026-ARXIV-2605-16712:end -->
<!-- books-review:SF-2026-ARXIV-2605-16725:start -->
<!-- existing:SF-2026-ARXIV-2605-16725:start -->Ch25 already requires persistent, revisable and executable world state updated by failed predictions and targeted exploration.<!-- existing:SF-2026-ARXIV-2605-16725:end -->
<!-- delta:SF-2026-ARXIV-2605-16725:start -->Ch25 already requires persistent, revisable and executable world state updated by failed predictions and targeted exploration.<!-- delta:SF-2026-ARXIV-2605-16725:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-16725:end -->
<!-- books-review:SF-2026-ARXIV-2605-21516:start -->
<!-- existing:SF-2026-ARXIV-2605-21516:start -->Ch84 already binds inference-time harnesses to capability, evidence granularity, trajectory effects and partial-control reliability trade-offs.<!-- existing:SF-2026-ARXIV-2605-21516:end -->
<!-- delta:SF-2026-ARXIV-2605-21516:start -->Ch84 already binds inference-time harnesses to capability, evidence granularity, trajectory effects and partial-control reliability trade-offs.<!-- delta:SF-2026-ARXIV-2605-21516:end --> Final decision=`No Change — Existing Coverage`。
<!-- books-review:SF-2026-ARXIV-2605-21516:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260516-COVERAGE | fresh-context:may2026-day02 | coverage | coverage:SRC-ARXIV:20260516 | None | screening-ledger-independent-final.json#independent_reconciliation | passed |
| SA-20260516-EVIDENCE | fresh-context:may2026-day02 | evidence | review:SF-2026-ARXIV-2605-15508 | None | exact-v1-independent-review-packet.json#reviews | passed |
| SA-20260516-SELECTION | fresh-context:may2026-day02 | deep_analysis_selection | analysis:DA-SDC-SENSOR | None | semantic-independent-audit.json#deep_analysis_selection | passed |
| SA-20260516-BOOKS | fresh-context:may2026-day03 | books | books-review:SF-2026-ARXIV-2605-15508 | None | post-write-semantic-audit.json#items；13/13 mechanism placement and adjacent-owner checks passed | passed |

## 8. Ignored Noise

495 条 family-specific pre-denominator closure 保存在 `screening-ledger-independent-final.json`；没有把 Core Daily recall 偷换为 Candidate Denominator。

## 9. Recommended Action

保持本日结论；未来只在 primary-source revision、owner 冲突或 Books 机制结论变化时重开。

## 10. Repository Changes

- 05-16 date-local denominator、exact-v1 packet、Books comparison、queue、independent audit、post-write semantic audit 与 canonical Daily 已更新。
- 13 项共享 Books 写回由 root 完成；本审计 lane 只读取 Books 并核验 13/13，不修改共享 Books，未 stage、commit 或 push。

## 11. Open Questions

- 无。本日 Coverage、Evidence 与 Books Gate 均已闭合；13 项均形成完整机制链且未发现相邻章节 owner 冲突。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/html/2605.15508v1) — arXiv:2605.15508v1；first-public 2026-05-15；receipt `webcache-2605.15508.txt`；accessed 2026-09-01
- [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/html/2605.15514v1) — arXiv:2605.15514v1；first-public 2026-05-15；receipt `webcache-2605.15514.txt`；accessed 2026-09-01
- [On the Fragility of Data Attribution When Learning Is Distributed](https://arxiv.org/html/2605.15520v1) — arXiv:2605.15520v1；first-public 2026-05-15；receipt `webcache-2605.15520.txt`；accessed 2026-09-01
- [Process Rewards with Learned Reliability](https://arxiv.org/html/2605.15529v1) — arXiv:2605.15529v1；first-public 2026-05-15；receipt `../../weekly/2026-W20/README.md#process-rewards-with-learned-reliability`；accessed 2026-09-01
- [AstraFlow: Dataflow-Oriented Reinforcement Learning for Agentic LLMs](https://arxiv.org/html/2605.15565v1) — arXiv:2605.15565v1；first-public 2026-05-15；receipt `webcache-2605.15565.txt`；accessed 2026-09-01
- [Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems](https://arxiv.org/html/2605.15573v1) — arXiv:2605.15573v1；first-public 2026-05-15；receipt `webcache-2605.15573.txt`；accessed 2026-09-01
- [STAR: A Stage-attributed Triage and Repair framework for RCA Agents in Microservices](https://arxiv.org/html/2605.15581v1) — arXiv:2605.15581v1；first-public 2026-05-15；receipt `webcache-2605.15581.txt`；accessed 2026-09-01
- [PSD: Pushing the Pareto Frontier of Diffusion LLMs via Parallel Speculative Decoding](https://arxiv.org/html/2605.15609v1) — arXiv:2605.15609v1；first-public 2026-05-15；receipt `webcache-2605.15609.txt`；accessed 2026-09-01
- [A Few GPUs, A Whole Lotta Scale: Faithful LLM Training Emulation with PrismLLM](https://arxiv.org/html/2605.15617v1) — arXiv:2605.15617v1；first-public 2026-05-15；receipt `webcache-2605.15617.txt`；accessed 2026-09-01
- [Latent Video Prediction Learns Better World Models](https://arxiv.org/html/2605.15618v1) — arXiv:2605.15618v1；first-public 2026-05-15；receipt `webcache-2605.15618.txt`；accessed 2026-09-01
- [ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions](https://arxiv.org/html/2605.15638v1) — arXiv:2605.15638v1；first-public 2026-05-15；receipt `webcache-2605.15638.txt`；accessed 2026-09-01
- [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/html/2605.15648v1) — arXiv:2605.15648v1；first-public 2026-05-15；receipt `webcache-2605.15648.txt`；accessed 2026-09-01
- [PRISM: Prompt Reliability via Iterative Simulation and Monitoring for Enterprise Conversational AI](https://arxiv.org/html/2605.15665v1) — arXiv:2605.15665v1；first-public 2026-05-15；receipt `webcache-2605.15665.txt`；accessed 2026-09-01
- [Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices](https://arxiv.org/pdf/2605.15694v1) — arXiv:2605.15694v1；first-public 2026-05-15；receipt `pdfcache-2605.15694.txt`；accessed 2026-09-01
- [SMMBench: A Benchmark for Source-Distributed Multimodal Agent Memory](https://arxiv.org/html/2605.15710v1) — arXiv:2605.15710v1；first-public 2026-05-15；receipt `webcache-2605.15710.txt`；accessed 2026-09-01
- [Can We Trust AI-Inferred User States. A Psychometric Framework for Validating the Reliability of Users States Classification by LLMs in Operational Environments](https://arxiv.org/html/2605.15734v1) — arXiv:2605.15734v1；first-public 2026-05-15；receipt `webcache-2605.15734.txt`；accessed 2026-09-01
- [A Unified Perturbation Framework for Analyzing Leaderboard Stability and Manipulation](https://arxiv.org/html/2605.15761v1) — arXiv:2605.15761v1；first-public 2026-05-15；receipt `webcache-2605.15761.txt`；accessed 2026-09-01
- [SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](https://arxiv.org/html/2605.15777v1) — arXiv:2605.15777v1；first-public 2026-05-15；receipt `webcache-2605.15777.txt`；accessed 2026-09-01
- [BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge](https://arxiv.org/html/2605.15815v1) — arXiv:2605.15815v1；first-public 2026-05-15；receipt `webcache-2605.15815.txt`；accessed 2026-09-01
- [RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades](https://arxiv.org/html/2605.15846v1) — arXiv:2605.15846v1；first-public 2026-05-15；receipt `webcache-2605.15846.txt`；accessed 2026-09-01
- [To GPU or Not to GPU: Vector Search in Relational Engines](https://arxiv.org/html/2605.15957v1) — arXiv:2605.15957v1；first-public 2026-05-15；receipt `webcache-2605.15957.txt`；accessed 2026-09-01
- [Imperfect World Models are Exploitable](https://arxiv.org/html/2605.15960v1) — arXiv:2605.15960v1；first-public 2026-05-15；receipt `webcache-2605.15960.txt`；accessed 2026-09-01
- [Deterministic Event-Graph Substrates as World Models for Counterfactual Reasoning](https://arxiv.org/html/2605.15967v1) — arXiv:2605.15967v1；first-public 2026-05-15；receipt `webcache-2605.15967.txt`；accessed 2026-09-01
- [Ascend-RaBitQ: Heterogeneous NPU-CPU Acceleration of Billion-Scale Similarity Search with 1-bit Quantization](https://arxiv.org/html/2605.16007v1) — arXiv:2605.16007v1；first-public 2026-05-15；receipt `webcache-2605.16007.txt`；accessed 2026-09-01
- [Who Owns This Agent? Tracing AI Agents Back to Their Owners](https://arxiv.org/html/2605.16035v1) — arXiv:2605.16035v1；first-public 2026-05-15；receipt `webcache-2605.16035.txt`；accessed 2026-09-01
- [Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking](https://arxiv.org/html/2605.16154v1) — arXiv:2605.16154v1；first-public 2026-05-15；receipt `webcache-2605.16154.txt`；accessed 2026-09-01
- [Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training](https://arxiv.org/html/2605.16184v1) — arXiv:2605.16184v1；first-public 2026-05-15；receipt `webcache-2605.16184.txt`；accessed 2026-09-01
- [paper.json: A Coordination Convention for LLM-Agent-Actionable Papers](https://arxiv.org/pdf/2605.16194v1) — arXiv:2605.16194v1；first-public 2026-05-15；receipt `pdfcache-2605.16194.txt`；accessed 2026-09-01
- [Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems](https://arxiv.org/html/2605.16198v1) — arXiv:2605.16198v1；first-public 2026-05-15；receipt `webcache-2605.16198.txt`；accessed 2026-09-01
- [Argus: Evidence Assembly for Scalable Deep Research Agents](https://arxiv.org/html/2605.16217v1) — arXiv:2605.16217v1；first-public 2026-05-15；receipt `webcache-2605.16217.txt`；accessed 2026-09-01
- [No Free Swap: Protocol-Dependent Layer Redundancy in Transformers](https://arxiv.org/html/2605.16234v1) — arXiv:2605.16234v1；first-public 2026-05-15；receipt `webcache-2605.16234.txt`；accessed 2026-09-01
- [Designing Datacenter Power Delivery Hierarchies for the AI Era](https://arxiv.org/html/2605.16255v1) — arXiv:2605.16255v1；first-public 2026-05-15；receipt `webcache-2605.16255.txt`；accessed 2026-09-01
- [The Scaling Laws of Skills in LLM Agent Systems](https://arxiv.org/html/2605.16508v1) — arXiv:2605.16508v1；first-public 2026-05-15；receipt `webcache-2605.16508.txt`；accessed 2026-09-01
- [Skim: Speculative Execution for Fast and Efficient Web Agents](https://arxiv.org/html/2605.16565v1) — arXiv:2605.16565v1；first-public 2026-05-15；receipt `webcache-2605.16565.txt`；accessed 2026-09-01
- [Policy Library CBF: Finite-Horizon Safety at Runtime via Parallel Rollouts](https://arxiv.org/html/2605.16588v1) — arXiv:2605.16588v1；first-public 2026-05-15；receipt `webcache-2605.16588.txt`；accessed 2026-09-01
- [R2V Agent: Teaching SLMs When to Ask for Help](https://arxiv.org/html/2605.16604v1) — arXiv:2605.16604v1；first-public 2026-05-15；receipt `webcache-2605.16604.txt`；accessed 2026-09-01
- [MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility](https://arxiv.org/html/2605.16616v1) — arXiv:2605.16616v1；first-public 2026-05-15；receipt `webcache-2605.16616.txt`；accessed 2026-09-01
- [Does Weight Decay Enhance Training Stability?](https://arxiv.org/html/2605.16622v1) — arXiv:2605.16622v1；first-public 2026-05-15；receipt `webcache-2605.16622.txt`；accessed 2026-09-01
- [SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors](https://arxiv.org/html/2605.16626v1) — arXiv:2605.16626v1；first-public 2026-05-15；receipt `webcache-2605.16626.txt`；accessed 2026-09-01
- [PrivScope: Task-scoped Disclosure Control for Hybrid Agentic Systems](https://arxiv.org/html/2605.16630v1) — arXiv:2605.16630v1；first-public 2026-05-15；receipt `webcache-2605.16630.txt`；accessed 2026-09-01
- [HexAGenT: Efficient Agentic LLM Serving via Workflow- and Heterogeneity-Aware Scheduling](https://arxiv.org/html/2605.16637v1) — arXiv:2605.16637v1；first-public 2026-05-15；receipt `webcache-2605.16637.txt`；accessed 2026-09-01
- [Public-Decay Homomorphic State Space Models for Private Sequence Inference](https://arxiv.org/html/2605.16647v1) — arXiv:2605.16647v1；first-public 2026-05-15；receipt `webcache-2605.16647.txt`；accessed 2026-09-01
- [SKG-Eval: Stateful Evaluation of Multi-Turn Dialogue via Incremental Semantic Knowledge Graphs](https://arxiv.org/html/2605.16650v1) — arXiv:2605.16650v1；first-public 2026-05-15；receipt `webcache-2605.16650.txt`；accessed 2026-09-01
- [Convex Dataset Valuation for Post-Training](https://arxiv.org/html/2605.16704v1) — arXiv:2605.16704v1；first-public 2026-05-15；receipt `webcache-2605.16704.txt`；accessed 2026-09-01
- [Recall Isn't Enough: Bounding Commitments in Personalized Language Systems](https://arxiv.org/html/2605.16712v1) — arXiv:2605.16712v1；first-public 2026-05-15；receipt `webcache-2605.16712.txt`；accessed 2026-09-01
- [Baba in Wonderland: Online Self-Supervised Dynamics Discovery for Executable World Models](https://arxiv.org/html/2605.16725v1) — arXiv:2605.16725v1；first-public 2026-05-15；receipt `webcache-2605.16725.txt`；accessed 2026-09-01
- [Harnesses for Inference-Time Alignment over Execution Trajectories](https://arxiv.org/html/2605.21516v1) — arXiv:2605.21516v1；first-public 2026-05-15；receipt `webcache-2605.21516.txt`；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

05-16 recall、denominator、exact-v1 Evidence Review、Books writeback 与非写作者 post-write semantic audit 已全部闭合。
