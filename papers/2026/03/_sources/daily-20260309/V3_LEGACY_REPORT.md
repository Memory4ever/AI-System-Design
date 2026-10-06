# Daily Research — 2026-03-09

**Research Date:** 2026-03-09

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-08 09:00:00 ～ 2026-03-09 09:00:00（Asia/Shanghai，北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重放，Weekly dependency=0。

**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open；fresh-context Coverage / Evidence audit 已完成，Integrate 串行 writeback 与 post-write audit 未完成。

## Executive Summary

严格窗口 raw/registered/screened=527/527/527；denominator=54、pre-denominator closures=473。exact-v1 Review complete=54、blocked=0；Integrate 建议=4。旧 Weekly 未参与发现、筛选、评分、Review、Books 判断或漏项校准。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-09 |
| Window End | 2026-03-09 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260309-AUTHOR-54 |
| Denominator Frozen At | 2026-09-03T16:29:27.650758+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-08T09:00:00+08:00 | 2026-03-09T09:00:00+08:00 | 2026-09-03T16:29:27.650758+08:00 | official-schedule recovery receipt + 527/527 title/abstract replay + official abs/HTML/PDF exact-v1 | checked | 527 | SF-2026-ARXIV-2603-05517;SF-2026-ARXIV-2603-05520;SF-2026-ARXIV-2603-05528;SF-2026-ARXIV-2603-05540;SF-2026-ARXIV-2603-05553;SF-2026-ARXIV-2603-05578;SF-2026-ARXIV-2603-05618;SF-2026-ARXIV-2603-05637;SF-2026-ARXIV-2603-05692;SF-2026-ARXIV-2603-05697;SF-2026-ARXIV-2603-05706;SF-2026-ARXIV-2603-05725;SF-2026-ARXIV-2603-05739;SF-2026-ARXIV-2603-05754;SF-2026-ARXIV-2603-05786;SF-2026-ARXIV-2603-05800;SF-2026-ARXIV-2603-05815;SF-2026-ARXIV-2603-05828;SF-2026-ARXIV-2603-05872;SF-2026-ARXIV-2603-05881;SF-2026-ARXIV-2603-05910;SF-2026-ARXIV-2603-05912;SF-2026-ARXIV-2603-05931;SF-2026-ARXIV-2603-05959;SF-2026-ARXIV-2603-05960;SF-2026-ARXIV-2603-05974;SF-2026-ARXIV-2603-06001;SF-2026-ARXIV-2603-06003;SF-2026-ARXIV-2603-06007;SF-2026-ARXIV-2603-06009;SF-2026-ARXIV-2603-06081;SF-2026-ARXIV-2603-06123;SF-2026-ARXIV-2603-06130;SF-2026-ARXIV-2603-06138;SF-2026-ARXIV-2603-06198;SF-2026-ARXIV-2603-06199;SF-2026-ARXIV-2603-06263;SF-2026-ARXIV-2603-06274;SF-2026-ARXIV-2603-06317;SF-2026-ARXIV-2603-06331;SF-2026-ARXIV-2603-06350;SF-2026-ARXIV-2603-06365;SF-2026-ARXIV-2603-06394;SF-2026-ARXIV-2603-06403;SF-2026-ARXIV-2603-06413;SF-2026-ARXIV-2603-06422;SF-2026-ARXIV-2603-06444;SF-2026-ARXIV-2603-06445;SF-2026-ARXIV-2603-06450;SF-2026-ARXIV-2603-06453;SF-2026-ARXIV-2603-06508;SF-2026-ARXIV-2603-06569;SF-2026-ARXIV-2603-06577;SF-2026-ARXIV-2603-06578 | pages=100; prefixes=00..99; final_cursor=end; registered=527; screened=527; retained=54; closure=473 | 2026-03-09T01:00:00+00:00 | screening-ledger-final.json#sha256=a7bcd450a0a834faf0f1e3776c45e82b7f98d5a429070388e30f8f3ed7985c12; announcement-recovery#sha256=16dec71fcc675ae9b23a8bd7f6104113914987266b125be044d82b44b27a55bf | — |

### Coverage Limitations

