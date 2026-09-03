# Daily Research — 2026-07-15

**Research Date:** 2026-07-15

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-14 09:00:00 ～ 2026-07-15 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **482** 个 identity；全量 title + abstract 筛选后冻结 **55** 个候选与 **427** 个 family-specific closure，retain rate **11.41%**。exact-v1 Review 为 55/55：Deep 17、Standard 38、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-15 |
| Window End | 2026-07-15 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-15-0900-v2.1-sha256:bb643eedb7e93a63cf7108236a395716497a1238cf2714210bbae7f51d71ab73 |
| Denominator Frozen At | 2026-09-04T04:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260715:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-14T09:00:00+08:00 | 2026-07-15T09:00:00+08:00 | 2026-09-04T04:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 482 | SF-2026-ARXIV-2607-11897;SF-2026-ARXIV-2607-11942;SF-2026-ARXIV-2607-11944;SF-2026-ARXIV-2607-11945;SF-2026-ARXIV-2607-11953;SF-2026-ARXIV-2607-11969;SF-2026-ARXIV-2607-11976;SF-2026-ARXIV-2607-12056;SF-2026-ARXIV-2607-12068;SF-2026-ARXIV-2607-12085;SF-2026-ARXIV-2607-12104;SF-2026-ARXIV-2607-12121;SF-2026-ARXIV-2607-12188;SF-2026-ARXIV-2607-12200;SF-2026-ARXIV-2607-12211;SF-2026-ARXIV-2607-12227;SF-2026-ARXIV-2607-12231;SF-2026-ARXIV-2607-12273;SF-2026-ARXIV-2607-12278;SF-2026-ARXIV-2607-12287;SF-2026-ARXIV-2607-12356;SF-2026-ARXIV-2607-12385;SF-2026-ARXIV-2607-12395;SF-2026-ARXIV-2607-12406;SF-2026-ARXIV-2607-12463;SF-2026-ARXIV-2607-12505;SF-2026-ARXIV-2607-12550;SF-2026-ARXIV-2607-12571;SF-2026-ARXIV-2607-12592;SF-2026-ARXIV-2607-12614;SF-2026-ARXIV-2607-12625;SF-2026-ARXIV-2607-12650;SF-2026-ARXIV-2607-12659;SF-2026-ARXIV-2607-12696;SF-2026-ARXIV-2607-12747;SF-2026-ARXIV-2607-12767;SF-2026-ARXIV-2607-12790;SF-2026-ARXIV-2607-12831;SF-2026-ARXIV-2607-12835;SF-2026-ARXIV-2607-12839;SF-2026-ARXIV-2607-12875;SF-2026-ARXIV-2607-12885;SF-2026-ARXIV-2607-12893;SF-2026-ARXIV-2607-12894;SF-2026-ARXIV-2607-12911;SF-2026-ARXIV-2607-12931;SF-2026-ARXIV-2607-12962;SF-2026-ARXIV-2607-12963;SF-2026-ARXIV-2607-12986;SF-2026-ARXIV-2607-12992;SF-2026-ARXIV-2607-13013;SF-2026-ARXIV-2607-13017;SF-2026-ARXIV-2607-13027;SF-2026-ARXIV-2607-13028;SF-2026-ARXIV-2607-13034 | all registered category pages; cross-category dedup complete | 2026-07-15T09:00:00+08:00 | sha256:bb643eedb7e93a63cf7108236a395716497a1238cf2714210bbae7f51d71ab73 | — |
<!-- coverage:SRC-ARXIV:20260715:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-11897 | arXiv:2607.11897v1 | paper-v1:2607.11897 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11897 | self | — | new_in_window | MODEL-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11942 | arXiv:2607.11942v1 | paper-v1:2607.11942 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11942 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11944 | arXiv:2607.11944v1 | paper-v1:2607.11944 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11944 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11945 | arXiv:2607.11945v1 | paper-v1:2607.11945 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11945 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11953 | arXiv:2607.11953v1 | paper-v1:2607.11953 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11953 | self | — | new_in_window | TRAIN-REWARD-MODEL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11969 | arXiv:2607.11969v1 | paper-v1:2607.11969 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11969 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11976 | arXiv:2607.11976v1 | paper-v1:2607.11976 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11976 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12056 | arXiv:2607.12056v1 | paper-v1:2607.12056 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12056 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12068 | arXiv:2607.12068v1 | paper-v1:2607.12068 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12068 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12085 | arXiv:2607.12085v1 | paper-v1:2607.12085 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12085 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12104 | arXiv:2607.12104v1 | paper-v1:2607.12104 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12104 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12121 | arXiv:2607.12121v1 | paper-v1:2607.12121 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12121 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12188 | arXiv:2607.12188v1 | paper-v1:2607.12188 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12188 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12200 | arXiv:2607.12200v1 | paper-v1:2607.12200 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12200 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12211 | arXiv:2607.12211v1 | paper-v1:2607.12211 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12211 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12227 | arXiv:2607.12227v1 | paper-v1:2607.12227 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12227 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12231 | arXiv:2607.12231v1 | paper-v1:2607.12231 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12231 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12273 | arXiv:2607.12273v1 | paper-v1:2607.12273 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12273 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12278 | arXiv:2607.12278v1 | paper-v1:2607.12278 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12278 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12287 | arXiv:2607.12287v1 | paper-v1:2607.12287 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12287 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12356 | arXiv:2607.12356v1 | paper-v1:2607.12356 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12356 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12385 | arXiv:2607.12385v1 | paper-v1:2607.12385 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12385 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12395 | arXiv:2607.12395v1 | paper-v1:2607.12395 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12395 | self | — | new_in_window | TRAIN-REINFORCEMENT-LEARNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12406 | arXiv:2607.12406v1 | paper-v1:2607.12406 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12406 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12463 | arXiv:2607.12463v1 | paper-v1:2607.12463 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12463 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12505 | arXiv:2607.12505v1 | paper-v1:2607.12505 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12505 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12550 | arXiv:2607.12550v1 | paper-v1:2607.12550 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12550 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12571 | arXiv:2607.12571v1 | paper-v1:2607.12571 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12571 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12592 | arXiv:2607.12592v1 | paper-v1:2607.12592 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12592 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12614 | arXiv:2607.12614v1 | paper-v1:2607.12614 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12614 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12625 | arXiv:2607.12625v1 | paper-v1:2607.12625 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12625 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12650 | arXiv:2607.12650v1 | paper-v1:2607.12650 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12650 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12659 | arXiv:2607.12659v1 | paper-v1:2607.12659 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12659 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12696 | arXiv:2607.12696v1 | paper-v1:2607.12696 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12696 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12747 | arXiv:2607.12747v1 | paper-v1:2607.12747 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12747 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12767 | arXiv:2607.12767v1 | paper-v1:2607.12767 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12767 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12790 | arXiv:2607.12790v1 | paper-v1:2607.12790 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12790 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12831 | arXiv:2607.12831v1 | paper-v1:2607.12831 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12831 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12835 | arXiv:2607.12835v1 | paper-v1:2607.12835 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12835 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12839 | arXiv:2607.12839v1 | paper-v1:2607.12839 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12839 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12875 | arXiv:2607.12875v1 | paper-v1:2607.12875 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12875 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12885 | arXiv:2607.12885v1 | paper-v1:2607.12885 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12885 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12893 | arXiv:2607.12893v1 | paper-v1:2607.12893 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12893 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12894 | arXiv:2607.12894v1 | paper-v1:2607.12894 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12894 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12911 | arXiv:2607.12911v1 | paper-v1:2607.12911 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12911 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12931 | arXiv:2607.12931v1 | paper-v1:2607.12931 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12931 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12962 | arXiv:2607.12962v1 | paper-v1:2607.12962 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12962 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12963 | arXiv:2607.12963v1 | paper-v1:2607.12963 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12963 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12986 | arXiv:2607.12986v1 | paper-v1:2607.12986 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12986 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-12992 | arXiv:2607.12992v1 | paper-v1:2607.12992 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12992 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13013 | arXiv:2607.13013v1 | paper-v1:2607.13013 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13013 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13017 | arXiv:2607.13017v1 | paper-v1:2607.13017 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13017 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13027 | arXiv:2607.13027v1 | paper-v1:2607.13027 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13027 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13028 | arXiv:2607.13028v1 | paper-v1:2607.13028 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13028 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-13034 | arXiv:2607.13034v1 | paper-v1:2607.13034 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13034 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-11897 | RP-1797a5c387d7b9a9 | standard | arXiv:2607.11897v1 | SRC-ARXIV@arXiv:2607.11897v1 | https://arxiv.org/html/2607.11897v1#A4.SS2 — D.2 Finite automata as one-hot linear systems; https://arxiv.org/html/2607.11897v1#A7.SS3 — G.3 Why register memories are genuinely tied-SFDA, not only generalized-template systems | https://arxiv.org/html/2607.11897v1#A5 — Appendix E Experiment Protocol; https://arxiv.org/html/2607.11897v1#A5.SS3 — E.3 Kernel benchmarks | https://arxiv.org/html/2607.11897v1#S10 — 10 Limitations and Open Problems | Exact v1 links https://github.com/fla-org/flash-linear-attention, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11897 | complete |
| SF-2026-ARXIV-2607-11942 | RP-57767fa88720cafa | deep | arXiv:2607.11942v1 | SRC-ARXIV@arXiv:2607.11942v1 | https://arxiv.org/html/2607.11942v1#S3.SS1 — 3.1 Design principle: one variable; https://arxiv.org/html/2607.11942v1#S3.SS3 — 3.3 Benchmarks, models, protocols | https://arxiv.org/html/2607.11942v1#A2 — Appendix B Per-axis results, query-aware arm; https://arxiv.org/html/2607.11942v1#S3.SS3 — 3.3 Benchmarks, models, protocols | https://arxiv.org/html/2607.11942v1#S7 — 7 Limitations; https://arxiv.org/html/2607.11942v1#S8 — 8 Conclusion | Exact v1 links https://github.com/NVIDIA/kvpress, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11942 | complete |
| SF-2026-ARXIV-2607-11944 | RP-b04e0334414b45b4 | standard | arXiv:2607.11944v1 | SRC-ARXIV@arXiv:2607.11944v1 | https://arxiv.org/html/2607.11944v1#S4 — 4 Mage : Framework Design; https://arxiv.org/html/2607.11944v1#S4.SS4 — 4.4 Algorithm | https://arxiv.org/html/2607.11944v1#S5.SS3 — 5.3 Ablation Analysis; https://arxiv.org/html/2607.11944v1#S5 — 5 Experiments | https://arxiv.org/html/2607.11944v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.11944v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11944 | complete |
| SF-2026-ARXIV-2607-11945 | RP-65af445d8a4e4f18 | standard | arXiv:2607.11945v1 | SRC-ARXIV@arXiv:2607.11945v1 | https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-11945 | complete |
| SF-2026-ARXIV-2607-11953 | RP-7309aa2d314bddb6 | standard | arXiv:2607.11953v1 | SRC-ARXIV@arXiv:2607.11953v1 | https://arxiv.org/html/2607.11953v1#S5.SS1 — 5.1 The oracle selects diagnostic tasks; the interface, not just architecture, governs capacity; https://arxiv.org/html/2607.11953v1#Sx2 — Use of large language models | https://arxiv.org/html/2607.11953v1#S5 — 5 Experiments | https://arxiv.org/html/2607.11953v1#S6 — 6 Discussion, Limitations, and Conclusion; https://arxiv.org/html/2607.11953v1#S3a — C Behavioral diagnostics cannot localize the failure | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11953 | complete |
| SF-2026-ARXIV-2607-11969 | RP-cca9c3977b7be933 | standard | arXiv:2607.11969v1 | SRC-ARXIV@arXiv:2607.11969v1 | https://arxiv.org/html/2607.11969v1#S3 — 3 Method: an adversarial metric stress-test | https://arxiv.org/html/2607.11969v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.11969v1#S5 — 5 Results | https://arxiv.org/html/2607.11969v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11969v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11969 | complete |
| SF-2026-ARXIV-2607-11976 | RP-d7dde941ab3a332c | deep | arXiv:2607.11976v1 | SRC-ARXIV@arXiv:2607.11976v1 | https://arxiv.org/html/2607.11976v1#S3.SS2 — 3.2 Method | https://arxiv.org/html/2607.11976v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.11976v1#S4 — 4 Experiments | https://arxiv.org/html/2607.11976v1#S5 — 5 Conclusion and Discussion | Exact v1 links https://github.com/vllm-project/vllm/pull/36178, https://github.com/Heisenberg-Yin/LiteTopK, https://github.com/deepseek-ai/DeepGEMM; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11976 | complete |
| SF-2026-ARXIV-2607-12056 | RP-7111a9d8096ba83a | standard | arXiv:2607.12056v1 | SRC-ARXIV@arXiv:2607.12056v1 | https://arxiv.org/html/2607.12056v1#S2.SS3 — 2.3 Limitations of Existing Web Design; https://arxiv.org/html/2607.12056v1#S3 — 3 Research Problem and Approach | https://arxiv.org/html/2607.12056v1#S5.SS3 — 5.3 Evaluation Scoring and Analysis; https://arxiv.org/html/2607.12056v1#S6 — 6 Results and Analysis | https://arxiv.org/html/2607.12056v1#S2.SS2 — 2.2 Failure Modes of Web Agents; https://arxiv.org/html/2607.12056v1#S2.SS3 — 2.3 Limitations of Existing Web Design | Exact v1 links https://github.com/rashidiff/AIAgentReadWebSites, https://github.com/browser-use/browser-use, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12056 | complete |
| SF-2026-ARXIV-2607-12068 | RP-54c9d3dcbf1e30eb | standard | arXiv:2607.12068v1 | SRC-ARXIV@arXiv:2607.12068v1 | https://arxiv.org/html/2607.12068v1#S2 — II Study Design; https://arxiv.org/html/2607.12068v1#S6.SS1 — VI-A Environmental Modeling and Sandboxed Execution | https://arxiv.org/html/2607.12068v1#S3 — III Experimental Results; https://arxiv.org/html/2607.12068v1#S2.SS1 — II-A “White-Boxing” the Analysis Pipelines | https://arxiv.org/html/2607.12068v1#S4.SS1 — IV-A Threats to Conclusion Validity; https://arxiv.org/html/2607.12068v1#S4 — IV Threats To Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12068 | complete |
| SF-2026-ARXIV-2607-12085 | RP-01126019f0c8cd8b | standard | arXiv:2607.12085v1 | SRC-ARXIV@arXiv:2607.12085v1 | https://arxiv.org/html/2607.12085v1#S4.SS1 — 4.1 Pipeline Architecture and Design; https://arxiv.org/html/2607.12085v1#S4 — 4 Methodology | https://arxiv.org/html/2607.12085v1#S5 — 5 Results, Evaluation, and Reliability; https://arxiv.org/html/2607.12085v1#S5.SS4 — 5.4 Model Benchmarking and Comparative Evaluation | https://arxiv.org/html/2607.12085v1#S8 — 8 Conclusion and Future Work; https://arxiv.org/html/2607.12085v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12085 | complete |
| SF-2026-ARXIV-2607-12104 | RP-592429acfbfb96f6 | standard | arXiv:2607.12104v1 | SRC-ARXIV@arXiv:2607.12104v1 | https://arxiv.org/html/2607.12104v1#S3 — 3. Approach; https://arxiv.org/html/2607.12104v1#S3.SS2 — 3.2. Diffusion Model Architecture | https://arxiv.org/html/2607.12104v1#S4 — 4. Evaluation Setup; https://arxiv.org/html/2607.12104v1#S4.SS4 — 4.4. Downstream Task Evaluation | https://arxiv.org/html/2607.12104v1#S6.SS5 — 6.5. Limitations and Threats to Validity; https://arxiv.org/html/2607.12104v1#S7 — 7. Conclusion and Future Work | Exact v1 links https://github.com/17YuvrajSehgal/SyntheticLogGeneration, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12104 | complete |
| SF-2026-ARXIV-2607-12121 | RP-da11f90bd7ab67a6 | deep | arXiv:2607.12121v1 | SRC-ARXIV@arXiv:2607.12121v1 | https://arxiv.org/html/2607.12121v1#S4 — 4. FlashDiff Design; https://arxiv.org/html/2607.12121v1#S6.SS1 — 6.1. Methodology | https://arxiv.org/html/2607.12121v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.12121v1#A1.SS6 — A.6. Second-Order Analysis: Stale KV-Cache Effects | https://arxiv.org/html/2607.12121v1#S8 — 8. Conclusion | Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/NVIDIA/TensorRT, https://github.com/NVIDIA/TensorRT-LLM; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12121 | complete |
| SF-2026-ARXIV-2607-12188 | RP-6d292eb631e1d184 | deep | arXiv:2607.12188v1 | SRC-ARXIV@arXiv:2607.12188v1 | https://arxiv.org/html/2607.12188v1#S3 — III Architecture; https://arxiv.org/html/2607.12188v1#S4.SS5 — IV-E Comparison Against Alternative Index Architectures | https://arxiv.org/html/2607.12188v1#S4 — IV Evaluation; https://arxiv.org/html/2607.12188v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.12188v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.12188v1#S5 — V Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12188 | complete |
| SF-2026-ARXIV-2607-12200 | RP-e3e9939b27a67438 | standard | arXiv:2607.12200v1 | SRC-ARXIV@arXiv:2607.12200v1 | https://arxiv.org/html/2607.12200v1#A2 — Appendix B Our TEC’s comparison against industrial safety frameworks; https://arxiv.org/html/2607.12200v1#S3 — 3 Methodology | https://arxiv.org/html/2607.12200v1#A6 — Appendix F Reliability Thresholds and Results; https://arxiv.org/html/2607.12200v1#S4 — 4 Experimental Study | https://arxiv.org/html/2607.12200v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12200 | complete |
| SF-2026-ARXIV-2607-12211 | RP-6a88f24379518ba3 | standard | arXiv:2607.12211v1 | SRC-ARXIV@arXiv:2607.12211v1 | https://arxiv.org/html/2607.12211v1#S3 — III System Design; https://arxiv.org/html/2607.12211v1#S2 — II Design Motivation | https://arxiv.org/html/2607.12211v1#S4 — IV Evaluation | https://arxiv.org/html/2607.12211v1#S4.SS4 — IV-D Limitations; https://arxiv.org/html/2607.12211v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12211 | complete |
| SF-2026-ARXIV-2607-12227 | RP-99e8ba3c52c8caaf | deep | arXiv:2607.12227v1 | SRC-ARXIV@arXiv:2607.12227v1 | https://arxiv.org/html/2607.12227v1#S1 — 1 Introduction; https://arxiv.org/html/2607.12227v1#S2 — 2 Related Work | https://arxiv.org/html/2607.12227v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.12227v1#A1.SS5 — A.5 Evaluation Metrics | https://arxiv.org/html/2607.12227v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12227v1#S6 — 6 Conclusions | Exact v1 links https://github.com/rethinking-harness-evolution, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12227 | complete |
| SF-2026-ARXIV-2607-12231 | RP-3f3b5351df71548a | standard | arXiv:2607.12231v1 | SRC-ARXIV@arXiv:2607.12231v1 | https://arxiv.org/html/2607.12231v1#S10.SS1 — 10.1 The Staged Approach and Its Failure; https://arxiv.org/html/2607.12231v1#S10.SS2 — 10.2 Architecture Overview | https://arxiv.org/html/2607.12231v1#S1 — 1 Related Work; https://arxiv.org/html/2607.12231v1#S2 — 2 Overview and Evolution | https://arxiv.org/html/2607.12231v1#S10.SS1 — 10.1 The Staged Approach and Its Failure | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12231 | complete |
| SF-2026-ARXIV-2607-12273 | RP-e004730892c88cfb | standard | arXiv:2607.12273v1 | SRC-ARXIV@arXiv:2607.12273v1 | https://arxiv.org/html/2607.12273v1#S4 — 4. Method | https://arxiv.org/html/2607.12273v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.12273v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.12273v1#S6 — 6. Discussion; https://arxiv.org/html/2607.12273v1#S7 — 7. Threats to Validity | Exact v1 links https://github.com/hnurxn/Code-Uncertainty, https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12273 | complete |
| SF-2026-ARXIV-2607-12278 | RP-b2e98bf10c4dde9d | standard | arXiv:2607.12278v1 | SRC-ARXIV@arXiv:2607.12278v1 | https://arxiv.org/html/2607.12278v1#S2.SS1 — 2.1 WSI Multimodal Benchmarks and Models | https://arxiv.org/html/2607.12278v1#S2.SS1 — 2.1 WSI Multimodal Benchmarks and Models; https://arxiv.org/html/2607.12278v1#S4 — 4 Experiments | https://arxiv.org/html/2607.12278v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12278v1#S5.SS3 — 5.3 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12278 | complete |
| SF-2026-ARXIV-2607-12287 | RP-e797dab1d0186acc | deep | arXiv:2607.12287v1 | SRC-ARXIV@arXiv:2607.12287v1 | https://arxiv.org/html/2607.12287v1#S3 — III Methodology; https://arxiv.org/html/2607.12287v1#S4.SS4 — IV-D System Level Ablation | https://arxiv.org/html/2607.12287v1#A3 — Appendix C Full RoboTwin Benchmark Results.; https://arxiv.org/html/2607.12287v1#A2 — Appendix B Efficiency Analysis | https://arxiv.org/html/2607.12287v1#S5 — V Conclusion, Limitations and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12287 | complete |
| SF-2026-ARXIV-2607-12356 | RP-c95d5c7c812d469e | standard | arXiv:2607.12356v1 | SRC-ARXIV@arXiv:2607.12356v1 | https://arxiv.org/html/2607.12356v1#S3 — 3 Methods | https://arxiv.org/html/2607.12356v1#S4 — 4 Experiments; https://arxiv.org/html/2607.12356v1#S4.SS1 — 4.1 Real-World Experiments | https://arxiv.org/html/2607.12356v1#S5 — 5 Conclusion, Limitation, and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12356 | complete |
| SF-2026-ARXIV-2607-12385 | RP-c8165b8ec2e19248 | standard | arXiv:2607.12385v1 | SRC-ARXIV@arXiv:2607.12385v1 | https://arxiv.org/html/2607.12385v1#S3.SS1 — 3.1 Scenario Design; https://arxiv.org/html/2607.12385v1#S4.SS2 — 4.2 No Universal Best Scaffold Across Models and Metrics | https://arxiv.org/html/2607.12385v1#A1 — Appendix A Additional Benchmark Details and Results; https://arxiv.org/html/2607.12385v1#A1.SS6 — A.6 Additional Results and Failure Analysis | https://arxiv.org/html/2607.12385v1#A1.SS6 — A.6 Additional Results and Failure Analysis; https://arxiv.org/html/2607.12385v1#S5 — 5 Conclusion | Exact v1 links https://github.com/genglinliu/PMBench.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12385 | complete |
| SF-2026-ARXIV-2607-12395 | RP-82dba52278616f1f | standard | arXiv:2607.12395v1 | SRC-ARXIV@arXiv:2607.12395v1 | https://arxiv.org/html/2607.12395v1#S3 — 3 Methodology; https://arxiv.org/html/2607.12395v1#S5.SS5 — 5.5 How Does Native RL-based CoT Compare to Distillation-based Approaches at Scale? | https://arxiv.org/html/2607.12395v1#A2 — Appendix B LLM-as-a-Judge Evaluation Prompts; https://arxiv.org/html/2607.12395v1#S2 — 2 Evaluation Metrics for Chain-of-Thought Quality | https://arxiv.org/html/2607.12395v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12395v1#S8 — 8 Conclusion | Exact v1 links https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12395 | complete |
| SF-2026-ARXIV-2607-12406 | RP-5d834f8aa2b843b0 | standard | arXiv:2607.12406v1 | SRC-ARXIV@arXiv:2607.12406v1 | https://arxiv.org/html/2607.12406v1#S4.SS3 — 4.3 Embodied Agents and Vision-Language-Action Systems; https://arxiv.org/html/2607.12406v1#S6 — 6 System-Environment Boundary | https://arxiv.org/html/2607.12406v1#S2.SS4 — 2.4 Defenses, Evaluation, and Future Directions | https://arxiv.org/html/2607.12406v1#S2.SS1 — 2.1 Threat Model and Boundary Definition; https://arxiv.org/html/2607.12406v1#S2.SS4 — 2.4 Defenses, Evaluation, and Future Directions | Exact v1 links https://www.anthropic.com/engineering/claude-code-best-practices, https://openai.com/index/introducing-codex/, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12406 | complete |
| SF-2026-ARXIV-2607-12463 | RP-d26ac4a896ab4e15 | standard | arXiv:2607.12463v1 | SRC-ARXIV@arXiv:2607.12463v1 | https://arxiv.org/html/2607.12463v1#S2 — 2 Method; https://arxiv.org/html/2607.12463v1#A2 — Appendix B Algorithmic Details | https://arxiv.org/html/2607.12463v1#S3.SS2 — 3.2 Main Results on SWE Agent Benchmarks; https://arxiv.org/html/2607.12463v1#A4 — Appendix D Extended Behavioral Analysis (SWE-Bench-Verified) | https://arxiv.org/html/2607.12463v1#S6 — 6 Limitations and Discussion; https://arxiv.org/html/2607.12463v1#A4.SS4 — D.4 Failure-Mode Breakdown | Exact v1 links https://github.com/TIGER-AI-Lab/FIM-Midtraining, https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12463 | complete |
| SF-2026-ARXIV-2607-12505 | RP-f07f161f14267dd7 | deep | arXiv:2607.12505v1 | SRC-ARXIV@arXiv:2607.12505v1 | https://arxiv.org/html/2607.12505v1#S4.SS1 — 4.1 Design Methodology; https://arxiv.org/html/2607.12505v1#S3 — 3 Problem Formulation and Method Overview | https://arxiv.org/html/2607.12505v1#S6 — 6 Experiments; https://arxiv.org/html/2607.12505v1#S6.SS1 — 6.1 MD-SpMM Kernel Evaluation | https://arxiv.org/html/2607.12505v1#S7 — 7 Conclusion | Exact v1 links https://github.com/liuganhuo/realizable-nm-sparse-transformer, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12505 | complete |
| SF-2026-ARXIV-2607-12550 | RP-8607e3945cca5aad | deep | arXiv:2607.12550v1 | SRC-ARXIV@arXiv:2607.12550v1 | https://arxiv.org/html/2607.12550v1#S4 — 4 Method: Joint Tucker and JL Allocation (JoLT) | https://arxiv.org/html/2607.12550v1#A7 — Appendix G Full ablation grids; https://arxiv.org/html/2607.12550v1#S6 — 6 Experiments | https://arxiv.org/html/2607.12550v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12550 | complete |
| SF-2026-ARXIV-2607-12571 | RP-14b5792991b047f0 | deep | arXiv:2607.12571v1 | SRC-ARXIV@arXiv:2607.12571v1 | https://arxiv.org/html/2607.12571v1#S3 — 3 Proposed Method; https://arxiv.org/html/2607.12571v1#A2 — Appendix B Implementation and Calibration Details | https://arxiv.org/html/2607.12571v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.12571v1#A3 — Appendix C Ablation Protocol and Oracle Upper Bound | https://arxiv.org/html/2607.12571v1#A1.SS1 — A.1 Mechanistic Interpretation and Adaptive Threats; https://arxiv.org/html/2607.12571v1#A7 — Appendix G Failure-Mode Accounting | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12571 | complete |
| SF-2026-ARXIV-2607-12592 | RP-82eb55122b1175d8 | standard | arXiv:2607.12592v1 | SRC-ARXIV@arXiv:2607.12592v1 | https://arxiv.org/html/2607.12592v1#S3 — 3 Method; https://arxiv.org/html/2607.12592v1#S3.SS2 — 3.2 Model Design | https://arxiv.org/html/2607.12592v1#S4 — 4 Results; https://arxiv.org/html/2607.12592v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.12592v1#S5 — 5 Limitations; https://arxiv.org/html/2607.12592v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12592 | complete |
| SF-2026-ARXIV-2607-12614 | RP-e8232f9cc431438d | standard | arXiv:2607.12614v1 | SRC-ARXIV@arXiv:2607.12614v1 | https://arxiv.org/html/2607.12614v1#S1 — I Introduction; https://arxiv.org/html/2607.12614v1#S1.SS1 — I-A Pipelines as OS Objects | https://arxiv.org/html/2607.12614v1#S7 — VII Evaluation; https://arxiv.org/html/2607.12614v1#S7.SS1 — VII-A Experimental Setup | https://arxiv.org/html/2607.12614v1#S8 — VIII Discussion; https://arxiv.org/html/2607.12614v1#S8.SS2 — VIII-B Limitations | Exact v1 links https://github.com/Dimitrios-Kafetzis/SynapticOS, https://zephyrproject.org, https://github.com/ARM-software/CMSIS-NN; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12614 | complete |
| SF-2026-ARXIV-2607-12625 | RP-86920f5703c97c80 | standard | arXiv:2607.12625v1 | SRC-ARXIV@arXiv:2607.12625v1 | https://arxiv.org/html/2607.12625v1#S3.SS2 — 3.2 Host-Centric Multi-Agent Systems | https://arxiv.org/html/2607.12625v1#S5.SS3 — 5.3 Ablation and Efficiency Analysis; https://arxiv.org/html/2607.12625v1#S5 — 5 Experiments | https://arxiv.org/html/2607.12625v1#S6 — 6 Conclusion | Exact v1 links https://github.com/HITsz-TMG/KnowAct, https://github.com/HITsz-TMG/KnowAct/releases/tag/Result, https://github.com/HKUDS/nanobot; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12625 | complete |
| SF-2026-ARXIV-2607-12650 | RP-225f1465402cf824 | deep | arXiv:2607.12650v1 | SRC-ARXIV@arXiv:2607.12650v1 | https://arxiv.org/html/2607.12650v1#A9 — Appendix I Failure cases and formalizer-design notes | https://arxiv.org/html/2607.12650v1#A5 — Appendix E Tier 1.5 per-claim data, ablations, and pre-registration; https://arxiv.org/html/2607.12650v1#A5.SS3 — E.3 Authority-cue ablation: no-cue pilot vs authority-cued pilot per-claim | https://arxiv.org/html/2607.12650v1#A13 — Appendix M Scope limits and future extensions; https://arxiv.org/html/2607.12650v1#A13.SS1 — M.1 Limitations | Exact v1 links https://github.com/7pocheR/eg-var, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12650 | complete |
| SF-2026-ARXIV-2607-12659 | RP-50cdc8c8cb00020e | deep | arXiv:2607.12659v1 | SRC-ARXIV@arXiv:2607.12659v1 | https://arxiv.org/html/2607.12659v1#S4.SS3 — 4.3 System Design; https://arxiv.org/html/2607.12659v1#A1 — Appendix A Model Architecture of series Models | https://arxiv.org/html/2607.12659v1#S5 — 5 Experiments; https://arxiv.org/html/2607.12659v1#S5.SS1 — 5.1 Simulation Experiments | https://arxiv.org/html/2607.12659v1#A2 — Appendix B Architecture of Future Correction Module; https://arxiv.org/html/2607.12659v1#S6 — 6 Conclusion | Exact v1 links https://github.com/PKU-SEC-Lab/Jetson-PI, https://github.com/PKU-SEC-Lab/Jetson-PI-Edge, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12659 | complete |
| SF-2026-ARXIV-2607-12696 | RP-0f5ab05bb2aee84a | deep | arXiv:2607.12696v1 | SRC-ARXIV@arXiv:2607.12696v1 | https://arxiv.org/html/2607.12696v1#S4 — 4 Methodology: EcoSpec; https://arxiv.org/html/2607.12696v1#A6 — Appendix F Model Details | https://arxiv.org/html/2607.12696v1#A2 — Appendix B Predictor Details and Analysis; https://arxiv.org/html/2607.12696v1#A2.SS3 — B.3 Oracle Expert-Set Analysis | https://arxiv.org/html/2607.12696v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/lmsys/Qwen3-235B-A22B-EAGLE3, https://huggingface.co/lmsys/EAGLE3-gpt-oss-120b-bf16, https://huggingface.co/datasets/AI-MO/aimo-validation-amc; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12696 | complete |
| SF-2026-ARXIV-2607-12747 | RP-ac9b8b7f3d7866ca | deep | arXiv:2607.12747v1 | SRC-ARXIV@arXiv:2607.12747v1 | https://arxiv.org/html/2607.12747v1#S4 — 4 Methodology; https://arxiv.org/html/2607.12747v1#A6 — Appendix F Additional Implementation Details & Hyperparameters | https://arxiv.org/html/2607.12747v1#A7 — Appendix G Additional Experimental Results; https://arxiv.org/html/2607.12747v1#S5 — 5 Experiments | https://arxiv.org/html/2607.12747v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.12747v1#A5 — Appendix E Annotation of Failure Contributing Steps | Exact v1 links https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct, https://huggingface.co/blog/gemma4, https://neurips.cc/public/guides/CodeSubmissionPolicy; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12747 | complete |
| SF-2026-ARXIV-2607-12767 | RP-96906a3fd5082f7c | standard | arXiv:2607.12767v1 | SRC-ARXIV@arXiv:2607.12767v1 | https://arxiv.org/html/2607.12767v1#A1.SS3 — A.3 Algorithm; https://arxiv.org/html/2607.12767v1#S3.SS2 — 3.2 Benchmarks and Models | https://arxiv.org/html/2607.12767v1#A1.SS4 — A.4 Benchmark Details; https://arxiv.org/html/2607.12767v1#A1.SS5 — A.5 Benchmark Prompt Examples | https://arxiv.org/html/2607.12767v1#S5 — 5 Conclusion | Exact v1 links https://github.com/Aleph-Alpha-Research/eval-framework, https://github.com/huggingface/lighteval, https://huggingface.co/datasets/LeoLM/ArcChallenge_de; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12767 | complete |
| SF-2026-ARXIV-2607-12790 | RP-bbfb6c0d94abef57 | standard | arXiv:2607.12790v1 | SRC-ARXIV@arXiv:2607.12790v1 | https://arxiv.org/html/2607.12790v1#Sx1 — Introduction; https://arxiv.org/html/2607.12790v1#Sx2 — Related Work | https://arxiv.org/html/2607.12790v1#A7 — Appendix G Appendix G: Negative and Supporting Results; https://arxiv.org/html/2607.12790v1#Sx3.SSx4 — Two Ablations: Anchor Guards versus Lifecycle | https://arxiv.org/html/2607.12790v1#Sx6 — Discussion and Limitations; https://arxiv.org/html/2607.12790v1#Sx7 — Conclusion | Exact v1 links https://developers.openai.com/codex/record-and-replay, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12790 | complete |
| SF-2026-ARXIV-2607-12831 | RP-c47dc5891e91f498 | standard | arXiv:2607.12831v1 | SRC-ARXIV@arXiv:2607.12831v1 | https://arxiv.org/html/2607.12831v1#A14 — Appendix N Implementation Details; https://arxiv.org/html/2607.12831v1#S2 — 2 Knowledgeless Language Modelling | https://arxiv.org/html/2607.12831v1#A10 — Appendix J Data Efficiency Analysis; https://arxiv.org/html/2607.12831v1#A12 — Appendix L Representation-Level Analysis | https://arxiv.org/html/2607.12831v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.12831v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/flair/ner-english-ontonotes-large, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12831 | complete |
| SF-2026-ARXIV-2607-12835 | RP-a5097c5cba645a23 | standard | arXiv:2607.12835v1 | SRC-ARXIV@arXiv:2607.12835v1 | https://arxiv.org/html/2607.12835v1#S3 — 3 Methodology | https://arxiv.org/html/2607.12835v1#S4.SS1 — 4.1 Extrinsic Meta-Evaluation Results; https://arxiv.org/html/2607.12835v1#S4.SS2 — 4.2 Intrinsic Meta-Evaluation Results | https://arxiv.org/html/2607.12835v1#A4 — Appendix D Threshold Discussion; https://arxiv.org/html/2607.12835v1#S6 — 6 Conclusion | Exact v1 links https://code.claude.com/docs, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12835 | complete |
| SF-2026-ARXIV-2607-12839 | RP-947a3a3970e3b8f0 | deep | arXiv:2607.12839v1 | SRC-ARXIV@arXiv:2607.12839v1 | https://arxiv.org/html/2607.12839v1#S6.SS5 — 6.5. Comparison with Other Frameworks; https://arxiv.org/html/2607.12839v1#S3.SS1 — 3.1. Sparse and Model-Restructured Inference. | https://arxiv.org/html/2607.12839v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.12839v1#S6.SS1 — 6.1. Microbenchmarks | https://arxiv.org/html/2607.12839v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.12839v1#S8 — 8. Conclusion | Exact v1 links https://rocm.docs.amd.com/projects/HIP/en/develop/doxygen/html/group___event.html#ga5df2309c9f29ca4c8e669db658d411b4, https://rocm.docs.amd.com/projects/HIP/en/docs-develop/reference/hip_runtime_api/modules/stream_memory_operations.html, https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12839 | complete |
| SF-2026-ARXIV-2607-12875 | RP-bd51822467a7a9f5 | deep | arXiv:2607.12875v1 | SRC-ARXIV@arXiv:2607.12875v1 | https://arxiv.org/html/2607.12875v1#A1 — Appendix A Implementation Details of the MetaInfer Method; https://arxiv.org/html/2607.12875v1#S3 — 3 Method | https://arxiv.org/html/2607.12875v1#S4.SS1 — 4.1 Experimental setup and evaluation metrics; https://arxiv.org/html/2607.12875v1#A2 — Appendix B Historical Platform Results | https://arxiv.org/html/2607.12875v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12875v1#S5.SS3 — 5.3 Limitations and risks of the evolution strategy | Exact v1 links https://github.com/MetaInfer/MetaInfer, https://github.com/OpenBMB/ForgeTrain, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12875 | complete |
| SF-2026-ARXIV-2607-12885 | RP-045049aa51371bec | standard | arXiv:2607.12885v1 | SRC-ARXIV@arXiv:2607.12885v1 | https://arxiv.org/html/2607.12885v1#S3 — 3 Methodology | https://arxiv.org/html/2607.12885v1#A1.SS2 — A.2 Calibration Experiment Results; https://arxiv.org/html/2607.12885v1#A1.SS3 — A.3 Sensitivity Experiments | https://arxiv.org/html/2607.12885v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.12885v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/datasets/copenlu/answerable_tydiqa, https://huggingface.co/datasets/TeluguLLMResearch/MATA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12885 | complete |
| SF-2026-ARXIV-2607-12893 | RP-d703cc048e535cd5 | standard | arXiv:2607.12893v1 | SRC-ARXIV@arXiv:2607.12893v1 | https://arxiv.org/html/2607.12893v1#S2.SS2 — 2.2 Memory-Enhanced LLM Systems | https://arxiv.org/html/2607.12893v1#S2.SS1 — 2.1 Long-Term Conversation Benchmarks; https://arxiv.org/html/2607.12893v1#S3.SS2 — 3.2 Benchmark Construction | https://arxiv.org/html/2607.12893v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://github.com/MemTensor/MemOps, https://github.com/%7BQ%7Dwen%7BL%7D%7BM%7D/%7BQ%7Dwen3.6, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12893 | complete |
| SF-2026-ARXIV-2607-12894 | RP-15dcda421a1f1b27 | standard | arXiv:2607.12894v1 | SRC-ARXIV@arXiv:2607.12894v1 | https://arxiv.org/html/2607.12894v1#S3 — 3 Model Architecture | https://arxiv.org/html/2607.12894v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.12894v1#S6 — 6 Conclusion | Exact v1 links https://github.com/Tencent-Hunyuan/HY-Embodied, https://huggingface.co/tencent/Hy-Embodied-VLM-1.0, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12894 | complete |
| SF-2026-ARXIV-2607-12911 | RP-928caed6a5561663 | standard | arXiv:2607.12911v1 | SRC-ARXIV@arXiv:2607.12911v1 | https://arxiv.org/html/2607.12911v1#S3 — 3 Method: Open-KNEAD; https://arxiv.org/html/2607.12911v1#S3.SS1 — 3.1 Problem setting and design constraints | https://arxiv.org/html/2607.12911v1#A1.SS4 — A.4 Full main results (all backbones); https://arxiv.org/html/2607.12911v1#S4 — 4 Results | https://arxiv.org/html/2607.12911v1#A1.SS10 — A.10 Failure modes; https://arxiv.org/html/2607.12911v1#A1.SS9 — A.9 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12911 | complete |
| SF-2026-ARXIV-2607-12931 | RP-afe252b9960f0273 | deep | arXiv:2607.12931v1 | SRC-ARXIV@arXiv:2607.12931v1 | https://arxiv.org/html/2607.12931v1#A1.SS1 — A.1 Reinforcement Fine-tuning for VLA models | https://arxiv.org/html/2607.12931v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.12931v1#A3 — Appendix C Experimental Details | https://arxiv.org/html/2607.12931v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://github.com/MINT-SJTU/Evo-RL, https://github.com/Physical-Intelligence/openpi, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12931 | complete |
| SF-2026-ARXIV-2607-12962 | RP-80050fb1031299f1 | standard | arXiv:2607.12962v1 | SRC-ARXIV@arXiv:2607.12962v1 | https://arxiv.org/html/2607.12962v1#S2 — 2 Methods | https://arxiv.org/html/2607.12962v1#S3 — 3 Results | https://arxiv.org/html/2607.12962v1#S4 — 4 Discussion; https://arxiv.org/html/2607.12962v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12962 | complete |
| SF-2026-ARXIV-2607-12963 | RP-03c5b6980969365a | standard | arXiv:2607.12963v1 | SRC-ARXIV@arXiv:2607.12963v1 | https://arxiv.org/html/2607.12963v1#A7 — Appendix G Details of Local Model Experiments; https://arxiv.org/html/2607.12963v1#S3.SS2 — 3.2 Model Specificity | https://arxiv.org/html/2607.12963v1#A2 — Appendix B Extra Experiment Details; https://arxiv.org/html/2607.12963v1#A3 — Appendix C Details of Qualitative Analysis | https://arxiv.org/html/2607.12963v1#S5 — 5 Conclusion | Exact v1 links https://github.com/SALT-NLP/illusion-of-robustness, https://github.com/gkamradt/LLMTest_NeedleInAHaystack, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12963 | complete |
| SF-2026-ARXIV-2607-12986 | RP-f6ef8941a22c7f56 | standard | arXiv:2607.12986v1 | SRC-ARXIV@arXiv:2607.12986v1 | https://arxiv.org/html/2607.12986v1#S2.SS3 — 2.3 Model-Mediated Typing | https://arxiv.org/html/2607.12986v1#S4 — 4 Experimental Program | https://arxiv.org/html/2607.12986v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.12986v1#S9 — 9 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12986 | complete |
| SF-2026-ARXIV-2607-12992 | RP-7c621f2d241205b8 | standard | arXiv:2607.12992v1 | SRC-ARXIV@arXiv:2607.12992v1 | https://arxiv.org/html/2607.12992v1#S3 — III Method | https://arxiv.org/html/2607.12992v1#S4 — IV Experiment; https://arxiv.org/html/2607.12992v1#S4.SS1 — IV-A Dataset and Evaluation Metric | https://arxiv.org/html/2607.12992v1#S5 — V CONCLUSIONS | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-12992 | complete |
| SF-2026-ARXIV-2607-13013 | RP-7a1328b4082fef7c | standard | arXiv:2607.13013v1 | SRC-ARXIV@arXiv:2607.13013v1 | https://arxiv.org/html/2607.13013v1#S3 — 3 Method; https://arxiv.org/html/2607.13013v1#S5.SS4 — 5.4 Comparison with diffusion and autoregressive systems | https://arxiv.org/html/2607.13013v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.13013v1#S5 — 5 Results | https://arxiv.org/html/2607.13013v1#S7 — 7 Limitations; https://arxiv.org/html/2607.13013v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13013 | complete |
| SF-2026-ARXIV-2607-13017 | RP-fe2c66b14d847337 | standard | arXiv:2607.13017v1 | SRC-ARXIV@arXiv:2607.13017v1 | https://arxiv.org/html/2607.13017v1#S3 — 3 Method; https://arxiv.org/html/2607.13017v1#A1 — Appendix A Implementation Details and Training Pipeline | https://arxiv.org/html/2607.13017v1#A3 — Appendix C Additional RoboTwin Results; https://arxiv.org/html/2607.13017v1#A4 — Appendix D WorldArena Evaluation Details | https://arxiv.org/html/2607.13017v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13017 | complete |
| SF-2026-ARXIV-2607-13027 | RP-dfc19167cfbf89bd | deep | arXiv:2607.13027v1 | SRC-ARXIV@arXiv:2607.13027v1 | https://arxiv.org/html/2607.13027v1#S3 — 3 Framework | https://arxiv.org/html/2607.13027v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.13027v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.13027v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ModalityDance/PalmClaw/releases/latest, https://github.com/openclaw/openclaw, https://developers.openai.com/codex/cli; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13027 | complete |
| SF-2026-ARXIV-2607-13028 | RP-365c456b7a43adf7 | standard | arXiv:2607.13028v1 | SRC-ARXIV@arXiv:2607.13028v1 | https://arxiv.org/html/2607.13028v1#S3.SS1 — 3.1. Designing for Performance | https://arxiv.org/html/2607.13028v1#S6 — 6. Experiments & Results; https://arxiv.org/html/2607.13028v1#S6.SS3 — 6.3. Planner Benchmarks | https://arxiv.org/html/2607.13028v1#S7 — 7. Conclusion | Exact v1 links https://github.com/Emerge-Lab/PufferDrive, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13028 | complete |
| SF-2026-ARXIV-2607-13034 | RP-3e52bbe2e35b9d1f | standard | arXiv:2607.13034v1 | SRC-ARXIV@arXiv:2607.13034v1 | https://arxiv.org/html/2607.13034v1#S4 — 4 The E3 Framework: Estimate, Execute, Expand; https://arxiv.org/html/2607.13034v1#S5.SS1 — 5.1 Design principle: capability-invariant evaluation | https://arxiv.org/html/2607.13034v1#S7 — 7 Results and Analysis; https://arxiv.org/html/2607.13034v1#S5.SS1 — 5.1 Design principle: capability-invariant evaluation | https://arxiv.org/html/2607.13034v1#S10 — 10 Conclusion and Future Work; https://arxiv.org/html/2607.13034v1#S9 — 9 Discussion | Exact v1 links https://github.com/eejyin/Do-AI-Agents-Know-When-a-Task-Is-Simple-Toward-Complexity-Aware-Reasoning-and-Execution, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-13034 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-11897:start -->
### Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels

<!-- claim:SF-2026-ARXIV-2607-11897:start -->Linear attention replaces softmax attention's growing KV cache with a fixed recurrent state, but this compression limits exact state tracking and long-context memory. We introduce \emph{Semidirect Fourier Delta Attention} (SFDA), a phase-controlled generalization of Kimi Delta Attention that replaces real diagonal decay with block-rotational Fourier control: \[ S_t=(I-β_t k_tk_t^*)Λ_tS_{t-1}+β_tk_tv_t^*, \qquad Λ_t=\diag(α_t\odot e^{iθ_t}). \] Our main result is a constructive chunk-WY factorization for products \(A_t=Λ_t-u_tr_t^*\), giving \[ A_t\cdots A_1=Γ_t-Y_tM_tW_t^* \] with rank growth bounded inside fixed chunks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11897:end -->

**为什么进入候选分母。** 摘要首要问题为“Linear attention replaces softmax attention's growing KV cache with a fixed recurrent state, but this compression limits exact state tracking and long-context memory.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce \emph{Semidirect Fourier Delta Attention} (SFDA), a phase-controlled generalization of Kimi Delta Attention that replaces real diagonal decay with block-rotational Fourier control: \[ S_t=(I-β_t k_tk_t^*)Λ_tS_{t-1}+β_tk_tv_t^*, \qquad Λ_t=\diag(α_t\odot e^{iθ_t}). \] Our main result is a constructive chunk-WY factorization for products \(A_t=Λ_t-u_tr_t^*\), giving \[ A_t\cdots A_1=Γ_t-Y_tM_tW_t^* \] with rank growth bounded inside fixed chunks.

