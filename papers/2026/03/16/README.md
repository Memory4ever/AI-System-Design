# Daily Research — 2026-03-16

**Research Date:** 2026-03-16

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-15 09:00:00 ～ 2026-03-16 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=465/465/465；denominator=30、pre-denominator closures=435。exact-v1 Review complete=30、blocked=0；Integrate 建议=3。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-16 |
| Window End | 2026-03-16 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260316-AUTHOR-30 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-15T09:00:00+08:00 | 2026-03-16T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 465/465 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 465 | SF-2026-ARXIV-2603-12277;SF-2026-ARXIV-2603-12396;SF-2026-ARXIV-2603-12440;SF-2026-ARXIV-2603-12465;SF-2026-ARXIV-2603-12485;SF-2026-ARXIV-2603-12510;SF-2026-ARXIV-2603-12553;SF-2026-ARXIV-2603-12598;SF-2026-ARXIV-2603-12614;SF-2026-ARXIV-2603-12617;SF-2026-ARXIV-2603-12621;SF-2026-ARXIV-2603-12631;SF-2026-ARXIV-2603-12639;SF-2026-ARXIV-2603-12646;SF-2026-ARXIV-2603-12655;SF-2026-ARXIV-2603-12671;SF-2026-ARXIV-2603-12707;SF-2026-ARXIV-2603-12823;SF-2026-ARXIV-2603-12831;SF-2026-ARXIV-2603-12933;SF-2026-ARXIV-2603-12946;SF-2026-ARXIV-2603-13017;SF-2026-ARXIV-2603-13019;SF-2026-ARXIV-2603-13026;SF-2026-ARXIV-2603-13033;SF-2026-ARXIV-2603-13099;SF-2026-ARXIV-2603-13110;SF-2026-ARXIV-2603-13176;SF-2026-ARXIV-2603-13189;SF-2026-ARXIV-2603-13215 | pages=100; prefixes=00..99; final_cursor=end; registered=465; screened=465; retained=30; closure=435 | 2026-03-16T01:00:00+00:00 | screening-ledger-final.json#sha256=823c484a6030ed913fb54d0f85dc448df7abf1f911a16ac2f3c6fc063e6d9747; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260316:start -->作者侧已逐项筛选全部 465 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260316:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-12277 | arXiv:2603.12277v1 | paper-v1:2603.12277 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12277 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12277 | no |
| SF-2026-ARXIV-2603-12396 | arXiv:2603.12396v1 | paper-v1:2603.12396 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12396 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12396 | no |
| SF-2026-ARXIV-2603-12440 | arXiv:2603.12440v1 | paper-v1:2603.12440 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12440 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12440 | no |
| SF-2026-ARXIV-2603-12465 | arXiv:2603.12465v1 | paper-v1:2603.12465 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-12465 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-12465 | no |
| SF-2026-ARXIV-2603-12485 | arXiv:2603.12485v1 | paper-v1:2603.12485 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12485 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12485 | no |
| SF-2026-ARXIV-2603-12510 | arXiv:2603.12510v1 | paper-v1:2603.12510 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12510 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12510 | no |
| SF-2026-ARXIV-2603-12553 | arXiv:2603.12553v1 | paper-v1:2603.12553 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12553 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12553 | no |
| SF-2026-ARXIV-2603-12598 | arXiv:2603.12598v1 | paper-v1:2603.12598 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12598 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12598 | no |
| SF-2026-ARXIV-2603-12614 | arXiv:2603.12614v1 | paper-v1:2603.12614 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12614 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12614 | no |
| SF-2026-ARXIV-2603-12617 | arXiv:2603.12617v1 | paper-v1:2603.12617 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12617 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12617 | no |
| SF-2026-ARXIV-2603-12621 | arXiv:2603.12621v1 | paper-v1:2603.12621 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12621 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12621 | no |
| SF-2026-ARXIV-2603-12631 | arXiv:2603.12631v1 | paper-v1:2603.12631 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12631 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12631 | no |
| SF-2026-ARXIV-2603-12639 | arXiv:2603.12639v1 | paper-v1:2603.12639 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12639 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12639 | no |
| SF-2026-ARXIV-2603-12646 | arXiv:2603.12646v1 | paper-v1:2603.12646 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12646 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12646 | no |
| SF-2026-ARXIV-2603-12655 | arXiv:2603.12655v1 | paper-v1:2603.12655 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12655 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12655 | no |
| SF-2026-ARXIV-2603-12671 | arXiv:2603.12671v1 | paper-v1:2603.12671 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12671 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12671 | no |
| SF-2026-ARXIV-2603-12707 | arXiv:2603.12707v1 | paper-v1:2603.12707 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12707 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12707 | no |
| SF-2026-ARXIV-2603-12823 | arXiv:2603.12823v1 | paper-v1:2603.12823 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12823 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12823 | no |
| SF-2026-ARXIV-2603-12831 | arXiv:2603.12831v1 | paper-v1:2603.12831 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-12831 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-12831 | no |
| SF-2026-ARXIV-2603-12933 | arXiv:2603.12933v1 | paper-v1:2603.12933 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12933 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12933 | no |
| SF-2026-ARXIV-2603-12946 | arXiv:2603.12946v1 | paper-v1:2603.12946 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-12946 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12946 | no |
| SF-2026-ARXIV-2603-13017 | arXiv:2603.13017v1 | paper-v1:2603.13017 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13017 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13017 | no |
| SF-2026-ARXIV-2603-13019 | arXiv:2603.13019v1 | paper-v1:2603.13019 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13019 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13019 | no |
| SF-2026-ARXIV-2603-13026 | arXiv:2603.13026v1 | paper-v1:2603.13026 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13026 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13026 | no |
| SF-2026-ARXIV-2603-13033 | arXiv:2603.13033v1 | paper-v1:2603.13033 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13033 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13033 | no |
| SF-2026-ARXIV-2603-13099 | arXiv:2603.13099v1 | paper-v1:2603.13099 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13099 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13099 | no |
| SF-2026-ARXIV-2603-13110 | arXiv:2603.13110v1 | paper-v1:2603.13110 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-13110 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2603-13110 | no |
| SF-2026-ARXIV-2603-13176 | arXiv:2603.13176v1 | paper-v1:2603.13176 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13176 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13176 | no |
| SF-2026-ARXIV-2603-13189 | arXiv:2603.13189v1 | paper-v1:2603.13189 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13189 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13189 | no |
| SF-2026-ARXIV-2603-13215 | arXiv:2603.13215v1 | paper-v1:2603.13215 | 2026-W12 | 2026-03-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-13215 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13215 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-12277 | RP-483e59af87e2cfeb | standard | arXiv:2603.12277v1 | SRC-ARXIV@arXiv:2603.12277v1 | arXiv:2603.12277v1 HTML — §Methodology: Isolating Role Signals. [facet=method]; https://arxiv.org/html/2603.12277v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12277v1.html; sha256:81b49954856ec36a94a8503621379b3567e513f027b3bf534898259774cde374 | arXiv:2603.12277v1 HTML — §Evaluation. [facet=evaluation]; https://arxiv.org/html/2603.12277v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12277v1.html; sha256:81b49954856ec36a94a8503621379b3567e513f027b3bf534898259774cde374 | arXiv:2603.12277v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2603.12277v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12277v1.html; sha256:81b49954856ec36a94a8503621379b3567e513f027b3bf534898259774cde374 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12277v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12277 | complete |
| SF-2026-ARXIV-2603-12396 | RP-2986937a396b1626 | standard | arXiv:2603.12396v1 | SRC-ARXIV@arXiv:2603.12396v1 | arXiv:2603.12396v1 HTML — §3. Approach [facet=method]; https://arxiv.org/html/2603.12396v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12396v1.html; sha256:b03faf78a80c746ae3f180cad2d7250cb08ec09a11be42bdee05b35ba6366272 | arXiv:2603.12396v1 HTML — §4.1.5. Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.12396v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12396v1.html; sha256:b03faf78a80c746ae3f180cad2d7250cb08ec09a11be42bdee05b35ba6366272 | arXiv:2603.12396v1 HTML — §5. Conclusion [facet=limitations]; https://arxiv.org/html/2603.12396v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12396v1.html; sha256:b03faf78a80c746ae3f180cad2d7250cb08ec09a11be42bdee05b35ba6366272 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12396v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12396 | complete |
| SF-2026-ARXIV-2603-12440 | RP-27e5165d6e89bded | standard | arXiv:2603.12440v1 | SRC-ARXIV@arXiv:2603.12440v1 | arXiv:2603.12440v1 HTML — §3.1 System Architecture [facet=method]; https://arxiv.org/html/2603.12440v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12440v1.html; sha256:2cb0d4ac88ab073756f4e43909c9f7484cf978d0a057e7b08472255f3853242d | arXiv:2603.12440v1 HTML — §5.2 Evaluation on SYCL kernel generation [facet=evaluation]; https://arxiv.org/html/2603.12440v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12440v1.html; sha256:2cb0d4ac88ab073756f4e43909c9f7484cf978d0a057e7b08472255f3853242d | arXiv:2603.12440v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12440v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12440v1.html; sha256:2cb0d4ac88ab073756f4e43909c9f7484cf978d0a057e7b08472255f3853242d | arXiv exact-v1 identity https://arxiv.org/abs/2603.12440v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12440 | complete |
| SF-2026-ARXIV-2603-12465 | RP-9b1595b1584aca14 | deep | arXiv:2603.12465v1 | SRC-ARXIV@arXiv:2603.12465v1 | arXiv:2603.12465v1 HTML — §III TaxBreak Methodology [facet=method]; https://arxiv.org/html/2603.12465v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12465v1.html; sha256:1d38142cac361bf377409ca78d8fe358d23b66f22e1e659aa213d86af609f23f | arXiv:2603.12465v1 HTML — §V Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12465v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12465v1.html; sha256:1d38142cac361bf377409ca78d8fe358d23b66f22e1e659aa213d86af609f23f | arXiv:2603.12465v1 HTML — §VII Conclusion and Outlook [facet=limitations]; https://arxiv.org/html/2603.12465v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12465v1.html; sha256:1d38142cac361bf377409ca78d8fe358d23b66f22e1e659aa213d86af609f23f | arXiv exact-v1 identity https://arxiv.org/abs/2603.12465v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12465 | complete |
| SF-2026-ARXIV-2603-12485 | RP-50676cc3e6b1588a | standard | arXiv:2603.12485v1 | SRC-ARXIV@arXiv:2603.12485v1 | arXiv:2603.12485v1 HTML — §2.1. GPU Architecture [facet=method]; https://arxiv.org/html/2603.12485v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12485v1.html; sha256:428f2705da3cd2d24bc0ca181c0a59ce0cf8978eed4e5390ee048f12835d084c | arXiv:2603.12485v1 HTML — §7. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12485v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12485v1.html; sha256:428f2705da3cd2d24bc0ca181c0a59ce0cf8978eed4e5390ee048f12835d084c | arXiv:2603.12485v1 HTML — §8.3. Thread-Interleaving Coverage Limitations [facet=limitations]; https://arxiv.org/html/2603.12485v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12485v1.html; sha256:428f2705da3cd2d24bc0ca181c0a59ce0cf8978eed4e5390ee048f12835d084c | arXiv exact-v1 identity https://arxiv.org/abs/2603.12485v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12485 | complete |
| SF-2026-ARXIV-2603-12510 | RP-98f7af60f8499ff9 | standard | arXiv:2603.12510v1 | SRC-ARXIV@arXiv:2603.12510v1 | arXiv:2603.12510v1 HTML — §IV Method: Q-DIG [facet=method]; https://arxiv.org/html/2603.12510v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12510v1.html; sha256:067bde76b19e70fc48bb1db4630a76e649d67088fabdd8109cf4c4c156f9181f | arXiv:2603.12510v1 HTML — §VI-C Results: Real-World Experiments [facet=evaluation]; https://arxiv.org/html/2603.12510v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12510v1.html; sha256:067bde76b19e70fc48bb1db4630a76e649d67088fabdd8109cf4c4c156f9181f | arXiv:2603.12510v1 HTML — §VII Conclusion and Limitations [facet=limitations]; https://arxiv.org/html/2603.12510v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12510v1.html; sha256:067bde76b19e70fc48bb1db4630a76e649d67088fabdd8109cf4c4c156f9181f | arXiv exact-v1 identity https://arxiv.org/abs/2603.12510v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12510 | complete |
| SF-2026-ARXIV-2603-12553 | RP-7aa3e942428bf13b | standard | arXiv:2603.12553v1 | SRC-ARXIV@arXiv:2603.12553v1 | arXiv:2603.12553v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.12553v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12553v1.html; sha256:dee4a75237add006f93ec4275369f79ae24ec27b2342c43e33a377cd7f3a81de | arXiv:2603.12553v1 HTML — §4.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.12553v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12553v1.html; sha256:dee4a75237add006f93ec4275369f79ae24ec27b2342c43e33a377cd7f3a81de | arXiv:2603.12553v1 HTML — §Limitations and Discussion. [facet=limitations]; https://arxiv.org/html/2603.12553v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12553v1.html; sha256:dee4a75237add006f93ec4275369f79ae24ec27b2342c43e33a377cd7f3a81de | arXiv exact-v1 identity https://arxiv.org/abs/2603.12553v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12553 | complete |
| SF-2026-ARXIV-2603-12598 | RP-b2b38a8f4daa26e4 | standard | arXiv:2603.12598v1 | SRC-ARXIV@arXiv:2603.12598v1 | arXiv:2603.12598v1 HTML — §8.1 Settings of Methods [facet=method]; https://arxiv.org/html/2603.12598v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12598v1.html; sha256:c3c5d382dad8da9a803e9cbd2a738d9a11fa135e15f5afa1da79c0a7e15dc65f | arXiv:2603.12598v1 HTML — §8.3 Details of Evaluation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.12598v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12598v1.html; sha256:c3c5d382dad8da9a803e9cbd2a738d9a11fa135e15f5afa1da79c0a7e15dc65f | arXiv:2603.12598v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12598v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12598v1.html; sha256:c3c5d382dad8da9a803e9cbd2a738d9a11fa135e15f5afa1da79c0a7e15dc65f | arXiv exact-v1 identity https://arxiv.org/abs/2603.12598v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12598 | complete |
| SF-2026-ARXIV-2603-12614 | RP-b78c0bf707d4073c | standard | arXiv:2603.12614v1 | SRC-ARXIV@arXiv:2603.12614v1 | arXiv:2603.12614v1 HTML — §3.2. ChainFuzzer Workflow [facet=method]; https://arxiv.org/html/2603.12614v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12614v1.html; sha256:91545519f157debb0c3f69753bf5c4db6777fcca3bb9d444330552781349419f | arXiv:2603.12614v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12614v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12614v1.html; sha256:91545519f157debb0c3f69753bf5c4db6777fcca3bb9d444330552781349419f | arXiv:2603.12614v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.12614v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12614v1.html; sha256:91545519f157debb0c3f69753bf5c4db6777fcca3bb9d444330552781349419f | arXiv exact-v1 identity https://arxiv.org/abs/2603.12614v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12614 | complete |
| SF-2026-ARXIV-2603-12617 | RP-b833fd5fa5259df8 | standard | arXiv:2603.12617v1 | SRC-ARXIV@arXiv:2603.12617v1 | arXiv:2603.12617v1 HTML — §4.2 Evaluation of Our Approach [facet=method]; https://arxiv.org/html/2603.12617v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12617v1.html; sha256:842788faef144175a9803b62a0ffa8b6949ce1c9537e266927d78218a13297c2 | arXiv:2603.12617v1 HTML — §Appendix B Additional Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.12617v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12617v1.html; sha256:842788faef144175a9803b62a0ffa8b6949ce1c9537e266927d78218a13297c2 | arXiv:2603.12617v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12617v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12617v1.html; sha256:842788faef144175a9803b62a0ffa8b6949ce1c9537e266927d78218a13297c2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12617v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12617 | complete |
| SF-2026-ARXIV-2603-12621 | RP-98b2c8cec7aa40d3 | standard | arXiv:2603.12621v1 | SRC-ARXIV@arXiv:2603.12621v1 | arXiv:2603.12621v1 HTML — §2. System Overview and Threat Model [facet=method]; https://arxiv.org/html/2603.12621v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12621v1.html; sha256:313a60c293e0dc61b408f483fd91d01bb32021edb9484c67c0fd6f5af563a5cf | arXiv:2603.12621v1 HTML — §3. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12621v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12621v1.html; sha256:313a60c293e0dc61b408f483fd91d01bb32021edb9484c67c0fd6f5af563a5cf | arXiv:2603.12621v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.12621v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12621v1.html; sha256:313a60c293e0dc61b408f483fd91d01bb32021edb9484c67c0fd6f5af563a5cf | arXiv exact-v1 identity https://arxiv.org/abs/2603.12621v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12621 | complete |
| SF-2026-ARXIV-2603-12631 | RP-2beb505b44971af8 | standard | arXiv:2603.12631v1 | SRC-ARXIV@arXiv:2603.12631v1 | arXiv:2603.12631v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.12631v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12631v1.html; sha256:0ac15284b3eeb172990e5fbc328248c0a94cbd6e32378672536f4df16f9b9af2 | arXiv:2603.12631v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.12631v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12631v1.html; sha256:0ac15284b3eeb172990e5fbc328248c0a94cbd6e32378672536f4df16f9b9af2 | arXiv:2603.12631v1 HTML — §Appendix E Limitation [facet=limitations]; https://arxiv.org/html/2603.12631v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12631v1.html; sha256:0ac15284b3eeb172990e5fbc328248c0a94cbd6e32378672536f4df16f9b9af2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12631v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12631 | complete |
| SF-2026-ARXIV-2603-12639 | RP-0de55d06b5ce5c4b | standard | arXiv:2603.12639v1 | SRC-ARXIV@arXiv:2603.12639v1 | arXiv:2603.12639v1 HTML — §3.1 Architecture Design [facet=method]; https://arxiv.org/html/2603.12639v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12639v1.html; sha256:c8dd88873aa9ea37405a9f4bc518edc5cf25adb5d255830635e5569a97e59a4d | arXiv:2603.12639v1 HTML — §4.2 Video Quality Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12639v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12639v1.html; sha256:c8dd88873aa9ea37405a9f4bc518edc5cf25adb5d255830635e5569a97e59a4d | arXiv:2603.12639v1 HTML — §4.4 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.12639v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12639v1.html; sha256:c8dd88873aa9ea37405a9f4bc518edc5cf25adb5d255830635e5569a97e59a4d | arXiv exact-v1 identity https://arxiv.org/abs/2603.12639v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12639 | complete |
| SF-2026-ARXIV-2603-12646 | RP-1e174d5d1b6c983c | standard | arXiv:2603.12646v1 | SRC-ARXIV@arXiv:2603.12646v1 | arXiv:2603.12646v1 HTML — §IV System Design [facet=method]; https://arxiv.org/html/2603.12646v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12646v1.html; sha256:c0006e50345bebc407d79f6e0fdf7cc430678cf394b0def28c6e40829ef1874c | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12646v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12646v1.html; sha256:c0006e50345bebc407d79f6e0fdf7cc430678cf394b0def28c6e40829ef1874c | arXiv:2603.12646v1 HTML — §VI Discussion [facet=limitations]; https://arxiv.org/html/2603.12646v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12646v1.html; sha256:c0006e50345bebc407d79f6e0fdf7cc430678cf394b0def28c6e40829ef1874c | arXiv exact-v1 identity https://arxiv.org/abs/2603.12646v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12646 | complete |
| SF-2026-ARXIV-2603-12655 | RP-a5426cea1abb7784 | standard | arXiv:2603.12655v1 | SRC-ARXIV@arXiv:2603.12655v1 | arXiv:2603.12655v1 HTML — §0.B.1 Model Architecture [facet=method]; https://arxiv.org/html/2603.12655v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12655v1.html; sha256:db942c8f20b970c741b6543bd743557c7b560669f728ca6506a763feb24f0b54 | arXiv:2603.12655v1 HTML — §0.B.2 Evaluation Datasets [facet=evaluation]; https://arxiv.org/html/2603.12655v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12655v1.html; sha256:db942c8f20b970c741b6543bd743557c7b560669f728ca6506a763feb24f0b54 | arXiv:2603.12655v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.12655v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12655v1.html; sha256:db942c8f20b970c741b6543bd743557c7b560669f728ca6506a763feb24f0b54 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12655v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12655 | complete |
| SF-2026-ARXIV-2603-12671 | RP-39134e2d2961f3a4 | standard | arXiv:2603.12671v1 | SRC-ARXIV@arXiv:2603.12671v1 | arXiv:2603.12671v1 HTML — §V Architecture of Execution Layer [facet=method]; https://arxiv.org/html/2603.12671v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12671v1.html; sha256:a625e5c3f9654ce9fefcf0bbc066dac1608a85108deea3e889d391095ac57810 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12671v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12671v1.html; sha256:a625e5c3f9654ce9fefcf0bbc066dac1608a85108deea3e889d391095ac57810 | arXiv:2603.12671v1 HTML — §VIII Conclusion [facet=limitations]; https://arxiv.org/html/2603.12671v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12671v1.html; sha256:a625e5c3f9654ce9fefcf0bbc066dac1608a85108deea3e889d391095ac57810 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12671v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12671 | complete |
| SF-2026-ARXIV-2603-12707 | RP-088200951efec3f5 | standard | arXiv:2603.12707v1 | SRC-ARXIV@arXiv:2603.12707v1 | arXiv:2603.12707v1 HTML — §5 HeteroServe: System Design [facet=method]; https://arxiv.org/html/2603.12707v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12707v1.html; sha256:a70e9761c4053129a3e0181ed315aeee257552d82fce9cf8e2848237b5a74314 | arXiv:2603.12707v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.12707v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12707v1.html; sha256:a70e9761c4053129a3e0181ed315aeee257552d82fce9cf8e2848237b5a74314 | arXiv:2603.12707v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.12707v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12707v1.html; sha256:a70e9761c4053129a3e0181ed315aeee257552d82fce9cf8e2848237b5a74314 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12707v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12707 | complete |
| SF-2026-ARXIV-2603-12823 | RP-e2e76357847cb245 | standard | arXiv:2603.12823v1 | SRC-ARXIV@arXiv:2603.12823v1 | arXiv:2603.12823v1 HTML — §Appendix E Cost Projection Methodology [facet=method]; https://arxiv.org/html/2603.12823v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12823v1.html; sha256:ba18a88724211e9c8e65e9c8c8b638168932b6fd3f0ff0def17a559953e3b31d | arXiv:2603.12823v1 HTML — §4 Evidence and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12823v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12823v1.html; sha256:ba18a88724211e9c8e65e9c8c8b638168932b6fd3f0ff0def17a559953e3b31d | arXiv:2603.12823v1 HTML — §8 Limitations [facet=limitations]; https://arxiv.org/html/2603.12823v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12823v1.html; sha256:ba18a88724211e9c8e65e9c8c8b638168932b6fd3f0ff0def17a559953e3b31d | arXiv exact-v1 identity https://arxiv.org/abs/2603.12823v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12823 | complete |
| SF-2026-ARXIV-2603-12831 | RP-bb16c6832447357d | deep | arXiv:2603.12831v1 | SRC-ARXIV@arXiv:2603.12831v1 | arXiv:2603.12831v1 HTML — §3.3.2–§3.3.6 online scheduling/admission + §4 queues and residual correctness [facet=method]; https://arxiv.org/html/2603.12831v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12831v1.html; sha256:6e6c5a51865db900ad879911566dcb68494718cefff8d770a0a148633746728c | arXiv:2603.12831v1 HTML — §5 Experimental Evaluation on the disclosed A100/CPU testbed [facet=evaluation]; https://arxiv.org/html/2603.12831v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12831v1.html; sha256:6e6c5a51865db900ad879911566dcb68494718cefff8d770a0a148633746728c | arXiv:2603.12831v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.12831v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12831v1.html; sha256:6e6c5a51865db900ad879911566dcb68494718cefff8d770a0a148633746728c | arXiv exact-v1 identity https://arxiv.org/abs/2603.12831v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12831 | complete |
| SF-2026-ARXIV-2603-12933 | RP-69e440f160a394b4 | standard | arXiv:2603.12933v1 | SRC-ARXIV@arXiv:2603.12933v1 | arXiv:2603.12933v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.12933v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12933v1.html; sha256:2d525b951a71a2d5ab3cf7002aa9d79013f93cb3b0ea7af5bab17aef7c63c886 | arXiv:2603.12933v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.12933v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12933v1.html; sha256:2d525b951a71a2d5ab3cf7002aa9d79013f93cb3b0ea7af5bab17aef7c63c886 | arXiv:2603.12933v1 HTML — §V Conclusion [facet=limitations]; https://arxiv.org/html/2603.12933v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12933v1.html; sha256:2d525b951a71a2d5ab3cf7002aa9d79013f93cb3b0ea7af5bab17aef7c63c886 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12933v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12933 | complete |
| SF-2026-ARXIV-2603-12946 | RP-6868cb578087cb01 | standard | arXiv:2603.12946v1 | SRC-ARXIV@arXiv:2603.12946v1 | arXiv:2603.12946v1 HTML — §III-A Overview of PrivQJ [facet=method]; https://arxiv.org/html/2603.12946v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12946v1.html; sha256:525895ee2c45e090d98591f34d8ecacbcd1149adf9b3451e846840cd0db4e133 | arXiv:2603.12946v1 HTML — §IV Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12946v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12946v1.html; sha256:525895ee2c45e090d98591f34d8ecacbcd1149adf9b3451e846840cd0db4e133 | arXiv:2603.12946v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.12946v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12946v1.html; sha256:525895ee2c45e090d98591f34d8ecacbcd1149adf9b3451e846840cd0db4e133 | arXiv exact-v1 identity https://arxiv.org/abs/2603.12946v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-12946 | complete |
| SF-2026-ARXIV-2603-13017 | RP-f8efa5c1875df7da | standard | arXiv:2603.13017v1 | SRC-ARXIV@arXiv:2603.13017v1 | arXiv:2603.13017v1 HTML — §4.3 Grading Methodology [facet=method]; https://arxiv.org/html/2603.13017v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13017v1.html; sha256:59fc8064461c0c93b04424dd1619261aa674667b679cf941998709fc2eeb4406 | arXiv:2603.13017v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13017v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13017v1.html; sha256:59fc8064461c0c93b04424dd1619261aa674667b679cf941998709fc2eeb4406 | arXiv:2603.13017v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.13017v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13017v1.html; sha256:59fc8064461c0c93b04424dd1619261aa674667b679cf941998709fc2eeb4406 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13017v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13017 | complete |
| SF-2026-ARXIV-2603-13019 | RP-de3da957b7de6dda | standard | arXiv:2603.13019v1 | SRC-ARXIV@arXiv:2603.13019v1 | arXiv:2603.13019v1 HTML — §3 Architecture [facet=method]; https://arxiv.org/html/2603.13019v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13019v1.html; sha256:233a406636b677d75e363e8b548a85d3980b2735494f385ac5a43c51e91c8423 | arXiv:2603.13019v1 HTML — §6 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13019v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13019v1.html; sha256:233a406636b677d75e363e8b548a85d3980b2735494f385ac5a43c51e91c8423 | arXiv:2603.13019v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.13019v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13019v1.html; sha256:233a406636b677d75e363e8b548a85d3980b2735494f385ac5a43c51e91c8423 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13019v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13019 | complete |
| SF-2026-ARXIV-2603-13026 | RP-3ea348f94209f501 | standard | arXiv:2603.13026v1 | SRC-ARXIV@arXiv:2603.13026v1 | arXiv:2603.13026v1 HTML — §3.3 Design of PISmith [facet=method]; https://arxiv.org/html/2603.13026v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13026v1.html; sha256:d7fd9c28cec030bfbf8dca7a792a7ccf1edf1deb9904531a0b99ed2da1da876e | arXiv:2603.13026v1 HTML — §Appendix E Full Results for Utility–Robustness Evaluation (RQ2) [facet=evaluation]; https://arxiv.org/html/2603.13026v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13026v1.html; sha256:d7fd9c28cec030bfbf8dca7a792a7ccf1edf1deb9904531a0b99ed2da1da876e | arXiv:2603.13026v1 HTML — §4.5 Ablation Studies [facet=limitations]; https://arxiv.org/html/2603.13026v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13026v1.html; sha256:d7fd9c28cec030bfbf8dca7a792a7ccf1edf1deb9904531a0b99ed2da1da876e | arXiv exact-v1 identity https://arxiv.org/abs/2603.13026v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13026 | complete |
| SF-2026-ARXIV-2603-13033 | RP-6da7007351b5010b | standard | arXiv:2603.13033v1 | SRC-ARXIV@arXiv:2603.13033v1 | arXiv:2603.13033v1 HTML — §Algorithms. [facet=method]; https://arxiv.org/html/2603.13033v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13033v1.html; sha256:11a2e8ad43bbf5df292784b2a5d2d2ae17f47c2bf51f913fdf713a637bb449fe | arXiv:2603.13033v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13033v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13033v1.html; sha256:11a2e8ad43bbf5df292784b2a5d2d2ae17f47c2bf51f913fdf713a637bb449fe | arXiv:2603.13033v1 HTML — §6 Discussion and Future Work [facet=limitations]; https://arxiv.org/html/2603.13033v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13033v1.html; sha256:11a2e8ad43bbf5df292784b2a5d2d2ae17f47c2bf51f913fdf713a637bb449fe | arXiv exact-v1 identity https://arxiv.org/abs/2603.13033v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13033 | complete |
| SF-2026-ARXIV-2603-13099 | RP-3ba39fbe002e0cd2 | standard | arXiv:2603.13099v1 | SRC-ARXIV@arXiv:2603.13099v1 | arXiv:2603.13099v1 HTML — §S6.1 GRPO Framework [facet=method]; https://arxiv.org/html/2603.13099v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13099v1.html; sha256:365d0c76087a379f5bd654811570ab915aa45547278f81dcd5f35e678ea6b0c9 | arXiv:2603.13099v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13099v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13099v1.html; sha256:365d0c76087a379f5bd654811570ab915aa45547278f81dcd5f35e678ea6b0c9 | arXiv:2603.13099v1 HTML — §4.4 Ablation Studies [facet=limitations]; https://arxiv.org/html/2603.13099v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13099v1.html; sha256:365d0c76087a379f5bd654811570ab915aa45547278f81dcd5f35e678ea6b0c9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13099v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13099 | complete |
| SF-2026-ARXIV-2603-13110 | RP-70626329d831e488 | deep | arXiv:2603.13110v1 | SRC-ARXIV@arXiv:2603.13110v1 | arXiv:2603.13110v1 HTML — §IV AgentRM Architecture [facet=method]; https://arxiv.org/html/2603.13110v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13110v1.html; sha256:5b1f3234b2dc15ab6c0b9751f79d7bbad7fb41d36c61eb12cf9dccc2c04eddd5 | arXiv:2603.13110v1 HTML — §VI Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13110v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13110v1.html; sha256:5b1f3234b2dc15ab6c0b9751f79d7bbad7fb41d36c61eb12cf9dccc2c04eddd5 | arXiv:2603.13110v1 HTML — §VII-C Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.13110v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13110v1.html; sha256:5b1f3234b2dc15ab6c0b9751f79d7bbad7fb41d36c61eb12cf9dccc2c04eddd5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13110v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13110 | complete |
| SF-2026-ARXIV-2603-13176 | RP-8fd894c45918a17e | standard | arXiv:2603.13176v1 | SRC-ARXIV@arXiv:2603.13176v1 | arXiv:2603.13176v1 HTML — §III Perception Scheduling Framework [facet=method]; https://arxiv.org/html/2603.13176v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13176v1.html; sha256:1b8da69d8c5879a1218fb630ad90bd48b9deca55397ec3229f98696b9b70aa33 | arXiv:2603.13176v1 HTML — §V-C Perception Module Selector Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13176v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13176v1.html; sha256:1b8da69d8c5879a1218fb630ad90bd48b9deca55397ec3229f98696b9b70aa33 | arXiv:2603.13176v1 HTML — §VII Conclusion [facet=limitations]; https://arxiv.org/html/2603.13176v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13176v1.html; sha256:1b8da69d8c5879a1218fb630ad90bd48b9deca55397ec3229f98696b9b70aa33 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13176v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13176 | complete |
| SF-2026-ARXIV-2603-13189 | RP-731c7549199b2b2b | standard | arXiv:2603.13189v1 | SRC-ARXIV@arXiv:2603.13189v1 | arXiv:2603.13189v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.13189v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13189v1.html; sha256:ce7a4de78a138c700e1e3305aae74520c1323315e400ce7df39bd86b857a58fa | arXiv:2603.13189v1 HTML — §4.1 Multi-Seed Replication and Statistical Validation [facet=evaluation]; https://arxiv.org/html/2603.13189v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13189v1.html; sha256:ce7a4de78a138c700e1e3305aae74520c1323315e400ce7df39bd86b857a58fa | arXiv:2603.13189v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.13189v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13189v1.html; sha256:ce7a4de78a138c700e1e3305aae74520c1323315e400ce7df39bd86b857a58fa | arXiv exact-v1 identity https://arxiv.org/abs/2603.13189v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13189 | complete |
| SF-2026-ARXIV-2603-13215 | RP-538fb0893d85e6c8 | standard | arXiv:2603.13215v1 | SRC-ARXIV@arXiv:2603.13215v1 | arXiv:2603.13215v1 HTML — §3 Benchmarking State Evolution in Video World Models [facet=method]; https://arxiv.org/html/2603.13215v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13215v1.html; sha256:ed90a31ecfdf4ab3e080229d688c50e5301165cc74448528c5bf237c02c7bf52 | arXiv:2603.13215v1 HTML — §3.2 Evaluation Criteria and Automatic Verifiers [facet=evaluation]; https://arxiv.org/html/2603.13215v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13215v1.html; sha256:ed90a31ecfdf4ab3e080229d688c50e5301165cc74448528c5bf237c02c7bf52 | arXiv:2603.13215v1 HTML — §6 Conclusions [facet=limitations]; https://arxiv.org/html/2603.13215v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13215v1.html; sha256:ed90a31ecfdf4ab3e080229d688c50e5301165cc74448528c5bf237c02c7bf52 | arXiv exact-v1 identity https://arxiv.org/abs/2603.13215v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-13215 | complete |

