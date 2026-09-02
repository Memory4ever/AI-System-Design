# Daily Research — 2026-03-19

**Research Date:** 2026-03-19

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-18 09:00:00 ～ 2026-03-19 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=593/593/593；denominator=13、pre-denominator closures=580。exact-v1 Review complete=13、blocked=0；Integrate 建议=1。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-19 |
| Window End | 2026-03-19 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260319-AUTHOR-13 |
| Denominator Frozen At | 2026-09-02T16:17:56.686449+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-18T09:00:00+08:00 | 2026-03-19T09:00:00+08:00 | 2026-09-02T16:17:56.686449+08:00 | official-schedule recovery receipt + 593/593 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 593 | SF-2026-ARXIV-2603-16938;SF-2026-ARXIV-2603-17104;SF-2026-ARXIV-2603-17117;SF-2026-ARXIV-2603-17170;SF-2026-ARXIV-2603-17244;SF-2026-ARXIV-2603-17357;SF-2026-ARXIV-2603-17445;SF-2026-ARXIV-2603-17456;SF-2026-ARXIV-2603-17573;SF-2026-ARXIV-2603-17673;SF-2026-ARXIV-2603-17787;SF-2026-ARXIV-2603-17803;SF-2026-ARXIV-2603-17808 | pages=100; prefixes=00..99; final_cursor=end; registered=593; screened=593; retained=13; closure=580 | 2026-03-19T01:00:00+00:00 | screening-ledger-final.json#sha256=f525095c5101424d579c59b7e936e99d19610d6d853a590a9c8e832c98c3ea3c; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260319:start -->作者侧已逐项筛选全部 593 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260319:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-16938 | arXiv:2603.16938v1 | paper-v1:2603.16938 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-16938 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16938 | no |
| SF-2026-ARXIV-2603-17104 | arXiv:2603.17104v1 | paper-v1:2603.17104 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17104 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17104 | no |
| SF-2026-ARXIV-2603-17117 | arXiv:2603.17117v1 | paper-v1:2603.17117 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17117 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17117 | no |
| SF-2026-ARXIV-2603-17170 | arXiv:2603.17170v1 | paper-v1:2603.17170 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17170 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17170 | no |
| SF-2026-ARXIV-2603-17244 | arXiv:2603.17244v1 | paper-v1:2603.17244 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17244 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17244 | no |
| SF-2026-ARXIV-2603-17357 | arXiv:2603.17357v1 | paper-v1:2603.17357 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17357 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17357 | no |
| SF-2026-ARXIV-2603-17445 | arXiv:2603.17445v1 | paper-v1:2603.17445 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17445 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17445 | no |
| SF-2026-ARXIV-2603-17456 | arXiv:2603.17456v1 | paper-v1:2603.17456 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17456 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17456 | no |
| SF-2026-ARXIV-2603-17573 | arXiv:2603.17573v1 | paper-v1:2603.17573 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17573 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17573 | no |
| SF-2026-ARXIV-2603-17673 | arXiv:2603.17673v1 | paper-v1:2603.17673 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17673 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17673 | no |
| SF-2026-ARXIV-2603-17787 | arXiv:2603.17787v1 | paper-v1:2603.17787 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17787 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17787 | no |
| SF-2026-ARXIV-2603-17803 | arXiv:2603.17803v1 | paper-v1:2603.17803 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17803 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2603-17803 | no |
| SF-2026-ARXIV-2603-17808 | arXiv:2603.17808v1 | paper-v1:2603.17808 | 2026-W12 | 2026-03-19 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-17808 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17808 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-16938 | RP-3a6cafd9614d7c86 | deep | arXiv:2603.16938v1 | SRC-ARXIV@arXiv:2603.16938v1 | arXiv:2603.16938v1 HTML — §8. Methodology [facet=method]; https://arxiv.org/html/2603.16938v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.16938v1.html; sha256:29a625cf1845dfe9999c5c54ac74e63ff2e5350e43c3c62b1293b294e48e195b | arXiv:2603.16938v1 HTML — §vi. Proofing and Validation [facet=evaluation]; https://arxiv.org/html/2603.16938v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.16938v1.html; sha256:29a625cf1845dfe9999c5c54ac74e63ff2e5350e43c3c62b1293b294e48e195b | arXiv:2603.16938v1 HTML — §11. Limitations and Open Questions [facet=limitations]; https://arxiv.org/html/2603.16938v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.16938v1.html; sha256:29a625cf1845dfe9999c5c54ac74e63ff2e5350e43c3c62b1293b294e48e195b | arXiv exact-v1 identity https://arxiv.org/abs/2603.16938v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-16938 | complete |
| SF-2026-ARXIV-2603-17104 | RP-fe555f3d5020100e | deep | arXiv:2603.17104v1 | SRC-ARXIV@arXiv:2603.17104v1 | arXiv:2603.17104v1 HTML — §5.1 Method [facet=method]; https://arxiv.org/html/2603.17104v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17104v1.html; sha256:0e52fbf560526dd3261530b34ffdfddbf6de8e622775d292ea0f76024c90bcd2 | arXiv:2603.17104v1 HTML — §3.3 Benchmark Fairness Validation [facet=evaluation]; https://arxiv.org/html/2603.17104v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17104v1.html; sha256:0e52fbf560526dd3261530b34ffdfddbf6de8e622775d292ea0f76024c90bcd2 | arXiv:2603.17104v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.17104v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17104v1.html; sha256:0e52fbf560526dd3261530b34ffdfddbf6de8e622775d292ea0f76024c90bcd2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17104v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17104 | complete |
| SF-2026-ARXIV-2603-17117 | RP-bbb6708d70d5519f | deep | arXiv:2603.17117v1 | SRC-ARXIV@arXiv:2603.17117v1 | arXiv:2603.17117v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.17117v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17117v1.html; sha256:a6011e2fcbf824da05f2ba99a18d6b3aa6f8ee30b4fecfc5673e4ad947829174 | arXiv:2603.17117v1 HTML — §4 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17117v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17117v1.html; sha256:a6011e2fcbf824da05f2ba99a18d6b3aa6f8ee30b4fecfc5673e4ad947829174 | arXiv:2603.17117v1 HTML — §4.2 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.17117v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17117v1.html; sha256:a6011e2fcbf824da05f2ba99a18d6b3aa6f8ee30b4fecfc5673e4ad947829174 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17117v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17117 | complete |
| SF-2026-ARXIV-2603-17170 | RP-a8c30bb7c301592d | deep | arXiv:2603.17170v1 | SRC-ARXIV@arXiv:2603.17170v1 | arXiv:2603.17170v1 HTML — §4.1 Implementation on AgentDojo [facet=method]; https://arxiv.org/html/2603.17170v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17170v1.html; sha256:a4cb29c13c61a280372483107a0b5b7eabb6cb78271a80ac3f611321696bcea5 | arXiv:2603.17170v1 HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17170v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17170v1.html; sha256:a4cb29c13c61a280372483107a0b5b7eabb6cb78271a80ac3f611321696bcea5 | arXiv:2603.17170v1 HTML — §6 Discussion [facet=limitations]; https://arxiv.org/html/2603.17170v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17170v1.html; sha256:a4cb29c13c61a280372483107a0b5b7eabb6cb78271a80ac3f611321696bcea5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17170v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17170 | complete |
| SF-2026-ARXIV-2603-17244 | RP-fb11571592c5b791 | deep | arXiv:2603.17244v1 | SRC-ARXIV@arXiv:2603.17244v1 | arXiv:2603.17244v1 HTML — §2.1 Agent Memory Architectures [facet=method]; https://arxiv.org/html/2603.17244v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17244v1.html; sha256:6c60d9513edf77ad90f30f232791fb0a5c7cefa37eb7ef09c8023b7944d04979 | arXiv:2603.17244v1 HTML — §15.2 LoCoMo Benchmark Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17244v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17244v1.html; sha256:6c60d9513edf77ad90f30f232791fb0a5c7cefa37eb7ef09c8023b7944d04979 | arXiv:2603.17244v1 HTML — §15.9 Limitations [facet=limitations]; https://arxiv.org/html/2603.17244v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17244v1.html; sha256:6c60d9513edf77ad90f30f232791fb0a5c7cefa37eb7ef09c8023b7944d04979 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17244v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17244 | complete |
| SF-2026-ARXIV-2603-17357 | RP-23f385b554bcef5d | deep | arXiv:2603.17357v1 | SRC-ARXIV@arXiv:2603.17357v1 | arXiv:2603.17357v1 HTML — §3.2.1 Text-Based Methods [facet=method]; https://arxiv.org/html/2603.17357v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17357v1.html; sha256:081008177792635975b32afcfd563b019f608fe7d25ef2a1728d17045ca78694 | arXiv:2603.17357v1 HTML — §3.3 Results [facet=evaluation]; https://arxiv.org/html/2603.17357v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17357v1.html; sha256:081008177792635975b32afcfd563b019f608fe7d25ef2a1728d17045ca78694 | arXiv:2603.17357v1 HTML — §4.2 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.17357v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17357v1.html; sha256:081008177792635975b32afcfd563b019f608fe7d25ef2a1728d17045ca78694 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17357v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17357 | complete |
| SF-2026-ARXIV-2603-17445 | RP-097ed950eea929e7 | deep | arXiv:2603.17445v1 | SRC-ARXIV@arXiv:2603.17445v1 | arXiv:2603.17445v1 HTML — §3.2 Experimental Design [facet=method]; https://arxiv.org/html/2603.17445v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17445v1.html; sha256:9a116a310c1419a36c52b229ab75cb50b4f5487b30000fb15f49e4d4acaa2ed5 | arXiv:2603.17445v1 HTML — §3.5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17445v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17445v1.html; sha256:9a116a310c1419a36c52b229ab75cb50b4f5487b30000fb15f49e4d4acaa2ed5 | arXiv:2603.17445v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.17445v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17445v1.html; sha256:9a116a310c1419a36c52b229ab75cb50b4f5487b30000fb15f49e4d4acaa2ed5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17445v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17445 | complete |
| SF-2026-ARXIV-2603-17456 | RP-4a0204690d91e462 | deep | arXiv:2603.17456v1 | SRC-ARXIV@arXiv:2603.17456v1 | arXiv:2603.17456v1 HTML — §4.1. Design Challenges [facet=method]; https://arxiv.org/html/2603.17456v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17456v1.html; sha256:8e627c37261364e9c77a270d0fe335b491f08f032b2617296d993d811fe3f053 | arXiv:2603.17456v1 HTML — §6.1. Experiments setup [facet=evaluation]; https://arxiv.org/html/2603.17456v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17456v1.html; sha256:8e627c37261364e9c77a270d0fe335b491f08f032b2617296d993d811fe3f053 | arXiv:2603.17456v1 HTML — §2.3. Limitation of Existing Work [facet=limitations]; https://arxiv.org/html/2603.17456v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17456v1.html; sha256:8e627c37261364e9c77a270d0fe335b491f08f032b2617296d993d811fe3f053 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17456v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17456 | complete |
| SF-2026-ARXIV-2603-17573 | RP-5c02f92ae645c9a4 | deep | arXiv:2603.17573v1 | SRC-ARXIV@arXiv:2603.17573v1 | arXiv:2603.17573v1 HTML — §6 HeiSD Framework Implementation [facet=method]; https://arxiv.org/html/2603.17573v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17573v1.html; sha256:dc45e2dfa9216a60bbe2be780ab5dc08de98b74d1697c359f8101c094b3d12ed | arXiv:2603.17573v1 HTML — §7.2 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.17573v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17573v1.html; sha256:dc45e2dfa9216a60bbe2be780ab5dc08de98b74d1697c359f8101c094b3d12ed | arXiv:2603.17573v1 HTML — §7.3 Discussion [facet=limitations]; https://arxiv.org/html/2603.17573v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17573v1.html; sha256:dc45e2dfa9216a60bbe2be780ab5dc08de98b74d1697c359f8101c094b3d12ed | arXiv exact-v1 identity https://arxiv.org/abs/2603.17573v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17573 | complete |
| SF-2026-ARXIV-2603-17673 | RP-9cb9755eeaecf945 | deep | arXiv:2603.17673v1 | SRC-ARXIV@arXiv:2603.17673v1 | arXiv:2603.17673v1 HTML — §Cost Methodology [facet=method]; https://arxiv.org/html/2603.17673v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17673v1.html; sha256:08d39d06bff4249e7744c2a39e52079914bbdb68b42236fcdce0c0ce2c145c9a | arXiv:2603.17673v1 HTML — §V-A Main Results [facet=evaluation]; https://arxiv.org/html/2603.17673v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17673v1.html; sha256:08d39d06bff4249e7744c2a39e52079914bbdb68b42236fcdce0c0ce2c145c9a | arXiv:2603.17673v1 HTML — §VI Discussion [facet=limitations]; https://arxiv.org/html/2603.17673v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17673v1.html; sha256:08d39d06bff4249e7744c2a39e52079914bbdb68b42236fcdce0c0ce2c145c9a | arXiv exact-v1 identity https://arxiv.org/abs/2603.17673v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17673 | complete |
| SF-2026-ARXIV-2603-17787 | RP-347ebd9644e8a21b | deep | arXiv:2603.17787v1 | SRC-ARXIV@arXiv:2603.17787v1 | arXiv:2603.17787v1 HTML — §3 Architecture Overview [facet=method]; https://arxiv.org/html/2603.17787v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17787v1.html; sha256:98eb053ef0643e0824004687926a6bfc91f5e315f5986b9c430262b0564e4d61 | arXiv:2603.17787v1 HTML — §8.11 External Benchmark Validation: LoCoMo [facet=evaluation]; https://arxiv.org/html/2603.17787v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17787v1.html; sha256:98eb053ef0643e0824004687926a6bfc91f5e315f5986b9c430262b0564e4d61 | arXiv:2603.17787v1 HTML — §9.1 Limitations [facet=limitations]; https://arxiv.org/html/2603.17787v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17787v1.html; sha256:98eb053ef0643e0824004687926a6bfc91f5e315f5986b9c430262b0564e4d61 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17787v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17787 | complete |
| SF-2026-ARXIV-2603-17803 | RP-f3e99764988edd35 | deep | arXiv:2603.17803v1 | SRC-ARXIV@arXiv:2603.17803v1 | arXiv:2603.17803v1 HTML — §4 Design Overview [facet=method]; https://arxiv.org/html/2603.17803v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17803v1.html; sha256:e0f3b6194f2590aad0612f1256df993f3d949997dccaa5087fbd9f3b673f10a9 | arXiv:2603.17803v1 HTML — §8.2 Overall Performance [facet=evaluation]; https://arxiv.org/html/2603.17803v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17803v1.html; sha256:e0f3b6194f2590aad0612f1256df993f3d949997dccaa5087fbd9f3b673f10a9 | arXiv:2603.17803v1 HTML — §8.4 Sensitivity Analysis [facet=limitations]; https://arxiv.org/html/2603.17803v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17803v1.html; sha256:e0f3b6194f2590aad0612f1256df993f3d949997dccaa5087fbd9f3b673f10a9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17803v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17803 | complete |
| SF-2026-ARXIV-2603-17808 | RP-fd3c30cb431ac0e2 | deep | arXiv:2603.17808v1 | SRC-ARXIV@arXiv:2603.17808v1 | arXiv:2603.17808v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.17808v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17808v1.html; sha256:c72bf786797d8b9611a198efb0c4704b2a71b4cb6351b18bb5395d0756eb15c7 | arXiv:2603.17808v1 HTML — §Appendix 0.A Detailed Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.17808v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17808v1.html; sha256:c72bf786797d8b9611a198efb0c4704b2a71b4cb6351b18bb5395d0756eb15c7 | arXiv:2603.17808v1 HTML — §5.6 Failure Modes [facet=limitations]; https://arxiv.org/html/2603.17808v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17808v1.html; sha256:c72bf786797d8b9611a198efb0c4704b2a71b4cb6351b18bb5395d0756eb15c7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.17808v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-17808 | complete |

