# Daily Research — 2026-03-17

**Research Date:** 2026-03-17

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-16 09:00:00 ～ 2026-03-17 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=1405/1405/1405；denominator=30、pre-denominator closures=1375。exact-v1 Review complete=30、blocked=0；Integrate 建议=0。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-17 |
| Window End | 2026-03-17 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260317-AUTHOR-30 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-16T09:00:00+08:00 | 2026-03-17T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 1405/1405 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 1405 | SF-2026-ARXIV-2603-13281;SF-2026-ARXIV-2603-13289;SF-2026-ARXIV-2603-13319;SF-2026-ARXIV-2603-13335;SF-2026-ARXIV-2603-13358;SF-2026-ARXIV-2603-13364;SF-2026-ARXIV-2603-13384;SF-2026-ARXIV-2603-13404;SF-2026-ARXIV-2603-13420;SF-2026-ARXIV-2603-13424;SF-2026-ARXIV-2603-13591;SF-2026-ARXIV-2603-13594;SF-2026-ARXIV-2603-13605;SF-2026-ARXIV-2603-13606;SF-2026-ARXIV-2603-13644;SF-2026-ARXIV-2603-13791;SF-2026-ARXIV-2603-13870;SF-2026-ARXIV-2603-13875;SF-2026-ARXIV-2603-13906;SF-2026-ARXIV-2603-13925;SF-2026-ARXIV-2603-13940;SF-2026-ARXIV-2603-13950;SF-2026-ARXIV-2603-13966;SF-2026-ARXIV-2603-14688;SF-2026-ARXIV-2603-14799;SF-2026-ARXIV-2603-14987;SF-2026-ARXIV-2603-15042;SF-2026-ARXIV-2603-15125;SF-2026-ARXIV-2603-15202;SF-2026-ARXIV-2603-15340 | pages=100; prefixes=00..99; final_cursor=end; registered=1405; screened=1405; retained=30; closure=1375 | 2026-03-17T01:00:00+00:00 | screening-ledger-final.json#sha256=46287e854498a0fb5eeb1fd715fb136a667f9a3866f78ae96e34ee9ac4f1d084; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260317:start -->作者侧已逐项筛选全部 1405 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260317:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-13281 | arXiv:2603.13281v1 | paper-v1:2603.13281 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13281 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13281 | no |
| SF-2026-ARXIV-2603-13289 | arXiv:2603.13289v1 | paper-v1:2603.13289 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13289 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13289 | no |
| SF-2026-ARXIV-2603-13319 | arXiv:2603.13319v1 | paper-v1:2603.13319 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13319 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13319 | no |
| SF-2026-ARXIV-2603-13335 | arXiv:2603.13335v1 | paper-v1:2603.13335 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13335 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13335 | no |
| SF-2026-ARXIV-2603-13358 | arXiv:2603.13358v1 | paper-v1:2603.13358 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13358 | self | — | new_in_window | INFER-PD-DISAGGREGATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13358 | no |
| SF-2026-ARXIV-2603-13364 | arXiv:2603.13364v1 | paper-v1:2603.13364 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13364 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13364 | no |
| SF-2026-ARXIV-2603-13384 | arXiv:2603.13384v1 | paper-v1:2603.13384 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13384 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13384 | no |
| SF-2026-ARXIV-2603-13404 | arXiv:2603.13404v1 | paper-v1:2603.13404 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13404 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13404 | no |
| SF-2026-ARXIV-2603-13420 | arXiv:2603.13420v1 | paper-v1:2603.13420 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13420 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13420 | no |
| SF-2026-ARXIV-2603-13424 | arXiv:2603.13424v1 | paper-v1:2603.13424 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13424 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13424 | no |
| SF-2026-ARXIV-2603-13591 | arXiv:2603.13591v1 | paper-v1:2603.13591 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13591 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13591 | no |
| SF-2026-ARXIV-2603-13594 | arXiv:2603.13594v1 | paper-v1:2603.13594 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13594 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13594 | no |
| SF-2026-ARXIV-2603-13605 | arXiv:2603.13605v1 | paper-v1:2603.13605 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13605 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13605 | no |
| SF-2026-ARXIV-2603-13606 | arXiv:2603.13606v1 | paper-v1:2603.13606 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13606 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13606 | no |
| SF-2026-ARXIV-2603-13644 | arXiv:2603.13644v1 | paper-v1:2603.13644 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13644 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13644 | no |
| SF-2026-ARXIV-2603-13791 | arXiv:2603.13791v1 | paper-v1:2603.13791 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13791 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13791 | no |
| SF-2026-ARXIV-2603-13870 | arXiv:2603.13870v1 | paper-v1:2603.13870 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13870 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13870 | no |
| SF-2026-ARXIV-2603-13875 | arXiv:2603.13875v1 | paper-v1:2603.13875 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13875 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13875 | no |
| SF-2026-ARXIV-2603-13906 | arXiv:2603.13906v1 | paper-v1:2603.13906 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13906 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13906 | no |
| SF-2026-ARXIV-2603-13925 | arXiv:2603.13925v1 | paper-v1:2603.13925 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13925 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13925 | no |
| SF-2026-ARXIV-2603-13940 | arXiv:2603.13940v1 | paper-v1:2603.13940 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13940 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13940 | no |
| SF-2026-ARXIV-2603-13950 | arXiv:2603.13950v1 | paper-v1:2603.13950 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13950 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13950 | no |
| SF-2026-ARXIV-2603-13966 | arXiv:2603.13966v1 | paper-v1:2603.13966 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13966 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13966 | no |
| SF-2026-ARXIV-2603-14688 | arXiv:2603.14688v1 | paper-v1:2603.14688 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-14688 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14688 | no |
| SF-2026-ARXIV-2603-14799 | arXiv:2603.14799v1 | paper-v1:2603.14799 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-14799 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14799 | no |
| SF-2026-ARXIV-2603-14987 | arXiv:2603.14987v1 | paper-v1:2603.14987 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-14987 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14987 | no |
| SF-2026-ARXIV-2603-15042 | arXiv:2603.15042v1 | paper-v1:2603.15042 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15042 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15042 | no |
| SF-2026-ARXIV-2603-15125 | arXiv:2603.15125v1 | paper-v1:2603.15125 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15125 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15125 | no |
| SF-2026-ARXIV-2603-15202 | arXiv:2603.15202v1 | paper-v1:2603.15202 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15202 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15202 | no |
| SF-2026-ARXIV-2603-15340 | arXiv:2603.15340v1 | paper-v1:2603.15340 | 2026-W12 | 2026-03-17 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15340 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15340 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-13281 | RP-864c2833e3d4cda8 | deep | arXiv:2603.13281v1 | SRC-ARXIV@arXiv:2603.13281v1 | arXiv:2603.13281v1 HTML — §A.2.2 Multi Model Architecture with LoRA Adapters [facet=method]; https://arxiv.org/html/2603.13281v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13281v1.html; sha256:6fcbdba2a1a86b405f0f4dfaab2943c7c5d802d52953832c2f2610041b12a0be | arXiv:2603.13281v1 HTML — §4.2 Accuracy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13281v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13281v1.html; sha256:6fcbdba2a1a86b405f0f4dfaab2943c7c5d802d52953832c2f2610041b12a0be | arXiv:2603.13281v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13281v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13281v1.html; sha256:6fcbdba2a1a86b405f0f4dfaab2943c7c5d802d52953832c2f2610041b12a0be | arXiv exact-v1 identity https://arxiv.org/abs/2603.13281v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13281 | complete |
| SF-2026-ARXIV-2603-13289 | RP-69950e66f76179ca | deep | arXiv:2603.13289v1 | SRC-ARXIV@arXiv:2603.13289v1 | arXiv:2603.13289v1 HTML — §4.1 Overall Architecture [facet=method]; https://arxiv.org/html/2603.13289v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13289v1.html; sha256:88e0a6b065050492bed908530439878c49be8999e2ec92f25fa3c8bb6f68ae87 | arXiv:2603.13289v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13289v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13289v1.html; sha256:88e0a6b065050492bed908530439878c49be8999e2ec92f25fa3c8bb6f68ae87 | arXiv:2603.13289v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13289v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13289v1.html; sha256:88e0a6b065050492bed908530439878c49be8999e2ec92f25fa3c8bb6f68ae87 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13289v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13289 | complete |
| SF-2026-ARXIV-2603-13319 | RP-6eb49a4fa3d9ad06 | deep | arXiv:2603.13319v1 | SRC-ARXIV@arXiv:2603.13319v1 | arXiv:2603.13319v1 HTML — §3 LightningRL: Breaking the Accuracy–Parallelism Trade-off [facet=method]; https://arxiv.org/html/2603.13319v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13319v1.html; sha256:c117dd2b93211b7581e25ce70241990655a4a4a2daee524986408fe12e7ac512 | arXiv:2603.13319v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13319v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13319v1.html; sha256:c117dd2b93211b7581e25ce70241990655a4a4a2daee524986408fe12e7ac512 | arXiv:2603.13319v1 HTML — §Appendix A Discussion on Value Model Incorporation [facet=limitations]; https://arxiv.org/html/2603.13319v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13319v1.html; sha256:c117dd2b93211b7581e25ce70241990655a4a4a2daee524986408fe12e7ac512 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13319v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13319 | complete |
| SF-2026-ARXIV-2603-13335 | RP-7053838165a925d3 | standard | arXiv:2603.13335v1 | SRC-ARXIV@arXiv:2603.13335v1 | arXiv:2603.13335v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.13335v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13335v1.html; sha256:9c3252164912ff98ab504bf309c312afcbdeeae9dc23d0cd1fbec33abc4562a7 | arXiv:2603.13335v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13335v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13335v1.html; sha256:9c3252164912ff98ab504bf309c312afcbdeeae9dc23d0cd1fbec33abc4562a7 | arXiv:2603.13335v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13335v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13335v1.html; sha256:9c3252164912ff98ab504bf309c312afcbdeeae9dc23d0cd1fbec33abc4562a7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13335v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13335 | complete |
| SF-2026-ARXIV-2603-13358 | RP-a404d8d1107a6daf | deep | arXiv:2603.13358v1 | SRC-ARXIV@arXiv:2603.13358v1 | arXiv:2603.13358v1 HTML — §5 PPD: Dynamic AP Routing System [facet=method]; https://arxiv.org/html/2603.13358v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13358v1.html; sha256:e8e4221ae4e5ab2fb04f7e0b475b2b82088857d8ed1f05a9488c7aa8d04a64f0 | arXiv:2603.13358v1 HTML — §6 Real-world Validation [facet=evaluation]; https://arxiv.org/html/2603.13358v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13358v1.html; sha256:e8e4221ae4e5ab2fb04f7e0b475b2b82088857d8ed1f05a9488c7aa8d04a64f0 | arXiv:2603.13358v1 HTML — §C.4 Failure Rate Analysis [facet=limitations]; https://arxiv.org/html/2603.13358v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13358v1.html; sha256:e8e4221ae4e5ab2fb04f7e0b475b2b82088857d8ed1f05a9488c7aa8d04a64f0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13358v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13358 | complete |
| SF-2026-ARXIV-2603-13364 | RP-8e7e37a2e32581f4 | deep | arXiv:2603.13364v1 | SRC-ARXIV@arXiv:2603.13364v1 | arXiv:2603.13364v1 HTML — §3.1 FineRMoE Architecture [facet=method]; https://arxiv.org/html/2603.13364v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13364v1.html; sha256:5ae821a94ee67274f90ddc35f79309ab488a191811778a019ad4717865282af4 | arXiv:2603.13364v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.13364v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13364v1.html; sha256:5ae821a94ee67274f90ddc35f79309ab488a191811778a019ad4717865282af4 | arXiv:2603.13364v1 HTML — §4.5 Ablation Study on Fine-Grained Configurations [facet=limitations]; https://arxiv.org/html/2603.13364v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13364v1.html; sha256:5ae821a94ee67274f90ddc35f79309ab488a191811778a019ad4717865282af4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13364v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13364 | complete |
| SF-2026-ARXIV-2603-13384 | RP-67445d57330a4d1a | deep | arXiv:2603.13384v1 | SRC-ARXIV@arXiv:2603.13384v1 | arXiv:2603.13384v1 HTML — §4.4 Implementation protocol [facet=method]; https://arxiv.org/html/2603.13384v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13384v1.html; sha256:1d697d4457815d91537efc72fb76e45d72414ee11f53b2a2880b17bc71e9468e | arXiv:2603.13384v1 HTML — §4.5 Evaluation metrics [facet=evaluation]; https://arxiv.org/html/2603.13384v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13384v1.html; sha256:1d697d4457815d91537efc72fb76e45d72414ee11f53b2a2880b17bc71e9468e | arXiv:2603.13384v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2603.13384v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13384v1.html; sha256:1d697d4457815d91537efc72fb76e45d72414ee11f53b2a2880b17bc71e9468e | arXiv exact-v1 identity https://arxiv.org/abs/2603.13384v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13384 | complete |
| SF-2026-ARXIV-2603-13404 | RP-9f7dd371950c34c4 | standard | arXiv:2603.13404v1 | SRC-ARXIV@arXiv:2603.13404v1 | arXiv:2603.13404v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.13404v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13404v1.html; sha256:2998135785c22abc4446c1d05188eb7e202c20c412e51679e1e7620e9f912b4c | arXiv:2603.13404v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.13404v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13404v1.html; sha256:2998135785c22abc4446c1d05188eb7e202c20c412e51679e1e7620e9f912b4c | arXiv:2603.13404v1 HTML — §Failure taxonomy. [facet=limitations]; https://arxiv.org/html/2603.13404v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13404v1.html; sha256:2998135785c22abc4446c1d05188eb7e202c20c412e51679e1e7620e9f912b4c | arXiv exact-v1 identity https://arxiv.org/abs/2603.13404v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13404 | complete |
| SF-2026-ARXIV-2603-13420 | RP-0f58efa482a459ef | standard | arXiv:2603.13420v1 | SRC-ARXIV@arXiv:2603.13420v1 | arXiv:2603.13420v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.13420v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13420v1.html; sha256:8a316cdc500cadbe75db44b5cf411e185c394157a3dde83abe1fcd018bb3a556 | arXiv:2603.13420v1 HTML — §5.2 Results [facet=evaluation]; https://arxiv.org/html/2603.13420v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13420v1.html; sha256:8a316cdc500cadbe75db44b5cf411e185c394157a3dde83abe1fcd018bb3a556 | arXiv:2603.13420v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13420v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13420v1.html; sha256:8a316cdc500cadbe75db44b5cf411e185c394157a3dde83abe1fcd018bb3a556 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13420v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13420 | complete |
| SF-2026-ARXIV-2603-13424 | RP-881c44dec79c12d9 | deep | arXiv:2603.13424v1 | SRC-ARXIV@arXiv:2603.13424v1 | arXiv:2603.13424v1 HTML — §3 Defense Design [facet=method]; https://arxiv.org/html/2603.13424v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13424v1.html; sha256:c7152de98218680cfdb190003a704e8c8c2272f909a6c68efb4f17ab2c3a7597 | arXiv:2603.13424v1 HTML — §4.1 Overall Ablation [facet=evaluation]; https://arxiv.org/html/2603.13424v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13424v1.html; sha256:c7152de98218680cfdb190003a704e8c8c2272f909a6c68efb4f17ab2c3a7597 | arXiv:2603.13424v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.13424v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13424v1.html; sha256:c7152de98218680cfdb190003a704e8c8c2272f909a6c68efb4f17ab2c3a7597 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13424v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13424 | complete |
| SF-2026-ARXIV-2603-13591 | RP-2f323ce40ac05659 | deep | arXiv:2603.13591v1 | SRC-ARXIV@arXiv:2603.13591v1 | arXiv:2603.13591v1 HTML — §5.1. Methodology [facet=method]; https://arxiv.org/html/2603.13591v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13591v1.html; sha256:dc2be0af7292eb2f63ce20aaeca58c509b55f351562cf7450c0f3640ebfddc92 | arXiv:2603.13591v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13591v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13591v1.html; sha256:dc2be0af7292eb2f63ce20aaeca58c509b55f351562cf7450c0f3640ebfddc92 | arXiv:2603.13591v1 HTML — §7. Conclusion [facet=limitations]; https://arxiv.org/html/2603.13591v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13591v1.html; sha256:dc2be0af7292eb2f63ce20aaeca58c509b55f351562cf7450c0f3640ebfddc92 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13591v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13591 | complete |
| SF-2026-ARXIV-2603-13594 | RP-1b0ae5c75b449b76 | deep | arXiv:2603.13594v1 | SRC-ARXIV@arXiv:2603.13594v1 | arXiv:2603.13594v1 HTML — §3 EnterpriseOps-Gym [facet=method]; https://arxiv.org/html/2603.13594v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13594v1.html; sha256:a206becc3e3855f14a7dc4cae405c3bf5fa02934def09f444671f748eeb38ce8 | arXiv:2603.13594v1 HTML — §4.2 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.13594v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13594v1.html; sha256:a206becc3e3855f14a7dc4cae405c3bf5fa02934def09f444671f748eeb38ce8 | arXiv:2603.13594v1 HTML — §5 Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.13594v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13594v1.html; sha256:a206becc3e3855f14a7dc4cae405c3bf5fa02934def09f444671f748eeb38ce8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13594v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13594 | complete |
| SF-2026-ARXIV-2603-13605 | RP-ca74dac6730a61a3 | deep | arXiv:2603.13605v1 | SRC-ARXIV@arXiv:2603.13605v1 | arXiv:2603.13605v1 HTML — §2.1. Core Abstractions [facet=method]; https://arxiv.org/html/2603.13605v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13605v1.html; sha256:27071129fc87a347b7425706dc6de7e90271841449f1e07f051104fcd60ce132 | arXiv:2603.13605v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13605v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13605v1.html; sha256:27071129fc87a347b7425706dc6de7e90271841449f1e07f051104fcd60ce132 | arXiv:2603.13605v1 HTML — §5. Conclusion [facet=limitations]; https://arxiv.org/html/2603.13605v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13605v1.html; sha256:27071129fc87a347b7425706dc6de7e90271841449f1e07f051104fcd60ce132 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13605v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13605 | complete |
| SF-2026-ARXIV-2603-13606 | RP-7a585527f7fa3f7b | deep | arXiv:2603.13606v1 | SRC-ARXIV@arXiv:2603.13606v1 | arXiv:2603.13606v1 HTML — §V-A Kernel Architecture [facet=method]; https://arxiv.org/html/2603.13606v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13606v1.html; sha256:a0a14ef8eeeb20cdffd5846b5a8a6ce55e4ceafb6830e2fe7c3114fdc359c2f9 | arXiv:2603.13606v1 HTML — §VII Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13606v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13606v1.html; sha256:a0a14ef8eeeb20cdffd5846b5a8a6ce55e4ceafb6830e2fe7c3114fdc359c2f9 | arXiv:2603.13606v1 HTML — §IX Conclusions and Future Work [facet=limitations]; https://arxiv.org/html/2603.13606v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13606v1.html; sha256:a0a14ef8eeeb20cdffd5846b5a8a6ce55e4ceafb6830e2fe7c3114fdc359c2f9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13606v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13606 | complete |
| SF-2026-ARXIV-2603-13644 | RP-3b05051a80a5d24d | deep | arXiv:2603.13644v1 | SRC-ARXIV@arXiv:2603.13644v1 | arXiv:2603.13644v1 HTML — §V StatePlane Architecture [facet=method]; https://arxiv.org/html/2603.13644v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13644v1.html; sha256:29216315053dd14bcb819fc460954a9fbf571b3703e865b996ab99299c5ac47a | arXiv:2603.13644v1 HTML — §XII-A Benchmark Suite [facet=evaluation]; https://arxiv.org/html/2603.13644v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13644v1.html; sha256:29216315053dd14bcb819fc460954a9fbf571b3703e865b996ab99299c5ac47a | arXiv:2603.13644v1 HTML — §XV Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.13644v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13644v1.html; sha256:29216315053dd14bcb819fc460954a9fbf571b3703e865b996ab99299c5ac47a | arXiv exact-v1 identity https://arxiv.org/abs/2603.13644v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13644 | complete |
| SF-2026-ARXIV-2603-13791 | RP-80957d9958cd37d6 | deep | arXiv:2603.13791v1 | SRC-ARXIV@arXiv:2603.13791v1 | arXiv:2603.13791v1 HTML — §5.2 Generation Architecture [facet=method]; https://arxiv.org/html/2603.13791v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13791v1.html; sha256:deeab42f7ba72470bf548268b471afdac0bca5d428911486c902e37d16aa25f8 | arXiv:2603.13791v1 HTML — §7 DeceptArena: Evaluation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.13791v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13791v1.html; sha256:deeab42f7ba72470bf548268b471afdac0bca5d428911486c902e37d16aa25f8 | arXiv:2603.13791v1 HTML — §9.3 Limitations [facet=limitations]; https://arxiv.org/html/2603.13791v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13791v1.html; sha256:deeab42f7ba72470bf548268b471afdac0bca5d428911486c902e37d16aa25f8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13791v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13791 | complete |
| SF-2026-ARXIV-2603-13870 | RP-1072c34f32557500 | deep | arXiv:2603.13870v1 | SRC-ARXIV@arXiv:2603.13870v1 | arXiv:2603.13870v1 HTML — §Implementation and extensions. [facet=method]; https://arxiv.org/html/2603.13870v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13870v1.html; sha256:33597bdd5a7bd3024b58999eb276690bf3047f18f00df63db592174df9a170ab | arXiv:2603.13870v1 HTML — §LLM judges for screening and evaluation. [facet=evaluation]; https://arxiv.org/html/2603.13870v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13870v1.html; sha256:33597bdd5a7bd3024b58999eb276690bf3047f18f00df63db592174df9a170ab | arXiv:2603.13870v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13870v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13870v1.html; sha256:33597bdd5a7bd3024b58999eb276690bf3047f18f00df63db592174df9a170ab | arXiv exact-v1 identity https://arxiv.org/abs/2603.13870v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13870 | complete |
| SF-2026-ARXIV-2603-13875 | RP-2aa200038c094c00 | deep | arXiv:2603.13875v1 | SRC-ARXIV@arXiv:2603.13875v1 | arXiv:2603.13875v1 HTML — §2.2 GradMem: Test-Time Gradient Descent Memory [facet=method]; https://arxiv.org/html/2603.13875v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13875v1.html; sha256:db1aebf2191a80dc9d720ec0150f2a33ba406f4b6b8c911b0ca72982029d0b59 | arXiv:2603.13875v1 HTML — §3.3 Results on KV-retrieval task [facet=evaluation]; https://arxiv.org/html/2603.13875v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13875v1.html; sha256:db1aebf2191a80dc9d720ec0150f2a33ba406f4b6b8c911b0ca72982029d0b59 | arXiv:2603.13875v1 HTML — §4 Discussion and Conclusions [facet=limitations]; https://arxiv.org/html/2603.13875v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13875v1.html; sha256:db1aebf2191a80dc9d720ec0150f2a33ba406f4b6b8c911b0ca72982029d0b59 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13875v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13875 | complete |
| SF-2026-ARXIV-2603-13906 | RP-8adea8c5819c9527 | deep | arXiv:2603.13906v1 | SRC-ARXIV@arXiv:2603.13906v1 | arXiv:2603.13906v1 HTML — §4.3. Cost-Aware Reward Design [facet=method]; https://arxiv.org/html/2603.13906v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13906v1.html; sha256:3b0584d45700b8241b8dd09bf00fecdd07fa53d1c41d7c8cbf6e278cbe25056c | arXiv:2603.13906v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13906v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13906v1.html; sha256:3b0584d45700b8241b8dd09bf00fecdd07fa53d1c41d7c8cbf6e278cbe25056c | arXiv:2603.13906v1 HTML — §5.6. Discussion [facet=limitations]; https://arxiv.org/html/2603.13906v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13906v1.html; sha256:3b0584d45700b8241b8dd09bf00fecdd07fa53d1c41d7c8cbf6e278cbe25056c | arXiv exact-v1 identity https://arxiv.org/abs/2603.13906v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13906 | complete |
| SF-2026-ARXIV-2603-13925 | RP-04bee9e9e0af376d | standard | arXiv:2603.13925v1 | SRC-ARXIV@arXiv:2603.13925v1 | arXiv:2603.13925v1 HTML — §4.1.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.13925v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13925v1.html; sha256:10b1c23bffa11bca904debeeb62a48b4e2c1762b27d8eea182586acb8046eaf2 | arXiv:2603.13925v1 HTML — §4.2.3 Results [facet=evaluation]; https://arxiv.org/html/2603.13925v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13925v1.html; sha256:10b1c23bffa11bca904debeeb62a48b4e2c1762b27d8eea182586acb8046eaf2 | arXiv:2603.13925v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13925v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13925v1.html; sha256:10b1c23bffa11bca904debeeb62a48b4e2c1762b27d8eea182586acb8046eaf2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13925v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13925 | complete |
| SF-2026-ARXIV-2603-13940 | RP-32d9d9bf1bc8c75f | deep | arXiv:2603.13940v1 | SRC-ARXIV@arXiv:2603.13940v1 | arXiv:2603.13940v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.13940v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13940v1.html; sha256:03556a21e846f67b0bfd1e678ff3c8033f6a5b3a1762da9f48f824e45b619d96 | arXiv:2603.13940v1 HTML — §Appendix A Detailed Experimental Results across Topologies [facet=evaluation]; https://arxiv.org/html/2603.13940v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13940v1.html; sha256:03556a21e846f67b0bfd1e678ff3c8033f6a5b3a1762da9f48f824e45b619d96 | arXiv:2603.13940v1 HTML — §Limitation [facet=limitations]; https://arxiv.org/html/2603.13940v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13940v1.html; sha256:03556a21e846f67b0bfd1e678ff3c8033f6a5b3a1762da9f48f824e45b619d96 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13940v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13940 | complete |
| SF-2026-ARXIV-2603-13950 | RP-be8e5caf8e8e5912 | deep | arXiv:2603.13950v1 | SRC-ARXIV@arXiv:2603.13950v1 | arXiv:2603.13950v1 HTML — §2.1 Agent Design Patterns and Tool Ecosystems [facet=method]; https://arxiv.org/html/2603.13950v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13950v1.html; sha256:569b95f23056837849bea2091b79fb72fb05c6c5803557dd6930c4e46755c824 | arXiv:2603.13950v1 HTML — §5.4 Main results [facet=evaluation]; https://arxiv.org/html/2603.13950v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13950v1.html; sha256:569b95f23056837849bea2091b79fb72fb05c6c5803557dd6930c4e46755c824 | arXiv:2603.13950v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.13950v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13950v1.html; sha256:569b95f23056837849bea2091b79fb72fb05c6c5803557dd6930c4e46755c824 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13950v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13950 | complete |
| SF-2026-ARXIV-2603-13966 | RP-14503628f94c7c70 | deep | arXiv:2603.13966v1 | SRC-ARXIV@arXiv:2603.13966v1 | arXiv:2603.13966v1 HTML — §II-A Architecture [facet=method]; https://arxiv.org/html/2603.13966v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13966v1.html; sha256:2bb5da0f7b0f40c9fe3519126aa7d3a411f53563c01c9b7b33c417e43b414488 | arXiv:2603.13966v1 HTML — §II-C Parallel Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13966v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13966v1.html; sha256:2bb5da0f7b0f40c9fe3519126aa7d3a411f53563c01c9b7b33c417e43b414488 | arXiv:2603.13966v1 HTML — §V Discussion [facet=limitations]; https://arxiv.org/html/2603.13966v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13966v1.html; sha256:2bb5da0f7b0f40c9fe3519126aa7d3a411f53563c01c9b7b33c417e43b414488 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13966v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13966 | complete |
| SF-2026-ARXIV-2603-14688 | RP-30be91bc32073326 | deep | arXiv:2603.14688v1 | SRC-ARXIV@arXiv:2603.14688v1 | arXiv:2603.14688v1 HTML — §3.2 Causal Graph Construction [facet=method]; https://arxiv.org/html/2603.14688v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14688v1.html; sha256:5b0d4c61ca9718a903fa8d958c4cc0b563994ff8747111df88735094ad8649ad | arXiv:2603.14688v1 HTML — §5.1 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.14688v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14688v1.html; sha256:5b0d4c61ca9718a903fa8d958c4cc0b563994ff8747111df88735094ad8649ad | arXiv:2603.14688v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.14688v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14688v1.html; sha256:5b0d4c61ca9718a903fa8d958c4cc0b563994ff8747111df88735094ad8649ad | arXiv exact-v1 identity https://arxiv.org/abs/2603.14688v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-14688 | complete |
| SF-2026-ARXIV-2603-14799 | RP-152ba0651a8b7b28 | deep | arXiv:2603.14799v1 | SRC-ARXIV@arXiv:2603.14799v1 | arXiv:2603.14799v1 HTML — §3.3 Model Architecture [facet=method]; https://arxiv.org/html/2603.14799v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14799v1.html; sha256:a4b39bdc13f3e61b6718c0ad020e93f8e16f209946dcb4b6b688a533e5413ba1 | arXiv:2603.14799v1 HTML — §4.1 Main Results: Semantic Understanding vs. Keyword Matching [facet=evaluation]; https://arxiv.org/html/2603.14799v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14799v1.html; sha256:a4b39bdc13f3e61b6718c0ad020e93f8e16f209946dcb4b6b688a533e5413ba1 | arXiv:2603.14799v1 HTML — §5 Discussion [facet=limitations]; https://arxiv.org/html/2603.14799v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14799v1.html; sha256:a4b39bdc13f3e61b6718c0ad020e93f8e16f209946dcb4b6b688a533e5413ba1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.14799v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-14799 | complete |
| SF-2026-ARXIV-2603-14987 | RP-b7a448a7d859d63f | deep | arXiv:2603.14987v1 | SRC-ARXIV@arXiv:2603.14987v1 | arXiv:2603.14987v1 HTML — §3.5. Layer 4: Distribution-Aware Representative Sampling [facet=method]; https://arxiv.org/html/2603.14987v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14987v1.html; sha256:9670088caf162e9e0eb9dc81e4dfa62665aebef43d170e30f11f4f61e20d038c | arXiv:2603.14987v1 HTML — §Re-evaluation (second red-team pass). [facet=evaluation]; https://arxiv.org/html/2603.14987v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14987v1.html; sha256:9670088caf162e9e0eb9dc81e4dfa62665aebef43d170e30f11f4f61e20d038c | arXiv:2603.14987v1 HTML — §Limitations and future work. [facet=limitations]; https://arxiv.org/html/2603.14987v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14987v1.html; sha256:9670088caf162e9e0eb9dc81e4dfa62665aebef43d170e30f11f4f61e20d038c | arXiv exact-v1 identity https://arxiv.org/abs/2603.14987v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-14987 | complete |
| SF-2026-ARXIV-2603-15042 | RP-11c044fe3f5c0f91 | deep | arXiv:2603.15042v1 | SRC-ARXIV@arXiv:2603.15042v1 | arXiv:2603.15042v1 HTML — §4 DetShare Design [facet=method]; https://arxiv.org/html/2603.15042v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15042v1.html; sha256:f64912d59362f573e46b763803cd861e4906e08d1efc8e44af8d13c5cf3fd56f | arXiv:2603.15042v1 HTML — §6.1 End-to-End Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15042v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15042v1.html; sha256:f64912d59362f573e46b763803cd861e4906e08d1efc8e44af8d13c5cf3fd56f | arXiv:2603.15042v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.15042v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15042v1.html; sha256:f64912d59362f573e46b763803cd861e4906e08d1efc8e44af8d13c5cf3fd56f | arXiv exact-v1 identity https://arxiv.org/abs/2603.15042v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15042 | complete |
| SF-2026-ARXIV-2603-15125 | RP-234f165181a8737b | deep | arXiv:2603.15125v1 | SRC-ARXIV@arXiv:2603.15125v1 | arXiv:2603.15125v1 HTML — §3.3 Methodology: MemFlow [facet=method]; https://arxiv.org/html/2603.15125v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15125v1.html; sha256:5ec8efcc4c7c4951072da6535be8479ad59c4b21a511231eb45cd076a9791ecf | arXiv:2603.15125v1 HTML — §4.2 Main Results: MCFA Vulnerability Landscape [facet=evaluation]; https://arxiv.org/html/2603.15125v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15125v1.html; sha256:5ec8efcc4c7c4951072da6535be8479ad59c4b21a511231eb45cd076a9791ecf | arXiv:2603.15125v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.15125v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15125v1.html; sha256:5ec8efcc4c7c4951072da6535be8479ad59c4b21a511231eb45cd076a9791ecf | arXiv exact-v1 identity https://arxiv.org/abs/2603.15125v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15125 | complete |
| SF-2026-ARXIV-2603-15202 | RP-9c144542922e87db | deep | arXiv:2603.15202v1 | SRC-ARXIV@arXiv:2603.15202v1 | arXiv:2603.15202v1 HTML — §The Analysis Framework [facet=method]; https://arxiv.org/html/2603.15202v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15202v1.html; sha256:23d1b76ab2c9191429e0dba3872e6c9a63f8bf2ae4a0ac9058a8edcb3b994e16 | arXiv:2603.15202v1 HTML — §End-to-end Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15202v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15202v1.html; sha256:23d1b76ab2c9191429e0dba3872e6c9a63f8bf2ae4a0ac9058a8edcb3b994e16 | arXiv:2603.15202v1 HTML — §Benign and Failure Cases Analysis of Multiplication-based Scheduling Score [facet=limitations]; https://arxiv.org/html/2603.15202v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15202v1.html; sha256:23d1b76ab2c9191429e0dba3872e6c9a63f8bf2ae4a0ac9058a8edcb3b994e16 | arXiv exact-v1 identity https://arxiv.org/abs/2603.15202v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15202 | complete |
| SF-2026-ARXIV-2603-15340 | RP-cea7cc8da9467250 | deep | arXiv:2603.15340v1 | SRC-ARXIV@arXiv:2603.15340v1 | arXiv:2603.15340v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.15340v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15340v1.html; sha256:60c2158ed442d703868688a5806ace0d4b2fbfb2f9aba5755d45c39e7e43828e | arXiv:2603.15340v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.15340v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15340v1.html; sha256:60c2158ed442d703868688a5806ace0d4b2fbfb2f9aba5755d45c39e7e43828e | arXiv:2603.15340v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.15340v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15340v1.html; sha256:60c2158ed442d703868688a5806ace0d4b2fbfb2f9aba5755d45c39e7e43828e | arXiv exact-v1 identity https://arxiv.org/abs/2603.15340v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15340 | complete |