**证据证明什么。** We verify the algebra numerically and show in toy state-tracking experiments that SFDA learns cyclic memory where the phase-disabled KDA baseline remains near chance.

**证据没有证明什么。** 10 Limitations and Open Problems This preprint deliberately avoids several overclaims. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11897v1#A4.SS2 — D.2 Finite automata as one-hot linear systems; https://arxiv.org/html/2607.11897v1#A7.SS3 — G.3 Why register memories are genuinely tied-SFDA, not only generalized-template systems。Evaluation：https://arxiv.org/html/2607.11897v1#A5 — Appendix E Experiment Protocol; https://arxiv.org/html/2607.11897v1#A5.SS3 — E.3 Kernel benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.11897v1#S10 — 10 Limitations and Open Problems。

**Artifact boundary。** Exact v1 links https://github.com/fla-org/flash-linear-attention, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：10 Limitations and Open Problems This preprint deliberately avoids several overclaims.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-ATTENTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11897:end -->

<!-- review:SF-2026-ARXIV-2607-11942:start -->
### How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit

<!-- claim:SF-2026-ARXIV-2607-11942:start -->KV-cache compression methods are predominantly evaluated with the query appended to the context before compression -- a query-aware protocol. Yet the economic case for a compressed KV cache is reuse: compress a document once, answer many future questions against it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11942:end -->

**为什么进入候选分母。** 摘要首要问题为“KV-cache compression methods are predominantly evaluated with the query appended to the context before compression -- a query-aware protocol.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a matched-budget audit of six published compression methods against three trivial baselines on three open 7-9B models (144,300 paired evaluations on RULER-8192; 40,800 on LongBench; 50,000-resample paired bootstrap throughout).

**证据证明什么。** Three findings. (1) Query visibility changes the rankings: under the agnostic protocol, of the five audited methods that share a common attention backend, only KeyDiff beats a best-of-3 trivial baseline consistently (31 of 36 cells), and the most widely deployed method, SnapKV, loses to "keep the start and the recent window" on average (-0.066). (2) The per-method drop between the two protocols is ordered consistently with how visible the question is to each method's scoring signal, legible in its source code: from Delta=+0.198 for SnapKV (the question sits inside its 64-token observation window) down to Delta=+0.011 for KeyDiff (its score contains no query term at all).