### Source Reviews

### Cryptographic Runtime Governance for Autonomous AI Systems: The Aegis Architecture for Verifiable Policy Enforcement

<!-- review:SF-2026-ARXIV-2603-16938:start -->
**问题**：post-hoc policy 和行为 alignment 在高速自治执行中不能证明某个 action 当时满足约束。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：Aegis 将不可变 policy、运行时许可与加密审计链绑定，使 policy decision 成为执行前条件。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.16938v1 HTML — §8. Methodology [facet=method]; https://arxiv.org/html/2603.16938v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.16938v1.html; sha256:29a625cf1845dfe9999c5c54ac74e63ff2e5350e43c3c62b1293b294e48e195b`。

**Evaluation contract 与未证明部分**：论文主要提供架构和协议论证；没有证明实现可满足大规模 agent latency 或抵抗全部密钥攻击。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.16938v1 HTML — §vi. Proofing and Validation [facet=evaluation]; https://arxiv.org/html/2603.16938v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.16938v1.html; sha256:29a625cf1845dfe9999c5c54ac74e63ff2e5350e43c3c62b1293b294e48e195b`。

**Trade-off / failure / coexistence**：强治理增加密钥管理和中心依赖；低风险只读 agent 可使用轻量审计。

<!-- claim:SF-2026-ARXIV-2603-16938:start -->**Claim Boundary**：只支持 arXiv:2603.16938v1 §8. Methodology 的机制与 §vi. Proofing and Validation 的公开 workload；§11. Limitations and Open Questions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-16938:end -->
<!-- review:SF-2026-ARXIV-2603-16938:end -->
### When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents

<!-- review:SF-2026-ARXIV-2603-17104:start -->
**问题**：真实 coding agent 的 specification 会在执行中逐步出现，若只保存当前 prompt，早期设计承诺会在长链修改中丢失。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：ProjectGuard 维护同步的 durable semantic state 与项目 artifact 视图，把新约束、决策和依据持续合并后再提供给 agent。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.17104v1 HTML — §5.1 Method [facet=method]; https://arxiv.org/html/2603.17104v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17104v1.html; sha256:0e52fbf560526dd3261530b34ffdfddbf6de8e622775d292ea0f76024c90bcd2`。

**Evaluation contract 与未证明部分**：benchmark 对比一次性完整规格与渐进披露，测量最终实现的 faithfulness loss；证据限于研究型 coding 任务。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17104v1 HTML — §3.3 Benchmark Fairness Validation [facet=evaluation]; https://arxiv.org/html/2603.17104v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17104v1.html; sha256:0e52fbf560526dd3261530b34ffdfddbf6de8e622775d292ea0f76024c90bcd2`。

**Trade-off / failure / coexistence**：外部状态可降低 specification drift，却引入抽取错误和过期承诺；短任务或规格一次给全时不需要该层。

<!-- claim:SF-2026-ARXIV-2603-17104:start -->**Claim Boundary**：只支持 arXiv:2603.17104v1 §5.1 Method 的机制与 §3.3 Benchmark Fairness Validation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17104:end -->
<!-- review:SF-2026-ARXIV-2603-17104:end -->
### MosaicMem: Hybrid Spatial Memory for Controllable Video World Models

<!-- review:SF-2026-ARXIV-2603-17117:start -->
**问题**：视频 world model 需要在回访和相机运动下保持空间一致，又不能让显式 3D memory 抹掉动态对象。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：MosaicMem 把 patch 提升到 3D 以定位/检索，同时由生成模型原生条件保留动态内容，形成显式与隐式 memory 的混合。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.17117v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.17117v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17117v1.html; sha256:a6011e2fcbf824da05f2ba99a18d6b3aa6f8ee30b4fecfc5673e4ad947829174`。

**Evaluation contract 与未证明部分**：实验支持所测相机轨迹与生成任务的空间一致性；不能证明长期交互状态不会漂移。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17117v1 HTML — §4 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17117v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17117v1.html; sha256:a6011e2fcbf824da05f2ba99a18d6b3aa6f8ee30b4fecfc5673e4ad947829174`。

