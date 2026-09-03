# Daily Research — 2026-03-27

**Research Date:** 2026-03-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-26 09:00:00 ～ 2026-03-27 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=557/557/557；denominator=14、pre-denominator closures=543。exact-v1 Review complete=14、blocked=0；Integrate 建议=3。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-27 |
| Window End | 2026-03-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260327-AUTHOR-14 |
| Denominator Frozen At | 2026-09-02T16:07:11.473626+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-26T09:00:00+08:00 | 2026-03-27T09:00:00+08:00 | 2026-09-02T16:07:11.473626+08:00 | official-schedule recovery receipt + 557/557 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 557 | SF-2026-ARXIV-2603-24595;SF-2026-ARXIV-2603-24676;SF-2026-ARXIV-2603-24755;SF-2026-ARXIV-2603-24775;SF-2026-ARXIV-2603-24963;SF-2026-ARXIV-2603-25056;SF-2026-ARXIV-2603-25111;SF-2026-ARXIV-2603-25120;SF-2026-ARXIV-2603-25158;SF-2026-ARXIV-2603-25289;SF-2026-ARXIV-2603-25342;SF-2026-ARXIV-2603-25685;SF-2026-ARXIV-2603-25702;SF-2026-ARXIV-2603-25716 | pages=100; prefixes=00..99; final_cursor=end; registered=557; screened=557; retained=14; closure=543 | 2026-03-27T01:00:00+00:00 | screening-ledger-final.json#sha256=95bce3d377a375f2e651c2703a41626b21aacced7a0cd8e261b23fbce3f516c4; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260327:start -->作者侧已逐项筛选全部 557 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260327:end -->

### Fresh-context Audit

