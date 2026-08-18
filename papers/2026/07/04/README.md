# Daily Research — 2026-07-04

**Research Date:** 2026-07-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-03 09:00:00 ～ 2026-07-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 849 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 9 个。当前路由账目为 2 个 Deep、0 个 Standard、7 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-04 |
| Window End | 2026-07-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-04-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T00:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-03T09:00:00+08:00 | 2026-07-04T09:00:00+08:00 | 2026-08-27T00:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 849 | SF-2026-ARXIV-2607-02865<br>SF-2026-ARXIV-2607-02882<br>SF-2026-ARXIV-2607-02980<br>SF-2026-ARXIV-2607-03146<br>SF-2026-ARXIV-2607-03182<br>SF-2026-ARXIV-2607-03333<br>SF-2026-ARXIV-2607-03449<br>SF-2026-ARXIV-2607-03461<br>SF-2026-ARXIV-2607-03473 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-04T09:00:00+08:00 | coverage:SRC-ARXIV:20260704 | GAP-ARXIV-DIRECT-RESET-20260704 |
| SRC-GITHUB-COMMIT | 2026-07-03T09:00:00+08:00 | 2026-07-04T09:00:00+08:00 | 2026-08-27T00:00:00+08:00 | exact GitHub commit API lookups: baihuajun24/spork@a027e4287758affd1fd4ecd0e1e79991faad1804 | checked | 1 | SF-2026-ARXIV-2607-03333 | pages=1; final cursors=a027e4287758affd1fd4ecd0e1e79991faad1804; one bounded commit lookup per family | 2026-07-04T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260704 | — |

