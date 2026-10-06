# Daily Research — 2026-03-24

**Research Date:** 2026-03-24

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-23 09:00:00 ～ 2026-03-24 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=1102/1102/1102；denominator=34、pre-denominator closures=1068。exact-v1 Review complete=34、blocked=0；Integrate 建议=1。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-24 |
| Window End | 2026-03-24 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260324-AUTHOR-34 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-23T09:00:00+08:00 | 2026-03-24T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 1102/1102 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 1102 | SF-2026-ARXIV-2603-20216;SF-2026-ARXIV-2603-20217;SF-2026-ARXIV-2603-20218;SF-2026-ARXIV-2603-20219;SF-2026-ARXIV-2603-20356;SF-2026-ARXIV-2603-20357;SF-2026-ARXIV-2603-20586;SF-2026-ARXIV-2603-20616;SF-2026-ARXIV-2603-20625;SF-2026-ARXIV-2603-20711;SF-2026-ARXIV-2603-20953;SF-2026-ARXIV-2603-21019;SF-2026-ARXIV-2603-21104;SF-2026-ARXIV-2603-21177;SF-2026-ARXIV-2603-21257;SF-2026-ARXIV-2603-21331;SF-2026-ARXIV-2603-21340;SF-2026-ARXIV-2603-21354;SF-2026-ARXIV-2603-21383;SF-2026-ARXIV-2603-21465;SF-2026-ARXIV-2603-21522;SF-2026-ARXIV-2603-21523;SF-2026-ARXIV-2603-21564;SF-2026-ARXIV-2603-21576;SF-2026-ARXIV-2603-21641;SF-2026-ARXIV-2603-21642;SF-2026-ARXIV-2603-21692;SF-2026-ARXIV-2603-21862;SF-2026-ARXIV-2603-22075;SF-2026-ARXIV-2603-22078;SF-2026-ARXIV-2603-22206;SF-2026-ARXIV-2603-22212;SF-2026-ARXIV-2603-22276;SF-2026-ARXIV-2603-22286 | pages=100; prefixes=00..99; final_cursor=end; registered=1102; screened=1102; retained=34; closure=1068 | 2026-03-24T01:00:00+00:00 | screening-ledger-final.json#sha256=e3c091cc9e38f820baeaee78f5fd1d614eb46a77db6bb790182f1cded6e936fe; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260324:start -->作者侧已逐项筛选全部 1102 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260324:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-20216 | arXiv:2603.20216v1 | paper-v1:2603.20216 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20216 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20216 | no |
| SF-2026-ARXIV-2603-20217 | arXiv:2603.20217v1 | paper-v1:2603.20217 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20217 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20217 | no |
| SF-2026-ARXIV-2603-20218 | arXiv:2603.20218v1 | paper-v1:2603.20218 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20218 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20218 | no |
| SF-2026-ARXIV-2603-20219 | arXiv:2603.20219v1 | paper-v1:2603.20219 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20219 | self | — | new_in_window | MODEL-DECODER-ONLY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20219 | no |
| SF-2026-ARXIV-2603-20356 | arXiv:2603.20356v1 | paper-v1:2603.20356 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20356 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20356 | no |
| SF-2026-ARXIV-2603-20357 | arXiv:2603.20357v1 | paper-v1:2603.20357 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20357 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20357 | no |
| SF-2026-ARXIV-2603-20586 | arXiv:2603.20586v1 | paper-v1:2603.20586 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20586 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20586 | no |
| SF-2026-ARXIV-2603-20616 | arXiv:2603.20616v1 | paper-v1:2603.20616 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20616 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20616 | no |
| SF-2026-ARXIV-2603-20625 | arXiv:2603.20625v1 | paper-v1:2603.20625 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20625 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20625 | no |
| SF-2026-ARXIV-2603-20711 | arXiv:2603.20711v1 | paper-v1:2603.20711 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20711 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20711 | no |
| SF-2026-ARXIV-2603-20953 | arXiv:2603.20953v1 | paper-v1:2603.20953 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20953 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20953 | no |
| SF-2026-ARXIV-2603-21019 | arXiv:2603.21019v1 | paper-v1:2603.21019 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21019 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21019 | no |
| SF-2026-ARXIV-2603-21104 | arXiv:2603.21104v1 | paper-v1:2603.21104 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21104 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21104 | no |
| SF-2026-ARXIV-2603-21177 | arXiv:2603.21177v1 | paper-v1:2603.21177 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21177 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2603-21177 | no |
| SF-2026-ARXIV-2603-21257 | arXiv:2603.21257v1 | paper-v1:2603.21257 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21257 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21257 | no |
| SF-2026-ARXIV-2603-21331 | arXiv:2603.21331v1 | paper-v1:2603.21331 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21331 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21331 | no |
| SF-2026-ARXIV-2603-21340 | arXiv:2603.21340v1 | paper-v1:2603.21340 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | disputed | none | review:SF-2026-ARXIV-2603-21340 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Disputed | books-review:SF-2026-ARXIV-2603-21340 | no |
| SF-2026-ARXIV-2603-21354 | arXiv:2603.21354v1 | paper-v1:2603.21354 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21354 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21354 | no |
| SF-2026-ARXIV-2603-21383 | arXiv:2603.21383v1 | paper-v1:2603.21383 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-21383 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21383 | no |
| SF-2026-ARXIV-2603-21465 | arXiv:2603.21465v1 | paper-v1:2603.21465 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21465 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21465 | no |
| SF-2026-ARXIV-2603-21522 | arXiv:2603.21522v1 | paper-v1:2603.21522 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21522 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21522 | no |
| SF-2026-ARXIV-2603-21523 | arXiv:2603.21523v1 | paper-v1:2603.21523 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21523 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21523 | no |
| SF-2026-ARXIV-2603-21564 | arXiv:2603.21564v1 | paper-v1:2603.21564 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21564 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21564 | no |
| SF-2026-ARXIV-2603-21576 | arXiv:2603.21576v1 | paper-v1:2603.21576 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21576 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21576 | no |
| SF-2026-ARXIV-2603-21641 | arXiv:2603.21641v1 | paper-v1:2603.21641 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21641 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21641 | no |
| SF-2026-ARXIV-2603-21642 | arXiv:2603.21642v1 | paper-v1:2603.21642 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21642 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21642 | no |
| SF-2026-ARXIV-2603-21692 | arXiv:2603.21692v1 | paper-v1:2603.21692 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21692 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21692 | no |
| SF-2026-ARXIV-2603-21862 | arXiv:2603.21862v1 | paper-v1:2603.21862 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-21862 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21862 | no |
| SF-2026-ARXIV-2603-22075 | arXiv:2603.22075v1 | paper-v1:2603.22075 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22075 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22075 | no |
| SF-2026-ARXIV-2603-22078 | arXiv:2603.22078v1 | paper-v1:2603.22078 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22078 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22078 | no |
| SF-2026-ARXIV-2603-22206 | arXiv:2603.22206v1 | paper-v1:2603.22206 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22206 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22206 | no |
| SF-2026-ARXIV-2603-22212 | arXiv:2603.22212v1 | paper-v1:2603.22212 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22212 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22212 | no |
| SF-2026-ARXIV-2603-22276 | arXiv:2603.22276v1 | paper-v1:2603.22276 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22276 | self | — | new_in_window | TRAIN-LORA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22276 | no |
| SF-2026-ARXIV-2603-22286 | arXiv:2603.22286v1 | paper-v1:2603.22286 | 2026-W13 | 2026-03-24 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22286 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22286 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-20216 | RP-b8f3afb10c179140 | deep | arXiv:2603.20216v1 | SRC-ARXIV@arXiv:2603.20216v1 | arXiv:2603.20216v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.20216v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20216v1.html; sha256:49c909ce396bc25b54b9d4eec6aae5067d1fbc8dd281920b23c5b9204b4dfb7b | arXiv:2603.20216v1 HTML — §A.2 Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.20216v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20216v1.html; sha256:49c909ce396bc25b54b9d4eec6aae5067d1fbc8dd281920b23c5b9204b4dfb7b | arXiv:2603.20216v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.20216v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20216v1.html; sha256:49c909ce396bc25b54b9d4eec6aae5067d1fbc8dd281920b23c5b9204b4dfb7b | arXiv exact-v1 identity https://arxiv.org/abs/2603.20216v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20216 | complete |
| SF-2026-ARXIV-2603-20217 | RP-dd36b0c67958f938 | deep | arXiv:2603.20217v1 | SRC-ARXIV@arXiv:2603.20217v1 | arXiv:2603.20217v1 HTML — §Model Routing Methods. [facet=method]; https://arxiv.org/html/2603.20217v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20217v1.html; sha256:efd0a666d03531f0adfb0464d05b72931a4c3ac75aa9a9f84a1fe4205ede0c59 | arXiv:2603.20217v1 HTML — §Routing Evaluations. [facet=evaluation]; https://arxiv.org/html/2603.20217v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20217v1.html; sha256:efd0a666d03531f0adfb0464d05b72931a4c3ac75aa9a9f84a1fe4205ede0c59 | arXiv:2603.20217v1 HTML — §5 Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.20217v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20217v1.html; sha256:efd0a666d03531f0adfb0464d05b72931a4c3ac75aa9a9f84a1fe4205ede0c59 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20217v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20217 | complete |
| SF-2026-ARXIV-2603-20218 | RP-22992a6c5665b16d | deep | arXiv:2603.20218v1 | SRC-ARXIV@arXiv:2603.20218v1 | arXiv:2603.20218v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.20218v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20218v1.html; sha256:e8bbfebc54a26d3ced565fe2fdc3015d14a6084dad5ff2f8d935aa3961d8da57 | arXiv:2603.20218v1 HTML — §4. Experimental study [facet=evaluation]; https://arxiv.org/html/2603.20218v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20218v1.html; sha256:e8bbfebc54a26d3ced565fe2fdc3015d14a6084dad5ff2f8d935aa3961d8da57 | arXiv:2603.20218v1 HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.20218v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20218v1.html; sha256:e8bbfebc54a26d3ced565fe2fdc3015d14a6084dad5ff2f8d935aa3961d8da57 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20218v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20218 | complete |
| SF-2026-ARXIV-2603-20219 | RP-01727bad17d1f67f | deep | arXiv:2603.20219v1 | SRC-ARXIV@arXiv:2603.20219v1 | arXiv:2603.20219v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.20219v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20219v1.html; sha256:045a043b5330cfc40c2649f87e0439a69321665eae0c14298a3455953a21f4df | arXiv:2603.20219v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.20219v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20219v1.html; sha256:045a043b5330cfc40c2649f87e0439a69321665eae0c14298a3455953a21f4df | arXiv:2603.20219v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.20219v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20219v1.html; sha256:045a043b5330cfc40c2649f87e0439a69321665eae0c14298a3455953a21f4df | arXiv exact-v1 identity https://arxiv.org/abs/2603.20219v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20219 | complete |
| SF-2026-ARXIV-2603-20356 | RP-aed5017d6fa337fc | deep | arXiv:2603.20356v1 | SRC-ARXIV@arXiv:2603.20356v1 | arXiv:2603.20356v1 HTML — §4 System overview [facet=method]; https://arxiv.org/html/2603.20356v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20356v1.html; sha256:420e2f649c6d5fa4bd941987770d60ffcf9ba8830dd48449dc0dd08641b9ea04 | arXiv:2603.20356v1 HTML — §7.3 Temporal policy evaluation [facet=evaluation]; https://arxiv.org/html/2603.20356v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20356v1.html; sha256:420e2f649c6d5fa4bd941987770d60ffcf9ba8830dd48449dc0dd08641b9ea04 | arXiv:2603.20356v1 HTML — §Human-node detection limitation. [facet=limitations]; https://arxiv.org/html/2603.20356v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20356v1.html; sha256:420e2f649c6d5fa4bd941987770d60ffcf9ba8830dd48449dc0dd08641b9ea04 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20356v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20356 | complete |
| SF-2026-ARXIV-2603-20357 | RP-d178a1fe92e1fed1 | deep | arXiv:2603.20357v1 | SRC-ARXIV@arXiv:2603.20357v1 | arXiv:2603.20357v1 HTML — §3.1 Semantic memory poisoning attacks [facet=method]; https://arxiv.org/html/2603.20357v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20357v1.html; sha256:f8731ef152199259accd13c3f6f5075b083b5c3d2e9516a7445de53115b95678 | arXiv:2603.20357v1 HTML — §Mitigation strategies against semantic memory poisoning attacks [facet=evaluation]; https://arxiv.org/html/2603.20357v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20357v1.html; sha256:f8731ef152199259accd13c3f6f5075b083b5c3d2e9516a7445de53115b95678 | arXiv:2603.20357v1 HTML — §4 Conclusions [facet=limitations]; https://arxiv.org/html/2603.20357v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20357v1.html; sha256:f8731ef152199259accd13c3f6f5075b083b5c3d2e9516a7445de53115b95678 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20357v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20357 | complete |
| SF-2026-ARXIV-2603-20586 | RP-e0f28977f0e32be8 | deep | arXiv:2603.20586v1 | SRC-ARXIV@arXiv:2603.20586v1 | arXiv:2603.20586v1 HTML — §4. Methodology [facet=method]; https://arxiv.org/html/2603.20586v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20586v1.html; sha256:f08f886fa596dc1af176319d8182b2955a5c0251c52fda0ad93a0fe9643c2c03 | arXiv:2603.20586v1 HTML — §6.3. Experimental Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.20586v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20586v1.html; sha256:f08f886fa596dc1af176319d8182b2955a5c0251c52fda0ad93a0fe9643c2c03 | arXiv:2603.20586v1 HTML — §6.7. Discussion [facet=limitations]; https://arxiv.org/html/2603.20586v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20586v1.html; sha256:f08f886fa596dc1af176319d8182b2955a5c0251c52fda0ad93a0fe9643c2c03 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20586v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20586 | complete |
| SF-2026-ARXIV-2603-20616 | RP-a0d03488322f131a | deep | arXiv:2603.20616v1 | SRC-ARXIV@arXiv:2603.20616v1 | arXiv:2603.20616v1 HTML — §5 Implementation [facet=method]; https://arxiv.org/html/2603.20616v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20616v1.html; sha256:212f2965800229075d17b7a521198ef00e490e005ba487ebbc00f6f064c3963f | arXiv:2603.20616v1 HTML — §6.2 Main Results on Long-Context Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.20616v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20616v1.html; sha256:212f2965800229075d17b7a521198ef00e490e005ba487ebbc00f6f064c3963f | arXiv:2603.20616v1 HTML — §6.5 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.20616v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20616v1.html; sha256:212f2965800229075d17b7a521198ef00e490e005ba487ebbc00f6f064c3963f | arXiv exact-v1 identity https://arxiv.org/abs/2603.20616v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20616 | complete |
| SF-2026-ARXIV-2603-20625 | RP-63993afd8d8afd00 | deep | arXiv:2603.20625v1 | SRC-ARXIV@arXiv:2603.20625v1 | arXiv:2603.20625v1 HTML — §4. Mitigation: ACRFence [facet=method]; https://arxiv.org/html/2603.20625v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20625v1.html; sha256:c63d0648a0a18acdcbd4a10628782203a81e6a18a0093e7638ecb320538f63df | arXiv:2603.20625v1 HTML — §3. Attacks and Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.20625v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20625v1.html; sha256:c63d0648a0a18acdcbd4a10628782203a81e6a18a0093e7638ecb320538f63df | arXiv:2603.20625v1 HTML — §6. Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.20625v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20625v1.html; sha256:c63d0648a0a18acdcbd4a10628782203a81e6a18a0093e7638ecb320538f63df | arXiv exact-v1 identity https://arxiv.org/abs/2603.20625v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20625 | complete |
| SF-2026-ARXIV-2603-20711 | RP-6dd18c636301b2d4 | deep | arXiv:2603.20711v1 | SRC-ARXIV@arXiv:2603.20711v1 | arXiv:2603.20711v1 HTML — §IV RoboECC Framework [facet=method]; https://arxiv.org/html/2603.20711v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20711v1.html; sha256:0a4fc25eda92ff465e8a3089c2c8df48f33a81020557f97fce7b5f955ca056cb | arXiv:2603.20711v1 HTML — §V-B1 Results in Simulation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.20711v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20711v1.html; sha256:0a4fc25eda92ff465e8a3089c2c8df48f33a81020557f97fce7b5f955ca056cb | arXiv:2603.20711v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.20711v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20711v1.html; sha256:0a4fc25eda92ff465e8a3089c2c8df48f33a81020557f97fce7b5f955ca056cb | arXiv exact-v1 identity https://arxiv.org/abs/2603.20711v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20711 | complete |
| SF-2026-ARXIV-2603-20953 | RP-75c13589427eda9f | deep | arXiv:2603.20953v1 | SRC-ARXIV@arXiv:2603.20953v1 | arXiv:2603.20953v1 HTML — §3.2 Architecture [facet=method]; https://arxiv.org/html/2603.20953v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20953v1.html; sha256:cdfdd6a1c1147ac2c7bcdc1c49c69c775f6c4dc0e36d96d21a97baae3d8ebf1f | arXiv:2603.20953v1 HTML — §2.2 Post-Hoc Evaluation [facet=evaluation]; https://arxiv.org/html/2603.20953v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20953v1.html; sha256:cdfdd6a1c1147ac2c7bcdc1c49c69c775f6c4dc0e36d96d21a97baae3d8ebf1f | arXiv:2603.20953v1 HTML — §8.1 Limitations [facet=limitations]; https://arxiv.org/html/2603.20953v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20953v1.html; sha256:cdfdd6a1c1147ac2c7bcdc1c49c69c775f6c4dc0e36d96d21a97baae3d8ebf1f | arXiv exact-v1 identity https://arxiv.org/abs/2603.20953v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20953 | complete |
| SF-2026-ARXIV-2603-21019 | RP-143520d8fd34f586 | deep | arXiv:2603.21019v1 | SRC-ARXIV@arXiv:2603.21019v1 | arXiv:2603.21019v1 HTML — §3.4 System Implementation [facet=method]; https://arxiv.org/html/2603.21019v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21019v1.html; sha256:e2b19122a26d61f24cb89cc5e3853f6460c57e2b001357b554c1eb5c309a6aa5 | arXiv:2603.21019v1 HTML — §4.3 Large-scale Empirical Audit [facet=evaluation]; https://arxiv.org/html/2603.21019v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21019v1.html; sha256:e2b19122a26d61f24cb89cc5e3853f6460c57e2b001357b554c1eb5c309a6aa5 | arXiv:2603.21019v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2603.21019v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21019v1.html; sha256:e2b19122a26d61f24cb89cc5e3853f6460c57e2b001357b554c1eb5c309a6aa5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21019v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21019 | complete |
| SF-2026-ARXIV-2603-21104 | RP-d1e0c7d67bd9757b | deep | arXiv:2603.21104v1 | SRC-ARXIV@arXiv:2603.21104v1 | arXiv:2603.21104v1 HTML — §Implementation Details. [facet=method]; https://arxiv.org/html/2603.21104v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21104v1.html; sha256:b35ef6f4e98efbc15f7671e53dba33ba6d6c2313089d0a10a6ad53edaee0145b | arXiv:2603.21104v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.21104v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21104v1.html; sha256:b35ef6f4e98efbc15f7671e53dba33ba6d6c2313089d0a10a6ad53edaee0145b | arXiv:2603.21104v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.21104v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21104v1.html; sha256:b35ef6f4e98efbc15f7671e53dba33ba6d6c2313089d0a10a6ad53edaee0145b | arXiv exact-v1 identity https://arxiv.org/abs/2603.21104v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21104 | complete |
| SF-2026-ARXIV-2603-21177 | RP-c28038a925be3c03 | deep | arXiv:2603.21177v1 | SRC-ARXIV@arXiv:2603.21177v1 | arXiv:2603.21177v1 HTML — §Appendix B Algorithm [facet=method]; https://arxiv.org/html/2603.21177v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21177v1.html; sha256:9bb5031e7669ee1556437b78ca21adfbc4d3e5ae6fab2853a9df6a272fa26936 | arXiv:2603.21177v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.21177v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21177v1.html; sha256:9bb5031e7669ee1556437b78ca21adfbc4d3e5ae6fab2853a9df6a272fa26936 | arXiv:2603.21177v1 HTML — §6.2 Limitations & Future Work [facet=limitations]; https://arxiv.org/html/2603.21177v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21177v1.html; sha256:9bb5031e7669ee1556437b78ca21adfbc4d3e5ae6fab2853a9df6a272fa26936 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21177v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21177 | complete |
| SF-2026-ARXIV-2603-21257 | RP-af5832aa46744870 | deep | arXiv:2603.21257v1 | SRC-ARXIV@arXiv:2603.21257v1 | arXiv:2603.21257v1 HTML — §3. Solution [facet=method]; https://arxiv.org/html/2603.21257v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21257v1.html; sha256:85b681bc71313742ab85044439a467f208c21c526e27b393fc7eecca98d37fc1 | arXiv:2603.21257v1 HTML — §4.3. Micro-benchmark Analysis [facet=evaluation]; https://arxiv.org/html/2603.21257v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21257v1.html; sha256:85b681bc71313742ab85044439a467f208c21c526e27b393fc7eecca98d37fc1 | arXiv:2603.21257v1 HTML — §5. Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.21257v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21257v1.html; sha256:85b681bc71313742ab85044439a467f208c21c526e27b393fc7eecca98d37fc1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21257v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21257 | complete |
| SF-2026-ARXIV-2603-21331 | RP-f5af5afabff7d0a0 | deep | arXiv:2603.21331v1 | SRC-ARXIV@arXiv:2603.21331v1 | arXiv:2603.21331v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.21331v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21331v1.html; sha256:aef41f1cd9228a3cb49e529278270632057adfc61c976e3ba766ff57f659d22b | arXiv:2603.21331v1 HTML — §7 Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21331v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21331v1.html; sha256:aef41f1cd9228a3cb49e529278270632057adfc61c976e3ba766ff57f659d22b | arXiv:2603.21331v1 HTML — §11 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.21331v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21331v1.html; sha256:aef41f1cd9228a3cb49e529278270632057adfc61c976e3ba766ff57f659d22b | arXiv exact-v1 identity https://arxiv.org/abs/2603.21331v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21331 | complete |
| SF-2026-ARXIV-2603-21340 | RP-6c87aa8e670e7d51 | deep | arXiv:2603.21340v1 | SRC-ARXIV@arXiv:2603.21340v1 | arXiv:2603.21340v1 PDF — §3 System Architecture Overview [facet=method]; https://arxiv.org/pdf/2603.21340v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21340v1.pdf.txt; sha256:89d029d40d6913049fbb3603ea24028495bc4e4899529e2dd51fa404f0ab397e | arXiv:2603.21340v1 PDF — §11 Empirical Evaluation [facet=evaluation]; https://arxiv.org/pdf/2603.21340v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21340v1.pdf.txt; sha256:89d029d40d6913049fbb3603ea24028495bc4e4899529e2dd51fa404f0ab397e | arXiv:2603.21340v1 PDF — §12 Discussion [facet=limitations]; https://arxiv.org/pdf/2603.21340v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21340v1.pdf.txt; sha256:89d029d40d6913049fbb3603ea24028495bc4e4899529e2dd51fa404f0ab397e | arXiv exact-v1 identity https://arxiv.org/abs/2603.21340v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21340 | complete |
| SF-2026-ARXIV-2603-21354 | RP-cab67637397ff1cd | deep | arXiv:2603.21354v1 | SRC-ARXIV@arXiv:2603.21354v1 | arXiv:2603.21354v1 HTML — §2.1 Pillar 1: Routing Architecture [facet=method]; https://arxiv.org/html/2603.21354v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21354v1.html; sha256:31a0c2520506b10b895818400dd0ae7f7e799c5070b6c1a59801e105652f55b1 | arXiv:2603.21354v1 HTML — §Validated building blocks (separate systems, public benchmarks). [facet=evaluation]; https://arxiv.org/html/2603.21354v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21354v1.html; sha256:31a0c2520506b10b895818400dd0ae7f7e799c5070b6c1a59801e105652f55b1 | arXiv:2603.21354v1 HTML — §Agent serving and failure analysis. [facet=limitations]; https://arxiv.org/html/2603.21354v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21354v1.html; sha256:31a0c2520506b10b895818400dd0ae7f7e799c5070b6c1a59801e105652f55b1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21354v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21354 | complete |
| SF-2026-ARXIV-2603-21383 | RP-f71987c99e783cc2 | standard | arXiv:2603.21383v1 | SRC-ARXIV@arXiv:2603.21383v1 | arXiv:2603.21383v1 HTML — §3.1 Method [facet=method]; https://arxiv.org/html/2603.21383v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21383v1.html; sha256:6b486c3cc3bcacbe5ecb07a0d1a1fe498e2a69249d4a0ca3bdb89f3466d912f2 | arXiv:2603.21383v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.21383v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21383v1.html; sha256:6b486c3cc3bcacbe5ecb07a0d1a1fe498e2a69249d4a0ca3bdb89f3466d912f2 | arXiv:2603.21383v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.21383v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21383v1.html; sha256:6b486c3cc3bcacbe5ecb07a0d1a1fe498e2a69249d4a0ca3bdb89f3466d912f2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21383v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21383 | complete |
| SF-2026-ARXIV-2603-21465 | RP-79124234ec04f91f | deep | arXiv:2603.21465v1 | SRC-ARXIV@arXiv:2603.21465v1 | arXiv:2603.21465v1 HTML — §4 Training Pipeline [facet=method]; https://arxiv.org/html/2603.21465v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21465v1.html; sha256:878637c83e477be0fc2477e9c307b8a08ffd8c9966e7dd5bb26d0d9e48321961 | arXiv:2603.21465v1 HTML — §5.2 Results on Synthetic Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.21465v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21465v1.html; sha256:878637c83e477be0fc2477e9c307b8a08ffd8c9966e7dd5bb26d0d9e48321961 | arXiv:2603.21465v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.21465v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21465v1.html; sha256:878637c83e477be0fc2477e9c307b8a08ffd8c9966e7dd5bb26d0d9e48321961 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21465v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21465 | complete |
| SF-2026-ARXIV-2603-21522 | RP-8b4091f0dd8ec43e | deep | arXiv:2603.21522v1 | SRC-ARXIV@arXiv:2603.21522v1 | arXiv:2603.21522v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.21522v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21522v1.html; sha256:018b0fc4cdff60de08d8b734dfbd1b4c4da2ec9b35d3466dce8b300058192994 | arXiv:2603.21522v1 HTML — §2.2. Evaluation of Existing Embeddings on Reasoning Trace Representation [facet=evaluation]; https://arxiv.org/html/2603.21522v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21522v1.html; sha256:018b0fc4cdff60de08d8b734dfbd1b4c4da2ec9b35d3466dce8b300058192994 | arXiv:2603.21522v1 HTML — §2.1. Failure Pattern Concentration in Multi-Agent Systems [facet=limitations]; https://arxiv.org/html/2603.21522v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21522v1.html; sha256:018b0fc4cdff60de08d8b734dfbd1b4c4da2ec9b35d3466dce8b300058192994 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21522v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21522 | complete |
| SF-2026-ARXIV-2603-21523 | RP-3f59d97d559bff79 | deep | arXiv:2603.21523v1 | SRC-ARXIV@arXiv:2603.21523v1 | arXiv:2603.21523v1 HTML — §4. System Design [facet=method]; https://arxiv.org/html/2603.21523v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21523v1.html; sha256:5458b605fce3e390dd5d8989548197ceede4e60d60fae7f5ae433c1a627c781f | arXiv:2603.21523v1 HTML — §5. Experiments [facet=evaluation]; https://arxiv.org/html/2603.21523v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21523v1.html; sha256:5458b605fce3e390dd5d8989548197ceede4e60d60fae7f5ae433c1a627c781f | arXiv:2603.21523v1 HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.21523v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21523v1.html; sha256:5458b605fce3e390dd5d8989548197ceede4e60d60fae7f5ae433c1a627c781f | arXiv exact-v1 identity https://arxiv.org/abs/2603.21523v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21523 | complete |
| SF-2026-ARXIV-2603-21564 | RP-fbe13137a436f3f2 | deep | arXiv:2603.21564v1 | SRC-ARXIV@arXiv:2603.21564v1 | arXiv:2603.21564v1 HTML — §2.1 Core Definitions [facet=method]; https://arxiv.org/html/2603.21564v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21564v1.html; sha256:8848b8e1c2211f29d732d7a1a1c6e867127f23dc1adac38051d0bced09ea0383 | arXiv:2603.21564v1 HTML — §3.1 Data and Trace Systems [facet=evaluation]; https://arxiv.org/html/2603.21564v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21564v1.html; sha256:8848b8e1c2211f29d732d7a1a1c6e867127f23dc1adac38051d0bced09ea0383 | arXiv:2603.21564v1 HTML — §4 Discussion and Future Work [facet=limitations]; https://arxiv.org/html/2603.21564v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21564v1.html; sha256:8848b8e1c2211f29d732d7a1a1c6e867127f23dc1adac38051d0bced09ea0383 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21564v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21564 | complete |
| SF-2026-ARXIV-2603-21576 | RP-df62a5fd28c288da | deep | arXiv:2603.21576v1 | SRC-ARXIV@arXiv:2603.21576v1 | arXiv:2603.21576v1 HTML — §III.1 System Overview [facet=method]; https://arxiv.org/html/2603.21576v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21576v1.html; sha256:9fea03d9a8fcafda79c9b82286babc1f03cbd991f5df0037066a7cb1f02b323f | arXiv:2603.21576v1 HTML — §V System-Level Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21576v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21576v1.html; sha256:9fea03d9a8fcafda79c9b82286babc1f03cbd991f5df0037066a7cb1f02b323f | arXiv:2603.21576v1 HTML — §VII.1 Limitations and Practical Considerations [facet=limitations]; https://arxiv.org/html/2603.21576v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21576v1.html; sha256:9fea03d9a8fcafda79c9b82286babc1f03cbd991f5df0037066a7cb1f02b323f | arXiv exact-v1 identity https://arxiv.org/abs/2603.21576v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21576 | complete |
| SF-2026-ARXIV-2603-21641 | RP-29df8bda9d712fc0 | deep | arXiv:2603.21641v1 | SRC-ARXIV@arXiv:2603.21641v1 | arXiv:2603.21641v1 HTML — §2. Tool Architecture and Implementation [facet=method]; https://arxiv.org/html/2603.21641v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21641v1.html; sha256:9d31c161f5c335eb9b0ef1ab5f7c47b54a61623e767d6c383638ae251723b233 | arXiv:2603.21641v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21641v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21641v1.html; sha256:9d31c161f5c335eb9b0ef1ab5f7c47b54a61623e767d6c383638ae251723b233 | arXiv:2603.21641v1 HTML — §5. Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.21641v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21641v1.html; sha256:9d31c161f5c335eb9b0ef1ab5f7c47b54a61623e767d6c383638ae251723b233 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21641v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21641 | complete |
| SF-2026-ARXIV-2603-21642 | RP-9bf3c7738c0a0470 | deep | arXiv:2603.21642v1 | SRC-ARXIV@arXiv:2603.21642v1 | arXiv:2603.21642v1 HTML — §4.1. Attack Implementation [facet=method]; https://arxiv.org/html/2603.21642v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21642v1.html; sha256:0efd356d4c594fd1fd4c41fac701a42dba211e4d2dcd79d9fe4e81f8fee9c2ce | arXiv:2603.21642v1 HTML — §5. Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.21642v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21642v1.html; sha256:0efd356d4c594fd1fd4c41fac701a42dba211e4d2dcd79d9fe4e81f8fee9c2ce | arXiv:2603.21642v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.21642v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21642v1.html; sha256:0efd356d4c594fd1fd4c41fac701a42dba211e4d2dcd79d9fe4e81f8fee9c2ce | arXiv exact-v1 identity https://arxiv.org/abs/2603.21642v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21642 | complete |
| SF-2026-ARXIV-2603-21692 | RP-84161daccbce805f | deep | arXiv:2603.21692v1 | SRC-ARXIV@arXiv:2603.21692v1 | arXiv:2603.21692v1 HTML — §7 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.21692v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21692v1.html; sha256:9ce8aa2f2bd18c1bb493112d4ec8ca857b1fc0b53be6a0b8aa966e0dd3345e36 | arXiv:2603.21692v1 HTML — §7 Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.21692v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21692v1.html; sha256:9ce8aa2f2bd18c1bb493112d4ec8ca857b1fc0b53be6a0b8aa966e0dd3345e36 | arXiv:2603.21692v1 HTML — §3.3 Limitation: Self-Reported Reasoning [facet=limitations]; https://arxiv.org/html/2603.21692v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21692v1.html; sha256:9ce8aa2f2bd18c1bb493112d4ec8ca857b1fc0b53be6a0b8aa966e0dd3345e36 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21692v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21692 | complete |
| SF-2026-ARXIV-2603-21862 | RP-7e0964ede42420f3 | deep | arXiv:2603.21862v1 | SRC-ARXIV@arXiv:2603.21862v1 | arXiv:2603.21862v1 HTML — §4 Decoupling and reducing MoE scaling dimensions [facet=method]; https://arxiv.org/html/2603.21862v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21862v1.html; sha256:38e8d720a63e0ff39a846844dfbb6d38799a01878320fb6ed5f46e339ca5c058 | arXiv:2603.21862v1 HTML — §5.3 Results and scaling laws derivation [facet=evaluation]; https://arxiv.org/html/2603.21862v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21862v1.html; sha256:38e8d720a63e0ff39a846844dfbb6d38799a01878320fb6ed5f46e339ca5c058 | arXiv:2603.21862v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2603.21862v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21862v1.html; sha256:38e8d720a63e0ff39a846844dfbb6d38799a01878320fb6ed5f46e339ca5c058 | arXiv exact-v1 identity https://arxiv.org/abs/2603.21862v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-21862 | complete |
| SF-2026-ARXIV-2603-22075 | RP-4ee2d829da2aa993 | deep | arXiv:2603.22075v1 | SRC-ARXIV@arXiv:2603.22075v1 | arXiv:2603.22075v1 HTML — §3.1 Controlled Variables [facet=method]; https://arxiv.org/html/2603.22075v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22075v1.html; sha256:eeb9794bb58afc845b8942a4251376bab8a840c5627db3f7b37036cb4f6411da | arXiv:2603.22075v1 HTML — §4.3 Generation Diversity: Quantitative Analysis [facet=evaluation]; https://arxiv.org/html/2603.22075v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22075v1.html; sha256:eeb9794bb58afc845b8942a4251376bab8a840c5627db3f7b37036cb4f6411da | arXiv:2603.22075v1 HTML — §5.4 Limitations [facet=limitations]; https://arxiv.org/html/2603.22075v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22075v1.html; sha256:eeb9794bb58afc845b8942a4251376bab8a840c5627db3f7b37036cb4f6411da | arXiv exact-v1 identity https://arxiv.org/abs/2603.22075v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22075 | complete |
| SF-2026-ARXIV-2603-22078 | RP-ca7354fbd85c01de | deep | arXiv:2603.22078v1 | SRC-ARXIV@arXiv:2603.22078v1 | arXiv:2603.22078v1 HTML — §3.2 Evaluation Methods [facet=method]; https://arxiv.org/html/2603.22078v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22078v1.html; sha256:6c24b97d46efead2d9b6b71a2dfe2c00045dd8e85bbc1ff940231f5531a061d4 | arXiv:2603.22078v1 HTML — §3.2 Evaluation Methods [facet=evaluation]; https://arxiv.org/html/2603.22078v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22078v1.html; sha256:6c24b97d46efead2d9b6b71a2dfe2c00045dd8e85bbc1ff940231f5531a061d4 | arXiv:2603.22078v1 HTML — §4 Conclusion [facet=limitations]; https://arxiv.org/html/2603.22078v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22078v1.html; sha256:6c24b97d46efead2d9b6b71a2dfe2c00045dd8e85bbc1ff940231f5531a061d4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22078v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22078 | complete |
| SF-2026-ARXIV-2603-22206 | RP-c12ad7ea6be89bb9 | deep | arXiv:2603.22206v1 | SRC-ARXIV@arXiv:2603.22206v1 | arXiv:2603.22206v1 HTML — §3.8 Implementation Details [facet=method]; https://arxiv.org/html/2603.22206v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22206v1.html; sha256:0c223f09a316371310c7989d8062c7e9ae095e9061bb786e985dda9ca694827e | arXiv:2603.22206v1 HTML — §4.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.22206v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22206v1.html; sha256:0c223f09a316371310c7989d8062c7e9ae095e9061bb786e985dda9ca694827e | arXiv:2603.22206v1 HTML — §4.4 Ablations [facet=limitations]; https://arxiv.org/html/2603.22206v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22206v1.html; sha256:0c223f09a316371310c7989d8062c7e9ae095e9061bb786e985dda9ca694827e | arXiv exact-v1 identity https://arxiv.org/abs/2603.22206v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22206 | complete |
| SF-2026-ARXIV-2603-22212 | RP-3f23dc14774b29cf | deep | arXiv:2603.22212v1 | SRC-ARXIV@arXiv:2603.22212v1 | arXiv:2603.22212v1 HTML — §2.1 World Models Design [facet=method]; https://arxiv.org/html/2603.22212v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22212v1.html; sha256:5fd9b6f3e80c5ef144862efb3dc3888f77be2d1ac3dde37cbe09588dace5f3e0 | arXiv:2603.22212v1 HTML — §5.3 Quantitative Evaluation Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.22212v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22212v1.html; sha256:5fd9b6f3e80c5ef144862efb3dc3888f77be2d1ac3dde37cbe09588dace5f3e0 | arXiv:2603.22212v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.22212v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22212v1.html; sha256:5fd9b6f3e80c5ef144862efb3dc3888f77be2d1ac3dde37cbe09588dace5f3e0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22212v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22212 | complete |
| SF-2026-ARXIV-2603-22276 | RP-94021a4be6dafc14 | deep | arXiv:2603.22276v1 | SRC-ARXIV@arXiv:2603.22276v1 | arXiv:2603.22276v1 HTML — §Memory measurement methodology. [facet=method]; https://arxiv.org/html/2603.22276v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22276v1.html; sha256:3312ecc076a84c5cd8d5bd9dbab87c71ccf7e7170401053114735b706d39aeb0 | arXiv:2603.22276v1 HTML — §Ablation. [facet=evaluation]; https://arxiv.org/html/2603.22276v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22276v1.html; sha256:3312ecc076a84c5cd8d5bd9dbab87c71ccf7e7170401053114735b706d39aeb0 | arXiv:2603.22276v1 HTML — §6.2 Tradeoffs and Limitations [facet=limitations]; https://arxiv.org/html/2603.22276v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22276v1.html; sha256:3312ecc076a84c5cd8d5bd9dbab87c71ccf7e7170401053114735b706d39aeb0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22276v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22276 | complete |
| SF-2026-ARXIV-2603-22286 | RP-9486dfe708147d84 | deep | arXiv:2603.22286v1 | SRC-ARXIV@arXiv:2603.22286v1 | arXiv:2603.22286v1 HTML — §Appendix 0.B Implementation Details and Runtime Setup [facet=method]; https://arxiv.org/html/2603.22286v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22286v1.html; sha256:7fe1a5b61a5b5d87923afe1c13a25d9a9777dbe23b2a8c6dfeeb42bc757131eb | arXiv:2603.22286v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.22286v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22286v1.html; sha256:7fe1a5b61a5b5d87923afe1c13a25d9a9777dbe23b2a8c6dfeeb42bc757131eb | arXiv:2603.22286v1 HTML — §Appendix 0.H Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.22286v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22286v1.html; sha256:7fe1a5b61a5b5d87923afe1c13a25d9a9777dbe23b2a8c6dfeeb42bc757131eb | arXiv exact-v1 identity https://arxiv.org/abs/2603.22286v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22286 | complete |

