# Daily Research — 2026-03-25

**Research Date:** 2026-03-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-24 09:00:00 ～ 2026-03-25 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context Coverage / Evidence / Selection / Books Semantic Audit 与必要的 post-write audit 均已闭合。

## Executive Summary

严格窗口 raw/registered/screened=628/628/628；denominator=21、pre-denominator closures=607。exact-v1 Review complete=21、blocked=0；Integrate 建议=6。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-25 |
| Window End | 2026-03-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260325-AUTHOR-21 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-24T09:00:00+08:00 | 2026-03-25T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 628/628 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 628 | SF-2026-ARXIV-2603-22300;SF-2026-ARXIV-2603-22339;SF-2026-ARXIV-2603-22350;SF-2026-ARXIV-2603-22367;SF-2026-ARXIV-2603-22489;SF-2026-ARXIV-2603-22563;SF-2026-ARXIV-2603-22751;SF-2026-ARXIV-2603-22774;SF-2026-ARXIV-2603-22855;SF-2026-ARXIV-2603-22858;SF-2026-ARXIV-2603-22868;SF-2026-ARXIV-2603-22910;SF-2026-ARXIV-2603-22928;SF-2026-ARXIV-2603-23049;SF-2026-ARXIV-2603-23055;SF-2026-ARXIV-2603-23064;SF-2026-ARXIV-2603-23149;SF-2026-ARXIV-2603-23292;SF-2026-ARXIV-2603-23376;SF-2026-ARXIV-2603-23414;SF-2026-ARXIV-2603-23483 | pages=100; prefixes=00..99; final_cursor=end; registered=628; screened=628; retained=21; closure=607 | 2026-03-25T01:00:00+00:00 | screening-ledger-final.json#sha256=20b8d894338b30b520a4170d62a7df7d70687f6842e6de628efebd30f35e141e; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260325:start -->作者侧已逐项筛选全部 628 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260325:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 628/628 条 title+abstract：作者 retained 12 项均保留，9 个 false-negative family 已完成 exact-v1 Source Review，21 个 recall challenge 被逐项驳回，0 个 withdrawn 只保留 identity/status；reconciled denominator 为 21；Books queue 中 5 个 `Integrate` 被降为 `No Change — Existing Coverage`，3 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260325/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-22300 | arXiv:2603.22300v1 | paper-v1:2603.22300 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22300 | self | — | new_in_window | MODEL-SELF-ATTENTION | Integrate | books-review:SF-2026-ARXIV-2603-22300 | no |
| SF-2026-ARXIV-2603-22339 | arXiv:2603.22339v1 | paper-v1:2603.22339 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22339 | self | — | new_in_window | WORLDVIEW-SCALING-LAW | Integrate | books-review:SF-2026-ARXIV-2603-22339 | no |
| SF-2026-ARXIV-2603-22350 | arXiv:2603.22350v1 | paper-v1:2603.22350 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22350 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22350 | no |
| SF-2026-ARXIV-2603-22367 | arXiv:2603.22367v1 | paper-v1:2603.22367 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22367 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22367 | no |
| SF-2026-ARXIV-2603-22489 | arXiv:2603.22489v1 | paper-v1:2603.22489 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22489 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22489 | no |
| SF-2026-ARXIV-2603-22563 | arXiv:2603.22563v1 | paper-v1:2603.22563 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22563 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22563 | no |
| SF-2026-ARXIV-2603-22751 | arXiv:2603.22751v1 | paper-v1:2603.22751 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22751 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2603-22751 | no |
| SF-2026-ARXIV-2603-22774 | arXiv:2603.22774v1 | paper-v1:2603.22774 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-22774 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-22774 | no |
| SF-2026-ARXIV-2603-22855 | arXiv:2603.22855v1 | paper-v1:2603.22855 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22855 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22855 | no |
| SF-2026-ARXIV-2603-22858 | arXiv:2603.22858v1 | paper-v1:2603.22858 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22858 | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22858 | no |
| SF-2026-ARXIV-2603-22868 | arXiv:2603.22868v1 | paper-v1:2603.22868 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22868 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22868 | no |
| SF-2026-ARXIV-2603-22910 | arXiv:2603.22910v1 | paper-v1:2603.22910 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22910 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22910 | no |
| SF-2026-ARXIV-2603-22928 | arXiv:2603.22928v1 | paper-v1:2603.22928 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-22928 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22928 | no |
| SF-2026-ARXIV-2603-23049 | arXiv:2603.23049v1 | paper-v1:2603.23049 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-23049 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2603-23049 | no |
| SF-2026-ARXIV-2603-23055 | arXiv:2603.23055v1 | paper-v1:2603.23055 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23055 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23055 | no |
| SF-2026-ARXIV-2603-23064 | arXiv:2603.23064v1 | paper-v1:2603.23064 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23064 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23064 | no |
| SF-2026-ARXIV-2603-23149 | arXiv:2603.23149v1 | paper-v1:2603.23149 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-23149 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2603-23149 | no |
| SF-2026-ARXIV-2603-23292 | arXiv:2603.23292v1 | paper-v1:2603.23292 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23292 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23292 | no |
| SF-2026-ARXIV-2603-23376 | arXiv:2603.23376v1 | paper-v1:2603.23376 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23376 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23376 | no |
| SF-2026-ARXIV-2603-23414 | arXiv:2603.23414v1 | paper-v1:2603.23414 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23414 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23414 | no |
| SF-2026-ARXIV-2603-23483 | arXiv:2603.23483v1 | paper-v1:2603.23483 | 2026-W13 | 2026-03-25 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-23483 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23483 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-22300 | RP-797a92df04857a17 | deep | arXiv:2603.22300v1 | SRC-ARXIV@arXiv:2603.22300v1 | HTML — §3 Sparse Feature Attention [facet=method]; https://arxiv.org/html/2603.22300v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22300v1.html; sha256:f4724ca0e7159eb2c6edddae8061bb0a5d088648257db8f3c49b5fb50d131073 | HTML — §4.3 Benchmarking Computation and Memory Efficiency of SFA [facet=evaluation]; https://arxiv.org/html/2603.22300v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22300v1.html; sha256:f4724ca0e7159eb2c6edddae8061bb0a5d088648257db8f3c49b5fb50d131073 | HTML — §7 Conclusion and Limitations [facet=limitations]; https://arxiv.org/html/2603.22300v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22300v1.html; sha256:f4724ca0e7159eb2c6edddae8061bb0a5d088648257db8f3c49b5fb50d131073 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22300v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22300 | complete |
| SF-2026-ARXIV-2603-22339 | RP-59120ba212e68a16 | deep | arXiv:2603.22339v1 | SRC-ARXIV@arXiv:2603.22339v1 | HTML — §8.2 Variable Projection (VPNLS) [facet=method]; https://arxiv.org/html/2603.22339v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22339v1.html; sha256:6d4d4800e4f36ce08ec49d310b281319cb6def3e99f19e4a87a9dd0ba9fe6f58 | HTML — §8.3 Method Comparison (Parameter Recovery) [facet=evaluation]; https://arxiv.org/html/2603.22339v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22339v1.html; sha256:6d4d4800e4f36ce08ec49d310b281319cb6def3e99f19e4a87a9dd0ba9fe6f58 | HTML — §9.1 Limitations [facet=limitations]; https://arxiv.org/html/2603.22339v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22339v1.html; sha256:6d4d4800e4f36ce08ec49d310b281319cb6def3e99f19e4a87a9dd0ba9fe6f58 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22339v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22339 | complete |
| SF-2026-ARXIV-2603-22350 | RP-32f9c1031fe680c6 | standard | arXiv:2603.22350v1 | SRC-ARXIV@arXiv:2603.22350v1 | PDF — §3.2 Session Behavioral Centroid [facet=method]; https://arxiv.org/pdf/2603.22350v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22350v1.pdf.txt; sha256:84a8106a03ec10750bc945319b1fe88b952ff47e7e1cf2759e8b643f404dda23 | PDF — §5.2 Evaluation Protocol [facet=evaluation]; https://arxiv.org/pdf/2603.22350v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22350v1.pdf.txt; sha256:84a8106a03ec10750bc945319b1fe88b952ff47e7e1cf2759e8b643f404dda23 | PDF — §6.3 Limitations [facet=limitations]; https://arxiv.org/pdf/2603.22350v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22350v1.pdf.txt; sha256:84a8106a03ec10750bc945319b1fe88b952ff47e7e1cf2759e8b643f404dda23 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22350v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22350 | complete |
| SF-2026-ARXIV-2603-22367 | RP-cd17e14457c68954 | standard | arXiv:2603.22367v1 | SRC-ARXIV@arXiv:2603.22367v1 | PDF — §III. THE RES ARCHITECTURE [facet=method]; https://arxiv.org/pdf/2603.22367v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22367v1.pdf.txt; sha256:303b1b6bd0d4aed93d2df9c153bfaad20a4c91ec6e5983c1431ca924ce4f064d | PDF — §B. Results [facet=evaluation]; https://arxiv.org/pdf/2603.22367v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22367v1.pdf.txt; sha256:303b1b6bd0d4aed93d2df9c153bfaad20a4c91ec6e5983c1431ca924ce4f064d | PDF — §D. Limitations [facet=limitations]; https://arxiv.org/pdf/2603.22367v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22367v1.pdf.txt; sha256:303b1b6bd0d4aed93d2df9c153bfaad20a4c91ec6e5983c1431ca924ce4f064d | arXiv exact-v1 identity https://arxiv.org/abs/2603.22367v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22367 | complete |
| SF-2026-ARXIV-2603-22489 | RP-29c77098f583a81a | standard | arXiv:2603.22489v1 | SRC-ARXIV@arXiv:2603.22489v1 | HTML — §4. Tool Poisoning Architecture and Attack Flow [facet=method]; https://arxiv.org/html/2603.22489v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22489v1.html; sha256:b0b921d82f6069a3e3e10e9591d4f8627b162ec676c8bd0363da81527fb496ae | HTML — §5.2. Testing Procedure [facet=evaluation]; https://arxiv.org/html/2603.22489v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22489v1.html; sha256:b0b921d82f6069a3e3e10e9591d4f8627b162ec676c8bd0363da81527fb496ae | HTML — §7.4. Threats to validity [facet=limitations]; https://arxiv.org/html/2603.22489v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22489v1.html; sha256:b0b921d82f6069a3e3e10e9591d4f8627b162ec676c8bd0363da81527fb496ae | arXiv exact-v1 identity https://arxiv.org/abs/2603.22489v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22489 | complete |
| SF-2026-ARXIV-2603-22563 | RP-0cd5a071f1cd7d55 | standard | arXiv:2603.22563v1 | SRC-ARXIV@arXiv:2603.22563v1 | HTML — §3.2 Proposed Framework: Private Reward-Based Alignment [facet=method]; https://arxiv.org/html/2603.22563v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22563v1.html; sha256:e7f9d5857f4c574b0ff3a7f7d019c0ec06a01c0d1a65a3dcb27061e32ea5c14f | HTML — §5.1.1 Validation of Theoretical Results [facet=evaluation]; https://arxiv.org/html/2603.22563v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22563v1.html; sha256:e7f9d5857f4c574b0ff3a7f7d019c0ec06a01c0d1a65a3dcb27061e32ea5c14f | HTML — §6 Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.22563v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22563v1.html; sha256:e7f9d5857f4c574b0ff3a7f7d019c0ec06a01c0d1a65a3dcb27061e32ea5c14f | arXiv exact-v1 identity https://arxiv.org/abs/2603.22563v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22563 | complete |
| SF-2026-ARXIV-2603-22751 | RP-e38c924c539c95ba | deep | arXiv:2603.22751v1 | SRC-ARXIV@arXiv:2603.22751v1 | HTML — §3.1–§3.6 CIPL threat model, observable-channel interface and channel-inversion attack [facet=method]; https://arxiv.org/html/2603.22751v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22751v1.html; sha256:bb1ee65e73af3f69c561a03d468d94b14da9de8df9a6dd5cabea4c19361ae8c0 | HTML — §Appendix B Full Main Results [facet=evaluation]; https://arxiv.org/html/2603.22751v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22751v1.html; sha256:bb1ee65e73af3f69c561a03d468d94b14da9de8df9a6dd5cabea4c19361ae8c0 | HTML — §6 Limitations [facet=limitations]; https://arxiv.org/html/2603.22751v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22751v1.html; sha256:bb1ee65e73af3f69c561a03d468d94b14da9de8df9a6dd5cabea4c19361ae8c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22751v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22751 | complete |
| SF-2026-ARXIV-2603-22774 | RP-79f12e9c92f33f22 | deep | arXiv:2603.22774v1 | SRC-ARXIV@arXiv:2603.22774v1 | HTML — §V Understanding the CPU Bottlenecks in Multi-GPU Systems [facet=method]; https://arxiv.org/html/2603.22774v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22774v1.html; sha256:5c5604d8c27ef15af5b3330755efea24c2eb4204c6a5da400d819d2add03cb71 | HTML — §IV CPU Bottleneck in LLM Inference [facet=evaluation]; https://arxiv.org/html/2603.22774v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22774v1.html; sha256:5c5604d8c27ef15af5b3330755efea24c2eb4204c6a5da400d819d2add03cb71 | HTML — §VI-C Limitations [facet=limitations]; https://arxiv.org/html/2603.22774v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22774v1.html; sha256:5c5604d8c27ef15af5b3330755efea24c2eb4204c6a5da400d819d2add03cb71 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22774v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22774 | complete |
| SF-2026-ARXIV-2603-22855 | RP-18dc1bcb4e2f37e8 | standard | arXiv:2603.22855v1 | SRC-ARXIV@arXiv:2603.22855v1 | HTML — §3.2. Algorithmic Design [facet=method]; https://arxiv.org/html/2603.22855v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22855v1.html; sha256:676279bccb014e598851a034bcd47fdcc89ac7f5ef1e0d1ea67fdb9b7b77c4ec | HTML — §5.3. Accelerator Execution Results [facet=evaluation]; https://arxiv.org/html/2603.22855v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22855v1.html; sha256:676279bccb014e598851a034bcd47fdcc89ac7f5ef1e0d1ea67fdb9b7b77c4ec | HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.22855v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22855v1.html; sha256:676279bccb014e598851a034bcd47fdcc89ac7f5ef1e0d1ea67fdb9b7b77c4ec | arXiv exact-v1 identity https://arxiv.org/abs/2603.22855v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22855 | complete |
| SF-2026-ARXIV-2603-22858 | RP-172164b6c741ed7b | standard | arXiv:2603.22858v1 | SRC-ARXIV@arXiv:2603.22858v1 | HTML — §3 Architecture: Dual-View Pheromone Pathway Networks [facet=method]; https://arxiv.org/html/2603.22858v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22858v1.html; sha256:1715fa2cd6c8fffe0b45dbffb268d8c0974b9c2087cd81ebdaff8ff2403c93fb | HTML — §7.5 Results: Aligned Distillation [facet=evaluation]; https://arxiv.org/html/2603.22858v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22858v1.html; sha256:1715fa2cd6c8fffe0b45dbffb268d8c0974b9c2087cd81ebdaff8ff2403c93fb | HTML — §15 Conclusion [facet=limitations]; https://arxiv.org/html/2603.22858v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22858v1.html; sha256:1715fa2cd6c8fffe0b45dbffb268d8c0974b9c2087cd81ebdaff8ff2403c93fb | arXiv exact-v1 identity https://arxiv.org/abs/2603.22858v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22858 | complete |
| SF-2026-ARXIV-2603-22868 | RP-88c61ca19a661077 | standard | arXiv:2603.22868v1 | SRC-ARXIV@arXiv:2603.22868v1 | HTML — §13.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.22868v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22868v1.html; sha256:b790f0957118e59c67d35bbbed9d67a3fe96a0b9ecef7884bccf793b32af4846 | HTML — §5.2 Evaluation Procedure [facet=evaluation]; https://arxiv.org/html/2603.22868v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22868v1.html; sha256:b790f0957118e59c67d35bbbed9d67a3fe96a0b9ecef7884bccf793b32af4846 | HTML — §6.4 Ablation Study: Intent Alignment without Functionality Graph [facet=limitations]; https://arxiv.org/html/2603.22868v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22868v1.html; sha256:b790f0957118e59c67d35bbbed9d67a3fe96a0b9ecef7884bccf793b32af4846 | arXiv exact-v1 identity https://arxiv.org/abs/2603.22868v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22868 | complete |
| SF-2026-ARXIV-2603-22910 | RP-34158703aff8cb5d | standard | arXiv:2603.22910v1 | SRC-ARXIV@arXiv:2603.22910v1 | HTML — §3.1 Overview of EchoKV [facet=method]; https://arxiv.org/html/2603.22910v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22910v1.html; sha256:917231568a688330eb44bc4420c6bae9ad1f008142f92bcde9c94aab6743095b | HTML — §5.5 Ablation of Input Features [facet=evaluation]; https://arxiv.org/html/2603.22910v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22910v1.html; sha256:917231568a688330eb44bc4420c6bae9ad1f008142f92bcde9c94aab6743095b | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.22910v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22910v1.html; sha256:917231568a688330eb44bc4420c6bae9ad1f008142f92bcde9c94aab6743095b | arXiv exact-v1 identity https://arxiv.org/abs/2603.22910v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22910 | complete |
| SF-2026-ARXIV-2603-22928 | RP-b4404a877f4a86eb | standard | arXiv:2603.22928v1 | SRC-ARXIV@arXiv:2603.22928v1 | HTML — §7.1. Formal Methods for Agent Plans and Tool Use [facet=method]; https://arxiv.org/html/2603.22928v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22928v1.html; sha256:156f334273e13d251e078d25209ec15f67eaba6ebb68c697170c40f0a36cf67f | HTML — §6. Evaluation & Metrics for Agentic AI Security [facet=evaluation]; https://arxiv.org/html/2603.22928v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22928v1.html; sha256:156f334273e13d251e078d25209ec15f67eaba6ebb68c697170c40f0a36cf67f | HTML — §9. Conclusion [facet=limitations]; https://arxiv.org/html/2603.22928v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22928v1.html; sha256:156f334273e13d251e078d25209ec15f67eaba6ebb68c697170c40f0a36cf67f | arXiv exact-v1 identity https://arxiv.org/abs/2603.22928v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-22928 | complete |
| SF-2026-ARXIV-2603-23049 | RP-57d4cf12876e33c7 | deep | arXiv:2603.23049v1 | SRC-ARXIV@arXiv:2603.23049v1 | HTML — §4.1. System Overview [facet=method]; https://arxiv.org/html/2603.23049v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23049v1.html; sha256:26cf463e5078a674e6736594ea30aff50d308165fc26b33e9262a3640fe9ce42 | HTML — §6.1. Experimental Methodology [facet=evaluation]; https://arxiv.org/html/2603.23049v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23049v1.html; sha256:26cf463e5078a674e6736594ea30aff50d308165fc26b33e9262a3640fe9ce42 | HTML — §8. Conclusion [facet=limitations]; https://arxiv.org/html/2603.23049v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23049v1.html; sha256:26cf463e5078a674e6736594ea30aff50d308165fc26b33e9262a3640fe9ce42 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23049v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23049 | complete |
| SF-2026-ARXIV-2603-23055 | RP-2c2cf6150a3336ff | standard | arXiv:2603.23055v1 | SRC-ARXIV@arXiv:2603.23055v1 | HTML — §Appendix F Alternative Implementation of PS-DME via Berk–Jones CDF Bands [facet=method]; https://arxiv.org/html/2603.23055v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23055v1.html; sha256:d7cd479846a9b0968cf9c304152b2bc6bddeac006380596717762b1a31bf0306 | HTML — §3.1 Sample-Splitting Distributional Model Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23055v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23055v1.html; sha256:d7cd479846a9b0968cf9c304152b2bc6bddeac006380596717762b1a31bf0306 | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.23055v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23055v1.html; sha256:d7cd479846a9b0968cf9c304152b2bc6bddeac006380596717762b1a31bf0306 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23055v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23055 | complete |
| SF-2026-ARXIV-2603-23064 | RP-a41c4eeab002e974 | standard | arXiv:2603.23064v1 | SRC-ARXIV@arXiv:2603.23064v1 | HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.23064v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23064v1.html; sha256:087b2b6f045236d13b16247053e330620b6d3d439ba44a61f7966ff606b29bc2 | HTML — §5 Case Studies and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23064v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23064v1.html; sha256:087b2b6f045236d13b16247053e330620b6d3d439ba44a61f7966ff606b29bc2 | HTML — §7.2 Limitations [facet=limitations]; https://arxiv.org/html/2603.23064v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23064v1.html; sha256:087b2b6f045236d13b16247053e330620b6d3d439ba44a61f7966ff606b29bc2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23064v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23064 | complete |
| SF-2026-ARXIV-2603-23149 | RP-07693a963c060a99 | deep | arXiv:2603.23149v1 | SRC-ARXIV@arXiv:2603.23149v1 | HTML — §3 Distilled Language Action World Model [facet=method]; https://arxiv.org/html/2603.23149v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23149v1.html; sha256:273e0b7daf8b97759d309718f254d4f386629ced10f672fed55e700025077722 | HTML — §4.4 Proactive Policy Steering and Inference Latency [facet=evaluation]; https://arxiv.org/html/2603.23149v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23149v1.html; sha256:273e0b7daf8b97759d309718f254d4f386629ced10f672fed55e700025077722 | HTML — §5 Limitations [facet=limitations]; https://arxiv.org/html/2603.23149v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23149v1.html; sha256:273e0b7daf8b97759d309718f254d4f386629ced10f672fed55e700025077722 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23149v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23149 | complete |
| SF-2026-ARXIV-2603-23292 | RP-4bdbc13f3ab65559 | standard | arXiv:2603.23292v1 | SRC-ARXIV@arXiv:2603.23292v1 | HTML — §3.2 Design principles [facet=method]; https://arxiv.org/html/2603.23292v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23292v1.html; sha256:96b1e376fae37631b3fd505cbf86f36ffd13843f664c1f561cf42fb081962c9d | HTML — §C.4 Evaluation scale [facet=evaluation]; https://arxiv.org/html/2603.23292v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23292v1.html; sha256:96b1e376fae37631b3fd505cbf86f36ffd13843f664c1f561cf42fb081962c9d | HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.23292v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23292v1.html; sha256:96b1e376fae37631b3fd505cbf86f36ffd13843f664c1f561cf42fb081962c9d | arXiv exact-v1 identity https://arxiv.org/abs/2603.23292v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23292 | complete |
| SF-2026-ARXIV-2603-23376 | RP-1a11cd9c4286c04f | standard | arXiv:2603.23376v1 | SRC-ARXIV@arXiv:2603.23376v1 | HTML — §3.2 Physical Preference Alignment [facet=method]; https://arxiv.org/html/2603.23376v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23376v1.html; sha256:35ddec198b2bf6a587e2cf3b25e17d1f1d71d64a3e3aaa4cfce4d814c3067033 | HTML — §5.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.23376v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23376v1.html; sha256:35ddec198b2bf6a587e2cf3b25e17d1f1d71d64a3e3aaa4cfce4d814c3067033 | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.23376v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23376v1.html; sha256:35ddec198b2bf6a587e2cf3b25e17d1f1d71d64a3e3aaa4cfce4d814c3067033 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23376v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23376 | complete |
| SF-2026-ARXIV-2603-23414 | RP-4489b13719f83e1e | standard | arXiv:2603.23414v1 | SRC-ARXIV@arXiv:2603.23414v1 | HTML — §4.4.1 Throughput of Different Methods [facet=method]; https://arxiv.org/html/2603.23414v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23414v1.html; sha256:e48bad22f24ac9a7c4dfbbf44630bfd09f81b113aab744c51167faeb7ad4a0e5 | HTML — §4.2 Results on Logic Problems [facet=evaluation]; https://arxiv.org/html/2603.23414v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23414v1.html; sha256:e48bad22f24ac9a7c4dfbbf44630bfd09f81b113aab744c51167faeb7ad4a0e5 | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.23414v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23414v1.html; sha256:e48bad22f24ac9a7c4dfbbf44630bfd09f81b113aab744c51167faeb7ad4a0e5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.23414v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23414 | complete |
| SF-2026-ARXIV-2603-23483 | RP-4a8a1682bfe02bb5 | standard | arXiv:2603.23483v1 | SRC-ARXIV@arXiv:2603.23483v1 | HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23483v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23483v1.html; sha256:8862f2365c98d199b9729423c8d0d2139e2dee9f487187c548775c637a2f714e | HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.23483v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23483v1.html; sha256:8862f2365c98d199b9729423c8d0d2139e2dee9f487187c548775c637a2f714e | HTML — §5 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.23483v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23483v1.html; sha256:8862f2365c98d199b9729423c8d0d2139e2dee9f487187c548775c637a2f714e | arXiv exact-v1 identity https://arxiv.org/abs/2603.23483v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-23483 | complete |