### Source Reviews

### Prompt Injection as Role Confusion

<!-- review:SF-2026-ARXIV-2603-12277:start -->
**问题**：`Prompt Injection as Role Confusion` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `Methodology: Isolating Role Signals.` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12277v1 HTML — §Methodology: Isolating Role Signals. [facet=method]; https://arxiv.org/html/2603.12277v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12277v1.html; sha256:81b49954856ec36a94a8503621379b3567e513f027b3bf534898259774cde374`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation.`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12277v1 HTML — §Evaluation. [facet=evaluation]; https://arxiv.org/html/2603.12277v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12277v1.html; sha256:81b49954856ec36a94a8503621379b3567e513f027b3bf534898259774cde374`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Discussion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12277:start -->**Claim Boundary**：只支持 arXiv:2603.12277v1 §Methodology: Isolating Role Signals. 的机制与 §Evaluation. 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12277:end -->
<!-- review:SF-2026-ARXIV-2603-12277:end -->
### Test-Time Strategies for More Efficient and Accurate Agentic RAG

<!-- review:SF-2026-ARXIV-2603-12396:start -->
**问题**：`Test-Time Strategies for More Efficient and Accurate Agentic RAG` 检查的是 `AGENT-RAG` 中 知识时效、私有数据和可引用证据要求在生成前建立可追踪的检索路径。 是否会改变现有设计边界。

