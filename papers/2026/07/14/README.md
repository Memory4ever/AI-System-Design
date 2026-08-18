# Daily Research — 2026-07-14

**Research Date:** 2026-07-14

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-13 09:00:00 ～ 2026-07-14 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1223 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 15 个。当前路由账目为 9 个 Deep、6 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-14 |
| Window End | 2026-07-14 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-14-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T00:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-13T09:00:00+08:00 | 2026-07-14T09:00:00+08:00 | 2026-08-27T00:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1223 | SF-2026-ARXIV-2607-10987<br>SF-2026-ARXIV-2607-11070<br>SF-2026-ARXIV-2607-11079<br>SF-2026-ARXIV-2607-11149<br>SF-2026-ARXIV-2607-11172<br>SF-2026-ARXIV-2607-11183<br>SF-2026-ARXIV-2607-11250<br>SF-2026-ARXIV-2607-11487<br>SF-2026-ARXIV-2607-11498<br>SF-2026-ARXIV-2607-11505<br>SF-2026-ARXIV-2607-11656<br>SF-2026-ARXIV-2607-11673<br>SF-2026-ARXIV-2607-11849<br>SF-2026-ARXIV-2607-11886<br>SF-2026-ARXIV-2607-12227 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-14T09:00:00+08:00 | coverage:SRC-ARXIV:20260714 | GAP-ARXIV-DIRECT-RESET-20260714 |
| SRC-GITHUB-COMMIT | 2026-07-13T09:00:00+08:00 | 2026-07-14T09:00:00+08:00 | 2026-08-27T00:00:00+08:00 | exact GitHub commit API lookups: arupcsedu/AAFLOW@90bb569d67bf2796870ff3dfbddc75e635fd2dcb; deeplearning-wisc/mace@6d8f59d58cb6a670631e51f683602435dbf937d2; KnowledgeXLab/P-OPD@cca5fbca05c5fdb673c63b398b41f44e50821ba8 | checked | 3 | SF-2026-ARXIV-2607-10987; SF-2026-ARXIV-2607-11250; SF-2026-ARXIV-2607-11505 | pages=3; final cursors=90bb569d67bf2796870ff3dfbddc75e635fd2dcb,6d8f59d58cb6a670631e51f683602435dbf937d2,cca5fbca05c5fdb673c63b398b41f44e50821ba8; one bounded commit lookup per family | 2026-07-14T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260714 | — |

