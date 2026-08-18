# Daily Research — 2026-07-22

**Research Date:** 2026-07-22

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-21 09:00:00 ～ 2026-07-22 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 984 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 8 个。当前路由账目为 6 个 Deep、1 个 Standard、1 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-22 |
| Window End | 2026-07-22 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-22-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T18:31:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-21T09:00:00+08:00 | 2026-07-22T09:00:00+08:00 | 2026-08-27T18:31:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 984 | SF-2026-ARXIV-2607-18631<br>SF-2026-ARXIV-2607-18722<br>SF-2026-ARXIV-2607-18754<br>SF-2026-ARXIV-2607-19438<br>SF-2026-ARXIV-2607-19058<br>SF-2026-ARXIV-2607-19096<br>SF-2026-ARXIV-2607-19456<br>SF-2026-ARXIV-2607-19490 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-22T09:00:00+08:00 | coverage:SRC-ARXIV:20260722 | GAP-ARXIV-DIRECT-RESET-20260722 |
| SRC-GITHUB-COMMIT | 2026-07-21T09:00:00+08:00 | 2026-07-22T09:00:00+08:00 | 2026-08-27T18:31:00+08:00 | exact GitHub commit API lookups: Tencent-Hunyuan/GradLoc@0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5; AgentDebugX/AgentDebugX@27e55234bb617ef968f44800901c18e0fc55087f; basecompute/baseRT@1e9230269db7129dddef604c8d88f468fa55bc40; nuemaan/skewadam@ab17683889358217f28c1b5b870e719e7477e4e7 | checked | 4 | SF-2026-ARXIV-2607-18722; SF-2026-ARXIV-2607-18754; SF-2026-ARXIV-2607-19438; SF-2026-ARXIV-2607-19058 | pages=4; final cursors=0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5,27e55234bb617ef968f44800901c18e0fc55087f,1e9230269db7129dddef604c8d88f468fa55bc40,ab17683889358217f28c1b5b870e719e7477e4e7; one bounded commit lookup per family | 2026-07-22T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260722 | — |

