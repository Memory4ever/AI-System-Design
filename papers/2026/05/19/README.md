# Daily Research — 2026-05-19

**Research Date:** 2026-05-19

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-18 09:00:00 ～ 2026-05-19 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML/PDF。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。第三轮 post-write audit 已逐项顺读 18/18：owner、相邻章、exact-v1 boundary、章内演进与退出契约均通过，unresolved=0。

## Executive Summary

独立 reviewer 重放 703/703 个 registered identities：author denominator 46 中移除 20 个 false positive，恢复 34 个 false negative，最终 denominator=60、pre-denominator closures=643。60/60 exact-v1 Review 完成，blocked=0、ordinary pending=0；31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项并已写回。第三轮 post-write audit 逐项顺读前一段、机制段、后一段与更新后小结：18/18 位于 canonical H2 的直接演进链中，owner、相邻章、机制字段、exact-v1 boundary、fallback/coexistence 与退出契约均通过；Books Gate 已关闭。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-19 |
| Window End | 2026-05-19 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260519-V2-INDEPENDENT |
| Denominator Frozen At | 2026-09-01T23:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-18T09:00:00+08:00 | 2026-05-19T09:00:00+08:00 | 2026-09-01T23:20:00+08:00 | DataCite v2 00..99 + 703/703 independent semantic replay + official exact-v1 HTML | checked | 703 | SF-2026-ARXIV-2605-17734;SF-2026-ARXIV-2605-17757;SF-2026-ARXIV-2605-17787;SF-2026-ARXIV-2605-17821;SF-2026-ARXIV-2605-17830;SF-2026-ARXIV-2605-17842;SF-2026-ARXIV-2605-17849;SF-2026-ARXIV-2605-17862;SF-2026-ARXIV-2605-17877;SF-2026-ARXIV-2605-17879;SF-2026-ARXIV-2605-17889;SF-2026-ARXIV-2605-17912;SF-2026-ARXIV-2605-17921;SF-2026-ARXIV-2605-17923;SF-2026-ARXIV-2605-17932;SF-2026-ARXIV-2605-17954;SF-2026-ARXIV-2605-17986;SF-2026-ARXIV-2605-17989;SF-2026-ARXIV-2605-17992;SF-2026-ARXIV-2605-17998;SF-2026-ARXIV-2605-18032;SF-2026-ARXIV-2605-18041;SF-2026-ARXIV-2605-18053;SF-2026-ARXIV-2605-18067;SF-2026-ARXIV-2605-18071;SF-2026-ARXIV-2605-18106;SF-2026-ARXIV-2605-18165;SF-2026-ARXIV-2605-18271;SF-2026-ARXIV-2605-18401;SF-2026-ARXIV-2605-18414;SF-2026-ARXIV-2605-18421;SF-2026-ARXIV-2605-18498;SF-2026-ARXIV-2605-18565;SF-2026-ARXIV-2605-18583;SF-2026-ARXIV-2605-18607;SF-2026-ARXIV-2605-18652;SF-2026-ARXIV-2605-18693;SF-2026-ARXIV-2605-18697;SF-2026-ARXIV-2605-18703;SF-2026-ARXIV-2605-18710;SF-2026-ARXIV-2605-18739;SF-2026-ARXIV-2605-18750;SF-2026-ARXIV-2605-18918;SF-2026-ARXIV-2605-18930;SF-2026-ARXIV-2605-18991;SF-2026-ARXIV-2605-19008;SF-2026-ARXIV-2605-19049;SF-2026-ARXIV-2605-19099;SF-2026-ARXIV-2605-19101;SF-2026-ARXIV-2605-19127;SF-2026-ARXIV-2605-19140;SF-2026-ARXIV-2605-19151;SF-2026-ARXIV-2605-19169;SF-2026-ARXIV-2605-19192;SF-2026-ARXIV-2605-19193;SF-2026-ARXIV-2605-19196;SF-2026-ARXIV-2605-19218;SF-2026-ARXIV-2605-19228;SF-2026-ARXIV-2605-20251;SF-2026-ARXIV-2605-20270 | pages=300;final_cursor=end;raw=91841;registered=703;screened=703;retained=60;closure=643 | 2026-05-19T00:59:59Z | screening-ledger-final.json#sha256=3843e4062f272925bb77d04a5b9f312522c996299611a03e513f92ba3bfc6fc4 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260519:start -->703/703 identity 的 title+abstract 已由不同 reviewer 重放；20 FP 与 34 FN 已逐 family reconciliation。Coverage 不以 Books 写回为前提，当前无未决 source-discovery finding。<!-- coverage:SRC-ARXIV:20260519:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17734 | arXiv:2605.17734v1 | paper-v1:2605.17734 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17734 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17734 | no |
| SF-2026-ARXIV-2605-17757 | arXiv:2605.17757v1 | paper-v1:2605.17757 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17757 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17757 | no |
| SF-2026-ARXIV-2605-17787 | arXiv:2605.17787v1 | paper-v1:2605.17787 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17787 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17787 | no |
| SF-2026-ARXIV-2605-17821 | arXiv:2605.17821v1 | paper-v1:2605.17821 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17821 | self | — | new_in_window | TRAIN-CHECKPOINT | Integrate | books-review:SF-2026-ARXIV-2605-17821 | no |
| SF-2026-ARXIV-2605-17830 | arXiv:2605.17830v1 | paper-v1:2605.17830 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17830 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17830 | no |
| SF-2026-ARXIV-2605-17842 | arXiv:2605.17842v1 | paper-v1:2605.17842 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17842 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17842 | no |
| SF-2026-ARXIV-2605-17849 | arXiv:2605.17849v1 | paper-v1:2605.17849 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17849 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17849 | no |
| SF-2026-ARXIV-2605-17862 | arXiv:2605.17862v1 | paper-v1:2605.17862 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17862 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-17862 | no |
| SF-2026-ARXIV-2605-17877 | arXiv:2605.17877v1 | paper-v1:2605.17877 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17877 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2605-17877 | no |
| SF-2026-ARXIV-2605-17879 | arXiv:2605.17879v1 | paper-v1:2605.17879 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17879 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-17879 | no |
| SF-2026-ARXIV-2605-17889 | arXiv:2605.17889v1 | paper-v1:2605.17889 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17889 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2605-17889 | no |
| SF-2026-ARXIV-2605-17912 | arXiv:2605.17912v1 | paper-v1:2605.17912 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17912 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17912 | no |
| SF-2026-ARXIV-2605-17921 | arXiv:2605.17921v1 | paper-v1:2605.17921 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17921 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17921 | no |
| SF-2026-ARXIV-2605-17923 | arXiv:2605.17923v1 | paper-v1:2605.17923 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17923 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-17923 | no |
| SF-2026-ARXIV-2605-17932 | arXiv:2605.17932v1 | paper-v1:2605.17932 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17932 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17932 | no |
| SF-2026-ARXIV-2605-17954 | arXiv:2605.17954v1 | paper-v1:2605.17954 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17954 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17954 | no |
| SF-2026-ARXIV-2605-17986 | arXiv:2605.17986v1 | paper-v1:2605.17986 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-17986 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17986 | no |
| SF-2026-ARXIV-2605-17989 | arXiv:2605.17989v1 | paper-v1:2605.17989 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17989 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-17989 | no |
| SF-2026-ARXIV-2605-17992 | arXiv:2605.17992v1 | paper-v1:2605.17992 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17992 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-17992 | no |
| SF-2026-ARXIV-2605-17998 | arXiv:2605.17998v1 | paper-v1:2605.17998 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-17998 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-17998 | no |
| SF-2026-ARXIV-2605-18032 | arXiv:2605.18032v1 | paper-v1:2605.18032 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18032 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18032 | no |
| SF-2026-ARXIV-2605-18041 | arXiv:2605.18041v1 | paper-v1:2605.18041 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-18041 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18041 | no |
| SF-2026-ARXIV-2605-18053 | arXiv:2605.18053v1 | paper-v1:2605.18053 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18053 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-18053 | no |
| SF-2026-ARXIV-2605-18067 | arXiv:2605.18067v1 | paper-v1:2605.18067 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18067 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18067 | no |
| SF-2026-ARXIV-2605-18071 | arXiv:2605.18071v1 | paper-v1:2605.18071 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18071 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18071 | no |
| SF-2026-ARXIV-2605-18106 | arXiv:2605.18106v1 | paper-v1:2605.18106 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18106 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-18106 | no |
| SF-2026-ARXIV-2605-18165 | arXiv:2605.18165v1 | paper-v1:2605.18165 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18165 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18165 | no |
| SF-2026-ARXIV-2605-18271 | arXiv:2605.18271v1 | paper-v1:2605.18271 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18271 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18271 | no |
| SF-2026-ARXIV-2605-18401 | arXiv:2605.18401v1 | paper-v1:2605.18401 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18401 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18401 | no |
| SF-2026-ARXIV-2605-18414 | arXiv:2605.18414v1 | paper-v1:2605.18414 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18414 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18414 | no |
| SF-2026-ARXIV-2605-18421 | arXiv:2605.18421v1 | paper-v1:2605.18421 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18421 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18421 | no |
| SF-2026-ARXIV-2605-18498 | arXiv:2605.18498v1 | paper-v1:2605.18498 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18498 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-18498 | no |
| SF-2026-ARXIV-2605-18565 | arXiv:2605.18565v1 | paper-v1:2605.18565 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18565 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-18565 | no |
| SF-2026-ARXIV-2605-18583 | arXiv:2605.18583v1 | paper-v1:2605.18583 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18583 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18583 | no |
| SF-2026-ARXIV-2605-18607 | arXiv:2605.18607v1 | paper-v1:2605.18607 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18607 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18607 | no |
| SF-2026-ARXIV-2605-18652 | arXiv:2605.18652v1 | paper-v1:2605.18652 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18652 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18652 | no |
| SF-2026-ARXIV-2605-18693 | arXiv:2605.18693v1 | paper-v1:2605.18693 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18693 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18693 | no |
| SF-2026-ARXIV-2605-18697 | arXiv:2605.18697v1 | paper-v1:2605.18697 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18697 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18697 | no |
| SF-2026-ARXIV-2605-18703 | arXiv:2605.18703v1 | paper-v1:2605.18703 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18703 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18703 | no |
| SF-2026-ARXIV-2605-18710 | arXiv:2605.18710v1 | paper-v1:2605.18710 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18710 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-18710 | no |
| SF-2026-ARXIV-2605-18739 | arXiv:2605.18739v1 | paper-v1:2605.18739 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18739 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18739 | no |
| SF-2026-ARXIV-2605-18750 | arXiv:2605.18750v1 | paper-v1:2605.18750 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-18750 | self | — | new_in_window | TRAIN-PIPELINE-PARALLEL | Integrate | books-review:SF-2026-ARXIV-2605-18750 | no |
| SF-2026-ARXIV-2605-18918 | arXiv:2605.18918v1 | paper-v1:2605.18918 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18918 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18918 | no |
| SF-2026-ARXIV-2605-18930 | arXiv:2605.18930v1 | paper-v1:2605.18930 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18930 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18930 | no |
| SF-2026-ARXIV-2605-18991 | arXiv:2605.18991v1 | paper-v1:2605.18991 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-18991 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18991 | no |
| SF-2026-ARXIV-2605-19008 | arXiv:2605.19008v1 | paper-v1:2605.19008 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19008 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2605-19008 | no |
| SF-2026-ARXIV-2605-19049 | arXiv:2605.19049v1 | paper-v1:2605.19049 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-19049 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-19049 | no |
| SF-2026-ARXIV-2605-19099 | arXiv:2605.19099v1 | paper-v1:2605.19099 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19099 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19099 | no |
| SF-2026-ARXIV-2605-19101 | arXiv:2605.19101v1 | paper-v1:2605.19101 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19101 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19101 | no |
| SF-2026-ARXIV-2605-19127 | arXiv:2605.19127v1 | paper-v1:2605.19127 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19127 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19127 | no |
| SF-2026-ARXIV-2605-19140 | arXiv:2605.19140v1 | paper-v1:2605.19140 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19140 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19140 | no |
| SF-2026-ARXIV-2605-19151 | arXiv:2605.19151v1 | paper-v1:2605.19151 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19151 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19151 | no |
| SF-2026-ARXIV-2605-19169 | arXiv:2605.19169v1 | paper-v1:2605.19169 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19169 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19169 | no |
| SF-2026-ARXIV-2605-19192 | arXiv:2605.19192v1 | paper-v1:2605.19192 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19192 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19192 | no |
| SF-2026-ARXIV-2605-19193 | arXiv:2605.19193v1 | paper-v1:2605.19193 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19193 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19193 | no |
| SF-2026-ARXIV-2605-19196 | arXiv:2605.19196v1 | paper-v1:2605.19196 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19196 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19196 | no |
| SF-2026-ARXIV-2605-19218 | arXiv:2605.19218v1 | paper-v1:2605.19218 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19218 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19218 | no |
| SF-2026-ARXIV-2605-19228 | arXiv:2605.19228v1 | paper-v1:2605.19228 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-19228 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-19228 | no |
| SF-2026-ARXIV-2605-20251 | arXiv:2605.20251v1 | paper-v1:2605.20251 | 2026-W21 | 2026-05-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20251 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20251 | no |
| SF-2026-ARXIV-2605-20270 | arXiv:2605.20270v1 | paper-v1:2605.20270 | 2026-W21 | 2026-05-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-20270 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20270 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17734 | RP-a0b5b8edab9b2319 | deep | arXiv:2605.17734v1 | SRC-ARXIV@arXiv:2605.17734v1 | arXiv:2605.17734v1 HTML — §3.1–3.3 Program Functions | arXiv:2605.17734v1 HTML — §4.1–4.2 Experiments | arXiv:2605.17734v1 HTML — Appendix A Limitations | arXiv:2605.17734v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17734 | complete |
| SF-2026-ARXIV-2605-17757 | RP-5ffb4a0509895ab1 | deep | arXiv:2605.17757v1 | SRC-ARXIV@arXiv:2605.17757v1 | arXiv:2605.17757v1 HTML — §3 OSCAR; §3.1–3.4 offline covariance-aware rotation and mixed K/V layout | arXiv:2605.17757v1 HTML — §4 Experiments; §4.1–4.5 quality, memory and kernel latency | arXiv:2605.17757v1 HTML — Appendix D Limitations | arXiv:2605.17757v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17757 | complete |
| SF-2026-ARXIV-2605-17787 | RP-b65fc9d1cab0fc01 | deep | arXiv:2605.17787v1 | SRC-ARXIV@arXiv:2605.17787v1 | arXiv:2605.17787v1 HTML — §3 Training Dynamics; §4.1–4.2 clipping | arXiv:2605.17787v1 HTML — Appendix B–C settings and ablations | arXiv:2605.17787v1 HTML — §5 Conclusions; Appendix C.4 seeds | arXiv:2605.17787v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17787 | complete |
| SF-2026-ARXIV-2605-17821 | RP-19ab22f616f4d751 | deep | arXiv:2605.17821v1 | SRC-ARXIV@arXiv:2605.17821v1 | arXiv:2605.17821v1 HTML — §3 TierCheck Design; §3.1 save/retrieve/reclaim across local, peer and remote tiers | arXiv:2605.17821v1 HTML — §5 Evaluation; failure frequency, checkpoint overhead and recovery | arXiv:2605.17821v1 HTML — §7 Conclusion; no dedicated limitations section, production failure correlation Not Disclosed | arXiv:2605.17821v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17821 | complete |
| SF-2026-ARXIV-2605-17830 | RP-22d5f6d458a04b87 | deep | arXiv:2605.17830v1 | SRC-ARXIV@arXiv:2605.17830v1 | arXiv:2605.17830v1 HTML — §3.1–3.5 stateful setting and monitor | arXiv:2605.17830v1 HTML — §4 protocol; §5 results | arXiv:2605.17830v1 HTML — §6 Discussion and limitations | arXiv:2605.17830v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17830 | complete |
| SF-2026-ARXIV-2605-17842 | RP-6f3e2305afb21987 | deep | arXiv:2605.17842v1 | SRC-ARXIV@arXiv:2605.17842v1 | arXiv:2605.17842v1 HTML — §3.2–3.5 Structured Newton Layer Parallelism | arXiv:2605.17842v1 HTML — §5.1–5.3 experiments | arXiv:2605.17842v1 HTML — §6 Limitations | arXiv:2605.17842v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17842 | complete |
| SF-2026-ARXIV-2605-17849 | RP-782a8edd284bb7a0 | deep | arXiv:2605.17849v1 | SRC-ARXIV@arXiv:2605.17849v1 | arXiv:2605.17849v1 HTML — §3.1–3.3 model-aware synthesis | arXiv:2605.17849v1 HTML — §4 experiments and analyses | arXiv:2605.17849v1 HTML — §5 limitations | arXiv:2605.17849v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17849 | complete |
| SF-2026-ARXIV-2605-17862 | RP-252dab091f3d839c | deep | arXiv:2605.17862v1 | SRC-ARXIV@arXiv:2605.17862v1 | arXiv:2605.17862v1 HTML — §3.1–3.3 drift decomposition; §4 freshness control | arXiv:2605.17862v1 HTML — §5.1–5.4 experiments | arXiv:2605.17862v1 HTML — §6 limitations | arXiv:2605.17862v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17862 | complete |
| SF-2026-ARXIV-2605-17877 | RP-0dcd3afd9fbbf4dc | deep | arXiv:2605.17877v1 | SRC-ARXIV@arXiv:2605.17877v1 | arXiv:2605.17877v1 HTML — §3 PAIR; prefix-aware dense reward construction and intervention | arXiv:2605.17877v1 HTML — §4 Experiments; multi-turn agent optimization and ablations | arXiv:2605.17877v1 HTML — Appendix J Limitations | arXiv:2605.17877v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17877 | complete |
| SF-2026-ARXIV-2605-17879 | RP-24e57c07b3182fda | deep | arXiv:2605.17879v1 | SRC-ARXIV@arXiv:2605.17879v1 | arXiv:2605.17879v1 HTML — §3–§6 Guard architecture; online monitor, offline node sweep and triage | arXiv:2605.17879v1 HTML — §7 Evaluation; fail-slow detection, false positives and cluster overhead | arXiv:2605.17879v1 HTML — §7–§8 claim boundary; no dedicated limitations section | arXiv:2605.17879v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17879 | complete |
| SF-2026-ARXIV-2605-17889 | RP-ceff824f43de350b | deep | arXiv:2605.17889v1 | SRC-ARXIV@arXiv:2605.17889v1 | arXiv:2605.17889v1 HTML — §3 Motivation; §4.1–4.2 orchestration | arXiv:2605.17889v1 HTML — §5 evaluation | arXiv:2605.17889v1 HTML — §6 discussion and limitations | arXiv:2605.17889v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17889 | complete |
| SF-2026-ARXIV-2605-17912 | RP-6f71c93a50fcb2bb | deep | arXiv:2605.17912v1 | SRC-ARXIV@arXiv:2605.17912v1 | arXiv:2605.17912v1 HTML — §3 WorldArena 2.0 benchmark axes and task construction | arXiv:2605.17912v1 HTML — §4 Experiments across modality, functionality and platform | arXiv:2605.17912v1 HTML — §5 Discussion/Conclusion; simulator and selected-model boundary | arXiv:2605.17912v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17912 | complete |
| SF-2026-ARXIV-2605-17921 | RP-a02c424b3c54be6f | deep | arXiv:2605.17921v1 | SRC-ARXIV@arXiv:2605.17921v1 | arXiv:2605.17921v1 HTML — §3–§4 R3-Streaming cascaded memory, readiness and compute routing | arXiv:2605.17921v1 HTML — §5 Experiments; latency/accuracy under streaming video workloads | arXiv:2605.17921v1 HTML — §6 Conclusion; no production tail-SLO or failure-recovery evidence | arXiv:2605.17921v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17921 | complete |
| SF-2026-ARXIV-2605-17923 | RP-5e997a97976986cb | deep | arXiv:2605.17923v1 | SRC-ARXIV@arXiv:2605.17923v1 | arXiv:2605.17923v1 HTML — §3 AdaptiveLoad; dual memory/compute constrained batch construction and fused execution | arXiv:2605.17923v1 HTML — §4 Experiments on video diffusion training | arXiv:2605.17923v1 HTML — §5 Conclusion/limitations; selected models and hardware only | arXiv:2605.17923v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17923 | complete |
| SF-2026-ARXIV-2605-17932 | RP-a5dd7c7800d2dfa1 | deep | arXiv:2605.17932v1 | SRC-ARXIV@arXiv:2605.17932v1 | arXiv:2605.17932v1 HTML — §III-A–C compression pipeline | arXiv:2605.17932v1 HTML — §III-D; §IV-A–C | arXiv:2605.17932v1 HTML — §V Discussion; §VII Future Work | arXiv:2605.17932v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17932 | complete |
| SF-2026-ARXIV-2605-17954 | RP-01379cd993382ecb | deep | arXiv:2605.17954v1 | SRC-ARXIV@arXiv:2605.17954v1 | arXiv:2605.17954v1 HTML — §2 motivation; §3.1–3.4 tokenization | arXiv:2605.17954v1 HTML — §4.1–4.4 experiments | arXiv:2605.17954v1 HTML — §5 limitations | arXiv:2605.17954v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17954 | complete |
| SF-2026-ARXIV-2605-17986 | RP-e92ff8a8f642e82b | deep | arXiv:2605.17986v1 | SRC-ARXIV@arXiv:2605.17986v1 | arXiv:2605.17986v1 HTML — §3 Threat model and benchmark construction | arXiv:2605.17986v1 HTML — §4–§5 evaluation and defense analysis across live interaction surfaces | arXiv:2605.17986v1 HTML — §6 Limitations | arXiv:2605.17986v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17986 | complete |
| SF-2026-ARXIV-2605-17989 | RP-6f92f00df0a7d022 | deep | arXiv:2605.17989v1 | SRC-ARXIV@arXiv:2605.17989v1 | arXiv:2605.17989v1 HTML — §3 Predictive prefetch controller and retrieval-generation overlap | arXiv:2605.17989v1 HTML — §4 Evaluation; latency, retrieval usefulness and prediction error | arXiv:2605.17989v1 HTML — §6 Limitations; stale/incorrect demand and workload boundary | arXiv:2605.17989v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17989 | complete |
| SF-2026-ARXIV-2605-17992 | RP-d500e8299cf252c6 | deep | arXiv:2605.17992v1 | SRC-ARXIV@arXiv:2605.17992v1 | arXiv:2605.17992v1 HTML — §3 PipeANN-Filter superset traversal, post-verification and pipelined SSD IO | arXiv:2605.17992v1 HTML — §4–§5 implementation and filtered-ANN evaluation | arXiv:2605.17992v1 HTML — §6 Limitations; index/filter/update boundary | arXiv:2605.17992v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17992 | complete |
| SF-2026-ARXIV-2605-17998 | RP-1e8793fab16b7d56 | deep | arXiv:2605.17998v1 | SRC-ARXIV@arXiv:2605.17998v1 | arXiv:2605.17998v1 HTML — §3–§8 read-only verifier, proposal/admission state and bounded completion protocol | arXiv:2605.17998v1 HTML — §9–§10 architecture case study and failure injection | arXiv:2605.17998v1 HTML — §12 Limitations; bounded case study, not a universal correctness proof | arXiv:2605.17998v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-17998 | complete |
| SF-2026-ARXIV-2605-18032 | RP-1c13034dd3b4c092 | deep | arXiv:2605.18032v1 | SRC-ARXIV@arXiv:2605.18032v1 | arXiv:2605.18032v1 HTML — §2 architecture; §3.1–3.3 node diagnosis | arXiv:2605.18032v1 HTML — §4.1–4.3 evaluation | arXiv:2605.18032v1 HTML — §5 Conclusion | arXiv:2605.18032v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18032 | complete |
| SF-2026-ARXIV-2605-18041 | RP-a017770fe83edc69 | standard | arXiv:2605.18041v1 | SRC-ARXIV@arXiv:2605.18041v1 | arXiv:2605.18041v1 HTML — §3 OmniSelect modality-aware token-budget controller | arXiv:2605.18041v1 HTML — §4 Experiments on audio-video OmniLLMs | arXiv:2605.18041v1 HTML — §5 Limitations; model/task-local compression evidence | arXiv:2605.18041v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18041 | complete |
| SF-2026-ARXIV-2605-18053 | RP-d13fb94bd59cda38 | deep | arXiv:2605.18053v1 | SRC-ARXIV@arXiv:2605.18053v1 | arXiv:2605.18053v1 HTML — §3–§7 globally capped KV eviction and structural boundary protection | arXiv:2605.18053v1 HTML — §8–§9 evaluation across policies/models and cross-architecture challenge | arXiv:2605.18053v1 HTML — §10.22 Limitations | arXiv:2605.18053v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18053 | complete |
| SF-2026-ARXIV-2605-18067 | RP-ed48c39e12ae07f7 | deep | arXiv:2605.18067v1 | SRC-ARXIV@arXiv:2605.18067v1 | arXiv:2605.18067v1 HTML — §IV–VI agent scoring and serving game | arXiv:2605.18067v1 HTML — §VIII implementation and experiments | arXiv:2605.18067v1 HTML — §VII Discussion | arXiv:2605.18067v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18067 | complete |
| SF-2026-ARXIV-2605-18071 | RP-1810f220fe28004a | deep | arXiv:2605.18071v1 | SRC-ARXIV@arXiv:2605.18071v1 | arXiv:2605.18071v1 HTML — §4–§7 multi-tier KV design | arXiv:2605.18071v1 HTML — §9.1–9.3 experiments | arXiv:2605.18071v1 HTML — §10–§11 conclusion and future work | arXiv:2605.18071v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18071 | complete |
| SF-2026-ARXIV-2605-18106 | RP-a0c3c051241d947a | deep | arXiv:2605.18106v1 | SRC-ARXIV@arXiv:2605.18106v1 | arXiv:2605.18106v1 HTML — §3–§5 symmetry-compatible optimizer design | arXiv:2605.18106v1 HTML — §6 experiments | arXiv:2605.18106v1 HTML — §1 Scope and limitations; §7 discussion | arXiv:2605.18106v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18106 | complete |
| SF-2026-ARXIV-2605-18165 | RP-bbf05cdd370c502d | deep | arXiv:2605.18165v1 | SRC-ARXIV@arXiv:2605.18165v1 | arXiv:2605.18165v1 HTML — §3 mask state; §4.1–4.3 compression | arXiv:2605.18165v1 HTML — §5.1–5.4 experiments | arXiv:2605.18165v1 HTML — §6 limitations | arXiv:2605.18165v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18165 | complete |
| SF-2026-ARXIV-2605-18271 | RP-b618e263c39bbaf0 | deep | arXiv:2605.18271v1 | SRC-ARXIV@arXiv:2605.18271v1 | arXiv:2605.18271v1 HTML — PDF pp.3–5 §3.1–3.3 memory construction | arXiv:2605.18271v1 HTML — PDF §4–§5; device experiments | arXiv:2605.18271v1 HTML — PDF §6 Limitations | arXiv:2605.18271v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18271 | complete |
| SF-2026-ARXIV-2605-18401 | RP-0e10991beabfb448 | deep | arXiv:2605.18401v1 | SRC-ARXIV@arXiv:2605.18401v1 | arXiv:2605.18401v1 HTML — §3 SkillsVote collection, recommendation, validation and evolution lifecycle | arXiv:2605.18401v1 HTML — §4 Experiments and lifecycle ablations | arXiv:2605.18401v1 HTML — §5/Appendix limitations; ecosystem and environment sensitivity | arXiv:2605.18401v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18401 | complete |
| SF-2026-ARXIV-2605-18414 | RP-feb9599fea2d9335 | deep | arXiv:2605.18414v1 | SRC-ARXIV@arXiv:2605.18414v1 | arXiv:2605.18414v1 HTML — §3 governed MCP proxy | arXiv:2605.18414v1 HTML — §4–§5 benchmark and results | arXiv:2605.18414v1 HTML — §6–§7 discussion and threat-model limits | arXiv:2605.18414v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18414 | complete |
| SF-2026-ARXIV-2605-18421 | RP-833f930afb3c701a | deep | arXiv:2605.18421v1 | SRC-ARXIV@arXiv:2605.18421v1 | arXiv:2605.18421v1 HTML — §3–§4 EvoMemBench in/cross-episode and knowledge/execution axes | arXiv:2605.18421v1 HTML — §5 Experiments across memory systems | arXiv:2605.18421v1 HTML — §6 Conclusion; benchmark/model coverage boundary | arXiv:2605.18421v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18421 | complete |
| SF-2026-ARXIV-2605-18498 | RP-18a67d9e5ec45674 | deep | arXiv:2605.18498v1 | SRC-ARXIV@arXiv:2605.18498v1 | arXiv:2605.18498v1 HTML — PDF pp.3–5 §3 routing-specialization metrics | arXiv:2605.18498v1 HTML — PDF pp.5–11 §4 experiments and intervention | arXiv:2605.18498v1 HTML — PDF p.11 §4.3 intervention boundary; §5 Conclusion | arXiv:2605.18498v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18498 | complete |
| SF-2026-ARXIV-2605-18565 | RP-1e362dd51e3c4598 | deep | arXiv:2605.18565v1 | SRC-ARXIV@arXiv:2605.18565v1 | arXiv:2605.18565v1 HTML — §3 MINTEval multi-target interference construction and update semantics | arXiv:2605.18565v1 HTML — §4 Experiments; recall and aggregation under evolving memories | arXiv:2605.18565v1 HTML — §5 Limitations; synthetic tasks and selected agents | arXiv:2605.18565v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18565 | complete |
| SF-2026-ARXIV-2605-18583 | RP-58c5225348983c36 | deep | arXiv:2605.18583v1 | SRC-ARXIV@arXiv:2605.18583v1 | arXiv:2605.18583v1 HTML — §3 benchmark, benign task scope and overeager-action taxonomy | arXiv:2605.18583v1 HTML — §4 Experiments across coding agents | arXiv:2605.18583v1 HTML — §5 Limitations; harness and observable-action boundary | arXiv:2605.18583v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18583 | complete |
| SF-2026-ARXIV-2605-18607 | RP-05c7d985e620ad3c | deep | arXiv:2605.18607v1 | SRC-ARXIV@arXiv:2605.18607v1 | arXiv:2605.18607v1 HTML — §3 proxy metrics | arXiv:2605.18607v1 HTML — §4–§5 model/data ranking | arXiv:2605.18607v1 HTML — §6 limitations | arXiv:2605.18607v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18607 | complete |
| SF-2026-ARXIV-2605-18652 | RP-fb32c4b5d2bfc297 | deep | arXiv:2605.18652v1 | SRC-ARXIV@arXiv:2605.18652v1 | arXiv:2605.18652v1 HTML — §3 MementoGUI multimodal memory controller and write/read policy | arXiv:2605.18652v1 HTML — §4–§5 benchmark construction and experiments | arXiv:2605.18652v1 HTML — §6 Limitations; GUI domain and selected backbones | arXiv:2605.18652v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18652 | complete |
| SF-2026-ARXIV-2605-18693 | RP-8ced56893e741499 | deep | arXiv:2605.18693v1 | SRC-ARXIV@arXiv:2605.18693v1 | arXiv:2605.18693v1 HTML — §3.1–3.4 skill-generation artifact contract | arXiv:2605.18693v1 HTML — §4.1–4.4 execution evaluation | arXiv:2605.18693v1 HTML — §5 Conclusion; appendix sensitivity | arXiv:2605.18693v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18693 | complete |
| SF-2026-ARXIV-2605-18697 | RP-276218662ac669c8 | deep | arXiv:2605.18697v1 | SRC-ARXIV@arXiv:2605.18697v1 | arXiv:2605.18697v1 HTML — §3–§6 PopPy compiler/runtime dependency discovery and external-call parallelism | arXiv:2605.18697v1 HTML — §8 Evaluation; latency and semantic-equivalence checks | arXiv:2605.18697v1 HTML — §10 Discussion; Python/compound-application boundary | arXiv:2605.18697v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18697 | complete |
| SF-2026-ARXIV-2605-18703 | RP-8a546d8bff6fd339 | deep | arXiv:2605.18703v1 | SRC-ARXIV@arXiv:2605.18703v1 | arXiv:2605.18703v1 HTML — §3–§4 executable-environment synthesis, verification and RL data path | arXiv:2605.18703v1 HTML — §5 Evaluation of environment validity and agent training | arXiv:2605.18703v1 HTML — §6 Limitations | arXiv:2605.18703v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18703 | complete |
| SF-2026-ARXIV-2605-18710 | RP-c006e759b41b9bff | deep | arXiv:2605.18710v1 | SRC-ARXIV@arXiv:2605.18710v1 | arXiv:2605.18710v1 HTML — §3 Mosaic spatial resource multiplexing, placement and performance model | arXiv:2605.18710v1 HTML — §4 Evaluation across multimodal module mixtures | arXiv:2605.18710v1 HTML — §5 Limitations; selected architectures/hardware | arXiv:2605.18710v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18710 | complete |
| SF-2026-ARXIV-2605-18739 | RP-6890bac3cb8945fc | deep | arXiv:2605.18739v1 | SRC-ARXIV@arXiv:2605.18739v1 | arXiv:2605.18739v1 HTML — §3–§4 NVFP4 training/inference infrastructure and parallel layouts | arXiv:2605.18739v1 HTML — §5 Evaluation on long-video generation | arXiv:2605.18739v1 HTML — §6 Limitations; vendor precision and workload boundary | arXiv:2605.18739v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18739 | complete |
| SF-2026-ARXIV-2605-18750 | RP-6c2b5f23f488451e | deep | arXiv:2605.18750v1 | SRC-ARXIV@arXiv:2605.18750v1 | arXiv:2605.18750v1 HTML — §3 readiness-driven runtime and dependency state | arXiv:2605.18750v1 HTML — §4–§5 implementation and evaluation under runtime variability | arXiv:2605.18750v1 HTML — §6 Limitations; schedule/hardware/workload boundary | arXiv:2605.18750v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-18750 | complete |
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
| SF-2026-ARXIV-2605-20251 | RP-070441416d60c224 | deep | arXiv:2605.20251v1 | SRC-ARXIV@arXiv:2605.20251v1 | arXiv:2605.20251v1 HTML — §3.1–3.5 trajectory/control contract | arXiv:2605.20251v1 HTML — §4.1–4.5 experiments | arXiv:2605.20251v1 HTML — §5 Limitations and Conclusion | arXiv:2605.20251v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-20251 | complete |
| SF-2026-ARXIV-2605-20270 | RP-15488bfb8700e030 | deep | arXiv:2605.20270v1 | SRC-ARXIV@arXiv:2605.20270v1 | arXiv:2605.20270v1 HTML — §1–§4 deployment contract and e-process | arXiv:2605.20270v1 HTML — §5–§7 proofs and 650-stream evaluation | arXiv:2605.20270v1 HTML — §8 limitations and boundary | arXiv:2605.20270v1 artifact links; immutable commit Not Disclosed unless stated in exact-v1 | claim:SF-2026-ARXIV-2605-20270 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-17734:start -->
#### Harnessing LLM Agents with Skill Programs