### Source Reviews

### Locally Coherent Parallel Decoding in Diffusion Language Models

<!-- review:SF-2026-ARXIV-2603-20216:start -->
**问题**：离散 diffusion 同时独立采样多个 token 会破坏代码等局部联合结构。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：CoDiLA 在每个并行 block 内引入短程 autoregressive coherence，同时保留 block 间并行修正。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.20216v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.20216v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20216v1.html; sha256:49c909ce396bc25b54b9d4eec6aae5067d1fbc8dd281920b23c5b9204b4dfb7b`。

**Evaluation contract 与未证明部分**：论文结果支持指定代码/文本任务的速度质量折中；不证明 sub-linear latency 在所有硬件成立。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20216v1 HTML — §A.2 Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.20216v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20216v1.html; sha256:49c909ce396bc25b54b9d4eec6aae5067d1fbc8dd281920b23c5b9204b4dfb7b`。

**Trade-off / failure / coexistence**：局部 AR 恢复依赖也减少并行度；结构弱的生成可继续独立 denoise。

<!-- claim:SF-2026-ARXIV-2603-20216:start -->**Claim Boundary**：只支持 arXiv:2603.20216v1 §3 Method 的机制与 §A.2 Evaluation Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20216:end -->
<!-- review:SF-2026-ARXIV-2603-20216:end -->
### Expected Reward Prediction, with Applications to Model Routing

