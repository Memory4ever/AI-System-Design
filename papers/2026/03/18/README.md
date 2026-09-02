# Daily Research — 2026-03-18

**Research Date:** 2026-03-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-17 09:00:00 ～ 2026-03-18 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=660/660/660；denominator=13、pre-denominator closures=647。exact-v1 Review complete=13、blocked=0；Integrate 建议=0。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-18 |
| Window End | 2026-03-18 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260318-AUTHOR-13 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-17T09:00:00+08:00 | 2026-03-18T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 660/660 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 660 | SF-2026-ARXIV-2603-15690;SF-2026-ARXIV-2603-15714;SF-2026-ARXIV-2603-15727;SF-2026-ARXIV-2603-15798;SF-2026-ARXIV-2603-15973;SF-2026-ARXIV-2603-16013;SF-2026-ARXIV-2603-16104;SF-2026-ARXIV-2603-16158;SF-2026-ARXIV-2603-16435;SF-2026-ARXIV-2603-16572;SF-2026-ARXIV-2603-16586;SF-2026-ARXIV-2603-16731;SF-2026-ARXIV-2603-16817 | pages=100; prefixes=00..99; final_cursor=end; registered=660; screened=660; retained=13; closure=647 | 2026-03-18T01:00:00+00:00 | screening-ledger-final.json#sha256=b1c0833af54907b2a8b8c289ceb1f0b98577c14cc908021b939c5ffed3f7b6d5; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260318:start -->作者侧已逐项筛选全部 660 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260318:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-15690 | arXiv:2603.15690v1 | paper-v1:2603.15690 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15690 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15690 | no |
| SF-2026-ARXIV-2603-15714 | arXiv:2603.15714v1 | paper-v1:2603.15714 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15714 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15714 | no |
| SF-2026-ARXIV-2603-15727 | arXiv:2603.15727v1 | paper-v1:2603.15727 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15727 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15727 | no |
| SF-2026-ARXIV-2603-15798 | arXiv:2603.15798v1 | paper-v1:2603.15798 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15798 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15798 | no |
| SF-2026-ARXIV-2603-15973 | arXiv:2603.15973v1 | paper-v1:2603.15973 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-15973 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15973 | no |
| SF-2026-ARXIV-2603-16013 | arXiv:2603.16013v1 | paper-v1:2603.16013 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16013 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16013 | no |
| SF-2026-ARXIV-2603-16104 | arXiv:2603.16104v1 | paper-v1:2603.16104 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16104 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16104 | no |
| SF-2026-ARXIV-2603-16158 | arXiv:2603.16158v1 | paper-v1:2603.16158 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16158 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16158 | no |
| SF-2026-ARXIV-2603-16435 | arXiv:2603.16435v1 | paper-v1:2603.16435 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16435 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16435 | no |
| SF-2026-ARXIV-2603-16572 | arXiv:2603.16572v1 | paper-v1:2603.16572 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16572 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16572 | no |
| SF-2026-ARXIV-2603-16586 | arXiv:2603.16586v1 | paper-v1:2603.16586 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16586 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16586 | no |
| SF-2026-ARXIV-2603-16731 | arXiv:2603.16731v1 | paper-v1:2603.16731 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16731 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16731 | no |
| SF-2026-ARXIV-2603-16817 | arXiv:2603.16817v1 | paper-v1:2603.16817 | 2026-W12 | 2026-03-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16817 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16817 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-15690 | RP-1f34ec6c782089aa | deep | arXiv:2603.15690v1 | SRC-ARXIV@arXiv:2603.15690v1 | arXiv:2603.15690v1 HTML — §4.2. Design Patterns [facet=method]; https://arxiv.org/html/2603.15690v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15690v1.html; sha256:88053af6106cb2e65e058690dd9207297df0dfe1add34e377f6d8d236a79fafd | arXiv:2603.15690v1 HTML — §8.1. Evaluation on RepoBench-R [facet=evaluation]; https://arxiv.org/html/2603.15690v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15690v1.html; sha256:88053af6106cb2e65e058690dd9207297df0dfe1add34e377f6d8d236a79fafd | arXiv:2603.15690v1 HTML — §9. Conclusion [facet=limitations]; https://arxiv.org/html/2603.15690v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15690v1.html; sha256:88053af6106cb2e65e058690dd9207297df0dfe1add34e377f6d8d236a79fafd | arXiv exact-v1 identity https://arxiv.org/abs/2603.15690v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15690 | complete |
| SF-2026-ARXIV-2603-15714 | RP-c5b027bac9110a1a | deep | arXiv:2603.15714v1 | SRC-ARXIV@arXiv:2603.15714v1 | arXiv:2603.15714v1 HTML — §Red-Teaming Methodologies. [facet=method]; https://arxiv.org/html/2603.15714v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15714v1.html; sha256:6e1ba9544ecdb61f79578fee500ed3a7ac045dd4a0223bb1aaad158a37af2ae5 | arXiv:2603.15714v1 HTML — §3.2 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15714v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15714v1.html; sha256:6e1ba9544ecdb61f79578fee500ed3a7ac045dd4a0223bb1aaad158a37af2ae5 | arXiv:2603.15714v1 HTML — §Threat Model. [facet=limitations]; https://arxiv.org/html/2603.15714v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15714v1.html; sha256:6e1ba9544ecdb61f79578fee500ed3a7ac045dd4a0223bb1aaad158a37af2ae5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.15714v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15714 | complete |
| SF-2026-ARXIV-2603-15727 | RP-38898f5d1cfbe849 | deep | arXiv:2603.15727v1 | SRC-ARXIV@arXiv:2603.15727v1 | arXiv:2603.15727v1 HTML — §Testbed architecture. [facet=method]; https://arxiv.org/html/2603.15727v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15727v1.html; sha256:9daefcfaeb9a2ea1c3a22077e87104c2ce55f5a0f8fbe08ba0cba6e60c200ee7 | arXiv:2603.15727v1 HTML — §5.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.15727v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15727v1.html; sha256:9daefcfaeb9a2ea1c3a22077e87104c2ce55f5a0f8fbe08ba0cba6e60c200ee7 | arXiv:2603.15727v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.15727v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15727v1.html; sha256:9daefcfaeb9a2ea1c3a22077e87104c2ce55f5a0f8fbe08ba0cba6e60c200ee7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.15727v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15727 | complete |
| SF-2026-ARXIV-2603-15798 | RP-15f2ad1d78201609 | deep | arXiv:2603.15798v1 | SRC-ARXIV@arXiv:2603.15798v1 | arXiv:2603.15798v1 HTML — §3.5 Python-First Design with RPC Fallback [facet=method]; https://arxiv.org/html/2603.15798v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15798v1.html; sha256:ffb4381df3f40fd5c9318582eead42667232c1780dab1a14cc003ddfc8857a71 | arXiv:2603.15798v1 HTML — §3.2 Benchmark-Level Interface [facet=evaluation]; https://arxiv.org/html/2603.15798v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15798v1.html; sha256:ffb4381df3f40fd5c9318582eead42667232c1780dab1a14cc003ddfc8857a71 | arXiv:2603.15798v1 HTML — §Lighter-Weight Alternatives [facet=limitations]; https://arxiv.org/html/2603.15798v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15798v1.html; sha256:ffb4381df3f40fd5c9318582eead42667232c1780dab1a14cc003ddfc8857a71 | arXiv exact-v1 identity https://arxiv.org/abs/2603.15798v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15798 | complete |
| SF-2026-ARXIV-2603-15973 | RP-df4a81f4bf970864 | deep | arXiv:2603.15973v1 | SRC-ARXIV@arXiv:2603.15973v1 | arXiv:2603.15973v1 PDF — §Algorithm 1 Capability Closure (Optimised Worklist) [facet=method]; https://arxiv.org/pdf/2603.15973v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15973v1.pdf.txt; sha256:55a02fb412e950fe48bb2af8c47032d898f6212bfdbebf0920ca71d9fda6265b | arXiv:2603.15973v1 PDF — §results in the Safe Audit Surface Theorem (Theorem 10.1)—a polynomial-time-computable, [facet=evaluation]; https://arxiv.org/pdf/2603.15973v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15973v1.pdf.txt; sha256:55a02fb412e950fe48bb2af8c47032d898f6212bfdbebf0920ca71d9fda6265b | arXiv:2603.15973v1 PDF — §Discussion [facet=limitations]; https://arxiv.org/pdf/2603.15973v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15973v1.pdf.txt; sha256:55a02fb412e950fe48bb2af8c47032d898f6212bfdbebf0920ca71d9fda6265b | arXiv exact-v1 identity https://arxiv.org/abs/2603.15973v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-15973 | complete |
| SF-2026-ARXIV-2603-16013 | RP-eb692d5a7771e17d | deep | arXiv:2603.16013v1 | SRC-ARXIV@arXiv:2603.16013v1 | arXiv:2603.16013v1 HTML — §3.1 Overview [facet=method]; https://arxiv.org/html/2603.16013v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16013v1.html; sha256:110d0c2752ca513490150b5c54a30cbbbb046f33b97c7af1d460f442687ac0a1 | arXiv:2603.16013v1 HTML — §4.1 Key Takeaways [facet=evaluation]; https://arxiv.org/html/2603.16013v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16013v1.html; sha256:110d0c2752ca513490150b5c54a30cbbbb046f33b97c7af1d460f442687ac0a1 | arXiv:2603.16013v1 HTML — §4.2 Threats to Validity [facet=limitations]; https://arxiv.org/html/2603.16013v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16013v1.html; sha256:110d0c2752ca513490150b5c54a30cbbbb046f33b97c7af1d460f442687ac0a1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.16013v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16013 | complete |
| SF-2026-ARXIV-2603-16104 | RP-8560e27826fa46d1 | deep | arXiv:2603.16104v1 | SRC-ARXIV@arXiv:2603.16104v1 | arXiv:2603.16104v1 HTML — §3. System Overview [facet=method]; https://arxiv.org/html/2603.16104v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16104v1.html; sha256:39314f43505f4971bcab3fb875e81da1dbe43bdd869a2de50d361973b4cc6393 | arXiv:2603.16104v1 HTML — §7. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.16104v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16104v1.html; sha256:39314f43505f4971bcab3fb875e81da1dbe43bdd869a2de50d361973b4cc6393 | arXiv:2603.16104v1 HTML — §9. Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.16104v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16104v1.html; sha256:39314f43505f4971bcab3fb875e81da1dbe43bdd869a2de50d361973b4cc6393 | arXiv exact-v1 identity https://arxiv.org/abs/2603.16104v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16104 | complete |
| SF-2026-ARXIV-2603-16158 | RP-2dbac5ad1b3dbe6f | deep | arXiv:2603.16158v1 | SRC-ARXIV@arXiv:2603.16158v1 | arXiv:2603.16158v1 HTML — §4.2 Training Setup and Implementation Details [facet=method]; https://arxiv.org/html/2603.16158v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16158v1.html; sha256:b02301fdd379e8d2c7cb079b53dd8ac286fcd48f5335decf87b1cf6fca39e6cc | arXiv:2603.16158v1 HTML — §4.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.16158v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16158v1.html; sha256:b02301fdd379e8d2c7cb079b53dd8ac286fcd48f5335decf87b1cf6fca39e6cc | arXiv:2603.16158v1 HTML — §5 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.16158v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16158v1.html; sha256:b02301fdd379e8d2c7cb079b53dd8ac286fcd48f5335decf87b1cf6fca39e6cc | arXiv exact-v1 identity https://arxiv.org/abs/2603.16158v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16158 | complete |
| SF-2026-ARXIV-2603-16435 | RP-0ff82d278fc63c1c | deep | arXiv:2603.16435v1 | SRC-ARXIV@arXiv:2603.16435v1 | arXiv:2603.16435v1 HTML — §3 Compressing KV with Vector Quantization [facet=method]; https://arxiv.org/html/2603.16435v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16435v1.html; sha256:bf3b31c12771633e661b24e5e856641af9cf27e228592dcbd510ce6bf5330900 | arXiv:2603.16435v1 HTML — §4.2 Long-Context Evaluation [facet=evaluation]; https://arxiv.org/html/2603.16435v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16435v1.html; sha256:bf3b31c12771633e661b24e5e856641af9cf27e228592dcbd510ce6bf5330900 | arXiv:2603.16435v1 HTML — §6 Limitations [facet=limitations]; https://arxiv.org/html/2603.16435v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16435v1.html; sha256:bf3b31c12771633e661b24e5e856641af9cf27e228592dcbd510ce6bf5330900 | arXiv exact-v1 identity https://arxiv.org/abs/2603.16435v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16435 | complete |
| SF-2026-ARXIV-2603-16572 | RP-da34ab60a38cbcbe | deep | arXiv:2603.16572v1 | SRC-ARXIV@arXiv:2603.16572v1 | arXiv:2603.16572v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.16572v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16572v1.html; sha256:074d2216d51efc9978e7f84b3c9ca1f29ea33e1d382da17591b6a98803f5da0a | arXiv:2603.16572v1 HTML — §3.3 Repository-Aware Analysis [facet=evaluation]; https://arxiv.org/html/2603.16572v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16572v1.html; sha256:074d2216d51efc9978e7f84b3c9ca1f29ea33e1d382da17591b6a98803f5da0a | arXiv:2603.16572v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.16572v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16572v1.html; sha256:074d2216d51efc9978e7f84b3c9ca1f29ea33e1d382da17591b6a98803f5da0a | arXiv exact-v1 identity https://arxiv.org/abs/2603.16572v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16572 | complete |
| SF-2026-ARXIV-2603-16586 | RP-cf4e92deacd9ad24 | deep | arXiv:2603.16586v1 | SRC-ARXIV@arXiv:2603.16586v1 | arXiv:2603.16586v1 HTML — §3 A Formal Framework for Agent Governance [facet=method]; https://arxiv.org/html/2603.16586v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16586v1.html; sha256:e194938486e880b9eb0585c85bf5ea26eb031bd1904bb78c82713cec52f8d8fd | arXiv:2603.16586v1 HTML — §4.4 Concrete intervention outcomes [facet=evaluation]; https://arxiv.org/html/2603.16586v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16586v1.html; sha256:e194938486e880b9eb0585c85bf5ea26eb031bd1904bb78c82713cec52f8d8fd | arXiv:2603.16586v1 HTML — §4.6 Challenges [facet=limitations]; https://arxiv.org/html/2603.16586v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16586v1.html; sha256:e194938486e880b9eb0585c85bf5ea26eb031bd1904bb78c82713cec52f8d8fd | arXiv exact-v1 identity https://arxiv.org/abs/2603.16586v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16586 | complete |
| SF-2026-ARXIV-2603-16731 | RP-49d400d32ddb3f5a | deep | arXiv:2603.16731v1 | SRC-ARXIV@arXiv:2603.16731v1 | arXiv:2603.16731v1 HTML — §A.11 Algorithms [facet=method]; https://arxiv.org/html/2603.16731v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16731v1.html; sha256:7dc0de3d3deb0f40fc608bcfa5318050b130de30a50a5c37f771b72235daa34c | arXiv:2603.16731v1 HTML — §6.2 Results [facet=evaluation]; https://arxiv.org/html/2603.16731v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16731v1.html; sha256:7dc0de3d3deb0f40fc608bcfa5318050b130de30a50a5c37f771b72235daa34c | arXiv:2603.16731v1 HTML — §8 Limitations [facet=limitations]; https://arxiv.org/html/2603.16731v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16731v1.html; sha256:7dc0de3d3deb0f40fc608bcfa5318050b130de30a50a5c37f771b72235daa34c | arXiv exact-v1 identity https://arxiv.org/abs/2603.16731v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16731 | complete |
| SF-2026-ARXIV-2603-16817 | RP-2938b142d6e63d00 | deep | arXiv:2603.16817v1 | SRC-ARXIV@arXiv:2603.16817v1 | arXiv:2603.16817v1 HTML — §4 Design Choices for Factuality Scoring in Conformal Filtering [facet=method]; https://arxiv.org/html/2603.16817v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16817v1.html; sha256:601125574af4cab66c56ba8b6f2bbdbcd57a88c0d9280356e647f549f97374f0 | arXiv:2603.16817v1 HTML — §6 Efficiency Evaluation of the Conformal Factuality Pipeline End-to-End [facet=evaluation]; https://arxiv.org/html/2603.16817v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16817v1.html; sha256:601125574af4cab66c56ba8b6f2bbdbcd57a88c0d9280356e647f549f97374f0 | arXiv:2603.16817v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.16817v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16817v1.html; sha256:601125574af4cab66c56ba8b6f2bbdbcd57a88c0d9280356e647f549f97374f0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.16817v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16817 | complete |

