# Daily Research — 2025-05-01

**Research Date:** 2025-05-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2025-04-30 09:00:00 ～ 2025-05-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed；四个 fresh-context Semantic Audit scope 均已通过，状态真值见第 7 节

## Executive Summary

本轮不是从 W18 的旧 `/30` 评分反推日报，而是从严格窗口的官方 arXiv Atom 快照重新建立分母。快照包含 853 条 raw identities：217 条 Core Daily 逐项完成 title+abstract 语义筛选；122 条 keyword-routed 分类中 107 条触发系统关键词并继续语义判断；514 条非注册分类完成 identity/date/topic closure。首次冻结后保留 15 个 Source Family；fresh-context 漏检审计发现 MutedRAG、LongFuncEval、VDDP 与 Coral Protocol 四个 false negative，完成 exact-v1 Review 后重新冻结为 19 个（2.23%），其余 834 项都有 family-specific pre-denominator closure。

19 个候选均已读取 exact-v1 的 Method、evaluation、limitations/结论及已公开 artifact，完成 V2 三维评分、route-matched Review、Benchmark Contract 和 Books Comparison。最强的长期线索是：训练系统从人工并行组合推进到 profile/search/telemetry/fallback 的 plan control；模型 artifact store 从文件级对象推进到 tensor/delta 的物理共享、但不合并逻辑身份；端侧推理把 logical tensor 与 device object 解耦。SWE-smith、DeepSeek-Prover、Who&When、WebThinker 等已由 Books 现有主线完整承载。

Coverage、Evidence 与 Books Gate 均已闭合。Books 比较发现 COSMOS、ZipLLM 与 Galvatron 三项可定位长期增量；root 已把三项分别写入 Ch70、Ch59 与 Ch36。未参与本日报主要写作或共享 Books 写回的 reviewer 随后重读 exact-v1、owner 与相邻章节，确认三项已进入旧路径、约束变化、state/authority、trade-off、failure/fallback 的正文链；复核发现的三处相邻章节旧路径名也已修正。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2025-05-01 |
| Window End | 2025-05-01 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | |
| Changed Source IDs | |
| Previous Denominator ID | |
| Denominator ID | DEN-20250501-a5ee7eba1414127491c0 |
| Denominator Frozen At | 2026-08-31T17:50:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2025-04-30T09:00:00+08:00 | 2025-05-01T09:00:00+08:00 | 2026-08-31T17:23:00+08:00 | official Atom API `submittedDate:[202504300100 TO 202505010100]`; Core full semantic + registered keyword route | checked | 853 | SF-2025-COSMOS-ADAPTATION<br>SF-2025-ZIPLLM-STORAGE<br>SF-2025-BAYES-EVAL-CONFIDENCE<br>SF-2025-PHI4-REASONING<br>SF-2025-NEXUS-GEN<br>SF-2025-SHORTERBETTER<br>SF-2025-GALVATRON<br>SF-2025-RWKV-X<br>SF-2025-RAGFORENSICS<br>SF-2025-WEBTHINKER<br>SF-2025-SWE-SMITH<br>SF-2025-DEEPSEEK-PROVER-V2<br>SF-2025-WHOWHEN<br>SF-2025-ML-DRIFT<br>SF-2025-TRAJ-BOOTSTRAP<br>SF-2025-MUTEDRAG-AVAILABILITY<br>SF-2025-LONGFUNCEVAL<br>SF-2025-VDDP<br>SF-2025-CORAL-PROTOCOL | page=1; final_cursor=end; totalResults=853 | 2025-05-01T01:00:00Z | coverage:SRC-ARXIV:20250501 | — |

<!-- coverage:SRC-ARXIV:20250501:start -->官方 Atom 快照 `arxiv-20250501.xml`（SHA-256 `2baec2f5e321c55bba9c4fa4e839dab866b43827cddf185cc0f7535239968b01`）返回 853/853；`screening-ledger.json` 保存 217 条 Core 逐项语义筛选、122 条注册分类路由（107 条 keyword-triggered）、19 retained 与 834 family-specific closure。首次冻结后的 fresh-context audit 发现并修复 4 个 false negative。<!-- coverage:SRC-ARXIV:20250501:end -->

### Coverage Limitations