<!-- review:SF-2026-ARXIV-2603-20217:start -->
**问题**：response reward model 通常在看到输出后排序，不能直接在请求到达时选择模型。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：论文估计每个模型对 prompt 的期望 reward，把 response-level scorer 提升为 pre-execution model-routing signal。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.20217v1 HTML — §Model Routing Methods. [facet=method]; https://arxiv.org/html/2603.20217v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20217v1.html; sha256:efd0a666d03531f0adfb0464d05b72931a4c3ac75aa9a9f84a1fe4205ede0c59`。

**Evaluation contract 与未证明部分**：实验说明期望值在所测模型池中具有区分力；不证明 reward model 对分布外 prompt 校准。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20217v1 HTML — §Routing Evaluations. [facet=evaluation]; https://arxiv.org/html/2603.20217v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20217v1.html; sha256:efd0a666d03531f0adfb0464d05b72931a4c3ac75aa9a9f84a1fe4205ede0c59`。

**Trade-off / failure / coexistence**：路由减少昂贵采样却继承 reward bias；高风险请求仍需实际生成后验证。

<!-- claim:SF-2026-ARXIV-2603-20217:start -->**Claim Boundary**：只支持 arXiv:2603.20217v1 §Model Routing Methods. 的机制与 §Routing Evaluations. 的公开 workload；§5 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20217:end -->
<!-- review:SF-2026-ARXIV-2603-20217:end -->
### An experimental study of KV cache reuse strategies in chunk-level caching systems

<!-- review:SF-2026-ARXIV-2603-20218:start -->
**问题**：chunk-level cache 跳过跨 chunk attention，命中率提升可能以回答质量为代价。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：研究在统一系统中比较多种 KV reuse 修复策略，明确哪些依赖可恢复、哪些结构性误差仍存在。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.20218v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.20218v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20218v1.html; sha256:e8bbfebc54a26d3ced565fe2fdc3015d14a6084dad5ff2f8d935aa3961d8da57`。

**Evaluation contract 与未证明部分**：结果是特定模型、chunking 和 RAG workload 的实验边界，不是通用缓存排序。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20218v1 HTML — §4. Experimental study [facet=evaluation]; https://arxiv.org/html/2603.20218v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20218v1.html; sha256:e8bbfebc54a26d3ced565fe2fdc3015d14a6084dad5ff2f8d935aa3961d8da57`。

**Trade-off / failure / coexistence**：更精确修复增加重算；短检索上下文可直接完整 prefill。

<!-- claim:SF-2026-ARXIV-2603-20218:start -->**Claim Boundary**：只支持 arXiv:2603.20218v1 §3. Methodology 的机制与 §4. Experimental study 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20218:end -->
<!-- review:SF-2026-ARXIV-2603-20218:end -->
### Thinking into the Future: Latent Lookahead Training for Transformers

<!-- review:SF-2026-ARXIV-2603-20219:start -->
**问题**：next-token objective 强制每步立即提交且每个 token 分配同等 compute，困难位置无法先探索多条继续路径。

**旧路径为何合理**：next-token 因果分解提供简单可扩展的训练与流式生成。

**约束变化与机制**：latent lookahead 在离散输出前训练隐藏的前瞻状态，让额外计算发生在未提交空间。

**State / data / control owner**：`MODEL-DECODER-ONLY` 负责 隐藏状态演化、token commitment 与动态计算分配；定位证据为 `arXiv:2603.20219v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.20219v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20219v1.html; sha256:045a043b5330cfc40c2649f87e0439a69321665eae0c14298a3455953a21f4df`。

**Evaluation contract 与未证明部分**：实验支持所测语言任务的质量变化；不证明 latent trajectory 可解释或带来系统级低延迟。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20219v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.20219v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20219v1.html; sha256:045a043b5330cfc40c2649f87e0439a69321665eae0c14298a3455953a21f4df`。

**Trade-off / failure / coexistence**：额外 hidden steps 增加训练/推理计算；简单 token 不需要动态思考预算。

<!-- claim:SF-2026-ARXIV-2603-20219:start -->**Claim Boundary**：只支持 arXiv:2603.20219v1 §3 Methodology 的机制与 §4 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20219:end -->
<!-- review:SF-2026-ARXIV-2603-20219:end -->
### Agentproof: Static Verification of Agent Workflow Graphs

<!-- review:SF-2026-ARXIV-2603-20356:start -->
**问题**：显式 agent workflow graph 在部署前已经暴露工具和分支结构，但安全检查通常等到 runtime 才发生。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：Agentproof 从框架 API 抽取 graph，静态传播 node/tool 属性并检查不可达授权、缺失 human gate 等结构规则。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.20356v1 HTML — §4 System overview [facet=method]; https://arxiv.org/html/2603.20356v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20356v1.html; sha256:420e2f649c6d5fa4bd941987770d60ffcf9ba8830dd48449dc0dd08641b9ea04`。

**Evaluation contract 与未证明部分**：评测验证多个 framework graph 的提取与规则命中；LangGraph human-node 依赖命名 heuristic，限制了完备性。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20356v1 HTML — §7.3 Temporal policy evaluation [facet=evaluation]; https://arxiv.org/html/2603.20356v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20356v1.html; sha256:420e2f649c6d5fa4bd941987770d60ffcf9ba8830dd48449dc0dd08641b9ea04`。

**Trade-off / failure / coexistence**：静态检查便宜且可前移 release gate，但看不到运行时 prompt/data；动态行为仍需 runtime policy 与 trace。

<!-- claim:SF-2026-ARXIV-2603-20356:start -->**Claim Boundary**：只支持 arXiv:2603.20356v1 §4 System overview 的机制与 §7.3 Temporal policy evaluation 的公开 workload；§Human-node detection limitation. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20356:end -->
<!-- review:SF-2026-ARXIV-2603-20356:end -->
### Memory poisoning and secure multi-agent systems

<!-- review:SF-2026-ARXIV-2603-20357:start -->
**问题**：多 agent 共用多类 memory 时，污染可从一个写入域传播到其他 agent 和后续会话，单次输入过滤看不到该路径。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文按 memory duration、origin 与 location 建立威胁分类，并把 provenance、write authority 和 retrieval validation 作为隔离边界。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.20357v1 HTML — §3.1 Semantic memory poisoning attacks [facet=method]; https://arxiv.org/html/2603.20357v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20357v1.html; sha256:f8731ef152199259accd13c3f6f5075b083b5c3d2e9516a7445de53115b95678`。

**Evaluation contract 与未证明部分**：exact-v1 主要是 threat taxonomy/设计讨论，没有可复算防御 benchmark，不能声称某机制有效率。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20357v1 HTML — §Mitigation strategies against semantic memory poisoning attacks [facet=evaluation]; https://arxiv.org/html/2603.20357v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20357v1.html; sha256:f8731ef152199259accd13c3f6f5075b083b5c3d2e9516a7445de53115b95678`。

**Trade-off / failure / coexistence**：更强隔离降低共享收益并增加治理状态；无持久共享 memory 时攻击面显著缩小。

<!-- claim:SF-2026-ARXIV-2603-20357:start -->**Claim Boundary**：只支持 arXiv:2603.20357v1 §3.1 Semantic memory poisoning attacks 的机制与 §Mitigation strategies against semantic memory poisoning attacks 的公开 workload；§4 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20357:end -->
<!-- review:SF-2026-ARXIV-2603-20357:end -->
### MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning

<!-- review:SF-2026-ARXIV-2603-20586:start -->
**问题**：单层 KV 对所有历史使用同一保留策略，不能同时服务局部依赖、会话状态和长期记忆。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：MKA 用 memory key 在 L1/L2/L3 timescale 间动态路由 attention，在固定 KV 预算下选择不同层级的表示。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.20586v1 HTML — §4. Methodology [facet=method]; https://arxiv.org/html/2603.20586v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20586v1.html; sha256:f08f886fa596dc1af176319d8182b2955a5c0251c52fda0ad93a0fe9643c2c03`。

