# Daily Research — 2026-03-23

**Research Date:** 2026-03-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-22 09:00:00 ～ 2026-03-23 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=513/513/513；denominator=15、pre-denominator closures=498。exact-v1 Review complete=15、blocked=0；Integrate 建议=1。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-23 |
| Window End | 2026-03-23 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260323-AUTHOR-15 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-22T09:00:00+08:00 | 2026-03-23T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 513/513 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 513 | SF-2026-ARXIV-2603-19289;SF-2026-ARXIV-2603-19296;SF-2026-ARXIV-2603-19312;SF-2026-ARXIV-2603-19328;SF-2026-ARXIV-2603-19335;SF-2026-ARXIV-2603-19423;SF-2026-ARXIV-2603-19469;SF-2026-ARXIV-2603-19544;SF-2026-ARXIV-2603-19610;SF-2026-ARXIV-2603-19664;SF-2026-ARXIV-2603-19677;SF-2026-ARXIV-2603-19822;SF-2026-ARXIV-2603-19987;SF-2026-ARXIV-2603-20075;SF-2026-ARXIV-2603-20105 | pages=100; prefixes=00..99; final_cursor=end; registered=513; screened=513; retained=15; closure=498 | 2026-03-23T01:00:00+00:00 | screening-ledger-final.json#sha256=518452d93981fc009f94b91e5992f8732c0cce623e190a23076b002f4dbde740; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260323:start -->作者侧已逐项筛选全部 513 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260323:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-19289 | arXiv:2603.19289v1 | paper-v1:2603.19289 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19289 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19289 | no |
| SF-2026-ARXIV-2603-19296 | arXiv:2603.19296v1 | paper-v1:2603.19296 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19296 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19296 | no |
| SF-2026-ARXIV-2603-19312 | arXiv:2603.19312v1 | paper-v1:2603.19312 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-19312 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19312 | no |
| SF-2026-ARXIV-2603-19328 | arXiv:2603.19328v1 | paper-v1:2603.19328 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19328 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19328 | no |
| SF-2026-ARXIV-2603-19335 | arXiv:2603.19335v1 | paper-v1:2603.19335 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19335 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19335 | no |
| SF-2026-ARXIV-2603-19423 | arXiv:2603.19423v1 | paper-v1:2603.19423 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19423 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19423 | no |
| SF-2026-ARXIV-2603-19469 | arXiv:2603.19469v1 | paper-v1:2603.19469 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19469 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19469 | no |
| SF-2026-ARXIV-2603-19544 | arXiv:2603.19544v1 | paper-v1:2603.19544 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19544 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19544 | no |
| SF-2026-ARXIV-2603-19610 | arXiv:2603.19610v1 | paper-v1:2603.19610 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19610 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19610 | no |
| SF-2026-ARXIV-2603-19664 | arXiv:2603.19664v1 | paper-v1:2603.19664 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19664 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2603-19664 | no |
| SF-2026-ARXIV-2603-19677 | arXiv:2603.19677v1 | paper-v1:2603.19677 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19677 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19677 | no |
| SF-2026-ARXIV-2603-19822 | arXiv:2603.19822v1 | paper-v1:2603.19822 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19822 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19822 | no |
| SF-2026-ARXIV-2603-19987 | arXiv:2603.19987v1 | paper-v1:2603.19987 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-19987 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19987 | no |
| SF-2026-ARXIV-2603-20075 | arXiv:2603.20075v1 | paper-v1:2603.20075 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-20075 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20075 | no |
| SF-2026-ARXIV-2603-20105 | arXiv:2603.20105v1 | paper-v1:2603.20105 | 2026-W13 | 2026-03-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-20105 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20105 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-19289 | RP-5d028419bffdb342 | deep | arXiv:2603.19289v1 | SRC-ARXIV@arXiv:2603.19289v1 | arXiv:2603.19289v1 HTML — §Appendix A Estimator Architecture [facet=method]; https://arxiv.org/html/2603.19289v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19289v1.html; sha256:2b5d4d9eda201058f72d9a122756898c0ec0243bf503951e5d2ec271aec1a114 | arXiv:2603.19289v1 HTML — §5.1.3 Comparing On-Demand Loading Vs. Prefetching [facet=evaluation]; https://arxiv.org/html/2603.19289v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19289v1.html; sha256:2b5d4d9eda201058f72d9a122756898c0ec0243bf503951e5d2ec271aec1a114 | arXiv:2603.19289v1 HTML — §8 Future Work [facet=limitations]; https://arxiv.org/html/2603.19289v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19289v1.html; sha256:2b5d4d9eda201058f72d9a122756898c0ec0243bf503951e5d2ec271aec1a114 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19289v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19289 | complete |
| SF-2026-ARXIV-2603-19296 | RP-7062420682987626 | deep | arXiv:2603.19296v1 | SRC-ARXIV@arXiv:2603.19296v1 | arXiv:2603.19296v1 HTML — §TTQ: Test-Time Quantization with Online AWQ [facet=method]; https://arxiv.org/html/2603.19296v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19296v1.html; sha256:04be9fc678a1236879087e9efa4b8f5e9920738585d91d5b6ce5b2c75b5d0642 | arXiv:2603.19296v1 HTML — §Appendix K VLA Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.19296v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19296v1.html; sha256:04be9fc678a1236879087e9efa4b8f5e9920738585d91d5b6ce5b2c75b5d0642 | arXiv:2603.19296v1 HTML — §3 Conclusion [facet=limitations]; https://arxiv.org/html/2603.19296v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19296v1.html; sha256:04be9fc678a1236879087e9efa4b8f5e9920738585d91d5b6ce5b2c75b5d0642 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19296v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19296 | complete |
| SF-2026-ARXIV-2603-19312 | RP-6b196e759c3ed811 | standard | arXiv:2603.19312v1 | SRC-ARXIV@arXiv:2603.19312v1 | arXiv:2603.19312v1 HTML — §3 Method: LeWorldModel [facet=method]; https://arxiv.org/html/2603.19312v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19312v1.html; sha256:1d600ae7a572e90be32a27a4efdfc302bbf7f6b41346f23b2b0068e51c88b92d | arXiv:2603.19312v1 HTML — §Ablations. [facet=evaluation]; https://arxiv.org/html/2603.19312v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19312v1.html; sha256:1d600ae7a572e90be32a27a4efdfc302bbf7f6b41346f23b2b0068e51c88b92d | arXiv:2603.19312v1 HTML — §Limitations & Future Work. [facet=limitations]; https://arxiv.org/html/2603.19312v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19312v1.html; sha256:1d600ae7a572e90be32a27a4efdfc302bbf7f6b41346f23b2b0068e51c88b92d | arXiv exact-v1 identity https://arxiv.org/abs/2603.19312v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19312 | complete |
| SF-2026-ARXIV-2603-19328 | RP-e586673df4f3a28c | deep | arXiv:2603.19328v1 | SRC-ARXIV@arXiv:2603.19328v1 | arXiv:2603.19328v1 HTML — §3.1. Agent Architectures [facet=method]; https://arxiv.org/html/2603.19328v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19328v1.html; sha256:461dcc281f35304264c6da34f821e68510788a5d11e1e8567b4ab9e61e05f27c | arXiv:2603.19328v1 HTML — §3.7. Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.19328v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19328v1.html; sha256:461dcc281f35304264c6da34f821e68510788a5d11e1e8567b4ab9e61e05f27c | arXiv:2603.19328v1 HTML — §5. Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.19328v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19328v1.html; sha256:461dcc281f35304264c6da34f821e68510788a5d11e1e8567b4ab9e61e05f27c | arXiv exact-v1 identity https://arxiv.org/abs/2603.19328v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19328 | complete |
| SF-2026-ARXIV-2603-19335 | RP-05a41c7b0429a080 | deep | arXiv:2603.19335v1 | SRC-ARXIV@arXiv:2603.19335v1 | arXiv:2603.19335v1 HTML — §3.1 Framework Design [facet=method]; https://arxiv.org/html/2603.19335v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19335v1.html; sha256:c73a0e2730eac0008c99106e819c4cc492a0f825000b356bda59f6c20e2acdb7 | arXiv:2603.19335v1 HTML — §3.3 Evaluation Protocol [facet=evaluation]; https://arxiv.org/html/2603.19335v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19335v1.html; sha256:c73a0e2730eac0008c99106e819c4cc492a0f825000b356bda59f6c20e2acdb7 | arXiv:2603.19335v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.19335v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19335v1.html; sha256:c73a0e2730eac0008c99106e819c4cc492a0f825000b356bda59f6c20e2acdb7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19335v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19335 | complete |
| SF-2026-ARXIV-2603-19423 | RP-3a39e49998a09558 | deep | arXiv:2603.19423v1 | SRC-ARXIV@arXiv:2603.19423v1 | arXiv:2603.19423v1 HTML — §A.3 Diagnostic Dataset Design Extended Methodology [facet=method]; https://arxiv.org/html/2603.19423v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19423v1.html; sha256:5b440eff9dca2d0656627c09ed39ca9e96faee4361fbf6020edb22c48ac69cab | arXiv:2603.19423v1 HTML — §A.7.1 Empirical Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.19423v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19423v1.html; sha256:5b440eff9dca2d0656627c09ed39ca9e96faee4361fbf6020edb22c48ac69cab | arXiv:2603.19423v1 HTML — §8 Limitations [facet=limitations]; https://arxiv.org/html/2603.19423v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19423v1.html; sha256:5b440eff9dca2d0656627c09ed39ca9e96faee4361fbf6020edb22c48ac69cab | arXiv exact-v1 identity https://arxiv.org/abs/2603.19423v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19423 | complete |
| SF-2026-ARXIV-2603-19469 | RP-0782c1e08bf48b4e | deep | arXiv:2603.19469v1 | SRC-ARXIV@arXiv:2603.19469v1 | arXiv:2603.19469v1 HTML — §4.4 Integrated Security Definition [facet=method]; https://arxiv.org/html/2603.19469v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19469v1.html; sha256:dda7406994e2ab7ff6364f05d75fc8c0632359606566dea416cd11d2b5a04fa4 | arXiv:2603.19469v1 HTML — §6 Analysis of Existing Defenses [facet=evaluation]; https://arxiv.org/html/2603.19469v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19469v1.html; sha256:dda7406994e2ab7ff6364f05d75fc8c0632359606566dea416cd11d2b5a04fa4 | arXiv:2603.19469v1 HTML — §8 Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.19469v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19469v1.html; sha256:dda7406994e2ab7ff6364f05d75fc8c0632359606566dea416cd11d2b5a04fa4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19469v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19469 | complete |
| SF-2026-ARXIV-2603-19544 | RP-96f09f98a2aa7024 | deep | arXiv:2603.19544v1 | SRC-ARXIV@arXiv:2603.19544v1 | arXiv:2603.19544v1 HTML — §3.2 Practical FL Algorithm Design [facet=method]; https://arxiv.org/html/2603.19544v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19544v1.html; sha256:3902bec85c6ee8ef1ee407b70e6ab5431d32970e561673a49f91a50f803395ed | arXiv:2603.19544v1 HTML — §2 Results [facet=evaluation]; https://arxiv.org/html/2603.19544v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19544v1.html; sha256:3902bec85c6ee8ef1ee407b70e6ab5431d32970e561673a49f91a50f803395ed | arXiv:2603.19544v1 HTML — §3 Discussion [facet=limitations]; https://arxiv.org/html/2603.19544v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19544v1.html; sha256:3902bec85c6ee8ef1ee407b70e6ab5431d32970e561673a49f91a50f803395ed | arXiv exact-v1 identity https://arxiv.org/abs/2603.19544v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19544 | complete |
| SF-2026-ARXIV-2603-19610 | RP-49302ef3200d6997 | deep | arXiv:2603.19610v1 | SRC-ARXIV@arXiv:2603.19610v1 | arXiv:2603.19610v1 HTML — §4.2 ParallelVLM Pipeline [facet=method]; https://arxiv.org/html/2603.19610v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19610v1.html; sha256:6f8ec7c5caf4f4c7b3884ae280b706dcffaeed0d505d6c33892119dbad4e8f62 | arXiv:2603.19610v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.19610v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19610v1.html; sha256:6f8ec7c5caf4f4c7b3884ae280b706dcffaeed0d505d6c33892119dbad4e8f62 | arXiv:2603.19610v1 HTML — §5.3 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.19610v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19610v1.html; sha256:6f8ec7c5caf4f4c7b3884ae280b706dcffaeed0d505d6c33892119dbad4e8f62 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19610v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19610 | complete |
| SF-2026-ARXIV-2603-19664 | RP-4e831cab7ce46ef9 | deep | arXiv:2603.19664v1 | SRC-ARXIV@arXiv:2603.19664v1 | arXiv:2603.19664v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.19664v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19664v1.html; sha256:0177dd594c55ffbe2682f98a599cdd656f73450fb4db8e7b58601ddbfe5bdcd9 | arXiv:2603.19664v1 HTML — §5.4 Downstream Task Evaluation (RQ2) [facet=evaluation]; https://arxiv.org/html/2603.19664v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19664v1.html; sha256:0177dd594c55ffbe2682f98a599cdd656f73450fb4db8e7b58601ddbfe5bdcd9 | arXiv:2603.19664v1 HTML — §6 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.19664v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19664v1.html; sha256:0177dd594c55ffbe2682f98a599cdd656f73450fb4db8e7b58601ddbfe5bdcd9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19664v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19664 | complete |
| SF-2026-ARXIV-2603-19677 | RP-e4dbb316e38ec2e8 | deep | arXiv:2603.19677v1 | SRC-ARXIV@arXiv:2603.19677v1 | arXiv:2603.19677v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.19677v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19677v1.html; sha256:88d6120249bef241cf6e204ff552e535d993cbce9e58e2aa162bc7518d049241 | arXiv:2603.19677v1 HTML — §4.2 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.19677v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19677v1.html; sha256:88d6120249bef241cf6e204ff552e535d993cbce9e58e2aa162bc7518d049241 | arXiv:2603.19677v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.19677v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19677v1.html; sha256:88d6120249bef241cf6e204ff552e535d993cbce9e58e2aa162bc7518d049241 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19677v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19677 | complete |
| SF-2026-ARXIV-2603-19822 | RP-c6ad31f5fc2ee2f2 | deep | arXiv:2603.19822v1 | SRC-ARXIV@arXiv:2603.19822v1 | arXiv:2603.19822v1 HTML — §3 HUGE-Bench [facet=method]; https://arxiv.org/html/2603.19822v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19822v1.html; sha256:9538e8084fb8607d782383e589833ac93072ba0bea27d2d95b2bc24b4bc92b00 | arXiv:2603.19822v1 HTML — §2.3 Environment Representations and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.19822v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19822v1.html; sha256:9538e8084fb8607d782383e589833ac93072ba0bea27d2d95b2bc24b4bc92b00 | arXiv:2603.19822v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.19822v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19822v1.html; sha256:9538e8084fb8607d782383e589833ac93072ba0bea27d2d95b2bc24b4bc92b00 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19822v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19822 | complete |
| SF-2026-ARXIV-2603-19987 | RP-522bebab57f7968e | deep | arXiv:2603.19987v1 | SRC-ARXIV@arXiv:2603.19987v1 | arXiv:2603.19987v1 HTML — §Implementation Details [facet=method]; https://arxiv.org/html/2603.19987v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19987v1.html; sha256:e2baa60071be32ed6364c80688101b3d6d25cdb06375698f98d7d2d884c40219 | arXiv:2603.19987v1 HTML — §4.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.19987v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19987v1.html; sha256:e2baa60071be32ed6364c80688101b3d6d25cdb06375698f98d7d2d884c40219 | arXiv:2603.19987v1 HTML — §B.2 Discussion of Assumption 1 [facet=limitations]; https://arxiv.org/html/2603.19987v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19987v1.html; sha256:e2baa60071be32ed6364c80688101b3d6d25cdb06375698f98d7d2d884c40219 | arXiv exact-v1 identity https://arxiv.org/abs/2603.19987v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-19987 | complete |
| SF-2026-ARXIV-2603-20075 | RP-4086975fd8d32344 | deep | arXiv:2603.20075v1 | SRC-ARXIV@arXiv:2603.20075v1 | arXiv:2603.20075v1 HTML — §2 The llvm-autofix Harness [facet=method]; https://arxiv.org/html/2603.20075v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20075v1.html; sha256:ba8a49a0e94502e6beb9d44c3af8aa293fa672a495efe5b77b9f256e97a99d7f | arXiv:2603.20075v1 HTML — §4.1 Benchmark and Model Performance [facet=evaluation]; https://arxiv.org/html/2603.20075v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20075v1.html; sha256:ba8a49a0e94502e6beb9d44c3af8aa293fa672a495efe5b77b9f256e97a99d7f | arXiv:2603.20075v1 HTML — §4.2 Baseline Comparison and Common Failures [facet=limitations]; https://arxiv.org/html/2603.20075v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20075v1.html; sha256:ba8a49a0e94502e6beb9d44c3af8aa293fa672a495efe5b77b9f256e97a99d7f | arXiv exact-v1 identity https://arxiv.org/abs/2603.20075v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20075 | complete |
| SF-2026-ARXIV-2603-20105 | RP-fffa6e318edf1dc0 | standard | arXiv:2603.20105v1 | SRC-ARXIV@arXiv:2603.20105v1 | arXiv:2603.20105v1 HTML — §3 The λ​-RLM\lambda\text{-}\textsf{RLM} Framework [facet=method]; https://arxiv.org/html/2603.20105v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20105v1.html; sha256:98d5b59d453a861f201e5e1fbd81e188db91bc953307dc7274f020025f732466 | arXiv:2603.20105v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.20105v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20105v1.html; sha256:98d5b59d453a861f201e5e1fbd81e188db91bc953307dc7274f020025f732466 | arXiv:2603.20105v1 HTML — §7 Conclusions and Future Work [facet=limitations]; https://arxiv.org/html/2603.20105v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20105v1.html; sha256:98d5b59d453a861f201e5e1fbd81e188db91bc953307dc7274f020025f732466 | arXiv exact-v1 identity https://arxiv.org/abs/2603.20105v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-20105 | complete |