<!-- coverage:SRC-ARXIV:20260704:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 849 unique identities in this strict window; 9 routed families.<!-- coverage:SRC-ARXIV:20260704:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260704:start -->repository=baihuajun24/spork, until=2026-07-03T13:51:32Z, full_sha=a027e4287758affd1fd4ecd0e1e79991faad1804, commit_timestamp=2026-07-03T13:05:25Z, url=https://github.com/baihuajun24/spork/commit/a027e4287758affd1fd4ecd0e1e79991faad1804; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260704:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 9 个 family：exact v1 为 2 个 family 披露 artifact/evidence locator，其中 2 个提供外部 repository/project/demo locator，另有 7 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02865 | arXiv:2607.02865v1 | paper-v1:2607.02865 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02865 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02882 | arXiv:2607.02882v1 | paper-v1:2607.02882 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02882 | self | — | new_in_window | AGENT-WORKFLOW | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02980 | arXiv:2607.02980v1 | paper-v1:2607.02980 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02980 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2607-02980 | yes |
| SF-2026-ARXIV-2607-03146 | arXiv:2607.03146v1 | paper-v1:2607.03146 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03146 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03182 | arXiv:2607.03182v1 | paper-v1:2607.03182 | 2026-W27 | 2026-07-03 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03182 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03333 | arXiv:2607.03333v1 | paper-v1:2607.03333 | 2026-W27 | 2026-07-03 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-03333 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2607-03333 | yes |
| SF-2026-ARXIV-2607-03449 | arXiv:2607.03449v1 | paper-v1:2607.03449 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03449 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03461 | arXiv:2607.03461v1 | paper-v1:2607.03461 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03461 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03473 | arXiv:2607.03473v1 | paper-v1:2607.03473 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03473 | self | — | new_in_window | INFER-SCHEDULING | Rejected — Low Durability / Out of Scope | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02865 | RP-07894bdef6bcecb1 | closure | doi:10.48550/arxiv.2607.02865@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02865@v1 | doi:10.48550/arxiv.2607.02865#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02865 | complete |
| SF-2026-ARXIV-2607-02882 | RP-ec5b72216dafb3d4 | closure | doi:10.48550/arxiv.2607.02882@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02882@v1 | doi:10.48550/arxiv.2607.02882#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02882 | complete |
| SF-2026-ARXIV-2607-02980 | RP-c099d1a1d6a7ec22 | deep | arXiv:2607.02980v1 | SRC-ARXIV@arXiv:2607.02980v1 | https://arxiv.org/html/2607.02980v1#S2.SS2 :: mean/max pooled chunk summaries cannot uniformly approximate query-dependent LogSumExp chunk mass; https://arxiv.org/html/2607.02980v1#S3 :: affine first-order chunk-mass surrogate and hierarchical inter-/intra-chunk normalization place retrieval scores in the forward path; https://arxiv.org/html/2607.02980v1#S4.SS1 through #S4.SS3 :: landmark/query calibration, HoPE/GQA variants, adjacent-query packing and checkpoint migration; https://arxiv.org/html/2607.02980v1#A1 and #A2 :: derivation and proof details | https://arxiv.org/html/2607.02980v1#S5.SS1 through #S5.SS3 :: 345M 8K/256K training, dense/sparse baselines, PPL, modified RULER/NIAH and ablations; https://arxiv.org/html/2607.02980v1#S6.SS1 and #S6.SS2 :: 1.4B from-scratch and OLMo3-7B conversion studies; https://arxiv.org/html/2607.02980v1#S7.SS1 and #S7.SS2 :: single-H800 SGLang/Triton inference and adjacent-query overlap; https://arxiv.org/html/2607.02980v1#A4 through #A8 :: recipes and evaluator details | https://arxiv.org/html/2607.02980v1#S4.SS1 and #S5.SS3 :: position encoding, query calibration and landmark choices materially affect extrapolation, and the calibration mechanism is not fully understood; https://arxiv.org/html/2607.02980v1#S6.SS2 :: 7B migration cost and short/general-task trade-offs remain recipe-bound; https://arxiv.org/html/2607.02980v1#S7.SS1 :: latency uses one H800, batch 1 and matched Triton kernels, with full attention faster below the reported crossover; Not Disclosed — no production concurrency/arrival/SLO study or independent replication | https://github.com/Tencent-Hunyuan/HiLS-Attention :: repository linked by v1; bounded event-time query found no commit at or before 2026-07-03T05:39:00Z. The first visible commit 562167440a4ae460c32e4e8136e0a2ee45e0b71d is five minutes after v1 and is not event-time implementation evidence. | claim:SF-2026-ARXIV-2607-02980 | complete |
| SF-2026-ARXIV-2607-03146 | RP-f01c95b0254f3666 | closure | doi:10.48550/arxiv.2607.03146@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03146@v1 | doi:10.48550/arxiv.2607.03146#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03146 | complete |
| SF-2026-ARXIV-2607-03182 | RP-645754c953c28d8a | closure | doi:10.48550/arxiv.2607.03182@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03182@v1 | doi:10.48550/arxiv.2607.03182#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03182 | complete |
| SF-2026-ARXIV-2607-03333 | RP-2a7770e7cef5c105 | deep | arXiv:2607.03333v1 | SRC-ARXIV@arXiv:2607.03333v1; SRC-GITHUB-COMMIT@commit:a027e4287758affd1fd4ecd0e1e79991faad1804 | https://arxiv.org/html/2607.03333v1#S2.SS2 :: overlap cost model and break-even condition; https://arxiv.org/html/2607.03333v1#S3 through #S5 :: forced-prefix self-probe, D1 prefix-KV fork, D2 confidence gate, D3 verified-prefix reuse, strict action-match commit and read-only manifest boundary; https://arxiv.org/html/2607.03333v1#A1, #A2 and #A8 :: derivation, partial-token acceptance and late-probe supersession | https://arxiv.org/html/2607.03333v1#S6.SS1 through #S6.SS6 :: Qwen3-4B/32B and Qwen3.5-35B-A3B on H20-3e, bf16, vLLM, greedy think-mode, GAIA/HotpotQA/tau2 latency and quality, component ablations, drafter comparison and break-even sweep; https://arxiv.org/html/2607.03333v1#A3 through #A7 :: BrowseComp, serving configuration and format-divergence details | https://arxiv.org/html/2607.03333v1#S6.SS3 and #S6.SS6 :: real-network nondeterminism, fast tools, short/no-think decode, format divergence, probe overhead and batching can shrink or reverse benefit; https://arxiv.org/html/2607.03333v1#S8 :: only read-only tools and open serving interfaces are in scope; https://arxiv.org/html/2607.03333v1#A6 through #A8 :: format collapse, small-model boundary and cancellation/supersession; exact action match does not undo quota, privacy or external side effects | https://github.com/baihuajun24/spork/tree/a027e4287758affd1fd4ecd0e1e79991faad1804 :: latest commit at or before v1, timestamp 2026-07-03T13:05:25Z; tree contains controller, gates, executor, vLLM integration, tau2 backend and evaluation entrypoints | claim:SF-2026-ARXIV-2607-03333 | complete |
| SF-2026-ARXIV-2607-03449 | RP-a8e88adcac516b2c | closure | doi:10.48550/arxiv.2607.03449@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03449@v1 | doi:10.48550/arxiv.2607.03449#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03449 | complete |
| SF-2026-ARXIV-2607-03461 | RP-2b95a209329062ca | closure | doi:10.48550/arxiv.2607.03461@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03461@v1 | doi:10.48550/arxiv.2607.03461#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03461 | complete |
| SF-2026-ARXIV-2607-03473 | RP-da06d14463a63a72 | closure | doi:10.48550/arxiv.2607.03473@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03473@v1 | doi:10.48550/arxiv.2607.03473#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03473 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-02865:start -->
#### DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning

<!-- claim:SF-2026-ARXIV-2607-02865:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02865:end -->

- Identity：`arXiv:2607.02865v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02865:end -->

<!-- review:SF-2026-ARXIV-2607-02882:start -->
#### Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference

<!-- claim:SF-2026-ARXIV-2607-02882:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02882:end -->

- Identity：`arXiv:2607.02882v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02882:end -->

<!-- review:SF-2026-ARXIV-2607-02980:start -->
#### Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling

<!-- claim:SF-2026-ARXIV-2607-02980:start -->Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02980:end -->

**旧方案与约束变化。** `Native sparse attention already couples selector training, block/GQA granularity and kernels, while teacher-owned stop-gradient warm-up provides an auditable migration path from dense checkpoints.`（`books/part-02-model/22-long-context.md#L194-L228`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02980v1#S2.SS2 :: mean/max pooled chunk summaries cannot uniformly approximate query-dependent LogSumExp chunk mass; https://arxiv.org/html/2607.02980v1#S3 :: affine first-order chunk-mass surrogate and hierarchical inter-/intra-chunk normalization place retrieval scores in the forward path; https://arxiv.org/html/2607.02980v1#S4.SS1 through #S4.SS3 :: landmark/query calibration, HoPE/GQA variants, adjacent-query packing and checkpoint migration; https://arxiv.org/html/2607.02980v1#A1 and #A2 :: derivation and proof details`；Evaluation：`https://arxiv.org/html/2607.02980v1#S5.SS1 through #S5.SS3 :: 345M 8K/256K training, dense/sparse baselines, PPL, modified RULER/NIAH and ablations; https://arxiv.org/html/2607.02980v1#S6.SS1 and #S6.SS2 :: 1.4B from-scratch and OLMo3-7B conversion studies; https://arxiv.org/html/2607.02980v1#S7.SS1 and #S7.SS2 :: single-H800 SGLang/Triton inference and adjacent-query overlap; https://arxiv.org/html/2607.02980v1#A4 through #A8 :: recipes and evaluator details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02980v1#S4.SS1 and #S5.SS3 :: position encoding, query calibration and landmark choices materially affect extrapolation, and the calibration mechanism is not fully understood; https://arxiv.org/html/2607.02980v1#S6.SS2 :: 7B migration cost and short/general-task trade-offs remain recipe-bound; https://arxiv.org/html/2607.02980v1#S7.SS1 :: latency uses one H800, batch 1 and matched Triton kernels, with full attention faster below the reported crossover; Not Disclosed — no production concurrency/arrival/SLO study or independent replication`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L540-L549`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-02980:end -->

<!-- review:SF-2026-ARXIV-2607-03146:start -->
#### Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations

<!-- claim:SF-2026-ARXIV-2607-03146:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03146:end -->

- Identity：`arXiv:2607.03146v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03146:end -->

<!-- review:SF-2026-ARXIV-2607-03182:start -->
#### AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning

<!-- claim:SF-2026-ARXIV-2607-03182:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03182:end -->

- Identity：`arXiv:2607.03182v1`；first-public（Asia/Shanghai）：`2026-07-03`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03182:end -->

<!-- review:SF-2026-ARXIV-2607-03333:start -->
#### SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference

<!-- claim:SF-2026-ARXIV-2607-03333:start -->Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03333:end -->

**旧方案与约束变化。** `Speculation is provisional work whose target/verifier owns commit; Agent phase hints may change proposal budgets but cannot change target authority, while tool authorization and side-effect classes remain outside the model.`（`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03333v1#S2.SS2 :: overlap cost model and break-even condition; https://arxiv.org/html/2607.03333v1#S3 through #S5 :: forced-prefix self-probe, D1 prefix-KV fork, D2 confidence gate, D3 verified-prefix reuse, strict action-match commit and read-only manifest boundary; https://arxiv.org/html/2607.03333v1#A1, #A2 and #A8 :: derivation, partial-token acceptance and late-probe supersession`；Evaluation：`https://arxiv.org/html/2607.03333v1#S6.SS1 through #S6.SS6 :: Qwen3-4B/32B and Qwen3.5-35B-A3B on H20-3e, bf16, vLLM, greedy think-mode, GAIA/HotpotQA/tau2 latency and quality, component ablations, drafter comparison and break-even sweep; https://arxiv.org/html/2607.03333v1#A3 through #A7 :: BrowseComp, serving configuration and format-divergence details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03333v1#S6.SS3 and #S6.SS6 :: real-network nondeterminism, fast tools, short/no-think decode, format divergence, probe overhead and batching can shrink or reverse benefit; https://arxiv.org/html/2607.03333v1#S8 :: only read-only tools and open serving interfaces are in scope; https://arxiv.org/html/2607.03333v1#A6 through #A8 :: format collapse, small-model boundary and cancellation/supersession; exact action match does not undo quota, privacy or external side effects`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-03333:end -->

