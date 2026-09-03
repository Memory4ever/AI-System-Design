# Daily Research — 2026-05-10

**Research Date:** 2026-05-10

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-09 09:00:00 ～ 2026-05-10 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；DataCite 只用于 identity/date/abstract recovery；技术结论绑定 official arXiv exact-v1。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。29 项 Books 写回通过独立 post-write 语义与 placement 复核。

## Executive Summary

相邻月份 v2 snapshot 含 91,841 条 raw records；严格窗口注册 436 条 identity。436/436 完成 title+abstract 语义筛选；独立审计将 author 的 42/394 重判为 57/379，其中 15 个 false negative 经 exact-v1 challenge 后进入 denominator。57/57 official exact-v1 已读取并记录 Method、evaluation、limitations 与 artifact boundary；blocked=0，29 项进入 root 串行 Books queue，本 reviewer 未修改共享 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-10 |
| Window End | 2026-05-10 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260510-V2-FRESH-AUDIT |
| Denominator Frozen At | 2026-09-01T03:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-09T09:00:00+08:00 | 2026-05-10T09:00:00+08:00 | 2026-09-01T03:20:00+08:00 | DataCite v2 prefixes 00..99 + full semantic screen + exact-v1 HTML | checked | 436 | SF-2026-ARXIV-2605-08586;SF-2026-ARXIV-2605-08587;SF-2026-ARXIV-2605-08590;SF-2026-ARXIV-2605-08594;SF-2026-ARXIV-2605-08621;SF-2026-ARXIV-2605-08632;SF-2026-ARXIV-2605-08636;SF-2026-ARXIV-2605-08639;SF-2026-ARXIV-2605-08646;SF-2026-ARXIV-2605-08647;SF-2026-ARXIV-2605-08658;SF-2026-ARXIV-2605-08666;SF-2026-ARXIV-2605-08678;SF-2026-ARXIV-2605-08715;SF-2026-ARXIV-2605-08717;SF-2026-ARXIV-2605-08737;SF-2026-ARXIV-2605-08747;SF-2026-ARXIV-2605-08761;SF-2026-ARXIV-2605-08769;SF-2026-ARXIV-2605-08828;SF-2026-ARXIV-2605-08835;SF-2026-ARXIV-2605-08838;SF-2026-ARXIV-2605-08840;SF-2026-ARXIV-2605-08862;SF-2026-ARXIV-2605-08871;SF-2026-ARXIV-2605-08876;SF-2026-ARXIV-2605-08879;SF-2026-ARXIV-2605-08894;SF-2026-ARXIV-2605-08908;SF-2026-ARXIV-2605-08913;SF-2026-ARXIV-2605-08927;SF-2026-ARXIV-2605-08962;SF-2026-ARXIV-2605-08982;SF-2026-ARXIV-2605-09023;SF-2026-ARXIV-2605-09033;SF-2026-ARXIV-2605-09045;SF-2026-ARXIV-2605-09055;SF-2026-ARXIV-2605-09070;SF-2026-ARXIV-2605-09076;SF-2026-ARXIV-2605-09126;SF-2026-ARXIV-2605-09163;SF-2026-ARXIV-2605-09168;SF-2026-ARXIV-2605-09192;SF-2026-ARXIV-2605-09204;SF-2026-ARXIV-2605-09218;SF-2026-ARXIV-2605-09225;SF-2026-ARXIV-2605-09227;SF-2026-ARXIV-2605-09241;SF-2026-ARXIV-2605-10980;SF-2026-ARXIV-2605-10987;SF-2026-ARXIV-2605-10990;SF-2026-ARXIV-2605-10993;SF-2026-ARXIV-2605-10999;SF-2026-ARXIV-2605-11002;SF-2026-ARXIV-2605-16359;SF-2026-ARXIV-2605-16360;SF-2026-ARXIV-2605-23951 | pages=100; final_cursor=end; raw=91841; registered=436; screened=436; retained=57; closure=379 | 2026-05-10T00:59:59Z | screening-ledger-final.json#sha256=88f47b960e49acfa5364f5eec7334f54424ec8f255b0bdc591a2e5b5c245e624 | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260510:start -->Recall 与独立语义审计均已闭合：436/436 identity 全量筛选；author 42/394 经 non-author challenge 后重判为 57/379，15 个 false negative 已重开并完成 exact-v1，blocked=0。<!-- coverage:SRC-ARXIV:20260510:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-08586 | arXiv:2605.08586v1 | paper-v1:2605.08586 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08586 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08586 | no |
| SF-2026-ARXIV-2605-08587 | arXiv:2605.08587v1 | paper-v1:2605.08587 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08587 | self | — | new_in_window | MODEL-SELF-ATTENTION | Integrate | books-review:SF-2026-ARXIV-2605-08587 | no |
| SF-2026-ARXIV-2605-08590 | arXiv:2605.08590v1 | paper-v1:2605.08590 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08590 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08590 | no |
| SF-2026-ARXIV-2605-08594 | arXiv:2605.08594v1 | paper-v1:2605.08594 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08594 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2605-08594 | no |
| SF-2026-ARXIV-2605-08621 | arXiv:2605.08621v1 | paper-v1:2605.08621 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08621 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08621 | no |
| SF-2026-ARXIV-2605-08632 | arXiv:2605.08632v1 | paper-v1:2605.08632 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08632 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08632 | no |
| SF-2026-ARXIV-2605-08636 | arXiv:2605.08636v1 | paper-v1:2605.08636 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08636 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08636 | no |
| SF-2026-ARXIV-2605-08639 | arXiv:2605.08639v1 | paper-v1:2605.08639 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08639 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-08639 | no |
| SF-2026-ARXIV-2605-08646 | arXiv:2605.08646v1 | paper-v1:2605.08646 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08646 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08646 | no |
| SF-2026-ARXIV-2605-08647 | arXiv:2605.08647v1 | paper-v1:2605.08647 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08647 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2605-08647 | no |
| SF-2026-ARXIV-2605-08658 | arXiv:2605.08658v1 | paper-v1:2605.08658 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08658 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08658 | no |
| SF-2026-ARXIV-2605-08666 | arXiv:2605.08666v1 | paper-v1:2605.08666 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08666 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08666 | no |
| SF-2026-ARXIV-2605-08678 | arXiv:2605.08678v1 | paper-v1:2605.08678 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08678 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08678 | no |
| SF-2026-ARXIV-2605-08715 | arXiv:2605.08715v1 | paper-v1:2605.08715 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08715 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08715 | no |
| SF-2026-ARXIV-2605-08717 | arXiv:2605.08717v1 | paper-v1:2605.08717 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08717 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-08717 | no |
| SF-2026-ARXIV-2605-08737 | arXiv:2605.08737v1 | paper-v1:2605.08737 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08737 | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08737 | no |
| SF-2026-ARXIV-2605-08747 | arXiv:2605.08747v1 | paper-v1:2605.08747 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08747 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-08747 | no |
| SF-2026-ARXIV-2605-08761 | arXiv:2605.08761v1 | paper-v1:2605.08761 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08761 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08761 | no |
| SF-2026-ARXIV-2605-08769 | arXiv:2605.08769v1 | paper-v1:2605.08769 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08769 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08769 | no |
| SF-2026-ARXIV-2605-08828 | arXiv:2605.08828v1 | paper-v1:2605.08828 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08828 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08828 | no |
| SF-2026-ARXIV-2605-08835 | arXiv:2605.08835v1 | paper-v1:2605.08835 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08835 | self | — | new_in_window | INFER-CONTINUOUS-BATCHING | Integrate | books-review:SF-2026-ARXIV-2605-08835 | no |
| SF-2026-ARXIV-2605-08838 | arXiv:2605.08838v1 | paper-v1:2605.08838 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08838 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-08838 | no |
| SF-2026-ARXIV-2605-08840 | arXiv:2605.08840v1 | paper-v1:2605.08840 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08840 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08840 | no |
| SF-2026-ARXIV-2605-08862 | arXiv:2605.08862v1 | paper-v1:2605.08862 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08862 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-08862 | no |
| SF-2026-ARXIV-2605-08871 | arXiv:2605.08871v1 | paper-v1:2605.08871 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08871 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08871 | no |
| SF-2026-ARXIV-2605-08876 | arXiv:2605.08876v1 | paper-v1:2605.08876 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08876 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-08876 | no |
| SF-2026-ARXIV-2605-08879 | arXiv:2605.08879v1 | paper-v1:2605.08879 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-08879 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08879 | no |
| SF-2026-ARXIV-2605-08894 | arXiv:2605.08894v1 | paper-v1:2605.08894 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08894 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08894 | no |
| SF-2026-ARXIV-2605-08908 | arXiv:2605.08908v1 | paper-v1:2605.08908 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08908 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-08908 | no |
| SF-2026-ARXIV-2605-08913 | arXiv:2605.08913v1 | paper-v1:2605.08913 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08913 | self | — | new_in_window | INFER-DECODE | Integrate | books-review:SF-2026-ARXIV-2605-08913 | no |
| SF-2026-ARXIV-2605-08927 | arXiv:2605.08927v1 | paper-v1:2605.08927 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08927 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2605-08927 | no |
| SF-2026-ARXIV-2605-08962 | arXiv:2605.08962v1 | paper-v1:2605.08962 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-08962 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-08962 | no |
| SF-2026-ARXIV-2605-08982 | arXiv:2605.08982v1 | paper-v1:2605.08982 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-08982 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08982 | no |
| SF-2026-ARXIV-2605-09023 | arXiv:2605.09023v1 | paper-v1:2605.09023 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-09023 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09023 | no |
| SF-2026-ARXIV-2605-09033 | arXiv:2605.09033v1 | paper-v1:2605.09033 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09033 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2605-09033 | no |
| SF-2026-ARXIV-2605-09045 | arXiv:2605.09045v1 | paper-v1:2605.09045 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-09045 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09045 | no |
| SF-2026-ARXIV-2605-09055 | arXiv:2605.09055v1 | paper-v1:2605.09055 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-09055 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09055 | no |
| SF-2026-ARXIV-2605-09070 | arXiv:2605.09070v1 | paper-v1:2605.09070 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-09070 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09070 | no |
| SF-2026-ARXIV-2605-09076 | arXiv:2605.09076v1 | paper-v1:2605.09076 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-09076 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09076 | no |
| SF-2026-ARXIV-2605-09126 | arXiv:2605.09126v1 | paper-v1:2605.09126 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09126 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-09126 | no |
| SF-2026-ARXIV-2605-09163 | arXiv:2605.09163v1 | paper-v1:2605.09163 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-09163 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09163 | no |
| SF-2026-ARXIV-2605-09168 | arXiv:2605.09168v1 | paper-v1:2605.09168 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09168 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2605-09168 | no |
| SF-2026-ARXIV-2605-09192 | arXiv:2605.09192v1 | paper-v1:2605.09192 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-09192 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09192 | no |
| SF-2026-ARXIV-2605-09204 | arXiv:2605.09204v1 | paper-v1:2605.09204 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09204 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2605-09204 | no |
| SF-2026-ARXIV-2605-09218 | arXiv:2605.09218v1 | paper-v1:2605.09218 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09218 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-09218 | no |
| SF-2026-ARXIV-2605-09225 | arXiv:2605.09225v1 | paper-v1:2605.09225 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-09225 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09225 | no |
| SF-2026-ARXIV-2605-09227 | arXiv:2605.09227v1 | paper-v1:2605.09227 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-09227 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09227 | no |
| SF-2026-ARXIV-2605-09241 | arXiv:2605.09241v1 | paper-v1:2605.09241 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-09241 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2605-09241 | no |
| SF-2026-ARXIV-2605-10980 | arXiv:2605.10980v1 | paper-v1:2605.10980 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-10980 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2605-10980 | no |
| SF-2026-ARXIV-2605-10987 | arXiv:2605.10987v1 | paper-v1:2605.10987 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-10987 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-10987 | no |
| SF-2026-ARXIV-2605-10990 | arXiv:2605.10990v1 | paper-v1:2605.10990 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-10990 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2605-10990 | no |
| SF-2026-ARXIV-2605-10993 | arXiv:2605.10993v1 | paper-v1:2605.10993 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-10993 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10993 | no |
| SF-2026-ARXIV-2605-10999 | arXiv:2605.10999v1 | paper-v1:2605.10999 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-10999 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10999 | no |
| SF-2026-ARXIV-2605-11002 | arXiv:2605.11002v1 | paper-v1:2605.11002 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-11002 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-11002 | no |
| SF-2026-ARXIV-2605-16359 | arXiv:2605.16359v1 | paper-v1:2605.16359 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2605-16359 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16359 | no |
| SF-2026-ARXIV-2605-16360 | arXiv:2605.16360v1 | paper-v1:2605.16360 | 2026-W19 | 2026-05-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-16360 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-16360 | no |
| SF-2026-ARXIV-2605-23951 | arXiv:2605.23951v1 | paper-v1:2605.23951 | 2026-W19 | 2026-05-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23951 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23951 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-08586 | RP-727dcea55e2e8743 | deep | arXiv:2605.08586v1 | SRC-ARXIV@arXiv:2605.08586v1 | https://arxiv.org/html/2605.08586v1 §3 Problem and Security Properties; §4 Threat Model; §5 K-Veritas — mechanism: To show that the problem is solvable, we built K-Veritas, a reference implementation in Go that produces signed reports without accessing training data. | https://arxiv.org/html/2605.08586v1 §5 Reference Implementation and Protocol Walkthrough — disclosed scope: We name the underlying problem experiment nonrepudiation: a compliant protocol must bind the numbers in a paper to an actual executed computation in a way the author cannot later alter or deny. | https://arxiv.org/html/2605.08586v1 §6 Discussion; position-paper and prototype boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08586v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08586 | complete |
| SF-2026-ARXIV-2605-08587 | RP-9d5d630f52f2d852 | deep | arXiv:2605.08587v1 | SRC-ARXIV@arXiv:2605.08587v1 | https://arxiv.org/html/2605.08587v1 §3 Kaczmarz Linear Attention — mechanism: We revisit the online-regression objective underlying GDN and, inspired by the Kaczmarz projection method, derive the key-norm-normalized dynamic step size $β_t = η_t / (\/k_t\/_2^2 + ε)$ for residual updates. | https://arxiv.org/html/2605.08587v1 §5 Experiments — disclosed scope: Long-context language modeling remains central to modern sequence modeling, but the quadratic cost of Transformer attention makes scaling computationally prohibitive. Linear recurrent models address this bottleneck by compressing the context into a fixed-size state, making the rule that forgets, writes, and edits information a central design… | https://arxiv.org/html/2605.08587v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08587v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08587 | complete |
| SF-2026-ARXIV-2605-08590 | RP-7ca1483cb04ff517 | deep | arXiv:2605.08590v1 | SRC-ARXIV@arXiv:2605.08590v1 | https://arxiv.org/html/2605.08590v1 §3 Study Design and Methods; §3.4 Evaluation Methodology — mechanism: We introduce epistemic overreach (EO) as a measure for cases where a generated explanation implies more than the available sensing evidence can justify. | https://arxiv.org/html/2605.08590v1 §4 Results — disclosed scope: These findings suggest that evidential grounding should be a first-order evaluation criterion for LLM-generated personal sensing explanations, alongside fluency and plausibility. | https://arxiv.org/html/2605.08590v1 §5.5 Limitations and Future Directions — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08590v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08590 | complete |
| SF-2026-ARXIV-2605-08594 | RP-73b8bca5ff1cb5af | deep | arXiv:2605.08594v1 | SRC-ARXIV@arXiv:2605.08594v1 | https://arxiv.org/html/2605.08594v1 §4 One-Round Localization; §5 Two-Round Localization — mechanism: In this paper, we propose a lightweight, purely algorithmic remedy based on coprime test vectors. | https://arxiv.org/html/2605.08594v1 §6 Evaluation — disclosed scope: Systolic arrays are the dominant compute fabric for neural network inference. Prior work has addressed column-level fault detection efficiently with uniform test patterns, but row-level (PE-level) fault localization within a faulty column remains open without resorting to hardware redundancy. The fundamental obstacle is that uniform test… | https://arxiv.org/html/2605.08594v1 §7 Discussion and Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08594v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08594 | complete |
| SF-2026-ARXIV-2605-08621 | RP-bca89287ef97b2dd | deep | arXiv:2605.08621v1 | SRC-ARXIV@arXiv:2605.08621v1 | https://arxiv.org/html/2605.08621v1 §4 EvidenT Framework — mechanism: While recent LLM-based repair methods show promise for project-level source fixes, they struggle with system-level repair, where failures span multi-language artifacts such as build recipes, scripts, and source archives, and require iterative validation through external build services. | https://arxiv.org/html/2605.08621v1 §5 Evaluation — disclosed scope: Frequent toolchain updates and growing ISA diversity have made system-level software package repair increasingly important. Diagnosing and repairing build failures remains challenging because failures involve heterogeneous evidence, dependency constraints, and architecture-specific build conventions. While recent LLM-based repair methods show promise for project-level source fixes, they struggle… | https://arxiv.org/html/2605.08621v1 §5.6 Failure Analysis and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08621v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08621 | complete |
| SF-2026-ARXIV-2605-08632 | RP-9abad846701171e2 | standard | arXiv:2605.08632v1 | SRC-ARXIV@arXiv:2605.08632v1 | https://arxiv.org/html/2605.08632v1 §3 PARD-2; §3.2 Confidence-Adaptive Token Optimization — mechanism: Speculative decoding accelerates Large Language Models (LLMs) inference by using a lightweight draft model to propose candidate tokens that are verified in parallel by the target model. | https://arxiv.org/html/2605.08632v1 §4 Experiments — disclosed scope: Experiments across diverse models and tasks demonstrate that PARD-2 achieves up to 6.94$\times$ lossless acceleration, surpassing EAGLE-3 by 1.9$\times$ and PARD by 1.3$\times$ on Llama3.1-8B. | https://arxiv.org/html/2605.08632v1 §5 Limitations and Conclusion — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08632v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08632 | complete |
| SF-2026-ARXIV-2605-08636 | RP-52f8e669c3b850f3 | deep | arXiv:2605.08636v1 | SRC-ARXIV@arXiv:2605.08636v1 | https://arxiv.org/html/2605.08636v1 §2 EdgeFlowerTune Benchmark Design; §2.2 Benchmarking Protocols — mechanism: We present EdgeFlowerTune, a deployment-oriented benchmark for federated LLM fine-tuning under realistic edge-system constraints. | https://arxiv.org/html/2605.08636v1 §3 Experimental Settings; §4 Results — disclosed scope: Our benchmark results show that accuracy-only evaluation can lead to misleading conclusions: methods with similar final quality may differ substantially in deployability once realistic system constraints are considered. | https://arxiv.org/html/2605.08636v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08636v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08636 | complete |
| SF-2026-ARXIV-2605-08639 | RP-26c67b7a951f9a60 | deep | arXiv:2605.08639v1 | SRC-ARXIV@arXiv:2605.08639v1 | https://arxiv.org/html/2605.08639v1 §3 Design; §4 Routing-Replay-Guided Load Balancing — mechanism: We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity. | https://arxiv.org/html/2605.08639v1 §5 Evaluation — disclosed scope: Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making them less effective under sharp… | https://arxiv.org/html/2605.08639v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08639v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08639 | complete |
| SF-2026-ARXIV-2605-08646 | RP-5aacbccb47be501c | deep | arXiv:2605.08646v1 | SRC-ARXIV@arXiv:2605.08646v1 | https://arxiv.org/html/2605.08646v1 §3 PAAC — mechanism: In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism. | https://arxiv.org/html/2605.08646v1 §4 Experiments — disclosed scope: Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to… | https://arxiv.org/html/2605.08646v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08646v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08646 | complete |
| SF-2026-ARXIV-2605-08647 | RP-477d37ee2d91a653 | deep | arXiv:2605.08647v1 | SRC-ARXIV@arXiv:2605.08647v1 | https://arxiv.org/html/2605.08647v1 §3 Benchmark Design; §4 Process Metrics — mechanism: To make these vulnerabilities measurable before deployment, we introduce AgentCollabBench, a diagnostic benchmark of 900 human-validated tasks spanning software engineering, DevOps, and data engineering. | https://arxiv.org/html/2605.08647v1 §5 Experiments — disclosed scope: Evaluating four modern LLMs (GPT 4.1 mini, Gemini 2.5 Flash Lite, Qwen-3.5-35B-A3B, and Llama 3.1 8B Instruct), we expose model-specific vulnerability profiles invisible to outcome-only evaluation; Qwen-3.5-35B-A3B, for example, leads on tracer durability and instruction stability, while GPT 4.1 mini leads on leakage containment and false-belief… | https://arxiv.org/html/2605.08647v1 Appendix K Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08647v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08647 | complete |
| SF-2026-ARXIV-2605-08658 | RP-283a9fc57774b690 | standard | arXiv:2605.08658v1 | SRC-ARXIV@arXiv:2605.08658v1 | https://arxiv.org/html/2605.08658v1 §2 Sketch-and-Verify — mechanism: We characterize the K-vs-M trade-off via a Flash Lite scaling sweep, report HumanEval+ saturation on Flash and Pro, and show the method composes cleanly with execution-based selection from the concurrent Semantic Voting line of work. | https://arxiv.org/html/2605.08658v1 §3 Evaluation — disclosed scope: SKETCHVERIFY is a within-tier cost-performance policy, not a universal accuracy improvement. The operational question: a practitioner stuck with a small, cheap code model (here, Gemini 3.1 Flash Lite) for latency, deployment, or budget reasons -- how should they spend a small amount of extra test-time compute?… | https://arxiv.org/html/2605.08658v1 §4 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08658v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08658 | complete |
| SF-2026-ARXIV-2605-08666 | RP-6dbf774fe779b1a1 | deep | arXiv:2605.08666v1 | SRC-ARXIV@arXiv:2605.08666v1 | https://arxiv.org/html/2605.08666v1 §3 Token-Level Analysis; §4 Cancellation Hypothesis — mechanism: To explain this phenomenon, we further show that a token's change in probability is not fully determined by its own advantage; coupled gradient interactions with other tokens also play a non-negligible role. | https://arxiv.org/html/2605.08666v1 §5 Experiments — disclosed scope: Building upon this analysis, we propose the cancellation hypothesis: as a result of coupling, opposing signals cancel out for tokens shared by positive and negative rollouts, while tokens more specific to successful rollouts receive stronger reinforcement, thereby inducing hidden token-level credit assignment from rollout-level rewards. | https://arxiv.org/html/2605.08666v1 Appendix A Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08666v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08666 | complete |
| SF-2026-ARXIV-2605-08678 | RP-ba8ad673f41de82d | deep | arXiv:2605.08678v1 | SRC-ARXIV@arXiv:2605.08678v1 | https://arxiv.org/html/2605.08678v1 §3 MLS-Bench; §3.2 Evaluation Rigor — mechanism: We introduce MLS-Bench, a benchmark for evaluating whether AI systems can invent generalizable and scalable ML methods. | https://arxiv.org/html/2605.08678v1 §4 Experiments; §5 Analysis — disclosed scope: As large language models demonstrate advanced capabilities in reasoning, coding, and engineering tasks, it is increasingly important to understand whether they can discover such methods rather than only apply existing ones. | https://arxiv.org/html/2605.08678v1 §6 Conclusion and Future Work — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08678v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08678 | complete |
| SF-2026-ARXIV-2605-08715 | RP-ee3f899148adcfc4 | deep | arXiv:2605.08715v1 | SRC-ARXIV@arXiv:2605.08715v1 | https://arxiv.org/html/2605.08715v1 §3 AgentForesight — mechanism: In this work, we introduce AgentForesight, a framework that reframes this problem as online auditing: at each step of an unfolding trajectory, an auditor observes only the current prefix and must either continue the run or alarm at the earliest decisive error, without access to future… | https://arxiv.org/html/2605.08715v1 §4 Experiments — disclosed scope: LLM-based multi-agent systems are increasingly deployed on long-horizon tasks, but a single decisive error is often accepted by downstream agents and cascades into trajectory-level failure. Existing work frames this as \emph{post-hoc failure attribution}, diagnosing the responsible agent and step after the trajectory has ended. However, this… | https://arxiv.org/html/2605.08715v1 Appendix G.2 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08715v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08715 | complete |
| SF-2026-ARXIV-2605-08717 | RP-4a4bb5458654d5b8 | deep | arXiv:2605.08717v1 | SRC-ARXIV@arXiv:2605.08717v1 | https://arxiv.org/html/2605.08717v1 §3 PROBE Framework — mechanism: We present PROBE, a failure-anchored framework for structured recovery in software engineering agents. | https://arxiv.org/html/2605.08717v1 §4 Evaluation — disclosed scope: Beyond controlled evaluation, a Microsoft IcM prototype shows that PROBE can attach as a non-intrusive side channel to existing service-diagnosis workflows without changing the agent policy, toolset, or execution budget. | https://arxiv.org/html/2605.08717v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08717v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08717 | complete |
| SF-2026-ARXIV-2605-08737 | RP-f847e0d7e2e0fe9b | standard | arXiv:2605.08737v1 | SRC-ARXIV@arXiv:2605.08737v1 | https://arxiv.org/html/2605.08737v1 §3 Base-Relative Clip-Safety Threshold; §4 K-ary Extension — mechanism: In a single-position Bernoulli reduction, we derive a closed-form base-relative clip-safety threshold lambda*(p,b,c) determined by three measurable quantities: the teacher modal probability, the warm-start mass, and the importance-sampling clip strength. | https://arxiv.org/html/2605.08737v1 §5 Experiments — disclosed scope: On-policy distillation (OPD) is widely used for LLM post-training. When pushed with a reward-extrapolation coefficient lambda &gt; 1, the student can lift past the teacher in domain, but past a threshold lambda* the same step violates the output contract on structured-output tasks. In a single-position Bernoulli… | https://arxiv.org/html/2605.08737v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08737v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08737 | complete |
| SF-2026-ARXIV-2605-08747 | RP-d319a537af2af9c8 | deep | arXiv:2605.08747v1 | SRC-ARXIV@arXiv:2605.08747v1 | https://arxiv.org/html/2605.08747v1 §3 VIGIL Protocol — mechanism: We introduce VIGIL, an evaluation framework that makes terminal commitment independently measurable. | https://arxiv.org/html/2605.08747v1 §4 Experiments — disclosed scope: We introduce VIGIL, an evaluation framework that makes terminal commitment independently measurable. | https://arxiv.org/html/2605.08747v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08747v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08747 | complete |
| SF-2026-ARXIV-2605-08761 | RP-f29853fcb85905f7 | deep | arXiv:2605.08761v1 | SRC-ARXIV@arXiv:2605.08761v1 | https://arxiv.org/html/2605.08761v1 §3 EntCollabBench; Role-specialized workflow design — mechanism: We introduce \textsc{EntCollabBench}, a benchmark for evaluating enterprise multi-agent collaboration. | https://arxiv.org/html/2605.08761v1 §4 Experiments; Appendix G Failure Analysis — disclosed scope: \textsc{EntCollabBench} simulates a permission-isolated organization with 11 role-specialized agents across six departments and contains two evaluation subsets: a Workflow subset, where agents collaboratively modify enterprise system states, and an Approval subset, where agents make policy-grounded decisions. | https://arxiv.org/html/2605.08761v1 Appendix H Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08761v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08761 | complete |
| SF-2026-ARXIV-2605-08769 | RP-86f934d0c6017eee | standard | arXiv:2605.08769v1 | SRC-ARXIV@arXiv:2605.08769v1 | https://arxiv.org/html/2605.08769v1 §2 Formulation; §3 EvoMAS — mechanism: We propose EvoMAS, a framework for execution-time multi-agent workflow construction. | https://arxiv.org/html/2605.08769v1 §4 Experiments — disclosed scope: Large language model (LLM)-based multi-agent systems have shown strong potential on complex tasks through agent specialization, tool use, and collaborative reasoning. However, most automated multi-agent system design methods still follow a one-shot paradigm: a workflow is optimized or selected before execution and then reused unchanged throughout… | https://arxiv.org/html/2605.08769v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08769v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08769 | complete |
| SF-2026-ARXIV-2605-08828 | RP-e517cd8238fb2f59 | deep | arXiv:2605.08828v1 | SRC-ARXIV@arXiv:2605.08828v1 | https://arxiv.org/html/2605.08828v1 §3 EnvTrustBench Framework; §4 Controlled Stress Cases — mechanism: We introduce EnvTrustBench, an agentic framework for benchmarking this failure mode. | https://arxiv.org/html/2605.08828v1 §5 Evaluation and Scaffold Inspection — disclosed scope: Large language model agents increasingly operate through environment-facing scaffolds that expose files, web pages, APIs, and logs. These observations influence tool use, state tracking, and action sequencing, yet their reliability and authority are often uncertain. Environmental grounding is therefore a systems-level problem involving context admission, evidence… | https://arxiv.org/html/2605.08828v1 §6 Limitations and Threats to Validity — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08828v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08828 | complete |
| SF-2026-ARXIV-2605-08835 | RP-7b723ce4e2e16aad | deep | arXiv:2605.08835v1 | SRC-ARXIV@arXiv:2605.08835v1 | https://arxiv.org/html/2605.08835v1 §III SynerDiff Design — mechanism: To address these, we propose SynerDiff, an efficient continuous batching system built on intra-inter level synergy. | https://arxiv.org/html/2605.08835v1 §IV-B Evaluation — disclosed scope: The expansion of Artificial Intelligence-generated content service requires diffusion model serving to simultaneously achieve high throughput and low task end-to-end (E2E) latency. However, existing continuous batching methods suffer from severe resource contention during UNet-VAE concurrency, leading to latency spikes. Furthermore, concurrent multi-task scheduling entails a trade-off… | https://arxiv.org/html/2605.08835v1 §V Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08835v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08835 | complete |
| SF-2026-ARXIV-2605-08838 | RP-7b5593825e3293f0 | deep | arXiv:2605.08838v1 | SRC-ARXIV@arXiv:2605.08838v1 | https://arxiv.org/html/2605.08838v1 §3 Leakage-Free Benchmark Generation — mechanism: We introduce SeedRG, a semi-synthetic benchmark generation pipeline that mitigates knowledge leakage and addresses the issue of benchmark aging. | https://arxiv.org/html/2605.08838v1 §4 Experiments and Robustness Evaluation — disclosed scope: This leads to unreliable evaluation. | https://arxiv.org/html/2605.08838v1 §5 Discussion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08838v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08838 | complete |
| SF-2026-ARXIV-2605-08840 | RP-83c12b92fa7fe857 | standard | arXiv:2605.08840v1 | SRC-ARXIV@arXiv:2605.08840v1 | https://arxiv.org/html/2605.08840v1 §3 ReST-KV — mechanism: In this paper, we propose ReST-KV, a robust KV eviction method that combines layer-wise output Reconstruction and Spatial-Temporal smoothing to provide a more comprehensive perspective for the KV cache eviction task. | https://arxiv.org/html/2605.08840v1 §4 Experiments — disclosed scope: Large language models (LLMs) face growing challenges in efficient generative inference due to the increasing memory demands of Key-Value (KV) caches, especially for long sequences. Existing eviction methods typically retain KV pairs with high attention weights but overlook the impact of attention redistribution caused by token… | https://arxiv.org/html/2605.08840v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08840v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08840 | complete |
| SF-2026-ARXIV-2605-08862 | RP-8d91884cd7f4e90a | deep | arXiv:2605.08862v1 | SRC-ARXIV@arXiv:2605.08862v1 | https://arxiv.org/html/2605.08862v1 §3 BubbleSpec — mechanism: Instead, we propose BubbleSpec, a novel framework that accelerates RL rollouts while strictly keeping the mathematical exactness. | https://arxiv.org/html/2605.08862v1 Appendix A Evaluation — disclosed scope: Extensive evaluations demonstrate that BubbleSpec reduces decoding steps by 50% and increases rollout throughput by up to 1.8x. | https://arxiv.org/html/2605.08862v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08862v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08862 | complete |
| SF-2026-ARXIV-2605-08871 | RP-532f50d788fe3cb8 | deep | arXiv:2605.08871v1 | SRC-ARXIV@arXiv:2605.08871v1 | https://arxiv.org/html/2605.08871v1 §3 Rennala MVR — mechanism: We show that, under a mean-squared smoothness assumption, variance reduction can improve time complexity in relevant parameter regimes. | https://arxiv.org/html/2605.08871v1 §4 Experiments — disclosed scope: Large-scale machine learning models are trained on clusters of machines that exhibit heterogeneous performance due to hardware variability, network delays, and system-level instabilities. In such environments, time complexity rather than iteration complexity becomes the relevant performance metric for optimization algorithms. Recent work by Tyurin and Richtárik… | https://arxiv.org/html/2605.08871v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08871v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08871 | complete |
| SF-2026-ARXIV-2605-08876 | RP-e9d90dadbc4a8910 | deep | arXiv:2605.08876v1 | SRC-ARXIV@arXiv:2605.08876v1 | https://arxiv.org/html/2605.08876v1 §3 OTora Threat Model and Framework — mechanism: We introduce OTora, the first unified, two-stage red-teaming framework for instantiating R-DoS attacks. | https://arxiv.org/html/2605.08876v1 §4 Experiments — disclosed scope: Large Language Models (LLMs) are increasingly deployed as autonomous agents that execute tool-augmented, multi-step tasks, where latency is a critical factor for real-world applications. Yet an overlooked threat is Reasoning-Level Denial-of-Service (R-DoS), in which an attacker preserves task correctness but degrades availability by inflating an agent's… | https://arxiv.org/html/2605.08876v1 Appendix A Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08876v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08876 | complete |
| SF-2026-ARXIV-2605-08879 | RP-5f4f546601e4d240 | deep | arXiv:2605.08879v1 | SRC-ARXIV@arXiv:2605.08879v1 | https://arxiv.org/html/2605.08879v1 §3 Conservative SFT — mechanism: We present Conservative Supervised Fine-Tuning (ConSFT), an optimization objective that adapts to target distributions while mitigating catastrophic forgetting, requiring zero prior data or architectural overhead. | https://arxiv.org/html/2605.08879v1 §4–§5 Simulated and Physical Experiments — disclosed scope: Unconstrained fine-tuning of flow-matching Vision-Language-Action (VLA) models drives dense parameter overwrites, degrading pre-trained capabilities. We present Conservative Supervised Fine-Tuning (ConSFT), an optimization objective that adapts to target distributions while mitigating catastrophic forgetting, requiring zero prior data or architectural overhead. By dynamically scaling learning signals based on… | https://arxiv.org/html/2605.08879v1 §6 Conclusion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08879v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08879 | complete |
| SF-2026-ARXIV-2605-08894 | RP-261e7e50356d5d26 | standard | arXiv:2605.08894v1 | SRC-ARXIV@arXiv:2605.08894v1 | https://arxiv.org/html/2605.08894v1 §5 Smoothness-Aware Quantization — mechanism: In this paper, we show that extremely quantized LLMs suffer from systematic smoothness degradation beyond numerical precision loss. | https://arxiv.org/html/2605.08894v1 §6 Experiments — disclosed scope: To validate it, we introduce a simple smoothness-preserving principle in both post-training quantization and quantization-aware training, and demonstrate that preserving smoothness brings additional gains beyond numerical accuracy. | https://arxiv.org/html/2605.08894v1 Appendix A.7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08894v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08894 | complete |
| SF-2026-ARXIV-2605-08908 | RP-6ffa794712586554 | deep | arXiv:2605.08908v1 | SRC-ARXIV@arXiv:2605.08908v1 | https://arxiv.org/html/2605.08908v1 §IV LERN Reuse Prediction; §V HyDRA Policy — mechanism: We propose a novel clustering-based methodology, LERN, for learning and predicting the reuse behavior of hardware accelerators at the shared cache. | https://arxiv.org/html/2605.08908v1 §VI Evaluation — disclosed scope: The system-level cache is a critical resource shared by processor cores and domain-specific accelerators in heterogeneous systems on chips (SoCs). The strict QoS requirements of accelerators, such as deadlines, can lead to severe performance degradation of processor cores. Thus, managing the shared cache efficiently between cores… | https://arxiv.org/html/2605.08908v1 §VII Conclusion; evaluated accelerator/cache boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08908v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08908 | complete |
| SF-2026-ARXIV-2605-08913 | RP-9f4f9adf9eebacf3 | deep | arXiv:2605.08913v1 | SRC-ARXIV@arXiv:2605.08913v1 | https://arxiv.org/html/2605.08913v1 §3 Experimental Methodology — mechanism: Controlled experiments show that these anomalies originate primarily during the decode phase rather than prefill, are not explained by memory pressure alone, and remain absent on CPU and NVIDIA CUDA backends under identical conditions. | https://arxiv.org/html/2605.08913v1 §4 Results and KV Ablation — disclosed scope: These findings suggest that autoregressive decoding on MPS enters discrete execution regimes that are not captured by coarse-grained benchmarking, highlighting the importance of hardware-aware evaluation for long-context inference. | https://arxiv.org/html/2605.08913v1 §5.2 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08913v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08913 | complete |
| SF-2026-ARXIV-2605-08927 | RP-c346ca6bc9fd442d | deep | arXiv:2605.08927v1 | SRC-ARXIV@arXiv:2605.08927v1 | https://arxiv.org/html/2605.08927v1 §3 Credible Compilation and Verification Workflows — mechanism: We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification. | https://arxiv.org/html/2605.08927v1 §5–§6 Quantitative Comparison — disclosed scope: Formal program verification is a longstanding goal in the field. We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification. Working with the first verified compiler developed by a coding agent (operating under human supervision), we present… | https://arxiv.org/html/2605.08927v1 §8 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08927v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08927 | complete |
| SF-2026-ARXIV-2605-08962 | RP-e442d53861b8c184 | deep | arXiv:2605.08962v1 | SRC-ARXIV@arXiv:2605.08962v1 | https://arxiv.org/html/2605.08962v1 §3 System Overview; §4 Model Parallelization; §5 Workload Balancing — mechanism: As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions. However, existing MLLM systems remain inefficient under dynamic workloads, due to statically coupled decisions of resource allocation and… | https://arxiv.org/html/2605.08962v1 §7 Evaluation — disclosed scope: Our experimental results demonstrate $1.27\times$-$7.57\times$ throughput improvement under production-grade dynamic workloads, as compared to four state-of-the-art systems. | https://arxiv.org/html/2605.08962v1 §8 Discussion; undisclosed production-cluster specifications — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08962v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08962 | complete |
| SF-2026-ARXIV-2605-08982 | RP-c8c5059e38a18238 | standard | arXiv:2605.08982v1 | SRC-ARXIV@arXiv:2605.08982v1 | https://arxiv.org/html/2605.08982v1 §3 Simple PMCTS; §4 PMCTS — mechanism: We introduce Particle MCTS (PMCTS), to our knowledge the first principled parallel MCTS algorithm which is suited for neural network evaluations and can preserve formal policy improvement guarantees. | https://arxiv.org/html/2605.08982v1 §7 Experiments — disclosed scope: Monte Carlo Tree Search (MCTS) is a widely used approach for policy improvement through search with increasing popularity for real world applications. Due to the sequential and deterministic nature of its search, runtime-scaling of MCTS with parallel compute remains a major challenge. We introduce Particle MCTS… | https://arxiv.org/html/2605.08982v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.08982v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-08982 | complete |
| SF-2026-ARXIV-2605-09023 | RP-b536f001d595ff03 | deep | arXiv:2605.09023v1 | SRC-ARXIV@arXiv:2605.09023v1 | https://arxiv.org/html/2605.09023v1 §3 Semantic-Distance Uncertainty — mechanism: LLMs show strong performance in code generation, but their outputs lack correctness guarantees. | https://arxiv.org/html/2605.09023v1 §4 Experiments — disclosed scope: Across LiveCodeBench, MBPP, HumanEval-X and BigCodeBench, spanning Python, Java and C++, our metrics provide strong proxies for correctness, and consistently outperform state-of-the-art sample-based baselines across both closed-source models (GPT-3.5-Turbo, GPT-4o-mini, Gemini-2.5-Flash-Lite, Claude Opus 4.5) and an open-source model (DeepSeek-Coder-V2). | https://arxiv.org/html/2605.09023v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09023v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09023 | complete |
| SF-2026-ARXIV-2605-09033 | RP-468bea2747e8a430 | deep | arXiv:2605.09033v1 | SRC-ARXIV@arXiv:2605.09033v1 | https://arxiv.org/html/2605.09033v1 §III Threat Model; §IV AIR Pipeline — mechanism: We present SHADOWMERGE, a poisoning attack against graph-based agent memory that exploits relation-channel conflicts. | https://arxiv.org/html/2605.09033v1 §V Evaluation — disclosed scope: Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into graph memory so that it is later retrieved and influences agent behavior. Existing… | https://arxiv.org/html/2605.09033v1 §VI Defense Analysis and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09033v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09033 | complete |
| SF-2026-ARXIV-2605-09045 | RP-03c5af40f8b5ef3a | deep | arXiv:2605.09045v1 | SRC-ARXIV@arXiv:2605.09045v1 | https://arxiv.org/html/2605.09045v1 §3 Formal Model; §4 Refinement Proof — mechanism: We introduce containment verification, which locates safety guarantees in the agentic framework itself. | https://arxiv.org/html/2605.09045v1 §5 Case Study — disclosed scope: Agentic frameworks are the software layer through which AI agents act in the world. Existing safety methods intervene on the model and therefore remain conditional on unverifiable properties of learned behavior. We introduce containment verification, which locates safety guarantees in the agentic framework itself. Under havoc… | https://arxiv.org/html/2605.09045v1 §5.1 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09045v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09045 | complete |
| SF-2026-ARXIV-2605-09055 | RP-d390399619f237b2 | standard | arXiv:2605.09055v1 | SRC-ARXIV@arXiv:2605.09055v1 | https://arxiv.org/html/2605.09055v1 §2 Octopus Protocol — mechanism: We present Octopus Protocol, a system that collapses that cost to a single shell command. | https://arxiv.org/html/2605.09055v1 §3 Demonstration — disclosed scope: Recent agentic-robotics systems, from Code-asPolicies to modern vision-language-action (VLA) foundation models, presuppose that drivers, SDKs, or ROS-style primitives for the target hardware already exist. Writing those primitives is the dominant engineering cost of bringing up new hardware for agent control. We present Octopus Protocol, a system… | https://arxiv.org/html/2605.09055v1 §4 Conclusion; no dedicated evaluation or limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09055v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09055 | complete |
| SF-2026-ARXIV-2605-09070 | RP-86c2acb4076f6cae | deep | arXiv:2605.09070v1 | SRC-ARXIV@arXiv:2605.09070v1 | https://arxiv.org/html/2605.09070v1 §3 Distributional ASR — mechanism: We propose two new measures for jailbreak attacks: the Variant Sensitivity Measure (VSM) and Union Coverage (UC). | https://arxiv.org/html/2605.09070v1 §5 Experiments — disclosed scope: We empirically demonstrate the importance of these measures using two attack families across three open-source target models. | https://arxiv.org/html/2605.09070v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09070v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09070 | complete |
| SF-2026-ARXIV-2605-09076 | RP-b33477978941c787 | deep | arXiv:2605.09076v1 | SRC-ARXIV@arXiv:2605.09076v1 | https://arxiv.org/html/2605.09076v1 §4 Method — mechanism: We study decentralized LLM multi-agent systems (LLM-MAS) and propose Self-Anchored Consensus (SAC), a fully decentralized iterative filter-and-refine protocol in which agents iteratively exchange responses, locally evaluate and filter unreliable messages, and refine their own outputs. | https://arxiv.org/html/2605.09076v1 §5 Experiments; §6 Discussion — disclosed scope: Large language model (LLM) agents increasingly collaborate over peer-to-peer networks to improve their reliability. However, these same interactions can also become a source of vulnerability, as unreliable or Byzantine agents may sway neighboring agents toward incorrect conclusions and degrade overall system performance. Existing methods rely on… | https://arxiv.org/html/2605.09076v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09076v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09076 | complete |
| SF-2026-ARXIV-2605-09126 | RP-67cf38b76b5c29ea | deep | arXiv:2605.09126v1 | SRC-ARXIV@arXiv:2605.09126v1 | https://arxiv.org/html/2605.09126v1 §3 Method — mechanism: We propose Cosine Gated Adam Decay (CGAD), a simple, drop-in, age-aware outer optimizer that scales each incoming pseudo-gradient by $σ(τ) = γ(τ) e^{-ατ}$ before it enters Adam's first- and second-moment buffers; the exponential models information decay and the cosine gate $γ(τ)$ smoothly zeroes contributions past a… | https://arxiv.org/html/2605.09126v1 §5 Experiments — disclosed scope: Asynchronous DiLoCo systems may receive pseudo-gradients computed several outer rounds earlier, yet the standard Nesterov outer optimizer does not explicitly condition its update on per-update age. This can make the outer momentum buffer brittle under large controlled delays. We propose Cosine Gated Adam Decay (CGAD), a… | https://arxiv.org/html/2605.09126v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09126v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09126 | complete |
| SF-2026-ARXIV-2605-09163 | RP-44de4457cc6c4397 | deep | arXiv:2605.09163v1 | SRC-ARXIV@arXiv:2605.09163v1 | https://arxiv.org/html/2605.09163v1 §3 FORTIS Benchmark Construction — mechanism: We present \textbf{FORTIS}, a benchmark that evaluates over-privilege in agent skills across two stages: whether a model selects the minimally sufficient skill from a large overlapping library, and whether it executes that skill without expanding into broader tools or actions than the skill permits. | https://arxiv.org/html/2605.09163v1 §4 Experiments — disclosed scope: Large language model agents increasingly operate through an intermediate skill layer that mediates between user intent and concrete task execution. This layer is widely treated as an organizational abstraction, but we argue it is also a privilege boundary that current models routinely exceed. We present \textbf{FORTIS},… | https://arxiv.org/html/2605.09163v1 Appendix H Limitations and Broader Impact — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09163v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09163 | complete |
| SF-2026-ARXIV-2605-09168 | RP-b323cd49fecdbe90 | deep | arXiv:2605.09168v1 | SRC-ARXIV@arXiv:2605.09168v1 | https://arxiv.org/html/2605.09168v1 §3 CIVeX; §5 Evaluation Protocol — mechanism: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN. | https://arxiv.org/html/2605.09168v1 §6 Experiments — disclosed scope: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN. | https://arxiv.org/html/2605.09168v1 §7 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09168v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09168 | complete |
| SF-2026-ARXIV-2605-09192 | RP-68379c99d301832c | standard | arXiv:2605.09192v1 | SRC-ARXIV@arXiv:2605.09192v1 | https://arxiv.org/html/2605.09192v1 §3 Method — mechanism: In this study, we introduce the Posterior Distillation Index (PDI), a trajectory-level metric that quantifies how well a distilled skill is grounded in the task-environment evidence. | https://arxiv.org/html/2605.09192v1 §4 Experiments — disclosed scope: Across 86 runnable tasks, SPARK-generated skills consistently surpass no-skill baselines and outperform human-written skills on student models (inference cost up to 1,000x cheaper than teacher models). | https://arxiv.org/html/2605.09192v1 Appendix L Limitations and Scope — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09192v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09192 | complete |
| SF-2026-ARXIV-2605-09204 | RP-70b7d77018f58879 | deep | arXiv:2605.09204v1 | SRC-ARXIV@arXiv:2605.09204v1 | https://arxiv.org/html/2605.09204v1 §2 Scan Formulation; §3 Model Realization — mechanism: We introduce Latent Bounded Interfaces (LBI), an algorithmic formulation that makes scan-based backpropagation tractable by restricting inter-region communication to a low-dimensional latent interface, $ m_k \in \mathbb{R}^{r}$, where $r \ll d$. | https://arxiv.org/html/2605.09204v1 §4 Experiments — disclosed scope: We demonstrate that LBI maintains model quality across four architectures (Mamba-2, Mamba-3, Transformer, and a Mamba--Transformer hybrid) at 47--61M block parameters. | https://arxiv.org/html/2605.09204v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09204v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09204 | complete |
| SF-2026-ARXIV-2605-09218 | RP-4b56b41cb032b1c3 | deep | arXiv:2605.09218v1 | SRC-ARXIV@arXiv:2605.09218v1 | https://arxiv.org/html/2605.09218v1 §3 Flame3D Editable Scene Memory and Spatial Tools — mechanism: We propose Flame3D, a training-free framework that represents scenes as editable visual-textual 3D memories and exposes them to an off-the-shelf MLLM through composable spatial tools. | https://arxiv.org/html/2605.09218v1 §4 Experiments; Compose3D — disclosed scope: 3D scene understanding spans reasoning about free space, object grounding, hypothetical object insertions, complex geometric relationships, and integrating all of these with external tools and data sources. Existing 3D understanding methods typically rely on large-scale 3D-language training or focus on object grounding and simple spatial relationships.… | https://arxiv.org/html/2605.09218v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09218v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09218 | complete |
| SF-2026-ARXIV-2605-09225 | RP-01dc5a01d1b23832 | standard | arXiv:2605.09225v1 | SRC-ARXIV@arXiv:2605.09225v1 | https://arxiv.org/html/2605.09225v1 §3.3 Robust Evaluation Metric; §4 Method — mechanism: Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating them systematically. This paper addresses that gap with three contributions. (1) Large-scale compositional jailbreak… | https://arxiv.org/html/2605.09225v1 §5 Evaluation — disclosed scope: Experiments across 114,000 prompts confirm that OPTIMUS separates Weak, Moderate, and Optimal jailbreaks with category-level evidence binary evaluation cannot supply. | https://arxiv.org/html/2605.09225v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09225v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09225 | complete |
| SF-2026-ARXIV-2605-09227 | RP-48ec48fa9bc47b08 | standard | arXiv:2605.09227v1 | SRC-ARXIV@arXiv:2605.09227v1 | https://arxiv.org/html/2605.09227v1 §IV Hierarchical Bayesian Calibration; §V Neural-ODE Score Transport — mechanism: [Abridged] Using a Large Language Model (LLM) as an automatic rater (LLM-as-a-judge) is cheap but potentially biased: some judges run lenient, others strict, the middle of the scale gets compressed, and verbose answers may be over-rewarded. A common remedy is post-hoc calibration: leave the cheap judge… | https://arxiv.org/html/2605.09227v1 §VI Experiments — disclosed scope: The headline result is that the choice between methods is primarily a data-budget question. | https://arxiv.org/html/2605.09227v1 §VIII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09227v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09227 | complete |
| SF-2026-ARXIV-2605-09241 | RP-77c4edb171499b79 | deep | arXiv:2605.09241v1 | SRC-ARXIV@arXiv:2605.09241v1 | https://arxiv.org/html/2605.09241v1 §3 Method — mechanism: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be… | https://arxiv.org/html/2605.09241v1 §4 Experiments — disclosed scope: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be… | https://arxiv.org/html/2605.09241v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.09241v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-09241 | complete |
| SF-2026-ARXIV-2605-10980 | RP-c0e140eebf747944 | deep | arXiv:2605.10980v1 | SRC-ARXIV@arXiv:2605.10980v1 | https://arxiv.org/html/2605.10980v1 §3 LEAP — mechanism: In response, we introduce LEAP (Lookahead Early-Convergence Token Detection for Accelerated Parallel Decoding). | https://arxiv.org/html/2605.10980v1 §4 Experiments — disclosed scope: Diffusion Language Models (dLLMs) have garnered significant attention for their potential in highly parallel processing. The parallel capabilities of existing dLLMs stem from the assumption of conditional independence at high confidence levels, which ensures negligible discrepancy between the marginal and joint distributions. However, the stringent confidence… | https://arxiv.org/html/2605.10980v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.10980v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10980 | complete |
| SF-2026-ARXIV-2605-10987 | RP-668e083d7d090910 | deep | arXiv:2605.10987v1 | SRC-ARXIV@arXiv:2605.10987v1 | https://arxiv.org/html/2605.10987v1 §IV Threat Model and AESOP — mechanism: We show that this structure creates an efficiency-attack surface that existing methods targeting single models cannot exploit: on identical inputs and budgets, path-aware targeting inflates FLOPs by $2,407\times$ while the strongest single-model baseline achieves $117\times$ -- a $20\times$ gap attributable entirely to where the attack is… | https://arxiv.org/html/2605.10987v1 §VI Evaluation — disclosed scope: Modern machine learning deployments increasingly compose specialized models into dynamic inference pipelines, where upstream components produce intermediate predictions that determine the workload and inputs of downstream components. The cost of processing an input is therefore not determined by any single model, but by two coupled factors:… | https://arxiv.org/html/2605.10987v1 §VII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.10987v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10987 | complete |
| SF-2026-ARXIV-2605-10990 | RP-01e86017d8cb8a85 | deep | arXiv:2605.10990v1 | SRC-ARXIV@arXiv:2605.10990v1 | https://arxiv.org/html/2605.10990v1 §3 Contract Extraction and Validation — mechanism: We formulate skill drift as contract violation and introduce \sgname{}, which extracts executable environment contracts from skill documents and validates only those role-bearing assumptions against known or live conditions. | https://arxiv.org/html/2605.10990v1 §4 Evaluation — disclosed scope: LLM agents increasingly rely on reusable skill libraries, but these skills silently decay as the external services, packages, APIs, and configurations they reference evolve. Existing monitors detect such changes at the wrong granularity: they observe values, not the role those values play in a skill. A… | https://arxiv.org/html/2605.10990v1 Appendix C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.10990v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10990 | complete |
| SF-2026-ARXIV-2605-10993 | RP-09f9887a068932ef | standard | arXiv:2605.10993v1 | SRC-ARXIV@arXiv:2605.10993v1 | https://arxiv.org/html/2605.10993v1 §3 ECHO — mechanism: Inspired by the hierarchical organization of human experience, we propose ECHO (Experience Consolidation and Hierarchical Organization), a novel memory framework operating within a Continuous Hierarchical Space. | https://arxiv.org/html/2605.10993v1 §4 Experiments — disclosed scope: Evaluations on LIBERO and preliminary real-world experiments demonstrate the effectiveness of our approach, notably achieving a 12.8% absolute improvement in execution success rate over the $π_0$ baseline on LIBERO-Long, while improving compositional generalization on cross-suite unseen long-horizon tasks. | https://arxiv.org/html/2605.10993v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.10993v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10993 | complete |
| SF-2026-ARXIV-2605-10999 | RP-820e892d3e6ca1d0 | deep | arXiv:2605.10999v1 | SRC-ARXIV@arXiv:2605.10999v1 | https://arxiv.org/html/2605.10999v1 §3 SkillGen — mechanism: We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a base agent. | https://arxiv.org/html/2605.10999v1 §4 Evaluation — disclosed scope: Skills are a promising way to improve LLM agent capabilities without retraining, while keeping the added procedure reusable and controllable. However, high-quality skills are still largely written by hand. We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a… | https://arxiv.org/html/2605.10999v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.10999v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-10999 | complete |
| SF-2026-ARXIV-2605-11002 | RP-501eabcf1735a16f | deep | arXiv:2605.11002v1 | SRC-ARXIV@arXiv:2605.11002v1 | https://arxiv.org/html/2605.11002v1 §3 MT-JailBench Modular Framework — mechanism: We introduce MT-JailBench, a modular evaluation framework for benchmarking multi-turn jailbreaks under fixed conditions. | https://arxiv.org/html/2605.11002v1 §4 Experiments and Component Ablations — disclosed scope: Recent methods demonstrate this risk, but they are usually evaluated as black-box pipelines with different budgets, judges, retry rules, and strategy generation procedures. | https://arxiv.org/html/2605.11002v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.11002v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-11002 | complete |
| SF-2026-ARXIV-2605-16359 | RP-de943576e61cb50d | standard | arXiv:2605.16359v1 | SRC-ARXIV@arXiv:2605.16359v1 | https://arxiv.org/html/2605.16359v1 §3 Method — mechanism: We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens. | https://arxiv.org/html/2605.16359v1 §4 Experiments — disclosed scope: Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token… | https://arxiv.org/html/2605.16359v1 Appendix E Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16359v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16359 | complete |
| SF-2026-ARXIV-2605-16360 | RP-22ca47efa032efb3 | deep | arXiv:2605.16360v1 | SRC-ARXIV@arXiv:2605.16360v1 | https://arxiv.org/html/2605.16360v1 §4 ProxyKV and HybridAxialMapper — mechanism: To bridge this scoring-cost--accuracy gap, we propose ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target. | https://arxiv.org/html/2605.16360v1 §5 Evaluation — disclosed scope: Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost--accuracy gap, we… | https://arxiv.org/html/2605.16360v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.16360v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-16360 | complete |
| SF-2026-ARXIV-2605-23951 | RP-8d7f744bbf216f42 | deep | arXiv:2605.23951v1 | SRC-ARXIV@arXiv:2605.23951v1 | https://arxiv.org/html/2605.23951v1 §3 Semantics; §4–§6 Three Verification Layers — mechanism: We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a deterministic script-side reachable through a non-deterministic LLM-side), state the verification problem as a capability-containment property over that semantics, and present three composable methods that together raise… | https://arxiv.org/html/2605.23951v1 §8 Bundle Re-checker; §10 Threat Coverage — disclosed scope: The companion paper introduced a four-level verification lattice on agent-skill manifests (unverified, declared, tested, formal) and left the top level aspirational. This paper closes that gap. We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a… | https://arxiv.org/html/2605.23951v1 §11 Scope and Residual LLM Refusal Boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO | https://arxiv.org/html/2605.23951v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named | claim:SF-2026-ARXIV-2605-23951 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-08586:start -->
#### Computer Science Conferences Should Require Nonrepudiable Experimental Results

