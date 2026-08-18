# Daily Research — 2026-07-28

**Research Date:** 2026-07-28

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-27 09:00:00 ～ 2026-07-28 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；直接 arXiv 枚举冻结候选分母，技术 claim 回到精确 arXiv v1 与事件时 artifact receipt

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1174 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 12 个。当前路由账目为 12 个 Deep、0 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-28 |
| Window End | 2026-07-28 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-28-0900-v2.1-recovery-02 |
| Denominator Frozen At | 2026-08-27T20:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-27T09:00:00+08:00 | 2026-07-28T09:00:00+08:00 | 2026-08-27T20:30:00+08:00 | https://export.arxiv.org/api/query; submittedDate:[202607270100 TO 202607280100]; v1 published timestamp; cross-list deduplicated by arXiv ID | checked | 1174 | SF-2026-ARXIV-2607-23933<br>SF-2026-ARXIV-2607-23999<br>SF-2026-ARXIV-2607-24148<br>SF-2026-ARXIV-2607-24223<br>SF-2026-ARXIV-2607-24260<br>SF-2026-ARXIV-2607-24331<br>SF-2026-ARXIV-2607-24434<br>SF-2026-ARXIV-2607-24653<br>SF-2026-ARXIV-2607-24692<br>SF-2026-ARXIV-2607-24741<br>SF-2026-ARXIV-2607-25018<br>SF-2026-ARXIV-2607-25063 | archived pages arxiv-20260727-29-start0000.xml.gz and arxiv-20260727-29-start2000.xml.gz; strict-window filter; final_cursor=end | 2026-07-28T09:00:00+08:00 | coverage:SRC-ARXIV:20260728 | — |
| SRC-GITHUB-COMMIT | 2026-07-27T09:00:00+08:00 | 2026-07-28T09:00:00+08:00 | 2026-08-27T20:30:00+08:00 | exact GitHub commit API lookups: https://github.com/LeqsNaN/RARG@bbd912fc9d9b86899f59daaea701c54d0c80843c | checked | 1 | SF-2026-ARXIV-2607-24223 | pages=1; final cursors=bbd912fc9d9b86899f59daaea701c54d0c80843c; one bounded commit lookup per family | 2026-07-28T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260728 | — |

<!-- coverage:SRC-ARXIV:20260728:start -->Archived direct-arXiv submittedDate replay froze the strict-window denominator. Canonical source: papers/2026/07/_sources/arxiv-v2.1-replay-20260727-31/coverage-2026-07-28.json; sha256:9a868cb957813289b1a5bed2783d07e9af855a5329f81dbe462b55202926ccb8; 1174 unique identities in this strict window; 12 routed families.<!-- coverage:SRC-ARXIV:20260728:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260728:start -->repository=https://github.com/LeqsNaN/RARG, until=2026-07-28T01:00:00Z, full_sha=bbd912fc9d9b86899f59daaea701c54d0c80843c, commit_timestamp=2026-07-27T08:49:08Z, url=https://github.com/LeqsNaN/RARG/commit/bbd912fc9d9b86899f59daaea701c54d0c80843c; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260728:end -->

### Coverage Limitations

