# Daily Research — 2026-07-26

**Research Date:** 2026-07-26

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-25 09:00:00 ～ 2026-07-26 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 447 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 2 个。当前路由账目为 1 个 Deep、0 个 Standard、1 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-26 |
| Window End | 2026-07-26 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-26-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-25T09:00:00+08:00 | 2026-07-26T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 447 | SF-2026-ARXIV-2607-22997<br>SF-2026-ARXIV-2607-23250 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-26T09:00:00+08:00 | coverage:SRC-ARXIV:20260726 | GAP-ARXIV-DIRECT-RESET-20260726 |

<!-- coverage:SRC-ARXIV:20260726:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 447 unique identities in this strict window; 2 routed families.<!-- coverage:SRC-ARXIV:20260726:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 2 个 family：exact v1 为 1 个 family 披露 artifact/evidence locator，其中 1 个提供外部 repository/project/demo locator，另有 1 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22997 | arXiv:2607.22997v1 | paper-v1:2607.22997 | 2026-W30 | 2026-07-25 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-22997 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22997 | no |
| SF-2026-ARXIV-2607-23250 | arXiv:2607.23250v1 | paper-v1:2607.23250 | 2026-W30 | 2026-07-25 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-23250 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2607-23250 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22997 | RP-453c987cd265e91e | closure | arXiv:2607.22997v1 | SRC-ARXIV@arXiv:2607.22997v1 | https://arxiv.org/html/2607.22997v1#S2; https://arxiv.org/html/2607.22997v1#S4 | https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1; https://arxiv.org/html/2607.22997v1#S5 | https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1 — the real-robot transfer evidence is qualitative and scoped to the described basic pick-and-place distribution; https://arxiv.org/html/2607.22997v1#S5.SS0.SSS0.Px1 — cross-device throughput is task/algorithm dependent and the text itself attributes results to unisolated host, synchronization and batch effects | https://github.com/AMD-AIM/Physical_AI_Challenge; https://github.com/PhysicalAI-AIM/Robot_synthetic_data_generation_workshop; https://github.com/ZJLi2013/vk-gsplat-plugin — exact v1 discloses these resources, but event-time immutable commits and an end-to-end reproduction were not audited, so no code-level or reproducibility claim is retained | claim:SF-2026-ARXIV-2607-22997 | complete |
| SF-2026-ARXIV-2607-23250 | RP-d9301f62f4a46260 | deep | arXiv:2607.23250v1 | SRC-ARXIV@arXiv:2607.23250v1 | https://arxiv.org/html/2607.23250v1#S3.SS2; https://arxiv.org/html/2607.23250v1#S4.SS1; https://arxiv.org/html/2607.23250v1#S4.SS2; https://arxiv.org/html/2607.23250v1#S4.SS3; https://arxiv.org/html/2607.23250v1#S4.SS4; https://arxiv.org/html/2607.23250v1#S5 | https://arxiv.org/html/2607.23250v1#S6.SS1; https://arxiv.org/html/2607.23250v1#S6.SS2; https://arxiv.org/html/2607.23250v1#S6.SS3; https://arxiv.org/html/2607.23250v1#S6.SS4; https://arxiv.org/html/2607.23250v1#S6.SS5; https://arxiv.org/html/2607.23250v1#S6.SS6 | https://arxiv.org/html/2607.23250v1#S2.SS2 — the design is scoped to dense causal attention; sparse or linear attention is left to future work; https://arxiv.org/html/2607.23250v1#S5.p6 — raw-sample step semantics are preserved but bitwise-equivalent gradients, optimizer states and trajectories are explicitly not claimed; https://arxiv.org/html/2607.23250v1#S6.SS1 — WLB-LLM is reimplemented without outlier deferral and DistCA is scope-emulated rather than run end-to-end; PP bubble reduction is inferred from forward-time compression rather than a pipeline trace | Not Disclosed — exact v1 contains no public Libra code or artifact URL; the MagiAttention repository is a cited baseline resource, not the reviewed system's implementation | claim:SF-2026-ARXIV-2607-23250 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-22997:start -->
#### Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline

<!-- claim:SF-2026-ARXIV-2607-22997:start -->The exact v1 supports that the authors assembled and demonstrated the described AMD/ROCm workflows and disclosed resource links. It does not prove general sim-to-real robustness, safety, causal world-model correctness, matched cross-hardware superiority, or artifact-complete reproduction. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-22997:end -->

