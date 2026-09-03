# Daily Research — 2026-07-16

**Research Date:** 2026-07-16

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-15 09:00:00 ～ 2026-07-16 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **446** 个 identity；全量 title + abstract 筛选后冻结 **62** 个候选与 **384** 个 family-specific closure，retain rate **13.90%**。exact-v1 Review 为 62/62：Deep 23、Standard 39、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-16 |
| Window End | 2026-07-16 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-16-0900-v2.1-sha256:46245aa1c0816ac55cb270d515e8097a701cc61f13d344875cc6ff64d29354a1 |
| Denominator Frozen At | 2026-09-04T06:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260716:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-15T09:00:00+08:00 | 2026-07-16T09:00:00+08:00 | 2026-09-04T06:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 446 | SF-2026-ARXIV-2607-13037;SF-2026-ARXIV-2607-13048;SF-2026-ARXIV-2607-13062;SF-2026-ARXIV-2607-13068;SF-2026-ARXIV-2607-13071;SF-2026-ARXIV-2607-13075;SF-2026-ARXIV-2607-13078;SF-2026-ARXIV-2607-13083;SF-2026-ARXIV-2607-13085;SF-2026-ARXIV-2607-13091;SF-2026-ARXIV-2607-13093;SF-2026-ARXIV-2607-13095;SF-2026-ARXIV-2607-13124;SF-2026-ARXIV-2607-13157;SF-2026-ARXIV-2607-13172;SF-2026-ARXIV-2607-13184;SF-2026-ARXIV-2607-13205;SF-2026-ARXIV-2607-13220;SF-2026-ARXIV-2607-13221;SF-2026-ARXIV-2607-13285;SF-2026-ARXIV-2607-13298;SF-2026-ARXIV-2607-13305;SF-2026-ARXIV-2607-13332;SF-2026-ARXIV-2607-13359;SF-2026-ARXIV-2607-13389;SF-2026-ARXIV-2607-13396;SF-2026-ARXIV-2607-13399;SF-2026-ARXIV-2607-13410;SF-2026-ARXIV-2607-13411;SF-2026-ARXIV-2607-13418;SF-2026-ARXIV-2607-13429;SF-2026-ARXIV-2607-13441;SF-2026-ARXIV-2607-13465;SF-2026-ARXIV-2607-13474;SF-2026-ARXIV-2607-13477;SF-2026-ARXIV-2607-13511;SF-2026-ARXIV-2607-13527;SF-2026-ARXIV-2607-13541;SF-2026-ARXIV-2607-13591;SF-2026-ARXIV-2607-13594;SF-2026-ARXIV-2607-13596;SF-2026-ARXIV-2607-13605;SF-2026-ARXIV-2607-13618;SF-2026-ARXIV-2607-13640;SF-2026-ARXIV-2607-13649;SF-2026-ARXIV-2607-13651;SF-2026-ARXIV-2607-13683;SF-2026-ARXIV-2607-13705;SF-2026-ARXIV-2607-13716;SF-2026-ARXIV-2607-13718;SF-2026-ARXIV-2607-13753;SF-2026-ARXIV-2607-13854;SF-2026-ARXIV-2607-13884;SF-2026-ARXIV-2607-13920;SF-2026-ARXIV-2607-13921;SF-2026-ARXIV-2607-13926;SF-2026-ARXIV-2607-13987;SF-2026-ARXIV-2607-13988;SF-2026-ARXIV-2607-14004;SF-2026-ARXIV-2607-14005;SF-2026-ARXIV-2607-14047;SF-2026-ARXIV-2607-14076 | all registered category pages; cross-category dedup complete | 2026-07-16T09:00:00+08:00 | sha256:46245aa1c0816ac55cb270d515e8097a701cc61f13d344875cc6ff64d29354a1 | — |
<!-- coverage:SRC-ARXIV:20260716:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13037 | arXiv:2607.13037v1 | paper-v1:2607.13037 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13037 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13048 | arXiv:2607.13048v1 | paper-v1:2607.13048 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13048 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13062 | arXiv:2607.13062v1 | paper-v1:2607.13062 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13062 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13068 | arXiv:2607.13068v1 | paper-v1:2607.13068 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13068 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13071 | arXiv:2607.13071v1 | paper-v1:2607.13071 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13071 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13075 | arXiv:2607.13075v1 | paper-v1:2607.13075 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13075 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13078 | arXiv:2607.13078v1 | paper-v1:2607.13078 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13078 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13083 | arXiv:2607.13083v1 | paper-v1:2607.13083 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13083 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13085 | arXiv:2607.13085v1 | paper-v1:2607.13085 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13085 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13091 | arXiv:2607.13091v1 | paper-v1:2607.13091 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13091 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13093 | arXiv:2607.13093v1 | paper-v1:2607.13093 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13093 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13095 | arXiv:2607.13095v1 | paper-v1:2607.13095 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13095 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13124 | arXiv:2607.13124v1 | paper-v1:2607.13124 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13124 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13157 | arXiv:2607.13157v1 | paper-v1:2607.13157 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13157 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13172 | arXiv:2607.13172v1 | paper-v1:2607.13172 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13172 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13184 | arXiv:2607.13184v1 | paper-v1:2607.13184 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13184 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13205 | arXiv:2607.13205v1 | paper-v1:2607.13205 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13205 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13220 | arXiv:2607.13220v1 | paper-v1:2607.13220 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13220 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13221 | arXiv:2607.13221v1 | paper-v1:2607.13221 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13221 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13285 | arXiv:2607.13285v1 | paper-v1:2607.13285 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13285 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13298 | arXiv:2607.13298v1 | paper-v1:2607.13298 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13298 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13305 | arXiv:2607.13305v1 | paper-v1:2607.13305 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13305 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13332 | arXiv:2607.13332v1 | paper-v1:2607.13332 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13332 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13359 | arXiv:2607.13359v1 | paper-v1:2607.13359 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13359 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13389 | arXiv:2607.13389v1 | paper-v1:2607.13389 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13389 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13396 | arXiv:2607.13396v1 | paper-v1:2607.13396 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13396 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13399 | arXiv:2607.13399v1 | paper-v1:2607.13399 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13399 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13410 | arXiv:2607.13410v1 | paper-v1:2607.13410 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13410 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13411 | arXiv:2607.13411v1 | paper-v1:2607.13411 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13411 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13418 | arXiv:2607.13418v1 | paper-v1:2607.13418 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13418 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13429 | arXiv:2607.13429v1 | paper-v1:2607.13429 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13429 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13441 | arXiv:2607.13441v1 | paper-v1:2607.13441 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13441 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13465 | arXiv:2607.13465v1 | paper-v1:2607.13465 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13465 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13474 | arXiv:2607.13474v1 | paper-v1:2607.13474 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13474 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13477 | arXiv:2607.13477v1 | paper-v1:2607.13477 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13477 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13511 | arXiv:2607.13511v1 | paper-v1:2607.13511 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13511 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13527 | arXiv:2607.13527v1 | paper-v1:2607.13527 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13527 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13541 | arXiv:2607.13541v1 | paper-v1:2607.13541 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13541 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13591 | arXiv:2607.13591v1 | paper-v1:2607.13591 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13591 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13594 | arXiv:2607.13594v1 | paper-v1:2607.13594 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13594 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13596 | arXiv:2607.13596v1 | paper-v1:2607.13596 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13596 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13605 | arXiv:2607.13605v1 | paper-v1:2607.13605 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13605 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13618 | arXiv:2607.13618v1 | paper-v1:2607.13618 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13618 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13640 | arXiv:2607.13640v1 | paper-v1:2607.13640 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13640 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13649 | arXiv:2607.13649v1 | paper-v1:2607.13649 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13649 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13651 | arXiv:2607.13651v1 | paper-v1:2607.13651 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13651 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13683 | arXiv:2607.13683v1 | paper-v1:2607.13683 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13683 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13705 | arXiv:2607.13705v1 | paper-v1:2607.13705 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13705 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13716 | arXiv:2607.13716v1 | paper-v1:2607.13716 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13716 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13718 | arXiv:2607.13718v1 | paper-v1:2607.13718 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13718 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13753 | arXiv:2607.13753v1 | paper-v1:2607.13753 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13753 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13854 | arXiv:2607.13854v1 | paper-v1:2607.13854 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13854 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13884 | arXiv:2607.13884v1 | paper-v1:2607.13884 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13884 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13920 | arXiv:2607.13920v1 | paper-v1:2607.13920 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13920 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13921 | arXiv:2607.13921v1 | paper-v1:2607.13921 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13921 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13926 | arXiv:2607.13926v1 | paper-v1:2607.13926 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13926 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13987 | arXiv:2607.13987v1 | paper-v1:2607.13987 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13987 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13988 | arXiv:2607.13988v1 | paper-v1:2607.13988 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13988 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14004 | arXiv:2607.14004v1 | paper-v1:2607.14004 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14004 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14005 | arXiv:2607.14005v1 | paper-v1:2607.14005 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-14005 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14047 | arXiv:2607.14047v1 | paper-v1:2607.14047 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14047 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-14076 | arXiv:2607.14076v1 | paper-v1:2607.14076 | 2026-W29 | 2026-07-16 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-14076 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13037 | RP-602cae08d5085901 | deep | arXiv:2607.13037v1 | SRC-ARXIV@arXiv:2607.13037v1 | https://arxiv.org/html/2607.13037v1#S4 — 4 System Design; https://arxiv.org/html/2607.13037v1#S4.SS1 — 4.1 Architecture Overview | https://arxiv.org/html/2607.13037v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.13037v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.13037v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13037v1#S7 — 7 Conclusion | Exact v1 links https://github.com/tzbkk/originblame, https://github.com/tzbkk/rust-originblame, https://github.com/huggingface/datatrove; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13037 | complete |
| SF-2026-ARXIV-2607-13048 | RP-9d841a16ce1bb001 | standard | arXiv:2607.13048v1 | SRC-ARXIV@arXiv:2607.13048v1 | https://arxiv.org/html/2607.13048v1#S4 — 4 System Architecture; https://arxiv.org/html/2607.13048v1#S3 — 3 Theoretical Framework | https://arxiv.org/html/2607.13048v1#Pt0.A2 — Appendix 0.B Experimental Details; https://arxiv.org/html/2607.13048v1#S3.SS8 — 3.8 Roadmap from theory to evaluation | https://arxiv.org/html/2607.13048v1#Pt0.A5 — Appendix 0.E Limitations; https://arxiv.org/html/2607.13048v1#S7.SS2 — 7.2 LLM Failure Analysis | Exact v1 links https://github.com/GeoffreyWang1117/event-triggered-llm-streaming, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13048 | complete |
| SF-2026-ARXIV-2607-13062 | RP-e402ca0b9bd74e66 | deep | arXiv:2607.13062v1 | SRC-ARXIV@arXiv:2607.13062v1 | https://arxiv.org/html/2607.13062v1#S2 — 2 Setup and the calibration gate; https://arxiv.org/html/2607.13062v1#S5 — 5 Decide: the speculation-decision pass; https://arxiv.org/html/2607.13062v1#S6 — 6 Execute: the runtime executor | https://arxiv.org/html/2607.13062v1#S3 — 3 Measure: the predictability and speedup bracket; https://arxiv.org/html/2607.13062v1#S4 — 4 Bound, refute, and explain: the misprediction blast radius | https://arxiv.org/html/2607.13062v1#S8 — 8 Limitations and future work; https://arxiv.org/html/2607.13062v1#S9 — 9 Conclusion | Exact v1 links https://codeberg.org/rylanmalarchick/speculative-qec, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13062 | complete |
| SF-2026-ARXIV-2607-13068 | RP-45aad037686af4ef | deep | arXiv:2607.13068v1 | SRC-ARXIV@arXiv:2607.13068v1 | https://arxiv.org/html/2607.13068v1#S5 — 5 A rebalanced design: less F, more S, deliberately less B | https://arxiv.org/html/2607.13068v1#S1 — 1 Introduction: the decode inefficiency; https://arxiv.org/html/2607.13068v1#S2 — 2 Two hardware constants: F/B and F/S | https://arxiv.org/html/2607.13068v1#S8 — 8 Conclusion | Exact v1 links https://github.com/deepseek-ai/DeepGEMM, https://github.com/dzhsurf/deepseek-v3-r1-deploy-and-benchmarks, https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13068 | complete |
| SF-2026-ARXIV-2607-13071 | RP-26f56c352bb64f4b | deep | arXiv:2607.13071v1 | SRC-ARXIV@arXiv:2607.13071v1 | https://arxiv.org/html/2607.13071v1#S6 — 6 Implications for Agentic Tool Design; https://arxiv.org/html/2607.13071v1#S6.SS3 — 6.3 For Multi-Model Pipelines | https://arxiv.org/html/2607.13071v1#S3.SS1 — 3.1 Experimental Context; https://arxiv.org/html/2607.13071v1#S4 — 4 Mechanism Analysis | https://arxiv.org/html/2607.13071v1#S3 — 3 Observed Failure Mode; https://arxiv.org/html/2607.13071v1#S7 — 7 Limitations | Exact v1 links https://github.com/anthropics/claude-code/issues/76584, https://docs.anthropic.com/en/docs/claude-code, https://openai.com/index/introducing-codex/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13071 | complete |
| SF-2026-ARXIV-2607-13075 | RP-bc803e71ddf7f86f | standard | arXiv:2607.13075v1 | SRC-ARXIV@arXiv:2607.13075v1 | https://arxiv.org/html/2607.13075v1#S3.SS2 — 3.2 Benchmark methodology; https://arxiv.org/html/2607.13075v1#S4 — 4 Methods | https://arxiv.org/html/2607.13075v1#A3.SSx1 — Post-hoc criteria analysis; https://arxiv.org/html/2607.13075v1#S3 — 3 Activation Sensor Evaluation | https://arxiv.org/html/2607.13075v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13075v1#S7 — 7 Limitations | Exact v1 links https://github.com/dschwarz32/entanglement-wall, https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501, https://github.com/tatsu-lab/stanford_alpaca; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13075 | complete |
| SF-2026-ARXIV-2607-13078 | RP-309b799f8dd19d85 | standard | arXiv:2607.13078v1 | SRC-ARXIV@arXiv:2607.13078v1 | https://arxiv.org/html/2607.13078v1#S3 — 3 Scope and Survey Methodology | https://arxiv.org/html/2607.13078v1#S6 — 6 Evaluation Practices and Trustworthiness | https://arxiv.org/html/2607.13078v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13078 | complete |
| SF-2026-ARXIV-2607-13083 | RP-b010f54168ea5f2a | standard | arXiv:2607.13083v1 | SRC-ARXIV@arXiv:2607.13083v1 | https://arxiv.org/html/2607.13083v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13083v1#S2 — 2. Related Work | https://arxiv.org/html/2607.13083v1#A7 — Appendix G Per-proposer results across every arm; https://arxiv.org/html/2607.13083v1#S4 — 4. Results | https://arxiv.org/html/2607.13083v1#S5 — 5. Discussion and Limitations; https://arxiv.org/html/2607.13083v1#S4.SS2 — 4.2. RQ2: Shown a benign pattern, does it invent a failure? | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13083 | complete |
| SF-2026-ARXIV-2607-13085 | RP-3b87a764cc4c6647 | standard | arXiv:2607.13085v1 | SRC-ARXIV@arXiv:2607.13085v1 | https://arxiv.org/html/2607.13085v1#S2.SS3 — II-C LLM-Based Penetration Testing Systems; https://arxiv.org/html/2607.13085v1#S4 — IV Experimental Design | https://arxiv.org/html/2607.13085v1#S2.SS5 — II-E The XBOW Benchmark; https://arxiv.org/html/2607.13085v1#S3.SS3 — III-C Experimental Logic | https://arxiv.org/html/2607.13085v1#S7 — VII Discussion; https://arxiv.org/html/2607.13085v1#S7.SS4 — VII-D Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13085 | complete |
| SF-2026-ARXIV-2607-13091 | RP-401753e28080fac5 | standard | arXiv:2607.13091v1 | SRC-ARXIV@arXiv:2607.13091v1 | https://arxiv.org/html/2607.13091v1#S2 — II Framework Architecture; https://arxiv.org/html/2607.13091v1#S10.SSx1 — Operationalizing the Framework in an Enterprise Setting | https://arxiv.org/html/2607.13091v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.13091v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.13091v1#S8 — VIII Limitations and Threats to Validity; https://arxiv.org/html/2607.13091v1#S10 — X Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13091 | complete |
| SF-2026-ARXIV-2607-13093 | RP-6f3b323ca710c6f6 | deep | arXiv:2607.13093v1 | SRC-ARXIV@arXiv:2607.13093v1 | https://arxiv.org/html/2607.13093v1#S3 — 3 System Overview; https://arxiv.org/html/2607.13093v1#S4 — 4 Threat Model and Design Goals | https://arxiv.org/html/2607.13093v1#S7 — 7 Experimental Evaluation; https://arxiv.org/html/2607.13093v1#S7.SS10 — 7.10 Generation-Quality Evaluation | https://arxiv.org/html/2607.13093v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.13093v1#S4 — 4 Threat Model and Design Goals | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13093 | complete |
| SF-2026-ARXIV-2607-13095 | RP-e15c5f2b72a50074 | deep | arXiv:2607.13095v1 | SRC-ARXIV@arXiv:2607.13095v1 | https://arxiv.org/html/2607.13095v1#S3 — 3 KVCache System Refactor; https://arxiv.org/html/2607.13095v1#S7.SS1 — 7.1 Architecture Optimization | https://arxiv.org/html/2607.13095v1#S2.SS1 — 2.1 Compute Analysis; https://arxiv.org/html/2607.13095v1#S2.SS2 — 2.2 KVCache Storage Analysis | https://arxiv.org/html/2607.13095v1#S3.SS3 — 3.3 Discussion on Cache Hit Rate | Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/MiniMaxAI/MiniMax-M2; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13095 | complete |
| SF-2026-ARXIV-2607-13124 | RP-84c7b91bf825dd54 | deep | arXiv:2607.13124v1 | SRC-ARXIV@arXiv:2607.13124v1 | https://arxiv.org/html/2607.13124v1#S3 — 3 Method; https://arxiv.org/html/2607.13124v1#S3.SS3 — 3.3 A design space for recovery signals | https://arxiv.org/html/2607.13124v1#S10 — 10 Evaluation details; https://arxiv.org/html/2607.13124v1#S4 — 4 Experiments | https://arxiv.org/html/2607.13124v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.13124v1#S6 — 6 Limitations | Exact v1 links https://github.com/icip-cas/ShortX, https://github.com/VisionOPD/Vision-OPD, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13124 | complete |
| SF-2026-ARXIV-2607-13157 | RP-fa73f74bd11b8b12 | standard | arXiv:2607.13157v1 | SRC-ARXIV@arXiv:2607.13157v1 | https://arxiv.org/html/2607.13157v1#S3.SS4 — 3.4 Contemporary Agent-Memory Systems; https://arxiv.org/html/2607.13157v1#S4 — 4 Oracle Agent Memory Architecture | https://arxiv.org/html/2607.13157v1#S7 — 7 Evaluation and Benchmarking; https://arxiv.org/html/2607.13157v1#S3 — 3 Related Work and Benchmarks | https://arxiv.org/html/2607.13157v1#S10 — 10 Future Work; https://arxiv.org/html/2607.13157v1#S11 — 11 Conclusion | Exact v1 links https://github.com/langchain-ai/langmem, https://github.com/letta-ai/letta, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13157 | complete |
| SF-2026-ARXIV-2607-13172 | RP-0cb8b007f22c6226 | standard | arXiv:2607.13172v1 | SRC-ARXIV@arXiv:2607.13172v1 | https://arxiv.org/html/2607.13172v1#S5.SS1 — 5.1 Learning a World Model; https://arxiv.org/html/2607.13172v1#S5.SS3 — 5.3 Learning a Reward Model from User Preferences and Justifications | https://arxiv.org/html/2607.13172v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.13172v1#S7.SS1 — 7.1 Experimental Setup | https://arxiv.org/html/2607.13172v1#S8 — 8 Conclusion | Exact v1 links https://github.com/ilkaza/DROPJ, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13172 | complete |
| SF-2026-ARXIV-2607-13184 | RP-22ce6160444331ec | deep | arXiv:2607.13184v1 | SRC-ARXIV@arXiv:2607.13184v1 | https://arxiv.org/html/2607.13184v1#S2 — 2. Microflow Framework Design | https://arxiv.org/html/2607.13184v1#S2.SS4 — 2.4. Analysis Engine; https://arxiv.org/html/2607.13184v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.13184v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13184v1#S2 — 2. Microflow Framework Design | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13184 | complete |
| SF-2026-ARXIV-2607-13205 | RP-0a0018989ef1886d | deep | arXiv:2607.13205v1 | SRC-ARXIV@arXiv:2607.13205v1 | https://arxiv.org/html/2607.13205v1#S4 — 4 Counterfactual eviction and the combined method; https://arxiv.org/html/2607.13205v1#S4.SS1 — 4.1 The combined method | https://arxiv.org/html/2607.13205v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13205v1#S2 — 2 Background and related work | https://arxiv.org/html/2607.13205v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13205 | complete |
| SF-2026-ARXIV-2607-13220 | RP-f220ee0444902d5f | standard | arXiv:2607.13220v1 | SRC-ARXIV@arXiv:2607.13220v1 | https://arxiv.org/html/2607.13220v1#S2 — 2 Methods; https://arxiv.org/html/2607.13220v1#Sx2 — Supplementary Methods | https://arxiv.org/html/2607.13220v1#S3 — 3 Results | https://arxiv.org/html/2607.13220v1#S4 — 4 Discussion; https://arxiv.org/html/2607.13220v1#S4.SS4 — 4.4 Limitations and outlook | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13220 | complete |
| SF-2026-ARXIV-2607-13221 | RP-fd65db28547a13ff | standard | arXiv:2607.13221v1 | SRC-ARXIV@arXiv:2607.13221v1 | https://arxiv.org/html/2607.13221v1#S7.SS2 — VII-B Validity and cost across systems | https://arxiv.org/html/2607.13221v1#S7 — VII Experiments | https://arxiv.org/html/2607.13221v1#S8 — VIII Discussion and Limitations; https://arxiv.org/html/2607.13221v1#S9 — IX Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13221 | complete |
| SF-2026-ARXIV-2607-13285 | RP-42626433bd029670 | deep | arXiv:2607.13285v1 | SRC-ARXIV@arXiv:2607.13285v1 | https://arxiv.org/html/2607.13285v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13285v1#S2 — 2 Related Work | https://arxiv.org/html/2607.13285v1#S4.SS2 — 4.2 Experiment Results; https://arxiv.org/html/2607.13285v1#A3 — Appendix C Experimental Details | https://arxiv.org/html/2607.13285v1#S5 — 5 Conclusion | Exact v1 links https://openai.com/index/introducing-codex/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13285 | complete |
| SF-2026-ARXIV-2607-13298 | RP-c54c456b39686fd8 | standard | arXiv:2607.13298v1 | SRC-ARXIV@arXiv:2607.13298v1 | https://arxiv.org/html/2607.13298v1#A4 — Appendix D Additional Method Details; https://arxiv.org/html/2607.13298v1#A8 — Appendix H System Efficiency and Memory Footprint | https://arxiv.org/html/2607.13298v1#A5 — Appendix E Additional Dataset Results; https://arxiv.org/html/2607.13298v1#A5.SS1 — E.1 Additional Efficiency and Ablation Tables | https://arxiv.org/html/2607.13298v1#A7 — Appendix G Failure Taxonomy Discussion; https://arxiv.org/html/2607.13298v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13298 | complete |
| SF-2026-ARXIV-2607-13305 | RP-7235dbe0b7cfe55b | standard | arXiv:2607.13305v1 | SRC-ARXIV@arXiv:2607.13305v1 | https://arxiv.org/html/2607.13305v1#S3 — 3. Method; https://arxiv.org/html/2607.13305v1#S13 — S13. Cross-Model Question-Level Agreement (Table S14) | https://arxiv.org/html/2607.13305v1#S11 — S11. CRF Bidirectional Flip Analysis (Table S12); https://arxiv.org/html/2607.13305v1#S1a — S1. MVBench: Full Per-Task-Type Results (Table S1) | https://arxiv.org/html/2607.13305v1#S6 — 6. Discussion; https://arxiv.org/html/2607.13305v1#S7 — 7. Conclusion | Exact v1 links https://github.com/JaeLee18/accuracy-without-grounding, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13305 | complete |
| SF-2026-ARXIV-2607-13332 | RP-c510c8a738fbb809 | standard | arXiv:2607.13332v1 | SRC-ARXIV@arXiv:2607.13332v1 | https://arxiv.org/html/2607.13332v1#S3.SS1 — 3.1 System Overview; https://arxiv.org/html/2607.13332v1#S3.SS6 — 3.6 System Components | https://arxiv.org/html/2607.13332v1#S5 — 5 Results; https://arxiv.org/html/2607.13332v1#S6 — 6 Ablation Studies on Convergence Robustness | https://arxiv.org/html/2607.13332v1#S6.SS4 — 6.4 All-Reduce Failures | Exact v1 links https://github.com/PluralisResearch/agora, https://github.com/PluralisResearch/node0, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13332 | complete |
| SF-2026-ARXIV-2607-13359 | RP-559a9cef49db3566 | standard | arXiv:2607.13359v1 | SRC-ARXIV@arXiv:2607.13359v1 | https://arxiv.org/html/2607.13359v1#S3 — 3 Methodology; https://arxiv.org/html/2607.13359v1#S3.SS2 — 3.2 Orchestrator Architecture | https://arxiv.org/html/2607.13359v1#S4.SS2 — 4.2 Result Analysis; https://arxiv.org/html/2607.13359v1#A2 — Appendix B Experimental Setup Details | https://arxiv.org/html/2607.13359v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.13359v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13359 | complete |
| SF-2026-ARXIV-2607-13389 | RP-0da6e8909ed1aad2 | deep | arXiv:2607.13389v1 | SRC-ARXIV@arXiv:2607.13389v1 | https://arxiv.org/html/2607.13389v1#A1.SS2 — A.2 Stage A: Model-Aware IsoFLOP Design; https://arxiv.org/html/2607.13389v1#S3 — 3 Method: Conditional Compute Allocation | https://arxiv.org/html/2607.13389v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.13389v1#A1.SS1 — A.1 Overview of Experimental Stages | https://arxiv.org/html/2607.13389v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.13389v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13389 | complete |
| SF-2026-ARXIV-2607-13396 | RP-7aeab71b752dafad | standard | arXiv:2607.13396v1 | SRC-ARXIV@arXiv:2607.13396v1 | https://arxiv.org/html/2607.13396v1#A2 — Appendix B Benchmark Construction and Verifier Design; https://arxiv.org/html/2607.13396v1#S3 — 3 Study Design and Evaluation | https://arxiv.org/html/2607.13396v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.13396v1#A2 — Appendix B Benchmark Construction and Verifier Design | https://arxiv.org/html/2607.13396v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.13396v1#S6 — 6 Conclusion | Exact v1 links https://github.com/zwycl/wcst-tool-bench, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://github.com/NousResearch/hermes-agent; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13396 | complete |
| SF-2026-ARXIV-2607-13399 | RP-3efc20db63a88b4b | deep | arXiv:2607.13399v1 | SRC-ARXIV@arXiv:2607.13399v1 | https://arxiv.org/html/2607.13399v1#S2.SS2 — 2.2 Empirical Framework and Setup | https://arxiv.org/html/2607.13399v1#A1 — Appendix A Experiment Configurations; https://arxiv.org/html/2607.13399v1#S5.SS2 — 5.2 Analysis | https://arxiv.org/html/2607.13399v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.13399v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13399 | complete |
| SF-2026-ARXIV-2607-13410 | RP-c4b385e56ed915fb | deep | arXiv:2607.13410v1 | SRC-ARXIV@arXiv:2607.13410v1 | https://arxiv.org/html/2607.13410v1#S4 — IV Methodology; https://arxiv.org/html/2607.13410v1#S2.SS1 — II-A World Models for Autonomous Driving | https://arxiv.org/html/2607.13410v1#S6 — VI Experiments; https://arxiv.org/html/2607.13410v1#S6.SS1 — VI-A Experimental Setup | https://arxiv.org/html/2607.13410v1#S7 — VII Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13410 | complete |
| SF-2026-ARXIV-2607-13411 | RP-33ddd061e04222e2 | standard | arXiv:2607.13411v1 | SRC-ARXIV@arXiv:2607.13411v1 | https://arxiv.org/html/2607.13411v1#S2.SS3 — 2.3 Model Calibration and Uncertainty Quantification; https://arxiv.org/html/2607.13411v1#S4.SS1 — 4.1 Models Evaluated | https://arxiv.org/html/2607.13411v1#S2.SS6 — 2.6 Agent Evaluation Benchmarks; https://arxiv.org/html/2607.13411v1#A2 — Appendix B Complete Per-Run Results | https://arxiv.org/html/2607.13411v1#S6.SS5 — 6.5 Limitations and Future Work; https://arxiv.org/html/2607.13411v1#S2.SS4 — 2.4 Adversarial Threats in Clinical and Healthcare AI | Exact v1 links https://github.com/MichaelEnny/clinical-ai-security-eval, https://github.com/METR/task-standard, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13411 | complete |
| SF-2026-ARXIV-2607-13418 | RP-fc37917878f9fef7 | standard | arXiv:2607.13418v1 | SRC-ARXIV@arXiv:2607.13418v1 | https://arxiv.org/html/2607.13418v1#A4.SS5 — D.5 Black-Box Recommender Systems; https://arxiv.org/html/2607.13418v1#A4.SS6 — D.6 The Performance of Different Recommender Systems in Task 1 | https://arxiv.org/html/2607.13418v1#A4 — Appendix D Detailed Experimental Setup; https://arxiv.org/html/2607.13418v1#A4.SS3 — D.3 Training Experiment Details | https://arxiv.org/html/2607.13418v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.13418v1#Sx1 — Limitations | Exact v1 links https://github.com/caskcsg/CtrlBenchRec, https://github.com/camel-ai/oasis, https://huggingface.co/datasets/smartcat/Amazon_Toys_and_Games_2018; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13418 | complete |
| SF-2026-ARXIV-2607-13429 | RP-279905025ec719bb | deep | arXiv:2607.13429v1 | SRC-ARXIV@arXiv:2607.13429v1 | https://arxiv.org/html/2607.13429v1#S3 — 3 Anchor-Align Method; https://arxiv.org/html/2607.13429v1#S3.SS1 — 3.1 Base VLA Architecture | https://arxiv.org/html/2607.13429v1#A3 — Appendix C Extended Quantitative Results; https://arxiv.org/html/2607.13429v1#A3.SS3 — C.3 Multi-Seed Evaluation: Statistical Significance | https://arxiv.org/html/2607.13429v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://github.com/huggingface/lerobot, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13429 | complete |
| SF-2026-ARXIV-2607-13441 | RP-2adda9d7f96c0a35 | standard | arXiv:2607.13441v1 | SRC-ARXIV@arXiv:2607.13441v1 | https://arxiv.org/html/2607.13441v1#S4 — 4. Framework Overview | https://arxiv.org/html/2607.13441v1#S5 — 5. Preliminary Results | https://arxiv.org/html/2607.13441v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13441v1#S2 — 2. Background | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13441 | complete |
| SF-2026-ARXIV-2607-13465 | RP-83dc17139e902127 | standard | arXiv:2607.13465v1 | SRC-ARXIV@arXiv:2607.13465v1 | https://arxiv.org/html/2607.13465v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13465v1#S2 — 2 Cross-Device Collaborative Operation | https://arxiv.org/html/2607.13465v1#S3.SS1 — 3.1 Benchmark Overview; https://arxiv.org/html/2607.13465v1#S3.SS4 — 3.4 Task Execution and Evaluation | https://arxiv.org/html/2607.13465v1#S4.SS3 — 4.3 Failure Analysis; https://arxiv.org/html/2607.13465v1#S5 — 5 Discussion | Exact v1 links https://github.com/AgenticOrgLab/DevicesWorld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13465 | complete |
| SF-2026-ARXIV-2607-13474 | RP-8e61174c2c228ef6 | standard | arXiv:2607.13474v1 | SRC-ARXIV@arXiv:2607.13474v1 | https://arxiv.org/html/2607.13474v1#S2 — 2 Framework | https://arxiv.org/html/2607.13474v1#A2 — Appendix B Extra Results; https://arxiv.org/html/2607.13474v1#S2.SS3 — 2.3 Efficiency Analysis | https://arxiv.org/html/2607.13474v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.13474v1#Sx1 — Limitations | Exact v1 links https://github.com/zzsfornlp/MyAG, https://github.com/zzsfornlp/MyAG/blob/main/demo.mp4, https://github.com/langchain-ai/langgraph; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13474 | complete |
| SF-2026-ARXIV-2607-13477 | RP-dd6b30a64a5c1b62 | standard | arXiv:2607.13477v1 | SRC-ARXIV@arXiv:2607.13477v1 | https://arxiv.org/html/2607.13477v1#S3 — III Method; https://arxiv.org/html/2607.13477v1#S4.SS3 — IV-C Specialist models | https://arxiv.org/html/2607.13477v1#S4 — IV Experimental Setup; https://arxiv.org/html/2607.13477v1#S5 — V Results | https://arxiv.org/html/2607.13477v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13477 | complete |
| SF-2026-ARXIV-2607-13511 | RP-43be99311356f65a | deep | arXiv:2607.13511v1 | SRC-ARXIV@arXiv:2607.13511v1 | https://arxiv.org/html/2607.13511v1#S2 — 2 Method; https://arxiv.org/html/2607.13511v1#S2.SS6 — 2.6 Cost model | https://arxiv.org/html/2607.13511v1#S3 — 3 Results | https://arxiv.org/html/2607.13511v1#S5 — 5 Limitations; https://arxiv.org/html/2607.13511v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13511 | complete |
| SF-2026-ARXIV-2607-13527 | RP-3ebe587709007526 | standard | arXiv:2607.13527v1 | SRC-ARXIV@arXiv:2607.13527v1 | https://arxiv.org/html/2607.13527v1#S3.SS1 — 3.1 Framework Overview | https://arxiv.org/html/2607.13527v1#S4.SS1 — 4.1 Benchmark Construction; https://arxiv.org/html/2607.13527v1#S4.SS2 — 4.2 Benchmark Structure and Distribution | https://arxiv.org/html/2607.13527v1#S6 — 6 Conclusion | Exact v1 links https://github.com/PRIS-CV/VGIF-SCORE, https://github.com/genmoai/models, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13527 | complete |
| SF-2026-ARXIV-2607-13541 | RP-5064a04c92cfb587 | standard | arXiv:2607.13541v1 | SRC-ARXIV@arXiv:2607.13541v1 | https://arxiv.org/html/2607.13541v1#S4.SS2 — IV-B Method; https://arxiv.org/html/2607.13541v1#S5.SS2 — V-B Attack Methodology | https://arxiv.org/html/2607.13541v1#S4.SS4 — IV-D Evaluation Results; https://arxiv.org/html/2607.13541v1#S5.SS5 — V-E Evaluation Results | https://arxiv.org/html/2607.13541v1#S1.SS1 — I-A Limitation; https://arxiv.org/html/2607.13541v1#S4.SS1 — IV-A Threat Model | Exact v1 links https://github.com/TencentARC/FluxKits, https://huggingface.co/TencentARC/flux-mini, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13541 | complete |
| SF-2026-ARXIV-2607-13591 | RP-3604b6f7714d92f2 | deep | arXiv:2607.13591v1 | SRC-ARXIV@arXiv:2607.13591v1 | https://arxiv.org/html/2607.13591v1#A1.SS2 — A.2 Agent Frameworks; https://arxiv.org/html/2607.13591v1#A5.SS1 — E.1 Benchmark Solver System Prompts | https://arxiv.org/html/2607.13591v1#A1 — Appendix A Experimental Setup Details; https://arxiv.org/html/2607.13591v1#A1.SS1 — A.1 Benchmarks | https://arxiv.org/html/2607.13591v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ericjiang18/MemCon/, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13591 | complete |
| SF-2026-ARXIV-2607-13594 | RP-9222bfb081907f3e | standard | arXiv:2607.13594v1 | SRC-ARXIV@arXiv:2607.13594v1 | https://arxiv.org/html/2607.13594v1#S3 — 3 Method; https://arxiv.org/html/2607.13594v1#S4.SS6 — 4.6 Robustness to Framework and Backbone | https://arxiv.org/html/2607.13594v1#S4 — 4 Experiments; https://arxiv.org/html/2607.13594v1#S4.SS2 — 4.2 Main Results | https://arxiv.org/html/2607.13594v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.13594v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13594 | complete |
| SF-2026-ARXIV-2607-13596 | RP-fe02f17a386ee861 | standard | arXiv:2607.13596v1 | SRC-ARXIV@arXiv:2607.13596v1 | https://arxiv.org/html/2607.13596v1#Sx4 — Methodology; https://arxiv.org/html/2607.13596v1#Sx4.SSx1 — Experimental Design | https://arxiv.org/html/2607.13596v1#Sx4.SSx1 — Experimental Design; https://arxiv.org/html/2607.13596v1#Sx5 — Results | https://arxiv.org/html/2607.13596v1#Sx6 — Discussion; https://arxiv.org/html/2607.13596v1#Sx6.SSx7 — Scope and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13596 | complete |
| SF-2026-ARXIV-2607-13605 | RP-b8c6dc50e93b50f0 | standard | arXiv:2607.13605v1 | SRC-ARXIV@arXiv:2607.13605v1 | https://arxiv.org/html/2607.13605v1#S3 — III Method | https://arxiv.org/html/2607.13605v1#S4 — IV Experiments; https://arxiv.org/html/2607.13605v1#S4.SS1 — IV-A Experiment Setup | https://arxiv.org/html/2607.13605v1#S5 — V Discussion; https://arxiv.org/html/2607.13605v1#S5.SS3 — V-C Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13605 | complete |
| SF-2026-ARXIV-2607-13618 | RP-d0fab359be5ff1b3 | standard | arXiv:2607.13618v1 | SRC-ARXIV@arXiv:2607.13618v1 | https://arxiv.org/html/2607.13618v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13618v1#S2 — 2 Related Work | https://arxiv.org/html/2607.13618v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.13618v1#S5 — 5 Results | https://arxiv.org/html/2607.13618v1#S6 — 6 Discussion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13618 | complete |
| SF-2026-ARXIV-2607-13640 | RP-555dc054b50e8af0 | standard | arXiv:2607.13640v1 | SRC-ARXIV@arXiv:2607.13640v1 | https://arxiv.org/html/2607.13640v1#S2.SS3 — 2.3. NVIDIA GPU Architecture; https://arxiv.org/html/2607.13640v1#S5 — 5. Design | https://arxiv.org/html/2607.13640v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.13640v1#S7.SS1 — 7.1. Performance Analysis | https://arxiv.org/html/2607.13640v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.13640v1#S4 — 4. Threat Model | Exact v1 links https://cordis.europa.eu/project/id/101167904, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13640 | complete |
| SF-2026-ARXIV-2607-13649 | RP-1c98f8a85a76c70f | deep | arXiv:2607.13649v1 | SRC-ARXIV@arXiv:2607.13649v1 | https://arxiv.org/html/2607.13649v1#S2 — II CIMERA Hardware Architecture; https://arxiv.org/html/2607.13649v1#S4 — IV System Evaluation | https://arxiv.org/html/2607.13649v1#S4 — IV System Evaluation; https://arxiv.org/html/2607.13649v1#S4.SS1 — IV-A Performance Benchmarking | https://arxiv.org/html/2607.13649v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13649 | complete |
| SF-2026-ARXIV-2607-13651 | RP-9a44147f58c98438 | standard | arXiv:2607.13651v1 | SRC-ARXIV@arXiv:2607.13651v1 | https://arxiv.org/html/2607.13651v1#S5 — 5 Model; https://arxiv.org/html/2607.13651v1#S5.SS1 — 5.1 EarthNet2021 adaptation of LeWorldModel | https://arxiv.org/html/2607.13651v1#A1 — Appendix A Supplementary Results; https://arxiv.org/html/2607.13651v1#A1.SS1 — A.1 Training checkpoint used in all experiments | https://arxiv.org/html/2607.13651v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.13651v1#S9 — 9 Discussion | Exact v1 links https://github.com/AlbughdadiM/lewm-eo-cloud-monitoring, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13651 | complete |
| SF-2026-ARXIV-2607-13683 | RP-b67b68fb8f86b86a | standard | arXiv:2607.13683v1 | SRC-ARXIV@arXiv:2607.13683v1 | https://arxiv.org/html/2607.13683v1#S3 — 3 Method; https://arxiv.org/html/2607.13683v1#S4.SS5 — 4.5 Cross-model dissociation | https://arxiv.org/html/2607.13683v1#A2 — Appendix B Formal analysis; https://arxiv.org/html/2607.13683v1#S4 — 4 Experiments | https://arxiv.org/html/2607.13683v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.13683v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13683 | complete |
| SF-2026-ARXIV-2607-13705 | RP-2e76466b4a1bed54 | deep | arXiv:2607.13705v1 | SRC-ARXIV@arXiv:2607.13705v1 | https://arxiv.org/html/2607.13705v1#S3 — 3 Framework; https://arxiv.org/html/2607.13705v1#S3.SS1 — 3.1 Design Overview | https://arxiv.org/html/2607.13705v1#S4.SS3 — 4.3 Analysis Results; https://arxiv.org/html/2607.13705v1#A1 — Appendix A Detailed Experimental Configurations | https://arxiv.org/html/2607.13705v1#S5 — 5 Conclusion | Exact v1 links https://github.com/open-compass/AgentCompass, https://github.com/paul-gauthier/aider, https://github.com/confident-ai/deepeval; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13705 | complete |
| SF-2026-ARXIV-2607-13716 | RP-f5f9b27877901c03 | deep | arXiv:2607.13716v1 | SRC-ARXIV@arXiv:2607.13716v1 | https://arxiv.org/html/2607.13716v1#A1 — Appendix A System Scope and Release Posture; https://arxiv.org/html/2607.13716v1#A5 — Appendix E Safeguard Design | https://arxiv.org/html/2607.13716v1#A10 — Appendix J Comparative Evaluation; https://arxiv.org/html/2607.13716v1#A16 — Appendix P Benchmark Dataset Schema | https://arxiv.org/html/2607.13716v1#A8 — Appendix H Failure Modes and Incident Classes; https://arxiv.org/html/2607.13716v1#S10 — 10 Discussion | Exact v1 links https://github.com/open-telemetry/semantic-conventions-genai, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13716 | complete |
| SF-2026-ARXIV-2607-13718 | RP-3c7c28fc8c03ef62 | standard | arXiv:2607.13718v1 | SRC-ARXIV@arXiv:2607.13718v1 | https://arxiv.org/html/2607.13718v1#S2.SS2 — 2.2 User-Facing Permissions in Non-AI Systems; https://arxiv.org/html/2607.13718v1#S3 — 3 Methods | https://arxiv.org/html/2607.13718v1#S4 — 4 Results | https://arxiv.org/html/2607.13718v1#S5 — 5 Discussion; https://arxiv.org/html/2607.13718v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13718 | complete |
| SF-2026-ARXIV-2607-13753 | RP-13789e303c91be90 | standard | arXiv:2607.13753v1 | SRC-ARXIV@arXiv:2607.13753v1 | https://arxiv.org/html/2607.13753v1#S2 — 2 Confidence Calibration Framework; https://arxiv.org/html/2607.13753v1#S3.SS0.SSS0.Px1 — Models. | https://arxiv.org/html/2607.13753v1#A3 — Appendix C Inference and Evaluation Protocol; https://arxiv.org/html/2607.13753v1#A3.SS0.SSS0.Px2 — Repeated evaluation. | https://arxiv.org/html/2607.13753v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13753v1#S7 — 7 Conclusion | Exact v1 links https://github.com/EIT-NLP/Post-Training-Calibration, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13753 | complete |
| SF-2026-ARXIV-2607-13854 | RP-f97da46bace4d1aa | standard | arXiv:2607.13854v1 | SRC-ARXIV@arXiv:2607.13854v1 | https://arxiv.org/html/2607.13854v1#S3 — 3 Methodology | https://arxiv.org/html/2607.13854v1#S4 — 4 Experiments; https://arxiv.org/html/2607.13854v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.13854v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13854 | complete |
| SF-2026-ARXIV-2607-13884 | RP-053355c977635cc7 | standard | arXiv:2607.13884v1 | SRC-ARXIV@arXiv:2607.13884v1 | https://arxiv.org/html/2607.13884v1#S4 — 4. Method; https://arxiv.org/html/2607.13884v1#A2 — Appendix B Algorithm of extracting common subgraph and graph edit path | https://arxiv.org/html/2607.13884v1#S5 — 5. Experiments; https://arxiv.org/html/2607.13884v1#S5.SS1 — 5.1. Experimental Settings | https://arxiv.org/html/2607.13884v1#A3 — Appendix C Discussion about the robustness of graph edit path; https://arxiv.org/html/2607.13884v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13884 | complete |
| SF-2026-ARXIV-2607-13920 | RP-37d4ee7b03340da1 | standard | arXiv:2607.13920v1 | SRC-ARXIV@arXiv:2607.13920v1 | https://arxiv.org/html/2607.13920v1#A2.SS1 — B.1 Design choices; https://arxiv.org/html/2607.13920v1#S3 — 3 Methodology | https://arxiv.org/html/2607.13920v1#A1.SS1 — A.1 Human evaluation; https://arxiv.org/html/2607.13920v1#A3 — Appendix C Additional qualitative experiments | https://arxiv.org/html/2607.13920v1#S5.SS3 — 5.3 Discussion and future directions; https://arxiv.org/html/2607.13920v1#A2 — Appendix B Aggregate metrics discussion | Exact v1 links https://github.com/OpenSourcesGroup/opensources, https://huggingface.co/google/gemma-4-31B-it, https://github.com/PeterGriffinJin/Search-R1/blob/main/infer.py; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13920 | complete |
| SF-2026-ARXIV-2607-13921 | RP-6f0ab8d8bc41c1aa | deep | arXiv:2607.13921v1 | SRC-ARXIV@arXiv:2607.13921v1 | https://arxiv.org/pdf/2607.13921v1#page=7 — PDF page 7; https://arxiv.org/pdf/2607.13921v1#page=12 — PDF page 12 | https://arxiv.org/pdf/2607.13921v1#page=20 — PDF page 20; https://arxiv.org/pdf/2607.13921v1#page=25 — PDF page 25 | https://arxiv.org/pdf/2607.13921v1#page=31 — PDF page 31; https://arxiv.org/pdf/2607.13921v1#page=37 — PDF page 37 | Exact v1 links https://openrouter.ai/openai/gpt-5.3-codex, https://huggingface.co/moonshotai/Kimi-K2.7-Code, https://deploymentsafety.openai.com/gpt-5-3-codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13921 | complete |
| SF-2026-ARXIV-2607-13926 | RP-e052949c4a722ec6 | deep | arXiv:2607.13926v1 | SRC-ARXIV@arXiv:2607.13926v1 | https://arxiv.org/html/2607.13926v1#S2 — II Method; https://arxiv.org/html/2607.13926v1#S3.SS2 — III-B Implementation Details | https://arxiv.org/html/2607.13926v1#S3 — III Experiments; https://arxiv.org/html/2607.13926v1#S4 — IV Results | https://arxiv.org/html/2607.13926v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13926 | complete |
| SF-2026-ARXIV-2607-13987 | RP-ad0a15bf04565443 | standard | arXiv:2607.13987v1 | SRC-ARXIV@arXiv:2607.13987v1 | https://arxiv.org/html/2607.13987v1#S2.SS3 — 2.3 Secure Skill and Tool Ecosystems; https://arxiv.org/html/2607.13987v1#S4 — 4 SkillSec-Eval Framework | https://arxiv.org/html/2607.13987v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.13987v1#S5.SS3 — 5.3 Experimental Configuration | https://arxiv.org/html/2607.13987v1#S3 — 3 Agent Skill Lifecycle and Threat Model; https://arxiv.org/html/2607.13987v1#S3.SS3 — 3.3 Threat Model | Exact v1 links https://github.com/openai/openai-agents, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13987 | complete |
| SF-2026-ARXIV-2607-13988 | RP-55d5e36366767ea3 | deep | arXiv:2607.13988v1 | SRC-ARXIV@arXiv:2607.13988v1 | https://arxiv.org/html/2607.13988v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13988v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.13988v1#A1.SS5 — A.5 Qualitative Analysis of the Turn Credit; https://arxiv.org/html/2607.13988v1#S4 — 4 Experiments | https://arxiv.org/html/2607.13988v1#S6 — 6 Limitations; https://arxiv.org/html/2607.13988v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13988 | complete |
| SF-2026-ARXIV-2607-14004 | RP-23c415638015cd88 | standard | arXiv:2607.14004v1 | SRC-ARXIV@arXiv:2607.14004v1 | https://arxiv.org/html/2607.14004v1#A3 — Appendix C Method-Specific Diffs and Failure Cases; https://arxiv.org/html/2607.14004v1#S4 — 4 Methods Compared | https://arxiv.org/html/2607.14004v1#S2.SS3 — 2.3 Benchmark Overfitting and the Static-Benchmark Critique; https://arxiv.org/html/2607.14004v1#S2.SS4 — 2.4 Terminal-Bench as an Evaluation Substrate | https://arxiv.org/html/2607.14004v1#A3 — Appendix C Method-Specific Diffs and Failure Cases; https://arxiv.org/html/2607.14004v1#S7 — 7 Limitations and Toward Realistic Continual-Learning Benchmarks | Exact v1 links https://github.com/relai-ai/Continual-Learning-Terminal-Bench, https://www.anthropic.com/claude-code, https://github.com/context-labs/halo; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14004 | complete |
| SF-2026-ARXIV-2607-14005 | RP-a791b2ffc4272705 | deep | arXiv:2607.14005v1 | SRC-ARXIV@arXiv:2607.14005v1 | https://arxiv.org/html/2607.14005v1#S3.SS2 — 3.2 Model Architecture of M World; https://arxiv.org/html/2607.14005v1#S2.SS1 — 2.1 World Models for Driving Simulation | https://arxiv.org/html/2607.14005v1#S9 — 9 Experiments and Results; https://arxiv.org/html/2607.14005v1#S8 — 8 Controllability Evaluation Using a VLM Judge | https://arxiv.org/html/2607.14005v1#S10 — 10 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14005 | complete |
| SF-2026-ARXIV-2607-14047 | RP-cb911a00d986d72f | standard | arXiv:2607.14047v1 | SRC-ARXIV@arXiv:2607.14047v1 | https://arxiv.org/html/2607.14047v1#S3 — 3 Method | https://arxiv.org/html/2607.14047v1#A2 — Appendix B Training and Evaluation Protocols; https://arxiv.org/html/2607.14047v1#A2.SS4 — B.4 Deployment Evaluation | https://arxiv.org/html/2607.14047v1#S5 — 5 Conclusion | Exact v1 links https://github.com/openclaw/openclaw, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14047 | complete |
| SF-2026-ARXIV-2607-14076 | RP-c54c7979a0199ff5 | standard | arXiv:2607.14076v1 | SRC-ARXIV@arXiv:2607.14076v1 | https://arxiv.org/html/2607.14076v1#S2.SS1 — 2.1 Video Generation Models; https://arxiv.org/html/2607.14076v1#S2.SS2 — 2.2 Interactive Game World Models | https://arxiv.org/html/2607.14076v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14076v1#S2 — 2 Related Work | https://arxiv.org/html/2607.14076v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-14076 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-13037:start -->
### OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets

<!-- claim:SF-2026-ARXIV-2607-13037:start -->When a data contributor requests removal, model trainers face a practical gap: unlearning algorithms require a forget set, yet no tool can locate which training records belong to a given author. Existing provenance systems operate at file or dataset level, forcing catastrophic over-deletion. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13037:end -->

**为什么进入候选分母。** 摘要首要问题为“When a data contributor requests removal, model trainers face a practical gap: unlearning algorithms require a forget set, yet no tool can locate which training records belong to a given author.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present ob, a record- and token-level data provenance system that propagates author identity through data processing pipelines and resolves revocation requests into precise forget sets via deterministic queries.

**证据证明什么。** Evaluation on 219,555 Wikipedia pages demonstrates that record-level provenance eliminates dataset-level over-deletion (from 101x to 1.3x), while integration adds 1.3-4.0% throughput overhead (HuggingFace) and 2.1-19.0% (Datatrove) on wiki data.

**证据没有证明什么。** 6 Discussion OriginBlame has four limitations. (1) Incremental adoption is difficult: users cannot retroactively add provenance to existing datasets. (2) The parser ecosystem is immature: only a MediaWiki parser is currently available, though our cross-domain evaluation (§ 5.6 ) confirms that the core provenance tracking is domain-agnostic and works with arbitrary attribution sources like git blame. (3) Single-hop provenance: the system tracks only direct mappings from raw data to final output. (4) The index must be rebuilt when data changes; indexed variants do not consistently outperform the full-scan path due to rayon parallelism amortizing the scan cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13037v1#S4 — 4 System Design; https://arxiv.org/html/2607.13037v1#S4.SS1 — 4.1 Architecture Overview。Evaluation：https://arxiv.org/html/2607.13037v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.13037v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13037v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13037v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/tzbkk/originblame, https://github.com/tzbkk/rust-originblame, https://github.com/huggingface/datatrove; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6 Discussion OriginBlame has four limitations. (1) Incremental adoption is difficult: users cannot retroactively add provenance to existing datasets. (2) The parser ecosystem is immature: only a MediaWiki parser is currently available, though our cross-domain evaluation (§ 5.6 ) confirms that the core provenance tracking is domain-agnostic and works with arbitrary attribution sources like git blame. (3) Single-hop provenance: the system tracks only direct mappings from raw data to final output. (4) The index must be rebuilt when data changes; indexed variants do not consistently outperform the full-scan path due to rayon parallelism amortizing the scan cost.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13037:end -->

