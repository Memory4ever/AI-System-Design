# Daily Research — 2025-05-02

**Research Date:** 2025-05-02

**Timezone:** Asia/Shanghai

**Strict Window:** 2025-05-01 09:00:00 ～ 2025-05-02 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。fresh-context reviewer 已完成全量语义复核、exact-v1 证据验收与 post-write Books audit。

## Executive Summary

官方 announcement owner 分母为 321；全量逐行读取 title+abstract 后保留 26 个 family，关闭 295 条，withdrawn/removed exact-v1 为 0，blocked evidence 为 0。未使用 Weekly 作 discovery、筛选、评分、Review 或 Books 证据。7 个初始 closure false negative 已纠正；所有 current-content comparison 与 Gate 已由 fresh-context reviewer 验收。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2025-05-02 |
| Window End | 2025-05-02 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20250502-994341fc36c975991942 |
| Denominator Frozen At | 2026-09-03T21:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2025-05-01T09:00:00+08:00 | 2025-05-02T09:00:00+08:00 | 2026-09-03T21:15:00+08:00 | official announcement owner recovery; owner_report_date=2025-05-02 | checked | 321 | SF-2025-HAACS<br>SF-2025-PROMPT-COMPRESSION<br>SF-2025-PRETRAIN-DATA-MEMBERSHIP<br>SF-2025-NEMOTRON-TOOL-N1<br>SF-2025-MCMCOMM<br>SF-2025-CONSENS-CONTEXT-GROUNDING<br>SF-2025-EMBEDDING-QUANTIZATION<br>SF-2025-WHOWHEN<br>SF-2025-ML-DRIFT<br>SF-2025-TRAJ-BOOTSTRAP<br>SF-2025-AVA<br>SF-2025-ENRONQA<br>SF-2025-MOSA<br>SF-2025-EDGE-LAM<br>SF-2025-T2VPHYS<br>SF-2025-LLMPRISM<br>SF-2025-SOLO<br>SF-2025-RNB<br>SF-2025-SACFL<br>SF-2025-DISTRIBUTED-RAG<br>SF-2025-MEMORY-CENTRIC-COMPUTING<br>SF-2025-PROPERTY-DRIVEN-ML<br>SF-2025-HALLUMIX<br>SF-2025-FREQKV<br>SF-2025-ROLE-SEPARATION-SHORTCUTS<br>SF-2025-AGENT-MEMORY-OPERATIONS | pages=1; final_cursor=end; rows=321 | 2025-05-02T09:00:00+08:00 | coverage:SRC-ARXIV:20250502 | — |

<!-- coverage:SRC-ARXIV:20250502:start -->owner inventory SHA prefix `994341fc36c975991942`；semantic ledger SHA prefix `13c1e2960c37714bbc20`；算术 `321 = 26 retained + 295 closures`。<!-- coverage:SRC-ARXIV:20250502:end -->

### Coverage Limitations

