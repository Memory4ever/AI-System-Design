# Daily Research — 2026-08-15

**Research Date:** 2026-08-15

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-14 09:00:00 ～ 2026-08-15 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-14 09:00:00` 至 `2026-08-15 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 385 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 8 个候选：1 个 Deep Review、7 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`AGENT-PLATFORM` 中由《P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-15 |
| Window End | 2026-08-15 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-15-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-14T09:00:00+08:00 | 2026-08-15T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 385 | SF-2026-ARXIV-2608-13883<br>SF-2026-ARXIV-2608-14094<br>SF-2026-ARXIV-2608-14191<br>SF-2026-ARXIV-2608-14205<br>SF-2026-ARXIV-2608-14376<br>SF-2026-ARXIV-2608-14380<br>SF-2026-ARXIV-2608-14498<br>SF-2026-ARXIV-2608-14822 | page count=7 snapshot files; final_cursor=end; daily-window total=385; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-15T09:00:00+08:00 | coverage:SRC-ARXIV:20260815 | — |

<!-- coverage:SRC-ARXIV:20260815:start -->submittedDate query filtered to [2026-08-14T09:00:00+08:00, 2026-08-15T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 8 routed families.<!-- coverage:SRC-ARXIV:20260815:end -->

### Coverage Limitations

- arXiv 采用 first-public `published` timestamp；跨分类条目按 ID 去重，revision 不伪装为新 family。
- `docs/RESEARCH_SOURCES.md` 的固定来源注册表于 2026-08-25 生效；依据 Effective Date，不把 19 个机构源和 Hugging Face 反推为此前窗口的 Required Daily，也不伪造历史 `no_hit`。
- 本次用户授权的历史 replay 以可枚举 arXiv 主分母为确定性 Coverage；原始分页、UTC query、SHA-256 与 daily 09:00 分桶保存在月级 snapshot manifest。
- Hugging Face Daily Papers 属于 non-deterministic discovery backstop；历史日期页恢复失败不改变 arXiv v1 的 owner，也不参与 Coverage Gate 算术。
- vLLM、SGLang、Dynamo、KServe、Kubernetes、DeepSpeed 等工程源由完整 Sunday Weekly 负责，不强塞进 Daily。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-13883 | arXiv:2608.13883v1 | paper-v1:2608.13883 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-13883 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14094 | arXiv:2608.14094v1 | paper-v1:2608.14094 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-14094 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2608-14094 | yes |
| SF-2026-ARXIV-2608-14191 | arXiv:2608.14191v1 | paper-v1:2608.14191 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14191 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14205 | arXiv:2608.14205v1 | paper-v1:2608.14205 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14205 | self | — | new_in_window | MODEL-MOE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14376 | arXiv:2608.14376v1 | paper-v1:2608.14376 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14376 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14380 | arXiv:2608.14380v1 | paper-v1:2608.14380 | 2026-W33 | 2026-08-14 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14380 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14498 | arXiv:2608.14498v1 | paper-v1:2608.14498 | 2026-W33 | 2026-08-15 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14498 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-14822 | arXiv:2608.14822v1 | paper-v1:2608.14822 | 2026-W33 | 2026-08-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-14822 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-13883 | RP-de3088fee9030727 | standard | arXiv:2608.13883v1 | SRC-ARXIV@arXiv:2608.13883v1 | https://arxiv.org/html/2608.13883v1#S3.SS1 (3.1–3.2 matched whole-backend protocol) | https://arxiv.org/html/2608.13883v1#S5 (5 Results) | https://arxiv.org/html/2608.13883v1#S6 (6 Discussion and Limitations) | Not Required — v1 exposes a public artifact, but this Standard review relies only on the versioned paper and does not import repository code or an event-time commit | claim:SF-2026-ARXIV-2608-13883 | complete |
| SF-2026-ARXIV-2608-14094 | RP-048c721b5f09c360 | deep | arXiv:2608.14094v1 | SRC-ARXIV@arXiv:2608.14094v1 | https://arxiv.org/html/2608.14094v1 (§§3.1–3.4: decomposition, skill distillation, privacy routing and reconstruction) | https://arxiv.org/html/2608.14094v1 (§§4.1–4.4 and Appendix C: PRISM 160 prompts, four SLMs, GPT-4o and Sonnet-4.6 judges) | https://arxiv.org/html/2608.14094v1 (§5 Limitations and Appendix D pipeline traces) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-14094 | complete |
| SF-2026-ARXIV-2608-14191 | RP-49b8e5b81244a973 | standard | arXiv:2608.14191v1 | SRC-ARXIV@arXiv:2608.14191v1 | https://arxiv.org/html/2608.14191v1#S5 (V AATC: Attention-Aware Bit Allocation via Transform Coding) | https://arxiv.org/html/2608.14191v1#S6 (VI Experiments) | https://arxiv.org/html/2608.14191v1#S7 (VII Limitations and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14191 | complete |
| SF-2026-ARXIV-2608-14205 | RP-a1879aa2a0d435cd | standard | arXiv:2608.14205v1 | SRC-ARXIV@arXiv:2608.14205v1 | https://arxiv.org/html/2608.14205v1#S3 (3 Method) | https://arxiv.org/html/2608.14205v1#S4 (4 Evaluation) | https://arxiv.org/html/2608.14205v1#S6 (6 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14205 | complete |
| SF-2026-ARXIV-2608-14376 | RP-9792d6da8b8c0d2b | standard | arXiv:2608.14376v1 | SRC-ARXIV@arXiv:2608.14376v1 | https://arxiv.org/html/2608.14376v1#S4 (IV Design) | https://arxiv.org/html/2608.14376v1#S5 (V Evaluation) | https://arxiv.org/html/2608.14376v1#S7 (VII Limitations and Design Tradeoffs) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14376 | complete |
| SF-2026-ARXIV-2608-14380 | RP-713da31e3559eef3 | standard | arXiv:2608.14380v1 | SRC-ARXIV@arXiv:2608.14380v1 | https://arxiv.org/html/2608.14380v1#Sx3 (AgentRewind Framework) | https://arxiv.org/html/2608.14380v1#Sx5 (Experiments) | https://arxiv.org/html/2608.14380v1#Sx6 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14380 | complete |
| SF-2026-ARXIV-2608-14498 | RP-01361311a41bcbce | standard | arXiv:2608.14498v1 | SRC-ARXIV@arXiv:2608.14498v1 | https://arxiv.org/html/2608.14498v1#S3 (3. Rollplex Design) | https://arxiv.org/html/2608.14498v1#S4 (4. Evaluation) | https://arxiv.org/html/2608.14498v1#S5 (5. Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14498 | complete |
| SF-2026-ARXIV-2608-14822 | RP-1bf95bc192a9c765 | standard | arXiv:2608.14822v1 | SRC-ARXIV@arXiv:2608.14822v1 | https://arxiv.org/html/2608.14822v1#Sx3 (Methodology) | https://arxiv.org/html/2608.14822v1#Sx4 (Experiments) | https://arxiv.org/html/2608.14822v1#Sx5 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-14822 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-13883:start -->
#### MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends

<!-- claim:SF-2026-ARXIV-2608-13883:start -->《MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends》把 `AGENT-MEMORY` 的问题具体化为：多 session 任务依赖整套 write/retrieve/consolidate/budget/prompt assembly。其机制是在相同 agent/model alias/tasks/scoring 下只替换整套 memory backend 做 matched comparison；primary v1 的 evaluation 绑定为MemoryArena 五域 shared sets；另有 MemoryLake-only 221 queries，不用于 baseline comparison，比较对象为Mem0、vector RAG 与 long-context control。<!-- claim:SF-2026-ARXIV-2608-13883:end -->

证据支持的范围是：共享小样本上 MemoryLake 五域等权 point average 最高且优势 workload-dependent；不支持的外推是：representation 因果优势、cost-matched、统计显著或 benchmark-wide SOTA。旧方案仍有成立条件：post-hoc recall 或 representation-only ablation；更易解释单组件。新机制获得的收益与代价必须一起读取：structured backend 收益与整套 pipeline 成本绑定，不能拆成单因素。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：CI overlap、域内大量零分、alias/backend 漂移或混入独立 run。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-13883:end -->

<!-- review:SF-2026-ARXIV-2608-14094:start -->
#### P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems

<!-- claim:SF-2026-ARXIV-2608-14094:start -->P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。<!-- claim:SF-2026-ARXIV-2608-14094:end -->

P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。 全本地推理保护数据但牺牲云模型质量，直接上云则暴露原始 PII。P2Skill 把 prompt 分解、去标识、路由和重组固化成小模型可执行 skill，只把允许的子任务发云端；它以 skill 维护、detector recall 和 residual leakage 换质量/隐私折中，最小 1.5B 模型的分解失败说明能力门槛不可忽略。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了Agent 运行与治理状态的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以隔离、审计与生命周期为长期设计约束。
- Knowledge owner：`AGENT-PLATFORM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14094:end -->

<!-- review:SF-2026-ARXIV-2608-14191:start -->
#### KV Cache Compression Through the Lens of Transform Coding

<!-- claim:SF-2026-ARXIV-2608-14191:start -->《KV Cache Compression Through the Lens of Transform Coding》把 `INFER-KV-CACHE` 的问题具体化为：量化误差经 attention 的传播权重随 token/channel 不同。其机制是在 white-noise 模型下分解 attention-aware K/V distortion，再用 transform coding 与 reverse water-filling 分配 bits；primary v1 的 evaluation 绑定为Llama-3.1-8B、Qwen2.5-7B；LongBench/RULER/GSM8K/MMLU-Pro/MATH-500，比较对象为uniform/lower-precision KV quantization baselines。<!-- claim:SF-2026-ARXIV-2608-14191:end -->

证据支持的范围是：所测模型/任务在约 5.8x compression 近无损且 baselines 至少某些设置退化；不支持的外推是：white-noise 假设真实、生产 latency/throughput 或无 calibration shift。旧方案仍有成立条件：统一低精度并最小化 KV reconstruction error；实现简单。新机制获得的收益与代价必须一起读取：更好 rate-distortion 换 calibration、transform/bit allocation 与实现复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：相关误差、attention shift、校准集失配或 codec overhead。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14191:end -->

<!-- review:SF-2026-ARXIV-2608-14205:start -->
#### FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction

<!-- claim:SF-2026-ARXIV-2608-14205:start -->《FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction》把 `MODEL-MOE` 的问题具体化为：routing 随 layer/batch 变，离线 placement 不足但前置 compute 可 overlap。其机制是用跨层 hidden similarity 在 router 前预测 workload，attention 阶段提前迁移 experts，并由 cost model 限制 swaps；primary v1 的 evaluation 绑定为多 models/datasets 的 expert-parallel prefill；load ratio 与 end-to-end latency，比较对象为post-router migration 与 offline placement。<!-- claim:SF-2026-ARXIV-2608-14205:end -->

证据支持的范围是：所测 prefill 中可隐藏平均 5.1 experts/layer 的 balancing overhead；不支持的外推是：decode/所有 workload、预测永准或 lossless 表示 bitwise 等价。旧方案仍有成立条件：router 后迁移或离线 placement；稳定 routing 时仍合理。新机制获得的收益与代价必须一起读取：隐藏迁移换 predictor/cost model、额外流量和无效 swap 风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：跨层相关弱、window 短、routing 突变或带宽争用。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供条件计算路由的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-MOE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14205:end -->

<!-- review:SF-2026-ARXIV-2608-14376:start -->
#### CoRun: Padding is Simple and Efficient for Deterministic LLM Inference

<!-- claim:SF-2026-ARXIV-2608-14376:start -->《CoRun: Padding is Simple and Efficient for Deterministic LLM Inference》把 `INFER-SCHEDULING` 的问题具体化为：batch shape 改变浮点 tiling/reduction，固定 seed 仍分叉。其机制是隔离 prefill，把 decode pad 成固定 shape batch，利用 position-invariant kernels/CUDA Graph 保持结果确定；primary v1 的 evaluation 绑定为Qwen/DeepSeek 等架构；determinism、throughput、TTFT、TPOT，比较对象为batch-invariant kernels。<!-- claim:SF-2026-ARXIV-2608-14376:end -->

证据支持的范围是：所测栈中 scheduling/padding 可确定复现且比受限 kernel 更快；不支持的外推是：跨硬件/driver/kernel 版本 bitwise 一致或任意长度无浪费。旧方案仍有成立条件：动态 batching 高效但不确定，或强制 batch-invariant kernel 牺牲优化。新机制获得的收益与代价必须一起读取：允许高效 kernel 换 padding、固定 shape 队列和 prefill 隔离。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：长度长尾、kernel 非 position-invariant、队列饥饿或 graph shape 不足。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供请求调度与资源所有权的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14376:end -->

<!-- review:SF-2026-ARXIV-2608-14380:start -->
#### AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

<!-- claim:SF-2026-ARXIV-2608-14380:start -->《AgentRewind: Recoverable Execution for Long-Horizon LLM Agents》把 `AGENT-WORKFLOW` 的问题具体化为：早期错误同时污染 context 和 environment 并长程传播。其机制是同时 checkpoint agent context 与受控 environment，失败后回早期状态并携带前次信息继续；primary v1 的 evaluation 绑定为MettleBench 长程 engineering assignments；多 tasks/models/strategies/harnesses，比较对象为plan refinement/safety-check prevention families 与 compared baselines。<!-- claim:SF-2026-ARXIV-2608-14380:end -->

证据支持的范围是：所测受控环境中提高 task success 与 checklist progress；不支持的外推是：真实不可逆工具可恢复、自动选对 checkpoint 或副作用已撤销。旧方案仍有成立条件：只预防错误或失败后继续补救；环境简单时成本低。新机制获得的收益与代价必须一起读取：恢复性换 checkpoint storage、环境控制、重执行和副作用治理。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：未纳管外部状态、非幂等动作、世界变化或旧信息再污染。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可恢复 workflow state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-WORKFLOW`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14380:end -->

<!-- review:SF-2026-ARXIV-2608-14498:start -->
#### Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training

<!-- claim:SF-2026-ARXIV-2608-14498:start -->《Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training》把 `TRAIN-DISTRIBUTED-TRAINING` 的问题具体化为：视频/prefix 占阶段大头且 decode 留算力，但共置内存和 TP layout 冲突。其机制是把 response-independent prefix compute 搬入 rollout decode window，并用 phase-aware HBM residency 与跨 TP weight sharing；primary v1 的 evaluation 绑定为Qwen2.5-VL-32B、32×H800、同步 on-policy RL，比较对象为serial colocation 与 phase disaggregation under same GPU budget。<!-- claim:SF-2026-ARXIV-2608-14498:end -->

证据支持的范围是：该 VLM/集群中保持同步 update 语义下加速；不支持的外推是：异步 RL、其他 GPU/model/视频长度、收敛质量或生产稳定。旧方案仍有成立条件：rollout/reference/training 串行或分离并复制 actor；隔离清楚。新机制获得的收益与代价必须一起读取：利用率换跨阶段干扰、lifetime 管理与 tensor 重建。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：prefix 占比小、decode 饱和、layout 不兼容、HBM 不足或 lifetime 误判。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供分布式训练状态的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-DISTRIBUTED-TRAINING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14498:end -->

<!-- review:SF-2026-ARXIV-2608-14822:start -->
#### Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2608-14822:start -->《Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：在线目标/场景/robot state 变化，需保留进度且避免实物试错。其机制是检测偏差后从近期 viable state 合成 observation，让冻结 VLA 想象延续，再最小 realignment 接回轨迹；primary v1 的 evaluation 绑定为多个 simulators/VLA backbones 与 real-world settings；instruction/physical perturbations，比较对象为failure-data/retraining/external corrective-agent families。<!-- claim:SF-2026-ARXIV-2608-14822:end -->

证据支持的范围是：所测干扰中 training-free recovery 提升 success 并减少 physical restorations；不支持的外推是：counterfactual 正确、恢复安全、检测可靠或所有真机 near-nominal。旧方案仍有成立条件：收集 failure data 重训或外部 agent 边试边纠正；证据更直接但成本高。新机制获得的收益与代价必须一起读取：少实物试错换 synthesis/counterfactual planning 与 realignment 复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：漏检、无 viable state、合成不物理、realignment 不可达或 policy 不可恢复。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-14822:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-14094 | PRISM 160-prompt privacy/quality benchmark across four domains | Qwen3.5:2B, Gemma4:e2B, Qwen2.5:1.5B and Llama3.2:3B via Ollama | NVIDIA L4 | Not Disclosed | 160 prompts: 40 each Medical, Banking, Tourism and General Knowledge | maximum 2048 output tokens | one prompt; batch Not Disclosed | Not Disclosed | inference quality, PII leakage and privacy-quality; no production SLO | uniform LDP, selective LDP, cloud/local controls; GPT-4o judge plus Sonnet-4.6 cross-check |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-14094 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260815-2608-14094 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=Agent skill becomes a versioned, authorized and revocable capability supply chain | analysis:DA-20260815-2608-14094 |

<!-- analysis:DA-20260815-2608-14094:start -->
### P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems

P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。 全本地推理保护数据但牺牲云模型质量，直接上云则暴露原始 PII。P2Skill 把 prompt 分解、去标识、路由和重组固化成小模型可执行 skill，只把允许的子任务发云端；它以 skill 维护、detector recall 和 residual leakage 换质量/隐私折中，最小 1.5B 模型的分解失败说明能力门槛不可忽略。

<!-- analysis:DA-20260815-2608-14094:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-14094 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L14<br>books/part-07-agent/84-agent-platform.md#L532 | books/part-07-agent/81-workflow.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L14 | existing:SF-2026-ARXIV-2608-14094 | delta:SF-2026-ARXIV-2608-14094 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2608-14094 |

<!-- books-review:SF-2026-ARXIV-2608-14094:start --><!-- existing:SF-2026-ARXIV-2608-14094:start -->现有中心命题：Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。<!-- existing:SF-2026-ARXIV-2608-14094:end --><!-- delta:SF-2026-ARXIV-2608-14094:start -->P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。<!-- delta:SF-2026-ARXIV-2608-14094:end -->与上述中心命题相比，这个 family 的新增证据是：P2Skill 把云端能力蒸馏为本地 skill，并用受限信息通道降低原始数据外泄。PRISM、四个小模型与 L4 环境支持受限比较，但残余泄漏、质量差距与不同 skill schema 的迁移仍是主要风险。 该 delta 已落在《第84章 Agent Platform》的正文机制锚点；语义相邻边界为 AGENT-WORKFLOW：Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。；PLATFORM-SECURITY：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-14094:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260815-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260815; semantic-review:SA-20260815-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260815-EVIDENCE | fresh-context:contract-adversary | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-13883; review:SF-2026-ARXIV-2608-14094; review:SF-2026-ARXIV-2608-14191; review:SF-2026-ARXIV-2608-14205; review:SF-2026-ARXIV-2608-14376; review:SF-2026-ARXIV-2608-14380; review:SF-2026-ARXIV-2608-14498; review:SF-2026-ARXIV-2608-14822; semantic-review:SA-20260815-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260815-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260815-2608-14094; semantic-review:SA-20260815-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260815-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-14094; review:SF-2026-ARXIV-2608-13883; review:SF-2026-ARXIV-2608-14191; review:SF-2026-ARXIV-2608-14205; review:SF-2026-ARXIV-2608-14376; review:SF-2026-ARXIV-2608-14380; review:SF-2026-ARXIV-2608-14498; review:SF-2026-ARXIV-2608-14822; semantic-review:SA-20260815-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260815-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260815-COVERAGE:end -->
<!-- semantic-review:SA-20260815-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260815-EVIDENCE:end -->
<!-- semantic-review:SA-20260815-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260815-SELECTION:end -->
<!-- semantic-review:SA-20260815-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260815-BOOKS:end -->

## 8. Ignored Noise

385 条 arXiv v1 中有 377 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：1 个 `Integrate`、0 个 `No Change — Existing Coverage`、7 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/15/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-07-agent/84-agent-platform.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends](https://arxiv.org/abs/2608.13883v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems](https://arxiv.org/abs/2608.14094v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [KV Cache Compression Through the Lens of Transform Coding](https://arxiv.org/abs/2608.14191v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction](https://arxiv.org/abs/2608.14205v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [CoRun: Padding is Simple and Efficient for Deterministic LLM Inference](https://arxiv.org/abs/2608.14376v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [AgentRewind: Recoverable Execution for Long-Horizon LLM Agents](https://arxiv.org/abs/2608.14380v1) — published/event date: 2026-08-14; accessed: 2026-08-25
- [Rollplex: Cross-Phase GPU Spatial Sharing for Vision Language Model Post-Training](https://arxiv.org/abs/2608.14498v1) — published/event date: 2026-08-15; accessed: 2026-08-25
- [Imagining Recovery: Inference-Time Counterfactual Realignment for Vision-Language-Action Models](https://arxiv.org/abs/2608.14822v1) — published/event date: 2026-08-15; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
