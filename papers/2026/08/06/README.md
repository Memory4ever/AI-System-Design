# Daily Research — 2026-08-06

**Research Date:** 2026-08-06

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-05 09:00:00 ～ 2026-08-06 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-05 09:00:00` 至 `2026-08-06 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 534 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 15 个候选：1 个 Deep Review、14 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-GPU-MEMORY` 中由《PLoRA: An NDP-Enhanced Pooled-Memory System for Cost-Efficient Multi-LoRA Serving》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-06 |
| Window End | 2026-08-06 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-06-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-05T09:00:00+08:00 | 2026-08-06T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 534 | SF-2026-ARXIV-2608-04401<br>SF-2026-ARXIV-2608-04428<br>SF-2026-ARXIV-2608-04450<br>SF-2026-ARXIV-2608-04458<br>SF-2026-ARXIV-2608-04502<br>SF-2026-ARXIV-2608-05204<br>SF-2026-ARXIV-2608-05212<br>SF-2026-ARXIV-2608-05219<br>SF-2026-ARXIV-2608-05225<br>SF-2026-ARXIV-2608-05245<br>SF-2026-ARXIV-2608-05246<br>SF-2026-ARXIV-2608-05095<br>SF-2026-ARXIV-2608-05136<br>SF-2026-ARXIV-2608-05144<br>SF-2026-ARXIV-2608-05483 | page count=7 snapshot files; final_cursor=end; daily-window total=534; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-06T09:00:00+08:00 | coverage:SRC-ARXIV:20260806 | — |

<!-- coverage:SRC-ARXIV:20260806:start -->submittedDate query filtered to [2026-08-05T09:00:00+08:00, 2026-08-06T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 15 routed families.<!-- coverage:SRC-ARXIV:20260806:end -->

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
| SF-2026-ARXIV-2608-04401 | arXiv:2608.04401v1 | paper-v1:2608.04401 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-04401 | self | — | new_in_window | MODEL-MOE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04428 | arXiv:2608.04428v1 | paper-v1:2608.04428 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-04428 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04450 | arXiv:2608.04450v1 | paper-v1:2608.04450 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-04450 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04458 | arXiv:2608.04458v1 | paper-v1:2608.04458 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-04458 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-04502 | arXiv:2608.04502v1 | paper-v1:2608.04502 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-04502 | self | — | new_in_window | INFER-SCHEDULING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05204 | arXiv:2608.05204v1 | paper-v1:2608.05204 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05204 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05212 | arXiv:2608.05212v1 | paper-v1:2608.05212 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05212 | self | — | new_in_window | AGENT-REFLECTION | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05219 | arXiv:2608.05219v1 | paper-v1:2608.05219 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05219 | self | — | new_in_window | TRAIN-GRPO | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05225 | arXiv:2608.05225v1 | paper-v1:2608.05225 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05225 | self | — | new_in_window | AGENT-PLANNING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05245 | arXiv:2608.05245v1 | paper-v1:2608.05245 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05245 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05246 | arXiv:2608.05246v1 | paper-v1:2608.05246 | 2026-W32 | 2026-08-05 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05246 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05095 | arXiv:2608.05095v1 | paper-v1:2608.05095 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05095 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05136 | arXiv:2608.05136v1 | paper-v1:2608.05136 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05136 | self | — | new_in_window | TRAIN-PRETRAINING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05144 | arXiv:2608.05144v1 | paper-v1:2608.05144 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05144 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05483 | arXiv:2608.05483v1 | paper-v1:2608.05483 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-05483 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2608-05483 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-04401 | RP-41e1b611f1e3ee7e | standard | arXiv:2608.04401v1 | SRC-ARXIV@arXiv:2608.04401v1 | https://arxiv.org/html/2608.04401v1#S2 (2 Elbow-Based Routing) | https://arxiv.org/html/2608.04401v1#S3 (3 Experimental Validation) | https://arxiv.org/html/2608.04401v1#S4 (4 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-04401 | complete |
| SF-2026-ARXIV-2608-04428 | RP-2f3227b3afdec7a6 | standard | arXiv:2608.04428v1 | SRC-ARXIV@arXiv:2608.04428v1 | https://arxiv.org/html/2608.04428v1#S6 (6. Deltoris Architecture) | https://arxiv.org/html/2608.04428v1#S8 (8. Evaluation) | https://arxiv.org/html/2608.04428v1#S10 (10. Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-04428 | complete |
| SF-2026-ARXIV-2608-04450 | RP-77c4ce9c7ea194c2 | standard | arXiv:2608.04450v1 | SRC-ARXIV@arXiv:2608.04450v1 | https://arxiv.org/html/2608.04450v1#S2 (2 CommBench and Framework Structure) | https://arxiv.org/html/2608.04450v1#S3 (3 Experiments) | https://arxiv.org/html/2608.04450v1#S5 (5 Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-04450 | complete |
| SF-2026-ARXIV-2608-04458 | RP-ca41bd0bc83c95f1 | standard | arXiv:2608.04458v1 | SRC-ARXIV@arXiv:2608.04458v1 | https://arxiv.org/html/2608.04458v1#S5 (V Server Design Principles and Case Studies) | Not Required — reviewed v1 full text exposes no standalone controlled-evaluation heading; scope is delimited by https://arxiv.org/html/2608.04458v1#S5 (V Server Design Principles and Case Studies) | https://arxiv.org/html/2608.04458v1#S6 (VI Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-04458 | complete |
| SF-2026-ARXIV-2608-04502 | RP-422d8ae38f5a04ec | standard | arXiv:2608.04502v1 | SRC-ARXIV@arXiv:2608.04502v1 | https://arxiv.org/html/2608.04502v1#S3 (3. Design) | https://arxiv.org/html/2608.04502v1#S5 (5. Evaluation) | https://arxiv.org/html/2608.04502v1#S6 (6. Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-04502 | complete |
| SF-2026-ARXIV-2608-05204 | RP-54cfb91cbb6eff5a | standard | arXiv:2608.05204v1 | SRC-ARXIV@arXiv:2608.05204v1 | https://arxiv.org/html/2608.05204v1#S3 (III SkillTrace Design) | https://arxiv.org/html/2608.05204v1#S4 (IV Evaluation) | https://arxiv.org/html/2608.05204v1#S5 (V Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05204 | complete |
| SF-2026-ARXIV-2608-05212 | RP-be8388b40205435c | standard | arXiv:2608.05212v1 | SRC-ARXIV@arXiv:2608.05212v1 | https://arxiv.org/html/2608.05212v1#Sx4 (4 SearchAuditor) | https://arxiv.org/html/2608.05212v1#Sx5 (5 Experiments) | https://arxiv.org/html/2608.05212v1#A5 (Appendix E Cost and Efficiency Analysis) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05212 | complete |
| SF-2026-ARXIV-2608-05219 | RP-9f9a22682615ece2 | standard | arXiv:2608.05219v1 | SRC-ARXIV@arXiv:2608.05219v1 | https://arxiv.org/html/2608.05219v1#Sx5.SSx3 (State-Contextualized Guidance Construction) | https://arxiv.org/html/2608.05219v1#Sx6 (Experimental Setup) | https://arxiv.org/html/2608.05219v1#Sx9 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05219 | complete |
| SF-2026-ARXIV-2608-05225 | RP-9ad380c9bbf9f899 | standard | arXiv:2608.05225v1 | SRC-ARXIV@arXiv:2608.05225v1 | https://arxiv.org/html/2608.05225v1#S3 (3 Method) | https://arxiv.org/html/2608.05225v1#S4 (4 Experiments) | https://arxiv.org/html/2608.05225v1#S5 (5 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05225 | complete |
| SF-2026-ARXIV-2608-05245 | RP-491e628e2bac4a5f | standard | arXiv:2608.05245v1 | SRC-ARXIV@arXiv:2608.05245v1 | https://arxiv.org/html/2608.05245v1#Sx4 (Methodology of Search2Skill) | https://arxiv.org/html/2608.05245v1#Sx5 (Experimental Setup) | https://arxiv.org/html/2608.05245v1#Sx8 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05245 | complete |
| SF-2026-ARXIV-2608-05246 | RP-852cacdb4dd32084 | standard | arXiv:2608.05246v1 | SRC-ARXIV@arXiv:2608.05246v1 | https://arxiv.org/html/2608.05246v1#S4 (4 LUNAR Construction) | https://arxiv.org/html/2608.05246v1#S6 (6 Experiments); https://arxiv.org/html/2608.05246v1#S11 (11 Experimental Details) | https://arxiv.org/html/2608.05246v1#Sx1 (Ethical Considerations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05246 | complete |
| SF-2026-ARXIV-2608-05095 | RP-3bab5320147ebb12 | standard | arXiv:2608.05095v1 | SRC-ARXIV@arXiv:2608.05095v1 | https://arxiv.org/html/2608.05095v1#S3 (3 The Proposed Method) | https://arxiv.org/html/2608.05095v1#S4 (4 Experiments) | https://arxiv.org/html/2608.05095v1#S5 (5 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05095 | complete |
| SF-2026-ARXIV-2608-05136 | RP-169722745e761bd4 | standard | arXiv:2608.05136v1 | SRC-ARXIV@arXiv:2608.05136v1 | https://arxiv.org/html/2608.05136v1#S3 (3 Setup: gauge, task, and protocol) | https://arxiv.org/html/2608.05136v1#S9 (9 Real data at matched training loss) | https://arxiv.org/html/2608.05136v1#S11 (11 Discussion and limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05136 | complete |
| SF-2026-ARXIV-2608-05144 | RP-bd88626ceea05fd8 | standard | arXiv:2608.05144v1 | SRC-ARXIV@arXiv:2608.05144v1 | https://arxiv.org/html/2608.05144v1#S4 (4 Argus Runtime) | https://arxiv.org/html/2608.05144v1#S5 (5 Empirical Methodology); https://arxiv.org/html/2608.05144v1#S6 (6 Results) | https://arxiv.org/html/2608.05144v1#S8 (8 Limitations and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05144 | complete |
| SF-2026-ARXIV-2608-05483 | RP-b1d0275f18454bdd | deep | arXiv:2608.05483v1 | SRC-ARXIV@arXiv:2608.05483v1 | https://arxiv.org/html/2608.05483v1#S4 (§IV PLoRA architecture)<br>https://arxiv.org/html/2608.05483v1#S5 (§V GPU/NDP collaboration)<br>https://arxiv.org/html/2608.05483v1#S6 (§VI memory manager, strategy selection and cost model) | https://arxiv.org/html/2608.05483v1#S7 (§VII calibrated simulator evaluation, real-hardware inputs, performance and ablations) | https://arxiv.org/html/2608.05483v1#S7.SS6 (§VII-F device-parameter sensitivity)<br>https://arxiv.org/html/2608.05483v1#S8 (§VIII link-bandwidth sensitivity; v1 reports calibrated simulation rather than an independent production deployment) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-05483 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-04401:start -->
#### Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection

<!-- claim:SF-2026-ARXIV-2608-04401:start -->《Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection》把 `MODEL-MOE` 的问题具体化为：统一 k 会对易 token 过算或对难 token 少算。其机制是对每 token 的 router probabilities 排序并寻找 elbow，动态决定 expert count 并检查负载；primary v1 的 evaluation 绑定为一个 state-of-the-art MoE、多 benchmark；测 latency、accuracy 与 load balance，比较对象为fixed top-k routing。<!-- claim:SF-2026-ARXIV-2608-04401:end -->

证据支持的范围是：所测 MoE 中 token 间 relevance 分布不同，动态 k 改善计算-质量折中；不支持的外推是：适用所有 router calibration、expert topology、并发和 serving stack。旧方案仍有成立条件：固定 top-k 在 relevance 分布近似一致时确定且易容量规划。新机制获得的收益与代价必须一起读取：减少无效 expert compute 换可变 fan-out、load/tail 管理和检测开销。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：概率无清晰 elbow、router 未校准、imbalance 或通信 tail 增大。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供条件计算路由的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-MOE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04401:end -->

<!-- review:SF-2026-ARXIV-2608-04428:start -->
#### Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference

<!-- claim:SF-2026-ARXIV-2608-04428:start -->《Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference》把 `INFER-TENSORRT-LLM` 的问题具体化为：高频 edge control 的相邻状态相似且受 latency/energy 限制。其机制是用 temporal bit sparsity 计算输入 delta，在连续 control step 间 speculative reuse，并由 bit-serial accelerator 执行；primary v1 的 evaluation 绑定为diffusion VLA edge inference；mobile GPU 与 prior accelerators；检查 action accuracy，比较对象为mobile GPU 与 prior accelerator 类别。<!-- claim:SF-2026-ARXIV-2608-04428:end -->

证据支持的范围是：所测 VLA 流中时间相似性与硬件协同可减少重复运算/搬运并保持所测动作精度；不支持的外推是：控制安全、跨场景泛化或通用硬件可部署。旧方案仍有成立条件：控制频率低或相邻变化大时通用 GPU 全量重算更稳妥。新机制获得的收益与代价必须一起读取：速度/能效换 temporal assumption、speculative state 和 custom hardware。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：场景/动作突变、delta sparsity 消失、speculation 失效或 PE 不均衡。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供编译后的执行计划的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04428:end -->

<!-- review:SF-2026-ARXIV-2608-04450:start -->
#### CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?

<!-- claim:SF-2026-ARXIV-2608-04450:start -->《CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：AI coding evaluation 从生成语法扩展到多设备执行与性能 correctness 联合合同。其机制是建立覆盖 P2P、collective、expert parallel、compute-communication fusion 与 utility 的任务集，并在真实多 GPU 上编译、执行、校验 correctness 与 performance；primary v1 的 evaluation 绑定为100 余个专家任务，在 NVLink intra-node 与 RDMA inter-node 平台评测 frontier/open code models，比较对象为以单 GPU kernel benchmark、文本相似度或仅能编译作为 GPU communication code 能力证据。<!-- claim:SF-2026-ARXIV-2608-04450:end -->

证据支持的范围是：通信代码必须同时满足分布式语义正确性和硬件相关性能，单一 pass/fail 不足以刻画；不支持的外推是：作者测得的通过比例可代表其他模型版本或平台、benchmark 无泄漏，或统一指标可替代逐 task failure analysis。旧方案仍有成立条件：常规算法代码、单 GPU kernel 或成熟 NCCL primitive 直接调用场景不需要该 benchmark 深度。新机制获得的收益与代价必须一起读取：cheat-resistant 实测提高可信度，但依赖昂贵硬件、reference 实现、公平阈值和环境稳定性。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：测试污染、非确定性通信、拓扑差异、deadlock/hang、性能噪声或 reference 本身非最优。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04450:end -->

<!-- review:SF-2026-ARXIV-2608-04458:start -->
#### Architectural Implications of Agentic AI Workflows

<!-- claim:SF-2026-ARXIV-2608-04458:start -->《Architectural Implications of Agentic AI Workflows》把 `AGENT-PLATFORM` 的问题具体化为：workflow 交错 LLM、tool 与 orchestration，平均利用低而 burst 明显。其机制是先画像 agent workflow，再按 role/affinity 池化 CPU，回收空闲 cores、保护 tool burst tail，并对 GPU state 预取/oversubscribe；primary v1 的 evaluation 绑定为Azure 生产观测、开源 agent framework 实验与 commodity-server prototype，比较对象为uniform/homogeneous server 与普通 shared-core multiplexing。<!-- claim:SF-2026-ARXIV-2608-04458:end -->

证据支持的范围是：所观测 workflow 中角色异构和突发性导致资源失配，原型可改善利用/SLO；不支持的外推是：对所有 agent stack、云和硬件都优于专用/同构部署。旧方案仍有成立条件：单体推理、角色稳定和负载规律时同构资源池易规划隔离。新机制获得的收益与代价必须一起读取：利用率换预取、placement、oversubscription、隔离和调参复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：tool burst 预测错、GPU state thrash、locality 丢失或 role mix 漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供Agent 运行与治理状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-PLATFORM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04458:end -->

<!-- review:SF-2026-ARXIV-2608-04502:start -->
#### AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation

<!-- claim:SF-2026-ARXIV-2608-04502:start -->《AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation》把 `INFER-SCHEDULING` 的问题具体化为：预算/SLO 下设备和架构组合爆炸且 attention/FFN 的设备性价比不同。其机制是用解析模型分别优化 AFD 与 collocated 架构，并在受限 hardware search 中联合选设备和组织；primary v1 的 evaluation 绑定为exhaustive ground-truth deployment space 与 LongCat 2.0 实机；固定 SLO/budget/catalog/runtime，比较对象为exhaustive provisioning、最佳 collocated 与 heuristic device selection。<!-- claim:SF-2026-ARXIV-2608-04502:end -->

证据支持的范围是：所验证空间中受限搜索保留架构选择质量，且 AFD 并非总是更优；不支持的外推是：覆盖任意模型、价格、拓扑、runtime 或动态负载。旧方案仍有成立条件：候选空间小时 exhaustive 最可靠；互补设备不足时 collocation 更简单。新机制获得的收益与代价必须一起读取：减少实测换解析模型、校准和 catalog/runtime 假设误差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：性能模型失配、价格边界变化、未见拓扑/负载或能力判断错误。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供请求调度与资源所有权的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-04502:end -->

<!-- review:SF-2026-ARXIV-2608-05204:start -->
#### SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse

<!-- claim:SF-2026-ARXIV-2608-05204:start -->《SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse》把 `AGENT-PLATFORM` 的问题具体化为：agent skill 的复用证据分散在文字、实现片段和运行结构，单模态会漏掉部分复用。其机制是分别抽取 Expression、Implementation 与 Operational provenance trace，并把 activation/procedure/resource-flow 表为 SOG；ingestion 时用 LLM，audit 时缓存后确定性比较和逐 trace 校准；primary v1 的 evaluation 绑定为100 marketplace anchor、820 reuse positive、751 negative 的 SkillTrace-Bench，以及 36,446 skill wild audit，比较对象为只做源码 clone detection 或 whole-package embedding similarity。<!-- claim:SF-2026-ARXIV-2608-05204:end -->

证据支持的范围是：该 benchmark 中，多 trace attribution 比 repository-level baseline 更能恢复被变换或只保留部分形态的 reuse evidence；不支持的外推是：高相似度等于侵权/恶意复用、wild audit 队列是真值，或 LLM 抽取 operation graph 无误。旧方案仍有成立条件：纯代码 package、许可证明确且 operation structure 不重要时，传统 clone detection 更便宜。新机制获得的收益与代价必须一起读取：多 trace 提高可解释召回，但增加 ingestion、阈值校准、缓存版本与人工 adjudication 成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：paraphrase/obfuscation、同功能严格负例、SOG 抽取错误、skill version 漂移或 marketplace metadata 不完整。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供Agent 运行与治理状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-PLATFORM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05204:end -->

<!-- review:SF-2026-ARXIV-2608-05212:start -->
#### SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents

<!-- claim:SF-2026-ARXIV-2608-05212:start -->《SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents》把 `AGENT-REFLECTION` 的问题具体化为：长搜索轨迹嘈杂且早期错误传播，人工定位/重跑成本高。其机制是为失败搜索轨迹标注 error step/root cause/reference repair，并用多视角 evidence adjudication 定位、修复、续跑；primary v1 的 evaluation 绑定为open-weight models 的 deep-search 失败长轨迹；frontier auditors；端到端 recovery，比较对象为GPT-5.5 驱动的 strongest auditor baseline。<!-- claim:SF-2026-ARXIV-2608-05212:end -->

证据支持的范围是：策展失败轨迹中多视角定位/修复改善诊断和恢复；不支持的外推是：能在线预防错误或覆盖所有 agent/tool workflow。旧方案仍有成立条件：短轨迹和低失败率时人工逐步检查负责且够用。新机制获得的收益与代价必须一起读取：降低人工审计换额外 auditor 推理、标注与 judge 偏差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：证据缺失、judge 偏差、root-cause 标签错或 repair 副作用。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-REFLECTION`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05212:end -->

