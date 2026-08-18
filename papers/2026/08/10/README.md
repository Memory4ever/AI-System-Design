# Daily Research — 2026-08-10

**Research Date:** 2026-08-10

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-09 09:00:00 ～ 2026-08-10 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；先冻结全局分母，再按 first-public timestamp 回写 owner Daily

**Status:** Complete；fresh-context Coverage、Selection 与 Books audits 已通过；本次回放不生成 provisional Weekly

## Executive Summary

本日报严格覆盖 `2026-08-09 09:00:00` 至 `2026-08-10 09:00:00`。官方 arXiv API 的冻结快照在该窗口内返回 288 条唯一 v1；经过 AI-System route filter、Source Family 去重与 primary identity 核验后，分母冻结为 14 个候选：2 个 Deep Review、12 个 Standard Review。候选按首次公开时间归属，不按旧日报发现日搬运。

本窗口最值得长期保留的不是孤立论文名，而是以下系统压力：`INFER-KV-CACHE` 中由《DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference》暴露的状态/证据边界；`MULTIMODAL-REPRESENTATION` 中由《VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference》暴露的状态/证据边界。所有作者实验都保留 workload 与 evidence boundary，不转写为通用生产结论。

Books 判断在 Source Review 完成后执行。只有能够定位到当前 owner 具体命题的 family 才写 `No Change — Existing Coverage`；其余高分候选因证据仍是受限实验、诊断或早期系统实例而保留 `Weekly Only — Context`，不以高分自动追加书稿。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-10 |
| Window End | 2026-08-10 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-08-10-0900-v2.1-replay-01 |
| Denominator Frozen At | 2026-08-25T23:59:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-09T09:00:00+08:00 | 2026-08-10T09:00:00+08:00 | 2026-08-25T23:19:00+08:00 | https://export.arxiv.org/api/query; V2.1 replay | checked | 288 | SF-2026-ARXIV-2608-08413<br>SF-2026-ARXIV-2608-08569<br>SF-2026-ARXIV-2608-08600<br>SF-2026-ARXIV-2608-08621<br>SF-2026-ARXIV-2608-08744<br>SF-2026-ARXIV-2608-08800<br>SF-2026-ARXIV-2608-08802<br>SF-2026-ARXIV-2608-08822<br>SF-2026-ARXIV-2608-08829<br>SF-2026-ARXIV-2608-08853<br>SF-2026-ARXIV-2608-08878<br>SF-2026-ARXIV-2608-08881<br>SF-2026-ARXIV-2608-08883<br>SF-2026-ARXIV-2608-08889 | page count=7 snapshot files; final_cursor=end; daily-window total=288; deduplicated by arXiv ID; [archived manifest](../_sources/arxiv-v2.1-replay-20260801-24/README.md) | 2026-08-10T09:00:00+08:00 | coverage:SRC-ARXIV:20260810 | — |
| SRC-GITHUB-COMMIT | 2026-08-09T09:00:00+08:00 | 2026-08-10T09:00:00+08:00 | 2026-08-26T03:45:00+08:00 | SF-2026-ARXIV-2608-08569: https://api.github.com/repos/MM-Speech/VoxZip/commits?until=2026-08-09T08:17:18Z&per_page=1<br>SF-2026-ARXIV-2608-08883: https://api.github.com/repos/AquiLLM/AquiLLM/commits?until=2026-08-09T19:45:35Z&per_page=1; per-family event-time recovery | checked | 2 | SF-2026-ARXIV-2608-08569<br>SF-2026-ARXIV-2608-08883 | page=1; per_page=1; selected first result as latest commit at/before each exact `until`; older-history pages intentionally not traversed/not required; full SHA, commit timestamp and URL retained | 2026-08-10T09:00:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260810 | — |

