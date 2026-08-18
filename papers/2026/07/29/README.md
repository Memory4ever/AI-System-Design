# Daily Research — 2026-07-29

**Research Date:** 2026-07-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-28 09:00:00 ～ 2026-07-29 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；直接 arXiv 枚举冻结候选分母，技术 claim 回到精确 arXiv v1 与事件时 artifact receipt

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1201 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 12 个。当前路由账目为 12 个 Deep、0 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-29 |
| Window End | 2026-07-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-29-0900-v2.1-recovery-01 |
| Denominator Frozen At | 2026-08-27T21:40:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-28T09:00:00+08:00 | 2026-07-29T09:00:00+08:00 | 2026-08-27T21:40:00+08:00 | https://export.arxiv.org/api/query; archived query submittedDate:[202607260100 TO 202607290100]; strict Atom v1 published-time filter [202607280100 TO 202607290100); cross-list deduplicated by arXiv ID; later revisions excluded | checked | 1201 | SF-2026-ARXIV-2607.25255<br>SF-2026-ARXIV-2607.25291<br>SF-2026-ARXIV-2607.25431<br>SF-2026-ARXIV-2607.25487<br>SF-2026-ARXIV-2607.25498<br>SF-2026-ARXIV-2607.25504<br>SF-2026-ARXIV-2607.25816<br>SF-2026-ARXIV-2607.25852<br>SF-2026-ARXIV-2607.25884<br>SF-2026-ARXIV-2607.25886<br>SF-2026-ARXIV-2607.25904<br>SF-2026-ARXIV-2607.25970 | archived pages arxiv-20260727-29-start0000.xml.gz and arxiv-20260727-29-start2000.xml.gz; 2000 + 924 entries of query total 2924; strict-window filtered raw hits 1201; final_cursor=end | 2026-07-29T09:00:00+08:00 | coverage:SRC-ARXIV:20260729 | — |
| SRC-GITHUB-COMMIT | 2026-07-28T09:00:00+08:00 | 2026-07-29T09:00:00+08:00 | 2026-08-27T21:40:00+08:00 | exact GitHub commit API lookups: https://github.com/BrainJellyPie/CoTinyVLA@71083bd34bfeb1c1063cf3a0835c4a1fa424e072; https://github.com/YIAI-02/DOPS@e2ecb0116a82a45b50216e1b4201f37ca625d3d5; https://github.com/dakaidan/CONQuER-Replication@25aaac1161961547e32c358155384d6ededb9a48; https://github.com/evolvent-ai/RSIBench-Data@408c36c5202435314abfa374ba6cbc3c924c46ef | checked | 4 | SF-2026-ARXIV-2607.25487; SF-2026-ARXIV-2607.25498; SF-2026-ARXIV-2607.25884; SF-2026-ARXIV-2607.25886 | pages=4; final cursors=71083bd34bfeb1c1063cf3a0835c4a1fa424e072,e2ecb0116a82a45b50216e1b4201f37ca625d3d5,25aaac1161961547e32c358155384d6ededb9a48,408c36c5202435314abfa374ba6cbc3c924c46ef; one bounded commit lookup per family | 2026-07-29T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260729 | — |

<!-- coverage:SRC-ARXIV:20260729:start -->Archived direct-arXiv submittedDate replay froze the strict-window denominator. Canonical source: papers/2026/07/_sources/arxiv-v2.1-replay-20260727-31/coverage-2026-07-29.json; sha256:73d50069c99cd32f012fe4dd536502d2ed00feda30b07bdfb64f78b2f89287d8; 1201 unique identities in this strict window; 12 routed families.<!-- coverage:SRC-ARXIV:20260729:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260729:start -->repository=https://github.com/BrainJellyPie/CoTinyVLA, until=2026-07-29T01:00:00Z, full_sha=71083bd34bfeb1c1063cf3a0835c4a1fa424e072, commit_timestamp=2026-07-28T09:26:32Z, url=https://github.com/BrainJellyPie/CoTinyVLA/commit/71083bd34bfeb1c1063cf3a0835c4a1fa424e072; repository=https://github.com/YIAI-02/DOPS, until=2026-07-29T01:00:00Z, full_sha=e2ecb0116a82a45b50216e1b4201f37ca625d3d5, commit_timestamp=2026-07-12T11:08:29Z, url=https://github.com/YIAI-02/DOPS/commit/e2ecb0116a82a45b50216e1b4201f37ca625d3d5; repository=https://github.com/dakaidan/CONQuER-Replication, until=2026-07-29T01:00:00Z, full_sha=25aaac1161961547e32c358155384d6ededb9a48, commit_timestamp=2026-07-07T15:53:44Z, url=https://github.com/dakaidan/CONQuER-Replication/commit/25aaac1161961547e32c358155384d6ededb9a48; repository=https://github.com/evolvent-ai/RSIBench-Data, until=2026-07-29T01:00:00Z, full_sha=408c36c5202435314abfa374ba6cbc3c924c46ef, commit_timestamp=2026-07-28T15:07:01Z, url=https://github.com/evolvent-ai/RSIBench-Data/commit/408c36c5202435314abfa374ba6cbc3c924c46ef; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260729:end -->

### Coverage Limitations