### Source Reviews

### Scaling Attention via Feature Sparsity

<!-- review:SF-2026-ARXIV-2603-22300:start -->
**问题**：长上下文 attention 过去主要沿 sequence 轴做窗口、近似或 token pruning，代价是直接丢掉一部分 token 关系。

**旧路径为何合理**：dense attention 保留完整 token 交互。

**约束变化与机制**：SFA 改为稀疏化 query/key 的 feature 维，并用 IO-aware FlashSFA kernel 执行；控制权从 token admission 转到 feature-code 与 kernel layout。

**State / data / control owner**：`MODEL-SELF-ATTENTION` 负责 attention feature 的选择、稀疏化与精度边界；定位证据为 `HTML — §3 Sparse Feature Attention [facet=method]; https://arxiv.org/html/2603.22300v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22300v1.html; sha256:f4724ca0e7159eb2c6edddae8061bb0a5d088648257db8f3c49b5fb50d131073`。

**Evaluation contract 与未证明部分**：exact-v1 比较预训练与长序列效率，能支持所测模型和 kernel 上的 accuracy/throughput 边界；不能证明任意任务都比 sequence sparsity 更稳。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.3 Benchmarking Computation and Memory Efficiency of SFA [facet=evaluation]; https://arxiv.org/html/2603.22300v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22300v1.html; sha256:f4724ca0e7159eb2c6edddae8061bb0a5d088648257db8f3c49b5fb50d131073`。

