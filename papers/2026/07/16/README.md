# Daily Research — 2026-07-16

**Research Date:** 2026-07-16

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-15 09:00:00 ～ 2026-07-16 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1050 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 18 个。当前路由账目为 8 个 Deep、6 个 Standard、4 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-16 |
| Window End | 2026-07-16 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-16-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T15:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-15T09:00:00+08:00 | 2026-07-16T09:00:00+08:00 | 2026-08-27T15:20:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1050 | SF-2026-ARXIV-2607-13399<br>SF-2026-ARXIV-2607-13410<br>SF-2026-ARXIV-2607-13429<br>SF-2026-ARXIV-2607-13511<br>SF-2026-ARXIV-2607-13605<br>SF-2026-ARXIV-2607-14169<br>SF-2026-ARXIV-2607-13649<br>SF-2026-ARXIV-2607-13651<br>SF-2026-ARXIV-2607-13705<br>SF-2026-ARXIV-2607-14178<br>SF-2026-ARXIV-2607-13921<br>SF-2026-ARXIV-2607-13926<br>SF-2026-ARXIV-2607-14005<br>SF-2026-ARXIV-2607-14076<br>SF-2026-ARXIV-2607-14236<br>SF-2026-ARXIV-2607-14280<br>SF-2026-ARXIV-2607-14396<br>SF-2026-ARXIV-2607-14431 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-16T09:00:00+08:00 | coverage:SRC-ARXIV:20260716 | GAP-ARXIV-DIRECT-RESET-20260716 |
| SRC-GITHUB-COMMIT | 2026-07-15T09:00:00+08:00 | 2026-07-16T09:00:00+08:00 | 2026-08-27T15:20:00+08:00 | exact GitHub commit API lookups: JaviMaligno/code-world-models@47240d07ac3b1b5d301e5a82c977ae308240e108; AlbughdadiM/lewm-eo-cloud-monitoring@ed989abb4b3534ab5e5f041b1ec6fd87066658c6; open-compass/AgentCompass@7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74; eth-sri/generative-compilation@ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e; pegah-kh/dimas@972db401c4aa4c4491004c836cc20d5596042c45 | checked | 5 | SF-2026-ARXIV-2607-14169; SF-2026-ARXIV-2607-13651; SF-2026-ARXIV-2607-13705; SF-2026-ARXIV-2607-13921; SF-2026-ARXIV-2607-14280 | pages=5; final cursors=47240d07ac3b1b5d301e5a82c977ae308240e108,ed989abb4b3534ab5e5f041b1ec6fd87066658c6,7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74,ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e,972db401c4aa4c4491004c836cc20d5596042c45; one bounded commit lookup per family | 2026-07-16T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260716 | — |