<!-- coverage:SRC-ARXIV:20260722:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 984 unique identities in this strict window; 8 routed families.<!-- coverage:SRC-ARXIV:20260722:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260722:start -->repository=Tencent-Hunyuan/GradLoc, until=2026-07-22T01:00:00Z, full_sha=0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5, commit_timestamp=2026-02-16T09:17:25Z, url=https://github.com/Tencent-Hunyuan/GradLoc/commit/0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5; repository=AgentDebugX/AgentDebugX, until=2026-07-22T01:00:00Z, full_sha=27e55234bb617ef968f44800901c18e0fc55087f, commit_timestamp=2026-07-18T03:16:55Z, url=https://github.com/AgentDebugX/AgentDebugX/commit/27e55234bb617ef968f44800901c18e0fc55087f; repository=basecompute/baseRT, until=2026-07-22T01:00:00Z, full_sha=1e9230269db7129dddef604c8d88f468fa55bc40, commit_timestamp=2026-07-21T03:57:49Z, url=https://github.com/basecompute/baseRT/commit/1e9230269db7129dddef604c8d88f468fa55bc40; repository=nuemaan/skewadam, until=2026-07-22T01:00:00Z, full_sha=ab17683889358217f28c1b5b870e719e7477e4e7, commit_timestamp=2026-07-20T06:32:58Z, url=https://github.com/nuemaan/skewadam/commit/ab17683889358217f28c1b5b870e719e7477e4e7; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260722:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 8 个 family：exact v1 为 6 个 family 披露 artifact/evidence locator，其中 4 个提供外部 repository/project/demo locator，另有 2 个未披露；本日确认 4 个 family、4 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18631 | arXiv:2607.18631v1 | paper-v1:2607.18631 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18631 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-18631 | yes |
| SF-2026-ARXIV-2607-18722 | arXiv:2607.18722v1 | paper-v1:2607.18722 | 2026-W30 | 2026-07-21 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18722 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-18722 | yes |
| SF-2026-ARXIV-2607-18754 | arXiv:2607.18754v1 | paper-v1:2607.18754 | 2026-W30 | 2026-07-21 | SRC-ARXIV; SRC-GITHUB-COMMIT | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-18754 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2607-18754 | yes |
| SF-2026-ARXIV-2607-19438 | arXiv:2607.19438v1 | paper-v1:2607.19438 | 2026-W30 | 2026-07-21 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19438 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19438 | yes |
| SF-2026-ARXIV-2607-19058 | arXiv:2607.19058v1 | paper-v1:2607.19058 | 2026-W30 | 2026-07-21 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19058 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2607-19058 | yes |
| SF-2026-ARXIV-2607-19096 | arXiv:2607.19096v1 | paper-v1:2607.19096 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-19096 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19096 | yes |
| SF-2026-ARXIV-2607-19456 | arXiv:2607.19456v1 | paper-v1:2607.19456 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-19456 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19456 | no |
| SF-2026-ARXIV-2607-19490 | arXiv:2607.19490v1 | paper-v1:2607.19490 | 2026-W30 | 2026-07-22 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-19490 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-19490 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18631 | RP-4c82052bda274a39 | deep | arXiv:2607.18631v1 | SRC-ARXIV@arXiv:2607.18631v1 | https://arxiv.org/html/2607.18631v1#S3; https://arxiv.org/html/2607.18631v1#S4 | https://arxiv.org/html/2607.18631v1#S5 | https://arxiv.org/html/2607.18631v1#S6.SS4 | https://arxiv.org/html/2607.18631v1#A1 — exact v1 states that the artifact release URL and license are pending; no public artifact is credited | claim:SF-2026-ARXIV-2607-18631 | complete |
| SF-2026-ARXIV-2607-18722 | RP-b92a154db99b7efd | deep | arXiv:2607.18722v1 | SRC-ARXIV@arXiv:2607.18722v1; SRC-GITHUB-COMMIT@commit:0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5 | https://arxiv.org/html/2607.18722v1#S4 | https://arxiv.org/html/2607.18722v1#S5; https://arxiv.org/html/2607.18722v1#A6; https://arxiv.org/html/2607.18722v1#A7 | https://arxiv.org/html/2607.18722v1#S6; https://arxiv.org/html/2607.18722v1#A5 | https://github.com/Tencent-Hunyuan/GradLoc; https://github.com/Tencent-Hunyuan/GradLoc/commit/0fdd859a5945a59f3531ded48bc5d6cfd8a15fd5 — event-time repository pointer exists, but this pre-paper commit does not establish that the paper-specific SAT implementation was public | claim:SF-2026-ARXIV-2607-18722 | complete |
| SF-2026-ARXIV-2607-18754 | RP-615434f3bd1a3b3a | deep | arXiv:2607.18754v1 | SRC-ARXIV@arXiv:2607.18754v1; SRC-GITHUB-COMMIT@commit:27e55234bb617ef968f44800901c18e0fc55087f | https://arxiv.org/html/2607.18754v1#S3 | https://arxiv.org/html/2607.18754v1#S4; https://arxiv.org/html/2607.18754v1#A3 | https://arxiv.org/html/2607.18754v1#A5 | https://github.com/AgentDebugX/AgentDebugX; https://github.com/AgentDebugX/AgentDebugX/commit/27e55234bb617ef968f44800901c18e0fc55087f | claim:SF-2026-ARXIV-2607-18754 | complete |
| SF-2026-ARXIV-2607-19438 | RP-bf147b9ae61e80b4 | deep | arXiv:2607.19438v1 | SRC-ARXIV@arXiv:2607.19438v1; SRC-GITHUB-COMMIT@commit:1e9230269db7129dddef604c8d88f468fa55bc40 | https://arxiv.org/html/2607.19438v1#S3 | https://arxiv.org/html/2607.19438v1#S4 | https://arxiv.org/html/2607.19438v1#S5.SS1 | https://github.com/basecompute/baseRT; https://github.com/basecompute/baseRT/commit/1e9230269db7129dddef604c8d88f468fa55bc40 | claim:SF-2026-ARXIV-2607-19438 | complete |
| SF-2026-ARXIV-2607-19058 | RP-53bbff9b61a081cc | deep | arXiv:2607.19058v1 | SRC-ARXIV@arXiv:2607.19058v1; SRC-GITHUB-COMMIT@commit:ab17683889358217f28c1b5b870e719e7477e4e7 | https://arxiv.org/html/2607.19058v1#S3 | https://arxiv.org/html/2607.19058v1#S4; https://arxiv.org/html/2607.19058v1#S5; https://arxiv.org/html/2607.19058v1#A2; https://arxiv.org/html/2607.19058v1#A3; https://arxiv.org/html/2607.19058v1#A4 | https://arxiv.org/html/2607.19058v1#S6 | https://github.com/nuemaan/skewadam; https://github.com/nuemaan/skewadam/commit/ab17683889358217f28c1b5b870e719e7477e4e7 | claim:SF-2026-ARXIV-2607-19058 | complete |
| SF-2026-ARXIV-2607-19096 | RP-ef8ddbb8af8be5ea | standard | arXiv:2607.19096v1 | SRC-ARXIV@arXiv:2607.19096v1 | https://arxiv.org/html/2607.19096v1#S3 | https://arxiv.org/html/2607.19096v1#S4; https://arxiv.org/html/2607.19096v1#S5; https://arxiv.org/html/2607.19096v1#A3; https://arxiv.org/html/2607.19096v1#A4 | https://arxiv.org/html/2607.19096v1#S6; https://arxiv.org/html/2607.19096v1#A2 | https://arxiv.org/html/2607.19096v1#A2 — exact v1 says release requires later sanitization, licensing and a reproducibility manifest; no public artifact is credited | claim:SF-2026-ARXIV-2607-19096 | complete |
| SF-2026-ARXIV-2607-19456 | RP-3afa6fda84baf544 | closure | arXiv:2607.19456v1 | SRC-ARXIV@arXiv:2607.19456v1 | https://arxiv.org/html/2607.19456v1#S3; https://arxiv.org/html/2607.19456v1#S4 | https://arxiv.org/html/2607.19456v1#S5; https://arxiv.org/html/2607.19456v1#S6 | https://arxiv.org/html/2607.19456v1#S7; https://arxiv.org/html/2607.19456v1#S8 | Not Disclosed — exact v1 provides no public repository or measured GPU kernel artifact | claim:SF-2026-ARXIV-2607-19456 | complete |
| SF-2026-ARXIV-2607-19490 | RP-d82cc008d1a3e4e0 | deep | arXiv:2607.19490v1 | SRC-ARXIV@arXiv:2607.19490v1 | https://arxiv.org/html/2607.19490v1#S3 | https://arxiv.org/html/2607.19490v1#S4; https://arxiv.org/html/2607.19490v1#S5 | https://arxiv.org/html/2607.19490v1#S6 | Not Disclosed — exact v1 provides no public repository, code release, or immutable artifact locator | claim:SF-2026-ARXIV-2607-19490 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-18631:start -->
#### Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving

<!-- claim:SF-2026-ARXIV-2607-18631:start -->The exact v1 supports emitter-defined realizability, launch probing, realization-tax calibration, and bounded single-node measurements. It does not prove that dry-run buildability guarantees runtime feasibility or that the reported search quality generalizes to frontier multi-node deployments. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18631:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The search IR spans parallelism, schedule and kernels. A dry-run reuses the code emitter as the realizability predicate, launch probes catch memory/runtime gaps the static predicate misses, and measured realization overhead is priced back into the search rather than represented as a separate rule list. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18631v1#S3; https://arxiv.org/html/2607.18631v1#S4`；Evaluation：`https://arxiv.org/html/2607.18631v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18631v1#S6.SS4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-18631:end -->

<!-- review:SF-2026-ARXIV-2607-18722:start -->
#### Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-18722:start -->The exact v1 supports a sampled log-ratio risk proxy and outward-only, batch-quantile clip contraction in one asynchronous math-RL setup. It does not establish a full-distribution trust-region guarantee, universal stability, or artifact-complete reproducibility. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18722:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** SAT derives a detached sampled log-ratio, computes a batch-relative high-tail quantile, and contracts only the sign-selected outward side of PPO's interval. It is a drop-in sampled-surrogate change: the adaptive interval is contained in PPO's, pull-back updates are unchanged, and the objective differs only in the newly clipped outward band. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18722v1#S4`；Evaluation：`https://arxiv.org/html/2607.18722v1#S5; https://arxiv.org/html/2607.18722v1#A6; https://arxiv.org/html/2607.18722v1#A7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18722v1#S6; https://arxiv.org/html/2607.18722v1#A5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L571-L579`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-18722:end -->

<!-- review:SF-2026-ARXIV-2607-18754:start -->
#### AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-18754:start -->The exact v1 and event-time repository support a typed trace-diagnosis-rerun toolkit and bounded evaluations on Who&When and failed GAIA tasks. They do not prove causal attribution, safe autonomous repair, privacy adequacy, or robustness across agent frameworks. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18754:end -->

**旧方案与约束变化。** `本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**`（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Typed trace capture feeds a multi-turn debugger that narrows agent, step and failure class; the diagnosis is converted into a bounded repair and evaluated by a single rerun. Failure taxonomy and framework integrations are extensible surfaces rather than model truth. 它改变 `PLATFORM-TRACE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18754v1#S3`；Evaluation：`https://arxiv.org/html/2607.18754v1#S4; https://arxiv.org/html/2607.18754v1#A3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18754v1#A5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L580-L587`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-TRACE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-18754:end -->

<!-- review:SF-2026-ARXIV-2607-19438:start -->
#### BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators

<!-- claim:SF-2026-ARXIV-2607-19438:start -->The exact v1 and event-time repository support a phase- and silicon-specific Apple M5 implementation case with pinned single-device comparisons. They do not establish multi-request, multi-device, tail-latency, portability, or general accelerator superiority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19438:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Metal 4 cooperative-tensor kernels cover dense/MoE GEMM, fused expert projections and prefill attention. Dispatch selects this path only for compute-bound shapes/phases and retains specialized SIMD/GEMV kernels for memory-bound decode or unsupported hardware. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19438v1#S3`；Evaluation：`https://arxiv.org/html/2607.19438v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19438v1#S5.SS1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-19438:end -->