**Trade-off / failure / coexistence**：feature 编码和专用 kernel 增加实现复杂度，稀疏码碰撞会损伤全局关系；中短序列或缺少 kernel 支持时 dense attention 仍合理。

<!-- claim:SF-2026-ARXIV-2603-22300:start -->**Claim Boundary**：只支持 arXiv:2603.22300v1 §3 Sparse Feature Attention 的机制与 §4.3 Benchmarking Computation and Memory Efficiency of SFA 的公开 workload；§7 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22300:end -->
<!-- review:SF-2026-ARXIV-2603-22300:end -->
### Problems with Chinchilla Approach 2: Systematic Biases in IsoFLOP Parabola Fits

<!-- review:SF-2026-ARXIV-2603-22339:start -->
**问题**：IsoFLOP 二次曲线拟合之所以流行，是因为它用少量定算力实验即可估计 compute-optimal 参数/数据配比。

**旧路径为何合理**：按单次拟合曲线外推最省实验成本。

**约束变化与机制**：论文证明非对称 loss surface、偏心采样与有限 grid 会给 Approach 2 引入结构性偏差，并以直接 surface fit/variable projection 恢复五个参数的联合估计。

**State / data / control owner**：`WORLDVIEW-SCALING-LAW` 负责 scaling experiment 的数据、拟合与决策证据；定位证据为 `HTML — §8.2 Variable Projection (VPNLS) [facet=method]; https://arxiv.org/html/2603.22339v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22339v1.html; sha256:6d4d4800e4f36ce08ec49d310b281319cb6def3e99f19e4a87a9dd0ba9fe6f58`。

**Evaluation contract 与未证明部分**：noise-free synthetic、公开 Llama 3 IsoFLOP 数据和方法对比支持偏差方向与所报成本估计；美元换算仍依赖 MFU、价格和外推假设。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §8.3 Method Comparison (Parameter Recovery) [facet=evaluation]; https://arxiv.org/html/2603.22339v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22339v1.html; sha256:6d4d4800e4f36ce08ec49d310b281319cb6def3e99f19e4a87a9dd0ba9fe6f58`。

**Trade-off / failure / coexistence**：直接拟合减少系统偏差，却对初始化、数值条件和实验设计要求更高；局部、近对称且只作插值时简化抛物线仍可作为廉价诊断。

<!-- claim:SF-2026-ARXIV-2603-22339:start -->**Claim Boundary**：只支持 arXiv:2603.22339v1 §8.2 Variable Projection (VPNLS) 的机制与 §8.3 Method Comparison (Parameter Recovery) 的公开 workload；§9.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22339:end -->
<!-- review:SF-2026-ARXIV-2603-22339:end -->
### Session Risk Memory (SRM): Temporal Authorization for Deterministic Pre-Execution Safety Gates

<!-- review:SF-2026-ARXIV-2603-22350:start -->
**问题**：逐 action 的 deterministic gate 能清楚授权单步副作用，却看不到多个合规动作累积成的数据外泄轨迹。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SRM 在 gate 外维护 session semantic centroid 与基线扣除后的 EMA risk，把历史状态交给确定性 pre-execution decision，而不是让 LLM 自报安全。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `PDF — §3.2 Session Behavioral Centroid [facet=method]; https://arxiv.org/pdf/2603.22350v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22350v1.pdf.txt; sha256:84a8106a03ec10750bc945319b1fe88b952ff47e7e1cf2759e8b643f404dda23`。

**Evaluation contract 与未证明部分**：80-session 多轮 benchmark 支持所测阈值下的 trajectory discrimination 与 false-positive 抑制；未证明 centroid 能覆盖语义伪装或长期分布漂移。 未披露的字段保持 `Not Disclosed`，具体定位为 `PDF — §5.2 Evaluation Protocol [facet=evaluation]; https://arxiv.org/pdf/2603.22350v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22350v1.pdf.txt; sha256:84a8106a03ec10750bc945319b1fe88b952ff47e7e1cf2759e8b643f404dda23`。

**Trade-off / failure / coexistence**：跨 turn 状态提高检测面，也引入阈值校准、误拒和 session reset/poisoning 风险；真正无状态、低副作用调用仍可只用单步 gate。

<!-- claim:SF-2026-ARXIV-2603-22350:start -->**Claim Boundary**：只支持 arXiv:2603.22350v1 §3.2 Session Behavioral Centroid 的机制与 §5.2 Evaluation Protocol 的公开 workload；§6.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22350:end -->
<!-- review:SF-2026-ARXIV-2603-22350:end -->
### Reasoner-Executor-Synthesizer: Scalable Agentic Architecture with Static O(1) Context Window

<!-- review:SF-2026-ARXIV-2603-22367:start -->
**问题**：把检索原文持续塞回上下文会让 token 成本和可生成陈述面随数据集增长。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：RES 把意图解析、确定性检索聚合和叙述生成拆开；Executor 只向 Synthesizer 交付固定尺寸统计摘要，使 raw record 不进入生成状态。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `PDF — §III. THE RES ARCHITECTURE [facet=method]; https://arxiv.org/pdf/2603.22367v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22367v1.pdf.txt; sha256:303b1b6bd0d4aed93d2df9c153bfaad20a4c91ec6e5983c1431ca924ce4f064d`。

**Evaluation contract 与未证明部分**：Crossref-backed ScholarSearch 的 100 次运行支持所测数据规模下的 O(1) token 输入；它不证明固定摘要足以回答任意开放问题。 未披露的字段保持 `Not Disclosed`，具体定位为 `PDF — §B. Results [facet=evaluation]; https://arxiv.org/pdf/2603.22367v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22367v1.pdf.txt; sha256:303b1b6bd0d4aed93d2df9c153bfaad20a4c91ec6e5983c1431ca924ce4f064d`。

**Trade-off / failure / coexistence**：固定摘要压低成本与数据幻觉面，却牺牲逐条证据可见性；需要引用原文或开放探索时 RAG 仍必要。

<!-- claim:SF-2026-ARXIV-2603-22367:start -->**Claim Boundary**：只支持 arXiv:2603.22367v1 §III. THE RES ARCHITECTURE 的机制与 §B. Results 的公开 workload；§D. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22367:end -->
<!-- review:SF-2026-ARXIV-2603-22367:end -->
### Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning

<!-- review:SF-2026-ARXIV-2603-22489:start -->
**问题**：MCP 早期实现常把 server 注册、tool description 与执行授权视为同一信任边界，客户端因此会直接消费被污染的 capability metadata。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：论文用 STRIDE/DREAD 分解 host、client、LLM、server、data store 与 authorization server，再把注册校验、decision-path 检查、runtime monitoring 和用户透明度组成分层防线。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `HTML — §4. Tool Poisoning Architecture and Attack Flow [facet=method]; https://arxiv.org/html/2603.22489v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22489v1.html; sha256:b0b921d82f6069a3e3e10e9591d4f8627b162ec676c8bd0363da81527fb496ae`。