注册表晚于历史窗口；本次只对可复现的官方 announcement owner inventory 作完整论文 recall。组织来源若无历史枚举证据，不伪造 retroactive no-hit。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HAACS | arXiv:2505.00018v1 | paper-v1:2505.00018 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-HAACS | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2025-HAACS | no |
| SF-2025-PROMPT-COMPRESSION | arXiv:2505.00019v1 | paper-v1:2505.00019 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-PROMPT-COMPRESSION | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2025-PROMPT-COMPRESSION | no |
| SF-2025-PRETRAIN-DATA-MEMBERSHIP | arXiv:2505.00020v1 | paper-v1:2505.00020 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-PRETRAIN-DATA-MEMBERSHIP | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP | no |
| SF-2025-NEMOTRON-TOOL-N1 | arXiv:2505.00024v1 | paper-v1:2505.00024 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-NEMOTRON-TOOL-N1 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2025-NEMOTRON-TOOL-N1 | no |
| SF-2025-MCMCOMM | arXiv:2505.00041v1 | paper-v1:2505.00041 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-MCMCOMM | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2025-MCMCOMM | no |
| SF-2025-CONSENS-CONTEXT-GROUNDING | arXiv:2505.00065v1 | paper-v1:2505.00065 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-CONSENS-CONTEXT-GROUNDING | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-CONSENS-CONTEXT-GROUNDING | no |
| SF-2025-EMBEDDING-QUANTIZATION | arXiv:2505.00105v1 | paper-v1:2505.00105 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-EMBEDDING-QUANTIZATION | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2025-EMBEDDING-QUANTIZATION | no |
| SF-2025-WHOWHEN | arXiv:2505.00212v1 | paper-v1:2505.00212 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-WHOWHEN | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2025-WHOWHEN | yes |
| SF-2025-ML-DRIFT | arXiv:2505.00232v1 | paper-v1:2505.00232 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-ML-DRIFT | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2025-ML-DRIFT | yes |
| SF-2025-TRAJ-BOOTSTRAP | arXiv:2505.00234v1 | paper-v1:2505.00234 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2025-TRAJ-BOOTSTRAP | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2025-TRAJ-BOOTSTRAP | yes |
| SF-2025-AVA | arXiv:2505.00254v1 | paper-v1:2505.00254 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2025-AVA | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2025-AVA | yes |
| SF-2025-ENRONQA | arXiv:2505.00263v1 | paper-v1:2505.00263 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-ENRONQA | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2025-ENRONQA | yes |
| SF-2025-MOSA | arXiv:2505.00315v1 | paper-v1:2505.00315 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-MOSA | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2025-MOSA | yes |
| SF-2025-EDGE-LAM | arXiv:2505.00321v1 | paper-v1:2505.00321 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-EDGE-LAM | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2025-EDGE-LAM | no |
| SF-2025-T2VPHYS | arXiv:2505.00337v1 | paper-v1:2505.00337 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-T2VPHYS | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2025-T2VPHYS | yes |
| SF-2025-LLMPRISM | arXiv:2505.00342v1 | paper-v1:2505.00342 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-LLMPRISM | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2025-LLMPRISM | yes |
| SF-2025-SOLO | arXiv:2505.00347v1 | paper-v1:2505.00347 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2025-SOLO | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2025-SOLO | yes |
| SF-2025-RNB | arXiv:2505.00358v1 | paper-v1:2505.00358 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-RNB | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2025-RNB | yes |
| SF-2025-SACFL | arXiv:2505.00365v1 | paper-v1:2505.00365 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-SACFL | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2025-SACFL | no |
| SF-2025-DISTRIBUTED-RAG | arXiv:2505.00443v1 | paper-v1:2505.00443 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-DISTRIBUTED-RAG | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2025-DISTRIBUTED-RAG | yes |
| SF-2025-MEMORY-CENTRIC-COMPUTING | arXiv:2505.00458v1 | paper-v1:2505.00458 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-MEMORY-CENTRIC-COMPUTING | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2025-MEMORY-CENTRIC-COMPUTING | no |
| SF-2025-PROPERTY-DRIVEN-ML | arXiv:2505.00466v1 | paper-v1:2505.00466 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-PROPERTY-DRIVEN-ML | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2025-PROPERTY-DRIVEN-ML | no |
| SF-2025-HALLUMIX | arXiv:2505.00506v1 | paper-v1:2505.00506 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-HALLUMIX | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-HALLUMIX | yes |
| SF-2025-FREQKV | arXiv:2505.00570v1 | paper-v1:2505.00570 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2025-FREQKV | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2025-FREQKV | yes |
| SF-2025-ROLE-SEPARATION-SHORTCUTS | arXiv:2505.00626v1 | paper-v1:2505.00626 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-ROLE-SEPARATION-SHORTCUTS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS | no |
| SF-2025-AGENT-MEMORY-OPERATIONS | arXiv:2505.00675v1 | paper-v1:2505.00675 | 2025-W18 | 2025-05-02 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2025-AGENT-MEMORY-OPERATIONS | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2025-AGENT-MEMORY-OPERATIONS | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HAACS | RP-9226d76a21f62c83 | standard | arXiv:2505.00018v1 | SRC-ARXIV@arXiv:2505.00018v1 | https://arxiv.org/html/2505.00018v1#S9.SS2 | Not Disclosed — position paper provides no controlled end-to-end evaluation | https://arxiv.org/html/2505.00018v1#S9.SS6 | Not Required — Standard Review | claim:SF-2025-HAACS | complete |
| SF-2025-PROMPT-COMPRESSION | RP-1e25d6df19c65ad4 | deep | arXiv:2505.00019v1 | SRC-ARXIV@arXiv:2505.00019v1 | https://arxiv.org/html/2505.00019v1#S3 | https://arxiv.org/html/2505.00019v1#S5 | https://arxiv.org/html/2505.00019v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-PROMPT-COMPRESSION | complete |
| SF-2025-PRETRAIN-DATA-MEMBERSHIP | RP-24b4eee40467e6b0 | deep | arXiv:2505.00020v1 | SRC-ARXIV@arXiv:2505.00020v1 | https://arxiv.org/html/2505.00020v1#S2 | https://arxiv.org/html/2505.00020v1#S3.SS1 | https://arxiv.org/html/2505.00020v1#S3.SS4 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-PRETRAIN-DATA-MEMBERSHIP | complete |
| SF-2025-NEMOTRON-TOOL-N1 | RP-08510693c8e25bbc | deep | arXiv:2505.00024v1 | SRC-ARXIV@arXiv:2505.00024v1 | https://arxiv.org/html/2505.00024v1#S4 | https://arxiv.org/html/2505.00024v1#S5 | https://arxiv.org/html/2505.00024v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-NEMOTRON-TOOL-N1 | complete |
| SF-2025-MCMCOMM | RP-1f9e4e92cafcd4ca | deep | arXiv:2505.00041v1 | SRC-ARXIV@arXiv:2505.00041v1 | https://arxiv.org/html/2505.00041v1#S4; #S5 | https://arxiv.org/html/2505.00041v1#S7 | https://arxiv.org/html/2505.00041v1#S8 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-MCMCOMM | complete |
| SF-2025-CONSENS-CONTEXT-GROUNDING | RP-9daf94a9490bf191 | deep | arXiv:2505.00065v1 | SRC-ARXIV@arXiv:2505.00065v1 | https://arxiv.org/html/2505.00065v1#S2 | https://arxiv.org/html/2505.00065v1#S3 | https://arxiv.org/html/2505.00065v1#S4 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-CONSENS-CONTEXT-GROUNDING | complete |
| SF-2025-EMBEDDING-QUANTIZATION | RP-80ea5a839a23f316 | deep | arXiv:2505.00105v1 | SRC-ARXIV@arXiv:2505.00105v1 | https://arxiv.org/html/2505.00105v1#S4 | https://arxiv.org/html/2505.00105v1#S5 | https://arxiv.org/html/2505.00105v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-EMBEDDING-QUANTIZATION | complete |
| SF-2025-WHOWHEN | RP-78dcb9f50b93cecd | deep | arXiv:2505.00212v1 | SRC-ARXIV@arXiv:2505.00212v1 | https://arxiv.org/html/2505.00212v1#S2; https://arxiv.org/html/2505.00212v1#S3; https://arxiv.org/html/2505.00212v1#A2 | https://arxiv.org/html/2505.00212v1#S4; https://arxiv.org/html/2505.00212v1#A4 | https://arxiv.org/html/2505.00212v1#S6; https://arxiv.org/html/2505.00212v1#S7 | https://github.com/mingyin1/Agents_Failure_Attribution — repository linked from exact-v1 | claim:SF-2025-WHOWHEN | complete |
| SF-2025-ML-DRIFT | RP-423c3e08352153c9 | deep | arXiv:2505.00232v1 | SRC-ARXIV@arXiv:2505.00232v1 | https://arxiv.org/html/2505.00232v1#S3; https://arxiv.org/html/2505.00232v1#S3.SS7; https://arxiv.org/html/2505.00232v1#S3.SS8 | https://arxiv.org/html/2505.00232v1#S4; https://arxiv.org/html/2505.00232v1#S4.SS2 | https://arxiv.org/html/2505.00232v1#S5 | Not Disclosed — exact-v1 describes the framework but does not identify a frozen public ML Drift repository | claim:SF-2025-ML-DRIFT | complete |
| SF-2025-TRAJ-BOOTSTRAP | RP-4c25305c7c594b33 | deep | arXiv:2505.00234v1 | SRC-ARXIV@arXiv:2505.00234v1 | https://arxiv.org/html/2505.00234v1#S5; https://arxiv.org/html/2505.00234v1#A4 | https://arxiv.org/html/2505.00234v1#S6; https://arxiv.org/html/2505.00234v1#A5; https://arxiv.org/html/2505.00234v1#A6 | https://arxiv.org/html/2505.00234v1#S7; https://arxiv.org/html/2505.00234v1#A2 | Not Disclosed — exact-v1 does not identify a released trajectory database implementation | claim:SF-2025-TRAJ-BOOTSTRAP | complete |
| SF-2025-AVA | RP-5d482f3eeba8e5e3 | deep | arXiv:2505.00254v1 | SRC-ARXIV@arXiv:2505.00254v1 | https://arxiv.org/html/2505.00254v1 — exact-v1 §3 system overview；§4 index construction；§4.1 Event KG | https://arxiv.org/html/2505.00254v1 — exact-v1 §5 agentic retrieval；§6 implementation；§7 evaluation | https://arxiv.org/html/2505.00254v1 — exact-v1 §8 limitations | Not Disclosed — linked implementation revision is not frozen in the paper | claim:SF-2025-AVA | complete |
| SF-2025-ENRONQA | RP-f5694b6cc89062bb | standard | arXiv:2505.00263v1 | SRC-ARXIV@arXiv:2505.00263v1 | https://arxiv.org/html/2505.00263v1 — exact-v1 §3 dataset construction；§4 quality | https://arxiv.org/html/2505.00263v1 — exact-v1 §5 benchmarking；§6 memorized knowledge | https://arxiv.org/html/2505.00263v1 — exact-v1 §7 discussion；Ethics statement | Not Disclosed — dataset release revision is not frozen | claim:SF-2025-ENRONQA | complete |
| SF-2025-MOSA | RP-e0eff22681655851 | standard | arXiv:2505.00315v1 | SRC-ARXIV@arXiv:2505.00315v1 | https://arxiv.org/html/2505.00315v1 — exact-v1 §2 Mixture of Sparse Attention | https://arxiv.org/html/2505.00315v1 — exact-v1 §3 experiments；Appendix FLOPs/model settings | https://arxiv.org/html/2505.00315v1 — exact-v1 §5 limitations | Not Disclosed — optimized sparse kernel is not released as frozen evidence | claim:SF-2025-MOSA | complete |
| SF-2025-EDGE-LAM | RP-1fd50651017e3762 | deep | arXiv:2505.00321v1 | SRC-ARXIV@arXiv:2505.00321v1 | https://arxiv.org/html/2505.00321v1#S2; #S3 | https://arxiv.org/html/2505.00321v1#S5 | https://arxiv.org/html/2505.00321v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-EDGE-LAM | complete |
| SF-2025-T2VPHYS | RP-a7dd096fa6a14828 | standard | arXiv:2505.00337v1 | SRC-ARXIV@arXiv:2505.00337v1 | https://arxiv.org/html/2505.00337v1 — exact-v1 §3 benchmark；§3.3 protocol | https://arxiv.org/html/2505.00337v1 — exact-v1 §4 experiments；Appendix A implementation | https://arxiv.org/html/2505.00337v1 — exact-v1 §5 discussion；Appendix B limitations | Not Disclosed — benchmark revision is not frozen | claim:SF-2025-T2VPHYS | complete |
| SF-2025-LLMPRISM | RP-45270c77721f3a37 | deep | arXiv:2505.00342v1 | SRC-ARXIV@arXiv:2505.00342v1 | https://arxiv.org/html/2505.00342v1 — exact-v1 §III motivation；§IV methodology A-D | https://arxiv.org/html/2505.00342v1 — exact-v1 §V evaluation and deployed experience A-D | https://arxiv.org/html/2505.00342v1 — exact-v1 §VII generalization and limits | Not Disclosed — production deployment code is not public | claim:SF-2025-LLMPRISM | complete |
| SF-2025-SOLO | RP-8e97daa877e57fa9 | deep | arXiv:2505.00347v1 | SRC-ARXIV@arXiv:2505.00347v1 | https://arxiv.org/html/2505.00347v1 — exact-v1 §3 ultra-low-bit optimizer；§3.1-3.3 EMA dynamics | https://arxiv.org/html/2505.00347v1 — exact-v1 §4 experiments；Appendix C settings | https://arxiv.org/html/2505.00347v1 — exact-v1 § Discussion/Limitations boundary — exact-v1 discussion/ablation and precision limits | Not Disclosed — exact training implementation revision not frozen | claim:SF-2025-SOLO | complete |
| SF-2025-RNB | RP-66cb5a5af3eebc67 | deep | arXiv:2505.00358v1 | SRC-ARXIV@arXiv:2505.00358v1 | https://arxiv.org/html/2505.00358v1 — exact-v1 §3 regrouping and balancing | https://arxiv.org/html/2505.00358v1 — exact-v1 §4 experiments；Appendix E/F implementation/settings | https://arxiv.org/html/2505.00358v1 — exact-v1 Appendix D cost and discussion limits | Not Disclosed — exact data/control artifact revision is not frozen | claim:SF-2025-RNB | complete |
| SF-2025-SACFL | RP-c709935ac7232342 | standard | arXiv:2505.00365v1 | SRC-ARXIV@arXiv:2505.00365v1 | https://arxiv.org/html/2505.00365v1#S3 | https://arxiv.org/html/2505.00365v1#S5 | https://arxiv.org/html/2505.00365v1#S6 | https://github.com/Zhong-Zhengyi/SacFL-Code — repository linked from exact-v1; revision not frozen | claim:SF-2025-SACFL | complete |
| SF-2025-DISTRIBUTED-RAG | RP-af959f00565708d7 | deep | arXiv:2505.00443v1 | SRC-ARXIV@arXiv:2505.00443v1 | https://arxiv.org/html/2505.00443v1 — exact-v1 §3 distributed RAG model and topic-aware random walk | https://arxiv.org/html/2505.00443v1 — exact-v1 §4 experiments and sensitivity | https://arxiv.org/html/2505.00443v1 — exact-v1 § Discussion/Limitations boundary — exact-v1 discussion and threat boundary | Not Disclosed — exact simulation/repository revision is not frozen | claim:SF-2025-DISTRIBUTED-RAG | complete |
| SF-2025-MEMORY-CENTRIC-COMPUTING | RP-8b0c22ed964d7ae2 | standard | arXiv:2505.00458v1 | SRC-ARXIV@arXiv:2505.00458v1 | https://arxiv.org/html/2505.00458v1#S2 | https://arxiv.org/html/2505.00458v1#S3 | https://arxiv.org/html/2505.00458v1#S4 | Not Required — Standard Review | claim:SF-2025-MEMORY-CENTRIC-COMPUTING | complete |
| SF-2025-PROPERTY-DRIVEN-ML | RP-4a84d251861e95da | deep | arXiv:2505.00466v1 | SRC-ARXIV@arXiv:2505.00466v1 | https://arxiv.org/html/2505.00466v1#S3 | https://arxiv.org/html/2505.00466v1#S4 | https://arxiv.org/html/2505.00466v1#S5 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-PROPERTY-DRIVEN-ML | complete |
| SF-2025-HALLUMIX | RP-18e6c620b163bad2 | standard | arXiv:2505.00506v1 | SRC-ARXIV@arXiv:2505.00506v1 | https://arxiv.org/html/2505.00506v1 — exact-v1 §2 benchmark；§3 methodology | https://arxiv.org/html/2505.00506v1 — exact-v1 §4 results | https://arxiv.org/html/2505.00506v1 — exact-v1 §5 discussion, sub-source overfitting and length | Not Disclosed — exact benchmark release revision not frozen | claim:SF-2025-HALLUMIX | complete |
| SF-2025-FREQKV | RP-a6d41e065303d3ac | deep | arXiv:2505.00570v1 | SRC-ARXIV@arXiv:2505.00570v1 | https://arxiv.org/html/2505.00570v1 — exact-v1 §4 method | https://arxiv.org/html/2505.00570v1 — exact-v1 §5 experiments；§6 latency analysis | https://arxiv.org/html/2505.00570v1 — exact-v1 analysis and Appendix D overhead | Not Disclosed — exact implementation revision not frozen | claim:SF-2025-FREQKV | complete |
| SF-2025-ROLE-SEPARATION-SHORTCUTS | RP-4333acfbfbe89fe2 | deep | arXiv:2505.00626v1 | SRC-ARXIV@arXiv:2505.00626v1 | https://arxiv.org/html/2505.00626v1#S3 | https://arxiv.org/html/2505.00626v1#S5 | https://arxiv.org/html/2505.00626v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-ROLE-SEPARATION-SHORTCUTS | complete |
| SF-2025-AGENT-MEMORY-OPERATIONS | RP-769b04b2dcf2d39a | deep | arXiv:2505.00675v1 | SRC-ARXIV@arXiv:2505.00675v1 | https://arxiv.org/html/2505.00675v1#S2; #S3 | Not Disclosed — survey provides no unified controlled evaluation | https://arxiv.org/html/2505.00675v1#S6 | https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI — survey catalog; not an implementation artifact | claim:SF-2025-AGENT-MEMORY-OPERATIONS | complete |