- 直接 arXiv replay 只闭合候选枚举与 first-public identity；机制和实验结论仍逐项来自 exact-v1 全文与可追溯 artifact。
- Artifact-boundary routing 覆盖 12 个 family：exact v1 为 5 个 family 披露 artifact/evidence locator，其中 5 个提供外部 repository/project/demo locator，另有 7 个未披露；本日确认 4 个 family、4 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607.25255 | arXiv:2607.25255v1 | paper-v1:2607.25255 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25255 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607.25255 | yes |
| SF-2026-ARXIV-2607.25291 | arXiv:2607.25291v1 | paper-v1:2607.25291 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25291 | self | — | new_in_window | INFER-PREFILL | Integrate | books-review:SF-2026-ARXIV-2607.25291 | yes |
| SF-2026-ARXIV-2607.25431 | arXiv:2607.25431v1 | paper-v1:2607.25431 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25431 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25431 | yes |
| SF-2026-ARXIV-2607.25487 | arXiv:2607.25487v1 | paper-v1:2607.25487 | 2026-W31 | 2026-07-28 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25487 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2607.25487 | yes |
| SF-2026-ARXIV-2607.25498 | arXiv:2607.25498v1 | paper-v1:2607.25498 | 2026-W31 | 2026-07-28 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25498 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25498 | yes |
| SF-2026-ARXIV-2607.25504 | arXiv:2607.25504v1 | paper-v1:2607.25504 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25504 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25504 | yes |
| SF-2026-ARXIV-2607.25816 | arXiv:2607.25816v1 | paper-v1:2607.25816 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25816 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2607.25816 | yes |
| SF-2026-ARXIV-2607.25852 | arXiv:2607.25852v1 | paper-v1:2607.25852 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25852 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2607.25852 | yes |
| SF-2026-ARXIV-2607.25884 | arXiv:2607.25884v1 | paper-v1:2607.25884 | 2026-W31 | 2026-07-28 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25884 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607.25884 | yes |
| SF-2026-ARXIV-2607.25886 | arXiv:2607.25886v1 | paper-v1:2607.25886 | 2026-W31 | 2026-07-28 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25886 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607.25886 | yes |
| SF-2026-ARXIV-2607.25904 | arXiv:2607.25904v1 | paper-v1:2607.25904 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25904 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25904 | yes |
| SF-2026-ARXIV-2607.25970 | arXiv:2607.25970v1 | paper-v1:2607.25970 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607.25970 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25970 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607.25255 | RP-bcd9a76d6d4a9664 | deep | arXiv:2607.25255v1 | SRC-ARXIV@arXiv:2607.25255v1 | https://arxiv.org/html/2607.25255v1#S3; https://arxiv.org/html/2607.25255v1#S4 | https://arxiv.org/html/2607.25255v1#S5; https://arxiv.org/html/2607.25255v1#S5.SS6 | https://arxiv.org/html/2607.25255v1#S5.SS7; https://arxiv.org/html/2607.25255v1#S5.SS8; https://arxiv.org/html/2607.25255v1#S6 | Not Disclosed — exact v1 names no immutable author implementation or experiment commit; a later revision must not be projected backward. | claim:SF-2026-ARXIV-2607.25255 | complete |
| SF-2026-ARXIV-2607.25291 | RP-af9c2cea6ca1dc60 | deep | arXiv:2607.25291v1 | SRC-ARXIV@arXiv:2607.25291v1 | https://arxiv.org/html/2607.25291v1#S4 | https://arxiv.org/html/2607.25291v1#S5 | https://arxiv.org/html/2607.25291v1#S3; https://arxiv.org/html/2607.25291v1#S5.SS4; https://arxiv.org/html/2607.25291v1#S6 | Not Disclosed — exact v1 contains no author artifact URL, repository, immutable commit, release tag or source archive; the AngelSlim repository appears only in a later revision and cannot be projected backward into this event-time v1 evidence package. | claim:SF-2026-ARXIV-2607.25291 | complete |
| SF-2026-ARXIV-2607.25431 | RP-dff48c766a141d3f | deep | arXiv:2607.25431v1 | SRC-ARXIV@arXiv:2607.25431v1 | https://arxiv.org/html/2607.25431v1#S3; https://arxiv.org/html/2607.25431v1#S4; https://arxiv.org/html/2607.25431v1#S5; https://arxiv.org/html/2607.25431v1#S6; https://arxiv.org/html/2607.25431v1#S7; https://arxiv.org/html/2607.25431v1#S8 | https://arxiv.org/html/2607.25431v1#S9 | https://arxiv.org/html/2607.25431v1#S3.SS4; https://arxiv.org/html/2607.25431v1#S10 | Not Disclosed — exact v1 links dependencies but no immutable author repository or experiment commit. | claim:SF-2026-ARXIV-2607.25431 | complete |
| SF-2026-ARXIV-2607.25487 | RP-7d2e246682a7d2e3 | deep | arXiv:2607.25487v1 | SRC-ARXIV@arXiv:2607.25487v1; SRC-GITHUB-COMMIT@commit:71083bd34bfeb1c1063cf3a0835c4a1fa424e072 | https://arxiv.org/html/2607.25487v1#S3 | https://arxiv.org/html/2607.25487v1#S4; https://arxiv.org/html/2607.25487v1#S5; https://arxiv.org/html/2607.25487v1#A8; https://arxiv.org/html/2607.25487v1#A9; https://arxiv.org/html/2607.25487v1#A10; https://arxiv.org/html/2607.25487v1#A11; https://arxiv.org/html/2607.25487v1#A12 | https://arxiv.org/html/2607.25487v1#S6; https://arxiv.org/html/2607.25487v1#S7 | https://github.com/BrainJellyPie/CoTinyVLA/commit/71083bd34bfeb1c1063cf3a0835c4a1fa424e072 | claim:SF-2026-ARXIV-2607.25487 | complete |
| SF-2026-ARXIV-2607.25498 | RP-6194d7a5df687830 | deep | arXiv:2607.25498v1 | SRC-ARXIV@arXiv:2607.25498v1; SRC-GITHUB-COMMIT@commit:e2ecb0116a82a45b50216e1b4201f37ca625d3d5 | https://arxiv.org/html/2607.25498v1#S4; https://arxiv.org/html/2607.25498v1#S5 | https://arxiv.org/html/2607.25498v1#S6 | https://arxiv.org/html/2607.25498v1#S3; https://arxiv.org/html/2607.25498v1#S8 | https://github.com/YIAI-02/DOPS/commit/e2ecb0116a82a45b50216e1b4201f37ca625d3d5 | claim:SF-2026-ARXIV-2607.25498 | complete |
| SF-2026-ARXIV-2607.25504 | RP-b498f38203a852e6 | deep | arXiv:2607.25504v1 | SRC-ARXIV@arXiv:2607.25504v1 | https://arxiv.org/html/2607.25504v1#S3; https://arxiv.org/html/2607.25504v1#S3.SS1; https://arxiv.org/html/2607.25504v1#S3.SS2 | https://arxiv.org/html/2607.25504v1#S4; https://arxiv.org/html/2607.25504v1#S4.SS1; https://arxiv.org/html/2607.25504v1#S4.SS2 | Not Disclosed — exact v1 contains no dedicated limitations or counterevidence section; applicability is therefore bounded to the disclosed Section IV methodology/results and excludes arbitrary sparsity patterns, other silicon generations and unpruned models. | Not Disclosed — exact v1 exposes no immutable RTL, simulator or experiment commit. | claim:SF-2026-ARXIV-2607.25504 | complete |
| SF-2026-ARXIV-2607.25816 | RP-b0a12942a9cda923 | deep | arXiv:2607.25816v1 | SRC-ARXIV@arXiv:2607.25816v1 | https://arxiv.org/html/2607.25816v1#S2; https://arxiv.org/html/2607.25816v1#S3 | https://arxiv.org/html/2607.25816v1#S4 | https://arxiv.org/html/2607.25816v1#Sx1 | Not Disclosed — exact v1 exposes no immutable author training or evaluation repository. | claim:SF-2026-ARXIV-2607.25816 | complete |
| SF-2026-ARXIV-2607.25852 | RP-d09507d44cddec30 | deep | arXiv:2607.25852v1 | SRC-ARXIV@arXiv:2607.25852v1 | https://arxiv.org/html/2607.25852v1#S2; https://arxiv.org/html/2607.25852v1#S3; https://arxiv.org/html/2607.25852v1#S4 | https://arxiv.org/html/2607.25852v1#S2.SS5; https://arxiv.org/html/2607.25852v1#S3.SS4; https://arxiv.org/html/2607.25852v1#S4.SS4; https://arxiv.org/html/2607.25852v1#S5 | https://arxiv.org/html/2607.25852v1#S4.SS1 | https://github.com/Tencent/AngelSpec is disclosed by exact v1, but the repository had no commit at or before the Daily cutoff; event-time implementation identity is therefore unverified. | claim:SF-2026-ARXIV-2607.25852 | complete |
| SF-2026-ARXIV-2607.25884 | RP-e47777c17878816b | deep | arXiv:2607.25884v1 | SRC-ARXIV@arXiv:2607.25884v1; SRC-GITHUB-COMMIT@commit:25aaac1161961547e32c358155384d6ededb9a48 | https://arxiv.org/html/2607.25884v1#S2 | https://arxiv.org/html/2607.25884v1#S3; https://arxiv.org/html/2607.25884v1#S4 | https://arxiv.org/html/2607.25884v1#S5; https://arxiv.org/html/2607.25884v1#S6 | https://github.com/dakaidan/CONQuER-Replication/commit/25aaac1161961547e32c358155384d6ededb9a48 | claim:SF-2026-ARXIV-2607.25884 | complete |
| SF-2026-ARXIV-2607.25886 | RP-edeb5fed5aaca2ba | deep | arXiv:2607.25886v1 | SRC-ARXIV@arXiv:2607.25886v1; SRC-GITHUB-COMMIT@commit:408c36c5202435314abfa374ba6cbc3c924c46ef | https://arxiv.org/html/2607.25886v1#S3 | https://arxiv.org/html/2607.25886v1#S4; https://arxiv.org/html/2607.25886v1#S5 | https://arxiv.org/html/2607.25886v1#S6 | https://github.com/evolvent-ai/RSIBench-Data/commit/408c36c5202435314abfa374ba6cbc3c924c46ef | claim:SF-2026-ARXIV-2607.25886 | complete |
| SF-2026-ARXIV-2607.25904 | RP-cb228ca03f78d7b1 | deep | arXiv:2607.25904v1 | SRC-ARXIV@arXiv:2607.25904v1 | https://arxiv.org/html/2607.25904v1#Sx3; https://arxiv.org/html/2607.25904v1#Sx3.SSx2; https://arxiv.org/html/2607.25904v1#Sx3.SSx3 | https://arxiv.org/html/2607.25904v1#Sx4; https://arxiv.org/html/2607.25904v1#Sx4.SSx4; https://arxiv.org/html/2607.25904v1#Sx5; https://arxiv.org/html/2607.25904v1#Sx5.SSx2; https://arxiv.org/html/2607.25904v1#Sx5.SSx5; https://arxiv.org/html/2607.25904v1#Sx5.SSx7 | https://arxiv.org/html/2607.25904v1#Sx6; https://arxiv.org/html/2607.25904v1#A1.SS11 | Not Disclosed — exact v1 exposes no immutable author evaluator, task corpus or experiment commit. | claim:SF-2026-ARXIV-2607.25904 | complete |
| SF-2026-ARXIV-2607.25970 | RP-2b7589b5685062b0 | deep | arXiv:2607.25970v1 | SRC-ARXIV@arXiv:2607.25970v1 | https://arxiv.org/html/2607.25970v1#S3; https://arxiv.org/html/2607.25970v1#S4 | https://arxiv.org/html/2607.25970v1#S5; https://arxiv.org/html/2607.25970v1#S6 | https://arxiv.org/html/2607.25970v1#A2; https://arxiv.org/html/2607.25970v1#A3; https://arxiv.org/html/2607.25970v1#A4; https://arxiv.org/html/2607.25970v1#A5; https://arxiv.org/html/2607.25970v1#A6 | Not Disclosed — exact v1 identifies public dependencies and evaluation services but no immutable author training/experiment commit. | claim:SF-2026-ARXIV-2607.25970 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607.25255:start -->
#### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607.25255:start -->Supports semantic taint propagation and workflow-level validation in the disclosed benchmarks. It does not prove labels are complete, adaptive attackers cannot evade reconstruction, or the framework withstands compromised hosts or model weights. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25255:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25255v1#S3; https://arxiv.org/html/2607.25255v1#S4`；Evaluation：`https://arxiv.org/html/2607.25255v1#S5; https://arxiv.org/html/2607.25255v1#S5.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25255v1#S5.SS7; https://arxiv.org/html/2607.25255v1#S5.SS8; https://arxiv.org/html/2607.25255v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization.`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25255:end -->