**Evaluation contract 与未证明部分**：论文在 Qwen2.5 等三类模型/压缩策略上测量 perplexity 与任务表现；证据不覆盖任意 memory hierarchy。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20586v1 HTML — §6.3. Experimental Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.20586v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20586v1.html; sha256:f08f886fa596dc1af176319d8182b2955a5c0251c52fda0ad93a0fe9643c2c03`。

**Trade-off / failure / coexistence**：层次路由提高预算利用率但引入 key 学习和错误层级选择；短上下文仍可用单层 KV。

<!-- claim:SF-2026-ARXIV-2603-20586:start -->**Claim Boundary**：只支持 arXiv:2603.20586v1 §4. Methodology 的机制与 §6.3. Experimental Results Analysis 的公开 workload；§6.7. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20586:end -->
<!-- review:SF-2026-ARXIV-2603-20586:end -->
### Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression

<!-- review:SF-2026-ARXIV-2603-20616:start -->
**问题**：只按 token eviction 分配 KV 预算忽略不同 head/channel 的冗余差异，固定维度压缩会浪费容量。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：MixedDimKV 联合选择 token 与投影维度，并重排 memory layout、复用 projection matrix，以不同维数编码不同 KV 子空间。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.20616v1 HTML — §5 Implementation [facet=method]; https://arxiv.org/html/2603.20616v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20616v1.html; sha256:212f2965800229075d17b7a521198ef00e490e005ba487ebbc00f6f064c3963f`。

**Evaluation contract 与未证明部分**：实验在公开模型上比较同预算压缩；收益依赖 PCA 子空间和层/head 统计稳定性。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20616v1 HTML — §6.2 Main Results on Long-Context Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.20616v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20616v1.html; sha256:212f2965800229075d17b7a521198ef00e490e005ba487ebbc00f6f064c3963f`。

**Trade-off / failure / coexistence**：混合维度减少浪费却使 kernel、layout 和 metadata 更复杂；规则形状或硬件 kernel 受限时固定维度更易部署。

<!-- claim:SF-2026-ARXIV-2603-20616:start -->**Claim Boundary**：只支持 arXiv:2603.20616v1 §5 Implementation 的机制与 §6.2 Main Results on Long-Context Benchmarks 的公开 workload；§6.5 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20616:end -->
<!-- review:SF-2026-ARXIV-2603-20616:end -->
### ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore

<!-- review:SF-2026-ARXIV-2603-20625:start -->
**问题**：checkpoint restore 后 LLM 会重新合成语义相同但字节不同的请求，传统 idempotency key 无法识别重复副作用。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：ACRFence 对 action 语义与 authority consumption 建立持久承诺，在 restore 后拒绝 action replay 与 credential resurrection。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.20625v1 HTML — §4. Mitigation: ACRFence [facet=method]; https://arxiv.org/html/2603.20625v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20625v1.html; sha256:c63d0648a0a18acdcbd4a10628782203a81e6a18a0093e7638ecb320538f63df`。

**Evaluation contract 与未证明部分**：论文攻击与原型验证支持定义的两类 rollback；不证明语义 canonicalizer 覆盖所有工具。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20625v1 HTML — §3. Attacks and Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.20625v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20625v1.html; sha256:c63d0648a0a18acdcbd4a10628782203a81e6a18a0093e7638ecb320538f63df`。

**Trade-off / failure / coexistence**：更强防重放需要持久 ledger 且可能误并合法重试；确定性程序仍可使用普通 request ID。

<!-- claim:SF-2026-ARXIV-2603-20625:start -->**Claim Boundary**：只支持 arXiv:2603.20625v1 §4. Mitigation: ACRFence 的机制与 §3. Attacks and Experimental Validation 的公开 workload；§6. Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20625:end -->
<!-- review:SF-2026-ARXIV-2603-20625:end -->
### RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models

<!-- review:SF-2026-ARXIV-2603-20711:start -->
**问题**：VLA 的感知、推理与控制跨 edge/cloud 切分时，单看算力无法满足网络波动和控制周期。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：RoboECC 联合 model-hardware segmentation 与 network-aware adjustment，运行时改变 VLA partition 和放置。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.20711v1 HTML — §IV RoboECC Framework [facet=method]; https://arxiv.org/html/2603.20711v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20711v1.html; sha256:0a4fc25eda92ff465e8a3089c2c8df48f33a81020557f97fce7b5f955ca056cb`。

**Evaluation contract 与未证明部分**：公开实验分析所测模型、设备与网络下的部署收益；不能证明所有机器人链路都能安全动态切分。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20711v1 HTML — §V-B1 Results in Simulation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.20711v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20711v1.html; sha256:0a4fc25eda92ff465e8a3089c2c8df48f33a81020557f97fce7b5f955ca056cb`。

**Trade-off / failure / coexistence**：自适应放置改善资源利用但引入中间状态传输和切换抖动；网络不可靠或安全关键闭环应优先 edge-local。

<!-- claim:SF-2026-ARXIV-2603-20711:start -->**Claim Boundary**：只支持 arXiv:2603.20711v1 §IV RoboECC Framework 的机制与 §V-B1 Results in Simulation Benchmark 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20711:end -->
<!-- review:SF-2026-ARXIV-2603-20711:end -->
### Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents

<!-- review:SF-2026-ARXIV-2603-20953:start -->
**问题**：模型 alignment 和事后评测都不能在具体 tool call 执行前提供确定性权限判断。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：OAP 拦截 action proposal，将 principal、capability、policy 与请求参数绑定后再签发一次性执行许可。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.20953v1 HTML — §3.2 Architecture [facet=method]; https://arxiv.org/html/2603.20953v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20953v1.html; sha256:cdfdd6a1c1147ac2c7bcdc1c49c69c775f6c4dc0e36d96d21a97baae3d8ebf1f`。

**Evaluation contract 与未证明部分**：公开 spec/reference implementation 证明协议可实现，不构成所有攻击面或性能证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20953v1 HTML — §2.2 Post-Hoc Evaluation [facet=evaluation]; https://arxiv.org/html/2603.20953v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.20953v1.html; sha256:cdfdd6a1c1147ac2c7bcdc1c49c69c775f6c4dc0e36d96d21a97baae3d8ebf1f`。

**Trade-off / failure / coexistence**：集中 authorization 增加依赖与撤销状态；受限单工具进程可用本地 ACL。

<!-- claim:SF-2026-ARXIV-2603-20953:start -->**Claim Boundary**：只支持 arXiv:2603.20953v1 §3.2 Architecture 的机制与 §2.2 Post-Hoc Evaluation 的公开 workload；§8.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20953:end -->
<!-- review:SF-2026-ARXIV-2603-20953:end -->
### SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration

<!-- review:SF-2026-ARXIV-2603-21019:start -->
**问题**：agent skill marketplace 的包同时含说明、脚本和资产，下载量或静态 metadata 不能说明实际 capability 风险。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SkillProbe 组合多 agent 分工、静态扫描与可选动态执行，对 skill 的声明、代码行为和权限需求做交叉审计。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.21019v1 HTML — §3.4 System Implementation [facet=method]; https://arxiv.org/html/2603.21019v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21019v1.html; sha256:e2b19122a26d61f24cb89cc5e3853f6460c57e2b001357b554c1eb5c309a6aa5`。

**Evaluation contract 与未证明部分**：评测使用真实生态样本与受控环境；检测率受 Python/工具 sandbox 和规则覆盖限制。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21019v1 HTML — §4.3 Large-scale Empirical Audit [facet=evaluation]; https://arxiv.org/html/2603.21019v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21019v1.html; sha256:e2b19122a26d61f24cb89cc5e3853f6460c57e2b001357b554c1eb5c309a6aa5`。

**Trade-off / failure / coexistence**：协作审计扩大覆盖却增加模型判断与执行成本；可信内部 registry 仍可用签名和人工 review。

<!-- claim:SF-2026-ARXIV-2603-21019:start -->**Claim Boundary**：只支持 arXiv:2603.21019v1 §3.4 System Implementation 的机制与 §4.3 Large-scale Empirical Audit 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21019:end -->
<!-- review:SF-2026-ARXIV-2603-21019:end -->
### CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation

<!-- review:SF-2026-ARXIV-2603-21104:start -->
**问题**：安全关键 world-model 评测若只生成更危险的画面，无法说明哪一动作或交互导致风险。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：CounterScene 把场景生成写成对 multi-agent dynamics 的 counterfactual intervention，比较改变特定因果变量后的 rollout。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.21104v1 HTML — §Implementation Details. [facet=method]; https://arxiv.org/html/2603.21104v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21104v1.html; sha256:b35ef6f4e98efbc15f7671e53dba33ba6d6c2313089d0a10a6ad53edaee0145b`。

**Evaluation contract 与未证明部分**：闭环驾驶场景实验支持该干预在所测 simulator 中产生可解释危险交互；不证明 learned causality 等同真实世界。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21104v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.21104v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21104v1.html; sha256:b35ef6f4e98efbc15f7671e53dba33ba6d6c2313089d0a10a6ad53edaee0145b`。

**Trade-off / failure / coexistence**：因果控制增强诊断但依赖结构假设；仅需视觉多样性时普通生成模型成本更低。

<!-- claim:SF-2026-ARXIV-2603-21104:start -->**Claim Boundary**：只支持 arXiv:2603.21104v1 §Implementation Details. 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21104:end -->
<!-- review:SF-2026-ARXIV-2603-21104:end -->
### Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts

<!-- review:SF-2026-ARXIV-2603-21177:start -->
**问题**：GRPO 每轮重新采样全部 prompt 浪费 rollout，而简单 replay 又会破坏 on-policy freshness。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：方法只重放近期产生高方差/高信号 group outcome 的 prompt，再用当前 policy 重新 rollout，而不是复用旧 trajectory。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.21177v1 HTML — §Appendix B Algorithm [facet=method]; https://arxiv.org/html/2603.21177v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21177v1.html; sha256:9bb5031e7669ee1556437b78ca21adfbc4d3e5ae6fab2853a9df6a272fa26936`。

**Evaluation contract 与未证明部分**：基于 OLMo-RL 并在六个 benchmark 报告准确率/训练效率；结论绑定筛选规则和任务分布。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21177v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.21177v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21177v1.html; sha256:9bb5031e7669ee1556437b78ca21adfbc4d3e5ae6fab2853a9df6a272fa26936`。

**Trade-off / failure / coexistence**：prompt replay 提高样本利用率但可能过度聚焦困难样本并改变 curriculum；信号均匀时标准采样更稳。

<!-- claim:SF-2026-ARXIV-2603-21177:start -->**Claim Boundary**：只支持 arXiv:2603.21177v1 §Appendix B Algorithm 的机制与 §5.1 Main Results 的公开 workload；§6.2 Limitations & Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21177:end -->
<!-- review:SF-2026-ARXIV-2603-21177:end -->
### CALVO: Improve Serving Efficiency for LLM Inferences with Intense Network Demands

<!-- review:SF-2026-ARXIV-2603-21257:start -->
**问题**：高命中长上下文请求可能被远端 KV 加载而非 GPU compute 主导，compute-centric scheduler 看不到网络关键路径。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：CALVO 将 KV block loading 建模为一等阶段，联合网络预取、请求排序和 GPU admission。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.21257v1 HTML — §3. Solution [facet=method]; https://arxiv.org/html/2603.21257v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21257v1.html; sha256:85b681bc71313742ab85044439a467f208c21c526e27b393fc7eecca98d37fc1`。

**Evaluation contract 与未证明部分**：结果支持指定集群、命中率和模型的吞吐/延迟；不能外推其他 fabric。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21257v1 HTML — §4.3. Micro-benchmark Analysis [facet=evaluation]; https://arxiv.org/html/2603.21257v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21257v1.html; sha256:85b681bc71313742ab85044439a467f208c21c526e27b393fc7eecca98d37fc1`。

**Trade-off / failure / coexistence**：网络感知提高利用率但增加预测与缓存一致性；KV 本地时传统 scheduler 更简单。

<!-- claim:SF-2026-ARXIV-2603-21257:start -->**Claim Boundary**：只支持 arXiv:2603.21257v1 §3. Solution 的机制与 §4.3. Micro-benchmark Analysis 的公开 workload；§5. Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21257:end -->
<!-- review:SF-2026-ARXIV-2603-21257:end -->
### AutoKernel: Autonomous GPU Kernel Optimization via Iterative Agent-Driven Search

<!-- review:SF-2026-ARXIV-2603-21331:start -->
**问题**：自动 kernel agent 若只追求单点速度，容易生成数值错误、shape 脆弱或不确定实现。

**旧路径为何合理**：成熟 vendor kernel 在稳定 shape 上通常最可靠。

**约束变化与机制**：AutoKernel 以 profile/Amdahl 排序优化目标，并用五阶段 correctness harness 约束每轮 Triton/CUDA 搜索。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel/graph execution、量化、编译和硬件适配；定位证据为 `arXiv:2603.21331v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.21331v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21331v1.html; sha256:aef41f1cd9228a3cb49e529278270632057adfc61c976e3ba766ff57f659d22b`。

**Evaluation contract 与未证明部分**：数百次实验和多 shape 测试支持其优化 loop；不证明 harness 已覆盖所有数值边界。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21331v1 HTML — §7 Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21331v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21331v1.html; sha256:aef41f1cd9228a3cb49e529278270632057adfc61c976e3ba766ff57f659d22b`。

**Trade-off / failure / coexistence**：搜索成本高且容易过拟合硬件；成熟常用算子仍优先人工库。

<!-- claim:SF-2026-ARXIV-2603-21331:start -->**Claim Boundary**：只支持 arXiv:2603.21331v1 §3 System Design 的机制与 §7 Experimental Evaluation 的公开 workload；§11 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21331:end -->
<!-- review:SF-2026-ARXIV-2603-21331:end -->
### ARYA: A Physics-Constrained Composable &amp; Deterministic World Model Architecture

<!-- review:SF-2026-ARXIV-2603-21340:start -->
**问题**：monolithic learned world model 难同时提供物理一致、可组合模块、确定性 rollout 和可审计安全边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：ARYA 提出由小型物理约束组件组合出的 deterministic state-transition architecture，把 causal interface 显式化。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.21340v1 PDF — §3 System Architecture Overview [facet=method]; https://arxiv.org/pdf/2603.21340v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21340v1.pdf.txt; sha256:89d029d40d6913049fbb3603ea24028495bc4e4899529e2dd51fa404f0ab397e`。

**Evaluation contract 与未证明部分**：公开 v1 是架构主张，缺少可复算的实现和独立实验，因此不能确认其满足所宣称的全部 world-model 要求。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21340v1 PDF — §11 Empirical Evaluation [facet=evaluation]; https://arxiv.org/pdf/2603.21340v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21340v1.pdf.txt; sha256:89d029d40d6913049fbb3603ea24028495bc4e4899529e2dd51fa404f0ab397e`。

**Trade-off / failure / coexistence**：确定性和模块化牺牲表示容量并把误差移到接口；数据丰富的感知生成仍可能需要大模型。

<!-- claim:SF-2026-ARXIV-2603-21340:start -->**Claim Boundary**：只支持 exact-v1 白皮书 §3 的公开架构描述；§11 的厂商 benchmark 主张缺少独立复核，因此维持 Disputed，不将生产部署、SOTA 或安全有效性作为已证实事实。<!-- claim:SF-2026-ARXIV-2603-21340:end -->
<!-- review:SF-2026-ARXIV-2603-21340:end -->
### The Workload-Router-Pool Architecture for LLM Inference Optimization: A Vision Paper from the vLLM Semantic Router Project

<!-- review:SF-2026-ARXIV-2603-21354:start -->
**问题**：单 router 同时承担内容分类、模型选择、cache、安全和 fleet provisioning，会造成策略冲突与不可独立扩缩。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：WRP vision 将 workload classification、router policy 与执行 pool 分层，主张每层拥有不同状态与扩缩周期。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.21354v1 HTML — §2.1 Pillar 1: Routing Architecture [facet=method]; https://arxiv.org/html/2603.21354v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21354v1.html; sha256:31a0c2520506b10b895818400dd0ae7f7e799c5070b6c1a59801e105652f55b1`。

**Evaluation contract 与未证明部分**：这是项目经验汇总和 vision，不提供统一对照实验，因此只作为架构候选而非性能事实。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21354v1 HTML — §Validated building blocks (separate systems, public benchmarks). [facet=evaluation]; https://arxiv.org/html/2603.21354v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21354v1.html; sha256:31a0c2520506b10b895818400dd0ae7f7e799c5070b6c1a59801e105652f55b1`。

**Trade-off / failure / coexistence**：分层清晰但引入更多控制面与一致性；单模型小流量仍可单 gateway。

<!-- claim:SF-2026-ARXIV-2603-21354:start -->**Claim Boundary**：只支持 arXiv:2603.21354v1 §2.1 Pillar 1: Routing Architecture 的机制与 §Validated building blocks (separate systems, public benchmarks). 的公开 workload；§Agent serving and failure analysis. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21354:end -->
<!-- review:SF-2026-ARXIV-2603-21354:end -->
### PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost

<!-- review:SF-2026-ARXIV-2603-21383:start -->
**问题**：trajectory-level RL 把大量已确定或无信息的 turn 一并训练，浪费 verifier 和 rollout compute。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：PivotRL 离线识别 mixed-outcome pivot turn，只在局部 state 上组成 group-normalized 更新，并用 verifier 约束选择。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.21383v1 HTML — §3.1 Method [facet=method]; https://arxiv.org/html/2603.21383v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21383v1.html; sha256:6b486c3cc3bcacbe5ecb07a0d1a1fe498e2a69249d4a0ca3bdb89f3466d912f2`。