### Source Reviews

### ICaRus: Identical Cache Reuse for Efficient Multi Model Inference

<!-- review:SF-2026-ARXIV-2603-13281:start -->
**问题**：相同 prompt 在异构模型间仍会生成不同形状的 KV，常规 prefix cache 因模型身份隔离而重复计算。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：ICaRus 只共享一个冻结 logical encoder 产生的模型无关中间表示，再由各目标模型映射为本模型 KV；复用身份从‘同模型 prefix’上移到‘相同逻辑输入’。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.13281v1 HTML — §A.2.2 Multi Model Architecture with LoRA Adapters [facet=method]; https://arxiv.org/html/2603.13281v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13281v1.html; sha256:6fcbdba2a1a86b405f0f4dfaab2943c7c5d802d52953832c2f2610041b12a0be`。

**Evaluation contract 与未证明部分**：作者比较多模型服务的内存与尾延迟；证据限于论文中的模型配对、映射器和请求分布，不能推出任意模型都能无损共享。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13281v1 HTML — §4.2 Accuracy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13281v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13281v1.html; sha256:6fcbdba2a1a86b405f0f4dfaab2943c7c5d802d52953832c2f2610041b12a0be`。

**Trade-off / failure / coexistence**：共享 encoder 和映射器新增训练、版本一致性与误差面；单模型或映射成本高于 prefill 时，普通 prefix cache 仍合理。

<!-- claim:SF-2026-ARXIV-2603-13281:start -->**Claim Boundary**：只支持 arXiv:2603.13281v1 §A.2.2 Multi Model Architecture with LoRA Adapters 的机制与 §4.2 Accuracy Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13281:end -->
<!-- review:SF-2026-ARXIV-2603-13281:end -->
### RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse

<!-- review:SF-2026-ARXIV-2603-13289:start -->
**问题**：agent 生成的上游文本会成为下游模型输入，逐模型重新 prefill 使协作链的 TTFT 随 hop 累积。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：RelayCaching 把上游 decode 过程中已有的 KV 作为转换输入，只对语义敏感位置选择性重算，改变了跨模型 handoff 的状态所有权。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.13289v1 HTML — §4.1 Overall Architecture [facet=method]; https://arxiv.org/html/2603.13289v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13289v1.html; sha256:88e0a6b065050492bed908530439878c49be8999e2ec92f25fa3c8bb6f68ae87`。

