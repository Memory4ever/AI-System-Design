# Daily Research — 2026-03-09

**Research Date:** 2026-03-09

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-08 09:00:00 ～ 2026-03-09 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=527/527/527；denominator=22、pre-denominator closures=505。exact-v1 Review complete=22、blocked=0；Integrate 建议=3。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-09 |
| Window End | 2026-03-09 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260309-AUTHOR-22 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-08T09:00:00+08:00 | 2026-03-09T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 527/527 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 527 | SF-2026-ARXIV-2603-05517;SF-2026-ARXIV-2603-05520;SF-2026-ARXIV-2603-05553;SF-2026-ARXIV-2603-05578;SF-2026-ARXIV-2603-05637;SF-2026-ARXIV-2603-05692;SF-2026-ARXIV-2603-05754;SF-2026-ARXIV-2603-05800;SF-2026-ARXIV-2603-05881;SF-2026-ARXIV-2603-05910;SF-2026-ARXIV-2603-05912;SF-2026-ARXIV-2603-05931;SF-2026-ARXIV-2603-06001;SF-2026-ARXIV-2603-06003;SF-2026-ARXIV-2603-06007;SF-2026-ARXIV-2603-06081;SF-2026-ARXIV-2603-06199;SF-2026-ARXIV-2603-06331;SF-2026-ARXIV-2603-06350;SF-2026-ARXIV-2603-06365;SF-2026-ARXIV-2603-06394;SF-2026-ARXIV-2603-06403 | pages=100; prefixes=00..99; final_cursor=end; registered=527; screened=527; retained=22; closure=505 | 2026-03-09T01:00:00+00:00 | screening-ledger-final.json#sha256=85d0626354261c541cd090295c125b7666eb2d65b04992d2d8006ebd4e67c867; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260309:start -->作者侧已逐项筛选全部 527 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260309:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | arXiv:2603.05517v1 | paper-v1:2603.05517 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05517 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05517 | no |
| SF-2026-ARXIV-2603-05520 | arXiv:2603.05520v1 | paper-v1:2603.05520 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05520 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05520 | no |
| SF-2026-ARXIV-2603-05553 | arXiv:2603.05553v1 | paper-v1:2603.05553 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05553 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05553 | no |
| SF-2026-ARXIV-2603-05578 | arXiv:2603.05578v1 | paper-v1:2603.05578 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05578 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05578 | no |
| SF-2026-ARXIV-2603-05637 | arXiv:2603.05637v1 | paper-v1:2603.05637 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05637 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05637 | no |
| SF-2026-ARXIV-2603-05692 | arXiv:2603.05692v1 | paper-v1:2603.05692 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05692 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05692 | no |
| SF-2026-ARXIV-2603-05754 | arXiv:2603.05754v1 | paper-v1:2603.05754 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05754 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05754 | no |
| SF-2026-ARXIV-2603-05800 | arXiv:2603.05800v1 | paper-v1:2603.05800 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05800 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-05800 | no |
| SF-2026-ARXIV-2603-05881 | arXiv:2603.05881v1 | paper-v1:2603.05881 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05881 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05881 | no |
| SF-2026-ARXIV-2603-05910 | arXiv:2603.05910v1 | paper-v1:2603.05910 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05910 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05910 | no |
| SF-2026-ARXIV-2603-05912 | arXiv:2603.05912v1 | paper-v1:2603.05912 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05912 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05912 | no |
| SF-2026-ARXIV-2603-05931 | arXiv:2603.05931v1 | paper-v1:2603.05931 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05931 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-05931 | no |
| SF-2026-ARXIV-2603-06001 | arXiv:2603.06001v1 | paper-v1:2603.06001 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06001 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06001 | no |
| SF-2026-ARXIV-2603-06003 | arXiv:2603.06003v1 | paper-v1:2603.06003 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06003 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06003 | no |
| SF-2026-ARXIV-2603-06007 | arXiv:2603.06007v1 | paper-v1:2603.06007 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06007 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06007 | no |
| SF-2026-ARXIV-2603-06081 | arXiv:2603.06081v1 | paper-v1:2603.06081 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06081 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06081 | no |
| SF-2026-ARXIV-2603-06199 | arXiv:2603.06199v1 | paper-v1:2603.06199 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06199 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06199 | no |
| SF-2026-ARXIV-2603-06331 | arXiv:2603.06331v1 | paper-v1:2603.06331 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06331 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06331 | no |
| SF-2026-ARXIV-2603-06350 | arXiv:2603.06350v1 | paper-v1:2603.06350 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06350 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-06350 | no |
| SF-2026-ARXIV-2603-06365 | arXiv:2603.06365v1 | paper-v1:2603.06365 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06365 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06365 | no |
| SF-2026-ARXIV-2603-06394 | arXiv:2603.06394v1 | paper-v1:2603.06394 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06394 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06394 | no |
| SF-2026-ARXIV-2603-06403 | arXiv:2603.06403v1 | paper-v1:2603.06403 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06403 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06403 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | RP-96fd4c556a71319e | standard | arXiv:2603.05517v1 | SRC-ARXIV@arXiv:2603.05517v1 | arXiv:2603.05517v1 HTML — §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks [facet=method]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv:2603.05517v1 HTML — §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) [facet=evaluation]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv:2603.05517v1 HTML — §O.1 Limitations and Open Failure Modes [facet=limitations]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv exact-v1 identity https://arxiv.org/abs/2603.05517v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05517 | complete |
| SF-2026-ARXIV-2603-05520 | RP-a8834f9393096a87 | standard | arXiv:2603.05520v1 | SRC-ARXIV@arXiv:2603.05520v1 | arXiv:2603.05520v1 HTML — §4.3 Design Implications [facet=method]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv:2603.05520v1 HTML — §7.1 Overall Performance on Medical and Financial Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv:2603.05520v1 HTML — §8 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05520v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05520 | complete |
| SF-2026-ARXIV-2603-05553 | RP-15785024b5ba4312 | standard | arXiv:2603.05553v1 | SRC-ARXIV@arXiv:2603.05553v1 | arXiv:2603.05553v1 HTML — §3.3.1 Architecture [facet=method]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv:2603.05553v1 HTML — §4.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv:2603.05553v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05553v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05553 | complete |
| SF-2026-ARXIV-2603-05578 | RP-e857fb474c66952d | standard | arXiv:2603.05578v1 | SRC-ARXIV@arXiv:2603.05578v1 | arXiv:2603.05578v1 HTML — §Appendix A Evaluation Methodology Details [facet=method]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv:2603.05578v1 HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv:2603.05578v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv exact-v1 identity https://arxiv.org/abs/2603.05578v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05578 | complete |
| SF-2026-ARXIV-2603-05637 | RP-dc7e253e72c0c112 | standard | arXiv:2603.05637v1 | SRC-ARXIV@arXiv:2603.05637v1 | arXiv:2603.05637v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv:2603.05637v1 HTML — §3.3. Taxonomy Creation and Validation [facet=evaluation]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv:2603.05637v1 HTML — §7. Conclusion and Future Works [facet=limitations]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05637v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05637 | complete |
| SF-2026-ARXIV-2603-05692 | RP-85ab44e4499f160c | standard | arXiv:2603.05692v1 | SRC-ARXIV@arXiv:2603.05692v1 | arXiv:2603.05692v1 HTML — §2.2. Overview of Llama 3.1-70B/-405B Models [facet=method]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv:2603.05692v1 HTML — §3. In-House Simulator and Its Validation [facet=evaluation]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv:2603.05692v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05692v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05692 | complete |
| SF-2026-ARXIV-2603-05754 | RP-62a3782416cbb04a | standard | arXiv:2603.05754v1 | SRC-ARXIV@arXiv:2603.05754v1 | arXiv:2603.05754v1 HTML — §III-A System Architecture and Adaptation Strategy [facet=method]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv:2603.05754v1 HTML — §V-C Exploratory Mechanism Analysis: Attention Ablation [facet=evaluation]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv:2603.05754v1 HTML — §V-B1 Limitations of RGB-Only and RGB-D Variants [facet=limitations]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05754v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05754 | complete |
| SF-2026-ARXIV-2603-05800 | RP-596cee8794398ded | deep | arXiv:2603.05800v1 | SRC-ARXIV@arXiv:2603.05800v1 | arXiv:2603.05800v1 HTML — §4.7. Implementation [facet=method]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv:2603.05800v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv:2603.05800v1 HTML — §7. Conclusions [facet=limitations]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv exact-v1 identity https://arxiv.org/abs/2603.05800v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05800 | complete |
| SF-2026-ARXIV-2603-05881 | RP-1f5f15cfd4e878f5 | standard | arXiv:2603.05881v1 | SRC-ARXIV@arXiv:2603.05881v1 | arXiv:2603.05881v1 HTML — §3.2 Confidence-First Paradigm Definition [facet=method]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv:2603.05881v1 HTML — §4.1.2 Evaluation Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv:2603.05881v1 HTML — §6 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv exact-v1 identity https://arxiv.org/abs/2603.05881v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05881 | complete |
| SF-2026-ARXIV-2603-05910 | RP-c11a05f52e34973c | standard | arXiv:2603.05910v1 | SRC-ARXIV@arXiv:2603.05910v1 | arXiv:2603.05910v1 HTML — §C.2 Tool Designer in Saturation Strategy [facet=method]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv:2603.05910v1 HTML — §4.4 State-Wise User Simulation and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv:2603.05910v1 HTML — §6 Conclusions [facet=limitations]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05910v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05910 | complete |
| SF-2026-ARXIV-2603-05912 | RP-56d93815581b9ece | standard | arXiv:2603.05912v1 | SRC-ARXIV@arXiv:2603.05912v1 | arXiv:2603.05912v1 HTML — §4.1 Methodology: The Micro-Gold Protocol [facet=method]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv:2603.05912v1 HTML — §7.3 Results on Other Factuality Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv:2603.05912v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05912v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05912 | complete |
| SF-2026-ARXIV-2603-05931 | RP-cab5bc9837c5db14 | deep | arXiv:2603.05931v1 | SRC-ARXIV@arXiv:2603.05931v1 | arXiv:2603.05931v1 HTML — §IV-E System Overview [facet=method]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv:2603.05931v1 HTML — §VI-E Ablation Analysis [facet=evaluation]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv:2603.05931v1 HTML — §VIII Conclusion [facet=limitations]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05931v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05931 | complete |
| SF-2026-ARXIV-2603-06001 | RP-8fcff515ced2225b | standard | arXiv:2603.06001v1 | SRC-ARXIV@arXiv:2603.06001v1 | arXiv:2603.06001v1 HTML — §3.2 Contradiction Taxonomy and Design Principles [facet=method]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv:2603.06001v1 HTML — §5.6 Real-World Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv:2603.06001v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06001v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06001 | complete |
| SF-2026-ARXIV-2603-06003 | RP-a969a52754a4b94e | standard | arXiv:2603.06003v1 | SRC-ARXIV@arXiv:2603.06003v1 | arXiv:2603.06003v1 HTML — §2.3 Other Compression Methods [facet=method]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv:2603.06003v1 HTML — §4.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv:2603.06003v1 HTML — §Appendix C Limitations [facet=limitations]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv exact-v1 identity https://arxiv.org/abs/2603.06003v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06003 | complete |
| SF-2026-ARXIV-2603-06007 | RP-44993cf2f29bc76c | standard | arXiv:2603.06007v1 | SRC-ARXIV@arXiv:2603.06007v1 | arXiv:2603.06007v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv:2603.06007v1 HTML — §4 Evaluation and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv:2603.06007v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv exact-v1 identity https://arxiv.org/abs/2603.06007v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06007 | complete |
| SF-2026-ARXIV-2603-06081 | RP-524316fc7207f84e | standard | arXiv:2603.06081v1 | SRC-ARXIV@arXiv:2603.06081v1 | arXiv:2603.06081v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv:2603.06081v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv:2603.06081v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06081v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06081 | complete |
| SF-2026-ARXIV-2603-06199 | RP-104be6310eff5ea2 | standard | arXiv:2603.06199v1 | SRC-ARXIV@arXiv:2603.06199v1 | arXiv:2603.06199v1 HTML — §3.3 Comparison with Previous Methods. [facet=method]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv:2603.06199v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv:2603.06199v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06199v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06199 | complete |
| SF-2026-ARXIV-2603-06331 | RP-3b853e2f31ed6527 | standard | arXiv:2603.06331v1 | SRC-ARXIV@arXiv:2603.06331v1 | arXiv:2603.06331v1 HTML — §4.1 Curvature-guided Heterogeneous Token Prediction [facet=method]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv:2603.06331v1 HTML — §5.2 World Generation Results [facet=evaluation]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv:2603.06331v1 HTML — §Failure of Uniform Strategies. [facet=limitations]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06331v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06331 | complete |
| SF-2026-ARXIV-2603-06350 | RP-fc8fc6579f986b7e | deep | arXiv:2603.06350v1 | SRC-ARXIV@arXiv:2603.06350v1 | arXiv:2603.06350v1 HTML — §3.2. Architecture and Workflow [facet=method]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv:2603.06350v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv:2603.06350v1 HTML — §8. Conclusion [facet=limitations]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv exact-v1 identity https://arxiv.org/abs/2603.06350v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06350 | complete |
| SF-2026-ARXIV-2603-06365 | RP-c8cf6f39c28d4c25 | standard | arXiv:2603.06365v1 | SRC-ARXIV@arXiv:2603.06365v1 | arXiv:2603.06365v1 HTML — §3 ESAA-Security Architecture [facet=method]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv:2603.06365v1 HTML — §6 Evaluation Design and Research Questions [facet=evaluation]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv:2603.06365v1 HTML — §8 Discussion, Limitations, and Threats to Validity [facet=limitations]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06365v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06365 | complete |
| SF-2026-ARXIV-2603-06394 | RP-d242a92d3a73fddc | standard | arXiv:2603.06394v1 | SRC-ARXIV@arXiv:2603.06394v1 | arXiv:2603.06394v1 HTML — §5.1 Architecture overview [facet=method]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv:2603.06394v1 HTML — §5.3 Validation framework [facet=evaluation]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv:2603.06394v1 HTML — §6.5 Future work [facet=limitations]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06394v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06394 | complete |
| SF-2026-ARXIV-2603-06403 | RP-fcc14a57d3bada47 | standard | arXiv:2603.06403v1 | SRC-ARXIV@arXiv:2603.06403v1 | arXiv:2603.06403v1 HTML — §3.1 Reward and Cost Predictor Design [facet=method]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv:2603.06403v1 HTML — §5.3 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv:2603.06403v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06403v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06403 | complete |

