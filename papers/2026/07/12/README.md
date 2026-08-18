# Daily Research — 2026-07-12

**Research Date:** 2026-07-12

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-11 09:00:00 ～ 2026-07-12 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 498 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 7 个。当前路由账目为 3 个 Deep、2 个 Standard、2 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-12 |
| Window End | 2026-07-12 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-12-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-27T00:00:00Z |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-11T09:00:00+08:00 | 2026-07-12T09:00:00+08:00 | 2026-08-27T00:00:00Z | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 498 | SF-2026-ARXIV-2607-10172<br>SF-2026-ARXIV-2607-10180<br>SF-2026-ARXIV-2607-10183<br>SF-2026-ARXIV-2607-10186<br>SF-2026-ARXIV-2607-11942<br>SF-2026-ARXIV-2607-10350<br>SF-2026-ARXIV-2607-10463 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-12T09:00:00+08:00 | coverage:SRC-ARXIV:20260712 | GAP-ARXIV-DIRECT-RESET-20260712 |
| SRC-GITHUB-COMMIT | 2026-07-11T09:00:00+08:00 | 2026-07-12T09:00:00+08:00 | 2026-08-27T00:00:00Z | exact GitHub commit API lookups: https://github.com/NVIDIA/kvpress@6d965557a5b9f0201a2301b23c454473dd681d0d | checked | 1 | SF-2026-ARXIV-2607-11942 | pages=1; final cursors=6d965557a5b9f0201a2301b23c454473dd681d0d; one bounded commit lookup per family | 2026-07-12T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260712 | — |