<!-- coverage:SRC-ARXIV:20260714:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1223 unique identities in this strict window; 15 routed families.<!-- coverage:SRC-ARXIV:20260714:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260714:start -->repository=arupcsedu/AAFLOW, until=2026-07-14T01:00:00Z, full_sha=90bb569d67bf2796870ff3dfbddc75e635fd2dcb, commit_timestamp=2026-06-14T05:11:27Z, url=https://github.com/arupcsedu/AAFLOW/commit/90bb569d67bf2796870ff3dfbddc75e635fd2dcb; repository=deeplearning-wisc/mace, until=2026-07-14T01:00:00Z, full_sha=6d8f59d58cb6a670631e51f683602435dbf937d2, commit_timestamp=2026-07-11T05:48:09Z, url=https://github.com/deeplearning-wisc/mace/commit/6d8f59d58cb6a670631e51f683602435dbf937d2; repository=KnowledgeXLab/P-OPD, until=2026-07-14T01:00:00Z, full_sha=cca5fbca05c5fdb673c63b398b41f44e50821ba8, commit_timestamp=2026-06-29T09:26:26Z, url=https://github.com/KnowledgeXLab/P-OPD/commit/cca5fbca05c5fdb673c63b398b41f44e50821ba8; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260714:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 15 个 family：exact v1 为 7 个 family 披露 artifact/evidence locator，其中 7 个提供外部 repository/project/demo locator，另有 8 个未披露；本日确认 3 个 family、3 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10987 | arXiv:2607.10987v1 | paper-v1:2607.10987 | 2026-W29 | 2026-07-13 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10987 | self | — | new_in_window | INFER-DYNAMO | Integrate | books-review:SF-2026-ARXIV-2607-10987 | yes |
| SF-2026-ARXIV-2607-11070 | arXiv:2607.11070v1 | paper-v1:2607.11070 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11070 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-11070 | yes |
| SF-2026-ARXIV-2607-11079 | arXiv:2607.11079v1 | paper-v1:2607.11079 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11079 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11079 | yes |
| SF-2026-ARXIV-2607-11149 | arXiv:2607.11149v1 | paper-v1:2607.11149 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11149 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2607-11149 | yes |
| SF-2026-ARXIV-2607-11172 | arXiv:2607.11172v1 | paper-v1:2607.11172 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11172 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-11172 | yes |
| SF-2026-ARXIV-2607-11183 | arXiv:2607.11183v1 | paper-v1:2607.11183 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11183 | self | — | new_in_window | MODEL-FFN | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2607-11250 | arXiv:2607.11250v1 | paper-v1:2607.11250 | 2026-W29 | 2026-07-13 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11250 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2607-11250 | yes |
| SF-2026-ARXIV-2607-11487 | arXiv:2607.11487v1 | paper-v1:2607.11487 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11487 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11487 | yes |
| SF-2026-ARXIV-2607-11498 | arXiv:2607.11498v1 | paper-v1:2607.11498 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11498 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-11498 | yes |
| SF-2026-ARXIV-2607-11505 | arXiv:2607.11505v1 | paper-v1:2607.11505 | 2026-W29 | 2026-07-13 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11505 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-11505 | yes |
| SF-2026-ARXIV-2607-11656 | arXiv:2607.11656v1 | paper-v1:2607.11656 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11656 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11656 | yes |
| SF-2026-ARXIV-2607-11673 | arXiv:2607.11673v1 | paper-v1:2607.11673 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11673 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11673 | yes |
| SF-2026-ARXIV-2607-11849 | arXiv:2607.11849v1 | paper-v1:2607.11849 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11849 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11849 | yes |
| SF-2026-ARXIV-2607-11886 | arXiv:2607.11886v1 | paper-v1:2607.11886 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11886 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-11886 | yes |
| SF-2026-ARXIV-2607-12227 | arXiv:2607.12227v1 | paper-v1:2607.12227 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12227 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12227 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10987 | RP-2a736c87fa9cd860 | deep | arXiv:2607.10987v1 | SRC-ARXIV@arXiv:2607.10987v1; SRC-GITHUB-COMMIT@commit:90bb569d67bf2796870ff3dfbddc75e635fd2dcb | https://arxiv.org/html/2607.10987v1#S3; https://arxiv.org/html/2607.10987v1#S4; https://arxiv.org/html/2607.10987v1#S5 | https://arxiv.org/html/2607.10987v1#S6; https://arxiv.org/html/2607.10987v1#S6.SS1 | https://arxiv.org/html/2607.10987v1#S8 | https://github.com/arupcsedu/AAFLOW/commit/90bb569d67bf2796870ff3dfbddc75e635fd2dcb (event-time base artifact; paper-specific AAFLOW+ parity not established) | claim:SF-2026-ARXIV-2607-10987 | complete |
| SF-2026-ARXIV-2607-11070 | RP-1cc14c941147121b | deep | arXiv:2607.11070v1 | SRC-ARXIV@arXiv:2607.11070v1 | https://arxiv.org/html/2607.11070v1#S4; https://arxiv.org/html/2607.11070v1#S4.SS1; https://arxiv.org/html/2607.11070v1#S4.SS2 | https://arxiv.org/html/2607.11070v1#S5; https://arxiv.org/html/2607.11070v1#S5.SS1; https://arxiv.org/html/2607.11070v1#S5.SS2 | https://arxiv.org/html/2607.11070v1#S6 | Not Disclosed — No paper-specific public repository disclosed in exact v1. | claim:SF-2026-ARXIV-2607-11070 | complete |
| SF-2026-ARXIV-2607-11079 | RP-969ad9f41589b2ab | standard | arXiv:2607.11079v1 | SRC-ARXIV@arXiv:2607.11079v1 | https://arxiv.org/html/2607.11079v1#S3; https://arxiv.org/html/2607.11079v1#S3.SS1; https://arxiv.org/html/2607.11079v1#S3.SS4 | https://arxiv.org/html/2607.11079v1#S4; https://arxiv.org/html/2607.11079v1#S4.SS1; https://arxiv.org/html/2607.11079v1#S4.SS3 | https://arxiv.org/html/2607.11079v1#S5 | Not Disclosed — No paper-specific public artifact URL disclosed in exact v1. | claim:SF-2026-ARXIV-2607-11079 | complete |
| SF-2026-ARXIV-2607-11149 | RP-d3ef90faaa4a270d | deep | arXiv:2607.11149v1 | SRC-ARXIV@arXiv:2607.11149v1 | https://arxiv.org/html/2607.11149v1#S3; https://arxiv.org/html/2607.11149v1#S3.SS1; https://arxiv.org/html/2607.11149v1#S4 | https://arxiv.org/html/2607.11149v1#S5; https://arxiv.org/html/2607.11149v1#S5.SS1; https://arxiv.org/html/2607.11149v1#S5.SS6 | https://arxiv.org/html/2607.11149v1#S8; https://arxiv.org/html/2607.11149v1#S9 | Not Disclosed — Paper states adapter/compactor ships with artifact, but exact v1 exposes no uniquely verifiable public repository; retain artifact scope as not independently verified. | claim:SF-2026-ARXIV-2607-11149 | complete |
| SF-2026-ARXIV-2607-11172 | RP-c5653332e8ade065 | deep | arXiv:2607.11172v1 | SRC-ARXIV@arXiv:2607.11172v1 | https://arxiv.org/html/2607.11172v1#S2; https://arxiv.org/html/2607.11172v1#S2.SS1; https://arxiv.org/html/2607.11172v1#S2.SS4 | https://arxiv.org/html/2607.11172v1#S3; https://arxiv.org/html/2607.11172v1#S3.SS1; https://arxiv.org/html/2607.11172v1#S3.SS4 | https://arxiv.org/html/2607.11172v1#S6 | Not Disclosed — No public paper-specific repository disclosed in exact v1. | claim:SF-2026-ARXIV-2607-11172 | complete |
| SF-2026-ARXIV-2607-11183 | RP-374863a822fd5805 | standard | arXiv:2607.11183v1 | SRC-ARXIV@arXiv:2607.11183v1 | arXiv:2607.11183v1 PDF p.5 §3.4 AG as the conservative successor; arXiv:2607.11183v1 PDF p.6 §3.5 FFN computation; arXiv:2607.11183v1 PDF p.7 §3.6-§3.7 intervention points and taxonomy; arXiv:2607.11183v1 PDF p.10 §3.8 gate and fallback | arXiv:2607.11183v1 PDF p.10 §4 Experiment Design; arXiv:2607.11183v1 PDF §5 Experiment Results; arXiv:2607.11183v1 PDF §6 Analysis | arXiv:2607.11183v1 PDF p.26 §8 Limitations; arXiv:2607.11183v1 PDF p.26-27 §9 Future Work | Not Disclosed — No uniquely verifiable public artifact disclosed in exact v1 PDF. | claim:SF-2026-ARXIV-2607-11183 | complete |
| SF-2026-ARXIV-2607-11250 | RP-40f7e344324ea3dc | deep | arXiv:2607.11250v1 | SRC-ARXIV@arXiv:2607.11250v1; SRC-GITHUB-COMMIT@commit:6d8f59d58cb6a670631e51f683602435dbf937d2 | https://arxiv.org/html/2607.11250v1#S3; https://arxiv.org/html/2607.11250v1#S3.SS1; https://arxiv.org/html/2607.11250v1#S3.SS2 | https://arxiv.org/html/2607.11250v1#S5; https://arxiv.org/html/2607.11250v1#S5.SS1; https://arxiv.org/html/2607.11250v1#S5.SS3 | https://arxiv.org/html/2607.11250v1#A6 | https://github.com/deeplearning-wisc/mace/commit/6d8f59d58cb6a670631e51f683602435dbf937d2 (event-time artifact) | claim:SF-2026-ARXIV-2607-11250 | complete |
| SF-2026-ARXIV-2607-11487 | RP-944ceb31f49c4995 | standard | arXiv:2607.11487v1 | SRC-ARXIV@arXiv:2607.11487v1 | https://arxiv.org/html/2607.11487v1#S3; https://arxiv.org/html/2607.11487v1#S3.SS1; https://arxiv.org/html/2607.11487v1#S3.SS5 | https://arxiv.org/html/2607.11487v1#S5; https://arxiv.org/html/2607.11487v1#S5.SS1; https://arxiv.org/html/2607.11487v1#S5.SS5 | https://arxiv.org/html/2607.11487v1#S6; https://arxiv.org/html/2607.11487v1#Sx1; https://arxiv.org/html/2607.11487v1#Sx2 | Not Required — repository commit was not reviewed with an event-time artifact receipt and is not part of the technical claim | claim:SF-2026-ARXIV-2607-11487 | complete |
| SF-2026-ARXIV-2607-11498 | RP-2a6f0df34fed0602 | deep | arXiv:2607.11498v1 | SRC-ARXIV@arXiv:2607.11498v1 | https://arxiv.org/html/2607.11498v1#S3; https://arxiv.org/html/2607.11498v1#S4.SS1; https://arxiv.org/html/2607.11498v1#S4.SS3 | https://arxiv.org/html/2607.11498v1#S5; https://arxiv.org/html/2607.11498v1#S5.SS1; https://arxiv.org/html/2607.11498v1#S5.SS2 | https://arxiv.org/html/2607.11498v1#S6 | https://davian-robotics.github.io/pointmap/ (paper project page; no event-time code commit exposed in exact v1) | claim:SF-2026-ARXIV-2607-11498 | complete |
| SF-2026-ARXIV-2607-11505 | RP-c1c5b3448c898e8d | deep | arXiv:2607.11505v1 | SRC-ARXIV@arXiv:2607.11505v1; SRC-GITHUB-COMMIT@commit:cca5fbca05c5fdb673c63b398b41f44e50821ba8 | https://arxiv.org/html/2607.11505v1#S3; https://arxiv.org/html/2607.11505v1#S3.SS2; https://arxiv.org/html/2607.11505v1#S3.SS4 | https://arxiv.org/html/2607.11505v1#S4; https://arxiv.org/html/2607.11505v1#S4.SS1; https://arxiv.org/html/2607.11505v1#S4.SS5 | https://arxiv.org/html/2607.11505v1#S6 | https://github.com/KnowledgeXLab/P-OPD/commit/cca5fbca05c5fdb673c63b398b41f44e50821ba8 (URL redirects from PUST; event-time commit); https://huggingface.co/KnowledgeXLab/PUST-Experiments | claim:SF-2026-ARXIV-2607-11505 | complete |
| SF-2026-ARXIV-2607-11656 | RP-3fa528cef0f0c393 | standard | arXiv:2607.11656v1 | SRC-ARXIV@arXiv:2607.11656v1 | https://arxiv.org/html/2607.11656v1#S4; https://arxiv.org/html/2607.11656v1#S4.SS2; https://arxiv.org/html/2607.11656v1#S4.SS4; https://arxiv.org/html/2607.11656v1#S4.SS5 | https://arxiv.org/html/2607.11656v1#S2; https://arxiv.org/html/2607.11656v1#S5 | https://arxiv.org/html/2607.11656v1#S3 | Not Required — repository commit was not reviewed with an event-time artifact receipt and is not part of the technical claim | claim:SF-2026-ARXIV-2607-11656 | complete |
| SF-2026-ARXIV-2607-11673 | RP-4649e6c5674329c0 | standard | arXiv:2607.11673v1 | SRC-ARXIV@arXiv:2607.11673v1 | https://arxiv.org/html/2607.11673v1#S2; https://arxiv.org/html/2607.11673v1#S3; https://arxiv.org/html/2607.11673v1#S3.SS3; https://arxiv.org/html/2607.11673v1#S3.SS6 | https://arxiv.org/html/2607.11673v1#S4; https://arxiv.org/html/2607.11673v1#S4.SS2; https://arxiv.org/html/2607.11673v1#S4.SS5 | No dedicated Limitations section in exact v1; counter-boundary derived conservatively from arXiv:2607.11673v1#S3 and #S4, not from an author limitation claim. | https://abot-world.amap.com/plaza (system/demo endpoint); exact v1 does not expose a paper-specific event-time code repository. | claim:SF-2026-ARXIV-2607-11673 | complete |
| SF-2026-ARXIV-2607-11849 | RP-d8c32be56f7a4ca9 | standard | arXiv:2607.11849v1 | SRC-ARXIV@arXiv:2607.11849v1 | https://arxiv.org/html/2607.11849v1#S3; https://arxiv.org/html/2607.11849v1#S3.SS1; https://arxiv.org/html/2607.11849v1#S4; https://arxiv.org/html/2607.11849v1#S4.SS4 | https://arxiv.org/html/2607.11849v1#S5; https://arxiv.org/html/2607.11849v1#S5.SS1; https://arxiv.org/html/2607.11849v1#S5.SS4 | No dedicated Limitations section in exact v1; annotation scope and benchmark boundary are localized in arXiv:2607.11849v1#S3 and Appendix A/C. | Not Disclosed — No uniquely identified public code/data repository disclosed in exact v1. | claim:SF-2026-ARXIV-2607-11849 | complete |
| SF-2026-ARXIV-2607-11886 | RP-6d511f022bc69d33 | deep | arXiv:2607.11886v1 | SRC-ARXIV@arXiv:2607.11886v1 | https://arxiv.org/html/2607.11886v1#S3; https://arxiv.org/html/2607.11886v1#S3.SS1; https://arxiv.org/html/2607.11886v1#S3.SS2 | https://arxiv.org/html/2607.11886v1#S4; https://arxiv.org/html/2607.11886v1#S4.SS1; https://arxiv.org/html/2607.11886v1#S4.SS4 | https://arxiv.org/html/2607.11886v1#A1 | https://huangrh99.github.io/SpectraReward/ (paper project page; no uniquely verified event-time code commit exposed) | claim:SF-2026-ARXIV-2607-11886 | complete |
| SF-2026-ARXIV-2607-12227 | RP-781653b9e59f81cb | deep | arXiv:2607.12227v1 | SRC-ARXIV@arXiv:2607.12227v1 | https://arxiv.org/html/2607.12227v1#S3; https://arxiv.org/html/2607.12227v1#S3.SS2; https://arxiv.org/html/2607.12227v1#S3.SS5 | https://arxiv.org/html/2607.12227v1#S4; https://arxiv.org/html/2607.12227v1#S4.SS1; https://arxiv.org/html/2607.12227v1#S4.SS4 | https://arxiv.org/html/2607.12227v1#S5; https://arxiv.org/html/2607.12227v1#S5.SS2 | https://github.com/rethinking-harness-evolution (organization disclosed by paper; exact event-time repository/commit identity not uniquely specified) | claim:SF-2026-ARXIV-2607-12227 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-10987:start -->
#### [AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows

<!-- claim:SF-2026-ARXIV-2607-10987:start -->Supports typed distributed KV-state orchestration under shared-prefix synthetic workflows; does not prove arbitrary cross-model state compatibility, production fault tolerance, persistence, or end-to-end agent quality. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10987:end -->

**旧方案与约束变化。** `本章的核心判断是：**Dynamo 位于 inference engine 之上，通过 request path、control path 和 KV state path 协调多个 worker pools；它优化的是分布式能力交付系统，而不是替代底层模型执行引擎。**`（`books/part-05-inference-system/52-dynamo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Stateful operator tuple and graph separate data edges from KV-state edges; compatibility identity, fork/compose/transfer/evict/recompute policies make cache movement an explicit orchestration decision. 它改变 `INFER-DYNAMO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10987v1#S3; https://arxiv.org/html/2607.10987v1#S4; https://arxiv.org/html/2607.10987v1#S5`；Evaluation：`https://arxiv.org/html/2607.10987v1#S6; https://arxiv.org/html/2607.10987v1#S6.SS1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10987v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-DYNAMO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10987:end -->

<!-- review:SF-2026-ARXIV-2607-11070:start -->
#### MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment

<!-- claim:SF-2026-ARXIV-2607-11070:start -->Offensive jailbreaking experiments show bounded credit-assignment utility, not defensive robustness, causal turn attribution, or general multi-turn agent-training superiority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11070:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** DC-GRPO decomposes centered discounted return into separately normalized immediate-reward and future-return deviations, then recombines them so turns do not inherit one undifferentiated trajectory advantage. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11070v1#S4; https://arxiv.org/html/2607.11070v1#S4.SS1; https://arxiv.org/html/2607.11070v1#S4.SS2`；Evaluation：`https://arxiv.org/html/2607.11070v1#S5; https://arxiv.org/html/2607.11070v1#S5.SS1; https://arxiv.org/html/2607.11070v1#S5.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11070v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11070:end -->

<!-- review:SF-2026-ARXIV-2607-11079:start -->
#### Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists

<!-- claim:SF-2026-ARXIV-2607-11079:start -->Measures performance under this benchmark and scorer contract; synthetic causal structure does not establish real scientific-discovery competence or faithful mechanisms. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11079:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** SDA-Bench crosses five scientific domains with six discovery task types; synthetic instances use semantic/causal subgraphs and executable equations while real instances test transfer. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11079v1#S3; https://arxiv.org/html/2607.11079v1#S3.SS1; https://arxiv.org/html/2607.11079v1#S3.SS4`；Evaluation：`https://arxiv.org/html/2607.11079v1#S4; https://arxiv.org/html/2607.11079v1#S4.SS1; https://arxiv.org/html/2607.11079v1#S4.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11079v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-11079:end -->

<!-- review:SF-2026-ARXIV-2607-11149:start -->
#### The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation

<!-- claim:SF-2026-ARXIV-2607-11149:start -->Shows storage can dominate and duplicate under selected versions/tasks; does not rank frameworks generally, prove production retention cost, or establish reasoning-quality gains. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11149:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI cost 是资源在时间上的占用与机会成本，必须在质量、可靠性和 SLO 约束下按可归属结果计算；脱离 outcome 的利用率或单价会驱动错误优化。**`（`books/part-06-ai-infrastructure/70-cost.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** AgentFootprint diffs fresh per-run sandboxes, classifies retained artifacts, measures logical bytes/composition/duplication/echo/compressibility/growth and separately tests reconstructability. 它改变 `PLATFORM-COST` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11149v1#S3; https://arxiv.org/html/2607.11149v1#S3.SS1; https://arxiv.org/html/2607.11149v1#S4`；Evaluation：`https://arxiv.org/html/2607.11149v1#S5; https://arxiv.org/html/2607.11149v1#S5.SS1; https://arxiv.org/html/2607.11149v1#S5.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11149v1#S8; https://arxiv.org/html/2607.11149v1#S9`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-COST`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11149:end -->

<!-- review:SF-2026-ARXIV-2607-11172:start -->
#### STAMP: Provenance-Guided Credit Assignment for Deep Search Agents

<!-- claim:SF-2026-ARXIV-2607-11172:start -->Supports relevance-guided credit on one model/checkpoint and selected web-search tasks; earliest exposure is not causal attribution and judge agreement is not ground truth. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11172:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A verifier maps each supported atomic evidence item to the earliest search/read step that exposed the cited document; sign-preserving modulation amplifies credited positive steps and shields them from uniform negative penalty. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11172v1#S2; https://arxiv.org/html/2607.11172v1#S2.SS1; https://arxiv.org/html/2607.11172v1#S2.SS4`；Evaluation：`https://arxiv.org/html/2607.11172v1#S3; https://arxiv.org/html/2607.11172v1#S3.SS1; https://arxiv.org/html/2607.11172v1#S3.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11172v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11172:end -->

<!-- review:SF-2026-ARXIV-2607-11183:start -->
#### Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results

<!-- claim:SF-2026-ARXIV-2607-11183:start -->Demonstrates bounded Qwen-family offline gains on tool/JSON routes; not a universal quality booster, not cross-family evidence, and not a production serving benchmark. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11183:end -->