<!-- coverage:SRC-ARXIV:20260716:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1050 unique identities in this strict window; 18 routed families.<!-- coverage:SRC-ARXIV:20260716:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260716:start -->repository=JaviMaligno/code-world-models, until=2026-07-16T01:00:00Z, full_sha=47240d07ac3b1b5d301e5a82c977ae308240e108, commit_timestamp=2026-07-15T21:13:47Z, url=https://github.com/JaviMaligno/code-world-models/commit/47240d07ac3b1b5d301e5a82c977ae308240e108; repository=AlbughdadiM/lewm-eo-cloud-monitoring, until=2026-07-16T01:00:00Z, full_sha=ed989abb4b3534ab5e5f041b1ec6fd87066658c6, commit_timestamp=2026-07-15T09:24:47Z, url=https://github.com/AlbughdadiM/lewm-eo-cloud-monitoring/commit/ed989abb4b3534ab5e5f041b1ec6fd87066658c6; repository=open-compass/AgentCompass, until=2026-07-16T01:00:00Z, full_sha=7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74, commit_timestamp=2026-07-15T11:34:55Z, url=https://github.com/open-compass/AgentCompass/commit/7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74; repository=eth-sri/generative-compilation, until=2026-07-16T01:00:00Z, full_sha=ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e, commit_timestamp=2026-07-15T12:19:40Z, url=https://github.com/eth-sri/generative-compilation/commit/ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e; repository=pegah-kh/dimas, until=2026-07-16T01:00:00Z, full_sha=972db401c4aa4c4491004c836cc20d5596042c45, commit_timestamp=2026-07-15T22:14:31Z, url=https://github.com/pegah-kh/dimas/commit/972db401c4aa4c4491004c836cc20d5596042c45; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260716:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 18 个 family：exact v1 为 8 个 family 披露 artifact/evidence locator，其中 8 个提供外部 repository/project/demo locator，另有 10 个未披露；本日确认 5 个 family、5 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13399 | arXiv:2607.13399v1 | paper-v1:2607.13399 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13399 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-13399 | yes |
| SF-2026-ARXIV-2607-13410 | arXiv:2607.13410v1 | paper-v1:2607.13410 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13410 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-13410 | yes |
| SF-2026-ARXIV-2607-13429 | arXiv:2607.13429v1 | paper-v1:2607.13429 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-13429 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-13429 | yes |
| SF-2026-ARXIV-2607-13511 | arXiv:2607.13511v1 | paper-v1:2607.13511 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13511 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13511 | yes |
| SF-2026-ARXIV-2607-13605 | arXiv:2607.13605v1 | paper-v1:2607.13605 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 1 | 1 | 2 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-13605 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-14169 | arXiv:2607.14169v1 | paper-v1:2607.14169 | 2026-W29 | 2026-07-15 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14169 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-14169 | yes |
| SF-2026-ARXIV-2607-13649 | arXiv:2607.13649v1 | paper-v1:2607.13649 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13649 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13649 | yes |
| SF-2026-ARXIV-2607-13651 | arXiv:2607.13651v1 | paper-v1:2607.13651 | 2026-W29 | 2026-07-15 | SRC-ARXIV; SRC-GITHUB-COMMIT | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-13651 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-13705 | arXiv:2607.13705v1 | paper-v1:2607.13705 | 2026-W29 | 2026-07-15 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13705 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-13705 | yes |
| SF-2026-ARXIV-2607-14178 | arXiv:2607.14178v1 | paper-v1:2607.14178 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-14178 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-13921 | arXiv:2607.13921v1 | paper-v1:2607.13921 | 2026-W29 | 2026-07-15 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13921 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2607-13921 | yes |
| SF-2026-ARXIV-2607-13926 | arXiv:2607.13926v1 | paper-v1:2607.13926 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13926 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13926 | yes |
| SF-2026-ARXIV-2607-14005 | arXiv:2607.14005v1 | paper-v1:2607.14005 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14005 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14005 | yes |
| SF-2026-ARXIV-2607-14076 | arXiv:2607.14076v1 | paper-v1:2607.14076 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14076 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14076 | yes |
| SF-2026-ARXIV-2607-14236 | arXiv:2607.14236v1 | paper-v1:2607.14236 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14236 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-14236 | yes |
| SF-2026-ARXIV-2607-14280 | arXiv:2607.14280v1 | paper-v1:2607.14280 | 2026-W29 | 2026-07-16 | SRC-ARXIV; SRC-GITHUB-COMMIT | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14280 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14280 | yes |
| SF-2026-ARXIV-2607-14396 | arXiv:2607.14396v1 | paper-v1:2607.14396 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-14396 | self | — | new_in_window | AGENT-PLATFORM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-14431 | arXiv:2607.14431v1 | paper-v1:2607.14431 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14431 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13399 | RP-c2c8d096855da359 | deep | arXiv:2607.13399v1 | SRC-ARXIV@arXiv:2607.13399v1 | https://arxiv.org/html/2607.13399v1#S3; https://arxiv.org/html/2607.13399v1#S4; https://arxiv.org/html/2607.13399v1#S5 | https://arxiv.org/html/2607.13399v1#S2.SS2; https://arxiv.org/html/2607.13399v1#S5.SS2; https://arxiv.org/html/2607.13399v1#A1 | https://arxiv.org/html/2607.13399v1#Sx1; https://arxiv.org/html/2607.13399v1#S7 | Not Disclosed — exact v1 links no author implementation artifact | claim:SF-2026-ARXIV-2607-13399 | complete |
| SF-2026-ARXIV-2607-13410 | RP-4563ce723ef2434f | deep | arXiv:2607.13410v1 | SRC-ARXIV@arXiv:2607.13410v1 | https://arxiv.org/html/2607.13410v1#S4; https://arxiv.org/html/2607.13410v1#S5 | https://arxiv.org/html/2607.13410v1#S6.SS1; https://arxiv.org/html/2607.13410v1#S6.SS3; https://arxiv.org/html/2607.13410v1#S6.SS4 | https://arxiv.org/html/2607.13410v1#S7 | Not Disclosed — no author code or immutable model artifact linked in exact v1 | claim:SF-2026-ARXIV-2607-13410 | complete |
| SF-2026-ARXIV-2607-13429 | RP-37ff60d30ed423e5 | deep | arXiv:2607.13429v1 | SRC-ARXIV@arXiv:2607.13429v1 | https://arxiv.org/html/2607.13429v1#S3.SS2; https://arxiv.org/html/2607.13429v1#S3.SS3 | https://arxiv.org/html/2607.13429v1#S4.SS2; https://arxiv.org/html/2607.13429v1#S4.SS3; https://arxiv.org/html/2607.13429v1#S4.SS4; https://arxiv.org/html/2607.13429v1#A2.SS5 | https://arxiv.org/html/2607.13429v1#S5; https://arxiv.org/html/2607.13429v1#A3.SS3 | https://anchoralignvla.github.io — project page; Not Disclosed — exact v1 links no immutable author code repository | claim:SF-2026-ARXIV-2607-13429 | complete |
| SF-2026-ARXIV-2607-13511 | RP-1ba3623ac46b8714 | standard | arXiv:2607.13511v1 | SRC-ARXIV@arXiv:2607.13511v1 | https://arxiv.org/html/2607.13511v1#S2.SS1; https://arxiv.org/html/2607.13511v1#S2.SS4; https://arxiv.org/html/2607.13511v1#A1 | https://arxiv.org/html/2607.13511v1#S3.SS3; https://arxiv.org/html/2607.13511v1#S3.SS5 | https://arxiv.org/html/2607.13511v1#S5 | Not Disclosed — no public fused kernel or reproduction repository linked in exact v1 | claim:SF-2026-ARXIV-2607-13511 | complete |
| SF-2026-ARXIV-2607-13605 | RP-7730c19b15a9ac33 | closure | arXiv:2607.13605v1 | SRC-ARXIV@arXiv:2607.13605v1 | https://arxiv.org/html/2607.13605v1#S3 | https://arxiv.org/html/2607.13605v1#S4 | https://arxiv.org/html/2607.13605v1#S5.SS3 | Not Disclosed — no author artifact linked in exact v1 | claim:SF-2026-ARXIV-2607-13605 | complete |
| SF-2026-ARXIV-2607-14169 | RP-2e4c682a0d92eb30 | deep | arXiv:2607.14169v1 | SRC-ARXIV@arXiv:2607.14169v1; SRC-GITHUB-COMMIT@commit:47240d07ac3b1b5d301e5a82c977ae308240e108 | https://arxiv.org/html/2607.14169v1#S2; https://arxiv.org/html/2607.14169v1#S4; https://arxiv.org/html/2607.14169v1#S6 | https://arxiv.org/html/2607.14169v1#S3; https://arxiv.org/html/2607.14169v1#S5; https://arxiv.org/html/2607.14169v1#A1 | https://arxiv.org/html/2607.14169v1#S8 | https://github.com/JaviMaligno/code-world-models/commit/47240d07ac3b1b5d301e5a82c977ae308240e108 | claim:SF-2026-ARXIV-2607-14169 | complete |
| SF-2026-ARXIV-2607-13649 | RP-1fc455004bf20d5c | standard | arXiv:2607.13649v1 | SRC-ARXIV@arXiv:2607.13649v1 | https://arxiv.org/html/2607.13649v1#S2; https://arxiv.org/html/2607.13649v1#S3 | https://arxiv.org/html/2607.13649v1#S4 | Not Disclosed — no dedicated limitations section; simulation/tapeout boundary comes from S4 | Not Disclosed — no public RTL/tapeout artifact | claim:SF-2026-ARXIV-2607-13649 | complete |
| SF-2026-ARXIV-2607-13651 | RP-6fe2c927d8bc6a0a | closure | arXiv:2607.13651v1 | SRC-ARXIV@arXiv:2607.13651v1; SRC-GITHUB-COMMIT@commit:ed989abb4b3534ab5e5f041b1ec6fd87066658c6 | https://arxiv.org/html/2607.13651v1#S5 | https://arxiv.org/html/2607.13651v1#S7; https://arxiv.org/html/2607.13651v1#S8 | https://arxiv.org/html/2607.13651v1#S9 | https://github.com/AlbughdadiM/lewm-eo-cloud-monitoring/commit/ed989abb4b3534ab5e5f041b1ec6fd87066658c6 | claim:SF-2026-ARXIV-2607-13651 | complete |
| SF-2026-ARXIV-2607-13705 | RP-9339bbf548eb4b38 | deep | arXiv:2607.13705v1 | SRC-ARXIV@arXiv:2607.13705v1; SRC-GITHUB-COMMIT@commit:7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74 | https://arxiv.org/html/2607.13705v1#S3 | https://arxiv.org/html/2607.13705v1#S4; https://arxiv.org/html/2607.13705v1#A1 | Not Disclosed — no dedicated section; harness sensitivity is evidenced in S4 | https://github.com/open-compass/AgentCompass/commit/7faf1a6cc5c2b0cfd0c9934f1262ebe211830b74 | claim:SF-2026-ARXIV-2607-13705 | complete |
| SF-2026-ARXIV-2607-14178 | RP-7496ef0926d9e42e | closure | arXiv:2607.14178v1 | SRC-ARXIV@arXiv:2607.14178v1 | https://arxiv.org/html/2607.14178v1#S3; https://arxiv.org/html/2607.14178v1#S4 | https://arxiv.org/html/2607.14178v1#S5 | https://arxiv.org/html/2607.14178v1#S6 | https://github.com/ReasLab/ReasFlow — disclosed, but GitHub API returned no commit at or before 2026-07-16T01:00:00Z | claim:SF-2026-ARXIV-2607-14178 | complete |
| SF-2026-ARXIV-2607-13921 | RP-91df5f1b7478601e | deep | arXiv:2607.13921v1 | SRC-ARXIV@arXiv:2607.13921v1; SRC-ARXIV-SOURCE@https://export.arxiv.org/e-print/2607.13921v1; SRC-GITHUB-COMMIT@commit:ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e | https://export.arxiv.org/e-print/2607.13921v1 :: Methodology: exact source files sections-new/method.tex and sections-new/rust.tex | https://export.arxiv.org/e-print/2607.13921v1 :: Experiments: exact source files sections-new/eval.tex and sections-new/appendix/app_experimental_details.tex | https://export.arxiv.org/e-print/2607.13921v1 :: Scope and Limitations: exact source file sections-new/discussion.tex; compiler success is not functional/security correctness | https://github.com/eth-sri/generative-compilation/commit/ee3e21d6f0c62dd0931ff483b1e35f86adf80f2e | claim:SF-2026-ARXIV-2607-13921 | complete |
| SF-2026-ARXIV-2607-13926 | RP-9b670c7d723cb027 | standard | arXiv:2607.13926v1 | SRC-ARXIV@arXiv:2607.13926v1 | https://arxiv.org/html/2607.13926v1#S2.SS1; https://arxiv.org/html/2607.13926v1#S2.SS2; https://arxiv.org/html/2607.13926v1#S2.SS3 | https://arxiv.org/html/2607.13926v1#S3; https://arxiv.org/html/2607.13926v1#S4.SS3 | Not Disclosed — no dedicated limitations section; https://arxiv.org/html/2607.13926v1#S5 scopes the conclusion | Not Disclosed — no author code linked | claim:SF-2026-ARXIV-2607-13926 | complete |
| SF-2026-ARXIV-2607-14005 | RP-106bd002530a68cd | standard | arXiv:2607.14005v1 | SRC-ARXIV@arXiv:2607.14005v1 | https://arxiv.org/html/2607.14005v1#S3; https://arxiv.org/html/2607.14005v1#S4.SS2; https://arxiv.org/html/2607.14005v1#S4.SS3 | https://arxiv.org/html/2607.14005v1#S8; https://arxiv.org/html/2607.14005v1#S9 | https://arxiv.org/html/2607.14005v1#S10 — closed-loop policy interaction remains future work | Not Disclosed — no author code/model artifact linked | claim:SF-2026-ARXIV-2607-14005 | complete |
| SF-2026-ARXIV-2607-14076 | RP-f2331c09a12cd6e3 | standard | arXiv:2607.14076v1 | SRC-ARXIV@arXiv:2607.14076v1 | https://arxiv.org/html/2607.14076v1#S3 | https://arxiv.org/html/2607.14076v1#S4 | https://arxiv.org/html/2607.14076v1#S5 | Not Disclosed — no immutable dataset release linked | claim:SF-2026-ARXIV-2607-14076 | complete |
| SF-2026-ARXIV-2607-14236 | RP-a0c1f471a07fe6d5 | deep | arXiv:2607.14236v1 | SRC-ARXIV@arXiv:2607.14236v1 | https://arxiv.org/html/2607.14236v1#S3.SS1; https://arxiv.org/html/2607.14236v1#S3.SS2; https://arxiv.org/html/2607.14236v1#A2; https://arxiv.org/html/2607.14236v1#A3 | https://arxiv.org/html/2607.14236v1#S4; https://arxiv.org/html/2607.14236v1#A7; https://arxiv.org/html/2607.14236v1#A8 | https://arxiv.org/html/2607.14236v1#S6; https://arxiv.org/html/2607.14236v1#A10; https://arxiv.org/html/2607.14236v1#A11 | https://lift-policy.github.io — project page; code promised after acceptance and therefore not event-time accessible | claim:SF-2026-ARXIV-2607-14236 | complete |
| SF-2026-ARXIV-2607-14280 | RP-d071d5e510e3fbf0 | standard | arXiv:2607.14280v1 | SRC-ARXIV@arXiv:2607.14280v1; SRC-ARXIV-SOURCE@https://export.arxiv.org/e-print/2607.14280v1; SRC-GITHUB-COMMIT@commit:972db401c4aa4c4491004c836cc20d5596042c45 | https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/method.tex | https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/experiments.tex; https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/ablation.tex; https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/appendix.tex | https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/conclusion.tex; transfer and steering-layer sensitivity in appendix.tex | https://github.com/pegah-kh/dimas/commit/972db401c4aa4c4491004c836cc20d5596042c45 | claim:SF-2026-ARXIV-2607-14280 | complete |
| SF-2026-ARXIV-2607-14396 | RP-270f62cf8c1592aa | closure | arXiv:2607.14396v1 | SRC-ARXIV@arXiv:2607.14396v1 | https://arxiv.org/html/2607.14396v1#S2 | https://arxiv.org/html/2607.14396v1#S3 | https://arxiv.org/html/2607.14396v1#S5 | Not Disclosed — no public implementation artifact | claim:SF-2026-ARXIV-2607-14396 | complete |
| SF-2026-ARXIV-2607-14431 | RP-7ba0bbb9625b34ae | deep | arXiv:2607.14431v1 | SRC-ARXIV@arXiv:2607.14431v1 | https://arxiv.org/html/2607.14431v1#S3.SS2; https://arxiv.org/html/2607.14431v1#S3.SS3; https://arxiv.org/html/2607.14431v1#S3.SS4 | https://arxiv.org/html/2607.14431v1#S4.SS1; https://arxiv.org/html/2607.14431v1#S4.SS5; https://arxiv.org/html/2607.14431v1#S4.SS7; https://arxiv.org/html/2607.14431v1#S4.SS13 | https://arxiv.org/html/2607.14431v1#S5.SS3; https://arxiv.org/html/2607.14431v1#S5.SS4 | Not Disclosed — proprietary graft engine and closed benchmark; paper describes hashes but no executable artifact | claim:SF-2026-ARXIV-2607-14431 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-13399:start -->
#### Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations

<!-- claim:SF-2026-ARXIV-2607-13399:start -->Authors show prompt diversity and signal quality dominate teacher scale in tested math reasoning settings; the project inference is to version reachable prompt coverage with the objective. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13399:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** OPD is an exploration catalyst on student-owned on-policy states, not a capacity creator; teacher/student mismatch and length aggregation can corrupt the guidance signal. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13399v1#S3; https://arxiv.org/html/2607.13399v1#S4; https://arxiv.org/html/2607.13399v1#S5`；Evaluation：`https://arxiv.org/html/2607.13399v1#S2.SS2; https://arxiv.org/html/2607.13399v1#S5.SS2; https://arxiv.org/html/2607.13399v1#A1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13399v1#Sx1; https://arxiv.org/html/2607.13399v1#S7`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1047-L1056`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13399:end -->

<!-- review:SF-2026-ARXIV-2607-13410:start -->
#### Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation

<!-- claim:SF-2026-ARXIV-2607-13410:start -->The paper proves an entropy/KL reduction under stated assumptions and reports CARLA cross-chassis results; the reusable project conclusion is conditional factorization of known deterministic transition components, not autonomous-driving universality. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13410:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Known ego motion is factored out of egocentric observation transition and propagated as an identifiable context, leaving the learned world model to spend capacity on residual scene dynamics. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13410v1#S4; https://arxiv.org/html/2607.13410v1#S5`；Evaluation：`https://arxiv.org/html/2607.13410v1#S6.SS1; https://arxiv.org/html/2607.13410v1#S6.SS3; https://arxiv.org/html/2607.13410v1#S6.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13410v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13410:end -->

