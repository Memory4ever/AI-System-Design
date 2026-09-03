# Daily Research — 2026-03-10

**Research Date:** 2026-03-10

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-09 09:00:00 ～ 2026-03-10 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=1205/1205/1205；denominator=33、pre-denominator closures=1172。exact-v1 Review complete=33、blocked=0；Integrate 建议=2。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-10 |
| Window End | 2026-03-10 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260310-AUTHOR-33 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-09T09:00:00+08:00 | 2026-03-10T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 1205/1205 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 1205 | SF-2026-ARXIV-2603-06588;SF-2026-ARXIV-2603-06604;SF-2026-ARXIV-2603-06626;SF-2026-ARXIV-2603-06728;SF-2026-ARXIV-2603-06798;SF-2026-ARXIV-2603-06847;SF-2026-ARXIV-2603-07006;SF-2026-ARXIV-2603-07373;SF-2026-ARXIV-2603-07416;SF-2026-ARXIV-2603-07427;SF-2026-ARXIV-2603-07433;SF-2026-ARXIV-2603-07466;SF-2026-ARXIV-2603-07557;SF-2026-ARXIV-2603-07607;SF-2026-ARXIV-2603-07670;SF-2026-ARXIV-2603-07685;SF-2026-ARXIV-2603-07770;SF-2026-ARXIV-2603-07777;SF-2026-ARXIV-2603-07799;SF-2026-ARXIV-2603-07915;SF-2026-ARXIV-2603-07917;SF-2026-ARXIV-2603-07972;SF-2026-ARXIV-2603-08088;SF-2026-ARXIV-2603-08113;SF-2026-ARXIV-2603-08124;SF-2026-ARXIV-2603-08163;SF-2026-ARXIV-2603-08221;SF-2026-ARXIV-2603-08316;SF-2026-ARXIV-2603-08361;SF-2026-ARXIV-2603-08429;SF-2026-ARXIV-2603-08519;SF-2026-ARXIV-2603-08546;SF-2026-ARXIV-2603-08640 | pages=100; prefixes=00..99; final_cursor=end; registered=1205; screened=1205; retained=33; closure=1172 | 2026-03-10T01:00:00+00:00 | screening-ledger-final.json#sha256=243cbc64d67129bfe36eecc772c2557053d1f6e1d8f773b6d5a81bb643dca3b2; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260310:start -->作者侧已逐项筛选全部 1205 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260310:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-06588 | arXiv:2603.06588v1 | paper-v1:2603.06588 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06588 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06588 | no |
| SF-2026-ARXIV-2603-06604 | arXiv:2603.06604v1 | paper-v1:2603.06604 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06604 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06604 | no |
| SF-2026-ARXIV-2603-06626 | arXiv:2603.06626v1 | paper-v1:2603.06626 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06626 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06626 | no |
| SF-2026-ARXIV-2603-06728 | arXiv:2603.06728v1 | paper-v1:2603.06728 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06728 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06728 | no |
| SF-2026-ARXIV-2603-06798 | arXiv:2603.06798v1 | paper-v1:2603.06798 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06798 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06798 | no |
| SF-2026-ARXIV-2603-06847 | arXiv:2603.06847v1 | paper-v1:2603.06847 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06847 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06847 | no |
| SF-2026-ARXIV-2603-07006 | arXiv:2603.07006v1 | paper-v1:2603.07006 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07006 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07006 | no |
| SF-2026-ARXIV-2603-07373 | arXiv:2603.07373v1 | paper-v1:2603.07373 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07373 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07373 | no |
| SF-2026-ARXIV-2603-07416 | arXiv:2603.07416v1 | paper-v1:2603.07416 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07416 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07416 | no |
| SF-2026-ARXIV-2603-07427 | arXiv:2603.07427v1 | paper-v1:2603.07427 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07427 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07427 | no |
| SF-2026-ARXIV-2603-07433 | arXiv:2603.07433v1 | paper-v1:2603.07433 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07433 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07433 | no |
| SF-2026-ARXIV-2603-07466 | arXiv:2603.07466v1 | paper-v1:2603.07466 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07466 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07466 | no |
| SF-2026-ARXIV-2603-07557 | arXiv:2603.07557v1 | paper-v1:2603.07557 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07557 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07557 | no |
| SF-2026-ARXIV-2603-07607 | arXiv:2603.07607v1 | paper-v1:2603.07607 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07607 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07607 | no |
| SF-2026-ARXIV-2603-07670 | arXiv:2603.07670v1 | paper-v1:2603.07670 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07670 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07670 | no |
| SF-2026-ARXIV-2603-07685 | arXiv:2603.07685v1 | paper-v1:2603.07685 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-07685 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2603-07685 | no |
| SF-2026-ARXIV-2603-07770 | arXiv:2603.07770v1 | paper-v1:2603.07770 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07770 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07770 | no |
| SF-2026-ARXIV-2603-07777 | arXiv:2603.07777v1 | paper-v1:2603.07777 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07777 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07777 | no |
| SF-2026-ARXIV-2603-07799 | arXiv:2603.07799v1 | paper-v1:2603.07799 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07799 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07799 | no |
| SF-2026-ARXIV-2603-07915 | arXiv:2603.07915v1 | paper-v1:2603.07915 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07915 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07915 | no |
| SF-2026-ARXIV-2603-07917 | arXiv:2603.07917v1 | paper-v1:2603.07917 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07917 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07917 | no |
| SF-2026-ARXIV-2603-07972 | arXiv:2603.07972v1 | paper-v1:2603.07972 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-07972 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07972 | no |
| SF-2026-ARXIV-2603-08088 | arXiv:2603.08088v1 | paper-v1:2603.08088 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-08088 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2603-08088 | no |
| SF-2026-ARXIV-2603-08113 | arXiv:2603.08113v1 | paper-v1:2603.08113 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08113 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08113 | no |
| SF-2026-ARXIV-2603-08124 | arXiv:2603.08124v1 | paper-v1:2603.08124 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08124 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08124 | no |
| SF-2026-ARXIV-2603-08163 | arXiv:2603.08163v1 | paper-v1:2603.08163 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08163 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08163 | no |
| SF-2026-ARXIV-2603-08221 | arXiv:2603.08221v1 | paper-v1:2603.08221 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08221 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08221 | no |
| SF-2026-ARXIV-2603-08316 | arXiv:2603.08316v1 | paper-v1:2603.08316 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08316 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08316 | no |
| SF-2026-ARXIV-2603-08361 | arXiv:2603.08361v1 | paper-v1:2603.08361 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08361 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08361 | no |
| SF-2026-ARXIV-2603-08429 | arXiv:2603.08429v1 | paper-v1:2603.08429 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08429 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08429 | no |
| SF-2026-ARXIV-2603-08519 | arXiv:2603.08519v1 | paper-v1:2603.08519 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08519 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08519 | no |
| SF-2026-ARXIV-2603-08546 | arXiv:2603.08546v1 | paper-v1:2603.08546 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08546 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08546 | no |
| SF-2026-ARXIV-2603-08640 | arXiv:2603.08640v1 | paper-v1:2603.08640 | 2026-W11 | 2026-03-10 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-08640 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08640 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-06588 | RP-1af6c284c520bacd | standard | arXiv:2603.06588v1 | SRC-ARXIV@arXiv:2603.06588v1 | arXiv:2603.06588v1 HTML — §2 Core Functions of vLLM Hook [facet=method]; https://arxiv.org/html/2603.06588v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06588v1.html; sha256:48d124e03a9ac718b7c7837e4684af271c49ac62032353cd42690769b7643f64 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.06588v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06588v1.html; sha256:48d124e03a9ac718b7c7837e4684af271c49ac62032353cd42690769b7643f64 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/html/2603.06588v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06588v1.html; sha256:48d124e03a9ac718b7c7837e4684af271c49ac62032353cd42690769b7643f64 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06588v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06588 | complete |
| SF-2026-ARXIV-2603-06604 | RP-426af905f313fcc6 | standard | arXiv:2603.06604v1 | SRC-ARXIV@arXiv:2603.06604v1 | arXiv:2603.06604v1 HTML — §3 Know When You’re Wrong [facet=method]; https://arxiv.org/html/2603.06604v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06604v1.html; sha256:b44fd93eca16eb6c69cbb404264024ce5f5fc19c87c70858f6d474f950e48fd2 | arXiv:2603.06604v1 HTML — §3.3 Confidence Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06604v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06604v1.html; sha256:b44fd93eca16eb6c69cbb404264024ce5f5fc19c87c70858f6d474f950e48fd2 | arXiv:2603.06604v1 HTML — §6 Future Work [facet=limitations]; https://arxiv.org/html/2603.06604v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06604v1.html; sha256:b44fd93eca16eb6c69cbb404264024ce5f5fc19c87c70858f6d474f950e48fd2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06604v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06604 | complete |
| SF-2026-ARXIV-2603-06626 | RP-c2dc7a51624fc032 | standard | arXiv:2603.06626v1 | SRC-ARXIV@arXiv:2603.06626v1 | arXiv:2603.06626v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06626v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06626v1.html; sha256:9cafa8157495112cc1b8bec356af6cb273cfbf99e405bebff190292318b5ef14 | arXiv:2603.06626v1 HTML — §Appendix I Downstream Experiments [facet=evaluation]; https://arxiv.org/html/2603.06626v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06626v1.html; sha256:9cafa8157495112cc1b8bec356af6cb273cfbf99e405bebff190292318b5ef14 | arXiv:2603.06626v1 HTML — §4.3 Discussion [facet=limitations]; https://arxiv.org/html/2603.06626v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06626v1.html; sha256:9cafa8157495112cc1b8bec356af6cb273cfbf99e405bebff190292318b5ef14 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06626v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06626 | complete |
| SF-2026-ARXIV-2603-06728 | RP-081941d43f76e138 | standard | arXiv:2603.06728v1 | SRC-ARXIV@arXiv:2603.06728v1 | arXiv:2603.06728v1 HTML — §4 System Design [facet=method]; https://arxiv.org/html/2603.06728v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06728v1.html; sha256:20c10acaf59830e80654ec10b300fac317d07dfb13d102ed6f13da27ee3dc398 | arXiv:2603.06728v1 HTML — §8 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06728v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06728v1.html; sha256:20c10acaf59830e80654ec10b300fac317d07dfb13d102ed6f13da27ee3dc398 | arXiv:2603.06728v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.06728v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06728v1.html; sha256:20c10acaf59830e80654ec10b300fac317d07dfb13d102ed6f13da27ee3dc398 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06728v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06728 | complete |
| SF-2026-ARXIV-2603-06798 | RP-c4192b7b9416a310 | standard | arXiv:2603.06798v1 | SRC-ARXIV@arXiv:2603.06798v1 | arXiv:2603.06798v1 HTML — §5.1 Methodology and Setup [facet=method]; https://arxiv.org/html/2603.06798v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06798v1.html; sha256:abfd5fa2fbf0f754a1e4feb2645f8dd14511040e1230316235300e6150b79da7 | arXiv:2603.06798v1 HTML — §A.6 Evaluation and expected results [facet=evaluation]; https://arxiv.org/html/2603.06798v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06798v1.html; sha256:abfd5fa2fbf0f754a1e4feb2645f8dd14511040e1230316235300e6150b79da7 | arXiv:2603.06798v1 HTML — §7 Limitation and Discussion [facet=limitations]; https://arxiv.org/html/2603.06798v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06798v1.html; sha256:abfd5fa2fbf0f754a1e4feb2645f8dd14511040e1230316235300e6150b79da7 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06798v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06798 | complete |
| SF-2026-ARXIV-2603-06847 | RP-378faf72d3fd8b05 | standard | arXiv:2603.06847v1 | SRC-ARXIV@arXiv:2603.06847v1 | arXiv:2603.06847v1 HTML — §2. Methodology [facet=method]; https://arxiv.org/html/2603.06847v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06847v1.html; sha256:a092be8ef6c1d706a918195ec2de09545c586398ad390efc9338216430406d4b | arXiv:2603.06847v1 HTML — §3.3.1. Quantitative Validation Results [facet=evaluation]; https://arxiv.org/html/2603.06847v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06847v1.html; sha256:a092be8ef6c1d706a918195ec2de09545c586398ad390efc9338216430406d4b | arXiv:2603.06847v1 HTML — §7. Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.06847v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06847v1.html; sha256:a092be8ef6c1d706a918195ec2de09545c586398ad390efc9338216430406d4b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06847v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06847 | complete |
| SF-2026-ARXIV-2603-07006 | RP-d432ec1b781a3076 | standard | arXiv:2603.07006v1 | SRC-ARXIV@arXiv:2603.07006v1 | arXiv:2603.07006v1 HTML — §𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures [facet=method]; https://arxiv.org/html/2603.07006v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07006v1.html; sha256:fe04160e0b4cca3154b0c18597e6fb8ca3eaab68aac20c7307fb5bda2c1a187d | arXiv:2603.07006v1 HTML — §Appendix B More Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.07006v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07006v1.html; sha256:fe04160e0b4cca3154b0c18597e6fb8ca3eaab68aac20c7307fb5bda2c1a187d | arXiv:2603.07006v1 HTML — §6 Conclusion and Limitations [facet=limitations]; https://arxiv.org/html/2603.07006v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07006v1.html; sha256:fe04160e0b4cca3154b0c18597e6fb8ca3eaab68aac20c7307fb5bda2c1a187d | arXiv exact-v1 identity https://arxiv.org/abs/2603.07006v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07006 | complete |
| SF-2026-ARXIV-2603-07373 | RP-793d3bbed988cb26 | standard | arXiv:2603.07373v1 | SRC-ARXIV@arXiv:2603.07373v1 | arXiv:2603.07373v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.07373v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07373v1.html; sha256:5d17313785cd1ea7bc1887406cb3b77c97dd9cc19658dc064d41876a5ee17b80 | arXiv:2603.07373v1 HTML — §V-C Benchmark Workload [facet=evaluation]; https://arxiv.org/html/2603.07373v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07373v1.html; sha256:5d17313785cd1ea7bc1887406cb3b77c97dd9cc19658dc064d41876a5ee17b80 | arXiv:2603.07373v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.07373v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07373v1.html; sha256:5d17313785cd1ea7bc1887406cb3b77c97dd9cc19658dc064d41876a5ee17b80 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07373v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07373 | complete |
| SF-2026-ARXIV-2603-07416 | RP-8668e029d1c94a15 | standard | arXiv:2603.07416v1 | SRC-ARXIV@arXiv:2603.07416v1 | arXiv:2603.07416v1 HTML — §6.3.1 speculation methods [facet=method]; https://arxiv.org/html/2603.07416v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07416v1.html; sha256:b8b91002da8590df3bf59ab26a155f9f26c70519f8fe939e51763719e40708aa | arXiv:2603.07416v1 HTML — §6.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.07416v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07416v1.html; sha256:b8b91002da8590df3bf59ab26a155f9f26c70519f8fe939e51763719e40708aa | arXiv:2603.07416v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.07416v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07416v1.html; sha256:b8b91002da8590df3bf59ab26a155f9f26c70519f8fe939e51763719e40708aa | arXiv exact-v1 identity https://arxiv.org/abs/2603.07416v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07416 | complete |
| SF-2026-ARXIV-2603-07427 | RP-dd5d341e94aaebe1 | standard | arXiv:2603.07427v1 | SRC-ARXIV@arXiv:2603.07427v1 | arXiv:2603.07427v1 HTML — §3.2 Architect Agent: Scenario Design [facet=method]; https://arxiv.org/html/2603.07427v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07427v1.html; sha256:4e789c108077ccc46ce404bb539949cff631eb8eba07041e1a30007dab591e00 | arXiv:2603.07427v1 HTML — §2.2 Simulation Paradigms for Agent Safety Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07427v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07427v1.html; sha256:4e789c108077ccc46ce404bb539949cff631eb8eba07041e1a30007dab591e00 | arXiv:2603.07427v1 HTML — §A.2 Limitations [facet=limitations]; https://arxiv.org/html/2603.07427v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07427v1.html; sha256:4e789c108077ccc46ce404bb539949cff631eb8eba07041e1a30007dab591e00 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07427v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07427 | complete |
| SF-2026-ARXIV-2603-07433 | RP-3d6bd7dc7b8df876 | standard | arXiv:2603.07433v1 | SRC-ARXIV@arXiv:2603.07433v1 | arXiv:2603.07433v1 HTML — §3 The Proposed Method [facet=method]; https://arxiv.org/html/2603.07433v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07433v1.html; sha256:4ca0c34dd2e8b7234f3de63c203a5c20009e51c8d064c11a977cacfa6c323971 | arXiv:2603.07433v1 HTML — §4.7 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.07433v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07433v1.html; sha256:4ca0c34dd2e8b7234f3de63c203a5c20009e51c8d064c11a977cacfa6c323971 | arXiv:2603.07433v1 HTML — §4.7 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.07433v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07433v1.html; sha256:4ca0c34dd2e8b7234f3de63c203a5c20009e51c8d064c11a977cacfa6c323971 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07433v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07433 | complete |
| SF-2026-ARXIV-2603-07466 | RP-9e7532e74c277089 | standard | arXiv:2603.07466v1 | SRC-ARXIV@arXiv:2603.07466v1 | arXiv:2603.07466v1 HTML — §4 Overview [facet=method]; https://arxiv.org/html/2603.07466v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07466v1.html; sha256:0f9e038f6c2996828d761e11205df03e95bcee1a7acd248b62f69e994b0734d3 | arXiv:2603.07466v1 HTML — §6.2 System Overhead Analysis [facet=evaluation]; https://arxiv.org/html/2603.07466v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07466v1.html; sha256:0f9e038f6c2996828d761e11205df03e95bcee1a7acd248b62f69e994b0734d3 | arXiv:2603.07466v1 HTML — §8.2 Limitations [facet=limitations]; https://arxiv.org/html/2603.07466v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07466v1.html; sha256:0f9e038f6c2996828d761e11205df03e95bcee1a7acd248b62f69e994b0734d3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07466v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07466 | complete |
| SF-2026-ARXIV-2603-07557 | RP-ef5a15f133645810 | standard | arXiv:2603.07557v1 | SRC-ARXIV@arXiv:2603.07557v1 | arXiv:2603.07557v1 HTML — §2.1. LLM Agent Architecture [facet=method]; https://arxiv.org/html/2603.07557v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07557v1.html; sha256:f914fbb59fa99700b41c4f5c7300080ff5c551264cd633c474d4dc796c4f2977 | arXiv:2603.07557v1 HTML — §5.1. Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.07557v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07557v1.html; sha256:f914fbb59fa99700b41c4f5c7300080ff5c551264cd633c474d4dc796c4f2977 | arXiv:2603.07557v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.07557v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07557v1.html; sha256:f914fbb59fa99700b41c4f5c7300080ff5c551264cd633c474d4dc796c4f2977 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07557v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07557 | complete |
| SF-2026-ARXIV-2603-07607 | RP-01370f2f0543484c | standard | arXiv:2603.07607v1 | SRC-ARXIV@arXiv:2603.07607v1 | arXiv:2603.07607v1 HTML — §3.4 Prototype Implementation [facet=method]; https://arxiv.org/html/2603.07607v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07607v1.html; sha256:d38b4f77ef045e9ebd1b2410c5b350222647f57d1d4898f4fbf74fa4b496ea95 | arXiv:2603.07607v1 HTML — §4.1.2 Evaluation Scenarios and Workload Profiles: [facet=evaluation]; https://arxiv.org/html/2603.07607v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07607v1.html; sha256:d38b4f77ef045e9ebd1b2410c5b350222647f57d1d4898f4fbf74fa4b496ea95 | arXiv:2603.07607v1 HTML — §5 Discussion and Future Work [facet=limitations]; https://arxiv.org/html/2603.07607v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07607v1.html; sha256:d38b4f77ef045e9ebd1b2410c5b350222647f57d1d4898f4fbf74fa4b496ea95 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07607v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07607 | complete |
| SF-2026-ARXIV-2603-07670 | RP-18afbea927072058 | standard | arXiv:2603.07670v1 | SRC-ARXIV@arXiv:2603.07670v1 | arXiv:2603.07670v1 HTML — §7.6 Three architecture patterns [facet=method]; https://arxiv.org/html/2603.07670v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07670v1.html; sha256:e62acc70d6286c162237f11626ea4437d035a71228cb13fad41125d27669db52 | arXiv:2603.07670v1 HTML — §9.10 Standardized evaluation [facet=evaluation]; https://arxiv.org/html/2603.07670v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07670v1.html; sha256:e62acc70d6286c162237f11626ea4437d035a71228cb13fad41125d27669db52 | arXiv:2603.07670v1 HTML — §10 Conclusion [facet=limitations]; https://arxiv.org/html/2603.07670v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07670v1.html; sha256:e62acc70d6286c162237f11626ea4437d035a71228cb13fad41125d27669db52 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07670v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07670 | complete |
| SF-2026-ARXIV-2603-07685 | RP-0c9adb3a97f80b46 | deep | arXiv:2603.07685v1 | SRC-ARXIV@arXiv:2603.07685v1 | arXiv:2603.07685v1 HTML — §2.1 token dispatch semantics + §3.3 Parallel Folding and Multi-Dimensional Framework [facet=method]; https://arxiv.org/html/2603.07685v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07685v1.html; sha256:c03f93b132fcea8a84e5b19c29d56410746588b168db08838655653b0f0337ac | arXiv:2603.07685v1 HTML — §8. Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07685v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07685v1.html; sha256:c03f93b132fcea8a84e5b19c29d56410746588b168db08838655653b0f0337ac | arXiv:2603.07685v1 HTML — §11. Conclusion [facet=limitations]; https://arxiv.org/html/2603.07685v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07685v1.html; sha256:c03f93b132fcea8a84e5b19c29d56410746588b168db08838655653b0f0337ac | arXiv exact-v1 identity https://arxiv.org/abs/2603.07685v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07685 | complete |
| SF-2026-ARXIV-2603-07770 | RP-2af38ea33a55f22a | standard | arXiv:2603.07770v1 | SRC-ARXIV@arXiv:2603.07770v1 | arXiv:2603.07770v1 HTML — §2 System Design [facet=method]; https://arxiv.org/html/2603.07770v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07770v1.html; sha256:fcddd0bc9c08d3e42d8d07051e800da248239a78dcd98d18bd66e8f3fdefc279 | arXiv:2603.07770v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.07770v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07770v1.html; sha256:fcddd0bc9c08d3e42d8d07051e800da248239a78dcd98d18bd66e8f3fdefc279 | arXiv:2603.07770v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.07770v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07770v1.html; sha256:fcddd0bc9c08d3e42d8d07051e800da248239a78dcd98d18bd66e8f3fdefc279 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07770v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07770 | complete |
| SF-2026-ARXIV-2603-07777 | RP-31a46b967af384a1 | standard | arXiv:2603.07777v1 | SRC-ARXIV@arXiv:2603.07777v1 | arXiv:2603.07777v1 HTML — §5 Experimental Design [facet=method]; https://arxiv.org/html/2603.07777v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07777v1.html; sha256:97f397fa6dafc805ba25355a963a93fe02423d3d491d73b3951c5d4eb6660597 | arXiv:2603.07777v1 HTML — §6 Results [facet=evaluation]; https://arxiv.org/html/2603.07777v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07777v1.html; sha256:97f397fa6dafc805ba25355a963a93fe02423d3d491d73b3951c5d4eb6660597 | arXiv:2603.07777v1 HTML — §8 Conclusions [facet=limitations]; https://arxiv.org/html/2603.07777v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07777v1.html; sha256:97f397fa6dafc805ba25355a963a93fe02423d3d491d73b3951c5d4eb6660597 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07777v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07777 | complete |
| SF-2026-ARXIV-2603-07799 | RP-ec5f50c699f43d62 | standard | arXiv:2603.07799v1 | SRC-ARXIV@arXiv:2603.07799v1 | arXiv:2603.07799v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.07799v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07799v1.html; sha256:d55bea37affff314998ffc0637e81bf1c0551c787e552f265cedb72be89735b4 | arXiv:2603.07799v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.07799v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07799v1.html; sha256:d55bea37affff314998ffc0637e81bf1c0551c787e552f265cedb72be89735b4 | arXiv:2603.07799v1 HTML — §V CONCLUSIONS [facet=limitations]; https://arxiv.org/html/2603.07799v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07799v1.html; sha256:d55bea37affff314998ffc0637e81bf1c0551c787e552f265cedb72be89735b4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07799v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07799 | complete |
| SF-2026-ARXIV-2603-07915 | RP-8099f60da182e5a2 | standard | arXiv:2603.07915v1 | SRC-ARXIV@arXiv:2603.07915v1 | arXiv:2603.07915v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.07915v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07915v1.html; sha256:756fa16a83b340be8688095669253f309ec25b617276b8417ad5b109e89b728d | arXiv:2603.07915v1 HTML — §4.6 Generalization Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07915v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07915v1.html; sha256:756fa16a83b340be8688095669253f309ec25b617276b8417ad5b109e89b728d | arXiv:2603.07915v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.07915v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07915v1.html; sha256:756fa16a83b340be8688095669253f309ec25b617276b8417ad5b109e89b728d | arXiv exact-v1 identity https://arxiv.org/abs/2603.07915v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07915 | complete |
| SF-2026-ARXIV-2603-07917 | RP-36af6c3b7cb7ed19 | standard | arXiv:2603.07917v1 | SRC-ARXIV@arXiv:2603.07917v1 | arXiv:2603.07917v1 HTML — §4.3.2 Superiority of our Cost Modeling Method [facet=method]; https://arxiv.org/html/2603.07917v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07917v1.html; sha256:4cdc67f8eea82fa2b1b541b36bceb1431b34d1f3e843cc88d46bab5dec91681f | arXiv:2603.07917v1 HTML — §4.4 Overhead and Sensitivity Analysis [facet=evaluation]; https://arxiv.org/html/2603.07917v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07917v1.html; sha256:4cdc67f8eea82fa2b1b541b36bceb1431b34d1f3e843cc88d46bab5dec91681f | arXiv:2603.07917v1 HTML — §2.2 Limitations of Existing LLM Schedulers [facet=limitations]; https://arxiv.org/html/2603.07917v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07917v1.html; sha256:4cdc67f8eea82fa2b1b541b36bceb1431b34d1f3e843cc88d46bab5dec91681f | arXiv exact-v1 identity https://arxiv.org/abs/2603.07917v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07917 | complete |
| SF-2026-ARXIV-2603-07972 | RP-a8fa0133961ef930 | standard | arXiv:2603.07972v1 | SRC-ARXIV@arXiv:2603.07972v1 | arXiv:2603.07972v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.07972v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07972v1.html; sha256:6044fd36fc2c4b63946eaa962d9203957ea319782880d9dbeb2ccb07dedf92f6 | arXiv:2603.07972v1 HTML — §C.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.07972v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07972v1.html; sha256:6044fd36fc2c4b63946eaa962d9203957ea319782880d9dbeb2ccb07dedf92f6 | arXiv:2603.07972v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.07972v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07972v1.html; sha256:6044fd36fc2c4b63946eaa962d9203957ea319782880d9dbeb2ccb07dedf92f6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.07972v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-07972 | complete |
| SF-2026-ARXIV-2603-08088 | RP-9d6b448a80780d64 | deep | arXiv:2603.08088v1 | SRC-ARXIV@arXiv:2603.08088v1 | arXiv:2603.08088v1 HTML — §3.1–§3.3 Branchable KV, tree tensor semantics and fused teacher execution [facet=method]; https://arxiv.org/html/2603.08088v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08088v1.html; sha256:9ce1216fe34d509a0536f16b4caa5c0ee8e31f09f4c28a86b493083bc73be927 | arXiv:2603.08088v1 HTML — §4.5 timing methodology + §5.1–§5.2 experiments [facet=evaluation]; https://arxiv.org/html/2603.08088v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08088v1.html; sha256:9ce1216fe34d509a0536f16b4caa5c0ee8e31f09f4c28a86b493083bc73be927 | arXiv:2603.08088v1 HTML — §Limitations and future work. [facet=limitations]; https://arxiv.org/html/2603.08088v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08088v1.html; sha256:9ce1216fe34d509a0536f16b4caa5c0ee8e31f09f4c28a86b493083bc73be927 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08088v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08088 | complete |
| SF-2026-ARXIV-2603-08113 | RP-f69c9dc34aef9e7a | standard | arXiv:2603.08113v1 | SRC-ARXIV@arXiv:2603.08113v1 | arXiv:2603.08113v1 HTML — §3.1 Method Architecture [facet=method]; https://arxiv.org/html/2603.08113v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08113v1.html; sha256:5ea7dccba7a8d724011d2eb18c5d491b2dbabaa889e30a60456cd8fff8e3d4b3 | arXiv:2603.08113v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08113v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08113v1.html; sha256:5ea7dccba7a8d724011d2eb18c5d491b2dbabaa889e30a60456cd8fff8e3d4b3 | arXiv:2603.08113v1 HTML — §Fundamental Limitation of Token-Level Routing Under Local Information [facet=limitations]; https://arxiv.org/html/2603.08113v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08113v1.html; sha256:5ea7dccba7a8d724011d2eb18c5d491b2dbabaa889e30a60456cd8fff8e3d4b3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08113v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08113 | complete |
| SF-2026-ARXIV-2603-08124 | RP-8ef58e313a0ccd79 | standard | arXiv:2603.08124v1 | SRC-ARXIV@arXiv:2603.08124v1 | arXiv:2603.08124v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.08124v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08124v1.html; sha256:3df00ccd1225bf338f0d3460c46c974c27bd4dd8fe4f04975b131e3ff6c645c4 | arXiv:2603.08124v1 HTML — §Historical prototype settings (not used in main results). [facet=evaluation]; https://arxiv.org/html/2603.08124v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08124v1.html; sha256:3df00ccd1225bf338f0d3460c46c974c27bd4dd8fe4f04975b131e3ff6c645c4 | arXiv:2603.08124v1 HTML — §6 Limitations & Ethics [facet=limitations]; https://arxiv.org/html/2603.08124v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08124v1.html; sha256:3df00ccd1225bf338f0d3460c46c974c27bd4dd8fe4f04975b131e3ff6c645c4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08124v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08124 | complete |
| SF-2026-ARXIV-2603-08163 | RP-cce0c016edbb29e6 | standard | arXiv:2603.08163v1 | SRC-ARXIV@arXiv:2603.08163v1 | arXiv:2603.08163v1 HTML — §2.1 SparseLoCo [facet=method]; https://arxiv.org/html/2603.08163v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08163v1.html; sha256:5cdb0a0c235eb4caa40a3e0a24a4b786854a181b585434928db62f79d7f75ea5 | arXiv:2603.08163v1 HTML — §4.2 Main Pre-Training Results [facet=evaluation]; https://arxiv.org/html/2603.08163v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08163v1.html; sha256:5cdb0a0c235eb4caa40a3e0a24a4b786854a181b585434928db62f79d7f75ea5 | arXiv:2603.08163v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.08163v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08163v1.html; sha256:5cdb0a0c235eb4caa40a3e0a24a4b786854a181b585434928db62f79d7f75ea5 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08163v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08163 | complete |
| SF-2026-ARXIV-2603-08221 | RP-1c20bfa7e8f90c1c | standard | arXiv:2603.08221v1 | SRC-ARXIV@arXiv:2603.08221v1 | arXiv:2603.08221v1 HTML — §IV-A Architecture Overview [facet=method]; https://arxiv.org/html/2603.08221v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08221v1.html; sha256:de025298e41a00f7a3934b5cfa73b511ee2b74255a06db6a18b13d275f3d2ddc | arXiv:2603.08221v1 HTML — §VII Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08221v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08221v1.html; sha256:de025298e41a00f7a3934b5cfa73b511ee2b74255a06db6a18b13d275f3d2ddc | arXiv:2603.08221v1 HTML — §VIII-B Limitations [facet=limitations]; https://arxiv.org/html/2603.08221v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08221v1.html; sha256:de025298e41a00f7a3934b5cfa73b511ee2b74255a06db6a18b13d275f3d2ddc | arXiv exact-v1 identity https://arxiv.org/abs/2603.08221v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08221 | complete |
| SF-2026-ARXIV-2603-08316 | RP-7254655e7473e86e | standard | arXiv:2603.08316v1 | SRC-ARXIV@arXiv:2603.08316v1 | arXiv:2603.08316v1 HTML — §4.2 Method Overview [facet=method]; https://arxiv.org/html/2603.08316v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08316v1.html; sha256:07b5c5e87e64d80e42010ca75b1b40f3c2eb0cabca270c01fb07fade927a3b1a | arXiv:2603.08316v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08316v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08316v1.html; sha256:07b5c5e87e64d80e42010ca75b1b40f3c2eb0cabca270c01fb07fade927a3b1a | arXiv:2603.08316v1 HTML — §5.3 Ablation Study [facet=limitations]; https://arxiv.org/html/2603.08316v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08316v1.html; sha256:07b5c5e87e64d80e42010ca75b1b40f3c2eb0cabca270c01fb07fade927a3b1a | arXiv exact-v1 identity https://arxiv.org/abs/2603.08316v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08316 | complete |
| SF-2026-ARXIV-2603-08361 | RP-16205d7d6b8908a2 | standard | arXiv:2603.08361v1 | SRC-ARXIV@arXiv:2603.08361v1 | arXiv:2603.08361v1 HTML — §IV 𝚫\DeltaVLA [facet=method]; https://arxiv.org/html/2603.08361v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08361v1.html; sha256:e70572e92dcad3b22c8868b8ed16e248ac9e83ccb451077907643cb26d7b79c8 | arXiv:2603.08361v1 HTML — §V-C Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.08361v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08361v1.html; sha256:e70572e92dcad3b22c8868b8ed16e248ac9e83ccb451077907643cb26d7b79c8 | arXiv:2603.08361v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.08361v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08361v1.html; sha256:e70572e92dcad3b22c8868b8ed16e248ac9e83ccb451077907643cb26d7b79c8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08361v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08361 | complete |
| SF-2026-ARXIV-2603-08429 | RP-4565c90a4e0d6c3b | standard | arXiv:2603.08429v1 | SRC-ARXIV@arXiv:2603.08429v1 | arXiv:2603.08429v1 HTML — §3.3 Projection Head Architecture [facet=method]; https://arxiv.org/html/2603.08429v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08429v1.html; sha256:03542ce6050aecdfdef82d6d59daea1fe7c099748228ebfe33f7b37650c57a04 | arXiv:2603.08429v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08429v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08429v1.html; sha256:03542ce6050aecdfdef82d6d59daea1fe7c099748228ebfe33f7b37650c57a04 | arXiv:2603.08429v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.08429v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08429v1.html; sha256:03542ce6050aecdfdef82d6d59daea1fe7c099748228ebfe33f7b37650c57a04 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08429v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08429 | complete |
| SF-2026-ARXIV-2603-08519 | RP-939123cbdfcc0996 | standard | arXiv:2603.08519v1 | SRC-ARXIV@arXiv:2603.08519v1 | arXiv:2603.08519v1 HTML — §III-A Model Architecture [facet=method]; https://arxiv.org/html/2603.08519v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08519v1.html; sha256:04ceb53c35fa56a73fa80aa88f00babcf602f70873f27644006c58a9fcff2fc1 | arXiv:2603.08519v1 HTML — §IV-B Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.08519v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08519v1.html; sha256:04ceb53c35fa56a73fa80aa88f00babcf602f70873f27644006c58a9fcff2fc1 | arXiv:2603.08519v1 HTML — §VI CONCLUSION [facet=limitations]; https://arxiv.org/html/2603.08519v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08519v1.html; sha256:04ceb53c35fa56a73fa80aa88f00babcf602f70873f27644006c58a9fcff2fc1 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08519v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08519 | complete |
| SF-2026-ARXIV-2603-08546 | RP-cb44cd299b3acfde | standard | arXiv:2603.08546v1 | SRC-ARXIV@arXiv:2603.08546v1 | arXiv:2603.08546v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.08546v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08546v1.html; sha256:8f7c6f8e7792ef68413fcfdd67605d55cb85c1cc267da2058e42e503cb588ed8 | arXiv:2603.08546v1 HTML — §II-C Imitation Policy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08546v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08546v1.html; sha256:8f7c6f8e7792ef68413fcfdd67605d55cb85c1cc267da2058e42e503cb588ed8 | arXiv:2603.08546v1 HTML — §V Conclusion [facet=limitations]; https://arxiv.org/html/2603.08546v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08546v1.html; sha256:8f7c6f8e7792ef68413fcfdd67605d55cb85c1cc267da2058e42e503cb588ed8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08546v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08546 | complete |
| SF-2026-ARXIV-2603-08640 | RP-ca452e9821517530 | standard | arXiv:2603.08640v1 | SRC-ARXIV@arXiv:2603.08640v1 | arXiv:2603.08640v1 HTML — §5.2 Post-Training Method Selection [facet=method]; https://arxiv.org/html/2603.08640v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08640v1.html; sha256:373c8c9339989e0c40da25ef338f26fdbcb3185ddf18a541c72399b228955090 | arXiv:2603.08640v1 HTML — §3.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08640v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08640v1.html; sha256:373c8c9339989e0c40da25ef338f26fdbcb3185ddf18a541c72399b228955090 | arXiv:2603.08640v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2603.08640v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08640v1.html; sha256:373c8c9339989e0c40da25ef338f26fdbcb3185ddf18a541c72399b228955090 | arXiv exact-v1 identity https://arxiv.org/abs/2603.08640v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-08640 | complete |