<!-- review:SF-2026-ARXIV-2607.25291:start -->
#### CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention

<!-- claim:SF-2026-ARXIV-2607.25291:start -->Supports proxy-kernel co-design for sparse prefill in the tested models, hardware and budgets. It does not establish exactness, universal recall under tighter masks, sparse-decode benefit or cross-hardware portability. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25291:end -->

**旧方案与约束变化。** `本章的核心判断是：**Prefill 将整段 prompt 映射为第一个 next-token distribution 和逐层 KV state；它利用 token 维度并行换取高 GPU efficiency，但工作量、显存峰值和调度占用会随 prompt 长度快速增长。**`（`books/part-05-inference-system/43-prefill.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: binary proxy mask -> ordered candidate mask -> online-softmax kernel refinement -> budget-aware sparse prefill. 它改变 `INFER-PREFILL` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25291v1#S4`；Evaluation：`https://arxiv.org/html/2607.25291v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25291v1#S3; https://arxiv.org/html/2607.25291v1#S5.SS4; https://arxiv.org/html/2607.25291v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: binary proxy mask -> ordered candidate mask -> online-softmax kernel refinement -> budget-aware sparse prefill.`。
- Stable owner：`INFER-PREFILL`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25291:end -->

<!-- review:SF-2026-ARXIV-2607.25431:start -->
#### CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents

<!-- claim:SF-2026-ARXIV-2607.25431:start -->Supports multi-view context serving with explicit validity boundaries. It does not prove semantic equivalence of incremental and rebuilt views outside measured operations or guarantee downstream agent correctness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25431:end -->

**旧方案与约束变化。** `本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**`（`books/part-07-agent/75-context.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: task-local search -> commit-indexed reusable views -> operation-scoped incremental maintenance -> bounded context assembly. 它改变 `AGENT-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25431v1#S3; https://arxiv.org/html/2607.25431v1#S4; https://arxiv.org/html/2607.25431v1#S5; https://arxiv.org/html/2607.25431v1#S6; https://arxiv.org/html/2607.25431v1#S7; https://arxiv.org/html/2607.25431v1#S8`；Evaluation：`https://arxiv.org/html/2607.25431v1#S9`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25431v1#S3.SS4; https://arxiv.org/html/2607.25431v1#S10`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: task-local search -> commit-indexed reusable views -> operation-scoped incremental maintenance -> bounded context assembly.`。
- Stable owner：`AGENT-CONTEXT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607.25431:end -->

<!-- review:SF-2026-ARXIV-2607.25487:start -->
#### CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model

<!-- claim:SF-2026-ARXIV-2607.25487:start -->Supports structured supervision as a capacity alternative on LIBERO-Plus. It does not prove cross-robot transfer, real-world physical safety, superiority to all larger VLAs or causal validity of natural-language rationales. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25487:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Alternative Branch: scale backbone capacity -> preserve temporal evidence -> distill slow Plan and fast Think state -> execute bounded action chunks. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25487v1#S3`；Evaluation：`https://arxiv.org/html/2607.25487v1#S4; https://arxiv.org/html/2607.25487v1#S5; https://arxiv.org/html/2607.25487v1#A8; https://arxiv.org/html/2607.25487v1#A9; https://arxiv.org/html/2607.25487v1#A10; https://arxiv.org/html/2607.25487v1#A11; https://arxiv.org/html/2607.25487v1#A12`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25487v1#S6; https://arxiv.org/html/2607.25487v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Alternative Branch: scale backbone capacity -> preserve temporal evidence -> distill slow Plan and fast Think state -> execute bounded action chunks.`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25487:end -->

<!-- review:SF-2026-ARXIV-2607.25498:start -->
#### Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling

<!-- claim:SF-2026-ARXIV-2607.25498:start -->Supports closed-loop operator placement and weight-layout selection on the disclosed heterogeneous platform. It does not prove universal advantage over PD, portable cost models or production robustness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25498:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: phase placement -> operator DAG -> runtime contention-aware placement -> persistent weight-layout arbitration. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25498v1#S4; https://arxiv.org/html/2607.25498v1#S5`；Evaluation：`https://arxiv.org/html/2607.25498v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25498v1#S3; https://arxiv.org/html/2607.25498v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: phase placement -> operator DAG -> runtime contention-aware placement -> persistent weight-layout arbitration.`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607.25498:end -->

<!-- review:SF-2026-ARXIV-2607.25504:start -->
#### At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference

<!-- claim:SF-2026-ARXIV-2607.25504:start -->Supports ISA/kernel co-design for the evaluated sparse contractions. It does not prove end-to-end benefit for arbitrary sparsity patterns, silicon generations or unpruned models. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25504:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: model sparsity -> Gustavson dataflow -> indexed ISA support -> calibrated cluster scale-out. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25504v1#S3; https://arxiv.org/html/2607.25504v1#S3.SS1; https://arxiv.org/html/2607.25504v1#S3.SS2`；Evaluation：`https://arxiv.org/html/2607.25504v1#S4; https://arxiv.org/html/2607.25504v1#S4.SS1; https://arxiv.org/html/2607.25504v1#S4.SS2`；Limitations/Counterevidence：`Not Disclosed — exact v1 contains no dedicated limitations or counterevidence section; applicability is therefore bounded to the disclosed Section IV methodology/results and excludes arbitrary sparsity patterns, other silicon generations and unpruned models.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency: model sparsity -> Gustavson dataflow -> indexed ISA support -> calibrated cluster scale-out.`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607.25504:end -->

<!-- review:SF-2026-ARXIV-2607.25816:start -->
#### Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL

<!-- claim:SF-2026-ARXIV-2607.25816:start -->Supports reduced proposal mismatch through a dual-mode self-speculator. It does not prove wall-clock benefit, safe speculation for irreversible tools or stable performance under agent-policy updates. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25816:end -->

**旧方案与约束变化。** `本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**`（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: separate tool-call predictor -> same-model speculative mode -> self-rollout targets -> joint agent/speculator optimization with canonical commit. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25816v1#S2; https://arxiv.org/html/2607.25816v1#S3`；Evaluation：`https://arxiv.org/html/2607.25816v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25816v1#Sx1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: separate tool-call predictor -> same-model speculative mode -> self-rollout targets -> joint agent/speculator optimization with canonical commit.`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25816:end -->

<!-- review:SF-2026-ARXIV-2607.25852:start -->
#### AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607.25852:start -->Supports workload-specialized drafters and batch-level verification allocation in the disclosed stack. It does not prove a universal drafter choice, exact transfer to other targets/hardware or stable gains under production drift. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25852:end -->