### Source Reviews

### Speculating Experts Accelerates Inference for Mixture-of-Experts

<!-- review:SF-2026-ARXIV-2603-19289:start -->
**问题**：MoE expert offload 把 decode 瓶颈从算力转为 CPU-GPU 权重传输，需求到达后再加载会阻塞 token。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：论文从当前 hidden representation 预测后续 expert，在计算重叠窗口内预取权重，并在误预测时回退正常加载。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.19289v1 HTML — §Appendix A Estimator Architecture [facet=method]; https://arxiv.org/html/2603.19289v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19289v1.html; sha256:2b5d4d9eda201058f72d9a122756898c0ec0243bf503951e5d2ec271aec1a114`。

**Evaluation contract 与未证明部分**：实验支持指定 MoE、内存预算与 interconnect 上的延迟；不证明 predictor 在分布变化时保持命中。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19289v1 HTML — §5.1.3 Comparing On-Demand Loading Vs. Prefetching [facet=evaluation]; https://arxiv.org/html/2603.19289v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19289v1.html; sha256:2b5d4d9eda201058f72d9a122756898c0ec0243bf503951e5d2ec271aec1a114`。

**Trade-off / failure / coexistence**：预取浪费带宽和显存，低可预测路由时按需加载更稳。

<!-- claim:SF-2026-ARXIV-2603-19289:start -->**Claim Boundary**：只支持 arXiv:2603.19289v1 §Appendix A Estimator Architecture 的机制与 §5.1.3 Comparing On-Demand Loading Vs. Prefetching 的公开 workload；§8 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19289:end -->
<!-- review:SF-2026-ARXIV-2603-19289:end -->
### TTQ: Activation-Aware Test-Time Quantization to Accelerate LLM Inference On The Fly

