# Daily Research — 2026-03-20

**Research Date:** 2026-03-20

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-19 09:00:00 ～ 2026-03-20 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=644/644/644；denominator=19、pre-denominator closures=625。exact-v1 Review complete=19、blocked=0；Integrate 建议=0。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-20 |
| Window End | 2026-03-20 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260320-AUTHOR-19 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-19T09:00:00+08:00 | 2026-03-20T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 644/644 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 644 | SF-2026-ARXIV-2603-18016;SF-2026-ARXIV-2603-18034;SF-2026-ARXIV-2603-18043;SF-2026-ARXIV-2603-18046;SF-2026-ARXIV-2603-18063;SF-2026-ARXIV-2603-18096;SF-2026-ARXIV-2603-18245;SF-2026-ARXIV-2603-18280;SF-2026-ARXIV-2603-18330;SF-2026-ARXIV-2603-18433;SF-2026-ARXIV-2603-18464;SF-2026-ARXIV-2603-18516;SF-2026-ARXIV-2603-18567;SF-2026-ARXIV-2603-18773;SF-2026-ARXIV-2603-18829;SF-2026-ARXIV-2603-19025;SF-2026-ARXIV-2603-19131;SF-2026-ARXIV-2603-19133;SF-2026-ARXIV-2603-19173 | pages=100; prefixes=00..99; final_cursor=end; registered=644; screened=644; retained=19; closure=625 | 2026-03-20T01:00:00+00:00 | screening-ledger-final.json#sha256=f51445920e94a7c7e379e3b70f56f0c85b91eaa84161849bfeaa113eb19e4930; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260320:start -->作者侧已逐项筛选全部 644 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260320:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-18016 | arXiv:2603.18016v1 | paper-v1:2603.18016 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18016 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18016 | no |
| SF-2026-ARXIV-2603-18034 | arXiv:2603.18034v1 | paper-v1:2603.18034 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18034 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18034 | no |
| SF-2026-ARXIV-2603-18043 | arXiv:2603.18043v1 | paper-v1:2603.18043 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18043 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18043 | no |
| SF-2026-ARXIV-2603-18046 | arXiv:2603.18046v1 | paper-v1:2603.18046 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18046 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18046 | no |
| SF-2026-ARXIV-2603-18063 | arXiv:2603.18063v1 | paper-v1:2603.18063 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18063 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18063 | no |
| SF-2026-ARXIV-2603-18096 | arXiv:2603.18096v1 | paper-v1:2603.18096 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18096 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18096 | no |
| SF-2026-ARXIV-2603-18245 | arXiv:2603.18245v1 | paper-v1:2603.18245 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18245 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18245 | no |
| SF-2026-ARXIV-2603-18280 | arXiv:2603.18280v1 | paper-v1:2603.18280 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18280 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18280 | no |
| SF-2026-ARXIV-2603-18330 | arXiv:2603.18330v1 | paper-v1:2603.18330 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18330 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18330 | no |
| SF-2026-ARXIV-2603-18433 | arXiv:2603.18433v1 | paper-v1:2603.18433 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18433 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18433 | no |
| SF-2026-ARXIV-2603-18464 | arXiv:2603.18464v1 | paper-v1:2603.18464 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18464 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18464 | no |
| SF-2026-ARXIV-2603-18516 | arXiv:2603.18516v1 | paper-v1:2603.18516 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18516 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18516 | no |
| SF-2026-ARXIV-2603-18567 | arXiv:2603.18567v1 | paper-v1:2603.18567 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18567 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18567 | no |
| SF-2026-ARXIV-2603-18773 | arXiv:2603.18773v1 | paper-v1:2603.18773 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-18773 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18773 | no |
| SF-2026-ARXIV-2603-18829 | arXiv:2603.18829v1 | paper-v1:2603.18829 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-18829 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18829 | no |
| SF-2026-ARXIV-2603-19025 | arXiv:2603.19025v1 | paper-v1:2603.19025 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19025 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19025 | no |
| SF-2026-ARXIV-2603-19131 | arXiv:2603.19131v1 | paper-v1:2603.19131 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19131 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19131 | no |
| SF-2026-ARXIV-2603-19133 | arXiv:2603.19133v1 | paper-v1:2603.19133 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19133 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19133 | no |
| SF-2026-ARXIV-2603-19173 | arXiv:2603.19173v1 | paper-v1:2603.19173 | 2026-W12 | 2026-03-20 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19173 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19173 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-18016 | RP-e878f3288fd699e0 | deep | arXiv:2603.18016v1 | SRC-ARXIV@arXiv:2603.18016v1 | arXiv:2603.18016v1 HTML — §5 MineDraft: A Framework for Batch Parallel Speculative Decoding [facet=method]; https://arxiv.org/html/2603.18016v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18016v1.html; sha256:23e96e5dcf83b976fc1104e5f5d68975794def5eca3e581773f6c72da384e197 | arXiv:2603.18016v1 HTML — §6.2 Results with Different Drafting Strategies [facet=evaluation]; https://arxiv.org/html/2603.18016v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18016v1.html; sha256:23e96e5dcf83b976fc1104e5f5d68975794def5eca3e581773f6c72da384e197 | arXiv:2603.18016v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.18016v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18016v1.html; sha256:23e96e5dcf83b976fc1104e5f5d68975794def5eca3e581773f6c72da384e197 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18016v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18016 | complete |
| SF-2026-ARXIV-2603-18034 | RP-9537361ed4e5cc81 | deep | arXiv:2603.18034v1 | SRC-ARXIV@arXiv:2603.18034v1 | arXiv:2603.18034v1 HTML — §4. Detection Framework (Exploratory) [facet=method]; https://arxiv.org/html/2603.18034v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18034v1.html; sha256:4f0035c5bf4a6780cb627006000bdb8584303e2a1cc1a52ccb24ef33363247d7 | arXiv:2603.18034v1 HTML — §6.3. Multi-Model End-to-End Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18034v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18034v1.html; sha256:4f0035c5bf4a6780cb627006000bdb8584303e2a1cc1a52ccb24ef33363247d7 | arXiv:2603.18034v1 HTML — §7.1. Limitations [facet=limitations]; https://arxiv.org/html/2603.18034v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18034v1.html; sha256:4f0035c5bf4a6780cb627006000bdb8584303e2a1cc1a52ccb24ef33363247d7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18034v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18034 | complete |
| SF-2026-ARXIV-2603-18043 | RP-bd28f7d6cb8c2f86 | deep | arXiv:2603.18043v1 | SRC-ARXIV@arXiv:2603.18043v1 | arXiv:2603.18043v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.18043v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18043v1.html; sha256:848bb6750a672b2771d31e0584fbbbe8cccc9111bed99bd95bd94c4a9359bbe1 | arXiv:2603.18043v1 HTML — §5.4 Real-Model Validation [facet=evaluation]; https://arxiv.org/html/2603.18043v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18043v1.html; sha256:848bb6750a672b2771d31e0584fbbbe8cccc9111bed99bd95bd94c4a9359bbe1 | arXiv:2603.18043v1 HTML — §7 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.18043v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18043v1.html; sha256:848bb6750a672b2771d31e0584fbbbe8cccc9111bed99bd95bd94c4a9359bbe1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18043v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18043 | complete |
| SF-2026-ARXIV-2603-18046 | RP-2e8d555bbb71b6ce | deep | arXiv:2603.18046v1 | SRC-ARXIV@arXiv:2603.18046v1 | arXiv:2603.18046v1 HTML — §2.2 Transformer Architecture [facet=method]; https://arxiv.org/html/2603.18046v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18046v1.html; sha256:b1468eb11a9a1892d7a6aabcea9a61b1152a9c0a35db5c66e8902ee85d07dbb4 | arXiv:2603.18046v1 HTML — §5.2 Empirical Validation [facet=evaluation]; https://arxiv.org/html/2603.18046v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18046v1.html; sha256:b1468eb11a9a1892d7a6aabcea9a61b1152a9c0a35db5c66e8902ee85d07dbb4 | arXiv:2603.18046v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.18046v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18046v1.html; sha256:b1468eb11a9a1892d7a6aabcea9a61b1152a9c0a35db5c66e8902ee85d07dbb4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18046v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18046 | complete |
| SF-2026-ARXIV-2603-18063 | RP-feab8a912688c00d | deep | arXiv:2603.18063v1 | SRC-ARXIV@arXiv:2603.18063v1 | arXiv:2603.18063v1 HTML — §2.3 Existing Framework Coverage [facet=method]; https://arxiv.org/html/2603.18063v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18063v1.html; sha256:0a4ecb9573579f078ca2f20d4b1d06a03cce985e01ecde8a58a1626e8860ad1c | arXiv:2603.18063v1 HTML — §2.4 Gap Analysis and Motivation [facet=evaluation]; https://arxiv.org/html/2603.18063v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18063v1.html; sha256:0a4ecb9573579f078ca2f20d4b1d06a03cce985e01ecde8a58a1626e8860ad1c | arXiv:2603.18063v1 HTML — §2.4 Gap Analysis and Motivation [facet=limitations]; https://arxiv.org/html/2603.18063v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18063v1.html; sha256:0a4ecb9573579f078ca2f20d4b1d06a03cce985e01ecde8a58a1626e8860ad1c | arXiv exact-v1 identity https://arxiv.org/abs/2603.18063v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18063 | complete |
| SF-2026-ARXIV-2603-18096 | RP-1b7296dfd5cb6ff3 | deep | arXiv:2603.18096v1 | SRC-ARXIV@arXiv:2603.18096v1 | arXiv:2603.18096v1 HTML — §IV Framework: Trace Contracts, Adversarial Testing, and Governance [facet=method]; https://arxiv.org/html/2603.18096v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18096v1.html; sha256:e0a3a19a0152171e7054f50cb03761cc70898f8f0b173c92b6d81d1ab502ed68 | arXiv:2603.18096v1 HTML — §V Evaluation and Metrics [facet=evaluation]; https://arxiv.org/html/2603.18096v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18096v1.html; sha256:e0a3a19a0152171e7054f50cb03761cc70898f8f0b173c92b6d81d1ab502ed68 | arXiv:2603.18096v1 HTML — §III System Model and Failure Taxonomy for Agentic Systems [facet=limitations]; https://arxiv.org/html/2603.18096v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18096v1.html; sha256:e0a3a19a0152171e7054f50cb03761cc70898f8f0b173c92b6d81d1ab502ed68 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18096v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18096 | complete |
| SF-2026-ARXIV-2603-18245 | RP-0409a9bfc7e7a1f1 | deep | arXiv:2603.18245v1 | SRC-ARXIV@arXiv:2603.18245v1 | arXiv:2603.18245v1 HTML — §3.1 Problem Formulation [facet=method]; https://arxiv.org/html/2603.18245v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18245v1.html; sha256:3873e31a2a589b3f6512c26031845b11356358910dcae452ae0dcd7417215afb | arXiv:2603.18245v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.18245v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18245v1.html; sha256:3873e31a2a589b3f6512c26031845b11356358910dcae452ae0dcd7417215afb | arXiv:2603.18245v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.18245v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18245v1.html; sha256:3873e31a2a589b3f6512c26031845b11356358910dcae452ae0dcd7417215afb | arXiv exact-v1 identity https://arxiv.org/abs/2603.18245v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18245 | complete |
| SF-2026-ARXIV-2603-18280 | RP-c85f0b3bf6bd6a6b | deep | arXiv:2603.18280v1 | SRC-ARXIV@arXiv:2603.18280v1 | arXiv:2603.18280v1 HTML — §3.3 Surgical Ablation Works in Most Architectures [facet=method]; https://arxiv.org/html/2603.18280v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18280v1.html; sha256:6c457ca691a4476516f3bc5fb011a85e05d987aa6a455456dca00269d9675c46 | arXiv:2603.18280v1 HTML — §2.5 Multi-Judge Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18280v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18280v1.html; sha256:6c457ca691a4476516f3bc5fb011a85e05d987aa6a455456dca00269d9675c46 | arXiv:2603.18280v1 HTML — §6. Limitations [facet=limitations]; https://arxiv.org/html/2603.18280v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18280v1.html; sha256:6c457ca691a4476516f3bc5fb011a85e05d987aa6a455456dca00269d9675c46 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18280v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18280 | complete |
| SF-2026-ARXIV-2603-18330 | RP-ed98a7f98ed00c3a | deep | arXiv:2603.18330v1 | SRC-ARXIV@arXiv:2603.18330v1 | arXiv:2603.18330v1 HTML — §2.2 The Governance Cycle & Dependencies [facet=method]; https://arxiv.org/html/2603.18330v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18330v1.html; sha256:d2e12f5e1ac90944ec99877ba44b890dbb41d3cfc388ab1ee8bca77d066de7bc | arXiv:2603.18330v1 HTML — §3.2 Quantitative Results [facet=evaluation]; https://arxiv.org/html/2603.18330v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18330v1.html; sha256:d2e12f5e1ac90944ec99877ba44b890dbb41d3cfc388ab1ee8bca77d066de7bc | arXiv:2603.18330v1 HTML — §4 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.18330v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18330v1.html; sha256:d2e12f5e1ac90944ec99877ba44b890dbb41d3cfc388ab1ee8bca77d066de7bc | arXiv exact-v1 identity https://arxiv.org/abs/2603.18330v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18330 | complete |
| SF-2026-ARXIV-2603-18433 | RP-0052a84c81bb23e4 | deep | arXiv:2603.18433v1 | SRC-ARXIV@arXiv:2603.18433v1 | arXiv:2603.18433v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.18433v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18433v1.html; sha256:6f9408db77fa13eb38256ab1819bf7d75fc7ce52a56ece042236b62340f680c0 | arXiv:2603.18433v1 HTML — §IV-B Evaluation Variants and Metrics [facet=evaluation]; https://arxiv.org/html/2603.18433v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18433v1.html; sha256:6f9408db77fa13eb38256ab1819bf7d75fc7ce52a56ece042236b62340f680c0 | arXiv:2603.18433v1 HTML — §V-C Limitations [facet=limitations]; https://arxiv.org/html/2603.18433v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18433v1.html; sha256:6f9408db77fa13eb38256ab1819bf7d75fc7ce52a56ece042236b62340f680c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18433v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18433 | complete |
| SF-2026-ARXIV-2603-18464 | RP-3e8f2a2dc0b0f762 | deep | arXiv:2603.18464v1 | SRC-ARXIV@arXiv:2603.18464v1 | arXiv:2603.18464v1 HTML — §5.2 Value Head Design [facet=method]; https://arxiv.org/html/2603.18464v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18464v1.html; sha256:cb6238b35dba2ceccc14c4a44490b496b583896d0a657fa9d2c563beed02067a | arXiv:2603.18464v1 HTML — §6.4 Performance Evaluation of AcceRL-WM on the LIBERO [facet=evaluation]; https://arxiv.org/html/2603.18464v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18464v1.html; sha256:cb6238b35dba2ceccc14c4a44490b496b583896d0a657fa9d2c563beed02067a | arXiv:2603.18464v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.18464v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18464v1.html; sha256:cb6238b35dba2ceccc14c4a44490b496b583896d0a657fa9d2c563beed02067a | arXiv exact-v1 identity https://arxiv.org/abs/2603.18464v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18464 | complete |
| SF-2026-ARXIV-2603-18516 | RP-24011d0a26008ed3 | deep | arXiv:2603.18516v1 | SRC-ARXIV@arXiv:2603.18516v1 | arXiv:2603.18516v1 HTML — §2. TRQA Framework and Data Construction [facet=method]; https://arxiv.org/html/2603.18516v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18516v1.html; sha256:24fa4e5a798900581f3197462ff027b41df145f79fbafb8a8067092595197a5c | arXiv:2603.18516v1 HTML — §5. Results [facet=evaluation]; https://arxiv.org/html/2603.18516v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18516v1.html; sha256:24fa4e5a798900581f3197462ff027b41df145f79fbafb8a8067092595197a5c | arXiv:2603.18516v1 HTML — §6. Conclusions [facet=limitations]; https://arxiv.org/html/2603.18516v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18516v1.html; sha256:24fa4e5a798900581f3197462ff027b41df145f79fbafb8a8067092595197a5c | arXiv exact-v1 identity https://arxiv.org/abs/2603.18516v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18516 | complete |
| SF-2026-ARXIV-2603-18567 | RP-6d0faea45a6d012e | deep | arXiv:2603.18567v1 | SRC-ARXIV@arXiv:2603.18567v1 | arXiv:2603.18567v1 HTML — §2.3 Architecture Paradigm [facet=method]; https://arxiv.org/html/2603.18567v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18567v1.html; sha256:96fa2598e071b17ea4e4d2e494b97987ccc60838c91e14c04201d70f47e3c5e9 | arXiv:2603.18567v1 HTML — §6.1 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.18567v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18567v1.html; sha256:96fa2598e071b17ea4e4d2e494b97987ccc60838c91e14c04201d70f47e3c5e9 | arXiv:2603.18567v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.18567v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18567v1.html; sha256:96fa2598e071b17ea4e4d2e494b97987ccc60838c91e14c04201d70f47e3c5e9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.18567v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18567 | complete |
| SF-2026-ARXIV-2603-18773 | RP-94c423fdceec8b4e | standard | arXiv:2603.18773v1 | SRC-ARXIV@arXiv:2603.18773v1 | arXiv:2603.18773v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.18773v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18773v1.html; sha256:e002b2c2d4c79ec63e2d18e19fb8b4f52e45c5a229620399ffe7037dbb26225e | arXiv:2603.18773v1 HTML — §C.1 End-to-end Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18773v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18773v1.html; sha256:e002b2c2d4c79ec63e2d18e19fb8b4f52e45c5a229620399ffe7037dbb26225e | arXiv:2603.18773v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.18773v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18773v1.html; sha256:e002b2c2d4c79ec63e2d18e19fb8b4f52e45c5a229620399ffe7037dbb26225e | arXiv exact-v1 identity https://arxiv.org/abs/2603.18773v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18773 | complete |
| SF-2026-ARXIV-2603-18829 | RP-0cb5e82226f600e9 | deep | arXiv:2603.18829v1 | SRC-ARXIV@arXiv:2603.18829v1 | arXiv:2603.18829v1 HTML — §2.2 Design Principles [facet=method]; https://arxiv.org/html/2603.18829v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18829v1.html; sha256:8fbf28bf3f0a2d1ae6c695c41bcff5e16fa0599d55e2930d1543af68b2340a5d | arXiv:2603.18829v1 HTML — §3.4 Deterministic Risk Evaluation (ACP-RISK-1.0) [facet=evaluation]; https://arxiv.org/html/2603.18829v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18829v1.html; sha256:8fbf28bf3f0a2d1ae6c695c41bcff5e16fa0599d55e2930d1543af68b2340a5d | arXiv:2603.18829v1 HTML — §11 Conclusion [facet=limitations]; https://arxiv.org/html/2603.18829v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18829v1.html; sha256:8fbf28bf3f0a2d1ae6c695c41bcff5e16fa0599d55e2930d1543af68b2340a5d | arXiv exact-v1 identity https://arxiv.org/abs/2603.18829v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-18829 | complete |
| SF-2026-ARXIV-2603-19025 | RP-dd663c037f4fa69b | deep | arXiv:2603.19025v1 | SRC-ARXIV@arXiv:2603.19025v1 | arXiv:2603.19025v1 HTML — §7.1 Attack Design [facet=method]; https://arxiv.org/html/2603.19025v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19025v1.html; sha256:267868db4581a54ca110727020ba935a2b3b2b2d5a5ddbe6c7cefc8004986828 | arXiv:2603.19025v1 HTML — §8.1 Evaluation Design and Setup [facet=evaluation]; https://arxiv.org/html/2603.19025v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19025v1.html; sha256:267868db4581a54ca110727020ba935a2b3b2b2d5a5ddbe6c7cefc8004986828 | arXiv:2603.19025v1 HTML — §9 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.19025v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19025v1.html; sha256:267868db4581a54ca110727020ba935a2b3b2b2d5a5ddbe6c7cefc8004986828 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19025v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19025 | complete |
| SF-2026-ARXIV-2603-19131 | RP-227bb42cab057bd1 | deep | arXiv:2603.19131v1 | SRC-ARXIV@arXiv:2603.19131v1 | arXiv:2603.19131v1 HTML — §III-A From Model Inference to Robotic Actuation [facet=method]; https://arxiv.org/html/2603.19131v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19131v1.html; sha256:023a8528e507630e2e492bb5d0fddd16a2a4ccb6e17ac648da9b5bcbb7fcd2bb | arXiv:2603.19131v1 HTML — §IV Inference Efficiency vs. Embodied Efficiency [facet=evaluation]; https://arxiv.org/html/2603.19131v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19131v1.html; sha256:023a8528e507630e2e492bb5d0fddd16a2a4ccb6e17ac648da9b5bcbb7fcd2bb | arXiv:2603.19131v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.19131v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19131v1.html; sha256:023a8528e507630e2e492bb5d0fddd16a2a4ccb6e17ac648da9b5bcbb7fcd2bb | arXiv exact-v1 identity https://arxiv.org/abs/2603.19131v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19131 | complete |
| SF-2026-ARXIV-2603-19133 | RP-f7df37df35f23d67 | deep | arXiv:2603.19133v1 | SRC-ARXIV@arXiv:2603.19133v1 | arXiv:2603.19133v1 HTML — §3.3 Efficient Separate Rejection Sampling Algorithm [facet=method]; https://arxiv.org/html/2603.19133v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19133v1.html; sha256:a02ac0d2f0660290a4c49d79cf328a44bd0c9f44dd78ceac11d4532abcd34fbf | arXiv:2603.19133v1 HTML — §4.2 Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.19133v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19133v1.html; sha256:a02ac0d2f0660290a4c49d79cf328a44bd0c9f44dd78ceac11d4532abcd34fbf | arXiv:2603.19133v1 HTML — §4.3 Ablation Experiment [facet=limitations]; https://arxiv.org/html/2603.19133v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19133v1.html; sha256:a02ac0d2f0660290a4c49d79cf328a44bd0c9f44dd78ceac11d4532abcd34fbf | arXiv exact-v1 identity https://arxiv.org/abs/2603.19133v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19133 | complete |
| SF-2026-ARXIV-2603-19173 | RP-7b8967bea849972f | deep | arXiv:2603.19173v1 | SRC-ARXIV@arXiv:2603.19173v1 | arXiv:2603.19173v1 HTML — §4.4 Evaluation Framework [facet=method]; https://arxiv.org/html/2603.19173v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19173v1.html; sha256:4fbe7a072e3898e640425c93711b1c26c20c2b7ace0794f3853d97fb7b522886 | arXiv:2603.19173v1 HTML — §4.4 Evaluation Framework [facet=evaluation]; https://arxiv.org/html/2603.19173v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19173v1.html; sha256:4fbe7a072e3898e640425c93711b1c26c20c2b7ace0794f3853d97fb7b522886 | arXiv:2603.19173v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.19173v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19173v1.html; sha256:4fbe7a072e3898e640425c93711b1c26c20c2b7ace0794f3853d97fb7b522886 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19173v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19173 | complete |