问题与演进：实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08586v1 §3 Problem and Security Properties; §4 Threat Model; §5 K-Veritas — mechanism: To show that the problem is solvable, we built K-Veritas, a reference implementation in Go that produces signed reports without accessing training data.`。

Evaluation：`https://arxiv.org/html/2605.08586v1 §5 Reference Implementation and Protocol Walkthrough — disclosed scope: We name the underlying problem experiment nonrepudiation: a compliant protocol must bind the numbers in a paper to an actual executed computation in a way the author cannot later alter or deny.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08586v1 §6 Discussion; position-paper and prototype boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08586v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08586:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08586:end -->
<!-- review:SF-2026-ARXIV-2605-08586:end -->

<!-- review:SF-2026-ARXIV-2605-08587:start -->
#### Kaczmarz Linear Attention

问题与演进：线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08587v1 §3 Kaczmarz Linear Attention — mechanism: We revisit the online-regression objective underlying GDN and, inspired by the Kaczmarz projection method, derive the key-norm-normalized dynamic step size $β_t = η_t / (\/k_t\/_2^2 + ε)$ for residual updates.`。

Evaluation：`https://arxiv.org/html/2605.08587v1 §5 Experiments — disclosed scope: Long-context language modeling remains central to modern sequence modeling, but the quadratic cost of Transformer attention makes scaling computationally prohibitive. Linear recurrent models address this bottleneck by compressing the context into a fixed-size state, making the rule that forgets, writes, and edits information a central design…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08587v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08587v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08587:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08587:end -->
<!-- review:SF-2026-ARXIV-2605-08587:end -->

