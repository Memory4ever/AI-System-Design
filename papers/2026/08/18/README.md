# Daily Research — 2026-08-18

**Research Date:** 2026-08-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-17 09:00:00 ～ 2026-08-18 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary
本日报严格覆盖 `2026-08-17 09:00:00` 至 `2026-08-18 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 526 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 10 个候选：4 个 Deep Review、6 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-KV-CACHE` 中由《Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN》暴露的状态/证据边界；`PLATFORM-SECURITY` 中由《Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation》暴露的状态/证据边界；`AGENT-TOOL-CALLING` 中由《SkillEffect: Checked Lowering for Memory-Bounded Agent Tools》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-18 |
| Window End | 2026-08-18 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-18-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-17T09:00:00+08:00 | 2026-08-18T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 526 | SF-2026-ARXIV-2608-16002<br>SF-2026-ARXIV-2608-16068<br>SF-2026-ARXIV-2608-16477<br>SF-2026-ARXIV-2608-16798<br>SF-2026-ARXIV-2608-16843<br>SF-2026-ARXIV-2608-17007<br>SF-2026-ARXIV-2608-17071<br>SF-2026-ARXIV-2608-17095<br>SF-2026-ARXIV-2608-17124<br>SF-2026-ARXIV-2608-17202 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260818/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260818; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260818 |