- 直接 arXiv replay 只闭合候选枚举与 first-public identity；机制和实验结论仍逐项来自 exact-v1 全文与可追溯 artifact。
- Artifact-boundary routing 覆盖 12 个 family：exact v1 为 4 个 family 披露 artifact/evidence locator，其中 2 个提供外部 repository/project/demo locator，另有 8 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23933 | arXiv:2607.23933v1 | paper-v1:2607.23933 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23933 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23933 | yes |
| SF-2026-ARXIV-2607-23999 | arXiv:2607.23999v1 | paper-v1:2607.23999 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23999 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-23999 | yes |
| SF-2026-ARXIV-2607-24148 | arXiv:2607.24148v1 | paper-v1:2607.24148 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24148 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-24148 | yes |
| SF-2026-ARXIV-2607-24223 | arXiv:2607.24223v1 | paper-v1:2607.24223 | 2026-W31 | 2026-07-27 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24223 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24223 | yes |
| SF-2026-ARXIV-2607-24260 | arXiv:2607.24260v1 | paper-v1:2607.24260 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24260 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-24260 | yes |
| SF-2026-ARXIV-2607-24331 | arXiv:2607.24331v1 | paper-v1:2607.24331 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24331 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24331 | yes |
| SF-2026-ARXIV-2607-24434 | arXiv:2607.24434v1 | paper-v1:2607.24434 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24434 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2607-24434 | yes |
| SF-2026-ARXIV-2607-24653 | arXiv:2607.24653v1 | paper-v1:2607.24653 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24653 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24653 | yes |
| SF-2026-ARXIV-2607-24692 | arXiv:2607.24692v1 | paper-v1:2607.24692 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24692 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-24692 | yes |
| SF-2026-ARXIV-2607-24741 | arXiv:2607.24741v1 | paper-v1:2607.24741 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24741 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2607-25018 | arXiv:2607.25018v1 | paper-v1:2607.25018 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25018 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-25018 | yes |
| SF-2026-ARXIV-2607-25063 | arXiv:2607.25063v1 | paper-v1:2607.25063 | 2026-W31 | 2026-07-28 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25063 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2607-25063 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23933 | RP-aaadf4a002b7e0d9 | deep | arXiv:2607.23933v1 | SRC-ARXIV@arXiv:2607.23933v1 | https://arxiv.org/html/2607.23933v1#S3; https://arxiv.org/html/2607.23933v1#S3.SS1; https://arxiv.org/html/2607.23933v1#S3.SS2; https://arxiv.org/html/2607.23933v1#S3.SS3 | https://arxiv.org/html/2607.23933v1#S5; https://arxiv.org/html/2607.23933v1#S5.SS2; https://arxiv.org/html/2607.23933v1#S5.SS3 | https://arxiv.org/html/2607.23933v1#S6 | Not Disclosed — exact v1 links component dependencies and public MCP tools, but no immutable author implementation or experiment commit. | claim:SF-2026-ARXIV-2607-23933 | complete |
| SF-2026-ARXIV-2607-23999 | RP-e32e592af5fcc825 | deep | arXiv:2607.23999v1 | SRC-ARXIV@arXiv:2607.23999v1 | https://arxiv.org/html/2607.23999v1#S4; https://arxiv.org/html/2607.23999v1#S4.SS2; https://arxiv.org/html/2607.23999v1#S4.SS3; https://arxiv.org/html/2607.23999v1#S4.SS4; https://arxiv.org/html/2607.23999v1#S5 | https://arxiv.org/html/2607.23999v1#S6; https://arxiv.org/html/2607.23999v1#S7 | https://arxiv.org/html/2607.23999v1#S8 | https://arxiv.org/html/2607.23999v1#S9 and https://arxiv.org/html/2607.23999v1#A12 — v1 discloses a reproducibility/artifact package inside the manuscript, but no immutable external repository commit. | claim:SF-2026-ARXIV-2607-23999 | complete |
| SF-2026-ARXIV-2607-24148 | RP-bb3cb64300baef50 | deep | arXiv:2607.24148v1 | SRC-ARXIV@arXiv:2607.24148v1 | https://arxiv.org/html/2607.24148v1#S4; https://arxiv.org/html/2607.24148v1#S5; https://arxiv.org/html/2607.24148v1#S6 | https://arxiv.org/html/2607.24148v1#S7; https://arxiv.org/html/2607.24148v1#S7.SS2; https://arxiv.org/html/2607.24148v1#S7.SS3 | https://arxiv.org/html/2607.24148v1#S7.SS4; https://arxiv.org/html/2607.24148v1#S8 | Not Disclosed — exact v1 exposes no immutable author implementation, accelerator RTL or experiment commit. | claim:SF-2026-ARXIV-2607-24148 | complete |
| SF-2026-ARXIV-2607-24223 | RP-ce63c127d7c43491 | deep | arXiv:2607.24223v1 | SRC-ARXIV@arXiv:2607.24223v1; SRC-GITHUB-COMMIT@commit:bbd912fc9d9b86899f59daaea701c54d0c80843c | https://arxiv.org/html/2607.24223v1#S3; https://arxiv.org/html/2607.24223v1#S3.SS2; https://arxiv.org/html/2607.24223v1#S3.SS3 | https://arxiv.org/html/2607.24223v1#S4; https://arxiv.org/html/2607.24223v1#S4.SS2; https://arxiv.org/html/2607.24223v1#S4.SS3 | https://arxiv.org/html/2607.24223v1#Sx1 | https://github.com/LeqsNaN/RARG/commit/bbd912fc9d9b86899f59daaea701c54d0c80843c — latest repository commit verified at or before the Daily cutoff; it supports artifact availability by cutoff, not identity with every reported experiment run. | claim:SF-2026-ARXIV-2607-24223 | complete |
| SF-2026-ARXIV-2607-24260 | RP-9935340099e244ea | deep | arXiv:2607.24260v1 | SRC-ARXIV@arXiv:2607.24260v1 | https://arxiv.org/html/2607.24260v1#S2.SS2; https://arxiv.org/html/2607.24260v1#S3; https://arxiv.org/html/2607.24260v1#S4 | https://arxiv.org/html/2607.24260v1#S5; https://arxiv.org/html/2607.24260v1#S5.SS2; https://arxiv.org/html/2607.24260v1#S5.SS3 | https://arxiv.org/html/2607.24260v1#S7 | Not Disclosed — exact v1 presents the GraphSpec compiler/executor realization but does not bind it to an immutable public implementation commit. | claim:SF-2026-ARXIV-2607-24260 | complete |
| SF-2026-ARXIV-2607-24331 | RP-e629da3ab32ad4f2 | deep | arXiv:2607.24331v1 | SRC-ARXIV@arXiv:2607.24331v1 | https://arxiv.org/html/2607.24331v1#S3; https://arxiv.org/html/2607.24331v1#S3.SS2; https://arxiv.org/html/2607.24331v1#S3.SS3 | https://arxiv.org/html/2607.24331v1#S4; https://arxiv.org/html/2607.24331v1#S4.SS2 | https://arxiv.org/html/2607.24331v1#S5 | Not Disclosed — exact v1 exposes no immutable author implementation or experiment commit. | claim:SF-2026-ARXIV-2607-24331 | complete |
| SF-2026-ARXIV-2607-24434 | RP-833186c0a5f7822d | deep | arXiv:2607.24434v1 | SRC-ARXIV@arXiv:2607.24434v1 | https://arxiv.org/html/2607.24434v1#Sx3; https://arxiv.org/html/2607.24434v1#Sx3.SSx2; https://arxiv.org/html/2607.24434v1#Sx3.SSx3 | https://arxiv.org/html/2607.24434v1#Sx4; https://arxiv.org/html/2607.24434v1#Sx4.SSx2 | https://arxiv.org/html/2607.24434v1#Sx4.SSx4; https://arxiv.org/html/2607.24434v1#Sx5 | Not Disclosed — exact v1 cites related DeepSpec/llama.cpp material but exposes no immutable DraftExpert implementation or experiment commit. | claim:SF-2026-ARXIV-2607-24434 | complete |
| SF-2026-ARXIV-2607-24653 | RP-a94f554dfdbb01cc | deep | arXiv:2607.24653v1 | SRC-ARXIV@arXiv:2607.24653v1 | https://arxiv.org/html/2607.24653v1#S2; https://arxiv.org/html/2607.24653v1#S3; https://arxiv.org/html/2607.24653v1#S4; https://arxiv.org/html/2607.24653v1#S5 | https://arxiv.org/html/2607.24653v1#S6 | Not Disclosed — exact v1 has no dedicated limitations section; the claim remains bounded to the disclosed architecture, training recipe and Section 6 evaluation, and aggregate quality cannot be attributed to any single component. | https://huggingface.co/moonshotai/Kimi-K3 and https://github.com/MoonshotAI/MoonEP — v1 discloses weights and component repositories, but no single immutable aggregate experiment commit for all architecture/training/serving claims. | claim:SF-2026-ARXIV-2607-24653 | complete |
| SF-2026-ARXIV-2607-24692 | RP-1b683a3d4e42cc94 | deep | arXiv:2607.24692v1 | SRC-ARXIV@arXiv:2607.24692v1 | https://arxiv.org/html/2607.24692v1#S2.SS2; https://arxiv.org/html/2607.24692v1#S2.SS3; https://arxiv.org/html/2607.24692v1#S3 | https://arxiv.org/html/2607.24692v1#S4; https://arxiv.org/html/2607.24692v1#S4.SS2 | https://arxiv.org/html/2607.24692v1#S3.SS1; https://arxiv.org/html/2607.24692v1#S5 | Not Disclosed — exact v1 exposes no immutable author implementation, trace dataset or experiment commit. | claim:SF-2026-ARXIV-2607-24692 | complete |
| SF-2026-ARXIV-2607-24741 | RP-52722c769d82a436 | deep | arXiv:2607.24741v1 | SRC-ARXIV@arXiv:2607.24741v1 | https://arxiv.org/html/2607.24741v1#S3; https://arxiv.org/html/2607.24741v1#S4; https://arxiv.org/html/2607.24741v1#S5 | https://arxiv.org/html/2607.24741v1#S6; https://arxiv.org/html/2607.24741v1#S6.SS2; https://arxiv.org/html/2607.24741v1#S6.SS3 | https://arxiv.org/html/2607.24741v1#S7; https://arxiv.org/html/2607.24741v1#S3.SS3 | https://arxiv.org/html/2607.24741v1#S8.SS0.SSS0.Px1 — v1 discloses a reproducibility statement but no immutable external repository or experiment commit. | claim:SF-2026-ARXIV-2607-24741 | complete |
| SF-2026-ARXIV-2607-25018 | RP-618476e4e530dd6a | deep | arXiv:2607.25018v1 | SRC-ARXIV@arXiv:2607.25018v1 | https://arxiv.org/html/2607.25018v1#S3; https://arxiv.org/html/2607.25018v1#S3.SS2; https://arxiv.org/html/2607.25018v1#S3.SS3; https://arxiv.org/html/2607.25018v1#S3.SS4 | https://arxiv.org/html/2607.25018v1#S5; https://arxiv.org/html/2607.25018v1#S5.SS2; https://arxiv.org/html/2607.25018v1#S5.SS3 | https://arxiv.org/html/2607.25018v1#S6.SS0.SSS0.Px2; https://arxiv.org/html/2607.25018v1#A12 | Not Disclosed — exact v1 exposes no immutable author implementation, calibration data artifact or experiment commit. | claim:SF-2026-ARXIV-2607-25018 | complete |
| SF-2026-ARXIV-2607-25063 | RP-8cf73a24734967f2 | deep | arXiv:2607.25063v1 | SRC-ARXIV@arXiv:2607.25063v1 | https://arxiv.org/html/2607.25063v1#S3; https://arxiv.org/html/2607.25063v1#S3.SS0.SSS0.Px2; https://arxiv.org/html/2607.25063v1#S3.SS0.SSS0.Px4 | https://arxiv.org/html/2607.25063v1#S4; https://arxiv.org/html/2607.25063v1#S4.SS2; https://arxiv.org/html/2607.25063v1#S4.SS4 | https://arxiv.org/html/2607.25063v1#A11 | Not Disclosed — exact v1 names public datasets and evaluation suites but exposes no immutable author training code, branch checkpoints or experiment commit. | claim:SF-2026-ARXIV-2607-25063 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-23933:start -->
#### SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving

<!-- claim:SF-2026-ARXIV-2607-23933:start -->Supports speculative preparation, its three timing opportunities and the disclosed prototype results. It does not prove intent prediction is safe authorization, that semantic cache hits preserve behavior, or that prewarming cannot leak capability or tenant state. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23933:end -->