<!-- review:SF-2026-ARXIV-2605-08590:start -->
#### Causal Stories from Sensor Traces: Auditing Epistemic Overreach in LLM-Generated Personal Sensing Explanations

问题与演进：生成式解释需要把 observation、inference、unknown 分层；增加 context 或 bounded prompt 不能替代 claim-level evidence gate。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08590v1 §3 Study Design and Methods; §3.4 Evaluation Methodology — mechanism: We introduce epistemic overreach (EO) as a measure for cases where a generated explanation implies more than the available sensing evidence can justify.`。

Evaluation：`https://arxiv.org/html/2605.08590v1 §4 Results — disclosed scope: These findings suggest that evidential grounding should be a first-order evaluation criterion for LLM-generated personal sensing explanations, alongside fluency and plausibility.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08590v1 §5.5 Limitations and Future Directions — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08590v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08590:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08590:end -->
<!-- review:SF-2026-ARXIV-2605-08590:end -->

<!-- review:SF-2026-ARXIV-2605-08594:start -->
#### FLARE: One-Shot PE-Level Fault Localization in Systolic Arrays via Algebraic Test Vectors

问题与演进：AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08594v1 §4 One-Round Localization; §5 Two-Round Localization — mechanism: In this paper, we propose a lightweight, purely algorithmic remedy based on coprime test vectors.`。

Evaluation：`https://arxiv.org/html/2605.08594v1 §6 Evaluation — disclosed scope: Systolic arrays are the dominant compute fabric for neural network inference. Prior work has addressed column-level fault detection efficiently with uniform test patterns, but row-level (PE-level) fault localization within a faulty column remains open without resorting to hardware redundancy. The fundamental obstacle is that uniform test…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08594v1 §7 Discussion and Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08594v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08594:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08594:end -->
<!-- review:SF-2026-ARXIV-2605-08594:end -->

<!-- review:SF-2026-ARXIV-2605-08621:start -->
#### EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair

问题与演进：迭代修复必须把 build artifact、历史尝试与环境反馈保存为 durable evidence state，并把 tool execution 与 diagnosis/reasoning 分离。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08621v1 §4 EvidenT Framework — mechanism: While recent LLM-based repair methods show promise for project-level source fixes, they struggle with system-level repair, where failures span multi-language artifacts such as build recipes, scripts, and source archives, and require iterative validation through external build services.`。

Evaluation：`https://arxiv.org/html/2605.08621v1 §5 Evaluation — disclosed scope: Frequent toolchain updates and growing ISA diversity have made system-level software package repair increasingly important. Diagnosing and repairing build failures remains challenging because failures involve heterogeneous evidence, dependency constraints, and architecture-specific build conventions. While recent LLM-based repair methods show promise for project-level source fixes, they struggle…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08621v1 §5.6 Failure Analysis and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08621v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08621:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08621:end -->
<!-- review:SF-2026-ARXIV-2605-08621:end -->

<!-- review:SF-2026-ARXIV-2605-08632:start -->
#### PARD-2: Target-Aligned Parallel Draft Model for Dual-Mode Speculative Decoding

问题与演进：draft model 训练目标应对齐连续 acceptance length，并显式区分 target-dependent 与 target-independent mode。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08632v1 §3 PARD-2; §3.2 Confidence-Adaptive Token Optimization — mechanism: Speculative decoding accelerates Large Language Models (LLMs) inference by using a lightweight draft model to propose candidate tokens that are verified in parallel by the target model.`。

Evaluation：`https://arxiv.org/html/2605.08632v1 §4 Experiments — disclosed scope: Experiments across diverse models and tasks demonstrate that PARD-2 achieves up to 6.94$\times$ lossless acceleration, surpassing EAGLE-3 by 1.9$\times$ and PARD by 1.3$\times$ on Llama3.1-8B.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08632v1 §5 Limitations and Conclusion — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08632v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08632:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08632:end -->
<!-- review:SF-2026-ARXIV-2605-08632:end -->

<!-- review:SF-2026-ARXIV-2605-08636:start -->
#### EdgeFlowerTune: Evaluating Federated LLM Fine-Tuning Under Realistic Edge System Constraints

问题与演进：edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08636v1 §2 EdgeFlowerTune Benchmark Design; §2.2 Benchmarking Protocols — mechanism: We present EdgeFlowerTune, a deployment-oriented benchmark for federated LLM fine-tuning under realistic edge-system constraints.`。

Evaluation：`https://arxiv.org/html/2605.08636v1 §3 Experimental Settings; §4 Results — disclosed scope: Our benchmark results show that accuracy-only evaluation can lead to misleading conclusions: methods with similar final quality may differ substantially in deployability once realistic system constraints are considered.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08636v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08636v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08636:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08636:end -->
<!-- review:SF-2026-ARXIV-2605-08636:end -->

<!-- review:SF-2026-ARXIV-2605-08639:start -->
#### ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning

问题与演进：MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08639v1 §3 Design; §4 Routing-Replay-Guided Load Balancing — mechanism: We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity.`。

Evaluation：`https://arxiv.org/html/2605.08639v1 §5 Evaluation — disclosed scope: Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making them less effective under sharp…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08639v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08639v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08639:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08639:end -->
<!-- review:SF-2026-ARXIV-2605-08639:end -->

<!-- review:SF-2026-ARXIV-2605-08646:start -->
#### PAAC: Privacy-Aware Agentic Device-Cloud Collaboration

问题与演进：device-cloud agent 的 compute split 本质是 trust boundary；typed placeholder identity 与 deterministic reversal 必须留在设备端。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08646v1 §3 PAAC — mechanism: In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism.`。

Evaluation：`https://arxiv.org/html/2605.08646v1 §4 Experiments — disclosed scope: Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08646v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08646v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08646:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08646:end -->
<!-- review:SF-2026-ARXIV-2605-08646:end -->

<!-- review:SF-2026-ARXIV-2605-08647:start -->
#### AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators

问题与演进：多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08647v1 §3 Benchmark Design; §4 Process Metrics — mechanism: To make these vulnerabilities measurable before deployment, we introduce AgentCollabBench, a diagnostic benchmark of 900 human-validated tasks spanning software engineering, DevOps, and data engineering.`。

Evaluation：`https://arxiv.org/html/2605.08647v1 §5 Experiments — disclosed scope: Evaluating four modern LLMs (GPT 4.1 mini, Gemini 2.5 Flash Lite, Qwen-3.5-35B-A3B, and Llama 3.1 8B Instruct), we expose model-specific vulnerability profiles invisible to outcome-only evaluation; Qwen-3.5-35B-A3B, for example, leads on tracer durability and instruction stability, while GPT 4.1 mini leads on leakage containment and false-belief…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08647v1 Appendix K Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08647v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08647:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08647:end -->
<!-- review:SF-2026-ARXIV-2605-08647:end -->

<!-- review:SF-2026-ARXIV-2605-08658:start -->
#### Sketch-and-Verify: Structured Inference-Time Scaling via Program Sketching

问题与演进：inference-time search 应分离 strategy sketch、candidate completion、execution verification 与 selection，并承认升级模型 tier 的替代边界。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08658v1 §2 Sketch-and-Verify — mechanism: We characterize the K-vs-M trade-off via a Flash Lite scaling sweep, report HumanEval+ saturation on Flash and Pro, and show the method composes cleanly with execution-based selection from the concurrent Semantic Voting line of work.`。

Evaluation：`https://arxiv.org/html/2605.08658v1 §3 Evaluation — disclosed scope: SKETCHVERIFY is a within-tier cost-performance policy, not a universal accuracy improvement. The operational question: a practitioner stuck with a small, cheap code model (here, Gemini 3.1 Flash Lite) for latency, deployment, or budget reasons -- how should they spend a small amount of extra test-time compute?…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08658v1 §4 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08658v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08658:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08658:end -->
<!-- review:SF-2026-ARXIV-2605-08658:end -->

<!-- review:SF-2026-ARXIV-2605-08666:start -->
#### The Cancellation Hypothesis in Critic-Free RL: From Outcome Rewards to Token Credits

问题与演进：sequence-level outcome reward 通过共享低置信 token 的梯度耦合产生隐式 token credit；batch composition 因而成为训练语义的一部分。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08666v1 §3 Token-Level Analysis; §4 Cancellation Hypothesis — mechanism: To explain this phenomenon, we further show that a token's change in probability is not fully determined by its own advantage; coupled gradient interactions with other tokens also play a non-negligible role.`。