<!-- coverage:SRC-ARXIV:20260818:start -->submittedDate query filtered to [2026-08-17T09:00:00+08:00, 2026-08-18T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 10 routed families.<!-- coverage:SRC-ARXIV:20260818:end -->

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
| SF-2026-ARXIV-2608-16002 | arXiv:2608.16002v1 | paper-v1:2608.16002 | 2026-W34 | 2026-08-17 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-16002 | self | — | new_in_window | AGENT-REFLECTION | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-16068 | arXiv:2608.16068v1 | paper-v1:2608.16068 | 2026-W34 | 2026-08-17 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-16068 | self | — | new_in_window | AGENT-PROMPT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-16477 | arXiv:2608.16477v1 | paper-v1:2608.16477 | 2026-W34 | 2026-08-17 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-16477 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2608-16477 | yes |
| SF-2026-ARXIV-2608-16798 | arXiv:2608.16798v1 | paper-v1:2608.16798 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-16798 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-16843 | arXiv:2608.16843v1 | paper-v1:2608.16843 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-16843 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2608-16843 | yes |
| SF-2026-ARXIV-2608-17007 | arXiv:2608.17007v1 | paper-v1:2608.17007 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-17007 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2608-17007 | yes |
| SF-2026-ARXIV-2608-17071 | arXiv:2608.17071v1 | paper-v1:2608.17071 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-17071 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-17095 | arXiv:2608.17095v1 | paper-v1:2608.17095 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-17095 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-17124 | arXiv:2608.17124v1 | paper-v1:2608.17124 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-17124 | self | — | new_in_window | MODEL-SAMPLING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-17202 | arXiv:2608.17202v1 | paper-v1:2608.17202 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-17202 | self | — | new_in_window | PLATFORM-SECURITY | Weekly Only — Context | — | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-16002 | RP-c29c72eb1aac3b7b | standard | arXiv:2608.16002v1 | SRC-ARXIV@arXiv:2608.16002v1 | https://arxiv.org/html/2608.16002v1#S4 (4 Methods) | https://arxiv.org/html/2608.16002v1#S5 (5 Experiments) | https://arxiv.org/html/2608.16002v1#S6 (6 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-16002 | complete |
| SF-2026-ARXIV-2608-16068 | RP-59ecafa987289f54 | standard | arXiv:2608.16068v1 | SRC-ARXIV@arXiv:2608.16068v1 | https://arxiv.org/html/2608.16068v1#S3.SS1 (3.1 Problem Formulation) | https://arxiv.org/html/2608.16068v1#S7 (7 Experiments) | https://arxiv.org/html/2608.16068v1#S8 (8 Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-16068 | complete |
| SF-2026-ARXIV-2608-16477 | RP-7069fd4c718a916a | deep | arXiv:2608.16477v1 | SRC-ARXIV@arXiv:2608.16477v1 | https://arxiv.org/html/2608.16477v1 (§§3–4.5: prefetch-window model, online selection, parallel preparation, replanning and contention-aware migration) | https://arxiv.org/html/2608.16477v1 (§§6.1–6.5, Figs. 5–9 and Tables 2–3: three-model A6000/vLLM evaluation, traces, concurrency and ablations) | https://arxiv.org/html/2608.16477v1 (§§4.4–4.5 and §6.3–6.4: prediction availability, stale preparation, target mismatch and joint resource-allocation boundary) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-16477 | complete |
| SF-2026-ARXIV-2608-16798 | RP-cb58b943783431ed | standard | arXiv:2608.16798v1 | SRC-ARXIV@arXiv:2608.16798v1 | https://arxiv.org/html/2608.16798v1#S2.SS3 (2.3 Agentic Reinforcement Learning Algorithms) | https://arxiv.org/html/2608.16798v1#S4 (4 Experiments) | https://arxiv.org/html/2608.16798v1#S5 (5 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-16798 | complete |
| SF-2026-ARXIV-2608-16843 | RP-948925535bbd7168 | deep | arXiv:2608.16843v1 | SRC-ARXIV@arXiv:2608.16843v1 | https://arxiv.org/html/2608.16843v1 (§§2.1–2.5: study population, temporal boundary, multi-label coding and six coding dimensions) | https://arxiv.org/html/2608.16843v1 (§8 and Appendices A–B: quantitative coding of 58 attack and 61 defense records; §9 evaluation recommendations) | https://arxiv.org/html/2608.16843v1 (§2.5 and §§11.1–11.4: methodology limits, preprint drift, multi-label judgment and paper-count-versus-risk boundary) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-16843 | complete |
| SF-2026-ARXIV-2608-17007 | RP-58746e8785b1c91b | deep | arXiv:2608.17007v1 | SRC-ARXIV@arXiv:2608.17007v1 | https://arxiv.org/html/2608.17007v1 (§§2.1–2.3 and §§3.1–3.3: relation registry, independent lowering check, capacity lease and staged publication) | https://arxiv.org/html/2608.17007v1 (§§4.1–4.8 and Appendices A–F: six operator families, five bounded patterns, adversarial proposals and runtime integration) | https://arxiv.org/html/2608.17007v1 (§2.2, §6 and Appendices A/D: trusted-base, parser, plugin coverage, calibration, remote-effect and evaluation-breadth limits) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-17007 | complete |
| SF-2026-ARXIV-2608-17071 | RP-e570ce0ff8f6a7ae | standard | arXiv:2608.17071v1 | SRC-ARXIV@arXiv:2608.17071v1 | https://arxiv.org/html/2608.17071v1#S3 (3. Methodology) | https://arxiv.org/html/2608.17071v1#S4 (4. Experimental Results) | https://arxiv.org/html/2608.17071v1#S5 (5. Analysis and Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-17071 | complete |
| SF-2026-ARXIV-2608-17095 | RP-843ef8ee50caf8d0 | standard | arXiv:2608.17095v1 | SRC-ARXIV@arXiv:2608.17095v1 | https://arxiv.org/html/2608.17095v1#S3 (3 Method) | https://arxiv.org/html/2608.17095v1#S4 (4 Experimental Setup) | https://arxiv.org/html/2608.17095v1#S6 (6 Discussion and Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-17095 | complete |
| SF-2026-ARXIV-2608-17124 | RP-7cd19ff73820bb44 | standard | arXiv:2608.17124v1 | SRC-ARXIV@arXiv:2608.17124v1 | https://arxiv.org/html/2608.17124v1#S3 (3 Method) | https://arxiv.org/html/2608.17124v1#S5 (5 Experimental setup) | https://arxiv.org/html/2608.17124v1#S8 (8 Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-17124 | complete |
| SF-2026-ARXIV-2608-17202 | RP-b920e5aad2846b92 | deep | arXiv:2608.17202v1 | SRC-ARXIV@arXiv:2608.17202v1 | https://arxiv.org/html/2608.17202v1 (§§III–IV: threat model, decoy corpus, attacked-state binding, refusal pin and benign leash) | https://arxiv.org/html/2608.17202v1 (§§V–VII plus Appendices F–N: seven-model registered gates, K=64 attacks, frozen splits and utility checks) | https://arxiv.org/html/2608.17202v1 (§IX plus §VII-H and Appendices L–O: clean escape, benign shift, tell leakage and jailbreak/non-coverage boundaries) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-17202 | complete |

### Source Reviews
<!-- review:SF-2026-ARXIV-2608-16002:start -->
#### From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents

<!-- claim:SF-2026-ARXIV-2608-16002:start -->《From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents》把 `AGENT-REFLECTION` 的问题具体化为：长程依赖使局部错误和置信度沿后续步骤传播。其机制是将轨迹表示为依赖 DAG，结合 behavior/goal 特征传播不确定性并定位早期错误来源；primary v1 的 evaluation 绑定为τ-2、TB2、GAIA、六个开源模型及既有 uncertainty baselines，比较对象为token entropy、单步置信度或只看最终答案的 uncertainty。<!-- claim:SF-2026-ARXIV-2608-16002:end -->

证据支持的范围是：所测长轨迹中图式传播改善 uncertainty 与早期错误检测；不支持的外推是：它能给出因果根因、生产校准或 OOD 下可靠置信度。旧方案仍有成立条件：短、近独立轨迹中单步 entropy 更简单。新机制获得的收益与代价必须一起读取：可定位性换图构建、边推断与校准成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：依赖图错误、相关误差、goal leakage 或分布漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-REFLECTION`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-16002:end -->

<!-- review:SF-2026-ARXIV-2608-16068:start -->
#### CAPO: Constraint-Aware Prompt Optimization for LLM Agents

<!-- claim:SF-2026-ARXIV-2608-16068:start -->《CAPO: Constraint-Aware Prompt Optimization for LLM Agents》把 `AGENT-PROMPT` 的问题具体化为：多个质量/成本约束同时存在且不能靠单一 reward 表达。其机制是维护 prompt rewrite pool，并用 primal-dual 约束和自适应权重在无需 SFT 的情况下搜索可行提示；primary v1 的 evaluation 绑定为DCAPO pool-GRPO rewriter、冻结 task agent 与多 benchmark/模型规模比较，比较对象为人工提示或无约束 prompt optimization。<!-- claim:SF-2026-ARXIV-2608-16068:end -->

证据支持的范围是：作者任务中可找到满足约束并改善目标的 operating points；不支持的外推是：可保证全局最优、安全约束或长期分布稳定。旧方案仍有成立条件：约束少且专家已知规则时人工提示更透明。新机制获得的收益与代价必须一起读取：自动改写换反馈评估、dual 更新和 rewrite 成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：surrogate 偏差、reward gaming、离散局部最优或约束漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-PROMPT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-16068:end -->

<!-- review:SF-2026-ARXIV-2608-16477:start -->
#### Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN

<!-- claim:SF-2026-ARXIV-2608-16477:start -->Pallas 在无线 handover 前预测迁移并主动搬运 KV，vLLM 0.8.5、A6000 与 1Gbps 跨主机实验验证受限路径。预测错误、重规划与网络竞争会把提前迁移变成额外负载，因此它是条件化优化而非默认策略。<!-- claim:SF-2026-ARXIV-2608-16477:end -->

Pallas 在无线 handover 前预测迁移并主动搬运 KV，vLLM 0.8.5、A6000 与 1Gbps 跨主机实验验证受限路径。预测错误、重规划与网络竞争会把提前迁移变成额外负载，因此它是条件化优化而非默认策略。 handover 发生后再迁移 KV 或依赖 forwarding，在移动性不可预测且状态较小时仍是稳妥基线；恢复时间成为尾延迟主项后，Pallas 预测 opportunity window，提前或自适应迁移，并在链路 contention 下重新规划。它以预测、重复传输和共享 WAN 协调成本换更低恢复尾延迟；预测失准、stale transfer 与并发迁移竞争会反噬收益。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了context-conditioned KV state的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、带宽、精度与恢复为长期设计约束。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2608-16477:end -->

<!-- review:SF-2026-ARXIV-2608-16798:start -->
#### ClawGym II: Exploring Black-Box RL on Agent Harness

<!-- claim:SF-2026-ARXIV-2608-16798:start -->《ClawGym II: Exploring Black-Box RL on Agent Harness》把 `TRAIN-RLHF` 的问题具体化为：Agent harness 可能不透明、并发且带持久副作用。其机制是用 sandbox、proxy、prefix tree 与可混合 harness 支持黑盒 coding-agent 的 PPO/GRPO 训练；primary v1 的 evaluation 绑定为Qwen3-30A3B、OpenClaw/Claude Code、JobBench/OfficeQA 与 200–400 步任务，比较对象为白盒单一 harness 或短 horizon tool benchmark。<!-- claim:SF-2026-ARXIV-2608-16798:end -->

证据支持的范围是：作者环境中黑盒长程交互可被记录并用于 RL 训练；不支持的外推是：任意 harness、生产副作用或组件因果性已经闭合。旧方案仍有成立条件：短、可内嵌工具任务中白盒环境成本更低。新机制获得的收益与代价必须一起读取：真实交互覆盖换 sandbox/proxy/tree 基础设施和训练成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：工具调用遗漏、prefix tree 不一致、副作用泄漏、harness drift 或 RL 不稳定。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-RLHF`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-16798:end -->

<!-- review:SF-2026-ARXIV-2608-16843:start -->
#### Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation

<!-- claim:SF-2026-ARXIV-2608-16843:start -->该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。<!-- claim:SF-2026-ARXIV-2608-16843:end -->

该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。 按攻击名称或单组件整理文献，在 pipeline 边界孤立时便于检索；具身 Agent 的感知、推理、动作与环境反馈形成闭环后，同一攻击会跨阶段传播。该研究用 first-compromised boundary 与 lifecycle coding 重建覆盖图，以多标签主观性、preprint drift 和 paper-count 偏差换跨 attack/defense 的结构视图；文献密度不等于 runtime robustness proof。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以policy、隔离与执行边界为长期设计约束。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2608-16843:end -->

<!-- review:SF-2026-ARXIV-2608-17007:start -->
#### SkillEffect: Checked Lowering for Memory-Bounded Agent Tools

<!-- claim:SF-2026-ARXIV-2608-17007:start -->SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。<!-- claim:SF-2026-ARXIV-2608-17007:end -->

SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。 直接执行模型生成的程序，或只靠 cgroup 在超限后 kill，在工具很小、输入可信且结果易重放时成本最低；当正确程序也会因 eager materialization 超过 per-call cap，SkillEffect 把控制点前移到 dispatch 前的 relation recovery、independent lowering check、capacity lease 与 staged publication。它以每类计算都需 audited plugin、checker/VM TCB 和 preflight 扫描换可恢复的 bounded execution；未知 relation、远程副作用与 parser DoS 仍必须 fail closed。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了动作提案与工具结果的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以schema、权限与副作用为长期设计约束。
- Knowledge owner：`AGENT-TOOL-CALLING`；Disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2608-17007:end -->

<!-- review:SF-2026-ARXIV-2608-17071:start -->
#### KernelArc: A Multi-Agent Framework for GPU Kernel Optimization

<!-- claim:SF-2026-ARXIV-2608-17071:start -->《KernelArc: A Multi-Agent Framework for GPU Kernel Optimization》把 `INFER-TENSORRT-LLM` 的问题具体化为：异构 kernel 与硬件空间使单一路径易陷入平台期。其机制是多个策略 Agent 并行搜索 kernel，只共享结论性记忆，并用确定性 guard 和 plateau detector 控制继续探索；primary v1 的 evaluation 绑定为H100/B200 的 SOL-ExecBench snapshot，固定预算，并与单 Agent/人工搜索设置比较，比较对象为单 Agent 或人工逐 kernel 优化。<!-- claim:SF-2026-ARXIV-2608-17071:end -->

证据支持的范围是：作者 snapshot 中多策略搜索可在固定预算内找到更优候选；不支持的外推是：组件贡献、任意硬件泛化或长期生产维护成本已被证明。旧方案仍有成立条件：kernel 数量少或专家已有模板时人工计划更稳。新机制获得的收益与代价必须一起读取：搜索覆盖换多 Agent 推理、协调和验证成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：benchmark 泄漏、过拟合、guard 漏检、共享信息损失或错误停机。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供编译后的执行计划的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17071:end -->

<!-- review:SF-2026-ARXIV-2608-17095:start -->
#### Inference-Time Attention Steering for Vision-Language-Action Driving Models

<!-- claim:SF-2026-ARXIV-2608-17095:start -->《Inference-Time Attention Steering for Vision-Language-Action Driving Models》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：部署后需要低成本干预而不能重新训练模型。其机制是在 detector 定位视觉 token 后，对 pre-softmax attention 加方向性 bias，并以 fail-open runtime hook 无训练介入；primary v1 的 evaluation 绑定为Alpamayo-R1/Qwen3-VL、50 个合成换道场景，以及 zero-bias、剂量和层位 ablation，比较对象为重新训练 safety policy 或完全不做 runtime steering。<!-- claim:SF-2026-ARXIV-2608-17095:end -->

证据支持的范围是：所测场景中能改变轨迹并保留显式 reasoning path；不支持的外推是：真实道路安全、避障正确性或任意 actor/direction 可迁移。旧方案仍有成立条件：已覆盖场景且可重训时端到端安全训练更完整。新机制获得的收益与代价必须一起读取：快速 steering 换 detector、hook、方向和剂量校准。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：漏检、朝向错误、clamp 饱和、OOD 或隐藏状态漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17095:end -->

<!-- review:SF-2026-ARXIV-2608-17124:start -->
#### A decodability criterion predicts when hidden-state selection beats majority voting in large language models

<!-- claim:SF-2026-ARXIV-2608-17124:start -->《A decodability criterion predicts when hidden-state selection beats majority voting in large language models》把 `MODEL-SAMPLING` 的问题具体化为：相关错误会使更多样本共同走向错误答案。其机制是从答案 token 的隐藏状态训练 leakage-free 线性 gate，判断何时 select 单答案、何时 majority vote；primary v1 的 evaluation 绑定为一般与医疗任务、中等/困难/未见科学题，对比 majority vote 和泄漏 probe，比较对象为固定 majority vote 或用同分布泄漏特征决定聚合。<!-- claim:SF-2026-ARXIV-2608-17124:end -->

证据支持的范围是：所测 held-out 任务中 hidden-state decodability 可预测 select-vote 策略；不支持的外推是：该分数是通用 correctness probability 或能识别所有未知问题。旧方案仍有成立条件：样本独立且错误不相关时 majority vote 仍稳健。新机制获得的收益与代价必须一起读取：更少无效采样换标签、校准和 gate 阈值维护。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：训练泄漏、shift、候选中无正确答案或阈值失配。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MODEL-SAMPLING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17124:end -->

<!-- review:SF-2026-ARXIV-2608-17202:start -->
#### Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

<!-- claim:SF-2026-ARXIV-2608-17202:start -->Fool's Gold 在 safety-removal attack 的可微模拟中训练 decoy，使拒答方向被移除后输出流畅但关键步骤错误，同时以 refusal pin 与 benign leash 约束 clean state。多模型实验只支持最初发布权重、特定 abliteration 与化生危害设置；仍存在 clean escape tail、benign 偏移，并且它不处理 in-context jailbreak。该机制用攻击者验证成本换防御，但同时引入 deliberate falsehood 的治理与误用风险。<!-- claim:SF-2026-ARXIV-2608-17202:end -->

Fool's Gold 在 safety-removal attack 的可微模拟中训练 decoy，使拒答方向被移除后输出流畅但关键步骤错误，同时以 refusal pin 与 benign leash 约束 clean state。多模型实验只支持最初发布权重、特定 abliteration 与化生危害设置；仍存在 clean escape tail、benign 偏移，并且它不处理 in-context jailbreak。该机制用攻击者验证成本换防御，但同时引入 deliberate falsehood 的治理与误用风险。 权重受控时加强 refusal policy 仍是直接防线；开放权重允许 abliteration 移除 refusal 后，单靠同一状态已不足。Fool’s Gold 接受 stripability，把 decoy 绑定到被攻击后的模型状态，以额外 verification cost 换攻击者判断成本；deliberate falsehood、clean escape、benign shift 仍存在，也不证明能抵御 jailbreak 或再次 fine-tune。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以policy、隔离与执行边界为长期设计约束。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17202:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-16477 | wireless-handover KV migration using ShareGPT requests and nuScenes/SNOB-5G traces | Meta-Llama-3-8B, Qwen3-14B and Qwen3-32B-Instruct-AWQ served by vLLM 0.8.5 | two NVIDIA RTX A6000 48GB GPUs across hosts; 1-Gbps full-duplex Ethernet | FP16/BF16 KV for Llama/Qwen; AWQ checkpoint for Qwen3-32B | 500–4500-token contexts; 1000-token repeated-handover prompts; 2000-token concurrency context | decoded tokens throughout handover replay; exact generation count Not Disclosed | one request per single-handover sample; ten repetitions per concurrency configuration | K=1–4 concurrent migrations; R=0–3 resident sessions; joint K=2/R=2 | 100-ms ITL objective plus SIT/ITL average and tail | five recovery/forwarding strategies, controlled goodput, SNOB-5G and nuScenes trace replay |
| SF-2026-ARXIV-2608-16843 | systematic coding of 58 attack and 61 defense studies through 2026-08-15 | foundation-model-powered embodied-agent literature; no evaluated learner model | Not Required — literature study | Not Required — literature study | Not Disclosed — corpus size is not a model input length | multi-label taxonomy and quantitative research-landscape tables; not a generated-token length | Not Required — literature study | Not Required — literature study | research-density and coverage map, not incident probability | §2 coding methodology, Appendices A–C coding tables and §11 anti-overgeneralization rules |
| SF-2026-ARXIV-2608-17007 | memory-bounded local Agent tool dispatch across CSV, FASTA, FCS, Zarr, XLSX and audit Top-k | registered checked-relation runtime is the evaluated mechanism; model-generation arms use Qwen2.5-14B-Instruct-AWQ or Mistral-7B | Apple M5 MacBook Air (10 CPU/16GiB); Linux 6.8 aarch64 VM (4 vCPU); formal containers 2 vCPU with cgroup v2/no swap; generation on one A800-80GB PCIe; uncapped control 112 vCPU/~979.5GiB RAM | Not Required — checked execution semantics and resource caps, not model numeric precision, are the evaluated mechanism | operator-specific immutable inputs; up to two-million-row table examples | registered staged result with postcondition | single isolated tool transaction plus shared-capacity lease experiments | lease-controlled concurrent transactions; normalized request concurrency Not Disclosed in v1 | hard-cap completion, no limit events/swap and postcondition pass | exact task verifier, adversarial proposal rejection and cap-feedback protocols |
| SF-2026-ARXIV-2608-17202 | CBRNE safety-removal/abliteration attacks, attacked-state decoy defense, frozen/held-out strata and repeated consensus through K=64 | Qwen3.5-9B, Qwen3.5-27B, Qwen3.5-122B, Qwen3-14B, gpt-oss-20b, gemma-4-31B and GLM-4.5-Air | Not Disclosed — v1 does not identify the accelerator | Not Disclosed — v1 does not state a normalized precision | Not Disclosed — prompt strata and corpus counts are not token length | Not Disclosed — v1 does not normalize per-response length | Not Disclosed — K=64 is repeated sampling, not request batch | Not Disclosed — no serving-concurrency benchmark | Not Required as an operational SLO; registered efficacy, benign-behavior and capability gates | fatal-flaw judge, accepted-attack conjunction, frozen split, expert audit and StrongReject/HarmBench/MMLU/GSM8K/WMDP/IFEval controls |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-17202 | score_7_9<br>forced_review | selected | DA-20260818-2608-17202 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision | analysis:DA-20260818-2608-17202 |
| SF-2026-ARXIV-2608-17007 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260818-2608-17007 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=tool intent execution becomes checked lowering with capacity lease and bounded publication | analysis:DA-20260818-2608-17007 |
| SF-2026-ARXIV-2608-16843 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260818-2608-16843 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=embodied security is partitioned by first-compromised boundary across perception and action | analysis:DA-20260818-2608-16843 |
| SF-2026-ARXIV-2608-16477 | score_7_9<br>potential_books_delta | not_selected | — | — | 已完成独立 Deep Source Review；本 family 为 override=none、V2=9/9 (3/3/3)，排在选中阈值为 override=release_security_contract、V2=9/9 (3/3/3)之后；未选只限制长叙事数量，不降低证据状态或 Books Decision；pre-Books delta=cross-node KV reuse gains semantic identity, lookup and stale-state failure policy | analysis-decision:SF-2026-ARXIV-2608-16477 |

<!-- analysis-decision:SF-2026-ARXIV-2608-16477:start -->《Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN》已完成独立 Deep Source Review 与 Books Decision；未进入本窗口三个长叙事单元只表示逐 family 的优先级取舍，不降低证据状态，也不由其他 family 代替。<!-- analysis-decision:SF-2026-ARXIV-2608-16477:end -->

<!-- analysis:DA-20260818-2608-17202:start -->
### Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models

Fool's Gold 在 safety-removal attack 的可微模拟中训练 decoy，使拒答方向被移除后输出流畅但关键步骤错误，同时以 refusal pin 与 benign leash 约束 clean state。多模型实验只支持最初发布权重、特定 abliteration 与化生危害设置；仍存在 clean escape tail、benign 偏移，并且它不处理 in-context jailbreak。该机制用攻击者验证成本换防御，但同时引入 deliberate falsehood 的治理与误用风险。 权重受控时加强 refusal policy 仍是直接防线；开放权重允许 abliteration 移除 refusal 后，单靠同一状态已不足。Fool’s Gold 接受 stripability，把 decoy 绑定到被攻击后的模型状态，以额外 verification cost 换攻击者判断成本；deliberate falsehood、clean escape、benign shift 仍存在，也不证明能抵御 jailbreak 或再次 fine-tune。

<!-- analysis:DA-20260818-2608-17202:end -->

<!-- analysis:DA-20260818-2608-17007:start -->
### SkillEffect: Checked Lowering for Memory-Bounded Agent Tools

SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。 直接执行模型生成的程序，或只靠 cgroup 在超限后 kill，在工具很小、输入可信且结果易重放时成本最低；当正确程序也会因 eager materialization 超过 per-call cap，SkillEffect 把控制点前移到 dispatch 前的 relation recovery、independent lowering check、capacity lease 与 staged publication。它以每类计算都需 audited plugin、checker/VM TCB 和 preflight 扫描换可恢复的 bounded execution；未知 relation、远程副作用与 parser DoS 仍必须 fail closed。

<!-- analysis:DA-20260818-2608-17007:end -->

<!-- analysis:DA-20260818-2608-16843:start -->
### Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation

该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。 按攻击名称或单组件整理文献，在 pipeline 边界孤立时便于检索；具身 Agent 的感知、推理、动作与环境反馈形成闭环后，同一攻击会跨阶段传播。该研究用 first-compromised boundary 与 lifecycle coding 重建覆盖图，以多标签主观性、preprint drift 和 paper-count 偏差换跨 attack/defense 的结构视图；文献密度不等于 runtime robustness proof。

<!-- analysis:DA-20260818-2608-16843:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-16477 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L399 | books/part-02-model/19-kv-cache.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-16477 | delta:SF-2026-ARXIV-2608-16477 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-16477 |
| SF-2026-ARXIV-2608-16843 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L612 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2608-16843 | delta:SF-2026-ARXIV-2608-16843 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2608-16843 |
| SF-2026-ARXIV-2608-17007 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L14<br>books/part-07-agent/78-tool-calling.md#L180 | books/part-07-agent/77-memory.md#L14<br>books/part-07-agent/81-workflow.md#L14 | existing:SF-2026-ARXIV-2608-17007 | delta:SF-2026-ARXIV-2608-17007 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-17007 |

<!-- books-review:SF-2026-ARXIV-2608-16477:start --><!-- existing:SF-2026-ARXIV-2608-16477:start -->现有中心命题：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。<!-- existing:SF-2026-ARXIV-2608-16477:end --><!-- delta:SF-2026-ARXIV-2608-16477:start -->Pallas 在无线 handover 前预测迁移并主动搬运 KV，vLLM 0.8.5、A6000 与 1Gbps 跨主机实验验证受限路径。预测错误、重规划与网络竞争会把提前迁移变成额外负载，因此它是条件化优化而非默认策略。<!-- delta:SF-2026-ARXIV-2608-16477:end -->与上述中心命题相比，这个 family 的新增证据是：Pallas 在无线 handover 前预测迁移并主动搬运 KV，vLLM 0.8.5、A6000 与 1Gbps 跨主机实验验证受限路径。预测错误、重规划与网络竞争会把提前迁移变成额外负载，因此它是条件化优化而非默认策略。 该 delta 已落在《第45章 为什么 KV Cache 能提速》的正文机制锚点；语义相邻边界为 MODEL-KV-CACHE：KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-16477:end -->

<!-- books-review:SF-2026-ARXIV-2608-16843:start --><!-- existing:SF-2026-ARXIV-2608-16843:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2608-16843:end --><!-- delta:SF-2026-ARXIV-2608-16843:start -->该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。<!-- delta:SF-2026-ARXIV-2608-16843:end -->与上述中心命题相比，这个 family 的新增证据是：该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-16843:end -->

<!-- books-review:SF-2026-ARXIV-2608-17007:start --><!-- existing:SF-2026-ARXIV-2608-17007:start -->现有中心命题：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。<!-- existing:SF-2026-ARXIV-2608-17007:end --><!-- delta:SF-2026-ARXIV-2608-17007:start -->SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。<!-- delta:SF-2026-ARXIV-2608-17007:end -->与上述中心命题相比，这个 family 的新增证据是：SkillEffect 不信任模型生成的 tool program，而由独立 checker 从 immutable input 重建 source relation、bounded IR 与 live-set bound；只有唯一匹配、容量 lease 和 registered postcondition 都通过才 staged publish。六类 operator、五种 execution pattern 与 adversarial proposal 只证明已注册 plugin 的 hard-cap execution；未知 relation、parser denial-of-service、远程不可逆副作用和多租户 preflight 仍明确在保证外。 该 delta 已落在《第78章 Tool Calling》的正文机制锚点；语义相邻边界为 AGENT-MEMORY：Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。；AGENT-WORKFLOW：Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-17007:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260818-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260818; semantic-review:SA-20260818-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260818-EVIDENCE | fresh-context:contract-adversary | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-16002; review:SF-2026-ARXIV-2608-16068; review:SF-2026-ARXIV-2608-16477; review:SF-2026-ARXIV-2608-16798; review:SF-2026-ARXIV-2608-16843; review:SF-2026-ARXIV-2608-17007; review:SF-2026-ARXIV-2608-17071; review:SF-2026-ARXIV-2608-17095; review:SF-2026-ARXIV-2608-17124; review:SF-2026-ARXIV-2608-17202; semantic-review:SA-20260818-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260818-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2608-16477; analysis:DA-20260818-2608-16843; analysis:DA-20260818-2608-17007; analysis:DA-20260818-2608-17202; semantic-review:SA-20260818-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260818-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-16477; books-review:SF-2026-ARXIV-2608-16843; books-review:SF-2026-ARXIV-2608-17007; review:SF-2026-ARXIV-2608-16002; review:SF-2026-ARXIV-2608-16068; review:SF-2026-ARXIV-2608-16798; review:SF-2026-ARXIV-2608-17071; review:SF-2026-ARXIV-2608-17095; review:SF-2026-ARXIV-2608-17124; review:SF-2026-ARXIV-2608-17202; semantic-review:SA-20260818-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260818-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260818-COVERAGE:end -->
<!-- semantic-review:SA-20260818-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260818-EVIDENCE:end -->
<!-- semantic-review:SA-20260818-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260818-SELECTION:end -->
<!-- semantic-review:SA-20260818-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260818-BOOKS:end -->

## 8. Ignored Noise

526 条 arXiv v1 中有 516 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：3 个 `Integrate`、0 个 `No Change — Existing Coverage`、7 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/18/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-06-ai-infrastructure/72-security.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-07-agent/78-tool-calling.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents](https://arxiv.org/abs/2608.16002v1) — published/event date: 2026-08-17; accessed: 2026-08-25
- [CAPO: Constraint-Aware Prompt Optimization for LLM Agents](https://arxiv.org/abs/2608.16068v1) — published/event date: 2026-08-17; accessed: 2026-08-25
- [Pallas: A Proactive KV Cache Migration Framework for LLM Inference in AI-RAN](https://arxiv.org/abs/2608.16477v1) — published/event date: 2026-08-17; accessed: 2026-08-25
- [ClawGym II: Exploring Black-Box RL on Agent Harness](https://arxiv.org/abs/2608.16798v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [Security of Foundation-Model-Powered Embodied Agents: Attack Surfaces, Attacks, Defenses, and Evaluation](https://arxiv.org/abs/2608.16843v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [SkillEffect: Checked Lowering for Memory-Bounded Agent Tools](https://arxiv.org/abs/2608.17007v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [KernelArc: A Multi-Agent Framework for GPU Kernel Optimization](https://arxiv.org/abs/2608.17071v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [Inference-Time Attention Steering for Vision-Language-Action Driving Models](https://arxiv.org/abs/2608.17095v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [A decodability criterion predicts when hidden-state selection beats majority voting in large language models](https://arxiv.org/abs/2608.17124v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models](https://arxiv.org/abs/2608.17202v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
