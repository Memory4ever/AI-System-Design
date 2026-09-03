# Daily Research — 2026-03-12

**Research Date:** 2026-03-12

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-11 09:00:00 ～ 2026-03-12 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

严格窗口 raw/registered/screened=551/551/551；denominator=33、pre-denominator closures=518。exact-v1 Review complete=33、blocked=0；Integrate 建议=3。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-12 |
| Window End | 2026-03-12 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260312-AUTHOR-33 |
| Denominator Frozen At | 2026-09-02T16:27:58.265174+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-11T09:00:00+08:00 | 2026-03-12T09:00:00+08:00 | 2026-09-02T16:27:58.265174+08:00 | official-schedule recovery receipt + 551/551 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 551 | SF-2026-ARXIV-2603-09983;SF-2026-ARXIV-2603-10030;SF-2026-ARXIV-2603-10031;SF-2026-ARXIV-2603-10032;SF-2026-ARXIV-2603-10044;SF-2026-ARXIV-2603-10057;SF-2026-ARXIV-2603-10060;SF-2026-ARXIV-2603-10062;SF-2026-ARXIV-2603-10085;SF-2026-ARXIV-2603-10087;SF-2026-ARXIV-2603-10088;SF-2026-ARXIV-2603-10143;SF-2026-ARXIV-2603-10163;SF-2026-ARXIV-2603-10165;SF-2026-ARXIV-2603-10291;SF-2026-ARXIV-2603-10335;SF-2026-ARXIV-2603-10342;SF-2026-ARXIV-2603-10353;SF-2026-ARXIV-2603-10379;SF-2026-ARXIV-2603-10422;SF-2026-ARXIV-2603-10444;SF-2026-ARXIV-2603-10469;SF-2026-ARXIV-2603-10494;SF-2026-ARXIV-2603-10521;SF-2026-ARXIV-2603-10577;SF-2026-ARXIV-2603-10600;SF-2026-ARXIV-2603-10712;SF-2026-ARXIV-2603-10726;SF-2026-ARXIV-2603-10742;SF-2026-ARXIV-2603-10749;SF-2026-ARXIV-2603-10765;SF-2026-ARXIV-2603-10779;SF-2026-ARXIV-2603-10899 | pages=100; prefixes=00..99; final_cursor=end; registered=551; screened=551; retained=33; closure=518 | 2026-03-12T01:00:00+00:00 | screening-ledger-final.json#sha256=a83fa2dd41a11ba6f1a139967246bdc0c346f49385ef9edf407ee516c2436ebd; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260312:start -->作者侧已逐项筛选全部 551 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260312:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-09983 | arXiv:2603.09983v1 | paper-v1:2603.09983 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-09983 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09983 | no |
| SF-2026-ARXIV-2603-10030 | arXiv:2603.10030v1 | paper-v1:2603.10030 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10030 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10030 | no |
| SF-2026-ARXIV-2603-10031 | arXiv:2603.10031v1 | paper-v1:2603.10031 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10031 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10031 | no |
| SF-2026-ARXIV-2603-10032 | arXiv:2603.10032v1 | paper-v1:2603.10032 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10032 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10032 | no |
| SF-2026-ARXIV-2603-10044 | arXiv:2603.10044v1 | paper-v1:2603.10044 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10044 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10044 | no |
| SF-2026-ARXIV-2603-10057 | arXiv:2603.10057v1 | paper-v1:2603.10057 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10057 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10057 | no |
| SF-2026-ARXIV-2603-10060 | arXiv:2603.10060v1 | paper-v1:2603.10060 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10060 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10060 | no |
| SF-2026-ARXIV-2603-10062 | arXiv:2603.10062v1 | paper-v1:2603.10062 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10062 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10062 | no |
| SF-2026-ARXIV-2603-10085 | arXiv:2603.10085v1 | paper-v1:2603.10085 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10085 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10085 | no |
| SF-2026-ARXIV-2603-10087 | arXiv:2603.10087v1 | paper-v1:2603.10087 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10087 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10087 | no |
| SF-2026-ARXIV-2603-10088 | arXiv:2603.10088v1 | paper-v1:2603.10088 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10088 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10088 | no |
| SF-2026-ARXIV-2603-10143 | arXiv:2603.10143v1 | paper-v1:2603.10143 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10143 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10143 | no |
| SF-2026-ARXIV-2603-10163 | arXiv:2603.10163v1 | paper-v1:2603.10163 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10163 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10163 | no |
| SF-2026-ARXIV-2603-10165 | arXiv:2603.10165v1 | paper-v1:2603.10165 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10165 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10165 | no |
| SF-2026-ARXIV-2603-10291 | arXiv:2603.10291v1 | paper-v1:2603.10291 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10291 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10291 | no |
| SF-2026-ARXIV-2603-10335 | arXiv:2603.10335v1 | paper-v1:2603.10335 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10335 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10335 | no |
| SF-2026-ARXIV-2603-10342 | arXiv:2603.10342v1 | paper-v1:2603.10342 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-10342 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-10342 | no |
| SF-2026-ARXIV-2603-10353 | arXiv:2603.10353v1 | paper-v1:2603.10353 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-10353 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-10353 | no |
| SF-2026-ARXIV-2603-10379 | arXiv:2603.10379v1 | paper-v1:2603.10379 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10379 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10379 | no |
| SF-2026-ARXIV-2603-10422 | arXiv:2603.10422v1 | paper-v1:2603.10422 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10422 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10422 | no |
| SF-2026-ARXIV-2603-10444 | arXiv:2603.10444v1 | paper-v1:2603.10444 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10444 | self | — | new_in_window | TRAIN-PRETRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10444 | no |
| SF-2026-ARXIV-2603-10469 | arXiv:2603.10469v1 | paper-v1:2603.10469 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10469 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10469 | no |
| SF-2026-ARXIV-2603-10494 | arXiv:2603.10494v1 | paper-v1:2603.10494 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10494 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10494 | no |
| SF-2026-ARXIV-2603-10521 | arXiv:2603.10521v1 | paper-v1:2603.10521 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10521 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10521 | no |
| SF-2026-ARXIV-2603-10577 | arXiv:2603.10577v1 | paper-v1:2603.10577 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10577 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10577 | no |
| SF-2026-ARXIV-2603-10600 | arXiv:2603.10600v1 | paper-v1:2603.10600 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10600 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10600 | no |
| SF-2026-ARXIV-2603-10712 | arXiv:2603.10712v1 | paper-v1:2603.10712 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10712 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10712 | no |
| SF-2026-ARXIV-2603-10726 | arXiv:2603.10726v1 | paper-v1:2603.10726 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10726 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10726 | no |
| SF-2026-ARXIV-2603-10742 | arXiv:2603.10742v1 | paper-v1:2603.10742 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10742 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10742 | no |
| SF-2026-ARXIV-2603-10749 | arXiv:2603.10749v1 | paper-v1:2603.10749 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10749 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10749 | no |
| SF-2026-ARXIV-2603-10765 | arXiv:2603.10765v1 | paper-v1:2603.10765 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-10765 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2603-10765 | no |
| SF-2026-ARXIV-2603-10779 | arXiv:2603.10779v1 | paper-v1:2603.10779 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10779 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10779 | no |
| SF-2026-ARXIV-2603-10899 | arXiv:2603.10899v1 | paper-v1:2603.10899 | 2026-W11 | 2026-03-12 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-10899 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10899 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-09983 | RP-90c151425fc2bb47 | standard | arXiv:2603.09983v1 | SRC-ARXIV@arXiv:2603.09983v1 | arXiv:2603.09983v1 HTML — §2.2 Mixture-of-Experts Architecture [facet=method]; https://arxiv.org/html/2603.09983v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.09983v1.html; sha256:5fb1ccdb5ec973aecc86ba17d907c01410ba5b3814119ac94eb061141fe77dae | arXiv:2603.09983v1 HTML — §4.4 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.09983v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.09983v1.html; sha256:5fb1ccdb5ec973aecc86ba17d907c01410ba5b3814119ac94eb061141fe77dae | arXiv:2603.09983v1 HTML — §Appendix H Future Work and Limitations [facet=limitations]; https://arxiv.org/html/2603.09983v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.09983v1.html; sha256:5fb1ccdb5ec973aecc86ba17d907c01410ba5b3814119ac94eb061141fe77dae | arXiv exact-v1 identity https://arxiv.org/abs/2603.09983v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-09983 | complete |
| SF-2026-ARXIV-2603-10030 | RP-3f20a6b94f242c51 | standard | arXiv:2603.10030v1 | SRC-ARXIV@arXiv:2603.10030v1 | arXiv:2603.10030v1 HTML — §Appendix A Methodology [facet=method]; https://arxiv.org/html/2603.10030v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10030v1.html; sha256:2b63d3990048a75ae7f771d5e1abeabcb04320ab4d35858a60563f661c86d30b | arXiv:2603.10030v1 HTML — §6. Evaluation and Discussion [facet=evaluation]; https://arxiv.org/html/2603.10030v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10030v1.html; sha256:2b63d3990048a75ae7f771d5e1abeabcb04320ab4d35858a60563f661c86d30b | arXiv:2603.10030v1 HTML — §6. Evaluation and Discussion [facet=limitations]; https://arxiv.org/html/2603.10030v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10030v1.html; sha256:2b63d3990048a75ae7f771d5e1abeabcb04320ab4d35858a60563f661c86d30b | arXiv exact-v1 identity https://arxiv.org/abs/2603.10030v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10030 | complete |
| SF-2026-ARXIV-2603-10031 | RP-a326c0ad01f3c486 | standard | arXiv:2603.10031v1 | SRC-ARXIV@arXiv:2603.10031v1 | arXiv:2603.10031v1 HTML — §5 Experimental Methodology [facet=method]; https://arxiv.org/html/2603.10031v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10031v1.html; sha256:ae89156301de70986ba561790fcd8f51fad9ffa9d3681a306786904231682af6 | arXiv:2603.10031v1 HTML — §6 Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.10031v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10031v1.html; sha256:ae89156301de70986ba561790fcd8f51fad9ffa9d3681a306786904231682af6 | arXiv:2603.10031v1 HTML — §7.5 Limitations [facet=limitations]; https://arxiv.org/html/2603.10031v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10031v1.html; sha256:ae89156301de70986ba561790fcd8f51fad9ffa9d3681a306786904231682af6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10031v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10031 | complete |
| SF-2026-ARXIV-2603-10032 | RP-ae5d8b36c4df2e75 | standard | arXiv:2603.10032v1 | SRC-ARXIV@arXiv:2603.10032v1 | arXiv:2603.10032v1 HTML — §2 System Architecture [facet=method]; https://arxiv.org/html/2603.10032v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10032v1.html; sha256:65d3637f9178a41b4822db65f57d97921560ee0dd176fdc03a6a93445688d47e | arXiv:2603.10032v1 HTML — §5 Ablation Study under Saturation (Scenario B) [facet=evaluation]; https://arxiv.org/html/2603.10032v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10032v1.html; sha256:65d3637f9178a41b4822db65f57d97921560ee0dd176fdc03a6a93445688d47e | arXiv:2603.10032v1 HTML — §9 Limitations [facet=limitations]; https://arxiv.org/html/2603.10032v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10032v1.html; sha256:65d3637f9178a41b4822db65f57d97921560ee0dd176fdc03a6a93445688d47e | arXiv exact-v1 identity https://arxiv.org/abs/2603.10032v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10032 | complete |
| SF-2026-ARXIV-2603-10044 | RP-98f51a5a2d47eac8 | standard | arXiv:2603.10044v1 | SRC-ARXIV@arXiv:2603.10044v1 | arXiv:2603.10044v1 HTML — §2.1 Safety Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.10044v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10044v1.html; sha256:0aa9dcce18f73a692b579dbc9026986fc658a5b984c4e4d83c6a10e873762d8e | arXiv:2603.10044v1 HTML — §2.1 Safety Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.10044v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10044v1.html; sha256:0aa9dcce18f73a692b579dbc9026986fc658a5b984c4e4d83c6a10e873762d8e | arXiv:2603.10044v1 HTML — §7.4 Limitations [facet=limitations]; https://arxiv.org/html/2603.10044v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10044v1.html; sha256:0aa9dcce18f73a692b579dbc9026986fc658a5b984c4e4d83c6a10e873762d8e | arXiv exact-v1 identity https://arxiv.org/abs/2603.10044v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10044 | complete |
| SF-2026-ARXIV-2603-10057 | RP-ac9e093ec0ea8634 | standard | arXiv:2603.10057v1 | SRC-ARXIV@arXiv:2603.10057v1 | arXiv:2603.10057v1 PDF — §3 METHODOLOGIES [facet=method]; https://arxiv.org/pdf/2603.10057v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10057v1.pdf.txt; sha256:de36234368ed80d53f781aa1b118a8ec8cdc31495975efc528759f5ccfd524b3 | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.10057v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10057v1.pdf.txt; sha256:de36234368ed80d53f781aa1b118a8ec8cdc31495975efc528759f5ccfd524b3 | Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/pdf/2603.10057v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10057v1.pdf.txt; sha256:de36234368ed80d53f781aa1b118a8ec8cdc31495975efc528759f5ccfd524b3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10057v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10057 | complete |
| SF-2026-ARXIV-2603-10060 | RP-2dd52f45cb104d45 | standard | arXiv:2603.10060v1 | SRC-ARXIV@arXiv:2603.10060v1 | arXiv:2603.10060v1 HTML — §4.3 Injection Methodology [facet=method]; https://arxiv.org/html/2603.10060v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10060v1.html; sha256:a6efc0dd1d7e9d58ff1e123f91d434867b47482caa8ed38deec1cacf49dcbf4a | arXiv:2603.10060v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10060v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10060v1.html; sha256:a6efc0dd1d7e9d58ff1e123f91d434867b47482caa8ed38deec1cacf49dcbf4a | arXiv:2603.10060v1 HTML — §6.4 Limitations [facet=limitations]; https://arxiv.org/html/2603.10060v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10060v1.html; sha256:a6efc0dd1d7e9d58ff1e123f91d434867b47482caa8ed38deec1cacf49dcbf4a | arXiv exact-v1 identity https://arxiv.org/abs/2603.10060v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10060 | complete |
| SF-2026-ARXIV-2603-10062 | RP-2ccd42bfc504fc08 | standard | arXiv:2603.10062v1 | SRC-ARXIV@arXiv:2603.10062v1 | arXiv:2603.10062v1 HTML — §4. An Architecture-Inspired Memory Hierarchy [facet=method]; https://arxiv.org/html/2603.10062v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10062v1.html; sha256:98f08f8f7bd8729da33311cdde5f38ad5d387a36302e2bfe3446b3d2f2a7d8e8 | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.10062v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10062v1.html; sha256:98f08f8f7bd8729da33311cdde5f38ad5d387a36302e2bfe3446b3d2f2a7d8e8 | arXiv:2603.10062v1 HTML — §7. Conclusion [facet=limitations]; https://arxiv.org/html/2603.10062v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10062v1.html; sha256:98f08f8f7bd8729da33311cdde5f38ad5d387a36302e2bfe3446b3d2f2a7d8e8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10062v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10062 | complete |
| SF-2026-ARXIV-2603-10085 | RP-6680fc50a9e6dba1 | standard | arXiv:2603.10085v1 | SRC-ARXIV@arXiv:2603.10085v1 | arXiv:2603.10085v1 HTML — §4.1.1 Framework Overview [facet=method]; https://arxiv.org/html/2603.10085v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10085v1.html; sha256:679d57469d71cd5214c9f232eec2613934c44469cc5ac9ea9e7bb292e7bebe37 | arXiv:2603.10085v1 HTML — §5.4 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.10085v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10085v1.html; sha256:679d57469d71cd5214c9f232eec2613934c44469cc5ac9ea9e7bb292e7bebe37 | arXiv:2603.10085v1 HTML — §5.5 Ablation [facet=limitations]; https://arxiv.org/html/2603.10085v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10085v1.html; sha256:679d57469d71cd5214c9f232eec2613934c44469cc5ac9ea9e7bb292e7bebe37 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10085v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10085 | complete |
| SF-2026-ARXIV-2603-10087 | RP-95734dd04ca7af08 | standard | arXiv:2603.10087v1 | SRC-ARXIV@arXiv:2603.10087v1 | arXiv:2603.10087v1 HTML — §4.3. Implementation in Inference Framework [facet=method]; https://arxiv.org/html/2603.10087v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10087v1.html; sha256:8cd14261133a22c838f94d2c60ff6bb10edab36d06e6433bc044e72f04b0c00d | arXiv:2603.10087v1 HTML — §5.4. Cost Analysis [facet=evaluation]; https://arxiv.org/html/2603.10087v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10087v1.html; sha256:8cd14261133a22c838f94d2c60ff6bb10edab36d06e6433bc044e72f04b0c00d | arXiv:2603.10087v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.10087v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10087v1.html; sha256:8cd14261133a22c838f94d2c60ff6bb10edab36d06e6433bc044e72f04b0c00d | arXiv exact-v1 identity https://arxiv.org/abs/2603.10087v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10087 | complete |
| SF-2026-ARXIV-2603-10088 | RP-110c0e7244c42bd5 | standard | arXiv:2603.10088v1 | SRC-ARXIV@arXiv:2603.10088v1 | arXiv:2603.10088v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.10088v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10088v1.html; sha256:47958e696898d84295cb3d1378e1e64a765c47a349ad6d1f8559f97dfcef8cc9 | arXiv:2603.10088v1 HTML — §6.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.10088v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10088v1.html; sha256:47958e696898d84295cb3d1378e1e64a765c47a349ad6d1f8559f97dfcef8cc9 | arXiv:2603.10088v1 HTML — §7 Discussion [facet=limitations]; https://arxiv.org/html/2603.10088v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10088v1.html; sha256:47958e696898d84295cb3d1378e1e64a765c47a349ad6d1f8559f97dfcef8cc9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10088v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10088 | complete |
| SF-2026-ARXIV-2603-10143 | RP-791308a7826f5dc8 | standard | arXiv:2603.10143v1 | SRC-ARXIV@arXiv:2603.10143v1 | arXiv:2603.10143v1 HTML — §3.1. Framework Architecture [facet=method]; https://arxiv.org/html/2603.10143v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10143v1.html; sha256:93e20bc8c615691811d46de714c92bac1e20c60d043b1a7363ae1cc738c40a48 | arXiv:2603.10143v1 HTML — §4.2. Human Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.10143v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10143v1.html; sha256:93e20bc8c615691811d46de714c92bac1e20c60d043b1a7363ae1cc738c40a48 | arXiv:2603.10143v1 HTML — §6. Limitations [facet=limitations]; https://arxiv.org/html/2603.10143v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10143v1.html; sha256:93e20bc8c615691811d46de714c92bac1e20c60d043b1a7363ae1cc738c40a48 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10143v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10143 | complete |
| SF-2026-ARXIV-2603-10163 | RP-5b3cfb3c6ad9d2fc | standard | arXiv:2603.10163v1 | SRC-ARXIV@arXiv:2603.10163v1 | arXiv:2603.10163v1 HTML — §IV-B Challenges and Approach Overview [facet=method]; https://arxiv.org/html/2603.10163v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10163v1.html; sha256:cb581dfd131fe05e09fb521930bd69cf75ef47afed20197a1fad2ea02dcada51 | arXiv:2603.10163v1 HTML — §V Evaluations [facet=evaluation]; https://arxiv.org/html/2603.10163v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10163v1.html; sha256:cb581dfd131fe05e09fb521930bd69cf75ef47afed20197a1fad2ea02dcada51 | arXiv:2603.10163v1 HTML — §IV-A Limitations of Existing Tools [facet=limitations]; https://arxiv.org/html/2603.10163v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10163v1.html; sha256:cb581dfd131fe05e09fb521930bd69cf75ef47afed20197a1fad2ea02dcada51 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10163v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10163 | complete |
| SF-2026-ARXIV-2603-10165 | RP-0cbb2cade2a7cc87 | standard | arXiv:2603.10165v1 | SRC-ARXIV@arXiv:2603.10165v1 | arXiv:2603.10165v1 HTML — §4.3 Combine Binary and OPD Methods [facet=method]; https://arxiv.org/html/2603.10165v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10165v1.html; sha256:d41332e35f806913236ca2dd9e55b0c46aaa6ab83661ce156fd5c1aae3606766 | arXiv:2603.10165v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.10165v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10165v1.html; sha256:d41332e35f806913236ca2dd9e55b0c46aaa6ab83661ce156fd5c1aae3606766 | arXiv:2603.10165v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.10165v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10165v1.html; sha256:d41332e35f806913236ca2dd9e55b0c46aaa6ab83661ce156fd5c1aae3606766 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10165v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10165 | complete |
| SF-2026-ARXIV-2603-10291 | RP-804df1c74c862597 | standard | arXiv:2603.10291v1 | SRC-ARXIV@arXiv:2603.10291v1 | arXiv:2603.10291v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.10291v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10291v1.html; sha256:f1b527c23c0cfb10216bfdc0fa78aa946f75e703b2686ff8b42d6ff47de5dc77 | arXiv:2603.10291v1 HTML — §Appendix B Additional Qualitative Results [facet=evaluation]; https://arxiv.org/html/2603.10291v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10291v1.html; sha256:f1b527c23c0cfb10216bfdc0fa78aa946f75e703b2686ff8b42d6ff47de5dc77 | arXiv:2603.10291v1 HTML — §6 Limitations [facet=limitations]; https://arxiv.org/html/2603.10291v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10291v1.html; sha256:f1b527c23c0cfb10216bfdc0fa78aa946f75e703b2686ff8b42d6ff47de5dc77 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10291v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10291 | complete |
| SF-2026-ARXIV-2603-10335 | RP-fef200f857c16921 | standard | arXiv:2603.10335v1 | SRC-ARXIV@arXiv:2603.10335v1 | arXiv:2603.10335v1 HTML — §4.4 Fuel Gauge Implementation [facet=method]; https://arxiv.org/html/2603.10335v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10335v1.html; sha256:ff3b6d57b7607d420615663bbd189d961b98dd5baea13908007f00b2140a6239 | arXiv:2603.10335v1 HTML — §B.1 Experimental Results on LMM Intern-S1 [facet=evaluation]; https://arxiv.org/html/2603.10335v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10335v1.html; sha256:ff3b6d57b7607d420615663bbd189d961b98dd5baea13908007f00b2140a6239 | arXiv:2603.10335v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.10335v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10335v1.html; sha256:ff3b6d57b7607d420615663bbd189d961b98dd5baea13908007f00b2140a6239 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10335v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10335 | complete |
| SF-2026-ARXIV-2603-10342 | RP-2c19da6e13a73272 | deep | arXiv:2603.10342v1 | SRC-ARXIV@arXiv:2603.10342v1 | arXiv:2603.10342v1 HTML — §III-A–§III-C request classification, TPOT feedback and Green Context isolation [facet=method]; https://arxiv.org/html/2603.10342v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10342v1.html; sha256:8a505f2cb52a0df7a5af7e27b4f6344f73adbbdda5cfec8dd22a6fe1b50bba0d | arXiv:2603.10342v1 HTML — §IV complete consumer-GPU evaluation [facet=evaluation]; https://arxiv.org/html/2603.10342v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10342v1.html; sha256:8a505f2cb52a0df7a5af7e27b4f6344f73adbbdda5cfec8dd22a6fe1b50bba0d | arXiv:2603.10342v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.10342v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10342v1.html; sha256:8a505f2cb52a0df7a5af7e27b4f6344f73adbbdda5cfec8dd22a6fe1b50bba0d | arXiv exact-v1 identity https://arxiv.org/abs/2603.10342v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10342 | complete |
| SF-2026-ARXIV-2603-10353 | RP-ee59d154a1e22965 | deep | arXiv:2603.10353v1 | SRC-ARXIV@arXiv:2603.10353v1 | arXiv:2603.10353v1 HTML — §3.2–§3.3 calibrated per-head budgets and greedy assignment [facet=method]; https://arxiv.org/html/2603.10353v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10353v1.html; sha256:dc39630f1baf826e220e48d339e96ba8c86946c98e4f1b40faad89ac0958dd69 | arXiv:2603.10353v1 HTML — §5.1–§5.4 evaluation and ablation [facet=evaluation]; https://arxiv.org/html/2603.10353v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10353v1.html; sha256:dc39630f1baf826e220e48d339e96ba8c86946c98e4f1b40faad89ac0958dd69 | Not Disclosed — exact-v1 has no dedicated limitations section; drift/network fallback is project design inference [facet=limitations]; https://arxiv.org/html/2603.10353v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10353v1.html; sha256:dc39630f1baf826e220e48d339e96ba8c86946c98e4f1b40faad89ac0958dd69 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10353v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10353 | complete |
| SF-2026-ARXIV-2603-10379 | RP-694dbe84842d5e93 | standard | arXiv:2603.10379v1 | SRC-ARXIV@arXiv:2603.10379v1 | arXiv:2603.10379v1 HTML — §B.1 Model Architecture and Training Configuration [facet=method]; https://arxiv.org/html/2603.10379v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10379v1.html; sha256:80f21e65a9250ce34a004a8e6881442bca43a2c2d4ebf37f8b58e131450d6828 | arXiv:2603.10379v1 HTML — §4.2 Empirical Validation of the Extended Scaling Law [facet=evaluation]; https://arxiv.org/html/2603.10379v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10379v1.html; sha256:80f21e65a9250ce34a004a8e6881442bca43a2c2d4ebf37f8b58e131450d6828 | arXiv:2603.10379v1 HTML — §6.2 Limitations [facet=limitations]; https://arxiv.org/html/2603.10379v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10379v1.html; sha256:80f21e65a9250ce34a004a8e6881442bca43a2c2d4ebf37f8b58e131450d6828 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10379v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10379 | complete |
| SF-2026-ARXIV-2603-10422 | RP-c853ec4897903e56 | standard | arXiv:2603.10422v1 | SRC-ARXIV@arXiv:2603.10422v1 | arXiv:2603.10422v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.10422v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10422v1.html; sha256:5ae8550f2b8ec703e0ce481fba7829d9a358cc518feec6d5cb9e1e38c231d9c3 | arXiv:2603.10422v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10422v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10422v1.html; sha256:5ae8550f2b8ec703e0ce481fba7829d9a358cc518feec6d5cb9e1e38c231d9c3 | arXiv:2603.10422v1 HTML — §D Failure Cases Analysis [facet=limitations]; https://arxiv.org/html/2603.10422v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10422v1.html; sha256:5ae8550f2b8ec703e0ce481fba7829d9a358cc518feec6d5cb9e1e38c231d9c3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10422v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10422 | complete |
| SF-2026-ARXIV-2603-10444 | RP-8cd2c7c1bd3c81b1 | standard | arXiv:2603.10444v1 | SRC-ARXIV@arXiv:2603.10444v1 | arXiv:2603.10444v1 HTML — §5 Mean Bias-Aware Low-Bit Training Method [facet=method]; https://arxiv.org/html/2603.10444v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10444v1.html; sha256:7c909e8a75bb638999783b063eefe925d130f9688b5785b9ba6c11576629c617 | arXiv:2603.10444v1 HTML — §6.2 Results [facet=evaluation]; https://arxiv.org/html/2603.10444v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10444v1.html; sha256:7c909e8a75bb638999783b063eefe925d130f9688b5785b9ba6c11576629c617 | arXiv:2603.10444v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.10444v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10444v1.html; sha256:7c909e8a75bb638999783b063eefe925d130f9688b5785b9ba6c11576629c617 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10444v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10444 | complete |
| SF-2026-ARXIV-2603-10469 | RP-ce840a40ef16fbe6 | standard | arXiv:2603.10469v1 | SRC-ARXIV@arXiv:2603.10469v1 | arXiv:2603.10469v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.10469v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10469v1.html; sha256:5fb50d9e6e171900dfce6db89e25683a23d49f4100f7febf37dbd853a20072b9 | arXiv:2603.10469v1 HTML — §IV EXPERIMENTS [facet=evaluation]; https://arxiv.org/html/2603.10469v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10469v1.html; sha256:5fb50d9e6e171900dfce6db89e25683a23d49f4100f7febf37dbd853a20072b9 | arXiv:2603.10469v1 HTML — §V CONCLUSION [facet=limitations]; https://arxiv.org/html/2603.10469v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10469v1.html; sha256:5fb50d9e6e171900dfce6db89e25683a23d49f4100f7febf37dbd853a20072b9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10469v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10469 | complete |
| SF-2026-ARXIV-2603-10494 | RP-ce47dec6debee7e6 | standard | arXiv:2603.10494v1 | SRC-ARXIV@arXiv:2603.10494v1 | arXiv:2603.10494v1 PDF — §Method [facet=method]; https://arxiv.org/pdf/2603.10494v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf.txt; sha256:adcff730d907dbf787e1da6ca65d0fcf8fc357220df6c463f13da50b47403af3 | arXiv:2603.10494v1 PDF — §Experimental Setup [facet=evaluation]; https://arxiv.org/pdf/2603.10494v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf.txt; sha256:adcff730d907dbf787e1da6ca65d0fcf8fc357220df6c463f13da50b47403af3 | arXiv:2603.10494v1 PDF — §Limitations [facet=limitations]; https://arxiv.org/pdf/2603.10494v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf.txt; sha256:adcff730d907dbf787e1da6ca65d0fcf8fc357220df6c463f13da50b47403af3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10494v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10494 | complete |
| SF-2026-ARXIV-2603-10521 | RP-a2dda116e706417b | standard | arXiv:2603.10521v1 | SRC-ARXIV@arXiv:2603.10521v1 | arXiv:2603.10521v1 HTML — §3 Constructing IH-Challenge [facet=method]; https://arxiv.org/html/2603.10521v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10521v1.html; sha256:d19c81186ba879aa23607b6bbee9f8601b76bd90e1c1d9b4e2975a9fb9cbc8ff | arXiv:2603.10521v1 HTML — §5.1 Ablation on Training Task Splits [facet=evaluation]; https://arxiv.org/html/2603.10521v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10521v1.html; sha256:d19c81186ba879aa23607b6bbee9f8601b76bd90e1c1d9b4e2975a9fb9cbc8ff | arXiv:2603.10521v1 HTML — §7 Conclusion [facet=limitations]; https://arxiv.org/html/2603.10521v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10521v1.html; sha256:d19c81186ba879aa23607b6bbee9f8601b76bd90e1c1d9b4e2975a9fb9cbc8ff | arXiv exact-v1 identity https://arxiv.org/abs/2603.10521v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10521 | complete |
| SF-2026-ARXIV-2603-10577 | RP-f3d0f64843a2f406 | standard | arXiv:2603.10577v1 | SRC-ARXIV@arXiv:2603.10577v1 | arXiv:2603.10577v1 HTML — §3.1. Vision-Language Model–Based Auditors [facet=method]; https://arxiv.org/html/2603.10577v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10577v1.html; sha256:9604846d5181c13bff513fd3c98bc51bf84fbacbb5aea112b5cbc03d26eb731f | arXiv:2603.10577v1 HTML — §3.2. Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.10577v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10577v1.html; sha256:9604846d5181c13bff513fd3c98bc51bf84fbacbb5aea112b5cbc03d26eb731f | arXiv:2603.10577v1 HTML — §5. Discussion and Limitations [facet=limitations]; https://arxiv.org/html/2603.10577v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10577v1.html; sha256:9604846d5181c13bff513fd3c98bc51bf84fbacbb5aea112b5cbc03d26eb731f | arXiv exact-v1 identity https://arxiv.org/abs/2603.10577v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10577 | complete |
| SF-2026-ARXIV-2603-10600 | RP-ae61bccf624cbde0 | standard | arXiv:2603.10600v1 | SRC-ARXIV@arXiv:2603.10600v1 | arXiv:2603.10600v1 HTML — §5.1. Memory Taxonomies and Architectures [facet=method]; https://arxiv.org/html/2603.10600v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10600v1.html; sha256:ef1376e3fc1dce021991f7cc6dc998afceecd701ab0353e83f9e8ff258a78690 | arXiv:2603.10600v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.10600v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10600v1.html; sha256:ef1376e3fc1dce021991f7cc6dc998afceecd701ab0353e83f9e8ff258a78690 | arXiv:2603.10600v1 HTML — §6. Conclusions [facet=limitations]; https://arxiv.org/html/2603.10600v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10600v1.html; sha256:ef1376e3fc1dce021991f7cc6dc998afceecd701ab0353e83f9e8ff258a78690 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10600v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10600 | complete |
| SF-2026-ARXIV-2603-10712 | RP-ea6ba0da733a0882 | standard | arXiv:2603.10712v1 | SRC-ARXIV@arXiv:2603.10712v1 | arXiv:2603.10712v1 HTML — §0.A.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.10712v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10712v1.html; sha256:a8904875126ed2d192924038380d27f95aa242e8869da32bf92670f3ae331c6d | arXiv:2603.10712v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10712v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10712v1.html; sha256:a8904875126ed2d192924038380d27f95aa242e8869da32bf92670f3ae331c6d | arXiv:2603.10712v1 HTML — §0.A.4 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.10712v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10712v1.html; sha256:a8904875126ed2d192924038380d27f95aa242e8869da32bf92670f3ae331c6d | arXiv exact-v1 identity https://arxiv.org/abs/2603.10712v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10712 | complete |
| SF-2026-ARXIV-2603-10726 | RP-80a55e7f4eadbb75 | standard | arXiv:2603.10726v1 | SRC-ARXIV@arXiv:2603.10726v1 | arXiv:2603.10726v1 HTML — §3. System Design [facet=method]; https://arxiv.org/html/2603.10726v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10726v1.html; sha256:c84d6e9b9ca1832501f4f91aeb12e88d4c6a2c107d48d1a793836521930385ce | arXiv:2603.10726v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.10726v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10726v1.html; sha256:c84d6e9b9ca1832501f4f91aeb12e88d4c6a2c107d48d1a793836521930385ce | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Limitations 章节 [facet=limitations]; https://arxiv.org/html/2603.10726v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10726v1.html; sha256:c84d6e9b9ca1832501f4f91aeb12e88d4c6a2c107d48d1a793836521930385ce | arXiv exact-v1 identity https://arxiv.org/abs/2603.10726v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10726 | complete |
| SF-2026-ARXIV-2603-10742 | RP-ba5f87c7641cef10 | standard | arXiv:2603.10742v1 | SRC-ARXIV@arXiv:2603.10742v1 | arXiv:2603.10742v1 HTML — §4 Design Properties [facet=method]; https://arxiv.org/html/2603.10742v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10742v1.html; sha256:a57cd3d2107ffa0e07b437df61bf9d69b7bfc23cb57186395cb750384177cf0f | arXiv:2603.10742v1 HTML — §8.4 External validation [facet=evaluation]; https://arxiv.org/html/2603.10742v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10742v1.html; sha256:a57cd3d2107ffa0e07b437df61bf9d69b7bfc23cb57186395cb750384177cf0f | arXiv:2603.10742v1 HTML — §9 Conclusion [facet=limitations]; https://arxiv.org/html/2603.10742v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10742v1.html; sha256:a57cd3d2107ffa0e07b437df61bf9d69b7bfc23cb57186395cb750384177cf0f | arXiv exact-v1 identity https://arxiv.org/abs/2603.10742v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10742 | complete |
| SF-2026-ARXIV-2603-10749 | RP-fdf5f9f2e0ebd934 | standard | arXiv:2603.10749v1 | SRC-ARXIV@arXiv:2603.10749v1 | arXiv:2603.10749v1 HTML — §D.2 Attack framework: OpenEvolve [facet=method]; https://arxiv.org/html/2603.10749v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10749v1.html; sha256:5f4b606c2c56b52dee9ff67e949609b4aa321400ae0146c1bd81f5cb2e647459 | arXiv:2603.10749v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.10749v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10749v1.html; sha256:5f4b606c2c56b52dee9ff67e949609b4aa321400ae0146c1bd81f5cb2e647459 | arXiv:2603.10749v1 HTML — §3.1 Limitations of Model-level Defenses [facet=limitations]; https://arxiv.org/html/2603.10749v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10749v1.html; sha256:5f4b606c2c56b52dee9ff67e949609b4aa321400ae0146c1bd81f5cb2e647459 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10749v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10749 | complete |
| SF-2026-ARXIV-2603-10765 | RP-623b53cd5b359515 | deep | arXiv:2603.10765v1 | SRC-ARXIV@arXiv:2603.10765v1 | arXiv:2603.10765v1 HTML — §3.1–§3.5 configurable pipeline, workload and profiler design [facet=method]; https://arxiv.org/html/2603.10765v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10765v1.html; sha256:6468028dd15e9e48de41cbd04f421d23dc99c8a41ff17c4ef6986ef49fa9131f | arXiv:2603.10765v1 HTML — §5.2–§5.8 latency, throughput, accuracy, update, resource, sensitivity and overhead evaluation [facet=evaluation]; https://arxiv.org/html/2603.10765v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10765v1.html; sha256:6468028dd15e9e48de41cbd04f421d23dc99c8a41ff17c4ef6986ef49fa9131f | arXiv:2603.10765v1 HTML — §7. Conclusion [facet=limitations]; https://arxiv.org/html/2603.10765v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10765v1.html; sha256:6468028dd15e9e48de41cbd04f421d23dc99c8a41ff17c4ef6986ef49fa9131f | arXiv exact-v1 identity https://arxiv.org/abs/2603.10765v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10765 | complete |
| SF-2026-ARXIV-2603-10779 | RP-6f4da65222bf7d28 | standard | arXiv:2603.10779v1 | SRC-ARXIV@arXiv:2603.10779v1 | arXiv:2603.10779v1 HTML — §II Problem Formulation and Unified Agentic Control Architecture [facet=method]; https://arxiv.org/html/2603.10779v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10779v1.html; sha256:ee40a7c3badac0d3c66cedecd8078e033f9664c394faa7926f8111b79ea7d9ab | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.10779v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10779v1.html; sha256:ee40a7c3badac0d3c66cedecd8078e033f9664c394faa7926f8111b79ea7d9ab | arXiv:2603.10779v1 HTML — §V-F Discussion and Limitations of the Linear Setting [facet=limitations]; https://arxiv.org/html/2603.10779v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10779v1.html; sha256:ee40a7c3badac0d3c66cedecd8078e033f9664c394faa7926f8111b79ea7d9ab | arXiv exact-v1 identity https://arxiv.org/abs/2603.10779v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10779 | complete |
| SF-2026-ARXIV-2603-10899 | RP-5b874443549eb92a | standard | arXiv:2603.10899v1 | SRC-ARXIV@arXiv:2603.10899v1 | arXiv:2603.10899v1 HTML — §3 Proposed Method: LookaheadKV [facet=method]; https://arxiv.org/html/2603.10899v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10899v1.html; sha256:1b28d1872dbab87bed2a2fe997bb2b9481c2f865129184e1b50e595a3261a630 | arXiv:2603.10899v1 HTML — §4.2 Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.10899v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10899v1.html; sha256:1b28d1872dbab87bed2a2fe997bb2b9481c2f865129184e1b50e595a3261a630 | arXiv:2603.10899v1 HTML — §7 Conclusion and Limitation [facet=limitations]; https://arxiv.org/html/2603.10899v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10899v1.html; sha256:1b28d1872dbab87bed2a2fe997bb2b9481c2f865129184e1b50e595a3261a630 | arXiv exact-v1 identity https://arxiv.org/abs/2603.10899v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-10899 | complete |