### Source Reviews

### Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems

<!-- review:SF-2026-ARXIV-2603-15690:start -->
**问题**：运行时可重接线的多 agent 软件会让上下文、结构与演化历史共同决定行为，传统静态代码边界不足以解释漂移。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：论文把 context artifact、semantic lens、index generator 与 evolution entropy 组合为显式工程对象，使 rewiring 的来源和结构变化可追踪。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.15690v1 HTML — §4.2. Design Patterns [facet=method]; https://arxiv.org/html/2603.15690v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15690v1.html; sha256:88053af6106cb2e65e058690dd9207297df0dfe1add34e377f6d8d236a79fafd`。

**Evaluation contract 与未证明部分**：RepoBench-R 只验证其中语义检索与索引机制，不能证明整套 loosely-structured software 治理在生产多 agent 系统中有效。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15690v1 HTML — §8.1. Evaluation on RepoBench-R [facet=evaluation]; https://arxiv.org/html/2603.15690v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15690v1.html; sha256:88053af6106cb2e65e058690dd9207297df0dfe1add34e377f6d8d236a79fafd`。

**Trade-off / failure / coexistence**：结构显式化提高可诊断性，却引入额外索引和版本状态；规模小、拓扑固定的 agent graph 仍适合普通代码配置。

<!-- claim:SF-2026-ARXIV-2603-15690:start -->**Claim Boundary**：只支持 arXiv:2603.15690v1 §4.2. Design Patterns 的机制与 §8.1. Evaluation on RepoBench-R 的公开 workload；§9. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15690:end -->
<!-- review:SF-2026-ARXIV-2603-15690:end -->
### How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition

<!-- review:SF-2026-ARXIV-2603-15714:start -->
**问题**：间接 prompt injection 通过环境内容进入 agent，单轮拒答或静态 jailbreak benchmark 无法覆盖实际工具路径。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：工作从公开竞赛记录恢复攻击与防御路径，将成功条件绑定到 agent 对不可信内容的读取、指令采纳和工具执行链。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.15714v1 HTML — §Red-Teaming Methodologies. [facet=method]; https://arxiv.org/html/2603.15714v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15714v1.html; sha256:6e1ba9544ecdb61f79578fee500ed3a7ac045dd4a0223bb1aaad158a37af2ae5`。

**Evaluation contract 与未证明部分**：大规模竞赛提供现实攻击多样性，但参与者选择、赛题环境和评分规则限制了对其他 agent stack 的外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15714v1 HTML — §3.2 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.15714v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15714v1.html; sha256:6e1ba9544ecdb61f79578fee500ed3a7ac045dd4a0223bb1aaad158a37af2ae5`。

**Trade-off / failure / coexistence**：真实路径证据优于合成单轮测试；代价是数据分布不可控且难区分模型弱点、工具权限和 orchestration 缺陷。

<!-- claim:SF-2026-ARXIV-2603-15714:start -->**Claim Boundary**：只支持 arXiv:2603.15714v1 §Red-Teaming Methodologies. 的机制与 §3.2 Evaluation 的公开 workload；§Threat Model. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15714:end -->
<!-- review:SF-2026-ARXIV-2603-15714:end -->
### AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems

<!-- review:SF-2026-ARXIV-2603-15727:start -->
**问题**：长驻 agent 具有持久配置、消息传播与工具权限，恶意指令因此可以像 worm 一样跨实例复制。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：AgentWorm 展示单消息触发的自主感染链，把传播载荷、持久化和跨平台发送连成系统攻击路径。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.15727v1 HTML — §Testbed architecture. [facet=method]; https://arxiv.org/html/2603.15727v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15727v1.html; sha256:9daefcfaeb9a2ea1c3a22077e87104c2ce55f5a0f8fbe08ba0cba6e60c200ee7`。

