# Daily Research — 2026-05-23

**Research Date:** 2026-05-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-05-22 09:00:00 ～ 2026-05-23 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；technical claims bind official arXiv exact-v1 HTML。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。13/13 串行 Books 写回已通过不同 reviewer post-write semantic audit。

## Executive Summary

独立重放 508/508 个窗口身份：author denominator 37，经 0 个 false positive 与 24 个 false negative reconciliation 后冻结为 61；pre-denominator closures=447，exact-v1=61/61，blocked=0，ordinary pending=0。current Books owner+adjacent challenge 将 author queue 26 重判为最终 queue 13；13/13 已进入 8 个 canonical owner 章节的机制主线，Books Gate 仍等待不同 reviewer 独立验收。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-05-23 |
| Window End | 2026-05-23 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260523-V2-INDEPENDENT |
| Denominator Frozen At | 2026-09-01T10:38:35+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-05-22T09:00:00+08:00 | 2026-05-23T09:00:00+08:00 | 2026-09-01T10:38:35+08:00 | DataCite v2 00..99 + independent 508/508 title+abstract replay + official exact-v1 HTML | checked | 508 | SF-2026-ARXIV-2605-23157;SF-2026-ARXIV-2605-23158;SF-2026-ARXIV-2605-23168;SF-2026-ARXIV-2605-23170;SF-2026-ARXIV-2605-23196;SF-2026-ARXIV-2605-23200;SF-2026-ARXIV-2605-23215;SF-2026-ARXIV-2605-23218;SF-2026-ARXIV-2605-23220;SF-2026-ARXIV-2605-23258;SF-2026-ARXIV-2605-23262;SF-2026-ARXIV-2605-23294;SF-2026-ARXIV-2605-23296;SF-2026-ARXIV-2605-23311;SF-2026-ARXIV-2605-23348;SF-2026-ARXIV-2605-23362;SF-2026-ARXIV-2605-23389;SF-2026-ARXIV-2605-23414;SF-2026-ARXIV-2605-23454;SF-2026-ARXIV-2605-23464;SF-2026-ARXIV-2605-23493;SF-2026-ARXIV-2605-23574;SF-2026-ARXIV-2605-23590;SF-2026-ARXIV-2605-23628;SF-2026-ARXIV-2605-23640;SF-2026-ARXIV-2605-23657;SF-2026-ARXIV-2605-23701;SF-2026-ARXIV-2605-23723;SF-2026-ARXIV-2605-23764;SF-2026-ARXIV-2605-23856;SF-2026-ARXIV-2605-23893;SF-2026-ARXIV-2605-23899;SF-2026-ARXIV-2605-23904;SF-2026-ARXIV-2605-24060;SF-2026-ARXIV-2605-24069;SF-2026-ARXIV-2605-24117;SF-2026-ARXIV-2605-24134;SF-2026-ARXIV-2605-24154;SF-2026-ARXIV-2605-24168;SF-2026-ARXIV-2605-24183;SF-2026-ARXIV-2605-24197;SF-2026-ARXIV-2605-24202;SF-2026-ARXIV-2605-24213;SF-2026-ARXIV-2605-24216;SF-2026-ARXIV-2605-24217;SF-2026-ARXIV-2605-24219;SF-2026-ARXIV-2605-24220;SF-2026-ARXIV-2605-24229;SF-2026-ARXIV-2605-24245;SF-2026-ARXIV-2605-24247;SF-2026-ARXIV-2605-24248;SF-2026-ARXIV-2605-24259;SF-2026-ARXIV-2605-24279;SF-2026-ARXIV-2605-24286;SF-2026-ARXIV-2605-24299;SF-2026-ARXIV-2605-24309;SF-2026-ARXIV-2605-24312;SF-2026-ARXIV-2605-26147;SF-2026-ARXIV-2605-27432;SF-2026-ARXIV-2605-27435;SF-2026-ARXIV-2605-27437 | pages=300;final_cursor=end;raw=91841;registered=508;screened=508;retained=61;closure=447 | 2026-05-23T00:59:59Z | screening-ledger-final.json#sha256=6b930a37106506b23aa9e8dd03db740f926a4aa8a6f74a3b61ce9cf7794901de | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260523:start -->508/508 identity 已独立逐项重放；24 个 author false negative 已恢复，0 个 author false positive，447 条 family-specific closure 已复核。first-public、v1、owner week 与重复 family 已对账；无 ordinary pending 或 exact-version blocker。<!-- coverage:SRC-ARXIV:20260523:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23157 | arXiv:2605.23157v1 | paper-v1:2605.23157 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23157 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23157 | no |
| SF-2026-ARXIV-2605-23158 | arXiv:2605.23158v1 | paper-v1:2605.23158 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23158 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23158 | no |
| SF-2026-ARXIV-2605-23168 | arXiv:2605.23168v1 | paper-v1:2605.23168 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23168 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23168 | no |
| SF-2026-ARXIV-2605-23170 | arXiv:2605.23170v1 | paper-v1:2605.23170 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23170 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-23170 | no |
| SF-2026-ARXIV-2605-23196 | arXiv:2605.23196v1 | paper-v1:2605.23196 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23196 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23196 | no |
| SF-2026-ARXIV-2605-23200 | arXiv:2605.23200v1 | paper-v1:2605.23200 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23200 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23200 | no |
| SF-2026-ARXIV-2605-23215 | arXiv:2605.23215v1 | paper-v1:2605.23215 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23215 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23215 | no |
| SF-2026-ARXIV-2605-23218 | arXiv:2605.23218v1 | paper-v1:2605.23218 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23218 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23218 | no |
| SF-2026-ARXIV-2605-23220 | arXiv:2605.23220v1 | paper-v1:2605.23220 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23220 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23220 | no |
| SF-2026-ARXIV-2605-23258 | arXiv:2605.23258v1 | paper-v1:2605.23258 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23258 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23258 | no |
| SF-2026-ARXIV-2605-23262 | arXiv:2605.23262v1 | paper-v1:2605.23262 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23262 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23262 | no |
| SF-2026-ARXIV-2605-23294 | arXiv:2605.23294v1 | paper-v1:2605.23294 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23294 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23294 | no |
| SF-2026-ARXIV-2605-23296 | arXiv:2605.23296v1 | paper-v1:2605.23296 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23296 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-23296 | no |
| SF-2026-ARXIV-2605-23311 | arXiv:2605.23311v1 | paper-v1:2605.23311 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23311 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23311 | no |
| SF-2026-ARXIV-2605-23348 | arXiv:2605.23348v1 | paper-v1:2605.23348 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23348 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23348 | no |
| SF-2026-ARXIV-2605-23362 | arXiv:2605.23362v1 | paper-v1:2605.23362 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23362 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23362 | no |
| SF-2026-ARXIV-2605-23389 | arXiv:2605.23389v1 | paper-v1:2605.23389 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23389 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2605-23389 | no |
| SF-2026-ARXIV-2605-23414 | arXiv:2605.23414v1 | paper-v1:2605.23414 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23414 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23414 | no |
| SF-2026-ARXIV-2605-23454 | arXiv:2605.23454v1 | paper-v1:2605.23454 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23454 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23454 | no |
| SF-2026-ARXIV-2605-23464 | arXiv:2605.23464v1 | paper-v1:2605.23464 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23464 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2605-23464 | no |
| SF-2026-ARXIV-2605-23493 | arXiv:2605.23493v1 | paper-v1:2605.23493 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23493 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23493 | no |
| SF-2026-ARXIV-2605-23574 | arXiv:2605.23574v1 | paper-v1:2605.23574 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23574 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23574 | no |
| SF-2026-ARXIV-2605-23590 | arXiv:2605.23590v1 | paper-v1:2605.23590 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23590 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23590 | no |
| SF-2026-ARXIV-2605-23628 | arXiv:2605.23628v1 | paper-v1:2605.23628 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23628 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23628 | no |
| SF-2026-ARXIV-2605-23640 | arXiv:2605.23640v1 | paper-v1:2605.23640 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23640 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23640 | no |
| SF-2026-ARXIV-2605-23657 | arXiv:2605.23657v1 | paper-v1:2605.23657 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23657 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23657 | no |
| SF-2026-ARXIV-2605-23701 | arXiv:2605.23701v1 | paper-v1:2605.23701 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23701 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23701 | no |
| SF-2026-ARXIV-2605-23723 | arXiv:2605.23723v1 | paper-v1:2605.23723 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23723 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23723 | no |
| SF-2026-ARXIV-2605-23764 | arXiv:2605.23764v1 | paper-v1:2605.23764 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23764 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23764 | no |
| SF-2026-ARXIV-2605-23856 | arXiv:2605.23856v1 | paper-v1:2605.23856 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23856 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23856 | no |
| SF-2026-ARXIV-2605-23893 | arXiv:2605.23893v1 | paper-v1:2605.23893 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-23893 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2605-23893 | no |
| SF-2026-ARXIV-2605-23899 | arXiv:2605.23899v1 | paper-v1:2605.23899 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23899 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23899 | no |
| SF-2026-ARXIV-2605-23904 | arXiv:2605.23904v1 | paper-v1:2605.23904 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-23904 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23904 | no |
| SF-2026-ARXIV-2605-24060 | arXiv:2605.24060v1 | paper-v1:2605.24060 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24060 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24060 | no |
| SF-2026-ARXIV-2605-24069 | arXiv:2605.24069v1 | paper-v1:2605.24069 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24069 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24069 | no |
| SF-2026-ARXIV-2605-24117 | arXiv:2605.24117v1 | paper-v1:2605.24117 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24117 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24117 | no |
| SF-2026-ARXIV-2605-24134 | arXiv:2605.24134v1 | paper-v1:2605.24134 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24134 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24134 | no |
| SF-2026-ARXIV-2605-24154 | arXiv:2605.24154v1 | paper-v1:2605.24154 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24154 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24154 | no |
| SF-2026-ARXIV-2605-24168 | arXiv:2605.24168v1 | paper-v1:2605.24168 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24168 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24168 | no |
| SF-2026-ARXIV-2605-24183 | arXiv:2605.24183v1 | paper-v1:2605.24183 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24183 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24183 | no |
| SF-2026-ARXIV-2605-24197 | arXiv:2605.24197v1 | paper-v1:2605.24197 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24197 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24197 | no |
| SF-2026-ARXIV-2605-24202 | arXiv:2605.24202v1 | paper-v1:2605.24202 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24202 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24202 | no |
| SF-2026-ARXIV-2605-24213 | arXiv:2605.24213v1 | paper-v1:2605.24213 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24213 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24213 | no |
| SF-2026-ARXIV-2605-24216 | arXiv:2605.24216v1 | paper-v1:2605.24216 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24216 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24216 | no |
| SF-2026-ARXIV-2605-24217 | arXiv:2605.24217v1 | paper-v1:2605.24217 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24217 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24217 | no |
| SF-2026-ARXIV-2605-24219 | arXiv:2605.24219v1 | paper-v1:2605.24219 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24219 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24219 | no |
| SF-2026-ARXIV-2605-24220 | arXiv:2605.24220v1 | paper-v1:2605.24220 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24220 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24220 | no |
| SF-2026-ARXIV-2605-24229 | arXiv:2605.24229v1 | paper-v1:2605.24229 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24229 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2605-24229 | no |
| SF-2026-ARXIV-2605-24245 | arXiv:2605.24245v1 | paper-v1:2605.24245 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24245 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24245 | no |
| SF-2026-ARXIV-2605-24247 | arXiv:2605.24247v1 | paper-v1:2605.24247 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24247 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24247 | no |
| SF-2026-ARXIV-2605-24248 | arXiv:2605.24248v1 | paper-v1:2605.24248 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24248 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2605-24248 | no |
| SF-2026-ARXIV-2605-24259 | arXiv:2605.24259v1 | paper-v1:2605.24259 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24259 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2605-24259 | no |
| SF-2026-ARXIV-2605-24279 | arXiv:2605.24279v1 | paper-v1:2605.24279 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24279 | self | — | new_in_window | AGENT-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2605-24279 | no |
| SF-2026-ARXIV-2605-24286 | arXiv:2605.24286v1 | paper-v1:2605.24286 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24286 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24286 | no |
| SF-2026-ARXIV-2605-24299 | arXiv:2605.24299v1 | paper-v1:2605.24299 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24299 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24299 | no |
| SF-2026-ARXIV-2605-24309 | arXiv:2605.24309v1 | paper-v1:2605.24309 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-24309 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24309 | no |
| SF-2026-ARXIV-2605-24312 | arXiv:2605.24312v1 | paper-v1:2605.24312 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2605-24312 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2605-24312 | no |
| SF-2026-ARXIV-2605-26147 | arXiv:2605.26147v1 | paper-v1:2605.26147 | 2026-W21 | 2026-05-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-26147 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26147 | no |
| SF-2026-ARXIV-2605-27432 | arXiv:2605.27432v1 | paper-v1:2605.27432 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27432 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27432 | no |
| SF-2026-ARXIV-2605-27435 | arXiv:2605.27435v1 | paper-v1:2605.27435 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27435 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27435 | no |
| SF-2026-ARXIV-2605-27437 | arXiv:2605.27437v1 | paper-v1:2605.27437 | 2026-W21 | 2026-05-22 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2605-27437 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27437 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23157 | RP-a5e7eb75c98b990e | deep | arXiv:2605.23157v1 | SRC-ARXIV@arXiv:2605.23157v1 | https://arxiv.org/html/2605.23157v1 — §3 Study Design; §3.1–§3.4 language × modality threat matrix | https://arxiv.org/html/2605.23157v1 — §4 Results; mixed-effects and matched-annotator evaluation | https://arxiv.org/html/2605.23157v1 — §7 Limitations; four-model/two-language scope | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23157 | complete |
| SF-2026-ARXIV-2605-23158 | RP-b2c602abcd2fe586 | deep | arXiv:2605.23158v1 | SRC-ARXIV@arXiv:2605.23158v1 | https://arxiv.org/html/2605.23158v1 — §3 Split Inference Protocol; §4.1–§4.2 Threat Model and ActInv | https://arxiv.org/html/2605.23158v1 — §4.3–§4.4 Evaluation | https://arxiv.org/html/2605.23158v1 — §5.3 Potential Defenses and split-point boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23158 | complete |
| SF-2026-ARXIV-2605-23168 | RP-2c31431371f1ac81 | deep | arXiv:2605.23168v1 | SRC-ARXIV@arXiv:2605.23168v1 | https://arxiv.org/html/2605.23168v1 — §3 PoisonForge threat model and parameterized benchmark | https://arxiv.org/html/2605.23168v1 — §4–§5 twelve-model poisoning evaluation | https://arxiv.org/html/2605.23168v1 — §6 Limitations; instruction-tuning and tested poison-budget boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23168 | complete |
| SF-2026-ARXIV-2605-23170 | RP-5d3695102d13073c | deep | arXiv:2605.23170v1 | SRC-ARXIV@arXiv:2605.23170v1 | https://arxiv.org/html/2605.23170v1 — §3 Context Rot Evaluation; controlled position/content/length factors | https://arxiv.org/html/2605.23170v1 — §4 Evaluation across nine models and two reasoning tasks | https://arxiv.org/html/2605.23170v1 — §7 Limitations; benchmark/task/context-family boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23170 | complete |
| SF-2026-ARXIV-2605-23196 | RP-b858c1b78baceb05 | deep | arXiv:2605.23196v1 | SRC-ARXIV@arXiv:2605.23196v1 | https://arxiv.org/html/2605.23196v1 — §3 Prompt-Overflow Threat Model | https://arxiv.org/html/2605.23196v1 — §4 Guardrail/Model Evaluation | https://arxiv.org/html/2605.23196v1 — §5 Discussion and tokenizer/context-boundary limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23196 | complete |
| SF-2026-ARXIV-2605-23200 | RP-da06ef546f54d6ce | deep | arXiv:2605.23200v1 | SRC-ARXIV@arXiv:2605.23200v1 | https://arxiv.org/html/2605.23200v1 — §3 Adaptive Mass-Segmented KV Compression | https://arxiv.org/html/2605.23200v1 — §4 Long-Form Reasoning Evaluation | https://arxiv.org/html/2605.23200v1 — §5 Conclusion and evaluated-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23200 | complete |
| SF-2026-ARXIV-2605-23215 | RP-cb8c0cd9246d1439 | deep | arXiv:2605.23215v1 | SRC-ARXIV@arXiv:2605.23215v1 | https://arxiv.org/html/2605.23215v1 — §3 FastKernels Production Benchmark Contract | https://arxiv.org/html/2605.23215v1 — §5 Kernel-Generation Evaluation | https://arxiv.org/html/2605.23215v1 — §6 Discussion and production-workload coverage limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23215 | complete |
| SF-2026-ARXIV-2605-23218 | RP-0b7b32429b301d1e | deep | arXiv:2605.23218v1 | SRC-ARXIV@arXiv:2605.23218v1 | https://arxiv.org/html/2605.23218v1 — §3 Foundation Protocol Coordination Layer | https://arxiv.org/html/2605.23218v1 — §5 Multi-Agent Evaluation | https://arxiv.org/html/2605.23218v1 — §6 Limitations and governance-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23218 | complete |
| SF-2026-ARXIV-2605-23220 | RP-3fd9d54eb7ed1280 | deep | arXiv:2605.23220v1 | SRC-ARXIV@arXiv:2605.23220v1 | https://arxiv.org/html/2605.23220v1 — §3 WMAttack Automated Attack Search | https://arxiv.org/html/2605.23220v1 — §4 World-Model Agent Evaluation | https://arxiv.org/html/2605.23220v1 — §5 Limitations and tested-environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23220 | complete |
| SF-2026-ARXIV-2605-23258 | RP-7e8ee0e18e9fbabb | deep | arXiv:2605.23258v1 | SRC-ARXIV@arXiv:2605.23258v1 | https://arxiv.org/html/2605.23258v1 — §3 Eviction-Aware KV Compression Plug-in | https://arxiv.org/html/2605.23258v1 — §4 Evaluation | https://arxiv.org/html/2605.23258v1 — §5 Conclusion and eviction-policy boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23258 | complete |
| SF-2026-ARXIV-2605-23262 | RP-fed5c51d38199cf0 | deep | arXiv:2605.23262v1 | SRC-ARXIV@arXiv:2605.23262v1 | https://arxiv.org/html/2605.23262v1 — §2–§4 work-centered benchmark representation | https://arxiv.org/html/2605.23262v1 — §5 worked benchmark comparisons | https://arxiv.org/html/2605.23262v1 — §6 Discussion; conceptual representation does not prove predictive validity | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23262 | complete |
| SF-2026-ARXIV-2605-23294 | RP-6dde5b87016a8054 | deep | arXiv:2605.23294v1 | SRC-ARXIV@arXiv:2605.23294v1 | https://arxiv.org/html/2605.23294v1 — §III NASiC CAM-selected multibit CIM architecture | https://arxiv.org/html/2605.23294v1 — §IV–§V architecture/model evaluation | https://arxiv.org/html/2605.23294v1 — §VI Discussion; simulated 3D-NAND/device-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23294 | complete |
| SF-2026-ARXIV-2605-23296 | RP-425574fcac35b682 | deep | arXiv:2605.23296v1 | SRC-ARXIV@arXiv:2605.23296v1 | https://arxiv.org/html/2605.23296v1 — §3 Parallel Context Compaction Runtime | https://arxiv.org/html/2605.23296v1 — §5 Long-Horizon Agent-Serving Evaluation | https://arxiv.org/html/2605.23296v1 — §6 Discussion and compaction-fidelity boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23296 | complete |
| SF-2026-ARXIV-2605-23311 | RP-6362c6ec2344c81d | deep | arXiv:2605.23311v1 | SRC-ARXIV@arXiv:2605.23311v1 | https://arxiv.org/html/2605.23311v1 — §3 DART Semantic-Recoverability Contract | https://arxiv.org/html/2605.23311v1 — §5 Structured-Tool Agent Evaluation | https://arxiv.org/html/2605.23311v1 — §6 Limitations and tool-schema boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23311 | complete |
| SF-2026-ARXIV-2605-23348 | RP-d67c7fcd55d6e402 | deep | arXiv:2605.23348v1 | SRC-ARXIV@arXiv:2605.23348v1 | https://arxiv.org/html/2605.23348v1 — §3 XWind Cross-Site Routing Controller | https://arxiv.org/html/2605.23348v1 — §5 Renewable-Site Serving Evaluation | https://arxiv.org/html/2605.23348v1 — §6 Limitations and forecast/topology boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23348 | complete |
| SF-2026-ARXIV-2605-23362 | RP-3286bf917956c518 | deep | arXiv:2605.23362v1 | SRC-ARXIV@arXiv:2605.23362v1 | https://arxiv.org/html/2605.23362v1 — §2–§4 budgeted heteroskedastic multi-judge estimation | https://arxiv.org/html/2605.23362v1 — §5 theory and empirical allocation evaluation | https://arxiv.org/html/2605.23362v1 — §6 Discussion; known-cost/bounded-score assumptions | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23362 | complete |
| SF-2026-ARXIV-2605-23389 | RP-d31f7b43f0ecb7ff | deep | arXiv:2605.23389v1 | SRC-ARXIV@arXiv:2605.23389v1 | https://arxiv.org/html/2605.23389v1 — §3 AlignedServe Prefix-Aware Batching | https://arxiv.org/html/2605.23389v1 — §5 Throughput/Compute Evaluation | https://arxiv.org/html/2605.23389v1 — §6 Conclusion and workload boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23389 | complete |
| SF-2026-ARXIV-2605-23414 | RP-550125b9681b344c | deep | arXiv:2605.23414v1 | SRC-ARXIV@arXiv:2605.23414v1 | https://arxiv.org/html/2605.23414v1 — §3 Epistemic-Calibration Model for Multi-Agent Planning | https://arxiv.org/html/2605.23414v1 — §4 Evaluation | https://arxiv.org/html/2605.23414v1 — §5 Limitations and planning/execution boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23414 | complete |
| SF-2026-ARXIV-2605-23454 | RP-0507968efac4b381 | deep | arXiv:2605.23454v1 | SRC-ARXIV@arXiv:2605.23454v1 | https://arxiv.org/html/2605.23454v1 — §3 ARES automatic rubric synthesis and reward construction | https://arxiv.org/html/2605.23454v1 — §4 and Appendix F evaluation | https://arxiv.org/html/2605.23454v1 — Appendix A Limitations; generated-rubric correctness boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23454 | complete |
| SF-2026-ARXIV-2605-23464 | RP-192bc644aad84ff7 | deep | arXiv:2605.23464v1 | SRC-ARXIV@arXiv:2605.23464v1 | https://arxiv.org/html/2605.23464v1 — §3 Unextractable Protocol Model Construction | https://arxiv.org/html/2605.23464v1 — §5 Collaborative Training/Inference Evaluation | https://arxiv.org/html/2605.23464v1 — §6 Security Assumptions and protocol limitations | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23464 | complete |
| SF-2026-ARXIV-2605-23493 | RP-048d9637fe33d612 | deep | arXiv:2605.23493v1 | SRC-ARXIV@arXiv:2605.23493v1 | https://arxiv.org/html/2605.23493v1 — §3 EDGE-OPD evidence-guided on-policy distillation | https://arxiv.org/html/2605.23493v1 — §4–§5 experiments and diagnostics | https://arxiv.org/html/2605.23493v1 — Appendix A.10 Limitations; teacher/evidence/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23493 | complete |
| SF-2026-ARXIV-2605-23574 | RP-5c316d8181d387b2 | deep | arXiv:2605.23574v1 | SRC-ARXIV@arXiv:2605.23574v1 | https://arxiv.org/html/2605.23574v1 — §3 Quantitative Goal-Persistence Contract | https://arxiv.org/html/2605.23574v1 — §5 Long-Horizon Agent Evaluation | https://arxiv.org/html/2605.23574v1 — §6 Limitations and task-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23574 | complete |
| SF-2026-ARXIV-2605-23590 | RP-547a40f059f156d0 | deep | arXiv:2605.23590v1 | SRC-ARXIV@arXiv:2605.23590v1 | https://arxiv.org/html/2605.23590v1 — §2–§3 Co-ReAct step-level rubric and control loop | https://arxiv.org/html/2605.23590v1 — §4–§5 agent evaluation | https://arxiv.org/html/2605.23590v1 — §6 Limitations; rubric and environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23590 | complete |
| SF-2026-ARXIV-2605-23628 | RP-1523ed940f94db13 | deep | arXiv:2605.23628v1 | SRC-ARXIV@arXiv:2605.23628v1 | https://arxiv.org/html/2605.23628v1 — §3 Social-Choice Leaderboard Model | https://arxiv.org/html/2605.23628v1 — §4 Benchmark-Rigging Analysis | https://arxiv.org/html/2605.23628v1 — §5 Discussion and scoring-rule assumptions | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23628 | complete |
| SF-2026-ARXIV-2605-23640 | RP-b9d297fc63bc2e63 | deep | arXiv:2605.23640v1 | SRC-ARXIV@arXiv:2605.23640v1 | https://arxiv.org/html/2605.23640v1 — §3 CachePrune Privacy-Aware KV Sharing | https://arxiv.org/html/2605.23640v1 — §5 Efficiency/Leakage Evaluation | https://arxiv.org/html/2605.23640v1 — §6 Limitations and attacker/model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23640 | complete |
| SF-2026-ARXIV-2605-23657 | RP-6ec64a2c7768b800 | deep | arXiv:2605.23657v1 | SRC-ARXIV@arXiv:2605.23657v1 | https://arxiv.org/html/2605.23657v1 — §3 OpenSkillEval Audit Pipeline | https://arxiv.org/html/2605.23657v1 — §4 Open-Skill Ecosystem Evaluation | https://arxiv.org/html/2605.23657v1 — §5 Limitations and registry-coverage boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23657 | complete |
| SF-2026-ARXIV-2605-23701 | RP-76760412a47fb37e | deep | arXiv:2605.23701v1 | SRC-ARXIV@arXiv:2605.23701v1 | https://arxiv.org/html/2605.23701v1 — §3 Intervention-Based Weak-Label Audit | https://arxiv.org/html/2605.23701v1 — §4 Controlled Evaluation | https://arxiv.org/html/2605.23701v1 — §5 Discussion and intervention-identifiability limits | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23701 | complete |
| SF-2026-ARXIV-2605-23723 | RP-6b7ff0f74ca2d717 | deep | arXiv:2605.23723v1 | SRC-ARXIV@arXiv:2605.23723v1 | https://arxiv.org/html/2605.23723v1 — §3 MemAudit Causal/Structural Audit | https://arxiv.org/html/2605.23723v1 — §5 Poisoned-Memory Evaluation | https://arxiv.org/html/2605.23723v1 — §6 Limitations and post-hoc-detection boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23723 | complete |
| SF-2026-ARXIV-2605-23764 | RP-613534380557f522 | deep | arXiv:2605.23764v1 | SRC-ARXIV@arXiv:2605.23764v1 | https://arxiv.org/html/2605.23764v1 — §3 HyperParallel-MoE Interleaved Scheduling | https://arxiv.org/html/2605.23764v1 — §5 Ascend-NPU Training Evaluation | https://arxiv.org/html/2605.23764v1 — §6 Conclusion and hardware/topology boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23764 | complete |
| SF-2026-ARXIV-2605-23856 | RP-63fb361e8b1290df | deep | arXiv:2605.23856v1 | SRC-ARXIV@arXiv:2605.23856v1 | https://arxiv.org/html/2605.23856v1 — §3 Point-Tracking World-Action Model | https://arxiv.org/html/2605.23856v1 — §4 Evaluation | https://arxiv.org/html/2605.23856v1 — §5 Limitations and observed-environment boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23856 | complete |
| SF-2026-ARXIV-2605-23893 | RP-ff7583edfd2016e5 | deep | arXiv:2605.23893v1 | SRC-ARXIV@arXiv:2605.23893v1 | https://arxiv.org/html/2605.23893v1 — §3 Complete-μE MoE Parameterization | https://arxiv.org/html/2605.23893v1 — §5 Hyperparameter-Transfer/Scaling Evaluation | https://arxiv.org/html/2605.23893v1 — §6 Limitations and tested-scale boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23893 | complete |
| SF-2026-ARXIV-2605-23899 | RP-3e95e4e8b2a46779 | deep | arXiv:2605.23899v1 | SRC-ARXIV@arXiv:2605.23899v1 | https://arxiv.org/html/2605.23899v1 — §3 Model-Generated Skill Pipeline | https://arxiv.org/html/2605.23899v1 — §4 Skill-Use Evaluation | https://arxiv.org/html/2605.23899v1 — §5 Limitations and model/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23899 | complete |
| SF-2026-ARXIV-2605-23904 | RP-557190908b08e8d0 | deep | arXiv:2605.23904v1 | SRC-ARXIV@arXiv:2605.23904v1 | https://arxiv.org/html/2605.23904v1 — §3 SkillOpt Executive Strategy | https://arxiv.org/html/2605.23904v1 — §5 Self-Evolving Agent Evaluation | https://arxiv.org/html/2605.23904v1 — §6 Limitations and library-drift boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-23904 | complete |
| SF-2026-ARXIV-2605-24060 | RP-53ca81da553bf549 | deep | arXiv:2605.24060v1 | SRC-ARXIV@arXiv:2605.24060v1 | https://arxiv.org/html/2605.24060v1 — §3 memory benchmark scoring-target intervention | https://arxiv.org/html/2605.24060v1 — §4–§5 controlled benchmark evaluation | https://arxiv.org/html/2605.24060v1 — §7 Limitations; tested-memory systems and tasks | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24060 | complete |
| SF-2026-ARXIV-2605-24069 | RP-edfc3e1a0860e2d4 | deep | arXiv:2605.24069v1 | SRC-ARXIV@arXiv:2605.24069v1 | https://arxiv.org/html/2605.24069v1 — §3 MCP Poisoning Threat Model and Benchmark | https://arxiv.org/html/2605.24069v1 — §4 Evaluation | https://arxiv.org/html/2605.24069v1 — §5 Limitations and manual/registry boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24069 | complete |
| SF-2026-ARXIV-2605-24117 | RP-1945ab82f7d8942d | deep | arXiv:2605.24117v1 | SRC-ARXIV@arXiv:2605.24117v1 | https://arxiv.org/html/2605.24117v1 — §3 SkillEvolBench lifecycle/evolution protocol | https://arxiv.org/html/2605.24117v1 — §4–§5 benchmark protocol and experiments | https://arxiv.org/html/2605.24117v1 — §6 Discussion; benchmark coverage does not prove deployment safety | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24117 | complete |
| SF-2026-ARXIV-2605-24134 | RP-e60e94ab77294bb7 | deep | arXiv:2605.24134v1 | SRC-ARXIV@arXiv:2605.24134v1 | https://arxiv.org/html/2605.24134v1 — §3 ProofAgent Harness Architecture | https://arxiv.org/html/2605.24134v1 — §5 Adversarial Agent Evaluation | https://arxiv.org/html/2605.24134v1 — §6 Limitations and proof-domain boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24134 | complete |
| SF-2026-ARXIV-2605-24154 | RP-e0c811bb34fd8177 | deep | arXiv:2605.24154v1 | SRC-ARXIV@arXiv:2605.24154v1 | https://arxiv.org/html/2605.24154v1 — §3 Palette Authorized Safety-Relaxation Modules | https://arxiv.org/html/2605.24154v1 — §5 Safety/Utility Evaluation | https://arxiv.org/html/2605.24154v1 — §6 Limitations and authorization boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24154 | complete |
| SF-2026-ARXIV-2605-24168 | RP-7d918c661cf20669 | deep | arXiv:2605.24168v1 | SRC-ARXIV@arXiv:2605.24168v1 | https://arxiv.org/html/2605.24168v1 — §3 Inference-Time Context-Sparsity Analysis | https://arxiv.org/html/2605.24168v1 — §4 Evaluation | https://arxiv.org/html/2605.24168v1 — §5 Discussion and model/task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24168 | complete |
| SF-2026-ARXIV-2605-24183 | RP-c3fa6cd87b633384 | deep | arXiv:2605.24183v1 | SRC-ARXIV@arXiv:2605.24183v1 | https://arxiv.org/html/2605.24183v1 — §2–§3 AvalancheBench latent-world recovery protocol | https://arxiv.org/html/2605.24183v1 — §4 early experiments | https://arxiv.org/html/2605.24183v1 — §5 Limitations; synthetic/latent-world scope | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24183 | complete |
| SF-2026-ARXIV-2605-24197 | RP-7014a32fa7fb0410 | deep | arXiv:2605.24197v1 | SRC-ARXIV@arXiv:2605.24197v1 | https://arxiv.org/html/2605.24197v1 — §3 formulation; §4 evidence-attribution mechanism | https://arxiv.org/html/2605.24197v1 — §5 experiments | https://arxiv.org/html/2605.24197v1 — Appendix B Limitations; simulated-agent and attribution boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24197 | complete |
| SF-2026-ARXIV-2605-24202 | RP-4930f30a517dca9e | deep | arXiv:2605.24202v1 | SRC-ARXIV@arXiv:2605.24202v1 | https://arxiv.org/html/2605.24202v1 — §3 multi-agent RL workflow and policy-sharing mechanism | https://arxiv.org/html/2605.24202v1 — §4 experiments | https://arxiv.org/html/2605.24202v1 — §5 Discussion; policy-sharing topology and task boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24202 | complete |
| SF-2026-ARXIV-2605-24213 | RP-560b2532606bbdda | deep | arXiv:2605.24213v1 | SRC-ARXIV@arXiv:2605.24213v1 | https://arxiv.org/html/2605.24213v1 — §3 Evaluation-Harness Measurement Method | https://arxiv.org/html/2605.24213v1 — §5 Empirical Harness Study | https://arxiv.org/html/2605.24213v1 — §6 Threats to Validity | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24213 | complete |
| SF-2026-ARXIV-2605-24216 | RP-077abf5941d8963d | deep | arXiv:2605.24216v1 | SRC-ARXIV@arXiv:2605.24216v1 | https://arxiv.org/html/2605.24216v1 — §3 Agent-ToM learning-to-monitor architecture | https://arxiv.org/html/2605.24216v1 — §4–§5 monitoring evaluation | https://arxiv.org/html/2605.24216v1 — §6 Limitations; ToM inference is a sensor, not intent ground truth | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24216 | complete |
| SF-2026-ARXIV-2605-24217 | RP-83b7fc2b50acda2c | deep | arXiv:2605.24217v1 | SRC-ARXIV@arXiv:2605.24217v1 | https://arxiv.org/html/2605.24217v1 — §3 Production-Inference Measurement-Bias Model | https://arxiv.org/html/2605.24217v1 — §4 Benchmark Evaluation | https://arxiv.org/html/2605.24217v1 — §5 Mitigation and production-scope boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24217 | complete |
| SF-2026-ARXIV-2605-24219 | RP-cb6de191d8d1a25b | deep | arXiv:2605.24219v1 | SRC-ARXIV@arXiv:2605.24219v1 | https://arxiv.org/html/2605.24219v1 — §3 Trajectory-Level Hallucination Audit | https://arxiv.org/html/2605.24219v1 — §5 Multi-Agent Workflow Evaluation | https://arxiv.org/html/2605.24219v1 — §6 Limitations and industrial-workflow boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24219 | complete |
| SF-2026-ARXIV-2605-24220 | RP-e1e6b29bd447f830 | deep | arXiv:2605.24220v1 | SRC-ARXIV@arXiv:2605.24220v1 | https://arxiv.org/html/2605.24220v1 — §3 Polar Harness-Agnostic Agentic-RL Runtime | https://arxiv.org/html/2605.24220v1 — §5 Scale Evaluation | https://arxiv.org/html/2605.24220v1 — §6 Limitations and harness/reward boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24220 | complete |
| SF-2026-ARXIV-2605-24229 | RP-95b9d6a655c9ba1b | deep | arXiv:2605.24229v1 | SRC-ARXIV@arXiv:2605.24229v1 | https://arxiv.org/html/2605.24229v1 — §3 atomic-tenet extraction and adversarial audit pipeline | https://arxiv.org/html/2605.24229v1 — §4–§5 multi-turn constitution-adherence evaluation | https://arxiv.org/html/2605.24229v1 — §6 Limitations; published-spec and evaluator boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24229 | complete |
| SF-2026-ARXIV-2605-24245 | RP-d9a0c3a52f264bbf | deep | arXiv:2605.24245v1 | SRC-ARXIV@arXiv:2605.24245v1 | https://arxiv.org/html/2605.24245v1 — §3 User-Generated-Content Poisoning Attack | https://arxiv.org/html/2605.24245v1 — §5 Deep-Research Agent Evaluation | https://arxiv.org/html/2605.24245v1 — §6 Limitations and source/ecosystem boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24245 | complete |
| SF-2026-ARXIV-2605-24247 | RP-c6b27047965b1a2c | deep | arXiv:2605.24247v1 | SRC-ARXIV@arXiv:2605.24247v1 | https://arxiv.org/html/2605.24247v1 — §3 detailed constitutional definitions and AI-assisted labeling workflow | https://arxiv.org/html/2605.24247v1 — §4–§5 label-consistency evaluation | https://arxiv.org/html/2605.24247v1 — §6 Limitations; category/specification and annotator boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24247 | complete |
| SF-2026-ARXIV-2605-24248 | RP-3c1364836d648be2 | deep | arXiv:2605.24248v1 | SRC-ARXIV@arXiv:2605.24248v1 | https://arxiv.org/html/2605.24248v1 — §3 Attested Tool-Server Admission Protocol | https://arxiv.org/html/2605.24248v1 — §5 Security Evaluation | https://arxiv.org/html/2605.24248v1 — §6 Limitations and attestation-root boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24248 | complete |
| SF-2026-ARXIV-2605-24259 | RP-b6c8edc6414dc377 | deep | arXiv:2605.24259v1 | SRC-ARXIV@arXiv:2605.24259v1 | https://arxiv.org/html/2605.24259v1 — §3 Resident-KV Conformance Contract | https://arxiv.org/html/2605.24259v1 — §5 Active-Pressure Evaluation | https://arxiv.org/html/2605.24259v1 — §6 Limitations and cache-manager boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24259 | complete |
| SF-2026-ARXIV-2605-24279 | RP-8b8d5013744b9560 | deep | arXiv:2605.24279v1 | SRC-ARXIV@arXiv:2605.24279v1 | https://arxiv.org/html/2605.24279v1 — §3 ContextEcho snapshot-then-probe deployment harness | https://arxiv.org/html/2605.24279v1 — §4–§5 long agentic-coding session evaluation | https://arxiv.org/html/2605.24279v1 — §6 Limitations; persona probes and coding-session boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24279 | complete |
| SF-2026-ARXIV-2605-24286 | RP-84921df9be98938b | deep | arXiv:2605.24286v1 | SRC-ARXIV@arXiv:2605.24286v1 | https://arxiv.org/html/2605.24286v1 — §3 information-flow faithfulness criteria and diagnostics | https://arxiv.org/html/2605.24286v1 — §4–§5 faithfulness evaluation/training | https://arxiv.org/html/2605.24286v1 — §6 Limitations; diagnostic proxies do not reveal hidden computation | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24286 | complete |
| SF-2026-ARXIV-2605-24299 | RP-724533acc435b3a4 | deep | arXiv:2605.24299v1 | SRC-ARXIV@arXiv:2605.24299v1 | https://arxiv.org/html/2605.24299v1 — §3 factor-analysis decomposition of elicited confidence | https://arxiv.org/html/2605.24299v1 — §4 pairwise calibration across twenty models/six benchmarks | https://arxiv.org/html/2605.24299v1 — §5–§6 Limitations; elicited-confidence and tested-benchmark boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24299 | complete |
| SF-2026-ARXIV-2605-24309 | RP-e7e9cb98a7e9408c | deep | arXiv:2605.24309v1 | SRC-ARXIV@arXiv:2605.24309v1 | https://arxiv.org/html/2605.24309v1 — §3 agent-human security mechanism taxonomy | https://arxiv.org/html/2605.24309v1 — §4 audit of papers, production agents and plugins | https://arxiv.org/html/2605.24309v1 — §5 Limitations; observational taxonomy does not prove mechanism efficacy | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24309 | complete |
| SF-2026-ARXIV-2605-24312 | RP-2668bfa075d3ed92 | deep | arXiv:2605.24312v1 | SRC-ARXIV@arXiv:2605.24312v1 | https://arxiv.org/html/2605.24312v1 — §3 Entailment-Based RAG Membership Inference | https://arxiv.org/html/2605.24312v1 — §4 Five-Query Evaluation | https://arxiv.org/html/2605.24312v1 — §5 Limitations and black-box-access boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-24312 | complete |
| SF-2026-ARXIV-2605-26147 | RP-34f654f3eebfbbf7 | deep | arXiv:2605.26147v1 | SRC-ARXIV@arXiv:2605.26147v1 | https://arxiv.org/html/2605.26147v1 — §3–§5 DAG evidence accumulation and sequential routing | https://arxiv.org/html/2605.26147v1 — §6–§8 controlled experiments and ablations | https://arxiv.org/html/2605.26147v1 — §9 Discussion; conjugate-belief assumptions and tested-model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-26147 | complete |
| SF-2026-ARXIV-2605-27432 | RP-42cf134168eb2253 | deep | arXiv:2605.27432v1 | SRC-ARXIV@arXiv:2605.27432v1 | https://arxiv.org/html/2605.27432v1 — §4 federated dual-system retrieval and compact QA memory | https://arxiv.org/html/2605.27432v1 — §5 experiments | https://arxiv.org/html/2605.27432v1 — Appendix D privacy/cost analysis; no general privacy guarantee | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27432 | complete |
| SF-2026-ARXIV-2605-27435 | RP-b64815f80025c282 | deep | arXiv:2605.27435v1 | SRC-ARXIV@arXiv:2605.27435v1 | https://arxiv.org/html/2605.27435v1 — §3 Stage-Level Mobile LLM Method | https://arxiv.org/html/2605.27435v1 — §4 CPU/GPU/NPU Evaluation | https://arxiv.org/html/2605.27435v1 — §5 Discussion and device/model boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27435 | complete |
| SF-2026-ARXIV-2605-27437 | RP-a720725bcd86910c | deep | arXiv:2605.27437v1 | SRC-ARXIV@arXiv:2605.27437v1 | https://arxiv.org/html/2605.27437v1 — §3 memory-guided reflective retrieval | https://arxiv.org/html/2605.27437v1 — §4 long-dialogue experiments | https://arxiv.org/html/2605.27437v1 — §5 Discussion; tested-memory/task and extra-latency boundary | Not Disclosed — exact-v1 paper does not disclose a separate immutable artifact required for this review | claim:SF-2026-ARXIV-2605-27437 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2605-23157:start -->
#### Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs

**问题与机制。** We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Study Design; §3.1–§3.4 language × modality threat matrix`；Evaluation=`§4 Results; mixed-effects and matched-annotator evaluation`；Limitations/Counterevidence=`§7 Limitations; four-model/two-language scope`。

<!-- claim:SF-2026-ARXIV-2605-23157:start -->Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23157:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23157:end -->

<!-- review:SF-2026-ARXIV-2605-23158:start -->
#### What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference

**问题与机制。** To fill this gap, we introduce ActInv, which solves an intermediate activation matching problem to reconstruct the client's input. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Split Inference Protocol; §4.1–§4.2 Threat Model and ActInv`；Evaluation=`§4.3–§4.4 Evaluation`；Limitations/Counterevidence=`§5.3 Potential Defenses and split-point boundary`。

<!-- claim:SF-2026-ARXIV-2605-23158:start -->What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23158:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23158:end -->

<!-- review:SF-2026-ARXIV-2605-23168:start -->
#### PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs

**问题与机制。** We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 PoisonForge threat model and parameterized benchmark`；Evaluation=`§4–§5 twelve-model poisoning evaluation`；Limitations/Counterevidence=`§6 Limitations; instruction-tuning and tested poison-budget boundary`。

<!-- claim:SF-2026-ARXIV-2605-23168:start -->PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23168:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23168:end -->

<!-- review:SF-2026-ARXIV-2605-23170:start -->
#### Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks

**问题与机制。** We propose Context Rot Evaluation (CRE), a controlled framework varying all three factors, and evaluate nine LLMs on GSM8K and ARC-Challenge across two rounds: an initial five-model set and four newer vendor releases. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Context Rot Evaluation; controlled position/content/length factors`；Evaluation=`§4 Evaluation across nine models and two reasoning tasks`；Limitations/Counterevidence=`§7 Limitations; benchmark/task/context-family boundary`。