### Source Reviews

### vLLM Hook v0: A Plug-in for Programming Model Internals on vLLM

<!-- review:SF-2026-ARXIV-2603-06588:start -->
**问题**：高性能 serving engine 封装内部 state 后，activation probe、steering 与安全 monitor 无法在不 fork runtime 时接入。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：vLLM Hook 以配置声明捕获点，并区分只读 probe 与主动修改，使内部状态干预成为显式扩展接口。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.06588v1 HTML — §2 Core Functions of vLLM Hook [facet=method]; https://arxiv.org/html/2603.06588v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06588v1.html; sha256:48d124e03a9ac718b7c7837e4684af271c49ac62032353cd42690769b7643f64`。

**Evaluation contract 与未证明部分**：实现与实验只证明特定 vLLM 版本/模型中的可编程性和开销；不证明任意 intervention 保持 correctness。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.06588v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06588v1.html; sha256:48d124e03a9ac718b7c7837e4684af271c49ac62032353cd42690769b7643f64`。

**Trade-off / failure / coexistence**：开放 hook 扩大 ABI、隔离和安全面；不需要内部干预的生产服务应保留封闭快路径。

<!-- claim:SF-2026-ARXIV-2603-06588:start -->**Claim Boundary**：只支持 arXiv:2603.06588v1 §2 Core Functions of vLLM Hook 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06588:end -->
<!-- review:SF-2026-ARXIV-2603-06588:end -->
### Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection

<!-- review:SF-2026-ARXIV-2603-06604:start -->
**问题**：模型自报置信度常与正确性错配，阈值化拒答无法仅凭 token probability 获得可靠 assurance。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：该工作把 confidence-correctness alignment 作为单独训练/校准目标，并比较 error detection 而非只看 accuracy。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06604v1 HTML — §3 Know When You’re Wrong [facet=method]; https://arxiv.org/html/2603.06604v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06604v1.html; sha256:b44fd93eca16eb6c69cbb404264024ce5f5fc19c87c70858f6d474f950e48fd2`。