**问题与机制。** To bridge the gap, we introduce HASP(Harnessing LLM Agents with Skill Programs), a new framework that upgrades skills into executable Program Functions (PFs). 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 Program Functions`；Evaluation=`§4.1–4.2 Experiments`；Limitations/Counterevidence=`Appendix A Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17734:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17734:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17734:end -->

<!-- review:SF-2026-ARXIV-2605-17757:start -->
#### OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization

**问题与机制。** We propose OSCAR, an Ultra-low-bit KV Cache quantization method that estimates attention-aware covariance structures offline and uses them to derive fixed rotations and clipping thresholds for quantization. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 OSCAR; §3.1–3.4 offline covariance-aware rotation and mixed K/V layout`；Evaluation=`§4 Experiments; §4.1–4.5 quality, memory and kernel latency`；Limitations/Counterevidence=`Appendix D Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17757:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17757:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17757:end -->

<!-- review:SF-2026-ARXIV-2605-17787:start -->
#### Revisiting the Adam-SGD Gap in LLM Pre-Training: The Role of Large Effective Learning Rates

**问题与机制。** Through empirical and theoretical analysis of LLM pre-training dynamics, we identify that training is characterized by small gradient norms and large weight-to-gradient ratios, an effect that becomes more pronounced with larger batch sizes typical in pre-training, necessitating such large effective learning rates. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Training Dynamics; §4.1–4.2 clipping`；Evaluation=`Appendix B–C settings and ablations`；Limitations/Counterevidence=`§5 Conclusions; Appendix C.4 seeds`。

<!-- claim:SF-2026-ARXIV-2605-17787:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17787:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17787:end -->

<!-- review:SF-2026-ARXIV-2605-17821:start -->
#### TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training

**问题与机制。** We propose TierCheck, a cluster-aware tiered checkpointing system that aligns storage placement with failure heterogeneity. 该 family 改变或挑战 `TRAIN-CHECKPOINT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 TierCheck Design; §3.1 save/retrieve/reclaim across local, peer and remote tiers`；Evaluation=`§5 Evaluation; failure frequency, checkpoint overhead and recovery`；Limitations/Counterevidence=`§7 Conclusion; no dedicated limitations section, production failure correlation Not Disclosed`。

<!-- claim:SF-2026-ARXIV-2605-17821:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17821:end -->

**Books Comparison。** 当前 checkpoint 章有完整/增量 checkpoint 与异步保存，但没有按 failure blast radius 把 local/peer/remote recovery tier 变成同一 durability policy；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17821:end -->

<!-- review:SF-2026-ARXIV-2605-17830:start -->
#### Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents

**问题与机制。** To isolate memory exposure from stream non-stationarity, we introduce a trigger-probe protocol that evaluates a fixed probe set against read-only memory snapshots at varying prefix lengths, together with a NullMemory counterfactual baseline for identifying memory-induced violations. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.5 stateful setting and monitor`；Evaluation=`§4 protocol; §5 results`；Limitations/Counterevidence=`§6 Discussion and limitations`。