**Evaluation contract 与未证明部分**：证据来自特定生产型 agent framework 与实验部署；不代表所有平台可被同一载荷感染。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15727v1 HTML — §5.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.15727v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15727v1.html; sha256:9daefcfaeb9a2ea1c3a22077e87104c2ce55f5a0f8fbe08ba0cba6e60c200ee7`。

**Trade-off / failure / coexistence**：阻断传播需要能力隔离、消息 provenance 与速率限制，并会牺牲开放协作。

<!-- claim:SF-2026-ARXIV-2603-15727:start -->**Claim Boundary**：只支持 arXiv:2603.15727v1 §Testbed architecture. 的机制与 §5.3 Main Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15727:end -->
<!-- review:SF-2026-ARXIV-2603-15727:end -->
### CUBE: A Standard for Unifying Agent Benchmarks

<!-- review:SF-2026-ARXIV-2603-15798:start -->
**问题**：每个 agent benchmark 都自带环境、task 和 runner API，新增模型需要重复适配，跨基准结果难复算。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：CUBE 用 MCP/Gym 风格协议拆分 task、benchmark、package 和 registry，使环境包装与 agent implementation 独立。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.15798v1 HTML — §3.5 Python-First Design with RPC Fallback [facet=method]; https://arxiv.org/html/2603.15798v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15798v1.html; sha256:ffb4381df3f40fd5c9318582eead42667232c1780dab1a14cc003ddfc8857a71`。

**Evaluation contract 与未证明部分**：原型集成展示协议互操作性，不证明指标本身有效或所有环境语义都可统一。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15798v1 HTML — §3.2 Benchmark-Level Interface [facet=evaluation]; https://arxiv.org/html/2603.15798v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15798v1.html; sha256:ffb4381df3f40fd5c9318582eead42667232c1780dab1a14cc003ddfc8857a71`。

**Trade-off / failure / coexistence**：标准层减少 integration tax，却引入版本兼容和最低公分母风险；单 benchmark 可保持原生 API。

<!-- claim:SF-2026-ARXIV-2603-15798:start -->**Claim Boundary**：只支持 arXiv:2603.15798v1 §3.5 Python-First Design with RPC Fallback 的机制与 §3.2 Benchmark-Level Interface 的公开 workload；§Lighter-Weight Alternatives 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15798:end -->
<!-- review:SF-2026-ARXIV-2603-15798:end -->
### Safety is Non-Compositional: A Formal Framework for Capability-Based AI Systems

<!-- review:SF-2026-ARXIV-2603-15973:start -->
**问题**：逐 agent capability check 假设安全属性可组合，但两个各自无害能力可能通过 conjunctive dependency 共同到达禁用状态。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文用 capability graph 与组合规则证明 non-compositionality，并要求 governance 在联合可达状态而非单主体权限上判断。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.15973v1 PDF — §Algorithm 1 Capability Closure (Optimised Worklist) [facet=method]; https://arxiv.org/pdf/2603.15973v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15973v1.pdf.txt; sha256:55a02fb412e950fe48bb2af8c47032d898f6212bfdbebf0920ca71d9fda6265b`。

**Evaluation contract 与未证明部分**：形式化证明只在定义的 dependency semantics 内成立，没有给出开放生态的完整依赖发现机制。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.15973v1 PDF — §results in the Safe Audit Surface Theorem (Theorem 10.1)—a polynomial-time-computable, [facet=evaluation]; https://arxiv.org/pdf/2603.15973v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.15973v1.pdf.txt; sha256:55a02fb412e950fe48bb2af8c47032d898f6212bfdbebf0920ca71d9fda6265b`。

**Trade-off / failure / coexistence**：联合分析组合爆炸且可能过度拒绝；能力确实独立时局部检查仍充分。

<!-- claim:SF-2026-ARXIV-2603-15973:start -->**Claim Boundary**：只支持 arXiv:2603.15973v1 §Algorithm 1 Capability Closure (Optimised Worklist) 的机制与 §results in the Safe Audit Surface Theorem (Theorem 10.1)—a polynomial-time-computable, 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-15973:end -->
<!-- review:SF-2026-ARXIV-2603-15973:end -->
### Safety Case Patterns for VLA-based driving systems: Insights from SimLingo

<!-- review:SF-2026-ARXIV-2603-16013:start -->
**问题**：VLA 驾驶把开放语言接入物理控制，传统感知/规划 safety case 无法覆盖指令诱发的危险。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：论文用 SimLingo 提炼 safety-case patterns，将语言输入、action generation、monitor 与 fallback 对应到可审查 assurance claim。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.16013v1 HTML — §3.1 Overview [facet=method]; https://arxiv.org/html/2603.16013v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16013v1.html; sha256:110d0c2752ca513490150b5c54a30cbbbb046f33b97c7af1d460f442687ac0a1`。

**Evaluation contract 与未证明部分**：它提供案例化模式而非统计安全证明；模拟证据不能直接替代道路验证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16013v1 HTML — §4.1 Key Takeaways [facet=evaluation]; https://arxiv.org/html/2603.16013v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16013v1.html; sha256:110d0c2752ca513490150b5c54a30cbbbb046f33b97c7af1d460f442687ac0a1`。

**Trade-off / failure / coexistence**：更完整 assurance 增加 hazard analysis 和 runtime monitor 成本；封闭指令集可采用更简单 contract。

<!-- claim:SF-2026-ARXIV-2603-16013:start -->**Claim Boundary**：只支持 arXiv:2603.16013v1 §3.1 Overview 的机制与 §4.1 Key Takeaways 的公开 workload；§4.2 Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16013:end -->
<!-- review:SF-2026-ARXIV-2603-16013:end -->
### Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective

<!-- review:SF-2026-ARXIV-2603-16104:start -->
**问题**：agent workflow 的多个 LLM call 具有依赖关系和重叠中间状态，按独立请求调度会浪费 prefix/KV 并放大尾延迟。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Helium 把 workflow dependency 与中间结果纳入数据系统，联合执行 cache-aware routing、共享状态复用与 workflow-level scheduling。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.16104v1 HTML — §3. System Overview [facet=method]; https://arxiv.org/html/2603.16104v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16104v1.html; sha256:39314f43505f4971bcab3fb875e81da1dbe43bdd869a2de50d361973b4cc6393`。