<!-- review:SF-2026-ARXIV-2603-19296:start -->
**问题**：离线 calibration 的量化参数在 prompt 域变化时失配，静态部署无法适应每次请求的 activation 分布。

**旧路径为何合理**：成熟 vendor kernel 在稳定 shape 上通常最可靠。

**约束变化与机制**：TTQ 在请求到达时做轻量在线 calibration，再选择本次推理的量化参数。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel/graph execution、量化、编译和硬件适配；定位证据为 `arXiv:2603.19296v1 HTML — §TTQ: Test-Time Quantization with Online AWQ [facet=method]; https://arxiv.org/html/2603.19296v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19296v1.html; sha256:04be9fc678a1236879087e9efa4b8f5e9920738585d91d5b6ce5b2c75b5d0642`。

**Evaluation contract 与未证明部分**：实验支持所测模型/任务的量化质量与速度；不证明每请求校准在高并发 SLO 下划算。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19296v1 HTML — §Appendix K VLA Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.19296v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19296v1.html; sha256:04be9fc678a1236879087e9efa4b8f5e9920738585d91d5b6ce5b2c75b5d0642`。

**Trade-off / failure / coexistence**：适配减少域偏差却增加首 token 开销；分布稳定时离线量化更便宜。

<!-- claim:SF-2026-ARXIV-2603-19296:start -->**Claim Boundary**：只支持 arXiv:2603.19296v1 §TTQ: Test-Time Quantization with Online AWQ 的机制与 §Appendix K VLA Benchmark Results 的公开 workload；§3 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19296:end -->
<!-- review:SF-2026-ARXIV-2603-19296:end -->
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels

<!-- review:SF-2026-ARXIV-2603-19312:start -->
**问题**：JEPA world model 为防 representation collapse 常依赖 EMA teacher、预训练 encoder 和多项辅助 loss。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：LeWM 只用 next-embedding prediction 与 Gaussian latent regularizer 从像素端到端训练，把防坍塌约束缩减为显式统计结构。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.19312v1 HTML — §3 Method: LeWorldModel [facet=method]; https://arxiv.org/html/2603.19312v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19312v1.html; sha256:1d600ae7a572e90be32a27a4efdfc302bbf7f6b41346f23b2b0068e51c88b92d`。

**Evaluation contract 与未证明部分**：结果支持指定视觉环境中的稳定训练和预测；不证明 latent state 可用于因果控制。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19312v1 HTML — §Ablations. [facet=evaluation]; https://arxiv.org/html/2603.19312v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19312v1.html; sha256:1d600ae7a572e90be32a27a4efdfc302bbf7f6b41346f23b2b0068e51c88b92d`。

