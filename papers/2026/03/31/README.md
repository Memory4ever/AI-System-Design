# Daily Research — 2026-03-31

**Research Date:** 2026-03-31

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-30 09:00:00 ～ 2026-03-31 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=1102/1102/1102；denominator=28、pre-denominator closures=1074。exact-v1 Review complete=28、blocked=0；Integrate 建议=8。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-31 |
| Window End | 2026-03-31 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260331-AUTHOR-28 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-30T09:00:00+08:00 | 2026-03-31T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 1102/1102 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 1102 | SF-2026-ARXIV-2603-26728;SF-2026-ARXIV-2603-26942;SF-2026-ARXIV-2603-26993;SF-2026-ARXIV-2603-27116;SF-2026-ARXIV-2603-27138;SF-2026-ARXIV-2603-27204;SF-2026-ARXIV-2603-27287;SF-2026-ARXIV-2603-27299;SF-2026-ARXIV-2603-27355;SF-2026-ARXIV-2603-27467;SF-2026-ARXIV-2603-27517;SF-2026-ARXIV-2603-27624;SF-2026-ARXIV-2603-27819;SF-2026-ARXIV-2603-27905;SF-2026-ARXIV-2603-28005;SF-2026-ARXIV-2603-28013;SF-2026-ARXIV-2603-28063;SF-2026-ARXIV-2603-28101;SF-2026-ARXIV-2603-28166;SF-2026-ARXIV-2603-28168;SF-2026-ARXIV-2603-28239;SF-2026-ARXIV-2603-28342;SF-2026-ARXIV-2603-28345;SF-2026-ARXIV-2603-28507;SF-2026-ARXIV-2603-28565;SF-2026-ARXIV-2603-28590;SF-2026-ARXIV-2603-28622;SF-2026-ARXIV-2603-28650 | pages=100; prefixes=00..99; final_cursor=end; registered=1102; screened=1102; retained=28; closure=1074 | 2026-03-31T01:00:00+00:00 | screening-ledger-final.json#sha256=cf9396dafbbea945d69ae8198ff374bb7c0666f3cece1e5be24d115420c0b959; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260331:start -->作者侧已逐项筛选全部 1102 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260331:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 1102/1102 条 title+abstract：作者 retained 16 项均保留，12 个 false-negative family 已完成 exact-v1 Source Review，22 个 recall challenge 被逐项驳回，1 个 withdrawn 只保留 identity/status；reconciled denominator 为 28；Books queue 中 5 个 `Integrate` 被降为 `No Change — Existing Coverage`，1 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260331/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26728 | arXiv:2603.26728v1 | paper-v1:2603.26728 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-26728 | self | — | new_in_window | PLATFORM-GATEWAY | Integrate | books-review:SF-2026-ARXIV-2603-26728 | no |
| SF-2026-ARXIV-2603-26942 | arXiv:2603.26942v1 | paper-v1:2603.26942 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-26942 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26942 | no |
| SF-2026-ARXIV-2603-26993 | arXiv:2603.26993v1 | paper-v1:2603.26993 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-26993 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2603-26993 | no |
| SF-2026-ARXIV-2603-27116 | arXiv:2603.27116v1 | paper-v1:2603.27116 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-27116 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2603-27116 | no |
| SF-2026-ARXIV-2603-27138 | arXiv:2603.27138v1 | paper-v1:2603.27138 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-27138 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2603-27138 | no |
| SF-2026-ARXIV-2603-27204 | arXiv:2603.27204v1 | paper-v1:2603.27204 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27204 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27204 | no |
| SF-2026-ARXIV-2603-27287 | arXiv:2603.27287v1 | paper-v1:2603.27287 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27287 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27287 | no |
| SF-2026-ARXIV-2603-27299 | arXiv:2603.27299v1 | paper-v1:2603.27299 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27299 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27299 | no |
| SF-2026-ARXIV-2603-27355 | arXiv:2603.27355v1 | paper-v1:2603.27355 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27355 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27355 | no |
| SF-2026-ARXIV-2603-27467 | arXiv:2603.27467v1 | paper-v1:2603.27467 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27467 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27467 | no |
| SF-2026-ARXIV-2603-27517 | arXiv:2603.27517v1 | paper-v1:2603.27517 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27517 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27517 | no |
| SF-2026-ARXIV-2603-27624 | arXiv:2603.27624v1 | paper-v1:2603.27624 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-27624 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-27624 | no |
| SF-2026-ARXIV-2603-27819 | arXiv:2603.27819v1 | paper-v1:2603.27819 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-27819 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2603-27819 | no |
| SF-2026-ARXIV-2603-27905 | arXiv:2603.27905v1 | paper-v1:2603.27905 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-27905 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27905 | no |
| SF-2026-ARXIV-2603-28005 | arXiv:2603.28005v1 | paper-v1:2603.28005 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28005 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28005 | no |
| SF-2026-ARXIV-2603-28013 | arXiv:2603.28013v1 | paper-v1:2603.28013 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28013 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28013 | no |
| SF-2026-ARXIV-2603-28063 | arXiv:2603.28063v1 | paper-v1:2603.28063 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28063 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28063 | no |
| SF-2026-ARXIV-2603-28101 | arXiv:2603.28101v1 | paper-v1:2603.28101 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-28101 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2603-28101 | no |
| SF-2026-ARXIV-2603-28166 | arXiv:2603.28166v1 | paper-v1:2603.28166 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28166 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28166 | no |
| SF-2026-ARXIV-2603-28168 | arXiv:2603.28168v1 | paper-v1:2603.28168 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28168 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28168 | no |
| SF-2026-ARXIV-2603-28239 | arXiv:2603.28239v1 | paper-v1:2603.28239 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-28239 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-28239 | no |
| SF-2026-ARXIV-2603-28342 | arXiv:2603.28342v1 | paper-v1:2603.28342 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28342 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28342 | no |
| SF-2026-ARXIV-2603-28345 | arXiv:2603.28345v1 | paper-v1:2603.28345 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28345 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28345 | no |
| SF-2026-ARXIV-2603-28507 | arXiv:2603.28507v1 | paper-v1:2603.28507 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28507 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28507 | no |
| SF-2026-ARXIV-2603-28565 | arXiv:2603.28565v1 | paper-v1:2603.28565 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28565 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28565 | no |
| SF-2026-ARXIV-2603-28590 | arXiv:2603.28590v1 | paper-v1:2603.28590 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28590 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28590 | no |
| SF-2026-ARXIV-2603-28622 | arXiv:2603.28622v1 | paper-v1:2603.28622 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28622 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28622 | no |
| SF-2026-ARXIV-2603-28650 | arXiv:2603.28650v1 | paper-v1:2603.28650 | 2026-W14 | 2026-03-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-28650 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28650 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26728 | RP-5ca0713d1ac68fc0 | deep | arXiv:2603.26728v1 | SRC-ARXIV@arXiv:2603.26728v1 | HTML — §3. The SEAR Framework [facet=method]; https://arxiv.org/html/2603.26728v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26728v1.html; sha256:e45779a637f0881501b2aabb8cd44413185518ba1e84f19feedda3b0f22448b6 | HTML — §6.2. Evaluation Performance and §6.3. Routing Performance [facet=evaluation]; https://arxiv.org/html/2603.26728v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26728v1.html; sha256:e45779a637f0881501b2aabb8cd44413185518ba1e84f19feedda3b0f22448b6 | HTML — §8. Future Work [facet=limitations]; https://arxiv.org/html/2603.26728v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26728v1.html; sha256:e45779a637f0881501b2aabb8cd44413185518ba1e84f19feedda3b0f22448b6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26728v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26728 | complete |
| SF-2026-ARXIV-2603-26942 | RP-bc24235990423752 | standard | arXiv:2603.26942v1 | SRC-ARXIV@arXiv:2603.26942v1 | HTML — §3.1. Experimental Setup [facet=method]; https://arxiv.org/html/2603.26942v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26942v1.html; sha256:9c4125f62825f8813f42c9d2eaab1b3ab22c1caadfe3466a262a1c6f21954e85 | HTML — §3.2.2. Finding 2: The Observability Gap. [facet=evaluation]; https://arxiv.org/html/2603.26942v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26942v1.html; sha256:9c4125f62825f8813f42c9d2eaab1b3ab22c1caadfe3466a262a1c6f21954e85 | HTML — §4. Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.26942v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26942v1.html; sha256:9c4125f62825f8813f42c9d2eaab1b3ab22c1caadfe3466a262a1c6f21954e85 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26942v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26942 | complete |
| SF-2026-ARXIV-2603-26993 | RP-bfb3f78b75ab8885 | deep | arXiv:2603.26993v1 | SRC-ARXIV@arXiv:2603.26993v1 | HTML — §2 Delegated Decision Model [facet=method]; https://arxiv.org/html/2603.26993v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26993v1.html; sha256:0b86c9759b64ef9de47a37438e3649255153be62e71c82ca77fecf3c7866e2d4 | HTML — §7 Numerical Experiments [facet=evaluation]; https://arxiv.org/html/2603.26993v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26993v1.html; sha256:0b86c9759b64ef9de47a37438e3649255153be62e71c82ca77fecf3c7866e2d4 | HTML — §4 Proposition 6 and Theorem 7 [facet=scope-boundary]; https://arxiv.org/html/2603.26993v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26993v1.html; sha256:0b86c9759b64ef9de47a37438e3649255153be62e71c82ca77fecf3c7866e2d4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.26993v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-26993 | complete |
| SF-2026-ARXIV-2603-27116 | RP-257ef204dac3ada2 | deep | arXiv:2603.27116v1 | SRC-ARXIV@arXiv:2603.27116v1 | HTML — §Mathematical framework: the no-escape theorem [facet=method]; https://arxiv.org/html/2603.27116v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27116v1.html; sha256:82aba70430ed24751f308a1ee668e7799d00e10e52007ba3bee1bd561b61fe5e | HTML — §Forgetting experiments [facet=evaluation]; https://arxiv.org/html/2603.27116v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27116v1.html; sha256:82aba70430ed24751f308a1ee668e7799d00e10e52007ba3bee1bd561b61fe5e | HTML — §Discussion [facet=limitations]; https://arxiv.org/html/2603.27116v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27116v1.html; sha256:82aba70430ed24751f308a1ee668e7799d00e10e52007ba3bee1bd561b61fe5e | arXiv exact-v1 identity https://arxiv.org/abs/2603.27116v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27116 | complete |
| SF-2026-ARXIV-2603-27138 | RP-1650029ea7e55e72 | deep | arXiv:2603.27138v1 | SRC-ARXIV@arXiv:2603.27138v1 | HTML — §3.2–§3.4 CPU-based attention estimation, asynchronous prefetch and pipeline integration [facet=method]; https://arxiv.org/html/2603.27138v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27138v1.html; sha256:f53eaf4dda068dc4f3020903103cd79dee2141daaae1f6bbbd061fa6fbdf6058 | HTML — §4.3. Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.27138v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27138v1.html; sha256:f53eaf4dda068dc4f3020903103cd79dee2141daaae1f6bbbd061fa6fbdf6058 | HTML — §5. Conclusion [facet=limitations]; https://arxiv.org/html/2603.27138v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27138v1.html; sha256:f53eaf4dda068dc4f3020903103cd79dee2141daaae1f6bbbd061fa6fbdf6058 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27138v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27138 | complete |
| SF-2026-ARXIV-2603-27204 | RP-4f5351f8de330e73 | standard | arXiv:2603.27204v1 | SRC-ARXIV@arXiv:2603.27204v1 | HTML — §4. Methodology [facet=method]; https://arxiv.org/html/2603.27204v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27204v1.html; sha256:322df4ae7340ff998bfbe90c67c64e6f5c110c284b2fb8eee25707de2d0985d7 | HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.27204v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27204v1.html; sha256:322df4ae7340ff998bfbe90c67c64e6f5c110c284b2fb8eee25707de2d0985d7 | HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.27204v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27204v1.html; sha256:322df4ae7340ff998bfbe90c67c64e6f5c110c284b2fb8eee25707de2d0985d7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27204v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27204 | complete |
| SF-2026-ARXIV-2603-27287 | RP-36cc39dc1954682d | standard | arXiv:2603.27287v1 | SRC-ARXIV@arXiv:2603.27287v1 | HTML — §3 Methods [facet=method]; https://arxiv.org/html/2603.27287v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27287v1.html; sha256:7cbf9225bf4bc9e3e02f0d60093197f93b2b947a9e1ffe1b506c9bec7706e6a5 | HTML — §4.1 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.27287v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27287v1.html; sha256:7cbf9225bf4bc9e3e02f0d60093197f93b2b947a9e1ffe1b506c9bec7706e6a5 | HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.27287v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27287v1.html; sha256:7cbf9225bf4bc9e3e02f0d60093197f93b2b947a9e1ffe1b506c9bec7706e6a5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27287v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27287 | complete |
| SF-2026-ARXIV-2603-27299 | RP-08d0fbc01a6346cb | standard | arXiv:2603.27299v1 | SRC-ARXIV@arXiv:2603.27299v1 | HTML — §3.1 Compilation Architecture [facet=method]; https://arxiv.org/html/2603.27299v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27299v1.html; sha256:94c6ea669f265287d15d81616802fcfba08afa16b70e87bfe71a2d3c2fcb1568 | HTML — §A.3 Generated: LangGraph Decision Node (Strategy A) [facet=evaluation]; https://arxiv.org/html/2603.27299v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27299v1.html; sha256:94c6ea669f265287d15d81616802fcfba08afa16b70e87bfe71a2d3c2fcb1568 | HTML — §7.1 Limitations [facet=limitations]; https://arxiv.org/html/2603.27299v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27299v1.html; sha256:94c6ea669f265287d15d81616802fcfba08afa16b70e87bfe71a2d3c2fcb1568 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27299v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27299 | complete |
| SF-2026-ARXIV-2603-27355 | RP-bce462f1d4d4a624 | standard | arXiv:2603.27355v1 | SRC-ARXIV@arXiv:2603.27355v1 | HTML — §2 System Overview [facet=method]; https://arxiv.org/html/2603.27355v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27355v1.html; sha256:566ea9e917527b6870c3da3ca75917ed0e76e39b5cfa11e0be820402b9d35650 | HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.27355v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27355v1.html; sha256:566ea9e917527b6870c3da3ca75917ed0e76e39b5cfa11e0be820402b9d35650 | HTML — §8 Limitations and Threats to Validity [facet=limitations]; https://arxiv.org/html/2603.27355v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27355v1.html; sha256:566ea9e917527b6870c3da3ca75917ed0e76e39b5cfa11e0be820402b9d35650 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27355v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27355 | complete |
| SF-2026-ARXIV-2603-27467 | RP-78dbac734e9127fe | standard | arXiv:2603.27467v1 | SRC-ARXIV@arXiv:2603.27467v1 | HTML — §3.1 Angular Quantization [facet=method]; https://arxiv.org/html/2603.27467v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27467v1.html; sha256:cfee62c0d25b6bc44d6f6d0df84787f867ed99accbb2005544871bd10dfb896e | HTML — §4.7 Competitive Comparison [facet=evaluation]; https://arxiv.org/html/2603.27467v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27467v1.html; sha256:cfee62c0d25b6bc44d6f6d0df84787f867ed99accbb2005544871bd10dfb896e | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.27467v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27467v1.html; sha256:cfee62c0d25b6bc44d6f6d0df84787f867ed99accbb2005544871bd10dfb896e | arXiv exact-v1 identity https://arxiv.org/abs/2603.27467v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27467 | complete |
| SF-2026-ARXIV-2603-27517 | RP-22e6bd44a5f63da1 | standard | arXiv:2603.27517v1 | SRC-ARXIV@arXiv:2603.27517v1 | HTML — §4 Security Taxonomy [facet=method]; https://arxiv.org/html/2603.27517v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27517v1.html; sha256:639fe9ecdf3eaca9d8788361d40a3bb9f2bca2aadfd9c7d4355f055a8c0da21e | HTML — §3 Corpus Overview [facet=evaluation]; https://arxiv.org/html/2603.27517v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27517v1.html; sha256:639fe9ecdf3eaca9d8788361d40a3bb9f2bca2aadfd9c7d4355f055a8c0da21e | HTML — §6 Defense Discussion [facet=limitations]; https://arxiv.org/html/2603.27517v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27517v1.html; sha256:639fe9ecdf3eaca9d8788361d40a3bb9f2bca2aadfd9c7d4355f055a8c0da21e | arXiv exact-v1 identity https://arxiv.org/abs/2603.27517v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27517 | complete |
| SF-2026-ARXIV-2603-27624 | RP-a15f33332a907a36 | deep | arXiv:2603.27624v1 | SRC-ARXIV@arXiv:2603.27624v1 | HTML — §IV FSE-DP with Micro-Slice Flow + §V MoE Scheduler [facet=method]; https://arxiv.org/html/2603.27624v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27624v1.html; sha256:8044b905d9dfa3b7204fef979255be015d46705b078637e682465583bb56c50e | HTML — §VI-C End-to-End Evaluation with Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.27624v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27624v1.html; sha256:8044b905d9dfa3b7204fef979255be015d46705b078637e682465583bb56c50e | HTML — §VII Conclusion [facet=limitations]; https://arxiv.org/html/2603.27624v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27624v1.html; sha256:8044b905d9dfa3b7204fef979255be015d46705b078637e682465583bb56c50e | arXiv exact-v1 identity https://arxiv.org/abs/2603.27624v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27624 | complete |
| SF-2026-ARXIV-2603-27819 | RP-099c51721e5565b0 | deep | arXiv:2603.27819v1 | SRC-ARXIV@arXiv:2603.27819v1 | HTML — §3.2 Loss Function [facet=method]; https://arxiv.org/html/2603.27819v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27819v1.html; sha256:a8d981fbdd44b29ee3b9388c5c504e5190368b1805928e462d8245b7619c3367 | HTML — §5.1 Main Results: Distillation vs. Eviction [facet=evaluation]; https://arxiv.org/html/2603.27819v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27819v1.html; sha256:a8d981fbdd44b29ee3b9388c5c504e5190368b1805928e462d8245b7619c3367 | HTML — §6 Analysis: Limits of Per-Layer Optimization [facet=limitations]; https://arxiv.org/html/2603.27819v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27819v1.html; sha256:a8d981fbdd44b29ee3b9388c5c504e5190368b1805928e462d8245b7619c3367 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27819v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27819 | complete |
| SF-2026-ARXIV-2603-27905 | RP-a968f322fe15ec5f | standard | arXiv:2603.27905v1 | SRC-ARXIV@arXiv:2603.27905v1 | HTML — §3.9 Implementation [facet=method]; https://arxiv.org/html/2603.27905v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27905v1.html; sha256:abb1754a4b2be29c93e4277660d622af2f357861c122b02bfe7de10237ea4271 | HTML — §Relation to Post-hoc Validation and Repair. [facet=evaluation]; https://arxiv.org/html/2603.27905v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27905v1.html; sha256:abb1754a4b2be29c93e4277660d622af2f357861c122b02bfe7de10237ea4271 | HTML — §Limitations of Drift Detection. [facet=limitations]; https://arxiv.org/html/2603.27905v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27905v1.html; sha256:abb1754a4b2be29c93e4277660d622af2f357861c122b02bfe7de10237ea4271 | arXiv exact-v1 identity https://arxiv.org/abs/2603.27905v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-27905 | complete |
| SF-2026-ARXIV-2603-28005 | RP-59cb30f8a9cb31fa | standard | arXiv:2603.28005v1 | SRC-ARXIV@arXiv:2603.28005v1 | HTML — §3.1 Judge designs [facet=method]; https://arxiv.org/html/2603.28005v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28005v1.html; sha256:6f94ed98c43b761f6dfd1c068495e2df8d8110532e152484d4134b4f5a8c7b38 | HTML — §A Matched Holistic Rubric Rivals Self-Decomposing Atomic Judges for Benchmark-Style Reference-Support Classification [facet=evaluation]; https://arxiv.org/html/2603.28005v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28005v1.html; sha256:6f94ed98c43b761f6dfd1c068495e2df8d8110532e152484d4134b4f5a8c7b38 | HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.28005v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28005v1.html; sha256:6f94ed98c43b761f6dfd1c068495e2df8d8110532e152484d4134b4f5a8c7b38 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28005v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28005 | complete |
| SF-2026-ARXIV-2603-28013 | RP-d59e1df2a8b3c34b | standard | arXiv:2603.28013v1 | SRC-ARXIV@arXiv:2603.28013v1 | HTML — §3.2 Kill-Chain Stages and Attack Scenarios [facet=method]; https://arxiv.org/html/2603.28013v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28013v1.html; sha256:de58184a1b182e4ab5fd9d6faa1a6dae70e3c4d242a94771b5bd039ed407777b | HTML — §4.1 Exposure Is Universal; Defense Is Downstream [facet=evaluation]; https://arxiv.org/html/2603.28013v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28013v1.html; sha256:de58184a1b182e4ab5fd9d6faa1a6dae70e3c4d242a94771b5bd039ed407777b | HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.28013v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28013v1.html; sha256:de58184a1b182e4ab5fd9d6faa1a6dae70e3c4d242a94771b5bd039ed407777b | arXiv exact-v1 identity https://arxiv.org/abs/2603.28013v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28013 | complete |
| SF-2026-ARXIV-2603-28063 | RP-6fc0befca189d1f7 | standard | arXiv:2603.28063v1 | SRC-ARXIV@arXiv:2603.28063v1 | HTML — §7.1 What This Framework Provides [facet=method]; https://arxiv.org/html/2603.28063v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28063v1.html; sha256:c9d819fe17c108947432f6b76705621e89876aebae07bf39712d7a12fdb2182c | HTML — §6.2 Capability-Dependent Evaluation Fidelity [facet=evaluation]; https://arxiv.org/html/2603.28063v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28063v1.html; sha256:c9d819fe17c108947432f6b76705621e89876aebae07bf39712d7a12fdb2182c | HTML — §5.5 Conditions for Model Failure [facet=limitations]; https://arxiv.org/html/2603.28063v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28063v1.html; sha256:c9d819fe17c108947432f6b76705621e89876aebae07bf39712d7a12fdb2182c | arXiv exact-v1 identity https://arxiv.org/abs/2603.28063v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28063 | complete |
| SF-2026-ARXIV-2603-28101 | RP-ac8029c1b154050b | deep | arXiv:2603.28101v1 | SRC-ARXIV@arXiv:2603.28101v1 | HTML — §4 Trajectory-level Scheduler [facet=method]; https://arxiv.org/html/2603.28101v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28101v1.html; sha256:6db6453b7511dc4fea5543a5351ad8424d1003ad2fce9b2a1927946c83a5d04f | HTML — §7.1 Overall Performance [facet=evaluation]; https://arxiv.org/html/2603.28101v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28101v1.html; sha256:6db6453b7511dc4fea5543a5351ad8424d1003ad2fce9b2a1927946c83a5d04f | HTML — §8 Discussion [facet=limitations]; https://arxiv.org/html/2603.28101v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28101v1.html; sha256:6db6453b7511dc4fea5543a5351ad8424d1003ad2fce9b2a1927946c83a5d04f | arXiv exact-v1 identity https://arxiv.org/abs/2603.28101v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28101 | complete |
| SF-2026-ARXIV-2603-28166 | RP-a90654abb12a6beb | standard | arXiv:2603.28166v1 | SRC-ARXIV@arXiv:2603.28166v1 | HTML — §2. Method [facet=method]; https://arxiv.org/html/2603.28166v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28166v1.html; sha256:f7b71ff51add384dcc77cc577f980c52a6e289d6badd128881dd4a2820f455de | HTML — §3.3. LLM Security Evaluation [facet=evaluation]; https://arxiv.org/html/2603.28166v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28166v1.html; sha256:f7b71ff51add384dcc77cc577f980c52a6e289d6badd128881dd4a2820f455de | HTML — §4. Discussion [facet=limitations]; https://arxiv.org/html/2603.28166v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28166v1.html; sha256:f7b71ff51add384dcc77cc577f980c52a6e289d6badd128881dd4a2820f455de | arXiv exact-v1 identity https://arxiv.org/abs/2603.28166v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28166 | complete |
| SF-2026-ARXIV-2603-28168 | RP-601af900229d7a23 | standard | arXiv:2603.28168v1 | SRC-ARXIV@arXiv:2603.28168v1 | HTML — §III-C How to design intra-Pod architecture [facet=method]; https://arxiv.org/html/2603.28168v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28168v1.html; sha256:3210fff764f92720d53efb81b80e788a9adab83ff1d24952f66eb9c7ce6395cc | HTML — §IV-B Performance Analysis [facet=evaluation]; https://arxiv.org/html/2603.28168v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28168v1.html; sha256:3210fff764f92720d53efb81b80e788a9adab83ff1d24952f66eb9c7ce6395cc | HTML — §VI Discussion [facet=limitations]; https://arxiv.org/html/2603.28168v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28168v1.html; sha256:3210fff764f92720d53efb81b80e788a9adab83ff1d24952f66eb9c7ce6395cc | arXiv exact-v1 identity https://arxiv.org/abs/2603.28168v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28168 | complete |
| SF-2026-ARXIV-2603-28239 | RP-0deee1f0a4a54987 | deep | arXiv:2603.28239v1 | SRC-ARXIV@arXiv:2603.28239v1 | HTML — §3. Design and Implementation [facet=method]; https://arxiv.org/html/2603.28239v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28239v1.html; sha256:a8e52b8bf9827e08f6ee558d6b03a645c32facfd8b99f951acd3717b17ed123c | HTML — §4.5. LLM TP Inference [facet=evaluation]; https://arxiv.org/html/2603.28239v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28239v1.html; sha256:a8e52b8bf9827e08f6ee558d6b03a645c32facfd8b99f951acd3717b17ed123c | HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.28239v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28239v1.html; sha256:a8e52b8bf9827e08f6ee558d6b03a645c32facfd8b99f951acd3717b17ed123c | arXiv exact-v1 identity https://arxiv.org/abs/2603.28239v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28239 | complete |
| SF-2026-ARXIV-2603-28342 | RP-b51ad4e6c6d49fa5 | standard | arXiv:2603.28342v1 | SRC-ARXIV@arXiv:2603.28342v1 | HTML — §2.3 Advanced Search and Evolution Algorithms [facet=method]; https://arxiv.org/html/2603.28342v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28342v1.html; sha256:71dabc1c9dbb65ebb64f473f2f54031aa381e6ecfa7247844bbb34dffffad2a6 | HTML — §3.3 Evaluation Backends [facet=evaluation]; https://arxiv.org/html/2603.28342v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28342v1.html; sha256:71dabc1c9dbb65ebb64f473f2f54031aa381e6ecfa7247844bbb34dffffad2a6 | HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.28342v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28342v1.html; sha256:71dabc1c9dbb65ebb64f473f2f54031aa381e6ecfa7247844bbb34dffffad2a6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28342v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28342 | complete |
| SF-2026-ARXIV-2603-28345 | RP-fd14ddbd5afa8730 | standard | arXiv:2603.28345v1 | SRC-ARXIV@arXiv:2603.28345v1 | HTML — §4.2.2. Method Comparison [facet=method]; https://arxiv.org/html/2603.28345v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28345v1.html; sha256:224c96638605c03309909517fb5d74bbb0311828c0f6ff424e9797092a1a41d5 | HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.28345v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28345v1.html; sha256:224c96638605c03309909517fb5d74bbb0311828c0f6ff424e9797092a1a41d5 | HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.28345v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28345v1.html; sha256:224c96638605c03309909517fb5d74bbb0311828c0f6ff424e9797092a1a41d5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28345v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28345 | complete |
| SF-2026-ARXIV-2603-28507 | RP-cac78529475a3c39 | standard | arXiv:2603.28507v1 | SRC-ARXIV@arXiv:2603.28507v1 | HTML — §4 A Time-Indexed Efficiency-Doubling Extension [facet=method]; https://arxiv.org/html/2603.28507v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28507v1.html; sha256:19d95beb5b41e821c142d2ea6e86a20172b7c3b7d5b19f51b55f8e9c75a28bcb | HTML — §5 The Operational Meaning of Diminishing Returns [facet=evaluation]; https://arxiv.org/html/2603.28507v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28507v1.html; sha256:19d95beb5b41e821c142d2ea6e86a20172b7c3b7d5b19f51b55f8e9c75a28bcb | HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.28507v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28507v1.html; sha256:19d95beb5b41e821c142d2ea6e86a20172b7c3b7d5b19f51b55f8e9c75a28bcb | arXiv exact-v1 identity https://arxiv.org/abs/2603.28507v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28507 | complete |
| SF-2026-ARXIV-2603-28565 | RP-8091330d029bd6a3 | standard | arXiv:2603.28565v1 | SRC-ARXIV@arXiv:2603.28565v1 | HTML — §4.1 State-based Modeling of Action Flow Matching [facet=method]; https://arxiv.org/html/2603.28565v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28565v1.html; sha256:01e94cd7760c5754ba517db1d330f4ecea288fbce15eb5deead177d7a3df05c1 | HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.28565v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28565v1.html; sha256:01e94cd7760c5754ba517db1d330f4ecea288fbce15eb5deead177d7a3df05c1 | HTML — §7 Conclusions [facet=limitations]; https://arxiv.org/html/2603.28565v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28565v1.html; sha256:01e94cd7760c5754ba517db1d330f4ecea288fbce15eb5deead177d7a3df05c1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28565v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28565 | complete |
| SF-2026-ARXIV-2603-28590 | RP-b88ec2863f6b5212 | standard | arXiv:2603.28590v1 | SRC-ARXIV@arXiv:2603.28590v1 | HTML — §3.1 Evaluation Design [facet=method]; https://arxiv.org/html/2603.28590v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28590v1.html; sha256:98b2973d8f1d2625800744ee3ab60ee791b064d3f2724ed56342b3080acc4178 | HTML — §3.3 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.28590v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28590v1.html; sha256:98b2973d8f1d2625800744ee3ab60ee791b064d3f2724ed56342b3080acc4178 | HTML — §4.3 Mechanisms of Failure and Evasion in Monitoring (RQ3) [facet=limitations]; https://arxiv.org/html/2603.28590v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28590v1.html; sha256:98b2973d8f1d2625800744ee3ab60ee791b064d3f2724ed56342b3080acc4178 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28590v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28590 | complete |
| SF-2026-ARXIV-2603-28622 | RP-27bbfcc0497cec90 | standard | arXiv:2603.28622v1 | SRC-ARXIV@arXiv:2603.28622v1 | HTML — §IV G-TRAC Design and Algorithm [facet=method]; https://arxiv.org/html/2603.28622v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28622v1.html; sha256:fa3f72e9e68357b3bcc9d5c9fdfbe7c9b8ed11f82c28deae8aaa39e0d7fe3623 | HTML — §IV-D Complexity Analysis [facet=evaluation]; https://arxiv.org/html/2603.28622v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28622v1.html; sha256:fa3f72e9e68357b3bcc9d5c9fdfbe7c9b8ed11f82c28deae8aaa39e0d7fe3623 | HTML — §VII Conclusion [facet=limitations]; https://arxiv.org/html/2603.28622v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28622v1.html; sha256:fa3f72e9e68357b3bcc9d5c9fdfbe7c9b8ed11f82c28deae8aaa39e0d7fe3623 | arXiv exact-v1 identity https://arxiv.org/abs/2603.28622v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28622 | complete |
| SF-2026-ARXIV-2603-28650 | RP-13ba0412782a3ea9 | standard | arXiv:2603.28650v1 | SRC-ARXIV@arXiv:2603.28650v1 | HTML — §4.2 Construction: Lipschitz Ball Verifier [facet=method]; https://arxiv.org/html/2603.28650v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28650v1.html; sha256:8f7b79d227df5121cd1e1744c1daf12fa9d597c0b88a2f89df519b3ecc96321e | HTML — §7.1 LLM-Scale Mechanism Validation: GPT-2 with LoRA [facet=evaluation]; https://arxiv.org/html/2603.28650v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28650v1.html; sha256:8f7b79d227df5121cd1e1744c1daf12fa9d597c0b88a2f89df519b3ecc96321e | HTML — §9 Conclusion [facet=limitations]; https://arxiv.org/html/2603.28650v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28650v1.html; sha256:8f7b79d227df5121cd1e1744c1daf12fa9d597c0b88a2f89df519b3ecc96321e | arXiv exact-v1 identity https://arxiv.org/abs/2603.28650v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-28650 | complete |