<!-- review:SF-2026-ARXIV-2608-05219:start -->
#### When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents

<!-- claim:SF-2026-ARXIV-2608-05219:start -->《When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents》把 `TRAIN-GRPO` 的问题具体化为：student 动作改变环境状态与子目标顺序后，reference 可能不再提供局部兼容指导。其机制是逐 turn 检查 student execution state 是否匹配 reference trajectory 中受支持状态，只在 matched state 蒸馏，并用该状态下的成功轨迹构造 teacher context；primary v1 的 evaluation 绑定为ALFWorld 与 WebShop、Qwen3-1.7B，对比 unconditional full-path distillation 并做 routing/context ablation，比较对象为privileged on-policy teacher 在每个 turn 无条件用成功 reference 重评分 student response。<!-- claim:SF-2026-ARXIV-2608-05219:end -->

证据支持的范围是：作者两环境和 ablation 中，筛选局部匹配 turn 与构造 state-compatible teacher context 都对 success 增益有贡献；不支持的外推是：state matching 是充分因果对齐、适用于任意环境，或两项 success 增益可外推到其他 agent/model。旧方案仍有成立条件：student 与 reference 高度同步、环境确定且短 horizon 时，无条件 distillation 更简单且监督更密。新机制获得的收益与代价必须一起读取：过滤失配指导减少错误梯度，但牺牲监督覆盖，并需要可靠 state matcher 与 context construction。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：状态等价判断错误、参考轨迹覆盖不足、稀疏 matched turn、环境部分可观测或 teacher 偏差。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供组内相对 credit的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`TRAIN-GRPO`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05219:end -->