**Trade-off / failure / coexistence**：更少组件提高可复现性但 Gaussian 假设限制表示；复杂环境仍可能需要 teacher 或多任务监督。

<!-- claim:SF-2026-ARXIV-2603-19312:start -->**Claim Boundary**：只支持 arXiv:2603.19312v1 §3 Method: LeWorldModel 的机制与 §Ablations. 的公开 workload；§Limitations & Future Work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19312:end -->
<!-- review:SF-2026-ARXIV-2603-19312:end -->
### The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents

<!-- review:SF-2026-ARXIV-2603-19328:start -->
**问题**：tool-using agent 的 runtime verifier 越精细，安全性可能提高，但检查开销和拒绝会随任务 horizon 累积。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：作者固定模型、工具和环境，只改变 control-flow 与 verifier precision，以区分 verifier tax 与模型能力差异。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.19328v1 HTML — §3.1. Agent Architectures [facet=method]; https://arxiv.org/html/2603.19328v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19328v1.html; sha256:461dcc281f35304264c6da34f821e68510788a5d11e1e8567b4ab9e61e05f27c`。

**Evaluation contract 与未证明部分**：评测同时报告任务成功和程序性安全，并观察 horizon 变化；结论只属于所测架构与风险定义。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19328v1 HTML — §3.7. Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.19328v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19328v1.html; sha256:461dcc281f35304264c6da34f821e68510788a5d11e1e8567b4ab9e61e05f27c`。

**Trade-off / failure / coexistence**：更强 verifier 带来延迟与 false reject；低风险短任务可采用较薄检查，高风险长任务需要按路径分配验证预算。

<!-- claim:SF-2026-ARXIV-2603-19328:start -->**Claim Boundary**：只支持 arXiv:2603.19328v1 §3.1. Agent Architectures 的机制与 §3.7. Evaluation Metrics 的公开 workload；§5. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19328:end -->
<!-- review:SF-2026-ARXIV-2603-19328:end -->
### Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions

<!-- review:SF-2026-ARXIV-2603-19335:start -->
**问题**：post-training 算法排名常在单一模型规模上得出，可能把规模效应误当算法普遍优越。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：oxRL 用统一实现控制 51 种配方，在多个模型规模下分离 scale、online/offline paradigm 和具体算法。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.19335v1 HTML — §3.1 Framework Design [facet=method]; https://arxiv.org/html/2603.19335v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19335v1.html; sha256:c73a0e2730eac0008c99106e819c4cc492a0f825000b356bda59f6c20e2acdb7`。

**Evaluation contract 与未证明部分**：GSM8K 等可验证任务显示排名会随规模反转；这证明配方选择依赖规模，不证明同一排序适用于开放任务。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19335v1 HTML — §3.3 Evaluation Protocol [facet=evaluation]; https://arxiv.org/html/2603.19335v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19335v1.html; sha256:c73a0e2730eac0008c99106e819c4cc492a0f825000b356bda59f6c20e2acdb7`。

**Trade-off / failure / coexistence**：统一控制提高可比性但任务窄；成熟固定 workload 仍可复用已验证算法，无需全量重扫。

<!-- claim:SF-2026-ARXIV-2603-19335:start -->**Claim Boundary**：只支持 arXiv:2603.19335v1 §3.1 Framework Design 的机制与 §3.3 Evaluation Protocol 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19335:end -->
<!-- review:SF-2026-ARXIV-2603-19335:end -->
### The Autonomy Tax: Defense Training Breaks LLM Agents

<!-- review:SF-2026-ARXIV-2603-19423:start -->
**问题**：prompt-injection defense training 可能提高拒绝，却同时破坏 agent 完成长工具链任务的自治能力。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：研究把攻击鲁棒性与任务 competence 放在同一评测矩阵，比较不同 defense training 强度下的 capability-alignment frontier。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.19423v1 HTML — §A.3 Diagnostic Dataset Design Extended Methodology [facet=method]; https://arxiv.org/html/2603.19423v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19423v1.html; sha256:5b440eff9dca2d0656627c09ed39ca9e96faee4361fbf6020edb22c48ac69cab`。

**Evaluation contract 与未证明部分**：结果限于所测 agents、攻击和任务，不能推出防御训练必然降低所有能力。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19423v1 HTML — §A.7.1 Empirical Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.19423v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19423v1.html; sha256:5b440eff9dca2d0656627c09ed39ca9e96faee4361fbf6020edb22c48ac69cab`。

**Trade-off / failure / coexistence**：安全收益必须与自治损失共同设 release gate；高风险环境可接受更保守策略。

<!-- claim:SF-2026-ARXIV-2603-19423:start -->**Claim Boundary**：只支持 arXiv:2603.19423v1 §A.3 Diagnostic Dataset Design Extended Methodology 的机制与 §A.7.1 Empirical Evaluation Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19423:end -->
<!-- review:SF-2026-ARXIV-2603-19423:end -->
### A Framework for Formalizing LLM Agent Security

<!-- review:SF-2026-ARXIV-2603-19469:start -->
**问题**：agent action 是否越权取决于指令来源、目标、时间和此前状态，静态恶意字符串无法定义安全性。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文把安全判定分解为若干 contextual oracle，并用 temporal property 描述授权、信息流与 action sequence。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.19469v1 HTML — §4.4 Integrated Security Definition [facet=method]; https://arxiv.org/html/2603.19469v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19469v1.html; sha256:dda7406994e2ab7ff6364f05d75fc8c0632359606566dea416cd11d2b5a04fa4`。

**Evaluation contract 与未证明部分**：exact-v1 通过现有防御映射展示覆盖缺口，没有独立攻击/防御实验；它提供形式化需求而非实现效果。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19469v1 HTML — §6 Analysis of Existing Defenses [facet=evaluation]; https://arxiv.org/html/2603.19469v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19469v1.html; sha256:dda7406994e2ab7ff6364f05d75fc8c0632359606566dea416cd11d2b5a04fa4`。

**Trade-off / failure / coexistence**：oracle 分解澄清责任但实现近似会产生组合误差；单用户、单工具和无状态场景可用简单 ACL。

<!-- claim:SF-2026-ARXIV-2603-19469:start -->**Claim Boundary**：只支持 arXiv:2603.19469v1 §4.4 Integrated Security Definition 的机制与 §6 Analysis of Existing Defenses 的公开 workload；§8 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19469:end -->
<!-- review:SF-2026-ARXIV-2603-19469:end -->
### Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers

<!-- review:SF-2026-ARXIV-2603-19544:start -->
**问题**：科学 foundation model 的数据受主权和体量限制无法集中，普通跨数据中心 FL 又未覆盖 supercomputer job/failure semantics。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：系统在多个 HPC facility 之间只交换模型状态，并将本地大规模并行训练、跨站聚合和恢复分层。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.19544v1 HTML — §3.2 Practical FL Algorithm Design [facet=method]; https://arxiv.org/html/2603.19544v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19544v1.html; sha256:3902bec85c6ee8ef1ee407b70e6ab5431d32970e561673a49f91a50f803395ed`。

**Evaluation contract 与未证明部分**：跨设施实验支持指定网络和科学模型的可运行性；不证明隐私泄露已由不搬原始数据解决。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19544v1 HTML — §2 Results [facet=evaluation]; https://arxiv.org/html/2603.19544v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19544v1.html; sha256:3902bec85c6ee8ef1ee407b70e6ab5431d32970e561673a49f91a50f803395ed`。

