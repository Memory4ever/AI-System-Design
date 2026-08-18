# Daily Research — 2026-07-31

**Research Date:** 2026-07-31

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-30 09:00:00 ～ 2026-07-31 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；直接 arXiv 枚举冻结候选分母，技术 claim 回到精确 arXiv v1 与事件时 artifact receipt

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1353 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 15 个。当前路由账目为 15 个 Deep、0 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-31 |
| Window End | 2026-07-31 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-31-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T20:48:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-30T09:00:00+08:00 | 2026-07-31T09:00:00+08:00 | 2026-08-27T20:48:00+08:00 | https://export.arxiv.org/api/query; submittedDate exact replay; v1 published timestamp; cross-list deduplicated by arXiv ID | checked | 1353 | SF-2026-ARXIV-2607-27694<br>SF-2026-ARXIV-2607-27704<br>SF-2026-ARXIV-2607-27773<br>SF-2026-ARXIV-2607-27782<br>SF-2026-ARXIV-2607-27834<br>SF-2026-ARXIV-2607-27933<br>SF-2026-ARXIV-2607-27967<br>SF-2026-ARXIV-2607-28699<br>SF-2026-ARXIV-2607-28150<br>SF-2026-ARXIV-2607-28336<br>SF-2026-ARXIV-2607-28415<br>SF-2026-ARXIV-2607-28418<br>SF-2026-ARXIV-2607-28495<br>SF-2026-ARXIV-2607-28624<br>SF-2026-ARXIV-2607-28884 | archived direct-arXiv pages; final_cursor=end | 2026-07-31T09:00:00+08:00 | coverage:SRC-ARXIV:20260731 | — |
| SRC-GITHUB-COMMIT | 2026-07-30T09:00:00+08:00 | 2026-07-31T09:00:00+08:00 | 2026-08-27T20:48:00+08:00 | exact GitHub commit API lookups: https://github.com/rrrrrrzy/fm-geometry@8feb469ab2e358e465ac0ea58ee13c46e956696c; https://github.com/EIT-NLP/LLM-Pruning@040b61ef141834c7f524f258d731deebff5f09d0 | checked | 2 | SF-2026-ARXIV-2607-27933; SF-2026-ARXIV-2607-28418 | pages=2; final cursors=8feb469ab2e358e465ac0ea58ee13c46e956696c,040b61ef141834c7f524f258d731deebff5f09d0; one bounded commit lookup per family | 2026-07-31T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260731 | — |

<!-- coverage:SRC-ARXIV:20260731:start -->Archived direct-arXiv submittedDate replay froze the strict-window denominator. Canonical source: papers/2026/07/_sources/arxiv-v2.1-replay-20260727-31/README.md; sha256:None; 1353 unique identities in this strict window; 15 routed families.<!-- coverage:SRC-ARXIV:20260731:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260731:start -->repository=https://github.com/rrrrrrzy/fm-geometry, until=2026-07-31T01:00:00Z, full_sha=8feb469ab2e358e465ac0ea58ee13c46e956696c, commit_timestamp=2026-07-30T09:08:14Z, url=https://github.com/rrrrrrzy/fm-geometry/commit/8feb469ab2e358e465ac0ea58ee13c46e956696c; repository=https://github.com/EIT-NLP/LLM-Pruning, until=2026-07-31T01:00:00Z, full_sha=040b61ef141834c7f524f258d731deebff5f09d0, commit_timestamp=2026-07-30T14:38:33Z, url=https://github.com/EIT-NLP/LLM-Pruning/commit/040b61ef141834c7f524f258d731deebff5f09d0; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260731:end -->

### Coverage Limitations