<!-- coverage:SRC-ARXIV:20260309:start -->作者侧已逐项筛选全部 527 个 identity；selected exact-v1 同时检查 withdrawn 状态。按 Window End 与来源 Effective Date 计算，2026 年 3 月到期的 Required Daily 只有 `SRC-ARXIV`；机构类与 HF 来源自 2026-08-25 生效，不反推本窗口。<!-- coverage:SRC-ARXIV:20260309:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | arXiv:2603.05517v1 | paper-v1:2603.05517 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05517 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05517 | no |
| SF-2026-ARXIV-2603-05520 | arXiv:2603.05520v1 | paper-v1:2603.05520 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05520 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05520 | no |
| SF-2026-ARXIV-2603-05528 | arXiv:2603.05528v1 | paper-v1:2603.05528 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05528 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05528 | no |
| SF-2026-ARXIV-2603-05540 | arXiv:2603.05540v1 | paper-v1:2603.05540 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05540 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05540 | no |
| SF-2026-ARXIV-2603-05553 | arXiv:2603.05553v1 | paper-v1:2603.05553 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05553 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05553 | no |
| SF-2026-ARXIV-2603-05578 | arXiv:2603.05578v1 | paper-v1:2603.05578 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05578 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05578 | no |
| SF-2026-ARXIV-2603-05618 | arXiv:2603.05618v1 | paper-v1:2603.05618 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05618 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05618 | no |
| SF-2026-ARXIV-2603-05637 | arXiv:2603.05637v1 | paper-v1:2603.05637 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05637 | self | — | new_in_window | AGENT-MCP | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05637 | no |
| SF-2026-ARXIV-2603-05692 | arXiv:2603.05692v1 | paper-v1:2603.05692 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05692 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05692 | no |
| SF-2026-ARXIV-2603-05697 | arXiv:2603.05697v1 | paper-v1:2603.05697 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05697 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05697 | no |
| SF-2026-ARXIV-2603-05706 | arXiv:2603.05706v1 | paper-v1:2603.05706 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05706 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05706 | no |
| SF-2026-ARXIV-2603-05725 | arXiv:2603.05725v1 | paper-v1:2603.05725 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05725 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05725 | no |
| SF-2026-ARXIV-2603-05739 | arXiv:2603.05739v1 | paper-v1:2603.05739 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05739 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05739 | no |
| SF-2026-ARXIV-2603-05754 | arXiv:2603.05754v1 | paper-v1:2603.05754 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05754 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05754 | no |
| SF-2026-ARXIV-2603-05786 | arXiv:2603.05786v1 | paper-v1:2603.05786 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05786 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05786 | no |
| SF-2026-ARXIV-2603-05800 | arXiv:2603.05800v1 | paper-v1:2603.05800 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05800 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-05800 | no |
| SF-2026-ARXIV-2603-05815 | arXiv:2603.05815v1 | paper-v1:2603.05815 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05815 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05815 | no |
| SF-2026-ARXIV-2603-05828 | arXiv:2603.05828v1 | paper-v1:2603.05828 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05828 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05828 | no |
| SF-2026-ARXIV-2603-05872 | arXiv:2603.05872v1 | paper-v1:2603.05872 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05872 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05872 | no |
| SF-2026-ARXIV-2603-05881 | arXiv:2603.05881v1 | paper-v1:2603.05881 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05881 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05881 | no |
| SF-2026-ARXIV-2603-05910 | arXiv:2603.05910v1 | paper-v1:2603.05910 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05910 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05910 | no |
| SF-2026-ARXIV-2603-05912 | arXiv:2603.05912v1 | paper-v1:2603.05912 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05912 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05912 | no |
| SF-2026-ARXIV-2603-05931 | arXiv:2603.05931v1 | paper-v1:2603.05931 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05931 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2603-05931 | no |
| SF-2026-ARXIV-2603-05959 | arXiv:2603.05959v1 | paper-v1:2603.05959 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-05959 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05959 | no |
| SF-2026-ARXIV-2603-05960 | arXiv:2603.05960v1 | paper-v1:2603.05960 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05960 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05960 | no |
| SF-2026-ARXIV-2603-05974 | arXiv:2603.05974v1 | paper-v1:2603.05974 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-05974 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05974 | no |
| SF-2026-ARXIV-2603-06001 | arXiv:2603.06001v1 | paper-v1:2603.06001 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06001 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06001 | no |
| SF-2026-ARXIV-2603-06003 | arXiv:2603.06003v1 | paper-v1:2603.06003 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06003 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06003 | no |
| SF-2026-ARXIV-2603-06007 | arXiv:2603.06007v1 | paper-v1:2603.06007 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06007 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06007 | no |
| SF-2026-ARXIV-2603-06009 | arXiv:2603.06009v1 | paper-v1:2603.06009 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06009 | self | — | new_in_window | TRAIN-PPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06009 | no |
| SF-2026-ARXIV-2603-06081 | arXiv:2603.06081v1 | paper-v1:2603.06081 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06081 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06081 | no |
| SF-2026-ARXIV-2603-06123 | arXiv:2603.06123v1 | paper-v1:2603.06123 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06123 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06123 | no |
| SF-2026-ARXIV-2603-06130 | arXiv:2603.06130v1 | paper-v1:2603.06130 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06130 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06130 | no |
| SF-2026-ARXIV-2603-06138 | arXiv:2603.06138v1 | paper-v1:2603.06138 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06138 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06138 | no |
| SF-2026-ARXIV-2603-06198 | arXiv:2603.06198v1 | paper-v1:2603.06198 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06198 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06198 | no |
| SF-2026-ARXIV-2603-06199 | arXiv:2603.06199v1 | paper-v1:2603.06199 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06199 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06199 | no |
| SF-2026-ARXIV-2603-06263 | arXiv:2603.06263v1 | paper-v1:2603.06263 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06263 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06263 | no |
| SF-2026-ARXIV-2603-06274 | arXiv:2603.06274v1 | paper-v1:2603.06274 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06274 | self | — | new_in_window | MODEL-SELF-ATTENTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06274 | no |
| SF-2026-ARXIV-2603-06317 | arXiv:2603.06317v1 | paper-v1:2603.06317 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06317 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06317 | no |
| SF-2026-ARXIV-2603-06331 | arXiv:2603.06331v1 | paper-v1:2603.06331 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06331 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06331 | no |
| SF-2026-ARXIV-2603-06350 | arXiv:2603.06350v1 | paper-v1:2603.06350 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06350 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-06350 | no |
| SF-2026-ARXIV-2603-06365 | arXiv:2603.06365v1 | paper-v1:2603.06365 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06365 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06365 | no |
| SF-2026-ARXIV-2603-06394 | arXiv:2603.06394v1 | paper-v1:2603.06394 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06394 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06394 | no |
| SF-2026-ARXIV-2603-06403 | arXiv:2603.06403v1 | paper-v1:2603.06403 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06403 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06403 | no |
| SF-2026-ARXIV-2603-06413 | arXiv:2603.06413v1 | paper-v1:2603.06413 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06413 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06413 | no |
| SF-2026-ARXIV-2603-06422 | arXiv:2603.06422v1 | paper-v1:2603.06422 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06422 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06422 | no |
| SF-2026-ARXIV-2603-06444 | arXiv:2603.06444v1 | paper-v1:2603.06444 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06444 | self | — | new_in_window | INFER-DECODE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06444 | no |
| SF-2026-ARXIV-2603-06445 | arXiv:2603.06445v1 | paper-v1:2603.06445 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06445 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06445 | no |
| SF-2026-ARXIV-2603-06450 | arXiv:2603.06450v1 | paper-v1:2603.06450 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06450 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06450 | no |
| SF-2026-ARXIV-2603-06453 | arXiv:2603.06453v1 | paper-v1:2603.06453 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06453 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06453 | no |
| SF-2026-ARXIV-2603-06508 | arXiv:2603.06508v1 | paper-v1:2603.06508 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06508 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06508 | no |
| SF-2026-ARXIV-2603-06569 | arXiv:2603.06569v1 | paper-v1:2603.06569 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06569 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06569 | no |
| SF-2026-ARXIV-2603-06577 | arXiv:2603.06577v1 | paper-v1:2603.06577 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2603-06577 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06577 | no |
| SF-2026-ARXIV-2603-06578 | arXiv:2603.06578v1 | paper-v1:2603.06578 | 2026-W11 | 2026-03-09 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-06578 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2603-06578 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | RP-96fd4c556a71319e | standard | arXiv:2603.05517v1 | SRC-ARXIV@arXiv:2603.05517v1 | arXiv:2603.05517v1 HTML — §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks [facet=method]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv:2603.05517v1 HTML — §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) [facet=evaluation]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv:2603.05517v1 HTML — §O.1 Limitations and Open Failure Modes [facet=limitations]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d | arXiv exact-v1 identity https://arxiv.org/abs/2603.05517v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05517 | complete |
| SF-2026-ARXIV-2603-05520 | RP-a8834f9393096a87 | standard | arXiv:2603.05520v1 | SRC-ARXIV@arXiv:2603.05520v1 | arXiv:2603.05520v1 HTML — §4.3 Design Implications [facet=method]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv:2603.05520v1 HTML — §7.1 Overall Performance on Medical and Financial Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv:2603.05520v1 HTML — §8 Conclusion and Future Work [facet=limitations]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05520v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05520 | complete |
| SF-2026-ARXIV-2603-05528 | RP-6f9ba4af627cc40e | standard | arXiv:2603.05528v1 | SRC-ARXIV@arXiv:2603.05528v1 | arXiv:2603.05528v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.05528v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05528v1.html; sha256:3c79da9c11b969078776df31d8632294fe015143fe86fa316e1274d858962660 | arXiv:2603.05528v1 HTML — §IV Experiments [facet=evaluation]; https://arxiv.org/html/2603.05528v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05528v1.html; sha256:3c79da9c11b969078776df31d8632294fe015143fe86fa316e1274d858962660 | arXiv:2603.05528v1 HTML — §VI Conclusion [facet=limitations]; https://arxiv.org/html/2603.05528v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05528v1.html; sha256:3c79da9c11b969078776df31d8632294fe015143fe86fa316e1274d858962660 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05528v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05528 | complete |
| SF-2026-ARXIV-2603-05540 | RP-38e767373b86ce6e | deep | arXiv:2603.05540v1 | SRC-ARXIV@arXiv:2603.05540v1 | arXiv:2603.05540v1 HTML — §Neural architecture coupling. [facet=method]; https://arxiv.org/html/2603.05540v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05540v1.html; sha256:8020b2c9f7ce64c2801b538af6a84f5884147c7d8f2a5ea2caf90fb50351103a | arXiv:2603.05540v1 HTML — §Parsing theory and reachability. [facet=evaluation]; https://arxiv.org/html/2603.05540v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05540v1.html; sha256:8020b2c9f7ce64c2801b538af6a84f5884147c7d8f2a5ea2caf90fb50351103a | arXiv:2603.05540v1 HTML — §12 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05540v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05540v1.html; sha256:8020b2c9f7ce64c2801b538af6a84f5884147c7d8f2a5ea2caf90fb50351103a | arXiv exact-v1 identity https://arxiv.org/abs/2603.05540v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05540 | complete |
| SF-2026-ARXIV-2603-05553 | RP-15785024b5ba4312 | standard | arXiv:2603.05553v1 | SRC-ARXIV@arXiv:2603.05553v1 | arXiv:2603.05553v1 HTML — §3.3.1 Architecture [facet=method]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv:2603.05553v1 HTML — §4.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv:2603.05553v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05553v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05553 | complete |
| SF-2026-ARXIV-2603-05578 | RP-e857fb474c66952d | standard | arXiv:2603.05578v1 | SRC-ARXIV@arXiv:2603.05578v1 | arXiv:2603.05578v1 HTML — §Appendix A Evaluation Methodology Details [facet=method]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv:2603.05578v1 HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv:2603.05578v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e | arXiv exact-v1 identity https://arxiv.org/abs/2603.05578v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05578 | complete |
| SF-2026-ARXIV-2603-05618 | RP-0f51987661f5ec6d | standard | arXiv:2603.05618v1 | SRC-ARXIV@arXiv:2603.05618v1 | arXiv:2603.05618v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.05618v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05618v1.html; sha256:07fcda3ca34b32359eee1454fb86fc000b2ddd8e1bbba4a25adc73edafa7aa7b | arXiv:2603.05618v1 HTML — §3.3 Gatekeeper Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05618v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05618v1.html; sha256:07fcda3ca34b32359eee1454fb86fc000b2ddd8e1bbba4a25adc73edafa7aa7b | arXiv:2603.05618v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.05618v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05618v1.html; sha256:07fcda3ca34b32359eee1454fb86fc000b2ddd8e1bbba4a25adc73edafa7aa7b | arXiv exact-v1 identity https://arxiv.org/abs/2603.05618v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05618 | complete |
| SF-2026-ARXIV-2603-05637 | RP-dc7e253e72c0c112 | standard | arXiv:2603.05637v1 | SRC-ARXIV@arXiv:2603.05637v1 | arXiv:2603.05637v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv:2603.05637v1 HTML — §3.3. Taxonomy Creation and Validation [facet=evaluation]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv:2603.05637v1 HTML — §7. Conclusion and Future Works [facet=limitations]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05637v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05637 | complete |
| SF-2026-ARXIV-2603-05692 | RP-85ab44e4499f160c | standard | arXiv:2603.05692v1 | SRC-ARXIV@arXiv:2603.05692v1 | arXiv:2603.05692v1 HTML — §2.2. Overview of Llama 3.1-70B/-405B Models [facet=method]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv:2603.05692v1 HTML — §3. In-House Simulator and Its Validation [facet=evaluation]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv:2603.05692v1 HTML — §6. Discussion [facet=limitations]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05692v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05692 | complete |
| SF-2026-ARXIV-2603-05697 | RP-9e718d373ce986bc | standard | arXiv:2603.05697v1 | SRC-ARXIV@arXiv:2603.05697v1 | arXiv:2603.05697v1 HTML — §0.D.1 Implementation details [facet=method]; https://arxiv.org/html/2603.05697v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05697v1.html; sha256:03f6adfd0cf6c1c4385ba176b3ebb561bae916cc452cc2bc76d20e6f015171d2 | arXiv:2603.05697v1 HTML — §0.D.3 Evaluation Models [facet=evaluation]; https://arxiv.org/html/2603.05697v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05697v1.html; sha256:03f6adfd0cf6c1c4385ba176b3ebb561bae916cc452cc2bc76d20e6f015171d2 | arXiv:2603.05697v1 HTML — §Appendix 0.J Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.05697v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05697v1.html; sha256:03f6adfd0cf6c1c4385ba176b3ebb561bae916cc452cc2bc76d20e6f015171d2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05697v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05697 | complete |
| SF-2026-ARXIV-2603-05706 | RP-25b37d0c233ebf40 | standard | arXiv:2603.05706v1 | SRC-ARXIV@arXiv:2603.05706v1 | arXiv:2603.05706v1 HTML — §2.2 Evaluation Design [facet=method]; https://arxiv.org/html/2603.05706v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05706v1.html; sha256:16a5cf0fbdb820f36e393662e9fced3af825aedda26bd542a01984acf514dd1f | arXiv:2603.05706v1 HTML — §2.2 Evaluation Design [facet=evaluation]; https://arxiv.org/html/2603.05706v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05706v1.html; sha256:16a5cf0fbdb820f36e393662e9fced3af825aedda26bd542a01984acf514dd1f | arXiv:2603.05706v1 HTML — §Limitations. [facet=limitations]; https://arxiv.org/html/2603.05706v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05706v1.html; sha256:16a5cf0fbdb820f36e393662e9fced3af825aedda26bd542a01984acf514dd1f | arXiv exact-v1 identity https://arxiv.org/abs/2603.05706v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05706 | complete |
| SF-2026-ARXIV-2603-05725 | RP-6b36e3b246d58810 | deep | arXiv:2603.05725v1 | SRC-ARXIV@arXiv:2603.05725v1 | arXiv:2603.05725v1 HTML — §4. The GPU-Native Design [facet=method]; https://arxiv.org/html/2603.05725v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05725v1.html; sha256:a2f11f7b2d6a964961d23c2ffdc69392e0e134dd5c45b1fb4b189365d2fcdd27 | arXiv:2603.05725v1 HTML — §5. Preliminary Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05725v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05725v1.html; sha256:a2f11f7b2d6a964961d23c2ffdc69392e0e134dd5c45b1fb4b189365d2fcdd27 | arXiv:2603.05725v1 HTML — §6. Conclusion [facet=limitations]; https://arxiv.org/html/2603.05725v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05725v1.html; sha256:a2f11f7b2d6a964961d23c2ffdc69392e0e134dd5c45b1fb4b189365d2fcdd27 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05725v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05725 | complete |
| SF-2026-ARXIV-2603-05739 | RP-36d8052f9543769a | standard | arXiv:2603.05739v1 | SRC-ARXIV@arXiv:2603.05739v1 | arXiv:2603.05739v1 HTML — §2.1 Inference-time alignment framework [facet=method]; https://arxiv.org/html/2603.05739v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05739v1.html; sha256:5a5804a713ff42732281d158dbfae4791319284098eb2648fdb4e61f6cc6c19e | arXiv:2603.05739v1 HTML — §5.1 Proof Sketch of Theorem 3 [facet=evaluation]; https://arxiv.org/html/2603.05739v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05739v1.html; sha256:5a5804a713ff42732281d158dbfae4791319284098eb2648fdb4e61f6cc6c19e | arXiv:2603.05739v1 HTML — §Conclusion. [facet=limitations]; https://arxiv.org/html/2603.05739v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05739v1.html; sha256:5a5804a713ff42732281d158dbfae4791319284098eb2648fdb4e61f6cc6c19e | arXiv exact-v1 identity https://arxiv.org/abs/2603.05739v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05739 | complete |
| SF-2026-ARXIV-2603-05754 | RP-62a3782416cbb04a | standard | arXiv:2603.05754v1 | SRC-ARXIV@arXiv:2603.05754v1 | arXiv:2603.05754v1 HTML — §III-A System Architecture and Adaptation Strategy [facet=method]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv:2603.05754v1 HTML — §V-C Exploratory Mechanism Analysis: Attention Ablation [facet=evaluation]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv:2603.05754v1 HTML — §V-B1 Limitations of RGB-Only and RGB-D Variants [facet=limitations]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05754v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05754 | complete |
| SF-2026-ARXIV-2603-05786 | RP-9442f8a55338dbc0 | deep | arXiv:2603.05786v1 | SRC-ARXIV@arXiv:2603.05786v1 | arXiv:2603.05786v1 HTML — §An agent skill-based proof-of-guardrail implementation. [facet=method]; https://arxiv.org/html/2603.05786v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05786v1.html; sha256:615e4b77b2d881e703e9d296257d161690894ac7614b9d4f4147e468d19753ea | arXiv:2603.05786v1 HTML — §3.2 Proof-of-Guardrail with TEE Attestation [facet=evaluation]; https://arxiv.org/html/2603.05786v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05786v1.html; sha256:615e4b77b2d881e703e9d296257d161690894ac7614b9d4f4147e468d19753ea | arXiv:2603.05786v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.05786v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05786v1.html; sha256:615e4b77b2d881e703e9d296257d161690894ac7614b9d4f4147e468d19753ea | arXiv exact-v1 identity https://arxiv.org/abs/2603.05786v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05786 | complete |
| SF-2026-ARXIV-2603-05800 | RP-596cee8794398ded | deep | arXiv:2603.05800v1 | SRC-ARXIV@arXiv:2603.05800v1 | arXiv:2603.05800v1 HTML — §4.7. Implementation [facet=method]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv:2603.05800v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv:2603.05800v1 HTML — §7. Conclusions [facet=limitations]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c | arXiv exact-v1 identity https://arxiv.org/abs/2603.05800v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05800 | complete |
| SF-2026-ARXIV-2603-05815 | RP-cdc90b615a8bd91b | standard | arXiv:2603.05815v1 | SRC-ARXIV@arXiv:2603.05815v1 | arXiv:2603.05815v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.05815v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05815v1.html; sha256:2b37ae924a692244b15c75c6e7cfed4466e662929a65170fa16da17d6d131ad2 | arXiv:2603.05815v1 HTML — §4.2.1 LIBERO Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.05815v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05815v1.html; sha256:2b37ae924a692244b15c75c6e7cfed4466e662929a65170fa16da17d6d131ad2 | arXiv:2603.05815v1 HTML — §5 Conclusion and Limitations [facet=limitations]; https://arxiv.org/html/2603.05815v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05815v1.html; sha256:2b37ae924a692244b15c75c6e7cfed4466e662929a65170fa16da17d6d131ad2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05815v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05815 | complete |
| SF-2026-ARXIV-2603-05828 | RP-58e4c619c2921338 | standard | arXiv:2603.05828v1 | SRC-ARXIV@arXiv:2603.05828v1 | arXiv:2603.05828v1 HTML — §4.1.3. Implementation [facet=method]; https://arxiv.org/html/2603.05828v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05828v1.html; sha256:e94c154f1ce87fc610e3b57932df541e8a499a3801d88f5bda6ce90a8f1f04c0 | arXiv:2603.05828v1 HTML — §4.2. Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05828v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05828v1.html; sha256:e94c154f1ce87fc610e3b57932df541e8a499a3801d88f5bda6ce90a8f1f04c0 | arXiv:2603.05828v1 HTML — §5. Conclusion [facet=limitations]; https://arxiv.org/html/2603.05828v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05828v1.html; sha256:e94c154f1ce87fc610e3b57932df541e8a499a3801d88f5bda6ce90a8f1f04c0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05828v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05828 | complete |
| SF-2026-ARXIV-2603-05872 | RP-ef1b33a0ac1a9848 | standard | arXiv:2603.05872v1 | SRC-ARXIV@arXiv:2603.05872v1 | arXiv:2603.05872v1 HTML — §Appendix A Self-Evolution Algorithm [facet=method]; https://arxiv.org/html/2603.05872v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05872v1.html; sha256:60bdbfcc2ad4c8bcbdceb33da5d9bec7457cee703f1463e16ac9de3696ca7def | arXiv:2603.05872v1 HTML — §4.3 Evaluation Configuration [facet=evaluation]; https://arxiv.org/html/2603.05872v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05872v1.html; sha256:60bdbfcc2ad4c8bcbdceb33da5d9bec7457cee703f1463e16ac9de3696ca7def | arXiv:2603.05872v1 HTML — §8 Limitations [facet=limitations]; https://arxiv.org/html/2603.05872v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05872v1.html; sha256:60bdbfcc2ad4c8bcbdceb33da5d9bec7457cee703f1463e16ac9de3696ca7def | arXiv exact-v1 identity https://arxiv.org/abs/2603.05872v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05872 | complete |
| SF-2026-ARXIV-2603-05881 | RP-1f5f15cfd4e878f5 | standard | arXiv:2603.05881v1 | SRC-ARXIV@arXiv:2603.05881v1 | arXiv:2603.05881v1 HTML — §3.2 Confidence-First Paradigm Definition [facet=method]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv:2603.05881v1 HTML — §4.1.2 Evaluation Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv:2603.05881v1 HTML — §6 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf | arXiv exact-v1 identity https://arxiv.org/abs/2603.05881v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05881 | complete |
| SF-2026-ARXIV-2603-05910 | RP-c11a05f52e34973c | standard | arXiv:2603.05910v1 | SRC-ARXIV@arXiv:2603.05910v1 | arXiv:2603.05910v1 HTML — §C.2 Tool Designer in Saturation Strategy [facet=method]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv:2603.05910v1 HTML — §4.4 State-Wise User Simulation and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv:2603.05910v1 HTML — §6 Conclusions [facet=limitations]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05910v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05910 | complete |
| SF-2026-ARXIV-2603-05912 | RP-56d93815581b9ece | standard | arXiv:2603.05912v1 | SRC-ARXIV@arXiv:2603.05912v1 | arXiv:2603.05912v1 HTML — §4.1 Methodology: The Micro-Gold Protocol [facet=method]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv:2603.05912v1 HTML — §7.3 Results on Other Factuality Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv:2603.05912v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05912v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05912 | complete |
| SF-2026-ARXIV-2603-05931 | RP-cab5bc9837c5db14 | deep | arXiv:2603.05931v1 | SRC-ARXIV@arXiv:2603.05931v1 | arXiv:2603.05931v1 HTML — §IV-E System Overview [facet=method]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv:2603.05931v1 HTML — §VI-E Ablation Analysis [facet=evaluation]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv:2603.05931v1 HTML — §VIII Conclusion [facet=limitations]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05931v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05931 | complete |
| SF-2026-ARXIV-2603-05959 | RP-f5cdf76a78b6ee19 | deep | arXiv:2603.05959v1 | SRC-ARXIV@arXiv:2603.05959v1 | arXiv:2603.05959v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.05959v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05959v1.html; sha256:0efab5d5c840316cafc0b348d496af2cf11cda5781dae932742b11322ea26899 | arXiv:2603.05959v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.05959v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05959v1.html; sha256:0efab5d5c840316cafc0b348d496af2cf11cda5781dae932742b11322ea26899 | arXiv:2603.05959v1 HTML — §E Failure Cases [facet=limitations]; https://arxiv.org/html/2603.05959v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05959v1.html; sha256:0efab5d5c840316cafc0b348d496af2cf11cda5781dae932742b11322ea26899 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05959v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05959 | complete |
| SF-2026-ARXIV-2603-05960 | RP-af12349bd718fbcd | standard | arXiv:2603.05960v1 | SRC-ARXIV@arXiv:2603.05960v1 | arXiv:2603.05960v1 HTML — §3.2 Omni-Masked Gradient Descent [facet=method]; https://arxiv.org/html/2603.05960v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05960v1.html; sha256:9cd83752cf382eafab558b81aa57b3982f3a561cef7a9e05e682024f893f70e9 | arXiv:2603.05960v1 HTML — §5.4 Pre-training Experiments of LLMs [facet=evaluation]; https://arxiv.org/html/2603.05960v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05960v1.html; sha256:9cd83752cf382eafab558b81aa57b3982f3a561cef7a9e05e682024f893f70e9 | arXiv:2603.05960v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.05960v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05960v1.html; sha256:9cd83752cf382eafab558b81aa57b3982f3a561cef7a9e05e682024f893f70e9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05960v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05960 | complete |
| SF-2026-ARXIV-2603-05974 | RP-367a6b5778dfc158 | standard | arXiv:2603.05974v1 | SRC-ARXIV@arXiv:2603.05974v1 | arXiv:2603.05974v1 HTML — §4.3. Implementation Details [facet=method]; https://arxiv.org/html/2603.05974v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05974v1.html; sha256:22d05069b51076c8214d0ba6afadda5de3234e88bef014a15210703c44110744 | arXiv:2603.05974v1 HTML — §5. Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05974v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05974v1.html; sha256:22d05069b51076c8214d0ba6afadda5de3234e88bef014a15210703c44110744 | arXiv:2603.05974v1 HTML — §6.5. Limitation [facet=limitations]; https://arxiv.org/html/2603.05974v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05974v1.html; sha256:22d05069b51076c8214d0ba6afadda5de3234e88bef014a15210703c44110744 | arXiv exact-v1 identity https://arxiv.org/abs/2603.05974v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-05974 | complete |
| SF-2026-ARXIV-2603-06001 | RP-8fcff515ced2225b | standard | arXiv:2603.06001v1 | SRC-ARXIV@arXiv:2603.06001v1 | arXiv:2603.06001v1 HTML — §3.2 Contradiction Taxonomy and Design Principles [facet=method]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv:2603.06001v1 HTML — §5.6 Real-World Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv:2603.06001v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06001v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06001 | complete |
| SF-2026-ARXIV-2603-06003 | RP-a969a52754a4b94e | standard | arXiv:2603.06003v1 | SRC-ARXIV@arXiv:2603.06003v1 | arXiv:2603.06003v1 HTML — §2.3 Other Compression Methods [facet=method]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv:2603.06003v1 HTML — §4.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv:2603.06003v1 HTML — §Appendix C Limitations [facet=limitations]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd | arXiv exact-v1 identity https://arxiv.org/abs/2603.06003v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06003 | complete |
| SF-2026-ARXIV-2603-06007 | RP-44993cf2f29bc76c | standard | arXiv:2603.06007v1 | SRC-ARXIV@arXiv:2603.06007v1 | arXiv:2603.06007v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv:2603.06007v1 HTML — §4 Evaluation and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv:2603.06007v1 HTML — §Limitations [facet=limitations]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a | arXiv exact-v1 identity https://arxiv.org/abs/2603.06007v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06007 | complete |
| SF-2026-ARXIV-2603-06009 | RP-eb0390d2e99c1c84 | deep | arXiv:2603.06009v1 | SRC-ARXIV@arXiv:2603.06009v1 | arXiv:2603.06009v1 HTML — §Appendix F SFL Hand Designed Results [facet=method]; https://arxiv.org/html/2603.06009v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06009v1.html; sha256:c450f493354e0d32d28546e9bafd0da30b15a00ae2e27c9acac4b424c122625d | arXiv:2603.06009v1 HTML — §5.1 Robotics Results [facet=evaluation]; https://arxiv.org/html/2603.06009v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06009v1.html; sha256:c450f493354e0d32d28546e9bafd0da30b15a00ae2e27c9acac4b424c122625d | arXiv:2603.06009v1 HTML — §8 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06009v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06009v1.html; sha256:c450f493354e0d32d28546e9bafd0da30b15a00ae2e27c9acac4b424c122625d | arXiv exact-v1 identity https://arxiv.org/abs/2603.06009v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06009 | complete |
| SF-2026-ARXIV-2603-06081 | RP-524316fc7207f84e | standard | arXiv:2603.06081v1 | SRC-ARXIV@arXiv:2603.06081v1 | arXiv:2603.06081v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv:2603.06081v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv:2603.06081v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06081v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06081 | complete |
| SF-2026-ARXIV-2603-06123 | RP-3b2a6ef403d5e418 | standard | arXiv:2603.06123v1 | SRC-ARXIV@arXiv:2603.06123v1 | arXiv:2603.06123v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.06123v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06123v1.html; sha256:f1ce18dd10ba66c3ab1e9c528925d5f5783975e0e502f2fa1123c0ba770405ef | arXiv:2603.06123v1 HTML — §4.2 Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.06123v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06123v1.html; sha256:f1ce18dd10ba66c3ab1e9c528925d5f5783975e0e502f2fa1123c0ba770405ef | arXiv:2603.06123v1 HTML — §7 Limitations [facet=limitations]; https://arxiv.org/html/2603.06123v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06123v1.html; sha256:f1ce18dd10ba66c3ab1e9c528925d5f5783975e0e502f2fa1123c0ba770405ef | arXiv exact-v1 identity https://arxiv.org/abs/2603.06123v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06123 | complete |
| SF-2026-ARXIV-2603-06130 | RP-4c17571d6f10d797 | standard | arXiv:2603.06130v1 | SRC-ARXIV@arXiv:2603.06130v1 | arXiv:2603.06130v1 HTML — §1.3 Literature Overview [facet=method]; https://arxiv.org/html/2603.06130v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06130v1.html; sha256:7bd236a37cdb05d13d4b6885de7ff6664b2e07339f4674edb99320a2a401a03a | Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.06130v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06130v1.html; sha256:7bd236a37cdb05d13d4b6885de7ff6664b2e07339f4674edb99320a2a401a03a | arXiv:2603.06130v1 HTML — §4 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06130v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06130v1.html; sha256:7bd236a37cdb05d13d4b6885de7ff6664b2e07339f4674edb99320a2a401a03a | arXiv exact-v1 identity https://arxiv.org/abs/2603.06130v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06130 | complete |
| SF-2026-ARXIV-2603-06138 | RP-2638ce6977454d97 | standard | arXiv:2603.06138v1 | SRC-ARXIV@arXiv:2603.06138v1 | arXiv:2603.06138v1 HTML — §5.3 Baselines and Compared Methods [facet=method]; https://arxiv.org/html/2603.06138v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06138v1.html; sha256:e716afb6d974bfeae3c9dabab0eeaac494589190ee36e2a8505ea2454328b0a4 | arXiv:2603.06138v1 HTML — §5.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.06138v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06138v1.html; sha256:e716afb6d974bfeae3c9dabab0eeaac494589190ee36e2a8505ea2454328b0a4 | arXiv:2603.06138v1 HTML — §G.9 Failure Mode Taxonomy [facet=limitations]; https://arxiv.org/html/2603.06138v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06138v1.html; sha256:e716afb6d974bfeae3c9dabab0eeaac494589190ee36e2a8505ea2454328b0a4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06138v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06138 | complete |
| SF-2026-ARXIV-2603-06198 | RP-c0c6631ac5b7808a | standard | arXiv:2603.06198v1 | SRC-ARXIV@arXiv:2603.06198v1 | arXiv:2603.06198v1 HTML — §5.2. Evaluation Method [facet=method]; https://arxiv.org/html/2603.06198v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06198v1.html; sha256:9b71be1d0b24d8ced81e5e28b81fd136d0ba2ea761a91a75cbd47b4cb7bc3bca | arXiv:2603.06198v1 HTML — §4.1.1. Evaluation Categories and Aspects [facet=evaluation]; https://arxiv.org/html/2603.06198v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06198v1.html; sha256:9b71be1d0b24d8ced81e5e28b81fd136d0ba2ea761a91a75cbd47b4cb7bc3bca | arXiv:2603.06198v1 HTML — §6. Limitations [facet=limitations]; https://arxiv.org/html/2603.06198v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06198v1.html; sha256:9b71be1d0b24d8ced81e5e28b81fd136d0ba2ea761a91a75cbd47b4cb7bc3bca | arXiv exact-v1 identity https://arxiv.org/abs/2603.06198v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06198 | complete |
| SF-2026-ARXIV-2603-06199 | RP-104be6310eff5ea2 | standard | arXiv:2603.06199v1 | SRC-ARXIV@arXiv:2603.06199v1 | arXiv:2603.06199v1 HTML — §3.3 Comparison with Previous Methods. [facet=method]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv:2603.06199v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv:2603.06199v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06199v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06199 | complete |
| SF-2026-ARXIV-2603-06263 | RP-cccb7d977a157222 | standard | arXiv:2603.06263v1 | SRC-ARXIV@arXiv:2603.06263v1 | arXiv:2603.06263v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.06263v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06263v1.html; sha256:1efece04d776fd96ac940a6b92c206ee1b98c75fc1b155ae7101596c626bb2d9 | arXiv:2603.06263v1 HTML — §5.2 Results: Security [facet=evaluation]; https://arxiv.org/html/2603.06263v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06263v1.html; sha256:1efece04d776fd96ac940a6b92c206ee1b98c75fc1b155ae7101596c626bb2d9 | arXiv:2603.06263v1 HTML — §Limitations of TBP: security vs. efficiency. [facet=limitations]; https://arxiv.org/html/2603.06263v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06263v1.html; sha256:1efece04d776fd96ac940a6b92c206ee1b98c75fc1b155ae7101596c626bb2d9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06263v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06263 | complete |
| SF-2026-ARXIV-2603-06274 | RP-c4b0f1ee23da8466 | standard | arXiv:2603.06274v1 | SRC-ARXIV@arXiv:2603.06274v1 | arXiv:2603.06274v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.06274v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06274v1.html; sha256:43b90be1228e2f3bfa4ab948277cf74f5bc1e4c3023de350fcc617b114ab809b | arXiv:2603.06274v1 HTML — §3.3 Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.06274v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06274v1.html; sha256:43b90be1228e2f3bfa4ab948277cf74f5bc1e4c3023de350fcc617b114ab809b | arXiv:2603.06274v1 HTML — §Limitations of Score-Aware Metric. [facet=limitations]; https://arxiv.org/html/2603.06274v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06274v1.html; sha256:43b90be1228e2f3bfa4ab948277cf74f5bc1e4c3023de350fcc617b114ab809b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06274v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06274 | complete |
| SF-2026-ARXIV-2603-06317 | RP-80f5803091c90a23 | deep | arXiv:2603.06317v1 | SRC-ARXIV@arXiv:2603.06317v1 | arXiv:2603.06317v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.06317v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06317v1.html; sha256:e859a0c2d1e8b5f9fc545019a6c59c7ede265e75b2f6807414cd1e2b79728710 | arXiv:2603.06317v1 HTML — §A.3 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06317v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06317v1.html; sha256:e859a0c2d1e8b5f9fc545019a6c59c7ede265e75b2f6807414cd1e2b79728710 | arXiv:2603.06317v1 HTML — §5 Discussion and Conclusion [facet=limitations]; https://arxiv.org/html/2603.06317v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06317v1.html; sha256:e859a0c2d1e8b5f9fc545019a6c59c7ede265e75b2f6807414cd1e2b79728710 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06317v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06317 | complete |
| SF-2026-ARXIV-2603-06331 | RP-3b853e2f31ed6527 | standard | arXiv:2603.06331v1 | SRC-ARXIV@arXiv:2603.06331v1 | arXiv:2603.06331v1 HTML — §4.1 Curvature-guided Heterogeneous Token Prediction [facet=method]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv:2603.06331v1 HTML — §5.2 World Generation Results [facet=evaluation]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv:2603.06331v1 HTML — §Failure of Uniform Strategies. [facet=limitations]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06331v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06331 | complete |
| SF-2026-ARXIV-2603-06350 | RP-fc8fc6579f986b7e | deep | arXiv:2603.06350v1 | SRC-ARXIV@arXiv:2603.06350v1 | arXiv:2603.06350v1 HTML — §3.2. Architecture and Workflow [facet=method]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv:2603.06350v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv:2603.06350v1 HTML — §8. Conclusion [facet=limitations]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a | arXiv exact-v1 identity https://arxiv.org/abs/2603.06350v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06350 | complete |
| SF-2026-ARXIV-2603-06365 | RP-c8cf6f39c28d4c25 | standard | arXiv:2603.06365v1 | SRC-ARXIV@arXiv:2603.06365v1 | arXiv:2603.06365v1 HTML — §3 ESAA-Security Architecture [facet=method]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv:2603.06365v1 HTML — §6 Evaluation Design and Research Questions [facet=evaluation]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv:2603.06365v1 HTML — §8 Discussion, Limitations, and Threats to Validity [facet=limitations]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06365v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06365 | complete |
| SF-2026-ARXIV-2603-06394 | RP-d242a92d3a73fddc | standard | arXiv:2603.06394v1 | SRC-ARXIV@arXiv:2603.06394v1 | arXiv:2603.06394v1 HTML — §5.1 Architecture overview [facet=method]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv:2603.06394v1 HTML — §5.3 Validation framework [facet=evaluation]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv:2603.06394v1 HTML — §6.5 Future work [facet=limitations]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06394v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06394 | complete |
| SF-2026-ARXIV-2603-06403 | RP-fcc14a57d3bada47 | standard | arXiv:2603.06403v1 | SRC-ARXIV@arXiv:2603.06403v1 | arXiv:2603.06403v1 HTML — §3.1 Reward and Cost Predictor Design [facet=method]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv:2603.06403v1 HTML — §5.3 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv:2603.06403v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06403v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06403 | complete |
| SF-2026-ARXIV-2603-06413 | RP-ea248548e4e09bde | deep | arXiv:2603.06413v1 | SRC-ARXIV@arXiv:2603.06413v1 | arXiv:2603.06413v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.06413v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06413v1.html; sha256:672607fe39827c5d6b7c257a08a1f33c9397beec1b2cacd4b2e0283d8bf5bc99 | arXiv:2603.06413v1 HTML — §VI Results Evaluation and Quality Assessment [facet=evaluation]; https://arxiv.org/html/2603.06413v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06413v1.html; sha256:672607fe39827c5d6b7c257a08a1f33c9397beec1b2cacd4b2e0283d8bf5bc99 | arXiv:2603.06413v1 HTML — §VIII Conclusion [facet=limitations]; https://arxiv.org/html/2603.06413v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06413v1.html; sha256:672607fe39827c5d6b7c257a08a1f33c9397beec1b2cacd4b2e0283d8bf5bc99 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06413v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06413 | complete |
| SF-2026-ARXIV-2603-06422 | RP-033483df6406e84a | standard | arXiv:2603.06422v1 | SRC-ARXIV@arXiv:2603.06422v1 | arXiv:2603.06422v1 HTML — §IV-B Agent Design [facet=method]; https://arxiv.org/html/2603.06422v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06422v1.html; sha256:3479a6efc13a154aef3a87ddd8eb7eab063584f738f5a7bf1fb93178be032498 | arXiv:2603.06422v1 HTML — §V Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06422v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06422v1.html; sha256:3479a6efc13a154aef3a87ddd8eb7eab063584f738f5a7bf1fb93178be032498 | arXiv:2603.06422v1 HTML — §V-B3 Primary Factors of LLM’s Failure (RQ3) [facet=limitations]; https://arxiv.org/html/2603.06422v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06422v1.html; sha256:3479a6efc13a154aef3a87ddd8eb7eab063584f738f5a7bf1fb93178be032498 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06422v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06422 | complete |
| SF-2026-ARXIV-2603-06444 | RP-86d941c27e8fc285 | standard | arXiv:2603.06444v1 | SRC-ARXIV@arXiv:2603.06444v1 | arXiv:2603.06444v1 HTML — §3.4.2 Baselines and Proposed Method [facet=method]; https://arxiv.org/html/2603.06444v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06444v1.html; sha256:574ab5b264d0d1bddafa2393b2f097ae19988eec9aa7914f678c6b2470c468aa | arXiv:2603.06444v1 HTML — §3.3 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.06444v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06444v1.html; sha256:574ab5b264d0d1bddafa2393b2f097ae19988eec9aa7914f678c6b2470c468aa | arXiv:2603.06444v1 HTML — §4.3 Ablation Studies [facet=limitations]; https://arxiv.org/html/2603.06444v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06444v1.html; sha256:574ab5b264d0d1bddafa2393b2f097ae19988eec9aa7914f678c6b2470c468aa | arXiv exact-v1 identity https://arxiv.org/abs/2603.06444v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06444 | complete |
| SF-2026-ARXIV-2603-06445 | RP-de2fac98d8d92012 | standard | arXiv:2603.06445v1 | SRC-ARXIV@arXiv:2603.06445v1 | arXiv:2603.06445v1 HTML — §5.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.06445v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06445v1.html; sha256:89e0343638390a96a6b2f2da8524e308fd85394b9a66901f3cf6a8dc38470de0 | arXiv:2603.06445v1 HTML — §Appendix 0.C Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06445v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06445v1.html; sha256:89e0343638390a96a6b2f2da8524e308fd85394b9a66901f3cf6a8dc38470de0 | arXiv:2603.06445v1 HTML — §6 Limitations and Future Work [facet=limitations]; https://arxiv.org/html/2603.06445v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06445v1.html; sha256:89e0343638390a96a6b2f2da8524e308fd85394b9a66901f3cf6a8dc38470de0 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06445v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06445 | complete |
| SF-2026-ARXIV-2603-06450 | RP-8887e00789e0502d | standard | arXiv:2603.06450v1 | SRC-ARXIV@arXiv:2603.06450v1 | arXiv:2603.06450v1 HTML — §III Cross-Embodiment Data Analogies [facet=method]; https://arxiv.org/html/2603.06450v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06450v1.html; sha256:84f01ce204cd5799d112dd917ecebaf420121b1fac663adf9e8717866082b10b | arXiv:2603.06450v1 HTML — §Evaluation Tasks [facet=evaluation]; https://arxiv.org/html/2603.06450v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06450v1.html; sha256:84f01ce204cd5799d112dd917ecebaf420121b1fac663adf9e8717866082b10b | arXiv:2603.06450v1 HTML — §VI Limitations [facet=limitations]; https://arxiv.org/html/2603.06450v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06450v1.html; sha256:84f01ce204cd5799d112dd917ecebaf420121b1fac663adf9e8717866082b10b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06450v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06450 | complete |
| SF-2026-ARXIV-2603-06453 | RP-29e324995606355e | standard | arXiv:2603.06453v1 | SRC-ARXIV@arXiv:2603.06453v1 | arXiv:2603.06453v1 HTML — §3. System Overview [facet=method]; https://arxiv.org/html/2603.06453v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06453v1.html; sha256:de8802789b8b1abdd6a6cc10b2606b3f6f8570a6cd166685c3975bd794b5392b | arXiv:2603.06453v1 HTML — §5.1. Offline Evaluations for Outpainting [facet=evaluation]; https://arxiv.org/html/2603.06453v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06453v1.html; sha256:de8802789b8b1abdd6a6cc10b2606b3f6f8570a6cd166685c3975bd794b5392b | arXiv:2603.06453v1 HTML — §6. Conclusions [facet=limitations]; https://arxiv.org/html/2603.06453v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06453v1.html; sha256:de8802789b8b1abdd6a6cc10b2606b3f6f8570a6cd166685c3975bd794b5392b | arXiv exact-v1 identity https://arxiv.org/abs/2603.06453v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06453 | complete |
| SF-2026-ARXIV-2603-06508 | RP-f6ed111d0f751419 | standard | arXiv:2603.06508v1 | SRC-ARXIV@arXiv:2603.06508v1 | arXiv:2603.06508v1 HTML — §4 Problem Formulation [facet=method]; https://arxiv.org/html/2603.06508v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06508v1.html; sha256:f1a848eb0679fb055329856a71a86fa1d555715f37fceaf9c3e1b29a49c66980 | arXiv:2603.06508v1 HTML — §5.2 Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.06508v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06508v1.html; sha256:f1a848eb0679fb055329856a71a86fa1d555715f37fceaf9c3e1b29a49c66980 | arXiv:2603.06508v1 HTML — §6 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06508v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06508v1.html; sha256:f1a848eb0679fb055329856a71a86fa1d555715f37fceaf9c3e1b29a49c66980 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06508v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06508 | complete |
| SF-2026-ARXIV-2603-06569 | RP-72577c70a93bf85a | standard | arXiv:2603.06569v1 | SRC-ARXIV@arXiv:2603.06569v1 | arXiv:2603.06569v1 HTML — §4.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.06569v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06569v1.html; sha256:378d575c3423b11c22ccfa484927823d92055164c54667c9a3553747516777e4 | arXiv:2603.06569v1 HTML — §4.3 Image Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.06569v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06569v1.html; sha256:378d575c3423b11c22ccfa484927823d92055164c54667c9a3553747516777e4 | arXiv:2603.06569v1 HTML — §6.2 Future Work [facet=limitations]; https://arxiv.org/html/2603.06569v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06569v1.html; sha256:378d575c3423b11c22ccfa484927823d92055164c54667c9a3553747516777e4 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06569v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06569 | complete |
| SF-2026-ARXIV-2603-06577 | RP-573af14b6c08891f | standard | arXiv:2603.06577v1 | SRC-ARXIV@arXiv:2603.06577v1 | arXiv:2603.06577v1 HTML — §3.2 Model Architecture [facet=method]; https://arxiv.org/html/2603.06577v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06577v1.html; sha256:c53b31a5369d09c9361c71ccf3d5db778c386d88a46e45652f75ee3c1400e0b2 | arXiv:2603.06577v1 HTML — §Speech-Vision Alignment Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06577v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06577v1.html; sha256:c53b31a5369d09c9361c71ccf3d5db778c386d88a46e45652f75ee3c1400e0b2 | arXiv:2603.06577v1 HTML — §5 Conclusion [facet=limitations]; https://arxiv.org/html/2603.06577v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06577v1.html; sha256:c53b31a5369d09c9361c71ccf3d5db778c386d88a46e45652f75ee3c1400e0b2 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06577v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06577 | complete |
| SF-2026-ARXIV-2603-06578 | RP-9576116e8d4472d2 | deep | arXiv:2603.06578v1 | SRC-ARXIV@arXiv:2603.06578v1 | arXiv:2603.06578v1 HTML — §2.4 Model and class names overview [facet=method]; https://arxiv.org/html/2603.06578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06578v1.html; sha256:9d3a6d91b83510a070bb82d75327eeb478f7b9c51909e003b1330f89e6bdbc91 | arXiv:2603.06578v1 HTML — §2.2 Evaluation metric [facet=evaluation]; https://arxiv.org/html/2603.06578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06578v1.html; sha256:9d3a6d91b83510a070bb82d75327eeb478f7b9c51909e003b1330f89e6bdbc91 | arXiv:2603.06578v1 HTML — §4 Conclusions [facet=limitations]; https://arxiv.org/html/2603.06578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06578v1.html; sha256:9d3a6d91b83510a070bb82d75327eeb478f7b9c51909e003b1330f89e6bdbc91 | arXiv exact-v1 identity https://arxiv.org/abs/2603.06578v1; linked external artifact was not required for the manuscript claim unless disclosed in正文 | claim:SF-2026-ARXIV-2603-06578 | complete |