**Evaluation contract 与未证明部分**：评测覆盖公开 agent workflow，能支持局部 cache/scheduling 收益；作者也明确当前设计优先 locality，尚未证明动态负载下的公平性与隔离。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16104v1 HTML — §7. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.16104v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16104v1.html; sha256:39314f43505f4971bcab3fb875e81da1dbe43bdd869a2de50d361973b4cc6393`。

**Trade-off / failure / coexistence**：共享提高命中率却增加跨步骤 identity、失效和 admission 复杂度；无依赖的普通在线请求仍应走独立调度。

<!-- claim:SF-2026-ARXIV-2603-16104:start -->**Claim Boundary**：只支持 arXiv:2603.16104v1 §3. System Overview 的机制与 §7. Evaluation 的公开 workload；§9. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16104:end -->
<!-- review:SF-2026-ARXIV-2603-16104:end -->
### Execution-Grounded Credit Assignment for GRPO in Code Generation

<!-- review:SF-2026-ARXIV-2603-16158:start -->
**问题**：代码 RLVR 把单个测试结果均匀分给整段程序，局部语义错误会污染无关 token 的梯度。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：EGCA 对候选与参考程序做同仪器执行，定位首次状态分歧并把 GRPO credit 聚焦到相关片段。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.16158v1 HTML — §4.2 Training Setup and Implementation Details [facet=method]; https://arxiv.org/html/2603.16158v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16158v1.html; sha256:b02301fdd379e8d2c7cb079b53dd8ac286fcd48f5335decf87b1cf6fca39e6cc`。

**Evaluation contract 与未证明部分**：实验支持所测编程任务的 credit efficiency；依赖可执行 reference 和 instrumentation，不覆盖无 oracle 任务。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16158v1 HTML — §4.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.16158v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16158v1.html; sha256:b02301fdd379e8d2c7cb079b53dd8ac286fcd48f5335decf87b1cf6fca39e6cc`。

**Trade-off / failure / coexistence**：更细 credit 需要执行跟踪且 reference 偏差会误导学习；短程序仍可使用 outcome reward。

<!-- claim:SF-2026-ARXIV-2603-16158:start -->**Claim Boundary**：只支持 arXiv:2603.16158v1 §4.2 Training Setup and Implementation Details 的机制与 §4.4 Main Results 的公开 workload；§5 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16158:end -->
<!-- review:SF-2026-ARXIV-2603-16158:end -->
### VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization

<!-- review:SF-2026-ARXIV-2603-16435:start -->
**问题**：逐 token、逐 head 保留完整 KV 在长上下文和高并发下成为容量瓶颈，而简单低维投影容易损失相关结构。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：VQKV 用 vector quantization 对 KV 的联合结构编码，以可复用 codebook 换取更高压缩比，并保持训练外部署路径。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.16435v1 HTML — §3 Compressing KV with Vector Quantization [facet=method]; https://arxiv.org/html/2603.16435v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16435v1.html; sha256:bf3b31c12771633e661b24e5e856641af9cf27e228592dcbd510ce6bf5330900`。

**Evaluation contract 与未证明部分**：论文在多模型与下游任务上比较相同压缩预算；结果只说明这些模型/任务下的 fidelity，不证明所有注意力层都可同等量化。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16435v1 HTML — §4.2 Long-Context Evaluation [facet=evaluation]; https://arxiv.org/html/2603.16435v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16435v1.html; sha256:bf3b31c12771633e661b24e5e856641af9cf27e228592dcbd510ce6bf5330900`。

**Trade-off / failure / coexistence**：codebook 查找与量化误差成为新成本；短上下文、严格 exactness 或内存充足时完整 KV 仍是稳健基线。

<!-- claim:SF-2026-ARXIV-2603-16435:start -->**Claim Boundary**：只支持 arXiv:2603.16435v1 §3 Compressing KV with Vector Quantization 的机制与 §4.2 Long-Context Evaluation 的公开 workload；§6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16435:end -->
<!-- review:SF-2026-ARXIV-2603-16435:end -->
### Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem

<!-- review:SF-2026-ARXIV-2603-16572:start -->
**问题**：agent skill 扫描若脱离 repository 上下文，会把示例、测试或声明性能力误判为恶意行为。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：研究在跨 marketplace 的 238,180 个去重 skill 上联合分析文件内容、行为和仓库语境，重新定义生态风险分母。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.16572v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.16572v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16572v1.html; sha256:074d2216d51efc9978e7f84b3c9ca1f29ea33e1d382da17591b6a98803f5da0a`。

**Evaluation contract 与未证明部分**：证据可支持该采样快照的分类差异，不证明未收录私有 skill 的风险率。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16572v1 HTML — §3.3 Repository-Aware Analysis [facet=evaluation]; https://arxiv.org/html/2603.16572v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16572v1.html; sha256:074d2216d51efc9978e7f84b3c9ca1f29ea33e1d382da17591b6a98803f5da0a`。

**Trade-off / failure / coexistence**：上下文分析降低误报却提高抓取和执行风险；高置信 signature 仍适合快速阻断。

<!-- claim:SF-2026-ARXIV-2603-16572:start -->**Claim Boundary**：只支持 arXiv:2603.16572v1 §3 Methodology 的机制与 §3.3 Repository-Aware Analysis 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16572:end -->
<!-- review:SF-2026-ARXIV-2603-16572:end -->
### Runtime Governance for AI Agents: Policies on Paths

<!-- review:SF-2026-ARXIV-2603-16586:start -->
**问题**：对单次 action 做 allow/deny 无法表达 agent 路径中先前授权、累计风险与状态变化。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文把 governance 定义为作用在 action path、principal、当前 state 与历史摘要上的 policy function，使每个执行边都有可判定的策略状态。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.16586v1 HTML — §3 A Formal Framework for Agent Governance [facet=method]; https://arxiv.org/html/2603.16586v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16586v1.html; sha256:e194938486e880b9eb0585c85bf5ea26eb031bd1904bb78c82713cec52f8d8fd`。

**Evaluation contract 与未证明部分**：exact-v1 主要给出形式化与现有机制的缺口分析，没有独立系统实验；因此它提供设计合同，而非性能或防护效果证据。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16586v1 HTML — §4.4 Concrete intervention outcomes [facet=evaluation]; https://arxiv.org/html/2603.16586v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16586v1.html; sha256:e194938486e880b9eb0585c85bf5ea26eb031bd1904bb78c82713cec52f8d8fd`。

**Trade-off / failure / coexistence**：路径策略提高可表达性但带来 state reconstruction 和 policy conflict；无持久状态的单工具调用仍可使用普通 capability check。

