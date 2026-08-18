# Daily Research — 2026-08-09

**Research Date:** 2026-08-09

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-08 09:00:00 ～ 2026-08-09 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-08 09:00:00` 至 `2026-08-09 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 267 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 6 个候选：1 个 Deep Review、5 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-SCHEDULING` 中由《OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-09 |
| Window End | 2026-08-09 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-09-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-08T09:00:00+08:00 | 2026-08-09T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 267 | SF-2026-ARXIV-2608-07855<br>SF-2026-ARXIV-2608-07915<br>SF-2026-ARXIV-2608-07971<br>SF-2026-ARXIV-2608-08038<br>SF-2026-ARXIV-2608-08097<br>SF-2026-ARXIV-2608-08340 | page count=7 snapshot files; final_cursor=end; daily-window total=267; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-09T09:00:00+08:00 | coverage:SRC-ARXIV:20260809 | — |

<!-- coverage:SRC-ARXIV:20260809:start -->submittedDate query filtered to [2026-08-08T09:00:00+08:00, 2026-08-09T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 6 routed families.<!-- coverage:SRC-ARXIV:20260809:end -->

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
| SF-2026-ARXIV-2608-07855 | arXiv:2608.07855v1 | paper-v1:2608.07855 | 2026-W32 | 2026-08-08 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-07855 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-07915 | arXiv:2608.07915v1 | paper-v1:2608.07915 | 2026-W32 | 2026-08-08 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-07915 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-07971 | arXiv:2608.07971v1 | paper-v1:2608.07971 | 2026-W32 | 2026-08-08 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-07971 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08038 | arXiv:2608.08038v1 | paper-v1:2608.08038 | 2026-W32 | 2026-08-08 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08038 | self | — | new_in_window | AGENT-MULTI-AGENT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08097 | arXiv:2608.08097v1 | paper-v1:2608.08097 | 2026-W32 | 2026-08-08 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08097 | self | — | new_in_window | INFER-KV-CACHE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08340 | arXiv:2608.08340v1 | paper-v1:2608.08340 | 2026-W32 | 2026-08-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-08340 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2608-08340 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-07855 | RP-811eb90b398a1ee2 | standard | arXiv:2608.07855v1 | SRC-ARXIV@arXiv:2608.07855v1 | https://arxiv.org/html/2608.07855v1#S3 (3 Methodology) | https://arxiv.org/html/2608.07855v1#S4 (4 Experiments) | https://arxiv.org/html/2608.07855v1#S5 (5 Conclusion and Future Work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-07855 | complete |
| SF-2026-ARXIV-2608-07915 | RP-7a1be5079c27f5eb | standard | arXiv:2608.07915v1 | SRC-ARXIV@arXiv:2608.07915v1 | https://arxiv.org/html/2608.07915v1#S3 (3 Method) | https://arxiv.org/html/2608.07915v1#S4 (4 Experiments) | https://arxiv.org/html/2608.07915v1#S6 (6 Conclusion) | Not Required — v1 discloses https://github.com/nokia-applied-research/SPECTRA, but this Standard claim does not use repository code; the declared repository returned 404 on 2026-08-26, so no event-time tree was imported | claim:SF-2026-ARXIV-2608-07915 | complete |
| SF-2026-ARXIV-2608-07971 | RP-65e0a3ee8862fd09 | standard | arXiv:2608.07971v1 | SRC-ARXIV@arXiv:2608.07971v1 | https://arxiv.org/html/2608.07971v1#S3 (3 System Design) | https://arxiv.org/html/2608.07971v1#S5 (5 Evaluation) | https://arxiv.org/html/2608.07971v1#S7 (7 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-07971 | complete |
| SF-2026-ARXIV-2608-08038 | RP-9520709fad3db1a9 | standard | arXiv:2608.08038v1 | SRC-ARXIV@arXiv:2608.08038v1 | https://arxiv.org/html/2608.08038v1#S4 (IV Methodology) | https://arxiv.org/html/2608.08038v1#S6 (VI Experimental Setup: Requirements and Compliance) | https://arxiv.org/html/2608.08038v1#S8 (VIII Discussion and Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08038 | complete |
| SF-2026-ARXIV-2608-08097 | RP-004b92fe9154599f | standard | arXiv:2608.08097v1 | SRC-ARXIV@arXiv:2608.08097v1 | https://arxiv.org/html/2608.08097v1#S4 (4. System Design) | https://arxiv.org/html/2608.08097v1#S5 (5. Evaluation) | https://arxiv.org/html/2608.08097v1#S7 (7. Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08097 | complete |
| SF-2026-ARXIV-2608-08340 | RP-bde4bc9415c54138 | deep | arXiv:2608.08340v1 | SRC-ARXIV@arXiv:2608.08340v1 | https://arxiv.org/html/2608.08340v1 (§§3.2–4.7: operator model, segment compilation, data plane, scheduling, state and implementation) | https://arxiv.org/html/2608.08340v1 (§§5.1–5.8: setup, pipeline/framework/Higress benchmarks, retrieval quality and scaling) | https://arxiv.org/html/2608.08340v1 (§7.1 Limitations and Future Work) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-08340 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-07855:start -->
#### CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents

<!-- claim:SF-2026-ARXIV-2608-07855:start -->《CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents》把 `INFER-KV-CACHE` 的问题具体化为：多轮工具轨迹中当前低注意信息仍可能被后续 observation 重新激活。其机制是按 tool-call commit 前后做页面删除效应配对，联合测试后只退休已完成生命周期的 KV 页；primary v1 的 evaluation 绑定为多种未命名 benchmark 的 multi-turn ReAct agent；测 memory、端到端 inference 与 accuracy，比较对象为existing KV-cache compression methods（摘要未命名）。<!-- claim:SF-2026-ARXIV-2608-07855:end -->

证据支持的范围是：作者 workload 中可区分暂眠页与已完成页并改善 memory/latency/accuracy；不支持的外推是：任意未来回访模式下均可安全驱逐，或生产 tail/SLO 与跨模型泛化。旧方案仍有成立条件：按当前 attention score 的 snapshot eviction；在未来依赖与当前注意力一致时仍简单有效。新机制获得的收益与代价必须一起读取：节省 KV 与注意力成本，交换为 commit 前后测量、pending-page 保护和联合测试开销。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：commit 边界错误、未来语义回开、工具观察改变依赖或 K/V/position 索引不一致。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-07855:end -->

<!-- review:SF-2026-ARXIV-2608-07915:start -->
#### SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding

<!-- claim:SF-2026-ARXIV-2608-07915:start -->《SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding》把 `INFER-KV-CACHE` 的问题具体化为：outlier-heavy 且原坐标强相关，四级量化会把主体信号压成噪声。其机制是由 KV 统计求去相关谱坐标，再把 bit budget 集中到高信息通道的 training-free codec；primary v1 的 evaluation 绑定为Llama-3.1-8B、Qwen2.5-7B 的 long-context benchmark；覆盖多个激进 compression operating points，比较对象为uniform low-bit KV quantization（摘要未命名具体方法）。<!-- claim:SF-2026-ARXIV-2608-07915:end -->

证据支持的范围是：所测模型和任务上改善 uniform low-bit quantization 的质量边界；不支持的外推是：任意模型/分布近无损、codec/kernel 开销可忽略或必然带来生产吞吐收益。旧方案仍有成立条件：统一低精度量化；当通道相关性和 outlier 不显著时实现更直接。新机制获得的收益与代价必须一起读取：压缩率和质量改善，交换为统计、旋转、非均匀编码及编解码开销。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：校准统计失配、分布漂移、谱能量不集中或极端 bit budget。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-07915:end -->

<!-- review:SF-2026-ARXIV-2608-07971:start -->
#### ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters

<!-- claim:SF-2026-ARXIV-2608-07971:start -->《ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters》把 `PLATFORM-GPU-SCHEDULER` 的问题具体化为：训练周期性空闲且离线推理 bursty，静态配额长期闲置。其机制是resource-shape family、elastic shadow pricing 与干扰预测器联合决定 GPU co-location；primary v1 的 evaluation 绑定为64-GPU testbed 与最高 512-GPU trace simulation；training 加 offline inference，比较对象为rigid static isolated allocation（摘要未命名具体 scheduler）。<!-- claim:SF-2026-ARXIV-2608-07971:end -->

证据支持的范围是：该 testbed/trace 中可降低 JCT 并提高 throughput/utilization；不支持的外推是：生产 trace 外 predictor 泛化、在线安全隔离或长期 fairness。旧方案仍有成立条件：训练和推理隔离且整卡静态预留；在相位稳定或隔离优先时仍合理。新机制获得的收益与代价必须一起读取：利用率换配置搜索、干扰预测和共置隔离风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：未见 workload、突发相位同步、硬件计数器漂移或错误 resource shape。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-GPU-SCHEDULER`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-07971:end -->