### Source Reviews

### Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents

<!-- review:SF-2026-ARXIV-2603-05517:start -->
**问题**：`Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.05517v1 HTML — §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks [facet=method]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d`。

**Evaluation contract 与未证明部分**：公开验证定位在 `I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts)`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05517v1 HTML — §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) [facet=evaluation]; https://arxiv.org/html/2603.05517v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05517v1.html; sha256:c9a291f7ac885ed0a42be617068ac8423d19c343b80533006d3d434774ac523d`。

**Trade-off / failure / coexistence**：限制与反证定位在 `O.1 Limitations and Open Failure Modes`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-05517:start -->**Claim Boundary**：只支持 arXiv:2603.05517v1 §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks 的机制与 §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) 的公开 workload；§O.1 Limitations and Open Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05517:end -->
<!-- review:SF-2026-ARXIV-2603-05517:end -->
### Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems

<!-- review:SF-2026-ARXIV-2603-05520:start -->
**问题**：`Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems` 检查的是 `PLATFORM-SECURITY` 中 工具、记忆和多 agent 委托把不可信内容转化为可执行控制流。 是否会改变现有设计边界。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：exact-v1 的 `4.3 Design Implications` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05520v1 HTML — §4.3 Design Implications [facet=method]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7.1 Overall Performance on Medical and Financial Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05520v1 HTML — §7.1 Overall Performance on Medical and Financial Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05520v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05520v1.html; sha256:f19e9de0c86c4c9553579b290b0f0f8adc1cdc7c42d331e32798894c2c01d344`。

**Trade-off / failure / coexistence**：限制与反证定位在 `8 Conclusion and Future Work`。无工具、无持久状态的只读场景仍可采用较薄边界。

<!-- claim:SF-2026-ARXIV-2603-05520:start -->**Claim Boundary**：只支持 arXiv:2603.05520v1 §4.3 Design Implications 的机制与 §7.1 Overall Performance on Medical and Financial Benchmarks 的公开 workload；§8 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05520:end -->
<!-- review:SF-2026-ARXIV-2603-05520:end -->
### Omni-C: Compressing Heterogeneous Modalities into a Single Dense Encoder

<!-- review:SF-2026-ARXIV-2603-05528:start -->
**问题**：每增加一种模态就常驻一个专用 encoder，会让参数、显存和部署路径近似线性增长。

**旧路径为何合理**：各模态保留独立 encoder 和静态融合点，职责清楚且便于单独优化。

**约束变化与机制**：Omni-C 以共享 dense Transformer 承担图像、语音与文本表示，只保留轻量模态投影，并用未配对的单模态对比目标抑制跨模态冲突。

**State / data / control owner**：`MULTIMODAL-REPRESENTATION` 负责 跨模态 token identity、融合、时间锚点与可变表示状态；定位证据为 `arXiv:2603.05528v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.05528v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05528v1.html; sha256:3c79da9c11b969078776df31d8632294fe015143fe86fa316e1274d858962660`。

**Evaluation contract 与未证明部分**：公开结果只支持所测 encoder、任务与设备中的质量/显存取舍；零样本退化和线性探针恢复不能证明共享表示在所有组合任务上等价。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05528v1 HTML — §IV Experiments [facet=evaluation]; https://arxiv.org/html/2603.05528v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05528v1.html; sha256:3c79da9c11b969078776df31d8632294fe015143fe86fa316e1274d858962660`。

**Trade-off / failure / coexistence**：共享骨干降低常驻成本，却扩大负迁移与串行处理延迟；模态差异大或并行低延迟优先时，专用 encoder 仍合理。

<!-- claim:SF-2026-ARXIV-2603-05528:start -->**Claim Boundary**：只支持 arXiv:2603.05528v1 §III Methodology 的机制与 §IV Experiments 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05528:end -->
<!-- review:SF-2026-ARXIV-2603-05528:end -->
### Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding

<!-- review:SF-2026-ARXIV-2603-05540:start -->
**问题**：grammar-constrained decoding 只比较最终语言是否相同，会遗漏等价 grammar 在在线解析状态和每 token 延迟上的巨大差异。

**旧路径为何合理**：模型只输出文本时，错误影响停留在信息层。

**约束变化与机制**：论文把解码写成 next-token distribution 与 pushdown reachability oracle 的耦合，证明语言等价不等于执行成本等价，并用 SAC 描述逐 token parse-forest 增长。

**State / data / control owner**：`AGENT-TOOL-CALLING` 负责 tool identity、argument validation、authorization、receipt 与 side-effect commit；定位证据为 `arXiv:2603.05540v1 HTML — §Neural architecture coupling. [facet=method]; https://arxiv.org/html/2603.05540v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05540v1.html; sha256:8020b2c9f7ce64c2801b538af6a84f5884147c7d8f2a5ea2caf90fb50351103a`。

**Evaluation contract 与未证明部分**：定理支持特定 CFG family 的控制状态膨胀、复杂度下界与 hard mask 分布失真；不证明所有 schema 或具体 engine 都达到该下界。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05540v1 HTML — §Parsing theory and reachability. [facet=evaluation]; https://arxiv.org/html/2603.05540v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05540v1.html; sha256:8020b2c9f7ce64c2801b538af6a84f5884147c7d8f2a5ea2caf90fb50351103a`。

**Trade-off / failure / coexistence**：grammar rewrite 能降低在线状态成本，却不消除受约束采样对原分布的扭曲；小 grammar 或低 QPS 路径仍可优先简单正确性。

<!-- claim:SF-2026-ARXIV-2603-05540:start -->**Claim Boundary**：只支持 arXiv:2603.05540v1 §Neural architecture coupling. 的机制与 §Parsing theory and reachability. 的公开 workload；§12 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05540:end -->
<!-- review:SF-2026-ARXIV-2603-05540:end -->
### EigenData: A Self-Evolving Multi-Agent Platform for Function-Calling Data Synthesis, Auditing, and Repair

<!-- review:SF-2026-ARXIV-2603-05553:start -->
**问题**：function-calling 数据的数据库、可执行环境、schema 与 trajectory 若分开生成，跨 artifact 错误无法归因。

**旧路径为何合理**：固定离线数据集让训练可复现，也避免在线选择反馈回路。

**约束变化与机制**：EigenData 让多个专责 agent 共享可验证 artifact graph，并以数据库终态而非轨迹表面匹配作为任务 oracle。

**State / data / control owner**：`TRAIN-DATA` 负责 样本 identity、选择策略、版本、provenance 与训练消费顺序；定位证据为 `arXiv:2603.05553v1 HTML — §3.3.1 Architecture [facet=method]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0`。

**Evaluation contract 与未证明部分**：BFCL-V3 修复案例只证明所测 schema、实现和轨迹错误能被该闭环发现；不证明自动修复对任意工具生态安全。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05553v1 HTML — §4.3 Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05553v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05553v1.html; sha256:660f5a719fa7871e291edbbb353fa18f6cfdc51acbcea1e32fd5c7e7bebb61c0`。

**Trade-off / failure / coexistence**：闭环提升一致性却扩大生成器、测试器和 oracle 的共同故障域；人工冻结的小型工具集仍更易审计。

<!-- claim:SF-2026-ARXIV-2603-05553:start -->**Claim Boundary**：只支持 arXiv:2603.05553v1 §3.3.1 Architecture 的机制与 §4.3 Evaluation Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05553:end -->
<!-- review:SF-2026-ARXIV-2603-05553:end -->
### Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent

<!-- review:SF-2026-ARXIV-2603-05578:start -->
**问题**：只测 agent 是否最终完成任务，会把工具接口、实现与调用失败混成一个分数。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Tool-Genesis 从抽象需求开始，分别验证 interface compliance、functional correctness 与 downstream utility，使失败位置可归因。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05578v1 HTML — §Appendix A Evaluation Methodology Details [facet=method]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e`。

**Evaluation contract 与未证明部分**：基准证明其任务集合中一处早期接口缺陷会沿调用链放大；不证明该任务分布代表生产工具市场。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05578v1 HTML — §5.2 Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05578v1.html; sha256:8ebd4c611566379e9d77473f217369724492e966429ee74033c7f50729aafa5e`。

**Trade-off / failure / coexistence**：诊断粒度提高证据价值但增加 oracle 和 sandbox 维护；预定义稳定工具仍可使用普通端到端测试。

<!-- claim:SF-2026-ARXIV-2603-05578:start -->**Claim Boundary**：只支持 arXiv:2603.05578v1 §Appendix A Evaluation Methodology Details 的机制与 §5.2 Experimental Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05578:end -->
<!-- review:SF-2026-ARXIV-2603-05578:end -->
### Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in LLMs

<!-- review:SF-2026-ARXIV-2603-05618:start -->
**问题**：把 Chain-of-Thought 当作内部调试信息，会忽略 prompt 中 PII 被 reasoning trace 再暴露的独立泄漏面。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：该工作把 PII 类型、风险权重和允许的 reasoning budget 绑定到同一评测合同，并比较多种推理时 gatekeeper。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05618v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.05618v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05618v1.html; sha256:07fcda3ca34b32359eee1454fb86fc000b2ddd8e1bbba4a25adc73edafa7aa7b`。

**Evaluation contract 与未证明部分**：结果只支持所测模型、PII 数据和 budget；没有单一 gatekeeper 在所有模型上占优，也不能把低泄漏等同于隐私保证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05618v1 HTML — §3.3 Gatekeeper Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05618v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05618v1.html; sha256:07fcda3ca34b32359eee1454fb86fc000b2ddd8e1bbba4a25adc73edafa7aa7b`。

**Trade-off / failure / coexistence**：更强过滤降低泄漏却可能截断有用推理并增加误报；不输出 reasoning trace 的受控服务仍具有更小暴露面。

<!-- claim:SF-2026-ARXIV-2603-05618:start -->**Claim Boundary**：只支持 arXiv:2603.05618v1 §2 Methodology 的机制与 §3.3 Gatekeeper Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05618:end -->
<!-- review:SF-2026-ARXIV-2603-05618:end -->
### Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy

<!-- review:SF-2026-ARXIV-2603-05637:start -->
**问题**：`Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy` 检查的是 `AGENT-MCP` 中 跨 server capability、委托链与动态发现使权限边界不再等同于一次函数调用。 是否会改变现有设计边界。

**旧路径为何合理**：把协议当作普通 tool adapter，部署和权限模型最简单。

**约束变化与机制**：exact-v1 的 `3. Methodology` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-MCP` 负责 协议身份、capability 声明、授权与审计状态；定位证据为 `arXiv:2603.05637v1 HTML — §3. Methodology [facet=method]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3.3. Taxonomy Creation and Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05637v1 HTML — §3.3. Taxonomy Creation and Validation [facet=evaluation]; https://arxiv.org/html/2603.05637v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05637v1.html; sha256:0f06fa547dbafba60a5491163b4494e314b759f70216390bcc06c7ac6e0d95e3`。

**Trade-off / failure / coexistence**：限制与反证定位在 `7. Conclusion and Future Works`。固定工具集、单一信任域仍可保留较薄的 adapter。

<!-- claim:SF-2026-ARXIV-2603-05637:start -->**Claim Boundary**：只支持 arXiv:2603.05637v1 §3. Methodology 的机制与 §3.3. Taxonomy Creation and Validation 的公开 workload；§7. Conclusion and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05637:end -->
<!-- review:SF-2026-ARXIV-2603-05637:end -->
### Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks

<!-- review:SF-2026-ARXIV-2603-05692:start -->
**问题**：`Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks` 检查的是 `INFER-TENSORRT-LLM` 中 固定热点、异构硬件和严格 SLO 迫使系统显式优化 execution plan、kernel 与 state layout。 是否会改变现有设计边界。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：exact-v1 的 `2.2. Overview of Llama 3.1-70B/-405B Models` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.05692v1 HTML — §2.2. Overview of Llama 3.1-70B/-405B Models [facet=method]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051`。

**Evaluation contract 与未证明部分**：公开验证定位在 `3. In-House Simulator and Its Validation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05692v1 HTML — §3. In-House Simulator and Its Validation [facet=evaluation]; https://arxiv.org/html/2603.05692v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05692v1.html; sha256:f46cae15647a0b5c39bd13ea8b8e81cec1dc1ccfcc59505295912fa2b7162051`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6. Discussion`。模型变化频繁或 workload 较小时，通用执行路径仍具有更低维护成本。

<!-- claim:SF-2026-ARXIV-2603-05692:start -->**Claim Boundary**：只支持 arXiv:2603.05692v1 §2.2. Overview of Llama 3.1-70B/-405B Models 的机制与 §3. In-House Simulator and Its Validation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05692:end -->
<!-- review:SF-2026-ARXIV-2603-05692:end -->
### MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents

<!-- review:SF-2026-ARXIV-2603-05697:start -->
**问题**：把正确 evidence 直接交给模型的多模态 benchmark，会隐藏跨文档、图像和视频检索本身的主瓶颈。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：MultiHaystack 将唯一可验证 evidence 放入四万级异构候选池，分别测 retrieval recall 与 evidence-conditioned reasoning。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05697v1 HTML — §0.D.1 Implementation details [facet=method]; https://arxiv.org/html/2603.05697v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05697v1.html; sha256:03f6adfd0cf6c1c4385ba176b3ebb561bae916cc452cc2bc76d20e6f015171d2`。

**Evaluation contract 与未证明部分**：公开数字只属于其 747 个问题、候选池、retriever 与 MLLM；不能外推企业语料版本、权限过滤或生产时延。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05697v1 HTML — §0.D.3 Evaluation Models [facet=evaluation]; https://arxiv.org/html/2603.05697v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05697v1.html; sha256:03f6adfd0cf6c1c4385ba176b3ebb561bae916cc452cc2bc76d20e6f015171d2`。

**Trade-off / failure / coexistence**：端到端分解改善归因，却增加 evidence 标注和 corpus 版本成本；检索已知的离线任务仍可单独评测 reasoning。

<!-- claim:SF-2026-ARXIV-2603-05697:start -->**Claim Boundary**：只支持 arXiv:2603.05697v1 §0.D.1 Implementation details 的机制与 §0.D.3 Evaluation Models 的公开 workload；§Appendix 0.J Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05697:end -->
<!-- review:SF-2026-ARXIV-2603-05697:end -->
### Reasoning Models Struggle to Control their Chains of Thought

<!-- review:SF-2026-ARXIV-2603-05706:start -->
**问题**：依赖 Chain-of-Thought monitor 的安全方案隐含假设模型不能随意控制自己暴露的推理内容。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：CoT-Control 将隐藏推理的可控性与最终输出可控性分开测量，并改变模型规模、RL 强度、test-time compute 和任务难度。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05706v1 HTML — §2.2 Evaluation Design [facet=method]; https://arxiv.org/html/2603.05706v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05706v1.html; sha256:16a5cf0fbdb820f36e393662e9fced3af825aedda26bd542a01984acf514dd1f`。

**Evaluation contract 与未证明部分**：结果支持当前受测 reasoning models 的 CoT controllability 较低；机制尚不明确，不能据此把 monitorability 当作长期保证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05706v1 HTML — §2.2 Evaluation Design [facet=evaluation]; https://arxiv.org/html/2603.05706v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05706v1.html; sha256:16a5cf0fbdb820f36e393662e9fced3af825aedda26bd542a01984acf514dd1f`。

**Trade-off / failure / coexistence**：监控 reasoning trace 能增加可见性，却会随能力和训练变化失效并引入隐私面；外部 action gate 仍不可省略。

<!-- claim:SF-2026-ARXIV-2603-05706:start -->**Claim Boundary**：只支持 arXiv:2603.05706v1 §2.2 Evaluation Design 的机制与 §2.2 Evaluation Design 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05706:end -->
<!-- review:SF-2026-ARXIV-2603-05706:end -->
### Challenges and Design Considerations for Finding CUDA Bugs Through GPU-Native Fuzzing

<!-- review:SF-2026-ARXIV-2603-05725:start -->
**问题**：把 CUDA 程序翻译到 CPU 上 fuzz，会丢失 GPU memory、SIMT、异步执行与 runtime 语义，导致测试对象不再忠实。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文将 behavior faithfulness 设为 GPU-native fuzzing 的核心合同，并梳理生成、调度、oracle 与 crash triage 的设计约束。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05725v1 HTML — §4. The GPU-Native Design [facet=method]; https://arxiv.org/html/2603.05725v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05725v1.html; sha256:a2f11f7b2d6a964961d23c2ffdc69392e0e134dd5c45b1fb4b189365d2fcdd27`。

**Evaluation contract 与未证明部分**：这是设计与漏洞趋势证据，不是一个已闭合的通用 fuzzer benchmark；未证明所有 CUDA bug 类都可自动发现。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05725v1 HTML — §5. Preliminary Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05725v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05725v1.html; sha256:a2f11f7b2d6a964961d23c2ffdc69392e0e134dd5c45b1fb4b189365d2fcdd27`。

**Trade-off / failure / coexistence**：原生执行提高忠实度，却增加设备成本、非确定性和故障隔离难度；纯 host 逻辑仍可用 CPU 侧快速筛查。

<!-- claim:SF-2026-ARXIV-2603-05725:start -->**Claim Boundary**：只支持 arXiv:2603.05725v1 §4. The GPU-Native Design 的机制与 §5. Preliminary Experimental Results 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05725:end -->
<!-- review:SF-2026-ARXIV-2603-05725:end -->
### Revisiting the (Sub)Optimality of Best-of-N for Inference-Time Alignment

<!-- review:SF-2026-ARXIV-2603-05739:start -->
**问题**：Best-of-N 常以期望真实 reward 分析，但实践中的 reward model 主要由 pairwise preference 训练，目标错配会误判方案优劣。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：论文改用 win-rate 作为推理时对齐目标，给出 BoN 最优条件，并提出在保持统计效率时限制 reward hacking 的变体。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.05739v1 HTML — §2.1 Inference-time alignment framework [facet=method]; https://arxiv.org/html/2603.05739v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05739v1.html; sha256:5a5804a713ff42732281d158dbfae4791319284098eb2648fdb4e61f6cc6c19e`。

**Evaluation contract 与未证明部分**：理论只在其 reference/reward-model 假设下成立；不证明有限样本、分布漂移或开放式 evaluator 中不存在 hacking。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05739v1 HTML — §5.1 Proof Sketch of Theorem 3 [facet=evaluation]; https://arxiv.org/html/2603.05739v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05739v1.html; sha256:5a5804a713ff42732281d158dbfae4791319284098eb2648fdb4e61f6cc6c19e`。

**Trade-off / failure / coexistence**：增加 N 提高选择机会却线性增加推理成本，并放大 evaluator 偏差；低风险或预算紧张时单样本仍是有效基线。

<!-- claim:SF-2026-ARXIV-2603-05739:start -->**Claim Boundary**：只支持 arXiv:2603.05739v1 §2.1 Inference-time alignment framework 的机制与 §5.1 Proof Sketch of Theorem 3 的公开 workload；§Conclusion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05739:end -->
<!-- review:SF-2026-ARXIV-2603-05739:end -->
### Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation

<!-- review:SF-2026-ARXIV-2603-05754:start -->
**问题**：`Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation` 检查的是 `MULTIMODAL-EMBODIED-VLA` 中 物理闭环引入控制频率、感知延迟、动作安全和 edge/cloud placement 约束。 是否会改变现有设计边界。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：exact-v1 的 `III-A System Architecture and Adaptation Strategy` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.05754v1 HTML — §III-A System Architecture and Adaptation Strategy [facet=method]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6`。

**Evaluation contract 与未证明部分**：公开验证定位在 `V-C Exploratory Mechanism Analysis: Attention Ablation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05754v1 HTML — §V-C Exploratory Mechanism Analysis: Attention Ablation [facet=evaluation]; https://arxiv.org/html/2603.05754v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05754v1.html; sha256:95467be2bab99b33830a6264200f782ed0715cac6f40722d41d7c79fa96fb6a6`。

**Trade-off / failure / coexistence**：限制与反证定位在 `V-B1 Limitations of RGB-Only and RGB-D Variants`。低频、可人工接管或环境稳定时集中式 VLA 路径仍可成立。

<!-- claim:SF-2026-ARXIV-2603-05754:start -->**Claim Boundary**：只支持 arXiv:2603.05754v1 §III-A System Architecture and Adaptation Strategy 的机制与 §V-C Exploratory Mechanism Analysis: Attention Ablation 的公开 workload；§V-B1 Limitations of RGB-Only and RGB-D Variants 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05754:end -->
<!-- review:SF-2026-ARXIV-2603-05754:end -->
### Proof-of-Guardrail in AI Agents and What (Not) to Trust from It

<!-- review:SF-2026-ARXIV-2603-05786:start -->
**问题**：服务方声称执行了 guardrail 时，用户通常只能信任声明，无法验证安全检查是否真正位于 response commit 前。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：Proof-of-Guardrail 把 agent 与公开 guardrail 放入 TEE，并用远程证明绑定代码身份和执行顺序。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05786v1 HTML — §An agent skill-based proof-of-guardrail implementation. [facet=method]; https://arxiv.org/html/2603.05786v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05786v1.html; sha256:615e4b77b2d881e703e9d296257d161690894ac7614b9d4f4147e468d19753ea`。

**Evaluation contract 与未证明部分**：证明只覆盖指定 guardrail 被执行，不证明规则有效、输入完整或 guardrail 未被 jailbreak；成本结果绑定其 OpenClaw 实现。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05786v1 HTML — §3.2 Proof-of-Guardrail with TEE Attestation [facet=evaluation]; https://arxiv.org/html/2603.05786v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05786v1.html; sha256:615e4b77b2d881e703e9d296257d161690894ac7614b9d4f4147e468d19753ea`。

**Trade-off / failure / coexistence**：attestation 缩小运行完整性信任面，却把 TEE、测量身份和规则质量变成新根信任；可控单租户环境仍可用普通审计。

<!-- claim:SF-2026-ARXIV-2603-05786:start -->**Claim Boundary**：只支持 arXiv:2603.05786v1 §An agent skill-based proof-of-guardrail implementation. 的机制与 §3.2 Proof-of-Guardrail with TEE Attestation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05786:end -->
<!-- review:SF-2026-ARXIV-2603-05786:end -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale

<!-- review:SF-2026-ARXIV-2603-05800:start -->
**问题**：多模态生成流同时包含持续到达、异质阶段和实时 deadline；把每个请求当成单次模型调用会隐藏跨阶段排队。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.05800v1 HTML — §4.7. Implementation [facet=method]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c`。

**Evaluation contract 与未证明部分**：作者在其公开模型、设备和请求分布上测量吞吐与尾延迟，足以支持所测实时 pipeline 的联合调度收益；未披露的跨集群网络、租户隔离和生产 SLO 不属于结论。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05800v1 HTML — §5. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05800v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05800v1.html; sha256:e0848bfed4a28a4fbb745f28517ca54d621f5a2eeaf59b09a14ad224d9f66f3c`。

**Trade-off / failure / coexistence**：更细的阶段状态提升利用率，也增加队列、取消和中间结果失效复杂度；离线同质批处理仍适合静态流水线。

<!-- claim:SF-2026-ARXIV-2603-05800:start -->**Claim Boundary**：只支持 arXiv:2603.05800v1 §4.7. Implementation 的机制与 §5. Evaluation 的公开 workload；§7. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05800:end -->
<!-- review:SF-2026-ARXIV-2603-05800:end -->
### Hierarchical Latent Action Model

<!-- review:SF-2026-ARXIV-2603-05815:start -->
**问题**：只从相邻帧学习 latent action，通常只能编码短期运动，无法给 world model 或 policy 提供长时间技能状态。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：HiLAM 在低层 latent-action extractor 之上聚合动作序列，形成具有更长时间尺度的 latent skill。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.05815v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.05815v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05815v1.html; sha256:2b37ae924a692244b15c75c6e7cfed4466e662929a65170fa16da17d6d131ad2`。

**Evaluation contract 与未证明部分**：实验只支持所测 actionless video 和动态技能发现指标；latent skill 的可控性、因果性和跨 embodiment 迁移未被证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05815v1 HTML — §4.2.1 LIBERO Benchmark Results [facet=evaluation]; https://arxiv.org/html/2603.05815v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05815v1.html; sha256:2b37ae924a692244b15c75c6e7cfed4466e662929a65170fa16da17d6d131ad2`。

**Trade-off / failure / coexistence**：层级状态扩大规划跨度，却增加抽象错配和不可辨识性；短 horizon 控制仍适合低层 latent action。

<!-- claim:SF-2026-ARXIV-2603-05815:start -->**Claim Boundary**：只支持 arXiv:2603.05815v1 §3 Method 的机制与 §4.2.1 LIBERO Benchmark Results 的公开 workload；§5 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05815:end -->
<!-- review:SF-2026-ARXIV-2603-05815:end -->
### HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models