- 直接 arXiv replay 只闭合候选枚举与 first-public identity；机制和实验结论仍逐项来自 exact-v1 全文与可追溯 artifact。
- Artifact-boundary routing 覆盖 15 个 family：exact v1 为 4 个 family 披露 artifact/evidence locator，其中 4 个提供外部 repository/project/demo locator，另有 11 个未披露；本日确认 2 个 family、2 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27694 | arXiv:2607.27694v1 | paper-v1:2607.27694 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27694 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-27694 | yes |
| SF-2026-ARXIV-2607-27704 | arXiv:2607.27704v1 | paper-v1:2607.27704 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27704 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-27704 | yes |
| SF-2026-ARXIV-2607-27773 | arXiv:2607.27773v1 | paper-v1:2607.27773 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27773 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2607-27773 | yes |
| SF-2026-ARXIV-2607-27782 | arXiv:2607.27782v1 | paper-v1:2607.27782 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27782 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-27782 | yes |
| SF-2026-ARXIV-2607-27834 | arXiv:2607.27834v1 | paper-v1:2607.27834 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27834 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2607-27834 | yes |
| SF-2026-ARXIV-2607-27933 | arXiv:2607.27933v1 | paper-v1:2607.27933 | 2026-W31 | 2026-07-30 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27933 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-27933 | yes |
| SF-2026-ARXIV-2607-27967 | arXiv:2607.27967v1 | paper-v1:2607.27967 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-27967 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2607-27967 | yes |
| SF-2026-ARXIV-2607-28699 | arXiv:2607.28699v1 | paper-v1:2607.28699 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28699 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-28699 | yes |
| SF-2026-ARXIV-2607-28150 | arXiv:2607.28150v1 | paper-v1:2607.28150 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28150 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Integrate | books-review:SF-2026-ARXIV-2607-28150 | yes |
| SF-2026-ARXIV-2607-28336 | arXiv:2607.28336v1 | paper-v1:2607.28336 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28336 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2607-28336 | yes |
| SF-2026-ARXIV-2607-28415 | arXiv:2607.28415v1 | paper-v1:2607.28415 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28415 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-28415 | yes |
| SF-2026-ARXIV-2607-28418 | arXiv:2607.28418v1 | paper-v1:2607.28418 | 2026-W31 | 2026-07-31 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28418 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-28418 | yes |
| SF-2026-ARXIV-2607-28495 | arXiv:2607.28495v1 | paper-v1:2607.28495 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28495 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-28495 | yes |
| SF-2026-ARXIV-2607-28624 | arXiv:2607.28624v1 | paper-v1:2607.28624 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28624 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2607-28624 | yes |
| SF-2026-ARXIV-2607-28884 | arXiv:2607.28884v1 | paper-v1:2607.28884 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-28884 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-28884 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27694 | RP-f3a6514bdb72dd53 | deep | arXiv:2607.27694v1 | SRC-ARXIV@arXiv:2607.27694v1 | https://arxiv.org/html/2607.27694v1#S3; https://arxiv.org/html/2607.27694v1#S4; https://arxiv.org/html/2607.27694v1#S5 | https://arxiv.org/html/2607.27694v1#S6.SS1; https://arxiv.org/html/2607.27694v1#S6.SS2; https://arxiv.org/html/2607.27694v1#S6.SS3 | Not Disclosed — exact v1 has no dedicated limitations section; scope limits are inferred only from the disclosed RTL/model evaluation and are recorded as what_is_not_proven. | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-27694 | complete |
| SF-2026-ARXIV-2607-27704 | RP-7976dd2f8e4772ad | deep | arXiv:2607.27704v1 | SRC-ARXIV@arXiv:2607.27704v1 | https://arxiv.org/html/2607.27704v1#S3; https://arxiv.org/html/2607.27704v1#S5 | https://arxiv.org/html/2607.27704v1#S4; https://arxiv.org/html/2607.27704v1#S6 | https://arxiv.org/html/2607.27704v1#S7 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-27704 | complete |
| SF-2026-ARXIV-2607-27773 | RP-dffac03e26d4fbba | deep | arXiv:2607.27773v1 | SRC-ARXIV@arXiv:2607.27773v1 | https://arxiv.org/html/2607.27773v1#S3; https://arxiv.org/html/2607.27773v1#S3.SS3 | https://arxiv.org/html/2607.27773v1#S4; https://arxiv.org/html/2607.27773v1#S5 | https://arxiv.org/html/2607.27773v1#Sx1 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-27773 | complete |
| SF-2026-ARXIV-2607-27782 | RP-8934b5024b659cc7 | deep | arXiv:2607.27782v1 | SRC-ARXIV@arXiv:2607.27782v1 | https://arxiv.org/html/2607.27782v1#S3; https://arxiv.org/html/2607.27782v1#S3.SS3 | https://arxiv.org/html/2607.27782v1#S4; https://arxiv.org/html/2607.27782v1#S4.SS1 | https://arxiv.org/html/2607.27782v1#A6 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-27782 | complete |
| SF-2026-ARXIV-2607-27834 | RP-026a28a294d77d57 | deep | arXiv:2607.27834v1 | SRC-ARXIV@arXiv:2607.27834v1 | https://arxiv.org/html/2607.27834v1#Sx3 | https://arxiv.org/html/2607.27834v1#Sx4 | https://arxiv.org/html/2607.27834v1#Sx5 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-27834 | complete |
| SF-2026-ARXIV-2607-27933 | RP-e621177701911d27 | deep | arXiv:2607.27933v1 | SRC-ARXIV@arXiv:2607.27933v1; SRC-GITHUB-COMMIT@commit:8feb469ab2e358e465ac0ea58ee13c46e956696c | https://arxiv.org/html/2607.27933v1#S2; https://arxiv.org/html/2607.27933v1#S3 | https://arxiv.org/html/2607.27933v1#S4; https://arxiv.org/html/2607.27933v1#A1; https://arxiv.org/html/2607.27933v1#A2 | https://arxiv.org/html/2607.27933v1#S6; https://arxiv.org/html/2607.27933v1#A3; https://arxiv.org/html/2607.27933v1#A4 | https://github.com/rrrrrrzy/fm-geometry — event-time commit pinned; paper claim remains bounded to v1 evaluation. | claim:SF-2026-ARXIV-2607-27933 | complete |
| SF-2026-ARXIV-2607-27967 | RP-58000b06b1a56654 | deep | arXiv:2607.27967v1 | SRC-ARXIV@arXiv:2607.27967v1 | https://arxiv.org/html/2607.27967v1#S5 | https://arxiv.org/html/2607.27967v1#S8; https://arxiv.org/html/2607.27967v1#A3; https://arxiv.org/html/2607.27967v1#A6 | https://arxiv.org/html/2607.27967v1#S10 | https://github.com/Vector-Wangel/XLeRobot — validation platform/reference only, not MARS-RA experiment provenance. | claim:SF-2026-ARXIV-2607-27967 | complete |
| SF-2026-ARXIV-2607-28699 | RP-f118e2e2264a2666 | deep | arXiv:2607.28699v1 | SRC-ARXIV@arXiv:2607.28699v1 | https://arxiv.org/html/2607.28699v1#S3; https://arxiv.org/html/2607.28699v1#S4; https://arxiv.org/html/2607.28699v1#S6.SS1; https://arxiv.org/html/2607.28699v1#S6.SS2 | https://arxiv.org/html/2607.28699v1#S5; https://arxiv.org/html/2607.28699v1#S6.SS3 | https://arxiv.org/html/2607.28699v1#S6.SS4.SSS6; https://arxiv.org/html/2607.28699v1#A2 | https://github.com/wayfind/witcert — repository was private/404 at event-time review; exact implementation commit unavailable. | claim:SF-2026-ARXIV-2607-28699 | complete |
| SF-2026-ARXIV-2607-28150 | RP-1c44324e84bd16f0 | deep | arXiv:2607.28150v1 | SRC-ARXIV@arXiv:2607.28150v1 | https://arxiv.org/html/2607.28150v1#S4 | https://arxiv.org/html/2607.28150v1#S5 | https://arxiv.org/html/2607.28150v1#S4.SS4 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28150 | complete |
| SF-2026-ARXIV-2607-28336 | RP-d2437bb47d484473 | deep | arXiv:2607.28336v1 | SRC-ARXIV@arXiv:2607.28336v1 | https://arxiv.org/html/2607.28336v1#S3; https://arxiv.org/html/2607.28336v1#S3.SS1; https://arxiv.org/html/2607.28336v1#S3.SS6 | https://arxiv.org/html/2607.28336v1#S4 | https://arxiv.org/html/2607.28336v1#S4.SS5 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28336 | complete |
| SF-2026-ARXIV-2607-28415 | RP-c9a71dfa8c20657d | deep | arXiv:2607.28415v1 | SRC-ARXIV@arXiv:2607.28415v1 | https://arxiv.org/html/2607.28415v1#S3; https://arxiv.org/html/2607.28415v1#S3.SS3 | https://arxiv.org/html/2607.28415v1#S4 | https://arxiv.org/html/2607.28415v1#S4.SS6 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28415 | complete |
| SF-2026-ARXIV-2607-28418 | RP-17a61f5c1fb9e394 | deep | arXiv:2607.28418v1 | SRC-ARXIV@arXiv:2607.28418v1; SRC-GITHUB-COMMIT@commit:040b61ef141834c7f524f258d731deebff5f09d0 | https://arxiv.org/html/2607.28418v1#S3 | https://arxiv.org/html/2607.28418v1#S4.SS1; https://arxiv.org/html/2607.28418v1#S4.SS2; https://arxiv.org/html/2607.28418v1#S4.SS3; https://arxiv.org/html/2607.28418v1#S4.SS4; https://arxiv.org/html/2607.28418v1#A1; https://arxiv.org/html/2607.28418v1#A2; https://arxiv.org/html/2607.28418v1#A3 | Not Disclosed — exact v1 has no dedicated limitations section; unsupported shapes, metadata cost and production tail-SLO remain untested boundaries, not claims attributed to §4.4. | https://github.com/EIT-NLP/LLM-Pruning/tree/main/WIDE — event-time repository commit pinned, but v1 does not bind every figure to that commit. | claim:SF-2026-ARXIV-2607-28418 | complete |
| SF-2026-ARXIV-2607-28495 | RP-b5f2e072f827a6e3 | deep | arXiv:2607.28495v1 | SRC-ARXIV@arXiv:2607.28495v1 | https://arxiv.org/html/2607.28495v1#S3 | https://arxiv.org/html/2607.28495v1#S4 | https://arxiv.org/html/2607.28495v1#S6 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28495 | complete |
| SF-2026-ARXIV-2607-28624 | RP-8bb482a29648af82 | deep | arXiv:2607.28624v1 | SRC-ARXIV@arXiv:2607.28624v1 | https://arxiv.org/html/2607.28624v1#S3 | https://arxiv.org/html/2607.28624v1#S4; https://arxiv.org/html/2607.28624v1#A2; https://arxiv.org/html/2607.28624v1#A3 | https://arxiv.org/html/2607.28624v1#A5 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28624 | complete |
| SF-2026-ARXIV-2607-28884 | RP-e3567ecbf3fb48ad | deep | arXiv:2607.28884v1 | SRC-ARXIV@arXiv:2607.28884v1 | https://arxiv.org/html/2607.28884v1#S3; https://arxiv.org/html/2607.28884v1#S4 | https://arxiv.org/html/2607.28884v1#S5 | https://arxiv.org/html/2607.28884v1#S6; https://arxiv.org/html/2607.28884v1#Sx2 | Not Disclosed — exact v1 does not bind its result to an immutable public experiment commit. | claim:SF-2026-ARXIV-2607-28884 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-27694:start -->
#### GyRot