**旧路径为何合理**：把训练权重或完整上下文视为唯一知识来源，链路短且状态少。

**约束变化与机制**：exact-v1 的 `3. Approach` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-RAG` 负责 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；定位证据为 `arXiv:2603.12396v1 HTML — §3. Approach [facet=method]; https://arxiv.org/html/2603.12396v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12396v1.html; sha256:b03faf78a80c746ae3f180cad2d7250cb08ec09a11be42bdee05b35ba6366272`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1.5. Evaluation Metrics`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12396v1 HTML — §4.1.5. Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.12396v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12396v1.html; sha256:b03faf78a80c746ae3f180cad2d7250cb08ec09a11be42bdee05b35ba6366272`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5. Conclusion`。知识稳定且已被模型可靠覆盖时，直接生成仍具有更低延迟。

<!-- claim:SF-2026-ARXIV-2603-12396:start -->**Claim Boundary**：只支持 arXiv:2603.12396v1 §3. Approach 的机制与 §4.1.5. Evaluation Metrics 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12396:end -->
<!-- review:SF-2026-ARXIV-2603-12396:end -->
### KernelFoundry: Hardware-aware evolutionary GPU kernel optimization

<!-- review:SF-2026-ARXIV-2603-12440:start -->
**问题**：`KernelFoundry: Hardware-aware evolutionary GPU kernel optimization` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `3.1 System Architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.12440v1 HTML — §3.1 System Architecture [facet=method]; https://arxiv.org/html/2603.12440v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12440v1.html; sha256:2cb0d4ac88ab073756f4e43909c9f7484cf978d0a057e7b08472255f3853242d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Evaluation on SYCL kernel generation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12440v1 HTML — §5.2 Evaluation on SYCL kernel generation [facet=evaluation]; https://arxiv.org/html/2603.12440v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12440v1.html; sha256:2cb0d4ac88ab073756f4e43909c9f7484cf978d0a057e7b08472255f3853242d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-12440:start -->**Claim Boundary**：只支持 arXiv:2603.12440v1 §3.1 System Architecture 的机制与 §5.2 Evaluation on SYCL kernel generation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12440:end -->
<!-- review:SF-2026-ARXIV-2603-12440:end -->
### TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition

<!-- review:SF-2026-ARXIV-2603-12465:start -->
**问题**：端到端 LLM latency 常把 framework、launch、memory 和 synchronization 开销混成一个数字，导致优化目标归因错误。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：TaxBreak 将每个 kernel 的 host orchestration 拆为 framework translation、CUDA-library front-end translation 与 kernel-launch floor，并用 HDBI 对照 host orchestration 与 device-active time。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 execution-stack diagnosis 与 plan selection；TaxBreak 只提供 §III 的三段归因与 HDBI，不拥有 admission 或 placement。

**Evaluation contract 与未证明部分**：作者数据能说明所测栈中各类开销比例；这些比例不应外推到不同模型、硬件、精度或并发。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12465v1 HTML — §V Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12465v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12465v1.html; sha256:1d38142cac361bf377409ca78d8fe358d23b66f22e1e659aa213d86af609f23f`。