<!-- coverage:SRC-ARXIV:20260712:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 498 unique identities in this strict window; 7 routed families.<!-- coverage:SRC-ARXIV:20260712:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260712:start -->repository=https://github.com/NVIDIA/kvpress, until=v0.5.4, full_sha=6d965557a5b9f0201a2301b23c454473dd681d0d, commit_timestamp=2026-07-02T10:13:48Z, url=https://github.com/NVIDIA/kvpress/commit/6d965557a5b9f0201a2301b23c454473dd681d0d; each commit establishes only the event-time public tree and does not independently prove paper claims.<!-- coverage:SRC-GITHUB-COMMIT:20260712:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 7 个 family：exact v1 为 2 个 family 披露 artifact/evidence locator，其中 2 个提供外部 repository/project/demo locator，另有 5 个未披露；本日确认 1 个 family、1 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10172 | arXiv:2607.10172v1 | paper-v1:2607.10172 | 2026-W28 | 2026-07-11 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-10172 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-10180 | arXiv:2607.10180v1 | paper-v1:2607.10180 | 2026-W28 | 2026-07-11 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-10180 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-10183 | arXiv:2607.10183v1 | paper-v1:2607.10183 | 2026-W28 | 2026-07-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10183 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-10183 | yes |
| SF-2026-ARXIV-2607-10186 | arXiv:2607.10186v1 | paper-v1:2607.10186 | 2026-W28 | 2026-07-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10186 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2607-10186 | yes |
| SF-2026-ARXIV-2607-11942 | arXiv:2607.11942v1 | paper-v1:2607.11942 | 2026-W28 | 2026-07-11 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11942 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-11942 | yes |
| SF-2026-ARXIV-2607-10350 | arXiv:2607.10350v1 | paper-v1:2607.10350 | 2026-W28 | 2026-07-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10350 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-10350 | yes |
| SF-2026-ARXIV-2607-10463 | arXiv:2607.10463v1 | paper-v1:2607.10463 | 2026-W28 | 2026-07-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10463 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-10463 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10172 | RP-569bd4ffe8bf07ab | closure | doi:10.48550/arxiv.2607.10172@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.10172@v1 | doi:10.48550/arxiv.2607.10172#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-10172 | complete |
| SF-2026-ARXIV-2607-10180 | RP-84a57856be208ed7 | closure | doi:10.48550/arxiv.2607.10180@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.10180@v1 | doi:10.48550/arxiv.2607.10180#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-10180 | complete |
| SF-2026-ARXIV-2607-10183 | RP-f428406a9a17c560 | deep | arXiv:2607.10183v1 | SRC-ARXIV@arXiv:2607.10183v1 | https://arxiv.org/html/2607.10183v1#S4.SS2.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS2.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS3; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS3; https://arxiv.org/html/2607.10183v1#S4.SS1 | https://arxiv.org/html/2607.10183v1#S5.SS1; https://arxiv.org/html/2607.10183v1#S5.SS2; https://arxiv.org/html/2607.10183v1#S5.SS3; https://arxiv.org/html/2607.10183v1#S5.SS4; https://arxiv.org/html/2607.10183v1#S5.SS5 | https://arxiv.org/html/2607.10183v1#S7 | Not Disclosed — exact v1 provides no source locator for artifact; No author repository is linked in exact v1; llama.cpp and Hugging Face Accelerate are cited dependencies, not ATSInfer provenance | claim:SF-2026-ARXIV-2607-10183 | complete |
| SF-2026-ARXIV-2607-10186 | RP-ba9e9b328c0fe161 | deep | arXiv:2607.10186v1 | SRC-ARXIV@arXiv:2607.10186v1 | https://arxiv.org/html/2607.10186v1#S4; https://arxiv.org/html/2607.10186v1#S5.SS1; https://arxiv.org/html/2607.10186v1#S5.SS2; https://arxiv.org/html/2607.10186v1#S6.SS1; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS1; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS2; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS3 | https://arxiv.org/html/2607.10186v1#S7.SS1; https://arxiv.org/html/2607.10186v1#S7.SS2; https://arxiv.org/html/2607.10186v1#S7.SS3; https://arxiv.org/html/2607.10186v1#S7.SS4; https://arxiv.org/html/2607.10186v1#S7.SS5; https://arxiv.org/html/2607.10186v1#S7.SS6 | https://arxiv.org/html/2607.10186v1#S9 | Not Disclosed — exact v1 provides no source locator for artifact; No FlashAccel implementation or simulator repository linked in exact v1; cited GitHub pages are dependency/background sources | claim:SF-2026-ARXIV-2607-10186 | complete |
| SF-2026-ARXIV-2607-11942 | RP-193b95cfdd4af65e | deep | arXiv:2607.11942v1 | SRC-ARXIV@arXiv:2607.11942v1; SRC-GITHUB-COMMIT@commit:6d965557a5b9f0201a2301b23c454473dd681d0d | https://arxiv.org/html/2607.11942v1#S3.SS1; https://arxiv.org/html/2607.11942v1#S3.SS2; https://arxiv.org/html/2607.11942v1#S3.SS3; https://arxiv.org/html/2607.11942v1#S3.SS4; https://arxiv.org/html/2607.11942v1#S5 | https://arxiv.org/html/2607.11942v1#S4.SS2; https://arxiv.org/html/2607.11942v1#S6.SS1; https://arxiv.org/html/2607.11942v1#S6.SS2; https://arxiv.org/html/2607.11942v1#S6.SS3; https://arxiv.org/html/2607.11942v1#A1 | https://arxiv.org/html/2607.11942v1#S7 | https://github.com/NVIDIA/kvpress (audited upstream implementation, version 0.5.4); no immutable author harness/records locator is linked in exact v1 HTML | claim:SF-2026-ARXIV-2607-11942 | complete |
| SF-2026-ARXIV-2607-10350 | RP-aec91ed916f810f4 | standard | arXiv:2607.10350v1 | SRC-ARXIV@arXiv:2607.10350v1 | https://arxiv.org/html/2607.10350v1#S2.SS1; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS1; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS2; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS3; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS4; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS1; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS2; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS3; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS4; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS5; https://arxiv.org/html/2607.10350v1#S4 | https://arxiv.org/html/2607.10350v1#S3.SS2; https://arxiv.org/html/2607.10350v1#S3.SS3; https://arxiv.org/html/2607.10350v1#S5.SS1; https://arxiv.org/html/2607.10350v1#S5.SS2 | https://arxiv.org/html/2607.10350v1#S6 | https://amap-cvlab.github.io/ABot-AgentOS (author project page; v1 states complete benchmark release is future work and private data/production results are not released) | claim:SF-2026-ARXIV-2607-10350 | complete |
| SF-2026-ARXIV-2607-10463 | RP-8c52a51b40675cbb | standard | arXiv:2607.10463v1 | SRC-ARXIV@arXiv:2607.10463v1 | https://arxiv.org/html/2607.10463v1#S3.SS1; https://arxiv.org/html/2607.10463v1#S3.SS2; https://arxiv.org/html/2607.10463v1#S3.SS3; https://arxiv.org/html/2607.10463v1#S3.SS4; https://arxiv.org/html/2607.10463v1#A3 | https://arxiv.org/html/2607.10463v1#S4.SS1; https://arxiv.org/html/2607.10463v1#S4.SS2; https://arxiv.org/html/2607.10463v1#S4.SS3; https://arxiv.org/html/2607.10463v1#S4.SS4; https://arxiv.org/html/2607.10463v1#S5.SS1; https://arxiv.org/html/2607.10463v1#S5.SS2; https://arxiv.org/html/2607.10463v1#S5.SS3 | https://arxiv.org/html/2607.10463v1#Sx1 | Not Disclosed — exact v1 provides no source locator for artifact; No author repository/checkpoint linked in exact v1; Search-R1 Hugging Face collection is a baseline artifact, not GRASP provenance | claim:SF-2026-ARXIV-2607-10463 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-10172:start -->
#### On the Efficiency of LoRA Fine-Tuning for Vision-Language-Action Models in Industrial Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-10172:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-10172:end -->