**旧方案与约束变化。** `本章的核心判断是：**Attention 负责跨 token 路由，MLP 负责对每个位置的上下文状态独立执行高容量非线性变换。**它可以形成任务相关特征和事实关联，但不能被简单描述成可逐条读取的人类知识数据库。`（`books/part-02-model/16-feed-forward-mlp.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** AG keeps FFN weights fixed and masks/shrinks activation amplitudes at selected SwiGLU points; task/model-specific learned gates accept a candidate path only when predicted beneficial, otherwise fall back. 它改变 `MODEL-FFN` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.11183v1 PDF p.5 §3.4 AG as the conservative successor; arXiv:2607.11183v1 PDF p.6 §3.5 FFN computation; arXiv:2607.11183v1 PDF p.7 §3.6-§3.7 intervention points and taxonomy; arXiv:2607.11183v1 PDF p.10 §3.8 gate and fallback`；Evaluation：`arXiv:2607.11183v1 PDF p.10 §4 Experiment Design; arXiv:2607.11183v1 PDF §5 Experiment Results; arXiv:2607.11183v1 PDF §6 Analysis`；Limitations/Counterevidence：`arXiv:2607.11183v1 PDF p.26 §8 Limitations; arXiv:2607.11183v1 PDF p.26-27 §9 Future Work`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MODEL-FFN`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-11183:end -->

<!-- review:SF-2026-ARXIV-2607-11250:start -->
#### Multi-Agent LLMs Fail to Explore Each Other

<!-- claim:SF-2026-ARXIV-2607-11250:start -->Theory is under contextual-bandit assumptions and experiments are small/medium N; does not establish thousand-agent scalability, joint coordination optimality, or nonstationary robustness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11250:end -->

**旧方案与约束变化。** `本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**`（`books/part-07-agent/82-multi-agent.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** MACE casts each agent’s peer choice as an independent contextual bandit and applies relational features plus LinUCB optimism so uncertain but potentially complementary peers are explored. 它改变 `AGENT-MULTI-AGENT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11250v1#S3; https://arxiv.org/html/2607.11250v1#S3.SS1; https://arxiv.org/html/2607.11250v1#S3.SS2`；Evaluation：`https://arxiv.org/html/2607.11250v1#S5; https://arxiv.org/html/2607.11250v1#S5.SS1; https://arxiv.org/html/2607.11250v1#S5.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11250v1#A6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-MULTI-AGENT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11250:end -->

<!-- review:SF-2026-ARXIV-2607-11487:start -->
#### LightMem-Ego: Your AI Memory for Everyday Life

<!-- claim:SF-2026-ARXIV-2607-11487:start -->Prototype evidence does not establish scalable retention, principled merge/forget/promotion, privacy/consent/ACL/deletion, or robust operation under upstream perception errors. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11487:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Frames/audio/metadata align by relative time and session, then asynchronous ASR/refinement/indexing builds current, short-term and long episodic/semantic memory. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11487v1#S3; https://arxiv.org/html/2607.11487v1#S3.SS1; https://arxiv.org/html/2607.11487v1#S3.SS5`；Evaluation：`https://arxiv.org/html/2607.11487v1#S5; https://arxiv.org/html/2607.11487v1#S5.SS1; https://arxiv.org/html/2607.11487v1#S5.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11487v1#S6; https://arxiv.org/html/2607.11487v1#Sx1; https://arxiv.org/html/2607.11487v1#Sx2`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L924-L934`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-11487:end -->

<!-- review:SF-2026-ARXIV-2607-11498:start -->
#### See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-11498:start -->Supports viewpoint robustness for selected simulation/real tasks and backbones; does not eliminate calibration error, embodiment shift, occlusion, control latency or sim-to-real risk. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11498:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Depth is unprojected and transformed into robot/end-effector coordinates, retained in image-form pointmaps and fused with RGB so perception and action share a less viewpoint-dependent frame. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11498v1#S3; https://arxiv.org/html/2607.11498v1#S4.SS1; https://arxiv.org/html/2607.11498v1#S4.SS3`；Evaluation：`https://arxiv.org/html/2607.11498v1#S5; https://arxiv.org/html/2607.11498v1#S5.SS1; https://arxiv.org/html/2607.11498v1#S5.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11498v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11498:end -->

<!-- review:SF-2026-ARXIV-2607-11505:start -->
#### Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update

<!-- claim:SF-2026-ARXIV-2607-11505:start -->Shows transfer inside Qwen3 and selected verifiable math/code tasks; does not prove cross-family transfer, universal reward awareness, optimal token relevance, or cost advantage after calibration/search. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11505:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A smaller proxy explores with GRPO; relative policy update signals are extracted, anchor-calibrated across model scales and applied to a larger primary with a signal-guided objective. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11505v1#S3; https://arxiv.org/html/2607.11505v1#S3.SS2; https://arxiv.org/html/2607.11505v1#S3.SS4`；Evaluation：`https://arxiv.org/html/2607.11505v1#S4; https://arxiv.org/html/2607.11505v1#S4.SS1; https://arxiv.org/html/2607.11505v1#S4.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11505v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L946-L955`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11505:end -->

<!-- review:SF-2026-ARXIV-2607-11656:start -->
#### Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts

<!-- claim:SF-2026-ARXIV-2607-11656:start -->Supports this clinical prediction setting only; missingness may be non-random, uncertainty adjustment is not universal epistemic calibration, and clinical validity/deployment safety are outside the system claim. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11656:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Mask-aware transformer consumes heterogeneous modalities without imputing missing inputs, then adjusts confidence according to missing-modality sensitivity and calibrates predictive uncertainty across cohorts. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11656v1#S4; https://arxiv.org/html/2607.11656v1#S4.SS2; https://arxiv.org/html/2607.11656v1#S4.SS4; https://arxiv.org/html/2607.11656v1#S4.SS5`；Evaluation：`https://arxiv.org/html/2607.11656v1#S2; https://arxiv.org/html/2607.11656v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11656v1#S3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-11656:end -->

<!-- review:SF-2026-ARXIV-2607-11673:start -->
#### ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

<!-- claim:SF-2026-ARXIV-2607-11673:start -->Evidence supports a 3D exploration-generation pipeline, not a universal causal world model, physically correct simulator, or policy-safe environment transition model. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11673:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A 3DGS asset engine renders training samples; a spatial primitive generates panorama/trajectory-conditioned video, then panoramic video is reconstructed to 3DGS with optional physical rendering attributes. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11673v1#S2; https://arxiv.org/html/2607.11673v1#S3; https://arxiv.org/html/2607.11673v1#S3.SS3; https://arxiv.org/html/2607.11673v1#S3.SS6`；Evaluation：`https://arxiv.org/html/2607.11673v1#S4; https://arxiv.org/html/2607.11673v1#S4.SS2; https://arxiv.org/html/2607.11673v1#S4.SS5`；Limitations/Counterevidence：`No dedicated Limitations section in exact v1; counter-boundary derived conservatively from arXiv:2607.11673v1#S3 and #S4, not from an author limitation claim.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-11673:end -->

<!-- review:SF-2026-ARXIV-2607-11849:start -->
#### AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification

<!-- claim:SF-2026-ARXIV-2607-11849:start -->Measures proof/verifier behavior under this dataset and annotation contract; does not establish mathematical correctness outside covered domains or make LLM judges proof authorities. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11849:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** AdvancedMathBench separates proof generation from verifier robustness; an annotation and augmentation pipeline creates positive/negative proof evidence and meta-verification/pessimistic aggregation reduces false acceptance. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11849v1#S3; https://arxiv.org/html/2607.11849v1#S3.SS1; https://arxiv.org/html/2607.11849v1#S4; https://arxiv.org/html/2607.11849v1#S4.SS4`；Evaluation：`https://arxiv.org/html/2607.11849v1#S5; https://arxiv.org/html/2607.11849v1#S5.SS1; https://arxiv.org/html/2607.11849v1#S5.SS4`；Limitations/Counterevidence：`No dedicated Limitations section in exact v1; annotation scope and benchmark boundary are localized in arXiv:2607.11849v1#S3 and Appendix A/C.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L935-L945`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-11849:end -->

<!-- review:SF-2026-ARXIV-2607-11886:start -->
#### Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation

<!-- claim:SF-2026-ARXIV-2607-11886:start -->Shows selected alignment gains; prompt recoverability can miss aesthetics, physical/common-sense implications and inherits MLLM bias, so it is neither human preference nor factual correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11886:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** SpectraReward treats a pretrained MLLM as a zero-shot reward by scoring how likely it is to read the original prompt back from an image; Self-SpectraReward adds self-reconstruction/spectral features without training a dedicated reward model. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11886v1#S3; https://arxiv.org/html/2607.11886v1#S3.SS1; https://arxiv.org/html/2607.11886v1#S3.SS2`；Evaluation：`https://arxiv.org/html/2607.11886v1#S4; https://arxiv.org/html/2607.11886v1#S4.SS1; https://arxiv.org/html/2607.11886v1#S4.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11886v1#A1`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L966-L975`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11886:end -->

