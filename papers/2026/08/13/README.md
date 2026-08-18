# Daily Research — 2026-08-13

**Research Date:** 2026-08-13

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-12 09:00:00 ～ 2026-08-13 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-12 09:00:00` 至 `2026-08-13 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 444 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 8 个候选：0 个 Deep Review、8 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`AGENT-WORKFLOW` 中由《Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents》暴露的状态/证据边界；`INFER-GPU-MEMORY` 中由《Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE Inference》暴露的状态/证据边界；`MULTIMODAL-EMBODIED-VLA` 中由《Foresight Without Seeing: Latent Futures for World Action Models》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-13 |
| Window End | 2026-08-13 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-13-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-12T09:00:00+08:00 | 2026-08-13T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 444 | SF-2026-ARXIV-2608-11605<br>SF-2026-ARXIV-2608-11632<br>SF-2026-ARXIV-2608-11671<br>SF-2026-ARXIV-2608-11738<br>SF-2026-ARXIV-2608-11775<br>SF-2026-ARXIV-2608-11888<br>SF-2026-ARXIV-2608-12103<br>SF-2026-ARXIV-2608-12629 | page count=7 snapshot files; final_cursor=end; daily-window total=444; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-13T09:00:00+08:00 | coverage:SRC-ARXIV:20260813 | — |
| SRC-GITHUB-COMMIT | 2026-08-12T09:00:00+08:00 | 2026-08-13T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-11775: https://api.github.com/repos/kyrkewood/sleeping-agent/commits?until=2026-08-12T08:19:15Z&per_page=1; per-family event-time recovery | checked | 1 | SF-2026-ARXIV-2608-11775 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-13T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260813 | — |