<!-- claim:SF-2026-ARXIV-2605-23170:start -->Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23170:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23170:end -->

<!-- review:SF-2026-ARXIV-2605-23196:start -->
#### Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers

**问题与机制。** In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Prompt-Overflow Threat Model`；Evaluation=`§4 Guardrail/Model Evaluation`；Limitations/Counterevidence=`§5 Discussion and tokenizer/context-boundary limits`。

<!-- claim:SF-2026-ARXIV-2605-23196:start -->Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23196:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23196:end -->

<!-- review:SF-2026-ARXIV-2605-23200:start -->
#### Adaptive Mass-Segmented KV Compression for Long-Context Reasoning

**问题与机制。** However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Adaptive Mass-Segmented KV Compression`；Evaluation=`§4 Long-Form Reasoning Evaluation`；Limitations/Counterevidence=`§5 Conclusion and evaluated-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23200:start -->Adaptive Mass-Segmented KV Compression for Long-Context Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23200:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23200:end -->

<!-- review:SF-2026-ARXIV-2605-23215:start -->
#### FastKernels: Benchmarking GPU Kernel Generation in Production

**问题与机制。** The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 FastKernels Production Benchmark Contract`；Evaluation=`§5 Kernel-Generation Evaluation`；Limitations/Counterevidence=`§6 Discussion and production-workload coverage limits`。

<!-- claim:SF-2026-ARXIV-2605-23215:start -->FastKernels: Benchmarking GPU Kernel Generation in Production only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23215:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23215:end -->

<!-- review:SF-2026-ARXIV-2605-23218:start -->
#### Foundation Protocol: A Coordination Layer for Agentic Society

**问题与机制。** Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Foundation Protocol Coordination Layer`；Evaluation=`§5 Multi-Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and governance-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-23218:start -->Foundation Protocol: A Coordination Layer for Agentic Society only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23218:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23218:end -->

<!-- review:SF-2026-ARXIV-2605-23220:start -->
#### WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents

**问题与机制。** We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 WMAttack Automated Attack Search`；Evaluation=`§4 World-Model Agent Evaluation`；Limitations/Counterevidence=`§5 Limitations and tested-environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23220:start -->WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23220:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23220:end -->

<!-- review:SF-2026-ARXIV-2605-23258:start -->
#### A Simple Plug-in for Improving Eviction-Based KV Cache Compression

**问题与机制。** We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Eviction-Aware KV Compression Plug-in`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Conclusion and eviction-policy boundary`。

<!-- claim:SF-2026-ARXIV-2605-23258:start -->A Simple Plug-in for Improving Eviction-Based KV Cache Compression only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23258:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23258:end -->

<!-- review:SF-2026-ARXIV-2605-23262:start -->
#### Designing Benchmarks for Knowledge Work

**问题与机制。** We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§4 work-centered benchmark representation`；Evaluation=`§5 worked benchmark comparisons`；Limitations/Counterevidence=`§6 Discussion; conceptual representation does not prove predictive validity`。

<!-- claim:SF-2026-ARXIV-2605-23262:start -->Designing Benchmarks for Knowledge Work only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23262:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23262:end -->

<!-- review:SF-2026-ARXIV-2605-23294:start -->
#### NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference

**问题与机制。** With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference. owner=`INFER-TENSORRT-LLM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§III NASiC CAM-selected multibit CIM architecture`；Evaluation=`§IV–§V architecture/model evaluation`；Limitations/Counterevidence=`§VI Discussion; simulated 3D-NAND/device-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23294:start -->NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23294:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23294:end -->

<!-- review:SF-2026-ARXIV-2605-23296:start -->
#### Parallel Context Compaction for Long-Horizon LLM Agent Serving

**问题与机制。** We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Parallel Context Compaction Runtime`；Evaluation=`§5 Long-Horizon Agent-Serving Evaluation`；Limitations/Counterevidence=`§6 Discussion and compaction-fidelity boundary`。

<!-- claim:SF-2026-ARXIV-2605-23296:start -->Parallel Context Compaction for Long-Horizon LLM Agent Serving only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23296:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23296:end -->

<!-- review:SF-2026-ARXIV-2605-23311:start -->
#### DART: Semantic Recoverability for Structured Tool Agents

**问题与机制。** We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise. owner=`AGENT-TOOL-CALLING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 DART Semantic-Recoverability Contract`；Evaluation=`§5 Structured-Tool Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and tool-schema boundary`。

<!-- claim:SF-2026-ARXIV-2605-23311:start -->DART: Semantic Recoverability for Structured Tool Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23311:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23311:end -->

<!-- review:SF-2026-ARXIV-2605-23348:start -->
#### CWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms

**问题与机制。** AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up. owner=`INFER-SCHEDULING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 XWind Cross-Site Routing Controller`；Evaluation=`§5 Renewable-Site Serving Evaluation`；Limitations/Counterevidence=`§6 Limitations and forecast/topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-23348:start -->CWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23348:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23348:end -->

<!-- review:SF-2026-ARXIV-2605-23362:start -->
#### Instance-Optimal Estimation with Multiple LLM Judges on a Budget

**问题与机制。** We formalize this question as *budgeted heteroskedastic multi-judge estimation*. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§4 budgeted heteroskedastic multi-judge estimation`；Evaluation=`§5 theory and empirical allocation evaluation`；Limitations/Counterevidence=`§6 Discussion; known-cost/bounded-score assumptions`。

<!-- claim:SF-2026-ARXIV-2605-23362:start -->Instance-Optimal Estimation with Multiple LLM Judges on a Budget only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23362:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23362:end -->

<!-- review:SF-2026-ARXIV-2605-23389:start -->
#### AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System

**问题与机制。** We propose AlignedServe, an LLM serving framework built around prefix-aware batching. owner=`INFER-SCHEDULING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 AlignedServe Prefix-Aware Batching`；Evaluation=`§5 Throughput/Compute Evaluation`；Limitations/Counterevidence=`§6 Conclusion and workload boundary`。

<!-- claim:SF-2026-ARXIV-2605-23389:start -->AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23389:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23389:end -->

<!-- review:SF-2026-ARXIV-2605-23414:start -->
#### When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems

**问题与机制。** To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Epistemic-Calibration Model for Multi-Agent Planning`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and planning/execution boundary`。

<!-- claim:SF-2026-ARXIV-2605-23414:start -->When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23414:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23414:end -->

<!-- review:SF-2026-ARXIV-2605-23454:start -->
#### ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning

**问题与机制。** We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 ARES automatic rubric synthesis and reward construction`；Evaluation=`§4 and Appendix F evaluation`；Limitations/Counterevidence=`Appendix A Limitations; generated-rubric correctness boundary`。

<!-- claim:SF-2026-ARXIV-2605-23454:start -->ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23454:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23454:end -->

<!-- review:SF-2026-ARXIV-2605-23464:start -->
#### Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization

**问题与机制。** We introduce Unextractable Protocol Models (UPMs): a training and inference framework that leverages the sharded model setup to ensure model shards (i.e., subsets) held by participants are incompatible at different time steps. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Unextractable Protocol Model Construction`；Evaluation=`§5 Collaborative Training/Inference Evaluation`；Limitations/Counterevidence=`§6 Security Assumptions and protocol limitations`。

<!-- claim:SF-2026-ARXIV-2605-23464:start -->Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23464:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23464:end -->

<!-- review:SF-2026-ARXIV-2605-23493:start -->
#### EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation

**问题与机制。** In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 EDGE-OPD evidence-guided on-policy distillation`；Evaluation=`§4–§5 experiments and diagnostics`；Limitations/Counterevidence=`Appendix A.10 Limitations; teacher/evidence/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-23493:start -->EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23493:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23493:end -->

<!-- review:SF-2026-ARXIV-2605-23574:start -->
#### Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents

**问题与机制。** We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items. owner=`AGENT-WORKFLOW`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Quantitative Goal-Persistence Contract`；Evaluation=`§5 Long-Horizon Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and task-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-23574:start -->Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23574:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23574:end -->

<!-- review:SF-2026-ARXIV-2605-23590:start -->
#### Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents

**问题与机制。** We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference. owner=`AGENT-WORKFLOW`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§3 Co-ReAct step-level rubric and control loop`；Evaluation=`§4–§5 agent evaluation`；Limitations/Counterevidence=`§6 Limitations; rubric and environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23590:start -->Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23590:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23590:end -->

<!-- review:SF-2026-ARXIV-2605-23628:start -->
#### How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness

**问题与机制。** Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Social-Choice Leaderboard Model`；Evaluation=`§4 Benchmark-Rigging Analysis`；Limitations/Counterevidence=`§5 Discussion and scoring-rule assumptions`。

<!-- claim:SF-2026-ARXIV-2605-23628:start -->How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23628:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23628:end -->

<!-- review:SF-2026-ARXIV-2605-23640:start -->
#### CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference

**问题与机制。** Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 CachePrune Privacy-Aware KV Sharing`；Evaluation=`§5 Efficiency/Leakage Evaluation`；Limitations/Counterevidence=`§6 Limitations and attacker/model boundary`。

<!-- claim:SF-2026-ARXIV-2605-23640:start -->CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23640:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23640:end -->

<!-- review:SF-2026-ARXIV-2605-23657:start -->
#### OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents

**问题与机制。** In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 OpenSkillEval Audit Pipeline`；Evaluation=`§4 Open-Skill Ecosystem Evaluation`；Limitations/Counterevidence=`§5 Limitations and registry-coverage boundary`。

<!-- claim:SF-2026-ARXIV-2605-23657:start -->OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23657:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23657:end -->

<!-- review:SF-2026-ARXIV-2605-23701:start -->
#### Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks

**问题与机制。** We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Intervention-Based Weak-Label Audit`；Evaluation=`§4 Controlled Evaluation`；Limitations/Counterevidence=`§5 Discussion and intervention-identifiability limits`。

<!-- claim:SF-2026-ARXIV-2605-23701:start -->Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23701:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23701:end -->

<!-- review:SF-2026-ARXIV-2605-23723:start -->
#### MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection

**问题与机制。** We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. owner=`AGENT-MEMORY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 MemAudit Causal/Structural Audit`；Evaluation=`§5 Poisoned-Memory Evaluation`；Limitations/Counterevidence=`§6 Limitations and post-hoc-detection boundary`。

<!-- claim:SF-2026-ARXIV-2605-23723:start -->MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23723:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23723:end -->

<!-- review:SF-2026-ARXIV-2605-23764:start -->
#### HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs

**问题与机制。** Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training. owner=`TRAIN-DISTRIBUTED-TRAINING`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 HyperParallel-MoE Interleaved Scheduling`；Evaluation=`§5 Ascend-NPU Training Evaluation`；Limitations/Counterevidence=`§6 Conclusion and hardware/topology boundary`。

<!-- claim:SF-2026-ARXIV-2605-23764:start -->HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23764:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23764:end -->

<!-- review:SF-2026-ARXIV-2605-23856:start -->
#### Point Tracking Improves World Action Models

**问题与机制。** We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer. owner=`MULTIMODAL-WORLD-MODELS`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Point-Tracking World-Action Model`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and observed-environment boundary`。

<!-- claim:SF-2026-ARXIV-2605-23856:start -->Point Tracking Improves World Action Models only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23856:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23856:end -->

<!-- review:SF-2026-ARXIV-2605-23893:start -->
#### Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models

**问题与机制。** We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks. owner=`MODEL-MOE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Complete-μE MoE Parameterization`；Evaluation=`§5 Hyperparameter-Transfer/Scaling Evaluation`；Limitations/Counterevidence=`§6 Limitations and tested-scale boundary`。

<!-- claim:SF-2026-ARXIV-2605-23893:start -->Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23893:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23893:end -->

<!-- review:SF-2026-ARXIV-2605-23899:start -->
#### From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills

**问题与机制。** However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Model-Generated Skill Pipeline`；Evaluation=`§4 Skill-Use Evaluation`；Limitations/Counterevidence=`§5 Limitations and model/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-23899:start -->From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23899:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23899:end -->

<!-- review:SF-2026-ARXIV-2605-23904:start -->
#### SkillOpt: Executive Strategy for Self-Evolving Agent Skills

**问题与机制。** Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization. owner=`AGENT-PLATFORM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 SkillOpt Executive Strategy`；Evaluation=`§5 Self-Evolving Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and library-drift boundary`。

<!-- claim:SF-2026-ARXIV-2605-23904:start -->SkillOpt: Executive Strategy for Self-Evolving Agent Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-23904:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-23904:end -->

<!-- review:SF-2026-ARXIV-2605-24060:start -->
#### Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks

**问题与机制。** We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 memory benchmark scoring-target intervention`；Evaluation=`§4–§5 controlled benchmark evaluation`；Limitations/Counterevidence=`§7 Limitations; tested-memory systems and tasks`。

<!-- claim:SF-2026-ARXIV-2605-24060:start -->Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24060:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24060:end -->

<!-- review:SF-2026-ARXIV-2605-24069:start -->
#### When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents

**问题与机制。** To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark. owner=`AGENT-MCP`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 MCP Poisoning Threat Model and Benchmark`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Limitations and manual/registry boundary`。

<!-- claim:SF-2026-ARXIV-2605-24069:start -->When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24069:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24069:end -->

<!-- review:SF-2026-ARXIV-2605-24117:start -->
#### SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills

**问题与机制。** We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation. owner=`AGENT-PLATFORM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 SkillEvolBench lifecycle/evolution protocol`；Evaluation=`§4–§5 benchmark protocol and experiments`；Limitations/Counterevidence=`§6 Discussion; benchmark coverage does not prove deployment safety`。

<!-- claim:SF-2026-ARXIV-2605-24117:start -->SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24117:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24117:end -->

<!-- review:SF-2026-ARXIV-2605-24134:start -->
#### ProofAgent Harness: Open Infrastructure for Adversarial Evaluation of AI Agents

**问题与机制。** We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 ProofAgent Harness Architecture`；Evaluation=`§5 Adversarial Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and proof-domain boundary`。

<!-- claim:SF-2026-ARXIV-2605-24134:start -->ProofAgent Harness: Open Infrastructure for Adversarial Evaluation of AI Agents only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24134:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24134:end -->

<!-- review:SF-2026-ARXIV-2605-24154:start -->
#### Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs

**问题与机制。** To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Palette Authorized Safety-Relaxation Modules`；Evaluation=`§5 Safety/Utility Evaluation`；Limitations/Counterevidence=`§6 Limitations and authorization boundary`。

<!-- claim:SF-2026-ARXIV-2605-24154:start -->Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24154:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24154:end -->

<!-- review:SF-2026-ARXIV-2605-24168:start -->
#### Inference Time Context Sparsity: Illusion or Opportunity?

**问题与机制。** Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels. owner=`AGENT-CONTEXT`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Inference-Time Context-Sparsity Analysis`；Evaluation=`§4 Evaluation`；Limitations/Counterevidence=`§5 Discussion and model/task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24168:start -->Inference Time Context Sparsity: Illusion or Opportunity? only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24168:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24168:end -->

<!-- review:SF-2026-ARXIV-2605-24183:start -->
#### AvalancheBench: Evaluating Enterprise Data Agents Through Latent World Recovery

**问题与机制。** We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§2–§3 AvalancheBench latent-world recovery protocol`；Evaluation=`§4 early experiments`；Limitations/Counterevidence=`§5 Limitations; synthetic/latent-world scope`。

<!-- claim:SF-2026-ARXIV-2605-24183:start -->AvalancheBench: Evaluating Enterprise Data Agents Through Latent World Recovery only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24183:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24183:end -->

<!-- review:SF-2026-ARXIV-2605-24197:start -->
#### A Sober Look at Agentic Misalignment in Automated Workflows

**问题与机制。** We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment. owner=`AGENT-MULTI-AGENT`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 formulation; §4 evidence-attribution mechanism`；Evaluation=`§5 experiments`；Limitations/Counterevidence=`Appendix B Limitations; simulated-agent and attribution boundary`。

<!-- claim:SF-2026-ARXIV-2605-24197:start -->A Sober Look at Agentic Misalignment in Automated Workflows only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24197:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24197:end -->

<!-- review:SF-2026-ARXIV-2605-24202:start -->
#### When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs

**问题与机制。** We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters. owner=`TRAIN-RLHF`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 multi-agent RL workflow and policy-sharing mechanism`；Evaluation=`§4 experiments`；Limitations/Counterevidence=`§5 Discussion; policy-sharing topology and task boundary`。

<!-- claim:SF-2026-ARXIV-2605-24202:start -->When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24202:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24202:end -->

<!-- review:SF-2026-ARXIV-2605-24213:start -->
#### Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild

**问题与机制。** We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Evaluation-Harness Measurement Method`；Evaluation=`§5 Empirical Harness Study`；Limitations/Counterevidence=`§6 Threats to Validity`。

<!-- claim:SF-2026-ARXIV-2605-24213:start -->Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24213:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24213:end -->

<!-- review:SF-2026-ARXIV-2605-24216:start -->
#### Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning

**问题与机制。** We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 Agent-ToM learning-to-monitor architecture`；Evaluation=`§4–§5 monitoring evaluation`；Limitations/Counterevidence=`§6 Limitations; ToM inference is a sensor, not intent ground truth`。

<!-- claim:SF-2026-ARXIV-2605-24216:start -->Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24216:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24216:end -->

<!-- review:SF-2026-ARXIV-2605-24217:start -->
#### Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks

**问题与机制。** We demonstrate that widely used benchmarking utilities rely on single-process, asyncio-driven architectures that introduce fundamental client-side queuing bottlenecks under high concurrency. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Production-Inference Measurement-Bias Model`；Evaluation=`§4 Benchmark Evaluation`；Limitations/Counterevidence=`§5 Mitigation and production-scope boundary`。

<!-- claim:SF-2026-ARXIV-2605-24217:start -->Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24217:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24217:end -->

<!-- review:SF-2026-ARXIV-2605-24219:start -->
#### Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows

**问题与机制。** We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Trajectory-Level Hallucination Audit`；Evaluation=`§5 Multi-Agent Workflow Evaluation`；Limitations/Counterevidence=`§6 Limitations and industrial-workflow boundary`。

<!-- claim:SF-2026-ARXIV-2605-24219:start -->Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24219:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24219:end -->

<!-- review:SF-2026-ARXIV-2605-24220:start -->
#### Polar: Agentic RL on Any Harness at Scale

**问题与机制。** This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads. owner=`TRAIN-RLHF`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Polar Harness-Agnostic Agentic-RL Runtime`；Evaluation=`§5 Scale Evaluation`；Limitations/Counterevidence=`§6 Limitations and harness/reward boundary`。

<!-- claim:SF-2026-ARXIV-2605-24220:start -->Polar: Agentic RL on Any Harness at Scale only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24220:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24220:end -->

<!-- review:SF-2026-ARXIV-2605-24229:start -->
#### How Well Do Models Follow Their Constitutions?

**问题与机制。** We propose a multi-method audit pipeline that treats each lab's published specification as an auditable target: it decomposes the specification into atomic testable tenets (205 for Anthropic, 197 for OpenAI), generates multi-turn adversarial scenarios with the Petri auditing agent (Anthropic, 2025b), runs a modified SURF-style rubric search (Murray et al., 2026) to catch shallow single-turn failures Petri misses, validates flagged transcripts against the relevant specification, and compares the findings against the lab's own published system card. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 atomic-tenet extraction and adversarial audit pipeline`；Evaluation=`§4–§5 multi-turn constitution-adherence evaluation`；Limitations/Counterevidence=`§6 Limitations; published-spec and evaluator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24229:start -->How Well Do Models Follow Their Constitutions? only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24229:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24229:end -->

<!-- review:SF-2026-ARXIV-2605-24245:start -->
#### Deep-Research Agents Can Be Poisoned via User-Generated Content

**问题与机制。** We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia. owner=`PLATFORM-SECURITY`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 User-Generated-Content Poisoning Attack`；Evaluation=`§5 Deep-Research Agent Evaluation`；Limitations/Counterevidence=`§6 Limitations and source/ecosystem boundary`。

<!-- claim:SF-2026-ARXIV-2605-24245:start -->Deep-Research Agents Can Be Poisoned via User-Generated Content only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24245:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24245:end -->

<!-- review:SF-2026-ARXIV-2605-24247:start -->
#### Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation

**问题与机制。** We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document. owner=`TRAIN-DATA`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 detailed constitutional definitions and AI-assisted labeling workflow`；Evaluation=`§4–§5 label-consistency evaluation`；Limitations/Counterevidence=`§6 Limitations; category/specification and annotator boundary`。

<!-- claim:SF-2026-ARXIV-2605-24247:start -->Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24247:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24247:end -->

<!-- review:SF-2026-ARXIV-2605-24248:start -->
#### Attested Tool-Server Admission: A Security Extension to the Model Context Protocol

**问题与机制。** We give the wire format, the verification algorithm, a security analysis, and an LLM-driven adversarial evaluation; we then state the design in normative Request-for-Comments (RFC 2119) form -- schema, verification rules, error registry, well-known registration, and machine-checkable conformance vectors -- so it can be adopted as an MCP addendum rather than reinvented. owner=`AGENT-MCP`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Attested Tool-Server Admission Protocol`；Evaluation=`§5 Security Evaluation`；Limitations/Counterevidence=`§6 Limitations and attestation-root boundary`。

<!-- claim:SF-2026-ARXIV-2605-24248:start -->Attested Tool-Server Admission: A Security Extension to the Model Context Protocol only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24248:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24248:end -->

<!-- review:SF-2026-ARXIV-2605-24259:start -->
#### Resident KV Claims: A Conformance Contract for Future Reuse under Active KV Pressure

**问题与机制。** We introduce resident KV claims, a conformance contract that binds future-reuse intent to a materialization predicate, lifecycle state, active/resident feasibility outcome, and claim-level telemetry. owner=`INFER-KV-CACHE`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Resident-KV Conformance Contract`；Evaluation=`§5 Active-Pressure Evaluation`；Limitations/Counterevidence=`§6 Limitations and cache-manager boundary`。

<!-- claim:SF-2026-ARXIV-2605-24259:start -->Resident KV Claims: A Conformance Contract for Future Reuse under Active KV Pressure only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24259:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24259:end -->

<!-- review:SF-2026-ARXIV-2605-24279:start -->
#### ContextEcho: A Benchmark for Persona Drift in Long Agentic-Coding Sessions

**问题与机制。** We introduce ContextEcho, a benchmark and reusable harness for measuring persona drift at deployment scale. owner=`AGENT-CONTEXT`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 ContextEcho snapshot-then-probe deployment harness`；Evaluation=`§4–§5 long agentic-coding session evaluation`；Limitations/Counterevidence=`§6 Limitations; persona probes and coding-session boundary`。

<!-- claim:SF-2026-ARXIV-2605-24279:start -->ContextEcho: A Benchmark for Persona Drift in Long Agentic-Coding Sessions only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24279:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24279:end -->

<!-- review:SF-2026-ARXIV-2605-24286:start -->
#### Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning

**问题与机制。** We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 information-flow faithfulness criteria and diagnostics`；Evaluation=`§4–§5 faithfulness evaluation/training`；Limitations/Counterevidence=`§6 Limitations; diagnostic proxies do not reveal hidden computation`。

<!-- claim:SF-2026-ARXIV-2605-24286:start -->Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24286:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24286:end -->

<!-- review:SF-2026-ARXIV-2605-24299:start -->
#### LLMs Show No Signs Of Individuated Metacognition

**问题与机制。** Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked. owner=`PLATFORM-EVALUATION-SYSTEM`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 factor-analysis decomposition of elicited confidence`；Evaluation=`§4 pairwise calibration across twenty models/six benchmarks`；Limitations/Counterevidence=`§5–§6 Limitations; elicited-confidence and tested-benchmark boundary`。

<!-- claim:SF-2026-ARXIV-2605-24299:start -->LLMs Show No Signs Of Individuated Metacognition only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24299:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24299:end -->

<!-- review:SF-2026-ARXIV-2605-24309:start -->
#### Reframing LLM Agent Security as an Agent-Human Interaction Problem