<!-- fresh-context-audit:lane-c:start -->
非作者审计已重放 557/557 条 title+abstract：作者 retained 9 项均保留，5 个 false-negative family 已完成 exact-v1 Source Review，13 个 recall challenge 被逐项驳回，1 个 withdrawn 只保留 identity/status；reconciled denominator 为 14；Books queue 中 6 个 `Integrate` 被降为 `No Change — Existing Coverage`，0 个 owner 已重绑。本审计已重建分母、Review 与 Books comparison，但不写 Books；Coverage/Evidence/Books Gate 继续保持 Open，等待 root final reconciliation。收据：`papers/2026/03/_sources/daily-20260327/fresh-context-audit-receipt.json`、`fresh-context-retained-evidence-audit.json`、`fresh-context-books-audit.json`。
<!-- fresh-context-audit:lane-c:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-24595 | arXiv:2603.24595v1 | paper-v1:2603.24595 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-24595 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-24595 | no |
| SF-2026-ARXIV-2603-24676 | arXiv:2603.24676v1 | paper-v1:2603.24676 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24676 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24676 | no |
| SF-2026-ARXIV-2603-24755 | arXiv:2603.24755v1 | paper-v1:2603.24755 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24755 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24755 | no |
| SF-2026-ARXIV-2603-24775 | arXiv:2603.24775v1 | paper-v1:2603.24775 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-24775 | self | — | new_in_window | AGENT-MCP | Integrate | books-review:SF-2026-ARXIV-2603-24775 | no |
| SF-2026-ARXIV-2603-24963 | arXiv:2603.24963v1 | paper-v1:2603.24963 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-24963 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24963 | no |
| SF-2026-ARXIV-2603-25056 | arXiv:2603.25056v1 | paper-v1:2603.25056 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25056 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25056 | no |
| SF-2026-ARXIV-2603-25111 | arXiv:2603.25111v1 | paper-v1:2603.25111 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25111 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25111 | no |
| SF-2026-ARXIV-2603-25120 | arXiv:2603.25120v1 | paper-v1:2603.25120 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25120 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25120 | no |
| SF-2026-ARXIV-2603-25158 | arXiv:2603.25158v1 | paper-v1:2603.25158 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25158 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25158 | no |
| SF-2026-ARXIV-2603-25289 | arXiv:2603.25289v1 | paper-v1:2603.25289 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25289 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25289 | no |
| SF-2026-ARXIV-2603-25342 | arXiv:2603.25342v1 | paper-v1:2603.25342 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25342 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25342 | no |
| SF-2026-ARXIV-2603-25685 | arXiv:2603.25685v1 | paper-v1:2603.25685 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25685 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25685 | no |
| SF-2026-ARXIV-2603-25702 | arXiv:2603.25702v1 | paper-v1:2603.25702 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-25702 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2603-25702 | no |
| SF-2026-ARXIV-2603-25716 | arXiv:2603.25716v1 | paper-v1:2603.25716 | 2026-W13 | 2026-03-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-25716 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25716 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-24595 | RP-f853ca4eb170cb43 | deep | arXiv:2603.24595v1 | SRC-ARXIV@arXiv:2603.24595v1 | HTML — §4 Design of Model2Kernel [facet=method]; https://arxiv.org/html/2603.24595v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24595v1.html; sha256:a8850a63800db829f90ecbbb0d8d6c1394a36b2fd27488e97ac1d12d10b56cb0 | HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.24595v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24595v1.html; sha256:a8850a63800db829f90ecbbb0d8d6c1394a36b2fd27488e97ac1d12d10b56cb0 | HTML — §6 Limitations and Discussion [facet=limitations]; https://arxiv.org/html/2603.24595v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24595v1.html; sha256:a8850a63800db829f90ecbbb0d8d6c1394a36b2fd27488e97ac1d12d10b56cb0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.24595v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24595 | complete |
| SF-2026-ARXIV-2603-24676 | RP-6c3d10eacb4e5ca9 | standard | arXiv:2603.24676v1 | SRC-ARXIV@arXiv:2603.24676v1 | HTML — §B.1.3 Method summary and reproducibility [facet=method]; https://arxiv.org/html/2603.24676v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24676v1.html; sha256:7d6add821b8438075a8089e33a388647420bda61689aa886de7253a9ba8a25bd | HTML — §4 Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.24676v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24676v1.html; sha256:7d6add821b8438075a8089e33a388647420bda61689aa886de7253a9ba8a25bd | HTML — §5 Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.24676v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24676v1.html; sha256:7d6add821b8438075a8089e33a388647420bda61689aa886de7253a9ba8a25bd | arXiv exact-v1 identity https://arxiv.org/abs/2603.24676v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24676 | complete |
| SF-2026-ARXIV-2603-24755 | RP-1921da3b2d2dd5b2 | standard | arXiv:2603.24755v1 | SRC-ARXIV@arXiv:2603.24755v1 | HTML — §2.1 Design Principles [facet=method]; https://arxiv.org/html/2603.24755v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24755v1.html; sha256:b723eec019870dcbbbca8d1ab8897d5135ce79562f787a47df6889b05ddee94a | HTML — §3 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.24755v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24755v1.html; sha256:b723eec019870dcbbbca8d1ab8897d5135ce79562f787a47df6889b05ddee94a | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.24755v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24755v1.html; sha256:b723eec019870dcbbbca8d1ab8897d5135ce79562f787a47df6889b05ddee94a | arXiv exact-v1 identity https://arxiv.org/abs/2603.24755v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24755 | complete |
| SF-2026-ARXIV-2603-24775 | RP-634bbf8fdcb74411 | deep | arXiv:2603.24775v1 | SRC-ARXIV@arXiv:2603.24775v1 | HTML — §3.3 Completion Blocks and Trust Model [facet=method]; https://arxiv.org/html/2603.24775v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24775v1.html; sha256:f6e5221edee364e31e6a05a027322e5c0eaf5c730977e7f67ac85c80bbc41469 | HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.24775v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24775v1.html; sha256:f6e5221edee364e31e6a05a027322e5c0eaf5c730977e7f67ac85c80bbc41469 | HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.24775v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24775v1.html; sha256:f6e5221edee364e31e6a05a027322e5c0eaf5c730977e7f67ac85c80bbc41469 | arXiv exact-v1 identity https://arxiv.org/abs/2603.24775v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24775 | complete |
| SF-2026-ARXIV-2603-24963 | RP-0a5e3232b185eb2b | standard | arXiv:2603.24963v1 | SRC-ARXIV@arXiv:2603.24963v1 | HTML — §4 Experimental Design [facet=method]; https://arxiv.org/html/2603.24963v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24963v1.html; sha256:323d662ae52fe2d80852eb80d995d790b56a60cda8ba6f8539667df6bec68bdf | HTML — §4 Experimental Design [facet=evaluation]; https://arxiv.org/html/2603.24963v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24963v1.html; sha256:323d662ae52fe2d80852eb80d995d790b56a60cda8ba6f8539667df6bec68bdf | HTML — §6.3 Limitations [facet=limitations]; https://arxiv.org/html/2603.24963v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24963v1.html; sha256:323d662ae52fe2d80852eb80d995d790b56a60cda8ba6f8539667df6bec68bdf | arXiv exact-v1 identity https://arxiv.org/abs/2603.24963v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-24963 | complete |
| SF-2026-ARXIV-2603-25056 | RP-b06b2f4431272925 | standard | arXiv:2603.25056v1 | SRC-ARXIV@arXiv:2603.25056v1 | HTML — §3.1 Threat Model [facet=method]; https://arxiv.org/html/2603.25056v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25056v1.html; sha256:98ded9fba081c4d1fbc0c7aad5ca16c8d98511b3f0a7d120968e2de234374b05 | HTML — §5.2 Cross-Model Generalization and the Instruction Specificity Paradox [facet=evaluation]; https://arxiv.org/html/2603.25056v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25056v1.html; sha256:98ded9fba081c4d1fbc0c7aad5ca16c8d98511b3f0a7d120968e2de234374b05 | HTML — §7.6 Limitations [facet=limitations]; https://arxiv.org/html/2603.25056v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25056v1.html; sha256:98ded9fba081c4d1fbc0c7aad5ca16c8d98511b3f0a7d120968e2de234374b05 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25056v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25056 | complete |
| SF-2026-ARXIV-2603-25111 | RP-759b2910bb5f1bc0 | standard | arXiv:2603.25111v1 | SRC-ARXIV@arXiv:2603.25111v1 | HTML — §6.1.2. Implementation Details [facet=method]; https://arxiv.org/html/2603.25111v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25111v1.html; sha256:7e541b1bdb536e75cc999b9a9a43334418387cd3e22a014ce92d042fed298029 | HTML — §6.2. Main Results [facet=evaluation]; https://arxiv.org/html/2603.25111v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25111v1.html; sha256:7e541b1bdb536e75cc999b9a9a43334418387cd3e22a014ce92d042fed298029 | HTML — §6.5. Discussion [facet=limitations]; https://arxiv.org/html/2603.25111v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25111v1.html; sha256:7e541b1bdb536e75cc999b9a9a43334418387cd3e22a014ce92d042fed298029 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25111v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25111 | complete |
| SF-2026-ARXIV-2603-25120 | RP-cce6da9c03005c36 | standard | arXiv:2603.25120v1 | SRC-ARXIV@arXiv:2603.25120v1 | HTML — §2.1. MLLM Architecture [facet=method]; https://arxiv.org/html/2603.25120v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25120v1.html; sha256:e164359b41040b6d9b15b5354ccaf07a65a633ea4df645a1048f5618d73bfff4 | HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.25120v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25120v1.html; sha256:e164359b41040b6d9b15b5354ccaf07a65a633ea4df645a1048f5618d73bfff4 | HTML — §7. Conclusion [facet=limitations]; https://arxiv.org/html/2603.25120v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25120v1.html; sha256:e164359b41040b6d9b15b5354ccaf07a65a633ea4df645a1048f5618d73bfff4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25120v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25120 | complete |
| SF-2026-ARXIV-2603-25158 | RP-c8657ba44936fd77 | standard | arXiv:2603.25158v1 | SRC-ARXIV@arXiv:2603.25158v1 | HTML — §4.2 Trace2Skill vs. Retrieval-Memory Baseline [facet=method]; https://arxiv.org/html/2603.25158v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25158v1.html; sha256:9b5de0e9d1b15323e637adbe66b223a66e7bf05fd9742eaa24ba99d56ef353bd | HTML — §3.1 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.25158v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25158v1.html; sha256:9b5de0e9d1b15323e637adbe66b223a66e7bf05fd9742eaa24ba99d56ef353bd | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25158v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25158v1.html; sha256:9b5de0e9d1b15323e637adbe66b223a66e7bf05fd9742eaa24ba99d56ef353bd | arXiv exact-v1 identity https://arxiv.org/abs/2603.25158v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25158 | complete |
| SF-2026-ARXIV-2603-25289 | RP-a512f4bc27ef3d1f | standard | arXiv:2603.25289v1 | SRC-ARXIV@arXiv:2603.25289v1 | HTML — §4.2 Experiment Design [facet=method]; https://arxiv.org/html/2603.25289v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25289v1.html; sha256:02c25204be857d5549b4453116f71e54c9221d62fc892535b41a29aba0b5be5f | HTML — §5.1 RQ1: Can a missing participant influence the model evaluation and, therefore, lead to wrong assumptions about the model quality? [facet=evaluation]; https://arxiv.org/html/2603.25289v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25289v1.html; sha256:02c25204be857d5549b4453116f71e54c9221d62fc892535b41a29aba0b5be5f | HTML — §3.1 Participant failures in FL systems [facet=limitations]; https://arxiv.org/html/2603.25289v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25289v1.html; sha256:02c25204be857d5549b4453116f71e54c9221d62fc892535b41a29aba0b5be5f | arXiv exact-v1 identity https://arxiv.org/abs/2603.25289v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25289 | complete |
| SF-2026-ARXIV-2603-25342 | RP-80264576addd67fe | standard | arXiv:2603.25342v1 | SRC-ARXIV@arXiv:2603.25342v1 | HTML — §4 Design of Evaluation [facet=method]; https://arxiv.org/html/2603.25342v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25342v1.html; sha256:aab7c9745935398b820cd3b46431dadeb9c3e4f86de96b1e611086c5ab3e92c0 | HTML — §5.1 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.25342v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25342v1.html; sha256:aab7c9745935398b820cd3b46431dadeb9c3e4f86de96b1e611086c5ab3e92c0 | HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25342v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25342v1.html; sha256:aab7c9745935398b820cd3b46431dadeb9c3e4f86de96b1e611086c5ab3e92c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25342v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25342 | complete |
| SF-2026-ARXIV-2603-25685 | RP-e84008c5e77ed863 | standard | arXiv:2603.25685v1 | SRC-ARXIV@arXiv:2603.25685v1 | HTML — §3 Improving Robot World Models with Reinforcement Learning [facet=method]; https://arxiv.org/html/2603.25685v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25685v1.html; sha256:274c9444d4df2b6328934fea8f3b1422f5ee3dd5bef6133455825115a12b5378 | HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.25685v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25685v1.html; sha256:274c9444d4df2b6328934fea8f3b1422f5ee3dd5bef6133455825115a12b5378 | HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25685v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25685v1.html; sha256:274c9444d4df2b6328934fea8f3b1422f5ee3dd5bef6133455825115a12b5378 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25685v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25685 | complete |
| SF-2026-ARXIV-2603-25702 | RP-ec7e5a9cf1943ab2 | deep | arXiv:2603.25702v1 | SRC-ARXIV@arXiv:2603.25702v1 | HTML — §4.1–§4.4 S2D2 Method [facet=method]; https://arxiv.org/html/2603.25702v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25702v1.html; sha256:0f6bd1451874a9a5a8c2818405bff8dfaff5a753bea92f6ac9317c0f243ec6fa | HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.25702v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25702v1.html; sha256:0f6bd1451874a9a5a8c2818405bff8dfaff5a753bea92f6ac9317c0f243ec6fa | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25702v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25702v1.html; sha256:0f6bd1451874a9a5a8c2818405bff8dfaff5a753bea92f6ac9317c0f243ec6fa | arXiv exact-v1 identity https://arxiv.org/abs/2603.25702v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25702 | complete |
| SF-2026-ARXIV-2603-25716 | RP-7ac4e9476a3df640 | standard | arXiv:2603.25716v1 | SRC-ARXIV@arXiv:2603.25716v1 | HTML — §3.1 Hybrid Memory [facet=method]; https://arxiv.org/html/2603.25716v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25716v1.html; sha256:bdc6024032f86a37aabb420c41ad98fe25369a94ca3f8ce5608a70263c5179e8 | HTML — §5.1 Experiment Setup [facet=evaluation]; https://arxiv.org/html/2603.25716v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25716v1.html; sha256:bdc6024032f86a37aabb420c41ad98fe25369a94ca3f8ce5608a70263c5179e8 | HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.25716v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25716v1.html; sha256:bdc6024032f86a37aabb420c41ad98fe25369a94ca3f8ce5608a70263c5179e8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.25716v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-25716 | complete |