### Source Reviews

### MineDraft: A Framework for Batch Parallel Speculative Decoding

<!-- review:SF-2026-ARXIV-2603-18016:start -->
**问题**：逐序列 speculative decoding 仍让多个样本在 draft/verify 间串行等待，batch 内接受长度不齐加剧空洞。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：MineDraft 对多个请求并行采样候选并重组验证批次，把 speculation scheduling 提升到 batch 控制层。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.18016v1 HTML — §5 MineDraft: A Framework for Batch Parallel Speculative Decoding [facet=method]; https://arxiv.org/html/2603.18016v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18016v1.html; sha256:23e96e5dcf83b976fc1104e5f5d68975794def5eca3e581773f6c72da384e197`。

**Evaluation contract 与未证明部分**：结果支持指定模型、batch 和硬件上的吞吐；未披露 workload 之外不能外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18016v1 HTML — §6.2 Results with Different Drafting Strategies [facet=evaluation]; https://arxiv.org/html/2603.18016v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18016v1.html; sha256:23e96e5dcf83b976fc1104e5f5d68975794def5eca3e581773f6c72da384e197`。

**Trade-off / failure / coexistence**：重组增加缓存和公平性复杂度；低并发时单请求 speculation 更简单。

<!-- claim:SF-2026-ARXIV-2603-18016:start -->**Claim Boundary**：只支持 arXiv:2603.18016v1 §5 MineDraft: A Framework for Batch Parallel Speculative Decoding 的机制与 §6.2 Results with Different Drafting Strategies 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18016:end -->
<!-- review:SF-2026-ARXIV-2603-18016:end -->
### Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems

