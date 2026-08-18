# Daily Research — 2026-08-01

**Research Date:** 2026-08-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-31 09:00:00 ～ 2026-08-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-07-31 09:00:00` 至 `2026-08-01 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 460 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 9 个候选：3 个 Deep Review、6 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-KV-CACHE` 中由《Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems》暴露的状态/证据边界；`PLATFORM-SECURITY` 中由《GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG》暴露的状态/证据边界；`PLATFORM-SECURITY` 中由《CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-01 |
| Window End | 2026-08-01 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-01-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-31T09:00:00+08:00 | 2026-08-01T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 460 | SF-2026-ARXIV-2607-29019<br>SF-2026-ARXIV-2607-29069<br>SF-2026-ARXIV-2607-29076<br>SF-2026-ARXIV-2608-11235<br>SF-2026-ARXIV-2607-29190<br>SF-2026-ARXIV-2607-29397<br>SF-2026-ARXIV-2607-29575<br>SF-2026-ARXIV-2607-29591<br>SF-2026-ARXIV-2607-29678 | page count=7 snapshot files; final_cursor=end; daily-window total=460; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-01T09:00:00+08:00 | coverage:SRC-ARXIV:20260801 | — |

<!-- coverage:SRC-ARXIV:20260801:start -->submittedDate query filtered to [2026-07-31T09:00:00+08:00, 2026-08-01T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 9 routed families.<!-- coverage:SRC-ARXIV:20260801:end -->

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
| SF-2026-ARXIV-2607-29019 | arXiv:2607.29019v1 | paper-v1:2607.29019 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-29019 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-29019 | yes |
| SF-2026-ARXIV-2607-29069 | arXiv:2607.29069v1 | paper-v1:2607.29069 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 1 | 3 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-29069 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-29076 | arXiv:2607.29076v1 | paper-v1:2607.29076 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-29076 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-29076 | yes |
| SF-2026-ARXIV-2608-11235 | arXiv:2608.11235v1 | paper-v1:2608.11235 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11235 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-29190 | arXiv:2607.29190v1 | paper-v1:2607.29190 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-29190 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-29190 | yes |
| SF-2026-ARXIV-2607-29397 | arXiv:2607.29397v1 | paper-v1:2607.29397 | 2026-W31 | 2026-07-31 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-29397 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-29575 | arXiv:2607.29575v1 | paper-v1:2607.29575 | 2026-W31 | 2026-08-01 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-29575 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-29591 | arXiv:2607.29591v1 | paper-v1:2607.29591 | 2026-W31 | 2026-08-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-29591 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2607-29678 | arXiv:2607.29678v1 | paper-v1:2607.29678 | 2026-W31 | 2026-08-01 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-29678 | self | — | new_in_window | MODEL-TOKENIZER | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-29019 | RP-30ea3293b472ab5e | deep | arXiv:2607.29019v1 | SRC-ARXIV@arXiv:2607.29019v1 | https://arxiv.org/html/2607.29019v1 (§4 Method: threshold selection, mask polarization and secure token extraction) | https://arxiv.org/html/2607.29019v1 (§6 Experiments: setup, main results, latency and scaling) | https://arxiv.org/html/2607.29019v1 (§5.2 Security Analysis: security assumptions and Limitations) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2607-29019 | complete |
| SF-2026-ARXIV-2607-29069 | RP-73b80a1f6ad995e8 | standard | arXiv:2607.29069v1 | SRC-ARXIV@arXiv:2607.29069v1 | https://arxiv.org/html/2607.29069v1#S3 (3. Aries: Trajectory-Level Telemetry) | https://arxiv.org/html/2607.29069v1#S4 (4. Why Is Modern Cloud AI Infrastructure a Poor Fit for Agents?) | https://arxiv.org/html/2607.29069v1#S5 (5. Future Research Directions) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2607-29069 | complete |
| SF-2026-ARXIV-2607-29076 | RP-db8e08e9f86a2989 | deep | arXiv:2607.29076v1 | SRC-ARXIV@arXiv:2607.29076v1 | https://arxiv.org/html/2607.29076v1 (Methodology: token vulnerability, Guard-of-Sink partitioning and tile scheduling) | https://arxiv.org/html/2607.29076v1 (Experiments: setup, results and row-utilization measurements) | https://arxiv.org/html/2607.29076v1 (Experiments / Scope and Limitations) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2607-29076 | complete |
| SF-2026-ARXIV-2608-11235 | RP-572cf1aef66da0a6 | standard | arXiv:2608.11235v1 | SRC-ARXIV@arXiv:2608.11235v1 | https://arxiv.org/html/2608.11235v1#S3 (3 Method) | https://arxiv.org/html/2608.11235v1#S4 (4 Experiments) | https://arxiv.org/html/2608.11235v1#S5 (5 Conclusion, Limitations, and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11235 | complete |
| SF-2026-ARXIV-2607-29190 | RP-e39b0dd4a91fe060 | deep | arXiv:2607.29190v1 | SRC-ARXIV@arXiv:2607.29190v1 | https://arxiv.org/html/2607.29190v1 (§5 Method: certification backends and guarantees) | https://arxiv.org/html/2607.29190v1 (§6 Experiments plus Appendices D–E: setup, soundness and external-validity tables) | https://arxiv.org/html/2607.29190v1 (§7 Discussion, Scope, and Limitations) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2607-29190 | complete |
| SF-2026-ARXIV-2607-29397 | RP-12d7c2be26727421 | standard | arXiv:2607.29397v1 | SRC-ARXIV@arXiv:2607.29397v1 | https://arxiv.org/html/2607.29397v1#S3 (3 Methods) | https://arxiv.org/html/2607.29397v1#S4 (4 Results) | https://arxiv.org/html/2607.29397v1#S6 (6 Limitations and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2607-29397 | complete |
| SF-2026-ARXIV-2607-29575 | RP-c7a4615d09a2ef9b | standard | arXiv:2607.29575v1 | SRC-ARXIV@arXiv:2607.29575v1 | https://arxiv.org/html/2607.29575v1#S4 (IV Methodology) | https://arxiv.org/html/2607.29575v1#S5 (V Performance Analysis) | https://arxiv.org/html/2607.29575v1#S8 (VIII Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2607-29575 | complete |
| SF-2026-ARXIV-2607-29591 | RP-7e2f8f1b233f335a | standard | arXiv:2607.29591v1 | SRC-ARXIV@arXiv:2607.29591v1 | https://arxiv.org/html/2607.29591v1#Sx5.SSx1 (Overview) | https://arxiv.org/html/2607.29591v1#Sx6 (Experiments) | https://arxiv.org/html/2607.29591v1#Sx7 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2607-29591 | complete |
| SF-2026-ARXIV-2607-29678 | RP-1c7466cb55b85f83 | standard | arXiv:2607.29678v1 | SRC-ARXIV@arXiv:2607.29678v1 | https://arxiv.org/html/2607.29678v1#S3 (3. System Design) | https://arxiv.org/html/2607.29678v1#S5 (5. Evaluation) | https://arxiv.org/html/2607.29678v1#S7 (7. Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2607-29678 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-29019:start -->
#### GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG

<!-- claim:SF-2026-ARXIV-2607-29019:start -->GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。<!-- claim:SF-2026-ARXIV-2607-29019:end -->

GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。 直接在密文域做同态 Top-k，在候选规模可控、允许较高交互/算术成本时仍是可审计基线；当 threshold 集合扩大、响应延迟与密文运算成为主约束时，论文把控制点移到 mask polarization 与 secure token extraction。代价是安全结论依赖 plaintext-corpus threat model、CKKS 数值精度和阈值选择，集合规模或近似误差漂移都可能破坏收益与正确性边界。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29019:end -->

<!-- review:SF-2026-ARXIV-2607-29069:start -->
#### Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework

<!-- claim:SF-2026-ARXIV-2607-29069:start -->《Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework》把 `INFER-SCHEDULING` 的问题具体化为：重复推理、持久 context 与 sandbox tool execution 使 request 不再是单一 prefill/decode 生命周期。其机制是把 task semantics 与 execution configuration 分离，并用跨组件 trajectory、相关 telemetry 与统一 sandbox 接口刻画 agent serving；primary v1 的 evaluation 绑定为开放 agent harness/benchmark 的可复现实验，并以商业平台 production trace 补充 token、context 与 sandbox 行为，比较对象为以 token throughput/latency 为中心的普通 LLM serving 与 snapshot 式 sandbox 管理。<!-- claim:SF-2026-ARXIV-2607-29069:end -->

证据支持的范围是：agent workload 的非推理瓶颈、context 收益递减和 sandbox burst/idle 状态需要进入 serving contract；不支持的外推是：Aries 已证明某个通用 agent-native 架构、所有 sandbox 都应激进 suspend，或商业 trace 可代表其他平台。旧方案仍有成立条件：短生命周期、无工具或 sandbox 成本可忽略的模型服务；此时 token-centric contract 仍可解释主成本。新机制获得的收益与代价必须一起读取：trajectory 级可观测性和弹性管理换来跨组件关联、持久状态与安全面治理成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：trace 偏差、benchmark 与生产任务不一致、sandbox snapshot 恢复昂贵及 attack surface 扩张。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 3 / Durability 1 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29069:end -->

<!-- review:SF-2026-ARXIV-2607-29076:start -->
#### Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems

<!-- claim:SF-2026-ARXIV-2607-29076:start -->论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。<!-- claim:SF-2026-ARXIV-2607-29076:end -->

论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。 对所有存内计算行一律提供数字保护，在 analog-noise 分布稳定且数字预算充足时最直接；当保护开销压低 tile 利用率时，Guard-of-Sink 先预测 token vulnerability，再只保护高风险行并重排 tile。它以 predictor 与 noise-model 的校准负担换数字保护预算和行利用率，分布漂移、漏保或保护集合膨胀会重新暴露准确率与吞吐折中。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了context-conditioned KV state的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、带宽、精度与恢复为长期设计约束。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29076:end -->

<!-- review:SF-2026-ARXIV-2608-11235:start -->
#### CORA-Diff: Confidence-Oriented Residual Acceptance for Efficient Diffusion Language Model Inference

<!-- claim:SF-2026-ARXIV-2608-11235:start -->《CORA-Diff: Confidence-Oriented Residual Acceptance for Efficient Diffusion Language Model Inference》把 `MULTIMODAL-GENERATIVE-PARADIGMS` 的问题具体化为：并行 diffusion decoding 中许多位置早已稳定，但 block 因少数 residual token 继续执行。其机制是保持原始 transfer rule，仅对仍未决 residual position 用 native confidence 与跨步 persistence gating；accepted token 继续作为 context，全部 resolved 后提前终止 block；primary v1 的 evaluation 绑定为独立 GSM8K calibration 后冻结 operating point，在 Learn2PD-style LLaDA 的八个 task-length setting、GSM8K/HumanEval、fixed-horizon isolation 与 Dream transfer 上测 runtime/score，比较对象为所有位置按固定 denoising horizon 重复 dense forward，或用 learned filter/modified score/cache mechanism 提前接受。<!-- claim:SF-2026-ARXIV-2608-11235:end -->

证据支持的范围是：在冻结 operating point 和作者匹配协议中，native confidence/persistence 可减少 residual denoising，并将所测 score 变化限制在报告范围内；不支持的外推是：confidence 等于 correctness、所有 DLM/采样规则无调参迁移，或作者 task score 边界证明 exact equivalence。旧方案仍有成立条件：短 horizon、早期 token 不稳定或 deterministic endpoint 必须严格复算时，dense decoding 更透明。新机制获得的收益与代价必须一起读取：training-free early acceptance 减少重复计算但用 calibration 和错误接受风险换 latency；可见 accepted token 还会影响后续轨迹。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：分布/calibration 漂移、过度自信、persistence 假稳定、非确定性 transfer rule、长度外推或 quality tail。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供生成分解与迭代顺序的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MULTIMODAL-GENERATIVE-PARADIGMS`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11235:end -->