Evaluation：`https://arxiv.org/html/2605.08666v1 §5 Experiments — disclosed scope: Building upon this analysis, we propose the cancellation hypothesis: as a result of coupling, opposing signals cancel out for tokens shared by positive and negative rollouts, while tokens more specific to successful rollouts receive stronger reinforcement, thereby inducing hidden token-level credit assignment from rollout-level rewards.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08666v1 Appendix A Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08666v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08666:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08666:end -->
<!-- review:SF-2026-ARXIV-2605-08666:end -->

<!-- review:SF-2026-ARXIV-2605-08678:start -->
#### MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI

问题与演进：评测 AI 发现新 ML 方法时必须冻结 evaluator 与 training knobs、限制 editable scope、复现强基线并跨 scale 验证，避免把调参或 harness hacking 计为 discovery。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08678v1 §3 MLS-Bench; §3.2 Evaluation Rigor — mechanism: We introduce MLS-Bench, a benchmark for evaluating whether AI systems can invent generalizable and scalable ML methods.`。

Evaluation：`https://arxiv.org/html/2605.08678v1 §4 Experiments; §5 Analysis — disclosed scope: As large language models demonstrate advanced capabilities in reasoning, coding, and engineering tasks, it is increasingly important to understand whether they can discover such methods rather than only apply existing ones.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08678v1 §6 Conclusion and Future Work — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08678v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08678:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08678:end -->
<!-- review:SF-2026-ARXIV-2605-08678:end -->

<!-- review:SF-2026-ARXIV-2605-08715:start -->
#### AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems

问题与演进：长轨迹评测应从 post-hoc attribution 前移到 prefix-only online audit，并把 earliest decisive error 作为可干预状态。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08715v1 §3 AgentForesight — mechanism: In this work, we introduce AgentForesight, a framework that reframes this problem as online auditing: at each step of an unfolding trajectory, an auditor observes only the current prefix and must either continue the run or alarm at the earliest decisive error, without access to future…`。

Evaluation：`https://arxiv.org/html/2605.08715v1 §4 Experiments — disclosed scope: LLM-based multi-agent systems are increasingly deployed on long-horizon tasks, but a single decisive error is often accepted by downstream agents and cascades into trajectory-level failure. Existing work frames this as \emph{post-hoc failure attribution}, diagnosing the responsible agent and step after the trajectory has ended. However, this…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08715v1 Appendix G.2 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08715v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08715:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08715:end -->
<!-- review:SF-2026-ARXIV-2605-08715:end -->

<!-- review:SF-2026-ARXIV-2605-08717:start -->
#### Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents

问题与演进：Agent 失败恢复应以运行 telemetry 锚定 diagnosis artifact，经 guidance gate 进入下一次尝试；wrapper 保留执行边界且不能冒充生产 recovery guarantee。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08717v1 §3 PROBE Framework — mechanism: We present PROBE, a failure-anchored framework for structured recovery in software engineering agents.`。

Evaluation：`https://arxiv.org/html/2605.08717v1 §4 Evaluation — disclosed scope: Beyond controlled evaluation, a Microsoft IcM prototype shows that PROBE can attach as a non-intrusive side channel to existing service-diagnosis workflows without changing the agent policy, toolset, or execution budget.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08717v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08717v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08717:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08717:end -->
<!-- review:SF-2026-ARXIV-2605-08717:end -->

<!-- review:SF-2026-ARXIV-2605-08737:start -->
#### The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs

问题与演进：near-deterministic structured output 的 on-policy distillation 存在可测 extrapolation cliff，格式合同应成为训练控制约束。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08737v1 §3 Base-Relative Clip-Safety Threshold; §4 K-ary Extension — mechanism: In a single-position Bernoulli reduction, we derive a closed-form base-relative clip-safety threshold lambda*(p,b,c) determined by three measurable quantities: the teacher modal probability, the warm-start mass, and the importance-sampling clip strength.`。

Evaluation：`https://arxiv.org/html/2605.08737v1 §5 Experiments — disclosed scope: On-policy distillation (OPD) is widely used for LLM post-training. When pushed with a reward-extrapolation coefficient lambda &gt; 1, the student can lift past the teacher in domain, but past a threshold lambda* the same step violates the output contract on structured-output tasks. In a single-position Bernoulli…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08737v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08737v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08737:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08737:end -->
<!-- review:SF-2026-ARXIV-2605-08737:end -->

<!-- review:SF-2026-ARXIV-2605-08747:start -->
#### Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents

问题与演进：embodied evaluation 必须把 world completion 与 terminal commitment 分开，避免执行成功、停止失败和无证据承诺被压成同一分数。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08747v1 §3 VIGIL Protocol — mechanism: We introduce VIGIL, an evaluation framework that makes terminal commitment independently measurable.`。

Evaluation：`https://arxiv.org/html/2605.08747v1 §4 Experiments — disclosed scope: We introduce VIGIL, an evaluation framework that makes terminal commitment independently measurable.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08747v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08747v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08747:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08747:end -->
<!-- review:SF-2026-ARXIV-2605-08747:end -->

<!-- review:SF-2026-ARXIV-2605-08761:start -->
#### Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows

问题与演进：企业多 Agent 评测需要把 role permission、stateful service transition、approval commitment 与 coordination cost 放进同一 executable workflow contract。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08761v1 §3 EntCollabBench; Role-specialized workflow design — mechanism: We introduce \textsc{EntCollabBench}, a benchmark for evaluating enterprise multi-agent collaboration.`。

Evaluation：`https://arxiv.org/html/2605.08761v1 §4 Experiments; Appendix G Failure Analysis — disclosed scope: \textsc{EntCollabBench} simulates a permission-isolated organization with 11 role-specialized agents across six departments and contains two evaluation subsets: a Workflow subset, where agents collaboratively modify enterprise system states, and an Approval subset, where agents make policy-grounded decisions.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08761v1 Appendix H Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08761v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08761:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08761:end -->
<!-- review:SF-2026-ARXIV-2605-08761:end -->

<!-- review:SF-2026-ARXIV-2605-08769:start -->
#### EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems

问题与演进：固定工作流在 task state 变化时会错配；execution-time workflow policy 可选择 agent/edge，但必须版本化 agent pool、depth、reward 与 evaluator。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08769v1 §2 Formulation; §3 EvoMAS — mechanism: We propose EvoMAS, a framework for execution-time multi-agent workflow construction.`。

Evaluation：`https://arxiv.org/html/2605.08769v1 §4 Experiments — disclosed scope: Large language model (LLM)-based multi-agent systems have shown strong potential on complex tasks through agent specialization, tool use, and collaborative reasoning. However, most automated multi-agent system design methods still follow a one-shot paradigm: a workflow is optimized or selected before execution and then reused unchanged throughout…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08769v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08769v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08769:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08769:end -->
<!-- review:SF-2026-ARXIV-2605-08769:end -->

<!-- review:SF-2026-ARXIV-2605-08828:start -->
#### When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents

问题与演进：Agent evidence-grounding 评测必须分开 execution authority、runtime feedback、verification、provenance 与 freshness，并用 oracle-visible environment state 判定误信路径。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08828v1 §3 EnvTrustBench Framework; §4 Controlled Stress Cases — mechanism: We introduce EnvTrustBench, an agentic framework for benchmarking this failure mode.`。

Evaluation：`https://arxiv.org/html/2605.08828v1 §5 Evaluation and Scaffold Inspection — disclosed scope: Large language model agents increasingly operate through environment-facing scaffolds that expose files, web pages, APIs, and logs. These observations influence tool use, state tracking, and action sequencing, yet their reliability and authority are often uncertain. Environmental grounding is therefore a systems-level problem involving context admission, evidence…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08828v1 §6 Limitations and Threats to Validity — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08828v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08828:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08828:end -->
<!-- review:SF-2026-ARXIV-2605-08828:end -->

<!-- review:SF-2026-ARXIV-2605-08835:start -->
#### SynerDiff: Synergetic Continuous Batching for Fast and Parallel Diffusion Model Inference

问题与演进：diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08835v1 §III SynerDiff Design — mechanism: To address these, we propose SynerDiff, an efficient continuous batching system built on intra-inter level synergy.`。

Evaluation：`https://arxiv.org/html/2605.08835v1 §IV-B Evaluation — disclosed scope: The expansion of Artificial Intelligence-generated content service requires diffusion model serving to simultaneously achieve high throughput and low task end-to-end (E2E) latency. However, existing continuous batching methods suffer from severe resource contention during UNet-VAE concurrency, leading to latency spikes. Furthermore, concurrent multi-task scheduling entails a trade-off…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08835v1 §V Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08835v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08835:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08835:end -->
<!-- review:SF-2026-ARXIV-2605-08835:end -->

<!-- review:SF-2026-ARXIV-2605-08838:start -->
#### Generating Leakage-Free Benchmarks for Robust RAG Evaluation

问题与演进：RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08838v1 §3 Leakage-Free Benchmark Generation — mechanism: We introduce SeedRG, a semi-synthetic benchmark generation pipeline that mitigates knowledge leakage and addresses the issue of benchmark aging.`。

Evaluation：`https://arxiv.org/html/2605.08838v1 §4 Experiments and Robustness Evaluation — disclosed scope: This leads to unreliable evaluation.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08838v1 §5 Discussion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08838v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08838:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08838:end -->
<!-- review:SF-2026-ARXIV-2605-08838:end -->

<!-- review:SF-2026-ARXIV-2605-08840:start -->
#### ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing

问题与演进：KV eviction 的 commit quality 可由 layer-wise output reconstruction 与 spatial-temporal smoothing共同约束，而不能只按局部 attention proxy。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08840v1 §3 ReST-KV — mechanism: In this paper, we propose ReST-KV, a robust KV eviction method that combines layer-wise output Reconstruction and Spatial-Temporal smoothing to provide a more comprehensive perspective for the KV cache eviction task.`。

Evaluation：`https://arxiv.org/html/2605.08840v1 §4 Experiments — disclosed scope: Large language models (LLMs) face growing challenges in efficient generative inference due to the increasing memory demands of Key-Value (KV) caches, especially for long sequences. Existing eviction methods typically retain KV pairs with high attention weights but overlook the impact of attention redistribution caused by token…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08840v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08840v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08840:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08840:end -->
<!-- review:SF-2026-ARXIV-2605-08840:end -->

<!-- review:SF-2026-ARXIV-2605-08862:start -->
#### BubbleSpec: Turning Long-Tail Bubbles into Speculative Rollout Drafts for Synchronous Reinforcement Learning

问题与演进：同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08862v1 §3 BubbleSpec — mechanism: Instead, we propose BubbleSpec, a novel framework that accelerates RL rollouts while strictly keeping the mathematical exactness.`。

Evaluation：`https://arxiv.org/html/2605.08862v1 Appendix A Evaluation — disclosed scope: Extensive evaluations demonstrate that BubbleSpec reduces decoding steps by 50% and increases rollout throughput by up to 1.8x.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08862v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08862v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08862:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08862:end -->
<!-- review:SF-2026-ARXIV-2605-08862:end -->

<!-- review:SF-2026-ARXIV-2605-08871:start -->
#### Rennala MVR: Improved Time Complexity for Parallel Stochastic Optimization via Momentum-Based Variance Reduction

问题与演进：parallel stochastic optimization 可用 momentum variance reduction 改变同步轮次复杂度，但证据仍限 stochastic quadratic 与 inexact-neural variant。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08871v1 §3 Rennala MVR — mechanism: We show that, under a mean-squared smoothness assumption, variance reduction can improve time complexity in relevant parameter regimes.`。

Evaluation：`https://arxiv.org/html/2605.08871v1 §4 Experiments — disclosed scope: Large-scale machine learning models are trained on clusters of machines that exhibit heterogeneous performance due to hardware variability, network delays, and system-level instabilities. In such environments, time complexity rather than iteration complexity becomes the relevant performance metric for optimization algorithms. Recent work by Tyurin and Richtárik…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08871v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08871v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08871:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08871:end -->
<!-- review:SF-2026-ARXIV-2605-08871:end -->

<!-- review:SF-2026-ARXIV-2605-08876:start -->
#### OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents

问题与演进：agent availability threat model 必须覆盖 reasoning-level cost amplification，并把 trigger optimization 与 payload optimization 分开。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08876v1 §3 OTora Threat Model and Framework — mechanism: We introduce OTora, the first unified, two-stage red-teaming framework for instantiating R-DoS attacks.`。

Evaluation：`https://arxiv.org/html/2605.08876v1 §4 Experiments — disclosed scope: Large Language Models (LLMs) are increasingly deployed as autonomous agents that execute tool-augmented, multi-step tasks, where latency is a critical factor for real-world applications. Yet an overlooked threat is Reasoning-Level Denial-of-Service (R-DoS), in which an attacker preserves task correctness but degrades availability by inflating an agent's…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08876v1 Appendix A Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08876v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08876:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08876:end -->
<!-- review:SF-2026-ARXIV-2605-08876:end -->

<!-- review:SF-2026-ARXIV-2605-08879:start -->
#### Preserving Foundational Capabilities in Flow-Matching VLAs through Conservative SFT

问题与演进：flow-matching VLA 的 downstream SFT 需要约束参数 disruption 并同时验收 target acquisition 与 prior-skill retention；保守更新会减慢新 primitive 学习。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08879v1 §3 Conservative SFT — mechanism: We present Conservative Supervised Fine-Tuning (ConSFT), an optimization objective that adapts to target distributions while mitigating catastrophic forgetting, requiring zero prior data or architectural overhead.`。

Evaluation：`https://arxiv.org/html/2605.08879v1 §4–§5 Simulated and Physical Experiments — disclosed scope: Unconstrained fine-tuning of flow-matching Vision-Language-Action (VLA) models drives dense parameter overwrites, degrading pre-trained capabilities. We present Conservative Supervised Fine-Tuning (ConSFT), an optimization objective that adapts to target distributions while mitigating catastrophic forgetting, requiring zero prior data or architectural overhead. By dynamically scaling learning signals based on…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08879v1 §6 Conclusion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08879v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08879:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08879:end -->
<!-- review:SF-2026-ARXIV-2605-08879:end -->

<!-- review:SF-2026-ARXIV-2605-08894:start -->
#### Fitting Is Not Enough: Smoothness in Extremely Quantized LLMs

问题与演进：极低比特量化不仅要拟合训练点，还要约束 loss landscape smoothness 与部署 perturbation sensitivity。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08894v1 §5 Smoothness-Aware Quantization — mechanism: In this paper, we show that extremely quantized LLMs suffer from systematic smoothness degradation beyond numerical precision loss.`。

Evaluation：`https://arxiv.org/html/2605.08894v1 §6 Experiments — disclosed scope: To validate it, we introduce a simple smoothness-preserving principle in both post-training quantization and quantization-aware training, and demonstrate that preserving smoothness brings additional gains beyond numerical accuracy.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08894v1 Appendix A.7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08894v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08894:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08894:end -->
<!-- review:SF-2026-ARXIV-2605-08894:end -->

<!-- review:SF-2026-ARXIV-2605-08908:start -->
#### HyDRA: Deadline and Reuse-Aware Cacheability for Hardware Accelerators

问题与演进：共享 cache 对 accelerator request 的 admission/bypass 必须联合预测 reuse 与 deadline；core-centric locality predictor 不能拥有 accelerator deadline commit。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08908v1 §IV LERN Reuse Prediction; §V HyDRA Policy — mechanism: We propose a novel clustering-based methodology, LERN, for learning and predicting the reuse behavior of hardware accelerators at the shared cache.`。

Evaluation：`https://arxiv.org/html/2605.08908v1 §VI Evaluation — disclosed scope: The system-level cache is a critical resource shared by processor cores and domain-specific accelerators in heterogeneous systems on chips (SoCs). The strict QoS requirements of accelerators, such as deadlines, can lead to severe performance degradation of processor cores. Thus, managing the shared cache efficiently between cores…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08908v1 §VII Conclusion; evaluated accelerator/cache boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08908v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08908:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08908:end -->
<!-- review:SF-2026-ARXIV-2605-08908:end -->

<!-- review:SF-2026-ARXIV-2605-08913:start -->
#### Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes

问题与演进：端侧 decode latency 不是 context/KV 容量的单调函数；backend execution regimes 与 instrumentation perturbation 必须进入 measurement contract。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08913v1 §3 Experimental Methodology — mechanism: Controlled experiments show that these anomalies originate primarily during the decode phase rather than prefill, are not explained by memory pressure alone, and remain absent on CPU and NVIDIA CUDA backends under identical conditions.`。

Evaluation：`https://arxiv.org/html/2605.08913v1 §4 Results and KV Ablation — disclosed scope: These findings suggest that autoregressive decoding on MPS enters discrete execution regimes that are not captured by coarse-grained benchmarking, highlighting the importance of hardware-aware evaluation for long-context inference.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08913v1 §5.2 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08913v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08913:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08913:end -->
<!-- review:SF-2026-ARXIV-2605-08913:end -->

<!-- review:SF-2026-ARXIV-2605-08927:start -->
#### Quantitative Comparison of Credible Compilation and Verification In Coding Agent Compiler Development

问题与演进：coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08927v1 §3 Credible Compilation and Verification Workflows — mechanism: We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification.`。

Evaluation：`https://arxiv.org/html/2605.08927v1 §5–§6 Quantitative Comparison — disclosed scope: Formal program verification is a longstanding goal in the field. We present the first quantitative comparison of the two primary compiler verification approaches, credible compilation/translation validation and full verification. Working with the first verified compiler developed by a coding agent (operating under human supervision), we present…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08927v1 §8 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08927v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08927:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08927:end -->
<!-- review:SF-2026-ARXIV-2605-08927:end -->

<!-- review:SF-2026-ARXIV-2605-08962:start -->
#### MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production

问题与演进：多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08962v1 §3 System Overview; §4 Model Parallelization; §5 Workload Balancing — mechanism: As the foundational component of versatile AI applications, training an multimodal large language model (MLLM) relies on multimodal datasets with dynamic modality mixture proportions and sample length distributions. However, existing MLLM systems remain inefficient under dynamic workloads, due to statically coupled decisions of resource allocation and…`。

Evaluation：`https://arxiv.org/html/2605.08962v1 §7 Evaluation — disclosed scope: Our experimental results demonstrate $1.27\times$-$7.57\times$ throughput improvement under production-grade dynamic workloads, as compared to four state-of-the-art systems.`。

Non-proof / fallback：`https://arxiv.org/html/2605.08962v1 §8 Discussion; undisclosed production-cluster specifications — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08962v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08962:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08962:end -->
<!-- review:SF-2026-ARXIV-2605-08962:end -->

<!-- review:SF-2026-ARXIV-2605-08982:start -->
#### PMCTS: Particle Monte Carlo Tree Search for Principled Parallelized Inference Time Scaling

问题与演进：parallel inference-time scaling 需要 particle diversity、tree state 与 verifier budget 的共同控制，而非独立重复 sampling。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.08982v1 §3 Simple PMCTS; §4 PMCTS — mechanism: We introduce Particle MCTS (PMCTS), to our knowledge the first principled parallel MCTS algorithm which is suited for neural network evaluations and can preserve formal policy improvement guarantees.`。

Evaluation：`https://arxiv.org/html/2605.08982v1 §7 Experiments — disclosed scope: Monte Carlo Tree Search (MCTS) is a widely used approach for policy improvement through search with increasing popularity for real world applications. Due to the sequential and deterministic nature of its search, runtime-scaling of MCTS with parallel compute remains a major challenge. We introduce Particle MCTS…`。

Non-proof / fallback：`https://arxiv.org/html/2605.08982v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.08982v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-08982:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-08982:end -->
<!-- review:SF-2026-ARXIV-2605-08982:end -->

<!-- review:SF-2026-ARXIV-2605-09023:start -->
#### Using Semantic Distance to Estimate Uncertainty in LLM-Based Code Generation

问题与演进：code-generation uncertainty 可以用可执行 outputs 的 semantic distance 作为 sensor，但不能被提升为通用 truth confidence。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09023v1 §3 Semantic-Distance Uncertainty — mechanism: LLMs show strong performance in code generation, but their outputs lack correctness guarantees.`。

Evaluation：`https://arxiv.org/html/2605.09023v1 §4 Experiments — disclosed scope: Across LiveCodeBench, MBPP, HumanEval-X and BigCodeBench, spanning Python, Java and C++, our metrics provide strong proxies for correctness, and consistently outperform state-of-the-art sample-based baselines across both closed-source models (GPT-3.5-Turbo, GPT-4o-mini, Gemini-2.5-Flash-Lite, Claude Opus 4.5) and an open-source model (DeepSeek-Coder-V2).`。

Non-proof / fallback：`https://arxiv.org/html/2605.09023v1 §5 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09023v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09023:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09023:end -->
<!-- review:SF-2026-ARXIV-2605-09023:end -->

<!-- review:SF-2026-ARXIV-2605-09033:start -->
#### ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts

问题与演进：graph memory poisoning 会利用 relation canonicalization、anchor merge 与 retrieval channel；memory write admission 必须验证关系级 provenance。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09033v1 §III Threat Model; §IV AIR Pipeline — mechanism: We present SHADOWMERGE, a poisoning attack against graph-based agent memory that exploits relation-channel conflicts.`。

Evaluation：`https://arxiv.org/html/2605.09033v1 §V Evaluation — disclosed scope: Graph-based agent memory is increasingly used in LLM agents to support structured long-term recall and multi-hop reasoning, but it also creates a new poisoning surface: an attacker can inject a crafted relation into graph memory so that it is later retrieved and influences agent behavior. Existing…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09033v1 §VI Defense Analysis and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09033v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09033:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09033:end -->
<!-- review:SF-2026-ARXIV-2605-09033:end -->

<!-- review:SF-2026-ARXIV-2605-09045:start -->
#### Containment Verification: AI Safety Guarantees Independent of Alignment

问题与演进：containment proof 的安全对象应是 typed action 到 boundary event 的 transition，而不是模型意图或 alignment。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09045v1 §3 Formal Model; §4 Refinement Proof — mechanism: We introduce containment verification, which locates safety guarantees in the agentic framework itself.`。

Evaluation：`https://arxiv.org/html/2605.09045v1 §5 Case Study — disclosed scope: Agentic frameworks are the software layer through which AI agents act in the world. Existing safety methods intervene on the model and therefore remain conditional on unverifiable properties of learned behavior. We introduce containment verification, which locates safety guarantees in the agentic framework itself. Under havoc…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09045v1 §5.1 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09045v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09045:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09045:end -->
<!-- review:SF-2026-ARXIV-2605-09045:end -->

<!-- review:SF-2026-ARXIV-2605-09055:start -->
#### Octopus Protocol: One-Shot Hardware Discovery and Control for AI Agents via Infrastructure-as-Prompts

问题与演进：hardware discovery 可编码为一次性 capability prompt，但没有独立 evaluation 或长期 protocol evidence 支持其成为新 owner。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09055v1 §2 Octopus Protocol — mechanism: We present Octopus Protocol, a system that collapses that cost to a single shell command.`。