### Source Reviews

### M2K: Making the Model-Kernel Interface Explicit for Reliable CUDA Kernel Verification

<!-- review:SF-2026-ARXIV-2603-24595:start -->
**问题**：模型和 CUDA kernel 独立演进时，tensor shape、buffer extent 与 launch configuration 的隐式约定会变成难复现的 memory bug。

**旧路径为何合理**：通用算子图优先可移植性和实现简单。

**约束变化与机制**：M2K 用 HFProbe 无 GPU 跟踪模型，区分固定/用户可变参数并生成接口约束；cuKLEE 再在这些约束下符号执行 kernel，把 model-kernel contract 变成可检查 artifact。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 kernel、precision、layout 与执行计划 owner；定位证据为 `HTML — §4 Design of Model2Kernel [facet=method]; https://arxiv.org/html/2603.24595v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24595v1.html; sha256:a8850a63800db829f90ecbbb0d8d6c1394a36b2fd27488e97ac1d12d10b56cb0`。

**Evaluation contract 与未证明部分**：真实 LLM inference kernel 上发现 181 个未知 bug、9 个 false positive，支持该接口化验证；覆盖仍受 symbolic model 与 kernel feature 支持限制。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.24595v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24595v1.html; sha256:a8850a63800db829f90ecbbb0d8d6c1394a36b2fd27488e97ac1d12d10b56cb0`。

**Trade-off / failure / coexistence**：显式约束提高 release safety，却增加 tracing、模型版本绑定和 solver 成本；简单静态 shape kernel 仍可用单元/边界测试。

<!-- claim:SF-2026-ARXIV-2603-24595:start -->**Claim Boundary**：只支持 arXiv:2603.24595v1 §4 Design of Model2Kernel 的机制与 §5 Evaluation 的公开 workload；§6 Limitations and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24595:end -->
<!-- review:SF-2026-ARXIV-2603-24595:end -->
### When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs

<!-- review:SF-2026-ARXIV-2603-24676:start -->
**问题**：多 agent 达成 consensus 可能来自随机对称破缺和 memetic drift，而非更强集体推理。

**旧路径为何合理**：单 agent 保持上下文与责任集中。

**约束变化与机制**：论文把 population size、interaction 与初始微小偏置纳入 scaling analysis，区分稳定集体信号与 lottery-like convergence。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 角色、消息、共享状态与失败归属；定位证据为 `HTML — §B.1.3 Method summary and reproducibility [facet=method]; https://arxiv.org/html/2603.24676v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24676v1.html; sha256:7d6add821b8438075a8089e33a388647420bda61689aa886de7253a9ba8a25bd`。

**Evaluation contract 与未证明部分**：命名/协作实验支持所测模型与拓扑下的 drift 规律；不能外推所有任务或把共识等同正确。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4 Experimental Validation [facet=evaluation]; https://arxiv.org/html/2603.24676v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24676v1.html; sha256:7d6add821b8438075a8089e33a388647420bda61689aa886de7253a9ba8a25bd`。

**Trade-off / failure / coexistence**：增加 agent 可提高探索也会放大协调偏差；高度耦合或缺少独立证据时单 agent/固定审议更稳。

<!-- claim:SF-2026-ARXIV-2603-24676:start -->**Claim Boundary**：只支持 arXiv:2603.24676v1 §B.1.3 Method summary and reproducibility 的机制与 §4 Experimental Validation 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24676:end -->
<!-- review:SF-2026-ARXIV-2603-24676:end -->
### SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks

<!-- review:SF-2026-ARXIV-2603-24755:start -->
**问题**：single-shot coding benchmark 会奖励眼前通过测试的 patch，却看不到架构决定如何侵蚀后续迭代。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：SlopCodeBench 让同一 agent 连续扩展自己先前的实现，并在 196 checkpoints 分开测 correctness、structural erosion 与 verbosity。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §2.1 Design Principles [facet=method]; https://arxiv.org/html/2603.24755v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24755v1.html; sha256:b723eec019870dcbbbca8d1ab8897d5135ce79562f787a47df6889b05ddee94a`。

**Evaluation contract 与未证明部分**：36 个问题、15 个 agent 与开源仓库对照支持 agent code 会随迭代累积退化；任务语言、metric 与 checkpoint 设计限制泛化。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.24755v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24755v1.html; sha256:b723eec019870dcbbbca8d1ab8897d5135ce79562f787a47df6889b05ddee94a`。

**Trade-off / failure / coexistence**：长程 benchmark 更接近维护，却昂贵且指标可能偏好特定结构；局部 bugfix 仍可保留 single-shot 测试，但不能代表可维护性。

<!-- claim:SF-2026-ARXIV-2603-24755:start -->**Claim Boundary**：只支持 arXiv:2603.24755v1 §2.1 Design Principles 的机制与 §3 Experimental Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24755:end -->
<!-- review:SF-2026-ARXIV-2603-24755:end -->
### AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A

<!-- review:SF-2026-ARXIV-2603-24775:start -->
**问题**：MCP/A2A 能传 tool call 与 delegation，却未把调用者身份、可衰减权限和 completion provenance 绑定成同一可验证链。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：AIP 的 IBCT 把 compact signed JWT 与多跳 Biscuit/Datalog chain 分开，holder 只能收窄权限，并把 invocation context 绑定到 completion record。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `HTML — §3.3 Completion Blocks and Trust Model [facet=method]; https://arxiv.org/html/2603.24775v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24775v1.html; sha256:f6e5221edee364e31e6a05a027322e5c0eaf5c730977e7f67ac85c80bbc41469`。