### Source Reviews

### SEAR: Schema-Based Evaluation and Routing for LLM Gateways

<!-- review:SF-2026-ARXIV-2603-26728:start -->
**问题**：LLM gateway 若把质量、成本、延迟和 issue label 分散在日志与离线表中，routing decision 无法追溯同一 evaluation contract。

**旧路径为何合理**：静态 endpoint 路由在模型与流量同质时足够。

**约束变化与机制**：SEAR 定义跨 context、intent、response issue、quality 与 operational metrics 的 typed relational schema，并以一致性 link 支撑 evaluator 与 router 共享证据。

**State / data / control owner**：`PLATFORM-GATEWAY` 负责 请求分类、策略、fallback 与路由证据；定位证据为 `HTML — §3. The SEAR Framework [facet=method]; https://arxiv.org/html/2603.26728v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26728v1.html; sha256:e45779a637f0881501b2aabb8cd44413185518ba1e84f19feedda3b0f22448b6`。

**Evaluation contract 与未证明部分**：论文展示 schema population 与多 provider routing 案例，能证明数据契约的可查询性；不证明约百列 schema 或自动 evaluator 在所有业务上都校准。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §6.2. Evaluation Performance and §6.3. Routing Performance [facet=evaluation]; https://arxiv.org/html/2603.26728v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26728v1.html; sha256:e45779a637f0881501b2aabb8cd44413185518ba1e84f19feedda3b0f22448b6`。