<!-- review:SF-2026-ARXIV-2607-29190:start -->
#### CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

<!-- claim:SF-2026-ARXIV-2607-29190:start -->CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。<!-- claim:SF-2026-ARXIV-2607-29190:end -->

CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。 对单次观测到的 typed return 做点式 allow/deny，在工具返回确定、类型构造可信且扰动不影响策略时最直接；当离散绑定歧义与连续数值误差都可能改变授权结果时，CAGE 枚举绑定邻域，并以 Exact、Lipschitz 或 randomized-smoothing backend 认证整个预算集合。它以 constructor 正确性、邻域枚举和校准预算成本换一次决策的可证明鲁棒性；完整 mediation 之外、预算外逃逸和跨动作累计风险仍不在证书内。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29190:end -->

<!-- review:SF-2026-ARXIV-2607-29397:start -->
#### Studying quantization trade-offs for efficient inference deployment in machine translation

<!-- claim:SF-2026-ARXIV-2607-29397:start -->《Studying quantization trade-offs for efficient inference deployment in machine translation》把 `INFER-TENSORRT-LLM` 的问题具体化为：服务同时受显存、吞吐、延迟与跨段一致性约束。其机制是联合改变权重量化、激活量化与文档切分，并用 WMT24++ 文档级评估暴露分段指标遗漏的退化；primary v1 的 evaluation 绑定为EuroLLM、Hy-MT2；W4A8/W8A8；A100/H100；segment 与 document-level 翻译，比较对象为standard segment-level MT evaluation 与 WMT24++ document evaluation。<!-- claim:SF-2026-ARXIV-2607-29397:end -->