<!-- review:SF-2026-ARXIV-2603-18034:start -->
**问题**：RAG poisoning 的有效载荷依赖 corpus 语境，离线静态检测不能代表检索时的实际暴露。

**旧路径为何合理**：可信小语料库直接检索即可提供低成本 grounding。

**约束变化与机制**：Semantic Chameleon 同时操纵文档语义位置与触发上下文，并把防御放在 ingestion、retrieval 和 generation 三个边界比较。

**State / data / control owner**：`AGENT-RAG` 负责 文档身份、索引、检索结果与引用 lineage；定位证据为 `arXiv:2603.18034v1 HTML — §4. Detection Framework (Exploratory) [facet=method]; https://arxiv.org/html/2603.18034v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18034v1.html; sha256:4f0035c5bf4a6780cb627006000bdb8584303e2a1cc1a52ccb24ef33363247d7`。

**Evaluation contract 与未证明部分**：实验支持所测 retriever/corpus 的攻击与缓解，不证明新语域同样成立。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18034v1 HTML — §6.3. Multi-Model End-to-End Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18034v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18034v1.html; sha256:4f0035c5bf4a6780cb627006000bdb8584303e2a1cc1a52ccb24ef33363247d7`。

**Trade-off / failure / coexistence**：更严格过滤降低 recall；可信小语料库可用 provenance allowlist。

<!-- claim:SF-2026-ARXIV-2603-18034:start -->**Claim Boundary**：只支持 arXiv:2603.18034v1 §4. Detection Framework (Exploratory) 的机制与 §6.3. Multi-Model End-to-End Evaluation 的公开 workload；§7.1. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18034:end -->
<!-- review:SF-2026-ARXIV-2603-18034:end -->
### The Provenance Paradox in Multi-Agent LLM Routing: Delegation Contracts and Attested Identity in LDP

<!-- review:SF-2026-ARXIV-2603-18043:start -->
**问题**：多 agent delegation 中，路由层看到的名称不等于可证明的执行主体，身份和能力可被转接。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文把 delegation contract 与 attested identity 绑定，使每次路由同时携带 principal、能力范围和可验证出处。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.18043v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.18043v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18043v1.html; sha256:848bb6750a672b2771d31e0584fbbbe8cccc9111bed99bd95bd94c4a9359bbe1`。

**Evaluation contract 与未证明部分**：主要证据是协议/威胁模型，不构成生产性能或全面安全证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18043v1 HTML — §5.4 Real-Model Validation [facet=evaluation]; https://arxiv.org/html/2603.18043v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18043v1.html; sha256:848bb6750a672b2771d31e0584fbbbe8cccc9111bed99bd95bd94c4a9359bbe1`。

**Trade-off / failure / coexistence**：证明链增加密钥、撤销和延迟成本；封闭单进程 agent 可使用进程内身份。

<!-- claim:SF-2026-ARXIV-2603-18043:start -->**Claim Boundary**：只支持 arXiv:2603.18043v1 §4 Implementation 的机制与 §5.4 Real-Model Validation 的公开 workload；§7 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18043:end -->
<!-- review:SF-2026-ARXIV-2603-18043:end -->
### NanoZK: Privacy-Preserving Verifiable Inference for Large Language Models via Layerwise Zero-Knowledge Proofs

<!-- review:SF-2026-ARXIV-2603-18046:start -->
**问题**：远端 LLM inference 的保密性不足以证明服务端按声明模型和计算执行。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：NanoZK 将推理拆成逐层可验证关系，以零知识证明连接输入承诺、权重承诺与输出。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.18046v1 HTML — §2.2 Transformer Architecture [facet=method]; https://arxiv.org/html/2603.18046v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18046v1.html; sha256:b1468eb11a9a1892d7a6aabcea9a61b1152a9c0a35db5c66e8902ee85d07dbb4`。

