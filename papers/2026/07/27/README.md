# Daily Research — 2026-07-27

**Research Date:** 2026-07-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-26 09:00:00 ～ 2026-07-27 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；直接 arXiv 枚举冻结候选分母，技术 claim 回到精确 arXiv v1 与事件时 artifact receipt

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 549 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 10 个。当前路由账目为 9 个 Deep、1 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-27 |
| Window End | 2026-07-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-27-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T20:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-26T09:00:00+08:00 | 2026-07-27T09:00:00+08:00 | 2026-08-27T20:00:00+08:00 | https://export.arxiv.org/api/query; submittedDate exact replay; v1 published timestamp; cross-list deduplicated by arXiv ID | checked | 549 | SF-2026-ARXIV-2607-23532<br>SF-2026-ARXIV-2607-23693<br>SF-2026-ARXIV-2607-23771<br>SF-2026-ARXIV-2607-24866<br>SF-2026-ARXIV-2607-23802<br>SF-2026-ARXIV-2607-23809<br>SF-2026-ARXIV-2607-23815<br>SF-2026-ARXIV-2607-23844<br>SF-2026-ARXIV-2607-23870<br>SF-2026-ARXIV-2607-23909 | four archived pages; final_cursor=end | 2026-07-27T09:00:00+08:00 | coverage:SRC-ARXIV:20260727 | — |
| SRC-GITHUB-COMMIT | 2026-07-26T09:00:00+08:00 | 2026-07-27T09:00:00+08:00 | 2026-08-27T20:00:00+08:00 | exact GitHub commit API lookups: https://github.com/oklen/Compute-Globally-Materialize-Locally@d1bdc97b36bed8321d9a94a6d04f168f6cd64750; https://github.com/wangqinsi1/SpyRL@13f402e1842f4b18d2b064063ade28dda204843c; https://github.com/lixiaochuan2020/agentic-context-management@868e634a65b3b476b622d8cad93ef86432319375 | checked | 3 | SF-2026-ARXIV-2607-23693; SF-2026-ARXIV-2607-23802; SF-2026-ARXIV-2607-23809 | pages=3; final cursors=d1bdc97b36bed8321d9a94a6d04f168f6cd64750,13f402e1842f4b18d2b064063ade28dda204843c,868e634a65b3b476b622d8cad93ef86432319375; one bounded commit lookup per family | 2026-07-27T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260727 | — |

<!-- coverage:SRC-ARXIV:20260727:start -->Archived direct-arXiv submittedDate replay froze the strict-window denominator. Canonical source: papers/2026/07/_sources/arxiv-v2.1-replay-20260727-31/README.md; sha256:ec82a1f28ee96359d86fd58b84301083004450e32e146a7c5bfa25fec413c6b6; 549 unique identities in this strict window; 10 routed families.<!-- coverage:SRC-ARXIV:20260727:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260727:start -->repository=https://github.com/oklen/Compute-Globally-Materialize-Locally, until=2026-07-27T01:00:00Z, full_sha=d1bdc97b36bed8321d9a94a6d04f168f6cd64750, commit_timestamp=2026-07-26T13:28:20Z, url=https://github.com/oklen/Compute-Globally-Materialize-Locally/commit/d1bdc97b36bed8321d9a94a6d04f168f6cd64750; repository=https://github.com/wangqinsi1/SpyRL, until=2026-07-27T01:00:00Z, full_sha=13f402e1842f4b18d2b064063ade28dda204843c, commit_timestamp=2026-07-26T21:32:35Z, url=https://github.com/wangqinsi1/SpyRL/commit/13f402e1842f4b18d2b064063ade28dda204843c; repository=https://github.com/lixiaochuan2020/agentic-context-management, until=2026-07-27T01:00:00Z, full_sha=868e634a65b3b476b622d8cad93ef86432319375, commit_timestamp=2026-07-26T18:06:29Z, url=https://github.com/lixiaochuan2020/agentic-context-management/commit/868e634a65b3b476b622d8cad93ef86432319375; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260727:end -->

### Coverage Limitations