**旧方案与约束变化。** `本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**`（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25852v1#S2; https://arxiv.org/html/2607.25852v1#S3; https://arxiv.org/html/2607.25852v1#S4`；Evaluation：`https://arxiv.org/html/2607.25852v1#S2.SS5; https://arxiv.org/html/2607.25852v1#S3.SS4; https://arxiv.org/html/2607.25852v1#S4.SS4; https://arxiv.org/html/2607.25852v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25852v1#S4.SS1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification.`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25852:end -->

<!-- review:SF-2026-ARXIV-2607.25884:start -->
#### CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates

<!-- claim:SF-2026-ARXIV-2607.25884:start -->Supports compiler-integrated, selectively measured MPQ search. It does not prove surrogate convergence, universal Pareto dominance or transfer of one policy across hardware/compiler versions. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25884:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: framework-side bit assignment -> compiler-visible quantization IR -> surrogate-prescreened search -> selective hardware calibration. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25884v1#S2`；Evaluation：`https://arxiv.org/html/2607.25884v1#S3; https://arxiv.org/html/2607.25884v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25884v1#S5; https://arxiv.org/html/2607.25884v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: framework-side bit assignment -> compiler-visible quantization IR -> surrogate-prescreened search -> selective hardware calibration.`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25884:end -->

<!-- review:SF-2026-ARXIV-2607.25886:start -->
#### RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

<!-- claim:SF-2026-ARXIV-2607.25886:start -->Supports isolating data-research decisions and preserving non-monotonic checkpoint trajectories. It does not prove recursive self-improvement, autonomous research reliability or transfer beyond the fixed stack. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25886:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25886v1#S3`；Evaluation：`https://arxiv.org/html/2607.25886v1#S4; https://arxiv.org/html/2607.25886v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25886v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy.`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607.25886:end -->

<!-- review:SF-2026-ARXIV-2607.25904:start -->
#### Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification

<!-- claim:SF-2026-ARXIV-2607.25904:start -->Supports interactive environment-state verification for the disclosed GUI tasks. It does not prove reward correctness on arbitrary applications, evaluator noninterference or safe use as a sole RL objective. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25904:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: screenshot judgment -> proposed postconditions -> read-only environment evidence -> reward with provenance. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25904v1#Sx3; https://arxiv.org/html/2607.25904v1#Sx3.SSx2; https://arxiv.org/html/2607.25904v1#Sx3.SSx3`；Evaluation：`https://arxiv.org/html/2607.25904v1#Sx4; https://arxiv.org/html/2607.25904v1#Sx4.SSx4; https://arxiv.org/html/2607.25904v1#Sx5; https://arxiv.org/html/2607.25904v1#Sx5.SSx2; https://arxiv.org/html/2607.25904v1#Sx5.SSx5; https://arxiv.org/html/2607.25904v1#Sx5.SSx7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25904v1#Sx6; https://arxiv.org/html/2607.25904v1#A1.SS11`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: screenshot judgment -> proposed postconditions -> read-only environment evidence -> reward with provenance.`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607.25904:end -->

<!-- review:SF-2026-ARXIV-2607.25970:start -->
#### Reinforcement Learning for Code Optimization