<!-- review:SF-2026-ARXIV-2607-12227:start -->
#### Rethinking the Evaluation of Harness Evolution for Agents

<!-- claim:SF-2026-ARXIV-2607-12227:start -->Shows no consistent advantage and limited transfer in this benchmark/model/budget setup; does not prove harness evolution never works, especially on harness-sensitive tasks with more headroom. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12227:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Compares automatic harness evolution with parallel sampling, sequential refinement and instance-level harness scaling under matched feedback/inference budgets, then tests transfer to held-out tasks. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12227v1#S3; https://arxiv.org/html/2607.12227v1#S3.SS2; https://arxiv.org/html/2607.12227v1#S3.SS5`；Evaluation：`https://arxiv.org/html/2607.12227v1#S4; https://arxiv.org/html/2607.12227v1#S4.SS1; https://arxiv.org/html/2607.12227v1#S4.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12227v1#S5; https://arxiv.org/html/2607.12227v1#S5.SS2`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1067-L1076`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-12227:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10987 | Synthetic deterministic shared-prefix multi-agent workflows on 4-16 nodes with deterministic decoding; analytical cost model parameterized by author microbenchmarks | Mistral-7B; Llama-3-8B-Instruct | 4-16 nodes with NVIDIA A100 40GB or 80GB GPUs, 32-64 CPU cores per node, and RDMA InfiniBand | Not Disclosed | Mistral context 32,640 tokens; Llama 3 context 8,128 tokens; deterministic shared-prefix prompts | 64 tokens | Not Disclosed | Workflow width 1-16 agents; serving request concurrency Not Disclosed | No production latency, quality, or availability SLO | Author-controlled system measurements and analytical cost model |
| SF-2026-ARXIV-2607-11070 | Multi-turn jailbreak training on AdvBench for 260 steps and evaluation on HarmBench, StrongREJECT, and JailbreakBench; attacker/victim/judge temperatures 0.9/0/0 | Qwen3-4B attacker; appendix Qwen2.5-3B; Llama, Qwen, Gemma, Mistral, and GPT-OSS-20B victims | Not Disclosed | Not Disclosed | Up to 5 attack turns; token length Not Disclosed | Not Disclosed | Group size 10; serving batch Not Disclosed | Not Disclosed | No production security or latency SLO | HarmBench, StrongREJECT, and JailbreakBench evaluation protocols |
| SF-2026-ARXIV-2607-11079 | Held-out synthetic and real scientific-discovery tasks using multiple-choice and open-ended questions | GPT-5.4; GPT-5.4 mini; Claude Sonnet 4.6; Gemini 3.1 Pro; Gemini 3.1 Flash; DeepSeek V3.2; DeepSeek R1; Qwen 3.5-397B-A17B; Qwen 3-235B-Instruct; Kimi K2.5; GLM 5; Llama 3.3-70B-Instruct; Llama-3.1-8B-Instruct; two LoRA variants of Llama-3.1-8B-Instruct | Not Disclosed; hosted-model hardware is not controlled by authors | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | No production latency or availability SLO | MCQ accuracy; deterministic OEQ scoring with GPT-4o fallback |
| SF-2026-ARXIV-2607-11149 | Six task families across eight agent-framework versions, three repetitions each, 70 controlled fresh-sandbox runs; DeepSeek-V4-Flash temperature 0 | DeepSeek-V4-Flash provider held constant | Not Disclosed | Not Disclosed | Task-dependent; Not Disclosed as a normalized token length | Task-dependent; Not Disclosed as a normalized token length | One isolated run per fresh sandbox; training/serving batch Not Applicable | Not Disclosed | No production retention, latency, or recovery SLO | Task accuracy, including deterministic exact-substring grading for selected file-QA tasks, plus logical bytes, composition, duplication, compressibility, growth, and reconstructability |
| SF-2026-ARXIV-2607-11172 | 3k SFT and 2.6k RL search queries with live Serper/Jina retrieval; BrowseComp, BrowseComp-ZH, and xbench-DS evaluation | Qwen3-30B-A3B-Thinking | 16 NVIDIA H800 GPUs for SFT and 16 NVIDIA H800 GPUs for RL | Not Disclosed | Maximum context 64K or 128K tokens depending on experiment | Not Disclosed | SFT batch size 32 for 1 epoch; RL global batch 256 with rollout size 32 and 8 samples per prompt | Rollout group 8 samples per prompt; serving request concurrency Not Disclosed | No production search latency or availability SLO | GPT-5.1 judge/verifier on BrowseComp, BrowseComp-ZH, and xbench-DS |
| SF-2026-ARXIV-2607-11183 | Offline aligned activation mining over three models and eight text/tool datasets; 241,056 feature rows each for Qwen3.5/Qwen2.5 and 165,432 for Qwen3; feature ablation uses a stable-hash split of 7,396 samples per model and common tool test n=2,556 per model | Qwen3.5-9B; Qwen3-8B; Qwen2.5-7B | Not measured or Not Disclosed for serving | Not Disclosed | Dataset-dependent; Not Disclosed as a normalized length | Dataset-dependent; Not Disclosed as a normalized length | Qwen2.5 run batch size 64; other model-run batch sizes Not Disclosed | Not measured | Online latency, throughput, memory, and production SLO not measured | Dataset task metrics with selected bootstrap confidence intervals |
| SF-2026-ARXIV-2607-11250 | HotpotQA hard subset (600 samples, 5 rounds) and Math500/GPQA (3 rounds), with exploration in the first half and exploitation thereafter; Qwen2.5-7B-Instruct temperature 1.2, GPT-4/GPT-5 default temperature | Ten Qwen2.5-7B-Instruct agents for HotpotQA; GPT-5, Qwen2.5-7B-Instruct, Llama3.1-8B-Instruct, and Mistral-7B-v0.3 agents for Math500/GPQA | Not Disclosed | Not Disclosed | Task-dependent; Not Disclosed as a normalized length | Maximum 2,048 tokens in all disclosed settings | Not Disclosed | Workflow width up to 10 agents; serving request concurrency Not Disclosed | No production latency or coordination SLO | Task-answer accuracy under fixed multi-round protocols |
| SF-2026-ARXIV-2607-11487 | Three daily-life egocentric-memory scenarios with manually annotated ground truth and phone/glasses prototype latency measurements | Upstream API, embedding, retrieval, and LLM component identities Not Disclosed | Phone and smart-glasses prototype; exact device SKUs Not Disclosed in the review contract | Not Disclosed | Scenario-dependent multimodal stream duration; normalized token/frame length Not Disclosed | Not Disclosed | Interactive single-user prototype; batch Not Applicable | Single-user prototype; multi-user concurrency Not Evaluated | P50/P90 component latency reported; no production availability or privacy SLO | Recall@k, MRR, LLM-based answer scoring, human scoring, and prototype latency |
| SF-2026-ARXIV-2607-11498 | RoboCasa simulation design ablations plus real-world VLA tasks; controlled study uses 24 tasks, 50 human demonstrations per task, 30k steps, and 50 evaluation episodes per task | π0.5 and SmolVLA pretrained VLA backbones; controlled study uses a PaliGemma-initialized π-style architecture with a fresh action expert | Simulation and real robot setup; full deployment compute Not Disclosed | bfloat16 for π0.5/SmolVLA fine-tuning | RGB at each backbone's native resolution plus robot-centric pointmap, language instruction, and proprioception; normalized sequence length Not Disclosed | Chunk of end-effector deltas; action-chunk length Not Disclosed in the review contract | Effective batch size 64 for π0.5/SmolVLA fine-tuning | Single embodied control loop; fleet concurrency Not Evaluated | Control frequency and physical-safety SLO Not Disclosed | RoboCasa success metrics, design ablations, and real-world task success |
| SF-2026-ARXIV-2607-11505 | Proxy-to-primary on-policy distillation on math and code tasks; PUST and proxy-GRPO training use temperature 1.0 and rollout count 8; proxy training runs 500 or 300 steps | Qwen3-1.7B and Qwen3-4B proxies; Qwen3-8B primary | 8 NVIDIA A100 80GB GPUs | Not Disclosed | PUST maximum prompt 1,024 or 2,048 tokens by task; proxy GRPO maximum prompt 2,048 tokens | Maximum response 16,384 tokens for PUST and proxy GRPO | PUST train batch 256; proxy GRPO train/microbatch 128; rollout count 8. Mean@16/Mean@8 are evaluation sampling, not optimizer batch | Not Disclosed | No deployment latency or availability SLO | Math/code correctness aggregated as Mean@16 or Mean@8 plus calibration ablations |
| SF-2026-ARXIV-2607-11656 | ADNI, AIBL, and OASIS clinical cohorts across binary classification, multiclass classification, and cognitive prediction; final transformer training uses 7 epochs at learning rate 1e-6 | NITROGEN and NAIM transformers; XGBoost, LightGBM, Random Forest, MA-Lasso, and MA-GBT baselines | Not Disclosed; not central to the clinical evaluation contract | Not Disclosed | Patient feature sequences with heterogeneous missingness; normalized sequence length Not Disclosed | Class or cognitive prediction; generative output length Not Applicable | AdamW batch size 128 | Not Disclosed to the reported offline cohort evaluation | No clinical deployment latency or safety SLO | Cohort task metrics, calibration, attribution, and sufficiency tests |
| SF-2026-ARXIV-2607-11673 | Module-level and end-to-end trajectory, panoramic-video, 3D Gaussian Splatting, and system-applicability evaluation | ABot-3DWorld 0 pipeline; exact component versions are source-version bound | Panoramic-generator inference measured on one node with 4 NVIDIA RTX 4090 GPUs; other pipeline hardware incompletely disclosed | Not Disclosed | Trajectory and panoramic-video dependent; normalized length Not Disclosed | Generated trajectory/video/3D-scene dependent; normalized length Not Disclosed | Not Disclosed | Not Disclosed | Author-measured panoramic generation latency is about 12 minutes per scene on 4x RTX 4090; this is not a production interactive SLO | Author-controlled module metrics, end-to-end metrics, and demonstrations |
| SF-2026-ARXIV-2607-11849 | Advanced mathematical proof generation and verifier-adversarial tasks; temperature 1.0 and highest available reasoning effort unless otherwise specified | GPT-5.5-xhigh; GPT-5.5-high; GPT-5.2; Gemini-3.1-Pro-Preview; Claude-Opus-4.8; DeepSeek-V4-Pro; Qwen3.5-397B-A17B; Kimi-K2.6; GLM-5.2; gpt-oss-120b; Intern-S2-Preview-35B | Not Disclosed; hosted-model hardware not controlled by authors | Not Disclosed | Problem-dependent; Not Disclosed as a normalized length | Maximum 64k tokens unless otherwise specified | Not Disclosed | Not Disclosed | No production latency or verifier false-acceptance SLO | Expert-aligned automatic proof/verifier pipeline plus human annotation; gpt-oss-120b meta-verifier for verification outputs |
| SF-2026-ARXIV-2607-11886 | AWM reinforcement learning on AlphaGRPO20k for text-to-image generation; 32 prompts per step, group size 16, 16 sampling steps with 6 sampled from the first 10 denoising steps, 380 training steps | BAGEL policy; Qwen3-VL-30B-A3B default SpectraReward MLLM; BAGEL understanding branch for Self-SpectraReward | 32 NVIDIA A100 GPUs | Not Disclosed | 32 text prompts per training step; normalized prompt-token length Not Disclosed | Group size 16 images per prompt at 512 x 512 training resolution | Batch size 2 with gradient accumulation 8 | Distributed training across 32 GPUs; serving request concurrency Not Evaluated | No serving latency or availability SLO | GenEval, TIIF, DPG-Bench, WISE, preference metrics, and reward-model ablations |
| SF-2026-ARXIV-2607-12227 | Terminal-Bench 2.1 with the AHE exploration agent disabled; high reasoning effort; results averaged over two independent runs; code agent capped at 300 turns, debugger at 25, and meta agent at 500 | GPT-5.4, GPT-5.4 mini, and Claude Opus 4.6 under source-version-bound API and harness configurations | Not controlled by authors | Not controlled by authors | 200k-token context window | Maximum 128k generated tokens per turn | Not Disclosed | Not Disclosed | No production latency or availability SLO | Terminal-Bench 2.1 pass@1/pass@k and held-out-transfer protocol |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10987 | score_7_9;potential_books_delta | selected | DA-20260714-01 | — | V2=9/9；Supports typed distributed KV-state orchestration under shared-prefix synthetic workflows; does not prove arbitrary cross-model state compatibility, production fault tolerance, persistence, or end-to-end agent quality.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260714-01 |
| SF-2026-ARXIV-2607-11070 | score_7_9;potential_books_delta | not_selected | — | — | Deep review remains mandatory, but its durable delta is a narrower training-objective branch and the offensive security workload limits cross-system reach relative to the three selected units. | analysis-decision:SF-2026-ARXIV-2607-11070 |
| SF-2026-ARXIV-2607-11149 | score_7_9;potential_books_delta | selected | DA-20260714-02 | — | V2=9/9；Shows storage can dominate and duplicate under selected versions/tasks; does not rank frameworks generally, prove production retention cost, or establish reasoning-quality gains.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260714-02 |
| SF-2026-ARXIV-2607-11172 | score_7_9;potential_books_delta | not_selected | — | — | Deep review is complete; provenance-guided earliest exposure is a meaningful experimental credit branch, but it is post-hoc relevance rather than causal credit and is narrower than the selected units. | analysis-decision:SF-2026-ARXIV-2607-11172 |
| SF-2026-ARXIV-2607-11250 | score_7_9;potential_books_delta | selected | DA-20260714-03 | — | V2=9/9；Theory is under contextual-bandit assumptions and experiments are small/medium N; does not establish thousand-agent scalability, joint coordination optimality, or nonstationary robustness.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260714-03 |
| SF-2026-ARXIV-2607-11498 | score_7_9;potential_books_delta | not_selected | — | — | Deep review is complete and the representation delta is integrable, but its calibrated coordinate transform is a compact bridge inside the existing VLA loop rather than a separate long-form analysis unit. | analysis-decision:SF-2026-ARXIV-2607-11498 |
| SF-2026-ARXIV-2607-11505 | score_7_9;potential_books_delta | not_selected | — | — | Deep review is complete; proxy-to-primary relative update transfer is a bounded weak-to-strong training branch whose evidence is confined to one model family and verifiable math/code tasks. | analysis-decision:SF-2026-ARXIV-2607-11505 |
| SF-2026-ARXIV-2607-11886 | score_7_9;potential_books_delta | not_selected | — | — | Deep review is complete, but prompt read-back likelihood is one experimental reward sensor with evaluator bias; it should be a compact Ch66 addition, not one of the three cross-system narratives. | analysis-decision:SF-2026-ARXIV-2607-11886 |
| SF-2026-ARXIV-2607-12227 | score_7_9;potential_books_delta | not_selected | — | — | Deep review is complete due to score 8; its matched-budget and held-out-transfer result confirms existing Ch66/Ch84 admission rules rather than creating a new long-form mechanism. | analysis-decision:SF-2026-ARXIV-2607-12227 |