### Source Reviews

### Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents

<!-- review:SF-2026-ARXIV-2603-05517:start -->
**问题**：`Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.05517v1 HTML — §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks [facet=method]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts)`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05517v1 HTML — §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) [facet=evaluation]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `O.1 Limitations and Open Failure Modes`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-05517:start -->**Claim Boundary**：只支持 arXiv:2603.05517v1 §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks 的机制与 §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) 的公开 workload；§O.1 Limitations and Open Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05517:end -->
<!-- review:SF-2026-ARXIV-2603-05517:end -->
### Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems

<!-- review:SF-2026-ARXIV-2603-05520:start -->
**问题**：`Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `4.3 Design Implications` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05520v1 HTML — §4.3 Design Implications [facet=method]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7.1 Overall Performance on Medical and Financial Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05520v1 HTML — §7.1 Overall Performance on Medical and Financial Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Conclusion and Future Work`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-05520:start -->**Claim Boundary**：只支持 arXiv:2603.05520v1 §4.3 Design Implications 的机制与 §7.1 Overall Performance on Medical and Financial Benchmarks 的公开 workload；§8 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05520:end -->
<!-- review:SF-2026-ARXIV-2603-05520:end -->
### EigenData: A Self-Evolving Multi-Agent Platform for Function-Calling Data Synthesis, Auditing, and Repair

