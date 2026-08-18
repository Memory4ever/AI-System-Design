# Daily Research — 2026-07-23

**Research Date:** 2026-07-23

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-22 09:00:00 ～ 2026-07-23 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1063 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 14 个。当前路由账目为 11 个 Deep、1 个 Standard、2 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-23 |
| Window End | 2026-07-23 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-23-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T13:50:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-22T09:00:00+08:00 | 2026-07-23T09:00:00+08:00 | 2026-08-27T13:50:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1063 | SF-2026-ARXIV-2607-19704<br>SF-2026-ARXIV-2607-19747<br>SF-2026-ARXIV-2607-19749<br>SF-2026-ARXIV-2607-19865<br>SF-2026-ARXIV-2607-19957<br>SF-2026-ARXIV-2607-27231<br>SF-2026-ARXIV-2607-20145<br>SF-2026-ARXIV-2607-20159<br>SF-2026-ARXIV-2607-20220<br>SF-2026-ARXIV-2607-20345<br>SF-2026-ARXIV-2607-20379<br>SF-2026-ARXIV-2607-20694<br>SF-2026-ARXIV-2607-20734<br>SF-2026-ARXIV-2607-20757 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-23T09:00:00+08:00 | coverage:SRC-ARXIV:20260723 | GAP-ARXIV-DIRECT-RESET-20260723 |
| SRC-GITHUB-COMMIT | 2026-07-22T09:00:00+08:00 | 2026-07-23T09:00:00+08:00 | 2026-08-27T13:50:00+08:00 | exact GitHub commit API lookups: https://github.com/Rubric4Setwise/Rubric4Setwise@d6e502f6ad57e98eb288bbd5d3e84cd489513f52; https://github.com/gurpnijjer/dream-rehearsal@8f0c2d0973105c7b8d61177859d8793494721d25; https://github.com/icip-cas/DocOps@33e672e00f3c56b4311fb172d007d7dbd48c5418; https://github.com/YichiCS/KV-Cache-Hijack@f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3; https://github.com/flagos-ai/KernelGenBench@c496279164b58b14c8dd754b4f4c1debb7a8b937; https://github.com/Ascend/MindSpeed-LLM@0a0f8cd8c6fc45048928a50f292afd8167e745fa; https://github.com/SLAI-AITP/SLAI-T-Rex@8d6487ebe2d569bbac251f2ab45f2cfd8f726b15; https://github.com/sriprabhar/SHFormer@2a3f3208e68d8a4a5f4f1affc5597e337312a03b; https://github.com/microsoft/evolving-intent@1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8 | checked | 8 | SF-2026-ARXIV-2607-19747; SF-2026-ARXIV-2607-19749; SF-2026-ARXIV-2607-19865; SF-2026-ARXIV-2607-19957; SF-2026-ARXIV-2607-27231; SF-2026-ARXIV-2607-20145; SF-2026-ARXIV-2607-20159; SF-2026-ARXIV-2607-20734 | pages=9; final cursors=d6e502f6ad57e98eb288bbd5d3e84cd489513f52,8f0c2d0973105c7b8d61177859d8793494721d25,33e672e00f3c56b4311fb172d007d7dbd48c5418,f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3,c496279164b58b14c8dd754b4f4c1debb7a8b937,0a0f8cd8c6fc45048928a50f292afd8167e745fa,8d6487ebe2d569bbac251f2ab45f2cfd8f726b15,2a3f3208e68d8a4a5f4f1affc5597e337312a03b,1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8; one bounded commit lookup per family | 2026-07-23T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260723 | — |