<!-- review:SF-2026-ARXIV-2607-13429:start -->
#### Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

<!-- claim:SF-2026-ARXIV-2607-13429:start -->Authors report cross-architecture simulation and xArm7 gains; this supports a bounded preservation/alignment branch, not universal catastrophic-forgetting prevention. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13429:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** VLA fine-tuning is split into action learning, frozen-teacher representation anchoring and same-observation language-action alignment, avoiding the false choice between preserving semantic priors and learning control. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13429v1#S3.SS2; https://arxiv.org/html/2607.13429v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.13429v1#S4.SS2; https://arxiv.org/html/2607.13429v1#S4.SS3; https://arxiv.org/html/2607.13429v1#S4.SS4; https://arxiv.org/html/2607.13429v1#A2.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13429v1#S5; https://arxiv.org/html/2607.13429v1#A3.SS3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13429:end -->

<!-- review:SF-2026-ARXIV-2607-13511:start -->
#### ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level

<!-- claim:SF-2026-ARXIV-2607-13511:start -->Authors prove matrix residual convergence and report one 4B perplexity conversion; no downstream tasks, fused kernels or greater-than-4B validation are provided. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13511:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Expanded-rank ternary factors turn inner-rank multiplier and sparsity threshold into continuous accuracy/storage dials; monotone residual reduction is a representation result, not executable speed evidence. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13511v1#S2.SS1; https://arxiv.org/html/2607.13511v1#S2.SS4; https://arxiv.org/html/2607.13511v1#A1`；Evaluation：`https://arxiv.org/html/2607.13511v1#S3.SS3; https://arxiv.org/html/2607.13511v1#S3.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13511v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-13511:end -->

<!-- review:SF-2026-ARXIV-2607-13605:start -->
#### An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-13605:start -->Three-run LIBERO-10 results only; no general hierarchy claim. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13605:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A bounded interface study shows stage metadata is not automatically useful and depends on representation and training order. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13605v1#S3`；Evaluation：`https://arxiv.org/html/2607.13605v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13605v1#S5.SS3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 1 / Durability 2 = **4/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Rejected — Low Durability / Out of Scope`。
<!-- review:SF-2026-ARXIV-2607-13605:end -->

<!-- review:SF-2026-ARXIV-2607-14169:start -->
#### When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models

<!-- claim:SF-2026-ARXIV-2607-14169:start -->Formal witnesses and selected games show a verified transition model can still lose; not a universal learned-video bound. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14169:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Transition accuracy must evolve to planner-induced coverage, play adequacy and separate belief/inference validation. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14169v1#S2; https://arxiv.org/html/2607.14169v1#S4; https://arxiv.org/html/2607.14169v1#S6`；Evaluation：`https://arxiv.org/html/2607.14169v1#S3; https://arxiv.org/html/2607.14169v1#S5; https://arxiv.org/html/2607.14169v1#A1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14169v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14169:end -->

<!-- review:SF-2026-ARXIV-2607-13649:start -->
#### CIMERA: Compute-in-Interconnect and Memory with Reconfigurable Precision for LLM Inference

<!-- claim:SF-2026-ARXIV-2607-13649:start -->Simulation/co-verification only; reported H100 ratios are not silicon or production SLO evidence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13649:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Precision becomes a compiler/runtime execution-plan dimension mapped to reconfigurable compute-in-memory/interconnect hardware. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13649v1#S2; https://arxiv.org/html/2607.13649v1#S3`；Evaluation：`https://arxiv.org/html/2607.13649v1#S4`；Limitations/Counterevidence：`Not Disclosed — no dedicated limitations section; simulation/tapeout boundary comes from S4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-13649:end -->

<!-- review:SF-2026-ARXIV-2607-13651:start -->
#### From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring

<!-- claim:SF-2026-ARXIV-2607-13651:start -->Locked EarthNet evaluation does not change general world-model ownership. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13651:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Domain-specific cloud observability forecasting. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13651v1#S5`；Evaluation：`https://arxiv.org/html/2607.13651v1#S7; https://arxiv.org/html/2607.13651v1#S8`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13651v1#S9`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 1 / Durability 1 = **3/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Rejected — Low Durability / Out of Scope`。
<!-- review:SF-2026-ARXIV-2607-13651:end -->

<!-- review:SF-2026-ARXIV-2607-13705:start -->
#### AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities

<!-- claim:SF-2026-ARXIV-2607-13705:start -->Framework and selected runs expose system effects; they do not prove cross-harness semantic equivalence or universal rankings. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13705:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Evaluation identity expands to model × benchmark × harness × environment × scorer with trajectories retained before aggregation. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13705v1#S3`；Evaluation：`https://arxiv.org/html/2607.13705v1#S4; https://arxiv.org/html/2607.13705v1#A1`；Limitations/Counterevidence：`Not Disclosed — no dedicated section; harness sensitivity is evidenced in S4`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L456-L466`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13705:end -->

<!-- review:SF-2026-ARXIV-2607-14178:start -->
#### ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System

<!-- claim:SF-2026-ARXIV-2607-14178:start -->Five generated-paper cases and curated LLM review do not establish autonomous scientific correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14178:end -->

**旧方案与约束变化。** `本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**`（`books/part-07-agent/82-multi-agent.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Applied-mathematics multi-agent workflow with internal verification and retrieval. 它改变 `AGENT-MULTI-AGENT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14178v1#S3; https://arxiv.org/html/2607.14178v1#S4`；Evaluation：`https://arxiv.org/html/2607.14178v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14178v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 2 / Durability 1 = **4/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MULTI-AGENT`。
- Books disposition：`Rejected — Low Durability / Out of Scope`。
<!-- review:SF-2026-ARXIV-2607-14178:end -->

<!-- review:SF-2026-ARXIV-2607-13921:start -->
#### Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code

<!-- claim:SF-2026-ARXIV-2607-13921:start -->Lean formalization and Rust implementation support stated properties; compilation is not task/security correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13921:end -->

**旧方案与约束变化。** `本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**`（`books/part-07-agent/78-tool-calling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Compiler authority moves from final-artifact repair into the partial-generation loop through a sealor that makes prefixes compilable for authoritative diagnostics. 它改变 `AGENT-TOOL-CALLING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://export.arxiv.org/e-print/2607.13921v1 :: Methodology: exact source files sections-new/method.tex and sections-new/rust.tex`；Evaluation：`https://export.arxiv.org/e-print/2607.13921v1 :: Experiments: exact source files sections-new/eval.tex and sections-new/appendix/app_experimental_details.tex`；Limitations/Counterevidence：`https://export.arxiv.org/e-print/2607.13921v1 :: Scope and Limitations: exact source file sections-new/discussion.tex; compiler success is not functional/security correctness`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-TOOL-CALLING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13921:end -->

<!-- review:SF-2026-ARXIV-2607-13926:start -->
#### S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving

<!-- claim:SF-2026-ARXIV-2607-13926:start -->NAVSIM SFT results support the branch; one driving benchmark does not prove universal spatial collapse or safety. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13926:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A spatial stream bypasses the language bottleneck and is fused with semantic intent only at the planning adapter. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13926v1#S2.SS1; https://arxiv.org/html/2607.13926v1#S2.SS2; https://arxiv.org/html/2607.13926v1#S2.SS3`；Evaluation：`https://arxiv.org/html/2607.13926v1#S3; https://arxiv.org/html/2607.13926v1#S4.SS3`；Limitations/Counterevidence：`Not Disclosed — no dedicated limitations section; https://arxiv.org/html/2607.13926v1#S5 scopes the conclusion`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-13926:end -->

<!-- review:SF-2026-ARXIV-2607-14005:start -->
#### M4World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming

<!-- claim:SF-2026-ARXIV-2607-14005:start -->Author generation and VLM-judge results do not prove a causally correct closed-loop simulator. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14005:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Bidirectional video prior becomes a causal few-step student trained on self-generated histories with latent refresh, while object identity is conditioned across views and LiDAR. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14005v1#S3; https://arxiv.org/html/2607.14005v1#S4.SS2; https://arxiv.org/html/2607.14005v1#S4.SS3`；Evaluation：`https://arxiv.org/html/2607.14005v1#S8; https://arxiv.org/html/2607.14005v1#S9`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14005v1#S10 — closed-loop policy interaction remains future work`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-14005:end -->

<!-- review:SF-2026-ARXIV-2607-14076:start -->
#### From Pixels to States: Rethinking Interactive World Models as Game Engines

<!-- claim:SF-2026-ARXIV-2607-14076:start -->Survey taxonomy and 90-hour data-engine description, not a controlled model result. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14076:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Interactive world is organized as action → authoritative game state → observation with separate control and consequence timing. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14076v1#S3`；Evaluation：`https://arxiv.org/html/2607.14076v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14076v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1037-L1046`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-14076:end -->

<!-- review:SF-2026-ARXIV-2607-14236:start -->
#### Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

<!-- claim:SF-2026-ARXIV-2607-14236:start -->Three Flexiv tasks and ablations support contact-reactive post-training; they do not establish cross-robot safety or eliminate human DAgger. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14236:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A slow cached vision-language prefix is separated from a fast force-conditioned causal action stream, allowing within-chunk contact correction while preserving the original policy at initialization. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14236v1#S3.SS1; https://arxiv.org/html/2607.14236v1#S3.SS2; https://arxiv.org/html/2607.14236v1#A2; https://arxiv.org/html/2607.14236v1#A3`；Evaluation：`https://arxiv.org/html/2607.14236v1#S4; https://arxiv.org/html/2607.14236v1#A7; https://arxiv.org/html/2607.14236v1#A8`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14236v1#S6; https://arxiv.org/html/2607.14236v1#A10; https://arxiv.org/html/2607.14236v1#A11`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14236:end -->

<!-- review:SF-2026-ARXIV-2607-14280:start -->
#### DiMaS: Distribution Matching for Steering Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14280:start -->Two VLA/LIBERO families support the branch; transfer weakens with task dissimilarity and success trades against steering magnitude. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14280:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Behavior can be linearly decodable yet not linearly steerable; DiMaS learns a gated distribution transport with interpolation rather than a fixed activation direction. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/method.tex`；Evaluation：`https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/experiments.tex; https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/ablation.tex; https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/appendix.tex`；Limitations/Counterevidence：`https://export.arxiv.org/e-print/2607.14280v1 :: eccv2026_files/conclusion.tex; transfer and steering-layer sensitivity in appendix.tex`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-14280:end -->

<!-- review:SF-2026-ARXIV-2607-14396:start -->
#### CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models

<!-- claim:SF-2026-ARXIV-2607-14396:start -->Internal catalog gains do not prove self-learning correctness or portable memory contracts. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14396:end -->

**旧方案与约束变化。** `本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**`（`books/part-07-agent/84-agent-platform.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Domain-specific supervisor arbitration and context summarization for catalog workers. 它改变 `AGENT-PLATFORM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14396v1#S2`；Evaluation：`https://arxiv.org/html/2607.14396v1#S3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14396v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 2 / Durability 1 = **4/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-PLATFORM`。
- Books disposition：`Rejected — Low Durability / Out of Scope`。
<!-- review:SF-2026-ARXIV-2607-14396:end -->

<!-- review:SF-2026-ARXIV-2607-14431:start -->
#### Smarter and Cheaper at Once: Byte-Exact KV-State Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel

<!-- claim:SF-2026-ARXIV-2607-14431:start -->Author-only own-position exactness and selected AIME/cost cases; recurrence is not new reasoning and no position-independent graft is proven. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14431:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Verified KV state is proposed as a model/runtime/position-bound artifact, distinct from weight updates or ordinary prefix cache. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.14431v1#S3.SS2; https://arxiv.org/html/2607.14431v1#S3.SS3; https://arxiv.org/html/2607.14431v1#S3.SS4`；Evaluation：`https://arxiv.org/html/2607.14431v1#S4.SS1; https://arxiv.org/html/2607.14431v1#S4.SS5; https://arxiv.org/html/2607.14431v1#S4.SS7; https://arxiv.org/html/2607.14431v1#S4.SS13`；Limitations/Counterevidence：`https://arxiv.org/html/2607.14431v1#S5.SS3; https://arxiv.org/html/2607.14431v1#S5.SS4`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1057-L1066`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-14431:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13399 | seven mathematical reasoning benchmarks | paper-disclosed Qwen-family student/teacher and GRPO checkpoints | Not Disclosed | Not Disclosed | benchmark-dependent prompts | reasoning length measured; caps table-scoped | training configuration table-scoped | Not Disclosed | none | author evaluation with verifiable answers |
| SF-2026-ARXIV-2607-13410 | CARLA Town03 urban and Town04 highway driving | DynaDreamer versus paper baselines | single RTX 6000 Ada for training | Not Disclosed | 128x128 BEV with K-step ego context | 500-step episode maximum | paper training configuration | Not Disclosed | 10 Hz simulator; no production SLO | success, driving quality and world-model metrics; 17 training and 2 held-out chassis |
| SF-2026-ARXIV-2607-13429 | LIBERO-PRO, LIBERO-Plus, CALVIN and physical xArm7 tasks | VLA-Adapter and OpenVLA-OFT families plus listed baselines | DeltaAI H200 for simulation training; xArm7 real robot; exact per-run topology in appendix | Not Disclosed | robot observations plus language instruction | fixed-horizon 7-DoF action chunks | paper configuration | Not Disclosed | none | simulation success and real-robot autonomous success |
| SF-2026-ARXIV-2607-13511 | matrix reconstruction and Qwen3.5-4B WikiText-2 perplexity | Gemma-4-E2B, Qwen3.5-4B, Granite-4.0-h-tiny matrices | single AMD MI50 32GB | ternary factors plus real scales; bf16 and Q4/Q5 references | 580 WikiText-2 chunks for full conversion | Not Disclosed | Not Disclosed | Not Disclosed | none; no fused-kernel latency | Frobenius/importance-weighted energy and llama-perplexity |
| SF-2026-ARXIV-2607-14169 | synthesized code world models in perfect/imperfect-information games | paper-disclosed LLM synthesis sweep | pure-Python MCTS; no hardware claim | Not Disclosed | game specifications and transition samples | generated code and arena rollouts | per-game seeds/samples | Not Disclosed | none | author instruments and formal certificates |
| SF-2026-ARXIV-2607-13649 | modeled LLM inference | 1B-13B table-scoped | modeled CIMERA versus H100 reference | variable weight bits | 1024/2048 contexts | Not Disclosed | Not Disclosed | Not Disclosed | none | authors; RTL/system simulation |
| SF-2026-ARXIV-2607-13705 | 20+ agent benchmarks; eight representative runs | paper-listed public/proprietary models | local/Docker/distributed backends; no single contract | provider specific | benchmark specific | full trajectories persisted | async dispatch | framework configured | latency recorded; no production SLO | benchmark scorers plus analyzers |
| SF-2026-ARXIV-2607-13921 | C-to-Rust and changed-API Rust repositories | seven coding models | dual AMD EPYC 9655 verifier; model hardware external | provider specific | 20 CRUST-derived and 30 API-upgrade projects | 20K/30K token caps | two samples per model-task | Not Disclosed | 600-second timeout | rustc plus unit tests |
| SF-2026-ARXIV-2607-13926 | NAVSIM closed-loop planning | InternVL3-2B based S-squared-VLA | 4 A100 GPUs | Not Disclosed | front view, navigation command, ego history | trajectory | 16 | Not Disclosed | none | PDMS with collision/drivable-area/progress/TTC/comfort |
| SF-2026-ARXIV-2607-14005 | six-view plus LiDAR driving generation and 60-second streaming | M4World versus MagicDriveV2 | 8 A100 GPUs | Not Disclosed | multi-view/control history | 10s quality clips and 60s rollouts | Not Disclosed | six views plus LiDAR | 0.7/2.3/7 FPS by resolution; no tail SLO | FID/FVD, VLM judge and downstream recall |
| SF-2026-ARXIV-2607-14076 | survey and Black Myth data-engine description | none | none | Not Disclosed | 90+ hours described gameplay | streaming rollouts discussed | Not Disclosed | Not Disclosed | conceptual latency split | no controlled comparator |
| SF-2026-ARXIV-2607-14236 | towel folding, book insertion, Hanoi ring placement | pi0.5-derived LIFT variants | Flexiv Rizon 4S with 6D force sensor; training on one 8xA800 node | Not Disclosed | cached vision-language prefix plus recent force memory | causally refreshed action chunk | offline plus DAgger sample counts per task | Not Disclosed | robot action budget discussed; exact tail SLO Not Disclosed | 10 autonomous rollouts per checkpoint and ablations |
| SF-2026-ARXIV-2607-14280 | LIBERO behavior steering | SmolVLA and pi0.5 | V100/A100/H100; 0.62ms mean intervention-step overhead reported | Not Disclosed | robot observation and flow-matching representations | action chunks | paper evaluation suites | Not Disclosed | approximately 50ms action budget; no tail SLO | feature distribution shift plus task success |
| SF-2026-ARXIV-2607-14431 | AIME recurrence and held-out transfer | frozen Gemma-4-12B/31B | Blackwell and Hopper cases | pinned deterministic configuration; details partly closed | 32768 serving context; larger external store claimed | 61 tokens for eight recurring tasks | single-task measurements | Not Disclosed | no tail SLO | author hashes, scoring and closed components |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13399 | score_7_9;potential_books_delta | not_selected | — | — | Complete Deep Review and a durable Books delta are present, but the three selected units have broader cross-layer control or evaluation impact. | analysis-decision:SF-2026-ARXIV-2607-13399 |
| SF-2026-ARXIV-2607-13410 | score_7_9;potential_books_delta | not_selected | — | — | The deterministic ego-motion factorization is durable and queued for Books, but its evidence is simulator-bounded and less cross-cutting than the selected world-model evaluation unit. | analysis-decision:SF-2026-ARXIV-2607-13410 |
| SF-2026-ARXIV-2607-13429 | forced_review;potential_books_delta | not_selected | — | — | Exact-v1 evidence confirms a durable representation-preservation and language-action alignment gap, so the knowledge-gap override upgrades the review to Deep; the selected physical-control unit remains more cross-layer and non-overlapping. | analysis-decision:SF-2026-ARXIV-2607-13429 |
| SF-2026-ARXIV-2607-14169 | score_7_9;potential_books_delta | selected | DA-20260716-02 | — | V2=8/9；Formal witnesses and selected games show a verified transition model can still lose; not a universal learned-video bound.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260716-02 |
| SF-2026-ARXIV-2607-13705 | score_7_9;potential_books_delta | not_selected | — | — | The component-identity contract is a durable Books delta, but the selected compiler and physical-control units add more distinct control-authority transitions while DA-02 already covers evaluation correctness. | analysis-decision:SF-2026-ARXIV-2607-13705 |
| SF-2026-ARXIV-2607-13921 | score_7_9;potential_books_delta | selected | DA-20260716-01 | — | V2=9/9；Lean formalization and Rust implementation support stated properties; compilation is not task/security correctness.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260716-01 |
| SF-2026-ARXIV-2607-14236 | score_7_9;potential_books_delta | selected | DA-20260716-03 | — | V2=8/9；Three Flexiv tasks and ablations support contact-reactive post-training; they do not establish cross-robot safety or eliminate human DAgger.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260716-03 |
| SF-2026-ARXIV-2607-14431 | score_7_9;potential_books_delta | not_selected | — | — | The byte-exact own-position result is technically notable, but the proprietary engine and closed workload prevent a durable Books mechanism claim; it remains Weekly Only. | analysis-decision:SF-2026-ARXIV-2607-14431 |

<!-- analysis:DA-20260716-01:start -->
### Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code

**旧方案为何合理。** Post-generation repair is portable and constrained decoding is strong for tractable grammars.（现有命题定位：`books/part-07-agent/78-tool-calling.md#L14-L14`）

**约束变化与机制。** Compiler authority moves from final-artifact repair into the partial-generation loop through a sealor that makes prefixes compilable for authoritative diagnostics. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `AGENT-TOOL-CALLING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Earlier diagnosis adds compiler calls, language-specific sealing and rollback state; future definitions create heavy-tail detection.

<!-- analysis:DA-20260716-01:end -->

<!-- analysis:DA-20260716-02:start -->
### When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models

**旧方案为何合理。** Sampled transition tests remain cheap when sample and planner visitation align.（现有命题定位：`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）

**约束变化与机制。** Transition accuracy must evolve to planner-induced coverage, play adequacy and separate belief/inference validation. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-WORLD-MODELS` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Certificates are strong but enumeration does not scale; sampling misses rare decisive states and repair data can corrupt synthesis.

<!-- analysis:DA-20260716-02:end -->

<!-- analysis:DA-20260716-03:start -->
### Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

**旧方案为何合理。** Vision-only action chunks are efficient when contact is visible/predictable and re-planning latency fits the control budget.（现有命题定位：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）

**约束变化与机制。** A slow cached vision-language prefix is separated from a fast force-conditioned causal action stream, allowing within-chunk contact correction while preserving the original policy at initialization. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-EMBODIED-VLA` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Force memory and online corrections improve contact response but add sensor calibration, causal masking, repeated action-expert inference and human correction load; transient force can mislead a single-frame baseline.