**旧方案与约束变化。** `本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The paper composes Genesis simulation, LeRobot-format demonstrations, SmolVLA fine-tuning, 3DGS scene reconstruction, ROCm/PyTorch execution and physical Franka deployment into four demonstrations on AMD hardware. It is a portability and workflow-integration case, not a new VLA, sim-to-real, control, or scheduling mechanism. 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.22997v1#S2; https://arxiv.org/html/2607.22997v1#S4`；Evaluation：`https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1; https://arxiv.org/html/2607.22997v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.22997v1#S2.SS0.SSS0.Px1 — the real-robot transfer evidence is qualitative and scoped to the described basic pick-and-place distribution; https://arxiv.org/html/2607.22997v1#S5.SS0.SSS0.Px1 — cross-device throughput is task/algorithm dependent and the text itself attributes results to unisolated host, synchronization and batch effects`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 1 / System Reach 2 / Durability 1 = **4/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-22997:end -->

<!-- review:SF-2026-ARXIV-2607-23250:start -->
#### Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool

<!-- claim:SF-2026-ARXIV-2607-23250:start -->The exact v1 supports that equal-token packing can leave dense-attention workload skew, and that a bounded sequence-pool design with step-preserving placement, sequence-head tiling and overlapped tensor exchange improved the stated Qwen3/NVIDIA workloads. It does not establish bitwise training equivalence, sparse/linear-attention applicability, complete end-to-end superiority over WLB-LLM or DistCA, public reproducibility, or topology-independent gains. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-23250:end -->

**旧方案与约束变化。** `本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。`（`books/part-04-training-system/36-distributed-training.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Libra freezes the raw-sample multiset of each optimizer step, partitions its DP replicas into fixed-size sequence pools, uses exact-cardinality variance-reduced placement to pair complementary packed-sequence workloads across pools, then dispatches sequence-by-head tiles within each pool. A CPU planner emits per-iteration plans; the GPU executor performs planned Q/K/V and output all-to-all around an unmodified variable-length FlashAttention kernel, with chunked overlap. Scaling DP creates more pools rather than expanding the communication domain of each pool. 它改变 `TRAIN-DISTRIBUTED-TRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.23250v1#S3.SS2; https://arxiv.org/html/2607.23250v1#S4.SS1; https://arxiv.org/html/2607.23250v1#S4.SS2; https://arxiv.org/html/2607.23250v1#S4.SS3; https://arxiv.org/html/2607.23250v1#S4.SS4; https://arxiv.org/html/2607.23250v1#S5`；Evaluation：`https://arxiv.org/html/2607.23250v1#S6.SS1; https://arxiv.org/html/2607.23250v1#S6.SS2; https://arxiv.org/html/2607.23250v1#S6.SS3; https://arxiv.org/html/2607.23250v1#S6.SS4; https://arxiv.org/html/2607.23250v1#S6.SS5; https://arxiv.org/html/2607.23250v1#S6.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.23250v1#S2.SS2 — the design is scoped to dense causal attention; sparse or linear attention is left to future work; https://arxiv.org/html/2607.23250v1#S5.p6 — raw-sample step semantics are preserved but bitwise-equivalent gradients, optimizer states and trajectories are explicitly not claimed; https://arxiv.org/html/2607.23250v1#S6.SS1 — WLB-LLM is reimplemented without outlier deferral and DistCA is scope-emulated rather than run end-to-end; PP bubble reduction is inferred from forward-time compression rather than a pipeline trace`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-DISTRIBUTED-TRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-23250:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23250 | Long-context Qwen3 training with long-tailed raw-sample lengths packed into 256K- and 1M-token sequences; separate core-attention microbenchmarks | Qwen3-30B-A3B (Qwen3-Turbo) end-to-end; synthetic 128-query-head attention configurations for microbenchmarks | NVIDIA cluster with NVLink intra-node and RoCE inter-node; 8–128 GPUs for 256K DP sweep and 16–256 GPUs for 1M DP sweep; production claims extend to thousands of GPUs without a fully disclosed topology | Not Disclosed | Packed 256K and 1M tokens; production deployment claims 32K to 1M | Not Disclosed — training workload | GBS 128 for 256K and GBS 32 for 1M in principal scale-outs; mbs=1; additional sweeps use stated GBS/DP/CP combinations | DP up to 16, CP 8 or 16 in principal scale-outs; PP=2 in the forward-time distribution experiment | Throughput scaling and slowest-worker core-attention latency; no online serving SLO | Author end-to-end tokens/GPU/s, per-step mean/max slowest-worker latency, VRSP imbalance and component sweeps; Ulysses primary end-to-end baseline |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-23250 | score_7_9;potential_books_delta | selected | DA-20260726-BOUNDED-ATTENTION-POOL | — | V2=9/9；The exact v1 supports that equal-token packing can leave dense-attention workload skew, and that a bounded sequence-pool design with step-preserving placement, sequence-head tiling and overlapped tensor exchange improved the stated Qwen3/NVIDIA workloads. It does not establish bitwise training equivalence, sparse/linear-attention applicability, complete end-to-end superiority over WLB-LLM or DistCA, public reproducibility, or topology-independent gains.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260726-BOUNDED-ATTENTION-POOL |

