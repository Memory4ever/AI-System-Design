# Daily Research — 2026-07-17

**Research Date:** 2026-07-17

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-16 09:00:00 ～ 2026-07-17 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1066 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 16 个。当前路由账目为 15 个 Deep、1 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-17 |
| Window End | 2026-07-17 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-17-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T00:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-16T09:00:00+08:00 | 2026-07-17T09:00:00+08:00 | 2026-08-27T00:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1066 | SF-2026-ARXIV-2607-14618<br>SF-2026-ARXIV-2607-14635<br>SF-2026-ARXIV-2607-14695<br>SF-2026-ARXIV-2607-14698<br>SF-2026-ARXIV-2607-14739<br>SF-2026-ARXIV-2607-14777<br>SF-2026-ARXIV-2607-14852<br>SF-2026-ARXIV-2607-14952<br>SF-2026-ARXIV-2607-15004<br>SF-2026-ARXIV-2607-15330<br>SF-2026-ARXIV-2607-15161<br>SF-2026-ARXIV-2607-15207<br>SF-2026-ARXIV-2607-15257<br>SF-2026-ARXIV-2607-15263<br>SF-2026-ARXIV-2607-15498<br>SF-2026-ARXIV-2607-15524 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-17T09:00:00+08:00 | coverage:SRC-ARXIV:20260717 | GAP-ARXIV-DIRECT-RESET-20260717 |