- Identity：`arXiv:2607.10172v1`；first-public（Asia/Shanghai）：`2026-07-11`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-10172:end -->

<!-- review:SF-2026-ARXIV-2607-10180:start -->
#### ActiveFly-Bench: Aligning Embodied Question Answering with Vision-Language-Action for Aerial Embodied Perception

<!-- claim:SF-2026-ARXIV-2607-10180:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与 contextual scope；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-10180:end -->

- Identity：`arXiv:2607.10180v1`；first-public（Asia/Shanghai）：`2026-07-11`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Weekly Only — Context`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-10180:end -->

<!-- review:SF-2026-ARXIV-2607-10183:start -->
#### Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices

<!-- claim:SF-2026-ARXIV-2607-10183:start -->Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10183:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10183v1#S4.SS2.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS2.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS3.SSS3; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS1; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS2; https://arxiv.org/html/2607.10183v1#S4.SS4.SSS3; https://arxiv.org/html/2607.10183v1#S4.SS1`；Evaluation：`https://arxiv.org/html/2607.10183v1#S5.SS1; https://arxiv.org/html/2607.10183v1#S5.SS2; https://arxiv.org/html/2607.10183v1#S5.SS3; https://arxiv.org/html/2607.10183v1#S5.SS4; https://arxiv.org/html/2607.10183v1#S5.SS5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10183v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10183:end -->

<!-- review:SF-2026-ARXIV-2607-10186:start -->
#### FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference

<!-- claim:SF-2026-ARXIV-2607-10186:start -->Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10186:end -->

**旧方案与约束变化。** `本章的核心判断是：**GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。**任何调度和加速机制最终都必须满足这个物理约束。`（`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints. 它改变 `INFER-GPU-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10186v1#S4; https://arxiv.org/html/2607.10186v1#S5.SS1; https://arxiv.org/html/2607.10186v1#S5.SS2; https://arxiv.org/html/2607.10186v1#S6.SS1; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS1; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS2; https://arxiv.org/html/2607.10186v1#S6.SS2.SSS3`；Evaluation：`https://arxiv.org/html/2607.10186v1#S7.SS1; https://arxiv.org/html/2607.10186v1#S7.SS2; https://arxiv.org/html/2607.10186v1#S7.SS3; https://arxiv.org/html/2607.10186v1#S7.SS4; https://arxiv.org/html/2607.10186v1#S7.SS5; https://arxiv.org/html/2607.10186v1#S7.SS6`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10186v1#S9`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-GPU-MEMORY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-10186:end -->

<!-- review:SF-2026-ARXIV-2607-11942:start -->
#### How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit

<!-- claim:SF-2026-ARXIV-2607-11942:start -->Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-11942:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.11942v1#S3.SS1; https://arxiv.org/html/2607.11942v1#S3.SS2; https://arxiv.org/html/2607.11942v1#S3.SS3; https://arxiv.org/html/2607.11942v1#S3.SS4; https://arxiv.org/html/2607.11942v1#S5`；Evaluation：`https://arxiv.org/html/2607.11942v1#S4.SS2; https://arxiv.org/html/2607.11942v1#S6.SS1; https://arxiv.org/html/2607.11942v1#S6.SS2; https://arxiv.org/html/2607.11942v1#S6.SS3; https://arxiv.org/html/2607.11942v1#A1`；Limitations/Counterevidence：`https://arxiv.org/html/2607.11942v1#S7`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-11942:end -->

<!-- review:SF-2026-ARXIV-2607-10350:start -->
#### ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory

<!-- claim:SF-2026-ARXIV-2607-10350:start -->Insert a deliberative harness above low-level controllers; isolate skill contexts; maintain structured task state; verify stage and terminal conditions; store multimodal observations/traces as typed provenance-bound graph memory; diagnose failures after evaluation and promote derived evo-assets only to later splits. Edge/cloud separation attempts to keep private memory local while sharing common knowledge. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10350:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Insert a deliberative harness above low-level controllers; isolate skill contexts; maintain structured task state; verify stage and terminal conditions; store multimodal observations/traces as typed provenance-bound graph memory; diagnose failures after evaluation and promote derived evo-assets only to later splits. Edge/cloud separation attempts to keep private memory local while sharing common knowledge. 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10350v1#S2.SS1; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS1; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS2; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS3; https://arxiv.org/html/2607.10350v1#S2.SS2.SSS4; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS1; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS2; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS3; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS4; https://arxiv.org/html/2607.10350v1#S2.SS3.SSS5; https://arxiv.org/html/2607.10350v1#S4`；Evaluation：`https://arxiv.org/html/2607.10350v1#S3.SS2; https://arxiv.org/html/2607.10350v1#S3.SS3; https://arxiv.org/html/2607.10350v1#S5.SS1; https://arxiv.org/html/2607.10350v1#S5.SS2`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10350v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L754-L765`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-10350:end -->

<!-- review:SF-2026-ARXIV-2607-10463:start -->
#### GRASP: GRanularity-Aware Search Policy for Agentic RAG

<!-- claim:SF-2026-ARXIV-2607-10463:start -->Expose semantic-search, keyword-search and read-parent-paragraph actions. Return sentence-level hits with parent metadata, let the policy expand a selected clue, and train a GRPO policy with answer, grounded-reading, complementary-search and turn-efficiency rewards. Retrieval observations are masked out of the policy loss; the model learns an explore/exact-match/verify sequence rather than a fixed fusion rule. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-10463:end -->

