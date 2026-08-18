# Daily Research — 2026-08-04

**Research Date:** 2026-08-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-03 09:00:00 ～ 2026-08-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-03 09:00:00` 至 `2026-08-04 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 670 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 7 个候选：0 个 Deep Review、7 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-KV-CACHE` 中由《Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression》暴露的状态/证据边界；`INFER-SCHEDULING` 中由《HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving》暴露的状态/证据边界；`INFER-SCHEDULING` 中由《Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-04 |
| Window End | 2026-08-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-04-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-03T09:00:00+08:00 | 2026-08-04T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 670 | SF-2026-ARXIV-2608-01631<br>SF-2026-ARXIV-2608-01651<br>SF-2026-ARXIV-2608-01785<br>SF-2026-ARXIV-2608-01891<br>SF-2026-ARXIV-2608-02508<br>SF-2026-ARXIV-2608-02515<br>SF-2026-ARXIV-2608-02569 | page count=7 snapshot files; final_cursor=end; daily-window total=670; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-04T09:00:00+08:00 | coverage:SRC-ARXIV:20260804 | — |

<!-- coverage:SRC-ARXIV:20260804:start -->submittedDate query filtered to [2026-08-03T09:00:00+08:00, 2026-08-04T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 7 routed families.<!-- coverage:SRC-ARXIV:20260804:end -->

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
| SF-2026-ARXIV-2608-01631 | arXiv:2608.01631v1 | paper-v1:2608.01631 | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-01631 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-01651 | arXiv:2608.01651v1 | paper-v1:2608.01651 | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-01651 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-01785 | arXiv:2608.01785v1 | paper-v1:2608.01785 | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-01785 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-01891 | arXiv:2608.01891v1 | paper-v1:2608.01891 | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-01891 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-02508 | arXiv:2608.02508v1 | paper-v1:2608.02508 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-02508 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-02515 | arXiv:2608.02515v1 | paper-v1:2608.02515 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-02515 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-02569 | arXiv:2608.02569v1 | paper-v1:2608.02569 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-02569 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-01631 | RP-615b2a46ea8bfc03 | standard | arXiv:2608.01631v1 | SRC-ARXIV@arXiv:2608.01631v1 | https://arxiv.org/html/2608.01631v1#S3 (3 Measuring Protocol) | https://arxiv.org/html/2608.01631v1#S4 (4 Experimental Results) | https://arxiv.org/html/2608.01631v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-01631 | complete |
| SF-2026-ARXIV-2608-01651 | RP-5c25bd79d995ffb4 | standard | arXiv:2608.01651v1 | SRC-ARXIV@arXiv:2608.01651v1 | https://arxiv.org/html/2608.01651v1#S3 (III The Bole Architecture) | https://arxiv.org/html/2608.01651v1#S6 (VI Evaluation) | https://arxiv.org/html/2608.01651v1#S8 (VIII Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-01651 | complete |
| SF-2026-ARXIV-2608-01785 | RP-ffdfd6a26ddfdc80 | standard | arXiv:2608.01785v1 | SRC-ARXIV@arXiv:2608.01785v1 | https://arxiv.org/html/2608.01785v1#S5 (5. Implementation) | https://arxiv.org/html/2608.01785v1#S6 (6. Experiments) | https://arxiv.org/html/2608.01785v1#S8 (8. Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-01785 | complete |
| SF-2026-ARXIV-2608-01891 | RP-03526d89cc94ce58 | standard | arXiv:2608.01891v1 | SRC-ARXIV@arXiv:2608.01891v1 | https://arxiv.org/html/2608.01891v1#S4 (IV AFlex Design) | https://arxiv.org/html/2608.01891v1#S6 (VI Evaluation) | https://arxiv.org/html/2608.01891v1#S8 (VIII Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-01891 | complete |
| SF-2026-ARXIV-2608-02508 | RP-8422390c9f28fd3c | standard | arXiv:2608.02508v1 | SRC-ARXIV@arXiv:2608.02508v1 | https://arxiv.org/html/2608.02508v1#S5.SS1 (5.1 Practical Implementation of RoMeRL) | https://arxiv.org/html/2608.02508v1#S6 (6 Experiments) | https://arxiv.org/html/2608.02508v1#S7 (7 Conclusion and Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-02508 | complete |
| SF-2026-ARXIV-2608-02515 | RP-3b8c57689e5936a0 | standard | arXiv:2608.02515v1 | SRC-ARXIV@arXiv:2608.02515v1 | https://arxiv.org/html/2608.02515v1#S3 (3 LiveMem) | https://arxiv.org/html/2608.02515v1#S4 (4 Experiments) | https://arxiv.org/html/2608.02515v1#A5 (Appendix E Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-02515 | complete |
| SF-2026-ARXIV-2608-02569 | RP-ad9fb4df6d108589 | standard | arXiv:2608.02569v1 | SRC-ARXIV@arXiv:2608.02569v1 | https://arxiv.org/html/2608.02569v1#S4 (IV Datacenter Task Compiler); https://arxiv.org/html/2608.02569v1#S5 (V Evolutionary Design Discovery Loop) | https://arxiv.org/html/2608.02569v1#S6 (VI Use-Case Studies) | https://arxiv.org/html/2608.02569v1#S7 (VII Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-02569 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-01631:start -->
#### Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression

<!-- claim:SF-2026-ARXIV-2608-01631:start -->《Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression》把 `INFER-KV-CACHE` 的问题具体化为：部署要求审计或证据可追踪后，cache policy 的 correctness contract 从 answer 扩展为 evidence preservation。其机制是用 fixed-trace replay 固定可见推理内容，分别测 final accuracy、answer-chain consistency 与 perturbation faithfulness，隔离 KV 压缩是否保留证据；primary v1 的 evaluation 绑定为十种 token eviction 和一种 quantization，在三个 reasoning model、数学/科学/临床/长上下文检索任务上比较，比较对象为只用最终答案 accuracy 判断 KV cache compression 是否保持推理能力。<!-- claim:SF-2026-ARXIV-2608-01631:end -->

证据支持的范围是：正确答案与其可见 supporting rationale 可在压缩下以不同速度退化，形成 answer-evidence gap；不支持的外推是：可见 chain 等于模型内部因果过程、量化普遍优于 eviction，或这些离线任务代表生产对话。旧方案仍有成立条件：只关心答案且 trace 可重算、压缩温和或 memory budget 充足时，accuracy-first 评估仍可能够用。新机制获得的收益与代价必须一起读取：多指标评估揭示隐性退化，但增加 replay、perturbation 与 evaluator 设计成本；quantization 也有数值代价。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：rationale 不忠实、task evaluator 偏差、压缩比变化、模型迁移或 trace 本身错误会限制结论。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-01631:end -->

<!-- review:SF-2026-ARXIV-2608-01651:start -->
#### Bole: Efficient Tree Speculation for Hybrid-Attention Language Models

<!-- claim:SF-2026-ARXIV-2608-01651:start -->《Bole: Efficient Tree Speculation for Hybrid-Attention Language Models》把 `INFER-SPECULATIVE-DECODING` 的问题具体化为：树宽和并发扩大后 recurrent state 随分支复制。其机制是为线性注意力推导树状 speculative decoding 的闭式状态更新，以 token-factor 共享状态并只重建选中分支；primary v1 的 evaluation 绑定为多种 hybrid-attention 模型、GPU 和数据集；offline 与 online agent traffic；TTFT/TPOT，比较对象为autoregressive decoding 与 strongest tree-speculative baseline。<!-- claim:SF-2026-ARXIV-2608-01651:end -->

证据支持的范围是：所测混合注意力模型中降低分支状态内存并加速验证；不支持的外推是：覆盖纯 full-attention、任意 recurrent update、任意树形或所有 batch。旧方案仍有成立条件：小树/小 batch 或状态便宜时逐分支物化最直接。新机制获得的收益与代价必须一起读取：更低状态成本换自定义 kernel、因子重建与 budget calibration。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：数值误差、极端树形、runtime 接口变化或预算估计失准。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供proposal/verify/commit 状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SPECULATIVE-DECODING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-01651:end -->

<!-- review:SF-2026-ARXIV-2608-01785:start -->
#### HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving

<!-- claim:SF-2026-ARXIV-2608-01785:start -->《HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving》把 `INFER-SCHEDULING` 的问题具体化为：共享 backbone 后分叉到成本差异大的模态阶段。其机制是按输出类别建立 first-response profile，用 slack admission、shared-stage rotation 和 SM 限制调度；primary v1 的 evaluation 绑定为omni-model GPU workloads；多到达率与 downstream-heavy traffic；逐类 first-response SLO，比较对象为token-progress/input-side scheduler 类方法。<!-- claim:SF-2026-ARXIV-2608-01785:end -->

证据支持的范围是：共享 backbone 加异构输出阶段中改善逐类首响应 SLO；不支持的外推是：适用所有 omni model、多 GPU 拓扑或非平稳流量。旧方案仍有成立条件：模态/阶段同质时 token-progress 调度简单可预测。新机制获得的收益与代价必须一起读取：SLO/利用率换 profiling、slack 预测、公平性与 SM 控制复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：profile 漂移、slack 估错、下游争用或类别饥饿。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供请求调度与资源所有权的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-01785:end -->

<!-- review:SF-2026-ARXIV-2608-01891:start -->
#### Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling

<!-- claim:SF-2026-ARXIV-2608-01891:start -->《Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling》把 `INFER-SCHEDULING` 的问题具体化为：attention/FFN 的算力/带宽敏感性随阶段、batch、负载变化。其机制是解耦 attention/FFN 部署，由全局调度和 operator-level DVFS 协同，并结合 pipeline/microbatch/batch 控制；primary v1 的 evaluation 绑定为SGLang、A800、Qwen3-32B、Mixtral-8x7B 与生产 conversation/coding traces，比较对象为state-of-the-art disaggregated serving 与 frequency-scaling 方法。<!-- claim:SF-2026-ARXIV-2608-01891:end -->

证据支持的范围是：指定 GPU/模型/runtime/trace 中改善能耗-SLO 折中；不支持的外推是：其他 GPU、模型、网络、电价或流量下同样成立。旧方案仍有成立条件：稳定负载下全程高频或请求阶段 DVFS，简单且 SLO 风险低。新机制获得的收益与代价必须一起读取：节能换控制器、通信、pipeline 排程和 SLO 违约风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：性能预测漂移、pipeline bubble、互联开销或突发负载。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供请求调度与资源所有权的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-01891:end -->

<!-- review:SF-2026-ARXIV-2608-02508:start -->
#### RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States

<!-- claim:SF-2026-ARXIV-2608-02508:start -->《RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States》把 `AGENT-MEMORY` 的问题具体化为：自演进 memory 的瓶颈从存储容量转为 feedback credit assignment 与 bounded utility support。其机制是把无限增长的 trajectory-indexed utility 压缩为按 outcome polarity 与 memory dynamics 分解的固定维 task memory state，并以固定 semantic coordinates 更新/替换经验；primary v1 的 evaluation 绑定为ALFWorld 与 LifelongAgentBench 上测 task performance、Cold-Q、feedback density、memory size 和 LLM calls，比较对象为为每条历史轨迹或共检索 memory 单独维护 utility，并把 trajectory reward 联合回填给所有 memory。<!-- claim:SF-2026-ARXIV-2608-02508:end -->

证据支持的范围是：反馈预算固定而历史增长时，utility 稀释和错误 memory 的 reward contamination 会长期累积；不支持的外推是：固定坐标保留所有细粒度因果贡献、理论稳态覆盖真实 agent 分布，或两个 benchmark 的比例可通用。旧方案仍有成立条件：短任务、memory 小或可获得 item-level feedback 时，直接 trajectory-indexed utility 更可解释。新机制获得的收益与代价必须一起读取：反馈更集中且 memory 更小，但替换机制会丢失长尾经验并引入 coordinate transition/聚类偏差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：任务语义漂移、polarity 误判、错误经验占据坐标或联合奖励仍不可分解时出现 memory-reward trap。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-02508:end -->

<!-- review:SF-2026-ARXIV-2608-02515:start -->
#### LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference

<!-- claim:SF-2026-ARXIV-2608-02515:start -->《LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference》把 `AGENT-MEMORY` 的问题具体化为：长运行交互持续越过 context capacity，需要 computation state 的连续性而不只是可检索文本。其机制是在 bounded KV window 外维护独立生命周期的 intrinsic memory state，并通过 turnover update、memory-oriented post-training 与 state-aware serving 使其在原 token 释放后继续承载历史；primary v1 的 evaluation 绑定为LongMemEval 及 evidence-distance 分析，测试证据移出 active context 后能否仅依赖 memory state 回答，比较对象为context retention、summarization 或 retrieval 只在当前窗口中重新注入选中历史。<!-- claim:SF-2026-ARXIV-2608-02515:end -->

证据支持的范围是：在作者 LongMemEval 协议中，原证据离开 active context 后，固定容量 memory state 仍可保留部分可用历史信息；不支持的外推是：memory state 精确保存完整历史、任何 pretrained model 可无成本接入，或 benchmark 结果等于生产长期一致性。旧方案仍有成立条件：历史可稀疏检索、会话可重启或 active context 足够时，RAG/summarization 的可解释性更高。新机制获得的收益与代价必须一起读取：状态 lifetime 从 token window 解耦，获得连续性但需要专门训练、序列化、迁移和 serving ownership。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：state corruption、错误累积、checkpoint/version 不兼容、跨租户泄漏与证据不可追溯。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-02515:end -->

<!-- review:SF-2026-ARXIV-2608-02569:start -->
#### AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies

<!-- claim:SF-2026-ARXIV-2608-02569:start -->《AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies》把 `AGENT-WORKFLOW` 的问题具体化为：搜索从语言候选转为机器可检查 spec 上的组合探索，减少 onboarding 但把正确性依赖转移到 compiler/evaluator。其机制是先把自然语言目标编译为含目标、约束、变量与 evaluation 的可检查 task spec，再用 diffusion、evolution 与 surrogate 联合搜索 control-plane policy；primary v1 的 evaluation 绑定为workload placement、resource scaling、power management 三类任务，对比 expert-engineered policy 与不同搜索/编译设置，比较对象为LLM 直接从 prompt 生成候选 policy，靠人工补约束和逐任务 onboarding。<!-- claim:SF-2026-ARXIV-2608-02569:end -->

证据支持的范围是：datacenter policy 设计空间相互依赖且 hard constraints 不能由语言流畅性保证；不支持的外推是：生成 policy 在未测 workload/故障下安全、formal spec 完整，或三个任务足以证明自治部署。旧方案仍有成立条件：设计空间小、约束稳定或专家已有成熟 controller 时，人工 policy 与传统优化更透明。新机制获得的收益与代价必须一起读取：覆盖率与迁移性换来 surrogate 偏差、仿真成本、spec 维护和最终 release gate 的额外复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：约束漏编译、sim-to-real gap、reward hacking、搜索局部最优或 unsafe candidate 被错误放行。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可恢复 workflow state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-WORKFLOW`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-02569:end -->

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |

<!-- analysis-decision:NO-DEEP:start -->本窗口没有进入 Deep Analysis 的 family；所有标准候选仍完成 Source Review。<!-- analysis-decision:NO-DEEP:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260804-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260804; semantic-review:SA-20260804-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260804-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-01631; review:SF-2026-ARXIV-2608-01651; review:SF-2026-ARXIV-2608-01785; review:SF-2026-ARXIV-2608-01891; review:SF-2026-ARXIV-2608-02508; review:SF-2026-ARXIV-2608-02515; review:SF-2026-ARXIV-2608-02569; semantic-review:SA-20260804-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260804-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis-decision:NO-DEEP; semantic-review:SA-20260804-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260804-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; review:SF-2026-ARXIV-2608-01631; review:SF-2026-ARXIV-2608-01651; review:SF-2026-ARXIV-2608-01785; review:SF-2026-ARXIV-2608-01891; review:SF-2026-ARXIV-2608-02508; review:SF-2026-ARXIV-2608-02515; review:SF-2026-ARXIV-2608-02569; semantic-review:SA-20260804-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260804-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260804-COVERAGE:end -->
<!-- semantic-review:SA-20260804-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260804-EVIDENCE:end -->
<!-- semantic-review:SA-20260804-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260804-SELECTION:end -->
<!-- semantic-review:SA-20260804-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260804-BOOKS:end -->