Evaluation：`https://arxiv.org/html/2605.09055v1 §3 Demonstration — disclosed scope: Recent agentic-robotics systems, from Code-asPolicies to modern vision-language-action (VLA) foundation models, presuppose that drivers, SDKs, or ROS-style primitives for the target hardware already exist. Writing those primitives is the dominant engineering cost of bringing up new hardware for agent control. We present Octopus Protocol, a system…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09055v1 §4 Conclusion; no dedicated evaluation or limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09055v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09055:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09055:end -->
<!-- review:SF-2026-ARXIV-2605-09055:end -->

<!-- review:SF-2026-ARXIV-2605-09070:start -->
#### Single-Configuration Attack Success Rate Is Not Enough: Jailbreak Evaluations Should Report Distributional Attack Success

问题与演进：jailbreak evaluation 应报告攻击配置分布而非单点 ASR，并冻结 judge、variant grid 与 generation count。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09070v1 §3 Distributional ASR — mechanism: We propose two new measures for jailbreak attacks: the Variant Sensitivity Measure (VSM) and Union Coverage (UC).`。

Evaluation：`https://arxiv.org/html/2605.09070v1 §5 Experiments — disclosed scope: We empirically demonstrate the importance of these measures using two attack families across three open-source target models.`。

Non-proof / fallback：`https://arxiv.org/html/2605.09070v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09070v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09070:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09070:end -->
<!-- review:SF-2026-ARXIV-2605-09070:end -->

<!-- review:SF-2026-ARXIV-2605-09076:start -->
#### Robust Multi-Agent LLMs under Byzantine Faults

问题与演进：Byzantine 多 Agent 不能信任 sender confidence；receiver-side trust 与 topology containment 必须共同决定 aggregation。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09076v1 §4 Method — mechanism: We study decentralized LLM multi-agent systems (LLM-MAS) and propose Self-Anchored Consensus (SAC), a fully decentralized iterative filter-and-refine protocol in which agents iteratively exchange responses, locally evaluate and filter unreliable messages, and refine their own outputs.`。

Evaluation：`https://arxiv.org/html/2605.09076v1 §5 Experiments; §6 Discussion — disclosed scope: Large language model (LLM) agents increasingly collaborate over peer-to-peer networks to improve their reliability. However, these same interactions can also become a source of vulnerability, as unreliable or Byzantine agents may sway neighboring agents toward incorrect conclusions and degrade overall system performance. Existing methods rely on…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09076v1 §6 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09076v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09076:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09076:end -->
<!-- review:SF-2026-ARXIV-2605-09076:end -->

<!-- review:SF-2026-ARXIV-2605-09126:start -->
#### Cosine-Gated Adam-Decay: Drop-In Staleness-Aware Outer Optimization for Decoupled DiLoCo

问题与演进：decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09126v1 §3 Method — mechanism: We propose Cosine Gated Adam Decay (CGAD), a simple, drop-in, age-aware outer optimizer that scales each incoming pseudo-gradient by $σ(τ) = γ(τ) e^{-ατ}$ before it enters Adam's first- and second-moment buffers; the exponential models information decay and the cosine gate $γ(τ)$ smoothly zeroes contributions past a…`。

Evaluation：`https://arxiv.org/html/2605.09126v1 §5 Experiments — disclosed scope: Asynchronous DiLoCo systems may receive pseudo-gradients computed several outer rounds earlier, yet the standard Nesterov outer optimizer does not explicitly condition its update on per-update age. This can make the outer momentum buffer brittle under large controlled delays. We propose Cosine Gated Adam Decay (CGAD), a…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09126v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09126v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09126:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09126:end -->
<!-- review:SF-2026-ARXIV-2605-09126:end -->

<!-- review:SF-2026-ARXIV-2605-09163:start -->
#### FORTIS: Benchmarking Over-Privilege in Agent Skills

问题与演进：skill 安全评测要比较声明 capability 与实际需要的最小 capability，并把 over-privilege 作为可执行 contract gap。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09163v1 §3 FORTIS Benchmark Construction — mechanism: We present \textbf{FORTIS}, a benchmark that evaluates over-privilege in agent skills across two stages: whether a model selects the minimally sufficient skill from a large overlapping library, and whether it executes that skill without expanding into broader tools or actions than the skill permits.`。

Evaluation：`https://arxiv.org/html/2605.09163v1 §4 Experiments — disclosed scope: Large language model agents increasingly operate through an intermediate skill layer that mediates between user intent and concrete task execution. This layer is widely treated as an organizational abstraction, but we argue it is also a privilege boundary that current models routinely exceed. We present \textbf{FORTIS},…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09163v1 Appendix H Limitations and Broader Impact — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09163v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09163:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09163:end -->
<!-- review:SF-2026-ARXIV-2605-09163:end -->

<!-- review:SF-2026-ARXIV-2605-09168:start -->
#### CIVeX: Causal Intervention Verification for Language Agents

问题与演进：高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09168v1 §3 CIVeX; §5 Evaluation Protocol — mechanism: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN.`。

Evaluation：`https://arxiv.org/html/2605.09168v1 §6 Experiments — disclosed scope: We introduce CIVeX, a causal intervention verifier that maps proposed actions to structural causal queries over a committed action-state graph, checks identifiability, and returns one of four auditable verdicts: EXECUTE, REJECT, EXPERIMENT, or ABSTAIN.`。

Non-proof / fallback：`https://arxiv.org/html/2605.09168v1 §7 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09168v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09168:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09168:end -->
<!-- review:SF-2026-ARXIV-2605-09168:end -->

<!-- review:SF-2026-ARXIV-2605-09192:start -->
#### Evidence Over Plans: Online Trajectory Verification for Skill Distillation

问题与演进：skill distillation 应保存 environment-verified trajectory evidence，并以在线 PDI 判断 procedure 是否真正改变执行结果。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09192v1 §3 Method — mechanism: In this study, we introduce the Posterior Distillation Index (PDI), a trajectory-level metric that quantifies how well a distilled skill is grounded in the task-environment evidence.`。

Evaluation：`https://arxiv.org/html/2605.09192v1 §4 Experiments — disclosed scope: Across 86 runnable tasks, SPARK-generated skills consistently surpass no-skill baselines and outperform human-written skills on student models (inference cost up to 1,000x cheaper than teacher models).`。

Non-proof / fallback：`https://arxiv.org/html/2605.09192v1 Appendix L Limitations and Scope — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09192v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09192:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09192:end -->
<!-- review:SF-2026-ARXIV-2605-09192:end -->

<!-- review:SF-2026-ARXIV-2605-09204:start -->
#### LBI: Parallel Scan Backpropagation via Latent Bounded Interfaces

问题与演进：depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09204v1 §2 Scan Formulation; §3 Model Realization — mechanism: We introduce Latent Bounded Interfaces (LBI), an algorithmic formulation that makes scan-based backpropagation tractable by restricting inter-region communication to a low-dimensional latent interface, $ m_k \in \mathbb{R}^{r}$, where $r \ll d$.`。

Evaluation：`https://arxiv.org/html/2605.09204v1 §4 Experiments — disclosed scope: We demonstrate that LBI maintains model quality across four architectures (Mamba-2, Mamba-3, Transformer, and a Mamba--Transformer hybrid) at 47--61M block parameters.`。

Non-proof / fallback：`https://arxiv.org/html/2605.09204v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09204v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09204:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09204:end -->
<!-- review:SF-2026-ARXIV-2605-09204:end -->

<!-- review:SF-2026-ARXIV-2605-09218:start -->
#### Flame3D: Zero-shot Compositional Reasoning of 3D Scenes with Agentic Language Models

问题与演进：可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09218v1 §3 Flame3D Editable Scene Memory and Spatial Tools — mechanism: We propose Flame3D, a training-free framework that represents scenes as editable visual-textual 3D memories and exposes them to an off-the-shelf MLLM through composable spatial tools.`。

Evaluation：`https://arxiv.org/html/2605.09218v1 §4 Experiments; Compose3D — disclosed scope: 3D scene understanding spans reasoning about free space, object grounding, hypothetical object insertions, complex geometric relationships, and integrating all of these with external tools and data sources. Existing 3D understanding methods typically rely on large-scale 3D-language training or focus on object grounding and simple spatial relationships.…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09218v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09218v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09218:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09218:end -->
<!-- review:SF-2026-ARXIV-2605-09218:end -->

<!-- review:SF-2026-ARXIV-2605-09225:start -->
#### The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring

问题与演进：jailbreak 评测需要连续质量函数同时刻画 harmfulness 与语义保真，binary ASR 只保留为受限指标。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09225v1 §3.3 Robust Evaluation Metric; §4 Method — mechanism: Jailbreak attacks -- adversarial prompts that bypass LLM alignment through purely linguistic manipulation -- pose a growing operational security threat, yet the field lacks large-scale, reproducible infrastructure for generating, categorizing, and evaluating them systematically. This paper addresses that gap with three contributions. (1) Large-scale compositional jailbreak…`。

Evaluation：`https://arxiv.org/html/2605.09225v1 §5 Evaluation — disclosed scope: Experiments across 114,000 prompts confirm that OPTIMUS separates Weak, Moderate, and Optimal jailbreaks with category-level evidence binary evaluation cannot supply.`。

Non-proof / fallback：`https://arxiv.org/html/2605.09225v1 §6 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09225v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09225:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09225:end -->
<!-- review:SF-2026-ARXIV-2605-09225:end -->

<!-- review:SF-2026-ARXIV-2605-09227:start -->
#### Two Ways to De-Bias an LLM-as-a-Judge: A Continuous-Score Comparison of Hierarchical Bayesian Calibration and Neural-ODE Score Transport

问题与演进：LLM-judge calibration 应按 paired-anchor budget 与非线性程度选择 hierarchical linear 或 score-transport corrector。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09227v1 §IV Hierarchical Bayesian Calibration; §V Neural-ODE Score Transport — mechanism: [Abridged] Using a Large Language Model (LLM) as an automatic rater (LLM-as-a-judge) is cheap but potentially biased: some judges run lenient, others strict, the middle of the scale gets compressed, and verbose answers may be over-rewarded. A common remedy is post-hoc calibration: leave the cheap judge…`。

Evaluation：`https://arxiv.org/html/2605.09227v1 §VI Experiments — disclosed scope: The headline result is that the choice between methods is primarily a data-budget question.`。

Non-proof / fallback：`https://arxiv.org/html/2605.09227v1 §VIII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09227v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09227:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09227:end -->
<!-- review:SF-2026-ARXIV-2605-09227:end -->

<!-- review:SF-2026-ARXIV-2605-09241:start -->
#### Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models

问题与演进：JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.09241v1 §3 Method — mechanism: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be…`。

Evaluation：`https://arxiv.org/html/2605.09241v1 §4 Experiments — disclosed scope: Joint-Embedding Predictive Architectures (JEPAs) provide a simpleframework for learning world models by predicting future latent representations.However, JEPA training is subject to a bias-variance tradeoff.Without sufficient structural constraints, excessive representationalvariance causes the model to collapse to trivial solutions.The recent LeWorldModel (LeWM) shows that this issue can be…`。

Non-proof / fallback：`https://arxiv.org/html/2605.09241v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.09241v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-09241:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-09241:end -->
<!-- review:SF-2026-ARXIV-2605-09241:end -->

<!-- review:SF-2026-ARXIV-2605-10980:start -->
#### LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection

问题与演进：diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10980v1 §3 LEAP — mechanism: In response, we introduce LEAP (Lookahead Early-Convergence Token Detection for Accelerated Parallel Decoding).`。

Evaluation：`https://arxiv.org/html/2605.10980v1 §4 Experiments — disclosed scope: Diffusion Language Models (dLLMs) have garnered significant attention for their potential in highly parallel processing. The parallel capabilities of existing dLLMs stem from the assumption of conditional independence at high confidence levels, which ensures negligible discrepancy between the marginal and joint distributions. However, the stringent confidence…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10980v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10980v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10980:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10980:end -->
<!-- review:SF-2026-ARXIV-2605-10980:end -->

<!-- review:SF-2026-ARXIV-2605-10987:start -->
#### AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines

问题与演进：动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10987v1 §IV Threat Model and AESOP — mechanism: We show that this structure creates an efficiency-attack surface that existing methods targeting single models cannot exploit: on identical inputs and budgets, path-aware targeting inflates FLOPs by $2,407\times$ while the strongest single-model baseline achieves $117\times$ -- a $20\times$ gap attributable entirely to where the attack is…`。

Evaluation：`https://arxiv.org/html/2605.10987v1 §VI Evaluation — disclosed scope: Modern machine learning deployments increasingly compose specialized models into dynamic inference pipelines, where upstream components produce intermediate predictions that determine the workload and inputs of downstream components. The cost of processing an input is therefore not determined by any single model, but by two coupled factors:…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10987v1 §VII-C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10987v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10987:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10987:end -->
<!-- review:SF-2026-ARXIV-2605-10987:end -->

<!-- review:SF-2026-ARXIV-2605-10990:start -->
#### Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries

问题与演进：skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10990v1 §3 Contract Extraction and Validation — mechanism: We formulate skill drift as contract violation and introduce \sgname{}, which extracts executable environment contracts from skill documents and validates only those role-bearing assumptions against known or live conditions.`。

Evaluation：`https://arxiv.org/html/2605.10990v1 §4 Evaluation — disclosed scope: LLM agents increasingly rely on reusable skill libraries, but these skills silently decay as the external services, packages, APIs, and configurations they reference evolve. Existing monitors detect such changes at the wrong granularity: they observe values, not the role those values play in a skill. A…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10990v1 Appendix C Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10990v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10990:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10990:end -->
<!-- review:SF-2026-ARXIV-2605-10990:end -->

<!-- review:SF-2026-ARXIV-2605-10993:start -->
#### ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models

问题与演进：VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10993v1 §3 ECHO — mechanism: Inspired by the hierarchical organization of human experience, we propose ECHO (Experience Consolidation and Hierarchical Organization), a novel memory framework operating within a Continuous Hierarchical Space.`。

Evaluation：`https://arxiv.org/html/2605.10993v1 §4 Experiments — disclosed scope: Evaluations on LIBERO and preliminary real-world experiments demonstrate the effectiveness of our approach, notably achieving a 12.8% absolute improvement in execution success rate over the $π_0$ baseline on LIBERO-Long, while improving compositional generalization on cross-suite unseen long-horizon tasks.`。

Non-proof / fallback：`https://arxiv.org/html/2605.10993v1 Appendix G Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10993v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10993:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10993:end -->
<!-- review:SF-2026-ARXIV-2605-10993:end -->

<!-- review:SF-2026-ARXIV-2605-10999:start -->
#### SkillGen: Verified Inference-Time Agent Skill Synthesis

问题与演进：inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.10999v1 §3 SkillGen — mechanism: We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a base agent.`。

Evaluation：`https://arxiv.org/html/2605.10999v1 §4 Evaluation — disclosed scope: Skills are a promising way to improve LLM agent capabilities without retraining, while keeping the added procedure reusable and controllable. However, high-quality skills are still largely written by hand. We introduce SkillGen, a multi-agent framework that synthesizes a single auditable skill from trajectories generated by a…`。

Non-proof / fallback：`https://arxiv.org/html/2605.10999v1 §5 Conclusion; no dedicated limitations section — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.10999v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-10999:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-10999:end -->
<!-- review:SF-2026-ARXIV-2605-10999:end -->

<!-- review:SF-2026-ARXIV-2605-11002:start -->
#### MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks

问题与演进：多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.11002v1 §3 MT-JailBench Modular Framework — mechanism: We introduce MT-JailBench, a modular evaluation framework for benchmarking multi-turn jailbreaks under fixed conditions.`。

Evaluation：`https://arxiv.org/html/2605.11002v1 §4 Experiments and Component Ablations — disclosed scope: Recent methods demonstrate this risk, but they are usually evaluated as black-box pipelines with different budgets, judges, retry rules, and strategy generation procedures.`。

Non-proof / fallback：`https://arxiv.org/html/2605.11002v1 §5 Discussion and Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.11002v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-11002:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-11002:end -->
<!-- review:SF-2026-ARXIV-2605-11002:end -->

<!-- review:SF-2026-ARXIV-2605-16359:start -->
#### How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token Pruning with F^3A

问题与演进：视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16359v1 §3 Method — mechanism: We propose F^3A, a training-free router for visual token pruning that operates before the language model consumes image tokens.`。

Evaluation：`https://arxiv.org/html/2605.16359v1 §4 Experiments — disclosed scope: Vision-language models improve perception by feeding increasingly long visual token sequences into language backbones, but the resulting inference cost raises a basic scaling question: as multimodal models grow, how many visual tokens are actually needed, and how should they be allocated under a fixed visual token…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16359v1 Appendix E Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16359v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16359:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16359:end -->
<!-- review:SF-2026-ARXIV-2605-16359:end -->

<!-- review:SF-2026-ARXIV-2605-16360:start -->
#### ProxyKV: Cross-Model Proxy Pruning for Efficient Long-Context LLM Inference

问题与演进：高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.16360v1 §4 ProxyKV and HybridAxialMapper — mechanism: To bridge this scoring-cost--accuracy gap, we propose ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target.`。

Evaluation：`https://arxiv.org/html/2605.16360v1 §5 Evaluation — disclosed scope: Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost--accuracy gap, we…`。

Non-proof / fallback：`https://arxiv.org/html/2605.16360v1 §7 Limitations — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.16360v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-16360:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-16360:end -->
<!-- review:SF-2026-ARXIV-2605-16360:end -->

<!-- review:SF-2026-ARXIV-2605-23951:start -->
#### Methods for Formal Verification of Agent Skills: Three Layers Toward a Mechanically Checkable Capability-Containment Proof

问题与演进：agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness。旧方案在其原 workload、风险和成本约束下仍成立。

Method：`https://arxiv.org/html/2605.23951v1 §3 Semantics; §4–§6 Three Verification Layers — mechanism: We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a deterministic script-side reachable through a non-deterministic LLM-side), state the verification problem as a capability-containment property over that semantics, and present three composable methods that together raise…`。

Evaluation：`https://arxiv.org/html/2605.23951v1 §8 Bundle Re-checker; §10 Threat Coverage — disclosed scope: The companion paper introduced a four-level verification lattice on agent-skill manifests (unverified, declared, tested, formal) and left the top level aspirational. This paper closes that gap. We give a precise semantics for skill behaviour faithful to how a skill is consumed by an LLM-driven runtime (a…`。

Non-proof / fallback：`https://arxiv.org/html/2605.23951v1 §11 Scope and Residual LLM Refusal Boundary — no generalization beyond the disclosed model, workload, hardware, precision, evaluator and SLO`。离开披露条件时回退既有机制，不把作者结果外推为通用保证。Artifact：`https://arxiv.org/html/2605.23951v1 — artifact/code statement; immutable event-time commit Not Disclosed unless explicitly named`。
<!-- claim:SF-2026-ARXIV-2605-23951:start -->长期结论只限 exact-v1 披露的机制和实验边界；未披露 model、hardware、precision、length、batch、concurrency、evaluator 或 SLO 一律记为 Not Disclosed。<!-- claim:SF-2026-ARXIV-2605-23951:end -->
<!-- review:SF-2026-ARXIV-2605-23951:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

本报告不把作者性能数字外推为通用 benchmark claim；完整条件留在各 Source Review 的 disclosed/not-disclosed boundary。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-08586 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08586 |
| SF-2026-ARXIV-2605-08587 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08587 |
| SF-2026-ARXIV-2605-08590 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08590 |
| SF-2026-ARXIV-2605-08594 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08594 |
| SF-2026-ARXIV-2605-08621 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08621 |
| SF-2026-ARXIV-2605-08636 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08636 |
| SF-2026-ARXIV-2605-08639 | score_7_9;forced_review;potential_books_delta | selected | DA-ROUTING-REPLAY | — | 改变跨 stage 状态/通信 ownership，且对 Training System 主线有长期解释力 | analysis:DA-ROUTING-REPLAY |
| SF-2026-ARXIV-2605-08646 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08646 |
| SF-2026-ARXIV-2605-08647 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08647 |
| SF-2026-ARXIV-2605-08666 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08666 |
| SF-2026-ARXIV-2605-08678 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08678 |
| SF-2026-ARXIV-2605-08715 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08715 |
| SF-2026-ARXIV-2605-08717 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08717 |
| SF-2026-ARXIV-2605-08747 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08747 |
| SF-2026-ARXIV-2605-08761 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08761 |
| SF-2026-ARXIV-2605-08828 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08828 |
| SF-2026-ARXIV-2605-08835 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08835 |
| SF-2026-ARXIV-2605-08838 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08838 |
| SF-2026-ARXIV-2605-08862 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08862 |
| SF-2026-ARXIV-2605-08871 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08871 |
| SF-2026-ARXIV-2605-08876 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08876 |
| SF-2026-ARXIV-2605-08879 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08879 |
| SF-2026-ARXIV-2605-08908 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08908 |
| SF-2026-ARXIV-2605-08913 | forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08913 |
| SF-2026-ARXIV-2605-08927 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-08927 |
| SF-2026-ARXIV-2605-08962 | score_7_9;forced_review;potential_books_delta | selected | DA-MULTIMODAL-TRAINING-CONTROL | — | 改变跨 stage 状态/通信 ownership，且对 Training System 主线有长期解释力 | analysis:DA-MULTIMODAL-TRAINING-CONTROL |
| SF-2026-ARXIV-2605-09023 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09023 |
| SF-2026-ARXIV-2605-09033 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09033 |
| SF-2026-ARXIV-2605-09045 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09045 |
| SF-2026-ARXIV-2605-09070 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09070 |
| SF-2026-ARXIV-2605-09076 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09076 |
| SF-2026-ARXIV-2605-09126 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09126 |
| SF-2026-ARXIV-2605-09163 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09163 |
| SF-2026-ARXIV-2605-09168 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09168 |
| SF-2026-ARXIV-2605-09204 | score_7_9;forced_review;potential_books_delta | selected | DA-BOUNDED-INTERFACE-BACKPROP | — | 改变跨 stage 状态/通信 ownership，且对 Training System 主线有长期解释力 | analysis:DA-BOUNDED-INTERFACE-BACKPROP |
| SF-2026-ARXIV-2605-09218 | forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09218 |
| SF-2026-ARXIV-2605-09241 | forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-09241 |
| SF-2026-ARXIV-2605-10980 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-10980 |
| SF-2026-ARXIV-2605-10987 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-10987 |
| SF-2026-ARXIV-2605-10990 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-10990 |
| SF-2026-ARXIV-2605-10999 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-10999 |
| SF-2026-ARXIV-2605-11002 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-11002 |
| SF-2026-ARXIV-2605-16360 | forced_review;potential_books_delta | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-16360 |
| SF-2026-ARXIV-2605-23951 | score_7_9 | not_selected | — | — | 完成全文 Review 与 Books Decision；未扩写不等于跳过，三项选中单元覆盖更强的跨层 ownership 变化 | analysis-decision:SF-2026-ARXIV-2605-23951 |