<!-- review:SF-2026-ARXIV-2607-19058:start -->
#### Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training

<!-- claim:SF-2026-ARXIV-2607-19058:start -->The exact v1 and event-time repository support role-aware optimizer-state allocation in one deliberately shallow MoE training regime. They do not establish a universal optimizer, large-scale distributed wall-clock gains, or general convergence across architectures and data. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19058:end -->

**旧方案与约束变化。** `本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。`（`books/part-04-training-system/28-pretraining.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** SkewAdam keeps momentum plus factored variance for the dense backbone, factored variance without momentum for experts, and exact variance for the router. Parameter role becomes the state-allocation key; this is orthogonal to ZeRO sharding and state quantization. 它改变 `TRAIN-PRETRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19058v1#S3`；Evaluation：`https://arxiv.org/html/2607.19058v1#S4; https://arxiv.org/html/2607.19058v1#S5; https://arxiv.org/html/2607.19058v1#A2; https://arxiv.org/html/2607.19058v1#A3; https://arxiv.org/html/2607.19058v1#A4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19058v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L597-L605`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-PRETRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19058:end -->

<!-- review:SF-2026-ARXIV-2607-19096:start -->
#### Supra Cognitive Modes: A Routed Architecture for Agent Memory

<!-- claim:SF-2026-ARXIV-2607-19096:start -->The exact v1 supports one routed memory architecture and benchmark-specific diagnostic results. It does not establish causal benefit from routing, portable timing/cost gains, statistically robust superiority, or public-artifact reproducibility. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19096:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A frozen semantic classifier selects a mode and maps it to a runtime payload over a shared asynchronous substrate. Optional enrichments can be absent; online fallback or omission prevents enrichment from becoming a readiness dependency. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19096v1#S3`；Evaluation：`https://arxiv.org/html/2607.19096v1#S4; https://arxiv.org/html/2607.19096v1#S5; https://arxiv.org/html/2607.19096v1#A3; https://arxiv.org/html/2607.19096v1#A4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19096v1#S6; https://arxiv.org/html/2607.19096v1#A2`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-19096:end -->

<!-- review:SF-2026-ARXIV-2607-19456:start -->
#### MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel

<!-- claim:SF-2026-ARXIV-2607-19456:start -->The exact v1 supports algebraic equivalence, CPU numerical checks and analytical traffic accounting. It does not demonstrate a new deployed execution mechanism, measured GPU speedup, production correctness, or public artifact. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19456:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The paper rewrites conventional single-query decode attention, KV append and GQA/MQA selection in MoA/DNF notation and sketches an OpenACC kernel. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19456v1#S3; https://arxiv.org/html/2607.19456v1#S4`；Evaluation：`https://arxiv.org/html/2607.19456v1#S5; https://arxiv.org/html/2607.19456v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19456v1#S7; https://arxiv.org/html/2607.19456v1#S8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 2 / Durability 1 = **4/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-19456:end -->

<!-- review:SF-2026-ARXIV-2607-19490:start -->
#### Integrity of peer-to-peer distributed LLM inference under malicious nodes