<!-- claim:SF-2026-ARXIV-2603-16586:start -->**Claim Boundary**：只支持 arXiv:2603.16586v1 §3 A Formal Framework for Agent Governance 的机制与 §4.4 Concrete intervention outcomes 的公开 workload；§4.6 Challenges 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16586:end -->
<!-- review:SF-2026-ARXIV-2603-16586:end -->
### Understanding Quantization of Optimizer States in LLM Pre-training: Dynamics of State Staleness and Effectiveness of State Resets

<!-- review:SF-2026-ARXIV-2603-16731:start -->
**问题**：量化 optimizer state 不只是存储误差：EMA 更新会积累 stale state，使长期训练动力学发生偏移。

**旧路径为何合理**：统一精度和静态 optimizer state 使收敛分析最直接。

**约束变化与机制**：工作把量化、反量化与 EMA reset 写进 optimizer 更新，并比较周期性重置能否清除累积陈旧性。

**State / data / control owner**：`TRAIN-PRETRAINING` 负责 optimizer/data state 的精度、更新与恢复边界；定位证据为 `arXiv:2603.16731v1 HTML — §A.11 Algorithms [facet=method]; https://arxiv.org/html/2603.16731v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16731v1.html; sha256:7dc0de3d3deb0f40fc608bcfa5318050b130de30a50a5c37f771b72235daa34c`。

**Evaluation contract 与未证明部分**：多种低精度 regime 的训练实验支持 state reset 的条件性收益；没有覆盖的模型规模、优化器和长训练 horizon 不能外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16731v1 HTML — §6.2 Results [facet=evaluation]; https://arxiv.org/html/2603.16731v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16731v1.html; sha256:7dc0de3d3deb0f40fc608bcfa5318050b130de30a50a5c37f771b72235daa34c`。

**Trade-off / failure / coexistence**：重置恢复新鲜度但会丢失动量历史并引入调参；显存允许或稳定性优先时高精度 optimizer state 仍更可靠。

<!-- claim:SF-2026-ARXIV-2603-16731:start -->**Claim Boundary**：只支持 arXiv:2603.16731v1 §A.11 Algorithms 的机制与 §6.2 Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16731:end -->
<!-- review:SF-2026-ARXIV-2603-16731:end -->
### Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights

<!-- review:SF-2026-ARXIV-2603-16817:start -->
**问题**：conformal factuality 可控制 claim-level error，但过滤后输出可能失去足够信息，单看 coverage 会高估可用性。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文联合测量统计可靠性与 informativeness，并挑战 calibration shift、retrieval 质量和 claim 分解对保证的影响。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.16817v1 HTML — §4 Design Choices for Factuality Scoring in Conformal Filtering [facet=method]; https://arxiv.org/html/2603.16817v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16817v1.html; sha256:601125574af4cab66c56ba8b6f2bbdbcd57a88c0d9280356e647f549f97374f0`。

**Evaluation contract 与未证明部分**：结论受数据可交换性、scorer 与 atomic-claim protocol 限制；不等于现实回答天然拥有概率置信度。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16817v1 HTML — §6 Efficiency Evaluation of the Conformal Factuality Pipeline End-to-End [facet=evaluation]; https://arxiv.org/html/2603.16817v1; papers/2026/03/_sources/daily-20260318/exact-v1-bodies/2603.16817v1.html; sha256:601125574af4cab66c56ba8b6f2bbdbcd57a88c0d9280356e647f549f97374f0`。

**Trade-off / failure / coexistence**：更保守阈值减少错误也会删掉更多有用内容；低风险场景可接受较松过滤。

<!-- claim:SF-2026-ARXIV-2603-16817:start -->**Claim Boundary**：只支持 arXiv:2603.16817v1 §4 Design Choices for Factuality Scoring in Conformal Filtering 的机制与 §6 Efficiency Evaluation of the Conformal Factuality Pipeline End-to-End 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16817:end -->
<!-- review:SF-2026-ARXIV-2603-16817:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-15690 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15690 |
| SF-2026-ARXIV-2603-15714 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15714 |
| SF-2026-ARXIV-2603-15727 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15727 |
| SF-2026-ARXIV-2603-15798 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-15798 |
| SF-2026-ARXIV-2603-15973 | score_7_9 | selected | DA-20260318-05 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260318-05 |
| SF-2026-ARXIV-2603-16013 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16013 |
| SF-2026-ARXIV-2603-16104 | score_7_9 | selected | DA-20260318-07 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260318-07 |
| SF-2026-ARXIV-2603-16158 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16158 |
| SF-2026-ARXIV-2603-16435 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16435 |
| SF-2026-ARXIV-2603-16572 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16572 |
| SF-2026-ARXIV-2603-16586 | score_7_9 | selected | DA-20260318-11 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260318-11 |
| SF-2026-ARXIV-2603-16731 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16731 |
| SF-2026-ARXIV-2603-16817 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16817 |

<!-- analysis-decision:SF-2026-ARXIV-2603-15690:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15690:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-15714:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15714:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-15727:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15727:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-15798:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-15798:end -->
<!-- analysis:DA-20260318-05:start -->
### Safety is Non-Compositional: A Formal Framework for Capability-Based AI Systems

逐 agent capability check 假设安全属性可组合，但两个各自无害能力可能通过 conjunctive dependency 共同到达禁用状态。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：论文用 capability graph 与组合规则证明 non-compositionality，并要求 governance 在联合可达状态而非单主体权限上判断。 其公开验证边界为：形式化证明只在定义的 dependency semantics 内成立，没有给出开放生态的完整依赖发现机制。 新增代价与回退条件为：联合分析组合爆炸且可能过度拒绝；能力确实独立时局部检查仍充分。
<!-- analysis:DA-20260318-05:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16013:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16013:end -->
<!-- analysis:DA-20260318-07:start -->
### Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective

agent workflow 的多个 LLM call 具有依赖关系和重叠中间状态，按独立请求调度会浪费 prefix/KV 并放大尾延迟。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：Helium 把 workflow dependency 与中间结果纳入数据系统，联合执行 cache-aware routing、共享状态复用与 workflow-level scheduling。 其公开验证边界为：评测覆盖公开 agent workflow，能支持局部 cache/scheduling 收益；作者也明确当前设计优先 locality，尚未证明动态负载下的公平性与隔离。 新增代价与回退条件为：共享提高命中率却增加跨步骤 identity、失效和 admission 复杂度；无依赖的普通在线请求仍应走独立调度。
<!-- analysis:DA-20260318-07:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16158:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16158:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16435:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16435:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16572:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16572:end -->
<!-- analysis:DA-20260318-11:start -->
### Runtime Governance for AI Agents: Policies on Paths