<!-- claim:SF-2026-ARXIV-2607-27694:start -->The author configuration couples algorithm and modeled numeric datapath successfully. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27694:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** CoRFiG decouples rotation R from group G; HAP aligns outliers; asymmetric scale/zero-point become INT8. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27694v1#S3; https://arxiv.org/html/2607.27694v1#S4; https://arxiv.org/html/2607.27694v1#S5`；Evaluation：`https://arxiv.org/html/2607.27694v1#S6.SS1; https://arxiv.org/html/2607.27694v1#S6.SS2; https://arxiv.org/html/2607.27694v1#S6.SS3`；Limitations/Counterevidence：`Not Disclosed — exact v1 has no dedicated limitations section; scope limits are inferred only from the disclosed RTL/model evaluation and are recorded as what_is_not_proven.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27694:end -->

<!-- review:SF-2026-ARXIV-2607-27704:start -->
#### LightRot

<!-- claim:SF-2026-ARXIV-2607-27704:start -->Local rotation/ODA is viable in the modeled design. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27704:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** GLR uses hierarchical 16x8 FHT; ODA aligns calibrated outliers to a Hadamard direction. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27704v1#S3; https://arxiv.org/html/2607.27704v1#S5`；Evaluation：`https://arxiv.org/html/2607.27704v1#S4; https://arxiv.org/html/2607.27704v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27704v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-27704:end -->

<!-- review:SF-2026-ARXIV-2607-27773:start -->
#### ChronoMem

<!-- claim:SF-2026-ARXIV-2607-27773:start -->Separating semantic selection from ID-based restore improves the tested rollback protocol. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27773:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Immutable events and whole-memory snapshots form semantic commits; natural-language resolver selects a version, ID rollback restores and advances HEAD. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27773v1#S3; https://arxiv.org/html/2607.27773v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.27773v1#S4; https://arxiv.org/html/2607.27773v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27773v1#Sx1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27773:end -->

<!-- review:SF-2026-ARXIV-2607-27782:start -->
#### RedFlow

<!-- claim:SF-2026-ARXIV-2607-27782:start -->Chunk-local supported correction improves author workloads and sample-efficiency comparisons. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27782:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A general reward model estimates smoothed progress; progress delta plus outcome signs chunks; HDBSCAN finds nearby positive corrective centroids; unsupported failures are suppressed. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27782v1#S3; https://arxiv.org/html/2607.27782v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.27782v1#S4; https://arxiv.org/html/2607.27782v1#S4.SS1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27782v1#A6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27782:end -->

<!-- review:SF-2026-ARXIV-2607-27834:start -->
#### MemTxn

<!-- claim:SF-2026-ARXIV-2607-27834:start -->The tested boundary separates semantic admission from storage recovery and restores the application-visible preimage. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27834:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Ordered PatchTest admits source-supported updates; chronology resolver declares visible version; durable before-image restores complete active map after reopen. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27834v1#Sx3`；Evaluation：`https://arxiv.org/html/2607.27834v1#Sx4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27834v1#Sx5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27834:end -->

<!-- review:SF-2026-ARXIV-2607-27933:start -->
#### Flow-Matching Uncertainty Geometry

<!-- claim:SF-2026-ARXIV-2607-27933:start -->In tested settings acceleration is a useful cheap detector and can alarm before timeout. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27933:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Deviation from affine-isotropic sink geometry links velocity Jacobian/posterior covariance to trajectory acceleration; prefix acceleration feeds calibrated CUSUM. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27933v1#S2; https://arxiv.org/html/2607.27933v1#S3`；Evaluation：`https://arxiv.org/html/2607.27933v1#S4; https://arxiv.org/html/2607.27933v1#A1; https://arxiv.org/html/2607.27933v1#A2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27933v1#S6; https://arxiv.org/html/2607.27933v1#A3; https://arxiv.org/html/2607.27933v1#A4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27933:end -->

<!-- review:SF-2026-ARXIV-2607-27967:start -->
#### MARS-RA

<!-- claim:SF-2026-ARXIV-2607-27967:start -->The ranking-based shaping improves author tasks under observed visual evidence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-27967:end -->

**旧方案与约束变化。** `本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**`（`books/part-07-agent/82-multi-agent.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** LMM pairwise comparisons form a matrix; rank aggregation yields contribution credits; potential shaping feeds MAPPO. 它改变 `AGENT-MULTI-AGENT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.27967v1#S5`；Evaluation：`https://arxiv.org/html/2607.27967v1#S8; https://arxiv.org/html/2607.27967v1#A3; https://arxiv.org/html/2607.27967v1#A6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.27967v1#S10`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-MULTI-AGENT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-27967:end -->

<!-- review:SF-2026-ARXIV-2607-28699:start -->
#### WitCert

<!-- claim:SF-2026-ARXIV-2607-28699:start -->Tier A is deterministic under stated quantizer class; Tier B is probabilistic for non-adaptive queries; tested gate detected sampled violations. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28699:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Tier A deterministic RoPE-band residual witness applies to reconstructable per-token quantizers; Tier B gives a dithered INT8 sub-Gaussian certificate under non-adaptive queries and request delta budget. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28699v1#S3; https://arxiv.org/html/2607.28699v1#S4; https://arxiv.org/html/2607.28699v1#S6.SS1; https://arxiv.org/html/2607.28699v1#S6.SS2`；Evaluation：`https://arxiv.org/html/2607.28699v1#S5; https://arxiv.org/html/2607.28699v1#S6.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28699v1#S6.SS4.SSS6; https://arxiv.org/html/2607.28699v1#A2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28699:end -->

<!-- review:SF-2026-ARXIV-2607-28150:start -->
#### SmartGen

<!-- claim:SF-2026-ARXIV-2607-28150:start -->Selective transfer with demand repair helps the author topology and workload. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28150:end -->

**旧方案与约束变化。** `本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**`（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Profiled proactive transfer, decode demand fetch and speculative prefetch cooperate; low load falls back to full transfer. 它改变 `INFER-PD-DISAGGREGATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28150v1#S4`；Evaluation：`https://arxiv.org/html/2607.28150v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28150v1#S4.SS4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-PD-DISAGGREGATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28150:end -->

<!-- review:SF-2026-ARXIV-2607-28336:start -->
#### Perception Credit Distillation

<!-- claim:SF-2026-ARXIV-2607-28336:start -->The two-witness allocation improves the single author setup and exposes token-specific control. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28336:end -->

**旧方案与约束变化。** `本章的核心判断是：**SFT 用高质量 `(instruction, response)` demonstrations 重新加权模型的条件生成行为，使“用户请求后应该怎样回答”成为训练分布中的高概率模式。**它主要教模型模仿目标行为，不等于证明回答正确，也不能表达所有相对偏好。`（`books/part-04-training-system/29-sft.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Shared-perception rollouts estimate PSR; teacher/student aware-span KL is a second witness; soft-AND deficiency reallocates a fixed distillation budget while DAPO stays separate. 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28336v1#S3; https://arxiv.org/html/2607.28336v1#S3.SS1; https://arxiv.org/html/2607.28336v1#S3.SS6`；Evaluation：`https://arxiv.org/html/2607.28336v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28336v1#S4.SS5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28336:end -->

<!-- review:SF-2026-ARXIV-2607-28415:start -->
#### QQWorld

<!-- claim:SF-2026-ARXIV-2607-28415:start -->QQ objective supplies stronger gradients in the tested environments; detached history can reduce memory. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28415:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Differentiable quantile-quantile matching replaces characteristic functions; a detached cross-batch queue enlarges rank statistics. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28415v1#S3; https://arxiv.org/html/2607.28415v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.28415v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28415v1#S4.SS6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28415:end -->