<!-- claim:SF-2026-ARXIV-2607-19490:start -->The exact v1 supports relative-L2 known-answer canaries as comparative integrity evidence in 408 simulated configurations. It does not establish production P2P integrity, heterogeneous-noise calibration, adaptive-attacker resistance, or authorization to evict a peer. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-19490:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The verifier interleaves indistinguishable known-answer canaries, stores clean fp32 intermediate activations, measures per-shard relative-L2 mismatch against live fp16 activations and ranks shards by per-canary AUROC rather than relying on one universal threshold. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.19490v1#S3`；Evaluation：`https://arxiv.org/html/2607.19490v1#S4; https://arxiv.org/html/2607.19490v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.19490v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-19490:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18631 | MoE training and serving plan search | paper-defined MoE configurations; 2048-GPU case is an oracle/search-only scale | 2x RTX4090 and 8x H800; single node | paper-specific framework/kernel configurations | Not uniformly disclosed | Serving protocol paper-specific | Paper-specific | Paper-specific | 0.98x strongest hand-tuned throughput acceptance gate | three-round medians, artifact-hashed preregistration and real launch probes |
| SF-2026-ARXIV-2607-18722 | asynchronous mathematical-reasoning RL | Qwen3-30B-A3B-Base | fully decoupled SGLang rollout and Megatron training GPU pools; exact count in Appendix F | paper configuration | training prompts from DAPO-Math-17k and Dolci-RL-Zero-Math-7B | 32k-token response limit | 256 prompts x 16 samples = 4096 responses/iteration | configured broadcast lag 1 or 8 trainer steps | stability and AIME24 performance, not serving SLO | rule-based verifier; sampled mismatch diagnostics |
| SF-2026-ARXIV-2607-18754 | agent failure localization and one-rerun repair | tested open-weight debugger backbones including qwen3.5-9b | Not disclosed as a comparative systems variable | Not disclosed | trace-dependent; long traces include around 40 events | diagnosis plus one repair rerun | 184 localization traces; 73 failed GAIA tasks | single-run evaluation | no production SLO | strict agent-and-step attribution and task success after rerun |
| SF-2026-ARXIV-2607-19438 | on-device LLM prefill and decode | 15 dense/MoE configurations from sub-1B to 35B | Apple M5 Pro 48GB, macOS Darwin 25.4 | Q4 and Q8 matched checkpoints | 128, 256, 512, 1024, 2048 tokens | 128 generated tokens for decode | single-user single-device | no continuous batching | throughput only; no tail-latency SLO | mean of five repetitions; llama.cpp b9960 and mlx-lm 0.31.3/MLX 0.32.0 |
| SF-2026-ARXIV-2607-19058 | single-GPU MoE pretraining optimizer comparison | 6.78B total, about 440M active, two-block decoder with 128 top-2 experts | NVIDIA H200 141GB main; H100 NVL 47GB MIG follow-ups | bf16 weights with common dithered rounding; fp32 optimizer statistics as specified | 128 tokens | training-only | 64x128 tokens with 8 accumulation steps | single GPU | memory, throughput, validation perplexity and router balance | shared initialization/data order; 10,000 steps; tier and LR ablations |
| SF-2026-ARXIV-2607-19096 | long-term agent-memory QA across LoCoMo, LongMemEval and MAB | declared benchmark-specific models/configurations | not disclosed as a controlled systems variable | not disclosed | benchmark-defined conversations/haystacks | benchmark-specific answers | repository-backed stored runs; two repetitions only for selected MAB result | asynchronous substrate but no comparative concurrency experiment | accuracy/abstention; timing boundary incomplete | benchmark judges and repository-backed diagnostic joins; no significance tests |
| SF-2026-ARXIV-2607-19490 | integrity auditing of pipeline-parallel peer-to-peer inference | GPT-2 124M, Pythia-160M; Pythia-410M only in depth study | simulated fp16 live stages against fp32 references; live heterogeneous pool not tested | fp32 reference, fp16 live pass with modeled noise | 100 canaries truncated to 48 tokens/configuration | last-token prediction | 216 factorial plus 192 substudy configurations | pipeline depth 2-12, colluders 1-4 | preregistered AUROC >=0.90, false-positive <=5% | relative-L2 per-canary AUROC, controls and harm frontier |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18631 | score_7_9;potential_books_delta | selected | DA-20260722-REALIZABILITY | — | V2=9/9；The exact v1 supports emitter-defined realizability, launch probing, realization-tax calibration, and bounded single-node measurements. It does not prove that dry-run buildability guarantees runtime feasibility or that the reported search quality generalizes to frontier multi-node deployments.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260722-REALIZABILITY |
| SF-2026-ARXIV-2607-18722 | score_7_9;potential_books_delta | selected | DA-20260722-STALE-TRUST | — | V2=8/9；The exact v1 supports a sampled log-ratio risk proxy and outward-only, batch-quantile clip contraction in one asynchronous math-RL setup. It does not establish a full-distribution trust-region guarantee, universal stability, or artifact-complete reproducibility.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260722-STALE-TRUST |
| SF-2026-ARXIV-2607-18754 | forced_review;potential_books_delta | not_selected | — | — | Deep-reviewed under knowledge_gap. The repair-authorization delta is durable but narrower, and current Ch69 already owns most of the root-cause-evidence chain; its Books patch remains independent of narrative selection. | analysis-decision:SF-2026-ARXIV-2607-18754 |
| SF-2026-ARXIV-2607-19438 | score_7_9;potential_books_delta | not_selected | — | — | Deep-reviewed. The bounded Apple M5 case confirms the phase/silicon dispatch contract already explicit in Ch49 and has no new canonical Books proposition. | analysis-decision:SF-2026-ARXIV-2607-19438 |
| SF-2026-ARXIV-2607-19058 | score_7_9;potential_books_delta | not_selected | — | — | Deep-reviewed and queued for Books. The role-aware optimizer-state branch is durable, but evidence remains a single-model, short-horizon training regime; selected units cover broader correctness boundaries for this report. | analysis-decision:SF-2026-ARXIV-2607-19058 |
| SF-2026-ARXIV-2607-19490 | score_7_9;potential_books_delta | selected | DA-20260722-INTERMEDIATE-INTEGRITY | — | 命中合同第一优先级 security contract；V2=7/9；The exact v1 supports relative-L2 known-answer canaries as comparative integrity evidence in 408 simulated configurations. It does not establish production P2P integrity, heterogeneous-noise calibration, adaptive-attacker resistance, or authorization to evict a peer.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260722-INTERMEDIATE-INTEGRITY |