<!-- review:SF-2026-ARXIV-2608-05225:start -->
#### Project2Task: Graph-Guided Project-Level Planning for Autonomous Research

<!-- claim:SF-2026-ARXIV-2608-05225:start -->《Project2Task: Graph-Guided Project-Level Planning for Autonomous Research》把 `AGENT-PLANNING` 的问题具体化为：project-level research 需要并行备选与依赖序列，同时保证 contribution ownership 和可集成输出。其机制是把候选贡献拆成 innovation atoms 与 directed lineage graph，用 Bernoulli block-model 选择横向/纵向/混合 portfolio，再生成含 owner、artifact、evaluation、boundary 与 dependency 的 task contract；primary v1 的 evaluation 绑定为十个 project brief、约三十项任务的 manuscript portfolio 评价，并接入 AutoResearchClaw 测下游 task accuracy，比较对象为把研究项目当作单个超大任务，或生成平坦、重叠且无依赖的 task list。<!-- claim:SF-2026-ARXIV-2608-05225:end -->

证据支持的范围是：作者十个 brief 的 portfolio judge 与下游 executor 实验中，显式 graph/task contract 改善任务边界、组合质量与执行准确率；不支持的外推是：自动评价分数等于真实科研质量、lineage graph 无遗漏，或十个 brief 可证明通用自治研究。旧方案仍有成立条件：目标单一、任务少或专家已明确 work breakdown 时，人工计划更直接。新机制获得的收益与代价必须一起读取：显式 graph/contract 改善边界和执行顺序，但增加 atom 抽取、portfolio objective 与 repair 维护成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：贡献重叠未识别、dependency 环、错误 evaluation contract、下游 executor 不兼容或 judge bias。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供计划状态与分支选择的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-PLANNING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05225:end -->