<!-- review:SF-2026-ARXIV-2607-13048:start -->
### Uncertainty-Aware Sequential Decision Rules for Event-Triggered LLM Invocation in Streaming Systems

<!-- claim:SF-2026-ARXIV-2607-13048:start -->Streaming inference pipelines increasingly pair lightweight fast models with Large Language Models (LLMs) that provide rich semantic understanding at substantial cost. The central question of when to invoke the LLM has received limited formal treatment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13048:end -->

**为什么进入候选分母。** 摘要首要问题为“Streaming inference pipelines increasingly pair lightweight fast models with Large Language Models (LLMs) that provide rich semantic understanding at substantial cost.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Several classical trigger families, including event-triggered, optimal stopping, SPRT, CUSUM, and Bayesian triggers, can be expressed as special cases of this framework.

**证据证明什么。** The results confirm sublinear regret, with alpha &lt; 1 for all principled triggers; high diagnostic quality, with 92.9 percent of 1600 LLM diagnoses reaching grounding score &gt;= 0.75 under our rubric; and that anomaly-score-driven risk functions dominate alternatives by roughly an order of magnitude on the Pareto AUC.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13048v1#S4 — 4 System Architecture; https://arxiv.org/html/2607.13048v1#S3 — 3 Theoretical Framework。Evaluation：https://arxiv.org/html/2607.13048v1#Pt0.A2 — Appendix 0.B Experimental Details; https://arxiv.org/html/2607.13048v1#S3.SS8 — 3.8 Roadmap from theory to evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13048v1#Pt0.A5 — Appendix 0.E Limitations; https://arxiv.org/html/2607.13048v1#S7.SS2 — 7.2 LLM Failure Analysis。

**Artifact boundary。** Exact v1 links https://github.com/GeoffreyWang1117/event-triggered-llm-streaming, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13048:end -->

<!-- review:SF-2026-ARXIV-2607-13062:start -->
### The verifier side of speculative window decoding: a predictability bracket, a machine-checked blast-radius bound, and a decoder-agnostic recover loop

<!-- claim:SF-2026-ARXIV-2607-13062:start -->Speculative window decoders hide quantum error-correction decoder latency by guessing the cross-boundary decisions that link adjacent decoding windows, running downstream work on the guess, and verifying lazily. SWIPER and ARTERY each build one predictor, about 90% accurate; neither built the verifier side. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13062:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative window decoders hide quantum error-correction decoder latency by guessing the cross-boundary decisions that link adjacent decoding windows, running downstream work on the guess, and verifying lazily.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** SWIPER and ARTERY each build one predictor, about 90% accurate; neither built the verifier side.

**证据证明什么。** A predictor-only bracket shows the cross-boundary decision is local, the achievable accuracy reaching about 0.999 within three rounds, with small, diffuse headroom over SWIPER.

**证据没有证明什么。** 8 Limitations and future work The matching-weight bound. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13062v1#S2 — 2 Setup and the calibration gate; https://arxiv.org/html/2607.13062v1#S5 — 5 Decide: the speculation-decision pass; https://arxiv.org/html/2607.13062v1#S6 — 6 Execute: the runtime executor。Evaluation：https://arxiv.org/html/2607.13062v1#S3 — 3 Measure: the predictability and speedup bracket; https://arxiv.org/html/2607.13062v1#S4 — 4 Bound, refute, and explain: the misprediction blast radius。Limitations / counterevidence：https://arxiv.org/html/2607.13062v1#S8 — 8 Limitations and future work; https://arxiv.org/html/2607.13062v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://codeberg.org/rylanmalarchick/speculative-qec, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：8 Limitations and future work The matching-weight bound.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13062:end -->

<!-- review:SF-2026-ARXIV-2607-13068:start -->
### The Economics of AI Decoding Chips: Rebalancing Compute, Capacity, and Bandwidth for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-13068:start -->Every mainstream GPU is built compute-heavy and capacity-light: it pairs enormous arithmetic throughput with too little memory to hold a modern model. In contrast, large language model decoding requires little compute and a large amount of memory: a GPU's floating-point units run at single-digit-percent utilization during decoding, and the memory the workload does need is sold only bundled with yet more compute. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13068:end -->

**为什么进入候选分母。** 摘要首要问题为“Every mainstream GPU is built compute-heavy and capacity-light: it pairs enormous arithmetic throughput with too little memory to hold a modern model.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In contrast, large language model decoding requires little compute and a large amount of memory: a GPU's floating-point units run at single-digit-percent utilization during decoding, and the memory the workload does need is sold only bundled with yet more compute.

**证据证明什么。** The HTX-301's decisive advantage is a supply chain free of every rationed input: it uses no high-bandwidth memory, no CoWoS, and no leading-edge logic.

**证据没有证明什么。** Consumer memory-rich devices approach this corner but do not reach it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13068v1#S5 — 5 A rebalanced design: less F, more S, deliberately less B。Evaluation：https://arxiv.org/html/2607.13068v1#S1 — 1 Introduction: the decode inefficiency; https://arxiv.org/html/2607.13068v1#S2 — 2 Two hardware constants: F/B and F/S。Limitations / counterevidence：https://arxiv.org/html/2607.13068v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deepseek-ai/DeepGEMM, https://github.com/dzhsurf/deepseek-v3-r1-deploy-and-benchmarks, https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Consumer memory-rich devices approach this corner but do not reach it.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13068:end -->

<!-- review:SF-2026-ARXIV-2607-13071:start -->
### Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes

<!-- claim:SF-2026-ARXIV-2607-13071:start -->Agentic LLM coding tools compress long session histories into compaction summaries that subsequent sessions inherit as ground truth. This paper documents a failure mode in Claude Code where partial standard output from timed-out commands (exit code 143) is recorded in compaction summaries as confirmed results, propagating false positives across sessions and model versions without re-verification. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13071:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic LLM coding tools compress long session histories into compaction summaries that subsequent sessions inherit as ground truth.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This paper documents a failure mode in Claude Code where partial standard output from timed-out commands (exit code 143) is recorded in compaction summaries as confirmed results, propagating false positives across sessions and model versions without re-verification.

**证据证明什么。** This finding extends the analysis of LLM self-evaluation failures reported in prior work on non-determinism in LLM-as-judge grading by showing that agentic tools exhibit analogous reliability deficits when reporting on their own operational outcomes.

**证据没有证明什么。** This participant-observation-like method provides ecological validity that controlled experiments cannot replicate, but it also means the finding is shaped by the specific workflow patterns of a single heavy user. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13071v1#S6 — 6 Implications for Agentic Tool Design; https://arxiv.org/html/2607.13071v1#S6.SS3 — 6.3 For Multi-Model Pipelines。Evaluation：https://arxiv.org/html/2607.13071v1#S3.SS1 — 3.1 Experimental Context; https://arxiv.org/html/2607.13071v1#S4 — 4 Mechanism Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.13071v1#S3 — 3 Observed Failure Mode; https://arxiv.org/html/2607.13071v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/anthropics/claude-code/issues/76584, https://docs.anthropic.com/en/docs/claude-code, https://openai.com/index/introducing-codex/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：This participant-observation-like method provides ecological validity that controlled experiments cannot replicate, but it also means the finding is shaped by the specific workflow patterns of a single heavy user.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13071:end -->