<!-- coverage:SRC-ARXIV:20260717:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1066 unique identities in this strict window; 16 routed families.<!-- coverage:SRC-ARXIV:20260717:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 16 个 family：exact v1 为 1 个 family 披露 artifact/evidence locator，其中 1 个提供外部 repository/project/demo locator，另有 15 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14618 | arXiv:2607.14618v1 | paper-v1:2607.14618 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14618 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-14618 | yes |
| SF-2026-ARXIV-2607-14635 | arXiv:2607.14635v1 | paper-v1:2607.14635 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14635 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-14635 | yes |
| SF-2026-ARXIV-2607-14695 | arXiv:2607.14695v1 | paper-v1:2607.14695 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14695 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-14695 | yes |
| SF-2026-ARXIV-2607-14698 | arXiv:2607.14698v1 | paper-v1:2607.14698 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14698 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-14698 | yes |
| SF-2026-ARXIV-2607-14739 | arXiv:2607.14739v1 | paper-v1:2607.14739 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14739 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-14739 | yes |
| SF-2026-ARXIV-2607-14777 | arXiv:2607.14777v1 | paper-v1:2607.14777 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14777 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-14777 | yes |
| SF-2026-ARXIV-2607-14852 | arXiv:2607.14852v1 | paper-v1:2607.14852 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14852 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607-14852 | yes |
| SF-2026-ARXIV-2607-14952 | arXiv:2607.14952v1 | paper-v1:2607.14952 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14952 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2607-14952 | yes |
| SF-2026-ARXIV-2607-15004 | arXiv:2607.15004v1 | paper-v1:2607.15004 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-15004 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15004 | yes |
| SF-2026-ARXIV-2607-15330 | arXiv:2607.15330v1 | paper-v1:2607.15330 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15330 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15330 | yes |
| SF-2026-ARXIV-2607-15161 | arXiv:2607.15161v1 | paper-v1:2607.15161 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15161 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15161 | yes |
| SF-2026-ARXIV-2607-15207 | arXiv:2607.15207v1 | paper-v1:2607.15207 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15207 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15207 | yes |
| SF-2026-ARXIV-2607-15257 | arXiv:2607.15257v1 | paper-v1:2607.15257 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15257 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15257 | yes |
| SF-2026-ARXIV-2607-15263 | arXiv:2607.15263v1 | paper-v1:2607.15263 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15263 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-15263 | yes |
| SF-2026-ARXIV-2607-15498 | arXiv:2607.15498v1 | paper-v1:2607.15498 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15498 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-15498 | yes |
| SF-2026-ARXIV-2607-15524 | arXiv:2607.15524v1 | paper-v1:2607.15524 | 2026-W29 | 2026-07-17 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-15524 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15524 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14618 | RP-318d3ccbb793222a | deep | arXiv:2607.14618v1 | SRC-ARXIV@arXiv:2607.14618v1 | arXiv:2607.14618v1#S3; arXiv:2607.14618v1#S3.SS1; arXiv:2607.14618v1#S3.SS4; arXiv:2607.14618v1#S4 | arXiv:2607.14618v1#S5; arXiv:2607.14618v1#S5.SS1; arXiv:2607.14618v1#S5.SS5 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-14618 | complete |
| SF-2026-ARXIV-2607-14635 | RP-52f5733b8c552b09 | deep | arXiv:2607.14635v1 | SRC-ARXIV@arXiv:2607.14635v1 | arXiv:2607.14635v1#S3 | arXiv:2607.14635v1#S4; arXiv:2607.14635v1#S4.SS1; arXiv:2607.14635v1#S4.SS2; arXiv:2607.14635v1#S5 | arXiv:2607.14635v1#S6 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-14635 | complete |
| SF-2026-ARXIV-2607-14695 | RP-bd17e1923c8d90da | deep | arXiv:2607.14695v1 | SRC-ARXIV@arXiv:2607.14695v1 | arXiv:2607.14695v1#S3; arXiv:2607.14695v1#S3.SS1; arXiv:2607.14695v1#S3.SS3; arXiv:2607.14695v1#S3.SS4 | arXiv:2607.14695v1#S4; arXiv:2607.14695v1#S4.SS1; arXiv:2607.14695v1#S4.SS2; arXiv:2607.14695v1#S4.SS6 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Required — event-time artifact receipt was not reviewed and the repository is not part of the retained technical claim | claim:SF-2026-ARXIV-2607-14695 | complete |
| SF-2026-ARXIV-2607-14698 | RP-d6624c0e275079d1 | deep | arXiv:2607.14698v1 | SRC-ARXIV@arXiv:2607.14698v1 | arXiv:2607.14698v1#S3; arXiv:2607.14698v1#S3.SS2; arXiv:2607.14698v1#S3.SS3 | arXiv:2607.14698v1#S4; arXiv:2607.14698v1#S4.SS1; arXiv:2607.14698v1#S5; arXiv:2607.14698v1#S5.SS3 | arXiv:2607.14698v1#S6 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-14698 | complete |
| SF-2026-ARXIV-2607-14739 | RP-0d8a8bd3b6a81dfd | deep | arXiv:2607.14739v1 | SRC-ARXIV@arXiv:2607.14739v1 | arXiv:2607.14739v1#S3; arXiv:2607.14739v1#S3.SS2; arXiv:2607.14739v1#S3.SS4; arXiv:2607.14739v1#S3.SS5 | arXiv:2607.14739v1#S4; arXiv:2607.14739v1#S4.SS1; arXiv:2607.14739v1#S4.SS3 | arXiv:2607.14739v1#S5 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-14739 | complete |
| SF-2026-ARXIV-2607-14777 | RP-681808ed2f97b009 | deep | arXiv:2607.14777v1 | SRC-ARXIV@arXiv:2607.14777v1 | arXiv:2607.14777v1#S3; arXiv:2607.14777v1#S3.SS1; arXiv:2607.14777v1#S3.SS3 | arXiv:2607.14777v1#S4; arXiv:2607.14777v1#S4.SS1; arXiv:2607.14777v1#S4.SS6 | arXiv:2607.14777v1#A5 | Not Required — event-time artifact receipt was not reviewed and the repository is not part of the retained technical claim | claim:SF-2026-ARXIV-2607-14777 | complete |
| SF-2026-ARXIV-2607-14852 | RP-76a09cbc51e44772 | deep | arXiv:2607.14852v1 | SRC-ARXIV@arXiv:2607.14852v1 | arXiv:2607.14852v1#S4; arXiv:2607.14852v1#S4.SS1; arXiv:2607.14852v1#S4.SS2 | arXiv:2607.14852v1#S5; arXiv:2607.14852v1#S5.SS0.SSS0.Px1; arXiv:2607.14852v1#S5.SS2; arXiv:2607.14852v1#S5.SS3 | arXiv:2607.14852v1#S7 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-14852 | complete |
| SF-2026-ARXIV-2607-14952 | RP-0e3cb8f8794e5833 | deep | arXiv:2607.14952v1 | SRC-ARXIV@arXiv:2607.14952v1 | arXiv:2607.14952v1#S2; arXiv:2607.14952v1#S3; arXiv:2607.14952v1#S4; arXiv:2607.14952v1#S7 | arXiv:2607.14952v1#S7; arXiv:2607.14952v1#S9; arXiv:2607.14952v1#S9.SS8 | arXiv:2607.14952v1#S12 | Not Required — event-time artifact receipt was not reviewed and the repository is not part of the retained technical claim | claim:SF-2026-ARXIV-2607-14952 | complete |
| SF-2026-ARXIV-2607-15004 | RP-bd923fd105b07687 | standard | arXiv:2607.15004v1 | SRC-ARXIV@arXiv:2607.15004v1 | arXiv:2607.15004v1#S3; arXiv:2607.15004v1#S4; arXiv:2607.15004v1#S4.SS2; arXiv:2607.15004v1#S4.SS3 | arXiv:2607.15004v1#S5; arXiv:2607.15004v1#S5.SS1; arXiv:2607.15004v1#S5.SS3 | arXiv:2607.15004v1#S7 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-15004 | complete |
| SF-2026-ARXIV-2607-15330 | RP-7c24781a868e4d5e | deep | arXiv:2607.15330v1 | SRC-ARXIV@arXiv:2607.15330v1 | arXiv:2607.15330v1#S2; arXiv:2607.15330v1#S2.SS2.SSS1; arXiv:2607.15330v1#S2.SS2.SSS2 | arXiv:2607.15330v1#S3; arXiv:2607.15330v1#S3.SS1; arXiv:2607.15330v1#S3.SS2 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-15330 | complete |
| SF-2026-ARXIV-2607-15161 | RP-316d3e8c302cfaba | deep | arXiv:2607.15161v1 | SRC-ARXIV@arXiv:2607.15161v1 | arXiv:2607.15161v1#S2; arXiv:2607.15161v1#S2.SS1; arXiv:2607.15161v1#S2.SS2 | arXiv:2607.15161v1#S3; arXiv:2607.15161v1#S3.SS1; arXiv:2607.15161v1#S3.SS3; arXiv:2607.15161v1#S3.SS4 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | https://github.com/naver-ai/opd2 is post-window artifact verification and does not change v1 event date. | claim:SF-2026-ARXIV-2607-15161 | complete |
| SF-2026-ARXIV-2607-15207 | RP-e62f008d1e3ca990 | deep | arXiv:2607.15207v1 | SRC-ARXIV@arXiv:2607.15207v1 | arXiv:2607.15207v1#S3; arXiv:2607.15207v1#S4 | arXiv:2607.15207v1#S5; arXiv:2607.15207v1#S5.SS1; arXiv:2607.15207v1#S5.SS5; arXiv:2607.15207v1#S5.SS8 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Required — event-time artifact receipt was not reviewed and the repository is not part of the retained technical claim | claim:SF-2026-ARXIV-2607-15207 | complete |
| SF-2026-ARXIV-2607-15257 | RP-6a08121381495be7 | deep | arXiv:2607.15257v1 | SRC-ARXIV@arXiv:2607.15257v1 | arXiv:2607.15257v1#S3; arXiv:2607.15257v1#S3.SS1; arXiv:2607.15257v1#S3.SS4 | arXiv:2607.15257v1#S4; arXiv:2607.15257v1#S4.SS3; arXiv:2607.15257v1#S5; arXiv:2607.15257v1#S5.SS4 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Required — event-time artifact receipt was not reviewed and the repository is not part of the retained technical claim | claim:SF-2026-ARXIV-2607-15257 | complete |
| SF-2026-ARXIV-2607-15263 | RP-c0956cf1b99c6480 | deep | arXiv:2607.15263v1 | SRC-ARXIV@arXiv:2607.15263v1 | arXiv:2607.15263v1#S3 | arXiv:2607.15263v1#S4; arXiv:2607.15263v1#S5; arXiv:2607.15263v1#S6; arXiv:2607.15263v1#A2 | arXiv:2607.15263v1#S7; arXiv:2607.15263v1#S8 | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-15263 | complete |
| SF-2026-ARXIV-2607-15498 | RP-82a07cd924a5b231 | deep | arXiv:2607.15498v1 | SRC-ARXIV@arXiv:2607.15498v1 | arXiv:2607.15498v1#S3; arXiv:2607.15498v1#S3.SS1; arXiv:2607.15498v1#S3.SS2 | arXiv:2607.15498v1#S4; arXiv:2607.15498v1#S4.SS1; arXiv:2607.15498v1#S4.SS5; arXiv:2607.15498v1#A1.SS15 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-15498 | complete |
| SF-2026-ARXIV-2607-15524 | RP-c6ed6b7ced8af14c | deep | arXiv:2607.15524v1 | SRC-ARXIV@arXiv:2607.15524v1 | arXiv:2607.15524v1#S3; arXiv:2607.15524v1#S3.SS1; arXiv:2607.15524v1#S3.SS3 | arXiv:2607.15524v1#S4; arXiv:2607.15524v1#S5; arXiv:2607.15524v1#S6 | Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors. | Not Disclosed — exact v1 links no public immutable author artifact | claim:SF-2026-ARXIV-2607-15524 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-14618:start -->
#### PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference

<!-- claim:SF-2026-ARXIV-2607-14618:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14618:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: uniform integer quantization -> fractional per-channel precision compiled into regular ISA quanta 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14618v1#S3; arXiv:2607.14618v1#S3.SS1; arXiv:2607.14618v1#S3.SS4; arXiv:2607.14618v1#S4`；Evaluation：`arXiv:2607.14618v1#S5; arXiv:2607.14618v1#S5.SS1; arXiv:2607.14618v1#S5.SS5`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14618:end -->

<!-- review:SF-2026-ARXIV-2607-14635:start -->
#### Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14635:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14635:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: direct action-loss rewriting of inherited representations -> mediated action-facing representation shaping 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14635v1#S3`；Evaluation：`arXiv:2607.14635v1#S4; arXiv:2607.14635v1#S4.SS1; arXiv:2607.14635v1#S4.SS2; arXiv:2607.14635v1#S5`；Limitations/Counterevidence：`arXiv:2607.14635v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14635:end -->

<!-- review:SF-2026-ARXIV-2607-14695:start -->
#### Reflex: Real-Time VLA Control through Streaming Inference