<!-- review:SF-2026-ARXIV-2608-05245:start -->
#### Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2608-05245:start -->《Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning》把 `AGENT-MEMORY` 的问题具体化为：专业程序位于参数知识之外且自身轨迹无法发现缺失能力。其机制是识别 capability gap 后检索外部来源并蒸馏为结构化 skill，再用 rubric RL 学何时搜、搜什么和如何生成；primary v1 的 evaluation 绑定为多个 expert-domain benchmarks；streaming/held-out 与跨模型规模分析，比较对象为search-augmented 与 trajectory-based skill-learning baselines。<!-- claim:SF-2026-ARXIV-2608-05245:end -->

证据支持的范围是：所测专业域中外部证据和结构化抽象可补参数/轨迹之外的能力缺口；不支持的外推是：保证 skill 正确、安全、有 provenance 或覆盖所有专业域。旧方案仍有成立条件：所需程序已在参数知识/自身轨迹时直接生成更便宜。新机制获得的收益与代价必须一起读取：能力扩展换检索成本、source trust、rubric gaming 和抽象误差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：低质量来源、provenance 丢失、skill 陈旧或省略关键例外。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05245:end -->

<!-- review:SF-2026-ARXIV-2608-05246:start -->
#### LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs

<!-- claim:SF-2026-ARXIV-2608-05246:start -->《LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：跨域个性化瓶颈在相关 evidence selection/integration，而不仅是上下文容量。其机制是构造由真实行为分布约束的 coarse-to-fine 合成跨域 app log，并评价模型能否从纵向行为证据做 personalization；primary v1 的 evaluation 绑定为19 个模型，覆盖 clothing/food/housing/mobility，对比 fine-grained retrieval、compressed memory、context/model scale 与 privacy trade-off，比较对象为用 textual persona 或单一行为信号评估 personalization，并假设更多 context/更大模型自然更好。<!-- claim:SF-2026-ARXIV-2608-05246:end -->

