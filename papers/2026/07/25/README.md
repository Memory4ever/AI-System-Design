# Daily Research — 2026-07-25

**Research Date:** 2026-07-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-24 09:00:00 ～ 2026-07-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 880 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 8 个。当前路由账目为 6 个 Deep、2 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-25 |
| Window End | 2026-07-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-25-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-24T09:00:00+08:00 | 2026-07-25T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 880 | SF-2026-ARXIV-2607-21918<br>SF-2026-ARXIV-2607-21927<br>SF-2026-ARXIV-2607-21962<br>SF-2026-ARXIV-2607-21985<br>SF-2026-ARXIV-2607-22000<br>SF-2026-ARXIV-2607-22043<br>SF-2026-ARXIV-2607-22242<br>SF-2026-ARXIV-2607-22389 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-25T09:00:00+08:00 | coverage:SRC-ARXIV:20260725 | GAP-ARXIV-DIRECT-RESET-20260725 |

<!-- coverage:SRC-ARXIV:20260725:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 880 unique identities in this strict window; 8 routed families.<!-- coverage:SRC-ARXIV:20260725:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 8 个 family：exact v1 为 5 个 family 披露 artifact/evidence locator，其中 4 个提供外部 repository/project/demo locator，另有 3 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21918 | arXiv:2607.21918v1 | paper-v1:2607.21918 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21918 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-21918 | no |
| SF-2026-ARXIV-2607-21927 | arXiv:2607.21927v1 | paper-v1:2607.21927 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21927 | self | — | new_in_window | MODEL-LONG-CONTEXT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-21962 | arXiv:2607.21962v1 | paper-v1:2607.21962 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21962 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-21962 | no |
| SF-2026-ARXIV-2607-21985 | arXiv:2607.21985v1 | paper-v1:2607.21985 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21985 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-21985 | no |
| SF-2026-ARXIV-2607-22000 | arXiv:2607.22000v1 | paper-v1:2607.22000 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22000 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22000 | no |
| SF-2026-ARXIV-2607-22043 | arXiv:2607.22043v1 | paper-v1:2607.22043 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22043 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2607-22043 | no |
| SF-2026-ARXIV-2607-22242 | arXiv:2607.22242v1 | paper-v1:2607.22242 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22242 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22242 | no |
| SF-2026-ARXIV-2607-22389 | arXiv:2607.22389v1 | paper-v1:2607.22389 | 2026-W30 | 2026-07-24 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22389 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2607-22389 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21918 | RP-0989eca664b51640 | deep | arXiv:2607.21918v1 | SRC-ARXIV@arXiv:2607.21918v1 | https://arxiv.org/html/2607.21918v1#S2.SS1; https://arxiv.org/html/2607.21918v1#S2.SS2; https://arxiv.org/html/2607.21918v1#S2.SS3 | https://arxiv.org/html/2607.21918v1#S3 | https://arxiv.org/html/2607.21918v1#S4; https://arxiv.org/html/2607.21918v1#S5 | Not Disclosed — exact v1 does not disclose a public executable artifact; no code or dataset behavior claim is retained | claim:SF-2026-ARXIV-2607-21918 | complete |
| SF-2026-ARXIV-2607-21927 | RP-0fcc271572ebbb07 | standard | arXiv:2607.21927v1 | SRC-ARXIV@arXiv:2607.21927v1 | https://arxiv.org/html/2607.21927v1#S4.SS1; https://arxiv.org/html/2607.21927v1#S4.SS2; https://arxiv.org/html/2607.21927v1#S4.SS3; https://arxiv.org/html/2607.21927v1#S4.SS4 | https://arxiv.org/html/2607.21927v1#S2.SS1; https://arxiv.org/html/2607.21927v1#S2.SS2; https://arxiv.org/html/2607.21927v1#S2.SS3; https://arxiv.org/html/2607.21927v1#S2.SS4 | https://arxiv.org/html/2607.21927v1#S3; https://arxiv.org/html/2607.21927v1#S4.SS1 | https://github.com/santosardr/riskernel — repository disclosed by exact v1; https://doi.org/10.24433/CO.0351350.v1 — Code Ocean capsule disclosed by exact v1; neither artifact was executed and an immutable event-time commit was not audited | claim:SF-2026-ARXIV-2607-21927 | complete |
| SF-2026-ARXIV-2607-21962 | RP-205f551670103654 | deep | arXiv:2607.21962v1 | SRC-ARXIV@arXiv:2607.21962v1 | https://arxiv.org/html/2607.21962v1#S3.SS1; https://arxiv.org/html/2607.21962v1#S3.SS2; https://arxiv.org/html/2607.21962v1#S3.SS3; https://arxiv.org/html/2607.21962v1#S3.SS4; https://arxiv.org/html/2607.21962v1#S4 | https://arxiv.org/html/2607.21962v1#S5.SS4; https://arxiv.org/html/2607.21962v1#S5.SS5; https://arxiv.org/html/2607.21962v1#A1; https://arxiv.org/html/2607.21962v1#A2 | https://arxiv.org/html/2607.21962v1#S7; https://arxiv.org/html/2607.21962v1#S8 | https://github.com/veracium-ai/Veracium — repository disclosed by exact v1; event-time immutable commit and executable behavior were not audited | claim:SF-2026-ARXIV-2607-21962 | complete |
| SF-2026-ARXIV-2607-21985 | RP-144af6b10536e8f6 | deep | arXiv:2607.21985v1 | SRC-ARXIV@arXiv:2607.21985v1 | https://arxiv.org/html/2607.21985v1#S3.SS1; https://arxiv.org/html/2607.21985v1#S3.SS2; https://arxiv.org/html/2607.21985v1#S4 | https://arxiv.org/html/2607.21985v1#S5.SS1; https://arxiv.org/html/2607.21985v1#S5.SS2; https://arxiv.org/html/2607.21985v1#S5.SS3; https://arxiv.org/html/2607.21985v1#S5.SS4; https://arxiv.org/html/2607.21985v1#S5.SS5 | https://arxiv.org/html/2607.21985v1#S6 | https://github.com/AIDASLab/SPDP — official repository disclosed by exact v1; event-time immutable commit and executable behavior were not audited | claim:SF-2026-ARXIV-2607-21985 | complete |
| SF-2026-ARXIV-2607-22000 | RP-a521fa76a0a75c6d | standard | arXiv:2607.22000v1 | SRC-ARXIV@arXiv:2607.22000v1 | https://arxiv.org/html/2607.22000v1#S3; https://arxiv.org/html/2607.22000v1#S3.SS4 | https://arxiv.org/html/2607.22000v1#S4.SS3; https://arxiv.org/html/2607.22000v1#S4.SS4; https://arxiv.org/html/2607.22000v1#S4.SS5 | https://arxiv.org/html/2607.22000v1#S5 | https://zzwaang.github.io/music-jepa-demo/ — demo disclosed by exact v1; code and checkpoints were only promised for future release, so no executable artifact claim is retained | claim:SF-2026-ARXIV-2607-22000 | complete |
| SF-2026-ARXIV-2607-22043 | RP-77d98df3270ca68d | deep | arXiv:2607.22043v1 | SRC-ARXIV@arXiv:2607.22043v1 | https://arxiv.org/html/2607.22043v1#S2.SS1; https://arxiv.org/html/2607.22043v1#S2.SS3; https://arxiv.org/html/2607.22043v1#S3 | https://arxiv.org/html/2607.22043v1#S4.SS1; https://arxiv.org/html/2607.22043v1#S4.SS2; https://arxiv.org/html/2607.22043v1#S4.SS3; https://arxiv.org/html/2607.22043v1#A2 | https://arxiv.org/html/2607.22043v1#S6 | Not Disclosed — exact v1 does not disclose an independently executable training artifact; no code or checkpoint behavior claim is retained | claim:SF-2026-ARXIV-2607-22043 | complete |
| SF-2026-ARXIV-2607-22242 | RP-8a2298ff792e0877 | deep | arXiv:2607.22242v1 | SRC-ARXIV@arXiv:2607.22242v1 | https://arxiv.org/html/2607.22242v1#S2; https://arxiv.org/html/2607.22242v1#S2.SS2; https://arxiv.org/html/2607.22242v1#S3 | https://arxiv.org/html/2607.22242v1#S4; https://arxiv.org/html/2607.22242v1#S4.SS5; https://arxiv.org/html/2607.22242v1#A1; https://arxiv.org/html/2607.22242v1#A3 | https://arxiv.org/html/2607.22242v1#S5 | https://arxiv.org/html/2607.22242v1#A2 — exact-v1 prompt and scheduler example; https://arxiv.org/html/2607.22242v1#A3 — exact-v1 mapping trace; no separately executable artifact is disclosed | claim:SF-2026-ARXIV-2607-22242 | complete |
| SF-2026-ARXIV-2607-22389 | RP-db5960c10d25507c | deep | arXiv:2607.22389v1 | SRC-ARXIV@arXiv:2607.22389v1 | https://arxiv.org/html/2607.22389v1#S3.SS2; https://arxiv.org/html/2607.22389v1#S3.SS3; https://arxiv.org/html/2607.22389v1#S4 | https://arxiv.org/html/2607.22389v1#S5.SS1; https://arxiv.org/html/2607.22389v1#S5.SS2; https://arxiv.org/html/2607.22389v1#S5.SS3; https://arxiv.org/html/2607.22389v1#S5.SS4 | https://arxiv.org/html/2607.22389v1#S6 | Not Disclosed — exact v1 does not disclose a public executable HiKV artifact; evaluation claims remain limited to the paper's algorithm and modeled hardware contract | claim:SF-2026-ARXIV-2607-22389 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-21918:start -->
#### Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound

<!-- claim:SF-2026-ARXIV-2607-21918:start -->A frozen action-conditioned latent transition model becomes a reward-bearing component of a bounded perception-action loop; real observation remains the authority after every action. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-21918:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A frozen action-conditioned latent transition model becomes a reward-bearing component of a bounded perception-action loop; real observation remains the authority after every action. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.21918v1#S2.SS1; https://arxiv.org/html/2607.21918v1#S2.SS2; https://arxiv.org/html/2607.21918v1#S2.SS3`；Evaluation：`https://arxiv.org/html/2607.21918v1#S3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.21918v1#S4; https://arxiv.org/html/2607.21918v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-21918:end -->

<!-- review:SF-2026-ARXIV-2607-21927:start -->
#### RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-21927:start -->RIS combines cached stochastic global anchors, a recent local window and dynamic positional scaling as an experimental sparse-attention branch whose coverage and extrapolation errors remain distinct. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-21927:end -->

**旧方案与约束变化。** `本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。`（`books/part-02-model/22-long-context.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** RIS combines cached stochastic global anchors, a recent local window and dynamic positional scaling as an experimental sparse-attention branch whose coverage and extrapolation errors remain distinct. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.21927v1#S4.SS1; https://arxiv.org/html/2607.21927v1#S4.SS2; https://arxiv.org/html/2607.21927v1#S4.SS3; https://arxiv.org/html/2607.21927v1#S4.SS4`；Evaluation：`https://arxiv.org/html/2607.21927v1#S2.SS1; https://arxiv.org/html/2607.21927v1#S2.SS2; https://arxiv.org/html/2607.21927v1#S2.SS3; https://arxiv.org/html/2607.21927v1#S2.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.21927v1#S3; https://arxiv.org/html/2607.21927v1#S4.SS1`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-21927:end -->