### Source Reviews

<!-- review:SF-2025-HAACS:start --><!-- claim:SF-2025-HAACS:start -->把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。<!-- claim:SF-2025-HAACS:end -->

这是 position paper 与综合性架构主张，没有实现 artifact 或端到端实证；只能作为 owner-boundary 提案，不能把 HE2-Net 视为已验证的生产协调协议。<!-- review:SF-2025-HAACS:end -->

<!-- review:SF-2025-PROMPT-COMPRESSION:start --><!-- claim:SF-2025-PROMPT-COMPRESSION:start -->把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。<!-- claim:SF-2025-PROMPT-COMPRESSION:end -->

经验结果绑定论文模型与任务，不构成跨模型最优压缩率或长上下文质量定律。<!-- review:SF-2025-PROMPT-COMPRESSION:end -->

<!-- review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start --><!-- claim:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。<!-- claim:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

membership inference 是统计 sensor；论文数据和模型上的结果不能证明某个未披露训练集成员关系，更不能替代法律许可判断。<!-- review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

<!-- review:SF-2025-NEMOTRON-TOOL-N1:start --><!-- claim:SF-2025-NEMOTRON-TOOL-N1:start -->把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。<!-- claim:SF-2025-NEMOTRON-TOOL-N1:end -->

结果绑定作者数据生成、工具集合和 evaluator；不能证明开放工具生态、权限副作用或分布外 schema 下同样可靠。<!-- review:SF-2025-NEMOTRON-TOOL-N1:end -->

<!-- review:SF-2025-MCMCOMM:start --><!-- claim:SF-2025-MCMCOMM:start -->把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。<!-- claim:SF-2025-MCMCOMM:end -->

分析与评估绑定作者的 MCM design space、模型集合及 analytical assumptions；没有公开冻结实现，不能把模拟收益外推到任意封装、互连或真实 congestion。<!-- review:SF-2025-MCMCOMM:end -->

<!-- review:SF-2025-CONSENS-CONTEXT-GROUNDING:start --><!-- claim:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。<!-- claim:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

验证覆盖论文数据集和 judge 配置；相关性不证明事实正确，也不能替代 retrieval-stage provenance。<!-- review:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

<!-- review:SF-2025-EMBEDDING-QUANTIZATION:start --><!-- claim:SF-2025-EMBEDDING-QUANTIZATION:start -->把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。<!-- claim:SF-2025-EMBEDDING-QUANTIZATION:end -->

PCA/quantization 的收益绑定论文数据、embedding model 与索引设置；没有证明所有语义空间或 ANN backend 都保持排序。<!-- review:SF-2025-EMBEDDING-QUANTIZATION:end -->

<!-- review:SF-2025-WHOWHEN:start --><!-- claim:SF-2025-WHOWHEN:start -->多 Agent debugging 必须保存 agent、step、tool result 与 shared-state revision；LLM attribution 只产生 diagnostic evidence，不能直接成为 rollback 或责任裁决。<!-- claim:SF-2025-WHOWHEN:end -->论文标注 127 个 systems、184 个 failed tasks，比较三种定位流程与 context/cost sensitivity。结果显示全局 receptive field、局部 step precision 和 token cost 冲突；judge bias、shared cause、single-blame 标签与隐私限制因果解释。<!-- review:SF-2025-WHOWHEN:end -->

<!-- review:SF-2025-ML-DRIFT:start --><!-- claim:SF-2025-ML-DRIFT:start -->on-device runtime 要把逻辑 tensor 与物理 GPU object 分离，再由 device specialization、memory manager、fusion 和 prefill/decode plan materialize；模型语义不应绑定单一 GPU API。<!-- claim:SF-2025-ML-DRIFT:end -->论文跨 mobile、desktop/laptop 与 Apple Silicon 测试 diffusion/LLM，并给出 virtualization、coordinate translation、memory、fusion 和 KV layout。作者 benchmark 受设备、driver、model 与 precision 约束；跨设备实现复杂度、memory pressure 和 fallback coverage 是代价。<!-- review:SF-2025-ML-DRIFT:end -->

<!-- review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- claim:SF-2025-TRAJ-BOOTSTRAP:start -->成功轨迹可以成为下次决策的候选 memory，但 source task、policy version、outcome verifier、selection 与 deletion policy 必须随 exemplar 保存；成功一次不等于普适规则。<!-- claim:SF-2025-TRAJ-BOOTSTRAP:end -->论文从 agent 自己的成功 experience 构建数据库并做 database/exemplar selection，在 ALFWorld、Wordcraft、InterCode-SQL 评估。收益受 benchmark、initial examples、retriever 和 growing-context cost 限制；feedback loop 会固化偶然成功或污染，人工示例在高风险/低数据时仍合理。<!-- review:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- review:SF-2025-AVA:start --><!-- claim:SF-2025-AVA:start -->长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。<!-- claim:SF-2025-AVA:end -->作者以 3 秒片段生成描述并做语义合并，构造事件/实体/时间图，再用多视图检索、MCTS 与 self-consistency 回答。AVA-100 只覆盖八段长视频和 120 个问题；描述误差、图陈旧与搜索成本会累积，不能外推为通用实时视频理解。<!-- review:SF-2025-AVA:end -->