证据支持的范围是：作者 19 模型结果支持：仅增加 context 或模型规模不足以保证跨域 personalization，直接检索细粒度行为在该协议中优于压缩 memory；不支持的外推是：合成 log 等于真实用户、personalization score 等于用户价值，或 direct retrieval 对所有隐私/SLO 都优越。旧方案仍有成立条件：领域单一、用户明确提供偏好或 privacy 风险高时，persona/显式配置更可控。新机制获得的收益与代价必须一起读取：细粒度 evidence 提升个性化但增加检索成本、隐私暴露和错误跨域关联。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：合成分布偏差、行为稀疏、敏感属性推断、长期漂移、错误 evidence 选择或 evaluator 偏好。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05246:end -->

<!-- review:SF-2026-ARXIV-2608-05095:start -->
#### Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite

<!-- claim:SF-2026-ARXIV-2608-05095:start -->《Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite》把 `AGENT-MEMORY` 的问题具体化为：历史累积且一次更新跨依赖单元，扁平检索和局部改写产生不一致。其机制是用层次图做 coarse-to-fine memory，MicroGraph 定位 support/evidence path 并协调局部和跨单元 rewrite；primary v1 的 evaluation 绑定为long-term conversational QA 与 conflict-aware memory；测 answer、token efficiency 与 evidence selection，比较对象为flat graph memory 与 independent unit-wise rewrite。<!-- claim:SF-2026-ARXIV-2608-05095:end -->