<!-- review:SF-2026-ARXIV-2607-21962:start -->
#### Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

<!-- claim:SF-2026-ARXIV-2607-21962:start -->Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-21962:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.21962v1#S3.SS1; https://arxiv.org/html/2607.21962v1#S3.SS2; https://arxiv.org/html/2607.21962v1#S3.SS3; https://arxiv.org/html/2607.21962v1#S3.SS4; https://arxiv.org/html/2607.21962v1#S4`；Evaluation：`https://arxiv.org/html/2607.21962v1#S5.SS4; https://arxiv.org/html/2607.21962v1#S5.SS5; https://arxiv.org/html/2607.21962v1#A1; https://arxiv.org/html/2607.21962v1#A2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.21962v1#S7; https://arxiv.org/html/2607.21962v1#S8`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L415-L423`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-21962:end -->

<!-- review:SF-2026-ARXIV-2607-21985:start -->
#### Unified Static-Dynamic Pruning for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-21985:start -->Static weight sparsity and input-dependent activation sparsity become composable through a shared column-addressable representation with phase-specific decode and prefill kernels. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-21985:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Static weight sparsity and input-dependent activation sparsity become composable through a shared column-addressable representation with phase-specific decode and prefill kernels. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.21985v1#S3.SS1; https://arxiv.org/html/2607.21985v1#S3.SS2; https://arxiv.org/html/2607.21985v1#S4`；Evaluation：`https://arxiv.org/html/2607.21985v1#S5.SS1; https://arxiv.org/html/2607.21985v1#S5.SS2; https://arxiv.org/html/2607.21985v1#S5.SS3; https://arxiv.org/html/2607.21985v1#S5.SS4; https://arxiv.org/html/2607.21985v1#S5.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.21985v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-21985:end -->