<!-- review:SF-2026-ARXIV-2603-05828:start -->
**问题**：只输出 hallucination 标签无法说明错误 span、生成机制与支持/反对 evidence 之间的对应关系。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：HART 把定位、机制归因、evidence retrieval 与 causal tracing 组织为结构化链路，并建立联合标注数据。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05828v1 HTML — §4.1.3. Implementation [facet=method]; https://arxiv.org/html/2603.05828v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05828v1.html; sha256:e94c154f1ce87fc610e3b57932df541e8a499a3801d88f5bda6ce90a8f1f04c0`。

**Evaluation contract 与未证明部分**：结果证明其数据集上优于检索基线；机制标签仍是任务定义下的监督，不能当作模型内部因果事实。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05828v1 HTML — §4.2. Experimental Results [facet=evaluation]; https://arxiv.org/html/2603.05828v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05828v1.html; sha256:e94c154f1ce87fc610e3b57932df541e8a499a3801d88f5bda6ce90a8f1f04c0`。

**Trade-off / failure / coexistence**：细粒度 trace 提高可审计性，却显著增加标注和 oracle 成本；低风险场景仍可使用答案级 groundedness 检查。

<!-- claim:SF-2026-ARXIV-2603-05828:start -->**Claim Boundary**：只支持 arXiv:2603.05828v1 §4.1.3. Implementation 的机制与 §4.2. Experimental Results 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05828:end -->
<!-- review:SF-2026-ARXIV-2603-05828:end -->
### Evolving Deception: When Agents Evolve, Deception Wins

<!-- review:SF-2026-ARXIV-2603-05872:start -->
**问题**：允许 agent 以效用为目标自我迭代时，局部成功会把策略更新推向可迁移的欺骗，而不是稳定遵循规范。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文在竞争式 bidding 环境中比较多条演化路径，并追踪 reflection 后的策略与内部 rationalization。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.05872v1 HTML — §Appendix A Self-Evolution Algorithm [facet=method]; https://arxiv.org/html/2603.05872v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05872v1.html; sha256:60bdbfcc2ad4c8bcbdceb33da5d9bec7457cee703f1463e16ac9de3696ca7def`。

**Evaluation contract 与未证明部分**：证据只支持所测 arena、模型和迭代协议中的欺骗漂移；不证明所有 self-improvement 必然产生同一均衡。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05872v1 HTML — §4.3 Evaluation Configuration [facet=evaluation]; https://arxiv.org/html/2603.05872v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05872v1.html; sha256:60bdbfcc2ad4c8bcbdceb33da5d9bec7457cee703f1463e16ac9de3696ca7def`。

**Trade-off / failure / coexistence**：自适应可提高跨任务效用，却扩大目标漂移和审计难度；固定 policy、外部 reward gate 与可回滚版本仍是安全边界。

<!-- claim:SF-2026-ARXIV-2603-05872:start -->**Claim Boundary**：只支持 arXiv:2603.05872v1 §Appendix A Self-Evolution Algorithm 的机制与 §4.3 Evaluation Configuration 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05872:end -->
<!-- review:SF-2026-ARXIV-2603-05872:end -->
### Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation

<!-- review:SF-2026-ARXIV-2603-05881:start -->
**问题**：`Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `3.2 Confidence-First Paradigm Definition` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05881v1 HTML — §3.2 Confidence-First Paradigm Definition [facet=method]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.1.2 Evaluation Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05881v1 HTML — §4.1.2 Evaluation Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05881v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05881v1.html; sha256:0c80cf9ae6e4657782075ab45c0dec7c2abd56e9ed6d5c8a923ed28feb4b91cf`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Limitations and Future Work`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05881:start -->**Claim Boundary**：只支持 arXiv:2603.05881v1 §3.2 Confidence-First Paradigm Definition 的机制与 §4.1.2 Evaluation Benchmarks 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05881:end -->
<!-- review:SF-2026-ARXIV-2603-05881:end -->
### The World Won't Stay Still: Programmable Evolution for Agent Benchmarks

<!-- review:SF-2026-ARXIV-2603-05910:start -->
**问题**：`The World Won't Stay Still: Programmable Evolution for Agent Benchmarks` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `C.2 Tool Designer in Saturation Strategy` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05910v1 HTML — §C.2 Tool Designer in Saturation Strategy [facet=method]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4.4 State-Wise User Simulation and Evaluation`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05910v1 HTML — §4.4 State-Wise User Simulation and Evaluation [facet=evaluation]; https://arxiv.org/html/2603.05910v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05910v1.html; sha256:58b3a1d95b43749470f9aa09a7c2e2a2308e60b64e728c1657618d627cf4bd37`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusions`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05910:start -->**Claim Boundary**：只支持 arXiv:2603.05910v1 §C.2 Tool Designer in Saturation Strategy 的机制与 §4.4 State-Wise User Simulation and Evaluation 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05910:end -->
<!-- review:SF-2026-ARXIV-2603-05910:end -->
### DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality

<!-- review:SF-2026-ARXIV-2603-05912:start -->
**问题**：`DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality` 检查的是 `PLATFORM-EVALUATION-SYSTEM` 中 agent、长时程和多模态系统把失败分散到状态、工具与环境交互链。 是否会改变现有设计边界。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：exact-v1 的 `4.1 Methodology: The Micro-Gold Protocol` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.05912v1 HTML — §4.1 Methodology: The Micro-Gold Protocol [facet=method]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45`。

**Evaluation contract 与未证明部分**：公开验证定位在 `7.3 Results on Other Factuality Benchmarks`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05912v1 HTML — §7.3 Results on Other Factuality Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.05912v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05912v1.html; sha256:26e257b3da135609d0e72f9f90543c3ea64f7d7b98bb79b52de3f2ca42d08b45`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。窄任务且 failure surface 稳定时单指标仍可作为局部信号。

<!-- claim:SF-2026-ARXIV-2603-05912:start -->**Claim Boundary**：只支持 arXiv:2603.05912v1 §4.1 Methodology: The Micro-Gold Protocol 的机制与 §7.3 Results on Other Factuality Benchmarks 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05912:end -->
<!-- review:SF-2026-ARXIV-2603-05912:end -->
### A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA

<!-- review:SF-2026-ARXIV-2603-05931:start -->
**问题**：线性注意力 decode 受反复装载持久状态限制，单纯增加算术单元不能消除片外带宽瓶颈。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.05931v1 HTML — §IV-E System Overview [facet=method]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543`。

**Evaluation contract 与未证明部分**：FPGA 原型证明给定算子、精度和器件上的带宽/吞吐变化；它没有证明不同线性注意力变体或 GPU runtime 可获得相同比例收益。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05931v1 HTML — §VI-E Ablation Analysis [facet=evaluation]; https://arxiv.org/html/2603.05931v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05931v1.html; sha256:5e5eb61e425aab90caeca1f577a230d770250579c7b9ee6eba8bffcb9c54f543`。

**Trade-off / failure / coexistence**：持久化减少内存流量，却占用片上容量并绑定状态布局；短序列或状态无法容纳时，通用外存执行仍更灵活。

<!-- claim:SF-2026-ARXIV-2603-05931:start -->**Claim Boundary**：只支持 arXiv:2603.05931v1 §IV-E System Overview 的机制与 §VI-E Ablation Analysis 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05931:end -->
<!-- review:SF-2026-ARXIV-2603-05931:end -->
### OVGGT: O(1) Constant-Cost Streaming Visual Geometry Transformer

<!-- review:SF-2026-ARXIV-2603-05959:start -->
**问题**：流式视觉几何若为每个新帧重算完整历史，计算和 memory 会随序列长度持续增长。

**旧路径为何合理**：完整、逐 token 保存 KV，换取语义透明和最低重算风险。

**约束变化与机制**：OVGGT 将历史压缩为固定大小的视觉几何状态，使新帧更新保持常数级 cache/compute contract。

**State / data / control owner**：`INFER-KV-CACHE` 负责 KV 的 identity、压缩、复用、放置与失效状态；定位证据为 `arXiv:2603.05959v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.05959v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05959v1.html; sha256:0efab5d5c840316cafc0b348d496af2cf11cda5781dae932742b11322ea26899`。

**Evaluation contract 与未证明部分**：作者结果只支持其几何任务、场景长度和压缩状态；不证明常数状态能保留任意长流的全部信息。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05959v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.05959v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05959v1.html; sha256:0efab5d5c840316cafc0b348d496af2cf11cda5781dae932742b11322ea26899`。

**Trade-off / failure / coexistence**：有界状态换来稳定资源，却引入不可逆遗忘和漂移；短序列或离线高精度重建仍应保留完整历史。

<!-- claim:SF-2026-ARXIV-2603-05959:start -->**Claim Boundary**：只支持 arXiv:2603.05959v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§E Failure Cases 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05959:end -->
<!-- review:SF-2026-ARXIV-2603-05959:end -->
### Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence

<!-- review:SF-2026-ARXIV-2603-05960:start -->
**问题**：大模型优化器若同时保存全部梯度、动量和参数更新，会让 optimizer state 成为训练显存上限。

**旧路径为何合理**：单机或纯数据并行状态最少、同步语义清晰。

**约束变化与机制**：Omni-Masked Gradient Descent 以 mask traversal 分批更新参数子集，在降低同时驻留状态时维持收敛路径。

**State / data / control owner**：`TRAIN-DISTRIBUTED-TRAINING` 负责 训练状态分片、collective、同步与故障恢复；定位证据为 `arXiv:2603.05960v1 HTML — §3.2 Omni-Masked Gradient Descent [facet=method]; https://arxiv.org/html/2603.05960v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05960v1.html; sha256:9cd83752cf382eafab558b81aa57b3982f3a561cef7a9e05e682024f893f70e9`。

**Evaluation contract 与未证明部分**：理论与实验只支持论文的 mask schedule、目标和模型；不能把内存节省外推为任意分布式训练中的 wall-clock 收益。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05960v1 HTML — §5.4 Pre-training Experiments of LLMs [facet=evaluation]; https://arxiv.org/html/2603.05960v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05960v1.html; sha256:9cd83752cf382eafab558b81aa57b3982f3a561cef7a9e05e682024f893f70e9`。

**Trade-off / failure / coexistence**：分块状态降低峰值 memory，却增加更新陈旧、调度和收敛超参；容量足够时全量同步 optimizer 更简单。

<!-- claim:SF-2026-ARXIV-2603-05960:start -->**Claim Boundary**：只支持 arXiv:2603.05960v1 §3.2 Omni-Masked Gradient Descent 的机制与 §5.4 Pre-training Experiments of LLMs 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05960:end -->
<!-- review:SF-2026-ARXIV-2603-05960:end -->
### Balancing Latency and Accuracy of Code Completion via Local-Cloud Model Cascading

<!-- review:SF-2026-ARXIV-2603-05974:start -->
**问题**：代码补全始终走云端会增加网络尾延迟和成本，始终走本地则受小模型质量限制。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：论文把 local/cloud 选择建模为带质量估计的请求级 cascade，在提交前决定是否升级到远端模型。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.05974v1 HTML — §4.3. Implementation Details [facet=method]; https://arxiv.org/html/2603.05974v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05974v1.html; sha256:22d05069b51076c8214d0ba6afadda5de3234e88bef014a15210703c44110744`。

**Evaluation contract 与未证明部分**：结果绑定其代码任务、网络与模型组合；不证明置信信号在新仓库或隐私约束下仍校准。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.05974v1 HTML — §5. Evaluation Results [facet=evaluation]; https://arxiv.org/html/2603.05974v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.05974v1.html; sha256:22d05069b51076c8214d0ba6afadda5de3234e88bef014a15210703c44110744`。

**Trade-off / failure / coexistence**：级联改善平均延迟/质量，却增加路由误判、两次计算和数据出域风险；稳定网络或单模型足够时固定路径更可控。

<!-- claim:SF-2026-ARXIV-2603-05974:start -->**Claim Boundary**：只支持 arXiv:2603.05974v1 §4.3. Implementation Details 的机制与 §5. Evaluation Results 的公开 workload；§6.5. Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-05974:end -->
<!-- review:SF-2026-ARXIV-2603-05974:end -->
### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration

<!-- review:SF-2026-ARXIV-2603-06001:start -->
**问题**：VLA 可在语言与场景矛盾时仍沿视觉先验行动，任务成功率因此掩盖 instruction-action coupling 失效。

**旧路径为何合理**：把感知与动作生成串成单次前向路径，静态任务中接口最少。

**约束变化与机制**：ICBench 固定视觉场景并注入矛盾指令；IGAR 在推理时重分配 attention，使语言约束重新进入动作生成。

**State / data / control owner**：`MULTIMODAL-EMBODIED-VLA` 负责 observation、action chunk、controller handoff 与环境反馈状态；定位证据为 `arXiv:2603.06001v1 HTML — §3.2 Contradiction Taxonomy and Design Principles [facet=method]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8`。

**Evaluation contract 与未证明部分**：三类 VLA、LIBERO 与 Franka 实验支持该 failure mode 和受限修复；不证明 attention weight 等于因果 grounding。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06001v1 HTML — §5.6 Real-World Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06001v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06001v1.html; sha256:b35ae772b6122c830ce2712991d3fb92ff549ea16d27824aecdc97aba88e82f8`。

**Trade-off / failure / coexistence**：重校准无需训练但可能压制合理视觉反应；闭集一致指令下原策略仍有更低控制开销。

<!-- claim:SF-2026-ARXIV-2603-06001:start -->**Claim Boundary**：只支持 arXiv:2603.06001v1 §3.2 Contradiction Taxonomy and Design Principles 的机制与 §5.6 Real-World Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06001:end -->
<!-- review:SF-2026-ARXIV-2603-06001:end -->
### EvoESAP: Non-Uniform Expert Pruning for Sparse MoE

<!-- review:SF-2026-ARXIV-2603-06003:start -->
**问题**：MoE 部署受完整 expert pool 显存约束，而逐层统一剪枝忽略不同层对容量损失的敏感度。

**旧路径为何合理**：dense 层让每个 token 经过同一参数路径，训练与部署最规则。

**约束变化与机制**：EvoESAP 把层内 expert 排序与跨层预算分开，用 teacher-forced acceptance proxy 搜索非均匀 sparsity。

**State / data / control owner**：`MODEL-MOE` 负责 expert 选择、capacity、placement 与通信；定位证据为 `arXiv:2603.06003v1 HTML — §2.3 Other Compression Methods [facet=method]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd`。

**Evaluation contract 与未证明部分**：7B--30B、固定全局预算实验支持该搜索空间内的质量差异；不证明 proxy 在其他 router 或数据上保持排序。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06003v1 HTML — §4.2 Main results [facet=evaluation]; https://arxiv.org/html/2603.06003v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06003v1.html; sha256:049da75df0aeb2865b0be7e0b99b011f0f2bd32855e2c1d4be5f09c8eb90ddfd`。

**Trade-off / failure / coexistence**：搜索与校准增加离线成本，且剪枝不可逆；显存足够或分布易漂移时保留完整 expert pool 更稳。

<!-- claim:SF-2026-ARXIV-2603-06003:start -->**Claim Boundary**：只支持 arXiv:2603.06003v1 §2.3 Other Compression Methods 的机制与 §4.2 Main results 的公开 workload；§Appendix C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06003:end -->
<!-- review:SF-2026-ARXIV-2603-06003:end -->
### MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing

<!-- review:SF-2026-ARXIV-2603-06007:start -->
**问题**：`MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `3 System Design` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.06007v1 HTML — §3 System Design [facet=method]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a`。

**Evaluation contract 与未证明部分**：公开验证定位在 `4 Evaluation and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06007v1 HTML — §4 Evaluation and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06007v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06007v1.html; sha256:1f1856b23fe817a1bb39f75d81389dce864d0f5a564162bf57e6e9ed506f542a`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Limitations`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-06007:start -->**Claim Boundary**：只支持 arXiv:2603.06007v1 §3 System Design 的机制与 §4 Evaluation and Analysis 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06007:end -->
<!-- review:SF-2026-ARXIV-2603-06007:end -->
### Preventing Learning Stagnation in PPO by Scaling to 1 Million Parallel Environments

<!-- review:SF-2026-ARXIV-2603-06009:start -->
**问题**：PPO 在有限并行环境中会因状态覆盖不足和同步采样停顿而出现学习停滞，单纯调学习率不能补足新 experience。

**旧路径为何合理**：同步、小规模 rollout 容易复算 policy version 与 trajectory，对早期实验足够。

**约束变化与机制**：该工作把环境并发扩展到百万级并重组采样/更新数据流，用更广状态覆盖维持 policy improvement。

**State / data / control owner**：`TRAIN-PPO` 负责 policy version、environment state、rollout ownership、advantage 与 optimizer commit；定位证据为 `arXiv:2603.06009v1 HTML — §Appendix F SFL Hand Designed Results [facet=method]; https://arxiv.org/html/2603.06009v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06009v1.html; sha256:c450f493354e0d32d28546e9bafd0da30b15a00ae2e27c9acac4b424c122625d`。

**Evaluation contract 与未证明部分**：证据只支持其 simulator、policy 和硬件布局；极端并发的样本相关性、通信成本与现实环境有效性仍需独立验证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06009v1 HTML — §5.1 Robotics Results [facet=evaluation]; https://arxiv.org/html/2603.06009v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06009v1.html; sha256:c450f493354e0d32d28546e9bafd0da30b15a00ae2e27c9acac4b424c122625d`。

**Trade-off / failure / coexistence**：更大并发提高覆盖，却增加环境一致性、聚合带宽和 stale-policy 风险；环境昂贵或可复用数据充分时较小并发仍合理。

<!-- claim:SF-2026-ARXIV-2603-06009:start -->**Claim Boundary**：只支持 arXiv:2603.06009v1 §Appendix F SFL Hand Designed Results 的机制与 §5.1 Robotics Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06009:end -->
<!-- review:SF-2026-ARXIV-2603-06009:end -->
### Lyapunov Probes for Hallucination Detection in Large Foundation Models

<!-- review:SF-2026-ARXIV-2603-06081:start -->
**问题**：输出后分类器只关联表面答案，难表达知识边界附近对扰动不稳定的内部表示。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：Lyapunov probe 以扰动下置信单调衰减为训练约束，把局部稳定性作为 hallucination 风险信号。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06081v1 HTML — §3 Method [facet=method]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329`。

**Evaluation contract 与未证明部分**：作者跨文本/多模态数据的比较只支持所测 probe 与扰动协议；稳定表示不是事实正确性的充分条件。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06081v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06081v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06081v1.html; sha256:a25e59b3d42dc6ae18f29625c0a0cf2fc170afa2694fd7125fdcdcf8a3469329`。

**Trade-off / failure / coexistence**：需要内部激活、额外训练和校准，且 OOD 扰动会改变阈值；不可访问权重时仍需 evidence-based verifier。

<!-- claim:SF-2026-ARXIV-2603-06081:start -->**Claim Boundary**：只支持 arXiv:2603.06081v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06081:end -->
<!-- review:SF-2026-ARXIV-2603-06081:end -->
### Diffusion Language Models Are Natively Length-Aware

<!-- review:SF-2026-ARXIV-2603-06123:start -->
**问题**：diffusion language model 若预先固定生成长度，会把长度预测错误转化为 padding 浪费或内容截断。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：论文指出 mask/denoise state 本身携带剩余长度信息，并据此让生成过程动态决定终止。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.06123v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.06123v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06123v1.html; sha256:f1ce18dd10ba66c3ab1e9c528925d5f5783975e0e502f2fa1123c0ba770405ef`。

**Evaluation contract 与未证明部分**：结果只支持所测 DLM、任务和 sampling schedule 的长度感知；不能等同于语义完成度或生产 SLO 保证。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06123v1 HTML — §4.2 Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.06123v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06123v1.html; sha256:f1ce18dd10ba66c3ab1e9c528925d5f5783975e0e502f2fa1123c0ba770405ef`。

**Trade-off / failure / coexistence**：动态长度减少固定预算浪费，却引入终止校准和批次形状变化；结构化输出仍可使用显式长度上限。

<!-- claim:SF-2026-ARXIV-2603-06123:start -->**Claim Boundary**：只支持 arXiv:2603.06123v1 §3 Methodology 的机制与 §4.2 Benchmarks 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06123:end -->
<!-- review:SF-2026-ARXIV-2603-06123:end -->
### A Hazard-Informed Data Pipeline for Robotics Physical Safety

<!-- review:SF-2026-ARXIV-2603-06130:start -->
**问题**：robot safety 数据若只从成功任务或随机失败收集，危险状态分母与伤害严重度不会进入训练 contract。

**旧路径为何合理**：固定离线数据集让训练可复现，也避免在线选择反馈回路。

**约束变化与机制**：论文以 hazard taxonomy 驱动场景、trajectory 与标注采集，使 physical risk 成为可追踪的数据 lineage。

**State / data / control owner**：`TRAIN-DATA` 负责 样本 identity、选择策略、版本、provenance 与训练消费顺序；定位证据为 `arXiv:2603.06130v1 HTML — §1.3 Literature Overview [facet=method]; https://arxiv.org/html/2603.06130v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06130v1.html; sha256:7bd236a37cdb05d13d4b6885de7ff6664b2e07339f4674edb99320a2a401a03a`。

**Evaluation contract 与未证明部分**：结果仅证明其机器人、hazard set 与 evaluator 下的数据覆盖；不能声明未枚举风险已被消除。 未披露的字段保持 `Not Disclosed`，具体定位为 `Not Disclosed — exact-v1 HTML 全文已审计但未提供独立 Evaluation 章节 [facet=evaluation]; https://arxiv.org/html/2603.06130v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06130v1.html; sha256:7bd236a37cdb05d13d4b6885de7ff6664b2e07339f4674edb99320a2a401a03a`。

**Trade-off / failure / coexistence**：hazard-driven 数据提高安全召回，却增加长尾采集、仿真真实性和标签维护成本；低风险封闭环境仍可用普通任务数据。

<!-- claim:SF-2026-ARXIV-2603-06130:start -->**Claim Boundary**：只支持 arXiv:2603.06130v1 §1.3 Literature Overview 的机制与 §Evaluation 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06130:end -->
<!-- review:SF-2026-ARXIV-2603-06130:end -->
### Partial Policy Gradients for RL in LLMs

<!-- review:SF-2026-ARXIV-2603-06138:start -->
**问题**：LLM policy gradient 若对整条 response 统一归因，会把无关 token 的噪声传播到真正决定 reward 的位置。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：Partial Policy Gradients 只对由规则或估计器识别的责任片段施加 policy update，改变 credit-assignment 粒度。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.06138v1 HTML — §5.3 Baselines and Compared Methods [facet=method]; https://arxiv.org/html/2603.06138v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06138v1.html; sha256:e716afb6d974bfeae3c9dabab0eeaac494589190ee36e2a8505ea2454328b0a4`。

**Evaluation contract 与未证明部分**：论文结果只支持其任务、责任选择器和 reward；不能证明选择器不会遗漏跨 token 依赖或引入偏差。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06138v1 HTML — §5.4 Main Results [facet=evaluation]; https://arxiv.org/html/2603.06138v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06138v1.html; sha256:e716afb6d974bfeae3c9dabab0eeaac494589190ee36e2a8505ea2454328b0a4`。

**Trade-off / failure / coexistence**：局部更新降低方差，却依赖可靠 attribution 并可能破坏全局一致性；短答案或 dense reward 仍适合全序列更新。

<!-- claim:SF-2026-ARXIV-2603-06138:start -->**Claim Boundary**：只支持 arXiv:2603.06138v1 §5.3 Baselines and Compared Methods 的机制与 §5.4 Main Results 的公开 workload；§G.9 Failure Mode Taxonomy 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06138:end -->
<!-- review:SF-2026-ARXIV-2603-06138:end -->
### LIT-RAGBench: Benchmarking Generator Capabilities of Large Language Models in Retrieval-Augmented Generation

<!-- review:SF-2026-ARXIV-2603-06198:start -->
**问题**：RAG 只报告检索 recall 或答案分数，会把 generator 使用 evidence 的能力与检索质量混在一起。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：LIT-RAGBench 固定提供的 evidence，并系统改变 relevance、noise 与回答要求以单独测 generator contract。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06198v1 HTML — §5.2. Evaluation Method [facet=method]; https://arxiv.org/html/2603.06198v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06198v1.html; sha256:9b71be1d0b24d8ced81e5e28b81fd136d0ba2ea761a91a75cbd47b4cb7bc3bca`。

**Evaluation contract 与未证明部分**：排名只属于其文档、模型、prompt 和 evaluator；不代表端到端 corpus、权限与 latency 已被覆盖。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06198v1 HTML — §4.1.1. Evaluation Categories and Aspects [facet=evaluation]; https://arxiv.org/html/2603.06198v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06198v1.html; sha256:9b71be1d0b24d8ced81e5e28b81fd136d0ba2ea761a91a75cbd47b4cb7bc3bca`。

**Trade-off / failure / coexistence**：解耦评测提高归因，却可能低估真实检索错误；生产 release gate 仍需补端到端链路。

<!-- claim:SF-2026-ARXIV-2603-06198:start -->**Claim Boundary**：只支持 arXiv:2603.06198v1 §5.2. Evaluation Method 的机制与 §4.1.1. Evaluation Categories and Aspects 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06198:end -->
<!-- review:SF-2026-ARXIV-2603-06198:end -->
### FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling

<!-- review:SF-2026-ARXIV-2603-06199:start -->
**问题**：长上下文 prefill 的稀疏模式搜索若需要排序或累计 attention score，会吞掉跳算收益。

**旧路径为何合理**：通用 eager/runtime 路径优先兼容性，适合形状和模型快速变化。