**Evaluation contract 与未证明部分**：公开结果限于所测任务、模型和 calibration split；不能把分数解释为开放世界真实概率。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06604v1 HTML — §3.3 Confidence Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06604v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06604v1.html; sha256:b44fd93eca16eb6c69cbb404264024ce5f5fc19c87c70858f6d474f950e48fd2`。

**Trade-off / failure / coexistence**：校准提高选择性但会牺牲 coverage，并随分布漂移失效；高风险结论仍需外部 evidence verification。

<!-- claim:SF-2026-ARXIV-2603-06604:start -->**Claim Boundary**：只支持 arXiv:2603.06604v1 §3 Know When You’re Wrong 的机制与 §3.3 Confidence Evaluation 的公开 workload；§6 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06604:end -->
<!-- review:SF-2026-ARXIV-2603-06604:end -->
### Grouter: Decoupling Routing from Representation for Accelerated MoE Training

<!-- review:SF-2026-ARXIV-2603-06626:start -->
**问题**：`Grouter: Decoupling Routing from Representation for Accelerated MoE Training` 检查的是 `MODEL-MOE` 中 容量扩大后，激活成本和通信使全参数计算不可持续。 是否会改变现有设计边界。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：exact-v1 的 `3 Method` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.06626v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06626v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06626v1.html; sha256:9cafa8157495112cc1b8bec356af6cb273cfbf99e405bebff190292318b5ef14`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix I Downstream Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06626v1 HTML — §Appendix I Downstream Experiments [facet=evaluation]; https://arxiv.org/html/2603.06626v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06626v1.html; sha256:9cafa8157495112cc1b8bec356af6cb273cfbf99e405bebff190292318b5ef14`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.3 Discussion`。规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2603-06626:start -->**Claim Boundary**：只支持 arXiv:2603.06626v1 §3 Method 的机制与 §Appendix I Downstream Experiments 的公开 workload；§4.3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06626:end -->
<!-- review:SF-2026-ARXIV-2603-06626:end -->
### Orion: Characterizing and Programming Apple's Neural Engine for LLM Training and Inference

<!-- review:SF-2026-ARXIV-2603-06728:start -->
**问题**：Apple Neural Engine 缺少公开编程模型时，LLM 训练/推理 placement 只能把它当黑盒能力。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：Orion 逆向刻画指令、memory 与执行限制，并把可运行算子映射到训练/推理 execution plan。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.06728v1 HTML — §4 System Design [facet=method]; https://arxiv.org/html/2603.06728v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06728v1.html; sha256:20c10acaf59830e80654ec10b300fac317d07dfb13d102ed6f13da27ee3dc398`。