<!-- review:SF-2026-ARXIV-2607-03449:start -->
#### HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

<!-- claim:SF-2026-ARXIV-2607-03449:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03449:end -->

- Identity：`arXiv:2607.03449v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03449:end -->

<!-- review:SF-2026-ARXIV-2607-03461:start -->
#### WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling

<!-- claim:SF-2026-ARXIV-2607-03461:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03461:end -->

- Identity：`arXiv:2607.03461v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03461:end -->

<!-- review:SF-2026-ARXIV-2607-03473:start -->
#### MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination

<!-- claim:SF-2026-ARXIV-2607-03473:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03473:end -->

- Identity：`arXiv:2607.03473v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03473:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02980 | 345M 8K from-scratch and 256K continued training; 1.4B/300B-token from-scratch; OLMo3-7B conversion; single-stream inference | 345M GPT-2-Medium-like; 1.4B; OLMo3-1025-7B | single NVIDIA H800 for disclosed inference; complete training topology Not Disclosed | bf16 for inference; complete training precision contract Not Disclosed | 8K/256K training; evaluation spans disclosed 512 through 4M contexts depending on study | Not Disclosed; not applicable to the prefill/PPL/retrieval runs, and generation length is not uniformly reported | batch 1 for inference; training/evaluation batch varies by recipe | single-stream inference; production concurrency Not Disclosed | No production SLO; paper reports PPL, retrieval/downstream quality, warm prefill and median per-token decode latency | paper-defined PPL, modified RULER/NIAH, downstream suites, LongBench-v1 and SGLang/Triton harness |
| SF-2026-ARXIV-2607-03333 | agentic read-only tool loops on GAIA, HotpotQA and tau2-bench; additional BrowseComp decomposition | Qwen3-4B, Qwen3-32B, Qwen3.5-35B-A3B | NVIDIA H20-3e 143 GiB; main TP=1, BrowseComp TP=4 on four GPUs | bf16 | benchmark-dependent; BrowseComp max_model_len=40960; exact per-query lengths otherwise Not Disclosed | thinking-mode decode; exact output-token distribution Not Disclosed | Not Disclosed uniformly across configurations | main and probe concurrent; BrowseComp workers=4; production arrival process Not Disclosed | No production SLO; paper reports end-to-end wall time, P50/P95/mean latency, EM/F1 and tool-latency break-even metrics | paper harness with real GAIA/HotpotQA APIs, tau2 tools and vLLM 0.19.1/0.18.1 |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02980 | score_7_9;potential_books_delta | selected | DA-20260704-2607-02980 | — | V2=8/9；Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260704-2607-02980 |
| SF-2026-ARXIV-2607-03333 | score_7_9;potential_books_delta | selected | DA-20260704-2607-03333 | — | V2=9/9；Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260704-2607-03333 |

<!-- analysis:DA-20260704-2607-03333:start -->
### SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference

**旧方案为何合理。** Serial tool dispatch remains the safest branch for writes, non-idempotent actions, fast tools, short/no-think generations, closed APIs and runtimes without shared prefix KV or token logprobs.（现有命题定位：`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）

**约束变化与机制。** Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `INFER-SPECULATIVE-DECODING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** SPORK overlaps only slow read-only tools with remaining reasoning and needs spare serving capacity, stable tool formatting, confidence calibration and open backend interfaces. Exact action match controls conversation commit but cannot undo quota, privacy exposure or remote reads; format divergence, heavy batching and short decode can erase the benefit. The next pressure is transactional authority for writes and multi-tenant tail-SLO accounting, neither of which v1 establishes.

<!-- analysis:DA-20260704-2607-03333:end -->

<!-- analysis:DA-20260704-2607-02980:start -->
### Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling

**旧方案为何合理。** Dense attention remains exact and often faster at short contexts; teacher-owned stop-gradient selectors preserve a stable dense semantic target and are easier to audit during checkpoint migration.（现有命题定位：`books/part-02-model/22-long-context.md#L194-L228`）