<!-- review:SF-2026-ARXIV-2607-13075:start -->
### The Entanglement Wall: Activation-Space Probes as Risk Detectors, Not Context Adjudicators

<!-- claim:SF-2026-ARXIV-2607-13075:start -->Context can change whether a request is harmful without changing its topic or surface form. We ask whether residual-stream probes distinguish harmful requests from surface-matched benign controls at a useful operating point. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13075:end -->

**为什么进入候选分母。** 摘要首要问题为“Context can change whether a request is harmful without changing its topic or surface form.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We ask whether residual-stream probes distinguish harmful requests from surface-matched benign controls at a useful operating point.

**证据证明什么。** At the tested read points, these activation scores behave as broad-risk detectors rather than standalone context adjudicators.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13075v1#S3.SS2 — 3.2 Benchmark methodology; https://arxiv.org/html/2607.13075v1#S4 — 4 Methods。Evaluation：https://arxiv.org/html/2607.13075v1#A3.SSx1 — Post-hoc criteria analysis; https://arxiv.org/html/2607.13075v1#S3 — 3 Activation Sensor Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13075v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13075v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/dschwarz32/entanglement-wall, https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501, https://github.com/tatsu-lab/stanford_alpaca; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13075:end -->

<!-- review:SF-2026-ARXIV-2607-13078:start -->
### Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows

<!-- claim:SF-2026-ARXIV-2607-13078:start -->LLMs are now proposed for fraud detection, scam investigation, content moderation, and other trust-and-safety workflows. Much of the public literature still evaluates them as models, with less attention to their behavior as components in operational pipelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13078:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs are now proposed for fraud detection, scam investigation, content moderation, and other trust-and-safety workflows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** These sources include systems, benchmarks, frameworks, and deployment-relevant surveys, not 49 production deployments.

**证据证明什么。** The resulting agenda identifies studies needed to support deployment claims for LLM-based fraud and trust-and-safety work.

**证据没有证明什么。** The role-and-evidence frame organizes the field by deployment role, not by model family. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13078v1#S3 — 3 Scope and Survey Methodology。Evaluation：https://arxiv.org/html/2607.13078v1#S6 — 6 Evaluation Practices and Trustworthiness。Limitations / counterevidence：https://arxiv.org/html/2607.13078v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The role-and-evidence frame organizes the field by deployment role, not by model family.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13078:end -->

<!-- review:SF-2026-ARXIV-2607-13083:start -->
### Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened

<!-- claim:SF-2026-ARXIV-2607-13083:start -->Self-improving AI agents are designed to learn from their mistakes. We show they can also hallucinate mistakes that never happened. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13083:end -->

**为什么进入候选分母。** 摘要首要问题为“Self-improving AI agents are designed to learn from their mistakes.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present the Counterfactual Fabrication Lab for measuring fabricated failures in self-improving agent harnesses.

**证据证明什么。** We show they can also hallucinate mistakes that never happened.

**证据没有证明什么。** Discussion and Limitations For suppression-rewarded search, the failure mode that matters is not only under-fixing the unobserved but fabricating it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13083v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13083v1#S2 — 2. Related Work。Evaluation：https://arxiv.org/html/2607.13083v1#A7 — Appendix G Per-proposer results across every arm; https://arxiv.org/html/2607.13083v1#S4 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.13083v1#S5 — 5. Discussion and Limitations; https://arxiv.org/html/2607.13083v1#S4.SS2 — 4.2. RQ2: Shown a benign pattern, does it invent a failure?。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Discussion and Limitations For suppression-rewarded search, the failure mode that matters is not only under-fixing the unobserved but fabricating it.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13083:end -->

<!-- review:SF-2026-ARXIV-2607-13085:start -->
### Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing

<!-- claim:SF-2026-ARXIV-2607-13085:start -->Recent autonomous penetration testing papers report high benchmark scores while adding multi-component security harnesses around frontier LLMs. Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13085:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent autonomous penetration testing papers report high benchmark scores while adding multi-component security harnesses around frontier LLMs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Because these systems often change both architecture and backbone model, it is difficult to tell how much performance comes from the harness rather than from the underlying model.

**证据证明什么。** The results show a mixed but practical picture.

**证据没有证明什么。** The jail blocks host and Docker access, but released aggregate data alone cannot independently audit every network destination the runtime attempted. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13085v1#S2.SS3 — II-C LLM-Based Penetration Testing Systems; https://arxiv.org/html/2607.13085v1#S4 — IV Experimental Design。Evaluation：https://arxiv.org/html/2607.13085v1#S2.SS5 — II-E The XBOW Benchmark; https://arxiv.org/html/2607.13085v1#S3.SS3 — III-C Experimental Logic。Limitations / counterevidence：https://arxiv.org/html/2607.13085v1#S7 — VII Discussion; https://arxiv.org/html/2607.13085v1#S7.SS4 — VII-D Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The jail blocks host and Docker access, but released aggregate data alone cannot independently audit every network destination the runtime attempted.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13085:end -->

<!-- review:SF-2026-ARXIV-2607-13091:start -->
### Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework

<!-- claim:SF-2026-ARXIV-2607-13091:start -->LLM-based coding agents repeat the same classes of mistakes across sessions because they lack a mechanism to retain corrections from human review feedback. We present a closed-loop framework in which every accepted review comment is codified as a persistent behavioral rule, progressively expanding the set of error classes the agent can self-detect. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13091:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based coding agents repeat the same classes of mistakes across sessions because they lack a mechanism to retain corrections from human review feedback.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present a closed-loop framework in which every accepted review comment is codified as a persistent behavioral rule, progressively expanding the set of error classes the agent can self-detect.

**证据证明什么。** We compare our approach against related work in experiential LLM learning (Reflexion, ExpeL, Voyager) and automated code review (CodeReviewer, SWE-bench agents), showing that our framework achieves persistent cross-session learning without weight updates, operates on production codebases rather than synthetic benchmarks, and addresses an orthogonal dimension (behavioral consistency over time) that existing benchmarks do not measure.

**证据没有证明什么。** VIII Limitations and Threats to Validity Context window constraints: Current rule sets ( 6,250 tokens) are within modern limits, but unbounded growth could require hierarchical organization or summarization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13091v1#S2 — II Framework Architecture; https://arxiv.org/html/2607.13091v1#S10.SSx1 — Operationalizing the Framework in an Enterprise Setting。Evaluation：https://arxiv.org/html/2607.13091v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.13091v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13091v1#S8 — VIII Limitations and Threats to Validity; https://arxiv.org/html/2607.13091v1#S10 — X Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：VIII Limitations and Threats to Validity Context window constraints: Current rule sets ( 6,250 tokens) are within modern limits, but unbounded growth could require hierarchical organization or summarization.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13091:end -->

<!-- review:SF-2026-ARXIV-2607-13093:start -->
### Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-13093:start -->On-device LLM inference faces a trilemma of response latency, limited hardware resources and user privacy. Full cloud inference delivers strong computing power but exposes user prompts and dialogue data, while standalone on-device inference is unfeasible for most consumer and embedded edge devices. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13093:end -->

**为什么进入候选分母。** 摘要首要问题为“On-device LLM inference faces a trilemma of response latency, limited hardware resources and user privacy.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This paper presents a privacy-centric edge-cloud collaborative LLM inference framework built on endpoint-authenticated KV cache.

**证据证明什么。** Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.

**证据没有证明什么。** Network attackers may observe, replay, or modify packets, but they do not know the authenticated-encryption keys. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13093v1#S3 — 3 System Overview; https://arxiv.org/html/2607.13093v1#S4 — 4 Threat Model and Design Goals。Evaluation：https://arxiv.org/html/2607.13093v1#S7 — 7 Experimental Evaluation; https://arxiv.org/html/2607.13093v1#S7.SS10 — 7.10 Generation-Quality Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13093v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.13093v1#S4 — 4 Threat Model and Design Goals。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Network attackers may observe, replay, or modify packets, but they do not know the authenticated-encryption keys.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13093:end -->

<!-- review:SF-2026-ARXIV-2607-13095:start -->
### Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit

<!-- claim:SF-2026-ARXIV-2607-13095:start -->We present a full-pipeline inference optimization for the MiMo-V2.5 model family, which combines Hybrid Sliding Window Attention (Hybrid SWA), sparse Mixture-of-Experts (MoE), and multimodal encoders. While Hybrid SWA can ideally reduce both attention compute and KVCache storage significantly compared to Full Attention, realizing these gains in production requires substantial engineering effort. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13095:end -->

**为什么进入候选分母。** 摘要首要问题为“We present a full-pipeline inference optimization for the MiMo-V2.5 model family, which combines Hybrid Sliding Window Attention (Hybrid SWA), sparse Mixture-of-Experts (MoE), and multimodal encoders.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Together, these optimizations constitute the first large-scale LLM serving system in production that efficiently covers the Hybrid SWA + MoE + multimodal composite architecture.

**证据证明什么。** While Hybrid SWA can ideally reduce both attention compute and KVCache storage significantly compared to Full Attention, realizing these gains in production requires substantial engineering effort.

**证据没有证明什么。** Additionally, SWA’s reduced bandwidth transfer overhead, while not directly affecting TTL, significantly lowers cross-tier data movement costs, ensuring stable and efficient operation of the entire caching system. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13095v1#S3 — 3 KVCache System Refactor; https://arxiv.org/html/2607.13095v1#S7.SS1 — 7.1 Architecture Optimization。Evaluation：https://arxiv.org/html/2607.13095v1#S2.SS1 — 2.1 Compute Analysis; https://arxiv.org/html/2607.13095v1#S2.SS2 — 2.2 KVCache Storage Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.13095v1#S3.SS3 — 3.3 Discussion on Cache Hit Rate。

**Artifact boundary。** Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://huggingface.co/MiniMaxAI/MiniMax-M2; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Additionally, SWA’s reduced bandwidth transfer overhead, while not directly affecting TTL, significantly lowers cross-tier data movement costs, ensuring stable and efficient operation of the entire caching system.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13095:end -->

<!-- review:SF-2026-ARXIV-2607-13124:start -->
### ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-13124:start -->Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires. First, greedy \textsc{pass}@$1$ nearly vanishes after compression, yet \textsc{pass}@$k$ recovers substantially under repeated sampling: useful generations are demoted, not erased. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13124:end -->

**为什么进入候选分母。** 摘要首要问题为“Structured pruning is a hardware-friendly way to compress LLMs, but it is mostly validated on multiple-choice recognition tasks, while the same compressed checkpoints can collapse on the free-form generation that deployment actually requires.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To mitigate this waste, we propose \textbf{\shortopd}, a short-to-long OPD schedule that detects teacher-confirmed repetitive suffixes, treats the surviving prefix as each rollout's effective length, and allocates future rollout budgets to the effective lengths the policy can currently use.

**证据证明什么。** We hope this recipe helps move structured pruning beyond marginal gains on perplexity and multiple-choice benchmarks, a step closer to deployment-ready generation quality.

**证据没有证明什么。** Finally, we do not yet establish the boundary where a model has been compressed too aggressively for light post-compression recovery. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13124v1#S3 — 3 Method; https://arxiv.org/html/2607.13124v1#S3.SS3 — 3.3 A design space for recovery signals。Evaluation：https://arxiv.org/html/2607.13124v1#S10 — 10 Evaluation details; https://arxiv.org/html/2607.13124v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13124v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.13124v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/icip-cas/ShortX, https://github.com/VisionOPD/Vision-OPD, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Finally, we do not yet establish the boundary where a model has been compressed too aggressively for light post-compression recovery.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13124:end -->

<!-- review:SF-2026-ARXIV-2607-13157:start -->
### Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents

<!-- claim:SF-2026-ARXIV-2607-13157:start -->Agent memory is a systems problem for long-horizon agents. Practical deployments require retention of task state across extended conversations, recovery of user-specific facts and preferences across sessions, and accumulation of procedural knowledge from prior outcomes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13157:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent memory is a systems problem for long-horizon agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Agent memory is a systems problem for long-horizon agents.

**证据证明什么。** The report summarizes LongMemEval results, reaching 93.8% accuracy, compares Oracle Agent Memory against flat-history baselines, using about 10.7x fewer tokens, and published or reported external baselines where available, and closes with implementation-oriented appendix material covering setup, thread lifecycle, and search semantics.

**证据没有证明什么。** Durable memory should not accumulate as an append-only log of extracted facts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13157v1#S3.SS4 — 3.4 Contemporary Agent-Memory Systems; https://arxiv.org/html/2607.13157v1#S4 — 4 Oracle Agent Memory Architecture。Evaluation：https://arxiv.org/html/2607.13157v1#S7 — 7 Evaluation and Benchmarking; https://arxiv.org/html/2607.13157v1#S3 — 3 Related Work and Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.13157v1#S10 — 10 Future Work; https://arxiv.org/html/2607.13157v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langmem, https://github.com/letta-ai/letta, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Durable memory should not accumulate as an append-only log of extracted facts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13157:end -->

<!-- review:SF-2026-ARXIV-2607-13172:start -->
### Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models

<!-- claim:SF-2026-ARXIV-2607-13172:start -->We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available. In the context of safety-critical environments, we consider traditional reinforcement learning impractical and resort to the resource of human input. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13172:end -->

**为什么进入候选分母。** 摘要首要问题为“We address the problem of safely training an agent policy and deploying a good and safe policy, in settings where the environment dynamics are unknown and no suitable reward function is available.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce DROPJ, a human-centred method for both safe training and deployment.

**证据证明什么。** Running real-user experiments, we find that generating informative simulated trajectories from a user significantly reduces the computational cost during training compared to other strategies, and can also improve the performance during deployment.

**证据没有证明什么。** The only concern of DROPJ is its reliance on past real-world examples in order to build a robust world model, and (as generally in human-centred methods) on qualified/capable users to create more examples via the learned simulator or provide accurate feedback. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13172v1#S5.SS1 — 5.1 Learning a World Model; https://arxiv.org/html/2607.13172v1#S5.SS3 — 5.3 Learning a Reward Model from User Preferences and Justifications。Evaluation：https://arxiv.org/html/2607.13172v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.13172v1#S7.SS1 — 7.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13172v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ilkaza/DROPJ, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The only concern of DROPJ is its reliance on past real-world examples in order to build a robust world model, and (as generally in human-centred methods) on qualified/capable users to create more examples via the learned simulator or provide accurate feedback.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13172:end -->

<!-- review:SF-2026-ARXIV-2607-13184:start -->
### Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization

<!-- claim:SF-2026-ARXIV-2607-13184:start -->Existing architectural simulators expose aggregate metrics or raw traces, but fail to reveal complex interactions among microarchitectural events and their relationship to program execution. Consequently, architects observe performance symptoms but cannot systematically attribute them to root causes across abstraction layers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13184:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing architectural simulators expose aggregate metrics or raw traces, but fail to reveal complex interactions among microarchitectural events and their relationship to program execution.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This paper introduces Microflow, an observability framework elevating causality to a first-class analytical object.

**证据证明什么。** We demonstrate it on two SPEC CPU 2017 benchmarks, uncovering bottlenecks invisible from aggregate symptoms: hidden misprediction costs in leela and cross-loop-iteration contention in mcf.

**证据没有证明什么。** What the aggregate statistics cannot reveal is that the stall is not a capacity problem at all. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13184v1#S2 — 2. Microflow Framework Design。Evaluation：https://arxiv.org/html/2607.13184v1#S2.SS4 — 2.4. Analysis Engine; https://arxiv.org/html/2607.13184v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13184v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13184v1#S2 — 2. Microflow Framework Design。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：What the aggregate statistics cannot reveal is that the stall is not a capacity problem at all.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13184:end -->

<!-- review:SF-2026-ARXIV-2607-13205:start -->
### Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference

<!-- claim:SF-2026-ARXIV-2607-13205:start -->Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest. On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13205:end -->

**为什么进入候选分母。** 摘要首要问题为“Attention-based KV cache eviction (H2O and its descendants) compresses the memory-constrained state of a long-context model by ranking tokens on accumulated attention mass, treated here as signal energy, and keeping the heaviest.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades.

**证据证明什么。** A 15 MB linear role probe supplies these labels at negligible inference cost, though matching parser-level downstream accuracy remains open.

**证据没有证明什么。** Limitations: a role-density floor on sparse-role corpora (e.g. wikitable); the seed-sensitive over-baseline margin; a masking-based harness that isolates accuracy but does not realize the memory/latency benefit; a Quest comparison that omits per-step re-selection (a lower bound); and fp16-only runs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13205v1#S4 — 4 Counterfactual eviction and the combined method; https://arxiv.org/html/2607.13205v1#S4.SS1 — 4.1 The combined method。Evaluation：https://arxiv.org/html/2607.13205v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13205v1#S2 — 2 Background and related work。Limitations / counterevidence：https://arxiv.org/html/2607.13205v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations: a role-density floor on sparse-role corpora (e.g. wikitable); the seed-sensitive over-baseline margin; a masking-based harness that isolates accuracy but does not realize the memory/latency benefit; a Quest comparison that omits per-step re-selection (a lower bound); and fp16-only runs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13205:end -->

<!-- review:SF-2026-ARXIV-2607-13220:start -->
### Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science

<!-- claim:SF-2026-ARXIV-2607-13220:start -->Most AI-for-science systems focus on scaling a single reasoning process by using better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user. However, challenging scientific problems are rarely solved by one reasoner alone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13220:end -->

**为什么进入候选分母。** 摘要首要问题为“Most AI-for-science systems focus on scaling a single reasoning process by using better models, larger context windows, long-horizon agentic execution, or digital co-scientists working with one principal user.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce Mycelium, an active shared workspace that automatically connects researchers and AI agents.

**证据证明什么。** This framework establishes when a scaled standalone agent is sufficient, and when isolated data and specialized expertise make a networked approach essential.

**证据没有证明什么。** While Mycelium tracks the exact origin of a claim, future systems must also measure the uncertainty and loss of specific meaning that occurs when a finding is adapted from one domain to another. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13220v1#S2 — 2 Methods; https://arxiv.org/html/2607.13220v1#Sx2 — Supplementary Methods。Evaluation：https://arxiv.org/html/2607.13220v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.13220v1#S4 — 4 Discussion; https://arxiv.org/html/2607.13220v1#S4.SS4 — 4.4 Limitations and outlook。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：While Mycelium tracks the exact origin of a claim, future systems must also measure the uncertainty and loss of specific meaning that occurs when a finding is adapted from one domain to another.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13220:end -->

<!-- review:SF-2026-ARXIV-2607-13221:start -->
### Audited Selective Verification for Risk-Controlled N-1 Thermal Contingency Screening under Deployment Shift

<!-- claim:SF-2026-ARXIV-2607-13221:start -->Real-time N-1 contingency screening in an energy management system trades assurance against cost: verifying every credible outage with full power flow is too slow, while fast linear-sensitivity screening gives no statistical guarantee and can silently pass unsafe operating points, especially when a controller drives the system into unfamiliar regimes. This paper introduces Audited Selective Verification, a risk-budgeted screening and triage layer for any controller's output (optimization, model-predictive, or learned). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13221:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-time N-1 contingency screening in an energy management system trades assurance against cost: verifying every credible outage with full power flow is too slow, while fast linear-sensitivity screening gives no statistical guarantee and can silently pass unsafe operating points, especially when a controller drives the system into unfamiliar regimes.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** On three public transmission systems up to 1354 buses, the realized violation rate stays within budget, standard deterministic and calibrated screens become unsafe under shift, and the method cuts full power-flow studies by 29 to 75 percent per real-time operating point.

**证据证明什么。** On three public transmission systems up to 1354 buses, the realized violation rate stays within budget, standard deterministic and calibrated screens become unsafe under shift, and the method cuts full power-flow studies by 29 to 75 percent per real-time operating point.

**证据没有证明什么。** Future work includes a joint thermal-and-voltage audit, a learned surrogate to lower cost on stressed systems, and end-to-end evaluation with trained learning-based controllers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13221v1#S7.SS2 — VII-B Validity and cost across systems。Evaluation：https://arxiv.org/html/2607.13221v1#S7 — VII Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13221v1#S8 — VIII Discussion and Limitations; https://arxiv.org/html/2607.13221v1#S9 — IX Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work includes a joint thermal-and-voltage audit, a learned surrogate to lower cost on stressed systems, and end-to-end evaluation with trained learning-based controllers.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13221:end -->

<!-- review:SF-2026-ARXIV-2607-13285:start -->
### Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable

<!-- claim:SF-2026-ARXIV-2607-13285:start -->The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution. As models, APIs, environments, and requirements evolve, the harness must be continually modified. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13285:end -->