**Trade-off / failure / coexistence**：更细归因提高优化精度，却增加 tracing 扰动和版本维护；瓶颈明显的稳定路径可先用粗粒度 profiling。

<!-- claim:SF-2026-ARXIV-2603-12465:start -->**Claim Boundary**：只支持 arXiv:2603.12465v1 §III 的三段 execution-stack 分解与 HDBI，以及 §IV–§VI 的测试条件；不支持 request/stage/plan identity 或其他 profiler taxonomy。<!-- claim:SF-2026-ARXIV-2603-12465:end -->
<!-- review:SF-2026-ARXIV-2603-12465:end -->
### Hunting CUDA Bugs at Scale with cuFuzz

<!-- review:SF-2026-ARXIV-2603-12485:start -->
**问题**：`Hunting CUDA Bugs at Scale with cuFuzz` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `2.1. GPU Architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.12485v1 HTML — §2.1. GPU Architecture [facet=method]; https://arxiv.org/html/2603.12485v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12485v1.html; sha256:428f2705da3cd2d24bc0ca181c0a59ce0cf8978eed4e5390ee048f12835d084c`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7. Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12485v1 HTML — §7. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12485v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12485v1.html; sha256:428f2705da3cd2d24bc0ca181c0a59ce0cf8978eed4e5390ee048f12835d084c`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8.3. Thread-Interleaving Coverage Limitations`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-12485:start -->**Claim Boundary**：只支持 arXiv:2603.12485v1 §2.1. GPU Architecture 的机制与 §7. Evaluation 的公开 workload；§8.3. Thread-Interleaving Coverage Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12485:end -->
<!-- review:SF-2026-ARXIV-2603-12485:end -->
### Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies

<!-- review:SF-2026-ARXIV-2603-12510:start -->
**问题**：`Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `IV Method: Q-DIG` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12510v1 HTML — §IV Method: Q-DIG [facet=method]; https://arxiv.org/html/2603.12510v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12510v1.html; sha256:067bde76b19e70fc48bb1db4630a76e649d67088fabdd8109cf4c4c156f9181f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `VI-C Results: Real-World Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12510v1 HTML — §VI-C Results: Real-World Experiments [facet=evaluation]; https://arxiv.org/html/2603.12510v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12510v1.html; sha256:067bde76b19e70fc48bb1db4630a76e649d67088fabdd8109cf4c4c156f9181f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VII Conclusion and Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12510:start -->**Claim Boundary**：只支持 arXiv:2603.12510v1 §IV Method: Q-DIG 的机制与 §VI-C Results: Real-World Experiments 的公开 workload；§VII Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12510:end -->
<!-- review:SF-2026-ARXIV-2603-12510:end -->
### Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation

<!-- review:SF-2026-ARXIV-2603-12553:start -->
**问题**：`Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `3 Method` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.12553v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.12553v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12553v1.html; sha256:dee4a75237add006f93ec4275369f79ae24ec27b2342c43e33a377cd7f3a81de`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.3 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12553v1 HTML — §4.3 Main Results [facet=evaluation]; https://arxiv.org/html/2603.12553v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12553v1.html; sha256:dee4a75237add006f93ec4275369f79ae24ec27b2342c43e33a377cd7f3a81de`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations and Discussion.`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-12553:start -->**Claim Boundary**：只支持 arXiv:2603.12553v1 §3 Method 的机制与 §4.3 Main Results 的公开 workload；§Limitations and Discussion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12553:end -->
<!-- review:SF-2026-ARXIV-2603-12553:end -->
### Neural Gate: Mitigating Privacy Risks in LVLMs via Neuron-Level Gradient Gating

<!-- review:SF-2026-ARXIV-2603-12598:start -->
**问题**：`Neural Gate: Mitigating Privacy Risks in LVLMs via Neuron-Level Gradient Gating` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `8.1 Settings of Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12598v1 HTML — §8.1 Settings of Methods [facet=method]; https://arxiv.org/html/2603.12598v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12598v1.html; sha256:c3c5d382dad8da9a803e9cbd2a738d9a11fa135e15f5afa1da79c0a7e15dc65f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `8.3 Details of Evaluation Benchmark`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12598v1 HTML — §8.3 Details of Evaluation Benchmark [facet=evaluation]; https://arxiv.org/html/2603.12598v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12598v1.html; sha256:c3c5d382dad8da9a803e9cbd2a738d9a11fa135e15f5afa1da79c0a7e15dc65f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12598:start -->**Claim Boundary**：只支持 arXiv:2603.12598v1 §8.1 Settings of Methods 的机制与 §8.3 Details of Evaluation Benchmark 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12598:end -->
<!-- review:SF-2026-ARXIV-2603-12598:end -->
### ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents

<!-- review:SF-2026-ARXIV-2603-12614:start -->
**问题**：`ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3.2. ChainFuzzer Workflow` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12614v1 HTML — §3.2. ChainFuzzer Workflow [facet=method]; https://arxiv.org/html/2603.12614v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12614v1.html; sha256:91545519f157debb0c3f69753bf5c4db6777fcca3bb9d444330552781349419f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5. Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12614v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12614v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12614v1.html; sha256:91545519f157debb0c3f69753bf5c4db6777fcca3bb9d444330552781349419f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Discussion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12614:start -->**Claim Boundary**：只支持 arXiv:2603.12614v1 §3.2. ChainFuzzer Workflow 的机制与 §5. Evaluation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12614:end -->
<!-- review:SF-2026-ARXIV-2603-12614:end -->
### When Drafts Evolve: Speculative Decoding Meets Online Learning

<!-- review:SF-2026-ARXIV-2603-12617:start -->
**问题**：`When Drafts Evolve: Speculative Decoding Meets Online Learning` 检查的是 `INFER-SPECULATIVE-DECODING` 中 decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。 是否会改变现有设计边界。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：exact-v1 的 `4.2 Evaluation of Our Approach` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.12617v1 HTML — §4.2 Evaluation of Our Approach [facet=method]; https://arxiv.org/html/2603.12617v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12617v1.html; sha256:842788faef144175a9803b62a0ffa8b6949ce1c9537e266927d78218a13297c2`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix B Additional Experimental Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12617v1 HTML — §Appendix B Additional Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.12617v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12617v1.html; sha256:842788faef144175a9803b62a0ffa8b6949ce1c9537e266927d78218a13297c2`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2603-12617:start -->**Claim Boundary**：只支持 arXiv:2603.12617v1 §4.2 Evaluation of Our Approach 的机制与 §Appendix B Additional Experimental Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12617:end -->
<!-- review:SF-2026-ARXIV-2603-12617:end -->
### AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents

<!-- review:SF-2026-ARXIV-2603-12621:start -->
**问题**：`AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `2. System Overview and Threat Model` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12621v1 HTML — §2. System Overview and Threat Model [facet=method]; https://arxiv.org/html/2603.12621v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12621v1.html; sha256:313a60c293e0dc61b408f483fd91d01bb32021edb9484c67c0fd6f5af563a5cf`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3. Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12621v1 HTML — §3. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12621v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12621v1.html; sha256:313a60c293e0dc61b408f483fd91d01bb32021edb9484c67c0fd6f5af563a5cf`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations.`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-12621:start -->**Claim Boundary**：只支持 arXiv:2603.12621v1 §2. System Overview and Threat Model 的机制与 §3. Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12621:end -->
<!-- review:SF-2026-ARXIV-2603-12621:end -->
### Joint Optimization of Multi-agent Memory System

<!-- review:SF-2026-ARXIV-2603-12631:start -->
**问题**：`Joint Optimization of Multi-agent Memory System` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `4 Method` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.12631v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.12631v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12631v1.html; sha256:0ac15284b3eeb172990e5fbc328248c0a94cbd6e32378672536f4df16f9b9af2`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12631v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.12631v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12631v1.html; sha256:0ac15284b3eeb172990e5fbc328248c0a94cbd6e32378672536f4df16f9b9af2`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Appendix E Limitation`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-12631:start -->**Claim Boundary**：只支持 arXiv:2603.12631v1 §4 Method 的机制与 §5 Experiments 的公开 workload；§Appendix E Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12631:end -->
<!-- review:SF-2026-ARXIV-2603-12631:end -->
### RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization

<!-- review:SF-2026-ARXIV-2603-12639:start -->
**问题**：`RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `3.1 Architecture Design` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.12639v1 HTML — §3.1 Architecture Design [facet=method]; https://arxiv.org/html/2603.12639v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12639v1.html; sha256:c8dd88873aa9ea37405a9f4bc518edc5cf25adb5d255830635e5569a97e59a4d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Video Quality Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12639v1 HTML — §4.2 Video Quality Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12639v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12639v1.html; sha256:c8dd88873aa9ea37405a9f4bc518edc5cf25adb5d255830635e5569a97e59a4d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.4 Ablation Study`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-12639:start -->**Claim Boundary**：只支持 arXiv:2603.12639v1 §3.1 Architecture Design 的机制与 §4.2 Video Quality Evaluation 的公开 workload；§4.4 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12639:end -->
<!-- review:SF-2026-ARXIV-2603-12639:end -->
### 98$\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router