<!-- coverage:SRC-ARXIV:20260723:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1063 unique identities in this strict window; 14 routed families.<!-- coverage:SRC-ARXIV:20260723:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260723:start -->repository=https://github.com/Rubric4Setwise/Rubric4Setwise, until=2026-07-23T01:00:00Z, full_sha=d6e502f6ad57e98eb288bbd5d3e84cd489513f52, commit_timestamp=2026-07-22T09:42:56Z, url=https://github.com/Rubric4Setwise/Rubric4Setwise/commit/d6e502f6ad57e98eb288bbd5d3e84cd489513f52; repository=https://github.com/gurpnijjer/dream-rehearsal, until=2026-07-23T01:00:00Z, full_sha=8f0c2d0973105c7b8d61177859d8793494721d25, commit_timestamp=2026-07-23T00:29:15Z, url=https://github.com/gurpnijjer/dream-rehearsal/commit/8f0c2d0973105c7b8d61177859d8793494721d25; repository=https://github.com/icip-cas/DocOps, until=2026-07-23T01:00:00Z, full_sha=33e672e00f3c56b4311fb172d007d7dbd48c5418, commit_timestamp=2026-07-22T06:28:34Z, url=https://github.com/icip-cas/DocOps/commit/33e672e00f3c56b4311fb172d007d7dbd48c5418; repository=https://github.com/YichiCS/KV-Cache-Hijack, until=2026-07-23T01:00:00Z, full_sha=f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3, commit_timestamp=2026-05-23T00:20:43Z, url=https://github.com/YichiCS/KV-Cache-Hijack/commit/f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3; repository=https://github.com/flagos-ai/KernelGenBench, until=2026-07-23T01:00:00Z, full_sha=c496279164b58b14c8dd754b4f4c1debb7a8b937, commit_timestamp=2026-07-22T13:17:09Z, url=https://github.com/flagos-ai/KernelGenBench/commit/c496279164b58b14c8dd754b4f4c1debb7a8b937; repository=https://github.com/Ascend/MindSpeed-LLM, until=2026-07-23T01:00:00Z, full_sha=0a0f8cd8c6fc45048928a50f292afd8167e745fa, commit_timestamp=2026-07-22T08:38:42Z, url=https://github.com/Ascend/MindSpeed-LLM/commit/0a0f8cd8c6fc45048928a50f292afd8167e745fa; repository=https://github.com/SLAI-AITP/SLAI-T-Rex, until=2026-07-23T01:00:00Z, full_sha=8d6487ebe2d569bbac251f2ab45f2cfd8f726b15, commit_timestamp=2026-07-17T05:52:42Z, url=https://github.com/SLAI-AITP/SLAI-T-Rex/commit/8d6487ebe2d569bbac251f2ab45f2cfd8f726b15; repository=https://github.com/sriprabhar/SHFormer, until=2026-07-23T01:00:00Z, full_sha=2a3f3208e68d8a4a5f4f1affc5597e337312a03b, commit_timestamp=2024-10-08T10:43:45Z, url=https://github.com/sriprabhar/SHFormer/commit/2a3f3208e68d8a4a5f4f1affc5597e337312a03b; repository=https://github.com/microsoft/evolving-intent, until=2026-07-23T01:00:00Z, full_sha=1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8, commit_timestamp=2026-06-10T20:00:07Z, url=https://github.com/microsoft/evolving-intent/commit/1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260723:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 14 个 family：exact v1 为 9 个 family 披露 artifact/evidence locator，其中 9 个提供外部 repository/project/demo locator，另有 5 个未披露；本日确认 8 个 family、9 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19704 | arXiv:2607.19704v1 | paper-v1:2607.19704 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19704 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-19704 | yes |
| SF-2026-ARXIV-2607-19747 | arXiv:2607.19747v1 | paper-v1:2607.19747 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19747 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19747 | yes |
| SF-2026-ARXIV-2607-19749 | arXiv:2607.19749v1 | paper-v1:2607.19749 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19749 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-19749 | yes |
| SF-2026-ARXIV-2607-19865 | arXiv:2607.19865v1 | paper-v1:2607.19865 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19865 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-19865 | yes |
| SF-2026-ARXIV-2607-19957 | arXiv:2607.19957v1 | paper-v1:2607.19957 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19957 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-19957 | yes |
| SF-2026-ARXIV-2607-27231 | arXiv:2607.27231v1 | paper-v1:2607.27231 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27231 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-27231 | yes |
| SF-2026-ARXIV-2607-20145 | arXiv:2607.20145v1 | paper-v1:2607.20145 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20145 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2607-20145 | yes |
| SF-2026-ARXIV-2607-20159 | arXiv:2607.20159v1 | paper-v1:2607.20159 | 2026-W30 | 2026-07-22 | SRC-ARXIV; SRC-GITHUB-COMMIT | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-20159 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-20220 | arXiv:2607.20220v1 | paper-v1:2607.20220 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20220 | self | — | new_in_window | MODEL-MOE | Integrate | books-review:SF-2026-ARXIV-2607-20220 | yes |
| SF-2026-ARXIV-2607-20345 | arXiv:2607.20345v1 | paper-v1:2607.20345 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-20345 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-20345 | yes |
| SF-2026-ARXIV-2607-20379 | arXiv:2607.20379v1 | paper-v1:2607.20379 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20379 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2607-20379 | yes |
| SF-2026-ARXIV-2607-20694 | arXiv:2607.20694v1 | paper-v1:2607.20694 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 2 | 1 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-20694 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-20734 | arXiv:2607.20734v1 | paper-v1:2607.20734 | 2026-W30 | 2026-07-23 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20734 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-20734 | yes |
| SF-2026-ARXIV-2607-20757 | arXiv:2607.20757v1 | paper-v1:2607.20757 | 2026-W30 | 2026-07-23 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-20757 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2607-20757 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19704 | RP-3b6cdc492de3e531 | deep | arXiv:2607.19704v1 | SRC-ARXIV@arXiv:2607.19704v1 | https://arxiv.org/html/2607.19704v1#S3; https://arxiv.org/html/2607.19704v1#S3.SS1; https://arxiv.org/html/2607.19704v1#S3.SS2; https://arxiv.org/html/2607.19704v1#A4.SS2; https://arxiv.org/html/2607.19704v1#A4.SS3; https://arxiv.org/html/2607.19704v1#A4.SS4; https://arxiv.org/html/2607.19704v1#A4.SS5; https://arxiv.org/html/2607.19704v1#A5 | https://arxiv.org/html/2607.19704v1#S4; https://arxiv.org/html/2607.19704v1#S4.SS1; https://arxiv.org/html/2607.19704v1#S4.SS2; https://arxiv.org/html/2607.19704v1#S4.SS3; https://arxiv.org/html/2607.19704v1#S5; https://arxiv.org/html/2607.19704v1#A6.SS3; https://arxiv.org/html/2607.19704v1#A6.SS4; https://arxiv.org/html/2607.19704v1#A7 | https://arxiv.org/html/2607.19704v1#S4.SS3; https://arxiv.org/html/2607.19704v1#S5; https://arxiv.org/html/2607.19704v1#A5.SS4; https://arxiv.org/html/2607.19704v1#A7 | Not Disclosed — Exact v1 exposes no author implementation repository or immutable artifact. | claim:SF-2026-ARXIV-2607-19704 | complete |
| SF-2026-ARXIV-2607-19747 | RP-f06465d7f83aa3f0 | deep | arXiv:2607.19747v1 | SRC-ARXIV@arXiv:2607.19747v1; SRC-GITHUB-COMMIT@commit:d6e502f6ad57e98eb288bbd5d3e84cd489513f52 | https://arxiv.org/html/2607.19747v1#S3.SS1; https://arxiv.org/html/2607.19747v1#S3.SS2; https://arxiv.org/html/2607.19747v1#S3.SS3 | https://arxiv.org/html/2607.19747v1#S4.SS1; https://arxiv.org/html/2607.19747v1#S4.SS1.SSS0.Px2; https://arxiv.org/html/2607.19747v1#S4.SS2; https://arxiv.org/html/2607.19747v1#S4.SS3; https://arxiv.org/html/2607.19747v1#A1.SS4; https://arxiv.org/html/2607.19747v1#A1.SS5; https://arxiv.org/html/2607.19747v1#A1.SS6; https://arxiv.org/html/2607.19747v1#A2.SS1; https://arxiv.org/html/2607.19747v1#A2.SS3 | https://arxiv.org/html/2607.19747v1#S6 | https://github.com/Rubric4Setwise/Rubric4Setwise/commit/d6e502f6ad57e98eb288bbd5d3e84cd489513f52 — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; Commit is after the v1 submission but before the Daily cutoff; it supports artifact availability by the report cutoff, not availability at the paper-submission instant. | claim:SF-2026-ARXIV-2607-19747 | complete |
| SF-2026-ARXIV-2607-19749 | RP-5e19f38a5cddbbf3 | deep | arXiv:2607.19749v1 | SRC-ARXIV@arXiv:2607.19749v1; SRC-GITHUB-COMMIT@commit:8f0c2d0973105c7b8d61177859d8793494721d25 | https://arxiv.org/html/2607.19749v1#S3; https://arxiv.org/html/2607.19749v1#S4.SS2; https://arxiv.org/html/2607.19749v1#S4.SS3; https://arxiv.org/html/2607.19749v1#S5; https://arxiv.org/html/2607.19749v1#S6; https://arxiv.org/html/2607.19749v1#S7 | https://arxiv.org/html/2607.19749v1#S4.SS1; https://arxiv.org/html/2607.19749v1#S4.SS3; https://arxiv.org/html/2607.19749v1#S4.SS4; https://arxiv.org/html/2607.19749v1#S5; https://arxiv.org/html/2607.19749v1#S6.SS1; https://arxiv.org/html/2607.19749v1#S6.SS2; https://arxiv.org/html/2607.19749v1#S7; https://arxiv.org/html/2607.19749v1#S8; https://arxiv.org/html/2607.19749v1#A2 | https://arxiv.org/html/2607.19749v1#S9; https://arxiv.org/html/2607.19749v1#A3 | https://github.com/gurpnijjer/dream-rehearsal/commit/8f0c2d0973105c7b8d61177859d8793494721d25 — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; Commit is after the v1 submission but before the Daily cutoff; no claim is made that it was public at the submission instant. | claim:SF-2026-ARXIV-2607-19749 | complete |
| SF-2026-ARXIV-2607-19865 | RP-9522f12fbf0c6b1c | deep | arXiv:2607.19865v1 | SRC-ARXIV@arXiv:2607.19865v1; SRC-GITHUB-COMMIT@commit:33e672e00f3c56b4311fb172d007d7dbd48c5418 | https://arxiv.org/html/2607.19865v1#S3.SS1; https://arxiv.org/html/2607.19865v1#S3.SS2; https://arxiv.org/html/2607.19865v1#S3.SS3 | https://arxiv.org/html/2607.19865v1#S4.SS1.SSS4; https://arxiv.org/html/2607.19865v1#S4.SS1.SSS5; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS1; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS2; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS3; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS4; https://arxiv.org/html/2607.19865v1#A3; https://arxiv.org/html/2607.19865v1#A6; https://arxiv.org/html/2607.19865v1#A8; https://arxiv.org/html/2607.19865v1#A9 | https://arxiv.org/html/2607.19865v1#Sx2 | https://github.com/icip-cas/DocOps/commit/33e672e00f3c56b4311fb172d007d7dbd48c5418 — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; The event-time commit establishes repository provenance; benchmark completeness still follows the exact-v1 manuscript and released artifact contract. | claim:SF-2026-ARXIV-2607-19865 | complete |
| SF-2026-ARXIV-2607-19957 | RP-4322a9526bf2167b | deep | arXiv:2607.19957v1 | SRC-ARXIV@arXiv:2607.19957v1; SRC-GITHUB-COMMIT@commit:f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3 | https://arxiv.org/html/2607.19957v1#S4.SS1; https://arxiv.org/html/2607.19957v1#S4.SS2; https://arxiv.org/html/2607.19957v1#S5 | https://arxiv.org/html/2607.19957v1#S6; https://arxiv.org/html/2607.19957v1#S7.SS1; https://arxiv.org/html/2607.19957v1#S7.SS2; https://arxiv.org/html/2607.19957v1#S7.SS3; https://arxiv.org/html/2607.19957v1#S7.SS4; https://arxiv.org/html/2607.19957v1#S7.SS5; https://arxiv.org/html/2607.19957v1#S7.SS6 | https://arxiv.org/html/2607.19957v1#S8; https://arxiv.org/html/2607.19957v1#Ax1.SS0.SSS0.Px2; https://arxiv.org/html/2607.19957v1#Ax2 | https://github.com/YichiCS/KV-Cache-Hijack/commit/f9a5c07bddeae9ef4e04582f4ab114f26c9cbec3; https://zenodo.org/records/20403786 (10.5281/zenodo.20403786, md5:7691c6ebaf4a43f18037af8f0adaf93a) — both pre-cutoff; Repository and Zenodo archive predate the cutoff; this proves artifact provenance, not production incidence or universal exploitability. | claim:SF-2026-ARXIV-2607-19957 | complete |
| SF-2026-ARXIV-2607-27231 | RP-6f9b1bf1b614e176 | deep | arXiv:2607.27231v1 | SRC-ARXIV@arXiv:2607.27231v1; SRC-GITHUB-COMMIT@commit:c496279164b58b14c8dd754b4f4c1debb7a8b937 | https://arxiv.org/html/2607.27231v1#S3.SS1; https://arxiv.org/html/2607.27231v1#S3.SS2; https://arxiv.org/html/2607.27231v1#S3.SS3 | https://arxiv.org/html/2607.27231v1#S4.SS1; https://arxiv.org/html/2607.27231v1#S4.SS2; https://arxiv.org/html/2607.27231v1#S4.SS3; https://arxiv.org/html/2607.27231v1#S4.SS4; https://arxiv.org/html/2607.27231v1#S4.SS5; https://arxiv.org/html/2607.27231v1#S4.SS6; https://arxiv.org/html/2607.27231v1#S4.SS7; https://arxiv.org/html/2607.27231v1#A4; https://arxiv.org/html/2607.27231v1#A5; https://arxiv.org/html/2607.27231v1#A6; https://arxiv.org/html/2607.27231v1#A7; https://arxiv.org/html/2607.27231v1#A9; https://arxiv.org/html/2607.27231v1#A11 | https://arxiv.org/html/2607.27231v1#S2.SS2; https://arxiv.org/html/2607.27231v1#S5; https://arxiv.org/html/2607.27231v1#A3; https://arxiv.org/html/2607.27231v1#A4 | https://github.com/flagos-ai/KernelGenBench/commit/c496279164b58b14c8dd754b4f4c1debb7a8b937 — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; Commit is after v1 submission but before the Daily cutoff; cross-platform claims remain limited by unequal anti-hack/profiler coverage. | claim:SF-2026-ARXIV-2607-27231 | complete |
| SF-2026-ARXIV-2607-20145 | RP-ce7667a9fd26ff38 | deep | arXiv:2607.20145v1 | SRC-ARXIV@arXiv:2607.20145v1; SRC-GITHUB-COMMIT@commit:0a0f8cd8c6fc45048928a50f292afd8167e745fa; SRC-GITHUB-COMMIT@commit:8d6487ebe2d569bbac251f2ab45f2cfd8f726b15 | https://arxiv.org/html/2607.20145v1#S2.SS1; https://arxiv.org/html/2607.20145v1#S2.SS2; https://arxiv.org/html/2607.20145v1#S2.SS3.SSS2; https://arxiv.org/html/2607.20145v1#S2.SS3.SSS3; https://arxiv.org/html/2607.20145v1#S3.SS1; https://arxiv.org/html/2607.20145v1#S3.SS2; https://arxiv.org/html/2607.20145v1#S3.SS3; https://arxiv.org/html/2607.20145v1#S3.SS4; https://arxiv.org/html/2607.20145v1#A2; https://arxiv.org/html/2607.20145v1#A4; https://arxiv.org/html/2607.20145v1#A5 | https://arxiv.org/html/2607.20145v1#S4.SS1; https://arxiv.org/html/2607.20145v1#S4.SS2; https://arxiv.org/html/2607.20145v1#S4.SS3; https://arxiv.org/html/2607.20145v1#S4.SS4; https://arxiv.org/html/2607.20145v1#S4.SS5; https://arxiv.org/html/2607.20145v1#S4.SS6 | https://arxiv.org/html/2607.20145v1#S5 | https://github.com/Ascend/MindSpeed-LLM/commit/0a0f8cd8c6fc45048928a50f292afd8167e745fa; https://github.com/SLAI-AITP/SLAI-T-Rex/commit/8d6487ebe2d569bbac251f2ab45f2cfd8f726b15; https://www.modelscope.cn/models/SLAIAITP/DeepSeek-V4-Flash-OR — Exact v1 links the historical Deepseek-OR URL, which now redirects to SLAI-T-Rex. GitHub commits are frozen before cutoff; the ModelScope model revision was not independently frozen and is not used for mechanism claims. | claim:SF-2026-ARXIV-2607-20145 | complete |
| SF-2026-ARXIV-2607-20159 | RP-449f37e43165dee3 | closure | arXiv:2607.20159v1 | SRC-ARXIV@arXiv:2607.20159v1; SRC-GITHUB-COMMIT@commit:2a3f3208e68d8a4a5f4f1affc5597e337312a03b | https://arxiv.org/html/2607.20159v1#S3.SS1; https://arxiv.org/html/2607.20159v1#S3.SS2; https://arxiv.org/html/2607.20159v1#S3.SS2.SSS1; https://arxiv.org/html/2607.20159v1#S3.SS2.SSS2 | https://arxiv.org/html/2607.20159v1#S4.SS1; https://arxiv.org/html/2607.20159v1#S4.SS2; https://arxiv.org/html/2607.20159v1#S4.SS3; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS4; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS5; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS6; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS7 | https://arxiv.org/html/2607.20159v1#S4; https://arxiv.org/html/2607.20159v1#S5 | https://github.com/sriprabhar/SHFormer/commit/2a3f3208e68d8a4a5f4f1affc5597e337312a03b — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; Artifact predates the cutoff, but the candidate remains a domain-specific architecture closure rather than a Books mechanism. | claim:SF-2026-ARXIV-2607-20159 | complete |
| SF-2026-ARXIV-2607-20220 | RP-1b3f6c6a8eb0acc4 | deep | arXiv:2607.20220v1 | SRC-ARXIV@arXiv:2607.20220v1 | https://arxiv.org/html/2607.20220v1#S2; https://arxiv.org/html/2607.20220v1#S2.SS1; https://arxiv.org/html/2607.20220v1#S2.SS2; https://arxiv.org/html/2607.20220v1#S2.SS3; https://arxiv.org/html/2607.20220v1#S2.SS4; https://arxiv.org/html/2607.20220v1#S2.SS5 | https://arxiv.org/html/2607.20220v1#S3; https://arxiv.org/html/2607.20220v1#S3.SS1; https://arxiv.org/html/2607.20220v1#S3.SS2; https://arxiv.org/html/2607.20220v1#S3.SS3; https://arxiv.org/html/2607.20220v1#S3.SS4 | https://arxiv.org/html/2607.20220v1#S4; https://arxiv.org/html/2607.20220v1#S4.SS0.SSS0.Px1; https://arxiv.org/html/2607.20220v1#S4.SS0.SSS0.Px2 | Not Disclosed — Exact v1 discusses implementation practicality but exposes no public implementation artifact. | claim:SF-2026-ARXIV-2607-20220 | complete |
| SF-2026-ARXIV-2607-20345 | RP-67ae2ccc45ed7ea2 | standard | arXiv:2607.20345v1 | SRC-ARXIV@arXiv:2607.20345v1 | https://arxiv.org/html/2607.20345v1#S2.SS1; https://arxiv.org/html/2607.20345v1#S2.SS2; https://arxiv.org/html/2607.20345v1#S2.SS3 | https://arxiv.org/html/2607.20345v1#S3.SS1; https://arxiv.org/html/2607.20345v1#S3.SS2; https://arxiv.org/html/2607.20345v1#S3.SS3 | https://arxiv.org/html/2607.20345v1#S3.SS3; https://arxiv.org/html/2607.20345v1#S4 | Not Disclosed — Exact v1 exposes no immutable public code, dataset, or model artifact. | claim:SF-2026-ARXIV-2607-20345 | complete |
| SF-2026-ARXIV-2607-20379 | RP-2689c0be73b348dc | deep | arXiv:2607.20379v1 | SRC-ARXIV@arXiv:2607.20379v1 | https://arxiv.org/html/2607.20379v1#S2.SS1; https://arxiv.org/html/2607.20379v1#S3.SS1; https://arxiv.org/html/2607.20379v1#S3.SS2; https://arxiv.org/html/2607.20379v1#S4; https://arxiv.org/html/2607.20379v1#S5.SS1 | https://arxiv.org/html/2607.20379v1#S5.SS2; https://arxiv.org/html/2607.20379v1#S5.SS3; https://arxiv.org/html/2607.20379v1#S5.SS4; https://arxiv.org/html/2607.20379v1#S6; https://arxiv.org/html/2607.20379v1#A2; https://arxiv.org/html/2607.20379v1#A3; https://arxiv.org/html/2607.20379v1#A5; https://arxiv.org/html/2607.20379v1#A6; https://arxiv.org/html/2607.20379v1#A7; https://arxiv.org/html/2607.20379v1#A8; https://arxiv.org/html/2607.20379v1#A10; https://arxiv.org/html/2607.20379v1#A11 | https://arxiv.org/html/2607.20379v1#S8 | Not Disclosed — Exact v1 provides reproducibility appendices but no public code or model repository. | claim:SF-2026-ARXIV-2607-20379 | complete |
| SF-2026-ARXIV-2607-20694 | RP-defc94343f636eb3 | closure | arXiv:2607.20694v1 | SRC-ARXIV@arXiv:2607.20694v1 | https://arxiv.org/html/2607.20694v1#S3.SS1; https://arxiv.org/html/2607.20694v1#S3.SS2; https://arxiv.org/html/2607.20694v1#S3.SS3; https://arxiv.org/html/2607.20694v1#S4.SS1; https://arxiv.org/html/2607.20694v1#S4.SS2; https://arxiv.org/html/2607.20694v1#S4.SS3; https://arxiv.org/html/2607.20694v1#S5.SS1; https://arxiv.org/html/2607.20694v1#S5.SS2 | https://arxiv.org/html/2607.20694v1#S6.SS1; https://arxiv.org/html/2607.20694v1#S6.SS2; https://arxiv.org/html/2607.20694v1#S6.SS3; https://arxiv.org/html/2607.20694v1#S6.SS8 | https://arxiv.org/html/2607.20694v1#S7.SS1; https://arxiv.org/html/2607.20694v1#S7.SS3 | Not Disclosed — Exact v1 exposes no public implementation or dataset artifact. | claim:SF-2026-ARXIV-2607-20694 | complete |
| SF-2026-ARXIV-2607-20734 | RP-8ba70420363029e0 | deep | arXiv:2607.20734v1 | SRC-ARXIV@arXiv:2607.20734v1; SRC-GITHUB-COMMIT@commit:1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8 | https://arxiv.org/html/2607.20734v1#S3; https://arxiv.org/html/2607.20734v1#S3.SS0.SSS0.Px1; https://arxiv.org/html/2607.20734v1#S3.SS0.SSS0.Px2; https://arxiv.org/html/2607.20734v1#S4.SS1; https://arxiv.org/html/2607.20734v1#S4.SS2; https://arxiv.org/html/2607.20734v1#S4.SS3 | https://arxiv.org/html/2607.20734v1#S5; https://arxiv.org/html/2607.20734v1#S5.SS1; https://arxiv.org/html/2607.20734v1#S5.SS2; https://arxiv.org/html/2607.20734v1#S5.SS3; https://arxiv.org/html/2607.20734v1#A2; https://arxiv.org/html/2607.20734v1#A4; https://arxiv.org/html/2607.20734v1#A6 | https://arxiv.org/html/2607.20734v1#Sx1 | https://github.com/microsoft/evolving-intent/commit/1e4f10a9db9cbe34e91efd7d180ad2b13dc913d8 — latest GitHub commit returned at or before 2026-07-23T01:00:00Z; The repository predates the cutoff; final-turn verifier coverage and synthetic-user limitations remain manuscript-bounded. | claim:SF-2026-ARXIV-2607-20734 | complete |
| SF-2026-ARXIV-2607-20757 | RP-d7883214eb706fb2 | deep | arXiv:2607.20757v1 | SRC-ARXIV@arXiv:2607.20757v1 | https://arxiv.org/html/2607.20757v1#S3; https://arxiv.org/html/2607.20757v1#S3.SS1; https://arxiv.org/html/2607.20757v1#S3.SS2; https://arxiv.org/html/2607.20757v1#S4; https://arxiv.org/html/2607.20757v1#S4.SSx1; https://arxiv.org/html/2607.20757v1#S4.SSx2 | https://arxiv.org/html/2607.20757v1#S5; https://arxiv.org/html/2607.20757v1#S5.SS0.SSS0.Px1; https://arxiv.org/html/2607.20757v1#S5.SS0.SSS0.Px2; https://arxiv.org/html/2607.20757v1#S5.SS1 | https://arxiv.org/html/2607.20757v1#S7; https://arxiv.org/html/2607.20757v1#A1; https://arxiv.org/html/2607.20757v1#A2 | https://github.com/MPedraBento/gauge-quant — disclosed in exact v1, but cutoff query returned no commit; later commit 103bb4a0bc3e1b06c689098509121d868f444f19 at 2026-07-23T15:15:38Z is excluded. | claim:SF-2026-ARXIV-2607-20757 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-19704:start -->
#### Efficient Clustering with Provable Guardrails for LLM Inference at Scale