<!-- coverage:SRC-ARXIV:20260810:start -->submittedDate query filtered to [2026-08-09T09:00:00+08:00, 2026-08-10T09:00:00+08:00); canonical snapshot-manifest sha256:4e6b4bd4e75a28b227c1ca674bae32e7fd08419d0da4c1702a091950d83b78d7 (rows sorted by basename as basename<TAB>sha256(file)<LF>); raw gzip snapshots, exact UTC queries and per-file hashes are archived at papers/2026/08/_sources/arxiv-v2.1-replay-20260801-24/README.md; 14 routed families.<!-- coverage:SRC-ARXIV:20260810:end -->
<!-- coverage:SRC-GITHUB-COMMIT:20260810:start -->GitHub Commit API recovered and froze 2 repository commit(s): SF-2026-ARXIV-2608-08569: repository=MM-Speech/VoxZip; until=2026-08-09T08:17:18Z; sha=8a022160744d64d01cc70da6b3ad019fa4f23ac5; commit_timestamp=2026-08-07T09:42:05Z; commit_url=https://github.com/MM-Speech/VoxZip/commit/8a022160744d64d01cc70da6b3ad019fa4f23ac5 | SF-2026-ARXIV-2608-08883: repository=AquiLLM/AquiLLM; until=2026-08-09T19:45:35Z; sha=6193a3c5b681b22c8d526edcc63ef105a1a39432; commit_timestamp=2026-06-25T17:49:50Z; commit_url=https://github.com/AquiLLM/AquiLLM/commit/6193a3c5b681b22c8d526edcc63ef105a1a39432; commit provenance supports artifact identity only, not the paper's mechanism claim.<!-- coverage:SRC-GITHUB-COMMIT:20260810:end -->

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
| SF-2026-ARXIV-2608-08413 | arXiv:2608.08413v1 | paper-v1:2608.08413 | 2026-W32 | 2026-08-09 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08413 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08569 | arXiv:2608.08569v1 | paper-v1:2608.08569 | 2026-W32 | 2026-08-09 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-08569 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Integrate | books-review:SF-2026-ARXIV-2608-08569 | yes |
| SF-2026-ARXIV-2608-08600 | arXiv:2608.08600v1 | paper-v1:2608.08600 | 2026-W32 | 2026-08-09 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08600 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08621 | arXiv:2608.08621v1 | paper-v1:2608.08621 | 2026-W32 | 2026-08-09 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08621 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08744 | arXiv:2608.08744v1 | paper-v1:2608.08744 | 2026-W32 | 2026-08-09 | SRC-ARXIV | 1 | 2 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08744 | self | — | new_in_window | PLATFORM-COST | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08800 | arXiv:2608.08800v1 | paper-v1:2608.08800 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 3 | 1 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08800 | self | — | new_in_window | TRAIN-PRETRAINING | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08802 | arXiv:2608.08802v1 | paper-v1:2608.08802 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08802 | self | — | new_in_window | TRAIN-GRPO | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08822 | arXiv:2608.08822v1 | paper-v1:2608.08822 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08822 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08829 | arXiv:2608.08829v1 | paper-v1:2608.08829 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08829 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08853 | arXiv:2608.08853v1 | paper-v1:2608.08853 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08853 | self | — | new_in_window | MODEL-MOE | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08878 | arXiv:2608.08878v1 | paper-v1:2608.08878 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2608-08878 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2608-08878 | yes |
| SF-2026-ARXIV-2608-08881 | arXiv:2608.08881v1 | paper-v1:2608.08881 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08881 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08883 | arXiv:2608.08883v1 | paper-v1:2608.08883 | 2026-W33 | 2026-08-10 | SRC-ARXIV<br>SRC-GITHUB-COMMIT | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08883 | self | — | new_in_window | AGENT-MEMORY | Weekly Only — Context | — | no |
| SF-2026-ARXIV-2608-08889 | arXiv:2608.08889v1 | paper-v1:2608.08889 | 2026-W33 | 2026-08-10 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2608-08889 | self | — | new_in_window | TRAIN-RLHF | Weekly Only — Context | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08413 | RP-3ff2f3f82f0ab052 | standard | arXiv:2608.08413v1 | SRC-ARXIV@arXiv:2608.08413v1 | https://arxiv.org/html/2608.08413v1#S2 (2. Dataset Collection and Labeling) | https://arxiv.org/html/2608.08413v1#S3 (3. Agent-Specific Testing Levels and Test Types) | https://arxiv.org/html/2608.08413v1#S8 (8. Threats to Validity) | Not Required — v1 discloses https://github.com/aster-test-generation/tangent-ase-2026, but this Standard claim relies on the paper; the repository was reachable but had no Git commits on 2026-08-26 | claim:SF-2026-ARXIV-2608-08413 | complete |
| SF-2026-ARXIV-2608-08569 | RP-3be27eb975bec52b | deep | arXiv:2608.08569v1 | SRC-ARXIV@arXiv:2608.08569v1; SRC-GITHUB-COMMIT@https://github.com/MM-Speech/VoxZip/commit/8a022160744d64d01cc70da6b3ad019fa4f23ac5 | https://arxiv.org/html/2608.08569v1 (§§3.2.1–3.2.2: semantic-anchored compression and temporally decayed eviction) | https://arxiv.org/html/2608.08569v1 (§§4.1–4.5: six suites, baselines, ablations and efficiency) | https://arxiv.org/html/2608.08569v1 (§5 Limitations) | https://github.com/MM-Speech/VoxZip/commit/8a022160744d64d01cc70da6b3ad019fa4f23ac5 (event-time commit 2026-08-07T09:42:05Z) | claim:SF-2026-ARXIV-2608-08569 | complete |
| SF-2026-ARXIV-2608-08600 | RP-cb3ffd33ef048221 | standard | arXiv:2608.08600v1 | SRC-ARXIV@arXiv:2608.08600v1 | https://arxiv.org/html/2608.08600v1#S4 (4 Method) | https://arxiv.org/html/2608.08600v1#S5 (5 Experiments) | https://arxiv.org/html/2608.08600v1#S6 (6 Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08600 | complete |
| SF-2026-ARXIV-2608-08621 | RP-0c2c4969d2fa3815 | standard | arXiv:2608.08621v1 | SRC-ARXIV@arXiv:2608.08621v1 | https://arxiv.org/html/2608.08621v1#S3 (3 Designing a Marketplace for Business Intelligence) | https://arxiv.org/html/2608.08621v1#S5 (5 Experiments) | https://arxiv.org/html/2608.08621v1#S7 (7 Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08621 | complete |
| SF-2026-ARXIV-2608-08744 | RP-285f3f8074bf6db7 | standard | arXiv:2608.08744v1 | SRC-ARXIV@arXiv:2608.08744v1 | https://arxiv.org/html/2608.08744v1#S2 (2 Method) | https://arxiv.org/html/2608.08744v1#S3 (3 Results) | https://arxiv.org/html/2608.08744v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08744 | complete |
| SF-2026-ARXIV-2608-08800 | RP-765c763cef78ff8c | standard | arXiv:2608.08800v1 | SRC-ARXIV@arXiv:2608.08800v1 | https://arxiv.org/html/2608.08800v1#S3 (3 Dataset); https://arxiv.org/html/2608.08800v1#S4.SS1 (4.1 Experiment Setups); https://arxiv.org/html/2608.08800v1#A1 (Appendix A.1–A.4 setup details) | https://arxiv.org/html/2608.08800v1#S4 (4 Experiments and Results) | https://arxiv.org/html/2608.08800v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08800 | complete |
| SF-2026-ARXIV-2608-08802 | RP-75d8d8a0427c36dd | standard | arXiv:2608.08802v1 | SRC-ARXIV@arXiv:2608.08802v1 | https://arxiv.org/html/2608.08802v1#S3 (3 Method: Prompt-Invariant RLVR) | https://arxiv.org/html/2608.08802v1#S4 (4 Experiments) | https://arxiv.org/html/2608.08802v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08802 | complete |
| SF-2026-ARXIV-2608-08822 | RP-c5fc8d9301703151 | standard | arXiv:2608.08822v1 | SRC-ARXIV@arXiv:2608.08822v1 | https://arxiv.org/html/2608.08822v1#S2 (2 Data Collection and Methods) | https://arxiv.org/html/2608.08822v1#S3 (3 Results) | https://arxiv.org/html/2608.08822v1#S4 (4 Discussion) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08822 | complete |
| SF-2026-ARXIV-2608-08829 | RP-6c429c7581fe373a | standard | arXiv:2608.08829v1 | SRC-ARXIV@arXiv:2608.08829v1 | https://arxiv.org/html/2608.08829v1#S3 (3 Experimental Design) | https://arxiv.org/html/2608.08829v1#S4 (4 Results) | https://arxiv.org/html/2608.08829v1#Sx1 (Limitations) | Not Required — v1 discloses https://github.com/pesolosep/per-instance-layer-steering, but this Standard claim does not use repository code; the declared repository returned 404 on 2026-08-26, so no event-time tree was imported | claim:SF-2026-ARXIV-2608-08829 | complete |
| SF-2026-ARXIV-2608-08853 | RP-b978c13cc8894605 | standard | arXiv:2608.08853v1 | SRC-ARXIV@arXiv:2608.08853v1 | https://arxiv.org/html/2608.08853v1#S4 (4 Fixed-Dispatch Adaptive Aggregation) | https://arxiv.org/html/2608.08853v1#S6 (6 Results) | https://arxiv.org/html/2608.08853v1#S9 (9 Limitations and Planned Revision) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08853 | complete |
| SF-2026-ARXIV-2608-08878 | RP-399b69e0d3e0d6e0 | deep | arXiv:2608.08878v1 | SRC-ARXIV@arXiv:2608.08878v1 | https://arxiv.org/html/2608.08878v1 (§§3.1–3.3: state/action/reward, policy optimization and train/inference split) | https://arxiv.org/html/2608.08878v1 (§§4.1–4.6 plus Appendices D–F: setup, budgets, transfer, ablations and error modes) | https://arxiv.org/html/2608.08878v1 (§5 Limitations and Appendix F.3 Error Mode Analysis) | Not Disclosed — the reviewed v1 paper does not identify a repository/commit used by this replay conclusion | claim:SF-2026-ARXIV-2608-08878 | complete |
| SF-2026-ARXIV-2608-08881 | RP-3b9c36df7341848e | standard | arXiv:2608.08881v1 | SRC-ARXIV@arXiv:2608.08881v1 | https://arxiv.org/pdf/2608.08881v1 (pp. 10–13, Method: seven theory-grounded RAG constructions and experimental design) | https://arxiv.org/pdf/2608.08881v1 (pp. 14–36, Results and Tables 1–3: baseline/RAG, model and dataset effects) | https://arxiv.org/pdf/2608.08881v1 (pp. 4–10 and 36, media-affordance, theory-fit and dataset/model boundary) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08881 | complete |
| SF-2026-ARXIV-2608-08883 | RP-3ec135c431e66eb3 | standard | arXiv:2608.08883v1 | SRC-ARXIV@arXiv:2608.08883v1; SRC-GITHUB-COMMIT@https://github.com/AquiLLM/AquiLLM/commit/6193a3c5b681b22c8d526edcc63ef105a1a39432 | https://arxiv.org/html/2608.08883v1#S3 (3 Improvements to AquiLLM) | Not Required — reviewed v1 full text exposes no standalone controlled-evaluation heading; scope is delimited by https://arxiv.org/html/2608.08883v1#S3 (3 Improvements to AquiLLM) | https://arxiv.org/html/2608.08883v1#S4 (4 Limitations) | https://github.com/AquiLLM/AquiLLM/commit/6193a3c5b681b22c8d526edcc63ef105a1a39432 (latest official-repository commit before arXiv v1; 2026-06-25T17:49:50Z; provenance only) | claim:SF-2026-ARXIV-2608-08883 | complete |
| SF-2026-ARXIV-2608-08889 | RP-1a0f02dc522f559b | standard | arXiv:2608.08889v1 | SRC-ARXIV@arXiv:2608.08889v1 | https://arxiv.org/html/2608.08889v1#S4.SS1 (4.1. Reward Shaping Formulations) | https://arxiv.org/html/2608.08889v1#S2.SS1 (2.1. Tasks and Experimental Setup) | https://arxiv.org/html/2608.08889v1#Sx1 (Limitations) | Not Disclosed — the reviewed v1 full text does not identify an artifact used by this standard disposition | claim:SF-2026-ARXIV-2608-08889 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2608-08413:start -->
#### Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications

<!-- claim:SF-2026-ARXIV-2608-08413:start -->《Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：多步交互、工具和非功能风险不能由传统单元测试覆盖率代表。其机制是矿取开源 agent tests、人工标注 2572 个 test methods，并以访谈校验 23 类模式 taxonomy；primary v1 的 evaluation 绑定为240 modules、2572 tests，加 10 位资深从业者访谈，比较对象为开源实践与行业访谈的描述性对照；没有 intervention baseline。<!-- claim:SF-2026-ARXIV-2608-08413:end -->

证据支持的范围是：该样本的测试以窄 unit、heavy mock 与 shallow assertion 为主；不支持的外推是：所有 agent 项目都如此，或某测试策略具有因果优势。旧方案仍有成立条件：用通用 benchmark 或单元覆盖率代表测试成熟度；对简单工具链仍有用。新机制获得的收益与代价必须一起读取：大规模可见性换人工标签、仓库选择偏差和描述性而非因果证据。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：项目/语言/模块抽样偏差、不可见运行语义与访谈自报偏差。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08413:end -->

<!-- review:SF-2026-ARXIV-2608-08569:start -->
#### VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference

<!-- claim:SF-2026-ARXIV-2608-08569:start -->VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。<!-- claim:SF-2026-ARXIV-2608-08569:end -->

VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。 文本 KV eviction 假设 token 的语义密度和时间结构近似文本；语音 token 冗余、连续且含副语言信息后，这个假设失效。VoxZip 先用 ASR anchor 压缩时间轴，再按衰减注意力淘汰，以 ASR 依赖和在线漂移风险换更小 KV；因此它是 speech-specific branch，而不是统一替代文本压缩。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Score rationale：Design Delta：改变了系统状态的表示、控制点或验证路径；System Reach：影响集中在该 owner 或受限 workload；Durability：结论以正确性、成本与可维护性为长期设计约束。
- Knowledge owner：`MULTIMODAL-REPRESENTATION`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08569:end -->

<!-- review:SF-2026-ARXIV-2608-08600:start -->
#### Population-Scalable Multi-Agent World Modeling

<!-- claim:SF-2026-ARXIV-2608-08600:start -->《Population-Scalable Multi-Agent World Modeling》把 `MULTIMODAL-WORLD-MODELS` 的问题具体化为：推理时 population 可变且各视图必须共享同一世界状态。其机制是将 shared-world-state evolution 与 population-agnostic view rendering 解耦；primary v1 的 evaluation 绑定为未见 agent population 的定性实验和 real-time interactive system，比较对象为fixed-population 或 dense cross-view interaction world model（摘要未命名）。<!-- claim:SF-2026-ARXIV-2608-08600:end -->

证据支持的范围是：展示设置中无需重训即可扩展视图数并保持定性一致性；不支持的外推是：任意 agent 数、复杂交互的定量正确性或稳定实时性。旧方案仍有成立条件：训练和推理固定 agent 数；规模固定时直接跨视图耦合更简单。新机制获得的收益与代价必须一起读取：近线性 per-view rendering 换 shared-state 容量与更新瓶颈。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：共享状态漏掉 agent-agent 作用、遮挡/冲突增长或 view query 压垮 renderer。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供环境状态转移的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MULTIMODAL-WORLD-MODELS`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08600:end -->

<!-- review:SF-2026-ARXIV-2608-08621:start -->
#### Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

<!-- claim:SF-2026-ARXIV-2608-08621:start -->《Business Arena: Benchmarking LLM Agents in a Realistic Marketplace》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：资本、合规与市场后果延迟耦合，单步分数难以解释能力。其机制是用真实 sourcing 数据校准长周期商店 simulator，并联合 profit、skill、action attribution 与 ablation；primary v1 的 evaluation 绑定为15 个 frontier models 经营跨境商店，比较对象为human-designed strategies 与 mechanism ablations。<!-- claim:SF-2026-ARXIV-2608-08621:end -->

证据支持的范围是：该环境中模型净值差异明显，最佳模型仍落后人工策略且可定位收益/损失动作；不支持的外推是：真实商业经营能力、跨市场泛化或单次动作的独立因果效应。旧方案仍有成立条件：短任务 benchmark 或只报 final score；对即时且独立任务仍够用。新机制获得的收益与代价必须一起读取：可控和可归因性换 simulator realism，profit 可测但不能单独解释能力。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：校准偏差、simulator shortcut、法规漂移或 human strategy 覆盖不足。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08621:end -->

<!-- review:SF-2026-ARXIV-2608-08744:start -->
#### Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs

<!-- claim:SF-2026-ARXIV-2608-08744:start -->《Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs》把 `PLATFORM-COST` 的问题具体化为：重复推理排放可能超过一次 fine-tuning，需把部署成本前移到目标函数。其机制是把硬件 profiling 拟合的 energy surrogate 加入 fine-tuning joint loss；primary v1 的 evaluation 绑定为Gemma-2-2B、Llama-3.1-8B、Qwen2.5-14B；三个 MMLU subjects，比较对象为ordinary fine-tuning / zero-carbon-term control。<!-- claim:SF-2026-ARXIV-2608-08744:end -->

证据支持的范围是：小范围存在 model/task-dependent break-even region，carbon term 可能正则化也可能干扰；不支持的外推是：通用零碳增益、生命周期减排或跨硬件 surrogate 有效。旧方案仍有成立条件：只优化准确率或训练后压缩；当推理量低时更直接。新机制获得的收益与代价必须一起读取：准确率与 surrogate energy 共同优化，交换为硬件校准和 proxy 偏差。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：换硬件/任务/模型后校准漂移，proxy 与真实 CO2 脱钩或 harmful interference。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 1 / System Reach 2 / Durability 2 = **5/9**。
- Score rationale：Design Delta：主要是版本或案例增量；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`PLATFORM-COST`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08744:end -->

<!-- review:SF-2026-ARXIV-2608-08800:start -->
#### Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages

<!-- claim:SF-2026-ARXIV-2608-08800:start -->《Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages》把 `TRAIN-PRETRAINING` 的问题具体化为：跨语言形态、tokenization 与模型规模改变迁移条件。其机制是在自然语言预训练前做 artificial-language pre-pretraining，并跨语言、Tokenizer、size、seed 复现；primary v1 的 evaluation 绑定为四个语言家族、两种 tokenizer、不同模型规模和随机种子，比较对象为direct pretraining 与先前的 headline token-efficiency 结果。<!-- claim:SF-2026-ARXIV-2608-08800:end -->

证据支持的范围是：收益高度依赖 setup/seed，仅小模型加 Llama tokenizer 的部分设置呈稳定趋势；不支持的外推是：pre-pretraining 普遍无效或能稳定复现固定比例的 token 节省。旧方案仍有成立条件：直接自然语言预训练；在迁移条件不确定时仍是稳健基线。新机制获得的收益与代价必须一起读取：潜在 token efficiency 换额外预训练成本和多 seed 验证。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：seed、tokenizer、morphology、model size 或 artificial-language choice 改变排名。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 3 / Durability 1 = **6/9**。
- Score rationale：Design Delta：提供训练目标与优化轨迹的一条受限机制/诊断分支；System Reach：会跨模型、runtime 与平台边界传播；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-PRETRAINING`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08800:end -->

<!-- review:SF-2026-ARXIV-2608-08802:start -->
#### Improving Generalization Robustness of Multimodal RLVR