<!-- review:SF-2026-ARXIV-2603-12646:start -->
**问题**：`98$\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `IV System Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.12646v1 HTML — §IV System Design [facet=method]; https://arxiv.org/html/2603.12646v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12646v1.html; sha256:c0006e50345bebc407d79f6e0fdf7cc430678cf394b0def28c6e40829ef1874c`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12646v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12646v1.html; sha256:c0006e50345bebc407d79f6e0fdf7cc430678cf394b0def28c6e40829ef1874c`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VI Discussion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-12646:start -->**Claim Boundary**：只支持 arXiv:2603.12646v1 §IV System Design 的机制与 §Evaluation 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12646:end -->
<!-- review:SF-2026-ARXIV-2603-12646:end -->
### VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model

<!-- review:SF-2026-ARXIV-2603-12655:start -->
**问题**：`VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `0.B.1 Model Architecture` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.12655v1 HTML — §0.B.1 Model Architecture [facet=method]; https://arxiv.org/html/2603.12655v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12655v1.html; sha256:db942c8f20b970c741b6543bd743557c7b560669f728ca6506a763feb24f0b54`。

**Evaluation contract 与未证明部分**：公开验证定位在 `0.B.2 Evaluation Datasets`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12655v1 HTML — §0.B.2 Evaluation Datasets [facet=evaluation]; https://arxiv.org/html/2603.12655v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12655v1.html; sha256:db942c8f20b970c741b6543bd743557c7b560669f728ca6506a763feb24f0b54`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations.`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-12655:start -->**Claim Boundary**：只支持 arXiv:2603.12655v1 §0.B.1 Model Architecture 的机制与 §0.B.2 Evaluation Datasets 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12655:end -->
<!-- review:SF-2026-ARXIV-2603-12655:end -->
### HyGra: Accelerating Network-State Simulation for LLM Training in DCNs via Adaptive Packet-Flow Granularity

<!-- review:SF-2026-ARXIV-2603-12671:start -->
**问题**：`HyGra: Accelerating Network-State Simulation for LLM Training in DCNs via Adaptive Packet-Flow Granularity` 检查的是 `TRAIN-DISTRIBUTED-TRAINING` 中 参数、optimizer state 和通信规模越过单设备边界。 是否会改变现有设计边界。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：exact-v1 的 `V Architecture of Execution Layer` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.12671v1 HTML — §V Architecture of Execution Layer [facet=method]; https://arxiv.org/html/2603.12671v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12671v1.html; sha256:a625e5c3f9654ce9fefcf0bbc066dac1608a85108deea3e889d391095ac57810`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.12671v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12671v1.html; sha256:a625e5c3f9654ce9fefcf0bbc066dac1608a85108deea3e889d391095ac57810`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VIII Conclusion`。模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2603-12671:start -->**Claim Boundary**：只支持 arXiv:2603.12671v1 §V Architecture of Execution Layer 的机制与 §Evaluation 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12671:end -->
<!-- review:SF-2026-ARXIV-2603-12671:end -->
### Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity

<!-- review:SF-2026-ARXIV-2603-12707:start -->
**问题**：`Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `5 HeteroServe: System Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.12707v1 HTML — §5 HeteroServe: System Design [facet=method]; https://arxiv.org/html/2603.12707v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12707v1.html; sha256:a70e9761c4053129a3e0181ed315aeee257552d82fce9cf8e2848237b5a74314`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12707v1 HTML — §6 Experiments [facet=evaluation]; https://arxiv.org/html/2603.12707v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12707v1.html; sha256:a70e9761c4053129a3e0181ed315aeee257552d82fce9cf8e2848237b5a74314`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-12707:start -->**Claim Boundary**：只支持 arXiv:2603.12707v1 §5 HeteroServe: System Design 的机制与 §6 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12707:end -->
<!-- review:SF-2026-ARXIV-2603-12707:end -->
### Adaptive Vision-Language Model Routing for Computer Use Agents

<!-- review:SF-2026-ARXIV-2603-12823:start -->
**问题**：`Adaptive Vision-Language Model Routing for Computer Use Agents` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `Appendix E Cost Projection Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.12823v1 HTML — §Appendix E Cost Projection Methodology [facet=method]; https://arxiv.org/html/2603.12823v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12823v1.html; sha256:ba18a88724211e9c8e65e9c8c8b638168932b6fd3f0ff0def17a559953e3b31d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Evidence and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12823v1 HTML — §4 Evidence and Analysis [facet=evaluation]; https://arxiv.org/html/2603.12823v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12823v1.html; sha256:ba18a88724211e9c8e65e9c8c8b638168932b6fd3f0ff0def17a559953e3b31d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Limitations`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-12823:start -->**Claim Boundary**：只支持 arXiv:2603.12823v1 §Appendix E Cost Projection Methodology 的机制与 §4 Evidence and Analysis 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12823:end -->
<!-- review:SF-2026-ARXIV-2603-12823:end -->
### Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking

<!-- review:SF-2026-ARXIV-2603-12831:start -->
**问题**：混合 LLM 请求在 GPU attention 饱和时仍可能留下 CPU 和数据搬移空隙，单一设备 admission 难同时守住不同 SLO。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Online controller 在 SLO admission 下安排 CPU attention piggyback，并通过 task queues 与 residual correction 管理 CPU/GPU 分支的执行和输出一致性。

**State / data / control owner**：`INFER-SCHEDULING` 负责 online admission/piggyback，机制定位于 §3.3.2–§3.3.6，queue 与 residual correctness 定位于 §4。

**Evaluation contract 与未证明部分**：§5 的 A100/CPU testbed 支持所测 SLO/吞吐变化；未覆盖 topology、model、NUMA、网络和生产长尾不属于证明。

**Trade-off / failure / coexistence**：异构并用扩大有效容量，但带来状态同步、预测误差和尾延迟反噬；负载同质或 GPU 未饱和时单 GPU 路径更可控。

<!-- claim:SF-2026-ARXIV-2603-12831:start -->**Claim Boundary**：只支持 arXiv:2603.12831v1 §3.3.2–§3.3.6、§4 与 §5 的 online scheduling、correctness 与 A100/CPU testbed；§6 之外不外推。<!-- claim:SF-2026-ARXIV-2603-12831:end -->
<!-- review:SF-2026-ARXIV-2603-12831:end -->
### Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization

<!-- review:SF-2026-ARXIV-2603-12933:start -->
**问题**：`Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization` 检查的是 `AGENT-MULTI-AGENT` 中 任务并行、能力异质和跨信任域协作迫使系统显式管理委托与共享状态。 是否会改变现有设计边界。

**旧路径为何合理**：单 agent 持有完整上下文和控制流，规模小时最容易归因。

**约束变化与机制**：exact-v1 的 `III Methodology` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 agent identity、委托边、消息状态、协作协议与冲突处理；定位证据为 `arXiv:2603.12933v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.12933v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12933v1.html; sha256:2d525b951a71a2d5ab3cf7002aa9d79013f93cb3b0ea7af5bab17aef7c63c886`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV-B Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12933v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.12933v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12933v1.html; sha256:2d525b951a71a2d5ab3cf7002aa9d79013f93cb3b0ea7af5bab17aef7c63c886`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V Conclusion`。任务短且角色不需要隔离时，单 agent 仍有更低协调成本。

<!-- claim:SF-2026-ARXIV-2603-12933:start -->**Claim Boundary**：只支持 arXiv:2603.12933v1 §III Methodology 的机制与 §IV-B Main Results 的公开 workload；§V Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12933:end -->
<!-- review:SF-2026-ARXIV-2603-12933:end -->
### Almost-Free Queue Jumping for Prior Inputs in Private Neural Inference

<!-- review:SF-2026-ARXIV-2603-12946:start -->
**问题**：隐私推理的批处理按固定顺序执行时，紧急请求插队会破坏加密计算共享并拖慢全批。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：PrivQJ 在 HE/MPC 处理中回收 slot，让高优先级输入 piggyback 到正在执行的 batch，而不重启共同计算。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.12946v1 HTML — §III-A Overview of PrivQJ [facet=method]; https://arxiv.org/html/2603.12946v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12946v1.html; sha256:525895ee2c45e090d98591f34d8ecacbcd1149adf9b3451e846840cd0db4e133`。

**Evaluation contract 与未证明部分**：理论和实验只支持论文 primitive、batch shape 与 threat model；不证明通用神经服务具有相同开销。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.12946v1 HTML — §IV Evaluation [facet=evaluation]; https://arxiv.org/html/2603.12946v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.12946v1.html; sha256:525895ee2c45e090d98591f34d8ecacbcd1149adf9b3451e846840cd0db4e133`。

**Trade-off / failure / coexistence**：优先插队增加调度 metadata 与公平性问题；无优先级或 batch 很小时固定顺序更简单。

<!-- claim:SF-2026-ARXIV-2603-12946:start -->**Claim Boundary**：只支持 arXiv:2603.12946v1 §III-A Overview of PrivQJ 的机制与 §IV Evaluation 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-12946:end -->
<!-- review:SF-2026-ARXIV-2603-12946:end -->
### Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation

<!-- review:SF-2026-ARXIV-2603-13017:start -->
**问题**：`Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `4.3 Grading Methodology` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.13017v1 HTML — §4.3 Grading Methodology [facet=method]; https://arxiv.org/html/2603.13017v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13017v1.html; sha256:59fc8064461c0c93b04424dd1619261aa674667b679cf941998709fc2eeb4406`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.1 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13017v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13017v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13017v1.html; sha256:59fc8064461c0c93b04424dd1619261aa674667b679cf941998709fc2eeb4406`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Limitations`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-13017:start -->**Claim Boundary**：只支持 arXiv:2603.13017v1 §4.3 Grading Methodology 的机制与 §5.1 Main Results 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13017:end -->
<!-- review:SF-2026-ARXIV-2603-13017:end -->
### ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning

<!-- review:SF-2026-ARXIV-2603-13019:start -->
**问题**：`ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning` 检查的是 `TRAIN-GRPO` 中 稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。 是否会改变现有设计边界。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：exact-v1 的 `3 Architecture` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.13019v1 HTML — §3 Architecture [facet=method]; https://arxiv.org/html/2603.13019v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13019v1.html; sha256:233a406636b677d75e363e8b548a85d3980b2735494f385ac5a43c51e91c8423`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13019v1 HTML — §6 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13019v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13019v1.html; sha256:233a406636b677d75e363e8b548a85d3980b2735494f385ac5a43c51e91c8423`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Conclusion`。高质量逐样本监督充足时 SFT/DPO 仍更简单。

<!-- claim:SF-2026-ARXIV-2603-13019:start -->**Claim Boundary**：只支持 arXiv:2603.13019v1 §3 Architecture 的机制与 §6 Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13019:end -->
<!-- review:SF-2026-ARXIV-2603-13019:end -->
### PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses

<!-- review:SF-2026-ARXIV-2603-13026:start -->
**问题**：`PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3.3 Design of PISmith` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13026v1 HTML — §3.3 Design of PISmith [facet=method]; https://arxiv.org/html/2603.13026v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13026v1.html; sha256:d7fd9c28cec030bfbf8dca7a792a7ccf1edf1deb9904531a0b99ed2da1da876e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix E Full Results for Utility–Robustness Evaluation (RQ2)`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13026v1 HTML — §Appendix E Full Results for Utility–Robustness Evaluation (RQ2) [facet=evaluation]; https://arxiv.org/html/2603.13026v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13026v1.html; sha256:d7fd9c28cec030bfbf8dca7a792a7ccf1edf1deb9904531a0b99ed2da1da876e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.5 Ablation Studies`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-13026:start -->**Claim Boundary**：只支持 arXiv:2603.13026v1 §3.3 Design of PISmith 的机制与 §Appendix E Full Results for Utility–Robustness Evaluation (RQ2) 的公开 workload；§4.5 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13026:end -->
<!-- review:SF-2026-ARXIV-2603-13026:end -->
### ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models