<!-- analysis:DA-20260714-01:start -->
### [AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows

**旧方案为何合理。** Request-local execution and ordinary data-flow edges were reasonable while each request owned its KV, prefix reuse stayed inside one engine, and moving cache state across workers cost more than recomputation.（现有命题定位：`books/part-05-inference-system/52-dynamo.md#L14-L14`）

**约束变化与机制。** Stateful operator tuple and graph separate data edges from KV-state edges; compatibility identity, fork/compose/transfer/evict/recompute policies make cache movement an explicit orchestration decision. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-DYNAMO` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Supports typed distributed KV-state orchestration under shared-prefix synthetic workflows; does not prove arbitrary cross-model state compatibility, production fault tolerance, persistence, or end-to-end agent quality.

<!-- analysis:DA-20260714-01:end -->

<!-- analysis:DA-20260714-02:start -->
### The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation

**旧方案为何合理。** Token, compute, latency, and task accuracy were reasonable accounting units while agent runs were short-lived, their workspaces were disposable, and retained files or hidden stores were operational residue rather than lifecycle state.（现有命题定位：`books/part-06-ai-infrastructure/70-cost.md#L14-L14`）

**约束变化与机制。** AgentFootprint diffs fresh per-run sandboxes, classifies retained artifacts, measures logical bytes/composition/duplication/echo/compressibility/growth and separately tests reconstructability. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-COST` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Shows storage can dominate and duplicate under selected versions/tasks; does not rank frameworks generally, prove production retention cost, or establish reasoning-quality gains.

<!-- analysis:DA-20260714-02:end -->

<!-- analysis:DA-20260714-03:start -->
### Multi-Agent LLMs Fail to Explore Each Other

**旧方案为何合理。** Fixed or greedy peer selection was reasonable for short workflows when peer quality was already known, coordination rounds were scarce, and the cost of exploring an uncertain peer exceeded the expected information gain.（现有命题定位：`books/part-07-agent/82-multi-agent.md#L14-L14`）

