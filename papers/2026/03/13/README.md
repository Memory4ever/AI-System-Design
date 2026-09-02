# Daily Research — 2026-03-13

**Research Date:** 2026-03-13

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-12 09:00:00 ～ 2026-03-13 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=614/614/614；denominator=31、pre-denominator closures=583。exact-v1 Review complete=31、blocked=0；Integrate 建议=2。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-13 |
| Window End | 2026-03-13 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260313-AUTHOR-31 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-12T09:00:00+08:00 | 2026-03-13T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 614/614 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 614 | SF-2026-ARXIV-2603-11053;SF-2026-ARXIV-2603-11088;SF-2026-ARXIV-2603-11101;SF-2026-ARXIV-2603-11132;SF-2026-ARXIV-2603-11212;SF-2026-ARXIV-2603-11273;SF-2026-ARXIV-2603-11287;SF-2026-ARXIV-2603-11337;SF-2026-ARXIV-2603-11340;SF-2026-ARXIV-2603-11438;SF-2026-ARXIV-2603-11445;SF-2026-ARXIV-2603-11504;SF-2026-ARXIV-2603-11535;SF-2026-ARXIV-2603-11560;SF-2026-ARXIV-2603-11564;SF-2026-ARXIV-2603-11619;SF-2026-ARXIV-2603-11768;SF-2026-ARXIV-2603-11853;SF-2026-ARXIV-2603-11873;SF-2026-ARXIV-2603-11875;SF-2026-ARXIV-2603-11896;SF-2026-ARXIV-2603-11935;SF-2026-ARXIV-2603-11975;SF-2026-ARXIV-2603-12031;SF-2026-ARXIV-2603-12038;SF-2026-ARXIV-2603-12056;SF-2026-ARXIV-2603-12118;SF-2026-ARXIV-2603-12201;SF-2026-ARXIV-2603-12230;SF-2026-ARXIV-2603-12255;SF-2026-ARXIV-2603-12262 | pages=100; prefixes=00..99; final_cursor=end; registered=614; screened=614; retained=31; closure=583 | 2026-03-13T01:00:00+00:00 | screening-ledger-final.json#sha256=5c99f2f2a9d9bd3ab6002d60e65076ea881d3cf58accdb40e984d5bc959beac9; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260313:start -->作者侧已逐项筛选全部 614 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260313:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-11053 | arXiv:2603.11053v1 | paper-v1:2603.11053 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11053 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11053 | no |
| SF-2026-ARXIV-2603-11088 | arXiv:2603.11088v1 | paper-v1:2603.11088 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11088 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11088 | no |
| SF-2026-ARXIV-2603-11101 | arXiv:2603.11101v1 | paper-v1:2603.11101 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11101 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11101 | no |
| SF-2026-ARXIV-2603-11132 | arXiv:2603.11132v1 | paper-v1:2603.11132 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11132 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11132 | no |
| SF-2026-ARXIV-2603-11212 | arXiv:2603.11212v1 | paper-v1:2603.11212 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11212 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11212 | no |
| SF-2026-ARXIV-2603-11273 | arXiv:2603.11273v1 | paper-v1:2603.11273 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11273 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11273 | no |
| SF-2026-ARXIV-2603-11287 | arXiv:2603.11287v1 | paper-v1:2603.11287 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11287 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11287 | no |
| SF-2026-ARXIV-2603-11337 | arXiv:2603.11337v1 | paper-v1:2603.11337 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11337 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11337 | no |
| SF-2026-ARXIV-2603-11340 | arXiv:2603.11340v1 | paper-v1:2603.11340 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11340 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11340 | no |
| SF-2026-ARXIV-2603-11438 | arXiv:2603.11438v1 | paper-v1:2603.11438 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-11438 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2603-11438 | no |
| SF-2026-ARXIV-2603-11445 | arXiv:2603.11445v1 | paper-v1:2603.11445 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11445 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11445 | no |
| SF-2026-ARXIV-2603-11504 | arXiv:2603.11504v1 | paper-v1:2603.11504 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11504 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11504 | no |
| SF-2026-ARXIV-2603-11535 | arXiv:2603.11535v1 | paper-v1:2603.11535 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11535 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11535 | no |
| SF-2026-ARXIV-2603-11560 | arXiv:2603.11560v1 | paper-v1:2603.11560 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11560 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11560 | no |
| SF-2026-ARXIV-2603-11564 | arXiv:2603.11564v1 | paper-v1:2603.11564 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11564 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11564 | no |
| SF-2026-ARXIV-2603-11619 | arXiv:2603.11619v1 | paper-v1:2603.11619 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11619 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11619 | no |
| SF-2026-ARXIV-2603-11768 | arXiv:2603.11768v1 | paper-v1:2603.11768 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11768 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11768 | no |
| SF-2026-ARXIV-2603-11853 | arXiv:2603.11853v1 | paper-v1:2603.11853 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11853 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11853 | no |
| SF-2026-ARXIV-2603-11873 | arXiv:2603.11873v1 | paper-v1:2603.11873 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11873 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11873 | no |
| SF-2026-ARXIV-2603-11875 | arXiv:2603.11875v1 | paper-v1:2603.11875 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11875 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11875 | no |
| SF-2026-ARXIV-2603-11896 | arXiv:2603.11896v1 | paper-v1:2603.11896 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11896 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11896 | no |
| SF-2026-ARXIV-2603-11935 | arXiv:2603.11935v1 | paper-v1:2603.11935 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11935 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11935 | no |
| SF-2026-ARXIV-2603-11975 | arXiv:2603.11975v1 | paper-v1:2603.11975 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-11975 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11975 | no |
| SF-2026-ARXIV-2603-12031 | arXiv:2603.12031v1 | paper-v1:2603.12031 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12031 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12031 | no |
| SF-2026-ARXIV-2603-12038 | arXiv:2603.12038v1 | paper-v1:2603.12038 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12038 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12038 | no |
| SF-2026-ARXIV-2603-12056 | arXiv:2603.12056v1 | paper-v1:2603.12056 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12056 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12056 | no |
| SF-2026-ARXIV-2603-12118 | arXiv:2603.12118v1 | paper-v1:2603.12118 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-12118 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-12118 | no |
| SF-2026-ARXIV-2603-12201 | arXiv:2603.12201v1 | paper-v1:2603.12201 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12201 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12201 | no |
| SF-2026-ARXIV-2603-12230 | arXiv:2603.12230v1 | paper-v1:2603.12230 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12230 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12230 | no |
| SF-2026-ARXIV-2603-12255 | arXiv:2603.12255v1 | paper-v1:2603.12255 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12255 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12255 | no |
| SF-2026-ARXIV-2603-12262 | arXiv:2603.12262v1 | paper-v1:2603.12262 | 2026-W11 | 2026-03-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12262 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12262 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-11053 | RP-df7adadbd602a0f0 | standard | arXiv:2603.11053v1 | SRC-ARXIV@arXiv:2603.11053v1 | arXiv:2603.11053v1 HTML — §5.1 Motivation and Numerical Approximation Methodology [facet=method]; https://arxiv.org/html/2603.11053v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11053v1.html; sha256:061e695127e2cbae381421b985b83b83a577d95c374ea48f8ff284b7ead0d1e5 | arXiv:2603.11053v1 HTML — §Results and validation. [facet=evaluation]; https://arxiv.org/html/2603.11053v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11053v1.html; sha256:061e695127e2cbae381421b985b83b83a577d95c374ea48f8ff284b7ead0d1e5 | arXiv:2603.11053v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.11053v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11053v1.html; sha256:061e695127e2cbae381421b985b83b83a577d95c374ea48f8ff284b7ead0d1e5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11053v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11053 | complete |
| SF-2026-ARXIV-2603-11088 | RP-dc776a68291ce666 | standard | arXiv:2603.11088v1 | SRC-ARXIV@arXiv:2603.11088v1 | arXiv:2603.11088v1 HTML — §4.4. Attack Methods [facet=method]; https://arxiv.org/html/2603.11088v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11088v1.html; sha256:a4377324e268ba95cf1dbdacb8644dfc36bae3049642218da9ccc5163e948dc4 | arXiv:2603.11088v1 HTML — §5.2.5. Human-In-The-Loop Validation [facet=evaluation]; https://arxiv.org/html/2603.11088v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11088v1.html; sha256:a4377324e268ba95cf1dbdacb8644dfc36bae3049642218da9ccc5163e948dc4 | arXiv:2603.11088v1 HTML — §8. Conclusion [facet=limitations]; https://arxiv.org/html/2603.11088v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11088v1.html; sha256:a4377324e268ba95cf1dbdacb8644dfc36bae3049642218da9ccc5163e948dc4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11088v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11088 | complete |
| SF-2026-ARXIV-2603-11101 | RP-4a0176a35cedc0e7 | standard | arXiv:2603.11101v1 | SRC-ARXIV@arXiv:2603.11101v1 | arXiv:2603.11101v1 HTML — §2.1 Overall Architecture Design [facet=method]; https://arxiv.org/html/2603.11101v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11101v1.html; sha256:2b44ad55ba20d6134493ef4fa04d43d90d07a9b09649f7fd6f13f686b6f6819b | arXiv:2603.11101v1 HTML — §3.1 Thousand-GPU Scale Framework Validation [facet=evaluation]; https://arxiv.org/html/2603.11101v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11101v1.html; sha256:2b44ad55ba20d6134493ef4fa04d43d90d07a9b09649f7fd6f13f686b6f6819b | arXiv:2603.11101v1 HTML — §4 Conclusion and Future Outlook [facet=limitations]; https://arxiv.org/html/2603.11101v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11101v1.html; sha256:2b44ad55ba20d6134493ef4fa04d43d90d07a9b09649f7fd6f13f686b6f6819b | arXiv exact-v1 identity https://arxiv.org/abs/2603.11101v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11101 | complete |
| SF-2026-ARXIV-2603-11132 | RP-e87edc554e9aba16 | standard | arXiv:2603.11132v1 | SRC-ARXIV@arXiv:2603.11132v1 | arXiv:2603.11132v1 HTML — §3.1 Threat Models [facet=method]; https://arxiv.org/html/2603.11132v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11132v1.html; sha256:ed02ca48aad4bcd6f5108fed3776631469e8211d65b9811f77180bb6fa2d1b5f | arXiv:2603.11132v1 HTML — §4.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11132v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11132v1.html; sha256:ed02ca48aad4bcd6f5108fed3776631469e8211d65b9811f77180bb6fa2d1b5f | arXiv:2603.11132v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.11132v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11132v1.html; sha256:ed02ca48aad4bcd6f5108fed3776631469e8211d65b9811f77180bb6fa2d1b5f | arXiv exact-v1 identity https://arxiv.org/abs/2603.11132v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11132 | complete |
| SF-2026-ARXIV-2603-11212 | RP-9eb4b1a0ea11301c | standard | arXiv:2603.11212v1 | SRC-ARXIV@arXiv:2603.11212v1 | arXiv:2603.11212v1 HTML — §V-A Datasets and Baseline Methods [facet=method]; https://arxiv.org/html/2603.11212v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11212v1.html; sha256:7f68d5d17ee4ea71ad0144ba63af4a155a47011389df76e24b2963bbfea946b1 | arXiv:2603.11212v1 HTML — §V Comparative Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11212v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11212v1.html; sha256:7f68d5d17ee4ea71ad0144ba63af4a155a47011389df76e24b2963bbfea946b1 | arXiv:2603.11212v1 HTML — §VI Discussion [facet=limitations]; https://arxiv.org/html/2603.11212v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11212v1.html; sha256:7f68d5d17ee4ea71ad0144ba63af4a155a47011389df76e24b2963bbfea946b1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11212v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11212 | complete |
| SF-2026-ARXIV-2603-11273 | RP-49d75dfb7ecae3bf | standard | arXiv:2603.11273v1 | SRC-ARXIV@arXiv:2603.11273v1 | arXiv:2603.11273v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.11273v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11273v1.html; sha256:ed607304032ba48bc06d5aa30e3d777867bfa9f0518d7f027ab9ec0016636e81 | arXiv:2603.11273v1 HTML — §Evaluation Metrics. [facet=evaluation]; https://arxiv.org/html/2603.11273v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11273v1.html; sha256:ed607304032ba48bc06d5aa30e3d777867bfa9f0518d7f027ab9ec0016636e81 | arXiv:2603.11273v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.11273v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11273v1.html; sha256:ed607304032ba48bc06d5aa30e3d777867bfa9f0518d7f027ab9ec0016636e81 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11273v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11273 | complete |
| SF-2026-ARXIV-2603-11287 | RP-04974d1029db10e8 | standard | arXiv:2603.11287v1 | SRC-ARXIV@arXiv:2603.11287v1 | arXiv:2603.11287v1 HTML — §Pass rate versus implementation quality. [facet=method]; https://arxiv.org/html/2603.11287v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11287v1.html; sha256:256bb91f0d11616be63a5dd0fed92184e473d572082822f0272445e525db4c08 | arXiv:2603.11287v1 HTML — §3.2. Evaluation Pipeline [facet=evaluation]; https://arxiv.org/html/2603.11287v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11287v1.html; sha256:256bb91f0d11616be63a5dd0fed92184e473d572082822f0272445e525db4c08 | arXiv:2603.11287v1 HTML — §Limitations and future work. [facet=limitations]; https://arxiv.org/html/2603.11287v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11287v1.html; sha256:256bb91f0d11616be63a5dd0fed92184e473d572082822f0272445e525db4c08 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11287v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11287 | complete |
| SF-2026-ARXIV-2603-11337 | RP-538d65e6f50cffc1 | standard | arXiv:2603.11337v1 | SRC-ARXIV@arXiv:2603.11337v1 | arXiv:2603.11337v1 HTML — §V Experimental Design [facet=method]; https://arxiv.org/html/2603.11337v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11337v1.html; sha256:516c6ea497eb225fa74bb6c8557ac584490e862b49acf5f23bf4620e0bcffe6f | arXiv:2603.11337v1 HTML — §VI Results [facet=evaluation]; https://arxiv.org/html/2603.11337v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11337v1.html; sha256:516c6ea497eb225fa74bb6c8557ac584490e862b49acf5f23bf4620e0bcffe6f | arXiv:2603.11337v1 HTML — §VII Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.11337v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11337v1.html; sha256:516c6ea497eb225fa74bb6c8557ac584490e862b49acf5f23bf4620e0bcffe6f | arXiv exact-v1 identity https://arxiv.org/abs/2603.11337v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11337 | complete |
| SF-2026-ARXIV-2603-11340 | RP-1f9a7c2509437524 | standard | arXiv:2603.11340v1 | SRC-ARXIV@arXiv:2603.11340v1 | arXiv:2603.11340v1 HTML — §II-B SLO-Tuner system design [facet=method]; https://arxiv.org/html/2603.11340v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11340v1.html; sha256:1164eb8ff6859ccacb63e3ec30db5ca8b71510f24d2b6bdfdfb3307570389ab5 | arXiv:2603.11340v1 HTML — §II-C Results [facet=evaluation]; https://arxiv.org/html/2603.11340v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11340v1.html; sha256:1164eb8ff6859ccacb63e3ec30db5ca8b71510f24d2b6bdfdfb3307570389ab5 | arXiv:2603.11340v1 HTML — §III Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.11340v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11340v1.html; sha256:1164eb8ff6859ccacb63e3ec30db5ca8b71510f24d2b6bdfdfb3307570389ab5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11340v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11340 | complete |
| SF-2026-ARXIV-2603-11438 | RP-894025db8dd4082e | deep | arXiv:2603.11438v1 | SRC-ARXIV@arXiv:2603.11438v1 | arXiv:2603.11438v1 HTML — §3.3. Architecture [facet=method]; https://arxiv.org/html/2603.11438v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11438v1.html; sha256:0e97e9e1eb1a293a5a0f96f233dacd104852d736d57354c80c849b8129fbf518 | arXiv:2603.11438v1 HTML — §5.1–§5.3 overhead, verifier/hot-reload and policy case studies [facet=evaluation]; https://arxiv.org/html/2603.11438v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11438v1.html; sha256:0e97e9e1eb1a293a5a0f96f233dacd104852d736d57354c80c849b8129fbf518 | arXiv:2603.11438v1 HTML — §7. Discussion [facet=limitations]; https://arxiv.org/html/2603.11438v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11438v1.html; sha256:0e97e9e1eb1a293a5a0f96f233dacd104852d736d57354c80c849b8129fbf518 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11438v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11438 | complete |
| SF-2026-ARXIV-2603-11445 | RP-eda8b09296ffe83f | standard | arXiv:2603.11445v1 | SRC-ARXIV@arXiv:2603.11445v1 | arXiv:2603.11445v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.11445v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11445v1.html; sha256:1532303b2d73c947ea37f054541cd41ac4e69259a7bdeb1f047f8f70e6cd5fdd | arXiv:2603.11445v1 HTML — §5.3 Results [facet=evaluation]; https://arxiv.org/html/2603.11445v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11445v1.html; sha256:1532303b2d73c947ea37f054541cd41ac4e69259a7bdeb1f047f8f70e6cd5fdd | arXiv:2603.11445v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.11445v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11445v1.html; sha256:1532303b2d73c947ea37f054541cd41ac4e69259a7bdeb1f047f8f70e6cd5fdd | arXiv exact-v1 identity https://arxiv.org/abs/2603.11445v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11445 | complete |
| SF-2026-ARXIV-2603-11504 | RP-bcad187e1d3f19d5 | standard | arXiv:2603.11504v1 | SRC-ARXIV@arXiv:2603.11504v1 | arXiv:2603.11504v1 HTML — §3.1 A Lightweight Design Philosophy [facet=method]; https://arxiv.org/html/2603.11504v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11504v1.html; sha256:17e497d769bcec912da606d8647a2454a48456d3b4f7a478bf8ea96bef79e707 | arXiv:2603.11504v1 HTML — §4.2 Main Results on Model Accuracy [facet=evaluation]; https://arxiv.org/html/2603.11504v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11504v1.html; sha256:17e497d769bcec912da606d8647a2454a48456d3b4f7a478bf8ea96bef79e707 | arXiv:2603.11504v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.11504v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11504v1.html; sha256:17e497d769bcec912da606d8647a2454a48456d3b4f7a478bf8ea96bef79e707 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11504v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11504 | complete |
| SF-2026-ARXIV-2603-11535 | RP-5fec986bb41b3bf3 | standard | arXiv:2603.11535v1 | SRC-ARXIV@arXiv:2603.11535v1 | arXiv:2603.11535v1 HTML — §Appendix B Architecture Details [facet=method]; https://arxiv.org/html/2603.11535v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11535v1.html; sha256:b10f8e3c824ecf10a2e0a314dcf04c899cc613cff5901d3b43a99cb18ace569d | arXiv:2603.11535v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11535v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11535v1.html; sha256:b10f8e3c824ecf10a2e0a314dcf04c899cc613cff5901d3b43a99cb18ace569d | arXiv:2603.11535v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.11535v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11535v1.html; sha256:b10f8e3c824ecf10a2e0a314dcf04c899cc613cff5901d3b43a99cb18ace569d | arXiv exact-v1 identity https://arxiv.org/abs/2603.11535v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11535 | complete |
| SF-2026-ARXIV-2603-11560 | RP-333ae7c4a56c88fe | standard | arXiv:2603.11560v1 | SRC-ARXIV@arXiv:2603.11560v1 | arXiv:2603.11560v1 HTML — §2 The Structural Architecture of Coordination [facet=method]; https://arxiv.org/html/2603.11560v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11560v1.html; sha256:3f49d5b371e93bfb4a989bd1fe016ee28a08027a0e917cfe194367964c892818 | arXiv:2603.11560v1 HTML — §How Intelligence Emerges: A Minimal Theory of Dynamic Adaptive Coordination [facet=evaluation]; https://arxiv.org/html/2603.11560v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11560v1.html; sha256:3f49d5b371e93bfb4a989bd1fe016ee28a08027a0e917cfe194367964c892818 | arXiv:2603.11560v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.11560v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11560v1.html; sha256:3f49d5b371e93bfb4a989bd1fe016ee28a08027a0e917cfe194367964c892818 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11560v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11560 | complete |
| SF-2026-ARXIV-2603-11564 | RP-2de349179d5f9313 | standard | arXiv:2603.11564v1 | SRC-ARXIV@arXiv:2603.11564v1 | arXiv:2603.11564v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.11564v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11564v1.html; sha256:34c5a66de1b92d508d22ad3b4eff82afbf385d69bde5463acb512e9a9c13d367 | arXiv:2603.11564v1 HTML — §C.2 Empirical Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11564v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11564v1.html; sha256:34c5a66de1b92d508d22ad3b4eff82afbf385d69bde5463acb512e9a9c13d367 | arXiv:2603.11564v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.11564v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11564v1.html; sha256:34c5a66de1b92d508d22ad3b4eff82afbf385d69bde5463acb512e9a9c13d367 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11564v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11564 | complete |
| SF-2026-ARXIV-2603-11619 | RP-d00c295854ad9044 | standard | arXiv:2603.11619v1 | SRC-ARXIV@arXiv:2603.11619v1 | arXiv:2603.11619v1 HTML — §2.2. OpenClaw Architecture [facet=method]; https://arxiv.org/html/2603.11619v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11619v1.html; sha256:57f3242d3f157f77ee46984c8444a61a2d2a18b87c6debbd18941716c86621f7 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.11619v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11619v1.html; sha256:57f3242d3f157f77ee46984c8444a61a2d2a18b87c6debbd18941716c86621f7 | arXiv:2603.11619v1 HTML — §5.2. Limitations of Existing Defenses in Guaranteeing OpenClaw Security [facet=limitations]; https://arxiv.org/html/2603.11619v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11619v1.html; sha256:57f3242d3f157f77ee46984c8444a61a2d2a18b87c6debbd18941716c86621f7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11619v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11619 | complete |
| SF-2026-ARXIV-2603-11768 | RP-64f02296edbba1f7 | standard | arXiv:2603.11768v1 | SRC-ARXIV@arXiv:2603.11768v1 | arXiv:2603.11768v1 HTML — §6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda [facet=method]; https://arxiv.org/html/2603.11768v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11768v1.html; sha256:fa263e4f70d9c2fd78885f09cb4c9ffe894e97f5063583efd0fd9ca3fda5aefe | arXiv:2603.11768v1 HTML — §6.3 Testable Research Hypotheses and Evaluation Protocols [facet=evaluation]; https://arxiv.org/html/2603.11768v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11768v1.html; sha256:fa263e4f70d9c2fd78885f09cb4c9ffe894e97f5063583efd0fd9ca3fda5aefe | arXiv:2603.11768v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.11768v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11768v1.html; sha256:fa263e4f70d9c2fd78885f09cb4c9ffe894e97f5063583efd0fd9ca3fda5aefe | arXiv exact-v1 identity https://arxiv.org/abs/2603.11768v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11768 | complete |
| SF-2026-ARXIV-2603-11853 | RP-927d8e561f2477dd | standard | arXiv:2603.11853v1 | SRC-ARXIV@arXiv:2603.11853v1 | arXiv:2603.11853v1 HTML — §3.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.11853v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11853v1.html; sha256:0e2ce58e7724682e968ec31245f3c4464e29d46457e6aa382192a1ec4fa3f8ad | arXiv:2603.11853v1 HTML — §5.5 Preliminary Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.11853v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11853v1.html; sha256:0e2ce58e7724682e968ec31245f3c4464e29d46457e6aa382192a1ec4fa3f8ad | arXiv:2603.11853v1 HTML — §7 Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.11853v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11853v1.html; sha256:0e2ce58e7724682e968ec31245f3c4464e29d46457e6aa382192a1ec4fa3f8ad | arXiv exact-v1 identity https://arxiv.org/abs/2603.11853v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11853 | complete |
| SF-2026-ARXIV-2603-11873 | RP-c0e59fc3074a44b5 | standard | arXiv:2603.11873v1 | SRC-ARXIV@arXiv:2603.11873v1 | arXiv:2603.11873v1 HTML — §Overview [facet=method]; https://arxiv.org/html/2603.11873v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11873v1.html; sha256:0a88b17ad6d744762e84ccd38eb0f1b3b8afaab01f6614a66c198401188045bd | arXiv:2603.11873v1 HTML — §Accuracy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11873v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11873v1.html; sha256:0a88b17ad6d744762e84ccd38eb0f1b3b8afaab01f6614a66c198401188045bd | arXiv:2603.11873v1 HTML — §Conclusion [facet=limitations]; https://arxiv.org/html/2603.11873v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11873v1.html; sha256:0a88b17ad6d744762e84ccd38eb0f1b3b8afaab01f6614a66c198401188045bd | arXiv exact-v1 identity https://arxiv.org/abs/2603.11873v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11873 | complete |
| SF-2026-ARXIV-2603-11875 | RP-e5ba18204443141f | standard | arXiv:2603.11875v1 | SRC-ARXIV@arXiv:2603.11875v1 | arXiv:2603.11875v1 HTML — §3 System Architecture [facet=method]; https://arxiv.org/html/2603.11875v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11875v1.html; sha256:735fdefad2e90ec15f50cd46e4fd3c10b8f3fbd9bad3e3f9957941de14311736 | arXiv:2603.11875v1 HTML — §6 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.11875v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11875v1.html; sha256:735fdefad2e90ec15f50cd46e4fd3c10b8f3fbd9bad3e3f9957941de14311736 | arXiv:2603.11875v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.11875v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11875v1.html; sha256:735fdefad2e90ec15f50cd46e4fd3c10b8f3fbd9bad3e3f9957941de14311736 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11875v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11875 | complete |
| SF-2026-ARXIV-2603-11896 | RP-5a6e0322f4d034c8 | standard | arXiv:2603.11896v1 | SRC-ARXIV@arXiv:2603.11896v1 | arXiv:2603.11896v1 HTML — §4.2 Streaming Architecture [facet=method]; https://arxiv.org/html/2603.11896v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11896v1.html; sha256:19d96bf2c9877d6e6e8146264e1c47a76317e2c91deaceec32c8cb1f35b2158e | arXiv:2603.11896v1 HTML — §5.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11896v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11896v1.html; sha256:19d96bf2c9877d6e6e8146264e1c47a76317e2c91deaceec32c8cb1f35b2158e | arXiv:2603.11896v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.11896v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11896v1.html; sha256:19d96bf2c9877d6e6e8146264e1c47a76317e2c91deaceec32c8cb1f35b2158e | arXiv exact-v1 identity https://arxiv.org/abs/2603.11896v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11896 | complete |
| SF-2026-ARXIV-2603-11935 | RP-c34c9963824f416a | standard | arXiv:2603.11935v1 | SRC-ARXIV@arXiv:2603.11935v1 | arXiv:2603.11935v1 HTML — §4.1 Agent Collaboration Design [facet=method]; https://arxiv.org/html/2603.11935v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11935v1.html; sha256:4048ff35633878191061d38791ead1276850a79ab983d5c27537a4a76a645645 | arXiv:2603.11935v1 HTML — §3.2 Evaluation Pipeline [facet=evaluation]; https://arxiv.org/html/2603.11935v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11935v1.html; sha256:4048ff35633878191061d38791ead1276850a79ab983d5c27537a4a76a645645 | arXiv:2603.11935v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.11935v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11935v1.html; sha256:4048ff35633878191061d38791ead1276850a79ab983d5c27537a4a76a645645 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11935v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11935 | complete |
| SF-2026-ARXIV-2603-11975 | RP-f5e5a86af1764a22 | standard | arXiv:2603.11975v1 | SRC-ARXIV@arXiv:2603.11975v1 | arXiv:2603.11975v1 HTML — §5.1.3 Implementation Details [facet=method]; https://arxiv.org/html/2603.11975v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11975v1.html; sha256:084d829b910434f7c307a29cda6eb773d6b46b0fef2fc038f759315c4b5d4902 | arXiv:2603.11975v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11975v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11975v1.html; sha256:084d829b910434f7c307a29cda6eb773d6b46b0fef2fc038f759315c4b5d4902 | arXiv:2603.11975v1 HTML — §D.3 Case III: Failure by System Latency [facet=limitations]; https://arxiv.org/html/2603.11975v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11975v1.html; sha256:084d829b910434f7c307a29cda6eb773d6b46b0fef2fc038f759315c4b5d4902 | arXiv exact-v1 identity https://arxiv.org/abs/2603.11975v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-11975 | complete |
| SF-2026-ARXIV-2603-12031 | RP-720702fbbace6cfe | standard | arXiv:2603.12031v1 | SRC-ARXIV@arXiv:2603.12031v1 | arXiv:2603.12031v1 HTML — §4 System Design [facet=method]; https://arxiv.org/html/2603.12031v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12031v1.html; sha256:60092a95c1aebdf50a54880841678a06bfc5618c1b7ac8db156bcd67be5955df | arXiv:2603.12031v1 HTML — §6 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12031v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12031v1.html; sha256:60092a95c1aebdf50a54880841678a06bfc5618c1b7ac8db156bcd67be5955df | arXiv:2603.12031v1 HTML — §7 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.12031v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12031v1.html; sha256:60092a95c1aebdf50a54880841678a06bfc5618c1b7ac8db156bcd67be5955df | arXiv exact-v1 identity https://arxiv.org/abs/2603.12031v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12031 | complete |
| SF-2026-ARXIV-2603-12038 | RP-879be74ed5f19c22 | standard | arXiv:2603.12038v1 | SRC-ARXIV@arXiv:2603.12038v1 | arXiv:2603.12038v1 HTML — §System Design and Kernel Optimization [facet=method]; https://arxiv.org/html/2603.12038v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12038v1.html; sha256:d1ffc2638384857b08d207dac8d44d2b7979ba77c243c6463eeabbf6c47a0525 | arXiv:2603.12038v1 HTML — §Experiments [facet=evaluation]; https://arxiv.org/html/2603.12038v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12038v1.html; sha256:d1ffc2638384857b08d207dac8d44d2b7979ba77c243c6463eeabbf6c47a0525 | arXiv:2603.12038v1 HTML — §Algorithm discussion. [facet=limitations]; https://arxiv.org/html/2603.12038v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12038v1.html; sha256:d1ffc2638384857b08d207dac8d44d2b7979ba77c243c6463eeabbf6c47a0525 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12038v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12038 | complete |
| SF-2026-ARXIV-2603-12056 | RP-bedae15c697bf978 | standard | arXiv:2603.12056v1 | SRC-ARXIV@arXiv:2603.12056v1 | arXiv:2603.12056v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.12056v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12056v1.html; sha256:eed286984161303f6e6ae5b0b515132afd1856a63c6a10691afac921f67bf20a | arXiv:2603.12056v1 HTML — §3.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.12056v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12056v1.html; sha256:eed286984161303f6e6ae5b0b515132afd1856a63c6a10691afac921f67bf20a | arXiv:2603.12056v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12056v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12056v1.html; sha256:eed286984161303f6e6ae5b0b515132afd1856a63c6a10691afac921f67bf20a | arXiv exact-v1 identity https://arxiv.org/abs/2603.12056v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12056 | complete |
| SF-2026-ARXIV-2603-12118 | RP-11db260130bcb988 | deep | arXiv:2603.12118v1 | SRC-ARXIV@arXiv:2603.12118v1 | arXiv:2603.12118v1 HTML — §2.1. Architecture Overview [facet=method]; https://arxiv.org/html/2603.12118v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12118v1.html; sha256:8e0992c40f3f18d1c84bfeffd9b88f9461ad9373068403056b16b3e52bf3c241 | arXiv:2603.12118v1 HTML — §3. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12118v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12118v1.html; sha256:8e0992c40f3f18d1c84bfeffd9b88f9461ad9373068403056b16b3e52bf3c241 | arXiv:2603.12118v1 HTML — §4. Conclusion [facet=limitations]; https://arxiv.org/html/2603.12118v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12118v1.html; sha256:8e0992c40f3f18d1c84bfeffd9b88f9461ad9373068403056b16b3e52bf3c241 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12118v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12118 | complete |
| SF-2026-ARXIV-2603-12201 | RP-c83cd1b58f6f7adf | standard | arXiv:2603.12201v1 | SRC-ARXIV@arXiv:2603.12201v1 | arXiv:2603.12201v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.12201v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12201v1.html; sha256:83cc704501eaf36f8f739f72d3e31c824caa50889c7e28e294a0862a1487f163 | arXiv:2603.12201v1 HTML — §4.3 Training-Free IndexCache Results [facet=evaluation]; https://arxiv.org/html/2603.12201v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12201v1.html; sha256:83cc704501eaf36f8f739f72d3e31c824caa50889c7e28e294a0862a1487f163 | arXiv:2603.12201v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12201v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12201v1.html; sha256:83cc704501eaf36f8f739f72d3e31c824caa50889c7e28e294a0862a1487f163 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12201v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12201 | complete |
| SF-2026-ARXIV-2603-12230 | RP-a8b7474b1bbf07d8 | standard | arXiv:2603.12230v1 | SRC-ARXIV@arXiv:2603.12230v1 | arXiv:2603.12230v1 HTML — §1.3 Agent Architecture, Deployment and Hosting [facet=method]; https://arxiv.org/html/2603.12230v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12230v1.html; sha256:b394e1a40b494abc6ae6efb52a0c04fcfc44e4dcbbc4ec69306c05f97f68d263 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12230v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12230v1.html; sha256:b394e1a40b494abc6ae6efb52a0c04fcfc44e4dcbbc4ec69306c05f97f68d263 | arXiv:2603.12230v1 HTML — §4 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12230v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12230v1.html; sha256:b394e1a40b494abc6ae6efb52a0c04fcfc44e4dcbbc4ec69306c05f97f68d263 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12230v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12230 | complete |
| SF-2026-ARXIV-2603-12255 | RP-4827d2fd5f034cd6 | standard | arXiv:2603.12255v1 | SRC-ARXIV@arXiv:2603.12255v1 | arXiv:2603.12255v1 HTML — §3.2 Overall Framework [facet=method]; https://arxiv.org/html/2603.12255v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12255v1.html; sha256:8e19b1b834aa69d1cba5220ad5dd113db1b178a67a1feddd593edf62849b6288 | arXiv:2603.12255v1 HTML — §4.4 Ablation Study and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12255v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12255v1.html; sha256:8e19b1b834aa69d1cba5220ad5dd113db1b178a67a1feddd593edf62849b6288 | arXiv:2603.12255v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12255v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12255v1.html; sha256:8e19b1b834aa69d1cba5220ad5dd113db1b178a67a1feddd593edf62849b6288 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12255v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12255 | complete |
| SF-2026-ARXIV-2603-12262 | RP-3979de435f87a8a8 | standard | arXiv:2603.12262v1 | SRC-ARXIV@arXiv:2603.12262v1 | arXiv:2603.12262v1 HTML — §2.2 Training Method for VST [facet=method]; https://arxiv.org/html/2603.12262v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12262v1.html; sha256:dbcee7a4450506878a8ddac91bde21819034a3a085a42a3676723c20fa5d2f4d | arXiv:2603.12262v1 HTML — §3.3 Online Video Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.12262v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12262v1.html; sha256:dbcee7a4450506878a8ddac91bde21819034a3a085a42a3676723c20fa5d2f4d | arXiv:2603.12262v1 HTML — §Limitation and Future Works. [facet=limitations]; https://arxiv.org/html/2603.12262v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12262v1.html; sha256:dbcee7a4450506878a8ddac91bde21819034a3a085a42a3676723c20fa5d2f4d | arXiv exact-v1 identity https://arxiv.org/abs/2603.12262v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12262 | complete |