**问题与机制。** Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations. owner=`PLATFORM-SECURITY`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3 agent-human security mechanism taxonomy`；Evaluation=`§4 audit of papers, production agents and plugins`；Limitations/Counterevidence=`§5 Limitations; observational taxonomy does not prove mechanism efficacy`。

<!-- claim:SF-2026-ARXIV-2605-24309:start -->Reframing LLM Agent Security as an Agent-Human Interaction Problem only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24309:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24309:end -->

<!-- review:SF-2026-ARXIV-2605-24312:start -->
#### Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment

**问题与机制。** However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information. owner=`AGENT-RAG`；independent reconciliation=`author_retention_reconfirmed`。

**Exact-v1。** Method=`§3 Entailment-Based RAG Membership Inference`；Evaluation=`§4 Five-Query Evaluation`；Limitations/Counterevidence=`§5 Limitations and black-box-access boundary`。

<!-- claim:SF-2026-ARXIV-2605-24312:start -->Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-24312:end -->

Books Decision=`Integrate`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-24312:end -->

<!-- review:SF-2026-ARXIV-2605-26147:start -->
#### Neural Bayesian Sequential Routing

**问题与机制。** We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG). owner=`INFER-SCHEDULING`；independent reconciliation=`false_negative_recovered`。

**Exact-v1。** Method=`§3–§5 DAG evidence accumulation and sequential routing`；Evaluation=`§6–§8 controlled experiments and ablations`；Limitations/Counterevidence=`§9 Discussion; conjugate-belief assumptions and tested-model boundary`。

<!-- claim:SF-2026-ARXIV-2605-26147:start -->Neural Bayesian Sequential Routing only supports the exact-v1 disclosed method and evaluated workload; it does not prove untested models, hardware, concurrency, tail-SLO, adversarial distributions or production generality.<!-- claim:SF-2026-ARXIV-2605-26147:end -->

Books Decision=`No Change — Existing Coverage`；已顺读 current owner 与 immediate adjacent，Review notes 不计现有语义覆盖。
<!-- review:SF-2026-ARXIV-2605-26147:end -->

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

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23157 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23157 |
| SF-2026-ARXIV-2605-23158 | score_7_9;forced_review;potential_books_delta | selected | DA-SPLIT-INFERENCE-PRIVACY | — | 跨层改变隐私、评估预算或置信度控制假设 | analysis:DA-SPLIT-INFERENCE-PRIVACY |
| SF-2026-ARXIV-2605-23168 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23168 |
| SF-2026-ARXIV-2605-23170 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23170 |
| SF-2026-ARXIV-2605-23196 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23196 |
| SF-2026-ARXIV-2605-23200 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23200 |
| SF-2026-ARXIV-2605-23215 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23215 |
| SF-2026-ARXIV-2605-23218 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23218 |
| SF-2026-ARXIV-2605-23220 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23220 |
| SF-2026-ARXIV-2605-23258 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23258 |
| SF-2026-ARXIV-2605-23262 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23262 |
| SF-2026-ARXIV-2605-23294 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23294 |
| SF-2026-ARXIV-2605-23296 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23296 |
| SF-2026-ARXIV-2605-23311 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23311 |
| SF-2026-ARXIV-2605-23348 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23348 |
| SF-2026-ARXIV-2605-23362 | score_7_9 | selected | DA-BUDGETED-MULTI-JUDGE | — | 跨层改变隐私、评估预算或置信度控制假设 | analysis:DA-BUDGETED-MULTI-JUDGE |
| SF-2026-ARXIV-2605-23389 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23389 |
| SF-2026-ARXIV-2605-23414 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23414 |
| SF-2026-ARXIV-2605-23454 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23454 |
| SF-2026-ARXIV-2605-23464 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23464 |
| SF-2026-ARXIV-2605-23493 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23493 |
| SF-2026-ARXIV-2605-23574 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23574 |
| SF-2026-ARXIV-2605-23590 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23590 |
| SF-2026-ARXIV-2605-23628 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23628 |
| SF-2026-ARXIV-2605-23640 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23640 |
| SF-2026-ARXIV-2605-23657 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23657 |
| SF-2026-ARXIV-2605-23701 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23701 |
| SF-2026-ARXIV-2605-23723 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23723 |
| SF-2026-ARXIV-2605-23764 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23764 |
| SF-2026-ARXIV-2605-23856 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23856 |
| SF-2026-ARXIV-2605-23893 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23893 |
| SF-2026-ARXIV-2605-23899 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23899 |
| SF-2026-ARXIV-2605-23904 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-23904 |
| SF-2026-ARXIV-2605-24060 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24060 |
| SF-2026-ARXIV-2605-24069 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24069 |
| SF-2026-ARXIV-2605-24117 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24117 |
| SF-2026-ARXIV-2605-24134 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24134 |
| SF-2026-ARXIV-2605-24154 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24154 |
| SF-2026-ARXIV-2605-24168 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24168 |
| SF-2026-ARXIV-2605-24183 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24183 |
| SF-2026-ARXIV-2605-24197 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24197 |
| SF-2026-ARXIV-2605-24202 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24202 |
| SF-2026-ARXIV-2605-24213 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24213 |
| SF-2026-ARXIV-2605-24216 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24216 |
| SF-2026-ARXIV-2605-24217 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24217 |
| SF-2026-ARXIV-2605-24219 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24219 |
| SF-2026-ARXIV-2605-24220 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24220 |
| SF-2026-ARXIV-2605-24229 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24229 |
| SF-2026-ARXIV-2605-24245 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24245 |
| SF-2026-ARXIV-2605-24247 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24247 |
| SF-2026-ARXIV-2605-24248 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24248 |
| SF-2026-ARXIV-2605-24259 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24259 |
| SF-2026-ARXIV-2605-24279 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24279 |
| SF-2026-ARXIV-2605-24286 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24286 |
| SF-2026-ARXIV-2605-24299 | score_7_9 | selected | DA-ELICITED-CONFIDENCE-BOUNDARY | — | 跨层改变隐私、评估预算或置信度控制假设 | analysis:DA-ELICITED-CONFIDENCE-BOUNDARY |
| SF-2026-ARXIV-2605-24309 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24309 |
| SF-2026-ARXIV-2605-24312 | score_7_9;forced_review;potential_books_delta | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-24312 |
| SF-2026-ARXIV-2605-26147 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-26147 |
| SF-2026-ARXIV-2605-27432 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-27432 |
| SF-2026-ARXIV-2605-27435 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-27435 |
| SF-2026-ARXIV-2605-27437 | score_7_9 | not_selected | — | — | exact-v1 已完成；未选仅受 Daily 三项叙事上限约束 | analysis-decision:SF-2026-ARXIV-2605-27437 |

<!-- analysis:DA-SPLIT-INFERENCE-PRIVACY:start -->
### DA-SPLIT-INFERENCE-PRIVACY

Split inference 在端侧算力受限且不上传原文时合理；当 server-visible activation 可被反演，隐私边界便从数据格式转为可验证攻击面。ActInv/PAF 把 split point 与 layer sensitivity 纳入选择，但防御会支付端侧计算、扰动和 utility cost；exact-v1 只证明所测模型、层与攻击，不能把未被恢复等同于隐私保证。
<!-- analysis:DA-SPLIT-INFERENCE-PRIVACY:end -->

<!-- analysis:DA-BUDGETED-MULTI-JUDGE:start -->
### DA-BUDGETED-MULTI-JUDGE

固定一个 judge 在成本和可靠性近似一致时简单；多 judge 价格、方差和样本难度异质后，evaluation controller 必须拥有预算分配。实例自适应分配降低给定预算下的估计误差，却新增 pilot query、方差估计和分配偏差；oracle/渐近结论不证明未知分布或 judge drift 下仍最优。
<!-- analysis:DA-BUDGETED-MULTI-JUDGE:end -->

<!-- analysis:DA-ELICITED-CONFIDENCE-BOUNDARY:start -->
### DA-ELICITED-CONFIDENCE-BOUNDARY

用模型自报 confidence 做 abstention/routing 在 aggregate calibration 稳定时诱人；跨模型 confidence 近似共同因子而非个体能力信号时，它不能回答‘这个模型是否知道自己不知道’。收益是把 self-report 与 behavior probe 分离，代价是必须实际执行 probe 或引入外部 evidence；20 个模型/六个 benchmark 不证明所有内部不确定性都不可访问。
<!-- analysis:DA-ELICITED-CONFIDENCE-BOUNDARY:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23157:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23157:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23168:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23168:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23170:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23170:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23196:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23196:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23200:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23200:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23215:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23215:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23218:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23218:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23220:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23220:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23258:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23258:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23262:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23262:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23294:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23294:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23296:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23296:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23311:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23311:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23348:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23348:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23389:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23389:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23414:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23414:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23454:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23454:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23464:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23464:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23493:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23493:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23574:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23574:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23590:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23590:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23628:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23628:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23640:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23640:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23657:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23657:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23701:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23701:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23723:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23723:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23764:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23764:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23856:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23856:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23893:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23893:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23899:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23899:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-23904:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-23904:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24060:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24060:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24069:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24069:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24117:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24117:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24134:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24134:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24154:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24154:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24168:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24168:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24183:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24183:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24197:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24197:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24202:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24202:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24213:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24213:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24216:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24216:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24217:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24217:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24219:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24219:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24220:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24220:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24229:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24229:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24245:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24245:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24247:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24247:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24248:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24248:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24259:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24259:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24279:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24279:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24286:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24286:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24309:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24309:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-24312:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-24312:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-26147:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-26147:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27432:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-27432:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27435:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-27435:end -->
<!-- analysis-decision:SF-2026-ARXIV-2605-27437:start -->exact-v1 Review 已完成；not_selected 仅是三项 Deep Analysis 上限，不改变 Evidence 或 Books Decision。<!-- analysis-decision:SF-2026-ARXIV-2605-27437:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2605-23157 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23157 | delta:SF-2026-ARXIV-2605-23157 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23157 |
| SF-2026-ARXIV-2605-23158 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23158 | delta:SF-2026-ARXIV-2605-23158 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23158 |
| SF-2026-ARXIV-2605-23168 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-23168 | delta:SF-2026-ARXIV-2605-23168 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23168 |
| SF-2026-ARXIV-2605-23170 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23170 | delta:SF-2026-ARXIV-2605-23170 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23170 |
| SF-2026-ARXIV-2605-23196 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23196 | delta:SF-2026-ARXIV-2605-23196 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23196 |
| SF-2026-ARXIV-2605-23200 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23200 | delta:SF-2026-ARXIV-2605-23200 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23200 |
| SF-2026-ARXIV-2605-23215 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23215 | delta:SF-2026-ARXIV-2605-23215 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23215 |
| SF-2026-ARXIV-2605-23218 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23218 | delta:SF-2026-ARXIV-2605-23218 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23218 |
| SF-2026-ARXIV-2605-23220 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23220 | delta:SF-2026-ARXIV-2605-23220 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23220 |
| SF-2026-ARXIV-2605-23258 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23258 | delta:SF-2026-ARXIV-2605-23258 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23258 |
| SF-2026-ARXIV-2605-23262 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23262 | delta:SF-2026-ARXIV-2605-23262 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23262 |
| SF-2026-ARXIV-2605-23294 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-23294 | delta:SF-2026-ARXIV-2605-23294 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23294 |
| SF-2026-ARXIV-2605-23296 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-23296 | delta:SF-2026-ARXIV-2605-23296 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23296 |
| SF-2026-ARXIV-2605-23311 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#chapter-78 | books/part-07-agent/77-memory.md#chapter-77;books/part-07-agent/79-planning.md#chapter-79 | existing:SF-2026-ARXIV-2605-23311 | delta:SF-2026-ARXIV-2605-23311 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23311 |
| SF-2026-ARXIV-2605-23348 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-23348 | delta:SF-2026-ARXIV-2605-23348 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23348 |
| SF-2026-ARXIV-2605-23362 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23362 | delta:SF-2026-ARXIV-2605-23362 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23362 |
| SF-2026-ARXIV-2605-23389 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-23389 | delta:SF-2026-ARXIV-2605-23389 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23389 |
| SF-2026-ARXIV-2605-23414 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23414 | delta:SF-2026-ARXIV-2605-23414 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23414 |
| SF-2026-ARXIV-2605-23454 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-23454 | delta:SF-2026-ARXIV-2605-23454 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23454 |
| SF-2026-ARXIV-2605-23464 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-23464 | delta:SF-2026-ARXIV-2605-23464 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23464 |
| SF-2026-ARXIV-2605-23493 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-23493 | delta:SF-2026-ARXIV-2605-23493 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23493 |
| SF-2026-ARXIV-2605-23574 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-23574 | delta:SF-2026-ARXIV-2605-23574 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23574 |
| SF-2026-ARXIV-2605-23590 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#chapter-81 | books/part-07-agent/80-reflection.md#chapter-80;books/part-07-agent/82-multi-agent.md#chapter-82 | existing:SF-2026-ARXIV-2605-23590 | delta:SF-2026-ARXIV-2605-23590 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23590 |
| SF-2026-ARXIV-2605-23628 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23628 | delta:SF-2026-ARXIV-2605-23628 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23628 |
| SF-2026-ARXIV-2605-23640 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-23640 | delta:SF-2026-ARXIV-2605-23640 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23640 |
| SF-2026-ARXIV-2605-23657 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23657 | delta:SF-2026-ARXIV-2605-23657 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23657 |
| SF-2026-ARXIV-2605-23701 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-23701 | delta:SF-2026-ARXIV-2605-23701 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23701 |
| SF-2026-ARXIV-2605-23723 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-23723 | delta:SF-2026-ARXIV-2605-23723 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23723 |
| SF-2026-ARXIV-2605-23764 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#chapter-36 | books/part-04-training-system/35-checkpoint.md#chapter-35;books/part-04-training-system/37-tensor-parallel.md#chapter-37 | existing:SF-2026-ARXIV-2605-23764 | delta:SF-2026-ARXIV-2605-23764 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23764 |
| SF-2026-ARXIV-2605-23856 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#chapter-25 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#chapter-24;books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#chapter-26 | existing:SF-2026-ARXIV-2605-23856 | delta:SF-2026-ARXIV-2605-23856 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23856 |
| SF-2026-ARXIV-2605-23893 | MODEL-MOE | books/part-02-model/21-moe.md#chapter-21 | books/part-02-model/20-sampling.md#chapter-20;books/part-02-model/22-long-context.md#chapter-22 | existing:SF-2026-ARXIV-2605-23893 | delta:SF-2026-ARXIV-2605-23893 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-23893 |
| SF-2026-ARXIV-2605-23899 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23899 | delta:SF-2026-ARXIV-2605-23899 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23899 |
| SF-2026-ARXIV-2605-23904 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-23904 | delta:SF-2026-ARXIV-2605-23904 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-23904 |
| SF-2026-ARXIV-2605-24060 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24060 | delta:SF-2026-ARXIV-2605-24060 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24060 |
| SF-2026-ARXIV-2605-24069 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-24069 | delta:SF-2026-ARXIV-2605-24069 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24069 |
| SF-2026-ARXIV-2605-24117 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#chapter-84 | books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24117 | delta:SF-2026-ARXIV-2605-24117 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24117 |
| SF-2026-ARXIV-2605-24134 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24134 | delta:SF-2026-ARXIV-2605-24134 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24134 |
| SF-2026-ARXIV-2605-24154 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24154 | delta:SF-2026-ARXIV-2605-24154 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24154 |
| SF-2026-ARXIV-2605-24168 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24168 | delta:SF-2026-ARXIV-2605-24168 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24168 |
| SF-2026-ARXIV-2605-24183 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24183 | delta:SF-2026-ARXIV-2605-24183 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24183 |
| SF-2026-ARXIV-2605-24197 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#chapter-82 | books/part-07-agent/81-workflow.md#chapter-81;books/part-07-agent/83-mcp.md#chapter-83 | existing:SF-2026-ARXIV-2605-24197 | delta:SF-2026-ARXIV-2605-24197 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24197 |
| SF-2026-ARXIV-2605-24202 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24202 | delta:SF-2026-ARXIV-2605-24202 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24202 |
| SF-2026-ARXIV-2605-24213 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24213 | delta:SF-2026-ARXIV-2605-24213 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24213 |
| SF-2026-ARXIV-2605-24216 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24216 | delta:SF-2026-ARXIV-2605-24216 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24216 |
| SF-2026-ARXIV-2605-24217 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24217 | delta:SF-2026-ARXIV-2605-24217 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24217 |
| SF-2026-ARXIV-2605-24219 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24219 | delta:SF-2026-ARXIV-2605-24219 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24219 |
| SF-2026-ARXIV-2605-24220 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#chapter-31 | books/part-04-training-system/30-lora.md#chapter-30;books/part-04-training-system/32-ppo.md#chapter-32 | existing:SF-2026-ARXIV-2605-24220 | delta:SF-2026-ARXIV-2605-24220 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24220 |
| SF-2026-ARXIV-2605-24229 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24229 | delta:SF-2026-ARXIV-2605-24229 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24229 |
| SF-2026-ARXIV-2605-24245 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24245 | delta:SF-2026-ARXIV-2605-24245 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24245 |
| SF-2026-ARXIV-2605-24247 | TRAIN-DATA | books/part-04-training-system/27-data.md#chapter-27 | books/part-04-training-system/28-pretraining.md#chapter-28 | existing:SF-2026-ARXIV-2605-24247 | delta:SF-2026-ARXIV-2605-24247 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24247 |
| SF-2026-ARXIV-2605-24248 | AGENT-MCP | books/part-07-agent/83-mcp.md#chapter-83 | books/part-07-agent/82-multi-agent.md#chapter-82;books/part-07-agent/84-agent-platform.md#chapter-84 | existing:SF-2026-ARXIV-2605-24248 | delta:SF-2026-ARXIV-2605-24248 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24248 |
| SF-2026-ARXIV-2605-24259 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#chapter-45 | books/part-05-inference-system/44-decode.md#chapter-44;books/part-05-inference-system/46-continuous-batching.md#chapter-46 | existing:SF-2026-ARXIV-2605-24259 | delta:SF-2026-ARXIV-2605-24259 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24259 |
| SF-2026-ARXIV-2605-24279 | AGENT-CONTEXT | books/part-07-agent/75-context.md#chapter-75 | books/part-07-agent/74-prompt.md#chapter-74;books/part-07-agent/76-rag.md#chapter-76 | existing:SF-2026-ARXIV-2605-24279 | delta:SF-2026-ARXIV-2605-24279 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24279 |
| SF-2026-ARXIV-2605-24286 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24286 | delta:SF-2026-ARXIV-2605-24286 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24286 |
| SF-2026-ARXIV-2605-24299 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#chapter-66 | books/part-06-ai-infrastructure/65-kai-scheduler.md#chapter-65;books/part-06-ai-infrastructure/67-monitoring.md#chapter-67 | existing:SF-2026-ARXIV-2605-24299 | delta:SF-2026-ARXIV-2605-24299 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24299 |
| SF-2026-ARXIV-2605-24309 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#chapter-72 | books/part-06-ai-infrastructure/71-multi-tenant.md#chapter-71;books/part-06-ai-infrastructure/73-production-best-practice.md#chapter-73 | existing:SF-2026-ARXIV-2605-24309 | delta:SF-2026-ARXIV-2605-24309 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-24309 |
| SF-2026-ARXIV-2605-24312 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-24312 | delta:SF-2026-ARXIV-2605-24312 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2605-24312 |
| SF-2026-ARXIV-2605-26147 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#chapter-56 | books/part-05-inference-system/55-pd-disaggregation.md#chapter-55 | existing:SF-2026-ARXIV-2605-26147 | delta:SF-2026-ARXIV-2605-26147 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-26147 |
| SF-2026-ARXIV-2605-27432 | AGENT-RAG | books/part-07-agent/76-rag.md#chapter-76 | books/part-07-agent/75-context.md#chapter-75;books/part-07-agent/77-memory.md#chapter-77 | existing:SF-2026-ARXIV-2605-27432 | delta:SF-2026-ARXIV-2605-27432 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27432 |
| SF-2026-ARXIV-2605-27435 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#chapter-49 | books/part-05-inference-system/48-speculative-decoding.md#chapter-48;books/part-05-inference-system/50-vllm.md#chapter-50 | existing:SF-2026-ARXIV-2605-27435 | delta:SF-2026-ARXIV-2605-27435 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27435 |
| SF-2026-ARXIV-2605-27437 | AGENT-MEMORY | books/part-07-agent/77-memory.md#chapter-77 | books/part-07-agent/76-rag.md#chapter-76;books/part-07-agent/78-tool-calling.md#chapter-78 | existing:SF-2026-ARXIV-2605-27437 | delta:SF-2026-ARXIV-2605-27437 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2605-27437 |
<!-- books-review:SF-2026-ARXIV-2605-23157:start -->
<!-- existing:SF-2026-ARXIV-2605-23157:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23157:end -->
<!-- delta:SF-2026-ARXIV-2605-23157:start -->We present the first systematic cross-lingual, multimodal red-teaming study comparing jailbreak vulnerability in US English (en-US) and Mexican Spanish (es-MX) across four frontier MLLMs: Claude Sonnet 4.5, GPT-5, Pixtral Large, and Qwen Omni.<!-- delta:SF-2026-ARXIV-2605-23157:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23157:end -->
<!-- books-review:SF-2026-ARXIV-2605-23158:start -->
<!-- existing:SF-2026-ARXIV-2605-23158:start -->现有安全章没有把 split point、server-visible activation 与 inversion attack 共同定义为隐私边界。<!-- existing:SF-2026-ARXIV-2605-23158:end -->
<!-- delta:SF-2026-ARXIV-2605-23158:start -->To fill this gap, we introduce ActInv, which solves an intermediate activation matching problem to reconstruct the client's input.<!-- delta:SF-2026-ARXIV-2605-23158:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23158:end -->
<!-- books-review:SF-2026-ARXIV-2605-23168:start -->
<!-- existing:SF-2026-ARXIV-2605-23168:start -->正文已覆盖 data lineage、poisoning/contamination、specification compilation 与 golden-data governance。 本 family 的具体机制 `We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23168:end -->
<!-- delta:SF-2026-ARXIV-2605-23168:start -->We introduce PoisonForge, a benchmark that parameterizes this threat along four dimensions (bias type, poisoning mode, appearance count, and target output length) and evaluates 12 open-weight models (from 2B to 32B parameters) across five families under a primarily 1% poison budget.<!-- delta:SF-2026-ARXIV-2605-23168:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1。
<!-- books-review:SF-2026-ARXIV-2605-23168:end -->
<!-- books-review:SF-2026-ARXIV-2605-23170:start -->
<!-- existing:SF-2026-ARXIV-2605-23170:start -->现有 Evaluation 主线没有把 target position、filler content 与 context length 冻结成 reasoning benchmark 的联合 identity。<!-- existing:SF-2026-ARXIV-2605-23170:end -->
<!-- delta:SF-2026-ARXIV-2605-23170:start -->We propose Context Rot Evaluation (CRE), a controlled framework varying all three factors, and evaluate nine LLMs on GSM8K and ARC-Challenge across two rounds: an initial five-model set and four newer vendor releases.<!-- delta:SF-2026-ARXIV-2605-23170:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23170:end -->
<!-- books-review:SF-2026-ARXIV-2605-23196:start -->
<!-- existing:SF-2026-ARXIV-2605-23196:start -->现有 pre-guard 叙述没有覆盖 guardrail inspection window 与 downstream model context window 不一致造成的可组合绕过。<!-- existing:SF-2026-ARXIV-2605-23196:end -->
<!-- delta:SF-2026-ARXIV-2605-23196:start -->In this paper, we identify a critical blind spot arising from the mismatch between the limited inspection windows of guardrail models and the substantially larger context inference windows of downstream LLMs.<!-- delta:SF-2026-ARXIV-2605-23196:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23196:end -->
<!-- books-review:SF-2026-ARXIV-2605-23200:start -->
<!-- existing:SF-2026-ARXIV-2605-23200:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23200:end -->
<!-- delta:SF-2026-ARXIV-2605-23200:start -->However, we show that their reliance on global Top-k selection triggers Region Wipe-out: the severe eviction of contiguous reasoning blocks that derails logical coherence.<!-- delta:SF-2026-ARXIV-2605-23200:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23200:end -->
<!-- books-review:SF-2026-ARXIV-2605-23215:start -->
<!-- existing:SF-2026-ARXIV-2605-23215:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23215:end -->
<!-- delta:SF-2026-ARXIV-2605-23215:start -->The resulting reward signals are misleading: agents learn to generate kernels that score well in sandboxes but introduce interface incompatibilities, compilation-stack conflicts, and silent correctness degradation when integrated into real systems.<!-- delta:SF-2026-ARXIV-2605-23215:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23215:end -->
<!-- books-review:SF-2026-ARXIV-2605-23218:start -->
<!-- existing:SF-2026-ARXIV-2605-23218:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23218:end -->
<!-- delta:SF-2026-ARXIV-2605-23218:start -->Autonomous agents are moving from tools into a layer of social infrastructure: they browse, purchase, deploy software, manage systems, and increasingly interact with one another.<!-- delta:SF-2026-ARXIV-2605-23218:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-23218:end -->
<!-- books-review:SF-2026-ARXIV-2605-23220:start -->
<!-- existing:SF-2026-ARXIV-2605-23220:start -->正文已覆盖 action-conditioned transition、rollout identity、attack surface、fallback 与 world-state evaluation。 本 family 的具体机制 `We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23220:end -->
<!-- delta:SF-2026-ARXIV-2605-23220:start -->We introduce WMAttack, an automated attack-search framework for adversarial evaluation of world-model agents.<!-- delta:SF-2026-ARXIV-2605-23220:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3。
<!-- books-review:SF-2026-ARXIV-2605-23220:end -->
<!-- books-review:SF-2026-ARXIV-2605-23258:start -->
<!-- existing:SF-2026-ARXIV-2605-23258:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23258:end -->
<!-- delta:SF-2026-ARXIV-2605-23258:start -->We present VECTOR, a plug-and-play augmentation for eviction-based pipelines that introduces three-way token routing: retention, approximation, and eviction.<!-- delta:SF-2026-ARXIV-2605-23258:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23258:end -->
<!-- books-review:SF-2026-ARXIV-2605-23262:start -->
<!-- existing:SF-2026-ARXIV-2605-23262:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23262:end -->
<!-- delta:SF-2026-ARXIV-2605-23262:start -->We introduce a work-centered benchmark representation with four fields: represented activity, tested setting, required work product, and evaluated result.<!-- delta:SF-2026-ARXIV-2605-23262:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23262:end -->
<!-- books-review:SF-2026-ARXIV-2605-23294:start -->
<!-- existing:SF-2026-ARXIV-2605-23294:start -->正文已把 backend lowering、heterogeneous execution、kernel correctness 与 device fallback 放在同一执行计划中。 本 family 的具体机制 `With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23294:end -->
<!-- delta:SF-2026-ARXIV-2605-23294:start -->With extensive experimental results, we demonstrate NASiC achieves 4-114.8x improved performance and 3.9-70x improved energy efficiency over state-of-the-art designs, along with high accuracy, showing its great potential for efficient on-device MoE LLM inference.<!-- delta:SF-2026-ARXIV-2605-23294:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4c19b842b8e2ddb31cc4681c31e5484defce4f9769950473cc31a5afa61e338a。
<!-- books-review:SF-2026-ARXIV-2605-23294:end -->
<!-- books-review:SF-2026-ARXIV-2605-23296:start -->
<!-- existing:SF-2026-ARXIV-2605-23296:start -->现有 Context Compression 尚未表达 blocking compaction 到 parallel/background compaction 的状态交接、stall 与 fidelity contract。<!-- existing:SF-2026-ARXIV-2605-23296:end -->
<!-- delta:SF-2026-ARXIV-2605-23296:start -->We introduce \textbf{parallel compaction} for long-horizon agentic flows and characterize it against the sequential synchronous baseline across four backbones spanning 8B to 120B parameters, mixing dense and MoE architectures with reasoning and non-reasoning models, on the HotpotQA multi-hop QA and LoCoMo long-context dialogue benchmarks.<!-- delta:SF-2026-ARXIV-2605-23296:end --> Independent decision=`Integrate`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-23296:end -->
<!-- books-review:SF-2026-ARXIV-2605-23311:start -->
<!-- existing:SF-2026-ARXIV-2605-23311:start -->正文已覆盖 proposal/commit、tool contract、recoverability、effect receipt 与 exactly-once boundary。 本 family 的具体机制 `We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23311:end -->
<!-- delta:SF-2026-ARXIV-2605-23311:start -->We formalize this gap as semantic recoverability and address it in DART, a modular runtime that localizes the failed instance, certifies semantically recoverable boundaries of that instance, aligns checkpoints to those boundaries, and selects an admissible restore point that preserves committed downstream work under dependency and effect constraints-or blocks otherwise.<!-- delta:SF-2026-ARXIV-2605-23311:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=3deca1b35edccc646c1982cea7dd44ce99b94d42a6052e4a581d9ef9007f2bf9。
<!-- books-review:SF-2026-ARXIV-2605-23311:end -->
<!-- books-review:SF-2026-ARXIV-2605-23348:start -->
<!-- existing:SF-2026-ARXIV-2605-23348:start -->正文已覆盖 workload-aware admission、placement、batch cost、SLO 与 fallback。 本 family 的具体机制 `AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23348:end -->
<!-- delta:SF-2026-ARXIV-2605-23348:start -->AI power demand is growing at an unprecedented rate while power grids are often ailing and struggle to keep up.<!-- delta:SF-2026-ARXIV-2605-23348:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-23348:end -->
<!-- books-review:SF-2026-ARXIV-2605-23362:start -->
<!-- existing:SF-2026-ARXIV-2605-23362:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We formalize this question as *budgeted heteroskedastic multi-judge estimation*.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23362:end -->
<!-- delta:SF-2026-ARXIV-2605-23362:start -->We formalize this question as *budgeted heteroskedastic multi-judge estimation*.<!-- delta:SF-2026-ARXIV-2605-23362:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23362:end -->
<!-- books-review:SF-2026-ARXIV-2605-23389:start -->
<!-- existing:SF-2026-ARXIV-2605-23389:start -->现有调度章未明确 decode iteration 内 KV-length 差异形成的 batch critical path 及 prefix-length-aware regrouping。<!-- existing:SF-2026-ARXIV-2605-23389:end -->
<!-- delta:SF-2026-ARXIV-2605-23389:start -->We propose AlignedServe, an LLM serving framework built around prefix-aware batching.<!-- delta:SF-2026-ARXIV-2605-23389:end --> Independent decision=`Integrate`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-23389:end -->
<!-- books-review:SF-2026-ARXIV-2605-23414:start -->
<!-- existing:SF-2026-ARXIV-2605-23414:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23414:end -->
<!-- delta:SF-2026-ARXIV-2605-23414:start -->To address this, we propose the Epistemic Planning Calibration Agentic Workflow (EPC-AW), which assesses whether plans remain supported under varying information conditions rather than directly verifying feasibility.<!-- delta:SF-2026-ARXIV-2605-23414:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-23414:end -->
<!-- books-review:SF-2026-ARXIV-2605-23454:start -->
<!-- existing:SF-2026-ARXIV-2605-23454:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23454:end -->
<!-- delta:SF-2026-ARXIV-2605-23454:start -->We propose ARES (Automated Rubric synthEsis for Scalable RL), a framework for automatically constructing rubric-based RL data at scale.<!-- delta:SF-2026-ARXIV-2605-23454:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-23454:end -->
<!-- books-review:SF-2026-ARXIV-2605-23464:start -->
<!-- existing:SF-2026-ARXIV-2605-23464:start -->现有安全章没有区分可协作训练/推理的 protocol-visible state 与不得 materialize 的 weight state。<!-- existing:SF-2026-ARXIV-2605-23464:end -->
<!-- delta:SF-2026-ARXIV-2605-23464:start -->We introduce Unextractable Protocol Models (UPMs): a training and inference framework that leverages the sharded model setup to ensure model shards (i.e., subsets) held by participants are incompatible at different time steps.<!-- delta:SF-2026-ARXIV-2605-23464:end --> Independent decision=`Integrate`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-23464:end -->
<!-- books-review:SF-2026-ARXIV-2605-23493:start -->
<!-- existing:SF-2026-ARXIV-2605-23493:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23493:end -->
<!-- delta:SF-2026-ARXIV-2605-23493:start -->In this paper, we study this problem in a rare-token/identity setting and propose EviDence GuidEd On-Policy Distillation (EDGE-OPD), a modification of OPSD with two distinct characteristics: a) it uses guided rollouts to inject privileged-context behavior to the student at sampling time, so that the rare target behavior is actually present in the on-policy data, and b) it applies an evidence mask: the student is updated only at token positions where the privileged context supports the sampled token, rather than on every token in the rollout.<!-- delta:SF-2026-ARXIV-2605-23493:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-23493:end -->
<!-- books-review:SF-2026-ARXIV-2605-23574:start -->
<!-- existing:SF-2026-ARXIV-2605-23574:start -->正文已覆盖 durable state、recovery、verification、workflow artifact 与 step-level effect receipt。 本 family 的具体机制 `We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23574:end -->
<!-- delta:SF-2026-ARXIV-2605-23574:start -->We study this gap as Quantitative Goal Persistence (QGP): whether an agent keeps working until an external verifier confirms enough distinct valid items.<!-- delta:SF-2026-ARXIV-2605-23574:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=7f7eae6d8d7e338dcabc560ffb2cfd50c173f0b680ad44fbde5bf434e38fa32e。
<!-- books-review:SF-2026-ARXIV-2605-23574:end -->
<!-- books-review:SF-2026-ARXIV-2605-23590:start -->
<!-- existing:SF-2026-ARXIV-2605-23590:start -->正文已覆盖 durable state、recovery、verification、workflow artifact 与 step-level effect receipt。 本 family 的具体机制 `We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23590:end -->
<!-- delta:SF-2026-ARXIV-2605-23590:start -->We introduce Co-ReAct, a rubric-guided action-selection framework that uses rubrics as step-level guidance during inference.<!-- delta:SF-2026-ARXIV-2605-23590:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=7f7eae6d8d7e338dcabc560ffb2cfd50c173f0b680ad44fbde5bf434e38fa32e。
<!-- books-review:SF-2026-ARXIV-2605-23590:end -->
<!-- books-review:SF-2026-ARXIV-2605-23628:start -->
<!-- existing:SF-2026-ARXIV-2605-23628:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23628:end -->
<!-- delta:SF-2026-ARXIV-2605-23628:start -->Leveraging this identification, we show that the benchmark-specific training problem is NP-hard under Borda count and mean win rate.<!-- delta:SF-2026-ARXIV-2605-23628:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23628:end -->
<!-- books-review:SF-2026-ARXIV-2605-23640:start -->
<!-- existing:SF-2026-ARXIV-2605-23640:start -->正文已覆盖 cache identity、reuse、eviction/offload、approximate residual、admission、tiering 与 failure fallback。 本 family 的具体机制 `Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23640:end -->
<!-- delta:SF-2026-ARXIV-2605-23640:start -->Building on this, we present CachePrune, a privacy-aware KV cache sharing mechanism that enables fine-grained reuse of KV entries across requests.<!-- delta:SF-2026-ARXIV-2605-23640:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-23640:end -->
<!-- books-review:SF-2026-ARXIV-2605-23657:start -->
<!-- existing:SF-2026-ARXIV-2605-23657:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23657:end -->
<!-- delta:SF-2026-ARXIV-2605-23657:start -->In this paper, we present \textsc{OpenSkillEval}, an automatic evaluation framework for both skill-augmented agent systems and the skills themselves.<!-- delta:SF-2026-ARXIV-2605-23657:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23657:end -->
<!-- books-review:SF-2026-ARXIV-2605-23701:start -->
<!-- existing:SF-2026-ARXIV-2605-23701:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23701:end -->
<!-- delta:SF-2026-ARXIV-2605-23701:start -->We study a protocol-level test for weak-label benchmarks: whether benchmark outputs change when the provided evidence is intervened on.<!-- delta:SF-2026-ARXIV-2605-23701:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-23701:end -->
<!-- books-review:SF-2026-ARXIV-2605-23723:start -->
<!-- existing:SF-2026-ARXIV-2605-23723:start -->正文已覆盖 memory write/read、reflective retrieval、provenance、rollback 与 lifecycle evaluation。 本 family 的具体机制 `We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23723:end -->
<!-- delta:SF-2026-ARXIV-2605-23723:start -->We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents.<!-- delta:SF-2026-ARXIV-2605-23723:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=f09fd5d839379ade75d2834c66aa9ce5c2eb4b2acac0e2773be3054d41222be0。
<!-- books-review:SF-2026-ARXIV-2605-23723:end -->
<!-- books-review:SF-2026-ARXIV-2605-23764:start -->
<!-- existing:SF-2026-ARXIV-2605-23764:start -->正文已覆盖 Expert Parallel、topology、heterogeneous execution、routing replay 与 distributed-state correctness。 本 family 的具体机制 `Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23764:end -->
<!-- delta:SF-2026-ARXIV-2605-23764:start -->Modern Mixture-of-Experts (MoE) models increasingly rely on large-scale AI accelerator clusters for efficient training.<!-- delta:SF-2026-ARXIV-2605-23764:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=4f93d876e7023721408d2cb9a84c868ecf7049796c99bb18d430ffb936337560。
<!-- books-review:SF-2026-ARXIV-2605-23764:end -->
<!-- books-review:SF-2026-ARXIV-2605-23856:start -->
<!-- existing:SF-2026-ARXIV-2605-23856:start -->正文已覆盖 action-conditioned transition、rollout identity、attack surface、fallback 与 world-state evaluation。 本 family 的具体机制 `We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23856:end -->
<!-- delta:SF-2026-ARXIV-2605-23856:start -->We propose JOPAT, a JOint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer.<!-- delta:SF-2026-ARXIV-2605-23856:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=bb63f32b52cb1e7457ed888eaa9f53fe6273a85a72dd5737709f9832795bf3a3。
<!-- books-review:SF-2026-ARXIV-2605-23856:end -->
<!-- books-review:SF-2026-ARXIV-2605-23893:start -->
<!-- existing:SF-2026-ARXIV-2605-23893:start -->现有 MoE 与 pretraining parameterization 未完整覆盖 expert width/count 改变时的超参数迁移与 scaling identity。<!-- existing:SF-2026-ARXIV-2605-23893:end -->
<!-- delta:SF-2026-ARXIV-2605-23893:start -->We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks.<!-- delta:SF-2026-ARXIV-2605-23893:end --> Independent decision=`Integrate`；owner_sha256=3eaf93101db6b0f4fb7aa292a3e610b6fc1cc14af84e385edd9b2c7d115de79d。
<!-- books-review:SF-2026-ARXIV-2605-23893:end -->
<!-- books-review:SF-2026-ARXIV-2605-23899:start -->
<!-- existing:SF-2026-ARXIV-2605-23899:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23899:end -->
<!-- delta:SF-2026-ARXIV-2605-23899:start -->However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail.<!-- delta:SF-2026-ARXIV-2605-23899:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23899:end -->
<!-- books-review:SF-2026-ARXIV-2605-23904:start -->
<!-- existing:SF-2026-ARXIV-2605-23904:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-23904:end -->
<!-- delta:SF-2026-ARXIV-2605-23904:start -->Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.<!-- delta:SF-2026-ARXIV-2605-23904:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-23904:end -->
<!-- books-review:SF-2026-ARXIV-2605-24060:start -->
<!-- existing:SF-2026-ARXIV-2605-24060:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24060:end -->
<!-- delta:SF-2026-ARXIV-2605-24060:start -->We show that this scoring-target choice is often left implicit and can materially change benchmark conclusions.<!-- delta:SF-2026-ARXIV-2605-24060:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24060:end -->
<!-- books-review:SF-2026-ARXIV-2605-24069:start -->
<!-- existing:SF-2026-ARXIV-2605-24069:start -->正文已覆盖 protocol/authorization boundary、tool-set admission、information flow、effect-time authorization 与 provenance。 本 family 的具体机制 `To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24069:end -->
<!-- delta:SF-2026-ARXIV-2605-24069:start -->To rigorously and systematically evaluate this emerging threat, we introduce the MCP-TDP Security Benchmark.<!-- delta:SF-2026-ARXIV-2605-24069:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=49fbcf4975553049fa6fbcf81baf5b91d04ff47dd5faa14191df42827025fc76。
<!-- books-review:SF-2026-ARXIV-2605-24069:end -->
<!-- books-review:SF-2026-ARXIV-2605-24117:start -->
<!-- existing:SF-2026-ARXIV-2605-24117:start -->正文已覆盖 Skill lifecycle、self-evolution admission、artifact identity 与 drift retirement。 本 family 的具体机制 `We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24117:end -->
<!-- delta:SF-2026-ARXIV-2605-24117:start -->We introduce SkillEvolBench, a diagnostic benchmark for evaluating this step from experience reuse to skill formation.<!-- delta:SF-2026-ARXIV-2605-24117:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6980a9cf747990532ed9860f9f29811513be4f712acea90972df70247cbc3360。
<!-- books-review:SF-2026-ARXIV-2605-24117:end -->
<!-- books-review:SF-2026-ARXIV-2605-24134:start -->
<!-- existing:SF-2026-ARXIV-2605-24134:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24134:end -->
<!-- delta:SF-2026-ARXIV-2605-24134:start -->We introduce ProofAgent Harness, open infrastructure for scalable, auditable, and adversarial AI agent evaluation.<!-- delta:SF-2026-ARXIV-2605-24134:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24134:end -->
<!-- books-review:SF-2026-ARXIV-2605-24154:start -->
<!-- existing:SF-2026-ARXIV-2605-24154:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24154:end -->
<!-- delta:SF-2026-ARXIV-2605-24154:start -->To this end, we propose \textsc{Palette}, a modular, controllable, and efficient framework that selectively relaxes refusal behavior on authorized target domains while preserving standard safety elsewhere.<!-- delta:SF-2026-ARXIV-2605-24154:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24154:end -->
<!-- books-review:SF-2026-ARXIV-2605-24168:start -->
<!-- existing:SF-2026-ARXIV-2605-24168:start -->正文已覆盖 context assembly、compression loss、identity、policy integrity 与 long-session state。 本 family 的具体机制 `Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24168:end -->
<!-- delta:SF-2026-ARXIV-2605-24168:start -->Second, we perform an extensive study of sparsity in LLMs spanning 20 models across five model families, varying context lengths, and different sparsity levels.<!-- delta:SF-2026-ARXIV-2605-24168:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24168:end -->
<!-- books-review:SF-2026-ARXIV-2605-24183:start -->
<!-- existing:SF-2026-ARXIV-2605-24183:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24183:end -->
<!-- delta:SF-2026-ARXIV-2605-24183:start -->We introduce AvalancheBench, a benchmark for evaluating enterprise data agents through \emph{latent world recovery}.<!-- delta:SF-2026-ARXIV-2605-24183:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24183:end -->
<!-- books-review:SF-2026-ARXIV-2605-24197:start -->
<!-- existing:SF-2026-ARXIV-2605-24197:start -->正文已覆盖 coordination state、identity/delegation、shared-state commit、verification 与 topology cost。 本 family 的具体机制 `We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24197:end -->
<!-- delta:SF-2026-ARXIV-2605-24197:start -->We study a class of emergent misalignment in multi-agent systems (MAS), with a focus on automated workflows, which we refer to agentic misalignment.<!-- delta:SF-2026-ARXIV-2605-24197:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=790fbd7fa453181af6ae4c0885cecf49590beecc162a4d9b3a8ea9f8823d0fd3。
<!-- books-review:SF-2026-ARXIV-2605-24197:end -->
<!-- books-review:SF-2026-ARXIV-2605-24202:start -->
<!-- existing:SF-2026-ARXIV-2605-24202:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24202:end -->
<!-- delta:SF-2026-ARXIV-2605-24202:start -->We study when end-to-end RL training of multi-agent LLM workflows improves over their base models, comparing Shared-Policy training, where all roles update one policy, with Isolated-Policy training, where each role has its own parameters.<!-- delta:SF-2026-ARXIV-2605-24202:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-24202:end -->
<!-- books-review:SF-2026-ARXIV-2605-24213:start -->
<!-- existing:SF-2026-ARXIV-2605-24213:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24213:end -->
<!-- delta:SF-2026-ARXIV-2605-24213:start -->We present an empirical study of 57 evaluation harnesses, deriving a five-stage harness model and classifying 16,560 issues by workflow stage and root cause.<!-- delta:SF-2026-ARXIV-2605-24213:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24213:end -->
<!-- books-review:SF-2026-ARXIV-2605-24216:start -->
<!-- existing:SF-2026-ARXIV-2605-24216:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24216:end -->
<!-- delta:SF-2026-ARXIV-2605-24216:start -->We propose \textbf{Agent-ToM}, a learning-to-monitor framework grounded in Theory-of-Mind (ToM) reasoning for security analysis of autonomous agents.<!-- delta:SF-2026-ARXIV-2605-24216:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24216:end -->
<!-- books-review:SF-2026-ARXIV-2605-24217:start -->
<!-- existing:SF-2026-ARXIV-2605-24217:start -->现有 Evaluation 章尚未把 benchmark client 自身的单进程排队偏差纳入 TTFT/TPOT measurement identity。<!-- existing:SF-2026-ARXIV-2605-24217:end -->
<!-- delta:SF-2026-ARXIV-2605-24217:start -->We demonstrate that widely used benchmarking utilities rely on single-process, asyncio-driven architectures that introduce fundamental client-side queuing bottlenecks under high concurrency.<!-- delta:SF-2026-ARXIV-2605-24217:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24217:end -->
<!-- books-review:SF-2026-ARXIV-2605-24219:start -->
<!-- existing:SF-2026-ARXIV-2605-24219:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24219:end -->
<!-- delta:SF-2026-ARXIV-2605-24219:start -->We present Trajel, a dataset and evaluation framework for auditing trajectory-level hallucinations in multi-agent industrial workflows.<!-- delta:SF-2026-ARXIV-2605-24219:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24219:end -->
<!-- books-review:SF-2026-ARXIV-2605-24220:start -->
<!-- existing:SF-2026-ARXIV-2605-24220:start -->正文已覆盖 rubric/reward ownership、on-policy freshness、teacher/evidence boundary 与 trajectory credit。 本 family 的具体机制 `This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24220:end -->
<!-- delta:SF-2026-ARXIV-2605-24220:start -->This decoupled design makes Polar agnostic to agent harnesses, training infrastructure, and RL algorithms while improving compute utilization for long-running agent workloads.<!-- delta:SF-2026-ARXIV-2605-24220:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=1399c1280771b79bb05afde8ddf4551654c2f7ab47c9654a799131a117ca3e09。
<!-- books-review:SF-2026-ARXIV-2605-24220:end -->
<!-- books-review:SF-2026-ARXIV-2605-24229:start -->
<!-- existing:SF-2026-ARXIV-2605-24229:start -->现有 Evaluation 章缺少将长篇 policy/constitution 分解为 versioned atomic tenets，并在多轮对抗压力下审计 adherence 的闭环。<!-- existing:SF-2026-ARXIV-2605-24229:end -->
<!-- delta:SF-2026-ARXIV-2605-24229:start -->We propose a multi-method audit pipeline that treats each lab's published specification as an auditable target: it decomposes the specification into atomic testable tenets (205 for Anthropic, 197 for OpenAI), generates multi-turn adversarial scenarios with the Petri auditing agent (Anthropic, 2025b), runs a modified SURF-style rubric search (Murray et al., 2026) to catch shallow single-turn failures Petri misses, validates flagged transcripts against the relevant specification, and compares the findings against the lab's own published system card.<!-- delta:SF-2026-ARXIV-2605-24229:end --> Independent decision=`Integrate`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24229:end -->
<!-- books-review:SF-2026-ARXIV-2605-24245:start -->
<!-- existing:SF-2026-ARXIV-2605-24245:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24245:end -->
<!-- delta:SF-2026-ARXIV-2605-24245:start -->We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia.<!-- delta:SF-2026-ARXIV-2605-24245:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24245:end -->
<!-- books-review:SF-2026-ARXIV-2605-24247:start -->
<!-- existing:SF-2026-ARXIV-2605-24247:start -->正文已覆盖 data lineage、poisoning/contamination、specification compilation 与 golden-data governance。 本 family 的具体机制 `We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24247:end -->
<!-- delta:SF-2026-ARXIV-2605-24247:start -->We propose and demonstrate the efficacy of an AI-driven workflow in which AI helps write a per-category constitution that defines the label in enough detail to cover edge cases, and a frontier LLM interprets it on each input to produce the golden label more consistently and accurately than humans reading the same document.<!-- delta:SF-2026-ARXIV-2605-24247:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=6a791d1111cd7019627ea79d0c2c9be8cc4ca30ec72dbb295553428a5250f5c1。
<!-- books-review:SF-2026-ARXIV-2605-24247:end -->
<!-- books-review:SF-2026-ARXIV-2605-24248:start -->
<!-- existing:SF-2026-ARXIV-2605-24248:start -->现有 MCP 章说明 authorization 不等于 trust，但未给出 server identity、tool allowlist、sensitivity 与 attestation root 的 admission contract。<!-- existing:SF-2026-ARXIV-2605-24248:end -->
<!-- delta:SF-2026-ARXIV-2605-24248:start -->We give the wire format, the verification algorithm, a security analysis, and an LLM-driven adversarial evaluation; we then state the design in normative Request-for-Comments (RFC 2119) form -- schema, verification rules, error registry, well-known registration, and machine-checkable conformance vectors -- so it can be adopted as an MCP addendum rather than reinvented.<!-- delta:SF-2026-ARXIV-2605-24248:end --> Independent decision=`Integrate`；owner_sha256=49fbcf4975553049fa6fbcf81baf5b91d04ff47dd5faa14191df42827025fc76。
<!-- books-review:SF-2026-ARXIV-2605-24248:end -->
<!-- books-review:SF-2026-ARXIV-2605-24259:start -->
<!-- existing:SF-2026-ARXIV-2605-24259:start -->现有 KV lifecycle 没有把 future-reuse intent、materialization predicate、active/resident feasibility 与 telemetry 合成可移植 conformance claim。<!-- existing:SF-2026-ARXIV-2605-24259:end -->
<!-- delta:SF-2026-ARXIV-2605-24259:start -->We introduce resident KV claims, a conformance contract that binds future-reuse intent to a materialization predicate, lifecycle state, active/resident feasibility outcome, and claim-level telemetry.<!-- delta:SF-2026-ARXIV-2605-24259:end --> Independent decision=`Integrate`；owner_sha256=322a087f0629a6acc48fc085f83172b753f8fa38a54f182e7b9d5f8d36b02348。
<!-- books-review:SF-2026-ARXIV-2605-24259:end -->
<!-- books-review:SF-2026-ARXIV-2605-24279:start -->
<!-- existing:SF-2026-ARXIV-2605-24279:start -->现有 Context 章没有把长会话 compaction 后的 persona/role drift 作为可 fork、可重放的 deployment-state evaluation。<!-- existing:SF-2026-ARXIV-2605-24279:end -->
<!-- delta:SF-2026-ARXIV-2605-24279:start -->We introduce ContextEcho, a benchmark and reusable harness for measuring persona drift at deployment scale.<!-- delta:SF-2026-ARXIV-2605-24279:end --> Independent decision=`Integrate`；owner_sha256=55db3e124881a0bcde65d0587c9c31fa32ada720f92e5a0fc530cbb77952a53d。
<!-- books-review:SF-2026-ARXIV-2605-24279:end -->
<!-- books-review:SF-2026-ARXIV-2605-24286:start -->
<!-- existing:SF-2026-ARXIV-2605-24286:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24286:end -->
<!-- delta:SF-2026-ARXIV-2605-24286:start -->We study CoT faithfulness through a structural information-flow perspective: faithful reasoning should route answer-relevant information through the mediated path from prompt to CoT to answer, rather than through a direct prompt-to-answer shortcut.<!-- delta:SF-2026-ARXIV-2605-24286:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24286:end -->
<!-- books-review:SF-2026-ARXIV-2605-24299:start -->
<!-- existing:SF-2026-ARXIV-2605-24299:start -->正文已覆盖 Evaluation Identity、trajectory、judge budget、confidence/calibration、policy-bound sensor 与 evidence/release gate。 本 family 的具体机制 `Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24299:end -->
<!-- delta:SF-2026-ARXIV-2605-24299:start -->Confidence-weighted routing, selective abstention, and ensemble weighting all assume that a model's stated confidence is informative about its capability on the question being asked.<!-- delta:SF-2026-ARXIV-2605-24299:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=2d996d80d292f4f17ab2ef9ecd57033f53ee34128f8ddad48df2fcce7e1c1f9d。
<!-- books-review:SF-2026-ARXIV-2605-24299:end -->
<!-- books-review:SF-2026-ARXIV-2605-24309:start -->
<!-- existing:SF-2026-ARXIV-2605-24309:start -->正文已覆盖 policy-bound sensor、supply-chain、prompt/tool authority、shared-state privacy 与 human approval；只有改变边界对象或 admission 权限的证据才需追加。 本 family 的具体机制 `Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations.` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-24309:end -->
<!-- delta:SF-2026-ARXIV-2605-24309:start -->Third, we propose a three-direction research agenda and call for AHI security to be recognized as a first-class research citizen, one that demands its own design principles, evaluation methods, and theoretical foundations.<!-- delta:SF-2026-ARXIV-2605-24309:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=40095d409cb4bf91595d96c61e60d528b79b073488677723402dd3c23057bb9f。
<!-- books-review:SF-2026-ARXIV-2605-24309:end -->
<!-- books-review:SF-2026-ARXIV-2605-24312:start -->
<!-- existing:SF-2026-ARXIV-2605-24312:start -->现有 RAG 安全叙述未明确输出蕴含信号可在低查询预算下泄露 corpus membership。<!-- existing:SF-2026-ARXIV-2605-24312:end -->
<!-- delta:SF-2026-ARXIV-2605-24312:start -->However, this design introduces a new privacy risk: model outputs may signal the presence of specific documents in the retrieval corpus, enabling membership inference attacks (MIAs) that leak sensitive information.<!-- delta:SF-2026-ARXIV-2605-24312:end --> Independent decision=`Integrate`；owner_sha256=3011c1f900fd57c3767efb22ef3cd9b180fd95ace4e1c157c325d229ff114c83。
<!-- books-review:SF-2026-ARXIV-2605-24312:end -->
<!-- books-review:SF-2026-ARXIV-2605-26147:start -->
<!-- existing:SF-2026-ARXIV-2605-26147:start -->正文已覆盖 workload-aware admission、placement、batch cost、SLO 与 fallback。 本 family 的具体机制 `We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG).` 未越过该边界。<!-- existing:SF-2026-ARXIV-2605-26147:end -->
<!-- delta:SF-2026-ARXIV-2605-26147:start -->We introduce \textbf{Neural Bayesian Sequential Routing (NBSR)}, a framework that models neural inference as active evidence accumulation over a hierarchical Directed Acyclic Graph (DAG).<!-- delta:SF-2026-ARXIV-2605-26147:end --> Independent decision=`No Change — Existing Coverage`；owner_sha256=a817082692581cba1335fa8e8a4579b523cd18de6cf7126ba49dad39e377cea1。
<!-- books-review:SF-2026-ARXIV-2605-26147:end -->
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

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260523-COVERAGE | fresh-context:may2026-day01 | coverage | coverage:SRC-ARXIV:20260523 | none | semantic-independent-audit.json#scope.coverage | passed |
| SA-20260523-EVIDENCE | fresh-context:may2026-day01 | evidence | review:SF-2026-ARXIV-2605-23157 | none | semantic-independent-audit.json#scope.evidence | passed |
| SA-20260523-SELECTION | fresh-context:may2026-day01 | deep_analysis_selection | analysis:DA-SPLIT-INFERENCE-PRIVACY | none | semantic-independent-audit.json#scope.deep_analysis_selection | passed |
| SA-20260523-BOOKS | fresh-context:root-non-author-non-writer | books | books-review:SF-2026-ARXIV-2605-23158; books-review:SF-2026-ARXIV-2605-24312 | none | day01 froze the 13-item queue；root independently verified 13/13 canonical owner placement, chapter flow, evolution chain, trade-off, failure, fallback and exact-v1 boundary；receipt=`post-write-semantic-audit.json` | passed |

Cross-model skipped: non-interactive subagent context。

## 8. Ignored Noise

447 条 family-specific pre-denominator closure 保存在 `screening-ledger-final.json`；每条保留具体 title/abstract 机制、排除边界与重开条件。

## 9. Recommended Action

本日不再有待执行动作。不同 reviewer 已顺读 `BOOKS_WRITEBACK_QUEUE.json` 的 13 项及 owner+adjacent；13/13 的实际机制、演进位置、trade-off、failure、fallback 与证据边界均通过，而非 marker-only 验收。

## 10. Repository Changes

- 重建 05-23 independent screening ledger、61 项 exact-v1 receipt、current Books comparison、13 项 root writeback queue、semantic audit 与空 Materials Request。
- 13 项已按 owner 写入 8 个 Books 章节的 canonical mechanism spine；queue 已标记 `post_write_semantic_audit_passed`。
- 新增 `post-write-semantic-audit.json`；queue 13/13 已更新为 `post_write_semantic_audit_passed`。
- 未 stage、commit 或 push。

## 11. Open Questions

- 无。13/13 已通过不同 reviewer 对 owner+adjacent 的 post-write semantic audit。

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 12. Sources

- [Same Model, Different Weakness: How Language and Modality Reshape the Jailbreak Attack Surface in Frontier MLLMs](https://arxiv.org/html/2605.23157v1) — arXiv:2605.23157v1；first-public 2026-05-22；accessed 2026-09-01
- [What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference](https://arxiv.org/html/2605.23158v1) — arXiv:2605.23158v1；first-public 2026-05-22；accessed 2026-09-01
- [PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs](https://arxiv.org/html/2605.23168v1) — arXiv:2605.23168v1；first-public 2026-05-22；accessed 2026-09-01
- [Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks](https://arxiv.org/html/2605.23170v1) — arXiv:2605.23170v1；first-public 2026-05-22；accessed 2026-09-01
- [Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers](https://arxiv.org/html/2605.23196v1) — arXiv:2605.23196v1；first-public 2026-05-22；accessed 2026-09-01
- [Adaptive Mass-Segmented KV Compression for Long-Context Reasoning](https://arxiv.org/html/2605.23200v1) — arXiv:2605.23200v1；first-public 2026-05-22；accessed 2026-09-01
- [FastKernels: Benchmarking GPU Kernel Generation in Production](https://arxiv.org/html/2605.23215v1) — arXiv:2605.23215v1；first-public 2026-05-22；accessed 2026-09-01
- [Foundation Protocol: A Coordination Layer for Agentic Society](https://arxiv.org/html/2605.23218v1) — arXiv:2605.23218v1；first-public 2026-05-22；accessed 2026-09-01
- [WMAttack: Automated Attack Search for Adversarial Evaluation of World-Model Agents](https://arxiv.org/html/2605.23220v1) — arXiv:2605.23220v1；first-public 2026-05-22；accessed 2026-09-01
- [A Simple Plug-in for Improving Eviction-Based KV Cache Compression](https://arxiv.org/html/2605.23258v1) — arXiv:2605.23258v1；first-public 2026-05-22；accessed 2026-09-01
- [Designing Benchmarks for Knowledge Work](https://arxiv.org/html/2605.23262v1) — arXiv:2605.23262v1；first-public 2026-05-22；accessed 2026-09-01
- [NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference](https://arxiv.org/html/2605.23294v1) — arXiv:2605.23294v1；first-public 2026-05-22；accessed 2026-09-01
- [Parallel Context Compaction for Long-Horizon LLM Agent Serving](https://arxiv.org/html/2605.23296v1) — arXiv:2605.23296v1；first-public 2026-05-22；accessed 2026-09-01
- [DART: Semantic Recoverability for Structured Tool Agents](https://arxiv.org/html/2605.23311v1) — arXiv:2605.23311v1；first-public 2026-05-22；accessed 2026-09-01
- [CWind: A Cross-site Router for Large Language Model Inference Serving at Renewable Energy Farms](https://arxiv.org/html/2605.23348v1) — arXiv:2605.23348v1；first-public 2026-05-22；accessed 2026-09-01
- [Instance-Optimal Estimation with Multiple LLM Judges on a Budget](https://arxiv.org/html/2605.23362v1) — arXiv:2605.23362v1；first-public 2026-05-22；accessed 2026-09-01
- [AlignedServe: Orchestrating Prefix-aware Batching to Build a High-throughput and Computing-efficient LLM Serving System](https://arxiv.org/html/2605.23389v1) — arXiv:2605.23389v1；first-public 2026-05-22；accessed 2026-09-01
- [When Planning Fails Despite Correct Execution: On Epistemic Calibration for LLM-Based Multi-Agent Systems](https://arxiv.org/html/2605.23414v1) — arXiv:2605.23414v1；first-public 2026-05-22；accessed 2026-09-01
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/html/2605.23454v1) — arXiv:2605.23454v1；first-public 2026-05-22；accessed 2026-09-01
- [Unextractable Protocol Models: Collaborative Training and Inference without Weight Materialization](https://arxiv.org/html/2605.23464v1) — arXiv:2605.23464v1；first-public 2026-05-22；accessed 2026-09-01
- [EDGE-OPD: Internalizing Privileged Context with Evidence Guided On-Policy Distillation](https://arxiv.org/html/2605.23493v1) — arXiv:2605.23493v1；first-public 2026-05-22；accessed 2026-09-01
- [Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents](https://arxiv.org/html/2605.23574v1) — arXiv:2605.23574v1；first-public 2026-05-22；accessed 2026-09-01
- [Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents](https://arxiv.org/html/2605.23590v1) — arXiv:2605.23590v1；first-public 2026-05-22；accessed 2026-09-01
- [How Hard is it to Rig a Benchmark? A Social Choice Analysis of Leaderboard Robustness](https://arxiv.org/html/2605.23628v1) — arXiv:2605.23628v1；first-public 2026-05-22；accessed 2026-09-01
- [CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference](https://arxiv.org/html/2605.23640v1) — arXiv:2605.23640v1；first-public 2026-05-22；accessed 2026-09-01
- [OpenSkillEval: Automatically Auditing the Open Skill Ecosystem for LLM Agents](https://arxiv.org/html/2605.23657v1) — arXiv:2605.23657v1；first-public 2026-05-22；accessed 2026-09-01
- [Metadata Predictability Is Not Evidence Dependence: An Intervention-Based Audit for Weak-Label Benchmarks](https://arxiv.org/html/2605.23701v1) — arXiv:2605.23701v1；first-public 2026-05-22；accessed 2026-09-01
- [MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection](https://arxiv.org/html/2605.23723v1) — arXiv:2605.23723v1；first-public 2026-05-22；accessed 2026-09-01
- [HyperParallel-MoE: Multi-Core Interleaved Scheduling for Fast MoE Training on Ascend NPUs](https://arxiv.org/html/2605.23764v1) — arXiv:2605.23764v1；first-public 2026-05-22；accessed 2026-09-01
- [Point Tracking Improves World Action Models](https://arxiv.org/html/2605.23856v1) — arXiv:2605.23856v1；first-public 2026-05-22；accessed 2026-09-01
- [Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](https://arxiv.org/html/2605.23893v1) — arXiv:2605.23893v1；first-public 2026-05-22；accessed 2026-09-01
- [From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills](https://arxiv.org/html/2605.23899v1) — arXiv:2605.23899v1；first-public 2026-05-22；accessed 2026-09-01
- [SkillOpt: Executive Strategy for Self-Evolving Agent Skills](https://arxiv.org/html/2605.23904v1) — arXiv:2605.23904v1；first-public 2026-05-22；accessed 2026-09-01
- [Same Ranking, Different Winner: How Scoring Targets Shape LLM Memory Benchmarks](https://arxiv.org/html/2605.24060v1) — arXiv:2605.24060v1；first-public 2026-05-22；accessed 2026-09-01
- [When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents](https://arxiv.org/html/2605.24069v1) — arXiv:2605.24069v1；first-public 2026-05-22；accessed 2026-09-01
- [SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills](https://arxiv.org/html/2605.24117v1) — arXiv:2605.24117v1；first-public 2026-05-22；accessed 2026-09-01
- [ProofAgent Harness: Open Infrastructure for Adversarial Evaluation of AI Agents](https://arxiv.org/html/2605.24134v1) — arXiv:2605.24134v1；first-public 2026-05-22；accessed 2026-09-01
- [Palette: A Modular, Controllable, and Efficient Framework for On-demand Authorized Safety Alignment Relaxation in LLMs](https://arxiv.org/html/2605.24154v1) — arXiv:2605.24154v1；first-public 2026-05-22；accessed 2026-09-01
- [Inference Time Context Sparsity: Illusion or Opportunity?](https://arxiv.org/html/2605.24168v1) — arXiv:2605.24168v1；first-public 2026-05-22；accessed 2026-09-01
- [AvalancheBench: Evaluating Enterprise Data Agents Through Latent World Recovery](https://arxiv.org/html/2605.24183v1) — arXiv:2605.24183v1；first-public 2026-05-22；accessed 2026-09-01
- [A Sober Look at Agentic Misalignment in Automated Workflows](https://arxiv.org/html/2605.24197v1) — arXiv:2605.24197v1；first-public 2026-05-22；accessed 2026-09-01
- [When Does Multi-Agent RL Improve LLM Workflows? Workflow, Scale, and Policy-Sharing Tradeoffs](https://arxiv.org/html/2605.24202v1) — arXiv:2605.24202v1；first-public 2026-05-22；accessed 2026-09-01
- [Towards Evaluation Engineering: An Empirical Study of ML Evaluation Harnesses in the Wild](https://arxiv.org/html/2605.24213v1) — arXiv:2605.24213v1；first-public 2026-05-22；accessed 2026-09-01
- [Agent-ToM: Learning to Monitor Autonomous LLM Agents via Theory-of-Mind Reasoning](https://arxiv.org/html/2605.24216v1) — arXiv:2605.24216v1；first-public 2026-05-22；accessed 2026-09-01
- [Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks](https://arxiv.org/html/2605.24217v1) — arXiv:2605.24217v1；first-public 2026-05-22；accessed 2026-09-01
- [Beyond Final Answers: Auditing Trajectory-Level Hallucinations in Multi-Agent Industrial Workflows](https://arxiv.org/html/2605.24219v1) — arXiv:2605.24219v1；first-public 2026-05-22；accessed 2026-09-01
- [Polar: Agentic RL on Any Harness at Scale](https://arxiv.org/html/2605.24220v1) — arXiv:2605.24220v1；first-public 2026-05-22；accessed 2026-09-01
- [How Well Do Models Follow Their Constitutions?](https://arxiv.org/html/2605.24229v1) — arXiv:2605.24229v1；first-public 2026-05-22；accessed 2026-09-01
- [Deep-Research Agents Can Be Poisoned via User-Generated Content](https://arxiv.org/html/2605.24245v1) — arXiv:2605.24245v1；first-public 2026-05-22；accessed 2026-09-01
- [Improving Labeling Consistency with Detailed Constitutional Definitions and AI-Driven Evaluation](https://arxiv.org/html/2605.24247v1) — arXiv:2605.24247v1；first-public 2026-05-22；accessed 2026-09-01
- [Attested Tool-Server Admission: A Security Extension to the Model Context Protocol](https://arxiv.org/html/2605.24248v1) — arXiv:2605.24248v1；first-public 2026-05-22；accessed 2026-09-01
- [Resident KV Claims: A Conformance Contract for Future Reuse under Active KV Pressure](https://arxiv.org/html/2605.24259v1) — arXiv:2605.24259v1；first-public 2026-05-22；accessed 2026-09-01
- [ContextEcho: A Benchmark for Persona Drift in Long Agentic-Coding Sessions](https://arxiv.org/html/2605.24279v1) — arXiv:2605.24279v1；first-public 2026-05-22；accessed 2026-09-01
- [Faithfulness as Information Flow: Evaluating and Training Faithful Chain-of-Thought Reasoning](https://arxiv.org/html/2605.24286v1) — arXiv:2605.24286v1；first-public 2026-05-22；accessed 2026-09-01
- [LLMs Show No Signs Of Individuated Metacognition](https://arxiv.org/html/2605.24299v1) — arXiv:2605.24299v1；first-public 2026-05-22；accessed 2026-09-01
- [Reframing LLM Agent Security as an Agent-Human Interaction Problem](https://arxiv.org/html/2605.24309v1) — arXiv:2605.24309v1；first-public 2026-05-22；accessed 2026-09-01
- [Five Queries Are Enough: Query-Efficient and Surrogate-Free Membership Inference Attacks on RAG via Entailment](https://arxiv.org/html/2605.24312v1) — arXiv:2605.24312v1；first-public 2026-05-22；accessed 2026-09-01
- [Neural Bayesian Sequential Routing](https://arxiv.org/html/2605.26147v1) — arXiv:2605.26147v1；first-public 2026-05-22；accessed 2026-09-01
- [FD-RAG: Federated Dual-System Retrieval-Augmented Generation](https://arxiv.org/html/2605.27432v1) — arXiv:2605.27432v1；first-public 2026-05-22；accessed 2026-09-01
- [When NPUs Are Not Always Faster: A Stage-Level Analysis of Mobile LLM Inference](https://arxiv.org/html/2605.27435v1) — arXiv:2605.27435v1；first-public 2026-05-22；accessed 2026-09-01
- [MGRetrieval: Memory-Guided Reflective Retrieval for Long-Term Dialogue Agents](https://arxiv.org/html/2605.27437v1) — arXiv:2605.27437v1；first-public 2026-05-22；accessed 2026-09-01

## 13. Final Status

Completion Status: `Complete`

Coverage: `Closed`

Evidence: `Passed`

Books: `Passed`

unresolved findings: 0

05-23 已完成 13/13 串行 Books 写回与不同 reviewer post-write semantic audit：508/508、61/61 exact-v1、ordinary pending=0、blocked=0、13/13 semantic pass，Daily 全链路闭合。