- 直接 arXiv replay 只闭合候选枚举与 first-public identity；机制和实验结论仍逐项来自 exact-v1 全文与可追溯 artifact。
- Artifact-boundary routing 覆盖 10 个 family：exact v1 为 4 个 family 披露 artifact/evidence locator，其中 3 个提供外部 repository/project/demo locator，另有 6 个未披露；本日确认 3 个 family、3 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23532 | arXiv:2607.23532v1 | paper-v1:2607.23532 | 2026-W30 | 2026-07-26 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23532 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-23532 | yes |
| SF-2026-ARXIV-2607-23693 | arXiv:2607.23693v1 | paper-v1:2607.23693 | 2026-W30 | 2026-07-26 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23693 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-23693 | yes |
| SF-2026-ARXIV-2607-23771 | arXiv:2607.23771v1 | paper-v1:2607.23771 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23771 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-23771 | yes |
| SF-2026-ARXIV-2607-24866 | arXiv:2607.24866v1 | paper-v1:2607.24866 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24866 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24866 | no |
| SF-2026-ARXIV-2607-23802 | arXiv:2607.23802v1 | paper-v1:2607.23802 | 2026-W31 | 2026-07-27 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23802 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23802 | yes |
| SF-2026-ARXIV-2607-23809 | arXiv:2607.23809v1 | paper-v1:2607.23809 | 2026-W31 | 2026-07-27 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23809 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23809 | yes |
| SF-2026-ARXIV-2607-23815 | arXiv:2607.23815v1 | paper-v1:2607.23815 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23815 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-23815 | yes |
| SF-2026-ARXIV-2607-23844 | arXiv:2607.23844v1 | paper-v1:2607.23844 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-23844 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23844 | yes |
| SF-2026-ARXIV-2607-23870 | arXiv:2607.23870v1 | paper-v1:2607.23870 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23870 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23870 | yes |
| SF-2026-ARXIV-2607-23909 | arXiv:2607.23909v1 | paper-v1:2607.23909 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23909 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23909 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23532 | RP-a30f620ba09eabe2 | deep | arXiv:2607.23532v1 | SRC-ARXIV@arXiv:2607.23532v1 | https://arxiv.org/html/2607.23532v1#S5 | https://arxiv.org/html/2607.23532v1#S7 | https://arxiv.org/html/2607.23532v1#S3.SS0.SSS0.Px6 | https://arxiv.org/html/2607.23532v1#Pt0.A1 — companion material is named in v1, but no external immutable experiment repository/commit is disclosed | claim:SF-2026-ARXIV-2607-23532 | complete |
| SF-2026-ARXIV-2607-23693 | RP-1bdada15d22b22b6 | deep | arXiv:2607.23693v1 | SRC-ARXIV@arXiv:2607.23693v1; SRC-GITHUB-COMMIT@commit:d1bdc97b36bed8321d9a94a6d04f168f6cd64750 | https://arxiv.org/html/2607.23693v1#S2 | https://arxiv.org/html/2607.23693v1#S3 | https://arxiv.org/html/2607.23693v1#S9 | https://github.com/oklen/Compute-Globally-Materialize-Locally/commit/d1bdc97b36bed8321d9a94a6d04f168f6cd64750 | claim:SF-2026-ARXIV-2607-23693 | complete |
| SF-2026-ARXIV-2607-23771 | RP-a35b52c1548c38d9 | deep | arXiv:2607.23771v1 | SRC-ARXIV@arXiv:2607.23771v1 | https://arxiv.org/html/2607.23771v1#S4 | https://arxiv.org/html/2607.23771v1#S6 | https://arxiv.org/html/2607.23771v1#S6 — no dedicated limitations section; claims are bounded to the disclosed controller/task/model recipe | Not Disclosed — exact v1 does not bind the reported experiments to an immutable public commit | claim:SF-2026-ARXIV-2607-23771 | complete |
| SF-2026-ARXIV-2607-24866 | RP-2f63f484afe4d36e | deep | arXiv:2607.24866v1 | SRC-ARXIV@arXiv:2607.24866v1 | https://arxiv.org/html/2607.24866v1#S7 | https://arxiv.org/html/2607.24866v1#S9 | https://arxiv.org/html/2607.24866v1#S10 | Not Disclosed — CARMA is described as a prototype instantiation without an exact immutable experiment artifact | claim:SF-2026-ARXIV-2607-24866 | complete |
| SF-2026-ARXIV-2607-23802 | RP-3861e95bcc341caa | deep | arXiv:2607.23802v1 | SRC-ARXIV@arXiv:2607.23802v1; SRC-GITHUB-COMMIT@commit:13f402e1842f4b18d2b064063ade28dda204843c | https://arxiv.org/html/2607.23802v1#S2; https://arxiv.org/html/2607.23802v1#S3 | https://arxiv.org/html/2607.23802v1#S4 | https://arxiv.org/html/2607.23802v1#S4 — no dedicated limitations section; proxy-game alignment and judge/human agreement bound the claim | https://github.com/wangqinsi1/SpyRL/commit/13f402e1842f4b18d2b064063ade28dda204843c | claim:SF-2026-ARXIV-2607-23802 | complete |
| SF-2026-ARXIV-2607-23809 | RP-eb9c08be47281bff | deep | arXiv:2607.23809v1 | SRC-ARXIV@arXiv:2607.23809v1; SRC-GITHUB-COMMIT@commit:868e634a65b3b476b622d8cad93ef86432319375 | https://arxiv.org/html/2607.23809v1#S3 | https://arxiv.org/html/2607.23809v1#S5; https://arxiv.org/html/2607.23809v1#S6 | https://arxiv.org/html/2607.23809v1#Sx1 | https://github.com/lixiaochuan2020/agentic-context-management/commit/868e634a65b3b476b622d8cad93ef86432319375 | claim:SF-2026-ARXIV-2607-23809 | complete |
| SF-2026-ARXIV-2607-23815 | RP-bec89fa3e9e3ff46 | deep | arXiv:2607.23815v1 | SRC-ARXIV@arXiv:2607.23815v1 | https://arxiv.org/html/2607.23815v1#S3; https://arxiv.org/html/2607.23815v1#S5; https://arxiv.org/html/2607.23815v1#S6 | https://arxiv.org/html/2607.23815v1#S7 | https://arxiv.org/html/2607.23815v1#S7 — no dedicated limitations section; claims remain bound to disclosed semantic-query workloads and runtime | Not Disclosed — exact v1 does not bind Kalypso to an immutable public implementation commit | claim:SF-2026-ARXIV-2607-23815 | complete |
| SF-2026-ARXIV-2607-23844 | RP-57ad55b1e04fb6cf | standard | arXiv:2607.23844v1 | SRC-ARXIV@arXiv:2607.23844v1 | https://arxiv.org/html/2607.23844v1#S3 | https://arxiv.org/html/2607.23844v1#S4 | https://arxiv.org/html/2607.23844v1#S5 | Not Disclosed — cited Open-Sora is a baseline, not an immutable OmniCache artifact | claim:SF-2026-ARXIV-2607-23844 | complete |
| SF-2026-ARXIV-2607-23870 | RP-79d2bed7a8b659fb | deep | arXiv:2607.23870v1 | SRC-ARXIV@arXiv:2607.23870v1 | https://arxiv.org/html/2607.23870v1#S3 | https://arxiv.org/html/2607.23870v1#S4.SS3; https://arxiv.org/html/2607.23870v1#S4.SS4; https://arxiv.org/html/2607.23870v1#S4.SS5 | https://arxiv.org/html/2607.23870v1#S4.SS8 | Not Disclosed — exact v1 does not bind the benchmark to an immutable public release/commit | claim:SF-2026-ARXIV-2607-23870 | complete |
| SF-2026-ARXIV-2607-23909 | RP-6eba71513333349e | deep | arXiv:2607.23909v1 | SRC-ARXIV@arXiv:2607.23909v1 | https://arxiv.org/html/2607.23909v1#S2 | https://arxiv.org/html/2607.23909v1#S3.SS1.SSS3; https://arxiv.org/html/2607.23909v1#S3.SS2 | https://arxiv.org/html/2607.23909v1#S4 | Not Disclosed — exact v1 does not bind the reported system to an immutable public artifact | claim:SF-2026-ARXIV-2607-23909 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-23532:start -->
#### Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric

<!-- claim:SF-2026-ARXIV-2607-23532:start -->The exact v1 supports the architecture and simulated fault-campaign behavior, not real radio, heterogeneous robot or production safety guarantees. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23532:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A three-tier L1/L2/L3 assurance fabric composes platform, squad and mission predicates over durable events; evidence gaps propagate as unknown instead of false all-clear. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23532v1#S5`；Evaluation：`https://arxiv.org/html/2607.23532v1#S7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23532v1#S3.SS0.SSS0.Px6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23532:end -->

<!-- review:SF-2026-ARXIV-2607-23693:start -->
#### Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV

<!-- claim:SF-2026-ARXIV-2607-23693:start -->The donor-swap serving experiment establishes a causal channel for the tested model/payload, not lossless recovery, universal source irrelevance or arbitrary post-hoc KV composability. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23693:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A retained downstream contextualized KV row can carry semantics of an omitted upstream observation, so sparse event-KV materializes derived state rather than merely sampling tokens. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23693v1#S2`；Evaluation：`https://arxiv.org/html/2607.23693v1#S3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23693v1#S9`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23693:end -->

<!-- review:SF-2026-ARXIV-2607-23771:start -->
#### Training Language Models to Cooperate with Inference-Time Controllers

<!-- claim:SF-2026-ARXIV-2607-23771:start -->The reported Llama-3.2-3B math experiments support reduced mismatch for the tested controller family; they do not establish controller-agnostic or task-general cooperation. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23771:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Multi-controller sampling and turn-level GRPO train the policy against a vocabulary of inference-time controller/module compositions. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23771v1#S4`；Evaluation：`https://arxiv.org/html/2607.23771v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23771v1#S6 — no dedicated limitations section; claims are bounded to the disclosed controller/task/model recipe`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23771:end -->

<!-- review:SF-2026-ARXIV-2607-24866:start -->
#### The Missing Layer: Specification Infrastructure for AI Oversight

<!-- claim:SF-2026-ARXIV-2607-24866:start -->The paper supports the missing-layer architecture and prototype direction, not production efficacy, completeness or resistance to specification error. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-24866:end -->

**旧方案与约束变化。** `本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**`（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Versioned human-authored specifications compile into runtime policy/monitor artifacts, sidecar mediation, audit and governance interfaces. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.24866v1#S7`；Evaluation：`https://arxiv.org/html/2607.24866v1#S9`；Limitations/Counterevidence：`https://arxiv.org/html/2607.24866v1#S10`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-24866:end -->

<!-- review:SF-2026-ARXIV-2607-23802:start -->
#### From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-23802:start -->The exact v1 supports improvement on the tested transformed tasks, not that proxy-game success faithfully captures every original open-ended objective. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23802:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Open-ended tasks are transformed into information-asymmetric self-play games whose internal detection outcome supplies a self-verifiable reward. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23802v1#S2; https://arxiv.org/html/2607.23802v1#S3`；Evaluation：`https://arxiv.org/html/2607.23802v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23802v1#S4 — no dedicated limitations section; proxy-game alignment and judge/human agreement bound the claim`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23802:end -->