<!-- claim:SF-2026-ARXIV-2607.25970:start -->Supports a staged measurement-to-reward pipeline in the disclosed code-optimization setting. It does not prove wall-clock reward is stationary, generated code is safe beyond tests or gains transfer across hardware. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607.25970:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: hidden-test correctness reward -> calibrated performance evidence -> composite reward -> stabilized GRPO and held-out percentile evaluation. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25970v1#S3; https://arxiv.org/html/2607.25970v1#S4`；Evaluation：`https://arxiv.org/html/2607.25970v1#S5; https://arxiv.org/html/2607.25970v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25970v1#A2; https://arxiv.org/html/2607.25970v1#A3; https://arxiv.org/html/2607.25970v1#A4; https://arxiv.org/html/2607.25970v1#A5; https://arxiv.org/html/2607.25970v1#A6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: hidden-test correctness reward -> calibrated performance evidence -> composite reward -> stabilized GRPO and held-out percentile evaluation.`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607.25970:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607.25255 | ASB, AgentHarm, RedCode and SafeArena adversarial tasks normalized to one schema; evaluated collaboration workflows contain 3–10 nodes. | DeepSeek-V3.2-Exp is the default defense-side model; sensitivity study also evaluates o4-mini, MiMo-v2.5, Kimi-K2.6, Claude-3.5-Haiku and GPT-5-mini. | Not Disclosed — exact v1 reports workflow-level calls and seconds but no accelerator or host configuration. | Not Disclosed — exact v1 does not bind the defense models to a numeric precision. | 3–10-node collaboration workflows; prompt/token lengths are Not Disclosed. | Not Disclosed — generated-token or response-length bounds are not reported. | Not Disclosed — evaluation batch size is not reported. | Not Disclosed — production or benchmark concurrency is not reported. | Average ASR 12.7% versus 69.3% undefended; default configuration adds 3.7 LLM calls and 8.8 seconds per harmful workflow. No production tail-latency SLO is disclosed. | Author evaluation using ASR, task completion rate, false-positive rate and paired benign-harmful success; the result supports the disclosed workflow threat model, not compromised hosts/weights or adaptive-evasion resistance. |
| SF-2026-ARXIV-2607.25291 | RULER synthetic long-context tasks from 4K to 128K and LongBench-v2 direct and chain-of-thought modes; sparse attention is applied only to prefill and decode remains dense. | Llama-3.1-8B-Instruct and Qwen3-8B; Qwen uses task-recommended sampling/thinking settings and YaRN to extend to 128K where needed. | One NVIDIA H20 node. | Not Disclosed — exact v1 does not state the numeric precision used for the reported accuracy and latency measurements. | 4K, 8K, 16K, 32K, 64K and 128K contexts in RULER; LongBench-v2 uses benchmark-defined inputs. | Not Disclosed — the benchmark report does not bind TTFT results to a generated-output length. | Not Disclosed — batch size for accuracy and TTFT measurements is not reported. | Not Disclosed — concurrent-request mix is not reported. | At 128K, 4.93x attention speedup and 2.53x TTFT speedup over full attention with negligible disclosed quality degradation; no production tail SLO. | Author RULER accuracy, LongBench-v2 task accuracy and repeated layer/TTFT timing against FlashAttention-2 and sparse-attention baselines; evidence is limited to tested models, H20 and budgets. |
| SF-2026-ARXIV-2607.25431 | 100 repository snapshots, 1,000 navigation requests, 40 commit transitions and 7,500 coding-agent trajectories covering view construction, freshness, navigation and context-policy comparisons. | Operation-specific coding agents and embedding/reranking components as configured by exact v1; no single model identity governs all four evaluation blocks. | Not Disclosed as one portable contract — exact v1 reports an experiment environment, but the claimed compatibility/token reductions are operation-specific rather than a hardware SLO. | Not Disclosed — numeric precision is not part of the reported data-system contract. | Repository snapshots and request/trajectory inputs; exact token lengths vary by operation and are not fixed globally. | Context and trajectory token counts are measured; one fixed output-length cap is Not Disclosed. | Not Disclosed — evaluation batch size is not a shared contract across construction, navigation and trajectory experiments. | Not Disclosed — concurrent serving load is not reported as an evaluation variable. | Conditional live/static navigation matching and 50–87% trajectory-token reduction; no production latency or freshness SLO is established. | Author-defined build/freshness, normalized-location compatibility and trajectory-token accounting; results do not establish one index/provider policy for every edit, operation or language. |
| SF-2026-ARXIV-2607.25487 | LIBERO-Plus with 10,030 perturbed tasks across Spatial, Object, Goal and Long suites and seven perturbation dimensions; original LIBERO is also evaluated. | CoTinyVLA 0.9B on a Qwen3.5-0.8B backbone, distilled from a 35B teacher; comparisons include published 3B–7B VLA baselines. | Not Disclosed for runtime identity — exact v1 reports 2.25 GiB peak closed-loop allocated GPU memory but does not name the runtime accelerator. | Not Disclosed for CoTinyVLA evaluation; the paper's 20+ GiB bfloat16 statement describes a typical 7B baseline, not the measured CoTinyVLA precision. | Sixteen history frames per control step: eight third-person and eight wrist-camera frames, with textual camera/time markers. | Bounded action chunks plus Plan/Think text; exact token and action-chunk lengths are not disclosed as a single benchmark constant. | Not Disclosed — closed-loop evaluation batch size is not reported. | Not Disclosed — robot/environment concurrency is not reported. | 80.7–90.8% suite success, 2.25 GiB peak allocated GPU memory and 40–45 success-point loss under empty/contradictory Plan interventions; no control-frequency or physical-safety SLO. | Author LIBERO-Plus and LIBERO success metrics with perturbation-axis ablations and paired Plan interventions; evidence does not establish real-robot transfer or safety. |
| SF-2026-ARXIV-2607.25498 | Prefill/decode inference traces and operator-placement/layout experiments on the paper's representative heterogeneous NPU/PIM configurations. | Paper-configured transformer/LLM shapes; exact model identities and shapes vary by experiment and are not one portable contract. | Representative heterogeneous NPU and PIM systems defined in exact v1; no GPU result is claimed. | Configuration-bound and not disclosed as one invariant precision across the reported systems. | Configuration-bound prompt/context shapes; no single input length governs all reported speedups. | Configuration-bound decode shapes; no single output length governs all reported speedups. | Configuration-bound and not disclosed as one benchmark-wide batch size. | Not Disclosed as a production request-concurrency contract. | 1.20–2.23x geometric-mean speedup over prefill/decode disaggregation and an additional 1.28–1.33x from weight-layout arbitration; no production tail SLO. | Author performance model/simulator and disclosed heterogeneous-platform comparisons; results do not establish a portable GPU cost model or universal advantage. |
| SF-2026-ARXIV-2607.25504 | Dual-sparse tensor-contraction kernels plus modeled LLM prefill/decode using DuoGPT-pruned Llama-3-8B at 40–60% dual sparsity. | DuoGPT-pruned Llama-3-8B for end-to-end modeling; kernel microbenchmarks cover disclosed sparse contraction shapes. | 12 nm custom vector-cluster implementation with the proposed sparse unit; this is not a GPU platform. | Paper-defined custom-vector data paths; one portable model-serving precision is not disclosed. | Paper-defined contraction and prefill shapes; no single token length is disclosed as the benchmark contract. | Paper-defined decode modeling; no single generated-token length is disclosed. | Not Disclosed as a serving batch-size contract. | Not Disclosed as a multi-request concurrency contract. | 3.1% cluster-area overhead, 6.9–7.4x kernel acceleration, modeled 2.40–5.25x prefill and 2.06–3.16x decode speedup; no production SLO. | Author RTL/implementation analysis, kernel measurements and calibrated end-to-end modeling; evidence is bounded to the custom vector architecture and evaluated sparsity patterns. |
| SF-2026-ARXIV-2607.25816 | Search question answering and conversational tool-use trajectories used to train/evaluate next-tool-call self-speculation. | Qwen3-4B and Qwen3.5-4B dual-mode agent/speculator models. | Not Disclosed — exact v1 does not bind the reported Hit@1/task results to an accelerator configuration. | Not Disclosed — training and serving numeric precision are not part of the reported contract. | Partial agent trajectories with shared prefix KV; prompt and trajectory token lengths are not disclosed as fixed bounds. | Next tool-call proposal; serialized call/token length is Not Disclosed. | Not Disclosed — evaluation and rollout batch sizes are not reported as the serving contract. | Not Disclosed — concurrent tool or request execution is not evaluated. | Hit@1 improves from 44.1 to 61.2 and from 48.9 to 66.3 while task success is preserved; no end-to-end latency or tail SLO. | Author task-success and exact next-tool-call Hit@1 evaluation; evidence does not establish safe speculative execution of irreversible tools or wall-clock benefit. |
| SF-2026-ARXIV-2607.25852 | Conversational, code and mathematics requests for Hy3-series targets; deployment replay includes Hunyuan production traffic and MATH-500 profiling. | Hy3-series targets including Hy3-295B-A21B, with workload-specialized MTP and block-diffusion drafters. | Single node with 8 NVIDIA H20 96 GB GPUs, tensor parallelism 8, for disclosed profiling/deployment measurements. | Not Disclosed — exact v1 does not state one numeric precision for the reported throughput results. | Production-traffic and benchmark-defined prompts; one prompt-length distribution is not fully disclosed. | MATH-500 profiler caps generation at 128 tokens; production-output distribution is not fully disclosed. | Dynamic live batches governed by D-cut; no single static batch size is the benchmark-wide contract. | 4–64 for headline Hy3-A21B throughput comparisons; production replay sweeps 2–64. | About 30% longer accepted spans on Hy3-A21B; 1.98–2.40x throughput over autoregressive decoding and 10.5–11.8% over DFlash. No production tail-latency/fairness SLO is disclosed. | Author throughput, acceptance-length and GPU-projected latency measurements after warm-up; CPU scheduling/queueing are excluded from the latency proxy, and the disclosed repository had no event-time commit. |
| SF-2026-ARXIV-2607.25884 | Hardware-in-the-loop mixed-precision quantization search and inference evaluation across paper-selected image-classification models/datasets. | Paper-selected classification model families; no one model identity governs the cross-platform headline. | Mobile/laptop CPUs and server GPUs enumerated by exact v1; Pareto policies are hardware-specific. | Mixed-precision policies searched in compiler IR; exact per-layer bit layouts vary by candidate and target. | Benchmark-defined image inputs; sequence length is not applicable. | Classification logits/top-1 label; generated-output length is not applicable. | Experiment-bound; no benchmark-wide batch size is disclosed as portable. | Not Disclosed — multi-request concurrency is not a search/evaluation dimension. | Up to 12.19x inference speedup with top-1 accuracy within 1.44 percentage points of the unquantized baseline; no production SLO. | Author top-1 accuracy and target-hardware latency/Pareto evaluation with online surrogate calibration; one policy is not transferable across hardware/compiler versions. |
| SF-2026-ARXIV-2607.25886 | Six software, terminal, science and mathematics benchmarks under a fixed data-centric post-training substrate and iterative checkpoint-feedback protocol. | Four frontier research agents; hosted agent/model versions are part of the benchmark identity and are not immutable in exact v1. | Fixed benchmark training/serving substrate, but physical accelerator identity is not disclosed as a portable field. | Fixed by the benchmark substrate but Not Disclosed as a numeric precision in the reported contract. | Benchmark-defined research tasks and fixed budgets; one prompt/token length is not disclosed. | Agent-generated data strategies and checkpoint trajectories; one output-length cap is not disclosed. | Fixed by the benchmark substrate but Not Disclosed as a public batch-size constant. | Not Disclosed — agent runs are evaluated as bounded research trajectories rather than production concurrent serving. | 58.33% of runs improve after the first valid attempt; 78.26% of searches that continue past their best checkpoint finish lower. No serving SLO is claimed. | Author benchmark-specific checkpoint evaluation retaining every attempt; hosted service/model/evaluator versions and drift remain part of the benchmark identity. |
| SF-2026-ARXIV-2607.25904 | GUI-RewardBench with 321 labeled task trajectories across 10 Ubuntu desktop application categories, plus OSWorld reinforcement-learning evaluation. | Not Disclosed as one immutable evaluator/agent version in exact v1. | Not Disclosed — desktop environment and tool interfaces are described, but accelerator identity is not bound to the headline results. | Not Disclosed — evaluator and policy numeric precision are not reported. | Task instruction, post-execution GUI/environment state and tool-acquired evidence; trajectory/token lengths are not fixed. | Proposed completion conditions, verification traces and a reward judgment; token/tool-call bounds are Not Disclosed. | Not Disclosed — evaluation/RL batch sizes are not part of the published result contract. | Not Disclosed — tool/evaluator concurrency is not evaluated. | 86.9% GUI-RewardBench evaluator accuracy and 34.0% OSWorld success when used for RL; tool latency and production SLO are not disclosed. | Author accuracy against labeled GUI-RewardBench outcomes and OSWorld task success; contamination, arbitrary-application transfer and evaluator noninterference are not established. |
| SF-2026-ARXIV-2607.25970 | DMC-Optim training tasks derived from programming-contest problems and LiveCodeBench-style held-out code-optimization evaluation with expanded correctness tests and calibrated runtime measurement. | Qwen2.5-7B and CWM-32B in the disclosed training/evaluation stages. | Remote calibrated execution service; physical hardware identity is experiment-specific and not disclosed as a portable target. | Not Disclosed — training and inference numeric precision are not stated as part of the benchmark contract. | Problem statements, reference programs and expanded tests; prompt/source-code lengths vary by task and are not fixed. | Generated optimized programs; source/token length limits are benchmark-specific and not disclosed as one constant. | Training/group sampling is method-specific; no benchmark-wide batch size is disclosed as portable. | Not Disclosed — remote measurement concurrency is not a reported control variable. | Correctness-gated speed reward and strict held-out percentile evaluation; no universal wall-clock speedup or production latency SLO. | Author expanded-test correctness gate plus calibrated remote timing and percentile ranking; hardware noise, service calibration and task distribution bound the result. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607.25255 | score_7_9;potential_books_delta | selected | DA-20260729-01 | — | 命中合同第一优先级 security contract；V2=9/9；Supports semantic taint propagation and workflow-level validation in the disclosed benchmarks. It does not prove labels are complete, adaptive attackers cannot evade reconstruction, or the framework withstands compromised hosts or model weights.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260729-01 |
| SF-2026-ARXIV-2607.25291 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: CoSA is a strong but specialized sparse-prefill proxy/kernel branch whose 128K gains are bound to two 8B models and one H20 node. Against selected 2607.25852, both compete for the inference-efficiency narrative slot, while AngelSpec exposes the broader batch-level ownership of proposal, verification budget and exact commit across heterogeneous live requests; CoSA remains the narrower attention-kernel mechanism. | analysis-decision:SF-2026-ARXIV-2607.25291 |
| SF-2026-ARXIV-2607.25431 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: CodeNib establishes commit-indexed multi-view repository context with operation-specific freshness and token savings, but it is confined to one coding-context substrate. Selected 2607.25886 covers the wider evaluation-lifecycle problem of freezing training, serving, sandbox and evaluator state while retaining a non-monotonic checkpoint trajectory, so CodeNib would add a narrower derived-view lifecycle rather than a fourth distinct system-evolution chain. | analysis-decision:SF-2026-ARXIV-2607.25431 |
| SF-2026-ARXIV-2607.25487 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: CoTinyVLA shows that temporal input and hierarchical Plan/Think distillation can substitute for backbone scale, but the evidence is bounded to LIBERO/LIBERO-Plus simulation and omits runtime hardware, control frequency and physical-safety SLO. The selected set already spans security authority, inference verification allocation and evaluation-substrate identity; adding this model-capacity branch would not displace any of those three more cross-component contracts. | analysis-decision:SF-2026-ARXIV-2607.25487 |
| SF-2026-ARXIV-2607.25498 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: DOPS makes operator placement and persistent weight layout dynamic on heterogeneous NPU/PIM systems, but its cost model and speedups are topology/configuration bound. Against selected 2607.25852 in the runtime-scheduling slot, AngelSpec has the more general request-level contract: workload-specific proposals, a shared live-batch verification budget and exact target commit; DOPS remains a hardware-specific execution-planning branch. | analysis-decision:SF-2026-ARXIV-2607.25498 |
| SF-2026-ARXIV-2607.25504 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: the dual-sparse contraction work demonstrates ISA/kernel co-design on a 12 nm custom vector cluster, with end-to-end Llama results modeled rather than measured on a general serving stack. It therefore has a narrower portability and system-reach boundary than selected 2607.25852, which changes verifier-compute allocation across live requests while preserving exact target ownership. | analysis-decision:SF-2026-ARXIV-2607.25504 |
| SF-2026-ARXIV-2607.25816 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: self-speculating tool calls reduce draft/target mismatch and improve next-call Hit@1, but exact v1 does not establish wall-clock benefit, side-effect isolation, hardware or concurrency behavior. Its proposal/commit concern overlaps selected 2607.25852, while irreversible-action authority is already represented more directly by selected 2607.25255; the disclosed evidence cannot displace either chain. | analysis-decision:SF-2026-ARXIV-2607.25816 |
| SF-2026-ARXIV-2607.25852 | score_7_9;potential_books_delta | selected | DA-20260729-02 | — | V2=9/9；Supports workload-specialized drafters and batch-level verification allocation in the disclosed stack. It does not prove a universal drafter choice, exact transfer to other targets/hardware or stable gains under production drift.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260729-02 |
| SF-2026-ARXIV-2607.25884 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: CONQuER closes mixed-precision search through compiler IR, surrogate prescreening and selective target-hardware calibration, but each Pareto policy remains tied to the measured model/compiler/hardware tuple. In the three-slot set, selected 2607.25852 carries a broader online inference-control contract across request confidence, load and exact verification; CONQuER is the more specialized compiler-policy branch. | analysis-decision:SF-2026-ARXIV-2607.25884 |
| SF-2026-ARXIV-2607.25886 | score_7_9;potential_books_delta | selected | DA-20260729-03 | — | V2=8/9；Supports isolating data-research decisions and preserving non-monotonic checkpoint trajectories. It does not prove recursive self-improvement, autonomous research reliability or transfer beyond the fixed stack.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260729-03 |
| SF-2026-ARXIV-2607.25904 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: IRA improves GUI reward grounding by proposing postconditions and reading hidden environment state, but its evidence covers 321 Ubuntu trajectories and one reward/evaluator loop with undisclosed model, hardware and tool-latency identity. Selected 2607.25886 addresses the broader evaluation-system contract—freezing the whole research substrate and retaining all checkpoint outcomes—so IRA remains a narrower evidence-sensor branch. | analysis-decision:SF-2026-ARXIV-2607.25904 |
| SF-2026-ARXIV-2607.25970 | score_7_9;potential_books_delta | not_selected | — | — | Pre-Books comparison: this work makes code runtime measurable enough to enter an RL reward through expanded tests, remote calibration and percentile evaluation, but the result is bound to DMC-Optim/LiveCodeBench-style tasks, two model scales and an experiment-specific execution service. Selected 2607.25886 covers the more general iterative-research identity problem across six benchmark families and full checkpoint trajectories; code-specific measurement-to-reward is the narrower branch. | analysis-decision:SF-2026-ARXIV-2607.25970 |