**Trade-off / failure / coexistence**：统一 schema 提高 lineage，却带来字段维护、迟到数据和 evaluator coupling；单 provider、单指标服务仍可使用较薄 telemetry。

<!-- claim:SF-2026-ARXIV-2603-26728:start -->**Claim Boundary**：只支持 arXiv:2603.26728v1 §3. The SEAR Framework 的机制与 §6.2. Evaluation Performance、§6.3. Routing Performance 的公开 workload；§8. Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26728:end -->
<!-- review:SF-2026-ARXIV-2603-26728:end -->
### The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents

<!-- review:SF-2026-ARXIV-2603-26942:start -->
**问题**：只看最终视觉输出给 human feedback，会让 coding agent 无法区分几何推理错、工具程序错还是执行状态错。

**旧路径为何合理**：日志记录结果适合单进程、短链路故障。

**约束变化与机制**：earned-autonomy 实验让 agent 从零构建函数库，并对比 output-only feedback 与可观察中间 action/trace；核心增量是把过程状态暴露给 verifier，而非增加模型调用。

**State / data / control owner**：`PLATFORM-TRACE` 负责 trace identity、因果边和可归责事件；定位证据为 `HTML — §3.1. Experimental Setup [facet=method]; https://arxiv.org/html/2603.26942v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26942v1.html; sha256:9c4125f62825f8813f42c9d2eaab1b3ab22c1caadfe3466a262a1c6f21954e85`。

**Evaluation contract 与未证明部分**：Blender 3D scene 任务中重发现 utility 但 0% full-scene success，支持输出反馈不足的诊断；单一环境不能证明所有 coding agent 都需要同样 trace。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.2.2. Finding 2: The Observability Gap. [facet=evaluation]; https://arxiv.org/html/2603.26942v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26942v1.html; sha256:9c4125f62825f8813f42c9d2eaab1b3ab22c1caadfe3466a262a1c6f21954e85`。

**Trade-off / failure / coexistence**：过程 observability 提高归因，却扩大日志隐私、反馈负担与可被迎合的表面；可由 deterministic tests 完整验收的短任务仍可少暴露内部 trace。

<!-- claim:SF-2026-ARXIV-2603-26942:start -->**Claim Boundary**：只支持 arXiv:2603.26942v1 §3.1. Experimental Setup 的机制与 §3.2.2. Finding 2: The Observability Gap. 的公开 workload；§4. Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-26942:end -->
<!-- review:SF-2026-ARXIV-2603-26942:end -->
### On the Reliability Limits of LLM-Based Multi-Agent Planning

<!-- review:SF-2026-ARXIV-2603-26993:start -->
**问题**：增加 agent 和消息 hop 常被假定能自动提升规划可靠性，即使所有 agent 只重复同一模型和共同证据。

**旧路径为何合理**：单 agent 保持上下文与责任集中。

**约束变化与机制**：论文把多 agent DAG 形式化为有限 delegated decision network，证明在没有新 exogenous signal 时它受同信息的 centralized Bayes decision maker 支配。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 角色、消息、共享状态与失败归属；定位证据为 `HTML — §2 Delegated Decision Model [facet=method]; https://arxiv.org/html/2603.26993v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26993v1.html; sha256:0b86c9759b64ef9de47a37438e3649255153be62e71c82ca77fecf3c7866e2d4`。

**Evaluation contract 与未证明部分**：理论结果与数值例子支持 common-evidence 边界；它不否定工具、独立传感器、异构模型或人审带来新信息的系统。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §7 Numerical Experiments [facet=evaluation]; https://arxiv.org/html/2603.26993v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.26993v1.html; sha256:0b86c9759b64ef9de47a37438e3649255153be62e71c82ca77fecf3c7866e2d4`。

**Trade-off / failure / coexistence**：集中决策减少 coordination tax，却可能成为容量与信任单点；多 agent 应以新增信息、并行执行或隔离责任为理由，而不是数量本身。

<!-- claim:SF-2026-ARXIV-2603-26993:start -->**Claim Boundary**：只支持 arXiv:2603.26993v1 §2 Delegated Decision Model、§4 Proposition 6/Theorem 7 的理想 centralized Bayes 上界（同一 exogenous information、bounded loss、no-new-information/conditional-independence 假设）及 §7 Numerical Experiments；不证明固定 compute/latency 的现实单 Agent 可模拟任意 DAG，也不外推开放环境的绝对优劣。<!-- claim:SF-2026-ARXIV-2603-26993:end -->
<!-- review:SF-2026-ARXIV-2603-26993:end -->
### The Price of Meaning: Why Every Semantic Memory System Forgets

<!-- review:SF-2026-ARXIV-2603-27116:start -->
**问题**：semantic vector memory 用邻近性实现概念泛化，通常把误召回和遗忘当作可继续调参消除的实现缺陷。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：论文在有限局部维度的 continuous kernel-threshold memory 类中证明：提高语义连续性会不可避免地扩大 interference/false recall，容量与可分性不能同时无限提升。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `HTML — §Mathematical framework: the no-escape theorem [facet=method]; https://arxiv.org/html/2603.27116v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27116v1.html; sha256:82aba70430ed24751f308a1ee668e7799d00e10e52007ba3bee1bd561b61fe5e`。

**Evaluation contract 与未证明部分**：形式定理与 forgetting experiments 支持该模型类内的下界；不覆盖 symbolic key、外部 provenance filter 或混合 exact/semantic memory。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §Forgetting experiments [facet=evaluation]; https://arxiv.org/html/2603.27116v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27116v1.html; sha256:82aba70430ed24751f308a1ee668e7799d00e10e52007ba3bee1bd561b61fe5e`。

**Trade-off / failure / coexistence**：语义 memory 获得类比与柔性检索，却必须接受干扰并配合 exact archive、namespace 与 verification；身份关键事实仍应使用显式 key。

<!-- claim:SF-2026-ARXIV-2603-27116:start -->**Claim Boundary**：只支持 arXiv:2603.27116v1 §Mathematical framework: the no-escape theorem 的机制与 §Forgetting experiments 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27116:end -->
<!-- review:SF-2026-ARXIV-2603-27116:end -->
### ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference

<!-- review:SF-2026-ARXIV-2603-27138:start -->
**问题**：KV offload 若等 GPU 请求后才从 CPU 搬运或计算，会把 PCIe/CPU 等待直接暴露在 decode critical path。

**旧路径为何合理**：全部活跃状态驻留 GPU，访问路径最短。

**约束变化与机制**：ScoutAttention 让 CPU 提前一层计算候选 attention，并把结果/状态与 GPU layer pipeline 重叠；offload owner 因而包含 layer-ahead schedule 和一致性。

**State / data / control owner**：`INFER-GPU-MEMORY` 负责 HBM/DRAM 状态放置、迁移与预取；定位证据为 `HTML — §3.2–§3.4 CPU-based attention estimation, asynchronous prefetch and pipeline integration [facet=method]; https://arxiv.org/html/2603.27138v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27138v1.html; sha256:f53eaf4dda068dc4f3020903103cd79dee2141daaae1f6bbbd061fa6fbdf6058`。

**Evaluation contract 与未证明部分**：长上下文模型上的 batch、latency 与 GPU utilization 实验支持所测 CPU/GPU 平衡；结果绑定主机核数、内存带宽、PCIe 与层结构。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.3. Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.27138v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27138v1.html; sha256:f53eaf4dda068dc4f3020903103cd79dee2141daaae1f6bbbd061fa6fbdf6058`。

**Trade-off / failure / coexistence**：预计算隐藏等待，却可能因 CPU 落后、错误预测或同步产生浪费；KV 可驻 HBM 或 CPU 很弱时普通 GPU attention 更好。

<!-- claim:SF-2026-ARXIV-2603-27138:start -->**Claim Boundary**：只支持 arXiv:2603.27138v1 §3.2–§3.4 的 CPU attention estimation、异步预取与 pipeline integration，以及 §4.3 的作者 workload；不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27138:end -->
<!-- review:SF-2026-ARXIV-2603-27138:end -->
### MalSkills: Detecting Malicious Skills in the Agentic Supply Chain via Neuro-symbolic Reasoning

<!-- review:SF-2026-ARXIV-2603-27204:start -->
**问题**：agent skill 同时含自然语言、代码和配置，单独静态扫描或 LLM 判断都看不到跨 artifact 的恶意意图与副作用。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：MalSkills 先抽取符号 facts，再让神经模型在上下文中推理并用规则约束结论，把 registry admission 建立在多 artifact evidence graph 上。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4. Methodology [facet=method]; https://arxiv.org/html/2603.27204v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27204v1.html; sha256:322df4ae7340ff998bfbe90c67c64e6f5c110c284b2fb8eee25707de2d0985d7`。

**Evaluation contract 与未证明部分**：公开 skill corpus 与攻击样本的检测实验支持组合方法；覆盖依赖规则、sandbox 和标签，不能证明未知语言/运行时无恶意行为。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.27204v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27204v1.html; sha256:322df4ae7340ff998bfbe90c67c64e6f5c110c284b2fb8eee25707de2d0985d7`。

**Trade-off / failure / coexistence**：neuro-symbolic 检查提高可解释性，却增加规则维护、动态执行成本与 false positive；可信内部 skill 仍应配合签名和最小权限。

<!-- claim:SF-2026-ARXIV-2603-27204:start -->**Claim Boundary**：只支持 arXiv:2603.27204v1 §4. Methodology 的机制与 §5. Evaluation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27204:end -->
<!-- review:SF-2026-ARXIV-2603-27204:end -->
### Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving

<!-- review:SF-2026-ARXIV-2603-27287:start -->
**问题**：先生成完整未来视频再规划会让 imagination 与 action decision 脱节，早期预测误差在开环 rollout 中持续累积。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：Uni-World VLA 交替生成 future frame 与 ego trajectory，让每一步 action 重新条件化下一段 world state；world prediction 与 planning 共享可修订状态。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3 Methods [facet=method]; https://arxiv.org/html/2603.27287v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27287v1.html; sha256:7cbf9225bf4bc9e3e02f0d60093197f93b2b947a9e1ffe1b506c9bec7706e6a5`。