证据支持的范围是：所测长期会话/冲突任务中减少无关检索和局部更新冲突；不支持的外推是：保证持久记忆真实/安全或覆盖无限在线规模。旧方案仍有成立条件：记忆小、关系浅且更新局部时 flat graph/独立 rewrite 简单可控。新机制获得的收益与代价必须一起读取：聚焦检索换层次维护、路径定位和依赖更新复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：support path 选错、hierarchy 陈旧、传播错误或缺 provenance。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05095:end -->

<!-- review:SF-2026-ARXIV-2608-05136:start -->
#### The Loss Does Not See the Basis, but Adam Does

<!-- claim:SF-2026-ARXIV-2608-05136:start -->《The Loss Does Not See the Basis, but Adam Does》把 `TRAIN-PRETRAINING` 的问题具体化为：欠定分解有 gauge-equivalent 表示，optimizer 可破坏对称性并改最终解。其机制是用 optimizer gauge-equivariance 分析低秩 gradient-flow bias 是否跨等价参数化保持，并给出结构/迁移定理；primary v1 的 evaluation 绑定为matrix sensing、gauge-equivalent transformer initializations 与 hyperspectral datasets，比较对象为GD、momentum、shared-scalar Adam、Muon、Shampoo 与 coordinate-wise methods。<!-- claim:SF-2026-ARXIV-2608-05136:end -->

证据支持的范围是：欠定/factored 设置中 basis/preconditioner 会改变 implicit interpolant，equivariance 必要但不充分；不支持的外推是：形成全任务 optimizer 排名或覆盖所有 Transformer training。旧方案仍有成立条件：坐标对称性不关键时 Adam 类逐坐标适配仍合理。新机制获得的收益与代价必须一起读取：坐标自适应和优化便利换 invariance 与预期低秩 bias。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：equivariance 不保证低秩；spectral tail、噪声和显式正则可主导。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供训练目标与优化轨迹的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-PRETRAINING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05136:end -->

