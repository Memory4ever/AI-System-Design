# Daily Research — 2026-07-05

**Research Date:** 2026-07-05

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-04 09:00:00 ～ 2026-07-05 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 442 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 6 个。当前路由账目为 1 个 Deep、0 个 Standard、5 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-05 |
| Window End | 2026-07-05 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-05-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T11:20:07+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-04T09:00:00+08:00 | 2026-07-05T09:00:00+08:00 | 2026-08-27T11:20:07+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 442 | SF-2026-ARXIV-2607-03693<br>SF-2026-ARXIV-2607-03751<br>SF-2026-ARXIV-2607-03870<br>SF-2026-ARXIV-2607-03876<br>SF-2026-ARXIV-2607-03948<br>SF-2026-ARXIV-2607-03964 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-05T09:00:00+08:00 | coverage:SRC-ARXIV:20260705 | GAP-ARXIV-DIRECT-RESET-20260705 |
| SRC-GITHUB-COMMIT | 2026-07-04T09:00:00+08:00 | 2026-07-05T09:00:00+08:00 | 2026-08-27T11:20:07+08:00 | exact GitHub commit API lookups: qqwetidx/Online-Linear-Programming-for-Vidur@c14eea013db3d60ad1aba0780a3d65688bfb9c19 | checked | 1 | SF-2026-ARXIV-2607-03948 | pages=1; final cursors=c14eea013db3d60ad1aba0780a3d65688bfb9c19; one bounded commit lookup per family | 2026-07-05T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260705 | — |

<!-- coverage:SRC-ARXIV:20260705:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 442 unique identities in this strict window; 6 routed families.<!-- coverage:SRC-ARXIV:20260705:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260705:start -->repository=qqwetidx/Online-Linear-Programming-for-Vidur, until=2026-07-04T16:48:37Z, full_sha=c14eea013db3d60ad1aba0780a3d65688bfb9c19, commit_timestamp=2026-01-18T05:01:02Z, url=https://github.com/qqwetidx/Online-Linear-Programming-for-Vidur/commit/c14eea013db3d60ad1aba0780a3d65688bfb9c19; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260705:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 6 个 family：exact v1 为 1 个 family 披露 artifact/evidence locator，其中 1 个提供外部 repository/project/demo locator，另有 5 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-03693 | arXiv:2607.03693v1 | paper-v1:2607.03693 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03693 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03751 | arXiv:2607.03751v1 | paper-v1:2607.03751 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03751 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03870 | arXiv:2607.03870v1 | paper-v1:2607.03870 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03870 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03876 | arXiv:2607.03876v1 | paper-v1:2607.03876 | 2026-W27 | 2026-07-04 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03876 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03948 | arXiv:2607.03948v1 | paper-v1:2607.03948 | 2026-W27 | 2026-07-05 | SRC-ARXIV; SRC-GITHUB-COMMIT | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-03948 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-03948 | yes |
| SF-2026-ARXIV-2607-03964 | arXiv:2607.03964v1 | paper-v1:2607.03964 | 2026-W27 | 2026-07-05 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03964 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-03693 | RP-d0e200b9a5a2c2b0 | closure | doi:10.48550/arxiv.2607.03693@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03693@v1 | doi:10.48550/arxiv.2607.03693#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03693 | complete |
| SF-2026-ARXIV-2607-03751 | RP-d1a366b09494410b | closure | doi:10.48550/arxiv.2607.03751@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03751@v1 | doi:10.48550/arxiv.2607.03751#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03751 | complete |
| SF-2026-ARXIV-2607-03870 | RP-c988939d3418394c | closure | doi:10.48550/arxiv.2607.03870@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03870@v1 | doi:10.48550/arxiv.2607.03870#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03870 | complete |
| SF-2026-ARXIV-2607-03876 | RP-73744f4b5304744b | closure | doi:10.48550/arxiv.2607.03876@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03876@v1 | doi:10.48550/arxiv.2607.03876#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03876 | complete |
| SF-2026-ARXIV-2607-03948 | RP-905250919facbb59 | deep | arXiv:2607.03948v1 | SRC-ARXIV@arXiv:2607.03948v1; SRC-GITHUB-COMMIT@commit:c14eea013db3d60ad1aba0780a3d65688bfb9c19 | https://arxiv.org/html/2607.03948v1#S2.SS0.SSS0.Px2, #S2.SS0.SSS0.Px5 and #S2.SS0.SSS0.Px6 :: central buffering, release-when-startable admission and time-coupled batch/KV occupancy; https://arxiv.org/html/2607.03948v1#S3.SS1 through #S3.SS3 :: SLO-weighted action reward, online LP constraints, dual shadow prices, SAA history and projected subgradient updates; https://arxiv.org/html/2607.03948v1#A2.SS1 and #A2.SS3 :: pseudocode | https://arxiv.org/html/2607.03948v1#S4.SS1 :: Vidur-only simulation on four A100 GPUs with LMSYS-Chat-1M and synthetic P/D-ratio workloads; model, precision, batch/concurrency and exact serving SLO Not Disclosed; https://arxiv.org/html/2607.03948v1#S4.SS2 and #S4.SS3 :: RR/LOR/Random/Power-of-2 baselines, noisy length estimates, objective sweeps and an arrival-rate shift; https://arxiv.org/html/2607.03948v1#A3 :: broader sweeps and tail-weight sensitivity | https://arxiv.org/html/2607.03948v1#S6 :: simulation-only, without serving-engine integration, preemption, KV swapping, distributed coordination, heterogeneous priorities or fairness validation; https://arxiv.org/html/2607.03948v1#A1.SS0.SSS0.Px9 :: PD-mixing duration is input-dependent; no LLM-specific theorem/regret/convergence or component ablation. Event-time artifact only partially corresponds to the manuscript noisy-length/tail-objective interface. | https://github.com/qqwetidx/Online-Linear-Programming-for-Vidur/tree/c14eea013db3d60ad1aba0780a3d65688bfb9c19 :: only repository commit, authored 2026-01-18 before v1; implements time-indexed batch/KV occupancy, projected dual-price updates and margin-ranked feasible admission, but only partially reproduces the full manuscript objective/prediction contract | claim:SF-2026-ARXIV-2607-03948 | complete |
| SF-2026-ARXIV-2607-03964 | RP-974c5c8e73366b61 | closure | doi:10.48550/arxiv.2607.03964@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03964@v1 | doi:10.48550/arxiv.2607.03964#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03964 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-03693:start -->
#### CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