**约束变化与机制。** MACE casts each agent’s peer choice as an independent contextual bandit and applies relational features plus LinUCB optimism so uncertain but potentially complementary peers are explored. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `AGENT-MULTI-AGENT` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Theory is under contextual-bandit assumptions and experiments are small/medium N; does not establish thousand-agent scalability, joint coordination optimality, or nonstationary robustness.

<!-- analysis:DA-20260714-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11070:start -->《MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment》已完成 Deep Source Review。Deep review remains mandatory, but its durable delta is a narrower training-objective branch and the offensive security workload limits cross-system reach relative to the three selected units.<!-- analysis-decision:SF-2026-ARXIV-2607-11070:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11172:start -->《STAMP: Provenance-Guided Credit Assignment for Deep Search Agents》已完成 Deep Source Review。Deep review is complete; provenance-guided earliest exposure is a meaningful experimental credit branch, but it is post-hoc relevance rather than causal credit and is narrower than the selected units.<!-- analysis-decision:SF-2026-ARXIV-2607-11172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11498:start -->《See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models》已完成 Deep Source Review。Deep review is complete and the representation delta is integrable, but its calibrated coordinate transform is a compact bridge inside the existing VLA loop rather than a separate long-form analysis unit.<!-- analysis-decision:SF-2026-ARXIV-2607-11498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11505:start -->《Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update》已完成 Deep Source Review。Deep review is complete; proxy-to-primary relative update transfer is a bounded weak-to-strong training branch whose evidence is confined to one model family and verifiable math/code tasks.<!-- analysis-decision:SF-2026-ARXIV-2607-11505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11886:start -->《Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation》已完成 Deep Source Review。Deep review is complete, but prompt read-back likelihood is one experimental reward sensor with evaluator bias; it should be a compact Ch66 addition, not one of the three cross-system narratives.<!-- analysis-decision:SF-2026-ARXIV-2607-11886:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12227:start -->《Rethinking the Evaluation of Harness Evolution for Agents》已完成 Deep Source Review。Deep review is complete due to score 8; its matched-budget and held-out-transfer result confirms existing Ch66/Ch84 admission rules rather than creating a new long-form mechanism.<!-- analysis-decision:SF-2026-ARXIV-2607-12227:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10987 | INFER-DYNAMO | books/part-05-inference-system/52-dynamo.md#L1 | books/part-05-inference-system/51-sglang.md#L14-L14; books/part-05-inference-system/53-kserve-llm.md#L14-L14 | existing:SF-2026-ARXIV-2607-10987 | delta:SF-2026-ARXIV-2607-10987 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10987 |
| SF-2026-ARXIV-2607-11070 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-11070 | delta:SF-2026-ARXIV-2607-11070 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11070 |
| SF-2026-ARXIV-2607-11079 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-11079 | delta:SF-2026-ARXIV-2607-11079 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11079 |
| SF-2026-ARXIV-2607-11149 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-06-ai-infrastructure/69-trace.md#L14-L14; books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14 | existing:SF-2026-ARXIV-2607-11149 | delta:SF-2026-ARXIV-2607-11149 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11149 |
| SF-2026-ARXIV-2607-11172 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-11172 | delta:SF-2026-ARXIV-2607-11172 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11172 |
| SF-2026-ARXIV-2607-11250 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L14-L14; books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-11250 | delta:SF-2026-ARXIV-2607-11250 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11250 |
| SF-2026-ARXIV-2607-11487 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14-L14 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-11487 | delta:SF-2026-ARXIV-2607-11487 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11487 |
| SF-2026-ARXIV-2607-11498 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-11498 | delta:SF-2026-ARXIV-2607-11498 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11498 |
| SF-2026-ARXIV-2607-11505 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-11505 | delta:SF-2026-ARXIV-2607-11505 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11505 |
| SF-2026-ARXIV-2607-11656 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-11656 | delta:SF-2026-ARXIV-2607-11656 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11656 |
| SF-2026-ARXIV-2607-11673 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-11673 | delta:SF-2026-ARXIV-2607-11673 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11673 |
| SF-2026-ARXIV-2607-11849 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-11849 | delta:SF-2026-ARXIV-2607-11849 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-11849 |
| SF-2026-ARXIV-2607-11886 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-11886 | delta:SF-2026-ARXIV-2607-11886 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11886 |
| SF-2026-ARXIV-2607-12227 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-12227 | delta:SF-2026-ARXIV-2607-12227 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12227 |

<!-- books-review:SF-2026-ARXIV-2607-10987:start --><!-- existing:SF-2026-ARXIV-2607-10987:start -->对读 `books/part-05-inference-system/52-dynamo.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/52-dynamo.md#L14-L14`）为：本章的核心判断是：**Dynamo 位于 inference engine 之上，通过 request path、control path 和 KV state path 协调多个 worker pools；它优化的是分布式能力交付系统，而不是替代底层模型执行引擎。**<!-- existing:SF-2026-ARXIV-2607-10987:end --><!-- delta:SF-2026-ARXIV-2607-10987:start -->新增证据边界：Stateful operator tuple and graph separate data edges from KV-state edges; compatibility identity, fork/compose/transfer/evict/recompute policies make cache movement an explicit orchestration decision. 该 delta 已进入 `books/part-05-inference-system/52-dynamo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10987:end --><!-- books-review:SF-2026-ARXIV-2607-10987:end -->

<!-- books-review:SF-2026-ARXIV-2607-11070:start --><!-- existing:SF-2026-ARXIV-2607-11070:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-11070:end --><!-- delta:SF-2026-ARXIV-2607-11070:start -->新增证据边界：DC-GRPO decomposes centered discounted return into separately normalized immediate-reward and future-return deviations, then recombines them so turns do not inherit one undifferentiated trajectory advantage. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11070:end --><!-- books-review:SF-2026-ARXIV-2607-11070:end -->

<!-- books-review:SF-2026-ARXIV-2607-11079:start --><!-- existing:SF-2026-ARXIV-2607-11079:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-11079:end --><!-- delta:SF-2026-ARXIV-2607-11079:start -->新增证据边界：SDA-Bench crosses five scientific domains with six discovery task types; synthetic instances use semantic/causal subgraphs and executable equations while real instances test transfer. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-11079:end --><!-- books-review:SF-2026-ARXIV-2607-11079:end -->

<!-- books-review:SF-2026-ARXIV-2607-11149:start --><!-- existing:SF-2026-ARXIV-2607-11149:start -->对读 `books/part-06-ai-infrastructure/70-cost.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/70-cost.md#L14-L14`）为：本章的核心判断是：**AI cost 是资源在时间上的占用与机会成本，必须在质量、可靠性和 SLO 约束下按可归属结果计算；脱离 outcome 的利用率或单价会驱动错误优化。**<!-- existing:SF-2026-ARXIV-2607-11149:end --><!-- delta:SF-2026-ARXIV-2607-11149:start -->新增证据边界：AgentFootprint diffs fresh per-run sandboxes, classifies retained artifacts, measures logical bytes/composition/duplication/echo/compressibility/growth and separately tests reconstructability. 该 delta 已进入 `books/part-06-ai-infrastructure/70-cost.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11149:end --><!-- books-review:SF-2026-ARXIV-2607-11149:end -->

<!-- books-review:SF-2026-ARXIV-2607-11172:start --><!-- existing:SF-2026-ARXIV-2607-11172:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-11172:end --><!-- delta:SF-2026-ARXIV-2607-11172:start -->新增证据边界：A verifier maps each supported atomic evidence item to the earliest search/read step that exposed the cited document; sign-preserving modulation amplifies credited positive steps and shields them from uniform negative penalty. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11172:end --><!-- books-review:SF-2026-ARXIV-2607-11172:end -->