<!-- analysis:DA-20260722-REALIZABILITY:start -->
### Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving

**旧方案为何合理。** Analytical cost search is reasonable when compiler, framework and kernel capability are stable and modeled constraints describe the executable domain. Once plan space spans phases, hardware and emitters, the optimizer can rank plans the actual toolchain cannot build.（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）

**约束变化与机制。** The search IR spans parallelism, schedule and kernels. A dry-run reuses the code emitter as the realizability predicate, launch probes catch memory/runtime gaps the static predicate misses, and measured realization overhead is priced back into the search rather than represented as a separate rule list. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Emitter reuse reduces drift but binds search to emitter completeness. Launch probing costs hardware time and still samples a finite environment. Evidence is single-node and small-model relative to frontier deployments; the artifact URL was not released in v1.

<!-- analysis:DA-20260722-REALIZABILITY:end -->

<!-- analysis:DA-20260722-STALE-TRUST:start -->
### Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning

**旧方案为何合理。** Fixed PPO/GRPO clipping is reasonable when rollout and update policies remain near each other. Decoupled rollout/training pools create heterogeneous realized mismatch inside one batch, so checkpoint lag alone no longer describes sample risk.（现有命题定位：`books/part-04-training-system/33-grpo.md#L14-L14`）

**约束变化与机制。** SAT derives a detached sampled log-ratio, computes a batch-relative high-tail quantile, and contracts only the sign-selected outward side of PPO's interval. It is a drop-in sampled-surrogate change: the adaptive interval is contained in PPO's, pull-back updates are unchanged, and the objective differs only in the newly clipped outward band. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-GRPO` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Batch quantiles add distribution dependence and may shift with length/domain mixture. Sampled log-ratios can be huge on low-probability actions without large mass movement; sequence ratios can cancel token mismatch. SAT controls the sampled surrogate, not an all-action trust region.

<!-- analysis:DA-20260722-STALE-TRUST:end -->

<!-- analysis:DA-20260722-INTERMEDIATE-INTEGRITY:start -->
### Integrity of peer-to-peer distributed LLM inference under malicious nodes

**旧方案为何合理。** Artifact signatures and final-output checks are reasonable when execution stays inside trusted infrastructure. Pipeline-parallel inference across untrusted peers needs evidence at intermediate state boundaries because a wrong final token cannot localize the stage that corrupted it.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** The verifier interleaves indistinguishable known-answer canaries, stores clean fp32 intermediate activations, measures per-shard relative-L2 mismatch against live fp16 activations and ranks shards by per-canary AUROC rather than relying on one universal threshold. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** References require trusted precomputation and activation storage. Real heterogeneous nondeterminism is not isotropic Gaussian; models are small. Adaptive attackers can fingerprint canaries or tune below the measured floor, and persistent-on-every-query attacks are easier than selective attacks.

<!-- analysis:DA-20260722-INTERMEDIATE-INTEGRITY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18754:start -->《AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents》已完成 Deep Source Review。Deep-reviewed under knowledge_gap. The repair-authorization delta is durable but narrower, and current Ch69 already owns most of the root-cause-evidence chain; its Books patch remains independent of narrative selection.<!-- analysis-decision:SF-2026-ARXIV-2607-18754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19438:start -->《BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators》已完成 Deep Source Review。Deep-reviewed. The bounded Apple M5 case confirms the phase/silicon dispatch contract already explicit in Ch49 and has no new canonical Books proposition.<!-- analysis-decision:SF-2026-ARXIV-2607-19438:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-19058:start -->《Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training》已完成 Deep Source Review。Deep-reviewed and queued for Books. The role-aware optimizer-state branch is durable, but evidence remains a single-model, short-horizon training regime; selected units cover broader correctness boundaries for this report.<!-- analysis-decision:SF-2026-ARXIV-2607-19058:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-18631 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-18631 | delta:SF-2026-ARXIV-2607-18631 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-18631 |
| SF-2026-ARXIV-2607-18722 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-18722 | delta:SF-2026-ARXIV-2607-18722 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-18722 |
| SF-2026-ARXIV-2607-18754 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-06-ai-infrastructure/68-logging.md#L14-L14; books/part-06-ai-infrastructure/70-cost.md#L14-L14 | existing:SF-2026-ARXIV-2607-18754 | delta:SF-2026-ARXIV-2607-18754 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-18754 |
| SF-2026-ARXIV-2607-19438 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-19438 | delta:SF-2026-ARXIV-2607-19438 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19438 |
| SF-2026-ARXIV-2607-19058 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L1 | books/part-04-training-system/27-data.md#L14-L14; books/part-04-training-system/29-sft.md#L14-L14 | existing:SF-2026-ARXIV-2607-19058 | delta:SF-2026-ARXIV-2607-19058 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-19058 |
| SF-2026-ARXIV-2607-19096 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14-L14 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-19096 | delta:SF-2026-ARXIV-2607-19096 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19096 |
| SF-2026-ARXIV-2607-19456 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-19456 | delta:SF-2026-ARXIV-2607-19456 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-19456 |
| SF-2026-ARXIV-2607-19490 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-19490 | delta:SF-2026-ARXIV-2607-19490 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-19490 |

<!-- books-review:SF-2026-ARXIV-2607-18631:start --><!-- existing:SF-2026-ARXIV-2607-18631:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-18631:end --><!-- delta:SF-2026-ARXIV-2607-18631:start -->新增证据边界：The search IR spans parallelism, schedule and kernels. A dry-run reuses the code emitter as the realizability predicate, launch probes catch memory/runtime gaps the static predicate misses, and measured realization overhead is priced back into the search rather than represented as a separate rule list. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-18631:end --><!-- books-review:SF-2026-ARXIV-2607-18631:end -->

<!-- books-review:SF-2026-ARXIV-2607-18722:start --><!-- existing:SF-2026-ARXIV-2607-18722:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-18722:end --><!-- delta:SF-2026-ARXIV-2607-18722:start -->新增证据边界：SAT derives a detached sampled log-ratio, computes a batch-relative high-tail quantile, and contracts only the sign-selected outward side of PPO's interval. It is a drop-in sampled-surrogate change: the adaptive interval is contained in PPO's, pull-back updates are unchanged, and the objective differs only in the newly clipped outward band. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-18722:end --><!-- books-review:SF-2026-ARXIV-2607-18722:end -->

<!-- books-review:SF-2026-ARXIV-2607-18754:start --><!-- existing:SF-2026-ARXIV-2607-18754:start -->对读 `books/part-06-ai-infrastructure/69-trace.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）为：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**<!-- existing:SF-2026-ARXIV-2607-18754:end --><!-- delta:SF-2026-ARXIV-2607-18754:start -->新增证据边界：Typed trace capture feeds a multi-turn debugger that narrows agent, step and failure class; the diagnosis is converted into a bounded repair and evaluated by a single rerun. Failure taxonomy and framework integrations are extensible surfaces rather than model truth. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-18754:end --><!-- books-review:SF-2026-ARXIV-2607-18754:end -->