<!-- claim:SF-2026-ARXIV-2607-14695:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14695:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: stop-think-act VLA serving -> asynchronous observation/action streams with bounded freshness 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14695v1#S3; arXiv:2607.14695v1#S3.SS1; arXiv:2607.14695v1#S3.SS3; arXiv:2607.14695v1#S3.SS4`；Evaluation：`arXiv:2607.14695v1#S4; arXiv:2607.14695v1#S4.SS1; arXiv:2607.14695v1#S4.SS2; arXiv:2607.14695v1#S4.SS6`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14695:end -->

<!-- review:SF-2026-ARXIV-2607-14698:start -->
#### Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color

<!-- claim:SF-2026-ARXIV-2607-14698:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14698:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: broad color augmentation -> invariant-feature collapse diagnosis -> semantics-preserving perturbation training 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14698v1#S3; arXiv:2607.14698v1#S3.SS2; arXiv:2607.14698v1#S3.SS3`；Evaluation：`arXiv:2607.14698v1#S4; arXiv:2607.14698v1#S4.SS1; arXiv:2607.14698v1#S5; arXiv:2607.14698v1#S5.SS3`；Limitations/Counterevidence：`arXiv:2607.14698v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14698:end -->

<!-- review:SF-2026-ARXIV-2607-14739:start -->
#### FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-14739:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14739:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering: action supervision -> training-only future feature and point-motion auxiliary supervision 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14739v1#S3; arXiv:2607.14739v1#S3.SS2; arXiv:2607.14739v1#S3.SS4; arXiv:2607.14739v1#S3.SS5`；Evaluation：`arXiv:2607.14739v1#S4; arXiv:2607.14739v1#S4.SS1; arXiv:2607.14739v1#S4.SS3`；Limitations/Counterevidence：`arXiv:2607.14739v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14739:end -->

<!-- review:SF-2026-ARXIV-2607-14777:start -->
#### SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-14777:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14777:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: sparse outcome RL/static skills -> policy-synchronous hindsight-skill on-policy distillation 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14777v1#S3; arXiv:2607.14777v1#S3.SS1; arXiv:2607.14777v1#S3.SS3`；Evaluation：`arXiv:2607.14777v1#S4; arXiv:2607.14777v1#S4.SS1; arXiv:2607.14777v1#S4.SS6`；Limitations/Counterevidence：`arXiv:2607.14777v1#A5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1016-L1026`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14777:end -->

<!-- review:SF-2026-ARXIV-2607-14852:start -->
#### Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-14852:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14852:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: one-shot task adaptation -> dual-timescale adapters plus bounded stochastic replay 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14852v1#S4; arXiv:2607.14852v1#S4.SS1; arXiv:2607.14852v1#S4.SS2`；Evaluation：`arXiv:2607.14852v1#S5; arXiv:2607.14852v1#S5.SS0.SSS0.Px1; arXiv:2607.14852v1#S5.SS2; arXiv:2607.14852v1#S5.SS3`；Limitations/Counterevidence：`arXiv:2607.14852v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14852:end -->

<!-- review:SF-2026-ARXIV-2607-14952:start -->
#### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

<!-- claim:SF-2026-ARXIV-2607-14952:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-14952:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: full-context autograd residency -> detached prompt-state boundary plus short-suffix differentiable replay 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.14952v1#S2; arXiv:2607.14952v1#S3; arXiv:2607.14952v1#S4; arXiv:2607.14952v1#S7`；Evaluation：`arXiv:2607.14952v1#S7; arXiv:2607.14952v1#S9; arXiv:2607.14952v1#S9.SS8`；Limitations/Counterevidence：`arXiv:2607.14952v1#S12`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-14952:end -->

<!-- review:SF-2026-ARXIV-2607-15004:start -->
#### CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking

<!-- claim:SF-2026-ARXIV-2607-15004:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15004:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Principle Reuse: visible-target tracking -> belief/state recovery under long occlusion 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15004v1#S3; arXiv:2607.15004v1#S4; arXiv:2607.15004v1#S4.SS2; arXiv:2607.15004v1#S4.SS3`；Evaluation：`arXiv:2607.15004v1#S5; arXiv:2607.15004v1#S5.SS1; arXiv:2607.15004v1#S5.SS3`；Limitations/Counterevidence：`arXiv:2607.15004v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15004:end -->

<!-- review:SF-2026-ARXIV-2607-15330:start -->
#### Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories

<!-- claim:SF-2026-ARXIV-2607-15330:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15330:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: robot-only teleoperation scale -> embodiment-free trajectory breadth then robot alignment 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15330v1#S2; arXiv:2607.15330v1#S2.SS2.SSS1; arXiv:2607.15330v1#S2.SS2.SSS2`；Evaluation：`arXiv:2607.15330v1#S3; arXiv:2607.15330v1#S3.SS1; arXiv:2607.15330v1#S3.SS2`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L658-L709`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15330:end -->

<!-- review:SF-2026-ARXIV-2607-15161:start -->
#### On-Policy Delta Distillation

<!-- claim:SF-2026-ARXIV-2607-15161:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15161:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: absolute teacher imitation -> matched teacher/base reasoning delta with direction gate 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15161v1#S2; arXiv:2607.15161v1#S2.SS1; arXiv:2607.15161v1#S2.SS2`；Evaluation：`arXiv:2607.15161v1#S3; arXiv:2607.15161v1#S3.SS1; arXiv:2607.15161v1#S3.SS3; arXiv:2607.15161v1#S3.SS4`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L518-L558`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15161:end -->

<!-- review:SF-2026-ARXIV-2607-15207:start -->
#### BadWAM: When World-Action Models Dream Right but Act Wrong

<!-- claim:SF-2026-ARXIV-2607-15207:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15207:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: plausible imagined future as safety sensor -> synchronized imagination/action verification under adaptive attack 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15207v1#S3; arXiv:2607.15207v1#S4`；Evaluation：`arXiv:2607.15207v1#S5; arXiv:2607.15207v1#S5.SS1; arXiv:2607.15207v1#S5.SS5; arXiv:2607.15207v1#S5.SS8`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1027-L1036`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15207:end -->

<!-- review:SF-2026-ARXIV-2607-15257:start -->
#### SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration

<!-- claim:SF-2026-ARXIV-2607-15257:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15257:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: conversation-local multi-agent progress -> externalized schema/evidence/task state and continuous dispatch 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15257v1#S3; arXiv:2607.15257v1#S3.SS1; arXiv:2607.15257v1#S3.SS4`；Evaluation：`arXiv:2607.15257v1#S4; arXiv:2607.15257v1#S4.SS3; arXiv:2607.15257v1#S5; arXiv:2607.15257v1#S5.SS4`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L467-L517`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15257:end -->

<!-- review:SF-2026-ARXIV-2607-15263:start -->
#### Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents

<!-- claim:SF-2026-ARXIV-2607-15263:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15263:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: peak security success -> workload-specific success/cost/refusal operating curves with contamination controls 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15263v1#S3`；Evaluation：`arXiv:2607.15263v1#S4; arXiv:2607.15263v1#S5; arXiv:2607.15263v1#S6; arXiv:2607.15263v1#A2`；Limitations/Counterevidence：`arXiv:2607.15263v1#S7; arXiv:2607.15263v1#S8`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L764-L810`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-15263:end -->

<!-- review:SF-2026-ARXIV-2607-15498:start -->
#### VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs

<!-- claim:SF-2026-ARXIV-2607-15498:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15498:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Alternative Branch: delete low-salience tokens/uniform rank -> salience-weighted variable rank with nonzero token floor 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15498v1#S3; arXiv:2607.15498v1#S3.SS1; arXiv:2607.15498v1#S3.SS2`；Evaluation：`arXiv:2607.15498v1#S4; arXiv:2607.15498v1#S4.SS1; arXiv:2607.15498v1#S4.SS5; arXiv:2607.15498v1#A1.SS15`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-15498:end -->

<!-- review:SF-2026-ARXIV-2607-15524:start -->
#### Recursive Harness Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-15524:start -->作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-15524:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Alternative Branch: population/global harness search -> adjacent-revision local search with cached comparator 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`arXiv:2607.15524v1#S3; arXiv:2607.15524v1#S3.SS1; arXiv:2607.15524v1#S3.SS3`；Evaluation：`arXiv:2607.15524v1#S4; arXiv:2607.15524v1#S5; arXiv:2607.15524v1#S6`；Limitations/Counterevidence：`Not Disclosed — exact v1 provides no dedicated Limitations section; the retained boundary is inferred conservatively from the exact Method and Evaluation anchors.`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L559-L605`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-15524:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14618 | WikiText-2 perplexity, five downstream tasks, and batch-1 CPU prefill/decode/energy measurements under 3-6 average-bit budgets | Falcon-H1-3B, Llama-2-13B, Qwen3-32B; Llama-3-8B appears in the budget-fit motivation | AMD Ryzen 9 9950X, AMD Ryzen 7 7840U, Intel Processor N250; Ubuntu 24.04; RAPL energy | FP16 activations; weights selected per channel from 2/3/4/8/16-bit palette; group size 128 | 128 calibration sequences; evaluation sequence lengths are benchmark-defined | Decode length is table-scoped; no production request distribution disclosed | 1 for edge inference measurements | 1 request; multi-request concurrency Not Disclosed | No production SLO; latency, tokens/s and energy/token are author measurements | Author perplexity/task harness plus wall-clock and RAPL instrumentation |
| SF-2026-ARXIV-2607-14635 | zero-shot sim-to-real closed-loop ObjectNav over four real-scene scenarios plus fixed-instruction action probes | Direct-fusion baseline and Action QFormer sharing a pretrained Qwen2.5-VL backbone and matched downstream policy/action supervision | Not Disclosed | Not Disclosed | single current observation plus generated or fixed intermediate instruction; action horizon H=8 | intermediate instruction plus 8-step local-frame action trajectory | training effective batch is matched between compared variants; exact deployment batch Not Disclosed | Not Disclosed to the reported closed-loop trials | control frequency, tail latency and physical safety SLO Not Disclosed | instruction-direction correctness, instruction OOD rate, action-direction correctness, collisions and task success; small scenario-level trial counts |
| SF-2026-ARXIV-2607-14695 | LIBERO four suites, Kinetix dynamic control and three AgileX PiPer real-robot tasks; latency, reaction latency, stall, memory, success and stability ablations | Pi0.5, Pi0 (3.1B) and SmolVLA (500M) | NVIDIA RTX 4090 24GB primary; RTX 3090 24GB portability check; AgileX PiPer robot | BFloat16 backbone/gating with FP32 RMS statistics in AdaRMSNorm | 10-frame visual history by default, approximately 300 ms; 10 denoising steps | default action chunk 50; ablation 25/50/100 | 1 | one vision producer thread and one policy consumer thread; no multi-request serving concurrency | 50 Hz controller target; latency after 100 warm-up steps over 1000 chunks reported at p95; 0% stall is empirical in tested settings | LIBERO 10 tasks/suite x 50 episodes capped at 500 steps, Kinetix 100 episodes/task, and 20 episodes per real task per method; formal equality only for fixed-input partitioned attention |
| SF-2026-ARXIV-2607-14698 | LIBERO illumination attacks and grayscale diagnostics plus SO-101 color-invariant and color-dependent physical manipulation | SmolVLA; real-world branch also fine-tunes pi0.5 | MuJoCo simulation and 6-DoF SO-101 Arm Pro with wrist and third-person cameras; accelerator Not Disclosed | Not Disclosed | dual-camera/current-frame observations; temporal attack sequences not evaluated | closed-loop action trajectories; exact action horizon Not Disclosed | Not Disclosed | Not Disclosed | no control-frequency or tail-latency SLO disclosed | 500 episodes per LIBERO suite; 20 physical trials for color-invariant and 40 for color-dependent tasks; success and trajectory-error metrics |
| SF-2026-ARXIV-2607-14739 | LIBERO, RoboCasa GR-1 Tabletop and zero-shot LIBERO-Plus perturbation evaluation with component ablations | StarVLA-GR00T base with foresight tokens, EMA feature teacher, frozen point-tracker supervision and FCCA | training on 8 NVIDIA H20 with ZeRO-2; inference-cost measurement on one H20 | Not Disclosed | 224x224 images, 64 image tokens, 64 tracking queries, 16 foresight tokens; action horizon T=8 LIBERO and T=16 RoboCasa | 8- or 16-step action sequence depending on benchmark | training batch 12 LIBERO and 8 RoboCasa; inference benchmark batch 1 | 1 inference stream | no production SLO; latency averaged over 1000 runs after 50 warm-ups | 20 rollouts/task on LIBERO, 50/task on 24 RoboCasa tasks, 10,030 zero-shot LIBERO-Plus instances; author success-rate evaluation |
| SF-2026-ARXIV-2607-14777 | ALFWorld, WebShop, search QA and two visual agent environments with static-distillation and GRPO comparisons | Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, Qwen3-1.7B-Instruct; visual branch Qwen2.5-VL-3B; GLM-5.2 analyzer | 8 NVIDIA A800 80GB for training | Not Disclosed | environment trajectories and analyzer-produced hindsight skill; context caps Not Disclosed | analyzer capped at 4096 tokens; policy response caps are benchmark/configuration scoped | RL batch 16 on ALFWorld/WebShop and 128 on search QA; rollout group 8; 150 policy updates | 8 independent offline rollouts per selected SFT task; serving concurrency Not Applicable | no production latency/cost SLO | environment success metrics and benchmark-specific exact outcome checks; author ablations and training curves |
| SF-2026-ARXIV-2607-14852 | ten sequential LIBERO manipulation tasks with continual-learning, replay and joint-training comparisons | frozen PaliGemma/Gemma 2B backbone plus approximately 300M action decoder with fast/slow LoRA adapters | Not Disclosed | Not Disclosed | image-rich demonstrations; prefix/suffix split is method-defined | action trajectory horizon is benchmark/configuration scoped | Not Disclosed; 10k steps/task and 40k-step joint-training upper bound | Not Disclosed | no runtime latency, physical-safety or production SLO | LIBERO sequential-task success and forgetting/transfer measures; replay cache M=500, LoRA rank 16 |
| SF-2026-ARXIV-2607-14952 | fixed-budget long-context GRPO feasibility and replay for dense Qwen and MoE GLM training | Qwen3.6-27B and GLM-5.2 | 8 NVIDIA H20 for Qwen and 32 NVIDIA H20 for GLM | model/training precision is configuration-scoped; full precision identity must remain attached to each run receipt | up to 4.456M positions for Qwen and 2.097M for GLM in disclosed configurations | included in total position accounting; prompt/response split is run-scoped | GRPO group G=2 for Qwen and G=8 for GLM in highlighted receipts | distributed CP/EP run topology, not serving concurrency | no production SLO; elapsed time and allocated memory are reported, not utilization, energy or cost | author trace/capacity receipts and replay checks; missing Qwen CP dK/dV and GLM global DSA/CP gradient semantics remain outside the proof |
| SF-2026-ARXIV-2607-15004 | simulated UAV target tracking with open-loop and closed-loop evaluation, occlusion slices and model-size variants | CosFly-VLA 0.8B quantitative model; larger 2B/9B variants are not equivalently proven | Not Disclosed | Not Disclosed | spatial visual-language observations; exact temporal window Not Disclosed | tracking action/trajectory sequence; exact horizon Not Disclosed | Not Disclosed | Not Disclosed | no physical UAV latency, noise, safety or tail-SLO evidence | author open-loop and closed-loop simulator metrics with occlusion analysis; no real-world denominator |
| SF-2026-ARXIV-2607-15330 | data/model scaling, four simulation benchmarks, novel-environment zero-shot tests and real-robot adaptation | Xiaomi-Robotics-1 model family as disclosed in exact v1 | Not Disclosed for the complete evaluation matrix | Not Disclosed | multi-camera/robot trajectory context is model/configuration scoped | action horizon is benchmark/configuration scoped | Not Disclosed | Not Disclosed | control frequency, tail latency and production safety SLO Not Disclosed | author simulation and physical-robot task-success evaluation; vendor evidence without independent replication |
| SF-2026-ARXIV-2607-15161 | math, science and code reasoning over fourteen benchmarks with on-policy delta distillation and ablations | Qwen3 and Gemma-family students/teachers from 1.7B to 8B | Not Disclosed | Not Disclosed | benchmark prompts; maximum generated context 8k in the disclosed training recipe | maximum 8k | 100 updates; optimizer AdamW learning rate 5e-6; exact global batch table-scoped | vLLM rollout engine; production concurrency Not Disclosed | no serving SLO; extra compute and memory are author-reported training costs | benchmark exact/author scorers with top-k 1024 and matched teacher-base ablations; long-run lineage drift remains open |
| SF-2026-ARXIV-2607-15207 | closed-loop attacks against three world-action-model interfaces on LIBERO and RoboTwin, including transfer and defense ablations | paper-disclosed WAM/VLA targets; selected models trained on 8 NVIDIA H100 | 8 NVIDIA H100 for selected training; evaluation hardware otherwise table-scoped | Not Disclosed | current observation, imagined next state and replanning context | action proposal/replan sequence; exact action horizon model-scoped | Not Disclosed | Not Disclosed | no production control-frequency or tail-latency SLO | LIBERO/RoboTwin task success and attack metrics; epsilon 0.06, 8 optimization iterations and 17 queries per replan in highlighted contract |
| SF-2026-ARXIV-2607-15257 | open-domain multi-agent information seeking on WideSearch and GISA with state/dispatch ablations | GLM-5 agent roles and Qwen3.5-35B-A3B extractor | provider/runtime hardware Not Disclosed | Not Disclosed | live-search task and durable SOCM state; model context limits Not Disclosed | up to 50 orchestration iterations | best-of-three runs | 8 subagents with up to 20 searches per agent | 1800-second run limit; no production latency/cost SLO | WideSearch/GISA benchmark scorers with Max@3; live-search drift limits temporal comparability |
| SF-2026-ARXIV-2607-15263 | offensive Cybench CTFs and defensive BOTS v1 incident-investigation questions with cost/success/refusal analysis | paper-disclosed frontier and shared model/agent configurations accessed through provider APIs and OpenRouter | provider-managed and Not Disclosed | Not Disclosed | benchmark task/context lengths are suite and provider scoped | agent trajectory length is provider/tool-policy scoped | Cybench 39 tasks x 3 attempts x 3 epochs; BOTS v1 has 31 questions and 10,300 possible points | Not Disclosed | cost is measured from API pricing; no deployment latency SLO | sandboxed CTF outcomes and BOTS v1 scoring with uncertainty analyses; public-data contamination and observational non-random model matrix explicitly limit causal comparison |
| SF-2026-ARXIV-2607-15498 | LongBench sixteen tasks with matched 20% KV budget, quality comparisons, codec overhead and paired significance tests | Llama-3.1-8B-Instruct and Qwen2.5-7B with Mistral cross-check | single NVIDIA A100 for accuracy measurement | half-precision shared bases; compressed-rank representation is method-defined; full codec precision table-scoped | LongBench task contexts; 200 examples per task | greedy benchmark generation; task-specific caps | single-request accuracy path; 20,000 paired bootstrap/sign-test samples | 1; no continuous-batching or multi-tenant test | no production tail-latency SLO; codec time/cost only | LongBench task scorers and paired bootstrap/sign tests; result is a training-free experimental compression contract |
| SF-2026-ARXIV-2607-15524 | thirty synthetic open-ended ML-research repository tasks across finance, robotics and pharmacy | Claude Sonnet 4.6, Opus 4.7 and Opus 4.8 coding agents; evaluator configurations use GPT-5.5 max and Opus 4.7/4.8 xhigh | provider-managed and Not Disclosed | Not Disclosed | task prompts plus prompt-represented harness; judge input truncated to roughly 30-40% of evaluator context when necessary | complete repository deliverables; output-token usage measured but hard cap Not Disclosed | 30 tasks, two primary LLM judges and three seeds; Opus 4.7 uses six evaluator configurations | workflow-specific agent fan-out; no standardized serving concurrency | no production SLO; normalized provider cost, output tokens and cache read/write are reported | pairwise LLM-as-judge over task-specified artifacts with multi-evaluator/seed repetition; synthetic tasks, judge bias and task-local search constrain generalization |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14618 | score_7_9;potential_books_delta | not_selected | — | — | Its precision-to-layout-to-kernel contract is durable and Books-worthy, but remains a CPU quantization execution branch narrower than the selected training/control/evaluation lifecycle changes. | analysis-decision:SF-2026-ARXIV-2607-14618 |
| SF-2026-ARXIV-2607-14635 | score_7_9;potential_books_delta | not_selected | — | — | The action-facing representation mediator is an important experimental VLA interface, but its evidence is narrower in embodiment, hardware disclosure and safety than the selected streaming-control contract. | analysis-decision:SF-2026-ARXIV-2607-14635 |
| SF-2026-ARXIV-2607-14695 | score_7_9;potential_books_delta | selected | DA-20260717-01 | — | V2=9/9；作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260717-01 |
| SF-2026-ARXIV-2607-14698 | score_7_9;potential_books_delta | not_selected | — | — | The semantic-invariance failure is valuable security evidence, but it is a single illumination/color attack family and is better carried by its Full Review plus Ch72 integration. | analysis-decision:SF-2026-ARXIV-2607-14698 |
| SF-2026-ARXIV-2607-14739 | score_7_9;potential_books_delta | not_selected | — | — | Training-only foresight supervision clarifies the boundary to causal world state, but it does not alter deployed state ownership as broadly as the selected streaming VLA unit. | analysis-decision:SF-2026-ARXIV-2607-14739 |
| SF-2026-ARXIV-2607-14777 | score_7_9;potential_books_delta | not_selected | — | — | Policy-synchronous hindsight skill distillation is a meaningful GRPO branch, but its analyzer-derived signal is bounded by one agentic RL setup and remains subordinate to the broader fixed-budget state-lifetime change. | analysis-decision:SF-2026-ARXIV-2607-14777 |
| SF-2026-ARXIV-2607-14852 | score_7_9;potential_books_delta | not_selected | — | — | Fast/slow adapters and bounded replay add a continual-learning lifecycle branch, but the evidence remains a robotics-specific experimental realization without broad runtime or safety validation. | analysis-decision:SF-2026-ARXIV-2607-14852 |
| SF-2026-ARXIV-2607-14952 | score_7_9;potential_books_delta | selected | DA-20260717-02 | — | V2=9/9；作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260717-02 |
| SF-2026-ARXIV-2607-15330 | score_7_9;potential_books_delta | not_selected | — | — | This high-score family is already explicitly integrated in Ch26; re-narrating it would duplicate the breadth-to-embodiment-alignment chain rather than add a new report-level unit. | analysis-decision:SF-2026-ARXIV-2607-15330 |
| SF-2026-ARXIV-2607-15161 | score_7_9;potential_books_delta | not_selected | — | — | The matched teacher-base delta and sign gate are already integrated in Ch33; the Source Review closes evidence without duplicating the established mechanism narrative. | analysis-decision:SF-2026-ARXIV-2607-15161 |
| SF-2026-ARXIV-2607-15207 | score_7_9;potential_books_delta | not_selected | — | — | BadWAM is already integrated in Ch72 as an action/imagination decoupling attack; no new report-level narrative is needed after confirming exact-v1 boundaries. | analysis-decision:SF-2026-ARXIV-2607-15207 |
| SF-2026-ARXIV-2607-15257 | score_7_9;potential_books_delta | not_selected | — | — | SearchOS is a bounded implementation of durable typed workflow state and collaboration ownership already covered by Ch81/82; its Full Review remains complete. | analysis-decision:SF-2026-ARXIV-2607-15257 |
| SF-2026-ARXIV-2607-15263 | score_7_9;potential_books_delta | selected | DA-20260717-03 | — | V2=9/9；作者正文与实验支持限定 workload 内的机制和结果；系统演进与 Books 归属为本次审计推断，不扩大作者 claim。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260717-03 |
| SF-2026-ARXIV-2607-15498 | score_7_9;potential_books_delta | not_selected | — | — | Variable-rank KV compression is Books-worthy but stays within a single inference-state representation branch; the selected units have wider lifecycle and cross-Part reach. | analysis-decision:SF-2026-ARXIV-2607-15498 |
| SF-2026-ARXIV-2607-15524 | score_7_9;potential_books_delta | not_selected | — | — | Recursive harness self-improvement is already represented in Ch81 with cached adjacent comparison, evaluator-drift and local-optimum boundaries; selection would repeat existing coverage. | analysis-decision:SF-2026-ARXIV-2607-15524 |

