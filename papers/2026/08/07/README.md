# Daily Research — 2026-08-07

**Research Date:** 2026-08-07

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-06 09:00:00 ～ 2026-08-07 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-06 09:00:00` 至 `2026-08-07 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 502 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 4 个候选：2 个 Deep Review、2 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`AGENT-MULTI-AGENT` 中由《A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems》暴露的状态/证据边界；`INFER-SCHEDULING` 中由《Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-07 |
| Window End | 2026-08-07 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-07-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-06T09:00:00+08:00 | 2026-08-07T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 502 | SF-2026-ARXIV-2608-06434<br>SF-2026-ARXIV-2608-05738<br>SF-2026-ARXIV-2608-05791<br>SF-2026-ARXIV-2608-06557 | page count=7 snapshot files; final_cursor=end; daily-window total=502; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-07T09:00:00+08:00 | coverage:SRC-ARXIV:20260807 | — |

<!-- coverage:SRC-ARXIV:20260807:start -->submittedDate query filtered to [2026-08-06T09:00:00+08:00, 2026-08-07T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 4 routed families.<!-- coverage:SRC-ARXIV:20260807:end -->

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
| SF-2026-ARXIV-2608-06434 | arXiv:2608.06434v1 | paper-v1:2608.06434 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-06434 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05738 | arXiv:2608.05738v1 | paper-v1:2608.05738 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-05738 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-05791 | arXiv:2608.05791v1 | paper-v1:2608.05791 | 2026-W32 | 2026-08-06 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-05791 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2608-05791 | yes |
| SF-2026-ARXIV-2608-06557 | arXiv:2608.06557v1 | paper-v1:2608.06557 | 2026-W32 | 2026-08-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-06557 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2608-06557 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-06434 | RP-f7127fad8ad02aa8 | standard | arXiv:2608.06434v1 | SRC-ARXIV@arXiv:2608.06434v1 | https://arxiv.org/html/2608.06434v1#S3 (III Method) | https://arxiv.org/html/2608.06434v1#S4 (IV Experiments) | https://arxiv.org/html/2608.06434v1#S5 (V Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-06434 | complete |
| SF-2026-ARXIV-2608-05738 | RP-ebb289857ec771fb | standard | arXiv:2608.05738v1 | SRC-ARXIV@arXiv:2608.05738v1 | https://arxiv.org/html/2608.05738v1#Sx3 (Method) | https://arxiv.org/html/2608.05738v1#Sx4 (Experiments) | https://arxiv.org/html/2608.05738v1#Sx5 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-05738 | complete |
| SF-2026-ARXIV-2608-05791 | RP-3bb40368284dd536 | deep | arXiv:2608.05791v1 | SRC-ARXIV@arXiv:2608.05791v1 | https://arxiv.org/html/2608.05791v1#S3 (§§3.1–3.3: framework, replica parallelism and dependency-aware structural parallelism) | https://arxiv.org/html/2608.05791v1#S4.SS1 (§4.1 GAIA setup)<br>https://arxiv.org/html/2608.05791v1#S4.SS2 (§4.2 main results)<br>https://arxiv.org/html/2608.05791v1#S4.SS3 (§4.3 critical-path and ablation analysis) | https://arxiv.org/html/2608.05791v1#S4.SS4 (§4.4 regime, cost and generalization discussion)<br>https://arxiv.org/html/2608.05791v1#S4.SS5 (§4.5 Failure Analysis)<br>https://arxiv.org/html/2608.05791v1#A4 (Appendix D Sensitivity and Limitations) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-05791 | complete |
| SF-2026-ARXIV-2608-06557 | RP-b41fa9bec33984a1 | deep | arXiv:2608.06557v1 | SRC-ARXIV@arXiv:2608.06557v1 | https://arxiv.org/html/2608.06557v1#S4 (§IV Cascade: latency estimator, dynamic budget tracking, feasible KV restoration and implementation) | https://arxiv.org/html/2608.06557v1#S5 (§V Evaluation: three-model production traces, goodput, SLO violations and fairness) | Not Disclosed — v1 has no standalone limitations or prediction-error sensitivity section; bounded counterevidence is https://arxiv.org/html/2608.06557v1#S5.SS2 (§V-B SLO violations), https://arxiv.org/html/2608.06557v1#S5.SS3 (§V-C heterogeneous-traffic fairness), https://arxiv.org/html/2608.06557v1#S5.SS4 (§V-D capacity/load sensitivity), and https://arxiv.org/html/2608.06557v1#S2.SS2 (§II-B PD-co-located and multi-tier-KV scope) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-06557 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-06434:start -->
#### Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection

<!-- claim:SF-2026-ARXIV-2608-06434:start -->《Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：既需长程规划又需高频闭环时，紧耦合限制模型替换并使 slow path 持续拖累频率。其机制是用 RL switching policy 根据实时环境反馈在完全解耦的大型 deliberative VLA 与轻量 reactive VLA 间选择，而非让 fast module 依赖 slow hidden representation；primary v1 的 evaluation 绑定为LIBERO simulation 与真实双臂 manipulation，比较 task success、effective action frequency 与完成时间，比较对象为紧耦合 dual-system VLA 端到端联合训练，fast controller 读取 slow intermediate state。<!-- claim:SF-2026-ARXIV-2608-06434:end -->

证据支持的范围是：在作者 simulation/real-robot 配置中，环境感知 switching 以稀疏 slow invocation 保持接近 large baseline 的 success，并提高 action frequency；不支持的外推是：作者测得的 action frequency 对其他硬件/robot 成立、RL selector 不影响安全，或 success comparable 等于 failure tail 相同。旧方案仍有成立条件：任务动态低、单一模型满足频率或已有稳定 hierarchical controller 时，固定切换更易验证。新机制获得的收益与代价必须一起读取：解耦支持替换并稀疏调用 slow model，但新增 selector policy、跨模型 state handoff 和一致性验证。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：selector 误判、slow plan 过期、两系统动作语义不一致、反馈延迟、distribution shift 或 safety envelope 被绕过。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-06434:end -->

<!-- review:SF-2026-ARXIV-2608-05738:start -->
#### In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use

<!-- claim:SF-2026-ARXIV-2608-05738:start -->《In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use》把 `MULTIMODAL-EMBODIED-VLA` 的问题具体化为：free-form reasoning 既增加闭环 latency，又让 narration token 与 action objective 冲突。其机制是不让 VLA 生成 free-form CoT，而以结构化 perceptual context 只监督 action，并允许 policy 调用 detector、depth 与 VLM 工具主动获得 grounded language；primary v1 的 evaluation 绑定为RoboCasa-GR1、SimplerEnv、LIBERO 及八项真机 manipulation，在 matched configuration 下比较 CoT-based VLA，比较对象为behavior cloning 只读 static image/instruction，或在 action 前生成自由文本 CoT。<!-- claim:SF-2026-ARXIV-2608-05738:end -->

证据支持的范围是：作者 matched evaluation 与分析中，消费 grounded language 的 action-only 路径在所测任务上兼顾效率和成功率，而 free-form CoT 暴露 latency/objective conflict；不支持的外推是：所有语言推理都会伤害控制、工具 observation 总是可靠，或仿真/八任务结果证明开放环境安全。旧方案仍有成立条件：任务简单、instruction 充分且工具调用成本高时，直接 behavior cloning action chunk 最稳定。新机制获得的收益与代价必须一起读取：从生成语言改为消费 grounded language 可保留控制频率，但依赖工具 orchestration、schema 和 observation freshness。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：detector/depth/VLM 错误、tool latency、语言证据与当前 frame 失配、未见 paraphrase 或 action supervision 偏差。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供感知到动作的闭环状态的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MULTIMODAL-EMBODIED-VLA`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05738:end -->

<!-- review:SF-2026-ARXIV-2608-05791:start -->
#### A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems

<!-- claim:SF-2026-ARXIV-2608-05791:start -->论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。<!-- claim:SF-2026-ARXIV-2608-05791:end -->

论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。 把并行等同为复制更多独立样本，在任务可分且无共享副作用时最直接；一旦 Agent workflow 内部存在依赖边、工具状态和串行 critical path，replica parallelism 不能缩短单条轨迹。论文把控制点拆成跨样本 replica 与图内 structural parallelism，换取更精细的依赖调度；代价是通信、状态一致性和副作用协调，下一阶段压力是可恢复的 workflow state，而不只是更多并发。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了共享状态与协作拓扑的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以并行收益、通信与共识为长期设计约束。
- Knowledge owner：`AGENT-MULTI-AGENT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-05791:end -->

<!-- review:SF-2026-ARXIV-2608-06557:start -->
#### Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving

<!-- claim:SF-2026-ARXIV-2608-06557:start -->Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。<!-- claim:SF-2026-ARXIV-2608-06557:end -->

Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。 按到达顺序或固定优先级调度，并将 KV 分层动作视为独立策略，在负载稳定且 SLO 宽松时简单；当请求 deadline、剩余服务时间和 restore/prefetch 共同决定可行性时，Cascade 以 latency budget 统一排序与 KV 决策。它以预测器和跨层调度复杂度换 goodput/fairness，预测误差、存储拥塞和租户公平仍会造成尾延迟。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了请求调度与资源所有权的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以goodput、公平性与 SLO为长期设计约束。
- Knowledge owner：`INFER-SCHEDULING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-06557:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-05791 | GAIA Level 1–3 multi-agent workflows with stratified repeats | Qwen-Plus; cross-backbone validation is a separate appendix scope | 4× Intel Xeon Platinum 8352V CPUs at 2.10GHz | Not Required — remote model API; local numeric precision is not part of the evaluation contract | task-dependent GAIA prompt and tool context | task-dependent answer/trajectory; normalized output length Not Disclosed | default replica count n=3 with Top-K judge selection k=2 | Python asynchronous workflow execution; exact simultaneous task count Not Disclosed | GAIA task outcome, token consumption and critical-path latency | GAIA official evaluator; Magentic-One baseline; §4.1–4.5, Tables 1–2 and Appendix A.3/D |
| SF-2026-ARXIV-2608-06557 | two-hour ChatBot, Tool&Agent, Coder, Reasoning and mixed production-trace serving across ten trace mixes | Qwen-2.5-72B, Llama-3-70B and Llama-3-405B; TP=4 | NVIDIA GB200 NVL72 profiles; 9 Qwen-2.5-72B, 6 Llama-3-70B and 12 Llama-3-405B instances in the default mixed cluster | NVFP4 model weights and FP8 KV cache | Table II p50/p95/p99 input tokens: 574–4,540 / 2,491–16,221 / 6,294–24,972 by base class; mixed p50/p95/p99=886/10,749/13,792 | Table II p50/p95/p99 output tokens: 39–1,665 / 328–12,669 / 1,006–34,686 by base class; mixed=86/1,478/4,812 | chunked-prefill chunk size 512; maximum batch size 128 | trace arrival rates 1.5–37.46 QPS; runtime concurrency emerges from arrivals and batching | p90 TTFT≤10× isolated and p90 TPOT≤5× isolated; Table III absolute TTFT/TPOT targets are model/class-specific | vLLM-v1/Vidur trace replay; FCFS, EDF, SJF and E2 baselines; goodput and SLO violation |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-06557 | score_7_9<br>potential_books_delta | selected | DA-20260807-2608-06557 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=static priority becomes consumable, exhaustible and auditable SLO slack | analysis:DA-20260807-2608-06557 |
| SF-2026-ARXIV-2608-05791 | score_7_9<br>potential_books_delta | selected | DA-20260807-2608-05791 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=replica and structural parallelism impose different multi-Agent state-decomposition contracts | analysis:DA-20260807-2608-05791 |

<!-- analysis:DA-20260807-2608-06557:start -->
### Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving

Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。 按到达顺序或固定优先级调度，并将 KV 分层动作视为独立策略，在负载稳定且 SLO 宽松时简单；当请求 deadline、剩余服务时间和 restore/prefetch 共同决定可行性时，Cascade 以 latency budget 统一排序与 KV 决策。它以预测器和跨层调度复杂度换 goodput/fairness，预测误差、存储拥塞和租户公平仍会造成尾延迟。

<!-- analysis:DA-20260807-2608-06557:end -->

<!-- analysis:DA-20260807-2608-05791:start -->
### A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems

论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。 把并行等同为复制更多独立样本，在任务可分且无共享副作用时最直接；一旦 Agent workflow 内部存在依赖边、工具状态和串行 critical path，replica parallelism 不能缩短单条轨迹。论文把控制点拆成跨样本 replica 与图内 structural parallelism，换取更精细的依赖调度；代价是通信、状态一致性和副作用协调，下一阶段压力是可恢复的 workflow state，而不只是更多并发。

<!-- analysis:DA-20260807-2608-05791:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-05791 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L14<br>books/part-07-agent/82-multi-agent.md#L388 | books/part-07-agent/81-workflow.md#L14<br>books/part-07-agent/84-agent-platform.md#L14 | existing:SF-2026-ARXIV-2608-05791 | delta:SF-2026-ARXIV-2608-05791 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2608-05791 |
| SF-2026-ARXIV-2608-06557 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L14<br>books/part-05-inference-system/56-inference-scheduling.md#L335 | books/part-05-inference-system/46-continuous-batching.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-06557 | delta:SF-2026-ARXIV-2608-06557 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-06557 |

<!-- books-review:SF-2026-ARXIV-2608-05791:start --><!-- existing:SF-2026-ARXIV-2608-05791:start -->现有中心命题：Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。<!-- existing:SF-2026-ARXIV-2608-05791:end --><!-- delta:SF-2026-ARXIV-2608-05791:start -->论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。<!-- delta:SF-2026-ARXIV-2608-05791:end -->与上述中心命题相比，这个 family 的新增证据是：论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。 该 delta 已落在《第82章 Multi-Agent》的正文机制锚点；语义相邻边界为 AGENT-WORKFLOW：Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。；AGENT-PLATFORM：Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-05791:end -->

<!-- books-review:SF-2026-ARXIV-2608-06557:start --><!-- existing:SF-2026-ARXIV-2608-06557:start -->现有中心命题：推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。<!-- existing:SF-2026-ARXIV-2608-06557:end --><!-- delta:SF-2026-ARXIV-2608-06557:start -->Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。<!-- delta:SF-2026-ARXIV-2608-06557:end -->与上述中心命题相比，这个 family 的新增证据是：Cascade 将 deadline 减去预测剩余服务时间定义为 per-request latency budget，并让调度顺序与 KV restore/prefetch/retain/recompute 共用这一控制量。三模型 production trace 支持作者范围内的 goodput/SLO 结论；服务时间预测误差、深层存储拥塞和跨租户公平性仍会改变收益。 该 delta 已落在《第56章 推理调度》的正文机制锚点；语义相邻边界为 INFER-CONTINUOUS-BATCHING：LLM Serving 的 batch 不是一个静态数组，而是一个会在每个 iteration 重新构造的 token-work 集合。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-06557:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260807-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260807; semantic-review:SA-20260807-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260807-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-06434; review:SF-2026-ARXIV-2608-05738; review:SF-2026-ARXIV-2608-05791; review:SF-2026-ARXIV-2608-06557; semantic-review:SA-20260807-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260807-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260807-2608-05791; analysis:DA-20260807-2608-06557; semantic-review:SA-20260807-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260807-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-05791; books-review:SF-2026-ARXIV-2608-06557; review:SF-2026-ARXIV-2608-06434; review:SF-2026-ARXIV-2608-05738; semantic-review:SA-20260807-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260807-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260807-COVERAGE:end -->
<!-- semantic-review:SA-20260807-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260807-EVIDENCE:end -->
<!-- semantic-review:SA-20260807-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260807-SELECTION:end -->
<!-- semantic-review:SA-20260807-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260807-BOOKS:end -->

## 8. Ignored Noise

502 条 arXiv v1 中有 498 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：2 个 `Integrate`、0 个 `No Change — Existing Coverage`、2 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/07/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/56-inference-scheduling.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-07-agent/82-multi-agent.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [Fast and Accurate: An Adaptive VLA Inference Framework through Environment-aware Model Selection](https://arxiv.org/abs/2608.06434v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use](https://arxiv.org/abs/2608.05738v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [A Two-Tier Perspective on Inference-Time Parallelism in Multi-Agent LLM Systems](https://arxiv.org/abs/2608.05791v1) — published/event date: 2026-08-06; accessed: 2026-08-25
- [Cascade: Exploiting SLO-Aware latency budget for fair and high goodput LLM inference serving](https://arxiv.org/abs/2608.06557v1) — published/event date: 2026-08-07; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