<!-- books-review:SF-2026-ARXIV-2607-19438:start --><!-- existing:SF-2026-ARXIV-2607-19438:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-19438:end --><!-- delta:SF-2026-ARXIV-2607-19438:start -->新增证据边界：Metal 4 cooperative-tensor kernels cover dense/MoE GEMM, fused expert projections and prefill attention. Dispatch selects this path only for compute-bound shapes/phases and retains specialized SIMD/GEMV kernels for memory-bound decode or unsupported hardware. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-19438:end --><!-- books-review:SF-2026-ARXIV-2607-19438:end -->

<!-- books-review:SF-2026-ARXIV-2607-19058:start --><!-- existing:SF-2026-ARXIV-2607-19058:start -->对读 `books/part-04-training-system/28-pretraining.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/28-pretraining.md#L14-L14`）为：本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。<!-- existing:SF-2026-ARXIV-2607-19058:end --><!-- delta:SF-2026-ARXIV-2607-19058:start -->新增证据边界：SkewAdam keeps momentum plus factored variance for the dense backbone, factored variance without momentum for experts, and exact variance for the router. Parameter role becomes the state-allocation key; this is orthogonal to ZeRO sharding and state quantization. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19058:end --><!-- books-review:SF-2026-ARXIV-2607-19058:end -->

