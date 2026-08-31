# Daily Research — 2025-05-04

**Research Date:** 2025-05-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2025-05-03 09:00:00 ～ 2025-05-04 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；fresh-context unresolved findings=0

## Executive Summary

本轮使用官方 arXiv Atom API 快照枚举严格窗口，得到 335 条原始记录；日期和注册分类过滤后，150 条进入 title+abstract 全语义筛选。独立 fresh-context audit 逐项复核 retained false positive 与 closure false negative，修复 6 个漏项后冻结 14 个候选，其余 136 条保留逐 family pre-denominator closure。

14 个候选均完成 exact-v1 Method、Evaluation、Limitations/Counterevidence 与 artifact Review，并完成 Score V2、Deep Analysis selection 和 owner/相邻章节对照。新增漏项揭示 preference annotation noise、systems reproducibility、LLM-evaluator length bias、online conformal monitoring、federated trust boundary 与 evidence-system adversarial attack；当前 Books 已由后续更完整证据承载这些长期命题，因此本日没有共享 Books 写入。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2025-05-04 |
| Window End | 2025-05-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20250504-97f7318739feea6c57f2 |
| Denominator Frozen At | 2026-08-31T18:20:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2025-05-03T09:00:00+08:00 | 2025-05-04T09:00:00+08:00 | 2026-08-31T18:20:00+08:00 | official Atom API; submittedDate UTC window; registered category route | checked | 150 | SF-2025-HPC-REPRODUCIBILITY<br>SF-2025-ROBUST-2D-DPO<br>SF-2025-ROBRIDGE<br>SF-2025-POSEPILOT<br>SF-2025-VLORP<br>SF-2025-LENGTH-BIASED-LLM-EVAL<br>SF-2025-CONTEXT-CONFORMAL-ANOMALY<br>SF-2025-BADPATCHES<br>SF-2025-NEW-NEWS-SYS2FT<br>SF-2025-INTRA-LAYER-RECURRENCE<br>SF-2025-CAFCOR<br>SF-2025-DITOX<br>SF-2025-CAMOUFLAGE<br>SF-2025-SPECULATIVE-SEARCH | pages=1; start=0; final_cursor=end | 2025-05-04T09:00:00+08:00 | coverage:SRC-ARXIV:20250504 | — |

<!-- coverage:SRC-ARXIV:20250504:start -->官方 Atom 快照包含 335 条原始 entry；脚本按 v1 timestamp 与注册分类冻结 150 条身份、14 个 retained candidates 和 136 个逐 family closure。独立 reviewer 逐项审阅 150/150，修复 6 个 false negatives、确认 retained false positives=0。快照、SHA-256、完整 title+abstract ledger 与 exact-v1 evidence locators 均保存在本日 `_sources` packet。<!-- coverage:SRC-ARXIV:20250504:end -->

### Coverage Limitations

- 以本窗口 `Window End` 计算，来源注册表中只有 `SRC-ARXIV` 的 Effective Date 已到期；2026-08-25 后加入的组织来源与 Hugging Face backstop 不反推为 2025 Daily 的 Required receipt。
- 150 条是完成全语义筛选的 registered identities，不是 150 篇全文 Review。只有冻结分母中的 14 个 family 进入精确全文审计与评分。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HPC-REPRODUCIBILITY | arXiv:2505.01671v1 | paper-v1:2505.01671 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-HPC-REPRODUCIBILITY | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-HPC-REPRODUCIBILITY | yes |
| SF-2025-ROBUST-2D-DPO | arXiv:2505.01706v1 | paper-v1:2505.01706 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-ROBUST-2D-DPO | self | — | new_in_window | TRAIN-DPO | No Change — Existing Coverage | books-review:SF-2025-ROBUST-2D-DPO | yes |
| SF-2025-ROBRIDGE | arXiv:2505.01709v1 | paper-v1:2505.01709 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2025-ROBRIDGE | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2025-ROBRIDGE | yes |
| SF-2025-POSEPILOT | arXiv:2505.01729v1 | paper-v1:2505.01729 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-POSEPILOT | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2025-POSEPILOT | yes |
| SF-2025-VLORP | arXiv:2505.01744v1 | paper-v1:2505.01744 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-VLORP | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2025-VLORP | yes |
| SF-2025-LENGTH-BIASED-LLM-EVAL | arXiv:2505.01761v1 | paper-v1:2505.01761 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2025-LENGTH-BIASED-LLM-EVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-LENGTH-BIASED-LLM-EVAL | yes |
| SF-2025-CONTEXT-CONFORMAL-ANOMALY | arXiv:2505.01783v1 | paper-v1:2505.01783 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2025-CONTEXT-CONFORMAL-ANOMALY | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY | yes |
| SF-2025-BADPATCHES | arXiv:2505.01811v1 | paper-v1:2505.01811 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-BADPATCHES | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-BADPATCHES | yes |
| SF-2025-NEW-NEWS-SYS2FT | arXiv:2505.01812v1 | paper-v1:2505.01812 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2025-NEW-NEWS-SYS2FT | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2025-NEW-NEWS-SYS2FT | yes |
| SF-2025-INTRA-LAYER-RECURRENCE | arXiv:2505.01855v1 | paper-v1:2505.01855 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-INTRA-LAYER-RECURRENCE | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | No Change — Existing Coverage | books-review:SF-2025-INTRA-LAYER-RECURRENCE | yes |
| SF-2025-CAFCOR | arXiv:2505.01874v1 | paper-v1:2505.01874 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-CAFCOR | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-CAFCOR | yes |
| SF-2025-DITOX | arXiv:2505.01892v1 | paper-v1:2505.01892 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-DITOX | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-DITOX | yes |
| SF-2025-CAMOUFLAGE | arXiv:2505.01900v1 | paper-v1:2505.01900 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-CAMOUFLAGE | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-CAMOUFLAGE | yes |
| SF-2025-SPECULATIVE-SEARCH | arXiv:2505.02865v1 | paper-v1:2505.02865 | 2025-W18 | 2025-05-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-SPECULATIVE-SEARCH | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2025-SPECULATIVE-SEARCH | yes |

