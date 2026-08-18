# Daily Research — 2026-08-05

**Research Date:** 2026-08-05

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-04 09:00:00 ～ 2026-08-05 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-04 09:00:00` 至 `2026-08-05 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 667 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 11 个候选：3 个 Deep Review、8 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-GPU-MEMORY` 中由《Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention》暴露的状态/证据边界；`INFER-KV-CACHE` 中由《Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms》暴露的状态/证据边界；`PLATFORM-SECURITY` 中由《SafeCommit: Certifying When Memory-Grounded Agents May Safely Act》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-05 |
| Window End | 2026-08-05 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-05-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-04T09:00:00+08:00 | 2026-08-05T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 667 | SF-2026-ARXIV-2608-03335<br>SF-2026-ARXIV-2608-03555<br>SF-2026-ARXIV-2608-03609<br>SF-2026-ARXIV-2608-03676<br>SF-2026-ARXIV-2608-03682<br>SF-2026-ARXIV-2608-03699<br>SF-2026-ARXIV-2608-03741<br>SF-2026-ARXIV-2608-03839<br>SF-2026-ARXIV-2608-04074<br>SF-2026-ARXIV-2608-03994<br>SF-2026-ARXIV-2608-04289 | page count=7 snapshot files; final_cursor=end; daily-window total=667; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-05T09:00:00+08:00 | coverage:SRC-ARXIV:20260805 | — |
| SRC-GITHUB-COMMIT | 2026-08-04T09:00:00+08:00 | 2026-08-05T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-04074: https://api.github.com/repos/Amir-zsh/nova-kv/commits?until=2026-08-04T16:10:59Z&per_page=1<br>SF-2026-ARXIV-2608-04289: https://api.github.com/repos/akewarmayur/SafeCommit/commits?until=2026-08-04T23:44:35Z&per_page=1; per-family event-time recovery | checked | 2 | SF-2026-ARXIV-2608-04074<br>SF-2026-ARXIV-2608-04289 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-05T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260805 | — |

<!-- coverage:SRC-ARXIV:20260805:start -->submittedDate query filtered to [2026-08-04T09:00:00+08:00, 2026-08-05T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 11 routed families.<!-- coverage:SRC-ARXIV:20260805:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260805:start -->GitHub Commit API recovered and froze 2 repository commit(s): SF-2026-ARXIV-2608-04074: repository=Amir-zsh/nova-kv; until=2026-08-04T16:10:59Z; sha=495c4e09fcd400c47cf424d19961fdffa2177bb7; commit_timestamp=2026-08-04T15:35:57Z; commit_url=https://github.com/Amir-zsh/nova-kv/commit/495c4e09fcd400c47cf424d19961fdffa2177bb7 | SF-2026-ARXIV-2608-04289: repository=akewarmayur/SafeCommit; until=2026-08-04T23:44:35Z; sha=146708eba8d6c768544330d20ed98047a3cc73dc; commit_timestamp=2026-08-04T04:28:09Z; commit_url=https://github.com/akewarmayur/SafeCommit/commit/146708eba8d6c768544330d20ed98047a3cc73dc; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260805:end -->

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
| SF-2026-ARXIV-2608-03335 | arXiv:2608.03335v1 | paper-v1:2608.03335 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03335 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03555 | arXiv:2608.03555v1 | paper-v1:2608.03555 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-03555 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2608-03555 | yes |
| SF-2026-ARXIV-2608-03609 | arXiv:2608.03609v1 | paper-v1:2608.03609 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03609 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03676 | arXiv:2608.03676v1 | paper-v1:2608.03676 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03676 | self | — | new_in_window | MODEL-MOE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03682 | arXiv:2608.03682v1 | paper-v1:2608.03682 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03682 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03699 | arXiv:2608.03699v1 | paper-v1:2608.03699 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03699 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03741 | arXiv:2608.03741v1 | paper-v1:2608.03741 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03741 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-03839 | arXiv:2608.03839v1 | paper-v1:2608.03839 | 2026-W32 | 2026-08-04 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03839 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04074 | arXiv:2608.04074v1 | paper-v1:2608.04074 | 2026-W32 | 2026-08-05 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-04074 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2608-04074 | yes |
| SF-2026-ARXIV-2608-03994 | arXiv:2608.03994v1 | paper-v1:2608.03994 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-03994 | self | — | new_in_window | MODEL-POSITION-ENCODING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04289 | arXiv:2608.04289v1 | paper-v1:2608.04289 | 2026-W32 | 2026-08-05 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-04289 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2608-04289 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-03335 | RP-87f95c6a7be48a09 | standard | arXiv:2608.03335v1 | SRC-ARXIV@arXiv:2608.03335v1 | https://arxiv.org/html/2608.03335v1#S3 (3. Methodology) | https://arxiv.org/html/2608.03335v1#S4 (4. Experiments) | https://arxiv.org/html/2608.03335v1#S5 (5. Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03335 | complete |
| SF-2026-ARXIV-2608-03555 | RP-12d8434c67eeec90 | deep | arXiv:2608.03555v1 | SRC-ARXIV@arXiv:2608.03555v1 | https://arxiv.org/html/2608.03555v1 (§III System Design: KARAT device, microbatch scheduling and configuration search) | https://arxiv.org/html/2608.03555v1 (§IV Evaluation: methodology, performance, ablations, area and power) | https://arxiv.org/html/2608.03555v1 (§IV-D–F sensitivity/design-space boundaries; no standalone limitations section) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-03555 | complete |
| SF-2026-ARXIV-2608-03609 | RP-92d1c105acb88386 | standard | arXiv:2608.03609v1 | SRC-ARXIV@arXiv:2608.03609v1 | https://arxiv.org/html/2608.03609v1#Sx3 (Equivariance by Construction) | https://arxiv.org/html/2608.03609v1#Sx2.SSx3 (Case Study: Agent Equivariance) | https://arxiv.org/html/2608.03609v1#Sx5 (Discussion and Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03609 | complete |
| SF-2026-ARXIV-2608-03676 | RP-17f765229f26487f | standard | arXiv:2608.03676v1 | SRC-ARXIV@arXiv:2608.03676v1 | https://arxiv.org/html/2608.03676v1#Sx3 (Method) | https://arxiv.org/html/2608.03676v1#Sx4 (Experiments) | https://arxiv.org/html/2608.03676v1#Sx5 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03676 | complete |
| SF-2026-ARXIV-2608-03682 | RP-ebf907dd5a05f798 | standard | arXiv:2608.03682v1 | SRC-ARXIV@arXiv:2608.03682v1 | https://arxiv.org/html/2608.03682v1#S4 (4 PhyAI Architecture) | https://arxiv.org/html/2608.03682v1#S6.SS2 (6.2 Climbing the Performance Mountain with Kernel Agents) | https://arxiv.org/html/2608.03682v1#S7 (7 Discussion and Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03682 | complete |
| SF-2026-ARXIV-2608-03699 | RP-8f6a3abf102df1d3 | standard | arXiv:2608.03699v1 | SRC-ARXIV@arXiv:2608.03699v1 | https://arxiv.org/html/2608.03699v1#Sx3 (Methodology) | https://arxiv.org/html/2608.03699v1#Sx4 (Experiment) | https://arxiv.org/html/2608.03699v1#Sx5 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03699 | complete |
| SF-2026-ARXIV-2608-03741 | RP-d52261355fe06fb2 | standard | arXiv:2608.03741v1 | SRC-ARXIV@arXiv:2608.03741v1 | https://arxiv.org/html/2608.03741v1#S4 (IV Inference Simulation); https://arxiv.org/html/2608.03741v1#S5 (V HeteroPanacea Search) | https://arxiv.org/html/2608.03741v1#S6 (VI Evaluation) | https://arxiv.org/html/2608.03741v1#S7 (VII Conclusions) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03741 | complete |
| SF-2026-ARXIV-2608-03839 | RP-eac3c4ccede47a7f | standard | arXiv:2608.03839v1 | SRC-ARXIV@arXiv:2608.03839v1 | https://arxiv.org/html/2608.03839v1#S4 (4 Oilbird: semantic source and tree merge) | https://arxiv.org/html/2608.03839v1#S6 (6 Results and Analysis) | https://arxiv.org/html/2608.03839v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03839 | complete |
| SF-2026-ARXIV-2608-04074 | RP-20a9d861f571108f | deep | arXiv:2608.04074v1 | SRC-ARXIV@arXiv:2608.04074v1; SRC-GITHUB-COMMIT@https://github.com/Amir-zsh/nova-kv/commit/495c4e09fcd400c47cf424d19961fdffa2177bb7 | https://arxiv.org/html/2608.04074v1 (§3–4: attention-preserving transforms and KV vector quantization) | https://arxiv.org/html/2608.04074v1 (§5 Experiments plus Appendix B serving/evaluation protocol) | https://arxiv.org/html/2608.04074v1 (Appendices I–K failure cases and chunked-prefill leak; no standalone limitations section) | https://github.com/Amir-zsh/nova-kv/commit/495c4e09fcd400c47cf424d19961fdffa2177bb7 (event-time commit 2026-08-04T15:35:57Z) | claim:SF-2026-ARXIV-2608-04074 | complete |
| SF-2026-ARXIV-2608-03994 | RP-ed857204213e9b56 | standard | arXiv:2608.03994v1 | SRC-ARXIV@arXiv:2608.03994v1 | https://arxiv.org/html/2608.03994v1#S3 (3 Numerical Failure in ALiBi) | https://arxiv.org/html/2608.03994v1#S4 (4 Experiments) | https://arxiv.org/html/2608.03994v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-03994 | complete |
| SF-2026-ARXIV-2608-04289 | RP-91356e3cd5359aea | deep | arXiv:2608.04289v1 | SRC-ARXIV@arXiv:2608.04289v1; SRC-GITHUB-COMMIT@https://github.com/akewarmayur/SafeCommit/commit/146708eba8d6c768544330d20ed98047a3cc73dc | https://arxiv.org/html/2608.04289v1#S2.SS3 (§2.3 conformal action certificate and unsafe-commit guarantee)<br>https://arxiv.org/html/2608.04289v1#S3 (§3 plausible-world controller, certificate gate, probes and fallback) | https://arxiv.org/html/2608.04289v1#S4 (§4 reproducible proof-of-concept protocol, results and ablations) | https://arxiv.org/html/2608.04289v1#S4.SS6 (§4.6 controlled-benchmark scope)<br>https://arxiv.org/html/2608.04289v1#A5 (Appendix E Limitations and Intended Use: exchangeability, safety-map and fixed-support assumptions) | https://github.com/akewarmayur/SafeCommit/commit/146708eba8d6c768544330d20ed98047a3cc73dc (event-time commit 2026-08-04T04:28:09Z) | claim:SF-2026-ARXIV-2608-04289 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-03335:start -->
#### SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference

<!-- claim:SF-2026-ARXIV-2608-03335:start -->《SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference》把 `INFER-TENSORRT-LLM` 的问题具体化为：视频 token 使二次 attention 成瓶颈，通用稀疏执行被索引/不规则性吞噬。其机制是构造 3D 稀疏候选，按 head 选择运行时 scheme，并配低开销索引、block-sparse kernel 与 grouping；primary v1 的 evaluation 绑定为Hunyuan-Video、Wan2.1/2.2；T2V/I2V；kernel、端到端性能和生成质量，比较对象为dense attention 与现有 sparse-attention engines。<!-- claim:SF-2026-ARXIV-2608-03335:end -->

证据支持的范围是：所测 Video DiT 中 head-aware 动态稀疏与专用 kernel 可降成本并维持所测质量；不支持的外推是：改变 diffusion 建模，或覆盖所有视频模型、分辨率、GPU 和质量分布。旧方案仍有成立条件：token 少、pattern 不稳或质量风险高时 dense attention 最可预测。新机制获得的收益与代价必须一起读取：计算节省换 mask 估计、索引、head policy 和 kernel 维护。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：漏选关键 token、估计偏差、稀疏不规则或分布变化。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供编译后的执行计划的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03335:end -->

<!-- review:SF-2026-ARXIV-2608-03555:start -->
#### Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention

<!-- claim:SF-2026-ARXIV-2608-03555:start -->KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。<!-- claim:SF-2026-ARXIV-2608-03555:end -->

KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。 固定把模型层映射到 GPU 或 PNM，并使用静态 microbatch，在模型、互连和负载稳定时仍简单可靠；KARAT 面对 placement、流水线气泡与设备资源耦合后，引入 PNM/GPU 联合映射、microbatch 调度和配置搜索。收益依赖 PNM 性能模型与校准，动态负载触发 rebalancing 时还会受链路、面积/功耗和迁移成本约束。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了多层内存状态的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、传输与重算为长期设计约束。
- Knowledge owner：`INFER-GPU-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03555:end -->