**Evaluation contract 与未证明部分**：exact-v1 比较端到端协作任务的速度与质量；它只证明所测模型组合和阈值下的条件性复用。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13289v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13289v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13289v1.html; sha256:88e0a6b065050492bed908530439878c49be8999e2ec92f25fa3c8bb6f68ae87`。

**Trade-off / failure / coexistence**：错误选择会把表示偏差传入下游；异构程度高或准确性优先时完整 prefill 仍是回退路径。

<!-- claim:SF-2026-ARXIV-2603-13289:start -->**Claim Boundary**：只支持 arXiv:2603.13289v1 §4.1 Overall Architecture 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13289:end -->
<!-- review:SF-2026-ARXIV-2603-13289:end -->
### LightningRL: Breaking the Accuracy-Parallelism Trade-off of Block-wise dLLMs via Reinforcement Learning

<!-- review:SF-2026-ARXIV-2603-13319:start -->
**问题**：block diffusion 同时提交更多 token 会积累局部错误，静态并行度无法兼顾速度与稳定性。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：LightningRL 用奖励把并行 token 数与生成正确性共同纳入策略，使 block-level proposal 的提交宽度成为可训练控制量。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.13319v1 HTML — §3 LightningRL: Breaking the Accuracy–Parallelism Trade-off [facet=method]; https://arxiv.org/html/2603.13319v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13319v1.html; sha256:c117dd2b93211b7581e25ce70241990655a4a4a2daee524986408fe12e7ac512`。

**Evaluation contract 与未证明部分**：论文在指定 dLLM、任务和 tokens-per-forward 配置上报告速度/质量曲线；不证明该奖励可迁移到所有扩散解码器。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13319v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13319v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13319v1.html; sha256:c117dd2b93211b7581e25ce70241990655a4a4a2daee524986408fe12e7ac512`。

**Trade-off / failure / coexistence**：更高并行度换来 rollout 成本和策略不稳定；低延迟压力不强时保守 block size 仍更稳。

<!-- claim:SF-2026-ARXIV-2603-13319:start -->**Claim Boundary**：只支持 arXiv:2603.13319v1 §3 LightningRL: Breaking the Accuracy–Parallelism Trade-off 的机制与 §4.2 Main Results 的公开 workload；§Appendix A Discussion on Value Model Incorporation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13319:end -->
<!-- review:SF-2026-ARXIV-2603-13319:end -->
### Information-Theoretic Constraints for Continual Vision-Language-Action Alignment

<!-- review:SF-2026-ARXIV-2603-13335:start -->
**问题**：VLA 连续学习新技能时，视觉、语言和动作之间的信息依赖比单模态参数更早漂移。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：Info-VLA 把跨模态 mutual-information 结构作为保留对象，用约束项保护旧技能的对齐关系。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.13335v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.13335v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13335v1.html; sha256:9c3252164912ff98ab504bf309c312afcbdeeae9dc23d0cd1fbec33abc4562a7`。

**Evaluation contract 与未证明部分**：实验测量连续任务上的遗忘和新技能学习；结果不能证明信息估计器在开放机器人流中保持校准。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13335v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13335v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13335v1.html; sha256:9c3252164912ff98ab504bf309c312afcbdeeae9dc23d0cd1fbec33abc4562a7`。

**Trade-off / failure / coexistence**：保护旧依赖会限制可塑性并增加估计成本；任务分布固定时普通微调仍更简单。

<!-- claim:SF-2026-ARXIV-2603-13335:start -->**Claim Boundary**：只支持 arXiv:2603.13335v1 §4 Methodology 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13335:end -->
<!-- review:SF-2026-ARXIV-2603-13335:end -->
### Not All Prefills Are Equal: PPD Disaggregation for Multi-turn LLM Serving

<!-- review:SF-2026-ARXIV-2603-13358:start -->
**问题**：经典 prefill/decode 分离假设一次 prefill 后持续 decode；多轮会话却反复追加 prompt 并迁移 KV，使每轮都产生新 prefill。

**旧路径为何合理**：prefill 与 decode 共置便于共享权重和 KV，低负载下最少网络跳转。

**约束变化与机制**：PPD 将初始 prefill 与增量 prefill 分开，并依据会话阶段在 AP/P/D pool 间动态路由，减少重复传输和资源干扰。

**State / data / control owner**：`INFER-PD-DISAGGREGATION` 负责 阶段拆分、KV handoff 与资源池选择；定位证据为 `arXiv:2603.13358v1 HTML — §5 PPD: Dynamic AP Routing System [facet=method]; https://arxiv.org/html/2603.13358v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13358v1.html; sha256:e8e4221ae4e5ab2fb04f7e0b475b2b82088857d8ed1f05a9488c7aa8d04a64f0`。

**Evaluation contract 与未证明部分**：真实 workload 实验支持论文集群中的 TTFT/TPOT 权衡；不同 KV fabric、模型和会话长度需重新测量。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13358v1 HTML — §6 Real-world Validation [facet=evaluation]; https://arxiv.org/html/2603.13358v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13358v1.html; sha256:e8e4221ae4e5ab2fb04f7e0b475b2b82088857d8ed1f05a9488c7aa8d04a64f0`。

**Trade-off / failure / coexistence**：多一类 pool 增加容量规划与 KV handoff 状态；短单轮请求仍适合普通 PD 或共置。

<!-- claim:SF-2026-ARXIV-2603-13358:start -->**Claim Boundary**：只支持 arXiv:2603.13358v1 §5 PPD: Dynamic AP Routing System 的机制与 §6 Real-world Validation 的公开 workload；§C.4 Failure Rate Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13358:end -->
<!-- review:SF-2026-ARXIV-2603-13358:end -->
### FineRMoE: Dimension Expansion for Finer-Grained Expert with Its Upcycling Approach

<!-- review:SF-2026-ARXIV-2603-13364:start -->
**问题**：只切分 FFN 中间维度的细粒度 expert 达到最优粒度后，继续切分不再增加有效容量。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：FineRMoE 同时沿 intermediate 与 output 维扩展专家，并用二级稀疏路由控制两层激活，改变 expert granularity 与通信组合。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.13364v1 HTML — §3.1 FineRMoE Architecture [facet=method]; https://arxiv.org/html/2603.13364v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13364v1.html; sha256:5ae821a94ee67274f90ddc35f79309ab488a191811778a019ad4717865282af4`。

**Evaluation contract 与未证明部分**：作者模型实验支持其设定下的质量/计算关系；未证明跨网络拓扑的通信收益。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13364v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.13364v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13364v1.html; sha256:5ae821a94ee67274f90ddc35f79309ab488a191811778a019ad4717865282af4`。

**Trade-off / failure / coexistence**：更细路由增加负载均衡、kernel 和 all-to-all 复杂度；规模较小时 dense 或单层 MoE 仍占优。

<!-- claim:SF-2026-ARXIV-2603-13364:start -->**Claim Boundary**：只支持 arXiv:2603.13364v1 §3.1 FineRMoE Architecture 的机制与 §4 Experiments 的公开 workload；§4.5 Ablation Study on Fine-Grained Configurations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13364:end -->
<!-- review:SF-2026-ARXIV-2603-13364:end -->
### VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection

<!-- review:SF-2026-ARXIV-2603-13384:start -->
**问题**：仓库漏洞取决于跨文件数据流和构建条件，单函数分类缺少可复核证据与置信校准。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：VulnAgent-R2 把反事实证据重加权、build-aware 验证计划和成本风险调度组成多 agent 审计控制面。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13384v1 HTML — §4.4 Implementation protocol [facet=method]; https://arxiv.org/html/2603.13384v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13384v1.html; sha256:1d697d4457815d91537efc72fb76e45d72414ee11f53b2a2880b17bc71e9468e`。