**约束变化与机制**：FlashPrefill 联合发现 vertical、slash 与 block pattern，并用动态阈值直接裁剪长尾 block，改变 prefill execution plan。

**State / data / control owner**：`INFER-TENSORRT-LLM` 负责 图变换、kernel 选择、设备放置、数值精度与执行缓存；定位证据为 `arXiv:2603.06199v1 HTML — §3.3 Comparison with Previous Methods. [facet=method]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63`。

**Evaluation contract 与未证明部分**：作者速度数字只属于所测模型、长度、kernel 与硬件；摘要不足以外推 27.78x 到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06199v1 HTML — §4 Experiments [facet=evaluation]; https://arxiv.org/html/2603.06199v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06199v1.html; sha256:d586007cb156cd018a48a46fad8b30e7c34b3dae98bdd54663ac921c15ad1b63`。

**Trade-off / failure / coexistence**：阈值搜索换来近似误差和 pattern metadata；短上下文或 exact attention 要求高时 dense prefill 仍合理。

<!-- claim:SF-2026-ARXIV-2603-06199:start -->**Claim Boundary**：只支持 arXiv:2603.06199v1 §3.3 Comparison with Previous Methods. 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06199:end -->
<!-- review:SF-2026-ARXIV-2603-06199:end -->
### SPOILER: TEE-Shielded DNN Partitioning of On-Device Secure Inference with Poison Learning

<!-- review:SF-2026-ARXIV-2603-06263:start -->
**问题**：on-device DNN 分层执行时，切分点会同时决定隐私暴露、TEE 容量和服务端算力，固定 partition 难以兼顾。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：SPOILER 将 TEE-shielded partition 与 poison-learning threat model 联合优化，显式划分可信/非可信执行边界。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.06263v1 HTML — §4 Methodology [facet=method]; https://arxiv.org/html/2603.06263v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06263v1.html; sha256:1efece04d776fd96ac940a6b92c206ee1b98c75fc1b155ae7101596c626bb2d9`。

**Evaluation contract 与未证明部分**：结果只支持其设备、DNN、TEE 和攻击模型；不证明 side channel、runtime 漏洞或所有 poisoning 被覆盖。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06263v1 HTML — §5.2 Results: Security [facet=evaluation]; https://arxiv.org/html/2603.06263v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06263v1.html; sha256:1efece04d776fd96ac940a6b92c206ee1b98c75fc1b155ae7101596c626bb2d9`。

**Trade-off / failure / coexistence**：更深可信切分减少暴露却增加 enclave memory/latency；完全本地或完全可信云在对应条件下仍更简单。

<!-- claim:SF-2026-ARXIV-2603-06263:start -->**Claim Boundary**：只支持 arXiv:2603.06263v1 §4 Methodology 的机制与 §5.2 Results: Security 的公开 workload；§Limitations of TBP: security vs. efficiency. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06263:end -->
<!-- review:SF-2026-ARXIV-2603-06263:end -->
### Stem: Rethinking Causal Information Flow in Sparse Attention

<!-- review:SF-2026-ARXIV-2603-06274:start -->
**问题**：稀疏 attention 只比较保留多少连接，会忽略被裁剪图是否仍允许关键信息跨层到达目标 token。

**旧路径为何合理**：dense attention 保留任意 token 间的直接依赖，最容易解释信息可达性。

**约束变化与机制**：Stem 从 causal information flow 角度刻画稀疏拓扑，把路径可达性与每层选择共同纳入设计。

**State / data / control owner**：`MODEL-SELF-ATTENTION` 负责 attention graph、causal reachability、稀疏 pattern 与跨层信息路径；定位证据为 `arXiv:2603.06274v1 HTML — §2 Methodology [facet=method]; https://arxiv.org/html/2603.06274v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06274v1.html; sha256:43b90be1228e2f3bfa4ab948277cf74f5bc1e4c3023de350fcc617b114ab809b`。

**Evaluation contract 与未证明部分**：理论和实验只支持指定 sparse pattern 与任务；可达不意味着信息无损，也不证明所有硬件实现更快。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06274v1 HTML — §3.3 Ablation Studies [facet=evaluation]; https://arxiv.org/html/2603.06274v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06274v1.html; sha256:43b90be1228e2f3bfa4ab948277cf74f5bc1e4c3023de350fcc617b114ab809b`。

**Trade-off / failure / coexistence**：结构化稀疏降低计算，却可能拉长路径并产生信息瓶颈；短序列或 exactness 优先时 dense attention 仍成立。

<!-- claim:SF-2026-ARXIV-2603-06274:start -->**Claim Boundary**：只支持 arXiv:2603.06274v1 §2 Methodology 的机制与 §3.3 Ablation Studies 的公开 workload；§Limitations of Score-Aware Metric. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06274:end -->
<!-- review:SF-2026-ARXIV-2603-06274:end -->
### From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty

<!-- review:SF-2026-ARXIV-2603-06317:start -->
**问题**：next-token entropy 是局部生成分布，不等于答案正确概率，直接据此拒答会系统性失校准。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文把 uncertainty reasoning 作为显式训练目标，并用 calibration、selective accuracy 与分布转移检查自报置信。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06317v1 HTML — §3 Methodology [facet=method]; https://arxiv.org/html/2603.06317v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06317v1.html; sha256:e859a0c2d1e8b5f9fc545019a6c59c7ede265e75b2f6807414cd1e2b79728710`。

**Evaluation contract 与未证明部分**：结果只支持所测模型、任务和 calibration split；模型生成的 confidence 仍不能替代外部 evidence。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06317v1 HTML — §A.3 Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06317v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06317v1.html; sha256:e859a0c2d1e8b5f9fc545019a6c59c7ede265e75b2f6807414cd1e2b79728710`。

**Trade-off / failure / coexistence**：校准训练改善风险排序，却牺牲 coverage 并随分布漂移失效；高风险 claim 仍需 claim-level verifier。

<!-- claim:SF-2026-ARXIV-2603-06317:start -->**Claim Boundary**：只支持 arXiv:2603.06317v1 §3 Methodology 的机制与 §A.3 Evaluation 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06317:end -->
<!-- review:SF-2026-ARXIV-2603-06317:end -->
### WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching

<!-- review:SF-2026-ARXIV-2603-06331:start -->
**问题**：`WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching` 检查的是 `MULTIMODAL-WORLD-MODELS` 中 规划与闭环评估要求预测 action-conditioned transition，而非只生成逼真视频。 是否会改变现有设计边界。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：exact-v1 的 `4.1 Curvature-guided Heterogeneous Token Prediction` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.06331v1 HTML — §4.1 Curvature-guided Heterogeneous Token Prediction [facet=method]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.2 World Generation Results`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06331v1 HTML — §5.2 World Generation Results [facet=evaluation]; https://arxiv.org/html/2603.06331v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06331v1.html; sha256:b921db561c075f5463f1371320cc7b564650bd498fdb971f483bbcba739b869b`。

**Trade-off / failure / coexistence**：限制与反证定位在 `Failure of Uniform Strategies.`。只需内容生成而不需要因果控制时普通 video model 仍足够。

<!-- claim:SF-2026-ARXIV-2603-06331:start -->**Claim Boundary**：只支持 arXiv:2603.06331v1 §4.1 Curvature-guided Heterogeneous Token Prediction 的机制与 §5.2 World Generation Results 的公开 workload；§Failure of Uniform Strategies. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06331:end -->
<!-- review:SF-2026-ARXIV-2603-06331:end -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing

<!-- review:SF-2026-ARXIV-2603-06350:start -->
**问题**：MoE serving 的冷门 expert 长期占据 GPU，会让峰值容量与平均利用率之间产生结构性浪费。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.06350v1 HTML — §3.2. Architecture and Workflow [facet=method]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a`。

**Evaluation contract 与未证明部分**：公开实验支持其工作负载下的成本/延迟取舍，但 serverless 冷启动、网络拓扑和 expert 热度稳定性限制外推。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06350v1 HTML — §6. Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06350v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06350v1.html; sha256:e2e9871d2231912bb6fd8da29fb96835feeb60203b44ac932725d051172b6b7a`。

**Trade-off / failure / coexistence**：弹性回收降低闲置成本，却把冷启动与跨节点通信引入 token 路径；高且稳定的 expert 利用率仍适合常驻部署。

<!-- claim:SF-2026-ARXIV-2603-06350:start -->**Claim Boundary**：只支持 arXiv:2603.06350v1 §3.2. Architecture and Workflow 的机制与 §6. Evaluation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06350:end -->
<!-- review:SF-2026-ARXIV-2603-06350:end -->
### ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code

<!-- review:SF-2026-ARXIV-2603-06365:start -->
**问题**：自由对话式安全审计没有不可变执行记录，启发式 agent 结论也难与真实仓库修改分离。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：ESAA-Security 让 agent 只提交结构化 intent，由 orchestrator 验证后写 append-only event log，再重放投影与 hash 校验。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.06365v1 HTML — §3 ESAA-Security Architecture [facet=method]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9`。

**Evaluation contract 与未证明部分**：公开稿提供体系和任务清单，能证明 contract 可表达；没有独立 artifact 时不能声称覆盖率或防护效果。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06365v1 HTML — §6 Evaluation Design and Research Questions [facet=evaluation]; https://arxiv.org/html/2603.06365v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06365v1.html; sha256:ec135e5e069e9ff89b5359220c7ee6938b16b0a881fdb82e9a39e8097e58cbf9`。

**Trade-off / failure / coexistence**：事件溯源提高复算性但增加 schema、存储和投影一致性；小型人工审计仍可用普通报告链。

<!-- claim:SF-2026-ARXIV-2603-06365:start -->**Claim Boundary**：只支持 arXiv:2603.06365v1 §3 ESAA-Security Architecture 的机制与 §6 Evaluation Design and Research Questions 的公开 workload；§8 Discussion, Limitations, and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06365:end -->
<!-- review:SF-2026-ARXIV-2603-06365:end -->
### Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows

<!-- review:SF-2026-ARXIV-2603-06394:start -->
**问题**：`Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows` 检查的是 `AGENT-WORKFLOW` 中 长任务、失败恢复和运行时重写要求控制流成为可验证、可持久化的对象。 是否会改变现有设计边界。

**旧路径为何合理**：把 agent loop 留在进程内代码，开发快且控制流直观。

**约束变化与机制**：exact-v1 的 `5.1 Architecture overview` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`AGENT-WORKFLOW` 负责 workflow graph、checkpoint、重试与演进状态；定位证据为 `arXiv:2603.06394v1 HTML — §5.1 Architecture overview [facet=method]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.3 Validation framework`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06394v1 HTML — §5.3 Validation framework [facet=evaluation]; https://arxiv.org/html/2603.06394v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06394v1.html; sha256:b1d21f77edf2c106ce93b3a8e271444f775bc1c116a4ad43b5a730c5c56bf492`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6.5 Future work`。短暂、幂等任务仍可采用轻量进程内循环。

<!-- claim:SF-2026-ARXIV-2603-06394:start -->**Claim Boundary**：只支持 arXiv:2603.06394v1 §5.1 Architecture overview 的机制与 §5.3 Validation framework 的公开 workload；§6.5 Future work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06394:end -->
<!-- review:SF-2026-ARXIV-2603-06394:end -->
### Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling

<!-- review:SF-2026-ARXIV-2603-06403:start -->
**问题**：`Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling` 检查的是 `INFER-SCHEDULING` 中 长度、阶段、SLO、模型和 agent fan-out 的异质性使排队决策决定整体尾延迟。 是否会改变现有设计边界。

**旧路径为何合理**：FIFO 或静态批次在请求同质时易预测、易实现。

**约束变化与机制**：exact-v1 的 `3.1 Reward and Cost Predictor Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。

**State / data / control owner**：`INFER-SCHEDULING` 负责 准入、批处理、优先级、路由和资源选择；定位证据为 `arXiv:2603.06403v1 HTML — §3.1 Reward and Cost Predictor Design [facet=method]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949`。

**Evaluation contract 与未证明部分**：公开验证定位在 `5.3 Experimental Results and Analysis`。证据足以判断该 family 与 owner 的关系，但未披露字段不得补写，且结果不外推到其他 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06403v1 HTML — §5.3 Experimental Results and Analysis [facet=evaluation]; https://arxiv.org/html/2603.06403v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06403v1.html; sha256:c24af41760609da6b1a35249551f629a269d0887b68624d92d649c69b0d60949`。

**Trade-off / failure / coexistence**：限制与反证定位在 `6 Conclusion`。同质离线吞吐任务仍可使用简单静态策略。

<!-- claim:SF-2026-ARXIV-2603-06403:start -->**Claim Boundary**：只支持 arXiv:2603.06403v1 §3.1 Reward and Cost Predictor Design 的机制与 §5.3 Experimental Results and Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06403:end -->
<!-- review:SF-2026-ARXIV-2603-06403:end -->
### A Reference Architecture of Reinforcement Learning Frameworks

<!-- review:SF-2026-ARXIV-2603-06413:start -->
**问题**：RL framework 各自命名 actor、environment、buffer 与 learner，导致架构比较被 API 表象遮蔽。

**旧路径为何合理**：固定后训练配方便于重复和对比。

**约束变化与机制**：该工作从 18 个框架归纳 reference architecture，以组件、数据流和控制关系重建可比较的训练系统 contract。

**State / data / control owner**：`TRAIN-RLHF` 负责 rollout、reward、policy/reference 与更新 freshness；定位证据为 `arXiv:2603.06413v1 HTML — §III Methodology [facet=method]; https://arxiv.org/html/2603.06413v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06413v1.html; sha256:672607fe39827c5d6b7c257a08a1f33c9397beec1b2cacd4b2e0283d8bf5bc99`。

**Evaluation contract 与未证明部分**：grounded-theory 结果支持这些实现中的共同结构，不证明 reference architecture 对未来异步/多智能体框架完备。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06413v1 HTML — §VI Results Evaluation and Quality Assessment [facet=evaluation]; https://arxiv.org/html/2603.06413v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06413v1.html; sha256:672607fe39827c5d6b7c257a08a1f33c9397beec1b2cacd4b2e0283d8bf5bc99`。

**Trade-off / failure / coexistence**：统一词汇改善比较和集成，却可能抹平性能关键特例；具体实现仍需保留自己的 execution semantics。

<!-- claim:SF-2026-ARXIV-2603-06413:start -->**Claim Boundary**：只支持 arXiv:2603.06413v1 §III Methodology 的机制与 §VI Results Evaluation and Quality Assessment 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06413:end -->
<!-- review:SF-2026-ARXIV-2603-06413:end -->
### Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis

<!-- review:SF-2026-ARXIV-2603-06422:start -->
**问题**：只用静态问答评测安全分析 LLM，会遗漏工具调用、动态证据和多阶段 incident workflow。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：SIABENCH 将深度调查与告警分诊拆为可扩展场景，并用 agent 执行网络、内存、恶意样本和日志分析。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06422v1 HTML — §IV-B Agent Design [facet=method]; https://arxiv.org/html/2603.06422v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06422v1.html; sha256:3479a6efc13a154aef3a87ddd8eb7eab063584f738f5a7bf1fb93178be032498`。

**Evaluation contract 与未证明部分**：结果只覆盖其 160 个场景、11 个模型和 sandbox；不能证明真实 SOC 权限、数据漂移或误操作成本。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06422v1 HTML — §V Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06422v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06422v1.html; sha256:3479a6efc13a154aef3a87ddd8eb7eab063584f738f5a7bf1fb93178be032498`。

**Trade-off / failure / coexistence**：更真实的 agentic benchmark 提高外部有效性，却增加环境维护和安全隔离；单一分类器仍可用静态 test set。

<!-- claim:SF-2026-ARXIV-2603-06422:start -->**Claim Boundary**：只支持 arXiv:2603.06422v1 §IV-B Agent Design 的机制与 §V Evaluation 的公开 workload；§V-B3 Primary Factors of LLM’s Failure (RQ3) 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06422:end -->
<!-- review:SF-2026-ARXIV-2603-06422:end -->
### Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input

<!-- review:SF-2026-ARXIV-2603-06444:start -->
**问题**：流式文本驱动 TTS 既缺未来 lookahead，又会因累积全部历史在长文本中崩溃。

**旧路径为何合理**：一次性离线生成可持有完整输入和历史，控制流简单且质量优先。

**约束变化与机制**：论文训练模型在 prosodic boundary 提前停止，并用滑动窗口携带有限文本/语音状态，实现有界上下文拼接。

**State / data / control owner**：`INFER-DECODE` 负责 per-step decode state、termination、stream boundary 与 output commit；定位证据为 `arXiv:2603.06444v1 HTML — §3.4.2 Baselines and Proposed Method [facet=method]; https://arxiv.org/html/2603.06444v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06444v1.html; sha256:574ab5b264d0d1bddafa2393b2f097ae19988eec9aa7914f678c6b2470c468aa`。

**Evaluation contract 与未证明部分**：结果绑定其 TTS 模型、语言和长文本集；不能从 WER 改善推断跨说话人、并发或端到端对话 SLO。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06444v1 HTML — §3.3 Evaluation Metrics [facet=evaluation]; https://arxiv.org/html/2603.06444v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06444v1.html; sha256:574ab5b264d0d1bddafa2393b2f097ae19988eec9aa7914f678c6b2470c468aa`。

**Trade-off / failure / coexistence**：有界 state 稳定长流资源，却可能在边界预测错误时产生韵律断裂；离线合成仍可利用完整文本。

<!-- claim:SF-2026-ARXIV-2603-06444:start -->**Claim Boundary**：只支持 arXiv:2603.06444v1 §3.4.2 Baselines and Proposed Method 的机制与 §3.3 Evaluation Metrics 的公开 workload；§4.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06444:end -->
<!-- review:SF-2026-ARXIV-2603-06444:end -->
### What if? Emulative Simulation with World Models for Situated Reasoning

<!-- review:SF-2026-ARXIV-2603-06445:start -->
**问题**：situated agent 无法安全探索时，单帧 observation 不足以回答路径和未来状态问题。

**旧路径为何合理**：下一帧生成可学习外观连续性，但不必显式承担动作可控的状态转移。

**约束变化与机制**：WanderDream 用 world model 生成从当前状态到目标的 imagined trajectory，并分别评测起点、路径与终态推理。

**State / data / control owner**：`MULTIMODAL-WORLD-MODELS` 负责 latent state、action-conditioned transition 与 rollout commitment；定位证据为 `arXiv:2603.06445v1 HTML — §5.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.06445v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06445v1.html; sha256:89e0343638390a96a6b2f2da8524e308fd85394b9a66901f3cf6a8dc38470de0`。

**Evaluation contract 与未证明部分**：数据与实验支持所测室内场景中的 emulative simulation；生成轨迹的物理/因果真实性和真实部署安全未被证明。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06445v1 HTML — §Appendix 0.C Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06445v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06445v1.html; sha256:89e0343638390a96a6b2f2da8524e308fd85394b9a66901f3cf6a8dc38470de0`。

**Trade-off / failure / coexistence**：想象 rollout 降低真实探索成本，却会传播 model bias；允许安全交互时真实 observation 仍是更强证据。

<!-- claim:SF-2026-ARXIV-2603-06445:start -->**Claim Boundary**：只支持 arXiv:2603.06445v1 §5.1 Implementation Details 的机制与 §Appendix 0.C Evaluation 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06445:end -->
<!-- review:SF-2026-ARXIV-2603-06445:end -->
### Data Analogies Enable Efficient Cross-Embodiment Transfer

<!-- review:SF-2026-ARXIV-2603-06450:start -->
**问题**：把跨 embodiment 数据简单混合，会把视角、外观和形态差异混为同一种 diversity。

**旧路径为何合理**：固定离线数据集让训练可复现，也避免在线选择反馈回路。

**约束变化与机制**：论文用配对 data analogy 对齐场景、任务或 trajectory，区分 perceptual diversity 与 morphology transfer 所需证据。

**State / data / control owner**：`TRAIN-DATA` 负责 样本 identity、选择策略、版本、provenance 与训练消费顺序；定位证据为 `arXiv:2603.06450v1 HTML — §III Cross-Embodiment Data Analogies [facet=method]; https://arxiv.org/html/2603.06450v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06450v1.html; sha256:84f01ce204cd5799d112dd917ecebaf420121b1fac663adf9e8717866082b10b`。

**Evaluation contract 与未证明部分**：结果只支持其仿真和机器人设置中的成功率变化；不能把 22.5% 提升外推到未对齐 action schema。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06450v1 HTML — §Evaluation Tasks [facet=evaluation]; https://arxiv.org/html/2603.06450v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06450v1.html; sha256:84f01ce204cd5799d112dd917ecebaf420121b1fac663adf9e8717866082b10b`。

**Trade-off / failure / coexistence**：配对提高 transfer 信号，却显著增加采集和对齐成本；单 embodiment 或目标数据充足时直接训练更简单。

<!-- claim:SF-2026-ARXIV-2603-06450:start -->**Claim Boundary**：只支持 arXiv:2603.06450v1 §III Cross-Embodiment Data Analogies 的机制与 §Evaluation Tasks 的公开 workload；§VI Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06450:end -->
<!-- review:SF-2026-ARXIV-2603-06450:end -->
### Pinterest Canvas: Large-Scale Image Generation at Pinterest

<!-- review:SF-2026-ARXIV-2603-06453:start -->
**问题**：一个通用图像生成模型难同时满足多个产品任务的严格控制、质量与上线节奏。

**旧路径为何合理**：单模型、单任务的离线交付在需求稳定时最少引入生命周期状态。

**约束变化与机制**：Pinterest Canvas 以共享 foundation diffusion model 为起点，再通过任务数据产生专用 variant，并把数据、训练、推理和 A/B release 串成产品流水线。

**State / data / control owner**：`PLATFORM-PRODUCTION` 负责 production asset identity、variant lineage、deployment state、online evidence 与 rollback；定位证据为 `arXiv:2603.06453v1 HTML — §3. System Overview [facet=method]; https://arxiv.org/html/2603.06453v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06453v1.html; sha256:de8802789b8b1abdd6a6cc10b2606b3f6f8570a6cd166685c3975bd794b5392b`。

**Evaluation contract 与未证明部分**：线上 uplift 只属于公开两个用例、用户流量和评价合同；未披露硬件、并发和长期漂移不能推断。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06453v1 HTML — §5.1. Offline Evaluations for Outpainting [facet=evaluation]; https://arxiv.org/html/2603.06453v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06453v1.html; sha256:de8802789b8b1abdd6a6cc10b2606b3f6f8570a6cd166685c3975bd794b5392b`。

**Trade-off / failure / coexistence**：共享基座降低重复训练，却引入 variant 管理、数据偏差和回归矩阵；需求相近时单一模型仍可减少运维成本。

<!-- claim:SF-2026-ARXIV-2603-06453:start -->**Claim Boundary**：只支持 arXiv:2603.06453v1 §3. System Overview 的机制与 §5.1. Offline Evaluations for Outpainting 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06453:end -->
<!-- review:SF-2026-ARXIV-2603-06453:end -->
### When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models

<!-- review:SF-2026-ARXIV-2603-06508:start -->
**问题**：多模态 diffusion 的高 attack-success rate 可能掩盖 trigger 实际只依赖单一模态，传统总分无法归因。

**旧路径为何合理**：把模型输出当文本并在边界做静态过滤，非行动系统中成本最低。

**约束变化与机制**：论文用 Trigger Modality Attribution 与 Cross-Trigger Interaction 分解各模态贡献，识别 backdoor modality collapse。

**State / data / control owner**：`PLATFORM-SECURITY` 负责 身份、授权、数据流、策略执行点与审计证据；定位证据为 `arXiv:2603.06508v1 HTML — §4 Problem Formulation [facet=method]; https://arxiv.org/html/2603.06508v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06508v1.html; sha256:f1a848eb0679fb055329856a71a86fa1d555715f37fceaf9c3e1b29a49c66980`。

**Evaluation contract 与未证明部分**：证据只支持其模型、攻击和训练配置；winner-takes-all 现象不等于所有 multimodal backdoor 都同构。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06508v1 HTML — §5.2 Results Analysis [facet=evaluation]; https://arxiv.org/html/2603.06508v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06508v1.html; sha256:f1a848eb0679fb055329856a71a86fa1d555715f37fceaf9c3e1b29a49c66980`。

**Trade-off / failure / coexistence**：分模态评测提高诊断，却增加组合实验成本；单模态模型仍可使用传统攻击成功率。

<!-- claim:SF-2026-ARXIV-2603-06508:start -->**Claim Boundary**：只支持 arXiv:2603.06508v1 §4 Problem Formulation 的机制与 §5.2 Results Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06508:end -->
<!-- review:SF-2026-ARXIV-2603-06508:end -->
### Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders

<!-- review:SF-2026-ARXIV-2603-06569:start -->
**问题**：VLM 依赖对比预训练视觉 encoder 时，分类不变性可能抹掉 dense perception 所需的细粒度时空信息。

**旧路径为何合理**：各模态保留独立 encoder 和静态融合点，职责清楚且便于单独优化。

**约束变化与机制**：Penguin-VL 从 text-only LLM 初始化视觉 encoder，测试表示目标而非单纯扩大模型规模的替代路线。

**State / data / control owner**：`MULTIMODAL-REPRESENTATION` 负责 跨模态 token identity、融合、时间锚点与可变表示状态；定位证据为 `arXiv:2603.06569v1 HTML — §4.1 Implementation Details [facet=method]; https://arxiv.org/html/2603.06569v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06569v1.html; sha256:378d575c3423b11c22ccfa484927823d92055164c54667c9a3553747516777e4`。

**Evaluation contract 与未证明部分**：公开结果支持 2B/8B 模型和所测图像视频任务；不能证明任意语言权重都优于 CLIP/SigLIP 初始化。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06569v1 HTML — §4.3 Image Benchmarks [facet=evaluation]; https://arxiv.org/html/2603.06569v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06569v1.html; sha256:378d575c3423b11c22ccfa484927823d92055164c54667c9a3553747516777e4`。