**旧方案与约束变化。** `本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**`（`books/part-07-agent/84-agent-platform.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: lazy or permanently reserved sandbox -> intent-triggered in-step prewarm -> dependency-graph prefetch under an explicit budget -> final tool-call commit and reclaimable speculation. 它改变 `AGENT-PLATFORM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23933v1#S3; https://arxiv.org/html/2607.23933v1#S3.SS1; https://arxiv.org/html/2607.23933v1#S3.SS2; https://arxiv.org/html/2607.23933v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.23933v1#S5; https://arxiv.org/html/2607.23933v1#S5.SS2; https://arxiv.org/html/2607.23933v1#S5.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23933v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution: lazy or permanently reserved sandbox -> intent-triggered in-step prewarm -> dependency-graph prefetch under an explicit budget -> final tool-call commit and reclaimable speculation.`。
- Stable owner：`AGENT-PLATFORM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23933:end -->

<!-- review:SF-2026-ARXIV-2607-23999:start -->
#### ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents

<!-- claim:SF-2026-ARXIV-2607-23999:start -->Supports the trace schema, stage-scoped metrics and the finding that equal terminal outcomes can hide materially different propagation and authorized-utility behavior. It does not prove the evaluated defenses are complete, transfer to arbitrary providers/tools, or that absence of observed commits establishes safety. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23999:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23999v1#S4; https://arxiv.org/html/2607.23999v1#S4.SS2; https://arxiv.org/html/2607.23999v1#S4.SS3; https://arxiv.org/html/2607.23999v1#S4.SS4; https://arxiv.org/html/2607.23999v1#S5`；Evaluation：`https://arxiv.org/html/2607.23999v1#S6; https://arxiv.org/html/2607.23999v1#S7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23999v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence.`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23999:end -->

<!-- review:SF-2026-ARXIV-2607-24148:start -->
#### A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference

<!-- claim:SF-2026-ARXIV-2607-24148:start -->Supports state-conditioned codebook choice and centroid-reuse co-design in the tested VLA contract. It does not prove action magnitude is a reliable physical-risk signal, that arbitrary VLA weights quantize similarly, or that the custom accelerator speedup transfers to GPUs. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24148:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: fixed precision -> offline dual codebooks -> action-derived runtime phase signal -> codebook-index execution and centroid reuse on a matching accelerator. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24148v1#S4; https://arxiv.org/html/2607.24148v1#S5; https://arxiv.org/html/2607.24148v1#S6`；Evaluation：`https://arxiv.org/html/2607.24148v1#S7; https://arxiv.org/html/2607.24148v1#S7.SS2; https://arxiv.org/html/2607.24148v1#S7.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24148v1#S7.SS4; https://arxiv.org/html/2607.24148v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency: fixed precision -> offline dual codebooks -> action-derived runtime phase signal -> codebook-index execution and centroid reuse on a matching accelerator.`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-24148:end -->

<!-- review:SF-2026-ARXIV-2607-24223:start -->
#### A New Role for Relevance: Guiding Corpus Interaction in Agentic Search

<!-- claim:SF-2026-ARXIV-2607-24223:start -->Supports relevance-guided traversal, entry points and match reranking in the disclosed fixed-corpus agent. It does not prove relevance equals sufficiency, truth, authorization or causal usefulness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24223:end -->

**旧方案与约束变化。** `本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**`（`books/part-07-agent/76-rag.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: relevance as content filter -> relevance as corpus-interaction prior -> evidence-aware stopping and verification. 它改变 `AGENT-RAG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24223v1#S3; https://arxiv.org/html/2607.24223v1#S3.SS2; https://arxiv.org/html/2607.24223v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.24223v1#S4; https://arxiv.org/html/2607.24223v1#S4.SS2; https://arxiv.org/html/2607.24223v1#S4.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24223v1#Sx1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution: relevance as content filter -> relevance as corpus-interaction prior -> evidence-aware stopping and verification.`。
- Stable owner：`AGENT-RAG`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-24223:end -->

<!-- review:SF-2026-ARXIV-2607-24260:start -->
#### KAP: Bridging the Knowledge Selection–Runtime Consumption Gap in LLM Systems

<!-- claim:SF-2026-ARXIV-2607-24260:start -->Supports a plan-driven physical KV access abstraction and its disclosed positive-speedup regime. It does not prove the selected plan contains all causally needed context, preserve arbitrary open-ended generation, or beat dense attention when access becomes broad or gather overhead dominates. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24260:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24260v1#S2.SS2; https://arxiv.org/html/2607.24260v1#S3; https://arxiv.org/html/2607.24260v1#S4`；Evaluation：`https://arxiv.org/html/2607.24260v1#S5; https://arxiv.org/html/2607.24260v1#S5.SS2; https://arxiv.org/html/2607.24260v1#S5.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24260v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback.`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-24260:end -->

<!-- review:SF-2026-ARXIV-2607-24331:start -->
#### DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation

<!-- claim:SF-2026-ARXIV-2607-24331:start -->Supports asymmetric K/V treatment, CKA grouping and budgeted rank allocation under the tested models. It does not prove end-to-end memory/latency gains or a universal grouping policy. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24331:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: uniform low-rank KV -> K/V-asymmetric calibration -> similarity-based head groups -> adaptive rank allocation under a cache budget. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24331v1#S3; https://arxiv.org/html/2607.24331v1#S3.SS2; https://arxiv.org/html/2607.24331v1#S3.SS3`；Evaluation：`https://arxiv.org/html/2607.24331v1#S4; https://arxiv.org/html/2607.24331v1#S4.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24331v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution: uniform low-rank KV -> K/V-asymmetric calibration -> similarity-based head groups -> adaptive rank allocation under a cache budget.`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-24331:end -->

<!-- review:SF-2026-ARXIV-2607-24434:start -->
#### DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference

<!-- claim:SF-2026-ARXIV-2607-24434:start -->Supports expansion-aware drafting and expert prefetch for the tested edge/offload systems. It does not prove universal exact speedup, that acceptance alone predicts latency, or that extra training generalizes to other MoE routers. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24434:end -->

**旧方案与约束变化。** `本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**`（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: self-speculation optimized for acceptance -> include target-expert expansion/residency cost -> fixed-footprint draft expert + expansion-aware truncation -> exact target verification and token/KV commit. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24434v1#Sx3; https://arxiv.org/html/2607.24434v1#Sx3.SSx2; https://arxiv.org/html/2607.24434v1#Sx3.SSx3`；Evaluation：`https://arxiv.org/html/2607.24434v1#Sx4; https://arxiv.org/html/2607.24434v1#Sx4.SSx2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24434v1#Sx4.SSx4; https://arxiv.org/html/2607.24434v1#Sx5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution: self-speculation optimized for acceptance -> include target-expert expansion/residency cost -> fixed-footprint draft expert + expansion-aware truncation -> exact target verification and token/KV commit.`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-24434:end -->

<!-- review:SF-2026-ARXIV-2607-24653:start -->
#### Kimi K3: Open Frontier Intelligence

<!-- claim:SF-2026-ARXIV-2607-24653:start -->Supports disclosed architecture and system co-design claims plus public weights. It does not prove any single component causes aggregate quality or that the recipe is optimal for other scales/hardware. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24653:end -->