<!-- review:SF-2026-ARXIV-2607-22000:start -->
#### Music-JEPA: Learning a World Model of Sound from Action

<!-- claim:SF-2026-ARXIV-2607-22000:start -->An audio JEPA reuses action-conditioned latent transition semantics for controllable sound, but remains an offline piano-domain case already covered by the world-model abstraction. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-22000:end -->

**旧方案与约束变化。** `本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An audio JEPA reuses action-conditioned latent transition semantics for controllable sound, but remains an offline piano-domain case already covered by the world-model abstraction. 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.22000v1#S3; https://arxiv.org/html/2607.22000v1#S3.SS4`；Evaluation：`https://arxiv.org/html/2607.22000v1#S4.SS3; https://arxiv.org/html/2607.22000v1#S4.SS4; https://arxiv.org/html/2607.22000v1#S4.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.22000v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-22000:end -->

<!-- review:SF-2026-ARXIV-2607-22043:start -->
#### Scaling Native Multimodal Pre-Training From Scratch

<!-- claim:SF-2026-ARXIV-2607-22043:start -->Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-22043:end -->

**旧方案与约束变化。** `本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。`（`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets. 它改变 `MULTIMODAL-REPRESENTATION` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.22043v1#S2.SS1; https://arxiv.org/html/2607.22043v1#S2.SS3; https://arxiv.org/html/2607.22043v1#S3`；Evaluation：`https://arxiv.org/html/2607.22043v1#S4.SS1; https://arxiv.org/html/2607.22043v1#S4.SS2; https://arxiv.org/html/2607.22043v1#S4.SS3; https://arxiv.org/html/2607.22043v1#A2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.22043v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L424-L432`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`MULTIMODAL-REPRESENTATION`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-22043:end -->

<!-- review:SF-2026-ARXIV-2607-22242:start -->
#### Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads

<!-- claim:SF-2026-ARXIV-2607-22242:start -->An LLM proposes heterogeneous placement from monitored CPU, immediate-GPU and queued-GPU state, while a deterministic executor retains DAG and memory-feasibility authority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-22242:end -->

**旧方案与约束变化。** `本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**`（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An LLM proposes heterogeneous placement from monitored CPU, immediate-GPU and queued-GPU state, while a deterministic executor retains DAG and memory-feasibility authority. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.22242v1#S2; https://arxiv.org/html/2607.22242v1#S2.SS2; https://arxiv.org/html/2607.22242v1#S3`；Evaluation：`https://arxiv.org/html/2607.22242v1#S4; https://arxiv.org/html/2607.22242v1#S4.SS5; https://arxiv.org/html/2607.22242v1#A1; https://arxiv.org/html/2607.22242v1#A3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.22242v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 2 = **7/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-22242:end -->

<!-- review:SF-2026-ARXIV-2607-22389:start -->
#### HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding

<!-- claim:SF-2026-ARXIV-2607-22389:start -->Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-22389:end -->

**旧方案与约束变化。** `本章的核心判断是：**GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。**任何调度和加速机制最终都必须满足这个物理约束。`（`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter. 它改变 `INFER-GPU-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.22389v1#S3.SS2; https://arxiv.org/html/2607.22389v1#S3.SS3; https://arxiv.org/html/2607.22389v1#S4`；Evaluation：`https://arxiv.org/html/2607.22389v1#S5.SS1; https://arxiv.org/html/2607.22389v1#S5.SS2; https://arxiv.org/html/2607.22389v1#S5.SS3; https://arxiv.org/html/2607.22389v1#S5.SS4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.22389v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L392-L414`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-GPU-MEMORY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-22389:end -->

## 4. Benchmark Contracts