- 当前来源注册表自 2026-08-25 生效，不能把后来新增的 organization/backstop 列表冒充 2025-05-01 当时已存在的确定性分母。本次以官方 arXiv exact-window 快照闭合论文 recall，并用 W18 只作 prior discovery baseline；MiMo/Amazon 等当日产品公告因缺公开机制留在 screening closure，不进入长期机制候选。
- 853 是 raw identity denominator，不是候选数；非注册分类和未达到长期 AI-System admission 的论文均保留逐 family closure，而不是静默删除。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-COSMOS-ADAPTATION | arXiv:2505.01449v1 | paper-v1:2505.01449 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2025-COSMOS-ADAPTATION | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2025-COSMOS-ADAPTATION | yes |
| SF-2025-ZIPLLM-STORAGE | arXiv:2505.06252v1 | paper-v1:2505.06252 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2025-ZIPLLM-STORAGE | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Integrate | books-review:SF-2025-ZIPLLM-STORAGE | yes |
| SF-2025-BAYES-EVAL-CONFIDENCE | arXiv:2504.21303v1 | paper-v1:2504.21303 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-BAYES-EVAL-CONFIDENCE | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-BAYES-EVAL-CONFIDENCE | yes |
| SF-2025-PHI4-REASONING | arXiv:2504.21318v1 | paper-v1:2504.21318 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-PHI4-REASONING | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2025-PHI4-REASONING | yes |
| SF-2025-NEXUS-GEN | arXiv:2504.21356v1 | paper-v1:2504.21356 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-NEXUS-GEN | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2025-NEXUS-GEN | no |
| SF-2025-SHORTERBETTER | arXiv:2504.21370v1 | paper-v1:2504.21370 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-SHORTERBETTER | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2025-SHORTERBETTER | yes |
| SF-2025-GALVATRON | arXiv:2504.21411v1 | paper-v1:2504.21411 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2025-GALVATRON | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2025-GALVATRON | yes |
| SF-2025-RWKV-X | arXiv:2504.21463v1 | paper-v1:2504.21463 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-RWKV-X | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2025-RWKV-X | yes |
| SF-2025-RAGFORENSICS | arXiv:2504.21668v1 | paper-v1:2504.21668 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-RAGFORENSICS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-RAGFORENSICS | yes |
| SF-2025-WEBTHINKER | arXiv:2504.21776v1 | paper-v1:2504.21776 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-WEBTHINKER | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2025-WEBTHINKER | yes |
| SF-2025-SWE-SMITH | arXiv:2504.21798v1 | paper-v1:2504.21798 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-SWE-SMITH | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2025-SWE-SMITH | yes |
| SF-2025-DEEPSEEK-PROVER-V2 | arXiv:2504.21801v1 | paper-v1:2504.21801 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-DEEPSEEK-PROVER-V2 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2025-DEEPSEEK-PROVER-V2 | yes |
| SF-2025-WHOWHEN | arXiv:2505.00212v1 | paper-v1:2505.00212 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-WHOWHEN | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2025-WHOWHEN | yes |
| SF-2025-ML-DRIFT | arXiv:2505.00232v1 | paper-v1:2505.00232 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-ML-DRIFT | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2025-ML-DRIFT | yes |
| SF-2025-TRAJ-BOOTSTRAP | arXiv:2505.00234v1 | paper-v1:2505.00234 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2025-TRAJ-BOOTSTRAP | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2025-TRAJ-BOOTSTRAP | yes |
| SF-2025-MUTEDRAG-AVAILABILITY | arXiv:2504.21680v1 | paper-v1:2504.21680 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-MUTEDRAG-AVAILABILITY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-MUTEDRAG-AVAILABILITY | yes |
| SF-2025-LONGFUNCEVAL | arXiv:2505.10570v1 | paper-v1:2505.10570 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-LONGFUNCEVAL | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-LONGFUNCEVAL | yes |
| SF-2025-VDDP | arXiv:2504.21752v1 | paper-v1:2504.21752 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-VDDP | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-VDDP | yes |
| SF-2025-CORAL-PROTOCOL | arXiv:2505.00749v1 | paper-v1:2505.00749 | 2025-W18 | 2025-04-30 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2025-CORAL-PROTOCOL | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2025-CORAL-PROTOCOL | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-COSMOS-ADAPTATION | RP-fa4addb9782006c7 | deep | arXiv:2505.01449v1 | SRC-ARXIV@arXiv:2505.01449v1 | https://arxiv.org/html/2505.01449v1#S3; https://arxiv.org/html/2505.01449v1#S4 | https://arxiv.org/html/2505.01449v1#S5; https://arxiv.org/html/2505.01449v1#A4 | https://arxiv.org/html/2505.01449v1#S6; https://arxiv.org/html/2505.01449v1#A9 | Not Disclosed — exact-v1 does not publish a frozen implementation artifact used in this review | claim:SF-2025-COSMOS-ADAPTATION | complete |
| SF-2025-ZIPLLM-STORAGE | RP-e50a0d20fb298132 | deep | arXiv:2505.06252v1 | SRC-ARXIV@arXiv:2505.06252v1 | https://arxiv.org/html/2505.06252v1#S3; https://arxiv.org/html/2505.06252v1#S4 | https://arxiv.org/html/2505.06252v1#S5; https://arxiv.org/html/2505.06252v1#A1 | https://arxiv.org/html/2505.06252v1#S6; https://arxiv.org/html/2505.06252v1#S7 | https://storageai.github.io/ZLLM/ — project artifact linked from exact-v1 | claim:SF-2025-ZIPLLM-STORAGE | complete |
| SF-2025-BAYES-EVAL-CONFIDENCE | RP-de7762d3e11b71a2 | deep | arXiv:2504.21303v1 | SRC-ARXIV@arXiv:2504.21303v1 | https://arxiv.org/html/2504.21303v1#S2; https://arxiv.org/html/2504.21303v1#S2.SS2 | https://arxiv.org/html/2504.21303v1#S3; https://arxiv.org/html/2504.21303v1#S4 | https://arxiv.org/html/2504.21303v1#S5.SS1 | Not Disclosed — exact-v1 does not identify a released evaluation implementation | claim:SF-2025-BAYES-EVAL-CONFIDENCE | complete |
| SF-2025-PHI4-REASONING | RP-411e602703ccd78d | standard | arXiv:2504.21318v1 | SRC-ARXIV@arXiv:2504.21318v1 | https://arxiv.org/html/2504.21318v1#S2; https://arxiv.org/html/2504.21318v1#S3; https://arxiv.org/html/2504.21318v1#S4 | https://arxiv.org/html/2504.21318v1#S5; https://arxiv.org/html/2504.21318v1#A1 | https://arxiv.org/html/2504.21318v1#S6 | https://github.com/microsoft/eureka-ml-insights — linked evaluation artifact; full training stack Not Disclosed | claim:SF-2025-PHI4-REASONING | complete |
| SF-2025-NEXUS-GEN | RP-955bd54a77a598c9 | standard | arXiv:2504.21356v1 | SRC-ARXIV@arXiv:2504.21356v1 | https://arxiv.org/html/2504.21356v1#S2.SS1; https://arxiv.org/html/2504.21356v1#S2.SS2; https://arxiv.org/html/2504.21356v1#S2.SS3 | https://arxiv.org/html/2504.21356v1#S3 | Not Disclosed — exact-v1 has no dedicated limitations section and provides qualitative case studies rather than a matched broad benchmark | https://github.com/modelscope/Nexus-Gen.git — repository linked from exact-v1 | claim:SF-2025-NEXUS-GEN | complete |
| SF-2025-SHORTERBETTER | RP-e3601e7d52483958 | standard | arXiv:2504.21370v1 | SRC-ARXIV@arXiv:2504.21370v1 | https://arxiv.org/html/2504.21370v1#S3 | https://arxiv.org/html/2504.21370v1#S4; https://arxiv.org/html/2504.21370v1#S5 | https://arxiv.org/html/2504.21370v1#S5.SS2; https://arxiv.org/html/2504.21370v1#S6 | Not Disclosed — exact-v1 does not identify a released implementation artifact | claim:SF-2025-SHORTERBETTER | complete |
| SF-2025-GALVATRON | RP-6bc469a12b841ae7 | deep | arXiv:2504.21411v1 | SRC-ARXIV@arXiv:2504.21411v1 | https://arxiv.org/html/2504.21411v1#S2; https://arxiv.org/html/2504.21411v1#S3 | https://arxiv.org/html/2504.21411v1#S4 | https://arxiv.org/html/2504.21411v1#S5 | https://github.com/PKU-DAIR/Hetu-Galvatron — repository linked from exact-v1 | claim:SF-2025-GALVATRON | complete |
| SF-2025-RWKV-X | RP-1af627e257ae741d | standard | arXiv:2504.21463v1 | SRC-ARXIV@arXiv:2504.21463v1 | https://arxiv.org/html/2504.21463v1#S3; https://arxiv.org/html/2504.21463v1#S3.SS2.SSS1 | https://arxiv.org/html/2504.21463v1#S4; https://arxiv.org/html/2504.21463v1#A2 | https://arxiv.org/html/2504.21463v1#S5; https://arxiv.org/html/2504.21463v1#A3 | https://github.com/howard-hou/RWKV-X — repository linked from exact-v1 | claim:SF-2025-RWKV-X | complete |
| SF-2025-RAGFORENSICS | RP-8b9076005e419bd4 | deep | arXiv:2504.21668v1 | SRC-ARXIV@arXiv:2504.21668v1 | https://arxiv.org/html/2504.21668v1#S3; https://arxiv.org/html/2504.21668v1#S4 | https://arxiv.org/html/2504.21668v1#S5 | https://arxiv.org/html/2504.21668v1#S6; https://arxiv.org/html/2504.21668v1#S7 | Not Disclosed — exact-v1 does not identify a released artifact | claim:SF-2025-RAGFORENSICS | complete |
| SF-2025-WEBTHINKER | RP-4d28dd4a6d4823ef | deep | arXiv:2504.21776v1 | SRC-ARXIV@arXiv:2504.21776v1 | https://arxiv.org/html/2504.21776v1#S3; https://arxiv.org/html/2504.21776v1#A1 | https://arxiv.org/html/2504.21776v1#S4; https://arxiv.org/html/2504.21776v1#S4.SS7 | https://arxiv.org/html/2504.21776v1#S5; https://arxiv.org/html/2504.21776v1#A3.SS4 | https://github.com/RUC-NLPIR/WebThinker — repository linked from exact-v1 | claim:SF-2025-WEBTHINKER | complete |
| SF-2025-SWE-SMITH | RP-0f6e83d3a721560f | deep | arXiv:2504.21798v1 | SRC-ARXIV@arXiv:2504.21798v1 | https://arxiv.org/html/2504.21798v1#S2; https://arxiv.org/html/2504.21798v1#A1; https://arxiv.org/html/2504.21798v1#A2 | https://arxiv.org/html/2504.21798v1#S3; https://arxiv.org/html/2504.21798v1#S4; https://arxiv.org/html/2504.21798v1#A6 | https://arxiv.org/html/2504.21798v1#S6; https://arxiv.org/html/2504.21798v1#A6.SS3.SSS3 | https://github.com/SWE-bench/SWE-smith — official repository identified by the manuscript/project | claim:SF-2025-SWE-SMITH | complete |
| SF-2025-DEEPSEEK-PROVER-V2 | RP-a394ed1d348c25ee | deep | arXiv:2504.21801v1 | SRC-ARXIV@arXiv:2504.21801v1 | https://arxiv.org/html/2504.21801v1#S2; https://arxiv.org/html/2504.21801v1#S2.SS1 | https://arxiv.org/html/2504.21801v1#S3; https://arxiv.org/html/2504.21801v1#S3.SS4 | https://arxiv.org/html/2504.21801v1#S4; https://arxiv.org/html/2504.21801v1#A3 | https://github.com/deepseek-ai/DeepSeek-Prover-V2 — official repository linked from exact-v1 | claim:SF-2025-DEEPSEEK-PROVER-V2 | complete |
| SF-2025-WHOWHEN | RP-78dcb9f50b93cecd | deep | arXiv:2505.00212v1 | SRC-ARXIV@arXiv:2505.00212v1 | https://arxiv.org/html/2505.00212v1#S2; https://arxiv.org/html/2505.00212v1#S3; https://arxiv.org/html/2505.00212v1#A2 | https://arxiv.org/html/2505.00212v1#S4; https://arxiv.org/html/2505.00212v1#A4 | https://arxiv.org/html/2505.00212v1#S6; https://arxiv.org/html/2505.00212v1#S7 | https://github.com/mingyin1/Agents_Failure_Attribution — repository linked from exact-v1 | claim:SF-2025-WHOWHEN | complete |
| SF-2025-ML-DRIFT | RP-423c3e08352153c9 | deep | arXiv:2505.00232v1 | SRC-ARXIV@arXiv:2505.00232v1 | https://arxiv.org/html/2505.00232v1#S3; https://arxiv.org/html/2505.00232v1#S3.SS7; https://arxiv.org/html/2505.00232v1#S3.SS8 | https://arxiv.org/html/2505.00232v1#S4; https://arxiv.org/html/2505.00232v1#S4.SS2 | https://arxiv.org/html/2505.00232v1#S5 | Not Disclosed — exact-v1 describes the framework but does not identify a frozen public ML Drift repository | claim:SF-2025-ML-DRIFT | complete |
| SF-2025-TRAJ-BOOTSTRAP | RP-4c25305c7c594b33 | deep | arXiv:2505.00234v1 | SRC-ARXIV@arXiv:2505.00234v1 | https://arxiv.org/html/2505.00234v1#S5; https://arxiv.org/html/2505.00234v1#A4 | https://arxiv.org/html/2505.00234v1#S6; https://arxiv.org/html/2505.00234v1#A5; https://arxiv.org/html/2505.00234v1#A6 | https://arxiv.org/html/2505.00234v1#S7; https://arxiv.org/html/2505.00234v1#A2 | Not Disclosed — exact-v1 does not identify a released trajectory database implementation | claim:SF-2025-TRAJ-BOOTSTRAP | complete |
| SF-2025-MUTEDRAG-AVAILABILITY | RP-a1627173a1b750f0 | deep | arXiv:2504.21680v1 | SRC-ARXIV@arXiv:2504.21680v1 | https://arxiv.org/html/2504.21680v1#S3 | https://arxiv.org/html/2504.21680v1#S4 | https://arxiv.org/html/2504.21680v1#S5; https://arxiv.org/html/2504.21680v1#S6 | Not Disclosed — exact-v1 does not identify a frozen public attack/evaluation artifact | claim:SF-2025-MUTEDRAG-AVAILABILITY | complete |
| SF-2025-LONGFUNCEVAL | RP-8d1efa245f152845 | standard | arXiv:2505.10570v1 | SRC-ARXIV@arXiv:2505.10570v1 | https://arxiv.org/html/2505.10570v1#S3; https://arxiv.org/html/2505.10570v1#S4 | https://arxiv.org/html/2505.10570v1#S5 | https://arxiv.org/html/2505.10570v1#S6; Not Disclosed — exact-v1 has no dedicated limitations section | https://github.com/ShishirPatil/gorilla/ — BFCL repository linked by the manuscript; paper-specific frozen exact-v1 dataset artifact Not Disclosed | claim:SF-2025-LONGFUNCEVAL | complete |
| SF-2025-VDDP | RP-1b977aaae526e795 | deep | arXiv:2504.21752v1 | SRC-ARXIV@arXiv:2504.21752v1 | https://arxiv.org/pdf/2504.21752v1 — §3 Problem Formulation; §4 Verifiable Distributed Discrete Laplace Mechanism; §5 Verifiable Randomized Response | https://arxiv.org/pdf/2504.21752v1 — §6 Evaluation | https://arxiv.org/pdf/2504.21752v1 — §8 Conclusion and Open Questions; Appendix C.5 | Artifact announced for publication at https://github.com/sjtu-ipads/VDDP ; no frozen exact-v1 artifact was available for this review | claim:SF-2025-VDDP | complete |
| SF-2025-CORAL-PROTOCOL | RP-f48e628783a2022f | standard | arXiv:2505.00749v1 | SRC-ARXIV@arXiv:2505.00749v1 | https://arxiv.org/html/2505.00749v1#S4; https://arxiv.org/html/2505.00749v1#S5 | https://arxiv.org/html/2505.00749v1#S6 | https://arxiv.org/html/2505.00749v1#S7; Not Disclosed — exact-v1 has no rigorous matched benchmark or dedicated limitations section | Not Disclosed — exact-v1 describes a planned/open infrastructure but does not identify a frozen implementation release used by this review | claim:SF-2025-CORAL-PROTOCOL | complete |