**旧方案与约束变化。** `本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。`（`books/part-02-model/21-moe.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: sparse routing objective -> executable balanced dispatch shape -> low-precision distributed training -> long-context serving and rollout state. 它改变 `MODEL-MOE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24653v1#S2; https://arxiv.org/html/2607.24653v1#S3; https://arxiv.org/html/2607.24653v1#S4; https://arxiv.org/html/2607.24653v1#S5`；Evaluation：`https://arxiv.org/html/2607.24653v1#S6`；Limitations/Counterevidence：`Not Disclosed — exact v1 has no dedicated limitations section; the claim remains bounded to the disclosed architecture, training recipe and Section 6 evaluation, and aggregate quality cannot be attributed to any single component.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency: sparse routing objective -> executable balanced dispatch shape -> low-precision distributed training -> long-context serving and rollout state.`。
- Stable owner：`MODEL-MOE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-24653:end -->

<!-- review:SF-2026-ARXIV-2607-24692:start -->
#### Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines

<!-- claim:SF-2026-ARXIV-2607-24692:start -->Supports a network-driven accuracy-collapse attack surface in deadline-gated multi-tier inference. It does not prove all jitter is adversarial, all late-result discard causes equivalent semantic loss, or that the proposed workload transfers unchanged to other pipelines. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24692:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Layering / Dependency: latency deadline as SLO -> deadline as merge/commit boundary -> shaped contention suppresses high-accuracy evidence -> availability protection must include semantic-quality residual risk. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24692v1#S2.SS2; https://arxiv.org/html/2607.24692v1#S2.SS3; https://arxiv.org/html/2607.24692v1#S3`；Evaluation：`https://arxiv.org/html/2607.24692v1#S4; https://arxiv.org/html/2607.24692v1#S4.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24692v1#S3.SS1; https://arxiv.org/html/2607.24692v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency: latency deadline as SLO -> deadline as merge/commit boundary -> shaped contention suppresses high-accuracy evidence -> availability protection must include semantic-quality residual risk.`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-24692:end -->

<!-- review:SF-2026-ARXIV-2607-24741:start -->
#### Certified Parallel-in-Time Sinkhorn for Dynamic Entropic Optimal Transport

<!-- claim:SF-2026-ARXIV-2607-24741:start -->Supports certified speculative batching for this positive entropic-OT map and numerical contract. It does not establish a general AI collective, inherit guarantees after changing the fixed-point map, or prove training throughput gains. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24741:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Principle Reuse: speculative candidate work -> independent current-instance verifier -> prefix commit + suffix repair; applied to a specialized Sinkhorn stream rather than general model decoding. 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24741v1#S3; https://arxiv.org/html/2607.24741v1#S4; https://arxiv.org/html/2607.24741v1#S5`；Evaluation：`https://arxiv.org/html/2607.24741v1#S6; https://arxiv.org/html/2607.24741v1#S6.SS2; https://arxiv.org/html/2607.24741v1#S6.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24741v1#S7; https://arxiv.org/html/2607.24741v1#S3.SS3`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Principle Reuse: speculative candidate work -> independent current-instance verifier -> prefix commit + suffix repair; applied to a specialized Sinkhorn stream rather than general model decoding.`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-24741:end -->

<!-- review:SF-2026-ARXIV-2607-25018:start -->
#### Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference

<!-- claim:SF-2026-ARXIV-2607-25018:start -->Supports conformal set-size routing and finite-sample marginal coverage under the stated assumptions. It does not provide unconditional correctness for open-ended generation, adversarial/domain drift or arbitrary adaptive selection. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-25018:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: raw confidence threshold -> held-out conformal calibration -> prediction-set commit/defer -> multi-tier risk/cost scheduling with explicit assumptions and fallback. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25018v1#S3; https://arxiv.org/html/2607.25018v1#S3.SS2; https://arxiv.org/html/2607.25018v1#S3.SS3; https://arxiv.org/html/2607.25018v1#S3.SS4`；Evaluation：`https://arxiv.org/html/2607.25018v1#S5; https://arxiv.org/html/2607.25018v1#S5.SS2; https://arxiv.org/html/2607.25018v1#S5.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25018v1#S6.SS0.SSS0.Px2; https://arxiv.org/html/2607.25018v1#A12`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution: raw confidence threshold -> held-out conformal calibration -> prediction-set commit/defer -> multi-tier risk/cost scheduling with explicit assumptions and fallback.`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-25018:end -->

<!-- review:SF-2026-ARXIV-2607-25063:start -->
#### Similar Models Learn Differently: Final Window Pretraining Shapes Post-Training Beyond SFT

<!-- claim:SF-2026-ARXIV-2607-25063:start -->Supports path-dependent post-training response under the controlled final-window interventions and falsifies interchangeability based only on matched post-SFT endpoints. It does not establish a universal causal law, optimal data ordering or general capability/safety improvement. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-25063:end -->