<!-- review:SF-2026-ARXIV-2608-03609:start -->
#### Formal Verification of Agentic Systems over Operational Data

<!-- claim:SF-2026-ARXIV-2608-03609:start -->《Formal Verification of Agentic Systems over Operational Data》把 `PLATFORM-SECURITY` 的问题具体化为：数据随操作序列演化，性质跨时间和全局状态。其机制是用 STEAD 与 FO-CTL 形式化 stateful agent data，证明不可判定性边界，并给出有限域保持条件和 canonical wrapper；primary v1 的 evaluation 绑定为定理与复杂度证明；case-management agent 仅作实例，不是经验 benchmark，比较对象为仅 interface-level constraint/check 的未包装 agent。<!-- claim:SF-2026-ARXIV-2608-03609:end -->

证据支持的范围是：在论文形式模型、有限域和保持条件内可约束系统级性质；不支持的外推是：任意 LLM agent、无限域、外部副作用或概率行为都可验证。旧方案仍有成立条件：无持久状态或单次 I/O 性质时接口检查更轻量。新机制获得的收益与代价必须一起读取：形式保证换有限域/对称性限制、canonicalization 与复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：重命名不保持语义、图同构过高、外部副作用或无限/概率状态。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供授权与安全证据的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03609:end -->

<!-- review:SF-2026-ARXIV-2608-03676:start -->
#### TAOT: Topology-Aware Optimal Transport for Dynamic Expert Replica Placement in MoE Training