<!-- analysis:DA-20260726-BOUNDED-ATTENTION-POOL:start -->
### Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool

**旧方案为何合理。** Fixed-token packing plus Ulysses is reasonable when token count approximates work and variation remains within each CP group. Long-tailed raw sequences break that approximation because attention work is quadratic within each constituent sequence, while cluster-wide disaggregation expands the communication and failure domain. The changed constraint is therefore not merely more GPUs, but the scope over which work may be redistributed without changing optimizer-step membership.（现有命题定位：`books/part-04-training-system/36-distributed-training.md#L14-L14`）

**约束变化与机制。** Libra freezes the raw-sample multiset of each optimizer step, partitions its DP replicas into fixed-size sequence pools, uses exact-cardinality variance-reduced placement to pair complementary packed-sequence workloads across pools, then dispatches sequence-by-head tiles within each pool. A CPU planner emits per-iteration plans; the GPU executor performs planned Q/K/V and output all-to-all around an unmodified variable-length FlashAttention kernel, with chunked overlap. Scaling DP creates more pools rather than expanding the communication domain of each pool. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-DISTRIBUTED-TRAINING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** A bounded pool reduces global communication exposure and indivisible-outlier pressure, but adds all-to-all traffic, CPU planning, metadata broadcast, tile/KV bookkeeping and floating-point reordering. Pool size and tile shape are workload/topology dependent; overlap cannot hide first-dispatch/final-return costs, and adding more pools still grows the worst-pool tail. The evidence assumes microbatch size one, dense causal attention, proprietary production datasets and one NVIDIA NVLink/RoCE environment. Ordinary packing/Ulysses remains preferable when sequence skew is mild or orchestration cost dominates; a broader global pool may win inside a uniformly high-bandwidth domain.

<!-- analysis:DA-20260726-BOUNDED-ATTENTION-POOL:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-22997 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-22997 | delta:SF-2026-ARXIV-2607-22997 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-22997 |
| SF-2026-ARXIV-2607-23250 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L358 | books/part-04-training-system/35-checkpoint.md#L14-L14; books/part-04-training-system/37-tensor-parallel.md#L14-L14 | existing:SF-2026-ARXIV-2607-23250 | delta:SF-2026-ARXIV-2607-23250 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-23250 |