### Source Reviews

<!-- review:SF-2025-COSMOS-ADAPTATION:start --><!-- claim:SF-2025-COSMOS-ADAPTATION:start -->adaptation 不是先固定方法再计算账单；在 data/task/model/hardware contract 冻结后，可以先预测 fine-tuning、retrieval-ICL 及组合路径的 quality/cost，再由平台作有证据边界的选择。<!-- claim:SF-2025-COSMOS-ADAPTATION:end -->作者把策略选择形式化为性能与成本联合预测，比较 fine-tuning、retrieval-augmented ICL 及组合路径。该证据只支持论文的数据集、模型族、pricing/hardware 假设；预测器不拥有真实 deployment outcome，分布漂移、价格变化和训练失败都要求重新校准。<!-- review:SF-2025-COSMOS-ADAPTATION:end -->

<!-- review:SF-2025-ZIPLLM-STORAGE:start --><!-- claim:SF-2025-ZIPLLM-STORAGE:start -->物理去重不能合并逻辑模型身份：同源 checkpoint 可共享相同 tensor/chunk，并以 lossless delta materialize，但 base/delta lineage、hash、authorization 与独立恢复路径必须保持。<!-- claim:SF-2025-ZIPLLM-STORAGE:end -->论文从 Hugging Face model families 的 storage redundancy 出发，组合 tensor-level dedup、聚类和 BitX delta compression，并测量空间与恢复/serving throughput。它不证明任意 quantized/encrypted artifact 都可共享，也不允许 Registry 把物理共用误写成同一模型；聚类误判、base deletion 与恢复放大成为新 failure mode。<!-- review:SF-2025-ZIPLLM-STORAGE:end -->

<!-- review:SF-2025-BAYES-EVAL-CONFIDENCE:start --><!-- claim:SF-2025-BAYES-EVAL-CONFIDENCE:start -->有限 query 上的模型排序必须输出 posterior uncertainty，并把 prior、anchor model、query construction 和 judge 一起纳入 evaluation identity；高 posterior 不是跨分布正确性证明。<!-- claim:SF-2025-BAYES-EVAL-CONFIDENCE:end -->论文用 Bayesian inference 估计有限样本下相对成功率并与传统排名比较。结果支持在相同 query/judge contract 下表达排序不确定性；它不证明 prior 无偏、judge 正确或 posterior 能转移到新任务，anchor 与 query selection 会成为新的偏差来源。<!-- review:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- review:SF-2025-PHI4-REASONING:start --><!-- claim:SF-2025-PHI4-REASONING:start -->compact reasoning policy 可由高可教性 demonstration 扩展，再用 outcome-verifiable RL 增加探索；teacher/scaffold 和 token budget 仍是能力与成本边界。<!-- claim:SF-2025-PHI4-REASONING:end -->技术报告披露 seeds/data、SFT exploration/scaling 和 reasoning-plus RL，并在 reasoning/general/safety benchmark 上评估。它不披露完整训练 hardware、batch/concurrency 或生产 SLO，也不证明长 trace 忠实；旧的短响应模型在严格 latency 下仍合理。<!-- review:SF-2025-PHI4-REASONING:end -->

<!-- review:SF-2025-NEXUS-GEN:start --><!-- claim:SF-2025-NEXUS-GEN:start -->统一多模态模型仍需分开 representation identity 与 generation state：shared space 负责接口，prefilled AR 负责条件生成与 commit 顺序。<!-- claim:SF-2025-NEXUS-GEN:end -->论文给出 architecture、unified task representation、prefilled autoregression 与数据构建，并展示理解/生成/编辑案例。缺少系统性 matched benchmark、ablation 和 production latency，因此只支持可行性，不证明共享空间消除了 modality boundary 或独立 head 的必要性。<!-- review:SF-2025-NEXUS-GEN:end -->

<!-- review:SF-2025-SHORTERBETTER:start --><!-- claim:SF-2025-SHORTERBETTER:start -->reasoning 长度是受 workload 约束的可学习 stopping proposal，不是“越短越好”；上线仍需质量 guardrail、尾延迟和错误早停审计。<!-- claim:SF-2025-SHORTERBETTER:end -->作者搜索 sample optimal length 并训练模型在保持准确率时缩短输出，包含 out-of-domain 与 ablation。结果受选定数学任务、模型和 evaluator 限制；长度标签可能奖励跳步或格式捷径，旧的固定上限/自然 EOS 在低风险任务仍更简单。<!-- review:SF-2025-SHORTERBETTER:end -->

<!-- review:SF-2025-GALVATRON:start --><!-- claim:SF-2025-GALVATRON:start -->自动并行 planner 只拥有候选 plan；model shape、cluster topology、memory cap 和 collective profile 构成 plan identity，runtime telemetry 与 fallback 才拥有上线真值。<!-- claim:SF-2025-GALVATRON:end -->Galvatron 把 hybrid parallelism 搜索与执行 workflow 连接，并在作者 benchmark 下比较训练效率。它不证明 cost model 可跨拓扑、版本和动态故障稳定；profiling 成本、search explosion、错误 memory estimate 与 process-group churn 是新增 failure mode，固定静态 plan 在稳定 workload 下仍合理。<!-- review:SF-2025-GALVATRON:end -->

<!-- review:SF-2025-RWKV-X:start --><!-- claim:SF-2025-RWKV-X:start -->长上下文可以组合 recurrent linear state 与少量 sparse attention，但 active chunks、KV/state layout 和 continual-pretraining revision 必须共同定义运行时 identity。<!-- claim:SF-2025-RWKV-X:end -->论文给出 chunk sparse attention、KV 管理、复杂度和 continual pretraining，并测量长短 context 与效率。作者实验不证明 top-k retrieval 在所有任务保留关键信息；routing error、chunk metadata 与 hybrid kernel complexity 是代价，全 attention 在短上下文/高精度需求下仍成立。<!-- review:SF-2025-RWKV-X:end -->

<!-- review:SF-2025-RAGFORENSICS:start --><!-- claim:SF-2025-RAGFORENSICS:start -->RAG poisoning diagnosis 必须回溯 query、retrieved document、index revision 与 generated claim；traceback score 只拥有调查优先级，不拥有删除或定罪 authority。<!-- claim:SF-2025-RAGFORENSICS:end -->论文定义 threat model，组合可疑文本定位与实验评估，并测试 adaptive attacks。证据限于选定攻击、corpus、retriever 与 generator；false attribution、adaptive evasion 和昂贵 replay 要求人工/独立证据，简单 allowlist 和 immutable corpus 在高风险域仍适用。<!-- review:SF-2025-RAGFORENSICS:end -->

<!-- review:SF-2025-WEBTHINKER:start --><!-- claim:SF-2025-WEBTHINKER:start -->Deep Research 是 durable evidence workflow：搜索、读取、草稿与最终 claim 必须共享 source/version lineage，模型只拥有 proposal，工具结果和 verifier 拥有 evidence。<!-- claim:SF-2025-WEBTHINKER:end -->论文组合 Deep Web Explorer、think-search-draft 与 tool-use RL，在复杂问答和报告生成任务上比较并做 ablation。它不证明 web evidence 正确、引用完整或开放网络安全；搜索漂移、citation laundering、judge bias 与长轨迹成本仍需平台 gate。<!-- review:SF-2025-WEBTHINKER:end -->

<!-- review:SF-2025-SWE-SMITH:start --><!-- claim:SF-2025-SWE-SMITH:start -->可扩展 software-agent data 需要 repository commit、container、mutation、fail-to-pass test、issue 与 trajectory 的联合 identity；test oracle 而不是 LLM judge 拥有样本 admission。<!-- claim:SF-2025-SWE-SMITH:end -->论文构建 executable task factory 并用 128 个 repositories、50,137 instances 和下游训练测试其数据效用。结果不证明 synthetic bug 等同真实 issue 或跨语言泛化；container supply chain、test inadequacy、license 和 storage 成本是新增风险，真实 PR 仍是 calibration branch。<!-- review:SF-2025-SWE-SMITH:end -->