**Evaluation contract 与未证明部分**：测量只属于测试芯片、OS 与工具链版本；不证明未公开设备代际具有相同语义。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06728v1 HTML — §8 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06728v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06728v1.html; sha256:20c10acaf59830e80654ec10b300fac317d07dfb13d102ed6f13da27ee3dc398`。

**Trade-off / failure / coexistence**：专用映射提高设备利用率却承担兼容与正确性风险；稳定受支持路径仍应优先官方 runtime。

<!-- claim:SF-2026-ARXIV-2603-06728:start -->**Claim Boundary**：只支持 arXiv:2603.06728v1 §4 System Design 的机制与 §8 Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06728:end -->
<!-- review:SF-2026-ARXIV-2603-06728:end -->
### NEST: Network- and Memory-Aware Device Placement For Distributed Deep Learning

<!-- review:SF-2026-ARXIV-2603-06798:start -->
**问题**：分布式训练 placement 若只考虑计算量，会把 activation、optimizer state 与网络拓扑的峰值分开优化。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：NEST 联合建模 device memory、通信拓扑和 operator dependency，搜索满足容量约束的 placement。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.06798v1 HTML — §5.1 Methodology and Setup [facet=method]; https://arxiv.org/html/2603.06798v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06798v1.html; sha256:abfd5fa2fbf0f754a1e4feb2645f8dd14511040e1230316235300e6150b79da7`。

**Evaluation contract 与未证明部分**：作者工作负载支持所测拓扑中的峰值内存/通信权衡；不证明搜索在超大动态图中可及时收敛。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06798v1 HTML — §A.6 Evaluation and expected results [facet=evaluation]; https://arxiv.org/html/2603.06798v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06798v1.html; sha256:abfd5fa2fbf0f754a1e4feb2645f8dd14511040e1230316235300e6150b79da7`。

**Trade-off / failure / coexistence**：全局建模改善放置却提高 profile 和搜索成本；同质小集群仍适合规则化并行策略。

<!-- claim:SF-2026-ARXIV-2603-06798:start -->**Claim Boundary**：只支持 arXiv:2603.06798v1 §5.1 Methodology and Setup 的机制与 §A.6 Evaluation and expected results 的公开 workload；§7 Limitation and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06798:end -->
<!-- review:SF-2026-ARXIV-2603-06798:end -->
### Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes

<!-- review:SF-2026-ARXIV-2603-06847:start -->
**问题**：agentic AI 的失败跨模型、tool、memory 与 orchestration 传播，按单一异常标签无法定位责任。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：该 taxonomy 用真实 failure report 区分类型、症状和根因，为 fault injection 与 evidence schema 提供分母。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06847v1 HTML — §2. Methodology [facet=method]; https://arxiv.org/html/2603.06847v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06847v1.html; sha256:a092be8ef6c1d706a918195ec2de09545c586398ad390efc9338216430406d4b`。

**Evaluation contract 与未证明部分**：研究能支持其样本中的故障类别，不证明 taxonomy 对未来 agent runtime 完备。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06847v1 HTML — §3.3.1. Quantitative Validation Results [facet=evaluation]; https://arxiv.org/html/2603.06847v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.06847v1.html; sha256:a092be8ef6c1d706a918195ec2de09545c586398ad390efc9338216430406d4b`。

**Trade-off / failure / coexistence**：更细分类改善归因但增加标注歧义；边界清晰的单工具应用仍可使用传统故障分类。

<!-- claim:SF-2026-ARXIV-2603-06847:start -->**Claim Boundary**：只支持 arXiv:2603.06847v1 §2. Methodology 的机制与 §3.3.1. Quantitative Validation Results 的公开 workload；§7. Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06847:end -->
<!-- review:SF-2026-ARXIV-2603-06847:end -->
### Mozart: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures

<!-- review:SF-2026-ARXIV-2603-07006:start -->
**问题**：`Mozart: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures` 检查的是 `TRAIN-DISTRIBUTED-TRAINING` 中 参数、optimizer state 和通信规模越过单设备边界。 是否会改变现有设计边界。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：exact-v1 的 `𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.07006v1 HTML — §𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures [facet=method]; https://arxiv.org/html/2603.07006v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07006v1.html; sha256:fe04160e0b4cca3154b0c18597e6fb8ca3eaab68aac20c7307fb5bda2c1a187d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix B More Experimental Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07006v1 HTML — §Appendix B More Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.07006v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07006v1.html; sha256:fe04160e0b4cca3154b0c18597e6fb8ca3eaab68aac20c7307fb5bda2c1a187d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion and Limitations`。模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2603-07006:start -->**Claim Boundary**：只支持 arXiv:2603.07006v1 §𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures 的机制与 §Appendix B More Experimental Results 的公开 workload；§6 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07006:end -->
<!-- review:SF-2026-ARXIV-2603-07006:end -->
### Scheduling Parallel Optical Circuit Switches for AI Training

<!-- review:SF-2026-ARXIV-2603-07373:start -->
**问题**：`Scheduling Parallel Optical Circuit Switches for AI Training` 检查的是 `TRAIN-DISTRIBUTED-TRAINING` 中 参数、optimizer state 和通信规模越过单设备边界。 是否会改变现有设计边界。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：exact-v1 的 `III-A Overview` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.07373v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.07373v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07373v1.html; sha256:5d17313785cd1ea7bc1887406cb3b77c97dd9cc19658dc064d41876a5ee17b80`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V-C Benchmark Workload`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07373v1 HTML — §V-C Benchmark Workload [facet=evaluation]; https://arxiv.org/html/2603.07373v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07373v1.html; sha256:5d17313785cd1ea7bc1887406cb3b77c97dd9cc19658dc064d41876a5ee17b80`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VI Conclusion`。模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2603-07373:start -->**Claim Boundary**：只支持 arXiv:2603.07373v1 §III-A Overview 的机制与 §V-C Benchmark Workload 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07373:end -->
<!-- review:SF-2026-ARXIV-2603-07373:end -->
### DualSpec: Accelerating Deep Research Agents via Dual-Process Action Speculation

<!-- review:SF-2026-ARXIV-2603-07416:start -->
**问题**：`DualSpec: Accelerating Deep Research Agents via Dual-Process Action Speculation` 检查的是 `INFER-SPECULATIVE-DECODING` 中 decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。 是否会改变现有设计边界。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：exact-v1 的 `6.3.1 speculation methods` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.07416v1 HTML — §6.3.1 speculation methods [facet=method]; https://arxiv.org/html/2603.07416v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07416v1.html; sha256:b8b91002da8590df3bf59ab26a155f9f26c70519f8fe939e51763719e40708aa`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07416v1 HTML — §6.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.07416v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07416v1.html; sha256:b8b91002da8590df3bf59ab26a155f9f26c70519f8fe939e51763719e40708aa`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion`。接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2603-07416:start -->**Claim Boundary**：只支持 arXiv:2603.07416v1 §6.3.1 speculation methods 的机制与 §6.2 Main Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07416:end -->
<!-- review:SF-2026-ARXIV-2603-07416:end -->
### AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation

<!-- review:SF-2026-ARXIV-2603-07427:start -->
**问题**：`AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.2 Architect Agent: Scenario Design` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.07427v1 HTML — §3.2 Architect Agent: Scenario Design [facet=method]; https://arxiv.org/html/2603.07427v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07427v1.html; sha256:4e789c108077ccc46ce404bb539949cff631eb8eba07041e1a30007dab591e00`。

**Evaluation contract 与未证明部分**：公开验证定位在 `2.2 Simulation Paradigms for Agent Safety Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07427v1 HTML — §2.2 Simulation Paradigms for Agent Safety Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07427v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07427v1.html; sha256:4e789c108077ccc46ce404bb539949cff631eb8eba07041e1a30007dab591e00`。

**Trade-off / failure / coexistence**：限制与反证定位在 `A.2 Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-07427:start -->**Claim Boundary**：只支持 arXiv:2603.07427v1 §3.2 Architect Agent: Scenario Design 的机制与 §2.2 Simulation Paradigms for Agent Safety Evaluation 的公开 workload；§A.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07427:end -->
<!-- review:SF-2026-ARXIV-2603-07427:end -->
### Data Agent: Learning to Select Data via End-to-End Dynamic Optimization

<!-- review:SF-2026-ARXIV-2603-07433:start -->
**问题**：`Data Agent: Learning to Select Data via End-to-End Dynamic Optimization` 检查的是 `TRAIN-DATA` 中 数据质量、难度和策略能力随训练变化，使静态配比逐渐失去信息效率。 是否会改变现有设计边界。

**旧路径为何合理**：固定离线数据集让训练可复现，也避免在线选择反馈回路。

**约束变化与机制**：exact-v1 的 `3 The Proposed Method` 把论文方案定位到 样本 identity、选择策略、版本、provenance 与训练消费顺序；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DATA` 负责 样本 identity、选择策略、版本、provenance 与训练消费顺序；定位证据为 `arXiv:2603.07433v1 HTML — §3 The Proposed Method [facet=method]; https://arxiv.org/html/2603.07433v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07433v1.html; sha256:4ca0c34dd2e8b7234f3de63c203a5c20009e51c8d064c11a977cacfa6c323971`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.7 Ablation Study`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07433v1 HTML — §4.7 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.07433v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07433v1.html; sha256:4ca0c34dd2e8b7234f3de63c203a5c20009e51c8d064c11a977cacfa6c323971`。

**Trade-off / failure / coexistence**：限制与反证定位在 `4.7 Ablation Study`。数据分布稳定且治理优先时，冻结数据仍是更安全的基线。

<!-- claim:SF-2026-ARXIV-2603-07433:start -->**Claim Boundary**：只支持 arXiv:2603.07433v1 §3 The Proposed Method 的机制与 §4.7 Ablation Study 的公开 workload；§4.7 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07433:end -->
<!-- review:SF-2026-ARXIV-2603-07433:end -->
### Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI

<!-- review:SF-2026-ARXIV-2603-07466:start -->
**问题**：`Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `4 Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.07466v1 HTML — §4 Overview [facet=method]; https://arxiv.org/html/2603.07466v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07466v1.html; sha256:0f9e038f6c2996828d761e11205df03e95bcee1a7acd248b62f69e994b0734d3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.2 System Overhead Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07466v1 HTML — §6.2 System Overhead Analysis [facet=evaluation]; https://arxiv.org/html/2603.07466v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07466v1.html; sha256:0f9e038f6c2996828d761e11205df03e95bcee1a7acd248b62f69e994b0734d3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8.2 Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-07466:start -->**Claim Boundary**：只支持 arXiv:2603.07466v1 §4 Overview 的机制与 §6.2 System Overhead Analysis 的公开 workload；§8.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07466:end -->
<!-- review:SF-2026-ARXIV-2603-07466:end -->
### AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents

<!-- review:SF-2026-ARXIV-2603-07557:start -->
**问题**：`AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `2.1. LLM Agent Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.07557v1 HTML — §2.1. LLM Agent Architecture [facet=method]; https://arxiv.org/html/2603.07557v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07557v1.html; sha256:f914fbb59fa99700b41c4f5c7300080ff5c551264cd633c474d4dc796c4f2977`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.1. Evaluation Setup`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07557v1 HTML — §5.1. Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.07557v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07557v1.html; sha256:f914fbb59fa99700b41c4f5c7300080ff5c551264cd633c474d4dc796c4f2977`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Discussion`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-07557:start -->**Claim Boundary**：只支持 arXiv:2603.07557v1 §2.1. LLM Agent Architecture 的机制与 §5.1. Evaluation Setup 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07557:end -->
<!-- review:SF-2026-ARXIV-2603-07557:end -->
### MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling

<!-- review:SF-2026-ARXIV-2603-07607:start -->
**问题**：`MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `3.4 Prototype Implementation` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.07607v1 HTML — §3.4 Prototype Implementation [facet=method]; https://arxiv.org/html/2603.07607v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07607v1.html; sha256:d38b4f77ef045e9ebd1b2410c5b350222647f57d1d4898f4fbf74fa4b496ea95`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1.2 Evaluation Scenarios and Workload Profiles:`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07607v1 HTML — §4.1.2 Evaluation Scenarios and Workload Profiles: [facet=evaluation]; https://arxiv.org/html/2603.07607v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07607v1.html; sha256:d38b4f77ef045e9ebd1b2410c5b350222647f57d1d4898f4fbf74fa4b496ea95`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Discussion and Future Work`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-07607:start -->**Claim Boundary**：只支持 arXiv:2603.07607v1 §3.4 Prototype Implementation 的机制与 §4.1.2 Evaluation Scenarios and Workload Profiles: 的公开 workload；§5 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07607:end -->
<!-- review:SF-2026-ARXIV-2603-07607:end -->
### Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers

<!-- review:SF-2026-ARXIV-2603-07670:start -->
**问题**：`Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `7.6 Three architecture patterns` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.07670v1 HTML — §7.6 Three architecture patterns [facet=method]; https://arxiv.org/html/2603.07670v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07670v1.html; sha256:e62acc70d6286c162237f11626ea4437d035a71228cb13fad41125d27669db52`。

**Evaluation contract 与未证明部分**：公开验证定位在 `9.10 Standardized evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07670v1 HTML — §9.10 Standardized evaluation [facet=evaluation]; https://arxiv.org/html/2603.07670v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07670v1.html; sha256:e62acc70d6286c162237f11626ea4437d035a71228cb13fad41125d27669db52`。

**Trade-off / failure / coexistence**：限制与反证定位在 `10 Conclusion`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-07670:start -->**Claim Boundary**：只支持 arXiv:2603.07670v1 §7.6 Three architecture patterns 的机制与 §9.10 Standardized evaluation 的公开 workload；§10 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07670:end -->
<!-- review:SF-2026-ARXIV-2603-07670:end -->
### Scalable Training of Mixture-of-Experts Models with Megatron Core

