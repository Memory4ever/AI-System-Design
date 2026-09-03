# Daily Research — 2025-05-01

**Research Date:** 2025-05-01

**Timezone:** Asia/Shanghai

**Strict Window:** 2025-04-30 09:00:00 ～ 2025-05-01 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Historical Daily Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。fresh-context reviewer 已完成全量语义复核、exact-v1 证据验收与 post-write Books audit。

## Executive Summary

官方 announcement owner 分母为 375；全量逐行读取 title+abstract 后保留 22 个 family，关闭 353 条，withdrawn/removed exact-v1 为 0，blocked evidence 为 0。未使用 Weekly 作 discovery、筛选、评分、Review 或 Books 证据。7 个初始 closure false negative 已纠正；所有 current-content comparison 与 Gate 已由 fresh-context reviewer 验收。

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
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20250501-887af4a41aa52c033829 |
| Denominator Frozen At | 2026-09-03T21:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2025-04-30T09:00:00+08:00 | 2025-05-01T09:00:00+08:00 | 2026-09-03T21:15:00+08:00 | official announcement owner recovery; owner_report_date=2025-05-01 | checked | 375 | SF-2025-DONT-RETRIEVE-GENERATE<br>SF-2025-WEBEVOLVER<br>SF-2025-SAGA-IDENTITY<br>SF-2025-SEMANTIC-REIDENTIFICATION<br>SF-2025-DP-FINETUNING-PRIVACY<br>SF-2025-PREFILL-JAILBREAK<br>SF-2025-LEGILIMENS<br>SF-2025-SECREPOBENCH<br>SF-2025-CACHEPRUNE<br>SF-2025-BAYES-EVAL-CONFIDENCE<br>SF-2025-PHI4-REASONING<br>SF-2025-NEXUS-GEN<br>SF-2025-SHORTERBETTER<br>SF-2025-GALVATRON<br>SF-2025-RWKV-X<br>SF-2025-MCITY-DATA-ENGINE<br>SF-2025-RAGFORENSICS<br>SF-2025-MUTEDRAG-AVAILABILITY<br>SF-2025-VDDP<br>SF-2025-WEBTHINKER<br>SF-2025-SWE-SMITH<br>SF-2025-DEEPSEEK-PROVER-V2 | pages=1; final_cursor=end; rows=375 | 2025-05-01T09:00:00+08:00 | coverage:SRC-ARXIV:20250501 | — |

<!-- coverage:SRC-ARXIV:20250501:start -->owner inventory SHA prefix `887af4a41aa52c033829`；semantic ledger SHA prefix `d95014148273eae118f7`；算术 `375 = 22 retained + 353 closures`。<!-- coverage:SRC-ARXIV:20250501:end -->

### Coverage Limitations