**为什么进入候选分母。** 摘要首要问题为“The capability of a modern AI agent depends not only on its foundation model but also on its harness, which constructs prompts, manages state, invokes tools, and coordinates execution.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made.

**证据证明什么。** On diverse modification requests from two open-source harnesses, Handbook-Assisted planning improves behavior localization and edit-plan quality while using fewer planner tokens, with the largest gains on scattered sites, rarely executed paths, and cross-module interactions.

**证据没有证明什么。** Second, with the handbook a weaker planner matches the implementation-site localization of substantially stronger models, improving all 24 file- and symbol-level Recall, Precision, and F1 comparisons against two independent reference plans. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13285v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13285v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.13285v1#S4.SS2 — 4.2 Experiment Results; https://arxiv.org/html/2607.13285v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.13285v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://openai.com/index/introducing-codex/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Second, with the handbook a weaker planner matches the implementation-site localization of substantially stronger models, improving all 24 file- and symbol-level Recall, Precision, and F1 comparisons against two independent reference plans.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13285:end -->

<!-- review:SF-2026-ARXIV-2607-13298:start -->
### FOLIO: Focused Semantic Memory for Streaming Video Understanding

<!-- claim:SF-2026-ARXIV-2607-13298:start -->In online streaming video understanding, a video stream continues to arrive and queries may be issued at any time. Because streaming frames grow without bound, the system must continuously compress and retain information from the observed video prefix while future frames and future queries remain unknown. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13298:end -->

**为什么进入候选分母。** 摘要首要问题为“In online streaming video understanding, a video stream continues to arrive and queries may be issued at any time.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this challenge, we introduce FOLIO, a training-free focused semantic memory system that records important parts of the stream in higher detail while keeping surrounding context compact.

**证据证明什么。** FOLIO achieves state-of-the-art performance, reaching 82.0/69.1 Perception/Backward accuracy on OVO-Bench with Qwen3-VL-8B and 74.5 overall accuracy on StreamingBench, while substantially reducing the cost of maintaining streaming memory by reserving detailed records for focused entities and storing surrounding context compactly.

**证据没有证明什么。** The implication is that future gains are more likely to come from improving memory fidelity and evidence-sufficiency judgment than from only increasing retrieval breadth. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13298v1#A4 — Appendix D Additional Method Details; https://arxiv.org/html/2607.13298v1#A8 — Appendix H System Efficiency and Memory Footprint。Evaluation：https://arxiv.org/html/2607.13298v1#A5 — Appendix E Additional Dataset Results; https://arxiv.org/html/2607.13298v1#A5.SS1 — E.1 Additional Efficiency and Ablation Tables。Limitations / counterevidence：https://arxiv.org/html/2607.13298v1#A7 — Appendix G Failure Taxonomy Discussion; https://arxiv.org/html/2607.13298v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The implication is that future gains are more likely to come from improving memory fidelity and evidence-sufficiency judgment than from only increasing retrieval breadth.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13298:end -->

<!-- review:SF-2026-ARXIV-2607-13305:start -->
### Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks

<!-- claim:SF-2026-ARXIV-2607-13305:start -->Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding. We audit this assumption across twenty models spanning 2-78B parameters and ten architecture families. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13305:end -->

**为什么进入候选分母。** 摘要首要问题为“Benchmark accuracy in video large language models (LLMs) is often treated as evidence of visual understanding.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce the Visual Dependency Gap (VDG), the difference in per-question correctness between original-video and black-screen conditions.

**证据证明什么。** H.264 experiments further show that stable aggregate accuracy conceals bidirectional question-level answer flips.

**证据没有证明什么。** Discussion The VDG spectrum implies that most benchmark difficulty is linguistic, not visual: only 31% of Video-MME questions fall in Category I (pure visual), while 70% are answerable regardless of visual input. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13305v1#S3 — 3. Method; https://arxiv.org/html/2607.13305v1#S13 — S13. Cross-Model Question-Level Agreement (Table S14)。Evaluation：https://arxiv.org/html/2607.13305v1#S11 — S11. CRF Bidirectional Flip Analysis (Table S12); https://arxiv.org/html/2607.13305v1#S1a — S1. MVBench: Full Per-Task-Type Results (Table S1)。Limitations / counterevidence：https://arxiv.org/html/2607.13305v1#S6 — 6. Discussion; https://arxiv.org/html/2607.13305v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/JaeLee18/accuracy-without-grounding, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Discussion The VDG spectrum implies that most benchmark difficulty is linguistic, not visual: only 31% of Video-MME questions fall in Category I (pure visual), while 70% are answerable regardless of visual input.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13305:end -->

<!-- review:SF-2026-ARXIV-2607-13332:start -->
### Agora: Collective and Permissionless Internet-Scale Pretraining of Large Language Models

<!-- claim:SF-2026-ARXIV-2607-13332:start -->Training large language models at the multi-billion to trillion parameter scale is confined to datacenters, where data-parallel (DP) and model-parallel (MP) techniques presume homogeneous accelerators, high-speed interconnects, and a single orchestrating entity. Frontier model development is thereby concentrated among the few groups able to assemble such clusters. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13332:end -->

**为什么进入候选分母。** 摘要首要问题为“Training large language models at the multi-billion to trillion parameter scale is confined to datacenters, where data-parallel (DP) and model-parallel (MP) techniques presume homogeneous accelerators, high-speed interconnects, and a single orchestrating entity.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present Agora, a system that makes efficient use of this compute.

**证据证明什么。** The run sustained ~170k tokens/s and 4.2 tokens per TFLOP of pooled compute, 63% of the efficiency of a centralized H100 baseline, and converged to within a small margin of a centralized reference run.

**证据没有证明什么。** The loss continues to decrease, but its trajectory becomes noticeably shallower around 3.1. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13332v1#S3.SS1 — 3.1 System Overview; https://arxiv.org/html/2607.13332v1#S3.SS6 — 3.6 System Components。Evaluation：https://arxiv.org/html/2607.13332v1#S5 — 5 Results; https://arxiv.org/html/2607.13332v1#S6 — 6 Ablation Studies on Convergence Robustness。Limitations / counterevidence：https://arxiv.org/html/2607.13332v1#S6.SS4 — 6.4 All-Reduce Failures。

**Artifact boundary。** Exact v1 links https://github.com/PluralisResearch/agora, https://github.com/PluralisResearch/node0, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The loss continues to decrease, but its trajectory becomes noticeably shallower around 3.1.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13332:end -->

<!-- review:SF-2026-ARXIV-2607-13359:start -->
### Learning Latency-Aware Orchestration for Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-13359:start -->Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations. Existing orchestration methods primarily optimize task performance and inference cost, leaving latency largely unaddressed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13359:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent systems (MAS) coordinate multiple LLM-powered agents through structured workflows, gaining reasoning power but incurring high inference latency from multi-step execution and repeated model invocations.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address this gap, we propose Latency-Aware Multi-agent System (LAMaS), a latency-aware orchestration framework for learning-based multi-agent systems.

**证据证明什么。** Experiments on four benchmarks show that LAMaS achieves the best latency among evaluated learning-based MAS baselines, reducing end-to-end latency by over 50\% while maintaining competitive or better accuracy.

**证据没有证明什么。** 5 Conclusion This paper addresses a key limitation of existing multi-agent orchestration methods: optimizing accuracy and cost alone does not reliably control execution latency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13359v1#S3 — 3 Methodology; https://arxiv.org/html/2607.13359v1#S3.SS2 — 3.2 Orchestrator Architecture。Evaluation：https://arxiv.org/html/2607.13359v1#S4.SS2 — 4.2 Result Analysis; https://arxiv.org/html/2607.13359v1#A2 — Appendix B Experimental Setup Details。Limitations / counterevidence：https://arxiv.org/html/2607.13359v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.13359v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：5 Conclusion This paper addresses a key limitation of existing multi-agent orchestration methods: optimizing accuracy and cost alone does not reliably control execution latency.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13359:end -->

<!-- review:SF-2026-ARXIV-2607-13389:start -->
### Where Should RL Post-Training Compute Go? Model Size, Search, Learning, and Feedback

<!-- claim:SF-2026-ARXIV-2607-13389:start -->Reinforcement Learning (RL) post-training is increasingly used to adapt foundation models for reasoning, planning, and feedback-driven robot-learning pipelines, but constrained post-training resources are often summarized by a single total FLOP budget. We study the fixed-budget decision problem behind this practice: under the same post-training budget, should one use a larger policy, train a smaller policy longer, generate more rollout search, or spend compute on stronger reward feedback? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13389:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement Learning (RL) post-training is increasingly used to adapt foundation models for reasoning, planning, and feedback-driven robot-learning pipelines, but constrained post-training resources are often summarized by a single total FLOP budget.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce a FLOP-accounting framework for GRPO post-training that decomposes compute into rollout/search, policy-update/learning, and reward- or feedback-model evaluation.

**证据证明什么。** We present RACE as a diagnostic pilot-grid protocol, not a guarantee of held-out improvement, for identifying allocation regimes before expensive validation runs; our results suggest that RL post-training papers should report total FLOPs together with how compute is divided among model size, search, learning, and feedback.

**证据没有证明什么。** We use one model family, GRPO, LoRA adaptation, and limited seeds. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13389v1#A1.SS2 — A.2 Stage A: Model-Aware IsoFLOP Design; https://arxiv.org/html/2607.13389v1#S3 — 3 Method: Conditional Compute Allocation。Evaluation：https://arxiv.org/html/2607.13389v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.13389v1#A1.SS1 — A.1 Overview of Experimental Stages。Limitations / counterevidence：https://arxiv.org/html/2607.13389v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.13389v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：We use one model family, GRPO, LoRA adaptation, and limited seeds.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13389:end -->

<!-- review:SF-2026-ARXIV-2607-13396:start -->
### Set-shifting Behavioral Test for Harnessed Agents

<!-- claim:SF-2026-ARXIV-2607-13396:start -->What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session? We borrow the notion of set-shifting from cognitive psychology to study how well agents adapt to hidden reliability shifts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13396:end -->

**为什么进入候选分母。** 摘要首要问题为“What happens to an LLM agent's tool choice when the reliable tool silently changes within an ongoing session?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a suite of measures to quantify agent behavior after reliability shifts.

**证据证明什么。** We conduct our study on a panel of LLMs equipped with harnesses and show that the same set of shifts results in distinct behaviors across models: some latch onto a fixed routine within a few turns, whereas others continue to vary.

**证据没有证明什么。** We have not yet included closed-weight frontier models because of per trajectory costs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13396v1#A2 — Appendix B Benchmark Construction and Verifier Design; https://arxiv.org/html/2607.13396v1#S3 — 3 Study Design and Evaluation。Evaluation：https://arxiv.org/html/2607.13396v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.13396v1#A2 — Appendix B Benchmark Construction and Verifier Design。Limitations / counterevidence：https://arxiv.org/html/2607.13396v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.13396v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/zwycl/wcst-tool-bench, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://github.com/NousResearch/hermes-agent; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We have not yet included closed-weight frontier models because of per trajectory costs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13396:end -->

<!-- review:SF-2026-ARXIV-2607-13399:start -->
### Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations

<!-- claim:SF-2026-ARXIV-2607-13399:start -->On-policy distillation (OPD) has become a key paradigm in LLM post-training, yet its training dynamics remain poorly understood. We present a systematic study examining the role, pathologies, and regulations of OPD. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13399:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation (OPD) has become a key paradigm in LLM post-training, yet its training dynamics remain poorly understood.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present a systematic study examining the role, pathologies, and regulations of OPD.

**证据证明什么。** We confirm this by showing that prompt diversity matters more than per-problem sampling numbers, and critically, that the effectiveness of OPD hinges entirely on the quality of its guiding signal.

**证据没有证明什么。** The behavior of regulated OPD in open-ended text generation or knowledge-intensive QA tasks has not been fully verified. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13399v1#S2.SS2 — 2.2 Empirical Framework and Setup。Evaluation：https://arxiv.org/html/2607.13399v1#A1 — Appendix A Experiment Configurations; https://arxiv.org/html/2607.13399v1#S5.SS2 — 5.2 Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.13399v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.13399v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The behavior of regulated OPD in open-ended text generation or knowledge-intensive QA tasks has not been fully verified.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13399:end -->

<!-- review:SF-2026-ARXIV-2607-13410:start -->
### Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation

<!-- claim:SF-2026-ARXIV-2607-13410:start -->World model (WM)-based reinforcement learning enables sample-efficient end-to-end autonomous driving learning by imagining long-horizon trajectories in latent space. However, most driving WMs operate on bird's-eye-view (BEV) representations that are inherently egocentric: the transition between consecutive frames entangles the ego vehicle's own motion with scene dynamics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13410:end -->

**为什么进入候选分母。** 摘要首要问题为“World model (WM)-based reinforcement learning enables sample-efficient end-to-end autonomous driving learning by imagining long-horizon trajectories in latent space.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** This work proposes DynaDreamer, a dynamics-augmented Dreamer-style reinforcement learning method to address this problem by augmenting the WM with an explicit ego-dynamics prior.

**证据证明什么。** Experiments demonstrate that DynaDreamer improves task success rates over the strongest baseline by 28% and 61% in urban and highway driving scenarios, respectively, with the advantage rising to 73% when extrapolating to unseen chassis.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13410v1#S4 — IV Methodology; https://arxiv.org/html/2607.13410v1#S2.SS1 — II-A World Models for Autonomous Driving。Evaluation：https://arxiv.org/html/2607.13410v1#S6 — VI Experiments; https://arxiv.org/html/2607.13410v1#S6.SS1 — VI-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13410v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13410:end -->

<!-- review:SF-2026-ARXIV-2607-13411:start -->
### Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors

<!-- claim:SF-2026-ARXIV-2607-13411:start -->Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time. We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13411:end -->

**为什么进入候选分母。** 摘要首要问题为“Clinical AI models can expose patients to harm when adversarial vulnerabilities go undetected, yet formal security auditing requires statistical expertise, specialized tools, and significant time.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present an open evaluation task, built on METR Task Standard v0.3.0, that tests whether frontier AI agents can autonomously implement a structured clinical AI security audit.

**证据证明什么。** The task, scoring infrastructure, and Wisconsin Breast Cancer assets are publicly released; MIMIC-IV variants require separate PhysioNet access.

**证据没有证明什么。** A harder version of the task would require the agent to determine the appropriate attacks from a clinical security specification without pseudocode. (4) MIMIC-IV reproducibility : The MIMIC-IV variants cannot be replicated without independent PhysioNet credentials, which limits reproducibility of those six out of 18 runs per model. (5) Run count : Three runs per variant is a minimum for variance estimation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13411v1#S2.SS3 — 2.3 Model Calibration and Uncertainty Quantification; https://arxiv.org/html/2607.13411v1#S4.SS1 — 4.1 Models Evaluated。Evaluation：https://arxiv.org/html/2607.13411v1#S2.SS6 — 2.6 Agent Evaluation Benchmarks; https://arxiv.org/html/2607.13411v1#A2 — Appendix B Complete Per-Run Results。Limitations / counterevidence：https://arxiv.org/html/2607.13411v1#S6.SS5 — 6.5 Limitations and Future Work; https://arxiv.org/html/2607.13411v1#S2.SS4 — 2.4 Adversarial Threats in Clinical and Healthcare AI。

**Artifact boundary。** Exact v1 links https://github.com/MichaelEnny/clinical-ai-security-eval, https://github.com/METR/task-standard, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A harder version of the task would require the agent to determine the appropriate attacks from a clinical security specification without pseudocode. (4) MIMIC-IV reproducibility : The MIMIC-IV variants cannot be replicated without independent PhysioNet credentials, which limits reproducibility of those six out of 18 runs per model. (5) Run count : Three runs per variant is a minimum for variance estimation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13411:end -->

<!-- review:SF-2026-ARXIV-2607-13418:start -->
### Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender Systems with Collaborative Agents

<!-- claim:SF-2026-ARXIV-2607-13418:start -->Recommender systems operate as Black-Boxes, leaving users and regulators unable to steer their outputs toward specific intentions or audit their behavior. This lack of controllability, defined as the system's ability to respond to explicit guidance, remains an unaddressed dimension in existing evaluation paradigms. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13418:end -->

**为什么进入候选分母。** 摘要首要问题为“Recommender systems operate as Black-Boxes, leaving users and regulators unable to steer their outputs toward specific intentions or audit their behavior.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To fill this gap, we propose CtrlBench-Rec, a collaborative multi-agent framework for systematic assessment of controllability.

**证据证明什么。** We formalize three fundamental tasks: target content discovery, interest profile shaping, and popularity bias mitigation, which together measure steerability from explicit commands to implicit representation steering and finally to overcoming algorithmic biases.Extensive experiments on real-world datasets and multiple recommendation models demonstrate that our framework effectively quantifies controllability and exposes critical system bottlenecks, most notably persistent resistance to guiding long tail content.

**证据没有证明什么。** Future work includes extending to more fine-grained tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13418v1#A4.SS5 — D.5 Black-Box Recommender Systems; https://arxiv.org/html/2607.13418v1#A4.SS6 — D.6 The Performance of Different Recommender Systems in Task 1。Evaluation：https://arxiv.org/html/2607.13418v1#A4 — Appendix D Detailed Experimental Setup; https://arxiv.org/html/2607.13418v1#A4.SS3 — D.3 Training Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.13418v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.13418v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/caskcsg/CtrlBenchRec, https://github.com/camel-ai/oasis, https://huggingface.co/datasets/smartcat/Amazon_Toys_and_Games_2018; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work includes extending to more fine-grained tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13418:end -->

<!-- review:SF-2026-ARXIV-2607-13429:start -->
### Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

<!-- claim:SF-2026-ARXIV-2607-13429:start -->Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13429:end -->

**为什么进入候选分母。** 摘要首要问题为“Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Anchor-Align, which augments BC with two objectives: Vision-Language Anchoring distills layer-wise representations from a frozen VLM copy to prevent this drift, while Language-Action Alignment converts each action target into a discrete motion-direction label and jointly trains language and action prediction on the same robot observation.

**证据证明什么。** At scale in simulation, we demonstrate consistent improvements on OOD perturbations, perceptual robustness, and long-horizon control across LIBERO-PRO, LIBERO-Plus, and CALVIN, respectively, suggesting that preserving pretrained representations and effective action learning are not fundamentally at odds.

**证据没有证明什么。** 5 Conclusion and Future Work Standard BC overwrites pretrained VLM semantics and co-training leaves VLA language and action misaligned. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13429v1#S3 — 3 Anchor-Align Method; https://arxiv.org/html/2607.13429v1#S3.SS1 — 3.1 Base VLA Architecture。Evaluation：https://arxiv.org/html/2607.13429v1#A3 — Appendix C Extended Quantitative Results; https://arxiv.org/html/2607.13429v1#A3.SS3 — C.3 Multi-Seed Evaluation: Statistical Significance。Limitations / counterevidence：https://arxiv.org/html/2607.13429v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/lerobot, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5 Conclusion and Future Work Standard BC overwrites pretrained VLM semantics and co-training leaves VLA language and action misaligned.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13429:end -->

<!-- review:SF-2026-ARXIV-2607-13441:start -->
### ReBound: Reuse-Aware Privacy For Interactive Decision Support

<!-- claim:SF-2026-ARXIV-2607-13441:start -->Differentially private decision support frameworks answer complex aggregate threshold queries with formal bounds on false negative and false positive rates, but treat each query independently with no memory of past results. In practice, analysts work interactively, issuing sequences of related queries that refine bounds, adjust thresholds, or derive new functions from previous ones. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13441:end -->

**为什么进入候选分母。** 摘要首要问题为“Differentially private decision support frameworks answer complex aggregate threshold queries with formal bounds on false negative and false positive rates, but treat each query independently with no memory of past results.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose ReBound, a framework that reuses cached results from previous queries to answer new queries at reduced or zero additional privacy cost while maintaining formal utility guarantees.

**证据证明什么。** We propose ReBound, a framework that reuses cached results from previous queries to answer new queries at reduced or zero additional privacy cost while maintaining formal utility guarantees.

**证据没有证明什么。** However, all three treat each query independently and do not exploit the natural overlap in interactive analyst sessions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13441v1#S4 — 4. Framework Overview。Evaluation：https://arxiv.org/html/2607.13441v1#S5 — 5. Preliminary Results。Limitations / counterevidence：https://arxiv.org/html/2607.13441v1#S1 — 1. Introduction; https://arxiv.org/html/2607.13441v1#S2 — 2. Background。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, all three treat each query independently and do not exploit the natural overlap in interactive analyst sessions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13441:end -->

