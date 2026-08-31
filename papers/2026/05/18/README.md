# Daily Research — 2026-05-18

**Research Date:** 2026-05-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-17 09:00:00 ～ 2026-05-18 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。14/14 Books Integration 已通过 fresh-context post-write semantic audit。

## Executive Summary

91,841 条 raw records 中窗口注册并逐项筛选 324 项。独立审计把作者分母 26 修正为 52（重开 26 个 false negatives），closure 298→272；52/52 exact-v1 完整、blocked=0。作者 16 项 provisional Integrate 经 current owner+adjacent 比较后收敛为 14 项最终 queue；root 已写回 14/14。fresh-context post-write re-audit 确认 owner、相邻章、唯一 marker 与 Review notes 位置全部正确，8 项既有 finding 已修复，14/14 均具备旧路径、约束变化、状态或控制权、收益与代价、failure mode、source-specific exact-v1 evidence boundary 以及 fallback/coexistence，Books Gate 已通过。

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
| Denominator ID | DEN-20260518-INDEPENDENT-52 |
| Denominator Frozen At | 2026-09-01T21:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-17T09:00:00+08:00 | 2026-05-18T09:00:00+08:00 | 2026-09-01T21:40:00+08:00 | DataCite v2 deterministic snapshot + 324/324 title/abstract replay + official exact-v1 | checked | 324 | SF-2026-ARXIV-2605-17222;SF-2026-ARXIV-2605-17234;SF-2026-ARXIV-2605-17242;SF-2026-ARXIV-2605-17246;SF-2026-ARXIV-2605-17260;SF-2026-ARXIV-2605-17268;SF-2026-ARXIV-2605-17273;SF-2026-ARXIV-2605-17281;SF-2026-ARXIV-2605-17288;SF-2026-ARXIV-2605-17289;SF-2026-ARXIV-2605-17291;SF-2026-ARXIV-2605-17292;SF-2026-ARXIV-2605-17301;SF-2026-ARXIV-2605-17304;SF-2026-ARXIV-2605-17305;SF-2026-ARXIV-2605-17320;SF-2026-ARXIV-2605-17324;SF-2026-ARXIV-2605-17329;SF-2026-ARXIV-2605-17348;SF-2026-ARXIV-2605-17360;SF-2026-ARXIV-2605-17373;SF-2026-ARXIV-2605-17380;SF-2026-ARXIV-2605-17415;SF-2026-ARXIV-2605-17439;SF-2026-ARXIV-2605-17453;SF-2026-ARXIV-2605-17467;SF-2026-ARXIV-2605-17471;SF-2026-ARXIV-2605-17480;SF-2026-ARXIV-2605-17497;SF-2026-ARXIV-2605-17508;SF-2026-ARXIV-2605-17522;SF-2026-ARXIV-2605-17554;SF-2026-ARXIV-2605-17558;SF-2026-ARXIV-2605-17570;SF-2026-ARXIV-2605-17590;SF-2026-ARXIV-2605-17609;SF-2026-ARXIV-2605-17610;SF-2026-ARXIV-2605-17613;SF-2026-ARXIV-2605-17617;SF-2026-ARXIV-2605-17625;SF-2026-ARXIV-2605-17634;SF-2026-ARXIV-2605-17641;SF-2026-ARXIV-2605-17659;SF-2026-ARXIV-2605-17672;SF-2026-ARXIV-2605-17683;SF-2026-ARXIV-2605-17707;SF-2026-ARXIV-2605-17721;SF-2026-ARXIV-2605-18891;SF-2026-ARXIV-2605-18899;SF-2026-ARXIV-2606-20591;SF-2026-ARXIV-2605-23988;SF-2026-ARXIV-2605-23993 | pages=300; final_cursor=end; raw=91841; registered=324; screened=324; retained=52; closure=272 | 2026-05-18T00:59:59Z | screening-ledger-independent-final.json#sha256=1bd0c6036bbb58ea290473e1ff18d73a40ee30395cbdd80d6fe4ac25bf4b4394 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260518:start -->确定性窗口枚举、324/324 语义筛选与非作者 false-positive/false-negative challenge 已闭合。重开 26 项不是把所有 AI 论文扩入分母，而是修正那些改变 workflow/evaluation/security/training/inference state 或 control contract 的漏项；其余 272 项保留 author family-specific closure。<!-- coverage:SRC-ARXIV:20260518:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17222 | arXiv:2605.17222v1 | paper-v1:2605.17222 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17222 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17222 | no |
| SF-2026-ARXIV-2605-17234 | arXiv:2605.17234v1 | paper-v1:2605.17234 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17234 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17234 | no |
| SF-2026-ARXIV-2605-17242 | arXiv:2605.17242v1 | paper-v1:2605.17242 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17242 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17242 | no |
| SF-2026-ARXIV-2605-17246 | arXiv:2605.17246v1 | paper-v1:2605.17246 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17246 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17246 | no |
| SF-2026-ARXIV-2605-17260 | arXiv:2605.17260v1 | paper-v1:2605.17260 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17260 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17260 | no |
| SF-2026-ARXIV-2605-17268 | arXiv:2605.17268v1 | paper-v1:2605.17268 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17268 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17268 | no |
| SF-2026-ARXIV-2605-17273 | arXiv:2605.17273v1 | paper-v1:2605.17273 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17273 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17273 | no |
| SF-2026-ARXIV-2605-17281 | arXiv:2605.17281v1 | paper-v1:2605.17281 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17281 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-17281 | no |
| SF-2026-ARXIV-2605-17288 | arXiv:2605.17288v1 | paper-v1:2605.17288 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17288 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17288 | no |
| SF-2026-ARXIV-2605-17289 | arXiv:2605.17289v1 | paper-v1:2605.17289 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17289 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17289 | no |
| SF-2026-ARXIV-2605-17291 | arXiv:2605.17291v1 | paper-v1:2605.17291 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17291 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17291 | no |
| SF-2026-ARXIV-2605-17292 | arXiv:2605.17292v1 | paper-v1:2605.17292 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17292 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17292 | no |
| SF-2026-ARXIV-2605-17301 | arXiv:2605.17301v1 | paper-v1:2605.17301 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17301 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17301 | no |
| SF-2026-ARXIV-2605-17304 | arXiv:2605.17304v1 | paper-v1:2605.17304 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17304 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17304 | no |
| SF-2026-ARXIV-2605-17305 | arXiv:2605.17305v1 | paper-v1:2605.17305 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17305 | self | — | new_in_window | AGENT-REFLECTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17305 | no |
| SF-2026-ARXIV-2605-17320 | arXiv:2605.17320v1 | paper-v1:2605.17320 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17320 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17320 | no |
| SF-2026-ARXIV-2605-17324 | arXiv:2605.17324v1 | paper-v1:2605.17324 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17324 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17324 | no |
| SF-2026-ARXIV-2605-17329 | arXiv:2605.17329v1 | paper-v1:2605.17329 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17329 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17329 | no |
| SF-2026-ARXIV-2605-17348 | arXiv:2605.17348v1 | paper-v1:2605.17348 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17348 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17348 | no |
| SF-2026-ARXIV-2605-17360 | arXiv:2605.17360v1 | paper-v1:2605.17360 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17360 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-17360 | no |
| SF-2026-ARXIV-2605-17373 | arXiv:2605.17373v1 | paper-v1:2605.17373 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17373 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17373 | no |
| SF-2026-ARXIV-2605-17380 | arXiv:2605.17380v1 | paper-v1:2605.17380 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17380 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17380 | no |
| SF-2026-ARXIV-2605-17415 | arXiv:2605.17415v1 | paper-v1:2605.17415 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17415 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17415 | no |
| SF-2026-ARXIV-2605-17439 | arXiv:2605.17439v1 | paper-v1:2605.17439 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17439 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17439 | no |
| SF-2026-ARXIV-2605-17453 | arXiv:2605.17453v1 | paper-v1:2605.17453 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17453 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17453 | no |
| SF-2026-ARXIV-2605-17467 | arXiv:2605.17467v1 | paper-v1:2605.17467 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17467 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17467 | no |
| SF-2026-ARXIV-2605-17471 | arXiv:2605.17471v1 | paper-v1:2605.17471 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17471 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17471 | no |
| SF-2026-ARXIV-2605-17480 | arXiv:2605.17480v1 | paper-v1:2605.17480 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17480 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17480 | no |
| SF-2026-ARXIV-2605-17497 | arXiv:2605.17497v1 | paper-v1:2605.17497 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17497 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-17497 | no |
| SF-2026-ARXIV-2605-17508 | arXiv:2605.17508v1 | paper-v1:2605.17508 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17508 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17508 | no |
| SF-2026-ARXIV-2605-17522 | arXiv:2605.17522v1 | paper-v1:2605.17522 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17522 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17522 | no |
| SF-2026-ARXIV-2605-17554 | arXiv:2605.17554v1 | paper-v1:2605.17554 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17554 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17554 | no |
| SF-2026-ARXIV-2605-17558 | arXiv:2605.17558v1 | paper-v1:2605.17558 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17558 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17558 | no |
| SF-2026-ARXIV-2605-17570 | arXiv:2605.17570v1 | paper-v1:2605.17570 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17570 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2605-17570 | no |
| SF-2026-ARXIV-2605-17590 | arXiv:2605.17590v1 | paper-v1:2605.17590 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17590 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-17590 | no |
| SF-2026-ARXIV-2605-17609 | arXiv:2605.17609v1 | paper-v1:2605.17609 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17609 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17609 | no |
| SF-2026-ARXIV-2605-17610 | arXiv:2605.17610v1 | paper-v1:2605.17610 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17610 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17610 | no |
| SF-2026-ARXIV-2605-17613 | arXiv:2605.17613v1 | paper-v1:2605.17613 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17613 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-17613 | no |
| SF-2026-ARXIV-2605-17617 | arXiv:2605.17617v1 | paper-v1:2605.17617 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17617 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17617 | no |
| SF-2026-ARXIV-2605-17625 | arXiv:2605.17625v1 | paper-v1:2605.17625 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17625 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17625 | no |
| SF-2026-ARXIV-2605-17634 | arXiv:2605.17634v1 | paper-v1:2605.17634 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17634 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17634 | no |
| SF-2026-ARXIV-2605-17641 | arXiv:2605.17641v1 | paper-v1:2605.17641 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17641 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17641 | no |
| SF-2026-ARXIV-2605-17659 | arXiv:2605.17659v1 | paper-v1:2605.17659 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17659 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-17659 | no |
| SF-2026-ARXIV-2605-17672 | arXiv:2605.17672v1 | paper-v1:2605.17672 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17672 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17672 | no |
| SF-2026-ARXIV-2605-17683 | arXiv:2605.17683v1 | paper-v1:2605.17683 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17683 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17683 | no |
| SF-2026-ARXIV-2605-17707 | arXiv:2605.17707v1 | paper-v1:2605.17707 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17707 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-17707 | no |
| SF-2026-ARXIV-2605-17721 | arXiv:2605.17721v1 | paper-v1:2605.17721 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17721 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17721 | no |
| SF-2026-ARXIV-2605-18891 | arXiv:2605.18891v1 | paper-v1:2605.18891 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18891 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2605-18891 | no |
| SF-2026-ARXIV-2605-18899 | arXiv:2605.18899v1 | paper-v1:2605.18899 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18899 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 | no |
| SF-2026-ARXIV-2606-20591 | arXiv:2606.20591v1 | paper-v1:2606.20591 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2606-20591 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-20591 | no |
| SF-2026-ARXIV-2605-23988 | arXiv:2605.23988v1 | paper-v1:2605.23988 | 2026-W20 | 2026-05-17 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23988 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-23988 | no |
| SF-2026-ARXIV-2605-23993 | arXiv:2605.23993v1 | paper-v1:2605.23993 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23993 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23993 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17222 | RP-2def8a53e65eb02b | deep | arXiv:2605.17222v1 | SRC-ARXIV@arXiv:2605.17222v1 | arXiv:2605.17222v1 — §II-B BSGS Algorithm for HE-LT (frozen exact-v1 official HTML receipt) | arXiv:2605.17222v1 — §VI Experimental Results and Comparisons (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17222v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17222 | complete |
| SF-2026-ARXIV-2605-17234 | RP-d0a4bdd64998e0c6 | deep | arXiv:2605.17234v1 | SRC-ARXIV@arXiv:2605.17234v1 | arXiv:2605.17234v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17234v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17234v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17234 | complete |
| SF-2026-ARXIV-2605-17242 | RP-7407c464354ff140 | deep | arXiv:2605.17242v1 | SRC-ARXIV@arXiv:2605.17242v1 | arXiv:2605.17242v1 — §3 Methodology (§3.1–§3.4) (official exact-v1 HTML) | arXiv:2605.17242v1 — §4 Experimental Setup; §5 Results (official exact-v1 HTML) | arXiv:2605.17242v1 — §6.4 Threats to Validity (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17242v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17242 | complete |
| SF-2026-ARXIV-2605-17246 | RP-42c4c7936b115319 | deep | arXiv:2605.17246v1 | SRC-ARXIV@arXiv:2605.17246v1 | arXiv:2605.17246v1 — §3 The Behavioural Alignment Framework (frozen exact-v1 official HTML receipt) | arXiv:2605.17246v1 — §5 Empirical Evaluation on CardDemo (frozen exact-v1 official HTML receipt) | arXiv:2605.17246v1 — §6 Discussion and limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17246v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17246 | complete |
| SF-2026-ARXIV-2605-17260 | RP-e0ee173099242c7b | deep | arXiv:2605.17260v1 | SRC-ARXIV@arXiv:2605.17260v1 | arXiv:2605.17260v1 — §4.1 Architecture: Spatio-temporal Token Compressive Encoding (frozen exact-v1 official HTML receipt) | arXiv:2605.17260v1 — §5 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-a.txt#sha256=f5074c159bee3cbb728f67926c05f4e6ef651304d936baea943e38a9e4ffabeb; exact-v1 URL=https://arxiv.org/html/2605.17260v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17260 | complete |
| SF-2026-ARXIV-2605-17268 | RP-9e5be2bb668ee336 | deep | arXiv:2605.17268v1 | SRC-ARXIV@arXiv:2605.17268v1 | arXiv:2605.17268v1 — §4 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17268v1 — §5 Results (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17268v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17268 | complete |
| SF-2026-ARXIV-2605-17273 | RP-0e9c0f295ed9bcc7 | deep | arXiv:2605.17273v1 | SRC-ARXIV@arXiv:2605.17273v1 | arXiv:2605.17273v1 — §2.1 Statistical Comparison Methods (frozen exact-v1 official HTML receipt) | arXiv:2605.17273v1 — §4.1 Case Analysis: HELM MMLU (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17273v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17273 | complete |
| SF-2026-ARXIV-2605-17281 | RP-4b09b99c431cf845 | deep | arXiv:2605.17281v1 | SRC-ARXIV@arXiv:2605.17281v1 | arXiv:2605.17281v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17281v1 — §3.2 Evaluation Protocol (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17281v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17281 | complete |
| SF-2026-ARXIV-2605-17288 | RP-49ea30f3df91eee1 | deep | arXiv:2605.17288v1 | SRC-ARXIV@arXiv:2605.17288v1 | arXiv:2605.17288v1 — §3.2 System Model (frozen exact-v1 official HTML receipt) | arXiv:2605.17288v1 — §6 Experiment (frozen exact-v1 official HTML receipt) | arXiv:2605.17288v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-b.txt#sha256=0e855f40ad6257ba4a7e7c30bfbc192a95d80b5cda955f812a4716ed51dfc56e; exact-v1 URL=https://arxiv.org/html/2605.17288v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17288 | complete |
| SF-2026-ARXIV-2605-17289 | RP-dd9f7024fd489d32 | deep | arXiv:2605.17289v1 | SRC-ARXIV@arXiv:2605.17289v1 | arXiv:2605.17289v1 — §3 LEAP: Method (frozen exact-v1 official HTML receipt) | arXiv:2605.17289v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | arXiv:2605.17289v1 — §5 Discussion and Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17289v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17289 | complete |
| SF-2026-ARXIV-2605-17291 | RP-116f75c7a0506fff | deep | arXiv:2605.17291v1 | SRC-ARXIV@arXiv:2605.17291v1 | arXiv:2605.17291v1 — §3 Method (frozen exact-v1 official HTML receipt) | arXiv:2605.17291v1 — §2.2 Rubric-Based Evaluation and Rewards (frozen exact-v1 official HTML receipt) | arXiv:2605.17291v1 — §6 Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17291v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17291 | complete |
| SF-2026-ARXIV-2605-17292 | RP-fb7a352115fdd929 | deep | arXiv:2605.17292v1 | SRC-ARXIV@arXiv:2605.17292v1 | arXiv:2605.17292v1 — §III MetaCogAgent Framework (§III-B–§III-D) (official exact-v1 HTML) | arXiv:2605.17292v1 — §V Experiments (official exact-v1 HTML) | arXiv:2605.17292v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17292v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17292 | complete |
| SF-2026-ARXIV-2605-17301 | RP-300748087f71a17d | deep | arXiv:2605.17301v1 | SRC-ARXIV@arXiv:2605.17301v1 | arXiv:2605.17301v1 — §III Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17301v1 — §IV Experimental Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17301v1 — §V-G Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17301v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17301 | complete |
| SF-2026-ARXIV-2605-17304 | RP-129af85d7881f49c | deep | arXiv:2605.17304v1 | SRC-ARXIV@arXiv:2605.17304v1 | arXiv:2605.17304v1 — §3 Problem Formulation (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-c.txt#sha256=5266e2523e5fbffa0991a5fdfcb698f84c0fca6f4509734861dea2378293b440; exact-v1 URL=https://arxiv.org/html/2605.17304v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17304 | complete |
| SF-2026-ARXIV-2605-17305 | RP-69003ea762f0c911 | deep | arXiv:2605.17305v1 | SRC-ARXIV@arXiv:2605.17305v1 | arXiv:2605.17305v1 — §III CyberCorrect Framework (§III-B–§III-D) (official exact-v1 HTML) | arXiv:2605.17305v1 — §V Experiments (official exact-v1 HTML) | arXiv:2605.17305v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17305v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17305 | complete |
| SF-2026-ARXIV-2605-17320 | RP-d50b23a3e16d22b5 | deep | arXiv:2605.17320v1 | SRC-ARXIV@arXiv:2605.17320v1 | arXiv:2605.17320v1 — §4 TClone Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17320v1 — §5 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17320v1 — §2.3 Limitations of Existing Solutions (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17320v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17320 | complete |
| SF-2026-ARXIV-2605-17324 | RP-7b6430846ac5a3dc | deep | arXiv:2605.17324v1 | SRC-ARXIV@arXiv:2605.17324v1 | arXiv:2605.17324v1 — §5.1 Evaluation Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17324v1 — §5 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17324v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17324v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17324 | complete |
| SF-2026-ARXIV-2605-17329 | RP-8d1934bd28977f9c | deep | arXiv:2605.17329v1 | SRC-ARXIV@arXiv:2605.17329v1 | arXiv:2605.17329v1 — §4 Method (§4.2–§4.6) (official exact-v1 HTML) | arXiv:2605.17329v1 — §5 Main Results; §6 Ablation (official exact-v1 HTML) | arXiv:2605.17329v1 — Appendix D Limitations and Broader Impacts (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17329v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17329 | complete |
| SF-2026-ARXIV-2605-17348 | RP-de1353951694879a | deep | arXiv:2605.17348v1 | SRC-ARXIV@arXiv:2605.17348v1 | arXiv:2605.17348v1 — §4 Methodology (§4.2–§4.3) (official exact-v1 HTML) | arXiv:2605.17348v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17348v1 — §6 Conclusion and robustness appendix; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17348v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17348 | complete |
| SF-2026-ARXIV-2605-17360 | RP-aecc7d038ca36b79 | deep | arXiv:2605.17360v1 | SRC-ARXIV@arXiv:2605.17360v1 | arXiv:2605.17360v1 — §3 Omni-DuplexEval (§3.2–§3.3) (official exact-v1 HTML) | arXiv:2605.17360v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17360v1 — Appendix D Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17360v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17360 | complete |
| SF-2026-ARXIV-2605-17373 | RP-49302d50a914dfa1 | deep | arXiv:2605.17373v1 | SRC-ARXIV@arXiv:2605.17373v1 | arXiv:2605.17373v1 — §3 FML-bench (§3.2–§3.4) (official exact-v1 HTML) | arXiv:2605.17373v1 — §4 Experiments; §5 Search-dynamics analysis (official exact-v1 HTML) | arXiv:2605.17373v1 — Appendix N Broader impacts; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17373v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17373 | complete |
| SF-2026-ARXIV-2605-17380 | RP-4579206d5622b075 | deep | arXiv:2605.17380v1 | SRC-ARXIV@arXiv:2605.17380v1 | arXiv:2605.17380v1 — §3 ADR System Design (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17380v1 — §5 Evaluation; §6 Real-World Deployment (official exact-v1 HTML) | arXiv:2605.17380v1 — §7 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17380v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17380 | complete |
| SF-2026-ARXIV-2605-17415 | RP-392968683dd732a5 | deep | arXiv:2605.17415v1 | SRC-ARXIV@arXiv:2605.17415v1 | arXiv:2605.17415v1 — §3 IVF-TQ (§3.1–§3.3) (official exact-v1 HTML) | arXiv:2605.17415v1 — §4 Streaming Experiments; §5 Million-Scale Evaluation (official exact-v1 HTML) | arXiv:2605.17415v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17415v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17415 | complete |
| SF-2026-ARXIV-2605-17439 | RP-74eebdfcbfd4cd12 | deep | arXiv:2605.17439v1 | SRC-ARXIV@arXiv:2605.17439v1 | arXiv:2605.17439v1 — §4 DiagEval (§4.1–§4.4) (official exact-v1 HTML) | arXiv:2605.17439v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17439v1 — §6 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17439v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17439 | complete |
| SF-2026-ARXIV-2605-17453 | RP-2957f8febb15b9b1 | deep | arXiv:2605.17453v1 | SRC-ARXIV@arXiv:2605.17453v1 | arXiv:2605.17453v1 — §3 Method: VISTA-Guard under Untrusted Tool Feedback (frozen exact-v1 official HTML receipt) | arXiv:2605.17453v1 — §2 Threat Model, Benchmark, and Evaluation Lens (frozen exact-v1 official HTML receipt) | arXiv:2605.17453v1 — §5 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17453v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17453 | complete |
| SF-2026-ARXIV-2605-17467 | RP-d0c2dd1a542fab26 | deep | arXiv:2605.17467v1 | SRC-ARXIV@arXiv:2605.17467v1 | arXiv:2605.17467v1 — §3 VerifyMAS (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17467v1 — §4 Main Experiments (official exact-v1 HTML) | arXiv:2605.17467v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17467v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17467 | complete |
| SF-2026-ARXIV-2605-17471 | RP-a4a77dd56fd5f14c | deep | arXiv:2605.17471v1 | SRC-ARXIV@arXiv:2605.17471v1 | arXiv:2605.17471v1 — §3 Our Approach (§3.1–§3.2) (official exact-v1 HTML) | arXiv:2605.17471v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17471v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17471v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17471 | complete |
| SF-2026-ARXIV-2605-17480 | RP-292df48dad510acb | deep | arXiv:2605.17480v1 | SRC-ARXIV@arXiv:2605.17480v1 | arXiv:2605.17480v1 — §3 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17480v1 — §4 Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17480v1 — §6 Limitations (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-d.txt#sha256=420494531f6942665b1f3de8dd395e22d8d5ba1f4d5a8f68eaaabc8e364847fe; exact-v1 URL=https://arxiv.org/html/2605.17480v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17480 | complete |
| SF-2026-ARXIV-2605-17497 | RP-c90245d0a1481fe3 | deep | arXiv:2605.17497v1 | SRC-ARXIV@arXiv:2605.17497v1 | arXiv:2605.17497v1 — §3 Self-Supervised On-Policy Distillation (official exact-v1 HTML) | arXiv:2605.17497v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17497v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17497v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17497 | complete |
| SF-2026-ARXIV-2605-17508 | RP-58b7bdadd08a1df1 | deep | arXiv:2605.17508v1 | SRC-ARXIV@arXiv:2605.17508v1 | arXiv:2605.17508v1 — §4 Methodology (official exact-v1 HTML) | arXiv:2605.17508v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17508v1 — §6 Discussion (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17508v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17508 | complete |
| SF-2026-ARXIV-2605-17522 | RP-6bc13b2fc4831772 | deep | arXiv:2605.17522v1 | SRC-ARXIV@arXiv:2605.17522v1 | arXiv:2605.17522v1 — §3 Methodology (§3.2–§3.4) (official exact-v1 HTML) | arXiv:2605.17522v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17522v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17522v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17522 | complete |
| SF-2026-ARXIV-2605-17554 | RP-8fd81b6c2deb1a72 | deep | arXiv:2605.17554v1 | SRC-ARXIV@arXiv:2605.17554v1 | arXiv:2605.17554v1 — §3 Benchmark Design (§3.3–§3.4) (official exact-v1 HTML) | arXiv:2605.17554v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.17554v1 — §5 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17554v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17554 | complete |
| SF-2026-ARXIV-2605-17558 | RP-4e90e6a30316ee3c | deep | arXiv:2605.17558v1 | SRC-ARXIV@arXiv:2605.17558v1 | arXiv:2605.17558v1 — §3 Method (§3.1–§3.3) (official exact-v1 HTML) | arXiv:2605.17558v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17558v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17558v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17558 | complete |
| SF-2026-ARXIV-2605-17570 | RP-50aa0ee32143c72b | deep | arXiv:2605.17570v1 | SRC-ARXIV@arXiv:2605.17570v1 | arXiv:2605.17570v1 — §3 Diagnosing rollout staleness; §4 μ-GRPO (official exact-v1 HTML) | arXiv:2605.17570v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17570v1 — §6 Discussion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17570v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17570 | complete |
| SF-2026-ARXIV-2605-17590 | RP-ea7dfb0b951aa8b6 | deep | arXiv:2605.17590v1 | SRC-ARXIV@arXiv:2605.17590v1 | arXiv:2605.17590v1 — §4 Problem Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17590v1 — §5 Theoretical Results (frozen exact-v1 official HTML receipt) | arXiv:2605.17590v1 — §7 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17590v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17590 | complete |
| SF-2026-ARXIV-2605-17609 | RP-1f65541b4be860cd | deep | arXiv:2605.17609v1 | SRC-ARXIV@arXiv:2605.17609v1 | arXiv:2605.17609v1 — §4 ADAP Adaptive Policy (official exact-v1 HTML) | arXiv:2605.17609v1 — §5 Experiments (official exact-v1 HTML) | arXiv:2605.17609v1 — §7 Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17609v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17609 | complete |
| SF-2026-ARXIV-2605-17610 | RP-c880c7a672f66557 | deep | arXiv:2605.17610v1 | SRC-ARXIV@arXiv:2605.17610v1 | arXiv:2605.17610v1 — §4 Data Curation; §5 SafeLens (official exact-v1 HTML) | arXiv:2605.17610v1 — §6 Experiments (official exact-v1 HTML) | arXiv:2605.17610v1 — Appendix A Limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17610v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17610 | complete |
| SF-2026-ARXIV-2605-17613 | RP-27371fd8358ec6cf | deep | arXiv:2605.17613v1 | SRC-ARXIV@arXiv:2605.17613v1 | arXiv:2605.17613v1 — §3 Motivation: Why Lossy KV Methods Fail (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17613v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17613 | complete |
| SF-2026-ARXIV-2605-17617 | RP-1873e52a02c202e2 | deep | arXiv:2605.17617v1 | SRC-ARXIV@arXiv:2605.17617v1 | arXiv:2605.17617v1 — §3 Offline Workflow Graph; §4 Online Traversal; §5 Reinforcement (official exact-v1 HTML) | arXiv:2605.17617v1 — §6 Evaluation; §7 Production Deployment (official exact-v1 HTML) | arXiv:2605.17617v1 — §8 Discussion (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17617v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17617 | complete |
| SF-2026-ARXIV-2605-17625 | RP-fd0bb5cfe38cb552 | deep | arXiv:2605.17625v1 | SRC-ARXIV@arXiv:2605.17625v1 | arXiv:2605.17625v1 — §3 Dual-Process Memory Architecture; §3.2 Episodic Window; §3.3 Semantic Consolidation (official exact-v1 HTML) | arXiv:2605.17625v1 — §4 Experimental Design; §5 Results (official exact-v1 HTML) | arXiv:2605.17625v1 — §6 Discussion and limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17625v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17625 | complete |
| SF-2026-ARXIV-2605-17634 | RP-541d3dd31d65f8f0 | deep | arXiv:2605.17634v1 | SRC-ARXIV@arXiv:2605.17634v1 | arXiv:2605.17634v1 — §1 Introduction (frozen exact-v1 official HTML receipt) | arXiv:2605.17634v1 — §5.1 Attacking Context Parameters Inference and Norm Evaluation (frozen exact-v1 official HTML receipt) | arXiv:2605.17634v1 — §3 Limitations of Current Views on Prompt Injection (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17634v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17634 | complete |
| SF-2026-ARXIV-2605-17641 | RP-850eed6256cef4eb | deep | arXiv:2605.17641v1 | SRC-ARXIV@arXiv:2605.17641v1 | arXiv:2605.17641v1 — §3 Proposed Framework (frozen exact-v1 official HTML receipt) | arXiv:2605.17641v1 — §5 Experimental Setup (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-e.txt#sha256=1e15947a8136d8f1b1232dcfbe26d6079e3ebda4c1eeefa746a92fa7918ad8f5; exact-v1 URL=https://arxiv.org/html/2605.17641v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17641 | complete |
| SF-2026-ARXIV-2605-17659 | RP-636ba38b321ddb96 | deep | arXiv:2605.17659v1 | SRC-ARXIV@arXiv:2605.17659v1 | arXiv:2605.17659v1 — §1 Formal Illustration of Negative Weight Drift (frozen exact-v1 official HTML receipt) | arXiv:2605.17659v1 — §2 Empirical Results for Negative Weight Drift (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17659v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17659 | complete |
| SF-2026-ARXIV-2605-17672 | RP-c7e5999b05d0e91b | deep | arXiv:2605.17672v1 | SRC-ARXIV@arXiv:2605.17672v1 | arXiv:2605.17672v1 — §3 Methodology (frozen exact-v1 official HTML receipt) | arXiv:2605.17672v1 — §4 Experimental Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17672v1 — §6 Analysis and Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17672v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17672 | complete |
| SF-2026-ARXIV-2605-17683 | RP-bea65cf30fc02aa6 | deep | arXiv:2605.17683v1 | SRC-ARXIV@arXiv:2605.17683v1 | arXiv:2605.17683v1 — §4 μ-ORCA Architecture and Implementation; §5 Performance Model and Design-Space Exploration (official exact-v1 HTML) | arXiv:2605.17683v1 — §6 Evaluation (official exact-v1 HTML) | arXiv:2605.17683v1 — §7 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.17683v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17683 | complete |
| SF-2026-ARXIV-2605-17707 | RP-e51ce4b248dde7df | deep | arXiv:2605.17707v1 | SRC-ARXIV@arXiv:2605.17707v1 | arXiv:2605.17707v1 — §VIII-B () Setup (frozen exact-v1 official HTML receipt) | arXiv:2605.17707v1 — §VIII-D2 Results (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17707v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17707 | complete |
| SF-2026-ARXIV-2605-17721 | RP-4178bdceb2bc8b46 | deep | arXiv:2605.17721v1 | SRC-ARXIV@arXiv:2605.17721v1 | arXiv:2605.17721v1 — §2 Experience Graph Design (frozen exact-v1 official HTML receipt) | arXiv:2605.17721v1 — §4 Experiments (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-f.txt#sha256=25ee65e984dcd51bcaa12e55ddab1afb3634d8c37ee61aeb21b4ed08e72bec0b; exact-v1 URL=https://arxiv.org/html/2605.17721v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-17721 | complete |
| SF-2026-ARXIV-2605-18891 | RP-95ea8bc96626981c | deep | arXiv:2605.18891v1 | SRC-ARXIV@arXiv:2605.18891v1 | arXiv:2605.18891v1 — §3 Setup and the Bypass Metric (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §4 Results (frozen exact-v1 official HTML receipt) | arXiv:2605.18891v1 — §5 Discussion (frozen exact-v1 official HTML receipt) | papers/2026/05/_sources/daily-20260518/exact-review-batch-g.txt#sha256=804cad573138683e86544b653813a5ca64961d7fe4c52ed742315b9a7f54ce63; exact-v1 URL=https://arxiv.org/html/2605.18891v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18891 | complete |
| SF-2026-ARXIV-2605-18899 | RP-de7028b2b7ed378a | deep | arXiv:2605.18899v1 | SRC-ARXIV@arXiv:2605.18899v1 | arXiv:2605.18899v1 — §3 Anchored Bandit Policy Optimization (official exact-v1 HTML) | arXiv:2605.18899v1 — §4 Experiments (official exact-v1 HTML) | arXiv:2605.18899v1 — Appendix E.4 Scope limitations (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.18899v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-18899 | complete |
| SF-2026-ARXIV-2606-20591 | RP-d231c73c30e3afc6 | deep | arXiv:2606.20591v1 | SRC-ARXIV@arXiv:2606.20591v1 | arXiv:2606.20591v1 — §III System Model and Problem Formulation (frozen exact-v1 official HTML receipt) | arXiv:2606.20591v1 — §IV Theoretical Results (frozen exact-v1 official HTML receipt) | Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup | papers/2026/05/_sources/daily-20260518/exact-review-batch-g.txt#sha256=804cad573138683e86544b653813a5ca64961d7fe4c52ed742315b9a7f54ce63; exact-v1 URL=https://arxiv.org/html/2606.20591v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2606-20591 | complete |
| SF-2026-ARXIV-2605-23988 | RP-fc4f8fb00f24ce39 | deep | arXiv:2605.23988v1 | SRC-ARXIV@arXiv:2605.23988v1 | arXiv:2605.23988v1 — §II Architecture and Workflow; §III Token Compression (official exact-v1 HTML) | arXiv:2605.23988v1 — §VI Experiments (official exact-v1 HTML) | arXiv:2605.23988v1 — §VII Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.23988v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23988 | complete |
| SF-2026-ARXIV-2605-23993 | RP-2aa525f1ee506fca | deep | arXiv:2605.23993v1 | SRC-ARXIV@arXiv:2605.23993v1 | arXiv:2605.23993v1 — §3 Diffusion-Forcing Interface and Experimental Substrate (official exact-v1 HTML) | arXiv:2605.23993v1 — §4 Findings (official exact-v1 HTML) | arXiv:2605.23993v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML) | exact-v1 URL=https://arxiv.org/html/2605.23993v1; immutable code commit Not Disclosed | claim:SF-2026-ARXIV-2605-23993 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-17222:start -->
#### Triple-Hoisted Baby-Step Giant-Step Linear Transformation over CKKS Homomorphic Encryption and Hardware Accelerator

问题与 changed constraint：CKKS 线性变换把 rotation 数量、off-chip traffic 与 FPGA permutation/data-path 共同暴露为隐私推理的硬件执行合同；收益不等于通用 GPU/模型加速。

机制与 ownership：Computations can be directly carried out over ciphertexts using homomorphic encryption (HE), which is indispensable for privacy-preserving cloud computing. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17222v1 — §II-B BSGS Algorithm for HE-LT (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17222v1 — §VI Experimental Results and Comparisons (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17222:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17222:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17222:end -->

<!-- review:SF-2026-ARXIV-2605-17234:start -->
#### Active Budget Allocation for Efficient Scaling Law Estimation via Surrogate-Guided Pruning

问题与 changed constraint：Scaling-law 实验预算从均匀采样演进为 successive-halving 与 surrogate-guided pruning；节省拟合成本的同时引入错误早停与 surrogate selection bias。

机制与 ownership：In addition to enabling a more systematic allocation of a given compute budget, our findings show that SH paired with surrogate models yields a set of learning curves that includes one with a lower loss-compute value than what naive uniform allocation or an SH-only approach can obtain. owner=`WORLDVIEW-SCALING-LAW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17234v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17234v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17234:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17234:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17234:end -->

<!-- review:SF-2026-ARXIV-2605-17242:start -->
#### From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements

问题与 changed constraint：acceptance tests become pre-execution workflow state; browser-observed failures become typed repair evidence rather than terminal text

机制与 ownership：We present TDDev, a framework that automates this closed loop through three stages: (1) converting high-level requirements into structured acceptance tests before any code is written, (2) deploying the application and validating it through browser-based interaction simulation, and (3) translating browser-observed failures into structured repair reports for the coding agent. owner=`AGENT-WORKFLOW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17242v1 — §3 Methodology (§3.1–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17242v1 — §4 Experimental Setup; §5 Results (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17242v1 — §6.4 Threats to Validity (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17242:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17242:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17242:end -->

<!-- review:SF-2026-ARXIV-2605-17246:start -->
#### Fidelity Probes for Specification--Code Alignment

问题与 changed constraint：Specification–code alignment 由单一测试通过率扩展为 code-grounded fidelity probes、contradiction/coverage-gap 分解和 frozen held-out resampling；probe generator 仍不是完整语义 oracle。

机制与 ownership：We introduce fidelity probes: natural-language questions generated from a reference artifact with code-derived ground-truth answers, answered from a candidate specification. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17246v1 — §3 The Behavioural Alignment Framework (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17246v1 — §5 Empirical Evaluation on CardDemo (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17246v1 — §6 Discussion and limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17246:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17246:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17246:end -->

<!-- review:SF-2026-ARXIV-2605-17260:start -->
#### LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs

问题与 changed constraint：post-hoc visual-token reduction 会把瓶颈推回逐帧 vision encoder；compressed-token distillation 让 encoder 直接生成时空压缩表示，交换 teacher 成本、表示偏差和 frame coverage。

机制与 ownership：To address this, we introduce LiteFrame, a strong, yet highly efficient video encoder backbone for Video LLMs. owner=`MULTIMODAL-REPRESENTATION`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17260v1 — §4.1 Architecture: Spatio-temporal Token Compressive Encoding (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17260v1 — §5 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17260:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17260:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17260:end -->

<!-- review:SF-2026-ARXIV-2605-17268:start -->
#### Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving Models

问题与 changed constraint：VLA 的自然语言 rationale 不能取得 trajectory safety authority；reasoning fidelity、entity/action consistency 与视觉扰动稳定性必须成为独立传感器并由安全控制器提交动作。

机制与 ownership：We present the first systematic study of faithfulness in Vision-Language-Action (VLA) driving models, analyzing 300 Alpamayo-R1-10B inferences across 100 diverse PhysicalAI-AV scenarios. owner=`MULTIMODAL-EMBODIED-VLA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17268v1 — §4 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17268v1 — §5 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17268:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17268:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17268:end -->

<!-- review:SF-2026-ARXIV-2605-17273:start -->
#### Position: State-of-the-Art Claims Require State-of-the-Art Evidence

问题与 changed constraint：SOTA claim 需要 effect size、consistency、uncertainty 与 task-level superiority 证据，平均分第一只证明 aggregate ranking，不证明广泛优越。

机制与 ownership：This requires no additional experiments, only honest reporting of what results actually show, enabling more precise and interpretable comparisons across models. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17273v1 — §2.1 Statistical Comparison Methods (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17273v1 — §4.1 Case Analysis: HELM MMLU (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17273:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17273:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17273:end -->

<!-- review:SF-2026-ARXIV-2605-17281:start -->
#### ContractBench: Can LLM Agents Preserve Observation Contracts?

问题与 changed constraint：工具 observation 中的 presigned URL、session token 与 OAuth state 是带 byte-integrity 和 expiry 的 contract；模型只能传递，不能自由改写或延迟复用。

机制与 ownership：We show that observation contract compliance (preserving the temporal validity and byte-level integrity) is an emergent, regression-prone capability: it is neither guaranteed by general tool-use ability nor consistently improved by larger or newer models. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17281v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17281v1 — §3.2 Evaluation Protocol (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17281:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17281:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17281:end -->

<!-- review:SF-2026-ARXIV-2605-17288:start -->
#### When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack

问题与 changed constraint：模型 cascade 的轻量 front-end 与 escalation controller 扩大攻击面；攻击可同时破坏质量和成本目标，因此 route/admission 需绑定 adversarial evidence 与保守 fallback。

机制与 ownership：In this work, we present the first study demonstrating that LLM cascade systems are susceptible to targeted adversarial manipulation, which disrupts both performance objectives and the intended cost advantages of the cascade design. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17288v1 — §3.2 System Model (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17288v1 — §6 Experiment (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17288v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17288:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17288:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17288:end -->

<!-- review:SF-2026-ARXIV-2605-17289:start -->
#### LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models

问题与 changed constraint：端到端 unstructured mask learning 把 pruning owner 从 layer-wise surrogate 移到全局 mask objective，但一次性 H100 训练成本和 kernel compatibility 不等于部署 speedup。

机制与 ownership：End-to-end alternatives such as MaskLLM and PATCH show that learnable masks can close this gap, but their categorical-over-patterns parameterization scales with the number of valid masks per row and does not port to the unstructured setting. owner=`INFER-TENSORRT-LLM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17289v1 — §3 LEAP: Method (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17289v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17289v1 — §5 Discussion and Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17289:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17289:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17289:end -->

<!-- review:SF-2026-ARXIV-2605-17291:start -->
#### Step-wise Rubric Rewards for LLM Reasoning

问题与 changed constraint：final-answer reward 对中间步骤产生错误 credit；step-wise rubric attribution/normalization 改变 gradient ownership，但依赖 judge 与显式 step boundary。

机制与 ownership：Rubric-based methods such as Rubrics as Rewards (RaR) introduce finer-grained supervision by scoring rollouts against structured criteria, yet the rubric scores are still aggregated into a single scalar applied to the entire response, causing three weaknesses: loss of multi-criterion structure, uniform supervision of correct and incorrect steps, and reward hacking through unbounded self-correction. owner=`TRAIN-RLHF`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17291v1 — §3 Method (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17291v1 — §2.2 Rubric-Based Evaluation and Rewards (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17291v1 — §6 Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17291:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17291:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17291:end -->

<!-- review:SF-2026-ARXIV-2605-17292:start -->
#### MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation

问题与 changed constraint：delegation consumes a capability profile and confidence sensor, but self-reported confidence cannot own commit authority

机制与 ownership：Inspired by metacognition theory from cognitive science, we propose MetaCogAgent, a multi-agent LLM framework where each agent is equipped with a Metacognitive Self-Assessment Unit that evaluates task-capability alignment before execution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17292v1 — §III MetaCogAgent Framework (§III-B–§III-D) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17292v1 — §V Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17292v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17292:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17292:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17292:end -->

<!-- review:SF-2026-ARXIV-2605-17301:start -->
#### ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retrieval Augmented Generation

问题与 changed constraint：RAG 在生成前显式检测、分类并解决 retrieved-source conflict；source credibility 与 temporal/opinion policy 变成可审计状态，但 LLM judge 与合成冲突数据限制外推。

机制与 ownership：We present ConflictRAG, a conflict-aware RAG framework that detects, classifies, and resolves knowledge conflicts prior to answer generation. owner=`AGENT-RAG`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17301v1 — §III Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17301v1 — §IV Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17301v1 — §V-G Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17301:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17301:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17301:end -->

<!-- review:SF-2026-ARXIV-2605-17304:start -->
#### Compress the Context, Keep the Commitments: A Formal Framework for Verifiable LLM Context Compression

问题与 changed constraint：Context compression 的对象从 token 变为 typed, source-grounded commitment atoms；压缩必须验证 critical recall、conflict/equivalence 与 recoverability，并在不确定时回退 raw spans/更大 context。

机制与 ownership：We propose Context Codec, a commitment-level framework for compressing prompts and chat histories. owner=`AGENT-CONTEXT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17304v1 — §3 Problem Formulation (frozen exact-v1 official HTML receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17304:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17304:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17304:end -->

<!-- review:SF-2026-ARXIV-2605-17305:start -->
#### CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models

问题与 changed constraint：self-correction is represented as detector-controller-stop state with overshoot and oscillation, not an unbounded retry loop

机制与 ownership：We propose CyberCorrect, a framework that formalizes LLM self-correction as a closed-loop control system grounded in cybernetic theory. owner=`AGENT-REFLECTION`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17305v1 — §III CyberCorrect Framework (§III-B–§III-D) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17305v1 — §V Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17305v1 — §VI Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17305:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17305:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17305:end -->

<!-- review:SF-2026-ARXIV-2605-17320:start -->
#### TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents

问题与 changed constraint：Computer-use workspace 从一次性 sandbox 演进为 live save/fork/rollback/selective-commit；低延迟 branch 与 durable checkpoint 分权，同时引入 credential、GUI、external side-effect merge 边界。

机制与 ownership：We present TClone, a forkable personal workspace system for computer-use agents. owner=`AGENT-PLATFORM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17320v1 — §4 TClone Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17320v1 — §5 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17320v1 — §2.3 Limitations of Existing Solutions (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17320:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17320:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17320:end -->

<!-- review:SF-2026-ARXIV-2605-17324:start -->
#### ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents

问题与 changed constraint：Clarification 是独立 agent state transition，可能把 prompt injection 从 tool-return path 扩展到后续 user-input path；clarify 不能自动提升输入 authority。

机制与 ownership：We introduce ASPI (Ambiguous-State Prompt Injection), a benchmark of 728 task-attack scenarios that isolates clarification as a distinct agent state and measures how this state transition affects vulnerability under controlled conditions. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17324v1 — §5.1 Evaluation Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17324v1 — §5 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17324v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17324:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17324:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17324:end -->

<!-- review:SF-2026-ARXIV-2605-17329:start -->
#### LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails

问题与 changed constraint：dynamic policy clauses are inference-time guardrail state; latent compression saves latency but remains a fallible sensor

机制与 ownership：We introduce Latent Policy Guardrail (LPG), a guardrail framework that learnssemantic latent deliberation over dynamic policies. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17329v1 — §4 Method (§4.2–§4.6) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17329v1 — §5 Main Results; §6 Ablation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17329v1 — Appendix D Limitations and Broader Impacts (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17329:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17329:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17329:end -->

<!-- review:SF-2026-ARXIV-2605-17348:start -->
#### Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution

问题与 changed constraint：Active/Standby/Terminated is a recoverable agent lifecycle that avoids irreversible pruning after one bad round

机制与 ownership：In this paper, we propose AgentRevive, a Markov state-aware framework for resilient multi-agent evolution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17348v1 — §4 Methodology (§4.2–§4.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17348v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17348v1 — §6 Conclusion and robustness appendix; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17348:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17348:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17348:end -->

<!-- review:SF-2026-ARXIV-2605-17360:start -->
#### Omni-DuplexEval: Evaluating Real-time Duplex Omni-modal Interaction

问题与 changed constraint：duplex evaluation makes response timing and content alignment joint evidence instead of scoring only a completed offline answer

机制与 ownership：To address this gap, we propose Omni-DuplexEval, a benchmark for systematically evaluating real-time duplex interaction. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17360v1 — §3 Omni-DuplexEval (§3.2–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17360v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17360v1 — Appendix D Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17360:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17360:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17360:end -->

<!-- review:SF-2026-ARXIV-2605-17373:start -->
#### FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics

问题与 changed constraint：research-agent benchmarks must separate search policy from execution substrate and preserve process-level trajectory metrics

机制与 ownership：We propose FML-Bench, a benchmark of 18 fundamental ML research tasks across 10 domains that separates agent strategy from execution infrastructure and defines 12 process-level behavioral metrics. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17373v1 — §3 FML-bench (§3.2–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17373v1 — §4 Experiments; §5 Search-dynamics analysis (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17373v1 — Appendix N Broader impacts; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17373:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17373:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17373:end -->

<!-- review:SF-2026-ARXIV-2605-17380:start -->
#### ADR: An Agentic Detection System for Enterprise Agentic AI Security

问题与 changed constraint：agent security needs prompt/tool/causal-chain telemetry plus cheap triage and contextual escalation, not file events alone

机制与 ownership：We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven enterprise framework for securing AI agents operating through the Model Context Protocol (MCP). owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17380v1 — §3 ADR System Design (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17380v1 — §5 Evaluation; §6 Real-World Deployment (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17380v1 — §7 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17380:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17380:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17380:end -->

<!-- review:SF-2026-ARXIV-2605-17415:start -->
#### IVF-TQ: Calibration-Free Streaming Vector Search via a Codebook-Free Residual Layer

问题与 changed constraint：streaming ANN requires an explicit coarse-index refresh owner and bounded stale-assignment fallback

机制与 ownership：Approximate nearest neighbor (ANN) indexes deployed against streaming corpora silently lose recall over weeks. owner=`AGENT-RAG`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17415v1 — §3 IVF-TQ (§3.1–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17415v1 — §4 Streaming Experiments; §5 Million-Scale Evaluation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17415v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17415:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17415:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17415:end -->

<!-- review:SF-2026-ARXIV-2605-17439:start -->
#### DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents

问题与 changed constraint：GUI-agent evaluation separates outcome scoring from failure localization and counterfactual diagnosis

机制与 ownership：We present DiagEval, a trajectory-conditioned diagnostic evaluation protocol for post-failure GUI-agent evaluation of interactive software. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17439v1 — §4 DiagEval (§4.1–§4.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17439v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17439v1 — §6 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17439:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17439:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17439:end -->

<!-- review:SF-2026-ARXIV-2605-17453:start -->
#### Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback

问题与 changed constraint：工具在探索期积累可信反馈、到隐藏状态满足时才毒化最终 action；final-action guard 必须对 trajectory-derived environment variables 做风险审查，单次 tool selection 不足。

机制与 ownership：To study this setting, we construct TRUST-Bench, a task-conditioned benchmark of 1,970 hidden-trigger tool-compromise episodes with matched safe controls, introduce an asymmetric penalty metric, GuardedJoint, to better reflect real deployment risk, and present VISTA-Guard, a backbone-agnostic framework for final-action risk scoring. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17453v1 — §3 Method: VISTA-Guard under Untrusted Tool Feedback (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17453v1 — §2 Threat Model, Benchmark, and Evaluation Lens (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17453v1 — §5 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17453:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17453:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17453:end -->

<!-- review:SF-2026-ARXIV-2605-17467:start -->
#### VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems

问题与 changed constraint：multi-agent verification assigns claims and evidence to agents so disagreement is attributable rather than pooled

机制与 ownership：To address these challenges, we propose VerifyMAS, a hypothesis verification framework for agent failure attribution. owner=`AGENT-MULTI-AGENT`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17467v1 — §3 VerifyMAS (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17467v1 — §4 Main Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17467v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17467:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17467:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17467:end -->

<!-- review:SF-2026-ARXIV-2605-17471:start -->
#### WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points

问题与 changed constraint：quantization-aware training changes loss geometry and convergence assumptions; deployment speedup still depends on compatible kernels

机制与 ownership：To mitigate these issues, we propose an algorithm called WinQ to accelerate QAT, which involves: (1) periodically resetting weights to the linear interpolation of full-precision and quantized weights, reducing the distance to the quantization grid and increasing eigenvalue magnitude, and (2) computing gradients of noise-injected weights to regularize the Hessian. owner=`TRAIN-PRETRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17471v1 — §3 Our Approach (§3.1–§3.2) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17471v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17471v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17471:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17471:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17471:end -->

<!-- review:SF-2026-ARXIV-2605-17480:start -->
#### The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure

问题与 changed constraint：更强 Worker 可能以更确定语言把 semantic hijacking 传给 Manager；capability/certainty 不能替代 independent evidence，跨 Agent commit 需要来源与反证门。

机制与 ownership：Building on the mediation finding, we propose heterogeneous ensemble verification, which pairs Workers of asymmetric domain competence so their complementary vulnerabilities break the certainty-to-execution chain, reducing ASR from 52.8% to 2.0% with negligible benign-task impact. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17480v1 — §3 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17480v1 — §4 Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17480v1 — §6 Limitations (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17480:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17480:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17480:end -->

<!-- review:SF-2026-ARXIV-2605-17497:start -->
#### Self-Supervised On-Policy Distillation for Reasoning Language Models

问题与 changed constraint：teacher signals are generated on the learner's current rollout distribution, trading stale offline supervision for online sampling cost

机制与 ownership：We show that a mixed group contains a richer process signal: a correct completion is a self-generated witness of how the current policy can solve the problem, while a wrong completion provides on-policy prefixes where the policy needs correction. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17497v1 — §3 Self-Supervised On-Policy Distillation (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17497v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17497v1 — §5 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17497:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17497:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17497:end -->

<!-- review:SF-2026-ARXIV-2605-17508:start -->
#### BESplit: Bias-Compensated Split Federated Learning with Evidential Aggregation

问题与 changed constraint：split federated execution moves activation and optimizer state across a trust/network boundary but remains tied to the disclosed edge workload

机制与 ownership：Based on this insight, we propose BESplit, an architecture-aware framework that exploits the intrinsic structure of SFL to mitigate non-IID effects. owner=`TRAIN-DISTRIBUTED-TRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17508v1 — §4 Methodology (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17508v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17508v1 — §6 Discussion (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17508:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17508:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17508:end -->

<!-- review:SF-2026-ARXIV-2605-17522:start -->
#### RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation

问题与 changed constraint：closed-loop world-model evaluation must bind action conditioning, rollout state and downstream control outcome

机制与 ownership：To address these challenges, we introduce RoboFlow4D, a lightweight flow world model that unifies perception and planning by estimating temporal motion in physical 3D space. owner=`MULTIMODAL-WORLD-MODELS`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17522v1 — §3 Methodology (§3.2–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17522v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17522v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17522:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17522:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17522:end -->

<!-- review:SF-2026-ARXIV-2605-17554:start -->
#### Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps

问题与 changed constraint：deep-research evaluation preserves search process, evidence use and final artifact as distinct measurement planes

机制与 ownership：We introduce a benchmark of 70 SME-authored management consulting prompts, each embedding cognitive traps that penalize surface-pattern reasoning. owner=`PLATFORM-EVALUATION-SYSTEM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17554v1 — §3 Benchmark Design (§3.3–§3.4) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17554v1 — §4 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17554v1 — §5 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17554:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17554:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17554:end -->

<!-- review:SF-2026-ARXIV-2605-17558:start -->
#### Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs

问题与 changed constraint：tool-call training data is admitted only after executable verification and typed failure closure

机制与 ownership：We present FireFly, a pipeline for generating verified tool-call data from real-world MCP servers. owner=`AGENT-TOOL-CALLING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17558v1 — §3 Method (§3.1–§3.3) (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17558v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17558v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17558:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17558:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17558:end -->

<!-- review:SF-2026-ARXIV-2605-17570:start -->
#### How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning

问题与 changed constraint：asynchronous RL must account for policy-version staleness in advantage updates rather than treating every rollout as current

机制与 ownership：We show that GRPO-style algorithms can tolerate substantially larger rollout staleness than previously assumed, and propose Mu-GRPO, an RL training framework that organizes training into a small number (e.g., four) of large sequential generation-optimization stages. owner=`TRAIN-GRPO`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17570v1 — §3 Diagnosing rollout staleness; §4 μ-GRPO (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17570v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17570v1 — §6 Discussion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17570:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17570:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17570:end -->

<!-- review:SF-2026-ARXIV-2605-17590:start -->
#### Form and Function: Machine Unlearning as a Problem of Misaligned States

问题与 changed constraint：Machine unlearning 的目标不是只校正参数，而是对齐删除编辑后的 counterfactual optimizer state，包括 L-BFGS memory operator 与下一步 update direction。

机制与 ownership：We introduce state-aware metrics that separately measure parameter error, memory-operator error, combined state error, and update-direction error. owner=`TRAIN-DATA`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17590v1 — §4 Problem Setup (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17590v1 — §5 Theoretical Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17590v1 — §7 Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17590:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17590:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17590:end -->

<!-- review:SF-2026-ARXIV-2605-17609:start -->
#### Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification

问题与 changed constraint：test-time compute allocation jointly owns generation count, rank signal, verifier budget and stopping under an explicit monotonicity assumption

机制与 ownership：We formalize this setting using a learning-theoretic lens as generative active search: a cost-sensitive first-positive search problem in which a policy adaptively samples candidates from an unknown distribution, observes cheap scores, and pays for verifier labels until it finds a positive example. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17609v1 — §4 ADAP Adaptive Policy (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17609v1 — §5 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17609v1 — §7 Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17609:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17609:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17609:end -->

<!-- review:SF-2026-ARXIV-2605-17610:start -->
#### SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening

问题与 changed constraint：fast/slow video moderation routes only uncertain temporal cases to deliberation while preserving a conservative safety fallback

机制与 ownership：We propose SafeLens, a video guardrail framework that introduces a fast-and-slow inference architecture for efficient and accurate content moderation with variable computational cost across inputs. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17610v1 — §4 Data Curation; §5 SafeLens (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17610v1 — §6 Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17610v1 — Appendix A Limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17610:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17610:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17610:end -->

<!-- review:SF-2026-ARXIV-2605-17613:start -->
#### VeriCache: Turning Lossy KV Cache into Lossless LLM Inference

问题与 changed constraint：有损 KV 只作为 draft，full KV 被保留到慢层并拥有最终 verification/commit；换取 lossless output 的代价是 full-state tier、swap/prefetch 与验证失败回退。

机制与 ownership：We present VeriCache, the first inference framework that ensures the same output as full-KV-cache decoding but largely preserves the high decoding throughput of a range of KV cache compression algorithms. owner=`INFER-KV-CACHE`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17613v1 — §3 Motivation: Why Lossy KV Methods Fail (frozen exact-v1 official HTML receipt)`；Evaluation=`Not Disclosed — no dedicated evaluation heading in the frozen exact-v1 receipt`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17613:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17613:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17613:end -->

<!-- review:SF-2026-ARXIV-2605-17617:start -->
#### GraphMind: From Operational Traces to Self-Evolving Workflow Automation

问题与 changed constraint：operational traces become versioned workflow graphs whose online traversal and reinforcement need separate owners

机制与 ownership：We present GraphMind, a system that constructs, executes, and evolves action-centric workflow graphs with minimal human effort. owner=`AGENT-WORKFLOW`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17617v1 — §3 Offline Workflow Graph; §4 Online Traversal; §5 Reinforcement (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17617v1 — §6 Evaluation; §7 Production Deployment (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17617v1 — §8 Discussion (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17617:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17617:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17617:end -->

<!-- review:SF-2026-ARXIV-2605-17625:start -->
#### Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents

问题与 changed constraint：episodic window and semantic consolidation are separate memory states; consolidation quality, contradiction and growth are explicit failure modes

机制与 ownership：As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17625v1 — §3 Dual-Process Memory Architecture; §3.2 Episodic Window; §3.3 Semantic Consolidation (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17625v1 — §4 Experimental Design; §5 Results (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17625v1 — §6 Discussion and limitations (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17625:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17625:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17625:end -->

<!-- review:SF-2026-ARXIV-2605-17634:start -->
#### AI Agents May Always Fall for Prompt Injections

问题与 changed constraint：Prompt injection 不可仅靠 data/instruction separation 完全解决；Contextual Integrity 显示 norm manipulation/mixed flows 的不可判定边界，最终 authority 必须由 capability policy/approval 持有。

机制与 ownership：Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17634v1 — §1 Introduction (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17634v1 — §5.1 Attacking Context Parameters Inference and Norm Evaluation (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17634v1 — §3 Limitations of Current Views on Prompt Injection (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17634:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17634:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17634:end -->

<!-- review:SF-2026-ARXIV-2605-17641:start -->
#### Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents

问题与 changed constraint：Memory selection 从 semantic similarity 演进为 controlled causal interventions；收益依赖 intervention/judge validity，计算成本和 distribution shift 要求保留普通 retrieval fallback。

机制与 ownership：We propose Causal Memory Intervention (CMI), a causal memory-selection technique that estimates how candidate memories affect the model's answer under controlled interventions, selecting memories that improve task performance while suppressing unstable, irrelevant, or harmful ones. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17641v1 — §3 Proposed Framework (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17641v1 — §5 Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17641:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17641:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17641:end -->

<!-- review:SF-2026-ARXIV-2605-17659:start -->
#### Bug or Feature$^2$: Weight Drift, Activation Sparsity and Spikes

问题与 changed constraint：正偏激活与标准 loss 在初始化产生 negative weight drift，进而形成 activation sparsity/spikes；这是 optimizer–activation coupling，不是单纯数据性质或默认正则收益。

机制与 ownership：The design of modern neural architectures has converged through incremental empirical choices, yet the mechanisms governing their training dynamics remain only partially understood. owner=`TRAIN-PRETRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17659v1 — §1 Formal Illustration of Negative Weight Drift (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17659v1 — §2 Empirical Results for Negative Weight Drift (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17659:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17659:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17659:end -->

<!-- review:SF-2026-ARXIV-2605-17672:start -->
#### Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models

问题与 changed constraint：Reasoning early exit 应检测 successive-step semantic convergence，而非只看 answer confidence；节省 token 的代价是 embedding/judge 开销与 premature-stop failure。

机制与 ownership：Building on this insight, we propose PUMA, a plug-and-play framework that combines a lightweight Redundancy Detector with answer-level verification. owner=`INFER-SCHEDULING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17672v1 — §3 Methodology (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17672v1 — §4 Experimental Setup (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`arXiv:2605.17672v1 — §6 Analysis and Discussion (frozen exact-v1 official HTML receipt)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17672:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17672:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17672:end -->

<!-- review:SF-2026-ARXIV-2605-17683:start -->
#### μ-ORCA: Optimizing Acceleration for Microsecond-Scale Deep Neural Network Inference on ACAP

问题与 changed constraint：microsecond inference requires overhead-aware execution planning across direct inter-layer links, synchronization and non-matmul operators

机制与 ownership：To address these problems, we propose μ-ORCA, a customized heterogeneous accelerator framework for ultra-low-latency model inference. owner=`INFER-TENSORRT-LLM`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17683v1 — §4 μ-ORCA Architecture and Implementation; §5 Performance Model and Design-Space Exploration (official exact-v1 HTML)`；Evaluation=`arXiv:2605.17683v1 — §6 Evaluation (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.17683v1 — §7 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17683:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17683:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17683:end -->

<!-- review:SF-2026-ARXIV-2605-17707:start -->
#### Speed Kills: Exploring Confused Deputy Attacks Through Edge AI Accelerators

问题与 changed constraint：Edge AI accelerator 绕过 OS 语义隔离时可能成为 confused deputy；DMA/地址/权限验证必须进入 accelerator–driver contract，而不是只相信应用进程边界。

机制与 ownership：We propose an on-demand validation defense against CDA, and evaluation on the Gem5- salam simulator shows that it incurs minimal runtime overhead (i.e., ~15%). owner=`PLATFORM-SECURITY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17707v1 — §VIII-B () Setup (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17707v1 — §VIII-D2 Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17707:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17707:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17707:end -->

<!-- review:SF-2026-ARXIV-2605-17721:start -->
#### EXG: Self-Evolving Agents with Experience Graphs

问题与 changed constraint：Self-evolving Agent 把成功/失败经验组织为 online/offline experience graph；结构化复用提高可用性，同时带来 provenance、staleness、错误传播与 graph lifecycle 成本。

机制与 ownership：To address this limitation, we introduce EXG, an experience graph framework for self-evolving agents that explicitly organizes accumulated successes and failures into a structured, relational representation. owner=`AGENT-MEMORY`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.17721v1 — §2 Experience Graph Design (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2605.17721v1 — §4 Experiments (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-17721:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-17721:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-17721:end -->

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

<!-- review:SF-2026-ARXIV-2606-20591:start -->
#### Delay-Adaptive Speculation Control for Low-Latency Edge-Cloud LLM Inference

问题与 changed constraint：edge-cloud speculative decoding 的 draft length 是 communication delay 与 acceptance 的在线 optimal-stopping 控制量；网络状态估计失真时必须回退固定/短 draft。

机制与 ownership：Speculative decoding accelerates large language model (LLM) inference by using a lightweight draft model to propose tokens and a larger target model to verify them in parallel. owner=`INFER-SPECULATIVE-DECODING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2606.20591v1 — §III System Model and Problem Formulation (frozen exact-v1 official HTML receipt)`；Evaluation=`arXiv:2606.20591v1 — §IV Theoretical Results (frozen exact-v1 official HTML receipt)`。

Trade-off / failure：`Not Disclosed — no dedicated limitations heading; claim remains bounded to disclosed setup`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2606-20591:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2606-20591:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2606-20591:end -->

<!-- review:SF-2026-ARXIV-2605-23988:start -->
#### TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks

问题与 changed constraint：split fine-tuning compresses activation tokens before transmission, coupling accuracy, uplink traffic, server compute and frozen-backbone identity

机制与 ownership：Experiments on ViT models over CIFAR-10, CIFAR-100, and TinyImageNet show that TSFLora achieves up to \textbf{6.8$\times$} communication reduction and \textbf{41\%} memory saving while maintaining competitive accuracy. owner=`TRAIN-DISTRIBUTED-TRAINING`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.23988v1 — §II Architecture and Workflow; §III Token Compression (official exact-v1 HTML)`；Evaluation=`arXiv:2605.23988v1 — §VI Experiments (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.23988v1 — §VII Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-23988:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-23988:end -->

Books Decision=`Integrate`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-23988:end -->

<!-- review:SF-2026-ARXIV-2605-23993:start -->
#### Nano World Models: A Minimalist Implementation of Future Video Prediction

问题与 changed constraint：a reproducible world-model substrate versions objective, action conditioning, latent state, rollout and evaluation rather than comparing entangled codebases

机制与 ownership：We introduce Nano World Models, a minimalist codebase for future video prediction centered around diffusion forcing. owner=`MULTIMODAL-WORLD-MODELS`；模型/论文只提出 signal 或 proposal，最终 authority 仍由 owner contract 持有。

Evaluation contract：Method=`arXiv:2605.23993v1 — §3 Diffusion-Forcing Interface and Experimental Substrate (official exact-v1 HTML)`；Evaluation=`arXiv:2605.23993v1 — §4 Findings (official exact-v1 HTML)`。

Trade-off / failure：`arXiv:2605.23993v1 — §5 Conclusion; no dedicated limitations section (official exact-v1 HTML)`；未披露字段保持 Not Disclosed，越出 exact-v1 设置即回退旧路径。

<!-- claim:SF-2026-ARXIV-2605-23993:start -->只支持 exact-v1 披露设置中的机制与结果，不证明跨模型、跨硬件、开放分布或生产尾部保证。<!-- claim:SF-2026-ARXIV-2605-23993:end -->

Books Decision=`No Change — Existing Coverage`；共享 Books 尚未写入。
<!-- review:SF-2026-ARXIV-2605-23993:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

所有数字只属于 exact-v1 披露合同；未披露字段保持 Not Disclosed。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17222 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17222 |
| SF-2026-ARXIV-2605-17234 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17234 |
| SF-2026-ARXIV-2605-17242 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17242 |
| SF-2026-ARXIV-2605-17246 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17246 |
| SF-2026-ARXIV-2605-17260 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17260 |
| SF-2026-ARXIV-2605-17268 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17268 |
| SF-2026-ARXIV-2605-17273 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17273 |
| SF-2026-ARXIV-2605-17281 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17281 |
| SF-2026-ARXIV-2605-17288 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17288 |
| SF-2026-ARXIV-2605-17289 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17289 |
| SF-2026-ARXIV-2605-17291 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17291 |
| SF-2026-ARXIV-2605-17292 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17292 |
| SF-2026-ARXIV-2605-17301 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17301 |
| SF-2026-ARXIV-2605-17304 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17304 |
| SF-2026-ARXIV-2605-17305 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17305 |
| SF-2026-ARXIV-2605-17320 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17320 |
| SF-2026-ARXIV-2605-17324 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17324 |
| SF-2026-ARXIV-2605-17329 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17329 |
| SF-2026-ARXIV-2605-17348 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17348 |
| SF-2026-ARXIV-2605-17360 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17360 |
| SF-2026-ARXIV-2605-17373 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17373 |
| SF-2026-ARXIV-2605-17380 | score_7_9; forced_review; potential_books_delta | selected | DA-AGENT-SECURITY-TELEMETRY | — | 跨层 ownership 与运行时 failure pressure | analysis:DA-AGENT-SECURITY-TELEMETRY |
| SF-2026-ARXIV-2605-17415 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17415 |
| SF-2026-ARXIV-2605-17439 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17439 |
| SF-2026-ARXIV-2605-17453 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17453 |
| SF-2026-ARXIV-2605-17467 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17467 |
| SF-2026-ARXIV-2605-17471 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17471 |
| SF-2026-ARXIV-2605-17480 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17480 |
| SF-2026-ARXIV-2605-17497 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17497 |
| SF-2026-ARXIV-2605-17508 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17508 |
| SF-2026-ARXIV-2605-17522 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17522 |
| SF-2026-ARXIV-2605-17554 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17554 |
| SF-2026-ARXIV-2605-17558 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17558 |
| SF-2026-ARXIV-2605-17570 | score_7_9; forced_review; potential_books_delta | selected | DA-ROLLOUT-STALENESS | — | 跨层 ownership 与运行时 failure pressure | analysis:DA-ROLLOUT-STALENESS |
| SF-2026-ARXIV-2605-17590 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17590 |
| SF-2026-ARXIV-2605-17609 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17609 |
| SF-2026-ARXIV-2605-17610 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17610 |
| SF-2026-ARXIV-2605-17613 | score_7_9; forced_review; potential_books_delta | selected | DA-LOSSLESS-KV | — | 跨层 ownership 与运行时 failure pressure | analysis:DA-LOSSLESS-KV |
| SF-2026-ARXIV-2605-17617 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17617 |
| SF-2026-ARXIV-2605-17625 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17625 |
| SF-2026-ARXIV-2605-17634 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17634 |
| SF-2026-ARXIV-2605-17641 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17641 |
| SF-2026-ARXIV-2605-17659 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17659 |
| SF-2026-ARXIV-2605-17672 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17672 |
| SF-2026-ARXIV-2605-17683 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17683 |
| SF-2026-ARXIV-2605-17707 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17707 |
| SF-2026-ARXIV-2605-17721 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-17721 |
| SF-2026-ARXIV-2605-18891 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-18891 |
| SF-2026-ARXIV-2605-18899 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2606-20591 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2606-20591 |
| SF-2026-ARXIV-2605-23988 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-23988 |
| SF-2026-ARXIV-2605-23993 | score_7_9 | not_selected | — | — | 已完成同等 exact-v1 Review；Top-3 仅限制叙事 | analysis-decision:SF-2026-ARXIV-2605-23993 |

<!-- analysis:DA-AGENT-SECURITY-TELEMETRY:start -->### 从文件事件到 Agent 因果链

传统 EDR 看到副作用，却看不到 prompt、tool observation 与意图到执行的因果链。ADR 把高保真 agent telemetry、离线 hard-example red team、在线 cheap triage 与上下文升级串成两速检测路径。收益是可归因与成本控制；代价是敏感 telemetry、detector drift、误报与 prompt 隐私。传感器缺失或上下文越界时必须 fail closed 或回退人工审查。<!-- analysis:DA-AGENT-SECURITY-TELEMETRY:end -->

<!-- analysis:DA-ROLLOUT-STALENESS:start -->### 从异步吞吐到 policy-version correctness

异步 rollout 提高设备利用率，但 learner 已更新后，旧 policy 轨迹会给当前 policy 错配 credit。μ-GRPO 把 rollout version/staleness 进入更新权重与拒收条件；换来的是额外版本状态、样本丢弃和吞吐波动。同步 rollout 在模型小、网络稳定或 correctness 优先时仍更透明。<!-- analysis:DA-ROLLOUT-STALENESS:end -->

<!-- analysis:DA-LOSSLESS-KV:start -->### 从有损 KV 到 draft/verify/commit

直接压缩 KV 省显存，却可能改变自回归结果。VeriCache 让压缩 KV 只拥有 draft 权，full KV 在慢层验证并 commit；收益是可验证 exactness，代价是 full-state tier、swap/prefetch、验证失败和 acceptance 波动。内存足够或尾延迟更重要时直接 full KV 仍是基线。<!-- analysis:DA-LOSSLESS-KV:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17222:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17222:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17234:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17234:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17242:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17242:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17246:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17246:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17260:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17260:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17268:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17268:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17273:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17273:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17281:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17281:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17288:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17288:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17289:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17289:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17291:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17291:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17292:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17292:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17301:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17301:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17304:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17304:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17305:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17305:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17320:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17320:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17324:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17324:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17329:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17329:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17348:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17348:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17360:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17360:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17373:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17373:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17415:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17415:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17439:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17439:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17453:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17453:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17467:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17467:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17471:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17471:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17480:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17480:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17497:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17497:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17508:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17508:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17522:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17522:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17554:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17554:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17558:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17558:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17590:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17590:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17609:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17609:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17610:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17610:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17617:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17617:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17625:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17625:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17634:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17634:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17641:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17641:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17659:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17659:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17672:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17672:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17683:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17683:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17707:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17707:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17721:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-17721:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18891:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-18891:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18899:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-18899:end -->
<!-- analysis-decision:SF-2026-ARXIV-2606-20591:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2606-20591:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23988:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-23988:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23993:start -->完成 exact-v1 Source Review；未进入 Top-3 只代表日报叙事被更强跨层候选 subsume，不降低证据义务。<!-- analysis-decision:SF-2026-ARXIV-2605-23993:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17222 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17222 | delta:SF-2026-ARXIV-2605-17222 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17222 |
| SF-2026-ARXIV-2605-17234 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#chapter-7 | books/part-01-worldview/06-why-transformer-changed-the-world.md#chapter-6; books/part-01-worldview/08-why-llms-show-intelligence.md#chapter-8 | existing:SF-2026-ARXIV-2605-17234 | delta:SF-2026-ARXIV-2605-17234 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17234 |
| SF-2026-ARXIV-2605-17242 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17242 | delta:SF-2026-ARXIV-2605-17242 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17242 |
| SF-2026-ARXIV-2605-17246 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17246 | delta:SF-2026-ARXIV-2605-17246 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17246 |
| SF-2026-ARXIV-2605-17260 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-17260 | delta:SF-2026-ARXIV-2605-17260 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17260 |
| SF-2026-ARXIV-2605-17268 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-17268 | delta:SF-2026-ARXIV-2605-17268 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17268 |
| SF-2026-ARXIV-2605-17273 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17273 | delta:SF-2026-ARXIV-2605-17273 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17273 |
| SF-2026-ARXIV-2605-17281 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17281 | delta:SF-2026-ARXIV-2605-17281 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17281 |
| SF-2026-ARXIV-2605-17288 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17288 | delta:SF-2026-ARXIV-2605-17288 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17288 |
| SF-2026-ARXIV-2605-17289 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17289 | delta:SF-2026-ARXIV-2605-17289 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17289 |
| SF-2026-ARXIV-2605-17291 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30; books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17291 | delta:SF-2026-ARXIV-2605-17291 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17291 |
| SF-2026-ARXIV-2605-17292 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17292 | delta:SF-2026-ARXIV-2605-17292 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17292 |
| SF-2026-ARXIV-2605-17301 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17301 | delta:SF-2026-ARXIV-2605-17301 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17301 |
| SF-2026-ARXIV-2605-17304 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74; books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-17304 | delta:SF-2026-ARXIV-2605-17304 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17304 |
| SF-2026-ARXIV-2605-17305 | AGENT-REFLECTION | books/part-07-agent/80-reflection.md#chapter-80 | books/part-07-agent/79-planning.md#chapter-79; books/part-07-agent/81-workflow.md#chapter-81 | existing:SF-2026-ARXIV-2605-17305 | delta:SF-2026-ARXIV-2605-17305 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17305 |
| SF-2026-ARXIV-2605-17320 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17320 | delta:SF-2026-ARXIV-2605-17320 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17320 |
| SF-2026-ARXIV-2605-17324 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17324 | delta:SF-2026-ARXIV-2605-17324 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17324 |
| SF-2026-ARXIV-2605-17329 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17329 | delta:SF-2026-ARXIV-2605-17329 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17329 |
| SF-2026-ARXIV-2605-17348 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17348 | delta:SF-2026-ARXIV-2605-17348 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17348 |
| SF-2026-ARXIV-2605-17360 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17360 | delta:SF-2026-ARXIV-2605-17360 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17360 |
| SF-2026-ARXIV-2605-17373 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17373 | delta:SF-2026-ARXIV-2605-17373 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17373 |
| SF-2026-ARXIV-2605-17380 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17380 | delta:SF-2026-ARXIV-2605-17380 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17380 |
| SF-2026-ARXIV-2605-17415 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17415 | delta:SF-2026-ARXIV-2605-17415 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17415 |
| SF-2026-ARXIV-2605-17439 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17439 | delta:SF-2026-ARXIV-2605-17439 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17439 |
| SF-2026-ARXIV-2605-17453 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17453 | delta:SF-2026-ARXIV-2605-17453 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17453 |
| SF-2026-ARXIV-2605-17467 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17467 | delta:SF-2026-ARXIV-2605-17467 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17467 |
| SF-2026-ARXIV-2605-17471 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17471 | delta:SF-2026-ARXIV-2605-17471 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17471 |
| SF-2026-ARXIV-2605-17480 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17480 | delta:SF-2026-ARXIV-2605-17480 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17480 |
| SF-2026-ARXIV-2605-17497 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-17497 | delta:SF-2026-ARXIV-2605-17497 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17497 |
| SF-2026-ARXIV-2605-17508 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-17508 | delta:SF-2026-ARXIV-2605-17508 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17508 |
| SF-2026-ARXIV-2605-17522 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-17522 | delta:SF-2026-ARXIV-2605-17522 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17522 |
| SF-2026-ARXIV-2605-17554 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17554 | delta:SF-2026-ARXIV-2605-17554 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17554 |
| SF-2026-ARXIV-2605-17558 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-17558 | delta:SF-2026-ARXIV-2605-17558 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17558 |
| SF-2026-ARXIV-2605-17570 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-17570 | delta:SF-2026-ARXIV-2605-17570 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17570 |
| SF-2026-ARXIV-2605-17590 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17590 | delta:SF-2026-ARXIV-2605-17590 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17590 |
| SF-2026-ARXIV-2605-17609 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17609 | delta:SF-2026-ARXIV-2605-17609 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17609 |
| SF-2026-ARXIV-2605-17610 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17610 | delta:SF-2026-ARXIV-2605-17610 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17610 |
| SF-2026-ARXIV-2605-17613 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17613 | delta:SF-2026-ARXIV-2605-17613 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17613 |
| SF-2026-ARXIV-2605-17617 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17617 | delta:SF-2026-ARXIV-2605-17617 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17617 |
| SF-2026-ARXIV-2605-17625 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17625 | delta:SF-2026-ARXIV-2605-17625 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17625 |
| SF-2026-ARXIV-2605-17634 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17634 | delta:SF-2026-ARXIV-2605-17634 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17634 |
| SF-2026-ARXIV-2605-17641 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17641 | delta:SF-2026-ARXIV-2605-17641 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17641 |
| SF-2026-ARXIV-2605-17659 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17659 | delta:SF-2026-ARXIV-2605-17659 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17659 |
| SF-2026-ARXIV-2605-17672 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17672 | delta:SF-2026-ARXIV-2605-17672 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17672 |
| SF-2026-ARXIV-2605-17683 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17683 | delta:SF-2026-ARXIV-2605-17683 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17683 |
| SF-2026-ARXIV-2605-17707 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-17707 | delta:SF-2026-ARXIV-2605-17707 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17707 |
| SF-2026-ARXIV-2605-17721 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17721 | delta:SF-2026-ARXIV-2605-17721 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17721 |
| SF-2026-ARXIV-2605-18891 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-18891 | delta:SF-2026-ARXIV-2605-18891 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18891 |
| SF-2026-ARXIV-2605-18899 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-18899 | delta:SF-2026-ARXIV-2605-18899 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18899 |
| SF-2026-ARXIV-2606-20591 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2606-20591 | delta:SF-2026-ARXIV-2606-20591 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-20591 |
| SF-2026-ARXIV-2605-23988 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-23988 | delta:SF-2026-ARXIV-2605-23988 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23988 |
| SF-2026-ARXIV-2605-23993 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23993 | delta:SF-2026-ARXIV-2605-23993 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23993 |

<!-- books-review:SF-2026-ARXIV-2605-17222:start -->
<!-- existing:SF-2026-ARXIV-2605-17222:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17222:end -->
<!-- delta:SF-2026-ARXIV-2605-17222:start -->CKKS 线性变换把 rotation 数量、off-chip traffic 与 FPGA permutation/data-path 共同暴露为隐私推理的硬件执行合同；收益不等于通用 GPU/模型加速。<!-- delta:SF-2026-ARXIV-2605-17222:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17222:end -->
<!-- books-review:SF-2026-ARXIV-2605-17234:start -->
<!-- existing:SF-2026-ARXIV-2605-17234:start -->独立 reviewer 顺读 `books/part-01-worldview/07-scaling-law.md` 与相邻章节 ['books/part-01-worldview/06-why-transformer-changed-the-world.md', 'books/part-01-worldview/08-why-llms-show-intelligence.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e0c3271fd260faf72be338e83ba9a9e394be267b033f70d14914934a4d51801a。<!-- existing:SF-2026-ARXIV-2605-17234:end -->
<!-- delta:SF-2026-ARXIV-2605-17234:start -->Scaling-law 实验预算从均匀采样演进为 successive-halving 与 surrogate-guided pruning；节省拟合成本的同时引入错误早停与 surrogate selection bias。<!-- delta:SF-2026-ARXIV-2605-17234:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17234:end -->
<!-- books-review:SF-2026-ARXIV-2605-17242:start -->
<!-- existing:SF-2026-ARXIV-2605-17242:start -->独立 reviewer 顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6e71a861a0983658675a17c274f4899af49cf05cf91646a8a52289bd724fd6ab。<!-- existing:SF-2026-ARXIV-2605-17242:end -->
<!-- delta:SF-2026-ARXIV-2605-17242:start -->acceptance tests become pre-execution workflow state; browser-observed failures become typed repair evidence rather than terminal text<!-- delta:SF-2026-ARXIV-2605-17242:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17242:end -->
<!-- books-review:SF-2026-ARXIV-2605-17246:start -->
<!-- existing:SF-2026-ARXIV-2605-17246:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17246:end -->
<!-- delta:SF-2026-ARXIV-2605-17246:start -->Specification–code alignment 由单一测试通过率扩展为 code-grounded fidelity probes、contradiction/coverage-gap 分解和 frozen held-out resampling；probe generator 仍不是完整语义 oracle。<!-- delta:SF-2026-ARXIV-2605-17246:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17246:end -->
<!-- books-review:SF-2026-ARXIV-2605-17260:start -->
<!-- existing:SF-2026-ARXIV-2605-17260:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=cde0ccfed7241f74e706727568f977cfe98384d75b2483b4c57eedc44fa486c4。<!-- existing:SF-2026-ARXIV-2605-17260:end -->
<!-- delta:SF-2026-ARXIV-2605-17260:start -->post-hoc visual-token reduction 会把瓶颈推回逐帧 vision encoder；compressed-token distillation 让 encoder 直接生成时空压缩表示，交换 teacher 成本、表示偏差和 frame coverage。<!-- delta:SF-2026-ARXIV-2605-17260:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17260:end -->
<!-- books-review:SF-2026-ARXIV-2605-17268:start -->
<!-- existing:SF-2026-ARXIV-2605-17268:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节 ['books/part-03-multimodal-world-models/25-multimodal-world-models.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=42393275c6844463595681634a612f8895ae52a56bd78a817077a56b26e65038。<!-- existing:SF-2026-ARXIV-2605-17268:end -->
<!-- delta:SF-2026-ARXIV-2605-17268:start -->VLA 的自然语言 rationale 不能取得 trajectory safety authority；reasoning fidelity、entity/action consistency 与视觉扰动稳定性必须成为独立传感器并由安全控制器提交动作。<!-- delta:SF-2026-ARXIV-2605-17268:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17268:end -->
<!-- books-review:SF-2026-ARXIV-2605-17273:start -->
<!-- existing:SF-2026-ARXIV-2605-17273:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17273:end -->
<!-- delta:SF-2026-ARXIV-2605-17273:start -->SOTA claim 需要 effect size、consistency、uncertainty 与 task-level superiority 证据，平均分第一只证明 aggregate ranking，不证明广泛优越。<!-- delta:SF-2026-ARXIV-2605-17273:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17273:end -->
<!-- books-review:SF-2026-ARXIV-2605-17281:start -->
<!-- existing:SF-2026-ARXIV-2605-17281:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17281:end -->
<!-- delta:SF-2026-ARXIV-2605-17281:start -->工具 observation 中的 presigned URL、session token 与 OAuth state 是带 byte-integrity 和 expiry 的 contract；模型只能传递，不能自由改写或延迟复用。<!-- delta:SF-2026-ARXIV-2605-17281:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17281:end -->
<!-- books-review:SF-2026-ARXIV-2605-17288:start -->
<!-- existing:SF-2026-ARXIV-2605-17288:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17288:end -->
<!-- delta:SF-2026-ARXIV-2605-17288:start -->模型 cascade 的轻量 front-end 与 escalation controller 扩大攻击面；攻击可同时破坏质量和成本目标，因此 route/admission 需绑定 adversarial evidence 与保守 fallback。<!-- delta:SF-2026-ARXIV-2605-17288:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17288:end -->
<!-- books-review:SF-2026-ARXIV-2605-17289:start -->
<!-- existing:SF-2026-ARXIV-2605-17289:start -->独立 reviewer 顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17289:end -->
<!-- delta:SF-2026-ARXIV-2605-17289:start -->端到端 unstructured mask learning 把 pruning owner 从 layer-wise surrogate 移到全局 mask objective，但一次性 H100 训练成本和 kernel compatibility 不等于部署 speedup。<!-- delta:SF-2026-ARXIV-2605-17289:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17289:end -->
<!-- books-review:SF-2026-ARXIV-2605-17291:start -->
<!-- existing:SF-2026-ARXIV-2605-17291:start -->独立 reviewer 顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=f89604163f74332678caef15a44cb856c58d35237798871d9009db06389a44be。<!-- existing:SF-2026-ARXIV-2605-17291:end -->
<!-- delta:SF-2026-ARXIV-2605-17291:start -->final-answer reward 对中间步骤产生错误 credit；step-wise rubric attribution/normalization 改变 gradient ownership，但依赖 judge 与显式 step boundary。<!-- delta:SF-2026-ARXIV-2605-17291:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17291:end -->
<!-- books-review:SF-2026-ARXIV-2605-17292:start -->
<!-- existing:SF-2026-ARXIV-2605-17292:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17292:end -->
<!-- delta:SF-2026-ARXIV-2605-17292:start -->delegation consumes a capability profile and confidence sensor, but self-reported confidence cannot own commit authority<!-- delta:SF-2026-ARXIV-2605-17292:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17292:end -->
<!-- books-review:SF-2026-ARXIV-2605-17301:start -->
<!-- existing:SF-2026-ARXIV-2605-17301:start -->独立 reviewer 顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=3986f4307ffd57af8ace87d5c720982b992e07f247a91b16d73a39d83a8917a2。<!-- existing:SF-2026-ARXIV-2605-17301:end -->
<!-- delta:SF-2026-ARXIV-2605-17301:start -->RAG 在生成前显式检测、分类并解决 retrieved-source conflict；source credibility 与 temporal/opinion policy 变成可审计状态，但 LLM judge 与合成冲突数据限制外推。<!-- delta:SF-2026-ARXIV-2605-17301:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17301:end -->
<!-- books-review:SF-2026-ARXIV-2605-17304:start -->
<!-- existing:SF-2026-ARXIV-2605-17304:start -->独立 reviewer 顺读 `books/part-07-agent/75-context.md` 与相邻章节 ['books/part-07-agent/74-prompt.md', 'books/part-07-agent/76-rag.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=dcfe0b447383d99f4a06e25113b952af345025eaccbae7b73223e12444fe9ba6。<!-- existing:SF-2026-ARXIV-2605-17304:end -->
<!-- delta:SF-2026-ARXIV-2605-17304:start -->Context compression 的对象从 token 变为 typed, source-grounded commitment atoms；压缩必须验证 critical recall、conflict/equivalence 与 recoverability，并在不确定时回退 raw spans/更大 context。<!-- delta:SF-2026-ARXIV-2605-17304:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17304:end -->
<!-- books-review:SF-2026-ARXIV-2605-17305:start -->
<!-- existing:SF-2026-ARXIV-2605-17305:start -->独立 reviewer 顺读 `books/part-07-agent/80-reflection.md` 与相邻章节 ['books/part-07-agent/79-planning.md', 'books/part-07-agent/81-workflow.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c1293a34a41ce0c0ee8d27ebdb10d68cada38430db2d77545ddb7873abd6fe08。<!-- existing:SF-2026-ARXIV-2605-17305:end -->
<!-- delta:SF-2026-ARXIV-2605-17305:start -->self-correction is represented as detector-controller-stop state with overshoot and oscillation, not an unbounded retry loop<!-- delta:SF-2026-ARXIV-2605-17305:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17305:end -->
<!-- books-review:SF-2026-ARXIV-2605-17320:start -->
<!-- existing:SF-2026-ARXIV-2605-17320:start -->独立 reviewer 顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c90613b1e2cab33b382c0cff6ae0226e44b2d66b051e12a15174eae9c5fc6cdc。<!-- existing:SF-2026-ARXIV-2605-17320:end -->
<!-- delta:SF-2026-ARXIV-2605-17320:start -->Computer-use workspace 从一次性 sandbox 演进为 live save/fork/rollback/selective-commit；低延迟 branch 与 durable checkpoint 分权，同时引入 credential、GUI、external side-effect merge 边界。<!-- delta:SF-2026-ARXIV-2605-17320:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17320:end -->
<!-- books-review:SF-2026-ARXIV-2605-17324:start -->
<!-- existing:SF-2026-ARXIV-2605-17324:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17324:end -->
<!-- delta:SF-2026-ARXIV-2605-17324:start -->Clarification 是独立 agent state transition，可能把 prompt injection 从 tool-return path 扩展到后续 user-input path；clarify 不能自动提升输入 authority。<!-- delta:SF-2026-ARXIV-2605-17324:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17324:end -->
<!-- books-review:SF-2026-ARXIV-2605-17329:start -->
<!-- existing:SF-2026-ARXIV-2605-17329:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17329:end -->
<!-- delta:SF-2026-ARXIV-2605-17329:start -->dynamic policy clauses are inference-time guardrail state; latent compression saves latency but remains a fallible sensor<!-- delta:SF-2026-ARXIV-2605-17329:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17329:end -->
<!-- books-review:SF-2026-ARXIV-2605-17348:start -->
<!-- existing:SF-2026-ARXIV-2605-17348:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17348:end -->
<!-- delta:SF-2026-ARXIV-2605-17348:start -->Active/Standby/Terminated is a recoverable agent lifecycle that avoids irreversible pruning after one bad round<!-- delta:SF-2026-ARXIV-2605-17348:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17348:end -->
<!-- books-review:SF-2026-ARXIV-2605-17360:start -->
<!-- existing:SF-2026-ARXIV-2605-17360:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17360:end -->
<!-- delta:SF-2026-ARXIV-2605-17360:start -->duplex evaluation makes response timing and content alignment joint evidence instead of scoring only a completed offline answer<!-- delta:SF-2026-ARXIV-2605-17360:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17360:end -->
<!-- books-review:SF-2026-ARXIV-2605-17373:start -->
<!-- existing:SF-2026-ARXIV-2605-17373:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17373:end -->
<!-- delta:SF-2026-ARXIV-2605-17373:start -->research-agent benchmarks must separate search policy from execution substrate and preserve process-level trajectory metrics<!-- delta:SF-2026-ARXIV-2605-17373:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17373:end -->
<!-- books-review:SF-2026-ARXIV-2605-17380:start -->
<!-- existing:SF-2026-ARXIV-2605-17380:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17380:end -->
<!-- delta:SF-2026-ARXIV-2605-17380:start -->agent security needs prompt/tool/causal-chain telemetry plus cheap triage and contextual escalation, not file events alone<!-- delta:SF-2026-ARXIV-2605-17380:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17380:end -->
<!-- books-review:SF-2026-ARXIV-2605-17415:start -->
<!-- existing:SF-2026-ARXIV-2605-17415:start -->独立 reviewer 顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=3986f4307ffd57af8ace87d5c720982b992e07f247a91b16d73a39d83a8917a2。<!-- existing:SF-2026-ARXIV-2605-17415:end -->
<!-- delta:SF-2026-ARXIV-2605-17415:start -->streaming ANN requires an explicit coarse-index refresh owner and bounded stale-assignment fallback<!-- delta:SF-2026-ARXIV-2605-17415:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17415:end -->
<!-- books-review:SF-2026-ARXIV-2605-17439:start -->
<!-- existing:SF-2026-ARXIV-2605-17439:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17439:end -->
<!-- delta:SF-2026-ARXIV-2605-17439:start -->GUI-agent evaluation separates outcome scoring from failure localization and counterfactual diagnosis<!-- delta:SF-2026-ARXIV-2605-17439:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17439:end -->
<!-- books-review:SF-2026-ARXIV-2605-17453:start -->
<!-- existing:SF-2026-ARXIV-2605-17453:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17453:end -->
<!-- delta:SF-2026-ARXIV-2605-17453:start -->工具在探索期积累可信反馈、到隐藏状态满足时才毒化最终 action；final-action guard 必须对 trajectory-derived environment variables 做风险审查，单次 tool selection 不足。<!-- delta:SF-2026-ARXIV-2605-17453:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17453:end -->
<!-- books-review:SF-2026-ARXIV-2605-17467:start -->
<!-- existing:SF-2026-ARXIV-2605-17467:start -->独立 reviewer 顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=948a0d2dac39b1e241adb0b692a057f0b8ef5411dda794e210d733cba06fa3d3。<!-- existing:SF-2026-ARXIV-2605-17467:end -->
<!-- delta:SF-2026-ARXIV-2605-17467:start -->multi-agent verification assigns claims and evidence to agents so disagreement is attributable rather than pooled<!-- delta:SF-2026-ARXIV-2605-17467:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17467:end -->
<!-- books-review:SF-2026-ARXIV-2605-17471:start -->
<!-- existing:SF-2026-ARXIV-2605-17471:start -->独立 reviewer 顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-17471:end -->
<!-- delta:SF-2026-ARXIV-2605-17471:start -->quantization-aware training changes loss geometry and convergence assumptions; deployment speedup still depends on compatible kernels<!-- delta:SF-2026-ARXIV-2605-17471:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17471:end -->
<!-- books-review:SF-2026-ARXIV-2605-17480:start -->
<!-- existing:SF-2026-ARXIV-2605-17480:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17480:end -->
<!-- delta:SF-2026-ARXIV-2605-17480:start -->更强 Worker 可能以更确定语言把 semantic hijacking 传给 Manager；capability/certainty 不能替代 independent evidence，跨 Agent commit 需要来源与反证门。<!-- delta:SF-2026-ARXIV-2605-17480:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17480:end -->
<!-- books-review:SF-2026-ARXIV-2605-17497:start -->
<!-- existing:SF-2026-ARXIV-2605-17497:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-17497:end -->
<!-- delta:SF-2026-ARXIV-2605-17497:start -->teacher signals are generated on the learner's current rollout distribution, trading stale offline supervision for online sampling cost<!-- delta:SF-2026-ARXIV-2605-17497:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17497:end -->
<!-- books-review:SF-2026-ARXIV-2605-17508:start -->
<!-- existing:SF-2026-ARXIV-2605-17508:start -->独立 reviewer 顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c940481ca012303f984917615764a048e4a6742978fcb826524402093905481b。<!-- existing:SF-2026-ARXIV-2605-17508:end -->
<!-- delta:SF-2026-ARXIV-2605-17508:start -->split federated execution moves activation and optimizer state across a trust/network boundary but remains tied to the disclosed edge workload<!-- delta:SF-2026-ARXIV-2605-17508:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17508:end -->
<!-- books-review:SF-2026-ARXIV-2605-17522:start -->
<!-- existing:SF-2026-ARXIV-2605-17522:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-17522:end -->
<!-- delta:SF-2026-ARXIV-2605-17522:start -->closed-loop world-model evaluation must bind action conditioning, rollout state and downstream control outcome<!-- delta:SF-2026-ARXIV-2605-17522:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17522:end -->
<!-- books-review:SF-2026-ARXIV-2605-17554:start -->
<!-- existing:SF-2026-ARXIV-2605-17554:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6ef373ceb7416023b9a2ee18a9a6b6b920f2219bb2dae08748e4a6adc5a1febc。<!-- existing:SF-2026-ARXIV-2605-17554:end -->
<!-- delta:SF-2026-ARXIV-2605-17554:start -->deep-research evaluation preserves search process, evidence use and final artifact as distinct measurement planes<!-- delta:SF-2026-ARXIV-2605-17554:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17554:end -->
<!-- books-review:SF-2026-ARXIV-2605-17558:start -->
<!-- existing:SF-2026-ARXIV-2605-17558:start -->独立 reviewer 顺读 `books/part-07-agent/78-tool-calling.md` 与相邻章节 ['books/part-07-agent/77-memory.md', 'books/part-07-agent/79-planning.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c0020f56aeee2c8008004dd34f27ed47f49f190f17a43909a885ce972a2a41d4。<!-- existing:SF-2026-ARXIV-2605-17558:end -->
<!-- delta:SF-2026-ARXIV-2605-17558:start -->tool-call training data is admitted only after executable verification and typed failure closure<!-- delta:SF-2026-ARXIV-2605-17558:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17558:end -->
<!-- books-review:SF-2026-ARXIV-2605-17570:start -->
<!-- existing:SF-2026-ARXIV-2605-17570:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-17570:end -->
<!-- delta:SF-2026-ARXIV-2605-17570:start -->asynchronous RL must account for policy-version staleness in advantage updates rather than treating every rollout as current<!-- delta:SF-2026-ARXIV-2605-17570:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17570:end -->
<!-- books-review:SF-2026-ARXIV-2605-17590:start -->
<!-- existing:SF-2026-ARXIV-2605-17590:start -->独立 reviewer 顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8e594c3827c4a7778945dbe71f0c1af1ca4089918dcd0c8998ff54d98ac664a1。<!-- existing:SF-2026-ARXIV-2605-17590:end -->
<!-- delta:SF-2026-ARXIV-2605-17590:start -->Machine unlearning 的目标不是只校正参数，而是对齐删除编辑后的 counterfactual optimizer state，包括 L-BFGS memory operator 与下一步 update direction。<!-- delta:SF-2026-ARXIV-2605-17590:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17590:end -->
<!-- books-review:SF-2026-ARXIV-2605-17609:start -->
<!-- existing:SF-2026-ARXIV-2605-17609:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17609:end -->
<!-- delta:SF-2026-ARXIV-2605-17609:start -->test-time compute allocation jointly owns generation count, rank signal, verifier budget and stopping under an explicit monotonicity assumption<!-- delta:SF-2026-ARXIV-2605-17609:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17609:end -->
<!-- books-review:SF-2026-ARXIV-2605-17610:start -->
<!-- existing:SF-2026-ARXIV-2605-17610:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17610:end -->
<!-- delta:SF-2026-ARXIV-2605-17610:start -->fast/slow video moderation routes only uncertain temporal cases to deliberation while preserving a conservative safety fallback<!-- delta:SF-2026-ARXIV-2605-17610:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17610:end -->
<!-- books-review:SF-2026-ARXIV-2605-17613:start -->
<!-- existing:SF-2026-ARXIV-2605-17613:start -->独立 reviewer 顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=94425d5fe4db0238e99350a5a0299edb408dcffcdb7b32453c76854a9dbc8e86。<!-- existing:SF-2026-ARXIV-2605-17613:end -->
<!-- delta:SF-2026-ARXIV-2605-17613:start -->有损 KV 只作为 draft，full KV 被保留到慢层并拥有最终 verification/commit；换取 lossless output 的代价是 full-state tier、swap/prefetch 与验证失败回退。<!-- delta:SF-2026-ARXIV-2605-17613:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17613:end -->
<!-- books-review:SF-2026-ARXIV-2605-17617:start -->
<!-- existing:SF-2026-ARXIV-2605-17617:start -->独立 reviewer 顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=6e71a861a0983658675a17c274f4899af49cf05cf91646a8a52289bd724fd6ab。<!-- existing:SF-2026-ARXIV-2605-17617:end -->
<!-- delta:SF-2026-ARXIV-2605-17617:start -->operational traces become versioned workflow graphs whose online traversal and reinforcement need separate owners<!-- delta:SF-2026-ARXIV-2605-17617:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17617:end -->
<!-- books-review:SF-2026-ARXIV-2605-17625:start -->
<!-- existing:SF-2026-ARXIV-2605-17625:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17625:end -->
<!-- delta:SF-2026-ARXIV-2605-17625:start -->episodic window and semantic consolidation are separate memory states; consolidation quality, contradiction and growth are explicit failure modes<!-- delta:SF-2026-ARXIV-2605-17625:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17625:end -->
<!-- books-review:SF-2026-ARXIV-2605-17634:start -->
<!-- existing:SF-2026-ARXIV-2605-17634:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17634:end -->
<!-- delta:SF-2026-ARXIV-2605-17634:start -->Prompt injection 不可仅靠 data/instruction separation 完全解决；Contextual Integrity 显示 norm manipulation/mixed flows 的不可判定边界，最终 authority 必须由 capability policy/approval 持有。<!-- delta:SF-2026-ARXIV-2605-17634:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17634:end -->
<!-- books-review:SF-2026-ARXIV-2605-17641:start -->
<!-- existing:SF-2026-ARXIV-2605-17641:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17641:end -->
<!-- delta:SF-2026-ARXIV-2605-17641:start -->Memory selection 从 semantic similarity 演进为 controlled causal interventions；收益依赖 intervention/judge validity，计算成本和 distribution shift 要求保留普通 retrieval fallback。<!-- delta:SF-2026-ARXIV-2605-17641:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17641:end -->
<!-- books-review:SF-2026-ARXIV-2605-17659:start -->
<!-- existing:SF-2026-ARXIV-2605-17659:start -->独立 reviewer 顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=0eca9f709aa5037490fd8ccf36118c63b0a7a18c7abb5e68100e8b89473faf65。<!-- existing:SF-2026-ARXIV-2605-17659:end -->
<!-- delta:SF-2026-ARXIV-2605-17659:start -->正偏激活与标准 loss 在初始化产生 negative weight drift，进而形成 activation sparsity/spikes；这是 optimizer–activation coupling，不是单纯数据性质或默认正则收益。<!-- delta:SF-2026-ARXIV-2605-17659:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17659:end -->
<!-- books-review:SF-2026-ARXIV-2605-17672:start -->
<!-- existing:SF-2026-ARXIV-2605-17672:start -->独立 reviewer 顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=1e3e8c3dff17a6bd79b65130176926b9f10cb1e2ff5bf3e042d4ccee6c302280。<!-- existing:SF-2026-ARXIV-2605-17672:end -->
<!-- delta:SF-2026-ARXIV-2605-17672:start -->Reasoning early exit 应检测 successive-step semantic convergence，而非只看 answer confidence；节省 token 的代价是 embedding/judge 开销与 premature-stop failure。<!-- delta:SF-2026-ARXIV-2605-17672:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17672:end -->
<!-- books-review:SF-2026-ARXIV-2605-17683:start -->
<!-- existing:SF-2026-ARXIV-2605-17683:start -->独立 reviewer 顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8ee7425b911361c8e1e632272a759a2ae9eb63723aeb30c1237bc304ce07fb7b。<!-- existing:SF-2026-ARXIV-2605-17683:end -->
<!-- delta:SF-2026-ARXIV-2605-17683:start -->microsecond inference requires overhead-aware execution planning across direct inter-layer links, synchronization and non-matmul operators<!-- delta:SF-2026-ARXIV-2605-17683:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17683:end -->
<!-- books-review:SF-2026-ARXIV-2605-17707:start -->
<!-- existing:SF-2026-ARXIV-2605-17707:start -->独立 reviewer 顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=b4a3cdb8a1a37d72b85afa4def5d2fd3756d9432a2a7ddd0c60732f5bdbf9c1d。<!-- existing:SF-2026-ARXIV-2605-17707:end -->
<!-- delta:SF-2026-ARXIV-2605-17707:start -->Edge AI accelerator 绕过 OS 语义隔离时可能成为 confused deputy；DMA/地址/权限验证必须进入 accelerator–driver contract，而不是只相信应用进程边界。<!-- delta:SF-2026-ARXIV-2605-17707:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17707:end -->
<!-- books-review:SF-2026-ARXIV-2605-17721:start -->
<!-- existing:SF-2026-ARXIV-2605-17721:start -->独立 reviewer 顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c6d90ee41a0332b99f4f0a78dc25c6253eb7c7cb12b4bb3769360926879e8751。<!-- existing:SF-2026-ARXIV-2605-17721:end -->
<!-- delta:SF-2026-ARXIV-2605-17721:start -->Self-evolving Agent 把成功/失败经验组织为 online/offline experience graph；结构化复用提高可用性，同时带来 provenance、staleness、错误传播与 graph lifecycle 成本。<!-- delta:SF-2026-ARXIV-2605-17721:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-17721:end -->
<!-- books-review:SF-2026-ARXIV-2605-18891:start -->
<!-- existing:SF-2026-ARXIV-2605-18891:start -->独立 reviewer 顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=8e594c3827c4a7778945dbe71f0c1af1ca4089918dcd0c8998ff54d98ac664a1。<!-- existing:SF-2026-ARXIV-2605-18891:end -->
<!-- delta:SF-2026-ARXIV-2605-18891:start -->reasoning-trace bypass gap 可能由 prefill/parser/format 造成，不能直接证明 weights 仍记忆；unlearning evaluation 必须冻结 parser、prompt head、seed 与 intervention identity。<!-- delta:SF-2026-ARXIV-2605-18891:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18891:end -->
<!-- books-review:SF-2026-ARXIV-2605-18899:start -->
<!-- existing:SF-2026-ARXIV-2605-18899:start -->独立 reviewer 顺读 `books/part-04-training-system/33-grpo.md` 与相邻章节 ['books/part-04-training-system/32-ppo.md', 'books/part-04-training-system/34-dpo.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=c75d66bc18a9221e70da0fc29018962765e69241af2ce0959becf0ab5f8e49a8。<!-- existing:SF-2026-ARXIV-2605-18899:end -->
<!-- delta:SF-2026-ARXIV-2605-18899:start -->continual policy updates bind logged-action propensity and ambiguous no-response feedback to the serving-policy revision<!-- delta:SF-2026-ARXIV-2605-18899:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-18899:end -->
<!-- books-review:SF-2026-ARXIV-2606-20591:start -->
<!-- existing:SF-2026-ARXIV-2606-20591:start -->独立 reviewer 顺读 `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节 ['books/part-05-inference-system/47-pagedattention.md', 'books/part-05-inference-system/49-tensorrt-llm.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=bfb06a6d85e69aad14c37ededa68ac94f05ffe7f93c83b38f16b16942be3acdc。<!-- existing:SF-2026-ARXIV-2606-20591:end -->
<!-- delta:SF-2026-ARXIV-2606-20591:start -->edge-cloud speculative decoding 的 draft length 是 communication delay 与 acceptance 的在线 optimal-stopping 控制量；网络状态估计失真时必须回退固定/短 draft。<!-- delta:SF-2026-ARXIV-2606-20591:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2606-20591:end -->
<!-- books-review:SF-2026-ARXIV-2605-23988:start -->
<!-- existing:SF-2026-ARXIV-2605-23988:start -->独立 reviewer 顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']。当前正文已覆盖一般机制；本项仍留下不可被现有论证替代的状态/控制/证据增量。 owner_sha256=c940481ca012303f984917615764a048e4a6742978fcb826524402093905481b。<!-- existing:SF-2026-ARXIV-2605-23988:end -->
<!-- delta:SF-2026-ARXIV-2605-23988:start -->split fine-tuning compresses activation tokens before transmission, coupling accuracy, uplink traffic, server compute and frozen-backbone identity<!-- delta:SF-2026-ARXIV-2605-23988:end --> Decision=`Integrate`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23988:end -->
<!-- books-review:SF-2026-ARXIV-2605-23993:start -->
<!-- existing:SF-2026-ARXIV-2605-23993:start -->独立 reviewer 顺读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md']。当前正文已覆盖一般机制；本项属于现有演进链的受限实现或重复证据，不另建 owner。 owner_sha256=e3eb726b0a302cf0dd2994ec6c50e1f6615e7bfee81edf9ca9bdbff7c78a6325。<!-- existing:SF-2026-ARXIV-2605-23993:end -->
<!-- delta:SF-2026-ARXIV-2605-23993:start -->a reproducible world-model substrate versions objective, action conditioning, latent state, rollout and evaluation rather than comparing entangled codebases<!-- delta:SF-2026-ARXIV-2605-23993:end --> Decision=`No Change — Existing Coverage`；独立 reviewer 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23993:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260518-COVERAGE | fresh-context:may2026-day03 | coverage | coverage:SRC-ARXIV:20260518 | none | 324/324 replay；26 false negatives 重开并完成 exact-v1 | passed |
| SA-20260518-EVIDENCE | fresh-context:may2026-day03 | evidence | review:SF-2026-ARXIV-2605-17222; review:SF-2026-ARXIV-2605-23993 | none | 52/52 exact-v1 locators 与 claim boundary 完整，blocked=0 | passed |
| SA-20260518-DEEP | fresh-context:may2026-day03 | deep_analysis_selection | analysis:DA-AGENT-SECURITY-TELEMETRY; analysis:DA-ROLLOUT-STALENESS; analysis:DA-LOSSLESS-KV | none | Top-3 按跨层 ownership/failure pressure 重选 | passed |
| SA-20260518-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17281; books-review:SF-2026-ARXIV-2605-23988 | none | post-write-semantic-audit.json：14/14 structure pass、14/14 semantic pass；8 项 prior finding 已逐项复验关闭 | passed |

## 8. Ignored Noise

272 项分母前 closure 保存在 `papers/2026/05/_sources/daily-20260518/screening-ledger-independent-final.json`；独立审计没有把领域相关性等同于长期系统增量。

## 9. Recommended Action

本日 Coverage、Evidence 与 Books Gate 已闭合；后续只在 primary source revision 或 owner contract 变化时重开相应 Source Family。

## 10. Repository Changes

- 新增 05-18 independent ledger、exact-v1 packet、Books comparison、最终 queue 与 fresh-context audit。
- 更新本日 README；未修改共享 Books，未 stage、commit 或 push。

## 11. Open Questions

- 无。本轮 8 项 finding 已在正文主线修复并通过逐项复验。
- 已通过：14/14 均完成 owner+adjacent 与完整语义复验。

## 12. Sources
- [Triple-Hoisted Baby-Step Giant-Step Linear Transformation over CKKS Homomorphic Encryption and Hardware Accelerator](https://arxiv.org/html/2605.17222v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Active Budget Allocation for Efficient Scaling Law Estimation via Surrogate-Guided Pruning](https://arxiv.org/html/2605.17234v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [From Runnable to Shippable: Multi-Agent Test-Driven Development for Generating Full-Stack Web Applications from Requirements](https://arxiv.org/html/2605.17242v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Fidelity Probes for Specification--Code Alignment](https://arxiv.org/html/2605.17246v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [LiteFrame: Efficient Vision Encoders Unlock Frame Scaling in Video LLMs](https://arxiv.org/html/2605.17260v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Is VLA Reasoning Faithful? Probing Safety of Chain-of-Causation in Autonomous Driving Models](https://arxiv.org/html/2605.17268v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Position: State-of-the-Art Claims Require State-of-the-Art Evidence](https://arxiv.org/html/2605.17273v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [ContractBench: Can LLM Agents Preserve Observation Contracts?](https://arxiv.org/html/2605.17281v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack](https://arxiv.org/html/2605.17288v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [LEAP: Learnable End-to-End Adaptive Pruning of Large Language Models](https://arxiv.org/html/2605.17289v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Step-wise Rubric Rewards for LLM Reasoning](https://arxiv.org/html/2605.17291v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [MetaCogAgent: A Metacognitive Multi-Agent LLM Framework with Self-Aware Task Delegation](https://arxiv.org/html/2605.17292v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retrieval Augmented Generation](https://arxiv.org/html/2605.17301v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Compress the Context, Keep the Commitments: A Formal Framework for Verifiable LLM Context Compression](https://arxiv.org/html/2605.17304v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models](https://arxiv.org/html/2605.17305v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [TClone: Low-Latency Forking of Live GUI Environments for Computer-Use Agents](https://arxiv.org/html/2605.17320v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents](https://arxiv.org/html/2605.17324v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [LPG: Balancing Efficiency and Policy Reasoning in Latent Policy Guardrails](https://arxiv.org/html/2605.17329v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Taming "Zombie'' Agents: A Markov State-Aware Framework for Resilient Multi-Agent Evolution](https://arxiv.org/html/2605.17348v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Omni-DuplexEval: Evaluating Real-time Duplex Omni-modal Interaction](https://arxiv.org/html/2605.17360v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [FML-bench: A Controlled Study of AI Research Agent Strategies from the Perspective of Search Dynamics](https://arxiv.org/html/2605.17373v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [ADR: An Agentic Detection System for Enterprise Agentic AI Security](https://arxiv.org/html/2605.17380v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [IVF-TQ: Calibration-Free Streaming Vector Search via a Codebook-Free Residual Layer](https://arxiv.org/html/2605.17415v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [DiagEval: Trajectory-Conditioned Diagnosis for Reliable Software Evaluation with GUI Agents](https://arxiv.org/html/2605.17439v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback](https://arxiv.org/html/2605.17453v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [VerifyMAS: Hypothesis Verification for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/html/2605.17467v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [WinQ: Accelerating Quantization-Aware Training of Language Models Around Saddle Points](https://arxiv.org/html/2605.17471v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [The Capability Paradox: How Smarter Auditors Make Multi-Agent Systems Less Secure](https://arxiv.org/html/2605.17480v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Self-Supervised On-Policy Distillation for Reasoning Language Models](https://arxiv.org/html/2605.17497v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [BESplit: Bias-Compensated Split Federated Learning with Evidential Aggregation](https://arxiv.org/html/2605.17508v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [RoboFlow4D: A Lightweight Flow World Model Toward Real-Time Flow-Guided Robotic Manipulation](https://arxiv.org/html/2605.17522v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Evaluating Deep Research Agents on Expert Consulting Work: A Benchmark with Verifiers, Rubrics, and Cognitive Traps](https://arxiv.org/html/2605.17554v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs](https://arxiv.org/html/2605.17558v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [How Off-Policy Can GRPO Be? Mu-GRPO for Efficient LLM Reinforcement Learning](https://arxiv.org/html/2605.17570v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Form and Function: Machine Unlearning as a Problem of Misaligned States](https://arxiv.org/html/2605.17590v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification](https://arxiv.org/html/2605.17609v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [SafeLens: Deliberate and Efficient Video Guardrails with Fast-and-Slow Screening](https://arxiv.org/html/2605.17610v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [VeriCache: Turning Lossy KV Cache into Lossless LLM Inference](https://arxiv.org/html/2605.17613v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [GraphMind: From Operational Traces to Self-Evolving Workflow Automation](https://arxiv.org/html/2605.17617v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents](https://arxiv.org/html/2605.17625v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [AI Agents May Always Fall for Prompt Injections](https://arxiv.org/html/2605.17634v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Causal Intervention-Based Memory Selection for Long-Horizon LLM Agents](https://arxiv.org/html/2605.17641v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Bug or Feature$^2$: Weight Drift, Activation Sparsity and Spikes](https://arxiv.org/html/2605.17659v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models](https://arxiv.org/html/2605.17672v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [μ-ORCA: Optimizing Acceleration for Microsecond-Scale Deep Neural Network Inference on ACAP](https://arxiv.org/html/2605.17683v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Speed Kills: Exploring Confused Deputy Attacks Through Edge AI Accelerators](https://arxiv.org/html/2605.17707v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [EXG: Self-Evolving Agents with Experience Graphs](https://arxiv.org/html/2605.17721v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Auditing Reasoning-Trace Memorization Claims after Unlearning with Head-Conditioned Canaries](https://arxiv.org/html/2605.18891v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Don't Let Bandit Feedback Pull Continual LLM-Recommender Updates Off Target](https://arxiv.org/html/2605.18899v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Delay-Adaptive Speculation Control for Low-Latency Edge-Cloud LLM Inference](https://arxiv.org/html/2606.20591v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [TSFLora: Token-Compressed Split Fine-Tuning for Wireless Edge Networks](https://arxiv.org/html/2605.23988v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01
- [Nano World Models: A Minimalist Implementation of Future Video Prediction](https://arxiv.org/html/2605.23993v1) — exact-v1；first-public 2026-05-17；accessed 2026-09-01

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

无：52/52 retained family 的 official exact-v1 已读取，blocked=0。

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

Coverage、Evidence 与 Books 均已闭合；14/14 Books Integration 通过独立 post-write semantic audit，未解决 finding 为零。