<!-- review:SF-2026-ARXIV-2603-05553:start -->
**问题**：function-calling 数据的数据库、可执行环境、schema 与 trajectory 若分开生成，跨 artifact 错误无法归因。

**旧路径为何合理**：固定离线数据集让训练可复现，也避免在线选择反馈回路。

**约束变化与机制**：EigenData 让多个专责 agent 共享可验证 artifact graph，并以数据库终态而非轨迹表面匹配作为任务 oracle。

**State / data / control owner**：`TRAIN-DATA` 负责 样本 identity、选择策略、版本、provenance 与训练消费顺序；定位证据为 `arXiv:2603.05553v1 HTML — §3.3.1 Architecture [facet=method]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0`。

**Evaluation contract 与未证明部分**：BFCL-V3 修复案例只证明所测 schema、实现和轨迹错误能被该闭环发现；不证明自动修复对任意工具生态安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05553v1 HTML — §4.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0`。

**Trade-off / failure / coexistence**：闭环提升一致性却扩大生成器、测试器和 oracle 的共同故障域；人工冻结的小型工具集仍更易审计。

<!-- claim:SF-2026-ARXIV-2603-05553:start -->**Claim Boundary**：只支持 arXiv:2603.05553v1 §3.3.1 Architecture 的机制与 §4.3 Evaluation Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05553:end -->
<!-- review:SF-2026-ARXIV-2603-05553:end -->
### Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent

<!-- review:SF-2026-ARXIV-2603-05578:start -->
**问题**：只测 agent 是否最终完成任务，会把工具接口、实现与调用失败混成一个分数。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Tool-Genesis 从抽象需求开始，分别验证 interface compliance、functional correctness 与 downstream utility，使失败位置可归因。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05578v1 HTML — §Appendix A Evaluation Methodology Details [facet=method]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e`。

**Evaluation contract 与未证明部分**：基准证明其任务集合中一处早期接口缺陷会沿调用链放大；不证明该任务分布代表生产工具市场。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05578v1 HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e`。

**Trade-off / failure / coexistence**：诊断粒度提高证据价值但增加 oracle 和 sandbox 维护；预定义稳定工具仍可使用普通端到端测试。

<!-- claim:SF-2026-ARXIV-2603-05578:start -->**Claim Boundary**：只支持 arXiv:2603.05578v1 §Appendix A Evaluation Methodology Details 的机制与 §5.2 Experimental Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05578:end -->
<!-- review:SF-2026-ARXIV-2603-05578:end -->
### Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy

<!-- review:SF-2026-ARXIV-2603-05637:start -->
**问题**：`Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy` 检查的是 `AGENT-MCP` 中 跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。 是否会改变现有设计边界。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：exact-v1 的 `3. Methodology` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.05637v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.3. Taxonomy Creation and Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05637v1 HTML — §3.3. Taxonomy Creation and Validation [facet=evaluation]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7. Conclusion and Future Works`。固定工具集、单一信任域仍可保留较薄的 adapter。

<!-- claim:SF-2026-ARXIV-2603-05637:start -->**Claim Boundary**：只支持 arXiv:2603.05637v1 §3. Methodology 的机制与 §3.3. Taxonomy Creation and Validation 的公开 workload；§7. Conclusion and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05637:end -->
<!-- review:SF-2026-ARXIV-2603-05637:end -->
### Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks

<!-- review:SF-2026-ARXIV-2603-05692:start -->
**问题**：`Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `2.2. Overview of Llama 3.1-70B/-405B Models` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.05692v1 HTML — §2.2. Overview of Llama 3.1-70B/-405B Models [facet=method]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3. In-House Simulator and Its Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05692v1 HTML — §3. In-House Simulator and Its Validation [facet=evaluation]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Discussion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-05692:start -->**Claim Boundary**：只支持 arXiv:2603.05692v1 §2.2. Overview of Llama 3.1-70B/-405B Models 的机制与 §3. In-House Simulator and Its Validation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05692:end -->
<!-- review:SF-2026-ARXIV-2603-05692:end -->
### Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation

<!-- review:SF-2026-ARXIV-2603-05754:start -->
**问题**：`Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `III-A System Architecture and Adaptation Strategy` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.05754v1 HTML — §III-A System Architecture and Adaptation Strategy [facet=method]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V-C Exploratory Mechanism Analysis: Attention Ablation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05754v1 HTML — §V-C Exploratory Mechanism Analysis: Attention Ablation [facet=evaluation]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V-B1 Limitations of RGB-Only and RGB-D Variants`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-05754:start -->**Claim Boundary**：只支持 arXiv:2603.05754v1 §III-A System Architecture and Adaptation Strategy 的机制与 §V-C Exploratory Mechanism Analysis: Attention Ablation 的公开 workload；§V-B1 Limitations of RGB-Only and RGB-D Variants 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05754:end -->
<!-- review:SF-2026-ARXIV-2603-05754:end -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale

<!-- review:SF-2026-ARXIV-2603-05800:start -->
**问题**：多模态生成流同时包含持续到达、异质阶段和实时 deadline；把每个请求当成单次模型调用会隐藏跨阶段排队。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.05800v1 HTML — §4.7. Implementation [facet=method]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c`。