### Source Reviews

### Speculative Decoding Scaling Laws (SDSL): Throughput Optimization Made Simple

<!-- review:SF-2026-ARXIV-2603-11053:start -->
**问题**：`Speculative Decoding Scaling Laws (SDSL): Throughput Optimization Made Simple` 检查的是 `INFER-SPECULATIVE-DECODING` 中 decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。 是否会改变现有设计边界。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：exact-v1 的 `5.1 Motivation and Numerical Approximation Methodology` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.11053v1 HTML — §5.1 Motivation and Numerical Approximation Methodology [facet=method]; https://arxiv.org/html/2603.11053v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11053v1.html; sha256:061e695127e2cbae381421b985b83b83a577d95c374ea48f8ff284b7ead0d1e5`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Results and validation.`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11053v1 HTML — §Results and validation. [facet=evaluation]; https://arxiv.org/html/2603.11053v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11053v1.html; sha256:061e695127e2cbae381421b985b83b83a577d95c374ea48f8ff284b7ead0d1e5`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Limitations`。接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2603-11053:start -->**Claim Boundary**：只支持 arXiv:2603.11053v1 §5.1 Motivation and Numerical Approximation Methodology 的机制与 §Results and validation. 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11053:end -->
<!-- review:SF-2026-ARXIV-2603-11053:end -->
### The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey

<!-- review:SF-2026-ARXIV-2603-11088:start -->
**问题**：`The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `4.4. Attack Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11088v1 HTML — §4.4. Attack Methods [facet=method]; https://arxiv.org/html/2603.11088v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11088v1.html; sha256:a4377324e268ba95cf1dbdacb8644dfc36bae3049642218da9ccc5163e948dc4`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2.5. Human-In-The-Loop Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11088v1 HTML — §5.2.5. Human-In-The-Loop Validation [facet=evaluation]; https://arxiv.org/html/2603.11088v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11088v1.html; sha256:a4377324e268ba95cf1dbdacb8644dfc36bae3049642218da9ccc5163e948dc4`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8. Conclusion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11088:start -->**Claim Boundary**：只支持 arXiv:2603.11088v1 §4.4. Attack Methods 的机制与 §5.2.5. Human-In-The-Loop Validation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11088:end -->
<!-- review:SF-2026-ARXIV-2603-11088:end -->
### Thousand-GPU Large-Scale Training and Optimization Recipe for AI-Native Cloud Embodied Intelligence Infrastructure

<!-- review:SF-2026-ARXIV-2603-11101:start -->
**问题**：`Thousand-GPU Large-Scale Training and Optimization Recipe for AI-Native Cloud Embodied Intelligence Infrastructure` 检查的是 `TRAIN-DISTRIBUTED-TRAINING` 中 参数、optimizer state 和通信规模越过单设备边界。 是否会改变现有设计边界。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：exact-v1 的 `2.1 Overall Architecture Design` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.11101v1 HTML — §2.1 Overall Architecture Design [facet=method]; https://arxiv.org/html/2603.11101v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11101v1.html; sha256:2b44ad55ba20d6134493ef4fa04d43d90d07a9b09649f7fd6f13f686b6f6819b`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.1 Thousand-GPU Scale Framework Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11101v1 HTML — §3.1 Thousand-GPU Scale Framework Validation [facet=evaluation]; https://arxiv.org/html/2603.11101v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11101v1.html; sha256:2b44ad55ba20d6134493ef4fa04d43d90d07a9b09649f7fd6f13f686b6f6819b`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4 Conclusion and Future Outlook`。模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2603-11101:start -->**Claim Boundary**：只支持 arXiv:2603.11101v1 §2.1 Overall Architecture Design 的机制与 §3.1 Thousand-GPU Scale Framework Validation 的公开 workload；§4 Conclusion and Future Outlook 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11101:end -->
<!-- review:SF-2026-ARXIV-2603-11101:end -->
### WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference

<!-- review:SF-2026-ARXIV-2603-11132:start -->
**问题**：`WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3.1 Threat Models` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11132v1 HTML — §3.1 Threat Models [facet=method]; https://arxiv.org/html/2603.11132v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11132v1.html; sha256:ed02ca48aad4bcd6f5108fed3776631469e8211d65b9811f77180bb6fa2d1b5f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11132v1 HTML — §4.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11132v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11132v1.html; sha256:ed02ca48aad4bcd6f5108fed3776631469e8211d65b9811f77180bb6fa2d1b5f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11132:start -->**Claim Boundary**：只支持 arXiv:2603.11132v1 §3.1 Threat Models 的机制与 §4.1 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11132:end -->
<!-- review:SF-2026-ARXIV-2603-11132:end -->
### Security-by-Design for LLM-Based Code Generation: Leveraging Internal Representations for Concept-Driven Steering Mechanisms

<!-- review:SF-2026-ARXIV-2603-11212:start -->
**问题**：`Security-by-Design for LLM-Based Code Generation: Leveraging Internal Representations for Concept-Driven Steering Mechanisms` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `V-A Datasets and Baseline Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11212v1 HTML — §V-A Datasets and Baseline Methods [facet=method]; https://arxiv.org/html/2603.11212v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11212v1.html; sha256:7f68d5d17ee4ea71ad0144ba63af4a155a47011389df76e24b2963bbfea946b1`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V Comparative Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11212v1 HTML — §V Comparative Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11212v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11212v1.html; sha256:7f68d5d17ee4ea71ad0144ba63af4a155a47011389df76e24b2963bbfea946b1`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VI Discussion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11212:start -->**Claim Boundary**：只支持 arXiv:2603.11212v1 §V-A Datasets and Baseline Methods 的机制与 §V Comparative Evaluation 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11212:end -->
<!-- review:SF-2026-ARXIV-2603-11212:end -->
### Duration Aware Scheduling for ASR Serving Under Workload Drift

<!-- review:SF-2026-ARXIV-2603-11273:start -->
**问题**：`Duration Aware Scheduling for ASR Serving Under Workload Drift` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `3 Methodology` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.11273v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.11273v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11273v1.html; sha256:ed607304032ba48bc06d5aa30e3d777867bfa9f0518d7f027ab9ec0016636e81`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation Metrics.`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11273v1 HTML — §Evaluation Metrics. [facet=evaluation]; https://arxiv.org/html/2603.11273v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11273v1.html; sha256:ed607304032ba48bc06d5aa30e3d777867bfa9f0518d7f027ab9ec0016636e81`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-11273:start -->**Claim Boundary**：只支持 arXiv:2603.11273v1 §3 Methodology 的机制与 §Evaluation Metrics. 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11273:end -->
<!-- review:SF-2026-ARXIV-2603-11273:end -->
### Synthesis-in-the-Loop Evaluation of LLMs for RTL Generation: Quality, Reliability, and Failure Modes

<!-- review:SF-2026-ARXIV-2603-11287:start -->
**问题**：`Synthesis-in-the-Loop Evaluation of LLMs for RTL Generation: Quality, Reliability, and Failure Modes` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `Pass rate versus implementation quality.` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.11287v1 HTML — §Pass rate versus implementation quality. [facet=method]; https://arxiv.org/html/2603.11287v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11287v1.html; sha256:256bb91f0d11616be63a5dd0fed92184e473d572082822f0272445e525db4c08`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.2. Evaluation Pipeline`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11287v1 HTML — §3.2. Evaluation Pipeline [facet=evaluation]; https://arxiv.org/html/2603.11287v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11287v1.html; sha256:256bb91f0d11616be63a5dd0fed92184e473d572082822f0272445e525db4c08`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations and future work.`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-11287:start -->**Claim Boundary**：只支持 arXiv:2603.11287v1 §Pass rate versus implementation quality. 的机制与 §3.2. Evaluation Pipeline 的公开 workload；§Limitations and future work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11287:end -->
<!-- review:SF-2026-ARXIV-2603-11287:end -->
### RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents

<!-- review:SF-2026-ARXIV-2603-11337:start -->
**问题**：`RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `V Experimental Design` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.11337v1 HTML — §V Experimental Design [facet=method]; https://arxiv.org/html/2603.11337v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11337v1.html; sha256:516c6ea497eb225fa74bb6c8557ac584490e862b49acf5f23bf4620e0bcffe6f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `VI Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11337v1 HTML — §VI Results [facet=evaluation]; https://arxiv.org/html/2603.11337v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11337v1.html; sha256:516c6ea497eb225fa74bb6c8557ac584490e862b49acf5f23bf4620e0bcffe6f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VII Discussion and Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-11337:start -->**Claim Boundary**：只支持 arXiv:2603.11337v1 §V Experimental Design 的机制与 §VI Results 的公开 workload；§VII Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11337:end -->
<!-- review:SF-2026-ARXIV-2603-11337:end -->
### Improving LLM Performance Through Black-Box Online Tuning: A Case for Adding System Specs to Factsheets for Trusted AI

<!-- review:SF-2026-ARXIV-2603-11340:start -->
**问题**：缺少内部指标的托管 serving 仍需在 workload 漂移下调参，离线固定配置无法最大化 SLO goodput。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：黑盒 controller 只使用短窗口端到端观测，以 hill climbing 更新配置，并把系统规格纳入 factsheet。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.11340v1 HTML — §II-B SLO-Tuner system design [facet=method]; https://arxiv.org/html/2603.11340v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11340v1.html; sha256:1164eb8ff6859ccacb63e3ec30db5ca8b71510f24d2b6bdfdfb3307570389ab5`。

**Evaluation contract 与未证明部分**：作者测量只证明给定参数空间和负载中的局部调优；不证明无状态 hill climbing 避免所有振荡。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11340v1 HTML — §II-C Results [facet=evaluation]; https://arxiv.org/html/2603.11340v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11340v1.html; sha256:1164eb8ff6859ccacb63e3ec30db5ca8b71510f24d2b6bdfdfb3307570389ab5`。

**Trade-off / failure / coexistence**：在线探索可能伤害 SLO，且 factsheet 会随版本过期；稳定服务仍应冻结经过压测的配置。

<!-- claim:SF-2026-ARXIV-2603-11340:start -->**Claim Boundary**：只支持 arXiv:2603.11340v1 §II-B SLO-Tuner system design 的机制与 §II-C Results 的公开 workload；§III Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11340:end -->
<!-- review:SF-2026-ARXIV-2603-11340:end -->
### NCCLbpf: Verified, Composable Policy Execution for GPU Collective Communication

<!-- review:SF-2026-ARXIV-2603-11438:start -->
**问题**：GPU collective 的策略若只存在于动态 hook 或运维脚本，执行顺序和安全边界难以复算。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：NCCLbpf 将通信策略编译为受限、可组合且可验证的执行单元，在 collective 边界检查并应用调度/传输决定。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.11438v1 HTML — §3.3. Architecture [facet=method]; https://arxiv.org/html/2603.11438v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11438v1.html; sha256:0e97e9e1eb1a293a5a0f96f233dacd104852d736d57354c80c849b8129fbf518`。

**Evaluation contract 与未证明部分**：§5.1 测量 CPU/GPU overhead，§5.2 验证 verifier rejection 与 hot reload，§5.3 给出 policy case studies。Verifier acceptance 只约束 memory/control safety；memory-safe 的坏策略仍可能通过并严重降低吞吐，仍需 operator/性能验证。

**Trade-off / failure / coexistence**：可验证策略减少不可控扩展，却限制表达能力并增加 verifier/ABI 兼容责任；固定拓扑仍可采用静态 NCCL 配置。

<!-- claim:SF-2026-ARXIV-2603-11438:start -->**Claim Boundary**：只支持 arXiv:2603.11438v1 §3.3 的受限 policy runtime 与 §5.1–§5.3 的公开评测；verifier 不证明语义/性能安全，§7 之外不外推。<!-- claim:SF-2026-ARXIV-2603-11438:end -->
<!-- review:SF-2026-ARXIV-2603-11438:end -->
### Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution

<!-- review:SF-2026-ARXIV-2603-11445:start -->
**问题**：`Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution` 检查的是 `AGENT-MULTI-AGENT` 中 任务并行、能力异质和跨信任域协作迫使系统显式管理委托与共享状态。 是否会改变现有设计边界。

**旧路径为何合理**：单 agent 持有完整上下文和控制流，规模小时最容易归因。

**约束变化与机制**：exact-v1 的 `4 Implementation` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 agent identity、委托边、消息状态、协作协议与冲突处理；定位证据为 `arXiv:2603.11445v1 HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.11445v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11445v1.html; sha256:1532303b2d73c947ea37f054541cd41ac4e69259a7bdeb1f047f8f70e6cd5fdd`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.3 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11445v1 HTML — §5.3 Results [facet=evaluation]; https://arxiv.org/html/2603.11445v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11445v1.html; sha256:1532303b2d73c947ea37f054541cd41ac4e69259a7bdeb1f047f8f70e6cd5fdd`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Discussion`。任务短且角色不需要隔离时，单 agent 仍有更低协调成本。

<!-- claim:SF-2026-ARXIV-2603-11445:start -->**Claim Boundary**：只支持 arXiv:2603.11445v1 §4 Implementation 的机制与 §5.3 Results 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11445:end -->
<!-- review:SF-2026-ARXIV-2603-11445:end -->
### LongFlow: Efficient KV Cache Compression for Reasoning Models

<!-- review:SF-2026-ARXIV-2603-11504:start -->
**问题**：`LongFlow: Efficient KV Cache Compression for Reasoning Models` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `3.1 A Lightweight Design Philosophy` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.11504v1 HTML — §3.1 A Lightweight Design Philosophy [facet=method]; https://arxiv.org/html/2603.11504v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11504v1.html; sha256:17e497d769bcec912da606d8647a2454a48456d3b4f7a478bf8ea96bef79e707`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Results on Model Accuracy`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11504v1 HTML — §4.2 Main Results on Model Accuracy [facet=evaluation]; https://arxiv.org/html/2603.11504v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11504v1.html; sha256:17e497d769bcec912da606d8647a2454a48456d3b4f7a478bf8ea96bef79e707`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-11504:start -->**Claim Boundary**：只支持 arXiv:2603.11504v1 §3.1 A Lightweight Design Philosophy 的机制与 §4.2 Main Results on Model Accuracy 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11504:end -->
<!-- review:SF-2026-ARXIV-2603-11504:end -->
### Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing

<!-- review:SF-2026-ARXIV-2603-11535:start -->
**问题**：top-k token-choice 路由固定每 token 计算并依赖跨 batch load-balance loss，难支持因 token 变化的动态容量。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：Expert Threshold 让每个 expert 维护全局分布 EMA threshold，独立决定接收 token，保持 causal routing。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.11535v1 HTML — §Appendix B Architecture Details [facet=method]; https://arxiv.org/html/2603.11535v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11535v1.html; sha256:b10f8e3c824ecf10a2e0a314dcf04c899cc613cff5901d3b43a99cb18ace569d`。

**Evaluation contract 与未证明部分**：2.4B 预训练结果支持该规模/数据中的 loss 与 balance；不证明超大 MoE 的 all-to-all 尾延迟。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11535v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11535v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11535v1.html; sha256:b10f8e3c824ecf10a2e0a314dcf04c899cc613cff5901d3b43a99cb18ace569d`。

**Trade-off / failure / coexistence**：动态 expert 数提高适配性，却让每 token compute 和 capacity 更难预测；硬 SLO 下固定 top-k 更可控。

<!-- claim:SF-2026-ARXIV-2603-11535:start -->**Claim Boundary**：只支持 arXiv:2603.11535v1 §Appendix B Architecture Details 的机制与 §4.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11535:end -->
<!-- review:SF-2026-ARXIV-2603-11535:end -->
### Feedback-Coupled Memory Systems: A Dynamical Model for Adaptive Coordination

<!-- review:SF-2026-ARXIV-2603-11560:start -->
**问题**：`Feedback-Coupled Memory Systems: A Dynamical Model for Adaptive Coordination` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `2 The Structural Architecture of Coordination` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.11560v1 HTML — §2 The Structural Architecture of Coordination [facet=method]; https://arxiv.org/html/2603.11560v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11560v1.html; sha256:3f49d5b371e93bfb4a989bd1fe016ee28a08027a0e917cfe194367964c892818`。