<!-- review:SF-2026-ARXIV-2603-07685:start -->
**问题**：MoE 训练不能只在 dense 并行方案上附加 all-to-all：expert capacity、token dispatch 和并行维度会共同改变通信临界路径。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：该工作在 Megatron Core 中把 expert parallel、tensor/data/pipeline parallel 及 dispatcher 实现组合为统一训练配置，并显式管理 token permutation 与负载均衡。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责训练状态分片、collective、同步与故障恢复；§2.1 只定义 token dispatch，parallel folding 与 EP/TP/DP/PP 组合的决定性定位是 exact-v1 §3.3，§8 给出测量配置。

**Evaluation contract 与未证明部分**：结果证明公开模型和集群配置中的扩展行为；没有披露或未覆盖的网络、失败恢复与极端路由倾斜仍需独立验证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07685v1 HTML — §8. Performance Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07685v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07685v1.html; sha256:c03f93b132fcea8a84e5b19c29d56410746588b168db08838655653b0f0337ac`。

**Trade-off / failure / coexistence**：多维并行提高大规模吞吐，但配置空间、collective 干扰和 straggler 风险同步上升；规模较小时 dense 或较少并行维度更易稳定。

<!-- claim:SF-2026-ARXIV-2603-07685:start -->**Claim Boundary**：§2.1 只建立 token dispatch 语义；parallel folding 与多维并行组合由 arXiv:2603.07685v1 §3.3 支持，测量边界为 §8；§11 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07685:end -->
<!-- review:SF-2026-ARXIV-2603-07685:end -->
### ArcLight: A Lightweight LLM Inference Architecture for Many-Core CPUs

<!-- review:SF-2026-ARXIV-2603-07770:start -->
**问题**：`ArcLight: A Lightweight LLM Inference Architecture for Many-Core CPUs` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `2 System Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.07770v1 HTML — §2 System Design [facet=method]; https://arxiv.org/html/2603.07770v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07770v1.html; sha256:fcddd0bc9c08d3e42d8d07051e800da248239a78dcd98d18bd66e8f3fdefc279`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07770v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.07770v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07770v1.html; sha256:fcddd0bc9c08d3e42d8d07051e800da248239a78dcd98d18bd66e8f3fdefc279`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-07770:start -->**Claim Boundary**：只支持 arXiv:2603.07770v1 §2 System Design 的机制与 §4 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07770:end -->
<!-- review:SF-2026-ARXIV-2603-07770:end -->
### Breaking Training Bottlenecks: Effective and Stable Reinforcement Learning for Coding Models

<!-- review:SF-2026-ARXIV-2603-07777:start -->
**问题**：`Breaking Training Bottlenecks: Effective and Stable Reinforcement Learning for Coding Models` 检查的是 `TRAIN-GRPO` 中 稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。 是否会改变现有设计边界。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：exact-v1 的 `5 Experimental Design` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.07777v1 HTML — §5 Experimental Design [facet=method]; https://arxiv.org/html/2603.07777v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07777v1.html; sha256:97f397fa6dafc805ba25355a963a93fe02423d3d491d73b3951c5d4eb6660597`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07777v1 HTML — §6 Results [facet=evaluation]; https://arxiv.org/html/2603.07777v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07777v1.html; sha256:97f397fa6dafc805ba25355a963a93fe02423d3d491d73b3951c5d4eb6660597`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Conclusions`。高质量逐样本监督充足时 SFT/DPO 仍更简单。

<!-- claim:SF-2026-ARXIV-2603-07777:start -->**Claim Boundary**：只支持 arXiv:2603.07777v1 §5 Experimental Design 的机制与 §6 Results 的公开 workload；§8 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07777:end -->
<!-- review:SF-2026-ARXIV-2603-07777:end -->
### MWM: Mobile World Models for Action-Conditioned Consistent Prediction

<!-- review:SF-2026-ARXIV-2603-07799:start -->
**问题**：`MWM: Mobile World Models for Action-Conditioned Consistent Prediction` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `III-A Overview` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.07799v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.07799v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07799v1.html; sha256:d55bea37affff314998ffc0637e81bf1c0551c787e552f265cedb72be89735b4`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV-B Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07799v1 HTML — §IV-B Main Results [facet=evaluation]; https://arxiv.org/html/2603.07799v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07799v1.html; sha256:d55bea37affff314998ffc0637e81bf1c0551c787e552f265cedb72be89735b4`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V CONCLUSIONS`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-07799:start -->**Claim Boundary**：只支持 arXiv:2603.07799v1 §III-A Overview 的机制与 §IV-B Main Results 的公开 workload；§V CONCLUSIONS 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07799:end -->
<!-- review:SF-2026-ARXIV-2603-07799:end -->
### Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents

<!-- review:SF-2026-ARXIV-2603-07915:start -->
**问题**：`Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents` 检查的是 `AGENT-PLANNING` 中 自演化与长链任务需要区分已知、未知和可验证的下一步。 是否会改变现有设计边界。

**旧路径为何合理**：按当前 prompt 即时选择下一步，在短任务中无需维护额外 epistemic state。

**约束变化与机制**：exact-v1 的 `3 Method` 把论文方案定位到 计划路由、证据需求与停止条件；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-PLANNING` 负责 计划路由、证据需求与停止条件；定位证据为 `arXiv:2603.07915v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.07915v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07915v1.html; sha256:756fa16a83b340be8688095669253f309ec25b617276b8417ad5b109e89b728d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.6 Generalization Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07915v1 HTML — §4.6 Generalization Evaluation [facet=evaluation]; https://arxiv.org/html/2603.07915v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07915v1.html; sha256:756fa16a83b340be8688095669253f309ec25b617276b8417ad5b109e89b728d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。目标明确且一步可完成时直接执行仍更稳健。

<!-- claim:SF-2026-ARXIV-2603-07915:start -->**Claim Boundary**：只支持 arXiv:2603.07915v1 §3 Method 的机制与 §4.6 Generalization Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07915:end -->
<!-- review:SF-2026-ARXIV-2603-07915:end -->
### SageSched: Efficient LLM Scheduling Confronting Demand Uncertainty and Hybridity

<!-- review:SF-2026-ARXIV-2603-07917:start -->
**问题**：`SageSched: Efficient LLM Scheduling Confronting Demand Uncertainty and Hybridity` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `4.3.2 Superiority of our Cost Modeling Method` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.07917v1 HTML — §4.3.2 Superiority of our Cost Modeling Method [facet=method]; https://arxiv.org/html/2603.07917v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07917v1.html; sha256:4cdc67f8eea82fa2b1b541b36bceb1431b34d1f3e843cc88d46bab5dec91681f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.4 Overhead and Sensitivity Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07917v1 HTML — §4.4 Overhead and Sensitivity Analysis [facet=evaluation]; https://arxiv.org/html/2603.07917v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07917v1.html; sha256:4cdc67f8eea82fa2b1b541b36bceb1431b34d1f3e843cc88d46bab5dec91681f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `2.2 Limitations of Existing LLM Schedulers`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-07917:start -->**Claim Boundary**：只支持 arXiv:2603.07917v1 §4.3.2 Superiority of our Cost Modeling Method 的机制与 §4.4 Overhead and Sensitivity Analysis 的公开 workload；§2.2 Limitations of Existing LLM Schedulers 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07917:end -->
<!-- review:SF-2026-ARXIV-2603-07917:end -->
### Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning

<!-- review:SF-2026-ARXIV-2603-07972:start -->
**问题**：`Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning` 检查的是 `AGENT-MULTI-AGENT` 中 任务并行、能力异质和跨信任域协作迫使系统显式管理委托与共享状态。 是否会改变现有设计边界。

**旧路径为何合理**：单 agent 持有完整上下文和控制流，规模小时最容易归因。

**约束变化与机制**：exact-v1 的 `3 Methodology` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MULTI-AGENT` 负责 agent identity、委托边、消息状态、协作协议与冲突处理；定位证据为 `arXiv:2603.07972v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.07972v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07972v1.html; sha256:6044fd36fc2c4b63946eaa962d9203957ea319782880d9dbeb2ccb07dedf92f6`。

**Evaluation contract 与未证明部分**：公开验证定位在 `C.2 Experimental Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.07972v1 HTML — §C.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.07972v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.07972v1.html; sha256:6044fd36fc2c4b63946eaa962d9203957ea319782880d9dbeb2ccb07dedf92f6`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5 Conclusion`。任务短且角色不需要隔离时，单 agent 仍有更低协调成本。

<!-- claim:SF-2026-ARXIV-2603-07972:start -->**Claim Boundary**：只支持 arXiv:2603.07972v1 §3 Methodology 的机制与 §C.2 Experimental Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-07972:end -->
<!-- review:SF-2026-ARXIV-2603-07972:end -->
### EAGLE-Pangu: Accelerator-Safe Tree Speculative Decoding on Ascend NPUs

<!-- review:SF-2026-ARXIV-2603-08088:start -->
**问题**：树式 speculative decoding 在专用加速器上若沿用 GPU 动态控制流，会因 shape、内存与回滚语义不匹配失去收益。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：EAGLE-Pangu 将候选树展平为加速器可执行的静态批结构，并把验证、接受和 KV 提交边界重新组织为硬件安全路径。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；exact-v1 §3.1–§3.3 定义 branchable KV、tree flattening/mask/position 与 fused teacher，§4.5 仅是 timing methodology。

**Evaluation contract 与未证明部分**：§4.5 定义 timing contract，§5.1–§5.2 的 Ascend NPU 实验支持该实现下的接受/延迟收益；结论不等于所有 target/draft 或其他加速器都具备相同瓶颈。

**Trade-off / failure / coexistence**：静态化减少运行时分支，却可能增加无效候选计算并限制树形自适应；低接受率时普通 decode 仍更稳健。

<!-- claim:SF-2026-ARXIV-2603-08088:start -->**Claim Boundary**：只支持 arXiv:2603.08088v1 §3.1–§3.3 的机制与 §4.5、§5.1–§5.2 的 timing/实验合同；Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08088:end -->
<!-- review:SF-2026-ARXIV-2603-08088:end -->
### SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving

<!-- review:SF-2026-ARXIV-2603-08113:start -->
**问题**：`SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `3.1 Method Architecture` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.08113v1 HTML — §3.1 Method Architecture [facet=method]; https://arxiv.org/html/2603.08113v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08113v1.html; sha256:5ea7dccba7a8d724011d2eb18c5d491b2dbabaa889e30a60456cd8fff8e3d4b3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08113v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08113v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08113v1.html; sha256:5ea7dccba7a8d724011d2eb18c5d491b2dbabaa889e30a60456cd8fff8e3d4b3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Fundamental Limitation of Token-Level Routing Under Local Information`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-08113:start -->**Claim Boundary**：只支持 arXiv:2603.08113v1 §3.1 Method Architecture 的机制与 §4.2 Main Results 的公开 workload；§Fundamental Limitation of Token-Level Routing Under Local Information 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08113:end -->
<!-- review:SF-2026-ARXIV-2603-08113:end -->
### SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action

<!-- review:SF-2026-ARXIV-2603-08124:start -->
**问题**：`SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `3 Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.08124v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.08124v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08124v1.html; sha256:3df00ccd1225bf338f0d3460c46c974c27bd4dd8fe4f04975b131e3ff6c645c4`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Historical prototype settings (not used in main results).`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08124v1 HTML — §Historical prototype settings (not used in main results). [facet=evaluation]; https://arxiv.org/html/2603.08124v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08124v1.html; sha256:3df00ccd1225bf338f0d3460c46c974c27bd4dd8fe4f04975b131e3ff6c645c4`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Limitations & Ethics`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-08124:start -->**Claim Boundary**：只支持 arXiv:2603.08124v1 §3 Method 的机制与 §Historical prototype settings (not used in main results). 的公开 workload；§6 Limitations & Ethics 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08124:end -->
<!-- review:SF-2026-ARXIV-2603-08124:end -->
### Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet

<!-- review:SF-2026-ARXIV-2603-08163:start -->
**问题**：`Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet` 检查的是 `TRAIN-DISTRIBUTED-TRAINING` 中 参数、optimizer state 和通信规模越过单设备边界。 是否会改变现有设计边界。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：exact-v1 的 `2.1 SparseLoCo` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.08163v1 HTML — §2.1 SparseLoCo [facet=method]; https://arxiv.org/html/2603.08163v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08163v1.html; sha256:5cdb0a0c235eb4caa40a3e0a24a4b786854a181b585434928db62f79d7f75ea5`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Pre-Training Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08163v1 HTML — §4.2 Main Pre-Training Results [facet=evaluation]; https://arxiv.org/html/2603.08163v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08163v1.html; sha256:5cdb0a0c235eb4caa40a3e0a24a4b786854a181b585434928db62f79d7f75ea5`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。模型可装入单机且通信占比高时简单并行仍更优。

<!-- claim:SF-2026-ARXIV-2603-08163:start -->**Claim Boundary**：只支持 arXiv:2603.08163v1 §2.1 SparseLoCo 的机制与 §4.2 Main Pre-Training Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08163:end -->
<!-- review:SF-2026-ARXIV-2603-08163:end -->
### SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration

<!-- review:SF-2026-ARXIV-2603-08221:start -->
**问题**：`SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `IV-A Architecture Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.08221v1 HTML — §IV-A Architecture Overview [facet=method]; https://arxiv.org/html/2603.08221v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08221v1.html; sha256:de025298e41a00f7a3934b5cfa73b511ee2b74255a06db6a18b13d275f3d2ddc`。

**Evaluation contract 与未证明部分**：公开验证定位在 `VII Experimental Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08221v1 HTML — §VII Experimental Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08221v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08221v1.html; sha256:de025298e41a00f7a3934b5cfa73b511ee2b74255a06db6a18b13d275f3d2ddc`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VIII-B Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-08221:start -->**Claim Boundary**：只支持 arXiv:2603.08221v1 §IV-A Architecture Overview 的机制与 §VII Experimental Evaluation 的公开 workload；§VIII-B Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08221:end -->
<!-- review:SF-2026-ARXIV-2603-08221:end -->
### SlowBA: An efficiency backdoor attack towards VLM-based GUI agents