**Evaluation contract 与未证明部分**：作者在其公开模型、设备和请求分布上测量吞吐与尾延迟，足以支持所测实时 pipeline 的联合调度收益；未披露的跨集群网络、租户隔离和生产 SLO 不属于结论。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05800v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c`。

**Trade-off / failure / coexistence**：更细的阶段状态提升利用率，也增加队列、取消和中间结果失效复杂度；离线同质批处理仍适合静态流水线。

<!-- claim:SF-2026-ARXIV-2603-05800:start -->**Claim Boundary**：只支持 arXiv:2603.05800v1 §4.7. Implementation 的机制与 §5. Evaluation 的公开 workload；§7. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05800:end -->
<!-- review:SF-2026-ARXIV-2603-05800:end -->
### Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation

<!-- review:SF-2026-ARXIV-2603-05881:start -->
**问题**：`Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.2 Confidence-First Paradigm Definition` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05881v1 HTML — §3.2 Confidence-First Paradigm Definition [facet=method]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1.2 Evaluation Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05881v1 HTML — §4.1.2 Evaluation Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Limitations and Future Work`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05881:start -->**Claim Boundary**：只支持 arXiv:2603.05881v1 §3.2 Confidence-First Paradigm Definition 的机制与 §4.1.2 Evaluation Benchmarks 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05881:end -->
<!-- review:SF-2026-ARXIV-2603-05881:end -->
### The World Won't Stay Still: Programmable Evolution for Agent Benchmarks

<!-- review:SF-2026-ARXIV-2603-05910:start -->
**问题**：`The World Won't Stay Still: Programmable Evolution for Agent Benchmarks` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `C.2 Tool Designer in Saturation Strategy` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05910v1 HTML — §C.2 Tool Designer in Saturation Strategy [facet=method]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.4 State-Wise User Simulation and Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05910v1 HTML — §4.4 State-Wise User Simulation and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusions`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05910:start -->**Claim Boundary**：只支持 arXiv:2603.05910v1 §C.2 Tool Designer in Saturation Strategy 的机制与 §4.4 State-Wise User Simulation and Evaluation 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05910:end -->
<!-- review:SF-2026-ARXIV-2603-05910:end -->
### DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality

<!-- review:SF-2026-ARXIV-2603-05912:start -->
**问题**：`DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `4.1 Methodology: The Micro-Gold Protocol` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05912v1 HTML — §4.1 Methodology: The Micro-Gold Protocol [facet=method]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7.3 Results on Other Factuality Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05912v1 HTML — §7.3 Results on Other Factuality Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05912:start -->**Claim Boundary**：只支持 arXiv:2603.05912v1 §4.1 Methodology: The Micro-Gold Protocol 的机制与 §7.3 Results on Other Factuality Benchmarks 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05912:end -->
<!-- review:SF-2026-ARXIV-2603-05912:end -->
### A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA

<!-- review:SF-2026-ARXIV-2603-05931:start -->
**问题**：线性注意力 decode 受反复装载持久状态限制，单纯增加算术单元不能消除片外带宽瓶颈。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.05931v1 HTML — §IV-E System Overview [facet=method]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543`。

**Evaluation contract 与未证明部分**：FPGA 原型证明给定算子、精度和器件上的带宽/吞吐变化；它没有证明不同线性注意力变体或 GPU runtime 可获得相同比例收益。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05931v1 HTML — §VI-E Ablation Analysis [facet=evaluation]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543`。

**Trade-off / failure / coexistence**：持久化减少内存流量，却占用片上容量并绑定状态布局；短序列或状态无法容纳时，通用外存执行仍更灵活。

<!-- claim:SF-2026-ARXIV-2603-05931:start -->**Claim Boundary**：只支持 arXiv:2603.05931v1 §IV-E System Overview 的机制与 §VI-E Ablation Analysis 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05931:end -->
<!-- review:SF-2026-ARXIV-2603-05931:end -->
### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

<!-- review:SF-2026-ARXIV-2603-06001:start -->
**问题**：VLA 可在语言与场景矛盾时仍沿视觉先验行动，任务成功率因此掩盖 instruction-action coupling 失效。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：ICBench 固定视觉场景并注入矛盾指令；IGAR 在推理时重分配 attention，使语言约束重新进入动作生成。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.06001v1 HTML — §3.2 Contradiction Taxonomy and Design Principles [facet=method]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8`。

**Evaluation contract 与未证明部分**：三类 VLA、LIBERO 与 Franka 实验支持该 failure mode 和受限修复；不证明 attention weight 等于因果 grounding。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06001v1 HTML — §5.6 Real-World Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8`。

**Trade-off / failure / coexistence**：重校准无需训练但可能压制合理视觉反应；闭集一致指令下原策略仍有更低控制开销。

<!-- claim:SF-2026-ARXIV-2603-06001:start -->**Claim Boundary**：只支持 arXiv:2603.06001v1 §3.2 Contradiction Taxonomy and Design Principles 的机制与 §5.6 Real-World Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06001:end -->
<!-- review:SF-2026-ARXIV-2603-06001:end -->
### EvoESAP: Non-Uniform Expert Pruning for Sparse MoE

<!-- review:SF-2026-ARXIV-2603-06003:start -->
**问题**：MoE 部署受完整 expert pool 显存约束，而逐层统一剪枝忽略不同层对容量损失的敏感度。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：EvoESAP 把层内 expert 排序与跨层预算分开，用 teacher-forced acceptance proxy 搜索非均匀 sparsity。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.06003v1 HTML — §2.3 Other Compression Methods [facet=method]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd`。

**Evaluation contract 与未证明部分**：7B--30B、固定全局预算实验支持该搜索空间内的质量差异；不证明 proxy 在其他 router 或数据上保持排序。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06003v1 HTML — §4.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd`。

**Trade-off / failure / coexistence**：搜索与校准增加离线成本，且剪枝不可逆；显存足够或分布易漂移时保留完整 expert pool 更稳。