**Evaluation contract 与未证明部分**：公开验证定位在 `How Intelligence Emerges: A Minimal Theory of Dynamic Adaptive Coordination`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11560v1 HTML — §How Intelligence Emerges: A Minimal Theory of Dynamic Adaptive Coordination [facet=evaluation]; https://arxiv.org/html/2603.11560v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11560v1.html; sha256:3f49d5b371e93bfb4a989bd1fe016ee28a08027a0e917cfe194367964c892818`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-11560:start -->**Claim Boundary**：只支持 arXiv:2603.11560v1 §2 The Structural Architecture of Coordination 的机制与 §How Intelligence Emerges: A Minimal Theory of Dynamic Adaptive Coordination 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11560:end -->
<!-- review:SF-2026-ARXIV-2603-11560:end -->
### Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries

<!-- review:SF-2026-ARXIV-2603-11564:start -->
**问题**：`Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `4 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.11564v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.11564v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11564v1.html; sha256:34c5a66de1b92d508d22ad3b4eff82afbf385d69bde5463acb512e9a9c13d367`。

**Evaluation contract 与未证明部分**：公开验证定位在 `C.2 Empirical Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11564v1 HTML — §C.2 Empirical Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11564v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11564v1.html; sha256:34c5a66de1b92d508d22ad3b4eff82afbf385d69bde5463acb512e9a9c13d367`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-11564:start -->**Claim Boundary**：只支持 arXiv:2603.11564v1 §4 Method 的机制与 §C.2 Empirical Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11564:end -->
<!-- review:SF-2026-ARXIV-2603-11564:end -->
### Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats

<!-- review:SF-2026-ARXIV-2603-11619:start -->
**问题**：`Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `2.2. OpenClaw Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11619v1 HTML — §2.2. OpenClaw Architecture [facet=method]; https://arxiv.org/html/2603.11619v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11619v1.html; sha256:57f3242d3f157f77ee46984c8444a61a2d2a18b87c6debbd18941716c86621f7`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.11619v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11619v1.html; sha256:57f3242d3f157f77ee46984c8444a61a2d2a18b87c6debbd18941716c86621f7`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5.2. Limitations of Existing Defenses in Guaranteeing OpenClaw Security`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11619:start -->**Claim Boundary**：只支持 arXiv:2603.11619v1 §2.2. OpenClaw Architecture 的机制与 §Evaluation 的公开 workload；§5.2. Limitations of Existing Defenses in Guaranteeing OpenClaw Security 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11619:end -->
<!-- review:SF-2026-ARXIV-2603-11619:end -->
### Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework

<!-- review:SF-2026-ARXIV-2603-11768:start -->
**问题**：`Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.11768v1 HTML — §6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda [facet=method]; https://arxiv.org/html/2603.11768v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11768v1.html; sha256:fa263e4f70d9c2fd78885f09cb4c9ffe894e97f5063583efd0fd9ca3fda5aefe`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.3 Testable Research Hypotheses and Evaluation Protocols`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11768v1 HTML — §6.3 Testable Research Hypotheses and Evaluation Protocols [facet=evaluation]; https://arxiv.org/html/2603.11768v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11768v1.html; sha256:fa263e4f70d9c2fd78885f09cb4c9ffe894e97f5063583efd0fd9ca3fda5aefe`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-11768:start -->**Claim Boundary**：只支持 arXiv:2603.11768v1 §6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda 的机制与 §6.3 Testable Research Hypotheses and Evaluation Protocols 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11768:end -->
<!-- review:SF-2026-ARXIV-2603-11768:end -->
### OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents

<!-- review:SF-2026-ARXIV-2603-11853:start -->
**问题**：`OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3.1 Architecture Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11853v1 HTML — §3.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.11853v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11853v1.html; sha256:0e2ce58e7724682e968ec31245f3c4464e29d46457e6aa382192a1ec4fa3f8ad`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.5 Preliminary Benchmark Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11853v1 HTML — §5.5 Preliminary Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.11853v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11853v1.html; sha256:0e2ce58e7724682e968ec31245f3c4464e29d46457e6aa382192a1ec4fa3f8ad`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Discussion and Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11853:start -->**Claim Boundary**：只支持 arXiv:2603.11853v1 §3.1 Architecture Overview 的机制与 §5.5 Preliminary Benchmark Results 的公开 workload；§7 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11853:end -->
<!-- review:SF-2026-ARXIV-2603-11853:end -->
### AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization

<!-- review:SF-2026-ARXIV-2603-11873:start -->
**问题**：`AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `Overview` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.11873v1 HTML — §Overview [facet=method]; https://arxiv.org/html/2603.11873v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11873v1.html; sha256:0a88b17ad6d744762e84ccd38eb0f1b3b8afaab01f6614a66c198401188045bd`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Accuracy Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11873v1 HTML — §Accuracy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.11873v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11873v1.html; sha256:0a88b17ad6d744762e84ccd38eb0f1b3b8afaab01f6614a66c198401188045bd`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Conclusion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-11873:start -->**Claim Boundary**：只支持 arXiv:2603.11873v1 §Overview 的机制与 §Accuracy Evaluation 的公开 workload；§Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11873:end -->
<!-- review:SF-2026-ARXIV-2603-11873:end -->
### The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection

<!-- review:SF-2026-ARXIV-2603-11875:start -->
**问题**：`The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3 System Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.11875v1 HTML — §3 System Architecture [facet=method]; https://arxiv.org/html/2603.11875v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11875v1.html; sha256:735fdefad2e90ec15f50cd46e4fd3c10b8f3fbd9bad3e3f9957941de14311736`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Experimental Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11875v1 HTML — §6 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.11875v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11875v1.html; sha256:735fdefad2e90ec15f50cd46e4fd3c10b8f3fbd9bad3e3f9957941de14311736`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-11875:start -->**Claim Boundary**：只支持 arXiv:2603.11875v1 §3 System Architecture 的机制与 §6 Experimental Results 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11875:end -->
<!-- review:SF-2026-ARXIV-2603-11875:end -->
### Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models

<!-- review:SF-2026-ARXIV-2603-11896:start -->
**问题**：`Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `4.2 Streaming Architecture` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.11896v1 HTML — §4.2 Streaming Architecture [facet=method]; https://arxiv.org/html/2603.11896v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11896v1.html; sha256:19d96bf2c9877d6e6e8146264e1c47a76317e2c91deaceec32c8cb1f35b2158e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.4 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11896v1 HTML — §5.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11896v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11896v1.html; sha256:19d96bf2c9877d6e6e8146264e1c47a76317e2c91deaceec32c8cb1f35b2158e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-11896:start -->**Claim Boundary**：只支持 arXiv:2603.11896v1 §4.2 Streaming Architecture 的机制与 §5.4 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11896:end -->
<!-- review:SF-2026-ARXIV-2603-11896:end -->
### MobileKernelBench: Can LLMs Write Efficient Kernels for Mobile Devices?

<!-- review:SF-2026-ARXIV-2603-11935:start -->
**问题**：`MobileKernelBench: Can LLMs Write Efficient Kernels for Mobile Devices?` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `4.1 Agent Collaboration Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.11935v1 HTML — §4.1 Agent Collaboration Design [facet=method]; https://arxiv.org/html/2603.11935v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11935v1.html; sha256:4048ff35633878191061d38791ead1276850a79ab983d5c27537a4a76a645645`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.2 Evaluation Pipeline`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11935v1 HTML — §3.2 Evaluation Pipeline [facet=evaluation]; https://arxiv.org/html/2603.11935v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11935v1.html; sha256:4048ff35633878191061d38791ead1276850a79ab983d5c27537a4a76a645645`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-11935:start -->**Claim Boundary**：只支持 arXiv:2603.11935v1 §4.1 Agent Collaboration Design 的机制与 §3.2 Evaluation Pipeline 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11935:end -->
<!-- review:SF-2026-ARXIV-2603-11935:end -->
### HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios

<!-- review:SF-2026-ARXIV-2603-11975:start -->
**问题**：`HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `5.1.3 Implementation Details` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.11975v1 HTML — §5.1.3 Implementation Details [facet=method]; https://arxiv.org/html/2603.11975v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11975v1.html; sha256:084d829b910434f7c307a29cda6eb773d6b46b0fef2fc038f759315c4b5d4902`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.11975v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.11975v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.11975v1.html; sha256:084d829b910434f7c307a29cda6eb773d6b46b0fef2fc038f759315c4b5d4902`。

**Trade-off / failure / coexistence**：限制与反证定位在 `D.3 Case III: Failure by System Latency`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-11975:start -->**Claim Boundary**：只支持 arXiv:2603.11975v1 §5.1.3 Implementation Details 的机制与 §5.2 Main Results 的公开 workload；§D.3 Case III: Failure by System Latency 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-11975:end -->
<!-- review:SF-2026-ARXIV-2603-11975:end -->
### Agentic-Kube: A Graph-Enhanced Multi-Agent Reinforcement Learning Framework for Multi-Objective Kubernetes Scheduling

<!-- review:SF-2026-ARXIV-2603-12031:start -->
**问题**：`Agentic-Kube: A Graph-Enhanced Multi-Agent Reinforcement Learning Framework for Multi-Objective Kubernetes Scheduling` 检查的是 `PLATFORM-GPU-SCHEDULER` 中 并发 workload 与成本压力要求共享，同时又不能破坏确定性。 是否会改变现有设计边界。

**旧路径为何合理**：独占 GPU 提供最清晰的隔离和性能归因。

**约束变化与机制**：exact-v1 的 `4 System Design` 把论文方案定位到 GPU slice、隔离、配额与抢占控制；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-GPU-SCHEDULER` 负责 GPU slice、隔离、配额与抢占控制；定位证据为 `arXiv:2603.12031v1 HTML — §4 System Design [facet=method]; https://arxiv.org/html/2603.12031v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12031v1.html; sha256:60092a95c1aebdf50a54880841678a06bfc5618c1b7ac8db156bcd67be5955df`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Experimental Results and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12031v1 HTML — §6 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12031v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12031v1.html; sha256:60092a95c1aebdf50a54880841678a06bfc5618c1b7ac8db156bcd67be5955df`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion and Future Work`。高风险或稳定满载任务仍宜独占。

<!-- claim:SF-2026-ARXIV-2603-12031:start -->**Claim Boundary**：只支持 arXiv:2603.12031v1 §4 System Design 的机制与 §6 Experimental Results and Analysis 的公开 workload；§7 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12031:end -->
<!-- review:SF-2026-ARXIV-2603-12031:end -->
### Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability

<!-- review:SF-2026-ARXIV-2603-12038:start -->
**问题**：`Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `System Design and Kernel Optimization` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.12038v1 HTML — §System Design and Kernel Optimization [facet=method]; https://arxiv.org/html/2603.12038v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12038v1.html; sha256:d1ffc2638384857b08d207dac8d44d2b7979ba77c243c6463eeabbf6c47a0525`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12038v1 HTML — §Experiments [facet=evaluation]; https://arxiv.org/html/2603.12038v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12038v1.html; sha256:d1ffc2638384857b08d207dac8d44d2b7979ba77c243c6463eeabbf6c47a0525`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Algorithm discussion.`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-12038:start -->**Claim Boundary**：只支持 arXiv:2603.12038v1 §System Design and Kernel Optimization 的机制与 §Experiments 的公开 workload；§Algorithm discussion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12038:end -->
<!-- review:SF-2026-ARXIV-2603-12038:end -->
### XSkill: Continual Learning from Experience and Skills in Multimodal Agents

<!-- review:SF-2026-ARXIV-2603-12056:start -->
**问题**：`XSkill: Continual Learning from Experience and Skills in Multimodal Agents` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `2 Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.12056v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.12056v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12056v1.html; sha256:eed286984161303f6e6ae5b0b515132afd1856a63c6a10691afac921f67bf20a`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12056v1 HTML — §3.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.12056v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12056v1.html; sha256:eed286984161303f6e6ae5b0b515132afd1856a63c6a10691afac921f67bf20a`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-12056:start -->**Claim Boundary**：只支持 arXiv:2603.12056v1 §2 Methodology 的机制与 §3.2 Main Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12056:end -->
<!-- review:SF-2026-ARXIV-2603-12056:end -->
### Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models

<!-- review:SF-2026-ARXIV-2603-12118:start -->
**问题**：any-to-any 多模态模型包含编码、跨模态变换与解码 DAG，沿用文本 LLM 的单 token 队列会让中间张量和阶段资源失配。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Cornserve 将 deployment/replicas、invocation routing、intermediate-tensor transfer/completion 与 execution/batching 分别交给 Resource/Task Managers、Dispatcher、per-GPU Sidecars 和 Executors。

**State / data / control owner**：`INFER-SCHEDULING` 负责跨组件资源与路由合同，但控制面、传输 sidecar 和 executor 保持独立 owner；定位于 exact-v1 §2.1–§2.2。

**Evaluation contract 与未证明部分**：§3 支持所测 DAG 的端到端收益；record/replay 要求请求 path deterministic，data-dependent control flow 必须由 application 用真实结果处理。

**Trade-off / failure / coexistence**：DAG-aware serving 提高异质资源利用率，但扩大状态 identity、故障恢复和跨阶段 backpressure 的复杂度；纯文本路径仍适合专用 engine。

<!-- claim:SF-2026-ARXIV-2603-12118:start -->**Claim Boundary**：只支持 arXiv:2603.12118v1 §2.1–§2.2 的分层 ownership 与 deterministic record/replay，以及 §3 的公开 workload；动态控制流留在 application 层。<!-- claim:SF-2026-ARXIV-2603-12118:end -->
<!-- review:SF-2026-ARXIV-2603-12118:end -->
### IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse

<!-- review:SF-2026-ARXIV-2603-12201:start -->
**问题**：`IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `3 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.12201v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.12201v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12201v1.html; sha256:83cc704501eaf36f8f739f72d3e31c824caa50889c7e28e294a0862a1487f163`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.3 Training-Free IndexCache Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12201v1 HTML — §4.3 Training-Free IndexCache Results [facet=evaluation]; https://arxiv.org/html/2603.12201v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12201v1.html; sha256:83cc704501eaf36f8f739f72d3e31c824caa50889c7e28e294a0862a1487f163`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-12201:start -->**Claim Boundary**：只支持 arXiv:2603.12201v1 §3 Method 的机制与 §4.3 Training-Free IndexCache Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12201:end -->
<!-- review:SF-2026-ARXIV-2603-12201:end -->
### Security Considerations for Artificial Intelligence Agents