<!-- claim:SF-2026-ARXIV-2608-03676:start -->《TAOT: Topology-Aware Optimal Transport for Dynamic Expert Replica Placement in MoE Training》把 `MODEL-MOE` 的问题具体化为：多节点拓扑中，额外 replica 的通信可能超过负载均衡收益。其机制是将 hot-rank overload 与 idle-rank capacity 建模为带拓扑通信矩阵的熵正则 optimal transport，再做整数 replica matching 与 token assignment，并重叠 guest-weight transfer；primary v1 的 evaluation 绑定为MoE training 配置上比较 end-to-end speed、balance quality 与 weighted expert communication cost，比较对象为动态复制 hot expert 只追求 rank load balance，不计跨节点 weight movement。<!-- claim:SF-2026-ARXIV-2608-03676:end -->

证据支持的范围是：作者配置中，显式 topology cost 的 replica schedule 同时改善端到端训练速度、负载质量和 weighted communication cost；不支持的外推是：任意 fabric、routing skew 与模型规模均有相同收益，或 Sinkhorn flow 自动保证最终整数 schedule 全局最优。旧方案仍有成立条件：单节点、拓扑均匀、expert 较小或热点稳定时，load-only replica placement 更简单。新机制获得的收益与代价必须一起读取：把 topology cost 写入 placement objective 可减少跨节点移动，但增加求解、转换和 transfer overlap 依赖。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：flow-to-integer rounding、拓扑矩阵陈旧、热点突变、weight transfer 不能隐藏或内存不足。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供条件计算路由的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-MOE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03676:end -->