<!-- review:SF-2026-ARXIV-2603-13033:start -->
**问题**：`ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `Algorithms.` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.13033v1 HTML — §Algorithms. [facet=method]; https://arxiv.org/html/2603.13033v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13033v1.html; sha256:11a2e8ad43bbf5df292784b2a5d2d2ae17f47c2bf51f913fdf713a637bb449fe`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13033v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13033v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13033v1.html; sha256:11a2e8ad43bbf5df292784b2a5d2d2ae17f47c2bf51f913fdf713a637bb449fe`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Discussion and Future Work`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-13033:start -->**Claim Boundary**：只支持 arXiv:2603.13033v1 §Algorithms. 的机制与 §5.2 Main Results 的公开 workload；§6 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13033:end -->
<!-- review:SF-2026-ARXIV-2603-13033:end -->
### Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation

<!-- review:SF-2026-ARXIV-2603-13099:start -->
**问题**：`Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `S6.1 GRPO Framework` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.13099v1 HTML — §S6.1 GRPO Framework [facet=method]; https://arxiv.org/html/2603.13099v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13099v1.html; sha256:365d0c76087a379f5bd654811570ab915aa45547278f81dcd5f35e678ea6b0c9`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13099v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.13099v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13099v1.html; sha256:365d0c76087a379f5bd654811570ab915aa45547278f81dcd5f35e678ea6b0c9`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.4 Ablation Studies`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-13099:start -->**Claim Boundary**：只支持 arXiv:2603.13099v1 §S6.1 GRPO Framework 的机制与 §4.2 Main Results 的公开 workload；§4.4 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13099:end -->
<!-- review:SF-2026-ARXIV-2603-13099:end -->
### AgentRM: An OS-Inspired Resource Manager for LLM Agent Systems

<!-- review:SF-2026-ARXIV-2603-13110:start -->
**问题**：并发 Agent 共享 execution lanes、provider rate limits 与 Context window 时，FIFO、僵尸执行和 quota cascade 会破坏交互性。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：AgentRM 以 MLFQ、zombie reaper、rate-limit admission、DRF-inspired fairness、Context Lifecycle Manager 与 resource monitor 形成平台资源控制面。

**State / data / control owner**：`AGENT-PLATFORM` 负责跨 run 资源控制，Workflow 仍拥有业务 DAG 与副作用真值；组件定位于 exact-v1 §IV。

**Evaluation contract 与未证明部分**：§VI 结果只绑定由观察模式构造的 simulated agent workloads，不证明生产语义公平、durable workflow commit 或 lease recovery。

**Trade-off / failure / coexistence**：独立资源层增加错误分类、饥饿、reaper 误杀与 compaction loss；小规模单 Agent 仍可用简单队列。

<!-- claim:SF-2026-ARXIV-2603-13110:start -->**Claim Boundary**：只支持 arXiv:2603.13110v1 §IV 的 middleware 与 §VI simulated workloads；§VII-C 之外不证明 production fairness、durable commit、versioned lease 或 recovery。<!-- claim:SF-2026-ARXIV-2603-13110:end -->
<!-- review:SF-2026-ARXIV-2603-13110:end -->
### Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception

<!-- review:SF-2026-ARXIV-2603-13176:start -->
**问题**：`Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `III Perception Scheduling Framework` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.13176v1 HTML — §III Perception Scheduling Framework [facet=method]; https://arxiv.org/html/2603.13176v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13176v1.html; sha256:1b8da69d8c5879a1218fb630ad90bd48b9deca55397ec3229f98696b9b70aa33`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V-C Perception Module Selector Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13176v1 HTML — §V-C Perception Module Selector Evaluation [facet=evaluation]; https://arxiv.org/html/2603.13176v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13176v1.html; sha256:1b8da69d8c5879a1218fb630ad90bd48b9deca55397ec3229f98696b9b70aa33`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VII Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-13176:start -->**Claim Boundary**：只支持 arXiv:2603.13176v1 §III Perception Scheduling Framework 的机制与 §V-C Perception Module Selector Evaluation 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13176:end -->
<!-- review:SF-2026-ARXIV-2603-13176:end -->
### LLM Constitutional Multi-Agent Governance

<!-- review:SF-2026-ARXIV-2603-13189:start -->
**问题**：`LLM Constitutional Multi-Agent Governance` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3 Methodology` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.13189v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.13189v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13189v1.html; sha256:ce7a4de78a138c700e1e3305aae74520c1323315e400ce7df39bd86b857a58fa`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1 Multi-Seed Replication and Statistical Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13189v1 HTML — §4.1 Multi-Seed Replication and Statistical Validation [facet=evaluation]; https://arxiv.org/html/2603.13189v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13189v1.html; sha256:ce7a4de78a138c700e1e3305aae74520c1323315e400ce7df39bd86b857a58fa`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations.`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-13189:start -->**Claim Boundary**：只支持 arXiv:2603.13189v1 §3 Methodology 的机制与 §4.1 Multi-Seed Replication and Statistical Validation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13189:end -->
<!-- review:SF-2026-ARXIV-2603-13189:end -->
### Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models

<!-- review:SF-2026-ARXIV-2603-13215:start -->
**问题**：`Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `3 Benchmarking State Evolution in Video World Models` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.13215v1 HTML — §3 Benchmarking State Evolution in Video World Models [facet=method]; https://arxiv.org/html/2603.13215v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13215v1.html; sha256:ed90a31ecfdf4ab3e080229d688c50e5301165cc74448528c5bf237c02c7bf52`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.2 Evaluation Criteria and Automatic Verifiers`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.13215v1 HTML — §3.2 Evaluation Criteria and Automatic Verifiers [facet=evaluation]; https://arxiv.org/html/2603.13215v1; papers/2026/03/_sources/daily-20260316/exact-v1-bodies/2603.13215v1.html; sha256:ed90a31ecfdf4ab3e080229d688c50e5301165cc74448528c5bf237c02c7bf52`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusions`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-13215:start -->**Claim Boundary**：只支持 arXiv:2603.13215v1 §3 Benchmarking State Evolution in Video World Models 的机制与 §3.2 Evaluation Criteria and Automatic Verifiers 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-13215:end -->
<!-- review:SF-2026-ARXIV-2603-13215:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-12465 | score_7_9;potential_books_delta | selected | DA-20260316-04 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260316-04 |
| SF-2026-ARXIV-2603-12831 | score_7_9;potential_books_delta | selected | DA-20260316-19 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260316-19 |
| SF-2026-ARXIV-2603-13110 | score_7_9;potential_books_delta | selected | DA-20260316-27 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260316-27 |

<!-- analysis:DA-20260316-04:start -->
### TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition

端到端 LLM latency 常把 framework、launch、memory 和 synchronization 开销混成一个数字，导致优化目标归因错误。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：TaxBreak 以分层 instrumentation 将请求时间拆到算子、runtime 与系统边界，并把不可归属空洞作为显式 overhead 类别。 其公开验证边界为：作者数据能说明所测栈中各类开销比例；这些比例不应外推到不同模型、硬件、精度或并发。 新增代价与回退条件为：更细归因提高优化精度，却增加 tracing 扰动和版本维护；瓶颈明显的稳定路径可先用粗粒度 profiling。
<!-- analysis:DA-20260316-04:end -->
<!-- analysis:DA-20260316-19:start -->
### Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking

混合 LLM 请求在 GPU attention 饱和时仍可能留下 CPU 和数据搬移空隙，单一设备 admission 难同时守住不同 SLO。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：论文让 CPU attention work 在 GPU request 间隙 piggyback，并由 SLO slack、阶段和资源占用决定是否卸载与何时回收。 其公开验证边界为：实验支持给定 CPU/GPU、模型和请求混合中的 SLO/吞吐变化；未覆盖的 NUMA、网络和长尾输入不属于证明。 新增代价与回退条件为：异构并用扩大有效容量，但带来状态同步、预测误差和尾延迟反噬；负载同质或 GPU 未饱和时单 GPU 路径更可控。
<!-- analysis:DA-20260316-19:end -->
<!-- analysis:DA-20260316-27:start -->
### AgentRM: An OS-Inspired Resource Manager for LLM Agent Systems

agent 系统把 token、tool、memory 和并发额度散落在 workflow 代码中，资源压力会反过来破坏行为语义。 旧路径在其原约束下仍合理：把 agent loop 留在进程内代码，开发快且控制流直观。 本 family 的设计变化是：AgentRM 把资源描述、allocation、preemption 与 accounting 提升为独立 manager state，并为 agent execution 提供受控 lease。 其公开验证边界为：公开实验或原型只支持论文定义 workload 下的资源协调，不证明 OS 类抽象已经解决语义公平、安全或跨平台兼容。 新增代价与回退条件为：独立资源层提升可治理性，却增加控制面和 lease failure mode；小规模单 agent 仍可由 workflow 直接持有资源。
<!-- analysis:DA-20260316-27:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-12277 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12277 | delta:SF-2026-ARXIV-2603-12277 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12277 |
| SF-2026-ARXIV-2603-12396 | AGENT-RAG | books/part-07-agent/76-rag.md#agentic-retrieval：relevance-也可以是执行先验 (section Ch-owner) | books/part-07-agent/75-context.md#第75章-context (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12396 | delta:SF-2026-ARXIV-2603-12396 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12396 |
| SF-2026-ARXIV-2603-12440 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12440 | delta:SF-2026-ARXIV-2603-12440 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12440 |
| SF-2026-ARXIV-2603-12465 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-vllm (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12465 | delta:SF-2026-ARXIV-2603-12465 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-12465 |
| SF-2026-ARXIV-2603-12485 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12485 | delta:SF-2026-ARXIV-2603-12485 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12485 |
| SF-2026-ARXIV-2603-12510 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12510 | delta:SF-2026-ARXIV-2603-12510 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12510 |
| SF-2026-ARXIV-2603-12553 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12553 | delta:SF-2026-ARXIV-2603-12553 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12553 |
| SF-2026-ARXIV-2603-12598 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#隐私检测是-policy-bound-sensor，不是安全判决 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12598 | delta:SF-2026-ARXIV-2603-12598 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12598 |
| SF-2026-ARXIV-2603-12614 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12614 | delta:SF-2026-ARXIV-2603-12614 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12614 |
| SF-2026-ARXIV-2603-12617 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12617 | delta:SF-2026-ARXIV-2603-12617 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12617 |
| SF-2026-ARXIV-2603-12621 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#search-query-本身也是-public-egress-action (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12621 | delta:SF-2026-ARXIV-2603-12621 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12621 |
| SF-2026-ARXIV-2603-12631 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12631 | delta:SF-2026-ARXIV-2603-12631 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12631 |
| SF-2026-ARXIV-2603-12639 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#在谈-state-之前，先声明预测-channel (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12639 | delta:SF-2026-ARXIV-2603-12639 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12639 |
| SF-2026-ARXIV-2603-12646 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#不确定输出长度下的-future-state-reservation (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12646 | delta:SF-2026-ARXIV-2603-12646 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12646 |
| SF-2026-ARXIV-2603-12655 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12655 | delta:SF-2026-ARXIV-2603-12655 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12655 |
| SF-2026-ARXIV-2603-12671 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#arrival-bias-与-stale-direction-是两种独立误差 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12671 | delta:SF-2026-ARXIV-2603-12671 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12671 |
| SF-2026-ARXIV-2603-12707 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12707 | delta:SF-2026-ARXIV-2603-12707 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12707 |
| SF-2026-ARXIV-2603-12823 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12823 | delta:SF-2026-ARXIV-2603-12823 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12823 |
| SF-2026-ARXIV-2603-12831 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#低带宽拓扑要联合预算-hops、bytes-与-steps (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12831 | delta:SF-2026-ARXIV-2603-12831 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-12831 |
| SF-2026-ARXIV-2603-12933 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12933 | delta:SF-2026-ARXIV-2603-12933 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12933 |
| SF-2026-ARXIV-2603-12946 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-12946 | delta:SF-2026-ARXIV-2603-12946 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-12946 |
| SF-2026-ARXIV-2603-13017 | AGENT-MEMORY | books/part-07-agent/77-memory.md#从-outcome-reward-到-content-level-credit：归因只能约束写入，不能成为真值 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13017 | delta:SF-2026-ARXIV-2603-13017 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13017 |
| SF-2026-ARXIV-2603-13019 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#measurement-也是-reward-interface-的一部分 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13019 | delta:SF-2026-ARXIV-2603-13019 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13019 |
| SF-2026-ARXIV-2603-13026 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13026 | delta:SF-2026-ARXIV-2603-13026 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13026 |
| SF-2026-ARXIV-2603-13033 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13033 | delta:SF-2026-ARXIV-2603-13033 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13033 |
| SF-2026-ARXIV-2603-13099 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13099 | delta:SF-2026-ARXIV-2603-13099 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13099 |
| SF-2026-ARXIV-2603-13110 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#scheduling-不只是-gpu (section Ch-owner) | books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13110 | delta:SF-2026-ARXIV-2603-13110 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-13110 |
| SF-2026-ARXIV-2603-13176 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13176 | delta:SF-2026-ARXIV-2603-13176 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13176 |
| SF-2026-ARXIV-2603-13189 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13189 | delta:SF-2026-ARXIV-2603-13189 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13189 |
| SF-2026-ARXIV-2603-13215 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-13215 | delta:SF-2026-ARXIV-2603-13215 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-13215 |

<!-- books-review:SF-2026-ARXIV-2603-12277:start -->
### Prompt Injection as Role Confusion — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12277:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：交互结束也不是 prompt injection 的自然终点。攻击内容一旦被写入 session context、长期 memory 或可复用 skill，可能在之后的良性 query 才触发；只做当前 response moderation 会把 dormant payload 当成已消失。持久状态因此必须在写入时保存 origin、trust/taint 与 policy generation，在每次读取或执行前按当前 principal、工具权限和目的重新验证，过期或来源不明时 quarantine、降权或删除。<!-- existing:SF-2026-ARXIV-2603-12277:end -->

<!-- delta:SF-2026-ARXIV-2603-12277:start -->新证据差异：exact-v1 的 `Methodology: Isolating Role Signals.` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12277:end -->

边界：只支持 arXiv:2603.12277v1 §Methodology: Isolating Role Signals. 的机制与 §Evaluation. 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12277:end -->
<!-- books-review:SF-2026-ARXIV-2603-12396:start -->
### Test-Time Strategies for More Efficient and Accurate Agentic RAG — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12396:start -->已读 owner `books/part-07-agent/76-rag.md` 与相邻章节。现有命题：RARG 预印本在固定 corpus 的 BrowseComp-Plus 与 BRIGHT 设置中报告了更好的 accuracy/interaction-cost frontier，并通过 document order、entry-point paragraphs 与 match-level reranking 实现这种 prior。该结果仍是单篇作者实验，依赖具体 embedding、 corpus、模型、tool budget 与 truncation policy；因此本章只吸收机制，不把其 benchmark 外推为所有 RAG 或 Agentic Search 的默认实现。<!-- existing:SF-2026-ARXIV-2603-12396:end -->

<!-- delta:SF-2026-ARXIV-2603-12396:start -->新证据差异：exact-v1 的 `3. Approach` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12396:end -->

边界：只支持 arXiv:2603.12396v1 §3. Approach 的机制与 §4.1.5. Evaluation Metrics 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12396:end -->
<!-- books-review:SF-2026-ARXIV-2603-12440:start -->
### KernelFoundry: Hardware-aware evolutionary GPU kernel optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12440:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。<!-- existing:SF-2026-ARXIV-2603-12440:end -->

<!-- delta:SF-2026-ARXIV-2603-12440:start -->新证据差异：exact-v1 的 `3.1 System Architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12440:end -->