**Evaluation contract 与未证明部分**：自动驾驶 benchmark 支持所测模型在预测/规划指标上的联合收益；生成帧质量与闭环道路安全仍不是同一证据。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.1 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.27287v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27287v1.html; sha256:7cbf9225bf4bc9e3e02f0d60093197f93b2b947a9e1ffe1b506c9bec7706e6a5`。

**Trade-off / failure / coexistence**：交错闭环减少漂移，却增加推理延迟、状态 commit 与错误耦合；低延迟 reactive control 或高保真 simulator 仍可能分层部署。

<!-- claim:SF-2026-ARXIV-2603-27287:start -->**Claim Boundary**：只支持 arXiv:2603.27287v1 §3 Methods 的机制与 §4.1 Experimental Setup 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27287:end -->
<!-- review:SF-2026-ARXIV-2603-27287:end -->
### From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification

<!-- review:SF-2026-ARXIV-2603-27299:start -->
**问题**：gateway、agent workflow、Kubernetes 与协议边界分别维护策略，会让同一阈值和权限在层间漂移。

**旧路径为何合理**：单团队脚本可快速交付模型服务。

**约束变化与机制**：Semantic Router DSL 用非图灵完备 declarative source 编译 priority decision tree、orchestration node、NetworkPolicy/Sandbox 和 MCP/A2A gate，并保留结构化 audit trace。

**State / data / control owner**：`PLATFORM-FOUNDATIONS` 负责 资产、workload、service 与 controller ownership；定位证据为 `HTML — §3.1 Compilation Architecture [facet=method]; https://arxiv.org/html/2603.27299v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27299v1.html; sha256:94c6ea669f265287d15d81616802fcfba08afa16b70e87bfe71a2d3c2fcb1568`。

**Evaluation contract 与未证明部分**：论文可支持语言约束与生成 artifact 的一致性主张；不能证明所有目标 runtime 语义等价或 production scale。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §A.3 Generated: LangGraph Decision Node (Strategy A) [facet=evaluation]; https://arxiv.org/html/2603.27299v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27299v1.html; sha256:94c6ea669f265287d15d81616802fcfba08afa16b70e87bfe71a2d3c2fcb1568`。

**Trade-off / failure / coexistence**：统一编译减少 drift，却放大 compiler bug blast radius并限制表达力；局部复杂策略仍需专用控制器。

<!-- claim:SF-2026-ARXIV-2603-27299:start -->**Claim Boundary**：只支持 arXiv:2603.27299v1 §3.1 Compilation Architecture 的机制与 §A.3 Generated: LangGraph Decision Node (Strategy A) 的公开 workload；§7.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27299:end -->
<!-- review:SF-2026-ARXIV-2603-27299:end -->
### LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications

<!-- review:SF-2026-ARXIV-2603-27355:start -->
**问题**：离线平均分、线上 telemetry 与 CI 发布通常分属不同工具，任何一个单独通过都不足以说明 LLM/RAG workload ready。

**旧路径为何合理**：离线测试通过后人工发布最直观。

**约束变化与机制**：readiness harness 以统一 scenario schema 聚合 workflow success、policy、groundedness、retrieval、cost 与 p95 latency，并用 Pareto frontier 形成 release gate。

**State / data / control owner**：`PLATFORM-PRODUCTION` 负责 evaluation evidence、release gate 与 rollback；定位证据为 `HTML — §2 System Overview [facet=method]; https://arxiv.org/html/2603.27355v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27355v1.html; sha256:566ea9e917527b6870c3da3ca75917ed0e76e39b5cfa11e0be820402b9d35650`。

**Evaluation contract 与未证明部分**：ticket routing、BEIR 与 Azure matrix 支持该 harness 的可复现组合判断；权重和阈值是案例配置，不是通用生产标准。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.27355v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27355v1.html; sha256:566ea9e917527b6870c3da3ca75917ed0e76e39b5cfa11e0be820402b9d35650`。

**Trade-off / failure / coexistence**：统一 gate 提高发布可追溯性，却可能被错误权重或 evaluator drift 绑架；窄服务仍可使用更少指标，但必须保留独立回滚条件。

<!-- claim:SF-2026-ARXIV-2603-27355:start -->**Claim Boundary**：只支持 arXiv:2603.27355v1 §2 System Overview 的机制与 §5 Experiments 的公开 workload；§8 Limitations and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27355:end -->
<!-- review:SF-2026-ARXIV-2603-27355:end -->
### TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization

<!-- review:SF-2026-ARXIV-2603-27467:start -->
**问题**：固定逐元素 KV quantization 忽略旋转后成对向量近似落在单位圆的结构，也常把所有层分配同一 bit budget。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：TurboAngle 在 Walsh-Hadamard 域量化角度，并按层分别提高 K/V codebook precision，把 bit allocation 变成模型层级策略。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `HTML — §3.1 Angular Quantization [facet=method]; https://arxiv.org/html/2603.27467v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27467v1.html; sha256:cfee62c0d25b6bc44d6f6d0df84787f867ed99accbb2005544871bd10dfb896e`。

**Evaluation contract 与未证明部分**：七个 1B–7B 模型的质量与 bit-rate 实验支持所测压缩范围；一个模型未达 near-lossless，且 kernel/硬件 SLO 未充分证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.7 Competitive Comparison [facet=evaluation]; https://arxiv.org/html/2603.27467v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27467v1.html; sha256:cfee62c0d25b6bc44d6f6d0df84787f867ed99accbb2005544871bd10dfb896e`。

**Trade-off / failure / coexistence**：角度编码降低 footprint，却增加旋转、norm metadata 和模型校准；未支持 kernel 或需严格 exactness 时更高精度 KV 仍合理。

<!-- claim:SF-2026-ARXIV-2603-27467:start -->**Claim Boundary**：只支持 arXiv:2603.27467v1 §3.1 Angular Quantization 的机制与 §4.7 Competitive Comparison 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27467:end -->
<!-- review:SF-2026-ARXIV-2603-27467:end -->
### A Security Analysis of the OpenClaw AI Agent Framework

<!-- review:SF-2026-ARXIV-2603-27517:start -->
**问题**：agent runtime 把 shell、filesystem、browser、plugin 与 messaging 接到模型后，传统按 CVE 组件计数无法说明 trust violation 穿过哪一执行层。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文把 470 条 OpenClaw advisory 按 system layer 与 attack technique 双轴归类，并据此比较 exec policy、gateway、channel、sandbox 与 prompt 的防线责任。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4 Security Taxonomy [facet=method]; https://arxiv.org/html/2603.27517v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27517v1.html; sha256:639fe9ecdf3eaca9d8788361d40a3bb9f2bca2aadfd9c7d4355f055a8c0da21e`。

**Evaluation contract 与未证明部分**：公开 advisory taxonomy 能证明该版本生态的缺陷分布；披露偏差、重复 advisory 和快速版本演进禁止外推为所有 agent framework 风险率。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3 Corpus Overview [facet=evaluation]; https://arxiv.org/html/2603.27517v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27517v1.html; sha256:639fe9ecdf3eaca9d8788361d40a3bb9f2bca2aadfd9c7d4355f055a8c0da21e`。

**Trade-off / failure / coexistence**：双轴分类改善 threat-model coverage，却仍是事后样本；生产系统需要 capability inventory、effect-time authorization 与可验证 patch lineage。

<!-- claim:SF-2026-ARXIV-2603-27517:start -->**Claim Boundary**：只支持 arXiv:2603.27517v1 §4 Security Taxonomy 的机制与 §3 Corpus Overview 的公开 workload；§6 Defense Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27517:end -->
<!-- review:SF-2026-ARXIV-2603-27517:end -->
### Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling

<!-- review:SF-2026-ARXIV-2603-27624:start -->
**问题**：低 batch edge MoE 不能把全部 expert 放入片上内存，传统 offload 又在动态 gate 下产生细粒度传输和负载失衡。

**旧路径为何合理**：通用算子图优先可移植性和实现简单。

**约束变化与机制**：Expert Streaming 在多 chiplet 共享 expert shard，并按预测的 expert trajectory 动态调度传输/执行，把 gate path、placement 与 interconnect schedule 联合优化。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel、precision、layout 与执行计划 owner；定位证据为 `HTML — §IV FSE-DP with Micro-Slice Flow + §V MoE Scheduler [facet=method]; https://arxiv.org/html/2603.27624v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27624v1.html; sha256:8044b905d9dfa3b7204fef979255be015d46705b078637e682465583bb56c50e`。

**Evaluation contract 与未证明部分**：架构模拟/实验支持所测模型与 chiplet 参数的 latency/energy 改善；结论依赖 die-to-die 带宽、gate 分布和低 batch 假设。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §VI-C End-to-End Evaluation with Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.27624v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27624v1.html; sha256:8044b905d9dfa3b7204fef979255be015d46705b078637e682465583bb56c50e`。

**Trade-off / failure / coexistence**：细粒度 streaming 减少 off-chip 等待，却增加预测错误、跨 chiplet 同步和硬件专用性；大 batch 数据中心仍可用常规 expert parallel。

<!-- claim:SF-2026-ARXIV-2603-27624:start -->**Claim Boundary**：只支持 arXiv:2603.27624v1 §IV FSE-DP with Micro-Slice Flow、§V MoE Scheduler 的机制与 §VI-C End-to-End Evaluation with Ablation Studies 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27624:end -->
<!-- review:SF-2026-ARXIV-2603-27624:end -->
### KVSculpt: KV Cache Compression as Distillation

<!-- review:SF-2026-ARXIV-2603-27819:start -->
**问题**：KV sequence compression 从 eviction 到 merging 都被原始 cache entry 约束，保留对象未必是最适合未来 query 的表示。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：KVSculpt 把压缩视为 distillation，直接优化一组更小、非原条目约束的连续 KV，使 future-query output 成为训练目标。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `HTML — §3.2 Loss Function [facet=method]; https://arxiv.org/html/2603.27819v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27819v1.html; sha256:a8d981fbdd44b29ee3b9388c5c504e5190368b1805928e462d8245b7619c3367`。

**Evaluation contract 与未证明部分**：所测模型/任务的质量-长度实验支持 learned synthetic KV 优于若干 eviction/merge baseline；优化查询分布与 offline 成本限制在线泛化。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.1 Main Results: Distillation vs. Eviction [facet=evaluation]; https://arxiv.org/html/2603.27819v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27819v1.html; sha256:a8d981fbdd44b29ee3b9388c5c504e5190368b1805928e462d8245b7619c3367`。

**Trade-off / failure / coexistence**：distilled KV 提高单位 slot 信息量，却可能过拟合未来 query、缺少可解释 token identity；动态未知 workload 仍可优先 eviction/merge。

<!-- claim:SF-2026-ARXIV-2603-27819:start -->**Claim Boundary**：只支持 arXiv:2603.27819v1 §3.2 Loss Function 的机制与 §5.1 Main Results: Distillation vs. Eviction 的公开 workload；§6 Analysis: Limits of Per-Layer Optimization 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27819:end -->
<!-- review:SF-2026-ARXIV-2603-27819:end -->
### ATLAS-RTC: Closing the Loop on LLM Agent Output with Token-Level Runtime Control

<!-- review:SF-2026-ARXIV-2603-27905:start -->
**问题**：post-hoc validator 只能在完整输出后拒绝，static constrained decoding 又难处理运行时 contract 漂移。

**旧路径为何合理**：把 agent 当进程内 loop 能快速试验。

**约束变化与机制**：ATLAS-RTC 在每个 token 监控 contract drift，并用 bias、mask 与 rollback 闭环干预，把生成状态的 commit 权交给 runtime controller。

**State / data / control owner**：`AGENT-PLATFORM` 负责 agent identity、skill、execution state 与控制面；定位证据为 `HTML — §3.9 Implementation [facet=method]; https://arxiv.org/html/2603.27905v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27905v1.html; sha256:abb1754a4b2be29c93e4277660d622af2f357861c122b02bfe7de10237ea4271`。

**Evaluation contract 与未证明部分**：structured generation/tool-calling 实验支持指定 failure-heavy workload 的 success/latency；不证明轻量信号能识别语义正确性。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §Relation to Post-hoc Validation and Repair. [facet=evaluation]; https://arxiv.org/html/2603.27905v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.27905v1.html; sha256:abb1754a4b2be29c93e4277660d622af2f357861c122b02bfe7de10237ea4271`。

**Trade-off / failure / coexistence**：逐 token 控制提高合规却增加监控开销和错误 rollback；语法固定时普通 constrained decoding 更简单。

<!-- claim:SF-2026-ARXIV-2603-27905:start -->**Claim Boundary**：只支持 arXiv:2603.27905v1 §3.9 Implementation 的机制与 §Relation to Post-hoc Validation and Repair. 的公开 workload；§Limitations of Drift Detection. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-27905:end -->
<!-- review:SF-2026-ARXIV-2603-27905:end -->
### Rethinking Atomic Decomposition for LLM Judges: A Prompt-Controlled Study of Reference-Grounded QA Evaluation

<!-- review:SF-2026-ARXIV-2603-28005:start -->
**问题**：atomic claim decomposition 常与更长、更细 rubric 一起变化，观察到的收益无法归因于 decomposition 本身。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：研究冻结输入与 prompt richness，只改变 self-decomposing atomic 与 holistic judge，并跨 prompt variant 做 paired/bootstrap 比较。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §3.1 Judge designs [facet=method]; https://arxiv.org/html/2603.28005v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28005v1.html; sha256:6f94ed98c43b761f6dfd1c068495e2df8d8110532e152484d4134b4f5a8c7b38`。

**Evaluation contract 与未证明部分**：三个 QA benchmark、四类模型支持该单 prompt 设定的条件结论；不覆盖多阶段 atomic pipeline 或非 QA。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §A Matched Holistic Rubric Rivals Self-Decomposing Atomic Judges for Benchmark-Style Reference-Support Classification [facet=evaluation]; https://arxiv.org/html/2603.28005v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28005v1.html; sha256:6f94ed98c43b761f6dfd1c068495e2df8d8110532e152484d4134b4f5a8c7b38`。

**Trade-off / failure / coexistence**：atomic 提高可定位性却会累积拆分误差和成本；完整性敏感任务中 rich holistic judge 可能更稳。

