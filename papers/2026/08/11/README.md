# Daily Research — 2026-08-11

**Research Date:** 2026-08-11

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-10 09:00:00 ～ 2026-08-11 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-10 09:00:00` 至 `2026-08-11 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 601 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 4 个候选：2 个 Deep Review、2 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`PLATFORM-SECURITY` 中由《Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference》暴露的状态/证据边界；`MULTIMODAL-WORLD-MODELS` 中由《World Tokens: Enhancing Embodied Policies with Training-Time World Modeling》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-11 |
| Window End | 2026-08-11 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-11-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-10T09:00:00+08:00 | 2026-08-11T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 601 | SF-2026-ARXIV-2608-09160<br>SF-2026-ARXIV-2608-09225<br>SF-2026-ARXIV-2608-09254<br>SF-2026-ARXIV-2608-09730 | page count=7 snapshot files; final_cursor=end; daily-window total=601; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-11T09:00:00+08:00 | coverage:SRC-ARXIV:20260811 | — |
| SRC-GITHUB-COMMIT | 2026-08-10T09:00:00+08:00 | 2026-08-11T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-09254: https://api.github.com/repos/k-w-lee/query_proof/commits?until=2026-08-10T08:14:24Z&per_page=1; per-family event-time recovery | checked | 1 | SF-2026-ARXIV-2608-09254 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-11T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260811 | — |