<!-- review:SF-2026-ARXIV-2608-03682:start -->
#### PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud

<!-- claim:SF-2026-ARXIV-2608-03682:start -->《PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud》把 `INFER-TENSORRT-LLM` 的问题具体化为：同一模型需跨开发、仿真、边缘与云部署，碎片化栈成本上升。其机制是以 adapter 抽象 conditioning、solver、cache 与 output，同时复用执行图、kernel、内存和并行服务；primary v1 的 evaluation 绑定为pi0、pi0.5、GR00T N1.7、MiniCPM-Robot、Cosmos3；onboard/edge/cloud GPU，比较对象为各模型官方实现与专用 runtime。<!-- claim:SF-2026-ARXIV-2608-03682:end -->

证据支持的范围是：所测 embodied/world models 中共享 runtime 可承载异构执行并暴露瓶颈差异；不支持的外推是：动作安全正确，或所有模型/硬件上统一 runtime 都最快。旧方案仍有成立条件：模型少且稳定时每模型独立程序便于专项优化。新机制获得的收益与代价必须一起读取：统一生命周期换 adapter/公共抽象和专项性能缺口。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：adapter 语义、cache/solver 或后端不匹配；窄场景专用栈可能更快。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供编译后的执行计划的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03682:end -->

<!-- review:SF-2026-ARXIV-2608-03699:start -->
#### TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents

<!-- claim:SF-2026-ARXIV-2608-03699:start -->《TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents》把 `AGENT-MEMORY` 的问题具体化为：长期记忆需 revise/reject/defer 并处理来源冲突和时间失效。其机制是把记忆更新拆为五种 action，维护 accepted/pending/rejected ledgers，并学习时序/来源条件下的状态化结果；primary v1 的 evaluation 绑定为in-domain、cross-source、temporal、counterfactual 与 sequential memory 场景，比较对象为binary Write/Hold memory policy。<!-- claim:SF-2026-ARXIV-2608-03699:end -->

证据支持的范围是：所测冲突/时序场景中细粒度 action/ledger 更能控制污染；不支持的外推是：提供来源真实性 oracle 或覆盖无限时长开放工具链风险。旧方案仍有成立条件：来源可信、append-only、几乎无冲突时 Write/Hold 简单低成本。新机制获得的收益与代价必须一起读取：更精细状态控制换标签、policy、ledger 一致性与训练成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：可靠性/时间判断错、action 分类错或早期 ledger 污染。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03699:end -->

<!-- review:SF-2026-ARXIV-2608-03741:start -->
#### When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference

<!-- claim:SF-2026-ARXIV-2608-03741:start -->《When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference》把 `INFER-PD-DISAGGREGATION` 的问题具体化为：prefill/decode 与 attention/FFN 的计算/带宽压力不同。其机制是用 simulation 联合搜索量化和 intra/inter-device parallel schedule，并以 PDAF 建模 NPU 的 attention/FFN 分工；primary v1 的 evaluation 绑定为多模型/硬件 simulation；prefill-decode 与四路异构配置；含 ablation，比较对象为homogeneous GPU serving。<!-- claim:SF-2026-ARXIV-2608-03741:end -->