本日报不转述性能 headline，`Benchmark Claim` 均为 `no`。论文实验只用于限定机制证据，不把不同模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 拼成跨论文排名。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21918 | score_7_9;potential_books_delta | not_selected | — | — | The action-conditioned transition and real-observation loop are important, but the week-level narrative already has a more general world-model evolution unit; retain as a fully reviewed Books case, not a duplicate narrative slot. | analysis-decision:SF-2026-ARXIV-2607-21918 |
| SF-2026-ARXIV-2607-21962 | score_7_9;potential_books_delta | selected | AU-20260725-21962 | — | V2=8/9；Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260725-21962 |
| SF-2026-ARXIV-2607-21985 | score_7_9;potential_books_delta | not_selected | — | — | The shared sparse representation and phase-specific kernels are fully reviewed for Books, but the narrative slot would overlap the broader execution-plan evolution already represented elsewhere. | analysis-decision:SF-2026-ARXIV-2607-21985 |
| SF-2026-ARXIV-2607-22043 | score_7_9;potential_books_delta | selected | AU-20260725-22043 | — | V2=9/9；Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260725-22043 |
| SF-2026-ARXIV-2607-22242 | score_7_9 | not_selected | — | — | The advisory-versus-authoritative scheduling boundary is durable and fully reviewed, but the evidence is limited to thirteen constructed scenarios and is narrower than the selected units. | analysis-decision:SF-2026-ARXIV-2607-22242 |
| SF-2026-ARXIV-2607-22389 | score_7_9;potential_books_delta | selected | AU-20260725-22389 | — | V2=8/9；Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260725-22389 |

<!-- analysis:AU-20260725-21962:start -->
### Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

**旧方案为何合理。** Conversation-first short-horizon sets are cheap and remain useful smoke tests; full history is a valid small-tenure reference when token pressure has not arrived.（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Truth-first construction improves auditability and reveals tenure crossover, but uses synthetic users and adds provenance/version-control obligations; accuracy still does not prove cautious behavior.

<!-- analysis:AU-20260725-21962:end -->

<!-- analysis:AU-20260725-22043:start -->
### Scaling Native Multimodal Pre-Training From Scratch

**旧方案为何合理。** Late fusion remains rational for encoder reuse, cheaper upgrades and modality-specific specialization; scalar compute-optimal rules are sufficient only for one objective and one token economy.（现有命题定位：`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）

**约束变化与机制。** Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `MULTIMODAL-REPRESENTATION` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Native integration can transfer across modalities but couples budgets and makes allocation Pareto; the fitted exponents remain architecture, data and measurement specific.

<!-- analysis:AU-20260725-22043:end -->

<!-- analysis:AU-20260725-22389:start -->
### HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding

**旧方案为何合理。** Full KV is the exact baseline; token-only eviction is simpler and fits existing accelerators when retained-vector traffic is not dominant.（现有命题定位：`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）

**约束变化与机制。** Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-GPU-MEMORY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Two-granularity reduction adds approximation, offline calibration, fragmented accesses and specialized ranking hardware; commercial-GPU and production-SLO transfer are unproven.

<!-- analysis:AU-20260725-22389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21918:start -->《Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound》已完成 Deep Source Review。The action-conditioned transition and real-observation loop are important, but the week-level narrative already has a more general world-model evolution unit; retain as a fully reviewed Books case, not a duplicate narrative slot.<!-- analysis-decision:SF-2026-ARXIV-2607-21918:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21985:start -->《Unified Static-Dynamic Pruning for Efficient LLM Inference》已完成 Deep Source Review。The shared sparse representation and phase-specific kernels are fully reviewed for Books, but the narrative slot would overlap the broader execution-plan evolution already represented elsewhere.<!-- analysis-decision:SF-2026-ARXIV-2607-21985:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22242:start -->《Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads》已完成 Deep Source Review。The advisory-versus-authoritative scheduling boundary is durable and fully reviewed, but the evidence is limited to thirteen constructed scenarios and is narrower than the selected units.<!-- analysis-decision:SF-2026-ARXIV-2607-22242:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21918 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-21918 | delta:SF-2026-ARXIV-2607-21918 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-21918 |
| SF-2026-ARXIV-2607-21962 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L736 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-21962 | delta:SF-2026-ARXIV-2607-21962 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-21962 |
| SF-2026-ARXIV-2607-21985 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L172 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-21985 | delta:SF-2026-ARXIV-2607-21985 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-21985 |
| SF-2026-ARXIV-2607-22000 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-22000 | delta:SF-2026-ARXIV-2607-22000 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22000 |
| SF-2026-ARXIV-2607-22043 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L69 | books/part-02-model/22-long-context.md#L14-L14; books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14 | existing:SF-2026-ARXIV-2607-22043 | delta:SF-2026-ARXIV-2607-22043 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-22043 |
| SF-2026-ARXIV-2607-22242 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L14-L14 | books/part-05-inference-system/55-pd-disaggregation.md#L14-L14; books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L14-L14 | existing:SF-2026-ARXIV-2607-22242 | delta:SF-2026-ARXIV-2607-22242 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22242 |
| SF-2026-ARXIV-2607-22389 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L188 | books/part-05-inference-system/53-kserve-llm.md#L14-L14; books/part-05-inference-system/55-pd-disaggregation.md#L14-L14 | existing:SF-2026-ARXIV-2607-22389 | delta:SF-2026-ARXIV-2607-22389 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-22389 |