证据支持的范围是：所测模型/精度/硬件中量化收益与文档切分存在耦合；不支持的外推是：某精度、chunk size 或 GPU 对所有翻译模型和文档都最优。旧方案仍有成立条件：逐句/短段评测；请求独立、上下文短时简单且足够。新机制获得的收益与代价必须一起读取：更低显存/更高吞吐换文档质量风险与模型/硬件相关调参。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：模型族、语言、文档长度或 GPU 改变时结论可反转。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29397:end -->

<!-- review:SF-2026-ARXIV-2607-29575:start -->
#### SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving

<!-- claim:SF-2026-ARXIV-2607-29575:start -->《SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving》把 `INFER-SCHEDULING` 的问题具体化为：batch 增益出现部署相关平台期，而更大 batch 继续增加 latency 与显存占用。其机制是以 Transformer compute/memory traffic 的半解析模型预测 latency/throughput，并由 BCA 选择满足 latency 约束的最高吞吐 batch 配置；primary v1 的 evaluation 绑定为对 OPT 系列、不同 batch 与 active-context operating point 做 GPU hardware profiling，并测试未见条件的预测，比较对象为把 decode saturation 粗略归因于 batch/HBM 带宽，或持续放大 batch 以追求吞吐。<!-- claim:SF-2026-ARXIV-2607-29575:end -->