<!-- review:SF-2026-ARXIV-2607-28418:start -->
#### WIDE

<!-- claim:SF-2026-ARXIV-2607-28418:start -->The co-designed route avoids the measured gather/scatter failure in the author setup. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28418:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Routers select head/channel groups; columns sort masks/indices; fused CuTe kernels skip blocks/loads/MMA and scatter epilogue; separate phase kernels and dense fallback. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28418v1#S3`；Evaluation：`https://arxiv.org/html/2607.28418v1#S4.SS1; https://arxiv.org/html/2607.28418v1#S4.SS2; https://arxiv.org/html/2607.28418v1#S4.SS3; https://arxiv.org/html/2607.28418v1#S4.SS4; https://arxiv.org/html/2607.28418v1#A1; https://arxiv.org/html/2607.28418v1#A2; https://arxiv.org/html/2607.28418v1#A3`；Limitations/Counterevidence：`Not Disclosed — exact v1 has no dedicated limitations section; unsupported shapes, metadata cost and production tail-SLO remain untested boundaries, not claims attributed to §4.4.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28418:end -->

<!-- review:SF-2026-ARXIV-2607-28495:start -->
#### Stage-Replay Divergence Follows the KV Cache

<!-- claim:SF-2026-ARXIV-2607-28495:start -->At tested boundaries the cache is a sufficient carrier of observed divergence. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28495:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Fixed-prefix controls isolate precision; bidirectional all-layer KV transplantation swaps outcomes between otherwise identical replays. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28495v1#S3`；Evaluation：`https://arxiv.org/html/2607.28495v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28495v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28495:end -->

<!-- review:SF-2026-ARXIV-2607-28624:start -->
#### PhiZero

<!-- claim:SF-2026-ARXIV-2607-28624:start -->The factorization supports tested generation/understanding and transfer cases. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28624:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Q-Former+FSQ learns discrete physical-language transitions; a VLM predicts tokens from frame/action intent; diffusion decoder renders future conditioned on current appearance. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28624v1#S3`；Evaluation：`https://arxiv.org/html/2607.28624v1#S4; https://arxiv.org/html/2607.28624v1#A2; https://arxiv.org/html/2607.28624v1#A3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28624v1#A5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28624:end -->

<!-- review:SF-2026-ARXIV-2607-28884:start -->
#### Hollow-LLM Attack