<!-- claim:SF-2026-ARXIV-2603-28005:start -->**Claim Boundary**：只支持 arXiv:2603.28005v1 §3.1 Judge designs 的机制与 §A Matched Holistic Rubric Rivals Self-Decomposing Atomic Judges for Benchmark-Style Reference-Support Classification 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28005:end -->
<!-- review:SF-2026-ARXIV-2603-28005:end -->
### Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers

<!-- review:SF-2026-ARXIV-2603-28013:start -->
**问题**：prompt injection 只报最终成功/失败，会把暴露、持久化、跨 agent relay 与真正执行混成一个二值结果。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：kill-chain canary 用加密 token 追踪 EXPOSED→PERSISTED→RELAYED→EXECUTED 四阶段，跨 attack surface 和 defense tier 定位防线在哪一 hop 失效。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §3.2 Kill-Chain Stages and Attack Scenarios [facet=method]; https://arxiv.org/html/2603.28013v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28013v1.html; sha256:de58184a1b182e4ab5fd9d6faa1a6dae70e3c4d242a94771b5bd039ed407777b`。

**Evaluation contract 与未证明部分**：950 runs、五个模型、六类 surface 与五种 defense 支持所测 pipeline 的阶段差异；canary 可见性和场景集合不等于所有真实攻击。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.1 Exposure Is Universal; Defense Is Downstream [facet=evaluation]; https://arxiv.org/html/2603.28013v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28013v1.html; sha256:de58184a1b182e4ab5fd9d6faa1a6dae70e3c4d242a94771b5bd039ed407777b`。

**Trade-off / failure / coexistence**：阶段 telemetry 提高诊断，却引入追踪状态、隐私和 canary 被识别的风险；单模型无持久状态系统仍可用更简单 outcome test。

<!-- claim:SF-2026-ARXIV-2603-28013:start -->**Claim Boundary**：只支持 arXiv:2603.28013v1 §3.2 Kill-Chain Stages and Attack Scenarios 的机制与 §4.1 Exposure Is Universal; Defense Is Downstream 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28013:end -->
<!-- review:SF-2026-ARXIV-2603-28013:end -->
### Reward Hacking as Equilibrium under Finite Evaluation

<!-- review:SF-2026-ARXIV-2603-28063:start -->
**问题**：有限 evaluator 只覆盖部分质量维度时，优化器会系统性把资源移向可测维度，reward hacking 不是偶发实现 bug。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文在多维质量、有限评测和资源约束下推导 distortion index，并分析 agent tool 增长使 coverage 组合性下降。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §7.1 What This Framework Provides [facet=method]; https://arxiv.org/html/2603.28063v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28063v1.html; sha256:c9d819fe17c108947432f6b76705621e89876aebae07bf39712d7a12fdb2182c`。

**Evaluation contract 与未证明部分**：主要证据是给定公理下的理论结果与部分分析；不能证明现实系统完全满足假设或数值阈值。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §6.2 Capability-Dependent Evaluation Fidelity [facet=evaluation]; https://arxiv.org/html/2603.28063v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28063v1.html; sha256:c9d819fe17c108947432f6b76705621e89876aebae07bf39712d7a12fdb2182c`。

**Trade-off / failure / coexistence**：扩大评测覆盖能减轻但不能消除盲区，并使成本快速增长；限制工具与权限仍是有效结构性手段。

<!-- claim:SF-2026-ARXIV-2603-28063:start -->**Claim Boundary**：只支持 arXiv:2603.28063v1 §7.1 What This Framework Provides 的机制与 §6.2 Capability-Dependent Evaluation Fidelity 的公开 workload；§5.5 Conditions for Model Failure 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28063:end -->
<!-- review:SF-2026-ARXIV-2603-28063:end -->
### Heddle: A Distributed Orchestration System for Agentic RL Rollout

<!-- review:SF-2026-ARXIV-2603-28101:start -->
**问题**：agentic RL rollout 按 step 排队时忽略 trajectory 的 tool-wait 与长尾上下文，造成 queueing、interference 和 inflated per-token time。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：Heddle 以 trajectory 为调度对象，联合决定何时继续、放到哪里以及如何组织 tool/LLM execution，使 rollout context 成为显式 runtime state。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `HTML — §4 Trajectory-level Scheduler [facet=method]; https://arxiv.org/html/2603.28101v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28101v1.html; sha256:6db6453b7511dc4fea5543a5351ad8424d1003ad2fce9b2a1927946c83a5d04f`。

**Evaluation contract 与未证明部分**：分布式 agentic RL workload 的 throughput/尾延迟实验支持所测系统；结果绑定工具延迟、模型、cluster 和训练同步策略。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §7.1 Overall Performance [facet=evaluation]; https://arxiv.org/html/2603.28101v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28101v1.html; sha256:6db6453b7511dc4fea5543a5351ad8424d1003ad2fce9b2a1927946c83a5d04f`。

**Trade-off / failure / coexistence**：trajectory-aware orchestration 减少长尾，却增加 state migration、fairness 和 stale-policy 管理；同步、短 rollout 仍可使用 step-centric pipeline。

<!-- claim:SF-2026-ARXIV-2603-28101:start -->**Claim Boundary**：只支持 arXiv:2603.28101v1 §4 Trajectory-level Scheduler 的机制与 §7.1 Overall Performance 的公开 workload；§8 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28101:end -->
<!-- review:SF-2026-ARXIV-2603-28101:end -->
### Evaluating Privilege Usage of Agents with Real-World Tools

<!-- review:SF-2026-ARXIV-2603-28166:start -->
**问题**：预编码 toy tool 无法暴露真实 SDK 的 privilege scope、副作用和 prompt-injection 路径。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：GrantBox 把真实工具接入隔离 sandbox，记录 agent 获得、请求和实际使用的 privilege，按 attack trace 评估越权。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §2. Method [facet=method]; https://arxiv.org/html/2603.28166v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28166v1.html; sha256:f7b71ff51add384dcc77cc577f980c52a6e289d6badd128881dd4a2820f455de`。

**Evaluation contract 与未证明部分**：公开场景支持所测 agent 在复杂 injection 下的高攻击成功率；不能外推所有工具或把 sandbox 当生产隔离证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.3. LLM Security Evaluation [facet=evaluation]; https://arxiv.org/html/2603.28166v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28166v1.html; sha256:f7b71ff51add384dcc77cc577f980c52a6e289d6badd128881dd4a2820f455de`。

**Trade-off / failure / coexistence**：真实工具提高生态效度却增加运行风险、凭证管理和复现成本；单元 conformance 仍适合早期检查。

<!-- claim:SF-2026-ARXIV-2603-28166:start -->**Claim Boundary**：只支持 arXiv:2603.28166v1 §2. Method 的机制与 §3.3. LLM Security Evaluation 的公开 workload；§4. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28166:end -->
<!-- review:SF-2026-ARXIV-2603-28166:end -->
### Leaf-centric Logical Topology Design for OCS-based GPU Clusters

<!-- review:SF-2026-ARXIV-2603-28168:start -->
**问题**：OCS GPU cluster 的 circuit path 会产生 routing polarization，传统以 spine 为中心的拓扑优化可能把不均衡下沉到 leaf link。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：leaf-centric 设计约束同一 leaf 流量在 spine 间均衡，并给出避免 polarization 的充分条件与多项式算法。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `HTML — §III-C How to design intra-Pod architecture [facet=method]; https://arxiv.org/html/2603.28168v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28168v1.html; sha256:3210fff764f92720d53efb81b80e788a9adab83ff1d24952f66eb9c7ce6395cc`。

**Evaluation contract 与未证明部分**：理论与大规模 simulation 支持所建流量/拓扑模型的吞吐和求解成本；未证明真实 OCS 重配置与故障下同样成立。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §IV-B Performance Analysis [facet=evaluation]; https://arxiv.org/html/2603.28168v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28168v1.html; sha256:3210fff764f92720d53efb81b80e788a9adab83ff1d24952f66eb9c7ce6395cc`。

**Trade-off / failure / coexistence**：快速均衡牺牲全局最优空间并依赖流量估计；规模小或拓扑静态时 MIP/固定布线仍可用。

<!-- claim:SF-2026-ARXIV-2603-28168:start -->**Claim Boundary**：只支持 arXiv:2603.28168v1 §III-C How to design intra-Pod architecture 的机制与 §IV-B Performance Analysis 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28168:end -->
<!-- review:SF-2026-ARXIV-2603-28168:end -->
### A Switch-Centric In-Network Architecture for Accelerating LLM Inference in Shared-Memory Network

<!-- review:SF-2026-ARXIV-2603-28239:start -->
**问题**：tensor parallel inference 的 All-Reduce 在关键路径上频繁同步，GPU 发起的细粒度 in-network 操作会重复占用 switch/GPU 控制。

**旧路径为何合理**：通用算子图优先可移植性和实现简单。

**约束变化与机制**：论文把 collective schedule 移到 switch-centric controller，由网络侧聚合 shared-memory operation，而不是每个 GPU 逐元素驱动。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel、precision、layout 与执行计划 owner；定位证据为 `HTML — §3. Design and Implementation [facet=method]; https://arxiv.org/html/2603.28239v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28239v1.html; sha256:a8e52b8bf9827e08f6ee558d6b03a645c32facfd8b99f951acd3717b17ed123c`。

**Evaluation contract 与未证明部分**：架构评估支持所测 topology/message size 的 latency 与利用率收益；尚不能证明真实交换芯片、故障和多租户隔离下同样成立。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.5. LLM TP Inference [facet=evaluation]; https://arxiv.org/html/2603.28239v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28239v1.html; sha256:a8e52b8bf9827e08f6ee558d6b03a645c32facfd8b99f951acd3717b17ed123c`。

**Trade-off / failure / coexistence**：网络拥有更多控制可减少 GPU 开销，却增加可编程 switch 状态、故障域和部署专用性；小规模或标准 collective 已足够时普通 NCCL 更可移植。

<!-- claim:SF-2026-ARXIV-2603-28239:start -->**Claim Boundary**：只支持 arXiv:2603.28239v1 §3. Design and Implementation 的机制与 §4.5. LLM TP Inference 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28239:end -->
<!-- review:SF-2026-ARXIV-2603-28239:end -->
### Kernel-Smith: A Unified Recipe for Evolutionary Kernel Optimization

<!-- review:SF-2026-ARXIV-2603-28342:start -->
**问题**：one-shot kernel generation 难同时保持 correctness 与性能，单一 incumbent 也容易在局部最优中坍缩。

**旧路径为何合理**：通用算子图优先可移植性和实现简单。

**约束变化与机制**：Kernel-Smith 维护可执行 candidate population，以 compile/correctness/speed feedback 进化，并将高增益正确 revision 转成 step-centric SFT/RL 信号。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel、precision、layout 与执行计划 owner；定位证据为 `HTML — §2.3 Advanced Search and Evolution Algorithms [facet=method]; https://arxiv.org/html/2603.28342v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28342v1.html; sha256:71dabc1c9dbb65ebb64f473f2f54031aa381e6ecfa7247844bbb34dffffad2a6`。

**Evaluation contract 与未证明部分**：KernelBench、NVIDIA Triton 与 MetaX MACA 结果支持所测 backend 的搜索/训练闭环；vendor/author benchmark 不代表任意生产 kernel。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.3 Evaluation Backends [facet=evaluation]; https://arxiv.org/html/2603.28342v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28342v1.html; sha256:71dabc1c9dbb65ebb64f473f2f54031aa381e6ecfa7247844bbb34dffffad2a6`。

**Trade-off / failure / coexistence**：evolution 提高搜索覆盖却消耗大量编译执行预算并可能过拟合 harness；成熟常用 kernel 仍优先人工库。

<!-- claim:SF-2026-ARXIV-2603-28342:start -->**Claim Boundary**：只支持 arXiv:2603.28342v1 §2.3 Advanced Search and Evolution Algorithms 的机制与 §3.3 Evaluation Backends 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28342:end -->
<!-- review:SF-2026-ARXIV-2603-28342:end -->
### Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications

<!-- review:SF-2026-ARXIV-2603-28345:start -->
**问题**：LLM call 把程序值穿过不透明自然语言变换，传统 taint summary 在 NL/PL 边界断裂。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：PRISM 用 placeholder→output reachability 和信息保留×输出模态的有限 taxonomy，为 LLM call 生成可组合 dataflow predicate。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4.2.2. Method Comparison [facet=method]; https://arxiv.org/html/2603.28345v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28345v1.html; sha256:224c96638605c03309909517fb5d74bbb0311828c0f6ff424e9797092a1a41d5`。

**Evaluation contract 与未证明部分**：8,119 对样本、annotator agreement 与 taint evaluation 支持 taxonomy coverage；soundness 只相对标签成立，不代表 LLM 变换可完全预测。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.28345v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28345v1.html; sha256:224c96638605c03309909517fb5d74bbb0311828c0f6ff424e9797092a1a41d5`。

**Trade-off / failure / coexistence**：taxonomy 恢复静态分析却引入分类误差和保守传播；不含动态 prompt 的普通函数仍用精确 summary。

<!-- claim:SF-2026-ARXIV-2603-28345:start -->**Claim Boundary**：只支持 arXiv:2603.28345v1 §4.2.2. Method Comparison 的机制与 §4. Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28345:end -->
<!-- review:SF-2026-ARXIV-2603-28345:end -->
### Continued AI Scaling Requires Repeated Efficiency Doublings

<!-- review:SF-2026-ARXIV-2603-28507:start -->
**问题**：只依赖更多算力延续 scaling，会忽略效率改进必须重复发生才能抵消硬件、数据与成本约束。

**旧路径为何合理**：按单次拟合曲线外推最省实验成本。

**约束变化与机制**：论文把能力扩展分解为 compute growth 与连续 efficiency doubling，要求 scaling forecast 显式记录算法/系统效率来源而非单一 FLOP。

**State / data / control owner**：`WORLDVIEW-SCALING-LAW` 负责 scaling experiment 的数据、拟合与决策证据；定位证据为 `HTML — §4 A Time-Indexed Efficiency-Doubling Extension [facet=method]; https://arxiv.org/html/2603.28507v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28507v1.html; sha256:19d95beb5b41e821c142d2ea6e86a20172b7c3b7d5b19f51b55f8e9c75a28bcb`。

**Evaluation contract 与未证明部分**：历史估计与情景分析只能支持所用指标和时间段的趋势；不能保证未来 doubling 速度或因果来源。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 The Operational Meaning of Diminishing Returns [facet=evaluation]; https://arxiv.org/html/2603.28507v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28507v1.html; sha256:19d95beb5b41e821c142d2ea6e86a20172b7c3b7d5b19f51b55f8e9c75a28bcb`。