<!-- review:SF-2026-ARXIV-2603-12230:start -->
**问题**：`Security Considerations for Artificial Intelligence Agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `1.3 Agent Architecture, Deployment and Hosting` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12230v1 HTML — §1.3 Agent Architecture, Deployment and Hosting [facet=method]; https://arxiv.org/html/2603.12230v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12230v1.html; sha256:b394e1a40b494abc6ae6efb52a0c04fcfc44e4dcbbc4ec69306c05f97f68d263`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12230v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12230v1.html; sha256:b394e1a40b494abc6ae6efb52a0c04fcfc44e4dcbbc4ec69306c05f97f68d263`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4 Conclusion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12230:start -->**Claim Boundary**：只支持 arXiv:2603.12230v1 §1.3 Agent Architecture, Deployment and Hosting 的机制与 §Evaluation 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12230:end -->
<!-- review:SF-2026-ARXIV-2603-12230:end -->
### Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training

<!-- review:SF-2026-ARXIV-2603-12255:start -->
**问题**：`Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training` 检查的是 `MULTIMODAL-REPRESENTATION` 中 流式、多轮和跨模态任务要求表示保留时间、来源与可更新状态。 是否会改变现有设计边界。

**旧路径为何合理**：各模态保留独立 encoder 和静态融合点，职责清楚且便于单独优化。

**约束变化与机制**：exact-v1 的 `3.2 Overall Framework` 把论文方案定位到 跨模态 token identity、融合、时间锚点与可变表示状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-REPRESENTATION` 负责 跨模态 token identity、融合、时间锚点与可变表示状态；定位证据为 `arXiv:2603.12255v1 HTML — §3.2 Overall Framework [facet=method]; https://arxiv.org/html/2603.12255v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12255v1.html; sha256:8e19b1b834aa69d1cba5220ad5dd113db1b178a67a1feddd593edf62849b6288`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.4 Ablation Study and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12255v1 HTML — §4.4 Ablation Study and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12255v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12255v1.html; sha256:8e19b1b834aa69d1cba5220ad5dd113db1b178a67a1feddd593edf62849b6288`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。模态关系固定且输入短时，静态 late fusion 仍具有更低复杂度。

<!-- claim:SF-2026-ARXIV-2603-12255:start -->**Claim Boundary**：只支持 arXiv:2603.12255v1 §3.2 Overall Framework 的机制与 §4.4 Ablation Study and Analysis 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12255:end -->
<!-- review:SF-2026-ARXIV-2603-12255:end -->
### Video Streaming Thinking: VideoLLMs Can Watch and Think Simultaneously

<!-- review:SF-2026-ARXIV-2603-12262:start -->
**问题**：视频生成若只能在完整上下文后开始 reasoning，会牺牲流式场景的时效和状态连续性。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：Video Streaming Thinking 将持续到达帧分段写入可更新表示，并让生成与观察交错，而非一次性消费完整视频。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.12262v1 HTML — §2.2 Training Method for VST [facet=method]; https://arxiv.org/html/2603.12262v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12262v1.html; sha256:dbcee7a4450506878a8ddac91bde21819034a3a085a42a3676723c20fa5d2f4d`。

**Evaluation contract 与未证明部分**：结果限于公开模型、视频任务和 chunk policy；不证明开放长流中的 memory drift 可控。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12262v1 HTML — §3.3 Online Video Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.12262v1; papers/2026/03/_sources/daily-20260313/exact-v1-bodies/2603.12262v1.html; sha256:dbcee7a4450506878a8ddac91bde21819034a3a085a42a3676723c20fa5d2f4d`。

**Trade-off / failure / coexistence**：在线处理降低等待却减少未来上下文并增加 segment boundary error；离线高质量理解仍可看完整视频。

<!-- claim:SF-2026-ARXIV-2603-12262:start -->**Claim Boundary**：只支持 arXiv:2603.12262v1 §2.2 Training Method for VST 的机制与 §3.3 Online Video Benchmark Results 的公开 workload；§Limitation and Future Works. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12262:end -->
<!-- review:SF-2026-ARXIV-2603-12262:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-11438 | score_7_9;potential_books_delta | selected | DA-20260313-10 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260313-10 |
| SF-2026-ARXIV-2603-12118 | score_7_9;potential_books_delta | selected | DA-20260313-27 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260313-27 |

<!-- analysis:DA-20260313-10:start -->
### NCCLbpf: Verified, Composable Policy Execution for GPU Collective Communication

GPU collective 的策略若只存在于动态 hook 或运维脚本，执行顺序和安全边界难以复算。 旧路径在其原约束下仍合理：单机或纯数据并行状态最少、同步语义清晰。 本 family 的设计变化是：NCCLbpf 将通信策略编译为受限、可组合且可验证的执行单元，在 collective 边界检查并应用调度/传输决定。 其公开验证边界为：作者验证公开策略与 collective workload 的可执行性和开销；不能据此证明任意 eBPF 类程序或故障场景都安全。 新增代价与回退条件为：可验证策略减少不可控扩展，却限制表达能力并增加 verifier/ABI 兼容责任；固定拓扑仍可采用静态 NCCL 配置。
<!-- analysis:DA-20260313-10:end -->
<!-- analysis:DA-20260313-27:start -->
### Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models

any-to-any 多模态模型包含编码、跨模态变换与解码 DAG，沿用文本 LLM 的单 token 队列会让中间张量和阶段资源失配。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：Cornserve 把 modality-specific stage、依赖和中间数据生命周期暴露给 distributed scheduler，联合执行放置、批处理与传输。 其公开验证边界为：公开模型和集群结果支持所测 DAG 的端到端收益；不同模态组合、网络和质量约束仍需重新测量。 新增代价与回退条件为：DAG-aware serving 提高异质资源利用率，但扩大状态 identity、故障恢复和跨阶段 backpressure 的复杂度；纯文本路径仍适合专用 engine。
<!-- analysis:DA-20260313-27:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-11053 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#自检问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11053 | delta:SF-2026-ARXIV-2603-11053 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11053 |
| SF-2026-ARXIV-2603-11088 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多跳-delegation-必须保留-human-principal (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11088 | delta:SF-2026-ARXIV-2603-11088 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11088 |
| SF-2026-ARXIV-2603-11101 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#矩阵耦合-optimizer-必须把更新本身变成-distributed-operation (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11101 | delta:SF-2026-ARXIV-2603-11101 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11101 |
| SF-2026-ARXIV-2603-11132 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11132 | delta:SF-2026-ARXIV-2603-11132 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11132 |
| SF-2026-ARXIV-2603-11212 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从资产与信任边界开始 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11212 | delta:SF-2026-ARXIV-2603-11212 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11212 |
| SF-2026-ARXIV-2603-11273 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#连续-edge-inference-需要跨窗口携带-violation-risk-budget (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11273 | delta:SF-2026-ARXIV-2603-11273 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11273 |
| SF-2026-ARXIV-2603-11287 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#tool-成功要从-component-扩展到-information-use-与-outcome (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11287 | delta:SF-2026-ARXIV-2603-11287 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11287 |
| SF-2026-ARXIV-2603-11337 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11337 | delta:SF-2026-ARXIV-2603-11337 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11337 |
| SF-2026-ARXIV-2603-11340 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11340 | delta:SF-2026-ARXIV-2603-11340 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11340 |
| SF-2026-ARXIV-2603-11438 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#从本机协作到分布式执行 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11438 | delta:SF-2026-ARXIV-2603-11438 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-11438 |
| SF-2026-ARXIV-2603-11445 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11445 | delta:SF-2026-ARXIV-2603-11445 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11445 |
| SF-2026-ARXIV-2603-11504 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11504 | delta:SF-2026-ARXIV-2603-11504 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11504 |
| SF-2026-ARXIV-2603-11535 | MODEL-MOE | books/part-02-model/21-moe.md#先改变通信坐标，再扩大稀疏容量 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11535 | delta:SF-2026-ARXIV-2603-11535 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11535 |
| SF-2026-ARXIV-2603-11560 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11560 | delta:SF-2026-ARXIV-2603-11560 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11560 |
| SF-2026-ARXIV-2603-11564 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11564 | delta:SF-2026-ARXIV-2603-11564 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11564 |
| SF-2026-ARXIV-2603-11619 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11619 | delta:SF-2026-ARXIV-2603-11619 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11619 |
| SF-2026-ARXIV-2603-11768 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11768 | delta:SF-2026-ARXIV-2603-11768 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11768 |
| SF-2026-ARXIV-2603-11853 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11853 | delta:SF-2026-ARXIV-2603-11853 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11853 |
| SF-2026-ARXIV-2603-11873 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11873 | delta:SF-2026-ARXIV-2603-11873 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11873 |
| SF-2026-ARXIV-2603-11875 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#capability-access-control-可以前移到训练状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11875 | delta:SF-2026-ARXIV-2603-11875 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11875 |
| SF-2026-ARXIV-2603-11896 | AGENT-MEMORY | books/part-07-agent/77-memory.md#fact-state-与-retrieval-policy-state-必须分离 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11896 | delta:SF-2026-ARXIV-2603-11896 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11896 |
| SF-2026-ARXIV-2603-11935 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11935 | delta:SF-2026-ARXIV-2603-11935 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11935 |
| SF-2026-ARXIV-2603-11975 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#tool-成功要从-component-扩展到-information-use-与-outcome (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-11975 | delta:SF-2026-ARXIV-2603-11975 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-11975 |
| SF-2026-ARXIV-2603-12031 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#从-pod-placement-到-workload-snapshot (section Ch-owner) | books/part-06-ai-infrastructure/62-gateway.md#第62章-gateway (section Ch-adjacent); books/part-06-ai-infrastructure/64-volcano.md#第64章-gang-与队列调度：以-volcano-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12031 | delta:SF-2026-ARXIV-2603-12031 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12031 |
| SF-2026-ARXIV-2603-12038 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#连续-edge-inference-需要跨窗口携带-violation-risk-budget (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12038 | delta:SF-2026-ARXIV-2603-12038 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12038 |
| SF-2026-ARXIV-2603-12056 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12056 | delta:SF-2026-ARXIV-2603-12056 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12056 |
| SF-2026-ARXIV-2603-12118 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12118 | delta:SF-2026-ARXIV-2603-12118 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-12118 |
| SF-2026-ARXIV-2603-12201 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#稀疏-kv-保留的是派生状态，不只是被抽样的-token (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12201 | delta:SF-2026-ARXIV-2603-12201 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12201 |
| SF-2026-ARXIV-2603-12230 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12230 | delta:SF-2026-ARXIV-2603-12230 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12230 |
| SF-2026-ARXIV-2603-12255 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#rate、distortion-与下游容量必须联合选择 (section Ch-owner) | books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent); books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12255 | delta:SF-2026-ARXIV-2603-12255 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12255 |
| SF-2026-ARXIV-2603-12262 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#diffusion：用迭代修正换并行状态更新 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12262 | delta:SF-2026-ARXIV-2603-12262 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12262 |

<!-- books-review:SF-2026-ARXIV-2603-11053:start -->
### Speculative Decoding Scaling Laws (SDSL): Throughput Optimization Made Simple — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11053:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：1. Speculative Decoding 为什么需要 draft model 和 target model？ 2. 为什么生成是串行的，但验证候选 token 可以并行？ 3. 为什么它不是简单的小模型替代？ 4. acceptance rate 对加速效果有什么影响？ 5. `min(1,p/q)` 与 residual sampling 怎样保持 target distribution？ 6. 为什么 acceptance rate 高仍不保证端到端加速？ 7. Speculative Decoding 会给 KV Cache 和 batching 带来哪些额外复杂度？ 8. 为什么 lossy verification 不能只被描述为 runtime optimization？ 9. 含 truncation policy 的 verification 为什么必须使用 matched-policy baseline？ 10. 为什么 draft checkpoint 必须与 target revision、tokenizer 和 runtime 一起版本化？ 11. Edge/cloud speculation 中，为什么 verify depth 必须同时看到网络状态与 target capacity？ 12. 为什么 hybrid attention/recurrent model 的 speculative rollback 不能只移动 KV cached-length pointer？<!-- existing:SF-2026-ARXIV-2603-11053:end -->

<!-- delta:SF-2026-ARXIV-2603-11053:start -->新证据差异：exact-v1 的 `5.1 Motivation and Numerical Approximation Methodology` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11053:end -->

边界：只支持 arXiv:2603.11053v1 §5.1 Motivation and Numerical Approximation Methodology 的机制与 §Results and validation. 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11053:end -->
<!-- books-review:SF-2026-ARXIV-2603-11088:start -->
### The Attack and Defense Landscape of Agentic AI: A Comprehensive Survey — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11088:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这把 authorization 从 prompt/Agent 自述迁移到可核验 provenance chain，但不证明行为正确，也不替代 prompt-injection defense、sandbox 或最小权限。Key/token 生命周期、撤销、重放和 scope composition 都是新增压力；链不完整、过期或验证失败时必须 fail closed，并回退人工授权。<!-- existing:SF-2026-ARXIV-2603-11088:end -->

<!-- delta:SF-2026-ARXIV-2603-11088:start -->新证据差异：exact-v1 的 `4.4. Attack Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11088:end -->