<!-- review:SF-2026-ARXIV-2607-13465:start -->
### DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments

<!-- claim:SF-2026-ARXIV-2607-13465:start -->LLM-based agents have rapidly improved at operating individual digital environments such as mobile applications, desktop systems, and smart homes. However, real-world user goals often span multiple devices: information may come from a phone, be processed on a desktop, and the result may need to appear on another device. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13465:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based agents have rapidly improved at operating individual digital environments such as mobile applications, desktop systems, and smart homes.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate five frontier LLM-agent systems on a fixed evaluation set.

**证据证明什么。** All methods achieve low success rates, with the best reaching only 12.5%.

**证据没有证明什么。** For subgoals with prerequisite dependencies, the agent should not bypass an unsatisfied prerequisite. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13465v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13465v1#S2 — 2 Cross-Device Collaborative Operation。Evaluation：https://arxiv.org/html/2607.13465v1#S3.SS1 — 3.1 Benchmark Overview; https://arxiv.org/html/2607.13465v1#S3.SS4 — 3.4 Task Execution and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13465v1#S4.SS3 — 4.3 Failure Analysis; https://arxiv.org/html/2607.13465v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/AgenticOrgLab/DevicesWorld, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：For subgoals with prerequisite dependencies, the agent should not bypass an unsatisfied prerequisite.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13465:end -->

<!-- review:SF-2026-ARXIV-2607-13474:start -->
### MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent Systems

<!-- claim:SF-2026-ARXIV-2607-13474:start -->We present MyAG, a graph-based framework for designing and analyzing composable LLM agent systems. Our framework separates agent system construction into three graph abstractions: a component graph for agents, environments, and modules; a workflow graph for execution control; and a search graph for runtime execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13474:end -->

**为什么进入候选分母。** 摘要首要问题为“We present MyAG, a graph-based framework for designing and analyzing composable LLM agent systems.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present MyAG, a graph-based framework for designing and analyzing composable LLM agent systems.

**证据证明什么。** Experiments on representative agent applications show that our framework supports flexible agent system design and helps analyze performance-efficiency tradeoffs.

**证据没有证明什么。** Limitations MyAG is designed as a lightweight, research-oriented framework rather than a full production platform. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13474v1#S2 — 2 Framework。Evaluation：https://arxiv.org/html/2607.13474v1#A2 — Appendix B Extra Results; https://arxiv.org/html/2607.13474v1#S2.SS3 — 2.3 Efficiency Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.13474v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.13474v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/zzsfornlp/MyAG, https://github.com/zzsfornlp/MyAG/blob/main/demo.mp4, https://github.com/langchain-ai/langgraph; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations MyAG is designed as a lightweight, research-oriented framework rather than a full production platform.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13474:end -->

<!-- review:SF-2026-ARXIV-2607-13477:start -->
### Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation

<!-- claim:SF-2026-ARXIV-2607-13477:start -->Large audio-language models (LALMs) are increasingly used as automatic judges for speech evaluation. However, high agreement with human ratings does not guarantee that their verdicts are grounded in the audio. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13477:end -->

**为什么进入候选分母。** 摘要首要问题为“Large audio-language models (LALMs) are increasingly used as automatic judges for speech evaluation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, high agreement with human ratings does not guarantee that their verdicts are grounded in the audio.

**证据证明什么。** Across six judges and four attributes, we find that several LALMs rely on protocol-level shortcuts.

**证据没有证明什么。** This contrast suggests a capability-dependent shortcut: the blueprint channel becomes unreliable when the judge cannot verify the specialist field acoustically. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13477v1#S3 — III Method; https://arxiv.org/html/2607.13477v1#S4.SS3 — IV-C Specialist models。Evaluation：https://arxiv.org/html/2607.13477v1#S4 — IV Experimental Setup; https://arxiv.org/html/2607.13477v1#S5 — V Results。Limitations / counterevidence：https://arxiv.org/html/2607.13477v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This contrast suggests a capability-dependent shortcut: the blueprint channel becomes unreliable when the judge cannot verify the specialist field acoustically.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13477:end -->

<!-- review:SF-2026-ARXIV-2607-13511:start -->
### ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level

<!-- claim:SF-2026-ARXIV-2607-13511:start -->We introduce ExTernD (Expanded-rank Ternary Decomposition), a post-training factorization of each LLM weight matrix $A \in \mathbb{R}^{m \times n}$ into $A \approx B \mathrm{diag}(D) C$ with ternary factors $B \in \{-1,0,+1\}^{m \times k}$, $C \in \{-1,0,+1\}^{k \times n}$ and a real scale vector $D \in \mathbb{R}^k$. The inner rank $k = μ\min(m,n)$ is deliberately expanded beyond full rank ($μ&gt; 1$), so that components past full rank correct the quantization error of earlier ones. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13511:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce ExTernD (Expanded-rank Ternary Decomposition), a post-training factorization of each LLM weight matrix $A \in \mathbb{R}^{m \times n}$ into $A \approx B \mathrm{diag}(D) C$ with ternary factors $B \in \{-1,0,+1\}^{m \times k}$, $C \in \{-1,0,+1\}^{k \times n}$ and a real scale vector $D \in \mathbb{R}^k$.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We introduce ExTernD (Expanded-rank Ternary Decomposition), a post-training factorization of each LLM weight matrix $A \in \mathbb{R}^{m \times n}$ into $A \approx B \mathrm{diag}(D) C$ with ternary factors $B \in \{-1,0,+1\}^{m \times k}$, $C \in \{-1,0,+1\}^{k \times n}$ and a real scale vector $D \in \mathbb{R}^k$.

**证据证明什么。** ExTernD matches Q4_K's per-matrix accuracy at 5.2-5.5 effective bpw (5.1-5.5 with importance weighting) on Gemma-4-E2B and Qwen3.5-4B, and a full Qwen3.5-4B conversion at $μ= 3$ reaches 10.10 wikitext-2 perplexity against 9.78 for bf16 (+3.2%), placing it near the Q4_K/Q5_K accuracy band at ~5.7 effective bpw.

**证据没有证明什么。** 2.1 ), but end-to-end task accuracy is not yet measured. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13511v1#S2 — 2 Method; https://arxiv.org/html/2607.13511v1#S2.SS6 — 2.6 Cost model。Evaluation：https://arxiv.org/html/2607.13511v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.13511v1#S5 — 5 Limitations; https://arxiv.org/html/2607.13511v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：2.1 ), but end-to-end task accuracy is not yet measured.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13511:end -->

<!-- review:SF-2026-ARXIV-2607-13527:start -->
### VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation

<!-- claim:SF-2026-ARXIV-2607-13527:start -->Recent video generation models (VGMs) have made substantial progress in visual fidelity, yet their ability to follow long, compositional instructions remains insufficiently evaluated. Existing evaluation protocols often rely on prompts that are short and semantically shallow, with limited atomic constraints and weak spatio-temporal dependencies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13527:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent video generation models (VGMs) have made substantial progress in visual fidelity, yet their ability to follow long, compositional instructions remains insufficiently evaluated.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we propose VGIF-Score, a highly automated and interpretable framework for evaluating instruction following in video generation.

**证据证明什么。** Experiments on 14 proprietary and open-source VGMs across more than 3K generated videos show that VGIF-Score provides reliable, interpretable, and diagnostically useful evaluation of video generation instruction following.

**证据没有证明什么。** We hope our work can support more diagnostic evaluation and guide future video generation models toward stronger semantic and causal instruction following. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13527v1#S3.SS1 — 3.1 Framework Overview。Evaluation：https://arxiv.org/html/2607.13527v1#S4.SS1 — 4.1 Benchmark Construction; https://arxiv.org/html/2607.13527v1#S4.SS2 — 4.2 Benchmark Structure and Distribution。Limitations / counterevidence：https://arxiv.org/html/2607.13527v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/PRIS-CV/VGIF-SCORE, https://github.com/genmoai/models, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We hope our work can support more diagnostic evaluation and guide future video generation models toward stronger semantic and causal instruction following.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13527:end -->

<!-- review:SF-2026-ARXIV-2607-13541:start -->
### When T2I Synthetic Data Backfires: Amplified Privacy Risks in Real-Synthetic Mix Training

<!-- claim:SF-2026-ARXIV-2607-13541:start -->To overcome data scarcity and privacy constraints in data collection, it has become standard practice across academia and industry to augment real training data with text-to-image (T2I)-generated synthetic data, a paradigm we term Real-Synthetic Mix-Training (RSMT). While substituting synthetic data for sensitive real samples is widely regarded as a means to mitigate privacy exposure of the substituted data, the risk to the remaining real samples that actively participate in training has remained largely unexamined. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13541:end -->

**为什么进入候选分母。** 摘要首要问题为“To overcome data scarcity and privacy constraints in data collection, it has become standard practice across academia and industry to augment real training data with text-to-image (T2I)-generated synthetic data, a paradigm we term Real-Synthetic Mix-Training (RSMT).”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Guided by this foundation, we propose RSMixLeak to systematically assess this risk through membership inference attacks (MIAs).

**证据证明什么。** Motivated by these findings, we further propose a lightweight leakage propensity indicator computable from real data alone that reliably identifies high-risk datasets unsuitable for entering RSMT, as a self-assessable mitigation.