**约束变化与机制。** Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 这条证据与现有主线的关系是 `Alternative Branch`：它改变或补充 `MODEL-LONG-CONTEXT` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** HiLS gains a forward-coupled selection gradient and bounded sparse access only when landmark summaries, query calibration, HoPE/position rules, retrieval budget and sparse kernels remain compatible with the checkpoint. Missing a chunk remains unrecoverable; adjacent-query union can overfetch; full attention is faster below the disclosed crossover. Evidence is limited to the specified training recipes and one H800 batch-1 inference study, so the next pressure is selector/kernel portability and production multi-tenant validation.

<!-- analysis:DA-20260704-2607-02980:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02980 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L247 | books/part-02-model/21-moe.md#L1 | existing:SF-2026-ARXIV-2607-02980 | delta:SF-2026-ARXIV-2607-02980 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607-02980 |
| SF-2026-ARXIV-2607-03333 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L510 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2607-03333 | delta:SF-2026-ARXIV-2607-03333 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-03333 |

<!-- books-review:SF-2026-ARXIV-2607-02980:start --><!-- existing:SF-2026-ARXIV-2607-02980:start -->对读 `books/part-02-model/22-long-context.md#L247` 与相邻章节后，现有命题（`books/part-02-model/22-long-context.md#L194-L228`）为：Native sparse attention already couples selector training, block/GQA granularity and kernels, while teacher-owned stop-gradient warm-up provides an auditable migration path from dense checkpoints.<!-- existing:SF-2026-ARXIV-2607-02980:end --><!-- delta:SF-2026-ARXIV-2607-02980:start -->新增证据边界：Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该 delta 已进入 `books/part-02-model/22-long-context.md#L247`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-02980:end --><!-- books-review:SF-2026-ARXIV-2607-02980:end -->

<!-- books-review:SF-2026-ARXIV-2607-03333:start --><!-- existing:SF-2026-ARXIV-2607-03333:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L510` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）为：Speculation is provisional work whose target/verifier owns commit; Agent phase hints may change proposal budgets but cannot change target authority, while tool authorization and side-effect classes remain outside the model.<!-- existing:SF-2026-ARXIV-2607-03333:end --><!-- delta:SF-2026-ARXIV-2607-03333:start -->新增证据边界：Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L510`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-03333:end --><!-- books-review:SF-2026-ARXIV-2607-03333:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260704-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260704; semantic-review:SA-20260704-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260704-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-02865; review:SF-2026-ARXIV-2607-02882; review:SF-2026-ARXIV-2607-02980; review:SF-2026-ARXIV-2607-03146; review:SF-2026-ARXIV-2607-03182; review:SF-2026-ARXIV-2607-03333; review:SF-2026-ARXIV-2607-03449; review:SF-2026-ARXIV-2607-03461; review:SF-2026-ARXIV-2607-03473; semantic-review:SA-20260704-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260704-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260704-2607-03333; analysis:DA-20260704-2607-02980; semantic-review:SA-20260704-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260704-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-02980; books-review:SF-2026-ARXIV-2607-03333; semantic-review:SA-20260704-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260704-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260704-COVERAGE:end -->
<!-- semantic-review:SA-20260704-EVIDENCE:start -->Fresh-context review reconciled all 9 frozen families: 2 Deep, 0 Standard and 7 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260704-EVIDENCE:end -->
<!-- semantic-review:SA-20260704-SELECTION:start -->Fresh-context review reconciled 2 eligible Deep families: 2 selected and 0 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260704-SELECTION:end -->
<!-- semantic-review:SA-20260704-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 2 个 family 已定位到实际 Books 段落，0 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260704-BOOKS:end -->

## 8. Ignored Noise

849 个窗口内 identity 中，840 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：2 个 `Integrate`，0 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，7 个 `Rejected — Low Durability / Out of Scope`；Deep 2 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/04/README.md`。
- 本日报长期 delta 已同步至：`books/part-02-model/22-long-context.md`、`books/part-05-inference-system/48-speculative-decoding.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning](https://arxiv.org/abs/2607.02865v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference](https://arxiv.org/abs/2607.02882v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/abs/2607.02980v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-27
- [Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations](https://arxiv.org/abs/2607.03146v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning](https://arxiv.org/abs/2607.03182v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-26
- [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference](https://arxiv.org/abs/2607.03333v1) — first-public（Asia/Shanghai）：2026-07-03；accessed：2026-08-27
- [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](https://arxiv.org/abs/2607.03449v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling](https://arxiv.org/abs/2607.03461v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination](https://arxiv.org/abs/2607.03473v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