边界：只支持 arXiv:2603.12440v1 §3.1 System Architecture 的机制与 §5.2 Evaluation on SYCL kernel generation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12440:end -->
<!-- books-review:SF-2026-ARXIV-2603-12465:start -->
### TaxBreak: Unmasking the Hidden Costs of LLM Inference Through Overhead Decomposition — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12465:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-12465:end -->

<!-- delta:SF-2026-ARXIV-2603-12465:start -->新证据差异：TaxBreak 以分层 instrumentation 将请求时间拆到算子、runtime 与系统边界，并把不可归属空洞作为显式 overhead 类别。<!-- delta:SF-2026-ARXIV-2603-12465:end -->

边界：只支持 arXiv:2603.12465v1 §III 的三段 execution-stack 分解与 HDBI，以及 §IV–§VI 的测试条件；不支持 request/stage/plan identity。已重路由 Ch49 并等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-12465:end -->
<!-- books-review:SF-2026-ARXIV-2603-12485:start -->
### Hunting CUDA Bugs at Scale with cuFuzz — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12485:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：独立 kernel launch 对大算子、稳定 control flow 和容易 capture 的 shape 最透明，CPU submission 开销相对计算也很小；CUDA Graph 进一步把重复 DAG 的准备成本移出 hot path。动态 inference、attention 辅助操作和 micro-batch 中出现大量短小算子后，单次 CPU→GPU launch 可能比算子本身更贵，而 graph 又要求可重复的结构，此时静态 fusion 与 graph capture 之间出现一个运行时分支。<!-- existing:SF-2026-ARXIV-2603-12485:end -->

<!-- delta:SF-2026-ARXIV-2603-12485:start -->新证据差异：exact-v1 的 `2.1. GPU Architecture` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12485:end -->

边界：只支持 arXiv:2603.12485v1 §2.1. GPU Architecture 的机制与 §7. Evaluation 的公开 workload；§8.3. Thread-Interleaving Coverage Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12485:end -->
<!-- books-review:SF-2026-ARXIV-2603-12510:start -->
### Red-Teaming Vision-Language-Action Models via Quality Diversity Prompt Generation for Robust Robot Policies — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12510:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：交互结束也不是 prompt injection 的自然终点。攻击内容一旦被写入 session context、长期 memory 或可复用 skill，可能在之后的良性 query 才触发；只做当前 response moderation 会把 dormant payload 当成已消失。持久状态因此必须在写入时保存 origin、trust/taint 与 policy generation，在每次读取或执行前按当前 principal、工具权限和目的重新验证，过期或来源不明时 quarantine、降权或删除。<!-- existing:SF-2026-ARXIV-2603-12510:end -->

<!-- delta:SF-2026-ARXIV-2603-12510:start -->新证据差异：exact-v1 的 `IV Method: Q-DIG` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12510:end -->

边界：只支持 arXiv:2603.12510v1 §IV Method: Q-DIG 的机制与 §VI-C Results: Real-World Experiments 的公开 workload；§VII Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12510:end -->
<!-- books-review:SF-2026-ARXIV-2603-12553:start -->
### Beyond Dense Futures: World Models as Structured Planners for Robotic Manipulation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12553:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-12553:end -->

<!-- delta:SF-2026-ARXIV-2603-12553:start -->新证据差异：exact-v1 的 `3 Method` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12553:end -->

边界：只支持 arXiv:2603.12553v1 §3 Method 的机制与 §4.3 Main Results 的公开 workload；§Limitations and Discussion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12553:end -->
<!-- books-review:SF-2026-ARXIV-2603-12598:start -->
### Neural Gate: Mitigating Privacy Risks in LVLMs via Neuron-Level Gradient Gating — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12598:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：OpenAI Privacy Filter 的 model card 明确把该模型限定为 data-minimization/redaction aid， 而非 anonymization 或 compliance guarantee。这一案例的长期结论是：**privacy filter 必须 绑定组织策略、目标分布、校准版本和人工升级路径**；默认阈值和作者 benchmark 不得外推为 任意 tenant、语言或高风险场景的安全保证。<!-- existing:SF-2026-ARXIV-2603-12598:end -->

<!-- delta:SF-2026-ARXIV-2603-12598:start -->新证据差异：exact-v1 的 `8.1 Settings of Methods` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12598:end -->

边界：只支持 arXiv:2603.12598v1 §8.1 Settings of Methods 的机制与 §8.3 Details of Evaluation Benchmark 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12598:end -->
<!-- books-review:SF-2026-ARXIV-2603-12614:start -->
### ChainFuzzer: Greybox Fuzzing for Workflow-Level Multi-Tool Vulnerabilities in LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12614:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-12614:end -->

<!-- delta:SF-2026-ARXIV-2603-12614:start -->新证据差异：exact-v1 的 `3.2. ChainFuzzer Workflow` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12614:end -->

边界：只支持 arXiv:2603.12614v1 §3.2. ChainFuzzer Workflow 的机制与 §5. Evaluation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12614:end -->
<!-- books-review:SF-2026-ARXIV-2603-12617:start -->
### When Drafts Evolve: Speculative Decoding Meets Online Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12617:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2603-12617:end -->

<!-- delta:SF-2026-ARXIV-2603-12617:start -->新证据差异：exact-v1 的 `4.2 Evaluation of Our Approach` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12617:end -->

边界：只支持 arXiv:2603.12617v1 §4.2 Evaluation of Our Approach 的机制与 §Appendix B Additional Experimental Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12617:end -->
<!-- books-review:SF-2026-ARXIV-2603-12621:start -->
### AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12621:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐次 tool call 都通过权限检查，仍不代表跨调用链安全：第一步合法读取出的敏感 value，可能在第二步被送进同样合法但不应接收它的 sink，形成 permission laundering。更强的 contract 把 authority 绑定到数据 value、允许的 transformation 与 sink，并规定跨调用只能单调收紧，不能由中间 Agent 重新扩大。Policy engine 拥有授权与衰减规则，tool runtime 只执行经过 capability/label 检查的调用，workflow trace 保存 authority provenance。<!-- existing:SF-2026-ARXIV-2603-12621:end -->

<!-- delta:SF-2026-ARXIV-2603-12621:start -->新证据差异：exact-v1 的 `2. System Overview and Threat Model` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12621:end -->

边界：只支持 arXiv:2603.12621v1 §2. System Overview and Threat Model 的机制与 §3. Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12621:end -->
<!-- books-review:SF-2026-ARXIV-2603-12631:start -->
### Joint Optimization of Multi-agent Memory System — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12631:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-12631:end -->

<!-- delta:SF-2026-ARXIV-2603-12631:start -->新证据差异：exact-v1 的 `4 Method` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12631:end -->

边界：只支持 arXiv:2603.12631v1 §4 Method 的机制与 §5 Experiments 的公开 workload；§Appendix E Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12631:end -->
<!-- books-review:SF-2026-ARXIV-2603-12639:start -->
### RoboStereo: Dual-Tower 4D Embodied World Models for Unified Policy Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12639:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：第一种回答“若执行这些 action，环境可能如何变化”，因此由 World Model 拥有；第二种更接近 policy 或 self-model，回答“看到这些 observation，agent 会怎样行动”；第三种描述二者闭环后实际可见的 trajectory。 三者可以在观测到的 policy support 上给出相同 continuation，却不拥有相同的 counterfactual contract。<!-- existing:SF-2026-ARXIV-2603-12639:end -->

<!-- delta:SF-2026-ARXIV-2603-12639:start -->新证据差异：exact-v1 的 `3.1 Architecture Design` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12639:end -->

边界：只支持 arXiv:2603.12639v1 §3.1 Architecture Design 的机制与 §4.2 Video Quality Evaluation 的公开 workload；§4.4 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12639:end -->
<!-- books-review:SF-2026-ARXIV-2603-12646:start -->
### 98$\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12646:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：固定 P90/P95 reservation 在流量稳定、类别近似同分布时简单而有效；当请求类别、GPU group、prefix reuse 与 output-length drift 同时变化时，单一 quantile 会把未来 KV 风险与 routing、queue 和 preemption 割裂。调度面应把 per-class reservation 写成 admission contract：由 preemption cost 与浪费 cost 决定 critical fractile，再在分布漂移下用 robust uncertainty set 联合求解 GPU configuration、routing、reservation 与 cache policy，并由 rolling telemetry 触发重估。<!-- existing:SF-2026-ARXIV-2603-12646:end -->