注册表晚于历史窗口；本次只对可复现的官方 announcement owner inventory 作完整论文 recall。组织来源若无历史枚举证据，不伪造 retroactive no-hit。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-DONT-RETRIEVE-GENERATE | arXiv:2504.21015v1 | paper-v1:2504.21015 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-DONT-RETRIEVE-GENERATE | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2025-DONT-RETRIEVE-GENERATE | no |
| SF-2025-WEBEVOLVER | arXiv:2504.21024v1 | paper-v1:2504.21024 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-WEBEVOLVER | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2025-WEBEVOLVER | no |
| SF-2025-SAGA-IDENTITY | arXiv:2504.21034v1 | paper-v1:2504.21034 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-SAGA-IDENTITY | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2025-SAGA-IDENTITY | no |
| SF-2025-SEMANTIC-REIDENTIFICATION | arXiv:2504.21035v1 | paper-v1:2504.21035 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-SEMANTIC-REIDENTIFICATION | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-SEMANTIC-REIDENTIFICATION | no |
| SF-2025-DP-FINETUNING-PRIVACY | arXiv:2504.21036v1 | paper-v1:2504.21036 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-DP-FINETUNING-PRIVACY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-DP-FINETUNING-PRIVACY | no |
| SF-2025-PREFILL-JAILBREAK | arXiv:2504.21038v1 | paper-v1:2504.21038 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-PREFILL-JAILBREAK | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-PREFILL-JAILBREAK | no |
| SF-2025-LEGILIMENS | arXiv:2504.21136v1 | paper-v1:2504.21136 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-LEGILIMENS | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2025-LEGILIMENS | no |
| SF-2025-SECREPOBENCH | arXiv:2504.21205v1 | paper-v1:2504.21205 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-SECREPOBENCH | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-SECREPOBENCH | no |
| SF-2025-CACHEPRUNE | arXiv:2504.21228v1 | paper-v1:2504.21228 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-CACHEPRUNE | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-CACHEPRUNE | no |
| SF-2025-BAYES-EVAL-CONFIDENCE | arXiv:2504.21303v1 | paper-v1:2504.21303 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-BAYES-EVAL-CONFIDENCE | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2025-BAYES-EVAL-CONFIDENCE | yes |
| SF-2025-PHI4-REASONING | arXiv:2504.21318v1 | paper-v1:2504.21318 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-PHI4-REASONING | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2025-PHI4-REASONING | yes |
| SF-2025-NEXUS-GEN | arXiv:2504.21356v1 | paper-v1:2504.21356 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-NEXUS-GEN | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2025-NEXUS-GEN | no |
| SF-2025-SHORTERBETTER | arXiv:2504.21370v1 | paper-v1:2504.21370 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-SHORTERBETTER | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2025-SHORTERBETTER | yes |
| SF-2025-GALVATRON | arXiv:2504.21411v1 | paper-v1:2504.21411 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2025-GALVATRON | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2025-GALVATRON | yes |
| SF-2025-RWKV-X | arXiv:2504.21463v1 | paper-v1:2504.21463 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2025-RWKV-X | self | — | new_in_window | MODEL-LONG-CONTEXT | No Change — Existing Coverage | books-review:SF-2025-RWKV-X | yes |
| SF-2025-MCITY-DATA-ENGINE | arXiv:2504.21614v1 | paper-v1:2504.21614 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-MCITY-DATA-ENGINE | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2025-MCITY-DATA-ENGINE | no |
| SF-2025-RAGFORENSICS | arXiv:2504.21668v1 | paper-v1:2504.21668 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-RAGFORENSICS | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-RAGFORENSICS | yes |
| SF-2025-MUTEDRAG-AVAILABILITY | arXiv:2504.21680v1 | paper-v1:2504.21680 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2025-MUTEDRAG-AVAILABILITY | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-MUTEDRAG-AVAILABILITY | yes |
| SF-2025-VDDP | arXiv:2504.21752v1 | paper-v1:2504.21752 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-VDDP | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2025-VDDP | yes |
| SF-2025-WEBTHINKER | arXiv:2504.21776v1 | paper-v1:2504.21776 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2025-WEBTHINKER | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2025-WEBTHINKER | yes |
| SF-2025-SWE-SMITH | arXiv:2504.21798v1 | paper-v1:2504.21798 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-SWE-SMITH | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2025-SWE-SMITH | yes |
| SF-2025-DEEPSEEK-PROVER-V2 | arXiv:2504.21801v1 | paper-v1:2504.21801 | 2025-W18 | 2025-05-01 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2025-DEEPSEEK-PROVER-V2 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2025-DEEPSEEK-PROVER-V2 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-DONT-RETRIEVE-GENERATE | RP-e4f3b8a4251c64f5 | deep | arXiv:2504.21015v1 | SRC-ARXIV@arXiv:2504.21015v1 | https://arxiv.org/html/2504.21015v1#S3 | https://arxiv.org/html/2504.21015v1#S5 | https://arxiv.org/html/2504.21015v1#S8 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-DONT-RETRIEVE-GENERATE | complete |
| SF-2025-WEBEVOLVER | RP-9b2a0b18a981d516 | deep | arXiv:2504.21024v1 | SRC-ARXIV@arXiv:2504.21024v1 | https://arxiv.org/html/2504.21024v1#S3 | https://arxiv.org/html/2504.21024v1#S4 | https://arxiv.org/html/2504.21024v1#S5 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-WEBEVOLVER | complete |
| SF-2025-SAGA-IDENTITY | RP-b66c6fd1e3cad531 | deep | arXiv:2504.21034v1 | SRC-ARXIV@arXiv:2504.21034v1 | https://arxiv.org/html/2504.21034v1#S3 | https://arxiv.org/html/2504.21034v1#S5 | https://arxiv.org/html/2504.21034v1#S7 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-SAGA-IDENTITY | complete |
| SF-2025-SEMANTIC-REIDENTIFICATION | RP-677a849b2b0bd2a1 | deep | arXiv:2504.21035v1 | SRC-ARXIV@arXiv:2504.21035v1 | https://arxiv.org/html/2504.21035v1#S3 | https://arxiv.org/html/2504.21035v1#S5 | https://arxiv.org/html/2504.21035v1#A1 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-SEMANTIC-REIDENTIFICATION | complete |
| SF-2025-DP-FINETUNING-PRIVACY | RP-14a323b8cdd47a78 | deep | arXiv:2504.21036v1 | SRC-ARXIV@arXiv:2504.21036v1 | https://arxiv.org/html/2504.21036v1#S3 | https://arxiv.org/html/2504.21036v1#S4 | https://arxiv.org/html/2504.21036v1#S5 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-DP-FINETUNING-PRIVACY | complete |
| SF-2025-PREFILL-JAILBREAK | RP-c2b38b58b90cac66 | deep | arXiv:2504.21038v1 | SRC-ARXIV@arXiv:2504.21038v1 | https://arxiv.org/html/2504.21038v1#S3 | https://arxiv.org/html/2504.21038v1#S4 | https://arxiv.org/html/2504.21038v1#S5 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-PREFILL-JAILBREAK | complete |
| SF-2025-LEGILIMENS | RP-7a1c8373eec6ac45 | deep | arXiv:2504.21136v1 | SRC-ARXIV@arXiv:2504.21136v1 | https://arxiv.org/pdf/2504.21136v1 — PDF p.4-9 (§3-4) | https://arxiv.org/pdf/2504.21136v1 — PDF p.10-12 (§5) | https://arxiv.org/pdf/2504.21136v1 — PDF p.16 (Appendix A.1) | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-LEGILIMENS | complete |
| SF-2025-SECREPOBENCH | RP-33aea37b5b016ff8 | deep | arXiv:2504.21205v1 | SRC-ARXIV@arXiv:2504.21205v1 | https://arxiv.org/html/2504.21205v1#S3 | https://arxiv.org/html/2504.21205v1#S5 | https://arxiv.org/html/2504.21205v1#S6 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-SECREPOBENCH | complete |
| SF-2025-CACHEPRUNE | RP-6d509a6eea5a9bc5 | deep | arXiv:2504.21228v1 | SRC-ARXIV@arXiv:2504.21228v1 | https://arxiv.org/html/2504.21228v1#S2 | https://arxiv.org/html/2504.21228v1#S4 | https://arxiv.org/html/2504.21228v1#S5 | Not Disclosed — exact-v1 does not identify a frozen implementation artifact | claim:SF-2025-CACHEPRUNE | complete |
| SF-2025-BAYES-EVAL-CONFIDENCE | RP-de7762d3e11b71a2 | deep | arXiv:2504.21303v1 | SRC-ARXIV@arXiv:2504.21303v1 | https://arxiv.org/html/2504.21303v1#S2; https://arxiv.org/html/2504.21303v1#S2.SS2 | https://arxiv.org/html/2504.21303v1#S3; https://arxiv.org/html/2504.21303v1#S4 | https://arxiv.org/html/2504.21303v1#S5.SS1 | Not Disclosed — exact-v1 does not identify a released evaluation implementation | claim:SF-2025-BAYES-EVAL-CONFIDENCE | complete |
| SF-2025-PHI4-REASONING | RP-411e602703ccd78d | standard | arXiv:2504.21318v1 | SRC-ARXIV@arXiv:2504.21318v1 | https://arxiv.org/html/2504.21318v1#S2; https://arxiv.org/html/2504.21318v1#S3; https://arxiv.org/html/2504.21318v1#S4 | https://arxiv.org/html/2504.21318v1#S5; https://arxiv.org/html/2504.21318v1#A1 | https://arxiv.org/html/2504.21318v1#S6 | https://github.com/microsoft/eureka-ml-insights — linked evaluation artifact; full training stack Not Disclosed | claim:SF-2025-PHI4-REASONING | complete |
| SF-2025-NEXUS-GEN | RP-955bd54a77a598c9 | standard | arXiv:2504.21356v1 | SRC-ARXIV@arXiv:2504.21356v1 | https://arxiv.org/html/2504.21356v1#S2.SS1; https://arxiv.org/html/2504.21356v1#S2.SS2; https://arxiv.org/html/2504.21356v1#S2.SS3 | https://arxiv.org/html/2504.21356v1#S3 | Not Disclosed — exact-v1 has no dedicated limitations section and provides qualitative case studies rather than a matched broad benchmark | https://github.com/modelscope/Nexus-Gen.git — repository linked from exact-v1 | claim:SF-2025-NEXUS-GEN | complete |
| SF-2025-SHORTERBETTER | RP-e3601e7d52483958 | standard | arXiv:2504.21370v1 | SRC-ARXIV@arXiv:2504.21370v1 | https://arxiv.org/html/2504.21370v1#S3 | https://arxiv.org/html/2504.21370v1#S4; https://arxiv.org/html/2504.21370v1#S5 | https://arxiv.org/html/2504.21370v1#S5.SS2; https://arxiv.org/html/2504.21370v1#S6 | Not Disclosed — exact-v1 does not identify a released implementation artifact | claim:SF-2025-SHORTERBETTER | complete |
| SF-2025-GALVATRON | RP-6bc469a12b841ae7 | deep | arXiv:2504.21411v1 | SRC-ARXIV@arXiv:2504.21411v1 | https://arxiv.org/html/2504.21411v1#S2; https://arxiv.org/html/2504.21411v1#S3 | https://arxiv.org/html/2504.21411v1#S4 | https://arxiv.org/html/2504.21411v1#S5 | https://github.com/PKU-DAIR/Hetu-Galvatron — repository linked from exact-v1 | claim:SF-2025-GALVATRON | complete |
| SF-2025-RWKV-X | RP-1af627e257ae741d | standard | arXiv:2504.21463v1 | SRC-ARXIV@arXiv:2504.21463v1 | https://arxiv.org/html/2504.21463v1#S3; https://arxiv.org/html/2504.21463v1#S3.SS2.SSS1 | https://arxiv.org/html/2504.21463v1#S4; https://arxiv.org/html/2504.21463v1#A2 | https://arxiv.org/html/2504.21463v1#S5; https://arxiv.org/html/2504.21463v1#A3 | https://github.com/howard-hou/RWKV-X — repository linked from exact-v1 | claim:SF-2025-RWKV-X | complete |
| SF-2025-MCITY-DATA-ENGINE | RP-70167cacea28a32d | deep | arXiv:2504.21614v1 | SRC-ARXIV@arXiv:2504.21614v1 | https://arxiv.org/html/2504.21614v1#S3 | https://arxiv.org/html/2504.21614v1#S4 | https://arxiv.org/html/2504.21614v1#S5 | https://github.com/mcity/mcity_data_engine — repository linked from exact-v1; revision not frozen | claim:SF-2025-MCITY-DATA-ENGINE | complete |
| SF-2025-RAGFORENSICS | RP-8b9076005e419bd4 | deep | arXiv:2504.21668v1 | SRC-ARXIV@arXiv:2504.21668v1 | https://arxiv.org/html/2504.21668v1#S3; https://arxiv.org/html/2504.21668v1#S4 | https://arxiv.org/html/2504.21668v1#S5 | https://arxiv.org/html/2504.21668v1#S6; https://arxiv.org/html/2504.21668v1#S7 | Not Disclosed — exact-v1 does not identify a released artifact | claim:SF-2025-RAGFORENSICS | complete |
| SF-2025-MUTEDRAG-AVAILABILITY | RP-a1627173a1b750f0 | deep | arXiv:2504.21680v1 | SRC-ARXIV@arXiv:2504.21680v1 | https://arxiv.org/html/2504.21680v1#S3 | https://arxiv.org/html/2504.21680v1#S4 | https://arxiv.org/html/2504.21680v1#S5; https://arxiv.org/html/2504.21680v1#S6 | Not Disclosed — exact-v1 does not identify a frozen public attack/evaluation artifact | claim:SF-2025-MUTEDRAG-AVAILABILITY | complete |
| SF-2025-VDDP | RP-1b977aaae526e795 | deep | arXiv:2504.21752v1 | SRC-ARXIV@arXiv:2504.21752v1 | https://arxiv.org/pdf/2504.21752v1 — §3 Problem Formulation; §4 Verifiable Distributed Discrete Laplace Mechanism; §5 Verifiable Randomized Response | https://arxiv.org/pdf/2504.21752v1 — §6 Evaluation | https://arxiv.org/pdf/2504.21752v1 — §8 Conclusion and Open Questions; Appendix C.5 | Artifact announced for publication at https://github.com/sjtu-ipads/VDDP ; no frozen exact-v1 artifact was available for this review | claim:SF-2025-VDDP | complete |
| SF-2025-WEBTHINKER | RP-4d28dd4a6d4823ef | deep | arXiv:2504.21776v1 | SRC-ARXIV@arXiv:2504.21776v1 | https://arxiv.org/html/2504.21776v1#S3; https://arxiv.org/html/2504.21776v1#A1 | https://arxiv.org/html/2504.21776v1#S4; https://arxiv.org/html/2504.21776v1#S4.SS7 | https://arxiv.org/html/2504.21776v1#S5; https://arxiv.org/html/2504.21776v1#A3.SS4 | https://github.com/RUC-NLPIR/WebThinker — repository linked from exact-v1 | claim:SF-2025-WEBTHINKER | complete |
| SF-2025-SWE-SMITH | RP-0f6e83d3a721560f | deep | arXiv:2504.21798v1 | SRC-ARXIV@arXiv:2504.21798v1 | https://arxiv.org/html/2504.21798v1#S2; https://arxiv.org/html/2504.21798v1#A1; https://arxiv.org/html/2504.21798v1#A2 | https://arxiv.org/html/2504.21798v1#S3; https://arxiv.org/html/2504.21798v1#S4; https://arxiv.org/html/2504.21798v1#A6 | https://arxiv.org/html/2504.21798v1#S6; https://arxiv.org/html/2504.21798v1#A6.SS3.SSS3 | https://github.com/SWE-bench/SWE-smith — official repository identified by the manuscript/project | claim:SF-2025-SWE-SMITH | complete |
| SF-2025-DEEPSEEK-PROVER-V2 | RP-a394ed1d348c25ee | deep | arXiv:2504.21801v1 | SRC-ARXIV@arXiv:2504.21801v1 | https://arxiv.org/html/2504.21801v1#S2; https://arxiv.org/html/2504.21801v1#S2.SS1 | https://arxiv.org/html/2504.21801v1#S3; https://arxiv.org/html/2504.21801v1#S3.SS4 | https://arxiv.org/html/2504.21801v1#S4; https://arxiv.org/html/2504.21801v1#A3 | https://github.com/deepseek-ai/DeepSeek-Prover-V2 — official repository linked from exact-v1 | claim:SF-2025-DEEPSEEK-PROVER-V2 | complete |