<!-- review:SF-2026-ARXIV-2603-08316:start -->
**问题**：`SlowBA: An efficiency backdoor attack towards VLM-based GUI agents` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `4.2 Method Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.08316v1 HTML — §4.2 Method Overview [facet=method]; https://arxiv.org/html/2603.08316v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08316v1.html; sha256:07b5c5e87e64d80e42010ca75b1b40f3c2eb0cabca270c01fb07fade927a3b1a`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08316v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08316v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08316v1.html; sha256:07b5c5e87e64d80e42010ca75b1b40f3c2eb0cabca270c01fb07fade927a3b1a`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5.3 Ablation Study`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-08316:start -->**Claim Boundary**：只支持 arXiv:2603.08316v1 §4.2 Method Overview 的机制与 §5.2 Main Results 的公开 workload；§5.3 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08316:end -->
<!-- review:SF-2026-ARXIV-2603-08316:end -->
### $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation

<!-- review:SF-2026-ARXIV-2603-08361:start -->
**问题**：`$Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `IV 𝚫\DeltaVLA` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.08361v1 HTML — §IV 𝚫\DeltaVLA [facet=method]; https://arxiv.org/html/2603.08361v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08361v1.html; sha256:e70572e92dcad3b22c8868b8ed16e248ac9e83ccb451077907643cb26d7b79c8`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V-C Ablation Studies`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08361v1 HTML — §V-C Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.08361v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08361v1.html; sha256:e70572e92dcad3b22c8868b8ed16e248ac9e83ccb451077907643cb26d7b79c8`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VI Conclusion`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-08361:start -->**Claim Boundary**：只支持 arXiv:2603.08361v1 §IV 𝚫\DeltaVLA 的机制与 §V-C Ablation Studies 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08361:end -->
<!-- review:SF-2026-ARXIV-2603-08361:end -->
### One Model Is Enough: Native Retrieval Embeddings from LLM Agent Hidden States

<!-- review:SF-2026-ARXIV-2603-08429:start -->
**问题**：`One Model Is Enough: Native Retrieval Embeddings from LLM Agent Hidden States` 检查的是 `AGENT-RAG` 中 知识时效、私有数据和可引用证据要求在生成前建立可追踪的检索路径。 是否会改变现有设计边界。

**旧路径为何合理**：把训练权重或完整上下文视为唯一知识来源，链路短且状态少。

**约束变化与机制**：exact-v1 的 `3.3 Projection Head Architecture` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-RAG` 负责 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；定位证据为 `arXiv:2603.08429v1 HTML — §3.3 Projection Head Architecture [facet=method]; https://arxiv.org/html/2603.08429v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08429v1.html; sha256:03542ce6050aecdfdef82d6d59daea1fe7c099748228ebfe33f7b37650c57a04`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.1 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08429v1 HTML — §5.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08429v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08429v1.html; sha256:03542ce6050aecdfdef82d6d59daea1fe7c099748228ebfe33f7b37650c57a04`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。知识稳定且已被模型可靠覆盖时，直接生成仍具有更低延迟。

<!-- claim:SF-2026-ARXIV-2603-08429:start -->**Claim Boundary**：只支持 arXiv:2603.08429v1 §3.3 Projection Head Architecture 的机制与 §5.1 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08429:end -->
<!-- review:SF-2026-ARXIV-2603-08429:end -->
### AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models

<!-- review:SF-2026-ARXIV-2603-08519:start -->
**问题**：`AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `III-A Model Architecture` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.08519v1 HTML — §III-A Model Architecture [facet=method]; https://arxiv.org/html/2603.08519v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08519v1.html; sha256:04ceb53c35fa56a73fa80aa88f00babcf602f70873f27644006c58a9fcff2fc1`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV-B Results Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08519v1 HTML — §IV-B Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.08519v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08519v1.html; sha256:04ceb53c35fa56a73fa80aa88f00babcf602f70873f27644006c58a9fcff2fc1`。

**Trade-off / failure / coexistence**：限制与反证定位在 `VI CONCLUSION`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-08519:start -->**Claim Boundary**：只支持 arXiv:2603.08519v1 §III-A Model Architecture 的机制与 §IV-B Results Analysis 的公开 workload；§VI CONCLUSION 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08519:end -->
<!-- review:SF-2026-ARXIV-2603-08519:end -->
### Interactive World Simulator for Robot Policy Training and Evaluation

<!-- review:SF-2026-ARXIV-2603-08546:start -->
**问题**：robot policy 训练需要可控环境 transition，而静态数据无法生成 action-conditioned counterfactual。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：交互式 world simulator 维护可更新环境状态，让 policy action 驱动下一 observation，并将 rollout 作为训练/评测输入。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.08546v1 HTML — §III Method [facet=method]; https://arxiv.org/html/2603.08546v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08546v1.html; sha256:8f7c6f8e7792ef68413fcfdd67605d55cb85c1cc267da2058e42e503cb588ed8`。

**Evaluation contract 与未证明部分**：作者只证明其 simulator 与机器人任务中的可交互性/预测质量；不证明 sim-to-real gap 已关闭。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08546v1 HTML — §II-C Imitation Policy Evaluation [facet=evaluation]; https://arxiv.org/html/2603.08546v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08546v1.html; sha256:8f7c6f8e7792ef68413fcfdd67605d55cb85c1cc267da2058e42e503cb588ed8`。

**Trade-off / failure / coexistence**：可控 rollout 扩大数据但会传播模型偏差；真实环境可用且风险低时直接采集仍更可信。

<!-- claim:SF-2026-ARXIV-2603-08546:start -->**Claim Boundary**：只支持 arXiv:2603.08546v1 §III Method 的机制与 §II-C Imitation Policy Evaluation 的公开 workload；§V Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08546:end -->
<!-- review:SF-2026-ARXIV-2603-08546:end -->
### PostTrainBench: Can LLM Agents Automate LLM Post-Training?

<!-- review:SF-2026-ARXIV-2603-08640:start -->
**问题**：`PostTrainBench: Can LLM Agents Automate LLM Post-Training?` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `5.2 Post-Training Method Selection` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.08640v1 HTML — §5.2 Post-Training Method Selection [facet=method]; https://arxiv.org/html/2603.08640v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08640v1.html; sha256:373c8c9339989e0c40da25ef338f26fdbcb3185ddf18a541c72399b228955090`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.1 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.08640v1 HTML — §3.1 Main Results [facet=evaluation]; https://arxiv.org/html/2603.08640v1; papers/2026/03/_sources/daily-20260310/exact-v1-bodies/2603.08640v1.html; sha256:373c8c9339989e0c40da25ef338f26fdbcb3185ddf18a541c72399b228955090`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Discussion`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-08640:start -->**Claim Boundary**：只支持 arXiv:2603.08640v1 §5.2 Post-Training Method Selection 的机制与 §3.1 Main Results 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-08640:end -->
<!-- review:SF-2026-ARXIV-2603-08640:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-07685 | score_7_9;potential_books_delta | selected | DA-20260310-16 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260310-16 |
| SF-2026-ARXIV-2603-08088 | score_7_9;potential_books_delta | selected | DA-20260310-23 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260310-23 |

<!-- analysis:DA-20260310-16:start -->
### Scalable Training of Mixture-of-Experts Models with Megatron Core

MoE 训练不能只在 dense 并行方案上附加 all-to-all：expert capacity、token dispatch 和并行维度会共同改变通信临界路径。 旧路径在其原约束下仍合理：单机或纯数据并行状态最少、同步语义清晰。 本 family 的设计变化是：该工作在 Megatron Core 中把 expert parallel、tensor/data/pipeline parallel 及 dispatcher 实现组合为统一训练配置，并显式管理 token permutation 与负载均衡。 其公开验证边界为：结果证明公开模型和集群配置中的扩展行为；没有披露或未覆盖的网络、失败恢复与极端路由倾斜仍需独立验证。 新增代价与回退条件为：多维并行提高大规模吞吐，但配置空间、collective 干扰和 straggler 风险同步上升；规模较小时 dense 或较少并行维度更易稳定。
<!-- analysis:DA-20260310-16:end -->
<!-- analysis:DA-20260310-23:start -->
### EAGLE-Pangu: Accelerator-Safe Tree Speculative Decoding on Ascend NPUs

树式 speculative decoding 在专用加速器上若沿用 GPU 动态控制流，会因 shape、内存与回滚语义不匹配失去收益。 旧路径在其原约束下仍合理：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。 本 family 的设计变化是：EAGLE-Pangu 将候选树展平为加速器可执行的静态批结构，并把验证、接受和 KV 提交边界重新组织为硬件安全路径。 其公开验证边界为：Ascend NPU 上的作者实验支持该实现下的接受/延迟收益；结论不等于所有 target/draft 或其他加速器都具备相同瓶颈。 新增代价与回退条件为：静态化减少运行时分支，却可能增加无效候选计算并限制树形自适应；低接受率时普通 decode 仍更稳健。
<!-- analysis:DA-20260310-23:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-06588 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#小结 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06588 | delta:SF-2026-ARXIV-2603-06588 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06588 |
| SF-2026-ARXIV-2603-06604 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#http-成功只是质量判断的第一道门 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06604 | delta:SF-2026-ARXIV-2603-06604 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06604 |
| SF-2026-ARXIV-2603-06626 | MODEL-MOE | books/part-02-model/21-moe.md#先改变通信坐标，再扩大稀疏容量 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06626 | delta:SF-2026-ARXIV-2603-06626 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06626 |
| SF-2026-ARXIV-2603-06728 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06728 | delta:SF-2026-ARXIV-2603-06728 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06728 |
| SF-2026-ARXIV-2603-06798 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#federated-tensor-type-定义一轮协议能表达什么 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06798 | delta:SF-2026-ARXIV-2603-06798 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06798 |
| SF-2026-ARXIV-2603-06847 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#skill-必须在真实-control-path-中评估 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06847 | delta:SF-2026-ARXIV-2603-06847 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06847 |
| SF-2026-ARXIV-2603-07006 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#owner-oriented-collective：通信算法也可以随参数所有权重写 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07006 | delta:SF-2026-ARXIV-2603-07006 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07006 |
| SF-2026-ARXIV-2603-07373 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07373 | delta:SF-2026-ARXIV-2603-07373 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07373 |
| SF-2026-ARXIV-2603-07416 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#从-token-draft-到-read-only-tool-speculation (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07416 | delta:SF-2026-ARXIV-2603-07416 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07416 |
| SF-2026-ARXIV-2603-07427 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07427 | delta:SF-2026-ARXIV-2603-07427 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07427 |
| SF-2026-ARXIV-2603-07433 | TRAIN-DATA | books/part-04-training-system/27-data.md#静态-mixture-到版本化-data-control-plane (section Ch-owner) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent); books/part-04-training-system/28-pretraining.md#第28章-pretraining (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07433 | delta:SF-2026-ARXIV-2603-07433 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07433 |
| SF-2026-ARXIV-2603-07466 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07466 | delta:SF-2026-ARXIV-2603-07466 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07466 |
| SF-2026-ARXIV-2603-07557 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07557 | delta:SF-2026-ARXIV-2603-07557 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07557 |
| SF-2026-ARXIV-2603-07607 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07607 | delta:SF-2026-ARXIV-2603-07607 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07607 |
| SF-2026-ARXIV-2603-07670 | AGENT-MEMORY | books/part-07-agent/77-memory.md#从-outcome-reward-到-content-level-credit：归因只能约束写入，不能成为真值 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07670 | delta:SF-2026-ARXIV-2603-07670 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07670 |
| SF-2026-ARXIV-2603-07685 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07685 | delta:SF-2026-ARXIV-2603-07685 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-07685 |
| SF-2026-ARXIV-2603-07770 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07770 | delta:SF-2026-ARXIV-2603-07770 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07770 |
| SF-2026-ARXIV-2603-07777 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#measurement-也是-reward-interface-的一部分 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07777 | delta:SF-2026-ARXIV-2603-07777 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07777 |
| SF-2026-ARXIV-2603-07799 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#在谈-state-之前，先声明预测-channel (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07799 | delta:SF-2026-ARXIV-2603-07799 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07799 |
| SF-2026-ARXIV-2603-07915 | AGENT-PLANNING | books/part-07-agent/79-planning.md#search-based-planning-的边界 (section Ch-owner) | books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent); books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07915 | delta:SF-2026-ARXIV-2603-07915 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07915 |
| SF-2026-ARXIV-2603-07917 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07917 | delta:SF-2026-ARXIV-2603-07917 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07917 |
| SF-2026-ARXIV-2603-07972 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/81-workflow.md#第81章-workflow (section Ch-adjacent); books/part-07-agent/83-mcp.md#第83章-mcp (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-07972 | delta:SF-2026-ARXIV-2603-07972 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-07972 |
| SF-2026-ARXIV-2603-08088 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08088 | delta:SF-2026-ARXIV-2603-08088 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-08088 |
| SF-2026-ARXIV-2603-08113 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#从语言推理到-one-step-meta-action (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08113 | delta:SF-2026-ARXIV-2603-08113 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08113 |
| SF-2026-ARXIV-2603-08124 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08124 | delta:SF-2026-ARXIV-2603-08124 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08124 |
| SF-2026-ARXIV-2603-08163 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#矩阵耦合-optimizer-必须把更新本身变成-distributed-operation (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08163 | delta:SF-2026-ARXIV-2603-08163 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08163 |
| SF-2026-ARXIV-2603-08221 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#hidden-state-release-不天然位于-privacy-与-utility-的中间地带 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08221 | delta:SF-2026-ARXIV-2603-08221 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08221 |
| SF-2026-ARXIV-2603-08316 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08316 | delta:SF-2026-ARXIV-2603-08316 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08316 |
| SF-2026-ARXIV-2603-08361 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08361 | delta:SF-2026-ARXIV-2603-08361 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08361 |
| SF-2026-ARXIV-2603-08429 | AGENT-RAG | books/part-07-agent/76-rag.md#retrieval-的基本度量 (section Ch-owner) | books/part-07-agent/75-context.md#第75章-context (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08429 | delta:SF-2026-ARXIV-2603-08429 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08429 |
| SF-2026-ARXIV-2603-08519 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08519 | delta:SF-2026-ARXIV-2603-08519 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08519 |
| SF-2026-ARXIV-2603-08546 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#在谈-state-之前，先声明预测-channel (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08546 | delta:SF-2026-ARXIV-2603-08546 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08546 |
| SF-2026-ARXIV-2603-08640 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-08640 | delta:SF-2026-ARXIV-2603-08640 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-08640 |