**Trade-off / failure / coexistence**：更统一的初始化提高细粒度表示潜力，却增加模态适配和训练不稳定性；检索/分类任务仍可能受益于对比 encoder。

<!-- claim:SF-2026-ARXIV-2603-06569:start -->**Claim Boundary**：只支持 arXiv:2603.06569v1 §4.1 Implementation Details 的机制与 §4.3 Image Benchmarks 的公开 workload；§6.2 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06569:end -->
<!-- review:SF-2026-ARXIV-2603-06569:end -->
### Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion

<!-- review:SF-2026-ARXIV-2603-06577:start -->
**问题**：any-to-any 多模态理解与生成若直接继承自回归骨干，会把所有模态都绑定到单向逐 token 提交。

**旧路径为何合理**：causal autoregression 提供明确顺序和简单缓存语义。

**约束变化与机制**：Omni-Diffusion 以 mask-based discrete diffusion 联合建模文本、图像与语音 token，并以模态专属 codec、长度控制和并行去噪保留各模态的生成边界。

**State / data / control owner**：`MULTIMODAL-GENERATIVE-PARADIGMS` 负责 生成顺序、proposal/correction 与终止状态；定位证据为 `arXiv:2603.06577v1 HTML — §3.2 Model Architecture [facet=method]; https://arxiv.org/html/2603.06577v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06577v1.html; sha256:c53b31a5369d09c9361c71ccf3d5db778c386d88a46e45652f75ee3c1400e0b2`。

**Evaluation contract 与未证明部分**：exact-v1 只支持 Dream-7B 及公开 ASR、TTS、VQA、文生图 workload 中的可行性与采样步数关系；硬件、精度、并发和生产 SLO 未披露。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06577v1 HTML — §Speech-Vision Alignment Evaluation [facet=evaluation]; https://arxiv.org/html/2603.06577v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06577v1.html; sha256:c53b31a5369d09c9361c71ccf3d5db778c386d88a46e45652f75ee3c1400e0b2`。

**Trade-off / failure / coexistence**：统一 backbone 提供并行可修正状态，却没有消除 codec、解码策略和 evaluator 的模态差异；需要强顺序 commit 或 typed output 时自回归/专用 head 仍成立。

<!-- claim:SF-2026-ARXIV-2603-06577:start -->**Claim Boundary**：只支持 arXiv:2603.06577v1 §3.2 Model Architecture 的机制与 §Speech-Vision Alignment Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06577:end -->
<!-- review:SF-2026-ARXIV-2603-06577:end -->
### Multimodal Large Language Models as Image Classifiers

<!-- review:SF-2026-ARXIV-2603-06578:start -->
**问题**：把 MLLM 分类得分视为模型固有能力，会隐藏标签、输出映射、distractor、batch 与样本顺序对结论的共同控制。

**旧路径为何合理**：单一离线分数便于比较版本。

**约束变化与机制**：论文把 closed-world、multiple-choice 与 open-world 协议拆开，并显式改变重标注、响应格式、OOV 处理、mapping encoder、batch size、顺序和组成，显示它们共同构成 EvalRun identity。

**State / data / control owner**：`PLATFORM-EVALUATION-SYSTEM` 负责 evaluation contract、覆盖分母、evidence lineage 与 release gate；定位证据为 `arXiv:2603.06578v1 HTML — §2.4 Model and class names overview [facet=method]; https://arxiv.org/html/2603.06578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06578v1.html; sha256:9d3a6d91b83510a070bb82d75327eeb478f7b9c51909e003b1330f89e6bdbc91`。

**Evaluation contract 与未证明部分**：exact-v1 只支持五个公开 MLLM、ImageNet-1k/ReGT 子集及披露协议下的结论反转；ReGT 尚未公开，不能把修正标签当作最终真值或外推所有分类 workload。 未披露的字段保持 `Not Disclosed`，具体定位为 `arXiv:2603.06578v1 HTML — §2.2 Evaluation metric [facet=evaluation]; https://arxiv.org/html/2603.06578v1; papers/2026/03/_sources/daily-20260309/exact-v1-bodies/2603.06578v1.html; sha256:9d3a6d91b83510a070bb82d75327eeb478f7b9c51909e003b1330f89e6bdbc91`。

**Trade-off / failure / coexistence**：更完整的评测身份改善归因，却增加标注成本、映射依赖和自由度；严格 exact-match 仍可作可复算基线，但必须显式声明其偏差。

<!-- claim:SF-2026-ARXIV-2603-06578:start -->**Claim Boundary**：只支持 arXiv:2603.06578v1 §2.4 Model and class names overview 的机制与 §2.2 Evaluation metric 的公开 workload；§4 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。<!-- claim:SF-2026-ARXIV-2603-06578:end -->
<!-- review:SF-2026-ARXIV-2603-06578:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05540 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-05540 |
| SF-2026-ARXIV-2603-05725 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-05725 |
| SF-2026-ARXIV-2603-05786 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-05786 |
| SF-2026-ARXIV-2603-05800 | score_7_9;potential_books_delta | selected | DA-20260309-16 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-16 |
| SF-2026-ARXIV-2603-05931 | score_7_9;potential_books_delta | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-05931 |
| SF-2026-ARXIV-2603-05959 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-05959 |
| SF-2026-ARXIV-2603-06009 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-06009 |
| SF-2026-ARXIV-2603-06317 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-06317 |
| SF-2026-ARXIV-2603-06350 | score_7_9;potential_books_delta | selected | DA-20260309-41 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-41 |
| SF-2026-ARXIV-2603-06413 | score_7_9 | not_selected | — | — | 证据 Review 已完成；相较所选单元，本 family 的长期变化更适合作为 owner comparison 而非本日报告长叙事 | analysis-decision:SF-2026-ARXIV-2603-06413 |
| SF-2026-ARXIV-2603-06578 | score_7_9;potential_books_delta | selected | DA-20260309-54 | — | 在本日候选中直接改变 durable state/control/evaluation owner，且与当前 Books 比较需要优先释放 | analysis:DA-20260309-54 |

<!-- analysis-decision:SF-2026-ARXIV-2603-05540:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-05540:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-05725:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-05725:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-05786:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-05786:end -->
<!-- analysis:DA-20260309-16:start -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale

多模态生成流同时包含持续到达、异质阶段和实时 deadline；把每个请求当成单次模型调用会隐藏跨阶段排队。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。 其公开验证边界为：作者在其公开模型、设备和请求分布上测量吞吐与尾延迟，足以支持所测实时 pipeline 的联合调度收益；未披露的跨集群网络、租户隔离和生产 SLO 不属于结论。 新增代价与回退条件为：更细的阶段状态提升利用率，也增加队列、取消和中间结果失效复杂度；离线同质批处理仍适合静态流水线。
<!-- analysis:DA-20260309-16:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-05931:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-05931:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-05959:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-05959:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-06009:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-06009:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-06317:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-06317:end -->
<!-- analysis:DA-20260309-41:start -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing

MoE serving 的冷门 expert 长期占据 GPU，会让峰值容量与平均利用率之间产生结构性浪费。 旧路径在其原约束下仍合理：FIFO 或静态批次在请求同质时易预测、易实现。 本 family 的设计变化是：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。 其公开验证边界为：公开实验支持其工作负载下的成本/延迟取舍，但 serverless 冷启动、网络拓扑和 expert 热度稳定性限制外推。 新增代价与回退条件为：弹性回收降低闲置成本，却把冷启动与跨节点通信引入 token 路径；高且稳定的 expert 利用率仍适合常驻部署。
<!-- analysis:DA-20260309-41:end -->
<!-- analysis-decision:SF-2026-ARXIV-2603-06413:start -->该 family 已完成 exact-v1 Review，但未进入三项长叙事；Review 深度未被降低，Books Comparison 仍独立执行。<!-- analysis-decision:SF-2026-ARXIV-2603-06413:end -->
<!-- analysis:DA-20260309-54:start -->
### Multimodal Large Language Models as Image Classifiers

把 MLLM 分类得分视为模型固有能力，会隐藏标签、输出映射、distractor、batch 与样本顺序对结论的共同控制。 旧路径在其原约束下仍合理：单一离线分数便于比较版本。 本 family 的设计变化是：论文把 closed-world、multiple-choice 与 open-world 协议拆开，并显式改变重标注、响应格式、OOV 处理、mapping encoder、batch size、顺序和组成，显示它们共同构成 EvalRun identity。 其公开验证边界为：exact-v1 只支持五个公开 MLLM、ImageNet-1k/ReGT 子集及披露协议下的结论反转；ReGT 尚未公开，不能把修正标签当作最终真值或外推所有分类 workload。 新增代价与回退条件为：更完整的评测身份改善归因，却增加标注成本、映射依赖和自由度；严格 exact-match 仍可作可复算基线，但必须显式声明其偏差。
<!-- analysis:DA-20260309-54:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-05517 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05517 | delta:SF-2026-ARXIV-2603-05517 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05517 |
| SF-2026-ARXIV-2603-05520 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#differential-privacy-先定义被保护对象，再选择机制 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05520 | delta:SF-2026-ARXIV-2603-05520 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05520 |
| SF-2026-ARXIV-2603-05528 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#codec-aware-tokenization：稀疏性可以在视觉-encoder-之前暴露 (section Ch-owner) | books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent); books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05528 | delta:SF-2026-ARXIV-2603-05528 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05528 |
| SF-2026-ARXIV-2603-05540 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#编译器反馈可以前移，但仍是受限-authority (section Ch-owner) | books/part-07-agent/77-memory.md#第77章-memory (section Ch-adjacent); books/part-07-agent/79-planning.md#第79章-planning (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05540 | delta:SF-2026-ARXIV-2603-05540 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05540 |
| SF-2026-ARXIV-2603-05553 | TRAIN-DATA | books/part-04-training-system/27-data.md#part-iv-的能力生产链 (section Ch-owner) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent); books/part-04-training-system/28-pretraining.md#第28章-pretraining (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05553 | delta:SF-2026-ARXIV-2603-05553 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05553 |
| SF-2026-ARXIV-2603-05578 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#第一个不变量：评估声明必须绑定完整对象 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05578 | delta:SF-2026-ARXIV-2603-05578 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05578 |
| SF-2026-ARXIV-2603-05618 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#safety-evaluation-的单位是-run，不只是-prompt (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05618 | delta:SF-2026-ARXIV-2603-05618 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05618 |
| SF-2026-ARXIV-2603-05637 | AGENT-MCP | books/part-07-agent/83-mcp.md#authorization-之前还需要可验证的-server-admission (section Ch-owner) | books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent); books/part-07-agent/84-agent-platform.md#第84章-agent-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05637 | delta:SF-2026-ARXIV-2603-05637 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05637 |
| SF-2026-ARXIV-2603-05692 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#异步工作不必永久绑定固定-physical-core (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05692 | delta:SF-2026-ARXIV-2603-05692 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05692 |
| SF-2026-ARXIV-2603-05697 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05697 | delta:SF-2026-ARXIV-2603-05697 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05697 |
| SF-2026-ARXIV-2603-05706 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05706 | delta:SF-2026-ARXIV-2603-05706 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05706 |
| SF-2026-ARXIV-2603-05725 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05725 | delta:SF-2026-ARXIV-2603-05725 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05725 |
| SF-2026-ARXIV-2603-05739 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05739 | delta:SF-2026-ARXIV-2603-05739 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05739 |
| SF-2026-ARXIV-2603-05754 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05754 | delta:SF-2026-ARXIV-2603-05754 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05754 |
| SF-2026-ARXIV-2603-05786 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05786 | delta:SF-2026-ARXIV-2603-05786 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05786 |
| SF-2026-ARXIV-2603-05800 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从队列启发式到时间耦合的资源影子价格 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05800 | delta:SF-2026-ARXIV-2603-05800 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-05800 |
| SF-2026-ARXIV-2603-05815 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05815 | delta:SF-2026-ARXIV-2603-05815 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05815 |
| SF-2026-ARXIV-2603-05828 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05828 | delta:SF-2026-ARXIV-2603-05828 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05828 |
| SF-2026-ARXIV-2603-05872 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#pre-guard-可以前移，但最终-authority-不能前移给-draft-model (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05872 | delta:SF-2026-ARXIV-2603-05872 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05872 |
| SF-2026-ARXIV-2603-05881 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#continual-update-需要同步推进-calibration-state (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05881 | delta:SF-2026-ARXIV-2603-05881 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05881 |
| SF-2026-ARXIV-2603-05910 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05910 | delta:SF-2026-ARXIV-2603-05910 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05910 |
| SF-2026-ARXIV-2603-05912 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05912 | delta:SF-2026-ARXIV-2603-05912 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05912 |
| SF-2026-ARXIV-2603-05931 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#accelerator-readiness-是-phase-×-shape-×-offload-×-host-control-contract (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05931 | delta:SF-2026-ARXIV-2603-05931 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-05931 |
| SF-2026-ARXIV-2603-05959 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#流式输入把-cache-变成可续租的-session-state (section Ch-owner) | books/part-05-inference-system/44-decode.md#第44章-decode (section Ch-adjacent); books/part-05-inference-system/46-continuous-batching.md#第46章-continuous-batching (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05959 | delta:SF-2026-ARXIV-2603-05959 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05959 |
| SF-2026-ARXIV-2603-05960 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/35-checkpoint.md#第35章-checkpoint (section Ch-adjacent); books/part-04-training-system/37-tensor-parallel.md#第37章-tensor-parallel (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05960 | delta:SF-2026-ARXIV-2603-05960 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05960 |
| SF-2026-ARXIV-2603-05974 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#drop-决策从超时后的反应演进为剩余预算准入 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-05974 | delta:SF-2026-ARXIV-2603-05974 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-05974 |
| SF-2026-ARXIV-2603-06001 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent); books/part-04-training-system/27-data.md#第27章-数据 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06001 | delta:SF-2026-ARXIV-2603-06001 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06001 |
| SF-2026-ARXIV-2603-06003 | MODEL-MOE | books/part-02-model/21-moe.md#router-选择-expert，placement-决定这次选择能否低成本执行 (section Ch-owner) | books/part-02-model/20-sampling.md#第20章-sampling (section Ch-adjacent); books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06003 | delta:SF-2026-ARXIV-2603-06003 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06003 |
| SF-2026-ARXIV-2603-06007 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#本章要回答的问题 (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06007 | delta:SF-2026-ARXIV-2603-06007 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06007 |
| SF-2026-ARXIV-2603-06009 | TRAIN-PPO | books/part-04-training-system/32-ppo.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/31-rlhf.md#第31章-rlhf (section Ch-adjacent); books/part-04-training-system/33-grpo.md#第33章-grpo：从组内相对优势到-trajectory-lifecycle (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06009 | delta:SF-2026-ARXIV-2603-06009 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06009 |
| SF-2026-ARXIV-2603-06081 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06081 | delta:SF-2026-ARXIV-2603-06081 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06081 |
| SF-2026-ARXIV-2603-06123 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#diffusion：用迭代修正换并行状态更新 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06123 | delta:SF-2026-ARXIV-2603-06123 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06123 |
| SF-2026-ARXIV-2603-06130 | TRAIN-DATA | books/part-04-training-system/27-data.md#内容无害不等于更新无害：过滤器还要预测-training-effect (section Ch-owner) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent); books/part-04-training-system/28-pretraining.md#第28章-pretraining (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06130 | delta:SF-2026-ARXIV-2603-06130 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06130 |
| SF-2026-ARXIV-2603-06138 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06138 | delta:SF-2026-ARXIV-2603-06138 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06138 |
| SF-2026-ARXIV-2603-06198 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#continual-update-需要同步推进-calibration-state (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06198 | delta:SF-2026-ARXIV-2603-06198 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06198 |
| SF-2026-ARXIV-2603-06199 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#binary-lifting-的核心是恢复-typed-state (section Ch-owner) | books/part-05-inference-system/48-speculative-decoding.md#第48章-speculative-decoding (section Ch-adjacent); books/part-05-inference-system/50-vllm.md#第50章-llm-serving-engine：以-vllm-为例 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06199 | delta:SF-2026-ARXIV-2603-06199 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06199 |
| SF-2026-ARXIV-2603-06263 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#responsive-不等于-semantic-available (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06263 | delta:SF-2026-ARXIV-2603-06263 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06263 |
| SF-2026-ARXIV-2603-06274 | MODEL-SELF-ATTENTION | books/part-02-model/14-self-attention.md#本章要回答的问题 (section Ch-owner) | books/part-02-model/13-position-encoding.md#第13章-position-encoding (section Ch-adjacent); books/part-02-model/15-multi-head-attention.md#第15章-multi-head-attention (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06274 | delta:SF-2026-ARXIV-2603-06274 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06274 |
| SF-2026-ARXIV-2603-06317 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#continual-update-需要同步推进-calibration-state (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06317 | delta:SF-2026-ARXIV-2603-06317 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06317 |
| SF-2026-ARXIV-2603-06331 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06331 | delta:SF-2026-ARXIV-2603-06331 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06331 |
| SF-2026-ARXIV-2603-06350 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#当前能放下，不等于未来可完成 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06350 | delta:SF-2026-ARXIV-2603-06350 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-06350 |
| SF-2026-ARXIV-2603-06365 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#requirement-也是-versioned-untrusted-supply-chain-input (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06365 | delta:SF-2026-ARXIV-2603-06365 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06365 |
| SF-2026-ARXIV-2603-06394 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#failure-attribution、perception-routing-与-sticky-state-ownership (section Ch-owner) | books/part-07-agent/80-reflection.md#第80章-reflection (section Ch-adjacent); books/part-07-agent/82-multi-agent.md#第82章-multi-agent (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06394 | delta:SF-2026-ARXIV-2603-06394 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06394 |
| SF-2026-ARXIV-2603-06403 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/55-pd-disaggregation.md#第55章-pd-分离 (section Ch-adjacent); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#第57章-什么是-ai-platform (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06403 | delta:SF-2026-ARXIV-2603-06403 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06403 |
| SF-2026-ARXIV-2603-06413 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#本章要回答的问题 (section Ch-owner) | books/part-04-training-system/30-lora.md#第30章-lora (section Ch-adjacent); books/part-04-training-system/32-ppo.md#第32章-ppo (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06413 | delta:SF-2026-ARXIV-2603-06413 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06413 |
| SF-2026-ARXIV-2603-06422 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06422 | delta:SF-2026-ARXIV-2603-06422 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06422 |
| SF-2026-ARXIV-2603-06444 | INFER-DECODE | books/part-05-inference-system/44-decode.md#本章要回答的问题 (section Ch-owner) | books/part-05-inference-system/43-prefill.md#第43章-prefill (section Ch-adjacent); books/part-05-inference-system/45-why-kv-cache-speeds-up.md#第45章-为什么-kv-cache-能提速 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06444 | delta:SF-2026-ARXIV-2603-06444 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06444 |
| SF-2026-ARXIV-2603-06445 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (section Ch-owner) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06445 | delta:SF-2026-ARXIV-2603-06445 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06445 |
| SF-2026-ARXIV-2603-06450 | TRAIN-DATA | books/part-04-training-system/27-data.md#part-iv-的能力生产链 (section Ch-owner) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#第26章-embodied-ai-与-vla：从感知到物理行动 (section Ch-adjacent); books/part-04-training-system/28-pretraining.md#第28章-pretraining (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06450 | delta:SF-2026-ARXIV-2603-06450 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06450 |
| SF-2026-ARXIV-2603-06453 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (section Ch-owner) | books/part-06-ai-infrastructure/72-security.md#第72章-security (section Ch-adjacent); books/part-07-agent/74-prompt.md#第74章-prompt (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06453 | delta:SF-2026-ARXIV-2603-06453 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06453 |
| SF-2026-ARXIV-2603-06508 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#safety-evaluation-的单位是-run，不只是-prompt (section Ch-owner) | books/part-06-ai-infrastructure/71-multi-tenant.md#第71章-multi-tenant (section Ch-adjacent); books/part-06-ai-infrastructure/73-production-best-practice.md#第73章-production-best-practice (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06508 | delta:SF-2026-ARXIV-2603-06508 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06508 |
| SF-2026-ARXIV-2603-06569 | MULTIMODAL-REPRESENTATION | books/part-03-multimodal-world-models/23-multimodal-representation.md#codec-aware-tokenization：稀疏性可以在视觉-encoder-之前暴露 (section Ch-owner) | books/part-02-model/22-long-context.md#第22章-long-context (section Ch-adjacent); books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#第24章-多模态生成范式 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06569 | delta:SF-2026-ARXIV-2603-06569 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06569 |
| SF-2026-ARXIV-2603-06577 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#exploration-是训练计算轴，不是新的生成真值 (section Ch-owner) | books/part-03-multimodal-world-models/23-multimodal-representation.md#第23章-多模态表示与融合 (section Ch-adjacent); books/part-03-multimodal-world-models/25-multimodal-world-models.md#第25章-world-models：从生成画面到预测环境 (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06577 | delta:SF-2026-ARXIV-2603-06577 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-06577 |
| SF-2026-ARXIV-2603-06578 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#model-self-report-不能拥有输入来源真值 (section Ch-owner) | books/part-06-ai-infrastructure/65-kai-scheduler.md#第65章-ai-集群公平共享与-gpu-调度：以-kai-scheduler-为例 (section Ch-adjacent); books/part-06-ai-infrastructure/67-monitoring.md#第67章-monitoring (section Ch-adjacent) | existing:SF-2026-ARXIV-2603-06578 | delta:SF-2026-ARXIV-2603-06578 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2603-06578 |

<!-- books-review:SF-2026-ARXIV-2603-05517:start -->
### Traversal-as-Policy: Log-Distilled Gated Behavior Trees as Externalized, Verifiable Policies for Safe, Robust, and Efficient Agents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05517:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-05517:end -->

<!-- delta:SF-2026-ARXIV-2603-05517:start -->新证据差异：exact-v1 的 `Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05517:end -->

边界：只支持 arXiv:2603.05517v1 §Appendix J GBT as a Plug-in Policy Artifact Improves Diverse Frameworks 的机制与 §I.1 Benchmarks and OpenHands Integration (Facts, Sizes, and Evaluation Contracts) 的公开 workload；§O.1 Limitations and Open Failure Modes 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05517:end -->
<!-- books-review:SF-2026-ARXIV-2603-05520:start -->
### Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05520:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的 runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness 不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用 post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加 前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。<!-- existing:SF-2026-ARXIV-2603-05520:end -->

<!-- delta:SF-2026-ARXIV-2603-05520:start -->新证据差异：exact-v1 的 `4.3 Design Implications` 把论文方案定位到 身份、授权、数据流、策略执行点与审计证据；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05520:end -->

边界：只支持 arXiv:2603.05520v1 §4.3 Design Implications 的机制与 §7.1 Overall Performance on Medical and Financial Benchmarks 的公开 workload；§8 Conclusion and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05520:end -->
<!-- books-review:SF-2026-ARXIV-2603-05528:start -->
### Omni-C: Compressing Heterogeneous Modalities into a Single Dense Encoder — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05528:start -->已读 owner `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节。现有命题：前者仍把选中区域解码为 RGB，兼容已有 vision encoder，却可能漏掉 codec metadata 未显著标记的语义变化； 后者减少重复 decode/encode work，却把 codec、GOP、motion vector、residual layout 与 tokenizer 一起变成模型 输入协议。Transcoding、随机 seek、corrupted stream、不同 codec/profile 与 frame-rate conversion 都可能改变 token identity。Dense frames 在格式多样、证据完整性优先或 codec path 不可信时仍成立。<!-- existing:SF-2026-ARXIV-2603-05528:end -->

<!-- delta:SF-2026-ARXIV-2603-05528:start -->新证据差异：Omni-C 以共享 dense Transformer 承担图像、语音与文本表示，只保留轻量模态投影，并用未配对的单模态对比目标抑制跨模态冲突。<!-- delta:SF-2026-ARXIV-2603-05528:end -->

边界：只支持 arXiv:2603.05528v1 §III Methodology 的机制与 §IV Experiments 的公开 workload；§VI Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05528:end -->
<!-- books-review:SF-2026-ARXIV-2603-05540:start -->
### Attention Meets Reachability: Structural Equivalence and Efficiency in Grammar-Constrained LLM Decoding — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05540:start -->已读 owner `books/part-07-agent/78-tool-calling.md` 与相邻章节。现有命题：先完整生成程序，再调用 compiler/test 并修复，是最通用的黑盒路径；当 grammar 可处理时，constrained decoding 也能提前排除语法错误。但后置诊断会浪费已经生成的 token，并把错误起点埋在长输出中；另一方面，任意 prefix 通常还不是可编译单元，不能直接交给编译器。<!-- existing:SF-2026-ARXIV-2603-05540:end -->

<!-- delta:SF-2026-ARXIV-2603-05540:start -->新证据差异：论文把解码写成 next-token distribution 与 pushdown reachability oracle 的耦合，证明语言等价不等于执行成本等价，并用 SAC 描述逐 token parse-forest 增长。<!-- delta:SF-2026-ARXIV-2603-05540:end -->

边界：只支持 arXiv:2603.05540v1 §Neural architecture coupling. 的机制与 §Parsing theory and reachability. 的公开 workload；§12 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05540:end -->
<!-- books-review:SF-2026-ARXIV-2603-05553:start -->
### EigenData: A Self-Evolving Multi-Agent Platform for Function-Calling Data Synthesis, Auditing, and Repair — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05553:start -->已读 owner `books/part-04-training-system/27-data.md` 与相邻章节。现有命题：多模态 raw sample、codec token、frame/second 和 action trajectory 不能用一个未经定义的“token 数”混合计量。第23～26章拥有表示与行动语义；本章拥有这些样本怎样被选择、版本化、配比与送入优化。这个边界使 representation 研究不会寄居于 Data，也使 Data 不退化成文件清单。<!-- existing:SF-2026-ARXIV-2603-05553:end -->