<!-- coverage:SRC-ARXIV:20260811:start -->submittedDate query filtered to [2026-08-10T09:00:00+08:00, 2026-08-11T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 4 routed families.<!-- coverage:SRC-ARXIV:20260811:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260811:start -->GitHub Commit API recovered and froze 1 repository commit(s): SF-2026-ARXIV-2608-09254: repository=k-w-lee/query_proof; until=2026-08-10T08:14:24Z; sha=c5d22984a238f53218507a03199d2d80c0ea2e2c; commit_timestamp=2026-08-10T07:53:22Z; commit_url=https://github.com/k-w-lee/query_proof/commit/c5d22984a238f53218507a03199d2d80c0ea2e2c; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260811:end -->

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
| SF-2026-ARXIV-2608-09160 | arXiv:2608.09160v1 | paper-v1:2608.09160 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-09160 | self | — | new_in_window | TRAIN-TENSOR-PARALLEL | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-09225 | arXiv:2608.09225v1 | paper-v1:2608.09225 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-09225 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2608-09225 | yes |
| SF-2026-ARXIV-2608-09254 | arXiv:2608.09254v1 | paper-v1:2608.09254 | 2026-W33 | 2026-08-10 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-09254 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-09730 | arXiv:2608.09730v1 | paper-v1:2608.09730 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-09730 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2608-09730 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-09160 | RP-46e759c675018927 | standard | arXiv:2608.09160v1 | SRC-ARXIV@arXiv:2608.09160v1 | https://arxiv.org/html/2608.09160v1#S3 (III Design and Implementation of SwiftQK) | https://arxiv.org/html/2608.09160v1#S4 (IV Evaluation) | https://arxiv.org/html/2608.09160v1#S5 (V Conclusion and future work) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-09160 | complete |
| SF-2026-ARXIV-2608-09225 | RP-665286b0c0ee5645 | deep | arXiv:2608.09225v1 | SRC-ARXIV@arXiv:2608.09225v1 | https://arxiv.org/html/2608.09225v1 (§§3.1–4.4: three attacks, HMAC namespace, boundary salting and ORIGAMI) | https://arxiv.org/html/2608.09225v1 (§§5.1–5.9: A100 measurement, simulation, M4 replication and overhead) | https://arxiv.org/html/2608.09225v1 (§7 Limitations) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-09225 | complete |
| SF-2026-ARXIV-2608-09254 | RP-b0345792c47b5deb | standard | arXiv:2608.09254v1 | SRC-ARXIV@arXiv:2608.09254v1; SRC-GITHUB-COMMIT@https://github.com/k-w-lee/query_proof/commit/c5d22984a238f53218507a03199d2d80c0ea2e2c | https://arxiv.org/html/2608.09254v1#S4 (4 Method) | https://arxiv.org/html/2608.09254v1#S5 (5 Experimental setup) | https://arxiv.org/html/2608.09254v1#S7 (7 Limitations) | https://github.com/k-w-lee/query_proof/commit/c5d22984a238f53218507a03199d2d80c0ea2e2c (latest official-repository commit before arXiv v1; 2026-08-10T07:53:22Z; provenance only) | claim:SF-2026-ARXIV-2608-09254 | complete |
| SF-2026-ARXIV-2608-09730 | RP-5cae49069e174e8d | deep | arXiv:2608.09730v1 | SRC-ARXIV@arXiv:2608.09730v1 | https://arxiv.org/html/2608.09730v1 (§§3.2–3.5: World Adapter, exclusive action path, training-time denoiser and branch removal) | https://arxiv.org/html/2608.09730v1 (§§4.1–4.5 plus Appendices A–B: LIBERO, SIMPLER, R1 Pro and RTX 5090D latency) | https://arxiv.org/html/2608.09730v1 (§5 Conclusion and Appendix B.4 Comparability) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-09730 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-09160:start -->
#### SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization

<!-- claim:SF-2026-ARXIV-2608-09160:start -->《SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization》把 `TRAIN-TENSOR-PARALLEL` 的问题具体化为：QK-Norm 的稳定性收益在 TP 下引入额外通信。其机制是仅交换 QK-Norm scalar statistics，并用 persistent kernel 重叠 P2P reduction 与 elementwise work；primary v1 的 evaluation 绑定为近期 LLM 的 multi-GPU TP；测 kernel latency 与 serving TPOT，比较对象为full-vector All-Gather TP QK-Norm 与 optimized scalar aggregation。<!-- claim:SF-2026-ARXIV-2608-09160:end -->

证据支持的范围是：所测拓扑/模型上显著降低 QK-Norm latency 与 TPOT；不支持的外推是：所有互连/shape、训练收敛或跨实现数值等价。旧方案仍有成立条件：full hidden-vector All-Gather；兼容性广且实现直接。新机制获得的收益与代价必须一起读取：少通信换定制 persistent kernel、P2P 同步和维护复杂度。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：互连拥塞、小 tensor、kernel residency 冲突、deadlock 或数值漂移。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供张量切分与 collective的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`TRAIN-TENSOR-PARALLEL`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-09160:end -->

<!-- review:SF-2026-ARXIV-2608-09225:start -->
#### Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference

<!-- claim:SF-2026-ARXIV-2608-09225:start -->KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。<!-- claim:SF-2026-ARXIV-2608-09225:end -->

KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。 共享 prefix cache 原本用跨租户复用换 TTFT/成本，在单信任域中合理；跨主体共享把 hit/miss 变成身份侧信道后，KVGov 将 principal identity 写进 HMAC namespace，并以 boundary salting 保留有限共享。获得隔离的代价是 cache hit 损失、principal lifecycle 与 audit 调度复杂度，模拟防御也不能替代真实多租户攻击复现。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以policy、隔离与执行边界为长期设计约束。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-09225:end -->

<!-- review:SF-2026-ARXIV-2608-09254:start -->
#### Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline

<!-- claim:SF-2026-ARXIV-2608-09254:start -->《Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：歧义、不可回答、schema drift 会产生成功执行但错误数字。其机制是semantic-layer/physical-catalog rules 决定 answer/clarify/abstain/refuse，再用 deterministic checks gate 输出；primary v1 的 evaluation 绑定为WarehouseReliabilityBench：400 frozen tasks、2 synthetic warehouses；80-task test 一次评估，比较对象为direct-prompted 32B、cost-matched few-shot 与 routing ablation。<!-- claim:SF-2026-ARXIV-2608-09254:end -->

证据支持的范围是：该 synthetic split 上 scaffolded 7B 的 Business Truth Rate 方向优于 baselines；不支持的外推是：7B 模型本身优于 32B、真实 warehouse 泛化或 deterministic layer 独立因果贡献。旧方案仍有成立条件：SQL syntax/execution match 加 direct prompt；业务定义稳定时够用。新机制获得的收益与代价必须一起读取：可靠性换 semantic layer 维护与 over-abstention，cost difference 未闭合。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：规则/denominator 过期、template-family CI 不稳或应拒答问题仍被回答。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可复算评估证据的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-09254:end -->

<!-- review:SF-2026-ARXIV-2608-09730:start -->
#### World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

<!-- claim:SF-2026-ARXIV-2608-09730:start -->World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。<!-- claim:SF-2026-ARXIV-2608-09730:end -->

World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。 在线 world-model rollout 直接提供未来，但把视频 denoising 留在控制环会降低频率；纯行为克隆很快，却缺少 dynamics supervision。World Tokens 把未来预测移到训练期，并强制 action expert 只读取 256 个共享 world tokens，部署时删除视频支路；它以训练耦合和表示瓶颈换 VLA 级延迟，开放环境因果正确性仍未由模拟和有限真机证明。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Score rationale：Design Delta：改变了环境状态转移的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MULTIMODAL-WORLD-MODELS`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-09730:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-09225 | multi-tenant prefix-cache timing attacks, defense simulation and independent-stack replication | Qwen2.5-7B-Instruct on vLLM; Qwen2.5-3B on llama.cpp | NVIDIA A100/vLLM 0.26.0 and Apple M4/Metal/llama.cpp | Not Disclosed | A100: 2119-token shared prefix; M4 replication: 781-token shared prefix | one first token measured by TTFT | single probe per measurement; simulation N=1000 trials | multi-tenant threat model; live concurrent-tenant count Not Disclosed | no production SLO; preregistered cached/cold TTFT-ratio breach threshold plus attack-success and audit metrics | real TTFT measurements, deterministic judges and independent llama.cpp replication |
| SF-2026-ARXIV-2608-09730 | LIBERO, SIMPLER and R1 Pro manipulation | Qwen3-VL-2B-Instruct + DiT-B action expert; Cosmos Predict2.5-2B training-only denoiser | RTX 5090D for latency; simulators plus Galaxea R1 Pro | Not Disclosed | multi-view observation and instruction; normalized input-token length Not Disclosed; 256 world tokens are an internal bottleneck | eight-step action chunk | Not Disclosed | single robot control loop; evaluation trial counts are not serving concurrency | success rate and per-action-chunk latency; no production SLO | LIBERO/SIMPLER task success and R1 Pro trial protocol; comparisons include matched Qwen-GR00T and published VLA/WAM baselines |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-09225 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260811-2608-09225 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=shared-prefix performance identity also becomes tenant authorization identity | analysis:DA-20260811-2608-09225 |
| SF-2026-ARXIV-2608-09730 | score_7_9<br>potential_books_delta | selected | DA-20260811-2608-09730 | — | 逐 family 排序：override=none，V2=8/9 (3/3/2)；保留独立机制、证据边界与 Books Decision；pre-Books delta=world-model transition supervision becomes a training-only branch, not only online rollout | analysis:DA-20260811-2608-09730 |

<!-- analysis:DA-20260811-2608-09225:start -->
### Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference

KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。 共享 prefix cache 原本用跨租户复用换 TTFT/成本，在单信任域中合理；跨主体共享把 hit/miss 变成身份侧信道后，KVGov 将 principal identity 写进 HMAC namespace，并以 boundary salting 保留有限共享。获得隔离的代价是 cache hit 损失、principal lifecycle 与 audit 调度复杂度，模拟防御也不能替代真实多租户攻击复现。

<!-- analysis:DA-20260811-2608-09225:end -->

<!-- analysis:DA-20260811-2608-09730:start -->
### World Tokens: Enhancing Embodied Policies with Training-Time World Modeling

World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。 在线 world-model rollout 直接提供未来，但把视频 denoising 留在控制环会降低频率；纯行为克隆很快，却缺少 dynamics supervision。World Tokens 把未来预测移到训练期，并强制 action expert 只读取 256 个共享 world tokens，部署时删除视频支路；它以训练耦合和表示瓶颈换 VLA 级延迟，开放环境因果正确性仍未由模拟和有限真机证明。

<!-- analysis:DA-20260811-2608-09730:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-09225 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L608 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2608-09225 | delta:SF-2026-ARXIV-2608-09225 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2608-09225 |
| SF-2026-ARXIV-2608-09730 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14<br>books/part-03-multimodal-world-models/25-multimodal-world-models.md#L276 | books/part-03-multimodal-world-models/23-multimodal-representation.md#L14<br>books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14 | existing:SF-2026-ARXIV-2608-09730 | delta:SF-2026-ARXIV-2608-09730 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2608-09730 |

<!-- books-review:SF-2026-ARXIV-2608-09225:start --><!-- existing:SF-2026-ARXIV-2608-09225:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2608-09225:end --><!-- delta:SF-2026-ARXIV-2608-09225:start -->KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。<!-- delta:SF-2026-ARXIV-2608-09225:end -->与上述中心命题相比，这个 family 的新增证据是：KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-09225:end -->

<!-- books-review:SF-2026-ARXIV-2608-09730:start --><!-- existing:SF-2026-ARXIV-2608-09730:start -->现有中心命题：World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。<!-- existing:SF-2026-ARXIV-2608-09730:end --><!-- delta:SF-2026-ARXIV-2608-09730:start -->World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。<!-- delta:SF-2026-ARXIV-2608-09730:end -->与上述中心命题相比，这个 family 的新增证据是：World Tokens 在训练时让 future-video denoising 与 action expert 共享固定 world tokens，并通过 exclusive routing 防止策略绕过该表示；部署时移除 world-model branch。它把 world modeling 作为 representation supervision 而非在线 simulator，代价是训练耦合，且 LIBERO/SIMPLER/有限真机结果不能证明开放环境因果正确性。 该 delta 已落在《第25章 World Models：从生成画面到预测环境》的正文机制锚点；语义相邻边界为 MULTIMODAL-REPRESENTATION：多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。；MULTIMODAL-EMBODIED-VLA：Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-09730:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260811-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260811; coverage:SRC-GITHUB-COMMIT:20260811; semantic-review:SA-20260811-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260811-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-09160; review:SF-2026-ARXIV-2608-09225; review:SF-2026-ARXIV-2608-09254; review:SF-2026-ARXIV-2608-09730; semantic-review:SA-20260811-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260811-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260811-2608-09225; analysis:DA-20260811-2608-09730; semantic-review:SA-20260811-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260811-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-09225; books-review:SF-2026-ARXIV-2608-09730; review:SF-2026-ARXIV-2608-09160; review:SF-2026-ARXIV-2608-09254; semantic-review:SA-20260811-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260811-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260811-COVERAGE:end -->
<!-- semantic-review:SA-20260811-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260811-EVIDENCE:end -->
<!-- semantic-review:SA-20260811-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260811-SELECTION:end -->
<!-- semantic-review:SA-20260811-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260811-BOOKS:end -->

## 8. Ignored Noise

601 条 arXiv v1 中有 597 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：2 个 `Integrate`、0 个 `No Change — Existing Coverage`、2 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/11/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-03-multimodal-world-models/25-multimodal-world-models.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-06-ai-infrastructure/72-security.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization](https://arxiv.org/abs/2608.09160v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference](https://arxiv.org/abs/2608.09225v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Business Truth, not SQL Accuracy: A Rule-Gated 7B Analytics Agent Outperforms a Direct-Prompted 32B Baseline](https://arxiv.org/abs/2608.09254v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