证据支持的范围是：attention decode 的 arithmetic intensity 随 active context 近似恒定，DRAM 饱和先于 compute 饱和；不支持的外推是：对所有模型、kernel、GPU 或 P99/SLO 的无校准通用预测，也不证明避免的显存必然可供其他 workload 使用。旧方案仍有成立条件：低 batch、短 context、compute-bound kernel 或 workload/SLO 固定时，直接 profiling 与静态配置更简单。新机制获得的收益与代价必须一起读取：轻量顾问减少搜索与过度配置，但依赖 kernel/硬件校准，模型漂移后需重建参数。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：attention 实现变化、prefill 占比上升、context 分布漂移或排队/P99 未纳入模型时预测失真。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供请求调度与资源所有权的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29575:end -->

<!-- review:SF-2026-ARXIV-2607-29591:start -->
#### ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression

<!-- claim:SF-2026-ARXIV-2607-29591:start -->《ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression》把 `INFER-KV-CACHE` 的问题具体化为：长上下文压缩后被删 token 的总 attention mass 不再可忽略。其机制是保留主 KV 并用 residual cache 近似被淘汰 token 对 softmax 的聚合贡献，按 layer/head 分配预算并 query gate 恢复；primary v1 的 evaluation 绑定为LongBench、RULER；多 backbone、预算和压缩比；测内存与 decode throughput，比较对象为代表性 KV eviction 与 merging 方法（摘要未列全）。<!-- claim:SF-2026-ARXIV-2607-29591:end -->