<!-- delta:SF-2026-ARXIV-2603-05553:start -->新证据差异：EigenData 让多个专责 agent 共享可验证 artifact graph，并以数据库终态而非轨迹表面匹配作为任务 oracle。<!-- delta:SF-2026-ARXIV-2603-05553:end -->

边界：只支持 arXiv:2603.05553v1 §3.3.1 Architecture 的机制与 §4.3 Evaluation Results 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05553:end -->
<!-- books-review:SF-2026-ARXIV-2603-05578:start -->
### Tool-Genesis: A Task-Driven Tool Creation Benchmark for Self-Evolving Language Agent — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05578:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或 architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision 纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一 对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。<!-- existing:SF-2026-ARXIV-2603-05578:end -->

<!-- delta:SF-2026-ARXIV-2603-05578:start -->新证据差异：Tool-Genesis 从抽象需求开始，分别验证 interface compliance、functional correctness 与 downstream utility，使失败位置可归因。<!-- delta:SF-2026-ARXIV-2603-05578:end -->

边界：只支持 arXiv:2603.05578v1 §Appendix A Evaluation Methodology Details 的机制与 §5.2 Experimental Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05578:end -->
<!-- books-review:SF-2026-ARXIV-2603-05618:start -->
### Safer Reasoning Traces: Measuring and Mitigating Chain-of-Thought Leakage in LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05618:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：Run-centric 仍不自动给出因果结论。若 single-turn 使用 direct goal，而 multi-turn 同时改变 prompt、history、 sampling 和 backtracking，差异属于完整 workflow，不能单独归因于“多轮压力”。若 modality order 没有随机化、 缺少 same-content paired control，turn 后的变化也不能证明 representation transition 必然破坏 alignment。 Hard/soft 或多级 compliance taxonomy 能保留 partial leakage，却仍需 severity、actionability、false-positive/ negative 与 human disagreement；同一模型同时充当 attacker 与 judge 还会产生相关误差。<!-- existing:SF-2026-ARXIV-2603-05618:end -->

<!-- delta:SF-2026-ARXIV-2603-05618:start -->新证据差异：该工作把 PII 类型、风险权重和允许的 reasoning budget 绑定到同一评测合同，并比较多种推理时 gatekeeper。<!-- delta:SF-2026-ARXIV-2603-05618:end -->

边界：只支持 arXiv:2603.05618v1 §2 Methodology 的机制与 §3.3 Gatekeeper Evaluation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05618:end -->
<!-- books-review:SF-2026-ARXIV-2603-05637:start -->
### Real Faults in Model Context Protocol (MCP) Software: a Comprehensive Taxonomy — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05637:start -->已读 owner `books/part-07-agent/83-mcp.md` 与相邻章节。现有命题：在 server 数量少、由同一团队静态安装时，固定 allowlist、TLS endpoint 与 package review 足以建立初始信任；开放 catalog 或第三方 MCP server 动态加入后，连接成功和 OAuth scope 只能证明通信/委托成立，不能证明眼前 server identity、tool set、sensitivity 声明和受审 artifact 与批准对象相同。Host admission plane 应在注册时验证 server identity、tool allowlist、sensitivity metadata、attestation root 与 conformance vector，并把验证结果绑定到 protocol/version；effect-time authorization 仍按 principal、参数和业务 policy 独立执行。<!-- existing:SF-2026-ARXIV-2603-05637:end -->

<!-- delta:SF-2026-ARXIV-2603-05637:start -->新证据差异：exact-v1 的 `3. Methodology` 把论文方案定位到 协议身份、capability 声明、授权与审计状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05637:end -->

边界：只支持 arXiv:2603.05637v1 §3. Methodology 的机制与 §3.3. Taxonomy Creation and Validation 的公开 workload；§7. Conclusion and Future Works 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05637:end -->
<!-- books-review:SF-2026-ARXIV-2603-05692:start -->
### Parallelization Strategies for Dense LLM Deployment: Navigating Through Application-Specific Tradeoffs and Bottlenecks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05692:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与 架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明 suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与 GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。<!-- existing:SF-2026-ARXIV-2603-05692:end -->

<!-- delta:SF-2026-ARXIV-2603-05692:start -->新证据差异：exact-v1 的 `2.2. Overview of Llama 3.1-70B/-405B Models` 把论文方案定位到 图变换、kernel 选择、设备放置、数值精度与执行缓存；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05692:end -->

边界：只支持 arXiv:2603.05692v1 §2.2. Overview of Llama 3.1-70B/-405B Models 的机制与 §3. In-House Simulator and Its Validation 的公开 workload；§6. Discussion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05692:end -->
<!-- books-review:SF-2026-ARXIV-2603-05697:start -->
### MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05697:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-05697:end -->

<!-- delta:SF-2026-ARXIV-2603-05697:start -->新证据差异：MultiHaystack 将唯一可验证 evidence 放入四万级异构候选池，分别测 retrieval recall 与 evidence-conditioned reasoning。<!-- delta:SF-2026-ARXIV-2603-05697:end -->

边界：只支持 arXiv:2603.05697v1 §0.D.1 Implementation details 的机制与 §0.D.3 Evaluation Models 的公开 workload；§Appendix 0.J Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05697:end -->
<!-- books-review:SF-2026-ARXIV-2603-05706:start -->
### Reasoning Models Struggle to Control their Chains of Thought — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05706:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-05706:end -->

<!-- delta:SF-2026-ARXIV-2603-05706:start -->新证据差异：CoT-Control 将隐藏推理的可控性与最终输出可控性分开测量，并改变模型规模、RL 强度、test-time compute 和任务难度。<!-- delta:SF-2026-ARXIV-2603-05706:end -->

边界：只支持 arXiv:2603.05706v1 §2.2 Evaluation Design 的机制与 §2.2 Evaluation Design 的公开 workload；§Limitations. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05706:end -->
<!-- books-review:SF-2026-ARXIV-2603-05725:start -->
### Challenges and Design Considerations for Finding CUDA Bugs Through GPU-Native Fuzzing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05725:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**<!-- existing:SF-2026-ARXIV-2603-05725:end -->

<!-- delta:SF-2026-ARXIV-2603-05725:start -->新证据差异：论文将 behavior faithfulness 设为 GPU-native fuzzing 的核心合同，并梳理生成、调度、oracle 与 crash triage 的设计约束。<!-- delta:SF-2026-ARXIV-2603-05725:end -->

边界：只支持 arXiv:2603.05725v1 §4. The GPU-Native Design 的机制与 §5. Preliminary Experimental Results 的公开 workload；§6. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05725:end -->
<!-- books-review:SF-2026-ARXIV-2603-05739:start -->
### Revisiting the (Sub)Optimality of Best-of-N for Inference-Time Alignment — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05739:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2603-05739:end -->

<!-- delta:SF-2026-ARXIV-2603-05739:start -->新证据差异：论文改用 win-rate 作为推理时对齐目标，给出 BoN 最优条件，并提出在保持统计效率时限制 reward hacking 的变体。<!-- delta:SF-2026-ARXIV-2603-05739:end -->

边界：只支持 arXiv:2603.05739v1 §2.1 Inference-time alignment framework 的机制与 §5.1 Proof Sketch of Theorem 3 的公开 workload；§Conclusion. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05739:end -->
<!-- books-review:SF-2026-ARXIV-2603-05754:start -->
### Safe-Night VLA: Seeing the Unseen via Thermal-Perceptive Vision-Language-Action Models for Safety-Critical Manipulation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05754:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-05754:end -->

<!-- delta:SF-2026-ARXIV-2603-05754:start -->新证据差异：exact-v1 的 `III-A System Architecture and Adaptation Strategy` 把论文方案定位到 observation、action chunk、controller handoff 与环境反馈状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05754:end -->

边界：只支持 arXiv:2603.05754v1 §III-A System Architecture and Adaptation Strategy 的机制与 §V-C Exploratory Mechanism Analysis: Attention Ablation 的公开 workload；§V-B1 Limitations of RGB-Only and RGB-D Variants 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05754:end -->
<!-- books-review:SF-2026-ARXIV-2603-05786:start -->
### Proof-of-Guardrail in AI Agents and What (Not) to Trust from It — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05786:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-05786:end -->

<!-- delta:SF-2026-ARXIV-2603-05786:start -->新证据差异：Proof-of-Guardrail 把 agent 与公开 guardrail 放入 TEE，并用远程证明绑定代码身份和执行顺序。<!-- delta:SF-2026-ARXIV-2603-05786:end -->

边界：只支持 arXiv:2603.05786v1 §An agent skill-based proof-of-guardrail implementation. 的机制与 §3.2 Proof-of-Guardrail with TEE Attestation 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05786:end -->
<!-- books-review:SF-2026-ARXIV-2603-05800:start -->
### StreamWise: Serving Multi-Modal Generation in Real-Time at Scale — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05800:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：这里必须拆开两条控制链。论文 v1 的 dual-price update 使用 residual capacity 与历史 predicted action columns；它在实验中注入 output-length prediction noise，但没有把 predicted-vs-realized error 反馈进价格更新。 生产系统仍需由独立的 length predictor / calibration loop 消费实际完成长度并校准预测，这属于把论文机制接入 真实 serving 的补全责任，而不是论文已经证明的反馈算法。<!-- existing:SF-2026-ARXIV-2603-05800:end -->

<!-- delta:SF-2026-ARXIV-2603-05800:start -->新证据差异：StreamWise 将 modality pipeline、chunk readiness 与 deadline 纳入统一运行时状态，由 scheduler 决定阶段准入、批次拼接和 backpressure，而不是只优化单个 kernel。<!-- delta:SF-2026-ARXIV-2603-05800:end -->

边界：只支持 arXiv:2603.05800v1 §4.7. Implementation 的机制与 §5. Evaluation 的公开 workload；§7. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05800:end -->
<!-- books-review:SF-2026-ARXIV-2603-05815:start -->
### Hierarchical Latent Action Model — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05815:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-05815:end -->

<!-- delta:SF-2026-ARXIV-2603-05815:start -->新证据差异：HiLAM 在低层 latent-action extractor 之上聚合动作序列，形成具有更长时间尺度的 latent skill。<!-- delta:SF-2026-ARXIV-2603-05815:end -->

边界：只支持 arXiv:2603.05815v1 §3 Method 的机制与 §4.2.1 LIBERO Benchmark Results 的公开 workload；§5 Conclusion and Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05815:end -->
<!-- books-review:SF-2026-ARXIV-2603-05828:start -->
### HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05828:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-05828:end -->

<!-- delta:SF-2026-ARXIV-2603-05828:start -->新证据差异：HART 把定位、机制归因、evidence retrieval 与 causal tracing 组织为结构化链路，并建立联合标注数据。<!-- delta:SF-2026-ARXIV-2603-05828:end -->

边界：只支持 arXiv:2603.05828v1 §4.1.3. Implementation 的机制与 §4.2. Experimental Results 的公开 workload；§5. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05828:end -->
<!-- books-review:SF-2026-ARXIV-2603-05872:start -->
### Evolving Deception: When Agents Evolve, Deception Wins — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05872:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。 同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、 approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些 边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能 把运行中配置和人工干预归因成 foundation-model 单一缺陷。<!-- existing:SF-2026-ARXIV-2603-05872:end -->

<!-- delta:SF-2026-ARXIV-2603-05872:start -->新证据差异：论文在竞争式 bidding 环境中比较多条演化路径，并追踪 reflection 后的策略与内部 rationalization。<!-- delta:SF-2026-ARXIV-2603-05872:end -->

边界：只支持 arXiv:2603.05872v1 §Appendix A Self-Evolution Algorithm 的机制与 §4.3 Evaluation Configuration 的公开 workload；§8 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05872:end -->
<!-- books-review:SF-2026-ARXIV-2603-05881:start -->
### Confidence Before Answering: A Paradigm Shift for Efficient LLM Uncertainty Estimation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05881:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。<!-- existing:SF-2026-ARXIV-2603-05881:end -->

<!-- delta:SF-2026-ARXIV-2603-05881:start -->新证据差异：exact-v1 的 `3.2 Confidence-First Paradigm Definition` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05881:end -->

边界：只支持 arXiv:2603.05881v1 §3.2 Confidence-First Paradigm Definition 的机制与 §4.1.2 Evaluation Benchmarks 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05881:end -->
<!-- books-review:SF-2026-ARXIV-2603-05910:start -->
### The World Won't Stay Still: Programmable Evolution for Agent Benchmarks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05910:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？<!-- existing:SF-2026-ARXIV-2603-05910:end -->

<!-- delta:SF-2026-ARXIV-2603-05910:start -->新证据差异：exact-v1 的 `C.2 Tool Designer in Saturation Strategy` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05910:end -->

边界：只支持 arXiv:2603.05910v1 §C.2 Tool Designer in Saturation Strategy 的机制与 §4.4 State-Wise User Simulation and Evaluation 的公开 workload；§6 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05910:end -->
<!-- books-review:SF-2026-ARXIV-2603-05912:start -->
### DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05912:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-05912:end -->

<!-- delta:SF-2026-ARXIV-2603-05912:start -->新证据差异：exact-v1 的 `4.1 Methodology: The Micro-Gold Protocol` 把论文方案定位到 evaluation contract、覆盖分母、evidence lineage 与 release gate；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-05912:end -->

边界：只支持 arXiv:2603.05912v1 §4.1 Methodology: The Micro-Gold Protocol 的机制与 §7.3 Results on Other Factuality Benchmarks 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05912:end -->
<!-- books-review:SF-2026-ARXIV-2603-05931:start -->
### A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05931:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：把整张模型图放到标称 TOPS 更高的 accelerator 上，在 graph 规则、offload coverage 完整、host control 便宜且 Prefill/Decode shape 相近时最简单。LLM 改变了这个前提：Prefill 的大矩阵与 Decode 的小 batch、逐 token 控制可能偏好不同 backend；unsupported operators、tensor/KV conversion、wake/sleep、polling 和 host-device synchronization 又可能吞掉计算收益。<!-- existing:SF-2026-ARXIV-2603-05931:end -->

<!-- delta:SF-2026-ARXIV-2603-05931:start -->新证据差异：该加速器把 recurrent state 固定为片上持久对象，并围绕 decode 的更新依赖组织数据流，使每个 token 只搬运必要输入而非重载完整历史。<!-- delta:SF-2026-ARXIV-2603-05931:end -->

边界：只支持 arXiv:2603.05931v1 §IV-E System Overview 的机制与 §VI-E Ablation Analysis 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05931:end -->
<!-- books-review:SF-2026-ARXIV-2603-05959:start -->
### OVGGT: O(1) Constant-Cost Streaming Visual Geometry Transformer — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05959:start -->已读 owner `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 与相邻章节。现有命题：多轮 Tool loop 把同一问题扩展到离散 request 之间：每轮重算完整 transcript 最容易保证状态一致；当会话变长、多个 Agent 交错推进时，重复 prefix 又会反复支付 Prefill。一个受限的 stateful 分支让 sequence owner 跨轮持有 persistent KV，只摄取本轮新增的 \(\Delta_t\) token，并让 radix prefix cache 在 identity-compatible 的会话之间共享不可变前缀。Sequence pool 与 scheduler 负责 admission、lease、eviction 和 invalidation；prompt-lookup speculative decoding 只是可选的下游加速器，streaming validator 也只验证结构化输出，二者都不拥有 cache identity 的真值。<!-- existing:SF-2026-ARXIV-2603-05959:end -->

<!-- delta:SF-2026-ARXIV-2603-05959:start -->新证据差异：OVGGT 将历史压缩为固定大小的视觉几何状态，使新帧更新保持常数级 cache/compute contract。<!-- delta:SF-2026-ARXIV-2603-05959:end -->

边界：只支持 arXiv:2603.05959v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§E Failure Cases 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05959:end -->
<!-- books-review:SF-2026-ARXIV-2603-05960:start -->
### Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05960:start -->已读 owner `books/part-04-training-system/36-distributed-training.md` 与相邻章节。现有命题：本章使用 `B_micro` 表示每个 DP rank 的 micro-batch size， `gradient_accumulation_steps` 表示梯度累积次数，`data_parallel_degree` 表示 data-parallel degree，`B_global` 表示 global batch size，`P` 表示 参数量，`N` 表示总 GPU 数。为缩短后续公式，令 `A=gradient_accumulation_steps`、`D=data_parallel_degree`；这些别名不改变 Part IV 的统一 batch contract。<!-- existing:SF-2026-ARXIV-2603-05960:end -->

<!-- delta:SF-2026-ARXIV-2603-05960:start -->新证据差异：Omni-Masked Gradient Descent 以 mask traversal 分批更新参数子集，在降低同时驻留状态时维持收敛路径。<!-- delta:SF-2026-ARXIV-2603-05960:end -->

边界：只支持 arXiv:2603.05960v1 §3.2 Omni-Masked Gradient Descent 的机制与 §5.4 Pre-training Experiments of LLMs 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05960:end -->
<!-- books-review:SF-2026-ARXIV-2603-05974:start -->
### Balancing Latency and Accuracy of Code Completion via Local-Cloud Model Cascading — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-05974:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：只有请求已经超时才 drop，容易实现且不依赖预测，在轻载或短 pipeline 中完全合理；多模型 pipeline 里，失败请求 可能在到达 deadline 前已消耗多个 stage，反应式丢弃既回收不了过去的 compute，也可能保留了更不可能完成的请求。 主动策略把剩余 latency budget、下游 queue、当前 workload intensity 与 request progress 合成 risk signal，分别回答 “何时应取消”和“取消哪一个”。<!-- existing:SF-2026-ARXIV-2603-05974:end -->

<!-- delta:SF-2026-ARXIV-2603-05974:start -->新证据差异：论文把 local/cloud 选择建模为带质量估计的请求级 cascade，在提交前决定是否升级到远端模型。<!-- delta:SF-2026-ARXIV-2603-05974:end -->

边界：只支持 arXiv:2603.05974v1 §4.3. Implementation Details 的机制与 §5. Evaluation Results 的公开 workload；§6.5. Limitation 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-05974:end -->
<!-- books-review:SF-2026-ARXIV-2603-06001:start -->
### Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06001:start -->已读 owner `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 与相邻章节。现有命题：模型能识别物体、理解指令并生成动作 token，为什么还不等于机器人系统？VLA 是把 “A” 接到 VLM 后面，还是改变了训练与 runtime contract？大模型推理慢、控制频率高时如何分层？video generation 形成的动作想象能否直接执行？<!-- existing:SF-2026-ARXIV-2603-06001:end -->

<!-- delta:SF-2026-ARXIV-2603-06001:start -->新证据差异：ICBench 固定视觉场景并注入矛盾指令；IGAR 在推理时重分配 attention，使语言约束重新进入动作生成。<!-- delta:SF-2026-ARXIV-2603-06001:end -->

边界：只支持 arXiv:2603.06001v1 §3.2 Contradiction Taxonomy and Design Principles 的机制与 §5.6 Real-World Evaluation 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06001:end -->
<!-- books-review:SF-2026-ARXIV-2603-06003:start -->
### EvoESAP: Non-Uniform Expert Pruning for Sparse MoE — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06003:start -->已读 owner `books/part-02-model/21-moe.md` 与相邻章节。现有命题：Router 不变，placement owner 持有 replica mapping，quantization artifact 持有每个 expert 的 format/scale，runtime 按同一 epoch dispatch。它用 calibration、量化误差和更复杂的 artifact 组合换并行容量；traffic/importance drift、错误 scale、 副本版本不一致或热点迁移都可能同时破坏质量与平衡。显存充足、热点不稳定、质量回归不可接受时，应只重排、不量化 或回退单副本。exact-v1 的作者结果只支持所测 sparse MoE 与 calibration contract，不证明 ±0.6% 一类结果跨模型成立。<!-- existing:SF-2026-ARXIV-2603-06003:end -->

<!-- delta:SF-2026-ARXIV-2603-06003:start -->新证据差异：EvoESAP 把层内 expert 排序与跨层预算分开，用 teacher-forced acceptance proxy 搜索非均匀 sparsity。<!-- delta:SF-2026-ARXIV-2603-06003:end -->

边界：只支持 arXiv:2603.06003v1 §2.3 Other Compression Methods 的机制与 §4.2 Main results 的公开 workload；§Appendix C Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06003:end -->
<!-- books-review:SF-2026-ARXIV-2603-06007:start -->
### MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06007:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2603-06007:end -->

<!-- delta:SF-2026-ARXIV-2603-06007:start -->新证据差异：exact-v1 的 `3 System Design` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06007:end -->

边界：只支持 arXiv:2603.06007v1 §3 System Design 的机制与 §4 Evaluation and Analysis 的公开 workload；§Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06007:end -->
<!-- books-review:SF-2026-ARXIV-2603-06009:start -->
### Preventing Learning Stagnation in PPO by Scaling to 1 Million Parallel Environments — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06009:start -->已读 owner `books/part-04-training-system/32-ppo.md` 与相邻章节。现有命题：第 31 章已经得到 learned reward 与 KL constraint，但怎样把完整回答的 reward 变成 token-level 参数更新？为什么不能对同一批高 reward outputs 无限训练？PPO 的 probability ratio、advantage 与 clipping 分别在限制什么？<!-- existing:SF-2026-ARXIV-2603-06009:end -->

<!-- delta:SF-2026-ARXIV-2603-06009:start -->新证据差异：该工作把环境并发扩展到百万级并重组采样/更新数据流，用更广状态覆盖维持 policy improvement。<!-- delta:SF-2026-ARXIV-2603-06009:end -->

边界：只支持 arXiv:2603.06009v1 §Appendix F SFL Hand Designed Results 的机制与 §5.1 Robotics Results 的公开 workload；§8 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06009:end -->
<!-- books-review:SF-2026-ARXIV-2603-06081:start -->
### Lyapunov Probes for Hallucination Detection in Large Foundation Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06081:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-06081:end -->

<!-- delta:SF-2026-ARXIV-2603-06081:start -->新证据差异：Lyapunov probe 以扰动下置信单调衰减为训练约束，把局部稳定性作为 hallucination 风险信号。<!-- delta:SF-2026-ARXIV-2603-06081:end -->

边界：只支持 arXiv:2603.06081v1 §3 Method 的机制与 §4 Experiments 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06081:end -->
<!-- books-review:SF-2026-ARXIV-2603-06123:start -->
### Diffusion Language Models Are Natively Length-Aware — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06123:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。<!-- existing:SF-2026-ARXIV-2603-06123:end -->

<!-- delta:SF-2026-ARXIV-2603-06123:start -->新证据差异：论文指出 mask/denoise state 本身携带剩余长度信息，并据此让生成过程动态决定终止。<!-- delta:SF-2026-ARXIV-2603-06123:end -->

边界：只支持 arXiv:2603.06123v1 §3 Methodology 的机制与 §4.2 Benchmarks 的公开 workload；§7 Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06123:end -->
<!-- books-review:SF-2026-ARXIV-2603-06130:start -->
### A Hazard-Informed Data Pipeline for Robotics Physical Safety — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06130:start -->已读 owner `books/part-04-training-system/27-data.md` 与相邻章节。现有命题：按主题、安全分类或表面质量过滤 benign SFT data，在样本风险与参数更新方向高度相关时便宜而合理；但微调会改变 模型内部的 compliance boundary，一条内容本身无害的样本仍可能沿着与拒答能力相关的表示方向推动参数。约束从 “这条文本说了什么”变成“这条文本在当前 checkpoint、训练 recipe 下会造成什么更新”后，filter artifact 需要同时 记录内容判定与有限的 training-effect evidence：用于抽取 compliance direction 的 checkpoint、被选中的 safety-critical layers、projection score、threshold 以及最终 admission decision。数据 pipeline 拥有这份证据与 decision lineage；trainer 只能消费已版本化的过滤结果，不能把训练后才出现的 safety regression 追溯成一个无身份的 “数据质量问题”。<!-- existing:SF-2026-ARXIV-2603-06130:end -->

<!-- delta:SF-2026-ARXIV-2603-06130:start -->新证据差异：论文以 hazard taxonomy 驱动场景、trajectory 与标注采集，使 physical risk 成为可追踪的数据 lineage。<!-- delta:SF-2026-ARXIV-2603-06130:end -->

边界：只支持 arXiv:2603.06130v1 §1.3 Literature Overview 的机制与 §Evaluation 的公开 workload；§4 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06130:end -->
<!-- books-review:SF-2026-ARXIV-2603-06138:start -->
### Partial Policy Gradients for RL in LLMs — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06138:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 preferred/chosen 与 dispreferred/rejected response，`r_phi(x,y)` 表示 Reward Model score，`pi_theta(y|x)` 表示当前 policy，`pi_ref(y|x)` 表示 reference policy，`beta` 表示 KL regularization strength。<!-- existing:SF-2026-ARXIV-2603-06138:end -->

<!-- delta:SF-2026-ARXIV-2603-06138:start -->新证据差异：Partial Policy Gradients 只对由规则或估计器识别的责任片段施加 policy update，改变 credit-assignment 粒度。<!-- delta:SF-2026-ARXIV-2603-06138:end -->

边界：只支持 arXiv:2603.06138v1 §5.3 Baselines and Compared Methods 的机制与 §5.4 Main Results 的公开 workload；§G.9 Failure Mode Taxonomy 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06138:end -->
<!-- books-review:SF-2026-ARXIV-2603-06198:start -->
### LIT-RAGBench: Benchmarking Generator Capabilities of Large Language Models in Retrieval-Augmented Generation — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06198:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。<!-- existing:SF-2026-ARXIV-2603-06198:end -->

<!-- delta:SF-2026-ARXIV-2603-06198:start -->新证据差异：LIT-RAGBench 固定提供的 evidence，并系统改变 relevance、noise 与回答要求以单独测 generator contract。<!-- delta:SF-2026-ARXIV-2603-06198:end -->