### Source Reviews

### MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios

<!-- review:SF-2026-ARXIV-2603-09983:start -->
**问题**：edge MoE 的 expert offload 在需求出现后才搬运，I/O 会阻塞 token；普通 speculation 只优化 compute。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：MoE-SpAc 把 draft lookahead 当 expert demand sensor，联合执行预取、淘汰与异构 workload placement。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.09983v1 HTML — §2.2 Mixture-of-Experts Architecture [facet=method]; https://arxiv.org/html/2603.09983v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.09983v1.html; sha256:5fb1ccdb5ec973aecc86ba17d907c01410ba5b3814119ac94eb061141fe77dae`。

**Evaluation contract 与未证明部分**：实验绑定七个 benchmark、具体模型/设备/预算；不证明预测在路由漂移时仍保持命中。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.09983v1 HTML — §4.4 Ablation Study [facet=evaluation]; https://arxiv.org/html/2603.09983v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.09983v1.html; sha256:5fb1ccdb5ec973aecc86ba17d907c01410ba5b3814119ac94eb061141fe77dae`。

**Trade-off / failure / coexistence**：预取会浪费 I/O 和显存，mis-speculation 形成新尾延迟；expert 常驻可行时无需该路径。

<!-- claim:SF-2026-ARXIV-2603-09983:start -->**Claim Boundary**：只支持 arXiv:2603.09983v1 §2.2 Mixture-of-Experts Architecture 的机制与 §4.4 Ablation Study 的公开 workload；§Appendix H Future Work and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-09983:end -->
<!-- review:SF-2026-ARXIV-2603-09983:end -->
### The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths

<!-- review:SF-2026-ARXIV-2603-10030:start -->
**问题**：AI transport 默认 buffer 已正确分配、注册并安全回收，completion/teardown 时 ownership 仍隐含。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：dmaplane 以 kernel UAPI 管理 NUMA allocation、dma-buf、RDMA credit、GPU BAR pinning 与 completion-safe lifecycle。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.10030v1 HTML — §Appendix A Methodology [facet=method]; https://arxiv.org/html/2603.10030v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10030v1.html; sha256:2b63d3990048a75ae7f771d5e1abeabcb04320ab4d35858a60563f661c86d30b`。

**Evaluation contract 与未证明部分**：Soft-RoCE 和指定 GPU/NUMA 测量支持实现行为；不代表 provider-independent performance。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10030v1 HTML — §6. Evaluation and Discussion [facet=evaluation]; https://arxiv.org/html/2603.10030v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10030v1.html; sha256:2b63d3990048a75ae7f771d5e1abeabcb04320ab4d35858a60563f661c86d30b`。

**Trade-off / failure / coexistence**：统一 buffer plane 减少 glue code，却扩大内核 TCB 与 pinning 风险；单机 memcpy 路径仍更简单。

<!-- claim:SF-2026-ARXIV-2603-10030:start -->**Claim Boundary**：只支持 arXiv:2603.10030v1 §Appendix A Methodology 的机制与 §6. Evaluation and Discussion 的公开 workload；§6. Evaluation and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10030:end -->
<!-- review:SF-2026-ARXIV-2603-10030:end -->
### Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study

<!-- review:SF-2026-ARXIV-2603-10031:start -->
**问题**：`Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `5 Experimental Methodology` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.10031v1 HTML — §5 Experimental Methodology [facet=method]; https://arxiv.org/html/2603.10031v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10031v1.html; sha256:ae89156301de70986ba561790fcd8f51fad9ffa9d3681a306786904231682af6`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6 Results and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10031v1 HTML — §6 Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.10031v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10031v1.html; sha256:ae89156301de70986ba561790fcd8f51fad9ffa9d3681a306786904231682af6`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7.5 Limitations`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-10031:start -->**Claim Boundary**：只支持 arXiv:2603.10031v1 §5 Experimental Methodology 的机制与 §6 Results and Analysis 的公开 workload；§7.5 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10031:end -->
<!-- review:SF-2026-ARXIV-2603-10031:end -->
### HTM-EAR: Importance-Preserving Tiered Memory with Hybrid Routing under Saturation