<!-- review:SF-2025-ENRONQA:start --><!-- claim:SF-2025-ENRONQA:start -->私有文档 RAG 的正确答案必须绑定用户、邮箱快照、权限与 retrieval receipt；benchmark 命中不证明真实企业隐私和访问控制。<!-- claim:SF-2025-ENRONQA:end -->作者从 103,638 封邮件构造 528,304 QA，并以 150 个 inbox 测试个性化检索与模型记忆。该合同支持检索/记忆差异分析，不证明真实企业 ACL、删除、时效或隐私合规。<!-- review:SF-2025-ENRONQA:end -->

<!-- review:SF-2025-MOSA:start --><!-- claim:SF-2025-MOSA:start -->content-based sparse attention 以 selector 换取更低 attention work，但 selector error、position identity 和稀疏 kernel 决定它是否优于 dense。<!-- claim:SF-2025-MOSA:end -->作者在 iso-FLOP 的非自回归语言建模设置比较 expert-choice sparse attention；perplexity 优势并不总转化为下游收益，短序列较弱，且未提供优化 kernel 或 causal serving 证据。<!-- review:SF-2025-MOSA:end -->

<!-- review:SF-2025-EDGE-LAM:start --><!-- claim:SF-2025-EDGE-LAM:start -->把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。<!-- claim:SF-2025-EDGE-LAM:end -->

论文主要是架构综述与 6G case study，没有完整端到端 implementation/benchmark；不能证明所述 looped TP 或 microservice migration 已满足真实 edge reliability。<!-- review:SF-2025-EDGE-LAM:end -->

<!-- review:SF-2025-T2VPHYS:start --><!-- claim:SF-2025-T2VPHYS:start -->视频生成质量不能代替物理一致性；评估必须冻结物理规律、prompt、hint/counterfactual、judge 与人类协议。<!-- claim:SF-2025-T2VPHYS:end -->作者以十二类 first-principles law 构建 benchmark 并报告受测系统平均分均低于 0.60。它诊断生成失败，不证明模型具有或缺乏可用于控制的因果 world state，也不预测真实机器人 policy success。<!-- review:SF-2025-T2VPHYS:end -->

<!-- review:SF-2025-LLMPRISM:start --><!-- claim:SF-2025-LLMPRISM:start -->当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。<!-- claim:SF-2025-LLMPRISM:end -->论文从交换机/host 网络流推断训练任务、并行策略与阶段，并报告自 2024-10 的生产部署经验。作者的识别率和时间线误差只属于其平台与流量合同；旁路传感无法证明模型正确，也可能被共享流量或版本漂移混淆。<!-- review:SF-2025-LLMPRISM:end -->

<!-- review:SF-2025-SOLO:start --><!-- claim:SF-2025-SOLO:start -->低比特 optimizer 的风险不只是静态误差：unsigned EMA 会淹没新信号，signed state 会放大方差或方向错误；状态演化决定是否还能学习。<!-- claim:SF-2025-SOLO:end -->作者用 log quantization 与 precision-specific momentum 处理 2-bit 级 Adam state，并在受限模型/训练设置比较。证据不覆盖所有 optimizer、分布式 checkpoint、故障恢复或数值格式；高精度 state 在小规模或不稳定训练中仍是基线。<!-- review:SF-2025-SOLO:end -->

<!-- review:SF-2025-RNB:start --><!-- claim:SF-2025-RNB:start -->数据域不能永久沿用人工标签；可由表示和梯度反馈重组，但 estimator、mixture revision 与 drift fallback 必须纳入 lineage。<!-- claim:SF-2025-RNB:end -->作者以 embedding 与累计 final-layer gradient similarity 动态重组域并更新 mixture。受控实验支持样本效率，不能证明 final-layer proxy 在 frontier scale、生产漂移或不同 optimizer 下稳定；cluster churn 和 feedback cost 是新风险。<!-- review:SF-2025-RNB:end -->

<!-- review:SF-2025-SACFL:start --><!-- claim:SF-2025-SACFL:start -->在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。<!-- claim:SF-2025-SACFL:end -->

实验覆盖作者选择的数据集、3-20 个任务与模拟/演示环境；论文未证明长期真实 client churn、secure aggregation 或不同硬件资源下的收敛与防御。<!-- review:SF-2025-SACFL:end -->

<!-- review:SF-2025-DISTRIBUTED-RAG:start --><!-- claim:SF-2025-DISTRIBUTED-RAG:start -->分布式 RAG 将 corpus ownership 留在 peer，并以 topic-aware discovery 代替中央索引；它减少集中收集，却不会自动提供 query privacy、信任或一致性。<!-- claim:SF-2025-DISTRIBUTED-RAG:end -->作者在仿真网络比较 topic-aware random walk 与 flooding/centralized baselines，并报告接近中央检索、消息更少。证据不覆盖对抗 peer、真实网络故障、隐私证明或生产尾延迟；稳定可审计 corpus 仍适合中央 RAG。<!-- review:SF-2025-DISTRIBUTED-RAG:end -->

<!-- review:SF-2025-MEMORY-CENTRIC-COMPUTING:start --><!-- claim:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。<!-- claim:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

论文是机制综述与系统立场，不提供一个可直接泛化到所有 LLM workload 的单一实现或 benchmark 结论。<!-- review:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

<!-- review:SF-2025-PROPERTY-DRIVEN-ML:start --><!-- claim:SF-2025-PROPERTY-DRIVEN-ML:start -->把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。<!-- claim:SF-2025-PROPERTY-DRIVEN-ML:end -->

MNIST 与 drone 案例只验证框架可行性；不能证明 property set 完备，learned checker 也不能独占发布 authority。<!-- review:SF-2025-PROPERTY-DRIVEN-ML:end -->

<!-- review:SF-2025-HALLUMIX:start --><!-- claim:SF-2025-HALLUMIX:start -->hallucination detector 的分数只属于给定任务、来源、长度和 evaluator；跨来源平均值不能替代 slice 与 calibration。<!-- claim:SF-2025-HALLUMIX:end -->作者构建 task-agnostic multi-domain benchmark，比较检测器并揭示来源过拟合与长度效应。最佳指标属于其数据划分和标签协议，不证明开放世界事实核验、生产置信度或单条 claim 正确性。<!-- review:SF-2025-HALLUMIX:end -->

<!-- review:SF-2025-FREQKV:start --><!-- claim:SF-2025-FREQKV:start -->频域 KV 压缩用有损 summary 延伸窗口；频率分配、RoPE/position identity 与关键 token 丢失决定它何时必须回退 FullKV。<!-- claim:SF-2025-FREQKV:end -->作者在 LLaMA2/3、8K 训练与最长 256K 评测下比较长上下文任务和 latency。证据不覆盖 continuous batching、并发尾延迟或关键事实不可丢失的 workload，不能把平均质量外推为通用无损缓存。<!-- review:SF-2025-FREQKV:end -->

<!-- review:SF-2025-ROLE-SEPARATION-SHORTCUTS:start --><!-- claim:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。<!-- claim:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

shortcut 分析与缓解绑定论文模型、模板和攻击；没有证明重排 position ID 能覆盖所有 provenance confusion。<!-- review:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

<!-- review:SF-2025-AGENT-MEMORY-OPERATIONS:start --><!-- claim:SF-2025-AGENT-MEMORY-OPERATIONS:start -->把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。<!-- claim:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

这是 survey/taxonomy，不是对六个操作统一实现或 benchmark 的 primary validation；所列 tools 与未来方向不能升级为跨系统性能结论。<!-- review:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

## 4. Benchmark Contracts