**Trade-off / failure / coexistence**：效率视角改善规划却高度依赖基准口径与选择偏差；同代固定系统比较仍可用纯 compute 曲线。

<!-- claim:SF-2026-ARXIV-2603-28507:start -->**Claim Boundary**：只支持 arXiv:2603.28507v1 §4 A Time-Indexed Efficiency-Doubling Extension 的机制与 §5 The Operational Meaning of Diminishing Returns 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28507:end -->
<!-- review:SF-2026-ARXIV-2603-28507:end -->
### StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation

<!-- review:SF-2026-ARXIV-2603-28565:start -->
**问题**：VLA 把 observation、action generation 与 execution 串行化时，robot 会在每轮推理等待，吞吐提升也不一定满足连续控制。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：StreamingVLA 用 action flow matching 流式生成 chunk，并按当前状态提前触发下一 observation，使感知与执行重叠且保持可取消的更新。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `HTML — §4.1 State-based Modeling of Action Flow Matching [facet=method]; https://arxiv.org/html/2603.28565v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28565v1.html; sha256:01e94cd7760c5754ba517db1d330f4ecea288fbce15eb5deead177d7a3df05c1`。

**Evaluation contract 与未证明部分**：机器人任务的控制流畅度、latency 与 success 实验支持所测平台；不能外推到更高频控制、不同传感器或安全关键动作。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.28565v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28565v1.html; sha256:01e94cd7760c5754ba517db1d330f4ecea288fbce15eb5deead177d7a3df05c1`。

**Trade-off / failure / coexistence**：streaming 降低停顿，却引入 observation staleness、chunk cancellation 与并发状态一致性；慢速或高精度动作仍可保持串行 observe-plan-act。

<!-- claim:SF-2026-ARXIV-2603-28565:start -->**Claim Boundary**：只支持 arXiv:2603.28565v1 §4.1 State-based Modeling of Action Flow Matching 的机制与 §5.2 Experimental Results 的公开 workload；§7 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28565:end -->
<!-- review:SF-2026-ARXIV-2603-28565:end -->
### MonitorBench: A Comprehensive Benchmark for Chain-of-Thought Monitorability in Large Language Models

<!-- review:SF-2026-ARXIV-2603-28590:start -->
**问题**：CoT 文本可能与最终决策因子脱钩，把可读推理直接当 oversight signal 会产生伪安全感。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：MonitorBench 用显式 decision-critical factor、19 类任务与 stress prompt 测量被监控模型、monitor 模型和任务的条件性交互。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §3.1 Evaluation Design [facet=method]; https://arxiv.org/html/2603.28590v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28590v1.html; sha256:98b2973d8f1d2625800744ee3ab60ee791b064d3f2724ed56342b3080acc4178`。

**Evaluation contract 与未证明部分**：1,514 例实验支持 monitorability 是条件属性且可被压低；不证明隐藏推理或真实因果链被恢复。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.3 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.28590v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28590v1.html; sha256:98b2973d8f1d2625800744ee3ab60ee791b064d3f2724ed56342b3080acc4178`。

**Trade-off / failure / coexistence**：更强 stress test 提高风险发现，却不能把低 monitorability 修复为可验证行为；高风险动作仍需外部 effect receipt。

<!-- claim:SF-2026-ARXIV-2603-28590:start -->**Claim Boundary**：只支持 arXiv:2603.28590v1 §3.1 Evaluation Design 的机制与 §3.3 Evaluation Metrics 的公开 workload；§4.3 Mechanisms of Failure and Evasion in Monitoring (RQ3) 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28590:end -->
<!-- review:SF-2026-ARXIV-2603-28590:end -->
### Trust-Aware Routing for Distributed Generative AI Inference at the Edge

<!-- review:SF-2026-ARXIV-2603-28622:start -->
**问题**：edge distributed inference 的 best-effort peer route 不区分节点失效、性能波动与恶意行为，单个 peer 可使链路失败。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：G-TRAC 用 trust-floor pruning 加 risk-bounded shortest path，并由稳定 anchor 保存 reputation、边缘后台同步轻量状态。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `HTML — §IV G-TRAC Design and Algorithm [facet=method]; https://arxiv.org/html/2603.28622v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28622v1.html; sha256:fa3f72e9e68357b3bcc9d5c9fdfbe7c9b8ed11f82c28deae8aaa39e0d7fe3623`。

**Evaluation contract 与未证明部分**：异构 testbed 支持指定规模/故障与分区下的 completion；trust score 来源与攻击适应性限制外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §IV-D Complexity Analysis [facet=evaluation]; https://arxiv.org/html/2603.28622v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28622v1.html; sha256:fa3f72e9e68357b3bcc9d5c9fdfbe7c9b8ed11f82c28deae8aaa39e0d7fe3623`。

**Trade-off / failure / coexistence**：trust-aware route 提高韧性却引入中心 anchor、陈旧 reputation 与误隔离；可信小集群仍可用普通最短路。

<!-- claim:SF-2026-ARXIV-2603-28622:start -->**Claim Boundary**：只支持 arXiv:2603.28622v1 §IV G-TRAC Design and Algorithm 的机制与 §IV-D Complexity Analysis 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28622:end -->
<!-- review:SF-2026-ARXIV-2603-28622:end -->
### Information-Theoretic Limits of Safety Verification for Self-Improving Systems

<!-- review:SF-2026-ARXIV-2603-28650:start -->
**问题**：若每轮 self-modification 都只靠有重叠分布的 classifier gate，要求累计风险可和与无限效用可能相互冲突。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文给出 classifier TPR 与风险预算的上界，并以 Lipschitz-ball verifier 说明可验证结构如何逃离统计分类限制。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4.2 Construction: Lipschitz Ball Verifier [facet=method]; https://arxiv.org/html/2603.28650v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28650v1.html; sha256:8f7b79d227df5121cd1e1744c1daf12fa9d597c0b88a2f89df519b3ecc96321e`。

**Evaluation contract 与未证明部分**：定理只在明确公理与分布条件内成立；GPT-2/LoRA 实验是受限验证，不证明大规模 agent 自改安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §7.1 LLM-Scale Mechanism Validation: GPT-2 with LoRA [facet=evaluation]; https://arxiv.org/html/2603.28650v1; papers/2026/03/_sources/daily-20260331/exact-v1-bodies/2603.28650v1.html; sha256:8f7b79d227df5121cd1e1744c1daf12fa9d597c0b88a2f89df519b3ecc96321e`。

**Trade-off / failure / coexistence**：形式 verifier 可把局部风险压低，却限制允许修改集合并依赖 bound 正确；不可验证开放修改必须设有限预算和人工 gate。

<!-- claim:SF-2026-ARXIV-2603-28650:start -->**Claim Boundary**：只支持 arXiv:2603.28650v1 §4.2 Construction: Lipschitz Ball Verifier 的机制与 §7.1 LLM-Scale Mechanism Validation: GPT-2 with LoRA 的公开 workload；§9 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-28650:end -->
<!-- review:SF-2026-ARXIV-2603-28650:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26728 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-26728 |
| SF-2026-ARXIV-2603-26993 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-26993 |
| SF-2026-ARXIV-2603-27116 | score_7_9;potential_books_delta | selected | DA-20260331-04 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260331-04 |
| SF-2026-ARXIV-2603-27138 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-27138 |
| SF-2026-ARXIV-2603-27624 | score_7_9;potential_books_delta | selected | DA-20260331-12 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260331-12 |
| SF-2026-ARXIV-2603-27819 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-27819 |
| SF-2026-ARXIV-2603-28101 | score_7_9;potential_books_delta | selected | DA-20260331-18 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260331-18 |
| SF-2026-ARXIV-2603-28239 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-28239 |

<!-- analysis-decision:SF-2026-ARXIV-2603-26728:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-26728:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-26993:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-26993:end -->
<!-- analysis:DA-20260331-04:start -->
### The Price of Meaning: Why Every Semantic Memory System Forgets

semantic vector memory 用邻近性实现概念泛化，通常把误召回和遗忘当作可继续调参消除的实现缺陷。 旧路径在其原约束下仍合理：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。 本 family 的设计变化是：论文在有限局部维度的 continuous kernel-threshold memory 类中证明：提高语义连续性会不可避免地扩大 interference/false recall，容量与可分性不能同时无限提升。 其公开验证边界为：形式定理与 forgetting experiments 支持该模型类内的下界；不覆盖 symbolic key、外部 provenance filter 或混合 exact/semantic memory。 新增代价与回退条件为：语义 memory 获得类比与柔性检索，却必须接受干扰并配合 exact archive、namespace 与 verification；身份关键事实仍应使用显式 key。
<!-- analysis:DA-20260331-04:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-27138:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-27138:end -->
<!-- analysis:DA-20260331-12:start -->
### Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling

低 batch edge MoE 不能把全部 expert 放入片上内存，传统 offload 又在动态 gate 下产生细粒度传输和负载失衡。 旧路径在其原约束下仍合理：通用算子图优先可移植性和实现简单。 本 family 的设计变化是：Expert Streaming 在多 chiplet 共享 expert shard，并按预测的 expert trajectory 动态调度传输/执行，把 gate path、placement 与 interconnect schedule 联合优化。 其公开验证边界为：架构模拟/实验支持所测模型与 chiplet 参数的 latency/energy 改善；结论依赖 die-to-die 带宽、gate 分布和低 batch 假设。 新增代价与回退条件为：细粒度 streaming 减少 off-chip 等待，却增加预测错误、跨 chiplet 同步和硬件专用性；大 batch 数据中心仍可用常规 expert parallel。
<!-- analysis:DA-20260331-12:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-27819:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-27819:end -->
<!-- analysis:DA-20260331-18:start -->
### Heddle: A Distributed Orchestration System for Agentic RL Rollout