<!-- analysis:DA-20260716-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13399:start -->《Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations》已完成 Deep Source Review。Complete Deep Review and a durable Books delta are present, but the three selected units have broader cross-layer control or evaluation impact.<!-- analysis-decision:SF-2026-ARXIV-2607-13399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13410:start -->《Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation》已完成 Deep Source Review。The deterministic ego-motion factorization is durable and queued for Books, but its evidence is simulator-bounded and less cross-cutting than the selected world-model evaluation unit.<!-- analysis-decision:SF-2026-ARXIV-2607-13410:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13429:start -->《Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment》已完成 Deep Source Review。Exact-v1 evidence confirms a durable representation-preservation and language-action alignment gap, so the knowledge-gap override upgrades the review to Deep; the selected physical-control unit remains more cross-layer and non-overlapping.<!-- analysis-decision:SF-2026-ARXIV-2607-13429:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13705:start -->《AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities》已完成 Deep Source Review。The component-identity contract is a durable Books delta, but the selected compiler and physical-control units add more distinct control-authority transitions while DA-02 already covers evaluation correctness.<!-- analysis-decision:SF-2026-ARXIV-2607-13705:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14431:start -->《Smarter and Cheaper at Once: Byte-Exact KV-State Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel》已完成 Deep Source Review。The byte-exact own-position result is technically notable, but the proprietary engine and closed workload prevent a durable Books mechanism claim; it remains Weekly Only.<!-- analysis-decision:SF-2026-ARXIV-2607-14431:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13399 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-13399 | delta:SF-2026-ARXIV-2607-13399 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13399 |
| SF-2026-ARXIV-2607-13410 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-13410 | delta:SF-2026-ARXIV-2607-13410 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13410 |
| SF-2026-ARXIV-2607-13429 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-13429 | delta:SF-2026-ARXIV-2607-13429 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13429 |
| SF-2026-ARXIV-2607-13511 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-13511 | delta:SF-2026-ARXIV-2607-13511 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13511 |
| SF-2026-ARXIV-2607-14169 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-14169 | delta:SF-2026-ARXIV-2607-14169 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14169 |
| SF-2026-ARXIV-2607-13649 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-13649 | delta:SF-2026-ARXIV-2607-13649 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13649 |
| SF-2026-ARXIV-2607-13705 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-13705 | delta:SF-2026-ARXIV-2607-13705 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13705 |
| SF-2026-ARXIV-2607-13921 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/77-memory.md#L14-L14; books/part-07-agent/79-planning.md#L14-L14 | existing:SF-2026-ARXIV-2607-13921 | delta:SF-2026-ARXIV-2607-13921 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13921 |
| SF-2026-ARXIV-2607-13926 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-13926 | delta:SF-2026-ARXIV-2607-13926 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13926 |
| SF-2026-ARXIV-2607-14005 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-14005 | delta:SF-2026-ARXIV-2607-14005 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14005 |
| SF-2026-ARXIV-2607-14076 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-14076 | delta:SF-2026-ARXIV-2607-14076 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14076 |
| SF-2026-ARXIV-2607-14236 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14236 | delta:SF-2026-ARXIV-2607-14236 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14236 |
| SF-2026-ARXIV-2607-14280 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14280 | delta:SF-2026-ARXIV-2607-14280 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-14280 |

<!-- books-review:SF-2026-ARXIV-2607-13399:start --><!-- existing:SF-2026-ARXIV-2607-13399:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-13399:end --><!-- delta:SF-2026-ARXIV-2607-13399:start -->新增证据边界：OPD is an exploration catalyst on student-owned on-policy states, not a capacity creator; teacher/student mismatch and length aggregation can corrupt the guidance signal. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13399:end --><!-- books-review:SF-2026-ARXIV-2607-13399:end -->

<!-- books-review:SF-2026-ARXIV-2607-13410:start --><!-- existing:SF-2026-ARXIV-2607-13410:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-13410:end --><!-- delta:SF-2026-ARXIV-2607-13410:start -->新增证据边界：Known ego motion is factored out of egocentric observation transition and propagated as an identifiable context, leaving the learned world model to spend capacity on residual scene dynamics. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13410:end --><!-- books-review:SF-2026-ARXIV-2607-13410:end -->

<!-- books-review:SF-2026-ARXIV-2607-13429:start --><!-- existing:SF-2026-ARXIV-2607-13429:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-13429:end --><!-- delta:SF-2026-ARXIV-2607-13429:start -->新增证据边界：VLA fine-tuning is split into action learning, frozen-teacher representation anchoring and same-observation language-action alignment, avoiding the false choice between preserving semantic priors and learning control. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13429:end --><!-- books-review:SF-2026-ARXIV-2607-13429:end -->

<!-- books-review:SF-2026-ARXIV-2607-13511:start --><!-- existing:SF-2026-ARXIV-2607-13511:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-13511:end --><!-- delta:SF-2026-ARXIV-2607-13511:start -->新增证据边界：Expanded-rank ternary factors turn inner-rank multiplier and sparsity threshold into continuous accuracy/storage dials; monotone residual reduction is a representation result, not executable speed evidence. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-13511:end --><!-- books-review:SF-2026-ARXIV-2607-13511:end -->

<!-- books-review:SF-2026-ARXIV-2607-14169:start --><!-- existing:SF-2026-ARXIV-2607-14169:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-14169:end --><!-- delta:SF-2026-ARXIV-2607-14169:start -->新增证据边界：Transition accuracy must evolve to planner-induced coverage, play adequacy and separate belief/inference validation. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14169:end --><!-- books-review:SF-2026-ARXIV-2607-14169:end -->

<!-- books-review:SF-2026-ARXIV-2607-13649:start --><!-- existing:SF-2026-ARXIV-2607-13649:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-13649:end --><!-- delta:SF-2026-ARXIV-2607-13649:start -->新增证据边界：Precision becomes a compiler/runtime execution-plan dimension mapped to reconfigurable compute-in-memory/interconnect hardware. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-13649:end --><!-- books-review:SF-2026-ARXIV-2607-13649:end -->

<!-- books-review:SF-2026-ARXIV-2607-13705:start --><!-- existing:SF-2026-ARXIV-2607-13705:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-13705:end --><!-- delta:SF-2026-ARXIV-2607-13705:start -->新增证据边界：Evaluation identity expands to model × benchmark × harness × environment × scorer with trajectories retained before aggregation. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13705:end --><!-- books-review:SF-2026-ARXIV-2607-13705:end -->