<!-- analysis:DA-20260729-01:start -->
### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

**旧方案为何合理。** Per-message prompt classifiers and per-agent policy checks are reasonable when harmful intent is local and each agent sees enough context. They fail when an objective is decomposed into locally benign-looking delegations.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization. 这条证据与现有主线的关系是 `Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization.`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Cross-agent context improves detection but adds labeling errors, reconstruction latency and graph-state retention. Static rules remain valid for small workflows; semantic taint is useful only when provenance and sink identities are trustworthy.

<!-- analysis:DA-20260729-01:end -->

<!-- analysis:DA-20260729-02:start -->
### AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding

**旧方案为何合理。** One universal drafter and fixed verify length are simple when workload entropy, batch composition and verification cost are stable.（现有命题定位：`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）

**约束变化与机制。** Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification. 这条证据与现有主线的关系是 `Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification.`：它改变或补充 `INFER-SPECULATIVE-DECODING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Specialization improves proposal efficiency but multiplies artifacts, routing errors and calibration. Shared verification allocation can starve hard requests; fixed budgets remain easier to reason about for homogeneous or strict-fairness workloads.

<!-- analysis:DA-20260729-02:end -->

<!-- analysis:DA-20260729-03:start -->
### RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

**旧方案为何合理。** End-to-end agent research benchmarks are realistic, but entangle data strategy with training, serving and evaluator implementation, making causal attribution weak.（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy. 这条证据与现有主线的关系是 `Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy.`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Fixing infrastructure improves attribution but narrows ecological validity. Retaining all checkpoints costs storage/evaluation; early stopping avoids regression but may miss delayed improvements. End-to-end benchmarks remain necessary after mechanism isolation.