**旧方案与约束变化。** `本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。`（`books/part-04-training-system/28-pretraining.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability. 它改变 `TRAIN-PRETRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.25063v1#S3; https://arxiv.org/html/2607.25063v1#S3.SS0.SSS0.Px2; https://arxiv.org/html/2607.25063v1#S3.SS0.SSS0.Px4`；Evaluation：`https://arxiv.org/html/2607.25063v1#S4; https://arxiv.org/html/2607.25063v1#S4.SS2; https://arxiv.org/html/2607.25063v1#S4.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.25063v1#A11`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability.`。
- Stable owner：`TRAIN-PRETRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-25063:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23933 | High-concurrency multi-turn tool-agent traces evaluated by the author prototype. | Alibaba DashScope Qwen3.5-Max accessed through the production cloud API for Agent reasoning. | Agent runtime on a commodity server with a 16-core CPU, 256 GiB host memory and 2 TB NVMe SSD; remote model-serving hardware Not Disclosed. | Not Disclosed — the remote Qwen3.5-Max API does not disclose the numeric precision contract. | Multi-turn traces; exact token-length distribution Not Disclosed. | Tool-call trajectories; exact generated-token distribution Not Disclosed. | Not Disclosed — execution batch shape is not frozen. | Multi-tenant QPS sweep with the paper identifying QPS >= 8 as the high-load regime; production arrival and tenant distribution Not Disclosed. | P99 end-to-end latency and peak memory in the author prototype; broad multi-tenant isolation SLO Not Disclosed. | Author prototype trace, latency and memory measurements; not an independent evaluator. |
| SF-2026-ARXIV-2607-23999 | 504 synthetic scenarios and 17,640 structured tool-agent trace rows across seven policies and five seeds, plus a 6,048-rollout interface check and limited AgentDojo-native workflows. | Qwen2.5-7B-Instruct for the frozen main configuration; a separate Mistral/common-JSON interface check. | Not Disclosed — exact v1 does not bind the trace results to a reproducible hardware contract. | Not Disclosed — exact v1 does not disclose the inference precision contract. | Graph-shaped scenarios and tool-agent histories; token lengths Not Disclosed. | Structured actions, recipients and commits; token lengths Not Disclosed. | Seven policies by five seeds; execution batch size Not Disclosed. | Not Disclosed — the evaluation is rollout-based rather than a production concurrency study. | Security, memory/recovery, active-tainted utility and clean utility; not a latency SLO. | Author trace parser and benchmark metrics; not an independent evaluator. |
| SF-2026-ARXIV-2607-24148 | Disclosed VLA/robot tasks evaluated with model inference and a custom accelerator study. | OpenVLA, OpenVLA-OFT, RDT, Pi0 and GR00T in the disclosed experiment cells. | NVIDIA A100 80GB HBM2e baseline plus an author cycle-level accelerator simulator; the RTL study is synthesized at 28nm/500MHz and analytically scaled to 7nm. | FP16 for OpenVLA, FP32 for OpenVLA-OFT, and BF16 for RDT, Pi0 and GR00T in the disclosed baseline cells; VQVLA uses the paper-defined codebooks. | Robot observations and action-conditioned VLA inputs; sequence lengths Not Disclosed. | Robot action outputs; action horizon and token lengths vary by task and are not frozen as one contract. | Not Disclosed — exact v1 does not freeze one batch size across all model/task cells. | Not Disclosed — the study does not establish multi-tenant serving behavior. | Latency, energy and task success in the author workload; end-to-end control-frequency and physical-safety SLO Not Disclosed. | Author simulator and task-success evaluation; not an independent deployment evaluation. |
| SF-2026-ARXIV-2607-24223 | BrowseComp-Plus and BRIGHT-style fixed-corpus reasoning-retrieval tasks under disclosed tool budgets. | GPT-5.4-mini and GPT-5.4 at medium thinking effort plus GPT-5.4-nano at high thinking effort; Qwen3-Embedding-4B for BrowseComp-Plus and llama-nv-embed-reasoning-3b for BRIGHT retrieval components. | Not Disclosed — exact v1 does not provide a reproducible hardware contract for the reported frontier. | Not Disclosed — embedding and generator precision are not frozen as one contract. | BrowseComp-Plus uses a 100K-document corpus with a 1M-document expansion; BRIGHT uses four domain corpora. Tool-result compaction threshold is 230K, while exact per-query token lengths are not frozen. | Search trajectories and final answers; exact generated-token lengths Not Disclosed. | Not Disclosed — evaluation batch shape is not frozen. | Not Disclosed — this is not a production concurrency study. | BrowseComp-Plus answer accuracy and tool-call count plus BRIGHT nDCG@10; production latency SLO Not Disclosed. | GPT-5.1 LLM-as-judge for BrowseComp-Plus and nDCG@10 for BRIGHT in the author harness. |
| SF-2026-ARXIV-2607-24260 | GraphSpec long-context question answering over structured knowledge and source text. | Qwen3-VL-32B-Instruct used as both proposal and verification model with k=6 speculative tokens. | Four NVIDIA A800 80GB GPUs with tensor parallelism 4. | bfloat16 execution. | 4K to 128K tokens. | Task-dependent QA outputs; exact generated-token distribution Not Disclosed. | Not Disclosed — exact v1 does not freeze a serving batch contract. | Not Disclosed — multi-tenant concurrency is not evaluated. | Answer quality and proposal-time physical KV access; tail-latency SLO Not Disclosed. | Author GraphSpec experiments; exact public implementation provenance Not Disclosed. |
| SF-2026-ARXIV-2607-24331 | Long-context evaluation across three instruction-tuned LLMs comparing K-cache parameter reduction and task accuracy. | Llama-3.2-1B-Instruct (GQA), Qwen1.5-1.8B-Chat (MHA) and SmolLM2-1.7B-Instruct (MHA). | Single NVIDIA T4 GPU. | Not Disclosed — physical cache encoding precision is not frozen as one contract. | Long-context tasks; exact per-cell sequence lengths remain experiment-specific. | Task-dependent outputs; exact generated-token lengths Not Disclosed. | Not Disclosed — continuous-batching behavior is not evaluated. | Not Disclosed — multi-tenant concurrency is not evaluated. | K-cache parameter budget and task accuracy; tail-latency SLO Not Disclosed. | Author long-context evaluation; not an independent evaluator. |
| SF-2026-ARXIV-2607-24434 | Latency-critical single-user MoE decoding with CPU-to-GPU and Flash-to-NPU expert offload. | DeepSeek-V2-Lite and Moonlight-16B-A3B. | NVIDIA RTX 4090 24GB for CPU-GPU experiments and Hexagon HTP v81 NPU with Flash storage for on-device experiments. | BF16 PyTorch on GPU and Q4_0 llama.cpp on NPU in the disclosed configurations. | Task-dependent prompts; exact prompt-length distribution Not Disclosed. | Decode-128 profiling and generation experiments as disclosed; broader output-length distribution Not Disclosed. | Single-user decode; production batching Not Disclosed. | Single-user latency-critical workload; multi-tenant concurrency Not Disclosed. | Decode throughput, acceptance and prefetch hit rate; production tail-latency SLO Not Disclosed. | Author platform measurements on the disclosed devices. |
| SF-2026-ARXIV-2607-24653 | Technical-report evaluation suites spanning reasoning, coding, agentic and million-token-context tasks. | Kimi K3, 2.8T total parameters with 104B active parameters. | Not Disclosed — the report does not provide a complete reproducible hardware recipe for aggregate results. | Low-precision training is described at a high level; one exact aggregate precision contract for all results is Not Disclosed. | Up to one million tokens in the disclosed long-context contract. | Task-dependent outputs; one frozen output-length distribution is Not Disclosed. | Not Disclosed — aggregate training and evaluation batch contracts are incomplete. | Not Disclosed — production serving concurrency is not established. | Benchmark quality and training-system evidence; production serving SLO Not Disclosed. | Author technical-report suites; component attribution and independent replication are incomplete. |
| SF-2026-ARXIV-2607-24692 | Simulated edge-cloud multi-object-tracking pipeline with about 4,000 burst requests. | Fast/slow detection paths disclosed by exact v1; the study does not freeze one general model identity. | Simulated edge-cloud topology; exact reproducible hardware deployment Not Disclosed. | Not Disclosed — detector precision is not frozen as one contract. | Tracked video frames and slow-path requests; token length is not the workload unit. | Tracking/detection results; token length is not the workload unit. | About 4,000 shaped burst requests; execution batch size Not Disclosed. | Burst workload; exact concurrent-request distribution Not Disclosed. | P99 deadline behavior and HOTA accuracy under attack; one application/topology only. | Author simulation and tracking metrics; not an independent deployment study. |
| SF-2026-ARXIV-2607-24741 | Dynamic entropic optimal-transport instance streams evaluated with a parallel-in-time Sinkhorn solver. | Specialized Sinkhorn solver; this is not an LLM model benchmark. | Single-node 4x NVIDIA A100 and 8x NVIDIA A100 configurations. | FP64 and FP32 evidence cells. | Sequences of related optimal-transport instances; tensor sizes are experiment-cell specific. | Transport solutions and certificates; token length is not applicable. | Windowed parallel-in-time instances; exact window/batch values are experiment-cell specific. | Four or eight GPUs on one node. | Wall time plus marginal-residual/tolerance certificate; not a model-serving SLO. | Author-controlled 30 paired runs; cross-node behavior not evaluated. |
| SF-2026-ARXIV-2607-25018 | Eighteen multiple-choice benchmarks evaluated as two-tier LLM cascades with N=16 samples per tier per query at temperature 0.7. | Two-tier combinations from Llama, Gemma, Ministral and Phi open-weight instruction-tuned families. | Four NVIDIA B200 SXM6 GPUs for the full evaluation. | Not Disclosed — inference precision is not frozen. | Multiple-choice prompts; exact token-length distribution Not Disclosed. | Multiple-choice outputs with repeated samples; open-ended generation is not established. | Four model families by eighteen benchmarks with N=16 samples per tier per query; execution microbatch Not Disclosed. | Four-GPU evaluation; production request concurrency is not evaluated. | Marginal coverage and expected cascade cost under exchangeability; not a latency-tail SLO. | Author conformal evaluation; tighter bounds additionally require selection preservation. |
| SF-2026-ARXIV-2607-25063 | Continued pretraining over matched 500M-token final windows followed by fixed Tulu-style SFT and UltraFeedback DPO; selected GRPO/RLVR and order-reversal checks. | OLMo-2-0425-1B main study with a Pythia-1B-deduped replication and a saturated approximately 4T-token fork check. | NVIDIA A100 80GB; two GPUs with FSDP for training and one GPU for generation evaluation. | Not Disclosed — exact v1 does not freeze one numeric-precision contract for all stages. | 500M-token final pretraining windows; per-sequence context length Not Disclosed. | Task-dependent generation during evaluation; exact output-length distribution Not Disclosed. | Three seeds; optimizer batch/microbatch contract Not Disclosed. | Two-GPU training and one-GPU generation evaluation; serving concurrency is not applicable. | Refusal erosion and capability retention across ordered training stages; not a serving SLO. | lm-eval-harness, WildGuard and author stage-wise metrics. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23933 | score_7_9;potential_books_delta | not_selected | — | — | SpecBox changes sandbox preparation timing through speculative prewarm, but its evidence is bounded to one agent-serving resource policy and its principal risk is wasted or unsafe preparation. Relative to selected 2607.23999, it does not introduce the broader stage-scoped evidence semantics needed to distinguish exposure, proposal, authorization and commit across system boundaries; selecting both would spend two narrative slots on adjacent agent-runtime control paths. | analysis-decision:SF-2026-ARXIV-2607-23933 |
| SF-2026-ARXIV-2607-23999 | score_7_9;potential_books_delta | selected | DA-20260728-01 | — | 命中合同第一优先级 security contract；V2=8/9；Supports the trace schema, stage-scoped metrics and the finding that equal terminal outcomes can hide materially different propagation and authorized-utility behavior. It does not prove the evaluated defenses are complete, transfer to arbitrary providers/tools, or that absence of observed commits establishes safety.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260728-01 |
| SF-2026-ARXIV-2607-24148 | score_7_9;potential_books_delta | not_selected | — | — | VQVLA provides a precision-selection and accelerator co-design branch, but the evidence is bound to the disclosed VLA models, motion-phase calibration and custom hardware assumptions. Relative to selected 2607.24260, it changes one embodied execution branch rather than establishing a general logical-to-physical state interface across long-context runtimes, so the latter has wider owner reach and a less workload-specific evolution chain. | analysis-decision:SF-2026-ARXIV-2607-24148 |
| SF-2026-ARXIV-2607-24223 | score_7_9;potential_books_delta | not_selected | — | — | RARG changes corpus-interaction policy through relevance-guided search and supplies an event-time artifact, but its system delta remains inside search-trajectory selection. Relative to selected 2607.24260, it does not compile a logical selection into a versioned physical KV access-plan contract, and its narrative would overlap the day's broader theme of selection without adding the same execution-state identity boundary. | analysis-decision:SF-2026-ARXIV-2607-24223 |
| SF-2026-ARXIV-2607-24260 | score_7_9;potential_books_delta | selected | DA-20260728-02 | — | V2=8/9；Supports a plan-driven physical KV access abstraction and its disclosed positive-speedup regime. It does not prove the selected plan contains all causally needed context, preserve arbitrary open-ended generation, or beat dense attention when access becomes broad or gather overhead dominates.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260728-02 |
| SF-2026-ARXIV-2607-24331 | score_7_9;potential_books_delta | not_selected | — | — | DynaCalKV adds head grouping and adaptive rank allocation inside KV compression, with evidence centered on representation size and retained task quality. Relative to selected 2607.24260, it does not change who owns the logical-to-physical access-plan interface; selecting both would duplicate the KV-state narrative while the GraphSpec chain exposes a more general execution contract and failure boundary. | analysis-decision:SF-2026-ARXIV-2607-24331 |
| SF-2026-ARXIV-2607-24434 | score_7_9;potential_books_delta | not_selected | — | — | DraftExpert changes speculation accounting for edge MoE expert expansion, but its evidence is bound to two models and specific CPU-GPU or Flash-NPU residency paths. Relative to selected 2607.24260, it is a specialized offload branch rather than a broadly reusable state-selection contract, so it receives full evidence review without occupying a top-level narrative slot. | analysis-decision:SF-2026-ARXIV-2607-24434 |
| SF-2026-ARXIV-2607-24653 | score_7_9;potential_books_delta | not_selected | — | — | Kimi K3 is a broad technical report with strong architecture and training evidence, but its claims span many components and aggregate quality cannot be attributed to one mechanism. Selected 2607.25063 isolates a falsifiable training-path identity contract under controlled interventions; that narrower causal unit provides a clearer non-overlapping evolution narrative than another whole-model architecture summary. | analysis-decision:SF-2026-ARXIV-2607-24653 |
| SF-2026-ARXIV-2607-24692 | score_7_9;potential_books_delta | not_selected | — | — | Denial of Deadline shows that latency pressure can become accuracy loss through a deadline-sensitive fallback path, but the evidence is limited to one simulated tracking topology. Relative to selected 2607.23999, the stage-aware trace schema generalizes the evidence unit across exposure, propagation, authorization and commit, whereas this family supplies a narrower security failure branch. | analysis-decision:SF-2026-ARXIV-2607-24692 |
| SF-2026-ARXIV-2607-24741 | score_7_9;potential_books_delta | not_selected | — | — | The certified parallel-in-time Sinkhorn solver provides useful distributed-algorithm evidence, but it is specialized to an entropic optimal-transport workload and its reusable contribution is the proof-and-correction pattern rather than a new AI lifecycle state owner. Relative to selected 2607.25063, it does not alter a canonical model artifact or training-path identity contract. | analysis-decision:SF-2026-ARXIV-2607-24741 |
| SF-2026-ARXIV-2607-25018 | score_7_9;potential_books_delta | not_selected | — | — | Conformal Cascade contributes a routing branch with finite-sample coverage under exchangeability and additional selection-preservation assumptions. Relative to selected 2607.25063, its guarantee is narrower and workload-assumption bound, while the selected family changes the more fundamental identity of a checkpoint as an ordered training-path artifact; the latter therefore carries the day's training-system narrative slot. | analysis-decision:SF-2026-ARXIV-2607-25018 |
| SF-2026-ARXIV-2607-25063 | score_7_9;potential_books_delta | selected | DA-20260728-03 | — | V2=7/9；Supports path-dependent post-training response under the controlled final-window interventions and falsifies interchangeability based only on matched post-SFT endpoints. It does not establish a universal causal law, optimal data ordering or general capability/safety improvement.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260728-03 |

<!-- analysis:DA-20260728-01:start -->
### ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents

**旧方案为何合理。** Terminal attack-success and policy-violation rates are cheap and useful when there is one input and one effect boundary. They become ambiguous once untrusted content can propagate through memory, delegation and multiple tool proposals before any side effect commits.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence. 这条证据与现有主线的关系是 `Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence.`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Trace-level evaluation improves localization and exposes overblocking, but requires versioned parsers, policies, scenario hashes and provenance storage. Metrics remain sensitive to stage selection, normalization and schema alignment; a common benchmark blind spot can make multiple defenses fail together.

<!-- analysis:DA-20260728-01:end -->

<!-- analysis:DA-20260728-02:start -->
### KAP: Bridging the Knowledge Selection–Runtime Consumption Gap in LLM Systems

**旧方案为何合理。** Flattening all evidence into the prompt and attending over full KV is simple and faithful when contexts are short, access is dense or irregular gathers cost more than saved HBM traffic.（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）

**约束变化与机制。** Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback. 这条证据与现有主线的关系是 `Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback.`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The IR can reduce memory traffic but introduces compiler correctness, plan staleness, irregular gather kernels, plan/cache identity and a mandatory fallback. Richer retrieval structure helps only if the serving backend can consume it without breaking logical prompt semantics.

<!-- analysis:DA-20260728-02:end -->

<!-- analysis:DA-20260728-03:start -->
### Similar Models Learn Differently: Final Window Pretraining Shapes Post-Training Beyond SFT

**旧方案为何合理。** Treating checkpoints with matched loss and post-SFT benchmarks as interchangeable is cheap and often adequate when subsequent training is small or the handoff is purely inference. It becomes unsafe for selecting a base checkpoint for further optimization.（现有命题定位：`books/part-04-training-system/28-pretraining.md#L14-L14`）