<!-- claim:SF-2026-ARXIV-2607-28884:start -->The constructed witnesses satisfy the declared relation while hiding trivial capacity in the tested circuit. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-28884:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Depth attack adds zero-work residual identities; width attack replicates coordinates with block-diagonal weights while preserving logits. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.28884v1#S3; https://arxiv.org/html/2607.28884v1#S4`；Evaluation：`https://arxiv.org/html/2607.28884v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.28884v1#S6; https://arxiv.org/html/2607.28884v1#Sx2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-28884:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27694 | WikiText-2 and LM-Eval/MT-Bench; RTL model | LLaMA-1/2 7B/13B; LLaMA-3 8B | RTL-synthesized Samsung 28nm 1GHz + modeled DDR4 | W4A4KV4; INT8 scale/zero-point; FP16 output | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | LM-Eval-Harness; MT-Bench LLM judge |
| SF-2026-ARXIV-2607-27704 | WikiText-2 PPL and MT-Bench | LLaMA-2 7B/13B; LLaMA-3 8B | 28nm CMOS synthesis, 250MHz, 0.9V, 1430KB SRAM | INT4 activations/weights/KV; selected FP16 attention subops | prefill 128 for energy figure | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | WikiText-2 PPL; MT-Bench LLM judge |
| SF-2026-ARXIV-2607-27773 | Rollback-adapted LoCoMo and MemoryAgentBench | three comparable backbones; Llama-3.1-8B shown | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Recall@1/5, Scope@2, QA F1, ROUGE-1 |
| SF-2026-ARXIV-2607-27782 | LIBERO suites and three real dual-arm tasks | Not Disclosed in exact-v1; no inference made | Agilex Cobot Magic with three cameras; training hardware ND | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | behavior-cloning pretraining: micro-batch 128, global batch 2048; RedFlow adaptation: batch 32 | offline; no online concurrency | Not Disclosed in exact-v1; no inference made | 500 episodes/suite; 100 episodes/real task |
| SF-2026-ARXIV-2607-27834 | Source admission with 179 hard negatives and 60 supported originals; FactConsolidation; LongMemEval-S/LoCoMo-derived recovery | 10 local + 2 API configs; 12 answer configs | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; dataset/example counts are not execution batch size | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | deterministic accept/reject, F1 and state equality |
| SF-2026-ARXIV-2607-27933 | Eight model×robot-benchmark settings; online failure detection; calibration uses 50 held-out successful rollouts per setting | Includes π0.5; remaining exact model list in paper evaluation | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; calibration-set size and per-decision sampling are not execution batch size | Not Disclosed in exact-v1; no inference made | target FPR 0.1; no latency SLO | failure detection and lead-time at target FPR 0.1; baseline decision estimate uses K=32 repeated samples |
| SF-2026-ARXIV-2607-27967 | MARS-Bench, Overcooked, Pistonball | MAPPO; Gemini-2.5-Pro; GPT-5.1/Qwen3-VL comparisons | i7-14700K, RTX3090 24GB; four RTX3090 for local judge | Not Disclosed in exact-v1; no inference made | MARS egocentric 128x128x4; episode max 2000 steps | Not Disclosed in exact-v1; no inference made | one query/comparison | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | task success; standard error |
| SF-2026-ARXIV-2607-28699 | offline retrieval/long-CoT; serving/RULER over 1000 requests; certificate validation over 50 prompts | Qwen2.5-7B, Mistral-7B, Yi-1.5-6B | 8×H200 for adaptive/cross-generation serving | Not Disclosed in exact-v1; no inference made | prefill 4096; long tests to 128K | decode 64 | validation batch=2 (§6.2.3); request count and dither repetitions are evaluation population, not serving batch size | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | attention/output risk, RULER-4k and violation counts; probabilistic check repeats 20 dither seeds per prompt |
| SF-2026-ARXIV-2607-28150 | LongBench MultiFieldQA/GovReport/SAMSum/LCC | Qwen3, Llama-3.1, Gemma-3, Phi-4 | 3 Alibaba gn8is Prefill + 1 gn8is Decode; PCIe4/eRDMA | Not disclosed for weights/KV | avg prompt 7K/10K/9K/3K | 64 tokens | max 60K input tokens across batch | DP up to 6; online arrival concurrency ND | TTST/TBT reported; no production threshold | LongBench metrics plus cumulative per-token latency |
| SF-2026-ARXIV-2607-28336 | Geo3K training and eight multimodal reasoning evaluations | Qwen3-VL 8B→2B and 32B→8B | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | 8 trajectories per prompt (a=2,b=4) | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | binary verifier Avg@8 and unweighted 8-dataset macro |
| SF-2026-ARXIV-2607-28415 | Four world-model environments and physical-state probing | QQWorld plus LeWM/Sub-JEPA/SD-JEPA/SMWM baselines | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | N=32 with 0/2/history queues; comparisons include N=128 | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | six seeds; reconstruction/prediction and physical-state probes |
| SF-2026-ARXIV-2607-28418 | lm-eval quality and kernel/end-to-end traces | Llama3.1-8B, Llama3.2-3B | 4×A100-SXM4-40G training; RTX5090 inference | Not Disclosed in exact-v1; no inference made | training/eval 4096; trace B=1,T=16384 | Not Disclosed in exact-v1; no inference made | training 16; trace 1 | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | lm-eval-harness; TFLOPs and end-to-end latency |
| SF-2026-ARXIV-2607-28495 | GPQA Main fixed-prefix replay/transplant | Qwen2.5-14B-Instruct-derived 14B checkpoint | Not Disclosed in exact-v1; no inference made | BF16/FP32 | 1025–5080 prefix tokens | branch/merge/answer caps 768/512/64 | duplicate batch=2 | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | 200-row holdout; 20k paired bootstraps; 32-row transplant |
| SF-2026-ARXIV-2607-28624 | 5M video clips, physical benchmarks, robot/driving and motion transfer | PhiZero components; size ND | 128×NVIDIA A100 | Not Disclosed in exact-v1; no inference made | 4-second clips, 8 FPS; 512x896 first frame | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Physics-IQ/PhyGround/WorldModelBench; released judges; IntPhys2/LikePhys/YoCausal |
| SF-2026-ARXIV-2607-28884 | synthetic GPT-2-like structural ZK configurations | inner 6-layer d512 vs declared 12-layer d1024 | Ubuntu 24.04, Intel Core Ultra 7 265F CPU, 20 cores | Not Disclosed in exact-v1; no inference made | fixed prompt T=64 | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | Not Disclosed in exact-v1; no inference made | zkGPT-derived verifier; identical outputs/perplexity; normalized serve/prove cost |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27694 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 只有作者 RTL/model contract，而非 request certificate；system reach 延伸到专用 accelerator；durability 依赖硬件落地；evidence stability 受 modeled 28nm datapath 限制；narrative overlap 是同属 low-bit compression evidence，故不占独立长叙事。 | analysis-decision:SF-2026-ARXIV-2607-27694 |
| SF-2026-ARXIV-2607-27704 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 是局部旋转后的作者精度/能耗结果；system reach 停在静态量化预处理；durability 低于带 fallback 的运行时 gate；evidence stability 受 modeled hardware 限制；narrative overlap 又被同 owner 的 GyRot numeric-plan 链涵盖。 | analysis-decision:SF-2026-ARXIV-2607-27704 |
| SF-2026-ARXIV-2607-27773 | score_7_9;potential_books_delta | selected | DA-20260731-01 | — | V2=9/9；Separating semantic selection from ID-based restore improves the tested rollback protocol.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260731-01 |
| SF-2026-ARXIV-2607-27782 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected PCD：correctness 依赖 progress estimate、clustering 与邻域正样本；system reach 落在 embodied offline correction；durability 受 embodiment/coverage 限制；evidence stability 只有 LIBERO 与三项实机任务；narrative overlap 是同属 outcome-to-credit authority。 | analysis-decision:SF-2026-ARXIV-2607-27782 |
| SF-2026-ARXIV-2607-27834 | score_7_9;potential_books_delta | not_selected | — | — | 对比同 owner 的 selected ChronoMem：correctness 扩展到 admission、visibility 与 recovery；system reach 与 memory lifecycle 同级；durability 更依赖 before-image/invariant 实现；evidence stability 受作者自建 benchmark 限制；narrative overlap 是 rollback 后的事务增强。 | analysis-decision:SF-2026-ARXIV-2607-27834 |
| SF-2026-ARXIV-2607-27933 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected PCD：correctness 只在 success-calibrated FPR contract 下成立；system reach 是运行时几何 sensor 而非训练 authority；durability 受 policy/robot drift 限制；evidence stability 依赖八个作者 setting；narrative overlap 是共同处理 embodied failure signal。 | analysis-decision:SF-2026-ARXIV-2607-27933 |
| SF-2026-ARXIV-2607-27967 | forced_review;potential_books_delta | not_selected | — | — | 对比 selected PCD：correctness 更依赖 pairwise judge 而缺 shared-state intervention；system reach 扩到 multi-agent credit；durability 受 non-stationarity 限制；evidence stability 暴露 position/judge bias；narrative overlap 是同属 outcome-to-credit proposal。 | analysis-decision:SF-2026-ARXIV-2607-27967 |
| SF-2026-ARXIV-2607-28699 | score_7_9;potential_books_delta | selected | DA-20260731-03 | — | V2=9/9；Tier A is deterministic under stated quantizer class; Tier B is probabilistic for non-adaptive queries; tested gate detected sampled violations.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260731-03 |
| SF-2026-ARXIV-2607-28150 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 由 exact demand repair 而非 certificate 保底；system reach 跨越 PD 节点 data movement；durability 受 topology/importance drift 限制；evidence stability 只有作者集群；narrative overlap 仅在两者都操作 KV object。 | analysis-decision:SF-2026-ARXIV-2607-28150 |
| SF-2026-ARXIV-2607-28336 | score_7_9;potential_books_delta | selected | DA-20260731-02 | — | V2=8/9；The two-witness allocation improves the single author setup and exposes token-specific control.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260731-02 |
| SF-2026-ARXIV-2607-28415 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected PCD：correctness 是 current-batch gradient/history-detach estimator 边界；system reach 局限于 latent regularizer；durability 受 encoder drift 限制；evidence stability 来自四个作者环境；narrative overlap 只在两者都改变训练 credit signal。 | analysis-decision:SF-2026-ARXIV-2607-28415 |
| SF-2026-ARXIV-2607-28418 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 是 indexed kernel 对 routing mask 的实现一致性而非风险证书；system reach 更深入 execution kernel；durability 依赖 shape/GPU；evidence stability 受 RTX5090 与作者 kernel 限制；narrative overlap 是 compression execution path。 | analysis-decision:SF-2026-ARXIV-2607-28418 |
| SF-2026-ARXIV-2607-28495 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 由 fixed-prefix transplant 提供 causal localization；system reach 较窄，仅覆盖单模型 stage boundary；durability 依赖 construction identity；evidence stability 缺跨模型复现；narrative overlap 是它构成 WitCert gate 的 identity 前提。 | analysis-decision:SF-2026-ARXIV-2607-28495 |
| SF-2026-ARXIV-2607-28624 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected PCD：correctness 只有 generation/transfer 可用性而非 causal control；system reach 覆盖 representation→rendering；durability 取决于 tokenizer/reasoner/renderer identity；evidence stability 缺 closed-loop control；narrative overlap 较低但未形成更稳定 authority 结论。 | analysis-decision:SF-2026-ARXIV-2607-28624 |
| SF-2026-ARXIV-2607-28884 | score_7_9;potential_books_delta | not_selected | — | — | 对比 selected WitCert：correctness 是 equation proof 与 work proof 的反例区分；system reach 面向 security verifier；durability 较高；evidence stability 仅为 zkGPT-derived CPU construction；narrative overlap 是两者都在限定 certificate claim，故保留独立审计而不占长叙事。 | analysis-decision:SF-2026-ARXIV-2607-28884 |

<!-- analysis:DA-20260731-01:start -->
### ChronoMem

**旧方案为何合理。** Append/overwrite and retrieval are cheap and adequate for forward-only memory. Writable long-lived agents need version selection separated from deterministic restoration.（现有命题定位：`books/part-07-agent/77-memory.md#L14-L14`）

**约束变化与机制。** Immutable events and whole-memory snapshots form semantic commits; natural-language resolver selects a version, ID rollback restores and advances HEAD. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `AGENT-MEMORY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Whole-state consistency costs snapshots, single-writer constraints and index reconciliation. Failure modes: Wrong semantic target, best-effort index divergence, external effects survive, linear-history loss.

<!-- analysis:DA-20260731-01:end -->

<!-- analysis:DA-20260731-02:start -->
### Perception Credit Distillation

**旧方案为何合理。** Uniform outcome-weighted distillation is simple when all tokens contribute similarly. Multimodal reasoners need perception-specific credit without giving reward control of reasoning updates.（现有命题定位：`books/part-04-training-system/29-sft.md#L14-L14`）