<!-- analysis:DA-20260729-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25291:start -->《CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention》已完成 Deep Source Review。Pre-Books comparison: CoSA is a strong but specialized sparse-prefill proxy/kernel branch whose 128K gains are bound to two 8B models and one H20 node. Against selected 2607.25852, both compete for the inference-efficiency narrative slot, while AngelSpec exposes the broader batch-level ownership of proposal, verification budget and exact commit across heterogeneous live requests; CoSA remains the narrower attention-kernel mechanism.<!-- analysis-decision:SF-2026-ARXIV-2607.25291:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25431:start -->《CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents》已完成 Deep Source Review。Pre-Books comparison: CodeNib establishes commit-indexed multi-view repository context with operation-specific freshness and token savings, but it is confined to one coding-context substrate. Selected 2607.25886 covers the wider evaluation-lifecycle problem of freezing training, serving, sandbox and evaluator state while retaining a non-monotonic checkpoint trajectory, so CodeNib would add a narrower derived-view lifecycle rather than a fourth distinct system-evolution chain.<!-- analysis-decision:SF-2026-ARXIV-2607.25431:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25487:start -->《CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model》已完成 Deep Source Review。Pre-Books comparison: CoTinyVLA shows that temporal input and hierarchical Plan/Think distillation can substitute for backbone scale, but the evidence is bounded to LIBERO/LIBERO-Plus simulation and omits runtime hardware, control frequency and physical-safety SLO. The selected set already spans security authority, inference verification allocation and evaluation-substrate identity; adding this model-capacity branch would not displace any of those three more cross-component contracts.<!-- analysis-decision:SF-2026-ARXIV-2607.25487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25498:start -->《Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling》已完成 Deep Source Review。Pre-Books comparison: DOPS makes operator placement and persistent weight layout dynamic on heterogeneous NPU/PIM systems, but its cost model and speedups are topology/configuration bound. Against selected 2607.25852 in the runtime-scheduling slot, AngelSpec has the more general request-level contract: workload-specific proposals, a shared live-batch verification budget and exact target commit; DOPS remains a hardware-specific execution-planning branch.<!-- analysis-decision:SF-2026-ARXIV-2607.25498:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25504:start -->《At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference》已完成 Deep Source Review。Pre-Books comparison: the dual-sparse contraction work demonstrates ISA/kernel co-design on a 12 nm custom vector cluster, with end-to-end Llama results modeled rather than measured on a general serving stack. It therefore has a narrower portability and system-reach boundary than selected 2607.25852, which changes verifier-compute allocation across live requests while preserving exact target ownership.<!-- analysis-decision:SF-2026-ARXIV-2607.25504:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25816:start -->《Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL》已完成 Deep Source Review。Pre-Books comparison: self-speculating tool calls reduce draft/target mismatch and improve next-call Hit@1, but exact v1 does not establish wall-clock benefit, side-effect isolation, hardware or concurrency behavior. Its proposal/commit concern overlaps selected 2607.25852, while irreversible-action authority is already represented more directly by selected 2607.25255; the disclosed evidence cannot displace either chain.<!-- analysis-decision:SF-2026-ARXIV-2607.25816:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25884:start -->《CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates》已完成 Deep Source Review。Pre-Books comparison: CONQuER closes mixed-precision search through compiler IR, surrogate prescreening and selective target-hardware calibration, but each Pareto policy remains tied to the measured model/compiler/hardware tuple. In the three-slot set, selected 2607.25852 carries a broader online inference-control contract across request confidence, load and exact verification; CONQuER is the more specialized compiler-policy branch.<!-- analysis-decision:SF-2026-ARXIV-2607.25884:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25904:start -->《Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification》已完成 Deep Source Review。Pre-Books comparison: IRA improves GUI reward grounding by proposing postconditions and reading hidden environment state, but its evidence covers 321 Ubuntu trajectories and one reward/evaluator loop with undisclosed model, hardware and tool-latency identity. Selected 2607.25886 addresses the broader evaluation-system contract—freezing the whole research substrate and retaining all checkpoint outcomes—so IRA remains a narrower evidence-sensor branch.<!-- analysis-decision:SF-2026-ARXIV-2607.25904:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607.25970:start -->《Reinforcement Learning for Code Optimization》已完成 Deep Source Review。Pre-Books comparison: this work makes code runtime measurable enough to enter an RL reward through expanded tests, remote calibration and percentile evaluation, but the result is bound to DMC-Optim/LiveCodeBench-style tasks, two model scales and an experiment-specific execution service. Selected 2607.25886 covers the more general iterative-research identity problem across six benchmark families and full checkpoint trajectories; code-specific measurement-to-reward is the narrower branch.<!-- analysis-decision:SF-2026-ARXIV-2607.25970:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607.25255 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607.25255 | delta:SF-2026-ARXIV-2607.25255 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25255 |
| SF-2026-ARXIV-2607.25291 | INFER-PREFILL | books/part-05-inference-system/43-prefill.md#L1 | books/part-05-inference-system/42-what-happens-during-inference.md#L14-L14; books/part-05-inference-system/44-decode.md#L14-L14 | existing:SF-2026-ARXIV-2607.25291 | delta:SF-2026-ARXIV-2607.25291 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25291 |
| SF-2026-ARXIV-2607.25431 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L14-L14 | books/part-07-agent/74-prompt.md#L14-L14; books/part-07-agent/76-rag.md#L14-L14 | existing:SF-2026-ARXIV-2607.25431 | delta:SF-2026-ARXIV-2607.25431 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25431 |
| SF-2026-ARXIV-2607.25487 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607.25487 | delta:SF-2026-ARXIV-2607.25487 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607.25487 |
| SF-2026-ARXIV-2607.25498 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607.25498 | delta:SF-2026-ARXIV-2607.25498 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25498 |
| SF-2026-ARXIV-2607.25504 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607.25504 | delta:SF-2026-ARXIV-2607.25504 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25504 |
| SF-2026-ARXIV-2607.25816 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/47-pagedattention.md#L14-L14; books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | existing:SF-2026-ARXIV-2607.25816 | delta:SF-2026-ARXIV-2607.25816 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25816 |
| SF-2026-ARXIV-2607.25852 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/47-pagedattention.md#L14-L14; books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | existing:SF-2026-ARXIV-2607.25852 | delta:SF-2026-ARXIV-2607.25852 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25852 |
| SF-2026-ARXIV-2607.25884 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607.25884 | delta:SF-2026-ARXIV-2607.25884 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25884 |
| SF-2026-ARXIV-2607.25886 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607.25886 | delta:SF-2026-ARXIV-2607.25886 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607.25886 |
| SF-2026-ARXIV-2607.25904 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607.25904 | delta:SF-2026-ARXIV-2607.25904 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25904 |
| SF-2026-ARXIV-2607.25970 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L14-L14 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607.25970 | delta:SF-2026-ARXIV-2607.25970 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607.25970 |

<!-- books-review:SF-2026-ARXIV-2607.25255:start --><!-- existing:SF-2026-ARXIV-2607.25255:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607.25255:end --><!-- delta:SF-2026-ARXIV-2607.25255:start -->新增证据边界：Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25255:end --><!-- books-review:SF-2026-ARXIV-2607.25255:end -->

<!-- books-review:SF-2026-ARXIV-2607.25291:start --><!-- existing:SF-2026-ARXIV-2607.25291:start -->对读 `books/part-05-inference-system/43-prefill.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/43-prefill.md#L14-L14`）为：本章的核心判断是：**Prefill 将整段 prompt 映射为第一个 next-token distribution 和逐层 KV state；它利用 token 维度并行换取高 GPU efficiency，但工作量、显存峰值和调度占用会随 prompt 长度快速增长。**<!-- existing:SF-2026-ARXIV-2607.25291:end --><!-- delta:SF-2026-ARXIV-2607.25291:start -->新增证据边界：Direct Evolution: binary proxy mask -> ordered candidate mask -> online-softmax kernel refinement -> budget-aware sparse prefill. 该 delta 已进入 `books/part-05-inference-system/43-prefill.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25291:end --><!-- books-review:SF-2026-ARXIV-2607.25291:end -->

<!-- books-review:SF-2026-ARXIV-2607.25431:start --><!-- existing:SF-2026-ARXIV-2607.25431:start -->对读 `books/part-07-agent/75-context.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/75-context.md#L14-L14`）为：本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**<!-- existing:SF-2026-ARXIV-2607.25431:end --><!-- delta:SF-2026-ARXIV-2607.25431:start -->新增证据边界：Direct Evolution: task-local search -> commit-indexed reusable views -> operation-scoped incremental maintenance -> bounded context assembly. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607.25431:end --><!-- books-review:SF-2026-ARXIV-2607.25431:end -->