边界：只支持 arXiv:2603.11088v1 §4.4. Attack Methods 的机制与 §5.2.5. Human-In-The-Loop Validation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11088:end -->
<!-- books-review:SF-2026-ARXIV-2603-11101:start -->
### Thousand-GPU Large-Scale Training and Optimization Recipe for AI-Native Cloud Embodied Intelligence Infrastructure — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11101:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：以 element-wise optimizer state 做 ZeRO/FSDP 式分片，在更新可按参数局部计算时是合理的。矩阵级 Newton–Schulz optimizer update 却耦合整块矩阵，局部 post-processing 会让相同 checkpoint 在不同 layout 下产生不同语义。训练状态因此必须增加 matrix layout、collective algorithm、worker group 与 optimizer-step identity，把更新本身作为分布式矩阵操作并与 checkpoint 原子提交。论文在 embodied foundation model 与 LLM 训练中报告加速且性能接近 AdamW，但没有证明任意拓扑、矩阵形状或长程收敛与集中式实现等价。collective 中断、layout 漂移或数值分歧时应恢复最近一致 checkpoint，并退回已验证的 AdamW/旧 optimizer 路径；局部优化器与矩阵耦合优化器按更新结构共存。<!-- existing:SF-2026-ARXIV-2603-11101:end -->

<!-- delta:SF-2026-ARXIV-2603-11101:start -->新证据差异：exact-v1 的 `2.1 Overall Architecture Design` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11101:end -->

边界：只支持 arXiv:2603.11101v1 §2.1 Overall Architecture Design 的机制与 §3.1 Thousand-GPU Scale Framework Validation 的公开 workload；§4 Conclusion and Future Outlook 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11101:end -->
<!-- books-review:SF-2026-ARXIV-2603-11132:start -->
### WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11132:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-11132:end -->

<!-- delta:SF-2026-ARXIV-2603-11132:start -->新证据差异：exact-v1 的 `3.1 Threat Models` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11132:end -->

边界：只支持 arXiv:2603.11132v1 §3.1 Threat Models 的机制与 §4.1 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11132:end -->
<!-- books-review:SF-2026-ARXIV-2603-11212:start -->
### Security-by-Design for LLM-Based Code Generation: Leveraging Internal Representations for Concept-Driven Steering Mechanisms — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11212:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。<!-- existing:SF-2026-ARXIV-2603-11212:end -->

<!-- delta:SF-2026-ARXIV-2603-11212:start -->新证据差异：exact-v1 的 `V-A Datasets and Baseline Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11212:end -->

边界：只支持 arXiv:2603.11212v1 §V-A Datasets and Baseline Methods 的机制与 §V Comparative Evaluation 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11212:end -->
<!-- books-review:SF-2026-ARXIV-2603-11273:start -->
### Duration Aware Scheduling for ASR Serving Under Workload Drift — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11273:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：Risk budget 不是成功概率真值，也不能取代 hard safety deadline。它用更高 utilization 与及时完成率的机会换预测误差、 distribution drift、风险相关性和跨流公平性；低估 burst 会连续透支，过度保守则长期闲置设备。独立请求、宽松 deadline、 稳定设备或 predictor 未校准时，EDF、固定 reservation 与 hard-cap admission 仍更透明。AEGIS 的 exact-v1 只支持其公开 的 continuous edge workload、risk assumptions 与实验指标，不证明任意模型、硬件、并发或安全控制周期。<!-- existing:SF-2026-ARXIV-2603-11273:end -->

<!-- delta:SF-2026-ARXIV-2603-11273:start -->新证据差异：exact-v1 的 `3 Methodology` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11273:end -->

边界：只支持 arXiv:2603.11273v1 §3 Methodology 的机制与 §Evaluation Metrics. 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11273:end -->
<!-- books-review:SF-2026-ARXIV-2603-11287:start -->
### Synthesis-in-the-Loop Evaluation of LLMs for RTL Generation: Quality, Reliability, and Failure Modes — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11287:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Schema/action 正确不等于系统正确使用 tool result。Evaluation 应分开 action correctness、redundancy/efficiency、 process quality、information utilization、output evidence 与 domain outcome；component tests 继续负责低成本定位， trajectory/outcome gate 才决定发布。FinTrace 在其金融工具集上支持这种 ladder，不提供跨域指标权重或通用 judge。<!-- existing:SF-2026-ARXIV-2603-11287:end -->

<!-- delta:SF-2026-ARXIV-2603-11287:start -->新证据差异：exact-v1 的 `Pass rate versus implementation quality.` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11287:end -->

边界：只支持 arXiv:2603.11287v1 §Pass rate versus implementation quality. 的机制与 §3.2. Evaluation Pipeline 的公开 workload；§Limitations and future work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11287:end -->
<!-- books-review:SF-2026-ARXIV-2603-11337:start -->
### RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11337:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-11337:end -->

<!-- delta:SF-2026-ARXIV-2603-11337:start -->新证据差异：exact-v1 的 `V Experimental Design` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11337:end -->

边界：只支持 arXiv:2603.11337v1 §V Experimental Design 的机制与 §VI Results 的公开 workload；§VII Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11337:end -->
<!-- books-review:SF-2026-ARXIV-2603-11340:start -->
### Improving LLM Performance Through Black-Box Online Tuning: A Case for Adding System Specs to Factsheets for Trusted AI — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11340:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-11340:end -->

<!-- delta:SF-2026-ARXIV-2603-11340:start -->新证据差异：黑盒 controller 只使用短窗口端到端观测，以 hill climbing 更新配置，并把系统规格纳入 factsheet。<!-- delta:SF-2026-ARXIV-2603-11340:end -->

边界：只支持 arXiv:2603.11340v1 §II-B SLO-Tuner system design 的机制与 §II-C Results 的公开 workload；§III Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11340:end -->
<!-- books-review:SF-2026-ARXIV-2603-11438:start -->
### NCCLbpf: Verified, Composable Policy Execution for GPU Collective Communication — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11438:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：MPI 把问题提升为并行程序的执行模型。它定义 process/rank、communicator、point-to-point、collective、topology、one-sided communication 等语义，使程序描述“哪些 participants 对哪些数据共同完成什么操作”。MPI implementation 可以选择 shared memory、network transport 或 accelerator-aware path；能否直接处理 device buffer 取决于具体 implementation 和构建能力，不能从 MPI 标准名称本身推出。<!-- existing:SF-2026-ARXIV-2603-11438:end -->

<!-- delta:SF-2026-ARXIV-2603-11438:start -->新证据差异：NCCLbpf 将通信策略编译为受限、可组合且可验证的执行单元，在 collective 边界检查并应用调度/传输决定。<!-- delta:SF-2026-ARXIV-2603-11438:end -->

边界：只支持 arXiv:2603.11438v1 §3.3 与 §5.1–§5.3；verifier 只约束 memory/control safety，不能证明通过策略的 semantic/performance safety。已写回，等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-11438:end -->
<!-- books-review:SF-2026-ARXIV-2603-11445:start -->
### Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11445:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-11445:end -->

<!-- delta:SF-2026-ARXIV-2603-11445:start -->新证据差异：exact-v1 的 `4 Implementation` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11445:end -->

边界：只支持 arXiv:2603.11445v1 §4 Implementation 的机制与 §5.3 Results 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11445:end -->
<!-- books-review:SF-2026-ARXIV-2603-11504:start -->
### LongFlow: Efficient KV Cache Compression for Reasoning Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11504:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是 新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不 等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。<!-- existing:SF-2026-ARXIV-2603-11504:end -->

<!-- delta:SF-2026-ARXIV-2603-11504:start -->新证据差异：exact-v1 的 `3.1 A Lightweight Design Philosophy` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11504:end -->

边界：只支持 arXiv:2603.11504v1 §3.1 A Lightweight Design Philosophy 的机制与 §4.2 Main Results on Model Accuracy 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11504:end -->
<!-- books-review:SF-2026-ARXIV-2603-11535:start -->
### Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11535:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：标准 MoE 在 `d_model` 维 token state 上 routing、dispatch 和 expert compute。增加 experts 可以扩大总容量，但每个 assignment 搬运的 payload 仍与 hidden width 绑定；当 All-to-All bytes 或低延迟下的 expert weight load 成为瓶颈时，仅继续增加 experts/top-k 会放大系统压力。<!-- existing:SF-2026-ARXIV-2603-11535:end -->

<!-- delta:SF-2026-ARXIV-2603-11535:start -->新证据差异：Expert Threshold 让每个 expert 维护全局分布 EMA threshold，独立决定接收 token，保持 causal routing。<!-- delta:SF-2026-ARXIV-2603-11535:end -->

边界：只支持 arXiv:2603.11535v1 §Appendix B Architecture Details 的机制与 §4.2 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11535:end -->
<!-- books-review:SF-2026-ARXIV-2603-11560:start -->
### Feedback-Coupled Memory Systems: A Dynamical Model for Adaptive Coordination — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11560:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-11560:end -->

<!-- delta:SF-2026-ARXIV-2603-11560:start -->新证据差异：exact-v1 的 `2 The Structural Architecture of Coordination` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11560:end -->

边界：只支持 arXiv:2603.11560v1 §2 The Structural Architecture of Coordination 的机制与 §How Intelligence Emerges: A Minimal Theory of Dynamic Adaptive Coordination 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11560:end -->
<!-- books-review:SF-2026-ARXIV-2603-11564:start -->
### Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11564:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是 新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不 等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。<!-- existing:SF-2026-ARXIV-2603-11564:end -->

<!-- delta:SF-2026-ARXIV-2603-11564:start -->新证据差异：exact-v1 的 `4 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11564:end -->

边界：只支持 arXiv:2603.11564v1 §4 Method 的机制与 §C.2 Empirical Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11564:end -->
<!-- books-review:SF-2026-ARXIV-2603-11619:start -->
### Taming OpenClaw: Security Analysis and Mitigation of Autonomous LLM Agent Threats — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11619:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-11619:end -->

<!-- delta:SF-2026-ARXIV-2603-11619:start -->新证据差异：exact-v1 的 `2.2. OpenClaw Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11619:end -->

边界：只支持 arXiv:2603.11619v1 §2.2. OpenClaw Architecture 的机制与 §Evaluation 的公开 workload；§5.2. Limitations of Existing Defenses in Guaranteeing OpenClaw Security 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11619:end -->
<!-- books-review:SF-2026-ARXIV-2603-11768:start -->
### Governing Evolving Memory in LLM Agents: Risks, Mechanisms, and the Stability and Safety Governed Memory (SSGM) Framework — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11768:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-11768:end -->

<!-- delta:SF-2026-ARXIV-2603-11768:start -->新证据差异：exact-v1 的 `6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11768:end -->

边界：只支持 arXiv:2603.11768v1 §6 Stability and Safety Governed Memory (SSGM): Design Principles and Research Agenda 的机制与 §6.3 Testable Research Hypotheses and Evaluation Protocols 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11768:end -->
<!-- books-review:SF-2026-ARXIV-2603-11853:start -->
### OpenClaw PRISM: A Zero-Fork, Defense-in-Depth Runtime Security Layer for Tool-Augmented LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11853:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-11853:end -->