### Routing Replay：把已知未来负载变成 Placement Input

<!-- analysis:DA-ROUTING-REPLAY:start -->普通 MoE placement 依赖历史负载，在 supervised training 或路由平稳时合理；RL rollout 与 training 重放同一 token 且参数不变时，未来 routing 已经可知。ReLibra 把这一事实分成两个 timescale：跨 batch 的 expert reorder 使用跨节点通信预算，batch 内 replication 使用节点内带宽吸收微批波动。它换来更接近理想均衡的 throughput，却新增 rollout/training 参数身份一致、replay stale、replica memory 与重排成本；这些前提不满足时仍应回退历史预测或静态 placement。<!-- analysis:DA-ROUTING-REPLAY:end -->

### 多模态训练：Encoder 与 LLM 不再共享同一并行假设

<!-- analysis:DA-MULTIMODAL-TRAINING-CONTROL:start -->纯文本训练可围绕相对稳定的 sequence shape 和单一 backbone 设计并行；多模态 workload 同时改变 encoder 大小、modality ratio 与 token length，使 encoder 与 LLM 的最优切分不同。MegaScale-Omni 通过 encoder-LLM multiplexing、长短样本重排与分层并行重新分配 data/control ownership。收益来自 workload resilience，代价是更复杂的 reshaping、profile 与 topology coupling；生产集群规格未公开，作者 throughput 不能外推为通用规模结论。<!-- analysis:DA-MULTIMODAL-TRAINING-CONTROL:end -->

### Bounded Interface：为了并行反向传播而共同设计模型边界

<!-- analysis:DA-BOUNDED-INTERFACE-BACKPROP:start -->标准 backprop 保留完整 hidden state，因此精确但跨深度依赖为 O(K)；full-rank scan 虽降 span，却把组合成本推到 O(d^3)。LBI 通过模型原生的低维 interface，把跨 region adjoint 变成 r×r suffix scan，并保持该 architecture 下的 exact gradient。收益以表示瓶颈和 Jacobian materialization 为代价；47–61M block 实验与 r=16 不能证明大模型 scale，interface 不足时必须回退普通 backprop 或增大边界。<!-- analysis:DA-BOUNDED-INTERFACE-BACKPROP:end -->