**证据没有证明什么。** The adversary cannot access the internal parameters of the victim model nor tamper with the RSMT pipeline at training time (e.g., data poisoning [ 82 ] ) or inference time (e.g., fault injection [ 83 ] ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13541v1#S4.SS2 — IV-B Method; https://arxiv.org/html/2607.13541v1#S5.SS2 — V-B Attack Methodology。Evaluation：https://arxiv.org/html/2607.13541v1#S4.SS4 — IV-D Evaluation Results; https://arxiv.org/html/2607.13541v1#S5.SS5 — V-E Evaluation Results。Limitations / counterevidence：https://arxiv.org/html/2607.13541v1#S1.SS1 — I-A Limitation; https://arxiv.org/html/2607.13541v1#S4.SS1 — IV-A Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/TencentARC/FluxKits, https://huggingface.co/TencentARC/flux-mini, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The adversary cannot access the internal parameters of the victim model nor tamper with the RSMT pipeline at training time (e.g., data poisoning [ 82 ] ) or inference time (e.g., fault injection [ 83 ] ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13541:end -->

<!-- review:SF-2026-ARXIV-2607-13591:start -->
### Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents

<!-- claim:SF-2026-ARXIV-2607-13591:start -->Large Language Model (LLM) agents increasingly rely on external memory systems to accumulate experience across tasks. Yet nearly all existing approaches, from graph-structured memories to reflective insight stores, access memory through fixed, hand-designed heuristics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13591:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents increasingly rely on external memory systems to accumulate experience across tasks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present Memory as a Controlled Process (MemCon), a framework that models memory operations as a Markov Decision Process and learns an online policy that adaptively decides when, what, and how much to retrieve, when to inject a distilled plan, and when to consolidate or forget.

**证据证明什么。** Across 6 benchmarks, 3 agent frameworks, and 3 LLM backbones, MemCon consistently outperforms multiple memory baselines by up to 15.2 points in task success while reducing token consumption by 5--20%.

**证据没有证明什么。** These results suggest that effective long-term memory for LLM agents depends not only on what is stored, but also on learning how memory should be accessed and managed over time. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13591v1#A1.SS2 — A.2 Agent Frameworks; https://arxiv.org/html/2607.13591v1#A5.SS1 — E.1 Benchmark Solver System Prompts。Evaluation：https://arxiv.org/html/2607.13591v1#A1 — Appendix A Experimental Setup Details; https://arxiv.org/html/2607.13591v1#A1.SS1 — A.1 Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.13591v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ericjiang18/MemCon/, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：These results suggest that effective long-term memory for LLM agents depends not only on what is stored, but also on learning how memory should be accessed and managed over time.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13591:end -->

<!-- review:SF-2026-ARXIV-2607-13594:start -->
### SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing

<!-- claim:SF-2026-ARXIV-2607-13594:start -->LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm. The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13594:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents act on real-world environments through tool calls, and a single misjudged action can cause irreversible harm.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The standard safeguard is a guard model that labels each proposed action as safe or unsafe, but this binary view conflates two distinct decisions: whether the action is harmful in itself, and whether it is appropriate given the user's context.

**证据证明什么。** Safety Sentry outperforms a broad set of open-weight and frontier closed-source baselines on overall accuracy and safety-related recall, while controlling both directional error rates simultaneously.

**证据没有证明什么。** Separating Ask from Refuse lets the guard defer without rejecting, balancing autonomy and oversight in a way binary guards cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13594v1#S3 — 3 Method; https://arxiv.org/html/2607.13594v1#S4.SS6 — 4.6 Robustness to Framework and Backbone。Evaluation：https://arxiv.org/html/2607.13594v1#S4 — 4 Experiments; https://arxiv.org/html/2607.13594v1#S4.SS2 — 4.2 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.13594v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.13594v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Separating Ask from Refuse lets the guard defer without rejecting, balancing autonomy and oversight in a way binary guards cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13594:end -->

<!-- review:SF-2026-ARXIV-2607-13596:start -->
### Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities

<!-- claim:SF-2026-ARXIV-2607-13596:start -->When cast as the protector of a vulnerable user yet given no explicit capability boundary, a large language model (LLM) may respond not by acknowledging its limits but by claiming to have taken -- or to be taking -- a real-world protective action it cannot perform, such as contacting emergency services or administering care. We term this phenomenon Protective Capacity Hallucination (PCH): a self-referential misattribution in which a model, acting in a protective role, asserts physical or institutional agency exceeding its affordances as a language model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13596:end -->

**为什么进入候选分母。** 摘要首要问题为“When cast as the protector of a vulnerable user yet given no explicit capability boundary, a large language model (LLM) may respond not by acknowledging its limits but by claiming to have taken -- or to be taking -- a real-world protective action it cannot perform, such as contacting emergency services or administering care.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We term this phenomenon Protective Capacity Hallucination (PCH): a self-referential misattribution in which a model, acting in a protective role, asserts physical or institutional agency exceeding its affordances as a language model.

**证据证明什么。** In a three-phase study spanning eight LLMs and 13{,}600 sessions, we find PCH jointly gated by situational severity and interactional format: multi-party dialogic input drives it toward ceiling in most models across ordinary service domains, whereas in intimate-partner conflict -- a domain explicitly covered by safety alignment -- it remains at floor in all eight models despite greater physical severity.

**证据没有证明什么。** Each condition is furthermore instantiated by a single stimulus, so condition effects cannot be fully separated from stimulus idiosyncrasy; we deliberately varied surface-level structure across domains, and the framing effect replicates directionally across all six uncovered service scenarios, but within-condition stimulus sampling remains a target for follow-up work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13596v1#Sx4 — Methodology; https://arxiv.org/html/2607.13596v1#Sx4.SSx1 — Experimental Design。Evaluation：https://arxiv.org/html/2607.13596v1#Sx4.SSx1 — Experimental Design; https://arxiv.org/html/2607.13596v1#Sx5 — Results。Limitations / counterevidence：https://arxiv.org/html/2607.13596v1#Sx6 — Discussion; https://arxiv.org/html/2607.13596v1#Sx6.SSx7 — Scope and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Each condition is furthermore instantiated by a single stimulus, so condition effects cannot be fully separated from stimulus idiosyncrasy; we deliberately varied surface-level structure across domains, and the framing effect replicates directionally across all six uncovered service scenarios, but within-condition stimulus sampling remains a target for follow-up work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13596:end -->

<!-- review:SF-2026-ARXIV-2607-13605:start -->
### An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-13605:start -->One high-level instruction in long-horizon manipulation can cover several action stages. We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13605:end -->

**为什么进入候选分母。** 摘要首要问题为“One high-level instruction in long-horizon manipulation can cover several action stages.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We use segmented action annotations as an intermediate representation between the full-task instruction and VLA action chunks.

**证据证明什么。** Under direct fine-tuning, full-task instruction, current-stage text, and Ordinal Stage-State achieve mean success rates of 57.45%, 50.24%, and 54.36%, respectively, showing that explicit stage information does not automatically improve the policy.

**证据没有证明什么。** Three paired action-policy runs provide only a limited view of variation across training seeds. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13605v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.13605v1#S4 — IV Experiments; https://arxiv.org/html/2607.13605v1#S4.SS1 — IV-A Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13605v1#S5 — V Discussion; https://arxiv.org/html/2607.13605v1#S5.SS3 — V-C Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Three paired action-policy runs provide only a limited view of variation across training seeds.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13605:end -->

<!-- review:SF-2026-ARXIV-2607-13618:start -->
### STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle

<!-- claim:SF-2026-ARXIV-2607-13618:start -->LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed. On such tasks the final cost cannot say why an agent failed: it may have misread the world, or read it correctly and still failed to act (the knowing-doing gap). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13618:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents are increasingly evaluated on multi-week decision tasks in which the state that drives cost is never directly observed.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce STOCKTAKE, a 26-week supply-chain replenishment benchmark built as a factored partially observable Markov decision process with six hidden factor processes, designed so that a fair reference policy is computable: an exact Bayes filter per factor drives a rollout policy on the identical observation stream the agent receives.

**证据证明什么。** STOCKTAKE measures both directions of that failure.

**证据没有证明什么。** A stratified manual read found the labels correct on the sampled metric-relevant weeks, and an independent second grader agrees with the production grader on the metric-relevant component (which named factors intersect true stress) at 89%; residual disagreement sits on calm-week over-labels, which cannot enter the knowing-doing rate by construction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13618v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13618v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.13618v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.13618v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.13618v1#S6 — 6 Discussion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A stratified manual read found the labels correct on the sampled metric-relevant weeks, and an independent second grader agrees with the production grader on the metric-relevant component (which named factors intersect true stress) at 89%; residual disagreement sits on calm-week over-labels, which cannot enter the knowing-doing rate by construction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13618:end -->

<!-- review:SF-2026-ARXIV-2607-13640:start -->
### WarpGuard: Towards Control-Flow Attestation for Heterogeneous CPU-GPU Execution

<!-- claim:SF-2026-ARXIV-2607-13640:start -->Heterogeneous CPU-GPU workloads are increasingly used in safety-critical embedded systems, yet no existing approach provides joint attestation of their execution. Prior Control-Flow Attestation (CFA) techniques focus on CPU-side CFA, while GPU attestation is limited to static, load-time verification and does not provide runtime guarantees. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13640:end -->

**为什么进入候选分母。** 摘要首要问题为“Heterogeneous CPU-GPU workloads are increasingly used in safety-critical embedded systems, yet no existing approach provides joint attestation of their execution.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present WarpGuard, the first composite CFA framework for heterogeneous CPU-GPU workloads.

**证据证明什么。** Our evaluation on an NVIDIA Jetson Orin Nano shows that WarpGuard detects GPU-side control-flow and cross-boundary attacks.

**证据没有证明什么。** Threat Model Our threat model is influenced by our motivating scenario of a robotics platform (Sec. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13640v1#S2.SS3 — 2.3. NVIDIA GPU Architecture; https://arxiv.org/html/2607.13640v1#S5 — 5. Design。Evaluation：https://arxiv.org/html/2607.13640v1#S7 — 7. Evaluation; https://arxiv.org/html/2607.13640v1#S7.SS1 — 7.1. Performance Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.13640v1#S10 — 10. Conclusion; https://arxiv.org/html/2607.13640v1#S4 — 4. Threat Model。

**Artifact boundary。** Exact v1 links https://cordis.europa.eu/project/id/101167904, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Threat Model Our threat model is influenced by our motivating scenario of a robotics platform (Sec.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13640:end -->

<!-- review:SF-2026-ARXIV-2607-13649:start -->
### CIMERA: Compute-in-Interconnect and Memory with Reconfigurable Precision for LLM Inference

<!-- claim:SF-2026-ARXIV-2607-13649:start -->LLM impose significant computational and memory demands, creating challenges for energy-efficient inference across platforms ranging from data centers to power-constrained edge devices. Weight precision plays a critical role in balancing inference accuracy, throughput, and energy consumption, while modern LLM workloads exhibit pronounced heterogeneity and tolerance that favors adaptive precision execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13649:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM impose significant computational and memory demands, creating challenges for energy-efficient inference across platforms ranging from data centers to power-constrained edge devices.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Weight precision plays a critical role in balancing inference accuracy, throughput, and energy consumption, while modern LLM workloads exhibit pronounced heterogeneity and tolerance that favors adaptive precision execution.

**证据证明什么。** Compared to Nvidia H100, CIMERA delivers up to $25\times$ and $10\times$ higher energy efficiency for 1B and 13B models, respectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13649v1#S2 — II CIMERA Hardware Architecture; https://arxiv.org/html/2607.13649v1#S4 — IV System Evaluation。Evaluation：https://arxiv.org/html/2607.13649v1#S4 — IV System Evaluation; https://arxiv.org/html/2607.13649v1#S4.SS1 — IV-A Performance Benchmarking。Limitations / counterevidence：https://arxiv.org/html/2607.13649v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13649:end -->

<!-- review:SF-2026-ARXIV-2607-13651:start -->
### From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring

<!-- claim:SF-2026-ARXIV-2607-13651:start -->The bottleneck of Earth Observation processing chains is not the arrival of new imagery but whether the surface is actually visible when the image arrives. We study this as an observability forecasting problem on EarthNet2021. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13651:end -->

**为什么进入候选分母。** 摘要首要问题为“The bottleneck of Earth Observation processing chains is not the arrival of new imagery but whether the surface is actually visible when the image arrives.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We study this as an observability forecasting problem on EarthNet2021.

**证据证明什么。** On the full frozen-bundle observability benchmark, LeWorldModel consistently outperforms persistence.

**证据没有证明什么。** The contribution is not a new world-model architecture. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13651v1#S5 — 5 Model; https://arxiv.org/html/2607.13651v1#S5.SS1 — 5.1 EarthNet2021 adaptation of LeWorldModel。Evaluation：https://arxiv.org/html/2607.13651v1#A1 — Appendix A Supplementary Results; https://arxiv.org/html/2607.13651v1#A1.SS1 — A.1 Training checkpoint used in all experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13651v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.13651v1#S9 — 9 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/AlbughdadiM/lewm-eo-cloud-monitoring, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The contribution is not a new world-model architecture.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13651:end -->

<!-- review:SF-2026-ARXIV-2607-13683:start -->
### HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution

<!-- claim:SF-2026-ARXIV-2607-13683:start -->Large Language Models (LLMs) have enabled capable agents across diverse applications. Beyond the foundation model, the performance of an agent is governed by the surrounding agent harness, including prompts, tools, control loops, etc. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13683:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have enabled capable agents across diverse applications.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To tackle these challenges, we introduce HarnessBank, a trustworthy agent-harness self-evolution framework that pairs a task agent with a separate evolver agent for iterative failure diagnosis, harness generation, and evolution verification.

**证据证明什么。** Across seven agent benchmarks, HarnessBank produces consistent performance improvements from 5.1% to 15.4%.

**证据没有证明什么。** Because one cannot assume a new model shares a given pathology, a new model still needs its own diagnosis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13683v1#S3 — 3 Method; https://arxiv.org/html/2607.13683v1#S4.SS5 — 4.5 Cross-model dissociation。Evaluation：https://arxiv.org/html/2607.13683v1#A2 — Appendix B Formal analysis; https://arxiv.org/html/2607.13683v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13683v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.13683v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Because one cannot assume a new model shares a given pathology, a new model still needs its own diagnosis.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13683:end -->

<!-- review:SF-2026-ARXIV-2607-13705:start -->
### AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities

<!-- claim:SF-2026-ARXIV-2607-13705:start -->As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical. However, current evaluation pipelines remain highly fragmented and tightly coupled, hindering reproducibility and causing redundant engineering. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13705:end -->

**为什么进入候选分母。** 摘要首要问题为“As Large Language Models (LLMs) evolve into autonomous agents, the need for unified evaluation infrastructure becomes critical.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents.

**证据证明什么。** Natively supporting over 20 benchmarks across five capability dimensions, AgentCompass provides the community with a scalable and reproducible infrastructure for advancing agent research.

**证据没有证明什么。** By decoupling the evaluation pipeline into independent Model, Benchmark, Harness, and Environment components, it eliminates redundant engineering and ensures rigorous reproducibility. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13705v1#S3 — 3 Framework; https://arxiv.org/html/2607.13705v1#S3.SS1 — 3.1 Design Overview。Evaluation：https://arxiv.org/html/2607.13705v1#S4.SS3 — 4.3 Analysis Results; https://arxiv.org/html/2607.13705v1#A1 — Appendix A Detailed Experimental Configurations。Limitations / counterevidence：https://arxiv.org/html/2607.13705v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/open-compass/AgentCompass, https://github.com/paul-gauthier/aider, https://github.com/confident-ai/deepeval; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：By decoupling the evaluation pipeline into independent Model, Benchmark, Harness, and Environment components, it eliminates redundant engineering and ensures rigorous reproducibility.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13705:end -->

<!-- review:SF-2026-ARXIV-2607-13716:start -->
### CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems

<!-- claim:SF-2026-ARXIV-2607-13716:start -->Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines. A single operational act such as publishing code, changing identity state, moving money, or exporting data may therefore be represented by many incompatible runtime records. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13716:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic AI systems increasingly act through heterogeneous runtimes: local coding hooks, SDK tools, browser automation, managed-agent traces, API gateways, and workflow engines.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance.

**证据证明什么。** The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance.

**证据没有证明什么。** Attestation failure Signature, credential, or ledger anchor cannot verify. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13716v1#A1 — Appendix A System Scope and Release Posture; https://arxiv.org/html/2607.13716v1#A5 — Appendix E Safeguard Design。Evaluation：https://arxiv.org/html/2607.13716v1#A10 — Appendix J Comparative Evaluation; https://arxiv.org/html/2607.13716v1#A16 — Appendix P Benchmark Dataset Schema。Limitations / counterevidence：https://arxiv.org/html/2607.13716v1#A8 — Appendix H Failure Modes and Incident Classes; https://arxiv.org/html/2607.13716v1#S10 — 10 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/open-telemetry/semantic-conventions-genai, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Attestation failure Signature, credential, or ledger anchor cannot verify.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13716:end -->

<!-- review:SF-2026-ARXIV-2607-13718:start -->
### How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement

<!-- claim:SF-2026-ARXIV-2607-13718:start -->As AI agents gain prevalence, users are increasingly exposed to the risks such systems entail. Prompt injection attacks, as well as hallucination, can cause agents to leak private information to third parties. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13718:end -->

**为什么进入候选分母。** 摘要首要问题为“As AI agents gain prevalence, users are increasingly exposed to the risks such systems entail.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** As AI agents gain prevalence, users are increasingly exposed to the risks such systems entail.

**证据证明什么。** We identify several high-level themes across the literature and commercial agents, as well as multiple gaps where future work is needed.

**证据没有证明什么。** 6 Limitations Our survey of papers and proposals relating to user-level agent permissions represents only a snapshot of current work in the area. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13718v1#S2.SS2 — 2.2 User-Facing Permissions in Non-AI Systems; https://arxiv.org/html/2607.13718v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.13718v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.13718v1#S5 — 5 Discussion; https://arxiv.org/html/2607.13718v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：6 Limitations Our survey of papers and proposals relating to user-level agent permissions represents only a snapshot of current work in the area.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13718:end -->

<!-- review:SF-2026-ARXIV-2607-13753:start -->
### Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and OPD Shape CoT Calibration

<!-- claim:SF-2026-ARXIV-2607-13753:start -->Large language models have made strong reasoning gains through supervised fine-tuning, reinforcement learning, and on-policy distillation, yet these post-training methods are usually evaluated only by final-answer accuracy. We study how they reshape confidence during reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13753:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models have made strong reasoning gains through supervised fine-tuning, reinforcement learning, and on-policy distillation, yet these post-training methods are usually evaluated only by final-answer accuracy.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a three-stage calibration framework that evaluates confidence before, during, and after chain-of-thought generation, corresponding to difficulty estimation, early termination, and answer aggregation.

**证据证明什么。** PosConf improves RL answer aggregation by 6.1 points over majority voting and consistently improves OPD early stopping under tight token budgets, with gains up to 4.3 points by avoiding its later inverse-calibration region, showing that \emph{confidence in reasoning models should be used both stage-wise and position-awarely}.

**证据没有证明什么。** We further find that confidence reliability is position-dependent within reasoning traces. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13753v1#S2 — 2 Confidence Calibration Framework; https://arxiv.org/html/2607.13753v1#S3.SS0.SSS0.Px1 — Models.。Evaluation：https://arxiv.org/html/2607.13753v1#A3 — Appendix C Inference and Evaluation Protocol; https://arxiv.org/html/2607.13753v1#A3.SS0.SSS0.Px2 — Repeated evaluation.。Limitations / counterevidence：https://arxiv.org/html/2607.13753v1#S6 — 6 Discussion; https://arxiv.org/html/2607.13753v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/EIT-NLP/Post-Training-Calibration, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We further find that confidence reliability is position-dependent within reasoning traces.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13753:end -->

<!-- review:SF-2026-ARXIV-2607-13854:start -->
### SPyCE: Skill-Policy Co-evolution for Multimodal Agents

<!-- claim:SF-2026-ARXIV-2607-13854:start -->Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps. Existing reinforcement learning methods reduce trajectories to scalar rewards, forcing the policy to discover reusable tool-use patterns from scratch on every new task; memory-based alternatives retain past experience, yet they rely on test-time retrieval, without updating the policy to absorb reusable patterns from that experience. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13854:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal agents that think with images iteratively manipulate visual evidence and invoke tools across many steps.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To this end, we propose SPyCE (Skill-Policy Co-evolution), a framework that distills trajectories into a hierarchical skill library and updates it throughout reinforcement learning.

**证据证明什么。** Experiments across eight benchmarks demonstrate that SPyCE consistently outperforms both RL-based and memory-based baselines.

**证据没有证明什么。** The analyses further highlight the notable skill evolution dynamics exhibited by our method. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13854v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.13854v1#S4 — 4 Experiments; https://arxiv.org/html/2607.13854v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13854v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The analyses further highlight the notable skill evolution dynamics exhibited by our method.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13854:end -->

<!-- review:SF-2026-ARXIV-2607-13884:start -->
### Experience Memory Graph: One-Shot Error Correction for Agents

<!-- claim:SF-2026-ARXIV-2607-13884:start -->Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations. However, in complex, long-horizon tasks, these agents frequently suffer from compounding errors and struggle to recover from failures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13884:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents have shown remarkable capabilities in autonomous decision-making by generating sequential trajectories of states, actions, and observations.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this, we propose Experience Memory Graph (EMG), a framework that reformulates agent failure recovery as a graph matching problem.

**证据证明什么。** Experiments on ALFWorld and ScienceWorld show that EMG consistently outperforms state-of-the-art reflection baselines in success rate and average reward, while requiring no test-time trial-and-error.

**证据没有证明什么。** For future work, we plan to extend EMG to environments without expert trajectories. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13884v1#S4 — 4. Method; https://arxiv.org/html/2607.13884v1#A2 — Appendix B Algorithm of extracting common subgraph and graph edit path。Evaluation：https://arxiv.org/html/2607.13884v1#S5 — 5. Experiments; https://arxiv.org/html/2607.13884v1#S5.SS1 — 5.1. Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.13884v1#A3 — Appendix C Discussion about the robustness of graph edit path; https://arxiv.org/html/2607.13884v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：For future work, we plan to extend EMG to environments without expert trajectories.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13884:end -->

<!-- review:SF-2026-ARXIV-2607-13920:start -->
### DeepStress: Stress-Testing Deep Search Agents

<!-- claim:SF-2026-ARXIV-2607-13920:start -->While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored. This phenomenon occurs rarely in realistic benchmarks but can lead to dramatic failure in real life applications. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13920:end -->

**为什么进入候选分母。** 摘要首要问题为“While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Therefore in this study we propose DeepStress, a stress testing framework that controls the frequency of challenging evidence by replacing the retrieval module of search agents with a controlled synthetic environment.

**证据证明什么。** While search agents demonstrate impressive capabilities in multi-step question answering, their robustness to poor-quality evidence remains under-explored.

**证据没有证明什么。** This constitutes preliminary work towards process-based evaluation, that cannot be reported fully in the core paper but reveals interesting insights towards more qualitative evaluation of search agents, constituting promising future directions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13920v1#A2.SS1 — B.1 Design choices; https://arxiv.org/html/2607.13920v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.13920v1#A1.SS1 — A.1 Human evaluation; https://arxiv.org/html/2607.13920v1#A3 — Appendix C Additional qualitative experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13920v1#S5.SS3 — 5.3 Discussion and future directions; https://arxiv.org/html/2607.13920v1#A2 — Appendix B Aggregate metrics discussion。

**Artifact boundary。** Exact v1 links https://github.com/OpenSourcesGroup/opensources, https://huggingface.co/google/gemma-4-31B-it, https://github.com/PeterGriffinJin/Search-R1/blob/main/infer.py; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This constitutes preliminary work towards process-based evaluation, that cannot be reported fully in the core paper but reveals interesting insights towards more qualitative evaluation of search agents, constituting promising future directions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13920:end -->

<!-- review:SF-2026-ARXIV-2607-13921:start -->
### Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code

<!-- claim:SF-2026-ARXIV-2607-13921:start -->Languages with rich static semantics, such as Rust, provide stronger guarantees for AI-generated code, but their strictness makes generation more difficult. Off-the-shelf compilers can provide useful feedback post-generation, but does not guide intermediate generation steps, such as those during autoregressive LLM decoding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13921:end -->

**为什么进入候选分母。** 摘要首要问题为“Languages with rich static semantics, such as Rust, provide stronger guarantees for AI-generated code, but their strictness makes generation more difficult.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce generative compilation, the first approach to obtaining compiler feedback on partial programs during generation.

**证据证明什么。** We show that generative compilation reduces non-compiling outputs and improves functional correctness, relative to standard post-generation feedback.

**证据没有证明什么。** Lifetimes 𝑙, 𝑚 annotate every lexical block {𝑙 𝑡} . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.13921v1#page=7 — PDF page 7; https://arxiv.org/pdf/2607.13921v1#page=12 — PDF page 12。Evaluation：https://arxiv.org/pdf/2607.13921v1#page=20 — PDF page 20; https://arxiv.org/pdf/2607.13921v1#page=25 — PDF page 25。Limitations / counterevidence：https://arxiv.org/pdf/2607.13921v1#page=31 — PDF page 31; https://arxiv.org/pdf/2607.13921v1#page=37 — PDF page 37。

**Artifact boundary。** Exact v1 links https://openrouter.ai/openai/gpt-5.3-codex, https://huggingface.co/moonshotai/Kimi-K2.7-Code, https://deploymentsafety.openai.com/gpt-5-3-codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Lifetimes 𝑙, 𝑚 annotate every lexical block {𝑙 𝑡} .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13921:end -->

<!-- review:SF-2026-ARXIV-2607-13926:start -->
### S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving

<!-- claim:SF-2026-ARXIV-2607-13926:start -->Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions. This limitation is rooted in a semantic-physical gap caused by the inherent mismatch between discrete language tokens and continuous trajectory planning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13926:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language Models (VLMs) have demonstrated remarkable potential for high-level reasoning in autonomous driving, yet they fundamentally struggle to generate precise, low-level control actions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** By mitigating the spatial representation collapse of traditional VLMs, our framework significantly outperforms baselines, achieving the highest No Collision (NC) rate of 98.4 among all evaluated methods.

**证据证明什么。** Evaluations on the NAVSIM closed-loop benchmark show that S-squared-VLA achieves a Predictive Driver Model Score (PDMS) of 87.1, establishing a new state-of-the-art for VLA models under a purely supervised fine-tuning (SFT) setting.

**证据没有证明什么。** Despite its effectiveness, our framework has two limitations, each suggesting a natural direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13926v1#S2 — II Method; https://arxiv.org/html/2607.13926v1#S3.SS2 — III-B Implementation Details。Evaluation：https://arxiv.org/html/2607.13926v1#S3 — III Experiments; https://arxiv.org/html/2607.13926v1#S4 — IV Results。Limitations / counterevidence：https://arxiv.org/html/2607.13926v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Despite its effectiveness, our framework has two limitations, each suggesting a natural direction for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13926:end -->

<!-- review:SF-2026-ARXIV-2607-13987:start -->
### Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation

<!-- claim:SF-2026-ARXIV-2607-13987:start -->Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications. However, existing security research primarily focuses on prompt injection and runtime execution, leaving security risks throughout the broader skill lifecycle largely unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13987:end -->

**为什么进入候选分母。** 摘要首要问题为“Reusable skills are becoming a fundamental building block of Large Language Model (LLM) agents, enabling capabilities to be packaged, shared, and reused across diverse applications.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we present SkillSec-Eval, a lifecycle-aware framework for systematically evaluating the security of reusable agent skills.

**证据证明什么。** Our study demonstrates that vulnerabilities arise at multiple lifecycle stages beyond execution, highlighting the need for lifecycle-aware security analysis of reusable agent skills.

**证据没有证明什么。** 3.3 Threat Model We consider an adversary whose objective is to manipulate an agent into executing unintended behavior by exploiting the skill ecosystem rather than the underlying language model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13987v1#S2.SS3 — 2.3 Secure Skill and Tool Ecosystems; https://arxiv.org/html/2607.13987v1#S4 — 4 SkillSec-Eval Framework。Evaluation：https://arxiv.org/html/2607.13987v1#S5 — 5 Experimental Setup; https://arxiv.org/html/2607.13987v1#S5.SS3 — 5.3 Experimental Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.13987v1#S3 — 3 Agent Skill Lifecycle and Threat Model; https://arxiv.org/html/2607.13987v1#S3.SS3 — 3.3 Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/openai/openai-agents, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：3.3 Threat Model We consider an adversary whose objective is to manipulate an agent into executing unintended behavior by exploiting the skill ecosystem rather than the underlying language model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13987:end -->

<!-- review:SF-2026-ARXIV-2607-13988:start -->
### TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents

<!-- claim:SF-2026-ARXIV-2607-13988:start -->Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training. Outcome rewards provide reliable supervision for short-horizon reasoning, but become sparse and high-variance as trajectories grow to tens or hundreds of tool calls. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13988:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-turn agents solve complex tasks through extended sequences of tool interactions before producing a final answer, making credit assignment a fundamental challenge during post-training.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning.

**证据证明什么。** The learned search behavior also transfers to open-web benchmarks, and the learning curves show earlier improvement and faster convergence during RL training.

**证据没有证明什么。** This limitation does not affect the main claim that turn-level credit can reduce the sparsity of outcome-only agentic RL, but it does bound the current scope of the method. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13988v1#S1 — 1 Introduction; https://arxiv.org/html/2607.13988v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.13988v1#A1.SS5 — A.5 Qualitative Analysis of the Turn Credit; https://arxiv.org/html/2607.13988v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.13988v1#S6 — 6 Limitations; https://arxiv.org/html/2607.13988v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This limitation does not affect the main claim that turn-level credit can reduce the sparsity of outcome-only agentic RL, but it does bound the current scope of the method.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13988:end -->

<!-- review:SF-2026-ARXIV-2607-14004:start -->
### Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0

<!-- claim:SF-2026-ARXIV-2607-14004:start -->Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14004:end -->

**为什么进入候选分母。** 摘要首要问题为“Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** All three methods improve over the baseline agent in the conventional, static, single-phase setting.

**证据证明什么。** All three methods improve over the baseline agent in the conventional, static, single-phase setting.

**证据没有证明什么。** 7 Limitations and Toward Realistic Continual-Learning Benchmarks The evaluation in this paper is a step toward more realistic continual-learning benchmarks for agents, not a complete one. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14004v1#A3 — Appendix C Method-Specific Diffs and Failure Cases; https://arxiv.org/html/2607.14004v1#S4 — 4 Methods Compared。Evaluation：https://arxiv.org/html/2607.14004v1#S2.SS3 — 2.3 Benchmark Overfitting and the Static-Benchmark Critique; https://arxiv.org/html/2607.14004v1#S2.SS4 — 2.4 Terminal-Bench as an Evaluation Substrate。Limitations / counterevidence：https://arxiv.org/html/2607.14004v1#A3 — Appendix C Method-Specific Diffs and Failure Cases; https://arxiv.org/html/2607.14004v1#S7 — 7 Limitations and Toward Realistic Continual-Learning Benchmarks。

**Artifact boundary。** Exact v1 links https://github.com/relai-ai/Continual-Learning-Terminal-Bench, https://www.anthropic.com/claude-code, https://github.com/context-labs/halo; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations and Toward Realistic Continual-Learning Benchmarks The evaluation in this paper is a step toward more realistic continual-learning benchmarks for agents, not a complete one.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14004:end -->

<!-- review:SF-2026-ARXIV-2607-14005:start -->
### M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming

<!-- claim:SF-2026-ARXIV-2607-14005:start -->Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. We present M$^\text{4}$World, a Multi-view and Multimodal generative driving world model that synthesizes future surround-view video streams and synchronized LiDAR scans while supporting interactive object Manipulation and stable Minute-long streaming. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14005:end -->

**为什么进入候选分母。** 摘要首要问题为“Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability.

**证据证明什么。** Together with downstream long-tail augmentation and scene editing, these results demonstrate the potential of M$^\text{4}$World for controllable, scalable driving simulation.

**证据没有证明什么。** More broadly, M World suggests a path toward simulation systems in which rare events are specified not only by where objects appear, but also by what they look like and how they persist across views, modalities, and time. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14005v1#S3.SS2 — 3.2 Model Architecture of M World; https://arxiv.org/html/2607.14005v1#S2.SS1 — 2.1 World Models for Driving Simulation。Evaluation：https://arxiv.org/html/2607.14005v1#S9 — 9 Experiments and Results; https://arxiv.org/html/2607.14005v1#S8 — 8 Controllability Evaluation Using a VLM Judge。Limitations / counterevidence：https://arxiv.org/html/2607.14005v1#S10 — 10 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：More broadly, M World suggests a path toward simulation systems in which rare events are specified not only by where objects appear, but also by what they look like and how they persist across views, modalities, and time.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14005:end -->

<!-- review:SF-2026-ARXIV-2607-14047:start -->
### Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment

<!-- claim:SF-2026-ARXIV-2607-14047:start -->Autonomous data collection governs the volume and quality of real-world trajectories for manipulation policy learning. Existing pipelines reduce human effort via self-resetting, VLM verification, or language-guided correction, yet episode-scoped fixes must be reissued whenever the same failure recurs, so oversight cost grows with session length rather than with the number of distinct problems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14047:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous data collection governs the volume and quality of real-world trajectories for manipulation policy learning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present Zero2Skill, a human-robot symbiotic agentic system in which corrections are retained and reused across rounds.

**证据证明什么。** Language corrections improve verifier-human agreement in all four evaluated settings and raise average single-attempt success from 12.5% to 47.5% (arm-selection: 20.0% to 50.0%).

**证据没有证明什么。** Tuning additional hyperparameters and broader task coverage are left to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14047v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.14047v1#A2 — Appendix B Training and Evaluation Protocols; https://arxiv.org/html/2607.14047v1#A2.SS4 — B.4 Deployment Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.14047v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/openclaw/openclaw, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Tuning additional hyperparameters and broader task coverage are left to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14047:end -->

<!-- review:SF-2026-ARXIV-2607-14076:start -->
### From Pixels to States: Rethinking Interactive World Models as Game Engines

<!-- claim:SF-2026-ARXIV-2607-14076:start -->Building interactive worlds that respond coherently to player actions has long been a shared goal of computer graphics, games, and artificial intelligence. Recent video generative models provide a data-driven route toward this goal by predicting future observations conditioned on user actions, and are increasingly regarded as potential next-generation game engines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-14076:end -->

**为什么进入候选分母。** 摘要首要问题为“Building interactive worlds that respond coherently to player actions has long been a shared goal of computer graphics, games, and artificial intelligence.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Complementing this analysis, we present a scalable data engine for Black Myth: Wukong that collects over 90 hours of gameplay with frame-aligned player actions, ground-truth game states, and visual observations, together with structured and semantic annotations, as a resource for state-aware game world modeling.

**证据证明什么。** We hope this paper offers a clear picture of where the field stands and fosters progress toward interactive game worlds.

**证据没有证明什么。** We further presented a scalable data engine for Black Myth: Wukong , contributing over 90 hours of gameplay with frame-aligned actions, engine-exported states, and visual observations to ease the data scarcity that limits state-aware approaches. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.14076v1#S2.SS1 — 2.1 Video Generation Models; https://arxiv.org/html/2607.14076v1#S2.SS2 — 2.2 Interactive Game World Models。Evaluation：https://arxiv.org/html/2607.14076v1#S1 — 1 Introduction; https://arxiv.org/html/2607.14076v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.14076v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We further presented a scalable data engine for Black Myth: Wukong , contributing over 90 hours of gameplay with frame-aligned actions, engine-exported states, and visual observations to ease the data scarcity that limits state-aware approaches.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-14076:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-13037 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13037 |
| SF-2026-ARXIV-2607-13062 | score_7_9 | selected | DA-20260716-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260716-01 |
| SF-2026-ARXIV-2607-13068 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13068 |
| SF-2026-ARXIV-2607-13071 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13071 |
| SF-2026-ARXIV-2607-13093 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13093 |
| SF-2026-ARXIV-2607-13095 | score_7_9 | selected | DA-20260716-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260716-02 |
| SF-2026-ARXIV-2607-13124 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13124 |
| SF-2026-ARXIV-2607-13184 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13184 |
| SF-2026-ARXIV-2607-13205 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13205 |
| SF-2026-ARXIV-2607-13285 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13285 |
| SF-2026-ARXIV-2607-13389 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13389 |
| SF-2026-ARXIV-2607-13399 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13399 |
| SF-2026-ARXIV-2607-13410 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13410 |
| SF-2026-ARXIV-2607-13429 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13429 |
| SF-2026-ARXIV-2607-13511 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13511 |
| SF-2026-ARXIV-2607-13591 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13591 |
| SF-2026-ARXIV-2607-13649 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13649 |
| SF-2026-ARXIV-2607-13705 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13705 |
| SF-2026-ARXIV-2607-13716 | score_7_9 | selected | DA-20260716-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260716-03 |
| SF-2026-ARXIV-2607-13921 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13921 |
| SF-2026-ARXIV-2607-13926 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13926 |
| SF-2026-ARXIV-2607-13988 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13988 |
| SF-2026-ARXIV-2607-14005 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-14005 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-13037:start -->
`SF-2026-ARXIV-2607-13037` 的 exact-v1 Deep Review 已保留。其机制为：We present ob, a record- and token-level data provenance system that propagates author identity through data processing pipelines and resolves revocation requests into precise forget sets via deterministic queries. 为避免挤压 `TRAIN-DATA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13068:start -->
`SF-2026-ARXIV-2607-13068` 的 exact-v1 Deep Review 已保留。其机制为：In contrast, large language model decoding requires little compute and a large amount of memory: a GPU's floating-point units run at single-digit-percent utilization during decoding, and the memory the workload does need is sold only bundled with yet more compute. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13068:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13071:start -->
`SF-2026-ARXIV-2607-13071` 的 exact-v1 Deep Review 已保留。其机制为：This paper documents a failure mode in Claude Code where partial standard output from timed-out commands (exit code 143) is recorded in compaction summaries as confirmed results, propagating false positives across sessions and model versions without re-verification. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13071:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13093:start -->
`SF-2026-ARXIV-2607-13093` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents a privacy-centric edge-cloud collaborative LLM inference framework built on endpoint-authenticated KV cache. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13093:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13124:start -->
`SF-2026-ARXIV-2607-13124` 的 exact-v1 Deep Review 已保留。其机制为：To mitigate this waste, we propose \textbf{\shortopd}, a short-to-long OPD schedule that detects teacher-confirmed repetitive suffixes, treats the surviving prefix as each rollout's effective length, and allocates future rollout budgets to the effective lengths the policy can currently use. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13124:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13184:start -->
`SF-2026-ARXIV-2607-13184` 的 exact-v1 Deep Review 已保留。其机制为：This paper introduces Microflow, an observability framework elevating causality to a first-class analytical object. 为避免挤压 `PLATFORM-TRACE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13184:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13205:start -->
`SF-2026-ARXIV-2607-13205` 的 exact-v1 Deep Review 已保留。其机制为：On schema-dense input streams such as nested JSON, this score acts as a non-stationary filter that disproportionately retains noise: a non-content sink role (delimiters or whitespace) carries an order of magnitude more energy than any content role, and structural KEY tokens are over-retained at roughly 1.8x the rate of the answer-carrying VALUE tokens, collapsing exact-match accuracy from 88% to 0% at a 5% budget as the signal-to-noise ratio of the retained state degrades. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13205:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13285:start -->
`SF-2026-ARXIV-2607-13285` 的 exact-v1 Deep Review 已保留。其机制为：Evolving complex agentic systems thus depends not only on generating edits, but also on determining where those edits should be made. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13285:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13389:start -->
`SF-2026-ARXIV-2607-13389` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a FLOP-accounting framework for GRPO post-training that decomposes compute into rollout/search, policy-update/learning, and reward- or feedback-model evaluation. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13389:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13399:start -->
`SF-2026-ARXIV-2607-13399` 的 exact-v1 Deep Review 已保留。其机制为：We present a systematic study examining the role, pathologies, and regulations of OPD. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13410:start -->
`SF-2026-ARXIV-2607-13410` 的 exact-v1 Deep Review 已保留。其机制为：This work proposes DynaDreamer, a dynamics-augmented Dreamer-style reinforcement learning method to address this problem by augmenting the WM with an explicit ego-dynamics prior. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13410:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13429:start -->
`SF-2026-ARXIV-2607-13429` 的 exact-v1 Deep Review 已保留。其机制为：We propose Anchor-Align, which augments BC with two objectives: Vision-Language Anchoring distills layer-wise representations from a frozen VLM copy to prevent this drift, while Language-Action Alignment converts each action target into a discrete motion-direction label and jointly trains language and action prediction on the same robot observation. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13429:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13511:start -->
`SF-2026-ARXIV-2607-13511` 的 exact-v1 Deep Review 已保留。其机制为：We introduce ExTernD (Expanded-rank Ternary Decomposition), a post-training factorization of each LLM weight matrix $A \in \mathbb{R}^{m \times n}$ into $A \approx B \mathrm{diag}(D) C$ with ternary factors $B \in \{-1,0,+1\}^{m \times k}$, $C \in \{-1,0,+1\}^{k \times n}$ and a real scale vector $D \in \mathbb{R}^k$. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13511:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13591:start -->
`SF-2026-ARXIV-2607-13591` 的 exact-v1 Deep Review 已保留。其机制为：We present Memory as a Controlled Process (MemCon), a framework that models memory operations as a Markov Decision Process and learns an online policy that adaptively decides when, what, and how much to retrieve, when to inject a distilled plan, and when to consolidate or forget. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13591:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13649:start -->
`SF-2026-ARXIV-2607-13649` 的 exact-v1 Deep Review 已保留。其机制为：Weight precision plays a critical role in balancing inference accuracy, throughput, and energy consumption, while modern LLM workloads exhibit pronounced heterogeneity and tolerance that favors adaptive precision execution. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13649:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13705:start -->
`SF-2026-ARXIV-2607-13705` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we introduce AgentCompass, an open-source, lightweight, and extensible infrastructure for evaluating LLM-based agents. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13705:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13921:start -->
`SF-2026-ARXIV-2607-13921` 的 exact-v1 Deep Review 已保留。其机制为：We introduce generative compilation, the first approach to obtaining compiler feedback on partial programs during generation. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13921:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13926:start -->
`SF-2026-ARXIV-2607-13926` 的 exact-v1 Deep Review 已保留。其机制为：By mitigating the spatial representation collapse of traditional VLMs, our framework significantly outperforms baselines, achieving the highest No Collision (NC) rate of 98.4 among all evaluated methods. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13926:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13988:start -->
`SF-2026-ARXIV-2607-13988` 的 exact-v1 Deep Review 已保留。其机制为：We propose TRACE (Turn-level Reward Assignment via Credit Estimation), a dense credit-assignment method for agentic reinforcement learning. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13988:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-14005:start -->
`SF-2026-ARXIV-2607-14005` 的 exact-v1 Deep Review 已保留。其机制为：Driving-world generation has emerged as a core capability for scalable autonomous-driving simulation, yet existing methods remain limited in object-level controllability and long-horizon stability. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-14005:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260716-01:start -->
### The verifier side of speculative window decoding: a predictability bracket, a machine-checked blast-radius bound, and a decoder-agnostic recover loop

**约束变化与机制。** SWIPER and ARTERY each build one predictor, about 90% accurate; neither built the verifier side.

**证明与未证明。** A predictor-only bracket shows the cross-boundary decision is local, the achievable accuracy reaching about 0.999 within three rounds, with small, diffuse headroom over SWIPER. 但 8 Limitations and future work The matching-weight bound. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：8 Limitations and future work The matching-weight bound. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-13062`。
<!-- analysis:DA-20260716-01:end -->

<!-- analysis:DA-20260716-02:start -->
### Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit

**约束变化与机制。** Together, these optimizations constitute the first large-scale LLM serving system in production that efficiently covers the Hybrid SWA + MoE + multimodal composite architecture.

**证明与未证明。** While Hybrid SWA can ideally reduce both attention compute and KVCache storage significantly compared to Full Attention, realizing these gains in production requires substantial engineering effort. 但 Additionally, SWA’s reduced bandwidth transfer overhead, while not directly affecting TTL, significantly lowers cross-tier data movement costs, ensuring stable and efficient operation of the entire caching system. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Additionally, SWA’s reduced bandwidth transfer overhead, while not directly affecting TTL, significantly lowers cross-tier data movement costs, ensuring stable and efficient operation of the entire caching system. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-13095`。
<!-- analysis:DA-20260716-02:end -->

<!-- analysis:DA-20260716-03:start -->
### CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems

**约束变化与机制。** The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance.

**证明与未证明。** The contribution is a systems formulation of action-level canonicalization and policy-addressable semantic patterns as a necessary substrate for deployer-side AI governance. 但 Attestation failure Signature, credential, or ledger anchor cannot verify. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Attestation failure Signature, credential, or ledger anchor cannot verify. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-13716`。
<!-- analysis:DA-20260716-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260716-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260716 | GAP-20260716-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260716-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260716-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260716-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260716-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260716-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260716-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

384 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：50
- `incremental_method_without_durable_system_delta`：273
- `local_benchmark_without_release_delta`：10
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：12
- `vertical_application_without_system_delta`：38

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 16、No Change 45、Structural 1；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/16/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [OriginBlame: Record- and Token-Level Data Provenance for AI Training Datasets](https://arxiv.org/html/2607.13037v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Uncertainty-Aware Sequential Decision Rules for Event-Triggered LLM Invocation in Streaming Systems](https://arxiv.org/html/2607.13048v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [The verifier side of speculative window decoding: a predictability bracket, a machine-checked blast-radius bound, and a decoder-agnostic recover loop](https://arxiv.org/html/2607.13062v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [The Economics of AI Decoding Chips: Rebalancing Compute, Capacity, and Bandwidth for Efficient LLM Inference](https://arxiv.org/html/2607.13068v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Compaction as Epistemic Failure: How Agentic LLM Tools Fabricate Confirmed Results from Killed Processes](https://arxiv.org/html/2607.13071v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [The Entanglement Wall: Activation-Space Probes as Risk Detectors, Not Context Adjudicators](https://arxiv.org/html/2607.13075v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows](https://arxiv.org/html/2607.13078v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Phantom Guardrails: When Self-Improving Agent Harnesses Fix Failures That Never Happened](https://arxiv.org/html/2607.13083v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Baselines Before Architecture: Evaluating Coding Agents for Autonomous Penetration Testing](https://arxiv.org/html/2607.13085v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules: A Closed-Loop Framework](https://arxiv.org/html/2607.13091v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](https://arxiv.org/html/2607.13093v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/html/2607.13095v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation](https://arxiv.org/html/2607.13124v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](https://arxiv.org/html/2607.13157v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Learning Safe Agent Behaviour from Human Preferences and Justifications via World Models](https://arxiv.org/html/2607.13172v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Microflow: Microarchitectural Causal Observability for Deep Cross-Layer Analysis and Optimization](https://arxiv.org/html/2607.13184v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference](https://arxiv.org/html/2607.13205v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Networked Intelligence: Active Shared Context Graphs for Human-AI Team Science](https://arxiv.org/html/2607.13220v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Audited Selective Verification for Risk-Controlled N-1 Thermal Contingency Screening under Deployment Shift](https://arxiv.org/html/2607.13221v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and Editable](https://arxiv.org/html/2607.13285v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [FOLIO: Focused Semantic Memory for Streaming Video Understanding](https://arxiv.org/html/2607.13298v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Accuracy Without Grounding: Diagnosing Visual Dependency Dissociation in Video LLM Benchmarks](https://arxiv.org/html/2607.13305v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Agora: Collective and Permissionless Internet-Scale Pretraining of Large Language Models](https://arxiv.org/html/2607.13332v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Learning Latency-Aware Orchestration for Multi-Agent Systems](https://arxiv.org/html/2607.13359v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Where Should RL Post-Training Compute Go? Model Size, Search, Learning, and Feedback](https://arxiv.org/html/2607.13389v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Set-shifting Behavioral Test for Harnessed Agents](https://arxiv.org/html/2607.13396v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/html/2607.13399v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Ego-Dynamics-Augmented World Model for Autonomous Driving with Zero-Shot Cross-Chassis Adaptation](https://arxiv.org/html/2607.13410v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Evaluating Frontier AI Agents as Autonomous Clinical Security Auditors](https://arxiv.org/html/2607.13411v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Can We Steer the Black-Box? Towards Controllability-Centric Evaluation of Recommender Systems with Collaborative Agents](https://arxiv.org/html/2607.13418v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment](https://arxiv.org/html/2607.13429v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [ReBound: Reuse-Aware Privacy For Interactive Decision Support](https://arxiv.org/html/2607.13441v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [DevicesWorld: Benchmarking Cross-Device Agents in Heterogeneous Environments](https://arxiv.org/html/2607.13465v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [MyAG: A Graph-Based Framework for Designing and Analyzing Composable LLM Agent Systems](https://arxiv.org/html/2607.13474v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Auditing Protocol-Level Shortcuts in Large Audio Language Model Judges for Speech Evaluation](https://arxiv.org/html/2607.13477v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ with Accuracy Approaching Any Quantization Level](https://arxiv.org/html/2607.13511v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/html/2607.13527v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [When T2I Synthetic Data Backfires: Amplified Privacy Risks in Real-Synthetic Mix Training](https://arxiv.org/html/2607.13541v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Memory as a Controlled Process: Learned Adaptive Memory Management for LLM Agents](https://arxiv.org/html/2607.13591v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [SAFETY SENTRY: Context-Aware Human Intervention via EXECUTE-ASK-REFUSE Routing](https://arxiv.org/html/2607.13594v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](https://arxiv.org/html/2607.13596v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning](https://arxiv.org/html/2607.13605v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [STOCKTAKE: Measuring the Gap Between Perception and Action in LLM Agents with a Fair Oracle](https://arxiv.org/html/2607.13618v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [WarpGuard: Towards Control-Flow Attestation for Heterogeneous CPU-GPU Execution](https://arxiv.org/html/2607.13640v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [CIMERA: Compute-in-Interconnect and Memory with Reconfigurable Precision for LLM Inference](https://arxiv.org/html/2607.13649v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring](https://arxiv.org/html/2607.13651v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [HarnessBank: Semantic Gene-Bank Search with Gated Verification for Agent-Harness Self-Evolution](https://arxiv.org/html/2607.13683v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/html/2607.13705v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [CAVA: Canonical Action Verification and Attestation for Runtime Governance of Agentic AI Systems](https://arxiv.org/html/2607.13716v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement](https://arxiv.org/html/2607.13718v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Post-Training Shifts Confidence: A Three-Stage Analysis of How SFT, RL, and OPD Shape CoT Calibration](https://arxiv.org/html/2607.13753v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [SPyCE: Skill-Policy Co-evolution for Multimodal Agents](https://arxiv.org/html/2607.13854v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Experience Memory Graph: One-Shot Error Correction for Agents](https://arxiv.org/html/2607.13884v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [DeepStress: Stress-Testing Deep Search Agents](https://arxiv.org/html/2607.13920v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code](https://arxiv.org/pdf/2607.13921v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [S-squared-VLA: Decoupling Semantic and Spatial Streams in Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/html/2607.13926v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Agent Skill Security: Threat Models, Attacks, Defenses, and Evaluation](https://arxiv.org/html/2607.13987v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [TRACE: Turn-level Reward Assignment via Credit Estimation for Long-Horizon Agents](https://arxiv.org/html/2607.13988v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](https://arxiv.org/html/2607.14004v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [M$^\text{4}$World: A Multi-view Multimodal Driving World Model for Interactive Object Manipulation and Minute-long Streaming](https://arxiv.org/html/2607.14005v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/html/2607.14047v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04
- [From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/html/2607.14076v1) — first-public（Asia/Shanghai）：2026-07-16；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、62/62 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