<!-- books-review:SF-2026-ARXIV-2603-06588:start -->
### vLLM Hook v0: A Plug-in for Programming Model Internals on vLLM — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06588:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：下一章转向 vLLM，观察另一个历史起点：如果首先把 KV allocation 与 scheduler 视为核心，完整 Serving engine 会怎样组织。<!-- existing:SF-2026-ARXIV-2603-06588:end -->

<!-- delta:SF-2026-ARXIV-2603-06588:start -->新证据差异：vLLM Hook 以配置声明捕获点，并区分只读 probe 与主动修改，使内部状态干预成为显式扩展接口。<!-- delta:SF-2026-ARXIV-2603-06588:end -->

边界：只支持 arXiv:2603.06588v1 §2 Core Functions of vLLM Hook 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06588:end -->
<!-- books-review:SF-2026-ARXIV-2603-06604:start -->
### Know When You're Wrong: Aligning Confidence with Correctness for LLM Error Detection — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06604:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。<!-- existing:SF-2026-ARXIV-2603-06604:end -->

<!-- delta:SF-2026-ARXIV-2603-06604:start -->新证据差异：该工作把 confidence-correctness alignment 作为单独训练/校准目标，并比较 error detection 而非只看 accuracy。<!-- delta:SF-2026-ARXIV-2603-06604:end -->

边界：只支持 arXiv:2603.06604v1 §3 Know When You’re Wrong 的机制与 §3.3 Confidence Evaluation 的公开 workload；§6 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06604:end -->
<!-- books-review:SF-2026-ARXIV-2603-06626:start -->
### Grouter: Decoupling Routing from Representation for Accelerated MoE Training — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06626:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：标准 MoE 在 `d_model` 维 token state 上 routing、dispatch 和 expert compute。增加 experts 可以扩大总容量，但每个 assignment 搬运的 payload 仍与 hidden width 绑定；当 All-to-All bytes 或低延迟下的 expert weight load 成为瓶颈时，仅继续增加 experts/top-k 会放大系统压力。<!-- existing:SF-2026-ARXIV-2603-06626:end -->

<!-- delta:SF-2026-ARXIV-2603-06626:start -->新证据差异：exact-v1 的 `3 Method` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06626:end -->

边界：只支持 arXiv:2603.06626v1 §3 Method 的机制与 §Appendix I Downstream Experiments 的公开 workload；§4.3 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06626:end -->
<!-- books-review:SF-2026-ARXIV-2603-06728:start -->
### Orion: Characterizing and Programming Apple's Neural Engine for LLM Training and Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06728:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-06728:end -->

<!-- delta:SF-2026-ARXIV-2603-06728:start -->新证据差异：Orion 逆向刻画指令、memory 与执行限制，并把可运行算子映射到训练/推理 execution plan。<!-- delta:SF-2026-ARXIV-2603-06728:end -->

边界：只支持 arXiv:2603.06728v1 §4 System Design 的机制与 §8 Evaluation 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06728:end -->
<!-- books-review:SF-2026-ARXIV-2603-06798:start -->
### NEST: Network- and Memory-Aware Device Placement For Distributed Deep Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06798:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：普通 distributed tensor type 描述 device shard；federated computation 还必须区分 client-record axis 与 fixed-dimensional shared state。一轮协议可被约束为 `encode → merge → decode`：客户端只导出编码状态，merge owner 只组合声明的 shared state，decoder 再生成本地结果。类型系统拥有可表达通信边界，transport 不能用任意 payload 绕过它。<!-- existing:SF-2026-ARXIV-2603-06798:end -->

<!-- delta:SF-2026-ARXIV-2603-06798:start -->新证据差异：NEST 联合建模 device memory、通信拓扑和 operator dependency，搜索满足容量约束的 placement。<!-- delta:SF-2026-ARXIV-2603-06798:end -->

边界：只支持 arXiv:2603.06798v1 §5.1 Methodology and Setup 的机制与 §A.6 Evaluation and expected results 的公开 workload；§7 Limitation and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06798:end -->
<!-- books-review:SF-2026-ARXIV-2603-06847:start -->
### Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06847:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：Refinement 只能重组已有 evidence，不能从缺失知识中创造可靠 procedure；失败还可能低于 no-Skill baseline。 Agentic Skills in the Wild 的作者结果支持这一分层，不支持固定模型排名或特定 registry size 的通用结论。<!-- existing:SF-2026-ARXIV-2603-06847:end -->

<!-- delta:SF-2026-ARXIV-2603-06847:start -->新证据差异：该 taxonomy 用真实 failure report 区分类型、症状和根因，为 fault injection 与 evidence schema 提供分母。<!-- delta:SF-2026-ARXIV-2603-06847:end -->

边界：只支持 arXiv:2603.06847v1 §2. Methodology 的机制与 §3.3.1. Quantitative Validation Results 的公开 workload；§7. Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-06847:end -->
<!-- books-review:SF-2026-ARXIV-2603-07006:start -->
### Mozart: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07006:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：标准 reduce-scatter/all-gather 先保持规则分片和 collective 对称性，最利于通用实现与故障推理。超大 MoE 或 不规则参数布局下，若 optimizer state 已有明确 owner，仍按逻辑 tensor 均匀切分可能产生多余中转和拓扑错配。 一个实验性分支让 owner 直接定义 reduction destination，并由 runtime 根据 shard、node 与 link hierarchy 生成 通信计划：<!-- existing:SF-2026-ARXIV-2603-07006:end -->

<!-- delta:SF-2026-ARXIV-2603-07006:start -->新证据差异：exact-v1 的 `𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07006:end -->

边界：只支持 arXiv:2603.07006v1 §𝙼𝚘𝚣𝚊𝚛𝚝\mathtt{Mozart}: Modularized and Efficient MoE Training on 3.5D Wafer-Scale Chiplet Architectures 的机制与 §Appendix B More Experimental Results 的公开 workload；§6 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07006:end -->
<!-- books-review:SF-2026-ARXIV-2603-07373:start -->
### Scheduling Parallel Optical Circuit Switches for AI Training — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07373:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：本章只建立总决策框架。第 37～39 章分别展开 Tensor Parallel、Pipeline Parallel 和 ZeRO；第 40～41 章再讨论 Megatron 与 DeepSpeed 如何组合这些机制。<!-- existing:SF-2026-ARXIV-2603-07373:end -->

<!-- delta:SF-2026-ARXIV-2603-07373:start -->新证据差异：exact-v1 的 `III-A Overview` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07373:end -->

边界：只支持 arXiv:2603.07373v1 §III-A Overview 的机制与 §V-C Benchmark Workload 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07373:end -->
<!-- books-review:SF-2026-ARXIV-2603-07416:start -->
### DualSpec: Accelerating Deep Research Agents via Dual-Process Action Speculation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07416:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：Token-level speculative decoding 只提前产生候选 token，外部工具仍在完整 action 生成后启动。对长 reasoning 与慢 read tool 的 Agent turn，可以增加一层 action speculation：main stream 产生首 token 后复用同一 prefix KV fork 当前模型，以 forced tool-call prefix 探测下一 action；只有 probe confidence 达到门限才并发执行被 manifest 标为 read-only 的工具。Main stream 完成后，最终 tool name 与 canonical arguments 完全匹配， precomputed observation 才能进入会话；不匹配则丢弃结果并走 serial fallback。被拒 probe 的已验证 token prefix 可以继续作为普通 speculative draft，但仍由 target verification 决定提交。<!-- existing:SF-2026-ARXIV-2603-07416:end -->

<!-- delta:SF-2026-ARXIV-2603-07416:start -->新证据差异：exact-v1 的 `6.3.1 speculation methods` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07416:end -->

边界：只支持 arXiv:2603.07416v1 §6.3.1 speculation methods 的机制与 §6.2 Main Results 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07416:end -->
<!-- books-review:SF-2026-ARXIV-2603-07427:start -->
### AutoControl Arena: Synthesizing Executable Test Environments for Frontier AI Risk Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07427:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-07427:end -->

<!-- delta:SF-2026-ARXIV-2603-07427:start -->新证据差异：exact-v1 的 `3.2 Architect Agent: Scenario Design` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07427:end -->

边界：只支持 arXiv:2603.07427v1 §3.2 Architect Agent: Scenario Design 的机制与 §2.2 Simulation Paradigms for Agent Safety Evaluation 的公开 workload；§A.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07427:end -->
<!-- books-review:SF-2026-ARXIV-2603-07433:start -->
### Data Agent: Learning to Select Data via End-to-End Dynamic Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07433:start -->已读 owner `books/part-04-training-system/27-data.md` 与相邻章节。现有命题：这里 data operator 只提出训练分布，training controller 拥有 active set、采样权重、cache 与更新时机， Evaluation 仍决定变化是否可接受。动态策略能把不同阶段的 data need 写进控制面，却新增 feedback delay、 validation leakage、oscillation、distributed-state access 和恢复问题。来自 Web Agent 的 trajectory 还必须保存 teacher 与 student 的 observation modality、action abstraction、browser/environment revision、verifier 和 side-effect policy；否则 privileged structural teacher 编译出的 screenshot-only 行为会失去关键 lineage。<!-- existing:SF-2026-ARXIV-2603-07433:end -->

<!-- delta:SF-2026-ARXIV-2603-07433:start -->新证据差异：exact-v1 的 `3 The Proposed Method` 把论文方案定位到 样本 identity、选择策略、版本、provenance 与训练消费顺序；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07433:end -->

边界：只支持 arXiv:2603.07433v1 §3 The Proposed Method 的机制与 §4.7 Ablation Study 的公开 workload；§4.7 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07433:end -->
<!-- books-review:SF-2026-ARXIV-2603-07466:start -->
### Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07466:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-07466:end -->

<!-- delta:SF-2026-ARXIV-2603-07466:start -->新证据差异：exact-v1 的 `4 Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07466:end -->

边界：只支持 arXiv:2603.07466v1 §4 Overview 的机制与 §6.2 System Overhead Analysis 的公开 workload；§8.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07466:end -->
<!-- books-review:SF-2026-ARXIV-2603-07557:start -->
### AgentRaft: Automated Detection of Data Over-Exposure in LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07557:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-07557:end -->

<!-- delta:SF-2026-ARXIV-2603-07557:start -->新证据差异：exact-v1 的 `2.1. LLM Agent Architecture` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07557:end -->

边界：只支持 arXiv:2603.07557v1 §2.1. LLM Agent Architecture 的机制与 §5.1. Evaluation Setup 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07557:end -->
<!-- books-review:SF-2026-ARXIV-2603-07607:start -->
### MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07607:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-07607:end -->

<!-- delta:SF-2026-ARXIV-2603-07607:start -->新证据差异：exact-v1 的 `3.4 Prototype Implementation` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07607:end -->

边界：只支持 arXiv:2603.07607v1 §3.4 Prototype Implementation 的机制与 §4.1.2 Evaluation Scenarios and Workload Profiles: 的公开 workload；§5 Discussion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07607:end -->
<!-- books-review:SF-2026-ARXIV-2603-07670:start -->
### Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07670:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：归因分数仍不是 causal ground truth。相关 token 会互相替代或共同起效，masking 会改变输入分布，judge 与 answer model 也共同决定 credit；反复 counterfactual scoring 还增加训练成本。因此 learned memory write 不能因为 attribution 较高就获得事实权威。source episode、extractor/judge version、masking policy、local/global reward、poisoning test、selective deletion 与 held-out evaluation 都必须进入写入收据。heuristic admission 与 outcome-only reward 在稳定、低风险、成本敏感的场景仍是合理分支。<!-- existing:SF-2026-ARXIV-2603-07670:end -->

<!-- delta:SF-2026-ARXIV-2603-07670:start -->新证据差异：exact-v1 的 `7.6 Three architecture patterns` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07670:end -->

边界：只支持 arXiv:2603.07670v1 §7.6 Three architecture patterns 的机制与 §9.10 Standardized evaluation 的公开 workload；§10 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07670:end -->
<!-- books-review:SF-2026-ARXIV-2603-07685:start -->
### Scalable Training of Mixture-of-Experts Models with Megatron Core — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07685:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：本章只建立总决策框架。第 37～39 章分别展开 Tensor Parallel、Pipeline Parallel 和 ZeRO；第 40～41 章再讨论 Megatron 与 DeepSpeed 如何组合这些机制。<!-- existing:SF-2026-ARXIV-2603-07685:end -->

<!-- delta:SF-2026-ARXIV-2603-07685:start -->新证据差异：该工作在 Megatron Core 中把 expert parallel、tensor/data/pipeline parallel 及 dispatcher 实现组合为统一训练配置，并显式管理 token permutation 与负载均衡。<!-- delta:SF-2026-ARXIV-2603-07685:end -->

边界：§2.1 只建立 token dispatch；parallel folding 与多维并行组合由 arXiv:2603.07685v1 §3.3 支持，测量边界为 §8，§11 之外不外推。作者侧决定为 **Integrate**，已写回并等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-07685:end -->
<!-- books-review:SF-2026-ARXIV-2603-07770:start -->
### ArcLight: A Lightweight LLM Inference Architecture for Many-Core CPUs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07770:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-07770:end -->

<!-- delta:SF-2026-ARXIV-2603-07770:start -->新证据差异：exact-v1 的 `2 System Design` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07770:end -->

边界：只支持 arXiv:2603.07770v1 §2 System Design 的机制与 §4 Experiments 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07770:end -->
<!-- books-review:SF-2026-ARXIV-2603-07777:start -->
### Breaking Training Bottlenecks: Effective and Stable Reinforcement Learning for Coding Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07777:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条 路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体 数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是： **verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**<!-- existing:SF-2026-ARXIV-2603-07777:end -->