### Source Reviews

<!-- review:SF-2025-DONT-RETRIEVE-GENERATE:start --><!-- claim:SF-2025-DONT-RETRIEVE-GENERATE:start -->把 RAG 训练数据来源从只检索公开问答扩展为可控生成的 hypothetical negatives；关键系统边界是生成器版本、去重、污染审计与真实检索回放必须共同冻结。<!-- claim:SF-2025-DONT-RETRIEVE-GENERATE:end -->

作者实验只比较其合成 hard-negative recipe 与披露数据集，不能证明生成数据普遍优于真实 retrieval logs。<!-- review:SF-2025-DONT-RETRIEVE-GENERATE:end -->

<!-- review:SF-2025-WEBEVOLVER:start --><!-- claim:SF-2025-WEBEVOLVER:start -->把 web agent 自我改进拆成 evolving policy 与 co-evolving environment model，说明 rollout 数据、网页状态和 evaluator revision 必须作为同一训练 identity 管理。<!-- claim:SF-2025-WEBEVOLVER:end -->

结果绑定作者构造的 web environment 与任务；没有证明开放互联网漂移、权限边界或真实副作用下仍能安全自演化。<!-- review:SF-2025-WEBEVOLVER:end -->

<!-- review:SF-2025-SAGA-IDENTITY:start --><!-- claim:SF-2025-SAGA-IDENTITY:start -->把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。<!-- claim:SF-2025-SAGA-IDENTITY:end -->

论文给出协议与原型评估，不等于互联网规模身份联邦、密钥轮换、撤权传播或恶意参与方下已经安全。<!-- review:SF-2025-SAGA-IDENTITY:end -->

<!-- review:SF-2025-SEMANTIC-REIDENTIFICATION:start --><!-- claim:SF-2025-SEMANTIC-REIDENTIFICATION:start -->证明移除显式 PII 或生成 synthetic text 并不关闭语义再识别通道；privacy boundary 必须绑定攻击者辅助信息、关系特征与 release surface。<!-- claim:SF-2025-SEMANTIC-REIDENTIFICATION:end -->

攻击成功率只对论文披露的数据、模型与辅助信息成立，不能外推为所有去标识化文本都可被同等重识别。<!-- review:SF-2025-SEMANTIC-REIDENTIFICATION:end -->

<!-- review:SF-2025-DP-FINETUNING-PRIVACY:start --><!-- claim:SF-2025-DP-FINETUNING-PRIVACY:start -->把 private fine-tuning 的证据从单一 utility 指标扩展为多种攻击面、机制参数与 privacy-utility slice；accountant、实现路径和攻击者能力必须同构。<!-- claim:SF-2025-DP-FINETUNING-PRIVACY:end -->

比较覆盖论文列出的 DP 方法与攻击，不能证明未测攻击、不同基础模型或部署精度具有相同 privacy guarantee。<!-- review:SF-2025-DP-FINETUNING-PRIVACY:end -->

<!-- review:SF-2025-PREFILL-JAILBREAK:start --><!-- claim:SF-2025-PREFILL-JAILBREAK:start -->把 jailbreak 攻击面推进到 assistant prefill：请求在 decode 前已携带带角色语义的生成状态，因此 API normalization、template ownership 与 prefill policy 都属于安全边界。<!-- claim:SF-2025-PREFILL-JAILBREAK:end -->

攻击结果绑定被测模型、模板与访问方式；不证明所有 prefill API 都同样脆弱，也不把检测器提升为最终 authority。<!-- review:SF-2025-PREFILL-JAILBREAK:end -->

<!-- review:SF-2025-LEGILIMENS:start --><!-- claim:SF-2025-LEGILIMENS:start -->把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。<!-- claim:SF-2025-LEGILIMENS:end -->

评估只覆盖作者的 50 小时视频、两类视觉任务与 Jetson SoC；多 base 结果依赖 oracle selection，且额外 base 会线性增加 memory，不能外推到任意 edge workload。<!-- review:SF-2025-LEGILIMENS:end -->

<!-- review:SF-2025-SECREPOBENCH:start --><!-- claim:SF-2025-SECREPOBENCH:start -->把 secure code completion 的评估对象从孤立片段推进到真实 repository、dependency context、unit tests 与 repair trace；安全声明必须绑定可执行 project identity。<!-- claim:SF-2025-SECREPOBENCH:end -->

benchmark 覆盖作者收集的仓库与漏洞类别；unit tests 不是完整安全证明，agent repair 成功也不保证无新缺陷。<!-- review:SF-2025-SECREPOBENCH:end -->

<!-- review:SF-2025-CACHEPRUNE:start --><!-- claim:SF-2025-CACHEPRUNE:start -->利用 KV-cache attribution 定位并削弱 prompt-injection influence，说明中间状态可以成为安全 sensor；但 eviction/pruning policy 必须保留 utility gate 与完整上下文 fallback。<!-- claim:SF-2025-CACHEPRUNE:end -->

防御只在披露模型、攻击与任务上评估；attribution signal 不是输入恶意性的真值，错误 pruning 可能删除任务关键语义。<!-- review:SF-2025-CACHEPRUNE:end -->

<!-- review:SF-2025-BAYES-EVAL-CONFIDENCE:start --><!-- claim:SF-2025-BAYES-EVAL-CONFIDENCE:start -->有限 query 上的模型排序必须输出 posterior uncertainty，并把 prior、anchor model、query construction 和 judge 一起纳入 evaluation identity；高 posterior 不是跨分布正确性证明。<!-- claim:SF-2025-BAYES-EVAL-CONFIDENCE:end -->论文用 Bayesian inference 估计有限样本下相对成功率并与传统排名比较。结果支持在相同 query/judge contract 下表达排序不确定性；它不证明 prior 无偏、judge 正确或 posterior 能转移到新任务，anchor 与 query selection 会成为新的偏差来源。<!-- review:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- review:SF-2025-PHI4-REASONING:start --><!-- claim:SF-2025-PHI4-REASONING:start -->compact reasoning policy 可由高可教性 demonstration 扩展，再用 outcome-verifiable RL 增加探索；teacher/scaffold 和 token budget 仍是能力与成本边界。<!-- claim:SF-2025-PHI4-REASONING:end -->技术报告披露 seeds/data、SFT exploration/scaling 和 reasoning-plus RL，并在 reasoning/general/safety benchmark 上评估。它不披露完整训练 hardware、batch/concurrency 或生产 SLO，也不证明长 trace 忠实；旧的短响应模型在严格 latency 下仍合理。<!-- review:SF-2025-PHI4-REASONING:end -->

<!-- review:SF-2025-NEXUS-GEN:start --><!-- claim:SF-2025-NEXUS-GEN:start -->统一多模态模型仍需分开 representation identity 与 generation state：shared space 负责接口，prefilled AR 负责条件生成与 commit 顺序。<!-- claim:SF-2025-NEXUS-GEN:end -->论文给出 architecture、unified task representation、prefilled autoregression 与数据构建，并展示理解/生成/编辑案例。缺少系统性 matched benchmark、ablation 和 production latency，因此只支持可行性，不证明共享空间消除了 modality boundary 或独立 head 的必要性。<!-- review:SF-2025-NEXUS-GEN:end -->