<!-- books-review:SF-2026-ARXIV-2607-21918:start --><!-- existing:SF-2026-ARXIV-2607-21918:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-21918:end --><!-- delta:SF-2026-ARXIV-2607-21918:start -->新增证据边界：A frozen action-conditioned latent transition model becomes a reward-bearing component of a bounded perception-action loop; real observation remains the authority after every action. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-21918:end --><!-- books-review:SF-2026-ARXIV-2607-21918:end -->

<!-- books-review:SF-2026-ARXIV-2607-21962:start --><!-- existing:SF-2026-ARXIV-2607-21962:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L736` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-21962:end --><!-- delta:SF-2026-ARXIV-2607-21962:start -->新增证据边界：Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L736`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-21962:end --><!-- books-review:SF-2026-ARXIV-2607-21962:end -->

<!-- books-review:SF-2026-ARXIV-2607-21985:start --><!-- existing:SF-2026-ARXIV-2607-21985:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L172` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-21985:end --><!-- delta:SF-2026-ARXIV-2607-21985:start -->新增证据边界：Static weight sparsity and input-dependent activation sparsity become composable through a shared column-addressable representation with phase-specific decode and prefill kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L172`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-21985:end --><!-- books-review:SF-2026-ARXIV-2607-21985:end -->

<!-- books-review:SF-2026-ARXIV-2607-22000:start --><!-- existing:SF-2026-ARXIV-2607-22000:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14`）为：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2607-22000:end --><!-- delta:SF-2026-ARXIV-2607-22000:start -->新增证据边界：An audio JEPA reuses action-conditioned latent transition semantics for controllable sound, but remains an offline piano-domain case already covered by the world-model abstraction. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-22000:end --><!-- books-review:SF-2026-ARXIV-2607-22000:end -->

<!-- books-review:SF-2026-ARXIV-2607-22043:start --><!-- existing:SF-2026-ARXIV-2607-22043:start -->对读 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L69` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/23-multimodal-representation.md#L14-L14`）为：本章的核心判断是：**多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。**共享 backbone 可以统一计算接口，却不会自动统一语义、采样率、误差模型和数据权利。<!-- existing:SF-2026-ARXIV-2607-22043:end --><!-- delta:SF-2026-ARXIV-2607-22043:start -->新增证据边界：Native multimodal pretraining turns shared capacity allocation into a multi-objective Pareto decision because text and multimodal losses prefer different parameter and token budgets. 该 delta 已进入 `books/part-03-multimodal-world-models/23-multimodal-representation.md#L69`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-22043:end --><!-- books-review:SF-2026-ARXIV-2607-22043:end -->