<!-- review:SF-2026-ARXIV-2603-10032:start -->
**问题**：`HTM-EAR: Importance-Preserving Tiered Memory with Hybrid Routing under Saturation` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `2 System Architecture` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.10032v1 HTML — §2 System Architecture [facet=method]; https://arxiv.org/html/2603.10032v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10032v1.html; sha256:65d3637f9178a41b4822db65f57d97921560ee0dd176fdc03a6a93445688d47e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Ablation Study under Saturation (Scenario B)`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10032v1 HTML — §5 Ablation Study under Saturation (Scenario B) [facet=evaluation]; https://arxiv.org/html/2603.10032v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10032v1.html; sha256:65d3637f9178a41b4822db65f57d97921560ee0dd176fdc03a6a93445688d47e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `9 Limitations`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-10032:start -->**Claim Boundary**：只支持 arXiv:2603.10032v1 §2 System Architecture 的机制与 §5 Ablation Study under Saturation (Scenario B) 的公开 workload；§9 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10032:end -->
<!-- review:SF-2026-ARXIV-2603-10032:end -->
### Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety

<!-- review:SF-2026-ARXIV-2603-10044:start -->
**问题**：`Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `2.1 Safety Evaluation Methodology` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.10044v1 HTML — §2.1 Safety Evaluation Methodology [facet=method]; https://arxiv.org/html/2603.10044v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10044v1.html; sha256:0aa9dcce18f73a692b579dbc9026986fc658a5b984c4e4d83c6a10e873762d8e`。

**Evaluation contract 与未证明部分**：公开验证定位在 `2.1 Safety Evaluation Methodology`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10044v1 HTML — §2.1 Safety Evaluation Methodology [facet=evaluation]; https://arxiv.org/html/2603.10044v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10044v1.html; sha256:0aa9dcce18f73a692b579dbc9026986fc658a5b984c4e4d83c6a10e873762d8e`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7.4 Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-10044:start -->**Claim Boundary**：只支持 arXiv:2603.10044v1 §2.1 Safety Evaluation Methodology 的机制与 §2.1 Safety Evaluation Methodology 的公开 workload；§7.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10044:end -->
<!-- review:SF-2026-ARXIV-2603-10044:end -->
### SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation

<!-- review:SF-2026-ARXIV-2603-10057:start -->
**问题**：`SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3 METHODOLOGIES` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.10057v1 PDF — §3 METHODOLOGIES [facet=method]; https://arxiv.org/pdf/2603.10057v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10057v1.pdf.txt; sha256:de36234368ed80d53f781aa1b118a8ec8cdc31495975efc528759f5ccfd524b3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 PDF 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/pdf/2603.10057v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10057v1.pdf.txt; sha256:de36234368ed80d53f781aa1b118a8ec8cdc31495975efc528759f5ccfd524b3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-10057:start -->**Claim Boundary**：只支持 arXiv:2603.10057v1 §3 METHODOLOGIES 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10057:end -->
<!-- review:SF-2026-ARXIV-2603-10057:end -->
### Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents

<!-- review:SF-2026-ARXIV-2603-10060:start -->
**问题**：`Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents` 检查的是 `AGENT-TOOL-CALLING` 中 外部 action、side effect 和动态工具目录要求把提议与执行分离。 是否会改变现有设计边界。

**旧路径为何合理**：模型只输出文本时，错误影响停留在信息层。

**约束变化与机制**：exact-v1 的 `4.3 Injection Methodology` 把论文方案定位到 tool identity、argument validation、authorization、receipt 与 side-effect commit；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-TOOL-CALLING` 负责 tool identity、argument validation、authorization、receipt 与 side-effect commit；定位证据为 `arXiv:2603.10060v1 HTML — §4.3 Injection Methodology [facet=method]; https://arxiv.org/html/2603.10060v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10060v1.html; sha256:a6efc0dd1d7e9d58ff1e123f91d434867b47482caa8ed38deec1cacf49dcbf4a`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10060v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10060v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10060v1.html; sha256:a6efc0dd1d7e9d58ff1e123f91d434867b47482caa8ed38deec1cacf49dcbf4a`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6.4 Limitations`。只读、无副作用查询仍可使用较薄的调用适配层。

<!-- claim:SF-2026-ARXIV-2603-10060:start -->**Claim Boundary**：只支持 arXiv:2603.10060v1 §4.3 Injection Methodology 的机制与 §5.2 Main Results 的公开 workload；§6.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10060:end -->
<!-- review:SF-2026-ARXIV-2603-10060:end -->
### Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead

<!-- review:SF-2026-ARXIV-2603-10062:start -->
**问题**：`Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `4. An Architecture-Inspired Memory Hierarchy` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.10062v1 HTML — §4. An Architecture-Inspired Memory Hierarchy [facet=method]; https://arxiv.org/html/2603.10062v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10062v1.html; sha256:98f08f8f7bd8729da33311cdde5f38ad5d387a36302e2bfe3446b3d2f2a7d8e8`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.10062v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10062v1.html; sha256:98f08f8f7bd8729da33311cdde5f38ad5d387a36302e2bfe3446b3d2f2a7d8e8`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7. Conclusion`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-10062:start -->**Claim Boundary**：只支持 arXiv:2603.10062v1 §4. An Architecture-Inspired Memory Hierarchy 的机制与 §Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10062:end -->
<!-- review:SF-2026-ARXIV-2603-10062:end -->
### KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization

<!-- review:SF-2026-ARXIV-2603-10085:start -->
**问题**：`KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `4.1.1 Framework Overview` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.10085v1 HTML — §4.1.1 Framework Overview [facet=method]; https://arxiv.org/html/2603.10085v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10085v1.html; sha256:679d57469d71cd5214c9f232eec2613934c44469cc5ac9ea9e7bb292e7bebe37`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.4 Experimental Results and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10085v1 HTML — §5.4 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.10085v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10085v1.html; sha256:679d57469d71cd5214c9f232eec2613934c44469cc5ac9ea9e7bb292e7bebe37`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5.5 Ablation`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-10085:start -->**Claim Boundary**：只支持 arXiv:2603.10085v1 §4.1.1 Framework Overview 的机制与 §5.4 Experimental Results and Analysis 的公开 workload；§5.5 Ablation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10085:end -->
<!-- review:SF-2026-ARXIV-2603-10085:end -->
### Pooling Engram Conditional Memory in Large Language Models using CXL

<!-- review:SF-2026-ARXIV-2603-10087:start -->
**问题**：`Pooling Engram Conditional Memory in Large Language Models using CXL` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `4.3. Implementation in Inference Framework` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.10087v1 HTML — §4.3. Implementation in Inference Framework [facet=method]; https://arxiv.org/html/2603.10087v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10087v1.html; sha256:8cd14261133a22c838f94d2c60ff6bb10edab36d06e6433bc044e72f04b0c00d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.4. Cost Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10087v1 HTML — §5.4. Cost Analysis [facet=evaluation]; https://arxiv.org/html/2603.10087v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10087v1.html; sha256:8cd14261133a22c838f94d2c60ff6bb10edab36d06e6433bc044e72f04b0c00d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Discussion`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-10087:start -->**Claim Boundary**：只支持 arXiv:2603.10087v1 §4.3. Implementation in Inference Framework 的机制与 §5.4. Cost Analysis 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10087:end -->
<!-- review:SF-2026-ARXIV-2603-10087:end -->
### ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping

<!-- review:SF-2026-ARXIV-2603-10088:start -->
**问题**：`ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping` 检查的是 `INFER-SPECULATIVE-DECODING` 中 decode 的串行依赖限制利用率，促使系统用廉价 proposal 换取并行验证。 是否会改变现有设计边界。

**旧路径为何合理**：逐 token 串行验证保持 exactness，且不维护额外 draft 状态。

**约束变化与机制**：exact-v1 的 `5 Methodology` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SPECULATIVE-DECODING` 负责 proposal、验证、接受/回滚与缓存提交状态；定位证据为 `arXiv:2603.10088v1 HTML — §5 Methodology [facet=method]; https://arxiv.org/html/2603.10088v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10088v1.html; sha256:47958e696898d84295cb3d1378e1e64a765c47a349ad6d1f8559f97dfcef8cc9`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.2 Main results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10088v1 HTML — §6.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.10088v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10088v1.html; sha256:47958e696898d84295cb3d1378e1e64a765c47a349ad6d1f8559f97dfcef8cc9`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Discussion`。接受率低、draft 成本高或状态提交复杂时普通 decode 仍成立。

<!-- claim:SF-2026-ARXIV-2603-10088:start -->**Claim Boundary**：只支持 arXiv:2603.10088v1 §5 Methodology 的机制与 §6.2 Main results 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10088:end -->
<!-- review:SF-2026-ARXIV-2603-10088:end -->
### Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation

<!-- review:SF-2026-ARXIV-2603-10143:start -->
**问题**：`Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation` 检查的是 `AGENT-RAG` 中 知识时效、私有数据和可引用证据要求在生成前建立可追踪的检索路径。 是否会改变现有设计边界。

**旧路径为何合理**：把训练权重或完整上下文视为唯一知识来源，链路短且状态少。

**约束变化与机制**：exact-v1 的 `3.1. Framework Architecture` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-RAG` 负责 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；定位证据为 `arXiv:2603.10143v1 HTML — §3.1. Framework Architecture [facet=method]; https://arxiv.org/html/2603.10143v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10143v1.html; sha256:93e20bc8c615691811d46de714c92bac1e20c60d043b1a7363ae1cc738c40a48`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2. Human Evaluation Setup`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10143v1 HTML — §4.2. Human Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.10143v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10143v1.html; sha256:93e20bc8c615691811d46de714c92bac1e20c60d043b1a7363ae1cc738c40a48`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Limitations`。知识稳定且已被模型可靠覆盖时，直接生成仍具有更低延迟。

<!-- claim:SF-2026-ARXIV-2603-10143:start -->**Claim Boundary**：只支持 arXiv:2603.10143v1 §3.1. Framework Architecture 的机制与 §4.2. Human Evaluation Setup 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10143:end -->
<!-- review:SF-2026-ARXIV-2603-10143:end -->
### Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities

<!-- review:SF-2026-ARXIV-2603-10163:start -->
**问题**：`Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities` 检查的是 `AGENT-MCP` 中 跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。 是否会改变现有设计边界。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：exact-v1 的 `IV-B Challenges and Approach Overview` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.10163v1 HTML — §IV-B Challenges and Approach Overview [facet=method]; https://arxiv.org/html/2603.10163v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10163v1.html; sha256:cb581dfd131fe05e09fb521930bd69cf75ef47afed20197a1fad2ea02dcada51`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V Evaluations`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10163v1 HTML — §V Evaluations [facet=evaluation]; https://arxiv.org/html/2603.10163v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10163v1.html; sha256:cb581dfd131fe05e09fb521930bd69cf75ef47afed20197a1fad2ea02dcada51`。

**Trade-off / failure / coexistence**：限制与反证定位在 `IV-A Limitations of Existing Tools`。固定工具集、单一信任域仍可保留较薄的 adapter。

<!-- claim:SF-2026-ARXIV-2603-10163:start -->**Claim Boundary**：只支持 arXiv:2603.10163v1 §IV-B Challenges and Approach Overview 的机制与 §V Evaluations 的公开 workload；§IV-A Limitations of Existing Tools 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10163:end -->
<!-- review:SF-2026-ARXIV-2603-10163:end -->
### OpenClaw-RL: Train Any Agent Simply by Talking

<!-- review:SF-2026-ARXIV-2603-10165:start -->
**问题**：`OpenClaw-RL: Train Any Agent Simply by Talking` 检查的是 `TRAIN-GRPO` 中 稀疏可验证奖励和 rollout 成本要求更有效地复用同组比较。 是否会改变现有设计边界。

**旧路径为何合理**：每条样本独立更新易实现，但难利用组内相对信号。

**约束变化与机制**：exact-v1 的 `4.3 Combine Binary and OPD Methods` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-GRPO` 负责 prompt、rollout、group advantage 与 on-policy freshness；定位证据为 `arXiv:2603.10165v1 HTML — §4.3 Combine Binary and OPD Methods [facet=method]; https://arxiv.org/html/2603.10165v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10165v1.html; sha256:d41332e35f806913236ca2dd9e55b0c46aaa6ab83661ce156fd5c1aae3606766`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10165v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.10165v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10165v1.html; sha256:d41332e35f806913236ca2dd9e55b0c46aaa6ab83661ce156fd5c1aae3606766`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion`。高质量逐样本监督充足时 SFT/DPO 仍更简单。

<!-- claim:SF-2026-ARXIV-2603-10165:start -->**Claim Boundary**：只支持 arXiv:2603.10165v1 §4.3 Combine Binary and OPD Methods 的机制与 §5 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10165:end -->
<!-- review:SF-2026-ARXIV-2603-10165:end -->
### Hybrid Self-evolving Structured Memory for GUI Agents

<!-- review:SF-2026-ARXIV-2603-10291:start -->
**问题**：`Hybrid Self-evolving Structured Memory for GUI Agents` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `3 Methodology` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.10291v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.10291v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10291v1.html; sha256:f1b527c23c0cfb10216bfdc0fa78aa946f75e703b2686ff8b42d6ff47de5dc77`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Appendix B Additional Qualitative Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10291v1 HTML — §Appendix B Additional Qualitative Results [facet=evaluation]; https://arxiv.org/html/2603.10291v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10291v1.html; sha256:f1b527c23c0cfb10216bfdc0fa78aa946f75e703b2686ff8b42d6ff47de5dc77`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Limitations`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-10291:start -->**Claim Boundary**：只支持 arXiv:2603.10291v1 §3 Methodology 的机制与 §Appendix B Additional Qualitative Results 的公开 workload；§6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10291:end -->
<!-- review:SF-2026-ARXIV-2603-10291:end -->
### Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models

<!-- review:SF-2026-ARXIV-2603-10335:start -->
**问题**：reasoning 长度运行前未知会造成 KV 过度预留、碎片和错误的 thinking budget。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：Fuel Gauge 从隐藏信号预测 CoT 长度，再把预测用于 KV allocation 和推理长度控制。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.10335v1 HTML — §4.4 Fuel Gauge Implementation [facet=method]; https://arxiv.org/html/2603.10335v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10335v1.html; sha256:ff3b6d57b7607d420615663bbd189d961b98dd5baea13908007f00b2140a6239`。

**Evaluation contract 与未证明部分**：多模态 QA 结果只支持所测模型/任务中的预测相关性；不能保证困难分布或新 policy 下稳定。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10335v1 HTML — §B.1 Experimental Results on LMM Intern-S1 [facet=evaluation]; https://arxiv.org/html/2603.10335v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10335v1.html; sha256:ff3b6d57b7607d420615663bbd189d961b98dd5baea13908007f00b2140a6239`。