**约束变化与机制。** Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability. 这条证据与现有主线的关系是 `Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability.`：它改变或补充 `TRAIN-PRETRAINING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Preserving ordered training lineage and stage-wise evaluations increases artifact/evaluation cost but prevents a later update from hiding pretraining imprint. The effect can shrink at saturated scale and may trade target retention against other capabilities.

<!-- analysis:DA-20260728-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23933:start -->《SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving》已完成 Deep Source Review。SpecBox changes sandbox preparation timing through speculative prewarm, but its evidence is bounded to one agent-serving resource policy and its principal risk is wasted or unsafe preparation. Relative to selected 2607.23999, it does not introduce the broader stage-scoped evidence semantics needed to distinguish exposure, proposal, authorization and commit across system boundaries; selecting both would spend two narrative slots on adjacent agent-runtime control paths.<!-- analysis-decision:SF-2026-ARXIV-2607-23933:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24148:start -->《A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference》已完成 Deep Source Review。VQVLA provides a precision-selection and accelerator co-design branch, but the evidence is bound to the disclosed VLA models, motion-phase calibration and custom hardware assumptions. Relative to selected 2607.24260, it changes one embodied execution branch rather than establishing a general logical-to-physical state interface across long-context runtimes, so the latter has wider owner reach and a less workload-specific evolution chain.<!-- analysis-decision:SF-2026-ARXIV-2607-24148:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24223:start -->《A New Role for Relevance: Guiding Corpus Interaction in Agentic Search》已完成 Deep Source Review。RARG changes corpus-interaction policy through relevance-guided search and supplies an event-time artifact, but its system delta remains inside search-trajectory selection. Relative to selected 2607.24260, it does not compile a logical selection into a versioned physical KV access-plan contract, and its narrative would overlap the day's broader theme of selection without adding the same execution-state identity boundary.<!-- analysis-decision:SF-2026-ARXIV-2607-24223:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24331:start -->《DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation》已完成 Deep Source Review。DynaCalKV adds head grouping and adaptive rank allocation inside KV compression, with evidence centered on representation size and retained task quality. Relative to selected 2607.24260, it does not change who owns the logical-to-physical access-plan interface; selecting both would duplicate the KV-state narrative while the GraphSpec chain exposes a more general execution contract and failure boundary.<!-- analysis-decision:SF-2026-ARXIV-2607-24331:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24434:start -->《DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference》已完成 Deep Source Review。DraftExpert changes speculation accounting for edge MoE expert expansion, but its evidence is bound to two models and specific CPU-GPU or Flash-NPU residency paths. Relative to selected 2607.24260, it is a specialized offload branch rather than a broadly reusable state-selection contract, so it receives full evidence review without occupying a top-level narrative slot.<!-- analysis-decision:SF-2026-ARXIV-2607-24434:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24653:start -->《Kimi K3: Open Frontier Intelligence》已完成 Deep Source Review。Kimi K3 is a broad technical report with strong architecture and training evidence, but its claims span many components and aggregate quality cannot be attributed to one mechanism. Selected 2607.25063 isolates a falsifiable training-path identity contract under controlled interventions; that narrower causal unit provides a clearer non-overlapping evolution narrative than another whole-model architecture summary.<!-- analysis-decision:SF-2026-ARXIV-2607-24653:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24692:start -->《Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines》已完成 Deep Source Review。Denial of Deadline shows that latency pressure can become accuracy loss through a deadline-sensitive fallback path, but the evidence is limited to one simulated tracking topology. Relative to selected 2607.23999, the stage-aware trace schema generalizes the evidence unit across exposure, propagation, authorization and commit, whereas this family supplies a narrower security failure branch.<!-- analysis-decision:SF-2026-ARXIV-2607-24692:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24741:start -->《Certified Parallel-in-Time Sinkhorn for Dynamic Entropic Optimal Transport》已完成 Deep Source Review。The certified parallel-in-time Sinkhorn solver provides useful distributed-algorithm evidence, but it is specialized to an entropic optimal-transport workload and its reusable contribution is the proof-and-correction pattern rather than a new AI lifecycle state owner. Relative to selected 2607.25063, it does not alter a canonical model artifact or training-path identity contract.<!-- analysis-decision:SF-2026-ARXIV-2607-24741:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25018:start -->《Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference》已完成 Deep Source Review。Conformal Cascade contributes a routing branch with finite-sample coverage under exchangeability and additional selection-preservation assumptions. Relative to selected 2607.25063, its guarantee is narrower and workload-assumption bound, while the selected family changes the more fundamental identity of a checkpoint as an ordered training-path artifact; the latter therefore carries the day's training-system narrative slot.<!-- analysis-decision:SF-2026-ARXIV-2607-25018:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23933 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L14-L14 | books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-23933 | delta:SF-2026-ARXIV-2607-23933 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23933 |
| SF-2026-ARXIV-2607-23999 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L261 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-23999 | delta:SF-2026-ARXIV-2607-23999 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23999 |
| SF-2026-ARXIV-2607-24148 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L549 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-24148 | delta:SF-2026-ARXIV-2607-24148 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-24148 |
| SF-2026-ARXIV-2607-24223 | AGENT-RAG | books/part-07-agent/76-rag.md#L14-L14 | books/part-07-agent/75-context.md#L14-L14; books/part-07-agent/77-memory.md#L14-L14 | existing:SF-2026-ARXIV-2607-24223 | delta:SF-2026-ARXIV-2607-24223 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24223 |
| SF-2026-ARXIV-2607-24260 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L138 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-24260 | delta:SF-2026-ARXIV-2607-24260 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-24260 |
| SF-2026-ARXIV-2607-24331 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-24331 | delta:SF-2026-ARXIV-2607-24331 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24331 |
| SF-2026-ARXIV-2607-24434 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L548 | books/part-05-inference-system/47-pagedattention.md#L14-L14; books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | existing:SF-2026-ARXIV-2607-24434 | delta:SF-2026-ARXIV-2607-24434 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-24434 |
| SF-2026-ARXIV-2607-24653 | MODEL-MOE | books/part-02-model/21-moe.md#L14-L14 | books/part-02-model/20-sampling.md#L14-L14; books/part-02-model/22-long-context.md#L14-L14 | existing:SF-2026-ARXIV-2607-24653 | delta:SF-2026-ARXIV-2607-24653 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24653 |
| SF-2026-ARXIV-2607-24692 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L684 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-24692 | delta:SF-2026-ARXIV-2607-24692 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-24692 |
| SF-2026-ARXIV-2607-25018 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L189 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-25018 | delta:SF-2026-ARXIV-2607-25018 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-25018 |
| SF-2026-ARXIV-2607-25063 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L527 | books/part-04-training-system/27-data.md#L14-L14; books/part-04-training-system/29-sft.md#L14-L14 | existing:SF-2026-ARXIV-2607-25063 | delta:SF-2026-ARXIV-2607-25063 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-25063 |

<!-- books-review:SF-2026-ARXIV-2607-23933:start --><!-- existing:SF-2026-ARXIV-2607-23933:start -->对读 `books/part-07-agent/84-agent-platform.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/84-agent-platform.md#L14-L14`）为：本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**<!-- existing:SF-2026-ARXIV-2607-23933:end --><!-- delta:SF-2026-ARXIV-2607-23933:start -->新增证据边界：Direct Evolution: lazy or permanently reserved sandbox -> intent-triggered in-step prewarm -> dependency-graph prefetch under an explicit budget -> final tool-call commit and reclaimable speculation. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23933:end --><!-- books-review:SF-2026-ARXIV-2607-23933:end -->