<!-- review:SF-2026-ARXIV-2607-23809:start -->
#### ACM: Agentic Context Management for Long Horizon Tasks

<!-- claim:SF-2026-ARXIV-2607-23809:start -->The exact v1 supports the tested long-horizon policy and ablations, not universal optimality, lossless compression or correctness of every self-triggered retrieval. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23809:end -->

**旧方案与约束变化。** `本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**`（`books/part-07-agent/75-context.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The agent chooses when to compress, externalize removed content and retrieve it later, turning context truncation into an explicit lifecycle policy. 它改变 `AGENT-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23809v1#S3`；Evaluation：`https://arxiv.org/html/2607.23809v1#S5; https://arxiv.org/html/2607.23809v1#S6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23809v1#Sx1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-CONTEXT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23809:end -->

<!-- review:SF-2026-ARXIV-2607-23815:start -->
#### Kalypso: Relational LLM Serving

<!-- claim:SF-2026-ARXIV-2607-23815:start -->The exact v1 supports gains on the disclosed vLLM/Lotus/Palimpzest workloads, not arbitrary semantic UDFs, models or production SLOs. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23815:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A relational query plan becomes a stage/operator DAG; the runtime performs operator-granular admission while the LLM engine retains request scheduling, with token-bound memory estimation, KV pinning and deadlock/fallback control. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23815v1#S3; https://arxiv.org/html/2607.23815v1#S5; https://arxiv.org/html/2607.23815v1#S6`；Evaluation：`https://arxiv.org/html/2607.23815v1#S7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23815v1#S7 — no dedicated limitations section; claims remain bound to disclosed semantic-query workloads and runtime`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23815:end -->

<!-- review:SF-2026-ARXIV-2607-23844:start -->
#### OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-23844:start -->The exact v1 supports author-reported gains for SVD-XT, Latte-1 and SD3-medium on A100 40GB; it does not establish a globally optimal cache policy or cross-model portability. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23844:end -->

**旧方案与约束变化。** `本章的核心判断是：**生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。**“一次生成更多 token”不自动等于更快；“允许修正”也不自动等于更准。必须把 proposal work、verification/correction、memory、并发和输出提交一起计算。`（`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Diffusion inference caches features hierarchically across token, frame, block, layer and denoising-step dimensions using workload-specific reuse schedules. 它改变 `MULTIMODAL-GENERATIVE-PARADIGMS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23844v1#S3`；Evaluation：`https://arxiv.org/html/2607.23844v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23844v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-GENERATIVE-PARADIGMS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23844:end -->

<!-- review:SF-2026-ARXIV-2607-23870:start -->
#### MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents

<!-- claim:SF-2026-ARXIV-2607-23870:start -->The exact v1 supports comparative behavior under one offline benchmark contract, not closed-loop flight safety, calibrated deployment risk or causal policy compliance. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23870:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An offline UAV benchmark evaluates protocol-conditioned decisions from physical observation, policy semantics and safe-action constraints, separating semantic and strict diagnostics. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23870v1#S3`；Evaluation：`https://arxiv.org/html/2607.23870v1#S4.SS3; https://arxiv.org/html/2607.23870v1#S4.SS4; https://arxiv.org/html/2607.23870v1#S4.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23870v1#S4.SS8`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23870:end -->

<!-- review:SF-2026-ARXIV-2607-23909:start -->
#### WorldDiT: A Unified Diffusion Architecture for World and Action Modeling