<!-- claim:SF-2026-ARXIV-2607-19704:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports the algorithm, set-cover guardrail and disclosed workload results. It does not prove semantic/output equivalence, safety preservation, universal alpha, or linear complexity unless the partition count scales with n as analyzed. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19704:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: request-level semantic coalescing -> representative inference -> member-level reuse under explicit guardrails 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19704v1#S3; https://arxiv.org/html/2607.19704v1#S3.SS1; https://arxiv.org/html/2607.19704v1#S3.SS2; https://arxiv.org/html/2607.19704v1#A4.SS2; https://arxiv.org/html/2607.19704v1#A4.SS3; https://arxiv.org/html/2607.19704v1#A4.SS4; https://arxiv.org/html/2607.19704v1#A4.SS5; https://arxiv.org/html/2607.19704v1#A5`；Evaluation：`https://arxiv.org/html/2607.19704v1#S4; https://arxiv.org/html/2607.19704v1#S4.SS1; https://arxiv.org/html/2607.19704v1#S4.SS2; https://arxiv.org/html/2607.19704v1#S4.SS3; https://arxiv.org/html/2607.19704v1#S5; https://arxiv.org/html/2607.19704v1#A6.SS3; https://arxiv.org/html/2607.19704v1#A6.SS4; https://arxiv.org/html/2607.19704v1#A7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19704v1#S4.SS3; https://arxiv.org/html/2607.19704v1#S5; https://arxiv.org/html/2607.19704v1#A5.SS4; https://arxiv.org/html/2607.19704v1#A7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency: request-level semantic coalescing -> representative inference -> member-level reuse under explicit guardrails`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19704:end -->