**Evaluation contract 与未证明部分**：五个客户端上的四类 tool-poisoning 演示能证明这些实现的具体暴露面；样本规模与版本有限，不能代表 MCP 协议或全部客户端的普遍漏洞率。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.2. Testing Procedure [facet=evaluation]; https://arxiv.org/html/2603.22489v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22489v1.html; sha256:b0b921d82f6069a3e3e10e9591d4f8627b162ec676c8bd0363da81527fb496ae`。

**Trade-off / failure / coexistence**：分层检查降低单点失守，却增加兼容、延迟和策略维护成本；可信单 server 环境仍可采用更薄的 admission，但 execution authorization 不能省略。

<!-- claim:SF-2026-ARXIV-2603-22489:start -->**Claim Boundary**：只支持 arXiv:2603.22489v1 §4. Tool Poisoning Architecture and Attack Flow 的机制与 §5.2. Testing Procedure 的公开 workload；§7.4. Threats to validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22489:end -->
<!-- review:SF-2026-ARXIV-2603-22489:end -->
### Privacy-Preserving Reinforcement Learning from Human Feedback via Decoupled Reward Modeling

<!-- review:SF-2026-ARXIV-2603-22563:start -->
**问题**：在整条 RLHF pipeline 上统一施加 DP 会把隐私噪声扩散到策略优化并浪费已公开的训练信号。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：该方案只在敏感偏好进入 reward learning 时建立 DP 边界，再让 policy 从私有 reward model 学习；隐私 owner 从最终策略更新前移到奖励数据接口。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `HTML — §3.2 Proposed Framework: Private Reward-Based Alignment [facet=method]; https://arxiv.org/html/2603.22563v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22563v1.html; sha256:e7f9d5857f4c574b0ff3a7f7d019c0ec06a01c0d1a65a3dcb27061e32ea5c14f`。

**Evaluation contract 与未证明部分**：理论 upper/lower bound 与 HH-RLHF/Gemma-2B-IT 实验支持特定预算下的额外误差项；不证明 reward model 输出不会泄漏未建模属性。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.1.1 Validation of Theoretical Results [facet=evaluation]; https://arxiv.org/html/2603.22563v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22563v1.html; sha256:e7f9d5857f4c574b0ff3a7f7d019c0ec06a01c0d1a65a3dcb27061e32ea5c14f`。

**Trade-off / failure / coexistence**：解耦降低 policy 侧噪声，却把风险集中到 reward model 版本、访问与再利用；无敏感偏好时普通 RLHF 更简单。

<!-- claim:SF-2026-ARXIV-2603-22563:start -->**Claim Boundary**：只支持 arXiv:2603.22563v1 §3.2 Proposed Framework: Private Reward-Based Alignment 的机制与 §5.1.1 Validation of Theoretical Results 的公开 workload；§6 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22563:end -->
<!-- review:SF-2026-ARXIV-2603-22563:end -->
### Observable Channels, Not Just Storage: Evaluating Privacy Leakage in LLM Agent Pipelines

<!-- review:SF-2026-ARXIV-2603-22751:start -->
**问题**：只分别审计 memory、retrieval 或 tool storage 会漏掉内部依赖如何经不同可观察输出被攻击者反演。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：CIPL 把目标属性、agent pipeline、可观察 channel 与 inversion attacker 统一成同一测量接口；privacy owner 从某个存储组件扩展为端到端 observable data flow。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §3.1–§3.6 CIPL threat model, observable-channel interface and channel-inversion attack [facet=method]; https://arxiv.org/html/2603.22751v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22751v1.html; sha256:bb1ee65e73af3f69c561a03d468d94b14da9de8df9a6dd5cabea4c19361ae8c0`。

**Evaluation contract 与未证明部分**：跨多类 agent pipeline 的实验支持该接口比较泄漏路径的能力；结果绑定攻击者观察权限、目标属性与 evaluator，不能给出通用隐私保证。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §Appendix B Full Main Results [facet=evaluation]; https://arxiv.org/html/2603.22751v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22751v1.html; sha256:bb1ee65e73af3f69c561a03d468d94b14da9de8df9a6dd5cabea4c19361ae8c0`。

**Trade-off / failure / coexistence**：channel-level 测量提高可比性，却需要枚举实际观察面且可能遗漏组合通道；隔离明确的单组件仍可先做局部测试，但不能据此宣称端到端安全。

<!-- claim:SF-2026-ARXIV-2603-22751:start -->**Claim Boundary**：只支持 arXiv:2603.22751v1 §3.1–§3.6 的 threat model、observable-channel measurement interface 与 channel-inversion attack，以及 Appendix B 的作者实验；不把该受限 evaluation contract 外推为通用隐私保证、生产 SLO、多租户或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22751:end -->
<!-- review:SF-2026-ARXIV-2603-22751:end -->
### Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference

<!-- review:SF-2026-ARXIV-2603-22774:start -->
**问题**：多 GPU serving 通常把慢吞吐归因于 GPU 算力或互联，默认 host CPU 只承担可忽略的调度工作。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：论文把 kernel launch、collective progress、tokenization 与 agentic host work 分解到 CPU allocation，显示 CPU 是维持 GPU feed 的控制面资源。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `HTML — §V Understanding the CPU Bottlenecks in Multi-GPU Systems [facet=method]; https://arxiv.org/html/2603.22774v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22774v1.html; sha256:5c5604d8c27ef15af5b3330755efea24c2eb4204c6a5da400d819d2add03cb71`。

**Evaluation contract 与未证明部分**：多 GPU serving 配置下的 profiling 支持 CPU 配额不足会造成 launch delay、通信停顿与 GPU idle；具体幅度绑定模型、框架、CPU/GPU 拓扑和请求混合。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §IV CPU Bottleneck in LLM Inference [facet=evaluation]; https://arxiv.org/html/2603.22774v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22774v1.html; sha256:5c5604d8c27ef15af5b3330755efea24c2eb4204c6a5da400d819d2add03cb71`。

**Trade-off / failure / coexistence**：增加 CPU 或隔离 host work 可恢复利用率，但提高成本并可能把瓶颈移到内存/互联；GPU 已饱和或 host path 很薄时继续加 CPU 无益。

<!-- claim:SF-2026-ARXIV-2603-22774:start -->**Claim Boundary**：只支持 arXiv:2603.22774v1 §V Understanding the CPU Bottlenecks in Multi-GPU Systems 的机制与 §IV CPU Bottleneck in LLM Inference 的公开 workload；§VI-C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22774:end -->
<!-- review:SF-2026-ARXIV-2603-22774:end -->
### TorR: Towards Brain-Inspired Task-Oriented Reasoning via Cache-Oriented Algorithm-Architecture Co-design

<!-- review:SF-2026-ARXIV-2603-22855:start -->
**问题**：edge 视觉推理中 dense CLIP window alignment 会同时受算力、存储流量和实时 deadline 约束。

**旧路径为何合理**：通用算子图优先可移植性和实现简单。

**约束变化与机制**：TorR 用 HDC associative reasoner、query cache、bit-delta update 与 load-gated bypass，在控制器中按负载选择 full/delta/bypass path。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel、precision、layout 与执行计划 owner；定位证据为 `HTML — §3.2. Algorithmic Design [facet=method]; https://arxiv.org/html/2603.22855v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22855v1.html; sha256:676279bccb014e598851a034bcd47fdcc89ac7f5ef1e0d1ea67fdb9b7b77c4ec`。

**Evaluation contract 与未证明部分**：28nm synthesis 与 cycle-accurate simulation 支持论文配置的能耗、延迟和 AP 折中；不是流片结果，也不能外推其他传感器与工艺。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.3. Accelerator Execution Results [facet=evaluation]; https://arxiv.org/html/2603.22855v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22855v1.html; sha256:676279bccb014e598851a034bcd47fdcc89ac7f5ef1e0d1ea67fdb9b7b77c4ec`。

**Trade-off / failure / coexistence**：缓存和多路径换取实时性，却新增阈值漂移、复用错误与专用硬件成本；负载低或精度优先时 dense path 仍成立。

<!-- claim:SF-2026-ARXIV-2603-22855:start -->**Claim Boundary**：只支持 arXiv:2603.22855v1 §3.2. Algorithmic Design 的机制与 §5.3. Accelerator Execution Results 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22855:end -->
<!-- review:SF-2026-ARXIV-2603-22855:end -->
### The Coordinate System Problem in Persistent Structural Memory for Neural Architectures

<!-- review:SF-2026-ARXIV-2603-22858:start -->
**问题**：把 learned structural memory 与主模型共同训练最自然，因为表示和 memory address 可以共同适配任务。

**旧路径为何合理**：全量 attention 保留任意 token 交互，在中短序列上最直接。

**约束变化与机制**：多轮 DPPN 实验暴露跨 run coordinate drift：persistent state 若依赖可旋转的 learned slot/embedding，transfer 时没有稳定身份；固定坐标只解决必要条件，仍需合适的写入与读出机制。

**State / data / control owner**：`MODEL-LONG-CONTEXT` 负责 上下文选择、层次化表示和可访问记忆的语义边界；定位证据为 `HTML — §3 Architecture: Dual-View Pheromone Pathway Networks [facet=method]; https://arxiv.org/html/2603.22858v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22858v1.html; sha256:1715fa2cd6c8fffe0b45dbffb268d8c0974b9c2087cd81ebdaff8ff2403c93fb`。

**Evaluation contract 与未证明部分**：五组实验、多个 seed 与 transfer target 支持 saturation、coordinate mismatch 和固定坐标的诊断；结果主要是受限架构上的正反例，不证明一种通用 memory 实现。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §7.5 Results: Aligned Distillation [facet=evaluation]; https://arxiv.org/html/2603.22858v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22858v1.html; sha256:1715fa2cd6c8fffe0b45dbffb268d8c0974b9c2087cd81ebdaff8ff2403c93fb`。

**Trade-off / failure / coexistence**：固定坐标提高可对齐性，却限制表示适配并可能损失任务性能；单任务、不跨版本转移的 memory 仍可使用共同学习的坐标。

<!-- claim:SF-2026-ARXIV-2603-22858:start -->**Claim Boundary**：只支持 arXiv:2603.22858v1 §3 Architecture: Dual-View Pheromone Pathway Networks 的机制与 §7.5 Results: Aligned Distillation 的公开 workload；§15 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22858:end -->
<!-- review:SF-2026-ARXIV-2603-22858:end -->
### Agent-Sentry: Bounding LLM Agents via Execution Provenance

<!-- review:SF-2026-ARXIV-2603-22868:start -->
**问题**：静态 allowlist 适合已知工具图，但开放 agent 的实际 action path 由 prompt、tool result 与 runtime state 动态产生。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：Agent-Sentry 从合法执行学习 provenance-conditioned behavior bound，在 action 落界前检查其来源与轨迹，而不是只过滤最终文本。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §13.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.22868v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22868v1.html; sha256:b790f0957118e59c67d35bbbed9d67a3fe96a0b9ecef7884bccf793b32af4846`。

**Evaluation contract 与未证明部分**：公开实验支持所测任务/攻击下对异常 action 的区分；学习到的 benign bound 不等同于授权真值，也未覆盖部署后的合法行为漂移。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.2 Evaluation Procedure [facet=evaluation]; https://arxiv.org/html/2603.22868v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22868v1.html; sha256:b790f0957118e59c67d35bbbed9d67a3fe96a0b9ecef7884bccf793b32af4846`。