<!-- review:SF-2026-ARXIV-2608-08038:start -->
#### Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering

<!-- claim:SF-2026-ARXIV-2608-08038:start -->《Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering》把 `AGENT-MULTI-AGENT` 的问题具体化为：行为视图必须服从先前结构接口与车辆信号本体。其机制是Class→Activity→Sequence 有状态生成，结合 VSS-grounded RAG、独立 validator 与回退；primary v1 的 evaluation 绑定为单个 ADAS MBSE scenario 的 cross-view interface alignment，比较对象为standard RAG。<!-- claim:SF-2026-ARXIV-2608-08038:end -->

证据支持的范围是：该场景中 entity traceability、signal conservation 与 F1 均改善；不支持的外推是：zero-error MBSE、任意车辆域可靠性或 validator 独立性。旧方案仍有成立条件：各视图一次性或弱状态 RAG；当接口少且人工复核充分时成本更低。新机制获得的收益与代价必须一起读取：跨阶段一致性换 validator、backtracking、state schema 的延迟和 token 成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：VSS/错误分类不全、validator 与生成器共因错误、未知接口或回退状态污染。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供共享状态与协作拓扑的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`AGENT-MULTI-AGENT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08038:end -->

<!-- review:SF-2026-ARXIV-2608-08097:start -->
#### OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching

<!-- claim:SF-2026-ARXIV-2608-08097:start -->《OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching》把 `INFER-KV-CACHE` 的问题具体化为：长上下文 decode 受 HBM 容量/流量限制，同时重要 token 具有可预测稀疏性。其机制是用 speculative lookahead 预测下一步重要 KV block，后台从 host/remote tier 预取到 HBM；primary v1 的 evaluation 绑定为reasoning、multi-GPU long-context 与 P/D disaggregation；2048-token KV budget，比较对象为full attention、dense vLLM 与 full-KV transfer。<!-- claim:SF-2026-ARXIV-2608-08097:end -->

证据支持的范围是：所测稀疏 decode workload 可用较小 HBM KV 保持接近完整注意力的质量并提升吞吐；不支持的外推是：所有 workload 都有足够稀疏性，或 remote-tier tail/SLO 与 miss 无害。旧方案仍有成立条件：完整 KV 常驻 HBM 并每 token dense reread；上下文短或 HBM 足够时最稳妥。新机制获得的收益与代价必须一起读取：HBM 节省换 speculative dependency、远端带宽和 prefetch pipeline。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：lookahead recall 下降、低稀疏性、tier contention、迟到预取或 P/D transfer 失速。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供context-conditioned KV state的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08097:end -->

<!-- review:SF-2026-ARXIV-2608-08340:start -->
#### OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows

<!-- claim:SF-2026-ARXIV-2608-08340:start -->OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。<!-- claim:SF-2026-ARXIV-2608-08340:end -->

OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。 旧的 agent/RAG framework 把 embedding、retrieval、memory 与 upsert 当回调；在单机和低并发时灵活性优先，这个选择合理。多阶段 CPU/GPU stall 成为主约束后，OpRAG 把阶段降为 typed operator 和确定性 segment，以 zero-copy、bounded queue 与 overlap 换取资源可控性；代价是 runtime 专用化、队列背压和状态 ownership 复杂度，远程索引与生产 P99 仍未闭合。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了请求调度与资源所有权的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以goodput、公平性与 SLO为长期设计约束。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08340:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08340 | multi-stage RAG over 32K WikiText-103-derived chunks; GPU pipeline, framework and Higress-style scenarios | meta-llama/Meta-Llama-3-8B-Instruct and mistralai/Mistral-7B-Instruct-v0.3 with FlashAttention 2.8.3.post1 | 2× NVIDIA A100; one complete replica per GPU with data-parallel corpus shards | BF16 | GPU pipeline max input 128 tokens; Higress-style max input 512 tokens; 900 characters per indexed chunk | maximum generation length 32 tokens | 64 sampled prompts per GPU for the generation workload | 1024 total queries per Higress-style scenario; one model replica per GPU | no production SLO; end-to-end latency, chunks/s, query throughput and Recall@5 | paper runtime protocol; Async/Dask/Ray/Higress and Agent/RAG framework baselines; Recall@5 |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08340 | score_7_9<br>potential_books_delta | selected | DA-20260809-2608-08340 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=an inference request becomes an operator DAG with explicit admission, placement and completion | analysis:DA-20260809-2608-08340 |

<!-- analysis:DA-20260809-2608-08340:start -->
### OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows

OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。 旧的 agent/RAG framework 把 embedding、retrieval、memory 与 upsert 当回调；在单机和低并发时灵活性优先，这个选择合理。多阶段 CPU/GPU stall 成为主约束后，OpRAG 把阶段降为 typed operator 和确定性 segment，以 zero-copy、bounded queue 与 overlap 换取资源可控性；代价是 runtime 专用化、队列背压和状态 ownership 复杂度，远程索引与生产 P99 仍未闭合。

<!-- analysis:DA-20260809-2608-08340:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08340 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L14<br>books/part-05-inference-system/56-inference-scheduling.md#L335 | books/part-05-inference-system/46-continuous-batching.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-08340 | delta:SF-2026-ARXIV-2608-08340 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-08340 |

<!-- books-review:SF-2026-ARXIV-2608-08340:start --><!-- existing:SF-2026-ARXIV-2608-08340:start -->现有中心命题：推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。<!-- existing:SF-2026-ARXIV-2608-08340:end --><!-- delta:SF-2026-ARXIV-2608-08340:start -->OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。<!-- delta:SF-2026-ARXIV-2608-08340:end -->与上述中心命题相比，这个 family 的新增证据是：OpRAG 将 embedding、retrieval、reasoning、memory 和 upsert 降为 resource-aware operators，并用 Arrow zero-copy、persistent worker、bounded queue 与 CPU/GPU overlap 构成确定性执行图。作者在两种 7B/8B 模型和 32K chunks 上测得的增益不能外推到不同 index、并发、尾延迟或远程存储。 该 delta 已落在《第56章 推理调度》的正文机制锚点；语义相邻边界为 INFER-CONTINUOUS-BATCHING：LLM Serving 的 batch 不是一个静态数组，而是一个会在每个 iteration 重新构造的 token-work 集合。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-08340:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260809-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260809; semantic-review:SA-20260809-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260809-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-07855; review:SF-2026-ARXIV-2608-07915; review:SF-2026-ARXIV-2608-07971; review:SF-2026-ARXIV-2608-08038; review:SF-2026-ARXIV-2608-08097; review:SF-2026-ARXIV-2608-08340; semantic-review:SA-20260809-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260809-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260809-2608-08340; semantic-review:SA-20260809-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260809-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-08340; review:SF-2026-ARXIV-2608-07855; review:SF-2026-ARXIV-2608-07915; review:SF-2026-ARXIV-2608-07971; review:SF-2026-ARXIV-2608-08038; review:SF-2026-ARXIV-2608-08097; semantic-review:SA-20260809-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260809-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260809-COVERAGE:end -->
<!-- semantic-review:SA-20260809-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260809-EVIDENCE:end -->
<!-- semantic-review:SA-20260809-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260809-SELECTION:end -->
<!-- semantic-review:SA-20260809-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260809-BOOKS:end -->

## 8. Ignored Noise

267 条 arXiv v1 中有 261 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：1 个 `Integrate`、0 个 `No Change — Existing Coverage`、5 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/09/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/56-inference-scheduling.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [CommitKV: Lifecycle-Aware KV Cache Compression via Commit Transitions for Multi-Turn Agents](https://arxiv.org/abs/2608.07855v1) — published/event date: 2026-08-08; accessed: 2026-08-25
- [SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding](https://arxiv.org/abs/2608.07915v1) — published/event date: 2026-08-08; accessed: 2026-08-25
- [ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters](https://arxiv.org/abs/2608.07971v1) — published/event date: 2026-08-08; accessed: 2026-08-25
- [Stateful Multi-Agent LLMs for Cross-View Interface Alignment in Automotive Model-Based Systems Engineering](https://arxiv.org/abs/2608.08038v1) — published/event date: 2026-08-08; accessed: 2026-08-25
- [OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching](https://arxiv.org/abs/2608.08097v1) — published/event date: 2026-08-08; accessed: 2026-08-25
- [OpRAG: A Resource-Deterministic Runtime for GPU-Backed Multi-Stage RAG Workflows](https://arxiv.org/abs/2608.08340v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