证据支持的范围是：给定模拟参数中异构资源及自动并行可产生更优配置；不支持的外推是：真实定制 NPU 生产验证或独立于模拟器校准的结论。旧方案仍有成立条件：阶段/算子资源相近且统一 GPU 易运维时同构部署最简单。新机制获得的收益与代价必须一起读取：专用化收益换跨设备通信、数据移动、搜索与模拟可信度风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：模拟校准、NPU 能力、互联或 workload mix 假设错误。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-PD-DISAGGREGATION`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03741:end -->

<!-- review:SF-2026-ARXIV-2608-03839:start -->
#### Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes

<!-- claim:SF-2026-ARXIV-2608-03839:start -->《Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes》把 `INFER-SPECULATIVE-DECODING` 的问题具体化为：工具结构重复但参数变化，语义相似 continuation 无法 exact 命中。其机制是用 verifier 已提交 token 的 hidden state 做 semantic re-key，再把命中 continuation 合并进 lexical draft tree；primary v1 的 evaluation 绑定为tool-calling 等 speculative benchmarks；匹配 pool/budget；API-Bank 与 published drafters，比较对象为exact-suffix lexical drafter、autoregressive decoding 与 EAGLE-3。<!-- claim:SF-2026-ARXIV-2608-03839:end -->

证据支持的范围是：所测工具流量中 exact lexical address 会漏掉语义相似 continuation；不支持的外推是：所有模型/流量/drafter 都应改用 hidden-state key，或越过 verifier commit 保证正确性。旧方案仍有成立条件：exact suffix 复用；重复上下文值相同时精准且索引简单。新机制获得的收益与代价必须一起读取：更广 draft reach 换 hidden-state 索引、碰撞、tree 管理和 verifier 工作。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：embedding collision、pool 陈旧、root 被拒或验证开销过大。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供proposal/verify/commit 状态的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-SPECULATIVE-DECODING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03839:end -->

<!-- review:SF-2026-ARXIV-2608-04074:start -->
#### Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms

<!-- claim:SF-2026-ARXIV-2608-04074:start -->论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。<!-- claim:SF-2026-ARXIV-2608-04074:end -->

论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。 直接保留全精度 KV 或只做逐元素量化，在上下文较短、显存充足且查询分布稳定时仍是更低风险方案；NOVA-KV 用 attention-preserving transform 再做 vector quantization，把压缩从数值近似推进到查询相关的结构保持。它以校准数据、额外 kernel 和解码路径复杂度换容量，quantization distortion、query-distribution shift 与 chunked-prefill 信息泄漏会限制可迁移性。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了context-conditioned KV state的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、带宽、精度与恢复为长期设计约束。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04074:end -->

<!-- review:SF-2026-ARXIV-2608-03994:start -->
#### When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings

<!-- claim:SF-2026-ARXIV-2608-03994:start -->《When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings》把 `MODEL-POSITION-ENCODING` 的问题具体化为：context 增长后有限精度把极小 attention weight 压成零。其机制是刻画 ALiBi 线性距离 bias 在有限精度下的 attention 下溢，并比较四类 mitigation；primary v1 的 evaluation 绑定为预训练 ALiBi models、小型 decoder pretraining、passkey 与标准 decoder benchmarks，比较对象为默认 ALiBi slope 与四类 mitigation/组合。<!-- claim:SF-2026-ARXIV-2608-03994:end -->

证据支持的范围是：所测精度/长度中下溢会令部分 head 对远端 token 失明；不支持的外推是：所有精度、长度、模型和任务中同一 mitigation 最优。旧方案仍有成立条件：训练长度内默认 ALiBi 简单且标准任务表现可接受。新机制获得的收益与代价必须一起读取：恢复长程可达性换位置偏置/训练行为改变及策略交互。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：精度、长度、slope/head 变化；passkey 恢复不等于生成质量提升。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-POSITION-ENCODING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-03994:end -->

<!-- review:SF-2026-ARXIV-2608-04289:start -->
#### SafeCommit: Certifying When Memory-Grounded Agents May Safely Act

<!-- claim:SF-2026-ARXIV-2608-04289:start -->SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。<!-- claim:SF-2026-ARXIV-2608-04289:end -->

SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。 仅凭模型置信度或单一最可能世界直接执行，在动作可撤销、环境观测充分且副作用低时成本最低；memory-grounded Agent 面对状态歧义和不可逆动作时，这个点估计不足。SafeCommit 维护 plausible-world support，仅在 conformal certificate 对全部保留世界安全时 commit，否则 probe 或 fallback，以校准、保守拒绝和额外交互换风险界；错误 safety map、exchangeability 破坏和固定动作/世界支持之外仍可能认证错误。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以policy、隔离与执行边界为长期设计约束。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2608-04289:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-03555 | retrieval sparse-attention decode over real long-context agent traces | GLM-5.2 (MLA+DSA), MiniMax-M3 (GQA+sparsity) and DeepSeek-V3.2 (MLA+DSA) | H200 GPU measurements plus paper-modeled/synthesized KARAT general-purpose PNM nodes | model-native formats including FP8 index keys where specified; no single normalized precision | agent traces with p99 198K–791K and max about 1M tokens | autoregressive decode under a P99 TBT SLO | global/model-dependent microbatches with configuration search; sensitivity includes large MoE batches | request concurrency represented through aggregate decode batch and context distribution; no single normalized count | P99 TBT≤100ms and SLO-constrained throughput per TDP | GPU-only model-native sparse attention plus training-free sparse-attention baselines; hardware-calibrated performance, area and power model |
| SF-2026-ARXIV-2608-04074 | long-context KV quantization | Llama, Qwen and GPT-OSS families | NVIDIA A100 and H100 | 2-bit KV plus paper comparison precisions | 16K/30K/60K/90K/128K quality protocols plus 8K serving protocol, depending on experiment | task answer or autoregressive decode; exact normalized output length varies by task | batch 1–128 across the disclosed serving experiments | Not Disclosed — v1 does not state one normalized multi-request serving concurrency beyond batch | quality-throughput frontier; no production SLO | paper-defined long-context quality tasks, serving measurements and full-cache/quantization comparisons |
| SF-2026-ARXIV-2608-04289 | controlled safe-commit simulator | proposal/probe policies in released scaffold | Not Disclosed | Not Disclosed | small fixed world supports | single commit/probe decision | Not Disclosed | repeated commitments require separate risk allocation | unsafe certified-commit target alpha | conformal certificate and simulator labels |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-04289 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260805-2608-04289 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=action confidence becomes a plausible-world safe-commit certificate | analysis:DA-20260805-2608-04289 |
| SF-2026-ARXIV-2608-04074 | score_7_9<br>potential_books_delta | selected | DA-20260805-2608-04074 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=KV quantization objective moves from element error to attention-output state sensitivity | analysis:DA-20260805-2608-04074 |
| SF-2026-ARXIV-2608-03555 | score_7_9<br>potential_books_delta | selected | DA-20260805-2608-03555 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=attention memory hierarchy expands to near-data processing and moves compute/data ownership | analysis:DA-20260805-2608-03555 |

<!-- analysis:DA-20260805-2608-04289:start -->
### SafeCommit: Certifying When Memory-Grounded Agents May Safely Act

SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。 仅凭模型置信度或单一最可能世界直接执行，在动作可撤销、环境观测充分且副作用低时成本最低；memory-grounded Agent 面对状态歧义和不可逆动作时，这个点估计不足。SafeCommit 维护 plausible-world support，仅在 conformal certificate 对全部保留世界安全时 commit，否则 probe 或 fallback，以校准、保守拒绝和额外交互换风险界；错误 safety map、exchangeability 破坏和固定动作/世界支持之外仍可能认证错误。

<!-- analysis:DA-20260805-2608-04289:end -->

<!-- analysis:DA-20260805-2608-04074:start -->
### Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms

论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。 直接保留全精度 KV 或只做逐元素量化，在上下文较短、显存充足且查询分布稳定时仍是更低风险方案；NOVA-KV 用 attention-preserving transform 再做 vector quantization，把压缩从数值近似推进到查询相关的结构保持。它以校准数据、额外 kernel 和解码路径复杂度换容量，quantization distortion、query-distribution shift 与 chunked-prefill 信息泄漏会限制可迁移性。

<!-- analysis:DA-20260805-2608-04074:end -->

<!-- analysis:DA-20260805-2608-03555:start -->
### Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention

KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。 固定把模型层映射到 GPU 或 PNM，并使用静态 microbatch，在模型、互连和负载稳定时仍简单可靠；KARAT 面对 placement、流水线气泡与设备资源耦合后，引入 PNM/GPU 联合映射、microbatch 调度和配置搜索。收益依赖 PNM 性能模型与校准，动态负载触发 rebalancing 时还会受链路、面积/功耗和迁移成本约束。

<!-- analysis:DA-20260805-2608-03555:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-03555 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L223 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/56-inference-scheduling.md#L14 | existing:SF-2026-ARXIV-2608-03555 | delta:SF-2026-ARXIV-2608-03555 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2608-03555 |
| SF-2026-ARXIV-2608-04074 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L385 | books/part-02-model/19-kv-cache.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-04074 | delta:SF-2026-ARXIV-2608-04074 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-04074 |
| SF-2026-ARXIV-2608-04289 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L353 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2608-04289 | delta:SF-2026-ARXIV-2608-04289 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-04289 |

<!-- books-review:SF-2026-ARXIV-2608-03555:start --><!-- existing:SF-2026-ARXIV-2608-03555:start -->现有中心命题：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。<!-- existing:SF-2026-ARXIV-2608-03555:end --><!-- delta:SF-2026-ARXIV-2608-03555:start -->KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。<!-- delta:SF-2026-ARXIV-2608-03555:end -->与上述中心命题相比，这个 family 的新增证据是：KARAT 将 retrieval sparse attention 的 KV/index 工作放到 PNM，并用 microbatch、重平衡和 configuration search 协调 GPU 与近存计算。作者在三种模型与 agent traces 上报告吞吐/TDP，但收益依赖 PNM 设备和模拟/原型合同，不能外推到普通 GPU fleet。 该 delta 已落在《第54章 GPU Memory》的正文机制锚点；语义相邻边界为 INFER-KV-CACHE：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。；INFER-SCHEDULING：推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-03555:end -->

<!-- books-review:SF-2026-ARXIV-2608-04074:start --><!-- existing:SF-2026-ARXIV-2608-04074:start -->现有中心命题：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。<!-- existing:SF-2026-ARXIV-2608-04074:end --><!-- delta:SF-2026-ARXIV-2608-04074:start -->论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。<!-- delta:SF-2026-ARXIV-2608-04074:end -->与上述中心命题相比，这个 family 的新增证据是：论文通过 attention-preserving transform 与 vector quantization，把 KV 位宽分配从逐元素误差改为 query 使用方式驱动。作者在 Llama/Qwen/GPT-OSS 和 A100/H100 范围内比较，2-bit 结果仍属于给定模型与 kernel 实现；joint K/V 和生产并发是开放边界。 该 delta 已落在《第45章 为什么 KV Cache 能提速》的正文机制锚点；语义相邻边界为 MODEL-KV-CACHE：KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-04074:end -->

<!-- books-review:SF-2026-ARXIV-2608-04289:start --><!-- existing:SF-2026-ARXIV-2608-04289:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2608-04289:end --><!-- delta:SF-2026-ARXIV-2608-04289:start -->SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。<!-- delta:SF-2026-ARXIV-2608-04289:end -->与上述中心命题相比，这个 family 的新增证据是：SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-04289:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260805-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260805; coverage:SRC-GITHUB-COMMIT:20260805; semantic-review:SA-20260805-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260805-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-03335; review:SF-2026-ARXIV-2608-03555; review:SF-2026-ARXIV-2608-03609; review:SF-2026-ARXIV-2608-03676; review:SF-2026-ARXIV-2608-03682; review:SF-2026-ARXIV-2608-03699; review:SF-2026-ARXIV-2608-03741; review:SF-2026-ARXIV-2608-03839; review:SF-2026-ARXIV-2608-04074; review:SF-2026-ARXIV-2608-03994; review:SF-2026-ARXIV-2608-04289; semantic-review:SA-20260805-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260805-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260805-2608-03555; analysis:DA-20260805-2608-04074; analysis:DA-20260805-2608-04289; semantic-review:SA-20260805-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260805-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-03555; books-review:SF-2026-ARXIV-2608-04074; books-review:SF-2026-ARXIV-2608-04289; review:SF-2026-ARXIV-2608-03335; review:SF-2026-ARXIV-2608-03609; review:SF-2026-ARXIV-2608-03676; review:SF-2026-ARXIV-2608-03682; review:SF-2026-ARXIV-2608-03699; review:SF-2026-ARXIV-2608-03741; review:SF-2026-ARXIV-2608-03839; review:SF-2026-ARXIV-2608-03994; semantic-review:SA-20260805-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260805-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260805-COVERAGE:end -->
<!-- semantic-review:SA-20260805-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260805-EVIDENCE:end -->
<!-- semantic-review:SA-20260805-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260805-SELECTION:end -->
<!-- semantic-review:SA-20260805-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260805-BOOKS:end -->

## 8. Ignored Noise

667 条 arXiv v1 中有 656 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：3 个 `Integrate`、0 个 `No Change — Existing Coverage`、8 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/05/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-05-inference-system/54-gpu-memory.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-06-ai-infrastructure/72-security.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [Formal Verification of Agentic Systems over Operational Data](https://arxiv.org/abs/2608.03609v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [TAOT: Topology-Aware Optimal Transport for Dynamic Expert Replica Placement in MoE Training](https://arxiv.org/abs/2608.03676v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [PhyAI: Real-Time Physical AI at the Edge, Scalable Rollouts in the Cloud](https://arxiv.org/abs/2608.03682v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents](https://arxiv.org/abs/2608.03699v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [When Does Disaggregation Pay? Simulating Prefill--Decode--Attention--FFN Specialization for Agentic LLM Inference](https://arxiv.org/abs/2608.03741v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [Oilbird: Training-Free Speculative Decoding with Keys the Verifier Already Computes](https://arxiv.org/abs/2608.03839v1) — published/event date: 2026-08-04; accessed: 2026-08-25
- [Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms](https://arxiv.org/abs/2608.04074v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings](https://arxiv.org/abs/2608.03994v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [SafeCommit: Certifying When Memory-Grounded Agents May Safely Act](https://arxiv.org/abs/2608.04289v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