**Trade-off / failure / coexistence**：预测错误会造成 OOM、频繁扩容或截断；保守动态增长仍是可靠回退。

<!-- claim:SF-2026-ARXIV-2603-10335:start -->**Claim Boundary**：只支持 arXiv:2603.10335v1 §4.4 Fuel Gauge Implementation 的机制与 §B.1 Experimental Results on LMM Intern-S1 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10335:end -->
<!-- review:SF-2026-ARXIV-2603-10335:end -->
### AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU

<!-- review:SF-2026-ARXIV-2603-10342:start -->
**问题**：Agent 请求的 cold prefill、tool-return resume prefill 与 decode 共享单 GPU 时，长恢复 Context 会破坏交互请求 TPOT。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：AgentServe 分类 cold prefill、resume prefill 与 decode；feedback scheduler 根据 TPOT 调整 resume-prefill token budget 和 decode SM reservation，CUDA Green Contexts 隔离资源。

**State / data / control owner**：`INFER-SCHEDULING` 负责 cold/resume prefill 与 decode 资源反馈控制；机制定位于 exact-v1 §III-A–§III-C。

**Evaluation contract 与未证明部分**：§IV 的 consumer-GPU 实验支持受限 workload；多 GPU、生产隔离、tool readiness、trajectory checkpoint 与 workflow state 均未被证明。

**Trade-off / failure / coexistence**：反馈控制会引入 oscillation、SM fragmentation 与单机调参成本；prefill 很短或 GPU 不拥塞时普通 serving engine 更简单。

<!-- claim:SF-2026-ARXIV-2603-10342:start -->**Claim Boundary**：只支持 arXiv:2603.10342v1 §III-A–§III-C 的分类、TPOT feedback、Green Context 隔离与 §IV 单 consumer-GPU 实验；不支持 workflow/tool state。<!-- claim:SF-2026-ARXIV-2603-10342:end -->
<!-- review:SF-2026-ARXIV-2603-10342:end -->
### S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance

<!-- review:SF-2026-ARXIV-2603-10353:start -->
**问题**：稀疏 attention head 的实际工作量不均衡，按 head 数量静态切分会让并行 worker 在 decode 中产生 straggler。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：S-HPLB 先以 calibration 冻结 per-head token budgets，承担 approximation/accuracy 取舍；再按预算做 greedy head-to-device assignment，承担 load balance。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责预算已冻结后的 execution plan 与 head placement；算法预算和放置定位为 exact-v1 §3.2–§3.3。

**Evaluation contract 与未证明部分**：§5.1–§5.4 支持指定模型与稀疏配置；论文没有独立 limitations，分布漂移和互联回退是项目设计推论。

**Trade-off / failure / coexistence**：重分配降低空等，却引入元数据、迁移和额外同步；head 负载均匀时静态并行的控制成本更低。

<!-- claim:SF-2026-ARXIV-2603-10353:start -->**Claim Boundary**：只支持 arXiv:2603.10353v1 §3.2–§3.3 的 calibrated budgets 与 frozen-budget placement，以及 §5.1–§5.4 实验；不支持运行时动态改写预算。<!-- claim:SF-2026-ARXIV-2603-10353:end -->
<!-- review:SF-2026-ARXIV-2603-10353:end -->
### Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design

<!-- review:SF-2026-ARXIV-2603-10379:start -->
**问题**：`Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design` 检查的是 `MODEL-MOE` 中 容量扩大后，激活成本和通信使全参数计算不可持续。 是否会改变现有设计边界。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：exact-v1 的 `B.1 Model Architecture and Training Configuration` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.10379v1 HTML — §B.1 Model Architecture and Training Configuration [facet=method]; https://arxiv.org/html/2603.10379v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10379v1.html; sha256:80f21e65a9250ce34a004a8e6881442bca43a2c2d4ebf37f8b58e131450d6828`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Empirical Validation of the Extended Scaling Law`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10379v1 HTML — §4.2 Empirical Validation of the Extended Scaling Law [facet=evaluation]; https://arxiv.org/html/2603.10379v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10379v1.html; sha256:80f21e65a9250ce34a004a8e6881442bca43a2c2d4ebf37f8b58e131450d6828`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6.2 Limitations`。规模较小、负载难预测或通信昂贵时 dense 仍可能占优。

<!-- claim:SF-2026-ARXIV-2603-10379:start -->**Claim Boundary**：只支持 arXiv:2603.10379v1 §B.1 Model Architecture and Training Configuration 的机制与 §4.2 Empirical Validation of the Extended Scaling Law 的公开 workload；§6.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10379:end -->
<!-- review:SF-2026-ARXIV-2603-10379:end -->
### World2Act: Latent Action Post-Training from World Model Dynamics

<!-- review:SF-2026-ARXIV-2603-10422:start -->
**问题**：`World2Act: Latent Action Post-Training from World Model Dynamics` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `4 Method` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.10422v1 HTML — §4 Method [facet=method]; https://arxiv.org/html/2603.10422v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10422v1.html; sha256:5ae8550f2b8ec703e0ce481fba7829d9a358cc518feec6d5cb9e1e38c231d9c3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10422v1 HTML — §5.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10422v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10422v1.html; sha256:5ae8550f2b8ec703e0ce481fba7829d9a358cc518feec6d5cb9e1e38c231d9c3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `D Failure Cases Analysis`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-10422:start -->**Claim Boundary**：只支持 arXiv:2603.10422v1 §4 Method 的机制与 §5.2 Main Results 的公开 workload；§D Failure Cases Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10422:end -->
<!-- review:SF-2026-ARXIV-2603-10422:end -->
### The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training

<!-- review:SF-2026-ARXIV-2603-10444:start -->
**问题**：`The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training` 检查的是 `TRAIN-PRETRAINING` 中 模型和状态规模增长使带宽、精度与数据选择共同限制训练。 是否会改变现有设计边界。

**旧路径为何合理**：统一精度和静态 optimizer state 使收敛分析最直接。

**约束变化与机制**：exact-v1 的 `5 Mean Bias-Aware Low-Bit Training Method` 把论文方案定位到 optimizer/data state 的精度、更新与恢复边界；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-PRETRAINING` 负责 optimizer/data state 的精度、更新与恢复边界；定位证据为 `arXiv:2603.10444v1 HTML — §5 Mean Bias-Aware Low-Bit Training Method [facet=method]; https://arxiv.org/html/2603.10444v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10444v1.html; sha256:7c909e8a75bb638999783b063eefe925d130f9688b5785b9ba6c11576629c617`。

**Evaluation contract 与未证明部分**：公开验证定位在 `6.2 Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10444v1 HTML — §6.2 Results [facet=evaluation]; https://arxiv.org/html/2603.10444v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10444v1.html; sha256:7c909e8a75bb638999783b063eefe925d130f9688b5785b9ba6c11576629c617`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Conclusion`。规模较小或稳定性优先时保守精度与全量状态仍合理。

<!-- claim:SF-2026-ARXIV-2603-10444:start -->**Claim Boundary**：只支持 arXiv:2603.10444v1 §5 Mean Bias-Aware Low-Bit Training Method 的机制与 §6.2 Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10444:end -->
<!-- review:SF-2026-ARXIV-2603-10444:end -->
### DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference

<!-- review:SF-2026-ARXIV-2603-10469:start -->
**问题**：`DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `III-A Overview` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.10469v1 HTML — §III-A Overview [facet=method]; https://arxiv.org/html/2603.10469v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10469v1.html; sha256:5fb50d9e6e171900dfce6db89e25683a23d49f4100f7febf37dbd853a20072b9`。

**Evaluation contract 与未证明部分**：公开验证定位在 `IV EXPERIMENTS`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10469v1 HTML — §IV EXPERIMENTS [facet=evaluation]; https://arxiv.org/html/2603.10469v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10469v1.html; sha256:5fb50d9e6e171900dfce6db89e25683a23d49f4100f7febf37dbd853a20072b9`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V CONCLUSION`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-10469:start -->**Claim Boundary**：只支持 arXiv:2603.10469v1 §III-A Overview 的机制与 §IV EXPERIMENTS 的公开 workload；§V CONCLUSION 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10469:end -->
<!-- review:SF-2026-ARXIV-2603-10469:end -->
### Coverage-Controlled Preference Mining from Noisy Claim Verification for Evidence-Grounded Generation

<!-- review:SF-2026-ARXIV-2603-10494:start -->
**问题**：`Coverage-Controlled Preference Mining from Noisy Claim Verification for Evidence-Grounded Generation` 检查的是 `TRAIN-RLHF` 中 模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。 是否会改变现有设计边界。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：exact-v1 的 `Method` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.10494v1 PDF — §Method [facet=method]; https://arxiv.org/pdf/2603.10494v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf.txt; sha256:adcff730d907dbf787e1da6ca65d0fcf8fc357220df6c463f13da50b47403af3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Experimental Setup`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10494v1 PDF — §Experimental Setup [facet=evaluation]; https://arxiv.org/pdf/2603.10494v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10494v1.pdf.txt; sha256:adcff730d907dbf787e1da6ca65d0fcf8fc357220df6c463f13da50b47403af3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2603-10494:start -->**Claim Boundary**：只支持 arXiv:2603.10494v1 §Method 的机制与 §Experimental Setup 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10494:end -->
<!-- review:SF-2026-ARXIV-2603-10494:end -->
### IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs

<!-- review:SF-2026-ARXIV-2603-10521:start -->
**问题**：`IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs` 检查的是 `TRAIN-RLHF` 中 模型规模、奖励来源和任务 horizon 改变后，同一配方的排序可能反转。 是否会改变现有设计边界。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：exact-v1 的 `3 Constructing IH-Challenge` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.10521v1 HTML — §3 Constructing IH-Challenge [facet=method]; https://arxiv.org/html/2603.10521v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10521v1.html; sha256:d19c81186ba879aa23607b6bbee9f8601b76bd90e1c1d9b4e2975a9fb9cbc8ff`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.1 Ablation on Training Task Splits`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10521v1 HTML — §5.1 Ablation on Training Task Splits [facet=evaluation]; https://arxiv.org/html/2603.10521v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10521v1.html; sha256:d19c81186ba879aa23607b6bbee9f8601b76bd90e1c1d9b4e2975a9fb9cbc8ff`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion`。反馈稳定、任务窄且分布固定时成熟配方仍可复用。

<!-- claim:SF-2026-ARXIV-2603-10521:start -->**Claim Boundary**：只支持 arXiv:2603.10521v1 §3 Constructing IH-Challenge 的机制与 §5.1 Ablation on Training Task Splits 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10521:end -->
<!-- review:SF-2026-ARXIV-2603-10521:end -->
### CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents

<!-- review:SF-2026-ARXIV-2603-10577:start -->
**问题**：`CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.1. Vision-Language Model–Based Auditors` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.10577v1 HTML — §3.1. Vision-Language Model–Based Auditors [facet=method]; https://arxiv.org/html/2603.10577v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10577v1.html; sha256:9604846d5181c13bff513fd3c98bc51bf84fbacbb5aea112b5cbc03d26eb731f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.2. Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10577v1 HTML — §3.2. Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.10577v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10577v1.html; sha256:9604846d5181c13bff513fd3c98bc51bf84fbacbb5aea112b5cbc03d26eb731f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `5. Discussion and Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-10577:start -->**Claim Boundary**：只支持 arXiv:2603.10577v1 §3.1. Vision-Language Model–Based Auditors 的机制与 §3.2. Benchmarks 的公开 workload；§5. Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10577:end -->
<!-- review:SF-2026-ARXIV-2603-10577:end -->
### Trajectory-Informed Memory Generation for Self-Improving Agent Systems

<!-- review:SF-2026-ARXIV-2603-10600:start -->
**问题**：`Trajectory-Informed Memory Generation for Self-Improving Agent Systems` 检查的是 `AGENT-MEMORY` 中 长时交互、容量和权限约束迫使系统决定何时写、如何索引、何时遗忘。 是否会改变现有设计边界。

**旧路径为何合理**：把全部历史直接放回 context，短会话下最忠实也最少引入派生状态。

**约束变化与机制**：exact-v1 的 `5.1. Memory Taxonomies and Architectures` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MEMORY` 负责 memory 的写入、版本、检索与失效控制权；定位证据为 `arXiv:2603.10600v1 HTML — §5.1. Memory Taxonomies and Architectures [facet=method]; https://arxiv.org/html/2603.10600v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10600v1.html; sha256:ef1376e3fc1dce021991f7cc6dc998afceecd701ab0353e83f9e8ff258a78690`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4. Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10600v1 HTML — §4. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.10600v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10600v1.html; sha256:ef1376e3fc1dce021991f7cc6dc998afceecd701ab0353e83f9e8ff258a78690`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Conclusions`。短会话或不可接受派生状态漂移时仍应回退原始 context。

<!-- claim:SF-2026-ARXIV-2603-10600:start -->**Claim Boundary**：只支持 arXiv:2603.10600v1 §5.1. Memory Taxonomies and Architectures 的机制与 §4. Evaluation 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10600:end -->
<!-- review:SF-2026-ARXIV-2603-10600:end -->
### FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model

<!-- review:SF-2026-ARXIV-2603-10712:start -->
**问题**：`FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `0.A.1 Architecture Overview` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.10712v1 HTML — §0.A.1 Architecture Overview [facet=method]; https://arxiv.org/html/2603.10712v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10712v1.html; sha256:a8904875126ed2d192924038380d27f95aa242e8869da32bf92670f3ae331c6d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Main Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10712v1 HTML — §4.2 Main Results [facet=evaluation]; https://arxiv.org/html/2603.10712v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10712v1.html; sha256:a8904875126ed2d192924038380d27f95aa242e8869da32bf92670f3ae331c6d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `0.A.4 Limitations and Future Work`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-10712:start -->**Claim Boundary**：只支持 arXiv:2603.10712v1 §0.A.1 Architecture Overview 的机制与 §4.2 Main Results 的公开 workload；§0.A.4 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10712:end -->
<!-- review:SF-2026-ARXIV-2603-10712:end -->
### PrefixWall: Mitigating Prefix Caching Side Channels in Shared LLM Systems

<!-- review:SF-2026-ARXIV-2603-10726:start -->
**问题**：`PrefixWall: Mitigating Prefix Caching Side Channels in Shared LLM Systems` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `3. System Design` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.10726v1 HTML — §3. System Design [facet=method]; https://arxiv.org/html/2603.10726v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10726v1.html; sha256:c84d6e9b9ca1832501f4f91aeb12e88d4c6a2c107d48d1a793836521930385ce`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5. Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10726v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.10726v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10726v1.html; sha256:c84d6e9b9ca1832501f4f91aeb12e88d4c6a2c107d48d1a793836521930385ce`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-10726:start -->**Claim Boundary**：只支持 arXiv:2603.10726v1 §3. System Design 的机制与 §5. Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10726:end -->
<!-- review:SF-2026-ARXIV-2603-10726:end -->
### A Grammar of Machine Learning Workflows: Rejecting Data Leakage at Call Time

<!-- review:SF-2026-ARXIV-2603-10742:start -->
**问题**：`A Grammar of Machine Learning Workflows: Rejecting Data Leakage at Call Time` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `4 Design Properties` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.10742v1 HTML — §4 Design Properties [facet=method]; https://arxiv.org/html/2603.10742v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10742v1.html; sha256:a57cd3d2107ffa0e07b437df61bf9d69b7bfc23cb57186395cb750384177cf0f`。