<!-- books-review:SF-2026-ARXIV-2607-11250:start --><!-- existing:SF-2026-ARXIV-2607-11250:start -->对读 `books/part-07-agent/82-multi-agent.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/82-multi-agent.md#L14-L14`）为：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2607-11250:end --><!-- delta:SF-2026-ARXIV-2607-11250:start -->新增证据边界：MACE casts each agent’s peer choice as an independent contextual bandit and applies relational features plus LinUCB optimism so uncertain but potentially complementary peers are explored. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11250:end --><!-- books-review:SF-2026-ARXIV-2607-11250:end -->

<!-- books-review:SF-2026-ARXIV-2607-11487:start --><!-- existing:SF-2026-ARXIV-2607-11487:start -->对读 `books/part-07-agent/77-memory.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-11487:end --><!-- delta:SF-2026-ARXIV-2607-11487:start -->新增证据边界：Frames/audio/metadata align by relative time and session, then asynchronous ASR/refinement/indexing builds current, short-term and long episodic/semantic memory. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-11487:end --><!-- books-review:SF-2026-ARXIV-2607-11487:end -->

<!-- books-review:SF-2026-ARXIV-2607-11498:start --><!-- existing:SF-2026-ARXIV-2607-11498:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-11498:end --><!-- delta:SF-2026-ARXIV-2607-11498:start -->新增证据边界：Depth is unprojected and transformed into robot/end-effector coordinates, retained in image-form pointmaps and fused with RGB so perception and action share a less viewpoint-dependent frame. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11498:end --><!-- books-review:SF-2026-ARXIV-2607-11498:end -->

<!-- books-review:SF-2026-ARXIV-2607-11505:start --><!-- existing:SF-2026-ARXIV-2607-11505:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-11505:end --><!-- delta:SF-2026-ARXIV-2607-11505:start -->新增证据边界：A smaller proxy explores with GRPO; relative policy update signals are extracted, anchor-calibrated across model scales and applied to a larger primary with a signal-guided objective. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11505:end --><!-- books-review:SF-2026-ARXIV-2607-11505:end -->

<!-- books-review:SF-2026-ARXIV-2607-11656:start --><!-- existing:SF-2026-ARXIV-2607-11656:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-11656:end --><!-- delta:SF-2026-ARXIV-2607-11656:start -->新增证据边界：Mask-aware transformer consumes heterogeneous modalities without imputing missing inputs, then adjusts confidence according to missing-modality sensitivity and calibrates predictive uncertainty across cohorts. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-11656:end --><!-- books-review:SF-2026-ARXIV-2607-11656:end -->

<!-- books-review:SF-2026-ARXIV-2607-11673:start --><!-- existing:SF-2026-ARXIV-2607-11673:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-11673:end --><!-- delta:SF-2026-ARXIV-2607-11673:start -->新增证据边界：A 3DGS asset engine renders training samples; a spatial primitive generates panorama/trajectory-conditioned video, then panoramic video is reconstructed to 3DGS with optional physical rendering attributes. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-11673:end --><!-- books-review:SF-2026-ARXIV-2607-11673:end -->

<!-- books-review:SF-2026-ARXIV-2607-11849:start --><!-- existing:SF-2026-ARXIV-2607-11849:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-11849:end --><!-- delta:SF-2026-ARXIV-2607-11849:start -->新增证据边界：AdvancedMathBench separates proof generation from verifier robustness; an annotation and augmentation pipeline creates positive/negative proof evidence and meta-verification/pessimistic aggregation reduces false acceptance. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-11849:end --><!-- books-review:SF-2026-ARXIV-2607-11849:end -->

<!-- books-review:SF-2026-ARXIV-2607-11886:start --><!-- existing:SF-2026-ARXIV-2607-11886:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-11886:end --><!-- delta:SF-2026-ARXIV-2607-11886:start -->新增证据边界：SpectraReward treats a pretrained MLLM as a zero-shot reward by scoring how likely it is to read the original prompt back from an image; Self-SpectraReward adds self-reconstruction/spectral features without training a dedicated reward model. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11886:end --><!-- books-review:SF-2026-ARXIV-2607-11886:end -->

<!-- books-review:SF-2026-ARXIV-2607-12227:start --><!-- existing:SF-2026-ARXIV-2607-12227:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-12227:end --><!-- delta:SF-2026-ARXIV-2607-12227:start -->新增证据边界：Compares automatic harness evolution with parallel sampling, sequential refinement and instance-level harness scaling under matched feedback/inference budgets, then tests transfer to held-out tasks. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-12227:end --><!-- books-review:SF-2026-ARXIV-2607-12227:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260714-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260714; semantic-review:SA-20260714-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260714-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-10987; review:SF-2026-ARXIV-2607-11070; review:SF-2026-ARXIV-2607-11079; review:SF-2026-ARXIV-2607-11149; review:SF-2026-ARXIV-2607-11172; review:SF-2026-ARXIV-2607-11183; review:SF-2026-ARXIV-2607-11250; review:SF-2026-ARXIV-2607-11487; review:SF-2026-ARXIV-2607-11498; review:SF-2026-ARXIV-2607-11505; review:SF-2026-ARXIV-2607-11656; review:SF-2026-ARXIV-2607-11673; review:SF-2026-ARXIV-2607-11849; review:SF-2026-ARXIV-2607-11886; review:SF-2026-ARXIV-2607-12227; semantic-review:SA-20260714-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260714-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260714-01; analysis:DA-20260714-02; analysis:DA-20260714-03; semantic-review:SA-20260714-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260714-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-10987; books-review:SF-2026-ARXIV-2607-11070; books-review:SF-2026-ARXIV-2607-11079; books-review:SF-2026-ARXIV-2607-11149; books-review:SF-2026-ARXIV-2607-11172; books-review:SF-2026-ARXIV-2607-11250; books-review:SF-2026-ARXIV-2607-11487; books-review:SF-2026-ARXIV-2607-11498; books-review:SF-2026-ARXIV-2607-11505; books-review:SF-2026-ARXIV-2607-11656; books-review:SF-2026-ARXIV-2607-11673; books-review:SF-2026-ARXIV-2607-11849; books-review:SF-2026-ARXIV-2607-11886; books-review:SF-2026-ARXIV-2607-12227; review:SF-2026-ARXIV-2607-11183; semantic-review:SA-20260714-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260714-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260714-COVERAGE:end -->
<!-- semantic-review:SA-20260714-EVIDENCE:start -->Fresh-context review reconciled all 15 frozen families: 9 Deep, 6 Standard and 0 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260714-EVIDENCE:end -->
<!-- semantic-review:SA-20260714-SELECTION:start -->Fresh-context review reconciled 9 eligible Deep families: 3 selected and 6 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260714-SELECTION:end -->
<!-- semantic-review:SA-20260714-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 8 个 family 已定位到实际 Books 段落，6 个 family 的 No Change 结论可定位，1 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260714-BOOKS:end -->

## 8. Ignored Noise

1223 个窗口内 identity 中，1208 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：8 个 `Integrate`，6 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 9 / Standard 6。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/14/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-04-training-system/33-grpo.md`、`books/part-05-inference-system/52-dynamo.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-06-ai-infrastructure/70-cost.md`、`books/part-07-agent/82-multi-agent.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows](https://arxiv.org/abs/2607.10987v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](https://arxiv.org/abs/2607.11070v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists](https://arxiv.org/abs/2607.11079v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation](https://arxiv.org/abs/2607.11149v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [STAMP: Provenance-Guided Credit Assignment for Deep Search Agents](https://arxiv.org/abs/2607.11172v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](https://arxiv.org/abs/2607.11183v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [Multi-Agent LLMs Fail to Explore Each Other](https://arxiv.org/abs/2607.11250v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [LightMem-Ego: Your AI Memory for Everyday Life](https://arxiv.org/abs/2607.11487v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models](https://arxiv.org/abs/2607.11498v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update](https://arxiv.org/abs/2607.11505v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [Imputation-free transformer learning enables robust Alzheimer's disease prediction and calibrated uncertainty quantification across heterogeneous clinical cohorts](https://arxiv.org/abs/2607.11656v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v1) — first-public（Asia/Shanghai）：2026-07-13；accessed：2026-08-27
- [AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification](https://arxiv.org/abs/2607.11849v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2607.11886v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/abs/2607.12227v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