<!-- claim:SF-2026-ARXIV-2603-06003:start -->**Claim Boundary**：只支持 arXiv:2603.06003v1 §2.3 Other Compression Methods 的机制与 §4.2 Main results 的公开 workload；§Appendix C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06003:end -->
<!-- review:SF-2026-ARXIV-2603-06003:end -->
### MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing

<!-- review:SF-2026-ARXIV-2603-06007:start -->
**问题**：`MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `3 System Design` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.06007v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Evaluation and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06007v1 HTML — §4 Evaluation and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-06007:start -->**Claim Boundary**：只支持 arXiv:2603.06007v1 §3 System Design 的机制与 §4 Evaluation and Analysis 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06007:end -->
<!-- review:SF-2026-ARXIV-2603-06007:end -->
### Lyapunov Probes for Hallucination Detection in Large Foundation Models

<!-- review:SF-2026-ARXIV-2603-06081:start -->
**问题**：输出后分类器只关联表面答案，难表达知识边界附近对扰动不稳定的内部表示。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Lyapunov probe 以扰动下置信单调衰减为训练约束，把局部稳定性作为 hallucination 风险信号。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06081v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329`。

**Evaluation contract 与未证明部分**：作者跨文本/多模态数据的比较只支持所测 probe 与扰动协议；稳定表示不是事实正确性的充分条件。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06081v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329`。

**Trade-off / failure / coexistence**：需要内部激活、额外训练和校准，且 OOD 扰动会改变阈值；不可访问权重时仍需 evidence-based verifier。

<!-- claim:SF-2026-ARXIV-2603-06081:start -->**Claim Boundary**：只支持 arXiv:2603.06081v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06081:end -->
<!-- review:SF-2026-ARXIV-2603-06081:end -->
### FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling

<!-- review:SF-2026-ARXIV-2603-06199:start -->
**问题**：长上下文 prefill 的稀疏模式搜索若需要排序或累计 attention score，会吞掉跳算收益。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：FlashPrefill 联合发现 vertical、slash 与 block pattern，并用动态阈值直接裁剪长尾 block，改变 prefill execution plan。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.06199v1 HTML — §3.3 Comparison with Previous Methods. [facet=method]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63`。

**Evaluation contract 与未证明部分**：作者速度数字只属于所测模型、长度、kernel 与硬件；摘要不足以外推 27.78x 到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06199v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63`。

**Trade-off / failure / coexistence**：阈值搜索换来近似误差和 pattern metadata；短上下文或 exact attention 要求高时 dense prefill 仍合理。

<!-- claim:SF-2026-ARXIV-2603-06199:start -->**Claim Boundary**：只支持 arXiv:2603.06199v1 §3.3 Comparison with Previous Methods. 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06199:end -->
<!-- review:SF-2026-ARXIV-2603-06199:end -->
### WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching

<!-- review:SF-2026-ARXIV-2603-06331:start -->
**问题**：`WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `4.1 Curvature-guided Heterogeneous Token Prediction` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.06331v1 HTML — §4.1 Curvature-guided Heterogeneous Token Prediction [facet=method]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 World Generation Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06331v1 HTML — §5.2 World Generation Results [facet=evaluation]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Failure of Uniform Strategies.`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-06331:start -->**Claim Boundary**：只支持 arXiv:2603.06331v1 §4.1 Curvature-guided Heterogeneous Token Prediction 的机制与 §5.2 World Generation Results 的公开 workload；§Failure of Uniform Strategies. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06331:end -->
<!-- review:SF-2026-ARXIV-2603-06331:end -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing

<!-- review:SF-2026-ARXIV-2603-06350:start -->
**问题**：MoE serving 的冷门 expert 长期占据 GPU，会让峰值容量与平均利用率之间产生结构性浪费。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.06350v1 HTML — §3.2. Architecture and Workflow [facet=method]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a`。

**Evaluation contract 与未证明部分**：公开实验支持其工作负载下的成本/延迟取舍，但 serverless 冷启动、网络拓扑和 expert 热度稳定性限制外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06350v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a`。

**Trade-off / failure / coexistence**：弹性回收降低闲置成本，却把冷启动与跨节点通信引入 token 路径；高且稳定的 expert 利用率仍适合常驻部署。

<!-- claim:SF-2026-ARXIV-2603-06350:start -->**Claim Boundary**：只支持 arXiv:2603.06350v1 §3.2. Architecture and Workflow 的机制与 §6. Evaluation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06350:end -->
<!-- review:SF-2026-ARXIV-2603-06350:end -->
### ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code

<!-- review:SF-2026-ARXIV-2603-06365:start -->
**问题**：自由对话式安全审计没有不可变执行记录，启发式 agent 结论也难与真实仓库修改分离。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：ESAA-Security 让 agent 只提交结构化 intent，由 orchestrator 验证后写 append-only event log，再重放投影与 hash 校验。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.06365v1 HTML — §3 ESAA-Security Architecture [facet=method]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9`。

**Evaluation contract 与未证明部分**：公开稿提供体系和任务清单，能证明 contract 可表达；没有独立 artifact 时不能声称覆盖率或防护效果。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06365v1 HTML — §6 Evaluation Design and Research Questions [facet=evaluation]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9`。

**Trade-off / failure / coexistence**：事件溯源提高复算性但增加 schema、存储和投影一致性；小型人工审计仍可用普通报告链。

<!-- claim:SF-2026-ARXIV-2603-06365:start -->**Claim Boundary**：只支持 arXiv:2603.06365v1 §3 ESAA-Security Architecture 的机制与 §6 Evaluation Design and Research Questions 的公开 workload；§8 Discussion, Limitations, and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06365:end -->
<!-- review:SF-2026-ARXIV-2603-06365:end -->
### Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows

<!-- review:SF-2026-ARXIV-2603-06394:start -->
**问题**：`Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `5.1 Architecture overview` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.06394v1 HTML — §5.1 Architecture overview [facet=method]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.3 Validation framework`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06394v1 HTML — §5.3 Validation framework [facet=evaluation]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6.5 Future work`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-06394:start -->**Claim Boundary**：只支持 arXiv:2603.06394v1 §5.1 Architecture overview 的机制与 §5.3 Validation framework 的公开 workload；§6.5 Future work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06394:end -->
<!-- review:SF-2026-ARXIV-2603-06394:end -->
### Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling

<!-- review:SF-2026-ARXIV-2603-06403:start -->
**问题**：`Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `3.1 Reward and Cost Predictor Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.06403v1 HTML — §3.1 Reward and Cost Predictor Design [facet=method]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.3 Experimental Results and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06403v1 HTML — §5.3 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-06403:start -->**Claim Boundary**：只支持 arXiv:2603.06403v1 §3.1 Reward and Cost Predictor Design 的机制与 §5.3 Experimental Results and Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06403:end -->
<!-- review:SF-2026-ARXIV-2603-06403:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05800 | score_7_9;potential_books_delta | selected | DA-20260309-08 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-08 |
| SF-2026-ARXIV-2603-05931 | score_7_9;potential_books_delta | selected | DA-20260309-12 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-12 |
| SF-2026-ARXIV-2603-06350 | score_7_9;potential_books_delta | selected | DA-20260309-19 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-19 |