<!-- delta:SF-2026-ARXIV-2603-12646:start -->新证据差异：exact-v1 的 `IV System Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12646:end -->

边界：只支持 arXiv:2603.12646v1 §IV System Design 的机制与 §Evaluation 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12646:end -->
<!-- books-review:SF-2026-ARXIV-2603-12655:start -->
### VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12655:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-12655:end -->

<!-- delta:SF-2026-ARXIV-2603-12655:start -->新证据差异：exact-v1 的 `0.B.1 Model Architecture` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12655:end -->

边界：只支持 arXiv:2603.12655v1 §0.B.1 Model Architecture 的机制与 §0.B.2 Evaluation Datasets 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12655:end -->
<!-- books-review:SF-2026-ARXIV-2603-12671:start -->
### HyGra: Accelerating Network-State Simulation for LLM Training in DCNs via Adaptive Packet-Flow Granularity — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12671:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：**Trade-off、failure、共存与回退。** quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。<!-- existing:SF-2026-ARXIV-2603-12671:end -->

<!-- delta:SF-2026-ARXIV-2603-12671:start -->新证据差异：exact-v1 的 `V Architecture of Execution Layer` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12671:end -->

边界：只支持 arXiv:2603.12671v1 §V Architecture of Execution Layer 的机制与 §Evaluation 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12671:end -->
<!-- books-review:SF-2026-ARXIV-2603-12707:start -->
### Cost-Efficient Multimodal LLM Inference via Cross-Tier GPU Heterogeneity — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12707:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：为什么 LLM 推理调度不是简单的请求队列？调度器到底在调什么：请求、token、GPU、KV Cache，还是成本？为什么每一种加速技术最终都会改变调度器的状态空间？<!-- existing:SF-2026-ARXIV-2603-12707:end -->

<!-- delta:SF-2026-ARXIV-2603-12707:start -->新证据差异：exact-v1 的 `5 HeteroServe: System Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12707:end -->

边界：只支持 arXiv:2603.12707v1 §5 HeteroServe: System Design 的机制与 §6 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12707:end -->
<!-- books-review:SF-2026-ARXIV-2603-12823:start -->
### Adaptive Vision-Language Model Routing for Computer Use Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12823:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-12823:end -->

<!-- delta:SF-2026-ARXIV-2603-12823:start -->新证据差异：exact-v1 的 `Appendix E Cost Projection Methodology` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12823:end -->

边界：只支持 arXiv:2603.12823v1 §Appendix E Cost Projection Methodology 的机制与 §4 Evidence and Analysis 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12823:end -->
<!-- books-review:SF-2026-ARXIV-2603-12831:start -->
### Serving Hybrid LLM Loads with SLO Guarantees Using CPU-GPU Attention Piggybacking — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12831:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：联合优化可以在低带宽环境减少通信暴露，却把 host CPU memory、压缩/解压、dynamic-program cost、拓扑漂移和故障恢复带进 serving contract。高带宽同构集群、KV offload 反而更慢、压缩收益不足或 topology/SLO 无法准确建模时，固定 placement 与普通 pipeline 仍更可验证。论文结果只绑定其 internet-scale testbed、模型和公开配置，不证明通用去中心化服务优势。<!-- existing:SF-2026-ARXIV-2603-12831:end -->

<!-- delta:SF-2026-ARXIV-2603-12831:start -->新证据差异：论文让 CPU attention work 在 GPU request 间隙 piggyback，并由 SLO slack、阶段和资源占用决定是否卸载与何时回收。<!-- delta:SF-2026-ARXIV-2603-12831:end -->

边界：只支持 arXiv:2603.12831v1 §3.3.2–§3.3.6、§4 与 §5 的 A100/CPU testbed；§6 之外不外推 topology、model 或生产 SLO。写回已完成，等待非作者 post-write 复核。
<!-- books-review:SF-2026-ARXIV-2603-12831:end -->
<!-- books-review:SF-2026-ARXIV-2603-12933:start -->
### Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12933:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-12933:end -->

<!-- delta:SF-2026-ARXIV-2603-12933:start -->新证据差异：exact-v1 的 `III Methodology` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-12933:end -->

边界：只支持 arXiv:2603.12933v1 §III Methodology 的机制与 §IV-B Main Results 的公开 workload；§V Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12933:end -->
<!-- books-review:SF-2026-ARXIV-2603-12946:start -->
### Almost-Free Queue Jumping for Prior Inputs in Private Neural Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-12946:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-12946:end -->

<!-- delta:SF-2026-ARXIV-2603-12946:start -->新证据差异：PrivQJ 在 HE/MPC 处理中回收 slot，让高优先级输入 piggyback 到正在执行的 batch，而不重启共同计算。<!-- delta:SF-2026-ARXIV-2603-12946:end -->

边界：只支持 arXiv:2603.12946v1 §III-A Overview of PrivQJ 的机制与 §IV Evaluation 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-12946:end -->
<!-- books-review:SF-2026-ARXIV-2603-13017:start -->
### Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13017:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：只用最终 QA reward 训练 memory policy 成本低，也适合短链路、固定 schema 和容易人工检查的任务；但它不能回答某段中间 memory content 是否真正帮助了最终答案。一个实验性分支是固定 retrieval/answer interface，对 memory token 或 span 做 masking/counterfactual scoring，把对 answer score 的变化映射为 local process reward，再与 global outcome reward 合并。它把“这次答对了”推进为“哪些被写入的内容可能贡献了这次答案”，从而给 admission、update、compress 与 discard 更稠密的学习信号。<!-- existing:SF-2026-ARXIV-2603-13017:end -->

<!-- delta:SF-2026-ARXIV-2603-13017:start -->新证据差异：exact-v1 的 `4.3 Grading Methodology` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13017:end -->

边界：只支持 arXiv:2603.13017v1 §4.3 Grading Methodology 的机制与 §5.1 Main Results 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13017:end -->
<!-- books-review:SF-2026-ARXIV-2603-13019:start -->
### ARL-Tangram: Unleash the Resource Efficiency in Agentic Reinforcement Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13019:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条 路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体 数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是： **verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**<!-- existing:SF-2026-ARXIV-2603-13019:end -->

<!-- delta:SF-2026-ARXIV-2603-13019:start -->新证据差异：exact-v1 的 `3 Architecture` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13019:end -->

边界：只支持 arXiv:2603.13019v1 §3 Architecture 的机制与 §6 Evaluation 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13019:end -->
<!-- books-review:SF-2026-ARXIV-2603-13026:start -->
### PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13026:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：交互结束也不是 prompt injection 的自然终点。攻击内容一旦被写入 session context、长期 memory 或可复用 skill，可能在之后的良性 query 才触发；只做当前 response moderation 会把 dormant payload 当成已消失。持久状态因此必须在写入时保存 origin、trust/taint 与 policy generation，在每次读取或执行前按当前 principal、工具权限和目的重新验证，过期或来源不明时 quarantine、降权或删除。<!-- existing:SF-2026-ARXIV-2603-13026:end -->

<!-- delta:SF-2026-ARXIV-2603-13026:start -->新证据差异：exact-v1 的 `3.3 Design of PISmith` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13026:end -->

边界：只支持 arXiv:2603.13026v1 §3.3 Design of PISmith 的机制与 §Appendix E Full Results for Utility–Robustness Evaluation (RQ2) 的公开 workload；§4.5 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13026:end -->
<!-- books-review:SF-2026-ARXIV-2603-13033:start -->
### ESPIRE: A Diagnostic Benchmark for Embodied Spatial Reasoning of Vision-Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13033:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-13033:end -->

<!-- delta:SF-2026-ARXIV-2603-13033:start -->新证据差异：exact-v1 的 `Algorithms.` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13033:end -->

边界：只支持 arXiv:2603.13033v1 §Algorithms. 的机制与 §5.2 Main Results 的公开 workload；§6 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13033:end -->
<!-- books-review:SF-2026-ARXIV-2603-13099:start -->
### Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13099:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-13099:end -->

<!-- delta:SF-2026-ARXIV-2603-13099:start -->新证据差异：exact-v1 的 `S6.1 GRPO Framework` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13099:end -->

边界：只支持 arXiv:2603.13099v1 §S6.1 GRPO Framework 的机制与 §4.2 Main Results 的公开 workload；§4.4 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13099:end -->
<!-- books-review:SF-2026-ARXIV-2603-13110:start -->
### AgentRM: An OS-Inspired Resource Manager for LLM Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13110:start -->已读 owner `books/part-07-agent/84-agent-platform.md` 与相邻章节。现有命题：Agent Platform 跨 run 管理 execution lanes、provider rate limits、Context 生命周期与资源公平；Workflow 仍拥有业务 DAG 和副作用真值。<!-- existing:SF-2026-ARXIV-2603-13110:end -->

<!-- delta:SF-2026-ARXIV-2603-13110:start -->新证据差异：AgentRM 以 MLFQ、zombie reaper、rate-limit admission、DRF-inspired fairness、Context Lifecycle Manager 与 resource monitor 形成平台资源控制面。<!-- delta:SF-2026-ARXIV-2603-13110:end -->

边界：只支持 arXiv:2603.13110v1 §IV middleware 与 §VI simulated workloads；§VII-C 之外不证明 production fairness、durable commit、versioned lease 或 recovery。已重路由 Ch84 并等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-13110:end -->
<!-- books-review:SF-2026-ARXIV-2603-13176:start -->
### Perceive What Matters: Relevance-Driven Scheduling for Multimodal Streaming Perception — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13176:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-13176:end -->

<!-- delta:SF-2026-ARXIV-2603-13176:start -->新证据差异：exact-v1 的 `III Perception Scheduling Framework` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13176:end -->

边界：只支持 arXiv:2603.13176v1 §III Perception Scheduling Framework 的机制与 §V-C Perception Module Selector Evaluation 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13176:end -->
<!-- books-review:SF-2026-ARXIV-2603-13189:start -->
### LLM Constitutional Multi-Agent Governance — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13189:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-13189:end -->

<!-- delta:SF-2026-ARXIV-2603-13189:start -->新证据差异：exact-v1 的 `3 Methodology` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13189:end -->

边界：只支持 arXiv:2603.13189v1 §3 Methodology 的机制与 §4.1 Multi-Seed Replication and Statistical Validation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13189:end -->
<!-- books-review:SF-2026-ARXIV-2603-13215:start -->
### Out of Sight, Out of Mind? Evaluating State Evolution in Video World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-13215:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-13215:end -->

<!-- delta:SF-2026-ARXIV-2603-13215:start -->新证据差异：exact-v1 的 `3 Benchmarking State Evolution in Video World Models` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-13215:end -->

边界：只支持 arXiv:2603.13215v1 §3 Benchmarking State Evolution in Video World Models 的机制与 §3.2 Evaluation Criteria and Automatic Verifiers 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-13215:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260316-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260316 | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260316-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-12277; review:SF-2026-ARXIV-2603-12396; review:SF-2026-ARXIV-2603-12440; review:SF-2026-ARXIV-2603-12465; review:SF-2026-ARXIV-2603-12485; review:SF-2026-ARXIV-2603-12510; review:SF-2026-ARXIV-2603-12553; review:SF-2026-ARXIV-2603-12598; review:SF-2026-ARXIV-2603-12614; review:SF-2026-ARXIV-2603-12617; review:SF-2026-ARXIV-2603-12621; review:SF-2026-ARXIV-2603-12631; review:SF-2026-ARXIV-2603-12639; review:SF-2026-ARXIV-2603-12646; review:SF-2026-ARXIV-2603-12655; review:SF-2026-ARXIV-2603-12671; review:SF-2026-ARXIV-2603-12707; review:SF-2026-ARXIV-2603-12823; review:SF-2026-ARXIV-2603-12831; review:SF-2026-ARXIV-2603-12933; review:SF-2026-ARXIV-2603-12946; review:SF-2026-ARXIV-2603-13017; review:SF-2026-ARXIV-2603-13019; review:SF-2026-ARXIV-2603-13026; review:SF-2026-ARXIV-2603-13033; review:SF-2026-ARXIV-2603-13099; review:SF-2026-ARXIV-2603-13110; review:SF-2026-ARXIV-2603-13176; review:SF-2026-ARXIV-2603-13189; review:SF-2026-ARXIV-2603-13215 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260316-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260316-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260316/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
- 更新并复核 `books/part-07-agent/84-agent-platform.md`。
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