<!-- analysis:DA-20260717-01:start -->
### Reflex: Real-Time VLA Control through Streaming Inference

**旧方案为何合理。** Sequential vision encode then action generation keeps state ownership simple, but its latency couples the slow visual path to the higher-frequency control loop.（现有命题定位：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）

**约束变化与机制。** Direct Evolution: stop-think-act VLA serving -> asynchronous observation/action streams with bounded freshness 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-EMBODIED-VLA` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Gains control frequency and overlap; pays freshness bookkeeping, predictor error, ring-buffer backpressure and harder failure recovery.

<!-- analysis:DA-20260717-01:end -->

<!-- analysis:DA-20260717-02:start -->
### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget

**旧方案为何合理。** Full-context autograd has the clearest gradient semantics, but prompt-length activations and MoE/attention scratch make fixed-device multi-million-token GRPO infeasible.（现有命题定位：`books/part-04-training-system/36-distributed-training.md#L14-L14`）

**约束变化与机制。** Direct Evolution: full-context autograd residency -> detached prompt-state boundary plus short-suffix differentiable replay 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-DISTRIBUTED-TRAINING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Fits fixed devices by shortening autograd lifetime; pays CPU traffic, recompute/serial replay and missing collective risks. Scale-out full-sequence training remains the stronger semantic baseline.