<!-- review:SF-2025-DEEPSEEK-PROVER-V2:start --><!-- claim:SF-2025-DEEPSEEK-PROVER-V2:start -->形式推理训练应把自然语言 sketch、subgoal proposal、Lean environment 与 executable verdict 分开；verifier 拥有 proof acceptance，policy 只拥有搜索 proposal。<!-- claim:SF-2025-DEEPSEEK-PROVER-V2:end -->论文用 recursive subgoal decomposition、synthetic cold start、expert iteration 和 RL 训练 prover，并在 MiniF2F/大学/组合题上评估。证据受 Lean version、sampling budget 和 benchmark formalization 限制；vacuous proof、benchmark bug、verifier exploitation 与高 rollout cost 不允许外推为通用 reasoning correctness。<!-- review:SF-2025-DEEPSEEK-PROVER-V2:end -->

<!-- review:SF-2025-WHOWHEN:start --><!-- claim:SF-2025-WHOWHEN:start -->多 Agent debugging 必须保存 agent、step、tool result 与 shared-state revision；LLM attribution 只产生 diagnostic evidence，不能直接成为 rollback 或责任裁决。<!-- claim:SF-2025-WHOWHEN:end -->论文标注 127 个 systems、184 个 failed tasks，比较三种定位流程与 context/cost sensitivity。结果显示全局 receptive field、局部 step precision 和 token cost 冲突；judge bias、shared cause、single-blame 标签与隐私限制因果解释。<!-- review:SF-2025-WHOWHEN:end -->

<!-- review:SF-2025-ML-DRIFT:start --><!-- claim:SF-2025-ML-DRIFT:start -->on-device runtime 要把逻辑 tensor 与物理 GPU object 分离，再由 device specialization、memory manager、fusion 和 prefill/decode plan materialize；模型语义不应绑定单一 GPU API。<!-- claim:SF-2025-ML-DRIFT:end -->论文跨 mobile、desktop/laptop 与 Apple Silicon 测试 diffusion/LLM，并给出 virtualization、coordinate translation、memory、fusion 和 KV layout。作者 benchmark 受设备、driver、model 与 precision 约束；跨设备实现复杂度、memory pressure 和 fallback coverage 是代价。<!-- review:SF-2025-ML-DRIFT:end -->

<!-- review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- claim:SF-2025-TRAJ-BOOTSTRAP:start -->成功轨迹可以成为下次决策的候选 memory，但 source task、policy version、outcome verifier、selection 与 deletion policy 必须随 exemplar 保存；成功一次不等于普适规则。<!-- claim:SF-2025-TRAJ-BOOTSTRAP:end -->论文从 agent 自己的成功 experience 构建数据库并做 database/exemplar selection，在 ALFWorld、Wordcraft、InterCode-SQL 评估。收益受 benchmark、initial examples、retriever 和 growing-context cost 限制；feedback loop 会固化偶然成功或污染，人工示例在高风险/低数据时仍合理。<!-- review:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- review:SF-2025-MUTEDRAG-AVAILABILITY:start --><!-- claim:SF-2025-MUTEDRAG-AVAILABILITY:start -->RAG 安全不能只测恶意内容是否被拒绝，还要把恶意检索内容诱发的正常请求拒绝视为 availability failure；retrieval hit、guardrail decision 与 final refusal 必须分开记录。<!-- claim:SF-2025-MUTEDRAG-AVAILABILITY:end -->论文给出攻击目标、黑盒/白盒路径和多数据集、多模型实验，并讨论若干防御。证据只支持论文所测 retriever、generator、guardrail 与攻击模板；它不证明任意安全过滤器都可被同样利用，也不证明内容过滤能无损修复。更严格 admission 会换来 false positive、延迟与维护成本；高风险域的 curated corpus/allowlist 仍是合理共存分支。<!-- review:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- review:SF-2025-LONGFUNCEVAL:start --><!-- claim:SF-2025-LONGFUNCEVAL:start -->长上下文 function-calling 评测必须分别改变 tool catalog size、tool-response length/answer position 与 multi-turn history，并冻结 schema、parser、model 与 evaluator；一个 long-context headline score 不能定位系统瓶颈。<!-- claim:SF-2025-LONGFUNCEVAL:end -->论文构造三类 workload 并比较模型在不同上下文压力下的 function-calling 成功。它证明的是冻结 benchmark contract 下的失效切片，不证明真实工具副作用、权限、网络故障或生产 SLO；扩充工具/历史会提高覆盖，也会增加 schema 检索、parser 与 evaluator 混杂。<!-- review:SF-2025-LONGFUNCEVAL:end -->

<!-- review:SF-2025-VDDP:start --><!-- claim:SF-2025-VDDP:start -->分布式差分隐私不能让 server 同时拥有随机机制执行与合规证明；mechanism revision、随机性来源、collusion model、proof/receipt 与 verifier identity 必须共同定义 privacy evidence。<!-- claim:SF-2025-VDDP:end -->论文形式化 client-server-verifier 设置，构建可验证离散 Laplace 与 randomized response，并测量密码学开销。它不消除 verifier/collusion 假设，也不证明部署中的 data pipeline、side channel 或 privacy budget composition 正确；证明成本、可信设置与系统复杂度是代价，受控环境下的 trusted aggregator 仍可能更简单。<!-- review:SF-2025-VDDP:end -->

<!-- review:SF-2025-CORAL-PROTOCOL:start --><!-- claim:SF-2025-CORAL-PROTOCOL:start -->Agent interoperability protocol 只拥有 message/discovery/coordination interface；authoritative workflow state、identity、authorization、payment settlement 与 safety commit 必须留在可审计 platform owner。<!-- claim:SF-2025-CORAL-PROTOCOL:end -->论文描述 ecosystem、component architecture、MCP/tool connection、server 与一个 real-world application narrative。它主要是 architecture/spec proposal，没有 matched benchmark、failure injection 或 production evidence；因此只能证明一种接口组合的可表达性，不能证明安全、互操作、性能或经济层成立。<!-- review:SF-2025-CORAL-PROTOCOL:end -->

## 4. Benchmark Contracts