<!-- claim:SF-2026-ARXIV-2605-17830:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17830:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17830:end -->

<!-- review:SF-2026-ARXIV-2605-17842:start -->
#### SNLP: Layer-Parallel Inference via Structured Newton Corrections

**问题与机制。** We study whether this layerwise dependency can be relaxed by treating the hidden-state trace across layers as the solution of a nonlinear residual equation and solving it with parallel Newton-style updates. 该 family 改变或挑战 `INFER-TENSORRT-LLM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.2–3.5 Structured Newton Layer Parallelism`；Evaluation=`§5.1–5.3 experiments`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17842:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17842:end -->

**Books Comparison。** 当前推理执行章覆盖 tensor/pipeline/kernel 并行，但没有把层序列改写为 residual root finding 后并行 correction 的实验分支；保留为受限机制。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17842:end -->

<!-- review:SF-2026-ARXIV-2605-17849:start -->
#### Generating Pretraining Tokens from Organic Data for Data-Bound Scaling

**问题与机制。** In this paper, we introduce SynPro, a synthetic data generation framework that helps LLMs more thoroughly learn from limited organic data. 该 family 改变或挑战 `TRAIN-DATA` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 model-aware synthesis`；Evaluation=`§4 experiments and analyses`；Limitations/Counterevidence=`§5 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17849:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17849:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17849:end -->

<!-- review:SF-2026-ARXIV-2605-17862:start -->
#### $\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control

**问题与机制。** Building on this, we introduce a sample-level freshness score that quantifies the reliability of a buffered sample with respect to the on-policy objective. 该 family 改变或挑战 `TRAIN-RLHF` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.3 drift decomposition; §4 freshness control`；Evaluation=`§5.1–5.4 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17862:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17862:end -->

**Books Comparison。** 当前 post-training 章有 policy version/freshness，但未同时分解 rollout drift 与 supervision drift 并以 freshness controller 控制异步 OPD；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17862:end -->

<!-- review:SF-2026-ARXIV-2605-17877:start -->
#### PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization

**问题与机制。** Existing remedies such as running full rollouts to assign step-level advantages, calling external LLM judges at each step, or computing intrinsic rewards that require ground-truth answers at every evaluation introduce significant costs or practical constraints. 该 family 改变或挑战 `TRAIN-RLHF` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 PAIR; prefix-aware dense reward construction and intervention`；Evaluation=`§4 Experiments; multi-turn agent optimization and ablations`；Limitations/Counterevidence=`Appendix J Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17877:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17877:end -->

**Books Comparison。** 当前 RLHF 章讨论 outcome/step reward 与 verifier，但没有把不可控 prefix contamination 从当前 action 的 dense credit 中分离；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17877:end -->

<!-- review:SF-2026-ARXIV-2605-17879:start -->
#### Guard: Scalable Straggler Detection and Node Health Management for Large-Scale Training

**问题与机制。** In this paper, we present Guard, a scalable system for detecting stragglers and ensuring node health in large-scale training clusters. 该 family 改变或挑战 `PLATFORM-MONITORING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§6 Guard architecture; online monitor, offline node sweep and triage`；Evaluation=`§7 Evaluation; fail-slow detection, false positives and cluster overhead`；Limitations/Counterevidence=`§7–§8 claim boundary; no dedicated limitations section`。

<!-- claim:SF-2026-ARXIV-2605-17879:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17879:end -->

**Books Comparison。** 当前 monitoring/training 章节缺少在线低开销 fail-slow signal 与离线节点资格复验的分权闭环；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17879:end -->

<!-- review:SF-2026-ARXIV-2605-17889:start -->
#### CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution

**问题与机制。** The Mixture-of-Experts (MoE) architecture improves computational efficiency via sparse expert activation, but throughput-oriented inference faces substantial GPU memory pressure due to a significant parameter size and intermediate data. 该 family 改变或挑战 `INFER-TENSORRT-LLM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Motivation; §4.1–4.2 orchestration`；Evaluation=`§5 evaluation`；Limitations/Counterevidence=`§6 discussion and limitations`。

<!-- claim:SF-2026-ARXIV-2605-17889:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17889:end -->

**Books Comparison。** 当前 MoE execution 章有 expert offload/placement，但缺少 CPU-GPU coalesced expert execution 对 micro-batch 与中间态搬运的统一控制；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17889:end -->

<!-- review:SF-2026-ARXIV-2605-17912:start -->
#### WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform

**问题与机制。** In this work, we introduce WorldArena 2.0, an expanded benchmark that systematically broadens embodied world model evaluation along three dimensions: modality, functionality, and platform. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 WorldArena 2.0 benchmark axes and task construction`；Evaluation=`§4 Experiments across modality, functionality and platform`；Limitations/Counterevidence=`§5 Discussion/Conclusion; simulator and selected-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-17912:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17912:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17912:end -->

<!-- review:SF-2026-ARXIV-2605-17921:start -->
#### An Efficient Streaming Video Understanding Framework with Agentic Control

**问题与机制。** Rather than fixing these decisions upfront, we propose R3-Streaming (Remember, Respond, Reason), which formulates streaming video understanding as a cascaded control problem: for each query, the system compresses memory, judges response readiness, and routes computation sequentially, so that each downstream decision builds on progressively refined information states. 该 family 改变或挑战 `INFER-SCHEDULING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 R3-Streaming cascaded memory, readiness and compute routing`；Evaluation=`§5 Experiments; latency/accuracy under streaming video workloads`；Limitations/Counterevidence=`§6 Conclusion; no production tail-SLO or failure-recovery evidence`。

<!-- claim:SF-2026-ARXIV-2605-17921:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17921:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17921:end -->

<!-- review:SF-2026-ARXIV-2605-17923:start -->
#### AdaptiveLoad: Towards Efficient Video Diffusion Transformer Training

**问题与机制。** In video generation models, particularly world models, training large-scale video diffusion Transformers (such as DiT and MMDiT) poses significant computational challenges due to the extreme variance in sequence lengths within mixed-mode datasets. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 AdaptiveLoad; dual memory/compute constrained batch construction and fused execution`；Evaluation=`§4 Experiments on video diffusion training`；Limitations/Counterevidence=`§5 Conclusion/limitations; selected models and hardware only`。

<!-- claim:SF-2026-ARXIV-2605-17923:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17923:end -->

**Books Comparison。** 当前分布式训练章讨论 packed/variable-length 调度，但没有把 video-DiT sequence 的 memory 与 compute 双约束一起冻结为 batch contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17923:end -->

<!-- review:SF-2026-ARXIV-2605-17932:start -->
#### Prompt Compression in Diffusion Large Language Models: Evaluating LLMLingua-2 on LLaDA

**问题与机制。** This study examines whether LLMLingua-2 transfers effectively to diffusion large language models (DLLMs), specifically LLaDA-8B-Instruct. 该 family 改变或挑战 `MULTIMODAL-GENERATIVE-PARADIGMS` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§III-A–C compression pipeline`；Evaluation=`§III-D; §IV-A–C`；Limitations/Counterevidence=`§V Discussion; §VII Future Work`。

<!-- claim:SF-2026-ARXIV-2605-17932:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17932:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17932:end -->

<!-- review:SF-2026-ARXIV-2605-17954:start -->
#### A More Word-like Image Tokenization for MLLMs