**Evaluation contract 与未证明部分**：跨 Python/Rust、真实 MCP/A2A 与 600 次攻击评估支持所测拒绝率和低开销；不覆盖密钥泄漏、撤销传播或所有 transport。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.24775v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24775v1.html; sha256:f6e5221edee364e31e6a05a027322e5c0eaf5c730977e7f67ac85c80bbc41469`。

**Trade-off / failure / coexistence**：可验证 delegation 增加 key lifecycle、clock/revocation 和 policy complexity；单 hop、同一信任域仍可用较简单 token，但匿名调用不应进入高权限链。

<!-- claim:SF-2026-ARXIV-2603-24775:start -->**Claim Boundary**：只支持 arXiv:2603.24775v1 §3.3 Completion Blocks and Trust Model 的机制与 §5 Evaluation 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24775:end -->
<!-- review:SF-2026-ARXIV-2603-24775:end -->
### Design Once, Deploy at Scale: Template-Driven ML Development for Large Model Ecosystems

<!-- review:SF-2026-ARXIV-2603-24963:start -->
**问题**：每个推荐模型独立定制能贴合局部目标，却让同一训练/serving 技术在大模型生态中以乘法成本传播。

**旧路径为何合理**：单团队脚本可快速交付模型服务。

**约束变化与机制**：SMT 把可组合模型部件与适配点标准化，使 technique 与 model family 的演进从逐对维护转成模板 lineage 与受控 specialization。

**State / data / control owner**：`PLATFORM-FOUNDATIONS` 负责 资产、workload、service 与 controller ownership；定位证据为 `HTML — §4 Experimental Design [facet=method]; https://arxiv.org/html/2603.24963v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24963v1.html; sha256:323d662ae52fe2d80852eb80d995d790b56a60cda8ba6f8539667df6bec68bdf`。

**Evaluation contract 与未证明部分**：Meta 广告系统四个开发周期支持所测生态的工程时间、adoption throughput 与 neutral-capacity 指标；组织、模型族和生产数据不可直接外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4 Experimental Design [facet=evaluation]; https://arxiv.org/html/2603.24963v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.24963v1.html; sha256:323d662ae52fe2d80852eb80d995d790b56a60cda8ba6f8539667df6bec68bdf`。

**Trade-off / failure / coexistence**：模板降低传播成本却可能压平真正需要专用结构的目标，并形成中心模板 blast radius；少量高异质模型仍可独立优化。

<!-- claim:SF-2026-ARXIV-2603-24963:start -->**Claim Boundary**：只支持 arXiv:2603.24963v1 §4 Experimental Design 的机制与 §4 Experimental Design 的公开 workload；§6.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-24963:end -->
<!-- review:SF-2026-ARXIV-2603-24963:end -->
### The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities

<!-- review:SF-2026-ARXIV-2603-25056:start -->
**问题**：把 system prompt 当作安全策略最便宜，但 prompt 中某个高相关启发式一旦被攻击者反转，模型会忠实执行错误假设。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：PhishNChips 系统扫描 model×prompt configuration，追踪 response reasoning，并用 Safetility 同时计入 recall 与 false-positive cost，把 prompt 版本变成安全评估对象。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §3.1 Threat Model [facet=method]; https://arxiv.org/html/2603.25056v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25056v1.html; sha256:98ded9fba081c4d1fbc0c7aad5ca16c8d98511b3f0a7d120968e2de234374b05`。

**Evaluation contract 与未证明部分**：11 个模型、10 种策略与 phishing/legitimate 集合支持配置可让同一模型跨越巨大 bypass 区间；数据分布和邮件域限制结论。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.2 Cross-Model Generalization and the Instruction Specificity Paradox [facet=evaluation]; https://arxiv.org/html/2603.25056v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25056v1.html; sha256:98ded9fba081c4d1fbc0c7aad5ca16c8d98511b3f0a7d120968e2de234374b05`。

**Trade-off / failure / coexistence**：更具体 prompt 可提升平均检测又制造单信号脆弱性；需要外部 ground truth、ensemble 与 tool verification，不能把 prompt 固化为 reference monitor。

<!-- claim:SF-2026-ARXIV-2603-25056:start -->**Claim Boundary**：只支持 arXiv:2603.25056v1 §3.1 Threat Model 的机制与 §5.2 Cross-Model Generalization and the Instruction Specificity Paradox 的公开 workload；§7.6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25056:end -->
<!-- review:SF-2026-ARXIV-2603-25056:end -->
### SEVerA: Verified Synthesis of Self-Evolving Agents

<!-- review:SF-2026-ARXIV-2603-25111:start -->
**问题**：self-evolving agent 若能改写自身策略或代码，仅用结果测试无法证明每次变化仍满足安全约束。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SEVerA 把候选演化、形式化 specification、verified synthesis 与 acceptance gate 连成闭环，使修改必须携带可检查 proof obligation。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `HTML — §6.1.2. Implementation Details [facet=method]; https://arxiv.org/html/2603.25111v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25111v1.html; sha256:7e541b1bdb536e75cc999b9a9a43334418387cd3e22a014ce92d042fed298029`。

**Evaluation contract 与未证明部分**：公开任务验证支持论文形式系统覆盖的性质；不能证明自然语言 specification 完整，也不覆盖 verifier bug。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §6.2. Main Results [facet=evaluation]; https://arxiv.org/html/2603.25111v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25111v1.html; sha256:7e541b1bdb536e75cc999b9a9a43334418387cd3e22a014ce92d042fed298029`。

**Trade-off / failure / coexistence**：证明门槛限制搜索空间并增加 solver 成本；低风险、可快速 rollback 的变化可用测试加审计。

<!-- claim:SF-2026-ARXIV-2603-25111:start -->**Claim Boundary**：只支持 arXiv:2603.25111v1 §6.1.2. Implementation Details 的机制与 §6.2. Main Results 的公开 workload；§6.5. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25111:end -->
<!-- review:SF-2026-ARXIV-2603-25111:end -->
### DFLOP: A Data-driven Framework for Multimodal LLM Training Pipeline Optimization

<!-- review:SF-2026-ARXIV-2603-25120:start -->
**问题**：多模态训练的 data loader、通信、memory 与算子瓶颈会随模态配比改变，固定 pipeline 参数难以保持效率。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：DFLOP 从运行 profile 学习数据驱动的 pipeline 配置，在阶段间联合调节 batch、并行与资源分配。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `HTML — §2.1. MLLM Architecture [facet=method]; https://arxiv.org/html/2603.25120v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25120v1.html; sha256:e164359b41040b6d9b15b5354ccaf07a65a633ea4df645a1048f5618d73bfff4`。