**Evaluation contract 与未证明部分**：评测支持所选仓库、漏洞类型和预算下的检测/成本权衡；不能证明自动 verifier 消除误报。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13384v1 HTML — §4.5 Evaluation metrics [facet=evaluation]; https://arxiv.org/html/2603.13384v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13384v1.html; sha256:1d697d4457815d91537efc72fb76e45d72414ee11f53b2a2880b17bc71e9468e`。

**Trade-off / failure / coexistence**：更完整证据链增加工具执行成本和攻击面；局部规则明确的代码仍适合静态分析。

<!-- claim:SF-2026-ARXIV-2603-13384:start -->**Claim Boundary**：只支持 arXiv:2603.13384v1 §4.4 Implementation protocol 的机制与 §4.5 Evaluation metrics 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13384:end -->
<!-- review:SF-2026-ARXIV-2603-13384:end -->
### Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance

<!-- review:SF-2026-ARXIV-2603-13404:start -->
**问题**：工具语义相同并不意味着接口等价；自由文本说明会让解析错误与恢复成本不可归因。

**旧路径为何合理**：工具少且能力固定时，模型直接按说明生成参数最简单。

**约束变化与机制**：该受控实验固定工具能力，只改变 free-form、JSON Schema 与结构化诊断，隔离 schema contract 对 action formation 的影响。

**State / data / control owner**：`AGENT-TOOL-CALLING` 负责 tool identity、retrieval admission、argument validation 与执行许可；定位证据为 `arXiv:2603.13404v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.13404v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13404v1.html; sha256:2998135785c22abc4446c1d05188eb7e202c20c412e51679e1e7620e9f912b4c`。

**Evaluation contract 与未证明部分**：一款本地模型、三组种子和确定性 sandbox 只能建立 pilot 级因果证据，不能外推其他模型。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13404v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.13404v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13404v1.html; sha256:2998135785c22abc4446c1d05188eb7e202c20c412e51679e1e7620e9f912b4c`。

**Trade-off / failure / coexistence**：schema 降低歧义却增加接口治理和验证开销；简单只读工具仍可用轻量说明。

<!-- claim:SF-2026-ARXIV-2603-13404:start -->**Claim Boundary**：只支持 arXiv:2603.13404v1 §5 Methodology 的机制与 §6 Experiments 的公开 workload；§Failure taxonomy. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13404:end -->
<!-- review:SF-2026-ARXIV-2603-13404:end -->
### Accelerating Suffix Jailbreak attacks with Prefix-Shared KV-cache

<!-- review:SF-2026-ARXIV-2603-13420:start -->
**问题**：大批 jailbreak suffix 候选共享同一有害前缀，重复计算相同 prefix KV 使红队搜索成本被 prefill 主导。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：PSKV 将共享前缀的 KV 设为只读基态，在候选 suffix 间复用，仅让差异部分进入搜索循环。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13420v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.13420v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13420v1.html; sha256:8a316cdc500cadbe75db44b5cf411e185c394157a3dde83abe1fcd018bb3a556`。

**Evaluation contract 与未证明部分**：论文证明所测攻击生成配置的计算节省；它不证明攻击成功率在不同防护模型上保持。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13420v1 HTML — §5.2 Results [facet=evaluation]; https://arxiv.org/html/2603.13420v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13420v1.html; sha256:8a316cdc500cadbe75db44b5cf411e185c394157a3dde83abe1fcd018bb3a556`。

**Trade-off / failure / coexistence**：复用加速同样会提高攻击吞吐，部署侧应把它视为双用机制；候选前缀不共享时无收益。

<!-- claim:SF-2026-ARXIV-2603-13420:start -->**Claim Boundary**：只支持 arXiv:2603.13420v1 §4 Methodology 的机制与 §5.2 Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13420:end -->
<!-- review:SF-2026-ARXIV-2603-13420:end -->
### Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection

<!-- review:SF-2026-ARXIV-2603-13424:start -->
**问题**：同一 agent 同时读取不可信内容并持有高权限工具，会让 prompt injection 直接跨越到副作用。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：防御把读取/解析与行动拆为两个权限域，并以结构化 JSON 作为唯一跨域消息，缩小污染上下文可控制的能力集合。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13424v1 HTML — §3 Defense Design [facet=method]; https://arxiv.org/html/2603.13424v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13424v1.html; sha256:c7152de98218680cfdb190003a704e8c8c2272f909a6c68efb4f17ab2c3a7597`。

**Evaluation contract 与未证明部分**：649 个已成功攻击上的对照支持该 OpenClaw 配置中的风险下降；不证明格式化可净化所有语义攻击。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13424v1 HTML — §4.1 Overall Ablation [facet=evaluation]; https://arxiv.org/html/2603.13424v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13424v1.html; sha256:c7152de98218680cfdb190003a704e8c8c2272f909a6c68efb4f17ab2c3a7597`。

**Trade-off / failure / coexistence**：隔离增加模型调用与信息损失，错误 schema 仍可携带恶意意图；无副作用工具可使用更薄边界。

<!-- claim:SF-2026-ARXIV-2603-13424:start -->**Claim Boundary**：只支持 arXiv:2603.13424v1 §3 Defense Design 的机制与 §4.1 Overall Ablation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13424:end -->
<!-- review:SF-2026-ARXIV-2603-13424:end -->
### d-HNSW: A High-performance Vector Search Engine on Disaggregated Memory

<!-- review:SF-2026-ARXIV-2603-13591:start -->
**问题**：HNSW 图遍历具有细粒度随机访存，直接搬到 disaggregated memory 会被 RDMA round trip 放大。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：d-HNSW 重排图索引与访问批次，使 compute node 以 RDMA 预取/聚合远端邻接状态，而不是逐边同步读取。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.13591v1 HTML — §5.1. Methodology [facet=method]; https://arxiv.org/html/2603.13591v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13591v1.html; sha256:dc2be0af7292eb2f63ce20aaeca58c509b55f351562cf7450c0f3640ebfddc92`。

**Evaluation contract 与未证明部分**：论文 testbed 支持其索引、网络和查询分布下的吞吐/召回；未证明跨 fabric 或强更新负载同样成立。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13591v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13591v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13591v1.html; sha256:dc2be0af7292eb2f63ce20aaeca58c509b55f351562cf7450c0f3640ebfddc92`。

**Trade-off / failure / coexistence**：批量远端读取增加陈旧性和预取浪费；内存可本地容纳时单机 HNSW 更简单。

<!-- claim:SF-2026-ARXIV-2603-13591:start -->**Claim Boundary**：只支持 arXiv:2603.13591v1 §5.1. Methodology 的机制与 §5. Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13591:end -->
<!-- review:SF-2026-ARXIV-2603-13591:end -->
### EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings

<!-- review:SF-2026-ARXIV-2603-13594:start -->
**问题**：静态 tool benchmark 不含持久数据库、权限和长程副作用，无法测出 enterprise agent 的状态一致性失败。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：EnterpriseOps-Gym 用容器化数据库、512 个工具和跨步状态转移定义可重放的规划环境。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.13594v1 HTML — §3 EnterpriseOps-Gym [facet=method]; https://arxiv.org/html/2603.13594v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13594v1.html; sha256:a206becc3e3855f14a7dc4cae405c3bf5fa02934def09f444671f748eeb38ce8`。

**Evaluation contract 与未证明部分**：基准能比较其任务集合上的完成率和协议遵循；不代表真实企业权限模型与长尾流程。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13594v1 HTML — §4.2 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.13594v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13594v1.html; sha256:a206becc3e3855f14a7dc4cae405c3bf5fa02934def09f444671f748eeb38ce8`。

**Trade-off / failure / coexistence**：更真实的 stateful evaluation 代价是环境维护和 oracle 复杂；窄工具技能仍可用单步测试。

<!-- claim:SF-2026-ARXIV-2603-13594:start -->**Claim Boundary**：只支持 arXiv:2603.13594v1 §3 EnterpriseOps-Gym 的机制与 §4.2 Evaluation Metrics 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13594:end -->
<!-- review:SF-2026-ARXIV-2603-13594:end -->
### Orla: A Library for Serving LLM-Based Multi-Agent Systems

<!-- review:SF-2026-ARXIV-2603-13605:start -->
**问题**：agent workflow 同时含模型调用、工具和依赖边，直接把 orchestration 代码绑在单一 serving engine 上难以更换策略。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Orla 把 workflow policy 与 request execution 解耦，在 engine 之上统一表达依赖、并发和后端选择。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.13605v1 HTML — §2.1. Core Abstractions [facet=method]; https://arxiv.org/html/2603.13605v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13605v1.html; sha256:27071129fc87a347b7425706dc6de7e90271841449f1e07f051104fcd60ce132`。

**Evaluation contract 与未证明部分**：公开 evaluation 证明 library abstraction 可承载所测 agent workloads；不证明其调度在所有后端达到最优。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13605v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13605v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13605v1.html; sha256:27071129fc87a347b7425706dc6de7e90271841449f1e07f051104fcd60ce132`。

**Trade-off / failure / coexistence**：中间层提升可移植性但增加状态同步和调试跨度；简单单模型 chain 可直接调用 engine。

<!-- claim:SF-2026-ARXIV-2603-13605:start -->**Claim Boundary**：只支持 arXiv:2603.13605v1 §2.1. Core Abstractions 的机制与 §4. Evaluation 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13605:end -->
<!-- review:SF-2026-ARXIV-2603-13605:end -->
### NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL

<!-- review:SF-2026-ARXIV-2603-13606:start -->
**问题**：MoE dispatch/combine 依赖 device-initiated RDMA，但各专用库拥有不兼容 API 和通信状态。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：NCCL EP 在 NCCL Device API 上提供统一 dispatch/combine，并把 low-latency 与 high-throughput 路径纳入同一通信接口。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.13606v1 HTML — §V-A Kernel Architecture [facet=method]; https://arxiv.org/html/2603.13606v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13606v1.html; sha256:a0a14ef8eeeb20cdffd5846b5a8a6ce55e4ceafb6830e2fe7c3114fdc359c2f9`。

**Evaluation contract 与未证明部分**：多 GPU/NIC 实验支持指定拓扑和 message shape；不能外推所有 expert placement 或网络。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13606v1 HTML — §VII Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13606v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13606v1.html; sha256:a0a14ef8eeeb20cdffd5846b5a8a6ce55e4ceafb6830e2fe7c3114fdc359c2f9`。

**Trade-off / failure / coexistence**：统一 API 降低集成成本但受 NCCL 语义约束；专用栈在固定拓扑仍可能更快。

<!-- claim:SF-2026-ARXIV-2603-13606:start -->**Claim Boundary**：只支持 arXiv:2603.13606v1 §V-A Kernel Architecture 的机制与 §VII Performance Evaluation 的公开 workload；§IX Conclusions and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13606:end -->
<!-- review:SF-2026-ARXIV-2603-13606:end -->
### StatePlane: A Cognitive State Plane for Long-Horizon AI Systems Under Bounded Context

<!-- review:SF-2026-ARXIV-2603-13644:start -->
**问题**：RAG、摘要和长 context 都把历史当作文本，无法显式保存跨会话的决策状态、置信和失效条件。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：StatePlane 把 belief、goal、decision 和 evidence 变成独立于 context window 的 versioned state，由 policy 决定写入、压缩和回注。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.13644v1 HTML — §V StatePlane Architecture [facet=method]; https://arxiv.org/html/2603.13644v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13644v1.html; sha256:29216315053dd14bcb819fc460954a9fbf571b3703e865b996ab99299c5ac47a`。

**Evaluation contract 与未证明部分**：benchmark/case study 支持原型在长任务中的状态保持；不证明自动抽取的认知状态始终正确。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13644v1 HTML — §XII-A Benchmark Suite [facet=evaluation]; https://arxiv.org/html/2603.13644v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13644v1.html; sha256:29216315053dd14bcb819fc460954a9fbf571b3703e865b996ab99299c5ac47a`。

**Trade-off / failure / coexistence**：外部 state plane 增加冲突、权限和一致性负担；短会话仍应优先原始 context。

<!-- claim:SF-2026-ARXIV-2603-13644:start -->**Claim Boundary**：只支持 arXiv:2603.13644v1 §V StatePlane Architecture 的机制与 §XII-A Benchmark Suite 的公开 workload；§XV Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13644:end -->
<!-- review:SF-2026-ARXIV-2603-13644:end -->
### DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents

<!-- review:SF-2026-ARXIV-2603-13791:start -->
**问题**：只观察输出和 tool call 的黑盒 monitor 看不到 deception 在内部推理中形成但尚未执行的阶段。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：DeceptGuard 在同一任务上对比 black-box、CoT-aware 与 activation-probe 三种监控信号，显式测量可见性与干预面。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13791v1 HTML — §5.2 Generation Architecture [facet=method]; https://arxiv.org/html/2603.13791v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13791v1.html; sha256:deeab42f7ba72470bf548268b471afdac0bca5d428911486c902e37d16aa25f8`。

**Evaluation contract 与未证明部分**：结果限于所用模型、可访问内部状态和 deception 任务；不证明 CoT 等于真实因果理由。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13791v1 HTML — §7 DeceptArena: Evaluation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.13791v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13791v1.html; sha256:deeab42f7ba72470bf548268b471afdac0bca5d428911486c902e37d16aa25f8`。

**Trade-off / failure / coexistence**：内部监控提高召回但需要模型特权访问并可能被自适应规避；托管模型只能退回行为监控。

<!-- claim:SF-2026-ARXIV-2603-13791:start -->**Claim Boundary**：只支持 arXiv:2603.13791v1 §5.2 Generation Architecture 的机制与 §7 DeceptArena: Evaluation Benchmark 的公开 workload；§9.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13791:end -->
<!-- review:SF-2026-ARXIV-2603-13791:end -->
### When to Screen, When to Bypass: LLM-Judges in Resource-Scarce AI-Human Workflow

<!-- review:SF-2026-ARXIV-2603-13870:start -->
**问题**：AI 输出进入人工审批队列时，额外 judge 既可能减负，也可能因误判增加返工和排队。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文把 judge 与 human reviewer 建模为串联/旁路队列，用准确率和服务率求何时 screening 优于直接人工。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.13870v1 HTML — §Implementation and extensions. [facet=method]; https://arxiv.org/html/2603.13870v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13870v1.html; sha256:33597bdd5a7bd3024b58999eb276690bf3047f18f00df63db592174df9a170ab`。

**Evaluation contract 与未证明部分**：结论是参数化队列模型的条件边界，不是对特定 judge 的通用性能证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13870v1 HTML — §LLM judges for screening and evaluation. [facet=evaluation]; https://arxiv.org/html/2603.13870v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13870v1.html; sha256:33597bdd5a7bd3024b58999eb276690bf3047f18f00df63db592174df9a170ab`。

**Trade-off / failure / coexistence**：judge 增加一层延迟与相关错误；人工容量充足或 judge 校准差时直接审核更合理。

<!-- claim:SF-2026-ARXIV-2603-13870:start -->**Claim Boundary**：只支持 arXiv:2603.13870v1 §Implementation and extensions. 的机制与 §LLM judges for screening and evaluation. 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13870:end -->
<!-- review:SF-2026-ARXIV-2603-13870:end -->
### GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent

<!-- review:SF-2026-ARXIV-2603-13875:start -->
**问题**：长上下文若只能保存逐层 KV，单个上下文的持久状态随 token 线性增长且难跨查询复用。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：GradMem 通过少量 test-time gradient steps 把一次性上下文写入紧凑参数状态，查询时不再读取原文。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.13875v1 HTML — §2.2 GradMem: Test-Time Gradient Descent Memory [facet=method]; https://arxiv.org/html/2603.13875v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13875v1.html; sha256:db1aebf2191a80dc9d720ec0150f2a33ba406f4b6b8c911b0ca72982029d0b59`。

**Evaluation contract 与未证明部分**：context-removal 实验支持所测任务中的压缩记忆能力；不能证明写入状态保持事实完整或适合频繁更新。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13875v1 HTML — §3.3 Results on KV-retrieval task [facet=evaluation]; https://arxiv.org/html/2603.13875v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13875v1.html; sha256:db1aebf2191a80dc9d720ec0150f2a33ba406f4b6b8c911b0ca72982029d0b59`。

**Trade-off / failure / coexistence**：每上下文优化增加写延迟和污染风险；短会话或要求逐字 provenance 时原始 context/KV 更可靠。

<!-- claim:SF-2026-ARXIV-2603-13875:start -->**Claim Boundary**：只支持 arXiv:2603.13875v1 §2.2 GradMem: Test-Time Gradient Descent Memory 的机制与 §3.3 Results on KV-retrieval task 的公开 workload；§4 Discussion and Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13875:end -->
<!-- review:SF-2026-ARXIV-2603-13875:end -->
### ATCC: Adaptive Concurrency Control for Unforeseen Agentic Transactions

<!-- review:SF-2026-ARXIV-2603-13906:start -->
**问题**：agent 事务会根据中间结果动态生成 SQL，持续时间、间隔和读写集合都无法预先估计。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：ATCC 在线观察冲突与阶段进度，在乐观/悲观控制间自适应切换，把 agent plan evolution 纳入数据库并发控制。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.13906v1 HTML — §4.3. Cost-Aware Reward Design [facet=method]; https://arxiv.org/html/2603.13906v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13906v1.html; sha256:3b0584d45700b8241b8dd09bf00fecdd07fa53d1c41d7c8cbf6e278cbe25056c`。

**Evaluation contract 与未证明部分**：事务 workload 的对照支持指定冲突模式下的吞吐/abort 权衡；不证明任意 LLM workflow 都可安全预测。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13906v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13906v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13906v1.html; sha256:3b0584d45700b8241b8dd09bf00fecdd07fa53d1c41d7c8cbf6e278cbe25056c`。

**Trade-off / failure / coexistence**：自适应器增加控制状态和误切换风险；访问模式稳定的传统事务仍适合固定协议。

<!-- claim:SF-2026-ARXIV-2603-13906:start -->**Claim Boundary**：只支持 arXiv:2603.13906v1 §4.3. Cost-Aware Reward Design 的机制与 §6. Evaluation 的公开 workload；§5.6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13906:end -->
<!-- review:SF-2026-ARXIV-2603-13906:end -->
### SmoothVLA: Aligning Vision-Language-Action Models with Physical Constraints via Intrinsic Smoothness Optimization

<!-- review:SF-2026-ARXIV-2603-13925:start -->
**问题**：VLA 的 RL 探索可能提高任务成功率，却产生违反机械系统约束的抖动轨迹。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：SmoothVLA 把 task reward 与速度/加速度平滑项联合优化，使物理可执行性进入 policy objective。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.13925v1 HTML — §4.1.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.13925v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13925v1.html; sha256:10b1c23bffa11bca904debeeb62a48b4e2c1762b27d8eea182586acb8046eaf2`。

**Evaluation contract 与未证明部分**：机器人任务结果支持所测 embodiment 的成功率/平滑度折中；不能把平滑等同于安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13925v1 HTML — §4.2.3 Results [facet=evaluation]; https://arxiv.org/html/2603.13925v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13925v1.html; sha256:10b1c23bffa11bca904debeeb62a48b4e2c1762b27d8eea182586acb8046eaf2`。

**Trade-off / failure / coexistence**：平滑约束可能抑制必要快速动作；低速或高质量示范充分时 SFT 仍可用。

<!-- claim:SF-2026-ARXIV-2603-13925:start -->**Claim Boundary**：只支持 arXiv:2603.13925v1 §4.1.1 Implementation Details 的机制与 §4.2.3 Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13925:end -->
<!-- review:SF-2026-ARXIV-2603-13925:end -->
### GroupGuard: A Framework for Modeling and Defending Collusive Attacks in Multi-Agent Systems

<!-- review:SF-2026-ARXIV-2603-13940:start -->
**问题**：多 agent 可通过协同而非单点恶意绕过逐 agent trust 检查。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：GroupGuard 维护交互图，结合持续监测、honeypot 诱导和结构剪枝识别并隔离可疑 coalition。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13940v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.13940v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13940v1.html; sha256:03556a21e846f67b0bfd1e678ff3c8033f6a5b3a1762da9f48f824e45b619d96`。

**Evaluation contract 与未证明部分**：五个数据集上的结果支持论文攻击模型内的检测；不证明未知协商信道或自适应联盟可被覆盖。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13940v1 HTML — §Appendix A Detailed Experimental Results across Topologies [facet=evaluation]; https://arxiv.org/html/2603.13940v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13940v1.html; sha256:03556a21e846f67b0bfd1e678ff3c8033f6a5b3a1762da9f48f824e45b619d96`。

**Trade-off / failure / coexistence**：图监控会误伤高协作子群并增加通信审计成本；固定可信拓扑可采用静态 ACL。

<!-- claim:SF-2026-ARXIV-2603-13940:start -->**Claim Boundary**：只支持 arXiv:2603.13940v1 §3 Methodology 的机制与 §Appendix A Detailed Experimental Results across Topologies 的公开 workload；§Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13940:end -->
<!-- review:SF-2026-ARXIV-2603-13940:end -->
### ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering

<!-- review:SF-2026-ARXIV-2603-13950:start -->
**问题**：工具检索只展示 top-k 时，攻击者无需诱导错误选择，只需让合法工具在候选集前被挤出。

**旧路径为何合理**：工具少且能力固定时，模型直接按说明生成参数最简单。

**约束变化与机制**：ToolFlood 在 embedding 空间布置少量恶意 metadata 形成 semantic covering，攻击的是 retrieval admission 而非后续 planner。

**State / data / control owner**：`AGENT-TOOL-CALLING` 负责 tool identity、retrieval admission、argument validation 与执行许可；定位证据为 `arXiv:2603.13950v1 HTML — §2.1 Agent Design Patterns and Tool Ecosystems [facet=method]; https://arxiv.org/html/2603.13950v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13950v1.html; sha256:569b95f23056837849bea2091b79fb72fb05c6c5803557dd6930c4e46755c824`。

**Evaluation contract 与未证明部分**：实验支持特定 embedding、tool corpus 和 k 值下的可用性攻击；不证明所有检索器同等脆弱。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13950v1 HTML — §5.4 Main results [facet=evaluation]; https://arxiv.org/html/2603.13950v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13950v1.html; sha256:569b95f23056837849bea2091b79fb72fb05c6c5803557dd6930c4e46755c824`。

**Trade-off / failure / coexistence**：防御需验证工具身份、限制注册和监控候选覆盖；全量小工具集可跳过向量检索。

<!-- claim:SF-2026-ARXIV-2603-13950:start -->**Claim Boundary**：只支持 arXiv:2603.13950v1 §2.1 Agent Design Patterns and Tool Ecosystems 的机制与 §5.4 Main results 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13950:end -->
<!-- review:SF-2026-ARXIV-2603-13950:end -->
### vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models

<!-- review:SF-2026-ARXIV-2603-13966:start -->
**问题**：VLA benchmark 的依赖、预处理和执行协议彼此不兼容，使跨模型比较难以复算。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：vla-eval 用 WebSocket/msgpack 隔离模型推理与 Docker benchmark runtime，把环境版本和消息协议变成显式 contract。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.13966v1 HTML — §II-A Architecture [facet=method]; https://arxiv.org/html/2603.13966v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13966v1.html; sha256:2bb5da0f7b0f40c9fe3519126aa7d3a411f53563c01c9b7b33c417e43b414488`。

**Evaluation contract 与未证明部分**：公开 harness 证明多个模拟环境可统一执行；不证明 benchmark 指标代表真实物理安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13966v1 HTML — §II-C Parallel Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13966v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.13966v1.html; sha256:2bb5da0f7b0f40c9fe3519126aa7d3a411f53563c01c9b7b33c417e43b414488`。

**Trade-off / failure / coexistence**：隔离提高复现性但引入协议延迟和镜像维护；单一环境可保留原生 runner。

<!-- claim:SF-2026-ARXIV-2603-13966:start -->**Claim Boundary**：只支持 arXiv:2603.13966v1 §II-A Architecture 的机制与 §II-C Parallel Evaluation 的公开 workload；§V Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13966:end -->
<!-- review:SF-2026-ARXIV-2603-13966:end -->
### AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems

<!-- review:SF-2026-ARXIV-2603-14688:start -->
**问题**：多 agent 故障会沿调用和共享状态级联，仅按时间线查看日志难以定位最早原因。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：AgentTrace 从执行日志重建因果图，从最终错误反向遍历并按传播关系排序候选根因。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `arXiv:2603.14688v1 HTML — §3.2 Causal Graph Construction [facet=method]; https://arxiv.org/html/2603.14688v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14688v1.html; sha256:5b0d4c61ca9718a903fa8d958c4cc0b563994ff8747111df88735094ad8649ad`。

**Evaluation contract 与未证明部分**：实验支持所测 workflow 和注入故障中的定位效果；未观测依赖仍会造成错误因果边。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.14688v1 HTML — §5.1 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.14688v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14688v1.html; sha256:5b0d4c61ca9718a903fa8d958c4cc0b563994ff8747111df88735094ad8649ad`。

**Trade-off / failure / coexistence**：图重建增加 trace 规范和存储成本；单进程短链故障仍可用结构化日志。

<!-- claim:SF-2026-ARXIV-2603-14688:start -->**Claim Boundary**：只支持 arXiv:2603.14688v1 §3.2 Causal Graph Construction 的机制与 §5.1 Evaluation Metrics 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-14688:end -->
<!-- review:SF-2026-ARXIV-2603-14688:end -->
### Universe Routing: Why Self-Evolving Agents Need Epistemic Control

<!-- review:SF-2026-ARXIV-2603-14799:start -->
**问题**：自演化 agent 若只按表面关键词选择知识域，会把‘知道什么’与‘下一步该验证什么’混在一起。

**旧路径为何合理**：按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。

**约束变化与机制**：该工作把 epistemic universe 作为显式路由状态，由分类器决定问题所属的推理制度，并把 hard/soft routing 与停止条件分开。

**State / data / control owner**：`AGENT-PLANNING` 负责 计划路由、证据需求与停止条件；定位证据为 `arXiv:2603.14799v1 HTML — §3.3 Model Architecture [facet=method]; https://arxiv.org/html/2603.14799v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14799v1.html; sha256:a4b39bdc13f3e61b6718c0ad020e93f8e16f209946dcb4b6b688a533e5413ba1`。

**Evaluation contract 与未证明部分**：验证比较 TF-IDF 与多种小型语言模型，并以刻意打破关键词相关性的 held-out 集合检查语义路由；它证明的是路由器在该分类任务上的鲁棒性，不是开放世界中的自知能力。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.14799v1 HTML — §4.1 Main Results: Semantic Understanding vs. Keyword Matching [facet=evaluation]; https://arxiv.org/html/2603.14799v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14799v1.html; sha256:a4b39bdc13f3e61b6718c0ad020e93f8e16f209946dcb4b6b688a533e5413ba1`。

**Trade-off / failure / coexistence**：新增错误面是 universe 标签漂移与错误路由后的级联；边界清楚、一步可解的任务仍无需维护额外 epistemic control plane。

<!-- claim:SF-2026-ARXIV-2603-14799:start -->**Claim Boundary**：只支持 arXiv:2603.14799v1 §3.3 Model Architecture 的机制与 §4.1 Main Results: Semantic Understanding vs. Keyword Matching 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-14799:end -->
<!-- review:SF-2026-ARXIV-2603-14799:end -->
### Beyond Benchmark Islands: Toward Representative Trustworthiness Evaluation for Agentic AI

<!-- review:SF-2026-ARXIV-2603-14987:start -->
**问题**：孤立 benchmark 的平均分无法代表 agent 在开放工具链、长任务和分布变化下的可信性。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文把评测重构为 distribution-aware Factory cycle：先定义目标部署分布，再生成/筛选场景、执行红队并把暴露出的 failure mode 反馈到下一轮。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.14987v1 HTML — §3.5. Layer 4: Distribution-Aware Representative Sampling [facet=method]; https://arxiv.org/html/2603.14987v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14987v1.html; sha256:9670088caf162e9e0eb9dc81e4dfa62665aebef43d170e30f11f4f61e20d038c`。

**Evaluation contract 与未证明部分**：公开实例只有单模型、合成数据和 24 个手工场景，因此证明的是评测流程可运行，而不是该流程已经覆盖真实生产分布。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.14987v1 HTML — §Re-evaluation (second red-team pass). [facet=evaluation]; https://arxiv.org/html/2603.14987v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.14987v1.html; sha256:9670088caf162e9e0eb9dc81e4dfa62665aebef43d170e30f11f4f61e20d038c`。

**Trade-off / failure / coexistence**：收益是把 coverage denominator 变成一等对象；代价是分布建模、场景生成与人工判定本身会引入选择偏差。

<!-- claim:SF-2026-ARXIV-2603-14987:start -->**Claim Boundary**：只支持 arXiv:2603.14987v1 §3.5. Layer 4: Distribution-Aware Representative Sampling 的机制与 §Re-evaluation (second red-team pass). 的公开 workload；§Limitations and future work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-14987:end -->
<!-- review:SF-2026-ARXIV-2603-14987:end -->
### Determinism-Preserving GPU Spatial Sharing with Vitamin-E

<!-- review:SF-2026-ARXIV-2603-15042:start -->
**问题**：GPU spatial sharing 若通过改变 kernel 并行形状追求利用率，浮点执行顺序变化会破坏 bitwise determinism。

**旧路径为何合理**：独占 GPU 提供最清晰的隔离和性能归因。

**约束变化与机制**：Vitamin-E 保持 logical launch 不变，只改变 block placement 与 wave count，在可证明的 parallel-structure equivalence 内调宽执行。

**State / data / control owner**：`PLATFORM-GPU-SCHEDULER` 负责 GPU slice、隔离、配额与抢占控制；定位证据为 `arXiv:2603.15042v1 HTML — §4 DetShare Design [facet=method]; https://arxiv.org/html/2603.15042v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15042v1.html; sha256:f64912d59362f573e46b763803cd861e4906e08d1efc8e44af8d13c5cf3fd56f`。