**问题与机制。** We propose a novel Disentangled Visual Tokenization (DiVT) that clusters patch embeddings into coherent semantic units, so each token corresponds to a distinct visual concept instead of a rigid grid cell. 该 family 改变或挑战 `MULTIMODAL-REPRESENTATION` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 motivation; §3.1–3.4 tokenization`；Evaluation=`§4.1–4.4 experiments`；Limitations/Counterevidence=`§5 limitations`。

<!-- claim:SF-2026-ARXIV-2605-17954:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-17954:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17954:end -->

<!-- review:SF-2026-ARXIV-2605-17986:start -->
#### LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection

**问题与机制。** We introduce LivePI (Live Prompt Injection), a structured benchmark for IPI risk in a production-like but test-controlled environment. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Threat model and benchmark construction`；Evaluation=`§4–§5 evaluation and defense analysis across live interaction surfaces`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-17986:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17986:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-17986:end -->

<!-- review:SF-2026-ARXIV-2605-17989:start -->
#### Predictive Prefetching for Retrieval-Augmented Generation

**问题与机制。** In this paper, we propose an advanced asynchronous retrieval framework that enables predictive prefetching aligned with evolving information needs. 该 family 改变或挑战 `AGENT-RAG` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Predictive prefetch controller and retrieval-generation overlap`；Evaluation=`§4 Evaluation; latency, retrieval usefulness and prediction error`；Limitations/Counterevidence=`§6 Limitations; stale/incorrect demand and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-17989:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17989:end -->

**Books Comparison。** 当前 RAG 章有同步/异步检索，却没有预测未来 information demand、允许误预测取消并绑定 freshness 的 prefetch control；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17989:end -->

<!-- review:SF-2026-ARXIV-2605-17992:start -->
#### PipeANN-Filter: An Efficient Filtered Vector Search System on SSD

**问题与机制。** We propose PipeANN-Filter, an efficient filtered vector search system on SSD. 该 family 改变或挑战 `AGENT-RAG` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 PipeANN-Filter superset traversal, post-verification and pipelined SSD IO`；Evaluation=`§4–§5 implementation and filtered-ANN evaluation`；Limitations/Counterevidence=`§6 Limitations; index/filter/update boundary`。

<!-- claim:SF-2026-ARXIV-2605-17992:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17992:end -->

**Books Comparison。** 当前 filtered ANN 已覆盖 query-aware routing，但没有 SSD superset traversal 与 top-k 后验证之间的 IO/recall contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17992:end -->

<!-- review:SF-2026-ARXIV-2605-17998:start -->
#### Verify-Gated Completion as Admission Control in a Governed Multi-Agent Runtime: A Bounded Architecture Case Study

**问题与机制。** This preprint studies verify-gated completion as an admission-control pattern for governed multi-agent runtimes: agents may propose completion, but a read-only verifier decides whether the claim is admitted. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§8 read-only verifier, proposal/admission state and bounded completion protocol`；Evaluation=`§9–§10 architecture case study and failure injection`；Limitations/Counterevidence=`§12 Limitations; bounded case study, not a universal correctness proof`。

<!-- claim:SF-2026-ARXIV-2605-17998:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-17998:end -->

**Books Comparison。** 当前 workflow 有 verifier/commit，但没有把 completion proposal 与只读 admission authority、bounded packet state 和 fail-closed recovery写成同一完成协议；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-17998:end -->

<!-- review:SF-2026-ARXIV-2605-18032:start -->
#### PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows

**问题与机制。** We present PROTEA, a unified interface for offline, test-driven improvement of multi-agent workflows. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§2 architecture; §3.1–3.3 node diagnosis`；Evaluation=`§4.1–4.3 evaluation`；Limitations/Counterevidence=`§5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-18032:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18032:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18032:end -->

<!-- review:SF-2026-ARXIV-2605-18041:start -->
#### OmniSelect: Dynamic Modality-Aware Token Compression for Efficient Omni-modal Large Language Models

**问题与机制。** To address this limitation, we propose $\textbf{OmniSelect}$, a training-free, modality-adaptive token pruning framework that dynamically selects appropriate compression strategies for multimodal inputs. 该 family 改变或挑战 `MULTIMODAL-REPRESENTATION` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 OmniSelect modality-aware token-budget controller`；Evaluation=`§4 Experiments on audio-video OmniLLMs`；Limitations/Counterevidence=`§5 Limitations; model/task-local compression evidence`。

<!-- claim:SF-2026-ARXIV-2605-18041:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18041:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18041:end -->

<!-- review:SF-2026-ARXIV-2605-18053:start -->
#### Protection Is (Nearly) All You Need: Structural Protection Dominates Scoring in Globally Capped KV Eviction

**问题与机制。** We study KV cache eviction under a shared globally capped decode-time harness. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§7 globally capped KV eviction and structural boundary protection`；Evaluation=`§8–§9 evaluation across policies/models and cross-architecture challenge`；Limitations/Counterevidence=`§10.22 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18053:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18053:end -->

**Books Comparison。** 当前 KV eviction 已覆盖 selector/quantizer/fallback，但没有把 prompt/modality boundary 的不可驱逐保护作为 global-cap 前的结构不变量；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18053:end -->

<!-- review:SF-2026-ARXIV-2605-18067:start -->
#### PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence

**问题与机制。** However, the ever-changing pool of agents and their interchangeable capacity introduce new challenges when it comes to matching queries to agents and balancing loads, compared with existing P2P systems. 该 family 改变或挑战 `AGENT-MULTI-AGENT` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§IV–VI agent scoring and serving game`；Evaluation=`§VIII implementation and experiments`；Limitations/Counterevidence=`§VII Discussion`。

<!-- claim:SF-2026-ARXIV-2605-18067:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18067:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18067:end -->

<!-- review:SF-2026-ARXIV-2605-18071:start -->
#### KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference

**问题与机制。** We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. 该 family 改变或挑战 `INFER-KV-CACHE` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§4–§7 multi-tier KV design`；Evaluation=`§9.1–9.3 experiments`；Limitations/Counterevidence=`§10–§11 conclusion and future work`。

<!-- claim:SF-2026-ARXIV-2605-18071:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18071:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18071:end -->

<!-- review:SF-2026-ARXIV-2605-18106:start -->
#### Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads, SwiGLU MLPs, and MoE Routers

**问题与机制。** We address this disparity by introducing a symmetry-compatible principle for optimizer design: the gradient update rule should be equivariant under the symmetry group acting on the corresponding weight block. 该 family 改变或挑战 `TRAIN-PRETRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§5 symmetry-compatible optimizer design`；Evaluation=`§6 experiments`；Limitations/Counterevidence=`§1 Scope and limitations; §7 discussion`。

<!-- claim:SF-2026-ARXIV-2605-18106:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18106:end -->

**Books Comparison。** 当前 optimizer 叙述未把 embedding/LM-head/SwiGLU/MoE-router 的参数对称性作为 optimizer state/action compatibility contract；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18106:end -->

<!-- review:SF-2026-ARXIV-2605-18165:start -->
#### Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs

**问题与机制。** Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. 该 family 改变或挑战 `MULTIMODAL-GENERATIVE-PARADIGMS` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 mask state; §4.1–4.3 compression`；Evaluation=`§5.1–5.4 experiments`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18165:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18165:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18165:end -->

<!-- review:SF-2026-ARXIV-2605-18271:start -->
#### From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG

**问题与机制。** We propose EPIC (Efficient Preference-aligned Index Construction), which focuses on user preferences as a compact and stable form of personal context and integrates them throughout the RAG pipeline. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`PDF pp.3–5 §3.1–3.3 memory construction`；Evaluation=`PDF §4–§5; device experiments`；Limitations/Counterevidence=`PDF §6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18271:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18271:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18271:end -->

<!-- review:SF-2026-ARXIV-2605-18401:start -->
#### SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution

**问题与机制。** We present SkillsVote, a lifecycle-governance framework for Agent Skills across collection, recommendation, attribution, and evolution. 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 SkillsVote collection, recommendation, validation and evolution lifecycle`；Evaluation=`§4 Experiments and lifecycle ablations`；Limitations/Counterevidence=`§5/Appendix limitations; ecosystem and environment sensitivity`。

<!-- claim:SF-2026-ARXIV-2605-18401:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18401:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18401:end -->

<!-- review:SF-2026-ARXIV-2605-18414:start -->
#### Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control

**问题与机制。** We identify a critical gap: when unauthorized tools are visible in an agent's context, models select them in 48-68% of adversarial scenarios, even when explicitly instructed not to. 该 family 改变或挑战 `AGENT-MCP` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 governed MCP proxy`；Evaluation=`§4–§5 benchmark and results`；Limitations/Counterevidence=`§6–§7 discussion and threat-model limits`。

<!-- claim:SF-2026-ARXIV-2605-18414:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18414:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18414:end -->

<!-- review:SF-2026-ARXIV-2605-18421:start -->
#### EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective

**问题与机制。** In this paper, we study agent memory from a self-evolving perspective and introduce EvoMemBench, a unified benchmark organized along two axes: memory scope (in-episode vs. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 EvoMemBench in/cross-episode and knowledge/execution axes`；Evaluation=`§5 Experiments across memory systems`；Limitations/Counterevidence=`§6 Conclusion; benchmark/model coverage boundary`。

<!-- claim:SF-2026-ARXIV-2605-18421:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18421:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18421:end -->

<!-- review:SF-2026-ARXIV-2605-18498:start -->
#### DBES: A Systematic Benchmark and Metric Suite for Evaluating Expert Specialization in Large-Scale MoEs

**问题与机制。** We introduce DBES, a comprehensive diagnostic framework combining a multi-domain benchmark with five theoretically grounded metrics: Routing Specialization, Normalized Effective Rank, Domain Isolation, Routing Stiffness Score, and N-gram Expertise measures. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`PDF pp.3–5 §3 routing-specialization metrics`；Evaluation=`PDF pp.5–11 §4 experiments and intervention`；Limitations/Counterevidence=`PDF p.11 §4.3 intervention boundary; §5 Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-18498:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18498:end -->

**Books Comparison。** 当前 evaluation 章缺少将 MoE load balance 与 functional specialization 分开、并用干预验证而非只看 routing frequency 的契约；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18498:end -->

<!-- review:SF-2026-ARXIV-2605-18565:start -->
#### MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems

**问题与机制。** In this paper, we study how current memory-augmented agents perform in realistic, interference-heavy, long-horizon settings across diverse domains and question types. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 MINTEval multi-target interference construction and update semantics`；Evaluation=`§4 Experiments; recall and aggregation under evolving memories`；Limitations/Counterevidence=`§5 Limitations; synthetic tasks and selected agents`。

<!-- claim:SF-2026-ARXIV-2605-18565:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18565:end -->

**Books Comparison。** 当前 memory 章覆盖版本与冲突，但没有把 multi-target interference、update history 与 aggregate reasoning 组合成一条验收轴；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18565:end -->

<!-- review:SF-2026-ARXIV-2605-18583:start -->
#### Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks

**问题与机制。** We present OverEager-Gen, a benchmark dedicated to overeager behavior on benign tasks. 该 family 改变或挑战 `PLATFORM-SECURITY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 benchmark, benign task scope and overeager-action taxonomy`；Evaluation=`§4 Experiments across coding agents`；Limitations/Counterevidence=`§5 Limitations; harness and observable-action boundary`。

<!-- claim:SF-2026-ARXIV-2605-18583:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18583:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18583:end -->

<!-- review:SF-2026-ARXIV-2605-18607:start -->
#### Forecasting Downstream Performance of LLMs With Proxy Metrics

**问题与机制。** Instead, we propose to construct proxy metrics by aggregating token-level statistics, such as entropy, top-k accuracy, and expert token rank, from a candidate model's next token distribution over expert-written solutions. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 proxy metrics`；Evaluation=`§4–§5 model/data ranking`；Limitations/Counterevidence=`§6 limitations`。

<!-- claim:SF-2026-ARXIV-2605-18607:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18607:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18607:end -->

<!-- review:SF-2026-ARXIV-2605-18652:start -->
#### MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents

**问题与机制。** To address these limitations, we introduce \textbf{MementoGUI}, a plug-in agentic memory framework that equips MLLM-based GUI agents with \textbf{MementoCore}, a learned controller for online memory selection, compression, and retrieval. 该 family 改变或挑战 `AGENT-MEMORY` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 MementoGUI multimodal memory controller and write/read policy`；Evaluation=`§4–§5 benchmark construction and experiments`；Limitations/Counterevidence=`§6 Limitations; GUI domain and selected backbones`。

<!-- claim:SF-2026-ARXIV-2605-18652:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18652:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18652:end -->

<!-- review:SF-2026-ARXIV-2605-18693:start -->
#### SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents

**问题与机制。** Existing benchmarks primarily evaluate the efficacy of given skills or the ability of agents to solve downstream tasks from raw context, but they do not isolate skill generation itself as the object of study. 该 family 改变或挑战 `AGENT-PLATFORM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.4 skill-generation artifact contract`；Evaluation=`§4.1–4.4 execution evaluation`；Limitations/Counterevidence=`§5 Conclusion; appendix sensitivity`。

<!-- claim:SF-2026-ARXIV-2605-18693:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-18693:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18693:end -->

<!-- review:SF-2026-ARXIV-2605-18697:start -->
#### PopPy: Opportunistically Exploiting Parallelism in Python Compound AI Applications

**问题与机制。** To address this problem, we develop PopPy, a system that can uncover parallelization opportunities in Python applications that invoke these heavy external components, including those used in compound AI applications. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§6 PopPy compiler/runtime dependency discovery and external-call parallelism`；Evaluation=`§8 Evaluation; latency and semantic-equivalence checks`；Limitations/Counterevidence=`§10 Discussion; Python/compound-application boundary`。

<!-- claim:SF-2026-ARXIV-2605-18697:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18697:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18697:end -->

<!-- review:SF-2026-ARXIV-2605-18703:start -->
#### EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

**问题与机制。** We introduce EnvFactory, a fully automated framework that addresses both challenges. 该 family 改变或挑战 `AGENT-WORKFLOW` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 executable-environment synthesis, verification and RL data path`；Evaluation=`§5 Evaluation of environment validity and agent training`；Limitations/Counterevidence=`§6 Limitations`。

<!-- claim:SF-2026-ARXIV-2605-18703:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18703:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18703:end -->

<!-- review:SF-2026-ARXIV-2605-18710:start -->
#### Mosaic: Towards Efficient Training of Multimodal Models with Spatial Resource Multiplexing

**问题与机制。** To improve GPU utilization and enable efficient MM training, we propose deploying MMs in a temporal-spatial multiplexing manner, allowing multiple MM modules to colocate on a GPU with well-controlled resource quotas. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 Mosaic spatial resource multiplexing, placement and performance model`；Evaluation=`§4 Evaluation across multimodal module mixtures`；Limitations/Counterevidence=`§5 Limitations; selected architectures/hardware`。

<!-- claim:SF-2026-ARXIV-2605-18710:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18710:end -->

**Books Comparison。** 当前 multimodal/distributed training 章缺少空间复用时 module placement、GPU share 与 interference budget 的联合 owner；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18710:end -->

<!-- review:SF-2026-ARXIV-2605-18739:start -->
#### LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation

**问题与机制。** We present LongLive-2.0, an NVFP4-based parallel infrastructure throughout the full training and inference workflow of long video generation, addressing speed and memory bottlenecks. 该 family 改变或挑战 `TRAIN-DISTRIBUTED-TRAINING` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3–§4 NVFP4 training/inference infrastructure and parallel layouts`；Evaluation=`§5 Evaluation on long-video generation`；Limitations/Counterevidence=`§6 Limitations; vendor precision and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-18739:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18739:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-18739:end -->

<!-- review:SF-2026-ARXIV-2605-18750:start -->
#### A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability

**问题与机制。** We present Runtime-Readiness-First Pipeline (RRFP), a readiness-driven runtime for pipeline-parallel training. 该 family 改变或挑战 `TRAIN-PIPELINE-PARALLEL` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3 readiness-driven runtime and dependency state`；Evaluation=`§4–§5 implementation and evaluation under runtime variability`；Limitations/Counterevidence=`§6 Limitations; schedule/hardware/workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-18750:start -->只支持 exact-v1 明确披露的模型、数据、硬件、精度、长度、并发与 evaluator；未披露字段为 Not Disclosed，不把模拟、单机或选定 benchmark 外推成生产保证。<!-- claim:SF-2026-ARXIV-2605-18750:end -->

**Books Comparison。** 当前 pipeline 章以 schedule 为主，但没有在运行时以真实 task readiness 取得 dispatch authority并保留静态 schedule fallback；保留为写回增量。 Decision=`Integrate`。
<!-- review:SF-2026-ARXIV-2605-18750:end -->

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

<!-- review:SF-2026-ARXIV-2605-20251:start -->
#### ProcCtrlBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents

**问题与机制。** We present ProcCtrlBench, a benchmark for execution-process evaluation in LLM coding agents. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§3.1–3.5 trajectory/control contract`；Evaluation=`§4.1–4.5 experiments`；Limitations/Counterevidence=`§5 Limitations and Conclusion`。

<!-- claim:SF-2026-ARXIV-2605-20251:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-20251:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-20251:end -->

<!-- review:SF-2026-ARXIV-2605-20270:start -->
#### Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs

**问题与机制。** Using a (test statistic, validity guarantee, deployment rule) framework, we identify one empty cell forced by deployment requirements: e-process per threshold, selective risk, anytime-pathwise validity, max-certified-threshold rule. 该 family 改变或挑战 `PLATFORM-EVALUATION-SYSTEM` 的系统契约，因此保留。

**Exact-v1 路径。** Method=`§1–§4 deployment contract and e-process`；Evaluation=`§5–§7 proofs and 650-stream evaluation`；Limitations/Counterevidence=`§8 limitations and boundary`。

<!-- claim:SF-2026-ARXIV-2605-20270:start -->Only the exact-v1 disclosed workload/model/hardware/precision/length/batch/concurrency/SLO/evaluator is supported; every undisclosed field is Not Disclosed.<!-- claim:SF-2026-ARXIV-2605-20270:end -->

**Books Comparison。** 当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。 Decision=`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2605-20270:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17734 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17734 |
| SF-2026-ARXIV-2605-17757 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17757 |
| SF-2026-ARXIV-2605-17787 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17787 |
| SF-2026-ARXIV-2605-17821 | score_7_9;forced_review;potential_books_delta | selected | DA-FAILURE-TIERED-CHECKPOINT | — | 跨层改变 durability、authority 或 runtime dispatch，且 false-negative 风险高 | analysis:DA-FAILURE-TIERED-CHECKPOINT |
| SF-2026-ARXIV-2605-17830 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17830 |
| SF-2026-ARXIV-2605-17842 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17842 |
| SF-2026-ARXIV-2605-17849 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17849 |
| SF-2026-ARXIV-2605-17862 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17862 |
| SF-2026-ARXIV-2605-17877 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17877 |
| SF-2026-ARXIV-2605-17879 | score_7_9;forced_review;potential_books_delta | selected | DA-FAIL-SLOW-NODE-QUALIFICATION | — | 跨层改变 durability、authority 或 runtime dispatch，且 false-negative 风险高 | analysis:DA-FAIL-SLOW-NODE-QUALIFICATION |
| SF-2026-ARXIV-2605-17889 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17889 |
| SF-2026-ARXIV-2605-17912 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17912 |
| SF-2026-ARXIV-2605-17921 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17921 |
| SF-2026-ARXIV-2605-17923 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17923 |
| SF-2026-ARXIV-2605-17932 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17932 |
| SF-2026-ARXIV-2605-17954 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17954 |
| SF-2026-ARXIV-2605-17986 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17986 |
| SF-2026-ARXIV-2605-17989 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17989 |
| SF-2026-ARXIV-2605-17992 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-17992 |
| SF-2026-ARXIV-2605-17998 | score_7_9;forced_review;potential_books_delta | selected | DA-VERIFY-GATED-COMPLETION | — | 跨层改变 durability、authority 或 runtime dispatch，且 false-negative 风险高 | analysis:DA-VERIFY-GATED-COMPLETION |
| SF-2026-ARXIV-2605-18032 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18032 |
| SF-2026-ARXIV-2605-18053 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18053 |
| SF-2026-ARXIV-2605-18067 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18067 |
| SF-2026-ARXIV-2605-18071 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18071 |
| SF-2026-ARXIV-2605-18106 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18106 |
| SF-2026-ARXIV-2605-18165 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18165 |
| SF-2026-ARXIV-2605-18271 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18271 |
| SF-2026-ARXIV-2605-18401 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18401 |
| SF-2026-ARXIV-2605-18414 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18414 |
| SF-2026-ARXIV-2605-18421 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18421 |
| SF-2026-ARXIV-2605-18498 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18498 |
| SF-2026-ARXIV-2605-18565 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18565 |
| SF-2026-ARXIV-2605-18583 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18583 |
| SF-2026-ARXIV-2605-18607 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18607 |
| SF-2026-ARXIV-2605-18652 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18652 |
| SF-2026-ARXIV-2605-18693 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18693 |
| SF-2026-ARXIV-2605-18697 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18697 |
| SF-2026-ARXIV-2605-18703 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18703 |
| SF-2026-ARXIV-2605-18710 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18710 |
| SF-2026-ARXIV-2605-18739 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18739 |
| SF-2026-ARXIV-2605-18750 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18750 |
| SF-2026-ARXIV-2605-18918 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18918 |
| SF-2026-ARXIV-2605-18930 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18930 |
| SF-2026-ARXIV-2605-18991 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-18991 |
| SF-2026-ARXIV-2605-19008 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19008 |
| SF-2026-ARXIV-2605-19049 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19049 |
| SF-2026-ARXIV-2605-19099 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19099 |
| SF-2026-ARXIV-2605-19101 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19101 |
| SF-2026-ARXIV-2605-19127 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19127 |
| SF-2026-ARXIV-2605-19140 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19140 |
| SF-2026-ARXIV-2605-19151 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19151 |
| SF-2026-ARXIV-2605-19169 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19169 |
| SF-2026-ARXIV-2605-19192 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19192 |
| SF-2026-ARXIV-2605-19193 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19193 |
| SF-2026-ARXIV-2605-19196 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19196 |
| SF-2026-ARXIV-2605-19218 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19218 |
| SF-2026-ARXIV-2605-19228 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-19228 |
| SF-2026-ARXIV-2605-20251 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-20251 |
| SF-2026-ARXIV-2605-20270 | score_7_9 | not_selected | — | — | exact-v1 Source Review 已完成；未进入三项扩写只受 Daily 上限约束 | analysis-decision:SF-2026-ARXIV-2605-20270 |

<!-- analysis:DA-FAILURE-TIERED-CHECKPOINT:start -->
### DA-FAILURE-TIERED-CHECKPOINT

单一远端 checkpoint 在集群稳定、保存频率低时简单可靠，但 failure 从单卡扩大到 rack/cluster 后，所有故障都支付同一远端 IO 成本。TierCheck 按 blast radius 把恢复状态放入 local、peer 与 remote tier，并让保存与回收策略拥有 durability class。收益是常见故障走快路径；代价是多副本状态、peer failure correlation 与 reclaim race。无法证明 tier 健康或灾难域独立时，远端 durable checkpoint 仍是权威 fallback。
<!-- analysis:DA-FAILURE-TIERED-CHECKPOINT:end -->

<!-- analysis:DA-FAIL-SLOW-NODE-QUALIFICATION:start -->
### DA-FAIL-SLOW-NODE-QUALIFICATION

功能性健康检查能排除硬故障，却看不到算力、互联或温控引起的 fail-slow；长训练中少数慢节点会把全局同步拖入尾部。Guard 把低开销在线 monitor 与昂贵离线 node qualification 分开：前者触发怀疑，后者决定隔离/复用。它用额外 telemetry、复验容量和误报风险换吞吐稳定；信号漂移或归因不清时不能自动驱逐，应回退人工/保守 quarantine。
<!-- analysis:DA-FAIL-SLOW-NODE-QUALIFICATION:end -->

<!-- analysis:DA-VERIFY-GATED-COMPLETION:start -->
### DA-VERIFY-GATED-COMPLETION

让生成 Agent 自己宣布完成在短、可逆任务中成本最低；持久工作流里，提议者同时掌握 completion authority 会把遗漏验证变成不可见提交。Verify-gated completion 将 proposal、read-only verification、admission 与 commit receipt 分开，并为失败保留 bounded packet state。收益是 completion 可审计、可拒绝；代价是 verifier 偏差、额外延迟和 liveness 风险。Verifier 不可用或证据不完整时应 fail closed/升级，而不是让 proposer 绕过 Gate。
<!-- analysis:DA-VERIFY-GATED-COMPLETION:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17734:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17734:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17757:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17757:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17787:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17787:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17830:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17830:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17842:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17842:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17849:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17849:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17862:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17862:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17877:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17877:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17889:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17889:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17912:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17912:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17921:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17921:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17923:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17923:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17932:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17932:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17954:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17954:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17986:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17986:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17989:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17989:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-17992:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-17992:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18032:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18032:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18041:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18041:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18053:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18053:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18067:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18067:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18071:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18071:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18106:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18106:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18165:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18165:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18271:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18271:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18401:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18401:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18414:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18414:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18421:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18421:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18498:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18498:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18565:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18565:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18583:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18583:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18607:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18607:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18652:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18652:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18693:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18693:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18697:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18697:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18703:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18703:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18710:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18710:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18739:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18739:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18750:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18750:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18918:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18918:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18930:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18930:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-18991:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-18991:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19008:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19008:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19049:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19049:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19099:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19099:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19101:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19101:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19127:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19127:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19140:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19140:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19151:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19151:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19169:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19169:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19192:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19192:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19193:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19193:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19196:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19196:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19218:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19218:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-19228:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-19228:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20251:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-20251:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-20270:start -->该 family 已完成 exact-v1 Source Review；未扩写不代表跳过 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-20270:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-17734 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-17734 | delta:SF-2026-ARXIV-2605-17734 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17734 |
| SF-2026-ARXIV-2605-17757 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-17757 | delta:SF-2026-ARXIV-2605-17757 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17757 |
| SF-2026-ARXIV-2605-17787 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-17787 | delta:SF-2026-ARXIV-2605-17787 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17787 |
| SF-2026-ARXIV-2605-17821 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#chapter-35 | books/part-04-training-system/34-dpo.md#chapter-34;books/part-04-training-system/36-distributed-training.md#chapter-36 | existing:SF-2026-ARXIV-2605-17821 | delta:SF-2026-ARXIV-2605-17821 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17821 |
| SF-2026-ARXIV-2605-17830 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-17830 | delta:SF-2026-ARXIV-2605-17830 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17830 |
| SF-2026-ARXIV-2605-17842 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17842 | delta:SF-2026-ARXIV-2605-17842 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17842 |
| SF-2026-ARXIV-2605-17849 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-17849 | delta:SF-2026-ARXIV-2605-17849 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17849 |
| SF-2026-ARXIV-2605-17862 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17862 | delta:SF-2026-ARXIV-2605-17862 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17862 |
| SF-2026-ARXIV-2605-17877 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-17877 | delta:SF-2026-ARXIV-2605-17877 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17877 |
| SF-2026-ARXIV-2605-17879 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66;books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-17879 | delta:SF-2026-ARXIV-2605-17879 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17879 |
| SF-2026-ARXIV-2605-17889 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-17889 | delta:SF-2026-ARXIV-2605-17889 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17889 |
| SF-2026-ARXIV-2605-17912 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17912 | delta:SF-2026-ARXIV-2605-17912 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17912 |
| SF-2026-ARXIV-2605-17921 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-17921 | delta:SF-2026-ARXIV-2605-17921 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17921 |
| SF-2026-ARXIV-2605-17923 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-17923 | delta:SF-2026-ARXIV-2605-17923 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17923 |
| SF-2026-ARXIV-2605-17932 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-17932 | delta:SF-2026-ARXIV-2605-17932 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17932 |
| SF-2026-ARXIV-2605-17954 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-17954 | delta:SF-2026-ARXIV-2605-17954 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17954 |
| SF-2026-ARXIV-2605-17986 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-17986 | delta:SF-2026-ARXIV-2605-17986 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-17986 |
| SF-2026-ARXIV-2605-17989 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17989 | delta:SF-2026-ARXIV-2605-17989 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17989 |
| SF-2026-ARXIV-2605-17992 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-17992 | delta:SF-2026-ARXIV-2605-17992 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17992 |
| SF-2026-ARXIV-2605-17998 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-17998 | delta:SF-2026-ARXIV-2605-17998 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-17998 |
| SF-2026-ARXIV-2605-18032 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18032 | delta:SF-2026-ARXIV-2605-18032 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18032 |
| SF-2026-ARXIV-2605-18041 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-18041 | delta:SF-2026-ARXIV-2605-18041 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18041 |
| SF-2026-ARXIV-2605-18053 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-18053 | delta:SF-2026-ARXIV-2605-18053 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18053 |
| SF-2026-ARXIV-2605-18067 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18067 | delta:SF-2026-ARXIV-2605-18067 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18067 |
| SF-2026-ARXIV-2605-18071 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-18071 | delta:SF-2026-ARXIV-2605-18071 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18071 |
| SF-2026-ARXIV-2605-18106 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27;books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-18106 | delta:SF-2026-ARXIV-2605-18106 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18106 |
| SF-2026-ARXIV-2605-18165 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23;books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-18165 | delta:SF-2026-ARXIV-2605-18165 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18165 |
| SF-2026-ARXIV-2605-18271 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18271 | delta:SF-2026-ARXIV-2605-18271 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18271 |
| SF-2026-ARXIV-2605-18401 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18401 | delta:SF-2026-ARXIV-2605-18401 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18401 |
| SF-2026-ARXIV-2605-18414 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-18414 | delta:SF-2026-ARXIV-2605-18414 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18414 |
| SF-2026-ARXIV-2605-18421 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18421 | delta:SF-2026-ARXIV-2605-18421 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18421 |
| SF-2026-ARXIV-2605-18498 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18498 | delta:SF-2026-ARXIV-2605-18498 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18498 |
| SF-2026-ARXIV-2605-18565 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18565 | delta:SF-2026-ARXIV-2605-18565 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18565 |
| SF-2026-ARXIV-2605-18583 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-18583 | delta:SF-2026-ARXIV-2605-18583 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18583 |
| SF-2026-ARXIV-2605-18607 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-18607 | delta:SF-2026-ARXIV-2605-18607 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18607 |
| SF-2026-ARXIV-2605-18652 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-18652 | delta:SF-2026-ARXIV-2605-18652 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18652 |
| SF-2026-ARXIV-2605-18693 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-18693 | delta:SF-2026-ARXIV-2605-18693 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18693 |
| SF-2026-ARXIV-2605-18697 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18697 | delta:SF-2026-ARXIV-2605-18697 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18697 |
| SF-2026-ARXIV-2605-18703 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-18703 | delta:SF-2026-ARXIV-2605-18703 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18703 |
| SF-2026-ARXIV-2605-18710 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-18710 | delta:SF-2026-ARXIV-2605-18710 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18710 |
| SF-2026-ARXIV-2605-18739 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-18739 | delta:SF-2026-ARXIV-2605-18739 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-18739 |
| SF-2026-ARXIV-2605-18750 | TRAIN-PIPELINE-PARALLEL | books/part-04-training-system/38-pipeline-parallel.md#chapter-38 | books/part-04-training-system/37-tensor-parallel.md#chapter-37;books/part-04-training-system/39-zero.md#chapter-39 | existing:SF-2026-ARXIV-2605-18750 | delta:SF-2026-ARXIV-2605-18750 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-18750 |
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
| SF-2026-ARXIV-2605-20251 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20251 | delta:SF-2026-ARXIV-2605-20251 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20251 |
| SF-2026-ARXIV-2605-20270 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-20270 | delta:SF-2026-ARXIV-2605-20270 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-20270 |
<!-- books-review:SF-2026-ARXIV-2605-17734:start -->
<!-- existing:SF-2026-ARXIV-2605-17734:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-17734:end -->
<!-- delta:SF-2026-ARXIV-2605-17734:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17734:end -->
<!-- books-review:SF-2026-ARXIV-2605-17734:end -->
<!-- books-review:SF-2026-ARXIV-2605-17757:start -->
<!-- existing:SF-2026-ARXIV-2605-17757:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-17757:end -->
<!-- delta:SF-2026-ARXIV-2605-17757:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17757:end -->
<!-- books-review:SF-2026-ARXIV-2605-17757:end -->
<!-- books-review:SF-2026-ARXIV-2605-17787:start -->
<!-- existing:SF-2026-ARXIV-2605-17787:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-17787:end -->
<!-- delta:SF-2026-ARXIV-2605-17787:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17787:end -->
<!-- books-review:SF-2026-ARXIV-2605-17787:end -->
<!-- books-review:SF-2026-ARXIV-2605-17821:start -->
<!-- existing:SF-2026-ARXIV-2605-17821:start -->已顺读 `books/part-04-training-system/35-checkpoint.md` 与相邻章节 ['books/part-04-training-system/34-dpo.md', 'books/part-04-training-system/36-distributed-training.md']；正文主线 headings=['本章要回答的问题', '为什么只保存 Weights 不够', '一个完整训练状态清单', 'Checkpoint Size 为什么远大于模型文件', '一致性首先是 Step 边界', 'Checkpoint 应像事务一样提交', '分布式 Sharded Checkpoint', 'Resharding 为什么比 Load 更难', 'Data Cursor 为什么必须保存', 'RNG State 为什么影响可复现性']。<!-- existing:SF-2026-ARXIV-2605-17821:end -->
<!-- delta:SF-2026-ARXIV-2605-17821:start -->当前 checkpoint 章有完整/增量 checkpoint 与异步保存，但没有按 failure blast radius 把 local/peer/remote recovery tier 变成同一 durability policy；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17821:end -->
<!-- books-review:SF-2026-ARXIV-2605-17821:end -->
<!-- books-review:SF-2026-ARXIV-2605-17830:start -->
<!-- existing:SF-2026-ARXIV-2605-17830:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-17830:end -->
<!-- delta:SF-2026-ARXIV-2605-17830:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17830:end -->
<!-- books-review:SF-2026-ARXIV-2605-17830:end -->
<!-- books-review:SF-2026-ARXIV-2605-17842:start -->
<!-- existing:SF-2026-ARXIV-2605-17842:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；正文主线 headings=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract', '从 Linear 语义到 GEMM 执行', '两种稀疏性必须共享地址合同，却不必共享 Kernel']。<!-- existing:SF-2026-ARXIV-2605-17842:end -->
<!-- delta:SF-2026-ARXIV-2605-17842:start -->当前推理执行章覆盖 tensor/pipeline/kernel 并行，但没有把层序列改写为 residual root finding 后并行 correction 的实验分支；保留为受限机制。<!-- delta:SF-2026-ARXIV-2605-17842:end -->
<!-- books-review:SF-2026-ARXIV-2605-17842:end -->
<!-- books-review:SF-2026-ARXIV-2605-17849:start -->
<!-- existing:SF-2026-ARXIV-2605-17849:start -->已顺读 `books/part-04-training-system/27-data.md` 与相邻章节 ['books/part-04-training-system/28-pretraining.md']；正文主线 headings=['本章要回答的问题', 'Part IV 的能力生产链', '先从“把互联网都抓下来”开始', 'Collection protocol 为什么先于 Filtering 定义数据', '数据分布就是优化权重', '静态 Mixture 到版本化 Data Control Plane', '一个三域配比小例子', 'Data tags 也可能训练一条隐式控制策略', 'Quality filtering 在过滤什么', 'Synthetic data：从“先生成再打分”到 Specification Compilation']。<!-- existing:SF-2026-ARXIV-2605-17849:end -->
<!-- delta:SF-2026-ARXIV-2605-17849:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17849:end -->
<!-- books-review:SF-2026-ARXIV-2605-17849:end -->
<!-- books-review:SF-2026-ARXIV-2605-17862:start -->
<!-- existing:SF-2026-ARXIV-2605-17862:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；正文主线 headings=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', "Reward hacking 与 Goodhart's Law", 'Sequence reward 与 token updates 的错位']。<!-- existing:SF-2026-ARXIV-2605-17862:end -->
<!-- delta:SF-2026-ARXIV-2605-17862:start -->当前 post-training 章有 policy version/freshness，但未同时分解 rollout drift 与 supervision drift 并以 freshness controller 控制异步 OPD；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17862:end -->
<!-- books-review:SF-2026-ARXIV-2605-17862:end -->
<!-- books-review:SF-2026-ARXIV-2605-17877:start -->
<!-- existing:SF-2026-ARXIV-2605-17877:start -->已顺读 `books/part-04-training-system/31-rlhf.md` 与相邻章节 ['books/part-04-training-system/30-lora.md', 'books/part-04-training-system/32-ppo.md']；正文主线 headings=['本章要回答的问题', 'Demonstration 为什么不足以表达偏好', 'RLHF 的完整 pipeline', 'Reward Model 怎样学习相对判断', '一个 preference score 小例子', 'Preference data 的难点不只是数量', '从 Reward 到 Policy objective', '改变输出分布是目标，不是无副作用的偏好标签', "Reward hacking 与 Goodhart's Law", 'Sequence reward 与 token updates 的错位']。<!-- existing:SF-2026-ARXIV-2605-17877:end -->
<!-- delta:SF-2026-ARXIV-2605-17877:start -->当前 RLHF 章讨论 outcome/step reward 与 verifier，但没有把不可控 prefix contamination 从当前 action 的 dense credit 中分离；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17877:end -->
<!-- books-review:SF-2026-ARXIV-2605-17877:end -->
<!-- books-review:SF-2026-ARXIV-2605-17879:start -->
<!-- existing:SF-2026-ARXIV-2605-17879:start -->已顺读 `books/part-06-ai-infrastructure/67-monitoring.md` 与相邻章节 ['books/part-06-ai-infrastructure/66-evaluation-system.md', 'books/part-06-ai-infrastructure/68-logging.md']；正文主线 headings=['本章要回答的问题', '先定义目标，再选择可测信号', 'Context generator 是 pre-failure sensor identity 的一部分', 'Review notes', '四层指标', 'Autonomy 不是一个纯模型指标', '从单次 Query 指标到 Session-level Search Trajectory Sensor', 'Rate、Errors、Duration 与 Saturation', '从 Error Counter 到 Layer × Detectability Failure Coordinate', '平均值为什么危险']。<!-- existing:SF-2026-ARXIV-2605-17879:end -->
<!-- delta:SF-2026-ARXIV-2605-17879:start -->当前 monitoring/training 章节缺少在线低开销 fail-slow signal 与离线节点资格复验的分权闭环；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17879:end -->
<!-- books-review:SF-2026-ARXIV-2605-17879:end -->
<!-- books-review:SF-2026-ARXIV-2605-17889:start -->
<!-- existing:SF-2026-ARXIV-2605-17889:start -->已顺读 `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节 ['books/part-05-inference-system/48-speculative-decoding.md', 'books/part-05-inference-system/50-vllm.md']；正文主线 headings=['本章要回答的问题', '从计算图开始', '三类基础优化', 'Execution Plan 可以修订，但只能在安全边界 Commit', '异步工作不必永久绑定固定 Physical Core', '从粗粒度 Offload 到负载观测的 Tensor Placement', 'Backend Choice 必须携带 Previous-backend State', 'Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract', '从 Linear 语义到 GEMM 执行', '两种稀疏性必须共享地址合同，却不必共享 Kernel']。<!-- existing:SF-2026-ARXIV-2605-17889:end -->
<!-- delta:SF-2026-ARXIV-2605-17889:start -->当前 MoE execution 章有 expert offload/placement，但缺少 CPU-GPU coalesced expert execution 对 micro-batch 与中间态搬运的统一控制；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17889:end -->
<!-- books-review:SF-2026-ARXIV-2605-17889:end -->
<!-- books-review:SF-2026-ARXIV-2605-17912:start -->
<!-- existing:SF-2026-ARXIV-2605-17912:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-17912:end -->
<!-- delta:SF-2026-ARXIV-2605-17912:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17912:end -->
<!-- books-review:SF-2026-ARXIV-2605-17912:end -->
<!-- books-review:SF-2026-ARXIV-2605-17921:start -->
<!-- existing:SF-2026-ARXIV-2605-17921:start -->已顺读 `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节 ['books/part-05-inference-system/55-pd-disaggregation.md']；正文主线 headings=['本章要回答的问题', '调度对象从 request 变成 token state', '目标函数不止吞吐', 'SLO-aware Admission', '当前能放下，不等于未来可完成', '不确定输出长度下的 Future-state Reservation', '连续 Edge Inference 需要跨窗口携带 Violation-risk Budget', '从队列启发式到时间耦合的资源影子价格', 'Reasoning Budget 必须进入调度与评估身份', 'Inference-time Process Guidance 也是可调度资源']。<!-- existing:SF-2026-ARXIV-2605-17921:end -->
<!-- delta:SF-2026-ARXIV-2605-17921:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17921:end -->
<!-- books-review:SF-2026-ARXIV-2605-17921:end -->
<!-- books-review:SF-2026-ARXIV-2605-17923:start -->
<!-- existing:SF-2026-ARXIV-2605-17923:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-17923:end -->
<!-- delta:SF-2026-ARXIV-2605-17923:start -->当前分布式训练章讨论 packed/variable-length 调度，但没有把 video-DiT sequence 的 memory 与 compute 双约束一起冻结为 batch contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17923:end -->
<!-- books-review:SF-2026-ARXIV-2605-17923:end -->
<!-- books-review:SF-2026-ARXIV-2605-17932:start -->
<!-- existing:SF-2026-ARXIV-2605-17932:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；正文主线 headings=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State', 'Block Diffusion：局部自回归与块内并行', 'Draft、Verify 与 Correct 不是同一件事']。<!-- existing:SF-2026-ARXIV-2605-17932:end -->
<!-- delta:SF-2026-ARXIV-2605-17932:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17932:end -->
<!-- books-review:SF-2026-ARXIV-2605-17932:end -->
<!-- books-review:SF-2026-ARXIV-2605-17954:start -->
<!-- existing:SF-2026-ARXIV-2605-17954:start -->已顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；正文主线 headings=['本章要回答的问题', '为什么文本 token 的经验不能直接复制', '一个思想实验：同样是 256 个 token', '表示演进：从专用特征到统一协议', '阶段一：手工特征与专用模型', '阶段二：modality-specific encoder + projector', '阶段三：共享 token space', '阶段四：native multimodal representation', '连续表示、离散表示与混合表示', '连续表示']。<!-- existing:SF-2026-ARXIV-2605-17954:end -->
<!-- delta:SF-2026-ARXIV-2605-17954:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17954:end -->
<!-- books-review:SF-2026-ARXIV-2605-17954:end -->
<!-- books-review:SF-2026-ARXIV-2605-17986:start -->
<!-- existing:SF-2026-ARXIV-2605-17986:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-17986:end -->
<!-- delta:SF-2026-ARXIV-2605-17986:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-17986:end -->
<!-- books-review:SF-2026-ARXIV-2605-17986:end -->
<!-- books-review:SF-2026-ARXIV-2605-17989:start -->
<!-- existing:SF-2026-ARXIV-2605-17989:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；正文主线 headings=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Agentic Retrieval：Relevance 也可以是执行先验']。<!-- existing:SF-2026-ARXIV-2605-17989:end -->
<!-- delta:SF-2026-ARXIV-2605-17989:start -->当前 RAG 章有同步/异步检索，却没有预测未来 information demand、允许误预测取消并绑定 freshness 的 prefetch control；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17989:end -->
<!-- books-review:SF-2026-ARXIV-2605-17989:end -->
<!-- books-review:SF-2026-ARXIV-2605-17992:start -->
<!-- existing:SF-2026-ARXIV-2605-17992:start -->已顺读 `books/part-07-agent/76-rag.md` 与相邻章节 ['books/part-07-agent/75-context.md', 'books/part-07-agent/77-memory.md']；正文主线 headings=['本章要回答的问题', '参数化知识的边界', 'Offline Ingestion 不是预处理细节', 'Online Retrieval Pipeline', 'Tenant Filter 必须在检索内核中前置执行', 'Retrieval 的基本度量', 'Chunking 是信息边界设计', 'Reranking 与 Context Packing', 'Relevance 不等于 Sufficient Context', 'Agentic Retrieval：Relevance 也可以是执行先验']。<!-- existing:SF-2026-ARXIV-2605-17992:end -->
<!-- delta:SF-2026-ARXIV-2605-17992:start -->当前 filtered ANN 已覆盖 query-aware routing，但没有 SSD superset traversal 与 top-k 后验证之间的 IO/recall contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17992:end -->
<!-- books-review:SF-2026-ARXIV-2605-17992:end -->
<!-- books-review:SF-2026-ARXIV-2605-17998:start -->
<!-- existing:SF-2026-ARXIV-2605-17998:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-17998:end -->
<!-- delta:SF-2026-ARXIV-2605-17998:start -->当前 workflow 有 verifier/commit，但没有把 completion proposal 与只读 admission authority、bounded packet state 和 fail-closed recovery写成同一完成协议；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-17998:end -->
<!-- books-review:SF-2026-ARXIV-2605-17998:end -->
<!-- books-review:SF-2026-ARXIV-2605-18032:start -->
<!-- existing:SF-2026-ARXIV-2605-18032:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18032:end -->
<!-- delta:SF-2026-ARXIV-2605-18032:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18032:end -->
<!-- books-review:SF-2026-ARXIV-2605-18032:end -->
<!-- books-review:SF-2026-ARXIV-2605-18041:start -->
<!-- existing:SF-2026-ARXIV-2605-18041:start -->已顺读 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节 ['books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md']；正文主线 headings=['本章要回答的问题', '为什么文本 token 的经验不能直接复制', '一个思想实验：同样是 256 个 token', '表示演进：从专用特征到统一协议', '阶段一：手工特征与专用模型', '阶段二：modality-specific encoder + projector', '阶段三：共享 token space', '阶段四：native multimodal representation', '连续表示、离散表示与混合表示', '连续表示']。<!-- existing:SF-2026-ARXIV-2605-18041:end -->
<!-- delta:SF-2026-ARXIV-2605-18041:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18041:end -->
<!-- books-review:SF-2026-ARXIV-2605-18041:end -->
<!-- books-review:SF-2026-ARXIV-2605-18053:start -->
<!-- existing:SF-2026-ARXIV-2605-18053:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-18053:end -->
<!-- delta:SF-2026-ARXIV-2605-18053:start -->当前 KV eviction 已覆盖 selector/quantizer/fallback，但没有把 prompt/modality boundary 的不可驱逐保护作为 global-cap 前的结构不变量；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18053:end -->
<!-- books-review:SF-2026-ARXIV-2605-18053:end -->
<!-- books-review:SF-2026-ARXIV-2605-18067:start -->
<!-- existing:SF-2026-ARXIV-2605-18067:start -->已顺读 `books/part-07-agent/82-multi-agent.md` 与相邻章节 ['books/part-07-agent/81-workflow.md', 'books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', '先建立单 Agent Baseline', '扩展 Agent 数量之前，先测量 Coordination Tax', '什么时候分解有意义', '典型拓扑', 'Topology 从部署前选择演进到运行时有界修复', '通信可以压缩成 latent，但 contract 不能一起消失', 'Behavioral belief 不等于 authenticated identity', 'Message 不是 State', 'Pairwise coupling 不能外推 group dynamics']。<!-- existing:SF-2026-ARXIV-2605-18067:end -->
<!-- delta:SF-2026-ARXIV-2605-18067:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18067:end -->
<!-- books-review:SF-2026-ARXIV-2605-18067:end -->
<!-- books-review:SF-2026-ARXIV-2605-18071:start -->
<!-- existing:SF-2026-ARXIV-2605-18071:start -->已顺读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节 ['books/part-05-inference-system/44-decode.md', 'books/part-05-inference-system/46-continuous-batching.md']；正文主线 headings=['本章要回答的问题', '如果完全不缓存', '为什么缓存 K/V 而不是 Query', '逻辑 Shape 与容量公式', '一个容量小例子', 'KV Cache 的生命周期', 'Segmented Execution 必须在训练与推理共享同一语义', 'Prefix reuse', 'KV 从生成私有状态演进为受约束的下游读出接口', 'Structured knowledge 只有进入 physical access plan 才改变 KV 成本']。<!-- existing:SF-2026-ARXIV-2605-18071:end -->
<!-- delta:SF-2026-ARXIV-2605-18071:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18071:end -->
<!-- books-review:SF-2026-ARXIV-2605-18071:end -->
<!-- books-review:SF-2026-ARXIV-2605-18106:start -->
<!-- existing:SF-2026-ARXIV-2605-18106:start -->已顺读 `books/part-04-training-system/28-pretraining.md` 与相邻章节 ['books/part-04-training-system/27-data.md', 'books/part-04-training-system/29-sft.md']；正文主线 headings=['本章要回答的问题', '从随机参数开始会发生什么', 'Next-token objective', '一个 token loss 小例子', 'Perplexity 能回答什么', '一次 training step 的状态流', 'Residual Path 也可以成为随 Depth 与 Time 演化的训练状态', 'Optimizer 不是与参数化无关的旋钮', 'Optimizer State Allocation 也应服从参数角色', 'Batch、tokens 与 optimizer steps 不是同一计量']。<!-- existing:SF-2026-ARXIV-2605-18106:end -->
<!-- delta:SF-2026-ARXIV-2605-18106:start -->当前 optimizer 叙述未把 embedding/LM-head/SwiGLU/MoE-router 的参数对称性作为 optimizer state/action compatibility contract；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18106:end -->
<!-- books-review:SF-2026-ARXIV-2605-18106:end -->
<!-- books-review:SF-2026-ARXIV-2605-18165:start -->
<!-- existing:SF-2026-ARXIV-2605-18165:start -->已顺读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节 ['books/part-03-multimodal-world-models/23-multimodal-representation.md', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md']；正文主线 headings=['本章要回答的问题', '从一个共同问题开始', '为什么 Autoregressive 是合理起点', 'Diffusion：用迭代修正换并行状态更新', 'Masked generation：未知位置与已知位置', 'Editable tokens 与 commit boundary', 'Self-revision：并行位置必须在 Commit 前保持可撤销', '生成 Workflow 也可以被训练进 Intermediate State', 'Block Diffusion：局部自回归与块内并行', 'Draft、Verify 与 Correct 不是同一件事']。<!-- existing:SF-2026-ARXIV-2605-18165:end -->
<!-- delta:SF-2026-ARXIV-2605-18165:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18165:end -->
<!-- books-review:SF-2026-ARXIV-2605-18165:end -->
<!-- books-review:SF-2026-ARXIV-2605-18271:start -->
<!-- existing:SF-2026-ARXIV-2605-18271:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18271:end -->
<!-- delta:SF-2026-ARXIV-2605-18271:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18271:end -->
<!-- books-review:SF-2026-ARXIV-2605-18271:end -->
<!-- books-review:SF-2026-ARXIV-2605-18401:start -->
<!-- existing:SF-2026-ARXIV-2605-18401:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-18401:end -->
<!-- delta:SF-2026-ARXIV-2605-18401:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18401:end -->
<!-- books-review:SF-2026-ARXIV-2605-18401:end -->
<!-- books-review:SF-2026-ARXIV-2605-18414:start -->
<!-- existing:SF-2026-ARXIV-2605-18414:start -->已顺读 `books/part-07-agent/83-mcp.md` 与相邻章节 ['books/part-07-agent/82-multi-agent.md', 'books/part-07-agent/84-agent-platform.md']；正文主线 headings=['本章要回答的问题', '为什么需要协议层', 'Host、Client、Server', 'Data Layer 与 Transport Layer', 'Server Primitives', 'Lifecycle 与 Version Contract', 'Update 2026-07-29 — 从连接会话到显式请求契约', 'MCP 不等于 Tool Authorization', 'Sampling、Elicitation 与递归能力', 'MCP 与 Workflow/Multi-Agent 的边界']。<!-- existing:SF-2026-ARXIV-2605-18414:end -->
<!-- delta:SF-2026-ARXIV-2605-18414:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18414:end -->
<!-- books-review:SF-2026-ARXIV-2605-18414:end -->
<!-- books-review:SF-2026-ARXIV-2605-18421:start -->
<!-- existing:SF-2026-ARXIV-2605-18421:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18421:end -->
<!-- delta:SF-2026-ARXIV-2605-18421:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18421:end -->
<!-- books-review:SF-2026-ARXIV-2605-18421:end -->
<!-- books-review:SF-2026-ARXIV-2605-18498:start -->
<!-- existing:SF-2026-ARXIV-2605-18498:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-18498:end -->
<!-- delta:SF-2026-ARXIV-2605-18498:start -->当前 evaluation 章缺少将 MoE load balance 与 functional specialization 分开、并用干预验证而非只看 routing frequency 的契约；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18498:end -->
<!-- books-review:SF-2026-ARXIV-2605-18498:end -->
<!-- books-review:SF-2026-ARXIV-2605-18565:start -->
<!-- existing:SF-2026-ARXIV-2605-18565:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18565:end -->
<!-- delta:SF-2026-ARXIV-2605-18565:start -->当前 memory 章覆盖版本与冲突，但没有把 multi-target interference、update history 与 aggregate reasoning 组合成一条验收轴；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18565:end -->
<!-- books-review:SF-2026-ARXIV-2605-18565:end -->
<!-- books-review:SF-2026-ARXIV-2605-18583:start -->
<!-- existing:SF-2026-ARXIV-2605-18583:start -->已顺读 `books/part-06-ai-infrastructure/72-security.md` 与相邻章节 ['books/part-06-ai-infrastructure/71-multi-tenant.md', 'books/part-06-ai-infrastructure/73-production-best-practice.md']；正文主线 headings=['本章要回答的问题', '从资产与信任边界开始', '生命周期威胁', '隐私检测是 Policy-bound Sensor，不是安全判决', '从独立 Span 到关系感知的本地 Sanitization', 'Differential Privacy 先定义被保护对象，再选择机制', 'Privacy Accountant 必须与真实实现同构', 'Capability Access Control 可以前移到训练状态', 'Policy-as-Data：可更新规则与模型判断必须分开版本化', '从“文本是否恶意”到“谁获得了行为控制权”']。<!-- existing:SF-2026-ARXIV-2605-18583:end -->
<!-- delta:SF-2026-ARXIV-2605-18583:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18583:end -->
<!-- books-review:SF-2026-ARXIV-2605-18583:end -->
<!-- books-review:SF-2026-ARXIV-2605-18607:start -->
<!-- existing:SF-2026-ARXIV-2605-18607:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-18607:end -->
<!-- delta:SF-2026-ARXIV-2605-18607:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18607:end -->
<!-- books-review:SF-2026-ARXIV-2605-18607:end -->
<!-- books-review:SF-2026-ARXIV-2605-18652:start -->
<!-- existing:SF-2026-ARXIV-2605-18652:start -->已顺读 `books/part-07-agent/77-memory.md` 与相邻章节 ['books/part-07-agent/76-rag.md', 'books/part-07-agent/78-tool-calling.md']；正文主线 headings=['本章要回答的问题', 'Context 与 Memory 的状态边界', 'Memory 类型是用途，不只是存储介质', 'Memory Write 是高风险决策', 'Write / Hold 不足以定义下一状态', '从 Outcome Reward 到 Content-level Credit：归因只能约束写入，不能成为真值', 'Memory Read 是受约束检索', '从按需读取到选择性主动干预', '从一次 Top-k 检索到有预算的关联回忆', 'Fact State 与 Retrieval-policy State 必须分离']。<!-- existing:SF-2026-ARXIV-2605-18652:end -->
<!-- delta:SF-2026-ARXIV-2605-18652:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18652:end -->
<!-- books-review:SF-2026-ARXIV-2605-18652:end -->
<!-- books-review:SF-2026-ARXIV-2605-18693:start -->
<!-- existing:SF-2026-ARXIV-2605-18693:start -->已顺读 `books/part-07-agent/84-agent-platform.md` 与相邻章节 ['books/part-07-agent/83-mcp.md']；正文主线 headings=['本章要回答的问题', 'Agent 改变了平台的控制对象', 'Serving 结束不等于 Agent 任务结束', 'Agent Definition 与 Run Identity', '可复用 Skill 不是一个 Prompt 文件', '从 Skill Catalog 到 Competence-aware Orchestration', '从 Trajectory 到 Skill 是一次受治理的 Compilation', 'Skill Compiler 必须绑定 Target Profile，而不是只绑定模型名', 'Self-evolution Admission 需要 Anytime-valid Acceptor', 'Workspace 是长期行动的隔离单元']。<!-- existing:SF-2026-ARXIV-2605-18693:end -->
<!-- delta:SF-2026-ARXIV-2605-18693:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18693:end -->
<!-- books-review:SF-2026-ARXIV-2605-18693:end -->
<!-- books-review:SF-2026-ARXIV-2605-18697:start -->
<!-- existing:SF-2026-ARXIV-2605-18697:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18697:end -->
<!-- delta:SF-2026-ARXIV-2605-18697:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18697:end -->
<!-- books-review:SF-2026-ARXIV-2605-18697:end -->
<!-- books-review:SF-2026-ARXIV-2605-18703:start -->
<!-- existing:SF-2026-ARXIV-2605-18703:start -->已顺读 `books/part-07-agent/81-workflow.md` 与相邻章节 ['books/part-07-agent/80-reflection.md', 'books/part-07-agent/82-multi-agent.md']；正文主线 headings=['本章要回答的问题', '一个循环为什么不够', 'State Machine 是基本模型', 'Failure attribution、perception routing 与 sticky state ownership', 'Review notes', '从“对象已保存”到“状态已激活”', 'Deterministic Spine，Agentic Nodes', '从一次性脚本到平台拥有的可编辑 DAG', 'Template、Realized Graph 与 Trace 不是同一个对象', 'Offline World 是可验证的数据工厂，不是 Live Workflow 的替身']。<!-- existing:SF-2026-ARXIV-2605-18703:end -->
<!-- delta:SF-2026-ARXIV-2605-18703:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18703:end -->
<!-- books-review:SF-2026-ARXIV-2605-18703:end -->
<!-- books-review:SF-2026-ARXIV-2605-18710:start -->
<!-- existing:SF-2026-ARXIV-2605-18710:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-18710:end -->
<!-- delta:SF-2026-ARXIV-2605-18710:start -->当前 multimodal/distributed training 章缺少空间复用时 module placement、GPU share 与 interference budget 的联合 owner；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18710:end -->
<!-- books-review:SF-2026-ARXIV-2605-18710:end -->
<!-- books-review:SF-2026-ARXIV-2605-18739:start -->
<!-- existing:SF-2026-ARXIV-2605-18739:start -->已顺读 `books/part-04-training-system/36-distributed-training.md` 与相邻章节 ['books/part-04-training-system/35-checkpoint.md', 'books/part-04-training-system/37-tensor-parallel.md']；正文主线 headings=['本章要回答的问题', '单卡为什么会失败', '从本机协作到分布式执行', '先分清五个通信层次', 'Collective 是群体语义，不是一种算法', '用 Alpha-Beta 模型建立下界直觉', 'Ring、Tree 与 Butterfly 在优化什么', 'MPI、NCCL、UCX、UCC 与 NIXL 的边界', 'Collective 进入计算图后，Completion 也成为 Autograd 语义', '从 Collective Call 到 Kernel 内 Remote Memory']。<!-- existing:SF-2026-ARXIV-2605-18739:end -->
<!-- delta:SF-2026-ARXIV-2605-18739:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-18739:end -->
<!-- books-review:SF-2026-ARXIV-2605-18739:end -->
<!-- books-review:SF-2026-ARXIV-2605-18750:start -->
<!-- existing:SF-2026-ARXIV-2605-18750:start -->已顺读 `books/part-04-training-system/38-pipeline-parallel.md` 与相邻章节 ['books/part-04-training-system/37-tensor-parallel.md', 'books/part-04-training-system/39-zero.md']；正文主线 headings=['本章要回答的问题', '只有 Layer Partition 会发生什么', 'Micro-batch 怎样填充 Pipeline', 'Bubble 从哪里来', 'GPipe：先 Forward，再 Backward', '1F1B：缩短 Activation Lifetime', '异步 Pipeline：去掉 Bubble 会把成本移到参数版本', 'Interleaving 为什么引入 Virtual Stages', 'Boundary Communication 在传什么', 'Stage Balance 比平均 Layer 数更重要']。<!-- existing:SF-2026-ARXIV-2605-18750:end -->
<!-- delta:SF-2026-ARXIV-2605-18750:start -->当前 pipeline 章以 schedule 为主，但没有在运行时以真实 task readiness 取得 dispatch authority并保留静态 schedule fallback；保留为写回增量。<!-- delta:SF-2026-ARXIV-2605-18750:end -->
<!-- books-review:SF-2026-ARXIV-2605-18750:end -->
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
<!-- books-review:SF-2026-ARXIV-2605-20251:start -->
<!-- existing:SF-2026-ARXIV-2605-20251:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-20251:end -->
<!-- delta:SF-2026-ARXIV-2605-20251:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-20251:end -->
<!-- books-review:SF-2026-ARXIV-2605-20251:end -->
<!-- books-review:SF-2026-ARXIV-2605-20270:start -->
<!-- existing:SF-2026-ARXIV-2605-20270:start -->已顺读 `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节 ['books/part-06-ai-infrastructure/65-kai-scheduler.md', 'books/part-06-ai-infrastructure/67-monitoring.md']；正文主线 headings=['本章要回答的问题', '为什么“选一个分数”不是评估系统', 'HTTP 成功只是质量判断的第一道门', '从目标到证据，而不是从指标到目标', '第一个不变量：评估声明必须绑定完整对象', 'Evaluation Identity 必须包含 Harness 与 Environment', '第二个不变量：评估结论总是相对于分布', '平均值、切片与不确定性', '评估对象有四个层次', 'Model Evaluation']。<!-- existing:SF-2026-ARXIV-2605-20270:end -->
<!-- delta:SF-2026-ARXIV-2605-20270:start -->当前 owner 与相邻章已覆盖相同 state/control/evaluation contract；exact-v1 作为受限证据保留，但不重复追加正文。<!-- delta:SF-2026-ARXIV-2605-20270:end -->
<!-- books-review:SF-2026-ARXIV-2605-20270:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260519-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260519 | — | independent-semantic-audit.json#SA-20260519-FP;independent-semantic-audit.json#SA-20260519-FN | passed |
| SA-20260519-EVIDENCE | fresh-context:may2026-day01 | evidence | review:SF-2026-ARXIV-2605-17734 | — | exact-v1-review-independent.json#60-of-60 | passed |
| SA-20260519-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-FAILURE-TIERED-CHECKPOINT | — | independent-semantic-audit.json#selection | passed |
| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | — | post-write-semantic-audit.json round 3：18/18 canonical H2、前向承接、后向收束、semantic fields 与 exact-v1 boundary 全部通过 | passed |

## 8. Ignored Noise

643 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`。其中 20 项是独立审计降级的 false positive；每项说明具体机制、排除边界与重开条件。

## 9. Recommended Action

05-19 已完成 18/18 post-write semantic audit；后续只在新证据改变机制判断或章节 owner 时重开。

## 10. Repository Changes

- 更新 2026-05-19 Daily、独立 screening/evidence/Books comparison/audit receipts。
- Root 已写回共享 Books；本 post-write reviewer 未修改 Books，也未 stage、commit 或 push。

## 11. Open Questions

- 当前无未解决 Books finding；后续关注新证据是否改变这些受限机制的适用边界。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [Harnessing LLM Agents with Skill Programs](https://arxiv.org/html/2605.17734v1) — arXiv:2605.17734v1；first-public 2026-05-18；accessed 2026-09-01
- [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/html/2605.17757v1) — arXiv:2605.17757v1；first-public 2026-05-18；accessed 2026-09-01
- [Revisiting the Adam-SGD Gap in LLM Pre-Training: The Role of Large Effective Learning Rates](https://arxiv.org/html/2605.17787v1) — arXiv:2605.17787v1；first-public 2026-05-18；accessed 2026-09-01
- [TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training](https://arxiv.org/html/2605.17821v1) — arXiv:2605.17821v1；first-public 2026-05-18；accessed 2026-09-01
- [Remembering More, Risking More: Longitudinal Safety Risks in Memory-Equipped LLM Agents](https://arxiv.org/html/2605.17830v1) — arXiv:2605.17830v1；first-public 2026-05-18；accessed 2026-09-01
- [SNLP: Layer-Parallel Inference via Structured Newton Corrections](https://arxiv.org/html/2605.17842v1) — arXiv:2605.17842v1；first-public 2026-05-18；accessed 2026-09-01
- [Generating Pretraining Tokens from Organic Data for Data-Bound Scaling](https://arxiv.org/html/2605.17849v1) — arXiv:2605.17849v1；first-public 2026-05-18；accessed 2026-09-01
- [$\boldsymbol{f}$-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](https://arxiv.org/html/2605.17862v1) — arXiv:2605.17862v1；first-public 2026-05-18；accessed 2026-09-01
- [PAIR: Prefix-Aware Internal Reward Model for Multi-Turn Agent Optimization](https://arxiv.org/html/2605.17877v1) — arXiv:2605.17877v1；first-public 2026-05-18；accessed 2026-09-01
- [Guard: Scalable Straggler Detection and Node Health Management for Large-Scale Training](https://arxiv.org/html/2605.17879v1) — arXiv:2605.17879v1；first-public 2026-05-18；accessed 2026-09-01
- [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/html/2605.17889v1) — arXiv:2605.17889v1；first-public 2026-05-18；accessed 2026-09-01
- [WorldArena 2.0: Extending Embodied World Model Benchmarking on Modality, Functionality and Platform](https://arxiv.org/html/2605.17912v1) — arXiv:2605.17912v1；first-public 2026-05-18；accessed 2026-09-01
- [An Efficient Streaming Video Understanding Framework with Agentic Control](https://arxiv.org/html/2605.17921v1) — arXiv:2605.17921v1；first-public 2026-05-18；accessed 2026-09-01
- [AdaptiveLoad: Towards Efficient Video Diffusion Transformer Training](https://arxiv.org/html/2605.17923v1) — arXiv:2605.17923v1；first-public 2026-05-18；accessed 2026-09-01
- [Prompt Compression in Diffusion Large Language Models: Evaluating LLMLingua-2 on LLaDA](https://arxiv.org/html/2605.17932v1) — arXiv:2605.17932v1；first-public 2026-05-18；accessed 2026-09-01
- [A More Word-like Image Tokenization for MLLMs](https://arxiv.org/html/2605.17954v1) — arXiv:2605.17954v1；first-public 2026-05-18；accessed 2026-09-01
- [LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection](https://arxiv.org/html/2605.17986v1) — arXiv:2605.17986v1；first-public 2026-05-18；accessed 2026-09-01
- [Predictive Prefetching for Retrieval-Augmented Generation](https://arxiv.org/html/2605.17989v1) — arXiv:2605.17989v1；first-public 2026-05-18；accessed 2026-09-01
- [PipeANN-Filter: An Efficient Filtered Vector Search System on SSD](https://arxiv.org/html/2605.17992v1) — arXiv:2605.17992v1；first-public 2026-05-18；accessed 2026-09-01
- [Verify-Gated Completion as Admission Control in a Governed Multi-Agent Runtime: A Bounded Architecture Case Study](https://arxiv.org/html/2605.17998v1) — arXiv:2605.17998v1；first-public 2026-05-18；accessed 2026-09-01
- [PROTEA: Offline Evaluation and Iterative Refinement for Multi-Agent LLM Workflows](https://arxiv.org/html/2605.18032v1) — arXiv:2605.18032v1；first-public 2026-05-18；accessed 2026-09-01
- [OmniSelect: Dynamic Modality-Aware Token Compression for Efficient Omni-modal Large Language Models](https://arxiv.org/html/2605.18041v1) — arXiv:2605.18041v1；first-public 2026-05-18；accessed 2026-09-01
- [Protection Is (Nearly) All You Need: Structural Protection Dominates Scoring in Globally Capped KV Eviction](https://arxiv.org/html/2605.18053v1) — arXiv:2605.18053v1；first-public 2026-05-18；accessed 2026-09-01
- [PPAI: Enabling Personalized LLM Agent Interoperability for Collaborative Edge Intelligence](https://arxiv.org/html/2605.18067v1) — arXiv:2605.18067v1；first-public 2026-05-18；accessed 2026-09-01
- [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://arxiv.org/html/2605.18071v1) — arXiv:2605.18071v1；first-public 2026-05-18；accessed 2026-09-01
- [Symmetry-Compatible Principle for Optimizer Design: Embeddings, LM Heads, SwiGLU MLPs, and MoE Routers](https://arxiv.org/html/2605.18106v1) — arXiv:2605.18106v1；first-public 2026-05-18；accessed 2026-09-01
- [Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs](https://arxiv.org/html/2605.18165v1) — arXiv:2605.18165v1；first-public 2026-05-18；accessed 2026-09-01
- [From Volume to Value: Preference-Aligned Memory Construction for On-Device RAG](https://arxiv.org/html/2605.18271v1) — arXiv:2605.18271v1；first-public 2026-05-18；accessed 2026-09-01
- [SkillsVote: Lifecycle Governance of Agent Skills from Collection, Recommendation to Evolution](https://arxiv.org/html/2605.18401v1) — arXiv:2605.18401v1；first-public 2026-05-18；accessed 2026-09-01
- [Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control](https://arxiv.org/html/2605.18414v1) — arXiv:2605.18414v1；first-public 2026-05-18；accessed 2026-09-01
- [EvoMemBench: Benchmarking Agent Memory from a Self-Evolving Perspective](https://arxiv.org/html/2605.18421v1) — arXiv:2605.18421v1；first-public 2026-05-18；accessed 2026-09-01
- [DBES: A Systematic Benchmark and Metric Suite for Evaluating Expert Specialization in Large-Scale MoEs](https://arxiv.org/html/2605.18498v1) — arXiv:2605.18498v1；first-public 2026-05-18；accessed 2026-09-01
- [MINTEval: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/html/2605.18565v1) — arXiv:2605.18565v1；first-public 2026-05-18；accessed 2026-09-01
- [Overeager Coding Agents: Measuring Out-of-Scope Actions on Benign Tasks](https://arxiv.org/html/2605.18583v1) — arXiv:2605.18583v1；first-public 2026-05-19；accessed 2026-09-01
- [Forecasting Downstream Performance of LLMs With Proxy Metrics](https://arxiv.org/html/2605.18607v1) — arXiv:2605.18607v1；first-public 2026-05-19；accessed 2026-09-01
- [MementoGUI: Learning Agentic Multimodal Memory Control for Long-Horizon GUI Agents](https://arxiv.org/html/2605.18652v1) — arXiv:2605.18652v1；first-public 2026-05-19；accessed 2026-09-01
- [SkillGenBench: Benchmarking Skill Generation Pipelines for LLM Agents](https://arxiv.org/html/2605.18693v1) — arXiv:2605.18693v1；first-public 2026-05-19；accessed 2026-09-01
- [PopPy: Opportunistically Exploiting Parallelism in Python Compound AI Applications](https://arxiv.org/html/2605.18697v1) — arXiv:2605.18697v1；first-public 2026-05-19；accessed 2026-09-01
- [EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL](https://arxiv.org/html/2605.18703v1) — arXiv:2605.18703v1；first-public 2026-05-19；accessed 2026-09-01
- [Mosaic: Towards Efficient Training of Multimodal Models with Spatial Resource Multiplexing](https://arxiv.org/html/2605.18710v1) — arXiv:2605.18710v1；first-public 2026-05-19；accessed 2026-09-01
- [LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation](https://arxiv.org/html/2605.18739v1) — arXiv:2605.18739v1；first-public 2026-05-19；accessed 2026-09-01
- [A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability](https://arxiv.org/html/2605.18750v1) — arXiv:2605.18750v1；first-public 2026-05-19；accessed 2026-09-01
- [ESLD (External Surrogate Latent Defense): A Latent-Space Architecture for Faster, Stronger Prompt-Injection Defense](https://arxiv.org/html/2605.18918v1) — arXiv:2605.18918v1；first-public 2026-05-18；accessed 2026-09-01
- [OEP: Poisoning Self-Evolving LLM Agents via Locally Correct but Non-Transferable Experiences](https://arxiv.org/html/2605.18930v1) — arXiv:2605.18930v1；first-public 2026-05-18；accessed 2026-09-01
- [Agent Security is a Systems Problem](https://arxiv.org/html/2605.18991v1) — arXiv:2605.18991v1；first-public 2026-05-19；accessed 2026-09-01
- [Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency](https://arxiv.org/html/2605.19008v1) — arXiv:2605.19008v1；first-public 2026-05-19；accessed 2026-09-01
- [KVBuffer: IO-aware Serving for Linear Attention](https://arxiv.org/html/2605.19049v1) — arXiv:2605.19049v1；first-public 2026-05-19；accessed 2026-09-01
- [DecisionBench: A Benchmark for Emergent Delegation in Long-Horizon Agentic Workflows](https://arxiv.org/html/2605.19099v1) — arXiv:2605.19099v1；first-public 2026-05-19；accessed 2026-09-01
- [Heterogeneity-Aware Dataset Scheduling for Efficient Audio Large Language Model Training](https://arxiv.org/html/2605.19101v1) — arXiv:2605.19101v1；first-public 2026-05-19；accessed 2026-09-01
- [POLAR-Bench: A Diagnostic Benchmark for Privacy-Utility Trade-offs in LLM Agents](https://arxiv.org/html/2605.19127v1) — arXiv:2605.19127v1；first-public 2026-05-19；accessed 2026-09-01
- [Learning to Hand Off: Provably Convergent Workflow Learning under Interface Constraints](https://arxiv.org/html/2605.19140v1) — arXiv:2605.19140v1；first-public 2026-05-19；accessed 2026-09-01
- [Progressive Autonomy as Preference Learning: A Formalization of Trust Calibration for Agentic Tool Use](https://arxiv.org/html/2605.19151v1) — arXiv:2605.19151v1；first-public 2026-05-19；accessed 2026-09-01
- [Modeling the Impact of Fiber Latency on Compute-Communication Overlap in Geo-Distributed Multi-Datacenter AI Training](https://arxiv.org/html/2605.19169v1) — arXiv:2605.19169v1；first-public 2026-05-19；accessed 2026-09-01
- [Hallucination as Exploit: Evidence-Carrying Multimodal Agents](https://arxiv.org/html/2605.19192v1) — arXiv:2605.19192v1；first-public 2026-05-19；accessed 2026-09-01
- [Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection](https://arxiv.org/html/2605.19193v1) — arXiv:2605.19193v1；first-public 2026-05-19；accessed 2026-09-01
- [Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?](https://arxiv.org/html/2605.19196v1) — arXiv:2605.19196v1；first-public 2026-05-19；accessed 2026-09-01
- [Rotation-Aligned Key Channel Pruning for Efficient Vision-Language Model Inference](https://arxiv.org/html/2605.19218v1) — arXiv:2605.19218v1；first-public 2026-05-19；accessed 2026-09-01
- [Diagnosing Multi-step Reasoning Failures in Black-box LLMs via Stepwise Confidence Attribution](https://arxiv.org/html/2605.19228v1) — arXiv:2605.19228v1；first-public 2026-05-19；accessed 2026-09-01
- [ProcCtrlBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents](https://arxiv.org/html/2605.20251v1) — arXiv:2605.20251v1；first-public 2026-05-18；accessed 2026-09-01
- [Conformal Selective Acting: Anytime-Valid Risk Control for RLVR-Trained LLMs](https://arxiv.org/html/2605.20270v1) — arXiv:2605.20270v1；first-public 2026-05-19；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

Coverage、Evidence 与 Books Gate 均已闭合；第三轮 post-write 顺读复验为 18/18 passed，ordinary pending=0、unresolved findings=0。