<!-- review:SF-2025-SHORTERBETTER:start --><!-- claim:SF-2025-SHORTERBETTER:start -->reasoning 长度是受 workload 约束的可学习 stopping proposal，不是“越短越好”；上线仍需质量 guardrail、尾延迟和错误早停审计。<!-- claim:SF-2025-SHORTERBETTER:end -->作者搜索 sample optimal length 并训练模型在保持准确率时缩短输出，包含 out-of-domain 与 ablation。结果受选定数学任务、模型和 evaluator 限制；长度标签可能奖励跳步或格式捷径，旧的固定上限/自然 EOS 在低风险任务仍更简单。<!-- review:SF-2025-SHORTERBETTER:end -->

<!-- review:SF-2025-GALVATRON:start --><!-- claim:SF-2025-GALVATRON:start -->自动并行 planner 只拥有候选 plan；model shape、cluster topology、memory cap 和 collective profile 构成 plan identity，runtime telemetry 与 fallback 才拥有上线真值。<!-- claim:SF-2025-GALVATRON:end -->Galvatron 把 hybrid parallelism 搜索与执行 workflow 连接，并在作者 benchmark 下比较训练效率。它不证明 cost model 可跨拓扑、版本和动态故障稳定；profiling 成本、search explosion、错误 memory estimate 与 process-group churn 是新增 failure mode，固定静态 plan 在稳定 workload 下仍合理。<!-- review:SF-2025-GALVATRON:end -->

<!-- review:SF-2025-RWKV-X:start --><!-- claim:SF-2025-RWKV-X:start -->长上下文可以组合 recurrent linear state 与少量 sparse attention，但 active chunks、KV/state layout 和 continual-pretraining revision 必须共同定义运行时 identity。<!-- claim:SF-2025-RWKV-X:end -->论文给出 chunk sparse attention、KV 管理、复杂度和 continual pretraining，并测量长短 context 与效率。作者实验不证明 top-k retrieval 在所有任务保留关键信息；routing error、chunk metadata 与 hybrid kernel complexity 是代价，全 attention 在短上下文/高精度需求下仍成立。<!-- review:SF-2025-RWKV-X:end -->

<!-- review:SF-2025-MCITY-DATA-ENGINE:start --><!-- claim:SF-2025-MCITY-DATA-ENGINE:start -->把 acquisition、storage、open-vocabulary selection、label alignment、training、validation 与 deployment 连成可迭代的数据开发闭环；每轮 model/data/index identity 与 selection threshold 必须可追溯。<!-- claim:SF-2025-MCITY-DATA-ENGINE:end -->

评估聚焦交通视觉数据、开放词汇检测器与有限迭代；未来工作明确仍需更多 labeling/training rounds，因此不能声称该闭环已验证任意领域或长期漂移。<!-- review:SF-2025-MCITY-DATA-ENGINE:end -->

<!-- review:SF-2025-RAGFORENSICS:start --><!-- claim:SF-2025-RAGFORENSICS:start -->RAG poisoning diagnosis 必须回溯 query、retrieved document、index revision 与 generated claim；traceback score 只拥有调查优先级，不拥有删除或定罪 authority。<!-- claim:SF-2025-RAGFORENSICS:end -->论文定义 threat model，组合可疑文本定位与实验评估，并测试 adaptive attacks。证据限于选定攻击、corpus、retriever 与 generator；false attribution、adaptive evasion 和昂贵 replay 要求人工/独立证据，简单 allowlist 和 immutable corpus 在高风险域仍适用。<!-- review:SF-2025-RAGFORENSICS:end -->

<!-- review:SF-2025-MUTEDRAG-AVAILABILITY:start --><!-- claim:SF-2025-MUTEDRAG-AVAILABILITY:start -->RAG 安全不能只测恶意内容是否被拒绝，还要把恶意检索内容诱发的正常请求拒绝视为 availability failure；retrieval hit、guardrail decision 与 final refusal 必须分开记录。<!-- claim:SF-2025-MUTEDRAG-AVAILABILITY:end -->论文给出攻击目标、黑盒/白盒路径和多数据集、多模型实验，并讨论若干防御。证据只支持论文所测 retriever、generator、guardrail 与攻击模板；它不证明任意安全过滤器都可被同样利用，也不证明内容过滤能无损修复。更严格 admission 会换来 false positive、延迟与维护成本；高风险域的 curated corpus/allowlist 仍是合理共存分支。<!-- review:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- review:SF-2025-VDDP:start --><!-- claim:SF-2025-VDDP:start -->分布式差分隐私不能让 server 同时拥有随机机制执行与合规证明；mechanism revision、随机性来源、collusion model、proof/receipt 与 verifier identity 必须共同定义 privacy evidence。<!-- claim:SF-2025-VDDP:end -->论文形式化 client-server-verifier 设置，构建可验证离散 Laplace 与 randomized response，并测量密码学开销。它不消除 verifier/collusion 假设，也不证明部署中的 data pipeline、side channel 或 privacy budget composition 正确；证明成本、可信设置与系统复杂度是代价，受控环境下的 trusted aggregator 仍可能更简单。<!-- review:SF-2025-VDDP:end -->

<!-- review:SF-2025-WEBTHINKER:start --><!-- claim:SF-2025-WEBTHINKER:start -->Deep Research 是 durable evidence workflow：搜索、读取、草稿与最终 claim 必须共享 source/version lineage，模型只拥有 proposal，工具结果和 verifier 拥有 evidence。<!-- claim:SF-2025-WEBTHINKER:end -->论文组合 Deep Web Explorer、think-search-draft 与 tool-use RL，在复杂问答和报告生成任务上比较并做 ablation。它不证明 web evidence 正确、引用完整或开放网络安全；搜索漂移、citation laundering、judge bias 与长轨迹成本仍需平台 gate。<!-- review:SF-2025-WEBTHINKER:end -->

<!-- review:SF-2025-SWE-SMITH:start --><!-- claim:SF-2025-SWE-SMITH:start -->可扩展 software-agent data 需要 repository commit、container、mutation、fail-to-pass test、issue 与 trajectory 的联合 identity；test oracle 而不是 LLM judge 拥有样本 admission。<!-- claim:SF-2025-SWE-SMITH:end -->论文构建 executable task factory 并用 128 个 repositories、50,137 instances 和下游训练测试其数据效用。结果不证明 synthetic bug 等同真实 issue 或跨语言泛化；container supply chain、test inadequacy、license 和 storage 成本是新增风险，真实 PR 仍是 calibration branch。<!-- review:SF-2025-SWE-SMITH:end -->

<!-- review:SF-2025-DEEPSEEK-PROVER-V2:start --><!-- claim:SF-2025-DEEPSEEK-PROVER-V2:start -->形式推理训练应把自然语言 sketch、subgoal proposal、Lean environment 与 executable verdict 分开；verifier 拥有 proof acceptance，policy 只拥有搜索 proposal。<!-- claim:SF-2025-DEEPSEEK-PROVER-V2:end -->论文用 recursive subgoal decomposition、synthetic cold start、expert iteration 和 RL 训练 prover，并在 MiniF2F/大学/组合题上评估。证据受 Lean version、sampling budget 和 benchmark formalization 限制；vacuous proof、benchmark bug、verifier exploitation 与高 rollout cost 不允许外推为通用 reasoning correctness。<!-- review:SF-2025-DEEPSEEK-PROVER-V2:end -->

## 4. Benchmark Contracts