Benchmark 数字只属于 exact-v1 的模型、数据、硬件和 evaluator；未披露字段保持 `Not Disclosed`，不从相邻工作补齐。Nexus-Gen 只有 qualitative case study，因此 Candidate Ledger 明确写 `Benchmark Claim=no`。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-COSMOS-ADAPTATION | 11 个 NLP classification tasks；fine-tuning、retrieval-augmented ICL 与组合策略 | Mistral-7B、Llama-2/3、Pythia 等论文 roster | NVIDIA A100 80GB（Appendix B） | Not Disclosed | task examples / retrieval context；token length Not Disclosed | class prediction | training/retrieval sweeps；统一 batch Not Disclosed | offline | quality/cost prediction error 与 strategy regret；无生产阈值 | task metric + measured/estimated cost |
| SF-2025-ZIPLLM-STORAGE | Hugging Face LLM family storage、dedup/compression 与 materialization/serving throughput | 多 base/fine-tuned LLM families | storage server / GPU setup 见 §5.1；具体 GPU 型号按表，正文不形成通用 hardware claim | lossless bytes；model precision follows artifacts | tensor/chunk corpus | materialized model bytes | storage pipeline | offline storage + load | reduction ratio、compression/decompression throughput；无生产 SLO | byte equality + throughput |
| SF-2025-BAYES-EVAL-CONFIDENCE | 有限 query 的 LLM pairwise/ranking evaluation | anchor 与 candidate LLM roster 见 §3 | Not Disclosed | Not Disclosed | constructed query set | model answers/judgments | limited samples | offline | posterior ranking confidence；无 production threshold | Bayesian posterior + comparison baselines |
| SF-2025-PHI4-REASONING | math/code/science reasoning、general 与 safety evaluation | Phi-4-reasoning、Phi-4-reasoning-plus 与 baseline models | Not Disclosed | Not Disclosed | 最大 context 32K；per-task prompt length Not Disclosed | long reasoning response | Not Disclosed | offline sampling | accuracy/pass metrics；无 latency SLO | benchmark scorers、best-of-5 / distribution analysis |
| SF-2025-SHORTERBETTER | 数学 reasoning 的 sample-optimal-length search 与 OOD evaluation | Qwen2.5-based reasoning models / paper roster | Not Disclosed | Not Disclosed | problem prompt | variable CoT length | Not Disclosed | offline | accuracy 与 generated token length | task exact-answer scorer |
| SF-2025-GALVATRON | hybrid-parallel plan search 与 foundation-model training | Transformer family configs in §4 | multi-GPU clusters in §4; exact topology bound to each experiment | Not Disclosed | model shapes / sequence configs | training step | plan-specific | distributed workers | throughput/memory；无 production SLO | runtime profiler + measured training throughput |
| SF-2025-RWKV-X | long-context LM quality、efficiency 与 ablations | RWKV-X sizes and Transformer/RWKV baselines | training/evaluation hardware in Appendix A/B | Not Disclosed | short context to 1M-token tests per paper | LM token prediction | Not Disclosed | offline | perplexity/accuracy/throughput/memory | task metrics + runtime measurement |
| SF-2025-RAGFORENSICS | poisoned RAG traceback under baseline/adaptive attacks | retriever/generator combinations in §5.1 | Not Disclosed | Not Disclosed | query + corpus documents | generated answer + suspect ranking | Not Disclosed | offline | traceback metrics and attack success；无 production SLO | known injected poison ground truth |
| SF-2025-WEBTHINKER | complex reasoning + scientific report generation with web tools | QwQ/DeepSeek-R1-based LRMs and baselines | Not Disclosed | Not Disclosed | web evidence and long prompts；length by task | answer/report | Not Disclosed | tool loop | task score/report judge；无 production SLO | task scorer + model-based report evaluation |
| SF-2025-SWE-SMITH | 50,137 executable SWE tasks / 128 repos；RFT on 5,016 trajectories | Qwen2.5-Coder 7B/32B | 2–8×H100 80GB | Not Disclosed | max context 32,768 | agent patch trajectory | training setup in Appendix F | offline agent runs | SWE-bench Verified Pass@1 | repository tests / harness |
| SF-2025-DEEPSEEK-PROVER-V2 | Lean theorem proving、MiniF2F/ProverBench/combinatorial tasks | DeepSeek-Prover-V2 7B/671B | Not Disclosed | Not Disclosed | SFT 16,384；GRPO max 32,768 | Lean proof | GRPO 256 prompts ×32 proofs/iteration | offline sampling | Pass@k / proof success；无 latency SLO | Lean 4.9.0-rc2 verifier |
| SF-2025-WHOWHEN | 127 multi-agent systems、184 failed tasks、step/agent attribution | GPT-4o and open/reasoning judge roster | Not Disclosed | Not Disclosed | full or partial trace | agent + decisive step | 184 annotated failures | offline | agent/step accuracy、tolerance、token cost | three-expert annotation consensus |
| SF-2025-ML-DRIFT | large diffusion/LLM inference across mobile、desktop/laptop、Apple Silicon GPUs | diffusion and LLM roster in §4 | multiple mobile GPUs、desktop/laptop GPUs、Apple Silicon | model/device-specific；not normalized | model/input-specific | image/audio/text generation | device-specific | single-device inference | latency/memory/throughput；无 production threshold | runtime timing + output checks |
| SF-2025-TRAJ-BOOTSTRAP | ALFWorld、Wordcraft、InterCode-SQL sequential decision tasks | LLM agent backbones in §6.1 | Appendix F computational resources | Not Disclosed | task observation/action history + retrieved exemplars | agent action trajectory | population/retrieval configs | sequential episodes | task success and quality metrics | environment/task evaluator |
| SF-2025-MUTEDRAG-AVAILABILITY | RAG denial-of-service attacks induced through safety guardrails across three datasets | 8 LLMs / paper guardrail and RAG configurations | Not Disclosed | Not Disclosed | query + retrieved adversarial text | answer or guardrail refusal | attack/evaluation batches by §4 | offline | attack success / refusal availability metrics；无 production SLO | known attack condition + task/refusal outcomes |
| SF-2025-LONGFUNCEVAL | large tool catalog、long tool responses/answer position、long multi-turn function calling | long-context model roster in §4 | Not Disclosed | Not Disclosed | three independently varied long-context workloads | function call / final answer | benchmark splits in §4 | offline | function-call and answer correctness；无 production latency SLO | BFCL-derived benchmark scorer / task oracle |
| SF-2025-VDDP | verifiable distributed discrete-Laplace and randomized-response mechanisms | cryptographic protocol implementations | Intel Xeon Platinum 8358, 32 cores, 231 GB RAM | integer/cryptographic protocol arithmetic | client records / protocol parameters | DP aggregate or randomized response + proof | microbenchmark configs in §6 | client-server-verifier protocol | proof verification time、communication and mechanism overhead；无 production SLO | cryptographic verifier + mechanism correctness checks |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2025-COSMOS-ADAPTATION | forced_review;potential_books_delta | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-COSMOS-ADAPTATION |
| SF-2025-ZIPLLM-STORAGE | score_7_9;forced_review;potential_books_delta | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-ZIPLLM-STORAGE |
| SF-2025-BAYES-EVAL-CONFIDENCE | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE |
| SF-2025-GALVATRON | score_7_9;forced_review;potential_books_delta | selected | DA-TRAIN-PLAN-CONTROL | — | 自动 parallel-plan control 同时改变 planner、runtime 与 telemetry ownership。 | analysis:DA-TRAIN-PLAN-CONTROL |
| SF-2025-RAGFORENSICS | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-RAGFORENSICS |
| SF-2025-WEBTHINKER | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-WEBTHINKER |
| SF-2025-SWE-SMITH | score_7_9 | selected | DA-EXECUTABLE-DATA | — | executable data factory 把 data identity、environment 与 verifier 串成一条长期链。 | analysis:DA-EXECUTABLE-DATA |
| SF-2025-DEEPSEEK-PROVER-V2 | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-DEEPSEEK-PROVER-V2 |
| SF-2025-WHOWHEN | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-WHOWHEN |
| SF-2025-ML-DRIFT | score_7_9 | selected | DA-DEVICE-RUNTIME | — | 端侧 tensor virtualization 最清楚暴露模型语义与 device object 的解耦。 | analysis:DA-DEVICE-RUNTIME |
| SF-2025-TRAJ-BOOTSTRAP | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-TRAJ-BOOTSTRAP |
| SF-2025-MUTEDRAG-AVAILABILITY | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY |
| SF-2025-VDDP | score_7_9 | not_selected | — | — | 已完成 route-matched Review 与 Books 比较；长叙事容量优先给本日报三条跨边界控制链，不降低该 family 的证据状态。 | analysis-decision:SF-2025-VDDP |

<!-- analysis:DA-TRAIN-PLAN-CONTROL:start -->### Deep Analysis 1 — 从手工并行组合到可校准 plan control

静态 DP/TP/PP 组合在模型 shape 和集群稳定时最容易验证，也能复用 process group。约束改变后，组合空间、memory cap 和 topology 使人工枚举昂贵；Galvatron 增加 profile/cost-model/search planner。planner 只提出候选，runtime telemetry 才能验证 predicted throughput/memory；版本或 topology 漂移时回退已验证静态 plan。收益是自动探索，代价是 profiling、search、错误模型和 plan churn。<!-- analysis:DA-TRAIN-PLAN-CONTROL:end -->

<!-- analysis-decision:SF-2025-COSMOS-ADAPTATION:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-COSMOS-ADAPTATION:end -->

<!-- analysis-decision:SF-2025-ZIPLLM-STORAGE:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-ZIPLLM-STORAGE:end -->

<!-- analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- analysis-decision:SF-2025-RAGFORENSICS:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-RAGFORENSICS:end -->

<!-- analysis-decision:SF-2025-WEBTHINKER:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-WEBTHINKER:end -->

<!-- analysis-decision:SF-2025-DEEPSEEK-PROVER-V2:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-DEEPSEEK-PROVER-V2:end -->

<!-- analysis-decision:SF-2025-WHOWHEN:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-WHOWHEN:end -->

<!-- analysis-decision:SF-2025-TRAJ-BOOTSTRAP:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- analysis-decision:SF-2025-VDDP:start -->该 family 已完成全文审计；其长期命题由 Source Review 与 Books Comparison 承载，本日报不再重复一段论文摘要式 Deep Analysis。<!-- analysis-decision:SF-2025-VDDP:end -->

<!-- analysis:DA-EXECUTABLE-DATA:start -->### Deep Analysis 2 — 从文本样本到 executable data factory

真实 PR 任务可信但稀缺，纯文本合成便宜却无法证明 patch 可执行。SWE-smith 把 repository commit、container、mutation、fail-to-pass tests、issue 与 trajectory 合成一个样本 identity，并让 test oracle 拥有 admission。它扩大规模，也引入 test inadequacy、synthetic distribution、license 和 container supply-chain 风险；真实 PR 仍是校准集。<!-- analysis:DA-EXECUTABLE-DATA:end -->

<!-- analysis:DA-DEVICE-RUNTIME:start -->### Deep Analysis 3 — 从单一 GPU backend 到逻辑 tensor virtualization