<!-- claim:SF-2026-ARXIV-2608-08802:start -->《Improving Generalization Robustness of Multimodal RLVR》把 `TRAIN-GRPO` 的问题具体化为：等义改写和模板变化使训练收益在部署时脆弱。其机制是PIRL 以 format/content 分离的 trinary reward 加 embedding-space adversarial consistency regularizer；primary v1 的 evaluation 绑定为multimodal RLVR stress test 与 dynamic evaluation，覆盖 paraphrase/template shift，比较对象为standard GRPO。<!-- claim:SF-2026-ARXIV-2608-08802:end -->

证据支持的范围是：所测扰动下 accuracy drop 小于 GRPO；不支持的外推是：高风险医疗可靠性、所有等义扰动或 verifier 无偏。旧方案仍有成立条件：binary verifier 加窄 prompt distribution；固定模板时简单且便宜。新机制获得的收益与代价必须一起读取：robustness 换 adversarial regularization 训练成本及过约束风险。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：扰动实际改意、adversary 漏覆盖、format/content 标签错或新模态 shift。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供组内相对 credit的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-GRPO`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08802:end -->

<!-- review:SF-2026-ARXIV-2608-08822:start -->
#### Automated Generation of Complexity-Validated Decision Scenarios Using Large Language Models

<!-- claim:SF-2026-ARXIV-2608-08822:start -->《Automated Generation of Complexity-Validated Decision Scenarios Using Large Language Models》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：需要规模化、多域且 complexity 可控的评测素材。其机制是LLM 生成结构化决策场景，再以 task-complexity theory 的 composite psychometric validator 分层；primary v1 的 evaluation 绑定为4238 scenarios、多个 domain/tier 和 5 个 model families，比较对象为模型横向、known-groups tiers；无命名旧系统 baseline。<!-- claim:SF-2026-ARXIV-2608-08822:end -->

证据支持的范围是：该 instrument 在样本中能稳定区分三个 complexity tier；不支持的外推是：测得纯粹 complexity construct、下游认知表现或 throughput 因果关系。旧方案仍有成立条件：人工生产情景；规模小但可逐项审查。新机制获得的收益与代价必须一起读取：生成规模换 construct purity，速度与 schema pass 还可能冲突。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：text-length leakage、tier/domain imbalance 或单一高速模型驱动相关性。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可复算评估证据的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08822:end -->

<!-- review:SF-2026-ARXIV-2608-08829:start -->
#### Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models

<!-- claim:SF-2026-ARXIV-2608-08829:start -->《Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models》把 `MODEL-TRANSFORMER-LAYER` 的问题具体化为：最佳 steering 层随输入实例变化。其机制是prompt embedding 的 per-instance layer ranker 加方向 classifier 与短 steered pass gate；primary v1 的 evaluation 绑定为两个 open-weight 8B models、六个 binary persona traits，比较对象为unsteered、fixed layer sets 与 oracle selectors。<!-- claim:SF-2026-ARXIV-2608-08829:end -->

证据支持的范围是：所测 trait/model 上可回收大部分 oracle lift 并减少 fluency collapse；不支持的外推是：跨任务/尺度泛化、方向推断可靠或每个实例都不低于 baseline。旧方案仍有成立条件：每任务固定 injection layers；输入分布窄时易部署。新机制获得的收益与代价必须一起读取：适配性换 ranker/classifier/短 pass 开销以及层数与 fluency 的折中。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：方向误判、过多层注入、prompt OOD 或输入不可 steer。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-TRANSFORMER-LAYER`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08829:end -->

<!-- review:SF-2026-ARXIV-2608-08853:start -->
#### Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts

<!-- claim:SF-2026-ARXIV-2608-08853:start -->《Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts》把 `MODEL-MOE` 的问题具体化为：selected experts 内的路由排序与反事实 utility 相关性很低。其机制是保持 Top-k dispatch 不变，仅学习 selected-expert within-set aggregation head；primary v1 的 evaluation 绑定为OLMoE-1B-7B 多域 frozen evaluation 与 DeepSeek-V2-Lite replication，比较对象为router-score aggregation 与 oracle aggregators。<!-- claim:SF-2026-ARXIV-2608-08853:end -->