<!-- books-review:SF-2026-ARXIV-2607.25487:start --><!-- existing:SF-2026-ARXIV-2607.25487:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607.25487:end --><!-- delta:SF-2026-ARXIV-2607.25487:start -->新增证据边界：Alternative Branch: scale backbone capacity -> preserve temporal evidence -> distill slow Plan and fast Think state -> execute bounded action chunks. 该 delta 已进入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25487:end --><!-- books-review:SF-2026-ARXIV-2607.25487:end -->

<!-- books-review:SF-2026-ARXIV-2607.25498:start --><!-- existing:SF-2026-ARXIV-2607.25498:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607.25498:end --><!-- delta:SF-2026-ARXIV-2607.25498:start -->新增证据边界：Direct Evolution: phase placement -> operator DAG -> runtime contention-aware placement -> persistent weight-layout arbitration. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607.25498:end --><!-- books-review:SF-2026-ARXIV-2607.25498:end -->

<!-- books-review:SF-2026-ARXIV-2607.25504:start --><!-- existing:SF-2026-ARXIV-2607.25504:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607.25504:end --><!-- delta:SF-2026-ARXIV-2607.25504:start -->新增证据边界：Layering / Dependency: model sparsity -> Gustavson dataflow -> indexed ISA support -> calibrated cluster scale-out. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607.25504:end --><!-- books-review:SF-2026-ARXIV-2607.25504:end -->

<!-- books-review:SF-2026-ARXIV-2607.25816:start --><!-- existing:SF-2026-ARXIV-2607.25816:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2607.25816:end --><!-- delta:SF-2026-ARXIV-2607.25816:start -->新增证据边界：Direct Evolution: separate tool-call predictor -> same-model speculative mode -> self-rollout targets -> joint agent/speculator optimization with canonical commit. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25816:end --><!-- books-review:SF-2026-ARXIV-2607.25816:end -->

<!-- books-review:SF-2026-ARXIV-2607.25852:start --><!-- existing:SF-2026-ARXIV-2607.25852:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2607.25852:end --><!-- delta:SF-2026-ARXIV-2607.25852:start -->新增证据边界：Direct Evolution: universal drafter + fixed verify length -> workload-specialized proposal structures -> batch-level utility/cost allocation -> exact target verification. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25852:end --><!-- books-review:SF-2026-ARXIV-2607.25852:end -->

<!-- books-review:SF-2026-ARXIV-2607.25884:start --><!-- existing:SF-2026-ARXIV-2607.25884:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607.25884:end --><!-- delta:SF-2026-ARXIV-2607.25884:start -->新增证据边界：Direct Evolution: framework-side bit assignment -> compiler-visible quantization IR -> surrogate-prescreened search -> selective hardware calibration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25884:end --><!-- books-review:SF-2026-ARXIV-2607.25884:end -->

<!-- books-review:SF-2026-ARXIV-2607.25886:start --><!-- existing:SF-2026-ARXIV-2607.25886:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607.25886:end --><!-- delta:SF-2026-ARXIV-2607.25886:start -->新增证据边界：Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607.25886:end --><!-- books-review:SF-2026-ARXIV-2607.25886:end -->

<!-- books-review:SF-2026-ARXIV-2607.25904:start --><!-- existing:SF-2026-ARXIV-2607.25904:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607.25904:end --><!-- delta:SF-2026-ARXIV-2607.25904:start -->新增证据边界：Direct Evolution: screenshot judgment -> proposed postconditions -> read-only environment evidence -> reward with provenance. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607.25904:end --><!-- books-review:SF-2026-ARXIV-2607.25904:end -->

<!-- books-review:SF-2026-ARXIV-2607.25970:start --><!-- existing:SF-2026-ARXIV-2607.25970:start -->对读 `books/part-04-training-system/33-grpo.md#L14-L14` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607.25970:end --><!-- delta:SF-2026-ARXIV-2607.25970:start -->新增证据边界：Direct Evolution: hidden-test correctness reward -> calibrated performance evidence -> composite reward -> stabilized GRPO and held-out percentile evaluation. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607.25970:end --><!-- books-review:SF-2026-ARXIV-2607.25970:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260729-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260729; semantic-review:SA-20260729-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260729-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607.25255; review:SF-2026-ARXIV-2607.25291; review:SF-2026-ARXIV-2607.25431; review:SF-2026-ARXIV-2607.25487; review:SF-2026-ARXIV-2607.25498; review:SF-2026-ARXIV-2607.25504; review:SF-2026-ARXIV-2607.25816; review:SF-2026-ARXIV-2607.25852; review:SF-2026-ARXIV-2607.25884; review:SF-2026-ARXIV-2607.25886; review:SF-2026-ARXIV-2607.25904; review:SF-2026-ARXIV-2607.25970; semantic-review:SA-20260729-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260729-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260729-01; analysis:DA-20260729-02; analysis:DA-20260729-03; semantic-review:SA-20260729-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260729-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607.25255; books-review:SF-2026-ARXIV-2607.25291; books-review:SF-2026-ARXIV-2607.25431; books-review:SF-2026-ARXIV-2607.25487; books-review:SF-2026-ARXIV-2607.25498; books-review:SF-2026-ARXIV-2607.25504; books-review:SF-2026-ARXIV-2607.25816; books-review:SF-2026-ARXIV-2607.25852; books-review:SF-2026-ARXIV-2607.25884; books-review:SF-2026-ARXIV-2607.25886; books-review:SF-2026-ARXIV-2607.25904; books-review:SF-2026-ARXIV-2607.25970; semantic-review:SA-20260729-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260729-COVERAGE:start -->Fresh-context audit independently replayed 1201 unique arXiv v1 identities in the strict Beijing window [2026-07-28 09:00, 2026-07-29 09:00), verified the day-specific coverage snapshot SHA-256 and both archived Atom page hashes, and reconciled the same twelve-family denominator and first-public timestamps across replay snapshot, packet and Daily. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260729-COVERAGE:end -->
<!-- semantic-review:SA-20260729-EVIDENCE:start -->Fresh-context audit recomputed all twelve durable exact-v1 snapshot SHA-256 digests; checked Method, Evaluation, Limitations/counterevidence and artifact locators against the actual v1 sections; verified every structured ten-field benchmark contract and source-bounded Not Disclosed exception; and reconciled review provenance IDs across packet families, packet central receipts, the central receipt ledger and Daily. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260729-EVIDENCE:end -->
<!-- semantic-review:SA-20260729-SELECTION:start -->Fresh-context audit verified all twelve Deep-eligible families, exactly three selected narrative units and nine source-specific non-selection rationales. Every rationale is based on pre-Books evidence scope, workload boundary, owner reach, portability and narrative non-overlap; no Books disposition or Integration result is used to reverse-justify selection. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260729-SELECTION:end -->
<!-- semantic-review:SA-20260729-BOOKS:start -->Fresh-context audit verified seven Integrate outcomes in six canonical owner passages, their exact-v1 source notes and current adjacent chapter references, plus five bounded No Change outcomes whose long-term propositions are already present. The actual Books text preserves prior valid baselines, changed constraints, mechanism and state/control ownership, trade-offs, coexistence and evidence limits without promoting undisclosed artifacts or paper-specific benchmarks into general claims. Books PASS; finding_count=0.<!-- semantic-review:SA-20260729-BOOKS:end -->

## 8. Ignored Noise

1201 个窗口内 identity 中，1189 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：7 个 `Integrate`，5 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 12 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/29/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`、`books/part-05-inference-system/43-prefill.md`、`books/part-05-inference-system/48-speculative-decoding.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](https://arxiv.org/abs/2607.25255v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/abs/2607.25291v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents](https://arxiv.org/abs/2607.25431v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/abs/2607.25487v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/abs/2607.25498v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](https://arxiv.org/abs/2607.25504v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/abs/2607.25816v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/abs/2607.25852v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates](https://arxiv.org/abs/2607.25884v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](https://arxiv.org/abs/2607.25886v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/abs/2607.25904v1) — first-public（Asia/Shanghai）：2026-07-29；accessed：2026-08-27
- [Reinforcement Learning for Code Optimization](https://arxiv.org/abs/2607.25970v1) — first-public（Asia/Shanghai）：2026-07-29；accessed：2026-08-27
- [July recovery snapshot](../_sources/arxiv-v2.1-replay-20260727-31/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