**Evaluation contract 与未证明部分**：理论分析与 agentic benchmark 检查 turn selection 和 verifier design；证据限于可可靠标注 pivot 的环境。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21383v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.21383v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21383v1.html; sha256:6b486c3cc3bcacbe5ecb07a0d1a1fe498e2a69249d4a0ca3bdb89f3466d912f2`。

**Trade-off / failure / coexistence**：局部训练节省算力但可能破坏长程 credit；任务奖励强依赖远期状态时完整 trajectory RL 仍必要。

<!-- claim:SF-2026-ARXIV-2603-21383:start -->**Claim Boundary**：只支持 arXiv:2603.21383v1 §3.1 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21383:end -->
<!-- review:SF-2026-ARXIV-2603-21383:end -->
### DRTriton: Large-Scale Synthetic Data Driven Reinforcement Learning for Triton Kernel Generation

<!-- review:SF-2026-ARXIV-2603-21465:start -->
**问题**：kernel-generation LLM 缺少规模化正确训练数据，直接 RL 容易在编译通过与真实加速之间投机。

**旧路径为何合理**：成熟 vendor kernel 在稳定 shape 上通常最可靠。

**约束变化与机制**：DRTriton 组合合成 PyTorch-Triton pairs、可执行 correctness filter 与性能 reward 来训练 kernel policy。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel/graph execution、量化、编译和硬件适配；定位证据为 `arXiv:2603.21465v1 HTML — §4 Training Pipeline [facet=method]; https://arxiv.org/html/2603.21465v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21465v1.html; sha256:878637c83e477be0fc2477e9c307b8a08ffd8c9966e7dd5bb26d0d9e48321961`。

**Evaluation contract 与未证明部分**：结果支持论文数据、GPU 和算子分布；不证明生成 kernel 可直接用于任意生产模型。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21465v1 HTML — §5.2 Results on Synthetic Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.21465v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21465v1.html; sha256:878637c83e477be0fc2477e9c307b8a08ffd8c9966e7dd5bb26d0d9e48321961`。

**Trade-off / failure / coexistence**：大规模编译/benchmark 成本高且 reward 依赖硬件；关键 kernel 仍需人工验证。

<!-- claim:SF-2026-ARXIV-2603-21465:start -->**Claim Boundary**：只支持 arXiv:2603.21465v1 §4 Training Pipeline 的机制与 §5.2 Results on Synthetic Benchmarks 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21465:end -->
<!-- review:SF-2026-ARXIV-2603-21465:end -->
### Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation

<!-- review:SF-2026-ARXIV-2603-21522:start -->
**问题**：多 agent failure 每次从单条 trace 重新分析，既慢又无法复用历史模式。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：论文把 reasoning trace 编码为可检索 failure representation，用历史相似模式辅助诊断与恢复。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `arXiv:2603.21522v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.21522v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21522v1.html; sha256:018b0fc4cdff60de08d8b734dfbd1b4c4da2ec9b35d3466dce8b300058192994`。

**Evaluation contract 与未证明部分**：初步实验只证明该表示在所测故障集中的可用性，不证明根因唯一或长期不漂移。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21522v1 HTML — §2.2. Evaluation of Existing Embeddings on Reasoning Trace Representation [facet=evaluation]; https://arxiv.org/html/2603.21522v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21522v1.html; sha256:018b0fc4cdff60de08d8b734dfbd1b4c4da2ec9b35d3466dce8b300058192994`。

**Trade-off / failure / coexistence**：模式复用会固化旧误诊并带来隐私成本；新型故障仍需完整 trace RCA。

<!-- claim:SF-2026-ARXIV-2603-21522:start -->**Claim Boundary**：只支持 arXiv:2603.21522v1 §3. Methodology 的机制与 §2.2. Evaluation of Existing Embeddings on Reasoning Trace Representation 的公开 workload；§2.1. Failure Pattern Concentration in Multi-Agent Systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21522:end -->
<!-- review:SF-2026-ARXIV-2603-21522:end -->
### SafePilot: A Framework for Assuring LLM-enabled Cyber-Physical Systems

<!-- review:SF-2026-ARXIV-2603-21523:start -->
**问题**：LLM 进入 CPS 后，语言层错误可能跨越到物理 action，纯模型准确率不能构成 safety assurance。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SafePilot 在 LLM planner 与低层 controller 之间加入安全 monitor、可验证约束和 fallback 控制链。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.21523v1 HTML — §4. System Design [facet=method]; https://arxiv.org/html/2603.21523v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21523v1.html; sha256:5458b605fce3e390dd5d8989548197ceede4e60d60fae7f5ae433c1a627c781f`。

**Evaluation contract 与未证明部分**：框架案例支持控制边界可实现，不等同于认证或真实事故率证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21523v1 HTML — §5. Experiments [facet=evaluation]; https://arxiv.org/html/2603.21523v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21523v1.html; sha256:5458b605fce3e390dd5d8989548197ceede4e60d60fae7f5ae433c1a627c781f`。

**Trade-off / failure / coexistence**：monitor 限制开放式规划并增加延迟；封闭控制任务优先传统 verified controller。

<!-- claim:SF-2026-ARXIV-2603-21523:start -->**Claim Boundary**：只支持 arXiv:2603.21523v1 §4. System Design 的机制与 §5. Experiments 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21523:end -->
<!-- review:SF-2026-ARXIV-2603-21523:end -->
### Toward a Theory of Hierarchical Memory for Language Agents

<!-- review:SF-2026-ARXIV-2603-21564:start -->
**问题**：hierarchical memory 系统使用不同术语，难比较它们究竟聚合什么、保留多少以及多久更新。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：论文用 (aggregation α, capacity C, timescale τ) 三元组统一 data memory 与 agent-trace memory 的层级设计。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.21564v1 HTML — §2.1 Core Definitions [facet=method]; https://arxiv.org/html/2603.21564v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21564v1.html; sha256:8848b8e1c2211f29d732d7a1a1c6e867127f23dc1adac38051d0bced09ea0383`。

**Evaluation contract 与未证明部分**：表格映射十一种系统，属于理论/分类比较而非新 runtime benchmark；它证明统一语言可覆盖这些案例。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21564v1 HTML — §3.1 Data and Trace Systems [facet=evaluation]; https://arxiv.org/html/2603.21564v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21564v1.html; sha256:8848b8e1c2211f29d732d7a1a1c6e867127f23dc1adac38051d0bced09ea0383`。

**Trade-off / failure / coexistence**：统一参数便于设计但会抽象掉权限和语义冲突；单层 memory 不需要额外层次模型。

<!-- claim:SF-2026-ARXIV-2603-21564:start -->**Claim Boundary**：只支持 arXiv:2603.21564v1 §2.1 Core Definitions 的机制与 §3.1 Data and Trace Systems 的公开 workload；§4 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21564:end -->
<!-- review:SF-2026-ARXIV-2603-21564:end -->
### PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection

<!-- review:SF-2026-ARXIV-2603-21576:start -->
**问题**：长上下文 decode 的瓶颈是每步扫描 O(n) KV block，单纯提高矩阵吞吐不改变带宽复杂度。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：PRISM 用光子相似搜索先做近常数时间 block selection，仅把被选 KV 送入电子 attention。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.21576v1 HTML — §III.1 System Overview [facet=method]; https://arxiv.org/html/2603.21576v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21576v1.html; sha256:9fea03d9a8fcafda79c9b82286babc1f03cbd991f5df0037066a7cb1f02b323f`。

**Evaluation contract 与未证明部分**：论文硬件模型/原型支持其配置下的带宽与精度；不证明商用系统成本和所有序列分布。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21576v1 HTML — §V System-Level Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21576v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21576v1.html; sha256:9fea03d9a8fcafda79c9b82286babc1f03cbd991f5df0037066a7cb1f02b323f`。

**Trade-off / failure / coexistence**：近似选择可能漏掉关键 token，且光电接口成为新瓶颈；中短上下文仍适合完整 attention。

<!-- claim:SF-2026-ARXIV-2603-21576:start -->**Claim Boundary**：只支持 arXiv:2603.21576v1 §III.1 System Overview 的机制与 §V System-Level Evaluation 的公开 workload；§VII.1 Limitations and Practical Considerations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21576:end -->
<!-- review:SF-2026-ARXIV-2603-21576:end -->
### Auditing MCP Servers for Over-Privileged Tool Capabilities

<!-- review:SF-2026-ARXIV-2603-21641:start -->
**问题**：MCP server 常把实现方便所需的内部能力全部暴露为 tool，形成超出任务需要的权限面。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：审计器解析 Python/JSON tool metadata，联合静态规则与可选 sandbox 动态检查，输出 capability 与最小权限差异。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.21641v1 HTML — §2. Tool Architecture and Implementation [facet=method]; https://arxiv.org/html/2603.21641v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21641v1.html; sha256:9d31c161f5c335eb9b0ef1ab5f7c47b54a61623e767d6c383638ae251723b233`。

**Evaluation contract 与未证明部分**：受控 vulnerable server、MCPTox 和 curated server 上的检测实验支持该实现；TypeScript/JavaScript 暂未覆盖。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21641v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.21641v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21641v1.html; sha256:9d31c161f5c335eb9b0ef1ab5f7c47b54a61623e767d6c383638ae251723b233`。

**Trade-off / failure / coexistence**：自动审计可前移 release gate，但静态近似会误报；语言不支持或动态 capability 仍需人工/运行时验证。

<!-- claim:SF-2026-ARXIV-2603-21641:start -->**Claim Boundary**：只支持 arXiv:2603.21641v1 §2. Tool Architecture and Implementation 的机制与 §4. Evaluation 的公开 workload；§5. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21641:end -->
<!-- review:SF-2026-ARXIV-2603-21641:end -->
### Are AI-assisted Development Tools Immune to Prompt Injection?

<!-- review:SF-2026-ARXIV-2603-21642:start -->
**问题**：MCP 客户端把 tool description 和返回内容送入 planner，供应链 metadata 可成为 prompt-injection 通道。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：研究对真实 AI coding clients 实施 tool-poisoning，比较不同客户端、模型与交互阶段的权限跨越。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.21642v1 HTML — §4.1. Attack Implementation [facet=method]; https://arxiv.org/html/2603.21642v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21642v1.html; sha256:0efd356d4c594fd1fd4c41fac701a42dba211e4d2dcd79d9fe4e81f8fee9c2ce`。

**Evaluation contract 与未证明部分**：证据只覆盖测试版本和攻击样本，不能证明未测客户端安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21642v1 HTML — §5. Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.21642v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21642v1.html; sha256:0efd356d4c594fd1fd4c41fac701a42dba211e4d2dcd79d9fe4e81f8fee9c2ce`。

**Trade-off / failure / coexistence**：防御需来源签名、展示差异和最小权限，会降低插件易用性；可信本地 server 风险较低。

<!-- claim:SF-2026-ARXIV-2603-21642:start -->**Claim Boundary**：只支持 arXiv:2603.21642v1 §4.1. Attack Implementation 的机制与 §5. Results and Analysis 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21642:end -->
<!-- review:SF-2026-ARXIV-2603-21642:end -->
### Reasoning Provenance for Autonomous AI Agents: Structured Behavioral Analytics Beyond State Checkpoints and Execution Traces

<!-- review:SF-2026-ARXIV-2603-21692:start -->
**问题**：checkpoint 和 execution trace 能回答发生了什么，却难以跨调查聚合 agent 为什么选择某 action。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：论文提出 normalized reasoning-provenance schema，将观察、候选、选择依据与行动关联为可查询记录。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `arXiv:2603.21692v1 HTML — §7 Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.21692v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21692v1.html; sha256:9ce8aa2f2bd18c1bb493112d4ec8ca857b1fc0b53be6a0b8aa966e0dd3345e36`。

**Evaluation contract 与未证明部分**：主要贡献是数据模型和分析案例，不证明记录就是模型真实因果理由。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21692v1 HTML — §7 Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.21692v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21692v1.html; sha256:9ce8aa2f2bd18c1bb493112d4ec8ca857b1fc0b53be6a0b8aa966e0dd3345e36`。

**Trade-off / failure / coexistence**：更细 provenance 增加敏感数据与存储成本；调试单次失败时普通 trace 已足够。

<!-- claim:SF-2026-ARXIV-2603-21692:start -->**Claim Boundary**：只支持 arXiv:2603.21692v1 §7 Evaluation Methodology 的机制与 §7 Evaluation Methodology 的公开 workload；§3.3 Limitation: Self-Reported Reasoning 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21692:end -->
<!-- review:SF-2026-ARXIV-2603-21692:end -->
### Holistic Scaling Laws for Optimal Mixture-of-Experts Architecture Optimization

<!-- review:SF-2026-ARXIV-2603-21862:start -->
**问题**：宏观 parameter/compute scaling law 不能直接决定 MoE 的 expert 数、粒度、共享层与 routing 配置。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：论文在统一实验基础设施上拟合面向 MoE architecture 的 scaling relations，并把 compute budget 映射到结构组合。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.21862v1 HTML — §4 Decoupling and reducing MoE scaling dimensions [facet=method]; https://arxiv.org/html/2603.21862v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21862v1.html; sha256:38e8d720a63e0ff39a846844dfbb6d38799a01878320fb6ed5f46e339ca5c058`。

**Evaluation contract 与未证明部分**：多组 MoE 实验支持所给设计空间内的趋势；硬件通信、训练配方和未测 router 会改变最优点。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.21862v1 HTML — §5.3 Results and scaling laws derivation [facet=evaluation]; https://arxiv.org/html/2603.21862v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.21862v1.html; sha256:38e8d720a63e0ff39a846844dfbb6d38799a01878320fb6ed5f46e339ca5c058`。

**Trade-off / failure / coexistence**：结构定标减少盲目 sweep，却可能固化历史硬件假设；小模型或通信昂贵时 dense/较少 expert 仍合理。

<!-- claim:SF-2026-ARXIV-2603-21862:start -->**Claim Boundary**：只支持 arXiv:2603.21862v1 §4 Decoupling and reducing MoE scaling dimensions 的机制与 §5.3 Results and scaling laws derivation 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-21862:end -->
<!-- review:SF-2026-ARXIV-2603-21862:end -->
### Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison

<!-- review:SF-2026-ARXIV-2603-22075:start -->
**问题**：AR 与 masked diffusion 常在不同数据和 compute 下比较，无法判断差异来自 factorization 还是训练预算。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：该工作固定 TinyStories 数据、step、batch、sequence 和 H100，分别训练 AR/MDLM，隔离生成范式作为实验变量。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.22075v1 HTML — §3.1 Controlled Variables [facet=method]; https://arxiv.org/html/2603.22075v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22075v1.html; sha256:eeb9794bb58afc845b8942a4251376bab8a840c5627db3f7b37036cb4f6411da`。

**Evaluation contract 与未证明部分**：受控比较只支持小数据/小模型和所报吞吐、质量、diversity；不能推断生产 LLM 哪个范式更优。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22075v1 HTML — §4.3 Generation Diversity: Quantitative Analysis [facet=evaluation]; https://arxiv.org/html/2603.22075v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22075v1.html; sha256:eeb9794bb58afc845b8942a4251376bab8a840c5627db3f7b37036cb4f6411da`。

**Trade-off / failure / coexistence**：MDLM 并行与迭代修正的收益依赖长度和硬件；AR 保留成熟 streaming/cache 路径。

<!-- claim:SF-2026-ARXIV-2603-22075:start -->**Claim Boundary**：只支持 arXiv:2603.22075v1 §3.1 Controlled Variables 的机制与 §4.3 Generation Diversity: Quantitative Analysis 的公开 workload；§5.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22075:end -->
<!-- review:SF-2026-ARXIV-2603-22075:end -->
### Do World Action Models Generalize Better than VLAs? A Robustness Study

<!-- review:SF-2026-ARXIV-2603-22078:start -->
**问题**：VLA 与 world-action model 的鲁棒性常在不同协议下比较，无法判断预测未来状态是否真的改善分布外控制。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：研究在共享 perturbation、任务和 action metric 下对两类模型做对照，隔离 world prediction 分支的条件收益。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.22078v1 HTML — §3.2 Evaluation Methods [facet=method]; https://arxiv.org/html/2603.22078v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22078v1.html; sha256:6c24b97d46efead2d9b6b71a2dfe2c00045dd8e85bbc1ff940231f5531a061d4`。