**Trade-off / failure / coexistence**：3D 对齐增加几何误差和维护成本；短视频或无回访任务可用纯隐式状态。

<!-- claim:SF-2026-ARXIV-2603-17117:start -->**Claim Boundary**：只支持 arXiv:2603.17117v1 §2 Methodology 的机制与 §4 Evaluation 的公开 workload；§4.2 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17117:end -->
<!-- review:SF-2026-ARXIV-2603-17117:end -->
### Beyond OAuth: Task-Scoped Authorization for AI Agents via Natural Language Slices

<!-- review:SF-2026-ARXIV-2603-17170:start -->
**问题**：OAuth scope 授权的是操作符，却不能表达金额、对象等运行时 operands，agent 因而持有超出任务的权限。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：task-scoped slice 从自然语言任务派生 operation predicate，并在跨服务执行时携带、缩减和验证该谓词。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.17170v1 HTML — §4.1 Implementation on AgentDojo [facet=method]; https://arxiv.org/html/2603.17170v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17170v1.html; sha256:a4cb29c13c61a280372483107a0b5b7eabb6cb78271a80ac3f611321696bcea5`。

**Evaluation contract 与未证明部分**：论文协议/案例支持 operand-level 表达力；不证明自然语言到 predicate 的编译不会错。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17170v1 HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17170v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17170v1.html; sha256:a4cb29c13c61a280372483107a0b5b7eabb6cb78271a80ac3f611321696bcea5`。

**Trade-off / failure / coexistence**：细粒度权限增加解析、委托和撤销复杂度；固定操作参数可继续静态 scope。

<!-- claim:SF-2026-ARXIV-2603-17170:start -->**Claim Boundary**：只支持 arXiv:2603.17170v1 §4.1 Implementation on AgentDojo 的机制与 §5 Evaluation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17170:end -->
<!-- review:SF-2026-ARXIV-2603-17170:end -->
### Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures

<!-- review:SF-2026-ARXIV-2603-17244:start -->
**问题**：agent memory 若只追加事实，无法在相互冲突的新证据到来时说明哪个 belief 有效、为什么被替换。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：该工作用 graph-native、versioned belief node 和形式化 revision operator 表达 provenance、冲突与 consolidation。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.17244v1 HTML — §2.1 Agent Memory Architectures [facet=method]; https://arxiv.org/html/2603.17244v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17244v1.html; sha256:6c60d9513edf77ad90f30f232791fb0a5c7cefa37eb7ef09c8023b7944d04979`。

**Evaluation contract 与未证明部分**：评测从九个维度与现有系统比较并在长会话数据上检查规模行为；它未证明形式语义能消除抽取或检索错误。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17244v1 HTML — §15.2 LoCoMo Benchmark Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17244v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17244v1.html; sha256:6c60d9513edf77ad90f30f232791fb0a5c7cefa37eb7ef09c8023b7944d04979`。

**Trade-off / failure / coexistence**：可追溯 belief revision 提升治理性，但图维护和一致性成本更高；只读知识库或无冲突短会话仍可用简单向量记忆。

<!-- claim:SF-2026-ARXIV-2603-17244:start -->**Claim Boundary**：只支持 arXiv:2603.17244v1 §2.1 Agent Memory Architectures 的机制与 §15.2 LoCoMo Benchmark Evaluation 的公开 workload；§15.9 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17244:end -->
<!-- review:SF-2026-ARXIV-2603-17244:end -->
### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents

<!-- review:SF-2026-ARXIV-2603-17357:start -->
**问题**：computer-use agent 的截图既可能进入训练集也可能上传云端，但现有隐私检测缺少网页视觉 PII 合同。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：WebPII 用合成电商 UI、细粒度 PII taxonomy 和部分填写状态定义 anticipatory detection benchmark。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.17357v1 HTML — §3.2.1 Text-Based Methods [facet=method]; https://arxiv.org/html/2603.17357v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17357v1.html; sha256:081008177792635975b32afcfd563b019f608fe7d25ef2a1728d17045ca78694`。

**Evaluation contract 与未证明部分**：44,865 张标注图只证明该生成分布上的识别能力，不代表真实网站长尾。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17357v1 HTML — §3.3 Results [facet=evaluation]; https://arxiv.org/html/2603.17357v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17357v1.html; sha256:081008177792635975b32afcfd563b019f608fe7d25ef2a1728d17045ca78694`。

**Trade-off / failure / coexistence**：更细检测能提前遮蔽但会误伤正常 UI；本地推理可降低云端泄露面。

<!-- claim:SF-2026-ARXIV-2603-17357:start -->**Claim Boundary**：只支持 arXiv:2603.17357v1 §3.2.1 Text-Based Methods 的机制与 §3.3 Results 的公开 workload；§4.2 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17357:end -->
<!-- review:SF-2026-ARXIV-2603-17357:end -->
### When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Auditing

<!-- review:SF-2026-ARXIV-2603-17445:start -->
**问题**：多 agent 输出脱离运行环境后，完整 trace 与 agent ID 不再可得，传统 RCA 无法归责。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：IET 在生成阶段嵌入可恢复的隐式 provenance，使最终文本成为最小审计载体。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `arXiv:2603.17445v1 HTML — §3.2 Experimental Design [facet=method]; https://arxiv.org/html/2603.17445v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17445v1.html; sha256:9a116a310c1419a36c52b229ab75cb50b4f5487b30000fb15f49e4d4acaa2ed5`。

**Evaluation contract 与未证明部分**：论文实验支持指定模型和变换下的恢复率；不证明强对手或重写链后仍可靠。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17445v1 HTML — §3.5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.17445v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17445v1.html; sha256:9a116a310c1419a36c52b229ab75cb50b4f5487b30000fb15f49e4d4acaa2ed5`。

**Trade-off / failure / coexistence**：内嵌信号可能影响文本并被移除；有完整可信 trace 时显式日志仍更强。

<!-- claim:SF-2026-ARXIV-2603-17445:start -->**Claim Boundary**：只支持 arXiv:2603.17445v1 §3.2 Experimental Design 的机制与 §3.5 Evaluation 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17445:end -->
<!-- review:SF-2026-ARXIV-2603-17445:end -->
### Multi-stage Flow Scheduling for LLM Serving

<!-- review:SF-2026-ARXIV-2603-17456:start -->
**问题**：LLM serving 的 prefill、decode 与 KV transfer 共享多阶段网络路径，单队列看不到下游拥塞导致的 TTFT 违约。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：MFS 用 defer-and-promote 在多级队列中延迟非紧急 flow，并依据阶段进展提升优先级，从控制通信 flow 而非只排 GPU request。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.17456v1 HTML — §4.1. Design Challenges [facet=method]; https://arxiv.org/html/2603.17456v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17456v1.html; sha256:8e627c37261364e9c77a270d0fe335b491f08f032b2617296d993d811fe3f053`。