<!-- books-review:SF-2026-ARXIV-2607-23999:start --><!-- existing:SF-2026-ARXIV-2607-23999:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L261` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-23999:end --><!-- delta:SF-2026-ARXIV-2607-23999:start -->新增证据边界：Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L261`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23999:end --><!-- books-review:SF-2026-ARXIV-2607-23999:end -->

<!-- books-review:SF-2026-ARXIV-2607-24148:start --><!-- existing:SF-2026-ARXIV-2607-24148:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L549` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-24148:end --><!-- delta:SF-2026-ARXIV-2607-24148:start -->新增证据边界：Layering / Dependency: fixed precision -> offline dual codebooks -> action-derived runtime phase signal -> codebook-index execution and centroid reuse on a matching accelerator. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L549`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-24148:end --><!-- books-review:SF-2026-ARXIV-2607-24148:end -->

<!-- books-review:SF-2026-ARXIV-2607-24223:start --><!-- existing:SF-2026-ARXIV-2607-24223:start -->对读 `books/part-07-agent/76-rag.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/76-rag.md#L14-L14`）为：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2607-24223:end --><!-- delta:SF-2026-ARXIV-2607-24223:start -->新增证据边界：Direct Evolution: relevance as content filter -> relevance as corpus-interaction prior -> evidence-aware stopping and verification. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-24223:end --><!-- books-review:SF-2026-ARXIV-2607-24223:end -->

<!-- books-review:SF-2026-ARXIV-2607-24260:start --><!-- existing:SF-2026-ARXIV-2607-24260:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L138` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-24260:end --><!-- delta:SF-2026-ARXIV-2607-24260:start -->新增证据边界：Layering / Dependency: flat prompt + dense KV -> structured knowledge selection -> versioned runtime access plan -> sparse physical KV consumption with exact semantic fallback. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L138`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-24260:end --><!-- books-review:SF-2026-ARXIV-2607-24260:end -->