只有 Candidate Ledger 明确标为 `yes` 的数字主张进入下表；其余论文数字不被提升为日报结论。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-BAYES-EVAL-CONFIDENCE | 有限 query 的 LLM pairwise/ranking evaluation | anchor 与 candidate LLM roster 见 §3 | Not Disclosed | Not Disclosed | constructed query set | model answers/judgments | limited samples | offline | posterior ranking confidence；无 production threshold | Bayesian posterior + comparison baselines |
| SF-2025-PHI4-REASONING | math/code/science reasoning、general 与 safety evaluation | Phi-4-reasoning、Phi-4-reasoning-plus 与 baseline models | Not Disclosed | Not Disclosed | 最大 context 32K；per-task prompt length Not Disclosed | long reasoning response | Not Disclosed | offline sampling | accuracy/pass metrics；无 latency SLO | benchmark scorers、best-of-5 / distribution analysis |
| SF-2025-SHORTERBETTER | 数学 reasoning 的 sample-optimal-length search 与 OOD evaluation | Qwen2.5-based reasoning models / paper roster | Not Disclosed | Not Disclosed | problem prompt | variable CoT length | Not Disclosed | offline | accuracy 与 generated token length | task exact-answer scorer |
| SF-2025-GALVATRON | hybrid-parallel plan search 与 foundation-model training | Transformer family configs in §4 | multi-GPU clusters in §4; exact topology bound to each experiment | Not Disclosed | model shapes / sequence configs | training step | plan-specific | distributed workers | throughput/memory；无 production SLO | runtime profiler + measured training throughput |
| SF-2025-RWKV-X | long-context LM quality、efficiency 与 ablations | RWKV-X sizes and Transformer/RWKV baselines | training/evaluation hardware in Appendix A/B | Not Disclosed | short context to 1M-token tests per paper | LM token prediction | Not Disclosed | offline | perplexity/accuracy/throughput/memory | task metrics + runtime measurement |
| SF-2025-RAGFORENSICS | poisoned RAG traceback under baseline/adaptive attacks | retriever/generator combinations in §5.1 | Not Disclosed | Not Disclosed | query + corpus documents | generated answer + suspect ranking | Not Disclosed | offline | traceback metrics and attack success；无 production SLO | known injected poison ground truth |
| SF-2025-MUTEDRAG-AVAILABILITY | RAG denial-of-service attacks induced through safety guardrails across three datasets | 8 LLMs / paper guardrail and RAG configurations | Not Disclosed | Not Disclosed | query + retrieved adversarial text | answer or guardrail refusal | attack/evaluation batches by §4 | offline | attack success / refusal availability metrics；无 production SLO | known attack condition + task/refusal outcomes |
| SF-2025-VDDP | verifiable distributed discrete-Laplace and randomized-response mechanisms | cryptographic protocol implementations | Intel Xeon Platinum 8358, 32 cores, 231 GB RAM | integer/cryptographic protocol arithmetic | client records / protocol parameters | DP aggregate or randomized response + proof | microbenchmark configs in §6 | client-server-verifier protocol | proof verification time、communication and mechanism overhead；无 production SLO | cryptographic verifier + mechanism correctness checks |
| SF-2025-WEBTHINKER | complex reasoning + scientific report generation with web tools | QwQ/DeepSeek-R1-based LRMs and baselines | Not Disclosed | Not Disclosed | web evidence and long prompts；length by task | answer/report | Not Disclosed | tool loop | task score/report judge；无 production SLO | task scorer + model-based report evaluation |
| SF-2025-SWE-SMITH | 50,137 executable SWE tasks / 128 repos；RFT on 5,016 trajectories | Qwen2.5-Coder 7B/32B | 2–8×H100 80GB | Not Disclosed | max context 32,768 | agent patch trajectory | training setup in Appendix F | offline agent runs | SWE-bench Verified Pass@1 | repository tests / harness |
| SF-2025-DEEPSEEK-PROVER-V2 | Lean theorem proving、MiniF2F/ProverBench/combinatorial tasks | DeepSeek-Prover-V2 7B/671B | Not Disclosed | Not Disclosed | SFT 16,384；GRPO max 32,768 | Lean proof | GRPO 256 prompts ×32 proofs/iteration | offline sampling | Pass@k / proof success；无 latency SLO | Lean 4.9.0-rc2 verifier |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2025-DONT-RETRIEVE-GENERATE | score_7_9 | not_selected | — | — | SF-2025-DONT-RETRIEVE-GENERATE 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-DONT-RETRIEVE-GENERATE |
| SF-2025-WEBEVOLVER | score_7_9 | not_selected | — | — | SF-2025-WEBEVOLVER 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-WEBEVOLVER |
| SF-2025-SAGA-IDENTITY | score_7_9 | selected | DA-SAGA-IDENTITY | — | 把 principal lineage、delegation 与 effect-time authorization 收进协议状态机，安全 reach 高。 | analysis:DA-SAGA-IDENTITY |
| SF-2025-SEMANTIC-REIDENTIFICATION | score_7_9 | not_selected | — | — | SF-2025-SEMANTIC-REIDENTIFICATION 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-SEMANTIC-REIDENTIFICATION |
| SF-2025-DP-FINETUNING-PRIVACY | score_7_9 | not_selected | — | — | SF-2025-DP-FINETUNING-PRIVACY 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-DP-FINETUNING-PRIVACY |
| SF-2025-PREFILL-JAILBREAK | score_7_9 | not_selected | — | — | SF-2025-PREFILL-JAILBREAK 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-PREFILL-JAILBREAK |
| SF-2025-LEGILIMENS | score_7_9 | selected | DA-LEGILIMENS | — | 把持续 edge inference 与在线 retraining 放进同一 SoC compute budget，是当日最清晰的跨训练/推理状态变化。 | analysis:DA-LEGILIMENS |
| SF-2025-SECREPOBENCH | score_7_9 | not_selected | — | — | SF-2025-SECREPOBENCH 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-SECREPOBENCH |
| SF-2025-CACHEPRUNE | score_7_9 | not_selected | — | — | SF-2025-CACHEPRUNE 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-CACHEPRUNE |
| SF-2025-BAYES-EVAL-CONFIDENCE | score_7_9 | not_selected | — | — | SF-2025-BAYES-EVAL-CONFIDENCE 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE |
| SF-2025-GALVATRON | score_7_9;forced_review | selected | DA-GALVATRON | — | 直接改变并行 plan 的 proposal/execution/truth ownership，且既有 Books writeback 需要 post-write 验证。 | analysis:DA-GALVATRON |
| SF-2025-MCITY-DATA-ENGINE | score_7_9 | not_selected | — | — | SF-2025-MCITY-DATA-ENGINE 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-MCITY-DATA-ENGINE |
| SF-2025-RAGFORENSICS | score_7_9 | not_selected | — | — | SF-2025-RAGFORENSICS 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-RAGFORENSICS |
| SF-2025-MUTEDRAG-AVAILABILITY | score_7_9 | not_selected | — | — | SF-2025-MUTEDRAG-AVAILABILITY 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY |
| SF-2025-VDDP | score_7_9 | not_selected | — | — | SF-2025-VDDP 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-VDDP |
| SF-2025-WEBTHINKER | score_7_9 | not_selected | — | — | SF-2025-WEBTHINKER 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-WEBTHINKER |
| SF-2025-SWE-SMITH | score_7_9 | not_selected | — | — | SF-2025-SWE-SMITH 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-SWE-SMITH |
| SF-2025-DEEPSEEK-PROVER-V2 | score_7_9 | not_selected | — | — | SF-2025-DEEPSEEK-PROVER-V2 已完成 exact-v1 Review/Books comparison；当日三项容量优先给 SF-2025-GALVATRON, SF-2025-LEGILIMENS, SF-2025-SAGA-IDENTITY 的 owner 或跨层变化。 | analysis-decision:SF-2025-DEEPSEEK-PROVER-V2 |

<!-- analysis:DA-SAGA-IDENTITY:start -->### DA-SAGA-IDENTITY

把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-SAGA-IDENTITY:end -->

<!-- analysis:DA-LEGILIMENS:start -->### DA-LEGILIMENS

把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-LEGILIMENS:end -->

<!-- analysis:DA-GALVATRON:start -->### DA-GALVATRON

自动并行 planner 只拥有候选 plan；model shape、cluster topology、memory cap 和 collective profile 构成 plan identity，runtime telemetry 与 fallback 才拥有上线真值。Galvatron 把 hybrid parallelism 搜索与执行 workflow 连接，并在作者 benchmark 下比较训练效率。它不证明 cost model 可跨拓扑、版本和动态故障稳定；profiling 成本、search explosion、错误 memory estimate 与 process-group churn 是新增 failure mode，固定静态 plan 在稳定 workload 下仍合理。 旧方案仍作为可验证 fallback；新机制的收益必须与新增状态、观测成本和 failure mode 一起评估。<!-- analysis:DA-GALVATRON:end -->

<!-- analysis-decision:SF-2025-DONT-RETRIEVE-GENERATE:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-DONT-RETRIEVE-GENERATE:end -->

<!-- analysis-decision:SF-2025-WEBEVOLVER:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-WEBEVOLVER:end -->

<!-- analysis-decision:SF-2025-SEMANTIC-REIDENTIFICATION:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-SEMANTIC-REIDENTIFICATION:end -->

<!-- analysis-decision:SF-2025-DP-FINETUNING-PRIVACY:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-DP-FINETUNING-PRIVACY:end -->

<!-- analysis-decision:SF-2025-PREFILL-JAILBREAK:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-PREFILL-JAILBREAK:end -->

<!-- analysis-decision:SF-2025-SECREPOBENCH:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-SECREPOBENCH:end -->

<!-- analysis-decision:SF-2025-CACHEPRUNE:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-CACHEPRUNE:end -->

<!-- analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- analysis-decision:SF-2025-MCITY-DATA-ENGINE:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-MCITY-DATA-ENGINE:end -->

<!-- analysis-decision:SF-2025-RAGFORENSICS:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-RAGFORENSICS:end -->

<!-- analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- analysis-decision:SF-2025-VDDP:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-VDDP:end -->

<!-- analysis-decision:SF-2025-WEBTHINKER:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-WEBTHINKER:end -->

<!-- analysis-decision:SF-2025-SWE-SMITH:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-SWE-SMITH:end -->