14/14 候选均为本窗口首次公开的 owner candidate；评分不用于替代 Evidence Level、Review Status、Access Status 或 Books disposition。

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HPC-REPRODUCIBILITY | RP-97f0aa14275b48e2 | deep | arXiv:2505.01671v1 | SRC-ARXIV@arXiv:2505.01671v1 | https://arxiv.org/html/2505.01671v1#S4; https://arxiv.org/html/2505.01671v1#S4.SS1; https://arxiv.org/html/2505.01671v1#S4.SS2 | https://arxiv.org/html/2505.01671v1#S5; https://arxiv.org/html/2505.01671v1#S7.SS3; https://arxiv.org/html/2505.01671v1#S7.SS4 | https://arxiv.org/html/2505.01671v1#S4; https://arxiv.org/html/2505.01671v1#S5 | https://doi.org/10.5281/zenodo.15306610 | claim:SF-2025-HPC-REPRODUCIBILITY | complete |
| SF-2025-ROBUST-2D-DPO | RP-7144e4ceee0ee080 | standard | arXiv:2505.01706v1 | SRC-ARXIV@arXiv:2505.01706v1 | https://arxiv.org/html/2505.01706v1#S3; https://arxiv.org/html/2505.01706v1#S4; https://arxiv.org/html/2505.01706v1#S4.SS2; https://arxiv.org/html/2505.01706v1#S4.SS3 | https://arxiv.org/html/2505.01706v1#S5; https://arxiv.org/html/2505.01706v1#A4; https://arxiv.org/html/2505.01706v1#A5 | https://arxiv.org/html/2505.01706v1#S6 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-ROBUST-2D-DPO | complete |
| SF-2025-ROBRIDGE | RP-9a56d2d1a75ce58d | deep | arXiv:2505.01709v1 | SRC-ARXIV@arXiv:2505.01709v1 | https://arxiv.org/html/2505.01709v1#S3; https://arxiv.org/html/2505.01709v1#S3.SS1; https://arxiv.org/html/2505.01709v1#S3.SS2 | https://arxiv.org/html/2505.01709v1#S4; https://arxiv.org/html/2505.01709v1#S4.SS3; https://arxiv.org/html/2505.01709v1#S4.SS5 | https://arxiv.org/html/2505.01709v1#S4.SS6; https://arxiv.org/html/2505.01709v1#A1 | https://abliao.github.io/RoBridge/ | claim:SF-2025-ROBRIDGE | complete |
| SF-2025-POSEPILOT | RP-85bc9f93d919cc73 | standard | arXiv:2505.01729v1 | SRC-ARXIV@arXiv:2505.01729v1 | https://arxiv.org/html/2505.01729v1#S3; https://arxiv.org/html/2505.01729v1#S3.SS1; https://arxiv.org/html/2505.01729v1#S3.SS2; https://arxiv.org/html/2505.01729v1#S3.SS3 | https://arxiv.org/html/2505.01729v1#S4; https://arxiv.org/html/2505.01729v1#S4.SS2; https://arxiv.org/html/2505.01729v1#S4.SS3 | https://arxiv.org/html/2505.01729v1#S5 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-POSEPILOT | complete |
| SF-2025-VLORP | RP-2cf27bfac9fa61d3 | deep | arXiv:2505.01744v1 | SRC-ARXIV@arXiv:2505.01744v1 | https://arxiv.org/html/2505.01744v1#S3; https://arxiv.org/html/2505.01744v1#S4; https://arxiv.org/html/2505.01744v1#A2; https://arxiv.org/html/2505.01744v1#A3 | https://arxiv.org/html/2505.01744v1#S5; https://arxiv.org/html/2505.01744v1#A4.SS2; https://arxiv.org/html/2505.01744v1#A4.SS7; https://arxiv.org/html/2505.01744v1#A4.SS8 | https://arxiv.org/html/2505.01744v1#S6 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-VLORP | complete |
| SF-2025-LENGTH-BIASED-LLM-EVAL | RP-4a06847bd13b69c2 | deep | arXiv:2505.01761v1 | SRC-ARXIV@arXiv:2505.01761v1 | https://arxiv.org/html/2505.01761v1#S2; https://arxiv.org/html/2505.01761v1#S3 | https://arxiv.org/html/2505.01761v1#S4; https://arxiv.org/html/2505.01761v1#S5; https://arxiv.org/html/2505.01761v1#S6 | https://arxiv.org/html/2505.01761v1#S7 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-LENGTH-BIASED-LLM-EVAL | complete |
| SF-2025-CONTEXT-CONFORMAL-ANOMALY | RP-3c00d5afc92ca77a | deep | arXiv:2505.01783v1 | SRC-ARXIV@arXiv:2505.01783v1 | https://arxiv.org/html/2505.01783v1#S2; https://arxiv.org/html/2505.01783v1#S3; https://arxiv.org/html/2505.01783v1#S3.SS3; https://arxiv.org/html/2505.01783v1#S3.SS4 | https://arxiv.org/html/2505.01783v1#S5; https://arxiv.org/html/2505.01783v1#S5.SS2; https://arxiv.org/html/2505.01783v1#S5.SS3 | https://arxiv.org/html/2505.01783v1#S6 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-CONTEXT-CONFORMAL-ANOMALY | complete |
| SF-2025-BADPATCHES | RP-e3b54cea71cbcfb2 | standard | arXiv:2505.01811v1 | SRC-ARXIV@arXiv:2505.01811v1 | https://arxiv.org/html/2505.01811v1#S3; https://arxiv.org/html/2505.01811v1#S3.SS1; https://arxiv.org/html/2505.01811v1#S3.SS2; https://arxiv.org/html/2505.01811v1#S3.SS3 | https://arxiv.org/html/2505.01811v1#S4; https://arxiv.org/html/2505.01811v1#S5; https://arxiv.org/html/2505.01811v1#S5.SS3 | https://arxiv.org/html/2505.01811v1#S6 | https://github.com/geefmegeld/pMoE-backdoor | claim:SF-2025-BADPATCHES | complete |
| SF-2025-NEW-NEWS-SYS2FT | RP-4e38f63819bed607 | deep | arXiv:2505.01812v1 | SRC-ARXIV@arXiv:2505.01812v1 | https://arxiv.org/html/2505.01812v1#S3; https://arxiv.org/html/2505.01812v1#S4; https://arxiv.org/html/2505.01812v1#S4.SS1 | https://arxiv.org/html/2505.01812v1#S4.SS2; https://arxiv.org/html/2505.01812v1#S5; https://arxiv.org/html/2505.01812v1#S6; https://arxiv.org/html/2505.01812v1#S7; https://arxiv.org/html/2505.01812v1#S8 | https://arxiv.org/html/2505.01812v1#S9; https://arxiv.org/html/2505.01812v1#A5 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-NEW-NEWS-SYS2FT | complete |
| SF-2025-INTRA-LAYER-RECURRENCE | RP-0427bb3f8fc67c40 | standard | arXiv:2505.01855v1 | SRC-ARXIV@arXiv:2505.01855v1 | https://arxiv.org/html/2505.01855v1#S3 | https://arxiv.org/html/2505.01855v1#S4; https://arxiv.org/html/2505.01855v1#A1 | https://arxiv.org/html/2505.01855v1#S5 | https://github.com/ant-8/Layer-Recurrent-Transformers | claim:SF-2025-INTRA-LAYER-RECURRENCE | complete |
| SF-2025-CAFCOR | RP-f563dcadba3c1a53 | deep | arXiv:2505.01874v1 | SRC-ARXIV@arXiv:2505.01874v1 | https://arxiv.org/html/2505.01874v1#S2; https://arxiv.org/html/2505.01874v1#S3; https://arxiv.org/html/2505.01874v1#S4 | https://arxiv.org/html/2505.01874v1#S5; https://arxiv.org/html/2505.01874v1#A4 | https://arxiv.org/html/2505.01874v1#S2.SS3; https://arxiv.org/html/2505.01874v1#S6 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-CAFCOR | complete |
| SF-2025-DITOX | RP-89ac29a26dce3d83 | deep | arXiv:2505.01892v1 | SRC-ARXIV@arXiv:2505.01892v1 | https://arxiv.org/html/2505.01892v1#S3; https://arxiv.org/html/2505.01892v1#S3.SS1; https://arxiv.org/html/2505.01892v1#S3.SS4 | https://arxiv.org/html/2505.01892v1#S5; https://arxiv.org/html/2505.01892v1#S6; https://arxiv.org/html/2505.01892v1#S6.SS2 | https://arxiv.org/html/2505.01892v1#S8 | Not Disclosed — exact DiTOX artifact is not disclosed in v1 | claim:SF-2025-DITOX | complete |
| SF-2025-CAMOUFLAGE | RP-4e67ecb5ff012468 | deep | arXiv:2505.01900v1 | SRC-ARXIV@arXiv:2505.01900v1 | https://arxiv.org/html/2505.01900v1#S3; https://arxiv.org/html/2505.01900v1#S4; https://arxiv.org/html/2505.01900v1#S4.SS1; https://arxiv.org/html/2505.01900v1#S4.SS3 | https://arxiv.org/html/2505.01900v1#S5; https://arxiv.org/html/2505.01900v1#S5.SS4; https://arxiv.org/html/2505.01900v1#S5.SS5; https://arxiv.org/html/2505.01900v1#S5.SS6 | https://arxiv.org/html/2505.01900v1#S6; https://arxiv.org/html/2505.01900v1#S7; https://arxiv.org/html/2505.01900v1#A3 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-CAMOUFLAGE | complete |
| SF-2025-SPECULATIVE-SEARCH | RP-4cb59e8b418f2b23 | deep | arXiv:2505.02865v1 | SRC-ARXIV@arXiv:2505.02865v1 | https://arxiv.org/html/2505.02865v1#S4; https://arxiv.org/html/2505.02865v1#S4.SS1; https://arxiv.org/html/2505.02865v1#S4.SS3; https://arxiv.org/html/2505.02865v1#A1 | https://arxiv.org/html/2505.02865v1#S5; https://arxiv.org/html/2505.02865v1#A7; https://arxiv.org/html/2505.02865v1#A8 | https://arxiv.org/html/2505.02865v1#S6; https://arxiv.org/html/2505.02865v1#A6 | Not Disclosed — no frozen event-time artifact | claim:SF-2025-SPECULATIVE-SEARCH | complete |