<!-- coverage:SRC-ARXIV:20260813:start -->submittedDate query filtered to [2026-08-12T09:00:00+08:00, 2026-08-13T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 8 routed families.<!-- coverage:SRC-ARXIV:20260813:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260813:start -->GitHub Commit API recovered and froze 1 repository commit(s): SF-2026-ARXIV-2608-11775: repository=kyrkewood/sleeping-agent; until=2026-08-12T08:19:15Z; sha=2a8e2c00f625b27e4de7d85e334a773a191d3df0; commit_timestamp=2026-05-11T12:53:07Z; commit_url=https://github.com/kyrkewood/sleeping-agent/commit/2a8e2c00f625b27e4de7d85e334a773a191d3df0; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260813:end -->

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
| SF-2026-ARXIV-2608-11605 | arXiv:2608.11605v1 | paper-v1:2608.11605 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11605 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11632 | arXiv:2608.11632v1 | paper-v1:2608.11632 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11632 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11671 | arXiv:2608.11671v1 | paper-v1:2608.11671 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11671 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11738 | arXiv:2608.11738v1 | paper-v1:2608.11738 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 1 | 3 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11738 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11775 | arXiv:2608.11775v1 | paper-v1:2608.11775 | 2026-W33 | 2026-08-12 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11775 | self | — | new_in_window | AGENT-CONTEXT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11888 | arXiv:2608.11888v1 | paper-v1:2608.11888 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11888 | self | — | new_in_window | AGENT-PLATFORM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-12103 | arXiv:2608.12103v1 | paper-v1:2608.12103 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-12103 | self | — | new_in_window | INFER-GPU-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-12629 | arXiv:2608.12629v1 | paper-v1:2608.12629 | 2026-W33 | 2026-08-13 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-12629 | self | — | new_in_window | INFER-TENSORRT-LLM | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-11605 | RP-e83e208ef3e55652 | standard | arXiv:2608.11605v1 | SRC-ARXIV@arXiv:2608.11605v1 | https://arxiv.org/html/2608.11605v1#S3 (3 Method) | https://arxiv.org/html/2608.11605v1#S4 (4 Experiments) | https://arxiv.org/html/2608.11605v1#S5 (5 Limitations and Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11605 | complete |
| SF-2026-ARXIV-2608-11632 | RP-05dd644bc5ab1177 | standard | arXiv:2608.11632v1 | SRC-ARXIV@arXiv:2608.11632v1 | https://arxiv.org/html/2608.11632v1#S2 (2 System Model and Contract) | https://arxiv.org/html/2608.11632v1#S5 (5 Evaluation) | https://arxiv.org/html/2608.11632v1#S7 (7 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11632 | complete |
| SF-2026-ARXIV-2608-11671 | RP-ab5e909867981c13 | standard | arXiv:2608.11671v1 | SRC-ARXIV@arXiv:2608.11671v1 | https://arxiv.org/html/2608.11671v1#S3 (3 Methodology) | https://arxiv.org/html/2608.11671v1#S4 (4 Experiments) | https://arxiv.org/html/2608.11671v1#S5 (5 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11671 | complete |
| SF-2026-ARXIV-2608-11738 | RP-334c059638f41e64 | standard | arXiv:2608.11738v1 | SRC-ARXIV@arXiv:2608.11738v1 | https://arxiv.org/html/2608.11738v1#S4 (IV Method) | https://arxiv.org/html/2608.11738v1#S5 (V Experiment) | https://arxiv.org/html/2608.11738v1#S6 (VI Limitations and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11738 | complete |
| SF-2026-ARXIV-2608-11775 | RP-619c1a07ae029a4b | standard | arXiv:2608.11775v1 | SRC-ARXIV@arXiv:2608.11775v1; SRC-GITHUB-COMMIT@https://github.com/kyrkewood/sleeping-agent/commit/2a8e2c00f625b27e4de7d85e334a773a191d3df0 | https://arxiv.org/html/2608.11775v1#S4.SS1 (4.1 Design Principles) | https://arxiv.org/html/2608.11775v1#S5 (5 Experimental Setup) | https://arxiv.org/html/2608.11775v1#S7 (7 Discussion) | https://github.com/kyrkewood/sleeping-agent/commit/2a8e2c00f625b27e4de7d85e334a773a191d3df0 (latest commit before arXiv v1; 2026-05-11T12:53:07Z) | claim:SF-2026-ARXIV-2608-11775 | complete |
| SF-2026-ARXIV-2608-11888 | RP-addad354548c511e | standard | arXiv:2608.11888v1 | SRC-ARXIV@arXiv:2608.11888v1 | https://arxiv.org/html/2608.11888v1#S3 (III Methodology) | https://arxiv.org/html/2608.11888v1#S6.SS2 (VI-B Evaluation Setup) | https://arxiv.org/html/2608.11888v1#S7 (VII Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11888 | complete |
| SF-2026-ARXIV-2608-12103 | RP-d7d4cf3ff6313274 | standard | arXiv:2608.12103v1 | SRC-ARXIV@arXiv:2608.12103v1 | https://arxiv.org/html/2608.12103v1#S4 (4. The Capacity Response T(C)) | https://arxiv.org/html/2608.12103v1#S9 (9. Design Consequences, Validated in Engines) | https://arxiv.org/html/2608.12103v1#S10 (10. Threats to Validity, and a Methods Ledger) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-12103 | complete |
| SF-2026-ARXIV-2608-12629 | RP-88fbf37a161f94dd | standard | arXiv:2608.12629v1 | SRC-ARXIV@arXiv:2608.12629v1 | https://arxiv.org/html/2608.12629v1#S4 (4 Agent workflow) | https://arxiv.org/html/2608.12629v1#S5 (5 Evaluation) | https://arxiv.org/html/2608.12629v1#S8 (8 Discussion and conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-12629 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-11605:start -->
#### Foresight Without Seeing: Latent Futures for World Action Models

<!-- claim:SF-2026-ARXIV-2608-11605:start -->《Foresight Without Seeing: Latent Futures for World Action Models》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：控制既需要 dynamics 又不能承担 video denoising latency。其机制是Future-KV 对当前视觉 latent 加 stochastic future slots 做一次 Video-DiT prefill，并在 action denoising 复用逐层 KV；primary v1 的 evaluation 绑定为LIBERO 与 LIBERO-Plus；standard/accelerated ForeWAM；无 embodied pretraining，比较对象为explicit-future WAM 与 direct-policy WAM classes。<!-- claim:SF-2026-ARXIV-2608-11605:end -->

证据支持的范围是：所测模拟任务中无需解码未来视频即可给 Action DiT latent predictive context；不支持的外推是：真实开放世界未来正确、latent 因果可解释或跨机器人泛化。旧方案仍有成立条件：在线生成 future video 或纯 direct policy；前者显式、后者快速。新机制获得的收益与代价必须一起读取：部署省视频生成，换训练期 future observations/teacher 和 latent bottleneck。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：future 分叉、register collapse、contact/OOD dynamics 或 KV 过期。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11605:end -->

<!-- review:SF-2026-ARXIV-2608-11632:start -->
#### Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents

<!-- claim:SF-2026-ARXIV-2608-11632:start -->《Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents》把 `AGENT-WORKFLOW` 的问题具体化为：并发候选、stale overwrite、未审计 exposure 与自授权风险。其机制是off-commit candidate evaluation 加 exact predecessor proposal，在短 activation 中重验 authority/freshness/effect 并写 receipt；primary v1 的 evaluation 绑定为bounded executable model：2808230 states、5526474 state-changing transitions，比较对象为storage-retention-only / unmediated updates。<!-- claim:SF-2026-ARXIV-2608-11632:end -->

证据支持的范围是：该有界模型和不变量内未发现 activation protocol violation；不支持的外推是：实现无 bug、业务语义正确、真实外部副作用可事务化或无界安全。旧方案仍有成立条件：只保存版本并允许直接写 authoritative state；简单但暴露窗口大。新机制获得的收益与代价必须一起读取：authoritative lineage 换串行化、defer/quarantine latency 与可用性。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：模型外状态、pre-commit 外部副作用、伪造 authority 或 unbounded concurrency。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供可恢复 workflow state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-WORKFLOW`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11632:end -->

<!-- review:SF-2026-ARXIV-2608-11671:start -->
#### StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2608-11671:start -->《StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：scene/view/object/embodiment OOD 且需高频实时控制。其机制是离线把 raw demo 结构化为 plan/subgoal/verbalized 3D motion，test-time 检索一个 demo 指导 action expert；primary v1 的 evaluation 绑定为VLA-Arena、LIBERO、LIBERO-Plus 与 real-robot OOD demos，比较对象为pi_0.5 与 LingBot-VLA。<!-- claim:SF-2026-ARXIV-2608-11671:end -->

证据支持的范围是：报告 snapshot 中结构化单 demo 提升任务分且 action-only inference 无 language latency；不支持的外推是：任意 OOD/embodiment、单 demo 充分或自动结构化无错。旧方案仍有成立条件：为新场景收集数据并 fine-tune，或直接模仿 raw trajectory。新机制获得的收益与代价必须一起读取：免在线 fine-tune 换离线标注、demo retrieval 和双目标训练。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：检错 demo、plan/3D verbalization 错、需多示例或动作语义不一致。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11671:end -->

<!-- review:SF-2026-ARXIV-2608-11738:start -->
#### Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System

<!-- claim:SF-2026-ARXIV-2608-11738:start -->《Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：极端尺度、任意航向和高密度对象需要域工具与自适应搜索。其机制是UAVQA-Bench 加 UAV-MAS：按 query 路由视觉工具、迭代校验推理并按难度调 search depth；primary v1 的 evaluation 绑定为1500 QA、13 UAV datasets、6 capabilities、16 tasks；open/closed MLLM 与 agents，比较对象为Gemini 3 Pro 与对应 32B/8B base model。<!-- claim:SF-2026-ARXIV-2608-11738:end -->

证据支持的范围是：该 benchmark 中暴露三类 failure，UAV-MAS 在所测配置提高 overall accuracy；不支持的外推是：真实飞行安全、benchmark 外能力或三个模块的独立因果贡献。旧方案仍有成立条件：碎片化窄任务与静态通用工具集；域简单时成本更低。新机制获得的收益与代价必须一起读取：accuracy 换工具调用、迭代校验/search latency 与更大 error surface。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：tool mismatch、validator 漏错、difficulty 估错、search runaway 或 contamination。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 3 / Durability 1 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11738:end -->

<!-- review:SF-2026-ARXIV-2608-11775:start -->
#### The Sleeping Agent: What Gist-Based Context Compression Loses and Why

<!-- claim:SF-2026-ARXIV-2608-11775:start -->《The Sleeping Agent: What Gist-Based Context Compression Loses and Why》把 `AGENT-CONTEXT` 的问题具体化为：长上下文需压缩，但 task 对关系/事件和精确日期依赖不同。其机制是按 salience 分层，只对中优先内容做 structured gist，并用 prompt 显式保留 temporal expressions；primary v1 的 evaluation 绑定为LoCoMo 10 conversations；1935 matched questions，主 aggregate 1501，temperature 0，比较对象为full context、truncation 与 original gist compression。<!-- claim:SF-2026-ARXIV-2608-11775:end -->

证据支持的范围是：该 matched set 中 gist 优于 truncation，但时间损伤可由保留指令恢复；不支持的外推是：所有长程 agent/memory 或真实 token-budget/latency 最优。旧方案仍有成立条件：直接 truncation 或不分类 gist；时间细节不重要时足够。新机制获得的收益与代价必须一起读取：更小 context 换细节丢失，保留时间表达又占压缩余量。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：salience 排错、隐式时间未识别、排除 adversarial 类别或 prompt/model 漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-CONTEXT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11775:end -->

<!-- review:SF-2026-ARXIV-2608-11888:start -->
#### Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents

<!-- claim:SF-2026-ARXIV-2608-11888:start -->《Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents》把 `AGENT-PLATFORM` 的问题具体化为：复用 guidance 会把 checklist/recipe 变成强制流程并改变路径。其机制是把 skill-guided run 与 no-skill/semantic-matched run 配对做 differential attribution，并生成证据报告；primary v1 的 evaluation 绑定为SkillsBench 与 SWE-Skills-Bench；307 attributed failures，比较对象为no-skill 或 semantically matched reference run。<!-- claim:SF-2026-ARXIV-2608-11888:end -->

证据支持的范围是：这些配对中相关 skill 可诱发功能失败/成本回归，过度验证是主要类别；不支持的外推是：skill 是唯一因果、所有相关 skill 有害或 taxonomy 覆盖生产。旧方案仍有成立条件：只看 aggregate success/token；规模小但便宜。新机制获得的收益与代价必须一起读取：可解释 attribution 换配对运行成本和 reference 选择假设。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：reference 不等价、stochasticity、多 skill interaction 或隐藏环境差异。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-PLATFORM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11888:end -->

<!-- review:SF-2026-ARXIV-2608-12103:start -->
#### Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE Inference

<!-- claim:SF-2026-ARXIV-2608-12103:start -->《Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE Inference》把 `INFER-GPU-MEMORY` 的问题具体化为：expert pool 超 DRAM 且 routing locality 随域变化。其机制是让 OS page cache 管 expert tier/eviction，以 router trace 做 full-pool replay，model knowledge 仅作 admission advice；primary v1 的 evaluation 绑定为GH200；3 个 MoE、128–896 experts/layer，含 1.45TB pool；三种 capacity enforcement，比较对象为same-domain oracle frequency table 与 untuned kernel LRU。<!-- claim:SF-2026-ARXIV-2608-12103:end -->

证据支持的范围是：该 GH200/trace regime 中 kernel LRU 在等内存墙接近 oracle；不支持的外推是：所有 OS/硬件/workload、低 tail latency 或 page cache 总优。旧方案仍有成立条件：user-space expert-granular pinned tiers；可控但需额外 policy。新机制获得的收益与代价必须一起读取：少一套控制面换 OS policy/page granularity/回收可观测性。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：低 locality/off-domain thrash、reclaim 差异、layout 不匹配或竞争。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供多层内存状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-GPU-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-12103:end -->

<!-- review:SF-2026-ARXIV-2608-12629:start -->
#### CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution

<!-- claim:SF-2026-ARXIV-2608-12629:start -->《CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution》把 `INFER-TENSORRT-LLM` 的问题具体化为：前沿 schedule 复杂，粗 error/correctness/timing 反馈不足以迭代。其机制是agent 写 typed hardware-explicit CAKE IR，配 verifier、cost model 与局部诊断，失败反哺 IR/harness；primary v1 的 evaluation 绑定为B200 hidden Flash-KMeans、Kimi Delta Attention、KNN/KMeans 400+ shapes，比较对象为tuned FlashML、direct CUDA/PTX 与 official FlashKDA。<!-- claim:SF-2026-ARXIV-2608-12629:end -->

证据支持的范围是：所测 kernels/shapes 中 compiler-agent co-design 可生成达到已调 baseline 的实现；不支持的外推是：所有 kernel 可复现、跨 vendor 泛化、PR 已合入或 cost model 永远准确。旧方案仍有成立条件：直接写 CUDA/PTX 或黑盒 compiler；专家足够时直接但反馈粗。新机制获得的收益与代价必须一起读取：可控搜索/验证换自有 IR/compiler/harness 与 vendor-specific 维护。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：verifier blind spot、cost drift、shape overfit 或 dispatcher 泛化失败。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供编译后的执行计划的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-12629:end -->

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
| SA-20260813-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260813; coverage:SRC-GITHUB-COMMIT:20260813; semantic-review:SA-20260813-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260813-EVIDENCE | fresh-context:contract-adversary | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-11605; review:SF-2026-ARXIV-2608-11632; review:SF-2026-ARXIV-2608-11671; review:SF-2026-ARXIV-2608-11738; review:SF-2026-ARXIV-2608-11775; review:SF-2026-ARXIV-2608-11888; review:SF-2026-ARXIV-2608-12103; review:SF-2026-ARXIV-2608-12629; semantic-review:SA-20260813-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260813-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis-decision:NO-DEEP; semantic-review:SA-20260813-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260813-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; review:SF-2026-ARXIV-2608-11605; review:SF-2026-ARXIV-2608-11632; review:SF-2026-ARXIV-2608-11671; review:SF-2026-ARXIV-2608-11738; review:SF-2026-ARXIV-2608-11775; review:SF-2026-ARXIV-2608-11888; review:SF-2026-ARXIV-2608-12103; review:SF-2026-ARXIV-2608-12629; semantic-review:SA-20260813-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260813-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260813-COVERAGE:end -->
<!-- semantic-review:SA-20260813-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260813-EVIDENCE:end -->
<!-- semantic-review:SA-20260813-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260813-SELECTION:end -->
<!-- semantic-review:SA-20260813-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260813-BOOKS:end -->

## 8. Ignored Noise

444 条 arXiv v1 中有 436 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：0 个 `Integrate`、0 个 `No Change — Existing Coverage`、8 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/13/README.md` 的 Coverage applicability 与 Books receipts。
- 本窗口没有新增达到长期知识门槛的机制，Books 正文无变化。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [Foresight Without Seeing: Latent Futures for World Action Models](https://arxiv.org/abs/2608.11605v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [Beyond Memory: A Transactional Continuity Kernel for Long-Lived AI Agents](https://arxiv.org/abs/2608.11632v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [Advancing MLLM-based UAV Image Understanding and Reasoning: A Benchmark and a Training-Free Multi-Agent System](https://arxiv.org/abs/2608.11738v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](https://arxiv.org/abs/2608.11775v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](https://arxiv.org/abs/2608.11888v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE Inference](https://arxiv.org/abs/2608.12103v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution](https://arxiv.org/abs/2608.12629v1) — published/event date: 2026-08-13; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