<!-- analysis-decision:SF-2025-DEEPSEEK-PROVER-V2:start -->该 family 的机制、反证与 Books 边界已在 Source Review/Comparison 给出；不重复论文摘要式叙事。<!-- analysis-decision:SF-2025-DEEPSEEK-PROVER-V2:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2025-DONT-RETRIEVE-GENERATE | AGENT-RAG | books/part-07-agent/76-rag.md#L592 | books/part-04-training-system/27-data.md#L762 | existing:SF-2025-DONT-RETRIEVE-GENERATE | delta:SF-2025-DONT-RETRIEVE-GENERATE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-DONT-RETRIEVE-GENERATE |
| SF-2025-WEBEVOLVER | AGENT-WORKFLOW | books/part-07-agent/84-agent-platform.md#L758 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L601 | existing:SF-2025-WEBEVOLVER | delta:SF-2025-WEBEVOLVER | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-WEBEVOLVER |
| SF-2025-SAGA-IDENTITY | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L561 | books/part-06-ai-infrastructure/72-security.md#L326 | existing:SF-2025-SAGA-IDENTITY | delta:SF-2025-SAGA-IDENTITY | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-SAGA-IDENTITY |
| SF-2025-SEMANTIC-REIDENTIFICATION | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L120 | books/part-06-ai-infrastructure/72-security.md#L141 | existing:SF-2025-SEMANTIC-REIDENTIFICATION | delta:SF-2025-SEMANTIC-REIDENTIFICATION | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-SEMANTIC-REIDENTIFICATION |
| SF-2025-DP-FINETUNING-PRIVACY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L163 | books/part-06-ai-infrastructure/72-security.md#L209 | existing:SF-2025-DP-FINETUNING-PRIVACY | delta:SF-2025-DP-FINETUNING-PRIVACY | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-DP-FINETUNING-PRIVACY |
| SF-2025-PREFILL-JAILBREAK | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L607 | books/part-05-inference-system/43-prefill.md#L33 | existing:SF-2025-PREFILL-JAILBREAK | delta:SF-2025-PREFILL-JAILBREAK | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-PREFILL-JAILBREAK |
| SF-2025-LEGILIMENS | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L834 | books/part-04-training-system/27-data.md#L735 | existing:SF-2025-LEGILIMENS | delta:SF-2025-LEGILIMENS | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-LEGILIMENS |
| SF-2025-SECREPOBENCH | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1059 | books/part-06-ai-infrastructure/72-security.md#L1486 | existing:SF-2025-SECREPOBENCH | delta:SF-2025-SECREPOBENCH | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-SECREPOBENCH |
| SF-2025-CACHEPRUNE | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L536 | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1049 | existing:SF-2025-CACHEPRUNE | delta:SF-2025-CACHEPRUNE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-CACHEPRUNE |
| SF-2025-BAYES-EVAL-CONFIDENCE | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1040 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L105; books/part-06-ai-infrastructure/67-monitoring.md#L596 | existing:SF-2025-BAYES-EVAL-CONFIDENCE | delta:SF-2025-BAYES-EVAL-CONFIDENCE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-BAYES-EVAL-CONFIDENCE |
| SF-2025-PHI4-REASONING | TRAIN-SFT | books/part-04-training-system/29-sft.md#L680 | books/part-04-training-system/28-pretraining.md#L1107; books/part-04-training-system/33-grpo.md#L1721 | existing:SF-2025-PHI4-REASONING | delta:SF-2025-PHI4-REASONING | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-PHI4-REASONING |
| SF-2025-NEXUS-GEN | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#L160 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L598; books/part-02-model/18-decoder-only.md#L227 | existing:SF-2025-NEXUS-GEN | delta:SF-2025-NEXUS-GEN | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-NEXUS-GEN |
| SF-2025-SHORTERBETTER | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L160 | books/part-02-model/20-sampling.md#L180; books/part-04-training-system/33-grpo.md#L1020 | existing:SF-2025-SHORTERBETTER | delta:SF-2025-SHORTERBETTER | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-SHORTERBETTER |
| SF-2025-GALVATRON | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L859 | books/part-04-training-system/37-tensor-parallel.md#L280; books/part-04-training-system/38-pipeline-parallel.md#L270 | existing:SF-2025-GALVATRON | delta:SF-2025-GALVATRON | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-GALVATRON |
| SF-2025-RWKV-X | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L756 | books/part-02-model/15-multi-head-attention.md#L237; books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L481 | existing:SF-2025-RWKV-X | delta:SF-2025-RWKV-X | Alternative Branch | No Change — Existing Coverage | books-review:SF-2025-RWKV-X |
| SF-2025-MCITY-DATA-ENGINE | TRAIN-DATA | books/part-04-training-system/27-data.md#L138 | books/part-06-ai-infrastructure/66-evaluation-system.md#L110 | existing:SF-2025-MCITY-DATA-ENGINE | delta:SF-2025-MCITY-DATA-ENGINE | Principle Reuse | No Change — Existing Coverage | books-review:SF-2025-MCITY-DATA-ENGINE |
| SF-2025-RAGFORENSICS | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1741 | books/part-07-agent/76-rag.md#L726; books/part-06-ai-infrastructure/69-trace.md#L351 | existing:SF-2025-RAGFORENSICS | delta:SF-2025-RAGFORENSICS | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-RAGFORENSICS |
| SF-2025-MUTEDRAG-AVAILABILITY | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1741 | books/part-07-agent/76-rag.md#L726; books/part-06-ai-infrastructure/69-trace.md#L351 | existing:SF-2025-MUTEDRAG-AVAILABILITY | delta:SF-2025-MUTEDRAG-AVAILABILITY | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-MUTEDRAG-AVAILABILITY |
| SF-2025-VDDP | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1741 | books/part-04-training-system/27-data.md#L910; books/part-06-ai-infrastructure/71-multi-tenant.md#L183 | existing:SF-2025-VDDP | delta:SF-2025-VDDP | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2025-VDDP |
| SF-2025-WEBTHINKER | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L791 | books/part-07-agent/76-rag.md#L726; books/part-06-ai-infrastructure/66-evaluation-system.md#L280 | existing:SF-2025-WEBTHINKER | delta:SF-2025-WEBTHINKER | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-WEBTHINKER |
| SF-2025-SWE-SMITH | TRAIN-DATA | books/part-04-training-system/27-data.md#L280 | books/part-06-ai-infrastructure/66-evaluation-system.md#L790; books/part-07-agent/81-workflow.md#L791 | existing:SF-2025-SWE-SMITH | delta:SF-2025-SWE-SMITH | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-SWE-SMITH |
| SF-2025-DEEPSEEK-PROVER-V2 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L940 | books/part-04-training-system/29-sft.md#L680; books/part-06-ai-infrastructure/66-evaluation-system.md#L750 | existing:SF-2025-DEEPSEEK-PROVER-V2 | delta:SF-2025-DEEPSEEK-PROVER-V2 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2025-DEEPSEEK-PROVER-V2 |

<!-- books-review:SF-2025-DONT-RETRIEVE-GENERATE:start --><!-- existing:SF-2025-DONT-RETRIEVE-GENERATE:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-DONT-RETRIEVE-GENERATE:end --><!-- delta:SF-2025-DONT-RETRIEVE-GENERATE:start -->把 RAG 训练数据来源从只检索公开问答扩展为可控生成的 hypothetical negatives；关键系统边界是生成器版本、去重、污染审计与真实检索回放必须共同冻结。<!-- delta:SF-2025-DONT-RETRIEVE-GENERATE:end -->

作者实验只比较其合成 hard-negative recipe 与披露数据集，不能证明生成数据普遍优于真实 retrieval logs。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-DONT-RETRIEVE-GENERATE:end -->

<!-- books-review:SF-2025-WEBEVOLVER:start --><!-- existing:SF-2025-WEBEVOLVER:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-WEBEVOLVER:end --><!-- delta:SF-2025-WEBEVOLVER:start -->把 web agent 自我改进拆成 evolving policy 与 co-evolving environment model，说明 rollout 数据、网页状态和 evaluator revision 必须作为同一训练 identity 管理。<!-- delta:SF-2025-WEBEVOLVER:end -->

结果绑定作者构造的 web environment 与任务；没有证明开放互联网漂移、权限边界或真实副作用下仍能安全自演化。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-WEBEVOLVER:end -->

<!-- books-review:SF-2025-SAGA-IDENTITY:start --><!-- existing:SF-2025-SAGA-IDENTITY:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-SAGA-IDENTITY:end --><!-- delta:SF-2025-SAGA-IDENTITY:start -->把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。<!-- delta:SF-2025-SAGA-IDENTITY:end -->

论文给出协议与原型评估，不等于互联网规模身份联邦、密钥轮换、撤权传播或恶意参与方下已经安全。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-SAGA-IDENTITY:end -->

<!-- books-review:SF-2025-SEMANTIC-REIDENTIFICATION:start --><!-- existing:SF-2025-SEMANTIC-REIDENTIFICATION:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-SEMANTIC-REIDENTIFICATION:end --><!-- delta:SF-2025-SEMANTIC-REIDENTIFICATION:start -->证明移除显式 PII 或生成 synthetic text 并不关闭语义再识别通道；privacy boundary 必须绑定攻击者辅助信息、关系特征与 release surface。<!-- delta:SF-2025-SEMANTIC-REIDENTIFICATION:end -->

攻击成功率只对论文披露的数据、模型与辅助信息成立，不能外推为所有去标识化文本都可被同等重识别。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-SEMANTIC-REIDENTIFICATION:end -->