<!-- review:SF-2026-ARXIV-2608-05144:start -->
#### Argus: A General-Purpose Agentic Reasoning Runtime for Long-Horizon Tasks

<!-- claim:SF-2026-ARXIV-2608-05144:start -->《Argus: A General-Purpose Agentic Reasoning Runtime for Long-Horizon Tasks》把 `AGENT-WORKFLOW` 的问题具体化为：长任务需要在 evidence 支持时坚持、在 measurement 失败时 pivot，并跨 mission 累积可审计状态。其机制是由 Manager、Planner、Engineer、Reviewer 在 durable project state 上执行 bounded mission，并只在 role-owned review/verification 后吸收 memory、skill、procedure、verifier 与 rejected route；primary v1 的 evaluation 绑定为七个 GPT-5.5 arena、SWE-Bench/AARRI/GPU kernel/训练等任务及多日 research pipeline，报告 tokens、workflow time、recovery 与 rollback，比较对象为一次性 agent loop 或只靠当前 context 自我反思，不持久保留已验证/证伪路线。<!-- claim:SF-2026-ARXIV-2608-05144:end -->

证据支持的范围是：作者所测 arena 与 multi-day pipeline 中，verification-gated runtime 能恢复失败路线并把已验证方法留给后续 mission；不支持的外推是：固定权重 harness 的提升可归因于单一组件、对其他模型通用，或高 token 成本在生产中总是合理。旧方案仍有成立条件：短任务、低风险或状态无需跨轮持久化时，简单 planner/tool loop 成本更低。新机制获得的收益与代价必须一起读取：self-evolution 从改权重转为更新 runtime state/control policy，获得可恢复性但需要角色、验证器和升级边界。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：验证器误判、错误 memory 被接纳、角色循环、token 成本、任务泄漏或 operator escalation 过晚。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供可恢复 workflow state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-WORKFLOW`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05144:end -->

<!-- review:SF-2026-ARXIV-2608-05483:start -->
#### PLoRA: An NDP-Enhanced Pooled-Memory System for Cost-Efficient Multi-LoRA Serving

<!-- claim:SF-2026-ARXIV-2608-05483:start -->PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。<!-- claim:SF-2026-ARXIV-2608-05483:end -->

PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。 把每个 LoRA adapter 完整放在 GPU，或依赖主机侧搬运，在 adapter 数量少且 PCIe/CXL 带宽未饱和时仍合理；PLoRA 将共享 adapter state、near-data processing 与 manager 联合起来，用 CXL 容量和 NDP 降低 GPU 驻留压力。其收益依赖带宽/成本模型、prefill 与 decode 比例以及 NDP 面积功耗，模型偏差或 workload 变化会让 placement 失配。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了多层内存状态的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、传输与重算为长期设计约束。
- Knowledge owner：`INFER-GPU-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05483:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-05483 | multi-LoRA prefill/decode serving with pooled memory | Llama2-7B, Llama2-13B, Llama3-8B and Qwen3-30B; scaling model extends to 1.2T | 1× NVIDIA H100 80GB plus four modeled 512GB PLoRA CXL/NDP devices; paper also sweeps CXL- to NVLink-class links | FP16 GPU/NDP compute; KV sensitivity also evaluates FP16/INT8/INT4 | LMSYS 2–430 tokens; synthetic 100–1024 and 2048–4096 input tokens; up to 1000 adapters | matching 2–430, 100–1024 and 2048–4096 output-token ranges | per-adapter batch 0–256; prefill batch 256/512/1024 | adapter/request mixture modeled by LMSYS, uniform and skewed distributions; no single normalized concurrent-request count | decode TPOT, prefill TTFT, capacity and throughput/cost sensitivity | S-LoRA, Pure CXL, CPU-LoRA-Offload, Grace-Hopper and PLoRA-NoCXL with hardware-calibrated simulation |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-05483 | score_7_9<br>potential_books_delta | selected | DA-20260806-2608-05483 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=single-node memory capacity becomes CXL pooled-state placement and shared-bandwidth control | analysis:DA-20260806-2608-05483 |

<!-- analysis:DA-20260806-2608-05483:start -->
### PLoRA: An NDP-Enhanced Pooled-Memory System for Cost-Efficient Multi-LoRA Serving

PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。 把每个 LoRA adapter 完整放在 GPU，或依赖主机侧搬运，在 adapter 数量少且 PCIe/CXL 带宽未饱和时仍合理；PLoRA 将共享 adapter state、near-data processing 与 manager 联合起来，用 CXL 容量和 NDP 降低 GPU 驻留压力。其收益依赖带宽/成本模型、prefill 与 decode 比例以及 NDP 面积功耗，模型偏差或 workload 变化会让 placement 失配。