<!-- analysis:DA-20260717-02:end -->

<!-- analysis:DA-20260717-03:start -->
### Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents

**旧方案为何合理。** Peak success and token counts are easy to collect, but they conflate operating budget, refusal policy, workflow/tool cost and public-benchmark contamination.（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Direct Evolution: peak security success -> workload-specific success/cost/refusal operating curves with contamination controls 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Produces actionable cost-success curves; pays pricing/provider drift and trace accounting. Public SOC data still needs decontamination.

<!-- analysis:DA-20260717-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14618:start -->《PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference》已完成 Deep Source Review。Its precision-to-layout-to-kernel contract is durable and Books-worthy, but remains a CPU quantization execution branch narrower than the selected training/control/evaluation lifecycle changes.<!-- analysis-decision:SF-2026-ARXIV-2607-14618:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14635:start -->《Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models》已完成 Deep Source Review。The action-facing representation mediator is an important experimental VLA interface, but its evidence is narrower in embodiment, hardware disclosure and safety than the selected streaming-control contract.<!-- analysis-decision:SF-2026-ARXIV-2607-14635:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14698:start -->《Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color》已完成 Deep Source Review。The semantic-invariance failure is valuable security evidence, but it is a single illumination/color attack family and is better carried by its Full Review plus Ch72 integration.<!-- analysis-decision:SF-2026-ARXIV-2607-14698:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14739:start -->《FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models》已完成 Deep Source Review。Training-only foresight supervision clarifies the boundary to causal world state, but it does not alter deployed state ownership as broadly as the selected streaming VLA unit.<!-- analysis-decision:SF-2026-ARXIV-2607-14739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14777:start -->《SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning》已完成 Deep Source Review。Policy-synchronous hindsight skill distillation is a meaningful GRPO branch, but its analyzer-derived signal is bounded by one agentic RL setup and remains subordinate to the broader fixed-budget state-lifetime change.<!-- analysis-decision:SF-2026-ARXIV-2607-14777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14852:start -->《Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation》已完成 Deep Source Review。Fast/slow adapters and bounded replay add a continual-learning lifecycle branch, but the evidence remains a robotics-specific experimental realization without broad runtime or safety validation.<!-- analysis-decision:SF-2026-ARXIV-2607-14852:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15330:start -->《Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories》已完成 Deep Source Review。This high-score family is already explicitly integrated in Ch26; re-narrating it would duplicate the breadth-to-embodiment-alignment chain rather than add a new report-level unit.<!-- analysis-decision:SF-2026-ARXIV-2607-15330:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15161:start -->《On-Policy Delta Distillation》已完成 Deep Source Review。The matched teacher-base delta and sign gate are already integrated in Ch33; the Source Review closes evidence without duplicating the established mechanism narrative.<!-- analysis-decision:SF-2026-ARXIV-2607-15161:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15207:start -->《BadWAM: When World-Action Models Dream Right but Act Wrong》已完成 Deep Source Review。BadWAM is already integrated in Ch72 as an action/imagination decoupling attack; no new report-level narrative is needed after confirming exact-v1 boundaries.<!-- analysis-decision:SF-2026-ARXIV-2607-15207:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15257:start -->《SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration》已完成 Deep Source Review。SearchOS is a bounded implementation of durable typed workflow state and collaboration ownership already covered by Ch81/82; its Full Review remains complete.<!-- analysis-decision:SF-2026-ARXIV-2607-15257:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15498:start -->《VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs》已完成 Deep Source Review。Variable-rank KV compression is Books-worthy but stays within a single inference-state representation branch; the selected units have wider lifecycle and cross-Part reach.<!-- analysis-decision:SF-2026-ARXIV-2607-15498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-15524:start -->《Recursive Harness Self-Improvement》已完成 Deep Source Review。Recursive harness self-improvement is already represented in Ch81 with cached adjacent comparison, evaluator-drift and local-optimum boundaries; selection would repeat existing coverage.<!-- analysis-decision:SF-2026-ARXIV-2607-15524:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-14618 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-14618 | delta:SF-2026-ARXIV-2607-14618 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14618 |
| SF-2026-ARXIV-2607-14635 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14635 | delta:SF-2026-ARXIV-2607-14635 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14635 |
| SF-2026-ARXIV-2607-14695 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14695 | delta:SF-2026-ARXIV-2607-14695 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14695 |
| SF-2026-ARXIV-2607-14698 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-14698 | delta:SF-2026-ARXIV-2607-14698 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14698 |
| SF-2026-ARXIV-2607-14739 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14739 | delta:SF-2026-ARXIV-2607-14739 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14739 |
| SF-2026-ARXIV-2607-14777 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-14777 | delta:SF-2026-ARXIV-2607-14777 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14777 |
| SF-2026-ARXIV-2607-14852 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-14852 | delta:SF-2026-ARXIV-2607-14852 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14852 |
| SF-2026-ARXIV-2607-14952 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/35-checkpoint.md#L14-L14; books/part-04-training-system/37-tensor-parallel.md#L14-L14 | existing:SF-2026-ARXIV-2607-14952 | delta:SF-2026-ARXIV-2607-14952 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-14952 |
| SF-2026-ARXIV-2607-15004 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-15004 | delta:SF-2026-ARXIV-2607-15004 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15004 |
| SF-2026-ARXIV-2607-15330 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-15330 | delta:SF-2026-ARXIV-2607-15330 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15330 |
| SF-2026-ARXIV-2607-15161 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L14-L14 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-15161 | delta:SF-2026-ARXIV-2607-15161 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15161 |
| SF-2026-ARXIV-2607-15207 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14-L14 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-15207 | delta:SF-2026-ARXIV-2607-15207 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15207 |
| SF-2026-ARXIV-2607-15257 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L14-L14 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-15257 | delta:SF-2026-ARXIV-2607-15257 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15257 |
| SF-2026-ARXIV-2607-15263 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-15263 | delta:SF-2026-ARXIV-2607-15263 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-15263 |
| SF-2026-ARXIV-2607-15498 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-15498 | delta:SF-2026-ARXIV-2607-15498 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-15498 |
| SF-2026-ARXIV-2607-15524 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L14-L14 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-15524 | delta:SF-2026-ARXIV-2607-15524 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-15524 |