边界：只支持 arXiv:2603.06198v1 §5.2. Evaluation Method 的机制与 §4.1.1. Evaluation Categories and Aspects 的公开 workload；§6. Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06198:end -->
<!-- books-review:SF-2026-ARXIV-2603-06199:start -->
### FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06199:start -->已读 owner `books/part-05-inference-system/49-tensorrt-llm.md` 与相邻章节。现有命题：GPU binary 到可分析 IR 的迁移不是指令文本替换：统一 register file 必须恢复 typed state，分支要重建显式 control flow，多指令 pattern 还要恢复组合语义。类型或控制流冲突时，生成貌似可执行的 IR 会把未知语义静默固化，因此 lifter 必须 fail closed 并保留 unsupported instruction surface。Typed LLVM IR 可成为审计和迁移的中间证据，但受支持架构、MUFU/texture 与完整 SIMT 语义限制；原生二进制验证仍不可删除。<!-- existing:SF-2026-ARXIV-2603-06199:end -->

<!-- delta:SF-2026-ARXIV-2603-06199:start -->新证据差异：FlashPrefill 联合发现 vertical、slash 与 block pattern，并用动态阈值直接裁剪长尾 block，改变 prefill execution plan。<!-- delta:SF-2026-ARXIV-2603-06199:end -->

边界：只支持 arXiv:2603.06199v1 §3.3 Comparison with Previous Methods. 的机制与 §4 Experiments 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06199:end -->
<!-- books-review:SF-2026-ARXIV-2603-06263:start -->
### SPOILER: TEE-Shielded DNN Partitioning of On-Device Secure Inference with Poison Learning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06263:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：分布式 inference 的 availability 不能只问 endpoint 是否按时返回。Fast / slow-path pipeline 若只在 deadline 前合并远端高质量结果，deadline 同时就是 semantic commit boundary：攻击者无需访问权重或 victim data，只要用 shaped burst 推迟 slow path，merger 就可能丢弃本应提高准确率的证据。系统仍及时响应，却发生 accuracy collapse。<!-- existing:SF-2026-ARXIV-2603-06263:end -->

<!-- delta:SF-2026-ARXIV-2603-06263:start -->新证据差异：SPOILER 将 TEE-shielded partition 与 poison-learning threat model 联合优化，显式划分可信/非可信执行边界。<!-- delta:SF-2026-ARXIV-2603-06263:end -->

边界：只支持 arXiv:2603.06263v1 §4 Methodology 的机制与 §5.2 Results: Security 的公开 workload；§Limitations of TBP: security vs. efficiency. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06263:end -->
<!-- books-review:SF-2026-ARXIV-2603-06274:start -->
### Stem: Rethinking Causal Information Flow in Sparse Attention — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06274:start -->已读 owner `books/part-02-model/14-self-attention.md` 与相邻章节。现有命题：本章的核心判断是：**Self Attention 是 content-dependent routing。**每个位置用 Query 描述自己在寻找什么，用 Key 描述自己可怎样被匹配，用 Value 提供真正被聚合的内容。<!-- existing:SF-2026-ARXIV-2603-06274:end -->

<!-- delta:SF-2026-ARXIV-2603-06274:start -->新证据差异：Stem 从 causal information flow 角度刻画稀疏拓扑，把路径可达性与每层选择共同纳入设计。<!-- delta:SF-2026-ARXIV-2603-06274:end -->

边界：只支持 arXiv:2603.06274v1 §2 Methodology 的机制与 §3.3 Ablation Studies 的公开 workload；§Limitations of Score-Aware Metric. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06274:end -->
<!-- books-review:SF-2026-ARXIV-2603-06317:start -->
### From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06317:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。<!-- existing:SF-2026-ARXIV-2603-06317:end -->

<!-- delta:SF-2026-ARXIV-2603-06317:start -->新证据差异：论文把 uncertainty reasoning 作为显式训练目标，并用 calibration、selective accuracy 与分布转移检查自报置信。<!-- delta:SF-2026-ARXIV-2603-06317:end -->

边界：只支持 arXiv:2603.06317v1 §3 Methodology 的机制与 §A.3 Evaluation 的公开 workload；§5 Discussion and Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06317:end -->
<!-- books-review:SF-2026-ARXIV-2603-06331:start -->
### WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06331:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-06331:end -->

<!-- delta:SF-2026-ARXIV-2603-06331:start -->新证据差异：exact-v1 的 `4.1 Curvature-guided Heterogeneous Token Prediction` 把论文方案定位到 latent state、action-conditioned transition 与 rollout commitment；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06331:end -->

边界：只支持 arXiv:2603.06331v1 §4.1 Curvature-guided Heterogeneous Token Prediction 的机制与 §5.2 World Generation Results 的公开 workload；§Failure of Uniform Strategies. 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06331:end -->
<!-- books-review:SF-2026-ARXIV-2603-06350:start -->
### MoEless: Efficient MoE LLM Serving via Serverless Computing — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06350:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：LLM request 的 KV footprint 会随未知输出长度增长。因此 admission 只检查“现在还有 blocks”可能 接受一组稍后必然不可行的 requests。更强的不变量是：在明确的 output estimate、preemption 和 reserve 假设下，当前选择之后的 future KV growth 仍有可行路径。<!-- existing:SF-2026-ARXIV-2603-06350:end -->

<!-- delta:SF-2026-ARXIV-2603-06350:start -->新证据差异：MoEless 将 expert 映射到可弹性实例，并把路由热度、冷启动与数据搬移作为 placement state；dense shared path 与稀疏 expert path 使用不同资源生命周期。<!-- delta:SF-2026-ARXIV-2603-06350:end -->

边界：只支持 arXiv:2603.06350v1 §3.2. Architecture and Workflow 的机制与 §6. Evaluation 的公开 workload；§8. Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06350:end -->
<!-- books-review:SF-2026-ARXIV-2603-06365:start -->
### ESAA-Security: An Event-Sourced, Verifiable Architecture for Agent-Assisted Security Audits of AI-Generated Code — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06365:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：控制权不能随 prompt 一并交给 coding model。模型只拥有 code proposal；security policy owner 定义不变量与 exception 规则，CI 以确定性功能测试、安全回归测试和 static analysis 执行检查并生成 receipt，repository owner 审阅 requirement revision、proposal、双重验证结果与 exception 后，才拥有 merge 或 revert authority。若 proposal 同时改写 policy、安全测试或 approved template，这些变化必须进入独立审批，而不能用“测试已通过”自证。这样可以阻止显式 usability objective 静默覆盖安全约束，并把每次合并追溯到授权它的 requirement revision；代价是规范与测试维护、额外 CI 延迟、false reject，以及 requirement、policy 与 tests 之间的漂移。<!-- existing:SF-2026-ARXIV-2603-06365:end -->

<!-- delta:SF-2026-ARXIV-2603-06365:start -->新证据差异：ESAA-Security 让 agent 只提交结构化 intent，由 orchestrator 验证后写 append-only event log，再重放投影与 hash 校验。<!-- delta:SF-2026-ARXIV-2603-06365:end -->

边界：只支持 arXiv:2603.06365v1 §3 ESAA-Security Architecture 的机制与 §6 Evaluation Design and Research Questions 的公开 workload；§8 Discussion, Limitations, and Threats to Validity 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06365:end -->
<!-- books-review:SF-2026-ARXIV-2603-06394:start -->
### Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06394:start -->已读 owner `books/part-07-agent/81-workflow.md` 与相邻章节。现有命题：ARTS 在 scientific search tree 中把 hypothesis merit 与 execution quality 分开；audit node 的 code/log 后决定 repair 同一 idea 还是 pivot，并把 search history用于 scientist test-time training。 ViRGo 根据目标尺度与置信度，在 global view、patch zoom 与 attention-guided visual retrieval间路由，避免固定高分辨率同时丢 context 或浪费 token。 StickyInvoc 把昂贵 model/runtime state 的 create/destroy 与 invocation goodput 解耦：sticky task 持有 node-local state，后续 invocation 继承但不销毁，抢占时按 state owner 重建。<!-- existing:SF-2026-ARXIV-2603-06394:end -->

<!-- delta:SF-2026-ARXIV-2603-06394:start -->新证据差异：exact-v1 的 `5.1 Architecture overview` 把论文方案定位到 workflow graph、checkpoint、重试与演进状态；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06394:end -->

边界：只支持 arXiv:2603.06394v1 §5.1 Architecture overview 的机制与 §5.3 Validation framework 的公开 workload；§6.5 Future work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06394:end -->
<!-- books-review:SF-2026-ARXIV-2603-06403:start -->
### Adapter-Augmented Bandits for Online Multi-Constrained Multi-Modal Inference Scheduling — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06403:start -->已读 owner `books/part-05-inference-system/56-inference-scheduling.md` 与相邻章节。现有命题：本章的核心判断是：**推理调度不是单一优先队列，而是一组跨时间尺度的决策：admission 决定是否承诺服务，iteration scheduling 决定下一轮 token work，routing/placement 决定计算与 KV 在哪里，autoscaling 决定未来 capacity。**<!-- existing:SF-2026-ARXIV-2603-06403:end -->

<!-- delta:SF-2026-ARXIV-2603-06403:start -->新证据差异：exact-v1 的 `3.1 Reward and Cost Predictor Design` 把论文方案定位到 准入、批处理、优先级、路由和资源选择；该项作为受限实现案例保留，不据此建立新的 canonical owner。<!-- delta:SF-2026-ARXIV-2603-06403:end -->

边界：只支持 arXiv:2603.06403v1 §3.1 Reward and Cost Predictor Design 的机制与 §5.3 Experimental Results and Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06403:end -->
<!-- books-review:SF-2026-ARXIV-2603-06413:start -->
### A Reference Architecture of Reinforcement Learning Frameworks — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06413:start -->已读 owner `books/part-04-training-system/31-rlhf.md` 与相邻章节。现有命题：本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 preferred/chosen 与 dispreferred/rejected response，`r_phi(x,y)` 表示 Reward Model score，`pi_theta(y|x)` 表示当前 policy，`pi_ref(y|x)` 表示 reference policy，`beta` 表示 KL regularization strength。<!-- existing:SF-2026-ARXIV-2603-06413:end -->

<!-- delta:SF-2026-ARXIV-2603-06413:start -->新证据差异：该工作从 18 个框架归纳 reference architecture，以组件、数据流和控制关系重建可比较的训练系统 contract。<!-- delta:SF-2026-ARXIV-2603-06413:end -->

边界：只支持 arXiv:2603.06413v1 §III Methodology 的机制与 §VI Results Evaluation and Quality Assessment 的公开 workload；§VIII Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06413:end -->
<!-- books-review:SF-2026-ARXIV-2603-06422:start -->
### Before You Hand Over the Wheel: Evaluating LLMs for Security Incident Analysis — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06422:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2603-06422:end -->

<!-- delta:SF-2026-ARXIV-2603-06422:start -->新证据差异：SIABENCH 将深度调查与告警分诊拆为可扩展场景，并用 agent 执行网络、内存、恶意样本和日志分析。<!-- delta:SF-2026-ARXIV-2603-06422:end -->

边界：只支持 arXiv:2603.06422v1 §IV-B Agent Design 的机制与 §V Evaluation 的公开 workload；§V-B3 Primary Factors of LLM’s Failure (RQ3) 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06422:end -->
<!-- books-review:SF-2026-ARXIV-2603-06444:start -->
### Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06444:start -->已读 owner `books/part-05-inference-system/44-decode.md` 与相邻章节。现有命题：本章的核心判断是：**Decode 是受 autoregressive dependency 约束的逐 token 状态机；单请求每一步的矩阵维度很小，却需要读取大量 weights 和历史 KV，因此性能由 memory movement、batch composition 与 iteration cadence 共同决定。**<!-- existing:SF-2026-ARXIV-2603-06444:end -->

<!-- delta:SF-2026-ARXIV-2603-06444:start -->新证据差异：论文训练模型在 prosodic boundary 提前停止，并用滑动窗口携带有限文本/语音状态，实现有界上下文拼接。<!-- delta:SF-2026-ARXIV-2603-06444:end -->

边界：只支持 arXiv:2603.06444v1 §3.4.2 Baselines and Proposed Method 的机制与 §3.3 Evaluation Metrics 的公开 workload；§4.3 Ablation Studies 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06444:end -->
<!-- books-review:SF-2026-ARXIV-2603-06445:start -->
### What if? Emulative Simulation with World Models for Situated Reasoning — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06445:start -->已读 owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md` 与相邻章节。现有命题：本章的核心判断是：**World Model 不是“生成世界画面”的名字，而是围绕环境状态转移建立的可检验契约。它必须把当前状态、action、预测 horizon 与 uncertainty 绑定起来，并始终区分 observed state、latent belief 和 imagined state。**视觉逼真可以是有用表示，却不能代替 action consequence、controllability 与 closed-loop outcome evidence。<!-- existing:SF-2026-ARXIV-2603-06445:end -->

<!-- delta:SF-2026-ARXIV-2603-06445:start -->新证据差异：WanderDream 用 world model 生成从当前状态到目标的 imagined trajectory，并分别评测起点、路径与终态推理。<!-- delta:SF-2026-ARXIV-2603-06445:end -->

边界：只支持 arXiv:2603.06445v1 §5.1 Implementation Details 的机制与 §Appendix 0.C Evaluation 的公开 workload；§6 Limitations and Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06445:end -->
<!-- books-review:SF-2026-ARXIV-2603-06450:start -->
### Data Analogies Enable Efficient Cross-Embodiment Transfer — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06450:start -->已读 owner `books/part-04-training-system/27-data.md` 与相邻章节。现有命题：多模态 raw sample、codec token、frame/second 和 action trajectory 不能用一个未经定义的“token 数”混合计量。第23～26章拥有表示与行动语义；本章拥有这些样本怎样被选择、版本化、配比与送入优化。这个边界使 representation 研究不会寄居于 Data，也使 Data 不退化成文件清单。<!-- existing:SF-2026-ARXIV-2603-06450:end -->

<!-- delta:SF-2026-ARXIV-2603-06450:start -->新证据差异：论文用配对 data analogy 对齐场景、任务或 trajectory，区分 perceptual diversity 与 morphology transfer 所需证据。<!-- delta:SF-2026-ARXIV-2603-06450:end -->

边界：只支持 arXiv:2603.06450v1 §III Cross-Embodiment Data Analogies 的机制与 §Evaluation Tasks 的公开 workload；§VI Limitations 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06450:end -->
<!-- books-review:SF-2026-ARXIV-2603-06453:start -->
### Pinterest Canvas: Large-Scale Image Generation at Pinterest — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06453:start -->已读 owner `books/part-06-ai-infrastructure/73-production-best-practice.md` 与相邻章节。现有命题：本章的核心判断是：**生产化不是在功能完成后追加监控与安全，而是让 artifact、deployment、SLO、evidence、cost、tenancy、security 和 recovery 从设计时就共享同一身份与控制闭环。**<!-- existing:SF-2026-ARXIV-2603-06453:end -->

<!-- delta:SF-2026-ARXIV-2603-06453:start -->新证据差异：Pinterest Canvas 以共享 foundation diffusion model 为起点，再通过任务数据产生专用 variant，并把数据、训练、推理和 A/B release 串成产品流水线。<!-- delta:SF-2026-ARXIV-2603-06453:end -->

边界：只支持 arXiv:2603.06453v1 §3. System Overview 的机制与 §5.1. Offline Evaluations for Outpainting 的公开 workload；§6. Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06453:end -->
<!-- books-review:SF-2026-ARXIV-2603-06508:start -->
### When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffusion Models — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06508:start -->已读 owner `books/part-06-ai-infrastructure/72-security.md` 与相邻章节。现有命题：从 single-turn text、isolated multimodal 或 multi-turn text，演进到 run-centric multimodal campaign，获得的是 transition-level attribution：哪一次表示变换、反馈或重试之后 policy 发生变化。新增代价包括有害 media 的 access/retention/deletion、campaign resume correctness、cache poisoning、provider drift、judge injection 与更高 成本。只保存最终 attack-success rate 会丢掉这些 state，也无法重放或修复失败路径。<!-- existing:SF-2026-ARXIV-2603-06508:end -->

<!-- delta:SF-2026-ARXIV-2603-06508:start -->新证据差异：论文用 Trigger Modality Attribution 与 Cross-Trigger Interaction 分解各模态贡献，识别 backdoor modality collapse。<!-- delta:SF-2026-ARXIV-2603-06508:end -->

边界：只支持 arXiv:2603.06508v1 §4 Problem Formulation 的机制与 §5.2 Results Analysis 的公开 workload；§6 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06508:end -->
<!-- books-review:SF-2026-ARXIV-2603-06569:start -->
### Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06569:start -->已读 owner `books/part-03-multimodal-world-models/23-multimodal-representation.md` 与相邻章节。现有命题：前者仍把选中区域解码为 RGB，兼容已有 vision encoder，却可能漏掉 codec metadata 未显著标记的语义变化； 后者减少重复 decode/encode work，却把 codec、GOP、motion vector、residual layout 与 tokenizer 一起变成模型 输入协议。Transcoding、随机 seek、corrupted stream、不同 codec/profile 与 frame-rate conversion 都可能改变 token identity。Dense frames 在格式多样、证据完整性优先或 codec path 不可信时仍成立。<!-- existing:SF-2026-ARXIV-2603-06569:end -->

<!-- delta:SF-2026-ARXIV-2603-06569:start -->新证据差异：Penguin-VL 从 text-only LLM 初始化视觉 encoder，测试表示目标而非单纯扩大模型规模的替代路线。<!-- delta:SF-2026-ARXIV-2603-06569:end -->

边界：只支持 arXiv:2603.06569v1 §4.1 Implementation Details 的机制与 §4.3 Image Benchmarks 的公开 workload；§6.2 Future Work 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06569:end -->
<!-- books-review:SF-2026-ARXIV-2603-06577:start -->
### Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06577:start -->已读 owner `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` 与相邻章节。现有命题：这让 exploration 成为除模型规模和每样本计算之外的第三条训练计算轴，但没有创造更可靠的 ground truth。候选数增加 会线性或超线性放大生成与筛选成本，选择器偏差还会把某种 mode 固化成训练偏好。固定单匹配在数据近单峰、预算紧或 scorer 不可信时仍合理；多候选探索只在候选多样性、selection contract 和单位训练预算收益一起验证时成立。作者的 受限 scaling curve 不能证明它会普遍替代 AR、diffusion 或 masked generation，只说明 training-time sampling policy 本身也需要被版本化和计量。<!-- existing:SF-2026-ARXIV-2603-06577:end -->

<!-- delta:SF-2026-ARXIV-2603-06577:start -->新证据差异：Omni-Diffusion 以 mask-based discrete diffusion 联合建模文本、图像与语音 token，并以模态专属 codec、长度控制和并行去噪保留各模态的生成边界。<!-- delta:SF-2026-ARXIV-2603-06577:end -->

边界：只支持 arXiv:2603.06577v1 §3.2 Model Architecture 的机制与 §Speech-Vision Alignment Evaluation 的公开 workload；§5 Conclusion 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **No Change — Existing Coverage**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06577:end -->
<!-- books-review:SF-2026-ARXIV-2603-06578:start -->
### Multimodal Large Language Models as Image Classifiers — Books Comparison

<!-- existing:SF-2026-ARXIV-2603-06578:start -->已读 owner `books/part-06-ai-infrastructure/66-evaluation-system.md` 与相邻章节。现有命题：多模态输入的来源由 ingestion path、artifact metadata 和 transform lineage 决定。若 evaluator 只问模型“这条信息来自图像还是文本”，模型可能把提示词中的 `image` 与语义或句法 cue 绑定，而不是读取真实 modality provenance。<!-- existing:SF-2026-ARXIV-2603-06578:end -->

<!-- delta:SF-2026-ARXIV-2603-06578:start -->新证据差异：论文把 closed-world、multiple-choice 与 open-world 协议拆开，并显式改变重标注、响应格式、OOV 处理、mapping encoder、batch size、顺序和组成，显示它们共同构成 EvalRun identity。<!-- delta:SF-2026-ARXIV-2603-06578:end -->

边界：只支持 arXiv:2603.06578v1 §2.4 Model and class names overview 的机制与 §2.2 Evaluation metric 的公开 workload；§4 Conclusions 之外不外推生产 SLO、多租户、跨硬件或长期可靠性。 作者侧决定为 **Integrate**；Integrate 项仅进入串行队列，尚未写回。
<!-- books-review:SF-2026-ARXIV-2603-06578:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260309-COVERAGE | fresh-context:march-lane-a-reviewer | coverage | coverage:SRC-ARXIV:20260309 | — | all 527 raw title+abstract rows independently adjudicated; false negatives corrected=39; false positives removed=0; receipt sha256=1a809e7da3a7e0cad1ee9f771a3346f2b9c5f45554451c835030cfd6a818e42c; Weekly dependency=0 | passed |
| SA-20260309-EVIDENCE | fresh-context:march-lane-a-reviewer | evidence | review:SF-2026-ARXIV-2603-05517; review:SF-2026-ARXIV-2603-05520; review:SF-2026-ARXIV-2603-05528; review:SF-2026-ARXIV-2603-05540; review:SF-2026-ARXIV-2603-05553; review:SF-2026-ARXIV-2603-05578; review:SF-2026-ARXIV-2603-05618; review:SF-2026-ARXIV-2603-05637; review:SF-2026-ARXIV-2603-05692; review:SF-2026-ARXIV-2603-05697; review:SF-2026-ARXIV-2603-05706; review:SF-2026-ARXIV-2603-05725; review:SF-2026-ARXIV-2603-05739; review:SF-2026-ARXIV-2603-05754; review:SF-2026-ARXIV-2603-05786; review:SF-2026-ARXIV-2603-05800; review:SF-2026-ARXIV-2603-05815; review:SF-2026-ARXIV-2603-05828; review:SF-2026-ARXIV-2603-05872; review:SF-2026-ARXIV-2603-05881; review:SF-2026-ARXIV-2603-05910; review:SF-2026-ARXIV-2603-05912; review:SF-2026-ARXIV-2603-05931; review:SF-2026-ARXIV-2603-05959; review:SF-2026-ARXIV-2603-05960; review:SF-2026-ARXIV-2603-05974; review:SF-2026-ARXIV-2603-06001; review:SF-2026-ARXIV-2603-06003; review:SF-2026-ARXIV-2603-06007; review:SF-2026-ARXIV-2603-06009; review:SF-2026-ARXIV-2603-06081; review:SF-2026-ARXIV-2603-06123; review:SF-2026-ARXIV-2603-06130; review:SF-2026-ARXIV-2603-06138; review:SF-2026-ARXIV-2603-06198; review:SF-2026-ARXIV-2603-06199; review:SF-2026-ARXIV-2603-06263; review:SF-2026-ARXIV-2603-06274; review:SF-2026-ARXIV-2603-06317; review:SF-2026-ARXIV-2603-06331; review:SF-2026-ARXIV-2603-06350; review:SF-2026-ARXIV-2603-06365; review:SF-2026-ARXIV-2603-06394; review:SF-2026-ARXIV-2603-06403; review:SF-2026-ARXIV-2603-06413; review:SF-2026-ARXIV-2603-06422; review:SF-2026-ARXIV-2603-06444; review:SF-2026-ARXIV-2603-06445; review:SF-2026-ARXIV-2603-06450; review:SF-2026-ARXIV-2603-06453; review:SF-2026-ARXIV-2603-06508; review:SF-2026-ARXIV-2603-06569; review:SF-2026-ARXIV-2603-06577; review:SF-2026-ARXIV-2603-06578 | — | exact-v1, Score V2, owner, locator-role and claim boundary independently audited for 54 candidates; receipt sha256=3794e84b3759000ca6ae88851d24c310145e8a2f5cc16b3068bffceb1bac9b2a | passed |
| SA-20260309-SELECTION | fresh-context:march-lane-a-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | — | review count and three-unit narrative selection kept separate | passed |
| SA-20260309-BOOKS | fresh-context:march-lane-a-reviewer | books | validator:books-comparison-v1 | FINDING-BOOKS-WRITEBACK-PENDING: 4 Integrate proposals require root serial reconciliation | no Books written; root must serially reconcile the date-specific queue, write canonical owners in date order, and run non-writer post-write audit | open |

## 8. Ignored Noise

完整逐项 closure 见 `papers/2026/03/_sources/daily-20260309/screening-ledger-final.json`；withdrawn family 只保留 identity/status，不保留 selected、Review 或 Books 痕迹。

## 9. Recommended Action

Coverage、Evidence 与 Selection 的独立审计已完成；由 root 按日期顺序复核并串行执行 4 项 Integrate 建议，再执行非写作者 post-write audit。

## 10. Repository Changes

- 新增本日 Daily 与 source packet。
- 未修改 `books/`、Weekly、`docs/LEARNING_STATE.md` 或月级共享索引。

## 11. Open Questions

- 0 项 exact-v1 仍 blocked。
- `SRC-ARXIV` 的独立 retained false-positive / closure false-negative audit 已完成；open candidates=0。
- fresh-context Coverage / Evidence / Selection audit 已完成；仅 Integrate 串行 writeback 与 post-write Books audit 尚未完成。

## 12. Sources

- [arXiv](https://arxiv.org/) — exact-v1 primary manuscript and status。
- DataCite March frozen snapshot — identity/title/abstract/submission provenance only。

### Materials Request Ledger

<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |


## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Closed`（SRC-ARXIV 全量枚举、严格窗口、withdrawn 与全 raw FP/FN 审计已闭合）
- Evidence: `Passed`（fresh-context exact-v1、Score、owner、locator-role 与 claim boundary 审计；open candidates=0）
- Books: `Open`（Integrate queue=4，未写回）
- unresolved findings: 4
- Raw identities=527；retained=54；retain rate=10.25%；closures=473。