**证据没有证明什么。** The dependence does not look incidental: across the six audited methods its size is ordered by the question’s visibility in each scoring signal, legible in source code, and the one method with no query term is the one whose performance the protocol cannot touch—an ordering we advance as a mechanistic hypothesis awaiting direct manipulation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11942v1#S3.SS1 — 3.1 Design principle: one variable; https://arxiv.org/html/2607.11942v1#S3.SS3 — 3.3 Benchmarks, models, protocols。Evaluation：https://arxiv.org/html/2607.11942v1#A2 — Appendix B Per-axis results, query-aware arm; https://arxiv.org/html/2607.11942v1#S3.SS3 — 3.3 Benchmarks, models, protocols。Limitations / counterevidence：https://arxiv.org/html/2607.11942v1#S7 — 7 Limitations; https://arxiv.org/html/2607.11942v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/kvpress, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The dependence does not look incidental: across the six audited methods its size is ordered by the question’s visibility in each scoring signal, legible in source code, and the one method with no query term is the one whose performance the protocol cannot touch—an ordering we advance as a mechanistic hypothesis awaiting direct manipulation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11942:end -->

<!-- review:SF-2026-ARXIV-2607-11944:start -->
### MAGE: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization

<!-- claim:SF-2026-ARXIV-2607-11944:start -->How do different components of iterative prompt optimization interact, and what happens when they are combined? We investigate this through MAGE (Memory-Augmented Goal-directed Prompt Evolution), a controlled analysis framework for studying component interaction in prompt optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11944:end -->

**为什么进入候选分母。** 摘要首要问题为“How do different components of iterative prompt optimization interact, and what happens when they are combined?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** First, failure-grounded reflection is essential: methods relying only on scores (OPRO) or abstract critique (Self-Refine) fail to improve prompts.

**证据证明什么。** We further validate on Llama 3.1 8B and show POCE is headroom-dependent: when the base model already achieves high accuracy, variance amplification disappears.

**证据没有证明什么。** Multi-component optimizers are coupled stochastic systems; reporting only average performance obscures stability costs critical for real-world deployment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11944v1#S4 — 4 Mage : Framework Design; https://arxiv.org/html/2607.11944v1#S4.SS4 — 4.4 Algorithm。Evaluation：https://arxiv.org/html/2607.11944v1#S5.SS3 — 5.3 Ablation Analysis; https://arxiv.org/html/2607.11944v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11944v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.11944v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Multi-component optimizers are coupled stochastic systems; reporting only average performance obscures stability costs critical for real-world deployment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11944:end -->

<!-- review:SF-2026-ARXIV-2607-11945:start -->
### Belief-reality separation lives in routing over a shared value slot in language models

<!-- claim:SF-2026-ARXIV-2607-11945:start -->Capable language models hold what a character believes apart from what is true: told "Anna believes the cup is blue; in reality it is red," they answer blue about Anna and red about the world. Where in the computation does that separation live? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11945:end -->

**为什么进入候选分母。** 摘要首要问题为“Capable language models hold what a character believes apart from what is true: told "Anna believes the cup is blue; in reality it is red," they answer blue about Anna and red about the world.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Where in the computation does that separation live?

**证据证明什么。** We show it rests on two separable mechanisms at two positions.

**证据没有证明什么。** A subspace trained on either route steers the other, and only the derived route depends on described visibility. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.11945v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11945v1#page=10 — PDF page 10。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A subspace trained on either route steers the other, and only the derived route depends on described visibility.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11945:end -->

<!-- review:SF-2026-ARXIV-2607-11953:start -->
### When Does Reward Teach State? A Hidden-Automaton Instrument and a Group-Language Warning Signal

<!-- claim:SF-2026-ARXIV-2607-11953:start -->Does a reinforcement-learning agent that earns high reward actually learn its task's hidden state, or only a shortcut that correlates with reward? We build an instrument that makes this question directly measurable: the task is a hidden finite automaton that the agent partially controls. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11953:end -->

**为什么进入候选分母。** 摘要首要问题为“Does a reinforcement-learning agent that earns high reward actually learn its task's hidden state, or only a shortcut that correlates with reward?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We build an instrument that makes this question directly measurable: the task is a hidden finite automaton that the agent partially controls.

**证据证明什么。** High reward alone is not evidence that the task's state was learned.

**证据没有证明什么。** C Behavioral diagnostics cannot localize the failure Figure 2 substantiates the § 5.4 claim that an exact instrument sees what a behavior-only diagnostic cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11953v1#S5.SS1 — 5.1 The oracle selects diagnostic tasks; the interface, not just architecture, governs capacity; https://arxiv.org/html/2607.11953v1#Sx2 — Use of large language models。Evaluation：https://arxiv.org/html/2607.11953v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11953v1#S6 — 6 Discussion, Limitations, and Conclusion; https://arxiv.org/html/2607.11953v1#S3a — C Behavioral diagnostics cannot localize the failure。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：C Behavioral diagnostics cannot localize the failure Figure 2 substantiates the § 5.4 claim that an exact instrument sees what a behavior-only diagnostic cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-REWARD-MODEL`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11953:end -->

<!-- review:SF-2026-ARXIV-2607-11969:start -->
### Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection

<!-- claim:SF-2026-ARXIV-2607-11969:start -->Point-adjustment (PA), for years the default scoring protocol in time-series anomaly detection (TSAD), was shown by Kim et al. (2022) to award near-perfect F1 to random anomaly scores. The field adopted a suite of replacement metrics (PA%K, range-based precision/recall, affiliation precision/recall, and Volume-Under-the-Surface, VUS, ROC/PR). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11969:end -->

**为什么进入候选分母。** 摘要首要问题为“Point-adjustment (PA), for years the default scoring protocol in time-series anomaly detection (TSAD), was shown by Kim et al.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The field adopted a suite of replacement metrics (PA%K, range-based precision/recall, affiliation precision/recall, and Volume-Under-the-Surface, VUS, ROC/PR).

**证据证明什么。** Point-adjustment (PA), for years the default scoring protocol in time-series anomaly detection (TSAD), was shown by Kim et al. (2022) to award near-perfect F1 to random anomaly scores.

**证据没有证明什么。** The no-skill statistic is a max over generators × 10 replicates (an extreme order statistic), so the ROC rates are mildly replicate-dependent; the gamed-SOTA=1.0 diagnostic shows this does not explain them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11969v1#S3 — 3 Method: an adversarial metric stress-test。Evaluation：https://arxiv.org/html/2607.11969v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.11969v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.11969v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11969v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The no-skill statistic is a max over generators × 10 replicates (an extreme order statistic), so the ROC rates are mildly replicate-dependent; the gamed-SOTA=1.0 diagnostic shows this does not explain them.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11969:end -->

<!-- review:SF-2026-ARXIV-2607-11976:start -->
### LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-11976:start -->Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention algorithms in large language models and vector retrieval in recommendation systems and vector databases. However, existing GPU-based Indexer-TopK kernels like DeepSeek Sparse Attention (DSA) remain inefficient due to excessive global memory traffic, costly synchronization, and prohibitive memory overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11976:end -->

**为什么进入候选分母。** 摘要首要问题为“Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention algorithms in large language models and vector retrieval in recommendation systems and vector databases.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Based on this observation, we propose LITETOPK, an efficient fused Indexer-TopK kernel.

**证据证明什么。** Experimental results in a real-world deployment environ ment with eight B200 GPUs show that LITETOPK+LITEDSA accelerates the prefill stage of GLM 5.2 by 1.35x, with no performance loss and lower memory overhead.

**证据没有证明什么。** A promising direction for future work is to extend this approach to the decode stage, particularly by integrating it with speculative decoding. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11976v1#S3.SS2 — 3.2 Method。Evaluation：https://arxiv.org/html/2607.11976v1#S4.SS2 — 4.2 Experimental Results; https://arxiv.org/html/2607.11976v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11976v1#S5 — 5 Conclusion and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/vllm-project/vllm/pull/36178, https://github.com/Heisenberg-Yin/LiteTopK, https://github.com/deepseek-ai/DeepGEMM; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A promising direction for future work is to extend this approach to the decode stage, particularly by integrating it with speculative decoding.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11976:end -->

<!-- review:SF-2026-ARXIV-2607-12056:start -->
### Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability

<!-- claim:SF-2026-ARXIV-2607-12056:start -->Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12056:end -->

**为什么进入候选分母。** 摘要首要问题为“Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents.

**证据证明什么。** These results provide preliminary evidence that enhanced structural clarity, action cues, evidence signals, and temporal validity indicators can substantially improve the reliability and efficiency of AI browser agents.