<!-- books-review:SF-2026-ARXIV-2607-19096:start --><!-- existing:SF-2026-ARXIV-2607-19096:start -->对读 `books/part-07-agent/77-memory.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-19096:end --><!-- delta:SF-2026-ARXIV-2607-19096:start -->新增证据边界：A frozen semantic classifier selects a mode and maps it to a runtime payload over a shared asynchronous substrate. Optional enrichments can be absent; online fallback or omission prevents enrichment from becoming a readiness dependency. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-19096:end --><!-- books-review:SF-2026-ARXIV-2607-19096:end -->

<!-- books-review:SF-2026-ARXIV-2607-19456:start --><!-- existing:SF-2026-ARXIV-2607-19456:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-19456:end --><!-- delta:SF-2026-ARXIV-2607-19456:start -->新增证据边界：The paper rewrites conventional single-query decode attention, KV append and GQA/MQA selection in MoA/DNF notation and sketches an OpenACC kernel. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-19456:end --><!-- books-review:SF-2026-ARXIV-2607-19456:end -->

<!-- books-review:SF-2026-ARXIV-2607-19490:start --><!-- existing:SF-2026-ARXIV-2607-19490:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-19490:end --><!-- delta:SF-2026-ARXIV-2607-19490:start -->新增证据边界：The verifier interleaves indistinguishable known-answer canaries, stores clean fp32 intermediate activations, measures per-shard relative-L2 mismatch against live fp16 activations and ranks shards by per-canary AUROC rather than relying on one universal threshold. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-19490:end --><!-- books-review:SF-2026-ARXIV-2607-19490:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260722-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260722; semantic-review:SA-20260722-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260722-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-18631; review:SF-2026-ARXIV-2607-18722; review:SF-2026-ARXIV-2607-18754; review:SF-2026-ARXIV-2607-19438; review:SF-2026-ARXIV-2607-19058; review:SF-2026-ARXIV-2607-19096; review:SF-2026-ARXIV-2607-19456; review:SF-2026-ARXIV-2607-19490; semantic-review:SA-20260722-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260722-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260722-REALIZABILITY; analysis:DA-20260722-STALE-TRUST; analysis:DA-20260722-INTERMEDIATE-INTEGRITY; semantic-review:SA-20260722-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260722-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-18631; books-review:SF-2026-ARXIV-2607-18722; books-review:SF-2026-ARXIV-2607-18754; books-review:SF-2026-ARXIV-2607-19438; books-review:SF-2026-ARXIV-2607-19058; books-review:SF-2026-ARXIV-2607-19096; books-review:SF-2026-ARXIV-2607-19456; books-review:SF-2026-ARXIV-2607-19490; semantic-review:SA-20260722-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260722-COVERAGE:start -->Fresh-context audit verified the frozen eight-family denominator and all first-public timestamps in the strict Beijing window [2026-07-21 09:00, 2026-07-22 09:00), with zero identifier overlap against D21 or D23. Artifact coverage now matches the observed evidence: four exact-v1 repository locators, four bounded pinned event-time commits and no fabricated GitHub attribution for the other four families. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260722-COVERAGE:end -->
<!-- semantic-review:SA-20260722-EVIDENCE:start -->Fresh-context audit recomputed all eight durable-snapshot SHA-256 digests, resolved every cited exact-v1 HTML anchor and confirmed packet-to-central-to-Daily consistency for identity, score, route, supporting sources, artifact boundary, claim boundary and disposition. Seven families retain exact full Source Reviews; 2607.19456 is now correctly imported as an accessible exact-v1 Closure with Score V2 1/2/1=4, RP, bounded mechanism/evaluation/limitations locators and No Change disposition. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260722-EVIDENCE:end -->
<!-- semantic-review:SA-20260722-SELECTION:start -->Fresh-context audit verified an eligibility denominator of exactly six Deep families, with three selected analysis units and three source-specific non-selection rationales persisted consistently in packet and Daily. The Standard and Closure families remain outside Selection without losing their completed reviews or Books decisions. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260722-SELECTION:end -->
<!-- semantic-review:SA-20260722-BOOKS:start -->Fresh-context audit read all five integrated passages in their unique owners and checked their adjacent chapter handoffs and Review notes: realizability-before-ranking, sample-level staleness control, trace-to-bounded-repair, role-aware optimizer state and intermediate-state integrity evidence. Each retains the old baseline, changed constraint, state/control mechanism, trade-off, failure/evidence boundary and coexistence condition. The remaining three families, including Closure 2607.19456, have bounded No Change comparisons with no duplicate owner. Books PASS; finding_count=0.<!-- semantic-review:SA-20260722-BOOKS:end -->

## 8. Ignored Noise

984 个窗口内 identity 中，976 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：5 个 `Integrate`，3 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 6 / Standard 1。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/22/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/28-pretraining.md`、`books/part-04-training-system/33-grpo.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/69-trace.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Searching for Plans You Can Actually Build: A Realizability-Aware Full-Space Optimizer for MoE Training and Serving](https://arxiv.org/abs/2607.18631v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning](https://arxiv.org/abs/2607.18722v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution, and Recovery in LLM Agents](https://arxiv.org/abs/2607.18754v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [BaseRT: Advancing Best-in-Class LLM Inference with Apple M5 Neural Accelerators](https://arxiv.org/abs/2607.19438v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2607.19058v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [Supra Cognitive Modes: A Routed Architecture for Agent Memory](https://arxiv.org/abs/2607.19096v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel](https://arxiv.org/abs/2607.19456v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [Integrity of peer-to-peer distributed LLM inference under malicious nodes](https://arxiv.org/abs/2607.19490v1) — first-public（Asia/Shanghai）：2026-07-22；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