**旧方案与约束变化。** `本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**`（`books/part-07-agent/76-rag.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Expose semantic-search, keyword-search and read-parent-paragraph actions. Return sentence-level hits with parent metadata, let the policy expand a selected clue, and train a GRPO policy with answer, grounded-reading, complementary-search and turn-efficiency rewards. Retrieval observations are masked out of the policy loss; the model learns an explore/exact-match/verify sequence rather than a fixed fusion rule. 它改变 `AGENT-RAG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.10463v1#S3.SS1; https://arxiv.org/html/2607.10463v1#S3.SS2; https://arxiv.org/html/2607.10463v1#S3.SS3; https://arxiv.org/html/2607.10463v1#S3.SS4; https://arxiv.org/html/2607.10463v1#A3`；Evaluation：`https://arxiv.org/html/2607.10463v1#S4.SS1; https://arxiv.org/html/2607.10463v1#S4.SS2; https://arxiv.org/html/2607.10463v1#S4.SS3; https://arxiv.org/html/2607.10463v1#S4.SS4; https://arxiv.org/html/2607.10463v1#S5.SS1; https://arxiv.org/html/2607.10463v1#S5.SS2; https://arxiv.org/html/2607.10463v1#S5.SS3`；Limitations/Counterevidence：`https://arxiv.org/html/2607.10463v1#Sx1`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L766-L777`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-RAG`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-10463:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10183 | Paper-defined evaluation contract: https://arxiv.org/html/2607.10183v1#S5.SS1; https://arxiv.org/html/2607.10183v1#S5.SS2; https://arxiv.org/html/2607.10183v1#S5.SS3; https://arxiv.org/html/2607.10183v1#S5.SS4; https://arxiv.org/html/2607.10183v1#S5.SS5 | Laptop: GLM-Z1-9B, Qwen3-14B, Qwen3-30B-A3B, GPT-OSS-20B; desktop: Llama3.1-70B, Qwen3-Next-80B-A3B, Qwen3.5-122B-A10B, GPT-OSS-120B | Laptop Intel i7-11800H + RTX 3060 6GB + 32GB DDR4 + PCIe Gen4 x16; desktop Intel i7-11700 + RTX 4090 24GB + 64GB DDR4 + PCIe Gen4 x16 | GLM-Z1-9B FP16; GPT-OSS native MXFP4; remaining models INT4 | Prefill 512-4096 tokens; decode prompt 2048 tokens | Decode 128 tokens; sustained laptop study varies 32-2048 tokens | Batch size 1; common local interactive setting, not multi-tenant serving | Batch size 1; common local interactive setting, not multi-tenant serving | No production tail SLO; throughput, TPOT, GPU SM utilization and effective PCIe bandwidth reported under the paper's setup | Evidence supports the measured consumer platforms and batch-1 models/formats only; it does not prove fleet-wide tail latency, energy, concurrency, portability or correctness under arbitrary background load |
| SF-2026-ARXIV-2607-10186 | Paper-defined evaluation contract: https://arxiv.org/html/2607.10186v1#S7.SS1; https://arxiv.org/html/2607.10186v1#S7.SS2; https://arxiv.org/html/2607.10186v1#S7.SS3; https://arxiv.org/html/2607.10186v1#S7.SS4; https://arxiv.org/html/2607.10186v1#S7.SS5; https://arxiv.org/html/2607.10186v1#S7.SS6 | Qwen3-235B, Qwen3-Coder-480B, Llama3.1-405B and DeepSeek-V3-671B | Modelled DGX-H200 baseline (8 H200, six 141GB HBM3e stacks/GPU as paper config) versus 4/8-GPU CSI/CLI designs with modelled HBF; each HBF stack 192GB Flash, 32MB SRAM, 768GB/s | FP16 except DeepSeek-V3 weights in FP8 | LongProc-derived 8.11K and agentic 15K average input lengths | LongProc-derived 2.53K and agentic 6K average output lengths | Largest simulated batch satisfying capacity and decode-latency constraint; varies by model/configuration | Largest simulated batch satisfying capacity and decode-latency constraint; varies by model/configuration | 50ms and 100ms per decode step (approximately 20 and 10 tokens/s/user as paper states) | All end-to-end gains are simulator/model outputs under assumed HBF characteristics, layouts and SLOs; they are not measurements from fabricated HBF hardware and do not establish endurance, yield, reliability or production tail behavior |
| SF-2026-ARXIV-2607-11942 | Paper-defined evaluation contract: https://arxiv.org/html/2607.11942v1#S4.SS2; https://arxiv.org/html/2607.11942v1#S6.SS1; https://arxiv.org/html/2607.11942v1#S6.SS2; https://arxiv.org/html/2607.11942v1#S6.SS3; https://arxiv.org/html/2607.11942v1#A1 | Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct and DeepSeek-R1-Distill-Qwen-7B; gemma-2-9B quarantined/disqualified for tokenizer-expanded positional overflow | Single rented RTX 3090 48GB | Paper reports backend numerical effects; portable dtype/accumulation contract is not fully disclosed in the headline | RULER nominal 8192 plus LongBench natural-text tasks; tokenizer-expanded length explicitly checked | Task-specific; fixed within matched pairs, not a serving throughput benchmark | Offline paired audit; no production concurrency/SLO | Offline paired audit; no production concurrency/SLO | Not Disclosed | Supports protocol sensitivity for the audited implementations, models, 8K RULER/LongBench and uniform budgets. It does not rank all KV compressors, resolve H2O, validate 32K-128K reuse, or establish the paper's ordinal visibility hypothesis causally |
| SF-2026-ARXIV-2607-10350 | Paper-defined evaluation contract: https://arxiv.org/html/2607.10350v1#S3.SS2; https://arxiv.org/html/2607.10350v1#S3.SS3; https://arxiv.org/html/2607.10350v1#S5.SS1; https://arxiv.org/html/2607.10350v1#S5.SS2 | Agent subset compares Qwen3.6-Plus single controller, Qwen3.6-Plus hierarchical system and DeepSeek-V4-Pro hierarchical system; common Qwen3-VL-Plus observation tool. Memory benchmarks use benchmark-specific GPT-5.4/Qwen3.6-Plus/Qwen3.5-Flash roles | Not disclosed as a reproducible systems benchmark | Not disclosed | Task/benchmark dependent; not disclosed as a common contract | Task/trajectory dependent | Offline agent/memory evaluations; no production concurrency | Offline agent/memory evaluations; no production concurrency | None | Initial validation, not a complete leaderboard or large-scale physical deployment. Base models differ across memory tasks; private production data/results and the full benchmark are not released in v1 |
| SF-2026-ARXIV-2607-10463 | Paper-defined evaluation contract: https://arxiv.org/html/2607.10463v1#S4.SS1; https://arxiv.org/html/2607.10463v1#S4.SS2; https://arxiv.org/html/2607.10463v1#S4.SS3; https://arxiv.org/html/2607.10463v1#S4.SS4; https://arxiv.org/html/2607.10463v1#S5.SS1; https://arxiv.org/html/2607.10463v1#S5.SS2; https://arxiv.org/html/2607.10463v1#S5.SS3 | Qwen2.5-3B-Instruct policy; BM25 lexical retriever; Qwen3-0.6B semantic retriever; Qwen3-Reranker-0.6B in the single-step hybrid baseline; gpt5-mini used for IRCoT trace generation and LLM judge | Full-parameter GRPO training on 2x NVIDIA A100 80GB; retrieval tools isolated on a third GPU node | Not disclosed | Dataset/task dependent; no fixed token length disclosed | Multi-turn tool trajectories; final run stabilizes near eight tool calls/trajectory, but token length not disclosed | Training batch size 64; 270 GRPO steps (~17,280 prompts, ~19% of an epoch). Evaluation samples 500 validation questions/dataset, seed 42 | Training batch size 64; 270 GRPO steps (~17,280 prompts, ~19% of an epoch). Evaluation samples 500 validation questions/dataset, seed 42 | None; retrieval/QA quality rather than online latency | Supports learned tool/granularity coordination on the stated 3B model and annotated multi-hop QA setup. It does not establish scaling, production latency, annotation-free rewards, calibrated stopping or resistance to hostile corpora |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10183 | score_7_9;potential_books_delta | selected | DA-20260712-2607-10183 | — | V2=9/9；Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260712-2607-10183 |
| SF-2026-ARXIV-2607-10186 | score_7_9;potential_books_delta | selected | DA-20260712-2607-10186 | — | V2=9/9；Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260712-2607-10186 |
| SF-2026-ARXIV-2607-11942 | score_7_9;potential_books_delta | selected | DA-20260712-2607-11942 | — | V2=9/9；Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260712-2607-11942 |