<!-- delta:SF-2026-ARXIV-2603-07777:start -->新证据差异：exact-v1 的 `5 Experimental Design` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07777:end -->

边界：只支持 arXiv:2603.07777v1 §5 Experimental Design 的机制与 §6 Results 的公开 workload；§8 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07777:end -->
<!-- books-review:SF-2026-ARXIV-2603-07799:start -->
### MWM: Mobile World Models for Action-Conditioned Consistent Prediction — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07799:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：现有证据给出了 environment、agent 与 joint channel 的形式化恒等式、support restriction 及有限 POMDP 示例；它澄清了 representation identity，却不是 learned world model 的开放世界经验性证明。工程上仍需用 action-conditioned outcome、counterfactual coverage 和 calibration 分别验证各 channel。<!-- existing:SF-2026-ARXIV-2603-07799:end -->

<!-- delta:SF-2026-ARXIV-2603-07799:start -->新证据差异：exact-v1 的 `III-A Overview` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07799:end -->

边界：只支持 arXiv:2603.07799v1 §III-A Overview 的机制与 §IV-B Main Results 的公开 workload；§V CONCLUSIONS 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07799:end -->
<!-- books-review:SF-2026-ARXIV-2603-07915:start -->
### Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07915:start -->已读 owner `books/part-07-agent/79-planning.md` 与相邻章节。现有命题：剩余预算不只是外层 hard cap，也可以成为 tree selection state。固定宽度或并行采样在分支便宜、critic 弱或 低 latency 依赖并行时仍合理；当不同路径共享前缀且 tool/output token 都昂贵时，planner 可以在每个 node 保存 累计 value、访问次数、父子关系和剩余资源，再根据资源收紧程度逐步从探索转向利用：<!-- existing:SF-2026-ARXIV-2603-07915:end -->

<!-- delta:SF-2026-ARXIV-2603-07915:start -->新证据差异：exact-v1 的 `3 Method` 把论文方案定位到 计划路由、证据需求与停止条件；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07915:end -->

边界：只支持 arXiv:2603.07915v1 §3 Method 的机制与 §4.6 Generalization Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07915:end -->
<!-- books-review:SF-2026-ARXIV-2603-07917:start -->
### SageSched: Efficient LLM Scheduling Confronting Demand Uncertainty and Hybridity — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07917:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-07917:end -->

<!-- delta:SF-2026-ARXIV-2603-07917:start -->新证据差异：exact-v1 的 `4.3.2 Superiority of our Cost Modeling Method` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07917:end -->

边界：只支持 arXiv:2603.07917v1 §4.3.2 Superiority of our Cost Modeling Method 的机制与 §4.4 Overhead and Sensitivity Analysis 的公开 workload；§2.2 Limitations of Existing LLM Schedulers 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07917:end -->
<!-- books-review:SF-2026-ARXIV-2603-07972:start -->
### Adaptive Collaboration with Humans: Metacognitive Policy Optimization for Multi-Agent LLMs with Continual Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-07972:start -->已读 owner `books/part-07-agent/82-multi-agent.md` 与相邻章节。现有命题：本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**<!-- existing:SF-2026-ARXIV-2603-07972:end -->

<!-- delta:SF-2026-ARXIV-2603-07972:start -->新证据差异：exact-v1 的 `3 Methodology` 把论文方案定位到 agent identity、委托边、消息状态、协作协议与冲突处理；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-07972:end -->

边界：只支持 arXiv:2603.07972v1 §3 Methodology 的机制与 §C.2 Experimental Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-07972:end -->
<!-- books-review:SF-2026-ARXIV-2603-08088:start -->
### EAGLE-Pangu: Accelerator-Safe Tree Speculative Decoding on Ascend NPUs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08088:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**<!-- existing:SF-2026-ARXIV-2603-08088:end -->

<!-- delta:SF-2026-ARXIV-2603-08088:start -->新证据差异：EAGLE-Pangu 将候选树展平为加速器可执行的静态批结构，并把验证、接受和 KV 提交边界重新组织为硬件安全路径。<!-- delta:SF-2026-ARXIV-2603-08088:end -->

边界：机制定位为 arXiv:2603.08088v1 §3.1–§3.3，timing/实验定位为 §4.5、§5.1–§5.2；Limitations 之外不外推。作者侧决定为 **Integrate**，已写回并等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-08088:end -->
<!-- books-review:SF-2026-ARXIV-2603-08113:start -->
### SAMoE-VLA: A Scene Adaptive Mixture-of-Experts Vision-Language-Action Model for Autonomous Driving — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08113:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：自然语言 reasoning 作为 driving action interface 可解释，但逐步生成会把标注、延迟和 grounding 放进控制关键路径。One-step meta-action 把高层语义压成有限 action schema，由低层 controller 解释坐标、速度和安全 envelope；policy 只拥有 meta-action proposal，确定性/实时控制器拥有物理 commit。<!-- existing:SF-2026-ARXIV-2603-08113:end -->

<!-- delta:SF-2026-ARXIV-2603-08113:start -->新证据差异：exact-v1 的 `3.1 Method Architecture` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08113:end -->

边界：只支持 arXiv:2603.08113v1 §3.1 Method Architecture 的机制与 §4.2 Main Results 的公开 workload；§Fundamental Limitation of Token-Level Routing Under Local Information 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08113:end -->
<!-- books-review:SF-2026-ARXIV-2603-08124:start -->
### SaiVLA-0: Cerebrum--Pons--Cerebellum Tripartite Architecture for Compute-Aware Vision-Language-Action — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08124:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-08124:end -->

<!-- delta:SF-2026-ARXIV-2603-08124:start -->新证据差异：exact-v1 的 `3 Method` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08124:end -->

边界：只支持 arXiv:2603.08124v1 §3 Method 的机制与 §Historical prototype settings (not used in main results). 的公开 workload；§6 Limitations & Ethics 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08124:end -->
<!-- books-review:SF-2026-ARXIV-2603-08163:start -->
### Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08163:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：以 element-wise optimizer state 做 ZeRO/FSDP 式分片，在更新可按参数局部计算时是合理的。矩阵级 Newton–Schulz optimizer update 却耦合整块矩阵，局部 post-processing 会让相同 checkpoint 在不同 layout 下产生不同语义。训练状态因此必须增加 matrix layout、collective algorithm、worker group 与 optimizer-step identity，把更新本身作为分布式矩阵操作并与 checkpoint 原子提交。论文在 embodied foundation model 与 LLM 训练中报告加速且性能接近 AdamW，但没有证明任意拓扑、矩阵形状或长程收敛与集中式实现等价。collective 中断、layout 漂移或数值分歧时应恢复最近一致 checkpoint，并退回已验证的 AdamW/旧 optimizer 路径；局部优化器与矩阵耦合优化器按更新结构共存。<!-- existing:SF-2026-ARXIV-2603-08163:end -->

<!-- delta:SF-2026-ARXIV-2603-08163:start -->新证据差异：exact-v1 的 `2.1 SparseLoCo` 把论文方案定位到 训练状态分片、collective、同步与故障恢复；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08163:end -->

边界：只支持 arXiv:2603.08163v1 §2.1 SparseLoCo 的机制与 §4.2 Main Pre-Training Results 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08163:end -->
<!-- books-review:SF-2026-ARXIV-2603-08221:start -->
### SplitAgent: A Privacy-Preserving Distributed Architecture for Enterprise-Cloud Agent Collaboration — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08221:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：把中间表示视为“比原始输入安全、比最终输出有用”的折中，在下游任务与攻击面固定时容易成立；只要 hidden state 仍保留任务信息，它也可能保留敏感属性。Release owner 必须先声明允许的下游能力、攻击者知识与撤销边界，再在 architecture co-design、受限查询接口或不发布之间选择，不能只提高噪声后宣称安全。<!-- existing:SF-2026-ARXIV-2603-08221:end -->

<!-- delta:SF-2026-ARXIV-2603-08221:start -->新证据差异：exact-v1 的 `IV-A Architecture Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08221:end -->

边界：只支持 arXiv:2603.08221v1 §IV-A Architecture Overview 的机制与 §VII Experimental Evaluation 的公开 workload；§VIII-B Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08221:end -->
<!-- books-review:SF-2026-ARXIV-2603-08316:start -->
### SlowBA: An efficiency backdoor attack towards VLM-based GUI agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08316:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-08316:end -->

<!-- delta:SF-2026-ARXIV-2603-08316:start -->新证据差异：exact-v1 的 `4.2 Method Overview` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08316:end -->

边界：只支持 arXiv:2603.08316v1 §4.2 Method Overview 的机制与 §5.2 Main Results 的公开 workload；§5.3 Ablation Study 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08316:end -->
<!-- books-review:SF-2026-ARXIV-2603-08361:start -->
### $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08361:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-08361:end -->

<!-- delta:SF-2026-ARXIV-2603-08361:start -->新证据差异：exact-v1 的 `IV 𝚫\DeltaVLA` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08361:end -->

边界：只支持 arXiv:2603.08361v1 §IV 𝚫\DeltaVLA 的机制与 §V-C Ablation Studies 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08361:end -->
<!-- books-review:SF-2026-ARXIV-2603-08429:start -->
### One Model Is Enough: Native Retrieval Embeddings from LLM Agent Hidden States — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08429:start -->已读 owner `books/part-07-agent/76-rag.md` 与相邻章节。现有命题：Retrieval metric 必须与 Agent 实际 query distribution 对齐。面向自然问题训练的 dense retriever，未必适合 deep-research Agent 生成的短 entity、keyword 或逐步 subquery；更强 encoder 在接口分布错位时也可能输给 lexical baseline。评估应联合版本化 query generator、corpus/index、retriever/reranker、packing policy 与 context use，并分开报告 source recall、duplicate evidence、search/tool cost 和 final outcome。<!-- existing:SF-2026-ARXIV-2603-08429:end -->

<!-- delta:SF-2026-ARXIV-2603-08429:start -->新证据差异：exact-v1 的 `3.3 Projection Head Architecture` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08429:end -->

边界：只支持 arXiv:2603.08429v1 §3.3 Projection Head Architecture 的机制与 §5.1 Main Results 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08429:end -->
<!-- books-review:SF-2026-ARXIV-2603-08519:start -->
### AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08519:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-08519:end -->

<!-- delta:SF-2026-ARXIV-2603-08519:start -->新证据差异：exact-v1 的 `III-A Model Architecture` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08519:end -->

边界：只支持 arXiv:2603.08519v1 §III-A Model Architecture 的机制与 §IV-B Results Analysis 的公开 workload；§VI CONCLUSION 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08519:end -->
<!-- books-review:SF-2026-ARXIV-2603-08546:start -->
### Interactive World Simulator for Robot Policy Training and Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08546:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：这不是缺陷，只是契约不同。固定 policy、有限 action menu 或只需回放已观测行为时，restricted predictor 更便宜也更容易校准；planning、off-policy evaluation 或安全 red-team 则需要扩大 action support，或在遇到 unsupported action 时拒绝推演并请求 simulator / real observation。Policy revision 还会改变 support，因此旧的 compact state 可能需要 invalidation、retraining 或重新验证，不能只把 policy version 换个标签继续使用。<!-- existing:SF-2026-ARXIV-2603-08546:end -->

<!-- delta:SF-2026-ARXIV-2603-08546:start -->新证据差异：交互式 world simulator 维护可更新环境状态，让 policy action 驱动下一 observation，并将 rollout 作为训练/评测输入。<!-- delta:SF-2026-ARXIV-2603-08546:end -->

边界：只支持 arXiv:2603.08546v1 §III Method 的机制与 §II-C Imitation Policy Evaluation 的公开 workload；§V Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08546:end -->
<!-- books-review:SF-2026-ARXIV-2603-08640:start -->
### PostTrainBench: Can LLM Agents Automate LLM Post-Training? — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-08640:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-08640:end -->

<!-- delta:SF-2026-ARXIV-2603-08640:start -->新证据差异：exact-v1 的 `5.2 Post-Training Method Selection` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-08640:end -->

边界：只支持 arXiv:2603.08640v1 §5.2 Post-Training Method Selection 的机制与 §3.1 Main Results 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-08640:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260310-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260310 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260310-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-06588; review:SF-2026-ARXIV-2603-06604; review:SF-2026-ARXIV-2603-06626; review:SF-2026-ARXIV-2603-06728; review:SF-2026-ARXIV-2603-06798; review:SF-2026-ARXIV-2603-06847; review:SF-2026-ARXIV-2603-07006; review:SF-2026-ARXIV-2603-07373; review:SF-2026-ARXIV-2603-07416; review:SF-2026-ARXIV-2603-07427; review:SF-2026-ARXIV-2603-07433; review:SF-2026-ARXIV-2603-07466; review:SF-2026-ARXIV-2603-07557; review:SF-2026-ARXIV-2603-07607; review:SF-2026-ARXIV-2603-07670; review:SF-2026-ARXIV-2603-07685; review:SF-2026-ARXIV-2603-07770; review:SF-2026-ARXIV-2603-07777; review:SF-2026-ARXIV-2603-07799; review:SF-2026-ARXIV-2603-07915; review:SF-2026-ARXIV-2603-07917; review:SF-2026-ARXIV-2603-07972; review:SF-2026-ARXIV-2603-08088; review:SF-2026-ARXIV-2603-08113; review:SF-2026-ARXIV-2603-08124; review:SF-2026-ARXIV-2603-08163; review:SF-2026-ARXIV-2603-08221; review:SF-2026-ARXIV-2603-08316; review:SF-2026-ARXIV-2603-08361; review:SF-2026-ARXIV-2603-08429; review:SF-2026-ARXIV-2603-08519; review:SF-2026-ARXIV-2603-08546; review:SF-2026-ARXIV-2603-08640 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260310-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260310-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260310/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 2 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 2 项 Books Integration：
- 更新并复核 `books/part-04-training-system/36-distributed-training.md`。
- 更新并复核 `books/part-05-inference-system/48-speculative-decoding.md`。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 未解决语义 finding=4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）；blocked / unverified / disputed 仍为 0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