**Evaluation contract 与未证明部分**：公开验证定位在 `8.4 External validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10742v1 HTML — §8.4 External validation [facet=evaluation]; https://arxiv.org/html/2603.10742v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10742v1.html; sha256:a57cd3d2107ffa0e07b437df61bf9d69b7bfc23cb57186395cb750384177cf0f`。

**Trade-off / failure / coexistence**：限制与反证定位在 `9 Conclusion`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-10742:start -->**Claim Boundary**：只支持 arXiv:2603.10742v1 §4 Design Properties 的机制与 §8.4 External validation 的公开 workload；§9 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10742:end -->
<!-- review:SF-2026-ARXIV-2603-10742:end -->
### AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations

<!-- review:SF-2026-ARXIV-2603-10749:start -->
**问题**：`AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `D.2 Attack framework: OpenEvolve` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.10749v1 HTML — §D.2 Attack framework: OpenEvolve [facet=method]; https://arxiv.org/html/2603.10749v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10749v1.html; sha256:5f4b606c2c56b52dee9ff67e949609b4aa321400ae0146c1bd81f5cb2e647459`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5 Experiments`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10749v1 HTML — §5 Experiments [facet=evaluation]; https://arxiv.org/html/2603.10749v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10749v1.html; sha256:5f4b606c2c56b52dee9ff67e949609b4aa321400ae0146c1bd81f5cb2e647459`。

**Trade-off / failure / coexistence**：限制与反证定位在 `3.1 Limitations of Model-level Defenses`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-10749:start -->**Claim Boundary**：只支持 arXiv:2603.10749v1 §D.2 Attack framework: OpenEvolve 的机制与 §5 Experiments 的公开 workload；§3.1 Limitations of Model-level Defenses 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10749:end -->
<!-- review:SF-2026-ARXIV-2603-10749:end -->
### RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems

<!-- review:SF-2026-ARXIV-2603-10765:start -->
**问题**：RAG 若分别评测检索和生成，无法归因端到端时延、召回、grounding 与成本之间的耦合。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：RAGPerf 把 corpus、retriever、reranker、generator、并发与质量判定绑定到同一可复现实验合同，并保留阶段级指标。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；pipeline/workload/profiler 机制定位于 exact-v1 §3.1–§3.5。

**Evaluation contract 与未证明部分**：§5.2–§5.8 覆盖 latency、throughput、accuracy、update、resource、sensitivity 与 measurement overhead；具体排名只对所用数据、模型、硬件和 evaluator 有效。

**Trade-off / failure / coexistence**：端到端合同改善归因，但实验矩阵和数据版本成本更高；单组件开发阶段仍可使用局部 microbenchmark。

<!-- claim:SF-2026-ARXIV-2603-10765:start -->**Claim Boundary**：只支持 arXiv:2603.10765v1 §3.1–§3.5 的 pipeline/workload/profiler 与 §5.2–§5.8 的端到端评测；§2.1 仅是背景。<!-- claim:SF-2026-ARXIV-2603-10765:end -->
<!-- review:SF-2026-ARXIV-2603-10765:end -->
### A Control-Theoretic Foundation for Agentic Systems

<!-- review:SF-2026-ARXIV-2603-10779:start -->
**问题**：`A Control-Theoretic Foundation for Agentic Systems` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `II Problem Formulation and Unified Agentic Control Architecture` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.10779v1 HTML — §II Problem Formulation and Unified Agentic Control Architecture [facet=method]; https://arxiv.org/html/2603.10779v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10779v1.html; sha256:ee40a7c3badac0d3c66cedecd8078e033f9664c394faa7926f8111b79ea7d9ab`。

