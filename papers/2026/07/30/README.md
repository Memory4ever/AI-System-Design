# Daily Research — 2026-07-30

**Research Date:** 2026-07-30

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-29 09:00:00 ～ 2026-07-30 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **467** 个 identity；全量 title + abstract 筛选后冻结 **136** 个候选与 **331** 个 family-specific closure，retain rate **29.12%**。exact-v1 Review 为 136/136：Deep 62、Standard 74、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-30 |
| Window End | 2026-07-30 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-30-0900-v2.1-sha256:b29140b215a2cfdd08fc131505971144564c78f76e05e87247681d08987cdfe2 |
| Denominator Frozen At | 2026-09-03T17:05:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260730:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-29T09:00:00+08:00 | 2026-07-30T09:00:00+08:00 | 2026-09-03T17:05:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 467 | SF-2026-ARXIV-2607-26060;SF-2026-ARXIV-2607-26064;SF-2026-ARXIV-2607-26066;SF-2026-ARXIV-2607-26070;SF-2026-ARXIV-2607-26076;SF-2026-ARXIV-2607-26094;SF-2026-ARXIV-2607-26099;SF-2026-ARXIV-2607-26115;SF-2026-ARXIV-2607-26119;SF-2026-ARXIV-2607-26120;SF-2026-ARXIV-2607-26121;SF-2026-ARXIV-2607-26148;SF-2026-ARXIV-2607-26159;SF-2026-ARXIV-2607-26160;SF-2026-ARXIV-2607-26173;SF-2026-ARXIV-2607-26181;SF-2026-ARXIV-2607-26191;SF-2026-ARXIV-2607-26192;SF-2026-ARXIV-2607-26200;SF-2026-ARXIV-2607-26228;SF-2026-ARXIV-2607-26244;SF-2026-ARXIV-2607-26246;SF-2026-ARXIV-2607-26247;SF-2026-ARXIV-2607-26253;SF-2026-ARXIV-2607-26300;SF-2026-ARXIV-2607-26307;SF-2026-ARXIV-2607-26313;SF-2026-ARXIV-2607-26314;SF-2026-ARXIV-2607-26326;SF-2026-ARXIV-2607-26335;SF-2026-ARXIV-2607-26336;SF-2026-ARXIV-2607-26339;SF-2026-ARXIV-2607-26340;SF-2026-ARXIV-2607-26348;SF-2026-ARXIV-2607-26350;SF-2026-ARXIV-2607-26358;SF-2026-ARXIV-2607-26389;SF-2026-ARXIV-2607-26390;SF-2026-ARXIV-2607-26410;SF-2026-ARXIV-2607-26411;SF-2026-ARXIV-2607-26417;SF-2026-ARXIV-2607-26444;SF-2026-ARXIV-2607-26448;SF-2026-ARXIV-2607-26452;SF-2026-ARXIV-2607-26455;SF-2026-ARXIV-2607-26464;SF-2026-ARXIV-2607-26470;SF-2026-ARXIV-2607-26475;SF-2026-ARXIV-2607-26491;SF-2026-ARXIV-2607-26512;SF-2026-ARXIV-2607-26513;SF-2026-ARXIV-2607-26515;SF-2026-ARXIV-2607-26520;SF-2026-ARXIV-2607-26523;SF-2026-ARXIV-2607-26536;SF-2026-ARXIV-2607-26566;SF-2026-ARXIV-2607-26571;SF-2026-ARXIV-2607-26582;SF-2026-ARXIV-2607-26587;SF-2026-ARXIV-2607-26596;SF-2026-ARXIV-2607-26604;SF-2026-ARXIV-2607-26608;SF-2026-ARXIV-2607-26618;SF-2026-ARXIV-2607-26627;SF-2026-ARXIV-2607-26633;SF-2026-ARXIV-2607-26637;SF-2026-ARXIV-2607-26643;SF-2026-ARXIV-2607-26648;SF-2026-ARXIV-2607-26652;SF-2026-ARXIV-2607-26654;SF-2026-ARXIV-2607-26657;SF-2026-ARXIV-2607-26661;SF-2026-ARXIV-2607-26688;SF-2026-ARXIV-2607-26694;SF-2026-ARXIV-2607-26710;SF-2026-ARXIV-2607-26712;SF-2026-ARXIV-2607-26719;SF-2026-ARXIV-2607-26722;SF-2026-ARXIV-2607-26754;SF-2026-ARXIV-2607-26760;SF-2026-ARXIV-2607-26769;SF-2026-ARXIV-2607-26773;SF-2026-ARXIV-2607-26777;SF-2026-ARXIV-2607-26784;SF-2026-ARXIV-2607-26789;SF-2026-ARXIV-2607-26791;SF-2026-ARXIV-2607-26801;SF-2026-ARXIV-2607-26807;SF-2026-ARXIV-2607-26809;SF-2026-ARXIV-2607-26818;SF-2026-ARXIV-2607-26819;SF-2026-ARXIV-2607-26820;SF-2026-ARXIV-2607-26825;SF-2026-ARXIV-2607-26828;SF-2026-ARXIV-2607-26831;SF-2026-ARXIV-2607-26836;SF-2026-ARXIV-2607-26843;SF-2026-ARXIV-2607-26845;SF-2026-ARXIV-2607-26849;SF-2026-ARXIV-2607-26862;SF-2026-ARXIV-2607-26865;SF-2026-ARXIV-2607-26873;SF-2026-ARXIV-2607-26903;SF-2026-ARXIV-2607-26913;SF-2026-ARXIV-2607-26922;SF-2026-ARXIV-2607-26924;SF-2026-ARXIV-2607-26928;SF-2026-ARXIV-2607-26935;SF-2026-ARXIV-2607-26937;SF-2026-ARXIV-2607-26953;SF-2026-ARXIV-2607-26988;SF-2026-ARXIV-2607-26991;SF-2026-ARXIV-2607-26998;SF-2026-ARXIV-2607-27011;SF-2026-ARXIV-2607-27017;SF-2026-ARXIV-2607-27023;SF-2026-ARXIV-2607-27030;SF-2026-ARXIV-2607-27031;SF-2026-ARXIV-2607-27042;SF-2026-ARXIV-2607-27056;SF-2026-ARXIV-2607-27069;SF-2026-ARXIV-2607-27080;SF-2026-ARXIV-2607-27081;SF-2026-ARXIV-2607-27083;SF-2026-ARXIV-2607-27090;SF-2026-ARXIV-2607-27110;SF-2026-ARXIV-2607-27143;SF-2026-ARXIV-2607-27146;SF-2026-ARXIV-2607-27155;SF-2026-ARXIV-2607-27167;SF-2026-ARXIV-2607-27178;SF-2026-ARXIV-2607-27180;SF-2026-ARXIV-2607-27187;SF-2026-ARXIV-2607-27191;SF-2026-ARXIV-2607-27201;SF-2026-ARXIV-2607-27205 | all registered category pages; cross-category dedup complete | 2026-07-30T09:00:00+08:00 | sha256:b29140b215a2cfdd08fc131505971144564c78f76e05e87247681d08987cdfe2 | — |
<!-- coverage:SRC-ARXIV:20260730:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-26060 | arXiv:2607.26060v1 | paper-v1:2607.26060 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26060 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26064 | arXiv:2607.26064v1 | paper-v1:2607.26064 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26064 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26066 | arXiv:2607.26066v1 | paper-v1:2607.26066 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26066 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26070 | arXiv:2607.26070v1 | paper-v1:2607.26070 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26070 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26076 | arXiv:2607.26076v1 | paper-v1:2607.26076 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26076 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26094 | arXiv:2607.26094v1 | paper-v1:2607.26094 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26094 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26099 | arXiv:2607.26099v1 | paper-v1:2607.26099 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26099 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26115 | arXiv:2607.26115v1 | paper-v1:2607.26115 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26115 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26119 | arXiv:2607.26119v1 | paper-v1:2607.26119 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26119 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26120 | arXiv:2607.26120v1 | paper-v1:2607.26120 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26120 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26121 | arXiv:2607.26121v1 | paper-v1:2607.26121 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26121 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26148 | arXiv:2607.26148v1 | paper-v1:2607.26148 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26148 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26159 | arXiv:2607.26159v1 | paper-v1:2607.26159 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26159 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26160 | arXiv:2607.26160v1 | paper-v1:2607.26160 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26160 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26173 | arXiv:2607.26173v1 | paper-v1:2607.26173 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26173 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26181 | arXiv:2607.26181v1 | paper-v1:2607.26181 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26181 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26191 | arXiv:2607.26191v1 | paper-v1:2607.26191 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26191 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26192 | arXiv:2607.26192v1 | paper-v1:2607.26192 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26192 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26200 | arXiv:2607.26200v1 | paper-v1:2607.26200 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26200 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26228 | arXiv:2607.26228v1 | paper-v1:2607.26228 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26228 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26244 | arXiv:2607.26244v1 | paper-v1:2607.26244 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26244 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26246 | arXiv:2607.26246v1 | paper-v1:2607.26246 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26246 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26247 | arXiv:2607.26247v1 | paper-v1:2607.26247 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26247 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26253 | arXiv:2607.26253v1 | paper-v1:2607.26253 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26253 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26300 | arXiv:2607.26300v1 | paper-v1:2607.26300 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26300 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26307 | arXiv:2607.26307v1 | paper-v1:2607.26307 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26307 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26313 | arXiv:2607.26313v1 | paper-v1:2607.26313 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26313 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26314 | arXiv:2607.26314v1 | paper-v1:2607.26314 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26314 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26326 | arXiv:2607.26326v1 | paper-v1:2607.26326 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26326 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26335 | arXiv:2607.26335v1 | paper-v1:2607.26335 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26335 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26336 | arXiv:2607.26336v1 | paper-v1:2607.26336 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26336 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26339 | arXiv:2607.26339v1 | paper-v1:2607.26339 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26339 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26340 | arXiv:2607.26340v1 | paper-v1:2607.26340 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26340 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26348 | arXiv:2607.26348v1 | paper-v1:2607.26348 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26348 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26350 | arXiv:2607.26350v1 | paper-v1:2607.26350 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26350 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26358 | arXiv:2607.26358v1 | paper-v1:2607.26358 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26358 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26389 | arXiv:2607.26389v1 | paper-v1:2607.26389 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26389 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26390 | arXiv:2607.26390v1 | paper-v1:2607.26390 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26390 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26410 | arXiv:2607.26410v1 | paper-v1:2607.26410 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26410 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26411 | arXiv:2607.26411v1 | paper-v1:2607.26411 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26411 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26417 | arXiv:2607.26417v1 | paper-v1:2607.26417 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26417 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26444 | arXiv:2607.26444v1 | paper-v1:2607.26444 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26444 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26448 | arXiv:2607.26448v1 | paper-v1:2607.26448 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26448 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26452 | arXiv:2607.26452v1 | paper-v1:2607.26452 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26452 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26455 | arXiv:2607.26455v1 | paper-v1:2607.26455 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26455 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26464 | arXiv:2607.26464v1 | paper-v1:2607.26464 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26464 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26470 | arXiv:2607.26470v1 | paper-v1:2607.26470 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26470 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26475 | arXiv:2607.26475v1 | paper-v1:2607.26475 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26475 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26491 | arXiv:2607.26491v1 | paper-v1:2607.26491 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26491 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26512 | arXiv:2607.26512v1 | paper-v1:2607.26512 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26512 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26513 | arXiv:2607.26513v1 | paper-v1:2607.26513 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26513 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26515 | arXiv:2607.26515v1 | paper-v1:2607.26515 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26515 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26520 | arXiv:2607.26520v1 | paper-v1:2607.26520 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26520 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26523 | arXiv:2607.26523v1 | paper-v1:2607.26523 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26523 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26536 | arXiv:2607.26536v1 | paper-v1:2607.26536 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26536 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26566 | arXiv:2607.26566v1 | paper-v1:2607.26566 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26566 | self | — | new_in_window | PLATFORM-PRODUCTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26571 | arXiv:2607.26571v1 | paper-v1:2607.26571 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26571 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26582 | arXiv:2607.26582v1 | paper-v1:2607.26582 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26582 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26587 | arXiv:2607.26587v1 | paper-v1:2607.26587 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26587 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26596 | arXiv:2607.26596v1 | paper-v1:2607.26596 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26596 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26604 | arXiv:2607.26604v1 | paper-v1:2607.26604 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26604 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26608 | arXiv:2607.26608v1 | paper-v1:2607.26608 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26608 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26618 | arXiv:2607.26618v1 | paper-v1:2607.26618 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26618 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26627 | arXiv:2607.26627v1 | paper-v1:2607.26627 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26627 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26633 | arXiv:2607.26633v1 | paper-v1:2607.26633 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26633 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26637 | arXiv:2607.26637v1 | paper-v1:2607.26637 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26637 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26643 | arXiv:2607.26643v1 | paper-v1:2607.26643 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26643 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26648 | arXiv:2607.26648v1 | paper-v1:2607.26648 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26648 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26652 | arXiv:2607.26652v1 | paper-v1:2607.26652 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26652 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26654 | arXiv:2607.26654v1 | paper-v1:2607.26654 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26654 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26657 | arXiv:2607.26657v1 | paper-v1:2607.26657 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26657 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26661 | arXiv:2607.26661v1 | paper-v1:2607.26661 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26661 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26688 | arXiv:2607.26688v1 | paper-v1:2607.26688 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26688 | self | — | new_in_window | PLATFORM-PRODUCTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26694 | arXiv:2607.26694v1 | paper-v1:2607.26694 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26694 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26710 | arXiv:2607.26710v1 | paper-v1:2607.26710 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26710 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26712 | arXiv:2607.26712v1 | paper-v1:2607.26712 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26712 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26719 | arXiv:2607.26719v1 | paper-v1:2607.26719 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26719 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26722 | arXiv:2607.26722v1 | paper-v1:2607.26722 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26722 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26754 | arXiv:2607.26754v1 | paper-v1:2607.26754 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26754 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26760 | arXiv:2607.26760v1 | paper-v1:2607.26760 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26760 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26769 | arXiv:2607.26769v1 | paper-v1:2607.26769 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26769 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26773 | arXiv:2607.26773v1 | paper-v1:2607.26773 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26773 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26777 | arXiv:2607.26777v1 | paper-v1:2607.26777 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26777 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26784 | arXiv:2607.26784v1 | paper-v1:2607.26784 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26784 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26789 | arXiv:2607.26789v1 | paper-v1:2607.26789 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26789 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26791 | arXiv:2607.26791v1 | paper-v1:2607.26791 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26791 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26801 | arXiv:2607.26801v1 | paper-v1:2607.26801 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26801 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26807 | arXiv:2607.26807v1 | paper-v1:2607.26807 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26807 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26809 | arXiv:2607.26809v1 | paper-v1:2607.26809 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26809 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26818 | arXiv:2607.26818v1 | paper-v1:2607.26818 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26818 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26819 | arXiv:2607.26819v1 | paper-v1:2607.26819 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26819 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26820 | arXiv:2607.26820v1 | paper-v1:2607.26820 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26820 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26825 | arXiv:2607.26825v1 | paper-v1:2607.26825 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26825 | self | — | new_in_window | WORLDVIEW-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26828 | arXiv:2607.26828v1 | paper-v1:2607.26828 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26828 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26831 | arXiv:2607.26831v1 | paper-v1:2607.26831 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26831 | self | — | new_in_window | MODEL-TOKENIZER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26836 | arXiv:2607.26836v1 | paper-v1:2607.26836 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26836 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26843 | arXiv:2607.26843v1 | paper-v1:2607.26843 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26843 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26845 | arXiv:2607.26845v1 | paper-v1:2607.26845 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26845 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26849 | arXiv:2607.26849v1 | paper-v1:2607.26849 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26849 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26862 | arXiv:2607.26862v1 | paper-v1:2607.26862 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26862 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26865 | arXiv:2607.26865v1 | paper-v1:2607.26865 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26865 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26873 | arXiv:2607.26873v1 | paper-v1:2607.26873 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26873 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26903 | arXiv:2607.26903v1 | paper-v1:2607.26903 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26903 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26913 | arXiv:2607.26913v1 | paper-v1:2607.26913 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26913 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26922 | arXiv:2607.26922v1 | paper-v1:2607.26922 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26922 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26924 | arXiv:2607.26924v1 | paper-v1:2607.26924 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26924 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26928 | arXiv:2607.26928v1 | paper-v1:2607.26928 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26928 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26935 | arXiv:2607.26935v1 | paper-v1:2607.26935 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26935 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26937 | arXiv:2607.26937v1 | paper-v1:2607.26937 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26937 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26953 | arXiv:2607.26953v1 | paper-v1:2607.26953 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26953 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26988 | arXiv:2607.26988v1 | paper-v1:2607.26988 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26988 | self | — | new_in_window | MODEL-SELF-ATTENTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26991 | arXiv:2607.26991v1 | paper-v1:2607.26991 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26991 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26998 | arXiv:2607.26998v1 | paper-v1:2607.26998 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26998 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27011 | arXiv:2607.27011v1 | paper-v1:2607.27011 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27011 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27017 | arXiv:2607.27017v1 | paper-v1:2607.27017 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27017 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27023 | arXiv:2607.27023v1 | paper-v1:2607.27023 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27023 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27030 | arXiv:2607.27030v1 | paper-v1:2607.27030 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27030 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27031 | arXiv:2607.27031v1 | paper-v1:2607.27031 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27031 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27042 | arXiv:2607.27042v1 | paper-v1:2607.27042 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27042 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27056 | arXiv:2607.27056v1 | paper-v1:2607.27056 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27056 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27069 | arXiv:2607.27069v1 | paper-v1:2607.27069 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27069 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27080 | arXiv:2607.27080v1 | paper-v1:2607.27080 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27080 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27081 | arXiv:2607.27081v1 | paper-v1:2607.27081 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27081 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27083 | arXiv:2607.27083v1 | paper-v1:2607.27083 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27083 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27090 | arXiv:2607.27090v1 | paper-v1:2607.27090 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27090 | self | — | new_in_window | INFER-VLLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27110 | arXiv:2607.27110v1 | paper-v1:2607.27110 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27110 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27143 | arXiv:2607.27143v1 | paper-v1:2607.27143 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27143 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27146 | arXiv:2607.27146v1 | paper-v1:2607.27146 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27146 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27155 | arXiv:2607.27155v1 | paper-v1:2607.27155 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27155 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27167 | arXiv:2607.27167v1 | paper-v1:2607.27167 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27167 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27178 | arXiv:2607.27178v1 | paper-v1:2607.27178 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-27178 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27180 | arXiv:2607.27180v1 | paper-v1:2607.27180 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27180 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27187 | arXiv:2607.27187v1 | paper-v1:2607.27187 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27187 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27191 | arXiv:2607.27191v1 | paper-v1:2607.27191 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27191 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27201 | arXiv:2607.27201v1 | paper-v1:2607.27201 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27201 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-27205 | arXiv:2607.27205v1 | paper-v1:2607.27205 | 2026-W31 | 2026-07-30 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-27205 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-26060 | RP-e80a37a107e85a7e | standard | arXiv:2607.26060v1 | SRC-ARXIV@arXiv:2607.26060v1 | https://arxiv.org/html/2607.26060v1#S2 — 2 Synthetic Customer Methodology; https://arxiv.org/html/2607.26060v1#S3 — 3 Framework for Validating a Chatbot Using SCA | https://arxiv.org/html/2607.26060v1#S2.SS1 — 2.1 Evaluation of SCA | https://arxiv.org/html/2607.26060v1#S4 — 4 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26060 | complete |
| SF-2026-ARXIV-2607-26064 | RP-f2b1198c2856b27e | standard | arXiv:2607.26064v1 | SRC-ARXIV@arXiv:2607.26064v1 | https://arxiv.org/html/2607.26064v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26064v1#S1.SS1 — 1.1 The Verification Gap Is Already Wide, and Agents Will Make It Worse | https://arxiv.org/html/2607.26064v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26064v1#S1.SS1 — 1.1 The Verification Gap Is Already Wide, and Agents Will Make It Worse | https://arxiv.org/html/2607.26064v1#S8 — 8 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26064 | complete |
| SF-2026-ARXIV-2607-26066 | RP-c7996ad9ff904a29 | standard | arXiv:2607.26066v1 | SRC-ARXIV@arXiv:2607.26066v1 | https://arxiv.org/html/2607.26066v1#S3 — III Methodology | https://arxiv.org/html/2607.26066v1#S4 — IV Evaluation and Experiments; https://arxiv.org/html/2607.26066v1#S5 — V Results and Analysis | https://arxiv.org/html/2607.26066v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.26066v1#S6 — VI Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26066 | complete |
| SF-2026-ARXIV-2607-26070 | RP-53a68f21a54b9c83 | standard | arXiv:2607.26070v1 | SRC-ARXIV@arXiv:2607.26070v1 | https://arxiv.org/html/2607.26070v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26070v1#S2 — 2 Environment | https://arxiv.org/html/2607.26070v1#S3 — 3 Benchmark Setup; https://arxiv.org/html/2607.26070v1#S4 — 4 Results | https://arxiv.org/html/2607.26070v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26070 | complete |
| SF-2026-ARXIV-2607-26076 | RP-f3b545060b2b3d06 | deep | arXiv:2607.26076v1 | SRC-ARXIV@arXiv:2607.26076v1 | https://arxiv.org/html/2607.26076v1#S3 — 3 System model and consistency target; https://arxiv.org/html/2607.26076v1#S4 — 4 FinCacheServe design | https://arxiv.org/html/2607.26076v1#S6 — 6 Experimental methodology; https://arxiv.org/html/2607.26076v1#S7 — 7 Results | https://arxiv.org/html/2607.26076v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.26076v1#S8 — 8 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26076 | complete |
| SF-2026-ARXIV-2607-26094 | RP-84f54c145217fc07 | standard | arXiv:2607.26094v1 | SRC-ARXIV@arXiv:2607.26094v1 | https://arxiv.org/html/2607.26094v1#Sx4 — Method; https://arxiv.org/html/2607.26094v1#Sx4.SSx1 — Composite Reward Design | https://arxiv.org/html/2607.26094v1#Sx5 — Theoretical Analysis; https://arxiv.org/html/2607.26094v1#Sx6 — Experiments | https://arxiv.org/html/2607.26094v1#Sx8 — Limitations and Future Work; https://arxiv.org/html/2607.26094v1#Sx9 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26094 | complete |
| SF-2026-ARXIV-2607-26099 | RP-66ebfd78b0d29939 | deep | arXiv:2607.26099v1 | SRC-ARXIV@arXiv:2607.26099v1 | https://arxiv.org/html/2607.26099v1#S4 — 4. Method; https://arxiv.org/html/2607.26099v1#S4.SS1 — 4.1. Method Overview | https://arxiv.org/html/2607.26099v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.26099v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.26099v1#S6 — 6. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26099 | complete |
| SF-2026-ARXIV-2607-26115 | RP-d0d074ad3b5a538e | deep | arXiv:2607.26115v1 | SRC-ARXIV@arXiv:2607.26115v1 | https://arxiv.org/html/2607.26115v1#S3.SS2 — \redsemiboldfont 3.2 \redsemiboldfont Threat Model and Affordances; https://arxiv.org/html/2607.26115v1#S7.SS1 — \redsemiboldfont 7.1 \redsemiboldfont Model Training | https://arxiv.org/html/2607.26115v1#A3 — Appendix C Additional Evaluation Details; https://arxiv.org/html/2607.26115v1#S7.SS2 — \redsemiboldfont 7.2 \redsemiboldfont Red-Teaming Evaluations | https://arxiv.org/html/2607.26115v1#S9 — \redsemiboldfont 9 \redsemiboldfont Conclusion and Future Work; https://arxiv.org/html/2607.26115v1#S3.SS2 — \redsemiboldfont 3.2 \redsemiboldfont Threat Model and Affordances | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26115 | complete |
| SF-2026-ARXIV-2607-26119 | RP-a60e3fd3b669fd0f | standard | arXiv:2607.26119v1 | SRC-ARXIV@arXiv:2607.26119v1 | https://arxiv.org/html/2607.26119v1#Sx2.SSx3 — Reasoning Models Exhibit Representation Clarity; https://arxiv.org/html/2607.26119v1#Sx3.SSx3 — Implementation | https://arxiv.org/html/2607.26119v1#Sx3.SSx4 — Results and Analysis; https://arxiv.org/html/2607.26119v1#A1 — Appendix A Additional Token Variability Experimental Details | https://arxiv.org/html/2607.26119v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26119 | complete |
| SF-2026-ARXIV-2607-26120 | RP-306d85dd1c5c383e | standard | arXiv:2607.26120v1 | SRC-ARXIV@arXiv:2607.26120v1 | https://arxiv.org/html/2607.26120v1#S3 — 3 Methodology and Experimental Design | https://arxiv.org/html/2607.26120v1#S3 — 3 Methodology and Experimental Design; https://arxiv.org/html/2607.26120v1#S4 — 4 Results | https://arxiv.org/html/2607.26120v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26120v1#S6 — 6 Conclusions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26120 | complete |
| SF-2026-ARXIV-2607-26121 | RP-166d5b09572df412 | deep | arXiv:2607.26121v1 | SRC-ARXIV@arXiv:2607.26121v1 | https://arxiv.org/html/2607.26121v1#S3.SS2 — 3.2 Framework Design; https://arxiv.org/html/2607.26121v1#S3 — 3 A Four-Layer Framework for Trustworthy Embodied Intelligence | https://arxiv.org/html/2607.26121v1#S6.SS1 — 6.1 Evaluation Objects and Claims; https://arxiv.org/html/2607.26121v1#S6.SS2 — 6.2 Joint Evaluation of Capability and Safety | https://arxiv.org/html/2607.26121v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.26121v1#S2.SS2 — 2.2 Cross-Layer Failure Propagation | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26121 | complete |
| SF-2026-ARXIV-2607-26148 | RP-967c346a4caa99cd | standard | arXiv:2607.26148v1 | SRC-ARXIV@arXiv:2607.26148v1 | https://arxiv.org/html/2607.26148v1#S3.SS1 — 3.1 Model-Directed Interaction; https://arxiv.org/html/2607.26148v1#S4.SS3 — 4.3 Ablations of the Model, Harness, and Interface | https://arxiv.org/html/2607.26148v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.26148v1#A1 — Appendix A Experimental Settings | https://arxiv.org/html/2607.26148v1#A2 — Appendix B Case Study: All 25 Failures; https://arxiv.org/html/2607.26148v1#S4.SS5 — 4.5 Long-Horizon Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26148 | complete |
| SF-2026-ARXIV-2607-26159 | RP-d4c49b371686da80 | deep | arXiv:2607.26159v1 | SRC-ARXIV@arXiv:2607.26159v1 | https://arxiv.org/html/2607.26159v1#S2.SS3 — 2.3 What projectibility adds to neighbouring frameworks; https://arxiv.org/html/2607.26159v1#S4.SS3 — 4.3 A confirmatory local design | https://arxiv.org/html/2607.26159v1#S4.SS1 — 4.1 The source result and the proposed use; https://arxiv.org/html/2607.26159v1#S4.SS4 — 4.4 Hypothetical results and their inferential status | https://arxiv.org/html/2607.26159v1#S8 — 8 Limitations; https://arxiv.org/html/2607.26159v1#S9 — 9 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26159 | complete |
| SF-2026-ARXIV-2607-26160 | RP-c4708e4cbb7c4d3c | standard | arXiv:2607.26160v1 | SRC-ARXIV@arXiv:2607.26160v1 | https://arxiv.org/html/2607.26160v1#A12 — Appendix L Prompt Design; https://arxiv.org/html/2607.26160v1#S3 — 3 Methodology | https://arxiv.org/html/2607.26160v1#A4 — Appendix D Sensitivity Analysis of Score Fusion; https://arxiv.org/html/2607.26160v1#A6 — Appendix F Efficiency Analysis | https://arxiv.org/html/2607.26160v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.26160v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26160 | complete |
| SF-2026-ARXIV-2607-26173 | RP-29235a0fdfa8a76e | standard | arXiv:2607.26173v1 | SRC-ARXIV@arXiv:2607.26173v1 | https://arxiv.org/html/2607.26173v1#A6 — Appendix F Model-Spec Pareto results; https://arxiv.org/html/2607.26173v1#A8.SS1 — H.1 Full off-model/on-model two-by-two | https://arxiv.org/html/2607.26173v1#A6 — Appendix F Model-Spec Pareto results; https://arxiv.org/html/2607.26173v1#A8 — Appendix H Experiment details and provenance | https://arxiv.org/html/2607.26173v1#S6 — 6 Limitations and future work; https://arxiv.org/html/2607.26173v1#A2 — Appendix B GPQA measurement and non-emission failure | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26173 | complete |
| SF-2026-ARXIV-2607-26181 | RP-7ef7babbc6da7b9b | standard | arXiv:2607.26181v1 | SRC-ARXIV@arXiv:2607.26181v1 | https://arxiv.org/html/2607.26181v1#S2.SS2 — 2.2. From Language Models to Agentic Systems; https://arxiv.org/html/2607.26181v1#S3 — 3. Methodology | https://arxiv.org/html/2607.26181v1#S4 — 4. Experimental Evaluation; https://arxiv.org/html/2607.26181v1#S4.SS1 — 4.1. Experimental Setup | https://arxiv.org/html/2607.26181v1#S5 — 5. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26181 | complete |
| SF-2026-ARXIV-2607-26191 | RP-7ccfe1955ea045d0 | standard | arXiv:2607.26191v1 | SRC-ARXIV@arXiv:2607.26191v1 | https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system | https://arxiv.org/html/2607.26191v1#S2 — 2 Trust inflation in evaluation; https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system | https://arxiv.org/html/2607.26191v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26191 | complete |
| SF-2026-ARXIV-2607-26192 | RP-adba65a9128831b9 | deep | arXiv:2607.26192v1 | SRC-ARXIV@arXiv:2607.26192v1 | https://arxiv.org/html/2607.26192v1#S3 — 3 Method: Frozen-Controller Auditing; https://arxiv.org/html/2607.26192v1#S4.SS1 — 4.1 Models and evidence protocol | https://arxiv.org/html/2607.26192v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.26192v1#S2.SS6 — 2.6 Intervention-Based Functional Analysis | https://arxiv.org/html/2607.26192v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26192v1#S6 — 6 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26192 | complete |
| SF-2026-ARXIV-2607-26200 | RP-730e76149f33da81 | deep | arXiv:2607.26200v1 | SRC-ARXIV@arXiv:2607.26200v1 | https://arxiv.org/html/2607.26200v1#A8 — Appendix H Rewrite Method Definitions and Offline Preparation; https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework | https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework; https://arxiv.org/html/2607.26200v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.26200v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26200v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26200 | complete |
| SF-2026-ARXIV-2607-26228 | RP-6a640a9b9c191b44 | standard | arXiv:2607.26228v1 | SRC-ARXIV@arXiv:2607.26228v1 | https://arxiv.org/html/2607.26228v1#S4 — 4 Method: V-Steer; https://arxiv.org/html/2607.26228v1#A1 — Appendix A Additional Algorithmic Details | https://arxiv.org/html/2607.26228v1#A1.SS5 — A.5 V-Auto Experimental Results; https://arxiv.org/html/2607.26228v1#A1.SS3 — A.3 Detailed Complexity Analysis | https://arxiv.org/html/2607.26228v1#S6 — 6 Conclusion, Limitations and Future Work; https://arxiv.org/html/2607.26228v1#S4.SS1 — 4.1 Attention Steering and Its Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26228 | complete |
| SF-2026-ARXIV-2607-26244 | RP-de66d846eb6b49dc | standard | arXiv:2607.26244v1 | SRC-ARXIV@arXiv:2607.26244v1 | https://arxiv.org/html/2607.26244v1#Sx2.SSx2 — Models and Evaluation | https://arxiv.org/html/2607.26244v1#Sx2 — Experimental Setup; https://arxiv.org/html/2607.26244v1#Sx2.SSx2 — Models and Evaluation | https://arxiv.org/html/2607.26244v1#Sx10 — Conclusion; https://arxiv.org/html/2607.26244v1#Sx7 — Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26244 | complete |
| SF-2026-ARXIV-2607-26246 | RP-16e79863e2ddcc5b | standard | arXiv:2607.26246v1 | SRC-ARXIV@arXiv:2607.26246v1 | https://arxiv.org/html/2607.26246v1#A3 — Appendix C Implementation Details; https://arxiv.org/html/2607.26246v1#A4.SS2 — D.2 Performance with Different Scales of Base Models | https://arxiv.org/html/2607.26246v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.26246v1#A4.SS1 — D.1 Runtime Analysis | https://arxiv.org/html/2607.26246v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26246 | complete |
| SF-2026-ARXIV-2607-26247 | RP-a8a4f274a44e4fb6 | standard | arXiv:2607.26247v1 | SRC-ARXIV@arXiv:2607.26247v1 | https://arxiv.org/html/2607.26247v1#Sx3 — Method | https://arxiv.org/html/2607.26247v1#Sx4 — Experiments; https://arxiv.org/html/2607.26247v1#Sx4.SSx1 — Results | https://arxiv.org/html/2607.26247v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26247 | complete |
| SF-2026-ARXIV-2607-26253 | RP-b151ae17e71e6aaf | deep | arXiv:2607.26253v1 | SRC-ARXIV@arXiv:2607.26253v1 | https://arxiv.org/html/2607.26253v1#A1 — Appendix A Use of Large Language Models; https://arxiv.org/html/2607.26253v1#A4 — Appendix D Algorithm and Implementation Details | https://arxiv.org/html/2607.26253v1#A3 — Appendix C Proofs and Theoretical Analysis; https://arxiv.org/html/2607.26253v1#A5 — Appendix E Detailed Experimental Setup | https://arxiv.org/html/2607.26253v1#A7 — Appendix G Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.26253v1#S5 — 5 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26253 | complete |
| SF-2026-ARXIV-2607-26300 | RP-0944748a54614af0 | standard | arXiv:2607.26300v1 | SRC-ARXIV@arXiv:2607.26300v1 | https://arxiv.org/html/2607.26300v1#S4 — 4 System evaluation | https://arxiv.org/html/2607.26300v1#A2 — Appendix B Statistical Testing and Analysis; https://arxiv.org/html/2607.26300v1#A3 — Appendix C Cost Analysis For Manager Steering | https://arxiv.org/html/2607.26300v1#S5 — 5 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26300 | complete |
| SF-2026-ARXIV-2607-26307 | RP-78c1afc3dc49c94a | standard | arXiv:2607.26307v1 | SRC-ARXIV@arXiv:2607.26307v1 | https://arxiv.org/html/2607.26307v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.26307v1#S2.SS3 — 2.3 Coding Agent Systems | https://arxiv.org/html/2607.26307v1#S6 — 6 Experimental Evaluation; https://arxiv.org/html/2607.26307v1#S2.SS7 — 2.7 Benchmarks and Specification Mining | https://arxiv.org/html/2607.26307v1#S8 — 8 Discussion; https://arxiv.org/html/2607.26307v1#S8.SS3 — 8.3 Threats to Evaluation Validity | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26307 | complete |
| SF-2026-ARXIV-2607-26313 | RP-936ee344f1f73afc | deep | arXiv:2607.26313v1 | SRC-ARXIV@arXiv:2607.26313v1 | https://arxiv.org/html/2607.26313v1#S3 — 3 Architecture | https://arxiv.org/html/2607.26313v1#A1.SS5 — A.5 Robustness: leave-one-class-out, ablations, and threshold sensitivity; https://arxiv.org/html/2607.26313v1#S7 — 7 Results (H1–H4) | https://arxiv.org/html/2607.26313v1#S12 — 12 Conclusion; https://arxiv.org/html/2607.26313v1#S9 — 9 Threats to validity | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26313 | complete |
| SF-2026-ARXIV-2607-26314 | RP-066e229960145b14 | standard | arXiv:2607.26314v1 | SRC-ARXIV@arXiv:2607.26314v1 | https://arxiv.org/html/2607.26314v1#Ax1.SSx1 — A.1 Agent System Prompt; https://arxiv.org/html/2607.26314v1#S2 — 2 Methodology | https://arxiv.org/html/2607.26314v1#S2.SS4 — 2.4 The Defining Experiment; https://arxiv.org/html/2607.26314v1#S2.SS6 — 2.6 Evaluation Metrics | https://arxiv.org/html/2607.26314v1#S4.SS3 — 4.3 Exploratory Qualitative Failure Mechanisms; https://arxiv.org/html/2607.26314v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26314 | complete |
| SF-2026-ARXIV-2607-26326 | RP-4ada50d21cb7ef32 | standard | arXiv:2607.26326v1 | SRC-ARXIV@arXiv:2607.26326v1 | https://arxiv.org/html/2607.26326v1#S4.SS1 — 4.1 Designing the Multimodal Context-Sensitivity Task; https://arxiv.org/html/2607.26326v1#A3 — Appendix C Implementation | https://arxiv.org/html/2607.26326v1#A2 — Appendix B Benchmark Composition and Curation; https://arxiv.org/html/2607.26326v1#A4 — Appendix D Extra reconstruction results and exact-match results | https://arxiv.org/html/2607.26326v1#A1 — Appendix A Limitations and Future work; https://arxiv.org/html/2607.26326v1#S8 — 8 Conclusions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26326 | complete |
| SF-2026-ARXIV-2607-26335 | RP-ba861b579e359034 | deep | arXiv:2607.26335v1 | SRC-ARXIV@arXiv:2607.26335v1 | https://arxiv.org/html/2607.26335v1#S3 — 3. Design; https://arxiv.org/html/2607.26335v1#S3.SS4 — 3.4. LLM Prefill Across Three Architectures | https://arxiv.org/html/2607.26335v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.26335v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.26335v1#S4.SS6 — 4.6. Failure and Fallback; https://arxiv.org/html/2607.26335v1#S7 — 7. Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26335 | complete |
| SF-2026-ARXIV-2607-26336 | RP-eed6da4c80cab0dd | standard | arXiv:2607.26336v1 | SRC-ARXIV@arXiv:2607.26336v1 | https://arxiv.org/html/2607.26336v1#A16 — Appendix P Neural Architecture Design and Baselines; https://arxiv.org/html/2607.26336v1#S4 — 4 Framework and Methodology | https://arxiv.org/html/2607.26336v1#A20.SS3 — T.3 Evaluation Results: High sample complexity experiments; https://arxiv.org/html/2607.26336v1#A21.SS2 — U.2 Evaluation Results: High sample complexity experiments | https://arxiv.org/html/2607.26336v1#S6 — 6 CONCLUSION AND LIMITATIONS; https://arxiv.org/html/2607.26336v1#A24.SS4 — X.4 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26336 | complete |
| SF-2026-ARXIV-2607-26339 | RP-db44b6b25503c101 | standard | arXiv:2607.26339v1 | SRC-ARXIV@arXiv:2607.26339v1 | https://arxiv.org/html/2607.26339v1#S3 — 3 Methods; https://arxiv.org/html/2607.26339v1#S3.SS1 — 3.1 Overall Architecture | https://arxiv.org/html/2607.26339v1#A1 — Appendix A Full Baseline and ZKIP Evaluation Results; https://arxiv.org/html/2607.26339v1#A4 — Appendix D Supervised Poison Classification Ablations | https://arxiv.org/html/2607.26339v1#A2 — Appendix B Threat Model Scope; https://arxiv.org/html/2607.26339v1#S4.SS1 — 4.1 Experimental Setup and Threat Model | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26339 | complete |
| SF-2026-ARXIV-2607-26340 | RP-e9582d6331af684b | deep | arXiv:2607.26340v1 | SRC-ARXIV@arXiv:2607.26340v1 | https://arxiv.org/html/2607.26340v1#S2.SS3 — 2.3. Frameworks; https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures | https://arxiv.org/html/2607.26340v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26340 | complete |
| SF-2026-ARXIV-2607-26348 | RP-0a22b29f8481dc5e | deep | arXiv:2607.26348v1 | SRC-ARXIV@arXiv:2607.26348v1 | https://arxiv.org/html/2607.26348v1#S2.SS6 — 2.6 Decision-support validity and expert-system validation; https://arxiv.org/html/2607.26348v1#A1 — Appendix A Model call settings | https://arxiv.org/html/2607.26348v1#S2.SS2 — 2.2 Survey-simulation benchmarks and cross-cultural value modeling; https://arxiv.org/html/2607.26348v1#S4 — 4 Results | https://arxiv.org/html/2607.26348v1#S4.SS6 — 4.6 RQ5: Both failures transfer across domains; https://arxiv.org/html/2607.26348v1#S5 — 5 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26348 | complete |
| SF-2026-ARXIV-2607-26350 | RP-954723be5e26e28a | standard | arXiv:2607.26350v1 | SRC-ARXIV@arXiv:2607.26350v1 | https://arxiv.org/html/2607.26350v1#S3.SS1 — 3.1 Experimental Design | https://arxiv.org/html/2607.26350v1#S3 — 3 Evaluation Setup; https://arxiv.org/html/2607.26350v1#S3.SS1 — 3.1 Experimental Design | https://arxiv.org/html/2607.26350v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26350 | complete |
| SF-2026-ARXIV-2607-26358 | RP-7ebc23e10405d8ba | standard | arXiv:2607.26358v1 | SRC-ARXIV@arXiv:2607.26358v1 | https://arxiv.org/html/2607.26358v1#A3.SS2 — C.2 Model Auditing; https://arxiv.org/html/2607.26358v1#S5.SS2 — 5.2 Model Auditing | https://arxiv.org/html/2607.26358v1#A3 — Appendix C Appendix for Section 5 : Experiments; https://arxiv.org/html/2607.26358v1#S5 — 5 Experiments | https://arxiv.org/html/2607.26358v1#S7 — 7 Conclusions and Future Research | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26358 | complete |
| SF-2026-ARXIV-2607-26389 | RP-59f14bf372848b92 | standard | arXiv:2607.26389v1 | SRC-ARXIV@arXiv:2607.26389v1 | https://arxiv.org/html/2607.26389v1#S3 — 3 Methodology | https://arxiv.org/html/2607.26389v1#A3 — Appendix C Transfer Benchmark: BIG5-CHAT; https://arxiv.org/html/2607.26389v1#A7 — Appendix G Full Result Tables | https://arxiv.org/html/2607.26389v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26389 | complete |
| SF-2026-ARXIV-2607-26390 | RP-0ebf2caa068286b2 | standard | arXiv:2607.26390v1 | SRC-ARXIV@arXiv:2607.26390v1 | https://arxiv.org/html/2607.26390v1#S1 — 1. Introduction; https://arxiv.org/html/2607.26390v1#S2 — 2. Study Setup | https://arxiv.org/html/2607.26390v1#S2.SS3 — 2.3. Data Analysis; https://arxiv.org/html/2607.26390v1#S2 — 2. Study Setup | https://arxiv.org/html/2607.26390v1#S7 — 7. Threats to Validity | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26390 | complete |
| SF-2026-ARXIV-2607-26410 | RP-bf74d70bcf180fc2 | standard | arXiv:2607.26410v1 | SRC-ARXIV@arXiv:2607.26410v1 | https://arxiv.org/html/2607.26410v1#S3 — 3 The Voice Memory Method | https://arxiv.org/html/2607.26410v1#S7 — 7 Analysis: Meaning versus Surface Error; https://arxiv.org/html/2607.26410v1#S7.SS3 — 7.3 Error Analysis | https://arxiv.org/html/2607.26410v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26410v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26410 | complete |
| SF-2026-ARXIV-2607-26411 | RP-a3fb7d8055826d87 | standard | arXiv:2607.26411v1 | SRC-ARXIV@arXiv:2607.26411v1 | https://arxiv.org/html/2607.26411v1#A1.SS4 — A.4 LLM Steering Methods Detail; https://arxiv.org/html/2607.26411v1#A2.SS4 — B.4 Full Evaluation of Understanding-to-Generation Steering across UMM Architectures | https://arxiv.org/html/2607.26411v1#A3 — Appendix C Additional Ablation Study and Analysis; https://arxiv.org/html/2607.26411v1#A1 — Appendix A Experiment Details | https://arxiv.org/html/2607.26411v1#A4.SS2 — D.2 Failure Case Analysis; https://arxiv.org/html/2607.26411v1#A6 — Appendix F Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26411 | complete |
| SF-2026-ARXIV-2607-26417 | RP-a7914b5e2c1fbc6a | deep | arXiv:2607.26417v1 | SRC-ARXIV@arXiv:2607.26417v1 | https://arxiv.org/html/2607.26417v1#Sx3 — Method | https://arxiv.org/html/2607.26417v1#Sx4 — Experimental Setup; https://arxiv.org/html/2607.26417v1#Sx5 — Results | https://arxiv.org/html/2607.26417v1#Sx6 — Discussion; https://arxiv.org/html/2607.26417v1#Sx7 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26417 | complete |
| SF-2026-ARXIV-2607-26444 | RP-aefa4f31970b7183 | deep | arXiv:2607.26444v1 | SRC-ARXIV@arXiv:2607.26444v1 | https://arxiv.org/html/2607.26444v1#S2.SS1 — 2.1. Supernode Architectures; https://arxiv.org/html/2607.26444v1#S4 — 4. Design Overview | https://arxiv.org/html/2607.26444v1#A1 — Appendix A Extended Microbenchmark; https://arxiv.org/html/2607.26444v1#A3 — Appendix C Workload Partitioning Overhead Analysis | https://arxiv.org/html/2607.26444v1#S11 — 11. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26444 | complete |
| SF-2026-ARXIV-2607-26448 | RP-3fcafca42a9e9dab | deep | arXiv:2607.26448v1 | SRC-ARXIV@arXiv:2607.26448v1 | https://arxiv.org/html/2607.26448v1#S4 — 4 Method | https://arxiv.org/html/2607.26448v1#A7 — Appendix G Statistical Analysis and Evaluation Scope; https://arxiv.org/html/2607.26448v1#A7.SS1 — G.1 Evaluation and statistical analysis | https://arxiv.org/html/2607.26448v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26448 | complete |
| SF-2026-ARXIV-2607-26452 | RP-86b8ad11ba339b08 | deep | arXiv:2607.26452v1 | SRC-ARXIV@arXiv:2607.26452v1 | https://arxiv.org/html/2607.26452v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26452v1#S2 — 2 Related Work | https://arxiv.org/html/2607.26452v1#S5 — 5 Experiments | https://arxiv.org/html/2607.26452v1#S7 — 7 Discussion and Conclusion; https://arxiv.org/html/2607.26452v1#S6 — 6 Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26452 | complete |
| SF-2026-ARXIV-2607-26455 | RP-56a9c7f0b2552ad3 | standard | arXiv:2607.26455v1 | SRC-ARXIV@arXiv:2607.26455v1 | https://arxiv.org/html/2607.26455v1#S3 — 3 Methodology | https://arxiv.org/html/2607.26455v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.26455v1#S5 — 5 Experiments | https://arxiv.org/html/2607.26455v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26455 | complete |
| SF-2026-ARXIV-2607-26464 | RP-e17f71cb727af964 | deep | arXiv:2607.26464v1 | SRC-ARXIV@arXiv:2607.26464v1 | https://arxiv.org/html/2607.26464v1#S2 — 2 The PUDA Architecture; https://arxiv.org/html/2607.26464v1#S2.SS1 — 2.1 Design Philosophy | https://arxiv.org/html/2607.26464v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26464v1#S2 — 2 The PUDA Architecture | https://arxiv.org/html/2607.26464v1#S6 — 6 Conclusions and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26464 | complete |
| SF-2026-ARXIV-2607-26470 | RP-4d4a52faa4c05189 | standard | arXiv:2607.26470v1 | SRC-ARXIV@arXiv:2607.26470v1 | https://arxiv.org/html/2607.26470v1#A2.SS1 — B.1 Architecture; https://arxiv.org/html/2607.26470v1#S3 — 3 Method | https://arxiv.org/html/2607.26470v1#A3 — Appendix C Inference and Evaluation; https://arxiv.org/html/2607.26470v1#A3.SS5 — C.5 Evaluation Protocol | https://arxiv.org/html/2607.26470v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26470 | complete |
| SF-2026-ARXIV-2607-26475 | RP-b2865d8e93ffca9e | deep | arXiv:2607.26475v1 | SRC-ARXIV@arXiv:2607.26475v1 | https://arxiv.org/html/2607.26475v1#S5 — 5. DualDecoder Design; https://arxiv.org/html/2607.26475v1#S5.SS1 — 5.1. System Overview | https://arxiv.org/html/2607.26475v1#S3.SS2 — 3.2. Memory Capacity Analysis; https://arxiv.org/html/2607.26475v1#S6 — 6. Evaluation | https://arxiv.org/html/2607.26475v1#S8 — 8. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26475 | complete |
| SF-2026-ARXIV-2607-26491 | RP-56592054e674695b | deep | arXiv:2607.26491v1 | SRC-ARXIV@arXiv:2607.26491v1 | https://arxiv.org/html/2607.26491v1#S2.SS1 — 2.1. LLM Serving Architecture; https://arxiv.org/html/2607.26491v1#S3 — 3. Proposed LLMET Framework | https://arxiv.org/html/2607.26491v1#S4 — 4. Evaluations | https://arxiv.org/html/2607.26491v1#S6 — 6. Conclusion and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26491 | complete |
| SF-2026-ARXIV-2607-26512 | RP-dce013eed0dafaa1 | standard | arXiv:2607.26512v1 | SRC-ARXIV@arXiv:2607.26512v1 | https://arxiv.org/html/2607.26512v1#S5.SS3 — 5.3 Positioning against adjacent systems | https://arxiv.org/html/2607.26512v1#S2.SS1 — 2.1 External claim-verification benchmarks; https://arxiv.org/html/2607.26512v1#S2.SS3 — 2.3 Agent evaluation through artifacts | https://arxiv.org/html/2607.26512v1#S6 — 6 Discussion; https://arxiv.org/html/2607.26512v1#S7 — 7 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26512 | complete |
| SF-2026-ARXIV-2607-26513 | RP-737e397a8ca20326 | standard | arXiv:2607.26513v1 | SRC-ARXIV@arXiv:2607.26513v1 | https://arxiv.org/html/2607.26513v1#A1.SS1 — A.1 Analytic Concept System; https://arxiv.org/html/2607.26513v1#A1.SS2 — A.2 Network Architecture | https://arxiv.org/html/2607.26513v1#A2 — Appendix B Experimental Setup; https://arxiv.org/html/2607.26513v1#S4 — 4 Experiment | https://arxiv.org/html/2607.26513v1#A4 — Appendix D Limitations and Future Work; https://arxiv.org/html/2607.26513v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26513 | complete |
| SF-2026-ARXIV-2607-26515 | RP-6972bfb067a03a0d | deep | arXiv:2607.26515v1 | SRC-ARXIV@arXiv:2607.26515v1 | https://arxiv.org/html/2607.26515v1#S4 — 4 Method | https://arxiv.org/html/2607.26515v1#S5 — 5 Experiments; https://arxiv.org/html/2607.26515v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.26515v1#S6 — 6 Limitations and Future Directions; https://arxiv.org/html/2607.26515v1#S7 — 7 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26515 | complete |
| SF-2026-ARXIV-2607-26520 | RP-044b4dba7abc2f70 | deep | arXiv:2607.26520v1 | SRC-ARXIV@arXiv:2607.26520v1 | https://arxiv.org/html/2607.26520v1#S3.SS1 — III-A Data Model; https://arxiv.org/html/2607.26520v1#S3.SS2 — III-B Bitemporal Model; https://arxiv.org/html/2607.26520v1#S4.SS2 — IV-B Agent Tool-Use Loop | https://arxiv.org/html/2607.26520v1#S5.SS1 — V-A Benchmark and Protocol; https://arxiv.org/html/2607.26520v1#S5.SS2 — V-B Results; https://arxiv.org/html/2607.26520v1#S5.SS5 — V-E Temporal Reasoning and the Dilution Effect | https://arxiv.org/html/2607.26520v1#S6 — VI Conclusion; https://arxiv.org/html/2607.26520v1#S6.SS2 — VI-B Future Directions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26520 | complete |
| SF-2026-ARXIV-2607-26523 | RP-3483d67d28c9b38f | standard | arXiv:2607.26523v1 | SRC-ARXIV@arXiv:2607.26523v1 | https://arxiv.org/html/2607.26523v1#S3 — 3 Architecture | https://arxiv.org/html/2607.26523v1#A3 — Appendix C Historical depth-line result; https://arxiv.org/html/2607.26523v1#A5 — Appendix E Preliminary scaling experiment | https://arxiv.org/html/2607.26523v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.26523v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26523 | complete |
| SF-2026-ARXIV-2607-26536 | RP-fe204d79bb15cdbe | standard | arXiv:2607.26536v1 | SRC-ARXIV@arXiv:2607.26536v1 | https://arxiv.org/html/2607.26536v1#S3 — 3 Method; https://arxiv.org/html/2607.26536v1#S4.SS4 — 4.4 Full Cross-Model Stress Test | https://arxiv.org/html/2607.26536v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26536v1#S4.SS2 — 4.2 Gate Ablations | https://arxiv.org/html/2607.26536v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26536v1#S6 — 6 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26536 | complete |
| SF-2026-ARXIV-2607-26566 | RP-dbcdb25fde9ff18b | deep | arXiv:2607.26566v1 | SRC-ARXIV@arXiv:2607.26566v1 | https://arxiv.org/html/2607.26566v1#S3 — 3. Motivation and System Overview; https://arxiv.org/html/2607.26566v1#S3.SS2 — 3.2. System Overview | https://arxiv.org/html/2607.26566v1#S8 — 8. Evaluation; https://arxiv.org/html/2607.26566v1#S8.SS2 — 8.2. End-to-end Evaluation | https://arxiv.org/html/2607.26566v1#S10 — 10. Conclusions; https://arxiv.org/html/2607.26566v1#S2.SS3 — 2.3. Limitations of Current Practices | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26566 | complete |
| SF-2026-ARXIV-2607-26571 | RP-99005d673981762a | standard | arXiv:2607.26571v1 | SRC-ARXIV@arXiv:2607.26571v1 | https://arxiv.org/html/2607.26571v1#A3 — Appendix C Model Architecture Details; https://arxiv.org/html/2607.26571v1#S2 — 2 Methodology | https://arxiv.org/html/2607.26571v1#S4 — 4 Results and Evaluation; https://arxiv.org/html/2607.26571v1#S3 — 3 Evaluation Setup and Assumptions | https://arxiv.org/html/2607.26571v1#S5 — 5 Limitations and Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26571 | complete |
| SF-2026-ARXIV-2607-26582 | RP-57709ee1323e4c24 | deep | arXiv:2607.26582v1 | SRC-ARXIV@arXiv:2607.26582v1 | https://arxiv.org/html/2607.26582v1#S3 — 3 The Portability Audit; https://arxiv.org/html/2607.26582v1#S4 — 4 Mechanism: Level and Sharpness Are Complementary Evidence; https://arxiv.org/html/2607.26582v1#S5 — 5 From Diagnosis to Deployment: The Complementary Evidence Guard | https://arxiv.org/html/2607.26582v1#S4.SS1 — 4.1 External Semantic Evidence Depends on Corpus Coverage; https://arxiv.org/html/2607.26582v1#A1 — Appendix A Appendix Overview and Organization; https://arxiv.org/html/2607.26582v1#A6 — Appendix F Protected All-Domain Audit | https://arxiv.org/html/2607.26582v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.26582v1#A5.SS1 — E.1 Non-compensatory property of CEG | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26582 | complete |
| SF-2026-ARXIV-2607-26587 | RP-c8e86159bcbe95b5 | deep | arXiv:2607.26587v1 | SRC-ARXIV@arXiv:2607.26587v1 | https://arxiv.org/html/2607.26587v1#S4 — 4 Study Design; https://arxiv.org/html/2607.26587v1#S3.SSx2 — Independent Implementations | https://arxiv.org/html/2607.26587v1#S5 — 5 Results; https://arxiv.org/html/2607.26587v1#S4 — 4 Study Design | https://arxiv.org/html/2607.26587v1#S7 — 7 Scope and Limitations; https://arxiv.org/html/2607.26587v1#S9 — 9 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26587 | complete |
| SF-2026-ARXIV-2607-26596 | RP-9f204956a59b36ef | standard | arXiv:2607.26596v1 | SRC-ARXIV@arXiv:2607.26596v1 | https://arxiv.org/html/2607.26596v1#S5.SS1 — 5.1 Implications for MLLM Architecture Design; https://arxiv.org/html/2607.26596v1#A1 — Appendix A Architecture Details | https://arxiv.org/html/2607.26596v1#A2 — Appendix B Detailed Benchmark Results; https://arxiv.org/html/2607.26596v1#A3 — Appendix C Computational Cost Analysis | https://arxiv.org/html/2607.26596v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.26596v1#S5 — 5 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26596 | complete |
| SF-2026-ARXIV-2607-26604 | RP-40cf8a8e93eee8d2 | deep | arXiv:2607.26604v1 | SRC-ARXIV@arXiv:2607.26604v1 | https://arxiv.org/html/2607.26604v1#S3 — 3 Method; https://arxiv.org/html/2607.26604v1#S3.SS1 — 3.1 Problem Formulation and Framework Overview | https://arxiv.org/html/2607.26604v1#A2 — Appendix B Complete Experimental Results; https://arxiv.org/html/2607.26604v1#A1 — Appendix A Experimental Details | https://arxiv.org/html/2607.26604v1#S5 — 5 Limitations; https://arxiv.org/html/2607.26604v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26604 | complete |
| SF-2026-ARXIV-2607-26608 | RP-5d06fbc9caa404f1 | standard | arXiv:2607.26608v1 | SRC-ARXIV@arXiv:2607.26608v1 | https://arxiv.org/html/2607.26608v1#Sx3 — Method; https://arxiv.org/html/2607.26608v1#A2.SS1 — B.1 Models and Configurations | https://arxiv.org/html/2607.26608v1#A2 — Appendix B Experimental and Evaluation Details; https://arxiv.org/html/2607.26608v1#A4 — Appendix D Complete Benchmark-Wise Best-of-Sweep Results | https://arxiv.org/html/2607.26608v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26608 | complete |
| SF-2026-ARXIV-2607-26618 | RP-0f79e180b1a63454 | deep | arXiv:2607.26618v1 | SRC-ARXIV@arXiv:2607.26618v1 | https://arxiv.org/html/2607.26618v1#Sx3 — Method; https://arxiv.org/html/2607.26618v1#A1 — Appendix A Implementation and Reproducibility Details | https://arxiv.org/html/2607.26618v1#A3 — Appendix C Theoretical Analysis; https://arxiv.org/html/2607.26618v1#Sx4 — Experiments | https://arxiv.org/html/2607.26618v1#Sx5 — Limitations; https://arxiv.org/html/2607.26618v1#Sx6 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26618 | complete |
| SF-2026-ARXIV-2607-26627 | RP-7f669cb04422b2ec | deep | arXiv:2607.26627v1 | SRC-ARXIV@arXiv:2607.26627v1 | https://arxiv.org/html/2607.26627v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26627v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.26627v1#A2 — Appendix B Verification Analysis; https://arxiv.org/html/2607.26627v1#A3 — Appendix C Extended Results | https://arxiv.org/html/2607.26627v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.26627v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26627 | complete |
| SF-2026-ARXIV-2607-26633 | RP-689514b72ec06407 | deep | arXiv:2607.26633v1 | SRC-ARXIV@arXiv:2607.26633v1 | https://arxiv.org/html/2607.26633v1#S3 — 3. Design Principles and Architecture Overview; https://arxiv.org/html/2607.26633v1#S5.SS1 — 5.1. NELSSA System Architecture | https://arxiv.org/html/2607.26633v1#S8 — 8. Experimental Results; https://arxiv.org/html/2607.26633v1#S7 — 7. Evaluation Methodology | https://arxiv.org/html/2607.26633v1#S10 — 10. Discussion; https://arxiv.org/html/2607.26633v1#S11 — 11. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26633 | complete |
| SF-2026-ARXIV-2607-26637 | RP-75dac2372640129d | deep | arXiv:2607.26637v1 | SRC-ARXIV@arXiv:2607.26637v1 | https://arxiv.org/html/2607.26637v1#A2 — Appendix B Example Memory Filesystems; https://arxiv.org/html/2607.26637v1#S2 — 2 Formalizing Filesystem-Based Agent Memory | https://arxiv.org/html/2607.26637v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.26637v1#A3 — Appendix C Experimental Details | https://arxiv.org/html/2607.26637v1#S5 — 5 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26637 | complete |
| SF-2026-ARXIV-2607-26643 | RP-c64179453982bba5 | deep | arXiv:2607.26643v1 | SRC-ARXIV@arXiv:2607.26643v1 | https://arxiv.org/html/2607.26643v1#Sx3 — Methodology | https://arxiv.org/html/2607.26643v1#A1.SSx2 — Cross-Benchmark Patterns; https://arxiv.org/html/2607.26643v1#A2.SSx3 — 3. Failure Mode Cluster Analysis | https://arxiv.org/html/2607.26643v1#A2.SSx3 — 3. Failure Mode Cluster Analysis; https://arxiv.org/html/2607.26643v1#Sx4.SSx5 — Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26643 | complete |
| SF-2026-ARXIV-2607-26648 | RP-f8a5a00b77191f79 | deep | arXiv:2607.26648v1 | SRC-ARXIV@arXiv:2607.26648v1 | https://arxiv.org/html/2607.26648v1#S2 — 2 Method; https://arxiv.org/html/2607.26648v1#S4.SS2 — 4.2 Sequence modeling hits a ceiling | https://arxiv.org/html/2607.26648v1#S4 — 4 Experiments | https://arxiv.org/html/2607.26648v1#S6 — 6 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26648 | complete |
| SF-2026-ARXIV-2607-26652 | RP-cbda01eb99d357bc | deep | arXiv:2607.26652v1 | SRC-ARXIV@arXiv:2607.26652v1 | https://arxiv.org/html/2607.26652v1#S2 — 2. Architecture; https://arxiv.org/html/2607.26652v1#S3 — 3. Implementation and Usage Workflow | https://arxiv.org/html/2607.26652v1#S4 — 4. Preliminary Evaluation | https://arxiv.org/html/2607.26652v1#S6 — 6. Conclusions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26652 | complete |
| SF-2026-ARXIV-2607-26654 | RP-f6c9ec5fe1cebd99 | standard | arXiv:2607.26654v1 | SRC-ARXIV@arXiv:2607.26654v1 | https://arxiv.org/html/2607.26654v1#S2.SS2 — 2.2 Constitutional Approaches to Alignment; https://arxiv.org/html/2607.26654v1#S3 — 3 Method | https://arxiv.org/html/2607.26654v1#A3 — Appendix C Centrality Analysis: Additional Detail; https://arxiv.org/html/2607.26654v1#A6 — Appendix F Evaluation: Extended Detail | https://arxiv.org/html/2607.26654v1#S5.SS6 — 5.6 Limitations and Future Work.; https://arxiv.org/html/2607.26654v1#A3.SS5 — C.5 Limitations of the Centrality Measure | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26654 | complete |
| SF-2026-ARXIV-2607-26657 | RP-50f8c2aa5fdb3c01 | deep | arXiv:2607.26657v1 | SRC-ARXIV@arXiv:2607.26657v1 | https://arxiv.org/html/2607.26657v1#S4 — 4 Method; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration | https://arxiv.org/html/2607.26657v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration | https://arxiv.org/html/2607.26657v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.26657v1#A2.SS3 — B.3 Future-Video Evaluation | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26657 | complete |
| SF-2026-ARXIV-2607-26661 | RP-deac3b4c0230c28d | standard | arXiv:2607.26661v1 | SRC-ARXIV@arXiv:2607.26661v1 | https://arxiv.org/html/2607.26661v1#Ax2 — B. Method Details; https://arxiv.org/html/2607.26661v1#Ax2.SSx1 — B.1. Algorithm Framework | https://arxiv.org/html/2607.26661v1#Ax3 — C. Experimental Benchmarks & Full Data Matrices; https://arxiv.org/html/2607.26661v1#Ax2.SSx5 — B.5. Experimental Infrastructure | https://arxiv.org/html/2607.26661v1#Ax4 — D. Discussion and Future Work; https://arxiv.org/html/2607.26661v1#Ax4.SSx3 — D.3. Limitations & Future Directions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26661 | complete |
| SF-2026-ARXIV-2607-26688 | RP-bb7450d83251fe59 | standard | arXiv:2607.26688v1 | SRC-ARXIV@arXiv:2607.26688v1 | https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2 | https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2 | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26688 | complete |
| SF-2026-ARXIV-2607-26694 | RP-1f385acbbf1b7da6 | deep | arXiv:2607.26694v1 | SRC-ARXIV@arXiv:2607.26694v1 | https://arxiv.org/html/2607.26694v1#S3 — 3 Model; https://arxiv.org/html/2607.26694v1#S3.SS0.SSS0.Px1 — Model Formulation. | https://arxiv.org/html/2607.26694v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.26694v1#S5.SS0.SSS0.Px1 — Evaluation protocol. | https://arxiv.org/html/2607.26694v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26694 | complete |
| SF-2026-ARXIV-2607-26710 | RP-04a994d35d5a1c2f | deep | arXiv:2607.26710v1 | SRC-ARXIV@arXiv:2607.26710v1 | https://arxiv.org/html/2607.26710v1#S4.SS2 — 4.2. Benchmark Design; https://arxiv.org/html/2607.26710v1#A1 — Appendix A ECBench Implementation Details | https://arxiv.org/html/2607.26710v1#S4.SS2 — 4.2. Benchmark Design; https://arxiv.org/html/2607.26710v1#S6 — 6. Experiments | https://arxiv.org/html/2607.26710v1#A4.SS3 — D.3. Limitations and Future Work; https://arxiv.org/html/2607.26710v1#A4 — Appendix D Additional Notes and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26710 | complete |
| SF-2026-ARXIV-2607-26712 | RP-3d5e580112e9a666 | deep | arXiv:2607.26712v1 | SRC-ARXIV@arXiv:2607.26712v1 | https://arxiv.org/html/2607.26712v1#A1 — Appendix A Model Architecture and Training Configuration; https://arxiv.org/html/2607.26712v1#Sx3 — Method | https://arxiv.org/html/2607.26712v1#A2 — Appendix B Step-Drift Evaluation Protocol; https://arxiv.org/html/2607.26712v1#A4 — Appendix D Cross-Game CEM Evaluation Protocol | https://arxiv.org/html/2607.26712v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26712 | complete |
| SF-2026-ARXIV-2607-26719 | RP-a5725060f547712f | deep | arXiv:2607.26719v1 | SRC-ARXIV@arXiv:2607.26719v1 | https://arxiv.org/html/2607.26719v1#S3 — 3. The Lily Approach; https://arxiv.org/html/2607.26719v1#S4.SS4 — 4.4. Reusing Common System Call Types | https://arxiv.org/html/2607.26719v1#S5 — 5. Experimental Evaluation; https://arxiv.org/html/2607.26719v1#S5.SS1 — 5.1. Experimental Protocol | https://arxiv.org/html/2607.26719v1#S5.SS7 — 5.7. Threats to Result Generalizability; https://arxiv.org/html/2607.26719v1#S7 — 7. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26719 | complete |
| SF-2026-ARXIV-2607-26722 | RP-1f642e06ee825667 | standard | arXiv:2607.26722v1 | SRC-ARXIV@arXiv:2607.26722v1 | https://arxiv.org/html/2607.26722v1#Sx3 — Proposed Approach | https://arxiv.org/html/2607.26722v1#Sx4.SSx2 — Experimental Results; https://arxiv.org/html/2607.26722v1#Sx4 — Experiments | https://arxiv.org/html/2607.26722v1#Sx5 — Conclusion and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26722 | complete |
| SF-2026-ARXIV-2607-26754 | RP-b09a660e7512c137 | deep | arXiv:2607.26754v1 | SRC-ARXIV@arXiv:2607.26754v1 | https://arxiv.org/html/2607.26754v1#S3.SS2 — 3.2 Model Architecture; https://arxiv.org/html/2607.26754v1#S1a — A Experimental Model Information | https://arxiv.org/html/2607.26754v1#S1a — A Experimental Model Information; https://arxiv.org/html/2607.26754v1#S4 — 4 Experiments | https://arxiv.org/html/2607.26754v1#S5 — 5 Conclusions and Discussions; https://arxiv.org/html/2607.26754v1#S3a — C Failure Cases | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26754 | complete |
| SF-2026-ARXIV-2607-26760 | RP-9afe37de350ffa33 | deep | arXiv:2607.26760v1 | SRC-ARXIV@arXiv:2607.26760v1 | https://arxiv.org/html/2607.26760v1#A3 — Appendix C Update Designs across Model Scales; https://arxiv.org/html/2607.26760v1#S3 — 3 Metis Architecture | https://arxiv.org/html/2607.26760v1#A2 — Appendix B Extensive Experiment Results; https://arxiv.org/html/2607.26760v1#A5 — Appendix E Evaluation Implementation Details | https://arxiv.org/html/2607.26760v1#S2.SS5 — 2.5 Discussion; https://arxiv.org/html/2607.26760v1#S8 — 8 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26760 | complete |
| SF-2026-ARXIV-2607-26769 | RP-ba757fdfcfc6a127 | standard | arXiv:2607.26769v1 | SRC-ARXIV@arXiv:2607.26769v1 | https://arxiv.org/html/2607.26769v1#S2.SS1 — 2.1 Task Design and Data Sources; https://arxiv.org/html/2607.26769v1#S8 — 8 Inference Prompts and Implementation Details | https://arxiv.org/html/2607.26769v1#S10 — 10 Complete Outcome and Paired-Intervention Results; https://arxiv.org/html/2607.26769v1#S10.SS1 — 10.1 Complete 1.2K Outcome Results | https://arxiv.org/html/2607.26769v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.26769v1#S13.SS2 — 13.2 Process-level Failure Cases | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26769 | complete |
| SF-2026-ARXIV-2607-26773 | RP-05bb512aff0cb0c6 | deep | arXiv:2607.26773v1 | SRC-ARXIV@arXiv:2607.26773v1 | https://arxiv.org/html/2607.26773v1#Sx3 — The Audit Framework | https://arxiv.org/html/2607.26773v1#Sx4 — Experiments and Results; https://arxiv.org/html/2607.26773v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.26773v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26773 | complete |
| SF-2026-ARXIV-2607-26777 | RP-eb4bce26bf99c185 | standard | arXiv:2607.26777v1 | SRC-ARXIV@arXiv:2607.26777v1 | https://arxiv.org/html/2607.26777v1#Sx3 — Method; https://arxiv.org/html/2607.26777v1#Sx4.SSx3 — Baselines and Implementation Details | https://arxiv.org/html/2607.26777v1#Sx5 — Experimental Results; https://arxiv.org/html/2607.26777v1#Sx2.SSx1 — Repository-level Feature Development Benchmarks | https://arxiv.org/html/2607.26777v1#Sx6 — Discussion; https://arxiv.org/html/2607.26777v1#Sx7 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26777 | complete |
| SF-2026-ARXIV-2607-26784 | RP-ebaa990c83894143 | standard | arXiv:2607.26784v1 | SRC-ARXIV@arXiv:2607.26784v1 | https://arxiv.org/html/2607.26784v1#S3 — 3 Method; https://arxiv.org/html/2607.26784v1#S5.SS2 — 5.2 Performance across Model Sizes | https://arxiv.org/html/2607.26784v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26784v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.26784v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.26784v1#S8 — 8 Limitation | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26784 | complete |
| SF-2026-ARXIV-2607-26789 | RP-5bfa6ba7331ce7c8 | deep | arXiv:2607.26789v1 | SRC-ARXIV@arXiv:2607.26789v1 | https://arxiv.org/html/2607.26789v1#Sx3 — Method; https://arxiv.org/html/2607.26789v1#A5 — Appendix E Episodic Context Implementation | https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries; https://arxiv.org/html/2607.26789v1#A13 — Appendix M Episodic-Memory Interaction Ablation | https://arxiv.org/html/2607.26789v1#A12 — Appendix L Natural Failures and Distribution Shifts; https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26789 | complete |
| SF-2026-ARXIV-2607-26791 | RP-6e8dd3d33f2c1ad7 | standard | arXiv:2607.26791v1 | SRC-ARXIV@arXiv:2607.26791v1 | https://arxiv.org/html/2607.26791v1#A3.SS1 — C.1 Task Prompt for Linux Operating System; https://arxiv.org/html/2607.26791v1#A3.SS2 — C.2 Task Prompt for Windows Operating System | https://arxiv.org/html/2607.26791v1#A4 — Appendix D Supplementary Experimental Results; https://arxiv.org/html/2607.26791v1#A3.SS3 — C.3 Evaluation Prompt | https://arxiv.org/html/2607.26791v1#S5 — 5 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26791 | complete |
| SF-2026-ARXIV-2607-26801 | RP-7a1fe1d60905a895 | standard | arXiv:2607.26801v1 | SRC-ARXIV@arXiv:2607.26801v1 | https://arxiv.org/html/2607.26801v1#S4 — IV Proposed Framework; https://arxiv.org/html/2607.26801v1#S4.SS1 — IV-A Framework Overview | https://arxiv.org/html/2607.26801v1#S5 — V Comparative Analysis; https://arxiv.org/html/2607.26801v1#S6 — VI Experiments | https://arxiv.org/html/2607.26801v1#S7 — VII Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26801 | complete |
| SF-2026-ARXIV-2607-26807 | RP-6b5937e6b01f1858 | standard | arXiv:2607.26807v1 | SRC-ARXIV@arXiv:2607.26807v1 | https://arxiv.org/html/2607.26807v1#Sx3.SSx1 — KinRT’s Architecture and Design Philosophy; https://arxiv.org/html/2607.26807v1#Sx3 — Methodology | https://arxiv.org/html/2607.26807v1#Sx4.SSx1 — Experimental Setups and Evaluation Metrics; https://arxiv.org/html/2607.26807v1#Sx3.SSx5 — DIYRobot Platform and Benchmark | https://arxiv.org/html/2607.26807v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26807 | complete |
| SF-2026-ARXIV-2607-26809 | RP-b5d03cbf4750ff98 | standard | arXiv:2607.26809v1 | SRC-ARXIV@arXiv:2607.26809v1 | https://arxiv.org/html/2607.26809v1#Sx3 — Method; https://arxiv.org/html/2607.26809v1#Sx4.SSx4 — System Analysis | https://arxiv.org/html/2607.26809v1#Sx4 — Experiments; https://arxiv.org/html/2607.26809v1#Sx4.SSx4 — System Analysis | https://arxiv.org/html/2607.26809v1#Sx5 — Limitations and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26809 | complete |
| SF-2026-ARXIV-2607-26818 | RP-2a6c8fdbb6a3d125 | deep | arXiv:2607.26818v1 | SRC-ARXIV@arXiv:2607.26818v1 | https://arxiv.org/html/2607.26818v1#Sx3 — Method | https://arxiv.org/html/2607.26818v1#A3 — Appendix C Long-Video Benchmark; https://arxiv.org/html/2607.26818v1#A4 — Appendix D Additional Ablations | https://arxiv.org/html/2607.26818v1#A6 — Appendix F Limitation and Discussion; https://arxiv.org/html/2607.26818v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26818 | complete |
| SF-2026-ARXIV-2607-26819 | RP-cd19c6eceed41b4e | standard | arXiv:2607.26819v1 | SRC-ARXIV@arXiv:2607.26819v1 | https://arxiv.org/html/2607.26819v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26819v1#S2 — 2 Related Work | https://arxiv.org/html/2607.26819v1#S3 — 3 The RepoComplianceBench Benchmark; https://arxiv.org/html/2607.26819v1#S4 — 4 Experiments | https://arxiv.org/html/2607.26819v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.26819v1#S5.SS3 — 5.3 Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26819 | complete |
| SF-2026-ARXIV-2607-26820 | RP-1de038c42395d81c | deep | arXiv:2607.26820v1 | SRC-ARXIV@arXiv:2607.26820v1 | https://arxiv.org/html/2607.26820v1#S3 — 3 Method; https://arxiv.org/html/2607.26820v1#S3.SSx2 — Compositional Risk State and Transition Modeling | https://arxiv.org/html/2607.26820v1#A1.SSx3 — Additional Experimental Results; https://arxiv.org/html/2607.26820v1#A1.SSx1 — Details of Evaluation Metrics | https://arxiv.org/html/2607.26820v1#S3.SSx3 — Future Risk Distribution Forecasting; https://arxiv.org/html/2607.26820v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26820 | complete |
| SF-2026-ARXIV-2607-26825 | RP-b3c94f080420dc17 | standard | arXiv:2607.26825v1 | SRC-ARXIV@arXiv:2607.26825v1 | https://arxiv.org/html/2607.26825v1#S2 — 2 Position: Concepts as a Design Axis; https://arxiv.org/html/2607.26825v1#S5.SS0.SSS0.Px2 — Found versus designed. | https://arxiv.org/html/2607.26825v1#S5.SS0.SSS0.Px4 — No shared benchmark across cells. | https://arxiv.org/html/2607.26825v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26825 | complete |
| SF-2026-ARXIV-2607-26828 | RP-7d1fd6651ca914f2 | deep | arXiv:2607.26828v1 | SRC-ARXIV@arXiv:2607.26828v1 | https://arxiv.org/html/2607.26828v1#S4 — 4 Method | https://arxiv.org/html/2607.26828v1#A5 — Appendix E Per-Benchmark Budget-Cutoff Results; https://arxiv.org/html/2607.26828v1#A3 — Appendix C Benchmark Details | https://arxiv.org/html/2607.26828v1#S3.SS2 — 3.2 Failure of Cost-Blind Credit; https://arxiv.org/html/2607.26828v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26828 | complete |
| SF-2026-ARXIV-2607-26831 | RP-6259b11cc4e6b440 | standard | arXiv:2607.26831v1 | SRC-ARXIV@arXiv:2607.26831v1 | https://arxiv.org/html/2607.26831v1#S3 — 3 Methodology; https://arxiv.org/html/2607.26831v1#A1 — Appendix A Model Size And Budget | https://arxiv.org/html/2607.26831v1#A3 — Appendix C Results on Excluded Languages; https://arxiv.org/html/2607.26831v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.26831v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26831v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26831 | complete |
| SF-2026-ARXIV-2607-26836 | RP-b2c8dec4a903d125 | deep | arXiv:2607.26836v1 | SRC-ARXIV@arXiv:2607.26836v1 | https://arxiv.org/html/2607.26836v1#S3 — 3 Method; https://arxiv.org/html/2607.26836v1#S3.SSx3 — System-Level Risk Inference | https://arxiv.org/html/2607.26836v1#S4.SSx4 — RQ3: Ablation Study and Configuration Analysis; https://arxiv.org/html/2607.26836v1#A1.SSx1 — Theoretical Analysis | https://arxiv.org/html/2607.26836v1#A1.SSx3 — Discussion on Intervention Strategies; https://arxiv.org/html/2607.26836v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26836 | complete |
| SF-2026-ARXIV-2607-26843 | RP-ed7334612a530a18 | deep | arXiv:2607.26843v1 | SRC-ARXIV@arXiv:2607.26843v1 | https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S3 — 3. System Model and Fault Taxonomy | https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S5 — 5. Experimental Setup | https://arxiv.org/html/2607.26843v1#S8 — 8. Threats to Validity; https://arxiv.org/html/2607.26843v1#S9 — 9. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26843 | complete |
| SF-2026-ARXIV-2607-26845 | RP-83466556910465a1 | standard | arXiv:2607.26845v1 | SRC-ARXIV@arXiv:2607.26845v1 | https://arxiv.org/html/2607.26845v1#S2 — 2 Methods; https://arxiv.org/html/2607.26845v1#A1.SS1 — A.1 Models and Thinking Modes | https://arxiv.org/html/2607.26845v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.26845v1#A2 — Appendix B Measurement and Analysis Details | https://arxiv.org/html/2607.26845v1#S4 — 4 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26845 | complete |
| SF-2026-ARXIV-2607-26849 | RP-4fc6efe03110fdcf | deep | arXiv:2607.26849v1 | SRC-ARXIV@arXiv:2607.26849v1 | https://arxiv.org/html/2607.26849v1#A6 — Appendix F Implementation Details; https://arxiv.org/html/2607.26849v1#S4.SS3 — 4.3 Models | https://arxiv.org/html/2607.26849v1#S3 — 3 ToxScreen: Backdoor Defense Benchmark; https://arxiv.org/html/2607.26849v1#S4 — 4 Experimental Set-up | https://arxiv.org/html/2607.26849v1#S7 — 7 Discussion and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26849 | complete |
| SF-2026-ARXIV-2607-26862 | RP-f07d60a08429d22e | deep | arXiv:2607.26862v1 | SRC-ARXIV@arXiv:2607.26862v1 | https://arxiv.org/html/2607.26862v1#A2.SS3 — B.3 Combining ReCo with Existing GRPO Methods; https://arxiv.org/html/2607.26862v1#S3 — 3 Method | https://arxiv.org/html/2607.26862v1#A1.SS2 — A.2 Evaluation Details; https://arxiv.org/html/2607.26862v1#A2 — Appendix B Additional Experiments | https://arxiv.org/html/2607.26862v1#Sx1 — Limitations and Discussion; https://arxiv.org/html/2607.26862v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26862 | complete |
| SF-2026-ARXIV-2607-26865 | RP-e3aca8495b33cc90 | deep | arXiv:2607.26865v1 | SRC-ARXIV@arXiv:2607.26865v1 | https://arxiv.org/html/2607.26865v1#A5 — Appendix E Probe Architecture Details | https://arxiv.org/html/2607.26865v1#A7 — Appendix G Additional Experimental Details; https://arxiv.org/html/2607.26865v1#A7.SS1 — G.1 Convergence Probe Ablation | https://arxiv.org/html/2607.26865v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26865 | complete |
| SF-2026-ARXIV-2607-26873 | RP-4ea0be0ae2d5f360 | standard | arXiv:2607.26873v1 | SRC-ARXIV@arXiv:2607.26873v1 | https://arxiv.org/html/2607.26873v1#S4 — 4 Method: SERPO; https://arxiv.org/html/2607.26873v1#A2 — Appendix B Complete SERPO Implementation | https://arxiv.org/html/2607.26873v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.26873v1#A4 — Appendix D Evaluation Protocol and Additional Analyses | https://arxiv.org/html/2607.26873v1#S6 — 6 Limitations and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26873 | complete |
| SF-2026-ARXIV-2607-26903 | RP-cd3ea044ede340d2 | deep | arXiv:2607.26903v1 | SRC-ARXIV@arXiv:2607.26903v1 | https://arxiv.org/html/2607.26903v1#S3 — 3 Method: Pegasus | https://arxiv.org/html/2607.26903v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26903v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.26903v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26903v1#S5.SS3 — 5.3 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26903 | complete |
| SF-2026-ARXIV-2607-26913 | RP-ec5ce0e8a7ac37c8 | standard | arXiv:2607.26913v1 | SRC-ARXIV@arXiv:2607.26913v1 | https://arxiv.org/html/2607.26913v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26913v1#S2 — 2 Related Work | https://arxiv.org/html/2607.26913v1#A1 — Appendix A Experimental and Prompt Details; https://arxiv.org/html/2607.26913v1#A2 — Appendix B Exact Prior-Force Results | https://arxiv.org/html/2607.26913v1#S8 — 8 Limitations; https://arxiv.org/html/2607.26913v1#S9 — 9 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26913 | complete |
| SF-2026-ARXIV-2607-26922 | RP-e22aafe009bb084e | standard | arXiv:2607.26922v1 | SRC-ARXIV@arXiv:2607.26922v1 | https://arxiv.org/html/2607.26922v1#S3 — 3 System and Methods; https://arxiv.org/html/2607.26922v1#S2.SS1 — 2.1 Multi-Agent LLM Systems | https://arxiv.org/html/2607.26922v1#S3.SS5 — 3.5 Experimental Setup; https://arxiv.org/html/2607.26922v1#S4 — 4 Results | https://arxiv.org/html/2607.26922v1#S6 — 6 Discussion; https://arxiv.org/html/2607.26922v1#S6.SS4 — 6.4 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26922 | complete |
| SF-2026-ARXIV-2607-26924 | RP-34d10b47ee672566 | standard | arXiv:2607.26924v1 | SRC-ARXIV@arXiv:2607.26924v1 | https://arxiv.org/html/2607.26924v1#A1.SS1 — A.1 Model and Implementation Details; https://arxiv.org/html/2607.26924v1#S4.SS1 — 4.1 Temporally Centered LeWorldModel | https://arxiv.org/html/2607.26924v1#S5.SS2 — 5.2 Main Results on the LIBERO Benchmark; https://arxiv.org/html/2607.26924v1#A1.SS2 — A.2 Monte Carlo Analysis Details | https://arxiv.org/html/2607.26924v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26924 | complete |
| SF-2026-ARXIV-2607-26928 | RP-98b4c633173c72a1 | standard | arXiv:2607.26928v1 | SRC-ARXIV@arXiv:2607.26928v1 | https://arxiv.org/html/2607.26928v1#Sx4 — Method; https://arxiv.org/html/2607.26928v1#A1 — Appendix A Implementation Details and Prompts | https://arxiv.org/html/2607.26928v1#Sx5 — Results; https://arxiv.org/html/2607.26928v1#Sx7 — Analysis | https://arxiv.org/html/2607.26928v1#Sx7.SSx3 — Future Work: Beyond Human-Move Imitation; https://arxiv.org/html/2607.26928v1#Sx8 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26928 | complete |
| SF-2026-ARXIV-2607-26935 | RP-dfff164a923e15ed | standard | arXiv:2607.26935v1 | SRC-ARXIV@arXiv:2607.26935v1 | https://arxiv.org/html/2607.26935v1#A3 — Appendix C SAINT Architecture and Training Details; https://arxiv.org/html/2607.26935v1#A4 — Appendix D Evasion Methodology | https://arxiv.org/html/2607.26935v1#S10 — 10. Multi-Seed Evaluation; https://arxiv.org/html/2607.26935v1#S11 — 11. Results Summary | https://arxiv.org/html/2607.26935v1#S12 — 12. Discussion & Conclusion; https://arxiv.org/html/2607.26935v1#S5.SS1 — 5.1. Threat Model | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26935 | complete |
| SF-2026-ARXIV-2607-26937 | RP-5417f36e0e19ad60 | standard | arXiv:2607.26937v1 | SRC-ARXIV@arXiv:2607.26937v1 | https://arxiv.org/html/2607.26937v1#S5.SS1 — 5.1 Method Overview | https://arxiv.org/html/2607.26937v1#S6 — 6 Experimental Evaluation; https://arxiv.org/html/2607.26937v1#S4 — 4 Analysis of Evidence Allocation | https://arxiv.org/html/2607.26937v1#S4.SS2 — 4.2 Limitations of Existing Allocation Controls; https://arxiv.org/html/2607.26937v1#S7 — 7 Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26937 | complete |
| SF-2026-ARXIV-2607-26953 | RP-8c375f8fa39c5139 | deep | arXiv:2607.26953v1 | SRC-ARXIV@arXiv:2607.26953v1 | https://arxiv.org/html/2607.26953v1#S6.SS1 — VI-A Validation Methodology | https://arxiv.org/html/2607.26953v1#S1 — I Introduction; https://arxiv.org/html/2607.26953v1#S2 — II Running Example: An Agentic Lifecycle Manager | https://arxiv.org/html/2607.26953v1#S7 — VII Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26953 | complete |
| SF-2026-ARXIV-2607-26988 | RP-e8484300430c3d18 | standard | arXiv:2607.26988v1 | SRC-ARXIV@arXiv:2607.26988v1 | https://arxiv.org/html/2607.26988v1#A2 — Appendix B NoPE Transformer Architecture | https://arxiv.org/html/2607.26988v1#S5.SSx3 — The Importance of Evaluation Order | https://arxiv.org/html/2607.26988v1#S7 — 7 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26988 | complete |
| SF-2026-ARXIV-2607-26991 | RP-be2558510e803505 | standard | arXiv:2607.26991v1 | SRC-ARXIV@arXiv:2607.26991v1 | https://arxiv.org/html/2607.26991v1#S5 — V Method | https://arxiv.org/html/2607.26991v1#S6 — VI Experiments; https://arxiv.org/html/2607.26991v1#S6.SS1 — VI-A Experimental Setup | https://arxiv.org/html/2607.26991v1#S5.SS3 — V-C Failure Detection for Adaptive Steering; https://arxiv.org/html/2607.26991v1#S7 — VII Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26991 | complete |
| SF-2026-ARXIV-2607-26998 | RP-19f589550d3ab629 | standard | arXiv:2607.26998v1 | SRC-ARXIV@arXiv:2607.26998v1 | https://arxiv.org/html/2607.26998v1#Sx4.SSx1 — System Overview; https://arxiv.org/html/2607.26998v1#Sx3 — Threat Model | https://arxiv.org/html/2607.26998v1#Sx2.SSx1 — Autonomous Penetration Agents and Benchmarks; https://arxiv.org/html/2607.26998v1#Sx6 — Experiments | https://arxiv.org/html/2607.26998v1#Sx3 — Threat Model; https://arxiv.org/html/2607.26998v1#Sx7 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-26998 | complete |
| SF-2026-ARXIV-2607-27011 | RP-70000620098a8869 | standard | arXiv:2607.27011v1 | SRC-ARXIV@arXiv:2607.27011v1 | https://arxiv.org/html/2607.27011v1#S3 — 3 System Overview | https://arxiv.org/html/2607.27011v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.27011v1#S6.SS4 — 6.4 VAE Component Evaluation | https://arxiv.org/html/2607.27011v1#S7 — 7 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27011 | complete |
| SF-2026-ARXIV-2607-27017 | RP-0a3256eaefcb6363 | deep | arXiv:2607.27017v1 | SRC-ARXIV@arXiv:2607.27017v1 | https://arxiv.org/html/2607.27017v1#S6 — 6 Design Rules | https://arxiv.org/html/2607.27017v1#A3 — Appendix C Full Results; https://arxiv.org/html/2607.27017v1#A3.SS5 — C.5 Real-robot results in full | https://arxiv.org/html/2607.27017v1#S7 — 7 Limitations; https://arxiv.org/html/2607.27017v1#S8 — 8 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27017 | complete |
| SF-2026-ARXIV-2607-27023 | RP-90ba439e97791878 | standard | arXiv:2607.27023v1 | SRC-ARXIV@arXiv:2607.27023v1 | https://arxiv.org/html/2607.27023v1#A3.SS1 — C.1 Implementations Details | https://arxiv.org/html/2607.27023v1#A3 — Appendix C Experimental Details and Additional Results; https://arxiv.org/html/2607.27023v1#A3.SS2 — C.2 Additional Benchmark Details | https://arxiv.org/html/2607.27023v1#S6 — 6 Discussion and Conclusions | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27023 | complete |
| SF-2026-ARXIV-2607-27030 | RP-7d98e1b499edc7e1 | standard | arXiv:2607.27030v1 | SRC-ARXIV@arXiv:2607.27030v1 | https://arxiv.org/html/2607.27030v1#A3 — Appendix C Supplement: One-Dimensional Reliability Model; https://arxiv.org/html/2607.27030v1#S4.SS2 — 4.2 Inexpensive, Non-Frontier Detector Models | https://arxiv.org/html/2607.27030v1#A1 — Appendix A Supplement: Benchmark Format; https://arxiv.org/html/2607.27030v1#S4 — 4 Reference Scanner and Evaluation Protocol | https://arxiv.org/html/2607.27030v1#S6 — 6 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27030 | complete |
| SF-2026-ARXIV-2607-27031 | RP-dd54bf113e30e59f | deep | arXiv:2607.27031v1 | SRC-ARXIV@arXiv:2607.27031v1 | https://arxiv.org/html/2607.27031v1#Sx1 — Introduction; https://arxiv.org/html/2607.27031v1#Sx2 — Behavioral Compatibility Audit | https://arxiv.org/html/2607.27031v1#A1.SSx3 — Theoretical Results; https://arxiv.org/html/2607.27031v1#A1.SSx5 — Experimental Protocol and Reproducibility | https://arxiv.org/html/2607.27031v1#A1.SSx11 — Limitations and Future Extensions; https://arxiv.org/html/2607.27031v1#A1.SSx9 — Additional Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27031 | complete |
| SF-2026-ARXIV-2607-27042 | RP-d3ea8ed302ea96a7 | standard | arXiv:2607.27042v1 | SRC-ARXIV@arXiv:2607.27042v1 | https://arxiv.org/html/2607.27042v1#A1 — Appendix A Nested Algorithm; https://arxiv.org/html/2607.27042v1#S4.SS2 — 4.2 GPTQ-2D Algorithm | https://arxiv.org/html/2607.27042v1#S4 — 4 Theoretical Results | https://arxiv.org/html/2607.27042v1#S6 — 6 Applications and Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27042 | complete |
| SF-2026-ARXIV-2607-27056 | RP-da21553bf8bdb69c | standard | arXiv:2607.27056v1 | SRC-ARXIV@arXiv:2607.27056v1 | https://arxiv.org/html/2607.27056v1#S2.SS1 — 2.1 Memory Systems; https://arxiv.org/html/2607.27056v1#S3 — 3 User Understanding Modeling | https://arxiv.org/html/2607.27056v1#S2.SS2 — 2.2 Memory Benchmarks; https://arxiv.org/html/2607.27056v1#S5 — 5 Experiments | https://arxiv.org/html/2607.27056v1#S5.SS2 — 5.2 Main Findings and Discussions; https://arxiv.org/html/2607.27056v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27056 | complete |
| SF-2026-ARXIV-2607-27069 | RP-6bbb3e203ef12237 | standard | arXiv:2607.27069v1 | SRC-ARXIV@arXiv:2607.27069v1 | https://arxiv.org/html/2607.27069v1#Sx3 — Method | https://arxiv.org/html/2607.27069v1#Sx16 — Held-Out Benchmark Filtering; https://arxiv.org/html/2607.27069v1#Sx4 — Experiments | https://arxiv.org/html/2607.27069v1#Sx5 — Discussion; https://arxiv.org/html/2607.27069v1#Sx6 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27069 | complete |
| SF-2026-ARXIV-2607-27080 | RP-43bd27b3a1175e33 | deep | arXiv:2607.27080v1 | SRC-ARXIV@arXiv:2607.27080v1 | https://arxiv.org/html/2607.27080v1#A1.SS3 — A.3 Taxonomy Design; https://arxiv.org/html/2607.27080v1#Sx3 — Methodology | https://arxiv.org/html/2607.27080v1#A1 — Appendix A Benchmark Construction and Taxonomy; https://arxiv.org/html/2607.27080v1#Sx3.SSx2 — MemSecBench Benchmark | https://arxiv.org/html/2607.27080v1#Sx3.SSx1 — Threat Model; https://arxiv.org/html/2607.27080v1#Sx5 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27080 | complete |
| SF-2026-ARXIV-2607-27081 | RP-470cf9a1c032ea39 | deep | arXiv:2607.27081v1 | SRC-ARXIV@arXiv:2607.27081v1 | https://arxiv.org/html/2607.27081v1#S4.SS4 — 4.4 The Robustness Boundary: Switching the System Prompt; https://arxiv.org/html/2607.27081v1#S3.SS1 — 3.1 Threat Model and Notation | https://arxiv.org/html/2607.27081v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27081v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.27081v1#S3.SS1 — 3.1 Threat Model and Notation; https://arxiv.org/html/2607.27081v1#S5 — 5 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27081 | complete |
| SF-2026-ARXIV-2607-27083 | RP-2a73b079e25d1593 | deep | arXiv:2607.27083v1 | SRC-ARXIV@arXiv:2607.27083v1 | https://arxiv.org/html/2607.27083v1#S5 — 5 Method: CAM-DF and CAM-DF-lite; https://arxiv.org/html/2607.27083v1#A3 — Appendix C Algorithmic and Prompt Details | https://arxiv.org/html/2607.27083v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.27083v1#A7.SS2 — G.2 Robustness, Ablations, and Tuning | https://arxiv.org/html/2607.27083v1#S7 — 7 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27083 | complete |
| SF-2026-ARXIV-2607-27090 | RP-bfa58e8aa360108a | deep | arXiv:2607.27090v1 | SRC-ARXIV@arXiv:2607.27090v1 | https://arxiv.org/html/2607.27090v1#S3 — 3. InferScale Design; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results | https://arxiv.org/html/2607.27090v1#A1 — Appendix A Full Serving-Latency Results; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results | https://arxiv.org/html/2607.27090v1#S7 — 7. Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27090 | complete |
| SF-2026-ARXIV-2607-27110 | RP-c6c0fe8b0da2a62b | standard | arXiv:2607.27110v1 | SRC-ARXIV@arXiv:2607.27110v1 | https://arxiv.org/html/2607.27110v1#Sx4 — Method | https://arxiv.org/html/2607.27110v1#Sx5 — Experiments; https://arxiv.org/html/2607.27110v1#Sx5.SSx1 — Experimental Settings | https://arxiv.org/html/2607.27110v1#Sx6 — Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27110 | complete |
| SF-2026-ARXIV-2607-27143 | RP-6281be50784b7319 | standard | arXiv:2607.27143v1 | SRC-ARXIV@arXiv:2607.27143v1 | https://arxiv.org/html/2607.27143v1#S3 — 3 Methodology & Theoretical Framework; https://arxiv.org/html/2607.27143v1#S6.SS1 — 6.1 System Architecture for Knowledge-Based Systems | https://arxiv.org/html/2607.27143v1#S5.SS4 — 5.4 Sensitivity & Ablation Analysis; https://arxiv.org/html/2607.27143v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.27143v1#S6.SS3 — 6.3 Threats to Validity & Limitations; https://arxiv.org/html/2607.27143v1#S7 — 7 Conclusion & Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27143 | complete |
| SF-2026-ARXIV-2607-27146 | RP-45b933aa5ce685cf | standard | arXiv:2607.27146v1 | SRC-ARXIV@arXiv:2607.27146v1 | https://arxiv.org/html/2607.27146v1#S3.SS1 — 3.1 Base Model | https://arxiv.org/html/2607.27146v1#S3.SS3 — 3.3 Evaluation Benchmarks and Metrics; https://arxiv.org/html/2607.27146v1#A3 — Appendix C Evaluation Details | https://arxiv.org/html/2607.27146v1#A5.SS1 — E.1 Examples of editing after failure recovery; https://arxiv.org/html/2607.27146v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27146 | complete |
| SF-2026-ARXIV-2607-27155 | RP-7efb0b412f4885b1 | standard | arXiv:2607.27155v1 | SRC-ARXIV@arXiv:2607.27155v1 | https://arxiv.org/html/2607.27155v1#A3 — Appendix C Incentive Mechanism and Computation Method for Human Labor Time | https://arxiv.org/html/2607.27155v1#A1.SS1 — A.1 Productivity-Agent Benchmarks; https://arxiv.org/html/2607.27155v1#A1.SS2 — A.2 Office-Automation and Office-Suite Benchmarks | https://arxiv.org/html/2607.27155v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27155 | complete |
| SF-2026-ARXIV-2607-27167 | RP-bfed499fae21e56b | standard | arXiv:2607.27167v1 | SRC-ARXIV@arXiv:2607.27167v1 | https://arxiv.org/html/2607.27167v1#S3 — III Approach of SpecFirst; https://arxiv.org/html/2607.27167v1#S3.SS5 — III-E Principles of Agent Design | https://arxiv.org/html/2607.27167v1#S4 — IV Experimental Design; https://arxiv.org/html/2607.27167v1#S4.SS2 — IV-B Benchmark | https://arxiv.org/html/2607.27167v1#S2.SS2 — II-B Limitations of Existing Code Synthesis Agent; https://arxiv.org/html/2607.27167v1#S7 — VII Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27167 | complete |
| SF-2026-ARXIV-2607-27178 | RP-e9f8fc814c4a16c4 | standard | arXiv:2607.27178v1 | SRC-ARXIV@arXiv:2607.27178v1 | https://arxiv.org/html/2607.27178v1#S2 — 2 Method | https://arxiv.org/html/2607.27178v1#A2 — Appendix B Detailed Results; https://arxiv.org/html/2607.27178v1#A2.SS2 — B.2 Extended Decontaminated BEIR Analysis | https://arxiv.org/html/2607.27178v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.27178v1#Sx1 — Limitations | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27178 | complete |
| SF-2026-ARXIV-2607-27180 | RP-940958e3dc26c94f | deep | arXiv:2607.27180v1 | SRC-ARXIV@arXiv:2607.27180v1 | https://arxiv.org/html/2607.27180v1#S3.SS1 — 3.1 Task Design and 3D Scene Setup | https://arxiv.org/html/2607.27180v1#S4 — 4 Experimental Result; https://arxiv.org/html/2607.27180v1#S3.SS2 — 3.2 Evaluation Metrics. | https://arxiv.org/html/2607.27180v1#S6 — 6 Discussion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27180 | complete |
| SF-2026-ARXIV-2607-27187 | RP-62d09f832b9f83a1 | deep | arXiv:2607.27187v1 | SRC-ARXIV@arXiv:2607.27187v1 | https://arxiv.org/pdf/2607.27187v1#page=5 — PDF page 5, Photonic Fabric Memory Appliance architecture; https://arxiv.org/pdf/2607.27187v1#page=8 — PDF page 8, DAX mapping and multi-host shared-memory data path | https://arxiv.org/pdf/2607.27187v1#page=3 — PDF page 3, repeated-request characterization matrix; https://arxiv.org/pdf/2607.27187v1#page=6 — PDF page 6, emulation methodology; https://arxiv.org/pdf/2607.27187v1#page=9 — PDF page 9, LLMServingSim workload and results | https://arxiv.org/pdf/2607.27187v1#page=10 — PDF page 10, VIII Limitations and Future Work | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27187 | complete |
| SF-2026-ARXIV-2607-27191 | RP-62f3fac07fc02e5d | deep | arXiv:2607.27191v1 | SRC-ARXIV@arXiv:2607.27191v1 | https://arxiv.org/html/2607.27191v1#S2 — 2 Shadow evaluations: A new method for measuring progress towards AI R&D automation; https://arxiv.org/html/2607.27191v1#S4.SS3 — 4.3 The agents committed to unpromising approaches too quickly | https://arxiv.org/html/2607.27191v1#S11 — 11 Pre-experiment expectations survey; https://arxiv.org/html/2607.27191v1#S12 — 12 Comprehensive survey of prior autonomous-AI R&D experiments | https://arxiv.org/html/2607.27191v1#S5 — 5 Log analysis reveals five failure modes; https://arxiv.org/html/2607.27191v1#S6 — 6 A robustness experiment with Codex and GPT-5.6 Sol Ultra reproduced these failure modes | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27191 | complete |
| SF-2026-ARXIV-2607-27201 | RP-c1a112a32c9fa91a | deep | arXiv:2607.27201v1 | SRC-ARXIV@arXiv:2607.27201v1 | https://arxiv.org/html/2607.27201v1#S3 — 3 Theoretical Framework; https://arxiv.org/html/2607.27201v1#S5.SS1 — 5.1 Mentis Design Principle | https://arxiv.org/html/2607.27201v1#A2.SS1 — B.1 Inspectability, Ablations, and Experimental Use; https://arxiv.org/html/2607.27201v1#S7 — 7 Experiments and Analysis | https://arxiv.org/html/2607.27201v1#A13 — Appendix M Future Directions; https://arxiv.org/html/2607.27201v1#A2.SS3 — B.3 Limitations of the Baseline | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27201 | complete |
| SF-2026-ARXIV-2607-27205 | RP-0aa39af713f51518 | deep | arXiv:2607.27205v1 | SRC-ARXIV@arXiv:2607.27205v1 | https://arxiv.org/html/2607.27205v1#S4 — 4 TurboVLA; https://arxiv.org/html/2607.27205v1#S4.SS2 — 4.2 Vision-Language Interaction Module; https://arxiv.org/html/2607.27205v1#S4.SS3 — 4.3 Continuous Action Chunk Prediction | https://arxiv.org/html/2607.27205v1#S5 — 5 Experiments; https://arxiv.org/html/2607.27205v1#S5.SS2 — 5.2 Benchmarks and Metrics | https://arxiv.org/html/2607.27205v1#S6 — 6 Conclusion | Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary. | claim:SF-2026-ARXIV-2607-27205 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-26060:start -->
### Large-Scale ChatBot Validation Through Customer Digital Twin Simulations

<!-- claim:SF-2026-ARXIV-2607-26060:start -->LLM-based chatbots are transforming customer service in regulated domains such as banking, but scalable and cost-effective validation remains a critical barrier to safe deployment. We present a two-part contribution for large-scale chatbot validation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26060:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based chatbots are transforming customer service in regulated domains such as banking, but scalable and cost-effective validation remains a critical barrier to safe deployment.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** First, we introduce a methodology for creating high-fidelity synthetic customer agents (SCAs) as digital twins, grounded in real transactional and conversational data, that enables automatic generation and behavioral conditioning to simulate diverse customer profiles and interaction styles.

**证据证明什么。** Evaluation demonstrates that SCAs achieve high semantic alignment with real customers, low hallucination rates, and successful personality trait reproduction with controllable interventions.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26060v1#S2 — 2 Synthetic Customer Methodology; https://arxiv.org/html/2607.26060v1#S3 — 3 Framework for Validating a Chatbot Using SCA。Evaluation：https://arxiv.org/html/2607.26060v1#S2.SS1 — 2.1 Evaluation of SCA。Limitations / counterevidence：https://arxiv.org/html/2607.26060v1#S4 — 4 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26060:end -->

<!-- review:SF-2026-ARXIV-2607-26064:start -->
### The Age of AI Agents Demands A New Scientific Paradigm To Sustain Trustworthy Science

<!-- claim:SF-2026-ARXIV-2607-26064:start -->AI systems are becoming autonomous research agents that generate hypotheses, design experiments, and produce discoveries at scales beyond human oversight. As seen by increased submissions to ML venues, the verification gap between scientific output and our ability to check it is already widening, and autonomous agents make it worse by magnitudes given human-agent asymmetry. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26064:end -->

**为什么进入候选分母。** 摘要首要问题为“AI systems are becoming autonomous research agents that generate hypotheses, design experiments, and produce discoveries at scales beyond human oversight.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** AI systems are becoming autonomous research agents that generate hypotheses, design experiments, and produce discoveries at scales beyond human oversight.

**证据证明什么。** We argue that without adaptation, ML and any scientific domain using agents face dangerous failures: experimental results that no person can verify, optimization for metrics over understanding, and accountability vacuums that erode scientific trust.

**证据没有证明什么。** Three interconnected challenges (observability, attribution, and reproducibility) break down when contributors cannot be meaningfully questioned or held accountable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26064v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26064v1#S1.SS1 — 1.1 The Verification Gap Is Already Wide, and Agents Will Make It Worse。Evaluation：https://arxiv.org/html/2607.26064v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26064v1#S1.SS1 — 1.1 The Verification Gap Is Already Wide, and Agents Will Make It Worse。Limitations / counterevidence：https://arxiv.org/html/2607.26064v1#S8 — 8 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Three interconnected challenges (observability, attribution, and reproducibility) break down when contributors cannot be meaningfully questioned or held accountable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26064:end -->

<!-- review:SF-2026-ARXIV-2607-26066:start -->
### Do Methods Support the Claims? Intra-Paper Verification for Peer Review

<!-- claim:SF-2026-ARXIV-2607-26066:start -->The growing volume of scientific submissions has motivated interest in using large language models (LLMs) to assist peer review. Existing automated novelty assessment approaches typically compare a paper's claimed contributions against prior literature, implicitly assuming that these contributions are accurately realized in the work itself. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26066:end -->

**为什么进入候选分母。** 摘要首要问题为“The growing volume of scientific submissions has motivated interest in using large language models (LLMs) to assist peer review.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we introduce intra-paper claim verification, a framework that evaluates whether novelty claims articulated in a paper are substantiated by the methods used to realize them.

**证据证明什么。** Human evaluation demonstrates significant alignment between framework-generated assessments and human reviewer concerns, particularly for novelty-related issues.

**证据没有证明什么。** VII Limitations and Future Work The evaluation was performed on a subset of 20 papers drawn from a corpus of 182 ICLR 2025 submissions, limiting the generalizability of the findings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26066v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.26066v1#S4 — IV Evaluation and Experiments; https://arxiv.org/html/2607.26066v1#S5 — V Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26066v1#S7 — VII Limitations and Future Work; https://arxiv.org/html/2607.26066v1#S6 — VI Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：VII Limitations and Future Work The evaluation was performed on a subset of 20 papers drawn from a corpus of 182 ICLR 2025 submissions, limiting the generalizability of the findings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26066:end -->

<!-- review:SF-2026-ARXIV-2607-26070:start -->
### SimpleWikiSearch: A Clean Offline Wikipedia Environment for Agentic Search

<!-- claim:SF-2026-ARXIV-2607-26070:start -->Large language model (LLM)-based agentic search systems are often evaluated as if the underlying LLM were the only component that matters, yet their measured performance also depends on the surrounding search environment: the Wikipedia snapshot, preprocessing pipeline, chunking policy, retrieval backend, tool schema, observation format, and answer submission rule. These details are frequently under-specified, making it difficult to compare results or reproduce reported baselines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26070:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM)-based agentic search systems are often evaluated as if the underlying LLM were the only component that matters, yet their measured performance also depends on the surrounding search environment: the Wikipedia snapshot, preprocessing pipeline, chunking policy, retrieval backend, tool schema, observation format, and answer submission rule.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present SimpleWikiSearch, whose corpus construction, retrieval stack, tool contract, and evaluation protocol are explicit and runnable.

**证据证明什么。** These details are frequently under-specified, making it difficult to compare results or reproduce reported baselines.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26070v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26070v1#S2 — 2 Environment。Evaluation：https://arxiv.org/html/2607.26070v1#S3 — 3 Benchmark Setup; https://arxiv.org/html/2607.26070v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26070v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26070:end -->

<!-- review:SF-2026-ARXIV-2607-26076:start -->
### FinCacheServe: Dependency-Consistent Answer Reuse for Cost-Efficient RAG Serving over Mutable Enterprise Documents

<!-- claim:SF-2026-ARXIV-2607-26076:start -->Retrieval-augmented generation services over mutable enterprise documents repeatedly execute semantically equivalent analysis requests. Answer reuse can remove GPU-bound generation work, yet response caches require dependency consistency when filings, evidence chunks, and tool outputs change. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26076:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented generation services over mutable enterprise documents repeatedly execute semantically equivalent analysis requests.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** FinCacheServe moves reuse above the model call: each answer is stored as a materialized serving object bound to normalized task identity, cited evidence hashes, source-document versions, tool-output fingerprints, model identity, and decoding configuration. A read-side gate checks those dependencies before reuse, while document updates first advance the version store and invalidate dependent answers through a reverse index; cache correctness is therefore separated from admission and eviction policy at one metadata-plane linearization point.

**证据证明什么。** Within the disclosed SEC-derived traces, Qwen2.5 7B/14B/32B serving environments, deterministic metadata fixtures, and stated 2 s SLO replay, the dependency gate produced zero observed dependency-stale answer serves while eliminating hosted model calls; the bounded-capacity and 100k-entry backend experiments additionally test admission, eviction, transactional invalidation, and metadata latency. The 44.30% Wh reduction is an estimate from archived request timing and explicit board-power assumptions, not direct whole-system energy measurement.

**证据没有证明什么。** Dependency freshness is not factual answer correctness, and the paper does not establish the same hit rate, metadata cost, or concurrency behavior for unrelated corpora, tool graphs, models, or production failure domains. It also does not prove that its online utility estimator is optimal; the offline policy is only an oracle-like replay target. Unreported workload, model, hardware, precision, length, batch, concurrency, SLO, and evaluator fields remain Not Disclosed rather than inferred.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26076v1#S3 — 3 System model and consistency target; https://arxiv.org/html/2607.26076v1#S4 — 4 FinCacheServe design。Evaluation：https://arxiv.org/html/2607.26076v1#S6 — 6 Experimental methodology; https://arxiv.org/html/2607.26076v1#S7 — 7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26076v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.26076v1#S8 — 8 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** Answer-level reuse can remove both prefill and decode, but it transfers responsibility to version identity, evidence/tool fingerprints, reverse-index fan-out, invalidation ordering, and capacity policy. Conservative dependency gates trade stale hits for false misses and metadata overhead; ordinary KV/prefix caching remains the safer coexistence branch when requests do not repeat semantically, dependencies cannot be versioned, or answer reuse is disallowed by privacy/isolation policy.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26076:end -->

<!-- review:SF-2026-ARXIV-2607-26094:start -->
### Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback

<!-- claim:SF-2026-ARXIV-2607-26094:start -->Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models. This mismatch leads to sparse learning signals and suboptimal alignment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26094:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement Learning from Human Feedback (RLHF) is the standard approach for aligning large language models with human preferences, but its quality is limited by static, task-agnostic reward models.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce MeRLa (Meta-Learned Reward Shaping), a principled framework that meta-learns a task-aware shaping function $Φ(x,y;ϕ)$ across auxiliary tasks before RLHF training.

**证据证明什么。** Experiments on LLaMA-3-8B across four benchmarks show consistent improvements over PPO, DPO, GRPO, and DAPO, achieving a 90.8% length-controlled win rate on AlpacaEval 2.0 and a score of 9.14 on MT-Bench, with 41% less training instability.

**证据没有证明什么。** Limitations and Future Work Several limitations merit discussion. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26094v1#Sx4 — Method; https://arxiv.org/html/2607.26094v1#Sx4.SSx1 — Composite Reward Design。Evaluation：https://arxiv.org/html/2607.26094v1#Sx5 — Theoretical Analysis; https://arxiv.org/html/2607.26094v1#Sx6 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26094v1#Sx8 — Limitations and Future Work; https://arxiv.org/html/2607.26094v1#Sx9 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations and Future Work Several limitations merit discussion.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26094:end -->

<!-- review:SF-2026-ARXIV-2607-26099:start -->
### Lilith: Backdoor Generalization under Training-Inference Trigger Shift

<!-- claim:SF-2026-ARXIV-2607-26099:start -->Machine-learning services increasingly rely on public data, third-party providers, and outsourced training, creating opportunities for data-poisoning attacks that implant persistent malicious behavior while preserving benign utility. However, existing backdoor studies largely evaluate exact trigger reuse, training-exposed trigger diversity, or variations along predefined transformation axes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26099:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine-learning services increasingly rely on public data, third-party providers, and outsourced training, creating opportunities for data-poisoning attacks that implant persistent malicious behavior while preserving benign utility.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We formulate this problem as backdoor generalization under training--inference trigger shift and introduce Lilith, a black-box anchor-to-family framework.

**证据证明什么。** Experiments across datasets, architectures, poisoning rates, and defenses show that Lilith achieves high family-wise attack success with limited utility degradation and a small trigger generalization gap.

**证据没有证明什么。** Future backdoor evaluation should therefore move beyond exact-trigger protocols and account for training–inference trigger shift. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26099v1#S4 — 4. Method; https://arxiv.org/html/2607.26099v1#S4.SS1 — 4.1. Method Overview。Evaluation：https://arxiv.org/html/2607.26099v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.26099v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26099v1#S6 — 6. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future backdoor evaluation should therefore move beyond exact-trigger protocols and account for training–inference trigger shift.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26099:end -->

<!-- review:SF-2026-ARXIV-2607-26115:start -->
### GPT-Red: Automated Red Teaming via Self-Play at Scale

<!-- claim:SF-2026-ARXIV-2607-26115:start -->We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs. The goal of this model is to evaluate and improve the robustness of our production systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26115:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce \textbf{GPT-Red}, an automated red-teaming agent that is trained to discover novel prompt injection attacks against frontier LLMs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The goal of this model is to evaluate and improve the robustness of our production systems.

**证据证明什么。** The goal of this model is to evaluate and improve the robustness of our production systems.

**证据没有证明什么。** We assume the attacker cannot modify privileged files and tool responses, such as a user’s AGENTS.md . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26115v1#S3.SS2 — \redsemiboldfont 3.2 \redsemiboldfont Threat Model and Affordances; https://arxiv.org/html/2607.26115v1#S7.SS1 — \redsemiboldfont 7.1 \redsemiboldfont Model Training。Evaluation：https://arxiv.org/html/2607.26115v1#A3 — Appendix C Additional Evaluation Details; https://arxiv.org/html/2607.26115v1#S7.SS2 — \redsemiboldfont 7.2 \redsemiboldfont Red-Teaming Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.26115v1#S9 — \redsemiboldfont 9 \redsemiboldfont Conclusion and Future Work; https://arxiv.org/html/2607.26115v1#S3.SS2 — \redsemiboldfont 3.2 \redsemiboldfont Threat Model and Affordances。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We assume the attacker cannot modify privileged files and tool responses, such as a user’s AGENTS.md .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26115:end -->

<!-- review:SF-2026-ARXIV-2607-26119:start -->
### Probing the Origins of Reasoning Performance: Representational Quality for Mathematical Problem-Solving in RL vs. SFT Fine-Tuned Models

<!-- claim:SF-2026-ARXIV-2607-26119:start -->Large reasoning models trained via reinforcement learning (RL) have been increasingly shown to outperform their supervised fine-tuned (SFT) counterparts on mathematical reasoning tasks; Yet the mechanistic basis for this advantage remains unclear. We therefore ask, what internal representational differences enable RL models' superior performance? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26119:end -->

**为什么进入候选分母。** 摘要首要问题为“Large reasoning models trained via reinforcement learning (RL) have been increasingly shown to outperform their supervised fine-tuned (SFT) counterparts on mathematical reasoning tasks; Yet the mechanistic basis for this advantage remains unclear.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We therefore ask, what internal representational differences enable RL models' superior performance?

**证据证明什么。** Large reasoning models trained via reinforcement learning (RL) have been increasingly shown to outperform their supervised fine-tuned (SFT) counterparts on mathematical reasoning tasks; Yet the mechanistic basis for this advantage remains unclear.

**证据没有证明什么。** Token variability analysis reveals model-dependent patterns: while Olmo-3 models maintain consistent generation across difficulty levels regardless of training method, DeepSeek-Math-RL exhibits higher variability than its SFT counterpart—suggesting that the relationship between RL training and output consistency depends on the specific training pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26119v1#Sx2.SSx3 — Reasoning Models Exhibit Representation Clarity; https://arxiv.org/html/2607.26119v1#Sx3.SSx3 — Implementation。Evaluation：https://arxiv.org/html/2607.26119v1#Sx3.SSx4 — Results and Analysis; https://arxiv.org/html/2607.26119v1#A1 — Appendix A Additional Token Variability Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.26119v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Token variability analysis reveals model-dependent patterns: while Olmo-3 models maintain consistent generation across difficulty levels regardless of training method, DeepSeek-Math-RL exhibits higher variability than its SFT counterpart—suggesting that the relationship between RL training and output consistency depends on the specific training pipeline.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26119:end -->

<!-- review:SF-2026-ARXIV-2607-26120:start -->
### Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-26120:start -->Large Language Models (LLMs)-powered multi-agent systems are increasingly deployed in mixed-motive environments, where agents operate under asymmetric information and strategic deception due to conflicting or hidden objectives. In these settings, misalignment with collective goals becomes a central concern. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26120:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs)-powered multi-agent systems are increasingly deployed in mixed-motive environments, where agents operate under asymmetric information and strategic deception due to conflicting or hidden objectives.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a novel framework for evaluating objective misalignment using the social deduction game Werewolf, modifying the objective of a single agent while preserving its assigned role.

**证据证明什么。** Our results show that objective misalignment undermines outcomes in inherently adversarial environments, an effect exacerbated by asymmetric information and specialized roles.

**证据没有证明什么。** The challenge is therefore not simply detecting adversaries, but determining whether an agent’s behavior is consistent with its objectives. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26120v1#S3 — 3 Methodology and Experimental Design。Evaluation：https://arxiv.org/html/2607.26120v1#S3 — 3 Methodology and Experimental Design; https://arxiv.org/html/2607.26120v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26120v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26120v1#S6 — 6 Conclusions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The challenge is therefore not simply detecting adversaries, but determining whether an agent’s behavior is consistent with its objectives.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26120:end -->

<!-- review:SF-2026-ARXIV-2607-26121:start -->
### Towards Trustworthy Embodied Intelligence: A Systems Framework and Graded Trustworthiness Levels

<!-- claim:SF-2026-ARXIV-2607-26121:start -->Embodied intelligence integrates learned perception and decision making with real-time computation, control, and physical interaction. Because failures can cause immediate physical or operational harm, task completion alone does not establish trustworthiness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26121:end -->

**为什么进入候选分母。** 摘要首要问题为“Embodied intelligence integrates learned perception and decision making with real-time computation, control, and physical interaction.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The system layer realizes authorized actions dependably through integrated sensing, computation, control, hardware safeguards, fault containment, and fallback.

**证据证明什么。** This hierarchy grades the strength of bounded deployment claims across task capability, safety, system assurance, operational governance, and supporting evidence, providing a basis for bounded deployment, comparative evaluation, research prioritization, and future standardization.

**证据没有证明什么。** Conversely, dependable control cannot determine whether a high-level objective is semantically appropriate or authorized. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26121v1#S3.SS2 — 3.2 Framework Design; https://arxiv.org/html/2607.26121v1#S3 — 3 A Four-Layer Framework for Trustworthy Embodied Intelligence。Evaluation：https://arxiv.org/html/2607.26121v1#S6.SS1 — 6.1 Evaluation Objects and Claims; https://arxiv.org/html/2607.26121v1#S6.SS2 — 6.2 Joint Evaluation of Capability and Safety。Limitations / counterevidence：https://arxiv.org/html/2607.26121v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.26121v1#S2.SS2 — 2.2 Cross-Layer Failure Propagation。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Conversely, dependable control cannot determine whether a high-level objective is semantically appropriate or authorized.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26121:end -->

<!-- review:SF-2026-ARXIV-2607-26148:start -->
### Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation

<!-- claim:SF-2026-ARXIV-2607-26148:start -->Autonomous embodied agents must sustain a long decision-making loop that involves perceiving, acting, verifying, and self-correcting over many steps. Current systems sustain this loop through task-specific workflows or embodied policies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26148:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous embodied agents must sustain a long decision-making loop that involves perceiving, acting, verifying, and self-correcting over many steps.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Current systems sustain this loop through task-specific workflows or embodied policies.

**证据证明什么。** Although longer horizons, latency, and context growth remain barriers to sustained autonomy, these results show that a general-purpose model can already achieve competitive embodied control without a navigation policy.

**证据没有证明什么。** Second, most failures are route-level, not stop-level : only 4 of 25 trajectories ever entered the 3 m success ball (oracle success), so the typical failure diverged at an early branch and never returned. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26148v1#S3.SS1 — 3.1 Model-Directed Interaction; https://arxiv.org/html/2607.26148v1#S4.SS3 — 4.3 Ablations of the Model, Harness, and Interface。Evaluation：https://arxiv.org/html/2607.26148v1#S4 — 4 Experimental Evaluation; https://arxiv.org/html/2607.26148v1#A1 — Appendix A Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.26148v1#A2 — Appendix B Case Study: All 25 Failures; https://arxiv.org/html/2607.26148v1#S4.SS5 — 4.5 Long-Horizon Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Second, most failures are route-level, not stop-level : only 4 of 25 trajectories ever entered the 3 m success ball (oracle success), so the typical failure diverged at an early branch and never returned.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26148:end -->

<!-- review:SF-2026-ARXIV-2607-26159:start -->
### When benchmark inferences do not compose: Projectibility in AI evaluation

<!-- claim:SF-2026-ARXIV-2607-26159:start -->An AI benchmark result rarely reaches a consequential claim in one step. Evaluators generalize it to further cases, interpret it as evidence of capability, extrapolate it to new tasks, transport it to another system or site, and combine it with assumptions about human review and downstream consequences. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26159:end -->

**为什么进入候选分母。** 摘要首要问题为“An AI benchmark result rarely reaches a consequential claim in one step.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The target of one study may not be the source of the next; system, population, outcome, or conditions may change at the interface; and shared data or model lineage may make apparently independent support dependent.

**证据证明什么。** A known-truth demonstration shows why aggregate stability can erase distinctions a later projection requires.

**证据没有证明什么。** Prospective declaration and independent scrutiny limit such rescue, but they don’t eliminate strategic framing. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26159v1#S2.SS3 — 2.3 What projectibility adds to neighbouring frameworks; https://arxiv.org/html/2607.26159v1#S4.SS3 — 4.3 A confirmatory local design。Evaluation：https://arxiv.org/html/2607.26159v1#S4.SS1 — 4.1 The source result and the proposed use; https://arxiv.org/html/2607.26159v1#S4.SS4 — 4.4 Hypothetical results and their inferential status。Limitations / counterevidence：https://arxiv.org/html/2607.26159v1#S8 — 8 Limitations; https://arxiv.org/html/2607.26159v1#S9 — 9 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Prospective declaration and independent scrutiny limit such rescue, but they don’t eliminate strategic framing.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26159:end -->

<!-- review:SF-2026-ARXIV-2607-26160:start -->
### GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning

<!-- claim:SF-2026-ARXIV-2607-26160:start -->Clinical practice guidelines (CPGs) encode diagnostic criteria, but LLM systems typically retrieve guideline text or absorb it through training rather than execute its rules. We introduce GuideSkill, an external reasoning layer that compiles disease-specific criteria into executable functions returning ordinal diagnostic-support scores. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26160:end -->

**为什么进入候选分母。** 摘要首要问题为“Clinical practice guidelines (CPGs) encode diagnostic criteria, but LLM systems typically retrieve guideline text or absorb it through training rather than execute its rules.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce GuideSkill, an external reasoning layer that compiles disease-specific criteria into executable functions returning ordinal diagnostic-support scores.

**证据证明什么。** GuideSkill-Evo achieves the highest macro-average for every backbone, improves over direct inference by 18.49% relatively, and increases gold-label skill coverage from 56.5% to 99.5%.

**证据没有证明什么。** First, the current skill library is built from a limited set of clinical guidelines. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26160v1#A12 — Appendix L Prompt Design; https://arxiv.org/html/2607.26160v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.26160v1#A4 — Appendix D Sensitivity Analysis of Score Fusion; https://arxiv.org/html/2607.26160v1#A6 — Appendix F Efficiency Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26160v1#A1 — Appendix A Limitations; https://arxiv.org/html/2607.26160v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：First, the current skill library is built from a limited set of clinical guidelines.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26160:end -->

<!-- review:SF-2026-ARXIV-2607-26173:start -->
### Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models

<!-- claim:SF-2026-ARXIV-2607-26173:start -->Alignment training, model organisms, and toy models are usually treated as separate research areas. But projects in all three frequently use supervised fine-tuning (SFT) to pursue the same underlying goals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26173:end -->

**为什么进入候选分母。** 摘要首要问题为“Alignment training, model organisms, and toy models are usually treated as separate research areas.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** But projects in all three frequently use supervised fine-tuning (SFT) to pursue the same underlying goals.

**证据证明什么。** We find that follow-up benign SFT can erase the alignment behavior while preserving capabilities, showing that capability preservation alone does not ensure robustness to subsequent training.

**证据没有证明什么。** 6 Limitations and future work Our experiments only test supervised fine-tuning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26173v1#A6 — Appendix F Model-Spec Pareto results; https://arxiv.org/html/2607.26173v1#A8.SS1 — H.1 Full off-model/on-model two-by-two。Evaluation：https://arxiv.org/html/2607.26173v1#A6 — Appendix F Model-Spec Pareto results; https://arxiv.org/html/2607.26173v1#A8 — Appendix H Experiment details and provenance。Limitations / counterevidence：https://arxiv.org/html/2607.26173v1#S6 — 6 Limitations and future work; https://arxiv.org/html/2607.26173v1#A2 — Appendix B GPQA measurement and non-emission failure。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Limitations and future work Our experiments only test supervised fine-tuning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26173:end -->

<!-- review:SF-2026-ARXIV-2607-26181:start -->
### GoGoTB: Agentic RTL Verification with Specification-Grounded Coverage Closure

<!-- claim:SF-2026-ARXIV-2607-26181:start -->Functional verification dominates integrated circuit (IC) front-end engineering effort, and a single missed bug that escapes to silicon can trigger a costly respin. Recent large language models (LLMs) offer new opportunities to automate this process, yet existing LLM-based approaches generate each component through independent single-turn calls with no shared context, leaving interface mismatches undetected and reported coverage disconnected from specification requirements. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26181:end -->

**为什么进入候选分母。** 摘要首要问题为“Functional verification dominates integrated circuit (IC) front-end engineering effort, and a single missed bug that escapes to silicon can trigger a costly respin.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address these challenges, we present GoGoTB, an agentic framework that achieves end-to-end verification closure through three subsystems: an agentic execution control layer, an evolvable knowledge system, and specification-grounded coverage closure.

**证据证明什么。** No prior work successfully generates a complete verification environment or achieves meaningful coverage on the same benchmarks.

**证据没有证明什么。** The primary limitation is directed test generation for complex multi-step protocol scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26181v1#S2.SS2 — 2.2. From Language Models to Agentic Systems; https://arxiv.org/html/2607.26181v1#S3 — 3. Methodology。Evaluation：https://arxiv.org/html/2607.26181v1#S4 — 4. Experimental Evaluation; https://arxiv.org/html/2607.26181v1#S4.SS1 — 4.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26181v1#S5 — 5. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The primary limitation is directed test generation for complex multi-step protocol scenarios.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26181:end -->

<!-- review:SF-2026-ARXIV-2607-26191:start -->
### Position: Evaluation Scores Are Perishable Knowledge Claims

<!-- claim:SF-2026-ARXIV-2607-26191:start -->Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results. When these signals are aggregated via averaging, evaluation confidence can then substantially exceed the reliability of the weakest signal: a phenomenon we call trust inflation in evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26191:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results.

**证据证明什么。** Evaluation methodologies for language models increasingly combine multiple signals, from automated metrics and LLM-as-judge ratings to human assessments and benchmark suite results.

**证据没有证明什么。** This risk exists but is mitigated by formality tiers, since refreshing an F0 crowd annotation extends only the F0 ceiling, not overall reliability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system。Evaluation：https://arxiv.org/html/2607.26191v1#S2 — 2 Trust inflation in evaluation; https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system。Limitations / counterevidence：https://arxiv.org/html/2607.26191v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This risk exists but is mitigated by formality tiers, since refreshing an F0 crowd annotation extends only the F0 ceiling, not overall reliability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26191:end -->

<!-- review:SF-2026-ARXIV-2607-26192:start -->
### Dynamic Parameterization Is Not Dynamic Inference

<!-- claim:SF-2026-ARXIV-2607-26192:start -->Input-dependent controller coefficients are often treated as evidence of dynamic inference or computational savings. This interpretation conflates three properties: coefficient variation, dependence of a frozen model on how coefficients are assigned to inputs, and conditional execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26192:end -->

**为什么进入候选分母。** 摘要首要问题为“Input-dependent controller coefficients are often treated as evidence of dynamic inference or computational savings.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This interpretation conflates three properties: coefficient variation, dependence of a frozen model on how coefficients are assigned to inputs, and conditional execution.

**证据证明什么。** The results show that dynamic parameterization alone does not establish dynamic inference and that functional dynamics do not establish computational savings.

**证据没有证明什么。** The 504M study uses three seeds and a training schedule that is not compute optimal, so it supports only the direction of the scaling result. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26192v1#S3 — 3 Method: Frozen-Controller Auditing; https://arxiv.org/html/2607.26192v1#S4.SS1 — 4.1 Models and evidence protocol。Evaluation：https://arxiv.org/html/2607.26192v1#S4 — 4 Experiments and Analysis; https://arxiv.org/html/2607.26192v1#S2.SS6 — 2.6 Intervention-Based Functional Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26192v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26192v1#S6 — 6 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The 504M study uses three seeds and a training schedule that is not compute optimal, so it supports only the direction of the scaling result.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26192:end -->

<!-- review:SF-2026-ARXIV-2607-26200:start -->
### Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting

<!-- claim:SF-2026-ARXIV-2607-26200:start -->Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26200:end -->

**为什么进入候选分母。** 摘要首要问题为“Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response.

**证据证明什么。** Probe routing substantially reduces conditional route-and-generation time relative to LLM routing at comparable measured outcomes.

**证据没有证明什么。** Because all 117 selected rewrites are human-labelled Safe and relevant, this audit cannot estimate grader sensitivity to harmful or irrelevant rewrites. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26200v1#A8 — Appendix H Rewrite Method Definitions and Offline Preparation; https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework。Evaluation：https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework; https://arxiv.org/html/2607.26200v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26200v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26200v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Because all 117 selected rewrites are human-labelled Safe and relevant, this audit cannot estimate grader sensitivity to harmful or irrelevant rewrites.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26200:end -->

<!-- review:SF-2026-ARXIV-2607-26228:start -->
### Steering Instruction Hierarchies at Inference Time

<!-- claim:SF-2026-ARXIV-2607-26228:start -->Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools. Yet frontier LLMs often violate this hierarchy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26228:end -->

**为什么进入候选分母。** 摘要首要问题为“Instruction hierarchies are a core safety assumption of language model deployment: higher priority inputs, such as system prompts, should override conflicting lower priority inputs from users or tools.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce V-Steer, a training-free inference time method that restores privileged influence by editing cached value vectors at prompt positions.

**证据证明什么。** Across models from 7B to 70B, this attribution guided intervention raises primary constraint accuracy from under 18% up to 92% on controlled role conflict benchmarks, and on broader instruction hierarchy evaluations substantially outperforms prompt only baselines while matching or exceeding SoTA training based methods on 3 of 4 scales of LLMs, with negligible decoding-speed overhead.

**证据没有证明什么。** 6 Conclusion, Limitations and Future Work Existing approaches to enforcing instruction hierarchies have largely relied either on prompting or on additional training, leaving little in the way of cheap and effective inference-time control. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26228v1#S4 — 4 Method: V-Steer; https://arxiv.org/html/2607.26228v1#A1 — Appendix A Additional Algorithmic Details。Evaluation：https://arxiv.org/html/2607.26228v1#A1.SS5 — A.5 V-Auto Experimental Results; https://arxiv.org/html/2607.26228v1#A1.SS3 — A.3 Detailed Complexity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26228v1#S6 — 6 Conclusion, Limitations and Future Work; https://arxiv.org/html/2607.26228v1#S4.SS1 — 4.1 Attention Steering and Its Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：6 Conclusion, Limitations and Future Work Existing approaches to enforcing instruction hierarchies have largely relied either on prompting or on additional training, leaving little in the way of cheap and effective inference-time control.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26228:end -->

<!-- review:SF-2026-ARXIV-2607-26244:start -->
### Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation

<!-- claim:SF-2026-ARXIV-2607-26244:start -->Public tests are widely used to guide large language model code generation, but whether models treat them as executable specifications or merely as extra prompt context remains unclear. We study test-driven code generation on HumanEval+, MBPP+, and recent LiveCodeBench tasks using Qwen2.5-Coder-7B and Qwen3.6-27B. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26244:end -->

**为什么进入候选分母。** 摘要首要问题为“Public tests are widely used to guide large language model code generation, but whether models treat them as executable specifications or merely as extra prompt context remains unclear.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study test-driven code generation on HumanEval+, MBPP+, and recent LiveCodeBench tasks using Qwen2.5-Coder-7B and Qwen3.6-27B.

**证据证明什么。** These results show that tests influence code models through both semantic guidance and prompt-context perturbation, and that representational change alone does not demonstrate effective test utilization.

**证据没有证明什么。** Capability is therefore a plausible necessary condition, but clearly not a sufficient one, for dependable test utilization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26244v1#Sx2.SSx2 — Models and Evaluation。Evaluation：https://arxiv.org/html/2607.26244v1#Sx2 — Experimental Setup; https://arxiv.org/html/2607.26244v1#Sx2.SSx2 — Models and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26244v1#Sx10 — Conclusion; https://arxiv.org/html/2607.26244v1#Sx7 — Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Capability is therefore a plausible necessary condition, but clearly not a sufficient one, for dependable test utilization.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26244:end -->

<!-- review:SF-2026-ARXIV-2607-26246:start -->
### Weak-to-Strong On-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-26246:start -->On-policy distillation (OPD), which aligns a student with the teacher's token-level distribution on the student's own rollouts, is an effective paradigm for transferring capabilities across LLMs. Prevailing approaches assume a teacher at least as capable as the student: they either distill a larger model into a smaller one, which fails at the frontier where no larger teacher exists, or consolidate multiple domain experts trained from a shared base, which requires costly training at the student's scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26246:end -->

**为什么进入候选分母。** 摘要首要问题为“On-policy distillation (OPD), which aligns a student with the teacher's token-level distribution on the student's own rollouts, is an effective paradigm for transferring capabilities across LLMs.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce Weak-to-Strong On-Policy Distillation (W2S-OPD), a simple yet effective OPD framework that improves the strong student by distilling from multiple weak models.

**证据证明什么。** We introduce Weak-to-Strong On-Policy Distillation (W2S-OPD), a simple yet effective OPD framework that improves the strong student by distilling from multiple weak models.

**证据没有证明什么。** 6 Conclusion We introduce W2S-OPD, a weak-to-strong on-policy distillation framework that improves a strong student using only smaller or weaker models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26246v1#A3 — Appendix C Implementation Details; https://arxiv.org/html/2607.26246v1#A4.SS2 — D.2 Performance with Different Scales of Base Models。Evaluation：https://arxiv.org/html/2607.26246v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.26246v1#A4.SS1 — D.1 Runtime Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26246v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Conclusion We introduce W2S-OPD, a weak-to-strong on-policy distillation framework that improves a strong student using only smaller or weaker models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26246:end -->

<!-- review:SF-2026-ARXIV-2607-26247:start -->
### Between Gradient and Natural Gradient: A Continuum of LoRA Initializations

<!-- claim:SF-2026-ARXIV-2607-26247:start -->Low-rank adaptation (LoRA) fine-tunes large pretrained models at a fraction of the cost of full fine-tuning, but its performance depends strongly on how the adapters are initialized. Recent schemes initialize the adapters from the downstream loss gradient: some project the raw gradient onto its top directions, while others first whiten it with an estimate of the loss curvature. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26247:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-rank adaptation (LoRA) fine-tunes large pretrained models at a fraction of the cost of full fine-tuning, but its performance depends strongly on how the adapters are initialized.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Our deployable, search-free variant, ULoRA-Auto, selects per-layer exponents from measured spectral statistics, approaches this upper bound at no additional search cost, and ranks at or near the top among deployable LoRA methods.

**证据证明什么。** Our results show that a principled design space for LoRA initialization and curvature preconditioning should be treated as a tunable dimension rather than a fixed design decision.

**证据没有证明什么。** Fixed choices, whether no whitening or full whitening, leave accuracy on the table in most settings, and the extended landscape shows a genuine failure region that a fixed choice cannot guard against. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26247v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26247v1#Sx4 — Experiments; https://arxiv.org/html/2607.26247v1#Sx4.SSx1 — Results。Limitations / counterevidence：https://arxiv.org/html/2607.26247v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Fixed choices, whether no whitening or full whitening, leave accuracy on the table in most settings, and the extended landscape shows a genuine failure region that a fixed choice cannot guard against.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26247:end -->

<!-- review:SF-2026-ARXIV-2607-26253:start -->
### Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR

<!-- claim:SF-2026-ARXIV-2607-26253:start -->Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by rollout generation, yet many sampled prompts produce saturated groups (all responses correct or all incorrect) whose zero reward variance yields no policy-gradient signal. Existing remedies either oversample a larger candidate pool and discard saturated prompts (dynamic sampling), paying heavy extra rollouts, or predict prompt difficulty before sampling, which is fragile under a shifting policy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26253:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards (RLVR) is bottlenecked by rollout generation, yet many sampled prompts produce saturated groups (all responses correct or all incorrect) whose zero reward variance yields no policy-gradient signal.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing remedies either oversample a larger candidate pool and discard saturated prompts (dynamic sampling), paying heavy extra rollouts, or predict prompt difficulty before sampling, which is fragile under a shifting policy.

**证据证明什么。** On mathematical reasoning and planning with 1.5B/3B models on a single GPU, SARA matches DPS (both below the DS oracle) while using 22% fewer rollouts than DS; composing SARA with DPS yields the best accuracy, slightly above DS, at 67% fewer rollouts (near-uniform cost).

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26253v1#A1 — Appendix A Use of Large Language Models; https://arxiv.org/html/2607.26253v1#A4 — Appendix D Algorithm and Implementation Details。Evaluation：https://arxiv.org/html/2607.26253v1#A3 — Appendix C Proofs and Theoretical Analysis; https://arxiv.org/html/2607.26253v1#A5 — Appendix E Detailed Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26253v1#A7 — Appendix G Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.26253v1#S5 — 5 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26253:end -->

<!-- review:SF-2026-ARXIV-2607-26300:start -->
### AgentGUI: An Interface for Observing and Steering Long-Running AI Agents

<!-- claim:SF-2026-ARXIV-2607-26300:start -->AI agents are increasingly adept at tackling complex, long-running tasks. With the rapid surge of autonomous capabilities, human oversight is systematically lagging behind due to limited human-centered interfacing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26300:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents are increasingly adept at tackling complex, long-running tasks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** With the rapid surge of autonomous capabilities, human oversight is systematically lagging behind due to limited human-centered interfacing.

**证据证明什么。** A controlled user study demonstrates statistically significant reduction in the time it takes to identify key elements from agent traces (38% faster, p = 0.023).

**证据没有证明什么。** First, the small and rather homogeneous user study limits the statistical test power and may not be fully generalizable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26300v1#S4 — 4 System evaluation。Evaluation：https://arxiv.org/html/2607.26300v1#A2 — Appendix B Statistical Testing and Analysis; https://arxiv.org/html/2607.26300v1#A3 — Appendix C Cost Analysis For Manager Steering。Limitations / counterevidence：https://arxiv.org/html/2607.26300v1#S5 — 5 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：First, the small and rather homogeneous user study limits the statistical test power and may not be fully generalizable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26300:end -->

<!-- review:SF-2026-ARXIV-2607-26307:start -->
### TraceCoder: Explainable and Auditable Code Generation with Position-Key Snippet Versioning

<!-- claim:SF-2026-ARXIV-2607-26307:start -->Contemporary LLM-based coding agents produce code as black-box outputs: the rationale behind each line is hidden, the evolution of the code through benchmark-driven repair is ephemeral, and post-hoc auditing is impossible. We present a code generation concept that addresses these shortcomings through three complementary mechanisms: (i) a relational snippet-history schema that records, per repair event, the benchmark reference, round number, failure text, and LLM explanation, enabling full provenance queries; (ii) a browser-based visualisation tool that renders this history as heat-mapped, hover-annotated source code; and (iii) a competitive fractional position-key indexing scheme with tree-node delimiters that assigns stable, lexicographically-ordered identifiers to each code snippet, enabling fine-grained tracking without disrupting surrounding lines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26307:end -->

**为什么进入候选分母。** 摘要首要问题为“Contemporary LLM-based coding agents produce code as black-box outputs: the rationale behind each line is hidden, the evolution of the code through benchmark-driven repair is ephemeral, and post-hoc auditing is impossible.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Three detailed case studies demonstrate how the system explains which specific benchmark failures shaped each line of the final program.

**证据证明什么。** Three detailed case studies demonstrate how the system explains which specific benchmark failures shaped each line of the final program.

**证据没有证明什么。** 8 Discussion The experiments surface both the promise and the current limits of TraceCoder. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26307v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.26307v1#S2.SS3 — 2.3 Coding Agent Systems。Evaluation：https://arxiv.org/html/2607.26307v1#S6 — 6 Experimental Evaluation; https://arxiv.org/html/2607.26307v1#S2.SS7 — 2.7 Benchmarks and Specification Mining。Limitations / counterevidence：https://arxiv.org/html/2607.26307v1#S8 — 8 Discussion; https://arxiv.org/html/2607.26307v1#S8.SS3 — 8.3 Threats to Evaluation Validity。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：8 Discussion The experiments surface both the promise and the current limits of TraceCoder.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26307:end -->

<!-- review:SF-2026-ARXIV-2607-26313:start -->
### SARC-DQ: Runtime Data-Quality Gating for Agentic AI: Silent Evidence Defects, the Incompetence Shield, and Downstream-Only Remediation

<!-- claim:SF-2026-ARXIV-2607-26313:start -->Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost. The most dangerous enterprise defects are metadata-borne: a stale price or a superseded record, perfectly well-formed in the payload and betrayed only by freshness, lineage, or provenance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26313:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost.

**证据证明什么。** Code, frozen results, and a deterministic analysis pipeline: https://github.com/besanson/dqSarc

**证据没有证明什么。** SARC-DQ does not eliminate upstream data-quality work and does not detect defects for which no predicate or trustworthy metadata exists; runtime gating complements rather than replaces upstream governance, and its benefit is predicate- and metadata-quality-dependent. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26313v1#S3 — 3 Architecture。Evaluation：https://arxiv.org/html/2607.26313v1#A1.SS5 — A.5 Robustness: leave-one-class-out, ablations, and threshold sensitivity; https://arxiv.org/html/2607.26313v1#S7 — 7 Results (H1–H4)。Limitations / counterevidence：https://arxiv.org/html/2607.26313v1#S12 — 12 Conclusion; https://arxiv.org/html/2607.26313v1#S9 — 9 Threats to validity。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：SARC-DQ does not eliminate upstream data-quality work and does not detect defects for which no predicate or trustworthy metadata exists; runtime gating complements rather than replaces upstream governance, and its benefit is predicate- and metadata-quality-dependent.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26313:end -->

<!-- review:SF-2026-ARXIV-2607-26314:start -->
### StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents

<!-- claim:SF-2026-ARXIV-2607-26314:start -->Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones. Elite security researchers and advanced persistent threats achieve their objectives unnoticed; autonomous agents increasingly inherit the same offensive tasks, but do they inherit the tradecraft? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26314:end -->

**为什么进入候选分母。** 摘要首要问题为“Stealth, the discipline of achieving an objective without revealing your presence, capabilities, or collected intelligence, is what separates sophisticated operators from detectable ones.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce StealthBench,a benchmark that measures operational stealth in autonomous offensive-security agents across six operational security (OPSEC) dimensions.

**证据证明什么。** Our results show that no model exceeds 54% safe success rate (the compound metric requiring both task completion and stealth), confirming that OPSEC failures are systematic across model families.

**证据没有证明什么。** Opus 4.8 / neighbor-services After staging returned “user not found,” proposed that the reset might work only in production and used production as a diagnostic oracle. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26314v1#Ax1.SSx1 — A.1 Agent System Prompt; https://arxiv.org/html/2607.26314v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.26314v1#S2.SS4 — 2.4 The Defining Experiment; https://arxiv.org/html/2607.26314v1#S2.SS6 — 2.6 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.26314v1#S4.SS3 — 4.3 Exploratory Qualitative Failure Mechanisms; https://arxiv.org/html/2607.26314v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Opus 4.8 / neighbor-services After staging returned “user not found,” proposed that the reset might work only in production and used production as a diagnostic oracle.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26314:end -->

<!-- review:SF-2026-ARXIV-2607-26326:start -->
### Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-26326:start -->Multimodal Large Language Models (MLLMs) achieve strong performance by integrating visual inputs with the rich priors of pretrained language models. However, they often fail on vision-centric tasks, especially when visual evidence conflicts with pretrained knowledge. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26326:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models (MLLMs) achieve strong performance by integrating visual inputs with the rich priors of pretrained language models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To support the second, we introduce the WhatIfVis, a benchmark spanning five coarse-grained dimensions (spatial-temporal, color, count, size, and weight) whose questions admit answers from either the image or the prior.

**证据证明什么。** Applying this steering vector, even without any intent instruction, improves controllability over the vanilla model.

**证据没有证明什么。** As for cross-modal comparison, our text channel states the counterfactual outright and so serves only as an upper bound; the performance gap between modalities on the same underlying fact remains a critical area for future exploration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26326v1#S4.SS1 — 4.1 Designing the Multimodal Context-Sensitivity Task; https://arxiv.org/html/2607.26326v1#A3 — Appendix C Implementation。Evaluation：https://arxiv.org/html/2607.26326v1#A2 — Appendix B Benchmark Composition and Curation; https://arxiv.org/html/2607.26326v1#A4 — Appendix D Extra reconstruction results and exact-match results。Limitations / counterevidence：https://arxiv.org/html/2607.26326v1#A1 — Appendix A Limitations and Future work; https://arxiv.org/html/2607.26326v1#S8 — 8 Conclusions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：As for cross-modal comparison, our text channel states the counterfactual outright and so serves only as an upper bound; the performance gap between modalities on the same underlying fact remains a critical area for future exploration.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26326:end -->

<!-- review:SF-2026-ARXIV-2607-26335:start -->
### The Fabric Is the Cluster Driver: Cross-Layer eBPF Policies for GPU-CXL Fabrics

<!-- claim:SF-2026-ARXIV-2607-26335:start -->We present fabric_ext, an eBPF middleware compiler and runtime for extensible OS policies over GPU--CXL fabrics. fabric_ext lets one policy program execute across GPU hooks, driver/runtime hooks, DPU/NIC hooks, and CXL switch or near-memory hooks. The key abstraction is a semantic movement graph: edges describe bytes, stride, reuse distance, read/write ratio, source and destination, ordering requirement, alias set, ownership, and transformations such as Move, Quantize, Compress, Checksum, Filter, Reduce, Scatter/Gather, Replicate, and Persist. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26335:end -->

**为什么进入候选分母。** 摘要首要问题为“We present fabric_ext, an eBPF middleware compiler and runtime for extensible OS policies over GPU--CXL fabrics.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present fabric_ext, an eBPF middleware compiler and runtime for extensible OS policies over GPU--CXL fabrics. fabric_ext lets one policy program execute across GPU hooks, driver/runtime hooks, DPU/NIC hooks, and CXL switch or near-memory hooks.

**证据证明什么。** The key abstraction is a semantic movement graph: edges describe bytes, stride, reuse distance, read/write ratio, source and destination, ordering requirement, alias set, ownership, and transformations such as Move, Quantize, Compress, Checksum, Filter, Reduce, Scatter/Gather, Replicate, and Persist.

**证据没有证明什么。** If a target cannot load a policy, the epoch switch is aborted and the previous policy remains active. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26335v1#S3 — 3. Design; https://arxiv.org/html/2607.26335v1#S3.SS4 — 3.4. LLM Prefill Across Three Architectures。Evaluation：https://arxiv.org/html/2607.26335v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.26335v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26335v1#S4.SS6 — 4.6. Failure and Fallback; https://arxiv.org/html/2607.26335v1#S7 — 7. Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：If a target cannot load a policy, the epoch switch is aborted and the previous policy remains active.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26335:end -->

<!-- review:SF-2026-ARXIV-2607-26336:start -->
### Learning Implicit Causal World Models from Multi-Agent Demonstrations

<!-- claim:SF-2026-ARXIV-2607-26336:start -->In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms. This problem is exacerbated in multi-agent systems where physical transitions are intertwined with strategic agent intents, causing world models to fail under distribution shift. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26336:end -->

**为什么进入候选分母。** 摘要首要问题为“In model-based reinforcement learning, world models exist as internal simulators, but their training often conflates statistical correlations with causal mechanisms.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Implicit Causal World Models to recover environmental dynamics from offline demonstrations without requiring pre-defined causal graphs.

**证据证明什么。** Evaluations across coordination tasks (Two-Door, Navigation, and Giveway) demonstrate that these models provide interpretable causal representations under both full and partial observability, with model accuracy scaling directly with interventional strength.

**证据没有证明什么。** Second, our guarantees do not extend to layout changes, and the model alone cannot tell a practitioner which regime a new deployment falls into. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26336v1#A16 — Appendix P Neural Architecture Design and Baselines; https://arxiv.org/html/2607.26336v1#S4 — 4 Framework and Methodology。Evaluation：https://arxiv.org/html/2607.26336v1#A20.SS3 — T.3 Evaluation Results: High sample complexity experiments; https://arxiv.org/html/2607.26336v1#A21.SS2 — U.2 Evaluation Results: High sample complexity experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26336v1#S6 — 6 CONCLUSION AND LIMITATIONS; https://arxiv.org/html/2607.26336v1#A24.SS4 — X.4 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Second, our guarantees do not extend to layout changes, and the model alone cannot tell a practitioner which regime a new deployment falls into.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26336:end -->

<!-- review:SF-2026-ARXIV-2607-26339:start -->
### RAGuard: A Layered Defense Framework for Retrieval-Augmented Generation Systems Against Data Poisoning

<!-- claim:SF-2026-ARXIV-2607-26339:start -->Retrieval-Augmented Generation (RAG) systems ground large language models (LLMs) in external corpora, but this reliance exposes them to corpus poisoning: maliciously injected passages that manipulate retrieved evidence. We introduce RAGuard, a layered defense against \emph{factual} corpus-poisoning attacks on RAG pipelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26339:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG) systems ground large language models (LLMs) in external corpora, but this reliance exposes them to corpus poisoning: maliciously injected passages that manipulate retrieved evidence.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce RAGuard, a layered defense against \emph{factual} corpus-poisoning attacks on RAG pipelines.

**证据证明什么。** The defense costs $k{+}1$ generator passes per query ($6\times$ for $k{=}5$); we analyze batching and early-stopping approximations that reduce this overhead.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26339v1#S3 — 3 Methods; https://arxiv.org/html/2607.26339v1#S3.SS1 — 3.1 Overall Architecture。Evaluation：https://arxiv.org/html/2607.26339v1#A1 — Appendix A Full Baseline and ZKIP Evaluation Results; https://arxiv.org/html/2607.26339v1#A4 — Appendix D Supervised Poison Classification Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.26339v1#A2 — Appendix B Threat Model Scope; https://arxiv.org/html/2607.26339v1#S4.SS1 — 4.1 Experimental Setup and Threat Model。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26339:end -->

<!-- review:SF-2026-ARXIV-2607-26340:start -->
### Incast-Free MoE Rate-Based Scheduling

<!-- claim:SF-2026-ARXIV-2607-26340:start -->Mixture of Experts (MoE) architectures have become key to large language models; however, their typical round-robin (RR) scheduling introduces significant bottlenecks. In this paper, we demonstrate that RR causes a previously-undiscovered exponential incast phenomenon with MoE traffic. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26340:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture of Experts (MoE) architectures have become key to large language models; however, their typical round-robin (RR) scheduling introduces significant bottlenecks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose an alternative proactive fair scheduling framework tailored for MoE workloads, which effectively prevents fabric oversubscription.

**证据证明什么。** Finally, through extensive simulations with real and synthetic workloads, we demonstrate that this framework consistently eliminates incast, maintains a near-100% link utilization, and reduces Collective Completion Time (CCT).

**证据没有证明什么。** As network speeds scale to 1,600 Gbps and beyond, building high-speed on-chip switch buffers becomes prohibitively expensive and physically limited by silicon scaling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26340v1#S2.SS3 — 2.3. Frameworks; https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures。Evaluation：https://arxiv.org/html/2607.26340v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：As network speeds scale to 1,600 Gbps and beyond, building high-speed on-chip switch buffers becomes prohibitively expensive and physically limited by silicon scaling.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26340:end -->

<!-- review:SF-2026-ARXIV-2607-26348:start -->
### When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses

<!-- claim:SF-2026-ARXIV-2607-26348:start -->Large language models (LLMs) are increasingly used as synthetic users, stand-ins for human respondents whose simulated answers feed product, policy, and market decisions. We ask when this substitution is valid and when it fails, and package the answer as an evaluation framework for intelligent synthetic-user systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26348:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly used as synthetic users, stand-ins for human respondents whose simulated answers feed product, policy, and market decisions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We ask when this substitution is valid and when it fails, and package the answer as an evaluation framework for intelligent synthetic-user systems.

**证据证明什么。** A decision-impact analysis shows why this matters in practice: on a segment-targeting task the models inflate between-segment gaps two to fourfold, would direct a team to the wrong segment in half of U.S. and most cross-cultural cases, and manufacture segment splits that do not exist in real people.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26348v1#S2.SS6 — 2.6 Decision-support validity and expert-system validation; https://arxiv.org/html/2607.26348v1#A1 — Appendix A Model call settings。Evaluation：https://arxiv.org/html/2607.26348v1#S2.SS2 — 2.2 Survey-simulation benchmarks and cross-cultural value modeling; https://arxiv.org/html/2607.26348v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26348v1#S4.SS6 — 4.6 RQ5: Both failures transfer across domains; https://arxiv.org/html/2607.26348v1#S5 — 5 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26348:end -->

<!-- review:SF-2026-ARXIV-2607-26350:start -->
### Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

<!-- claim:SF-2026-ARXIV-2607-26350:start -->Neural audio codecs (NACs) have become popular for obtaining speech representations as discrete tokens. Beyond compression, discrete tokens can be used to train self-supervised learning (SSL) models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26350:end -->

**为什么进入候选分母。** 摘要首要问题为“Neural audio codecs (NACs) have become popular for obtaining speech representations as discrete tokens.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we present a systematic analysis of language sensitivity by varying either the NAC training language or the SSL pre-training language while keeping the other fixed.

**证据证明什么。** Experimental results show that downstream performance is insensitive to the NAC training language but strongly dependent on the SSL pre-training language.

**证据没有证明什么。** Future work will extend the analysis to more languages and downstream tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26350v1#S3.SS1 — 3.1 Experimental Design。Evaluation：https://arxiv.org/html/2607.26350v1#S3 — 3 Evaluation Setup; https://arxiv.org/html/2607.26350v1#S3.SS1 — 3.1 Experimental Design。Limitations / counterevidence：https://arxiv.org/html/2607.26350v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work will extend the analysis to more languages and downstream tasks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26350:end -->

<!-- review:SF-2026-ARXIV-2607-26358:start -->
### Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-26358:start -->Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy. A standard way to balance this trade-off is via a KL-regularized RL objective, although this formulation does not by itself provide a principled way to set the regularization coefficient. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26358:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In experiments with Qwen3-8B and Llama-3.2-1B, we demonstrate that our methods result in competitive reward-retention trade-offs in a continual learning setting, and illustrate how our framework may be used to audit API providers serving open-source models.

**证据证明什么。** Reinforcement learning (RL) fine-tuning is widely used in language model training to improve model performance on a target task while limiting drift from a reference policy.

**证据没有证明什么。** 7 Conclusions and Future Research We have introduced the sequential detection game, a game-theoretic framework for RL fine-tuning in which an agent seeks to maximize reward while remaining difficult to distinguish from a reference policy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26358v1#A3.SS2 — C.2 Model Auditing; https://arxiv.org/html/2607.26358v1#S5.SS2 — 5.2 Model Auditing。Evaluation：https://arxiv.org/html/2607.26358v1#A3 — Appendix C Appendix for Section 5 : Experiments; https://arxiv.org/html/2607.26358v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26358v1#S7 — 7 Conclusions and Future Research。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：7 Conclusions and Future Research We have introduced the sequential detection game, a game-theoretic framework for RL fine-tuning in which an agent seeks to maximize reward while remaining difficult to distinguish from a reference policy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26358:end -->

<!-- review:SF-2026-ARXIV-2607-26389:start -->
### Misalignment Has a Personality: A Big Five Account of Emergent Misalignment

<!-- claim:SF-2026-ARXIV-2607-26389:start -->Fine-tuning a language model on data containing a narrow flaw, such as insecure code or incorrect mathematical answers, can cause broad misalignment through a mechanism that remains debated. We provide an interpretable account: in the models and corpora we study, misalignment behaves like a shift in personality. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26389:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-tuning a language model on data containing a narrow flaw, such as insecure code or incorrect mathematical answers, can cause broad misalignment through a mechanism that remains debated.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We provide an interpretable account: in the models and corpora we study, misalignment behaves like a shift in personality.

**证据证明什么。** Calibrated personality vectors transform an opaque safety phenomenon into a human-legible diagnostic profile.

**证据没有证明什么。** Our evidence shows measurement, correlation, and imprinting, not intervention; whether the profile is a causal mediator that steering could remove is future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26389v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.26389v1#A3 — Appendix C Transfer Benchmark: BIG5-CHAT; https://arxiv.org/html/2607.26389v1#A7 — Appendix G Full Result Tables。Limitations / counterevidence：https://arxiv.org/html/2607.26389v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Our evidence shows measurement, correlation, and imprinting, not intervention; whether the profile is a causal mediator that steering could remove is future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26389:end -->

<!-- review:SF-2026-ARXIV-2607-26390:start -->
### Impossible to hide secret ...: Uncovering Security and Privacy Issues in LLM-native IDEs

<!-- claim:SF-2026-ARXIV-2607-26390:start -->LLM-native IDEs (Integrated Development Environments), aka LIDEs, are designed from the ground up to work with Large Language Models (LLMs). LIDEs have found remarkable success in Software Engineering (SE) tasks such as coding, debugging, and program comprehension. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26390:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-native IDEs (Integrated Development Environments), aka LIDEs, are designed from the ground up to work with Large Language Models (LLMs).”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** LIDEs are software systems, and, like any system, they can exhibit vulnerabilities.

**证据证明什么。** Our results show that most issues in LIDEs stem from system-level design choices, rather than the underlying LLMs, such as user data access, unchecked autonomous actions, etc.

**证据没有证明什么。** Threats to Validity Construct validity may be affected by inferring security/privacy concerns from informal Reddit posts lacking configuration detail or root-cause evidence; results are thus developer-reported, not confirmed vulnerabilities. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26390v1#S1 — 1. Introduction; https://arxiv.org/html/2607.26390v1#S2 — 2. Study Setup。Evaluation：https://arxiv.org/html/2607.26390v1#S2.SS3 — 2.3. Data Analysis; https://arxiv.org/html/2607.26390v1#S2 — 2. Study Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26390v1#S7 — 7. Threats to Validity。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Threats to Validity Construct validity may be affected by inferring security/privacy concerns from informal Reddit posts lacking configuration detail or root-cause evidence; results are thus developer-reported, not confirmed vulnerabilities.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26390:end -->

<!-- review:SF-2026-ARXIV-2607-26410:start -->
### Voice Memory for Agentic Speech Recognition

<!-- claim:SF-2026-ARXIV-2607-26410:start -->We present Voice Memory, a inference-only scheme for agentic speech recognition: at stream time, a frozen corrector reads a single per-domain memory.md and decides per utterance whether to act on the hypothesis or abstain and keep the 1-best. Asynchronously, a score-gated optimizer revises that file through bounded edits, accepting an edit only when it strictly improves a held-out score. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26410:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Voice Memory, a inference-only scheme for agentic speech recognition: at stream time, a frozen corrector reads a single per-domain memory.md and decides per utterance whether to act on the hypothesis or abstain and keep the 1-best.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Extended from classical ASR-LM framework, we refer this split the listener-thinker architecture; the two roles are coupled only through the memory, so no weights change and the learned skill stays auditable and portable.

**证据证明什么。** Asynchronously, a score-gated optimizer revises that file through bounded edits, accepting an edit only when it strictly improves a held-out score.

**证据没有证明什么。** A memory written by one model family improves a reader from another, because explicit rules travel where weights cannot; the same trust can be trained into weights from audio [ 54 ] , but Voice Memory acquires it from inference-time feedback, with backpropagation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26410v1#S3 — 3 The Voice Memory Method。Evaluation：https://arxiv.org/html/2607.26410v1#S7 — 7 Analysis: Meaning versus Surface Error; https://arxiv.org/html/2607.26410v1#S7.SS3 — 7.3 Error Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26410v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26410v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：A memory written by one model family improves a reader from another, because explicit rules travel where weights cannot; the same trust can be trained into weights from audio [ 54 ] , but Voice Memory acquires it from inference-time feedback, with backpropagation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26410:end -->

<!-- review:SF-2026-ARXIV-2607-26411:start -->
### Do Unified Multimodal Models Think in One Space? A Lens Through Cross-Branch Steering

<!-- claim:SF-2026-ARXIV-2607-26411:start -->Unified multimodal models (UMMs) aim to integrate understanding and generation within a single architecture, yet it remains unclear whether these capabilities share a unified and transferable semantic space. This question is fundamentally challenging, as the two branches operate over heterogeneous representations (text tokens vs.\ visual latents) and distinct training objectives, making direct comparison difficult. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26411:end -->

**为什么进入候选分母。** 摘要首要问题为“Unified multimodal models (UMMs) aim to integrate understanding and generation within a single architecture, yet it remains unclear whether these capabilities share a unified and transferable semantic space.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this, we introduce \emph{cross-branch semantic steering}, an intervention-based framework that extracts semantic directions from one branch and applies them to the other.

**证据证明什么。** We show that steering vectors learned from the understanding branch can transfer to generation, enabling controllable image synthesis and improved semantic faithfulness.

**证据没有证明什么。** Although CAA generally enables precise cross-branch control, failures still arise when the model cannot reliably localize the target object or disentangle the intended semantic attribute. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26411v1#A1.SS4 — A.4 LLM Steering Methods Detail; https://arxiv.org/html/2607.26411v1#A2.SS4 — B.4 Full Evaluation of Understanding-to-Generation Steering across UMM Architectures。Evaluation：https://arxiv.org/html/2607.26411v1#A3 — Appendix C Additional Ablation Study and Analysis; https://arxiv.org/html/2607.26411v1#A1 — Appendix A Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.26411v1#A4.SS2 — D.2 Failure Case Analysis; https://arxiv.org/html/2607.26411v1#A6 — Appendix F Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Although CAA generally enables precise cross-branch control, failures still arise when the model cannot reliably localize the target object or disentangle the intended semantic attribute.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26411:end -->

<!-- review:SF-2026-ARXIV-2607-26417:start -->
### SCOUT: Per-Context Reset Curricula for Sparse-Reward Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-26417:start -->Sparse-reward reinforcement learning often fails because rollouts from the unassisted evaluation start rarely reach later task stages. Reset curricula address this by starting some training rollouts from easier intermediate states, called scaffolds. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26417:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse-reward reinforcement learning often fails because rollouts from the unassisted evaluation start rarely reach later task stages.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce SCOUT, an online, learner-agnostic reset controller that gives every context its own curriculum.

**证据证明什么。** A counting construction shows that synchronized global pacing can be insufficient when contexts need conflicting amounts of assisted practice.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26417v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26417v1#Sx4 — Experimental Setup; https://arxiv.org/html/2607.26417v1#Sx5 — Results。Limitations / counterevidence：https://arxiv.org/html/2607.26417v1#Sx6 — Discussion; https://arxiv.org/html/2607.26417v1#Sx7 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26417:end -->

<!-- review:SF-2026-ARXIV-2607-26444:start -->
### StrataCL: Fabric-Native Communication Library for Production Supernodes

<!-- claim:SF-2026-ARXIV-2607-26444:start -->Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck. Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26444:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern distributed AI workloads run across hundreds of accelerators, making communication a major bottleneck.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration.

**证据证明什么。** Across three production workloads, StrataCL improves LLM inference throughput by 1.9x, reduces P99 TTFT by 2.2x, and reduces LLM and Recsys training iteration time by 1.4x and 1.3x, respectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26444v1#S2.SS1 — 2.1. Supernode Architectures; https://arxiv.org/html/2607.26444v1#S4 — 4. Design Overview。Evaluation：https://arxiv.org/html/2607.26444v1#A1 — Appendix A Extended Microbenchmark; https://arxiv.org/html/2607.26444v1#A3 — Appendix C Workload Partitioning Overhead Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26444v1#S11 — 11. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26444:end -->

<!-- review:SF-2026-ARXIV-2607-26448:start -->
### Mergeable Model-Side Aggregation States for Long-Context Language Models

<!-- claim:SF-2026-ARXIV-2607-26448:start -->A known limitation of long-context language models is their increasingly unreliable performance in non-additive, set-based aggregation as context length grows. Examples include cardinality estimation, set relationships, and grouped statistics, which widely exist in logs, program outputs, tables, and multi-turn conversations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26448:end -->

**为什么进入候选分母。** 摘要首要问题为“A known limitation of long-context language models is their increasingly unreliable performance in non-additive, set-based aggregation as context length grows.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** On a fixed 1,200-task Oolong-Synth subset, our method reached 91.1% on Qwen and 99.3% on Gemma.

**证据证明什么。** On a matched set of 174 items, our method improved over direct full-context reasoning by 63.2 points on Qwen and 56.3 points on Gemma.

**证据没有证明什么。** Different from external execution methods, it does not require an additional generate–execute–return cycle. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26448v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.26448v1#A7 — Appendix G Statistical Analysis and Evaluation Scope; https://arxiv.org/html/2607.26448v1#A7.SS1 — G.1 Evaluation and statistical analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26448v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Different from external execution methods, it does not require an additional generate–execute–return cycle.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26448:end -->

<!-- review:SF-2026-ARXIV-2607-26452:start -->
### CG-World: A Large-Scale World-State Dataset and Protocol for World Models

<!-- claim:SF-2026-ARXIV-2607-26452:start -->World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure. We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26452:end -->

**为什么进入候选分母。** 摘要首要问题为“World models must learn the joint dynamics of states, actions, events, and observations, yet existing video, robotics, and simulation datasets usually capture only part of this structure.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines.

**证据证明什么。** Results show that CG-World provides reusable structured supervision for controlled generation, action modeling, and embodied policy transfer.

**证据没有证明什么。** 6 Future Work Future work will use strictly registered real–virtual scene pairs to measure biases in observations, dynamics, and intervention effects; develop error and uncertainty models; and calibrate industrial CG mechanisms and sampling ranges with limited real-world data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26452v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26452v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.26452v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26452v1#S7 — 7 Discussion and Conclusion; https://arxiv.org/html/2607.26452v1#S6 — 6 Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6 Future Work Future work will use strictly registered real–virtual scene pairs to measure biases in observations, dynamics, and intervention effects; develop error and uncertainty models; and calibrate industrial CG mechanisms and sampling ranges with limited real-world data.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26452:end -->

<!-- review:SF-2026-ARXIV-2607-26455:start -->
### ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models

<!-- claim:SF-2026-ARXIV-2607-26455:start -->Large language models (LLMs) have demonstrated strong capabilities in knowledge acquisition and reasoning, yet their ability to retain previously acquired knowledge under repeated updates remains insufficiently understood. Existing evaluation paradigms primarily focus on single-step reasoning or static knowledge editing, which fail to capture the temporal dynamics of knowledge retention and degradation during continual model modification. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26455:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) have demonstrated strong capabilities in knowledge acquisition and reasoning, yet their ability to retain previously acquired knowledge under repeated updates remains insufficiently understood.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we propose ForgetBench, a benchmark designed to systematically characterize forgetting behavior in LLMs under continual knowledge editing.

**证据证明什么。** Extensive experiments across diverse models and editing methods demonstrate that existing approaches fail to strike a balance between long-term retention and generalization quality.

**证据没有证明什么。** Future work could integrate continuously evolving corpora to enhance realism. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26455v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.26455v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.26455v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26455v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work could integrate continuously evolving corpora to enhance realism.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26455:end -->

<!-- review:SF-2026-ARXIV-2607-26464:start -->
### PUDA: An AI-Native Hardware Harness for Self-Driving Laboratories

<!-- claim:SF-2026-ARXIV-2607-26464:start -->Physical Unified Device Architecture (PUDA) is an AI-native hardware harness for self-driving laboratories (SDLs). Rather than building a human-centered graphical user interface (GUI) orchestration layer, PUDA creates a command-line runtime environment that lets agents observe, orient, decide, and act over experiments while hardware execution remains deterministic, atomic, and auditable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26464:end -->

**为什么进入候选分母。** 摘要首要问题为“Physical Unified Device Architecture (PUDA) is an AI-native hardware harness for self-driving laboratories (SDLs).”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** It is a practical execution and data environment for agentic SDLs; the broader physical AI implication is that PUDA provides an AI-native hardware harness for AI systems to interact with physical tools.

**证据证明什么。** It is a practical execution and data environment for agentic SDLs; the broader physical AI implication is that PUDA provides an AI-native hardware harness for AI systems to interact with physical tools.

**证据没有证明什么。** 6 Conclusions and Future Work Self-driving laboratories need more than automated instruments and optimization algorithms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26464v1#S2 — 2 The PUDA Architecture; https://arxiv.org/html/2607.26464v1#S2.SS1 — 2.1 Design Philosophy。Evaluation：https://arxiv.org/html/2607.26464v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26464v1#S2 — 2 The PUDA Architecture。Limitations / counterevidence：https://arxiv.org/html/2607.26464v1#S6 — 6 Conclusions and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6 Conclusions and Future Work Self-driving laboratories need more than automated instruments and optimization algorithms.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26464:end -->

<!-- review:SF-2026-ARXIV-2607-26470:start -->
### CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG

<!-- claim:SF-2026-ARXIV-2607-26470:start -->Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns. However, existing RAG systems typically represent conversational memory as raw dialogue history, rewritten queries, or unstructured summaries, making it difficult to recover the specific prior reasoning steps and evidence required for follow-up queries. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26470:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-turn information-seeking conversations require both multi-hop reasoning and long-range dependency tracking across turns.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Building on this insight, we introduce MuMu-QA, a benchmark for multi-turn multi-hop RAG with explicit cross-turn sub-question dependency annotations, and CMT-RAG, a complementary memory framework for this setting.

**证据证明什么。** Experiments on MuMu-QA and corpus-level RAG benchmarks show that CMT-RAG consistently outperforms five categories of RAG baselines in answer accuracy.

**证据没有证明什么。** As CMT-RAG relies on accurate sub-question decomposition and dependency prediction, future work will focus on more robust trace generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26470v1#A2.SS1 — B.1 Architecture; https://arxiv.org/html/2607.26470v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.26470v1#A3 — Appendix C Inference and Evaluation; https://arxiv.org/html/2607.26470v1#A3.SS5 — C.5 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.26470v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：As CMT-RAG relies on accurate sub-question decomposition and dependency prediction, future work will focus on more robust trace generation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26470:end -->

<!-- review:SF-2026-ARXIV-2607-26475:start -->
### DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch

<!-- claim:SF-2026-ARXIV-2607-26475:start -->Long-context inference is becoming a fundamental capability for modern LLM serving, especially driven by emerging agentic applications. Yet it faces a severe memory wall that the KV cache scales proportionally with increasing context length and request concurrency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26475:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context inference is becoming a fundamental capability for modern LLM serving, especially driven by emerging agentic applications.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we present DualDecoder, a lightweight serving system for long-context LLM inference that enables efficient sparse KV cache retrieval from host memory.

**证据证明什么。** Experimental results show that DualDecoder improves decoding throughput by up to 2.62$\times$ over state-of-the-art systems while preserving decoding latency and model quality.

**证据没有证明什么。** It exploits the strong predictability of sparse KV indices across consecutive decoding tokens to optimize future retrievals. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26475v1#S5 — 5. DualDecoder Design; https://arxiv.org/html/2607.26475v1#S5.SS1 — 5.1. System Overview。Evaluation：https://arxiv.org/html/2607.26475v1#S3.SS2 — 3.2. Memory Capacity Analysis; https://arxiv.org/html/2607.26475v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26475v1#S8 — 8. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：It exploits the strong predictability of sparse KV indices across consecutive decoding tokens to optimize future retrievals.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26475:end -->

<!-- review:SF-2026-ARXIV-2607-26491:start -->
### LLMET: Enabling Cross-Layer Evaluation of Emerging M3D Memories for Energy-Efficient LLM Serving

<!-- claim:SF-2026-ARXIV-2607-26491:start -->The energy consumption of Large Language Model (LLM) serving is becoming a major system challenge as deployment scales, driven by hardware power and thermal constraints and rising electricity costs. A key contributor to chip energy dissipation is data movement between limited on-chip cache and off-chip High Bandwidth Memory (HBM). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26491:end -->

**为什么进入候选分母。** 摘要首要问题为“The energy consumption of Large Language Model (LLM) serving is becoming a major system challenge as deployment scales, driven by hardware power and thermal constraints and rising electricity costs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** These results highlight the promise of ultra-large on-chip memories for energy-efficient LLM serving systems.

**证据证明什么。** These results highlight the promise of ultra-large on-chip memories for energy-efficient LLM serving systems.

**证据没有证明什么。** Conclusion and Future Work This work first presents LLMET, a validated cross-layer framework for co-designing LLM serving system and memory technologies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26491v1#S2.SS1 — 2.1. LLM Serving Architecture; https://arxiv.org/html/2607.26491v1#S3 — 3. Proposed LLMET Framework。Evaluation：https://arxiv.org/html/2607.26491v1#S4 — 4. Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.26491v1#S6 — 6. Conclusion and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion and Future Work This work first presents LLMET, a validated cross-layer framework for co-designing LLM serving system and memory technologies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26491:end -->

<!-- review:SF-2026-ARXIV-2607-26512:start -->
### Evidence-Ledger Adjudication for Claim-Evidence Traceability

<!-- claim:SF-2026-ARXIV-2607-26512:start -->AI agents can draft claims faster than authors can check whether the cited or retrieved evidence supports them. We study evidence-ledger adjudication: a claim-evidence traceability workflow that pairs each claim with an evidence packet, assigns a support relation, and routes unsupported, contradicted, or mixed-evidence claims back to the author. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26512:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents can draft claims faster than authors can check whether the cited or retrieved evidence supports them.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We study evidence-ledger adjudication: a claim-evidence traceability workflow that pairs each claim with an evidence packet, assigns a support relation, and routes unsupported, contradicted, or mixed-evidence claims back to the author.

**证据证明什么。** These results show that evidence-ledger adjudication can turn heterogeneous evidence packets into an auditable traceability layer for AI-assisted writing.

**证据没有证明什么。** These slices are useful targets for future evidence-packet design and adjudication calibration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26512v1#S5.SS3 — 5.3 Positioning against adjacent systems。Evaluation：https://arxiv.org/html/2607.26512v1#S2.SS1 — 2.1 External claim-verification benchmarks; https://arxiv.org/html/2607.26512v1#S2.SS3 — 2.3 Agent evaluation through artifacts。Limitations / counterevidence：https://arxiv.org/html/2607.26512v1#S6 — 6 Discussion; https://arxiv.org/html/2607.26512v1#S7 — 7 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：These slices are useful targets for future evidence-packet design and adjudication calibration.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26512:end -->

<!-- review:SF-2026-ARXIV-2607-26513:start -->
### Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-26513:start -->Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world. This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26513:end -->

**为什么进入候选分母。** 摘要首要问题为“Current Vision-Language-Action (VLA) models rely mainly on 2D inputs, neglecting the rich object structural information and commonsense knowledge inherent in the 3D physical world.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** This deficiency restricts their spatial awareness and adaptability for complex, high-precision manipulation.

**证据证明什么。** Our experimental results show consistent improvements in success rate and learning efficiency across supervised and reinforcement learning settings, demonstrating the effectiveness of structured, concept-based guidance for VLA post-training.

**证据没有证明什么。** However, this cost is incurred only during the concept initialization stage and does not affect the inference latency of the VLA policy during execution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26513v1#A1.SS1 — A.1 Analytic Concept System; https://arxiv.org/html/2607.26513v1#A1.SS2 — A.2 Network Architecture。Evaluation：https://arxiv.org/html/2607.26513v1#A2 — Appendix B Experimental Setup; https://arxiv.org/html/2607.26513v1#S4 — 4 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.26513v1#A4 — Appendix D Limitations and Future Work; https://arxiv.org/html/2607.26513v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：However, this cost is incurred only during the concept initialization stage and does not affect the inference latency of the VLA policy during execution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26513:end -->

<!-- review:SF-2026-ARXIV-2607-26515:start -->
### HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models

<!-- claim:SF-2026-ARXIV-2607-26515:start -->We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision. A systematic study reveals that the dominant source of degradation in FP4 RL is not training-side quantization error but rollout activation quantization: outliers stretch the dynamic range so far that a large number of activation values underflow to zero under FP4. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26515:end -->

**为什么进入候选分母。** 摘要首要问题为“We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision.

**证据证明什么。** Together, these results establish HiF4 as the enabling format for end-to-end FP4 RL post-training, and Rollout-ResQ as the activation-side mechanism that makes the gap to BF16 closable.

**证据没有证明什么。** 6 Limitations and Future Directions Due to the lack of native FP4 hardware support, all experiments rely on FP4 simulations 1 1 1 The simulated quantization code is publicly available at https://github.com/global-computing-consortium/HiFloat4 . where simulation overhead dominates training time, preventing direct measurement of real speedup and efficiency gains. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26515v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.26515v1#S5 — 5 Experiments; https://arxiv.org/html/2607.26515v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26515v1#S6 — 6 Limitations and Future Directions; https://arxiv.org/html/2607.26515v1#S7 — 7 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Limitations and Future Directions Due to the lack of native FP4 hardware support, all experiments rely on FP4 simulations 1 1 1 The simulated quantization code is publicly available at https://github.com/global-computing-consortium/HiFloat4 . where simulation overhead dominates training time, preventing direct measurement of real speedup and efficiency gains.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26515:end -->

<!-- review:SF-2026-ARXIV-2607-26520:start -->
### A Graph-Native Bitemporal Memory Store for Conversational AI Agents

<!-- claim:SF-2026-ARXIV-2607-26520:start -->Conversational AI agents commonly lack persistent memory across sessions. The obvious fixes like injecting full chat histories into the context window, or delegating to a third-party memory service, either exhaust the model's context budget or send personal data through infrastructure the user does not control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26520:end -->

**为什么进入候选分母。** 摘要首要问题为“Conversational AI agents commonly lack persistent memory across sessions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** The store separates immutable memory identity from mutable content: a stable Memory node owns graph relations, while append-only MemoryVersion nodes carry content, embeddings, tags, valid-time and transaction-time intervals. An update closes the current transaction interval and appends a new version instead of overwriting history; separate current-state and full-history HNSW indexes, plus interval filters, let the agent choose present-state or as-of retrieval through explicit tools.

**证据证明什么。** On the stated 60-question, seed-42 LongMemEval sample, the implementation shows that identity/version separation can preserve updates and expose current-state versus as-of queries. Current-state retrieval reaches 46.7% R@10 overall and 80% on knowledge-update questions, while the lower 37.5% time-travel result on eight non-null temporal cases exposes a concrete over-fetch-and-filter dilution failure rather than hiding it.

**证据没有证明什么。** The experiment is not the full 500-question benchmark and does not demonstrate reliable multi-session aggregation, preference inference, or recall of assistant-generated content because only user turns are indexed. It also does not establish privacy, deletion compliance, multi-writer consistency, long-lived embedding migration, or production-scale graph/index cost. These are explicit system boundaries, not evidence that bitemporal storage alone solves agent memory.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26520v1#S3.SS1 — III-A Data Model; https://arxiv.org/html/2607.26520v1#S3.SS2 — III-B Bitemporal Model; https://arxiv.org/html/2607.26520v1#S4.SS2 — IV-B Agent Tool-Use Loop。Evaluation：https://arxiv.org/html/2607.26520v1#S5.SS1 — V-A Benchmark and Protocol; https://arxiv.org/html/2607.26520v1#S5.SS2 — V-B Results; https://arxiv.org/html/2607.26520v1#S5.SS5 — V-E Temporal Reasoning and the Dilution Effect。Limitations / counterevidence：https://arxiv.org/html/2607.26520v1#S6 — VI Conclusion; https://arxiv.org/html/2607.26520v1#S6.SS2 — VI-B Future Directions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** Append-only versions make provenance, correction, and time travel explicit, but increase storage, interval/index maintenance, write amplification, and retrieval dilution. Keeping relationships on stable identity nodes avoids graph rewrites, yet assumes relationship meaning survives content revisions. A simpler current-state store remains appropriate when history has no product or audit value; derived counters, preference summaries, assistant turns, and re-ranking require separate owners rather than being inferred from raw retrieval.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26520:end -->

<!-- review:SF-2026-ARXIV-2607-26523:start -->
### The Art of Not Forgetting A Local Learning Architecture for Continual Learning

<!-- claim:SF-2026-ARXIV-2607-26523:start -->We introduce CMP (Cognitive Memory Primitive), a continual-learning architecture that repre?sents inputs as sparse relational codes, stores them in a two-tier competitive memory, and learns through local updates without end-to-end backpropagation through its feature-generating system. We investigate whether combining sparse representations, local learning, and persistent memory can reduce catastrophic forgetting relative to conventional backpropagation-based continual?learning approaches. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26523:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce CMP (Cognitive Memory Primitive), a continual-learning architecture that repre?sents inputs as sparse relational codes, stores them in a two-tier competitive memory, and learns through local updates without end-to-end backpropagation through its feature-generating system.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce CMP (Cognitive Memory Primitive), a continual-learning architecture that repre?sents inputs as sparse relational codes, stores them in a two-tier competitive memory, and learns through local updates without end-to-end backpropagation through its feature-generating system.

**证据证明什么。** We investigate whether combining sparse representations, local learning, and persistent memory can reduce catastrophic forgetting relative to conventional backpropagation-based continual?learning approaches.

**证据没有证明什么。** At the same time, the present study identifies several important limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26523v1#S3 — 3 Architecture。Evaluation：https://arxiv.org/html/2607.26523v1#A3 — Appendix C Historical depth-line result; https://arxiv.org/html/2607.26523v1#A5 — Appendix E Preliminary scaling experiment。Limitations / counterevidence：https://arxiv.org/html/2607.26523v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.26523v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：At the same time, the present study identifies several important limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26523:end -->

<!-- review:SF-2026-ARXIV-2607-26536:start -->
### TPCD: Tone-Pressure Contrastive Decoding and the Label-Free Gating Bottleneck in Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-26536:start -->High-pressure prompts can push vision-language models (VLMs) into unsupported commitments, such as reading illegible text, reporting indeterminate times, or affirming absent objects. This paper asks whether the pressure-induced distribution itself can serve as a contrastive-decoding negative branch. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26536:end -->

**为什么进入候选分母。** 摘要首要问题为“High-pressure prompts can push vision-language models (VLMs) into unsupported commitments, such as reading illegible text, reporting indeterminate times, or affirming absent objects.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This paper asks whether the pressure-induced distribution itself can serve as a contrastive-decoding negative branch.

**证据证明什么。** Treating this LLaVA analysis as the design split, full $n=800$ negative and $n=780$ matched-positive held-out runs on GLM-4.6V and Llama-3.2-Vision show that simple gates can improve over safe neutralization, with sensitivity analyses bounding the weak time-positive subtask.

**证据没有证明什么。** The text gate is operationally label-free but not independently validated, because its negative success is tied to the same surface predicates used by the scorer for several categories. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26536v1#S3 — 3 Method; https://arxiv.org/html/2607.26536v1#S4.SS4 — 4.4 Full Cross-Model Stress Test。Evaluation：https://arxiv.org/html/2607.26536v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26536v1#S4.SS2 — 4.2 Gate Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.26536v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26536v1#S6 — 6 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The text gate is operationally label-free but not independently validated, because its negative success is tied to the same surface predicates used by the scorer for several categories.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26536:end -->

<!-- review:SF-2026-ARXIV-2607-26566:start -->
### ServerlessT2I: Efficient Text-to-Image Workflow Serving on a Serverless Platform

<!-- claim:SF-2026-ARXIV-2607-26566:start -->Text-to-image (T2I) workflows are increasingly deployed on serverless platforms because users often compose customized workflows and invoke them intermittently. Existing platforms typically deploy each workflow as an opaque GPU function, provisioning, placing, and scaling all constituent models in the workflow together. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26566:end -->

**为什么进入候选分母。** 摘要首要问题为“Text-to-image (T2I) workflows are increasingly deployed on serverless platforms because users often compose customized workflows and invoke them intermittently.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we present ServerlessT2I, a serverless-native system that decomposes a T2I workflow into loosely coupled model functions that can be independently managed and scheduled.

**证据证明什么。** To make this decomposition efficient, ServerlessT2I harvests slack GPU memory left idle by compute-bound T2I inference to build a data plane that reduces model loading and data communication overheads. \sys{} further introduces a fair scheduler for multi-tenant serving.

**证据没有证明什么。** However, we identify following limitations, each of which undermines an essential property of serverless computing ( Schleier-Smith et al., 2021 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26566v1#S3 — 3. Motivation and System Overview; https://arxiv.org/html/2607.26566v1#S3.SS2 — 3.2. System Overview。Evaluation：https://arxiv.org/html/2607.26566v1#S8 — 8. Evaluation; https://arxiv.org/html/2607.26566v1#S8.SS2 — 8.2. End-to-end Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26566v1#S10 — 10. Conclusions; https://arxiv.org/html/2607.26566v1#S2.SS3 — 2.3. Limitations of Current Practices。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, we identify following limitations, each of which undermines an essential property of serverless computing ( Schleier-Smith et al., 2021 ) .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-PRODUCTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26566:end -->

<!-- review:SF-2026-ARXIV-2607-26571:start -->
### From Tokens to Watt-hours: Analytical Energy Estimation for LLM Inference on Modern GPUs

<!-- claim:SF-2026-ARXIV-2607-26571:start -->The operational energy consumption of large language model (LLM) inference is becoming an increasingly important component of the environmental footprint of deployed AI systems. However, direct measurement of inference energy often requires hardware telemetry, power instrumentation, or infrastructure-specific monitoring, limiting its applicability in comparative studies, early-stage system design, and sustainability reporting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26571:end -->

**为什么进入候选分母。** 摘要首要问题为“The operational energy consumption of large language model (LLM) inference is becoming an increasingly important component of the environmental footprint of deployed AI systems.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** The operational energy consumption of large language model (LLM) inference is becoming an increasingly important component of the environmental footprint of deployed AI systems.

**证据证明什么。** The resulting estimates are not intended to replace physical power measurements; rather, they provide transparent, reproducible, and assumption-explicit approximations suitable for model comparison, green-coding analysis, and design-time evaluation of LLM inference workloads.

**证据没有证明什么。** 5 Limitations and Conclusion The proposed estimator is limited to accelerator-side operational energy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26571v1#A3 — Appendix C Model Architecture Details; https://arxiv.org/html/2607.26571v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.26571v1#S4 — 4 Results and Evaluation; https://arxiv.org/html/2607.26571v1#S3 — 3 Evaluation Setup and Assumptions。Limitations / counterevidence：https://arxiv.org/html/2607.26571v1#S5 — 5 Limitations and Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：5 Limitations and Conclusion The proposed estimator is limited to accelerator-side operational energy.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26571:end -->

<!-- review:SF-2026-ARXIV-2607-26582:start -->
### Level, Sharpness, and Corpus: Why Zero-Shot OOD Detector Rankings Do Not Transfer

<!-- claim:SF-2026-ARXIV-2607-26582:start -->Selecting a zero-shot out-of-distribution (OOD) detector for a new deployment is typically based on benchmark rankings, implicitly assuming that the highest-ranked detector will transfer across domains. Through a controlled portability audit across seventeen in-distribution datasets, three vision-language models, and seven representative zero-shot OOD detectors, we find that detector rankings reverse across deployments, every detector exceeds $80\%$ FPR95 on at least one domain, and the preferred detector depends on both the in-distribution data and the underlying VLM. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26582:end -->

**为什么进入候选分母。** 摘要首要问题为“Selecting a zero-shot out-of-distribution (OOD) detector for a new deployment is typically based on benchmark rankings, implicitly assuming that the highest-ranked detector will transfer across domains.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Corpus-free detectors rely on different combinations of absolute match level and relative or spatial sharpness, while WordNet-based methods additionally depend on external semantic coverage.

**证据证明什么。** Without OOD samples, auxiliary corpora, or learned fusion, CEG reduces detector sensitivity and improves GL-MCM from $38.1$ to $28.8$ and MCM from $42.6$ to $30.5$ family-balanced FPR95.

**证据没有证明什么。** A portability audit across ID domains and VLMs showed that this assumption does not hold. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26582v1#S3 — 3 The Portability Audit; https://arxiv.org/html/2607.26582v1#S4 — 4 Mechanism: Level and Sharpness Are Complementary Evidence; https://arxiv.org/html/2607.26582v1#S5 — 5 From Diagnosis to Deployment: The Complementary Evidence Guard。Evaluation：https://arxiv.org/html/2607.26582v1#S4.SS1 — 4.1 External Semantic Evidence Depends on Corpus Coverage; https://arxiv.org/html/2607.26582v1#A1 — Appendix A Appendix Overview and Organization; https://arxiv.org/html/2607.26582v1#A6 — Appendix F Protected All-Domain Audit。Limitations / counterevidence：https://arxiv.org/html/2607.26582v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.26582v1#A5.SS1 — E.1 Non-compensatory property of CEG。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A portability audit across ID domains and VLMs showed that this assumption does not hold.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26582:end -->

<!-- review:SF-2026-ARXIV-2607-26587:start -->
### One Run Is Not an Idea: The Implementation Lottery in Automated Research

<!-- claim:SF-2026-ARXIV-2607-26587:start -->Automated research systems use experimental scores both to deliver artifacts and to decide which ideas to retain, transfer, and pursue. Yet one run scores one implementation of an idea. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26587:end -->

**为什么进入候选分母。** 摘要首要问题为“Automated research systems use experimental scores both to deliver artifacts and to decide which ideas to retain, transfer, and pursue.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Automated research systems use experimental scores both to deliver artifacts and to decide which ideas to retain, transfer, and pursue.

**证据证明什么。** Before a score guides idea-level branching, transfer, or research memory, evidence should cover multiple implementations.

**证据没有证明什么。** LOO also depends on a frozen cross-card alignment because the provider did not expose sampling seeds. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26587v1#S4 — 4 Study Design; https://arxiv.org/html/2607.26587v1#S3.SSx2 — Independent Implementations。Evaluation：https://arxiv.org/html/2607.26587v1#S5 — 5 Results; https://arxiv.org/html/2607.26587v1#S4 — 4 Study Design。Limitations / counterevidence：https://arxiv.org/html/2607.26587v1#S7 — 7 Scope and Limitations; https://arxiv.org/html/2607.26587v1#S9 — 9 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：LOO also depends on a frozen cross-card alignment because the provider did not expose sampling seeds.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26587:end -->

<!-- review:SF-2026-ARXIV-2607-26596:start -->
### Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution

<!-- claim:SF-2026-ARXIV-2607-26596:start -->Multimodal large language models (MLLMs) have demonstrated remarkable capabilities by integrating visual and textual understanding within a unified transformer architecture. However, fine-tuning all parameters of these models for visual instruction tuning is computationally expensive and often unnecessary, as the representation requirements for visual and textual tokens diverge significantly in the deeper layers of the network. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26596:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models (MLLMs) have demonstrated remarkable capabilities by integrating visual and textual understanding within a unified transformer architecture.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this paper, we propose Decoupled Visual Processing (DVP), an efficient training framework that replaces the upper decoder layers of a pretrained LLM with a lightweight, independently trainable single transformer block dedicated exclusively to visual token processing.

**证据证明什么。** Experiments on the LLaVA-1.5 framework demonstrate that DVP achieves competitive performance on MME, POPE, and ChartQA benchmarks while training only a fraction of the total parameters, suggesting that visual representations in MLLMs can be effectively learned through a decoupled, parameter-efficient pathway.

**证据没有证明什么。** Our results demonstrate that visual tokens do not require the full depth of LLM processing, and that a lightweight, dedicated visual pathway can effectively substitute for multiple decoder layers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26596v1#S5.SS1 — 5.1 Implications for MLLM Architecture Design; https://arxiv.org/html/2607.26596v1#A1 — Appendix A Architecture Details。Evaluation：https://arxiv.org/html/2607.26596v1#A2 — Appendix B Detailed Benchmark Results; https://arxiv.org/html/2607.26596v1#A3 — Appendix C Computational Cost Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26596v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.26596v1#S5 — 5 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Our results demonstrate that visual tokens do not require the full depth of LLM processing, and that a lightweight, dedicated visual pathway can effectively substitute for multiple decoder layers.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26596:end -->

<!-- review:SF-2026-ARXIV-2607-26604:start -->
### WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback

<!-- claim:SF-2026-ARXIV-2607-26604:start -->Knowledge-base construction and querying are typically optimized in isolation: retrieval-augmented agents operate over a fixed, externally maintained index, whereas construction receives no signal from downstream use. We present WikiLoop, a feedback-coupled framework that jointly learns to build and navigate an agent-native Wiki, a persistent linked-page knowledge base designed for machine navigation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26604:end -->

**为什么进入候选分母。** 摘要首要问题为“Knowledge-base construction and querying are typically optimized in isolation: retrieval-augmented agents operate over a fixed, externally maintained index, whereas construction receives no signal from downstream use.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present WikiLoop, a feedback-coupled framework that jointly learns to build and navigate an agent-native Wiki, a persistent linked-page knowledge base designed for machine navigation.

**证据证明什么。** Without dataset-specific training, WikiLoop also improves over the same-backbone LLM-Wiki, base on HotpotQA and MuSiQue.

**证据没有证明什么。** 5 Limitations Candidate patches are evaluated on isolated Wiki copies and discarded after scoring. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26604v1#S3 — 3 Method; https://arxiv.org/html/2607.26604v1#S3.SS1 — 3.1 Problem Formulation and Framework Overview。Evaluation：https://arxiv.org/html/2607.26604v1#A2 — Appendix B Complete Experimental Results; https://arxiv.org/html/2607.26604v1#A1 — Appendix A Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.26604v1#S5 — 5 Limitations; https://arxiv.org/html/2607.26604v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：5 Limitations Candidate patches are evaluated on isolated Wiki copies and discarded after scoring.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26604:end -->

<!-- review:SF-2026-ARXIV-2607-26608:start -->
### Understanding Knowledge Transfer Mechanism in Heterogeneous MLLM Fusion: A Simple Linear Approach

<!-- claim:SF-2026-ARXIV-2607-26608:start -->Training-free fusion of heterogeneous multimodal large language models (MLLMs) provides a direct route for cross-scale capability transfer, yet improvements in aggregate performance do not reveal what a smaller model actually inherits. Existing studies are largely designed and evaluated on limited task sets or aggregate metrics; as evaluation expands to broader task collections, whether different capabilities can transfer across scales remains poorly understood. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26608:end -->

**为什么进入候选分母。** 摘要首要问题为“Training-free fusion of heterogeneous multimodal large language models (MLLMs) provides a direct route for cross-scale capability transfer, yet improvements in aggregate performance do not reveal what a smaller model actually inherits.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To investigate this question, we introduce Cross-Scale Directional Parameter Injection (CDPI), a simple linear probe to analyze cross-scale knowledge transfer during heterogeneous fusion.

**证据证明什么。** Component-wise ablations further show that high-level reasoning gains arise primarily from the language model, while ratio analysis finds that positive selective transfer occurs mainly in the small-ratio regime.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26608v1#Sx3 — Method; https://arxiv.org/html/2607.26608v1#A2.SS1 — B.1 Models and Configurations。Evaluation：https://arxiv.org/html/2607.26608v1#A2 — Appendix B Experimental and Evaluation Details; https://arxiv.org/html/2607.26608v1#A4 — Appendix D Complete Benchmark-Wise Best-of-Sweep Results。Limitations / counterevidence：https://arxiv.org/html/2607.26608v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26608:end -->

<!-- review:SF-2026-ARXIV-2607-26618:start -->
### FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA

<!-- claim:SF-2026-ARXIV-2607-26618:start -->Federated PEFT enables LLMs to collaboratively adapt to decentralized private data without sharing raw examples. However, task heterogeneity across clients can cause cross-task interference and gradient conflicts during aggregation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26618:end -->

**为什么进入候选分母。** 摘要首要问题为“Federated PEFT enables LLMs to collaboratively adapt to decentralized private data without sharing raw examples.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose FedWeave, a framework that adopts asymmetric aggregation, separating expert aggregation from router optimization to meet these two requirements.

**证据证明什么。** On a heterogeneous multi-task benchmark with mainstream LLM backbones, FedWeave consistently outperforms strong baselines, while ablations verify the effectiveness of our design.

**证据没有证明什么。** Future work should test natural, drifting streams with privacy-preserving online alignment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26618v1#Sx3 — Method; https://arxiv.org/html/2607.26618v1#A1 — Appendix A Implementation and Reproducibility Details。Evaluation：https://arxiv.org/html/2607.26618v1#A3 — Appendix C Theoretical Analysis; https://arxiv.org/html/2607.26618v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26618v1#Sx5 — Limitations; https://arxiv.org/html/2607.26618v1#Sx6 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work should test natural, drifting streams with privacy-preserving online alignment.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26618:end -->

<!-- review:SF-2026-ARXIV-2607-26627:start -->
### Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs, and Failure Modes

<!-- claim:SF-2026-ARXIV-2607-26627:start -->Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently verified in parallel by a larger target model. Recent approaches introduce lossy verification schemes to further improve efficiency by relaxing strict distributional matching. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26627:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative Decoding (SD) accelerates large language model inference by allowing a lightweight draft model to propose tokens that are subsequently verified in parallel by a larger target model.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we present a principled analysis of the distributions induced by lossy verification methods.

**证据证明什么。** Recent approaches introduce lossy verification schemes to further improve efficiency by relaxing strict distributional matching.

**证据没有证明什么。** Third, our theoretical results characterize the per-token and per-position distributional gap under standard SD and EAGLE-3 tree verification, but the analysis assumes the specific truncation and collaborative rules we formalize and may not directly cover every future lossy verification scheme. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26627v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26627v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.26627v1#A2 — Appendix B Verification Analysis; https://arxiv.org/html/2607.26627v1#A3 — Appendix C Extended Results。Limitations / counterevidence：https://arxiv.org/html/2607.26627v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.26627v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Third, our theoretical results characterize the per-token and per-position distributional gap under standard SD and EAGLE-3 tree verification, but the analysis assumes the specific truncation and collaborative rules we formalize and may not directly cover every future lossy verification scheme.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26627:end -->

<!-- review:SF-2026-ARXIV-2607-26633:start -->
### NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-based Request Placement

<!-- claim:SF-2026-ARXIV-2607-26633:start -->Modern LLMs and their agentic applications are broadening the range of serving workloads, spanning context lengths from a few hundred tokens to hundreds of thousands. As these requests frequently interleave within the same serving window, LLM serving systems must handle highly heterogeneous mixed-length workloads. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26633:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern LLMs and their agentic applications are broadening the range of serving workloads, spanning context lengths from a few hundred tokens to hundreds of thousands.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we present NELSSA, an LLM serving system that integrates GPUs with real-world Processing-near-Memory (PNM) accelerator devices to efficiently support mixed-length workloads.

**证据证明什么。** Across mixed-length LLM workloads, NELSSA improves decode throughput by up to 5.5x in tokens/sec and reduces P99 latency by up to 15x compared to GPU-only baselines.

**证据没有证明什么。** To address this, we propose extending the system with orchestrator-level adaptive routing as future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26633v1#S3 — 3. Design Principles and Architecture Overview; https://arxiv.org/html/2607.26633v1#S5.SS1 — 5.1. NELSSA System Architecture。Evaluation：https://arxiv.org/html/2607.26633v1#S8 — 8. Experimental Results; https://arxiv.org/html/2607.26633v1#S7 — 7. Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.26633v1#S10 — 10. Discussion; https://arxiv.org/html/2607.26633v1#S11 — 11. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：To address this, we propose extending the system with orchestrator-level adaptive routing as future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26633:end -->

<!-- review:SF-2026-ARXIV-2607-26637:start -->
### Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability

<!-- claim:SF-2026-ARXIV-2607-26637:start -->Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organization pays. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26637:end -->

**为什么进入候选分母。** 摘要首要问题为“Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present the first systematic exploration of filesystem-based memory for LLM agents.

**证据证明什么。** The study turns the filesystem default from an assumption into a design space for agent memory.

**证据没有证明什么。** It depends equally on the consumer: the verbatim Episode log leads under a strong execution agent and inverts under a weak one, where only Curated skills+mem (GS) survives the capability drop. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26637v1#A2 — Appendix B Example Memory Filesystems; https://arxiv.org/html/2607.26637v1#S2 — 2 Formalizing Filesystem-Based Agent Memory。Evaluation：https://arxiv.org/html/2607.26637v1#S4 — 4 Results and Analysis; https://arxiv.org/html/2607.26637v1#A3 — Appendix C Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.26637v1#S5 — 5 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：It depends equally on the consumer: the verbatim Episode log leads under a strong execution agent and inverts under a weak one, where only Curated skills+mem (GS) survives the capability drop.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26637:end -->

<!-- review:SF-2026-ARXIV-2607-26643:start -->
### Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting

<!-- claim:SF-2026-ARXIV-2607-26643:start -->Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world applications. A promising solution is to treat skills as trainable states and optimize them in the same way as model parameters in neural network training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26643:end -->

**为什么进入候选分母。** 摘要首要问题为“Enabling large language model (LLM) agents to accumulate and reuse experience from past interactions remains a central challenge in real-world applications.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose SkillBoost, a three-stage framework that mitigates both risks: structured exploitation localizes observed failures to editable skill components, prior-guided exploration draws on prior knowledge in the LLM to generate diverse repair candidates, and verified acceptance commits a candidate only when it improves performance within a regression bound.

**证据证明什么。** Experiments across 23 model--benchmark configurations show that SkillBoost achieves state-of-the-art performance while mitigating overfitting, outperforming both human-crafted and LLM-generated skills.

**证据没有证明什么。** Root cause: The output-format section instructs “place only the option label inside the <answer> tag, no explanations.” This cleanliness constraint was over-generalized by the model into “do not explain at all,” causing it to emit bare <answer>X</answer> responses (18 characters) without any intermediate reasoning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26643v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.26643v1#A1.SSx2 — Cross-Benchmark Patterns; https://arxiv.org/html/2607.26643v1#A2.SSx3 — 3. Failure Mode Cluster Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26643v1#A2.SSx3 — 3. Failure Mode Cluster Analysis; https://arxiv.org/html/2607.26643v1#Sx4.SSx5 — Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Root cause: The output-format section instructs “place only the option label inside the <answer> tag, no explanations.” This cleanliness constraint was over-generalized by the model into “do not explain at all,” causing it to emit bare <answer>X</answer> responses (18 characters) without any intermediate reasoning.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26643:end -->

<!-- review:SF-2026-ARXIV-2607-26648:start -->
### The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy

<!-- claim:SF-2026-ARXIV-2607-26648:start -->Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates. We argue the energy dividend of sparsity is not a property of SNNs but of the task. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26648:end -->

**为什么进入候选分母。** 摘要首要问题为“Spiking neural networks (SNNs) are promoted as an energy-efficient substrate because sparse, event-driven activity replaces dense multiply-accumulates with cheap accumulates.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We argue the energy dividend of sparsity is not a property of SNNs but of the task.

**证据证明什么。** A layer-wise input floor further caps op reduction under dense input, isolating event-driven perception as where neuromorphic hardware wins.

**证据没有证明什么。** 6 Limitations (1) Perception uses rate-coded FashionMNIST as an event-stream stand-in; native N-MNIST/DVS and a real event-input accounting are needed. (2) The spiking Transformer is single-layer, char-level, small-scale; scaling it (and quantifying the KV-cache memory cost directly) is the key next step. (3) The bound is single-step; a tightening across and to task loss (not just distinguishability) is open. (4) Energy is a 45 nm proxy; measured Loihi 2 / SpiNNaker2 energy would convert estimate to measurement. (5) The mechanism sweep uses a narrow trainable window ( ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26648v1#S2 — 2 Method; https://arxiv.org/html/2607.26648v1#S4.SS2 — 4.2 Sequence modeling hits a ceiling。Evaluation：https://arxiv.org/html/2607.26648v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26648v1#S6 — 6 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：6 Limitations (1) Perception uses rate-coded FashionMNIST as an event-stream stand-in; native N-MNIST/DVS and a real event-input accounting are needed. (2) The spiking Transformer is single-layer, char-level, small-scale; scaling it (and quantifying the KV-cache memory cost directly) is the key next step. (3) The bound is single-step; a tightening across and to task loss (not just distinguishability) is open. (4) Energy is a 45 nm proxy; measured Loihi 2 / SpiNNaker2 energy would convert estimate to measurement. (5) The mechanism sweep uses a narrow trainable window ( ).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26648:end -->

<!-- review:SF-2026-ARXIV-2607-26652:start -->
### AIGen: Automating AI Bill of Materials Generation Through Hybrid MLOps Integration

<!-- claim:SF-2026-ARXIV-2607-26652:start -->The responsible development and deployment of artificial intelligence (AI) systems requires rigorous documentation of their constituent artifacts, e.g., datasets, model weights, training pipelines, and runtime dependencies. Although the Software Package Data Exchange (SPDX) 3.0 standard introduced native support for AI and dataset profiles, practical tooling capable of generating standards-compliant AI Bills of Materials (AIBoMs) in an automated and extensible manner remains scarce. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26652:end -->

**为什么进入候选分母。** 摘要首要问题为“The responsible development and deployment of artificial intelligence (AI) systems requires rigorous documentation of their constituent artifacts, e.g., datasets, model weights, training pipelines, and runtime dependencies.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** AIGen works on top of the MLflow MLOps framework and combines mining heuristics with Large Language Models to generate AIBoMs.

**证据证明什么。** Tool URL: https://github.com/danielebifolco/AIGen Tool Video: https://youtu.be/\_nAbXDWfVL4

**证据没有证明什么。** Future work will extend the current open-source evaluation with an industrial validation conducted in collaboration with our partner company. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26652v1#S2 — 2. Architecture; https://arxiv.org/html/2607.26652v1#S3 — 3. Implementation and Usage Workflow。Evaluation：https://arxiv.org/html/2607.26652v1#S4 — 4. Preliminary Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26652v1#S6 — 6. Conclusions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future work will extend the current open-source evaluation with an industrial validation conducted in collaboration with our partner company.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26652:end -->

<!-- review:SF-2026-ARXIV-2607-26654:start -->
### Constitutional Midtraining: Content Presence Drives Alignment Gains

<!-- claim:SF-2026-ARXIV-2607-26654:start -->Post-training alignment is often shallow, eroding under fine-tuning. It remains untested as to whether constitutional midtraining interventions can produce durable alignment when cleanly isolated from post-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26654:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training alignment is often shallow, eroding under fine-tuning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** It remains untested as to whether constitutional midtraining interventions can produce durable alignment when cleanly isolated from post-training.

**证据证明什么。** Constitutionally midtrained models outperformed the control on alignment generalization and durability, notably on blackmail: SFT instilled a blackmail propensity in all models, but constitutional midtraining blunted it, with the advantage surviving benign fine-tuning (-17.5pp).

**证据没有证明什么。** C.5 Limitations of the Centrality Measure Semantic centrality, as operationalised here, may not correspond exactly to “foundational” in the sense used by hierarchical-learning-theory accounts of curriculum ordering (§ 2.3 of the main paper): our measure captures embedding-space density, not a causal or logical dependency structure among values. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26654v1#S2.SS2 — 2.2 Constitutional Approaches to Alignment; https://arxiv.org/html/2607.26654v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.26654v1#A3 — Appendix C Centrality Analysis: Additional Detail; https://arxiv.org/html/2607.26654v1#A6 — Appendix F Evaluation: Extended Detail。Limitations / counterevidence：https://arxiv.org/html/2607.26654v1#S5.SS6 — 5.6 Limitations and Future Work.; https://arxiv.org/html/2607.26654v1#A3.SS5 — C.5 Limitations of the Centrality Measure。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：C.5 Limitations of the Centrality Measure Semantic centrality, as operationalised here, may not correspond exactly to “foundational” in the sense used by hierarchical-learning-theory accounts of curriculum ordering (§ 2.3 of the main paper): our measure captures embedding-space density, not a causal or logical dependency structure among values.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26654:end -->

<!-- review:SF-2026-ARXIV-2607-26657:start -->
### Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control

<!-- claim:SF-2026-ARXIV-2607-26657:start -->World generative models are typically used through what they produce: a rendered future, a video-conditioned action, or latent context computed by a costly generative branch. We argue that their more reusable asset is the computation that constructs a future. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26657:end -->

**为什么进入候选分母。** 摘要首要问题为“World generative models are typically used through what they produce: a rendered future, a video-conditioned action, or latent context computed by a costly generative branch.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present Enfold, which transfers this computation into a representation predicted from the current visual context and language instruction.

**证据证明什么。** Representation analyses show that it suppresses nuisance variation and preferentially captures changes that emerge over longer horizons.

**证据没有证明什么。** This representation is not shaped by action gradients, yet remains useful for both future generation and control. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26657v1#S4 — 4 Method; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration。Evaluation：https://arxiv.org/html/2607.26657v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.26657v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.26657v1#A2.SS3 — B.3 Future-Video Evaluation。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：This representation is not shaped by action gradients, yet remains useful for both future generation and control.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26657:end -->

<!-- review:SF-2026-ARXIV-2607-26661:start -->
### AgenticCANN: Automated Ascend C Operator Generation via Knowledge-Augmented Agentic Evolution

<!-- claim:SF-2026-ARXIV-2607-26661:start -->Ascend C operator optimization is critical for NPU (Neural Processing Unit) inference performance but requires deep hardware expertise. While large language models (LLMs) have shown promise in automated CUDA kernel generation, the fundamentally different programming model of Ascend C introduces unique challenges that remain unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26661:end -->

**为什么进入候选分母。** 摘要首要问题为“Ascend C operator optimization is critical for NPU (Neural Processing Unit) inference performance but requires deep hardware expertise.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In this paper, we propose AgenticCANN, a knowledge-augmented agentic evolution framework specifically tailored for automated Ascend C operator synthesis in low-corpus NPU environments.

**证据证明什么。** Extensive experiments on Huawei Ascend 910B across six operators spanning five pattern categories demonstrate that our method achieves 90 to 100 percent feasibility on elementwise and normalization operators, 56% on fusion operators, and up to 6.65$\times$ speedup on 1B Pangu model inference kernels.

**证据没有证明什么。** Limitations & Future Directions While AgenticCANN demonstrates strong results across elementwise and normalization operators, several limitations define the boundaries of the current framework and motivate concrete directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26661v1#Ax2 — B. Method Details; https://arxiv.org/html/2607.26661v1#Ax2.SSx1 — B.1. Algorithm Framework。Evaluation：https://arxiv.org/html/2607.26661v1#Ax3 — C. Experimental Benchmarks & Full Data Matrices; https://arxiv.org/html/2607.26661v1#Ax2.SSx5 — B.5. Experimental Infrastructure。Limitations / counterevidence：https://arxiv.org/html/2607.26661v1#Ax4 — D. Discussion and Future Work; https://arxiv.org/html/2607.26661v1#Ax4.SSx3 — D.3. Limitations & Future Directions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Limitations & Future Directions While AgenticCANN demonstrates strong results across elementwise and normalization operators, several limitations define the boundaries of the current framework and motivate concrete directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26661:end -->

<!-- review:SF-2026-ARXIV-2607-26688:start -->
### Nix to the Rescue for a Reproducible HPC-AI Software Stack

<!-- claim:SF-2026-ARXIV-2607-26688:start -->Reproducibility in HPC remains difficult under the constraints of production supercomputers: no root access, limited internet, and software stacks that increasingly span C/C++, Fortran, Python, MPI, and GPU runtimes. Traditional approaches based on environment modules and Conda require manual intervention to locate dependencies, leak system libraries into builds, and fail to compose across projects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26688:end -->

**为什么进入候选分母。** 摘要首要问题为“Reproducibility in HPC remains difficult under the constraints of production supercomputers: no root access, limited internet, and software stacks that increasingly span C/C++, Fortran, Python, MPI, and GPU runtimes.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Traditional approaches based on environment modules and Conda require manual intervention to locate dependencies, leak system libraries into builds, and fail to compose across projects.

**证据证明什么。** We discuss trade-offs against Spack and Guix, the development-versus-production split addressed via CMake presets, and current gaps in ML package coverage in Nixpkgs.

**证据没有证明什么。** The same mechanism handles dependencies available only as prebuilt vendor binaries. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2。Evaluation：https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2。Limitations / counterevidence：https://arxiv.org/pdf/2607.26688v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26688v1#page=2 — PDF page 2。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The same mechanism handles dependencies available only as prebuilt vendor binaries.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-PRODUCTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26688:end -->

<!-- review:SF-2026-ARXIV-2607-26694:start -->
### Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation

<!-- claim:SF-2026-ARXIV-2607-26694:start -->We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation. Users can change the prompt at any moment during generation, and the update becomes visible in real time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26694:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation.

**证据证明什么。** In long-form Arena comparisons, Visko Orbis 1.0 obtains the highest overall-preference and temporal-stability ratings among state-of-the-art real-time interactive video-generation systems.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26694v1#S3 — 3 Model; https://arxiv.org/html/2607.26694v1#S3.SS0.SSS0.Px1 — Model Formulation.。Evaluation：https://arxiv.org/html/2607.26694v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.26694v1#S5.SS0.SSS0.Px1 — Evaluation protocol.。Limitations / counterevidence：https://arxiv.org/html/2607.26694v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26694:end -->

<!-- review:SF-2026-ARXIV-2607-26710:start -->
### PowerAtlas: Towards Electricity-Computing Co-Scheduling for Power Systems

<!-- claim:SF-2026-ARXIV-2607-26710:start -->The rapid growth of AI workloads is turning data centers into large-scale, volatile, yet spatiotemporally flexible grid loads, creating an urgent need for coordinated electricity-computing scheduling. Under stringent grid constraints, schedules from general-purpose large language models (LLMs) are often infeasible, causing line-flow violations and unserved load. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26710:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid growth of AI workloads is turning data centers into large-scale, volatile, yet spatiotemporally flexible grid loads, creating an urgent need for coordinated electricity-computing scheduling.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present PowerAtlas, an LLM-agent framework for electricity-computing co-scheduling that integrates historical instances, domain knowledge, and physical constraints to produce joint decisions satisfying both grid operational rules and the service-level agreements (SLAs) of computing tasks.

**证据证明什么。** Experiments across eleven LLMs demonstrate the effectiveness of PowerAtlas under realistic physical operating conditions, with consistent feasibility and cost gains across three open-weight backbones.

**证据没有证明什么。** Limitations and Future Work Four limits of this study point directly at the next experiments. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26710v1#S4.SS2 — 4.2. Benchmark Design; https://arxiv.org/html/2607.26710v1#A1 — Appendix A ECBench Implementation Details。Evaluation：https://arxiv.org/html/2607.26710v1#S4.SS2 — 4.2. Benchmark Design; https://arxiv.org/html/2607.26710v1#S6 — 6. Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26710v1#A4.SS3 — D.3. Limitations and Future Work; https://arxiv.org/html/2607.26710v1#A4 — Appendix D Additional Notes and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Limitations and Future Work Four limits of this study point directly at the next experiments.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26710:end -->

<!-- review:SF-2026-ARXIV-2607-26712:start -->
### ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games

<!-- claim:SF-2026-ARXIV-2607-26712:start -->Latent world models support efficient model-predictive control by optimizing future control sequences in latent space and replanning in a receding-horizon manner. However, existing latent predictors often lack stable long-horizon rollout ability, and prediction accuracy alone does not ensure that rollouts remain responsive to the actions being planned. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26712:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models support efficient model-predictive control by optimizing future control sequences in latent space and replanning in a receding-horizon manner.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this issue, we propose ActSWM, an action-sensitive latent world model grounded in a transition-separation principle: a planning-useful latent dynamics model should keep alternative-action futures distinguishable and make the action associated with each local transition recoverable.

**证据证明什么。** Across step-drift analysis, closed-loop Minecraft planning, and cross-game local action recovery, ActSWM preserves larger action-dependent rollout gaps than existing baselines, improves task success in long-horizon interactive settings, and enables world-model-based action recovery from offline gameplay videos.

**证据没有证明什么。** These results establish action sensitivity as a core requirement for planning-oriented latent world models beyond future-state accuracy. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26712v1#A1 — Appendix A Model Architecture and Training Configuration; https://arxiv.org/html/2607.26712v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26712v1#A2 — Appendix B Step-Drift Evaluation Protocol; https://arxiv.org/html/2607.26712v1#A4 — Appendix D Cross-Game CEM Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.26712v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These results establish action sensitivity as a core requirement for planning-oriented latent world models beyond future-state accuracy.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26712:end -->

<!-- review:SF-2026-ARXIV-2607-26719:start -->
### Not In My Git Yard: Catching Backdoors at Commit and Release Time

<!-- claim:SF-2026-ARXIV-2607-26719:start -->Code-level backdoors-stealthy code changes that grant hidden privileges via secret triggers-pose a persistent threat to opensource software. Known attempts to inject such backdoors into widely used projects through malicious commits, tampered release packages, or compromised third-party dependencies, were stopped only by luck and manual review. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26719:end -->

**为什么进入候选分母。** 摘要首要问题为“Code-level backdoors-stealthy code changes that grant hidden privileges via secret triggers-pose a persistent threat to opensource software.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this work, we present Lily, an automated approach that strengthens open-source development and release processes against backdoor injection.

**证据证明什么。** Our experiments across hundreds of benign and backdoored commits and releases show that Lily achieves high detection accuracy with low false alarm rates, reliably identifies malicious code, resists adversarial attempts, and would have prevented real-world backdoor incidents.

**证据没有证明什么。** Given this context, evaluation methodologies commonly used for frequent but moderate-impact vulnerabilities (such as C memory bugs, which are often not exploitable ( Lacombe and Bardin, 2025 ) ) must be adapted to suit rarer but extremely high-impact threats. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26719v1#S3 — 3. The Lily Approach; https://arxiv.org/html/2607.26719v1#S4.SS4 — 4.4. Reusing Common System Call Types。Evaluation：https://arxiv.org/html/2607.26719v1#S5 — 5. Experimental Evaluation; https://arxiv.org/html/2607.26719v1#S5.SS1 — 5.1. Experimental Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.26719v1#S5.SS7 — 5.7. Threats to Result Generalizability; https://arxiv.org/html/2607.26719v1#S7 — 7. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Given this context, evaluation methodologies commonly used for frequent but moderate-impact vulnerabilities (such as C memory bugs, which are often not exploitable ( Lacombe and Bardin, 2025 ) ) must be adapted to suit rarer but extremely high-impact threats.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26719:end -->

<!-- review:SF-2026-ARXIV-2607-26722:start -->
### DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution

<!-- claim:SF-2026-ARXIV-2607-26722:start -->Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort. Therefore, recent research has increasingly explored harness self-evolution, which iteratively proposes, evaluates, and improves harnesses using historical trial experience. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26722:end -->

**为什么进入候选分母。** 摘要首要问题为“Harness plays a critical role in large language model agent performance, and building a high-performing harness requires substantial expert effort.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these limitations, we propose a new harness self-evolution method, named DREvo, which integrates function-level evidence anchoring, state-dependent evidence recalibration, and role-conditioned search intent distillation to determine which historical evidence remains valid and where the harness should evolve next.

**证据证明什么。** Therefore, recent research has increasingly explored harness self-evolution, which iteratively proposes, evaluates, and improves harnesses using historical trial experience.

**证据没有证明什么。** We identified two underlying limitations: historical evidence may become invalid as the harness state evolves , and it does not directly specify which component to modify or how to modify it . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26722v1#Sx3 — Proposed Approach。Evaluation：https://arxiv.org/html/2607.26722v1#Sx4.SSx2 — Experimental Results; https://arxiv.org/html/2607.26722v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26722v1#Sx5 — Conclusion and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We identified two underlying limitations: historical evidence may become invalid as the harness state evolves , and it does not directly specify which component to modify or how to modify it .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26722:end -->

<!-- review:SF-2026-ARXIV-2607-26754:start -->
### StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation

<!-- claim:SF-2026-ARXIV-2607-26754:start -->Recent game world models can generate visually realistic and interactive environments conditioned on player actions. However, games are not defined by pixels alone; they are governed by explicit mechanics, namely state-dependent rules that control health reduction, skill activation, and game termination. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26754:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent game world models can generate visually realistic and interactive environments conditioned on player actions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Furthermore, compared with models without explicit state modeling, our method improves mechanics fidelity in generated game rollouts by 18.6%.

**证据证明什么。** Experiments show that StatePlay achieves an average normalized L1 distance below 0.06 for state prediction.

**证据没有证明什么。** However, as publicly available datasets with synchronized state, frame and action remain limited, we focus our initial evaluation on Street Fighter 3 . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26754v1#S3.SS2 — 3.2 Model Architecture; https://arxiv.org/html/2607.26754v1#S1a — A Experimental Model Information。Evaluation：https://arxiv.org/html/2607.26754v1#S1a — A Experimental Model Information; https://arxiv.org/html/2607.26754v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26754v1#S5 — 5 Conclusions and Discussions; https://arxiv.org/html/2607.26754v1#S3a — C Failure Cases。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, as publicly available datasets with synchronized state, frame and action remain limited, we focus our initial evaluation on Street Fighter 3 .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26754:end -->

<!-- review:SF-2026-ARXIV-2607-26760:start -->
### Metis: Memory Foundation Model

<!-- claim:SF-2026-ARXIV-2607-26760:start -->Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models. However, agent memory is still primarily implemented through external modules, leaving the native memory capability largely unexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26760:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in AI agents have increasingly internalized native capabilities into their underlying foundation models, giving rise to multimodal foundation models and large reasoning models.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Based on this formulation, we propose Metis, the first prototype of memory foundation models.

**证据证明什么。** We show that native memory offers advantages in architecture, end-to-end optimization, and efficiency.

**证据没有证明什么。** Therefore, native memory still cannot be viewed as a complete replacement for external memory. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26760v1#A3 — Appendix C Update Designs across Model Scales; https://arxiv.org/html/2607.26760v1#S3 — 3 Metis Architecture。Evaluation：https://arxiv.org/html/2607.26760v1#A2 — Appendix B Extensive Experiment Results; https://arxiv.org/html/2607.26760v1#A5 — Appendix E Evaluation Implementation Details。Limitations / counterevidence：https://arxiv.org/html/2607.26760v1#S2.SS5 — 2.5 Discussion; https://arxiv.org/html/2607.26760v1#S8 — 8 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Therefore, native memory still cannot be viewed as a complete replacement for external memory.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26760:end -->

<!-- review:SF-2026-ARXIV-2607-26769:start -->
### See2Think: Do Multimodal Models Really Use Intermediate Visual States?

<!-- claim:SF-2026-ARXIV-2607-26769:start -->Multimodal large language models increasingly use sketches, annotations, tools, and intermediate images during reasoning, but it remains unclear whether they truly rely on these visual states. Existing benchmarks are limited both by task collections with narrow coverage or partially text-solvable samples and by evaluations that emphasize final answers without diagnosing how intermediate visual states are generated, rendered, and used. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26769:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models increasingly use sketches, annotations, tools, and intermediate images during reasoning, but it remains unclear whether they truly rely on these visual states.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce See2Think, a unified evaluation framework comprising See2ThinkBench and Visual Action-of-Thought (VAoT).

**证据证明什么。** Evaluating representative proprietary and open-source multimodal models, we find that visual reasoning is strongly model- and environment-dependent, with no single setting consistently dominating across tasks.

**证据没有证明什么。** First, our evaluation focuses on four representative multimodal models and may not capture the full diversity of current and future vision-language systems. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26769v1#S2.SS1 — 2.1 Task Design and Data Sources; https://arxiv.org/html/2607.26769v1#S8 — 8 Inference Prompts and Implementation Details。Evaluation：https://arxiv.org/html/2607.26769v1#S10 — 10 Complete Outcome and Paired-Intervention Results; https://arxiv.org/html/2607.26769v1#S10.SS1 — 10.1 Complete 1.2K Outcome Results。Limitations / counterevidence：https://arxiv.org/html/2607.26769v1#S6 — 6 Conclusion and Limitations; https://arxiv.org/html/2607.26769v1#S13.SS2 — 13.2 Process-level Failure Cases。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, our evaluation focuses on four representative multimodal models and may not capture the full diversity of current and future vision-language systems.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26769:end -->

<!-- review:SF-2026-ARXIV-2607-26773:start -->
### Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM

<!-- claim:SF-2026-ARXIV-2607-26773:start -->Latent communication in large language model (LLM)-based multi-agent systems (MAS) transmits continuous internal representations instead of text, but greater representational capacity does not establish that the receiver uses task-relevant information. End-task performance alone also cannot reveal whether an observed effect depends on message presence, content generated for the evaluated example, or information supplied by a separate agent. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26773:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent communication in large language model (LLM)-based multi-agent systems (MAS) transmits continuous internal representations instead of text, but greater representational capacity does not establish that the receiver uses task-relevant information.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a causal audit that applies controlled message replacements at the boundary where the sender-produced representation enters the receiver.

**证据证明什么。** These results show that aggregate accuracy does not identify how a latent message affects the receiver and motivate controlled message comparisons as a standard evaluation for latent communication.

**证据没有证明什么。** Our results show that aggregate performance alone does not identify the mechanism of latent communication. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26773v1#Sx3 — The Audit Framework。Evaluation：https://arxiv.org/html/2607.26773v1#Sx4 — Experiments and Results; https://arxiv.org/html/2607.26773v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26773v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Our results show that aggregate performance alone does not identify the mechanism of latent communication.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26773:end -->

<!-- review:SF-2026-ARXIV-2607-26777:start -->
### CodeSpec: Dual Executable Specifications for Agentic Long-Horizon Feature Development

<!-- claim:SF-2026-ARXIV-2607-26777:start -->LLM-based code agents have advanced repository-level software development through iterative interaction with codebases and tools. However, feature development requires integrating new behaviors into existing architectures through coherent cross-component functional chains. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26777:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based code agents have advanced repository-level software development through iterative interaction with codebases and tools.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We propose CodeSpec, a dual executable specification method for repository-level feature development.

**证据证明什么。** Results on the repository generation benchmark NL2Repo-Bench further demonstrate its generalizability.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26777v1#Sx3 — Method; https://arxiv.org/html/2607.26777v1#Sx4.SSx3 — Baselines and Implementation Details。Evaluation：https://arxiv.org/html/2607.26777v1#Sx5 — Experimental Results; https://arxiv.org/html/2607.26777v1#Sx2.SSx1 — Repository-level Feature Development Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.26777v1#Sx6 — Discussion; https://arxiv.org/html/2607.26777v1#Sx7 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26777:end -->

<!-- review:SF-2026-ARXIV-2607-26784:start -->
### SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution

<!-- claim:SF-2026-ARXIV-2607-26784:start -->Large language model agents often encounter related yet distinct tasks that share reusable solution patterns. Yet standard agentic reinforcement learning treats tasks as independent episodes, while existing approaches to skill learning either focus on repeated attempts of one task or use pipelines with multiple stages that entangle extraction, retrieval, and execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26784:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model agents often encounter related yet distinct tasks that share reusable solution patterns.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce SkillRise, a unified reinforcement learning framework for learning skills across tasks.

**证据证明什么。** Experiments on ALFWorld, WebShop, and ScienceWorld show that SkillRise achieves the strongest Pass@1 performance among the compared methods, with gains over the strongest baseline ranging from 2.3 to 8.5 percentage points.

**证据没有证明什么。** Moreover, due to computational constraints, our experiments are limited to models of up to 4B parameters, leaving evaluation at larger model scales for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26784v1#S3 — 3 Method; https://arxiv.org/html/2607.26784v1#S5.SS2 — 5.2 Performance across Model Sizes。Evaluation：https://arxiv.org/html/2607.26784v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26784v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26784v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.26784v1#S8 — 8 Limitation。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Moreover, due to computational constraints, our experiments are limited to models of up to 4B parameters, leaving evaluation at larger model scales for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26784:end -->

<!-- review:SF-2026-ARXIV-2607-26789:start -->
### CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation

<!-- claim:SF-2026-ARXIV-2607-26789:start -->Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input. A committed chunk therefore implies how observations should evolve, but accidental deviations can violate this expectation while the remaining actions continue to propagate the error: commit-time policy confidence cannot react to a deviation that occurs after dispatch, and observation-only anomaly scores lack an action-conditioned reference for separating expected effects from unexplained changes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26789:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) policies commonly execute long-horizon mobile manipulation through open-loop action chunks, issuing multiple actions without receiving new high-level visual input.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose CheckVLA, which verifies execution with a separately trained, frozen action-conditioned world model.

**证据证明什么。** These simulation results support action-conditioned verification as a way to restore feedback during chunked execution while keeping the repair consistent with inference latency.

**证据没有证明什么。** We report both all failures and the actionable subset, without excluding failures that the policy cannot repair. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26789v1#Sx3 — Method; https://arxiv.org/html/2607.26789v1#A5 — Appendix E Episodic Context Implementation。Evaluation：https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries; https://arxiv.org/html/2607.26789v1#A13 — Appendix M Episodic-Memory Interaction Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.26789v1#A12 — Appendix L Natural Failures and Distribution Shifts; https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We report both all failures and the actionable subset, without excluding failures that the policy cannot repair.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26789:end -->

<!-- review:SF-2026-ARXIV-2607-26791:start -->
### SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response

<!-- claim:SF-2026-ARXIV-2607-26791:start -->Large Language Model (LLM) agents are increasingly adopted in real-world security operations with access to host artifacts and command-line interfaces (CLIs), making it critical to thoroughly assess their security capabilities. However, existing cybersecurity benchmarks focus on pre-compromise settings where agents are placed in a clean and idealized environment before an attack occurs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26791:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents are increasingly adopted in real-world security operations with access to host artifacts and command-line interfaces (CLIs), making it critical to thoroughly assess their security capabilities.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we introduce SecRespond, the first benchmark for evaluating LLM agents on the post-compromise incident-response workflow.

**证据证明什么。** Experimental results show that although current agents can reliably uncover the problems exposed by alerts, they struggle to proactively investigate the disk for silent intrusions and to produce comprehensive, verified remediation plans, with no model achieving complete detection and remediation on any single range.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26791v1#A3.SS1 — C.1 Task Prompt for Linux Operating System; https://arxiv.org/html/2607.26791v1#A3.SS2 — C.2 Task Prompt for Windows Operating System。Evaluation：https://arxiv.org/html/2607.26791v1#A4 — Appendix D Supplementary Experimental Results; https://arxiv.org/html/2607.26791v1#A3.SS3 — C.3 Evaluation Prompt。Limitations / counterevidence：https://arxiv.org/html/2607.26791v1#S5 — 5 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26791:end -->

<!-- review:SF-2026-ARXIV-2607-26801:start -->
### FedTopo: Relation-Level Topology Sharing for Model-Heterogeneous Federated Learning

<!-- claim:SF-2026-ARXIV-2607-26801:start -->Federated learning (FL) enables collaborative learning over decentralized data silos without centralizing raw data. However, heterogeneous local architectures often induce non-aligned representation spaces, making it difficult to transfer global knowledge across silos. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26801:end -->

**为什么进入候选分母。** 摘要首要问题为“Federated learning (FL) enables collaborative learning over decentralized data silos without centralizing raw data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose FedTopo, a relation-level framework that encodes global knowledge as class relation topology, capturing how classes relate within each client rather than where they lie in feature space.

**证据证明什么。** Experiments on three datasets under eight heterogeneous backbones show that FedTopo consistently outperforms parameter-, distillation-, and prototype-sharing baselines, with low communication and no inference overhead.

**证据没有证明什么。** A limitation is that the communication cost grows quadratically with the number of classes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26801v1#S4 — IV Proposed Framework; https://arxiv.org/html/2607.26801v1#S4.SS1 — IV-A Framework Overview。Evaluation：https://arxiv.org/html/2607.26801v1#S5 — V Comparative Analysis; https://arxiv.org/html/2607.26801v1#S6 — VI Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26801v1#S7 — VII Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：A limitation is that the communication cost grows quadratically with the number of classes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26801:end -->

<!-- review:SF-2026-ARXIV-2607-26807:start -->
### Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA

<!-- claim:SF-2026-ARXIV-2607-26807:start -->While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions across manipulation tasks and, even worse, the unavailability of the kinematic signals at inference time. In this work, we first observe that most semantically distinct manipulation tasks reduce to multiple kinematic archetypes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26807:end -->

**为什么进入候选分母。** 摘要首要问题为“While MoE augments VLA via expert specialization, router suffers from ineffective expert routing owing to the kinematic heterogeneity of actions across manipulation tasks and, even worse, the unavailability of the kinematic signals at inference time.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Motivated by this finding, we propose Kinematics-supervised explicit routing (KinRT), a new paradigm that shifts from implicit, observation-driven expert routing to explicit, kinematics-guided expert dispatching.

**证据证明什么。** In this work, we first observe that most semantically distinct manipulation tasks reduce to multiple kinematic archetypes.

**证据没有证明什么。** Notably, KinRT achieves these gains with negligible additional inference cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26807v1#Sx3.SSx1 — KinRT’s Architecture and Design Philosophy; https://arxiv.org/html/2607.26807v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.26807v1#Sx4.SSx1 — Experimental Setups and Evaluation Metrics; https://arxiv.org/html/2607.26807v1#Sx3.SSx5 — DIYRobot Platform and Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.26807v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Notably, KinRT achieves these gains with negligible additional inference cost.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26807:end -->

<!-- review:SF-2026-ARXIV-2607-26809:start -->
### Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations

<!-- claim:SF-2026-ARXIV-2607-26809:start -->General-purpose robotic manipulation requires robots to perform diverse tasks in open-world environments while improving their skills over time. Despite recent progress in robotic manipulation, existing systems still primarily acquire manipulation skills in a static manner, where capabilities are learned for specific tasks or settings rather than adaptively evolving through physical interaction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26809:end -->

**为什么进入候选分母。** 摘要首要问题为“General-purpose robotic manipulation requires robots to perform diverse tasks in open-world environments while improving their skills over time.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To this end, we propose HERO, a self-improving hierarchical embodied agent that enables autonomous capability evolution from zero human demonstrations.

**证据证明什么。** Extensive experiments demonstrate that HERO substantially reduces human intervention during robotic data collection while achieving robust manipulation across diverse tasks, providing a promising path toward self-improving robotic systems.

**证据没有证明什么。** Limitations and Future Work In this work, we propose HERO, an agentic framework that bootstraps and consolidates robotic capabilities from zero human demonstrations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26809v1#Sx3 — Method; https://arxiv.org/html/2607.26809v1#Sx4.SSx4 — System Analysis。Evaluation：https://arxiv.org/html/2607.26809v1#Sx4 — Experiments; https://arxiv.org/html/2607.26809v1#Sx4.SSx4 — System Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26809v1#Sx5 — Limitations and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations and Future Work In this work, we propose HERO, an agentic framework that bootstraps and consolidates robotic capabilities from zero human demonstrations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26809:end -->

<!-- review:SF-2026-ARXIV-2607-26818:start -->
### Ripple: Real-Time Streaming Audio-Video Generation With Cross-Modal Recurrent Memory

<!-- claim:SF-2026-ARXIV-2607-26818:start -->Audio-video generative models achieve impressive quality but suffer from high latency, making them unsuitable for real-time applications. Although several streaming audio-video generation methods have been proposed, they remain costly and fail to support long-form generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26818:end -->

**为什么进入候选分母。** 摘要首要问题为“Audio-video generative models achieve impressive quality but suffer from high latency, making them unsuitable for real-time applications.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** To address this, we propose \textbf{Ripple}, a real-time joint audio-video generation system with a cross-modal recurrent memory mechanism.

**证据证明什么。** As a result, Ripple achieves ~28 FPS at 480P resolution, over faster than the teacher, while capable of coherent long-form generation.

**证据没有证明什么。** A promising direction for future work is to decouple identity and timbre preservation from motion dynamics. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26818v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26818v1#A3 — Appendix C Long-Video Benchmark; https://arxiv.org/html/2607.26818v1#A4 — Appendix D Additional Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.26818v1#A6 — Appendix F Limitation and Discussion; https://arxiv.org/html/2607.26818v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：A promising direction for future work is to decouple identity and timbre preservation from motion dynamics.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26818:end -->

<!-- review:SF-2026-ARXIV-2607-26819:start -->
### A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities

<!-- claim:SF-2026-ARXIV-2607-26819:start -->Open source communities have been flooded with AI-generated contributions. In defense, they have written contribution rules to regulate coding agents' behavior, spanning from a total ban, mandatory disclosure, to verification gates and human sign-offs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26819:end -->

**为什么进入候选分母。** 摘要首要问题为“Open source communities have been flooded with AI-generated contributions.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In defense, they have written contribution rules to regulate coding agents' behavior, spanning from a total ban, mandatory disclosure, to verification gates and human sign-offs.

**证据证明什么。** Our experiments on four frontier models show that today's agents almost never proactively retrieve the contribution rules.

**证据没有证明什么。** 5.3 Future Work Two directions follow directly from the findings. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26819v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26819v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.26819v1#S3 — 3 The RepoComplianceBench Benchmark; https://arxiv.org/html/2607.26819v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26819v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.26819v1#S5.SS3 — 5.3 Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：5.3 Future Work Two directions follow directly from the findings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26819:end -->

<!-- review:SF-2026-ARXIV-2607-26820:start -->
### Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions

<!-- claim:SF-2026-ARXIV-2607-26820:start -->As large language models (LLMs) evolve from standalone assistants into autonomous agents, ensuring their safety requires shifting beyond pointwise risk assessment to understand how risks emerge and unfold over long-horizon trajectories. In multi-turn interactions, malicious intent can be decomposed across seemingly harmless turns and gradually reconstructed through interaction trajectories, eventually resulting in safety failures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26820:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) evolve from standalone assistants into autonomous agents, ensuring their safety requires shifting beyond pointwise risk assessment to understand how risks emerge and unfold over long-horizon trajectories.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this limitation, we propose Recast, a safety risk forecasting framework that advances LLM safeguarding beyond turn-level violation detection to trajectory-level risk prediction.

**证据证明什么。** Extensive experiments across 7 risk categories show that Recast predicts 88.3% of future safety failures with an average lead time of 2.41 turns, while maintaining a false alarm rate of 12.3%, showcasing the effectiveness of trajectory-level forecasting in identifying emerging risks before safety violations occur.

**证据没有证明什么。** Future Risk Distribution Forecasting Intuitively, forecasting future risk requires modeling not only the current turn state but also the trajectory through which it emerges. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26820v1#S3 — 3 Method; https://arxiv.org/html/2607.26820v1#S3.SSx2 — Compositional Risk State and Transition Modeling。Evaluation：https://arxiv.org/html/2607.26820v1#A1.SSx3 — Additional Experimental Results; https://arxiv.org/html/2607.26820v1#A1.SSx1 — Details of Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.26820v1#S3.SSx3 — Future Risk Distribution Forecasting; https://arxiv.org/html/2607.26820v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future Risk Distribution Forecasting Intuitively, forecasting future risk requires modeling not only the current turn state but also the trajectory through which it emerges.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26820:end -->

<!-- review:SF-2026-ARXIV-2607-26825:start -->
### From Found to Designed: Concepts as a Design Axis for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-26825:start -->Large language models (LLMs) encode rich concept-like information, but represent it implicitly through distributed statistical associations rather than as explicit, structured, compositional concepts. Consequently, concept-level structure is typically \emph{found} rather than \emph{designed}: it is recovered after training through probing or dictionary learning, with no architectural guarantee of stability, compositionality, controllability, or alignment with human conceptual organization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26825:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) encode rich concept-like information, but represent it implicitly through distributed statistical associations rather than as explicit, structured, compositional concepts.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** This taxonomy reveals three broad patterns: inference-time approaches remain comparatively underexplored, related ideas have developed largely in isolation across pipeline stages, and externally grounded methods span the entire pipeline despite often being described under different terminology.

**证据证明什么。** Together, these observations motivate moving beyond recovering concept-like structure from trained models toward designing LLMs with explicit conceptual representations.

**证据没有证明什么。** We also do not adjudicate which pipeline stage or structural source is best for a given application, since that judgment depends on constraints (compute, need for post-hoc auditability, tolerance for architectural change) that vary by setting. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26825v1#S2 — 2 Position: Concepts as a Design Axis; https://arxiv.org/html/2607.26825v1#S5.SS0.SSS0.Px2 — Found versus designed.。Evaluation：https://arxiv.org/html/2607.26825v1#S5.SS0.SSS0.Px4 — No shared benchmark across cells.。Limitations / counterevidence：https://arxiv.org/html/2607.26825v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We also do not adjudicate which pipeline stage or structural source is best for a given application, since that judgment depends on constraints (compute, need for post-hoc auditability, tolerance for architectural change) that vary by setting.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-REPRESENTATION`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26825:end -->

<!-- review:SF-2026-ARXIV-2607-26828:start -->
### Budget-Aware LLM Discovery via Cost-Calibrated Frontier Utility

<!-- claim:SF-2026-ARXIV-2607-26828:start -->Large language models increasingly support scientific and algorithmic discovery through inference-time search over evaluated candidates. Existing adaptive discovery controllers assign credit based only on score progress, even though prompt length, retries, and guidance calls cause search actions to incur different token costs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26828:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly support scientific and algorithmic discovery through inference-time search over evaluated candidates.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce \textbf{CostAda}, a cost-calibrated adaptive controller built around \emph{cost-calibrated frontier utility}.

**证据证明什么。** CostAda reaches the strongest baseline's full-budget quality with at most half the budget on twelve of sixteen benchmark--backbone pairs while achieving the strongest mean final quality on all eight benchmarks under GLM-5 and GPT-5.4.

**证据没有证明什么。** 3.2 Failure of Cost-Blind Credit Call a controller cost-blind if its action distribution at every iteration depends only on the history of actions and observed scores, never on realized costs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26828v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.26828v1#A5 — Appendix E Per-Benchmark Budget-Cutoff Results; https://arxiv.org/html/2607.26828v1#A3 — Appendix C Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.26828v1#S3.SS2 — 3.2 Failure of Cost-Blind Credit; https://arxiv.org/html/2607.26828v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：3.2 Failure of Cost-Blind Credit Call a controller cost-blind if its action distribution at every iteration depends only on the history of actions and observed scores, never on realized costs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26828:end -->

<!-- review:SF-2026-ARXIV-2607-26831:start -->
### Language Models are not Equally Robust to Non-Canonical Tokenization across Languages

<!-- claim:SF-2026-ARXIV-2607-26831:start -->Despite the existence of exponentially many valid tokenizations for a given string, language models operate on a single canonical sequence deterministically produced by the tokenizer, leaving the broader tokenization space largely uncharacterized. In this paper, we investigate this overlooked space by studying the behavior of language models under non-canonical tokenizations across diverse languages. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26831:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite the existence of exponentially many valid tokenizations for a given string, language models operate on a single canonical sequence deterministically produced by the tokenizer, leaving the broader tokenization space largely uncharacterized.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The variation of tokenization invariance is systematic across languages.

**证据证明什么。** These results demonstrate that tokenization robustness is not a universal property of language models, but depends strongly on the language and its interaction with the tokenizer.

**证据没有证明什么。** Disentangling the independent contribution of these factors would require carefully controlled experiments that manipulate each variable in isolation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26831v1#S3 — 3 Methodology; https://arxiv.org/html/2607.26831v1#A1 — Appendix A Model Size And Budget。Evaluation：https://arxiv.org/html/2607.26831v1#A3 — Appendix C Results on Excluded Languages; https://arxiv.org/html/2607.26831v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26831v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26831v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Disentangling the independent contribution of these factors would require carefully controlled experiments that manipulate each variable in isolation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TOKENIZER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26831:end -->

<!-- review:SF-2026-ARXIV-2607-26836:start -->
### Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-26836:start -->LLM-based multi-agent systems (MAS) have exhibited remarkable capabilities in collaborative reasoning and decision-making, yet their interconnected communications introduce new systemic risk: localized hallucinations can propagate along agent communication chain, amplify through interactions, and ultimately trigger cascading failures. Existing countermeasures predominantly follow a post-hoc paradigm, identifying failures only after unsafe behaviors emerge, by which time harmful effects may have already spread throughout the agent network. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26836:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based multi-agent systems (MAS) have exhibited remarkable capabilities in collaborative reasoning and decision-making, yet their interconnected communications introduce new systemic risk: localized hallucinations can propagate along agent communication chain, amplify through interactions, and ultimately trigger cascading failures.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** By facilitating early intervention through upstream screening, HalluProp effectively complements post-hoc methods, highlighting the potential of pre-hoc risk inference for building more reliable multi-agent systems.

**证据证明什么。** Extensive experiments show that HalluProp accurately localizes faulty agents, achieving an average AUROC of 84.6%, while enabling sub-second diagnosis with over $65\times$ speedup over post-hoc methods.

**证据没有证明什么。** However, this approach is subject to recursive unreliability, as it essentially uses one unreliable agent to monitor another. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26836v1#S3 — 3 Method; https://arxiv.org/html/2607.26836v1#S3.SSx3 — System-Level Risk Inference。Evaluation：https://arxiv.org/html/2607.26836v1#S4.SSx4 — RQ3: Ablation Study and Configuration Analysis; https://arxiv.org/html/2607.26836v1#A1.SSx1 — Theoretical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26836v1#A1.SSx3 — Discussion on Intervention Strategies; https://arxiv.org/html/2607.26836v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, this approach is subject to recursive unreliability, as it essentially uses one unreliable agent to monitor another.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26836:end -->

<!-- review:SF-2026-ARXIV-2607-26843:start -->
### When Knowledge Changes: Metamorphic Testing of RAG Systems with Mutations

<!-- claim:SF-2026-ARXIV-2607-26843:start -->Retrieval-Augmented Generation (RAG)-based LLM systems rely on external document corpora that can evolve and change over time. However, current evaluation methodologies (e.g., RAGAS) assess correctness against static snapshots, failing to detect faults when routine updates, factual changes, or noise alter the underlying data. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26843:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG)-based LLM systems rely on external document corpora that can evolve and change over time.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a metamorphic testing framework that evaluates the consistency of RAG systems under corpus evolution.

**证据证明什么。** In a meta-evaluation against ground truth, our metamorphic oracle achieves F1 scores of 0.927-1.000, while the best RAGAS metric reaches only 0.570.

**证据没有证明什么。** While this is encouraging, their limited effectiveness on RepLiQA points to future work on alternative repair strategies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S3 — 3. System Model and Fault Taxonomy。Evaluation：https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S5 — 5. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26843v1#S8 — 8. Threats to Validity; https://arxiv.org/html/2607.26843v1#S9 — 9. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：While this is encouraging, their limited effectiveness on RepLiQA points to future work on alternative repair strategies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26843:end -->

<!-- review:SF-2026-ARXIV-2607-26845:start -->
### Thinking Under Uncertainty: Evidence Use and Information-Seeking in Language Models

<!-- claim:SF-2026-ARXIV-2607-26845:start -->Inference-time thinking improves the performance of large language models, but aggregate outcomes do not reveal whether models use available evidence more effectively or seek information that could improve future decisions. We distinguish these responses by measuring action preference, thinking length, and reported confidence under matched uncertainty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26845:end -->

**为什么进入候选分母。** 摘要首要问题为“Inference-time thinking improves the performance of large language models, but aggregate outcomes do not reveal whether models use available evidence more effectively or seek information that could improve future decisions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We distinguish these responses by measuring action preference, thinking length, and reported confidence under matched uncertainty.

**证据证明什么。** In this controlled decision setting, thinking improved how models acted on current evidence, while neither measured signature supported a shift toward a more information-seeking policy.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26845v1#S2 — 2 Methods; https://arxiv.org/html/2607.26845v1#A1.SS1 — A.1 Models and Thinking Modes。Evaluation：https://arxiv.org/html/2607.26845v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.26845v1#A2 — Appendix B Measurement and Analysis Details。Limitations / counterevidence：https://arxiv.org/html/2607.26845v1#S4 — 4 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26845:end -->

<!-- review:SF-2026-ARXIV-2607-26849:start -->
### ToxScreen: Detecting Whether an LLM Has Been Poisoned

<!-- claim:SF-2026-ARXIV-2607-26849:start -->As large language models (LLMs) are deployed in high-stakes domains, adversaries may poison training data to implant backdoors: hidden triggers that covertly manipulate model behavior at inference time. We ask whether a defender can recover such a trigger under realistic affordances, namely white-box access to the weights and knowledge of the behavior of concern, but no training data, no trusted reference model, no knowledge of the trigger, and no certainty that the model is poisoned. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26849:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) are deployed in high-stakes domains, adversaries may poison training data to implant backdoors: hidden triggers that covertly manipulate model behavior at inference time.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Finally, no method reliably surfaces every backdoor, but a broadly jailbreakable model is itself anomalous, a useful signal even when the exact trigger is not recovered.

**证据证明什么。** We find a phenomenon whereby backdoors operate via different mechanistic strategies than jailbreaks, allowing defenders to filter jailbreaks.

**证据没有证明什么。** We are curious how trigger recovery would work when the trigger is not describable in a few tokens. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26849v1#A6 — Appendix F Implementation Details; https://arxiv.org/html/2607.26849v1#S4.SS3 — 4.3 Models。Evaluation：https://arxiv.org/html/2607.26849v1#S3 — 3 ToxScreen: Backdoor Defense Benchmark; https://arxiv.org/html/2607.26849v1#S4 — 4 Experimental Set-up。Limitations / counterevidence：https://arxiv.org/html/2607.26849v1#S7 — 7 Discussion and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We are curious how trigger recovery would work when the trigger is not describable in a few tokens.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26849:end -->

<!-- review:SF-2026-ARXIV-2607-26862:start -->
### ReCo: Reweighting GRPO Against Distributional Concentration

<!-- claim:SF-2026-ARXIV-2607-26862:start -->Group Relative Policy Optimization (GRPO) has become a standard reinforcement learning method for post-training language models. Recent work shows that GRPO can reduce the base model's reasoning capacity and underperform it in Pass@k when k is large, indicating reduced coverage of reasoning paths. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26862:end -->

**为什么进入候选分母。** 摘要首要问题为“Group Relative Policy Optimization (GRPO) has become a standard reinforcement learning method for post-training language models.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose ReCo, a reweighting method that addresses both effects.

**证据证明什么。** Recent work shows that GRPO can reduce the base model's reasoning capacity and underperform it in Pass@k when k is large, indicating reduced coverage of reasoning paths.

**证据没有证明什么。** Moreover, ReCo reweights gradients after rollouts are sampled from the policy, but does not directly change the sampling process itself. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26862v1#A2.SS3 — B.3 Combining ReCo with Existing GRPO Methods; https://arxiv.org/html/2607.26862v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.26862v1#A1.SS2 — A.2 Evaluation Details; https://arxiv.org/html/2607.26862v1#A2 — Appendix B Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26862v1#Sx1 — Limitations and Discussion; https://arxiv.org/html/2607.26862v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Moreover, ReCo reweights gradients after rollouts are sampled from the policy, but does not directly change the sampling process itself.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26862:end -->

<!-- review:SF-2026-ARXIV-2607-26865:start -->
### Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware Deferral for Edge LLM Agents

<!-- claim:SF-2026-ARXIV-2607-26865:start -->LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems. Yet, when deployed at the edge, they must tightly manage their reasoning budget while remaining reliable and deferring to a cloud-side model only when local uncertainty is too high to act safely. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26865:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents following the ReAct paradigm are promising enablers of complex multi-step tasks, including multi-hop question answering, code generation, and control of physical AI systems.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose Think Short, Defer Smart (TSDS), a framework that synergistically integrates a lightweight convergence probe, which halts on-device reasoning once the intended action has stabilized, with a perplexity-based deferral rule that escalates uncertain actions to a cloud-side model.

**证据证明什么。** TSDS reduces per-episode thinking compute by 43%-65% over deferral-only baselines across HotpotQA, MBPP, and the household robot task, while maintaining certified reward and cloud-call rate guarantees.

**证据没有证明什么。** Across all four benchmarks, TSDS simultaneously satisfies the certified reward floor and the cloud-call budget, while consuming substantially fewer thought tokens than deferral-only baselines. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26865v1#A5 — Appendix E Probe Architecture Details。Evaluation：https://arxiv.org/html/2607.26865v1#A7 — Appendix G Additional Experimental Details; https://arxiv.org/html/2607.26865v1#A7.SS1 — G.1 Convergence Probe Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.26865v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Across all four benchmarks, TSDS simultaneously satisfies the certified reward floor and the cloud-call budget, while consuming substantially fewer thought tokens than deferral-only baselines.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26865:end -->

<!-- review:SF-2026-ARXIV-2607-26873:start -->
### SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-26873:start -->Test-time reinforcement learning (TTRL) enables language models to self-evolve at inference time without labeled feedback. Existing methods rely on answer voting and therefore do not extend naturally to open-ended generation, where valid responses cannot be mapped to a shared canonical answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26873:end -->

**为什么进入候选分母。** 摘要首要问题为“Test-time reinforcement learning (TTRL) enables language models to self-evolve at inference time without labeled feedback.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Existing methods rely on answer voting and therefore do not extend naturally to open-ended generation, where valid responses cannot be mapped to a shared canonical answer.

**证据证明什么。** Across two model configurations, two in-domain benchmarks, and four OOD benchmarks, SERPO improves HealthBench and ResearchQA by up to 20.63 and 20.31 points over the corresponding base models, raises the six-benchmark macro-average by up to 8.06 points, and supports OOD transfer and continued cross-benchmark evolution.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26873v1#S4 — 4 Method: SERPO; https://arxiv.org/html/2607.26873v1#A2 — Appendix B Complete SERPO Implementation。Evaluation：https://arxiv.org/html/2607.26873v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.26873v1#A4 — Appendix D Evaluation Protocol and Additional Analyses。Limitations / counterevidence：https://arxiv.org/html/2607.26873v1#S6 — 6 Limitations and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26873:end -->

<!-- review:SF-2026-ARXIV-2607-26903:start -->
### From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence

<!-- claim:SF-2026-ARXIV-2607-26903:start -->The key bottleneck in embodied AI is not model architecture but data. Although billions of human manipulation videos exist online, robots cannot directly learn from them due to the embodiment gap between human morphology and robot hardware. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26903:end -->

**为什么进入候选分母。** 摘要首要问题为“The key bottleneck in embodied AI is not model architecture but data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce Pegasus, a low-resource framework that bridges this gap by translating human demonstrations into robot-learnable data through structured knowledge transfer.

**证据证明什么。** Results demonstrate reliable cross-embodiment translation and show that robot data generation can be reframed from a hardware collection problem into a scalable, low-resource knowledge transfer problem.

**证据没有证明什么。** 5.3 Limitations Pegasus still depends on VideoLLMs for accurate task decomposition, and reasoning errors may propagate through the pipeline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26903v1#S3 — 3 Method: Pegasus。Evaluation：https://arxiv.org/html/2607.26903v1#S4 — 4 Experiments; https://arxiv.org/html/2607.26903v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26903v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26903v1#S5.SS3 — 5.3 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：5.3 Limitations Pegasus still depends on VideoLLMs for accurate task decomposition, and reasoning errors may propagate through the pipeline.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26903:end -->

<!-- review:SF-2026-ARXIV-2607-26913:start -->
### Prior Directions: Why GUI Grounding Gets Locked in the Past

<!-- claim:SF-2026-ARXIV-2607-26913:start -->Vision-language models often use descriptions of earlier visual states to make decisions about the current scene. When the scene changes, stale language can redirect an otherwise correct visual judgment toward an outdated answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26913:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models often use descriptions of earlier visual states to make decisions about the current scene.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** When the scene changes, stale language can redirect an otherwise correct visual judgment toward an outdated answer.

**证据证明什么。** Controlled interventions show that removing the component aligned with the Prior Directions restores visual grounding, whereas removing an equally large orthogonal component has little effect.

**证据没有证明什么。** 9 Conclusion Visual lock-in reflects how prior-induced change is organized, not how large that change is. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26913v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26913v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.26913v1#A1 — Appendix A Experimental and Prompt Details; https://arxiv.org/html/2607.26913v1#A2 — Appendix B Exact Prior-Force Results。Limitations / counterevidence：https://arxiv.org/html/2607.26913v1#S8 — 8 Limitations; https://arxiv.org/html/2607.26913v1#S9 — 9 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：9 Conclusion Visual lock-in reflects how prior-induced change is organized, not how large that change is.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26913:end -->

<!-- review:SF-2026-ARXIV-2607-26922:start -->
### Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models

<!-- claim:SF-2026-ARXIV-2607-26922:start -->Multi-agent LLM pipeline systems break down the task among multiple roles for better reasoning, but are benchmarked mainly with large-scale commercial models. In this study, we investigate Parishad, a structured multi-agent system involving five roles, by deploying it on Qwen2.5-7B-Instruct, a local model, on two datasets: GSM8K (500 questions) and HumanEval (164 questions), compared with prompting directly and two-call self-refinement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26922:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent LLM pipeline systems break down the task among multiple roles for better reasoning, but are benchmarked mainly with large-scale commercial models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The multi-agent system drops GSM8K accuracy from 75.0\% to 45.0\% with JSON data format due to the error accumulation problem.

**证据证明什么。** Our results demonstrate that communication format and implementation details determine outcomes more than architectural complexity, and that simpler approaches match or outperform multi-agent pipelines for local 7B model deployment.

**证据没有证明什么。** 6.4 Limitations We have certain limitations in our evaluation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26922v1#S3 — 3 System and Methods; https://arxiv.org/html/2607.26922v1#S2.SS1 — 2.1 Multi-Agent LLM Systems。Evaluation：https://arxiv.org/html/2607.26922v1#S3.SS5 — 3.5 Experimental Setup; https://arxiv.org/html/2607.26922v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26922v1#S6 — 6 Discussion; https://arxiv.org/html/2607.26922v1#S6.SS4 — 6.4 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6.4 Limitations We have certain limitations in our evaluation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26922:end -->

<!-- review:SF-2026-ARXIV-2607-26924:start -->
### Temporally Centered SIGReg Improves LeWorldModel Representations for Robot Policy Learning

<!-- claim:SF-2026-ARXIV-2607-26924:start -->Recent work on LeWorldModel (LeWM) has shown that the Sketched Isotropic Gaussian Regularizer (SIGReg) enables stable end-to-end world model learning from pixels by regularizing the latent representation toward an isotropic Gaussian. While effective for latent-space planning, the representations learned by Raw LeWM are poorly suited for downstream robot policy learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26924:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent work on LeWorldModel (LeWM) has shown that the Sketched Isotropic Gaussian Regularizer (SIGReg) enables stable end-to-end world model learning from pixels by regularizing the latent representation toward an isotropic Gaussian.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** On the LIBERO benchmark, our method improves downstream policy success on the Goal suite by 1.66x and raises the average success rate across all suites from 63.6% to 83.8%.

**证据证明什么。** These results associate the variance-allocation bias of Raw LeWM with the downstream policy gap, and show that decoupling persistent and residual variation yields representations better suited for downstream robot policy learning.

**证据没有证明什么。** Future work will investigate scaling TC-LeWM to larger reward-free datasets and integrating it with Vision-Language Action Models or World-Action-Models for open-world manipulation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26924v1#A1.SS1 — A.1 Model and Implementation Details; https://arxiv.org/html/2607.26924v1#S4.SS1 — 4.1 Temporally Centered LeWorldModel。Evaluation：https://arxiv.org/html/2607.26924v1#S5.SS2 — 5.2 Main Results on the LIBERO Benchmark; https://arxiv.org/html/2607.26924v1#A1.SS2 — A.2 Monte Carlo Analysis Details。Limitations / counterevidence：https://arxiv.org/html/2607.26924v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will investigate scaling TC-LeWM to larger reward-free datasets and integrating it with Vision-Language Action Models or World-Action-Models for open-world manipulation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26924:end -->

<!-- review:SF-2026-ARXIV-2607-26928:start -->
### Latent-IM: Latent Interaction Management for Speech LLMs

<!-- claim:SF-2026-ARXIV-2607-26928:start -->Classical spoken dialogue systems often separated dialogue management from response realization: a policy selected the next dialogue action, and a generation component expressed that action. As dialogue systems shift toward LLMs, this decomposition has largely disappeared into the model's hidden representations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26928:end -->

**为什么进入候选分母。** 摘要首要问题为“Classical spoken dialogue systems often separated dialogue management from response realization: a policy selected the next dialogue action, and a generation component expressed that action.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Latent-IM, an internal dialogue-management framework that provides a general interface for choosing and deploying conversational moves under different objectives.

**证据证明什么。** Here, we use this control to reproduce human move choices, improving average end-to-end move accuracy by 12.5 points over the unsteered backbone while performing comparably to fine-tuning.

**证据没有证明什么。** Future work can replace imitation-based selection with goal-conditioned policies that choose moves according to predicted task utility. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26928v1#Sx4 — Method; https://arxiv.org/html/2607.26928v1#A1 — Appendix A Implementation Details and Prompts。Evaluation：https://arxiv.org/html/2607.26928v1#Sx5 — Results; https://arxiv.org/html/2607.26928v1#Sx7 — Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26928v1#Sx7.SSx3 — Future Work: Beyond Human-Move Imitation; https://arxiv.org/html/2607.26928v1#Sx8 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work can replace imitation-based selection with goal-conditioned policies that choose moves according to predicted task utility.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26928:end -->

<!-- review:SF-2026-ARXIV-2607-26935:start -->
### What Does It Take to Detect an AI Agent? Minimal Feature Sets for Behavioral Detection under Browser Automation

<!-- claim:SF-2026-ARXIV-2607-26935:start -->Bot detectors deployed at scale treat traffic as binary: human or bot. This assumption breaks when AI agents browse the web through browser automation, a traffic class that is neither and that binary classifiers structurally cannot represent. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26935:end -->

**为什么进入候选分母。** 摘要首要问题为“Bot detectors deployed at scale treat traffic as binary: human or bot.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present a three-class detection framework distinguishing humans, bots, and AI agents, and show that the binary-vs-agent confusion is architectural: a binary human-vs-bot detector misroutes agent sessions because its label space lacks an agent class.

**证据证明什么。** We present a three-class detection framework distinguishing humans, bots, and AI agents, and show that the binary-vs-agent confusion is architectural: a binary human-vs-bot detector misroutes agent sessions because its label space lacks an agent class.

**证据没有证明什么。** The attacker has white-box knowledge of the feature set (all 16 continuous + 7 binary features) but only black-box access to the detection model: they cannot inspect model weights or gradients. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26935v1#A3 — Appendix C SAINT Architecture and Training Details; https://arxiv.org/html/2607.26935v1#A4 — Appendix D Evasion Methodology。Evaluation：https://arxiv.org/html/2607.26935v1#S10 — 10. Multi-Seed Evaluation; https://arxiv.org/html/2607.26935v1#S11 — 11. Results Summary。Limitations / counterevidence：https://arxiv.org/html/2607.26935v1#S12 — 12. Discussion & Conclusion; https://arxiv.org/html/2607.26935v1#S5.SS1 — 5.1. Threat Model。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The attacker has white-box knowledge of the feature set (all 16 continuous + 7 binary features) but only black-box access to the detection model: they cannot inspect model weights or gradients.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26935:end -->

<!-- review:SF-2026-ARXIV-2607-26937:start -->
### VITAL-RAG: Invariance Race for Context Allocation in Coding Agents

<!-- claim:SF-2026-ARXIV-2607-26937:start -->Coding agents often retrieve code from an entire repository, but only limited evidence can fit into the final model input. Conventional retrieval-augmented generation (RAG) for coding agents treats fragments from the same code object as separate results, so redundant views can occupy multiple context positions and crowd out useful code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26937:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents often retrieve code from an entire repository, but only limited evidence can fit into the final model input.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address this race, we introduce VITAL-RAG, which organizes evidence by canonical code object, keeps one query-relevant companion only when it adds semantics not already represented, and renders selected evidence under per-object and global token budgets.

**证据证明什么。** Across three model backends, it matches or outperforms recent baselines on RepoClassBench and achieves the highest raw Pass@1 on RepoExec.

**证据没有证明什么。** Exact Dedup changes Recall@4K by only 0.02 points, showing that byte-identical repetition is not the main issue. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26937v1#S5.SS1 — 5.1 Method Overview。Evaluation：https://arxiv.org/html/2607.26937v1#S6 — 6 Experimental Evaluation; https://arxiv.org/html/2607.26937v1#S4 — 4 Analysis of Evidence Allocation。Limitations / counterevidence：https://arxiv.org/html/2607.26937v1#S4.SS2 — 4.2 Limitations of Existing Allocation Controls; https://arxiv.org/html/2607.26937v1#S7 — 7 Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact Dedup changes Recall@4K by only 0.02 points, showing that byte-identical repetition is not the main issue.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26937:end -->

<!-- review:SF-2026-ARXIV-2607-26953:start -->
### Assurance-Scoped Reliability for Agentic Networks: Capturing the State That Matters

<!-- claim:SF-2026-ARXIV-2607-26953:start -->Agentic networks transform accepted intents into operational services through autonomous reasoning, adaptive planning, tool use, and cross-domain coordination, but these capabilities introduce failure modes that conventional reliability measures do not fully capture. An accepted intent may still be carried out incorrectly, for example because the system acts on stale information, repeats an external action, applies only part of a change, or enters a fallback mode that quietly relaxes policy enforcement. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26953:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic networks transform accepted intents into operational services through autonomous reasoning, adaptive planning, tool use, and cross-domain coordination, but these capabilities introduce failure modes that conventional reliability measures do not fully capture.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** This article proposes Reliability Assurance Intelligence (RAI), a general assurance architecture for such systems.

**证据证明什么。** Using an agentic lifecycle manager for deterministic network services as a running example, we design the RAI architecture and propose a methodology for validating its reliability assurances.

**证据没有证明什么。** Uptime and telemetry remain necessary, but they show only that the system is running, not that its autonomous decisions were properly authorized, accountable for their effects, and backed by enough evidence to recover and audit them. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26953v1#S6.SS1 — VI-A Validation Methodology。Evaluation：https://arxiv.org/html/2607.26953v1#S1 — I Introduction; https://arxiv.org/html/2607.26953v1#S2 — II Running Example: An Agentic Lifecycle Manager。Limitations / counterevidence：https://arxiv.org/html/2607.26953v1#S7 — VII Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Uptime and telemetry remain necessary, but they show only that the system is running, not that its autonomous decisions were properly authorized, accountable for their effects, and backed by enough evidence to recover and audit them.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26953:end -->

<!-- review:SF-2026-ARXIV-2607-26988:start -->
### A Compositional Theory of Causally Masked Transformers

<!-- claim:SF-2026-ARXIV-2607-26988:start -->What types of decision problems can a causally masked, finite-precision transformer solve for inputs of arbitrary length? Existing answers often rely on idealized arithmetic, but under finite precision, rounding and evaluation order can change what information attention retains and therefore what the model can compute. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26988:end -->

**为什么进入候选分母。** 摘要首要问题为“What types of decision problems can a causally masked, finite-precision transformer solve for inputs of arbitrary length?”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Applying this method to transformers without positional embeddings, we obtain an expressivity hierarchy governed by the attention type under specific numerical semantics.

**证据证明什么。** Under an explicit free-wiring assumption, all four bounds are tight.

**证据没有证明什么。** While unbounded position information cannot be assessed using this algebraic framework, certain finite or repeating position embeddings could be incorporated in future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26988v1#A2 — Appendix B NoPE Transformer Architecture。Evaluation：https://arxiv.org/html/2607.26988v1#S5.SSx3 — The Importance of Evaluation Order。Limitations / counterevidence：https://arxiv.org/html/2607.26988v1#S7 — 7 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：While unbounded position information cannot be assessed using this algebraic framework, certain finite or repeating position embeddings could be incorporated in future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SELF-ATTENTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26988:end -->

<!-- review:SF-2026-ARXIV-2607-26991:start -->
### RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-26991:start -->Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks. Recent test-time steering and scaling methods improve performance without extensive data collection and retraining, but action samples often remain concentrated around similar behaviors and therefore inherit correlated failure modes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26991:end -->

**为什么进入候选分母。** 摘要首要问题为“Despite the impressive visuomotor capabilities enabled by Vision-Language-Action (VLA) models, their performance often degrades on challenging and out-of-domain tasks.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these limitations, we introduce $RL^2$, an adaptive inference-time steering framework that leverages Reinforcement Learning on VLA Latents.

**证据证明什么。** Across the SIMPLER and PolaRiS benchmarks, $RL^2$ improves success rates by up to +17.3% in out-of-domain settings, while ablations and scaling studies demonstrate the importance of latent representations and RL training.

**证据没有证明什么。** We acknowledge the following limitations of , and leave further improvements to future work: Steering Function: While we evaluated many lightweight steering functions (Sec. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26991v1#S5 — V Method。Evaluation：https://arxiv.org/html/2607.26991v1#S6 — VI Experiments; https://arxiv.org/html/2607.26991v1#S6.SS1 — VI-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26991v1#S5.SS3 — V-C Failure Detection for Adaptive Steering; https://arxiv.org/html/2607.26991v1#S7 — VII Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：We acknowledge the following limitations of , and leave further improvements to future work: Steering Function: While we evaluated many lightweight steering functions (Sec.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26991:end -->

<!-- review:SF-2026-ARXIV-2607-26998:start -->
### AgentSnare: Learning to Delay, Divert, and Defuse Autonomous Penetration Agents

<!-- claim:SF-2026-ARXIV-2607-26998:start -->Large language model (LLM) agents automate penetration testing through an observation-action loop, selecting actions based on observations returned by tools. This dependence allows defenders to inject deceptive observations that can mislead the agent's decision-making process. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26998:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents automate penetration testing through an observation-action loop, selecting actions based on observations returned by tools.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this issue, we introduce AgentSnare, a trajectory-adaptive deception system that dynamically unfolds a decoy environment to continually steer the penetration agent away from the real target.

**证据证明什么。** Across 15 CVE-Bench web applications and three attacker models, AgentSnare absorbs 46.8% of the agent's tool calls in the decoy and retains 55.9% of post-entry actions there, while 90.0% of completion attempts are grounded in decoy evidence; across all 45 attacker-CVE pairs, no real target is successfully exploited at pass@3.

**证据没有证明什么。** Threat Model We consider an autonomous penetration agent that plans attacks, invokes tools, and revises its strategy based on the returned observations under a finite budget of tool calls. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26998v1#Sx4.SSx1 — System Overview; https://arxiv.org/html/2607.26998v1#Sx3 — Threat Model。Evaluation：https://arxiv.org/html/2607.26998v1#Sx2.SSx1 — Autonomous Penetration Agents and Benchmarks; https://arxiv.org/html/2607.26998v1#Sx6 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26998v1#Sx3 — Threat Model; https://arxiv.org/html/2607.26998v1#Sx7 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Threat Model We consider an autonomous penetration agent that plans attacks, invokes tools, and revises its strategy based on the returned observations under a finite budget of tool calls.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26998:end -->

<!-- review:SF-2026-ARXIV-2607-27011:start -->
### Qwen-Audio-3.0-Gen-Preview Technical Report

<!-- claim:SF-2026-ARXIV-2607-27011:start -->Existing single-domain and multi-task audio systems remain limited in directly organizing heterogeneous audio components, ambience, and multiple roles into long-form temporal scenes. We present Qwen-Audio-3.0-Gen-Preview, a unified non-autoregressive framework that uses a Diffusion Transformer (DiT) and a shared variational autoencoder (VAE) to generate the complete mixed waveform. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27011:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing single-domain and multi-task audio systems remain limited in directly organizing heterogeneous audio components, ambience, and multiple roles into long-form temporal scenes.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present Qwen-Audio-3.0-Gen-Preview, a unified non-autoregressive framework that uses a Diffusion Transformer (DiT) and a shared variational autoencoder (VAE) to generate the complete mixed waveform.

**证据证明什么。** These results demonstrate the potential of unified generation for temporally structured audio without task-specific branches.

**证据没有证明什么。** Real annotations, synthetic recipes, and prompt-enhanced requests use compatible structured records rendered as textual conditions, while semantic views, role-bundle integrity, and classifier-free guidance expose complementary information without breaking source–dialogue relations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27011v1#S3 — 3 System Overview。Evaluation：https://arxiv.org/html/2607.27011v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.27011v1#S6.SS4 — 6.4 VAE Component Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.27011v1#S7 — 7 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Real annotations, synthetic recipes, and prompt-enhanced requests use compatible structured records rendered as textual conditions, while semantic views, role-bundle integrity, and classifier-free guidance expose complementary information without breaking source–dialogue relations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27011:end -->

<!-- review:SF-2026-ARXIV-2607-27017:start -->
### What Can Latent World Models Know? Physical Parameter Identifiability in Multimodal Predictive Representations

<!-- claim:SF-2026-ARXIV-2607-27017:start -->A central premise of latent world models is that predicting the future forces a representation to internalize the physics of its environment. Which physical quantities does a trained latent actually contain, and what decides this? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27017:end -->

**为什么进入候选分母。** 摘要首要问题为“A central premise of latent world models is that predicting the future forces a representation to internalize the physics of its environment.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Which physical quantities does a trained latent actually contain, and what decides this?

**证据证明什么。** Objective structure determines which physical parameters a latent acquires, and additional data improves only the parameters it already acquires.

**证据没有证明什么。** 7 Limitations Both tested objectives are deterministic point predictions on one trunk. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27017v1#S6 — 6 Design Rules。Evaluation：https://arxiv.org/html/2607.27017v1#A3 — Appendix C Full Results; https://arxiv.org/html/2607.27017v1#A3.SS5 — C.5 Real-robot results in full。Limitations / counterevidence：https://arxiv.org/html/2607.27017v1#S7 — 7 Limitations; https://arxiv.org/html/2607.27017v1#S8 — 8 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations Both tested objectives are deterministic point predictions on one trunk.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27017:end -->

<!-- review:SF-2026-ARXIV-2607-27023:start -->
### BayesAME: Bayesian Active Model Evaluation

<!-- claim:SF-2026-ARXIV-2607-27023:start -->Evaluating large generative models across benchmarks is time-consuming and computationally expensive. This drives the need for methods that can estimate full benchmark performance by evaluating models on only a subset of items, known as a coreset. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27023:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluating large generative models across benchmarks is time-consuming and computationally expensive.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce BayesAME, a sequential Bayesian framework specifically targeting automatic determination of the coreset size.

**证据证明什么。** Through extensive experiments across diverse benchmarks, we demonstrate that BayesAME consistently outperforms sequential adaptations of existing methods.

**证据没有证明什么。** There are several limitations of BayesAME that provide promising avenues for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27023v1#A3.SS1 — C.1 Implementations Details。Evaluation：https://arxiv.org/html/2607.27023v1#A3 — Appendix C Experimental Details and Additional Results; https://arxiv.org/html/2607.27023v1#A3.SS2 — C.2 Additional Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.27023v1#S6 — 6 Discussion and Conclusions。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：There are several limitations of BayesAME that provide promising avenues for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27023:end -->

<!-- review:SF-2026-ARXIV-2607-27030:start -->
### HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models

<!-- claim:SF-2026-ARXIV-2607-27030:start -->LLM-based analyzers have begun finding real vulnerabilities in mature open-source projects: AISLE's analyzer is credited with more than 280 CVEs across 78 projects, including OpenSSL, curl, and GnuTLS. We introduce HoF-Bench (named after AISLE's public Hall of Fame), a benchmark built from 95 of these public AI-discovered CVEs across eight repositories pinned at vulnerable commits. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27030:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based analyzers have begun finding real vulnerabilities in mature open-source projects: AISLE's analyzer is credited with more than 280 CVEs across 78 projects, including OpenSSL, curl, and GnuTLS.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce HoF-Bench (named after AISLE's public Hall of Fame), a benchmark built from 95 of these public AI-discovered CVEs across eight repositories pinned at vulnerable commits.

**证据证明什么。** The dataset is available at https://huggingface.co/datasets/aisleinc/HoF-Bench.

**证据没有证明什么。** The results therefore cover ten configurations of a single analyzer and should not be interpreted as a comparison of ten independent products. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27030v1#A3 — Appendix C Supplement: One-Dimensional Reliability Model; https://arxiv.org/html/2607.27030v1#S4.SS2 — 4.2 Inexpensive, Non-Frontier Detector Models。Evaluation：https://arxiv.org/html/2607.27030v1#A1 — Appendix A Supplement: Benchmark Format; https://arxiv.org/html/2607.27030v1#S4 — 4 Reference Scanner and Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.27030v1#S6 — 6 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The results therefore cover ten configurations of a single analyzer and should not be interpreted as a comparison of ten independent products.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27030:end -->

<!-- review:SF-2026-ARXIV-2607-27031:start -->
### Lottery Tickets Are Not Deployment Tickets

<!-- claim:SF-2026-ARXIV-2607-27031:start -->Reports on how sparsification, compression, and lottery tickets change model behavior have been mixed in the prior literature, with beneficial effects observed in some studies and adverse effects in others. Moreover, prior work has not considered actual deployment conditions, where decision logic is already fixed for the incumbent. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27031:end -->

**为什么进入候选分母。** 摘要首要问题为“Reports on how sparsification, compression, and lottery tickets change model behavior have been mixed in the prior literature, with beneficial effects observed in some studies and adverse effects in others.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Moreover, prior work has not considered actual deployment conditions, where decision logic is already fixed for the incumbent.

**证据证明什么。** Across extensive experiments, sparse candidates repeatedly recover dense-reference accuracy yet remain behaviorally different; in several study-band-matched settings, LTs also show lower corruption accuracy.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27031v1#Sx1 — Introduction; https://arxiv.org/html/2607.27031v1#Sx2 — Behavioral Compatibility Audit。Evaluation：https://arxiv.org/html/2607.27031v1#A1.SSx3 — Theoretical Results; https://arxiv.org/html/2607.27031v1#A1.SSx5 — Experimental Protocol and Reproducibility。Limitations / counterevidence：https://arxiv.org/html/2607.27031v1#A1.SSx11 — Limitations and Future Extensions; https://arxiv.org/html/2607.27031v1#A1.SSx9 — Additional Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27031:end -->

<!-- review:SF-2026-ARXIV-2607-27042:start -->
### GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding

<!-- claim:SF-2026-ARXIV-2607-27042:start -->Adaptive rounding methods such as GPTQ, or equivalently Babai's nearest plane algorithm, round a real matrix to integers under a quadratic metric. They process the entries in a fixed order, one at a time, propagating each rounding error to the entries not yet processed through a triangular feedback matrix. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27042:end -->

**为什么进入候选分母。** 摘要首要问题为“Adaptive rounding methods such as GPTQ, or equivalently Babai's nearest plane algorithm, round a real matrix to integers under a quadratic metric.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present GPTQ-2D, which produces the identical rounded matrix in cubic time.

**证据证明什么。** It rounds the entries anti-diagonal by anti-diagonal; entries on the same anti-diagonal are independent and are rounded in parallel.

**证据没有证明什么。** First, the equivalence guarantee assumes the basis matrices and , hence the feedback factors and , are fixed throughout the sweep; if they adapt to intermediate rounding decisions, for instance through data-dependent scaling, exact equivalence to the fixed vectorized procedure need not hold. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27042v1#A1 — Appendix A Nested Algorithm; https://arxiv.org/html/2607.27042v1#S4.SS2 — 4.2 GPTQ-2D Algorithm。Evaluation：https://arxiv.org/html/2607.27042v1#S4 — 4 Theoretical Results。Limitations / counterevidence：https://arxiv.org/html/2607.27042v1#S6 — 6 Applications and Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：First, the equivalence guarantee assumes the basis matrices and , hence the feedback factors and , are fixed throughout the sweep; if they adapt to intermediate rounding decisions, for instance through data-dependent scaling, exact equivalence to the fixed vectorized procedure need not hold.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27042:end -->

<!-- review:SF-2026-ARXIV-2607-27056:start -->
### Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data

<!-- claim:SF-2026-ARXIV-2607-27056:start -->Personalized agents are increasingly applied to assist users across a wide range of tasks. Effective personalized assistance requires not only retrieving explicit facts from past interactions stored in agent memory, but also inferring abstract personal characteristics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27056:end -->

**为什么进入候选分母。** 摘要首要问题为“Personalized agents are increasingly applied to assist users across a wide range of tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Finally, we leverage Setoka to evaluate 3 language models combined with 5 memory systems for 10 synthetic users.

**证据证明什么。** These findings demonstrate that user understanding cannot be handled by simple fact retrieval, motivating the design of memory mechanisms for cross-source integration and abstraction over long-term user behavior.

**证据没有证明什么。** This is because a system cannot answer a concrete factual question when the relevant evidence is missing, whereas it can always guess an abstract personality trait. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27056v1#S2.SS1 — 2.1 Memory Systems; https://arxiv.org/html/2607.27056v1#S3 — 3 User Understanding Modeling。Evaluation：https://arxiv.org/html/2607.27056v1#S2.SS2 — 2.2 Memory Benchmarks; https://arxiv.org/html/2607.27056v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27056v1#S5.SS2 — 5.2 Main Findings and Discussions; https://arxiv.org/html/2607.27056v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This is because a system cannot answer a concrete factual question when the relevant evidence is missing, whereas it can always guess an abstract personality trait.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27056:end -->

<!-- review:SF-2026-ARXIV-2607-27069:start -->
### Visual Credit Audit for Multimodal Spatial Reasoning

<!-- claim:SF-2026-ARXIV-2607-27069:start -->Closed yes/no spatial benchmarks can reward a correct answer even when the image adds little support beyond no-image contexts. Under a fixed forced-choice interface, Visual Credit Audit (VCA) separates two estimands: whether the benchmark image gives the model's declared decision more support than text-only and blank controls, and whether the model responds to relation-specific visual evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27069:end -->

**为什么进入候选分母。** 摘要首要问题为“Closed yes/no spatial benchmarks can reward a correct answer even when the image adds little support beyond no-image contexts.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Under a fixed forced-choice interface, Visual Credit Audit (VCA) separates two estimands: whether the benchmark image gives the model's declared decision more support than text-only and blank controls, and whether the model responds to relation-specific visual evidence.

**证据证明什么。** Matched same-split image permutation reduces D-CC by 21.25-47.80 points, with every paired 95% interval above zero.

**证据没有证明什么。** A gold-only gain necessarily collapses this second distinction because it cannot credit evidence for an incorrect declared decision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27069v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.27069v1#Sx16 — Held-Out Benchmark Filtering; https://arxiv.org/html/2607.27069v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27069v1#Sx5 — Discussion; https://arxiv.org/html/2607.27069v1#Sx6 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A gold-only gain necessarily collapses this second distinction because it cannot credit evidence for an incorrect declared decision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27069:end -->

<!-- review:SF-2026-ARXIV-2607-27080:start -->
### MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair

<!-- claim:SF-2026-ARXIV-2607-27080:start -->Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist. A malicious instruction crafted by an attacker may be stored in long-term memory, recalled much later, and quietly shape a real action. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27080:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory systems allow agents to retain and reuse information from past interactions, but they can also let malicious content persist.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this gap, we introduce MemSecBench, a task-grounded benchmark for the lifecycle security of agent memory systems.

**证据证明什么。** Among successfully poisoned cases, 59.6% complete the full Execute chain, while 56.1% achieve selective repair.Compared with matched Native configurations, the largest absolute differences are 16.1 percentage points for end-to-end attack success and 41.3 percentage points for selective repair.

**证据没有证明什么。** The judge model belongs to the evaluation protocol but is not part of . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27080v1#A1.SS3 — A.3 Taxonomy Design; https://arxiv.org/html/2607.27080v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.27080v1#A1 — Appendix A Benchmark Construction and Taxonomy; https://arxiv.org/html/2607.27080v1#Sx3.SSx2 — MemSecBench Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.27080v1#Sx3.SSx1 — Threat Model; https://arxiv.org/html/2607.27080v1#Sx5 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The judge model belongs to the evaluation protocol but is not part of .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27080:end -->

<!-- review:SF-2026-ARXIV-2607-27081:start -->
### On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust Realignment

<!-- claim:SF-2026-ARXIV-2607-27081:start -->Fine-tuning is the dominant paradigm for specializing large language models (LLMs), yet it exposes a critical vulnerability: malicious data providers can embed harmful behaviors into downstream corpora, creating models that retain professional skills while violating human values on demand. Existing safety-realignment defenses often fail in practice due to three key limitations: they frequently cause catastrophic forgetting of specialized skills; their effectiveness collapses when the defender cannot observe the attacker's prompt template; and successfully realigned models remain susceptible to re-jailbreaking via simple system prompt switches. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27081:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-tuning is the dominant paradigm for specializing large language models (LLMs), yet it exposes a critical vulnerability: malicious data providers can embed harmful behaviors into downstream corpora, creating models that retain professional skills while violating human values on demand.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address these challenges, we propose Routing-based On-Policy Distillation (ROPD), a novel realignment framework that models the divergence between aligned and compromised output probability distributions rather than fitting specific prompt templates.

**证据证明什么。** Our results demonstrate that when baseline defenses face template mismatches, often accompanied by severe degradation in downstream task performance.

**证据没有证明什么。** 3.1 Threat Model and Notation Let denote an original, safety-aligned LLM. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27081v1#S4.SS4 — 4.4 The Robustness Boundary: Switching the System Prompt; https://arxiv.org/html/2607.27081v1#S3.SS1 — 3.1 Threat Model and Notation。Evaluation：https://arxiv.org/html/2607.27081v1#S4 — 4 Experiments; https://arxiv.org/html/2607.27081v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27081v1#S3.SS1 — 3.1 Threat Model and Notation; https://arxiv.org/html/2607.27081v1#S5 — 5 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：3.1 Threat Model and Notation Let denote an original, safety-aligned LLM.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27081:end -->

<!-- review:SF-2026-ARXIV-2607-27083:start -->
### Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-27083:start -->As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure. Routers and retrievers can rank candidate tools by relevance, but a ranking alone does not determine how many are worth selecting. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27083:end -->

**为什么进入候选分母。** 摘要首要问题为“As LLM agents increasingly depend on diverse external services such as search engines, databases, and connectors, agent harnesses face a fundamental tool-selection challenge: acquiring too few tools leaves the task under-informed, while too many adds cost, context load, and privacy exposure.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** On $τ$-bench Retail, CAM-DF attains the highest payoff among deployable methods, with gains over a predict-then-threshold baseline across all five ranking sources and two cost regimes.

**证据证明什么。** The CAM-DF family is a lightweight pre-execution plugin that turns existing tool rankings into lower-cost acquisition decisions without fine-tuning the underlying LLM.

**证据没有证明什么。** While CAM-DF provides a cost-aware framework for one-turn pre-execution acquisition, the current formulation does not update acquisition decisions after observing tool outputs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27083v1#S5 — 5 Method: CAM-DF and CAM-DF-lite; https://arxiv.org/html/2607.27083v1#A3 — Appendix C Algorithmic and Prompt Details。Evaluation：https://arxiv.org/html/2607.27083v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.27083v1#A7.SS2 — G.2 Robustness, Ablations, and Tuning。Limitations / counterevidence：https://arxiv.org/html/2607.27083v1#S7 — 7 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：While CAM-DF provides a cost-aware framework for one-turn pre-execution acquisition, the current formulation does not update acquisition decisions after observing tool outputs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27083:end -->

<!-- review:SF-2026-ARXIV-2607-27090:start -->
### InferScale: GPU-Native KV Injection for Personalized LLM Serving

<!-- claim:SF-2026-ARXIV-2607-27090:start -->Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests. Production memory systems (e.g., Mem0, MemGPT, and Zep) retrieve a relevant subset of this memory and inject it into the prompt, forcing the serving engine to repeatedly prefill the same content. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27090:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly deployed with persistent personalized context, such as accumulated memory profiles or long conversation histories, that is shared across a user's many requests.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present InferScale, a GPU-native LLM memory system that replaces repeated prompt prefilling with reusable KV state.

**证据证明什么。** Across three open-weight models on LoCoMo, InferScale keeps TTFT nearly constant as the retrieval budget increases: at k=50 it reduces TTFT by 72-79% (3.6-4.8x), achieves 60.3% accuracy versus 63.3% for Mem0 without serving-time recomputation, and delivers 3.7-4.5x the throughput under concurrent load.

**证据没有证明什么。** Offloading the KV store to host DRAM further lifts the GPU-memory capacity bound at only a few-millisecond TTFT cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27090v1#S3 — 3. InferScale Design; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results。Evaluation：https://arxiv.org/html/2607.27090v1#A1 — Appendix A Full Serving-Latency Results; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results。Limitations / counterevidence：https://arxiv.org/html/2607.27090v1#S7 — 7. Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Offloading the KV store to host DRAM further lifts the GPU-memory capacity bound at only a few-millisecond TTFT cost.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-VLLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27090:end -->

<!-- review:SF-2026-ARXIV-2607-27110:start -->
### FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring

<!-- claim:SF-2026-ARXIV-2607-27110:start -->Autoregressive video diffusion models enable real-time streaming video generation. However, errors introduced during self-rollout accumulate over long horizons, manifesting as color drift, motion stagnation, and eventual visual collapse. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27110:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoregressive video diffusion models enable real-time streaming video generation.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Motivated by the above analysis, we propose FreqForcing, a training-free framework that addresses error accumulation in long-video generation via Spectral Self-Anchoring (SSA).

**证据证明什么。** Extensive experiments show that FreqForcing outperforms existing training-free methods quantitatively and qualitatively while remaining competitive with representative training-based approaches.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27110v1#Sx4 — Method。Evaluation：https://arxiv.org/html/2607.27110v1#Sx5 — Experiments; https://arxiv.org/html/2607.27110v1#Sx5.SSx1 — Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.27110v1#Sx6 — Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27110:end -->

<!-- review:SF-2026-ARXIV-2607-27143:start -->
### Cost-Sensitive Conformal Prediction and Human-in-the-Loop Abstention for Imbalanced High-Stakes Decision Support: A Multi-Domain Benchmark

<!-- claim:SF-2026-ARXIV-2607-27143:start -->High-stakes decision systems in credit scoring, fraud detection, healthcare, and industrial safety require reliable uncertainty quantification under severe class imbalance and asymmetric error costs. Standard marginal conformal prediction (CP) provides valid overall coverage guarantees; however, we show that it severely under-covers rare, costly minority classes, with minority-class coverage dropping to as low as 0.5% on certain datasets. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27143:end -->

**为什么进入候选分母。** 摘要首要问题为“High-stakes decision systems in credit scoring, fraud detection, healthcare, and industrial safety require reliable uncertainty quantification under severe class imbalance and asymmetric error costs.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** These findings provide practical guidance for deploying distribution-free, cost-aware uncertainty quantification in high-stakes decision support systems.

**证据证明什么。** Our results show that Mondrian CP restores valid minority-class coverage, achieving an average minority-coverage improvement of 61.7 percentage points over marginal CP (p &lt; 1e-80).

**证据没有证明什么。** 6.3 Threats to Validity & Limitations Five methodological threats to validity affect real-world deployment: 1. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27143v1#S3 — 3 Methodology & Theoretical Framework; https://arxiv.org/html/2607.27143v1#S6.SS1 — 6.1 System Architecture for Knowledge-Based Systems。Evaluation：https://arxiv.org/html/2607.27143v1#S5.SS4 — 5.4 Sensitivity & Ablation Analysis; https://arxiv.org/html/2607.27143v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.27143v1#S6.SS3 — 6.3 Threats to Validity & Limitations; https://arxiv.org/html/2607.27143v1#S7 — 7 Conclusion & Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6.3 Threats to Validity & Limitations Five methodological threats to validity affect real-world deployment: 1.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27143:end -->

<!-- review:SF-2026-ARXIV-2607-27146:start -->
### MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering via Source-Free Program Synthesis

<!-- claim:SF-2026-ARXIV-2607-27146:start -->Coding agents have made substantial progress on software engineering tasks that modify existing codebases, including bug fixing and feature implementation. However, constructing a complete program from scratch remains a major challenge: even the frontier models evaluated on ProgramBench fully resolve fewer than 1% of tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27146:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents have made substantial progress on software engineering tasks that modify existing codebases, including bug fixing and feature implementation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this gap, we introduce MindForge, an automated pipeline that converts open-source command-line programs into source-free environments that expose only a compiled reference executable and its documentation.

**证据证明什么。** Moreover, the fine-tuned model consistently improves over the base model across all seven unseen software engineering benchmarks, spanning long-horizon repository generation and translation, bug fixing, feature implementation, and cross-language issue resolution, with absolute gains of 31.00 points on RepoZero-C2Rust, 14.16 on DeepSWE, 10.70/4.56 on NL2Repo-Bench (with/without tests), 5.04 on SWE-bench Verified, 5.93 on SWE-bench Pro, 5.22 on SWE-bench Multilingual, and 4.94 on FeatBench.

**证据没有证明什么。** In each excerpt below the agent has already implemented a candidate program, has just observed its output diverge from the reference executable, and has correctly identified the cause; the two differ only in what they do next. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27146v1#S3.SS1 — 3.1 Base Model。Evaluation：https://arxiv.org/html/2607.27146v1#S3.SS3 — 3.3 Evaluation Benchmarks and Metrics; https://arxiv.org/html/2607.27146v1#A3 — Appendix C Evaluation Details。Limitations / counterevidence：https://arxiv.org/html/2607.27146v1#A5.SS1 — E.1 Examples of editing after failure recovery; https://arxiv.org/html/2607.27146v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In each excerpt below the agent has already implemented a candidate program, has just observed its output diverge from the reference executable, and has correctly identified the cause; the two differ only in what they do next.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27146:end -->

<!-- review:SF-2026-ARXIV-2607-27155:start -->
### OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding

<!-- claim:SF-2026-ARXIV-2607-27155:start -->Large language model (LLM) agents are increasingly expected to assist users in completing tasks. However, existing benchmarks provide limited support for evaluating whether agents can carry out office-suite workflows at a reasonable cost. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27155:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are increasingly expected to assist users in completing tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce OmegaUse-OfficeVal, a benchmark for evaluating LLM agents on long-horizon office-suite tasks with task-level economic grounding.

**证据证明什么。** The code and dataset are fully open-sourced, and more information is available on our project website: https://omegause-officeval.github.io.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27155v1#A3 — Appendix C Incentive Mechanism and Computation Method for Human Labor Time。Evaluation：https://arxiv.org/html/2607.27155v1#A1.SS1 — A.1 Productivity-Agent Benchmarks; https://arxiv.org/html/2607.27155v1#A1.SS2 — A.2 Office-Automation and Office-Suite Benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.27155v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27155:end -->

<!-- review:SF-2026-ARXIV-2607-27167:start -->
### SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based Program Synthesis from Scratch

<!-- claim:SF-2026-ARXIV-2607-27167:start -->LLM-based agents excel at software engineering tasks where an existing codebase provides context, but constructing a program from scratch remains fundamentally harder. Recent benchmarks such as ProgramBench quantify this gap: given only natural-language documentation and an execute-only binary as a behavioral oracle, even frontier models solve fewer than 1% of instances. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27167:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based agents excel at software engineering tasks where an existing codebase provides context, but constructing a program from scratch remains fundamentally harder.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present SpecFirst, a two-stage framework that forces the specification elicitation before code synthesis.

**证据证明什么。** Our results demonstrate that an explicit requirements-engineering phase is an effective paradigm for from-scratch program construction.

**证据没有证明什么。** For gomplate , this is particularly damaging: the agent must understand not only the top-level CLI interface but also the semantics of functions across ten namespaces, each with its own argument conventions and edge-case behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27167v1#S3 — III Approach of SpecFirst; https://arxiv.org/html/2607.27167v1#S3.SS5 — III-E Principles of Agent Design。Evaluation：https://arxiv.org/html/2607.27167v1#S4 — IV Experimental Design; https://arxiv.org/html/2607.27167v1#S4.SS2 — IV-B Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.27167v1#S2.SS2 — II-B Limitations of Existing Code Synthesis Agent; https://arxiv.org/html/2607.27167v1#S7 — VII Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：For gomplate , this is particularly damaging: the agent must understand not only the top-level CLI interface but also the semantics of functions across ten namespaces, each with its own argument conventions and edge-case behavior.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27167:end -->

<!-- review:SF-2026-ARXIV-2607-27178:start -->
### DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search

<!-- claim:SF-2026-ARXIV-2607-27178:start -->State-of-the-art retrieval models increasingly rely on closed training data, creating a reproducibility gap. We present an open end-to-end recipe for training retrieval models and study how English supervision transfers to multilingual retrieval through translate-train. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27178:end -->

**为什么进入候选分母。** 摘要首要问题为“State-of-the-art retrieval models increasingly rely on closed training data, creating a reproducibility gap.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present an open end-to-end recipe for training retrieval models and study how English supervision transfers to multilingual retrieval through translate-train.

**证据证明什么。** They achieve 56.20 and 57.22 average nDCG@10 on BEIR, respectively, setting new state-of-the-art results for this size class.

**证据没有证明什么。** Also, our retrieval training covers only English and eight translated languages. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27178v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.27178v1#A2 — Appendix B Detailed Results; https://arxiv.org/html/2607.27178v1#A2.SS2 — B.2 Extended Decontaminated BEIR Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27178v1#S4 — 4 Conclusion; https://arxiv.org/html/2607.27178v1#Sx1 — Limitations。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Also, our retrieval training covers only English and eight translated languages.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27178:end -->

<!-- review:SF-2026-ARXIV-2607-27180:start -->
### HumanCLAW: Can Vision-Language Models Act Through a Body?

<!-- claim:SF-2026-ARXIV-2607-27180:start -->Evaluating whether a vision-language model (VLM) can act through a physical body is challenging. The outcome of an action couples the VLM's decision with motor control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27180:end -->

**为什么进入候选分母。** 摘要首要问题为“Evaluating whether a vision-language model (VLM) can act through a physical body is challenging.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this work, we introduce HumanCLAW, an evaluation framework that decouples action decision-making from low-level execution.

**证据证明什么。** What current VLMs lack is embodied self-awareness: they lose track of their own body, failing to tell where it is, whether it has reached the goal, or whether it has hit an obstacle.

**证据没有证明什么。** We offer it as a clean testbed for the next generation of agents—agents that not only see and plan, but act. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27180v1#S3.SS1 — 3.1 Task Design and 3D Scene Setup。Evaluation：https://arxiv.org/html/2607.27180v1#S4 — 4 Experimental Result; https://arxiv.org/html/2607.27180v1#S3.SS2 — 3.2 Evaluation Metrics.。Limitations / counterevidence：https://arxiv.org/html/2607.27180v1#S6 — 6 Discussion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We offer it as a clean testbed for the next generation of agents—agents that not only see and plan, but act.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27180:end -->

<!-- review:SF-2026-ARXIV-2607-27187:start -->
### A Photonic-CXL Memory Appliance for Scalable KV Cache Management in LLM Inference

<!-- claim:SF-2026-ARXIV-2607-27187:start -->The KV cache demands tens of terabytes at hundreds of gigabytes per second, yet no current memory tier delivers both at once. Characterization across multi-generation GPU systems with various LLaMA models shows host memory retrieval achieves up to 100x speedup over re-computation but supports only tens of concurrent long-context users. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27187:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM inference at scale faces a memory wall.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** The proposal treats KV capacity and bandwidth as one disaggregated-memory contract: sixteen CXL 3.1 Type-3 photonic memory modules expose a switch-free optical full crossbar, pooled DDR5 capacity, and HBM3E caching to multiple hosts. Host processes map the shared DAX region, GPU DMA moves KV payloads, and offset-addressed metadata coordinates allocation and reuse without assuming identical virtual addresses across hosts.

**证据证明什么。** The paper directly characterizes host-memory and disk KV retrieval across the disclosed A100/H100/H200 systems, LLaMA-family sizes, contexts and batch sizes, then combines separately measured/emulated CXL parameters with an LLMServingSim model for an 8xH200 LLaMA-405B multi-turn workload. Within that model, the 32 TB tier avoids the simulated eviction cliff and produces the reported TTFT and capacity gains; these are architecture projections grounded in emulation, not measurements from the proposed physical appliance.

**证据没有证明什么。** The manuscript explicitly says end-to-end validation on physical PF Memory Appliance hardware remains pending, and its serving projection inherits the simulator profile, latency, bandwidth, workload, model, cache policy, and power assumptions. It does not establish production tail latency, failure recovery, coherence behavior, fairness, cost, thermal limits, or compatibility across arbitrary inference runtimes. The 50% electrical-CXL latency comparison and 6.6x TTFT result must therefore remain separate emulation/simulation claims.

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.27187v1#page=5 — PDF page 5, Photonic Fabric Memory Appliance architecture; https://arxiv.org/pdf/2607.27187v1#page=8 — PDF page 8, DAX mapping and multi-host shared-memory data path。Evaluation：https://arxiv.org/pdf/2607.27187v1#page=3 — PDF page 3, repeated-request characterization matrix; https://arxiv.org/pdf/2607.27187v1#page=6 — PDF page 6, emulation methodology; https://arxiv.org/pdf/2607.27187v1#page=9 — PDF page 9, LLMServingSim workload and results。Limitations / counterevidence：https://arxiv.org/pdf/2607.27187v1#page=10 — PDF page 10, VIII Limitations and Future Work。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** Pooling tens of terabytes can retain prefixes that tiered per-node caches evict, but it adds specialized optical/CXL hardware, shared allocator and consistency state, NUMA-like placement choices, and a new failure/ownership domain. Compression, quantization, prefetch and local KV caching remain orthogonal and preferable for smaller working sets; the photonic branch becomes relevant only when capacity and cross-host reuse dominate enough to justify the fabric and its operational complexity.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27187:end -->

<!-- review:SF-2026-ARXIV-2607-27191:start -->
### Can AI agents conduct open-ended AI research? Early evidence from two case studies

<!-- claim:SF-2026-ARXIV-2607-27191:start -->Forecasts of explosive AI progress hinge on AI agents automating AI research. But evidence on whether agents can carry out open-ended AI research is thin. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27191:end -->

**为什么进入候选分母。** 摘要首要问题为“Forecasts of explosive AI progress hinge on AI agents automating AI research.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a third way to measure progress towards AI R\&amp;D automation.

**证据证明什么。** Our results provide early evidence that today's agents can do the engineering of AI research, but struggle with critical parts of the research lifecycle.

**证据没有证明什么。** They were unable to effectively use resources given to them, such as VMs and API limits, and they could not keep track of the deadline. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27191v1#S2 — 2 Shadow evaluations: A new method for measuring progress towards AI R&D automation; https://arxiv.org/html/2607.27191v1#S4.SS3 — 4.3 The agents committed to unpromising approaches too quickly。Evaluation：https://arxiv.org/html/2607.27191v1#S11 — 11 Pre-experiment expectations survey; https://arxiv.org/html/2607.27191v1#S12 — 12 Comprehensive survey of prior autonomous-AI R&D experiments。Limitations / counterevidence：https://arxiv.org/html/2607.27191v1#S5 — 5 Log analysis reveals five failure modes; https://arxiv.org/html/2607.27191v1#S6 — 6 A robustness experiment with Codex and GPT-5.6 Sol Ultra reproduced these failure modes。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：They were unable to effectively use resources given to them, such as VMs and API limits, and they could not keep track of the deadline.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27191:end -->

<!-- review:SF-2026-ARXIV-2607-27201:start -->
### Mental World Modeling

<!-- claim:SF-2026-ARXIV-2607-27201:start -->World models enable a predictive substrate for planning and action, yet existing formulations merely answer a physical question: what/where it is, and how will it evolve. Human behavior, however, is driven by hidden mental state (what a person believes, wants, intends, feels, and considers socially permissible), so a model that tracks the physical scene but not what each agent knows and believes about it predicts the wrong action for the right-looking scene. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27201:end -->

**为什么进入候选分母。** 摘要首要问题为“World models enable a predictive substrate for planning and action, yet existing formulations merely answer a physical question: what/where it is, and how will it evolve.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We instantiate the framework in MENTIS, a training-free and fully inspectable baseline that decomposes the process into state parsing, target-observation generation, action decomposition, coupled physical and mental transition, and branch-level value evaluation.

**证据证明什么。** On a manually constructed, quality-controlled dataset of situated decision scenarios spanning text, image, and sounding-video stories, experiments with 8 modern LLM-based world models demonstrate that explicitly modeling the mental state is essential for predicting human decisions.

**证据没有证明什么。** B.3 Limitations of the Baseline Mentis should be read as a baseline implementation, not as the final architecture of Mental World Modeling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27201v1#S3 — 3 Theoretical Framework; https://arxiv.org/html/2607.27201v1#S5.SS1 — 5.1 Mentis Design Principle。Evaluation：https://arxiv.org/html/2607.27201v1#A2.SS1 — B.1 Inspectability, Ablations, and Experimental Use; https://arxiv.org/html/2607.27201v1#S7 — 7 Experiments and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.27201v1#A13 — Appendix M Future Directions; https://arxiv.org/html/2607.27201v1#A2.SS3 — B.3 Limitations of the Baseline。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：B.3 Limitations of the Baseline Mentis should be read as a baseline implementation, not as the final architecture of Mental World Modeling.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27201:end -->

<!-- review:SF-2026-ARXIV-2607-27205:start -->
### TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with &lt;1 GB VRAM

<!-- claim:SF-2026-ARXIV-2607-27205:start -->Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-27205:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) models commonly adopt an LLM-centric $V \to L \to A$ pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** TurboVLA removes the generative LLM from the execution-frequency control path. A vision encoder and lightweight text encoder retain modality-specific features, bidirectional cross-attention performs task-conditioned fusion, robot state enters only at an ACT-style decoder, and parallel action queries emit a continuous action chunk in one forward pass. The claimed $V + L \to A$ path therefore narrows the execution model's responsibility instead of claiming that language reasoning is unnecessary everywhere.

**证据证明什么。** Under the disclosed LIBERO protocol (2,000 rollouts), RoboTwin clean-setting protocol, and real-platform task trials, the compact execution path remains competitive while reducing the measured deployment footprint. The headline 97.7% LIBERO average, 31.2 ms latency, and 0.9 GB inference VRAM are bound to the stated 0.2B configuration, single RTX 4090 and batch size one; ablations additionally show that language, bidirectional interaction depth, and semantic instruction encoding each contribute within that setup.

**证据没有证明什么。** The results do not show that a compact execution policy can replace an LLM for open-ended planning, unseen embodiment transfer, long-horizon semantic decomposition, or safety assurance. RoboTwin training excludes randomized-scene data, and the author comparison does not make every baseline's pretraining data, optimization budget, and deployment stack identical. The evidence therefore supports an execution-layer branch, not universal VLA superiority.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.27205v1#S4 — 4 TurboVLA; https://arxiv.org/html/2607.27205v1#S4.SS2 — 4.2 Vision-Language Interaction Module; https://arxiv.org/html/2607.27205v1#S4.SS3 — 4.3 Continuous Action Chunk Prediction。Evaluation：https://arxiv.org/html/2607.27205v1#S5 — 5 Experiments; https://arxiv.org/html/2607.27205v1#S5.SS2 — 5.2 Benchmarks and Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.27205v1#S6 — 6 Conclusion。

**Artifact boundary。** Not Disclosed — exact v1 manuscript is the sole claim authority; no event-time commit or release artifact was independently pinned or used to enlarge the claim boundary.

**Trade-off 与共存边界。** Removing the LLM from every control tick reduces activation memory and latency, but deliberately gives up broad generative reasoning inside that loop and relies on compact encoders, grounding initialization, behavior-cloning data, fixed action chunks, and an external planner when instructions exceed execution-level semantics. LLM-centric VLA remains reasonable when high-level reasoning and open-vocabulary interpretation dominate; a hierarchical planner plus lightweight real-time controller is the coexistence boundary exposed by the paper itself.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-27205:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-26076 | score_7_9 | selected | DA-20260730-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260730-01 |
| SF-2026-ARXIV-2607-26099 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26099 |
| SF-2026-ARXIV-2607-26115 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26115 |
| SF-2026-ARXIV-2607-26121 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26121 |
| SF-2026-ARXIV-2607-26159 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26159 |
| SF-2026-ARXIV-2607-26192 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26192 |
| SF-2026-ARXIV-2607-26200 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26200 |
| SF-2026-ARXIV-2607-26253 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26253 |
| SF-2026-ARXIV-2607-26313 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26313 |
| SF-2026-ARXIV-2607-26335 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26335 |
| SF-2026-ARXIV-2607-26340 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26340 |
| SF-2026-ARXIV-2607-26348 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26348 |
| SF-2026-ARXIV-2607-26417 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26417 |
| SF-2026-ARXIV-2607-26444 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26444 |
| SF-2026-ARXIV-2607-26448 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26448 |
| SF-2026-ARXIV-2607-26452 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26452 |
| SF-2026-ARXIV-2607-26464 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26464 |
| SF-2026-ARXIV-2607-26475 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26475 |
| SF-2026-ARXIV-2607-26491 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26491 |
| SF-2026-ARXIV-2607-26515 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26515 |
| SF-2026-ARXIV-2607-26520 | score_7_9 | selected | DA-20260730-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260730-02 |
| SF-2026-ARXIV-2607-26566 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26566 |
| SF-2026-ARXIV-2607-26582 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26582 |
| SF-2026-ARXIV-2607-26587 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26587 |
| SF-2026-ARXIV-2607-26604 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26604 |
| SF-2026-ARXIV-2607-26618 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26618 |
| SF-2026-ARXIV-2607-26627 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26627 |
| SF-2026-ARXIV-2607-26633 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26633 |
| SF-2026-ARXIV-2607-26637 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26637 |
| SF-2026-ARXIV-2607-26643 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26643 |
| SF-2026-ARXIV-2607-26648 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26648 |
| SF-2026-ARXIV-2607-26652 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26652 |
| SF-2026-ARXIV-2607-26657 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26657 |
| SF-2026-ARXIV-2607-26694 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26694 |
| SF-2026-ARXIV-2607-26710 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26710 |
| SF-2026-ARXIV-2607-26712 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26712 |
| SF-2026-ARXIV-2607-26719 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26719 |
| SF-2026-ARXIV-2607-26754 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26754 |
| SF-2026-ARXIV-2607-26760 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26760 |
| SF-2026-ARXIV-2607-26773 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26773 |
| SF-2026-ARXIV-2607-26789 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26789 |
| SF-2026-ARXIV-2607-26818 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26818 |
| SF-2026-ARXIV-2607-26820 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26820 |
| SF-2026-ARXIV-2607-26828 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26828 |
| SF-2026-ARXIV-2607-26836 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26836 |
| SF-2026-ARXIV-2607-26843 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26843 |
| SF-2026-ARXIV-2607-26849 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26849 |
| SF-2026-ARXIV-2607-26862 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26862 |
| SF-2026-ARXIV-2607-26865 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26865 |
| SF-2026-ARXIV-2607-26903 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26903 |
| SF-2026-ARXIV-2607-26953 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26953 |
| SF-2026-ARXIV-2607-27017 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27017 |
| SF-2026-ARXIV-2607-27031 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27031 |
| SF-2026-ARXIV-2607-27080 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27080 |
| SF-2026-ARXIV-2607-27081 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27081 |
| SF-2026-ARXIV-2607-27083 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27083 |
| SF-2026-ARXIV-2607-27090 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27090 |
| SF-2026-ARXIV-2607-27180 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27180 |
| SF-2026-ARXIV-2607-27187 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27187 |
| SF-2026-ARXIV-2607-27191 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27191 |
| SF-2026-ARXIV-2607-27201 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-27201 |
| SF-2026-ARXIV-2607-27205 | score_7_9 | selected | DA-20260730-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260730-03 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-26099:start -->
`SF-2026-ARXIV-2607-26099` 的 exact-v1 Deep Review 已保留。其机制为：We formulate this problem as backdoor generalization under training--inference trigger shift and introduce Lilith, a black-box anchor-to-family framework. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26099:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26115:start -->
`SF-2026-ARXIV-2607-26115` 的 exact-v1 Deep Review 已保留。其机制为：The goal of this model is to evaluate and improve the robustness of our production systems. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26115:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26121:start -->
`SF-2026-ARXIV-2607-26121` 的 exact-v1 Deep Review 已保留。其机制为：The system layer realizes authorized actions dependably through integrated sensing, computation, control, hardware safeguards, fault containment, and fallback. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26121:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26159:start -->
`SF-2026-ARXIV-2607-26159` 的 exact-v1 Deep Review 已保留。其机制为：The target of one study may not be the source of the next; system, population, outcome, or conditions may change at the interface; and shared data or model lineage may make apparently independent support dependent. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26159:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26192:start -->
`SF-2026-ARXIV-2607-26192` 的 exact-v1 Deep Review 已保留。其机制为：This interpretation conflates three properties: coefficient variation, dependence of a frozen model on how coefficients are assigned to inputs, and conditional execution. 为避免挤压 `MODEL-TRANSFORMER-LAYER` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26192:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26200:start -->
`SF-2026-ARXIV-2607-26200` 的 exact-v1 Deep Review 已保留。其机制为：We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26200:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26253:start -->
`SF-2026-ARXIV-2607-26253` 的 exact-v1 Deep Review 已保留。其机制为：Existing remedies either oversample a larger candidate pool and discard saturated prompts (dynamic sampling), paying heavy extra rollouts, or predict prompt difficulty before sampling, which is fragile under a shifting policy. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26253:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26313:start -->
`SF-2026-ARXIV-2607-26313` 的 exact-v1 Deep Review 已保留。其机制为：Agentic systems act, so a defect in the evidence they retrieve becomes a wrong action with a currency cost. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26313:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26335:start -->
`SF-2026-ARXIV-2607-26335` 的 exact-v1 Deep Review 已保留。其机制为：We present fabric_ext, an eBPF middleware compiler and runtime for extensible OS policies over GPU--CXL fabrics. fabric_ext lets one policy program execute across GPU hooks, driver/runtime hooks, DPU/NIC hooks, and CXL switch or near-memory hooks. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26335:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26340:start -->
`SF-2026-ARXIV-2607-26340` 的 exact-v1 Deep Review 已保留。其机制为：We propose an alternative proactive fair scheduling framework tailored for MoE workloads, which effectively prevents fabric oversubscription. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26340:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26348:start -->
`SF-2026-ARXIV-2607-26348` 的 exact-v1 Deep Review 已保留。其机制为：We ask when this substitution is valid and when it fails, and package the answer as an evaluation framework for intelligent synthetic-user systems. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26348:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26417:start -->
`SF-2026-ARXIV-2607-26417` 的 exact-v1 Deep Review 已保留。其机制为：We introduce SCOUT, an online, learner-agnostic reset controller that gives every context its own curriculum. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26417:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26444:start -->
`SF-2026-ARXIV-2607-26444` 的 exact-v1 Deep Review 已保留。其机制为：Existing communication libraries remain largely buffer-centric because user and communication buffers are managed separately, causing redundant data copies or costly user-buffer registration. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26444:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26448:start -->
`SF-2026-ARXIV-2607-26448` 的 exact-v1 Deep Review 已保留。其机制为：On a fixed 1,200-task Oolong-Synth subset, our method reached 91.1% on Qwen and 99.3% on Gemma. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26448:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26452:start -->
`SF-2026-ARXIV-2607-26452` 的 exact-v1 Deep Review 已保留。其机制为：We introduce CG-World, a large-scale world-state dataset and protocol derived from industrial computer graphics production pipelines. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26452:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26464:start -->
`SF-2026-ARXIV-2607-26464` 的 exact-v1 Deep Review 已保留。其机制为：It is a practical execution and data environment for agentic SDLs; the broader physical AI implication is that PUDA provides an AI-native hardware harness for AI systems to interact with physical tools. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26464:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26475:start -->
`SF-2026-ARXIV-2607-26475` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we present DualDecoder, a lightweight serving system for long-context LLM inference that enables efficient sparse KV cache retrieval from host memory. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26491:start -->
`SF-2026-ARXIV-2607-26491` 的 exact-v1 Deep Review 已保留。其机制为：These results highlight the promise of ultra-large on-chip memories for energy-efficient LLM serving systems. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26491:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26515:start -->
`SF-2026-ARXIV-2607-26515` 的 exact-v1 Deep Review 已保留。其机制为：We present, to our knowledge, the first end-to-end FP4 RL post-training, in which both the rollout and training policies, including their forward and backward passes, operate at 4-bit precision. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26515:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26566:start -->
`SF-2026-ARXIV-2607-26566` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we present ServerlessT2I, a serverless-native system that decomposes a T2I workflow into loosely coupled model functions that can be independently managed and scheduled. 为避免挤压 `PLATFORM-PRODUCTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26582:start -->
`SF-2026-ARXIV-2607-26582` 的 exact-v1 Deep Review 已保留。其机制为：Corpus-free detectors rely on different combinations of absolute match level and relative or spatial sharpness, while WordNet-based methods additionally depend on external semantic coverage. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26582:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26587:start -->
`SF-2026-ARXIV-2607-26587` 的 exact-v1 Deep Review 已保留。其机制为：Automated research systems use experimental scores both to deliver artifacts and to decide which ideas to retain, transfer, and pursue. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26587:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26604:start -->
`SF-2026-ARXIV-2607-26604` 的 exact-v1 Deep Review 已保留。其机制为：We present WikiLoop, a feedback-coupled framework that jointly learns to build and navigate an agent-native Wiki, a persistent linked-page knowledge base designed for machine navigation. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26618:start -->
`SF-2026-ARXIV-2607-26618` 的 exact-v1 Deep Review 已保留。其机制为：We propose FedWeave, a framework that adopts asymmetric aggregation, separating expert aggregation from router optimization to meet these two requirements. 为避免挤压 `TRAIN-LORA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26618:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26627:start -->
`SF-2026-ARXIV-2607-26627` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we present a principled analysis of the distributions induced by lossy verification methods. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26627:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26633:start -->
`SF-2026-ARXIV-2607-26633` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we present NELSSA, an LLM serving system that integrates GPUs with real-world Processing-near-Memory (PNM) accelerator devices to efficiently support mixed-length workloads. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26633:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26637:start -->
`SF-2026-ARXIV-2607-26637` 的 exact-v1 Deep Review 已保留。其机制为：We present the first systematic exploration of filesystem-based memory for LLM agents. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26637:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26643:start -->
`SF-2026-ARXIV-2607-26643` 的 exact-v1 Deep Review 已保留。其机制为：We propose SkillBoost, a three-stage framework that mitigates both risks: structured exploitation localizes observed failures to editable skill components, prior-guided exploration draws on prior knowledge in the LLM to generate diverse repair candidates, and verified acceptance commits a candidate only when it improves performance within a regression bound. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26643:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26648:start -->
`SF-2026-ARXIV-2607-26648` 的 exact-v1 Deep Review 已保留。其机制为：We argue the energy dividend of sparsity is not a property of SNNs but of the task. 为避免挤压 `MODEL-SELF-ATTENTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26648:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26652:start -->
`SF-2026-ARXIV-2607-26652` 的 exact-v1 Deep Review 已保留。其机制为：AIGen works on top of the MLflow MLOps framework and combines mining heuristics with Large Language Models to generate AIBoMs. 为避免挤压 `PLATFORM-MODEL-REGISTRY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26652:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26657:start -->
`SF-2026-ARXIV-2607-26657` 的 exact-v1 Deep Review 已保留。其机制为：We present Enfold, which transfers this computation into a representation predicted from the current visual context and language instruction. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26657:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26694:start -->
`SF-2026-ARXIV-2607-26694` 的 exact-v1 Deep Review 已保留。其机制为：We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26694:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26710:start -->
`SF-2026-ARXIV-2607-26710` 的 exact-v1 Deep Review 已保留。其机制为：We present PowerAtlas, an LLM-agent framework for electricity-computing co-scheduling that integrates historical instances, domain knowledge, and physical constraints to produce joint decisions satisfying both grid operational rules and the service-level agreements (SLAs) of computing tasks. 为避免挤压 `PLATFORM-GPU-SCHEDULER` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26710:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26712:start -->
`SF-2026-ARXIV-2607-26712` 的 exact-v1 Deep Review 已保留。其机制为：To address this issue, we propose ActSWM, an action-sensitive latent world model grounded in a transition-separation principle: a planning-useful latent dynamics model should keep alternative-action futures distinguishable and make the action associated with each local transition recoverable. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26719:start -->
`SF-2026-ARXIV-2607-26719` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we present Lily, an automated approach that strengthens open-source development and release processes against backdoor injection. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26719:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26754:start -->
`SF-2026-ARXIV-2607-26754` 的 exact-v1 Deep Review 已保留。其机制为：Furthermore, compared with models without explicit state modeling, our method improves mechanics fidelity in generated game rollouts by 18.6%. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26760:start -->
`SF-2026-ARXIV-2607-26760` 的 exact-v1 Deep Review 已保留。其机制为：Based on this formulation, we propose Metis, the first prototype of memory foundation models. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26760:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26773:start -->
`SF-2026-ARXIV-2607-26773` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a causal audit that applies controlled message replacements at the boundary where the sender-produced representation enters the receiver. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26773:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26789:start -->
`SF-2026-ARXIV-2607-26789` 的 exact-v1 Deep Review 已保留。其机制为：We propose CheckVLA, which verifies execution with a separately trained, frozen action-conditioned world model. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26789:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26818:start -->
`SF-2026-ARXIV-2607-26818` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we propose \textbf{Ripple}, a real-time joint audio-video generation system with a cross-modal recurrent memory mechanism. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26818:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26820:start -->
`SF-2026-ARXIV-2607-26820` 的 exact-v1 Deep Review 已保留。其机制为：To address this limitation, we propose Recast, a safety risk forecasting framework that advances LLM safeguarding beyond turn-level violation detection to trajectory-level risk prediction. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26820:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26828:start -->
`SF-2026-ARXIV-2607-26828` 的 exact-v1 Deep Review 已保留。其机制为：We introduce \textbf{CostAda}, a cost-calibrated adaptive controller built around \emph{cost-calibrated frontier utility}. 为避免挤压 `AGENT-PLANNING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26828:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26836:start -->
`SF-2026-ARXIV-2607-26836` 的 exact-v1 Deep Review 已保留。其机制为：By facilitating early intervention through upstream screening, HalluProp effectively complements post-hoc methods, highlighting the potential of pre-hoc risk inference for building more reliable multi-agent systems. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26836:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26843:start -->
`SF-2026-ARXIV-2607-26843` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a metamorphic testing framework that evaluates the consistency of RAG systems under corpus evolution. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26843:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26849:start -->
`SF-2026-ARXIV-2607-26849` 的 exact-v1 Deep Review 已保留。其机制为：Finally, no method reliably surfaces every backdoor, but a broadly jailbreakable model is itself anomalous, a useful signal even when the exact trigger is not recovered. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26849:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26862:start -->
`SF-2026-ARXIV-2607-26862` 的 exact-v1 Deep Review 已保留。其机制为：We propose ReCo, a reweighting method that addresses both effects. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26862:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26865:start -->
`SF-2026-ARXIV-2607-26865` 的 exact-v1 Deep Review 已保留。其机制为：We propose Think Short, Defer Smart (TSDS), a framework that synergistically integrates a lightweight convergence probe, which halts on-device reasoning once the intended action has stabilized, with a perplexity-based deferral rule that escalates uncertain actions to a cloud-side model. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26865:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26903:start -->
`SF-2026-ARXIV-2607-26903` 的 exact-v1 Deep Review 已保留。其机制为：We introduce Pegasus, a low-resource framework that bridges this gap by translating human demonstrations into robot-learnable data through structured knowledge transfer. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26903:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26953:start -->
`SF-2026-ARXIV-2607-26953` 的 exact-v1 Deep Review 已保留。其机制为：This article proposes Reliability Assurance Intelligence (RAI), a general assurance architecture for such systems. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26953:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27017:start -->
`SF-2026-ARXIV-2607-27017` 的 exact-v1 Deep Review 已保留。其机制为：Which physical quantities does a trained latent actually contain, and what decides this? 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27017:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27031:start -->
`SF-2026-ARXIV-2607-27031` 的 exact-v1 Deep Review 已保留。其机制为：Moreover, prior work has not considered actual deployment conditions, where decision logic is already fixed for the incumbent. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27031:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27080:start -->
`SF-2026-ARXIV-2607-27080` 的 exact-v1 Deep Review 已保留。其机制为：To address this gap, we introduce MemSecBench, a task-grounded benchmark for the lifecycle security of agent memory systems. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27080:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27081:start -->
`SF-2026-ARXIV-2607-27081` 的 exact-v1 Deep Review 已保留。其机制为：To address these challenges, we propose Routing-based On-Policy Distillation (ROPD), a novel realignment framework that models the divergence between aligned and compromised output probability distributions rather than fitting specific prompt templates. 为避免挤压 `TRAIN-RLHF` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27081:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27083:start -->
`SF-2026-ARXIV-2607-27083` 的 exact-v1 Deep Review 已保留。其机制为：On $τ$-bench Retail, CAM-DF attains the highest payoff among deployable methods, with gains over a predict-then-threshold baseline across all five ranking sources and two cost regimes. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27083:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27090:start -->
`SF-2026-ARXIV-2607-27090` 的 exact-v1 Deep Review 已保留。其机制为：We present InferScale, a GPU-native LLM memory system that replaces repeated prompt prefilling with reusable KV state. 为避免挤压 `INFER-VLLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27090:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27180:start -->
`SF-2026-ARXIV-2607-27180` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we introduce HumanCLAW, an evaluation framework that decouples action decision-making from low-level execution. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27180:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27187:start -->
`SF-2026-ARXIV-2607-27187` 的 exact-v1 Deep Review 已保留。其机制为：The proposal treats KV capacity and bandwidth as one disaggregated-memory contract: sixteen CXL 3.1 Type-3 photonic memory modules expose a switch-free optical full crossbar, pooled DDR5 capacity, and HBM3E caching to multiple hosts. Host processes map the shared DAX region, GPU DMA moves KV payloads, and offset-addressed metadata coordinates allocation and reuse without assuming identical virtual addresses across hosts. 为避免挤压 `INFER-GPU-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27187:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27191:start -->
`SF-2026-ARXIV-2607-27191` 的 exact-v1 Deep Review 已保留。其机制为：We introduce a third way to measure progress towards AI R\&amp;D automation. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27191:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-27201:start -->
`SF-2026-ARXIV-2607-27201` 的 exact-v1 Deep Review 已保留。其机制为：We instantiate the framework in MENTIS, a training-free and fully inspectable baseline that decomposes the process into state parsing, target-observation generation, action decomposition, coupled physical and mental transition, and branch-level value evaluation. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-27201:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260730-01:start -->
### FinCacheServe: Dependency-Consistent Answer Reuse for Cost-Efficient RAG Serving over Mutable Enterprise Documents

**约束变化与机制。** FinCacheServe moves reuse above the model call: each answer is stored as a materialized serving object bound to normalized task identity, cited evidence hashes, source-document versions, tool-output fingerprints, model identity, and decoding configuration. A read-side gate checks those dependencies before reuse, while document updates first advance the version store and invalidate dependent answers through a reverse index; cache correctness is therefore separated from admission and eviction policy at one metadata-plane linearization point.

**证明与未证明。** Within the disclosed SEC-derived traces, Qwen2.5 7B/14B/32B serving environments, deterministic metadata fixtures, and stated 2 s SLO replay, the dependency gate produced zero observed dependency-stale answer serves while eliminating hosted model calls; the bounded-capacity and 100k-entry backend experiments additionally test admission, eviction, transactional invalidation, and metadata latency. The 44.30% Wh reduction is an estimate from archived request timing and explicit board-power assumptions, not direct whole-system energy measurement. 但 Dependency freshness is not factual answer correctness, and the paper does not establish the same hit rate, metadata cost, or concurrency behavior for unrelated corpora, tool graphs, models, or production failure domains. It also does not prove that its online utility estimator is optimal; the offline policy is only an oracle-like replay target. Unreported workload, model, hardware, precision, length, batch, concurrency, SLO, and evaluator fields remain Not Disclosed rather than inferred.

**Trade-off 与共存边界。** Answer-level reuse can remove both prefill and decode, but it transfers responsibility to version identity, evidence/tool fingerprints, reverse-index fan-out, invalidation ordering, and capacity policy. Conservative dependency gates trade stale hits for false misses and metadata overhead; ordinary KV/prefix caching remains the safer coexistence branch when requests do not repeat semantically, dependencies cannot be versioned, or answer reuse is disallowed by privacy/isolation policy. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-26076`。
<!-- analysis:DA-20260730-01:end -->

<!-- analysis:DA-20260730-02:start -->
### A Graph-Native Bitemporal Memory Store for Conversational AI Agents

**约束变化与机制。** The store separates immutable memory identity from mutable content: a stable Memory node owns graph relations, while append-only MemoryVersion nodes carry content, embeddings, tags, valid-time and transaction-time intervals. An update closes the current transaction interval and appends a new version instead of overwriting history; separate current-state and full-history HNSW indexes, plus interval filters, let the agent choose present-state or as-of retrieval through explicit tools.

**证明与未证明。** On the stated 60-question, seed-42 LongMemEval sample, the implementation shows that identity/version separation can preserve updates and expose current-state versus as-of queries. Current-state retrieval reaches 46.7% R@10 overall and 80% on knowledge-update questions, while the lower 37.5% time-travel result on eight non-null temporal cases exposes a concrete over-fetch-and-filter dilution failure rather than hiding it. 但 The experiment is not the full 500-question benchmark and does not demonstrate reliable multi-session aggregation, preference inference, or recall of assistant-generated content because only user turns are indexed. It also does not establish privacy, deletion compliance, multi-writer consistency, long-lived embedding migration, or production-scale graph/index cost. These are explicit system boundaries, not evidence that bitemporal storage alone solves agent memory.

**Trade-off 与共存边界。** Append-only versions make provenance, correction, and time travel explicit, but increase storage, interval/index maintenance, write amplification, and retrieval dilution. Keeping relationships on stable identity nodes avoids graph rewrites, yet assumes relationship meaning survives content revisions. A simpler current-state store remains appropriate when history has no product or audit value; derived counters, preference summaries, assistant turns, and re-ranking require separate owners rather than being inferred from raw retrieval. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-26520`。
<!-- analysis:DA-20260730-02:end -->

<!-- analysis:DA-20260730-03:start -->
### TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with &lt;1 GB VRAM

**约束变化与机制。** TurboVLA removes the generative LLM from the execution-frequency control path. A vision encoder and lightweight text encoder retain modality-specific features, bidirectional cross-attention performs task-conditioned fusion, robot state enters only at an ACT-style decoder, and parallel action queries emit a continuous action chunk in one forward pass. The claimed $V + L \to A$ path therefore narrows the execution model's responsibility instead of claiming that language reasoning is unnecessary everywhere.

**证明与未证明。** Under the disclosed LIBERO protocol (2,000 rollouts), RoboTwin clean-setting protocol, and real-platform task trials, the compact execution path remains competitive while reducing the measured deployment footprint. The headline 97.7% LIBERO average, 31.2 ms latency, and 0.9 GB inference VRAM are bound to the stated 0.2B configuration, single RTX 4090 and batch size one; ablations additionally show that language, bidirectional interaction depth, and semantic instruction encoding each contribute within that setup. 但 The results do not show that a compact execution policy can replace an LLM for open-ended planning, unseen embodiment transfer, long-horizon semantic decomposition, or safety assurance. RoboTwin training excludes randomized-scene data, and the author comparison does not make every baseline's pretraining data, optimization budget, and deployment stack identical. The evidence therefore supports an execution-layer branch, not universal VLA superiority.

**Trade-off 与共存边界。** Removing the LLM from every control tick reduces activation memory and latency, but deliberately gives up broad generative reasoning inside that loop and relies on compact encoders, grounding initialization, behavior-cloning data, fixed action chunks, and an external planner when instructions exceed execution-level semantics. LLM-centric VLA remains reasonable when high-level reasoning and open-vocabulary interpretation dominate; a hierarchical planner plus lightweight real-time controller is the coexistence boundary exposed by the paper itself. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-27205`。
<!-- analysis:DA-20260730-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260730-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260730 | GAP-20260730-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260730-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260730-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260730-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260730-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260730-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260730-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

331 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：25
- `incremental_method_without_durable_system_delta`：255
- `local_benchmark_without_release_delta`：11
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：4
- `vertical_application_without_system_delta`：35

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 60、No Change 75、Structural 1；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/30/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Large-Scale ChatBot Validation Through Customer Digital Twin Simulations](https://arxiv.org/html/2607.26060v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [The Age of AI Agents Demands A New Scientific Paradigm To Sustain Trustworthy Science](https://arxiv.org/html/2607.26064v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Do Methods Support the Claims? Intra-Paper Verification for Peer Review](https://arxiv.org/html/2607.26066v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SimpleWikiSearch: A Clean Offline Wikipedia Environment for Agentic Search](https://arxiv.org/html/2607.26070v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [FinCacheServe: Dependency-Consistent Answer Reuse for Cost-Efficient RAG Serving over Mutable Enterprise Documents](https://arxiv.org/html/2607.26076v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Meta-Learned Reward Shaping for Reinforcement Learning from Human Feedback](https://arxiv.org/html/2607.26094v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Lilith: Backdoor Generalization under Training-Inference Trigger Shift](https://arxiv.org/html/2607.26099v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [GPT-Red: Automated Red Teaming via Self-Play at Scale](https://arxiv.org/html/2607.26115v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Probing the Origins of Reasoning Performance: Representational Quality for Mathematical Problem-Solving in RL vs. SFT Fine-Tuned Models](https://arxiv.org/html/2607.26119v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Even More Deception: Objective Misalignment in Mixed-Motive LLM Multi-Agent Systems](https://arxiv.org/html/2607.26120v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Towards Trustworthy Embodied Intelligence: A Systems Framework and Graded Trustworthiness Levels](https://arxiv.org/html/2607.26121v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation](https://arxiv.org/html/2607.26148v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [When benchmark inferences do not compose: Projectibility in AI evaluation](https://arxiv.org/html/2607.26159v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning](https://arxiv.org/html/2607.26160v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models](https://arxiv.org/html/2607.26173v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [GoGoTB: Agentic RTL Verification with Specification-Grounded Coverage Closure](https://arxiv.org/html/2607.26181v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Position: Evaluation Scores Are Perishable Knowledge Claims](https://arxiv.org/html/2607.26191v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Dynamic Parameterization Is Not Dynamic Inference](https://arxiv.org/html/2607.26192v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting](https://arxiv.org/html/2607.26200v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Steering Instruction Hierarchies at Inference Time](https://arxiv.org/html/2607.26228v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Do Code Language Models Use Tests? A Behavioral and Representational Study of Test-Driven Code Generation](https://arxiv.org/html/2607.26244v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Weak-to-Strong On-Policy Distillation](https://arxiv.org/html/2607.26246v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Between Gradient and Natural Gradient: A Continuum of LoRA Initializations](https://arxiv.org/html/2607.26247v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Early Verdicts, Better Budgets: Sequential Adaptive Rollout Allocation for Compute-Efficient RLVR](https://arxiv.org/html/2607.26253v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [AgentGUI: An Interface for Observing and Steering Long-Running AI Agents](https://arxiv.org/html/2607.26300v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [TraceCoder: Explainable and Auditable Code Generation with Position-Key Snippet Versioning](https://arxiv.org/html/2607.26307v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SARC-DQ: Runtime Data-Quality Gating for Agentic AI: Silent Evidence Defects, the Incompetence Shield, and Downstream-Only Remediation](https://arxiv.org/html/2607.26313v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents](https://arxiv.org/html/2607.26314v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Seeing or Knowing? Visual Context Sensitivity in Multimodal Large Language Models](https://arxiv.org/html/2607.26326v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [The Fabric Is the Cluster Driver: Cross-Layer eBPF Policies for GPU-CXL Fabrics](https://arxiv.org/html/2607.26335v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Learning Implicit Causal World Models from Multi-Agent Demonstrations](https://arxiv.org/html/2607.26336v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [RAGuard: A Layered Defense Framework for Retrieval-Augmented Generation Systems Against Data Poisoning](https://arxiv.org/html/2607.26339v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Incast-Free MoE Rate-Based Scheduling](https://arxiv.org/html/2607.26340v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [When Synthetic Users Fail: A Cross-Domain Benchmark of LLM-Simulated Human Survey Responses](https://arxiv.org/html/2607.26348v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens](https://arxiv.org/html/2607.26350v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Post-Training at the Edge of Detectability: A Game-Theoretic Approach to Fine-Tuning](https://arxiv.org/html/2607.26358v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Misalignment Has a Personality: A Big Five Account of Emergent Misalignment](https://arxiv.org/html/2607.26389v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Impossible to hide secret ...: Uncovering Security and Privacy Issues in LLM-native IDEs](https://arxiv.org/html/2607.26390v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Voice Memory for Agentic Speech Recognition](https://arxiv.org/html/2607.26410v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Do Unified Multimodal Models Think in One Space? A Lens Through Cross-Branch Steering](https://arxiv.org/html/2607.26411v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SCOUT: Per-Context Reset Curricula for Sparse-Reward Reinforcement Learning](https://arxiv.org/html/2607.26417v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [StrataCL: Fabric-Native Communication Library for Production Supernodes](https://arxiv.org/html/2607.26444v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Mergeable Model-Side Aggregation States for Long-Context Language Models](https://arxiv.org/html/2607.26448v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/html/2607.26452v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [ForgetBench: Benchmarking Forgetting Dynamics of Long-Term Parametric Memory in Language Models](https://arxiv.org/html/2607.26455v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [PUDA: An AI-Native Hardware Harness for Self-Driving Laboratories](https://arxiv.org/html/2607.26464v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [CMT-RAG: Complementary Memory Traces for Multi-turn Multi-hop RAG](https://arxiv.org/html/2607.26470v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch](https://arxiv.org/html/2607.26475v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [LLMET: Enabling Cross-Layer Evaluation of Emerging M3D Memories for Energy-Efficient LLM Serving](https://arxiv.org/html/2607.26491v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Evidence-Ledger Adjudication for Claim-Evidence Traceability](https://arxiv.org/html/2607.26512v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Explicit Kinematic Guidance from Analytic Concepts for Vision-Language-Action Models](https://arxiv.org/html/2607.26513v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/html/2607.26515v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [A Graph-Native Bitemporal Memory Store for Conversational AI Agents](https://arxiv.org/html/2607.26520v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [The Art of Not Forgetting A Local Learning Architecture for Continual Learning](https://arxiv.org/html/2607.26523v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [TPCD: Tone-Pressure Contrastive Decoding and the Label-Free Gating Bottleneck in Vision-Language Models](https://arxiv.org/html/2607.26536v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [ServerlessT2I: Efficient Text-to-Image Workflow Serving on a Serverless Platform](https://arxiv.org/html/2607.26566v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [From Tokens to Watt-hours: Analytical Energy Estimation for LLM Inference on Modern GPUs](https://arxiv.org/html/2607.26571v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Level, Sharpness, and Corpus: Why Zero-Shot OOD Detector Rankings Do Not Transfer](https://arxiv.org/html/2607.26582v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [One Run Is Not an Idea: The Implementation Lottery in Automated Research](https://arxiv.org/html/2607.26587v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Decoupled Visual Processing: Efficient Multimodal Adaptation via Modality-Specific Transformer Substitution](https://arxiv.org/html/2607.26596v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [WikiLoop: Jointly Learning to Build and Navigate Agent-Native Wikis with Downstream Feedback](https://arxiv.org/html/2607.26604v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Understanding Knowledge Transfer Mechanism in Heterogeneous MLLM Fusion: A Simple Linear Approach](https://arxiv.org/html/2607.26608v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [FedWeave: Rethinking the Unit of Specialization in Heterogeneous Federated MoE-LoRA](https://arxiv.org/html/2607.26618v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Revisiting Lossy Verification in Speculative Decoding: Mechanisms, Trade-offs, and Failure Modes](https://arxiv.org/html/2607.26627v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-based Request Placement](https://arxiv.org/html/2607.26633v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability](https://arxiv.org/html/2607.26637v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Rethinking Self-Evolution: A Constrained Exploration-Exploitation Process for Mitigating Skill Overfitting](https://arxiv.org/html/2607.26643v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [The Sparsity Ceiling: Where Spiking Networks Can and Cannot Trade Activity for Energy](https://arxiv.org/html/2607.26648v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [AIGen: Automating AI Bill of Materials Generation Through Hybrid MLOps Integration](https://arxiv.org/html/2607.26652v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Constitutional Midtraining: Content Presence Drives Alignment Gains](https://arxiv.org/html/2607.26654v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control](https://arxiv.org/html/2607.26657v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [AgenticCANN: Automated Ascend C Operator Generation via Knowledge-Augmented Agentic Evolution](https://arxiv.org/html/2607.26661v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Nix to the Rescue for a Reproducible HPC-AI Software Stack](https://arxiv.org/pdf/2607.26688v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](https://arxiv.org/html/2607.26694v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [PowerAtlas: Towards Electricity-Computing Co-Scheduling for Power Systems](https://arxiv.org/html/2607.26710v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [ActSWM: Action-Sensitive World Models for Long-Horizon Planning in Open-World Games](https://arxiv.org/html/2607.26712v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Not In My Git Yard: Catching Backdoors at Commit and Release Time](https://arxiv.org/html/2607.26719v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [DREvo: Distilling Recalibrated Historical Experience for Harness Self-Evolution](https://arxiv.org/html/2607.26722v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation](https://arxiv.org/html/2607.26754v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Metis: Memory Foundation Model](https://arxiv.org/html/2607.26760v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [See2Think: Do Multimodal Models Really Use Intermediate Visual States?](https://arxiv.org/html/2607.26769v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Do Latent Channels Actually Communicate? A Causal Audit of Latent Multi-Agent LLM](https://arxiv.org/html/2607.26773v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [CodeSpec: Dual Executable Specifications for Agentic Long-Horizon Feature Development](https://arxiv.org/html/2607.26777v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution](https://arxiv.org/html/2607.26784v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [CheckVLA: Execution-Time Verification with Action-Conditioned World Model for Long-Horizon Mobile Manipulation](https://arxiv.org/html/2607.26789v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response](https://arxiv.org/html/2607.26791v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [FedTopo: Relation-Level Topology Sharing for Model-Heterogeneous Federated Learning](https://arxiv.org/html/2607.26801v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Route by Kinematics, Act by Observation: Kinematics-Supervised Expert Routing in MoE-Augmented VLA](https://arxiv.org/html/2607.26807v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations](https://arxiv.org/html/2607.26809v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Ripple: Real-Time Streaming Audio-Video Generation With Cross-Modal Recurrent Memory](https://arxiv.org/html/2607.26818v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities](https://arxiv.org/html/2607.26819v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Forecasting Trajectory-Level Safety Risks in Black-Box Multi-Turn Interactions](https://arxiv.org/html/2607.26820v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [From Found to Designed: Concepts as a Design Axis for Large Language Models](https://arxiv.org/html/2607.26825v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Budget-Aware LLM Discovery via Cost-Calibrated Frontier Utility](https://arxiv.org/html/2607.26828v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Language Models are not Equally Robust to Non-Canonical Tokenization across Languages](https://arxiv.org/html/2607.26831v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Agent Systems](https://arxiv.org/html/2607.26836v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [When Knowledge Changes: Metamorphic Testing of RAG Systems with Mutations](https://arxiv.org/html/2607.26843v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Thinking Under Uncertainty: Evidence Use and Information-Seeking in Language Models](https://arxiv.org/html/2607.26845v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [ToxScreen: Detecting Whether an LLM Has Been Poisoned](https://arxiv.org/html/2607.26849v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [ReCo: Reweighting GRPO Against Distributional Concentration](https://arxiv.org/html/2607.26862v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Think Short, Defer Smart, Act, and Repeat: Calibrated Reasoning and Uncertainty-Aware Deferral for Edge LLM Agents](https://arxiv.org/html/2607.26865v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning](https://arxiv.org/html/2607.26873v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [From Passive Video to Editable Experience: Physically Grounded Experience Synthesis for Embodied Intelligence](https://arxiv.org/html/2607.26903v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Prior Directions: Why GUI Grounding Gets Locked in the Past](https://arxiv.org/html/2607.26913v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models](https://arxiv.org/html/2607.26922v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Temporally Centered SIGReg Improves LeWorldModel Representations for Robot Policy Learning](https://arxiv.org/html/2607.26924v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Latent-IM: Latent Interaction Management for Speech LLMs](https://arxiv.org/html/2607.26928v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [What Does It Take to Detect an AI Agent? Minimal Feature Sets for Behavioral Detection under Browser Automation](https://arxiv.org/html/2607.26935v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [VITAL-RAG: Invariance Race for Context Allocation in Coding Agents](https://arxiv.org/html/2607.26937v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Assurance-Scoped Reliability for Agentic Networks: Capturing the State That Matters](https://arxiv.org/html/2607.26953v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [A Compositional Theory of Causally Masked Transformers](https://arxiv.org/html/2607.26988v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/html/2607.26991v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [AgentSnare: Learning to Delay, Divert, and Defuse Autonomous Penetration Agents](https://arxiv.org/html/2607.26998v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Qwen-Audio-3.0-Gen-Preview Technical Report](https://arxiv.org/html/2607.27011v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [What Can Latent World Models Know? Physical Parameter Identifiability in Multimodal Predictive Representations](https://arxiv.org/html/2607.27017v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [BayesAME: Bayesian Active Model Evaluation](https://arxiv.org/html/2607.27023v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models](https://arxiv.org/html/2607.27030v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Lottery Tickets Are Not Deployment Tickets](https://arxiv.org/html/2607.27031v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding](https://arxiv.org/html/2607.27042v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents over Heterogeneous Data](https://arxiv.org/html/2607.27056v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Visual Credit Audit for Multimodal Spatial Reasoning](https://arxiv.org/html/2607.27069v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [MemSecBench: Tracking Agent Memory Poisoning from Persistence to Consequence and Repair](https://arxiv.org/html/2607.27080v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [On-Policy Distillation for LLM Safety: A Routing Approach to Template-Robust Realignment](https://arxiv.org/html/2607.27081v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents](https://arxiv.org/html/2607.27083v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [InferScale: GPU-Native KV Injection for Personalized LLM Serving](https://arxiv.org/html/2607.27090v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring](https://arxiv.org/html/2607.27110v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Cost-Sensitive Conformal Prediction and Human-in-the-Loop Abstention for Imbalanced High-Stakes Decision Support: A Multi-Domain Benchmark](https://arxiv.org/html/2607.27143v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [MindForge: Teaching Small Language Models Whole-Life-Cycle Software Engineering via Source-Free Program Synthesis](https://arxiv.org/html/2607.27146v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding](https://arxiv.org/html/2607.27155v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [SpecFirst: Behavioral Specification Elicitation as a First-Class Step in Agent-Based Program Synthesis from Scratch](https://arxiv.org/html/2607.27167v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [DenseOn with the LateOn: Fully Open Dense and Late-Interaction Models for Multilingual, Long-Context, and Code Search](https://arxiv.org/html/2607.27178v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/html/2607.27180v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [A Photonic-CXL Memory Appliance for Scalable KV Cache Management in LLM Inference](https://arxiv.org/pdf/2607.27187v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Can AI agents conduct open-ended AI research? Early evidence from two case studies](https://arxiv.org/html/2607.27191v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [Mental World Modeling](https://arxiv.org/html/2607.27201v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03
- [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with &lt;1 GB VRAM](https://arxiv.org/html/2607.27205v1) — first-public（Asia/Shanghai）：2026-07-30；exact evidence：v1；accessed：2026-09-03

## 13. Final Status

Author-side screening、denominator、exact-v1 access、136/136 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