**Evaluation contract 与未证明部分**：作者 GPU 实验支持所测 kernel 的确定性与利用率；不代表任意同步/原子 kernel 都可安全伸缩。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15042v1 HTML — §6.1 End-to-End Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15042v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15042v1.html; sha256:f64912d59362f573e46b763803cd861e4906e08d1efc8e44af8d13c5cf3fd56f`。

**Trade-off / failure / coexistence**：可伸缩集合受依赖约束且 scheduler 更复杂；独占运行仍提供最简单确定性。

<!-- claim:SF-2026-ARXIV-2603-15042:start -->**Claim Boundary**：只支持 arXiv:2603.15042v1 §4 DetShare Design 的机制与 §6.1 End-to-End Performance Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15042:end -->
<!-- review:SF-2026-ARXIV-2603-15042:end -->
### From Storage to Steering: Memory Control Flow Attacks on LLM Agents

<!-- review:SF-2026-ARXIV-2603-15125:start -->
**问题**：持久 memory 不只是被动数据：一次被污染的检索结果可以改写后续 tool arguments 和控制流。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：作者以 agent state machine 与 trace space 形式化 memory-control-flow attack，把写入、检索、参数构造和工具调用串成可审计的攻击映射，并给出对应验证条件。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.15125v1 HTML — §3.3 Methodology: MemFlow [facet=method]; https://arxiv.org/html/2603.15125v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15125v1.html; sha256:5ec8efcc4c7c4951072da6535be8479ad59c4b21a511231eb45cd076a9791ecf`。

**Evaluation contract 与未证明部分**：实验只验证论文定义的攻击族与 agent/tool 配置；它没有证明所列检测条件对未知 memory backend 或长期演化策略完备。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15125v1 HTML — §4.2 Main Results: MCFA Vulnerability Landscape [facet=evaluation]; https://arxiv.org/html/2603.15125v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15125v1.html; sha256:5ec8efcc4c7c4951072da6535be8479ad59c4b21a511231eb45cd076a9791ecf`。

**Trade-off / failure / coexistence**：防护必须约束 memory lineage 与消费点，但更严格的校验会增加检索延迟并可能拒绝合法派生记忆；无持久状态时传统输入过滤仍较简单。

<!-- claim:SF-2026-ARXIV-2603-15125:start -->**Claim Boundary**：只支持 arXiv:2603.15125v1 §3.3 Methodology: MemFlow 的机制与 §4.2 Main Results: MCFA Vulnerability Landscape 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15125:end -->
<!-- review:SF-2026-ARXIV-2603-15125:end -->
### Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling

<!-- review:SF-2026-ARXIV-2603-15202:start -->
**问题**：LLM scheduler 的目标常被拆成互不兼容的 KV locality、等待时间和长度优先级，复杂策略难以在同一合同下比较。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：LMetric 把策略拆为可组合的 request metrics，并用乘法组合同时表达 KV reuse 与 aging，使优先级不是某个 engine 内部的隐式分支。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.15202v1 HTML — §The Analysis Framework [facet=method]; https://arxiv.org/html/2603.15202v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15202v1.html; sha256:23d1b76ab2c9191429e0dba3872e6c9a63f8bf2ae4a0ac9058a8edcb3b994e16`。

**Evaluation contract 与未证明部分**：论文提供统一分析框架与端到端比较；结论只覆盖其请求分布、模型与实现，未公开的并发/SLO 不能外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15202v1 HTML — §End-to-end Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15202v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15202v1.html; sha256:23d1b76ab2c9191429e0dba3872e6c9a63f8bf2ae4a0ac9058a8edcb3b994e16`。

**Trade-off / failure / coexistence**：乘法简单但对尺度归一化和极端值敏感；工作负载同质时 FIFO 或单指标策略仍具有更低控制开销。

<!-- claim:SF-2026-ARXIV-2603-15202:start -->**Claim Boundary**：只支持 arXiv:2603.15202v1 §The Analysis Framework 的机制与 §End-to-end Evaluation 的公开 workload；§Benign and Failure Cases Analysis of Multiplication-based Scheduling Score 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15202:end -->
<!-- review:SF-2026-ARXIV-2603-15202:end -->
### DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models

<!-- review:SF-2026-ARXIV-2603-15340:start -->
**问题**：masked diffusion 按 token uncertainty 独立解 mask，忽略 token 间依赖时会先提交结构上错误的位置。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：DOS 从模型分布估计依赖方向，优先解开能为其他位置提供信息的 token，且无需重新训练。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.15340v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.15340v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15340v1.html; sha256:60c2158ed442d703868688a5806ace0d4b2fbfb2f9aba5755d45c39e7e43828e`。