固定 backend 直接把 tensor 映射到 device object，简单但把模型图绑定硬件 API。端侧设备、memory 上限和 prefill/decode 差异迫使 runtime 分离 logical tensor 与 physical object，再以 coordinate translation、device specialization、fusion 和 KV layout materialize。收益是跨 GPU 覆盖，代价是 backend matrix、fallback 缺口和 device-specific correctness/性能验证。<!-- analysis:DA-DEVICE-RUNTIME:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-COSMOS-ADAPTATION | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1; books/part-04-training-system/29-sft.md#L1 | existing:SF-2025-COSMOS-ADAPTATION | delta:SF-2025-COSMOS-ADAPTATION | Alternative Branch | Integrate | books-review:SF-2025-COSMOS-ADAPTATION |
| SF-2025-ZIPLLM-STORAGE | PLATFORM-MODEL-REGISTRY | books/part-06-ai-infrastructure/59-model-registry.md#L105 | books/part-06-ai-infrastructure/58-kubeflow.md#L1; books/part-06-ai-infrastructure/60-training-operator.md#L1 | existing:SF-2025-ZIPLLM-STORAGE | delta:SF-2025-ZIPLLM-STORAGE | Layering / Dependency | Integrate | books-review:SF-2025-ZIPLLM-STORAGE |
| SF-2025-BAYES-EVAL-CONFIDENCE | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1040 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1; books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2025-BAYES-EVAL-CONFIDENCE | delta:SF-2025-BAYES-EVAL-CONFIDENCE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-BAYES-EVAL-CONFIDENCE |
| SF-2025-PHI4-REASONING | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-04-training-system/33-grpo.md#L1 | existing:SF-2025-PHI4-REASONING | delta:SF-2025-PHI4-REASONING | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-PHI4-REASONING |
| SF-2025-NEXUS-GEN | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L160 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1; books/part-02-model/18-decoder-only.md#L1 | existing:SF-2025-NEXUS-GEN | delta:SF-2025-NEXUS-GEN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-NEXUS-GEN |
| SF-2025-SHORTERBETTER | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L160 | books/part-02-model/20-sampling.md#L180; books/part-04-training-system/33-grpo.md#L1020 | existing:SF-2025-SHORTERBETTER | delta:SF-2025-SHORTERBETTER | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-SHORTERBETTER |
| SF-2025-GALVATRON | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L610 | books/part-04-training-system/37-tensor-parallel.md#L1; books/part-04-training-system/38-pipeline-parallel.md#L1 | existing:SF-2025-GALVATRON | delta:SF-2025-GALVATRON | Direct Evolution | Integrate | books-review:SF-2025-GALVATRON |
| SF-2025-RWKV-X | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L1 | books/part-02-model/15-multi-head-attention.md#L1; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | existing:SF-2025-RWKV-X | delta:SF-2025-RWKV-X | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-RWKV-X |
| SF-2025-RAGFORENSICS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2025-RAGFORENSICS | delta:SF-2025-RAGFORENSICS | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-RAGFORENSICS |
| SF-2025-WEBTHINKER | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L280 | existing:SF-2025-WEBTHINKER | delta:SF-2025-WEBTHINKER | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-WEBTHINKER |
| SF-2025-SWE-SMITH | TRAIN-DATA | books/part-04-training-system/27-data.md#L280 | books/part-06-ai-infrastructure/66-evaluation-system.md#L790; books/part-07-agent/81-workflow.md#L1 | existing:SF-2025-SWE-SMITH | delta:SF-2025-SWE-SMITH | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-SWE-SMITH |
| SF-2025-DEEPSEEK-PROVER-V2 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L940 | books/part-04-training-system/29-sft.md#L1; books/part-06-ai-infrastructure/66-evaluation-system.md#L750 | existing:SF-2025-DEEPSEEK-PROVER-V2 | delta:SF-2025-DEEPSEEK-PROVER-V2 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-DEEPSEEK-PROVER-V2 |
| SF-2025-WHOWHEN | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L180 | books/part-06-ai-infrastructure/67-monitoring.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2025-WHOWHEN | delta:SF-2025-WHOWHEN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-WHOWHEN |
| SF-2025-ML-DRIFT | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L20 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1; books/part-05-inference-system/54-gpu-memory.md#L1 | existing:SF-2025-ML-DRIFT | delta:SF-2025-ML-DRIFT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-ML-DRIFT |
| SF-2025-TRAJ-BOOTSTRAP | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-07-agent/81-workflow.md#L1 | existing:SF-2025-TRAJ-BOOTSTRAP | delta:SF-2025-TRAJ-BOOTSTRAP | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-TRAJ-BOOTSTRAP |
| SF-2025-MUTEDRAG-AVAILABILITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-07-agent/76-rag.md#L1; books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2025-MUTEDRAG-AVAILABILITY | delta:SF-2025-MUTEDRAG-AVAILABILITY | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-MUTEDRAG-AVAILABILITY |
| SF-2025-LONGFUNCEVAL | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-07-agent/78-tool-calling.md#L1; books/part-07-agent/75-context.md#L1 | existing:SF-2025-LONGFUNCEVAL | delta:SF-2025-LONGFUNCEVAL | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-LONGFUNCEVAL |
| SF-2025-VDDP | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-04-training-system/27-data.md#L1; books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2025-VDDP | delta:SF-2025-VDDP | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-VDDP |
| SF-2025-CORAL-PROTOCOL | AGENT-MCP | books/part-07-agent/83-mcp.md#L1 | books/part-07-agent/82-multi-agent.md#L1; books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2025-CORAL-PROTOCOL | delta:SF-2025-CORAL-PROTOCOL | Explanatory Analogy | No Change — Existing Coverage | books-review:SF-2025-CORAL-PROTOCOL |

三项 `Integrate` 的写回收据位于 `_sources/daily-v2.1-replay-202505/20250501/books-writeback-queue.md`。root 已完成正文写回；随后由未参与本日报主要写作或共享 Books 写回的 reviewer 完成 owner/adjacent 语义复核，Books Gate 已通过。

<!-- books-review:SF-2025-COSMOS-ADAPTATION:start --><!-- existing:SF-2025-COSMOS-ADAPTATION:start -->成本章已有训练、推理和资源账本，但没有把 fine-tuning 与 retrieval-augmented ICL 写成受预算约束的 adaptation portfolio。<!-- existing:SF-2025-COSMOS-ADAPTATION:end --><!-- delta:SF-2025-COSMOS-ADAPTATION:start -->把 quality/cost predictor 只作为 strategy proposal，最终选择仍由冻结 workload、数据访问、hardware price 与 evaluation gate 决定。<!-- delta:SF-2025-COSMOS-ADAPTATION:end -->演进关系为 Alternative Branch；目标 `PLATFORM-COST` 与相邻章节已读。当前决定：`Integrate`。<!-- books-review:SF-2025-COSMOS-ADAPTATION:end -->

<!-- books-review:SF-2025-ZIPLLM-STORAGE:start --><!-- existing:SF-2025-ZIPLLM-STORAGE:start -->Registry 已区分 metadata/index 与 artifact store，但尚未说明大量同源 checkpoint 的物理存储可以怎样共享而不破坏 artifact identity。<!-- existing:SF-2025-ZIPLLM-STORAGE:end --><!-- delta:SF-2025-ZIPLLM-STORAGE:start -->在 artifact-store 一侧增加 tensor-level dedup、family clustering 与 lossless delta compression；Registry 仍保存逻辑模型、base/delta lineage、完整性 hash 与可独立 materialize 的部署引用。<!-- delta:SF-2025-ZIPLLM-STORAGE:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-MODEL-REGISTRY` 与相邻章节已读。当前决定：`Integrate`。<!-- books-review:SF-2025-ZIPLLM-STORAGE:end -->

<!-- books-review:SF-2025-BAYES-EVAL-CONFIDENCE:start --><!-- existing:SF-2025-BAYES-EVAL-CONFIDENCE:start -->Evaluation 章已把 point estimate、confidence/calibration、相关误差与 abstention 分开，并要求冻结 evaluator identity。<!-- existing:SF-2025-BAYES-EVAL-CONFIDENCE:end --><!-- delta:SF-2025-BAYES-EVAL-CONFIDENCE:start -->有限样本 Bayesian ranking 是该既有命题的一种实现：posterior 只属于给定 prior、anchor、query set 与 judge，不是模型的内在置信度。<!-- delta:SF-2025-BAYES-EVAL-CONFIDENCE:end -->演进关系为 Principle Reuse；目标 `PLATFORM-EVALUATION-SYSTEM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- books-review:SF-2025-PHI4-REASONING:start --><!-- existing:SF-2025-PHI4-REASONING:start -->SFT/GRPO 章节已经把 teacher demonstrations、cold start、outcome-verifiable RL 与长输出代价写成条件分支。<!-- existing:SF-2025-PHI4-REASONING:end --><!-- delta:SF-2025-PHI4-REASONING:start -->Phi-4-reasoning 是 compact model 上 teachable-prompt SFT 加短程 RL 的受限实例，不新增独立 owner。<!-- delta:SF-2025-PHI4-REASONING:end -->演进关系为 Direct Evolution；目标 `TRAIN-SFT` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-PHI4-REASONING:end -->

<!-- books-review:SF-2025-NEXUS-GEN:start --><!-- existing:SF-2025-NEXUS-GEN:start -->多模态章节已区分 shared semantic interface 与独立 generation head，并把 AR factorization 放在生成范式 owner。<!-- existing:SF-2025-NEXUS-GEN:end --><!-- delta:SF-2025-NEXUS-GEN:start -->shared embedding、task token 与 prefilled autoregression 是该分层的实现案例；case study 不足以宣称统一表示优于所有双塔。<!-- delta:SF-2025-NEXUS-GEN:end -->演进关系为 Layering / Dependency；目标 `MULTIMODAL-REPRESENTATION` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-NEXUS-GEN:end -->

<!-- books-review:SF-2025-SHORTERBETTER:start --><!-- existing:SF-2025-SHORTERBETTER:start -->调度章已把 reasoning token budget、stopping policy 与 expected value per token 作为 request-level control state。<!-- existing:SF-2025-SHORTERBETTER:end --><!-- delta:SF-2025-SHORTERBETTER:start -->sample-optimal-length 自训练只提供一种长度 proposal；scheduler 仍拥有上线预算、SLO 与 harmful early-stop audit。<!-- delta:SF-2025-SHORTERBETTER:end -->演进关系为 Direct Evolution；目标 `INFER-SCHEDULING` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SHORTERBETTER:end -->

<!-- books-review:SF-2025-GALVATRON:start --><!-- existing:SF-2025-GALVATRON:start -->分布式训练章已有 cost model、collective 与 static/dynamic plan 边界，但自动 plan search 的状态 owner、校准与失效回退尚未形成完整链条。<!-- existing:SF-2025-GALVATRON:end --><!-- delta:SF-2025-GALVATRON:start -->增加 planner 分支：冻结 model/hardware/memory/communication profile，搜索 DP/TP/PP/sharding 组合；runtime 执行并用真实 telemetry 校准，预测失真时回到已验证静态 plan。<!-- delta:SF-2025-GALVATRON:end -->演进关系为 Direct Evolution；目标 `TRAIN-DISTRIBUTED-TRAINING` 与相邻章节已读。当前决定：`Integrate`。<!-- books-review:SF-2025-GALVATRON:end -->