证据支持的范围是：两种架构中 router selection score 不等于最佳 commitment 权重，部分域可降低 CE；不支持的外推是：更优 expert selection、推理加速、所有域收益或普遍跨架构性。旧方案仍有成立条件：同一 router score 同时负责 dispatch 与 aggregation；开销最低。新机制获得的收益与代价必须一起读取：不省 expert compute，却增加 post-compute head、训练和部署路径。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：selected set 缺有用专家、off-domain neutral 或小收益被 head overhead 抵消。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供条件计算路由的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`MODEL-MOE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08853:end -->

<!-- review:SF-2026-ARXIV-2608-08878:start -->
#### DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2608-08878:start -->DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。<!-- claim:SF-2026-ARXIV-2608-08878:end -->

DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。 固定 attention/position heuristic 在分布稳定、预算温和时无需训练；压缩激进且未来 utility 依赖生成历史时，DistillCache 改为用逐步 KL 奖励学习 eviction policy。它用训练和 policy-transfer 风险换分布保持目标，实际并发 kernel 开销与跨模型迁移仍决定是否优于简单 heuristic。 该结论只在登记的模型、workload、硬件与 evaluation contract 内成立，不构成无条件替代。

- Evidence Level：primary paper v1；Review Route：`deep`。
- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Score rationale：Design Delta：改变了context-conditioned KV state的表示、控制点或验证路径；System Reach：会跨模型、runtime 与平台边界传播；Durability：结论以容量、带宽、精度与恢复为长期设计约束。
- Knowledge owner：`INFER-KV-CACHE`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08878:end -->

<!-- review:SF-2026-ARXIV-2608-08881:start -->
#### Theory-Guided Deception Detection: A RAG-Based Artificial Intelligence Exploration

<!-- claim:SF-2026-ARXIV-2608-08881:start -->《Theory-Guided Deception Detection: A RAG-Based Artificial Intelligence Exploration》把 `PLATFORM-EVALUATION-SYSTEM` 的问题具体化为：需要解释和控制 response bias，而不仅是整体 accuracy。其机制是按七种 deception theory 构造 RAG context，并与同模型无 RAG 条件比较 accuracy 与 bias；primary v1 的 evaluation 绑定为700 statements、5 datasets、4 LLMs，共 39200 judgments，比较对象为same-model baseline without theory-guided RAG。<!-- claim:SF-2026-ARXIV-2608-08881:end -->

证据支持的范围是：该设置中 RAG 不改善 accuracy，但理论选择显著改变 truth/lie response bias；不支持的外推是：可靠 deception detection、理论因果正确或跨内容/模型泛化。旧方案仍有成立条件：直接 LLM 判断；当检索理论本身不可靠时避免引入新偏差。新机制获得的收益与代价必须一起读取：理论 grounding 增加检索与偏置选择，却未带来 accuracy gain。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：theory-data mismatch、moderation、接近随机的基础准确率。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供可复算评估证据的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`PLATFORM-EVALUATION-SYSTEM`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08881:end -->

<!-- review:SF-2026-ARXIV-2608-08883:start -->
#### AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups

<!-- claim:SF-2026-ARXIV-2608-08883:start -->《AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups》把 `AGENT-MEMORY` 的问题具体化为：科研组需要本地隐私、透明复现和跨会话知识保留。其机制是本地 modular RAG 组合 embedding/reranking、多模态、semantic/episodic memory 与 skills；primary v1 的 evaluation 绑定为domain-expert discussions；摘要未披露定量 benchmark，比较对象为proprietary commercial AI 的概念对照；无 matched baseline。<!-- claim:SF-2026-ARXIV-2608-08883:end -->

证据支持的范围是：只证明 AquiLLM 的架构和 feature direction 已公开；不支持的外推是：捕获 tacit knowledge、提高科研质量/复现性或满足 privacy。旧方案仍有成立条件：云端助手或无持久记忆的基础 RAG；运维简单。新机制获得的收益与代价必须一起读取：本地控制换模型/运维负担，多类 memory 增加一致性治理。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：过期/错误 memory、检索失败、权限泄漏或讨论不能代表用户评测。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Score rationale：Design Delta：提供持久及派生记忆的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：机制可复用，但证据仍依赖当前 workload。
- Knowledge owner：`AGENT-MEMORY`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08883:end -->

<!-- review:SF-2026-ARXIV-2608-08889:start -->
#### LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing

<!-- claim:SF-2026-ARXIV-2608-08889:start -->《LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing》把 `TRAIN-RLHF` 的问题具体化为：主观 correctness 是 context-aware preference 而非二元真值。其机制是用 conditional length penalty 抑制 reasoning collapse，并按 socio-linguistic persona 路由 reasoning style；primary v1 的 evaluation 绑定为生产 recommender 的四个主观 verification tasks、多种模型和 1500 personas，比较对象为standard RLVR 与 rigid math-centric reasoning traces。<!-- claim:SF-2026-ARXIV-2608-08889:end -->

证据支持的范围是：所测主观 rubric 中刚性长推理会降质，长度约束可恢复且 persona framing 影响 macro-F1；不支持的外推是：所有主观任务、真实用户偏好或 persona routing 因果稳健性。旧方案仍有成立条件：把客观题 RLVR 与统一 reasoning style 迁移到主观审核；规则简单但分布错配。新机制获得的收益与代价必须一起读取：压短链可防 collapse 也会截断必要推理，persona router 增加治理成本。基于上述 mechanism、evaluation 与 comparator 的 Agent 推断，适用或失效边界包括：persona mismatch、rubric drift、reward ambiguity 或 length penalty 诱发猜测。这部分推断不是作者实验直接证明的 failure-rate 结论。因而该 family 保留为来源特定的标准证据实例，不因作者相对结果自动升级为默认架构或 Books 结论。

- Evidence Level：primary paper v1；Review Route：`standard`。
- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Score rationale：Design Delta：提供系统状态的一条受限机制/诊断分支；System Reach：影响集中在该 owner 或受限 workload；Durability：高度依赖当前模型/版本。
- Knowledge owner：`TRAIN-RLHF`；Disposition：`Weekly Only — Context`。
<!-- review:SF-2026-ARXIV-2608-08889:end -->

## 4. Benchmark Contracts

Deep Review 会核对作者 evaluation，但本日报不抽离复述性能数字。为避免用 `Benchmark Claim = no` 规避条件账本，所有使用作者实验范围支撑证据边界的 Deep family 均登记完整字段；只有 source v1 未披露的字段才能写带原因的 `Not Disclosed`。若只是本报告尚未提取或复算，该 family 必须保持 review incomplete 且 Evidence Gate Open。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08569 | Vox-Infinity, AudioMarathon and SPIRAL long-audio reasoning plus MMSU, MMAU and MMAR general audio-language evaluation; Personal-Monologue averages over 20 minutes | Qwen3-Omni-30B-Instruct and Qwen3-Omni-30B-Thinking with Whisper-Turbo ASR | single node with 8× NVIDIA A100 80GB | model precision Not Disclosed; KV compression ratio is not numeric precision | 64K-token context in the efficiency protocol; suite-dependent audio duration elsewhere | 300 output tokens in the 64K efficiency protocol; suite-dependent QA output elsewhere | Not Disclosed — v1 does not state a normalized batch for the 64K efficiency row | Not Disclosed — v1 does not state serving concurrency | no production SLO; suite quality, prefill latency, peak memory and tokens/s at 25% cache budget | suite-specific official scorers plus full-cache and compression baselines; Table 6 efficiency protocol |
| SF-2026-ARXIV-2608-08878 | LongBench, GSM8K and BBH at 12.5%–100% KV budgets | Mistral-7B-Instruct-v0.3 training/evaluation; Llama-3-8B-Instruct zero-shot cross-model transfer | 2× NVIDIA RTX 4090 with tensor parallelism | FP16 forward passes; cache budget is not numeric precision | task-dependent prompts with training max sequence length 4096 | greedy decoding with maximum 512 new tokens | training samples one prompt per step; inference batch Not Disclosed | single decoding trajectory; normalized serving concurrency Not Disclosed | no production SLO; exact match/ROUGE-L, KL-to-full-cache, throughput and latency | official LongBench/GSM8K/BBH scripts; full cache, H2O, SnapKV and best-effort ForesightKV/RLKV reimplementations |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08878 | score_7_9<br>potential_books_delta | selected | DA-20260810-2608-08878 | — | 逐 family 排序：override=none，V2=9/9 (3/3/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=KV compression budget becomes token, head and layer sensitive instead of uniform | analysis:DA-20260810-2608-08878 |
| SF-2026-ARXIV-2608-08569 | score_7_9<br>potential_books_delta | selected | DA-20260810-2608-08569 | — | 逐 family 排序：override=none，V2=8/9 (3/2/3)；保留独立机制、证据边界与 Books Decision；pre-Books delta=transcript changes from modality replacement to a provenance-bearing semantic anchor | analysis:DA-20260810-2608-08569 |

<!-- analysis:DA-20260810-2608-08878:start -->
### DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference

DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。 固定 attention/position heuristic 在分布稳定、预算温和时无需训练；压缩激进且未来 utility 依赖生成历史时，DistillCache 改为用逐步 KL 奖励学习 eviction policy。它用训练和 policy-transfer 风险换分布保持目标，实际并发 kernel 开销与跨模型迁移仍决定是否优于简单 heuristic。

<!-- analysis:DA-20260810-2608-08878:end -->

<!-- analysis:DA-20260810-2608-08569:start -->
### VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference

VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。 文本 KV eviction 假设 token 的语义密度和时间结构近似文本；语音 token 冗余、连续且含副语言信息后，这个假设失效。VoxZip 先用 ASR anchor 压缩时间轴，再按衰减注意力淘汰，以 ASR 依赖和在线漂移风险换更小 KV；因此它是 speech-specific branch，而不是统一替代文本压缩。

<!-- analysis:DA-20260810-2608-08569:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2608-08569 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L14<br>books/part-03-multimodal-world-models/23-multimodal-representation.md#L237 | books/part-02-model/17-transformer-layer.md#L14<br>books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14 | existing:SF-2026-ARXIV-2608-08569 | delta:SF-2026-ARXIV-2608-08569 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2608-08569 |
| SF-2026-ARXIV-2608-08878 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14<br>books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L385 | books/part-02-model/19-kv-cache.md#L14<br>books/part-05-inference-system/54-gpu-memory.md#L14 | existing:SF-2026-ARXIV-2608-08878 | delta:SF-2026-ARXIV-2608-08878 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2608-08878 |

<!-- books-review:SF-2026-ARXIV-2608-08569:start --><!-- existing:SF-2026-ARXIV-2608-08569:start -->现有中心命题：多模态系统的第一问题不是把所有输入变成同一 shape，而是建立可版本化的 representation contract：每个表示必须保留它来自哪种 modality、对应什么时间与空间范围、经过哪个 encoder/codec、属于哪个 artifact version，并明确哪些信息已经不可逆地丢失。<!-- existing:SF-2026-ARXIV-2608-08569:end --><!-- delta:SF-2026-ARXIV-2608-08569:start -->VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。<!-- delta:SF-2026-ARXIV-2608-08569:end -->与上述中心命题相比，这个 family 的新增证据是：VoxZip 先用 ASR transcript 作为 semantic anchor 对齐并融合 audio tokens，再以时间衰减 accumulated attention 做动态淘汰。Qwen3-Omni 六个 audio benchmark 支持作者范围内的压缩结论；ASR 错误、跨语言语音和实时 streaming 的累积偏差仍是 failure boundary。 该 delta 已落在《第23章 多模态表示与融合》的正文机制锚点；语义相邻边界为 MODEL-TRANSFORMER-LAYER：Transformer Layer 是一个保持 residual stream shape 不变、并显式管理跨层信息与梯度路径的可堆叠状态更新单元。；MULTIMODAL-GENERATIVE-PARADIGMS：生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-08569:end -->

<!-- books-review:SF-2026-ARXIV-2608-08878:start --><!-- existing:SF-2026-ARXIV-2608-08878:start -->现有中心命题：KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。<!-- existing:SF-2026-ARXIV-2608-08878:end --><!-- delta:SF-2026-ARXIV-2608-08878:start -->DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。<!-- delta:SF-2026-ARXIV-2608-08878:end -->与上述中心命题相比，这个 family 的新增证据是：DistillCache 把 KV eviction 建模为序贯决策，用 attention、value norm、entropy 和 position 训练轻量 policy，并以相对 full-cache logits 的逐步 KL 作为 reward。证据来自单个 Mistral-7B checkpoint 与作者重实现的 baselines；policy transfer、训练成本和实际并发 kernel 开销未被统一证明。 该 delta 已落在《第45章 为什么 KV Cache 能提速》的正文机制锚点；语义相邻边界为 MODEL-KV-CACHE：KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。；INFER-GPU-MEMORY：GPU inference capacity 不是“权重能否装入”的二元问题，而是 weights、resident KV、workspace、communication、fragmentation 和 safety reserve 对同一 HBM budget 的动态竞争。。相邻章节不接管该机制，正文也不继承作者 benchmark headline，只保留适用条件、代价和未证明边界。<!-- books-review:SF-2026-ARXIV-2608-08878:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260810-COVERAGE | fresh-context:final-contract-review | coverage | coverage:SRC-ARXIV:20260810; coverage:SRC-GITHUB-COMMIT:20260810; semantic-review:SA-20260810-COVERAGE | none | Verified — archived arXiv daily hits, Effective Date applicability, denominator and receipt match | passed |
| SA-20260810-EVIDENCE | fresh-context:final-contract-review | evidence | validator:review-completion-v1; review:SF-2026-ARXIV-2608-08413; review:SF-2026-ARXIV-2608-08569; review:SF-2026-ARXIV-2608-08600; review:SF-2026-ARXIV-2608-08621; review:SF-2026-ARXIV-2608-08744; review:SF-2026-ARXIV-2608-08800; review:SF-2026-ARXIV-2608-08802; review:SF-2026-ARXIV-2608-08822; review:SF-2026-ARXIV-2608-08829; review:SF-2026-ARXIV-2608-08853; review:SF-2026-ARXIV-2608-08878; review:SF-2026-ARXIV-2608-08881; review:SF-2026-ARXIV-2608-08883; review:SF-2026-ARXIV-2608-08889; semantic-review:SA-20260810-EVIDENCE | none | fresh-context reviewer 已核验版本身份、route-matched locator、claim boundary、benchmark contract 与 Evidence 状态 | passed |
| SA-20260810-SELECTION | fresh-context:final-contract-review | deep_analysis_selection | analysis:DA-20260810-2608-08569; analysis:DA-20260810-2608-08878; semantic-review:SA-20260810-SELECTION | none | Verified — evidence-stage potential delta, narrative selection and at-most-three selected units | passed |
| SA-20260810-BOOKS | fresh-context:final-contract-review | books | validator:books-comparison-v1; books-review:SF-2026-ARXIV-2608-08569; books-review:SF-2026-ARXIV-2608-08878; review:SF-2026-ARXIV-2608-08413; review:SF-2026-ARXIV-2608-08600; review:SF-2026-ARXIV-2608-08621; review:SF-2026-ARXIV-2608-08744; review:SF-2026-ARXIV-2608-08800; review:SF-2026-ARXIV-2608-08802; review:SF-2026-ARXIV-2608-08822; review:SF-2026-ARXIV-2608-08829; review:SF-2026-ARXIV-2608-08853; review:SF-2026-ARXIV-2608-08881; review:SF-2026-ARXIV-2608-08883; review:SF-2026-ARXIV-2608-08889; semantic-review:SA-20260810-BOOKS | none | Verified — durable body anchors, semantic adjacency, evolution relation and every Weekly Only review ref | passed |

<!-- semantic-review:SA-20260810-COVERAGE:start -->Fresh-context reviewer verified Effective Date applicability, archived arXiv daily hits and frozen denominator closure.<!-- semantic-review:SA-20260810-COVERAGE:end -->
<!-- semantic-review:SA-20260810-EVIDENCE:start -->Fresh-context review passed the frozen Candidate and Review receipt set after locator, claim-boundary and benchmark-contract corrections.<!-- semantic-review:SA-20260810-EVIDENCE:end -->
<!-- semantic-review:SA-20260810-SELECTION:start -->Fresh-context reviewer verified evidence-stage eligibility and every selected or not-selected narrative decision without Books feedback.<!-- semantic-review:SA-20260810-SELECTION:end -->
<!-- semantic-review:SA-20260810-BOOKS:start -->Fresh-context reviewer verified all Integrate body anchors, semantic adjacent-owner boundaries, evolution relations and Weekly Only dispositions.<!-- semantic-review:SA-20260810-BOOKS:end -->

## 8. Ignored Noise

288 条 arXiv v1 中有 274 条未进入候选分母。拒绝理由限定为：垂直应用不改变 AI-System contract；单数据集增量无机制差异；纯 quality headline 缺少状态/控制权变化；cross-listing 重复；或只有 LLM/Agent 关键词而没有系统贡献。它们完成 topic-level closure，不以大量低分行稀释候选账本。

## 9. Recommended Action

1. Sunday Weekly 按 Source Family 聚合本日报 Review Provenance；不得按后续发现日重复计分。
2. 只有重要 revision、artifact 或反证改变 identity、Method 或 claim boundary 时才重开本日报 family。
3. Books Decision：2 个 `Integrate`、0 个 `No Change — Existing Coverage`、12 个 `Weekly Only — Context`；每个 Integrate/No Change 均有 owner、相邻章节和 bounded Books Review receipt。

## 10. Repository Changes

- 重建 `papers/2026/08/10/README.md` 的 Coverage applicability 与 Books receipts。
- Refine `books/part-03-multimodal-world-models/23-multimodal-representation.md`，只吸收长期机制、取舍与失效边界。
- Refine `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`，只吸收长期机制、取舍与失效边界。

## 11. Open Questions

- 日期精度仅到天的官方页面能否补回原始 HTTP/发布系统 timestamp，以消除 09:00 边界不确定性？
- Sunday Weekly 是否出现 artifact、independent reproduction 或反证，要求升级/降级 Evidence Level？

## 12. Sources

- [Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications](https://arxiv.org/abs/2608.08413v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](https://arxiv.org/abs/2608.08569v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [Population-Scalable Multi-Agent World Modeling](https://arxiv.org/abs/2608.08600v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](https://arxiv.org/abs/2608.08621v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs](https://arxiv.org/abs/2608.08744v1) — published/event date: 2026-08-09; accessed: 2026-08-25
- [Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages](https://arxiv.org/abs/2608.08800v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Improving Generalization Robustness of Multimodal RLVR](https://arxiv.org/abs/2608.08802v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Automated Generation of Complexity-Validated Decision Scenarios Using Large Language Models](https://arxiv.org/abs/2608.08822v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](https://arxiv.org/abs/2608.08829v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.08853v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [DistillCache: KL-Guided Adaptive KV-Cache Eviction for Memory-Efficient LLM Inference](https://arxiv.org/abs/2608.08878v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [Theory-Guided Deception Detection: A RAG-Based Artificial Intelligence Exploration](https://arxiv.org/abs/2608.08881v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [AquiLLM: An Architecture for Supporting Tacit Knowledge Capture in Research Groups](https://arxiv.org/abs/2608.08883v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [LLM Reasoning for Subjective Tasks: Failure Modes, Mitigation, and Dynamic Reasoning Routing](https://arxiv.org/abs/2608.08889v1) — published/event date: 2026-08-10; accessed: 2026-08-25
- [arXiv API](https://export.arxiv.org/api/help/) — exact submittedDate snapshots; accessed: 2026-08-25
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 frozen denominator、Evidence Review、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，Coverage、Evidence 与 Books Gates 已闭合。