<!-- analysis:DA-20260309-08:start -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale

多模态生成流同时包含持续到达、异质阶段和实时 deadline；把每个请求当成单次模型调用会隐藏跨阶段排队。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。 其公开验证边界为：作者在其公开模型、设备和请求分布上测量吞吐与尾延迟，足以支持所测实时 pipeline 的联合调度收益；未披露的跨集群网络、租户隔离和生产 SLO 不属于结论。 新增代价与回退条件为：更细的阶段状态提升利用率，也增加队列、取消和中间结果失效复杂度；离线同质批处理仍适合静态流水线。
<!-- analysis:DA-20260309-08:end -->
<!-- analysis:DA-20260309-12:start -->
### A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA

线性注意力 decode 受反复装载持久状态限制，单纯增加算术单元不能消除片外带宽瓶颈。 旧路径在其原约束下仍合理：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。 本 family 的设计变化是：该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。 其公开验证边界为：FPGA 原型证明给定算子、精度和器件上的带宽/吞吐变化；它没有证明不同线性注意力变体或 GPU runtime 可获得相同比例收益。 新增代价与回退条件为：持久化减少内存流量，却占用片上容量并绑定状态布局；短序列或状态无法容纳时，通用外存执行仍更灵活。
<!-- analysis:DA-20260309-12:end -->
<!-- analysis:DA-20260309-19:start -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing

MoE serving 的冷门 expert 长期占据 GPU，会让峰值容量与平均利用率之间产生结构性浪费。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。 其公开验证边界为：公开实验支持其工作负载下的成本/延迟取舍，但 serverless 冷启动、网络拓扑和 expert 热度稳定性限制外推。 新增代价与回退条件为：弹性回收降低闲置成本，却把冷启动与跨节点通信引入 token 路径；高且稳定的 expert 利用率仍适合常驻部署。
<!-- analysis:DA-20260309-19:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05517 | delta:SF-2026-ARXIV-2603-05517 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05517 |
| SF-2026-ARXIV-2603-05520 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05520 | delta:SF-2026-ARXIV-2603-05520 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05520 |
| SF-2026-ARXIV-2603-05553 | TRAIN-DATA | books/part-04-training-system/27-data.md#part-iv-的能力生产链 (section Ch-owner) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent); books/part-04-training-system/28-pretraining.md#第28章-pretraining (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05553 | delta:SF-2026-ARXIV-2603-05553 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05553 |
| SF-2026-ARXIV-2603-05578 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量：评估声明必须绑定完整对象 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05578 | delta:SF-2026-ARXIV-2603-05578 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05578 |
| SF-2026-ARXIV-2603-05637 | AGENT-MCP | books/part-07-agent/83-mcp.md#authorization-之前还需要可验证的-server-admission (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05637 | delta:SF-2026-ARXIV-2603-05637 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05637 |
| SF-2026-ARXIV-2603-05692 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05692 | delta:SF-2026-ARXIV-2603-05692 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05692 |
| SF-2026-ARXIV-2603-05754 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05754 | delta:SF-2026-ARXIV-2603-05754 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05754 |
| SF-2026-ARXIV-2603-05800 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05800 | delta:SF-2026-ARXIV-2603-05800 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-05800 |
| SF-2026-ARXIV-2603-05881 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#continual-update-需要同步推进-calibration-state (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05881 | delta:SF-2026-ARXIV-2603-05881 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05881 |
| SF-2026-ARXIV-2603-05910 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05910 | delta:SF-2026-ARXIV-2603-05910 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05910 |
| SF-2026-ARXIV-2603-05912 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#self-report、behavior-probe-与-deployment-outcome-是三种证据 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05912 | delta:SF-2026-ARXIV-2603-05912 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05912 |
| SF-2026-ARXIV-2603-05931 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#accelerator-readiness-是-phase-×-shape-×-offload-×-host-control-contract (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05931 | delta:SF-2026-ARXIV-2603-05931 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-05931 |
| SF-2026-ARXIV-2603-06001 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06001 | delta:SF-2026-ARXIV-2603-06001 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06001 |
| SF-2026-ARXIV-2603-06003 | MODEL-MOE | books/part-02-model/21-moe.md#本章要回答的问题 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06003 | delta:SF-2026-ARXIV-2603-06003 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06003 |
| SF-2026-ARXIV-2603-06007 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06007 | delta:SF-2026-ARXIV-2603-06007 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06007 |
| SF-2026-ARXIV-2603-06081 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06081 | delta:SF-2026-ARXIV-2603-06081 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06081 |
| SF-2026-ARXIV-2603-06199 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#binary-lifting-的核心是恢复-typed-state (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06199 | delta:SF-2026-ARXIV-2603-06199 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06199 |
| SF-2026-ARXIV-2603-06331 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06331 | delta:SF-2026-ARXIV-2603-06331 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06331 |
| SF-2026-ARXIV-2603-06350 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06350 | delta:SF-2026-ARXIV-2603-06350 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-06350 |
| SF-2026-ARXIV-2603-06365 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#requirement-也是-versioned-untrusted-supply-chain-input (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06365 | delta:SF-2026-ARXIV-2603-06365 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06365 |
| SF-2026-ARXIV-2603-06394 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#failure-attribution、perception-routing-与-sticky-state-ownership (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06394 | delta:SF-2026-ARXIV-2603-06394 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06394 |
| SF-2026-ARXIV-2603-06403 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06403 | delta:SF-2026-ARXIV-2603-06403 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06403 |

<!-- books-review:SF-2026-ARXIV-2603-05517:start -->
### Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05517:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-05517:end -->