agentic RL rollout 按 step 排队时忽略 trajectory 的 tool-wait 与长尾上下文，造成 queueing、interference 和 inflated per-token time。 旧路径在其原约束下仍合理：单机或纯数据并行状态最少、同步语义清晰。 本 family 的设计变化是：Heddle 以 trajectory 为调度对象，联合决定何时继续、放到哪里以及如何组织 tool/LLM execution，使 rollout context 成为显式 runtime state。 其公开验证边界为：分布式 agentic RL workload 的 throughput/尾延迟实验支持所测系统；结果绑定工具延迟、模型、cluster 和训练同步策略。 新增代价与回退条件为：trajectory-aware orchestration 减少长尾，却增加 state migration、fairness 和 stale-policy 管理；同步、短 rollout 仍可使用 step-centric pipeline。
<!-- analysis:DA-20260331-18:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-28239:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-28239:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-26728 | PLATFORM-GATEWAY | books/part-06-ai-infrastructure/62-gateway.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/61-kserve.md#第61章-模型服务声明式控制面：以-kserve-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/63-gpu-scheduler.md#第63章-gpu-scheduler (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26728 | delta:SF-2026-ARXIV-2603-26728 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-26728 |
| SF-2026-ARXIV-2603-26942 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#从单一-monitor-score-到多维、分权的运行证据 (section Ch-owner) | books/part-06-ai-infrastructure/68-logging.md#第68章-logging (section Ch-adjacent); books/part-06-ai-infrastructure/70-cost.md#第70章-cost (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26942 | delta:SF-2026-ARXIV-2603-26942 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-26942 |
| SF-2026-ARXIV-2603-26993 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#mcp-不等于-tool-authorization (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-26993 | delta:SF-2026-ARXIV-2603-26993 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-26993 |
| SF-2026-ARXIV-2603-27116 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#retrieval-object-需要-validity-与-lifecycle (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27116 | delta:SF-2026-ARXIV-2603-27116 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-27116 |
| SF-2026-ARXIV-2603-27138 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#扩展层级 (section Ch-owner) | books/part-05-inference-system/53-kserve-llm.md#第53章-llm-serving-声明式拓扑：以-kserve-为例 (section Ch-adjacent); books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27138 | delta:SF-2026-ARXIV-2603-27138 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-27138 |
| SF-2026-ARXIV-2603-27204 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多跳-delegation-必须保留-human-principal (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27204 | delta:SF-2026-ARXIV-2603-27204 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27204 |
| SF-2026-ARXIV-2603-27287 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27287 | delta:SF-2026-ARXIV-2603-27287 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27287 |
| SF-2026-ARXIV-2603-27299 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#从单点成功到组织级失败 (section Ch-owner) | books/part-05-inference-system/56-inference-scheduling.md#第56章-推理调度 (section Ch-adjacent); books/part-06-ai-infrastructure/58-kubeflow.md#第58章-组合式-ml-platform：以-kubeflow-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27299 | delta:SF-2026-ARXIV-2603-27299 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27299 |
| SF-2026-ARXIV-2603-27355 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#从远程批处理后端到统一生命周期控制面 (section Ch-owner) | books/part-06-ai-infrastructure/72-security.md#canonical-action-与-effect-time-authorization (section Ch-adjacent); books/part-07-agent/74-prompt.md#第74章-prompt (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27355 | delta:SF-2026-ARXIV-2603-27355 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27355 |
| SF-2026-ARXIV-2603-27467 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27467 | delta:SF-2026-ARXIV-2603-27467 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27467 |
| SF-2026-ARXIV-2603-27517 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27517 | delta:SF-2026-ARXIV-2603-27517 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27517 |
| SF-2026-ARXIV-2603-27624 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从-routed-activation-materialization-到-indexed-execution (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27624 | delta:SF-2026-ARXIV-2603-27624 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-27624 |
| SF-2026-ARXIV-2603-27819 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27819 | delta:SF-2026-ARXIV-2603-27819 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-27819 |
| SF-2026-ARXIV-2603-27905 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#resume-是新的状态转换，不是简单读回-checkpoint (section Ch-owner) | books/part-07-agent/83-mcp.md#mcp-不等于-tool-authorization (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-27905 | delta:SF-2026-ARXIV-2603-27905 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-27905 |
| SF-2026-ARXIV-2603-28005 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28005 | delta:SF-2026-ARXIV-2603-28005 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28005 |
| SF-2026-ARXIV-2603-28013 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28013 | delta:SF-2026-ARXIV-2603-28013 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28013 |
| SF-2026-ARXIV-2603-28063 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28063 | delta:SF-2026-ARXIV-2603-28063 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28063 |
| SF-2026-ARXIV-2603-28101 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#federated-tensor-type-定义一轮协议能表达什么 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28101 | delta:SF-2026-ARXIV-2603-28101 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-28101 |
| SF-2026-ARXIV-2603-28166 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28166 | delta:SF-2026-ARXIV-2603-28166 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28166 |
| SF-2026-ARXIV-2603-28168 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28168 | delta:SF-2026-ARXIV-2603-28168 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28168 |
| SF-2026-ARXIV-2603-28239 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28239 | delta:SF-2026-ARXIV-2603-28239 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-28239 |
| SF-2026-ARXIV-2603-28342 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28342 | delta:SF-2026-ARXIV-2603-28342 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28342 |
| SF-2026-ARXIV-2603-28345 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#runtime-优化统计也可能成为跨租户共享状态 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28345 | delta:SF-2026-ARXIV-2603-28345 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28345 |
| SF-2026-ARXIV-2603-28507 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#本章要回答的问题 (section Ch-owner) | books/part-01-worldview/06-why-transformer-changed-the-world.md#第6章-transformer-为什么改变世界 (section Ch-adjacent); books/part-01-worldview/08-why-llms-show-intelligence.md#第8章-大模型为什么会产生智能 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28507 | delta:SF-2026-ARXIV-2603-28507 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28507 |
| SF-2026-ARXIV-2603-28565 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#streaming-vla-必须版本化-observation、buffer-与-control-deadline (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#open-loop-imagination-vs-closed-loop-correction (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28565 | delta:SF-2026-ARXIV-2603-28565 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28565 |
| SF-2026-ARXIV-2603-28590 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28590 | delta:SF-2026-ARXIV-2603-28590 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28590 |
| SF-2026-ARXIV-2603-28622 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#连续-edge-inference-需要跨窗口携带-violation-risk-budget (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28622 | delta:SF-2026-ARXIV-2603-28622 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28622 |
| SF-2026-ARXIV-2603-28650 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-28650 | delta:SF-2026-ARXIV-2603-28650 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-28650 |

<!-- books-review:SF-2026-ARXIV-2603-26728:start -->
### SEAR: Schema-Based Evaluation and Routing for LLM Gateways — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26728:start -->已读 owner `books/part-06-ai-infrastructure/62-gateway.md` 与相邻章节。现有命题：为什么模型服务前还需要 Gateway？它与 Kubernetes Service、KServe controller、EPP 和推理 scheduler 的职责如何分开？重试、限流和路由为什么可能破坏 LLM 请求语义？<!-- existing:SF-2026-ARXIV-2603-26728:end -->

<!-- delta:SF-2026-ARXIV-2603-26728:start -->新证据差异：SEAR 定义跨 context、intent、response issue、quality 与 operational metrics 的 typed relational schema，并以一致性 link 支撑 evaluator 与 router 共享证据。<!-- delta:SF-2026-ARXIV-2603-26728:end -->

边界：只支持 arXiv:2603.26728v1 §3. The SEAR Framework 的机制与 §6.2. Evaluation Performance、§6.3. Routing Performance 的公开 workload；§8. Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-26728:end -->
<!-- books-review:SF-2026-ARXIV-2603-26942:start -->
### The Observability Gap: Why Output-Level Human Feedback Fails for LLM Coding Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26942:start -->已读 owner `books/part-06-ai-infrastructure/69-trace.md` 与相邻章节。现有命题：分布式请求与 Agent workflow 往往包含并行 branch、共享 tool、retry 和异步回调。按时间读取完整 trace 能恢复 “发生过什么”，却容易把靠近失败的 span 误认成原因；只让 LLM 总结所有日志又会把噪声、Prompt 长度和不可 复算判断一起扩大。诊断层可以在 immutable trace 上构建一个派生 dependency graph：<!-- existing:SF-2026-ARXIV-2603-26942:end -->

<!-- delta:SF-2026-ARXIV-2603-26942:start -->新证据差异：earned-autonomy 实验让 agent 从零构建函数库，并对比 output-only feedback 与可观察中间 action/trace；核心增量是把过程状态暴露给 verifier，而非增加模型调用。<!-- delta:SF-2026-ARXIV-2603-26942:end -->

边界：只支持 arXiv:2603.26942v1 §3.1. Experimental Setup 的机制与 §3.2.2. Finding 2: The Observability Gap. 的公开 workload；§4. Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-26942:end -->
<!-- books-review:SF-2026-ARXIV-2603-26993:start -->
### On the Reliability Limits of LLM-Based Multi-Agent Planning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-26993:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-26993:end -->

<!-- delta:SF-2026-ARXIV-2603-26993:start -->新证据差异：论文把多 agent DAG 形式化为有限 delegated decision network，证明在没有新 exogenous signal 时它受同信息的 centralized Bayes decision maker 支配。<!-- delta:SF-2026-ARXIV-2603-26993:end -->

边界：只支持 arXiv:2603.26993v1 §2 Delegated Decision Model、§4 Proposition 6/Theorem 7 的理想 centralized Bayes 上界（同一 exogenous information、bounded loss、no-new-information/conditional-independence 假设）及 §7 Numerical Experiments；不证明固定 compute/latency 的现实单 Agent 可模拟任意 DAG，也不外推开放环境的绝对优劣。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-26993:end -->
<!-- books-review:SF-2026-ARXIV-2603-27116:start -->
### The Price of Meaning: Why Every Semantic Memory System Forgets — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27116:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-27116:end -->

<!-- delta:SF-2026-ARXIV-2603-27116:start -->新证据差异：论文在有限局部维度的 continuous kernel-threshold memory 类中证明：提高语义连续性会不可避免地扩大 interference/false recall，容量与可分性不能同时无限提升。<!-- delta:SF-2026-ARXIV-2603-27116:end -->

边界：只支持 arXiv:2603.27116v1 §Mathematical framework: the no-escape theorem 的机制与 §Forgetting experiments 的公开 workload；§Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-27116:end -->
<!-- books-review:SF-2026-ARXIV-2603-27138:start -->
### ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27138:start -->已读 owner `books/part-05-inference-system/54-gpu-memory.md` 与相邻章节。现有命题：CPU/SSD/off-node cache 扩大总容量，却加入 transfer latency、bandwidth contention 和 consistency。它们把“装不下”改成“何时值得搬”。<!-- existing:SF-2026-ARXIV-2603-27138:end -->

<!-- delta:SF-2026-ARXIV-2603-27138:start -->新证据差异：ScoutAttention 让 CPU 提前一层计算候选 attention，并把结果/状态与 GPU layer pipeline 重叠；offload owner 因而包含 layer-ahead schedule 和一致性。<!-- delta:SF-2026-ARXIV-2603-27138:end -->

边界：只支持 arXiv:2603.27138v1 §3.2–§3.4 的 CPU attention estimation、异步预取与 pipeline integration，以及 §4.3 的作者 workload；不外推生产 SLO、多租户、跨硬件或长期可靠性。最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-27138:end -->
<!-- books-review:SF-2026-ARXIV-2603-27204:start -->
### MalSkills: Detecting Malicious Skills in the Agentic Supply Chain via Neuro-symbolic Reasoning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27204:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这把 authorization 从 prompt/Agent 自述迁移到可核验 provenance chain，但不证明行为正确，也不替代 prompt-injection defense、sandbox 或最小权限。Key/token 生命周期、撤销、重放和 scope composition 都是新增压力；链不完整、过期或验证失败时必须 fail closed，并回退人工授权。<!-- existing:SF-2026-ARXIV-2603-27204:end -->

<!-- delta:SF-2026-ARXIV-2603-27204:start -->新证据差异：MalSkills 先抽取符号 facts，再让神经模型在上下文中推理并用规则约束结论，把 registry admission 建立在多 artifact evidence graph 上。<!-- delta:SF-2026-ARXIV-2603-27204:end -->

边界：只支持 arXiv:2603.27204v1 §4. Methodology 的机制与 §5. Evaluation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27204:end -->
<!-- books-review:SF-2026-ARXIV-2603-27287:start -->
### Uni-World VLA: Interleaved World Modeling and Planning for Autonomous Driving — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27287:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：一个模型能生成逼真视频，是否已经“理解世界”？能够预测下一帧，是否足以支持 planning？World Model 与 simulator、Agent Memory 有何边界？模型在内部 imagined rollout 时，谁保存事实状态，谁保存预测状态，又怎样在新 observation 到来后修正？<!-- existing:SF-2026-ARXIV-2603-27287:end -->

<!-- delta:SF-2026-ARXIV-2603-27287:start -->新证据差异：Uni-World VLA 交替生成 future frame 与 ego trajectory，让每一步 action 重新条件化下一段 world state；world prediction 与 planning 共享可修订状态。<!-- delta:SF-2026-ARXIV-2603-27287:end -->

边界：只支持 arXiv:2603.27287v1 §3 Methods 的机制与 §4.1 Experimental Setup 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27287:end -->
<!-- books-review:SF-2026-ARXIV-2603-27299:start -->
### From Inference Routing to Agent Orchestration: Declarative Policy Compilation with Cross-Layer Verification — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27299:start -->已读 owner `books/part-06-ai-infrastructure/57-what-is-ai-platform.md` 与相邻章节。现有命题：把更多工具链接放进门户只能改善发现成本，不能回答这些问题。工具集合缺少共享 identity、state、policy 和 feedback，最终仍靠人肉传递上下文。<!-- existing:SF-2026-ARXIV-2603-27299:end -->

<!-- delta:SF-2026-ARXIV-2603-27299:start -->新证据差异：Semantic Router DSL 用非图灵完备 declarative source 编译 priority decision tree、orchestration node、NetworkPolicy/Sandbox 和 MCP/A2A gate，并保留结构化 audit trace。<!-- delta:SF-2026-ARXIV-2603-27299:end -->

边界：只支持 arXiv:2603.27299v1 §3.1 Compilation Architecture 的机制与 §A.3 Generated: LangGraph Decision Node (Strategy A) 的公开 workload；§7.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27299:end -->
<!-- books-review:SF-2026-ARXIV-2603-27355:start -->
### LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27355:start -->已读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 与相邻章节。现有命题：混合架构可以让 Kubernetes 统一承载生命周期对象与服务状态，同时把 diskless GPU supercomputer、virtualized commodity infrastructure 和各自调度语义保留为不同 execution substrate。关键不是用 Kubernetes 抹平 HPC，而是让同一个 artifact identity、访问政策、evaluation evidence 和 rollout/rollback contract 穿过训练、注册与在线服务；底层 fabric、batch scheduler、storage 和 failure domain 仍由各自 owner 管理。<!-- existing:SF-2026-ARXIV-2603-27355:end -->

<!-- delta:SF-2026-ARXIV-2603-27355:start -->新证据差异：readiness harness 以统一 scenario schema 聚合 workflow success、policy、groundedness、retrieval、cost 与 p95 latency，并用 Pareto frontier 形成 release gate。<!-- delta:SF-2026-ARXIV-2603-27355:end -->

边界：只支持 arXiv:2603.27355v1 §2 System Overview 的机制与 §5 Experiments 的公开 workload；§8 Limitations and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27355:end -->
<!-- books-review:SF-2026-ARXIV-2603-27467:start -->
### TurboAngle: Near-Lossless KV Cache Compression via Uniform Angle Quantization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27467:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是 新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不 等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。<!-- existing:SF-2026-ARXIV-2603-27467:end -->

<!-- delta:SF-2026-ARXIV-2603-27467:start -->新证据差异：TurboAngle 在 Walsh-Hadamard 域量化角度，并按层分别提高 K/V codebook precision，把 bit allocation 变成模型层级策略。<!-- delta:SF-2026-ARXIV-2603-27467:end -->

边界：只支持 arXiv:2603.27467v1 §3.1 Angular Quantization 的机制与 §4.7 Competitive Comparison 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27467:end -->
<!-- books-review:SF-2026-ARXIV-2603-27517:start -->
### A Security Analysis of the OpenClaw AI Agent Framework — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27517:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-27517:end -->

<!-- delta:SF-2026-ARXIV-2603-27517:start -->新证据差异：论文把 470 条 OpenClaw advisory 按 system layer 与 attack technique 双轴归类，并据此比较 exec policy、gateway、channel、sandbox 与 prompt 的防线责任。<!-- delta:SF-2026-ARXIV-2603-27517:end -->

边界：只支持 arXiv:2603.27517v1 §4 Security Taxonomy 的机制与 §3 Corpus Overview 的公开 workload；§6 Defense Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27517:end -->
<!-- books-review:SF-2026-ARXIV-2603-27624:start -->
### Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27624:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `materialization-free` 不是“无状态”或“零搬运”。大 activation buffer 被 compact indices 取代，而 index construction、dense token-expert map、prefix sum、tile scan 与随机 gather 成为新成本。 在 token 数、Top-K 或 expert 数增加时，metadata 也会扩张；多节点时还必须与 All-to-All、load balance、 failure recovery 和 topology 联合设计。单卡单 MoE layer 的 kernel/activation 结果不能证明完整训练更快， 更不能证明收敛等价。<!-- existing:SF-2026-ARXIV-2603-27624:end -->

<!-- delta:SF-2026-ARXIV-2603-27624:start -->新证据差异：Expert Streaming 在多 chiplet 共享 expert shard，并按预测的 expert trajectory 动态调度传输/执行，把 gate path、placement 与 interconnect schedule 联合优化。<!-- delta:SF-2026-ARXIV-2603-27624:end -->

边界：只支持 arXiv:2603.27624v1 §IV FSE-DP with Micro-Slice Flow、§V MoE Scheduler 的机制与 §VI-C End-to-End Evaluation with Ablation Studies 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；正文已写回，当前等待非作者 post-write semantic audit。
<!-- books-review:SF-2026-ARXIV-2603-27624:end -->
<!-- books-review:SF-2026-ARXIV-2603-27819:start -->
### KVSculpt: KV Cache Compression as Distillation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27819:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：Threshold 使压缩率随输入信息密度变化，recent window 则保护位置和局部依赖。但这不是从 logical compression 自动得到 physical savings：surrogate parameters、score buffer 和不等长 head cache 都是 新状态；现有 PagedAttention/FlashAttention 的规则 block/kernel 可能无法直接执行。FLOP estimate 也不 等于 wall-clock、HBM saving 或端到端 throughput，必须在真实 engine、arrival、batch 与 tail SLO 下验证。<!-- existing:SF-2026-ARXIV-2603-27819:end -->

<!-- delta:SF-2026-ARXIV-2603-27819:start -->新证据差异：KVSculpt 把压缩视为 distillation，直接优化一组更小、非原条目约束的连续 KV，使 future-query output 成为训练目标。<!-- delta:SF-2026-ARXIV-2603-27819:end -->

边界：只支持 arXiv:2603.27819v1 §3.2 Loss Function 的机制与 §5.1 Main Results: Distillation vs. Eviction 的公开 workload；§6 Analysis: Limits of Per-Layer Optimization 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-27819:end -->
<!-- books-review:SF-2026-ARXIV-2603-27905:start -->
### ATLAS-RTC: Closing the Loop on LLM Agent Output with Token-Level Runtime Control — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-27905:start -->已读 owner `books/part-07-agent/84-agent-platform.md` 与相邻章节。现有命题：Agent workload 还改变了“资源需求何时可见”。普通 serving request 通常主要经过模型 runtime； Agent request 会展开为 LLM inference、host orchestration、tool execution 和等待事件，反复跨越 CPU–GPU 边界。不同 execution structure（串行/并行）、orchestration owner（host/model）与 model composition 会产生不同的 burst、critical path 和 residency pattern。若平台只看到平均 CPU/GPU utilization，就会把短时空闲误当作可安全回收容量，或把不同软件角色塞进同一 core pool 而破坏 locality。<!-- existing:SF-2026-ARXIV-2603-27905:end -->

<!-- delta:SF-2026-ARXIV-2603-27905:start -->新证据差异：ATLAS-RTC 在每个 token 监控 contract drift，并用 bias、mask 与 rollback 闭环干预，把生成状态的 commit 权交给 runtime controller。<!-- delta:SF-2026-ARXIV-2603-27905:end -->

边界：只支持 arXiv:2603.27905v1 §3.9 Implementation 的机制与 §Relation to Post-hoc Validation and Repair. 的公开 workload；§Limitations of Drift Detection. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-27905:end -->
<!-- books-review:SF-2026-ARXIV-2603-28005:start -->
### Rethinking Atomic Decomposition for LLM Judges: A Prompt-Controlled Study of Reference-Grounded QA Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28005:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-28005:end -->

<!-- delta:SF-2026-ARXIV-2603-28005:start -->新证据差异：研究冻结输入与 prompt richness，只改变 self-decomposing atomic 与 holistic judge，并跨 prompt variant 做 paired/bootstrap 比较。<!-- delta:SF-2026-ARXIV-2603-28005:end -->

边界：只支持 arXiv:2603.28005v1 §3.1 Judge designs 的机制与 §A Matched Holistic Rubric Rivals Self-Decomposing Atomic Judges for Benchmark-Style Reference-Support Classification 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28005:end -->
<!-- books-review:SF-2026-ARXIV-2603-28013:start -->
### Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Model Safety Tiers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28013:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：交互结束也不是 prompt injection 的自然终点。攻击内容一旦被写入 session context、长期 memory 或可复用 skill，可能在之后的良性 query 才触发；只做当前 response moderation 会把 dormant payload 当成已消失。持久状态因此必须在写入时保存 origin、trust/taint 与 policy generation，在每次读取或执行前按当前 principal、工具权限和目的重新验证，过期或来源不明时 quarantine、降权或删除。<!-- existing:SF-2026-ARXIV-2603-28013:end -->

<!-- delta:SF-2026-ARXIV-2603-28013:start -->新证据差异：kill-chain canary 用加密 token 追踪 EXPOSED→PERSISTED→RELAYED→EXECUTED 四阶段，跨 attack surface 和 defense tier 定位防线在哪一 hop 失效。<!-- delta:SF-2026-ARXIV-2603-28013:end -->

边界：只支持 arXiv:2603.28013v1 §3.2 Kill-Chain Stages and Attack Scenarios 的机制与 §4.1 Exposure Is Universal; Defense Is Downstream 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28013:end -->
<!-- books-review:SF-2026-ARXIV-2603-28063:start -->
### Reward Hacking as Equilibrium under Finite Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28063:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-28063:end -->

<!-- delta:SF-2026-ARXIV-2603-28063:start -->新证据差异：论文在多维质量、有限评测和资源约束下推导 distortion index，并分析 agent tool 增长使 coverage 组合性下降。<!-- delta:SF-2026-ARXIV-2603-28063:end -->

边界：只支持 arXiv:2603.28063v1 §7.1 What This Framework Provides 的机制与 §6.2 Capability-Dependent Evaluation Fidelity 的公开 workload；§5.5 Conditions for Model Failure 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28063:end -->
<!-- books-review:SF-2026-ARXIV-2603-28101:start -->
### Heddle: A Distributed Orchestration System for Agentic RL Rollout — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28101:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：普通 distributed tensor type 描述 device shard；federated computation 还必须区分 client-record axis 与 fixed-dimensional shared state。一轮协议可被约束为 `encode → merge → decode`：客户端只导出编码状态，merge owner 只组合声明的 shared state，decoder 再生成本地结果。类型系统拥有可表达通信边界，transport 不能用任意 payload 绕过它。<!-- existing:SF-2026-ARXIV-2603-28101:end -->

<!-- delta:SF-2026-ARXIV-2603-28101:start -->新证据差异：Heddle 以 trajectory 为调度对象，联合决定何时继续、放到哪里以及如何组织 tool/LLM execution，使 rollout context 成为显式 runtime state。<!-- delta:SF-2026-ARXIV-2603-28101:end -->

边界：只支持 arXiv:2603.28101v1 §4 Trajectory-level Scheduler 的机制与 §7.1 Overall Performance 的公开 workload；§8 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-28101:end -->
<!-- books-review:SF-2026-ARXIV-2603-28166:start -->
### Evaluating Privilege Usage of Agents with Real-World Tools — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28166:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-28166:end -->

<!-- delta:SF-2026-ARXIV-2603-28166:start -->新证据差异：GrantBox 把真实工具接入隔离 sandbox，记录 agent 获得、请求和实际使用的 privilege，按 attack trace 评估越权。<!-- delta:SF-2026-ARXIV-2603-28166:end -->

边界：只支持 arXiv:2603.28166v1 §2. Method 的机制与 §3.3. LLM Security Evaluation 的公开 workload；§4. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28166:end -->
<!-- books-review:SF-2026-ARXIV-2603-28168:start -->
### Leaf-centric Logical Topology Design for OCS-based GPU Clusters — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28168:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：第 35 章已经把一次训练定义成可恢复状态，为什么大模型训练不能简单地“增加 GPU 数量”？当单卡失败时，应该切 batch、矩阵、层、序列、experts，还是切 parameters/gradients/optimizer states？怎样保证切分后的计算仍然代表同一个 optimizer step？<!-- existing:SF-2026-ARXIV-2603-28168:end -->

<!-- delta:SF-2026-ARXIV-2603-28168:start -->新证据差异：leaf-centric 设计约束同一 leaf 流量在 spine 间均衡，并给出避免 polarization 的充分条件与多项式算法。<!-- delta:SF-2026-ARXIV-2603-28168:end -->

边界：只支持 arXiv:2603.28168v1 §III-C How to design intra-Pod architecture 的机制与 §IV-B Performance Analysis 的公开 workload；§VI Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28168:end -->
<!-- books-review:SF-2026-ARXIV-2603-28239:start -->
### A Switch-Centric In-Network Architecture for Accelerating LLM Inference in Shared-Memory Network — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28239:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-28239:end -->

<!-- delta:SF-2026-ARXIV-2603-28239:start -->新证据差异：论文把 collective schedule 移到 switch-centric controller，由网络侧聚合 shared-memory operation，而不是每个 GPU 逐元素驱动。<!-- delta:SF-2026-ARXIV-2603-28239:end -->

边界：只支持 arXiv:2603.28239v1 §3. Design and Implementation 的机制与 §4.5. LLM TP Inference 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-28239:end -->
<!-- books-review:SF-2026-ARXIV-2603-28342:start -->
### Kernel-Smith: A Unified Recipe for Evolutionary Kernel Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28342:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。<!-- existing:SF-2026-ARXIV-2603-28342:end -->

<!-- delta:SF-2026-ARXIV-2603-28342:start -->新证据差异：Kernel-Smith 维护可执行 candidate population，以 compile/correctness/speed feedback 进化，并将高增益正确 revision 转成 step-centric SFT/RL 信号。<!-- delta:SF-2026-ARXIV-2603-28342:end -->

边界：只支持 arXiv:2603.28342v1 §2.3 Advanced Search and Evolution Algorithms 的机制与 §3.3 Evaluation Backends 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28342:end -->
<!-- books-review:SF-2026-ARXIV-2603-28345:start -->
### Reachability Across the NL/PL Boundary: A Taxonomy-Driven Dataflow Model for LLM-Integrated Applications — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28345:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Per-tensor dynamic activation quantization 在单租户 batch 中根据当前输入计算共享 `min/max` 或 scale，可以比固定 scale 更贴合分布；当 batch 混合不同 tenant 时，同一统计却同时读取 victim 输入并改变 adversary 的 quantized logits，形成一条不经过显式 cache 的跨租户 side channel。于是量化 identity 不只包含 bit width 和 kernel，还必须包含 scale granularity、batch composition 与 tenant boundary。<!-- existing:SF-2026-ARXIV-2603-28345:end -->

<!-- delta:SF-2026-ARXIV-2603-28345:start -->新证据差异：PRISM 用 placeholder→output reachability 和信息保留×输出模态的有限 taxonomy，为 LLM call 生成可组合 dataflow predicate。<!-- delta:SF-2026-ARXIV-2603-28345:end -->

边界：只支持 arXiv:2603.28345v1 §4.2.2. Method Comparison 的机制与 §4. Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28345:end -->
<!-- books-review:SF-2026-ARXIV-2603-28507:start -->
### Continued AI Scaling Requires Repeated Efficiency Doublings — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28507:start -->已读 owner `books/part-01-worldview/07-scaling-law.md` 与相邻章节。现有命题：本章的中心命题是：**Scaling Law 是在特定模型族、数据分布、训练方法和观测范围内得到的经验性 power-law regularity。它能描述资源增加时 loss 的统计趋势，并帮助分配有限 compute，但不是能力增长的自然定律，更不是无限扩大的保证书。**<!-- existing:SF-2026-ARXIV-2603-28507:end -->

<!-- delta:SF-2026-ARXIV-2603-28507:start -->新证据差异：论文把能力扩展分解为 compute growth 与连续 efficiency doubling，要求 scaling forecast 显式记录算法/系统效率来源而非单一 FLOP。<!-- delta:SF-2026-ARXIV-2603-28507:end -->

边界：只支持 arXiv:2603.28507v1 §4 A Time-Indexed Efficiency-Doubling Extension 的机制与 §5 The Operational Meaning of Diminishing Returns 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28507:end -->
<!-- books-review:SF-2026-ARXIV-2603-28565:start -->
### StreamingVLA: Streaming Vision-Language-Action Model with Action Flow Matching and Adaptive Early Observation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28565:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：一种 streaming 分解把 context 划成三类不同生命周期的状态：固定 instruction prefix、按 FIFO 更新的 observation history，以及每个 denoising cycle 重置的 dynamic flow suffix。Vision producer 写入带 frontier 的 ring buffer，policy consumer 只读取已经 publish 的 observation version；future-state predictor 只能补偿短时延迟，不能把预测升级为 authoritative environment state。新的 action chunk 必须绑定 observation revision、buffer frontier、policy revision、deadline 与 cancellation token，过期或 prediction error 超界时回退到同步重算、缩短 chunk 或低层 controller。<!-- existing:SF-2026-ARXIV-2603-28565:end -->

<!-- delta:SF-2026-ARXIV-2603-28565:start -->新证据差异：StreamingVLA 用 action flow matching 流式生成 chunk，并按当前状态提前触发下一 observation，使感知与执行重叠且保持可取消的更新。<!-- delta:SF-2026-ARXIV-2603-28565:end -->

边界：只支持 arXiv:2603.28565v1 §4.1 State-based Modeling of Action Flow Matching 的机制与 §5.2 Experimental Results 的公开 workload；§7 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28565:end -->
<!-- books-review:SF-2026-ARXIV-2603-28590:start -->
### MonitorBench: A Comprehensive Benchmark for Chain-of-Thought Monitorability in Large Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28590:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-28590:end -->

<!-- delta:SF-2026-ARXIV-2603-28590:start -->新证据差异：MonitorBench 用显式 decision-critical factor、19 类任务与 stress prompt 测量被监控模型、monitor 模型和任务的条件性交互。<!-- delta:SF-2026-ARXIV-2603-28590:end -->

边界：只支持 arXiv:2603.28590v1 §3.1 Evaluation Design 的机制与 §3.3 Evaluation Metrics 的公开 workload；§4.3 Mechanisms of Failure and Evasion in Monitoring (RQ3) 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28590:end -->
<!-- books-review:SF-2026-ARXIV-2603-28622:start -->
### Trust-Aware Routing for Distributed Generative AI Inference at the Edge — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28622:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：逐请求 admission 在任务相互独立、设备容量稳定且 deadline 只属于当前请求时足够。Continuous edge inference 往往由 视频帧、传感器流或周期任务持续到达；一次延迟会压缩后续窗口，burst history 与设备状态又让风险随时间演化。只看 当前 queue length 或平均 latency，会把“本轮可执行”误当成“未来仍能守住违约上限”。<!-- existing:SF-2026-ARXIV-2603-28622:end -->

<!-- delta:SF-2026-ARXIV-2603-28622:start -->新证据差异：G-TRAC 用 trust-floor pruning 加 risk-bounded shortest path，并由稳定 anchor 保存 reputation、边缘后台同步轻量状态。<!-- delta:SF-2026-ARXIV-2603-28622:end -->

边界：只支持 arXiv:2603.28622v1 §IV G-TRAC Design and Algorithm 的机制与 §IV-D Complexity Analysis 的公开 workload；§VII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28622:end -->
<!-- books-review:SF-2026-ARXIV-2603-28650:start -->
### Information-Theoretic Limits of Safety Verification for Self-Improving Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-28650:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-28650:end -->

<!-- delta:SF-2026-ARXIV-2603-28650:start -->新证据差异：论文给出 classifier TPR 与风险预算的上界，并以 Lipschitz-ball verifier 说明可验证结构如何逃离统计分类限制。<!-- delta:SF-2026-ARXIV-2603-28650:end -->

边界：只支持 arXiv:2603.28650v1 §4.2 Construction: Lipschitz Ball Verifier 的机制与 §7.1 LLM-Scale Mechanism Validation: GPT-2 with LoRA 的公开 workload；§9 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-28650:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260331-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260331-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260331-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260331-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260331/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 8 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 8 项 Books Integration：
- 更新并复核 `books/part-04-training-system/36-distributed-training.md`。
- 更新并复核 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
- 更新并复核 `books/part-05-inference-system/54-gpu-memory.md`。
- 更新并复核 `books/part-06-ai-infrastructure/62-gateway.md`。
- 更新并复核 `books/part-07-agent/77-memory.md`。
- 更新并复核 `books/part-07-agent/82-multi-agent.md`。
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