**Evaluation contract 与未证明部分**：论文 benchmark 只支持所测网络规模和证明系统的开销；远未证明大模型在线 SLO。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18046v1 HTML — §5.2 Empirical Validation [facet=evaluation]; https://arxiv.org/html/2603.18046v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18046v1.html; sha256:b1468eb11a9a1892d7a6aabcea9a61b1152a9c0a35db5c66e8902ee85d07dbb4`。

**Trade-off / failure / coexistence**：可验证性付出巨大 proving 成本；可信执行环境或本地推理在某些威胁模型下更实用。

<!-- claim:SF-2026-ARXIV-2603-18046:start -->**Claim Boundary**：只支持 arXiv:2603.18046v1 §2.2 Transformer Architecture 的机制与 §5.2 Empirical Validation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18046:end -->
<!-- review:SF-2026-ARXIV-2603-18046:end -->
### MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0)

<!-- review:SF-2026-ARXIV-2603-18063:start -->
**问题**：MCP 把发现、描述与调用工具放进协议后，传统 API 威胁分类缺少对语义委托和 capability confusion 的表达。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：MCP-38 按 server、tool metadata、sampling、transport 与跨组件 trust boundary 建立 38 类威胁及对应资产/攻击路径。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.18063v1 HTML — §2.3 Existing Framework Coverage [facet=method]; https://arxiv.org/html/2603.18063v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18063v1.html; sha256:0a4ecb9573579f078ca2f20d4b1d06a03cce985e01ecde8a58a1626e8860ad1c`。

**Evaluation contract 与未证明部分**：exact-v1 是 taxonomy 与框架映射，没有攻击覆盖率或防护效果实验；它只能作为 threat-model denominator。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18063v1 HTML — §2.4 Gap Analysis and Motivation [facet=evaluation]; https://arxiv.org/html/2603.18063v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18063v1.html; sha256:0a4ecb9573579f078ca2f20d4b1d06a03cce985e01ecde8a58a1626e8860ad1c`。

**Trade-off / failure / coexistence**：统一词汇有助审计，但分类重叠和协议演化会带来维护成本；固定私有工具集仍可用较窄威胁模型。

<!-- claim:SF-2026-ARXIV-2603-18063:start -->**Claim Boundary**：只支持 arXiv:2603.18063v1 §2.3 Existing Framework Coverage 的机制与 §2.4 Gap Analysis and Motivation 的公开 workload；§2.4 Gap Analysis and Motivation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18063:end -->
<!-- review:SF-2026-ARXIV-2603-18063:end -->
### A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance

<!-- review:SF-2026-ARXIV-2603-18096:start -->
**问题**：agent orchestration 的失败可能来自长链状态和外部副作用，单次输出测试无法提供 assurance。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：框架把 contract、trace assertion、failure injection 与 governance evidence 关联到同一 workflow execution。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `arXiv:2603.18096v1 HTML — §IV Framework: Trace Contracts, Adversarial Testing, and Governance [facet=method]; https://arxiv.org/html/2603.18096v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18096v1.html; sha256:e0a3a19a0152171e7054f50cb03761cc70898f8f0b173c92b6d81d1ab502ed68`。

**Evaluation contract 与未证明部分**：论文展示方法和案例，不能证明规则集合覆盖开放世界副作用。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18096v1 HTML — §V Evaluation and Metrics [facet=evaluation]; https://arxiv.org/html/2603.18096v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18096v1.html; sha256:e0a3a19a0152171e7054f50cb03761cc70898f8f0b173c92b6d81d1ab502ed68`。

**Trade-off / failure / coexistence**：更强 trace assurance 增加存储和隐私成本；短幂等 flow 可用普通测试。

<!-- claim:SF-2026-ARXIV-2603-18096:start -->**Claim Boundary**：只支持 arXiv:2603.18096v1 §IV Framework: Trace Contracts, Adversarial Testing, and Governance 的机制与 §V Evaluation and Metrics 的公开 workload；§III System Model and Failure Taxonomy for Agentic Systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18096:end -->
<!-- review:SF-2026-ARXIV-2603-18096:end -->
### Who Tests the Testers? Systematic Enumeration and Coverage Audit of LLM Agent Tool Call Safety

<!-- review:SF-2026-ARXIV-2603-18245:start -->
**问题**：安全 benchmark 自己可能漏掉关键 tool-call workflow，单看 agent 得分无法知道测试分母是否完整。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：SafeAudit 系统枚举工具、风险、前置状态与交互序列，再量化既有 benchmark 的 coverage 与新增场景。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.18245v1 HTML — §3.1 Problem Formulation [facet=method]; https://arxiv.org/html/2603.18245v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18245v1.html; sha256:3873e31a2a589b3f6512c26031845b11356358910dcae452ae0dcd7417215afb`。

**Evaluation contract 与未证明部分**：实验支持对公开 tool-call benchmark 的覆盖审计；枚举规则和环境模型仍可能漏掉未知风险。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18245v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.18245v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18245v1.html; sha256:3873e31a2a589b3f6512c26031845b11356358910dcae452ae0dcd7417215afb`。

**Trade-off / failure / coexistence**：meta-audit 让 coverage 可计算，却显著扩大场景空间；窄工具集可采用人工威胁模型作为较低成本基线。

<!-- claim:SF-2026-ARXIV-2603-18245:start -->**Claim Boundary**：只支持 arXiv:2603.18245v1 §3.1 Problem Formulation 的机制与 §4.2 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18245:end -->
<!-- review:SF-2026-ARXIV-2603-18245:end -->
### Detection Is Cheap, Routing Is Learned: Why Refusal-Based Alignment Evaluation Fails

<!-- review:SF-2026-ARXIV-2603-18280:start -->
**问题**：refusal rate 与概念 probe 只说明模型识别危险内容或选择拒绝，不能定位 alignment 实际改变了哪层行为路由。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：研究用 probes、surgical ablation 和行为测试分离 concept representation 与 policy routing，观察防护是否只改变从识别到动作的映射。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.18280v1 HTML — §3.3 Surgical Ablation Works in Most Architectures [facet=method]; https://arxiv.org/html/2603.18280v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18280v1.html; sha256:6c457ca691a4476516f3bc5fb011a85e05d987aa6a455456dca00269d9675c46`。

**Evaluation contract 与未证明部分**：九个开放权重模型的自然实验只支持该政治审查任务中的层间差异，不代表所有安全训练机制。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18280v1 HTML — §2.5 Multi-Judge Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18280v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18280v1.html; sha256:6c457ca691a4476516f3bc5fb011a85e05d987aa6a455456dca00269d9675c46`。

**Trade-off / failure / coexistence**：内部可解释测试信息更丰富但依赖权重访问且可能误读相关激活；API 模型只能用行为评估。

<!-- claim:SF-2026-ARXIV-2603-18280:start -->**Claim Boundary**：只支持 arXiv:2603.18280v1 §3.3 Surgical Ablation Works in Most Architectures 的机制与 §2.5 Multi-Judge Evaluation 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18280:end -->
<!-- review:SF-2026-ARXIV-2603-18280:end -->
### MemArchitect: A Policy Driven Memory Governance Layer

<!-- review:SF-2026-ARXIV-2603-18330:start -->
**问题**：持久 agent memory 若只追加和向量检索，会把矛盾、过期或越权内容重新注入 context。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：MemArchitect 把 retention、conflict resolution、privacy 和 expiry 编成独立 policy layer，在读写两侧治理 memory lifecycle。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.18330v1 HTML — §2.2 The Governance Cycle & Dependencies [facet=method]; https://arxiv.org/html/2603.18330v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18330v1.html; sha256:d2e12f5e1ac90944ec99877ba44b890dbb41d3cfc388ab1ee8bca77d066de7bc`。

**Evaluation contract 与未证明部分**：原型评测支持所测 memory scenarios 的规则执行；不证明策略能自动判断所有语义冲突。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18330v1 HTML — §3.2 Quantitative Results [facet=evaluation]; https://arxiv.org/html/2603.18330v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18330v1.html; sha256:d2e12f5e1ac90944ec99877ba44b890dbb41d3cfc388ab1ee8bca77d066de7bc`。

**Trade-off / failure / coexistence**：policy layer 增加延迟与误删风险；短会话或只读知识可保持简单 RAG。

<!-- claim:SF-2026-ARXIV-2603-18330:start -->**Claim Boundary**：只支持 arXiv:2603.18330v1 §2.2 The Governance Cycle & Dependencies 的机制与 §3.2 Quantitative Results 的公开 workload；§4 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18330:end -->
<!-- review:SF-2026-ARXIV-2603-18330:end -->
### Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems

<!-- review:SF-2026-ARXIV-2603-18433:start -->
**问题**：prompt injection 的实质是低优先级不可信内容夺取高优先级控制流，单纯关键词过滤无法表达冲突来源。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：PCFI 在 gateway 维护消息优先级与 role provenance，以 lexical、role-switch 和 hierarchy check 阻止低级输入覆盖系统约束。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.18433v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.18433v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18433v1.html; sha256:6f9408db77fa13eb38256ab1819bf7d75fc7ce52a56ece042236b62340f680c0`。

**Evaluation contract 与未证明部分**：公开评测比较概念性无防护基线、各阶段信号与完整 pipeline；它未证明对语义等价或跨语言攻击完备。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18433v1 HTML — §IV-B Evaluation Variants and Metrics [facet=evaluation]; https://arxiv.org/html/2603.18433v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18433v1.html; sha256:6f9408db77fa13eb38256ab1819bf7d75fc7ce52a56ece042236b62340f680c0`。

**Trade-off / failure / coexistence**：运行时层级检查可快速阻断明显违规，但误报会损害任务完成；无外部内容的受控 prompt 可保留轻量过滤。