<!-- books-review:SF-2025-DP-FINETUNING-PRIVACY:start --><!-- existing:SF-2025-DP-FINETUNING-PRIVACY:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-DP-FINETUNING-PRIVACY:end --><!-- delta:SF-2025-DP-FINETUNING-PRIVACY:start -->把 private fine-tuning 的证据从单一 utility 指标扩展为多种攻击面、机制参数与 privacy-utility slice；accountant、实现路径和攻击者能力必须同构。<!-- delta:SF-2025-DP-FINETUNING-PRIVACY:end -->

比较覆盖论文列出的 DP 方法与攻击，不能证明未测攻击、不同基础模型或部署精度具有相同 privacy guarantee。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-DP-FINETUNING-PRIVACY:end -->

<!-- books-review:SF-2025-PREFILL-JAILBREAK:start --><!-- existing:SF-2025-PREFILL-JAILBREAK:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PREFILL-JAILBREAK:end --><!-- delta:SF-2025-PREFILL-JAILBREAK:start -->把 jailbreak 攻击面推进到 assistant prefill：请求在 decode 前已携带带角色语义的生成状态，因此 API normalization、template ownership 与 prefill policy 都属于安全边界。<!-- delta:SF-2025-PREFILL-JAILBREAK:end -->

攻击结果绑定被测模型、模板与访问方式；不证明所有 prefill API 都同样脆弱，也不把检测器提升为最终 authority。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PREFILL-JAILBREAK:end -->

<!-- books-review:SF-2025-LEGILIMENS:start --><!-- existing:SF-2025-LEGILIMENS:start -->Inference Scheduling 已把 continuous edge inference 的 violation-risk budget、runtime scheduling 与训练/交付边界分开；Data 章也已把在线 selection 定义为受版本治理的 control loop。<!-- existing:SF-2025-LEGILIMENS:end --><!-- delta:SF-2025-LEGILIMENS:start -->把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。<!-- delta:SF-2025-LEGILIMENS:end -->

评估只覆盖作者的 50 小时视频、两类视觉任务与 Jetson SoC；多 base 结果依赖 oracle selection，且额外 base 会线性增加 memory，不能外推到任意 edge workload。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-LEGILIMENS:end -->

<!-- books-review:SF-2025-SECREPOBENCH:start --><!-- existing:SF-2025-SECREPOBENCH:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-SECREPOBENCH:end --><!-- delta:SF-2025-SECREPOBENCH:start -->把 secure code completion 的评估对象从孤立片段推进到真实 repository、dependency context、unit tests 与 repair trace；安全声明必须绑定可执行 project identity。<!-- delta:SF-2025-SECREPOBENCH:end -->

benchmark 覆盖作者收集的仓库与漏洞类别；unit tests 不是完整安全证明，agent repair 成功也不保证无新缺陷。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-SECREPOBENCH:end -->

<!-- books-review:SF-2025-CACHEPRUNE:start --><!-- existing:SF-2025-CACHEPRUNE:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-CACHEPRUNE:end --><!-- delta:SF-2025-CACHEPRUNE:start -->利用 KV-cache attribution 定位并削弱 prompt-injection influence，说明中间状态可以成为安全 sensor；但 eviction/pruning policy 必须保留 utility gate 与完整上下文 fallback。<!-- delta:SF-2025-CACHEPRUNE:end -->

防御只在披露模型、攻击与任务上评估；attribution signal 不是输入恶意性的真值，错误 pruning 可能删除任务关键语义。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-CACHEPRUNE:end -->