**Evaluation contract 与未证明部分**：8 台服务器、每台 4 张 RTX 3090 的 testbed 给出端到端结果；不同 fabric、模型和 SLO 下的排序仍需重验。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17456v1 HTML — §6.1. Experiments setup [facet=evaluation]; https://arxiv.org/html/2603.17456v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17456v1.html; sha256:8e627c37261364e9c77a270d0fe335b491f08f032b2617296d993d811fe3f053`。

**Trade-off / failure / coexistence**：多阶段状态改善 deadline 管理但会增加队列维护和 starvation 风险；单阶段或低争用负载仍适合简单 FIFO。

<!-- claim:SF-2026-ARXIV-2603-17456:start -->**Claim Boundary**：只支持 arXiv:2603.17456v1 §4.1. Design Challenges 的机制与 §6.1. Experiments setup 的公开 workload；§2.3. Limitation of Existing Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17456:end -->
<!-- review:SF-2026-ARXIV-2603-17456:end -->
### HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness

<!-- review:SF-2026-ARXIV-2603-17573:start -->
**问题**：VLA action chunk 自回归生成占用控制周期，简单并行草稿若错误会破坏动作连续性。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：论文为动作序列建立 draft-and-verify，并让接受/回滚与 action chunk 边界一致。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.17573v1 HTML — §6 HeiSD Framework Implementation [facet=method]; https://arxiv.org/html/2603.17573v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17573v1.html; sha256:dc45e2dfa9216a60bbe2be780ab5dc08de98b74d1697c359f8101c094b3d12ed`。

**Evaluation contract 与未证明部分**：仿真/机器人结果只支持所测 policy、chunk 和控制频率；不证明所有 embodiment 都无损。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17573v1 HTML — §7.2 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.17573v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17573v1.html; sha256:dc45e2dfa9216a60bbe2be780ab5dc08de98b74d1697c359f8101c094b3d12ed`。

**Trade-off / failure / coexistence**：低接受率会增加验证开销；安全关键动作可退回逐步生成。

<!-- claim:SF-2026-ARXIV-2603-17573:start -->**Claim Boundary**：只支持 arXiv:2603.17573v1 §6 HeiSD Framework Implementation 的机制与 §7.2 Evaluation Results 的公开 workload；§7.3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17573:end -->
<!-- review:SF-2026-ARXIV-2603-17573:end -->
### Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation

<!-- review:SF-2026-ARXIV-2603-17673:start -->
**问题**：agent 安全微调若只奖励最终拒绝，不能定位哪一步权限或工具决策导致风险。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：该工作把可验证安全约束与 action trajectory 对齐，用执行结果为策略更新提供分步信号。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.17673v1 HTML — §Cost Methodology [facet=method]; https://arxiv.org/html/2603.17673v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17673v1.html; sha256:08d39d06bff4249e7744c2a39e52079914bbdb68b42236fcdce0c0ce2c145c9a`。

**Evaluation contract 与未证明部分**：证据限于论文环境中的攻击任务和 verifier；不能证明未知工具语义被覆盖。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17673v1 HTML — §V-A Main Results [facet=evaluation]; https://arxiv.org/html/2603.17673v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17673v1.html; sha256:08d39d06bff4249e7744c2a39e52079914bbdb68b42236fcdce0c0ce2c145c9a`。

**Trade-off / failure / coexistence**：更强约束降低探索并依赖 verifier 完整性；只读 agent 可采用较轻策略。

<!-- claim:SF-2026-ARXIV-2603-17673:start -->**Claim Boundary**：只支持 arXiv:2603.17673v1 §Cost Methodology 的机制与 §V-A Main Results 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17673:end -->
<!-- review:SF-2026-ARXIV-2603-17673:end -->
### Governed Memory: A Production Architecture for Multi-Agent Workflows

<!-- review:SF-2026-ARXIV-2603-17787:start -->
**问题**：多个 agent 对同一实体各自写 memory，会产生冲突、不可追踪派生与跨 workflow 数据泄漏。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：论文提出共享 governed memory layer，用 identity、provenance、temporal anchor 与写入 quality gate 统一多 agent 的读写契约。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.17787v1 HTML — §3 Architecture Overview [facet=method]; https://arxiv.org/html/2603.17787v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17787v1.html; sha256:98eb053ef0643e0824004687926a6bfc91f5e315f5986b9c430262b0564e4d61`。

**Evaluation contract 与未证明部分**：验证依赖 domain rubric、trace capture 和启发式质量分，能说明架构可运行但不能证明语义质量判定可靠。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17787v1 HTML — §8.11 External Benchmark Validation: LoCoMo [facet=evaluation]; https://arxiv.org/html/2603.17787v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17787v1.html; sha256:98eb053ef0643e0824004687926a6bfc91f5e315f5986b9c430262b0564e4d61`。

**Trade-off / failure / coexistence**：治理层提高可追责性，却成为集中式状态和策略瓶颈；隔离任务或短生命周期 agent 可保留私有 memory。

<!-- claim:SF-2026-ARXIV-2603-17787:start -->**Claim Boundary**：只支持 arXiv:2603.17787v1 §3 Architecture Overview 的机制与 §8.11 External Benchmark Validation: LoCoMo 的公开 workload；§9.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17787:end -->
<!-- review:SF-2026-ARXIV-2603-17787:end -->
### Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs

<!-- review:SF-2026-ARXIV-2603-17803:start -->
**问题**：KV offload 到单 SSD 时，相关条目常被一起请求，随机布局使多盘带宽无法并行利用。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：Swarm 离线学习 KV co-activation，按关联图跨 SSD 放置，并在在线阶段协同检索、更新和缓存。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.17803v1 HTML — §4 Design Overview [facet=method]; https://arxiv.org/html/2603.17803v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17803v1.html; sha256:e0f3b6194f2590aad0612f1256df993f3d949997dccaa5087fbd9f3b673f10a9`。

**Evaluation contract 与未证明部分**：公开系统使用 H20 GPU、DDR5 与多 NVMe 配置测试多种负载；结论绑定该存储层级和 co-activation 稳定性。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17803v1 HTML — §8.2 Overall Performance [facet=evaluation]; https://arxiv.org/html/2603.17803v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17803v1.html; sha256:e0f3b6194f2590aad0612f1256df993f3d949997dccaa5087fbd9f3b673f10a9`。

**Trade-off / failure / coexistence**：关联感知提高并行带宽但需要 profiling，分布漂移会使布局失效；小 KV 或 DRAM 足够时无需 SSD 层。