<!-- books-review:SF-2025-RWKV-X:start --><!-- existing:SF-2025-RWKV-X:start -->Long-context 章节已把 recurrent/linear state 与 sparse attention 作为替代分支，并要求保留 cache/state identity。<!-- existing:SF-2025-RWKV-X:end --><!-- delta:SF-2025-RWKV-X:start -->top-k chunk sparse attention 加 RWKV block 是该分支的组合实例，不改变 owner。<!-- delta:SF-2025-RWKV-X:end -->演进关系为 Alternative Branch；目标 `MODEL-LONG-CONTEXT` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-RWKV-X:end -->

<!-- books-review:SF-2025-RAGFORENSICS:start --><!-- existing:SF-2025-RAGFORENSICS:start -->Security/RAG 章节已要求 document provenance、retrieval trace、attack surface 与 quarantine 分离。<!-- existing:SF-2025-RAGFORENSICS:end --><!-- delta:SF-2025-RAGFORENSICS:start -->RAGForensics 的 traceback 是已有 provenance contract 的诊断实现，不把相似度归因升级为因果证明。<!-- delta:SF-2025-RAGFORENSICS:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-RAGFORENSICS:end -->

<!-- books-review:SF-2025-WEBTHINKER:start --><!-- existing:SF-2025-WEBTHINKER:start -->Workflow/RAG 章节已拥有 plan-search-draft、evidence provenance、tool receipt 与 report-level verification。<!-- existing:SF-2025-WEBTHINKER:end --><!-- delta:SF-2025-WEBTHINKER:start -->WebThinker 的 think-search-draft 与 RL 是该工作流的受限实例，不新增可绕过证据 gate 的自治 authority。<!-- delta:SF-2025-WEBTHINKER:end -->演进关系为 Direct Evolution；目标 `AGENT-WORKFLOW` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-WEBTHINKER:end -->

<!-- books-review:SF-2025-SWE-SMITH:start --><!-- existing:SF-2025-SWE-SMITH:start -->Data 章已把 executable mutation、environment/test oracle、trajectory 与 lineage 作为 agentic data factory。<!-- existing:SF-2025-SWE-SMITH:end --><!-- delta:SF-2025-SWE-SMITH:start -->SWE-smith 已被该命题承载；本轮只重建 exact-day provenance，不重复追加论文清单。<!-- delta:SF-2025-SWE-SMITH:end -->演进关系为 Direct Evolution；目标 `TRAIN-DATA` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SWE-SMITH:end -->

<!-- books-review:SF-2025-DEEPSEEK-PROVER-V2:start --><!-- existing:SF-2025-DEEPSEEK-PROVER-V2:start -->GRPO/Evaluation 已把 subgoal boundary、cold start、outcome verifier 与 reward hacking 边界写入主线。<!-- existing:SF-2025-DEEPSEEK-PROVER-V2:end --><!-- delta:SF-2025-DEEPSEEK-PROVER-V2:start -->Lean proof checking 是 executable verifier 分支；自然语言 sketch 和 recursive subgoal search 不取得 truth authority。<!-- delta:SF-2025-DEEPSEEK-PROVER-V2:end -->演进关系为 Direct Evolution；目标 `TRAIN-GRPO` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-DEEPSEEK-PROVER-V2:end -->

<!-- books-review:SF-2025-WHOWHEN:start --><!-- existing:SF-2025-WHOWHEN:start -->Trace 章已区分 immutable event、step/agent attribution、diagnostic confidence 与因果 authority。<!-- existing:SF-2025-WHOWHEN:end --><!-- delta:SF-2025-WHOWHEN:start -->Who&When 的 all-at-once、stepwise 与 binary-search judge 已作为 failure attribution 边界被承载。<!-- delta:SF-2025-WHOWHEN:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-TRACE` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-WHOWHEN:end -->

<!-- books-review:SF-2025-ML-DRIFT:start --><!-- existing:SF-2025-ML-DRIFT:start -->Execution 章已把 logical tensor、device-specific layout、memory placement、fusion 与 prefill/decode 分支纳入 plan identity。<!-- existing:SF-2025-ML-DRIFT:end --><!-- delta:SF-2025-ML-DRIFT:start -->ML Drift 的 tensor virtualization、coordinate translation 与 stage-aware optimization 是同一机制在 heterogeneous on-device GPU 上的实现。<!-- delta:SF-2025-ML-DRIFT:end -->演进关系为 Layering / Dependency；目标 `INFER-TENSORRT-LLM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-ML-DRIFT:end -->