对单次 action 做 allow/deny 无法表达 agent 路径中先前授权、累计风险与状态变化。 旧路径在其原约束下仍合理：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。 本 family 的设计变化是：论文把 governance 定义为作用在 action path、principal、当前 state 与历史摘要上的 policy function，使每个执行边都有可判定的策略状态。 其公开验证边界为：exact-v1 主要给出形式化与现有机制的缺口分析，没有独立系统实验；因此它提供设计合同，而非性能或防护效果证据。 新增代价与回退条件为：路径策略提高可表达性但带来 state reconstruction 和 policy conflict；无持久状态的单工具调用仍可使用普通 capability check。
<!-- analysis:DA-20260318-11:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16731:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16731:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-16817:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16817:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-15690 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#failure-attribution、perception-routing-与-sticky-state-ownership (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15690 | delta:SF-2026-ARXIV-2603-15690 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15690 |
| SF-2026-ARXIV-2603-15714 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#capability-access-control-可以前移到训练状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15714 | delta:SF-2026-ARXIV-2603-15714 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15714 |
| SF-2026-ARXIV-2603-15727 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#agent-自己的-instruction、config-与-memory-也是受保护资产 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15727 | delta:SF-2026-ARXIV-2603-15727 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15727 |
| SF-2026-ARXIV-2603-15798 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15798 | delta:SF-2026-ARXIV-2603-15798 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15798 |
| SF-2026-ARXIV-2603-15973 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-15973 | delta:SF-2026-ARXIV-2603-15973 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-15973 |
| SF-2026-ARXIV-2603-16013 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#streaming-vla-必须版本化-observation、buffer-与-control-deadline (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16013 | delta:SF-2026-ARXIV-2603-16013 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16013 |
| SF-2026-ARXIV-2603-16104 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16104 | delta:SF-2026-ARXIV-2603-16104 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16104 |
| SF-2026-ARXIV-2603-16158 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#measurement-也是-reward-interface-的一部分 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16158 | delta:SF-2026-ARXIV-2603-16158 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16158 |
| SF-2026-ARXIV-2603-16435 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16435 | delta:SF-2026-ARXIV-2603-16435 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16435 |
| SF-2026-ARXIV-2603-16572 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16572 | delta:SF-2026-ARXIV-2603-16572 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16572 |
| SF-2026-ARXIV-2603-16586 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16586 | delta:SF-2026-ARXIV-2603-16586 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16586 |
| SF-2026-ARXIV-2603-16731 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#一次-training-step-的状态流 (section Ch-owner) | books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent); books/part-04-training-system/29-sft.md#第29章-sft (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16731 | delta:SF-2026-ARXIV-2603-16731 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16731 |
| SF-2026-ARXIV-2603-16817 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#self-report、behavior-probe-与-deployment-outcome-是三种证据 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16817 | delta:SF-2026-ARXIV-2603-16817 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16817 |

<!-- books-review:SF-2026-ARXIV-2603-15690:start -->
### Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15690:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。<!-- existing:SF-2026-ARXIV-2603-15690:end -->

<!-- delta:SF-2026-ARXIV-2603-15690:start -->新证据差异：论文把 context artifact、semantic lens、index generator 与 evolution entropy 组合为显式工程对象，使 rewiring 的来源和结构变化可追踪。<!-- delta:SF-2026-ARXIV-2603-15690:end -->

边界：只支持 arXiv:2603.15690v1 §4.2. Design Patterns 的机制与 §8.1. Evaluation on RepoBench-R 的公开 workload；§9. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15690:end -->
<!-- books-review:SF-2026-ARXIV-2603-15714:start -->
### How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15714:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：安全数据闭环还可由当前 policy 生成 adversarial candidates，再由独立 guard / outcome policy 筛选后进入训练。它能把静态红队集扩展到当前模型暴露的 failure frontier，却同时制造 self-confirmation 风险：generator 与 guard 若共享模型家族、prompt 或表示盲点，可能一致地把危险样本标成安全；只保留通过 guard 的样本还会隐藏 false negative。因而 generated sample、generator checkpoint、guard version、policy taxonomy、人工复核切片和最终 deployment gate 必须分开保存。该机制适合作为受控 data augmentation，不能取代 output-time enforcement 或独立 red-team evaluation。<!-- existing:SF-2026-ARXIV-2603-15714:end -->

<!-- delta:SF-2026-ARXIV-2603-15714:start -->新证据差异：工作从公开竞赛记录恢复攻击与防御路径，将成功条件绑定到 agent 对不可信内容的读取、指令采纳和工具执行链。<!-- delta:SF-2026-ARXIV-2603-15714:end -->

边界：只支持 arXiv:2603.15714v1 §Red-Teaming Methodologies. 的机制与 §3.2 Evaluation 的公开 workload；§Threat Model. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15714:end -->
<!-- books-review:SF-2026-ARXIV-2603-15727:start -->
### AgentWorm: Self-Propagating Attacks Across LLM Agent Ecosystems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15727:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：OS telemetry 只能看到操作与时序，不拥有 Agent intent；semantic detector 也可能把正常自修改误报为攻击。 某些 mutation 在系统调用层与正常行为不可区分，必须依赖更高层 workflow invariant、human approval 或恢复点。 静态 ACL 仍适合 instruction/config 等低变更层，动态检测只用于确实需要写入的层。Self-State Attacks 的论文 提供 threat matrix 与受控 traces，不证明其 detector 覆盖生产 workload，也不允许 Memory backup 绕过删除政策。<!-- existing:SF-2026-ARXIV-2603-15727:end -->

<!-- delta:SF-2026-ARXIV-2603-15727:start -->新证据差异：AgentWorm 展示单消息触发的自主感染链，把传播载荷、持久化和跨平台发送连成系统攻击路径。<!-- delta:SF-2026-ARXIV-2603-15727:end -->

边界：只支持 arXiv:2603.15727v1 §Testbed architecture. 的机制与 §5.3 Main Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15727:end -->
<!-- books-review:SF-2026-ARXIV-2603-15798:start -->
### CUBE: A Standard for Unifying Agent Benchmarks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15798:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-15798:end -->

<!-- delta:SF-2026-ARXIV-2603-15798:start -->新证据差异：CUBE 用 MCP/Gym 风格协议拆分 task、benchmark、package 和 registry，使环境包装与 agent implementation 独立。<!-- delta:SF-2026-ARXIV-2603-15798:end -->

边界：只支持 arXiv:2603.15798v1 §3.5 Python-First Design with RPC Fallback 的机制与 §3.2 Benchmark-Level Interface 的公开 workload；§Lighter-Weight Alternatives 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15798:end -->
<!-- books-review:SF-2026-ARXIV-2603-15973:start -->
### Safety is Non-Compositional: A Formal Framework for Capability-Based AI Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-15973:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-15973:end -->

<!-- delta:SF-2026-ARXIV-2603-15973:start -->新证据差异：论文用 capability graph 与组合规则证明 non-compositionality，并要求 governance 在联合可达状态而非单主体权限上判断。<!-- delta:SF-2026-ARXIV-2603-15973:end -->