<!-- analysis:DA-20260712-2607-10183:start -->
### Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices

**旧方案为何合理。** Layer-level static offload is simple, predictable and amortizes profiling when the machine is dedicated and operator behavior is homogeneous. It becomes wasteful when tensors have different CPU/GPU speedup per byte and when local CPU, GPU or PCIe availability changes while prefill and decode share one device.（现有命题定位：`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）

**约束变化与机制。** Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-TENSORRT-LLM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Tensor granularity improves use of scarce GPU bytes and runtime load feedback avoids a stale plan, but adds profiling, pinned memory, buffer reservation, graph rebuild, dynamic-program and hysteresis policy. Re-scheduling too often costs a material fraction of TPOT; too slowly leaves a stale plan. Thermal drift, unsupported kernels/formats, PCIe contention and inaccurate profiles can erase gains. Static layer placement remains preferable for stable dedicated hosts, small models, strict predictability or insufficient telemetry.

<!-- analysis:DA-20260712-2607-10183:end -->

<!-- analysis:DA-20260712-2607-10186:start -->
### FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference

**旧方案为何合理。** HBM-only residency gives the simplest latency and consistency contract; host/NVMe offload is cheaper and deployable but often exposes a slow transfer boundary. The constraint changes when flash can be integrated at HBM-like aggregate bandwidth and its latency hidden by die-level parallelism, SRAM prefetch and layout-aware scheduling.（现有命题定位：`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）