<!-- claim:SF-2026-ARXIV-2603-18433:start -->**Claim Boundary**：只支持 arXiv:2603.18433v1 §III Methodology 的机制与 §IV-B Evaluation Variants and Metrics 的公开 workload；§V-C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18433:end -->
<!-- review:SF-2026-ARXIV-2603-18433:end -->
### AcceRL: A Distributed Asynchronous Reinforcement Learning and World Model Framework for Vision-Language-Action Models

<!-- review:SF-2026-ARXIV-2603-18464:start -->
**问题**：VLA RL 同步等待环境 rollout、inference 和 update，慢环境会让昂贵 GPU 形成级联 idle bubble。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：AcceRL 物理解耦三类 actor，并以异步队列和版本策略连接 rollout、world model 与 learner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.18464v1 HTML — §5.2 Value Head Design [facet=method]; https://arxiv.org/html/2603.18464v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18464v1.html; sha256:cb6238b35dba2ceccc14c4a44490b496b583896d0a657fa9d2c563beed02067a`。

**Evaluation contract 与未证明部分**：集群实验支持指定 scale 的利用率/训练结果；policy staleness 和 simulator bias 限制跨任务外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18464v1 HTML — §6.4 Performance Evaluation of AcceRL-WM on the LIBERO [facet=evaluation]; https://arxiv.org/html/2603.18464v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18464v1.html; sha256:cb6238b35dba2ceccc14c4a44490b496b583896d0a657fa9d2c563beed02067a`。

**Trade-off / failure / coexistence**：异步提高吞吐却牺牲严格 on-policy freshness；小规模稳定环境仍适合同步训练。

<!-- claim:SF-2026-ARXIV-2603-18464:start -->**Claim Boundary**：只支持 arXiv:2603.18464v1 §5.2 Value Head Design 的机制与 §6.4 Performance Evaluation of AcceRL-WM on the LIBERO 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18464:end -->
<!-- review:SF-2026-ARXIV-2603-18464:end -->
### Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents

<!-- review:SF-2026-ARXIV-2603-18516:start -->
**问题**：deep-research agent 的答案可覆盖很多来源，却遗漏关键文档；只测最终文本正确率看不到检索 denominator。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Total Recall QA 借鉴 total-recall protocol，将候选文档集合、发现曲线和可验证引用共同纳入评测。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.18516v1 HTML — §2. TRQA Framework and Data Construction [facet=method]; https://arxiv.org/html/2603.18516v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18516v1.html; sha256:24fa4e5a798900581f3197462ff027b41df145f79fbafb8a8067092595197a5c`。

**Evaluation contract 与未证明部分**：suite 证明其任务集可重放，不代表开放 Web 的相关文档集合可完全枚举。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18516v1 HTML — §5. Results [facet=evaluation]; https://arxiv.org/html/2603.18516v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18516v1.html; sha256:24fa4e5a798900581f3197462ff027b41df145f79fbafb8a8067092595197a5c`。

**Trade-off / failure / coexistence**：提高 recall evaluation 会显著增加标注与检索成本；封闭 corpus 更易建立 oracle。

<!-- claim:SF-2026-ARXIV-2603-18516:start -->**Claim Boundary**：只支持 arXiv:2603.18516v1 §2. TRQA Framework and Data Construction 的机制与 §5. Results 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18516:end -->
<!-- review:SF-2026-ARXIV-2603-18516:end -->
### SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding

<!-- review:SF-2026-ARXIV-2603-18567:start -->
**问题**：speculative decoding 的收益依赖 draft model 训练，但现有训练实现分散，数据、loss 与分布式执行难比较。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：SpecForge 把 draft 数据生成、训练目标和可扩展训练 runtime 模块化，使不同 proposal 方案共享同一训练合同。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.18567v1 HTML — §2.3 Architecture Paradigm [facet=method]; https://arxiv.org/html/2603.18567v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18567v1.html; sha256:96fa2598e071b17ea4e4d2e494b97987ccc60838c91e14c04201d70f47e3c5e9`。

**Evaluation contract 与未证明部分**：系统评测与两个公开实现比较训练性能；它不等价于证明所有 target/draft 组合都获得高接受率。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18567v1 HTML — §6.1 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.18567v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18567v1.html; sha256:96fa2598e071b17ea4e4d2e494b97987ccc60838c91e14c04201d70f47e3c5e9`。

**Trade-off / failure / coexistence**：统一框架降低实验成本，却增加抽象层和兼容维护；现成 draft 已满足 workload 时无需新训练栈。

<!-- claim:SF-2026-ARXIV-2603-18567:start -->**Claim Boundary**：只支持 arXiv:2603.18567v1 §2.3 Architecture Paradigm 的机制与 §6.1 Evaluation Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18567:end -->
<!-- review:SF-2026-ARXIV-2603-18567:end -->
### Automatic Configuration of LLM Post-Training Pipelines

<!-- review:SF-2026-ARXIV-2603-18773:start -->
**问题**：SFT 与 RL 参数相互耦合，逐阶段单独调参可能得到局部最优而让整条 post-training pipeline 退化。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：AutoPipe 先在便宜设置学习配置排序，再用少量 end-to-end 观测做 local correction，搜索联合 SFT-RL 配方。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.18773v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.18773v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18773v1.html; sha256:e002b2c2d4c79ec63e2d18e19fb8b4f52e45c5a229620399ffe7037dbb26225e`。

**Evaluation contract 与未证明部分**：验证集中在 biomedical chain-of-thought QA；结果支持 ranking transfer 在该域降低搜索成本，不证明跨域排序稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18773v1 HTML — §C.1 End-to-end Evaluation [facet=evaluation]; https://arxiv.org/html/2603.18773v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18773v1.html; sha256:e002b2c2d4c79ec63e2d18e19fb8b4f52e45c5a229620399ffe7037dbb26225e`。

**Trade-off / failure / coexistence**：代理排序节省算力但可能因规模/数据变化反转；预算足够或风险高时完整联合 sweep 仍是可靠基线。

<!-- claim:SF-2026-ARXIV-2603-18773:start -->**Claim Boundary**：只支持 arXiv:2603.18773v1 §3 Methodology 的机制与 §C.1 End-to-end Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18773:end -->
<!-- review:SF-2026-ARXIV-2603-18773:end -->
### Agent Control Protocol: Admission Control for Agent Actions

<!-- review:SF-2026-ARXIV-2603-18829:start -->
**问题**：单次合法 action 组合后仍可能形成危险行为，stateless policy 看不到累计风险和 cooldown。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：ACP 以 ledger 保存行为历史，把静态 risk score 与 anomaly accumulation/cooldown 合成为执行前 admission decision。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.18829v1 HTML — §2.2 Design Principles [facet=method]; https://arxiv.org/html/2603.18829v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18829v1.html; sha256:8fbf28bf3f0a2d1ae6c695c41bcff5e16fa0599d55e2930d1543af68b2340a5d`。

**Evaluation contract 与未证明部分**：500-request 合成 workload 证明其规则下的时序阻断；不证明风险分数能覆盖未知行为。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.18829v1 HTML — §3.4 Deterministic Risk Evaluation (ACP-RISK-1.0) [facet=evaluation]; https://arxiv.org/html/2603.18829v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.18829v1.html; sha256:8fbf28bf3f0a2d1ae6c695c41bcff5e16fa0599d55e2930d1543af68b2340a5d`。

**Trade-off / failure / coexistence**：stateful admission 会产生误拒和 ledger 一致性负担；无历史依赖动作仍可 stateless 检查。

<!-- claim:SF-2026-ARXIV-2603-18829:start -->**Claim Boundary**：只支持 arXiv:2603.18829v1 §2.2 Design Principles 的机制与 §3.4 Deterministic Risk Evaluation (ACP-RISK-1.0) 的公开 workload；§11 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-18829:end -->
<!-- review:SF-2026-ARXIV-2603-18829:end -->
### Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference

<!-- review:SF-2026-ARXIV-2603-19025:start -->
**问题**：云端模型客户既无法本地重跑，也难承受完整 ZK 推理，模型身份和执行正确性因此缺少可用证明。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文用抽样/轻量 cryptographic commitments 证明部分中间计算，并以统计检测替代逐算子完整证明。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.19025v1 HTML — §7.1 Attack Design [facet=method]; https://arxiv.org/html/2603.19025v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19025v1.html; sha256:267868db4581a54ca110727020ba935a2b3b2b2d5a5ddbe6c7cefc8004986828`。

**Evaluation contract 与未证明部分**：实验支持所测模型下的 verifier/prover 开销与检测概率；它不是确定性正确性保证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19025v1 HTML — §8.1 Evaluation Design and Setup [facet=evaluation]; https://arxiv.org/html/2603.19025v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19025v1.html; sha256:267868db4581a54ca110727020ba935a2b3b2b2d5a5ddbe6c7cefc8004986828`。

**Trade-off / failure / coexistence**：轻量化用概率 assurance 换性能，且抽样面可能被适应；高风险场景仍需完整证明或可信硬件。

<!-- claim:SF-2026-ARXIV-2603-19025:start -->**Claim Boundary**：只支持 arXiv:2603.19025v1 §7.1 Attack Design 的机制与 §8.1 Evaluation Design and Setup 的公开 workload；§9 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19025:end -->
<!-- review:SF-2026-ARXIV-2603-19025:end -->
### From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models

<!-- review:SF-2026-ARXIV-2603-19131:start -->
**问题**：VLA 的 tokens/s 或单次 latency 不能说明机器人是否在控制周期内完成安全、有效动作。

**旧路径为何合理**：单次模型调用用 TTFT/TPOT 和吞吐定位局部瓶颈最直接。