<!-- books-review:SF-2025-BAYES-EVAL-CONFIDENCE:start --><!-- existing:SF-2025-BAYES-EVAL-CONFIDENCE:start -->Evaluation 章已把 point estimate、confidence/calibration、相关误差与 abstention 分开，并要求冻结 evaluator identity。<!-- existing:SF-2025-BAYES-EVAL-CONFIDENCE:end --><!-- delta:SF-2025-BAYES-EVAL-CONFIDENCE:start -->有限样本 Bayesian ranking 是该既有命题的一种实现：posterior 只属于给定 prior、anchor、query set 与 judge，不是模型的内在置信度。<!-- delta:SF-2025-BAYES-EVAL-CONFIDENCE:end -->演进关系为 Principle Reuse；目标 `PLATFORM-EVALUATION-SYSTEM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-BAYES-EVAL-CONFIDENCE:end -->

<!-- books-review:SF-2025-PHI4-REASONING:start --><!-- existing:SF-2025-PHI4-REASONING:start -->SFT/GRPO 章节已经把 teacher demonstrations、cold start、outcome-verifiable RL 与长输出代价写成条件分支。<!-- existing:SF-2025-PHI4-REASONING:end --><!-- delta:SF-2025-PHI4-REASONING:start -->Phi-4-reasoning 是 compact model 上 teachable-prompt SFT 加短程 RL 的受限实例，不新增独立 owner。<!-- delta:SF-2025-PHI4-REASONING:end -->演进关系为 Direct Evolution；目标 `TRAIN-SFT` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-PHI4-REASONING:end -->

<!-- books-review:SF-2025-NEXUS-GEN:start --><!-- existing:SF-2025-NEXUS-GEN:start -->多模态章节已区分 shared semantic interface 与独立 generation head，并把 AR factorization 放在生成范式 owner。<!-- existing:SF-2025-NEXUS-GEN:end --><!-- delta:SF-2025-NEXUS-GEN:start -->shared embedding、task token 与 prefilled autoregression 是该分层的实现案例；case study 不足以宣称统一表示优于所有双塔。<!-- delta:SF-2025-NEXUS-GEN:end -->演进关系为 Layering / Dependency；目标 `MULTIMODAL-REPRESENTATION` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-NEXUS-GEN:end -->

<!-- books-review:SF-2025-SHORTERBETTER:start --><!-- existing:SF-2025-SHORTERBETTER:start -->调度章已把 reasoning token budget、stopping policy 与 expected value per token 作为 request-level control state。<!-- existing:SF-2025-SHORTERBETTER:end --><!-- delta:SF-2025-SHORTERBETTER:start -->sample-optimal-length 自训练只提供一种长度 proposal；scheduler 仍拥有上线预算、SLO 与 harmful early-stop audit。<!-- delta:SF-2025-SHORTERBETTER:end -->演进关系为 Direct Evolution；目标 `INFER-SCHEDULING` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SHORTERBETTER:end -->

<!-- books-review:SF-2025-GALVATRON:start --><!-- existing:SF-2025-GALVATRON:start -->分布式训练章已有 cost model、collective 与 static/dynamic plan 边界，但自动 plan search 的状态 owner、校准与失效回退尚未形成完整链条。<!-- existing:SF-2025-GALVATRON:end --><!-- delta:SF-2025-GALVATRON:start -->增加 planner 分支：冻结 model/hardware/memory/communication profile，搜索 DP/TP/PP/sharding 组合；runtime 执行并用真实 telemetry 校准，预测失真时回到已验证静态 plan。<!-- delta:SF-2025-GALVATRON:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-GALVATRON:end -->

<!-- books-review:SF-2025-RWKV-X:start --><!-- existing:SF-2025-RWKV-X:start -->Long-context 章节已把 recurrent/linear state 与 sparse attention 作为替代分支，并要求保留 cache/state identity。<!-- existing:SF-2025-RWKV-X:end --><!-- delta:SF-2025-RWKV-X:start -->top-k chunk sparse attention 加 RWKV block 是该分支的组合实例，不改变 owner。<!-- delta:SF-2025-RWKV-X:end -->演进关系为 Alternative Branch；目标 `MODEL-LONG-CONTEXT` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-RWKV-X:end -->

<!-- books-review:SF-2025-MCITY-DATA-ENGINE:start --><!-- existing:SF-2025-MCITY-DATA-ENGINE:start -->Data 章已把 mixture、filter/selection、lineage 与 post-training online selection 收进同一 control plane；Evaluation 章要求 continual update 同步推进 calibration state。<!-- existing:SF-2025-MCITY-DATA-ENGINE:end --><!-- delta:SF-2025-MCITY-DATA-ENGINE:start -->把 acquisition、storage、open-vocabulary selection、label alignment、training、validation 与 deployment 连成可迭代的数据开发闭环；每轮 model/data/index identity 与 selection threshold 必须可追溯。<!-- delta:SF-2025-MCITY-DATA-ENGINE:end -->

评估聚焦交通视觉数据、开放词汇检测器与有限迭代；未来工作明确仍需更多 labeling/training rounds，因此不能声称该闭环已验证任意领域或长期漂移。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MCITY-DATA-ENGINE:end -->

<!-- books-review:SF-2025-RAGFORENSICS:start --><!-- existing:SF-2025-RAGFORENSICS:start -->Security/RAG 章节已要求 document provenance、retrieval trace、attack surface 与 quarantine 分离。<!-- existing:SF-2025-RAGFORENSICS:end --><!-- delta:SF-2025-RAGFORENSICS:start -->RAGForensics 的 traceback 是已有 provenance contract 的诊断实现，不把相似度归因升级为因果证明。<!-- delta:SF-2025-RAGFORENSICS:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-RAGFORENSICS:end -->

<!-- books-review:SF-2025-MUTEDRAG-AVAILABILITY:start --><!-- existing:SF-2025-MUTEDRAG-AVAILABILITY:start -->Security 与 RAG 章节已把 retrieved content 视为不可信输入，并要求 provenance、admission、policy decision 与 availability outcome 可追踪。<!-- existing:SF-2025-MUTEDRAG-AVAILABILITY:end --><!-- delta:SF-2025-MUTEDRAG-AVAILABILITY:start -->MutedRAG 进一步证明 safety guardrail 本身可以被对抗性 retrieved text 触发而成为 availability attack surface；这强化既有命题，但不改变 owner。<!-- delta:SF-2025-MUTEDRAG-AVAILABILITY:end -->演进关系为 Direct Evolution；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-MUTEDRAG-AVAILABILITY:end -->

<!-- books-review:SF-2025-VDDP:start --><!-- existing:SF-2025-VDDP:start -->Security 章已要求 privacy claim 绑定可执行 policy、可信边界、receipt 与独立验证，而不是由执行方自我声明。<!-- existing:SF-2025-VDDP:end --><!-- delta:SF-2025-VDDP:start -->VDDP 用 client/server/verifier 分权、可验证随机机制与密码学证明具体化该 contract；新增的是机制证据，不是新的知识 owner。<!-- delta:SF-2025-VDDP:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-SECURITY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-VDDP:end -->

<!-- books-review:SF-2025-WEBTHINKER:start --><!-- existing:SF-2025-WEBTHINKER:start -->Workflow/RAG 章节已拥有 plan-search-draft、evidence provenance、tool receipt 与 report-level verification。<!-- existing:SF-2025-WEBTHINKER:end --><!-- delta:SF-2025-WEBTHINKER:start -->WebThinker 的 think-search-draft 与 RL 是该工作流的受限实例，不新增可绕过证据 gate 的自治 authority。<!-- delta:SF-2025-WEBTHINKER:end -->演进关系为 Direct Evolution；目标 `AGENT-WORKFLOW` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-WEBTHINKER:end -->

<!-- books-review:SF-2025-SWE-SMITH:start --><!-- existing:SF-2025-SWE-SMITH:start -->Data 章已把 executable mutation、environment/test oracle、trajectory 与 lineage 作为 agentic data factory。<!-- existing:SF-2025-SWE-SMITH:end --><!-- delta:SF-2025-SWE-SMITH:start -->SWE-smith 已被该命题承载；本轮只重建 exact-day provenance，不重复追加论文清单。<!-- delta:SF-2025-SWE-SMITH:end -->演进关系为 Direct Evolution；目标 `TRAIN-DATA` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SWE-SMITH:end -->

<!-- books-review:SF-2025-DEEPSEEK-PROVER-V2:start --><!-- existing:SF-2025-DEEPSEEK-PROVER-V2:start -->GRPO/Evaluation 已把 subgoal boundary、cold start、outcome verifier 与 reward hacking 边界写入主线。<!-- existing:SF-2025-DEEPSEEK-PROVER-V2:end --><!-- delta:SF-2025-DEEPSEEK-PROVER-V2:start -->Lean proof checking 是 executable verifier 分支；自然语言 sketch 和 recursive subgoal search 不取得 truth authority。<!-- delta:SF-2025-DEEPSEEK-PROVER-V2:end -->演进关系为 Direct Evolution；目标 `TRAIN-GRPO` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-DEEPSEEK-PROVER-V2:end -->

Books Gate 已通过：5 项既有语义绑定经 exact-v1 与目标/相邻正文复核后记为 `verified_existing_writeback`，不重复插入。

## 7. Semantic Audit

fresh-context audit 独立于作者重建；author recheck 不作为 Gate 证据。

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20250501-COVERAGE | fresh-context:daily_2025may_fresh_audit | coverage | coverage:SRC-ARXIV:20250501 | — | 696 title+abstract identities re-read without sampling; seven false negatives moved to their owner-day retained sets and zero-hit owner ledgers were rehashed | passed |
| SA-20250501-EVIDENCE | fresh-context:daily_2025may_fresh_audit | evidence | validator:review-completion-v1 | — | all retained routes were checked against primary packets for method, evaluation, limitation, artifact and withdrawal facets | passed |
| SA-20250501-SELECTION | fresh-context:daily_2025may_fresh_audit | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | every eligible family has a day-specific selected or non-selected disposition within the three-item narrative budget | passed |
| SA-20250501-BOOKS | fresh-context:daily_2025may_fresh_audit | books | validator:books-comparison-v1 | — | five exact-v1 sources and current target/adjacent flows were rechecked in date order; existing bindings were marked verified_existing_writeback and line-one placeholders removed | passed |

## 8. Ignored Noise

353 条 pre-denominator closure 均在 `semantic-screening-ledger-v2.1.json.gz` 中保留完整 identity、title、abstract evidence、closure class 与 family-specific reason；没有评分，也没有冒充全文 Review。

## 9. Recommended Action

保持当前 owner 与 Books 语义绑定；后续只在新 primary evidence 改变长期机制边界时重新打开 Books Decision。

## 10. Repository Changes

重建 05/01–04 Daily、owner-day ledger、exact-v1 manifests、no-hit receipts、Books queue 与 fresh-context audit receipt；既有 Books 正文经验证合格，未重复修改。未 stage/commit/push。

## 11. Open Questions

- None.

## 12. Sources

- [Don't Retrieve, Generate: Prompting LLMs for Synthetic Training Data in Dense Retrieval](https://arxiv.org/html/2504.21015v1) — exact v1；official owner `2025-05-01`。

- [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/html/2504.21024v1) — exact v1；official owner `2025-05-01`。

- [SAGA: A Security Architecture for Governing AI Agentic Systems](https://arxiv.org/html/2504.21034v1) — exact v1；official owner `2025-05-01`。

- [A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage](https://arxiv.org/html/2504.21035v1) — exact v1；official owner `2025-05-01`。

- [Can Differentially Private Fine-tuning LLMs Protect Against Privacy Attacks?](https://arxiv.org/html/2504.21036v1) — exact v1；official owner `2025-05-01`。

- [Prefill-level Jailbreak: A Black-Box Risk Analysis of Large Language Models](https://arxiv.org/html/2504.21038v1) — exact v1；official owner `2025-05-01`。

- [Legilimens: Performant Video Analytics on the System-on-Chip Edge](https://arxiv.org/pdf/2504.21136v1) — exact v1；official owner `2025-05-01`。

- [SecRepoBench: Benchmarking Code Agents for Secure Code Completion in Real-World Repositories](https://arxiv.org/html/2504.21205v1) — exact v1；official owner `2025-05-01`。

- [CachePrune: Teaching LLMs What Not to Follow via KV-Cache Editing](https://arxiv.org/html/2504.21228v1) — exact v1；official owner `2025-05-01`。

- [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](https://arxiv.org/html/2504.21303v1) — exact v1；official owner `2025-05-01`。

- [Phi-4-reasoning Technical Report](https://arxiv.org/html/2504.21318v1) — exact v1；official owner `2025-05-01`。

- [Nexus-Gen: Unified Image Understanding, Generation, and Editing via Prefilled Autoregression in Shared Embedding Space](https://arxiv.org/html/2504.21356v1) — exact v1；official owner `2025-05-01`。

- [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](https://arxiv.org/html/2504.21370v1) — exact v1；official owner `2025-05-01`。

- [Galvatron: An Automatic Distributed System for Efficient Foundation Model Training](https://arxiv.org/html/2504.21411v1) — exact v1；official owner `2025-05-01`。

- [RWKV-X: A Linear Complexity Hybrid Language Model](https://arxiv.org/html/2504.21463v1) — exact v1；official owner `2025-05-01`。

- [Mcity Data Engine: Iterative Model Improvement Through Open-Vocabulary Data Selection](https://arxiv.org/html/2504.21614v1) — exact v1；official owner `2025-05-01`。

- [Traceback of Poisoning Attacks to Retrieval-Augmented Generation](https://arxiv.org/html/2504.21668v1) — exact v1；official owner `2025-05-01`。

- [Hoist with His Own Petard: Inducing Guardrails to Facilitate Denial-of-Service Attacks on Retrieval-Augmented Generation of LLMs](https://arxiv.org/html/2504.21680v1) — exact v1；official owner `2025-05-01`。

- [VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup](https://arxiv.org/html/2504.21752v1) — exact v1；official owner `2025-05-01`。

- [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/html/2504.21776v1) — exact v1；official owner `2025-05-01`。

- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/html/2504.21798v1) — exact v1；official owner `2025-05-01`。

- [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/html/2504.21801v1) — exact v1；official owner `2025-05-01`。

## 13. Final Status

- Completion Status = `Complete`
- Coverage = `Closed`
- Evidence = `Passed`
- Books = `Passed`
- unresolved findings = 0