<!-- claim:SF-2026-ARXIV-2607-03693:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03693:end -->

- Identity：`arXiv:2607.03693v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03693:end -->

<!-- review:SF-2026-ARXIV-2607-03751:start -->
#### Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models

<!-- claim:SF-2026-ARXIV-2607-03751:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03751:end -->

- Identity：`arXiv:2607.03751v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03751:end -->

<!-- review:SF-2026-ARXIV-2607-03870:start -->
#### Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth

<!-- claim:SF-2026-ARXIV-2607-03870:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03870:end -->

- Identity：`arXiv:2607.03870v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03870:end -->

<!-- review:SF-2026-ARXIV-2607-03876:start -->
#### AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference

<!-- claim:SF-2026-ARXIV-2607-03876:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03876:end -->

- Identity：`arXiv:2607.03876v1`；first-public（Asia/Shanghai）：`2026-07-04`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03876:end -->

<!-- review:SF-2026-ARXIV-2607-03948:start -->
#### Online Linear Programming for Multi-Objective Routing in LLM Serving

<!-- claim:SF-2026-ARXIV-2607-03948:start -->When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03948:end -->

**旧方案与约束变化。** `Ch56 already separates admission, iteration scheduling, routing/placement and autoscaling and requires future-KV feasibility, goodput, calibration and fairness, but did not yet make future batch/KV scarcity an explicit per-request opportunity cost.`（`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03948v1#S2.SS0.SSS0.Px2, #S2.SS0.SSS0.Px5 and #S2.SS0.SSS0.Px6 :: central buffering, release-when-startable admission and time-coupled batch/KV occupancy; https://arxiv.org/html/2607.03948v1#S3.SS1 through #S3.SS3 :: SLO-weighted action reward, online LP constraints, dual shadow prices, SAA history and projected subgradient updates; https://arxiv.org/html/2607.03948v1#A2.SS1 and #A2.SS3 :: pseudocode`；Evaluation：`https://arxiv.org/html/2607.03948v1#S4.SS1 :: Vidur-only simulation on four A100 GPUs with LMSYS-Chat-1M and synthetic P/D-ratio workloads; model, precision, batch/concurrency and exact serving SLO Not Disclosed; https://arxiv.org/html/2607.03948v1#S4.SS2 and #S4.SS3 :: RR/LOR/Random/Power-of-2 baselines, noisy length estimates, objective sweeps and an arrival-rate shift; https://arxiv.org/html/2607.03948v1#A3 :: broader sweeps and tail-weight sensitivity`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03948v1#S6 :: simulation-only, without serving-engine integration, preemption, KV swapping, distributed coordination, heterogeneous priorities or fairness validation; https://arxiv.org/html/2607.03948v1#A1.SS0.SSS0.Px9 :: PD-mixing duration is input-dependent; no LLM-specific theorem/regret/convergence or component ablation. Event-time artifact only partially corresponds to the manuscript noisy-length/tail-objective interface.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-03948:end -->