### Source Reviews

<!-- review:SF-2025-HPC-REPRODUCIBILITY:start --><!-- claim:SF-2025-HPC-REPRODUCIBILITY:start -->把系统实验的可复现性从‘代码可运行’提升为受 hardware、firmware、environment、artifact identity、acceptance condition 与 reviewer cost 共同约束的 release evidence contract。<!-- claim:SF-2025-HPC-REPRODUCIBILITY:end -->

这是 2024 社区 workshop 的综合报告与 checklist，不是受控实验；它支持 evidence contract 与成本边界，不证明某种打包工具或 badge 能普遍获得可复现结果。<!-- review:SF-2025-HPC-REPRODUCIBILITY:end -->

<!-- review:SF-2025-ROBUST-2D-DPO:start --><!-- claim:SF-2025-ROBUST-2D-DPO:start -->把 preference supervision 从整条 response 的无噪声 pairwise label 扩展为 segment/aspect score，并显式把 annotation noise 写入 loss；annotation contract 因而成为 DPO objective 的一部分。<!-- claim:SF-2025-ROBUST-2D-DPO:end -->

理论与实验只覆盖文中 label-flip 和 segment-score perturbation；没有证明真实人类偏好噪声、其他 segmentation、reward model 或大规模 post-training 下同样稳健。<!-- review:SF-2025-ROBUST-2D-DPO:end -->

<!-- review:SF-2025-ROBRIDGE:start --><!-- claim:SF-2025-ROBRIDGE:start -->把开放指令拆成 VLM cognitive plan、可操作中间表示与 RL controller；中间表示成为 cognition 与 execution 的显式 handoff，而不是让语言模型直接拥有低层动作时序。<!-- claim:SF-2025-ROBRIDGE:end -->

75% 新任务与 83% sim-to-real 是作者在 MetaWorld、RoboSuite 和 Kinova Gen3 小样本设置中的结果；它不证明任意机器人、传感器、控制频率或安全约束下同样成立。<!-- review:SF-2025-ROBRIDGE:end -->

<!-- review:SF-2025-POSEPILOT:start --><!-- claim:SF-2025-POSEPILOT:start -->用 self-supervised depth、relative pose 与双向 photometric warping 把 camera control 注入生成式 world model，使 viewpoint transition 获得显式几何约束。<!-- claim:SF-2025-POSEPILOT:end -->

nuScenes、Vista/DrivingWorld 与一般视频实验只证明 camera-pose controllability 和生成指标；没有证明环境 transition 的因果正确性、policy utility 或闭环驾驶安全。<!-- review:SF-2025-POSEPILOT:end -->

<!-- review:SF-2025-VLORP:start --><!-- claim:SF-2025-VLORP:start -->把 low-rank gradient projection 的 projection granularity 提升为独立于 rank 的设计旋钮，并由 ProjFactor 持有投影基与 optimizer state，在固定显存预算下交换估计偏差、稳定性和状态成本。<!-- claim:SF-2025-VLORP:end -->

理论结论依赖文中假设，实验集中在 LLaMA2-7B 与给定 fine-tuning workload；未证明 full pretraining、其他 optimizer、并行拓扑或更长序列下仍保持相同收敛与吞吐优势。<!-- review:SF-2025-VLORP:end -->

<!-- review:SF-2025-LENGTH-BIASED-LLM-EVAL:start --><!-- claim:SF-2025-LENGTH-BIASED-LLM-EVAL:start -->证明 evaluator 的 input granularity 不是展示细节：同一文档按 segment、document 或 multi-document 输入会改变 error recall 与 system ranking，因此 length、chunking 和 focus policy 必须进入 evaluation contract。<!-- claim:SF-2025-LENGTH-BIASED-LLM-EVAL:end -->

结果来自 MT/MQM、Claude 3.5 与 GPT-4o 等披露设置；不能外推为所有 LLM judge 或所有长上下文任务的统一偏差，也未证明 fine-tuning 能跨版本保持校准。<!-- review:SF-2025-LENGTH-BIASED-LLM-EVAL:end -->