<!-- claim:SF-2026-ARXIV-2607-23909:start -->The exact v1 supports gains on disclosed LIBERO tasks, not causal/controllable environment modeling, planning through imagination or physical deployment robustness. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23909:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** One diffusion transformer jointly predicts continuous action chunks and future normalized RGB patches; the future head is a training-time representation constraint and is removed at deployment. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23909v1#S2`；Evaluation：`https://arxiv.org/html/2607.23909v1#S3.SS1.SSS3; https://arxiv.org/html/2607.23909v1#S3.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23909v1#S4`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-23909:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23532 | Simulated ISR swarm fault campaign | LLM-assisted agents as configured by authors | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Multi-agent simulated mission; exact concurrency not disclosed | Assurance detection/liveness, not serving latency SLO | Author fault injection and runtime-monitor outcomes |
| SF-2026-ARXIV-2607-23693 | Controlled omitted-source question answering with donor-row swaps | Author-tested language models; exact claim remains manuscript-scoped | Not Disclosed | Not Disclosed | Finite event payloads; exact production length contract not disclosed | Short answers | Not Disclosed | Not Disclosed | Answer preservation under sparse serving; no latency SLO | Author causal intervention and task correctness |
| SF-2026-ARXIV-2607-23771 | GSM8K, MATH500 and AMC23 under 12 inference-time controllers and held-out compositions | Llama-3.2-3B | Not Disclosed | Not Disclosed | Problem/controller dependent; Not Disclosed | Multi-turn controller trajectories; Not Disclosed | Not Disclosed | Not Disclosed | Task correctness/format reward, not serving SLO | Binary correctness plus format reward under author controller protocols |
| SF-2026-ARXIV-2607-23802 | Author-defined transformed open-ended tasks and alternating self-play | As disclosed in v1; conclusions remain setup-specific | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Alternating self-play roles | Task reward/correctness, not serving SLO | Game outcome plus author-reported human/judge comparisons |
| SF-2026-ARXIV-2607-23809 | Long-horizon agent tasks in the disclosed benchmark suite | Author-tested agents/models | Not Disclosed | Not Disclosed | Long-horizon contexts; exact universal bound not disclosed | Task trajectories | Not Disclosed | Not Disclosed | Task success/context cost; no online latency SLO | Author benchmark and ablation protocol |
| SF-2026-ARXIV-2607-23815 | Relational semantic-query pipelines from Lotus and Palimpzest | Llama-3.3-70B via vLLM | As disclosed in v1; general hardware portability not established | Not Disclosed | Operator/query dependent | Operator/query dependent | LLM engine batch up to 64 in disclosed setup | Pipeline/operator concurrency controlled by Kalypso | End-to-end query latency/throughput; no universal tail SLO | Author end-to-end and component measurements |
| SF-2026-ARXIV-2607-23844 | Image/video diffusion generation on UCF101, MS-COCO and disclosed prompts | SVD-XT, Latte-1, SD3-medium | NVIDIA A100 40GB | Not Disclosed | Diffusion/model dependent | Generated image/video dimensions as disclosed | Not Disclosed | Not Disclosed | Generation latency/quality, no online tail SLO | Author latency and quality metrics |
| SF-2026-ARXIV-2607-23870 | Offline multimodal UAV decision scenarios with security/safety policies | 17 models listed in v1 | Not Disclosed | Provider/model dependent; Not Disclosed | Scenario dependent | Decision/rationale outputs | Not Disclosed | Not Disclosed | Semantic/strict decision metrics, not flight-control SLO | Author benchmark scorers and modality-removal ablation |
| SF-2026-ARXIV-2607-23909 | LIBERO robotic manipulation suites | WorldDiT shared diffusion transformer as disclosed | Not Disclosed | Not Disclosed | Observation/history as disclosed | Action chunks plus future visual patches during training | Not Disclosed | Not Disclosed | Task success, not real-time control SLO | Author LIBERO evaluation |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23532 | score_7_9;potential_books_delta | selected | DA-20260727-MISSION-ASSURANCE | — | 命中合同第一优先级 security contract；V2=8/9；The exact v1 supports the architecture and simulated fault-campaign behavior, not real radio, heterogeneous robot or production safety guarantees.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260727-MISSION-ASSURANCE |
| SF-2026-ARXIV-2607-23693 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The donor-swap serving experiment establishes a causal channel for the tested model/payload, not lossless recovery, universal source irrelevance or arbitrary post-hoc KV composability.”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-23693 |
| SF-2026-ARXIV-2607-23771 | score_7_9;potential_books_delta | selected | DA-20260727-CONTROLLER-AWARE-LEARNING | — | V2=8/9；The reported Llama-3.2-3B math experiments support reduced mismatch for the tested controller family; they do not establish controller-agnostic or task-general cooperation.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260727-CONTROLLER-AWARE-LEARNING |
| SF-2026-ARXIV-2607-24866 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The paper supports the missing-layer architecture and prototype direction, not production efficacy, completeness or resistance to specification error.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-23532` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-24866 |
| SF-2026-ARXIV-2607-23802 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The exact v1 supports improvement on the tested transformed tasks, not that proxy-game success faithfully captures every original open-ended objective.”；V2=3/2/2。与同 owner 入选 `SF-2026-ARXIV-2607-23771` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-23802 |
| SF-2026-ARXIV-2607-23809 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The exact v1 supports the tested long-horizon policy and ablations, not universal optimality, lossless compression or correctness of every self-triggered retrieval.”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-23809 |
| SF-2026-ARXIV-2607-23815 | score_7_9;potential_books_delta | selected | DA-20260727-RELATIONAL-SERVING | — | V2=9/9；The exact v1 supports gains on the disclosed vLLM/Lotus/Palimpzest workloads, not arbitrary semantic UDFs, models or production SLOs.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260727-RELATIONAL-SERVING |
| SF-2026-ARXIV-2607-23870 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The exact v1 supports comparative behavior under one offline benchmark contract, not closed-loop flight safety, calibrated deployment risk or causal policy compliance.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-23870 |
| SF-2026-ARXIV-2607-23909 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“The exact v1 supports gains on disclosed LIBERO tasks, not causal/controllable environment modeling, planning through imagination or physical deployment robustness.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-23909 |

<!-- analysis:DA-20260727-MISSION-ASSURANCE:start -->
### Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric

**旧方案为何合理。** Per-agent guardrails are reasonable for local hazards; coordinated missions add cross-agent temporal invariants and missing-evidence ambiguity.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L14-L14`）

**约束变化与机制。** A three-tier L1/L2/L3 assurance fabric composes platform, squad and mission predicates over durable events; evidence gaps propagate as unknown instead of false all-clear. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Cross-layer provenance and durable clocks improve auditability but create ordering, availability, classification and common-mode policy risks.

<!-- analysis:DA-20260727-MISSION-ASSURANCE:end -->