<!-- claim:SF-2026-ARXIV-2603-17803:start -->**Claim Boundary**：只支持 arXiv:2603.17803v1 §4 Design Overview 的机制与 §8.2 Overall Performance 的公开 workload；§8.4 Sensitivity Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17803:end -->
<!-- review:SF-2026-ARXIV-2603-17803:end -->
### EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards

<!-- review:SF-2026-ARXIV-2603-17808:start -->
**问题**：仅预测未来视频不能说明动作为何导致状态变化，world model 难以支持可控 planning。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：论文联合学习 observation transition 与 inverse action，使 latent dynamics 同时受前向可预测性和动作可辨识性约束。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.17808v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.17808v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17808v1.html; sha256:c72bf786797d8b9611a198efb0c4704b2a71b4cb6351b18bb5395d0756eb15c7`。

**Evaluation contract 与未证明部分**：公开任务支持所测环境的 rollout 与 action recovery；不证明 latent state 具有真实因果语义。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.17808v1 HTML — §Appendix 0.A Detailed Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.17808v1; papers/2026/03/_sources/daily-20260319/exact-v1-bodies/2603.17808v1.html; sha256:c72bf786797d8b9611a198efb0c4704b2a71b4cb6351b18bb5395d0756eb15c7`。

**Trade-off / failure / coexistence**：联合目标增加训练耦合，错误 inverse model 会扭曲状态；纯生成工作负载无需动作约束。

<!-- claim:SF-2026-ARXIV-2603-17808:start -->**Claim Boundary**：只支持 arXiv:2603.17808v1 §4 Method 的机制与 §Appendix 0.A Detailed Experimental Results 的公开 workload；§5.6 Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-17808:end -->
<!-- review:SF-2026-ARXIV-2603-17808:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-16938 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-16938 |
| SF-2026-ARXIV-2603-17104 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17104 |
| SF-2026-ARXIV-2603-17117 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17117 |
| SF-2026-ARXIV-2603-17170 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17170 |
| SF-2026-ARXIV-2603-17244 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17244 |
| SF-2026-ARXIV-2603-17357 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17357 |
| SF-2026-ARXIV-2603-17445 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17445 |
| SF-2026-ARXIV-2603-17456 | score_7_9 | selected | DA-20260319-08 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260319-08 |
| SF-2026-ARXIV-2603-17573 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17573 |
| SF-2026-ARXIV-2603-17673 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17673 |
| SF-2026-ARXIV-2603-17787 | score_7_9 | selected | DA-20260319-11 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260319-11 |
| SF-2026-ARXIV-2603-17803 | score_7_9;potential_books_delta | selected | DA-20260319-12 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260319-12 |
| SF-2026-ARXIV-2603-17808 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-17808 |

<!-- analysis-decision:SF-2026-ARXIV-2603-16938:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-16938:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17104:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17104:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17117:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17117:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17170:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17170:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17244:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17244:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17357:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17357:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17445:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17445:end -->
<!-- analysis:DA-20260319-08:start -->
### Multi-stage Flow Scheduling for LLM Serving

LLM serving 的 prefill、decode 与 KV transfer 共享多阶段网络路径，单队列看不到下游拥塞导致的 TTFT 违约。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：MFS 用 defer-and-promote 在多级队列中延迟非紧急 flow，并依据阶段进展提升优先级，从控制通信 flow 而非只排 GPU request。 其公开验证边界为：8 台服务器、每台 4 张 RTX 3090 的 testbed 给出端到端结果；不同 fabric、模型和 SLO 下的排序仍需重验。 新增代价与回退条件为：多阶段状态改善 deadline 管理但会增加队列维护和 starvation 风险；单阶段或低争用负载仍适合简单 FIFO。
<!-- analysis:DA-20260319-08:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17573:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17573:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17673:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17673:end -->
<!-- analysis:DA-20260319-11:start -->
### Governed Memory: A Production Architecture for Multi-Agent Workflows

多个 agent 对同一实体各自写 memory，会产生冲突、不可追踪派生与跨 workflow 数据泄漏。 旧路径在其原约束下仍合理：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。 本 family 的设计变化是：论文提出共享 governed memory layer，用 identity、provenance、temporal anchor 与写入 quality gate 统一多 agent 的读写契约。 其公开验证边界为：验证依赖 domain rubric、trace capture 和启发式质量分，能说明架构可运行但不能证明语义质量判定可靠。 新增代价与回退条件为：治理层提高可追责性，却成为集中式状态和策略瓶颈；隔离任务或短生命周期 agent 可保留私有 memory。
<!-- analysis:DA-20260319-11:end -->
<!-- analysis:DA-20260319-12:start -->
### Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs

KV offload 到单 SSD 时，相关条目常被一起请求，随机布局使多盘带宽无法并行利用。 旧路径在其原约束下仍合理：完整、逐 token 保存 KV，换取语义透明和最低重算风险。 本 family 的设计变化是：Swarm 离线学习 KV co-activation，按关联图跨 SSD 放置，并在在线阶段协同检索、更新和缓存。 其公开验证边界为：公开系统使用 H20 GPU、DDR5 与多 NVMe 配置测试多种负载；结论绑定该存储层级和 co-activation 稳定性。 新增代价与回退条件为：关联感知提高并行带宽但需要 profiling，分布漂移会使布局失效；小 KV 或 DRAM 足够时无需 SSD 层。
<!-- analysis:DA-20260319-12:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-17808:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-17808:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-16938 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#capability-access-control-可以前移到训练状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-16938 | delta:SF-2026-ARXIV-2603-16938 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-16938 |
| SF-2026-ARXIV-2603-17104 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17104 | delta:SF-2026-ARXIV-2603-17104 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17104 |
| SF-2026-ARXIV-2603-17117 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17117 | delta:SF-2026-ARXIV-2603-17117 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17117 |
| SF-2026-ARXIV-2603-17170 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#capability-access-control-可以前移到训练状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17170 | delta:SF-2026-ARXIV-2603-17170 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17170 |
| SF-2026-ARXIV-2603-17244 | AGENT-MEMORY | books/part-07-agent/77-memory.md#从按需读取到选择性主动干预 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17244 | delta:SF-2026-ARXIV-2603-17244 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17244 |
| SF-2026-ARXIV-2603-17357 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#已披露漏洞要沿-design-lineage-搜索变体 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17357 | delta:SF-2026-ARXIV-2603-17357 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17357 |
| SF-2026-ARXIV-2603-17445 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#小结 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17445 | delta:SF-2026-ARXIV-2603-17445 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17445 |
| SF-2026-ARXIV-2603-17456 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17456 | delta:SF-2026-ARXIV-2603-17456 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17456 |
| SF-2026-ARXIV-2603-17573 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#自检问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17573 | delta:SF-2026-ARXIV-2603-17573 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17573 |
| SF-2026-ARXIV-2603-17673 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17673 | delta:SF-2026-ARXIV-2603-17673 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17673 |
| SF-2026-ARXIV-2603-17787 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17787 | delta:SF-2026-ARXIV-2603-17787 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17787 |
| SF-2026-ARXIV-2603-17803 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从不可逆-eviction-到可恢复的分层-recall (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17803 | delta:SF-2026-ARXIV-2603-17803 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-17803 |
| SF-2026-ARXIV-2603-17808 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#sparse-keyframe-prediction-是-dense-rollout-之前的-planner-branch (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-17808 | delta:SF-2026-ARXIV-2603-17808 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-17808 |

<!-- books-review:SF-2026-ARXIV-2603-16938:start -->
### Cryptographic Runtime Governance for Autonomous AI Systems: The Aegis Architecture for Verifiable Policy Enforcement — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-16938:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：安全数据闭环还可由当前 policy 生成 adversarial candidates，再由独立 guard / outcome policy 筛选后进入训练。它能把静态红队集扩展到当前模型暴露的 failure frontier，却同时制造 self-confirmation 风险：generator 与 guard 若共享模型家族、prompt 或表示盲点，可能一致地把危险样本标成安全；只保留通过 guard 的样本还会隐藏 false negative。因而 generated sample、generator checkpoint、guard version、policy taxonomy、人工复核切片和最终 deployment gate 必须分开保存。该机制适合作为受控 data augmentation，不能取代 output-time enforcement 或独立 red-team evaluation。<!-- existing:SF-2026-ARXIV-2603-16938:end -->

<!-- delta:SF-2026-ARXIV-2603-16938:start -->新证据差异：Aegis 将不可变 policy、运行时许可与加密审计链绑定，使 policy decision 成为执行前条件。<!-- delta:SF-2026-ARXIV-2603-16938:end -->

边界：只支持 arXiv:2603.16938v1 §8. Methodology 的机制与 §vi. Proofing and Validation 的公开 workload；§11. Limitations and Open Questions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-16938:end -->
<!-- books-review:SF-2026-ARXIV-2603-17104:start -->
### When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17104:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-17104:end -->

<!-- delta:SF-2026-ARXIV-2603-17104:start -->新证据差异：ProjectGuard 维护同步的 durable semantic state 与项目 artifact 视图，把新约束、决策和依据持续合并后再提供给 agent。<!-- delta:SF-2026-ARXIV-2603-17104:end -->

边界：只支持 arXiv:2603.17104v1 §5.1 Method 的机制与 §3.3 Benchmark Fairness Validation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17104:end -->
<!-- books-review:SF-2026-ARXIV-2603-17117:start -->
### MosaicMem: Hybrid Spatial Memory for Controllable Video World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17117:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：一个模型能生成逼真视频，是否已经“理解世界”？能够预测下一帧，是否足以支持 planning？World Model 与 simulator、Agent Memory 有何边界？模型在内部 imagined rollout 时，谁保存事实状态，谁保存预测状态，又怎样在新 observation 到来后修正？<!-- existing:SF-2026-ARXIV-2603-17117:end -->

<!-- delta:SF-2026-ARXIV-2603-17117:start -->新证据差异：MosaicMem 把 patch 提升到 3D 以定位/检索，同时由生成模型原生条件保留动态内容，形成显式与隐式 memory 的混合。<!-- delta:SF-2026-ARXIV-2603-17117:end -->

边界：只支持 arXiv:2603.17117v1 §2 Methodology 的机制与 §4 Evaluation 的公开 workload；§4.2 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17117:end -->
<!-- books-review:SF-2026-ARXIV-2603-17170:start -->
### Beyond OAuth: Task-Scoped Authorization for AI Agents via Natural Language Slices — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17170:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：训练数据过滤也可以前移 capability boundary，但粒度不同。Document removal 改变整段分布；token-level loss mask 可以保留上下文、只阻断目标位置的梯度；token removal 更强，却会破坏 syntax 与 distribution。 三者都依赖 relevance classifier，不能从“被标成敏感”推出该 token 对能力具有完整因果贡献，也不能阻止 tool/in-context 重新获得能力。Classifier、mask policy、training revision 与 held-out capability evaluation 必须绑定；output policy 和 tool authorization 仍不可删除。该路线保持 `Status: Experimental`。<!-- existing:SF-2026-ARXIV-2603-17170:end -->

<!-- delta:SF-2026-ARXIV-2603-17170:start -->新证据差异：task-scoped slice 从自然语言任务派生 operation predicate，并在跨服务执行时携带、缩减和验证该谓词。<!-- delta:SF-2026-ARXIV-2603-17170:end -->

边界：只支持 arXiv:2603.17170v1 §4.1 Implementation on AgentDojo 的机制与 §5 Evaluation 的公开 workload；§6 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17170:end -->
<!-- books-review:SF-2026-ARXIV-2603-17244:start -->
### Graph-Native Cognitive Memory for AI Agents: Formal Belief Revision Semantics for Versioned Memory Architectures — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17244:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：Bank 仍拥有事实、来源、valid time 与 supersession；controller 只拥有“何时值得打断”的策略状态，不拥有事实真值，也不能绕过 authorization。每次提醒都应引用具体 memory units，并记录 controller revision、触发信号、Context cost 和后续 outcome。评估也不能只看最终 success：至少要区分正确保持沉默、错误介入、关键时刻漏介入，以及提醒是否真的由可授权 evidence 支撑。<!-- existing:SF-2026-ARXIV-2603-17244:end -->

<!-- delta:SF-2026-ARXIV-2603-17244:start -->新证据差异：该工作用 graph-native、versioned belief node 和形式化 revision operator 表达 provenance、冲突与 consolidation。<!-- delta:SF-2026-ARXIV-2603-17244:end -->

边界：只支持 arXiv:2603.17244v1 §2.1 Agent Memory Architectures 的机制与 §15.2 LoCoMo Benchmark Evaluation 的公开 workload；§15.9 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17244:end -->
<!-- books-review:SF-2026-ARXIV-2603-17357:start -->
### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17357:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：TEE/attestation 只保护声明的 boundary，不证明模型质量、host I/O、side effect 或所有 accelerator computation； sampling 又以审计成本换 detection probability。CPU-only trusted boundary、commitment state、nonce/replay protection 与 failure policy 都必须显式。IMMACULATE 的作者实验提供了 service-integrity 机制证据，但其 threat model、硬件条件与未公开生产 artifact 不支持通用 latency 或完整性保证。<!-- existing:SF-2026-ARXIV-2603-17357:end -->

<!-- delta:SF-2026-ARXIV-2603-17357:start -->新证据差异：WebPII 用合成电商 UI、细粒度 PII taxonomy 和部分填写状态定义 anticipatory detection benchmark。<!-- delta:SF-2026-ARXIV-2603-17357:end -->

边界：只支持 arXiv:2603.17357v1 §3.2.1 Text-Based Methods 的机制与 §3.3 Results 的公开 workload；§4.2 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17357:end -->
<!-- books-review:SF-2026-ARXIV-2603-17445:start -->
### When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Auditing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17445:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：Trace 让请求经过多个控制面和数据面时仍保留 causal context。好的 tracing 记录关键边界与决策，而不是最大化 span 数量。下一章将可观测事实转换为成本归因与优化约束。<!-- existing:SF-2026-ARXIV-2603-17445:end -->

<!-- delta:SF-2026-ARXIV-2603-17445:start -->新证据差异：IET 在生成阶段嵌入可恢复的隐式 provenance，使最终文本成为最小审计载体。<!-- delta:SF-2026-ARXIV-2603-17445:end -->

边界：只支持 arXiv:2603.17445v1 §3.2 Experimental Design 的机制与 §3.5 Evaluation 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17445:end -->
<!-- books-review:SF-2026-ARXIV-2603-17456:start -->
### Multi-stage Flow Scheduling for LLM Serving — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17456:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-17456:end -->

<!-- delta:SF-2026-ARXIV-2603-17456:start -->新证据差异：MFS 用 defer-and-promote 在多级队列中延迟非紧急 flow，并依据阶段进展提升优先级，从控制通信 flow 而非只排 GPU request。<!-- delta:SF-2026-ARXIV-2603-17456:end -->

边界：只支持 arXiv:2603.17456v1 §4.1. Design Challenges 的机制与 §6.1. Experiments setup 的公开 workload；§2.3. Limitation of Existing Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17456:end -->
<!-- books-review:SF-2026-ARXIV-2603-17573:start -->
### HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17573:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：1. Speculative Decoding 为什么需要 draft model 和 target model？ 2. 为什么生成是串行的，但验证候选 token 可以并行？ 3. 为什么它不是简单的小模型替代？ 4. acceptance rate 对加速效果有什么影响？ 5. `min(1,p/q)` 与 residual sampling 怎样保持 target distribution？ 6. 为什么 acceptance rate 高仍不保证端到端加速？ 7. Speculative Decoding 会给 KV Cache 和 batching 带来哪些额外复杂度？ 8. 为什么 lossy verification 不能只被描述为 runtime optimization？ 9. 含 truncation policy 的 verification 为什么必须使用 matched-policy baseline？ 10. 为什么 draft checkpoint 必须与 target revision、tokenizer 和 runtime 一起版本化？ 11. Edge/cloud speculation 中，为什么 verify depth 必须同时看到网络状态与 target capacity？ 12. 为什么 hybrid attention/recurrent model 的 speculative rollback 不能只移动 KV cached-length pointer？<!-- existing:SF-2026-ARXIV-2603-17573:end -->

<!-- delta:SF-2026-ARXIV-2603-17573:start -->新证据差异：论文为动作序列建立 draft-and-verify，并让接受/回滚与 action chunk 边界一致。<!-- delta:SF-2026-ARXIV-2603-17573:end -->

边界：只支持 arXiv:2603.17573v1 §6 HeiSD Framework Implementation 的机制与 §7.2 Evaluation Results 的公开 workload；§7.3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17573:end -->
<!-- books-review:SF-2026-ARXIV-2603-17673:start -->
### Towards Reliable Local Security Agents: Verifiable Post-Training for Linux Privilege Escalation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17673:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2603-17673:end -->

<!-- delta:SF-2026-ARXIV-2603-17673:start -->新证据差异：该工作把可验证安全约束与 action trajectory 对齐，用执行结果为策略更新提供分步信号。<!-- delta:SF-2026-ARXIV-2603-17673:end -->

边界：只支持 arXiv:2603.17673v1 §Cost Methodology 的机制与 §V-A Main Results 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17673:end -->
<!-- books-review:SF-2026-ARXIV-2603-17787:start -->
### Governed Memory: A Production Architecture for Multi-Agent Workflows — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17787:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-17787:end -->

<!-- delta:SF-2026-ARXIV-2603-17787:start -->新证据差异：论文提出共享 governed memory layer，用 identity、provenance、temporal anchor 与写入 quality gate 统一多 agent 的读写契约。<!-- delta:SF-2026-ARXIV-2603-17787:end -->

边界：只支持 arXiv:2603.17787v1 §3 Architecture Overview 的机制与 §8.11 External Benchmark Validation: LoCoMo 的公开 workload；§9.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17787:end -->
<!-- books-review:SF-2026-ARXIV-2603-17803:start -->
### Swarm: Co-Activation Aware KVCache Offloading Across Multiple SSDs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17803:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：当 cold tier 从单一 host memory 扩展到多块 SSD，容量不再是主要矛盾，访问并行度和数据布局才是。简单 hash 或 round-robin striping 假设每个 KV block 独立且请求分布均匀；实际检索若经常共同激活一组历史 blocks， 它们落到同一设备就会形成热点。可选分支可以离线学习 co-activation graph，把相关 block 分散到不同设备， 在线再协同 fetch、更新 hot cache：<!-- existing:SF-2026-ARXIV-2603-17803:end -->

<!-- delta:SF-2026-ARXIV-2603-17803:start -->新证据差异：Swarm 离线学习 KV co-activation，按关联图跨 SSD 放置，并在在线阶段协同检索、更新和缓存。<!-- delta:SF-2026-ARXIV-2603-17803:end -->

边界：只支持 arXiv:2603.17803v1 §4 Design Overview 的机制与 §8.2 Overall Performance 的公开 workload；§8.4 Sensitivity Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-17803:end -->
<!-- books-review:SF-2026-ARXIV-2603-17808:start -->
### EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-17808:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：逐帧 video rollout 保留细粒度 dynamics，在控制频率高、接触过程关键时不可替代；任务级规划有时只需要判断“执行一段 action 后关键状态会是什么”。Image-editing model 可以把当前 observation、goal 与 action proposal 编译成少量 future keyframes，再由 action predictor 检查是否存在可行过渡。它改变的是 rollout granularity：world-model owner 只产生 sparse planning evidence，controller 仍必须用真实 observation 或 simulator 验证后才能提交物理 action。<!-- existing:SF-2026-ARXIV-2603-17808:end -->

<!-- delta:SF-2026-ARXIV-2603-17808:start -->新证据差异：论文联合学习 observation transition 与 inverse action，使 latent dynamics 同时受前向可预测性和动作可辨识性约束。<!-- delta:SF-2026-ARXIV-2603-17808:end -->

边界：只支持 arXiv:2603.17808v1 §4 Method 的机制与 §Appendix 0.A Detailed Experimental Results 的公开 workload；§5.6 Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-17808:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260319-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260319 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260319-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260319-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260319-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260319/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

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