<!-- analysis-decision:SF-2026-ARXIV-2605-08586:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08586:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08587:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MODEL-SELF-ATTENTION`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08587:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08590:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08590:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08594:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-MONITORING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08594:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08621:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-WORKFLOW`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08621:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08632:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-SPECULATIVE-DECODING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08632:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08636:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08636:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08646:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-SECURITY`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08646:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08647:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-MULTI-AGENT`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08647:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08658:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLANNING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08658:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08666:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `TRAIN-GRPO`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08666:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08678:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08678:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08715:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08715:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08717:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-WORKFLOW`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08717:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08737:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `TRAIN-DPO`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08737:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08747:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08747:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08761:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-MULTI-AGENT`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08761:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08769:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-WORKFLOW`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08769:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08828:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08828:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08835:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-CONTINUOUS-BATCHING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08835:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08838:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-RAG`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08838:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08840:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-KV-CACHE`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08840:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08862:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `TRAIN-DISTRIBUTED-TRAINING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08862:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08871:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `TRAIN-PRETRAINING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08871:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08876:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-SECURITY`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08876:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08879:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-EMBODIED-VLA`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08879:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08894:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-TENSORRT-LLM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08894:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08908:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-SCHEDULING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08908:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08913:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-DECODE`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08913:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08927:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-WORKFLOW`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08927:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-08982:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLANNING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-08982:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09023:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09023:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09033:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-MEMORY`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09033:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09045:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-SECURITY`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09045:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09055:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-TOOL-CALLING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09055:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09070:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09070:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09076:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-MULTI-AGENT`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09076:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09126:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `TRAIN-DISTRIBUTED-TRAINING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09126:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09163:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLATFORM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09163:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09168:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-TOOL-CALLING`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09168:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09192:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-WORKFLOW`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09192:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09218:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-WORLD-MODELS`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09218:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09225:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09225:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09227:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09227:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-09241:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-WORLD-MODELS`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-09241:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10980:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-GENERATIVE-PARADIGMS`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-10980:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10987:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-SECURITY`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-10987:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10990:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLATFORM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-10990:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10993:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-EMBODIED-VLA`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-10993:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-10999:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLATFORM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-10999:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-11002:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `PLATFORM-EVALUATION-SYSTEM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-11002:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16359:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `MULTIMODAL-REPRESENTATION`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-16359:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-16360:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `INFER-KV-CACHE`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-16360:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23951:start -->该 family 已完成 exact-v1 Review、Score 与 Books Comparison；其增量留在 `AGENT-PLATFORM`，没有被 Deep Analysis 上限排除出 Evidence Gate。<!-- analysis-decision:SF-2026-ARXIV-2605-23951:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-08586 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08586 | delta:SF-2026-ARXIV-2605-08586 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08586 |
| SF-2026-ARXIV-2605-08587 | MODEL-SELF-ATTENTION | books/part-02-model/14-self-attention.md#chapter-14 | books/part-02-model/13-position-encoding.md#chapter-13; books/part-02-model/15-multi-head-attention.md#chapter-15 | existing:SF-2026-ARXIV-2605-08587 | delta:SF-2026-ARXIV-2605-08587 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08587 |
| SF-2026-ARXIV-2605-08590 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08590 | delta:SF-2026-ARXIV-2605-08590 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08590 |
| SF-2026-ARXIV-2605-08594 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66; books/part-06-ai-infrastructure/68-logging.md#chapter-68 | existing:SF-2026-ARXIV-2605-08594 | delta:SF-2026-ARXIV-2605-08594 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08594 |
| SF-2026-ARXIV-2605-08621 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-08621 | delta:SF-2026-ARXIV-2605-08621 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08621 |
| SF-2026-ARXIV-2605-08632 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#chapter-48 | books/part-05-inference-system/47-pagedattention.md#chapter-47; books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | existing:SF-2026-ARXIV-2605-08632 | delta:SF-2026-ARXIV-2605-08632 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08632 |
| SF-2026-ARXIV-2605-08636 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08636 | delta:SF-2026-ARXIV-2605-08636 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08636 |
| SF-2026-ARXIV-2605-08639 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-08639 | delta:SF-2026-ARXIV-2605-08639 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08639 |
| SF-2026-ARXIV-2605-08646 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-08646 | delta:SF-2026-ARXIV-2605-08646 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08646 |
| SF-2026-ARXIV-2605-08647 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-08647 | delta:SF-2026-ARXIV-2605-08647 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08647 |
| SF-2026-ARXIV-2605-08658 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78; books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-08658 | delta:SF-2026-ARXIV-2605-08658 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08658 |
| SF-2026-ARXIV-2605-08666 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#chapter-33 | books/part-04-training-system/32-ppo.md#chapter-32; books/part-04-training-system/34-dpo.md#chapter-34 | existing:SF-2026-ARXIV-2605-08666 | delta:SF-2026-ARXIV-2605-08666 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08666 |
| SF-2026-ARXIV-2605-08678 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08678 | delta:SF-2026-ARXIV-2605-08678 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08678 |
| SF-2026-ARXIV-2605-08715 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08715 | delta:SF-2026-ARXIV-2605-08715 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08715 |
| SF-2026-ARXIV-2605-08717 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-08717 | delta:SF-2026-ARXIV-2605-08717 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08717 |
| SF-2026-ARXIV-2605-08737 | TRAIN-DPO | books/part-04-training-system/34-dpo.md#chapter-34 | books/part-04-training-system/33-grpo.md#chapter-33; books/part-04-training-system/35-checkpoint.md#chapter-35 | existing:SF-2026-ARXIV-2605-08737 | delta:SF-2026-ARXIV-2605-08737 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08737 |
| SF-2026-ARXIV-2605-08747 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08747 | delta:SF-2026-ARXIV-2605-08747 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08747 |
| SF-2026-ARXIV-2605-08761 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-08761 | delta:SF-2026-ARXIV-2605-08761 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08761 |
| SF-2026-ARXIV-2605-08769 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-08769 | delta:SF-2026-ARXIV-2605-08769 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08769 |
| SF-2026-ARXIV-2605-08828 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-08828 | delta:SF-2026-ARXIV-2605-08828 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08828 |
| SF-2026-ARXIV-2605-08835 | INFER-CONTINUOUS-BATCHING | books/part-05-inference-system/46-continuous-batching.md#chapter-46 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45; books/part-05-inference-system/47-pagedattention.md#chapter-47 | existing:SF-2026-ARXIV-2605-08835 | delta:SF-2026-ARXIV-2605-08835 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08835 |
| SF-2026-ARXIV-2605-08838 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75; books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-08838 | delta:SF-2026-ARXIV-2605-08838 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08838 |
| SF-2026-ARXIV-2605-08840 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-08840 | delta:SF-2026-ARXIV-2605-08840 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08840 |
| SF-2026-ARXIV-2605-08862 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-08862 | delta:SF-2026-ARXIV-2605-08862 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08862 |
| SF-2026-ARXIV-2605-08871 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#chapter-28 | books/part-04-training-system/27-data.md#chapter-27; books/part-04-training-system/29-sft.md#chapter-29 | existing:SF-2026-ARXIV-2605-08871 | delta:SF-2026-ARXIV-2605-08871 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08871 |
| SF-2026-ARXIV-2605-08876 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-08876 | delta:SF-2026-ARXIV-2605-08876 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08876 |
| SF-2026-ARXIV-2605-08879 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-08879 | delta:SF-2026-ARXIV-2605-08879 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08879 |
| SF-2026-ARXIV-2605-08894 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48; books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-08894 | delta:SF-2026-ARXIV-2605-08894 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08894 |
| SF-2026-ARXIV-2605-08908 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-08908 | delta:SF-2026-ARXIV-2605-08908 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08908 |
| SF-2026-ARXIV-2605-08913 | INFER-DECODE | books/part-05-inference-system/44-decode.md#chapter-44 | books/part-05-inference-system/43-prefill.md#chapter-43; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | existing:SF-2026-ARXIV-2605-08913 | delta:SF-2026-ARXIV-2605-08913 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08913 |
| SF-2026-ARXIV-2605-08927 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-08927 | delta:SF-2026-ARXIV-2605-08927 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08927 |
| SF-2026-ARXIV-2605-08962 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-08962 | delta:SF-2026-ARXIV-2605-08962 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-08962 |
| SF-2026-ARXIV-2605-08982 | AGENT-PLANNING | books/part-07-agent/79-planning.md#chapter-79 | books/part-07-agent/78-tool-calling.md#chapter-78; books/part-07-agent/80-reflection.md#chapter-80 | existing:SF-2026-ARXIV-2605-08982 | delta:SF-2026-ARXIV-2605-08982 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-08982 |
| SF-2026-ARXIV-2605-09023 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-09023 | delta:SF-2026-ARXIV-2605-09023 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09023 |
| SF-2026-ARXIV-2605-09033 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76; books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-09033 | delta:SF-2026-ARXIV-2605-09033 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09033 |
| SF-2026-ARXIV-2605-09045 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-09045 | delta:SF-2026-ARXIV-2605-09045 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09045 |
| SF-2026-ARXIV-2605-09055 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-09055 | delta:SF-2026-ARXIV-2605-09055 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09055 |
| SF-2026-ARXIV-2605-09070 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-09070 | delta:SF-2026-ARXIV-2605-09070 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09070 |
| SF-2026-ARXIV-2605-09076 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81; books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-09076 | delta:SF-2026-ARXIV-2605-09076 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09076 |
| SF-2026-ARXIV-2605-09126 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-09126 | delta:SF-2026-ARXIV-2605-09126 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09126 |
| SF-2026-ARXIV-2605-09163 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-09163 | delta:SF-2026-ARXIV-2605-09163 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09163 |
| SF-2026-ARXIV-2605-09168 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77; books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-09168 | delta:SF-2026-ARXIV-2605-09168 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09168 |
| SF-2026-ARXIV-2605-09192 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80; books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-09192 | delta:SF-2026-ARXIV-2605-09192 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09192 |
| SF-2026-ARXIV-2605-09204 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35; books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-09204 | delta:SF-2026-ARXIV-2605-09204 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09204 |
| SF-2026-ARXIV-2605-09218 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-09218 | delta:SF-2026-ARXIV-2605-09218 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09218 |
| SF-2026-ARXIV-2605-09225 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-09225 | delta:SF-2026-ARXIV-2605-09225 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09225 |
| SF-2026-ARXIV-2605-09227 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-09227 | delta:SF-2026-ARXIV-2605-09227 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-09227 |
| SF-2026-ARXIV-2605-09241 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-09241 | delta:SF-2026-ARXIV-2605-09241 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-09241 |
| SF-2026-ARXIV-2605-10980 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23; books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-10980 | delta:SF-2026-ARXIV-2605-10980 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-10980 |
| SF-2026-ARXIV-2605-10987 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71; books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-10987 | delta:SF-2026-ARXIV-2605-10987 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-10987 |
| SF-2026-ARXIV-2605-10990 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-10990 | delta:SF-2026-ARXIV-2605-10990 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-10990 |
| SF-2026-ARXIV-2605-10993 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | existing:SF-2026-ARXIV-2605-10993 | delta:SF-2026-ARXIV-2605-10993 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10993 |
| SF-2026-ARXIV-2605-10999 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-10999 | delta:SF-2026-ARXIV-2605-10999 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-10999 |
| SF-2026-ARXIV-2605-11002 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65; books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-11002 | delta:SF-2026-ARXIV-2605-11002 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-11002 |
| SF-2026-ARXIV-2605-16359 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#chapter-23 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24 | existing:SF-2026-ARXIV-2605-16359 | delta:SF-2026-ARXIV-2605-16359 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-16359 |
| SF-2026-ARXIV-2605-16360 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44; books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-16360 | delta:SF-2026-ARXIV-2605-16360 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-16360 |
| SF-2026-ARXIV-2605-23951 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23951 | delta:SF-2026-ARXIV-2605-23951 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23951 |
<!-- books-review:SF-2026-ARXIV-2605-08586:start -->
<!-- existing:SF-2026-ARXIV-2605-08586:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain。<!-- existing:SF-2026-ARXIV-2605-08586:end -->
<!-- delta:SF-2026-ARXIV-2605-08586:start -->实验结论需要把论文数字、实际执行、代码身份与签名收据绑定为不可抵赖的 evidence chain<!-- delta:SF-2026-ARXIV-2605-08586:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08586:end -->
<!-- books-review:SF-2026-ARXIV-2605-08587:start -->
<!-- existing:SF-2026-ARXIV-2605-08587:start -->已读取 `books/part-02-model/14-self-attention.md` 及同 Part 前后相邻章节；当前主线已覆盖full attention、线性/递归状态压缩及其写入、遗忘与容量边界。但正文尚未明确承载本 family 的增量边界：线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数。<!-- existing:SF-2026-ARXIV-2605-08587:end -->
<!-- delta:SF-2026-ARXIV-2605-08587:start -->线性注意力的 recurrent state update 应由 online-regression objective 推导步长，而不是只学习无归一化更新系数<!-- delta:SF-2026-ARXIV-2605-08587:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08587:end -->
<!-- books-review:SF-2026-ARXIV-2605-08590:start -->
<!-- existing:SF-2026-ARXIV-2605-08590:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“生成式解释需要把 observation、inference、unknown 分层；增加 context 或 bounded prompt 不能替代 claim-level evidence gate”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08590:end -->
<!-- delta:SF-2026-ARXIV-2605-08590:start -->生成式解释需要把 observation、inference、unknown 分层；增加 context 或 bounded prompt 不能替代 claim-level evidence gate<!-- delta:SF-2026-ARXIV-2605-08590:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08590:end -->
<!-- books-review:SF-2026-ARXIV-2605-08594:start -->
<!-- existing:SF-2026-ARXIV-2605-08594:start -->已读取 `books/part-06-ai-infrastructure/67-monitoring.md` 及同 Part 前后相邻章节；当前主线已覆盖信号采集、传感器身份、silent-data-corruption 检测与失效升级路径。但正文尚未明确承载本 family 的增量边界：AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback。<!-- existing:SF-2026-ARXIV-2605-08594:end -->
<!-- delta:SF-2026-ARXIV-2605-08594:start -->AI accelerator 的 silent-fault sensor 可用代数测试向量保留 PE 行身份；单轮概率定位失败时必须升级到比值型两轮 fallback<!-- delta:SF-2026-ARXIV-2605-08594:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08594:end -->
<!-- books-review:SF-2026-ARXIV-2605-08621:start -->
<!-- existing:SF-2026-ARXIV-2605-08621:start -->已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“迭代修复必须把 build artifact、历史尝试与环境反馈保存为 durable evidence state，并把 tool execution 与 diagnosis/reasoning 分离”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08621:end -->
<!-- delta:SF-2026-ARXIV-2605-08621:start -->迭代修复必须把 build artifact、历史尝试与环境反馈保存为 durable evidence state，并把 tool execution 与 diagnosis/reasoning 分离<!-- delta:SF-2026-ARXIV-2605-08621:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08621:end -->
<!-- books-review:SF-2026-ARXIV-2605-08632:start -->
<!-- existing:SF-2026-ARXIV-2605-08632:start -->已读取 `books/part-05-inference-system/48-speculative-decoding.md` 及同 Part 前后相邻章节；当前主线已覆盖draft/target 身份、target verification、acceptance accounting 与回退边界。本 family 的 exact-v1 增量为“draft model 训练目标应对齐连续 acceptance length，并显式区分 target-dependent 与 target-independent mode”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08632:end -->
<!-- delta:SF-2026-ARXIV-2605-08632:start -->draft model 训练目标应对齐连续 acceptance length，并显式区分 target-dependent 与 target-independent mode<!-- delta:SF-2026-ARXIV-2605-08632:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08632:end -->
<!-- books-review:SF-2026-ARXIV-2605-08636:start -->
<!-- existing:SF-2026-ARXIV-2605-08636:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability。<!-- existing:SF-2026-ARXIV-2605-08636:end -->
<!-- delta:SF-2026-ARXIV-2605-08636:start -->edge federated fine-tuning 的结论必须同时通过 quality-under-budget、cost-to-target 与 perturbation robustness，不能用 simulation 或 final accuracy 代替真实设备 deployability<!-- delta:SF-2026-ARXIV-2605-08636:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08636:end -->
<!-- books-review:SF-2026-ARXIV-2605-08639:start -->
<!-- existing:SF-2026-ARXIV-2605-08639:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权。<!-- existing:SF-2026-ARXIV-2605-08639:end -->
<!-- delta:SF-2026-ARXIV-2605-08639:start -->MoE RL 可把 rollout 已知 routing replay 提升为训练期 placement input，在 inter-batch 重排与 intra-batch replication 间分配控制权<!-- delta:SF-2026-ARXIV-2605-08639:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08639:end -->
<!-- books-review:SF-2026-ARXIV-2605-08646:start -->
<!-- existing:SF-2026-ARXIV-2605-08646:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。本 family 的 exact-v1 增量为“device-cloud agent 的 compute split 本质是 trust boundary；typed placeholder identity 与 deterministic reversal 必须留在设备端”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08646:end -->
<!-- delta:SF-2026-ARXIV-2605-08646:start -->device-cloud agent 的 compute split 本质是 trust boundary；typed placeholder identity 与 deterministic reversal 必须留在设备端<!-- delta:SF-2026-ARXIV-2605-08646:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08646:end -->
<!-- books-review:SF-2026-ARXIV-2605-08647:start -->
<!-- existing:SF-2026-ARXIV-2605-08647:start -->已读取 `books/part-07-agent/82-multi-agent.md` 及同 Part 前后相邻章节；当前主线已覆盖role、permission、coordination topology、错误传播与 Byzantine containment。但正文尚未明确承载本 family 的增量边界：多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案。<!-- existing:SF-2026-ARXIV-2605-08647:end -->
<!-- delta:SF-2026-ARXIV-2605-08647:start -->多 Agent 可靠性必须测量约束跨 hop 生存、错误传播与 converging-DAG synthesis bottleneck，而不只看最终答案<!-- delta:SF-2026-ARXIV-2605-08647:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08647:end -->
<!-- books-review:SF-2026-ARXIV-2605-08658:start -->
<!-- existing:SF-2026-ARXIV-2605-08658:start -->已读取 `books/part-07-agent/79-planning.md` 及同 Part 前后相邻章节；当前主线已覆盖proposal/search/verifier budget、执行反馈和 action commit 的分层。本 family 的 exact-v1 增量为“inference-time search 应分离 strategy sketch、candidate completion、execution verification 与 selection，并承认升级模型 tier 的替代边界”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08658:end -->
<!-- delta:SF-2026-ARXIV-2605-08658:start -->inference-time search 应分离 strategy sketch、candidate completion、execution verification 与 selection，并承认升级模型 tier 的替代边界<!-- delta:SF-2026-ARXIV-2605-08658:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08658:end -->
<!-- books-review:SF-2026-ARXIV-2605-08666:start -->
<!-- existing:SF-2026-ARXIV-2605-08666:start -->已读取 `books/part-04-training-system/33-grpo.md` 及同 Part 前后相邻章节；当前主线已覆盖sequence reward、token credit、group/batch composition 与 verifier 约束。本 family 的 exact-v1 增量为“sequence-level outcome reward 通过共享低置信 token 的梯度耦合产生隐式 token credit；batch composition 因而成为训练语义的一部分”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08666:end -->
<!-- delta:SF-2026-ARXIV-2605-08666:start -->sequence-level outcome reward 通过共享低置信 token 的梯度耦合产生隐式 token credit；batch composition 因而成为训练语义的一部分<!-- delta:SF-2026-ARXIV-2605-08666:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08666:end -->
<!-- books-review:SF-2026-ARXIV-2605-08678:start -->
<!-- existing:SF-2026-ARXIV-2605-08678:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：评测 AI 发现新 ML 方法时必须冻结 evaluator 与 training knobs、限制 editable scope、复现强基线并跨 scale 验证，避免把调参或 harness hacking 计为 discovery。<!-- existing:SF-2026-ARXIV-2605-08678:end -->
<!-- delta:SF-2026-ARXIV-2605-08678:start -->评测 AI 发现新 ML 方法时必须冻结 evaluator 与 training knobs、限制 editable scope、复现强基线并跨 scale 验证，避免把调参或 harness hacking 计为 discovery<!-- delta:SF-2026-ARXIV-2605-08678:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08678:end -->
<!-- books-review:SF-2026-ARXIV-2605-08715:start -->
<!-- existing:SF-2026-ARXIV-2605-08715:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：长轨迹评测应从 post-hoc attribution 前移到 prefix-only online audit，并把 earliest decisive error 作为可干预状态。<!-- existing:SF-2026-ARXIV-2605-08715:end -->
<!-- delta:SF-2026-ARXIV-2605-08715:start -->长轨迹评测应从 post-hoc attribution 前移到 prefix-only online audit，并把 earliest decisive error 作为可干预状态<!-- delta:SF-2026-ARXIV-2605-08715:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08715:end -->
<!-- books-review:SF-2026-ARXIV-2605-08717:start -->
<!-- existing:SF-2026-ARXIV-2605-08717:start -->已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。但正文尚未明确承载本 family 的增量边界：Agent 失败恢复应以运行 telemetry 锚定 diagnosis artifact，经 guidance gate 进入下一次尝试；wrapper 保留执行边界且不能冒充生产 recovery guarantee。<!-- existing:SF-2026-ARXIV-2605-08717:end -->
<!-- delta:SF-2026-ARXIV-2605-08717:start -->Agent 失败恢复应以运行 telemetry 锚定 diagnosis artifact，经 guidance gate 进入下一次尝试；wrapper 保留执行边界且不能冒充生产 recovery guarantee<!-- delta:SF-2026-ARXIV-2605-08717:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08717:end -->
<!-- books-review:SF-2026-ARXIV-2605-08737:start -->
<!-- existing:SF-2026-ARXIV-2605-08737:start -->已读取 `books/part-04-training-system/34-dpo.md` 及同 Part 前后相邻章节；当前主线已覆盖preference pair、reference policy、objective boundary 与 distribution shift。本 family 的 exact-v1 增量为“near-deterministic structured output 的 on-policy distillation 存在可测 extrapolation cliff，格式合同应成为训练控制约束”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08737:end -->
<!-- delta:SF-2026-ARXIV-2605-08737:start -->near-deterministic structured output 的 on-policy distillation 存在可测 extrapolation cliff，格式合同应成为训练控制约束<!-- delta:SF-2026-ARXIV-2605-08737:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08737:end -->
<!-- books-review:SF-2026-ARXIV-2605-08747:start -->
<!-- existing:SF-2026-ARXIV-2605-08747:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：embodied evaluation 必须把 world completion 与 terminal commitment 分开，避免执行成功、停止失败和无证据承诺被压成同一分数。<!-- existing:SF-2026-ARXIV-2605-08747:end -->
<!-- delta:SF-2026-ARXIV-2605-08747:start -->embodied evaluation 必须把 world completion 与 terminal commitment 分开，避免执行成功、停止失败和无证据承诺被压成同一分数<!-- delta:SF-2026-ARXIV-2605-08747:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08747:end -->
<!-- books-review:SF-2026-ARXIV-2605-08761:start -->
<!-- existing:SF-2026-ARXIV-2605-08761:start -->已读取 `books/part-07-agent/82-multi-agent.md` 及同 Part 前后相邻章节；当前主线已覆盖role、permission、coordination topology、错误传播与 Byzantine containment。本 family 的 exact-v1 增量为“企业多 Agent 评测需要把 role permission、stateful service transition、approval commitment 与 coordination cost 放进同一 executable workflow contract”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08761:end -->
<!-- delta:SF-2026-ARXIV-2605-08761:start -->企业多 Agent 评测需要把 role permission、stateful service transition、approval commitment 与 coordination cost 放进同一 executable workflow contract<!-- delta:SF-2026-ARXIV-2605-08761:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08761:end -->
<!-- books-review:SF-2026-ARXIV-2605-08769:start -->
<!-- existing:SF-2026-ARXIV-2605-08769:start -->已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“固定工作流在 task state 变化时会错配；execution-time workflow policy 可选择 agent/edge，但必须版本化 agent pool、depth、reward 与 evaluator”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08769:end -->
<!-- delta:SF-2026-ARXIV-2605-08769:start -->固定工作流在 task state 变化时会错配；execution-time workflow policy 可选择 agent/edge，但必须版本化 agent pool、depth、reward 与 evaluator<!-- delta:SF-2026-ARXIV-2605-08769:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08769:end -->
<!-- books-review:SF-2026-ARXIV-2605-08828:start -->
<!-- existing:SF-2026-ARXIV-2605-08828:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“Agent evidence-grounding 评测必须分开 execution authority、runtime feedback、verification、provenance 与 freshness，并用 oracle-visible environment state 判定误信路径”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08828:end -->
<!-- delta:SF-2026-ARXIV-2605-08828:start -->Agent evidence-grounding 评测必须分开 execution authority、runtime feedback、verification、provenance 与 freshness，并用 oracle-visible environment state 判定误信路径<!-- delta:SF-2026-ARXIV-2605-08828:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08828:end -->
<!-- books-review:SF-2026-ARXIV-2605-08835:start -->
<!-- existing:SF-2026-ARXIV-2605-08835:start -->已读取 `books/part-05-inference-system/46-continuous-batching.md` 及同 Part 前后相邻章节；当前主线已覆盖admission、batch membership、queue feedback、stage contention 与 SLO。但正文尚未明确承载本 family 的增量边界：diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback。<!-- existing:SF-2026-ARXIV-2605-08835:end -->
<!-- delta:SF-2026-ARXIV-2605-08835:start -->diffusion serving 的 continuous batching 要联合控制 UNet throughput、VAE latency、component contention 与 queue feedback<!-- delta:SF-2026-ARXIV-2605-08835:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08835:end -->
<!-- books-review:SF-2026-ARXIV-2605-08838:start -->
<!-- existing:SF-2026-ARXIV-2605-08838:start -->已读取 `books/part-07-agent/76-rag.md` 及同 Part 前后相邻章节；当前主线已覆盖corpus snapshot、retrieval provenance、answer/evidence binding 与 freshness。但正文尚未明确承载本 family 的增量边界：RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释。<!-- existing:SF-2026-ARXIV-2605-08838:end -->
<!-- delta:SF-2026-ARXIV-2605-08838:start -->RAG benchmark 生成必须以受控 corpus transformation 构造可验证 answer/evidence pair，并隔离训练污染与 retrieval leakage；高分只有在冻结 corpus 与 verifier 时可解释<!-- delta:SF-2026-ARXIV-2605-08838:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08838:end -->
<!-- books-review:SF-2026-ARXIV-2605-08840:start -->
<!-- existing:SF-2026-ARXIV-2605-08840:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及同 Part 前后相邻章节；当前主线已覆盖KV identity、生命周期、容量、eviction quality 与 correctness fallback。本 family 的 exact-v1 增量为“KV eviction 的 commit quality 可由 layer-wise output reconstruction 与 spatial-temporal smoothing共同约束，而不能只按局部 attention proxy”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08840:end -->
<!-- delta:SF-2026-ARXIV-2605-08840:start -->KV eviction 的 commit quality 可由 layer-wise output reconstruction 与 spatial-temporal smoothing共同约束，而不能只按局部 attention proxy<!-- delta:SF-2026-ARXIV-2605-08840:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08840:end -->
<!-- books-review:SF-2026-ARXIV-2605-08862:start -->
<!-- existing:SF-2026-ARXIV-2605-08862:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退。<!-- existing:SF-2026-ARXIV-2605-08862:end -->
<!-- delta:SF-2026-ARXIV-2605-08862:start -->同步 RL 的 long-tail bubble 可作为 speculative rollout draft capacity，但必须保留 policy-version verification 与失败回退<!-- delta:SF-2026-ARXIV-2605-08862:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08862:end -->
<!-- books-review:SF-2026-ARXIV-2605-08871:start -->
<!-- existing:SF-2026-ARXIV-2605-08871:start -->已读取 `books/part-04-training-system/28-pretraining.md` 及同 Part 前后相邻章节；当前主线已覆盖data/objective/optimizer coupling、收敛证据与 scale 外推边界。本 family 的 exact-v1 增量为“parallel stochastic optimization 可用 momentum variance reduction 改变同步轮次复杂度，但证据仍限 stochastic quadratic 与 inexact-neural variant”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08871:end -->
<!-- delta:SF-2026-ARXIV-2605-08871:start -->parallel stochastic optimization 可用 momentum variance reduction 改变同步轮次复杂度，但证据仍限 stochastic quadratic 与 inexact-neural variant<!-- delta:SF-2026-ARXIV-2605-08871:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08871:end -->
<!-- books-review:SF-2026-ARXIV-2605-08876:start -->
<!-- existing:SF-2026-ARXIV-2605-08876:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。但正文尚未明确承载本 family 的增量边界：agent availability threat model 必须覆盖 reasoning-level cost amplification，并把 trigger optimization 与 payload optimization 分开。<!-- existing:SF-2026-ARXIV-2605-08876:end -->
<!-- delta:SF-2026-ARXIV-2605-08876:start -->agent availability threat model 必须覆盖 reasoning-level cost amplification，并把 trigger optimization 与 payload optimization 分开<!-- delta:SF-2026-ARXIV-2605-08876:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08876:end -->
<!-- books-review:SF-2026-ARXIV-2605-08879:start -->
<!-- existing:SF-2026-ARXIV-2605-08879:start -->已读取 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及同 Part 前后相邻章节；当前主线已覆盖perception-to-action loop、controller 分层、skill retention 与 physical safety envelope。本 family 的 exact-v1 增量为“flow-matching VLA 的 downstream SFT 需要约束参数 disruption 并同时验收 target acquisition 与 prior-skill retention；保守更新会减慢新 primitive 学习”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08879:end -->
<!-- delta:SF-2026-ARXIV-2605-08879:start -->flow-matching VLA 的 downstream SFT 需要约束参数 disruption 并同时验收 target acquisition 与 prior-skill retention；保守更新会减慢新 primitive 学习<!-- delta:SF-2026-ARXIV-2605-08879:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08879:end -->
<!-- books-review:SF-2026-ARXIV-2605-08894:start -->
<!-- existing:SF-2026-ARXIV-2605-08894:start -->已读取 `books/part-05-inference-system/49-tensorrt-llm.md` 及同 Part 前后相邻章节；当前主线已覆盖execution plan、kernel/quantization contract、精度边界与 fallback。本 family 的 exact-v1 增量为“极低比特量化不仅要拟合训练点，还要约束 loss landscape smoothness 与部署 perturbation sensitivity”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08894:end -->
<!-- delta:SF-2026-ARXIV-2605-08894:start -->极低比特量化不仅要拟合训练点，还要约束 loss landscape smoothness 与部署 perturbation sensitivity<!-- delta:SF-2026-ARXIV-2605-08894:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08894:end -->
<!-- books-review:SF-2026-ARXIV-2605-08908:start -->
<!-- existing:SF-2026-ARXIV-2605-08908:start -->已读取 `books/part-05-inference-system/56-inference-scheduling.md` 及同 Part 前后相邻章节；当前主线已覆盖queue、admission、deadline、locality 与 topology-aware placement。但正文尚未明确承载本 family 的增量边界：共享 cache 对 accelerator request 的 admission/bypass 必须联合预测 reuse 与 deadline；core-centric locality predictor 不能拥有 accelerator deadline commit。<!-- existing:SF-2026-ARXIV-2605-08908:end -->
<!-- delta:SF-2026-ARXIV-2605-08908:start -->共享 cache 对 accelerator request 的 admission/bypass 必须联合预测 reuse 与 deadline；core-centric locality predictor 不能拥有 accelerator deadline commit<!-- delta:SF-2026-ARXIV-2605-08908:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08908:end -->
<!-- books-review:SF-2026-ARXIV-2605-08913:start -->
<!-- existing:SF-2026-ARXIV-2605-08913:start -->已读取 `books/part-05-inference-system/44-decode.md` 及同 Part 前后相邻章节；当前主线已覆盖逐 token decode 的 memory/compute regime、KV state 与 latency measurement contract。但正文尚未明确承载本 family 的增量边界：端侧 decode latency 不是 context/KV 容量的单调函数；backend execution regimes 与 instrumentation perturbation 必须进入 measurement contract。<!-- existing:SF-2026-ARXIV-2605-08913:end -->
<!-- delta:SF-2026-ARXIV-2605-08913:start -->端侧 decode latency 不是 context/KV 容量的单调函数；backend execution regimes 与 instrumentation perturbation 必须进入 measurement contract<!-- delta:SF-2026-ARXIV-2605-08913:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08913:end -->
<!-- books-review:SF-2026-ARXIV-2605-08927:start -->
<!-- existing:SF-2026-ARXIV-2605-08927:start -->已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。但正文尚未明确承载本 family 的增量边界：coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较。<!-- existing:SF-2026-ARXIV-2605-08927:end -->
<!-- delta:SF-2026-ARXIV-2605-08927:start -->coding Agent 生成 compiler optimization 时，proof-producing translation validation 与 credible compilation 是不同 verification contracts；supervision 工时与 compile-time overhead 必须分开比较<!-- delta:SF-2026-ARXIV-2605-08927:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08927:end -->
<!-- books-review:SF-2026-ARXIV-2605-08962:start -->
<!-- existing:SF-2026-ARXIV-2605-08962:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem。<!-- existing:SF-2026-ARXIV-2605-08962:end -->
<!-- delta:SF-2026-ARXIV-2605-08962:start -->多模态训练要把 encoder/LLM 异构并行、sample reshaping 与动态 modality workload 视为共同 runtime control problem<!-- delta:SF-2026-ARXIV-2605-08962:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08962:end -->
<!-- books-review:SF-2026-ARXIV-2605-08982:start -->
<!-- existing:SF-2026-ARXIV-2605-08982:start -->已读取 `books/part-07-agent/79-planning.md` 及同 Part 前后相邻章节；当前主线已覆盖proposal/search/verifier budget、执行反馈和 action commit 的分层。本 family 的 exact-v1 增量为“parallel inference-time scaling 需要 particle diversity、tree state 与 verifier budget 的共同控制，而非独立重复 sampling”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-08982:end -->
<!-- delta:SF-2026-ARXIV-2605-08982:start -->parallel inference-time scaling 需要 particle diversity、tree state 与 verifier budget 的共同控制，而非独立重复 sampling<!-- delta:SF-2026-ARXIV-2605-08982:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-08982:end -->
<!-- books-review:SF-2026-ARXIV-2605-09023:start -->
<!-- existing:SF-2026-ARXIV-2605-09023:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“code-generation uncertainty 可以用可执行 outputs 的 semantic distance 作为 sensor，但不能被提升为通用 truth confidence”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09023:end -->
<!-- delta:SF-2026-ARXIV-2605-09023:start -->code-generation uncertainty 可以用可执行 outputs 的 semantic distance 作为 sensor，但不能被提升为通用 truth confidence<!-- delta:SF-2026-ARXIV-2605-09023:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09023:end -->
<!-- books-review:SF-2026-ARXIV-2605-09033:start -->
<!-- existing:SF-2026-ARXIV-2605-09033:start -->已读取 `books/part-07-agent/77-memory.md` 及同 Part 前后相邻章节；当前主线已覆盖memory write admission、provenance、派生状态与 poisoning containment。但正文尚未明确承载本 family 的增量边界：graph memory poisoning 会利用 relation canonicalization、anchor merge 与 retrieval channel；memory write admission 必须验证关系级 provenance。<!-- existing:SF-2026-ARXIV-2605-09033:end -->
<!-- delta:SF-2026-ARXIV-2605-09033:start -->graph memory poisoning 会利用 relation canonicalization、anchor merge 与 retrieval channel；memory write admission 必须验证关系级 provenance<!-- delta:SF-2026-ARXIV-2605-09033:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09033:end -->
<!-- books-review:SF-2026-ARXIV-2605-09045:start -->
<!-- existing:SF-2026-ARXIV-2605-09045:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。本 family 的 exact-v1 增量为“containment proof 的安全对象应是 typed action 到 boundary event 的 transition，而不是模型意图或 alignment”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09045:end -->
<!-- delta:SF-2026-ARXIV-2605-09045:start -->containment proof 的安全对象应是 typed action 到 boundary event 的 transition，而不是模型意图或 alignment<!-- delta:SF-2026-ARXIV-2605-09045:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09045:end -->
<!-- books-review:SF-2026-ARXIV-2605-09055:start -->
<!-- existing:SF-2026-ARXIV-2605-09055:start -->已读取 `books/part-07-agent/78-tool-calling.md` 及同 Part 前后相邻章节；当前主线已覆盖tool proposal、typed capability、least privilege 与 high-risk commit authority。本 family 的 exact-v1 增量为“hardware discovery 可编码为一次性 capability prompt，但没有独立 evaluation 或长期 protocol evidence 支持其成为新 owner”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09055:end -->
<!-- delta:SF-2026-ARXIV-2605-09055:start -->hardware discovery 可编码为一次性 capability prompt，但没有独立 evaluation 或长期 protocol evidence 支持其成为新 owner<!-- delta:SF-2026-ARXIV-2605-09055:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09055:end -->
<!-- books-review:SF-2026-ARXIV-2605-09070:start -->
<!-- existing:SF-2026-ARXIV-2605-09070:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“jailbreak evaluation 应报告攻击配置分布而非单点 ASR，并冻结 judge、variant grid 与 generation count”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09070:end -->
<!-- delta:SF-2026-ARXIV-2605-09070:start -->jailbreak evaluation 应报告攻击配置分布而非单点 ASR，并冻结 judge、variant grid 与 generation count<!-- delta:SF-2026-ARXIV-2605-09070:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09070:end -->
<!-- books-review:SF-2026-ARXIV-2605-09076:start -->
<!-- existing:SF-2026-ARXIV-2605-09076:start -->已读取 `books/part-07-agent/82-multi-agent.md` 及同 Part 前后相邻章节；当前主线已覆盖role、permission、coordination topology、错误传播与 Byzantine containment。本 family 的 exact-v1 增量为“Byzantine 多 Agent 不能信任 sender confidence；receiver-side trust 与 topology containment 必须共同决定 aggregation”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09076:end -->
<!-- delta:SF-2026-ARXIV-2605-09076:start -->Byzantine 多 Agent 不能信任 sender confidence；receiver-side trust 与 topology containment 必须共同决定 aggregation<!-- delta:SF-2026-ARXIV-2605-09076:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09076:end -->
<!-- books-review:SF-2026-ARXIV-2605-09126:start -->
<!-- existing:SF-2026-ARXIV-2605-09126:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收。<!-- existing:SF-2026-ARXIV-2605-09126:end -->
<!-- delta:SF-2026-ARXIV-2605-09126:start -->decoupled DiLoCo outer optimizer 应根据 update cosine/staleness gate 衰减，而不是把所有迟到 update 等价接收<!-- delta:SF-2026-ARXIV-2605-09126:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09126:end -->
<!-- books-review:SF-2026-ARXIV-2605-09163:start -->
<!-- existing:SF-2026-ARXIV-2605-09163:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及同 Part 前后相邻章节；当前主线已覆盖skill/tool artifact 的身份、版本、admission、drift 与 capability containment。本 family 的 exact-v1 增量为“skill 安全评测要比较声明 capability 与实际需要的最小 capability，并把 over-privilege 作为可执行 contract gap”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09163:end -->
<!-- delta:SF-2026-ARXIV-2605-09163:start -->skill 安全评测要比较声明 capability 与实际需要的最小 capability，并把 over-privilege 作为可执行 contract gap<!-- delta:SF-2026-ARXIV-2605-09163:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09163:end -->
<!-- books-review:SF-2026-ARXIV-2605-09168:start -->
<!-- existing:SF-2026-ARXIV-2605-09168:start -->已读取 `books/part-07-agent/78-tool-calling.md` 及同 Part 前后相邻章节；当前主线已覆盖tool proposal、typed capability、least privilege 与 high-risk commit authority。但正文尚未明确承载本 family 的增量边界：高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据。<!-- existing:SF-2026-ARXIV-2605-09168:end -->
<!-- delta:SF-2026-ARXIV-2605-09168:start -->高风险 action commit 应咨询显式 causal graph，并用 intervention consistency 区分相关性证据与可执行因果依据<!-- delta:SF-2026-ARXIV-2605-09168:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09168:end -->
<!-- books-review:SF-2026-ARXIV-2605-09192:start -->
<!-- existing:SF-2026-ARXIV-2605-09192:start -->已读取 `books/part-07-agent/81-workflow.md` 及同 Part 前后相邻章节；当前主线已覆盖版本化 workflow artifact、外部执行证据、重试状态与 commit authority。本 family 的 exact-v1 增量为“skill distillation 应保存 environment-verified trajectory evidence，并以在线 PDI 判断 procedure 是否真正改变执行结果”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09192:end -->
<!-- delta:SF-2026-ARXIV-2605-09192:start -->skill distillation 应保存 environment-verified trajectory evidence，并以在线 PDI 判断 procedure 是否真正改变执行结果<!-- delta:SF-2026-ARXIV-2605-09192:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09192:end -->
<!-- books-review:SF-2026-ARXIV-2605-09204:start -->
<!-- existing:SF-2026-ARXIV-2605-09204:start -->已读取 `books/part-04-training-system/36-distributed-training.md` 及同 Part 前后相邻章节；当前主线已覆盖topology、collective、placement、并行维度和 stale-state 的 runtime ownership。但正文尚未明确承载本 family 的增量边界：depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度。<!-- existing:SF-2026-ARXIV-2605-09204:end -->
<!-- delta:SF-2026-ARXIV-2605-09204:start -->depth-parallel backprop 可通过模型原生 bounded interface 把跨 region adjoint transport 压缩为 exact suffix scan，但会牺牲表示自由度<!-- delta:SF-2026-ARXIV-2605-09204:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09204:end -->
<!-- books-review:SF-2026-ARXIV-2605-09218:start -->
<!-- existing:SF-2026-ARXIV-2605-09218:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及同 Part 前后相邻章节；当前主线已覆盖action-conditioned transition、persistent/revisable world state 与 planning handoff。但正文尚未明确承载本 family 的增量边界：可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写。<!-- existing:SF-2026-ARXIV-2605-09218:end -->
<!-- delta:SF-2026-ARXIV-2605-09218:start -->可编辑 3D scene memory 应把 geometry、free space、hypothetical insertion 与外部修正保存为 typed world state，并让 Agent 只通过 composable spatial tools 读写<!-- delta:SF-2026-ARXIV-2605-09218:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09218:end -->
<!-- books-review:SF-2026-ARXIV-2605-09225:start -->
<!-- existing:SF-2026-ARXIV-2605-09225:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“jailbreak 评测需要连续质量函数同时刻画 harmfulness 与语义保真，binary ASR 只保留为受限指标”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09225:end -->
<!-- delta:SF-2026-ARXIV-2605-09225:start -->jailbreak 评测需要连续质量函数同时刻画 harmfulness 与语义保真，binary ASR 只保留为受限指标<!-- delta:SF-2026-ARXIV-2605-09225:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09225:end -->
<!-- books-review:SF-2026-ARXIV-2605-09227:start -->
<!-- existing:SF-2026-ARXIV-2605-09227:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。本 family 的 exact-v1 增量为“LLM-judge calibration 应按 paired-anchor budget 与非线性程度选择 hierarchical linear 或 score-transport corrector”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-09227:end -->
<!-- delta:SF-2026-ARXIV-2605-09227:start -->LLM-judge calibration 应按 paired-anchor budget 与非线性程度选择 hierarchical linear 或 score-transport corrector<!-- delta:SF-2026-ARXIV-2605-09227:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09227:end -->
<!-- books-review:SF-2026-ARXIV-2605-09241:start -->
<!-- existing:SF-2026-ARXIV-2605-09241:start -->已读取 `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 及同 Part 前后相邻章节；当前主线已覆盖action-conditioned transition、persistent/revisable world state 与 planning handoff。但正文尚未明确承载本 family 的增量边界：JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior。<!-- existing:SF-2026-ARXIV-2605-09241:end -->
<!-- delta:SF-2026-ARXIV-2605-09241:start -->JEPA anti-collapse regularization 应在多个低维 subspace 中约束分布，而非强迫 full ambient representation 服从 isotropic prior<!-- delta:SF-2026-ARXIV-2605-09241:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-09241:end -->
<!-- books-review:SF-2026-ARXIV-2605-10980:start -->
<!-- existing:SF-2026-ARXIV-2605-10980:start -->已读取 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 及同 Part 前后相邻章节；当前主线已覆盖AR/diffusion/masked refinement 的 commit、correction 与并行边界。但正文尚未明确承载本 family 的增量边界：diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件。<!-- existing:SF-2026-ARXIV-2605-10980:end -->
<!-- delta:SF-2026-ARXIV-2605-10980:start -->diffusion LM parallel decode 应检测 early-converged token，而不是把 high confidence 当作唯一安全 commit 条件<!-- delta:SF-2026-ARXIV-2605-10980:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10980:end -->
<!-- books-review:SF-2026-ARXIV-2605-10987:start -->
<!-- existing:SF-2026-ARXIV-2605-10987:start -->已读取 `books/part-06-ai-infrastructure/72-security.md` 及同 Part 前后相邻章节；当前主线已覆盖typed capability、trust boundary、policy enforcement 与 least-privilege action commit。但正文尚未明确承载本 family 的增量边界：动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险。<!-- existing:SF-2026-ARXIV-2605-10987:end -->
<!-- delta:SF-2026-ARXIV-2605-10987:start -->动态 ML pipeline 的 availability attack surface 由 execution-path fan-out 与 downstream workload volume 共同决定，单模型 perturbation 预算不足以描述风险<!-- delta:SF-2026-ARXIV-2605-10987:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10987:end -->
<!-- books-review:SF-2026-ARXIV-2605-10990:start -->
<!-- existing:SF-2026-ARXIV-2605-10990:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及同 Part 前后相邻章节；当前主线已覆盖skill/tool artifact 的身份、版本、admission、drift 与 capability containment。但正文尚未明确承载本 family 的增量边界：skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警。<!-- existing:SF-2026-ARXIV-2605-10990:end -->
<!-- delta:SF-2026-ARXIV-2605-10990:start -->skill drift 应以 role-bearing environment contract violation 检测，而不是对版本字符串或任意值变化报警<!-- delta:SF-2026-ARXIV-2605-10990:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10990:end -->
<!-- books-review:SF-2026-ARXIV-2605-10993:start -->
<!-- existing:SF-2026-ARXIV-2605-10993:start -->已读取 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 及同 Part 前后相邻章节；当前主线已覆盖perception-to-action loop、controller 分层、skill retention 与 physical safety envelope。本 family 的 exact-v1 增量为“VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-10993:end -->
<!-- delta:SF-2026-ARXIV-2605-10993:start -->VLA 长任务记忆需要层次化 semantic tree、top-down retrieval 与 background consolidation，而不只是线性历史 buffer<!-- delta:SF-2026-ARXIV-2605-10993:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10993:end -->
<!-- books-review:SF-2026-ARXIV-2605-10999:start -->
<!-- existing:SF-2026-ARXIV-2605-10999:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及同 Part 前后相邻章节；当前主线已覆盖skill/tool artifact 的身份、版本、admission、drift 与 capability containment。本 family 的 exact-v1 增量为“inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-10999:end -->
<!-- delta:SF-2026-ARXIV-2605-10999:start -->inference-time skill synthesis 必须比较同一实例有/无 skill 的 repairs 与 regressions，生成 artifact 只是 proposal 而非 admission<!-- delta:SF-2026-ARXIV-2605-10999:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-10999:end -->
<!-- books-review:SF-2026-ARXIV-2605-11002:start -->
<!-- existing:SF-2026-ARXIV-2605-11002:start -->已读取 `books/part-06-ai-infrastructure/66-evaluation-system.md` 及同 Part 前后相邻章节；当前主线已覆盖model×harness×environment×scorer×budget 的可复算评测合同、evidence provenance 与 release authority 分离。但正文尚未明确承载本 family 的增量边界：多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块。<!-- existing:SF-2026-ARXIV-2605-11002:end -->
<!-- delta:SF-2026-ARXIV-2605-11002:start -->多轮 jailbreak benchmark 必须冻结 turn/retry/interaction/strategy/judge budget，并把 strategy、prompt generation、refinement 与 flow control 拆成可重组模块<!-- delta:SF-2026-ARXIV-2605-11002:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-11002:end -->
<!-- books-review:SF-2026-ARXIV-2605-16359:start -->
<!-- existing:SF-2026-ARXIV-2605-16359:start -->已读取 `books/part-03-multimodal-world-models/23-multimodal-representation.md` 及同 Part 前后相邻章节；当前主线已覆盖modality token identity、fusion、coverage 与 provenance。本 family 的 exact-v1 增量为“视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-16359:end -->
<!-- delta:SF-2026-ARXIV-2605-16359:start -->视觉 token pruning 应作为 task-conditioned evidence search，预算分配需同时保留局部相关性与 coverage recovery<!-- delta:SF-2026-ARXIV-2605-16359:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16359:end -->
<!-- books-review:SF-2026-ARXIV-2605-16360:start -->
<!-- existing:SF-2026-ARXIV-2605-16360:start -->已读取 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 及同 Part 前后相邻章节；当前主线已覆盖KV identity、生命周期、容量、eviction quality 与 correctness fallback。但正文尚未明确承载本 family 的增量边界：高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束。<!-- existing:SF-2026-ARXIV-2605-16360:end -->
<!-- delta:SF-2026-ARXIV-2605-16360:start -->高精度 KV importance scoring 可异步交给同 family 小模型 proxy，但会增加 prefill 峰值显存并受 intra-family transfer 约束<!-- delta:SF-2026-ARXIV-2605-16360:end --> Decision: `Integrate`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-16360:end -->
<!-- books-review:SF-2026-ARXIV-2605-23951:start -->
<!-- existing:SF-2026-ARXIV-2605-23951:start -->已读取 `books/part-07-agent/84-agent-platform.md` 及同 Part 前后相邻章节；当前主线已覆盖skill/tool artifact 的身份、版本、admission、drift 与 capability containment。本 family 的 exact-v1 增量为“agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness”，它没有改变现有 owner、控制权或共存边界，因此作为受限案例留在 Daily。<!-- existing:SF-2026-ARXIV-2605-23951:end -->
<!-- delta:SF-2026-ARXIV-2605-23951:start -->agent skill capability containment 需要 static effect analysis、refinement-typed dispatch 与 bounded model checking 组合，经验测试不能替代 soundness<!-- delta:SF-2026-ARXIV-2605-23951:end --> Decision: `No Change — Existing Coverage`。author lane 未修改共享 Books。
<!-- books-review:SF-2026-ARXIV-2605-23951:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260510-COVERAGE-FRESH | fresh-context:non-author | coverage | coverage:SRC-ARXIV:20260510 | none | 436/436 重放；author 42/394 经 challenge 后为 57/379，15 个 false negative 已重开 | passed |
| SA-20260510-EVIDENCE-FRESH | fresh-context:non-author | evidence | review:SF-2026-ARXIV-2605-08586 | none | 57/57 exact-v1 的 Method、evaluation、non-proof 与 claim boundary 已挑战；blocked=0 | passed |
| SA-20260510-SELECTION-FRESH | fresh-context:non-author | deep_analysis_selection | analysis:DA-ROUTING-REPLAY | none | 所有 eligible family 已完成 Review；3 个 narrative unit 保留跨层 ownership 变化最强的机制 | passed |
| SA-20260510-BOOKS-POSTWRITE | fresh-context:may2026_day03 | books | books-review:SF-2026-ARXIV-2605-08586 | none | 29/29 marker、机制、约束/控制权、trade-off、failure、fallback 与 evidence boundary 已核；29/29 位于首个二级 `## Review notes` 前，adjacent owner duplicate=0 | passed |