**Trade-off / failure / coexistence**：跨站同步慢、异构且故障域更大；允许集中数据时单集群训练更简单。

<!-- claim:SF-2026-ARXIV-2603-19544:start -->**Claim Boundary**：只支持 arXiv:2603.19544v1 §3.2 Practical FL Algorithm Design 的机制与 §2 Results 的公开 workload；§3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19544:end -->
<!-- review:SF-2026-ARXIV-2603-19544:end -->
### ParallelVLM: Lossless Video-LLM Acceleration with Visual Alignment Aware Parallel Speculative Decoding

<!-- review:SF-2026-ARXIV-2603-19610:start -->
**问题**：Video-LLM 的视觉 token 很多，普通 speculative decoding 在 draft/target 相互等待时无法填满硬件。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：ParallelVLM 并行化 draft 与 target 阶段，并用视觉对齐约束保持 exact acceptance。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.19610v1 HTML — §4.2 ParallelVLM Pipeline [facet=method]; https://arxiv.org/html/2603.19610v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19610v1.html; sha256:6f8ec7c5caf4f4c7b3884ae280b706dcffaeed0d505d6c33892119dbad4e8f62`。

**Evaluation contract 与未证明部分**：实验支持所测 video QA 模型的无损加速；不证明任意视觉剪枝或 draft 组合。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19610v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.19610v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19610v1.html; sha256:6f8ec7c5caf4f4c7b3884ae280b706dcffaeed0d505d6c33892119dbad4e8f62`。

**Trade-off / failure / coexistence**：并行执行消耗额外设备/显存；低并发或短视频时串行 decode 更省。

<!-- claim:SF-2026-ARXIV-2603-19610:start -->**Claim Boundary**：只支持 arXiv:2603.19610v1 §4.2 ParallelVLM Pipeline 的机制与 §5.2 Main Results 的公开 workload；§5.3 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19610:end -->
<!-- review:SF-2026-ARXIV-2603-19610:end -->
### The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference

<!-- review:SF-2026-ARXIV-2603-19664:start -->
**问题**：每层都存 K/V 假定这些张量不可重建，但 residual stream 已携带生成它们的大部分状态。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：论文从 residual stream 重新计算部分层的 K/V，以重算换缓存容量，并按层选择可替代的 KV。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.19664v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.19664v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19664v1.html; sha256:0177dd594c55ffbe2682f98a599cdd656f73450fb4db8e7b58601ddbfe5bdcd9`。

**Evaluation contract 与未证明部分**：多模型实验验证部分架构可近似或精确恢复；Gemma-3 sliding-window 层出现显著退化，证明该机制不是通用删除 KV。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19664v1 HTML — §5.4 Downstream Task Evaluation (RQ2) [facet=evaluation]; https://arxiv.org/html/2603.19664v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19664v1.html; sha256:0177dd594c55ffbe2682f98a599cdd656f73450fb4db8e7b58601ddbfe5bdcd9`。

**Trade-off / failure / coexistence**：省显存的代价是额外 compute 和架构敏感性；滑窗层、低算力或严苛 latency 下完整 KV 仍成立。

<!-- claim:SF-2026-ARXIV-2603-19664:start -->**Claim Boundary**：只支持 arXiv:2603.19664v1 §3 Method 的机制与 §5.4 Downstream Task Evaluation (RQ2) 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19664:end -->
<!-- review:SF-2026-ARXIV-2603-19664:end -->
### GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems

<!-- review:SF-2026-ARXIV-2603-19677:start -->
**问题**：多 agent topology 按单节点逐边生成，会把任务需要的协作组结构留给偶然涌现。

**旧路径为何合理**：固定少量 agent 的静态拓扑最易理解和调试。

**约束变化与机制**：GoAgent 先生成 group-of-agents，再在组内外布置通信边，使拓扑结构成为显式控制变量。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 agent group、communication topology、delegation 和故障隔离；定位证据为 `arXiv:2603.19677v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.19677v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19677v1.html; sha256:88d6120249bef241cf6e204ff552e535d993cbce9e58e2aa162bc7518d049241`。

**Evaluation contract 与未证明部分**：任务结果支持所测分工模式；不证明自动拓扑在动态失败下稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19677v1 HTML — §4.2 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.19677v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19677v1.html; sha256:88d6120249bef241cf6e204ff552e535d993cbce9e58e2aa162bc7518d049241`。

**Trade-off / failure / coexistence**：组结构增加规划和重配置成本；固定小团队可直接手工拓扑。

<!-- claim:SF-2026-ARXIV-2603-19677:start -->**Claim Boundary**：只支持 arXiv:2603.19677v1 §3 Methodology 的机制与 §4.2 Ablation Study 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19677:end -->
<!-- review:SF-2026-ARXIV-2603-19677:end -->
### HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks

<!-- review:SF-2026-ARXIV-2603-19822:start -->
**问题**：UAV benchmark 的逐步路线指令无法检验简短高层命令被展开为安全多阶段行为的能力。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：HUGE-Bench 以 digital twin、过程型轨迹和安全事件定义 high-level VLA evaluation contract。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.19822v1 HTML — §3 HUGE-Bench [facet=method]; https://arxiv.org/html/2603.19822v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19822v1.html; sha256:9538e8084fb8607d782383e589833ac93072ba0bea27d2d95b2bc24b4bc92b00`。

**Evaluation contract 与未证明部分**：四个场景和八类任务只支持该封闭分布，不代表真实飞行认证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19822v1 HTML — §2.3 Environment Representations and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.19822v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19822v1.html; sha256:9538e8084fb8607d782383e589833ac93072ba0bea27d2d95b2bc24b4bc92b00`。

**Trade-off / failure / coexistence**：过程评测更诊断但 simulator 成本高；低层导航仍适合传统 VLN suite。

<!-- claim:SF-2026-ARXIV-2603-19822:start -->**Claim Boundary**：只支持 arXiv:2603.19822v1 §3 HUGE-Bench 的机制与 §2.3 Environment Representations and Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19822:end -->
<!-- review:SF-2026-ARXIV-2603-19822:end -->
### Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States

<!-- review:SF-2026-ARXIV-2603-19987:start -->
**问题**：整段 trajectory 作为单一训练样本会丢失中间环境 state，使 post-training 难以学习 action 对下一状态的因果影响。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：工作把 rollout 重写为显式 Markov state-action transition，并在不输出 chain-of-thought 的条件下逐状态更新 policy。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.19987v1 HTML — §Implementation Details [facet=method]; https://arxiv.org/html/2603.19987v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19987v1.html; sha256:e2baa60071be32ed6364c80688101b3d6d25cdb06375698f98d7d2d884c40219`。

**Evaluation contract 与未证明部分**：实验与 conventional trajectory training 比较，支持所测环境中的能力提升；未证明所有任务都满足可观测 Markov 假设。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.19987v1 HTML — §4.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.19987v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.19987v1.html; sha256:e2baa60071be32ed6364c80688101b3d6d25cdb06375698f98d7d2d884c40219`。

**Trade-off / failure / coexistence**：状态化训练改善 credit assignment，却增加环境序列化和 state leakage 风险；短、静态任务仍可用整段偏好学习。

<!-- claim:SF-2026-ARXIV-2603-19987:start -->**Claim Boundary**：只支持 arXiv:2603.19987v1 §Implementation Details 的机制与 §4.1 Main Results 的公开 workload；§B.2 Discussion of Assumption 1 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-19987:end -->
<!-- review:SF-2026-ARXIV-2603-19987:end -->
### Agentic Harness for Real-World Compilers

<!-- review:SF-2026-ARXIV-2603-20075:start -->
**问题**：编译器修复 agent 若只在玩具代码上评估，无法暴露跨 pass、构建与回归测试的真实 workflow failure。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：该工作构建 llvm-bench 与 llvm-autofix harness，把缺陷定位、补丁生成、编译和测试反馈组织为可复现 agent loop。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.20075v1 HTML — §2 The llvm-autofix Harness [facet=method]; https://arxiv.org/html/2603.20075v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20075v1.html; sha256:ba8a49a0e94502e6beb9d44c3af8aa293fa672a495efe5b77b9f256e97a99d7f`。