**Evaluation contract 与未证明部分**：指定 MDLM/任务实验支持速度质量变化；不证明估计依赖等于真实语法或语义因果。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15340v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.15340v1; papers/2026/03/_sources/daily-20260317/exact-v1-bodies/2603.15340v1.html; sha256:60c2158ed442d703868688a5806ace0d4b2fbfb2f9aba5755d45c39e7e43828e`。

**Trade-off / failure / coexistence**：依赖估计增加每步控制计算；关系弱或预算极紧时 uncertainty sampler 更简单。

<!-- claim:SF-2026-ARXIV-2603-15340:start -->**Claim Boundary**：只支持 arXiv:2603.15340v1 §5 Methodology 的机制与 §6 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15340:end -->
<!-- review:SF-2026-ARXIV-2603-15340:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-13281 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13281 |
| SF-2026-ARXIV-2603-13289 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13289 |
| SF-2026-ARXIV-2603-13319 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13319 |
| SF-2026-ARXIV-2603-13358 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13358 |
| SF-2026-ARXIV-2603-13364 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13364 |
| SF-2026-ARXIV-2603-13384 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13384 |
| SF-2026-ARXIV-2603-13424 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13424 |
| SF-2026-ARXIV-2603-13591 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13591 |
| SF-2026-ARXIV-2603-13594 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13594 |
| SF-2026-ARXIV-2603-13605 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13605 |
| SF-2026-ARXIV-2603-13606 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13606 |
| SF-2026-ARXIV-2603-13644 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13644 |
| SF-2026-ARXIV-2603-13791 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13791 |
| SF-2026-ARXIV-2603-13870 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13870 |
| SF-2026-ARXIV-2603-13875 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13875 |
| SF-2026-ARXIV-2603-13906 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13906 |
| SF-2026-ARXIV-2603-13940 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13940 |
| SF-2026-ARXIV-2603-13950 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13950 |
| SF-2026-ARXIV-2603-13966 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-13966 |
| SF-2026-ARXIV-2603-14688 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-14688 |
| SF-2026-ARXIV-2603-14799 | score_7_9 | selected | DA-20260317-25 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260317-25 |
| SF-2026-ARXIV-2603-14987 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-14987 |
| SF-2026-ARXIV-2603-15042 | score_7_9 | selected | DA-20260317-27 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260317-27 |
| SF-2026-ARXIV-2603-15125 | score_7_9 | selected | DA-20260317-28 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260317-28 |
| SF-2026-ARXIV-2603-15202 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15202 |
| SF-2026-ARXIV-2603-15340 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15340 |

<!-- analysis-decision:SF-2026-ARXIV-2603-13281:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13281:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13289:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13289:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13319:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13319:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13358:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13358:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13364:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13364:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13384:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13384:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13424:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13424:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13591:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13591:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13594:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13594:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13605:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13605:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13606:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13606:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13644:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13644:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13791:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13791:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13870:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13870:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13875:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13875:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13906:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13906:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13940:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13940:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13950:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13950:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-13966:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-13966:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-14688:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-14688:end -->
<!-- analysis:DA-20260317-25:start -->
### Universe Routing: Why Self-Evolving Agents Need Epistemic Control

自演化 agent 若只按表面关键词选择知识域，会把‘知道什么’与‘下一步该验证什么’混在一起。 旧路径在其原约束下仍合理：按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。 本 family 的设计变化是：该工作把 epistemic universe 作为显式路由状态，由分类器决定问题所属的推理制度，并把 hard/soft routing 与停止条件分开。 其公开验证边界为：验证比较 TF-IDF 与多种小型语言模型，并以刻意打破关键词相关性的 held-out 集合检查语义路由；它证明的是路由器在该分类任务上的鲁棒性，不是开放世界中的自知能力。 新增代价与回退条件为：新增错误面是 universe 标签漂移与错误路由后的级联；边界清楚、一步可解的任务仍无需维护额外 epistemic control plane。
<!-- analysis:DA-20260317-25:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-14987:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-14987:end -->
<!-- analysis:DA-20260317-27:start -->
### Determinism-Preserving GPU Spatial Sharing with Vitamin-E

GPU spatial sharing 若通过改变 kernel 并行形状追求利用率，浮点执行顺序变化会破坏 bitwise determinism。 旧路径在其原约束下仍合理：独占 GPU 提供最清晰的隔离和性能归因。 本 family 的设计变化是：Vitamin-E 保持 logical launch 不变，只改变 block placement 与 wave count，在可证明的 parallel-structure equivalence 内调宽执行。 其公开验证边界为：作者 GPU 实验支持所测 kernel 的确定性与利用率；不代表任意同步/原子 kernel 都可安全伸缩。 新增代价与回退条件为：可伸缩集合受依赖约束且 scheduler 更复杂；独占运行仍提供最简单确定性。
<!-- analysis:DA-20260317-27:end -->
<!-- analysis:DA-20260317-28:start -->
### From Storage to Steering: Memory Control Flow Attacks on LLM Agents

持久 memory 不只是被动数据：一次被污染的检索结果可以改写后续 tool arguments 和控制流。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：作者以 agent state machine 与 trace space 形式化 memory-control-flow attack，把写入、检索、参数构造和工具调用串成可审计的攻击映射，并给出对应验证条件。 其公开验证边界为：实验只验证论文定义的攻击族与 agent/tool 配置；它没有证明所列检测条件对未知 memory backend 或长期演化策略完备。 新增代价与回退条件为：防护必须约束 memory lineage 与消费点，但更严格的校验会增加检索延迟并可能拒绝合法派生记忆；无持久状态时传统输入过滤仍较简单。
<!-- analysis:DA-20260317-28:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-15202:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15202:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-15340:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15340:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-13281 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#variable-rate-compression-把-rank-allocation-变成-request-state (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13281 | delta:SF-2026-ARXIV-2603-13281 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13281 |
| SF-2026-ARXIV-2603-13289 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#小结 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13289 | delta:SF-2026-ARXIV-2603-13289 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13289 |
| SF-2026-ARXIV-2603-13319 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13319 | delta:SF-2026-ARXIV-2603-13319 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13319 |
| SF-2026-ARXIV-2603-13335 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#research-outlook (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13335 | delta:SF-2026-ARXIV-2603-13335 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13335 |
| SF-2026-ARXIV-2603-13358 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#disaggregation-也重新定义-failure-domain (section Ch-owner) | books/part-05-inference-system/54-gpu-memory.md#第54章-gpu-memory (section Ch-adjacent); books/part-05-inference-system/56-inference-scheduling.md#第56章-推理调度 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13358 | delta:SF-2026-ARXIV-2603-13358 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13358 |
| SF-2026-ARXIV-2603-13364 | MODEL-MOE | books/part-02-model/21-moe.md#本章要回答的问题 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13364 | delta:SF-2026-ARXIV-2603-13364 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13364 |
| SF-2026-ARXIV-2603-13384 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13384 | delta:SF-2026-ARXIV-2603-13384 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13384 |
| SF-2026-ARXIV-2603-13404 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#tool-contract (section Ch-owner) | books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent); books/part-07-agent/79-planning.md#第79章-planning (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13404 | delta:SF-2026-ARXIV-2603-13404 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13404 |
| SF-2026-ARXIV-2603-13420 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#agent-自己的-instruction、config-与-memory-也是受保护资产 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13420 | delta:SF-2026-ARXIV-2603-13420 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13420 |
| SF-2026-ARXIV-2603-13424 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多跳-delegation-必须保留-human-principal (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13424 | delta:SF-2026-ARXIV-2603-13424 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13424 |
| SF-2026-ARXIV-2603-13591 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#exclusive-batching-的-phase-switch-是-workload-dependent-state (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13591 | delta:SF-2026-ARXIV-2603-13591 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13591 |
| SF-2026-ARXIV-2603-13594 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从-pass@k-到-pass^k：能力覆盖与重复可靠性不是同一问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13594 | delta:SF-2026-ARXIV-2603-13594 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13594 |
| SF-2026-ARXIV-2603-13605 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13605 | delta:SF-2026-ARXIV-2603-13605 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13605 |
| SF-2026-ARXIV-2603-13606 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#从-collective-call-到-kernel-内-remote-memory (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13606 | delta:SF-2026-ARXIV-2603-13606 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13606 |
| SF-2026-ARXIV-2603-13644 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13644 | delta:SF-2026-ARXIV-2603-13644 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13644 |
| SF-2026-ARXIV-2603-13791 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13791 | delta:SF-2026-ARXIV-2603-13791 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13791 |
| SF-2026-ARXIV-2603-13870 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量：评估声明必须绑定完整对象 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13870 | delta:SF-2026-ARXIV-2603-13870 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13870 |
| SF-2026-ARXIV-2603-13875 | AGENT-MEMORY | books/part-07-agent/77-memory.md#context-与-memory-的状态边界 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13875 | delta:SF-2026-ARXIV-2603-13875 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13875 |
| SF-2026-ARXIV-2603-13906 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13906 | delta:SF-2026-ARXIV-2603-13906 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13906 |
| SF-2026-ARXIV-2603-13925 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#从-unsafe-trajectory-到可训练分支，必须保留同一状态锚点 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13925 | delta:SF-2026-ARXIV-2603-13925 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13925 |
| SF-2026-ARXIV-2603-13940 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#memory-origin-confusion：reasoning-claim-低于-effect-receipt (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13940 | delta:SF-2026-ARXIV-2603-13940 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13940 |
| SF-2026-ARXIV-2603-13950 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#模型输出只是-proposal (section Ch-owner) | books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent); books/part-07-agent/79-planning.md#第79章-planning (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13950 | delta:SF-2026-ARXIV-2603-13950 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13950 |
| SF-2026-ARXIV-2603-13966 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量：评估声明必须绑定完整对象 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13966 | delta:SF-2026-ARXIV-2603-13966 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13966 |
| SF-2026-ARXIV-2603-14688 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#从单一-monitor-score-到多维、分权的运行证据 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-14688 | delta:SF-2026-ARXIV-2603-14688 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14688 |
| SF-2026-ARXIV-2603-14799 | AGENT-PLANNING | books/part-07-agent/79-planning.md#search-based-planning-的边界 (section Ch-owner) | books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent); books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-14799 | delta:SF-2026-ARXIV-2603-14799 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14799 |
| SF-2026-ARXIV-2603-14987 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-14987 | delta:SF-2026-ARXIV-2603-14987 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-14987 |
| SF-2026-ARXIV-2603-15042 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#gpu-sharing-的语义不同 (section Ch-owner) | books/part-06-ai-infrastructure/62-gateway.md#第62章-gateway (section Ch-adjacent); books/part-06-ai-infrastructure/64-volcano.md#第64章-gang-与队列调度：以-volcano-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15042 | delta:SF-2026-ARXIV-2603-15042 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15042 |
| SF-2026-ARXIV-2603-15125 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#已披露漏洞要沿-design-lineage-搜索变体 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15125 | delta:SF-2026-ARXIV-2603-15125 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15125 |
| SF-2026-ARXIV-2603-15202 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15202 | delta:SF-2026-ARXIV-2603-15202 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15202 |
| SF-2026-ARXIV-2603-15340 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#diffusion：用迭代修正换并行状态更新 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15340 | delta:SF-2026-ARXIV-2603-15340 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15340 |

<!-- books-review:SF-2026-ARXIV-2603-13281:start -->
### ICaRus: Identical Cache Reuse for Efficient Multi Model Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13281:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：一个 training-free 分支先离线建立 model-side PCA basis，再在每个 request prefill 中估计各层 reconstruction curve，用 water-filling 在总 KV budget 下分配 variable rank。它不删除 token，而是改变每个 region 保留的 feature subspace；basis revision、request statistic、rank map、packed offsets、codec precision 与 reuse scope 都必须进入 cache identity。Prefix reuse 只有在 basis、model、RoPE 与 rank policy 兼容时才能共享，Decode kernel 若不能直接消费 variable layout，projection/gather 成本会返还 memory 节省。<!-- existing:SF-2026-ARXIV-2603-13281:end -->

<!-- delta:SF-2026-ARXIV-2603-13281:start -->新证据差异：ICaRus 只共享一个冻结 logical encoder 产生的模型无关中间表示，再由各目标模型映射为本模型 KV；复用身份从‘同模型 prefix’上移到‘相同逻辑输入’。<!-- delta:SF-2026-ARXIV-2603-13281:end -->

边界：只支持 arXiv:2603.13281v1 §A.2.2 Multi Model Architecture with LoRA Adapters 的机制与 §4.2 Accuracy Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13281:end -->
<!-- books-review:SF-2026-ARXIV-2603-13289:start -->
### RelayCaching: Accelerating LLM Collaboration via Decoding KV Cache Reuse — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13289:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。<!-- existing:SF-2026-ARXIV-2603-13289:end -->

<!-- delta:SF-2026-ARXIV-2603-13289:start -->新证据差异：RelayCaching 把上游 decode 过程中已有的 KV 作为转换输入，只对语义敏感位置选择性重算，改变了跨模型 handoff 的状态所有权。<!-- delta:SF-2026-ARXIV-2603-13289:end -->

边界：只支持 arXiv:2603.13289v1 §4.1 Overall Architecture 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13289:end -->
<!-- books-review:SF-2026-ARXIV-2603-13319:start -->
### LightningRL: Breaking the Accuracy-Parallelism Trade-off of Block-wise dLLMs via Reinforcement Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13319:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-13319:end -->

<!-- delta:SF-2026-ARXIV-2603-13319:start -->新证据差异：LightningRL 用奖励把并行 token 数与生成正确性共同纳入策略，使 block-level proposal 的提交宽度成为可训练控制量。<!-- delta:SF-2026-ARXIV-2603-13319:end -->

边界：只支持 arXiv:2603.13319v1 §3 LightningRL: Breaking the Accuracy–Parallelism Trade-off 的机制与 §4.2 Main Results 的公开 workload；§Appendix A Discussion on Value Model Incorporation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13319:end -->
<!-- books-review:SF-2026-ARXIV-2603-13335:start -->
### Information-Theoretic Constraints for Continual Vision-Language-Action Alignment — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13335:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：下一阶段不是只扩大 VLA 参数，而是形成可验证闭环：跨 embodiment typed action、real-time adaptive chunking、uncertainty-aware controller、physical failure injection、sim/real evidence alignment 和人类接管后的状态恢复。<!-- existing:SF-2026-ARXIV-2603-13335:end -->

<!-- delta:SF-2026-ARXIV-2603-13335:start -->新证据差异：Info-VLA 把跨模态 mutual-information 结构作为保留对象，用约束项保护旧技能的对齐关系。<!-- delta:SF-2026-ARXIV-2603-13335:end -->

边界：只支持 arXiv:2603.13335v1 §4 Methodology 的机制与 §5.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13335:end -->
<!-- books-review:SF-2026-ARXIV-2603-13358:start -->
### Not All Prefills Are Equal: PPD Disaggregation for Multi-turn LLM Serving — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13358:start -->已读 owner `books/part-05-inference-system/55-pd-disaggregation.md` 与相邻章节。现有命题：2026 年两项 preprint 提供了互补但仍受限的证据：AFlex 在披露的 A800、模型、trace 与 SLO 条件下实现 A/F pool 和独立 power control；HeteroPanacea 用 component-level simulator 搜索 P/D/A/F、quantization、parallelism 与异构 NPU allocation。前者是有限平台实现，后者不是 cycle-accurate 或端到端 serving validation，代码也尚未公开。两者支持上述 `Principle Reuse`， 不能证明四池拓扑是跨硬件、跨模型的默认答案，也不能用作者峰值数字替代真实集群测量。<!-- existing:SF-2026-ARXIV-2603-13358:end -->

<!-- delta:SF-2026-ARXIV-2603-13358:start -->新证据差异：PPD 将初始 prefill 与增量 prefill 分开，并依据会话阶段在 AP/P/D pool 间动态路由，减少重复传输和资源干扰。<!-- delta:SF-2026-ARXIV-2603-13358:end -->

边界：只支持 arXiv:2603.13358v1 §5 PPD: Dynamic AP Routing System 的机制与 §6 Real-world Validation 的公开 workload；§C.4 Failure Rate Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13358:end -->
<!-- books-review:SF-2026-ARXIV-2603-13364:start -->
### FineRMoE: Dimension Expansion for Finer-Grained Expert with Its Upcycling Approach — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13364:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：本章使用 `B` 表示 batch size，`T` 表示 sequence length，`d_model` 表示 hidden dimension，`E` 表示 expert 数，`k` 表示每个 token 选择的 expert 数。<!-- existing:SF-2026-ARXIV-2603-13364:end -->

<!-- delta:SF-2026-ARXIV-2603-13364:start -->新证据差异：FineRMoE 同时沿 intermediate 与 output 维扩展专家，并用二级稀疏路由控制两层激活，改变 expert granularity 与通信组合。<!-- delta:SF-2026-ARXIV-2603-13364:end -->

边界：只支持 arXiv:2603.13364v1 §3.1 FineRMoE Architecture 的机制与 §4 Experiments 的公开 workload；§4.5 Ablation Study on Fine-Grained Configurations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13364:end -->
<!-- books-review:SF-2026-ARXIV-2603-13384:start -->
### VulnAgent-R2: Evidence-Calibrated Multi-Agent Auditing for Repository-Level Vulnerability Detection — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13384:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-13384:end -->

<!-- delta:SF-2026-ARXIV-2603-13384:start -->新证据差异：VulnAgent-R2 把反事实证据重加权、build-aware 验证计划和成本风险调度组成多 agent 审计控制面。<!-- delta:SF-2026-ARXIV-2603-13384:end -->

边界：只支持 arXiv:2603.13384v1 §4.4 Implementation protocol 的机制与 §4.5 Evaluation metrics 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13384:end -->
<!-- books-review:SF-2026-ARXIV-2603-13404:start -->
### Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13404:start -->已读 owner `books/part-07-agent/78-tool-calling.md` 与相邻章节。现有命题：Description 帮助模型选择工具，Schema 帮助构造参数；二者都不能替代服务端业务校验。Tool name 或描述可能来自第三方 server，应视为不可信 metadata，不能据此自动提升权限。<!-- existing:SF-2026-ARXIV-2603-13404:end -->

<!-- delta:SF-2026-ARXIV-2603-13404:start -->新证据差异：该受控实验固定工具能力，只改变 free-form、JSON Schema 与结构化诊断，隔离 schema contract 对 action formation 的影响。<!-- delta:SF-2026-ARXIV-2603-13404:end -->

边界：只支持 arXiv:2603.13404v1 §5 Methodology 的机制与 §6 Experiments 的公开 workload；§Failure taxonomy. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13404:end -->
<!-- books-review:SF-2026-ARXIV-2603-13420:start -->
### Accelerating Suffix Jailbreak attacks with Prefix-Shared KV-cache — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13420:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：OS telemetry 只能看到操作与时序，不拥有 Agent intent；semantic detector 也可能把正常自修改误报为攻击。 某些 mutation 在系统调用层与正常行为不可区分，必须依赖更高层 workflow invariant、human approval 或恢复点。 静态 ACL 仍适合 instruction/config 等低变更层，动态检测只用于确实需要写入的层。Self-State Attacks 的论文 提供 threat matrix 与受控 traces，不证明其 detector 覆盖生产 workload，也不允许 Memory backup 绕过删除政策。<!-- existing:SF-2026-ARXIV-2603-13420:end -->

<!-- delta:SF-2026-ARXIV-2603-13420:start -->新证据差异：PSKV 将共享前缀的 KV 设为只读基态，在候选 suffix 间复用，仅让差异部分进入搜索循环。<!-- delta:SF-2026-ARXIV-2603-13420:end -->

边界：只支持 arXiv:2603.13420v1 §4 Methodology 的机制与 §5.2 Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13420:end -->
<!-- books-review:SF-2026-ARXIV-2603-13424:start -->
### Agent Privilege Separation in OpenClaw: A Structural Defense Against Prompt Injection — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13424:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这把 authorization 从 prompt/Agent 自述迁移到可核验 provenance chain，但不证明行为正确，也不替代 prompt-injection defense、sandbox 或最小权限。Key/token 生命周期、撤销、重放和 scope composition 都是新增压力；链不完整、过期或验证失败时必须 fail closed，并回退人工授权。<!-- existing:SF-2026-ARXIV-2603-13424:end -->

<!-- delta:SF-2026-ARXIV-2603-13424:start -->新证据差异：防御把读取/解析与行动拆为两个权限域，并以结构化 JSON 作为唯一跨域消息，缩小污染上下文可控制的能力集合。<!-- delta:SF-2026-ARXIV-2603-13424:end -->

边界：只支持 arXiv:2603.13424v1 §3 Defense Design 的机制与 §4.1 Overall Ablation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13424:end -->
<!-- books-review:SF-2026-ARXIV-2603-13591:start -->
### d-HNSW: A High-performance Vector Search Engine on Disaggregated Memory — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13591:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：Mixed batching 在 Prefill 与 Decode 可以高效共批、硬件带宽充足时减少空隙，是现代 serving 的合理默认；若 engine 只能 exclusive batching，或 Prefill–Decode interference 抬高 mixed step 的边际成本，固定“优先 Decode”或“空出一个 slot 就 Prefill”都会忽略 phase switching 的真实代价。此时调度对象不仅是等待请求，还包括当前 busy/idle slots、保留的 KV、输入长度分布、输出 completion hazard、GPU bandwidth、model size 与 memory headroom。<!-- existing:SF-2026-ARXIV-2603-13591:end -->

<!-- delta:SF-2026-ARXIV-2603-13591:start -->新证据差异：d-HNSW 重排图索引与访问批次，使 compute node 以 RDMA 预取/聚合远端邻接状态，而不是逐边同步读取。<!-- delta:SF-2026-ARXIV-2603-13591:end -->

边界：只支持 arXiv:2603.13591v1 §5.1. Methodology 的机制与 §5. Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13591:end -->
<!-- books-review:SF-2026-ARXIV-2603-13594:start -->
### EnterpriseOps-Gym: Environments and Evaluations for Stateful Agentic Planning and Tool Use in Enterprise Settings — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13594:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：降低 temperature 只减少 sampling 随机性，不会消除 environment、instruction、tool 或 evaluator 引起的失败。 固定 plan 可降低行为方差，也可能固化错误；clarification 可减少歧义，也可能泄漏 benchmark oracle。Computer Use Agent 的重复运行研究只在其 OSWorld、三次重复和指定模型合同下支持该诊断，不证明 `k=3` 满足生产 SLO。 高副作用任务还必须定义 reset、retry budget 与 compensation；成本受限的离线回归仍可保留 single-run metric。<!-- existing:SF-2026-ARXIV-2603-13594:end -->

<!-- delta:SF-2026-ARXIV-2603-13594:start -->新证据差异：EnterpriseOps-Gym 用容器化数据库、512 个工具和跨步状态转移定义可重放的规划环境。<!-- delta:SF-2026-ARXIV-2603-13594:end -->

边界：只支持 arXiv:2603.13594v1 §3 EnterpriseOps-Gym 的机制与 §4.2 Evaluation Metrics 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13594:end -->
<!-- books-review:SF-2026-ARXIV-2603-13605:start -->
### Orla: A Library for Serving LLM-Based Multi-Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13605:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。 生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入 真实 serving 的补全责任，而不是论文已经证明的反馈算法。<!-- existing:SF-2026-ARXIV-2603-13605:end -->

<!-- delta:SF-2026-ARXIV-2603-13605:start -->新证据差异：Orla 把 workflow policy 与 request execution 解耦，在 engine 之上统一表达依赖、并发和后端选择。<!-- delta:SF-2026-ARXIV-2603-13605:end -->

边界：只支持 arXiv:2603.13605v1 §2.1. Core Abstractions 的机制与 §4. Evaluation 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13605:end -->
<!-- books-review:SF-2026-ARXIV-2603-13606:start -->
### NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13606:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：这是 `Layering / Dependency`，不是 NCCL、UCC 或 ProcessGroup 的后继替代。常规梯度同步、稳定 跨厂商接口、清晰故障边界优先时，collective call 仍然更合理；只有通信与计算必须深度融合，且 目标 hardware/transport 支持相应 memory model 时，kernel-specialized path 才值得承担调试和 portability 成本。PyTorch 2.9 的 Symmetric Memory 是这一分支的版本化证据，不代表该 API、 性能或 failure semantics 已成为跨 runtime 稳定标准。<!-- existing:SF-2026-ARXIV-2603-13606:end -->

<!-- delta:SF-2026-ARXIV-2603-13606:start -->新证据差异：NCCL EP 在 NCCL Device API 上提供统一 dispatch/combine，并把 low-latency 与 high-throughput 路径纳入同一通信接口。<!-- delta:SF-2026-ARXIV-2603-13606:end -->

边界：只支持 arXiv:2603.13606v1 §V-A Kernel Architecture 的机制与 §VII Performance Evaluation 的公开 workload；§IX Conclusions and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13606:end -->
<!-- books-review:SF-2026-ARXIV-2603-13644:start -->
### StatePlane: A Cognitive State Plane for Long-Horizon AI Systems Under Bounded Context — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13644:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章按四层逐步扩大 Memory 的责任：先界定 Context 与 persisted state，再建立 typed write 与 authorized read，然后讨论从原始 evidence 到可撤销 derived memory 的 consolidation，最后处理并发、安全、评估与修复。 这条路线的核心不是“记得更多”，而是让每次派生、采用、纠错和遗忘都有明确 owner。<!-- existing:SF-2026-ARXIV-2603-13644:end -->

<!-- delta:SF-2026-ARXIV-2603-13644:start -->新证据差异：StatePlane 把 belief、goal、decision 和 evidence 变成独立于 context window 的 versioned state，由 policy 决定写入、压缩和回注。<!-- delta:SF-2026-ARXIV-2603-13644:end -->

边界：只支持 arXiv:2603.13644v1 §V StatePlane Architecture 的机制与 §XII-A Benchmark Suite 的公开 workload；§XV Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13644:end -->
<!-- books-review:SF-2026-ARXIV-2603-13791:start -->
### DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13791:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-13791:end -->

<!-- delta:SF-2026-ARXIV-2603-13791:start -->新证据差异：DeceptGuard 在同一任务上对比 black-box、CoT-aware 与 activation-probe 三种监控信号，显式测量可见性与干预面。<!-- delta:SF-2026-ARXIV-2603-13791:end -->

边界：只支持 arXiv:2603.13791v1 §5.2 Generation Architecture 的机制与 §7 DeceptArena: Evaluation Benchmark 的公开 workload；§9.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13791:end -->
<!-- books-review:SF-2026-ARXIV-2603-13870:start -->
### When to Screen, When to Bypass: LLM-Judges in Resource-Scarce AI-Human Workflow — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13870:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：例如，模型离线比较可以固定 prompt 和 decoding；RAG 评估必须把 index 与 retriever 放进对象身份；Agent 评估还需要记录 tools、sandbox、workflow、budget 和 environment。若只记录 `model_name`，同一模型搭配不同系统组件产生的行为会被错误合并。<!-- existing:SF-2026-ARXIV-2603-13870:end -->

<!-- delta:SF-2026-ARXIV-2603-13870:start -->新证据差异：论文把 judge 与 human reviewer 建模为串联/旁路队列，用准确率和服务率求何时 screening 优于直接人工。<!-- delta:SF-2026-ARXIV-2603-13870:end -->

边界：只支持 arXiv:2603.13870v1 §Implementation and extensions. 的机制与 §LLM judges for screening and evaluation. 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13870:end -->
<!-- books-review:SF-2026-ARXIV-2603-13875:start -->
### GradMem: Learning to Write Context into Memory with Test-Time Gradient Descent — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13875:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：模型架构中的 test-time neural memory 也不属于本章的 Agent Memory。前者在 forward 期间按 surprise/gradient 更新模型内部参数化 state，owner 是 sequence model，主要目标是压缩和利用 长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。 二者共享“write、retain、forget”的 `Principle Reuse`，但 truth authority 与生命周期不同。 第 22 章讨论 Titans/MIRAS 这类模型内部路线，本章只处理外部 durable state。<!-- existing:SF-2026-ARXIV-2603-13875:end -->

<!-- delta:SF-2026-ARXIV-2603-13875:start -->新证据差异：GradMem 通过少量 test-time gradient steps 把一次性上下文写入紧凑参数状态，查询时不再读取原文。<!-- delta:SF-2026-ARXIV-2603-13875:end -->

边界：只支持 arXiv:2603.13875v1 §2.2 GradMem: Test-Time Gradient Descent Memory 的机制与 §3.3 Results on KV-retrieval task 的公开 workload；§4 Discussion and Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13875:end -->
<!-- books-review:SF-2026-ARXIV-2603-13906:start -->
### ATCC: Adaptive Concurrency Control for Unforeseen Agentic Transactions — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13906:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-13906:end -->

<!-- delta:SF-2026-ARXIV-2603-13906:start -->新证据差异：ATCC 在线观察冲突与阶段进度，在乐观/悲观控制间自适应切换，把 agent plan evolution 纳入数据库并发控制。<!-- delta:SF-2026-ARXIV-2603-13906:end -->

边界：只支持 arXiv:2603.13906v1 §4.3. Cost-Aware Reward Design 的机制与 §6. Evaluation 的公开 workload；§5.6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13906:end -->
<!-- books-review:SF-2026-ARXIV-2603-13925:start -->
### SmoothVLA: Aligning Vision-Language-Action Models with Physical Constraints via Intrinsic Smoothness Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13925:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：这种路径把在线 critic cost 移到训练期，却要求可恢复 simulator、anchor identity、matched branch budget 和可靠 verifier。真实世界副作用通常不能 rollback，sim-to-real 也会改变 contact 与 delay；因此它不能替代 physical safety controller、人类接管和真实 incident evidence。没有可信 snapshot 或 reset 成本过高时，离线 expert demonstration、规则 shield 与拒绝执行仍是更稳的旧分支。<!-- existing:SF-2026-ARXIV-2603-13925:end -->

<!-- delta:SF-2026-ARXIV-2603-13925:start -->新证据差异：SmoothVLA 把 task reward 与速度/加速度平滑项联合优化，使物理可执行性进入 policy objective。<!-- delta:SF-2026-ARXIV-2603-13925:end -->

边界：只支持 arXiv:2603.13925v1 §4.1.1 Implementation Details 的机制与 §4.2.3 Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13925:end -->
<!-- books-review:SF-2026-ARXIV-2603-13940:start -->
### GroupGuard: A Framework for Modeling and Defending Collusive Attacks in Multi-Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13940:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：现有作者实验支持具体 memory-origin confusion 与同源放大 failure mode，不覆盖 system prompt/weights compromise、 multi-Agent 长链传播或真实生产 EHR 风险；没有公开 artifact 也限制独立复现。因此正文只吸收 `reasoning claim < authoritative effect receipt` 与 lineage collapse 的安全合同。<!-- existing:SF-2026-ARXIV-2603-13940:end -->

<!-- delta:SF-2026-ARXIV-2603-13940:start -->新证据差异：GroupGuard 维护交互图，结合持续监测、honeypot 诱导和结构剪枝识别并隔离可疑 coalition。<!-- delta:SF-2026-ARXIV-2603-13940:end -->

边界：只支持 arXiv:2603.13940v1 §3 Methodology 的机制与 §Appendix A Detailed Experimental Results across Topologies 的公开 workload；§Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13940:end -->
<!-- books-review:SF-2026-ARXIV-2603-13950:start -->
### ToolFlood: Beyond Selection -- Hiding Valid Tools from LLM Agents via Semantic Covering — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13950:start -->已读 owner `books/part-07-agent/78-tool-calling.md` 与相邻章节。现有命题：Schema 可以拒绝缺字段、错误类型或非法 enum；semantic validation 还要检查金额、目标资源、环境、时间窗口和当前状态。Authorization 必须使用真实 principal，不接受模型生成的 `tenant_id` 或 scope。<!-- existing:SF-2026-ARXIV-2603-13950:end -->

<!-- delta:SF-2026-ARXIV-2603-13950:start -->新证据差异：ToolFlood 在 embedding 空间布置少量恶意 metadata 形成 semantic covering，攻击的是 retrieval admission 而非后续 planner。<!-- delta:SF-2026-ARXIV-2603-13950:end -->

边界：只支持 arXiv:2603.13950v1 §2.1 Agent Design Patterns and Tool Ecosystems 的机制与 §5.4 Main results 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13950:end -->
<!-- books-review:SF-2026-ARXIV-2603-13966:start -->
### vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13966:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或 architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision 纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一 对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。<!-- existing:SF-2026-ARXIV-2603-13966:end -->

<!-- delta:SF-2026-ARXIV-2603-13966:start -->新证据差异：vla-eval 用 WebSocket/msgpack 隔离模型推理与 Docker benchmark runtime，把环境版本和消息协议变成显式 contract。<!-- delta:SF-2026-ARXIV-2603-13966:end -->

边界：只支持 arXiv:2603.13966v1 §II-A Architecture 的机制与 §II-C Parallel Evaluation 的公开 workload；§V Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13966:end -->
<!-- books-review:SF-2026-ARXIV-2603-14688:start -->
### AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-14688:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：Graph owner 只拥有诊断 view，不得改写原 trace；candidate root cause 也不能直接授权自动 patch。Dependency prior 错误会漏掉真实边或制造伪因果，并行 branch 的时间相关不等于控制依赖，black-box tool 还可能没有足够结构。 因此输出必须保留被排除/保留 span、规则/模型版本、置信与复现实验。Full-trace manual review 在高风险事故、 依赖图不完整或低频新故障中仍是正确旧方案；结构化 slicing 适合重复 pipeline 和可见度足够的系统。STRACE 提供了 structure-guided attribution 的实验性证据，不证明 observational trace 本身已经识别真实因果。<!-- existing:SF-2026-ARXIV-2603-14688:end -->

<!-- delta:SF-2026-ARXIV-2603-14688:start -->新证据差异：AgentTrace 从执行日志重建因果图，从最终错误反向遍历并按传播关系排序候选根因。<!-- delta:SF-2026-ARXIV-2603-14688:end -->

边界：只支持 arXiv:2603.14688v1 §3.2 Causal Graph Construction 的机制与 §5.1 Evaluation Metrics 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-14688:end -->
<!-- books-review:SF-2026-ARXIV-2603-14799:start -->
### Universe Routing: Why Self-Evolving Agents Need Epistemic Control — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-14799:start -->已读 owner `books/part-07-agent/79-planning.md` 与相邻章节。现有命题：在部分可观测环境中，固定 branching factor 也会浪费预算：某些节点只有一个可信方向，另一些节点存在 高 epistemic uncertainty。Planner 可以把“请求展开”显式化，并给整棵搜索树共享 leaf budget：<!-- existing:SF-2026-ARXIV-2603-14799:end -->

<!-- delta:SF-2026-ARXIV-2603-14799:start -->新证据差异：该工作把 epistemic universe 作为显式路由状态，由分类器决定问题所属的推理制度，并把 hard/soft routing 与停止条件分开。<!-- delta:SF-2026-ARXIV-2603-14799:end -->

边界：只支持 arXiv:2603.14799v1 §3.3 Model Architecture 的机制与 §4.1 Main Results: Semantic Understanding vs. Keyword Matching 的公开 workload；§5 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-14799:end -->
<!-- books-review:SF-2026-ARXIV-2603-14987:start -->
### Beyond Benchmark Islands: Toward Representative Trustworthiness Evaluation for Agentic AI — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-14987:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-14987:end -->

<!-- delta:SF-2026-ARXIV-2603-14987:start -->新证据差异：论文把评测重构为 distribution-aware Factory cycle：先定义目标部署分布，再生成/筛选场景、执行红队并把暴露出的 failure mode 反馈到下一轮。<!-- delta:SF-2026-ARXIV-2603-14987:end -->

边界：只支持 arXiv:2603.14987v1 §3.5. Layer 4: Distribution-Aware Representative Sampling 的机制与 §Re-evaluation (second red-team pass). 的公开 workload；§Limitations and future work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-14987:end -->
<!-- books-review:SF-2026-ARXIV-2603-15042:start -->
### Determinism-Preserving GPU Spatial Sharing with Vitamin-E — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15042:start -->已读 owner `books/part-06-ai-infrastructure/63-gpu-scheduler.md` 与相邻章节。现有命题：因此 production sharing 需要显式 fault-domain contract：硬件/驱动拥有地址隔离，node runtime 负责检测 fatal fault、冻结受影响 allocation、重建 MPS client 与 context，scheduler 再依据恢复结果决定 rebind 或迁移。它以 recovery controller、重建延迟和更复杂的健康状态换取更细故障域；若驱动无法证明 client-level containment，或 workload 无 checkpoint / replay，MIG、独占 GPU 或整节点失败回退仍更可靠。单一软件栈的 fault-injection 结果不能外推为所有 GPU、driver 与 kernel 组合的隔离保证。<!-- existing:SF-2026-ARXIV-2603-15042:end -->

<!-- delta:SF-2026-ARXIV-2603-15042:start -->新证据差异：Vitamin-E 保持 logical launch 不变，只改变 block placement 与 wave count，在可证明的 parallel-structure equivalence 内调宽执行。<!-- delta:SF-2026-ARXIV-2603-15042:end -->

边界：只支持 arXiv:2603.15042v1 §4 DetShare Design 的机制与 §6.1 End-to-End Performance Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15042:end -->
<!-- books-review:SF-2026-ARXIV-2603-15125:start -->
### From Storage to Steering: Memory Control Flow Attacks on LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15125:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：按 repository 或 CVE 精确字符串修复，在实现独立、复用少时成本最低；AI infrastructure 常复制相似 loader、conversion、serving 与 agent workflow，同一设计缺陷可能以不同 API、文件名和数据流重新出现。安全 owner 因而要保存 vulnerability 的 reference behavior、关键 data/control flow 与 affected preconditions，再在相关 repository lineage 中做 variant search；scanner 只产生候选，代码 owner 与可执行 test 才能确认修复。<!-- existing:SF-2026-ARXIV-2603-15125:end -->

<!-- delta:SF-2026-ARXIV-2603-15125:start -->新证据差异：作者以 agent state machine 与 trace space 形式化 memory-control-flow attack，把写入、检索、参数构造和工具调用串成可审计的攻击映射，并给出对应验证条件。<!-- delta:SF-2026-ARXIV-2603-15125:end -->

边界：只支持 arXiv:2603.15125v1 §3.3 Methodology: MemFlow 的机制与 §4.2 Main Results: MCFA Vulnerability Landscape 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15125:end -->
<!-- books-review:SF-2026-ARXIV-2603-15202:start -->
### Simple is Better: Multiplication May Be All You Need for LLM Request Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15202:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-15202:end -->

<!-- delta:SF-2026-ARXIV-2603-15202:start -->新证据差异：LMetric 把策略拆为可组合的 request metrics，并用乘法组合同时表达 KV reuse 与 aging，使优先级不是某个 engine 内部的隐式分支。<!-- delta:SF-2026-ARXIV-2603-15202:end -->

边界：只支持 arXiv:2603.15202v1 §The Analysis Framework 的机制与 §End-to-end Evaluation 的公开 workload；§Benign and Failure Cases Analysis of Multiplication-based Scheduling Score 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15202:end -->
<!-- books-review:SF-2026-ARXIV-2603-15340:start -->
### DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15340:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。<!-- existing:SF-2026-ARXIV-2603-15340:end -->

<!-- delta:SF-2026-ARXIV-2603-15340:start -->新证据差异：DOS 从模型分布估计依赖方向，优先解开能为其他位置提供信息的 token，且无需重新训练。<!-- delta:SF-2026-ARXIV-2603-15340:end -->

边界：只支持 arXiv:2603.15340v1 §5 Methodology 的机制与 §6 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15340:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260317-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260317 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260317-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260317-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260317-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260317/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

当前 retained Review 可复用，但 denominator 的 full-row fresh-context 反证发现 false-negative；按 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 重做全量语义复核后，再重算 Selection 与 Books disposition。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- Books Decision 已闭合，本日无需修改 Books。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 未解决语义 finding=4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）；blocked / unverified / disputed 仍为 0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