**约束变化与机制。** Shared-perception rollouts estimate PSR; teacher/student aware-span KL is a second witness; soft-AND deficiency reallocates a fixed distillation budget while DAPO stays separate. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-SFT` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Sharper credit for extra grouped rollout/teacher cost and calibration dependence. Failure modes: Teacher wrong, PSR policy drift, threshold sensitivity, missing teacher probabilities.

<!-- analysis:DA-20260731-02:end -->

<!-- analysis:DA-20260731-03:start -->
### WitCert

**旧方案为何合理。** Static quantization is efficient when worst-case errors are acceptable. Adaptive serving needs a soundness-qualified meter, gate and fallback.（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）

**约束变化与机制。** Tier A deterministic RoPE-band residual witness applies to reconstructable per-token quantizers; Tier B gives a dithered INT8 sub-Gaussian certificate under non-adaptive queries and request delta budget. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Runtime safety signal and fallback for meter cost, looseness and scope limits. Failure modes: False fallback, undercovered adaptive query, quantizer outside class, delta-budget misuse.

<!-- analysis:DA-20260731-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27694:start -->《GyRot》已完成 Deep Source Review。对比 selected WitCert：correctness 只有作者 RTL/model contract，而非 request certificate；system reach 延伸到专用 accelerator；durability 依赖硬件落地；evidence stability 受 modeled 28nm datapath 限制；narrative overlap 是同属 low-bit compression evidence，故不占独立长叙事。<!-- analysis-decision:SF-2026-ARXIV-2607-27694:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27704:start -->《LightRot》已完成 Deep Source Review。对比 selected WitCert：correctness 是局部旋转后的作者精度/能耗结果；system reach 停在静态量化预处理；durability 低于带 fallback 的运行时 gate；evidence stability 受 modeled hardware 限制；narrative overlap 又被同 owner 的 GyRot numeric-plan 链涵盖。<!-- analysis-decision:SF-2026-ARXIV-2607-27704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27782:start -->《RedFlow》已完成 Deep Source Review。对比 selected PCD：correctness 依赖 progress estimate、clustering 与邻域正样本；system reach 落在 embodied offline correction；durability 受 embodiment/coverage 限制；evidence stability 只有 LIBERO 与三项实机任务；narrative overlap 是同属 outcome-to-credit authority。<!-- analysis-decision:SF-2026-ARXIV-2607-27782:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27834:start -->《MemTxn》已完成 Deep Source Review。对比同 owner 的 selected ChronoMem：correctness 扩展到 admission、visibility 与 recovery；system reach 与 memory lifecycle 同级；durability 更依赖 before-image/invariant 实现；evidence stability 受作者自建 benchmark 限制；narrative overlap 是 rollback 后的事务增强。<!-- analysis-decision:SF-2026-ARXIV-2607-27834:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27933:start -->《Flow-Matching Uncertainty Geometry》已完成 Deep Source Review。对比 selected PCD：correctness 只在 success-calibrated FPR contract 下成立；system reach 是运行时几何 sensor 而非训练 authority；durability 受 policy/robot drift 限制；evidence stability 依赖八个作者 setting；narrative overlap 是共同处理 embodied failure signal。<!-- analysis-decision:SF-2026-ARXIV-2607-27933:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27967:start -->《MARS-RA》已完成 Deep Source Review。对比 selected PCD：correctness 更依赖 pairwise judge 而缺 shared-state intervention；system reach 扩到 multi-agent credit；durability 受 non-stationarity 限制；evidence stability 暴露 position/judge bias；narrative overlap 是同属 outcome-to-credit proposal。<!-- analysis-decision:SF-2026-ARXIV-2607-27967:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28150:start -->《SmartGen》已完成 Deep Source Review。对比 selected WitCert：correctness 由 exact demand repair 而非 certificate 保底；system reach 跨越 PD 节点 data movement；durability 受 topology/importance drift 限制；evidence stability 只有作者集群；narrative overlap 仅在两者都操作 KV object。<!-- analysis-decision:SF-2026-ARXIV-2607-28150:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28415:start -->《QQWorld》已完成 Deep Source Review。对比 selected PCD：correctness 是 current-batch gradient/history-detach estimator 边界；system reach 局限于 latent regularizer；durability 受 encoder drift 限制；evidence stability 来自四个作者环境；narrative overlap 只在两者都改变训练 credit signal。<!-- analysis-decision:SF-2026-ARXIV-2607-28415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28418:start -->《WIDE》已完成 Deep Source Review。对比 selected WitCert：correctness 是 indexed kernel 对 routing mask 的实现一致性而非风险证书；system reach 更深入 execution kernel；durability 依赖 shape/GPU；evidence stability 受 RTX5090 与作者 kernel 限制；narrative overlap 是 compression execution path。<!-- analysis-decision:SF-2026-ARXIV-2607-28418:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28495:start -->《Stage-Replay Divergence Follows the KV Cache》已完成 Deep Source Review。对比 selected WitCert：correctness 由 fixed-prefix transplant 提供 causal localization；system reach 较窄，仅覆盖单模型 stage boundary；durability 依赖 construction identity；evidence stability 缺跨模型复现；narrative overlap 是它构成 WitCert gate 的 identity 前提。<!-- analysis-decision:SF-2026-ARXIV-2607-28495:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28624:start -->《PhiZero》已完成 Deep Source Review。对比 selected PCD：correctness 只有 generation/transfer 可用性而非 causal control；system reach 覆盖 representation→rendering；durability 取决于 tokenizer/reasoner/renderer identity；evidence stability 缺 closed-loop control；narrative overlap 较低但未形成更稳定 authority 结论。<!-- analysis-decision:SF-2026-ARXIV-2607-28624:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28884:start -->《Hollow-LLM Attack》已完成 Deep Source Review。对比 selected WitCert：correctness 是 equation proof 与 work proof 的反例区分；system reach 面向 security verifier；durability 较高；evidence stability 仅为 zkGPT-derived CPU construction；narrative overlap 是两者都在限定 certificate claim，故保留独立审计而不占长叙事。<!-- analysis-decision:SF-2026-ARXIV-2607-28884:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-27694 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-27694 | delta:SF-2026-ARXIV-2607-27694 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27694 |
| SF-2026-ARXIV-2607-27704 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-27704 | delta:SF-2026-ARXIV-2607-27704 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-27704 |
| SF-2026-ARXIV-2607-27773 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-27773 | delta:SF-2026-ARXIV-2607-27773 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27773 |
| SF-2026-ARXIV-2607-27782 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-27782 | delta:SF-2026-ARXIV-2607-27782 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27782 |
| SF-2026-ARXIV-2607-27834 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-27834 | delta:SF-2026-ARXIV-2607-27834 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27834 |
| SF-2026-ARXIV-2607-27933 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-27933 | delta:SF-2026-ARXIV-2607-27933 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27933 |
| SF-2026-ARXIV-2607-27967 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L14-L14; books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-27967 | delta:SF-2026-ARXIV-2607-27967 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-27967 |
| SF-2026-ARXIV-2607-28699 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-28699 | delta:SF-2026-ARXIV-2607-28699 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28699 |
| SF-2026-ARXIV-2607-28150 | INFER-PD-DISAGGREGATION | books/part-05-inference-system/55-pd-disaggregation.md#L1 | books/part-05-inference-system/54-gpu-memory.md#L14-L14; books/part-05-inference-system/56-inference-scheduling.md#L14-L14 | existing:SF-2026-ARXIV-2607-28150 | delta:SF-2026-ARXIV-2607-28150 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28150 |
| SF-2026-ARXIV-2607-28336 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/28-pretraining.md#L14-L14; books/part-04-training-system/30-lora.md#L14-L14 | existing:SF-2026-ARXIV-2607-28336 | delta:SF-2026-ARXIV-2607-28336 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28336 |
| SF-2026-ARXIV-2607-28415 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-28415 | delta:SF-2026-ARXIV-2607-28415 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28415 |
| SF-2026-ARXIV-2607-28418 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-28418 | delta:SF-2026-ARXIV-2607-28418 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28418 |
| SF-2026-ARXIV-2607-28495 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-28495 | delta:SF-2026-ARXIV-2607-28495 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28495 |
| SF-2026-ARXIV-2607-28624 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-28624 | delta:SF-2026-ARXIV-2607-28624 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28624 |
| SF-2026-ARXIV-2607-28884 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-28884 | delta:SF-2026-ARXIV-2607-28884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-28884 |

<!-- books-review:SF-2026-ARXIV-2607-27694:start --><!-- existing:SF-2026-ARXIV-2607-27694:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-27694:end --><!-- delta:SF-2026-ARXIV-2607-27694:start -->新增证据边界：CoRFiG decouples rotation R from group G; HAP aligns outliers; asymmetric scale/zero-point become INT8. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27694:end --><!-- books-review:SF-2026-ARXIV-2607-27694:end -->

<!-- books-review:SF-2026-ARXIV-2607-27704:start --><!-- existing:SF-2026-ARXIV-2607-27704:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-27704:end --><!-- delta:SF-2026-ARXIV-2607-27704:start -->新增证据边界：GLR uses hierarchical 16x8 FHT; ODA aligns calibrated outliers to a Hadamard direction. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-27704:end --><!-- books-review:SF-2026-ARXIV-2607-27704:end -->

<!-- books-review:SF-2026-ARXIV-2607-27773:start --><!-- existing:SF-2026-ARXIV-2607-27773:start -->对读 `books/part-07-agent/77-memory.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-27773:end --><!-- delta:SF-2026-ARXIV-2607-27773:start -->新增证据边界：Immutable events and whole-memory snapshots form semantic commits; natural-language resolver selects a version, ID rollback restores and advances HEAD. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27773:end --><!-- books-review:SF-2026-ARXIV-2607-27773:end -->