<!-- review:SF-2025-CONTEXT-CONFORMAL-ANOMALY:start --><!-- claim:SF-2025-CONTEXT-CONFORMAL-ANOMALY:start -->把在线 anomaly alert 从固定 threshold 提升为带 context、calibration ownership、real-data acquisition decision 与 time-averaged FDR guarantee 的 evidence loop。<!-- claim:SF-2025-CONTEXT-CONFORMAL-ANOMALY:end -->

理论保证针对文中 conformal/online-testing assumptions；实验只覆盖披露的 synthetic、thyroid 与 O-RAN 设置，不能证明任意 telemetry drift、dependent stream 或生成校准数据都满足同样 FDR。<!-- review:SF-2025-CONTEXT-CONFORMAL-ANOMALY:end -->

<!-- review:SF-2025-BADPATCHES:start --><!-- claim:SF-2025-BADPATCHES:start -->揭示 sparse routing 本身会成为 backdoor 的控制面：攻击者不必污染整幅输入，而可利用 patch-to-expert route 集中触发，使 router state、expert specialization 与模型供应链共同进入威胁模型。<!-- claim:SF-2025-BADPATCHES:end -->

CIFAR-10/GTSRB、pMoE/vision transformer 与作者 poisoning 设置不支持外推到 LLM token routing；fine-pruning 结果也不是通用防御保证。<!-- review:SF-2025-BADPATCHES:end -->

<!-- review:SF-2025-NEW-NEWS-SYS2FT:start --><!-- claim:SF-2025-NEW-NEWS-SYS2FT:start -->把新知识写入权重从重复答案监督改成 paraphrase、implication 与 self-QA 的派生监督；训练目标不只记住事实表面，还覆盖事实对下游问题的可用后果。<!-- claim:SF-2025-NEW-NEWS-SYS2FT:end -->

证据来自 hypothetical news、Qwen2.5 0.5B–32B 与作者的 fine-tuning recipe；初步 scaling 和 contextual shadowing 不能视为跨模型、真实持续学习或长期抗遗忘定律。<!-- review:SF-2025-NEW-NEWS-SYS2FT:end -->

<!-- review:SF-2025-INTRA-LAYER-RECURRENCE:start --><!-- claim:SF-2025-INTRA-LAYER-RECURRENCE:start -->把参数深度与计算深度解耦：同一 layer 可在一次 forward 中多次变换 hidden state，且 recurrence placement 成为表示迭代与额外时延之间的设计变量。<!-- claim:SF-2025-INTRA-LAYER-RECURRENCE:end -->

小规模 language-modeling 实验支持 earlier-layer recurrence 的局部趋势；未证明大模型、长上下文、训练稳定性或 serving latency 下仍是最优分配。<!-- review:SF-2025-INTRA-LAYER-RECURRENCE:end -->

<!-- review:SF-2025-CAFCOR:start --><!-- claim:SF-2025-CAFCOR:start -->把 federated trust boundary 从 trusted central server 改为 worker-pair shared randomness：noise ownership 分散到 worker pairs，server 只聚合取消后的统计量，同时 robust aggregation 处理恶意更新。<!-- claim:SF-2025-CAFCOR:end -->

privacy/utility 与 robustness 结论依赖 SecLDP、corruption upper bound、seed secrecy 和披露的优化假设；MNIST/Fashion-MNIST 不证明大模型训练、掉线或密钥生命周期下同样成立。<!-- review:SF-2025-CAFCOR:end -->

<!-- review:SF-2025-DITOX:start --><!-- claim:SF-2025-DITOX:start -->将编译优化正确性从“优化后能加载”提升为 original/optimized differential oracle，并逐 pass 重放以定位破坏语义的 transformation；模型 artifact、input generator、tolerance 与 pass sequence 共同构成 evaluation contract。<!-- claim:SF-2025-DITOX:end -->

130 个 ONNX Hub 模型与 47 个 passes 支持 ONNX Optimizer 缺陷发现，不证明任意 compiler、动态 shape、数值精度或生产输入分布都被覆盖。<!-- review:SF-2025-DITOX:end -->

<!-- review:SF-2025-CAMOUFLAGE:start --><!-- claim:SF-2025-CAMOUFLAGE:start -->把 evidence-based verifier 的 threat model 从单一 classifier perturbation 扩展到 retrieval 与 claim-evidence comparison 的组合攻击面；binary feedback 足以驱动 prompt-optimization/attacker loop。<!-- claim:SF-2025-CAMOUFLAGE:end -->

46.92% 平均 ASR 仅绑定四个 victim systems、十次 query budget 与作者的 semantic/coherence checks；不证明所有 RAG verifier 都同样脆弱，简单化防御也不是通用安全保证。<!-- review:SF-2025-CAMOUFLAGE:end -->

<!-- review:SF-2025-SPECULATIVE-SEARCH:start --><!-- claim:SF-2025-SPECULATIVE-SEARCH:start -->把 speculative execution 从 token prefix 扩展到 reasoning-tree proposal：小模型生成 thought proposal，大模型既验证 token 又执行 thought-quality admission，拒绝后回退到 target-owned search state。<!-- claim:SF-2025-SPECULATIVE-SEARCH:end -->

Qwen/Llama、GSM8K/MATH 与双 A800 实验中的最高 2.12× 是作者条件化结果；理论 rejection 条件不等于开放域 reasoning 的 universal exactness，也未给出生产并发 SLO。<!-- review:SF-2025-SPECULATIVE-SEARCH:end -->

## 4. Benchmark Contracts