**约束变化与机制**：论文把 inference、action chunk、actuation 与任务完成串成 embodied-efficiency contract，联合测量模型速度和物理执行。

**State / data / control owner**：`INFER-REQUEST-LIFECYCLE` 负责 request phase、action proposal、actuation、task outcome 与闭环 SLO；定位证据为 `arXiv:2603.19131v1 HTML — §III-A From Model Inference to Robotic Actuation [facet=method]; https://arxiv.org/html/2603.19131v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19131v1.html; sha256:023a8528e507630e2e492bb5d0fddd16a2a4ccb6e17ac648da9b5bcbb7fcd2bb`。

**Evaluation contract 与未证明部分**：实验能证明传统推理指标在所测 VLA/机器人任务上与真实表现错位；不能外推到未测 embodiment 与控制频率。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19131v1 HTML — §IV Inference Efficiency vs. Embodied Efficiency [facet=evaluation]; https://arxiv.org/html/2603.19131v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19131v1.html; sha256:023a8528e507630e2e492bb5d0fddd16a2a4ccb6e17ac648da9b5bcbb7fcd2bb`。

**Trade-off / failure / coexistence**：端到端指标更真实但重复成本高、环境噪声大；纯模型优化阶段仍可保留推理指标作局部信号。

<!-- claim:SF-2026-ARXIV-2603-19131:start -->**Claim Boundary**：只支持 arXiv:2603.19131v1 §III-A From Model Inference to Robotic Actuation 的机制与 §IV Inference Efficiency vs. Embodied Efficiency 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19131:end -->
<!-- review:SF-2026-ARXIV-2603-19131:end -->
### A Pipelined Collaborative Speculative Decoding Framework for Efficient Edge-Cloud LLM Inference

<!-- review:SF-2026-ARXIV-2603-19133:start -->
**问题**：edge-cloud speculative decoding 会同时受 uplink、draft 速度和验证流水线约束，串行传输会抵消 speculation 收益。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：PicoSpec 把 edge proposal、分块传输与 cloud verification 管线化，并以概率模型决定通信和计算重叠。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.19133v1 HTML — §3.3 Efficient Separate Rejection Sampling Algorithm [facet=method]; https://arxiv.org/html/2603.19133v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19133v1.html; sha256:a02ac0d2f0660290a4c49d79cf328a44bd0c9f44dd78ceac11d4532abcd34fbf`。

**Evaluation contract 与未证明部分**：论文用 throughput 模型和 edge-cloud 实验刻画边界；收益依赖网络、接受率和 batch 配置。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19133v1 HTML — §4.2 Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.19133v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19133v1.html; sha256:a02ac0d2f0660290a4c49d79cf328a44bd0c9f44dd78ceac11d4532abcd34fbf`。

**Trade-off / failure / coexistence**：流水线提高重叠但增加版本、回滚和缓存提交状态；网络差或接受率低时本地/云端普通 decode 更稳。

<!-- claim:SF-2026-ARXIV-2603-19133:start -->**Claim Boundary**：只支持 arXiv:2603.19133v1 §3.3 Efficient Separate Rejection Sampling Algorithm 的机制与 §4.2 Performance Evaluation 的公开 workload；§4.3 Ablation Experiment 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19133:end -->
<!-- review:SF-2026-ARXIV-2603-19133:end -->
### SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits

<!-- review:SF-2026-ARXIV-2603-19173:start -->
**问题**：kernel benchmark 若只相对软件 baseline 报 speedup，无法区分优化器进步与 baseline 低效。

**旧路径为何合理**：成熟 vendor kernel 在稳定 shape 上通常最可靠。

**约束变化与机制**：SOL-ExecBench 以硬件 speed-of-light 上界规范 235 个真实 kernel，并要求结果绑定 Blackwell、精度与前后向 workload。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel/graph execution、量化、编译和硬件适配；定位证据为 `arXiv:2603.19173v1 HTML — §4.4 Evaluation Framework [facet=method]; https://arxiv.org/html/2603.19173v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19173v1.html; sha256:4fbe7a072e3898e640425c93711b1c26c20c2b7ace0794f3853d97fb7b522886`。

**Evaluation contract 与未证明部分**：它建立可比较的效率合同，但只覆盖指定 GPU 世代和算子集合。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19173v1 HTML — §4.4 Evaluation Framework [facet=evaluation]; https://arxiv.org/html/2603.19173v1; papers/2026/03/_sources/daily-20260320/exact-v1-bodies/2603.19173v1.html; sha256:4fbe7a072e3898e640425c93711b1c26c20c2b7ace0794f3853d97fb7b522886`。

**Trade-off / failure / coexistence**：接近理论上界仍不代表端到端最优；跨硬件必须重建 roofline。

<!-- claim:SF-2026-ARXIV-2603-19173:start -->**Claim Boundary**：只支持 arXiv:2603.19173v1 §4.4 Evaluation Framework 的机制与 §4.4 Evaluation Framework 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19173:end -->
<!-- review:SF-2026-ARXIV-2603-19173:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-18016 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18016 |
| SF-2026-ARXIV-2603-18034 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18034 |
| SF-2026-ARXIV-2603-18043 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18043 |
| SF-2026-ARXIV-2603-18046 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18046 |
| SF-2026-ARXIV-2603-18063 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18063 |
| SF-2026-ARXIV-2603-18096 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18096 |
| SF-2026-ARXIV-2603-18245 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18245 |
| SF-2026-ARXIV-2603-18280 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18280 |
| SF-2026-ARXIV-2603-18330 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18330 |
| SF-2026-ARXIV-2603-18433 | score_7_9 | selected | DA-20260320-10 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260320-10 |
| SF-2026-ARXIV-2603-18464 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18464 |
| SF-2026-ARXIV-2603-18516 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18516 |
| SF-2026-ARXIV-2603-18567 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-18567 |
| SF-2026-ARXIV-2603-18829 | score_7_9 | selected | DA-20260320-15 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260320-15 |
| SF-2026-ARXIV-2603-19025 | score_7_9 | selected | DA-20260320-16 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260320-16 |
| SF-2026-ARXIV-2603-19131 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19131 |
| SF-2026-ARXIV-2603-19133 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19133 |
| SF-2026-ARXIV-2603-19173 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19173 |

<!-- analysis-decision:SF-2026-ARXIV-2603-18016:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18016:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18034:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18034:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18043:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18043:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18046:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18046:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18063:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18063:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18096:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18096:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18245:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18245:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18280:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18280:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18330:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18330:end -->
<!-- analysis:DA-20260320-10:start -->
### Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems

prompt injection 的实质是低优先级不可信内容夺取高优先级控制流，单纯关键词过滤无法表达冲突来源。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：PCFI 在 gateway 维护消息优先级与 role provenance，以 lexical、role-switch 和 hierarchy check 阻止低级输入覆盖系统约束。 其公开验证边界为：公开评测比较概念性无防护基线、各阶段信号与完整 pipeline；它未证明对语义等价或跨语言攻击完备。 新增代价与回退条件为：运行时层级检查可快速阻断明显违规，但误报会损害任务完成；无外部内容的受控 prompt 可保留轻量过滤。
<!-- analysis:DA-20260320-10:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18464:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18464:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18516:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18516:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-18567:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-18567:end -->
<!-- analysis:DA-20260320-15:start -->
### Agent Control Protocol: Admission Control for Agent Actions

单次合法 action 组合后仍可能形成危险行为，stateless policy 看不到累计风险和 cooldown。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：ACP 以 ledger 保存行为历史，把静态 risk score 与 anomaly accumulation/cooldown 合成为执行前 admission decision。 其公开验证边界为：500-request 合成 workload 证明其规则下的时序阻断；不证明风险分数能覆盖未知行为。 新增代价与回退条件为：stateful admission 会产生误拒和 ledger 一致性负担；无历史依赖动作仍可 stateless 检查。
<!-- analysis:DA-20260320-15:end -->
<!-- analysis:DA-20260320-16:start -->
### Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference

云端模型客户既无法本地重跑，也难承受完整 ZK 推理，模型身份和执行正确性因此缺少可用证明。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：论文用抽样/轻量 cryptographic commitments 证明部分中间计算，并以统计检测替代逐算子完整证明。 其公开验证边界为：实验支持所测模型下的 verifier/prover 开销与检测概率；它不是确定性正确性保证。 新增代价与回退条件为：轻量化用概率 assurance 换性能，且抽样面可能被适应；高风险场景仍需完整证明或可信硬件。
<!-- analysis:DA-20260320-16:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19131:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19131:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19133:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19133:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19173:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19173:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-18016 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#moe-verification-还要结算-target-expert-expansion (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18016 | delta:SF-2026-ARXIV-2603-18016 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18016 |
| SF-2026-ARXIV-2603-18034 | AGENT-RAG | books/part-07-agent/76-rag.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/75-context.md#第75章-context (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18034 | delta:SF-2026-ARXIV-2603-18034 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18034 |
| SF-2026-ARXIV-2603-18043 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#局部合理动作会累积成有害轨迹 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18043 | delta:SF-2026-ARXIV-2603-18043 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18043 |
| SF-2026-ARXIV-2603-18046 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#responsive-不等于-semantic-available (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18046 | delta:SF-2026-ARXIV-2603-18046 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18046 |
| SF-2026-ARXIV-2603-18063 | AGENT-MCP | books/part-07-agent/83-mcp.md#update-2026-07-29-—-从连接会话到显式请求契约 (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18063 | delta:SF-2026-ARXIV-2603-18063 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18063 |
| SF-2026-ARXIV-2603-18096 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18096 | delta:SF-2026-ARXIV-2603-18096 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18096 |
| SF-2026-ARXIV-2603-18245 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#tool-成功要从-component-扩展到-information-use-与-outcome (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18245 | delta:SF-2026-ARXIV-2603-18245 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18245 |
| SF-2026-ARXIV-2603-18280 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18280 | delta:SF-2026-ARXIV-2603-18280 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18280 |
| SF-2026-ARXIV-2603-18330 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18330 | delta:SF-2026-ARXIV-2603-18330 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18330 |
| SF-2026-ARXIV-2603-18433 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18433 | delta:SF-2026-ARXIV-2603-18433 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18433 |
| SF-2026-ARXIV-2603-18464 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18464 | delta:SF-2026-ARXIV-2603-18464 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18464 |
| SF-2026-ARXIV-2603-18516 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#self-report、behavior-probe-与-deployment-outcome-是三种证据 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18516 | delta:SF-2026-ARXIV-2603-18516 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18516 |
| SF-2026-ARXIV-2603-18567 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18567 | delta:SF-2026-ARXIV-2603-18567 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18567 |
| SF-2026-ARXIV-2603-18773 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18773 | delta:SF-2026-ARXIV-2603-18773 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18773 |
| SF-2026-ARXIV-2603-18829 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#harness-backdoor-把单次写入变成跨-run-控制状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-18829 | delta:SF-2026-ARXIV-2603-18829 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-18829 |
| SF-2026-ARXIV-2603-19025 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#responsive-不等于-semantic-available (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19025 | delta:SF-2026-ARXIV-2603-19025 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19025 |
| SF-2026-ARXIV-2603-19131 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/41-deepspeed.md#第41章-训练状态-runtime-policy：以-deepspeed-为例 (section Ch-adjacent); books/part-05-inference-system/43-prefill.md#第43章-prefill (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19131 | delta:SF-2026-ARXIV-2603-19131 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19131 |
| SF-2026-ARXIV-2603-19133 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19133 | delta:SF-2026-ARXIV-2603-19133 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19133 |
| SF-2026-ARXIV-2603-19173 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19173 | delta:SF-2026-ARXIV-2603-19173 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19173 |

<!-- books-review:SF-2026-ARXIV-2603-18016:start -->
### MineDraft: A Framework for Batch Parallel Speculative Decoding — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18016:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：第四，系统调度必须支持它。Speculative Decoding 改变了 Decode 的 token 产出形态：一个请求一次可能接受多个 token，也可能回退。这会影响 KV Cache 追加、batch scheduling、streaming 输出和 latency 统计。<!-- existing:SF-2026-ARXIV-2603-18016:end -->

<!-- delta:SF-2026-ARXIV-2603-18016:start -->新证据差异：MineDraft 对多个请求并行采样候选并重组验证批次，把 speculation scheduling 提升到 batch 控制层。<!-- delta:SF-2026-ARXIV-2603-18016:end -->

边界：只支持 arXiv:2603.18016v1 §5 MineDraft: A Framework for Batch Parallel Speculative Decoding 的机制与 §6.2 Results with Different Drafting Strategies 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18016:end -->
<!-- books-review:SF-2026-ARXIV-2603-18034:start -->
### Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18034:start -->已读 owner `books/part-07-agent/76-rag.md` 与相邻章节。现有命题：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2603-18034:end -->

<!-- delta:SF-2026-ARXIV-2603-18034:start -->新证据差异：Semantic Chameleon 同时操纵文档语义位置与触发上下文，并把防御放在 ingestion、retrieval 和 generation 三个边界比较。<!-- delta:SF-2026-ARXIV-2603-18034:end -->

边界：只支持 arXiv:2603.18034v1 §4. Detection Framework (Exploratory) 的机制与 §6.3. Multi-Model End-to-End Evaluation 的公开 workload；§7.1. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18034:end -->
<!-- books-review:SF-2026-ARXIV-2603-18043:start -->
### The Provenance Paradox in Multi-Agent LLM Routing: Delegation Contracts and Attested Identity in LDP — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18043:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：多 Agent 委派把这条链再推进一步：有害目标可能被拆成多个局部合理的子任务，单节点重新做 prompt classification 仍看不见跨节点累积的语义。运行时需要把 source、delegation、memory write 与 irreversible sink 组织成带 provenance 的信息流，在 sink 前重建跨节点上下文，再由确定性 policy 决定是否允许 commit。 这用额外图状态、标注误差和重建延迟换取跨委派风险可见性；semantic taint 仍只是 sensor input，不替代 capability isolation，也不能授权 LLM 自己拥有最终安全判决。<!-- existing:SF-2026-ARXIV-2603-18043:end -->

<!-- delta:SF-2026-ARXIV-2603-18043:start -->新证据差异：论文把 delegation contract 与 attested identity 绑定，使每次路由同时携带 principal、能力范围和可验证出处。<!-- delta:SF-2026-ARXIV-2603-18043:end -->

边界：只支持 arXiv:2603.18043v1 §4 Implementation 的机制与 §5.4 Real-Model Validation 的公开 workload；§7 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18043:end -->
<!-- books-review:SF-2026-ARXIV-2603-18046:start -->
### NanoZK: Privacy-Preserving Verifiable Inference for Large Language Models via Layerwise Zero-Knowledge Proofs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18046:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：分布式 inference 的 availability 不能只问 endpoint 是否按时返回。Fast / slow-path pipeline 若只在 deadline 前合并远端高质量结果，deadline 同时就是 semantic commit boundary：攻击者无需访问权重或 victim data，只要用 shaped burst 推迟 slow path，merger 就可能丢弃本应提高准确率的证据。系统仍及时响应，却发生 accuracy collapse。<!-- existing:SF-2026-ARXIV-2603-18046:end -->

<!-- delta:SF-2026-ARXIV-2603-18046:start -->新证据差异：NanoZK 将推理拆成逐层可验证关系，以零知识证明连接输入承诺、权重承诺与输出。<!-- delta:SF-2026-ARXIV-2603-18046:end -->

边界：只支持 arXiv:2603.18046v1 §2.2 Transformer Architecture 的机制与 §5.2 Empirical Validation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18046:end -->
<!-- books-review:SF-2026-ARXIV-2603-18063:start -->
### MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0) — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18063:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：`subscriptions/listen`、trace context、cache hints 与移入官方 extension 的 tasks 说明协议正在把长时交互、可观测性和缓存建议从隐式连接行为改写为显式契约。 Roots、Sampling、Logging 和 HTTP+SSE 则进入 feature lifecycle 的 deprecated 阶段。这里的“稳定”只描述 specification revision；它不表示 SDK/server fleet 已经同步迁移。官方 TypeScript SDK 迁移指南仍要求显式 opt-in，旧实现也可能继续 使用 2025-era handshake，因此生产部署必须按目标 SDK 与 server 的实际 revision 做 capability probe、兼容测试和分阶段迁移。<!-- existing:SF-2026-ARXIV-2603-18063:end -->

<!-- delta:SF-2026-ARXIV-2603-18063:start -->新证据差异：MCP-38 按 server、tool metadata、sampling、transport 与跨组件 trust boundary 建立 38 类威胁及对应资产/攻击路径。<!-- delta:SF-2026-ARXIV-2603-18063:end -->

边界：只支持 arXiv:2603.18063v1 §2.3 Existing Framework Coverage 的机制与 §2.4 Gap Analysis and Motivation 的公开 workload；§2.4 Gap Analysis and Motivation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18063:end -->
<!-- books-review:SF-2026-ARXIV-2603-18096:start -->
### A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18096:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**<!-- existing:SF-2026-ARXIV-2603-18096:end -->

<!-- delta:SF-2026-ARXIV-2603-18096:start -->新证据差异：框架把 contract、trace assertion、failure injection 与 governance evidence 关联到同一 workflow execution。<!-- delta:SF-2026-ARXIV-2603-18096:end -->

边界：只支持 arXiv:2603.18096v1 §IV Framework: Trace Contracts, Adversarial Testing, and Governance 的机制与 §V Evaluation and Metrics 的公开 workload；§III System Model and Failure Taxonomy for Agentic Systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18096:end -->
<!-- books-review:SF-2026-ARXIV-2603-18245:start -->
### Who Tests the Testers? Systematic Enumeration and Coverage Audit of LLM Agent Tool Call Safety — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18245:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Oracle retrieval 分支可以定位瓶颈，却不是生产系统成绩；增加 step budget 可能改善 coverage，也会制造循环与成本 尾部。MADQA 的受限 PDF collection 支持 `accuracy x grounding x effort x failure stage` 比单一正确率更有诊断性， 不证明其语料、模型排名或 tool budget 可外推到企业私有、多语言环境。Corpus 小、retrieval 稳定时 static RAG 仍更可控；多步 Agent 只有在 action trace、evidence provenance 与 refusal/recovery 一起评估时才增加可信度。<!-- existing:SF-2026-ARXIV-2603-18245:end -->

<!-- delta:SF-2026-ARXIV-2603-18245:start -->新证据差异：SafeAudit 系统枚举工具、风险、前置状态与交互序列，再量化既有 benchmark 的 coverage 与新增场景。<!-- delta:SF-2026-ARXIV-2603-18245:end -->

边界：只支持 arXiv:2603.18245v1 §3.1 Problem Formulation 的机制与 §4.2 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18245:end -->
<!-- books-review:SF-2026-ARXIV-2603-18280:start -->
### Detection Is Cheap, Routing Is Learned: Why Refusal-Based Alignment Evaluation Fails — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18280:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-18280:end -->

<!-- delta:SF-2026-ARXIV-2603-18280:start -->新证据差异：研究用 probes、surgical ablation 和行为测试分离 concept representation 与 policy routing，观察防护是否只改变从识别到动作的映射。<!-- delta:SF-2026-ARXIV-2603-18280:end -->