## 8. Ignored Noise

670 条 arXiv v1 中有 663 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：0 个 `Integrate`、0 个 `No Change — Existing Coverage`、7 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/04/README.md` 的 Coverage applicability 与 Books receipts。
- 本窗口没有新增达到长期知识门槛的机制，Books 正文无变化。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [Does Accuracy Equal Evidence? Reasoning Faithfulness under KV Cache Compression](https://arxiv.org/abs/2608.01631v1) — published/event date: 2026-08-03; accessed: 2026-08-25
- [Bole: Efficient Tree Speculation for Hybrid-Attention Language Models](https://arxiv.org/abs/2608.01651v1) — published/event date: 2026-08-03; accessed: 2026-08-25
- [HorizonServe: Coordinating Request Scheduling with GPU Sharing for Omni-Model Serving](https://arxiv.org/abs/2608.01785v1) — published/event date: 2026-08-03; accessed: 2026-08-25
- [Energy-Efficient LLM Serving via Disaggregated Attention--FFN and Flexible Frequency Scaling](https://arxiv.org/abs/2608.01891v1) — published/event date: 2026-08-03; accessed: 2026-08-25
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving Agent Memory via Reduced-Order Utility States](https://arxiv.org/abs/2608.02508v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference](https://arxiv.org/abs/2608.02515v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [AtumAI: A Principled Framework for Agentic Generation of Datacenter Control-Plane Policies](https://arxiv.org/abs/2608.02569v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