作者数字只在下列合同内解释；未公开字段保持 `Not Disclosed`。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HPC-REPRODUCIBILITY | SC24 workshop evidence and practical artifact-reproduction cases | Not Applicable — systems research report | specialized HPC systems; heterogeneous hardware | Not Disclosed — no numerical precision field applies to the report | artifact package/configuration | reproduction evidence | Not Disclosed — no batch field applies to the workshop synthesis | review process | cost-effective reproducibility condition | community workshop synthesis + actionable checklists |
| SF-2025-ROBUST-2D-DPO | noisy preference alignment experiments | open-source DPO/2D-DPO models disclosed in v1 | Not Disclosed | Not Disclosed | prompt + paired segmented responses | policy response | Not Disclosed | offline training | win rate / robustness under disclosed noise; no production SLO | author evaluation under label-flip and segment perturbation |
| SF-2025-ROBRIDGE | MetaWorld、RoboSuite、5 个现实操作任务 | VLM HCP + RL GEA | Kinova Gen3；2×RealSense；training hardware Not Disclosed | Not Disclosed | 任务/视觉观察 | action trajectory | 每现实任务 5 samples | Not Disclosed | task success；无 latency/safety SLO | simulator success + real task completion |
| SF-2025-POSEPILOT | nuScenes、Vista、DrivingWorld 与通用视频 | diffusion / autoregressive video world models | NVIDIA A100 | Not Disclosed | 1280×720；88 frames（公开设置） | video frames | Not Disclosed | Not Disclosed | pose error / generation quality；无 closed-loop SLO | translation/rotation error + video metrics |
| SF-2025-VLORP | commonsense、MMLU、GSM8K fine-tuning | LLaMA2-7B and disclosed baselines | Not Disclosed | Not Disclosed | max length 1024 | task answer | 16；含 gradient accumulation | offline | memory、throughput、task score；无 production SLO | official task metrics + memory profiler |
| SF-2025-LENGTH-BIASED-LLM-EVAL | MQM machine-translation evaluation at segment/document/5-document granularity | Claude 3.5 Haiku/Sonnet and GPT-4o variants disclosed in v1 | hosted API; hardware Not Disclosed | Not Disclosed | about 103/507/2713 GPT-4o tokens by granularity | MQM error spans and rankings | one evaluation input | API concurrency Not Disclosed | error recall + system-ranking accuracy; no latency SLO | MQM annotations / ranking agreement |
| SF-2025-CONTEXT-CONFORMAL-ANOMALY | synthetic data, thyroid and O-RAN anomaly detection | arbitrary pre-trained anomaly score + C-PP-COAD | Not Disclosed | Not Disclosed | streaming observations + context + calibration batches | online anomaly decisions | online sequential | one stream per experiment | decaying-memory FDR, power and real-data acquisition | formal online-testing metric + disclosed datasets |
| SF-2025-BADPATCHES | CIFAR-10、GTSRB patch poisoning | pMoE、MoE vision transformers | NVIDIA T4 | Not Disclosed | image patches | class label | Not Disclosed | offline | ASR、clean accuracy；无 production SLO | classification + attack success |
| SF-2025-NEW-NEWS-SYS2FT | hypothetical news across math/code/discovery/event domains | Qwen2.5 0.5B–32B | NVIDIA H100 | bfloat16 | news/context/question；tokens Not Disclosed | answer | Not Disclosed | offline | news QA + general capability retention；无 production SLO | dataset exact/LLM-graded metrics per v1 |
| SF-2025-INTRA-LAYER-RECURRENCE | language modeling and layer-position ablations | small recurrent Transformer variants | Not Disclosed | Not Disclosed | sequence length Not Disclosed | next-token logits | Not Disclosed | offline | perplexity / parameter count；无 serving SLO | held-out language-modeling perplexity |
| SF-2025-CAFCOR | adversarial federated/distributed learning | CafCor under SecLDP | Not Disclosed | Not Disclosed | MNIST/Fashion-MNIST worker updates | global model update | participant count varies by experiment | server + workers; exact concurrency Not Disclosed | privacy / robustness / utility bounds; no production SLO | theoretical guarantees + benchmark accuracy |
| SF-2025-DITOX | 130 ONNX Hub models；47 optimizer passes | ONNX Optimizer | Not Disclosed | model-dependent | user-defined model inputs | original/optimized outputs | one model/pass replay | offline | crash、invalid model、output discrepancy；tolerance per setup | differential execution + pass localization |
| SF-2025-CAMOUFLAGE | four evidence-based misinformation detectors | two academic systems + two real-world APIs; attacker LLMs disclosed in v1 | hosted API / hardware Not Disclosed | Not Disclosed | short claims; 1–2 sentences typical | binary verdict + adversarial rewrite | one claim | up to 10 victim queries per attempt | ASR with semantic equivalence/coherence; no latency SLO | victim verdict + embedding/LLM checks + human evaluation |
| SF-2025-SPECULATIVE-SEARCH | GSM8K、MATH tree search | Qwen and Llama target/draft pairs | 2×NVIDIA A800 80GB | Not Disclosed | task prompts；length Not Disclosed | reasoning thoughts / answers | Not Disclosed | Not Disclosed | quality parity + author speedup up to 2.12×；无 production SLO | task accuracy + wall-clock/token accounting |

## 5. Deep Analysis Selection

长叙事上限为 3。7–9 分 family 均完成 deep review；未入选长叙事不等于未审计。

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HPC-REPRODUCIBILITY | score_7_9 | selected | DA-EVIDENCE-CONTRACT | — | 建立可复算系统 artifact / environment contract | analysis:DA-EVIDENCE-CONTRACT |
| SF-2025-ROBRIDGE | score_7_9 | not_selected | — | — | controller handoff 已由 Ch26 完整承载；保留在 review | analysis-decision:SF-2025-ROBRIDGE |
| SF-2025-VLORP | score_7_9 | not_selected | — | — | optimizer-state 路线已有完整 owner；本日不重复长叙事 | analysis-decision:SF-2025-VLORP |
| SF-2025-LENGTH-BIASED-LLM-EVAL | score_7_9 | selected | DA-EVIDENCE-CONTRACT | — | 揭示 evaluator input granularity 会改变结论 | analysis:DA-EVIDENCE-CONTRACT |
| SF-2025-CONTEXT-CONFORMAL-ANOMALY | score_7_9 | selected | DA-EVIDENCE-CONTRACT | — | 把 calibration ownership 和 FDR 写入在线 evidence | analysis:DA-EVIDENCE-CONTRACT |
| SF-2025-NEW-NEWS-SYS2FT | score_7_9 | not_selected | — | — | 知识派生监督已由 Ch29 主线承载；保留在 review | analysis-decision:SF-2025-NEW-NEWS-SYS2FT |
| SF-2025-CAFCOR | score_7_9 | selected | DA-DISTRIBUTED-TRUST | — | 改变 federated noise 与 trust ownership | analysis:DA-DISTRIBUTED-TRUST |
| SF-2025-DITOX | score_7_9 | selected | DA-EVIDENCE-CONTRACT | — | 改变优化 artifact 的 release evidence contract | analysis:DA-EVIDENCE-CONTRACT |
| SF-2025-CAMOUFLAGE | score_7_9 | selected | DA-EVIDENCE-CONTRACT | — | 扩展 retrieval / comparison 组合攻击面 | analysis:DA-EVIDENCE-CONTRACT |
| SF-2025-SPECULATIVE-SEARCH | score_7_9 | selected | DA-REASONING-COMMIT | — | 把 proposal/verification 扩展到 reasoning-tree state | analysis:DA-REASONING-COMMIT |

### 从单一分数到可复算、可攻击、可持续校准的 evidence contract
<!-- analysis:DA-EVIDENCE-CONTRACT:start -->系统实验最初可以用论文、脚本和一个最终分数表达；当硬件、环境、输入粒度、持续漂移和对抗者进入路径后，结果已经不再由单一模型输出拥有。HPC reproducibility 把 artifact identity、environment、acceptance condition 与 reviewer cost 纳入合同；长度偏差实验进一步证明 evaluator 的 chunking 与 focus policy 会改变 error recall 和 ranking；在线 conformal monitoring 则把 calibration data ownership、acquisition decision 与 time-averaged FDR 变成持续状态。编译优化需要 original/optimized differential oracle 和逐 pass localization，evidence-based verifier 还必须接受针对 retrieval 与 comparison 的组合攻击。收益是结论可重放、可拒绝和可回滚；代价是更高 artifact 成本、校准假设、oracle coverage 与攻击面。轻量 benchmark 在依赖稳定、输入短且风险低时仍成立。<!-- analysis:DA-EVIDENCE-CONTRACT:end -->