<!-- books-review:SF-2026-ARXIV-2607-14618:start --><!-- existing:SF-2026-ARXIV-2607-14618:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-14618:end --><!-- delta:SF-2026-ARXIV-2607-14618:start -->新增证据边界：Direct Evolution: uniform integer quantization -> fractional per-channel precision compiled into regular ISA quanta 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14618:end --><!-- books-review:SF-2026-ARXIV-2607-14618:end -->

<!-- books-review:SF-2026-ARXIV-2607-14635:start --><!-- existing:SF-2026-ARXIV-2607-14635:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14635:end --><!-- delta:SF-2026-ARXIV-2607-14635:start -->新增证据边界：Direct Evolution: direct action-loss rewriting of inherited representations -> mediated action-facing representation shaping 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14635:end --><!-- books-review:SF-2026-ARXIV-2607-14635:end -->

<!-- books-review:SF-2026-ARXIV-2607-14695:start --><!-- existing:SF-2026-ARXIV-2607-14695:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14695:end --><!-- delta:SF-2026-ARXIV-2607-14695:start -->新增证据边界：Direct Evolution: stop-think-act VLA serving -> asynchronous observation/action streams with bounded freshness 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14695:end --><!-- books-review:SF-2026-ARXIV-2607-14695:end -->

<!-- books-review:SF-2026-ARXIV-2607-14698:start --><!-- existing:SF-2026-ARXIV-2607-14698:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-14698:end --><!-- delta:SF-2026-ARXIV-2607-14698:start -->新增证据边界：Direct Evolution: broad color augmentation -> invariant-feature collapse diagnosis -> semantics-preserving perturbation training 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14698:end --><!-- books-review:SF-2026-ARXIV-2607-14698:end -->

<!-- books-review:SF-2026-ARXIV-2607-14739:start --><!-- existing:SF-2026-ARXIV-2607-14739:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14739:end --><!-- delta:SF-2026-ARXIV-2607-14739:start -->新增证据边界：Layering: action supervision -> training-only future feature and point-motion auxiliary supervision 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14739:end --><!-- books-review:SF-2026-ARXIV-2607-14739:end -->

<!-- books-review:SF-2026-ARXIV-2607-14777:start --><!-- existing:SF-2026-ARXIV-2607-14777:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-14777:end --><!-- delta:SF-2026-ARXIV-2607-14777:start -->新增证据边界：Direct Evolution: sparse outcome RL/static skills -> policy-synchronous hindsight-skill on-policy distillation 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14777:end --><!-- books-review:SF-2026-ARXIV-2607-14777:end -->

<!-- books-review:SF-2026-ARXIV-2607-14852:start --><!-- existing:SF-2026-ARXIV-2607-14852:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-14852:end --><!-- delta:SF-2026-ARXIV-2607-14852:start -->新增证据边界：Direct Evolution: one-shot task adaptation -> dual-timescale adapters plus bounded stochastic replay 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14852:end --><!-- books-review:SF-2026-ARXIV-2607-14852:end -->

<!-- books-review:SF-2026-ARXIV-2607-14952:start --><!-- existing:SF-2026-ARXIV-2607-14952:start -->对读 `books/part-04-training-system/36-distributed-training.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/36-distributed-training.md#L14-L14`）为：本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。<!-- existing:SF-2026-ARXIV-2607-14952:end --><!-- delta:SF-2026-ARXIV-2607-14952:start -->新增证据边界：Direct Evolution: full-context autograd residency -> detached prompt-state boundary plus short-suffix differentiable replay 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-14952:end --><!-- books-review:SF-2026-ARXIV-2607-14952:end -->

<!-- books-review:SF-2026-ARXIV-2607-15004:start --><!-- existing:SF-2026-ARXIV-2607-15004:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-15004:end --><!-- delta:SF-2026-ARXIV-2607-15004:start -->新增证据边界：Principle Reuse: visible-target tracking -> belief/state recovery under long occlusion 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15004:end --><!-- books-review:SF-2026-ARXIV-2607-15004:end -->

<!-- books-review:SF-2026-ARXIV-2607-15330:start --><!-- existing:SF-2026-ARXIV-2607-15330:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-15330:end --><!-- delta:SF-2026-ARXIV-2607-15330:start -->新增证据边界：Direct Evolution: robot-only teleoperation scale -> embodiment-free trajectory breadth then robot alignment 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15330:end --><!-- books-review:SF-2026-ARXIV-2607-15330:end -->

<!-- books-review:SF-2026-ARXIV-2607-15161:start --><!-- existing:SF-2026-ARXIV-2607-15161:start -->对读 `books/part-04-training-system/33-grpo.md#L14-L14` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-15161:end --><!-- delta:SF-2026-ARXIV-2607-15161:start -->新增证据边界：Direct Evolution: absolute teacher imitation -> matched teacher/base reasoning delta with direction gate 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15161:end --><!-- books-review:SF-2026-ARXIV-2607-15161:end -->