**证据没有证明什么。** This limitation reflects a structural mismatch: the conventions of traditional web design were not developed with programmatic observation or automated action in mind, and existing interfaces often lack the properties needed [ 28 , 21 , 29 , 12 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12056v1#S2.SS3 — 2.3 Limitations of Existing Web Design; https://arxiv.org/html/2607.12056v1#S3 — 3 Research Problem and Approach。Evaluation：https://arxiv.org/html/2607.12056v1#S5.SS3 — 5.3 Evaluation Scoring and Analysis; https://arxiv.org/html/2607.12056v1#S6 — 6 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12056v1#S2.SS2 — 2.2 Failure Modes of Web Agents; https://arxiv.org/html/2607.12056v1#S2.SS3 — 2.3 Limitations of Existing Web Design。

**Artifact boundary。** Exact v1 links https://github.com/rashidiff/AIAgentReadWebSites, https://github.com/browser-use/browser-use, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：This limitation reflects a structural mismatch: the conventions of traditional web design were not developed with programmatic observation or automated action in mind, and existing interfaces often lack the properties needed [ 28 , 21 , 29 , 12 ] .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12056:end -->

<!-- review:SF-2026-ARXIV-2607-12068:start -->
### Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects

<!-- claim:SF-2026-ARXIV-2607-12068:start -->The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted. While these agents successfully automate the test generation, current evaluation benchmarks (e.g., SWE-bench) largely focus on pass-rates rather than the intrinsic quality of the generated tests. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12068:end -->

**为什么进入候选分母。** 摘要首要问题为“The integration of AI-powered coding agents into Continuous Integration/Continuous Delivery (CI/CD) pipelines has fundamentally altered how software verification is conducted.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We address this methodological gap through a large-scale, empirical comparison of 204,673 test artifacts which comprises of 24,941 human-authored files and 179,732 agent-generated files; sourced from the AIDev dataset.

**证据证明什么。** Our results present a nuanced inversion of traditional assumptions.

**证据没有证明什么。** IV-A Threats to Conclusion Validity The validity of the conclusion concerns the ability to draw a correct conclusion about the treatment (author type) and the outcome (test quality metrics). • Statistical Power and Sample Size: The study’s comparative analysis depends on statistical significance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12068v1#S2 — II Study Design; https://arxiv.org/html/2607.12068v1#S6.SS1 — VI-A Environmental Modeling and Sandboxed Execution。Evaluation：https://arxiv.org/html/2607.12068v1#S3 — III Experimental Results; https://arxiv.org/html/2607.12068v1#S2.SS1 — II-A “White-Boxing” the Analysis Pipelines。Limitations / counterevidence：https://arxiv.org/html/2607.12068v1#S4.SS1 — IV-A Threats to Conclusion Validity; https://arxiv.org/html/2607.12068v1#S4 — IV Threats To Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：IV-A Threats to Conclusion Validity The validity of the conclusion concerns the ability to draw a correct conclusion about the treatment (author type) and the outcome (test quality metrics). • Statistical Power and Sample Size: The study’s comparative analysis depends on statistical significance.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12068:end -->

<!-- review:SF-2026-ARXIV-2607-12085:start -->
### Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking

<!-- claim:SF-2026-ARXIV-2607-12085:start -->Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12085:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation of retail conversational systems.

**证据证明什么。** The pipeline achieved a macro F1 score of 0.93 and 89% human-acceptability accuracy for translation.

**证据没有证明什么。** A limitation of the current validation design is that each human-labeled record was reviewed by a single annotator. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12085v1#S4.SS1 — 4.1 Pipeline Architecture and Design; https://arxiv.org/html/2607.12085v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.12085v1#S5 — 5 Results, Evaluation, and Reliability; https://arxiv.org/html/2607.12085v1#S5.SS4 — 5.4 Model Benchmarking and Comparative Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.12085v1#S8 — 8 Conclusion and Future Work; https://arxiv.org/html/2607.12085v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A limitation of the current validation design is that each human-labeled record was reviewed by a single annotator.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12085:end -->

<!-- review:SF-2026-ARXIV-2607-12104:start -->
### TraceSynth: Generating Production-Quality Kernel Traces with Constraint-Guided Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-12104:start -->Machine learning models for system diagnostics rely on kernel execution traces to capture fine-grained system behavior, but collecting production traces in industrial systems is costly due to runtime overhead, storage demands, and privacy constraints. We present TraceSynth, a diffusion-based framework for generating synthetic kernel traces that augment limited real data for downstream ML tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12104:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine learning models for system diagnostics rely on kernel execution traces to capture fine-grained system behavior, but collecting production traces in industrial systems is costly due to runtime overhead, storage demands, and privacy constraints.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present TraceSynth, a diffusion-based framework for generating synthetic kernel traces that augment limited real data for downstream ML tasks.

**证据证明什么。** Across six benchmarks, results show strong workload dependence.

**证据没有证明什么。** Longer contexts may further improve generation quality, but cannot be assessed with current hardware. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12104v1#S3 — 3. Approach; https://arxiv.org/html/2607.12104v1#S3.SS2 — 3.2. Diffusion Model Architecture。Evaluation：https://arxiv.org/html/2607.12104v1#S4 — 4. Evaluation Setup; https://arxiv.org/html/2607.12104v1#S4.SS4 — 4.4. Downstream Task Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.12104v1#S6.SS5 — 6.5. Limitations and Threats to Validity; https://arxiv.org/html/2607.12104v1#S7 — 7. Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/17YuvrajSehgal/SyntheticLogGeneration, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Longer contexts may further improve generation quality, but cannot be assessed with current hardware.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12104:end -->

<!-- review:SF-2026-ARXIV-2607-12121:start -->
### FlashDiff: Efficient Regional Execution and Scheduling for Diffusion Model Serving

<!-- claim:SF-2026-ARXIV-2607-12121:start -->Diffusion models have become the central backbone for modern image, video, and audio generation, but their efficient service remains a challenge. Unlike autoregressive decoding, diffusion inference repeatedly updates high-dimensional spatial or temporal latents over many denoising steps. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12121:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion models have become the central backbone for modern image, video, and audio generation, but their efficient service remains a challenge.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** This paper presents FlashDiff, a diffusion serving system that improves inference efficiency through adaptive regional execution and scheduling.

**证据证明什么。** Across real-world image, video, and audio workloads, FlashDiff reduces end-to-end serving latency by 30-97% and improves throughput by 1.2-2.2x.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12121v1#S4 — 4. FlashDiff Design; https://arxiv.org/html/2607.12121v1#S6.SS1 — 6.1. Methodology。Evaluation：https://arxiv.org/html/2607.12121v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.12121v1#A1.SS6 — A.6. Second-Order Analysis: Stale KV-Cache Effects。Limitations / counterevidence：https://arxiv.org/html/2607.12121v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/NVIDIA/TensorRT, https://github.com/NVIDIA/TensorRT-LLM; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12121:end -->

<!-- review:SF-2026-ARXIV-2607-12188:start -->
### Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems

<!-- claim:SF-2026-ARXIV-2607-12188:start -->Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12188:end -->

**为什么进入候选分母。** 摘要首要问题为“Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant.

**证据证明什么。** The architecture reduces retrieval infrastructure cost by 3.1-9.0x compared to managed vector database services under the pricing assumptions detailed in Section IV.

**证据没有证明什么。** We note that this observation is limited to the codebook surface; it does not constitute end-to-end privacy guarantees, which would require a formal threat model and empirical evaluation beyond the scope of this paper. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12188v1#S3 — III Architecture; https://arxiv.org/html/2607.12188v1#S4.SS5 — IV-E Comparison Against Alternative Index Architectures。Evaluation：https://arxiv.org/html/2607.12188v1#S4 — IV Evaluation; https://arxiv.org/html/2607.12188v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.12188v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.12188v1#S5 — V Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：We note that this observation is limited to the codebook surface; it does not constitute end-to-end privacy guarantees, which would require a formal threat model and empirical evaluation beyond the scope of this paper.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12188:end -->

<!-- review:SF-2026-ARXIV-2607-12200:start -->
### A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models

<!-- claim:SF-2026-ARXIV-2607-12200:start -->As frontier language models advance, policymakers and model developers need methods for assessing whether model access materially increases a non-expert actor's ability to plan high-consequence Chemical, Biological, Radiological, or Nuclear (CBRN) misuse relative to public tools alone. Existing CBRN evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules, making results difficult to compare across studies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12200:end -->

**为什么进入候选分母。** 摘要首要问题为“As frontier language models advance, policymakers and model developers need methods for assessing whether model access materially increases a non-expert actor's ability to plan high-consequence Chemical, Biological, Radiological, or Nuclear (CBRN) misuse relative to public tools alone.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a Threshold Exceedance Criteria (TEC) framework that decomposes an uplift study into independently executable components: determining non-expert participant eligibility, defining the CBRN threat scope for the study, and statistically estimating material uplift.

**证据证明什么。** Existing CBRN evaluations differ in non-expert definitions, threat scope, baselines, scoring rubrics, and decision rules, making results difficult to compare across studies.

**证据没有证明什么。** This study has several limitations that future work should address. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12200v1#A2 — Appendix B Our TEC’s comparison against industrial safety frameworks; https://arxiv.org/html/2607.12200v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.12200v1#A6 — Appendix F Reliability Thresholds and Results; https://arxiv.org/html/2607.12200v1#S4 — 4 Experimental Study。Limitations / counterevidence：https://arxiv.org/html/2607.12200v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This study has several limitations that future work should address.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12200:end -->

<!-- review:SF-2026-ARXIV-2607-12211:start -->
### Overcoming Orchestration Bottlenecks at Exascale: A Decentralized, Policy-Driven Approach for Sim-AI Ensembles

<!-- claim:SF-2026-ARXIV-2607-12211:start -->Scientific computing is increasingly shifting from monolithic applications to coupled simulation-AI workflows composed of highly heterogeneous tasks with diverse hardware, scale, and runtime requirements. As these workflows scale to leadership-class systems, the resulting extreme ensemble sizes and task variability can create orchestration bottlenecks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12211:end -->

**为什么进入候选分母。** 摘要首要问题为“Scientific computing is increasingly shifting from monolithic applications to coupled simulation-AI workflows composed of highly heterogeneous tasks with diverse hardware, scale, and runtime requirements.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce EnsembleLauncher, a recursively hierarchical workflow orchestrator for exascale systems, featuring a fully decentralized control plane and a programmable scheduling policy interface.

**证据证明什么。** On the Aurora supercomputer, EnsembleLauncher successfully scales to the entire machine with up to eight million serial tasks, outperforming state-of-the-art tools by more than four times.

**证据没有证明什么。** Note that 8,192 nodes is only the maximum allowable allocation on Aurora supercomputer, and not the scalability limit of EnsembleLauncher. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12211v1#S3 — III System Design; https://arxiv.org/html/2607.12211v1#S2 — II Design Motivation。Evaluation：https://arxiv.org/html/2607.12211v1#S4 — IV Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.12211v1#S4.SS4 — IV-D Limitations; https://arxiv.org/html/2607.12211v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Note that 8,192 nodes is only the maximum allowable allocation on Aurora supercomputer, and not the scalability limit of EnsembleLauncher.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12211:end -->

<!-- review:SF-2026-ARXIV-2607-12227:start -->
### Rethinking the Evaluation of Harness Evolution for Agents

<!-- claim:SF-2026-ARXIV-2607-12227:start -->We revisit the evaluation of automatic harness evolution for LLM agents. Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12227:end -->

**为什么进入候选分母。** 摘要首要问题为“We revisit the evaluation of automatic harness evolution for LLM agents.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark.

**证据证明什么。** Experiments on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6 show that automatic harness evolution does not consistently outperform simple test-time scaling methods and exhibits limited generalization.

**证据没有证明什么。** Comparing automatic harness evolution against test-time discovery baselines under a unified budget, we find that it does not consistently outperform these baselines and that its gains generalize poorly beyond the training distribution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12227v1#S1 — 1 Introduction; https://arxiv.org/html/2607.12227v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.12227v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.12227v1#A1.SS5 — A.5 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.12227v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12227v1#S6 — 6 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/rethinking-harness-evolution, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Comparing automatic harness evolution against test-time discovery baselines under a unified budget, we find that it does not consistently outperform these baselines and that its gains generalize poorly beyond the training distribution.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12227:end -->

<!-- review:SF-2026-ARXIV-2607-12231:start -->
### The GEST-Engine: From Event Graphs to Synthetic Video. A Full Technical Report

<!-- claim:SF-2026-ARXIV-2607-12231:start -->We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video. At its core is an explicit world model: rather than encoding state as a learned latent, the engine maintains a complete, inspectable representation of the world (which actors exist, where they are, what they are doing, which objects they hold, and how events relate in time and space), expressed as a formal Graph of Events in Space and Time (GEST) and realized deterministically inside the open world of a commercial game engine driven through an open-source multiplayer scripting framework. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12231:end -->

**为什么进入候选分母。** 摘要首要问题为“We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present the GEST-Engine, a complete system that goes from natural-language text to fully-annotated multi-actor video.

**证据证明什么。** Because every frame traces back to a semantic specification, the engine guarantees object permanence, multi-actor coordination, and temporal consistency by construction, making its output valuable as training data, evaluation benchmarks, and diagnostic tools for video understanding.

**证据没有证明什么。** LLMs excel at the former but cannot maintain the precise state tracking the latter requires across the 50–200 events of a multi-actor story. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12231v1#S10.SS1 — 10.1 The Staged Approach and Its Failure; https://arxiv.org/html/2607.12231v1#S10.SS2 — 10.2 Architecture Overview。Evaluation：https://arxiv.org/html/2607.12231v1#S1 — 1 Related Work; https://arxiv.org/html/2607.12231v1#S2 — 2 Overview and Evolution。Limitations / counterevidence：https://arxiv.org/html/2607.12231v1#S10.SS1 — 10.1 The Staged Approach and Its Failure。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：LLMs excel at the former but cannot maintain the precise state tracking the latter requires across the 50–200 events of a multi-actor story.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12231:end -->

<!-- review:SF-2026-ARXIV-2607-12273:start -->
### Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs

<!-- claim:SF-2026-ARXIV-2607-12273:start -->As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences. Reliable automation, therefore, demands the ability to distinguish between confident, well-supported predictions and stochastic guessing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12273:end -->

**为什么进入候选分母。** 摘要首要问题为“As Code Large Language Models (LLMs) become central to modern software engineering, their inherent stochasticity poses significant real-world risks, where even minor errors can lead to severe functional, security, or safety consequences.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this syntax-semantics gap, we introduce Code-MUE, a purely black-box framework that measures uncertainty through execution-based Semantic Interaction Graphs.

**证据证明什么。** A large-scale empirical study across eight state-of-the-art LLMs demonstrates that Code-MUE achieves a strong negative correlation with functional correctness (Spearman's correlation up to -0.98), significantly outperforming lexical and embedding-based baselines while enabling robust risk detection and selective prediction in practical workflows.

**证据没有证明什么。** Another concern is whether our findings hold across different types of coding tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12273v1#S4 — 4. Method。Evaluation：https://arxiv.org/html/2607.12273v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.12273v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.12273v1#S6 — 6. Discussion; https://arxiv.org/html/2607.12273v1#S7 — 7. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/hnurxn/Code-Uncertainty, https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Another concern is whether our findings hold across different types of coding tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12273:end -->

<!-- review:SF-2026-ARXIV-2607-12278:start -->
### Auditing Data Leakage in Whole-Slide Image Multimodal Benchmarks

<!-- claim:SF-2026-ARXIV-2607-12278:start -->Recent vision-language models (VLMs) for computational pathology report striking zero-shot performance on whole-slide image (WSI) visual question answering (VQA) benchmarks. We audit these claims and find them fundamentally compromised by data leakage at two hierarchical levels: patient-level leakage, where slides from the same case appear in both training and test folds, and institutional-level leakage, where different cases nonetheless share staining-batch and scanner signatures through a common Tissue Source Site (TSS). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12278:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent vision-language models (VLMs) for computational pathology report striking zero-shot performance on whole-slide image (WSI) visual question answering (VQA) benchmarks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We audit these claims and find them fundamentally compromised by data leakage at two hierarchical levels: patient-level leakage, where slides from the same case appear in both training and test folds, and institutional-level leakage, where different cases nonetheless share staining-batch and scanner signatures through a common Tissue Source Site (TSS).

**证据证明什么。** We further demonstrate that both leakage levels are linearly decodable from foundation-model feature space, that they induce a measurable accuracy gap between leaked and audit-clean cases on a published checkpoint, and that across multiple published WSI VLMs, peak reported accuracies concentrate on the most heavily contaminated benchmarks.

**证据没有证明什么。** 5.3 Limitations Three scope conditions qualify our findings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12278v1#S2.SS1 — 2.1 WSI Multimodal Benchmarks and Models。Evaluation：https://arxiv.org/html/2607.12278v1#S2.SS1 — 2.1 WSI Multimodal Benchmarks and Models; https://arxiv.org/html/2607.12278v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12278v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12278v1#S5.SS3 — 5.3 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：5.3 Limitations Three scope conditions qualify our findings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12278:end -->

<!-- review:SF-2026-ARXIV-2607-12287:start -->
### Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference

<!-- claim:SF-2026-ARXIV-2607-12287:start -->Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment. We identify two primary sources of temporal redundancy in existing VLA pipelines: repeated visual encoding of highly similar consecutive frames and multi step iterative sampling in diffusion based policies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12287:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models exhibit strong generalization for robotic manipulation, yet their high inference latency limits real time deployment.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation.

**证据证明什么。** To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation.

**证据没有证明什么。** V Conclusion, Limitations and Future Work We presented a system level acceleration framework for Vision-Language-Action models that reduces temporal redundancy in both perception and policy inference. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12287v1#S3 — III Methodology; https://arxiv.org/html/2607.12287v1#S4.SS4 — IV-D System Level Ablation。Evaluation：https://arxiv.org/html/2607.12287v1#A3 — Appendix C Full RoboTwin Benchmark Results.; https://arxiv.org/html/2607.12287v1#A2 — Appendix B Efficiency Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12287v1#S5 — V Conclusion, Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：V Conclusion, Limitations and Future Work We presented a system level acceleration framework for Vision-Language-Action models that reduces temporal redundancy in both perception and policy inference.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12287:end -->

<!-- review:SF-2026-ARXIV-2607-12356:start -->
### VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-12356:start -->Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions. However, these models lack an explicit, scene-level 3D representation, limiting their ability to reason over spatial layouts and geometric constraints. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12356:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have emerged as a powerful end-to-end paradigm for robotic manipulation by mapping language instructions and 2D visual inputs directly to actions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In light of this, we present VistaVLA, a novel two-stage framework that constructs a geometry- and semantics-aware 3D cognitive representation from 3D Gaussian primitives and grounds it as compact context tokens for VLA policy learning.

**证据证明什么。** Extensive evaluations in both simulated and real-world environments demonstrate the effectiveness of VistaVLA.

**证据没有证明什么。** Our evaluation is currently limited to tabletop manipulation with a fixed robot platform and calibrated multi-view cameras. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12356v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.12356v1#S4 — 4 Experiments; https://arxiv.org/html/2607.12356v1#S4.SS1 — 4.1 Real-World Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12356v1#S5 — 5 Conclusion, Limitation, and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Our evaluation is currently limited to tabletop manipulation with a fixed robot platform and calibrated multi-view cameras.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12356:end -->

<!-- review:SF-2026-ARXIV-2607-12385:start -->
### PM-Bench: Evaluating Prospective Memory in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-12385:start -->A significant challenge in agentic AI is prospective memory: the ability to execute an intention at a specific future cue or state while other activities are ongoing. We introduce PM-Bench, a text-based benchmark for measuring prospective memory capabilities in modern LLM agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12385:end -->

**为什么进入候选分母。** 摘要首要问题为“A significant challenge in agentic AI is prospective memory: the ability to execute an intention at a specific future cue or state while other activities are ongoing.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce PM-Bench, a text-based benchmark for measuring prospective memory capabilities in modern LLM agents.

**证据证明什么。** We release PM-Bench as a controlled testbed for diagnosing these failures and developing training or inference-time interventions that support reliable prospective behavior.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12385v1#S3.SS1 — 3.1 Scenario Design; https://arxiv.org/html/2607.12385v1#S4.SS2 — 4.2 No Universal Best Scaffold Across Models and Metrics。Evaluation：https://arxiv.org/html/2607.12385v1#A1 — Appendix A Additional Benchmark Details and Results; https://arxiv.org/html/2607.12385v1#A1.SS6 — A.6 Additional Results and Failure Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12385v1#A1.SS6 — A.6 Additional Results and Failure Analysis; https://arxiv.org/html/2607.12385v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/genglinliu/PMBench.git, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12385:end -->

<!-- review:SF-2026-ARXIV-2607-12395:start -->
### Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

<!-- claim:SF-2026-ARXIV-2607-12395:start -->Reinforcement learning with verifiable rewards without human-annotated data, often referred to as zero RL, has emerged as a powerful paradigm for eliciting chain-of-thought reasoning. However, due to computational constraints, existing studies are largely restricted to small models, leaving the training dynamics and emergent capabilities at a large scale unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12395:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards without human-annotated data, often referred to as zero RL, has emerged as a powerful paradigm for eliciting chain-of-thought reasoning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address these challenges, we present a stable and efficient training pipeline, incorporating algorithmic and system optimizations such as clipped importance sampling, training-inference ratio correction, and mixed-precision control.

**证据证明什么。** Evaluated on seven mathematical benchmarks, Ring-2.5-1T-Zero achieves competitive performance.

**证据没有证明什么。** However, zero RL does not benefit from mimicking this natural frequency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12395v1#S3 — 3 Methodology; https://arxiv.org/html/2607.12395v1#S5.SS5 — 5.5 How Does Native RL-based CoT Compare to Distillation-based Approaches at Scale?。Evaluation：https://arxiv.org/html/2607.12395v1#A2 — Appendix B LLM-as-a-Judge Evaluation Prompts; https://arxiv.org/html/2607.12395v1#S2 — 2 Evaluation Metrics for Chain-of-Thought Quality。Limitations / counterevidence：https://arxiv.org/html/2607.12395v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12395v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/THUDM/slime, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, zero RL does not benefit from mimicking this natural frequency.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-REINFORCEMENT-LEARNING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12395:end -->

<!-- review:SF-2026-ARXIV-2607-12406:start -->
### Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions

<!-- claim:SF-2026-ARXIV-2607-12406:start -->The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12406:end -->

**为什么进入候选分母。** 摘要首要问题为“The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** It also concerns system behavior and real-world execution outcomes.

**证据证明什么。** We also summarize cross-boundary failure paths, discuss open challenges, and outline a research agenda for isolation-by-construction in future agent systems.

**证据没有证明什么。** 2.4 Defenses, Evaluation, and Future Directions Defenses at this boundary fall into three broad groups. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12406v1#S4.SS3 — 4.3 Embodied Agents and Vision-Language-Action Systems; https://arxiv.org/html/2607.12406v1#S6 — 6 System-Environment Boundary。Evaluation：https://arxiv.org/html/2607.12406v1#S2.SS4 — 2.4 Defenses, Evaluation, and Future Directions。Limitations / counterevidence：https://arxiv.org/html/2607.12406v1#S2.SS1 — 2.1 Threat Model and Boundary Definition; https://arxiv.org/html/2607.12406v1#S2.SS4 — 2.4 Defenses, Evaluation, and Future Directions。

**Artifact boundary。** Exact v1 links https://www.anthropic.com/engineering/claude-code-best-practices, https://openai.com/index/introducing-codex/, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：2.4 Defenses, Evaluation, and Future Directions Defenses at this boundary fall into three broad groups.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12406:end -->

<!-- review:SF-2026-ARXIV-2607-12463:start -->
### Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models

<!-- claim:SF-2026-ARXIV-2607-12463:start -->Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12463:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value.

**证据证明什么。** The improvement holds across two post-training pipelines (R2E-Gym, SWE-Smith) and on a non-Qwen2.5 base (Qwen3-8B with SWE-Lego).

**证据没有证明什么。** The mid-training corpus and the in-domain agent benchmarks are exclusively Python; cross-language evidence comes only indirectly through FullStackBench-EN (Section 3.3 ), and transfer to Java, C++, or Rust is left to future work. (ii) Teacher dependency for CoT. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12463v1#S2 — 2 Method; https://arxiv.org/html/2607.12463v1#A2 — Appendix B Algorithmic Details。Evaluation：https://arxiv.org/html/2607.12463v1#S3.SS2 — 3.2 Main Results on SWE Agent Benchmarks; https://arxiv.org/html/2607.12463v1#A4 — Appendix D Extended Behavioral Analysis (SWE-Bench-Verified)。Limitations / counterevidence：https://arxiv.org/html/2607.12463v1#S6 — 6 Limitations and Discussion; https://arxiv.org/html/2607.12463v1#A4.SS4 — D.4 Failure-Mode Breakdown。

**Artifact boundary。** Exact v1 links https://github.com/TIGER-AI-Lab/FIM-Midtraining, https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The mid-training corpus and the in-domain agent benchmarks are exclusively Python; cross-language evidence comes only indirectly through FullStackBench-EN (Section 3.3 ), and transfer to Java, C++, or Rust is left to future work. (ii) Teacher dependency for CoT.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12463:end -->

<!-- review:SF-2026-ARXIV-2607-12505:start -->
### Realizable N:M Sparse Transformer Inference via Search-Kernel Co-Design

<!-- claim:SF-2026-ARXIV-2607-12505:start -->Vision Transformers (ViTs) achieve strong accuracy but incur high inference latency. Semi-structured N:M sparsity can reduce arithmetic cost, yet its theoretical savings often fail to translate into proportional end-to-end speedups on modern GPUs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12505:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision Transformers (ViTs) achieve strong accuracy but incur high inference latency.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To this end, we propose a hardware-software co-design framework for N:M sparse ViT inference.

**证据证明什么。** Experiments on multiple ViT/Swin models and GPU platforms show that the framework achieves over 2.2x latency speedup while maintaining comparable accuracy and delivering superior accuracy under the same latency constraint.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12505v1#S4.SS1 — 4.1 Design Methodology; https://arxiv.org/html/2607.12505v1#S3 — 3 Problem Formulation and Method Overview。Evaluation：https://arxiv.org/html/2607.12505v1#S6 — 6 Experiments; https://arxiv.org/html/2607.12505v1#S6.SS1 — 6.1 MD-SpMM Kernel Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.12505v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/liuganhuo/realizable-nm-sparse-transformer, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12505:end -->

<!-- review:SF-2026-ARXIV-2607-12550:start -->
### A JoLT for the KV cache: Near-lossless KV cache compression via joint Lagrangian allocation of Tucker ranks and a rotated residual for llms

<!-- claim:SF-2026-ARXIV-2607-12550:start -->The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12550:end -->

**为什么进入候选分母。** 摘要首要问题为“The key-value (KV) cache has become the dominant memory cost of transformer inference: it grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the throughput ceiling.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry.

**证据证明什么。** A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at 1024-token context and matched quality.

**证据没有证明什么。** Finally, this study was conducted under a single-GPU (A100-40GB) compute budget; broader sweeps, larger models, and the harder multi-needle long-context regime are left to future work with more compute. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12550v1#S4 — 4 Method: Joint Tucker and JL Allocation (JoLT)。Evaluation：https://arxiv.org/html/2607.12550v1#A7 — Appendix G Full ablation grids; https://arxiv.org/html/2607.12550v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12550v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Finally, this study was conducted under a single-GPU (A100-40GB) compute budget; broader sweeps, larger models, and the harder multi-needle long-context regime are left to future work with more compute.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12550:end -->

<!-- review:SF-2026-ARXIV-2607-12571:start -->
### TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors

<!-- claim:SF-2026-ARXIV-2607-12571:start -->Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable. Existing vision or language defenses rarely explain what a triggered VLA representation looks like or how to recover behavior without retraining. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12571:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models are deployed through pipelines that end users cannot audit, and a poisoned VLA can behave normally on clean observations while a small visual trigger redirects a long-horizon robot policy before any failure becomes observable.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This footprint motivates TrustVLA, a mechanism-guided inference-time defense that adapts the Dirichlet evidence framework from trusted classification to monitor per-token, per-layer epistemic uncertainty in VLA policies.

**证据证明什么。** Across OpenVLA/LIBERO and $π_{0.5}$ transfer evaluations, TrustVLA reduces attack success while preserving clean-task performance, providing a retraining-free, mechanism-guided defense for visual-triggered VLA backdoors.

**证据没有证明什么。** Counterfactual score drop turns this signal into a localization criterion: a simple additive approximation yields (22) which explains why attention-only can fail (salient task objects need not reduce ), max-drop can over-select destructive regions, and Pareto/closure selection favors compact supports that suppress the mechanism while preserving task context. (a) LIBERO Object (b) LIBERO Spatial (c) LIBERO Goal (d) LIBERO-10 (e) Object, smaller trigger (f) Object, top-left trigger Figure 7: Layer-wise epistemic uncertainty under BadVLA. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12571v1#S3 — 3 Proposed Method; https://arxiv.org/html/2607.12571v1#A2 — Appendix B Implementation and Calibration Details。Evaluation：https://arxiv.org/html/2607.12571v1#A1 — Appendix A Theoretical Analysis; https://arxiv.org/html/2607.12571v1#A3 — Appendix C Ablation Protocol and Oracle Upper Bound。Limitations / counterevidence：https://arxiv.org/html/2607.12571v1#A1.SS1 — A.1 Mechanistic Interpretation and Adaptive Threats; https://arxiv.org/html/2607.12571v1#A7 — Appendix G Failure-Mode Accounting。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Counterfactual score drop turns this signal into a localization criterion: a simple additive approximation yields (22) which explains why attention-only can fail (salient task objects need not reduce ), max-drop can over-select destructive regions, and Pareto/closure selection favors compact supports that suppress the mechanism while preserving task context. (a) LIBERO Object (b) LIBERO Spatial (c) LIBERO Goal (d) LIBERO-10 (e) Object, smaller trigger (f) Object, top-left trigger Figure 7: Layer-wise epistemic uncertainty under BadVLA.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12571:end -->

<!-- review:SF-2026-ARXIV-2607-12592:start -->
### WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction

<!-- claim:SF-2026-ARXIV-2607-12592:start -->We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input. Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12592:end -->

**为什么进入候选分母。** 摘要首要问题为“We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input.

**证据证明什么。** To our knowledge, WanToFight is the first generative game engine to combine multi-player control, real-time inference, complex physical interaction, and adversarial gameplay in one system.

**证据没有证明什么。** 5 Limitations WanToFight pushes generative engines into the multi-player, real-time, adversarial regime, but several limitations remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12592v1#S3 — 3 Method; https://arxiv.org/html/2607.12592v1#S3.SS2 — 3.2 Model Design。Evaluation：https://arxiv.org/html/2607.12592v1#S4 — 4 Results; https://arxiv.org/html/2607.12592v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.12592v1#S5 — 5 Limitations; https://arxiv.org/html/2607.12592v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Limitations WanToFight pushes generative engines into the multi-player, real-time, adversarial regime, but several limitations remain.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12592:end -->

<!-- review:SF-2026-ARXIV-2607-12614:start -->
### Inference Pipelines as Operating-System Objects: Priority Scheduling and Constant-Footprint Streaming for Microcontroller Neural Inference

<!-- claim:SF-2026-ARXIV-2607-12614:start -->Microcontroller runtimes treat the inference pipeline -- pre-processing, accelerator invocation, post-processing -- as application code: every project re-implements stage sequencing, buffer sizing, and completion signalling around a library call. We argue these are operating-system concerns and present the Phase 2 inference engine of SynapticOS, an open-source Zephyr-based runtime that makes the pipeline a first-class OS object. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12614:end -->

**为什么进入候选分母。** 摘要首要问题为“Microcontroller runtimes treat the inference pipeline -- pre-processing, accelerator invocation, post-processing -- as application code: every project re-implements stage sequencing, buffer sizing, and completion signalling around a library call.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We argue these are operating-system concerns and present the Phase 2 inference engine of SynapticOS, an open-source Zephyr-based runtime that makes the pipeline a first-class OS object.

**证据证明什么。** Released under Apache 2.0 at https://github.com/Dimitrios-Kafetzis/SynapticOS

**证据没有证明什么。** Correct for models trained with this frontend; a parity mode is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12614v1#S1 — I Introduction; https://arxiv.org/html/2607.12614v1#S1.SS1 — I-A Pipelines as OS Objects。Evaluation：https://arxiv.org/html/2607.12614v1#S7 — VII Evaluation; https://arxiv.org/html/2607.12614v1#S7.SS1 — VII-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.12614v1#S8 — VIII Discussion; https://arxiv.org/html/2607.12614v1#S8.SS2 — VIII-B Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Dimitrios-Kafetzis/SynapticOS, https://zephyrproject.org, https://github.com/ARM-software/CMSIS-NN; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Correct for models trained with this frontend; a parity mode is future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12614:end -->

<!-- review:SF-2026-ARXIV-2607-12625:start -->
### KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

<!-- claim:SF-2026-ARXIV-2607-12625:start -->OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism. These flaws limit its adaptation to diverse device ecosystems and prevent performance improvements through continuous learning from execution experience. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12625:end -->

**为什么进入候选分母。** 摘要首要问题为“OpenClaw has emerged as a leading agent framework for complex task automation, yet it faces insufficient cross-platform GUI interaction support and a well-built self-evolution mechanism.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Based on this paradigm, we introduce KnowAct-GUIClaw, a novel Know-Route-Act-Reflect framework designed to address OpenClaw's GUI manipulation deficits and break through its cross-platform and recursive self-improvement constraints.

**证据证明什么。** Extensive experiments across Android, iOS, HarmonyOS and Windows show that KnowAct-GUIClaw achieves superior efficiency, accuracy and cross-platform adaptability.

**证据没有证明什么。** Future work targets tighter native integration of the Knowledge module, external general-purpose tools, and the GUI subagent to eliminate rigid sequential pipeline handoffs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12625v1#S3.SS2 — 3.2 Host-Centric Multi-Agent Systems。Evaluation：https://arxiv.org/html/2607.12625v1#S5.SS3 — 5.3 Ablation and Efficiency Analysis; https://arxiv.org/html/2607.12625v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12625v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/HITsz-TMG/KnowAct, https://github.com/HITsz-TMG/KnowAct/releases/tag/Result, https://github.com/HKUDS/nanobot; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work targets tighter native integration of the Knowledge module, external general-purpose tools, and the GUI subagent to eliminate rigid sequential pipeline handoffs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12625:end -->

<!-- review:SF-2026-ARXIV-2607-12650:start -->
### Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

<!-- claim:SF-2026-ARXIV-2607-12650:start -->Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12650:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts.

**证据证明什么。** Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure.

**证据没有证明什么。** The 3-blind-formalizer consensus design is implemented in the runtime but not evaluated here; we defer the consensus study to future work. (ii) Trust artifacts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12650v1#A9 — Appendix I Failure cases and formalizer-design notes。Evaluation：https://arxiv.org/html/2607.12650v1#A5 — Appendix E Tier 1.5 per-claim data, ablations, and pre-registration; https://arxiv.org/html/2607.12650v1#A5.SS3 — E.3 Authority-cue ablation: no-cue pilot vs authority-cued pilot per-claim。Limitations / counterevidence：https://arxiv.org/html/2607.12650v1#A13 — Appendix M Scope limits and future extensions; https://arxiv.org/html/2607.12650v1#A13.SS1 — M.1 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/7pocheR/eg-var, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The 3-blind-formalizer consensus design is implemented in the runtime but not evaluated here; we defer the consensus study to future work. (ii) Trust artifacts.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12650:end -->

<!-- review:SF-2026-ARXIV-2607-12659:start -->
### Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference

<!-- claim:SF-2026-ARXIV-2607-12659:start -->Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12659:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction.

**证据证明什么。** Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark.

**证据没有证明什么。** To address these, we use Foresight-Aligned Asynchronous Correction that predicts future VLM latents to guide action prediction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12659v1#S4.SS3 — 4.3 System Design; https://arxiv.org/html/2607.12659v1#A1 — Appendix A Model Architecture of series Models。Evaluation：https://arxiv.org/html/2607.12659v1#S5 — 5 Experiments; https://arxiv.org/html/2607.12659v1#S5.SS1 — 5.1 Simulation Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12659v1#A2 — Appendix B Architecture of Future Correction Module; https://arxiv.org/html/2607.12659v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/PKU-SEC-Lab/Jetson-PI, https://github.com/PKU-SEC-Lab/Jetson-PI-Edge, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：To address these, we use Foresight-Aligned Asynchronous Correction that predicts future VLM latents to guide action prediction.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12659:end -->

<!-- review:SF-2026-ARXIV-2607-12696:start -->
### Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts

<!-- claim:SF-2026-ARXIV-2607-12696:start -->Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns. Speculative decoding (SD) accelerates autoregressive generation by verifying multiple draft tokens in parallel, yet existing draft selection strategies primarily optimize acceptance likelihood. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12696:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We propose \textsc{EcoSpec}, a cost-aware speculative decoding framework that incorporates predicted marginal expert activation cost into draft selection.

**证据证明什么。** These results show that accounting for expert activation cost is important for efficient speculative decoding in large-scale MoE models.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12696v1#S4 — 4 Methodology: EcoSpec; https://arxiv.org/html/2607.12696v1#A6 — Appendix F Model Details。Evaluation：https://arxiv.org/html/2607.12696v1#A2 — Appendix B Predictor Details and Analysis; https://arxiv.org/html/2607.12696v1#A2.SS3 — B.3 Oracle Expert-Set Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12696v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/lmsys/Qwen3-235B-A22B-EAGLE3, https://huggingface.co/lmsys/EAGLE3-gpt-oss-120b-bf16, https://huggingface.co/datasets/AI-MO/aimo-validation-amc; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12696:end -->

<!-- review:SF-2026-ARXIV-2607-12747:start -->
### Tracing Agentic Failure from the Flow of Success

<!-- claim:SF-2026-ARXIV-2607-12747:start -->Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12747:end -->

**为什么进入候选分母。** 摘要首要问题为“Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems.

**证据证明什么。** With training on only 100 successful trajectories, experiments show that OAT is 200--5000 $\times$ faster than prompting-based baselines, and, at the same time, consistently outperforms them in both in-domain and out-of-distribution datasets with +20% and +7% F1 scores, respectively, demonstrating that OAT is a promising and efficient direction for diagnosing agentic system failures.

**证据没有证明什么。** The annotation process proceeds in two stages: trajectory filtering and step-level labeling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12747v1#S4 — 4 Methodology; https://arxiv.org/html/2607.12747v1#A6 — Appendix F Additional Implementation Details & Hyperparameters。Evaluation：https://arxiv.org/html/2607.12747v1#A7 — Appendix G Additional Experimental Results; https://arxiv.org/html/2607.12747v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12747v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.12747v1#A5 — Appendix E Annotation of Failure Contributing Steps。

**Artifact boundary。** Exact v1 links https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct, https://huggingface.co/blog/gemma4, https://neurips.cc/public/guides/CodeSubmissionPolicy; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The annotation process proceeds in two stages: trajectory filtering and step-level labeling.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12747:end -->

<!-- review:SF-2026-ARXIV-2607-12767:start -->
### Accuracy and Normalized Accuracy under Length Bias: Analysis, Guidelines, and a Bayesian Alternative

<!-- claim:SF-2026-ARXIV-2607-12767:start -->Multiple-choice benchmarks that rank candidate completions by conditional log-probability suffer from a length bias: because log-probabilities sum over tokens, longer answers tend to be penalized relative to shorter ones in practice. A common mitigation is to normalize scores by completion length, but we show empirically that this heuristic frequently over-corrects, introducing a bias toward longer answers instead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12767:end -->

**为什么进入候选分母。** 摘要首要问题为“Multiple-choice benchmarks that rank candidate completions by conditional log-probability suffer from a length bias: because log-probabilities sum over tokens, longer answers tend to be penalized relative to shorter ones in practice.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Motivated by this analysis, we introduce \emph{Bayesian accuracy}, a scoring rule that computes the posterior probability of each candidate under an explicit prior over answer length, thereby removing linear length effects.

**证据证明什么。** A common mitigation is to normalize scores by completion length, but we show empirically that this heuristic frequently over-corrects, introducing a bias toward longer answers instead.

**证据没有证明什么。** This addresses a measurable nuisance effect in likelihood-based evaluation, while broader questions of evaluation faithfulness, such as agreement with downstream capabilities, remain important directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12767v1#A1.SS3 — A.3 Algorithm; https://arxiv.org/html/2607.12767v1#S3.SS2 — 3.2 Benchmarks and Models。Evaluation：https://arxiv.org/html/2607.12767v1#A1.SS4 — A.4 Benchmark Details; https://arxiv.org/html/2607.12767v1#A1.SS5 — A.5 Benchmark Prompt Examples。Limitations / counterevidence：https://arxiv.org/html/2607.12767v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Aleph-Alpha-Research/eval-framework, https://github.com/huggingface/lighteval, https://huggingface.co/datasets/LeoLM/ArcChallenge_de; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This addresses a measurable nuisance effect in likelihood-based evaluation, while broader questions of evaluation faithfulness, such as agreement with downstream capabilities, remain important directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12767:end -->

<!-- review:SF-2026-ARXIV-2607-12790:start -->
### Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents

<!-- claim:SF-2026-ARXIV-2607-12790:start -->Self-evolving agent systems create, revise, and retire their own skills, but every such loop assumes a reliable evaluation metric already exists. We show the metric itself can be the evolving object: our loop searches compositions of small typed drawback detectors under a full evolutionary lifecycle, selecting for agreement with a ten-item anchored reference set and regularizing by consensus over unlabeled outputs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12790:end -->

**为什么进入候选分母。** 摘要首要问题为“Self-evolving agent systems create, revise, and retire their own skills, but every such loop assumes a reliable evaluation metric already exists.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Self-evolving agent systems create, revise, and retire their own skills, but every such loop assumes a reliable evaluation metric already exists.

**证据证明什么。** We show the metric itself can be the evolving object: our loop searches compositions of small typed drawback detectors under a full evolutionary lifecycle, selecting for agreement with a ten-item anchored reference set and regularizing by consensus over unlabeled outputs.

**证据没有证明什么。** Double Ratchet removes the assumption that a reliable grader pre-exists, retaining 88–110% of the supervised lift with an inspectable metric; its load-bearing guard is anchor discipline, not the pool lifecycle; and on the deployment-style task it caught its metric being gamed, repaired it with one detector, then caught its judge misreading the format contract. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12790v1#Sx1 — Introduction; https://arxiv.org/html/2607.12790v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.12790v1#A7 — Appendix G Appendix G: Negative and Supporting Results; https://arxiv.org/html/2607.12790v1#Sx3.SSx4 — Two Ablations: Anchor Guards versus Lifecycle。Limitations / counterevidence：https://arxiv.org/html/2607.12790v1#Sx6 — Discussion and Limitations; https://arxiv.org/html/2607.12790v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://developers.openai.com/codex/record-and-replay, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Double Ratchet removes the assumption that a reliable grader pre-exists, retaining 88–110% of the supervised lift with an inspectable metric; its load-bearing guard is anchor discipline, not the pool lifecycle; and on the deployment-style task it caught its metric being gamed, repaired it with one detector, then caught its judge misreading the format contract.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12790:end -->

<!-- review:SF-2026-ARXIV-2607-12831:start -->
### Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling

<!-- claim:SF-2026-ARXIV-2607-12831:start -->Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12831:end -->

**为什么进入候选分母。** 摘要首要问题为“Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning.

**证据证明什么。** Crucially, in retrieval-grounded settings with imperfect evidence, KLLMs show improved robustness and achieve up to 20--25\% relative gains over standard language models.

**证据没有证明什么。** Overall, KLLMs provide a concrete step toward language models that are not only capable, but reliably grounded and controllable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12831v1#A14 — Appendix N Implementation Details; https://arxiv.org/html/2607.12831v1#S2 — 2 Knowledgeless Language Modelling。Evaluation：https://arxiv.org/html/2607.12831v1#A10 — Appendix J Data Efficiency Analysis; https://arxiv.org/html/2607.12831v1#A12 — Appendix L Representation-Level Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12831v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.12831v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/flair/ner-english-ontonotes-large, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Overall, KLLMs provide a concrete step toward language models that are not only capable, but reliably grounded and controllable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12831:end -->

<!-- review:SF-2026-ARXIV-2607-12835:start -->
### Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction

<!-- claim:SF-2026-ARXIV-2607-12835:start -->Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12835:end -->

**为什么进入候选分母。** 摘要首要问题为“Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction.

**证据证明什么。** Our results show that the augmented settings substantially improves downstream evaluation alignment, with the strongest setting approaching the human baseline, while intrinsic gains are more modest.

**证据没有证明什么。** We manually re-annotated rubrics for PaperBench into a checklist-style format as a baseline and evaluated LLM-generated rubrics under four progressively augmented settings, using both intrinsic textual alignment and extrinsic repository-level alignment with human PaperBench judgments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12835v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.12835v1#S4.SS1 — 4.1 Extrinsic Meta-Evaluation Results; https://arxiv.org/html/2607.12835v1#S4.SS2 — 4.2 Intrinsic Meta-Evaluation Results。Limitations / counterevidence：https://arxiv.org/html/2607.12835v1#A4 — Appendix D Threshold Discussion; https://arxiv.org/html/2607.12835v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://code.claude.com/docs, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We manually re-annotated rubrics for PaperBench into a checklist-style format as a baseline and evaluated LLM-generated rubrics under four progressively augmented settings, using both intrinsic textual alignment and extrinsic repository-level alignment with human PaperBench judgments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12835:end -->

<!-- review:SF-2026-ARXIV-2607-12839:start -->
### HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference

<!-- claim:SF-2026-ARXIV-2607-12839:start -->Modern edge system-on-chips (SoCs) combine CPUs, integrated GPUs (iGPUs), and neural processing units (NPUs), yet existing LLM runtimes typically make coarse device-level decisions or optimize operators in isolation. As a result, they underutilize heterogeneous resources, particularly on unified-memory platforms where performance depends on both device placement and task-graph coordination. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12839:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern edge system-on-chips (SoCs) combine CPUs, integrated GPUs (iGPUs), and neural processing units (NPUs), yet existing LLM runtimes typically make coarse device-level decisions or optimize operators in isolation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present HeteroMosaic, a heterogeneity-first scheduling framework for edge LLM inference.

**证据证明什么。** It also improves performance over prior heterogeneous edge AI solutions by up to 2.35X.

**证据没有证明什么。** However, these workloads also introduce new constraints, such as image-token preprocessing, vision encoder stages, control-loop latency requirements, and diffusion-step dependencies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12839v1#S6.SS5 — 6.5. Comparison with Other Frameworks; https://arxiv.org/html/2607.12839v1#S3.SS1 — 3.1. Sparse and Model-Restructured Inference.。Evaluation：https://arxiv.org/html/2607.12839v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.12839v1#S6.SS1 — 6.1. Microbenchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.12839v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.12839v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://rocm.docs.amd.com/projects/HIP/en/develop/doxygen/html/group___event.html#ga5df2309c9f29ca4c8e669db658d411b4, https://rocm.docs.amd.com/projects/HIP/en/docs-develop/reference/hip_runtime_api/modules/stream_memory_operations.html, https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, these workloads also introduce new constraints, such as image-token preprocessing, vision encoder stages, control-loop latency requirements, and diffusion-step dependencies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12839:end -->

<!-- review:SF-2026-ARXIV-2607-12875:start -->
### Automatic Model-Hardware Co-Adaptation for Heterogeneous AI Accelerators

<!-- claim:SF-2026-ARXIV-2607-12875:start -->Large language models now evolve faster than production inference systems can be ported and optimized. New releases change attention, MoE routing, quantization formats, KV-cache layout, and parallel execution patterns, while deployed accelerator fleets remain heterogeneous across hardware generations, framework forks, operator libraries, compiler backends, and communication runtimes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12875:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models now evolve faster than production inference systems can be ported and optimized.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present MetaInfer, an LLM-agent system that formulates inference adaptation as route search over a costed execution-adaptation graph.

**证据证明什么。** MetaInfer constructs and updates this graph during execution, restores missing or blocked routes through patches, and reduces route cost through staged validation and end-to-end profiling.

**证据没有证明什么。** 5.3 Limitations and risks of the evolution strategy Knowledge-base evolution expands the applicability of MetaInfer , but it does not remove all human and environmental dependencies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12875v1#A1 — Appendix A Implementation Details of the MetaInfer Method; https://arxiv.org/html/2607.12875v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.12875v1#S4.SS1 — 4.1 Experimental setup and evaluation metrics; https://arxiv.org/html/2607.12875v1#A2 — Appendix B Historical Platform Results。Limitations / counterevidence：https://arxiv.org/html/2607.12875v1#S5 — 5 Discussion; https://arxiv.org/html/2607.12875v1#S5.SS3 — 5.3 Limitations and risks of the evolution strategy。

**Artifact boundary。** Exact v1 links https://github.com/MetaInfer/MetaInfer, https://github.com/OpenBMB/ForgeTrain, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：5.3 Limitations and risks of the evolution strategy Knowledge-base evolution expands the applicability of MetaInfer , but it does not remove all human and environmental dependencies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12875:end -->

<!-- review:SF-2026-ARXIV-2607-12885:start -->
### LLM Judges Can Be Too Generous When There Is No Reference Answer

<!-- claim:SF-2026-ARXIV-2607-12885:start -->LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12885:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Our results emphasize the need for calibrating the LLM judges with a sample with reference-aware evaluation before using them in reference-free setups reliably, and our methodology provides a blueprint for researchers and practitioners in doing such calibration of LLM judges for other tasks.

**证据证明什么。** Comparison with a subset of human annotations shows that these reference-driven changes generally align with human judgments.

**证据没有证明什么。** A human annotation study showed that the presence of a reference answer helps judge decisions align more closely with human judgments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12885v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.12885v1#A1.SS2 — A.2 Calibration Experiment Results; https://arxiv.org/html/2607.12885v1#A1.SS3 — A.3 Sensitivity Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.12885v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.12885v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/copenlu/answerable_tydiqa, https://huggingface.co/datasets/TeluguLLMResearch/MATA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A human annotation study showed that the presence of a reference answer helps judge decisions align more closely with human judgments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12885:end -->

<!-- review:SF-2026-ARXIV-2607-12893:start -->
### MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations

<!-- claim:SF-2026-ARXIV-2607-12893:start -->Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12893:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Across long-context, retrieval-based, parametric and managed-memory systems, MemOps disentangles failure modes that final-answer accuracy alone conceals, revealing that current systems remain far from uniformly reliable.

**证据证明什么。** These results move long-term memory evaluation from final-answer scoring toward interpretable, operation-level diagnosis.

**证据没有证明什么。** Third, MemOps can be used not only for evaluation, but also as a development signal for memory controllers that explicitly learn when to write, update, delete, retrieve, and justify memory states. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12893v1#S2.SS2 — 2.2 Memory-Enhanced LLM Systems。Evaluation：https://arxiv.org/html/2607.12893v1#S2.SS1 — 2.1 Long-Term Conversation Benchmarks; https://arxiv.org/html/2607.12893v1#S3.SS2 — 3.2 Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.12893v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/MemTensor/MemOps, https://github.com/%7BQ%7Dwen%7BL%7D%7BM%7D/%7BQ%7Dwen3.6, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Third, MemOps can be used not only for evaluation, but also as a development signal for memory controllers that explicitly learn when to write, update, delete, retrieve, and justify memory states.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12893:end -->

<!-- review:SF-2026-ARXIV-2607-12894:start -->
### Hy-Embodied-VLM-1.0: Efficient Physical-World Agents

<!-- claim:SF-2026-ARXIV-2607-12894:start -->Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodied agents operating in the physical world. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12894:end -->

**为什么进入候选分母。** 摘要首要问题为“Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Guided by this taxonomy, we develop a systematic data pipeline and curate data mixtures spanning both pre-training and post-training.

**证据证明什么。** The model achieves the best performance among similarly sized models on 19 of the 38 benchmarks and substantially outperforms strong competitors, including Qwen3.6-A3B and Cosmos 3.

**证据没有证明什么。** Built on the Hy3-A3B backbone and Hy-ViT2 vision encoder, the model activates only approximately 3B parameters per token while maintaining strong embodied capabilities. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12894v1#S3 — 3 Model Architecture。Evaluation：https://arxiv.org/html/2607.12894v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.12894v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Tencent-Hunyuan/HY-Embodied, https://huggingface.co/tencent/Hy-Embodied-VLM-1.0, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Built on the Hy3-A3B backbone and Hy-ViT2 vision encoder, the model activates only approximately 3B parameters per token while maintaining strong embodied capabilities.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12894:end -->

<!-- review:SF-2026-ARXIV-2607-12911:start -->
### Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition

<!-- claim:SF-2026-ARXIV-2607-12911:start -->Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12911:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Open-KNEAD, a knowledge-grounded agentic framework for meal nutrition estimation that is training-free and locally deployable.

**证据证明什么。** However, we find this premise no longer holds for current MLLMs.

**证据没有证明什么。** Multi-view fusion (extra camera views) Worsens portion for a model that cannot fuse views geometrically: g (N5k), g (OmniFood) MAE vs. single view. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12911v1#S3 — 3 Method: Open-KNEAD; https://arxiv.org/html/2607.12911v1#S3.SS1 — 3.1 Problem setting and design constraints。Evaluation：https://arxiv.org/html/2607.12911v1#A1.SS4 — A.4 Full main results (all backbones); https://arxiv.org/html/2607.12911v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.12911v1#A1.SS10 — A.10 Failure modes; https://arxiv.org/html/2607.12911v1#A1.SS9 — A.9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Multi-view fusion (extra camera views) Worsens portion for a model that cannot fuse views geometrically: g (N5k), g (OmniFood) MAE vs. single view.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12911:end -->

<!-- review:SF-2026-ARXIV-2607-12931:start -->
### ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning

<!-- claim:SF-2026-ARXIV-2607-12931:start -->Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks. However, its practical scalability remains severely limited by the substantial cost of environmental interactions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12931:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement Learning (RL) has demonstrated significant potential for improving Vision-Language-Action (VLA) models on complex manipulation tasks.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration.

**证据证明什么。** Extensive experiments across simulated and real-world robotic manipulation tasks demonstrate that ExToken consistently accelerates convergence, improves task performance, and exhibits strong robustness under highly constrained interaction budgets.

**证据没有证明什么。** While ExToken significantly enhances sample efficiency, our framework adopts a simplified design to validate the core hypothesis of token-guided exploration, presenting several avenues for future refinement. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12931v1#A1.SS1 — A.1 Reinforcement Fine-tuning for VLA models。Evaluation：https://arxiv.org/html/2607.12931v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.12931v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.12931v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/MINT-SJTU/Evo-RL, https://github.com/Physical-Intelligence/openpi, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：While ExToken significantly enhances sample efficiency, our framework adopts a simplified design to validate the core hypothesis of token-guided exploration, presenting several avenues for future refinement.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12931:end -->

<!-- review:SF-2026-ARXIV-2607-12962:start -->
### Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models

<!-- claim:SF-2026-ARXIV-2607-12962:start -->Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature. We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12962:end -->

**为什么进入候选分母。** 摘要首要问题为“Frozen small code LLMs are deployed locally, yet the information guiding a retry after a failed attempt is still measured without placebo controls in the self-repair literature.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We treat a failed program as a conjecture and an execution counterexample as an oracle-relative refutation, and introduce PoPE (Popperian Placebo-controlled Evaluation): a methodology for measuring whether evidence that falsifies LLM-generated code can be used operationally by that same model.

**证据证明什么。** These results do not constitute evidence of equivalence or non-inferiority.

**证据没有证明什么。** The 1,964-pair count should therefore not obscure the limit of 236 independent units, and the zero-leakage audit should not be read as a diversity audit. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12962v1#S2 — 2 Methods。Evaluation：https://arxiv.org/html/2607.12962v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.12962v1#S4 — 4 Discussion; https://arxiv.org/html/2607.12962v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The 1,964-pair count should therefore not obscure the limit of 236 independent units, and the zero-leakage audit should not be read as a diversity audit.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12962:end -->

<!-- review:SF-2026-ARXIV-2607-12963:start -->
### The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context

<!-- claim:SF-2026-ARXIV-2607-12963:start -->As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context. In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12963:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) grow more capable, they are increasingly deployed in context-rich settings where task inputs are often accompanied by long, partially irrelevant context.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In a controlled setting, we find that state-of-the-art models often appear robust to task-irrelevant context at the aggregate level: prepending it to benchmark questions causes little change in overall accuracy.

**证据证明什么。** We further show that this instability is modulated by context type, context length, test-time compute, and model development stage.

**证据没有证明什么。** Building on these findings, future work could explore several directions: • Improving measurement efficiency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12963v1#A7 — Appendix G Details of Local Model Experiments; https://arxiv.org/html/2607.12963v1#S3.SS2 — 3.2 Model Specificity。Evaluation：https://arxiv.org/html/2607.12963v1#A2 — Appendix B Extra Experiment Details; https://arxiv.org/html/2607.12963v1#A3 — Appendix C Details of Qualitative Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.12963v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SALT-NLP/illusion-of-robustness, https://github.com/gkamradt/LLMTest_NeedleInAHaystack, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Building on these findings, future work could explore several directions: • Improving measurement efficiency.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12963:end -->

<!-- review:SF-2026-ARXIV-2607-12986:start -->
### Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation

<!-- claim:SF-2026-ARXIV-2607-12986:start -->Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12986:end -->

**为什么进入候选分母。** 摘要首要问题为“Plan evaluators can reward a strategic plan for becoming less explicit.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes.

**证据证明什么。** Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i

**证据没有证明什么。** Registry provenance is therefore a real boundary: v1 cannot catch internally consistent but semantically empty authored fields, and the EXP B route-arounds plus EXP C evasions motivate independently authored, non-co-authorable field sets. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12986v1#S2.SS3 — 2.3 Model-Mediated Typing。Evaluation：https://arxiv.org/html/2607.12986v1#S4 — 4 Experimental Program。Limitations / counterevidence：https://arxiv.org/html/2607.12986v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.12986v1#S9 — 9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Registry provenance is therefore a real boundary: v1 cannot catch internally consistent but semantically empty authored fields, and the EXP B route-arounds plus EXP C evasions motivate independently authored, non-co-authorable field sets.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12986:end -->

<!-- review:SF-2026-ARXIV-2607-12992:start -->
### ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning

<!-- claim:SF-2026-ARXIV-2607-12992:start -->Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate. Existing methods, such as inference-time blending, merely reweight mismatched proposals without correcting underlying errors, leading to residual accumulation under biased or noisy histories. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-12992:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language action (VLA) models increasingly adopt chunked action heads to satisfy real-time constraints; however, this introduces boundary jitter: overlapping regions between consecutive chunks often yield inconsistent predictions, degrading temporal coherence and the task success rate.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose ChunkFlow, a seam-aware training-and-execution framework for chunked policies that aligns chunk structure with boundary execution.

**证据证明什么。** Experiments on CALVIN, LIBERO, and real robots show an improved success-stability trade-off with low-latency inference.

**证据没有证明什么。** These results support execution-indexed chunk alignment in simulation and initial hardware tests, while broader real-world robustness remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.12992v1#S3 — III Method。Evaluation：https://arxiv.org/html/2607.12992v1#S4 — IV Experiment; https://arxiv.org/html/2607.12992v1#S4.SS1 — IV-A Dataset and Evaluation Metric。Limitations / counterevidence：https://arxiv.org/html/2607.12992v1#S5 — V CONCLUSIONS。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These results support execution-indexed chunk alignment in simulation and initial hardware tests, while broader real-world robustness remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-12992:end -->

<!-- review:SF-2026-ARXIV-2607-13013:start -->
### Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model

<!-- claim:SF-2026-ARXIV-2607-13013:start -->Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13013:end -->

**为什么进入候选分母。** 摘要首要问题为“Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps.

**证据证明什么。** We find that the natural training objectives fail to ground the audio because their gradient reaches the projector only through attention that has already dismissed it.

**证据没有证明什么。** 7 Limitations The model trails autoregressive Whisper on every benchmark we tested, by the largest margin on multilingual read speech. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13013v1#S3 — 3 Method; https://arxiv.org/html/2607.13013v1#S5.SS4 — 5.4 Comparison with diffusion and autoregressive systems。Evaluation：https://arxiv.org/html/2607.13013v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.13013v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.13013v1#S7 — 7 Limitations; https://arxiv.org/html/2607.13013v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：7 Limitations The model trails autoregressive Whisper on every benchmark we tested, by the largest margin on multilingual read speech.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13013:end -->

<!-- review:SF-2026-ARXIV-2607-13017:start -->
### FlowWAM: Optical Flow as a Unified Action Representation for World Action Models

<!-- claim:SF-2026-ARXIV-2607-13017:start -->World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction. However, directly leveraging such video generators for control raises a new challenge: how to represent actions in a suitable form that aligns with pretrained video generators while carrying enough motion cues for accurate control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13017:end -->

**为什么进入候选分母。** 摘要首要问题为“World Action Models (WAMs) are able to leverage pretrained video generators for both world modeling and action prediction.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We address this issue with FlowWAM, a dual-stream diffusion framework that adopts optical flow as a unified, video-native action representation.

**证据证明什么。** On WorldArena world modeling, it achieves the best overall EWMScore (63.71) with an 18.4% relative improvement in trajectory accuracy.

**证据没有证明什么。** Future work includes scaling action-free pretraining to internet-scale datasets and extending flow-based planning to longer temporal horizons. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13017v1#S3 — 3 Method; https://arxiv.org/html/2607.13017v1#A1 — Appendix A Implementation Details and Training Pipeline。Evaluation：https://arxiv.org/html/2607.13017v1#A3 — Appendix C Additional RoboTwin Results; https://arxiv.org/html/2607.13017v1#A4 — Appendix D WorldArena Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.13017v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work includes scaling action-free pretraining to internet-scale datasets and extending flow-based planning to longer temporal horizons.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13017:end -->

<!-- review:SF-2026-ARXIV-2607-13027:start -->
### PalmClaw: A Native On-Device Agent Framework for Mobile Phones

<!-- claim:SF-2026-ARXIV-2607-13027:start -->Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13027:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device.

**证据证明什么。** Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13027v1#S3 — 3 Framework。Evaluation：https://arxiv.org/html/2607.13027v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.13027v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.13027v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ModalityDance/PalmClaw/releases/latest, https://github.com/openclaw/openclaw, https://developers.openai.com/codex/cli; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13027:end -->

<!-- review:SF-2026-ARXIV-2607-13028:start -->
### TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale

<!-- claim:SF-2026-ARXIV-2607-13028:start -->Training robust autonomous driving agents requires a simulator fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack that meets these goals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13028:end -->

**为什么进入候选分母。** 摘要首要问题为“Training robust autonomous driving agents requires a simulator fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present TerraZero, a procedural driving simulator and self-play training stack that meets these goals.

**证据证明什么。** On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13028v1#S3.SS1 — 3.1. Designing for Performance。Evaluation：https://arxiv.org/html/2607.13028v1#S6 — 6. Experiments & Results; https://arxiv.org/html/2607.13028v1#S6.SS3 — 6.3. Planner Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.13028v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Emerge-Lab/PufferDrive, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13028:end -->

<!-- review:SF-2026-ARXIV-2607-13034:start -->
### Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution

<!-- claim:SF-2026-ARXIV-2607-13034:start -->Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-13034:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit.

**证据证明什么。** We frame this as a controlled probe of execution redundancy, not a measurement of any deployed agent, and position task-aware execution as a step toward engineering-grounded AI (EGAI)--agents whose effort is anchored in the engineering reality of the task.

**证据没有证明什么。** 10 Conclusion and Future Work We asked whether AI agents know when a task is simple, and found—in a capability-controlled simulator—that a common default (gather maximal context, then act) turns trivial edits into disproportionately expensive audits, with redundancy largest on the simplest tasks . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.13034v1#S4 — 4 The E3 Framework: Estimate, Execute, Expand; https://arxiv.org/html/2607.13034v1#S5.SS1 — 5.1 Design principle: capability-invariant evaluation。Evaluation：https://arxiv.org/html/2607.13034v1#S7 — 7 Results and Analysis; https://arxiv.org/html/2607.13034v1#S5.SS1 — 5.1 Design principle: capability-invariant evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.13034v1#S10 — 10 Conclusion and Future Work; https://arxiv.org/html/2607.13034v1#S9 — 9 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/eejyin/Do-AI-Agents-Know-When-a-Task-Is-Simple-Toward-Complexity-Aware-Reasoning-and-Execution, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：10 Conclusion and Future Work We asked whether AI agents know when a task is simple, and found—in a capability-controlled simulator—that a common default (gather maximal context, then act) turns trivial edits into disproportionately expensive audits, with redundancy largest on the simplest tasks .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-13034:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-11942 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11942 |
| SF-2026-ARXIV-2607-11976 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11976 |
| SF-2026-ARXIV-2607-12121 | score_7_9 | selected | DA-20260715-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260715-01 |
| SF-2026-ARXIV-2607-12188 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12188 |
| SF-2026-ARXIV-2607-12227 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12227 |
| SF-2026-ARXIV-2607-12287 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12287 |
| SF-2026-ARXIV-2607-12505 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12505 |
| SF-2026-ARXIV-2607-12550 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12550 |
| SF-2026-ARXIV-2607-12571 | score_7_9 | selected | DA-20260715-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260715-02 |
| SF-2026-ARXIV-2607-12650 | score_7_9 | selected | DA-20260715-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260715-03 |
| SF-2026-ARXIV-2607-12659 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12659 |
| SF-2026-ARXIV-2607-12696 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12696 |
| SF-2026-ARXIV-2607-12747 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12747 |
| SF-2026-ARXIV-2607-12839 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12839 |
| SF-2026-ARXIV-2607-12875 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12875 |
| SF-2026-ARXIV-2607-12931 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-12931 |
| SF-2026-ARXIV-2607-13027 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-13027 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-11942:start -->
`SF-2026-ARXIV-2607-11942` 的 exact-v1 Deep Review 已保留。其机制为：We present a matched-budget audit of six published compression methods against three trivial baselines on three open 7-9B models (144,300 paired evaluations on RULER-8192; 40,800 on LongBench; 50,000-resample paired bootstrap throughout). 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-11942:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11976:start -->
`SF-2026-ARXIV-2607-11976` 的 exact-v1 Deep Review 已保留。其机制为：Based on this observation, we propose LITETOPK, an efficient fused Indexer-TopK kernel. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-11976:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12188:start -->
`SF-2026-ARXIV-2607-12188` 的 exact-v1 Deep Review 已保留。其机制为：We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant. 为避免挤压 `PLATFORM-COST` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12227:start -->
`SF-2026-ARXIV-2607-12227` 的 exact-v1 Deep Review 已保留。其机制为：Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12227:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12287:start -->
`SF-2026-ARXIV-2607-12287` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we propose a system level acceleration strategy that reduces computation in both perception and action generation. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12287:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12505:start -->
`SF-2026-ARXIV-2607-12505` 的 exact-v1 Deep Review 已保留。其机制为：To this end, we propose a hardware-software co-design framework for N:M sparse ViT inference. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12550:start -->
`SF-2026-ARXIV-2607-12550` 的 exact-v1 Deep Review 已保留。其机制为：Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12550:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12659:start -->
`SF-2026-ARXIV-2607-12659` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12659:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12696:start -->
`SF-2026-ARXIV-2607-12696` 的 exact-v1 Deep Review 已保留。其机制为：We propose \textsc{EcoSpec}, a cost-aware speculative decoding framework that incorporates predicted marginal expert activation cost into draft selection. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12696:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12747:start -->
`SF-2026-ARXIV-2607-12747` 的 exact-v1 Deep Review 已保留。其机制为：Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. 为避免挤压 `PLATFORM-TRACE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12839:start -->
`SF-2026-ARXIV-2607-12839` 的 exact-v1 Deep Review 已保留。其机制为：We present HeteroMosaic, a heterogeneity-first scheduling framework for edge LLM inference. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12839:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12875:start -->
`SF-2026-ARXIV-2607-12875` 的 exact-v1 Deep Review 已保留。其机制为：We present MetaInfer, an LLM-agent system that formulates inference adaptation as route search over a costed execution-adaptation graph. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12875:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12931:start -->
`SF-2026-ARXIV-2607-12931` 的 exact-v1 Deep Review 已保留。其机制为：Motivated by these insights, we introduce RL Exploration Token (ExToken), a simple yet general framework that condition VLA policies on discrete behavioral priors derived from offline demonstrations for structured exploration. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-12931:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13027:start -->
`SF-2026-ARXIV-2607-13027` 的 exact-v1 Deep Review 已保留。其机制为：We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-13027:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260715-01:start -->
### FlashDiff: Efficient Regional Execution and Scheduling for Diffusion Model Serving

**约束变化与机制。** This paper presents FlashDiff, a diffusion serving system that improves inference efficiency through adaptive regional execution and scheduling.

**证明与未证明。** Across real-world image, video, and audio workloads, FlashDiff reduces end-to-end serving latency by 30-97% and improves throughput by 1.2-2.2x. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-12121`。
<!-- analysis:DA-20260715-01:end -->

<!-- analysis:DA-20260715-02:start -->
### TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors

**约束变化与机制。** This footprint motivates TrustVLA, a mechanism-guided inference-time defense that adapts the Dirichlet evidence framework from trusted classification to monitor per-token, per-layer epistemic uncertainty in VLA policies.

**证明与未证明。** Across OpenVLA/LIBERO and $π_{0.5}$ transfer evaluations, TrustVLA reduces attack success while preserving clean-task performance, providing a retraining-free, mechanism-guided defense for visual-triggered VLA backdoors. 但 Counterfactual score drop turns this signal into a localization criterion: a simple additive approximation yields (22) which explains why attention-only can fail (salient task objects need not reduce ), max-drop can over-select destructive regions, and Pareto/closure selection favors compact supports that suppress the mechanism while preserving task context. (a) LIBERO Object (b) LIBERO Spatial (c) LIBERO Goal (d) LIBERO-10 (e) Object, smaller trigger (f) Object, top-left trigger Figure 7: Layer-wise epistemic uncertainty under BadVLA. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Counterfactual score drop turns this signal into a localization criterion: a simple additive approximation yields (22) which explains why attention-only can fail (salient task objects need not reduce ), max-drop can over-select destructive regions, and Pareto/closure selection favors compact supports that suppress the mechanism while preserving task context. (a) LIBERO Object (b) LIBERO Spatial (c) LIBERO Goal (d) LIBERO-10 (e) Object, smaller trigger (f) Object, top-left trigger Figure 7: Layer-wise epistemic uncertainty under BadVLA. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-12571`。
<!-- analysis:DA-20260715-02:end -->

<!-- analysis:DA-20260715-03:start -->
### Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

**约束变化与机制。** We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts.

**证明与未证明。** Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure. 但 The 3-blind-formalizer consensus design is implemented in the runtime but not evaluated here; we defer the consensus study to future work. (ii) Trust artifacts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The 3-blind-formalizer consensus design is implemented in the runtime but not evaluated here; we defer the consensus study to future work. (ii) Trust artifacts. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-12650`。
<!-- analysis:DA-20260715-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260715-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260715 | GAP-20260715-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260715-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260715-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260715-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260715-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260715-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260715-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

427 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：27
- `incremental_method_without_durable_system_delta`：332
- `local_benchmark_without_release_delta`：12
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：2
- `vertical_application_without_system_delta`：53

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 17、No Change 37、Structural 1；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/15/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels](https://arxiv.org/html/2607.11897v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit](https://arxiv.org/html/2607.11942v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [MAGE: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization](https://arxiv.org/html/2607.11944v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Belief-reality separation lives in routing over a shared value slot in language models](https://arxiv.org/pdf/2607.11945v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [When Does Reward Teach State? A Hidden-Automaton Instrument and a Group-Language Warning Signal](https://arxiv.org/html/2607.11953v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Did We Actually Fix It? An Independent Adversarial Stress-Test of Post-Point-Adjustment Evaluation Metrics for Time-Series Anomaly Detection](https://arxiv.org/html/2607.11969v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](https://arxiv.org/html/2607.11976v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](https://arxiv.org/html/2607.12056v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Beyond Test Presence: Assessing the Quality and Robustness of Agent-Generated Tests in Open-Source Projects](https://arxiv.org/html/2607.12068v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking](https://arxiv.org/html/2607.12085v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [TraceSynth: Generating Production-Quality Kernel Traces with Constraint-Guided Diffusion Models](https://arxiv.org/html/2607.12104v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [FlashDiff: Efficient Regional Execution and Scheduling for Diffusion Model Serving](https://arxiv.org/html/2607.12121v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems](https://arxiv.org/html/2607.12188v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [A Threshold Exceedance Framework for CBRN Uplift Evaluation in Frontier Language Models](https://arxiv.org/html/2607.12200v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Overcoming Orchestration Bottlenecks at Exascale: A Decentralized, Policy-Driven Approach for Sim-AI Ensembles](https://arxiv.org/html/2607.12211v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Rethinking the Evaluation of Harness Evolution for Agents](https://arxiv.org/html/2607.12227v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [The GEST-Engine: From Event Graphs to Synthetic Video. A Full Technical Report](https://arxiv.org/html/2607.12231v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs](https://arxiv.org/html/2607.12273v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Auditing Data Leakage in Whole-Slide Image Multimodal Benchmarks](https://arxiv.org/html/2607.12278v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference](https://arxiv.org/html/2607.12287v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/html/2607.12356v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [PM-Bench: Evaluating Prospective Memory in LLM Agents](https://arxiv.org/html/2607.12385v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning](https://arxiv.org/html/2607.12395v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions](https://arxiv.org/html/2607.12406v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models](https://arxiv.org/html/2607.12463v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Realizable N:M Sparse Transformer Inference via Search-Kernel Co-Design](https://arxiv.org/html/2607.12505v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [A JoLT for the KV cache: Near-lossless KV cache compression via joint Lagrangian allocation of Tucker ranks and a rotated residual for llms](https://arxiv.org/html/2607.12550v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/html/2607.12571v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/html/2607.12592v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Inference Pipelines as Operating-System Objects: Priority Scheduling and Constant-Footprint Streaming for Microcontroller Neural Inference](https://arxiv.org/html/2607.12614v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/html/2607.12625v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs](https://arxiv.org/html/2607.12650v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/html/2607.12659v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts](https://arxiv.org/html/2607.12696v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Tracing Agentic Failure from the Flow of Success](https://arxiv.org/html/2607.12747v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Accuracy and Normalized Accuracy under Length Bias: Analysis, Guidelines, and a Bayesian Alternative](https://arxiv.org/html/2607.12767v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/html/2607.12790v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling](https://arxiv.org/html/2607.12831v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](https://arxiv.org/html/2607.12835v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](https://arxiv.org/html/2607.12839v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Automatic Model-Hardware Co-Adaptation for Heterogeneous AI Accelerators](https://arxiv.org/html/2607.12875v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [LLM Judges Can Be Too Generous When There Is No Reference Answer](https://arxiv.org/html/2607.12885v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations](https://arxiv.org/html/2607.12893v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Hy-Embodied-VLM-1.0: Efficient Physical-World Agents](https://arxiv.org/html/2607.12894v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](https://arxiv.org/html/2607.12911v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](https://arxiv.org/html/2607.12931v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models](https://arxiv.org/html/2607.12962v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [The Illusion of Robustness: Aggregate Accuracy Hides Prediction Flips under Task-Irrelevant Context](https://arxiv.org/html/2607.12963v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation](https://arxiv.org/html/2607.12986v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [ChunkFlow: Towards Continuity-Consistent Chunked Policy Learning](https://arxiv.org/html/2607.12992v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model](https://arxiv.org/html/2607.13013v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/html/2607.13017v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/html/2607.13027v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale](https://arxiv.org/html/2607.13028v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04
- [Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution](https://arxiv.org/html/2607.13034v1) — first-public（Asia/Shanghai）：2026-07-15；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、55/55 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