### 从 trusted server 到分散持有的 privacy noise
<!-- analysis:DA-DISTRIBUTED-TRUST:start -->传统 federated learning 把聚合与 privacy authority 集中在 server；local DP 去掉信任，却用更大的独立噪声支付 utility。CafCor 的分支让 worker pair 持有 shared randomness，相关噪声在聚合后部分抵消，同时 robust aggregation 对抗恶意 worker。它减少对 trusted server 的依赖，但新增 seed lifecycle、collusion threshold、掉线恢复和 corruption upper bound；在没有共享秘密或参与者高度动态时，local DP/secure aggregation 仍是更清晰的旧路径。<!-- analysis:DA-DISTRIBUTED-TRUST:end -->

### 从 token draft 到 reasoning-tree proposal/commit
<!-- analysis:DA-REASONING-COMMIT:start -->token speculative decoding 假设 draft 与 target 对同一 prefix 提案；tree reasoning 的状态则是多条 thought branch，低质量分支会放大搜索成本。SpecSearch 让小模型拥有 proposal，大模型保留 quality admission 与 fallback，从而把控制权放在 target。收益是作者条件下的 latency 降低；代价是双模型内存、验证成本和质量判定误差。单模型搜索在低并发、小树或 draft gap 较大时仍合理。下一压力是将 thought acceptance 与可验证 reward、并发 scheduling 和 reproducible search trace 统一。<!-- analysis:DA-REASONING-COMMIT:end -->

<!-- analysis-decision:SF-2025-ROBRIDGE:start -->RoBridge 的分层 controller handoff 已在 Ch26 形成完整机制主线；其受限实验边界保留在 Source Review，不占用第四个长叙事。<!-- analysis-decision:SF-2025-ROBRIDGE:end -->
<!-- analysis-decision:SF-2025-VLORP:start -->VLoRP 已完成 deep Review，但 optimizer-state 的主线已由 Ch28 完整承载；相较当日 evidence/security 修正，它不占用独立长叙事。<!-- analysis-decision:SF-2025-VLORP:end -->
<!-- analysis-decision:SF-2025-NEW-NEWS-SYS2FT:start -->System-2 fine-tuning 的派生监督与 contextual shadowing 已由 Ch29 的知识写权重主线承载；本日保留独立 deep Review，不重复扩写长叙事。<!-- analysis-decision:SF-2025-NEW-NEWS-SYS2FT:end -->

## 6. Books Comparison