边界：只支持 arXiv:2603.15973v1 §Algorithm 1 Capability Closure (Optimised Worklist) 的机制与 §results in the Safe Audit Surface Theorem (Theorem 10.1)—a polynomial-time-computable, 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-15973:end -->
<!-- books-review:SF-2026-ARXIV-2603-16013:start -->
### Safety Case Patterns for VLA-based driving systems: Insights from SimLingo — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16013:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：固定 observation window 与固定输入下，partitioned attention 可以与 full-batch attention 保持相同；这个 exactness 不覆盖异步 scheduling、future prediction 或 mixed-precision stability。作者在 Pi0/Pi0.5/SmolVLA、RTX 4090/3090、LIBERO/Kinetix 与有限真实机器人任务上的 50 Hz/p95 latency 结果是 experimental systems evidence，不是开放物理环境的 safety proof。Streaming 获得的是 stall hiding 与 fresher action，代价是双线程可见性、ring-buffer ownership、numerical guardrail 与新的 stale-state failure mode。<!-- existing:SF-2026-ARXIV-2603-16013:end -->

<!-- delta:SF-2026-ARXIV-2603-16013:start -->新证据差异：论文用 SimLingo 提炼 safety-case patterns，将语言输入、action generation、monitor 与 fallback 对应到可审查 assurance claim。<!-- delta:SF-2026-ARXIV-2603-16013:end -->

边界：只支持 arXiv:2603.16013v1 §3.1 Overview 的机制与 §4.1 Key Takeaways 的公开 workload；§4.2 Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16013:end -->
<!-- books-review:SF-2026-ARXIV-2603-16104:start -->
### Efficient LLM Serving for Agentic Workflows: A Data Systems Perspective — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16104:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-16104:end -->

<!-- delta:SF-2026-ARXIV-2603-16104:start -->新证据差异：Helium 把 workflow dependency 与中间结果纳入数据系统，联合执行 cache-aware routing、共享状态复用与 workflow-level scheduling。<!-- delta:SF-2026-ARXIV-2603-16104:end -->

边界：只支持 arXiv:2603.16104v1 §3. System Overview 的机制与 §7. Evaluation 的公开 workload；§9. Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16104:end -->
<!-- books-review:SF-2026-ARXIV-2603-16158:start -->
### Execution-Grounded Credit Assignment for GRPO in Code Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16158:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条 路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体 数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是： **verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**<!-- existing:SF-2026-ARXIV-2603-16158:end -->

<!-- delta:SF-2026-ARXIV-2603-16158:start -->新证据差异：EGCA 对候选与参考程序做同仪器执行，定位首次状态分歧并把 GRPO credit 聚焦到相关片段。<!-- delta:SF-2026-ARXIV-2603-16158:end -->

边界：只支持 arXiv:2603.16158v1 §4.2 Training Setup and Implementation Details 的机制与 §4.4 Main Results 的公开 workload；§5 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16158:end -->
<!-- books-review:SF-2026-ARXIV-2603-16435:start -->
### VQKV: High-Fidelity and High-Ratio Cache Compression via Vector-Quantization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16435:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是 新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不 等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。<!-- existing:SF-2026-ARXIV-2603-16435:end -->

<!-- delta:SF-2026-ARXIV-2603-16435:start -->新证据差异：VQKV 用 vector quantization 对 KV 的联合结构编码，以可复用 codebook 换取更高压缩比，并保持训练外部署路径。<!-- delta:SF-2026-ARXIV-2603-16435:end -->

边界：只支持 arXiv:2603.16435v1 §3 Compressing KV with Vector Quantization 的机制与 §4.2 Long-Context Evaluation 的公开 workload；§6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16435:end -->
<!-- books-review:SF-2026-ARXIV-2603-16572:start -->
### Context Matters: Repository-Aware Security Analysis of the Agent Skill Ecosystem — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16572:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-16572:end -->

<!-- delta:SF-2026-ARXIV-2603-16572:start -->新证据差异：研究在跨 marketplace 的 238,180 个去重 skill 上联合分析文件内容、行为和仓库语境，重新定义生态风险分母。<!-- delta:SF-2026-ARXIV-2603-16572:end -->

边界：只支持 arXiv:2603.16572v1 §3 Methodology 的机制与 §3.3 Repository-Aware Analysis 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16572:end -->
<!-- books-review:SF-2026-ARXIV-2603-16586:start -->
### Runtime Governance for AI Agents: Policies on Paths — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16586:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-16586:end -->

<!-- delta:SF-2026-ARXIV-2603-16586:start -->新证据差异：论文把 governance 定义为作用在 action path、principal、当前 state 与历史摘要上的 policy function，使每个执行边都有可判定的策略状态。<!-- delta:SF-2026-ARXIV-2603-16586:end -->

边界：只支持 arXiv:2603.16586v1 §3 A Formal Framework for Agent Governance 的机制与 §4.4 Concrete intervention outcomes 的公开 workload；§4.6 Challenges 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16586:end -->
<!-- books-review:SF-2026-ARXIV-2603-16731:start -->
### Understanding Quantization of Optimizer States in LLM Pre-training: Dynamics of State Staleness and Effectiveness of State Resets — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16731:start -->已读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节。现有命题：第 35 章会说明：若 checkpoint 只保存 `theta` 而不保存 optimizer、scheduler、random state 和 data cursor，通常只能继续做新的 fine-tuning，不能精确恢复原 Pretraining trajectory。<!-- existing:SF-2026-ARXIV-2603-16731:end -->

<!-- delta:SF-2026-ARXIV-2603-16731:start -->新证据差异：工作把量化、反量化与 EMA reset 写进 optimizer 更新，并比较周期性重置能否清除累积陈旧性。<!-- delta:SF-2026-ARXIV-2603-16731:end -->

边界：只支持 arXiv:2603.16731v1 §A.11 Algorithms 的机制与 §6.2 Results 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16731:end -->
<!-- books-review:SF-2026-ARXIV-2603-16817:start -->
### Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16817:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失： 写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge 与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。<!-- existing:SF-2026-ARXIV-2603-16817:end -->

<!-- delta:SF-2026-ARXIV-2603-16817:start -->新证据差异：论文联合测量统计可靠性与 informativeness，并挑战 calibration shift、retrieval 质量和 claim 分解对保证的影响。<!-- delta:SF-2026-ARXIV-2603-16817:end -->

边界：只支持 arXiv:2603.16817v1 §4 Design Choices for Factuality Scoring in Conformal Filtering 的机制与 §6 Efficiency Evaluation of the Conformal Factuality Pipeline End-to-End 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16817:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260318-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260318 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260318-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260318-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260318-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | — | accepted: 所有 Books disposition 已复核，本日无需写回 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260318/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

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