<!-- books-review:SF-2026-ARXIV-2607-27782:start --><!-- existing:SF-2026-ARXIV-2607-27782:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-27782:end --><!-- delta:SF-2026-ARXIV-2607-27782:start -->新增证据边界：A general reward model estimates smoothed progress; progress delta plus outcome signs chunks; HDBSCAN finds nearby positive corrective centroids; unsupported failures are suppressed. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27782:end --><!-- books-review:SF-2026-ARXIV-2607-27782:end -->

<!-- books-review:SF-2026-ARXIV-2607-27834:start --><!-- existing:SF-2026-ARXIV-2607-27834:start -->对读 `books/part-07-agent/77-memory.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-27834:end --><!-- delta:SF-2026-ARXIV-2607-27834:start -->新增证据边界：Ordered PatchTest admits source-supported updates; chronology resolver declares visible version; durable before-image restores complete active map after reopen. 该 delta 已进入 `books/part-07-agent/77-memory.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27834:end --><!-- books-review:SF-2026-ARXIV-2607-27834:end -->

<!-- books-review:SF-2026-ARXIV-2607-27933:start --><!-- existing:SF-2026-ARXIV-2607-27933:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-27933:end --><!-- delta:SF-2026-ARXIV-2607-27933:start -->新增证据边界：Deviation from affine-isotropic sink geometry links velocity Jacobian/posterior covariance to trajectory acceleration; prefix acceleration feeds calibrated CUSUM. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27933:end --><!-- books-review:SF-2026-ARXIV-2607-27933:end -->

<!-- books-review:SF-2026-ARXIV-2607-27967:start --><!-- existing:SF-2026-ARXIV-2607-27967:start -->对读 `books/part-07-agent/82-multi-agent.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/82-multi-agent.md#L14-L14`）为：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2607-27967:end --><!-- delta:SF-2026-ARXIV-2607-27967:start -->新增证据边界：LMM pairwise comparisons form a matrix; rank aggregation yields contribution credits; potential shaping feeds MAPPO. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-27967:end --><!-- books-review:SF-2026-ARXIV-2607-27967:end -->

<!-- books-review:SF-2026-ARXIV-2607-28699:start --><!-- existing:SF-2026-ARXIV-2607-28699:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-28699:end --><!-- delta:SF-2026-ARXIV-2607-28699:start -->新增证据边界：Tier A deterministic RoPE-band residual witness applies to reconstructable per-token quantizers; Tier B gives a dithered INT8 sub-Gaussian certificate under non-adaptive queries and request delta budget. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28699:end --><!-- books-review:SF-2026-ARXIV-2607-28699:end -->

<!-- books-review:SF-2026-ARXIV-2607-28150:start --><!-- existing:SF-2026-ARXIV-2607-28150:start -->对读 `books/part-05-inference-system/55-pd-disaggregation.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/55-pd-disaggregation.md#L14-L14`）为：本章的核心判断是：**PD 分离利用 Prefill 与 Decode 在计算、memory、batch 和 SLO 上的差异实现独立资源规划，但必须用 KV transfer、跨池排队和更大故障面支付代价；它是否成立取决于 workload-specific break-even。**<!-- existing:SF-2026-ARXIV-2607-28150:end --><!-- delta:SF-2026-ARXIV-2607-28150:start -->新增证据边界：Profiled proactive transfer, decode demand fetch and speculative prefetch cooperate; low load falls back to full transfer. 该 delta 已进入 `books/part-05-inference-system/55-pd-disaggregation.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28150:end --><!-- books-review:SF-2026-ARXIV-2607-28150:end -->

<!-- books-review:SF-2026-ARXIV-2607-28336:start --><!-- existing:SF-2026-ARXIV-2607-28336:start -->对读 `books/part-04-training-system/29-sft.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/29-sft.md#L14-L14`）为：本章的核心判断是：**SFT 用高质量 `(instruction, response)` demonstrations 重新加权模型的条件生成行为，使“用户请求后应该怎样回答”成为训练分布中的高概率模式。**它主要教模型模仿目标行为，不等于证明回答正确，也不能表达所有相对偏好。<!-- existing:SF-2026-ARXIV-2607-28336:end --><!-- delta:SF-2026-ARXIV-2607-28336:start -->新增证据边界：Shared-perception rollouts estimate PSR; teacher/student aware-span KL is a second witness; soft-AND deficiency reallocates a fixed distillation budget while DAPO stays separate. 该 delta 已进入 `books/part-04-training-system/29-sft.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28336:end --><!-- books-review:SF-2026-ARXIV-2607-28336:end -->

<!-- books-review:SF-2026-ARXIV-2607-28415:start --><!-- existing:SF-2026-ARXIV-2607-28415:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-28415:end --><!-- delta:SF-2026-ARXIV-2607-28415:start -->新增证据边界：Differentiable quantile-quantile matching replaces characteristic functions; a detached cross-batch queue enlarges rank statistics. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28415:end --><!-- books-review:SF-2026-ARXIV-2607-28415:end -->

<!-- books-review:SF-2026-ARXIV-2607-28418:start --><!-- existing:SF-2026-ARXIV-2607-28418:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-28418:end --><!-- delta:SF-2026-ARXIV-2607-28418:start -->新增证据边界：Routers select head/channel groups; columns sort masks/indices; fused CuTe kernels skip blocks/loads/MMA and scatter epilogue; separate phase kernels and dense fallback. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28418:end --><!-- books-review:SF-2026-ARXIV-2607-28418:end -->