**Trade-off / failure / coexistence**：provenance bound 增加 runtime 检查与冷启动数据需求，且可能误拒新路径；静态、低变化 workflow 仍应优先显式 policy/allowlist。

<!-- claim:SF-2026-ARXIV-2603-22868:start -->**Claim Boundary**：只支持 arXiv:2603.22868v1 §13.1 Architecture Overview 的机制与 §5.2 Evaluation Procedure 的公开 workload；§6.4 Ablation Study: Intent Alignment without Functionality Graph 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22868:end -->
<!-- review:SF-2026-ARXIV-2603-22868:end -->
### EchoKV: Efficient KV Cache Compression via Similarity-Based Reconstruction

<!-- review:SF-2026-ARXIV-2603-22910:start -->
**问题**：低秩 KV 压缩常把投影写进模型结构，部署后难以在显存充足时无损回到标准 full-cache 路径。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：EchoKV 保留 full-cache 语义，在压力出现时丢弃可重建分量并用轻量网络恢复，使 compression policy 成为 runtime 可切换状态。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `HTML — §3.1 Overview of EchoKV [facet=method]; https://arxiv.org/html/2603.22910v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22910v1.html; sha256:917231568a688330eb44bc4420c6bae9ad1f008142f92bcde9c94aab6743095b`。

**Evaluation contract 与未证明部分**：LongBench 与所测模型上的质量/内存结果支持按需切换；不能证明重建网络对其他架构、层或分布外长上下文稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.5 Ablation of Input Features [facet=evaluation]; https://arxiv.org/html/2603.22910v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22910v1.html; sha256:917231568a688330eb44bc4420c6bae9ad1f008142f92bcde9c94aab6743095b`。

**Trade-off / failure / coexistence**：可切换性减少永久架构绑定，却增加重建 compute、模型专属训练和切换一致性；容量充足、低延迟场景仍应保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-22910:start -->**Claim Boundary**：只支持 arXiv:2603.22910v1 §3.1 Overview of EchoKV 的机制与 §5.5 Ablation of Input Features 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22910:end -->
<!-- review:SF-2026-ARXIV-2603-22910:end -->
### SoK: The Attack Surface of Agentic AI - Tools and Autonomy

<!-- review:SF-2026-ARXIV-2603-22928:start -->
**问题**：LLM 一旦接入 RAG、工具和多 agent，攻击不再停留在输入文本，而会沿知识、权限和协作边传播。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SoK 把 prompt、knowledge base、tool/plugin 与 cross-agent 组合成显式 trust-boundary taxonomy，并将 unsafe action 与 privilege escalation 纳入系统评估。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §7.1. Formal Methods for Agent Plans and Tool Use [facet=method]; https://arxiv.org/html/2603.22928v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22928v1.html; sha256:156f334273e13d251e078d25209ec15f67eaba6ebb68c697170c40f0a36cf67f`。

**Evaluation contract 与未证明部分**：证据是 2023–2025 研究与标准的系统化归纳，可支持威胁模型和控制清单；不能证明任一 defense 在生产中达到固定有效率。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §6. Evaluation & Metrics for Agentic AI Security [facet=evaluation]; https://arxiv.org/html/2603.22928v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.22928v1.html; sha256:156f334273e13d251e078d25209ec15f67eaba6ebb68c697170c40f0a36cf67f`。

**Trade-off / failure / coexistence**：统一 taxonomy 提高完整性却可能随新协议过时；封闭、只读单 agent 可使用更窄威胁模型。

<!-- claim:SF-2026-ARXIV-2603-22928:start -->**Claim Boundary**：只支持 arXiv:2603.22928v1 §7.1. Formal Methods for Agent Plans and Tool Use 的机制与 §6. Evaluation & Metrics for Agentic AI Security 的公开 workload；§9. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-22928:end -->
<!-- review:SF-2026-ARXIV-2603-22928:end -->
### PCR: A Prefetch-Enhanced Cache Reuse System for Low-Latency RAG Serving

<!-- review:SF-2026-ARXIV-2603-23049:start -->
**问题**：RAG prefix KV reuse 能避免重复 prefill，但从缓存读取大前缀仍会落在请求关键路径并产生新的 I/O 等待。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：PCR 用 prefix tree 管理可复用身份，按层把 cache transfer 与 compute 重叠，并根据队列提前 prefetch；reuse owner 因而同时包含命中、传输与失效状态。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `HTML — §4.1. System Overview [facet=method]; https://arxiv.org/html/2603.23049v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23049v1.html; sha256:26cf463e5078a674e6736594ea30aff50d308165fc26b33e9262a3640fe9ce42`。

**Evaluation contract 与未证明部分**：RAG serving 实验支持所测命中分布下的 latency 降低；收益依赖文档复用、队列可预测性、cache 容量和互联带宽。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §6.1. Experimental Methodology [facet=evaluation]; https://arxiv.org/html/2603.23049v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23049v1.html; sha256:26cf463e5078a674e6736594ea30aff50d308165fc26b33e9262a3640fe9ce42`。

**Trade-off / failure / coexistence**：prefetch 隐藏 I/O，却会浪费带宽、放大 stale cache 和公平性问题；低复用或突发 query 下按需 prefill 更简单。

<!-- claim:SF-2026-ARXIV-2603-23049:start -->**Claim Boundary**：只支持 arXiv:2603.23049v1 §4.1. System Overview 的机制与 §6.1. Experimental Methodology 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23049:end -->
<!-- review:SF-2026-ARXIV-2603-23049:end -->
### Post-Selection Distributional Model Evaluation

<!-- review:SF-2026-ARXIV-2603-23055:start -->
**问题**：同一数据先筛模型再估计 KPI 分布会产生 post-selection bias，普通 confidence interval 不再覆盖声明对象。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：PS-DME 用 e-value 在任意 data-dependent pre-selection 后控制 distributional KPI 的 false coverage rate，而不是只报告一个目标阈值。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §Appendix F Alternative Implementation of PS-DME via Berk–Jones CDF Bands [facet=method]; https://arxiv.org/html/2603.23055v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23055v1.html; sha256:d7cd479846a9b0968cf9c304152b2bc6bddeac006380596717762b1a31bf0306`。

**Evaluation contract 与未证明部分**：理论条件、synthetic、text-to-SQL 和 telecom 实验支持所述 coverage/sample-efficiency；不保证任意 evaluator 或分布漂移下仍校准。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.1 Sample-Splitting Distributional Model Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23055v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23055v1.html; sha256:d7cd479846a9b0968cf9c304152b2bc6bddeac006380596717762b1a31bf0306`。

**Trade-off / failure / coexistence**：复用数据提高效率但依赖统计假设与更复杂审计；样本充足时独立 holdout 仍更容易解释。

<!-- claim:SF-2026-ARXIV-2603-23055:start -->**Claim Boundary**：只支持 arXiv:2603.23055v1 §Appendix F Alternative Implementation of PS-DME via Berk–Jones CDF Bands 的机制与 §3.1 Sample-Splitting Distributional Model Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23055:end -->
<!-- review:SF-2026-ARXIV-2603-23055:end -->
### Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution

<!-- review:SF-2026-ARXIV-2603-23064:start -->
**问题**：heartbeat background execution 与前台会话共用 memory 时，不可信后台内容可在用户不可见的情况下变成后续行为状态。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文形式化 Exposure→Memory→Behavior 链，并区分短期 session 污染、长期写入和跨会话影响，要求 background identity、provenance 与 write authority 分离。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §4 Implementation [facet=method]; https://arxiv.org/html/2603.23064v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23064v1.html; sha256:087b2b6f045236d13b16247053e330620b6d3d439ba44a61f7966ff606b29bc2`。

**Evaluation contract 与未证明部分**：MissClaw 控制实验支持特定社交线索与 memory policy 下的污染率；不代表所有 Claw 实现或自然流量具有相同比例。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Case Studies and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.23064v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23064v1.html; sha256:087b2b6f045236d13b16247053e330620b6d3d439ba44a61f7966ff606b29bc2`。

**Trade-off / failure / coexistence**：隔离 background memory 降低静默污染，却减少跨渠道连续性并增加审批；可信本地定时任务仍可共享有限状态。

<!-- claim:SF-2026-ARXIV-2603-23064:start -->**Claim Boundary**：只支持 arXiv:2603.23064v1 §4 Implementation 的机制与 §5 Case Studies and Evaluation 的公开 workload；§7.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23064:end -->
<!-- review:SF-2026-ARXIV-2603-23064:end -->
### Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models

<!-- review:SF-2026-ARXIV-2603-23149:start -->
**问题**：用视觉 world model 预演 action outcome 最直观，却在安全 steering 的每一步引入秒级生成延迟。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：DILLO 从 policy latent 与 planned action 蒸馏语言化 outcome predictor，并以 latent rejection sampling 在执行前筛掉高风险 proposal；它预测的是决策相关后果而非完整视觉世界。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3 Distilled Language Action World Model [facet=method]; https://arxiv.org/html/2603.23149v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23149v1.html; sha256:273e0b7daf8b97759d309718f254d4f386629ced10f672fed55e700025077722`。

**Evaluation contract 与未证明部分**：latent sufficiency 与 steering 实验支持所测 policy/task 上的 failure prevention 和 latency 优势；未证明语言摘要保留所有物理安全变量。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.4 Proactive Policy Steering and Inference Latency [facet=evaluation]; https://arxiv.org/html/2603.23149v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23149v1.html; sha256:273e0b7daf8b97759d309718f254d4f386629ced10f672fed55e700025077722`。

**Trade-off / failure / coexistence**：压缩 outcome 提高实时性，却可能漏掉难以语言化的接触与几何细节；需要高保真模拟或分布外动作时视觉/物理模型仍必要。

<!-- claim:SF-2026-ARXIV-2603-23149:start -->**Claim Boundary**：只支持 arXiv:2603.23149v1 §3 Distilled Language Action World Model 的机制与 §4.4 Proactive Policy Steering and Inference Latency 的公开 workload；§5 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23149:end -->
<!-- review:SF-2026-ARXIV-2603-23149:end -->
### LLM Olympiad: Why Model Evaluation Needs a Sealed Exam

<!-- review:SF-2026-ARXIV-2603-23292:start -->
**问题**：公开 benchmark 会被训练暴露、反复调参与隐藏 harness 差异共同侵蚀，单看 leaderboard 无法区分能力与适配。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Olympiad contract 在评测前密封题目、冻结 submission、统一执行 harness，结束后再公开题目和代码，分离测量期保密与事后可审计。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §3.2 Design principles [facet=method]; https://arxiv.org/html/2603.23292v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23292v1.html; sha256:96b1e376fae37631b3fd505cbf86f36ffd13843f664c1f561cf42fb081962c9d`。

**Evaluation contract 与未证明部分**：这是 evaluation design proposal 而非新模型实验；可支持 release contract，不能证明密封本身消除组织泄漏或 evaluator 偏差。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §C.4 Evaluation scale [facet=evaluation]; https://arxiv.org/html/2603.23292v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23292v1.html; sha256:96b1e376fae37631b3fd505cbf86f36ffd13843f664c1f561cf42fb081962c9d`。