14/14 候选均完成目标与相邻章节比较。当前书稿由后续、更完整且已审计的机制证据承载本日增量，因此全部为 `No Change — Existing Coverage`；这不是把候选留在日报，而是明确证明没有新的长期命题需要写入。

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HPC-REPRODUCIBILITY | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2025-HPC-REPRODUCIBILITY | delta:SF-2025-HPC-REPRODUCIBILITY | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-HPC-REPRODUCIBILITY |
| SF-2025-ROBUST-2D-DPO | TRAIN-DPO | books/part-04-training-system/34-dpo.md#L1 | books/part-04-training-system/33-grpo.md#L1; books/part-04-training-system/35-checkpoint.md#L1 | existing:SF-2025-ROBUST-2D-DPO | delta:SF-2025-ROBUST-2D-DPO | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-ROBUST-2D-DPO |
| SF-2025-ROBRIDGE | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1; books/part-04-training-system/27-data.md#L1 | existing:SF-2025-ROBRIDGE | delta:SF-2025-ROBRIDGE | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-ROBRIDGE |
| SF-2025-POSEPILOT | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | existing:SF-2025-POSEPILOT | delta:SF-2025-POSEPILOT | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-POSEPILOT |
| SF-2025-VLORP | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L1 | books/part-04-training-system/27-data.md#L1; books/part-04-training-system/29-sft.md#L1 | existing:SF-2025-VLORP | delta:SF-2025-VLORP | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-VLORP |
| SF-2025-LENGTH-BIASED-LLM-EVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-05-inference-system/45-long-context-inference.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2025-LENGTH-BIASED-LLM-EVAL | delta:SF-2025-LENGTH-BIASED-LLM-EVAL | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-LENGTH-BIASED-LLM-EVAL |
| SF-2025-CONTEXT-CONFORMAL-ANOMALY | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-06-ai-infrastructure/68-logging.md#L1 | existing:SF-2025-CONTEXT-CONFORMAL-ANOMALY | delta:SF-2025-CONTEXT-CONFORMAL-ANOMALY | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY |
| SF-2025-BADPATCHES | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1; books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2025-BADPATCHES | delta:SF-2025-BADPATCHES | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-BADPATCHES |
| SF-2025-NEW-NEWS-SYS2FT | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-04-training-system/30-lora.md#L1 | existing:SF-2025-NEW-NEWS-SYS2FT | delta:SF-2025-NEW-NEWS-SYS2FT | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-NEW-NEWS-SYS2FT |
| SF-2025-INTRA-LAYER-RECURRENCE | MODEL-TRANSFORMER-LAYER | books/part-02-model/17-transformer-layer.md#L1 | books/part-02-model/16-attention-mlp.md#L1; books/part-02-model/18-decoder-only.md#L1 | existing:SF-2025-INTRA-LAYER-RECURRENCE | delta:SF-2025-INTRA-LAYER-RECURRENCE | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-INTRA-LAYER-RECURRENCE |
| SF-2025-CAFCOR | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-04-training-system/36-distributed-training.md#L1; books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2025-CAFCOR | delta:SF-2025-CAFCOR | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-CAFCOR |
| SF-2025-DITOX | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2025-DITOX | delta:SF-2025-DITOX | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-DITOX |
| SF-2025-CAMOUFLAGE | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-07-agent/76-rag.md#L1 | existing:SF-2025-CAMOUFLAGE | delta:SF-2025-CAMOUFLAGE | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-CAMOUFLAGE |
| SF-2025-SPECULATIVE-SEARCH | AGENT-PLANNING | books/part-07-agent/79-planning.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L1; books/part-07-agent/80-reflection.md#L1 | existing:SF-2025-SPECULATIVE-SEARCH | delta:SF-2025-SPECULATIVE-SEARCH | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-SPECULATIVE-SEARCH |
<!-- books-review:SF-2025-HPC-REPRODUCIBILITY:start --><!-- existing:SF-2025-HPC-REPRODUCIBILITY:start -->Ch66 已将 environment、artifact identity、workload contract、acceptance condition 与 evidence cost 串成可复算 release gate。<!-- existing:SF-2025-HPC-REPRODUCIBILITY:end --><!-- delta:SF-2025-HPC-REPRODUCIBILITY:start -->该报告给出早期 systems/HPC 社区证据，但不新增当前 owner 未覆盖的责任。<!-- delta:SF-2025-HPC-REPRODUCIBILITY:end -->Ch65 拥有执行资源；Ch67 拥有运行监测。<!-- books-review:SF-2025-HPC-REPRODUCIBILITY:end -->
<!-- books-review:SF-2025-ROBUST-2D-DPO:start --><!-- existing:SF-2025-ROBUST-2D-DPO:start -->Ch34 已把 preference noise、segment/token weighting、beta/update scale 与 evaluator contract 分离。<!-- existing:SF-2025-ROBUST-2D-DPO:end --><!-- delta:SF-2025-ROBUST-2D-DPO:start -->2D-DPO 的 segment score noise 是该主线的受限 objective 分支。<!-- delta:SF-2025-ROBUST-2D-DPO:end -->Ch33 拥有在线 RL 分支；Ch35 拥有 checkpoint state。<!-- books-review:SF-2025-ROBUST-2D-DPO:end -->
<!-- books-review:SF-2025-ROBRIDGE:start --><!-- existing:SF-2025-ROBRIDGE:start -->Ch26 已将 high-level proposal、symbolic/action handoff、low-level controller、sim-to-real 和 safety envelope 串成闭环。<!-- existing:SF-2025-ROBRIDGE:end --><!-- delta:SF-2025-ROBRIDGE:start -->本论文是该分层的早期实例，不增加新的状态 owner。<!-- delta:SF-2025-ROBRIDGE:end -->Ch25 拥有 environment transition；Ch27 拥有训练数据。<!-- books-review:SF-2025-ROBRIDGE:end -->
<!-- books-review:SF-2025-POSEPILOT:start --><!-- existing:SF-2025-POSEPILOT:start -->Ch25 已区分 video generation、geometry-conditioned transition、controllability 与 policy evidence。<!-- existing:SF-2025-POSEPILOT:end --><!-- delta:SF-2025-POSEPILOT:start -->self-supervised pose warping 是几何约束的实现分支。<!-- delta:SF-2025-POSEPILOT:end -->Ch24 拥有生成 factorization；Ch26 拥有物理动作闭环。<!-- books-review:SF-2025-POSEPILOT:end -->
<!-- books-review:SF-2025-VLORP:start --><!-- existing:SF-2025-VLORP:start -->Ch28 已覆盖低秩梯度、optimizer state、显存预算和压缩误差的共同权衡。<!-- existing:SF-2025-VLORP:end --><!-- delta:SF-2025-VLORP:start -->granularity/ProjFactor 提供案例但不改现有设计结论。<!-- delta:SF-2025-VLORP:end -->Ch27 拥有数据；Ch29 拥有监督行为拟合。<!-- books-review:SF-2025-VLORP:end -->
<!-- books-review:SF-2025-LENGTH-BIASED-LLM-EVAL:start --><!-- existing:SF-2025-LENGTH-BIASED-LLM-EVAL:start -->Ch66 已要求 evaluator contract 绑定 input/output length、chunking、judge identity、calibration 与 failure mode。<!-- existing:SF-2025-LENGTH-BIASED-LLM-EVAL:end --><!-- delta:SF-2025-LENGTH-BIASED-LLM-EVAL:start -->MT/MQM 结果给出 length-dependent judge 的早期受限证据，不新增当前命题。<!-- delta:SF-2025-LENGTH-BIASED-LLM-EVAL:end -->Ch45 拥有 long-context runtime；Ch67 拥有线上 drift signal。<!-- books-review:SF-2025-LENGTH-BIASED-LLM-EVAL:end -->
<!-- books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY:start --><!-- existing:SF-2025-CONTEXT-CONFORMAL-ANOMALY:start -->Ch67 已覆盖 reference-window calibration、sequential alarm、multiplicity control 与 conformal abstention。<!-- existing:SF-2025-CONTEXT-CONFORMAL-ANOMALY:end --><!-- delta:SF-2025-CONTEXT-CONFORMAL-ANOMALY:start -->C-PP-COAD 以 synthetic/real calibration acquisition 展示该路线，但不改变现有 owner。<!-- delta:SF-2025-CONTEXT-CONFORMAL-ANOMALY:end -->Ch66 拥有质量/统计保证；Ch68 拥有事件记录。<!-- books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY:end -->
<!-- books-review:SF-2025-BADPATCHES:start --><!-- existing:SF-2025-BADPATCHES:start -->Ch72 已把 router/expert state、model artifact provenance 与 backdoor threat 连接。<!-- existing:SF-2025-BADPATCHES:end --><!-- delta:SF-2025-BADPATCHES:start -->patch routing 是 vision-MoE 受限案例。<!-- delta:SF-2025-BADPATCHES:end -->Ch71 拥有 tenancy；Ch73 拥有 release gate。<!-- books-review:SF-2025-BADPATCHES:end -->
<!-- books-review:SF-2025-NEW-NEWS-SYS2FT:start --><!-- existing:SF-2025-NEW-NEWS-SYS2FT:start -->Ch29 已覆盖事实到派生监督、contextual shadowing、general-capability guardrail。<!-- existing:SF-2025-NEW-NEWS-SYS2FT:end --><!-- delta:SF-2025-NEW-NEWS-SYS2FT:start -->Self-QA/implication 是该主线的实验实例。<!-- delta:SF-2025-NEW-NEWS-SYS2FT:end -->Ch28 拥有 pretraining objective；Ch30 拥有参数高效适配。<!-- books-review:SF-2025-NEW-NEWS-SYS2FT:end -->
<!-- books-review:SF-2025-INTRA-LAYER-RECURRENCE:start --><!-- existing:SF-2025-INTRA-LAYER-RECURRENCE:start -->Ch17 已区分参数深度、计算深度、weight sharing 与 recurrence placement。<!-- existing:SF-2025-INTRA-LAYER-RECURRENCE:end --><!-- delta:SF-2025-INTRA-LAYER-RECURRENCE:start -->ILR 不改变该层级结论。<!-- delta:SF-2025-INTRA-LAYER-RECURRENCE:end -->Ch16 拥有 attention/MLP；Ch18 拥有 decoder-only composition。<!-- books-review:SF-2025-INTRA-LAYER-RECURRENCE:end -->
<!-- books-review:SF-2025-CAFCOR:start --><!-- existing:SF-2025-CAFCOR:start -->Ch72 已把 federated trust boundary、worker/server threat model、privacy noise ownership 与 key lifecycle 纳入安全合同。<!-- existing:SF-2025-CAFCOR:end --><!-- delta:SF-2025-CAFCOR:start -->CafCor 的 pairwise shared randomness 是该路线的受限实现分支。<!-- delta:SF-2025-CAFCOR:end -->Ch36 拥有 distributed optimization；Ch71 拥有 participant isolation。<!-- books-review:SF-2025-CAFCOR:end -->
<!-- books-review:SF-2025-DITOX:start --><!-- existing:SF-2025-DITOX:start -->Ch66 已将 differential testing、pass localization、artifact identity 与 release evidence 写成完整合同。<!-- existing:SF-2025-DITOX:end --><!-- delta:SF-2025-DITOX:start -->ONNX 结果提供故障实例但不新增机制。<!-- delta:SF-2025-DITOX:end -->Ch65 拥有资源执行；Ch67 拥有 telemetry。<!-- books-review:SF-2025-DITOX:end -->
<!-- books-review:SF-2025-CAMOUFLAGE:start --><!-- existing:SF-2025-CAMOUFLAGE:start -->Ch72 已将 retrieval、evidence comparison、agent feedback loop 与 adversarial evaluator 纳入组合 threat model。<!-- existing:SF-2025-CAMOUFLAGE:end --><!-- delta:SF-2025-CAMOUFLAGE:start -->CAMOUFLAGE 提供 binary-feedback attack 的早期案例，不新增当前安全结论。<!-- delta:SF-2025-CAMOUFLAGE:end -->Ch66 拥有 evaluator contract；Ch76 拥有 retrieval state。<!-- books-review:SF-2025-CAMOUFLAGE:end -->
<!-- books-review:SF-2025-SPECULATIVE-SEARCH:start --><!-- existing:SF-2025-SPECULATIVE-SEARCH:start -->Ch79 已覆盖 proposal、verification、commit/rollback 与 search state；Ch48 拥有 token-level speculation。<!-- existing:SF-2025-SPECULATIVE-SEARCH:end --><!-- delta:SF-2025-SPECULATIVE-SEARCH:start -->thought-level speculative search 属 principle reuse，不应搬入推理解码 owner。<!-- delta:SF-2025-SPECULATIVE-SEARCH:end -->Ch78 拥有 tool action；Ch80 拥有 reflection。<!-- books-review:SF-2025-SPECULATIVE-SEARCH:end -->