只有 Candidate Ledger 明确标为 `yes` 的数字主张进入下表；其余论文数字不被提升为日报结论。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-WHOWHEN | 127 multi-agent systems、184 failed tasks、step/agent attribution | GPT-4o and open/reasoning judge roster | Not Disclosed | Not Disclosed | full or partial trace | agent + decisive step | 184 annotated failures | offline | agent/step accuracy、tolerance、token cost | three-expert annotation consensus |
| SF-2025-ML-DRIFT | large diffusion/LLM inference across mobile、desktop/laptop、Apple Silicon GPUs | diffusion and LLM roster in §4 | multiple mobile GPUs、desktop/laptop GPUs、Apple Silicon | model/device-specific；not normalized | model/input-specific | image/audio/text generation | device-specific | single-device inference | latency/memory/throughput；无 production threshold | runtime timing + output checks |
| SF-2025-TRAJ-BOOTSTRAP | ALFWorld、Wordcraft、InterCode-SQL sequential decision tasks | LLM agent backbones in §6.1 | Appendix F computational resources | Not Disclosed | task observation/action history + retrieved exemplars | agent action trajectory | population/retrieval configs | sequential episodes | task success and quality metrics | environment/task evaluator |
| SF-2025-AVA | long-video indexing and agentic question answering | Qwen2.5-VL-7B for indexing; answer roster in paper | 2×RTX 4090 for index construction | Not Disclosed | 3-second video chunks; videos >10 hours | answer text | Not Disclosed | self-consistency 8/16 samples | >5 FPS indexing; QA quality; no production SLO | AVA-100 human-authored QA and paper metrics |
| SF-2025-ENRONQA | personalized QA over private email corpora | retrieval and LLM baselines listed in §5 | Not Disclosed | Not Disclosed | email/query-defined | answer text | Not Disclosed | offline | QA metrics; no latency or privacy SLO | dataset answers and benchmark scorer |
| SF-2025-MOSA | iso-FLOP language modeling with sparse attention | models listed in exact-v1 Appendix | Not Disclosed | Not Disclosed | sequence lengths in paper | Not Disclosed | Not Disclosed | offline | perplexity/downstream score; no serving SLO | paper task evaluators |
| SF-2025-T2VPHYS | text-to-video physical consistency across 12 law categories | video generators listed in §4 | Not Disclosed | Not Disclosed | prompt-defined | video | Not Disclosed | offline | physical consistency score; no production threshold | human protocol plus benchmark judge |
| SF-2025-LLMPRISM | black-box diagnosis of production LLM training network flows | production training jobs; exact model roster Not Disclosed | production platform topology Not Disclosed | Not Disclosed | flow sequence | job/parallelism/phase labels | Not Disclosed | multi-job platform | diagnosis accuracy and timeline error; no user-facing SLO | ground-truth platform job metadata |
| SF-2025-SOLO | language-model training with ultra-low-bit optimizer states | model roster in exact-v1 §4 | hardware Not Disclosed | 2-bit and comparison precisions | training sequence length Not Disclosed | Not Disclosed | settings in Appendix C | distributed topology Not Disclosed | loss/downstream quality and memory; no production SLO | paper training/evaluation pipeline |
| SF-2025-RNB | foundation-model pretraining data regrouping and mixture balancing | model roster in exact-v1 §4 | Not Disclosed | Not Disclosed | training corpus-defined | Not Disclosed | Not Disclosed | offline training | loss/downstream metrics; no production SLO | paper benchmark evaluators |
| SF-2025-DISTRIBUTED-RAG | peer-to-peer retrieval-augmented generation | retrieval/generation models in exact-v1 | simulation; hardware Not Disclosed | Not Disclosed | query/corpus-defined | answer text | Not Disclosed | peer network simulation | retrieval/answer quality and messages; no production SLO | simulation benchmark metrics |
| SF-2025-HALLUMIX | hallucination detection across NLI, summarization and QA | detector roster in exact-v1 | Not Disclosed | Not Disclosed | dataset/length slices | label | Not Disclosed | offline | accuracy/F1; no production calibration threshold | benchmark labels and paper metrics |
| SF-2025-FREQKV | long-context inference with frequency-domain KV compression | LLaMA2/3 roster in exact-v1 | hardware in exact-v1 §6; topology Not Disclosed | Not Disclosed | trained 8K; evaluated up to 256K | task-defined | Not Disclosed | Not Disclosed | task quality and latency; no production SLO | long-context benchmark metrics |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2025-PROMPT-COMPRESSION | score_7_9 | not_selected | — | — | SF-2025-PROMPT-COMPRESSION 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-PROMPT-COMPRESSION |
| SF-2025-PRETRAIN-DATA-MEMBERSHIP | score_7_9 | not_selected | — | — | SF-2025-PRETRAIN-DATA-MEMBERSHIP 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-PRETRAIN-DATA-MEMBERSHIP |
| SF-2025-NEMOTRON-TOOL-N1 | score_7_9 | not_selected | — | — | SF-2025-NEMOTRON-TOOL-N1 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-NEMOTRON-TOOL-N1 |
| SF-2025-MCMCOMM | score_7_9 | selected | DA-MCMCOMM | — | 把 chiplet layout、packaging 与 workload placement 联合建模，硬件/软件 reach 高。 | analysis:DA-MCMCOMM |
| SF-2025-CONSENS-CONTEXT-GROUNDING | score_7_9 | not_selected | — | — | SF-2025-CONSENS-CONTEXT-GROUNDING 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-CONSENS-CONTEXT-GROUNDING |
| SF-2025-EMBEDDING-QUANTIZATION | score_7_9 | not_selected | — | — | SF-2025-EMBEDDING-QUANTIZATION 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-EMBEDDING-QUANTIZATION |
| SF-2025-WHOWHEN | score_7_9 | not_selected | — | — | SF-2025-WHOWHEN 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-WHOWHEN |
| SF-2025-ML-DRIFT | score_7_9 | not_selected | — | — | SF-2025-ML-DRIFT 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-ML-DRIFT |
| SF-2025-TRAJ-BOOTSTRAP | score_7_9 | not_selected | — | — | SF-2025-TRAJ-BOOTSTRAP 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-TRAJ-BOOTSTRAP |
| SF-2025-AVA | forced_review | selected | DA-AVA | — | 持续媒体的 event/entity/time graph 改变检索状态 owner，且既有 Books writeback 需要 post-write 验证。 | analysis:DA-AVA |
| SF-2025-EDGE-LAM | score_7_9 | not_selected | — | — | SF-2025-EDGE-LAM 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-EDGE-LAM |
| SF-2025-LLMPRISM | score_7_9 | selected | DA-LLMPRISM | — | 提供无法插桩时的生产旁路 sensor 分支，且既有 Books writeback 需要 post-write 验证。 | analysis:DA-LLMPRISM |
| SF-2025-SOLO | score_7_9 | not_selected | — | — | SF-2025-SOLO 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-SOLO |
| SF-2025-RNB | score_7_9 | not_selected | — | — | SF-2025-RNB 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-RNB |
| SF-2025-DISTRIBUTED-RAG | score_7_9 | not_selected | — | — | SF-2025-DISTRIBUTED-RAG 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-DISTRIBUTED-RAG |
| SF-2025-PROPERTY-DRIVEN-ML | score_7_9 | not_selected | — | — | SF-2025-PROPERTY-DRIVEN-ML 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-PROPERTY-DRIVEN-ML |
| SF-2025-FREQKV | score_7_9 | not_selected | — | — | SF-2025-FREQKV 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-FREQKV |
| SF-2025-ROLE-SEPARATION-SHORTCUTS | score_7_9 | not_selected | — | — | SF-2025-ROLE-SEPARATION-SHORTCUTS 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-ROLE-SEPARATION-SHORTCUTS |
| SF-2025-AGENT-MEMORY-OPERATIONS | score_7_9 | not_selected | — | — | SF-2025-AGENT-MEMORY-OPERATIONS 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-LLMPRISM, SF-2025-MCMCOMM, SF-2025-AVA 的 owner 或跨层变化。 | analysis-decision:SF-2025-AGENT-MEMORY-OPERATIONS |

<!-- analysis:DA-MCMCOMM:start -->### DA-MCMCOMM

把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-MCMCOMM:end -->

<!-- analysis:DA-AVA:start -->### DA-AVA

长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。作者以 3 秒片段生成描述并做语义合并，构造事件/实体/时间图，再用多视图检索、MCTS 与 self-consistency 回答。AVA-100 只覆盖八段长视频和 120 个问题；描述误差、图陈旧与搜索成本会累积，不能外推为通用实时视频理解。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-AVA:end -->

<!-- analysis:DA-LLMPRISM:start -->### DA-LLMPRISM

当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。论文从交换机/host 网络流推断训练任务、并行策略与阶段，并报告自 2024-10 的生产部署经验。作者的识别率和时间线误差只属于其平台与流量合同；旁路传感无法证明模型正确，也可能被共享流量或版本漂移混淆。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-LLMPRISM:end -->

<!-- analysis-decision:SF-2025-PROMPT-COMPRESSION:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-PROMPT-COMPRESSION:end -->

<!-- analysis-decision:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

<!-- analysis-decision:SF-2025-NEMOTRON-TOOL-N1:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-NEMOTRON-TOOL-N1:end -->

<!-- analysis-decision:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

<!-- analysis-decision:SF-2025-EMBEDDING-QUANTIZATION:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-EMBEDDING-QUANTIZATION:end -->

<!-- analysis-decision:SF-2025-WHOWHEN:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-WHOWHEN:end -->

<!-- analysis-decision:SF-2025-ML-DRIFT:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-ML-DRIFT:end -->

<!-- analysis-decision:SF-2025-TRAJ-BOOTSTRAP:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- analysis-decision:SF-2025-EDGE-LAM:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-EDGE-LAM:end -->

<!-- analysis-decision:SF-2025-SOLO:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-SOLO:end -->

<!-- analysis-decision:SF-2025-RNB:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-RNB:end -->

<!-- analysis-decision:SF-2025-DISTRIBUTED-RAG:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-DISTRIBUTED-RAG:end -->

<!-- analysis-decision:SF-2025-PROPERTY-DRIVEN-ML:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-PROPERTY-DRIVEN-ML:end -->

<!-- analysis-decision:SF-2025-FREQKV:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-FREQKV:end -->

<!-- analysis-decision:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