<!-- delta:SF-2026-ARXIV-2603-11853:start -->新证据差异：exact-v1 的 `3.1 Architecture Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11853:end -->

边界：只支持 arXiv:2603.11853v1 §3.1 Architecture Overview 的机制与 §5.5 Preliminary Benchmark Results 的公开 workload；§7 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11853:end -->
<!-- books-review:SF-2026-ARXIV-2603-11873:start -->
### AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11873:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：独立 kernel launch 对大算子、稳定 control flow 和容易 capture 的 shape 最透明，CPU submission 开销相对计算也很小；CUDA Graph 进一步把重复 DAG 的准备成本移出 hot path。动态 inference、attention 辅助操作和 micro-batch 中出现大量短小算子后，单次 CPU→GPU launch 可能比算子本身更贵，而 graph 又要求可重复的结构，此时静态 fusion 与 graph capture 之间出现一个运行时分支。<!-- existing:SF-2026-ARXIV-2603-11873:end -->

<!-- delta:SF-2026-ARXIV-2603-11873:start -->新证据差异：exact-v1 的 `Overview` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11873:end -->

边界：只支持 arXiv:2603.11873v1 §Overview 的机制与 §Accuracy Evaluation 的公开 workload；§Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11873:end -->
<!-- books-review:SF-2026-ARXIV-2603-11875:start -->
### The Mirror Design Pattern: Strict Data Geometry over Model Scale for Prompt Injection Detection — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11875:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：安全数据闭环还可由当前 policy 生成 adversarial candidates，再由独立 guard / outcome policy 筛选后进入训练。它能把静态红队集扩展到当前模型暴露的 failure frontier，却同时制造 self-confirmation 风险：generator 与 guard 若共享模型家族、prompt 或表示盲点，可能一致地把危险样本标成安全；只保留通过 guard 的样本还会隐藏 false negative。因而 generated sample、generator checkpoint、guard version、policy taxonomy、人工复核切片和最终 deployment gate 必须分开保存。该机制适合作为受控 data augmentation，不能取代 output-time enforcement 或独立 red-team evaluation。<!-- existing:SF-2026-ARXIV-2603-11875:end -->

<!-- delta:SF-2026-ARXIV-2603-11875:start -->新证据差异：exact-v1 的 `3 System Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11875:end -->

边界：只支持 arXiv:2603.11875v1 §3 System Architecture 的机制与 §6 Experimental Results 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11875:end -->
<!-- books-review:SF-2026-ARXIV-2603-11896:start -->
### Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11896:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：用“加入第 k 批 memory 后的 downstream score 相对无 memory baseline 的变化”训练 selector，可以把终端 utility 回传给 memory ranking；但这个差值仍混合 generation sampling、candidate interaction 与 scorer noise， 不是单条 memory 的因果贡献。若 coarse filter 先误删 rare-but-critical evidence，后续 learned reasoning 无法 恢复；parser/error fallback 也可能静默改变训练标签。因此应同时测 candidate recall ceiling、selection precision、 working-model outcome、policy drift、fallback rate 和 selective deletion，而不只测最终任务分数。<!-- existing:SF-2026-ARXIV-2603-11896:end -->

<!-- delta:SF-2026-ARXIV-2603-11896:start -->新证据差异：exact-v1 的 `4.2 Streaming Architecture` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11896:end -->

边界：只支持 arXiv:2603.11896v1 §4.2 Streaming Architecture 的机制与 §5.4 Main Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11896:end -->
<!-- books-review:SF-2026-ARXIV-2603-11935:start -->
### MobileKernelBench: Can LLMs Write Efficient Kernels for Mobile Devices? — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11935:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2603-11935:end -->

<!-- delta:SF-2026-ARXIV-2603-11935:start -->新证据差异：exact-v1 的 `4.1 Agent Collaboration Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11935:end -->

边界：只支持 arXiv:2603.11935v1 §4.1 Agent Collaboration Design 的机制与 §3.2 Evaluation Pipeline 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11935:end -->
<!-- books-review:SF-2026-ARXIV-2603-11975:start -->
### HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-11975:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Oracle retrieval 分支可以定位瓶颈，却不是生产系统成绩；增加 step budget 可能改善 coverage，也会制造循环与成本 尾部。MADQA 的受限 PDF collection 支持 `accuracy x grounding x effort x failure stage` 比单一正确率更有诊断性， 不证明其语料、模型排名或 tool budget 可外推到企业私有、多语言环境。Corpus 小、retrieval 稳定时 static RAG 仍更可控；多步 Agent 只有在 action trace、evidence provenance 与 refusal/recovery 一起评估时才增加可信度。<!-- existing:SF-2026-ARXIV-2603-11975:end -->

<!-- delta:SF-2026-ARXIV-2603-11975:start -->新证据差异：exact-v1 的 `5.1.3 Implementation Details` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-11975:end -->

边界：只支持 arXiv:2603.11975v1 §5.1.3 Implementation Details 的机制与 §5.2 Main Results 的公开 workload；§D.3 Case III: Failure by System Latency 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-11975:end -->
<!-- books-review:SF-2026-ARXIV-2603-12031:start -->
### Agentic-Kube: A Graph-Enhanced Multi-Agent Reinforcement Learning Framework for Multi-Objective Kubernetes Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12031:start -->已读 owner `books/part-06-ai-infrastructure/63-gpu-scheduler.md` 与相邻章节。现有命题：同一 snapshot 避免成员在不同 cluster state 上各自“可行”，atomic commit 避免 partial placement；代价是 search space、snapshot staleness、reservation contention、rollback 与 fairness。Template owner 决定 workload intent， scheduler 拥有 placement attempt，resource drivers 拥有 inventory，queue policy 仍决定谁先获得机会。成员独立、 资源充足或低延迟单 Pod admission 更重要时，普通 Pod scheduling 仍合理。Kubernetes 1.36 的 Workload-Aware Scheduling v1alpha2 是实验性实现证据，不证明 dependency-heavy placement 已有完整搜索或 production fairness guarantee。<!-- existing:SF-2026-ARXIV-2603-12031:end -->

<!-- delta:SF-2026-ARXIV-2603-12031:start -->新证据差异：exact-v1 的 `4 System Design` 把论文方案定位到 GPU slice、隔离、配额与抢占控制；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12031:end -->

边界：只支持 arXiv:2603.12031v1 §4 System Design 的机制与 §6 Experimental Results and Analysis 的公开 workload；§7 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12031:end -->
<!-- books-review:SF-2026-ARXIV-2603-12038:start -->
### Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12038:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：逐请求 admission 在任务相互独立、设备容量稳定且 deadline 只属于当前请求时足够。Continuous edge inference 往往由 视频帧、传感器流或周期任务持续到达；一次延迟会压缩后续窗口，burst history 与设备状态又让风险随时间演化。只看 当前 queue length 或平均 latency，会把“本轮可执行”误当成“未来仍能守住违约上限”。<!-- existing:SF-2026-ARXIV-2603-12038:end -->

<!-- delta:SF-2026-ARXIV-2603-12038:start -->新证据差异：exact-v1 的 `System Design and Kernel Optimization` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12038:end -->

边界：只支持 arXiv:2603.12038v1 §System Design and Kernel Optimization 的机制与 §Experiments 的公开 workload；§Algorithm discussion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12038:end -->
<!-- books-review:SF-2026-ARXIV-2603-12056:start -->
### XSkill: Continual Learning from Experience and Skills in Multimodal Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12056:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-12056:end -->

<!-- delta:SF-2026-ARXIV-2603-12056:start -->新证据差异：exact-v1 的 `2 Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12056:end -->

边界：只支持 arXiv:2603.12056v1 §2 Methodology 的机制与 §3.2 Main Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12056:end -->
<!-- books-review:SF-2026-ARXIV-2603-12118:start -->
### Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12118:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。 生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入 真实 serving 的补全责任，而不是论文已经证明的反馈算法。<!-- existing:SF-2026-ARXIV-2603-12118:end -->

<!-- delta:SF-2026-ARXIV-2603-12118:start -->新证据差异：Cornserve 将 deployment/replica、invocation routing、intermediate transfer/completion 与 model execution/batching 分配给不同控制面/数据面 owner，并限定 record/replay 只适用于 deterministic task path。<!-- delta:SF-2026-ARXIV-2603-12118:end -->

边界：只支持 arXiv:2603.12118v1 §2.1–§2.2 与 §3；data-dependent control flow 必须留在 application 层。已写回，等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-12118:end -->
<!-- books-review:SF-2026-ARXIV-2603-12201:start -->
### IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12201:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：这不表示源 token 已被无损压缩。Donor-row swap 一类 causal intervention 只能证明所测 model、payload 和 question 中存在信息通道，不能证明任意数字、verbatim span、模型或位置变换都可恢复。Cache identity 除 checkpoint、tokenizer、 RoPE、dtype 和 layout 外，还必须保存 event role、source lineage、materialization rule 与 selected model positions；否则 相同 row index 可能对应不同派生语义。Selection、position policy 或模型变化时应 invalidation，readout 不确定时回到 完整 Context，而不是让 sparse state 自证充分。<!-- existing:SF-2026-ARXIV-2603-12201:end -->

<!-- delta:SF-2026-ARXIV-2603-12201:start -->新证据差异：exact-v1 的 `3 Method` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12201:end -->

边界：只支持 arXiv:2603.12201v1 §3 Method 的机制与 §4.3 Training-Free IndexCache Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12201:end -->
<!-- books-review:SF-2026-ARXIV-2603-12230:start -->
### Security Considerations for Artificial Intelligence Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12230:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2603-12230:end -->

<!-- delta:SF-2026-ARXIV-2603-12230:start -->新证据差异：exact-v1 的 `1.3 Agent Architecture, Deployment and Hosting` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12230:end -->

边界：只支持 arXiv:2603.12230v1 §1.3 Agent Architecture, Deployment and Hosting 的机制与 §Evaluation 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12230:end -->
<!-- books-review:SF-2026-ARXIV-2603-12255:start -->
### Spatial-TTT: Streaming Visual-based Spatial Intelligence with Test-Time Training — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12255:start -->已读 owner `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节。现有命题：这条路线从固定 spatial/channel bottleneck，演进到可度量的 rate，再到按 base-model capacity 选择 operating point。它没有否定传统 VAE、discrete codec 或 pixel-space model：低 latency、已有稳定 artifact、固定视觉域或需要明确 codebook identity 时，旧方案仍更合理。论文中排除 codec training 或 decoder sampling 的 FLOPs，不能被写成端到端系统更便宜。<!-- existing:SF-2026-ARXIV-2603-12255:end -->

<!-- delta:SF-2026-ARXIV-2603-12255:start -->新证据差异：exact-v1 的 `3.2 Overall Framework` 把论文方案定位到 跨模态 token identity、融合、时间锚点与可变表示状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12255:end -->

边界：只支持 arXiv:2603.12255v1 §3.2 Overall Framework 的机制与 §4.4 Ablation Study and Analysis 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12255:end -->
<!-- books-review:SF-2026-ARXIV-2603-12262:start -->
### Video Streaming Thinking: VideoLLMs Can Watch and Think Simultaneously — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12262:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：图像和视频往往容忍整体画面同时从粗到细修正，且用户不要求逐像素 streaming，因此 diffusion 的系统契约较自然。文本要求稳定前缀和低延迟流式输出，mutable tokens 的成本更明显。<!-- existing:SF-2026-ARXIV-2603-12262:end -->

<!-- delta:SF-2026-ARXIV-2603-12262:start -->新证据差异：Video Streaming Thinking 将持续到达帧分段写入可更新表示，并让生成与观察交错，而非一次性消费完整视频。<!-- delta:SF-2026-ARXIV-2603-12262:end -->

边界：只支持 arXiv:2603.12262v1 §2.2 Training Method for VST 的机制与 §3.3 Online Video Benchmark Results 的公开 workload；§Limitation and Future Works. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12262:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260313-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260313 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260313-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-11053; review:SF-2026-ARXIV-2603-11088; review:SF-2026-ARXIV-2603-11101; review:SF-2026-ARXIV-2603-11132; review:SF-2026-ARXIV-2603-11212; review:SF-2026-ARXIV-2603-11273; review:SF-2026-ARXIV-2603-11287; review:SF-2026-ARXIV-2603-11337; review:SF-2026-ARXIV-2603-11340; review:SF-2026-ARXIV-2603-11438; review:SF-2026-ARXIV-2603-11445; review:SF-2026-ARXIV-2603-11504; review:SF-2026-ARXIV-2603-11535; review:SF-2026-ARXIV-2603-11560; review:SF-2026-ARXIV-2603-11564; review:SF-2026-ARXIV-2603-11619; review:SF-2026-ARXIV-2603-11768; review:SF-2026-ARXIV-2603-11853; review:SF-2026-ARXIV-2603-11873; review:SF-2026-ARXIV-2603-11875; review:SF-2026-ARXIV-2603-11896; review:SF-2026-ARXIV-2603-11935; review:SF-2026-ARXIV-2603-11975; review:SF-2026-ARXIV-2603-12031; review:SF-2026-ARXIV-2603-12038; review:SF-2026-ARXIV-2603-12056; review:SF-2026-ARXIV-2603-12118; review:SF-2026-ARXIV-2603-12201; review:SF-2026-ARXIV-2603-12230; review:SF-2026-ARXIV-2603-12255; review:SF-2026-ARXIV-2603-12262 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260313-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260313-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260313/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 2 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 2 项 Books Integration：
- 更新并复核 `books/part-04-training-system/36-distributed-training.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
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