<!-- review:SF-2026-ARXIV-2607-19747:start -->
#### Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking

<!-- claim:SF-2026-ARXIV-2607-19747:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports set-level evaluation/selection under the disclosed generated rubrics and judge. It does not establish the rubric as complete ground truth, independence between selector and generator, or cross-domain transfer of its nine dimensions. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19747:end -->

**旧方案与约束变化。** `本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**`（`books/part-07-agent/76-rag.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: pointwise relevance ranking -> set-level coverage, redundancy, conflict and complementarity under a bounded context budget 它改变 `AGENT-RAG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19747v1#S3.SS1; https://arxiv.org/html/2607.19747v1#S3.SS2; https://arxiv.org/html/2607.19747v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.19747v1#S4.SS1; https://arxiv.org/html/2607.19747v1#S4.SS1.SSS0.Px2; https://arxiv.org/html/2607.19747v1#S4.SS2; https://arxiv.org/html/2607.19747v1#S4.SS3; https://arxiv.org/html/2607.19747v1#A1.SS4; https://arxiv.org/html/2607.19747v1#A1.SS5; https://arxiv.org/html/2607.19747v1#A1.SS6; https://arxiv.org/html/2607.19747v1#A2.SS1; https://arxiv.org/html/2607.19747v1#A2.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19747v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L616-L623`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: pointwise relevance ranking -> set-level coverage, redundancy, conflict and complementarity under a bounded context budget`。
- Stable owner：`AGENT-RAG`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-19747:end -->

<!-- review:SF-2026-ARXIV-2607-19749:start -->
#### The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL

<!-- claim:SF-2026-ARXIV-2607-19749:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports component-level forgetting and recovery in this Dreamer/MiniGrid contract. It does not prove world models generally remember, that imagined RL succeeds (it failed 0/3 here), or that dream rehearsal beats retained real episodes when those remain available. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19749:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: replay that preserves predictive state -> component-level forgetting diagnosis -> actor rehearsal from graded imagined trajectories 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19749v1#S3; https://arxiv.org/html/2607.19749v1#S4.SS2; https://arxiv.org/html/2607.19749v1#S4.SS3; https://arxiv.org/html/2607.19749v1#S5; https://arxiv.org/html/2607.19749v1#S6; https://arxiv.org/html/2607.19749v1#S7`；Evaluation：`https://arxiv.org/html/2607.19749v1#S4.SS1; https://arxiv.org/html/2607.19749v1#S4.SS3; https://arxiv.org/html/2607.19749v1#S4.SS4; https://arxiv.org/html/2607.19749v1#S5; https://arxiv.org/html/2607.19749v1#S6.SS1; https://arxiv.org/html/2607.19749v1#S6.SS2; https://arxiv.org/html/2607.19749v1#S7; https://arxiv.org/html/2607.19749v1#S8; https://arxiv.org/html/2607.19749v1#A2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19749v1#S9; https://arxiv.org/html/2607.19749v1#A3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution: replay that preserves predictive state -> component-level forgetting diagnosis -> actor rehearsal from graded imagined trajectories`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19749:end -->

<!-- review:SF-2026-ARXIV-2607-19865:start -->
#### DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations

<!-- claim:SF-2026-ARXIV-2607-19865:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports artifact-state evaluation and the measured verifier fidelity on released tasks/mutations. It does not prove predicate completeness, semantic equivalence to expert review, or that a higher pass rate transfers across harnesses. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19865:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: final-answer judge -> executable artifact-state predicates plus preservation invariants and verifier-fidelity audit 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19865v1#S3.SS1; https://arxiv.org/html/2607.19865v1#S3.SS2; https://arxiv.org/html/2607.19865v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.19865v1#S4.SS1.SSS4; https://arxiv.org/html/2607.19865v1#S4.SS1.SSS5; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS1; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS2; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS3; https://arxiv.org/html/2607.19865v1#S4.SS2.SSS4; https://arxiv.org/html/2607.19865v1#A3; https://arxiv.org/html/2607.19865v1#A6; https://arxiv.org/html/2607.19865v1#A8; https://arxiv.org/html/2607.19865v1#A9`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19865v1#Sx2`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L624-L631`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: final-answer judge -> executable artifact-state predicates plus preservation invariants and verifier-fidelity audit`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19865:end -->

<!-- review:SF-2026-ARXIV-2607-19957:start -->
#### HijackKV: New Threat in Position-Independent KV Cache Reuse

<!-- claim:SF-2026-ARXIV-2607-19957:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports a vulnerability in the authors’ position-independent multi-tenant reuse model and disclosed implementations. It does not prove ordinary exact-prefix cache reuse is vulnerable in the same way, deployed incidence, cache availability/probing in every platform, or that reported ASR generalizes beyond tested models/data. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19957:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19957v1#S4.SS1; https://arxiv.org/html/2607.19957v1#S4.SS2; https://arxiv.org/html/2607.19957v1#S5`；Evaluation：`https://arxiv.org/html/2607.19957v1#S6; https://arxiv.org/html/2607.19957v1#S7.SS1; https://arxiv.org/html/2607.19957v1#S7.SS2; https://arxiv.org/html/2607.19957v1#S7.SS3; https://arxiv.org/html/2607.19957v1#S7.SS4; https://arxiv.org/html/2607.19957v1#S7.SS5; https://arxiv.org/html/2607.19957v1#S7.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19957v1#S8; https://arxiv.org/html/2607.19957v1#Ax1.SS0.SSS0.Px2; https://arxiv.org/html/2607.19957v1#Ax2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19957:end -->

<!-- review:SF-2026-ARXIV-2607-27231:start -->
#### KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-27231:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports the released benchmark contract and its disclosed model/hardware runs. It does not establish production kernel correctness, universal tolerance, fair comparison where anti-hack coverage differs, or that a model ranking transfers across operators/chips/harnesses. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27231:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: single-source/single-GPU pass rate -> multi-source operator contract -> cross-chip correctness, speed and cost frontier 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27231v1#S3.SS1; https://arxiv.org/html/2607.27231v1#S3.SS2; https://arxiv.org/html/2607.27231v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.27231v1#S4.SS1; https://arxiv.org/html/2607.27231v1#S4.SS2; https://arxiv.org/html/2607.27231v1#S4.SS3; https://arxiv.org/html/2607.27231v1#S4.SS4; https://arxiv.org/html/2607.27231v1#S4.SS5; https://arxiv.org/html/2607.27231v1#S4.SS6; https://arxiv.org/html/2607.27231v1#S4.SS7; https://arxiv.org/html/2607.27231v1#A4; https://arxiv.org/html/2607.27231v1#A5; https://arxiv.org/html/2607.27231v1#A6; https://arxiv.org/html/2607.27231v1#A7; https://arxiv.org/html/2607.27231v1#A9; https://arxiv.org/html/2607.27231v1#A11`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27231v1#S2.SS2; https://arxiv.org/html/2607.27231v1#S5; https://arxiv.org/html/2607.27231v1#A3; https://arxiv.org/html/2607.27231v1#A4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: single-source/single-GPU pass rate -> multi-source operator contract -> cross-chip correctness, speed and cost frontier`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27231:end -->

<!-- review:SF-2026-ARXIV-2607-20145:start -->
#### SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD

<!-- claim:SF-2026-ARXIV-2607-20145:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports the disclosed Ascend post-training pipeline and author experiments. It does not prove the recipe is optimal on other models/hardware/domains, that MFU gains arise from one optimization, or that more SFT data monotonically helps. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20145:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: domain CPT and verified SFT recipe -> phase-aligned distributed runtime -> provenance-linked deployable artifact 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20145v1#S2.SS1; https://arxiv.org/html/2607.20145v1#S2.SS2; https://arxiv.org/html/2607.20145v1#S2.SS3.SSS2; https://arxiv.org/html/2607.20145v1#S2.SS3.SSS3; https://arxiv.org/html/2607.20145v1#S3.SS1; https://arxiv.org/html/2607.20145v1#S3.SS2; https://arxiv.org/html/2607.20145v1#S3.SS3; https://arxiv.org/html/2607.20145v1#S3.SS4; https://arxiv.org/html/2607.20145v1#A2; https://arxiv.org/html/2607.20145v1#A4; https://arxiv.org/html/2607.20145v1#A5`；Evaluation：`https://arxiv.org/html/2607.20145v1#S4.SS1; https://arxiv.org/html/2607.20145v1#S4.SS2; https://arxiv.org/html/2607.20145v1#S4.SS3; https://arxiv.org/html/2607.20145v1#S4.SS4; https://arxiv.org/html/2607.20145v1#S4.SS5; https://arxiv.org/html/2607.20145v1#S4.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20145v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L606-L615`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency: domain CPT and verified SFT recipe -> phase-aligned distributed runtime -> provenance-linked deployable artifact`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-20145:end -->

<!-- review:SF-2026-ARXIV-2607-20159:start -->
#### SHFormer: Dynamic Spectral Filtering Convolutional Neural Network and High-pass Kernel Generation Transformer for Adaptive MRI Reconstruction

<!-- claim:SF-2026-ARXIV-2607-20159:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports an MRI reconstruction architecture under the released experiments, not a general multimodal-token, serving, training-platform or medical-deployment conclusion. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20159:end -->

**旧方案与约束变化。** `本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。`（`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Alternative Branch: fixed reconstruction filters -> instance-conditioned spectral and high-pass kernels for MRI 它改变 `MULTIMODAL-REPRESENTATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20159v1#S3.SS1; https://arxiv.org/html/2607.20159v1#S3.SS2; https://arxiv.org/html/2607.20159v1#S3.SS2.SSS1; https://arxiv.org/html/2607.20159v1#S3.SS2.SSS2`；Evaluation：`https://arxiv.org/html/2607.20159v1#S4.SS1; https://arxiv.org/html/2607.20159v1#S4.SS2; https://arxiv.org/html/2607.20159v1#S4.SS3; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS4; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS5; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS6; https://arxiv.org/html/2607.20159v1#S4.SS3.SSS7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20159v1#S4; https://arxiv.org/html/2607.20159v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 1 / Durability 1 = **3/9**。
- Evolution relation：`Alternative Branch: fixed reconstruction filters -> instance-conditioned spectral and high-pass kernels for MRI`。
- Stable owner：`MULTIMODAL-REPRESENTATION`。
- Books disposition：`Rejected — Low Durability / Out of Scope`。
<!-- review:SF-2026-ARXIV-2607-20159:end -->

<!-- review:SF-2026-ARXIV-2607-20220:start -->
#### MoX: Efficient MoE Routing on Direct-Connect Topologies

<!-- claim:SF-2026-ARXIV-2607-20220:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports the routing/tree algorithm and simulated/proxy improvements under disclosed topology and workload assumptions. It does not prove deadlock-free implementation, fault behavior, exact hardware timing, or universal gains over switch fabrics. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20220:end -->

**旧方案与约束变化。** `本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。`（`books/part-02-model/21-moe.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion 它改变 `MODEL-MOE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20220v1#S2; https://arxiv.org/html/2607.20220v1#S2.SS1; https://arxiv.org/html/2607.20220v1#S2.SS2; https://arxiv.org/html/2607.20220v1#S2.SS3; https://arxiv.org/html/2607.20220v1#S2.SS4; https://arxiv.org/html/2607.20220v1#S2.SS5`；Evaluation：`https://arxiv.org/html/2607.20220v1#S3; https://arxiv.org/html/2607.20220v1#S3.SS1; https://arxiv.org/html/2607.20220v1#S3.SS2; https://arxiv.org/html/2607.20220v1#S3.SS3; https://arxiv.org/html/2607.20220v1#S3.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20220v1#S4; https://arxiv.org/html/2607.20220v1#S4.SS0.SSS0.Px1; https://arxiv.org/html/2607.20220v1#S4.SS0.SSS0.Px2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion`。
- Stable owner：`MODEL-MOE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-20220:end -->

<!-- review:SF-2026-ARXIV-2607-20345:start -->
#### Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids

<!-- claim:SF-2026-ARXIV-2607-20345:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports feasibility and author results for this embodiment/task. It does not prove general retail autonomy, detector calibration across environments, causal value estimates, sim-to-real transfer or physical safety. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20345:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: curated VLA SFT -> advantage-conditioned experience refinement -> OOD-triggered fallback in a physical loop 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20345v1#S2.SS1; https://arxiv.org/html/2607.20345v1#S2.SS2; https://arxiv.org/html/2607.20345v1#S2.SS3`；Evaluation：`https://arxiv.org/html/2607.20345v1#S3.SS1; https://arxiv.org/html/2607.20345v1#S3.SS2; https://arxiv.org/html/2607.20345v1#S3.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20345v1#S3.SS3; https://arxiv.org/html/2607.20345v1#S4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency: curated VLA SFT -> advantage-conditioned experience refinement -> OOD-triggered fallback in a physical loop`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-20345:end -->

<!-- review:SF-2026-ARXIV-2607-20379:start -->
#### Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

<!-- claim:SF-2026-ARXIV-2607-20379:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports failures of reconstruction-only scoring and the RECAP/probe results in disclosed settings. It does not establish neuron-level causal use, complete semantic legibility, safety under adaptive training, or that a high-AUC probe yields faithful language explanations. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20379:end -->

**旧方案与约束变化。** `训练把大量数值参数更新到了某个低损失区域。那些参数里究竟有什么？模型是在存储样本、提取规则、建立世界模型，还是以另一种方式组织经验？`（`books/part-01-worldview/05-what-neural-networks-learn.md#L12-L12`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring 它改变 `WORLDVIEW-REPRESENTATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20379v1#S2.SS1; https://arxiv.org/html/2607.20379v1#S3.SS1; https://arxiv.org/html/2607.20379v1#S3.SS2; https://arxiv.org/html/2607.20379v1#S4; https://arxiv.org/html/2607.20379v1#S5.SS1`；Evaluation：`https://arxiv.org/html/2607.20379v1#S5.SS2; https://arxiv.org/html/2607.20379v1#S5.SS3; https://arxiv.org/html/2607.20379v1#S5.SS4; https://arxiv.org/html/2607.20379v1#S6; https://arxiv.org/html/2607.20379v1#A2; https://arxiv.org/html/2607.20379v1#A3; https://arxiv.org/html/2607.20379v1#A5; https://arxiv.org/html/2607.20379v1#A6; https://arxiv.org/html/2607.20379v1#A7; https://arxiv.org/html/2607.20379v1#A8; https://arxiv.org/html/2607.20379v1#A10; https://arxiv.org/html/2607.20379v1#A11`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20379v1#S8`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L632-L641`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring`。
- Stable owner：`WORLDVIEW-REPRESENTATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-20379:end -->

<!-- review:SF-2026-ARXIV-2607-20694:start -->
#### Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions

<!-- claim:SF-2026-ARXIV-2607-20694:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports mathematical properties and synthetic allocation behavior; it does not validate real-user labels, causal credit, workflow authorization or large-scale convergence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20694:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Alternative Branch: nearest-task/soft assignment -> budget-capped fractional market allocation 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20694v1#S3.SS1; https://arxiv.org/html/2607.20694v1#S3.SS2; https://arxiv.org/html/2607.20694v1#S3.SS3; https://arxiv.org/html/2607.20694v1#S4.SS1; https://arxiv.org/html/2607.20694v1#S4.SS2; https://arxiv.org/html/2607.20694v1#S4.SS3; https://arxiv.org/html/2607.20694v1#S5.SS1; https://arxiv.org/html/2607.20694v1#S5.SS2`；Evaluation：`https://arxiv.org/html/2607.20694v1#S6.SS1; https://arxiv.org/html/2607.20694v1#S6.SS2; https://arxiv.org/html/2607.20694v1#S6.SS3; https://arxiv.org/html/2607.20694v1#S6.SS8`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20694v1#S7.SS1; https://arxiv.org/html/2607.20694v1#S7.SS3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 1 / Durability 1 = **4/9**。
- Evolution relation：`Alternative Branch: nearest-task/soft assignment -> budget-capped fractional market allocation`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-20694:end -->

<!-- review:SF-2026-ARXIV-2607-20734:start -->
#### LLMs Get Lost in Evolving User Intent

<!-- claim:SF-2026-ARXIV-2607-20734:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports performance degradation and transition diagnostics in the synthetic, final-anchor contract. It does not prove natural-user prevalence, that memory alone fixes intent tracking, or that the preliminary RL result generalizes. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20734:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: static single-turn task -> versioned intent-state transitions -> final anchored verifier plus transition-specific diagnostics 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20734v1#S3; https://arxiv.org/html/2607.20734v1#S3.SS0.SSS0.Px1; https://arxiv.org/html/2607.20734v1#S3.SS0.SSS0.Px2; https://arxiv.org/html/2607.20734v1#S4.SS1; https://arxiv.org/html/2607.20734v1#S4.SS2; https://arxiv.org/html/2607.20734v1#S4.SS3`；Evaluation：`https://arxiv.org/html/2607.20734v1#S5; https://arxiv.org/html/2607.20734v1#S5.SS1; https://arxiv.org/html/2607.20734v1#S5.SS2; https://arxiv.org/html/2607.20734v1#S5.SS3; https://arxiv.org/html/2607.20734v1#A2; https://arxiv.org/html/2607.20734v1#A4; https://arxiv.org/html/2607.20734v1#A6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20734v1#Sx1`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L660-L667`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: static single-turn task -> versioned intent-state transitions -> final anchored verifier plus transition-specific diagnostics`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-20734:end -->