**Evaluation contract 与未证明部分**：实验支持指定模型、集群和 modality workload 的吞吐改进；不证明 learned policy 跨硬件或数据分布稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.25120v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25120v1.html; sha256:e164359b41040b6d9b15b5354ccaf07a65a633ea4df645a1048f5618d73bfff4`。

**Trade-off / failure / coexistence**：动态优化减少手工调参，却新增 profiling 开销、控制振荡和复现难度；稳定 workload 仍宜冻结配置。

<!-- claim:SF-2026-ARXIV-2603-25120:start -->**Claim Boundary**：只支持 arXiv:2603.25120v1 §2.1. MLLM Architecture 的机制与 §5. Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25120:end -->
<!-- review:SF-2026-ARXIV-2603-25120:end -->
### Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

<!-- review:SF-2026-ARXIV-2603-25158:start -->
**问题**：人工编写 skill 难扩展，单条 trajectory 直接记忆又会把偶然步骤和局部错误固化成程序。

**旧路径为何合理**：把 agent 当进程内 loop 能快速试验。

**约束变化与机制**：Trace2Skill 并行归纳多条 execution trajectory，把反复出现的 failure/workaround 压缩为统一 skill directory，并在模型/任务间验证 transfer。

**State / data / control owner**：`AGENT-PLATFORM` 负责 agent identity、skill、execution state 与控制面；定位证据为 `HTML — §4.2 Trace2Skill vs. Retrieval-Memory Baseline [facet=method]; https://arxiv.org/html/2603.25158v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25158v1.html; sha256:9b5de0e9d1b15323e637adbe66b223a66e7bf05fd9742eaa24ba99d56ef353bd`。

**Evaluation contract 与未证明部分**：office、math、vision QA 及跨模型实验支持部分 skill 可迁移；高增益案例不证明所有归纳规则都正确或安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §3.1 Experimental Setup [facet=evaluation]; https://arxiv.org/html/2603.25158v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25158v1.html; sha256:9b5de0e9d1b15323e637adbe66b223a66e7bf05fd9742eaa24ba99d56ef353bd`。

**Trade-off / failure / coexistence**：经验蒸馏减少重复探索，却引入错误归纳、适用域漂移与供应链风险；稀有高风险操作仍需人工规则和 held-out gate。

<!-- claim:SF-2026-ARXIV-2603-25158:start -->**Claim Boundary**：只支持 arXiv:2603.25158v1 §4.2 Trace2Skill vs. Retrieval-Memory Baseline 的机制与 §3.1 Experimental Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25158:end -->
<!-- review:SF-2026-ARXIV-2603-25158:end -->
### Revealing the influence of participant failures on model quality in cross-silo Federated Learning

<!-- review:SF-2026-ARXIV-2603-25289:start -->
**问题**：cross-silo federated learning 中 participant dropout/straggler 不只降低吞吐，还会系统性改变每轮数据代表性和最终模型质量。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：论文把 failure pattern、参与集合与聚合结果关联，要求 runtime 同时跟踪 availability state 与 statistical contribution，而非只重试通信。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `HTML — §4.2 Experiment Design [facet=method]; https://arxiv.org/html/2603.25289v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25289v1.html; sha256:02c25204be857d5549b4453116f71e54c9221d62fc892535b41a29aba0b5be5f`。

**Evaluation contract 与未证明部分**：实验能支持所测数据异质性和故障率下的质量变化；不能外推任意聚合器或现实组织行为。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.1 RQ1: Can a missing participant influence the model evaluation and, therefore, lead to wrong assumptions about the model quality? [facet=evaluation]; https://arxiv.org/html/2603.25289v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25289v1.html; sha256:02c25204be857d5549b4453116f71e54c9221d62fc892535b41a29aba0b5be5f`。

**Trade-off / failure / coexistence**：failure-aware selection 提高鲁棒性却可能长期排除弱节点并引入公平偏差；稳定全参与环境仍可使用标准 FedAvg。

<!-- claim:SF-2026-ARXIV-2603-25289:start -->**Claim Boundary**：只支持 arXiv:2603.25289v1 §4.2 Experiment Design 的机制与 §5.1 RQ1: Can a missing participant influence the model evaluation and, therefore, lead to wrong assumptions about the model quality? 的公开 workload；§3.1 Participant failures in FL systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25289:end -->
<!-- review:SF-2026-ARXIV-2603-25289:end -->
### From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents

<!-- review:SF-2026-ARXIV-2603-25342:start -->
**问题**：deep-research agent 只按最终答案打分，无法定位意图分解、证据覆盖和推理结构在哪一步失真。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：该工作用 categorical structure 表达 intent→subclaim→evidence→conclusion 的可达/一致关系，把 process evidence 与 outcome 分开验证。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `HTML — §4 Design of Evaluation [facet=method]; https://arxiv.org/html/2603.25342v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25342v1.html; sha256:aab7c9745935398b820cd3b46431dadeb9c3e4f86de96b1e611086c5ab3e92c0`。

**Evaluation contract 与未证明部分**：所给任务和 evaluator 支持结构指标的诊断价值；LLM judge 与类别映射不等于事实真值。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.1 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.25342v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25342v1.html; sha256:aab7c9745935398b820cd3b46431dadeb9c3e4f86de96b1e611086c5ab3e92c0`。

**Trade-off / failure / coexistence**：结构化评估提高可解释性但增加标注与 schema bias；短事实查询仍可直接核对答案。

<!-- claim:SF-2026-ARXIV-2603-25342:start -->**Claim Boundary**：只支持 arXiv:2603.25342v1 §4 Design of Evaluation 的机制与 §5.1 Evaluation Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25342:end -->
<!-- review:SF-2026-ARXIV-2603-25342:end -->
### Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning

<!-- review:SF-2026-ARXIV-2603-25685:start -->
**问题**：robot world model 用真实历史 teacher forcing 训练时，部署却消费自身预测，autoregressive rollout 因分布漂移快速崩坏。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：论文在模型自己的 rollout state 上做 diffusion RL，用同一状态的多个可变长 future 和多视角 fidelity reward 形成相对更新。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3 Improving Robot World Models with Reinforcement Learning [facet=method]; https://arxiv.org/html/2603.25685v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25685v1.html; sha256:274c9444d4df2b6328934fea8f3b1422f5ee3dd5bef6133455825115a12b5378`。

**Evaluation contract 与未证明部分**：DROID 上的图像指标、pairwise 与人评支持所测 rollout 稳定性；视觉 fidelity reward 不证明动作因果或真实任务成功。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.25685v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25685v1.html; sha256:274c9444d4df2b6328934fea8f3b1422f5ee3dd5bef6133455825115a12b5378`。

**Trade-off / failure / coexistence**：on-rollout post-training 缓解 compounding error，却增加生成成本并可能 reward hack；短 horizon 或有可靠 simulator 时监督训练仍更简单。

<!-- claim:SF-2026-ARXIV-2603-25685:start -->**Claim Boundary**：只支持 arXiv:2603.25685v1 §3 Improving Robot World Models with Reinforcement Learning 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25685:end -->
<!-- review:SF-2026-ARXIV-2603-25685:end -->
### S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation

<!-- review:SF-2026-ARXIV-2603-25702:start -->
**问题**：block diffusion 在少 denoising step 时阈值激进会损伤质量，保守又失去并行加速。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：S2D2 让同一 block-diffusion 模型以 block-size=1 充当 AR verifier，并用轻量 router 只在值得时验证 diffusion proposal。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `HTML — §4.1–§4.4 S2D2 Method [facet=method]; https://arxiv.org/html/2603.25702v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25702v1.html; sha256:0f6bd1451874a9a5a8c2818405bff8dfaff5a753bea92f6ac9317c0f243ec6fa`。