<!-- analysis:DA-20260727-CONTROLLER-AWARE-LEARNING:start -->
### Training Language Models to Cooperate with Inference-Time Controllers

**旧方案为何合理。** One controller is a stable baseline when training and serving protocols match; controller composition and drift make controller identity part of the policy distribution.（现有命题定位：`books/part-04-training-system/33-grpo.md#L14-L14`）

**约束变化与机制。** Multi-controller sampling and turn-level GRPO train the policy against a vocabulary of inference-time controller/module compositions. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-GRPO` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Broader controller exposure buys robustness to tested compositions but increases rollout cost, variance, credit assignment, protocol-version coupling and negative transfer.

<!-- analysis:DA-20260727-CONTROLLER-AWARE-LEARNING:end -->

<!-- analysis:DA-20260727-RELATIONAL-SERVING:start -->
### Kalypso: Relational LLM Serving

**旧方案为何合理。** Independent request scheduling is correct for independent prompts; relational pipelines introduce inter-operator dependencies and reusable KV state.（现有命题定位：`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）

**约束变化与机制。** A relational query plan becomes a stage/operator DAG; the runtime performs operator-granular admission while the LLM engine retains request scheduling, with token-bound memory estimation, KV pinning and deadlock/fallback control. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-SCHEDULING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Cross-operator reuse and admission can improve pipeline efficiency but add query-plan state, token estimation error, pinning pressure, deadlock and workload-specific heuristics.

<!-- analysis:DA-20260727-RELATIONAL-SERVING:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23693:start -->《Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV》已完成 Deep Source Review。本 family 的独立增量为“The donor-swap serving experiment establishes a causal channel for the tested model/payload, not lossless recovery, universal source irrelevance or arbitrary post-hoc KV composability.”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-23693:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24866:start -->《The Missing Layer: Specification Infrastructure for AI Oversight》已完成 Deep Source Review。本 family 的独立增量为“The paper supports the missing-layer architecture and prototype direction, not production efficacy, completeness or resistance to specification error.”；V2=3/3/2。与同 owner 入选 `SF-2026-ARXIV-2607-23532` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-24866:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23802:start -->《From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement》已完成 Deep Source Review。本 family 的独立增量为“The exact v1 supports improvement on the tested transformed tasks, not that proxy-game success faithfully captures every original open-ended objective.”；V2=3/2/2。与同 owner 入选 `SF-2026-ARXIV-2607-23771` 相比，本项没有更高的 Design Delta / System Reach / Durability。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-23802:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23809:start -->《ACM: Agentic Context Management for Long Horizon Tasks》已完成 Deep Source Review。本 family 的独立增量为“The exact v1 supports the tested long-horizon policy and ablations, not universal optimality, lossless compression or correctness of every self-triggered retrieval.”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-23809:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23870:start -->《MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents》已完成 Deep Source Review。本 family 的独立增量为“The exact v1 supports comparative behavior under one offline benchmark contract, not closed-loop flight safety, calibrated deployment risk or causal policy compliance.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-23870:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-23909:start -->《WorldDiT: A Unified Diffusion Architecture for World and Action Modeling》已完成 Deep Source Review。本 family 的独立增量为“The exact v1 supports gains on disclosed LIBERO tasks, not causal/controllable environment modeling, planning through imagination or physical deployment robustness.”；V2=3/2/2。它与入选 `SF-2026-ARXIV-2607-23532` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-23909:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23532 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L604 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-23532 | delta:SF-2026-ARXIV-2607-23532 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23532 |
| SF-2026-ARXIV-2607-23693 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L144 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-23693 | delta:SF-2026-ARXIV-2607-23693 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23693 |
| SF-2026-ARXIV-2607-23771 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1115 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-23771 | delta:SF-2026-ARXIV-2607-23771 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23771 |
| SF-2026-ARXIV-2607-24866 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14-L14 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-24866 | delta:SF-2026-ARXIV-2607-24866 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-24866 |
| SF-2026-ARXIV-2607-23802 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L14-L14 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-23802 | delta:SF-2026-ARXIV-2607-23802 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23802 |
| SF-2026-ARXIV-2607-23809 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L14-L14 | books/part-07-agent/74-prompt.md#L14-L14; books/part-07-agent/76-rag.md#L14-L14 | existing:SF-2026-ARXIV-2607-23809 | delta:SF-2026-ARXIV-2607-23809 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23809 |
| SF-2026-ARXIV-2607-23815 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L304 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-23815 | delta:SF-2026-ARXIV-2607-23815 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23815 |
| SF-2026-ARXIV-2607-23844 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14 | books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14; books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | existing:SF-2026-ARXIV-2607-23844 | delta:SF-2026-ARXIV-2607-23844 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23844 |
| SF-2026-ARXIV-2607-23870 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-23870 | delta:SF-2026-ARXIV-2607-23870 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23870 |
| SF-2026-ARXIV-2607-23909 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-23909 | delta:SF-2026-ARXIV-2607-23909 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-23909 |