**约束变化与机制。** Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-GPU-MEMORY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The design exchanges new die/packaging area, SRAM, controller complexity, specialized layouts, simulator uncertainty, endurance/write amplification and heterogeneous fault recovery for much higher resident capacity. Strict SLOs can make lower-bandwidth configurations underperform HBM; hot mutable state may be a poor flash fit. HBM remains appropriate for hot latency-critical state, while conventional host/storage tiers remain preferable when new hardware is unavailable or persistence writes dominate.

<!-- analysis:DA-20260712-2607-10186:end -->

<!-- analysis:DA-20260712-2607-11942:start -->
### How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit

**旧方案为何合理。** Query-aware compression is valid when each request owns a one-shot prompt and query, because the query is available to select relevant KV. It is invalid as evidence for shared/reusable cache compression, whose state must commit before downstream queries arrive. A benchmark label such as 8192 also ceases to be comparable when tokenizer expansion exceeds a model's positional budget.（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Matched deployment protocols improve external validity but can exclude methods incompatible with the common backend or single-pass harness. Trivial baselines prevent false novelty but do not prove the winner is optimal. Backend numerical divergence, tokenizer overflow, OOM refill, lineage similarity and uniform ratios can silently reshape rankings. Query-aware evaluation remains appropriate for nonreusable per-query caches; query-agnostic evaluation is required for reusable caches.

<!-- analysis:DA-20260712-2607-11942:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-10183 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L60 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-10183 | delta:SF-2026-ARXIV-2607-10183 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10183 |
| SF-2026-ARXIV-2607-10186 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L262 | books/part-05-inference-system/53-kserve-llm.md#L14-L14; books/part-05-inference-system/55-pd-disaggregation.md#L14-L14 | existing:SF-2026-ARXIV-2607-10186 | delta:SF-2026-ARXIV-2607-10186 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-10186 |
| SF-2026-ARXIV-2607-11942 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1506 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-11942 | delta:SF-2026-ARXIV-2607-11942 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-11942 |
| SF-2026-ARXIV-2607-10350 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L14-L14 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-10350 | delta:SF-2026-ARXIV-2607-10350 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-10350 |
| SF-2026-ARXIV-2607-10463 | AGENT-RAG | books/part-07-agent/76-rag.md#L14-L14 | books/part-07-agent/75-context.md#L14-L14; books/part-07-agent/77-memory.md#L14-L14 | existing:SF-2026-ARXIV-2607-10463 | delta:SF-2026-ARXIV-2607-10463 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-10463 |

<!-- books-review:SF-2026-ARXIV-2607-10183:start --><!-- existing:SF-2026-ARXIV-2607-10183:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L60` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-10183:end --><!-- delta:SF-2026-ARXIV-2607-10183:start -->新增证据边界：Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L60`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10183:end --><!-- books-review:SF-2026-ARXIV-2607-10183:end -->

<!-- books-review:SF-2026-ARXIV-2607-10186:start --><!-- existing:SF-2026-ARXIV-2607-10186:start -->对读 `books/part-05-inference-system/54-gpu-memory.md#L262` 与相邻章节后，现有命题（`books/part-05-inference-system/54-gpu-memory.md#L14-L14`）为：本章的核心判断是：**GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。**任何调度和加速机制最终都必须满足这个物理约束。<!-- existing:SF-2026-ARXIV-2607-10186:end --><!-- delta:SF-2026-ARXIV-2607-10186:start -->新增证据边界：Co-design an HBF stack and GPU attachment, distribute small SRAM buffers close to flash planes, map weights and KV into layouts that expose plane-level parallelism, prefetch future pages without stalling dependent kernels, and use an HBF-aware storage/programming layer to coordinate persistent and HBM/SRAM state. Capacity permits larger SLO-bounded batches; bandwidth and page latency remain the limiting constraints. 该 delta 已进入 `books/part-05-inference-system/54-gpu-memory.md#L262`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-10186:end --><!-- books-review:SF-2026-ARXIV-2607-10186:end -->

<!-- books-review:SF-2026-ARXIV-2607-11942:start --><!-- existing:SF-2026-ARXIV-2607-11942:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1506` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-11942:end --><!-- delta:SF-2026-ARXIV-2607-11942:start -->新增证据边界：Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1506`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-11942:end --><!-- books-review:SF-2026-ARXIV-2607-11942:end -->