<!-- review:SF-2026-ARXIV-2607-03964:start -->
#### Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control

<!-- claim:SF-2026-ARXIV-2607-03964:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03964:end -->

- Identity：`arXiv:2607.03964v1`；first-public（Asia/Shanghai）：`2026-07-05`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03964:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-03948 | Vidur simulation with LMSYS-Chat-1M and synthetic P/D-ratio workloads | Not Disclosed | 4 x NVIDIA A100 | Not Disclosed | Trace/synthetic workload dependent; exact distribution Not Disclosed | Predicted and actual decode lengths are simulated; exact distribution Not Disclosed | Simulator-managed dynamic batching; exact sizes Not Disclosed | Not Disclosed; the workload uses Poisson arrival rates lambda in {0.4, 0.5}, which are not concurrency counts | No production SLO; reports EEL, TTFT, token throughput, QPS, tail indicator and SLO-violation metrics. Appendix C.1 uses TTFT threshold t2'=49 only in the corresponding sensitivity experiment | Vidur simulator with RR, LOR, Random and Power-of-2 baselines; exact Vidur version and experiment/config commit Not Disclosed |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-03948 | score_7_9;potential_books_delta | selected | DA-20260705-2607-03948 | — | V2=7/9；When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260705-2607-03948 |

<!-- analysis:DA-20260705-2607-03948:start -->
### Online Linear Programming for Multi-Objective Routing in LLM Serving

**旧方案为何合理。** Round Robin, least-queue and fixed priorities are cheap and robust under light load, homogeneous decode lengths and ample capacity because current queue state is then a useful cost proxy.（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）

**约束变化与机制。** When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Shadow prices expose future batch/KV scarcity but are not resource truth: stale prices or length errors can over-admit or reject, and a weighted objective can hide tenant starvation or hard security constraints. The manuscript evaluates injected decode-length noise but does not implement realized-error feedback into the dual-price update. The evidence is Vidur-only on four A100s, without production integration, formal percentile guarantees, preemption/swap or heterogeneous fleets; those remain the next validation pressure.

<!-- analysis:DA-20260705-2607-03948:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-03948 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L97 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2607-03948 | delta:SF-2026-ARXIV-2607-03948 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-03948 |

<!-- books-review:SF-2026-ARXIV-2607-03948:start --><!-- existing:SF-2026-ARXIV-2607-03948:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L97` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）为：Ch56 already separates admission, iteration scheduling, routing/placement and autoscaling and requires future-KV feasibility, goodput, calibration and fairness, but did not yet make future batch/KV scarcity an explicit per-request opportunity cost.<!-- existing:SF-2026-ARXIV-2607-03948:end --><!-- delta:SF-2026-ARXIV-2607-03948:start -->新增证据边界：When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L97`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-03948:end --><!-- books-review:SF-2026-ARXIV-2607-03948:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260705-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260705; semantic-review:SA-20260705-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260705-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-03693; review:SF-2026-ARXIV-2607-03751; review:SF-2026-ARXIV-2607-03870; review:SF-2026-ARXIV-2607-03876; review:SF-2026-ARXIV-2607-03948; review:SF-2026-ARXIV-2607-03964; semantic-review:SA-20260705-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260705-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260705-2607-03948; semantic-review:SA-20260705-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260705-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-03948; semantic-review:SA-20260705-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260705-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260705-COVERAGE:end -->
<!-- semantic-review:SA-20260705-EVIDENCE:start -->Fresh-context review reconciled all 6 frozen families: 1 Deep, 0 Standard and 5 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260705-EVIDENCE:end -->
<!-- semantic-review:SA-20260705-SELECTION:start -->Fresh-context review reconciled 1 eligible Deep families: 1 selected and 0 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260705-SELECTION:end -->
<!-- semantic-review:SA-20260705-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 1 个 family 已定位到实际 Books 段落，0 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260705-BOOKS:end -->

## 8. Ignored Noise

442 个窗口内 identity 中，436 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：1 个 `Integrate`，0 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，5 个 `Rejected — Low Durability / Out of Scope`；Deep 1 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/05/README.md`。
- 本日报长期 delta 已同步至：`books/part-05-inference-system/56-inference-scheduling.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](https://arxiv.org/abs/2607.03693v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models](https://arxiv.org/abs/2607.03751v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth](https://arxiv.org/abs/2607.03870v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference](https://arxiv.org/abs/2607.03876v1) — first-public（Asia/Shanghai）：2026-07-04；accessed：2026-08-26
- [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/abs/2607.03948v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-27
- [Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control](https://arxiv.org/abs/2607.03964v1) — first-public（Asia/Shanghai）：2026-07-05；accessed：2026-08-26
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