<!-- books-review:SF-2026-ARXIV-2607-23532:start --><!-- existing:SF-2026-ARXIV-2607-23532:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L604` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-23532:end --><!-- delta:SF-2026-ARXIV-2607-23532:start -->新增证据边界：A three-tier L1/L2/L3 assurance fabric composes platform, squad and mission predicates over durable events; evidence gaps propagate as unknown instead of false all-clear. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L604`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23532:end --><!-- books-review:SF-2026-ARXIV-2607-23532:end -->

<!-- books-review:SF-2026-ARXIV-2607-23693:start --><!-- existing:SF-2026-ARXIV-2607-23693:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L144` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-23693:end --><!-- delta:SF-2026-ARXIV-2607-23693:start -->新增证据边界：A retained downstream contextualized KV row can carry semantics of an omitted upstream observation, so sparse event-KV materializes derived state rather than merely sampling tokens. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L144`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23693:end --><!-- books-review:SF-2026-ARXIV-2607-23693:end -->

<!-- books-review:SF-2026-ARXIV-2607-23771:start --><!-- existing:SF-2026-ARXIV-2607-23771:start -->对读 `books/part-04-training-system/33-grpo.md#L1115` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-23771:end --><!-- delta:SF-2026-ARXIV-2607-23771:start -->新增证据边界：Multi-controller sampling and turn-level GRPO train the policy against a vocabulary of inference-time controller/module compositions. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1115`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23771:end --><!-- books-review:SF-2026-ARXIV-2607-23771:end -->

<!-- books-review:SF-2026-ARXIV-2607-24866:start --><!-- existing:SF-2026-ARXIV-2607-24866:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L14-L14`）为：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2607-24866:end --><!-- delta:SF-2026-ARXIV-2607-24866:start -->新增证据边界：Versioned human-authored specifications compile into runtime policy/monitor artifacts, sidecar mediation, audit and governance interfaces. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-24866:end --><!-- books-review:SF-2026-ARXIV-2607-24866:end -->

<!-- books-review:SF-2026-ARXIV-2607-23802:start --><!-- existing:SF-2026-ARXIV-2607-23802:start -->对读 `books/part-04-training-system/33-grpo.md#L14-L14` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-23802:end --><!-- delta:SF-2026-ARXIV-2607-23802:start -->新增证据边界：Open-ended tasks are transformed into information-asymmetric self-play games whose internal detection outcome supplies a self-verifiable reward. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23802:end --><!-- books-review:SF-2026-ARXIV-2607-23802:end -->

<!-- books-review:SF-2026-ARXIV-2607-23809:start --><!-- existing:SF-2026-ARXIV-2607-23809:start -->对读 `books/part-07-agent/75-context.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/75-context.md#L14-L14`）为：本章的核心判断是：**Context 是本次模型调用可见的、经过选择和序列化的工作状态。它受 token budget、信息相关性、位置、信任和隐私共同约束；accepted length 不等于 effective utilization。**<!-- existing:SF-2026-ARXIV-2607-23809:end --><!-- delta:SF-2026-ARXIV-2607-23809:start -->新增证据边界：The agent chooses when to compress, externalize removed content and retrieve it later, turning context truncation into an explicit lifecycle policy. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23809:end --><!-- books-review:SF-2026-ARXIV-2607-23809:end -->

<!-- books-review:SF-2026-ARXIV-2607-23815:start --><!-- existing:SF-2026-ARXIV-2607-23815:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L304` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-23815:end --><!-- delta:SF-2026-ARXIV-2607-23815:start -->新增证据边界：A relational query plan becomes a stage/operator DAG; the runtime performs operator-granular admission while the LLM engine retains request scheduling, with token-bound memory estimation, KV pinning and deadlock/fallback control. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L304`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23815:end --><!-- books-review:SF-2026-ARXIV-2607-23815:end -->