**Evaluation contract 与未证明部分**：公开验证定位在 `Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.10779v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10779v1.html; sha256:ee40a7c3badac0d3c66cedecd8078e033f9664c394faa7926f8111b79ea7d9ab`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V-F Discussion and Limitations of the Linear Setting`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-10779:start -->**Claim Boundary**：只支持 arXiv:2603.10779v1 §II Problem Formulation and Unified Agentic Control Architecture 的机制与 §Evaluation 的公开 workload；§V-F Discussion and Limitations of the Linear Setting 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10779:end -->
<!-- review:SF-2026-ARXIV-2603-10779:end -->
### LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation

<!-- review:SF-2026-ARXIV-2603-10899:start -->
**问题**：`LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation` 检查的是 `INFER-KV-CACHE` 中 长上下文、多会话和异构层级使 KV 容量、带宽及身份成为主瓶颈。 是否会改变现有设计边界。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：exact-v1 的 `3 Proposed Method: LookaheadKV` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.10899v1 HTML — §3 Proposed Method: LookaheadKV [facet=method]; https://arxiv.org/html/2603.10899v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10899v1.html; sha256:1b28d1872dbab87bed2a2fe997bb2b9481c2f865129184e1b50e595a3261a630`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.2 Evaluation Setup`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.10899v1 HTML — §4.2 Evaluation Setup [facet=evaluation]; https://arxiv.org/html/2603.10899v1; papers/2026/03/_sources/daily-20260312/exact-v1-bodies/2603.10899v1.html; sha256:1b28d1872dbab87bed2a2fe997bb2b9481c2f865129184e1b50e595a3261a630`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7 Conclusion and Limitation`。小 batch、短上下文或严格 exactness 场景仍宜保留完整 KV。

<!-- claim:SF-2026-ARXIV-2603-10899:start -->**Claim Boundary**：只支持 arXiv:2603.10899v1 §3 Proposed Method: LookaheadKV 的机制与 §4.2 Evaluation Setup 的公开 workload；§7 Conclusion and Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-10899:end -->
<!-- review:SF-2026-ARXIV-2603-10899:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-10342 | score_7_9;potential_books_delta | selected | DA-20260312-17 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260312-17 |
| SF-2026-ARXIV-2603-10353 | score_7_9;potential_books_delta | selected | DA-20260312-18 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260312-18 |
| SF-2026-ARXIV-2603-10765 | score_7_9;potential_books_delta | selected | DA-20260312-31 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260312-31 |

<!-- analysis:DA-20260312-17:start -->
### AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU

agent serving 在消费级单 GPU 上交替执行模型推理、工具等待和状态处理，单纯提高 batch 会被阶段阻塞抵消。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：AgentServe 将 agent trajectory 切为可调度阶段，并依据显存、tool readiness 与请求依赖共同安排模型执行和状态换入。 其公开验证边界为：作者在其 agent workload 与消费级 GPU 上报告吞吐/延迟，支持受限资源下的算法-系统协同；多 GPU 和生产隔离未被证明。 新增代价与回退条件为：阶段化可回收等待空隙，但会增加 trajectory checkpoint 与恢复成本；工具少、模型阶段占主导时普通 serving engine 更简单。
<!-- analysis:DA-20260312-17:end -->
<!-- analysis:DA-20260312-18:start -->
### S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance

稀疏 attention head 的实际工作量不均衡，按 head 数量静态切分会让并行 worker 在 decode 中产生 straggler。 旧路径在其原约束下仍合理：完整、逐 token 保存 KV，换取语义透明和最低重算风险。 本 family 的设计变化是：S-HPLB 根据活跃 head 与 token workload 重新分配 head parallel work，并把稀疏模式纳入通信和放置决策。 其公开验证边界为：公开 serving 实验支持指定模型与稀疏配置中的负载均衡收益；动态稀疏漂移和不同互连下的开销仍未覆盖。 新增代价与回退条件为：重分配降低空等，却引入元数据、迁移和额外同步；head 负载均匀时静态并行的控制成本更低。
<!-- analysis:DA-20260312-18:end -->
<!-- analysis:DA-20260312-31:start -->
### RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems

RAG 若分别评测检索和生成，无法归因端到端时延、召回、grounding 与成本之间的耦合。 旧路径在其原约束下仍合理：单一离线分数便于比较版本。 本 family 的设计变化是：RAGPerf 把 corpus、retriever、reranker、generator、并发与质量判定绑定到同一可复现实验合同，并保留阶段级指标。 其公开验证边界为：框架证明这些组件可在统一 workload 下比较；具体排名只对所用数据、模型、硬件和 evaluator 有效。 新增代价与回退条件为：端到端合同改善归因，但实验矩阵和数据版本成本更高；单组件开发阶段仍可使用局部 microbenchmark。
<!-- analysis:DA-20260312-31:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-09983 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#连续-edge-inference-需要跨窗口携带-violation-risk-budget (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-09983 | delta:SF-2026-ARXIV-2603-09983 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-09983 |
| SF-2026-ARXIV-2603-10030 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#流式输入把-cache-变成可续租的-session-state (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10030 | delta:SF-2026-ARXIV-2603-10030 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10030 |
| SF-2026-ARXIV-2603-10031 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10031 | delta:SF-2026-ARXIV-2603-10031 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10031 |
| SF-2026-ARXIV-2603-10032 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10032 | delta:SF-2026-ARXIV-2603-10032 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10032 |
| SF-2026-ARXIV-2603-10044 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10044 | delta:SF-2026-ARXIV-2603-10044 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10044 |
| SF-2026-ARXIV-2603-10057 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量：评估声明必须绑定完整对象 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10057 | delta:SF-2026-ARXIV-2603-10057 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10057 |
| SF-2026-ARXIV-2603-10060 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#interface-granularity：不是-tool-越多越有能力 (section Ch-owner) | books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent); books/part-07-agent/79-planning.md#第79章-planning (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10060 | delta:SF-2026-ARXIV-2603-10060 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10060 |
| SF-2026-ARXIV-2603-10062 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10062 | delta:SF-2026-ARXIV-2603-10062 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10062 |
| SF-2026-ARXIV-2603-10085 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10085 | delta:SF-2026-ARXIV-2603-10085 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10085 |
| SF-2026-ARXIV-2603-10087 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10087 | delta:SF-2026-ARXIV-2603-10087 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10087 |
| SF-2026-ARXIV-2603-10088 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#drafter-的演进：从辅助模型到受治理的-serving-artifact (section Ch-owner) | books/part-05-inference-system/47-pagedattention.md#第47章-pagedattention (section Ch-adjacent); books/part-05-inference-system/49-tensorrt-llm.md#第49章-高性能-gpu-推理执行：以-tensorrt-llm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10088 | delta:SF-2026-ARXIV-2603-10088 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10088 |
| SF-2026-ARXIV-2603-10143 | AGENT-RAG | books/part-07-agent/76-rag.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/75-context.md#第75章-context (section Ch-adjacent); books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10143 | delta:SF-2026-ARXIV-2603-10143 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10143 |
| SF-2026-ARXIV-2603-10163 | AGENT-MCP | books/part-07-agent/83-mcp.md#tool-catalog-扩大后，discovery-与-execution-必须分离 (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10163 | delta:SF-2026-ARXIV-2603-10163 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10163 |
| SF-2026-ARXIV-2603-10165 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#多阶段交互需要-phase-specific-credit，而不是一个终局标量 (section Ch-owner) | books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent); books/part-04-training-system/34-dpo.md#第34章-dpo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10165 | delta:SF-2026-ARXIV-2603-10165 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10165 |
| SF-2026-ARXIV-2603-10291 | AGENT-MEMORY | books/part-07-agent/77-memory.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10291 | delta:SF-2026-ARXIV-2603-10291 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10291 |
| SF-2026-ARXIV-2603-10335 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10335 | delta:SF-2026-ARXIV-2603-10335 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10335 |
| SF-2026-ARXIV-2603-10342 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#exclusive-batching-的-phase-switch-是-workload-dependent-state (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10342 | delta:SF-2026-ARXIV-2603-10342 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-10342 |
| SF-2026-ARXIV-2603-10353 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#execution-plan-先拥有-state再选择-kernel (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-vllm (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10353 | delta:SF-2026-ARXIV-2603-10353 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-10353 |
| SF-2026-ARXIV-2603-10379 | MODEL-MOE | books/part-02-model/21-moe.md#从参数化-router-到带检索记忆的-router (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10379 | delta:SF-2026-ARXIV-2603-10379 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10379 |
| SF-2026-ARXIV-2603-10422 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10422 | delta:SF-2026-ARXIV-2603-10422 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10422 |
| SF-2026-ARXIV-2603-10444 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#precision-policy-应沿误差传播路径分区 (section Ch-owner) | books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent); books/part-04-training-system/29-sft.md#第29章-sft (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10444 | delta:SF-2026-ARXIV-2603-10444 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10444 |
| SF-2026-ARXIV-2603-10469 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10469 | delta:SF-2026-ARXIV-2603-10469 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10469 |
| SF-2026-ARXIV-2603-10494 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10494 | delta:SF-2026-ARXIV-2603-10494 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10494 |
| SF-2026-ARXIV-2603-10521 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10521 | delta:SF-2026-ARXIV-2603-10521 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10521 |
| SF-2026-ARXIV-2603-10577 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10577 | delta:SF-2026-ARXIV-2603-10577 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10577 |
| SF-2026-ARXIV-2603-10600 | AGENT-MEMORY | books/part-07-agent/77-memory.md#context-与-memory-的状态边界 (section Ch-owner) | books/part-07-agent/76-rag.md#第76章-rag (section Ch-adjacent); books/part-07-agent/78-tool-calling.md#第78章-tool-calling (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10600 | delta:SF-2026-ARXIV-2603-10600 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10600 |
| SF-2026-ARXIV-2603-10712 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#vla-policy (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10712 | delta:SF-2026-ARXIV-2603-10712 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10712 |
| SF-2026-ARXIV-2603-10726 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#conversation-continuation-必须先验证-grounding-state (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10726 | delta:SF-2026-ARXIV-2603-10726 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10726 |
| SF-2026-ARXIV-2603-10742 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10742 | delta:SF-2026-ARXIV-2603-10742 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10742 |
| SF-2026-ARXIV-2603-10749 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#多-agent-cascade-需要跨-channel-的-influence-graph (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10749 | delta:SF-2026-ARXIV-2603-10749 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10749 |
| SF-2026-ARXIV-2603-10765 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#continual-update-需要同步推进-calibration-state (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10765 | delta:SF-2026-ARXIV-2603-10765 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-10765 |
| SF-2026-ARXIV-2603-10779 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10779 | delta:SF-2026-ARXIV-2603-10779 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10779 |
| SF-2026-ARXIV-2603-10899 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#从昂贵-oracle-到-learned-eviction-policy (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-10899 | delta:SF-2026-ARXIV-2603-10899 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-10899 |

<!-- books-review:SF-2026-ARXIV-2603-09983:start -->
### MoE-SpAc: Efficient MoE Inference Based on Speculative Activation Utility in Heterogeneous Edge Scenarios — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-09983:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：逐请求 admission 在任务相互独立、设备容量稳定且 deadline 只属于当前请求时足够。Continuous edge inference 往往由 视频帧、传感器流或周期任务持续到达；一次延迟会压缩后续窗口，burst history 与设备状态又让风险随时间演化。只看 当前 queue length 或平均 latency，会把“本轮可执行”误当成“未来仍能守住违约上限”。<!-- existing:SF-2026-ARXIV-2603-09983:end -->

<!-- delta:SF-2026-ARXIV-2603-09983:start -->新证据差异：MoE-SpAc 把 draft lookahead 当 expert demand sensor，联合执行预取、淘汰与异构 workload placement。<!-- delta:SF-2026-ARXIV-2603-09983:end -->

边界：只支持 arXiv:2603.09983v1 §2.2 Mixture-of-Experts Architecture 的机制与 §4.4 Ablation Study 的公开 workload；§Appendix H Future Work and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-09983:end -->
<!-- books-review:SF-2026-ARXIV-2603-10030:start -->
### The DMA Streaming Framework: Kernel-Level Buffer Orchestration for High-Performance AI Data Paths — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10030:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：多轮 Tool loop 把同一问题扩展到离散 request 之间：每轮重算完整 transcript 最容易保证状态一致；当会话变长、多个 Agent 交错推进时，重复 prefix 又会反复支付 Prefill。一个受限的 stateful 分支让 sequence owner 跨轮持有 persistent KV，只摄取本轮新增的 \(\Delta_t\) token，并让 radix prefix cache 在 identity-compatible 的会话之间共享不可变前缀。Sequence pool 与 scheduler 负责 admission、lease、eviction 和 invalidation；prompt-lookup speculative decoding 只是可选的下游加速器，streaming validator 也只验证结构化输出，二者都不拥有 cache identity 的真值。<!-- existing:SF-2026-ARXIV-2603-10030:end -->

<!-- delta:SF-2026-ARXIV-2603-10030:start -->新证据差异：dmaplane 以 kernel UAPI 管理 NUMA allocation、dma-buf、RDMA credit、GPU BAR pinning 与 completion-safe lifecycle。<!-- delta:SF-2026-ARXIV-2603-10030:end -->

边界：只支持 arXiv:2603.10030v1 §Appendix A Methodology 的机制与 §6. Evaluation and Discussion 的公开 workload；§6. Evaluation and Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10030:end -->
<!-- books-review:SF-2026-ARXIV-2603-10031:start -->
### Architecture-Aware LLM Inference Optimization on AMD Instinct GPUs: A Comprehensive Benchmark and Deployment Study — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10031:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-10031:end -->

<!-- delta:SF-2026-ARXIV-2603-10031:start -->新证据差异：exact-v1 的 `5 Experimental Methodology` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10031:end -->

边界：只支持 arXiv:2603.10031v1 §5 Experimental Methodology 的机制与 §6 Results and Analysis 的公开 workload；§7.5 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10031:end -->
<!-- books-review:SF-2026-ARXIV-2603-10032:start -->
### HTM-EAR: Importance-Preserving Tiered Memory with Hybrid Routing under Saturation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10032:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2603-10032:end -->

<!-- delta:SF-2026-ARXIV-2603-10032:start -->新证据差异：exact-v1 的 `2 System Architecture` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10032:end -->

边界：只支持 arXiv:2603.10032v1 §2 System Architecture 的机制与 §5 Ablation Study under Saturation (Scenario B) 的公开 workload；§9 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10032:end -->
<!-- books-review:SF-2026-ARXIV-2603-10044:start -->
### Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10044:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-10044:end -->

<!-- delta:SF-2026-ARXIV-2603-10044:start -->新证据差异：exact-v1 的 `2.1 Safety Evaluation Methodology` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10044:end -->

边界：只支持 arXiv:2603.10044v1 §2.1 Safety Evaluation Methodology 的机制与 §2.1 Safety Evaluation Methodology 的公开 workload；§7.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10044:end -->
<!-- books-review:SF-2026-ARXIV-2603-10057:start -->
### SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10057:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或 architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision 纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一 对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。<!-- existing:SF-2026-ARXIV-2603-10057:end -->

<!-- delta:SF-2026-ARXIV-2603-10057:start -->新证据差异：exact-v1 的 `3 METHODOLOGIES` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10057:end -->

边界：只支持 arXiv:2603.10057v1 §3 METHODOLOGIES 的机制与 §Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10057:end -->
<!-- books-review:SF-2026-ARXIV-2603-10060:start -->
### Tool Receipts, Not Zero-Knowledge Proofs: Practical Hallucination Detection for AI Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10060:start -->已读 owner `books/part-07-agent/78-tool-calling.md` 与相邻章节。现有命题：这是并存的 interface branches，不是单向升级。平台应根据 task risk、operation coverage、request volume 与 auditability 选择最窄且足够表达的 surface，并保持 canonical action、authorization 和 effect identity 不变。 Terminal Agents 的受限实验说明部分 enterprise gap 来自 interface granularity，不证明 shell 比 MCP、domain API 或 browser 普遍更好；benchmark sandbox、模型、tool catalog 与成本条件变化都会改变结论。<!-- existing:SF-2026-ARXIV-2603-10060:end -->

<!-- delta:SF-2026-ARXIV-2603-10060:start -->新证据差异：exact-v1 的 `4.3 Injection Methodology` 把论文方案定位到 tool identity、argument validation、authorization、receipt 与 side-effect commit；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10060:end -->

边界：只支持 arXiv:2603.10060v1 §4.3 Injection Methodology 的机制与 §5.2 Main Results 的公开 workload；§6.4 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10060:end -->
<!-- books-review:SF-2026-ARXIV-2603-10062:start -->
### Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10062:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-10062:end -->

<!-- delta:SF-2026-ARXIV-2603-10062:start -->新证据差异：exact-v1 的 `4. An Architecture-Inspired Memory Hierarchy` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10062:end -->

边界：只支持 arXiv:2603.10062v1 §4. An Architecture-Inspired Memory Hierarchy 的机制与 §Evaluation 的公开 workload；§7. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10062:end -->
<!-- books-review:SF-2026-ARXIV-2603-10085:start -->
### KernelSkill: A Multi-Agent Framework for GPU Kernel Optimization — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10085:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。<!-- existing:SF-2026-ARXIV-2603-10085:end -->

<!-- delta:SF-2026-ARXIV-2603-10085:start -->新证据差异：exact-v1 的 `4.1.1 Framework Overview` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10085:end -->

边界：只支持 arXiv:2603.10085v1 §4.1.1 Framework Overview 的机制与 §5.4 Experimental Results and Analysis 的公开 workload；§5.5 Ablation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10085:end -->
<!-- books-review:SF-2026-ARXIV-2603-10087:start -->
### Pooling Engram Conditional Memory in Large Language Models using CXL — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10087:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-10087:end -->

<!-- delta:SF-2026-ARXIV-2603-10087:start -->新证据差异：exact-v1 的 `4.3. Implementation in Inference Framework` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10087:end -->

边界：只支持 arXiv:2603.10087v1 §4.3. Implementation in Inference Framework 的机制与 §5.4. Cost Analysis 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10087:end -->
<!-- books-review:SF-2026-ARXIV-2603-10088:start -->
### ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10088:start -->已读 owner `books/part-05-inference-system/48-speculative-decoding.md` 与相邻章节。现有命题：Draft path 也可以从 autoregressive model 演进为并行 refinement model。Diffusion/block draft 能一次提出多个 provisional tokens，减少 draft critical path；若再注入 target hidden features，可提高候选与目标分布的匹配。它没有改变 correctness owner：target 仍必须执行 exact verification，拒绝后只提交已验证 prefix。<!-- existing:SF-2026-ARXIV-2603-10088:end -->

<!-- delta:SF-2026-ARXIV-2603-10088:start -->新证据差异：exact-v1 的 `5 Methodology` 把论文方案定位到 proposal、验证、接受/回滚与缓存提交状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10088:end -->

边界：只支持 arXiv:2603.10088v1 §5 Methodology 的机制与 §6.2 Main results 的公开 workload；§7 Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10088:end -->
<!-- books-review:SF-2026-ARXIV-2603-10143:start -->
### Reason and Verify: A Framework for Faithful Retrieval-Augmented Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10143:start -->已读 owner `books/part-07-agent/76-rag.md` 与相邻章节。现有命题：本章的核心判断是：**RAG 用运行时检索把非参数化 evidence 注入 Context，使知识可更新和可追溯；可靠性取决于 ingestion、retrieval、packing、generation 与 evaluation 的整条链，而非某一个 embedding model。**<!-- existing:SF-2026-ARXIV-2603-10143:end -->

<!-- delta:SF-2026-ARXIV-2603-10143:start -->新证据差异：exact-v1 的 `3.1. Framework Architecture` 把论文方案定位到 query、corpus version、retrieval/rerank 与 evidence-to-claim lineage；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10143:end -->

边界：只支持 arXiv:2603.10143v1 §3.1. Framework Architecture 的机制与 §4.2. Human Evaluation Setup 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10143:end -->
<!-- books-review:SF-2026-ARXIV-2603-10163:start -->
### Compatibility at a Cost: Systematic Discovery and Exploitation of MCP Clause-Compliance Vulnerabilities — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10163:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：全量注入在工具少、context 富余或 discovery 服务不可用时仍是清晰 fallback。Selective discovery 用额外检索 latency、index lifecycle、embedding dependency 与 observability 换 context 容量；生产 claim 必须绑定 catalog size、query set、top-k、latency 分布、fallback rate 与 client revisions，不能把单个企业目录的 token reduction 写成 MCP 协议常数。<!-- existing:SF-2026-ARXIV-2603-10163:end -->

<!-- delta:SF-2026-ARXIV-2603-10163:start -->新证据差异：exact-v1 的 `IV-B Challenges and Approach Overview` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10163:end -->

边界：只支持 arXiv:2603.10163v1 §IV-B Challenges and Approach Overview 的机制与 §V Evaluations 的公开 workload；§IV-A Limitations of Existing Tools 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10163:end -->
<!-- books-review:SF-2026-ARXIV-2603-10165:start -->
### OpenClaw-RL: Train Any Agent Simply by Talking — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10165:start -->已读 owner `books/part-04-training-system/33-grpo.md` 与相邻章节。现有命题：这只在状态足够可观测、schema 可版本化且 transition error 可检查时成立。错误 snapshot 会让整个 rollout 在看似紧凑的状态上稳定偏航；部分可观察、随机或不可逆环境仍需 belief/history、reconciliation、approval 和 rollback。单篇 text-game 实验不能证明显式 Markov state 普遍提高真实 Agent 能力。<!-- existing:SF-2026-ARXIV-2603-10165:end -->

<!-- delta:SF-2026-ARXIV-2603-10165:start -->新证据差异：exact-v1 的 `4.3 Combine Binary and OPD Methods` 把论文方案定位到 prompt、rollout、group advantage 与 on-policy freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10165:end -->

边界：只支持 arXiv:2603.10165v1 §4.3 Combine Binary and OPD Methods 的机制与 §5 Experiments 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10165:end -->
<!-- books-review:SF-2026-ARXIV-2603-10291:start -->
### Hybrid Self-evolving Structured Memory for GUI Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10291:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2603-10291:end -->

<!-- delta:SF-2026-ARXIV-2603-10291:start -->新证据差异：exact-v1 的 `3 Methodology` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10291:end -->

边界：只支持 arXiv:2603.10291v1 §3 Methodology 的机制与 §Appendix B Additional Qualitative Results 的公开 workload；§6 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10291:end -->
<!-- books-review:SF-2026-ARXIV-2603-10335:start -->
### Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10335:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：但 fully-online、对抗性 arrival 且输出长度未知时，不存在 workload-independent 的万能最优策略。 Shortest-estimated-work 可以降低平均 flow time，却会饿死长请求；更保守的 future-feasibility check 减少 memory dead-end，却降低 utilization；reserve 抵抗预测误差，也直接减少可售 capacity。论文中的 单 worker、non-preemptive 算法因此只提供 impossibility boundary 与设计原则，不是 vLLM/SGLang 的 生产处方。实际系统还必须把 prefix reuse、chunked prefill、recompute/preemption、tenant fairness、 tail SLO 和预测校准放进同一 workload contract。<!-- existing:SF-2026-ARXIV-2603-10335:end -->

<!-- delta:SF-2026-ARXIV-2603-10335:start -->新证据差异：Fuel Gauge 从隐藏信号预测 CoT 长度，再把预测用于 KV allocation 和推理长度控制。<!-- delta:SF-2026-ARXIV-2603-10335:end -->

边界：只支持 arXiv:2603.10335v1 §4.4 Fuel Gauge Implementation 的机制与 §B.1 Experimental Results on LMM Intern-S1 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10335:end -->
<!-- books-review:SF-2026-ARXIV-2603-10342:start -->
### AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10342:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：Mixed batching 在 Prefill 与 Decode 可以高效共批、硬件带宽充足时减少空隙，是现代 serving 的合理默认；若 engine 只能 exclusive batching，或 Prefill–Decode interference 抬高 mixed step 的边际成本，固定“优先 Decode”或“空出一个 slot 就 Prefill”都会忽略 phase switching 的真实代价。此时调度对象不仅是等待请求，还包括当前 busy/idle slots、保留的 KV、输入长度分布、输出 completion hazard、GPU bandwidth、model size 与 memory headroom。<!-- existing:SF-2026-ARXIV-2603-10342:end -->

<!-- delta:SF-2026-ARXIV-2603-10342:start -->新证据差异：AgentServe 区分 cold prefill、resume prefill 与 decode，用 TPOT feedback 调整 resume-prefill token budget 与 decode SM reservation，并以 Green Contexts 隔离资源。<!-- delta:SF-2026-ARXIV-2603-10342:end -->

边界：只支持 arXiv:2603.10342v1 §III-A–§III-C 与 §IV 的单 consumer-GPU 评测，不支持 tool readiness、trajectory checkpoint 或 workflow state。已写回，等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-10342:end -->
<!-- books-review:SF-2026-ARXIV-2603-10353:start -->
### S-HPLB: Efficient LLM Attention Serving via Sparsity-Aware Head Parallelism Load Balance — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10353:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：KV Cache 是 LLM Serving 的核心状态契约：它以显存换取历史 computation reuse，让 Decode 只推进新位置。容量不足时先保护 prompt/modality 等结构边界，再在剩余预算中选择；换成 linear attention 后，状态形态与 IO pipeline 也必须重新定义，不能继续沿用 token-KV 的身份假设。<!-- existing:SF-2026-ARXIV-2603-10353:end -->

<!-- delta:SF-2026-ARXIV-2603-10353:start -->新证据差异：S-HPLB 根据活跃 head 与 token workload 重新分配 head parallel work，并把稀疏模式纳入通信和放置决策。<!-- delta:SF-2026-ARXIV-2603-10353:end -->

边界：只支持 arXiv:2603.10353v1 §3.2–§3.3 与 §5.1–§5.4；动态漂移、互连和 fallback 属于项目推论。写回已完成，等待非作者 post-write 复核。
<!-- books-review:SF-2026-ARXIV-2603-10353:end -->
<!-- books-review:SF-2026-ARXIV-2603-10379:start -->
### Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10379:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：当 `E` 很大而 `k` 仍很小时，平衡问题还会从平均 loss 扩展到 executable shape。 若每个 expert 的 token count 在 critical path 上持续变化，runtime 可能需要动态 allocation、host synchronization 或大量 padding；这些成本会抵消稀疏计算收益。 因此有些模型会在训练时把 router balancing 与静态 dispatch shape 联合设计。<!-- existing:SF-2026-ARXIV-2603-10379:end -->

<!-- delta:SF-2026-ARXIV-2603-10379:start -->新证据差异：exact-v1 的 `B.1 Model Architecture and Training Configuration` 把论文方案定位到 expert 选择、capacity、placement 与通信；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10379:end -->

边界：只支持 arXiv:2603.10379v1 §B.1 Model Architecture and Training Configuration 的机制与 §4.2 Empirical Validation of the Extended Scaling Law 的公开 workload；§6.2 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10379:end -->
<!-- books-review:SF-2026-ARXIV-2603-10422:start -->
### World2Act: Latent Action Post-Training from World Model Dynamics — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10422:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-10422:end -->

<!-- delta:SF-2026-ARXIV-2603-10422:start -->新证据差异：exact-v1 的 `4 Method` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10422:end -->

边界：只支持 arXiv:2603.10422v1 §4 Method 的机制与 §5.2 Main Results 的公开 workload；§D Failure Cases Analysis 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10422:end -->
<!-- books-review:SF-2026-ARXIV-2603-10444:start -->
### The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10444:start -->已读 owner `books/part-04-training-system/28-pretraining.md` 与相邻章节。现有命题：它通过改变 quantizer 所见 distribution 保存 long-tail variation，却新增 mean reduction、subtraction、额外 cross terms 与融合要求；microbatch/sequence composition 改变时，mean 本身也是漂移状态。Averis 的受限实验 支持这种 source-aware split 在其 FP4 training graph 中缩小数值差距，不证明 column mean 是所有层、模型与训练 阶段的 dominant error，也没有公开硬件吞吐合同。Vanilla FP4 在偏置弱时更简单，FP8/BF16 在同步成本、 实现成熟度或失败代价优先时继续成立；是否采用分解必须同时看 convergence 与 end-to-end step time。<!-- existing:SF-2026-ARXIV-2603-10444:end -->

<!-- delta:SF-2026-ARXIV-2603-10444:start -->新证据差异：exact-v1 的 `5 Mean Bias-Aware Low-Bit Training Method` 把论文方案定位到 optimizer/data state 的精度、更新与恢复边界；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10444:end -->

边界：只支持 arXiv:2603.10444v1 §5 Mean Bias-Aware Low-Bit Training Method 的机制与 §6.2 Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10444:end -->
<!-- books-review:SF-2026-ARXIV-2603-10469:start -->
### DepthCache: Depth-Guided Training-Free Visual Token Merging for Vision-Language-Action Model Inference — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10469:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-10469:end -->

<!-- delta:SF-2026-ARXIV-2603-10469:start -->新证据差异：exact-v1 的 `III-A Overview` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10469:end -->

边界：只支持 arXiv:2603.10469v1 §III-A Overview 的机制与 §IV EXPERIMENTS 的公开 workload；§V CONCLUSION 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10469:end -->
<!-- books-review:SF-2026-ARXIV-2603-10494:start -->
### Coverage-Controlled Preference Mining from Noisy Claim Verification for Evidence-Grounded Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10494:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-10494:end -->

<!-- delta:SF-2026-ARXIV-2603-10494:start -->新证据差异：exact-v1 的 `Method` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10494:end -->

边界：只支持 arXiv:2603.10494v1 §Method 的机制与 §Experimental Setup 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10494:end -->
<!-- books-review:SF-2026-ARXIV-2603-10521:start -->
### IH-Challenge: A Training Dataset to Improve Instruction Hierarchy on Frontier LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10521:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-10521:end -->

<!-- delta:SF-2026-ARXIV-2603-10521:start -->新证据差异：exact-v1 的 `3 Constructing IH-Challenge` 把论文方案定位到 rollout、reward、policy/reference 与更新 freshness；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10521:end -->

边界：只支持 arXiv:2603.10521v1 §3 Constructing IH-Challenge 的机制与 §5.1 Ablation on Training Task Splits 的公开 workload；§7 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10521:end -->
<!-- books-review:SF-2026-ARXIV-2603-10577:start -->
### CUAAudit: Meta-Evaluation of Vision-Language Models as Auditors of Autonomous Computer-Use Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10577:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-10577:end -->

<!-- delta:SF-2026-ARXIV-2603-10577:start -->新证据差异：exact-v1 的 `3.1. Vision-Language Model–Based Auditors` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10577:end -->

边界：只支持 arXiv:2603.10577v1 §3.1. Vision-Language Model–Based Auditors 的机制与 §3.2. Benchmarks 的公开 workload；§5. Discussion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10577:end -->
<!-- books-review:SF-2026-ARXIV-2603-10600:start -->
### Trajectory-Informed Memory Generation for Self-Improving Agent Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10600:start -->已读 owner `books/part-07-agent/77-memory.md` 与相邻章节。现有命题：模型架构中的 test-time neural memory 也不属于本章的 Agent Memory。前者在 forward 期间按 surprise/gradient 更新模型内部参数化 state，owner 是 sequence model，主要目标是压缩和利用 长输入；后者由平台跨调用持久化，必须具备 provenance、authorization、correction 与 deletion。 二者共享“write、retain、forget”的 `Principle Reuse`，但 truth authority 与生命周期不同。 第 22 章讨论 Titans/MIRAS 这类模型内部路线，本章只处理外部 durable state。<!-- existing:SF-2026-ARXIV-2603-10600:end -->

<!-- delta:SF-2026-ARXIV-2603-10600:start -->新证据差异：exact-v1 的 `5.1. Memory Taxonomies and Architectures` 把论文方案定位到 memory 的写入、版本、检索与失效控制权；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10600:end -->

边界：只支持 arXiv:2603.10600v1 §5.1. Memory Taxonomies and Architectures 的机制与 §4. Evaluation 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10600:end -->
<!-- books-review:SF-2026-ARXIV-2603-10712:start -->
### FutureVLA: Joint Visuomotor Prediction for Vision-Language-Action Model — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10712:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：联合模型减少语义 handoff，不等于消除物理接口。action normalization、joint limits、coordinate transform、control frequency 与 actuator dynamics 仍在模型外定义。<!-- existing:SF-2026-ARXIV-2603-10712:end -->

<!-- delta:SF-2026-ARXIV-2603-10712:start -->新证据差异：exact-v1 的 `0.A.1 Architecture Overview` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10712:end -->

边界：只支持 arXiv:2603.10712v1 §0.A.1 Architecture Overview 的机制与 §4.2 Main Results 的公开 workload；§0.A.4 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10712:end -->
<!-- books-review:SF-2026-ARXIV-2603-10726:start -->
### PrefixWall: Mitigating Prefix Caching Side Channels in Shared LLM Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10726:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实 系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、 simulation、canary 与 incident evidence 因而继续存在。<!-- existing:SF-2026-ARXIV-2603-10726:end -->

<!-- delta:SF-2026-ARXIV-2603-10726:start -->新证据差异：exact-v1 的 `3. System Design` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10726:end -->

边界：只支持 arXiv:2603.10726v1 §3. System Design 的机制与 §5. Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10726:end -->
<!-- books-review:SF-2026-ARXIV-2603-10742:start -->
### A Grammar of Machine Learning Workflows: Rejecting Data Leakage at Call Time — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10742:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-10742:end -->

<!-- delta:SF-2026-ARXIV-2603-10742:start -->新证据差异：exact-v1 的 `4 Design Properties` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10742:end -->

边界：只支持 arXiv:2603.10742v1 §4 Design Properties 的机制与 §8.4 External validation 的公开 workload；§9 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10742:end -->
<!-- books-review:SF-2026-ARXIV-2603-10749:start -->
### AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10749:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。<!-- existing:SF-2026-ARXIV-2603-10749:end -->

<!-- delta:SF-2026-ARXIV-2603-10749:start -->新证据差异：exact-v1 的 `D.2 Attack framework: OpenEvolve` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10749:end -->

边界：只支持 arXiv:2603.10749v1 §D.2 Attack framework: OpenEvolve 的机制与 §5 Experiments 的公开 workload；§3.1 Limitations of Model-level Defenses 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10749:end -->
<!-- books-review:SF-2026-ARXIV-2603-10765:start -->
### RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10765:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。<!-- existing:SF-2026-ARXIV-2603-10765:end -->

<!-- delta:SF-2026-ARXIV-2603-10765:start -->新证据差异：RAGPerf 把 corpus、retriever、reranker、generator、并发与质量判定绑定到同一可复现实验合同，并保留阶段级指标。<!-- delta:SF-2026-ARXIV-2603-10765:end -->

边界：只支持 arXiv:2603.10765v1 §3.1–§3.5 的 pipeline/workload/profiler 设计与 §5.2–§5.8 的端到端评测；§2.1 仅为背景，§7 之外不外推。已写回，等待非作者复核。
<!-- books-review:SF-2026-ARXIV-2603-10765:end -->
<!-- books-review:SF-2026-ARXIV-2603-10779:start -->
### A Control-Theoretic Foundation for Agentic Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10779:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-10779:end -->

<!-- delta:SF-2026-ARXIV-2603-10779:start -->新证据差异：exact-v1 的 `II Problem Formulation and Unified Agentic Control Architecture` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10779:end -->

边界：只支持 arXiv:2603.10779v1 §II Problem Formulation and Unified Agentic Control Architecture 的机制与 §Evaluation 的公开 workload；§V-F Discussion and Limitations of the Linear Setting 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10779:end -->
<!-- books-review:SF-2026-ARXIV-2603-10899:start -->
### LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-10899:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：它以额外 embedding/adapter、训练数据和 selector drift 换取更低的在线估计开销。Base model、selector revision、 prompt template、sampling policy、domain、cache budget 与 kept indices 必须进入同一 cache identity；lookahead tokens 不应混入普通 Decode history。错误选择仍是 silent eviction，且 per-layer top-k 可能放大 paged-block fragmentation； LookaheadKV 的单请求作者实验不覆盖 continuous batching、prefix sharing、quantized KV 或 Decode-stage drift。 因此 FullKV、prompt heuristic 与 draft verification 均继续成立；隐式 lookahead 只在 selector 可回归测试、 workload 相对稳定且节省的 TTFT 足以覆盖 artifact lifecycle 时使用。<!-- existing:SF-2026-ARXIV-2603-10899:end -->

<!-- delta:SF-2026-ARXIV-2603-10899:start -->新证据差异：exact-v1 的 `3 Proposed Method: LookaheadKV` 把论文方案定位到 KV 的 identity、压缩、复用、放置与失效状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-10899:end -->

边界：只支持 arXiv:2603.10899v1 §3 Proposed Method: LookaheadKV 的机制与 §4.2 Evaluation Setup 的公开 workload；§7 Conclusion and Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 最终决定为 **No Change — Existing Coverage**；现有命题、结构边界与相邻章节已由 fresh-context reviewer 复核。
<!-- books-review:SF-2026-ARXIV-2603-10899:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260312-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260312 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260312-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-09983; review:SF-2026-ARXIV-2603-10030; review:SF-2026-ARXIV-2603-10031; review:SF-2026-ARXIV-2603-10032; review:SF-2026-ARXIV-2603-10044; review:SF-2026-ARXIV-2603-10057; review:SF-2026-ARXIV-2603-10060; review:SF-2026-ARXIV-2603-10062; review:SF-2026-ARXIV-2603-10085; review:SF-2026-ARXIV-2603-10087; review:SF-2026-ARXIV-2603-10088; review:SF-2026-ARXIV-2603-10143; review:SF-2026-ARXIV-2603-10163; review:SF-2026-ARXIV-2603-10165; review:SF-2026-ARXIV-2603-10291; review:SF-2026-ARXIV-2603-10335; review:SF-2026-ARXIV-2603-10342; review:SF-2026-ARXIV-2603-10353; review:SF-2026-ARXIV-2603-10379; review:SF-2026-ARXIV-2603-10422; review:SF-2026-ARXIV-2603-10444; review:SF-2026-ARXIV-2603-10469; review:SF-2026-ARXIV-2603-10494; review:SF-2026-ARXIV-2603-10521; review:SF-2026-ARXIV-2603-10577; review:SF-2026-ARXIV-2603-10600; review:SF-2026-ARXIV-2603-10712; review:SF-2026-ARXIV-2603-10726; review:SF-2026-ARXIV-2603-10742; review:SF-2026-ARXIV-2603-10749; review:SF-2026-ARXIV-2603-10765; review:SF-2026-ARXIV-2603-10779; review:SF-2026-ARXIV-2603-10899 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260312-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260312-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260312/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-05-inference-system/49-tensorrt-llm.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
- 更新并复核 `books/part-06-ai-infrastructure/66-evaluation-system.md`。
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