**Trade-off / failure / coexistence**：sealed exam 提高独立性却降低即时透明度并增加保密运营；诊断性公开集仍适合日常开发。

<!-- claim:SF-2026-ARXIV-2603-23292:start -->**Claim Boundary**：只支持 arXiv:2603.23292v1 §3.2 Design principles 的机制与 §C.4 Evaluation scale 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23292:end -->
<!-- review:SF-2026-ARXIV-2603-23292:end -->
### ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment

<!-- review:SF-2026-ARXIV-2603-23376:start -->
**问题**：通用视频 likelihood 能生成逼真画面，却不会自动惩罚穿透、反重力或 action 与结果不一致。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：ABot-PhysWorld 组合 embodied 数据筛选、physics-aware caption、解耦 VLM discriminator 的 diffusion-DPO 与 action-map conditioning，把物理偏好和可控动作写入训练目标。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3.2 Physical Preference Alignment [facet=method]; https://arxiv.org/html/2603.23376v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23376v1.html; sha256:35ddec198b2bf6a587e2cf3b25e17d1f1d71d64a3e3aaa4cfce4d814c3067033`。

**Evaluation contract 与未证明部分**：Embodied-ZeroShot 与视频实验支持所测 manipulation clips 上的视觉、物理和动作一致性；VLM 判别与视频指标不能替代真实机器人闭环成功率。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.23376v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23376v1.html; sha256:35ddec198b2bf6a587e2cf3b25e17d1f1d71d64a3e3aaa4cfce4d814c3067033`。

**Trade-off / failure / coexistence**：物理偏好提升约束一致性，却继承判别器偏差并增加数据/后训练成本；只追求开放域视频外观时通用生成模型仍更经济。

<!-- claim:SF-2026-ARXIV-2603-23376:start -->**Claim Boundary**：只支持 arXiv:2603.23376v1 §3.2 Physical Preference Alignment 的机制与 §5.3 Evaluation Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23376:end -->
<!-- review:SF-2026-ARXIV-2603-23376:end -->
### SortedRL: Accelerating RL Training for LLMs through Online Length-Aware Scheduling

<!-- review:SF-2026-ARXIV-2603-23414:start -->
**问题**：长 rollout 使 RL learner 等待最慢 trajectory，统一大 batch 会形成严重同步 bubble。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：SortedRL 在线按输出长度重排 rollout，允许短组先更新，并用 stateful controller、rollout buffer 与 cache 约束 off-policy 程度。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `HTML — §4.4.1 Throughput of Different Methods [facet=method]; https://arxiv.org/html/2603.23414v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23414v1.html; sha256:e48bad22f24ac9a7c4dfbbf44630bfd09f81b113aab744c51167faeb7ad4a0e5`。

**Evaluation contract 与未证明部分**：LLaMA-3.1-8B/Qwen-2.5-32B 的指定任务支持 bubble 与训练结果折中；不证明长度排序对所有 reward 或策略漂移稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.2 Results on Logic Problems [facet=evaluation]; https://arxiv.org/html/2603.23414v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23414v1.html; sha256:e48bad22f24ac9a7c4dfbbf44630bfd09f81b113aab744c51167faeb7ad4a0e5`。

**Trade-off / failure / coexistence**：异步重排提高利用率却改变数据时序和 freshness；短、同质 rollout 仍适合同步 batch。

<!-- claim:SF-2026-ARXIV-2603-23414:start -->**Claim Boundary**：只支持 arXiv:2603.23414v1 §4.4.1 Throughput of Different Methods 的机制与 §4.2 Results on Logic Problems 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23414:end -->
<!-- review:SF-2026-ARXIV-2603-23414:end -->
### SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning

<!-- review:SF-2026-ARXIV-2603-23483:start -->
**问题**：agentic vision 的感知、推理和工具循环串行累积，单纯加速每个模型调用不能消除 agentic depth。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：SpecEyes 让轻量无工具模型预测 trajectory，以 answer-separability gate 决定提前提交，并用异构并行 funnel 覆盖大模型串行执行。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.23483v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23483v1.html; sha256:8862f2365c98d199b9729423c8d0d2139e2dee9f487187c548775c637a2f714e`。

**Evaluation contract 与未证明部分**：V* Bench、HR-Bench、POPE 支持所测模型/并发下的速度质量；self-verification gate 不是通用 correctness proof。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.23483v1; papers/2026/03/_sources/daily-20260325/exact-v1-bodies/2603.23483v1.html; sha256:8862f2365c98d199b9729423c8d0d2139e2dee9f487187c548775c637a2f714e`。

**Trade-off / failure / coexistence**：错误 speculation 会跳过必要工具并放大置信误校准；高风险或难验证任务仍应执行完整链。

<!-- claim:SF-2026-ARXIV-2603-23483:start -->**Claim Boundary**：只支持 arXiv:2603.23483v1 §3 Methodology 的机制与 §4.2 Main Results 的公开 workload；§5 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-23483:end -->
<!-- review:SF-2026-ARXIV-2603-23483:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-22300 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22300 |
| SF-2026-ARXIV-2603-22339 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22339 |
| SF-2026-ARXIV-2603-22751 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-22751 |
| SF-2026-ARXIV-2603-22774 | score_7_9;potential_books_delta | selected | DA-20260325-08 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260325-08 |
| SF-2026-ARXIV-2603-23049 | score_7_9;potential_books_delta | selected | DA-20260325-14 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260325-14 |
| SF-2026-ARXIV-2603-23149 | score_7_9;potential_books_delta | selected | DA-20260325-17 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260325-17 |

<!-- analysis-decision:SF-2026-ARXIV-2603-22300:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22300:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22339:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22339:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-22751:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-22751:end -->
<!-- analysis:DA-20260325-08:start -->
### Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference

多 GPU serving 通常把慢吞吐归因于 GPU 算力或互联，默认 host CPU 只承担可忽略的调度工作。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：论文把 kernel launch、collective progress、tokenization 与 agentic host work 分解到 CPU allocation，显示 CPU 是维持 GPU feed 的控制面资源。 其公开验证边界为：多 GPU serving 配置下的 profiling 支持 CPU 配额不足会造成 launch delay、通信停顿与 GPU idle；具体幅度绑定模型、框架、CPU/GPU 拓扑和请求混合。 新增代价与回退条件为：增加 CPU 或隔离 host work 可恢复利用率，但提高成本并可能把瓶颈移到内存/互联；GPU 已饱和或 host path 很薄时继续加 CPU 无益。
<!-- analysis:DA-20260325-08:end -->
<!-- analysis:DA-20260325-14:start -->
### PCR: A Prefetch-Enhanced Cache Reuse System for Low-Latency RAG Serving

RAG prefix KV reuse 能避免重复 prefill，但从缓存读取大前缀仍会落在请求关键路径并产生新的 I/O 等待。 旧路径在其原约束下仍合理：完整、逐 token 保存 KV，换取语义透明和最低重算风险。 本 family 的设计变化是：PCR 用 prefix tree 管理可复用身份，按层把 cache transfer 与 compute 重叠，并根据队列提前 prefetch；reuse owner 因而同时包含命中、传输与失效状态。 其公开验证边界为：RAG serving 实验支持所测命中分布下的 latency 降低；收益依赖文档复用、队列可预测性、cache 容量和互联带宽。 新增代价与回退条件为：prefetch 隐藏 I/O，却会浪费带宽、放大 stale cache 和公平性问题；低复用或突发 query 下按需 prefill 更简单。
<!-- analysis:DA-20260325-14:end -->
<!-- analysis:DA-20260325-17:start -->
### Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models