**Evaluation contract 与未证明部分**：结果只支持指定机器人数据与扰动集，不建立 WAM 普遍优于 VLA 的结论。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22078v1 HTML — §3.2 Evaluation Methods [facet=evaluation]; https://arxiv.org/html/2603.22078v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22078v1.html; sha256:6c24b97d46efead2d9b6b71a2dfe2c00045dd8e85bbc1ff940231f5531a061d4`。

**Trade-off / failure / coexistence**：world rollout 增加计算并可能传播预测误差；分布内低延迟控制仍可直接 VLA。

<!-- claim:SF-2026-ARXIV-2603-22078:start -->**Claim Boundary**：只支持 arXiv:2603.22078v1 §3.2 Evaluation Methods 的机制与 §3.2 Evaluation Methods 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22078:end -->
<!-- review:SF-2026-ARXIV-2603-22078:end -->
### Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs

<!-- review:SF-2026-ARXIV-2603-22206:start -->
**问题**：multi-agent workflow 同时包含不同语义角色、输出长度和模型需求，固定模型/队列会同时浪费质量和延迟预算。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Chimera 在 vLLM 前加入异步 semantic router 与 length predictor，联合选择异构模型并形成批次。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.22206v1 HTML — §3.8 Implementation Details [facet=method]; https://arxiv.org/html/2603.22206v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22206v1.html; sha256:0c223f09a316371310c7989d8062c7e9ae095e9061bb786e985dda9ca694827e`。

**Evaluation contract 与未证明部分**：评测覆盖多种 Qwen/Ministral 规模与 agent workflow；结果绑定预测误差、模型池和请求分布。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22206v1 HTML — §4.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.22206v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22206v1.html; sha256:0c223f09a316371310c7989d8062c7e9ae095e9061bb786e985dda9ca694827e`。

**Trade-off / failure / coexistence**：动态路由提高利用率但引入错误选模、冷缓存与公平性问题；单模型同质请求仍宜直接调度。

<!-- claim:SF-2026-ARXIV-2603-22206:start -->**Claim Boundary**：只支持 arXiv:2603.22206v1 §3.8 Implementation Details 的机制与 §4.3 Main Results 的公开 workload；§4.4 Ablations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22206:end -->
<!-- review:SF-2026-ARXIV-2603-22206:end -->
### Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models

<!-- review:SF-2026-ARXIV-2603-22212:start -->
**问题**：world model benchmark 若只看视频质量或静态 3D 重建，无法判断 action-conditioned interaction 是否正确。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Omni-WorldBench 以交互任务、物理原则和时序响应组织 suite，评估 observation-action-transition 而非单帧外观。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.22212v1 HTML — §2.1 World Models Design [facet=method]; https://arxiv.org/html/2603.22212v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22212v1.html; sha256:5fd9b6f3e80c5ef144862efb3dc3888f77be2d1ac3dde37cbe09588dace5f3e0`。

**Evaluation contract 与未证明部分**：公开 suite 覆盖多类物理和任务，但作者明确环境、多样性与 evaluator 仍有限；它定义合同而非证明某模型通用。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22212v1 HTML — §5.3 Quantitative Evaluation Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.22212v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22212v1.html; sha256:5fd9b6f3e80c5ef144862efb3dc3888f77be2d1ac3dde37cbe09588dace5f3e0`。

**Trade-off / failure / coexistence**：交互评测更接近 planning，却更昂贵且依赖 simulator；纯内容生成仍可使用视觉质量指标。

<!-- claim:SF-2026-ARXIV-2603-22212:start -->**Claim Boundary**：只支持 arXiv:2603.22212v1 §2.1 World Models Design 的机制与 §5.3 Quantitative Evaluation Results and Analysis 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22212:end -->
<!-- review:SF-2026-ARXIV-2603-22212:end -->
### Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels

<!-- review:SF-2026-ARXIV-2603-22276:start -->
**问题**：高 rank DoRA 需要显式物化 BA 后求行范数，临时内存随矩阵面积增长。

**旧路径为何合理**：低 rank adapter 以小状态增量实现高效微调。

**约束变化与机制**：该工作把范数分解为 base、cross 与 Gram 项，并融合 kernel，避免创建 dense update。

**State / data / control owner**：`TRAIN-LORA` 负责 adapter 参数化、训练状态和融合执行；定位证据为 `arXiv:2603.22276v1 HTML — §Memory measurement methodology. [facet=method]; https://arxiv.org/html/2603.22276v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22276v1.html; sha256:3312ecc076a84c5cd8d5bd9dbab87c71ccf7e7170401053114735b706d39aeb0`。

**Evaluation contract 与未证明部分**：实验支持指定维度、rank、GPU 与精度下的内存/速度；不证明高 rank 本身提高所有任务质量。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22276v1 HTML — §Ablation. [facet=evaluation]; https://arxiv.org/html/2603.22276v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22276v1.html; sha256:3312ecc076a84c5cd8d5bd9dbab87c71ccf7e7170401053114735b706d39aeb0`。

**Trade-off / failure / coexistence**：factorization 增加数值与 kernel 复杂度；低 rank LoRA/DoRA 已足够时无需该路径。

<!-- claim:SF-2026-ARXIV-2603-22276:start -->**Claim Boundary**：只支持 arXiv:2603.22276v1 §Memory measurement methodology. 的机制与 §Ablation. 的公开 workload；§6.2 Tradeoffs and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22276:end -->
<!-- review:SF-2026-ARXIV-2603-22276:end -->
### WorldCache: Content-Aware Caching for Accelerated Video World Models

<!-- review:SF-2026-ARXIV-2603-22286:start -->
**问题**：video world model 每步重算全部 DiT 中间状态，即使场景内容变化很小，也浪费推理计算。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：WorldCache 按感知变化决定何时复用 cached activation，并在 runtime 动态启停，不修改模型权重。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.22286v1 HTML — §Appendix 0.B Implementation Details and Runtime Setup [facet=method]; https://arxiv.org/html/2603.22286v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22286v1.html; sha256:7fe1a5b61a5b5d87923afe1c13a25d9a9777dbe23b2a8c6dfeeb42bc757131eb`。