**Evaluation contract 与未证明部分**：评测覆盖 LLVM 基准中的真实修复任务；它证明 harness 的诊断价值，不证明 agent 已能可靠维护编译器。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20075v1 HTML — §4.1 Benchmark and Model Performance [facet=evaluation]; https://arxiv.org/html/2603.20075v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20075v1.html; sha256:ba8a49a0e94502e6beb9d44c3af8aa293fa672a495efe5b77b9f256e97a99d7f`。

**Trade-off / failure / coexistence**：真实工具链提高有效性却增加执行成本和 flaky build；小型语法修复仍可用轻量单轮 benchmark。

<!-- claim:SF-2026-ARXIV-2603-20075:start -->**Claim Boundary**：只支持 arXiv:2603.20075v1 §2 The llvm-autofix Harness 的机制与 §4.1 Benchmark and Model Performance 的公开 workload；§4.2 Baseline Comparison and Common Failures 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20075:end -->
<!-- review:SF-2026-ARXIV-2603-20075:end -->
### The $\mathbf{Y}$-Combinator for LLMs: Solving Long-Context Rot with $λ$-Calculus

<!-- review:SF-2026-ARXIV-2603-20105:start -->
**问题**：开放式 REPL 的 recursive context processing 允许模型生成任意控制代码，难以验证终止与副作用。

**旧路径为何合理**：全量 attention 保留任意 token 交互，在中短序列上最直接。

**约束变化与机制**：lambda-RLM 将递归操作限制为 typed、预验证 combinator，使外部 context 的分解与聚合拥有受限执行语义。

**State / data / control owner**：`MODEL-LONG-CONTEXT` 负责 上下文选择、层次化表示和可访问记忆的语义边界；定位证据为 `arXiv:2603.20105v1 HTML — §3 The λ​-RLM\lambda\text{-}\textsf{RLM} Framework [facet=method]; https://arxiv.org/html/2603.20105v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20105v1.html; sha256:98d5b59d453a861f201e5e1fbd81e188db91bc953307dc7274f020025f732466`。

