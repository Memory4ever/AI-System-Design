# Daily Research — 2026-08-12

**Research Date:** 2026-08-12

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-11 09:00:00 ～ 2026-08-12 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-11 09:00:00` 至 `2026-08-12 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 533 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 6 个候选：2 个 Deep Review、4 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`AGENT-MEMORY` 中由《MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows》暴露的状态/证据边界；`INFER-SPECULATIVE-DECODING` 中由《MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-12 |
| Window End | 2026-08-12 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-12-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-11T09:00:00+08:00 | 2026-08-12T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 533 | SF-2026-ARXIV-2608-10362<br>SF-2026-ARXIV-2608-10424<br>SF-2026-ARXIV-2608-10502<br>SF-2026-ARXIV-2608-10509<br>SF-2026-ARXIV-2608-11079<br>SF-2026-ARXIV-2608-11095 | page count=7 snapshot files; final_cursor=end; daily-window total=533; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-12T09:00:00+08:00 | coverage:SRC-ARXIV:20260812 | — |
| SRC-GITHUB-COMMIT | 2026-08-11T09:00:00+08:00 | 2026-08-12T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-10424: https://api.github.com/repos/tingtang2/autoresearch-compute-recovery/commits?until=2026-08-11T03:15:08Z&per_page=1; per-family event-time recovery | checked | 1 | SF-2026-ARXIV-2608-10424 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-12T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260812 | — |

