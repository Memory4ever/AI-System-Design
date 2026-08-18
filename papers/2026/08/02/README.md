# Daily Research — 2026-08-02

**Research Date:** 2026-08-02

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-01 09:00:00 ～ 2026-08-02 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-01 09:00:00` 至 `2026-08-02 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 291 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 2 个候选：0 个 Deep Review、2 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`AGENT-MULTI-AGENT` 中由《BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration》暴露的状态/证据边界；`MODEL-MOE` 中由《HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-02 |
| Window End | 2026-08-02 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-02-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-01T09:00:00+08:00 | 2026-08-02T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 291 | SF-2026-ARXIV-2608-00458<br>SF-2026-ARXIV-2608-00577 | page count=7 snapshot files; final_cursor=end; daily-window total=291; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-02T09:00:00+08:00 | coverage:SRC-ARXIV:20260802 | — |

<!-- coverage:SRC-ARXIV:20260802:start -->submittedDate query filtered to [2026-08-01T09:00:00+08:00, 2026-08-02T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 2 routed families.<!-- coverage:SRC-ARXIV:20260802:end -->

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
| SF-2026-ARXIV-2608-00458 | arXiv:2608.00458v1 | paper-v1:2608.00458 | 2026-W31 | 2026-08-01 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-00458 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-00577 | arXiv:2608.00577v1 | paper-v1:2608.00577 | 2026-W31 | 2026-08-01 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-00577 | self | — | new_in_window | MODEL-MOE | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-00458 | RP-90fdf13e8a4c0aac | standard | arXiv:2608.00458v1 | SRC-ARXIV@arXiv:2608.00458v1 | https://arxiv.org/html/2608.00458v1#S4 (IV BANDMAS Design) | https://arxiv.org/html/2608.00458v1#S5 (V Evaluation) | https://arxiv.org/html/2608.00458v1#S6 (VI Threats and Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-00458 | complete |
| SF-2026-ARXIV-2608-00577 | RP-8a9c99df21b6a138 | standard | arXiv:2608.00577v1 | SRC-ARXIV@arXiv:2608.00577v1 | https://arxiv.org/pdf/2608.00577v1 (pp. 4–9, §§III–V: cost model, deployment and collaborative routing) | https://arxiv.org/pdf/2608.00577v1 (pp. 10–14, §VI: 10-server trace-driven evaluation) | https://arxiv.org/pdf/2608.00577v1 (pp. 14–15, §§VI-F–VII: sensitivity, configured quality budget and conclusion scope) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-00577 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-00458:start -->
#### BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration

<!-- claim:SF-2026-ARXIV-2608-00458:start -->《BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration》把 `AGENT-MULTI-AGENT` 的问题具体化为：多 agent 中 bytes、tokens 与链路延迟随中间消息增长。其机制是把跨 agent 内容封装为 semantic packet，以 replay contribution 估值并与带宽/延迟/token 成本比较后传输；primary v1 的 evaluation 绑定为冻结 Qwen3-4B；SciFact、HotpotQA、FanOutQA；多种带宽上限，比较对象为完整转发、agent pruning 与消息丢弃类方法。<!-- claim:SF-2026-ARXIV-2608-00458:end -->

证据支持的范围是：冻结模型/任务/链路约束中改善带宽-任务质量折中；不支持的外推是：估值具有真实因果识别能力，或覆盖实时、对抗流量和任意拓扑。旧方案仍有成立条件：完整转发；消息少、链路足且漏证据代价高时最稳妥。新机制获得的收益与代价必须一起读取：通信节省换估值计算和误删关键证据风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：贡献预测失准、跨 packet 依赖、约束漂移或恶意消息。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供共享状态与协作拓扑的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-MULTI-AGENT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-00458:end -->

<!-- review:SF-2026-ARXIV-2608-00577:start -->
#### HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference

<!-- claim:SF-2026-ARXIV-2608-00577:start -->《HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference》把 `MODEL-MOE` 的问题具体化为：top-k experts 跨服务器分散后，单因子负载均衡会把成本转移到链路、加载或质量损失。其机制是用统一 assignment cost 同时建模跨机传输、GPU-CPU offload、GPU queue/compute 与量化质量惩罚；离线决定 placement/residency/precision，在线整体路由 top-k expert set；primary v1 的 evaluation 绑定为三个 MoE、异构十服务器 edge testbed 与 trace-driven load，比较 latency、P99、traffic、throughput 和质量预算，比较对象为只优化单一网络、算力、offload 或 replica precision 因素的分离式 expert routing。<!-- claim:SF-2026-ARXIV-2608-00577:end -->

证据支持的范围是：geo-distributed heterogeneous edge 上，专家组合的瓶颈由 placement、队列、链路和精度共同决定；不支持的外推是：任意规模组合优化都可实时求精确解，或作者 testbed 的提升可外推到数据中心 fabric 和其他 MoE。旧方案仍有成立条件：同构集群、专家常驻且网络稳定时，简单 locality/load-aware routing 的控制开销更低。新机制获得的收益与代价必须一起读取：联合成本降低局部瓶颈，但需要在线状态、精度预算和离线部署共同维护，beam search 还引入近似误差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：队列陈旧、链路突变、热专家迁移、候选域膨胀或质量 penalty 未校准会使路由次优。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供条件计算路由的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-MOE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-00577:end -->

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
| SA-20260802-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260802; semantic-review:SA-20260802-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260802-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-00458; review:SF-2026-ARXIV-2608-00577; semantic-review:SA-20260802-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260802-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis-decision:NO-DEEP; semantic-review:SA-20260802-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260802-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; review:SF-2026-ARXIV-2608-00458; review:SF-2026-ARXIV-2608-00577; semantic-review:SA-20260802-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260802-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260802-COVERAGE:end -->
<!-- semantic-review:SA-20260802-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260802-EVIDENCE:end -->
<!-- semantic-review:SA-20260802-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260802-SELECTION:end -->
<!-- semantic-review:SA-20260802-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260802-BOOKS:end -->

## 8. Ignored Noise

291 条 arXiv v1 中有 289 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：0 个 `Integrate`、0 个 `No Change — Existing Coverage`、2 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/02/README.md` 的 Coverage applicability 与 Books receipts。
- 本窗口没有新增达到长期知识门槛的机制，Books 正文无变化。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration](https://arxiv.org/abs/2608.00458v1) — published/event date: 2026-08-01; accessed: 2026-08-25
- [HetRoute Heterogeneous and Cost-aware Collaborative Routing Framework for Distributed Edge MoE Inference](https://arxiv.org/abs/2608.00577v1) — published/event date: 2026-08-01; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