<!-- analysis:DA-20260806-2608-05483:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-05483 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L223 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/56-inference-scheduling.md#L14 | existing:SF-2026-ARXIV-2608-05483 | delta:SF-2026-ARXIV-2608-05483 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-05483 |

<!-- books-review:SF-2026-ARXIV-2608-05483:start --><!-- existing:SF-2026-ARXIV-2608-05483:start -->现有中心命题：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。<!-- existing:SF-2026-ARXIV-2608-05483:end --><!-- delta:SF-2026-ARXIV-2608-05483:start -->PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。<!-- delta:SF-2026-ARXIV-2608-05483:end -->与上述中心命题相比，这个 family 的新增证据是：PLoRA 用 CXL pooled memory 与 near-data processing 承担多 LoRA 状态，把单 GPU 显存约束转成池化容量与传输/计算协同。系统管理器和模拟器由真实硬件校准，但主要结论仍受 H100 与四设备配置约束。 该 delta 已落在《第54章 GPU Memory》的正文机制锚点；语义相邻边界为 INFER-KV-CACHE：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。；INFER-SCHEDULING：推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-05483:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260806-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260806; semantic-review:SA-20260806-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260806-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-04401; review:SF-2026-ARXIV-2608-04428; review:SF-2026-ARXIV-2608-04450; review:SF-2026-ARXIV-2608-04458; review:SF-2026-ARXIV-2608-04502; review:SF-2026-ARXIV-2608-05204; review:SF-2026-ARXIV-2608-05212; review:SF-2026-ARXIV-2608-05219; review:SF-2026-ARXIV-2608-05225; review:SF-2026-ARXIV-2608-05245; review:SF-2026-ARXIV-2608-05246; review:SF-2026-ARXIV-2608-05095; review:SF-2026-ARXIV-2608-05136; review:SF-2026-ARXIV-2608-05144; review:SF-2026-ARXIV-2608-05483; semantic-review:SA-20260806-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260806-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260806-2608-05483; semantic-review:SA-20260806-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260806-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-05483; review:SF-2026-ARXIV-2608-04401; review:SF-2026-ARXIV-2608-04428; review:SF-2026-ARXIV-2608-04450; review:SF-2026-ARXIV-2608-04458; review:SF-2026-ARXIV-2608-04502; review:SF-2026-ARXIV-2608-05204; review:SF-2026-ARXIV-2608-05212; review:SF-2026-ARXIV-2608-05219; review:SF-2026-ARXIV-2608-05225; review:SF-2026-ARXIV-2608-05245; review:SF-2026-ARXIV-2608-05246; review:SF-2026-ARXIV-2608-05095; review:SF-2026-ARXIV-2608-05136; review:SF-2026-ARXIV-2608-05144; semantic-review:SA-20260806-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260806-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260806-COVERAGE:end -->
<!-- semantic-review:SA-20260806-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260806-EVIDENCE:end -->
<!-- semantic-review:SA-20260806-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260806-SELECTION:end -->
<!-- semantic-review:SA-20260806-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260806-BOOKS:end -->

## 8. Ignored Noise

534 条 arXiv v1 中有 519 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：1 个 `Integrate`、0 个 `No Change — Existing Coverage`、14 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/06/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/54-gpu-memory.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection](https://arxiv.org/abs/2608.04401v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference](https://arxiv.org/abs/2608.04428v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?](https://arxiv.org/abs/2608.04450v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [Architectural Implications of Agentic AI Workflows](https://arxiv.org/abs/2608.04458v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation](https://arxiv.org/abs/2608.04502v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse](https://arxiv.org/abs/2608.05204v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents](https://arxiv.org/abs/2608.05212v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [When Privileged Guidance Misaligns: State-Matched Routing and Contextualized Self-Distillation for Multi-Turn Agents](https://arxiv.org/abs/2608.05219v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [Project2Task: Graph-Guided Project-Level Planning for Autonomous Research](https://arxiv.org/abs/2608.05225v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [Search2Skill: Skill Distillation Beyond Knowledge Boundaries Via Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.05245v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [LUNAR: Benchmarking Personalized Large Language Models on UNiversal User BehAvioR Logs](https://arxiv.org/abs/2608.05246v1) — published/event date: 2026-08-05; accessed: 2026-08-25
- [Hierarchical Graph Memory for LLM Agents with Path-level Localization and Rewrite](https://arxiv.org/abs/2608.05095v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [The Loss Does Not See the Basis, but Adam Does](https://arxiv.org/abs/2608.05136v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [Argus: A General-Purpose Agentic Reasoning Runtime for Long-Horizon Tasks](https://arxiv.org/abs/2608.05144v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [PLoRA: An NDP-Enhanced Pooled-Memory System for Cost-Efficient Multi-LoRA Serving](https://arxiv.org/abs/2608.05483v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