<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- existing:SF-2025-TRAJ-BOOTSTRAP:start -->Memory 章已把 successful trajectory 转换为可撤销 derived memory，并要求 provenance、selection、forgetting 与 held-out evaluation。<!-- existing:SF-2025-TRAJ-BOOTSTRAP:end --><!-- delta:SF-2025-TRAJ-BOOTSTRAP:start -->Traj-Bootstrap 的 database/exemplar selection 是已有 derived-memory admission 的实例。<!-- delta:SF-2025-TRAJ-BOOTSTRAP:end -->演进关系为 Direct Evolution；目标 `AGENT-MEMORY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- books-review:SF-2025-MUTEDRAG-AVAILABILITY:start --><!-- existing:SF-2025-MUTEDRAG-AVAILABILITY:start -->Security 与 RAG 章节已把 retrieved content 视为不可信输入，并要求 provenance、admission、policy decision 与 availability outcome 可追踪。<!-- existing:SF-2025-MUTEDRAG-AVAILABILITY:end --><!-- delta:SF-2025-MUTEDRAG-AVAILABILITY:start -->MutedRAG 进一步证明 safety guardrail 本身可以被对抗性 retrieved text 触发而成为 availability attack surface；这强化既有命题，但不改变 owner。<!-- delta:SF-2025-MUTEDRAG-AVAILABILITY:end -->演进关系为 Direct Evolution；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- books-review:SF-2025-LONGFUNCEVAL:start --><!-- existing:SF-2025-LONGFUNCEVAL:start -->Evaluation 章已要求冻结 tool/schema、上下文构成、state evolution、evaluator 与执行结果，且不把单一聚合分数当成能力本体。<!-- existing:SF-2025-LONGFUNCEVAL:end --><!-- delta:SF-2025-LONGFUNCEVAL:start -->LongFuncEval 把长上下文 function calling 拆成大工具目录、长工具返回与多轮历史三种压力，是既有 evaluation contract 的具体化。<!-- delta:SF-2025-LONGFUNCEVAL:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-EVALUATION-SYSTEM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-LONGFUNCEVAL:end -->

<!-- books-review:SF-2025-VDDP:start --><!-- existing:SF-2025-VDDP:start -->Security 章已要求 privacy claim 绑定可执行 policy、可信边界、receipt 与独立验证，而不是由执行方自我声明。<!-- existing:SF-2025-VDDP:end --><!-- delta:SF-2025-VDDP:start -->VDDP 用 client/server/verifier 分权、可验证随机机制与密码学证明具体化该 contract；新增的是机制证据，不是新的知识 owner。<!-- delta:SF-2025-VDDP:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-VDDP:end -->

<!-- books-review:SF-2025-CORAL-PROTOCOL:start --><!-- existing:SF-2025-CORAL-PROTOCOL:start -->MCP/Multi-Agent 章节已明确连接协议只标准化 discovery、message 与 tool/resource interface，不授予信任、workflow commit 或业务授权。<!-- existing:SF-2025-CORAL-PROTOCOL:end --><!-- delta:SF-2025-CORAL-PROTOCOL:start -->Coral 把 agent、MCP server、coordination server、team formation 与跨域通信画成一套 architecture；其接口分层印证既有边界，但没有足够实证改变长期结论。<!-- delta:SF-2025-CORAL-PROTOCOL:end -->演进关系为 Explanatory Analogy；目标 `AGENT-MCP` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-CORAL-PROTOCOL:end -->

## 7. Semantic Audit

首次冻结后的 author pass 发现 MutedRAG、LongFuncEval、VDDP 与 Coral Protocol 四个 false negative，已提升并完成 exact-v1 Review。随后由未参与本日报主要写作或共享 Books 写回的 reviewer 独立复核：重新计算 853 raw、217 Core、122 keyword-routed、19 retained 与 834 closures；核对 19/19 primary packet、99 个 HTML section locator、Score/Review route 和全部 selection-eligible family；并重读 Ch70/59/36 的写回段及其相邻章节。复核发现 Books Comparison 中三处旧文件名，修正后不存在未解决 finding。`2505.10571` 也被作为高风险 closure 重开核对：其独立调用实验不建立跨请求 hidden-state persistence，不能把接口没有携带的状态反推为模型应当持有的持久状态，因此维持 pre-denominator closure。

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20250501-COVERAGE | fresh-context:may03_daily_cross_review_20260831 | coverage | coverage:SRC-ARXIV:20250501 | — | 独立复算 853 raw、217 Core + 122 keyword = 339 registered routes、19 retained 与 834 closures；确认四个已修复 false negative，且高风险 closure 复核未发现第五个应提升 family。 | passed |
| SA-20250501-EVIDENCE | fresh-context:may03_daily_cross_review_20260831 | evidence | review:SF-2025-COSMOS-ADAPTATION; review:SF-2025-ZIPLLM-STORAGE; review:SF-2025-BAYES-EVAL-CONFIDENCE; review:SF-2025-PHI4-REASONING; review:SF-2025-NEXUS-GEN; review:SF-2025-SHORTERBETTER; review:SF-2025-GALVATRON; review:SF-2025-RWKV-X; review:SF-2025-RAGFORENSICS; review:SF-2025-WEBTHINKER; review:SF-2025-SWE-SMITH; review:SF-2025-DEEPSEEK-PROVER-V2; review:SF-2025-WHOWHEN; review:SF-2025-ML-DRIFT; review:SF-2025-TRAJ-BOOTSTRAP; review:SF-2025-MUTEDRAG-AVAILABILITY; review:SF-2025-LONGFUNCEVAL; review:SF-2025-VDDP; review:SF-2025-CORAL-PROTOCOL | — | 独立核对 19/19 exact-v1 packet、版本、99 个 HTML locator、PDF-only VDDP 边界、claim boundary、评分总和与 route-matched Review，未发现未解决证据 finding。 | passed |
| SA-20250501-SELECTION | fresh-context:may03_daily_cross_review_20260831 | deep_analysis_selection | validator:deep-analysis-selection-v1; analysis:DA-TRAIN-PLAN-CONTROL; analysis:DA-EXECUTABLE-DATA; analysis:DA-DEVICE-RUNTIME | — | 独立复算 13 个 selection-eligible family；3 个 selected、10 个 not-selected 均有可追溯 disposition，且未用三项叙事上限替代其余 family 的 Source Review。 | passed |
| SA-20250501-BOOKS | fresh-context:may03_daily_cross_review_20260831 | books | validator:books-comparison-v1; books-review:SF-2025-COSMOS-ADAPTATION; books-review:SF-2025-ZIPLLM-STORAGE; books-review:SF-2025-BAYES-EVAL-CONFIDENCE; books-review:SF-2025-PHI4-REASONING; books-review:SF-2025-NEXUS-GEN; books-review:SF-2025-SHORTERBETTER; books-review:SF-2025-GALVATRON; books-review:SF-2025-RWKV-X; books-review:SF-2025-RAGFORENSICS; books-review:SF-2025-WEBTHINKER; books-review:SF-2025-SWE-SMITH; books-review:SF-2025-DEEPSEEK-PROVER-V2; books-review:SF-2025-WHOWHEN; books-review:SF-2025-ML-DRIFT; books-review:SF-2025-TRAJ-BOOTSTRAP; books-review:SF-2025-MUTEDRAG-AVAILABILITY; books-review:SF-2025-LONGFUNCEVAL; books-review:SF-2025-VDDP; books-review:SF-2025-CORAL-PROTOCOL | — | 复核发现并修正三处失效 adjacent ref：`15-multi-head-attention.md`、`78-tool-calling.md` 与 `71-multi-tenant.md`；COSMOS、ZipLLM、Galvatron 正文均保留旧路径、约束变化、state/authority、trade-off、failure/fallback 与 evidence boundary，owner/adjacent 交接无未解决 finding。 | passed |

## 8. Ignored Noise

834 个 pre-denominator closures 已保存在 `screening-ledger.json`，每项包含 identity、first-public timestamp、categories、route、family-specific closure reason 与 false-negative audit result。主要类别为非注册学科、垂直领域任务、secondary survey、局部 benchmark/dataset，以及没有改变 state/data/control ownership 的单点模型改进；这些项目没有被误写成低分候选，也没有被冒充全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合时使用 19 个 Source Family ID 和真实 v1 date，不能继承 W18 `/30` 或重复计分。
2. 后续若 COSMOS 的 predictor、ZipLLM 的物理共享或 Galvatron 的 planner 出现新 revision，应继续区分 proposal 与 decision truth，并保留直接 measurement、完整 checkpoint 与静态 plan 三条 fallback。

## 10. Repository Changes

- 新建 2025-05-01 Daily 与 source packet。
- 冻结官方 Atom XML、19 个候选的 exact-v1 primary packet（20 个 HTML/PDF files，其中 DeepSeek-Prover 同时保留 HTML 与 PDF）、SHA-256 manifest、853-row screening ledger 和 Books writeback receipt。
- root 已分别更新 `70-cost.md`、`59-model-registry.md` 与 `36-distributed-training.md`；本 worker 仅观察并同步该事实，未修改共享 Books、ROADMAP 或 LEARNING_STATE。
- fresh-context reviewer 修正 Books Comparison 的三处旧文件名，并完成四个 scope 的独立验收；未修改三处 Books 正文结论。
- 未 stage、commit 或 push；本日报没有未解决 finding。

## 11. Open Questions

- adaptation quality/cost predictor 在 dataset drift、价格变化和 failed training run 下怎样校准并决定 abstain？
- tensor/delta dedup 怎样与 encryption、quantization、license、base deletion 和独立 rollback 共存？
- parallel-plan cost model 在拓扑拥塞、heterogeneous accelerator 与 elastic failure 下何时失效？
- on-device logical tensor virtualization 如何证明跨 backend numeric equivalence，并为 unsupported operator 设计安全 fallback？

## 12. Sources

- [COSMOS: Predictable and Cost-Effective Adaptation of LLMs](https://arxiv.org/html/2505.01449v1) — arXiv:2505.01449v1；首次公开 `2025-04-30T02:06:26Z`；访问 2026-08-31。
- [ZipLLM: Efficient LLM Storage via Model-Aware Synergistic Data Deduplication and Compression](https://arxiv.org/html/2505.06252v1) — arXiv:2505.06252v1；首次公开 `2025-04-30T04:16:32Z`；访问 2026-08-31。
- [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](https://arxiv.org/html/2504.21303v1) — arXiv:2504.21303v1；首次公开 `2025-04-30T04:24:50Z`；访问 2026-08-31。
- [Phi-4-reasoning Technical Report](https://arxiv.org/html/2504.21318v1) — arXiv:2504.21318v1；首次公开 `2025-04-30T05:05:09Z`；访问 2026-08-31。
- [Nexus-Gen: Unified Image Understanding, Generation, and Editing via Prefilled Autoregression in Shared Embedding Space](https://arxiv.org/html/2504.21356v1) — arXiv:2504.21356v1；首次公开 `2025-04-30T06:30:48Z`；访问 2026-08-31。
- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](https://arxiv.org/html/2504.21370v1) — arXiv:2504.21370v1；首次公开 `2025-04-30T07:04:19Z`；访问 2026-08-31。
- [Galvatron: An Automatic Distributed System for Efficient Foundation Model Training](https://arxiv.org/html/2504.21411v1) — arXiv:2504.21411v1；首次公开 `2025-04-30T08:11:45Z`；访问 2026-08-31。
- [RWKV-X: A Linear Complexity Hybrid Language Model](https://arxiv.org/html/2504.21463v1) — arXiv:2504.21463v1；首次公开 `2025-04-30T09:38:17Z`；访问 2026-08-31。
- [Traceback of Poisoning Attacks to Retrieval-Augmented Generation](https://arxiv.org/html/2504.21668v1) — arXiv:2504.21668v1；首次公开 `2025-04-30T14:10:02Z`；访问 2026-08-31。
- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/html/2504.21776v1) — arXiv:2504.21776v1；首次公开 `2025-04-30T16:25:25Z`；访问 2026-08-31。
- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/html/2504.21798v1) — arXiv:2504.21798v1；首次公开 `2025-04-30T16:56:06Z`；访问 2026-08-31。
- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/html/2504.21801v1) — arXiv:2504.21801v1；首次公开 `2025-04-30T16:57:48Z`；访问 2026-08-31。
- [Which Agent Causes Task Failures and When?](https://arxiv.org/html/2505.00212v1) — arXiv:2505.00212v1；首次公开 `2025-04-30T23:09:44Z`；访问 2026-08-31。
- [Scaling On-Device GPU Inference for Large Generative Models](https://arxiv.org/html/2505.00232v1) — arXiv:2505.00232v1；首次公开 `2025-05-01T00:44:13Z`；访问 2026-08-31。
- [Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks](https://arxiv.org/html/2505.00234v1) — arXiv:2505.00234v1；首次公开 `2025-05-01T00:48:12Z`；访问 2026-08-31。
- [Hoist with His Own Petard: Inducing Guardrails to Facilitate Denial-of-Service Attacks on Retrieval-Augmented Generation of LLMs](https://arxiv.org/html/2504.21680v1) — arXiv:2504.21680v1；首次公开 `2025-04-30T14:18:11Z`；访问 2026-08-31。
- [LongFuncEval: Measuring the effectiveness of long context models for function calling](https://arxiv.org/html/2505.10570v1) — arXiv:2505.10570v1；首次公开 `2025-04-30T15:21:51Z`；访问 2026-08-31。
- [VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup](https://arxiv.org/pdf/2504.21752v1) — arXiv:2504.21752v1；首次公开 `2025-04-30T15:46:55Z`；访问 2026-08-31。
- [Coral Protocol: Open Infrastructure Connecting The Internet of Agents](https://arxiv.org/html/2505.00749v1) — arXiv:2505.00749v1；首次公开 `2025-04-30T22:17:13Z`；访问 2026-08-31。
- [W18 prior discovery baseline](../../weekly/2025-W18/README.md) — 只用于历史对照，不继承 V1 评分或 Review 完成声明。

## 13. Final Status

- Completion Status = `Complete`
- Coverage = `Closed`
- Evidence = `Passed`
- Books = `Passed`
- unresolved findings = `0`
- 最终 Gate：`Complete / Closed / Passed / Passed`。