<!-- review:SF-2026-ARXIV-2607-20757:start -->
#### GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries

<!-- claim:SF-2026-ARXIV-2607-20757:start -->作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports learned symmetry bases and fake-quantization perplexity in two model/short continued-training settings. It does not prove end-to-end speed, hardware support, full-pretraining stability, general low-bit robustness or that the proxy minimizes actual quantized loss. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-20757:end -->

**旧方案与约束变化。** `本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。`（`books/part-04-training-system/28-pretraining.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: post-training/random rotation -> symmetry-preserving learned basis during training -> quantized artifact with explicit runtime transform cost 它改变 `TRAIN-PRETRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.20757v1#S3; https://arxiv.org/html/2607.20757v1#S3.SS1; https://arxiv.org/html/2607.20757v1#S3.SS2; https://arxiv.org/html/2607.20757v1#S4; https://arxiv.org/html/2607.20757v1#S4.SSx1; https://arxiv.org/html/2607.20757v1#S4.SSx2`；Evaluation：`https://arxiv.org/html/2607.20757v1#S5; https://arxiv.org/html/2607.20757v1#S5.SS0.SSS0.Px1; https://arxiv.org/html/2607.20757v1#S5.SS0.SSS0.Px2; https://arxiv.org/html/2607.20757v1#S5.SS1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.20757v1#S7; https://arxiv.org/html/2607.20757v1#A1; https://arxiv.org/html/2607.20757v1#A2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: post-training/random rotation -> symmetry-preserving learned basis during training -> quantized artifact with explicit runtime transform cost`。
- Stable owner：`TRAIN-PRETRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-20757:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19704 | Internal shopping personas, AG News and Cosmopedia include 100K-scale subsets; production evidence covers 38M users, alpha=0.77 and exact household attributes. Authors report about 50x fewer downstream query/critic calls and a 0.7% relevance gap on 5,000 sampled member-representative pairs. Embedding model, full LLM/hardware/precision/concurrency and general production SLO are Not Disclosed. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-19747 | About 28K generated rubric items span short- and long-form scenarios, 12 rerankers and two independent evaluation passes. DeepSeek-V4 Pro is the main judge, with human validation and disclosed H20 resources; model/precision/batch/concurrency and production SLO are not a serving benchmark. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-19749 | MiniGrid continual learning with DreamerV3: four-task and eight-task sequences, three seeds; dream rehearsal runs every 2,000 environment steps with 50 updates per prior task and top-25% trajectories, about 15% compute at four tasks. Real-episode cloning is a cheaper comparison. No robotics, continuous control, safety SLO or broad model-family evidence. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-19865 | 210 tasks across four document formats and four complexity levels; full model/harness matrix uses final artifacts. Verifier audit reports 122/128 agreement (95.31%) and 174/180 mutation detections (96.67%). Harness configuration and costs are disclosed; results are not prevalence, production reliability or unrestricted desktop-agent evidence. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-19957 | Four QA datasets, 200 samples each; Llama/Qwen/Mistral families from 1B to 70B; CacheBlend, EPIC, random, vanilla/full recomputation; AMD EPYC 9334 and four RTX PRO 6000 Blackwell GPUs. Default cache ratio 0.3, recomputation 0.1, chunk 32; results include white-/black-box transfer, 0.1-0.5 cache/recompute sweeps and 0-2048 filler tokens. Precision, serving concurrency and production SLO are Not Disclosed. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-27231 | 210 operators (110 ATen, 50 vLLM, 50 cuBLAS), six accelerator ecosystems for the 110-ATen cross-platform subset, adaptive dtype/reduction tolerances, 300s correctness and 600s performance timeouts. Tables report pass@1/5, geomean/median/IQM speed, fast_0.8/1.0/1.5 and tokens/time. NVIDIA enables three anti-hack layers; other platforms only two due profiler adaptation. Exact chip commercial names are partly anonymized and production SLO is not claimed. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20145 | DeepSeek-V4-Flash family on Ascend CloudMatrix384 SuperPOD; author reports MFU up to 34.22%, kernel and fusion results, long-run stability, SFT size/cleaning ablations, matched CPT-to-SFT comparisons and OR/general benchmark slices. Full model internals, all kernel artifacts, concurrency and production serving SLO are not disclosed; only this post-training family is evaluated. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20220 | ASTRA-sim2 with token-level Expert Parallel traces; DeepSeek-V3 late-training distributions at 16/32/64 GPUs and 256 experts, Qwen3-225B popularity sensitivity, BF16 width 7168, 5,120 training tokens/GPU and 64-256 inference tokens. Degree-8 expander assumes 800 Gb/s aggregate link split and idealized switch/min-hop baselines; TPUv8i Boardfly uses an analytical proxy. No public end-to-end implementation or 1K-device production evidence. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20345 | One supermarket chip-restocking task on a Unitree G1-Edu in a store replica, with repeated long-horizon trials and SFT/experience/OOD comparisons. Trial counts, control frequency, complete calibration thresholds, hardware compute, safety incidents and production SLO are not fully disclosed. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20379 | Released Qwen2.5-7B verbalizer audit and synthetic ground-truth domains; continued Pythia-160M training with 64/512 targets, fresh-probe AUC and verbalizer audits. Authors report roughly 2% audited grounding in the released system (sensitivity-limited lower bound), 0.010 nats added loss for 64 targets and 0.14-0.20 for 512. Small-model/sandbox scope, single-seed aspects and lossy natural-language readout limit generalization. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20734 | 200 GSM8K, 100 BIRD-SQL, 100 BrowseComp+ and 50 SWE-Bench Verified examples; seven-turn interactions across frontier/open models, with exact/official final evaluators. Ablations separate repeated turns from extra transitions and include a small Qwen3-4B GRPO pilot. Intermediate turns are not independently outcome-verified; GPT-5.1 builds/verifies components; user styles and multi-intent turns are excluded. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2607-20757 | Qwen2.5-0.5B full fine-tuning and Llama-2-7B LoRA, C4 for 8,192 steps, batch 1, sequence 512 (~4M tokens), WikiText-2 length 2,048; W4A16, W4A4 group-128 and per-token fake quantization. No real low-bit kernel timing, serving batch/concurrency/SLO or full-scale pretraining; strict per-token W4A4 still collapses. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19704 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: the representative-inference branch is important and remains Deep/Integrate, but its proxy-compatibility story is narrower than the selected cross-tenant security contract and overlaps the scheduling/evaluation handoff already documented in the review. | analysis-decision:SF-2026-ARXIV-2607-19704 |
| SF-2026-ARXIV-2607-19747 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: the setwise-retrieval mechanism is already fully integrated in Ch76; repeating it would displace a genuinely new evolution chain. | analysis-decision:SF-2026-ARXIV-2607-19747 |
| SF-2026-ARXIV-2607-19749 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: component-level continual forgetting is a strong new Ch25 branch, but the three narrative slots prioritize an immediate security invariant, a physical communication rewrite, and a correction to representation evidence; the complete Deep Review and Books patch remain mandatory. | analysis-decision:SF-2026-ARXIV-2607-19749 |
| SF-2026-ARXIV-2607-19865 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: executable artifact predicates and mutation-tested verifiers are durable, but Ch66 already has the broader answer-to-artifact spine; this source is best integrated there without consuming a top-level Daily narrative slot. | analysis-decision:SF-2026-ARXIV-2607-19865 |
| SF-2026-ARXIV-2607-19957 | score_7_9;potential_books_delta | selected | DA-20260723-01 | — | 命中合同第一优先级 security contract；V2=9/9；作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports a vulnerability in the authors’ position-independent multi-tenant reuse model and disclosed implementations. It does not prove ordinary exact-prefix cache reuse is vulnerable in the same way, deployed incidence, cache availability/probing in every platform, or that reported ASR generalizes beyond tested models/data.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260723-01 |
| SF-2026-ARXIV-2607-27231 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: the benchmark contract is valuable and integrates into Ch66, but it is primarily an evaluation-harness refinement; the selected MoX unit carries the underlying network data-flow evolution. | analysis-decision:SF-2026-ARXIV-2607-27231 |
| SF-2026-ARXIV-2607-20145 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: the phase-linked CPT/SFT/runtime lineage is a meaningful cross-stage contract, but the author evidence is family/hardware-specific and the mechanism can be integrated accurately without a separate top-three narrative. | analysis-decision:SF-2026-ARXIV-2607-20145 |
| SF-2026-ARXIV-2607-20220 | score_7_9;potential_books_delta | selected | DA-20260723-02 | — | V2=9/9；作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports the routing/tree algorithm and simulated/proxy improvements under disclosed topology and workload assumptions. It does not prove deadlock-free implementation, fault behavior, exact hardware timing, or universal gains over switch fabrics.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260723-02 |
| SF-2026-ARXIV-2607-20379 | score_7_9;potential_books_delta | selected | DA-20260723-03 | — | V2=9/9；作者正文与实验只支持 exact v1 在限定 contract 下的机制与结果；Supports failures of reconstruction-only scoring and the RECAP/probe results in disclosed settings. It does not establish neuron-level causal use, complete semantic legibility, safety under adaptive training, or that a high-AUC probe yields faithful language explanations.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260723-03 |
| SF-2026-ARXIV-2607-20734 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: the intent-transition EvalSpec is a strong Ch66 integration, but its main contribution is a benchmark-state refinement rather than one of the three highest-priority mechanism corrections for this Daily. | analysis-decision:SF-2026-ARXIV-2607-20734 |
| SF-2026-ARXIV-2607-20757 | score_7_9;potential_books_delta | not_selected | — | — | Not selected: learned gauge bases are a substantive training mechanism and remain Deep/Integrate, but evidence is limited to short continued-training plus fake quantization and lacks event-time implementation provenance before cutoff. | analysis-decision:SF-2026-ARXIV-2607-20757 |

<!-- analysis:DA-20260723-01:start -->
### HijackKV: New Threat in Position-Independent KV Cache Reuse

**旧方案为何合理。** Exact-prefix reuse is restrictive but safe-by-construction with respect to preceding causal context; position-independent reuse reasonably relaxes this to improve hit rate when state mismatch is treated only as a quality problem.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation 这条证据与现有主线的关系是 `Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Strict context/tenant binding sacrifices cross-context hit rate; selective recomputation retains more reuse but leaves residual attack surface and compute cost. Cryptographic integrity only proves bytes were not changed—it cannot prove the producer context was authorized.