<!-- books-review:SF-2026-ARXIV-2607-10350:start --><!-- existing:SF-2026-ARXIV-2607-10350:start -->对读 `books/part-07-agent/81-workflow.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L14-L14`）为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2607-10350:end --><!-- delta:SF-2026-ARXIV-2607-10350:start -->新增证据边界：Insert a deliberative harness above low-level controllers; isolate skill contexts; maintain structured task state; verify stage and terminal conditions; store multimodal observations/traces as typed provenance-bound graph memory; diagnose failures after evaluation and promote derived evo-assets only to later splits. Edge/cloud separation attempts to keep private memory local while sharing common knowledge. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-10350:end --><!-- books-review:SF-2026-ARXIV-2607-10350:end -->

<!-- books-review:SF-2026-ARXIV-2607-10463:start --><!-- existing:SF-2026-ARXIV-2607-10463:start -->对读 `books/part-07-agent/76-rag.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/76-rag.md#L14-L14`）为：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2607-10463:end --><!-- delta:SF-2026-ARXIV-2607-10463:start -->新增证据边界：Expose semantic-search, keyword-search and read-parent-paragraph actions. Return sentence-level hits with parent metadata, let the policy expand a selected clue, and train a GRPO policy with answer, grounded-reading, complementary-search and turn-efficiency rewards. Retrieval observations are masked out of the policy loss; the model learns an explore/exact-match/verify sequence rather than a fixed fusion rule. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-10463:end --><!-- books-review:SF-2026-ARXIV-2607-10463:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260712-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260712; semantic-review:SA-20260712-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260712-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-10172; review:SF-2026-ARXIV-2607-10180; review:SF-2026-ARXIV-2607-10183; review:SF-2026-ARXIV-2607-10186; review:SF-2026-ARXIV-2607-11942; review:SF-2026-ARXIV-2607-10350; review:SF-2026-ARXIV-2607-10463; semantic-review:SA-20260712-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260712-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260712-2607-10183; analysis:DA-20260712-2607-10186; analysis:DA-20260712-2607-11942; semantic-review:SA-20260712-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260712-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-10183; books-review:SF-2026-ARXIV-2607-10186; books-review:SF-2026-ARXIV-2607-11942; books-review:SF-2026-ARXIV-2607-10350; books-review:SF-2026-ARXIV-2607-10463; review:SF-2026-ARXIV-2607-10180; semantic-review:SA-20260712-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260712-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260712-COVERAGE:end -->
<!-- semantic-review:SA-20260712-EVIDENCE:start -->Fresh-context review reconciled all 7 frozen families: 3 Deep, 2 Standard and 2 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260712-EVIDENCE:end -->
<!-- semantic-review:SA-20260712-SELECTION:start -->Fresh-context review reconciled 3 eligible Deep families: 3 selected and 0 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260712-SELECTION:end -->
<!-- semantic-review:SA-20260712-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 3 个 family 已定位到实际 Books 段落，2 个 family 的 No Change 结论可定位，1 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260712-BOOKS:end -->

## 8. Ignored Noise

498 个窗口内 identity 中，491 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：3 个 `Integrate`，2 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，1 个 `Rejected — Low Durability / Out of Scope`；Deep 3 / Standard 2。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/12/README.md`。
- 本日报长期 delta 已同步至：`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/54-gpu-memory.md`、`books/part-06-ai-infrastructure/66-evaluation-system.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [On the Efficiency of LoRA Fine-Tuning for Vision-Language-Action Models in Industrial Robotic Manipulation](https://arxiv.org/abs/2607.10172v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-26
- [ActiveFly-Bench: Aligning Embodied Question Answering with Vision-Language-Action for Aerial Embodied Perception](https://arxiv.org/abs/2607.10180v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-26
- [Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices](https://arxiv.org/abs/2607.10183v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-27
- [FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference](https://arxiv.org/abs/2607.10186v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-27
- [How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit](https://arxiv.org/abs/2607.11942v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-27
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350v1) — first-public（Asia/Shanghai）：2026-07-11；accessed：2026-08-27
- [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/abs/2607.10463v1) — first-public（Asia/Shanghai）：2026-07-12；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