<!-- delta:SF-2026-ARXIV-2603-05517:start -->新证据差异：exact-v1 的 `Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05517:end -->

边界：只支持 arXiv:2603.05517v1 §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks 的机制与 §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) 的公开 workload；§O.1 Limitations and Open Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05517:end -->
<!-- books-review:SF-2026-ARXIV-2603-05520:start -->
### Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05520:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-05520:end -->

<!-- delta:SF-2026-ARXIV-2603-05520:start -->新证据差异：exact-v1 的 `4.3 Design Implications` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05520:end -->

边界：只支持 arXiv:2603.05520v1 §4.3 Design Implications 的机制与 §7.1 Overall Performance on Medical and Financial Benchmarks 的公开 workload；§8 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05520:end -->
<!-- books-review:SF-2026-ARXIV-2603-05553:start -->
### EigenData: A Self-Evolving Multi-Agent Platform for Function-Calling Data Synthesis, Auditing, and Repair — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05553:start -->已读 owner `books/part-04-training-system/27-data.md` 与相邻章节。现有命题：多模态 raw sample、codec token、frame/second 和 action trajectory 不能用一个未经定义的“token 数”混合计量。第23～26章拥有表示与行动语义；本章拥有这些样本怎样被选择、版本化、配比与送入优化。这个边界使 representation 研究不会寄居于 Data，也使 Data 不退化成文件清单。<!-- existing:SF-2026-ARXIV-2603-05553:end -->

<!-- delta:SF-2026-ARXIV-2603-05553:start -->新证据差异：EigenData 让多个专责 agent 共享可验证 artifact graph，并以数据库终态而非轨迹表面匹配作为任务 oracle。<!-- delta:SF-2026-ARXIV-2603-05553:end -->

边界：只支持 arXiv:2603.05553v1 §3.3.1 Architecture 的机制与 §4.3 Evaluation Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05553:end -->
<!-- books-review:SF-2026-ARXIV-2603-05578:start -->
### Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05578:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或 architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision 纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一 对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。<!-- existing:SF-2026-ARXIV-2603-05578:end -->

<!-- delta:SF-2026-ARXIV-2603-05578:start -->新证据差异：Tool-Genesis 从抽象需求开始，分别验证 interface compliance、functional correctness 与 downstream utility，使失败位置可归因。<!-- delta:SF-2026-ARXIV-2603-05578:end -->

边界：只支持 arXiv:2603.05578v1 §Appendix A Evaluation Methodology Details 的机制与 §5.2 Experimental Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05578:end -->
<!-- books-review:SF-2026-ARXIV-2603-05637:start -->
### Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05637:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。<!-- existing:SF-2026-ARXIV-2603-05637:end -->

<!-- delta:SF-2026-ARXIV-2603-05637:start -->新证据差异：exact-v1 的 `3. Methodology` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05637:end -->

边界：只支持 arXiv:2603.05637v1 §3. Methodology 的机制与 §3.3. Taxonomy Creation and Validation 的公开 workload；§7. Conclusion and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05637:end -->
<!-- books-review:SF-2026-ARXIV-2603-05692:start -->
### Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05692:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-05692:end -->

<!-- delta:SF-2026-ARXIV-2603-05692:start -->新证据差异：exact-v1 的 `2.2. Overview of Llama 3.1-70B/-405B Models` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05692:end -->

边界：只支持 arXiv:2603.05692v1 §2.2. Overview of Llama 3.1-70B/-405B Models 的机制与 §3. In-House Simulator and Its Validation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05692:end -->
<!-- books-review:SF-2026-ARXIV-2603-05754:start -->
### Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05754:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-05754:end -->

<!-- delta:SF-2026-ARXIV-2603-05754:start -->新证据差异：exact-v1 的 `III-A System Architecture and Adaptation Strategy` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05754:end -->

边界：只支持 arXiv:2603.05754v1 §III-A System Architecture and Adaptation Strategy 的机制与 §V-C Exploratory Mechanism Analysis: Attention Ablation 的公开 workload；§V-B1 Limitations of RGB-Only and RGB-D Variants 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05754:end -->
<!-- books-review:SF-2026-ARXIV-2603-05800:start -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05800:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。 生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入 真实 serving 的补全责任，而不是论文已经证明的反馈算法。<!-- existing:SF-2026-ARXIV-2603-05800:end -->

<!-- delta:SF-2026-ARXIV-2603-05800:start -->新证据差异：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。<!-- delta:SF-2026-ARXIV-2603-05800:end -->

边界：只支持 arXiv:2603.05800v1 §4.7. Implementation 的机制与 §5. Evaluation 的公开 workload；§7. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-05800:end -->
<!-- books-review:SF-2026-ARXIV-2603-05881:start -->
### Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05881:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。<!-- existing:SF-2026-ARXIV-2603-05881:end -->

<!-- delta:SF-2026-ARXIV-2603-05881:start -->新证据差异：exact-v1 的 `3.2 Confidence-First Paradigm Definition` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05881:end -->

边界：只支持 arXiv:2603.05881v1 §3.2 Confidence-First Paradigm Definition 的机制与 §4.1.2 Evaluation Benchmarks 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05881:end -->
<!-- books-review:SF-2026-ARXIV-2603-05910:start -->
### The World Won't Stay Still: Programmable Evolution for Agent Benchmarks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05910:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-05910:end -->

<!-- delta:SF-2026-ARXIV-2603-05910:start -->新证据差异：exact-v1 的 `C.2 Tool Designer in Saturation Strategy` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05910:end -->

边界：只支持 arXiv:2603.05910v1 §C.2 Tool Designer in Saturation Strategy 的机制与 §4.4 State-Wise User Simulation and Evaluation 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05910:end -->
<!-- books-review:SF-2026-ARXIV-2603-05912:start -->
### DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05912:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失： 写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge 与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。<!-- existing:SF-2026-ARXIV-2603-05912:end -->

<!-- delta:SF-2026-ARXIV-2603-05912:start -->新证据差异：exact-v1 的 `4.1 Methodology: The Micro-Gold Protocol` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05912:end -->

边界：只支持 arXiv:2603.05912v1 §4.1 Methodology: The Micro-Gold Protocol 的机制与 §7.3 Results on Other Factuality Benchmarks 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-05912:end -->
<!-- books-review:SF-2026-ARXIV-2603-05931:start -->
### A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05931:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：把整张模型图放到标称 TOPS 更高的 accelerator 上，在 graph 规则、offload coverage 完整、host control 便宜且 Prefill/Decode shape 相近时最简单。LLM 改变了这个前提：Prefill 的大矩阵与 Decode 的小 batch、逐 token 控制可能偏好不同 backend；unsupported operators、tensor/KV conversion、wake/sleep、polling 和 host-device synchronization 又可能吞掉计算收益。<!-- existing:SF-2026-ARXIV-2603-05931:end -->

<!-- delta:SF-2026-ARXIV-2603-05931:start -->新证据差异：该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。<!-- delta:SF-2026-ARXIV-2603-05931:end -->

边界：只支持 arXiv:2603.05931v1 §IV-E System Overview 的机制与 §VI-E Ablation Analysis 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-05931:end -->
<!-- books-review:SF-2026-ARXIV-2603-06001:start -->
### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06001:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-06001:end -->

<!-- delta:SF-2026-ARXIV-2603-06001:start -->新证据差异：ICBench 固定视觉场景并注入矛盾指令；IGAR 在推理时重分配 attention，使语言约束重新进入动作生成。<!-- delta:SF-2026-ARXIV-2603-06001:end -->

边界：只支持 arXiv:2603.06001v1 §3.2 Contradiction Taxonomy and Design Principles 的机制与 §5.6 Real-World Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06001:end -->
<!-- books-review:SF-2026-ARXIV-2603-06003:start -->
### EvoESAP: Non-Uniform Expert Pruning for Sparse MoE — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06003:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。<!-- existing:SF-2026-ARXIV-2603-06003:end -->

<!-- delta:SF-2026-ARXIV-2603-06003:start -->新证据差异：EvoESAP 把层内 expert 排序与跨层预算分开，用 teacher-forced acceptance proxy 搜索非均匀 sparsity。<!-- delta:SF-2026-ARXIV-2603-06003:end -->

边界：只支持 arXiv:2603.06003v1 §2.3 Other Compression Methods 的机制与 §4.2 Main results 的公开 workload；§Appendix C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06003:end -->
<!-- books-review:SF-2026-ARXIV-2603-06007:start -->
### MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06007:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-06007:end -->

<!-- delta:SF-2026-ARXIV-2603-06007:start -->新证据差异：exact-v1 的 `3 System Design` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06007:end -->

边界：只支持 arXiv:2603.06007v1 §3 System Design 的机制与 §4 Evaluation and Analysis 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06007:end -->
<!-- books-review:SF-2026-ARXIV-2603-06081:start -->
### Lyapunov Probes for Hallucination Detection in Large Foundation Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06081:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-06081:end -->

<!-- delta:SF-2026-ARXIV-2603-06081:start -->新证据差异：Lyapunov probe 以扰动下置信单调衰减为训练约束，把局部稳定性作为 hallucination 风险信号。<!-- delta:SF-2026-ARXIV-2603-06081:end -->

边界：只支持 arXiv:2603.06081v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06081:end -->
<!-- books-review:SF-2026-ARXIV-2603-06199:start -->
### FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06199:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：GPU binary 到可分析 IR 的迁移不是指令文本替换：统一 register file 必须恢复 typed state，分支要重建显式 control flow，多指令 pattern 还要恢复组合语义。类型或控制流冲突时，生成貌似可执行的 IR 会把未知语义静默固化，因此 lifter 必须 fail closed 并保留 unsupported instruction surface。Typed LLVM IR 可成为审计和迁移的中间证据，但受支持架构、MUFU/texture 与完整 SIMT 语义限制；原生二进制验证仍不可删除。<!-- existing:SF-2026-ARXIV-2603-06199:end -->

<!-- delta:SF-2026-ARXIV-2603-06199:start -->新证据差异：FlashPrefill 联合发现 vertical、slash 与 block pattern，并用动态阈值直接裁剪长尾 block，改变 prefill execution plan。<!-- delta:SF-2026-ARXIV-2603-06199:end -->

边界：只支持 arXiv:2603.06199v1 §3.3 Comparison with Previous Methods. 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06199:end -->
<!-- books-review:SF-2026-ARXIV-2603-06331:start -->
### WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06331:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-06331:end -->

<!-- delta:SF-2026-ARXIV-2603-06331:start -->新证据差异：exact-v1 的 `4.1 Curvature-guided Heterogeneous Token Prediction` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06331:end -->

边界：只支持 arXiv:2603.06331v1 §4.1 Curvature-guided Heterogeneous Token Prediction 的机制与 §5.2 World Generation Results 的公开 workload；§Failure of Uniform Strategies. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06331:end -->
<!-- books-review:SF-2026-ARXIV-2603-06350:start -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06350:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-06350:end -->

<!-- delta:SF-2026-ARXIV-2603-06350:start -->新证据差异：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。<!-- delta:SF-2026-ARXIV-2603-06350:end -->

边界：只支持 arXiv:2603.06350v1 §3.2. Architecture and Workflow 的机制与 §6. Evaluation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-06350:end -->
<!-- books-review:SF-2026-ARXIV-2603-06365:start -->
### ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06365:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：控制权不能随 prompt 一并交给 coding model。模型只拥有 code proposal；security policy owner 定义不变量与 exception 规则，CI 以确定性功能测试、安全回归测试和 static analysis 执行检查并生成 receipt，repository owner 审阅 requirement revision、proposal、双重验证结果与 exception 后，才拥有 merge 或 revert authority。若 proposal 同时改写 policy、安全测试或 approved template，这些变化必须进入独立审批，而不能用“测试已通过”自证。这样可以阻止显式 usability objective 静默覆盖安全约束，并把每次合并追溯到授权它的 requirement revision；代价是规范与测试维护、额外 CI 延迟、false reject，以及 requirement、policy 与 tests 之间的漂移。<!-- existing:SF-2026-ARXIV-2603-06365:end -->

<!-- delta:SF-2026-ARXIV-2603-06365:start -->新证据差异：ESAA-Security 让 agent 只提交结构化 intent，由 orchestrator 验证后写 append-only event log，再重放投影与 hash 校验。<!-- delta:SF-2026-ARXIV-2603-06365:end -->

边界：只支持 arXiv:2603.06365v1 §3 ESAA-Security Architecture 的机制与 §6 Evaluation Design and Research Questions 的公开 workload；§8 Discussion, Limitations, and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06365:end -->
<!-- books-review:SF-2026-ARXIV-2603-06394:start -->
### Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06394:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。<!-- existing:SF-2026-ARXIV-2603-06394:end -->

<!-- delta:SF-2026-ARXIV-2603-06394:start -->新证据差异：exact-v1 的 `5.1 Architecture overview` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06394:end -->

边界：只支持 arXiv:2603.06394v1 §5.1 Architecture overview 的机制与 §5.3 Validation framework 的公开 workload；§6.5 Future work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06394:end -->
<!-- books-review:SF-2026-ARXIV-2603-06403:start -->
### Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06403:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-06403:end -->

<!-- delta:SF-2026-ARXIV-2603-06403:start -->新证据差异：exact-v1 的 `3.1 Reward and Cost Predictor Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06403:end -->