<!-- books-review:SF-2026-ARXIV-2607-15207:start --><!-- existing:SF-2026-ARXIV-2607-15207:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-15207:end --><!-- delta:SF-2026-ARXIV-2607-15207:start -->新增证据边界：Direct Evolution: plausible imagined future as safety sensor -> synchronized imagination/action verification under adaptive attack 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15207:end --><!-- books-review:SF-2026-ARXIV-2607-15207:end -->

<!-- books-review:SF-2026-ARXIV-2607-15257:start --><!-- existing:SF-2026-ARXIV-2607-15257:start -->对读 `books/part-07-agent/81-workflow.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L14-L14`）为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2607-15257:end --><!-- delta:SF-2026-ARXIV-2607-15257:start -->新增证据边界：Direct Evolution: conversation-local multi-agent progress -> externalized schema/evidence/task state and continuous dispatch 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15257:end --><!-- books-review:SF-2026-ARXIV-2607-15257:end -->

<!-- books-review:SF-2026-ARXIV-2607-15263:start --><!-- existing:SF-2026-ARXIV-2607-15263:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-15263:end --><!-- delta:SF-2026-ARXIV-2607-15263:start -->新增证据边界：Direct Evolution: peak security success -> workload-specific success/cost/refusal operating curves with contamination controls 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-15263:end --><!-- books-review:SF-2026-ARXIV-2607-15263:end -->

<!-- books-review:SF-2026-ARXIV-2607-15498:start --><!-- existing:SF-2026-ARXIV-2607-15498:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-15498:end --><!-- delta:SF-2026-ARXIV-2607-15498:start -->新增证据边界：Alternative Branch: delete low-salience tokens/uniform rank -> salience-weighted variable rank with nonzero token floor 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-15498:end --><!-- books-review:SF-2026-ARXIV-2607-15498:end -->

<!-- books-review:SF-2026-ARXIV-2607-15524:start --><!-- existing:SF-2026-ARXIV-2607-15524:start -->对读 `books/part-07-agent/81-workflow.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L14-L14`）为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2607-15524:end --><!-- delta:SF-2026-ARXIV-2607-15524:start -->新增证据边界：Alternative Branch: population/global harness search -> adjacent-revision local search with cached comparator 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-15524:end --><!-- books-review:SF-2026-ARXIV-2607-15524:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260717-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260717; semantic-review:SA-20260717-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260717-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-14618; review:SF-2026-ARXIV-2607-14635; review:SF-2026-ARXIV-2607-14695; review:SF-2026-ARXIV-2607-14698; review:SF-2026-ARXIV-2607-14739; review:SF-2026-ARXIV-2607-14777; review:SF-2026-ARXIV-2607-14852; review:SF-2026-ARXIV-2607-14952; review:SF-2026-ARXIV-2607-15004; review:SF-2026-ARXIV-2607-15330; review:SF-2026-ARXIV-2607-15161; review:SF-2026-ARXIV-2607-15207; review:SF-2026-ARXIV-2607-15257; review:SF-2026-ARXIV-2607-15263; review:SF-2026-ARXIV-2607-15498; review:SF-2026-ARXIV-2607-15524; semantic-review:SA-20260717-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260717-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260717-01; analysis:DA-20260717-02; analysis:DA-20260717-03; semantic-review:SA-20260717-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260717-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-14618; books-review:SF-2026-ARXIV-2607-14635; books-review:SF-2026-ARXIV-2607-14695; books-review:SF-2026-ARXIV-2607-14698; books-review:SF-2026-ARXIV-2607-14739; books-review:SF-2026-ARXIV-2607-14777; books-review:SF-2026-ARXIV-2607-14852; books-review:SF-2026-ARXIV-2607-14952; books-review:SF-2026-ARXIV-2607-15004; books-review:SF-2026-ARXIV-2607-15330; books-review:SF-2026-ARXIV-2607-15161; books-review:SF-2026-ARXIV-2607-15207; books-review:SF-2026-ARXIV-2607-15257; books-review:SF-2026-ARXIV-2607-15263; books-review:SF-2026-ARXIV-2607-15498; books-review:SF-2026-ARXIV-2607-15524; semantic-review:SA-20260717-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260717-COVERAGE:start -->PASS — 16/16 frozen denominator；全部 exact-v1 first-public timestamps 位于 [2026-07-16 09:00, 2026-07-17 09:00) Asia/Shanghai；D16/D18 相邻日去重无 owner 冲突；0 pending/blocked/unverified/disputed。<!-- semantic-review:SA-20260717-COVERAGE:end -->
<!-- semantic-review:SA-20260717-EVIDENCE:start -->PASS — 16/16 durable repo-relative HTML snapshots 存在且 SHA-256 匹配；所有 Method/Evaluation/Limitations 单锚点真实存在；15 Deep + 1 Standard route 与 Score V2 一致；artifact locator/claim boundaries 未把未审 repo 当作技术证据；packet central_receipts 与中央 ledger 16/16 完全一致。<!-- semantic-review:SA-20260717-EVIDENCE:end -->
<!-- semantic-review:SA-20260717-SELECTION:start -->PASS — 3 个 narrative units（2607.14695/2607.14952/2607.15263）均有 source-specific 选择理由；其余 12 个 Deep-eligible family 均有非模板化 not-selected 理由；2607.15004 Standard 未被误提为 Deep；selection 与 Daily/packet 一致。<!-- semantic-review:SA-20260717-SELECTION:end -->
<!-- semantic-review:SA-20260717-BOOKS:start -->PASS — 10 个 Integrate family 写入唯一 owner（Ch49、Ch26×4、Ch72、Ch33、Ch36、Ch66、Ch45）；owner/相邻章与旧方案→约束变化→机制→trade-off/failure boundary 连贯，正文不依赖论文名成立；Review notes 仅保留证据边界，其后无机制正文；Daily/packet/ledger disposition 一致。<!-- semantic-review:SA-20260717-BOOKS:end -->

## 8. Ignored Noise

1066 个窗口内 identity 中，1050 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：10 个 `Integrate`，6 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 15 / Standard 1。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/17/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-04-training-system/33-grpo.md`、`books/part-04-training-system/36-distributed-training.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference](https://arxiv.org/abs/2607.14618v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models](https://arxiv.org/abs/2607.14635v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Reflex: Real-Time VLA Control through Streaming Inference](https://arxiv.org/abs/2607.14695v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color](https://arxiv.org/abs/2607.14698v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models](https://arxiv.org/abs/2607.14739v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2607.14777v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Towards Human-like Physical Intelligence: Lifelong Vision-Language-Action Learning for Robotic Manipulation](https://arxiv.org/abs/2607.14852v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget](https://arxiv.org/abs/2607.14952v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking](https://arxiv.org/abs/2607.15004v1) — first-public（Asia/Shanghai）：2026-07-16；accessed：2026-08-27
- [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [On-Policy Delta Distillation](https://arxiv.org/abs/2607.15161v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [BadWAM: When World-Action Models Dream Right but Act Wrong](https://arxiv.org/abs/2607.15207v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration](https://arxiv.org/abs/2607.15257v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents](https://arxiv.org/abs/2607.15263v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs](https://arxiv.org/abs/2607.15498v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [Recursive Harness Self-Improvement](https://arxiv.org/abs/2607.15524v1) — first-public（Asia/Shanghai）：2026-07-17；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