<!-- books-review:SF-2026-ARXIV-2607-22997:start --><!-- existing:SF-2026-ARXIV-2607-22997:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14`）为：本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。<!-- existing:SF-2026-ARXIV-2607-22997:end --><!-- delta:SF-2026-ARXIV-2607-22997:start -->新增证据边界：The paper composes Genesis simulation, LeRobot-format demonstrations, SmolVLA fine-tuning, 3DGS scene reconstruction, ROCm/PyTorch execution and physical Franka deployment into four demonstrations on AMD hardware. It is a portability and workflow-integration case, not a new VLA, sim-to-real, control, or scheduling mechanism. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-22997:end --><!-- books-review:SF-2026-ARXIV-2607-22997:end -->

<!-- books-review:SF-2026-ARXIV-2607-23250:start --><!-- existing:SF-2026-ARXIV-2607-23250:start -->对读 `books/part-04-training-system/36-distributed-training.md#L358` 与相邻章节后，现有命题（`books/part-04-training-system/36-distributed-training.md#L14-L14`）为：本章的核心判断是：**分布式训练是在保持训练语义不变量的前提下，把计算、模型状态、activation 与通信映射到设备拓扑的约束优化。**每种并行只直接缓解某类瓶颈，并把一部分本地 memory/compute 问题转化成 collective、pipeline、同步或恢复问题。通信也不能被压缩成一个库名：必须分清语义、算法、runtime、transport 与物理拓扑。<!-- existing:SF-2026-ARXIV-2607-23250:end --><!-- delta:SF-2026-ARXIV-2607-23250:start -->新增证据边界：Libra freezes the raw-sample multiset of each optimizer step, partitions its DP replicas into fixed-size sequence pools, uses exact-cardinality variance-reduced placement to pair complementary packed-sequence workloads across pools, then dispatches sequence-by-head tiles within each pool. A CPU planner emits per-iteration plans; the GPU executor performs planned Q/K/V and output all-to-all around an unmodified variable-length FlashAttention kernel, with chunked overlap. Scaling DP creates more pools rather than expanding the communication domain of each pool. 该 delta 已进入 `books/part-04-training-system/36-distributed-training.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-23250:end --><!-- books-review:SF-2026-ARXIV-2607-23250:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260726-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260726; semantic-review:SA-20260726-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260726-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-22997; review:SF-2026-ARXIV-2607-23250; semantic-review:SA-20260726-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260726-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260726-BOUNDED-ATTENTION-POOL; semantic-review:SA-20260726-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260726-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-22997; books-review:SF-2026-ARXIV-2607-23250; semantic-review:SA-20260726-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260726-COVERAGE:start -->Fresh-context audit verified the frozen two-family denominator, strict Beijing window [2026-07-25 09:00, 2026-07-26 09:00), exact-v1 ownership and zero identifier overlap against D25 or D27. Artifact accounting matches observed evidence: 2607.22997 discloses external repository locators without an audited event-time commit, while 2607.23250 discloses no implementation artifact. No SRC-GITHUB-COMMIT attribution is present. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260726-COVERAGE:end -->
<!-- semantic-review:SA-20260726-EVIDENCE:start -->Fresh-context audit recomputed both durable exact-v1 snapshot SHA-256 digests and confirmed packet-to-central-to-Daily consistency for identity, timestamp, reviewed version, locators, route, Score V2, artifact boundary, benchmark contract, claim boundary and disposition. The Deep review remains limited to dense causal attention, the disclosed Qwen3 and NVIDIA NVLink/RoCE workload, non-bitwise-equivalent execution and emulated or reimplemented comparison baselines. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260726-EVIDENCE:end -->
<!-- semantic-review:SA-20260726-SELECTION:start -->Fresh-context audit verified one Deep and one Closure route. The Deep Selection denominator contains exactly the sole eligible family, 2607.23250, which is selected into one narrative unit; there are zero eligible non-selections. The Closure family remains outside Selection without losing its completed review or No Change disposition. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260726-SELECTION:end -->
<!-- semantic-review:SA-20260726-BOOKS:start -->Fresh-context audit confirmed the 2607.23250 integration under TRAIN-DISTRIBUTED-TRAINING in Ch36, headed '从等 Token Packing 到有界 Attention Workload Pool', together with its exact-v1 Review note. The passage preserves equal-token packing and Ulysses as the prior valid baseline, identifies quadratic attention-work skew as the changed constraint, assigns optimizer-step membership to the sampler and bounded execution placement to the pool planner, and records communication, planning, metadata, reordering and topology costs, exposed overlap boundaries, failure and restart semantics, coexistence conditions and evidence limitations. The 2607.22997 No Change decision remains consistent and does not create a duplicate owner. Books PASS; finding_count=0.<!-- semantic-review:SA-20260726-BOOKS:end -->

## 8. Ignored Noise

447 个窗口内 identity 中，445 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：1 个 `Integrate`，1 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 1 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/26/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/36-distributed-training.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Real2Sim2Real for Vision-Language-Action Manipulation: An AMD ROCm-Based Pipeline](https://arxiv.org/abs/2607.22997v1) — first-public（Asia/Shanghai）：2026-07-25；accessed：2026-08-27
- [Libra: Taming Attention Workload Skew in Long-Context LLM Training with Bounded Sequence Pool](https://arxiv.org/abs/2607.23250v1) — first-public（Asia/Shanghai）：2026-07-25；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