证据支持的范围是：固定预算下被淘汰 token 的聚合 attention mass 仍有价值；不支持的外推是：所有模型、任务、预算和线上 SLO 下均优于 eviction/merging。旧方案仍有成立条件：直接 eviction 或 merging；被删质量可忽略或冗余高时仍合理。新机制获得的收益与代价必须一起读取：信息保留换 residual state、预算分配和 query gating 开销。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：proxy/gate 误判、residual 近似失真、极端 attention 或域漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29591:end -->

<!-- review:SF-2026-ARXIV-2607-29678:start -->
#### TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving

<!-- claim:SF-2026-ARXIV-2607-29678:start -->《TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving》把 `MODEL-TOKENIZER` 的问题具体化为：长会话反复追加少量文本且边界附近 tokenization 会变化。其机制是围绕 append 点寻找稳定边界做增量重分词，必要时扩窗或回退；冷路径用 GPU regex+BPE 并 shadow verify；primary v1 的 evaluation 绑定为多种生产 tokenizer、真实文本和 agent-session replay；与 reference 差分；vLLM burst TTFT，比较对象为Hugging Face reference、Gigatoken、已发表 CPU 方法与 stateless front end。<!-- claim:SF-2026-ARXIV-2607-29678:end -->

证据支持的范围是：所测追加式会话可保持 exact token IDs 并减少全量重分词；不支持的外推是：覆盖所有 tokenizer 规范、版本、文本分布或短无状态请求。旧方案仍有成立条件：全量重分词/无状态前端；短 prompt 和低复用时语义直接。新机制获得的收益与代价必须一起读取：更低 TTFT 换 session state、GPU kernel、fallback 和 verifier 复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：无稳定边界、版本不一致、GPU 不可用或 verifier 漏检罕见差异。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-TOKENIZER`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2607-29678:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-29019 | MS MARCO, Natural Questions, HotpotQA and FiQA encrypted retrieval | BGE-base, 384-dimensional normalized embeddings | dual Intel Xeon Silver 4114 CPUs; 251 GB RAM; no GPU | CKKS approximate homomorphic arithmetic | Q=50 queries; B=100/500/1000 candidate documents; document token length T not disclosed | selected documents with fixed-length token reconstruction | one query per encrypted retrieval | Not Disclosed | no production SLO; Recall, Token Accuracy, Document Accuracy and latency reported | paper-defined retrieval metrics |
| SF-2026-ARXIV-2607-29076 | WikiText-2, ARC-Challenge, PIQA, GSM8K and MATH500 under calibrated analog-KV noise | Qwen3, Llama, DeepSeek, OLMo and OLMoE families | full-system accelerator simulated from measurements of hundreds of CIM chips | hybrid higher-precision digital path plus analog CIM bulk path | 2.56K dynamic-KV working set; 8K default sequence; scaling to 512K | next-token inference / task answer | Not Disclosed | Not Disclosed | no production SLO; perplexity, task accuracy, normalized energy and latency reported | standard dataset protocols plus chip-calibrated noise model |
| SF-2026-ARXIV-2607-29190 | typed-return authorization | policy engine and learned gates | Not Disclosed | Not Disclosed | typed low-dimensional returns | single authorization decision | Not Disclosed | Not Disclosed | false-allow and autonomy contract | exact/Lipschitz/randomized-smoothing certificates |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-29190 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260801-2607-29190 | — | 逐 family 排序：override=release_security_contract，V2=8/9 (3/3/2)；保留独立机制、证据边界与 Books Decision；pre-Books delta=point authorization becomes certification over a typed-return uncertainty set | analysis:DA-20260801-2607-29190 |
| SF-2026-ARXIV-2607-29019 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260801-2607-29019 | — | 逐 family 排序：override=release_security_contract，V2=8/9 (3/3/2)；保留独立机制、证据边界与 Books Decision；pre-Books delta=RAG privacy expands from transport protection to query, selection and plaintext-owner trust boundaries | analysis:DA-20260801-2607-29019 |
| SF-2026-ARXIV-2607-29076 | score_7_9<br>potential_books_delta | selected | DA-20260801-2607-29076 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=KV reliability changes from uniform protection to sensitivity-ranked reliability budgets | analysis:DA-20260801-2607-29076 |

<!-- analysis:DA-20260801-2607-29190:start -->
### CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。 对单次观测到的 typed return 做点式 allow/deny，在工具返回确定、类型构造可信且扰动不影响策略时最直接；当离散绑定歧义与连续数值误差都可能改变授权结果时，CAGE 枚举绑定邻域，并以 Exact、Lipschitz 或 randomized-smoothing backend 认证整个预算集合。它以 constructor 正确性、邻域枚举和校准预算成本换一次决策的可证明鲁棒性；完整 mediation 之外、预算外逃逸和跨动作累计风险仍不在证书内。

<!-- analysis:DA-20260801-2607-29190:end -->

<!-- analysis:DA-20260801-2607-29019:start -->
### GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG

GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。 直接在密文域做同态 Top-k，在候选规模可控、允许较高交互/算术成本时仍是可审计基线；当 threshold 集合扩大、响应延迟与密文运算成为主约束时，论文把控制点移到 mask polarization 与 secure token extraction。代价是安全结论依赖 plaintext-corpus threat model、CKKS 数值精度和阈值选择，集合规模或近似误差漂移都可能破坏收益与正确性边界。

<!-- analysis:DA-20260801-2607-29019:end -->

<!-- analysis:DA-20260801-2607-29076:start -->
### Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems

论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。 对所有存内计算行一律提供数字保护，在 analog-noise 分布稳定且数字预算充足时最直接；当保护开销压低 tile 利用率时，Guard-of-Sink 先预测 token vulnerability，再只保护高风险行并重排 tile。它以 predictor 与 noise-model 的校准负担换数字保护预算和行利用率，分布漂移、漏保或保护集合膨胀会重新暴露准确率与吞吐折中。

<!-- analysis:DA-20260801-2607-29076:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-29019 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L602 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2607-29019 | delta:SF-2026-ARXIV-2607-29019 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607-29019 |
| SF-2026-ARXIV-2607-29076 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L385 | books/part-02-model/19-kv-cache.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2607-29076 | delta:SF-2026-ARXIV-2607-29076 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-29076 |
| SF-2026-ARXIV-2607-29190 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L353 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2607-29190 | delta:SF-2026-ARXIV-2607-29190 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-29190 |

<!-- books-review:SF-2026-ARXIV-2607-29019:start --><!-- existing:SF-2026-ARXIV-2607-29019:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2607-29019:end --><!-- delta:SF-2026-ARXIV-2607-29019:start -->GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。<!-- delta:SF-2026-ARXIV-2607-29019:end -->与上述中心命题相比，这个 family 的新增证据是：GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2607-29019:end -->

<!-- books-review:SF-2026-ARXIV-2607-29076:start --><!-- existing:SF-2026-ARXIV-2607-29076:start -->现有中心命题：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。<!-- existing:SF-2026-ARXIV-2607-29076:end --><!-- delta:SF-2026-ARXIV-2607-29076:start -->论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。<!-- delta:SF-2026-ARXIV-2607-29076:end -->与上述中心命题相比，这个 family 的新增证据是：论文把模拟内存上的噪声风险从统一容错改成选择性保护：先识别对输出更敏感的 KV，再把有限的可靠存储预算用于这些状态。正文以芯片测量校准模拟，并在多类 dense/MoE checkpoint 上评估；它证明的是给定噪声模型下的保护排序，不是完整生产系统。 该 delta 已落在《第45章 为什么 KV Cache 能提速》的正文机制锚点；语义相邻边界为 MODEL-KV-CACHE：KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2607-29076:end -->

<!-- books-review:SF-2026-ARXIV-2607-29190:start --><!-- existing:SF-2026-ARXIV-2607-29190:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2607-29190:end --><!-- delta:SF-2026-ARXIV-2607-29190:start -->CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。<!-- delta:SF-2026-ARXIV-2607-29190:end -->与上述中心命题相比，这个 family 的新增证据是：CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2607-29190:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260801-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260801; semantic-review:SA-20260801-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260801-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2607-29019; review:SF-2026-ARXIV-2607-29069; review:SF-2026-ARXIV-2607-29076; review:SF-2026-ARXIV-2608-11235; review:SF-2026-ARXIV-2607-29190; review:SF-2026-ARXIV-2607-29397; review:SF-2026-ARXIV-2607-29575; review:SF-2026-ARXIV-2607-29591; review:SF-2026-ARXIV-2607-29678; semantic-review:SA-20260801-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260801-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260801-2607-29019; analysis:DA-20260801-2607-29076; analysis:DA-20260801-2607-29190; semantic-review:SA-20260801-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260801-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2607-29019; books-review:SF-2026-ARXIV-2607-29076; books-review:SF-2026-ARXIV-2607-29190; review:SF-2026-ARXIV-2607-29069; review:SF-2026-ARXIV-2608-11235; review:SF-2026-ARXIV-2607-29397; review:SF-2026-ARXIV-2607-29575; review:SF-2026-ARXIV-2607-29591; review:SF-2026-ARXIV-2607-29678; semantic-review:SA-20260801-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260801-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260801-COVERAGE:end -->
<!-- semantic-review:SA-20260801-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260801-EVIDENCE:end -->
<!-- semantic-review:SA-20260801-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260801-SELECTION:end -->
<!-- semantic-review:SA-20260801-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260801-BOOKS:end -->

## 8. Ignored Noise

460 条 arXiv v1 中有 451 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：3 个 `Integrate`、0 个 `No Change — Existing Coverage`、6 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/01/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-06-ai-infrastructure/72-security.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving RAG](https://arxiv.org/abs/2607.29019v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework](https://arxiv.org/abs/2607.29069v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems](https://arxiv.org/abs/2607.29076v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [CORA-Diff: Confidence-Oriented Residual Acceptance for Efficient Diffusion Language Model Inference](https://arxiv.org/abs/2608.11235v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents](https://arxiv.org/abs/2607.29190v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [Studying quantization trade-offs for efficient inference deployment in machine translation](https://arxiv.org/abs/2607.29397v1) — published/event date: 2026-07-31; accessed: 2026-08-25
- [SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving](https://arxiv.org/abs/2607.29575v1) — published/event date: 2026-08-01; accessed: 2026-08-25
- [ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression](https://arxiv.org/abs/2607.29591v1) — published/event date: 2026-08-01; accessed: 2026-08-25
- [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678v1) — published/event date: 2026-08-01; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