## 8. Ignored Noise

379 项 family-specific pre-denominator closure 位于 `../_sources/daily-20260510/screening-ledger-final.json`；它们保留真实 title、abstract、方法/结果摘要与排除边界。

## 9. Recommended Action

本日已闭环；后续仅在 primary revision 或相邻 owner 发生实质变化时重开。

## 10. Repository Changes

- 新增 05-10 date-local coverage、screening、exact-v1、provenance、Books comparison、queue 与 author audit。
- 未修改共享 Books，未 stage、commit 或 push。

## 11. Open Questions

- None。

## 12. Sources

- DataCite adjacent-month v2 snapshot（identity/date/abstract recovery only）
- [Computer Science Conferences Should Require Nonrepudiable Experimental Results](https://arxiv.org/html/2605.08586v1) — arXiv:2605.08586v1；first-public 2026-05-09；accessed 2026-09-01
- [Kaczmarz Linear Attention](https://arxiv.org/html/2605.08587v1) — arXiv:2605.08587v1；first-public 2026-05-09；accessed 2026-09-01
- [Causal Stories from Sensor Traces: Auditing Epistemic Overreach in LLM-Generated Personal Sensing Explanations](https://arxiv.org/html/2605.08590v1) — arXiv:2605.08590v1；first-public 2026-05-09；accessed 2026-09-01
- [FLARE: One-Shot PE-Level Fault Localization in Systolic Arrays via Algebraic Test Vectors](https://arxiv.org/html/2605.08594v1) — arXiv:2605.08594v1；first-public 2026-05-09；accessed 2026-09-01
- [EvidenT: An Evidence-Preserving Framework for Iterative System-Level Package Repair](https://arxiv.org/html/2605.08621v1) — arXiv:2605.08621v1；first-public 2026-05-09；accessed 2026-09-01
- [PARD-2: Target-Aligned Parallel Draft Model for Dual-Mode Speculative Decoding](https://arxiv.org/html/2605.08632v1) — arXiv:2605.08632v1；first-public 2026-05-09；accessed 2026-09-01
- [EdgeFlowerTune: Evaluating Federated LLM Fine-Tuning Under Realistic Edge System Constraints](https://arxiv.org/html/2605.08636v1) — arXiv:2605.08636v1；first-public 2026-05-09；accessed 2026-09-01
- [ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning](https://arxiv.org/html/2605.08639v1) — arXiv:2605.08639v1；first-public 2026-05-09；accessed 2026-09-01
- [PAAC: Privacy-Aware Agentic Device-Cloud Collaboration](https://arxiv.org/html/2605.08646v1) — arXiv:2605.08646v1；first-public 2026-05-09；accessed 2026-09-01
- [AgentCollabBench: Diagnosing When Good Agents Make Bad Collaborators](https://arxiv.org/html/2605.08647v1) — arXiv:2605.08647v1；first-public 2026-05-09；accessed 2026-09-01
- [Sketch-and-Verify: Structured Inference-Time Scaling via Program Sketching](https://arxiv.org/html/2605.08658v1) — arXiv:2605.08658v1；first-public 2026-05-09；accessed 2026-09-01
- [The Cancellation Hypothesis in Critic-Free RL: From Outcome Rewards to Token Credits](https://arxiv.org/html/2605.08666v1) — arXiv:2605.08666v1；first-public 2026-05-09；accessed 2026-09-01
- [MLS-Bench: A Holistic and Rigorous Assessment of AI Systems on Building Better AI](https://arxiv.org/html/2605.08678v1) — arXiv:2605.08678v1；first-public 2026-05-09；accessed 2026-09-01
- [AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent Systems](https://arxiv.org/html/2605.08715v1) — arXiv:2605.08715v1；first-public 2026-05-09；accessed 2026-09-01
- [Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering Agents](https://arxiv.org/html/2605.08717v1) — arXiv:2605.08717v1；first-public 2026-05-09；accessed 2026-09-01
- [The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs](https://arxiv.org/html/2605.08737v1) — arXiv:2605.08737v1；first-public 2026-05-09；accessed 2026-09-01
- [Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents](https://arxiv.org/html/2605.08747v1) — arXiv:2605.08747v1；first-public 2026-05-09；accessed 2026-09-01
- [Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows](https://arxiv.org/html/2605.08761v1) — arXiv:2605.08761v1；first-public 2026-05-09；accessed 2026-09-01
- [EvoMAS: Learning Execution-Time Workflows for Multi-Agent Systems](https://arxiv.org/html/2605.08769v1) — arXiv:2605.08769v1；first-public 2026-05-09；accessed 2026-09-01
- [When Agents Overtrust Environmental Evidence: An Extensible Agentic Framework for Benchmarking Evidence-Grounding Defects in LLM Agents](https://arxiv.org/html/2605.08828v1) — arXiv:2605.08828v1；first-public 2026-05-09；accessed 2026-09-01
- [SynerDiff: Synergetic Continuous Batching for Fast and Parallel Diffusion Model Inference](https://arxiv.org/html/2605.08835v1) — arXiv:2605.08835v1；first-public 2026-05-09；accessed 2026-09-01
- [Generating Leakage-Free Benchmarks for Robust RAG Evaluation](https://arxiv.org/html/2605.08838v1) — arXiv:2605.08838v1；first-public 2026-05-09；accessed 2026-09-01
- [ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing](https://arxiv.org/html/2605.08840v1) — arXiv:2605.08840v1；first-public 2026-05-09；accessed 2026-09-01
- [BubbleSpec: Turning Long-Tail Bubbles into Speculative Rollout Drafts for Synchronous Reinforcement Learning](https://arxiv.org/html/2605.08862v1) — arXiv:2605.08862v1；first-public 2026-05-09；accessed 2026-09-01
- [Rennala MVR: Improved Time Complexity for Parallel Stochastic Optimization via Momentum-Based Variance Reduction](https://arxiv.org/html/2605.08871v1) — arXiv:2605.08871v1；first-public 2026-05-09；accessed 2026-09-01
- [OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents](https://arxiv.org/html/2605.08876v1) — arXiv:2605.08876v1；first-public 2026-05-09；accessed 2026-09-01
- [Preserving Foundational Capabilities in Flow-Matching VLAs through Conservative SFT](https://arxiv.org/html/2605.08879v1) — arXiv:2605.08879v1；first-public 2026-05-09；accessed 2026-09-01
- [Fitting Is Not Enough: Smoothness in Extremely Quantized LLMs](https://arxiv.org/html/2605.08894v1) — arXiv:2605.08894v1；first-public 2026-05-09；accessed 2026-09-01
- [HyDRA: Deadline and Reuse-Aware Cacheability for Hardware Accelerators](https://arxiv.org/html/2605.08908v1) — arXiv:2605.08908v1；first-public 2026-05-09；accessed 2026-09-01
- [Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes](https://arxiv.org/html/2605.08913v1) — arXiv:2605.08913v1；first-public 2026-05-09；accessed 2026-09-01
- [Quantitative Comparison of Credible Compilation and Verification In Coding Agent Compiler Development](https://arxiv.org/html/2605.08927v1) — arXiv:2605.08927v1；first-public 2026-05-09；accessed 2026-09-01
- [MegaScale-Omni: A Hyper-Scale, Workload-Resilient System for MultiModal LLM Training in Production](https://arxiv.org/html/2605.08962v1) — arXiv:2605.08962v1；first-public 2026-05-09；accessed 2026-09-01
- [PMCTS: Particle Monte Carlo Tree Search for Principled Parallelized Inference Time Scaling](https://arxiv.org/html/2605.08982v1) — arXiv:2605.08982v1；first-public 2026-05-09；accessed 2026-09-01
- [Using Semantic Distance to Estimate Uncertainty in LLM-Based Code Generation](https://arxiv.org/html/2605.09023v1) — arXiv:2605.09023v1；first-public 2026-05-09；accessed 2026-09-01
- [ShadowMerge: A Novel Poisoning Attack on Graph-Based Agent Memory via Relation-Channel Conflicts](https://arxiv.org/html/2605.09033v1) — arXiv:2605.09033v1；first-public 2026-05-09；accessed 2026-09-01
- [Containment Verification: AI Safety Guarantees Independent of Alignment](https://arxiv.org/html/2605.09045v1) — arXiv:2605.09045v1；first-public 2026-05-09；accessed 2026-09-01
- [Octopus Protocol: One-Shot Hardware Discovery and Control for AI Agents via Infrastructure-as-Prompts](https://arxiv.org/html/2605.09055v1) — arXiv:2605.09055v1；first-public 2026-05-09；accessed 2026-09-01
- [Single-Configuration Attack Success Rate Is Not Enough: Jailbreak Evaluations Should Report Distributional Attack Success](https://arxiv.org/html/2605.09070v1) — arXiv:2605.09070v1；first-public 2026-05-09；accessed 2026-09-01
- [Robust Multi-Agent LLMs under Byzantine Faults](https://arxiv.org/html/2605.09076v1) — arXiv:2605.09076v1；first-public 2026-05-09；accessed 2026-09-01
- [Cosine-Gated Adam-Decay: Drop-In Staleness-Aware Outer Optimization for Decoupled DiLoCo](https://arxiv.org/html/2605.09126v1) — arXiv:2605.09126v1；first-public 2026-05-09；accessed 2026-09-01
- [FORTIS: Benchmarking Over-Privilege in Agent Skills](https://arxiv.org/html/2605.09163v1) — arXiv:2605.09163v1；first-public 2026-05-09；accessed 2026-09-01
- [CIVeX: Causal Intervention Verification for Language Agents](https://arxiv.org/html/2605.09168v1) — arXiv:2605.09168v1；first-public 2026-05-09；accessed 2026-09-01
- [Evidence Over Plans: Online Trajectory Verification for Skill Distillation](https://arxiv.org/html/2605.09192v1) — arXiv:2605.09192v1；first-public 2026-05-09；accessed 2026-09-01
- [LBI: Parallel Scan Backpropagation via Latent Bounded Interfaces](https://arxiv.org/html/2605.09204v1) — arXiv:2605.09204v1；first-public 2026-05-09；accessed 2026-09-01
- [Flame3D: Zero-shot Compositional Reasoning of 3D Scenes with Agentic Language Models](https://arxiv.org/html/2605.09218v1) — arXiv:2605.09218v1；first-public 2026-05-09；accessed 2026-09-01
- [The Art of the Jailbreak: Formulating Jailbreak Attacks for LLM Security Beyond Binary Scoring](https://arxiv.org/html/2605.09225v1) — arXiv:2605.09225v1；first-public 2026-05-09；accessed 2026-09-01
- [Two Ways to De-Bias an LLM-as-a-Judge: A Continuous-Score Comparison of Hierarchical Bayesian Calibration and Neural-ODE Score Transport](https://arxiv.org/html/2605.09227v1) — arXiv:2605.09227v1；first-public 2026-05-09；accessed 2026-09-01
- [Sub-JEPA: Subspace Gaussian Regularization for Stable End-to-End World Models](https://arxiv.org/html/2605.09241v1) — arXiv:2605.09241v1；first-public 2026-05-09；accessed 2026-09-01
- [LEAP: Unlocking dLLM Parallelism via Lookahead Early-Convergence Token Detection](https://arxiv.org/html/2605.10980v1) — arXiv:2605.10980v1；first-public 2026-05-09；accessed 2026-09-01
- [AESOP: Adversarial Execution-path Selection to Overload Deep Learning Pipelines](https://arxiv.org/html/2605.10987v1) — arXiv:2605.10987v1；first-public 2026-05-09；accessed 2026-09-01
- [Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries](https://arxiv.org/html/2605.10990v1) — arXiv:2605.10990v1；first-public 2026-05-09；accessed 2026-09-01
- [ECHO: Continuous Hierarchical Memory for Vision-Language-Action Models](https://arxiv.org/html/2605.10993v1) — arXiv:2605.10993v1；first-public 2026-05-09；accessed 2026-09-01
- [SkillGen: Verified Inference-Time Agent Skill Synthesis](https://arxiv.org/html/2605.10999v1) — arXiv:2605.10999v1；first-public 2026-05-09；accessed 2026-09-01
- [MT-JailBench: A Modular Benchmark for Understanding Multi-Turn Jailbreak Attacks](https://arxiv.org/html/2605.11002v1) — arXiv:2605.11002v1；first-public 2026-05-09；accessed 2026-09-01
- [How Many Visual Tokens Do Multimodal Language Models Need? Scaling Visual Token Pruning with F^3A](https://arxiv.org/html/2605.16359v1) — arXiv:2605.16359v1；first-public 2026-05-09；accessed 2026-09-01
- [ProxyKV: Cross-Model Proxy Pruning for Efficient Long-Context LLM Inference](https://arxiv.org/html/2605.16360v1) — arXiv:2605.16360v1；first-public 2026-05-09；accessed 2026-09-01
- [Methods for Formal Verification of Agent Skills: Three Layers Toward a Mechanically Checkable Capability-Containment Proof](https://arxiv.org/html/2605.23951v1) — arXiv:2605.23951v1；first-public 2026-05-09；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

29 项 Books writeback 的 marker、正文机制、首个二级 Review notes 前 placement、owner 唯一性与相邻章节边界均已通过独立复核；本日完整闭环。