**Evaluation contract 与未证明部分**：实验支持所测长上下文任务的正确性/成本；不证明组合器集合覆盖任意推理。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.20105v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.20105v1; papers/2026/03/_sources/daily-20260323/exact-v1-bodies/2603.20105v1.html; sha256:98d5b59d453a861f201e5e1fbd81e188db91bc953307dc7274f020025f732466`。

**Trade-off / failure / coexistence**：可验证性以表达力为代价；短上下文可直接 attention，探索任务可能仍需开放 REPL。

<!-- claim:SF-2026-ARXIV-2603-20105:start -->**Claim Boundary**：只支持 arXiv:2603.20105v1 §3 The λ​-RLM\lambda\text{-}\textsf{RLM} Framework 的机制与 §5.1 Main Results 的公开 workload；§7 Conclusions and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-20105:end -->
<!-- review:SF-2026-ARXIV-2603-20105:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-19289 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19289 |
| SF-2026-ARXIV-2603-19296 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19296 |
| SF-2026-ARXIV-2603-19328 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19328 |
| SF-2026-ARXIV-2603-19335 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19335 |
| SF-2026-ARXIV-2603-19423 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19423 |
| SF-2026-ARXIV-2603-19469 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19469 |
| SF-2026-ARXIV-2603-19544 | score_7_9 | selected | DA-20260323-08 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260323-08 |
| SF-2026-ARXIV-2603-19610 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19610 |
| SF-2026-ARXIV-2603-19664 | score_7_9;potential_books_delta | selected | DA-20260323-10 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260323-10 |
| SF-2026-ARXIV-2603-19677 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19677 |
| SF-2026-ARXIV-2603-19822 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-19822 |
| SF-2026-ARXIV-2603-19987 | score_7_9 | selected | DA-20260323-13 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260323-13 |
| SF-2026-ARXIV-2603-20075 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-20075 |

<!-- analysis-decision:SF-2026-ARXIV-2603-19289:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19289:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19296:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19296:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19328:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19328:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19335:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19335:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19423:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19423:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19469:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19469:end -->
<!-- analysis:DA-20260323-08:start -->
### Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers

科学 foundation model 的数据受主权和体量限制无法集中，普通跨数据中心 FL 又未覆盖 supercomputer job/failure semantics。 旧路径在其原约束下仍合理：单机或纯数据并行状态最少、同步语义清晰。 本 family 的设计变化是：系统在多个 HPC facility 之间只交换模型状态，并将本地大规模并行训练、跨站聚合和恢复分层。 其公开验证边界为：跨设施实验支持指定网络和科学模型的可运行性；不证明隐私泄露已由不搬原始数据解决。 新增代价与回退条件为：跨站同步慢、异构且故障域更大；允许集中数据时单集群训练更简单。
<!-- analysis:DA-20260323-08:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19610:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19610:end -->
<!-- analysis:DA-20260323-10:start -->
### The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference

每层都存 K/V 假定这些张量不可重建，但 residual stream 已携带生成它们的大部分状态。 旧路径在其原约束下仍合理：完整、逐 token 保存 KV，换取语义透明和最低重算风险。 本 family 的设计变化是：论文从 residual stream 重新计算部分层的 K/V，以重算换缓存容量，并按层选择可替代的 KV。 其公开验证边界为：多模型实验验证部分架构可近似或精确恢复；Gemma-3 sliding-window 层出现显著退化，证明该机制不是通用删除 KV。 新增代价与回退条件为：省显存的代价是额外 compute 和架构敏感性；滑窗层、低算力或严苛 latency 下完整 KV 仍成立。
<!-- analysis:DA-20260323-10:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19677:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19677:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-19822:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-19822:end -->
<!-- analysis:DA-20260323-13:start -->
### Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States

整段 trajectory 作为单一训练样本会丢失中间环境 state，使 post-training 难以学习 action 对下一状态的因果影响。 旧路径在其原约束下仍合理：固定后训练配方便于重复和对比。 本 family 的设计变化是：工作把 rollout 重写为显式 Markov state-action transition，并在不输出 chain-of-thought 的条件下逐状态更新 policy。 其公开验证边界为：实验与 conventional trajectory training 比较，支持所测环境中的能力提升；未证明所有任务都满足可观测 Markov 假设。 新增代价与回退条件为：状态化训练改善 credit assignment，却增加环境序列化和 state leakage 风险；短、静态任务仍可用整段偏好学习。
<!-- analysis:DA-20260323-13:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-20075:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-20075:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-19289 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#moe-verification-还要结算-target-expert-expansion (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19289 | delta:SF-2026-ARXIV-2603-19289 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19289 |
| SF-2026-ARXIV-2603-19296 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19296 | delta:SF-2026-ARXIV-2603-19296 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19296 |
| SF-2026-ARXIV-2603-19312 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#视觉连贯不证明模型保存了不可见状态 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19312 | delta:SF-2026-ARXIV-2603-19312 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19312 |
| SF-2026-ARXIV-2603-19328 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#http-成功只是质量判断的第一道门 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19328 | delta:SF-2026-ARXIV-2603-19328 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19328 |
| SF-2026-ARXIV-2603-19335 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19335 | delta:SF-2026-ARXIV-2603-19335 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19335 |
| SF-2026-ARXIV-2603-19423 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19423 | delta:SF-2026-ARXIV-2603-19423 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19423 |
| SF-2026-ARXIV-2603-19469 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19469 | delta:SF-2026-ARXIV-2603-19469 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19469 |
| SF-2026-ARXIV-2603-19544 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#federated-tensor-type-定义一轮协议能表达什么 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19544 | delta:SF-2026-ARXIV-2603-19544 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19544 |
| SF-2026-ARXIV-2603-19610 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#当-draft-可能优于-target，系统进入效用仲裁分支 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19610 | delta:SF-2026-ARXIV-2603-19610 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19610 |
| SF-2026-ARXIV-2603-19664 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从统一跨层共享到-token-×-depth-自适应残差 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19664 | delta:SF-2026-ARXIV-2603-19664 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-19664 |
| SF-2026-ARXIV-2603-19677 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#topology-从部署前选择演进到运行时有界修复 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19677 | delta:SF-2026-ARXIV-2603-19677 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19677 |
| SF-2026-ARXIV-2603-19822 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19822 | delta:SF-2026-ARXIV-2603-19822 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19822 |
| SF-2026-ARXIV-2603-19987 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-19987 | delta:SF-2026-ARXIV-2603-19987 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-19987 |
| SF-2026-ARXIV-2603-20075 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20075 | delta:SF-2026-ARXIV-2603-20075 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20075 |
| SF-2026-ARXIV-2603-20105 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#context-anchor-从-passive-sink-演进为独立状态轨道 (section Ch-owner) | books/part-02-model/21-moe.md#第21章-moe (section Ch-adjacent); books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-20105 | delta:SF-2026-ARXIV-2603-20105 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-20105 |

<!-- books-review:SF-2026-ARXIV-2603-19289:start -->
### Speculating Experts Accelerates Inference for Mixture-of-Experts — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19289:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：Edge MoE 的 speculative cost 不能只看 draft acceptance。若 target experts 从 CPU 或 Flash 按需搬运，多 token block 的 verification 会激活各 token expert 的 union；更长 proposal 可能减少 target steps，却触发更多 weight loading。一个受限分支使用固定驻留的 draft expert 产生候选，再由 confidence 与预计 expert expansion 共同截断 block，并预取 target experts；最终 token 与 KV 仍只由 target verification 提交。<!-- existing:SF-2026-ARXIV-2603-19289:end -->

<!-- delta:SF-2026-ARXIV-2603-19289:start -->新证据差异：论文从当前 hidden representation 预测后续 expert，在计算重叠窗口内预取权重，并在误预测时回退正常加载。<!-- delta:SF-2026-ARXIV-2603-19289:end -->

边界：只支持 arXiv:2603.19289v1 §Appendix A Estimator Architecture 的机制与 §5.1.3 Comparing On-Demand Loading Vs. Prefetching 的公开 workload；§8 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19289:end -->
<!-- books-review:SF-2026-ARXIV-2603-19296:start -->
### TTQ: Activation-Aware Test-Time Quantization to Accelerate LLM Inference On The Fly — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19296:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-19296:end -->

<!-- delta:SF-2026-ARXIV-2603-19296:start -->新证据差异：TTQ 在请求到达时做轻量在线 calibration，再选择本次推理的量化参数。<!-- delta:SF-2026-ARXIV-2603-19296:end -->

边界：只支持 arXiv:2603.19296v1 §TTQ: Test-Time Quantization with Online AWQ 的机制与 §Appendix K VLA Benchmark Results 的公开 workload；§3 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19296:end -->
<!-- books-review:SF-2026-ARXIV-2603-19312:start -->
### LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19312:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：mutable predictive state → update hidden arrangement in place → carry the revised state across chunks。<!-- existing:SF-2026-ARXIV-2603-19312:end -->

<!-- delta:SF-2026-ARXIV-2603-19312:start -->新证据差异：LeWM 只用 next-embedding prediction 与 Gaussian latent regularizer 从像素端到端训练，把防坍塌约束缩减为显式统计结构。<!-- delta:SF-2026-ARXIV-2603-19312:end -->

边界：只支持 arXiv:2603.19312v1 §3 Method: LeWorldModel 的机制与 §Ablations. 的公开 workload；§Limitations & Future Work. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19312:end -->
<!-- books-review:SF-2026-ARXIV-2603-19328:start -->
### The Verifier Tax: Horizon Dependent Safety Success Tradeoffs in Tool Using LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19328:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：第 67 章可以持续观察 transport/runtime errors 和已产出的质量信号趋势；本章负责定义 semantic success 的口径、样本与决策边界。两者共享 request、model、prompt、retriever、tool 与 environment identity，但不能用可观测性代替规范性判断。<!-- existing:SF-2026-ARXIV-2603-19328:end -->

<!-- delta:SF-2026-ARXIV-2603-19328:start -->新证据差异：作者固定模型、工具和环境，只改变 control-flow 与 verifier precision，以区分 verifier tax 与模型能力差异。<!-- delta:SF-2026-ARXIV-2603-19328:end -->

边界：只支持 arXiv:2603.19328v1 §3.1. Agent Architectures 的机制与 §3.7. Evaluation Metrics 的公开 workload；§5. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19328:end -->
<!-- books-review:SF-2026-ARXIV-2603-19335:start -->
### Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19335:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-19335:end -->

<!-- delta:SF-2026-ARXIV-2603-19335:start -->新证据差异：oxRL 用统一实现控制 51 种配方，在多个模型规模下分离 scale、online/offline paradigm 和具体算法。<!-- delta:SF-2026-ARXIV-2603-19335:end -->

边界：只支持 arXiv:2603.19335v1 §3.1 Framework Design 的机制与 §3.3 Evaluation Protocol 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19335:end -->
<!-- books-review:SF-2026-ARXIV-2603-19423:start -->
### The Autonomy Tax: Defense Training Breaks LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19423:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-19423:end -->

<!-- delta:SF-2026-ARXIV-2603-19423:start -->新证据差异：研究把攻击鲁棒性与任务 competence 放在同一评测矩阵，比较不同 defense training 强度下的 capability-alignment frontier。<!-- delta:SF-2026-ARXIV-2603-19423:end -->

边界：只支持 arXiv:2603.19423v1 §A.3 Diagnostic Dataset Design Extended Methodology 的机制与 §A.7.1 Empirical Evaluation Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19423:end -->
<!-- books-review:SF-2026-ARXIV-2603-19469:start -->
### A Framework for Formalizing LLM Agent Security — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19469:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-19469:end -->

<!-- delta:SF-2026-ARXIV-2603-19469:start -->新证据差异：论文把安全判定分解为若干 contextual oracle，并用 temporal property 描述授权、信息流与 action sequence。<!-- delta:SF-2026-ARXIV-2603-19469:end -->

边界：只支持 arXiv:2603.19469v1 §4.4 Integrated Security Definition 的机制与 §6 Analysis of Existing Defenses 的公开 workload；§8 Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19469:end -->
<!-- books-review:SF-2026-ARXIV-2603-19544:start -->
### Scalable Cross-Facility Federated Learning for Scientific Foundation Models on Multiple Supercomputers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19544:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：普通 distributed tensor type 描述 device shard；federated computation 还必须区分 client-record axis 与 fixed-dimensional shared state。一轮协议可被约束为 `encode → merge → decode`：客户端只导出编码状态，merge owner 只组合声明的 shared state，decoder 再生成本地结果。类型系统拥有可表达通信边界，transport 不能用任意 payload 绕过它。<!-- existing:SF-2026-ARXIV-2603-19544:end -->

<!-- delta:SF-2026-ARXIV-2603-19544:start -->新证据差异：系统在多个 HPC facility 之间只交换模型状态，并将本地大规模并行训练、跨站聚合和恢复分层。<!-- delta:SF-2026-ARXIV-2603-19544:end -->

边界：只支持 arXiv:2603.19544v1 §3.2 Practical FL Algorithm Design 的机制与 §2 Results 的公开 workload；§3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19544:end -->
<!-- books-review:SF-2026-ARXIV-2603-19610:start -->
### ParallelVLM: Lossless Video-LLM Acceleration with Visual Alignment Aware Parallel Speculative Decoding — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19610:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：经典 speculative decoding 的正确性前提是 target 拥有最终分布，draft 只是 proposal，因此 rejection sampling 必须保持 target exactness。若某些输入上 draft 本身质量更高，选择 draft 输出就不再是 exact acceleration，而是新的 model-routing 决策；仲裁器必须显式拥有 utility、风险和成本契约，并与 lossless verification 分开。收益是可能避免“更大 target 覆盖更好 draft”，代价是失去单一分布保证、需要独立校准和回滚。要求严格复现 target 时，经典接受规则仍是唯一合理路径。当前证据只支持特定评测中的相对质量现象，不证明 draft 普遍优于 target。<!-- existing:SF-2026-ARXIV-2603-19610:end -->

<!-- delta:SF-2026-ARXIV-2603-19610:start -->新证据差异：ParallelVLM 并行化 draft 与 target 阶段，并用视觉对齐约束保持 exact acceptance。<!-- delta:SF-2026-ARXIV-2603-19610:end -->

边界：只支持 arXiv:2603.19610v1 §4.2 ParallelVLM Pipeline 的机制与 §5.2 Main Results 的公开 workload；§5.3 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19610:end -->
<!-- books-review:SF-2026-ARXIV-2603-19664:start -->
### The Residual Stream Is All You Need: On the Redundancy of the KV Cache in Transformer Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19664:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：第一条分支按 head 在 shared、residual 与 exact mode 之间做离散路由，适合表达“这个 head 是否需要保真”； 第二条分支按 token 分配 residual rank，适合表达“同一 head 内哪些位置需要更多层间细节”。二者复用相邻层 相关性原则，却不是同一种 selector。attention-logit 或 attention-output reconstruction error 只是当前 prompt 的 保真 proxy，不是未来 causal utility；probe、router、basis、residual precision 与 policy revision 都必须进入 cache identity。<!-- existing:SF-2026-ARXIV-2603-19664:end -->

<!-- delta:SF-2026-ARXIV-2603-19664:start -->新证据差异：论文从 residual stream 重新计算部分层的 K/V，以重算换缓存容量，并按层选择可替代的 KV。<!-- delta:SF-2026-ARXIV-2603-19664:end -->

边界：只支持 arXiv:2603.19664v1 §3 Method 的机制与 §5.4 Downstream Task Evaluation (RQ2) 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-19664:end -->
<!-- books-review:SF-2026-ARXIV-2603-19677:start -->
### GoAgent: Group-of-Agents Communication Topology Generation for LLM-based Multi-Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19677:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：修复可以扩展局部分支，也可以只改变通信 edge、插入 critic，或把重复的 state-changing actions 从 parallel 改为 serialized。后者说明“适应 topology”不是追求更密的 graph， 而是让 communication、visibility、execution order 与 validation path 对应当前 failure。<!-- existing:SF-2026-ARXIV-2603-19677:end -->

<!-- delta:SF-2026-ARXIV-2603-19677:start -->新证据差异：GoAgent 先生成 group-of-agents，再在组内外布置通信边，使拓扑结构成为显式控制变量。<!-- delta:SF-2026-ARXIV-2603-19677:end -->

边界：只支持 arXiv:2603.19677v1 §3 Methodology 的机制与 §4.2 Ablation Study 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19677:end -->
<!-- books-review:SF-2026-ARXIV-2603-19822:start -->
### HUGE-Bench: A Benchmark for High-Level UAV Vision-Language-Action Tasks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19822:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-19822:end -->

<!-- delta:SF-2026-ARXIV-2603-19822:start -->新证据差异：HUGE-Bench 以 digital twin、过程型轨迹和安全事件定义 high-level VLA evaluation contract。<!-- delta:SF-2026-ARXIV-2603-19822:end -->

边界：只支持 arXiv:2603.19822v1 §3 HUGE-Bench 的机制与 §2.3 Environment Representations and Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19822:end -->
<!-- books-review:SF-2026-ARXIV-2603-19987:start -->
### Breaking the Capability Ceiling of LLM Post-Training by Reintroducing Markov States — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-19987:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-19987:end -->

<!-- delta:SF-2026-ARXIV-2603-19987:start -->新证据差异：工作把 rollout 重写为显式 Markov state-action transition，并在不输出 chain-of-thought 的条件下逐状态更新 policy。<!-- delta:SF-2026-ARXIV-2603-19987:end -->

边界：只支持 arXiv:2603.19987v1 §Implementation Details 的机制与 §4.1 Main Results 的公开 workload；§B.2 Discussion of Assumption 1 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-19987:end -->
<!-- books-review:SF-2026-ARXIV-2603-20075:start -->
### Agentic Harness for Real-World Compilers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20075:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-20075:end -->

<!-- delta:SF-2026-ARXIV-2603-20075:start -->新证据差异：该工作构建 llvm-bench 与 llvm-autofix harness，把缺陷定位、补丁生成、编译和测试反馈组织为可复现 agent loop。<!-- delta:SF-2026-ARXIV-2603-20075:end -->

边界：只支持 arXiv:2603.20075v1 §2 The llvm-autofix Harness 的机制与 §4.1 Benchmark and Model Performance 的公开 workload；§4.2 Baseline Comparison and Common Failures 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20075:end -->
<!-- books-review:SF-2026-ARXIV-2603-20105:start -->
### The $\mathbf{Y}$-Combinator for LLMs: Solving Long-Context Rot with $λ$-Calculus — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-20105:start -->已读 owner `books/part-02-model/22-long-context.md` 与相邻章节。现有命题：BOS/attention sink 可自然聚合全局信息，却不保证它保存的是当前 query 所需 evidence。硬替换 BOS 会破坏原 计算，静态融合又固定强度；另一分支保留 causal self-attention，同时在少数层用 cross-attention 更新独立 anchor state。它新增 source/context identity、anchor freshness、injection-layer contract、malicious-context amplification 与 KV/cache compatibility。短 Context、原生 long-context training 或 RAG 已能提供精确证据时， 不需要额外 anchor。SinkTrack 仅提供 Experimental evidence，不证明 dual-track anchor 普遍优于原生 Attention。<!-- existing:SF-2026-ARXIV-2603-20105:end -->

<!-- delta:SF-2026-ARXIV-2603-20105:start -->新证据差异：lambda-RLM 将递归操作限制为 typed、预验证 combinator，使外部 context 的分解与聚合拥有受限执行语义。<!-- delta:SF-2026-ARXIV-2603-20105:end -->

边界：只支持 arXiv:2603.20105v1 §3 The λ​-RLM\lambda\text{-}\textsf{RLM} Framework 的机制与 §5.1 Main Results 的公开 workload；§7 Conclusions and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-20105:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260323-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260323 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260323-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260323-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260323-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260323/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 1 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 1 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
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