<!-- coverage:SRC-ARXIV:20260812:start -->submittedDate query filtered to [2026-08-11T09:00:00+08:00, 2026-08-12T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 6 routed families.<!-- coverage:SRC-ARXIV:20260812:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260812:start -->GitHub Commit API recovered and froze 1 repository commit(s): SF-2026-ARXIV-2608-10424: repository=tingtang2/autoresearch-compute-recovery; until=2026-08-11T03:15:08Z; sha=f9eab61e1fd70b7eaf228f1624b45af2378048e5; commit_timestamp=2026-08-08T22:40:47Z; commit_url=https://github.com/tingtang2/autoresearch-compute-recovery/commit/f9eab61e1fd70b7eaf228f1624b45af2378048e5; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260812:end -->

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
| SF-2026-ARXIV-2608-10362 | arXiv:2608.10362v1 | paper-v1:2608.10362 | 2026-W33 | 2026-08-11 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-10362 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2608-10362 | yes |
| SF-2026-ARXIV-2608-10424 | arXiv:2608.10424v1 | paper-v1:2608.10424 | 2026-W33 | 2026-08-11 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-10424 | self | — | new_in_window | AGENT-WORKFLOW | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-10502 | arXiv:2608.10502v1 | paper-v1:2608.10502 | 2026-W33 | 2026-08-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-10502 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-10509 | arXiv:2608.10509v1 | paper-v1:2608.10509 | 2026-W33 | 2026-08-11 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-10509 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2608-10509 | yes |
| SF-2026-ARXIV-2608-11079 | arXiv:2608.11079v1 | paper-v1:2608.11079 | 2026-W33 | 2026-08-11 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11079 | self | — | new_in_window | AGENT-PROMPT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-11095 | arXiv:2608.11095v1 | paper-v1:2608.11095 | 2026-W33 | 2026-08-12 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-11095 | self | — | new_in_window | AGENT-PROMPT | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-10362 | RP-4a85e2cf9996bc06 | deep | arXiv:2608.10362v1 | SRC-ARXIV@arXiv:2608.10362v1 | https://arxiv.org/html/2608.10362v1 (§§3.1–3.5: prediction engine, resident draft cache, controller and implementation) | https://arxiv.org/html/2608.10362v1 (§§4.1–4.6: Jetson setup, throughput, breakdown, ablation and sensitivity) | https://arxiv.org/html/2608.10362v1 (§4.6 Discussion and §6 Conclusion scope) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-10362 | complete |
| SF-2026-ARXIV-2608-10424 | RP-3d193d04ada80a89 | standard | arXiv:2608.10424v1 | SRC-ARXIV@arXiv:2608.10424v1; SRC-GITHUB-COMMIT@https://github.com/tingtang2/autoresearch-compute-recovery/commit/f9eab61e1fd70b7eaf228f1624b45af2378048e5 | https://arxiv.org/html/2608.10424v1#S3 (3 Methodology) | https://arxiv.org/html/2608.10424v1#S4 (4 Experimental setup and results) | https://arxiv.org/html/2608.10424v1#S6 (6 Discussion) | https://github.com/tingtang2/autoresearch-compute-recovery/commit/f9eab61e1fd70b7eaf228f1624b45af2378048e5 (latest official-repository commit before arXiv v1; 2026-08-08T22:40:47Z; provenance only) | claim:SF-2026-ARXIV-2608-10424 | complete |
| SF-2026-ARXIV-2608-10502 | RP-fdceb65014ad4268 | standard | arXiv:2608.10502v1 | SRC-ARXIV@arXiv:2608.10502v1 | https://arxiv.org/html/2608.10502v1#S3.SS2 (3.2 Dependency Graph Construction) | https://arxiv.org/html/2608.10502v1#S5 (5 Experiments) | https://arxiv.org/html/2608.10502v1#S6 (6 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-10502 | complete |
| SF-2026-ARXIV-2608-10509 | RP-7c17ebd4f8c2071a | deep | arXiv:2608.10509v1 | SRC-ARXIV@arXiv:2608.10509v1 | https://arxiv.org/html/2608.10509v1 (§§3.1–3.5 and Appendix B: typed provenance graph, permission filtering, ancestry/trust ranking, revocation and action-time gating) | https://arxiv.org/html/2608.10509v1 (§§4.1–4.6 and Appendices C–F: three-domain protocol, baselines, main results, transfer and ablations) | https://arxiv.org/html/2608.10509v1 (§4.4 scope/limitations and Appendix F error analysis: synthetic-domain, provenance-integrity and access-boundary limits) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-10509 | complete |
| SF-2026-ARXIV-2608-11079 | RP-e01166127b264d42 | standard | arXiv:2608.11079v1 | SRC-ARXIV@arXiv:2608.11079v1 | https://arxiv.org/html/2608.11079v1#S5 (V SkillZip) | https://arxiv.org/html/2608.11079v1#S6 (VI Experiments) | https://arxiv.org/html/2608.11079v1#A1.SS4 (A-D Boundary of the Guarantee) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11079 | complete |
| SF-2026-ARXIV-2608-11095 | RP-de37c1316e496eaf | standard | arXiv:2608.11095v1 | SRC-ARXIV@arXiv:2608.11095v1 | https://arxiv.org/html/2608.11095v1#S3 (3 field-corpus ratchet); https://arxiv.org/html/2608.11095v1#S4 (4 prompt-comment intervention); https://arxiv.org/html/2608.11095v1#A1 (Appendix A field corpus) | https://arxiv.org/html/2608.11095v1#A3 (Appendix C Inverse-IFEval); https://arxiv.org/html/2608.11095v1#A4 (Appendix D WildIFEval) | https://arxiv.org/html/2608.11095v1#Sx1 (Limitations); https://arxiv.org/html/2608.11095v1#A5 (Appendix E reproducibility boundary) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-11095 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-10362:start -->
#### MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices

<!-- claim:SF-2026-ARXIV-2608-10362:start -->MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。<!-- claim:SF-2026-ARXIV-2608-10362:end -->

MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。 adaptive speculative decoding 若每次发现更合适 draft 才加载，在大内存服务器尚可，在 8GB edge device 上切换成本会吞掉接受率收益。MemSpec 把效果预测与 resident-set 管理分离，提前保持两个 draft；它以预测器、缓存驻留和调度错误风险换稳定吞吐，draft pool 或生成阶段变化时静态单 draft 仍可能更好。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Score rationale：Design Delta：改变了proposal/verify/commit 状态的表示、控制点或验证路径；System Reach：影响集中在该 owner 或受限 workload；Durability：结论以接受率、验证开销与回滚为长期设计约束。
- Knowledge owner：`INFER-SPECULATIVE-DECODING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-10362:end -->

<!-- review:SF-2026-ARXIV-2608-10424:start -->
#### Recovering Wasted Compute in Autoresearch Agents

<!-- claim:SF-2026-ARXIV-2608-10424:start -->《Recovering Wasted Compute in Autoresearch Agents》把 `AGENT-WORKFLOW` 的问题具体化为：长预算搜索跨分支反复遇到相同 runtime constraints。其机制是用 global debug consultant 跨 search branches 共享 runtime constraints，并加强 tree-search 探索和调参控制；primary v1 的 evaluation 绑定为tabular-dataset autoresearch agents；固定 underlying LLM 的 targeted interventions，比较对象为unmodified autoresearch/tree-search pipeline。<!-- claim:SF-2026-ARXIV-2608-10424:end -->

证据支持的范围是：所测表格 autoresearch 中仅改 agent design 即可减少重复 debug 等 compute waste；不支持的外推是：端到端科学研究、非表格任务或任意模型的同等增益。旧方案仍有成立条件：各 branch 独立排错；短搜索或约束确实分支特有时隔离更安全。新机制获得的收益与代价必须一起读取：共享约束和探索控制换全局协调，错误诊断会污染所有分支。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：约束其实 branch-specific、consultant 误诊或分析仍未进入决策。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可恢复 workflow state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-WORKFLOW`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-10424:end -->

<!-- review:SF-2026-ARXIV-2608-10502:start -->
#### From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents

<!-- claim:SF-2026-ARXIV-2608-10502:start -->《From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents》把 `AGENT-MEMORY` 的问题具体化为：错误会传播成派生记忆、动作和后续写入，删源不能撤销后果。其机制是从 runtime provenance 建 typed memory→action graph，保留独立可信支撑的状态并只 replay 受影响计算；primary v1 的 evaluation 绑定为150 controlled cases/3 tool domains/4 failures 加 50 LongMemEval-V2-derived trajectories，比较对象为delete/reset/full-replay recovery families。<!-- claim:SF-2026-ARXIV-2608-10502:end -->

证据支持的范围是：两套受控评测中改善 recovery-cost 折中且保留 benign memory；不支持的外推是：覆盖所有真实 agent memory 故障或诊断必然正确。旧方案仍有成立条件：删源、reset 或 full replay；依赖浅且副作用可重做时简单。新机制获得的收益与代价必须一起读取：精细恢复换 provenance instrumentation、dependency graph 和 selective replay。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：隐式依赖、误诊、不可回滚副作用、循环派生或支撑误判。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-10502:end -->

<!-- review:SF-2026-ARXIV-2608-10509:start -->
#### MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

<!-- claim:SF-2026-ARXIV-2608-10509:start -->MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。<!-- claim:SF-2026-ARXIV-2608-10509:end -->

MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。 普通相似度检索在单一信任域、来源一致且动作低风险时简单有效；共享记忆跨主体、摘要会隐藏 private、poisoned 或 revoked ancestry 后，MAP-Graph 把 permission、path trust、affected ancestry 与 action risk 放进在线 gate。它以召回率、图维护与校准成本换授权和可审计性；provenance 伪造、缺失、revocation race 与未知高风险动作仍要求独立 policy enforcement。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了持久及派生记忆的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以写入、检索、更新与回滚为长期设计约束。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-10509:end -->

<!-- review:SF-2026-ARXIV-2608-11079:start -->
#### SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure

<!-- claim:SF-2026-ARXIV-2608-11079:start -->《SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure》把 `AGENT-PROMPT` 的问题具体化为：skill 膨胀但 rare exception 和工具/output contract 不能被采样遗漏。其机制是以 typed MDL 优化 skill contract+residual，对 trigger/workflow edge/tool/output obligation 设 hard coverage；primary v1 的 evaluation 绑定为摘要仅称 comprehensive evaluations；数据集与模型 Not Disclosed，比较对象为generic prompt compression 与 evaluation-guided compression。<!-- claim:SF-2026-ARXIV-2608-11079:end -->

证据支持的范围是：作者评测中改善 compression/generalization/cost；不支持的外推是：未抽取语义也被保留，或无需行为验证即可保证等价。旧方案仍有成立条件：成功/失败 patch 只追加；token 预算宽裕时最不易误删例外。新机制获得的收益与代价必须一起读取：省 token/rollout 换结构抽取和 typed schema，最优性受抽取质量约束。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：漏 obligation/edge、scope 提升错误、引用歧义或增量 patch 破坏旧 contract。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-PROMPT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11079:end -->

<!-- review:SF-2026-ARXIV-2608-11095:start -->
#### Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding

<!-- claim:SF-2026-ARXIV-2608-11095:start -->《Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding》把 `AGENT-PROMPT` 的问题具体化为：长期 prompt 的删除风险随依赖集合增长。其机制是为 agent instruction 写保留 rationale 的 prompt comments，使未来删除可验证，并用 inverted IFEval 构造已知最优世界；primary v1 的 evaluation 绑定为1867 repos/247694 instruction lifetimes；inverted IFEval 与 WildIFEval，比较对象为uncommented growing prompts / original instruction history。<!-- claim:SF-2026-ARXIV-2608-11095:end -->

证据支持的范围是：样本中老规则更难删，comments 可在已知最优设置去 excess 并改善 WildIFEval；不支持的外推是：自然 repo 增长完全由 rationale loss 因果导致，或 comments 永久正确。旧方案仍有成立条件：遇回归就追加规则；信息不足时保留旧规则较安全。新机制获得的收益与代价必须一起读取：可维护性换 comment token/维护负担，错误 rationale 也会固化。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：comment 过期/虚假、规则不可验证或高阶交互/重写改变前提。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-PROMPT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-11095:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-10362 | GSM8K, MATH, HumanEval, MBPP, LexGLUE, MedQA and MedMCQA speculative decoding | GPTQ INT4 LLaMA-2-7B and Qwen2.5-7B targets; five draft roles per family: general, code, math, law and medical; each draft is 400M for LLaMA-2 or 0.5B for Qwen2.5 | NVIDIA Jetson Orin Nano with 8GB LPDDR5 | GPTQ INT4 target models; draft precision Not Disclosed | dataset-dependent prompt and phase context; exact normalized prompt length Not Disclosed | 128 generated tokens in the main throughput protocol | batch 1 | single request with at most two resident drafts | no production SLO; steady-state generation throughput, acceptance and switching breakdown | official task scorers plus static/adaptive draft selectors; exact checkpoint identities Not Disclosed in v1 |
| SF-2026-ARXIV-2608-10509 | provenance-aware shared-memory authorization across three synthetic multi-agent domains | MAP-Graph with two disclosed backbone-transfer settings; exact checkpoint identities are not normalized in v1 | Not Disclosed — v1 does not identify evaluation hardware | Not Disclosed — v1 does not state numeric precision | 2,700 synthetic tasks per method across three domains; token length Not Disclosed | retrieval choice, permission/trust decision and action-risk gate outcome | one task decision; 2,700 is corpus size, not batch | Not Disclosed — v1 does not state serving concurrency | utility, privacy/trust violations and action-risk outcomes; no production SLO | semantic retrieval, scoped access and lineage-only baselines; §§4.1–4.6 plus Appendices C–F, including ablation and backbone transfer |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-10509 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260812-2608-10509 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=Memory provenance moves into read authorization, trust ranking and action gating | analysis:DA-20260812-2608-10509 |
| SF-2026-ARXIV-2608-10362 | score_7_9<br>potential_books_delta | selected | DA-20260812-2608-10362 | — | 逐 family 排序：override=none，V2=8/9 (3/2/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=edge speculation is first constrained by draft residency and memory budget | analysis:DA-20260812-2608-10362 |

<!-- analysis:DA-20260812-2608-10509:start -->
### MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。 普通相似度检索在单一信任域、来源一致且动作低风险时简单有效；共享记忆跨主体、摘要会隐藏 private、poisoned 或 revoked ancestry 后，MAP-Graph 把 permission、path trust、affected ancestry 与 action risk 放进在线 gate。它以召回率、图维护与校准成本换授权和可审计性；provenance 伪造、缺失、revocation race 与未知高风险动作仍要求独立 policy enforcement。

<!-- analysis:DA-20260812-2608-10509:end -->

<!-- analysis:DA-20260812-2608-10362:start -->
### MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices

MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。 adaptive speculative decoding 若每次发现更合适 draft 才加载，在大内存服务器尚可，在 8GB edge device 上切换成本会吞掉接受率收益。MemSpec 把效果预测与 resident-set 管理分离，提前保持两个 draft；它以预测器、缓存驻留和调度错误风险换稳定吞吐，draft pool 或生成阶段变化时静态单 draft 仍可能更好。

<!-- analysis:DA-20260812-2608-10362:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-10362 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L16<br>books/part-05-inference-system/48-speculative-decoding.md#L470 | books/part-05-inference-system/44-decode.md#L14<br>books/part-05-inference-system/46-continuous-batching.md#L14 | existing:SF-2026-ARXIV-2608-10362 | delta:SF-2026-ARXIV-2608-10362 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-10362 |
| SF-2026-ARXIV-2608-10509 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14<br>books/part-07-agent/77-memory.md#L888 | books/part-07-agent/76-rag.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2608-10509 | delta:SF-2026-ARXIV-2608-10509 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2608-10509 |

<!-- books-review:SF-2026-ARXIV-2608-10362:start --><!-- existing:SF-2026-ARXIV-2608-10362:start -->现有中心命题：Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。<!-- existing:SF-2026-ARXIV-2608-10362:end --><!-- delta:SF-2026-ARXIV-2608-10362:start -->MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。<!-- delta:SF-2026-ARXIV-2608-10362:end -->与上述中心命题相比，这个 family 的新增证据是：MemSpec 将 draft 选择与 draft residency 分离：轻量 predictor 估计阶段性 draft 效果，memory-aware scheduler 提前维护 resident working set，避免 edge device 上的 reactive model load。Jetson Orin Nano 结果只支持给定 draft pool 与内存压力；预测失误和模型切换竞争可能吞掉 speculative gain。 该 delta 已落在《第48章 Speculative Decoding》的正文机制锚点；语义相邻边界为 INFER-DECODE：Decode 是受 autoregressive dependency 约束的逐 token 状态机；单请求每一步的矩阵维度很小，却需要读取大量 weights 和历史 KV，因此性能由 memory movement、batch composition 与 iteration cadence 共同决定。；INFER-CONTINUOUS-BATCHING：LLM Serving 的 batch 不是一个静态数组，而是一个会在每个 iteration 重新构造的 token-work 集合。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-10362:end -->

<!-- books-review:SF-2026-ARXIV-2608-10509:start --><!-- existing:SF-2026-ARXIV-2608-10509:start -->现有中心命题：Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。<!-- existing:SF-2026-ARXIV-2608-10509:end --><!-- delta:SF-2026-ARXIV-2608-10509:start -->MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。<!-- delta:SF-2026-ARXIV-2608-10509:end -->与上述中心命题相比，这个 family 的新增证据是：MAP-Graph 把共享记忆从相似度检索对象提升为带来源、权限、信任与 revocation ancestry 的安全状态：先做 permission filter，再按 path trust 排序，最后由 action-risk gate 决定是否允许高风险动作。作者的三域 synthetic benchmark、ablation 与 backbone transfer 支持该受控合同，但不证明真实组织权限、对抗性 provenance 或并发撤销已经安全。 该 delta 已落在《第77章 Memory》的正文机制锚点；语义相邻边界为 AGENT-RAG：RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-10509:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260812-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260812; coverage:SRC-GITHUB-COMMIT:20260812; semantic-review:SA-20260812-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260812-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-10362; review:SF-2026-ARXIV-2608-10424; review:SF-2026-ARXIV-2608-10502; review:SF-2026-ARXIV-2608-10509; review:SF-2026-ARXIV-2608-11079; review:SF-2026-ARXIV-2608-11095; semantic-review:SA-20260812-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260812-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260812-2608-10362; analysis:DA-20260812-2608-10509; semantic-review:SA-20260812-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260812-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-10362; books-review:SF-2026-ARXIV-2608-10509; review:SF-2026-ARXIV-2608-10424; review:SF-2026-ARXIV-2608-10502; review:SF-2026-ARXIV-2608-11079; review:SF-2026-ARXIV-2608-11095; semantic-review:SA-20260812-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260812-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260812-COVERAGE:end -->
<!-- semantic-review:SA-20260812-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260812-EVIDENCE:end -->
<!-- semantic-review:SA-20260812-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260812-SELECTION:end -->
<!-- semantic-review:SA-20260812-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260812-BOOKS:end -->

## 8. Ignored Noise

533 条 arXiv v1 中有 527 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：2 个 `Integrate`、0 个 `No Change — Existing Coverage`、4 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/12/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/48-speculative-decoding.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-07-agent/77-memory.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [MemSpec: Memory-Aware Runtime for Adaptive Draft Scheduling in Speculative Decoding on Edge Devices](https://arxiv.org/abs/2608.10362v1) — published/event date: 2026-08-11; accessed: 2026-08-25
- [Recovering Wasted Compute in Autoresearch Agents](https://arxiv.org/abs/2608.10424v1) — published/event date: 2026-08-11; accessed: 2026-08-25
- [From Faulty Memories to Corrected Actions: Dependency-Guided Rollback Repair for Memory-Augmented Agents](https://arxiv.org/abs/2608.10502v1) — published/event date: 2026-08-11; accessed: 2026-08-25
- [MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows](https://arxiv.org/abs/2608.10509v1) — published/event date: 2026-08-11; accessed: 2026-08-25
- [SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering Reusable Structure](https://arxiv.org/abs/2608.11079v1) — published/event date: 2026-08-11; accessed: 2026-08-25
- [Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding](https://arxiv.org/abs/2608.11095v1) — published/event date: 2026-08-12; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