边界：只支持 arXiv:2603.18280v1 §3.3 Surgical Ablation Works in Most Architectures 的机制与 §2.5 Multi-Judge Evaluation 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18280:end -->
<!-- books-review:SF-2026-ARXIV-2603-18330:start -->
### MemArchitect: A Policy Driven Memory Governance Layer — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18330:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-18330:end -->

<!-- delta:SF-2026-ARXIV-2603-18330:start -->新证据差异：MemArchitect 把 retention、conflict resolution、privacy 和 expiry 编成独立 policy layer，在读写两侧治理 memory lifecycle。<!-- delta:SF-2026-ARXIV-2603-18330:end -->

边界：只支持 arXiv:2603.18330v1 §2.2 The Governance Cycle & Dependencies 的机制与 §3.2 Quantitative Results 的公开 workload；§4 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18330:end -->
<!-- books-review:SF-2026-ARXIV-2603-18433:start -->
### Prompt Control-Flow Integrity: A Priority-Aware Runtime Defense Against Prompt Injection in LLM Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18433:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-18433:end -->

<!-- delta:SF-2026-ARXIV-2603-18433:start -->新证据差异：PCFI 在 gateway 维护消息优先级与 role provenance，以 lexical、role-switch 和 hierarchy check 阻止低级输入覆盖系统约束。<!-- delta:SF-2026-ARXIV-2603-18433:end -->

边界：只支持 arXiv:2603.18433v1 §III Methodology 的机制与 §IV-B Evaluation Variants and Metrics 的公开 workload；§V-C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18433:end -->
<!-- books-review:SF-2026-ARXIV-2603-18464:start -->
### AcceRL: A Distributed Asynchronous Reinforcement Learning and World Model Framework for Vision-Language-Action Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18464:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-18464:end -->

<!-- delta:SF-2026-ARXIV-2603-18464:start -->新证据差异：AcceRL 物理解耦三类 actor，并以异步队列和版本策略连接 rollout、world model 与 learner。<!-- delta:SF-2026-ARXIV-2603-18464:end -->

边界：只支持 arXiv:2603.18464v1 §5.2 Value Head Design 的机制与 §6.4 Performance Evaluation of AcceRL-WM on the LIBERO 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18464:end -->
<!-- books-review:SF-2026-ARXIV-2603-18516:start -->
### Total Recall QA: A Verifiable Evaluation Suite for Deep Research Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18516:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失： 写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge 与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。<!-- existing:SF-2026-ARXIV-2603-18516:end -->

<!-- delta:SF-2026-ARXIV-2603-18516:start -->新证据差异：Total Recall QA 借鉴 total-recall protocol，将候选文档集合、发现曲线和可验证引用共同纳入评测。<!-- delta:SF-2026-ARXIV-2603-18516:end -->

边界：只支持 arXiv:2603.18516v1 §2. TRQA Framework and Data Construction 的机制与 §5. Results 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18516:end -->
<!-- books-review:SF-2026-ARXIV-2603-18567:start -->
### SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18567:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2603-18567:end -->

<!-- delta:SF-2026-ARXIV-2603-18567:start -->新证据差异：SpecForge 把 draft 数据生成、训练目标和可扩展训练 runtime 模块化，使不同 proposal 方案共享同一训练合同。<!-- delta:SF-2026-ARXIV-2603-18567:end -->

边界：只支持 arXiv:2603.18567v1 §2.3 Architecture Paradigm 的机制与 §6.1 Evaluation Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18567:end -->
<!-- books-review:SF-2026-ARXIV-2603-18773:start -->
### Automatic Configuration of LLM Post-Training Pipelines — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18773:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-18773:end -->

<!-- delta:SF-2026-ARXIV-2603-18773:start -->新证据差异：AutoPipe 先在便宜设置学习配置排序，再用少量 end-to-end 观测做 local correction，搜索联合 SFT-RL 配方。<!-- delta:SF-2026-ARXIV-2603-18773:end -->

边界：只支持 arXiv:2603.18773v1 §3 Methodology 的机制与 §C.1 End-to-end Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18773:end -->
<!-- books-review:SF-2026-ARXIV-2603-18829:start -->
### Agent Control Protocol: Admission Control for Agent Actions — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-18829:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：当前 run 内检查 prompt、tool call 与 workspace mutation，在会话结束即清空、配置不可写时边界清楚；可持久化 harness 允许一次良性任务把 payload 写入 instruction、config、hook 或 memory，后续 run 才在特定 trigger 下接管行为。防线因此 不能只判断“这次写是否合法”，还要为每个 durable control cell 保存 writer principal、source provenance、content digest、 policy generation、activation predicate 与生命周期，并在 load/trigger 前重新 admission。State owner 拥有 publish、quarantine、 revocation 与 rollback；Agent 只能提出 mutation，不能凭后续运行中的自我解释让旧写入升级为可信 policy。<!-- existing:SF-2026-ARXIV-2603-18829:end -->

<!-- delta:SF-2026-ARXIV-2603-18829:start -->新证据差异：ACP 以 ledger 保存行为历史，把静态 risk score 与 anomaly accumulation/cooldown 合成为执行前 admission decision。<!-- delta:SF-2026-ARXIV-2603-18829:end -->

边界：只支持 arXiv:2603.18829v1 §2.2 Design Principles 的机制与 §3.4 Deterministic Risk Evaluation (ACP-RISK-1.0) 的公开 workload；§11 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-18829:end -->
<!-- books-review:SF-2026-ARXIV-2603-19025:start -->
### Towards Verifiable AI with Lightweight Cryptographic Proofs of Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19025:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：分布式 inference 的 availability 不能只问 endpoint 是否按时返回。Fast / slow-path pipeline 若只在 deadline 前合并远端高质量结果，deadline 同时就是 semantic commit boundary：攻击者无需访问权重或 victim data，只要用 shaped burst 推迟 slow path，merger 就可能丢弃本应提高准确率的证据。系统仍及时响应，却发生 accuracy collapse。<!-- existing:SF-2026-ARXIV-2603-19025:end -->

<!-- delta:SF-2026-ARXIV-2603-19025:start -->新证据差异：论文用抽样/轻量 cryptographic commitments 证明部分中间计算，并以统计检测替代逐算子完整证明。<!-- delta:SF-2026-ARXIV-2603-19025:end -->

边界：只支持 arXiv:2603.19025v1 §7.1 Attack Design 的机制与 §8.1 Evaluation Design and Setup 的公开 workload；§9 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19025:end -->
<!-- books-review:SF-2026-ARXIV-2603-19131:start -->
### From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19131:start -->已读 owner `books/part-05-inference-system/42-what-happens-during-inference.md` 与相邻章节。现有命题：本章的核心判断是：**LLM inference 是一个持续演化的 token-generation process，而不是一次无状态函数调用。**请求会依次经历输入处理、admission、Prefill、Decode、streaming 和完成清理；每一步都在改变 token progress、KV ownership、GPU memory 与调度资格。<!-- existing:SF-2026-ARXIV-2603-19131:end -->

<!-- delta:SF-2026-ARXIV-2603-19131:start -->新证据差异：论文把 inference、action chunk、actuation 与任务完成串成 embodied-efficiency contract，联合测量模型速度和物理执行。<!-- delta:SF-2026-ARXIV-2603-19131:end -->

边界：只支持 arXiv:2603.19131v1 §III-A From Model Inference to Robotic Actuation 的机制与 §IV Inference Efficiency vs. Embodied Efficiency 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19131:end -->
<!-- books-review:SF-2026-ARXIV-2603-19133:start -->
### A Pipelined Collaborative Speculative Decoding Framework for Efficient Edge-Cloud LLM Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19133:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：自回归 Decode 每次只能生成一个 token，这是 LLM 推理延迟的根本瓶颈之一。Speculative Decoding 为什么能让大模型“看起来一次生成多个 token”？它为什么不是简单地用小模型替代大模型？它在什么条件下才真正有效？<!-- existing:SF-2026-ARXIV-2603-19133:end -->

<!-- delta:SF-2026-ARXIV-2603-19133:start -->新证据差异：PicoSpec 把 edge proposal、分块传输与 cloud verification 管线化，并以概率模型决定通信和计算重叠。<!-- delta:SF-2026-ARXIV-2603-19133:end -->

边界：只支持 arXiv:2603.19133v1 §3.3 Efficient Separate Rejection Sampling Algorithm 的机制与 §4.2 Performance Evaluation 的公开 workload；§4.3 Ablation Experiment 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19133:end -->
<!-- books-review:SF-2026-ARXIV-2603-19173:start -->
### SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Hardware Limits — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19173:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2603-19173:end -->

<!-- delta:SF-2026-ARXIV-2603-19173:start -->新证据差异：SOL-ExecBench 以硬件 speed-of-light 上界规范 235 个真实 kernel，并要求结果绑定 Blackwell、精度与前后向 workload。<!-- delta:SF-2026-ARXIV-2603-19173:end -->

边界：只支持 arXiv:2603.19173v1 §4.4 Evaluation Framework 的机制与 §4.4 Evaluation Framework 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19173:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260320-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260320 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260320-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260320-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260320-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | — | accepted: 所有 Books disposition 已复核，本日无需写回 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260320/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日所有候选均已获得最终 disposition；没有需要写入 Books 的长期机制，后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- Books Decision 已闭合，本日无需修改 Books。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 普通 Gate finding=0；blocked / unverified / disputed=0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `Complete`
- Coverage: `Closed`
- Evidence: `Passed`
- Books: `Passed`
- unresolved findings: 0