<!-- analysis:DA-20260723-01:end -->

<!-- analysis:DA-20260723-02:start -->
### MoX: Efficient MoE Routing on Direct-Connect Topologies

**旧方案为何合理。** Direct unicast from source to each selected expert is simple and correct when a switch provides uniform bandwidth or expert fanout is small.（现有命题定位：`books/part-02-model/21-moe.md#L14-L14`）

**约束变化与机制。** Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion 这条证据与现有主线的关系是 `Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion`：它改变或补充 `MODEL-MOE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Multicast trees and in-network expert relays reduce repeated source traffic but add tree construction, relay load, ordering/reduction state and sensitivity to topology/failures. Direct unicast remains preferable on strong switched fabrics or rapidly changing topologies.

<!-- analysis:DA-20260723-02:end -->

<!-- analysis:DA-20260723-03:start -->
### Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations

**旧方案为何合理。** Reconstruction is an attractive self-contained score because it avoids external labels and tests whether a reader can recover the model output from an explanation.（现有命题定位：`books/part-01-worldview/05-what-neural-networks-learn.md#L12-L12`）

**约束变化与机制。** Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring 这条证据与现有主线的关系是 `Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring`：它改变或补充 `WORLDVIEW-REPRESENTATION` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** External decodability targets and independent probes reduce private-code circularity, but only monitor designated content, add objective cost and can drift. Reconstruction remains useful as one channel test, not a truth/causality certificate.

<!-- analysis:DA-20260723-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19704:start -->《Efficient Clustering with Provable Guardrails for LLM Inference at Scale》已完成 Deep Source Review。Not selected: the representative-inference branch is important and remains Deep/Integrate, but its proxy-compatibility story is narrower than the selected cross-tenant security contract and overlaps the scheduling/evaluation handoff already documented in the review.<!-- analysis-decision:SF-2026-ARXIV-2607-19704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19747:start -->《Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking》已完成 Deep Source Review。Not selected: the setwise-retrieval mechanism is already fully integrated in Ch76; repeating it would displace a genuinely new evolution chain.<!-- analysis-decision:SF-2026-ARXIV-2607-19747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19749:start -->《The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL》已完成 Deep Source Review。Not selected: component-level continual forgetting is a strong new Ch25 branch, but the three narrative slots prioritize an immediate security invariant, a physical communication rewrite, and a correction to representation evidence; the complete Deep Review and Books patch remain mandatory.<!-- analysis-decision:SF-2026-ARXIV-2607-19749:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19865:start -->《DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations》已完成 Deep Source Review。Not selected: executable artifact predicates and mutation-tested verifiers are durable, but Ch66 already has the broader answer-to-artifact spine; this source is best integrated there without consuming a top-level Daily narrative slot.<!-- analysis-decision:SF-2026-ARXIV-2607-19865:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27231:start -->《KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation》已完成 Deep Source Review。Not selected: the benchmark contract is valuable and integrates into Ch66, but it is primarily an evaluation-harness refinement; the selected MoX unit carries the underlying network data-flow evolution.<!-- analysis-decision:SF-2026-ARXIV-2607-27231:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20145:start -->《SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD》已完成 Deep Source Review。Not selected: the phase-linked CPT/SFT/runtime lineage is a meaningful cross-stage contract, but the author evidence is family/hardware-specific and the mechanism can be integrated accurately without a separate top-three narrative.<!-- analysis-decision:SF-2026-ARXIV-2607-20145:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20734:start -->《LLMs Get Lost in Evolving User Intent》已完成 Deep Source Review。Not selected: the intent-transition EvalSpec is a strong Ch66 integration, but its main contribution is a benchmark-state refinement rather than one of the three highest-priority mechanism corrections for this Daily.<!-- analysis-decision:SF-2026-ARXIV-2607-20734:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-20757:start -->《GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries》已完成 Deep Source Review。Not selected: learned gauge bases are a substantive training mechanism and remain Deep/Integrate, but evidence is limited to short continued-training plus fake quantization and lacks event-time implementation provenance before cutoff.<!-- analysis-decision:SF-2026-ARXIV-2607-20757:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-19704 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L195 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-19704 | delta:SF-2026-ARXIV-2607-19704 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-19704 |
| SF-2026-ARXIV-2607-19747 | AGENT-RAG | books/part-07-agent/76-rag.md#L14-L14 | books/part-07-agent/75-context.md#L14-L14; books/part-07-agent/77-memory.md#L14-L14 | existing:SF-2026-ARXIV-2607-19747 | delta:SF-2026-ARXIV-2607-19747 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19747 |
| SF-2026-ARXIV-2607-19749 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L175 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-19749 | delta:SF-2026-ARXIV-2607-19749 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-19749 |
| SF-2026-ARXIV-2607-19865 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L778 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-19865 | delta:SF-2026-ARXIV-2607-19865 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-19865 |
| SF-2026-ARXIV-2607-19957 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L732 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-19957 | delta:SF-2026-ARXIV-2607-19957 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-19957 |
| SF-2026-ARXIV-2607-27231 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L450 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-27231 | delta:SF-2026-ARXIV-2607-27231 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27231 |
| SF-2026-ARXIV-2607-20145 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L499 | books/part-04-training-system/35-checkpoint.md#L14-L14; books/part-04-training-system/37-tensor-parallel.md#L14-L14 | existing:SF-2026-ARXIV-2607-20145 | delta:SF-2026-ARXIV-2607-20145 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-20145 |
| SF-2026-ARXIV-2607-20220 | MODEL-MOE | books/part-02-model/21-moe.md#L242 | books/part-02-model/20-sampling.md#L14-L14; books/part-02-model/22-long-context.md#L14-L14 | existing:SF-2026-ARXIV-2607-20220 | delta:SF-2026-ARXIV-2607-20220 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-20220 |
| SF-2026-ARXIV-2607-20345 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-20345 | delta:SF-2026-ARXIV-2607-20345 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-20345 |
| SF-2026-ARXIV-2607-20379 | WORLDVIEW-REPRESENTATION | books/part-01-worldview/05-what-neural-networks-learn.md#L174 | books/part-01-worldview/04-why-models-learn.md#L12-L12; books/part-01-worldview/06-why-transformer-changed-the-world.md#L12-L12 | existing:SF-2026-ARXIV-2607-20379 | delta:SF-2026-ARXIV-2607-20379 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-20379 |
| SF-2026-ARXIV-2607-20734 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1225 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-20734 | delta:SF-2026-ARXIV-2607-20734 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-20734 |
| SF-2026-ARXIV-2607-20757 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L486 | books/part-04-training-system/27-data.md#L14-L14; books/part-04-training-system/29-sft.md#L14-L14 | existing:SF-2026-ARXIV-2607-20757 | delta:SF-2026-ARXIV-2607-20757 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-20757 |

<!-- books-review:SF-2026-ARXIV-2607-19704:start --><!-- existing:SF-2026-ARXIV-2607-19704:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L195` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-19704:end --><!-- delta:SF-2026-ARXIV-2607-19704:start -->新增证据边界：Layering / Dependency: request-level semantic coalescing -> representative inference -> member-level reuse under explicit guardrails 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L195`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19704:end --><!-- books-review:SF-2026-ARXIV-2607-19704:end -->

<!-- books-review:SF-2026-ARXIV-2607-19747:start --><!-- existing:SF-2026-ARXIV-2607-19747:start -->对读 `books/part-07-agent/76-rag.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/76-rag.md#L14-L14`）为：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2607-19747:end --><!-- delta:SF-2026-ARXIV-2607-19747:start -->新增证据边界：Direct Evolution: pointwise relevance ranking -> set-level coverage, redundancy, conflict and complementarity under a bounded context budget 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-19747:end --><!-- books-review:SF-2026-ARXIV-2607-19747:end -->

<!-- books-review:SF-2026-ARXIV-2607-19749:start --><!-- existing:SF-2026-ARXIV-2607-19749:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L175` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-19749:end --><!-- delta:SF-2026-ARXIV-2607-19749:start -->新增证据边界：Direct Evolution: replay that preserves predictive state -> component-level forgetting diagnosis -> actor rehearsal from graded imagined trajectories 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L175`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19749:end --><!-- books-review:SF-2026-ARXIV-2607-19749:end -->

<!-- books-review:SF-2026-ARXIV-2607-19865:start --><!-- existing:SF-2026-ARXIV-2607-19865:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L778` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-19865:end --><!-- delta:SF-2026-ARXIV-2607-19865:start -->新增证据边界：Direct Evolution: final-answer judge -> executable artifact-state predicates plus preservation invariants and verifier-fidelity audit 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L778`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19865:end --><!-- books-review:SF-2026-ARXIV-2607-19865:end -->

<!-- books-review:SF-2026-ARXIV-2607-19957:start --><!-- existing:SF-2026-ARXIV-2607-19957:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L732` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-19957:end --><!-- delta:SF-2026-ARXIV-2607-19957:start -->新增证据边界：Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L732`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19957:end --><!-- books-review:SF-2026-ARXIV-2607-19957:end -->