<!-- books-queue:20250504:start -->Books write queue = 0；14 项均由现有 canonical owner 完整承载。<!-- books-queue:20250504:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20250504-COVERAGE | fresh-context:may04-independent-audit | coverage | coverage:SRC-ARXIV:20250504 | — | resolved:FINDING-MAY04-FN-01；全量 150/150 重审，分母 8→14、closure 142→136、false positives=0 | passed |
| SA-20250504-EVIDENCE | fresh-context:may04-independent-audit | evidence | review:SF-2025-HPC-REPRODUCIBILITY; review:SF-2025-ROBUST-2D-DPO; review:SF-2025-LENGTH-BIASED-LLM-EVAL; review:SF-2025-CONTEXT-CONFORMAL-ANOMALY; review:SF-2025-CAFCOR; review:SF-2025-CAMOUFLAGE; review:SF-2025-DITOX | — | resolved:FINDING-MAY04-LOC-01；14/14 使用 source-specific exact-v1 section/appendix locator 并重算 provenance | passed |
| SA-20250504-SELECTION | fresh-context:may04-independent-audit | deep_analysis_selection | analysis:DA-EVIDENCE-CONTRACT; analysis:DA-DISTRIBUTED-TRUST; analysis:DA-REASONING-COMMIT; analysis-decision:SF-2025-VLORP | — | resolved:FINDING-MAY04-SEL-01；重放全 frontier，三项长叙事覆盖 evidence、trust 与 reasoning commit | passed |
| SA-20250504-BOOKS | fresh-context:may04-independent-audit | books | books-review:SF-2025-HPC-REPRODUCIBILITY; books-review:SF-2025-ROBUST-2D-DPO; books-review:SF-2025-LENGTH-BIASED-LLM-EVAL; books-review:SF-2025-CONTEXT-CONFORMAL-ANOMALY; books-review:SF-2025-CAFCOR; books-review:SF-2025-CAMOUFLAGE; books-queue:20250504 | — | 14/14 target/adjacent 对读；均由当前 canonical owner 更完整承载，queue=0 | passed |

## 8. Ignored Noise

136 个未保留 identity 已在 `_sources` ledger 中逐项记录标题、摘要命题与不进入长期 AI-System 分母的具体理由；主要类别是垂直应用、局部 accuracy/representation 增量、通用优化理论、单领域 benchmark 和不改变系统 contract 的 survey。它们完成的是 pre-denominator closure，不伪装成全文 Review。

## 9. Recommended Action

1. Sunday owner Weekly 只聚合本日报 14 个 family，并按 first-public date 去重；不得把 136 条 closure 重新膨胀为评分候选。
2. 后续若 source revision 改变 method/evaluation boundary，应重开真实 owner date，而不是在发现日追加新分数。

## 10. Repository Changes

- 冻结 2025-05-04 official arXiv snapshot、150 条全语义 screening ledger 与 14 份 exact-v1 route evidence。
- 独立审计修复 6 个 denominator false negatives 与 8 项原有 generic locator；未修改 Books、ROADMAP、DECISIONS 或 LEARNING_STATE。
- 未 stage、commit 或 push。

## 11. Open Questions

- low-rank gradient projection 在完整 pretraining、ZeRO/FSDP 与 tensor parallel 下如何分配 projection/optimizer state？
- compiler differential oracle 如何覆盖动态 shape、随机算子、量化与跨后端 tolerance？
- thought-level speculative acceptance 如何与可验证 reward、并发 scheduling 和 search-trace reproducibility 联合设计？

## 12. Sources

访问日期为 2026-08-31；事件日期使用 arXiv v1 timestamp。

- https://export.arxiv.org/api/query
- https://arxiv.org/html/2505.01671v1
- https://arxiv.org/html/2505.01706v1
- https://arxiv.org/html/2505.01709v1
- https://arxiv.org/html/2505.01729v1
- https://arxiv.org/html/2505.01744v1
- https://arxiv.org/html/2505.01761v1
- https://arxiv.org/html/2505.01783v1
- https://arxiv.org/html/2505.01811v1
- https://arxiv.org/html/2505.01812v1
- https://arxiv.org/html/2505.01855v1
- https://arxiv.org/html/2505.01874v1
- https://arxiv.org/html/2505.01892v1
- https://arxiv.org/html/2505.01900v1
- https://arxiv.org/html/2505.02865v1

## 13. Final Status

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；fresh-context unresolved findings=0。

150/150 denominator audit、14/14 exact-v1 Review、全 frontier Selection、14/14 Books Comparison 与四范围 Semantic Audit 均已闭合；Books write queue=0。