<!-- books-review:SF-2026-ARXIV-2607-28495:start --><!-- existing:SF-2026-ARXIV-2607-28495:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-28495:end --><!-- delta:SF-2026-ARXIV-2607-28495:start -->新增证据边界：Fixed-prefix controls isolate precision; bidirectional all-layer KV transplantation swaps outcomes between otherwise identical replays. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28495:end --><!-- books-review:SF-2026-ARXIV-2607-28495:end -->

<!-- books-review:SF-2026-ARXIV-2607-28624:start --><!-- existing:SF-2026-ARXIV-2607-28624:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-28624:end --><!-- delta:SF-2026-ARXIV-2607-28624:start -->新增证据边界：Q-Former+FSQ learns discrete physical-language transitions; a VLM predicts tokens from frame/action intent; diffusion decoder renders future conditioned on current appearance. 该 delta 已进入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28624:end --><!-- books-review:SF-2026-ARXIV-2607-28624:end -->

<!-- books-review:SF-2026-ARXIV-2607-28884:start --><!-- existing:SF-2026-ARXIV-2607-28884:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-28884:end --><!-- delta:SF-2026-ARXIV-2607-28884:start -->新增证据边界：Depth attack adds zero-work residual identities; width attack replicates coordinates with block-diagonal weights while preserving logits. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-28884:end --><!-- books-review:SF-2026-ARXIV-2607-28884:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260731-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260731; semantic-review:SA-20260731-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260731-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-27694; review:SF-2026-ARXIV-2607-27704; review:SF-2026-ARXIV-2607-27773; review:SF-2026-ARXIV-2607-27782; review:SF-2026-ARXIV-2607-27834; review:SF-2026-ARXIV-2607-27933; review:SF-2026-ARXIV-2607-27967; review:SF-2026-ARXIV-2607-28699; review:SF-2026-ARXIV-2607-28150; review:SF-2026-ARXIV-2607-28336; review:SF-2026-ARXIV-2607-28415; review:SF-2026-ARXIV-2607-28418; review:SF-2026-ARXIV-2607-28495; review:SF-2026-ARXIV-2607-28624; review:SF-2026-ARXIV-2607-28884; semantic-review:SA-20260731-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260731-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260731-01; analysis:DA-20260731-02; analysis:DA-20260731-03; semantic-review:SA-20260731-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260731-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-27694; books-review:SF-2026-ARXIV-2607-27704; books-review:SF-2026-ARXIV-2607-27773; books-review:SF-2026-ARXIV-2607-27782; books-review:SF-2026-ARXIV-2607-27834; books-review:SF-2026-ARXIV-2607-27933; books-review:SF-2026-ARXIV-2607-27967; books-review:SF-2026-ARXIV-2607-28699; books-review:SF-2026-ARXIV-2607-28150; books-review:SF-2026-ARXIV-2607-28336; books-review:SF-2026-ARXIV-2607-28415; books-review:SF-2026-ARXIV-2607-28418; books-review:SF-2026-ARXIV-2607-28495; books-review:SF-2026-ARXIV-2607-28624; books-review:SF-2026-ARXIV-2607-28884; semantic-review:SA-20260731-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260731-COVERAGE:start -->Fresh-context audit independently replayed both archived Atom pages (2,000 + 539 entries) for the strict Beijing window [2026-07-30 09:00, 2026-07-31 09:00), verified 1,353 unique first-public arXiv v1 identities, recomputed the day-specific denominator SHA-256, and reconciled all fifteen routed families and first-public timestamps across replay, denominator, packet and Daily. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260731-COVERAGE:end -->
<!-- semantic-review:SA-20260731-EVIDENCE:start -->Fresh-context audit recomputed all fifteen durable exact-v1 snapshot SHA-256 digests; checked Method, Evaluation and Limitations/Counterevidence anchors against the actual v1 HTML; verified the reasoned Not Disclosed boundaries for GyRot and WIDE and RedFlow's dedicated Appendix F limitations; and revalidated all fifteen ten-field benchmark contracts, including RedFlow's disclosed 128/2048 and 32 batches, MemTxn and FlowFailure's non-batch population counts, and WitCert's Section 6.2.3 validation batch=2. All fifteen routes are Deep across review, preaudit, packet central receipts and Daily, and all fifteen Review Provenance IDs agree across packet review, packet central, shared ledger and Daily. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260731-EVIDENCE:end -->
<!-- semantic-review:SA-20260731-SELECTION:start -->Fresh-context audit verified fifteen source-specific pre-Books selection rationales with no Books disposition or Integration result used to reverse-justify narrative selection. Exactly three narrative units are selected and twelve are explicitly not selected; every non-selection names a selected comparison (ChronoMem, PCD or WitCert) and provides source-specific correctness, system-reach, durability, evidence-stability and narrative-overlap reasons. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260731-SELECTION:end -->
<!-- semantic-review:SA-20260731-BOOKS:start -->Fresh-context audit verified fourteen Integrate decisions and one No Change — Existing Coverage decision against the actual canonical owner chapters and Daily review notes. Thirteen newly added owner paragraphs each have exactly one exact-v1 source note; WitCert remains idempotent with one paragraph and one source note; LightRot adds no duplicate paragraph; and Ch77 preserves ChronoMem before MemTxn. The text retains old-solution validity, changed constraints, mechanism/state ownership, trade-offs, failure boundaries and evidence scope. Books PASS; finding_count=0.<!-- semantic-review:SA-20260731-BOOKS:end -->

## 8. Ignored Noise

1353 个窗口内 identity 中，1338 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：14 个 `Integrate`，1 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 15 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/31/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/25-multimodal-world-models.md`、`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-04-training-system/29-sft.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/55-pd-disaggregation.md`、`books/part-06-ai-infrastructure/72-security.md`、`books/part-07-agent/77-memory.md`、`books/part-07-agent/82-multi-agent.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [GyRot](https://arxiv.org/abs/2607.27694v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [LightRot](https://arxiv.org/abs/2607.27704v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [ChronoMem](https://arxiv.org/abs/2607.27773v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [RedFlow](https://arxiv.org/abs/2607.27782v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [MemTxn](https://arxiv.org/abs/2607.27834v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [Flow-Matching Uncertainty Geometry](https://arxiv.org/abs/2607.27933v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [MARS-RA](https://arxiv.org/abs/2607.27967v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [WitCert](https://arxiv.org/abs/2607.28699v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [SmartGen](https://arxiv.org/abs/2607.28150v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [Perception Credit Distillation](https://arxiv.org/abs/2607.28336v1) — first-public（Asia/Shanghai）：2026-07-30；accessed：2026-08-27
- [QQWorld](https://arxiv.org/abs/2607.28415v1) — first-public（Asia/Shanghai）：2026-07-31；accessed：2026-08-27
- [WIDE](https://arxiv.org/abs/2607.28418v1) — first-public（Asia/Shanghai）：2026-07-31；accessed：2026-08-27
- [Stage-Replay Divergence Follows the KV Cache](https://arxiv.org/abs/2607.28495v1) — first-public（Asia/Shanghai）：2026-07-31；accessed：2026-08-27
- [PhiZero](https://arxiv.org/abs/2607.28624v1) — first-public（Asia/Shanghai）：2026-07-31；accessed：2026-08-27
- [Hollow-LLM Attack](https://arxiv.org/abs/2607.28884v1) — first-public（Asia/Shanghai）：2026-07-31；accessed：2026-08-27
- [July recovery snapshot](../_sources/arxiv-v2.1-replay-20260727-31/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