<!-- books-review:SF-2026-ARXIV-2607-27231:start --><!-- existing:SF-2026-ARXIV-2607-27231:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L450` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-27231:end --><!-- delta:SF-2026-ARXIV-2607-27231:start -->新增证据边界：Direct Evolution: single-source/single-GPU pass rate -> multi-source operator contract -> cross-chip correctness, speed and cost frontier 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L450`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27231:end --><!-- books-review:SF-2026-ARXIV-2607-27231:end -->

<!-- books-review:SF-2026-ARXIV-2607-20145:start --><!-- existing:SF-2026-ARXIV-2607-20145:start -->对读 `books/part-04-training-system/36-distributed-training.md#L499` 与相邻章节后，现有命题（`books/part-04-training-system/36-distributed-training.md#L14-L14`）为：本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。<!-- existing:SF-2026-ARXIV-2607-20145:end --><!-- delta:SF-2026-ARXIV-2607-20145:start -->新增证据边界：Layering / Dependency: domain CPT and verified SFT recipe -> phase-aligned distributed runtime -> provenance-linked deployable artifact 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L499`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-20145:end --><!-- books-review:SF-2026-ARXIV-2607-20145:end -->

<!-- books-review:SF-2026-ARXIV-2607-20220:start --><!-- existing:SF-2026-ARXIV-2607-20220:start -->对读 `books/part-02-model/21-moe.md#L242` 与相邻章节后，现有命题（`books/part-02-model/21-moe.md#L14-L14`）为：本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。<!-- existing:SF-2026-ARXIV-2607-20220:end --><!-- delta:SF-2026-ARXIV-2607-20220:start -->新增证据边界：Direct Evolution: source-to-destination unicast dispatch -> selected-expert multicast tree -> reverse-tree partial reduction under direct-connect congestion 该 delta 已进入 `books/part-02-model/21-moe.md#L242`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-20220:end --><!-- books-review:SF-2026-ARXIV-2607-20220:end -->

<!-- books-review:SF-2026-ARXIV-2607-20345:start --><!-- existing:SF-2026-ARXIV-2607-20345:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-20345:end --><!-- delta:SF-2026-ARXIV-2607-20345:start -->新增证据边界：Layering / Dependency: curated VLA SFT -> advantage-conditioned experience refinement -> OOD-triggered fallback in a physical loop 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-20345:end --><!-- books-review:SF-2026-ARXIV-2607-20345:end -->

<!-- books-review:SF-2026-ARXIV-2607-20379:start --><!-- existing:SF-2026-ARXIV-2607-20379:start -->对读 `books/part-01-worldview/05-what-neural-networks-learn.md#L174` 与相邻章节后，现有命题（`books/part-01-worldview/05-what-neural-networks-learn.md#L12-L12`）为：训练把大量数值参数更新到了某个低损失区域。那些参数里究竟有什么？模型是在存储样本、提取规则、建立世界模型，还是以另一种方式组织经验？<!-- existing:SF-2026-ARXIV-2607-20379:end --><!-- delta:SF-2026-ARXIV-2607-20379:start -->新增证据边界：Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring 该 delta 已进入 `books/part-01-worldview/05-what-neural-networks-learn.md#L174`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-20379:end --><!-- books-review:SF-2026-ARXIV-2607-20379:end -->

<!-- books-review:SF-2026-ARXIV-2607-20734:start --><!-- existing:SF-2026-ARXIV-2607-20734:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1225` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-20734:end --><!-- delta:SF-2026-ARXIV-2607-20734:start -->新增证据边界：Direct Evolution: static single-turn task -> versioned intent-state transitions -> final anchored verifier plus transition-specific diagnostics 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1225`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-20734:end --><!-- books-review:SF-2026-ARXIV-2607-20734:end -->

<!-- books-review:SF-2026-ARXIV-2607-20757:start --><!-- existing:SF-2026-ARXIV-2607-20757:start -->对读 `books/part-04-training-system/28-pretraining.md#L486` 与相邻章节后，现有命题（`books/part-04-training-system/28-pretraining.md#L14-L14`）为：本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。<!-- existing:SF-2026-ARXIV-2607-20757:end --><!-- delta:SF-2026-ARXIV-2607-20757:start -->新增证据边界：Direct Evolution: post-training/random rotation -> symmetry-preserving learned basis during training -> quantized artifact with explicit runtime transform cost 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L486`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-20757:end --><!-- books-review:SF-2026-ARXIV-2607-20757:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260723-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260723; semantic-review:SA-20260723-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260723-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-19704; review:SF-2026-ARXIV-2607-19747; review:SF-2026-ARXIV-2607-19749; review:SF-2026-ARXIV-2607-19865; review:SF-2026-ARXIV-2607-19957; review:SF-2026-ARXIV-2607-27231; review:SF-2026-ARXIV-2607-20145; review:SF-2026-ARXIV-2607-20159; review:SF-2026-ARXIV-2607-20220; review:SF-2026-ARXIV-2607-20345; review:SF-2026-ARXIV-2607-20379; review:SF-2026-ARXIV-2607-20694; review:SF-2026-ARXIV-2607-20734; review:SF-2026-ARXIV-2607-20757; semantic-review:SA-20260723-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260723-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260723-01; analysis:DA-20260723-02; analysis:DA-20260723-03; semantic-review:SA-20260723-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260723-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-19704; books-review:SF-2026-ARXIV-2607-19747; books-review:SF-2026-ARXIV-2607-19749; books-review:SF-2026-ARXIV-2607-19865; books-review:SF-2026-ARXIV-2607-19957; books-review:SF-2026-ARXIV-2607-27231; books-review:SF-2026-ARXIV-2607-20145; books-review:SF-2026-ARXIV-2607-20220; books-review:SF-2026-ARXIV-2607-20345; books-review:SF-2026-ARXIV-2607-20379; books-review:SF-2026-ARXIV-2607-20734; books-review:SF-2026-ARXIV-2607-20757; review:SF-2026-ARXIV-2607-20694; semantic-review:SA-20260723-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260723-COVERAGE:start -->Fresh-context audit verified the frozen 14-family denominator and strict Beijing window [2026-07-22 09:00, 2026-07-23 09:00), with zero identifier overlap against D22 or D24. Artifact coverage now matches observed evidence: eight families own nine event-time pinned commits, the GitHub Coverage Receipt records all nine bounded lookups, and Candidate Ledger supporting-source attribution appears only on those eight families. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260723-COVERAGE:end -->
<!-- semantic-review:SA-20260723-EVIDENCE:start -->Fresh-context audit recomputed all fourteen exact-v1 snapshot SHA-256 digests and confirmed packet-to-central-to-Daily consistency for reviewed canonical versions, durable snapshot paths, hashes, locators, routes, scores, claim boundaries, artifact boundaries and dispositions. All pinned commits are versioned as SRC-GITHUB-COMMIT@commit:<sha>; disclosed but unpinned artifacts remain bounded without unsupported commit attribution. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260723-EVIDENCE:end -->
<!-- semantic-review:SA-20260723-SELECTION:start -->Fresh-context audit verified an eligibility denominator of exactly eleven Deep families, with three selected narrative units and eight source-specific non-selection rationales persisted consistently in packet and Daily. The one Standard and two Closure families remain outside Selection without losing their completed Source Reviews or dispositions. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260723-SELECTION:end -->
<!-- semantic-review:SA-20260723-BOOKS:start -->Fresh-context regression audit confirmed that all ten integrated passages and corresponding exact-v1 Review notes remain present in their unique canonical owner chapters. Owner and adjacent-chapter handoffs preserve the old baseline, changed constraint, mechanism or state/control ownership, benefit, trade-off, failure/evidence boundary and coexistence condition. The remaining one Deep No Change, one Standard No Change, one Weekly Only and one Rejected disposition remain consistent across packet and Daily without duplicate Books ownership. Books PASS; finding_count=0.<!-- semantic-review:SA-20260723-BOOKS:end -->

## 8. Ignored Noise

1063 个窗口内 identity 中，1049 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：10 个 `Integrate`，2 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，1 个 `Rejected — Low Durability / Out of Scope`；Deep 11 / Standard 1。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/23/README.md`。
- 本日报长期 delta 已同步至：`books/part-01-worldview/05-what-neural-networks-learn.md`、`books/part-02-model/21-moe.md`、`books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-04-training-system/28-pretraining.md`、`books/part-04-training-system/36-distributed-training.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Efficient Clustering with Provable Guardrails for LLM Inference at Scale](https://arxiv.org/abs/2607.19704v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking](https://arxiv.org/abs/2607.19747v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL](https://arxiv.org/abs/2607.19749v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations](https://arxiv.org/abs/2607.19865v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [HijackKV: New Threat in Position-Independent KV Cache Reuse](https://arxiv.org/abs/2607.19957v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation](https://arxiv.org/abs/2607.27231v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD](https://arxiv.org/abs/2607.20145v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [SHFormer: Dynamic Spectral Filtering Convolutional Neural Network and High-pass Kernel Generation Transformer for Adaptive MRI Reconstruction](https://arxiv.org/abs/2607.20159v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [MoX: Efficient MoE Routing on Direct-Connect Topologies](https://arxiv.org/abs/2607.20220v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids](https://arxiv.org/abs/2607.20345v1) — first-public（Asia/Shanghai）：2026-07-23；accessed：2026-08-27
- [Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations](https://arxiv.org/abs/2607.20379v1) — first-public（Asia/Shanghai）：2026-07-23；accessed：2026-08-27
- [Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions](https://arxiv.org/abs/2607.20694v1) — first-public（Asia/Shanghai）：2026-07-23；accessed：2026-08-27
- [LLMs Get Lost in Evolving User Intent](https://arxiv.org/abs/2607.20734v1) — first-public（Asia/Shanghai）：2026-07-23；accessed：2026-08-27
- [GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries](https://arxiv.org/abs/2607.20757v1) — first-public（Asia/Shanghai）：2026-07-23；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
