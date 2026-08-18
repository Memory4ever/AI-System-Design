# Daily Research — 2026-08-19

**Research Date:** 2026-08-19

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-18 09:00:00 ～ 2026-08-19 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-18 09:00:00` 至 `2026-08-19 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 449 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 4 个候选：2 个 Deep Review、2 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-TENSORRT-LLM` 中由《TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration》暴露的状态/证据边界；`PLATFORM-SECURITY` 中由《FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-19 |
| Window End | 2026-08-19 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-19-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-18T09:00:00+08:00 | 2026-08-19T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 449 | SF-2026-ARXIV-2608-17336<br>SF-2026-ARXIV-2608-17442<br>SF-2026-ARXIV-2608-17616<br>SF-2026-ARXIV-2608-17756 | page count=7 snapshot files; final_cursor=end; daily-window total=449; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-19T09:00:00+08:00 | coverage:SRC-ARXIV:20260819 | — |
| SRC-GITHUB-COMMIT | 2026-08-18T09:00:00+08:00 | 2026-08-19T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-17336: https://api.github.com/repos/HanzhiZhang-Ulrica/TileMix/commits?until=2026-08-18T03:53:02Z&per_page=1; per-family event-time recovery | checked | 1 | SF-2026-ARXIV-2608-17336 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-19T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260819 | — |

<!-- coverage:SRC-ARXIV:20260819:start -->submittedDate query filtered to [2026-08-18T09:00:00+08:00, 2026-08-19T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 4 routed families.<!-- coverage:SRC-ARXIV:20260819:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260819:start -->GitHub Commit API recovered and froze 1 repository commit(s): SF-2026-ARXIV-2608-17336: repository=HanzhiZhang-Ulrica/TileMix; until=2026-08-18T03:53:02Z; sha=3eee6c9e0267b7579f24e2025cea0e5fdc211efa; commit_timestamp=2026-08-18T03:26:42Z; commit_url=https://github.com/HanzhiZhang-Ulrica/TileMix/commit/3eee6c9e0267b7579f24e2025cea0e5fdc211efa; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260819:end -->

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
| SF-2026-ARXIV-2608-17336 | arXiv:2608.17336v1 | paper-v1:2608.17336 | 2026-W34 | 2026-08-18 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-17336 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2608-17336 | yes |
| SF-2026-ARXIV-2608-17442 | arXiv:2608.17442v1 | paper-v1:2608.17442 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2608-17442 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2608-17442 | yes |
| SF-2026-ARXIV-2608-17616 | arXiv:2608.17616v1 | paper-v1:2608.17616 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-17616 | self | — | new_in_window | MODEL-LONG-CONTEXT | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-17756 | arXiv:2608.17756v1 | paper-v1:2608.17756 | 2026-W34 | 2026-08-18 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-17756 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-17336 | RP-be5e9fc21eff550a | deep | arXiv:2608.17336v1 | SRC-ARXIV@arXiv:2608.17336v1; SRC-GITHUB-COMMIT@https://github.com/HanzhiZhang-Ulrica/TileMix/commit/3eee6c9e0267b7579f24e2025cea0e5fdc211efa | https://arxiv.org/html/2608.17336v1 (§§4.1–4.3 and Appendices B–D: tile-group routing, bitmask encoding and mixed-precision execution) | https://arxiv.org/html/2608.17336v1 (§§5.1–5.4 and Appendices E–G: LongEval/LV-Eval quality, A100 efficiency and numerical behavior) | https://arxiv.org/html/2608.17336v1 (§5.4 and Appendix G.1–G.5: sequence/depth accumulation, pattern exposure and kernel-numerics boundaries) | https://github.com/HanzhiZhang-Ulrica/TileMix/commit/3eee6c9e0267b7579f24e2025cea0e5fdc211efa (event-time commit 2026-08-18T03:26:42Z) | claim:SF-2026-ARXIV-2608-17336 | complete |
| SF-2026-ARXIV-2608-17442 | RP-9654eeca469ed61a | deep | arXiv:2608.17442v1 | SRC-ARXIV@arXiv:2608.17442v1 | https://arxiv.org/html/2608.17442v1 (§IV, §§V-A–V-F, §§VI-A–VI-D and §VII: factorized HEScan, resident blocks, MPC nonlinearities and conversion) | https://arxiv.org/html/2608.17442v1 (§VIII, §§IX-A–IX-F and Appendices F/G/I: three long-document tasks, A100 runs, baselines, accuracy, memory and scaling) | https://arxiv.org/html/2608.17442v1 (§II-C, §XI and Appendices D/G: semi-honest threat model, approximation, 77.3-minute latency, refresh and sequence/memory feasibility boundary) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-17442 | complete |
| SF-2026-ARXIV-2608-17616 | RP-09e09e67c1f5ca3b | standard | arXiv:2608.17616v1 | SRC-ARXIV@arXiv:2608.17616v1 | https://arxiv.org/html/2608.17616v1#S3 (3 MoNe: Modular Neural Memory for Pretrained Transformer Attention) | https://arxiv.org/html/2608.17616v1#S4 (4 Experiments) | https://arxiv.org/html/2608.17616v1#S5 (5 Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-17616 | complete |
| SF-2026-ARXIV-2608-17756 | RP-e89e53c572a21224 | standard | arXiv:2608.17756v1 | SRC-ARXIV@arXiv:2608.17756v1 | https://arxiv.org/html/2608.17756v1#Sx2 (D 2 ACCI Framework) | https://arxiv.org/html/2608.17756v1#Sx3 (Experiments) | https://arxiv.org/html/2608.17756v1#Sx5 (Conclusion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-17756 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-17336:start -->
#### TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

<!-- claim:SF-2026-ARXIV-2608-17336:start -->TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。<!-- claim:SF-2026-ARXIV-2608-17336:end -->

TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。 显存充足时统一 FP attention 最容易保持数值行为，统一 low-bit 则无法表达 tile sensitivity；长上下文让 score/KV 带宽成为约束后，TileMix 以 tile group 在 INT8/FP16 间路由，并用 bitmask 与 kernel 支持 mixed execution。它以 calibration metadata 和 kernel complexity 换吞吐/显存收益；序列深度误差累积和硬件迁移仍会改变最优边界。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了编译后的执行计划的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以可移植性、kernel 与静态内存为长期设计约束。
- Knowledge owner：`INFER-TENSORRT-LLM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17336:end -->