<!-- analysis-decision:SF-2025-AGENT-MEMORY-OPERATIONS:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-HAACS | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L269 | books/part-07-agent/81-workflow.md#L531 | existing:SF-2025-HAACS | delta:SF-2025-HAACS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-HAACS |
| SF-2025-PROMPT-COMPRESSION | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L559 | books/part-07-agent/75-context.md#L397 | existing:SF-2025-PROMPT-COMPRESSION | delta:SF-2025-PROMPT-COMPRESSION | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-PROMPT-COMPRESSION |
| SF-2025-PRETRAIN-DATA-MEMBERSHIP | TRAIN-DATA | books/part-04-training-system/27-data.md#L762 | books/part-06-ai-infrastructure/72-security.md#L425 | existing:SF-2025-PRETRAIN-DATA-MEMBERSHIP | delta:SF-2025-PRETRAIN-DATA-MEMBERSHIP | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP |
| SF-2025-NEMOTRON-TOOL-N1 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L440 | books/part-04-training-system/33-grpo.md#L1401 | existing:SF-2025-NEMOTRON-TOOL-N1 | delta:SF-2025-NEMOTRON-TOOL-N1 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-NEMOTRON-TOOL-N1 |
| SF-2025-MCMCOMM | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L416 | books/part-04-training-system/36-distributed-training.md#L652 | existing:SF-2025-MCMCOMM | delta:SF-2025-MCMCOMM | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-MCMCOMM |
| SF-2025-CONSENS-CONTEXT-GROUNDING | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1174 | books/part-07-agent/76-rag.md#L592 | existing:SF-2025-CONSENS-CONTEXT-GROUNDING | delta:SF-2025-CONSENS-CONTEXT-GROUNDING | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-CONSENS-CONTEXT-GROUNDING |
| SF-2025-EMBEDDING-QUANTIZATION | AGENT-RAG | books/part-07-agent/76-rag.md#L592 | books/part-05-inference-system/54-gpu-memory.md#L186 | existing:SF-2025-EMBEDDING-QUANTIZATION | delta:SF-2025-EMBEDDING-QUANTIZATION | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-EMBEDDING-QUANTIZATION |
| SF-2025-WHOWHEN | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L180 | books/part-06-ai-infrastructure/67-monitoring.md#L596; books/part-07-agent/82-multi-agent.md#L861 | existing:SF-2025-WHOWHEN | delta:SF-2025-WHOWHEN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-WHOWHEN |
| SF-2025-ML-DRIFT | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L20 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L481; books/part-05-inference-system/54-gpu-memory.md#L629 | existing:SF-2025-ML-DRIFT | delta:SF-2025-ML-DRIFT | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-ML-DRIFT |
| SF-2025-TRAJ-BOOTSTRAP | AGENT-MEMORY | books/part-07-agent/77-memory.md#L800 | books/part-07-agent/76-rag.md#L726; books/part-07-agent/81-workflow.md#L791 | existing:SF-2025-TRAJ-BOOTSTRAP | delta:SF-2025-TRAJ-BOOTSTRAP | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-TRAJ-BOOTSTRAP |
| SF-2025-AVA | AGENT-RAG | books/part-07-agent/76-rag.md#L521 | books/part-07-agent/75-context.md#L397; books/part-07-agent/77-memory.md#L20 | existing:SF-2025-AVA | delta:SF-2025-AVA | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-AVA |
| SF-2025-ENRONQA | AGENT-RAG | books/part-07-agent/76-rag.md#L726 | books/part-07-agent/75-context.md#L295; books/part-06-ai-infrastructure/71-multi-tenant.md#L183 | existing:SF-2025-ENRONQA | delta:SF-2025-ENRONQA | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-ENRONQA |
| SF-2025-MOSA | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L756 | books/part-02-model/15-multi-head-attention.md#L237; books/part-05-inference-system/49-tensorrt-llm.md#L1522 | existing:SF-2025-MOSA | delta:SF-2025-MOSA | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-MOSA |
| SF-2025-EDGE-LAM | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L294 | books/part-06-ai-infrastructure/61-kserve.md#L104 | existing:SF-2025-EDGE-LAM | delta:SF-2025-EDGE-LAM | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-EDGE-LAM |
| SF-2025-T2VPHYS | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L857 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L598; books/part-06-ai-infrastructure/66-evaluation-system.md#L2773 | existing:SF-2025-T2VPHYS | delta:SF-2025-T2VPHYS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-T2VPHYS |
| SF-2025-LLMPRISM | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L319 | books/part-06-ai-infrastructure/66-evaluation-system.md#L303; books/part-06-ai-infrastructure/68-logging.md#L130 | existing:SF-2025-LLMPRISM | delta:SF-2025-LLMPRISM | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-LLMPRISM |
| SF-2025-SOLO | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L559 | books/part-04-training-system/27-data.md#L762; books/part-04-training-system/29-sft.md#L560 | existing:SF-2025-SOLO | delta:SF-2025-SOLO | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-SOLO |
| SF-2025-RNB | TRAIN-DATA | books/part-04-training-system/27-data.md#L910 | books/part-04-training-system/28-pretraining.md#L1107; books/part-06-ai-infrastructure/66-evaluation-system.md#L2773 | existing:SF-2025-RNB | delta:SF-2025-RNB | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-RNB |
| SF-2025-SACFL | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L294 | books/part-06-ai-infrastructure/60-training-operator.md#L145 | existing:SF-2025-SACFL | delta:SF-2025-SACFL | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-SACFL |
| SF-2025-DISTRIBUTED-RAG | AGENT-RAG | books/part-07-agent/76-rag.md#L529 | books/part-07-agent/75-context.md#L397; books/part-07-agent/77-memory.md#L128 | existing:SF-2025-DISTRIBUTED-RAG | delta:SF-2025-DISTRIBUTED-RAG | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-DISTRIBUTED-RAG |
| SF-2025-MEMORY-CENTRIC-COMPUTING | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L333 | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L253 | existing:SF-2025-MEMORY-CENTRIC-COMPUTING | delta:SF-2025-MEMORY-CENTRIC-COMPUTING | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-MEMORY-CENTRIC-COMPUTING |
| SF-2025-PROPERTY-DRIVEN-ML | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L242 | books/part-06-ai-infrastructure/66-evaluation-system.md#L78 | existing:SF-2025-PROPERTY-DRIVEN-ML | delta:SF-2025-PROPERTY-DRIVEN-ML | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-PROPERTY-DRIVEN-ML |
| SF-2025-HALLUMIX | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L2773 | books/part-06-ai-infrastructure/67-monitoring.md#L596; books/part-06-ai-infrastructure/72-security.md#L1741 | existing:SF-2025-HALLUMIX | delta:SF-2025-HALLUMIX | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-HALLUMIX |
| SF-2025-FREQKV | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L481 | books/part-02-model/22-long-context.md#L756; books/part-05-inference-system/47-pagedattention.md#L184 | existing:SF-2025-FREQKV | delta:SF-2025-FREQKV | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-FREQKV |
| SF-2025-ROLE-SEPARATION-SHORTCUTS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1197 | books/part-07-agent/74-prompt.md#L209 | existing:SF-2025-ROLE-SEPARATION-SHORTCUTS | delta:SF-2025-ROLE-SEPARATION-SHORTCUTS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS |
| SF-2025-AGENT-MEMORY-OPERATIONS | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1185 | books/part-07-agent/75-context.md#L397 | existing:SF-2025-AGENT-MEMORY-OPERATIONS | delta:SF-2025-AGENT-MEMORY-OPERATIONS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-AGENT-MEMORY-OPERATIONS |

<!-- books-review:SF-2025-HAACS:start --><!-- existing:SF-2025-HAACS:start -->Multi-Agent 已要求 coordination state、owner 与 commit transition 分离，Workflow 章也把并行 DAG、task、placement 与 commit 拆开。<!-- existing:SF-2025-HAACS:end --><!-- delta:SF-2025-HAACS:start -->把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。<!-- delta:SF-2025-HAACS:end -->

这是 position paper 与综合性架构主张，没有实现 artifact 或端到端实证；只能作为 owner-boundary 提案，不能把 HE2-Net 视为已验证的生产协调协议。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-HAACS:end -->

<!-- books-review:SF-2025-PROMPT-COMPRESSION:start --><!-- existing:SF-2025-PROMPT-COMPRESSION:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PROMPT-COMPRESSION:end --><!-- delta:SF-2025-PROMPT-COMPRESSION:start -->把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。<!-- delta:SF-2025-PROMPT-COMPRESSION:end -->

经验结果绑定论文模型与任务，不构成跨模型最优压缩率或长上下文质量定律。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PROMPT-COMPRESSION:end -->

<!-- books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start --><!-- existing:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end --><!-- delta:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。<!-- delta:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

membership inference 是统计 sensor；论文数据和模型上的结果不能证明某个未披露训练集成员关系，更不能替代法律许可判断。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

<!-- books-review:SF-2025-NEMOTRON-TOOL-N1:start --><!-- existing:SF-2025-NEMOTRON-TOOL-N1:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-NEMOTRON-TOOL-N1:end --><!-- delta:SF-2025-NEMOTRON-TOOL-N1:start -->把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。<!-- delta:SF-2025-NEMOTRON-TOOL-N1:end -->

结果绑定作者数据生成、工具集合和 evaluator；不能证明开放工具生态、权限副作用或分布外 schema 下同样可靠。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-NEMOTRON-TOOL-N1:end -->