<!-- books-review:SF-2026-ARXIV-2607-22242:start --><!-- existing:SF-2026-ARXIV-2607-22242:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L14-L14`）为：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2607-22242:end --><!-- delta:SF-2026-ARXIV-2607-22242:start -->新增证据边界：An LLM proposes heterogeneous placement from monitored CPU, immediate-GPU and queued-GPU state, while a deterministic executor retains DAG and memory-feasibility authority. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-22242:end --><!-- books-review:SF-2026-ARXIV-2607-22242:end -->

<!-- books-review:SF-2026-ARXIV-2607-22389:start --><!-- existing:SF-2026-ARXIV-2607-22389:start -->对读 `books/part-05-inference-system/54-gpu-memory.md#L188` 与相邻章节后，现有命题（`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）为：本章的核心判断是：**GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。**任何调度和加速机制最终都必须满足这个物理约束。<!-- existing:SF-2026-ARXIV-2607-22389:end --><!-- delta:SF-2026-ARXIV-2607-22389:start -->新增证据边界：Hierarchical token and element selection exposes intra-token vector fetch as a second KV bandwidth floor and co-designs ranking state with a reconfigurable sorter. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L188`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-22389:end --><!-- books-review:SF-2026-ARXIV-2607-22389:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260725-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260725; semantic-review:SA-20260725-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260725-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-21918; review:SF-2026-ARXIV-2607-21927; review:SF-2026-ARXIV-2607-21962; review:SF-2026-ARXIV-2607-21985; review:SF-2026-ARXIV-2607-22000; review:SF-2026-ARXIV-2607-22043; review:SF-2026-ARXIV-2607-22242; review:SF-2026-ARXIV-2607-22389; semantic-review:SA-20260725-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260725-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:AU-20260725-21962; analysis:AU-20260725-22043; analysis:AU-20260725-22389; semantic-review:SA-20260725-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260725-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-21918; books-review:SF-2026-ARXIV-2607-21962; books-review:SF-2026-ARXIV-2607-21985; books-review:SF-2026-ARXIV-2607-22000; books-review:SF-2026-ARXIV-2607-22043; books-review:SF-2026-ARXIV-2607-22242; books-review:SF-2026-ARXIV-2607-22389; review:SF-2026-ARXIV-2607-21927; semantic-review:SA-20260725-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260725-COVERAGE:start -->Fresh-context audit verified the frozen eight-family denominator, strict Beijing window [2026-07-24 09:00, 2026-07-25 09:00), exact-v1 ownership and zero identifier overlap against D24 or D26. Artifact accounting now distinguishes five families with artifact or evidence locators, including four with external repository, project or demo locators and one with in-paper appendix evidence only; three families disclose none. No event-time pinned commit or SRC-GITHUB-COMMIT attribution is present. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260725-COVERAGE:end -->
<!-- semantic-review:SA-20260725-EVIDENCE:start -->Fresh-context audit recomputed all eight durable exact-v1 snapshot SHA-256 digests and confirmed packet-to-central-to-Daily consistency for identities, reviewed versions, locators, routes, Score V2, artifact boundaries, benchmark boundaries and dispositions. The 2607.22242 receipt remains limited to exact-v1 appendix anchors A2 and A3, explicitly states that no separately executable artifact was disclosed, and carries no unsupported commit attribution. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260725-EVIDENCE:end -->
<!-- semantic-review:SA-20260725-SELECTION:start -->Fresh-context audit verified six Deep and two Standard routes. The Deep Selection denominator contains exactly the six eligible families, with three selected narrative units and three source-specific non-selection rationales; the two Standard families remain outside Selection without losing completed reviews or dispositions. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260725-SELECTION:end -->
<!-- semantic-review:SA-20260725-BOOKS:start -->Fresh-context regression audit confirmed all four integrations in their unique canonical owners: 2607.21962 in PLATFORM-EVALUATION-SYSTEM, 2607.21985 in INFER-TENSORRT-LLM, 2607.22043 in MULTIMODAL-REPRESENTATION and 2607.22389 in INFER-GPU-MEMORY. Each mechanism passage and exact-v1 Review note preserves the old baseline, changed constraint, state or control transition, benefit, trade-off, failure mode, coexistence condition and evidence boundary. Three No Change and one Weekly Only dispositions remain consistent across packet and Daily. Books PASS; finding_count=0.<!-- semantic-review:SA-20260725-BOOKS:end -->

## 8. Ignored Noise

880 个窗口内 identity 中，872 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：4 个 `Integrate`，3 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 6 / Standard 2。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/25/README.md`。
- 本日报长期 delta 已同步至：`books/part-03-multimodal-world-models/23-multimodal-representation.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/54-gpu-memory.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound](https://arxiv.org/abs/2607.21918v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/abs/2607.21927v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [Unified Static-Dynamic Pruning for Efficient LLM Inference](https://arxiv.org/abs/2607.21985v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [Music-JEPA: Learning a World Model of Sound from Action](https://arxiv.org/abs/2607.22000v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/abs/2607.22043v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads](https://arxiv.org/abs/2607.22242v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding](https://arxiv.org/abs/2607.22389v1) — first-public（Asia/Shanghai）：2026-07-24；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