用视觉 world model 预演 action outcome 最直观，却在安全 steering 的每一步引入秒级生成延迟。 旧路径在其原约束下仍合理：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。 本 family 的设计变化是：DILLO 从 policy latent 与 planned action 蒸馏语言化 outcome predictor，并以 latent rejection sampling 在执行前筛掉高风险 proposal；它预测的是决策相关后果而非完整视觉世界。 其公开验证边界为：latent sufficiency 与 steering 实验支持所测 policy/task 上的 failure prevention 和 latency 优势；未证明语言摘要保留所有物理安全变量。 新增代价与回退条件为：压缩 outcome 提高实时性，却可能漏掉难以语言化的接触与几何细节；需要高保真模拟或分布外动作时视觉/物理模型仍必要。
<!-- analysis:DA-20260325-17:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-22300 | MODEL-SELF-ATTENTION | books/part-02-model/14-self-attention.md#本章要回答的问题 (section Ch-owner) | books/part-02-model/13-position-encoding.md#第13章-position-encoding (section Ch-adjacent); books/part-02-model/15-multi-head-attention.md#第15章-multi-head-attention (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22300 | delta:SF-2026-ARXIV-2603-22300 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-22300 |
| SF-2026-ARXIV-2603-22339 | WORLDVIEW-SCALING-LAW | books/part-01-worldview/07-scaling-law.md#kaplan-与-chinchilla-的结论为什么不同 (section Ch-owner) | books/part-01-worldview/06-why-transformer-changed-the-world.md#第6章-transformer-为什么改变世界 (section Ch-adjacent); books/part-01-worldview/08-why-llms-show-intelligence.md#第8章-大模型为什么会产生智能 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22339 | delta:SF-2026-ARXIV-2603-22339 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-22339 |
| SF-2026-ARXIV-2603-22350 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#从-scalar-confidence-到-safe-commit-certificate (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22350 | delta:SF-2026-ARXIV-2603-22350 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22350 |
| SF-2026-ARXIV-2603-22367 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#failure-attribution、perception-routing-与-sticky-state-ownership (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#扩展-agent-数量之前，先测量-coordination-tax (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22367 | delta:SF-2026-ARXIV-2603-22367 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22367 |
| SF-2026-ARXIV-2603-22489 | AGENT-MCP | books/part-07-agent/83-mcp.md#tool-catalog-扩大后，discovery-与-execution-必须分离 (section Ch-owner) | books/part-07-agent/82-multi-agent.md#扩展-agent-数量之前，先测量-coordination-tax (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#从-trajectory-到-skill-是一次受治理的-compilation (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22489 | delta:SF-2026-ARXIV-2603-22489 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22489 |
| SF-2026-ARXIV-2603-22563 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22563 | delta:SF-2026-ARXIV-2603-22563 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22563 |
| SF-2026-ARXIV-2603-22751 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22751 | delta:SF-2026-ARXIV-2603-22751 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-22751 |
| SF-2026-ARXIV-2603-22774 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22774 | delta:SF-2026-ARXIV-2603-22774 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-22774 |
| SF-2026-ARXIV-2603-22855 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22855 | delta:SF-2026-ARXIV-2603-22855 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22855 |
| SF-2026-ARXIV-2603-22858 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#路线六：让模型在-test-time-更新内部记忆 (section Ch-owner) | books/part-02-model/21-moe.md#第21章-moe (section Ch-adjacent); books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22858 | delta:SF-2026-ARXIV-2603-22858 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22858 |
| SF-2026-ARXIV-2603-22868 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#局部合理动作会累积成有害轨迹 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22868 | delta:SF-2026-ARXIV-2603-22868 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22868 |
| SF-2026-ARXIV-2603-22910 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从统一跨层共享到-token-×-depth-自适应残差 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22910 | delta:SF-2026-ARXIV-2603-22910 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22910 |
| SF-2026-ARXIV-2603-22928 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#responsive-不等于-semantic-available (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-22928 | delta:SF-2026-ARXIV-2603-22928 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-22928 |
| SF-2026-ARXIV-2603-23049 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#小结 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23049 | delta:SF-2026-ARXIV-2603-23049 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-23049 |
| SF-2026-ARXIV-2603-23055 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23055 | delta:SF-2026-ARXIV-2603-23055 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23055 |
| SF-2026-ARXIV-2603-23064 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#weight-streaming-的保密边界在片上明文状态才结束 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23064 | delta:SF-2026-ARXIV-2603-23064 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23064 |
| SF-2026-ARXIV-2603-23149 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#在谈-state-之前，先声明预测-channel (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23149 | delta:SF-2026-ARXIV-2603-23149 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-23149 |
| SF-2026-ARXIV-2603-23292 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23292 | delta:SF-2026-ARXIV-2603-23292 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23292 |
| SF-2026-ARXIV-2603-23376 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23376 | delta:SF-2026-ARXIV-2603-23376 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23376 |
| SF-2026-ARXIV-2603-23414 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#arrival-bias-与-stale-direction-是两种独立误差 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23414 | delta:SF-2026-ARXIV-2603-23414 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23414 |
| SF-2026-ARXIV-2603-23483 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-可以修订，但只能在安全边界-commit (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-23483 | delta:SF-2026-ARXIV-2603-23483 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-23483 |

<!-- books-review:SF-2026-ARXIV-2603-22300:start -->
### Scaling Attention via Feature Sparsity — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22300:start -->已读 owner `books/part-02-model/14-self-attention.md` 与相邻章节。现有命题：本章的核心判断是：**Self Attention 是 content-dependent routing。**每个位置用 Query 描述自己在寻找什么，用 Key 描述自己可怎样被匹配，用 Value 提供真正被聚合的内容。<!-- existing:SF-2026-ARXIV-2603-22300:end -->

<!-- delta:SF-2026-ARXIV-2603-22300:start -->新证据差异：SFA 改为稀疏化 query/key 的 feature 维，并用 IO-aware FlashSFA kernel 执行；控制权从 token admission 转到 feature-code 与 kernel layout。<!-- delta:SF-2026-ARXIV-2603-22300:end -->

边界：只支持 arXiv:2603.22300v1 §3 Sparse Feature Attention 的机制与 §4.3 Benchmarking Computation and Memory Efficiency of SFA 的公开 workload；§7 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-22300:end -->
<!-- books-review:SF-2026-ARXIV-2603-22339:start -->
### Problems with Chinchilla Approach 2: Systematic Biases in IsoFLOP Parabola Fits — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22339:start -->已读 owner `books/part-01-worldview/07-scaling-law.md` 与相邻章节。现有命题：两者并不是一个正确、另一个毫无价值。差异说明 scaling exponent 和最优配置依赖实验覆盖、训练方法、数据与拟合假设。Chinchilla 修正了当时重要的工程判断，但它同样不是对所有架构、数据质量和后训练过程的永久常数。<!-- existing:SF-2026-ARXIV-2603-22339:end -->

<!-- delta:SF-2026-ARXIV-2603-22339:start -->新证据差异：论文证明非对称 loss surface、偏心采样与有限 grid 会给 Approach 2 引入结构性偏差，并以直接 surface fit/variable projection 恢复五个参数的联合估计。<!-- delta:SF-2026-ARXIV-2603-22339:end -->

边界：只支持 arXiv:2603.22339v1 §8.2 Variable Projection (VPNLS) 的机制与 §8.3 Method Comparison (Parameter Recovery) 的公开 workload；§9.1 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-22339:end -->
<!-- books-review:SF-2026-ARXIV-2603-22350:start -->
### Session Risk Memory (SRM): Temporal Authorization for Deterministic Pre-Execution Safety Gates — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22350:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Certificate 不替代 IAM、sandbox、审批或 compensation。它依赖可校准 support、准确 safety map 与可枚举 outcome； world/action 数增长会放大成本，stale 或 poisoned memory 也可能使 support 错误收缩。SafeCommit 的小型 simulator 只支持该控制结构，不证明生产规模与 coverage。规则清晰时 deterministic policy 更强；无法列举 plausible worlds 或副作用不可逆时，human approval 仍是必要旧分支。<!-- existing:SF-2026-ARXIV-2603-22350:end -->

<!-- delta:SF-2026-ARXIV-2603-22350:start -->新证据差异：SRM 在 gate 外维护 session semantic centroid 与基线扣除后的 EMA risk，把历史状态交给确定性 pre-execution decision，而不是让 LLM 自报安全。<!-- delta:SF-2026-ARXIV-2603-22350:end -->

边界：只支持 arXiv:2603.22350v1 §3.2 Session Behavioral Centroid 的机制与 §5.2 Evaluation Protocol 的公开 workload；§6.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22350:end -->
<!-- books-review:SF-2026-ARXIV-2603-22367:start -->
### Reasoner-Executor-Synthesizer: Scalable Agentic Architecture with Static O(1) Context Window — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22367:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。<!-- existing:SF-2026-ARXIV-2603-22367:end -->

<!-- delta:SF-2026-ARXIV-2603-22367:start -->新证据差异：RES 把意图解析、确定性检索聚合和叙述生成拆开；Executor 只向 Synthesizer 交付固定尺寸统计摘要，使 raw record 不进入生成状态。<!-- delta:SF-2026-ARXIV-2603-22367:end -->

边界：只支持 arXiv:2603.22367v1 §III. THE RES ARCHITECTURE 的机制与 §B. Results 的公开 workload；§D. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22367:end -->
<!-- books-review:SF-2026-ARXIV-2603-22489:start -->
### Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22489:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：把所有 tool schemas 在会话开始时注入 Context，目录小且稳定时最简单；当一个 gateway 聚合数百个 servers、数千个 tools 后，它会同时消耗上下文、放大 selection noise，并让用户无法知道能力位于哪个 server。Prompt caching 只能减少重复 prefill，不能释放逻辑 context，也不能改善 discoverability。<!-- existing:SF-2026-ARXIV-2603-22489:end -->

<!-- delta:SF-2026-ARXIV-2603-22489:start -->新证据差异：论文用 STRIDE/DREAD 分解 host、client、LLM、server、data store 与 authorization server，再把注册校验、decision-path 检查、runtime monitoring 和用户透明度组成分层防线。<!-- delta:SF-2026-ARXIV-2603-22489:end -->

边界：只支持 arXiv:2603.22489v1 §4. Tool Poisoning Architecture and Attack Flow 的机制与 §5.2. Testing Procedure 的公开 workload；§7.4. Threats to validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22489:end -->
<!-- books-review:SF-2026-ARXIV-2603-22563:start -->
### Privacy-Preserving Reinforcement Learning from Human Feedback via Decoupled Reward Modeling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22563:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-22563:end -->

<!-- delta:SF-2026-ARXIV-2603-22563:start -->新证据差异：该方案只在敏感偏好进入 reward learning 时建立 DP 边界，再让 policy 从私有 reward model 学习；隐私 owner 从最终策略更新前移到奖励数据接口。<!-- delta:SF-2026-ARXIV-2603-22563:end -->

边界：只支持 arXiv:2603.22563v1 §3.2 Proposed Framework: Private Reward-Based Alignment 的机制与 §5.1.1 Validation of Theoretical Results 的公开 workload；§6 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22563:end -->
<!-- books-review:SF-2026-ARXIV-2603-22751:start -->
### Observable Channels, Not Just Storage: Evaluating Privacy Leakage in LLM Agent Pipelines — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22751:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-22751:end -->

<!-- delta:SF-2026-ARXIV-2603-22751:start -->新证据差异：CIPL 把目标属性、agent pipeline、可观察 channel 与 inversion attacker 统一成同一测量接口；privacy owner 从某个存储组件扩展为端到端 observable data flow。<!-- delta:SF-2026-ARXIV-2603-22751:end -->

边界：只支持 arXiv:2603.22751v1 §3.1–§3.6 的 threat model、observable-channel measurement interface 与 channel-inversion attack，以及 Appendix B 的作者实验；不把该受限 evaluation contract 外推为通用隐私保证、生产 SLO、多租户或长期可靠性。最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-22751:end -->
<!-- books-review:SF-2026-ARXIV-2603-22774:start -->
### Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22774:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-22774:end -->

<!-- delta:SF-2026-ARXIV-2603-22774:start -->新证据差异：论文把 kernel launch、collective progress、tokenization 与 agentic host work 分解到 CPU allocation，显示 CPU 是维持 GPU feed 的控制面资源。<!-- delta:SF-2026-ARXIV-2603-22774:end -->

边界：只支持 arXiv:2603.22774v1 §V Understanding the CPU Bottlenecks in Multi-GPU Systems 的机制与 §IV CPU Bottleneck in LLM Inference 的公开 workload；§VI-C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-22774:end -->
<!-- books-review:SF-2026-ARXIV-2603-22855:start -->
### TorR: Towards Brain-Inspired Task-Oriented Reasoning via Cache-Oriented Algorithm-Architecture Co-design — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22855:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。<!-- existing:SF-2026-ARXIV-2603-22855:end -->

<!-- delta:SF-2026-ARXIV-2603-22855:start -->新证据差异：TorR 用 HDC associative reasoner、query cache、bit-delta update 与 load-gated bypass，在控制器中按负载选择 full/delta/bypass path。<!-- delta:SF-2026-ARXIV-2603-22855:end -->

边界：只支持 arXiv:2603.22855v1 §3.2. Algorithmic Design 的机制与 §5.3. Accelerator Execution Results 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22855:end -->
<!-- books-review:SF-2026-ARXIV-2603-22858:start -->
### The Coordinate System Problem in Persistent Structural Memory for Neural Architectures — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22858:start -->已读 owner `books/part-02-model/22-long-context.md` 与相邻章节。现有命题：Attention 保存可直接寻址的 token history，线性 RNN/SSM 把历史压入固定大小状态。Test-time neural memory 提出另一条分支：把 memory 本身做成可在线更新的参数化模块，用当前输入产生 的 prediction error 或 gradient 作为“surprise”信号，再通过 momentum 与 forgetting/ regularization 决定写入和保留。<!-- existing:SF-2026-ARXIV-2603-22858:end -->

<!-- delta:SF-2026-ARXIV-2603-22858:start -->新证据差异：多轮 DPPN 实验暴露跨 run coordinate drift：persistent state 若依赖可旋转的 learned slot/embedding，transfer 时没有稳定身份；固定坐标只解决必要条件，仍需合适的写入与读出机制。<!-- delta:SF-2026-ARXIV-2603-22858:end -->

边界：只支持 arXiv:2603.22858v1 §3 Architecture: Dual-View Pheromone Pathway Networks 的机制与 §7.5 Results: Aligned Distillation 的公开 workload；§15 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22858:end -->
<!-- books-review:SF-2026-ARXIV-2603-22868:start -->
### Agent-Sentry: Bounding LLM Agents via Execution Provenance — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22868:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：多 Agent 委派把这条链再推进一步：有害目标可能被拆成多个局部合理的子任务，单节点重新做 prompt classification 仍看不见跨节点累积的语义。运行时需要把 source、delegation、memory write 与 irreversible sink 组织成带 provenance 的信息流，在 sink 前重建跨节点上下文，再由确定性 policy 决定是否允许 commit。 这用额外图状态、标注误差和重建延迟换取跨委派风险可见性；semantic taint 仍只是 sensor input，不替代 capability isolation，也不能授权 LLM 自己拥有最终安全判决。<!-- existing:SF-2026-ARXIV-2603-22868:end -->

<!-- delta:SF-2026-ARXIV-2603-22868:start -->新证据差异：Agent-Sentry 从合法执行学习 provenance-conditioned behavior bound，在 action 落界前检查其来源与轨迹，而不是只过滤最终文本。<!-- delta:SF-2026-ARXIV-2603-22868:end -->

边界：只支持 arXiv:2603.22868v1 §13.1 Architecture Overview 的机制与 §5.2 Evaluation Procedure 的公开 workload；§6.4 Ablation Study: Intent Alignment without Functionality Graph 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22868:end -->
<!-- books-review:SF-2026-ARXIV-2603-22910:start -->
### EchoKV: Efficient KV Cache Compression via Similarity-Based Reconstruction — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22910:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：第一条分支按 head 在 shared、residual 与 exact mode 之间做离散路由，适合表达“这个 head 是否需要保真”； 第二条分支按 token 分配 residual rank，适合表达“同一 head 内哪些位置需要更多层间细节”。二者复用相邻层 相关性原则，却不是同一种 selector。attention-logit 或 attention-output reconstruction error 只是当前 prompt 的 保真 proxy，不是未来 causal utility；probe、router、basis、residual precision 与 policy revision 都必须进入 cache identity。<!-- existing:SF-2026-ARXIV-2603-22910:end -->

<!-- delta:SF-2026-ARXIV-2603-22910:start -->新证据差异：EchoKV 保留 full-cache 语义，在压力出现时丢弃可重建分量并用轻量网络恢复，使 compression policy 成为 runtime 可切换状态。<!-- delta:SF-2026-ARXIV-2603-22910:end -->

边界：只支持 arXiv:2603.22910v1 §3.1 Overview of EchoKV 的机制与 §5.5 Ablation of Input Features 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22910:end -->
<!-- books-review:SF-2026-ARXIV-2603-22928:start -->
### SoK: The Attack Surface of Agentic AI - Tools and Autonomy — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-22928:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：防御因此要把 per-tenant isolation、queue / admission、late-result policy 与最终质量一起监控。延长 deadline 会损害 SLO，强隔离会牺牲利用率；单一 tracking pipeline 的作者实验只证明该 attack surface 可以存在，不证明所有网络抖动或 tiered system 都会同样退化。队列与 placement 机制仍由第 56 章拥有，本章只定义 availability threat 与 security evidence boundary。<!-- existing:SF-2026-ARXIV-2603-22928:end -->

<!-- delta:SF-2026-ARXIV-2603-22928:start -->新证据差异：SoK 把 prompt、knowledge base、tool/plugin 与 cross-agent 组合成显式 trust-boundary taxonomy，并将 unsafe action 与 privilege escalation 纳入系统评估。<!-- delta:SF-2026-ARXIV-2603-22928:end -->

边界：只支持 arXiv:2603.22928v1 §7.1. Formal Methods for Agent Plans and Tool Use 的机制与 §6. Evaluation & Metrics for Agentic AI Security 的公开 workload；§9. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-22928:end -->
<!-- books-review:SF-2026-ARXIV-2603-23049:start -->
### PCR: A Prefetch-Enhanced Cache Reuse System for Low-Latency RAG Serving — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23049:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。<!-- existing:SF-2026-ARXIV-2603-23049:end -->

<!-- delta:SF-2026-ARXIV-2603-23049:start -->新证据差异：PCR 用 prefix tree 管理可复用身份，按层把 cache transfer 与 compute 重叠，并根据队列提前 prefetch；reuse owner 因而同时包含命中、传输与失效状态。<!-- delta:SF-2026-ARXIV-2603-23049:end -->

边界：只支持 arXiv:2603.23049v1 §4.1. System Overview 的机制与 §6.1. Experimental Methodology 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-23049:end -->
<!-- books-review:SF-2026-ARXIV-2603-23055:start -->
### Post-Selection Distributional Model Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23055:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-23055:end -->

<!-- delta:SF-2026-ARXIV-2603-23055:start -->新证据差异：PS-DME 用 e-value 在任意 data-dependent pre-selection 后控制 distributional KPI 的 false coverage rate，而不是只报告一个目标阈值。<!-- delta:SF-2026-ARXIV-2603-23055:end -->

边界：只支持 arXiv:2603.23055v1 §Appendix F Alternative Implementation of PS-DME via Berk–Jones CDF Bands 的机制与 §3.1 Sample-Splitting Distributional Model Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23055:end -->
<!-- books-review:SF-2026-ARXIV-2603-23064:start -->
### Mind Your HEARTBEAT! Claw Background Execution Inherently Enables Silent Memory Pollution — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23064:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：这条路径减少 off-chip plaintext exposure，却把 trusted die、SMMU/IOMMU 配置、counter/nonce lifecycle、SRAM isolation 与 scrub 正确性变成新的安全前置条件。SMMU 在这里约束 stream-ID 与地址映射，并不认证 ciphertext 或 DMA payload；AES-CTR 本身也不提供完整性。论文报告的近线速结果来自 proxy hardware measurement 与 idealized accelerator model，并非已制造 NPU silicon；它也不覆盖 invasive、side-channel 或 supply-chain adversary。因此该机制只能作为可信片上边界下的优化分支。缺少可信 die 或片上隔离时，平台必须缩小 confidentiality claim，或采用能覆盖目标 adversary 的受控 TEE/独立硬件边界；page-level memory encryption 只能回退保护较窄的 at-rest/DRAM threat，不能在同一 compromised-OS/physical adversary 下冒充等价保护。<!-- existing:SF-2026-ARXIV-2603-23064:end -->

<!-- delta:SF-2026-ARXIV-2603-23064:start -->新证据差异：论文形式化 Exposure→Memory→Behavior 链，并区分短期 session 污染、长期写入和跨会话影响，要求 background identity、provenance 与 write authority 分离。<!-- delta:SF-2026-ARXIV-2603-23064:end -->

边界：只支持 arXiv:2603.23064v1 §4 Implementation 的机制与 §5 Case Studies and Evaluation 的公开 workload；§7.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23064:end -->
<!-- books-review:SF-2026-ARXIV-2603-23149:start -->
### Describe-Then-Act: Proactive Agent Steering via Distilled Language-Action World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23149:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：第一种回答“若执行这些 action，环境可能如何变化”，因此由 World Model 拥有；第二种更接近 policy 或 self-model，回答“看到这些 observation，agent 会怎样行动”；第三种描述二者闭环后实际可见的 trajectory。 三者可以在观测到的 policy support 上给出相同 continuation，却不拥有相同的 counterfactual contract。<!-- existing:SF-2026-ARXIV-2603-23149:end -->

<!-- delta:SF-2026-ARXIV-2603-23149:start -->新证据差异：DILLO 从 policy latent 与 planned action 蒸馏语言化 outcome predictor，并以 latent rejection sampling 在执行前筛掉高风险 proposal；它预测的是决策相关后果而非完整视觉世界。<!-- delta:SF-2026-ARXIV-2603-23149:end -->

边界：只支持 arXiv:2603.23149v1 §3 Distilled Language Action World Model 的机制与 §4.4 Proactive Policy Steering and Inference Latency 的公开 workload；§5 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-23149:end -->
<!-- books-review:SF-2026-ARXIV-2603-23292:start -->
### LLM Olympiad: Why Model Evaluation Needs a Sealed Exam — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23292:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-23292:end -->

<!-- delta:SF-2026-ARXIV-2603-23292:start -->新证据差异：Olympiad contract 在评测前密封题目、冻结 submission、统一执行 harness，结束后再公开题目和代码，分离测量期保密与事后可审计。<!-- delta:SF-2026-ARXIV-2603-23292:end -->

边界：只支持 arXiv:2603.23292v1 §3.2 Design principles 的机制与 §C.4 Evaluation scale 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23292:end -->
<!-- books-review:SF-2026-ARXIV-2603-23376:start -->
### ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23376:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-23376:end -->

<!-- delta:SF-2026-ARXIV-2603-23376:start -->新证据差异：ABot-PhysWorld 组合 embodied 数据筛选、physics-aware caption、解耦 VLM discriminator 的 diffusion-DPO 与 action-map conditioning，把物理偏好和可控动作写入训练目标。<!-- delta:SF-2026-ARXIV-2603-23376:end -->

边界：只支持 arXiv:2603.23376v1 §3.2 Physical Preference Alignment 的机制与 §5.3 Evaluation Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23376:end -->
<!-- books-review:SF-2026-ARXIV-2603-23414:start -->
### SortedRL: Accelerating RL Training for LLMs through Online Length-Aware Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23414:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：**Trade-off、failure、共存与回退。** quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。<!-- existing:SF-2026-ARXIV-2603-23414:end -->

<!-- delta:SF-2026-ARXIV-2603-23414:start -->新证据差异：SortedRL 在线按输出长度重排 rollout，允许短组先更新，并用 stateful controller、rollout buffer 与 cache 约束 off-policy 程度。<!-- delta:SF-2026-ARXIV-2603-23414:end -->

边界：只支持 arXiv:2603.23414v1 §4.4.1 Throughput of Different Methods 的机制与 §4.2 Results on Logic Problems 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23414:end -->
<!-- books-review:SF-2026-ARXIV-2603-23483:start -->
### SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-23483:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2603-23483:end -->

<!-- delta:SF-2026-ARXIV-2603-23483:start -->新证据差异：SpecEyes 让轻量无工具模型预测 trajectory，以 answer-separability gate 决定提前提交，并用异构并行 funnel 覆盖大模型串行执行。<!-- delta:SF-2026-ARXIV-2603-23483:end -->

边界：只支持 arXiv:2603.23483v1 §3 Methodology 的机制与 §4.2 Main Results 的公开 workload；§5 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-23483:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260325-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | — | accepted: strict-window raw inventory、逐项 screening、withdrawn closure 与 weekly_dependency=0 已复核 | passed |
| SA-20260325-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260325-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | — | accepted: fresh-context false-positive / false-negative 与 Deep Analysis selection 已复核 | passed |
| SA-20260325-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | — | accepted: Integrate 项已写入 canonical owner，且非写作者 post-write audit 通过 | passed |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260325/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 6 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 6 项 Books Integration：
- 更新并复核 `books/part-01-worldview/07-scaling-law.md`。
- 更新并复核 `books/part-02-model/14-self-attention.md`。
- 更新并复核 `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 更新并复核 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
- 更新并复核 `books/part-06-ai-infrastructure/72-security.md`。
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