<!-- review:SF-2026-ARXIV-2608-17442:start -->
#### FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models

<!-- claim:SF-2026-ARXIV-2608-17442:start -->FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。<!-- claim:SF-2026-ARXIV-2608-17442:end -->

FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。 encrypted Transformer 在短序列、既有 protocol 和硬件充足时仍有成熟语义与对照基础；长文档使 token-pair work、密文状态驻留和 conversion 成为主瓶颈后，FESC 用 factorized scan-contract、resident chunks 与 hybrid CKKS/MPC 把复杂度转向线性 recurrence。代价是近似友好训练、两方 semi-honest 假设、分钟级 latency、refresh 通信和专用 kernel；交互服务、并发与更大模型仍是下一阶段压力。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了授权与安全证据的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以policy、隔离与执行边界为长期设计约束。
- Knowledge owner：`PLATFORM-SECURITY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17442:end -->

<!-- review:SF-2026-ARXIV-2608-17616:start -->
#### MoNe: Modular Neural Memory for Efficient Long Context Inference

<!-- claim:SF-2026-ARXIV-2608-17616:start -->《MoNe: Modular Neural Memory for Efficient Long Context Inference》把 `MODEL-LONG-CONTEXT` 的问题具体化为：上下文长度使每次查询重读全部 KV 成为瓶颈。其机制是把长上下文分段写入 layer-local fast-weight memory，查询时只保留 query KV；primary v1 的 evaluation 绑定为128K frozen Transformer、RULER 与 ICL baselines；报告计算、内存和参数开销，比较对象为完整 in-context KV 或直接扩展上下文。<!-- claim:SF-2026-ARXIV-2608-17616:end -->

证据支持的范围是：作者设置中实现 O(N) 预处理、O(1) 查询状态并减少所测计算/内存；不支持的外推是：任意推理、服务并发或多查询复用均保持质量。旧方案仍有成立条件：短上下文或一次查询时完整 ICL 最直接。新机制获得的收益与代价必须一起读取：查询成本换预处理、额外参数、memory TTL 和压缩误差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：memory 污染、顺序敏感、query mismatch 或过期状态。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供长序列表示的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`MODEL-LONG-CONTEXT`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17616:end -->

<!-- review:SF-2026-ARXIV-2608-17756:start -->
#### D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory

<!-- claim:SF-2026-ARXIV-2608-17756:start -->《D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：多阶段系统的局部失败会被最终平均分掩盖。其机制是用 paired evidence、protected slices 和可定位 trace 的 outer gate 形成可复算 promotion contract；primary v1 的 evaluation 绑定为MemStack、LoCoMo、LongMemEval、PersonaMem，六项 ablation，对比 aggregate/result-only logs，比较对象为只看 aggregate score 或最终结果日志。<!-- claim:SF-2026-ARXIV-2608-17756:end -->

证据支持的范围是：作者任务中能更可靠定位 memory-system 退化并支持 promotion 决策；不支持的外推是：它证明调度/goodput、通用因果解释或所有生产故障。旧方案仍有成立条件：低风险单阶段模型中 aggregate score 成本更低。新机制获得的收益与代价必须一起读取：诊断性换 paired runs、trace、切片统计和多重检验成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：instrumentation 缺失、slice 选择偏差、指标 gaming 或共因错误。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供可复算评估证据的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-17756:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-17336 | long-context mixed-precision attention | LLaMA, Qwen and Vicuna families | NVIDIA A100 40GB | INT8 and FP16 score paths with INT8 KV support | LongEval prompts 3.1K–38.7K; LV-Eval 16K/32K/64K; implementation prefill shapes 1K–8K | task answers; normalized output length Not Disclosed in v1 | throughput batch 8 with 3 warmups and 5 timed runs | Not Disclosed — v1 does not state normalized multi-request concurrency beyond batch | quality–prefill-throughput frontier; no production SLO | LongEval, LV-Eval and A100 prefill benchmarks across the disclosed Tables 6–14 and Figures 8–9 |
| SF-2026-ARXIV-2608-17442 | private long-document classification with hybrid CKKS/MPC selective SSM inference | 12-layer Mamba-base distilled from Mamba-2-130M; BERT-base and prior private-inference systems as references | one NVIDIA A100 40GB for main native runs; six GPU classes in portability study | CKKS approximate arithmetic plus MPC nonlinear protocols and approximation-aware fine-tuning | 128–4096 tokens in audited/native runs; 8192-token refreshed extension | single document classification/scoring output | single-query inference | two-party semi-honest protocol; no serving-concurrency contract | accuracy, end-to-end latency, communication and peak memory; no production SLO | SCOTUS, arXiv and Patent classification; AEGIS/MPCFormer/SIGMA/SHAFT/BOLT/BumbleBee/BLB/EncFormer/MPCMamba baselines |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-17442 | score_7_9<br>forced_review<br>potential_books_delta | selected | DA-20260819-2608-17442 | — | 逐 family 排序：override=release_security_contract，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=private long-context inference splits HE linear work, MPC nonlinear work and domain transitions | analysis:DA-20260819-2608-17442 |
| SF-2026-ARXIV-2608-17336 | score_7_9<br>potential_books_delta | selected | DA-20260819-2608-17336 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=mixed precision moves from model-wide configuration to tile/operator-aware execution planning | analysis:DA-20260819-2608-17336 |

<!-- analysis:DA-20260819-2608-17442:start -->
### FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models

FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。 encrypted Transformer 在短序列、既有 protocol 和硬件充足时仍有成熟语义与对照基础；长文档使 token-pair work、密文状态驻留和 conversion 成为主瓶颈后，FESC 用 factorized scan-contract、resident chunks 与 hybrid CKKS/MPC 把复杂度转向线性 recurrence。代价是近似友好训练、两方 semi-honest 假设、分钟级 latency、refresh 通信和专用 kernel；交互服务、并发与更大模型仍是下一阶段压力。

<!-- analysis:DA-20260819-2608-17442:end -->

<!-- analysis:DA-20260819-2608-17336:start -->
### TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration

TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。 显存充足时统一 FP attention 最容易保持数值行为，统一 low-bit 则无法表达 tile sensitivity；长上下文让 score/KV 带宽成为约束后，TileMix 以 tile group 在 INT8/FP16 间路由，并用 bitmask 与 kernel 支持 mixed execution。它以 calibration metadata 和 kernel complexity 换吞吐/显存收益；序列深度误差累积和硬件迁移仍会改变最优边界。

<!-- analysis:DA-20260819-2608-17336:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-17336 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14<br>books/part-05-inference-system/49-tensorrt-llm.md#L677 | books/part-02-model/17-transformer-layer.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-17336 | delta:SF-2026-ARXIV-2608-17336 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-17336 |
| SF-2026-ARXIV-2608-17442 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L14<br>books/part-06-ai-infrastructure/72-security.md#L602 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14<br>books/part-07-agent/78-tool-calling.md#L14 | existing:SF-2026-ARXIV-2608-17442 | delta:SF-2026-ARXIV-2608-17442 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2608-17442 |

<!-- books-review:SF-2026-ARXIV-2608-17336:start --><!-- existing:SF-2026-ARXIV-2608-17336:start -->现有中心命题：TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。<!-- existing:SF-2026-ARXIV-2608-17336:end --><!-- delta:SF-2026-ARXIV-2608-17336:start -->TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。<!-- delta:SF-2026-ARXIV-2608-17336:end -->与上述中心命题相比，这个 family 的新增证据是：TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。 该 delta 已落在《第49章 高性能 GPU 推理执行：以 TensorRT-LLM 为例》的正文机制锚点；语义相邻边界为 MODEL-TRANSFORMER-LAYER：Transformer Layer 是一个保持 residual stream shape 不变、并显式管理跨层信息与梯度路径的可堆叠状态更新单元。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-17336:end -->

<!-- books-review:SF-2026-ARXIV-2608-17442:start --><!-- existing:SF-2026-ARXIV-2608-17442:start -->现有中心命题：AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。<!-- existing:SF-2026-ARXIV-2608-17442:end --><!-- delta:SF-2026-ARXIV-2608-17442:start -->FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。<!-- delta:SF-2026-ARXIV-2608-17442:end -->与上述中心命题相比，这个 family 的新增证据是：FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。 该 delta 已落在《第72章 Security》的正文机制锚点；语义相邻边界为 PLATFORM-MULTI-TENANT：Multi-tenancy 是 tenant identity 在 control、data、resource 与 evidence planes 上的一致执行。Namespace 是重要机制，但不是完整租户模型。；AGENT-TOOL-CALLING：模型产生 tool intent 与 typed arguments，可信执行器完成 discovery、validation、authorization、execution 和 observation。Tool use 扩大能力，也把错误从文本域放大到真实环境。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-17442:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260819-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260819; coverage:SRC-GITHUB-COMMIT:20260819; semantic-review:SA-20260819-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260819-EVIDENCE | fresh-context:contract-adversary | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-17336; review:SF-2026-ARXIV-2608-17442; review:SF-2026-ARXIV-2608-17616; review:SF-2026-ARXIV-2608-17756; semantic-review:SA-20260819-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260819-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260819-2608-17336; analysis:DA-20260819-2608-17442; semantic-review:SA-20260819-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260819-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-17336; books-review:SF-2026-ARXIV-2608-17442; review:SF-2026-ARXIV-2608-17616; review:SF-2026-ARXIV-2608-17756; semantic-review:SA-20260819-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260819-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260819-COVERAGE:end -->
<!-- semantic-review:SA-20260819-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260819-EVIDENCE:end -->
<!-- semantic-review:SA-20260819-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260819-SELECTION:end -->
<!-- semantic-review:SA-20260819-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260819-BOOKS:end -->

## 8. Ignored Noise

449 条 arXiv v1 中有 445 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：2 个 `Integrate`、0 个 `No Change — Existing Coverage`、2 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/19/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-05-inference-system/49-tensorrt-llm.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-06-ai-infrastructure/72-security.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [TileMix: Tile-Centric Mixed-Precision Attention for LLM Inference Acceleration](https://arxiv.org/abs/2608.17336v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [FESC: Remodeling Long-Context Private Inference with Encrypted State-Space Models](https://arxiv.org/abs/2608.17442v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [MoNe: Modular Neural Memory for Efficient Long Context Inference](https://arxiv.org/abs/2608.17616v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [D$^2$ACCI: A Dual-Loop Diagnostic Protocol for Evidence-Preserving Agent Memory](https://arxiv.org/abs/2608.17756v1) — published/event date: 2026-08-18; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