<!-- books-review:SF-2025-MCMCOMM:start --><!-- existing:SF-2025-MCMCOMM:start -->GPU Memory 已把 chiplet locality 的 layout/placement 设为联合 owner，Distributed Training 也要求 topology mapping 先于执行。<!-- existing:SF-2025-MCMCOMM:end --><!-- delta:SF-2025-MCMCOMM:start -->把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。<!-- delta:SF-2025-MCMCOMM:end -->

分析与评估绑定作者的 MCM design space、模型集合及 analytical assumptions；没有公开冻结实现，不能把模拟收益外推到任意封装、互连或真实 congestion。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MCMCOMM:end -->

<!-- books-review:SF-2025-CONSENS-CONTEXT-GROUNDING:start --><!-- existing:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-CONSENS-CONTEXT-GROUNDING:end --><!-- delta:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。<!-- delta:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

验证覆盖论文数据集和 judge 配置；相关性不证明事实正确，也不能替代 retrieval-stage provenance。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

<!-- books-review:SF-2025-EMBEDDING-QUANTIZATION:start --><!-- existing:SF-2025-EMBEDDING-QUANTIZATION:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-EMBEDDING-QUANTIZATION:end --><!-- delta:SF-2025-EMBEDDING-QUANTIZATION:start -->把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。<!-- delta:SF-2025-EMBEDDING-QUANTIZATION:end -->

PCA/quantization 的收益绑定论文数据、embedding model 与索引设置；没有证明所有语义空间或 ANN backend 都保持排序。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-EMBEDDING-QUANTIZATION:end -->

<!-- books-review:SF-2025-WHOWHEN:start --><!-- existing:SF-2025-WHOWHEN:start -->Trace 章已区分 immutable event、step/agent attribution、diagnostic confidence 与因果 authority。<!-- existing:SF-2025-WHOWHEN:end --><!-- delta:SF-2025-WHOWHEN:start -->Who&When 的 all-at-once、stepwise 与 binary-search judge 已作为 failure attribution 边界被承载。<!-- delta:SF-2025-WHOWHEN:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-TRACE` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-WHOWHEN:end -->

<!-- books-review:SF-2025-ML-DRIFT:start --><!-- existing:SF-2025-ML-DRIFT:start -->Execution 章已把 logical tensor、device-specific layout、memory placement、fusion 与 prefill/decode 分支纳入 plan identity。<!-- existing:SF-2025-ML-DRIFT:end --><!-- delta:SF-2025-ML-DRIFT:start -->ML Drift 的 tensor virtualization、coordinate translation 与 stage-aware optimization 是同一机制在 heterogeneous on-device GPU 上的实现。<!-- delta:SF-2025-ML-DRIFT:end -->演进关系为 Layering / Dependency；目标 `INFER-TENSORRT-LLM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-ML-DRIFT:end -->