<!-- books-review:SF-2026-ARXIV-2607-23844:start --><!-- existing:SF-2026-ARXIV-2607-23844:start -->对读 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14`）为：本章的核心判断是：**生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。**“一次生成更多 token”不自动等于更快；“允许修正”也不自动等于更准。必须把 proposal work、verification/correction、memory、并发和输出提交一起计算。<!-- existing:SF-2026-ARXIV-2607-23844:end --><!-- delta:SF-2026-ARXIV-2607-23844:start -->新增证据边界：Diffusion inference caches features hierarchically across token, frame, block, layer and denoising-step dimensions using workload-specific reuse schedules. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23844:end --><!-- books-review:SF-2026-ARXIV-2607-23844:end -->

<!-- books-review:SF-2026-ARXIV-2607-23870:start --><!-- existing:SF-2026-ARXIV-2607-23870:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-23870:end --><!-- delta:SF-2026-ARXIV-2607-23870:start -->新增证据边界：An offline UAV benchmark evaluates protocol-conditioned decisions from physical observation, policy semantics and safe-action constraints, separating semantic and strict diagnostics. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23870:end --><!-- books-review:SF-2026-ARXIV-2607-23870:end -->

<!-- books-review:SF-2026-ARXIV-2607-23909:start --><!-- existing:SF-2026-ARXIV-2607-23909:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-23909:end --><!-- delta:SF-2026-ARXIV-2607-23909:start -->新增证据边界：One diffusion transformer jointly predicts continuous action chunks and future normalized RGB patches; the future head is a training-time representation constraint and is removed at deployment. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-23909:end --><!-- books-review:SF-2026-ARXIV-2607-23909:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260727-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260727; semantic-review:SA-20260727-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260727-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-23532; review:SF-2026-ARXIV-2607-23693; review:SF-2026-ARXIV-2607-23771; review:SF-2026-ARXIV-2607-24866; review:SF-2026-ARXIV-2607-23802; review:SF-2026-ARXIV-2607-23809; review:SF-2026-ARXIV-2607-23815; review:SF-2026-ARXIV-2607-23844; review:SF-2026-ARXIV-2607-23870; review:SF-2026-ARXIV-2607-23909; semantic-review:SA-20260727-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260727-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260727-MISSION-ASSURANCE; analysis:DA-20260727-CONTROLLER-AWARE-LEARNING; analysis:DA-20260727-RELATIONAL-SERVING; semantic-review:SA-20260727-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260727-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-23532; books-review:SF-2026-ARXIV-2607-23693; books-review:SF-2026-ARXIV-2607-23771; books-review:SF-2026-ARXIV-2607-24866; books-review:SF-2026-ARXIV-2607-23802; books-review:SF-2026-ARXIV-2607-23809; books-review:SF-2026-ARXIV-2607-23815; books-review:SF-2026-ARXIV-2607-23844; books-review:SF-2026-ARXIV-2607-23870; books-review:SF-2026-ARXIV-2607-23909; semantic-review:SA-20260727-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260727-COVERAGE:start -->Fresh-context audit verified 549 unique raw arXiv v1 identities, the frozen ten-family denominator and strict Beijing window [2026-07-26 09:00, 2026-07-27 09:00), with zero identifier overlap against D26 or D28. Artifact accounting matches observed evidence: four families retain artifact or evidence locators, three provide external repositories, and six disclose none. Exactly three families own three verified event-time commits and corresponding SRC-GITHUB-COMMIT attribution. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260727-COVERAGE:end -->
<!-- semantic-review:SA-20260727-EVIDENCE:start -->Fresh-context audit recomputed all ten durable exact-v1 snapshot SHA-256 digests and confirmed packet-to-central-to-Daily consistency for identity, reviewed versions, locators, routes, Score V2, artifact boundaries, benchmark contracts, claim boundaries and dispositions. The three commit-backed families retain exact commit provenance; in-paper evidence and undisclosed artifacts are not promoted into implementation claims. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260727-EVIDENCE:end -->
<!-- semantic-review:SA-20260727-SELECTION:start -->Fresh-context audit verified nine Deep and one Standard routes. The Deep Selection denominator contains exactly all nine eligible families, with three selected narrative units and six source-specific non-selection rationales. The Standard family remains fully reviewed outside Selection. Narrative selection does not reduce any family's Source Review or Books duty. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260727-SELECTION:end -->
<!-- semantic-review:SA-20260727-BOOKS:start -->Fresh-context audit confirmed all four integrations in their unique canonical owners: 2607.23532 in PLATFORM-SECURITY, 2607.23693 in INFER-KV-CACHE, 2607.23771 in TRAIN-GRPO and 2607.23815 in INFER-SCHEDULING. Each passage and exact-v1 Review note preserves the prior valid baseline, changed constraint, state or control ownership, benefit, cost, failure mode, coexistence condition and evidence boundary. The other six families retain bounded No Change dispositions without duplicate Books ownership. Books PASS; finding_count=0.<!-- semantic-review:SA-20260727-BOOKS:end -->

## 8. Ignored Noise

549 个窗口内 identity 中，539 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：4 个 `Integrate`，6 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 9 / Standard 1。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/27/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/33-grpo.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/72-security.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Mission-Level Runtime Assurance for LLM-Assisted ISR Swarms over a Verification-Aware Fabric](https://arxiv.org/abs/2607.23532v1) — first-public（Asia/Shanghai）：2026-07-26；accessed：2026-08-27
- [Compute Globally, Materialize Locally: The Memory Contract of Sparse Event-KV](https://arxiv.org/abs/2607.23693v1) — first-public（Asia/Shanghai）：2026-07-26；accessed：2026-08-27
- [Training Language Models to Cooperate with Inference-Time Controllers](https://arxiv.org/abs/2607.23771v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [The Missing Layer: Specification Infrastructure for AI Oversight](https://arxiv.org/abs/2607.24866v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open-Ended LLM Self-Improvement](https://arxiv.org/abs/2607.23802v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [ACM: Agentic Context Management for Long Horizon Tasks](https://arxiv.org/abs/2607.23809v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [Kalypso: Relational LLM Serving](https://arxiv.org/abs/2607.23815v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [OmniCache: Multidimensional Hierarchical Feature Caching For Diffusion Models](https://arxiv.org/abs/2607.23844v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [MulRobBench: A Decision-Level Benchmark for Safe and Security-Policy-Compliant Multimodal UAV Agents](https://arxiv.org/abs/2607.23870v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909v1) — first-public（Asia/Shanghai）：2026-07-27；accessed：2026-08-27
- [July recovery snapshot](../_sources/arxiv-v2.1-replay-20260727-31/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