**Evaluation contract 与未证明部分**：Cosmos-Predict2.5 2B/14B 的实验支持所测视频 workload 的加速；未证明高速运动或分布外场景保持 fidelity。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.22286v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.22286v1; papers/2026/03/_sources/daily-20260324/exact-v1-bodies/2603.22286v1.html; sha256:7fe1a5b61a5b5d87923afe1c13a25d9a9777dbe23b2a8c6dfeeb42bc757131eb`。

**Trade-off / failure / coexistence**：内容感知复用减少计算但可能缓存陈旧动态；变化剧烈、安全关键 rollout 应降低复用或完全重算。

<!-- claim:SF-2026-ARXIV-2603-22286:start -->**Claim Boundary**：只支持 arXiv:2603.22286v1 §Appendix 0.B Implementation Details and Runtime Setup 的机制与 §4.2 Main Results 的公开 workload；§Appendix 0.H Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22286:end -->
<!-- review:SF-2026-ARXIV-2603-22286:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-20216 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20216 |
| SF-2026-ARXIV-2603-20217 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20217 |
| SF-2026-ARXIV-2603-20218 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20218 |
| SF-2026-ARXIV-2603-20219 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20219 |
| SF-2026-ARXIV-2603-20356 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20356 |
| SF-2026-ARXIV-2603-20357 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20357 |
| SF-2026-ARXIV-2603-20586 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20586 |
| SF-2026-ARXIV-2603-20616 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20616 |
| SF-2026-ARXIV-2603-20625 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20625 |
| SF-2026-ARXIV-2603-20711 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20711 |
| SF-2026-ARXIV-2603-20953 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20953 |
| SF-2026-ARXIV-2603-21019 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21019 |
| SF-2026-ARXIV-2603-21104 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21104 |
| SF-2026-ARXIV-2603-21177 | score_7_9;potential_books_delta | selected | DA-20260324-14 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260324-14 |
| SF-2026-ARXIV-2603-21257 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21257 |
| SF-2026-ARXIV-2603-21331 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21331 |
| SF-2026-ARXIV-2603-21340 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21340 |
| SF-2026-ARXIV-2603-21354 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21354 |
| SF-2026-ARXIV-2603-21465 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21465 |
| SF-2026-ARXIV-2603-21522 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21522 |
| SF-2026-ARXIV-2603-21523 | score_7_9 | selected | DA-20260324-22 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260324-22 |
| SF-2026-ARXIV-2603-21564 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21564 |
| SF-2026-ARXIV-2603-21576 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21576 |
| SF-2026-ARXIV-2603-21641 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21641 |
| SF-2026-ARXIV-2603-21642 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21642 |
| SF-2026-ARXIV-2603-21692 | score_7_9 | selected | DA-20260324-27 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260324-27 |
| SF-2026-ARXIV-2603-21862 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-21862 |
| SF-2026-ARXIV-2603-22075 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22075 |
| SF-2026-ARXIV-2603-22078 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22078 |
| SF-2026-ARXIV-2603-22206 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22206 |
| SF-2026-ARXIV-2603-22212 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22212 |
| SF-2026-ARXIV-2603-22276 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22276 |
| SF-2026-ARXIV-2603-22286 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22286 |

<!-- analysis-decision:SF-2026-ARXIV-2603-20216:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20216:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20217:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20217:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20218:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20218:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20219:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20219:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20356:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20356:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20357:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20357:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20586:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20586:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20616:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20616:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20625:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20625:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20711:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20711:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20953:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20953:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21019:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21019:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21104:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21104:end -->
<!-- analysis:DA-20260324-14:start -->
### Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts

GRPO 每轮重新采样全部 prompt 浪费 rollout，而简单 replay 又会破坏 on-policy freshness。 旧路径在其原约束下仍合理：每条样本独立更新易实现，但难利用组内相对信号。 本 family 的设计变化是：方法只重放近期产生高方差/高信号 group outcome 的 prompt，再用当前 policy 重新 rollout，而不是复用旧 trajectory。 其公开验证边界为：基于 OLMo-RL 并在六个 benchmark 报告准确率/训练效率；结论绑定筛选规则和任务分布。 新增代价与回退条件为：prompt replay 提高样本利用率但可能过度聚焦困难样本并改变 curriculum；信号均匀时标准采样更稳。
<!-- analysis:DA-20260324-14:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21257:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21257:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21331:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21331:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21340:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21340:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21354:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21354:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21465:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21465:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21522:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21522:end -->
<!-- analysis:DA-20260324-22:start -->
### SafePilot: A Framework for Assuring LLM-enabled Cyber-Physical Systems

LLM 进入 CPS 后，语言层错误可能跨越到物理 action，纯模型准确率不能构成 safety assurance。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：SafePilot 在 LLM planner 与低层 controller 之间加入安全 monitor、可验证约束和 fallback 控制链。 其公开验证边界为：框架案例支持控制边界可实现，不等同于认证或真实事故率证明。 新增代价与回退条件为：monitor 限制开放式规划并增加延迟；封闭控制任务优先传统 verified controller。
<!-- analysis:DA-20260324-22:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21564:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21564:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21576:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21576:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21641:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21641:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21642:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21642:end -->
<!-- analysis:DA-20260324-27:start -->
### Reasoning Provenance for Autonomous AI Agents: Structured Behavioral Analytics Beyond State Checkpoints and Execution Traces

checkpoint 和 execution trace 能回答发生了什么，却难以跨调查聚合 agent 为什么选择某 action。 旧路径在其原约束下仍合理：日志记录结果适合单进程、短链路故障。 本 family 的设计变化是：论文提出 normalized reasoning-provenance schema，将观察、候选、选择依据与行动关联为可查询记录。 其公开验证边界为：主要贡献是数据模型和分析案例，不证明记录就是模型真实因果理由。 新增代价与回退条件为：更细 provenance 增加敏感数据与存储成本；调试单次失败时普通 trace 已足够。
<!-- analysis:DA-20260324-27:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-21862:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-21862:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22075:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22075:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22078:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22078:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22206:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22206:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22212:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22212:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22276:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22276:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22286:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22286:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-20216 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#diffusion：用迭代修正换并行状态更新 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20216 | delta:SF-2026-ARXIV-2603-20216 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20216 |
| SF-2026-ARXIV-2603-20217 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从经验-confidence-threshold-到有条件的-risk-contract (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20217 | delta:SF-2026-ARXIV-2603-20217 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20217 |
| SF-2026-ARXIV-2603-20218 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#kv-从生成私有状态演进为受约束的下游读出接口 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20218 | delta:SF-2026-ARXIV-2603-20218 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20218 |
| SF-2026-ARXIV-2603-20219 | MODEL-DECODER-ONLY | books/part-02-model/18-decoder-only.md#从显式-cot-到-latent-reasoning：减少-token-不等于消除状态 (section Ch-owner) | books/part-02-model/17-transformer-layer.md#第17章-transformer-layer (section Ch-adjacent); books/part-02-model/19-kv-cache.md#第19章-kv-cache (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20219 | delta:SF-2026-ARXIV-2603-20219 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20219 |
| SF-2026-ARXIV-2603-20356 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20356 | delta:SF-2026-ARXIV-2603-20356 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20356 |
| SF-2026-ARXIV-2603-20357 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#weight-streaming-的保密边界在片上明文状态才结束 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20357 | delta:SF-2026-ARXIV-2603-20357 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20357 |
| SF-2026-ARXIV-2603-20586 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#稀疏-kv-保留的是派生状态，不只是被抽样的-token (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20586 | delta:SF-2026-ARXIV-2603-20586 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20586 |
| SF-2026-ARXIV-2603-20616 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#agent-语义区域是-policy-hint，不是未来效用真值 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20616 | delta:SF-2026-ARXIV-2603-20616 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20616 |
| SF-2026-ARXIV-2603-20625 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#agent-自己的-instruction、config-与-memory-也是受保护资产 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20625 | delta:SF-2026-ARXIV-2603-20625 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20625 |
| SF-2026-ARXIV-2603-20711 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20711 | delta:SF-2026-ARXIV-2603-20711 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20711 |
| SF-2026-ARXIV-2603-20953 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#capability-access-control-可以前移到训练状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20953 | delta:SF-2026-ARXIV-2603-20953 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20953 |
| SF-2026-ARXIV-2603-21019 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21019 | delta:SF-2026-ARXIV-2603-21019 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21019 |
| SF-2026-ARXIV-2603-21104 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21104 | delta:SF-2026-ARXIV-2603-21104 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21104 |
| SF-2026-ARXIV-2603-21177 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21177 | delta:SF-2026-ARXIV-2603-21177 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-21177 |
| SF-2026-ARXIV-2603-21257 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21257 | delta:SF-2026-ARXIV-2603-21257 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21257 |
| SF-2026-ARXIV-2603-21331 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21331 | delta:SF-2026-ARXIV-2603-21331 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21331 |
| SF-2026-ARXIV-2603-21340 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21340 | delta:SF-2026-ARXIV-2603-21340 | Layering / Dependency | Disputed | books-review:SF-2026-ARXIV-2603-21340 |
| SF-2026-ARXIV-2603-21354 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21354 | delta:SF-2026-ARXIV-2603-21354 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21354 |
| SF-2026-ARXIV-2603-21383 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21383 | delta:SF-2026-ARXIV-2603-21383 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21383 |
| SF-2026-ARXIV-2603-21465 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#near-free-parallelism-只能消费不进入-critical-path-的-slack (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21465 | delta:SF-2026-ARXIV-2603-21465 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21465 |
| SF-2026-ARXIV-2603-21522 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#从单一-monitor-score-到多维、分权的运行证据 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21522 | delta:SF-2026-ARXIV-2603-21522 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21522 |
| SF-2026-ARXIV-2603-21523 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21523 | delta:SF-2026-ARXIV-2603-21523 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21523 |
| SF-2026-ARXIV-2603-21564 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21564 | delta:SF-2026-ARXIV-2603-21564 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21564 |
| SF-2026-ARXIV-2603-21576 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从不可逆-eviction-到可恢复的分层-recall (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21576 | delta:SF-2026-ARXIV-2603-21576 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21576 |
| SF-2026-ARXIV-2603-21641 | AGENT-MCP | books/part-07-agent/83-mcp.md#consequential-output-必须携带可独立验证的-claim-receipt (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21641 | delta:SF-2026-ARXIV-2603-21641 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21641 |
| SF-2026-ARXIV-2603-21642 | AGENT-MCP | books/part-07-agent/83-mcp.md#tool-catalog-扩大后，discovery-与-execution-必须分离 (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21642 | delta:SF-2026-ARXIV-2603-21642 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21642 |
| SF-2026-ARXIV-2603-21692 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#从单一-monitor-score-到多维、分权的运行证据 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21692 | delta:SF-2026-ARXIV-2603-21692 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21692 |
| SF-2026-ARXIV-2603-21862 | MODEL-MOE | books/part-02-model/21-moe.md#total-/-active-parameters-只是约束坐标，不是架构答案 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-21862 | delta:SF-2026-ARXIV-2603-21862 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-21862 |
| SF-2026-ARXIV-2603-22075 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22075 | delta:SF-2026-ARXIV-2603-22075 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22075 |
| SF-2026-ARXIV-2603-22078 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#tool-成功要从-component-扩展到-information-use-与-outcome (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22078 | delta:SF-2026-ARXIV-2603-22078 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22078 |
| SF-2026-ARXIV-2603-22206 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22206 | delta:SF-2026-ARXIV-2603-22206 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22206 |
| SF-2026-ARXIV-2603-22212 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22212 | delta:SF-2026-ARXIV-2603-22212 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22212 |
| SF-2026-ARXIV-2603-22276 | TRAIN-LORA | books/part-04-training-system/30-lora.md#high-rank-adapter-的瓶颈可能来自-intermediate，而不是参数本身 (section Ch-owner) | books/part-04-training-system/29-sft.md#第29章-sft (section Ch-adjacent); books/part-04-training-system/31-rlhf.md#第31章-rlhf (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22276 | delta:SF-2026-ARXIV-2603-22276 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22276 |
| SF-2026-ARXIV-2603-22286 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22286 | delta:SF-2026-ARXIV-2603-22286 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22286 |

<!-- books-review:SF-2026-ARXIV-2603-20216:start -->
### Locally Coherent Parallel Decoding in Diffusion Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20216:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。<!-- existing:SF-2026-ARXIV-2603-20216:end -->

<!-- delta:SF-2026-ARXIV-2603-20216:start -->新证据差异：CoDiLA 在每个并行 block 内引入短程 autoregressive coherence，同时保留 block 间并行修正。<!-- delta:SF-2026-ARXIV-2603-20216:end -->

边界：只支持 arXiv:2603.20216v1 §3 Method 的机制与 §A.2 Evaluation Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20216:end -->
<!-- books-review:SF-2026-ARXIV-2603-20217:start -->
### Expected Reward Prediction, with Applications to Model Routing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20217:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：多层模型 cascade 的 routing 可以从经验 confidence threshold 演进为带假设的 risk contract。每个 tier 用 held-out calibration 把 response frequency 或 logprob 转成 conformal prediction set；只有集合足够小才 commit，否则升级到更强模型。这样把误差预算与预计 cascade cost 放进同一调度状态。<!-- existing:SF-2026-ARXIV-2603-20217:end -->

<!-- delta:SF-2026-ARXIV-2603-20217:start -->新证据差异：论文估计每个模型对 prompt 的期望 reward，把 response-level scorer 提升为 pre-execution model-routing signal。<!-- delta:SF-2026-ARXIV-2603-20217:end -->

边界：只支持 arXiv:2603.20217v1 §Model Routing Methods. 的机制与 §Routing Evaluations. 的公开 workload；§5 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20217:end -->
<!-- books-review:SF-2026-ARXIV-2603-20218:start -->
### An experimental study of KV cache reuse strategies in chunk-level caching systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20218:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：对 KV 反向传播并直接修改 latent state 是另一条 Experimental 分支，不能与只读评分混在一起。它引入 reward hacking、不可解释 mutation、跨分支污染和 rollback 责任；必须使用 Copy-on-Write、版本化 branch state 与独立 outcome verifier。跨模型、跨信任域、cache 已释放、布局不兼容或需要更强独立复核时，重新 Prefill 的 text verifier 仍是正确方案。<!-- existing:SF-2026-ARXIV-2603-20218:end -->

<!-- delta:SF-2026-ARXIV-2603-20218:start -->新证据差异：研究在统一系统中比较多种 KV reuse 修复策略，明确哪些依赖可恢复、哪些结构性误差仍存在。<!-- delta:SF-2026-ARXIV-2603-20218:end -->

边界：只支持 arXiv:2603.20218v1 §3. Methodology 的机制与 §4. Experimental study 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20218:end -->
<!-- books-review:SF-2026-ARXIV-2603-20219:start -->
### Thinking into the Future: Latent Lookahead Training for Transformers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20219:start -->已读 owner `books/part-02-model/18-decoder-only.md` 与相邻章节。现有命题：显式 Chain-of-Thought 把中间步骤写成 token，优点是训练目标、停止条件、缓存和人工审计都复用语言模型接口；代价是每一步都要经过 vocabulary projection、采样和下一轮 Decode。将中间推理压缩成连续 latent state，可以少生成可见 token，却没有消除递归依赖：系统仍需决定 state representation、更新次数、termination、checkpoint identity 与失败恢复。<!-- existing:SF-2026-ARXIV-2603-20219:end -->

<!-- delta:SF-2026-ARXIV-2603-20219:start -->新证据差异：latent lookahead 在离散输出前训练隐藏的前瞻状态，让额外计算发生在未提交空间。<!-- delta:SF-2026-ARXIV-2603-20219:end -->

边界：只支持 arXiv:2603.20219v1 §3 Methodology 的机制与 §4 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20219:end -->
<!-- books-review:SF-2026-ARXIV-2603-20356:start -->
### Agentproof: Static Verification of Agent Workflow Graphs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20356:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-20356:end -->

<!-- delta:SF-2026-ARXIV-2603-20356:start -->新证据差异：Agentproof 从框架 API 抽取 graph，静态传播 node/tool 属性并检查不可达授权、缺失 human gate 等结构规则。<!-- delta:SF-2026-ARXIV-2603-20356:end -->

边界：只支持 arXiv:2603.20356v1 §4 System overview 的机制与 §7.3 Temporal policy evaluation 的公开 workload；§Human-node detection limitation. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20356:end -->
<!-- books-review:SF-2026-ARXIV-2603-20357:start -->
### Memory poisoning and secure multi-agent systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20357:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这条路径减少 off-chip plaintext exposure，却把 trusted die、SMMU/IOMMU 配置、counter/nonce lifecycle、SRAM isolation 与 scrub 正确性变成新的安全前置条件。SMMU 在这里约束 stream-ID 与地址映射，并不认证 ciphertext 或 DMA payload；AES-CTR 本身也不提供完整性。论文报告的近线速结果来自 proxy hardware measurement 与 idealized accelerator model，并非已制造 NPU silicon；它也不覆盖 invasive、side-channel 或 supply-chain adversary。因此该机制只能作为可信片上边界下的优化分支。缺少可信 die 或片上隔离时，平台必须缩小 confidentiality claim，或采用能覆盖目标 adversary 的受控 TEE/独立硬件边界；page-level memory encryption 只能回退保护较窄的 at-rest/DRAM threat，不能在同一 compromised-OS/physical adversary 下冒充等价保护。<!-- existing:SF-2026-ARXIV-2603-20357:end -->

<!-- delta:SF-2026-ARXIV-2603-20357:start -->新证据差异：论文按 memory duration、origin 与 location 建立威胁分类，并把 provenance、write authority 和 retrieval validation 作为隔离边界。<!-- delta:SF-2026-ARXIV-2603-20357:end -->

边界：只支持 arXiv:2603.20357v1 §3.1 Semantic memory poisoning attacks 的机制与 §Mitigation strategies against semantic memory poisoning attacks 的公开 workload；§4 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20357:end -->
<!-- books-review:SF-2026-ARXIV-2603-20586:start -->
### MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20586:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Full-context KV 把每个源 token 对应的派生表示都保留下来，最容易解释和回退；简单 token sampling 则默认“删除源 token 就删除了它的语义贡献”。Contextualized KV 打破了这个直觉：下游位置已经通过 attention 汇聚上游 observation， 因此一个被保留的 downstream row 可能仍携带某个已省略 event 的信息。稀疏 materialization 的对象于是从 token subset 演进为 **derived-state interface**：<!-- existing:SF-2026-ARXIV-2603-20586:end -->

<!-- delta:SF-2026-ARXIV-2603-20586:start -->新证据差异：MKA 用 memory key 在 L1/L2/L3 timescale 间动态路由 attention，在固定 KV 预算下选择不同层级的表示。<!-- delta:SF-2026-ARXIV-2603-20586:end -->

边界：只支持 arXiv:2603.20586v1 §4. Methodology 的机制与 §6.3. Experimental Results Analysis 的公开 workload；§6.7. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20586:end -->
<!-- books-review:SF-2026-ARXIV-2603-20616:start -->
### Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20616:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Attention-pattern classification 还可以从经验 taxonomy 推进到 temporal mechanism：若相邻 query 表示稳定， 结合 key continuity 与 relative position，attention 往往呈可预测的局部移动；query similarity 较低的层则可能 需要更多 retrieval budget。这个 signal 可用于 per-layer KV allocation，却仍只是 retention proxy，不能证明某个 token 不重要。模型、RoPE、domain 和 abrupt tool/code transition 都会改变 continuity；动态 statistic、窗口和 budget policy 必须进入 cache identity。静态均匀 budget 在 workload 稳定或校准不足时继续成立。<!-- existing:SF-2026-ARXIV-2603-20616:end -->

<!-- delta:SF-2026-ARXIV-2603-20616:start -->新证据差异：MixedDimKV 联合选择 token 与投影维度，并重排 memory layout、复用 projection matrix，以不同维数编码不同 KV 子空间。<!-- delta:SF-2026-ARXIV-2603-20616:end -->

边界：只支持 arXiv:2603.20616v1 §5 Implementation 的机制与 §6.2 Main Results on Long-Context Benchmarks 的公开 workload；§6.5 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20616:end -->
<!-- books-review:SF-2026-ARXIV-2603-20625:start -->
### ACRFence: Preventing Semantic Rollback Attacks in Agent Checkpoint-Restore — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20625:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：OS telemetry 只能看到操作与时序，不拥有 Agent intent；semantic detector 也可能把正常自修改误报为攻击。 某些 mutation 在系统调用层与正常行为不可区分，必须依赖更高层 workflow invariant、human approval 或恢复点。 静态 ACL 仍适合 instruction/config 等低变更层，动态检测只用于确实需要写入的层。Self-State Attacks 的论文 提供 threat matrix 与受控 traces，不证明其 detector 覆盖生产 workload，也不允许 Memory backup 绕过删除政策。<!-- existing:SF-2026-ARXIV-2603-20625:end -->

<!-- delta:SF-2026-ARXIV-2603-20625:start -->新证据差异：ACRFence 对 action 语义与 authority consumption 建立持久承诺，在 restore 后拒绝 action replay 与 credential resurrection。<!-- delta:SF-2026-ARXIV-2603-20625:end -->

边界：只支持 arXiv:2603.20625v1 §4. Mitigation: ACRFence 的机制与 §3. Attacks and Experimental Validation 的公开 workload；§6. Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20625:end -->
<!-- books-review:SF-2026-ARXIV-2603-20711:start -->
### RoboECC: Multi-Factor-Aware Edge-Cloud Collaborative Deployment for VLA Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20711:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-20711:end -->

<!-- delta:SF-2026-ARXIV-2603-20711:start -->新证据差异：RoboECC 联合 model-hardware segmentation 与 network-aware adjustment，运行时改变 VLA partition 和放置。<!-- delta:SF-2026-ARXIV-2603-20711:end -->

边界：只支持 arXiv:2603.20711v1 §IV RoboECC Framework 的机制与 §V-B1 Results in Simulation Benchmark 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20711:end -->
<!-- books-review:SF-2026-ARXIV-2603-20953:start -->
### Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20953:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：训练数据过滤也可以前移 capability boundary，但粒度不同。Document removal 改变整段分布；token-level loss mask 可以保留上下文、只阻断目标位置的梯度；token removal 更强，却会破坏 syntax 与 distribution。 三者都依赖 relevance classifier，不能从“被标成敏感”推出该 token 对能力具有完整因果贡献，也不能阻止 tool/in-context 重新获得能力。Classifier、mask policy、training revision 与 held-out capability evaluation 必须绑定；output policy 和 tool authorization 仍不可删除。该路线保持 `Status: Experimental`。<!-- existing:SF-2026-ARXIV-2603-20953:end -->

<!-- delta:SF-2026-ARXIV-2603-20953:start -->新证据差异：OAP 拦截 action proposal，将 principal、capability、policy 与请求参数绑定后再签发一次性执行许可。<!-- delta:SF-2026-ARXIV-2603-20953:end -->

边界：只支持 arXiv:2603.20953v1 §3.2 Architecture 的机制与 §2.2 Post-Hoc Evaluation 的公开 workload；§8.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20953:end -->
<!-- books-review:SF-2026-ARXIV-2603-21019:start -->
### SkillProbe: Security Auditing for Emerging Agent Skill Marketplaces via Multi-Agent Collaboration — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21019:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-21019:end -->

<!-- delta:SF-2026-ARXIV-2603-21019:start -->新证据差异：SkillProbe 组合多 agent 分工、静态扫描与可选动态执行，对 skill 的声明、代码行为和权限需求做交叉审计。<!-- delta:SF-2026-ARXIV-2603-21019:end -->

边界：只支持 arXiv:2603.21019v1 §3.4 System Implementation 的机制与 §4.3 Large-scale Empirical Audit 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21019:end -->
<!-- books-review:SF-2026-ARXIV-2603-21104:start -->
### CounterScene: Counterfactual Causal Reasoning in Generative World Models for Safety-Critical Closed-Loop Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21104:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-21104:end -->

<!-- delta:SF-2026-ARXIV-2603-21104:start -->新证据差异：CounterScene 把场景生成写成对 multi-agent dynamics 的 counterfactual intervention，比较改变特定因果变量后的 rollout。<!-- delta:SF-2026-ARXIV-2603-21104:end -->

边界：只支持 arXiv:2603.21104v1 §Implementation Details. 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21104:end -->
<!-- books-review:SF-2026-ARXIV-2603-21177:start -->
### Prompt replay: speeding up grpo with on-policy reuse of high-signal prompts — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21177:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2603-21177:end -->

<!-- delta:SF-2026-ARXIV-2603-21177:start -->新证据差异：方法只重放近期产生高方差/高信号 group outcome 的 prompt，再用当前 policy 重新 rollout，而不是复用旧 trajectory。<!-- delta:SF-2026-ARXIV-2603-21177:end -->

边界：只支持 arXiv:2603.21177v1 §Appendix B Algorithm 的机制与 §5.1 Main Results 的公开 workload；§6.2 Limitations & Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-21177:end -->
<!-- books-review:SF-2026-ARXIV-2603-21257:start -->
### CALVO: Improve Serving Efficiency for LLM Inferences with Intense Network Demands — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21257:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-21257:end -->

<!-- delta:SF-2026-ARXIV-2603-21257:start -->新证据差异：CALVO 将 KV block loading 建模为一等阶段，联合网络预取、请求排序和 GPU admission。<!-- delta:SF-2026-ARXIV-2603-21257:end -->

边界：只支持 arXiv:2603.21257v1 §3. Solution 的机制与 §4.3. Micro-benchmark Analysis 的公开 workload；§5. Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21257:end -->
<!-- books-review:SF-2026-ARXIV-2603-21331:start -->
### AutoKernel: Autonomous GPU Kernel Optimization via Iterative Agent-Driven Search — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21331:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。<!-- existing:SF-2026-ARXIV-2603-21331:end -->

<!-- delta:SF-2026-ARXIV-2603-21331:start -->新证据差异：AutoKernel 以 profile/Amdahl 排序优化目标，并用五阶段 correctness harness 约束每轮 Triton/CUDA 搜索。<!-- delta:SF-2026-ARXIV-2603-21331:end -->

边界：只支持 arXiv:2603.21331v1 §3 System Design 的机制与 §7 Experimental Evaluation 的公开 workload；§11 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21331:end -->
<!-- books-review:SF-2026-ARXIV-2603-21340:start -->
### ARYA: A Physics-Constrained Composable &amp; Deterministic World Model Architecture — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21340:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-21340:end -->

<!-- delta:SF-2026-ARXIV-2603-21340:start -->新证据差异：ARYA 提出由小型物理约束组件组合出的 deterministic state-transition architecture，把 causal interface 显式化。<!-- delta:SF-2026-ARXIV-2603-21340:end -->

边界：只支持 exact-v1 白皮书 §3 的公开架构描述；§11 的厂商 benchmark 主张缺少独立复核，因此维持 Disputed，不将生产部署、SOTA 或安全有效性作为已证实事实。 作者侧决定为 **Disputed**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-21340:end -->
<!-- books-review:SF-2026-ARXIV-2603-21354:start -->
### The Workload-Router-Pool Architecture for LLM Inference Optimization: A Vision Paper from the vLLM Semantic Router Project — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21354:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：但 fully-online、对抗性 arrival 且输出长度未知时，不存在 workload-independent 的万能最优策略。 Shortest-estimated-work 可以降低平均 flow time，却会饿死长请求；更保守的 future-feasibility check 减少 memory dead-end，却降低 utilization；reserve 抵抗预测误差，也直接减少可售 capacity。论文中的 单 worker、non-preemptive 算法因此只提供 impossibility boundary 与设计原则，不是 vLLM/SGLang 的 生产处方。实际系统还必须把 prefix reuse、chunked prefill、recompute/preemption、tenant fairness、 tail SLO 和预测校准放进同一 workload contract。<!-- existing:SF-2026-ARXIV-2603-21354:end -->

<!-- delta:SF-2026-ARXIV-2603-21354:start -->新证据差异：WRP vision 将 workload classification、router policy 与执行 pool 分层，主张每层拥有不同状态与扩缩周期。<!-- delta:SF-2026-ARXIV-2603-21354:end -->

边界：只支持 arXiv:2603.21354v1 §2.1 Pillar 1: Routing Architecture 的机制与 §Validated building blocks (separate systems, public benchmarks). 的公开 workload；§Agent serving and failure analysis. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21354:end -->
<!-- books-review:SF-2026-ARXIV-2603-21383:start -->
### PivotRL: High Accuracy Agentic Post-Training at Low Compute Cost — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21383:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-21383:end -->

<!-- delta:SF-2026-ARXIV-2603-21383:start -->新证据差异：PivotRL 离线识别 mixed-outcome pivot turn，只在局部 state 上组成 group-normalized 更新，并用 verifier 约束选择。<!-- delta:SF-2026-ARXIV-2603-21383:end -->

边界：只支持 arXiv:2603.21383v1 §3.1 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21383:end -->
<!-- books-review:SF-2026-ARXIV-2603-21465:start -->
### DRTriton: Large-Scale Synthetic Data Driven Reinforcement Learning for Triton Kernel Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21465:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：跨节点 fused/megakernel plan 还必须区分 **data movement completion** 与 **全局执行栅栏**。为每次传输等待统一 fence 最容易证明顺序，却会把 NIC、GPU kernel 和 expert compute 串行化；完全删除 fence 又可能让消费者读取尚未可见的数据。更细粒度的执行合同是让 producer 发布带 sequence/epoch 的 completion signal，consumer 只等待其真实依赖，并由 communicator owner 维护跨 rank ordering 与 coordinated abort：<!-- existing:SF-2026-ARXIV-2603-21465:end -->

<!-- delta:SF-2026-ARXIV-2603-21465:start -->新证据差异：DRTriton 组合合成 PyTorch-Triton pairs、可执行 correctness filter 与性能 reward 来训练 kernel policy。<!-- delta:SF-2026-ARXIV-2603-21465:end -->

边界：只支持 arXiv:2603.21465v1 §4 Training Pipeline 的机制与 §5.2 Results on Synthetic Benchmarks 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21465:end -->
<!-- books-review:SF-2026-ARXIV-2603-21522:start -->
### Efficient Failure Management for Multi-Agent Systems with Reasoning Trace Representation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21522:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：单一安全分数在 observer 可信、风险维度相关且只需粗粒度 gate 时便于部署；monitor 与 Agent 同源、可能共享盲点甚至串谋后，一个 scalar 会隐藏“目标一致但违反约束”或“推理看似连贯但 action trace 不一致”的结构。Trace owner 应保留 goal alignment、constraint adherence、reasoning coherence、safety awareness 与 action-trace consistency 等分维 observation，以及每个 observer 的身份和分歧。<!-- existing:SF-2026-ARXIV-2603-21522:end -->

<!-- delta:SF-2026-ARXIV-2603-21522:start -->新证据差异：论文把 reasoning trace 编码为可检索 failure representation，用历史相似模式辅助诊断与恢复。<!-- delta:SF-2026-ARXIV-2603-21522:end -->

边界：只支持 arXiv:2603.21522v1 §3. Methodology 的机制与 §2.2. Evaluation of Existing Embeddings on Reasoning Trace Representation 的公开 workload；§2.1. Failure Pattern Concentration in Multi-Agent Systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21522:end -->
<!-- books-review:SF-2026-ARXIV-2603-21523:start -->
### SafePilot: A Framework for Assuring LLM-enabled Cyber-Physical Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21523:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-21523:end -->

<!-- delta:SF-2026-ARXIV-2603-21523:start -->新证据差异：SafePilot 在 LLM planner 与低层 controller 之间加入安全 monitor、可验证约束和 fallback 控制链。<!-- delta:SF-2026-ARXIV-2603-21523:end -->

边界：只支持 arXiv:2603.21523v1 §4. System Design 的机制与 §5. Experiments 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21523:end -->
<!-- books-review:SF-2026-ARXIV-2603-21564:start -->
### Toward a Theory of Hierarchical Memory for Language Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21564:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-21564:end -->

<!-- delta:SF-2026-ARXIV-2603-21564:start -->新证据差异：论文用 (aggregation α, capacity C, timescale τ) 三元组统一 data memory 与 agent-trace memory 的层级设计。<!-- delta:SF-2026-ARXIV-2603-21564:end -->

边界：只支持 arXiv:2603.21564v1 §2.1 Core Definitions 的机制与 §3.1 Data and Trace Systems 的公开 workload；§4 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21564:end -->
<!-- books-review:SF-2026-ARXIV-2603-21576:start -->
### PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21576:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：当 cold tier 从单一 host memory 扩展到多块 SSD，容量不再是主要矛盾，访问并行度和数据布局才是。简单 hash 或 round-robin striping 假设每个 KV block 独立且请求分布均匀；实际检索若经常共同激活一组历史 blocks， 它们落到同一设备就会形成热点。可选分支可以离线学习 co-activation graph，把相关 block 分散到不同设备， 在线再协同 fetch、更新 hot cache：<!-- existing:SF-2026-ARXIV-2603-21576:end -->

<!-- delta:SF-2026-ARXIV-2603-21576:start -->新证据差异：PRISM 用光子相似搜索先做近常数时间 block selection，仅把被选 KV 送入电子 attention。<!-- delta:SF-2026-ARXIV-2603-21576:end -->

边界：只支持 arXiv:2603.21576v1 §III.1 System Overview 的机制与 §V System-Level Evaluation 的公开 workload；§VII.1 Limitations and Practical Considerations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21576:end -->
<!-- books-review:SF-2026-ARXIV-2603-21641:start -->
### Auditing MCP Servers for Over-Privileged Tool Capabilities — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21641:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：记录 server/tool/resource identity、latency、result size、policy decision、error/cancel，同时默认排除 credentials 和敏感 content。MCP 版本、capabilities 和 server trust level 也应进入 evidence。<!-- existing:SF-2026-ARXIV-2603-21641:end -->

<!-- delta:SF-2026-ARXIV-2603-21641:start -->新证据差异：审计器解析 Python/JSON tool metadata，联合静态规则与可选 sandbox 动态检查，输出 capability 与最小权限差异。<!-- delta:SF-2026-ARXIV-2603-21641:end -->

边界：只支持 arXiv:2603.21641v1 §2. Tool Architecture and Implementation 的机制与 §4. Evaluation 的公开 workload；§5. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21641:end -->
<!-- books-review:SF-2026-ARXIV-2603-21642:start -->
### Are AI-assisted Development Tools Immune to Prompt Injection? — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21642:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：把所有 tool schemas 在会话开始时注入 Context，目录小且稳定时最简单；当一个 gateway 聚合数百个 servers、数千个 tools 后，它会同时消耗上下文、放大 selection noise，并让用户无法知道能力位于哪个 server。Prompt caching 只能减少重复 prefill，不能释放逻辑 context，也不能改善 discoverability。<!-- existing:SF-2026-ARXIV-2603-21642:end -->

<!-- delta:SF-2026-ARXIV-2603-21642:start -->新证据差异：研究对真实 AI coding clients 实施 tool-poisoning，比较不同客户端、模型与交互阶段的权限跨越。<!-- delta:SF-2026-ARXIV-2603-21642:end -->

边界：只支持 arXiv:2603.21642v1 §4.1. Attack Implementation 的机制与 §5. Results and Analysis 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21642:end -->
<!-- books-review:SF-2026-ARXIV-2603-21692:start -->
### Reasoning Provenance for Autonomous AI Agents: Structured Behavioral Analytics Beyond State Checkpoints and Execution Traces — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21692:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：单一安全分数在 observer 可信、风险维度相关且只需粗粒度 gate 时便于部署；monitor 与 Agent 同源、可能共享盲点甚至串谋后，一个 scalar 会隐藏“目标一致但违反约束”或“推理看似连贯但 action trace 不一致”的结构。Trace owner 应保留 goal alignment、constraint adherence、reasoning coherence、safety awareness 与 action-trace consistency 等分维 observation，以及每个 observer 的身份和分歧。<!-- existing:SF-2026-ARXIV-2603-21692:end -->

<!-- delta:SF-2026-ARXIV-2603-21692:start -->新证据差异：论文提出 normalized reasoning-provenance schema，将观察、候选、选择依据与行动关联为可查询记录。<!-- delta:SF-2026-ARXIV-2603-21692:end -->

边界：只支持 arXiv:2603.21692v1 §7 Evaluation Methodology 的机制与 §7 Evaluation Methodology 的公开 workload；§3.3 Limitation: Self-Reported Reasoning 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21692:end -->
<!-- books-review:SF-2026-ARXIV-2603-21862:start -->
### Holistic Scaling Laws for Optimal Mixture-of-Experts Architecture Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-21862:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：小中规模搜索中拟合出的 exponent 可以帮助生成候选，不能成为跨规模定律。真实设计还必须把 HBM、 parallel divisibility、load imbalance、topology、kernel efficiency、training tokens 与 Serving SLO 加入 约束；当这些条件变化时，论文搜索空间内的“最优”也会变化。因此 total/active parameters 继续作为 model-card 粗 contract，architecture search 则必须用 loss evidence 与 system cost model 联合裁决。<!-- existing:SF-2026-ARXIV-2603-21862:end -->

<!-- delta:SF-2026-ARXIV-2603-21862:start -->新证据差异：论文在统一实验基础设施上拟合面向 MoE architecture 的 scaling relations，并把 compute budget 映射到结构组合。<!-- delta:SF-2026-ARXIV-2603-21862:end -->

边界：只支持 arXiv:2603.21862v1 §4 Decoupling and reducing MoE scaling dimensions 的机制与 §5.3 Results and scaling laws derivation 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-21862:end -->
<!-- books-review:SF-2026-ARXIV-2603-22075:start -->
### Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22075:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：为什么文本生成长期以 Autoregressive 为主，而图像和视频大量采用 Diffusion？Masked Diffusion 为什么能并行生成多个 token，却带来 mutable output、cache invalidation 和 streaming 难题？Block Diffusion、draft tree 和 correction loop 是同一条路线吗？<!-- existing:SF-2026-ARXIV-2603-22075:end -->

<!-- delta:SF-2026-ARXIV-2603-22075:start -->新证据差异：该工作固定 TinyStories 数据、step、batch、sequence 和 H100，分别训练 AR/MDLM，隔离生成范式作为实验变量。<!-- delta:SF-2026-ARXIV-2603-22075:end -->

边界：只支持 arXiv:2603.22075v1 §3.1 Controlled Variables 的机制与 §4.3 Generation Diversity: Quantitative Analysis 的公开 workload；§5.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22075:end -->
<!-- books-review:SF-2026-ARXIV-2603-22078:start -->
### Do World Action Models Generalize Better than VLAs? A Robustness Study — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22078:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Oracle retrieval 分支可以定位瓶颈，却不是生产系统成绩；增加 step budget 可能改善 coverage，也会制造循环与成本 尾部。MADQA 的受限 PDF collection 支持 `accuracy x grounding x effort x failure stage` 比单一正确率更有诊断性， 不证明其语料、模型排名或 tool budget 可外推到企业私有、多语言环境。Corpus 小、retrieval 稳定时 static RAG 仍更可控；多步 Agent 只有在 action trace、evidence provenance 与 refusal/recovery 一起评估时才增加可信度。<!-- existing:SF-2026-ARXIV-2603-22078:end -->

<!-- delta:SF-2026-ARXIV-2603-22078:start -->新证据差异：研究在共享 perturbation、任务和 action metric 下对两类模型做对照，隔离 world prediction 分支的条件收益。<!-- delta:SF-2026-ARXIV-2603-22078:end -->

边界：只支持 arXiv:2603.22078v1 §3.2 Evaluation Methods 的机制与 §3.2 Evaluation Methods 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22078:end -->
<!-- books-review:SF-2026-ARXIV-2603-22206:start -->
### Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22206:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。 生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入 真实 serving 的补全责任，而不是论文已经证明的反馈算法。<!-- existing:SF-2026-ARXIV-2603-22206:end -->

<!-- delta:SF-2026-ARXIV-2603-22206:start -->新证据差异：Chimera 在 vLLM 前加入异步 semantic router 与 length predictor，联合选择异构模型并形成批次。<!-- delta:SF-2026-ARXIV-2603-22206:end -->

边界：只支持 arXiv:2603.22206v1 §3.8 Implementation Details 的机制与 §4.3 Main Results 的公开 workload；§4.4 Ablations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22206:end -->
<!-- books-review:SF-2026-ARXIV-2603-22212:start -->
### Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22212:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-22212:end -->

<!-- delta:SF-2026-ARXIV-2603-22212:start -->新证据差异：Omni-WorldBench 以交互任务、物理原则和时序响应组织 suite，评估 observation-action-transition 而非单帧外观。<!-- delta:SF-2026-ARXIV-2603-22212:end -->

边界：只支持 arXiv:2603.22212v1 §2.1 World Models Design 的机制与 §5.3 Quantitative Evaluation Results and Analysis 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22212:end -->
<!-- books-review:SF-2026-ARXIV-2603-22276:start -->
### Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22276:start -->已读 owner `books/part-04-training-system/30-lora.md` 与相邻章节。现有命题：Runtime 需要按 training mode、shape crossover、precision、backend capability 与 compatibility guard 选择 fused backward、fused forward 或 eager fallback。这个 dispatch 是 checkpoint/runtime contract 的一部分， 不能隐藏成“同一个 kernel 在所有形状都更快”。Fused path 会带来数值非 bitwise identical、backend portability、FSDP/DTensor full-weight assumption 与 embedding compatibility 等新边界；小 tensor 或非 CUDA 环境仍应保留 eager 实现。高 rank 的可执行性改善，也不证明高 rank 对所有任务更优。<!-- existing:SF-2026-ARXIV-2603-22276:end -->

<!-- delta:SF-2026-ARXIV-2603-22276:start -->新证据差异：该工作把范数分解为 base、cross 与 Gram 项，并融合 kernel，避免创建 dense update。<!-- delta:SF-2026-ARXIV-2603-22276:end -->

边界：只支持 arXiv:2603.22276v1 §Memory measurement methodology. 的机制与 §Ablation. 的公开 workload；§6.2 Tradeoffs and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22276:end -->
<!-- books-review:SF-2026-ARXIV-2603-22286:start -->
### WorldCache: Content-Aware Caching for Accelerated Video World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22286:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-22286:end -->

<!-- delta:SF-2026-ARXIV-2603-22286:start -->新证据差异：WorldCache 按感知变化决定何时复用 cached activation，并在 runtime 动态启停，不修改模型权重。<!-- delta:SF-2026-ARXIV-2603-22286:end -->

边界：只支持 arXiv:2603.22286v1 §Appendix 0.B Implementation Details and Runtime Setup 的机制与 §4.2 Main Results 的公开 workload；§Appendix 0.H Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22286:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260324-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260324 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260324-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | conditionally accepted: retained family 均完成 exact-v1 review；普通 blocked/unverified=0，外部 disputed claim 已登记 Materials Request，且未写成已证实结论 | passed |
| SA-20260324-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260324-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260324/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 1 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 1 项 Books Integration：
- 更新并复核 `books/part-04-training-system/33-grpo.md`。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 普通 Gate finding=0；没有未执行的 review 或 writeback。
- 外部证据限制：SF-2026-ARXIV-2603-21340 保持 Disputed；精确缺失材料与可接受替代物见 `Materials Request Ledger`。该限制不会被伪装成已证实结论。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-SF-2026-ARXIV-2603-21340 | P2 Artifact | SF-2026-ARXIV-2603-21340 | — | — | 2026-W13 | arXiv:2603.21340v1; https://arxiv.org/abs/2603.21340v1 | version-matched benchmark configuration, raw result ledger and independently inspectable production/deployment artifact | 当前公开材料不能关闭 Disputed performance and deployment claims | author artifact with exact model/workload/hardware/evaluator identity or independent reproduction | 2603.21340v1.artifact | Disputed performance and deployment claims |

## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