<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- existing:SF-2025-TRAJ-BOOTSTRAP:start -->Memory 章已把 successful trajectory 转换为可撤销 derived memory，并要求 provenance、selection、forgetting 与 held-out evaluation。<!-- existing:SF-2025-TRAJ-BOOTSTRAP:end --><!-- delta:SF-2025-TRAJ-BOOTSTRAP:start -->Traj-Bootstrap 的 database/exemplar selection 是已有 derived-memory admission 的实例。<!-- delta:SF-2025-TRAJ-BOOTSTRAP:end -->演进关系为 Direct Evolution；目标 `AGENT-MEMORY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- books-review:SF-2025-AVA:start --><!-- existing:SF-2025-AVA:start -->RAG 已有 chunk/index/provenance，但缺少持续视频流如何变成可修订事件图的完整路径。<!-- existing:SF-2025-AVA:end --><!-- delta:SF-2025-AVA:start -->补充 observation→VLM description→semantic chunk→event/entity/temporal graph→tri-view retrieval/search；graph revision 与 staleness 成为 retrieval state。<!-- delta:SF-2025-AVA:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-AVA:end -->

<!-- books-review:SF-2025-ENRONQA:start --><!-- existing:SF-2025-ENRONQA:start -->RAG 已把 tenant、ACL、corpus revision 与 retrieval receipt 纳入私有知识边界。<!-- existing:SF-2025-ENRONQA:end --><!-- delta:SF-2025-ENRONQA:start -->EnronQA 是个性化私有文档 RAG 的数据与评测案例，不新增 owner。<!-- delta:SF-2025-ENRONQA:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-ENRONQA:end -->

<!-- books-review:SF-2025-MOSA:start --><!-- existing:SF-2025-MOSA:start -->Long Context 已区分 dense fallback、content selector、position identity 与 sparse-kernel cost。<!-- existing:SF-2025-MOSA:end --><!-- delta:SF-2025-MOSA:start -->把每个 attention head 视作 expert 并按 token content 选择子集，是现有 content-based sparse branch 的实现。<!-- delta:SF-2025-MOSA:end -->演进关系 `Alternative Branch`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MOSA:end -->

<!-- books-review:SF-2025-EDGE-LAM:start --><!-- existing:SF-2025-EDGE-LAM:start -->Distributed Training 已定义 federated tensor/跨设备协议表达边界，KServe 已分离 desired/applied/observed serving state；该综述未给出新的可验证协议。<!-- existing:SF-2025-EDGE-LAM:end --><!-- delta:SF-2025-EDGE-LAM:start -->把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。<!-- delta:SF-2025-EDGE-LAM:end -->

论文主要是架构综述与 6G case study，没有完整端到端 implementation/benchmark；不能证明所述 looped TP 或 microservice migration 已满足真实 edge reliability。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-EDGE-LAM:end -->

<!-- books-review:SF-2025-T2VPHYS:start --><!-- existing:SF-2025-T2VPHYS:start -->World Model/Evaluation 已区分视频 plausibility、物理一致性、action-conditioned transition 与因果证据。<!-- existing:SF-2025-T2VPHYS:end --><!-- delta:SF-2025-T2VPHYS:start -->十二类物理规律、hint/counterfactual probe 与人工协议是既有 evaluation contract 的案例。<!-- delta:SF-2025-T2VPHYS:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-T2VPHYS:end -->

<!-- books-review:SF-2025-LLMPRISM:start --><!-- existing:SF-2025-LLMPRISM:start -->Monitoring 已有 metrics/logs/traces 与 collective telemetry，但缺少无法植入代码时的网络流序列诊断分支。<!-- existing:SF-2025-LLMPRISM:end --><!-- delta:SF-2025-LLMPRISM:start -->补充 network-flow sequence 作为低侵入 correlated sensor，用来推断训练 job identity、并行配置、phase/timeline 与 stall；它只拥有诊断线索，不拥有 correctness。<!-- delta:SF-2025-LLMPRISM:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-LLMPRISM:end -->

<!-- books-review:SF-2025-SOLO:start --><!-- existing:SF-2025-SOLO:start -->Pretraining 已有 low-precision update、error feedback 与 role-aware optimizer state，但没有解释 EMA dynamics 的两种量化失真。<!-- existing:SF-2025-SOLO:end --><!-- delta:SF-2025-SOLO:start -->补充 unsigned EMA 的 signal swamping 与 signed state 的 variance/wrong-direction 分支；量化器、momentum precision 与 checkpoint identity 必须共同冻结。<!-- delta:SF-2025-SOLO:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SOLO:end -->

<!-- books-review:SF-2025-RNB:start --><!-- existing:SF-2025-RNB:start -->Data 已把 mixture weight 视为受 gradient/coverage/evaluation 反馈约束的动态控制状态。<!-- existing:SF-2025-RNB:end --><!-- delta:SF-2025-RNB:start -->embedding+gradient regrouping 与 final-layer similarity 是该控制链的受限 estimator，不新增 owner。<!-- delta:SF-2025-RNB:end -->演进关系 `Direct Evolution`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-RNB:end -->

<!-- books-review:SF-2025-SACFL:start --><!-- existing:SF-2025-SACFL:start -->Distributed Training 已把 federated payload 定义为 typed protocol，并分开 freshness、objective 与 commit；Training Operator 已要求失败恢复保持 artifact 一致。<!-- existing:SF-2025-SACFL:end --><!-- delta:SF-2025-SACFL:start -->在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。<!-- delta:SF-2025-SACFL:end -->

实验覆盖作者选择的数据集、3-20 个任务与模拟/演示环境；论文未证明长期真实 client churn、secure aggregation 或不同硬件资源下的收敛与防御。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-SACFL:end -->

<!-- books-review:SF-2025-DISTRIBUTED-RAG:start --><!-- existing:SF-2025-DISTRIBUTED-RAG:start -->RAG 主要以中央索引为默认，已讨论 partition 和 federation，但缺少 peer-owned knowledge 的完整控制边界。<!-- existing:SF-2025-DISTRIBUTED-RAG:end --><!-- delta:SF-2025-DISTRIBUTED-RAG:start -->补充 peer-owned indexes 与 topic-aware random walk：恢复数据所有权，同时引入 query leakage、peer availability/trust、routing 与 index consistency。<!-- delta:SF-2025-DISTRIBUTED-RAG:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-DISTRIBUTED-RAG:end -->

<!-- books-review:SF-2025-MEMORY-CENTRIC-COMPUTING:start --><!-- existing:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-MEMORY-CENTRIC-COMPUTING:end --><!-- delta:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。<!-- delta:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

论文是机制综述与系统立场，不提供一个可直接泛化到所有 LLM workload 的单一实现或 benchmark 结论。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

<!-- books-review:SF-2025-PROPERTY-DRIVEN-ML:start --><!-- existing:SF-2025-PROPERTY-DRIVEN-ML:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PROPERTY-DRIVEN-ML:end --><!-- delta:SF-2025-PROPERTY-DRIVEN-ML:start -->把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。<!-- delta:SF-2025-PROPERTY-DRIVEN-ML:end -->

MNIST 与 drone 案例只验证框架可行性；不能证明 property set 完备，learned checker 也不能独占发布 authority。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PROPERTY-DRIVEN-ML:end -->

<!-- books-review:SF-2025-HALLUMIX:start --><!-- existing:SF-2025-HALLUMIX:start -->Evaluation 已把 hallucination 拆为 claim/evidence、slice、length、evaluator 与 calibration contract。<!-- existing:SF-2025-HALLUMIX:end --><!-- delta:SF-2025-HALLUMIX:start -->HalluMix 是跨 NLI/summary/QA 的 benchmark 实例，强调 sub-source overfitting 与长度效应。<!-- delta:SF-2025-HALLUMIX:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-HALLUMIX:end -->

<!-- books-review:SF-2025-FREQKV:start --><!-- existing:SF-2025-FREQKV:start -->KV/Long Context 已覆盖 feature/frequency compression、position identity、lossy error 与 FullKV fallback。<!-- existing:SF-2025-FREQKV:end --><!-- delta:SF-2025-FREQKV:start -->FreqKV 的迭代频域压缩是已有 branch 的具体 estimator，不新增运行时 owner。<!-- delta:SF-2025-FREQKV:end -->演进关系 `Alternative Branch`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-FREQKV:end -->

<!-- books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS:start --><!-- existing:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-ROLE-SEPARATION-SHORTCUTS:end --><!-- delta:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。<!-- delta:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

shortcut 分析与缓解绑定论文模型、模板和攻击；没有证明重排 position ID 能覆盖所有 provenance confusion。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

<!-- books-review:SF-2025-AGENT-MEMORY-OPERATIONS:start --><!-- existing:SF-2025-AGENT-MEMORY-OPERATIONS:start -->Memory 章已按 write/read/consolidation/forgetting、admission、visibility、recovery 与显式 state operation 展开，比该 taxonomy 更细。<!-- existing:SF-2025-AGENT-MEMORY-OPERATIONS:end --><!-- delta:SF-2025-AGENT-MEMORY-OPERATIONS:start -->把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。<!-- delta:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

这是 survey/taxonomy，不是对六个操作统一实现或 benchmark 的 primary validation；所列 tools 与未来方向不能升级为跨系统性能结论。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

Books Gate 已通过：5 项既有语义绑定经 exact-v1 与目标/相邻正文复核后记为 `verified_existing_writeback`，不重复插入。

## 7. Semantic Audit

fresh-context audit 独立于作者重建；author recheck 不作为 Gate 证据。

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20250502-COVERAGE | fresh-context:daily_2025may_fresh_audit | coverage | coverage:SRC-ARXIV:20250502 | — | 696 title+abstract identities re-read without sampling; seven false negatives moved to their owner-day retained sets and zero-hit owner ledgers were rehashed | passed |
| SA-20250502-EVIDENCE | fresh-context:daily_2025may_fresh_audit | evidence | validator:review-completion-v1 | — | all retained routes were checked against primary packets for method, evaluation, limitation, artifact and withdrawal facets | passed |
| SA-20250502-SELECTION | fresh-context:daily_2025may_fresh_audit | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | every eligible family has a day-specific selected or non-selected disposition within the three-item narrative budget | passed |
| SA-20250502-BOOKS | fresh-context:daily_2025may_fresh_audit | books | validator:books-comparison-v1 | — | five exact-v1 sources and current target/adjacent flows were rechecked in date order; existing bindings were marked verified_existing_writeback and line-one placeholders removed | passed |

## 8. Ignored Noise

295 条 pre-denominator closure 均在 `semantic-screening-ledger-v2.1.json.gz` 中保留完整 identity、title、abstract evidence、closure class 与 family-specific reason；没有评分，也没有冒充全文 Review。

## 9. Recommended Action

保持当前 owner 与 Books 语义绑定；后续只在新 primary evidence 改变长期机制边界时重新打开 Books Decision。

## 10. Repository Changes

重建 05/01–04 Daily、owner-day ledger、exact-v1 manifests、no-hit receipts、Books queue 与 fresh-context audit receipt；既有 Books 正文经验证合格，未重复修改。未 stage/commit/push。

## 11. Open Questions

- None.

## 12. Sources

- [Position Paper: Towards Open Complex Human-AI Agents Collaboration Systems for Problem Solving and Knowledge Management](https://arxiv.org/html/2505.00018v1) — exact v1；official owner `2025-05-02`。

- [An Empirical Study on Prompt Compression for Large Language Models](https://arxiv.org/html/2505.00019v1) — exact v1；official owner `2025-05-02`。

- [Beyond Public Access in LLM Pre-Training Data](https://arxiv.org/html/2505.00020v1) — exact v1；official owner `2025-05-02`。

- [Nemotron-Research-Tool-N1: Exploring Tool-Using Language Models with Reinforced Reasoning](https://arxiv.org/html/2505.00024v1) — exact v1；official owner `2025-05-02`。

- [MCMComm: Hardware-Software Co-Optimization for End-to-End Communication in Multi-Chip-Modules](https://arxiv.org/html/2505.00041v1) — exact v1；official owner `2025-05-02`。

- [ConSens: Assessing context grounding in open-book question answering](https://arxiv.org/html/2505.00065v1) — exact v1；official owner `2025-05-02`。

- [Optimization of embeddings storage for RAG systems using quantization and dimensionality reduction techniques](https://arxiv.org/html/2505.00105v1) — exact v1；official owner `2025-05-02`。

- [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/html/2505.00212v1) — exact v1；official owner `2025-05-02`。

- [Scaling On-Device GPU Inference for Large Generative Models](https://arxiv.org/html/2505.00232v1) — exact v1；official owner `2025-05-02`。

- [Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks](https://arxiv.org/html/2505.00234v1) — exact v1；official owner `2025-05-02`。

- [AVA: Towards Agentic Video Analytics with Vision Language Models](https://arxiv.org/html/2505.00254v1) — exact v1；official owner `2025-05-02`。

- [EnronQA: Towards Personalized RAG over Private Documents](https://arxiv.org/html/2505.00263v1) — exact v1；official owner `2025-05-02`。

- [Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing](https://arxiv.org/html/2505.00315v1) — exact v1；official owner `2025-05-02`。

- [Edge Large AI Models: Revolutionizing 6G Networks](https://arxiv.org/html/2505.00321v1) — exact v1；official owner `2025-05-02`。

- [T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation](https://arxiv.org/html/2505.00337v1) — exact v1；official owner `2025-05-02`。

- [LLMPrism: Black-box Performance Diagnosis for Production LLM Training Platforms](https://arxiv.org/html/2505.00342v1) — exact v1；official owner `2025-05-02`。

- [Pushing the Limits of Low-Bit Optimizers: A Focus on EMA Dynamics](https://arxiv.org/html/2505.00347v1) — exact v1；official owner `2025-05-02`。

- [R&amp;B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training](https://arxiv.org/html/2505.00358v1) — exact v1；official owner `2025-05-02`。

- [SacFL: Self-Adaptive Federated Continual Learning for Resource-Constrained End Devices](https://arxiv.org/html/2505.00365v1) — exact v1；official owner `2025-05-02`。

- [Distributed Retrieval-Augmented Generation](https://arxiv.org/html/2505.00443v1) — exact v1；official owner `2025-05-02`。

- [Memory-Centric Computing: Solving Computing's Memory Problem](https://arxiv.org/html/2505.00458v1) — exact v1；official owner `2025-05-02`。

- [A General Framework for Property-Driven Machine Learning](https://arxiv.org/html/2505.00466v1) — exact v1；official owner `2025-05-02`。

- [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/html/2505.00506v1) — exact v1；official owner `2025-05-02`。

- [FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](https://arxiv.org/html/2505.00570v1) — exact v1；official owner `2025-05-02`。

- [The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (and How to Fix Them)](https://arxiv.org/html/2505.00626v1) — exact v1；official owner `2025-05-02`。

- [Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics](https://arxiv.org/html/2505.00675v1) — exact v1；official owner `2025-05-02`。

## 13. Final Status

- Completion Status = `Complete`
- Coverage = `Closed`
- Evidence = `Passed`
- Books = `Passed`
- unresolved findings = 0