<!-- books-review:SF-2026-ARXIV-2607-24331:start --><!-- existing:SF-2026-ARXIV-2607-24331:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-24331:end --><!-- delta:SF-2026-ARXIV-2607-24331:start -->新增证据边界：Direct Evolution: uniform low-rank KV -> K/V-asymmetric calibration -> similarity-based head groups -> adaptive rank allocation under a cache budget. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-24331:end --><!-- books-review:SF-2026-ARXIV-2607-24331:end -->

<!-- books-review:SF-2026-ARXIV-2607-24434:start --><!-- existing:SF-2026-ARXIV-2607-24434:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L548` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L16-L16`）为：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2607-24434:end --><!-- delta:SF-2026-ARXIV-2607-24434:start -->新增证据边界：Direct Evolution: self-speculation optimized for acceptance -> include target-expert expansion/residency cost -> fixed-footprint draft expert + expansion-aware truncation -> exact target verification and token/KV commit. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L548`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-24434:end --><!-- books-review:SF-2026-ARXIV-2607-24434:end -->

<!-- books-review:SF-2026-ARXIV-2607-24653:start --><!-- existing:SF-2026-ARXIV-2607-24653:start -->对读 `books/part-02-model/21-moe.md#L14-L14` 与相邻章节后，现有命题（`books/part-02-model/21-moe.md#L14-L14`）为：本章的核心判断是：**MoE 将总参数容量与单 token active parameters 部分解耦，代价是让模型每次前向都动态决定计算与通信路径。**稀疏的是激活路径，不代表 expert weights 使用稀疏矩阵存储。<!-- existing:SF-2026-ARXIV-2607-24653:end --><!-- delta:SF-2026-ARXIV-2607-24653:start -->新增证据边界：Layering / Dependency: sparse routing objective -> executable balanced dispatch shape -> low-precision distributed training -> long-context serving and rollout state. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-24653:end --><!-- books-review:SF-2026-ARXIV-2607-24653:end -->

<!-- books-review:SF-2026-ARXIV-2607-24692:start --><!-- existing:SF-2026-ARXIV-2607-24692:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L684` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-24692:end --><!-- delta:SF-2026-ARXIV-2607-24692:start -->新增证据边界：Layering / Dependency: latency deadline as SLO -> deadline as merge/commit boundary -> shaped contention suppresses high-accuracy evidence -> availability protection must include semantic-quality residual risk. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L684`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-24692:end --><!-- books-review:SF-2026-ARXIV-2607-24692:end -->

<!-- books-review:SF-2026-ARXIV-2607-25018:start --><!-- existing:SF-2026-ARXIV-2607-25018:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L189` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-25018:end --><!-- delta:SF-2026-ARXIV-2607-25018:start -->新增证据边界：Direct Evolution: raw confidence threshold -> held-out conformal calibration -> prediction-set commit/defer -> multi-tier risk/cost scheduling with explicit assumptions and fallback. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L189`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-25018:end --><!-- books-review:SF-2026-ARXIV-2607-25018:end -->

<!-- books-review:SF-2026-ARXIV-2607-25063:start --><!-- existing:SF-2026-ARXIV-2607-25063:start -->对读 `books/part-04-training-system/28-pretraining.md#L527` 与相邻章节后，现有命题（`books/part-04-training-system/28-pretraining.md#L14-L14`）为：本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。<!-- existing:SF-2026-ARXIV-2607-25063:end --><!-- delta:SF-2026-ARXIV-2607-25063:start -->新增证据边界：Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L527`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-25063:end --><!-- books-review:SF-2026-ARXIV-2607-25063:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260728-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260728; semantic-review:SA-20260728-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260728-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-23933; review:SF-2026-ARXIV-2607-23999; review:SF-2026-ARXIV-2607-24148; review:SF-2026-ARXIV-2607-24223; review:SF-2026-ARXIV-2607-24260; review:SF-2026-ARXIV-2607-24331; review:SF-2026-ARXIV-2607-24434; review:SF-2026-ARXIV-2607-24653; review:SF-2026-ARXIV-2607-24692; review:SF-2026-ARXIV-2607-24741; review:SF-2026-ARXIV-2607-25018; review:SF-2026-ARXIV-2607-25063; semantic-review:SA-20260728-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260728-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260728-01; analysis:DA-20260728-02; analysis:DA-20260728-03; semantic-review:SA-20260728-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260728-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-23933; books-review:SF-2026-ARXIV-2607-23999; books-review:SF-2026-ARXIV-2607-24148; books-review:SF-2026-ARXIV-2607-24223; books-review:SF-2026-ARXIV-2607-24260; books-review:SF-2026-ARXIV-2607-24331; books-review:SF-2026-ARXIV-2607-24434; books-review:SF-2026-ARXIV-2607-24653; books-review:SF-2026-ARXIV-2607-24692; books-review:SF-2026-ARXIV-2607-25018; books-review:SF-2026-ARXIV-2607-25063; review:SF-2026-ARXIV-2607-24741; semantic-review:SA-20260728-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260728-COVERAGE:start -->Fresh-context audit independently recomputed 1174 unique raw arXiv v1 identities in the strict Beijing window [2026-07-27 09:00, 2026-07-28 09:00), verified the day-specific snapshot SHA and both archived Atom page hashes, and reconciled the same twelve-family denominator and first-public timestamps across snapshot, packet and Daily. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260728-COVERAGE:end -->
<!-- semantic-review:SA-20260728-EVIDENCE:start -->Fresh-context audit verified all twelve exact-v1 snapshot hashes, Method/Evaluation/Limitations locators, source-bounded claims, structured ten-field benchmark contracts and review provenance IDs across packet families, packet central receipts, the central receipt ledger and Daily. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260728-EVIDENCE:end -->
<!-- semantic-review:SA-20260728-SELECTION:start -->Fresh-context re-audit verified three selected and nine non-selected Deep families. Every non-selection rationale is source-specific and uses only pre-Books evidence scope, workload boundary, owner reach, durability, failure boundary and narrative non-overlap; no Books disposition is used to reverse-justify selection. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260728-SELECTION:end -->
<!-- semantic-review:SA-20260728-BOOKS:start -->Fresh-context audit verified seven Integrate outcomes in their canonical owners, four source-bounded No Change outcomes and one Weekly Only outcome. The actual Books passages preserve mechanism, state/control ownership, trade-offs, coexistence boundaries and exact-v1 evidence limits without promoting unverified implementation claims. Books PASS; finding_count=0.<!-- semantic-review:SA-20260728-BOOKS:end -->

## 8. Ignored Noise

1174 个窗口内 identity 中，1162 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：7 个 `Integrate`，4 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 12 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/28/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/28-pretraining.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/48-speculative-decoding.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving](https://arxiv.org/abs/2607.23933v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [ContainmentBench: Trace-Based Evaluation of Post-Injection Containment in Tool-Using LLM Agents](https://arxiv.org/abs/2607.23999v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [A Motion-Aware Vector Quantization Framework with Centroid Reuse for Efficient VLA Inference](https://arxiv.org/abs/2607.24148v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [A New Role for Relevance: Guiding Corpus Interaction in Agentic Search](https://arxiv.org/abs/2607.24223v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [KAP: Bridging the Knowledge Selection–Runtime Consumption Gap in LLM Systems](https://arxiv.org/abs/2607.24260v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](https://arxiv.org/abs/2607.24331v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/abs/2607.24434v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [Kimi K3: Open Frontier Intelligence](https://arxiv.org/abs/2607.24653v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Denial of Deadline: Network-Driven Accuracy Collapse in Distributed Inference Pipelines](https://arxiv.org/abs/2607.24692v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Certified Parallel-in-Time Sinkhorn for Dynamic Entropic Optimal Transport](https://arxiv.org/abs/2607.24741v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference](https://arxiv.org/abs/2607.25018v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [Similar Models Learn Differently: Final Window Pretraining Shapes Post-Training Beyond SFT](https://arxiv.org/abs/2607.25063v1) — first-public（Asia/Shanghai）：2026-07-28；accessed：2026-08-27
- [July recovery snapshot](../_sources/arxiv-v2.1-replay-20260727-31/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