<!-- books-review:SF-2026-ARXIV-2607-13921:start --><!-- existing:SF-2026-ARXIV-2607-13921:start -->对读 `books/part-07-agent/78-tool-calling.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/78-tool-calling.md#L14-L14`）为：本章的核心判断是：**模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。**<!-- existing:SF-2026-ARXIV-2607-13921:end --><!-- delta:SF-2026-ARXIV-2607-13921:start -->新增证据边界：Compiler authority moves from final-artifact repair into the partial-generation loop through a sealor that makes prefixes compilable for authoritative diagnostics. 该 delta 已进入 `books/part-07-agent/78-tool-calling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13921:end --><!-- books-review:SF-2026-ARXIV-2607-13921:end -->

<!-- books-review:SF-2026-ARXIV-2607-13926:start --><!-- existing:SF-2026-ARXIV-2607-13926:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-13926:end --><!-- delta:SF-2026-ARXIV-2607-13926:start -->新增证据边界：A spatial stream bypasses the language bottleneck and is fused with semantic intent only at the planning adapter. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-13926:end --><!-- books-review:SF-2026-ARXIV-2607-13926:end -->

<!-- books-review:SF-2026-ARXIV-2607-14005:start --><!-- existing:SF-2026-ARXIV-2607-14005:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-14005:end --><!-- delta:SF-2026-ARXIV-2607-14005:start -->新增证据边界：Bidirectional video prior becomes a causal few-step student trained on self-generated histories with latent refresh, while object identity is conditioned across views and LiDAR. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-14005:end --><!-- books-review:SF-2026-ARXIV-2607-14005:end -->

<!-- books-review:SF-2026-ARXIV-2607-14076:start --><!-- existing:SF-2026-ARXIV-2607-14076:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-14076:end --><!-- delta:SF-2026-ARXIV-2607-14076:start -->新增证据边界：Interactive world is organized as action → authoritative game state → observation with separate control and consequence timing. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-14076:end --><!-- books-review:SF-2026-ARXIV-2607-14076:end -->

<!-- books-review:SF-2026-ARXIV-2607-14236:start --><!-- existing:SF-2026-ARXIV-2607-14236:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14236:end --><!-- delta:SF-2026-ARXIV-2607-14236:start -->新增证据边界：A slow cached vision-language prefix is separated from a fast force-conditioned causal action stream, allowing within-chunk contact correction while preserving the original policy at initialization. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14236:end --><!-- books-review:SF-2026-ARXIV-2607-14236:end -->

<!-- books-review:SF-2026-ARXIV-2607-14280:start --><!-- existing:SF-2026-ARXIV-2607-14280:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14280:end --><!-- delta:SF-2026-ARXIV-2607-14280:start -->新增证据边界：Behavior can be linearly decodable yet not linearly steerable; DiMaS learns a gated distribution transport with interpolation rather than a fixed activation direction. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-14280:end --><!-- books-review:SF-2026-ARXIV-2607-14280:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260716-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260716; semantic-review:SA-20260716-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260716-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-13399; review:SF-2026-ARXIV-2607-13410; review:SF-2026-ARXIV-2607-13429; review:SF-2026-ARXIV-2607-13511; review:SF-2026-ARXIV-2607-13605; review:SF-2026-ARXIV-2607-14169; review:SF-2026-ARXIV-2607-13649; review:SF-2026-ARXIV-2607-13651; review:SF-2026-ARXIV-2607-13705; review:SF-2026-ARXIV-2607-14178; review:SF-2026-ARXIV-2607-13921; review:SF-2026-ARXIV-2607-13926; review:SF-2026-ARXIV-2607-14005; review:SF-2026-ARXIV-2607-14076; review:SF-2026-ARXIV-2607-14236; review:SF-2026-ARXIV-2607-14280; review:SF-2026-ARXIV-2607-14396; review:SF-2026-ARXIV-2607-14431; semantic-review:SA-20260716-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260716-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260716-01; analysis:DA-20260716-02; analysis:DA-20260716-03; semantic-review:SA-20260716-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260716-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-13399; books-review:SF-2026-ARXIV-2607-13410; books-review:SF-2026-ARXIV-2607-13429; books-review:SF-2026-ARXIV-2607-13511; books-review:SF-2026-ARXIV-2607-14169; books-review:SF-2026-ARXIV-2607-13649; books-review:SF-2026-ARXIV-2607-13705; books-review:SF-2026-ARXIV-2607-13921; books-review:SF-2026-ARXIV-2607-13926; books-review:SF-2026-ARXIV-2607-14005; books-review:SF-2026-ARXIV-2607-14076; books-review:SF-2026-ARXIV-2607-14236; books-review:SF-2026-ARXIV-2607-14280; review:SF-2026-ARXIV-2607-14431; semantic-review:SA-20260716-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260716-COVERAGE:start -->PASS — 严格北京时间 [2026-07-15 09:00, 2026-07-16 09:00) 分母冻结为 18 个唯一 Source Family；1050 identity 的分页/水位闭合，DataCite 仅用于 identity/date metadata，18/18 first-public 均在窗口内，D15/D17 无 owner 冲突；5 个 GitHub artifact commit 均早于 event-time cutoff。<!-- semantic-review:SA-20260716-COVERAGE:end -->
<!-- semantic-review:SA-20260716-EVIDENCE:start -->PASS — 18/18 均有最终 evidence state：8 Deep、6 Standard、4 Closure，0 Pending/Blocked/Unverified/Disputed；所有 Full/Standard review 均绑定 exact-v1 Method/Evaluation/Limitations 与 claim boundary，Closure 仅承担 identity/date/rejection；18 个 HTML/PDF 与 2 个 exact-v1 source archive 已持久化到仓库且逐项 SHA-256 匹配，packet 与 central ledger 完全一致。2607.13429 以 canonical knowledge_gap override 升 Deep；2607.13921/14280 的 exact source version、file locator、artifact cutoff 与 benchmark contract 均闭合。<!-- semantic-review:SA-20260716-EVIDENCE:end -->
<!-- semantic-review:SA-20260716-SELECTION:start -->PASS — 8 个 Deep-eligible family 均有具名 selected/not-selected decision，3 个 narrative unit 分别覆盖 compiler feedback、planner-consumed world-model adequacy 与 contact-reactive fast loop；未选理由逐项说明相对信息增益与不重叠边界，未用三项 narrative 上限减少 Full Source Review。<!-- semantic-review:SA-20260716-SELECTION:end -->
<!-- semantic-review:SA-20260716-BOOKS:start -->PASS — 18/18 均有唯一 owner/disposition；7 个 Integrate 已分别写入 Ch25、Ch26、Ch33、Ch66、Ch78 的精确机制位置，目标与相邻章节复核无 owner 冲突。正文均保留旧方案合理性、约束变化、状态/控制权、trade-off、failure/coexistence boundary，Review notes 保留 exact-v1 来源与实验边界；6 No Change、1 Weekly Only、4 Rejected 均有可追溯理由。<!-- semantic-review:SA-20260716-BOOKS:end -->

## 8. Ignored Noise

1050 个窗口内 identity 中，1032 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：7 个 `Integrate`，6 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，4 个 `Rejected — Low Durability / Out of Scope`；Deep 8 / Standard 6。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/16/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-04-training-system/33-grpo.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-07-agent/78-tool-calling.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation](https://arxiv.org/abs/2607.13410v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/abs/2607.13429v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level](https://arxiv.org/abs/2607.13511v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](https://arxiv.org/abs/2607.13605v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [When a Verified World Model Still Loses: Play-Adequacy vs Prediction-Accuracy in LLM-Synthesized Code World Models](https://arxiv.org/abs/2607.14169v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [CIMERA: Compute-in-Interconnect and Memory with Reconfigurable Precision for LLM Inference](https://arxiv.org/abs/2607.13649v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring](https://arxiv.org/abs/2607.13651v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System](https://arxiv.org/abs/2607.14178v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code](https://arxiv.org/abs/2607.13921v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2607.13926v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [M4World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming](https://arxiv.org/abs/2607.14005v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection](https://arxiv.org/abs/2607.14236v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/abs/2607.14280v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models](https://arxiv.org/abs/2607.14396v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Smarter and Cheaper at Once: Byte-Exact KV-State Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel](https://arxiv.org/abs/2607.14431v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