**Evaluation contract 与未证明部分**：三个模型 family 的 accuracy-speed 实验支持所测配置优于阈值 baseline；收益绑定 router、接受率和 block schedule。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.25702v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25702v1.html; sha256:0f6bd1451874a9a5a8c2818405bff8dfaff5a753bea92f6ac9317c0f243ec6fa`。

**Trade-off / failure / coexistence**：self-verification 无需第二模型，却增加 mode switch、rollback 与重复 compute；小 batch 或低接受率时普通 AR/diffusion decode 仍更稳。

<!-- claim:SF-2026-ARXIV-2603-25702:start -->**Claim Boundary**：只支持 arXiv:2603.25702v1 §4.1–§4.4 的 same-model block-size-one verifier、routing policy 与 fallback，以及 §5 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25702:end -->
<!-- review:SF-2026-ARXIV-2603-25702:end -->
### Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models

<!-- review:SF-2026-ARXIV-2603-25716:start -->
**问题**：只保存静态背景的 video memory 无法解释动态主体离开视野后继续运动并重新出现。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：HyDRA 把 static archive 与 dynamic subject track 分开，以压缩 memory token 和时空相关检索维持 hidden subject 的 identity/motion。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `HTML — §3.1 Hybrid Memory [facet=method]; https://arxiv.org/html/2603.25716v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25716v1.html; sha256:bdc6024032f86a37aabb420c41ad98fe25369a94ca3f8ce5608a70263c5179e8`。

**Evaluation contract 与未证明部分**：HM-World 59K clips 与对比实验支持 exit-entry 场景的一致性收益；数据集和生成指标不能证明开放世界 object permanence。 未披露的字段保持 `Not Disclosed`，具体定位为 `HTML — §5.1 Experiment Setup [facet=evaluation]; https://arxiv.org/html/2603.25716v1; papers/2026/03/_sources/daily-20260327/exact-v1-bodies/2603.25716v1.html; sha256:bdc6024032f86a37aabb420c41ad98fe25369a94ca3f8ce5608a70263c5179e8`。

**Trade-off / failure / coexistence**：hybrid memory 改善动态连续性，却增加 entity association、stale motion 和 retrieval error；无遮挡短视频仍可用局部 context。

<!-- claim:SF-2026-ARXIV-2603-25716:start -->**Claim Boundary**：只支持 arXiv:2603.25716v1 §3.1 Hybrid Memory 的机制与 §5.1 Experiment Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-25716:end -->
<!-- review:SF-2026-ARXIV-2603-25716:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-24595 | score_7_9;potential_books_delta | selected | DA-20260327-01 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260327-01 |
| SF-2026-ARXIV-2603-24775 | score_7_9;potential_books_delta | selected | DA-20260327-04 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260327-04 |
| SF-2026-ARXIV-2603-25702 | score_7_9;potential_books_delta | selected | DA-20260327-13 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260327-13 |

<!-- analysis:DA-20260327-01:start -->
### M2K: Making the Model-Kernel Interface Explicit for Reliable CUDA Kernel Verification

模型和 CUDA kernel 独立演进时，tensor shape、buffer extent 与 launch configuration 的隐式约定会变成难复现的 memory bug。 旧路径在其原约束下仍合理：通用算子图优先可移植性和实现简单。 本 family 的设计变化是：M2K 用 HFProbe 无 GPU 跟踪模型，区分固定/用户可变参数并生成接口约束；cuKLEE 再在这些约束下符号执行 kernel，把 model-kernel contract 变成可检查 artifact。 其公开验证边界为：真实 LLM inference kernel 上发现 181 个未知 bug、9 个 false positive，支持该接口化验证；覆盖仍受 symbolic model 与 kernel feature 支持限制。 新增代价与回退条件为：显式约束提高 release safety，却增加 tracing、模型版本绑定和 solver 成本；简单静态 shape kernel 仍可用单元/边界测试。
<!-- analysis:DA-20260327-01:end -->
<!-- analysis:DA-20260327-04:start -->
### AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A

MCP/A2A 能传 tool call 与 delegation，却未把调用者身份、可衰减权限和 completion provenance 绑定成同一可验证链。 旧路径在其原约束下仍合理：把协议当作普通 tool adapter，部署和权限模型最简单。 本 family 的设计变化是：AIP 的 IBCT 把 compact signed JWT 与多跳 Biscuit/Datalog chain 分开，holder 只能收窄权限，并把 invocation context 绑定到 completion record。 其公开验证边界为：跨 Python/Rust、真实 MCP/A2A 与 600 次攻击评估支持所测拒绝率和低开销；不覆盖密钥泄漏、撤销传播或所有 transport。 新增代价与回退条件为：可验证 delegation 增加 key lifecycle、clock/revocation 和 policy complexity；单 hop、同一信任域仍可用较简单 token，但匿名调用不应进入高权限链。
<!-- analysis:DA-20260327-04:end -->
<!-- analysis:DA-20260327-13:start -->
### S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation

block diffusion 在少 denoising step 时阈值激进会损伤质量，保守又失去并行加速。 旧路径在其原约束下仍合理：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。 本 family 的设计变化是：S2D2 让同一 block-diffusion 模型以 block-size=1 充当 AR verifier，并用轻量 router 只在值得时验证 diffusion proposal。 其公开验证边界为：三个模型 family 的 accuracy-speed 实验支持所测配置优于阈值 baseline；收益绑定 router、接受率和 block schedule。 新增代价与回退条件为：self-verification 无需第二模型，却增加 mode switch、rollback 与重复 compute；小 batch 或低接受率时普通 AR/diffusion decode 仍更稳。
<!-- analysis:DA-20260327-13:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-24595 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24595 | delta:SF-2026-ARXIV-2603-24595 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-24595 |
| SF-2026-ARXIV-2603-24676 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#mcp-不等于-tool-authorization (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24676 | delta:SF-2026-ARXIV-2603-24676 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24676 |
| SF-2026-ARXIV-2603-24755 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24755 | delta:SF-2026-ARXIV-2603-24755 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24755 |
| SF-2026-ARXIV-2603-24775 | AGENT-MCP | books/part-07-agent/83-mcp.md#authorization-之前还需要可验证的-server-admission (section Ch-owner) | books/part-07-agent/82-multi-agent.md#扩展-agent-数量之前，先测量-coordination-tax (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#从-trajectory-到-skill-是一次受治理的-compilation (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24775 | delta:SF-2026-ARXIV-2603-24775 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-24775 |
| SF-2026-ARXIV-2603-24963 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/56-inference-scheduling.md#第56章-推理调度 (section Ch-adjacent); books/part-06-ai-infrastructure/58-kubeflow.md#第58章-组合式-ml-platform：以-kubeflow-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-24963 | delta:SF-2026-ARXIV-2603-24963 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-24963 |
| SF-2026-ARXIV-2603-25056 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#局部合理动作会累积成有害轨迹 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25056 | delta:SF-2026-ARXIV-2603-25056 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25056 |
| SF-2026-ARXIV-2603-25111 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#readiness-gates (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25111 | delta:SF-2026-ARXIV-2603-25111 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25111 |
| SF-2026-ARXIV-2603-25120 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#arrival-bias-与-stale-direction-是两种独立误差 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25120 | delta:SF-2026-ARXIV-2603-25120 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25120 |
| SF-2026-ARXIV-2603-25158 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#可复用-skill-不是一个-prompt-文件 (section Ch-owner) | books/part-07-agent/83-mcp.md#mcp-不等于-tool-authorization (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25158 | delta:SF-2026-ARXIV-2603-25158 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25158 |
| SF-2026-ARXIV-2603-25289 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#从本机协作到分布式执行 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25289 | delta:SF-2026-ARXIV-2603-25289 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25289 |
| SF-2026-ARXIV-2603-25342 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#self-report、behavior-probe-与-deployment-outcome-是三种证据 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25342 | delta:SF-2026-ARXIV-2603-25342 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25342 |
| SF-2026-ARXIV-2603-25685 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25685 | delta:SF-2026-ARXIV-2603-25685 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25685 |
| SF-2026-ARXIV-2603-25702 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-可以修订，但只能在安全边界-commit (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25702 | delta:SF-2026-ARXIV-2603-25702 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-25702 |
| SF-2026-ARXIV-2603-25716 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#latency-与-control-frequency (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-25716 | delta:SF-2026-ARXIV-2603-25716 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-25716 |

<!-- books-review:SF-2026-ARXIV-2603-24595:start -->
### M2K: Making the Model-Kernel Interface Explicit for Reliable CUDA Kernel Verification — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24595:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：独立 kernel launch 对大算子、稳定 control flow 和容易 capture 的 shape 最透明，CPU submission 开销相对计算也很小；CUDA Graph 进一步把重复 DAG 的准备成本移出 hot path。动态 inference、attention 辅助操作和 micro-batch 中出现大量短小算子后，单次 CPU→GPU launch 可能比算子本身更贵，而 graph 又要求可重复的结构，此时静态 fusion 与 graph capture 之间出现一个运行时分支。<!-- existing:SF-2026-ARXIV-2603-24595:end -->

<!-- delta:SF-2026-ARXIV-2603-24595:start -->新证据差异：M2K 用 HFProbe 无 GPU 跟踪模型，区分固定/用户可变参数并生成接口约束；cuKLEE 再在这些约束下符号执行 kernel，把 model-kernel contract 变成可检查 artifact。<!-- delta:SF-2026-ARXIV-2603-24595:end -->

边界：只支持 arXiv:2603.24595v1 §4 Design of Model2Kernel 的机制与 §5 Evaluation 的公开 workload；§6 Limitations and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-24595:end -->
<!-- books-review:SF-2026-ARXIV-2603-24676:start -->
### When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24676:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-24676:end -->

<!-- delta:SF-2026-ARXIV-2603-24676:start -->新证据差异：论文把 population size、interaction 与初始微小偏置纳入 scaling analysis，区分稳定集体信号与 lottery-like convergence。<!-- delta:SF-2026-ARXIV-2603-24676:end -->

边界：只支持 arXiv:2603.24676v1 §B.1.3 Method summary and reproducibility 的机制与 §4 Experimental Validation 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24676:end -->
<!-- books-review:SF-2026-ARXIV-2603-24755:start -->
### SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24755:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-24755:end -->

<!-- delta:SF-2026-ARXIV-2603-24755:start -->新证据差异：SlopCodeBench 让同一 agent 连续扩展自己先前的实现，并在 196 checkpoints 分开测 correctness、structural erosion 与 verbosity。<!-- delta:SF-2026-ARXIV-2603-24755:end -->

边界：只支持 arXiv:2603.24755v1 §2.1 Design Principles 的机制与 §3 Experimental Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24755:end -->
<!-- books-review:SF-2026-ARXIV-2603-24775:start -->
### AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24775:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。<!-- existing:SF-2026-ARXIV-2603-24775:end -->

<!-- delta:SF-2026-ARXIV-2603-24775:start -->新证据差异：AIP 的 IBCT 把 compact signed JWT 与多跳 Biscuit/Datalog chain 分开，holder 只能收窄权限，并把 invocation context 绑定到 completion record。<!-- delta:SF-2026-ARXIV-2603-24775:end -->

边界：只支持 arXiv:2603.24775v1 §3.3 Completion Blocks and Trust Model 的机制与 §5 Evaluation 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **Integrate**；已按日期顺序写回 canonical owner，并通过非写作者 post-write Semantic Audit。
<!-- books-review:SF-2026-ARXIV-2603-24775:end -->
<!-- books-review:SF-2026-ARXIV-2603-24963:start -->
### Design Once, Deploy at Scale: Template-Driven ML Development for Large Model Ecosystems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-24963:start -->已读 owner `books/part-06-ai-infrastructure/57-what-is-ai-platform.md` 与相邻章节。现有命题：本章的核心判断是：**AI Platform 是围绕 AI 资产与昂贵计算建立的一组稳定契约和控制闭环。它把异构工具转化为可复用、自助、可治理的能力，但不掩盖底层模型与资源约束。**<!-- existing:SF-2026-ARXIV-2603-24963:end -->

<!-- delta:SF-2026-ARXIV-2603-24963:start -->新证据差异：SMT 把可组合模型部件与适配点标准化，使 technique 与 model family 的演进从逐对维护转成模板 lineage 与受控 specialization。<!-- delta:SF-2026-ARXIV-2603-24963:end -->

边界：只支持 arXiv:2603.24963v1 §4 Experimental Design 的机制与 §4 Experimental Design 的公开 workload；§6.3 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-24963:end -->
<!-- books-review:SF-2026-ARXIV-2603-25056:start -->
### The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security and Creates Exploitable Vulnerabilities — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25056:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：多 Agent 委派把这条链再推进一步：有害目标可能被拆成多个局部合理的子任务，单节点重新做 prompt classification 仍看不见跨节点累积的语义。运行时需要把 source、delegation、memory write 与 irreversible sink 组织成带 provenance 的信息流，在 sink 前重建跨节点上下文，再由确定性 policy 决定是否允许 commit。 这用额外图状态、标注误差和重建延迟换取跨委派风险可见性；semantic taint 仍只是 sensor input，不替代 capability isolation，也不能授权 LLM 自己拥有最终安全判决。<!-- existing:SF-2026-ARXIV-2603-25056:end -->

<!-- delta:SF-2026-ARXIV-2603-25056:start -->新证据差异：PhishNChips 系统扫描 model×prompt configuration，追踪 response reasoning，并用 Safetility 同时计入 recall 与 false-positive cost，把 prompt 版本变成安全评估对象。<!-- delta:SF-2026-ARXIV-2603-25056:end -->

边界：只支持 arXiv:2603.25056v1 §3.1 Threat Model 的机制与 §5.2 Cross-Model Generalization and the Instruction Specificity Paradox 的公开 workload；§7.6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25056:end -->
<!-- books-review:SF-2026-ARXIV-2603-25111:start -->
### SEVerA: Verified Synthesis of Self-Evolving Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25111:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-25111:end -->

<!-- delta:SF-2026-ARXIV-2603-25111:start -->新证据差异：SEVerA 把候选演化、形式化 specification、verified synthesis 与 acceptance gate 连成闭环，使修改必须携带可检查 proof obligation。<!-- delta:SF-2026-ARXIV-2603-25111:end -->

边界：只支持 arXiv:2603.25111v1 §6.1.2. Implementation Details 的机制与 §6.2. Main Results 的公开 workload；§6.5. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25111:end -->
<!-- books-review:SF-2026-ARXIV-2603-25120:start -->
### DFLOP: A Data-driven Framework for Multimodal LLM Training Pipeline Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25120:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：**Trade-off、failure、共存与回退。** quality feedback 可能偏置 sampling，选择同步会制造 stale embedding；graph workloads 与硬件不证明 LLM training 或最终收敛等价。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。<!-- existing:SF-2026-ARXIV-2603-25120:end -->

<!-- delta:SF-2026-ARXIV-2603-25120:start -->新证据差异：DFLOP 从运行 profile 学习数据驱动的 pipeline 配置，在阶段间联合调节 batch、并行与资源分配。<!-- delta:SF-2026-ARXIV-2603-25120:end -->

边界：只支持 arXiv:2603.25120v1 §2.1. MLLM Architecture 的机制与 §5. Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25120:end -->
<!-- books-review:SF-2026-ARXIV-2603-25158:start -->
### Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25158:start -->已读 owner `books/part-07-agent/84-agent-platform.md` 与相邻章节。现有命题：Scan 只能发现已编码规则，signature 只证明 publisher/digest，Skill card 只是声明；三者都不授予 tool、data 或 runtime authority。真正执行仍需 task compatibility、least privilege、sandbox 与第 66 章的 trajectory/outcome evaluation。NVIDIA verified skills 提供了这条发布链的官方实现案例，但不能证明被验证 Skill 在所有 Agent、 environment 或版本下安全有效。人工维护的封闭 Skill set 在高风险、稳定 SOP 或证据不足时仍合理。<!-- existing:SF-2026-ARXIV-2603-25158:end -->

<!-- delta:SF-2026-ARXIV-2603-25158:start -->新证据差异：Trace2Skill 并行归纳多条 execution trajectory，把反复出现的 failure/workaround 压缩为统一 skill directory，并在模型/任务间验证 transfer。<!-- delta:SF-2026-ARXIV-2603-25158:end -->

边界：只支持 arXiv:2603.25158v1 §4.2 Trace2Skill vs. Retrieval-Memory Baseline 的机制与 §3.1 Experimental Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25158:end -->
<!-- books-review:SF-2026-ARXIV-2603-25289:start -->
### Revealing the influence of participant failures on model quality in cross-silo Federated Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25289:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：因此，从 IPC 到 MPI 不是“一个更快的通信 API”这么简单，而是协作范围、participant identity 和 group semantics 的扩展。<!-- existing:SF-2026-ARXIV-2603-25289:end -->

<!-- delta:SF-2026-ARXIV-2603-25289:start -->新证据差异：论文把 failure pattern、参与集合与聚合结果关联，要求 runtime 同时跟踪 availability state 与 statistical contribution，而非只重试通信。<!-- delta:SF-2026-ARXIV-2603-25289:end -->

边界：只支持 arXiv:2603.25289v1 §4.2 Experiment Design 的机制与 §5.1 RQ1: Can a missing participant influence the model evaluation and, therefore, lead to wrong assumptions about the model quality? 的公开 workload；§3.1 Participant failures in FL systems 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25289:end -->
<!-- books-review:SF-2026-ARXIV-2603-25342:start -->
### From Intent to Evidence: A Categorical Approach for Structural Evaluation of Deep Research Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25342:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失： 写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge 与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。<!-- existing:SF-2026-ARXIV-2603-25342:end -->

<!-- delta:SF-2026-ARXIV-2603-25342:start -->新证据差异：该工作用 categorical structure 表达 intent→subclaim→evidence→conclusion 的可达/一致关系，把 process evidence 与 outcome 分开验证。<!-- delta:SF-2026-ARXIV-2603-25342:end -->

边界：只支持 arXiv:2603.25342v1 §4 Design of Evaluation 的机制与 §5.1 Evaluation Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25342:end -->
<!-- books-review:SF-2026-ARXIV-2603-25685:start -->
### Persistent Robot World Models: Stabilizing Multi-Step Rollouts via Reinforcement Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25685:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-25685:end -->

<!-- delta:SF-2026-ARXIV-2603-25685:start -->新证据差异：论文在模型自己的 rollout state 上做 diffusion RL，用同一状态的多个可变长 future 和多视角 fidelity reward 形成相对更新。<!-- delta:SF-2026-ARXIV-2603-25685:end -->

边界：只支持 arXiv:2603.25685v1 §3 Improving Robot World Models with Reinforcement Learning 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25685:end -->
<!-- books-review:SF-2026-ARXIV-2603-25702:start -->
### S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25702:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2603-25702:end -->

<!-- delta:SF-2026-ARXIV-2603-25702:start -->新证据差异：S2D2 让同一 block-diffusion 模型以 block-size=1 充当 AR verifier，并用轻量 router 只在值得时验证 diffusion proposal。<!-- delta:SF-2026-ARXIV-2603-25702:end -->

边界：只支持 arXiv:2603.25702v1 §4.1–§4.4 的 same-model block-size-one verifier、routing policy 与 fallback，以及 §5 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；正文已写回，当前等待非作者 post-write semantic audit。
<!-- books-review:SF-2026-ARXIV-2603-25702:end -->
<!-- books-review:SF-2026-ARXIV-2603-25716:start -->
### Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-25716:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：一个模型能生成逼真视频，是否已经“理解世界”？能够预测下一帧，是否足以支持 planning？World Model 与 simulator、Agent Memory 有何边界？模型在内部 imagined rollout 时，谁保存事实状态，谁保存预测状态，又怎样在新 observation 到来后修正？<!-- existing:SF-2026-ARXIV-2603-25716:end -->

<!-- delta:SF-2026-ARXIV-2603-25716:start -->新证据差异：HyDRA 把 static archive 与 dynamic subject track 分开，以压缩 memory token 和时空相关检索维持 hidden subject 的 identity/motion。<!-- delta:SF-2026-ARXIV-2603-25716:end -->

边界：只支持 arXiv:2603.25716v1 §3.1 Hybrid Memory 的机制与 §5.1 Experiment Setup 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-25716:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260327-COVERAGE | fresh-context:march-lane-c-reviewer | coverage | fresh-context-audit:lane-c | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260327-EVIDENCE | fresh-context:march-lane-c-reviewer | evidence | fresh-context-audit:lane-c;validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260327-SELECTION | fresh-context:march-lane-c-reviewer | deep_analysis_selection | fresh-context-audit:lane-c;validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260327-BOOKS | fresh-context:march-lane-c-reviewer | books | fresh-context-audit:lane-c;validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260327/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/48-speculative-decoding.md`。
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
- 更新并复核 `books/part-07-agent/83-mcp.md`。
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