边界：只支持 arXiv:2603.06403v1 §3.1 Reward and Cost Predictor Design 的机制与 §5.3 Experimental Results and Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06403:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260309-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260309 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260309-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-05517; review:SF-2026-ARXIV-2603-05520; review:SF-2026-ARXIV-2603-05553; review:SF-2026-ARXIV-2603-05578; review:SF-2026-ARXIV-2603-05637; review:SF-2026-ARXIV-2603-05692; review:SF-2026-ARXIV-2603-05754; review:SF-2026-ARXIV-2603-05800; review:SF-2026-ARXIV-2603-05881; review:SF-2026-ARXIV-2603-05910; review:SF-2026-ARXIV-2603-05912; review:SF-2026-ARXIV-2603-05931; review:SF-2026-ARXIV-2603-06001; review:SF-2026-ARXIV-2603-06003; review:SF-2026-ARXIV-2603-06007; review:SF-2026-ARXIV-2603-06081; review:SF-2026-ARXIV-2603-06199; review:SF-2026-ARXIV-2603-06331; review:SF-2026-ARXIV-2603-06350; review:SF-2026-ARXIV-2603-06365; review:SF-2026-ARXIV-2603-06394; review:SF-2026-ARXIV-2603-06403 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260309-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260309-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260309/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
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
